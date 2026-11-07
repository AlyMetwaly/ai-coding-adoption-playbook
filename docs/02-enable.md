# 02 Enable

This guide helps you get people from "has a license" to "uses it on real work in week one". It covers onboarding paths by role, a first-week plan, office hours, a champion program, and the usual reasons people drop off. Use it after `01-align.md` is done.

## Checklist

- [ ] Each role has a short onboarding path with one real task.
- [ ] The first-week plan is published and has dated sessions.
- [ ] Office hours are scheduled for the first four weeks.
- [ ] Champions are chosen with clear criteria and a limit on their load.
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
| Senior engineer | Refactor a function with tests running | Writing precise prompts, rules files, scoping tasks | Dismissing the tool after one weak result |
| Tech lead | Draft a design note, then review an agent-made diff | Team rules, review gates, task splitting | Becoming the only reviewer |
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
| Day 4 | Try an agent-style task on a low-risk change, with review | One reviewed pull request |
| Day 5 | Office hours and a short retro | Written list of questions and blockers |

## Office hours design

- Hold them twice a week in the first month, then weekly.
- Keep them open to all roles. Record nothing that shows private code.
- Use a fixed format: five minutes of one tip, then open questions.
- Ask people to bring a real task they are stuck on.
- Keep a public log of questions and answers. Turn repeats into docs.
- Rotate the host between champions so no one burns out.
- Track attendance as a signal, not a goal.

## Champion program

Champions are volunteers who help peers. They are not a support desk.

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
- A template for sharing a win. See `templates/champion-charter.md`.
- A direct channel to the rollout owner.

**Cadence**

- Weekly 30-minute sync for champions in the first month, then every two weeks.
- One shared demo per month, run by a champion.
- A short written note from each champion on what blocked people.

**Recognition**

- Name champions in team updates and give credit in performance input.
- Offer learning time, not just thanks.
- Do not rank champions by usage numbers.

**Limits on champion load**

- Set a cap on hours per week, agreed with their manager. Example: a few hours.
- Champions do not carry on-call duty for the tool.
- If a champion's own delivery slips, reduce their load first.
- Replace champions who burn out, with no blame.

## Why people stop after week two

| Reason | Sign | What to do |
|---|---|---|
| One bad result early | Person says it is not useful | Pair on a better task. Show a prompt that works |
| No time to learn | Person returns to old habits during busy sprints | Ask the manager to protect an hour a week |
| Review fear | Person avoids agent tasks | Teach small diffs and the review gate in `03-embed.md` |
| Setup friction | Slow, crashes, or sign-in loops | Fix the setup, and test on a clean machine |
| Unclear rules | Person unsure what is allowed | Publish a one-page allowed use list |
| No peer use | Nobody on the team uses it | Place a champion on that team |
| Quality worries | Reviewers distrust the output | Add tests-first and diff-size rules |
| Cost worry | Person fears running up spend | Explain limits and how spend is tracked, verify against current Cursor docs |

Reach out within a week of a drop. Ask one open question and listen. Do not send a usage reminder.

Next step: `03-embed.md`.
