# 04 Measure

This guide defines four adoption metrics, shows how each one can be inflated, and names the companion metric that exposes the inflation. It also covers depth, honest reporting of value, and what not to report. `tools/adoption_scorecard` implements these definitions.

## Checklist

- [ ] All four metrics are defined the same way in every report.
- [ ] Every metric is shown next to its companion metric.
- [ ] Depth is reported, not only headcount.
- [ ] Usage and outcomes are reported in separate sections.
- [ ] The baseline and its date are stated.
- [ ] A "cannot attribute" note is in every report.
- [ ] The "do not report" list is agreed with the sponsor.
- [ ] You know which usage data your plan provides (verify against current Cursor docs).

## The four metrics

Pick a date, count users by the rules below, and divide by licensed users where a rate is needed. All thresholds here are definitions you may change, but change them once and keep them.

### 1. Licensed

**Definition.** People who hold a seat on the report date.

**How it can be inflated.** Buying seats for people who will never use them, or leaving departed people on the list.

**Companion metric.** Activated rate. Seats with no activity show up as the gap between licensed and activated.

### 2. Activated

**Definition.** Licensed people with any recorded use after their license date.

**How it can be inflated.** One-time sign-in trials. A single click on launch day counts.

**Companion metric.** Sustained rate. A trial that never repeats is activated but not sustained.

### 3. Weekly active

**Definition.** Licensed people with use on at least one day in the 7 days up to the report date. A calendar-week version is fine if you use it every time. The scorecard uses the rolling 7 days.

**How it can be inflated.** A reminder email or a team challenge in that week causes a spike. Light use such as one accepted completion counts the same as a full day of work.

**Companion metric.** Sustained rate, and the depth measures below. A spike fades in sustained, and shallow use shows in depth.

### 4. Sustained

**Definition.** Licensed people who were weekly active in at least 3 of the last 4 weeks.

**How it can be inflated.** A mandate or a daily-use target makes people tick a box each week. Small teams swing a lot from one person.

**Companion metric.** Depth, plus an outcome check such as a short survey or review quality. If sustained is high but depth and outcomes are flat, use may be ritual.

Quick reference:

| Metric | Counts | Inflated by | Exposed by |
|---|---|---|---|
| Licensed | Seats | Idle or stale seats | Activated rate |
| Activated | Any use ever | Sign-in trials | Sustained rate |
| Weekly active | Use in latest week | Pushes and campaigns | Sustained rate, depth |
| Sustained | 3 of last 4 weeks | Mandates, ticking | Depth, outcome check |

Report counts and rates. With small groups, show the count so nobody reads a swing as a trend.

Do not read a metric as proof of the next layer. Licenses do not prove use. Use does not prove depth. Depth does not prove productivity. Productivity does not prove business value.

## Depth measures

Headcount says who touched the tool. Depth says how.

- Split active users into those with agent sessions and those with completions only. Which events your data records depends on the tool, so verify against current Cursor docs.
- Report the share of active users with agent sessions in the period.
- Report median active days per person over the period. The scorecard uses the last 28 days.
- Do not rank people. Use depth to find teams that need coaching.

Completions only is not bad. It is a stage. Agent sessions are not always better. They suit larger tasks and need stronger review. For that reason the scorecard reports depth on its own and does not score it.

## Reporting value without overclaiming

1. Separate usage from outcomes. Show them in different sections.
2. State the baseline. Say what you measured, over what period, before rollout.
3. Choose outcomes that teams already track, such as review time, change failure signals, or cycle time.
4. Say what you cannot attribute. Many things change at once: staffing, projects, other tools.
5. Show ranges and uncertainty. Avoid a single number with false precision.
6. Add quality guardrails next to speed measures.
7. Use the words "associated with", not "caused by", unless you ran a controlled comparison.

Templates: `templates/exec-roi-one-pager.md` and `templates/outcome-review.md`.

## Do not report

- Hours saved, unless you measured them with a method you can describe.
- Lines of code generated or accepted as a productivity figure.
- Rankings of individuals by usage.
- Team leaderboards shown outside the team.
- Vendor-provided benchmarks as if they were your results.
- A single blended "productivity gain" number.
- Activated rate alone as proof of adoption.
- Any number without its date, definition and population.

## Survey versus telemetry

| | Telemetry | Survey |
|---|---|---|
| Shows | What people did | What people felt and why |
| Strength | Objective, continuous, cheap once set up | Explains reasons, catches value telemetry misses |
| Weakness | No reasons, easy to inflate, depends on what the plan records, verify against current Cursor docs | Self-report bias, low response, one point in time |
| Use for | Funnel, trends, flags | Barriers, trust, quality concerns |

Guidance:

- Use both. Telemetry finds where to look. Surveys explain what you find.
- Keep surveys short, anonymous where you can, and run them on a fixed schedule.
- Ask about behavior ("what did you use it for last week?") more than opinion.
- Do not average survey scores across teams of very different sizes.
- Share results back with respondents. Silence kills response rates.

Next step: `05-expand.md`.
