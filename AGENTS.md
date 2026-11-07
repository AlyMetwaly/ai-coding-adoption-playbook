# AGENTS.md

How an AI agent should work in this repo.

## What this repo is

A docs repo plus a small Python tool. It is a practical kit for rolling out an AI coding tool, written around Cursor.

- `docs/` has five guides and four templates.
- `.cursor/rules/` has two example rules.
- `tools/adoption_scorecard/` turns a usage CSV into a Markdown report.
- `tools/check_style.py` checks the style rules.
- `data/sample_usage.csv` is synthetic data.
- `SPEC.md` is the source of truth for scope. Read it first.

## Style rules

- Plain words. Short sentences, aiming for 20 words or fewer.
- No em dashes, no en dashes, no emojis.
- Never use the banned marketing words. The list lives in `tools/check_style.py`.
- US spelling: license, organization, behavior.
- Do not open a doc with a question.
- Each guide opens with one short paragraph on its purpose, then a checklist, then the detail.

## Content rules

- Never add statistics, percentages or results as facts. Numbers may appear only as definitions, thresholds the reader sets, or examples labelled "example" or "synthetic".
- Do not add employer data, real customer names, real person names, screenshots or internal tool names.
- Any statement that depends on how Cursor behaves must carry the exact phrase "verify against current Cursor docs".
- Sample data must stay labelled synthetic.

## Before you finish

1. Run `python tools/check_style.py` and fix every hit.
2. Run `pytest` and make sure it passes.
3. Check that guides stay within their length and that links between docs still work.

## Working rules

- Make small, focused commits with clear messages.
- Do not push. A person pushes after review.
- Do not rewrite a guide wholesale. Edit the part that needs to change.
- Do not add dependencies without asking.
- If a request conflicts with this file, stop and ask.
