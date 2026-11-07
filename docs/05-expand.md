# 05 Expand

This guide helps you decide when to add more teams or seats, when to wait, when to fix problems first, and when to stop. It covers expansion triggers, stop conditions, seat and cost planning, a 30-minute executive review, how to work with an account executive or vendor partner, failure patterns and a decision tree. Use it after at least one full cycle of measurement.

## Checklist

- [ ] Expansion triggers are written down before the review, not during it.
- [ ] Each threshold was chosen with the method in "How to choose a threshold".
- [ ] The scorecard report for the review period is ready. See `04-measure.md`.
- [ ] The decision log from `01-align.md` is up to date.
- [ ] Stop conditions are agreed, with a decision owner for each.
- [ ] Seat and cost tracking follows "Seat and cost planning".
- [ ] The executive review is on the calendar with a fixed agenda.
- [ ] You know what you will and will not share with the vendor.
- [ ] Pricing, seat and plan terms are checked (verify against current Cursor docs).
- [ ] The decision is recorded: expand, hold, fix first, or pause.

## Expansion triggers

Example only. These are not benchmarks or recommended targets.

| Trigger | Example threshold | Why it matters |
|---|---|---|
| Sustained rate in pilot teams | Above a level the sponsor agreed on in week 0 | Shows habits, not trials |
| Depth | Example only: active users work in more than one way (completions, chat, agent tasks) where it fits their work. | Shows use fits the work, not only one feature |
| Outcome guardrails | Review time and defect signals are no worse than baseline | Shows speed did not cost quality |
| Support load | Questions in office hours are falling or getting more advanced | Shows people are self-sufficient |
| Champion workload | Champions stay within the planning range, tracked separately | Shows the model scales |
| Review capacity | Median review wait is stable | Shows reviewers can cope |
| Open risks | No unresolved high security or privacy items | Shows it is safe to widen |

Rules for triggers:

- Require several triggers together. One strong metric is not enough.
- Write the threshold and the date you set it.
- Do not move a threshold after seeing the data, unless you log why.
- Small teams are noisy. Use counts, not only rates.
- Never present agent use as better by itself. Depth means the tool fits the work.

**How to choose a threshold.** Set it from the decision it controls, the support capacity you have, the risk of expanding, and your pilot baseline. Do not pick it because another organization used it.

## Stop conditions

Pause the pilot if the tool causes a confirmed sensitive-data exposure, repeated policy violations, material review overload, an unacceptable defect pattern, or a loss of engineering trust that the rollout team cannot correct. Record the decision owner and the conditions required to restart.

| Condition | Who decides | Evidence | Restart condition |
|---|---|---|---|
| Confirmed sensitive-data exposure | Security lead | Incident record: what data, which setting or path, who was affected | Cause fixed, settings re-checked (verify against current Cursor docs), security lead signs off in writing |
| Repeated policy violations | Rollout owner with the security lead | Logged violations by type and team | Policy restated, controls added, review of the log after an agreed period shows no repeats |
| Material review overload | Engineering lead | Review wait and reviewer reports compared with baseline | Scope narrowed or review capacity added, review gates tightened |
| Unacceptable defect pattern | Engineering lead | Defects and rework traced to tool-assisted changes, with the limits of attribution stated | Cause found, gates or scope changed, outcome re-measured over one full cycle |
| Loss of engineering trust | Sponsor with the engineering lead | Survey and interview themes, champion notes | Concerns answered in writing, restart with volunteer teams first |

## Seat and cost planning

Track five seat counts every month:

- **Paid.** Seats you are billed for.
- **Assigned.** Seats given to a named person.
- **Activated.** Assigned people with any recorded use.
- **Weekly active.** Assigned people with use in the latest 7 days.
- **Sustained.** Assigned people weekly active in at least 3 of the last 4 weeks. See `04-measure.md`.

Plan and pricing terms, billing units and usage-based charges change, so verify against current Cursor docs. This guide gives no prices.

Reassignment rules:

- Write the rule before launch. Example: a seat with no activation after an agreed period goes back to the pool.
- Tell the person and their manager before you reassign. Do it without blame.
- Let people ask for a seat again later.
- Count departed people off the list at once.

```text
monthly program cost = license cost
                     + rollout staff time
                     + champion time
                     + support time
                     + additional review time
```

Do not report license price as total rollout cost. Include internal rollout, support, champion and review capacity. Report cost per assigned seat and cost per sustained user separately.

## Executive review agenda (30 minutes)

Send the decision review (`templates/decision-review.md`) two days before. Do not read it aloud.

| Minutes | Item | Owner |
|---|---|---|
| 0 to 3 | Goal and decision requested | Sponsor |
| 3 to 10 | Funnel and depth: what moved, what did not | Rollout owner |
| 10 to 15 | Outcomes against baseline, and what we cannot attribute | Engineering lead |
| 15 to 20 | Risks, cost and open issues | Rollout owner |
| 20 to 27 | Options: expand, hold, fix first, pause | Sponsor |
| 27 to 30 | Decision, owners, next review date | Sponsor |

After the meeting, record the decision in the log and share it within a day.

## Working with an account executive or vendor partner

A vendor partner can help with plan questions, admin settings and training. They are not neutral on seat counts. Be clear about what you share.

Use vendor data to understand product activity and feature use. Do not use it as independent proof of productivity, quality or business value. Ask for field definitions, retention periods, exclusions, data latency, export options and changes to metric definitions. The account executive has an incentive to support expansion.

**Share**

- Your goals and success criteria.
- Aggregated adoption counts and the definitions behind them.
- Blockers you want help with, such as sign-in, admin controls or privacy settings.
- Your rollout schedule and the decisions coming up.
- Feedback on product gaps, with examples that contain no private code.

**Do not share**

- Source code, prompts or screenshots that contain private information.
- Names of individuals and their usage.
- Internal security findings or incident details.
- Your budget ceiling before you have to.
- Draft reports that include unattributed claims.

**Ask for**

- Current plan terms, limits and admin options (verify against current Cursor docs).
- Written answers on data handling.
- A named contact and a response time for blockers.
- A clear view of how seats and usage-based costs are billed.

Trade-off: sharing more helps the vendor help you, and it also gives them more room to push on pricing. Share outcomes and blockers, hold back budget and individual data.

## Failure patterns

These three cases are illustrative. They are not findings from a study.

**1. Activity without a change in delivery**

- Pattern: high weekly activity that is mostly chat questions and code explanation.
- What it looks like: weekly active is high, but the work that ships looks the same as before.
- Response: keep the pilot open and do not add seats. Pick two repeatable engineering workflows and check whether they survive review.

**2. One team carries the usage**

- Pattern: most usage comes from one team.
- What it looks like: the other pilot teams show low sustained use, while one team looks like a success.
- Response: investigate task fit and access before coaching. The cause may be the work, a setup gap or a missing permission, not the people.

**3. Speed up, quality down**

- Pattern: speed improves while review load and rework rise.
- What it looks like: pull requests open and merge faster, but reviewers report more effort and more follow-up fixes.
- Response: pause expansion, tighten review gates, re-measure. See `03-embed.md`.

## Decision tree: expand, hold, fix first, or pause

If a stop condition is met, **pause** first. See "Stop conditions". Otherwise work through the questions in order. Stop at the first match.

1. Is there an unresolved security, privacy or legal blocker?
   - Yes: **Fix first.** Close it before any expansion.
   - No: go to 2.
2. Did outcome guardrails get worse than baseline?
   - Yes: **Fix first.** Tighten review gates, see `03-embed.md`, and re-check after a cycle.
   - No: go to 3.
3. Is sustained use below your trigger in the pilot teams?
   - Yes: go to 3a.
   - No: go to 4.
   - 3a. Is activated high while sustained is low? Likely trials or weak onboarding. **Fix first** with `02-enable.md`.
   - 3b. Are both low? Likely weak fit or no sponsor push. **Hold** and revisit the use cases.
4. Is depth below your trigger?
   - Yes: **Hold** the seat expansion. Low depth means coach with champions and check task fit. Agent use is not the goal. Then re-check.
   - No: go to 5.
5. Can champions, reviewers and support absorb more teams?
   - No: **Hold** until capacity is added.
   - Yes: go to 6.
6. Is there a budget owner and a cost view for the next wave?
   - No: **Fix first.** Set the budget and alerts, verify against current Cursor docs.
   - Yes: **Expand.** Pick the next teams, copy the pilot plan, and set new triggers.

After any outcome, set the next review date and write the reason in the decision log.

Next step: see the simulated pilot in `06-worked-example.md`, then record your decision, set the next review date, and run the next wave from `02-enable.md`.
