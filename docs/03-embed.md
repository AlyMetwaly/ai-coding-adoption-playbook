# 03 Embed

This guide helps you turn scattered individual tricks into shared team habits. It covers repeatable workflows, what work is in scope, shared rules files, an AGENTS.md pattern, reusable skills and commands, and review gates for changes made by agents. Use it once a few people use the tool daily.

## Checklist

- [ ] Three to five use cases are picked from real team work.
- [ ] Each use case has a written workflow, an owner and a review rule.
- [ ] The in-scope, extra-review and excluded work lists are agreed with the security owner.
- [ ] A shared rules file and an AGENTS.md exist in each in-scope repo.
- [ ] Shared assets live in version control, with a named owner.
- [ ] A review gate for agent-made changes is written and used.
- [ ] Rules are reviewed on a schedule and old ones are removed.
- [ ] File formats and locations are checked (verify against current Cursor docs).

## From use case to repeatable workflow

A use case is a task people already do. A workflow is the same task, written so a colleague gets a similar result.

Steps:

1. Collect what your champions do already. Ask for real prompts and real outcomes.
2. Pick tasks that are frequent, low risk and easy to check. Tests, docs and small refactors are common first picks.
3. Write the workflow: input, steps, what good output looks like, what to check.
4. Try it with two people who did not write it.
5. Store it as a shared asset and name an owner.
6. Retire it when it stops helping.

A workflow is ready when someone new can follow it without asking the author.

## What work is in scope

Not every task suits the tool in the first months. Sort work into three lists and publish them. Teams should adjust these lists with their security owner. Record the result in the decision log from `01-align.md`.

**Allowed**

- Tests.
- Documentation.
- Local developer tooling.
- Small refactors with unchanged behavior.
- Boilerplate in established patterns.

**Allowed with additional review**

- New dependencies.
- Database migrations.
- API contract changes.
- Performance-sensitive code.
- CI/CD changes.

**Excluded initially**

- Authentication and authorization.
- Cryptography.
- Secrets management.
- Payment logic.
- Safety-critical systems.
- Production incident changes.
- Code involving restricted data.

Revisit the excluded list when you have evidence from the allowed work, not before.

## Shared rules files

Rules tell the tool how your team works. Keep them short and specific. The format, location and options for rules change over time, so verify against current Cursor docs. Two examples are in `.cursor/rules/` in this repo.

**What to put in**

- Build, test and lint commands.
- Naming and structure conventions that are not obvious from the code.
- Testing expectations for behavior changes.
- Security basics: no secrets in code, how to handle input.
- How to explain trade-offs in a change.
- Pointers to deeper docs, not copies of them.

**What to keep out**

- Secrets, tokens, internal URLs and customer data.
- Long style guides that a linter already enforces.
- Vague advice such as "write good code".
- Rules that contradict each other across files.
- Personal preferences that only one person holds.
- Anything that goes stale in a month.

Each rule should be testable. If you cannot tell whether the tool followed it, rewrite it.

## The AGENTS.md pattern

An AGENTS.md file at the repo root tells any coding agent how to work in that repo. Support for this file depends on the tool, so verify against current Cursor docs.

Suggested sections:

| Section | Content |
|---|---|
| What this repo is | Two sentences on purpose and layout |
| Setup and commands | How to install, build, test, lint |
| Conventions | The few rules that matter most |
| Do not | Hard limits: no pushing, no deleting data, no new dependencies without approval |
| Done means | Which checks must pass before work is finished |

Keep it under a page. Review it like code. This repo has an `AGENTS.md` as a working example.

## Skills and commands as team assets

Skills and commands package a workflow so people can run it again. Names, formats and availability vary, so verify against current Cursor docs.

- Store them in the repo, not on one person's laptop.
- Give each one a name that says what it does.
- Add a short description and one example of use.
- Name an owner and a review date.
- Test with a person who did not write it.
- Remove ones that nobody ran in a quarter.

Trade-off: more assets mean more to maintain. Ten good ones beat fifty stale ones.

## Review gates for agent-made changes

Agents can produce a lot of code fast. Review becomes the bottleneck and the safety net.

- [ ] Prefer changes small enough to review as one coherent unit. Do not split a risky change into several pull requests only to satisfy a size limit.
- [ ] Define the expected behavior before accepting the change. Add or update automated tests where practical. If automated coverage is not practical, record the manual verification performed and the remaining risk.
- [ ] The author must understand the behavior, assumptions, security implications and failure modes of the change. The author remains accountable for the full pull request, including generated code.
- [ ] The agent lists files touched and commands run.
- [ ] Human approval before merge. The agent never merges or pushes alone.
- [ ] Extra care for work on the "allowed with additional review" list above, and for anything on the excluded list that is later approved.
- [ ] Reviewers may ask for a change to be restructured when they cannot review it as one unit, and the author must respond.

Trade-offs to state openly:

- Changes that stay reviewable can mean more pull requests. Plan for review capacity.
- Defining expected behavior first adds time to the first draft. It gives reviewers something to check against.
- Manual verification is weaker evidence than automated tests. Record the remaining risk when you rely on it.
- Strict gates may annoy people at first. Relax them only with evidence, such as stable quality over time.

## Use case table (hypothetical rows)

These rows are examples. Replace them with your own.

| Use case | Shared asset | Owner | Review rule |
|---|---|---|---|
| Add tests for existing code | Command: generate tests for a file | Test champion | Tests must fail when behavior breaks |
| Explain unfamiliar module | Prompt in champion kit | Docs champion | Author checks claims against code |
| Small refactor | Rule: small focused changes | Tech lead | Reviewable as one unit, behavior unchanged, tests pass |
| Draft release notes | Command: summarize merged changes | Release owner | Human edits before publishing |
| Dependency upgrade | Skill: upgrade checklist | Platform lead | Two reviewers, full test run |

Next step: `04-measure.md`.
