# 01 Align

This guide helps you agree on why you are rolling out an AI coding tool, who owns it, and how you will judge it, before anyone gets a license. Most stalled rollouts skipped this step. Plan for about a week of work. Do it before you announce anything.

## Checklist

- [ ] One executive sponsor is named, briefed in one meeting, and has agreed to the obligations below.
- [ ] One rollout owner and a backup are named. The owner runs the day-to-day work.
- [ ] A budget owner is named.
- [ ] Success criteria are written down, with a baseline and its date, before launch.
- [ ] The usage data source is identified. Check what the admin analytics show (verify against current Cursor docs).
- [ ] Security, privacy and legal reviews are started, not just planned. Use `templates/security-data-checklist.md` and open it with written answers to the data questions.
- [ ] The questions in "Questions to settle first" have an answer or a dated owner.
- [ ] Pilot teams are chosen, with a stated reason for each.
- [ ] A decision log exists and is shared.
- [ ] The announcement is drafted by the sponsor, not by the tool vendor.

## The executive sponsor

A sponsor is not a name on a slide. The rollout needs someone who can remove blockers and who will be asked about results.

The sponsor has five obligations:

1. Approve scope. Say which teams, repositories and kinds of work are in, and why.
2. Resolve blocked decisions. Clear security and procurement blockers within days, not weeks.
3. Protect rollout capacity. People will not learn a tool on top of a full sprint.
4. Review evidence without inflating claims. Join the review described in `05-expand.md`, read the numbers, and accept that early numbers are small and noisy.
5. Make the expand, hold or stop decision, and record it.

What the sponsor should not do:

- Set a usage target that people can meet by clicking.
- Promise a productivity result before there is a baseline.
- Mandate daily use without saying what good use looks like.
- Compare teams in public. That ends honest reporting fast.

## Success criteria, written before rollout

Write criteria in three groups. Each needs a baseline you can actually collect today.

Example only. These are not benchmarks or recommended targets.

| Group | What it answers | Example criterion |
|---|---|---|
| Adoption | Are people using it? | Sustained use reaches a level the sponsor agreed on by day 90 |
| Depth | Are they using it well? | Example only: active users work in more than one way (completions, chat, agent tasks) where it fits their work. |
| Outcome | Does the work improve? | Median time from pull request open to merge does not get worse |

Rules for writing criteria:

- Set each target from the decision it controls. See "How to choose a threshold" in `05-expand.md`.
- Name the baseline and the date you collected it.
- Pair every usage criterion with an outcome or quality guardrail.
- Write down what you will not claim. See `04-measure.md`. The scorecard report shows what each metric can hide.

## Risks to name early

| Risk | What it looks like | First action | Control | Owner |
|---|---|---|---|---|
| Security review | Review blocks the pilot late | Start review in week 0 with the data-handling answers below | Completed `templates/security-data-checklist.md`, with a decision on each row before pilot access | Security lead |
| Privacy | Unclear what code or prompts leave the company | Document privacy settings, verify against current Cursor docs | Required privacy settings recorded in the decision log and checked at onboarding, where admin controls allow | Security lead |
| Code ownership | Questions on who owns generated code | Ask legal for a written position on generated code | Written legal position filed with the decision log, plus the license and intellectual-property row of the security checklist | Legal counsel |
| Cost control | Usage-based spend grows with no owner | Assign a budget owner, set alerts if available, verify against current Cursor docs | Monthly cost review using the formula in `05-expand.md` | Budget owner |
| Review load | Reviewers drown in agent-made diffs | Set review rules early, see `03-embed.md` | Review gates in place before launch, and reviewer capacity checked before each new wave | Engineering lead |
| Expectation gap | Leaders expect instant results | Share the 30-60-90 plan and its exit criteria | Exit criteria agreed with the sponsor in writing before launch | Sponsor |

## Questions to settle first

Write the answer, the owner and the date for each. Many answers depend on the plan and settings you buy, so verify against current Cursor docs. Record the evidence for each answer in `templates/security-data-checklist.md`.

**Data handling**

- What code and prompt data is stored or retained by the vendor?
- Is a privacy or no-retention mode available, and can an admin enforce it (verify against current Cursor docs)?
- Are secrets and customer data kept out of prompts? How do you check?

**Scope**

- Which repositories are in scope for the pilot? Which are out, and why?
- Are there regulated or export-controlled repos that need a separate decision?
- Which kinds of work are in scope, and which are excluded at first? See "What work is in scope" in `03-embed.md`.

**Model access**

- Which models can people choose? Who decides (verify against current Cursor docs)?
- Is there a cost difference between models that users will notice?

**Rules and assets**

- Who approves shared rules files and team commands?
- Where do they live, and who can change them?

**Support**

- Who answers questions in week one? See office hours in `02-enable.md`.

## Decision log

Keep one table. Add a row for every decision that someone could later ask about.

| Date | Decision | Options considered | Owner | Revisit on |
|---|---|---|---|---|
| [fill in] | Example: pilot starts with two teams | All teams, two teams, volunteers only | Rollout owner | [fill in] |
| [fill in] | Example: privacy mode required for all users | Required, optional | Security lead | [fill in] |
| [fill in] | Example: shared rules need two approvers | One approver, two approvers | Engineering lead | [fill in] |

Next step: `02-enable.md`.
