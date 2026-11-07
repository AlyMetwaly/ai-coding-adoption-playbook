# 02 Enable

This guide helps you get people from "has a license" to "uses it on real work in week one". It covers onboarding paths by role, a first-week plan, office hours, a champion program, and the usual reasons people drop off. Use it after `01-align.md` is done.

## Checklist

- [ ] Each role has a short onboarding path with one real task.
- [ ] The first-week plan is published and has dated sessions.
- [ ] Agent-style work starts only after the readiness conditions under the first-week plan are met.
- [ ] Office hours have an intake format, a triage rule, an owner and an escalation path.
- [ ] Champions are chosen with clear criteria and a planning limit on their load.
- [ ] Champion workload is tracked separately from rollout support.
- [ ] A champion kit exists and is in one shared place.
- [ ] You have a way to contact people who go quiet after week two.
- [ ] Setup steps are tested on a clean machine (verify against current Cursor docs).

## Principles

- Start with real work, not demos. People learn on tasks they care about.
- Keep the first win small. A fixed test or a clear explanation counts.
- Teach checking as much as asking. Reviewing output is the core skill.
- Never shame low use. Ask what is in the way.

## Onboarding paths by role

| Role | First task | What to teach | Watch out for |
|---|---|---|---|
| New graduate | Explain an unfamiliar module, then fix a small bug | Ask for explanations, check claims, read diffs | Accepting output they cannot explain |
| Experienced engineer or tech lead | Refactor a function with tests running, then review a diff made with the tool | Writing precise prompts, rules files, scoping tasks, team rules, review gates | Dismissing the tool after one weak result, or becoming the only reviewer |
| Manager | Summarize a codebase area, write a status draft | What the tool can and cannot do, how to read the metrics | Asking for numbers that reward clicking |
| Non-coding role (design, product, support, data) | Read code to answer a question, or edit a doc or script | Safe boundaries, asking engineers for review | Pushing changes without review |

Tips for every path:

- Pair each person with a named champion for the first two weeks.
- Give one task from the person's own backlog.
- End each path with the person showing one result to a peer.
- Say which repos and data are allowed. See the scope answer from `01-align.md`.

## First-week plan

Adjust the times. The shape matters more than the clock.

| Day | Activity | Output |
|---|---|---|
| Day 1 | Setup, sign-in, privacy settings, a 45-minute guided session | Tool works on the person's machine |
| Day 2 | One real task with a champion nearby | One small change or explanation |
| Day 3 | Learn rules files and shared team assets, verify against current Cursor docs | Person reads the team rules |
| Day 4 | Review practice: read and review an agent-made diff together | Reviewed example, agent work only if the readiness conditions are met |
| Day 5 | Office hours and a short retro | Written list of questions and blockers |

Introduce agent-style work only after access, data handling, task boundaries and review expectations are clear. For some teams that is day four. For others it should wait.

## Office hours design

Office hours are a support service with limits. Run them like one.

- **Intake format.** One form or thread with four fields: the task, the repo area (no private code pasted), what was tried, and what is blocking.
- **Triage.** Sort each item into setup and access, usage question, policy question, or product bug. Answer it in the session, route it, or log it.
- **Owner.** A named member of the rollout team runs each session. Champions may join as peers. They do not run the desk.
- **Escalation.** Policy and security questions go to the security lead. Product bugs go to the vendor contact through the rollout owner. Publish a response time for each route.
- **Service limits.** Office hours cover usage and workflow questions. They do not cover code review, production debugging or policy approval. Cap the length of each session and say so in advance.
- **Recurring-issue analysis.** Log every question with its category. Review the log each month. Turn repeated issues into docs or fixes. See the note on repeated support demand in the champion section.

## Champion program

Champions are volunteers who help peers.

A champion is not first-line support, a policy approver, or a substitute for engineering management. Budget one to two hours per week during the pilot as a planning range. If the role regularly exceeds that limit, fix the rollout or add formal support capacity. Track champion workload separately. Repeated support demand is a rollout defect, not evidence that the champion program is working.

**Selection criteria**

- Uses the tool on real work already, and can explain how.
- Respected by peers, not only the most senior person.
- Willing to say when the tool fails.
- Has manager approval for the time.
- Spread across teams, so no team is left out.

**Champion kit**

- A one-page quick start and the shared rules files.
- A list of tested prompts for common tasks.
- A short guide on how to review agent-made diffs.
- The champion charter. See `templates/champion-charter.md`.
- A direct channel to the rollout owner.

**Cadence**

- Weekly 30-minute sync for champions in the first month, then every two weeks.
- One shared demo per month, run by a champion.
- A short written note from each champion on what blocked people.

**Recognition**

- Name champions in team updates and give credit in performance input.
- Offer learning time, and do not rank champions by usage numbers.

**Limits on champion load**

- Champions do not carry on-call duty for the tool.
- If a champion's own delivery slips, reduce their load first.
- Replace champions who burn out, with no blame.

## Why people stop after week two

| Reason | Sign | What to do |
|---|---|---|
| One bad result early | Person says it is not useful | Pair on a better task. Show a prompt that works |
| No time to learn | Person returns to old habits during busy sprints | Ask the manager to protect an hour a week |
| Review fear | Person avoids agent-made changes | Practice reviewing a sample diff together, and teach the review gates in `03-embed.md` |
| Setup friction | Slow, crashes, or sign-in loops | Fix the setup, and test on a clean machine |
| Unclear rules | Person unsure what is allowed | Publish a one-page allowed use list. See "What work is in scope" in `03-embed.md` |
| No peer use | Nobody on the team uses it | Place a champion on that team |
| Quality worries | Reviewers distrust the output | Tighten the review gates in `03-embed.md` and check that expected behavior is defined |
| Cost worry | Person fears running up spend | Explain limits and how spend is tracked, verify against current Cursor docs |

Reach out within a week of a drop. Ask one open question and listen. Do not send a usage reminder.

Next step: `03-embed.md`.
