# 05 Expand

This guide helps you decide when to add more teams or seats, when to wait, and when to fix problems first. It covers expansion triggers, a 30-minute executive review, how to work with an account executive or vendor partner, and a decision tree. Use it after at least one full cycle of measurement.

## Checklist

- [ ] Expansion triggers are written down before the review, not during it.
- [ ] The scorecard for the review period is ready. See `04-measure.md`.
- [ ] The decision log from `01-align.md` is up to date.
- [ ] The executive review is on the calendar with a fixed agenda.
- [ ] You know what you will and will not share with the vendor.
- [ ] Pricing, seat and plan terms are checked (verify against current Cursor docs).
- [ ] The decision is recorded: expand, hold, or fix first.

## Expansion triggers

Set each threshold yourself. The numbers below are hypothetical examples only.

| Trigger | Example threshold (hypothetical) | Why it matters |
|---|---|---|
| Sustained rate in pilot teams | Example: above a level the sponsor agreed on in week 0 | Shows habits, not trials |
| Depth | Example: most active users have run agent sessions | Shows use beyond completions |
| Outcome guardrails | Example: review time and defect signals are no worse than baseline | Shows speed did not cost quality |
| Support load | Example: questions in office hours are falling or getting more advanced | Shows people are self-sufficient |
| Champion health | Example: champions stay within their agreed hours | Shows the model scales |
| Review capacity | Example: median review wait is stable | Shows reviewers can cope |
| Open risks | Example: no unresolved high security or privacy items | Shows it is safe to widen |

Rules for triggers:

- Require several triggers together. One strong metric is not enough.
- Write the threshold and the date you set it.
- Do not move a threshold after seeing the data, unless you log why.
- Small teams are noisy. Use counts, not only rates.

## Executive review agenda (30 minutes)

Send the one-pager two days before. Do not read it aloud.

| Minutes | Item | Owner |
|---|---|---|
| 0 to 3 | Goal and decision requested | Sponsor |
| 3 to 10 | Funnel and depth: what moved, what did not | Rollout owner |
| 10 to 15 | Outcomes against baseline, and what we cannot attribute | Engineering lead |
| 15 to 20 | Risks, cost and open issues | Rollout owner |
| 20 to 27 | Options: expand, hold, fix first | Sponsor |
| 27 to 30 | Decision, owners, next review date | Sponsor |

After the meeting, record the decision in the log and share it within a day.

## Working with an account executive or vendor partner

A vendor partner can help with plan questions, admin settings and training. They are not neutral on seat counts. Be clear about what you share.

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

## Decision tree: expand, hold, or fix first

Work through the questions in order. Stop at the first match.

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
   - Yes: **Hold** the seat expansion. Coach with champions, then re-check.
   - No: go to 5.
5. Can champions, reviewers and support absorb more teams?
   - No: **Hold** until capacity is added.
   - Yes: go to 6.
6. Is there a budget owner and a cost view for the next wave?
   - No: **Fix first.** Set the budget and alerts, verify against current Cursor docs.
   - Yes: **Expand.** Pick the next teams, copy the pilot plan, and set new triggers.

After any outcome, set the next review date and write the reason in the decision log.
