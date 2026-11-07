# 01 Align

This guide helps you agree on why you are rolling out an AI coding tool, who owns it, and how you will judge it, before anyone gets a license. Most stalled rollouts skipped this step. Plan for about a week of work. Do it before you announce anything.

## Checklist

- [ ] One executive sponsor is named and has agreed to the duties below.
- [ ] One rollout owner is named. This is the person running the day-to-day work.
- [ ] Success criteria are written down, with a baseline, before launch.
- [ ] Security, privacy and legal reviews are started, not just planned.
- [ ] The questions in "Questions to settle first" have an answer or a dated owner.
- [ ] A decision log exists and is shared.
- [ ] The week 0 checklist at the end of this guide is done.

## The executive sponsor

A sponsor is not a name on a slide. The rollout needs someone who can remove blockers and who will be asked about results.

What the sponsor must do:

- Say in public why the organization is doing this, in their own words.
- Clear security and procurement blockers within days, not weeks.
- Protect time for onboarding. People will not learn a tool on top of a full sprint.
- Join the review described in `05-expand.md` and read the numbers.
- Accept that early numbers are small and noisy.
- Decline to compare teams in public. That ends honest reporting fast.

What the sponsor should not do:

- Set a usage target that people can meet by clicking.
- Promise a productivity result before there is a baseline.
- Mandate daily use without saying what good use looks like.

## Success criteria, written before rollout

Write criteria in three groups. Each needs a baseline you can actually collect today.

| Group | What it answers | Example criterion (hypothetical) |
|---|---|---|
| Adoption | Are people using it? | Example: sustained use reaches a level the sponsor agreed on by day 90 |
| Depth | Are they using it well? | Example: most active users have tried agent-style work, not only completions |
| Outcome | Does the work improve? | Example: median time from pull request open to merge does not get worse |

Rules for writing criteria:

- Set the target yourself. This playbook gives no benchmark, because yours depends on your teams.
- Name the baseline and the date you collected it.
- Pair every usage criterion with an outcome or quality guardrail.
- Write down what you will not claim. See `04-measure.md`.

## Risks to name early

| Risk | What it looks like | First action |
|---|---|---|
| Security review | Review blocks the pilot late | Start review in week 0 with the data-handling answers below |
| Privacy | Unclear what code or prompts leave the company | Document privacy settings, verify against current Cursor docs |
| Code ownership | Questions on who owns generated code | Ask legal for a written position on generated code |
| Cost control | Usage-based spend grows with no owner | Assign a budget owner, set alerts if available, verify against current Cursor docs |
| Uneven access | Some teams get licenses, others wait | Publish the rollout order and the reason for it |
| Review load | Reviewers drown in agent-made diffs | Set review rules early, see `03-embed.md` |
| Expectation gap | Leaders expect instant results | Share the 30-60-90 plan and its exit criteria |

## Questions to settle first

Write the answer, the owner and the date for each. Many answers depend on the plan and settings you buy, so verify against current Cursor docs.

**Data handling**

- What code and prompt data is stored or retained by the vendor?
- Is a privacy or no-retention mode available, and can an admin enforce it (verify against current Cursor docs)?
- Are secrets and customer data kept out of prompts? How do you check?

**Scope**

- Which repositories are in scope for the pilot? Which are out, and why?
- Are there regulated or export-controlled repos that need a separate decision?

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

## Week 0 checklist

- [ ] Sponsor named and briefed in one meeting.
- [ ] Rollout owner and a backup named.
- [ ] Baseline collected for the outcome metrics you chose.
- [ ] Usage data source identified. Check what the admin analytics show, verify against current Cursor docs.
- [ ] Security and privacy review opened with written answers to the data questions.
- [ ] Pilot teams chosen, with a stated reason for each.
- [ ] Budget owner named.
- [ ] Decision log created.
- [ ] Announcement drafted by the sponsor, not by the tool vendor.
- [ ] Next step: `02-enable.md`.
