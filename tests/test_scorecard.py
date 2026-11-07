"""Tests for the adoption scorecard. All data in this file is synthetic."""

from __future__ import annotations

from datetime import date

import pytest

from adoption_scorecard.cli import main
from adoption_scorecard.core import (
    compute_depth,
    compute_funnel,
    compute_health,
    compute_teams,
    early_warning_flags,
    is_sustained,
    is_weekly_active,
    load_csv_text,
    parse_rows,
    previous_team_rates,
    resolve_as_of,
)
from adoption_scorecard.report import render_report

AS_OF = date(2025, 6, 30)
HEADER = (
    "user_id,team,licensed_date,last_active_date,active_days_last_28,"
    "agent_sessions_last_28,accepted_suggestions_last_28"
)


def row(user_id="u1", team="t1", licensed="2025-01-10", last="2025-06-29", days="10", agent="0", acc="0", **extra):
    base = {
        "user_id": user_id,
        "team": team,
        "licensed_date": licensed,
        "last_active_date": last,
        "active_days_last_28": days,
        "agent_sessions_last_28": agent,
        "accepted_suggestions_last_28": acc,
    }
    base.update(extra)
    return base


def users_from(*rows):
    return parse_rows(rows).users


def test_empty_file_is_an_error():
    with pytest.raises(ValueError, match="empty"):
        load_csv_text("")


def test_header_only_file_gives_empty_report():
    parsed = load_csv_text(HEADER + "\n")
    assert parsed.users == ()
    report = render_report(parsed)
    assert "No users in the file" in report
    assert "n/a (no users)" in report


def test_missing_columns_are_named():
    with pytest.raises(ValueError, match="agent_sessions_last_28"):
        load_csv_text("user_id,team\nu1,t1\n")


def test_all_inactive_users():
    users = users_from(
        row("u1", last="", days="0"),
        row("u2", last="", days="0"),
    )
    when = resolve_as_of(users)
    funnel = compute_funnel(users, when)
    assert (funnel.licensed, funnel.activated, funnel.weekly_active, funnel.sustained) == (2, 0, 0, 0)
    depth = compute_depth(users)
    health = compute_health(users, funnel)
    assert health.score == 0  # nobody used it, and balance is left out for one team
    assert health.balance_applies is False
    flags = early_warning_flags(users, funnel, depth)
    assert flags and flags[0].startswith("Activation is below")


def test_single_team_has_no_balance_penalty_or_flag():
    users = users_from(row("u1", days="20"), row("u2", days="1"))
    funnel = compute_funnel(users, AS_OF)
    depth = compute_depth(users)
    health = compute_health(users, funnel)
    assert health.balance_applies is False
    assert 0 < health.score <= 100
    assert not any("One team carries" in f for f in early_warning_flags(users, funnel, depth))


def test_malformed_values_are_skipped_and_listed():
    parsed = parse_rows(
        [
            row("ok"),
            row("bad-date", licensed="2025-13-40"),
            row("bad-last", last="yesterday"),
            row("negative", days="-3"),
            row("too-many-days", days="40"),
            row("not-a-number", agent="many"),
            row("", team="t1"),
        ]
    )
    assert [u.user_id for u in parsed.users] == ["ok"]
    assert len(parsed.skipped) == 6
    assert parsed.skipped[0][0] == 3  # first bad row is file line 3


def test_duplicate_user_ids_keep_the_first_row():
    parsed = parse_rows([row("u1", days="5"), row("u1", days="9")])
    assert len(parsed.users) == 1
    assert parsed.users[0].active_days == 5
    assert "duplicate" in parsed.skipped[0][1]


def test_last_active_before_license_is_skipped():
    parsed = parse_rows([row("u1", licensed="2025-06-01", last="2025-05-01")])
    assert parsed.users == ()
    assert "before licensed_date" in parsed.skipped[0][1]


def test_weekly_active_window_boundary():
    inside = users_from(row("a", last="2025-06-24"))[0]  # 6 days before
    outside = users_from(row("b", last="2025-06-23"))[0]  # 7 days before
    assert is_weekly_active(inside, AS_OF) is True
    assert is_weekly_active(outside, AS_OF) is False


def test_sustained_proxy_needs_recent_and_enough_days():
    steady = users_from(row("a", last="2025-06-29", days="8"))[0]
    light = users_from(row("b", last="2025-06-29", days="7"))[0]
    lapsed = users_from(row("c", last="2025-06-01", days="20"))[0]
    assert is_sustained(steady, AS_OF) is True
    assert is_sustained(light, AS_OF) is False
    assert is_sustained(lapsed, AS_OF) is False


def test_sustained_uses_weekly_column_when_present():
    users = users_from(
        row("a", days="2", active_weeks_last_4="3"),
        row("b", days="25", active_weeks_last_4="2"),
    )
    assert is_sustained(users[0], AS_OF) is True
    assert is_sustained(users[1], AS_OF) is False


def test_funnel_counts_are_nested():
    users = users_from(
        row("a", last="2025-06-29", days="12"),  # sustained
        row("b", last="2025-06-28", days="2"),  # weekly active only
        row("c", last="2025-05-01", days="0"),  # activated only
        row("d", last="", days="0"),  # licensed only
    )
    funnel = compute_funnel(users, AS_OF)
    assert (funnel.licensed, funnel.activated, funnel.weekly_active, funnel.sustained) == (4, 3, 2, 1)


def test_team_rows_median_and_rates():
    users = users_from(
        row("a1", team="alpha", days="20"),
        row("a2", team="alpha", days="10"),
        row("a3", team="alpha", days="0", last=""),
        row("b1", team="bravo", days="3"),
    )
    teams = {t.team: t for t in compute_teams(users, AS_OF)}
    assert teams["alpha"].users == 3
    assert teams["alpha"].median_active_days == 10
    assert teams["alpha"].sustained == 2
    assert teams["bravo"].sustained == 0
    assert teams["alpha"].trend == "n/a"


def test_trend_compares_with_previous_snapshot():
    now = users_from(
        row("a1", team="alpha", days="12"),
        row("b1", team="bravo", days="2"),
        row("c1", team="charlie", days="12"),
    )
    before = users_from(
        row("a1", team="alpha", days="2"),
        row("b1", team="bravo", days="12"),
        row("c1", team="charlie", days="12"),
    )
    previous = previous_team_rates(before, AS_OF)
    trends = {t.team: t.trend for t in compute_teams(now, AS_OF, previous)}
    assert trends == {"alpha": "up", "bravo": "down", "charlie": "flat"}
    new_team = compute_teams(users_from(row("z1", team="zulu")), AS_OF, previous)
    assert new_team[0].trend == "new"


def test_depth_splits_agent_completions_and_nothing():
    users = users_from(
        row("a", days="5", agent="3", acc="40"),
        row("b", days="5", agent="0", acc="40"),
        row("c", days="5", agent="0", acc="0"),
        row("d", days="0", last="", agent="0", acc="0"),
    )
    depth = compute_depth(users)
    assert (depth.active_users, depth.agent_users, depth.completions_only_users, depth.no_acceptance_users) == (
        3,
        1,
        1,
        1,
    )


def test_health_score_stays_between_0_and_100_and_rewards_better_use():
    weak = users_from(row("a", last="2025-04-01", days="1"), row("b", last="", days="0"))
    strong = users_from(
        row("a", team="t1", days="20", agent="5", acc="50"),
        row("b", team="t2", days="20", agent="5", acc="50"),
    )
    scores = []
    for users in (weak, strong):
        when = resolve_as_of(users)
        funnel = compute_funnel(users, when)
        scores.append(compute_health(users, funnel).score)
    assert 0 <= scores[0] < scores[1] <= 100


def test_one_team_carrying_usage_raises_a_flag():
    users = users_from(
        row("a", team="big", days="25", agent="4", acc="10"),
        row("b", team="big", days="25", agent="4", acc="10"),
        row("c", team="small", days="1", agent="1", acc="10"),
    )
    funnel = compute_funnel(users, AS_OF)
    flags = early_warning_flags(users, funnel, compute_depth(users))
    assert any("One team (big)" in f for f in flags)


def test_flags_are_capped_at_three():
    users = users_from(
        row("a", team="big", days="25", last="2025-06-29"),
        row("b", team="small", days="0", last=""),
        row("c", team="small", days="0", last=""),
    )
    funnel = compute_funnel(users, AS_OF)
    assert len(early_warning_flags(users, funnel, compute_depth(users))) <= 3


def test_report_has_all_sections_and_the_formula():
    parsed = load_csv_text(
        HEADER + "\nu1,t1,2025-01-10,2025-06-29,10,2,40\nu2,t2,2025-01-10,2025-06-20,3,0,10\n"
    )
    report = render_report(parsed, source_label="test.csv")
    for heading in ("## 1. Funnel", "## 2. By team", "## 3. Depth", "## 4. Adoption signal", "## 5. What each metric can hide"):
        assert heading in report
    assert "signal = 100 x (" in report
    assert "The fallback is a heuristic" in report


def test_report_lists_skipped_rows():
    parsed = load_csv_text(HEADER + "\nu1,t1,2025-01-10,2025-06-29,10,2,40\nu2,t1,not-a-date,,0,0,0\n")
    report = render_report(parsed)
    assert "## Rows skipped" in report
    assert "line 3: bad licensed_date" in report


def test_cli_prints_report_and_returns_zero(tmp_path, capsys):
    path = tmp_path / "usage.csv"
    path.write_text(HEADER + "\nu1,t1,2025-01-10,2025-06-29,10,2,40\n", encoding="utf-8")
    assert main([str(path)]) == 0
    assert "# Adoption scorecard: usage.csv" in capsys.readouterr().out


def test_cli_reports_bad_input_with_exit_code_2(tmp_path, capsys):
    path = tmp_path / "usage.csv"
    path.write_text("", encoding="utf-8")
    assert main([str(path)]) == 2
    assert "error:" in capsys.readouterr().err


def test_cli_missing_file_exits_2(tmp_path, capsys):
    assert main([str(tmp_path / "nope.csv")]) == 2
    assert "error:" in capsys.readouterr().err


def test_cli_writes_to_out_file(tmp_path):
    path = tmp_path / "usage.csv"
    out = tmp_path / "report.md"
    path.write_text(HEADER + "\nu1,t1,2025-01-10,2025-06-29,10,2,40\n", encoding="utf-8")
    assert main([str(path), "--out", str(out)]) == 0
    assert out.read_text(encoding="utf-8").startswith("# Adoption scorecard")
