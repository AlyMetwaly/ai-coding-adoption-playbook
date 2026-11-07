# 06 Worked example

This is a simulated six-week pilot. It shows how the guides, the scorecard and the decision review connect, and how to reach a decision from incomplete evidence. Every person, team, number and event here is invented. It is not a customer case study and it does not claim any productivity result. The two data files are synthetic: `data/worked_example_week3.csv` and `data/worked_example_week6.csv`.

## Checklist

- [ ] You have read `01-align.md` and `04-measure.md`.
- [ ] You can run `python tools/adoption_scorecard` on the two data files.
- [ ] You keep the simulated events apart from anything you would claim about a real rollout.

## The setup (simulated)

A 40-person engineering organization starts a six-week pilot with 12 developers on two teams. Team API maintains a TypeScript service. Team Tools maintains a Python internal tool. All 12 licenses were assigned on the same day.

Decisions made in week 0, with the owner and the reason:

| Decision | Reason | Cost | Revisit |
|---|---|---|---|
| Authentication, payment and infrastructure code are out of scope | The data and security review does not cover them yet | Some useful tasks are off the table | End of week 3 |
| Repository-wide indexing is off in week 1 | Not every in-scope repository has been reviewed (verify against current Cursor docs) | Weaker context, weaker first results | After the security owner signs off |
| Two champions, planning range of one to two hours a week | Support must stay inside the rollout team's capacity | Champions have less time for delivery | Week 3 |
| Triggers for expansion are written down now | Avoid choosing thresholds after seeing the data | None | Not moved unless logged |

Triggers set in week 0 (examples for this simulation only, not benchmarks): sustained use in both teams above the level the sponsor agreed, no unresolved security item, review wait no worse than the baseline.

## Week 3 report

Command:

```bash
python tools/adoption_scorecard data/worked_example_week3.csv
```

The scorecard reports, from the synthetic file:

| Signal | Week 3 |
|---|---|
| Activated | 10 of 12 users |
| Weekly active | 6 of 12 users |
| Sustained | 6 of 12 users (Team API 4 of 7, Team Tools 2 of 5) |
| Agent use | 40% of active users |
| Flags | None at the example thresholds |

How the rollout owner read it:

- Half the licensed users are sustained. That is not yet a story. The pilot is only three weeks old and the groups are small, so counts matter more than rates.
- Activated is 10 and sustained is 6. The gap is the group to talk to, not a number to chase.
- No flag fired. That is not evidence of health. It only means nothing crossed an example threshold.

Actions taken (simulated): the owner interviewed the four users who were activated but not sustained. Two said they could not find a first task. One said a long setup step was in the way. One said reviewers on the team did not trust the output.

## Week 6 report

Command:

```bash
python tools/adoption_scorecard data/worked_example_week6.csv --previous data/worked_example_week3.csv
```

| Signal | Week 3 | Week 6 |
|---|---|---|
| Activated | 10 of 12 | 11 of 12 |
| Weekly active | 6 of 12 | 7 of 12 |
| Sustained | 6 of 12 | 6 of 12 |
| Team API sustained | 4 of 7 | 5 of 7 (trend up) |
| Team Tools sustained | 2 of 5 | 1 of 5 (trend down) |
| Agent use | 40% of active users | 50% of active users |

Read each line against its companion metric:

- Overall sustained did not move. The total hides two opposite trends, so the team table matters more than the total.
- Team API improved. Team Tools got worse. With five users in Team Tools, one person changing habits moves the rate by 20 points. Read counts, not a trend.
- Agent use went up. That is reported, not rewarded. The score does not treat it as better use.
- Nothing here says whether delivery improved. The scorecard has no outcome data.

## Outcome check (simulated)

Using the decision review template, the rollout owner compared pull request cycle time and review rework for matched work, because those were already tracked.

| Outcome | Baseline | Current | What else could explain it? |
|---|---|---|---|
| Pull request cycle time, Team API | Collected before the pilot | Slightly shorter | A release freeze ended in week 4 |
| Review rework, Team API | Collected before the pilot | Higher | Reviewers read agent-made diffs more carefully, and two diffs were too large |
| Pull request cycle time, Team Tools | Collected before the pilot | No clear change | Only one person uses the tool steadily |

The owner wrote, in the decision review, that cycle time is associated with the pilot but that the evidence cannot separate it from the end of the freeze, and that higher review rework is a quality warning to investigate.

## Review finding (simulated)

An agent-made change to the Team API service passed its tests. In review, the reviewer found that it also changed a shared validation function used by another endpoint. The tests did not cover that endpoint. The author had not noticed.

What changed afterward:

- The review gate now asks the agent to list every file touched and why, and the reviewer checks callers of any shared function.
- A rule was added to the team's rules file: changes to shared helpers need a note on who calls them.
- The change was split into two coherent pull requests, each reviewable as one unit.

This is the kind of failure the guides expect. It is simulated, so use it as a pattern, not as a statistic.

## Decision (simulated)

Using the decision tree in `05-expand.md`:

1. Unresolved security blocker: no.
2. Outcome guardrails worse than baseline: review rework is higher. The owner treated this as a warning, not yet a failure, and logged it.
3. Sustained below the trigger in one pilot team: yes. Activated is high and sustained is low in Team Tools, which points to weak onboarding or poor task fit.

Decision: hold the seat count, fix the review bottleneck and the Team Tools onboarding, and review again in four weeks. Do not add seats.

## What this example shows

- Totals can hide opposite team trends.
- A flag that does not fire is not proof of health.
- A usage number is never proof of an outcome.
- A decision can be "hold" and still be a good, evidence-based decision.

To try it on your own data, copy the column layout from the README and run the scorecard on your own export.
