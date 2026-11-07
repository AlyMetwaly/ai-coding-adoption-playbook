"""Generate data/sample_usage.csv. The data is synthetic.

Seeded, so the output is the same every run. Nothing here comes from a real
organization, team or person. Team names and user ids are made up.

Run from the repo root: python tools/generate_sample.py
"""

from __future__ import annotations

import csv
import random
import sys
from datetime import date, timedelta
from pathlib import Path

SEED = 7
AS_OF = date(2025, 6, 30)
OUT = Path(__file__).resolve().parent.parent / "data" / "sample_usage.csv"

# name, users, chance of ever using it, typical active days, chance of agent use
TEAMS = [
    ("team-alpha", 30, 0.95, 16, 0.70),
    ("team-bravo", 28, 0.90, 11, 0.45),
    ("team-charlie", 24, 0.75, 8, 0.30),
    ("team-delta", 22, 0.55, 5, 0.15),
    ("team-echo", 16, 0.40, 3, 0.05),
]
HEADER = [
    "user_id",
    "team",
    "licensed_date",
    "last_active_date",
    "active_days_last_28",
    "agent_sessions_last_28",
    "accepted_suggestions_last_28",
]


def build_rows(seed: int = SEED) -> list[list[str]]:
    rng = random.Random(seed)
    rows: list[list[str]] = []
    number = 1
    for team, count, p_active, typical_days, p_agent in TEAMS:
        for _ in range(count):
            licensed = date(2025, 1, 6) + timedelta(days=rng.randint(0, 140))
            last_active: date | None = None
            active_days = agent = accepted = 0
            if rng.random() < p_active:
                # Most active users were seen recently. Some drifted away.
                days_ago = int(rng.expovariate(1 / 6))
                last_active = max(licensed, AS_OF - timedelta(days=days_ago))
                if (AS_OF - last_active).days <= 27:
                    active_days = max(1, min(28, round(rng.gauss(typical_days, 4))))
                    if rng.random() < p_agent:
                        agent = rng.randint(1, 20)
                    if rng.random() < 0.9:
                        accepted = rng.randint(5, 200)
            rows.append(
                [
                    f"u{number:03d}",
                    team,
                    licensed.isoformat(),
                    last_active.isoformat() if last_active else "",
                    str(active_days),
                    str(agent),
                    str(accepted),
                ]
            )
            number += 1
    return rows


def main() -> int:
    OUT.parent.mkdir(parents=True, exist_ok=True)
    with OUT.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle, lineterminator="\n")
        writer.writerow(HEADER)
        writer.writerows(build_rows())
    print(f"wrote {OUT}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
