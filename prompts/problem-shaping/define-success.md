# Define Success

## When to use this
Use this when you have a high-level goal like "improve retention" or "make onboarding better," but you don't have concrete metrics. This prompts helps convert fuzzy goals into testable, mathematical, or observational outcomes.

## What to feed it
- The high-level goal or shaped problem statement.
- `user-context.md` (to ensure metrics align with user behaviour).

## The Prompt

```markdown
We are preparing to solve the following problem:
[INSERT PROBLEM STATEMENT OR GOAL]

Before we build a prototype, we need to define exactly how we will know if it worked. 

Based on this problem, generate a success measurement framework that includes:
- **1 Lagging Indicator**: The ultimate business or user outcome we eventually want to see.
- **2 Leading Indicators**: Behavioural signals we can measure within 48 hours of launch that predict the lagging indicator.
- **1 Counter Metric**: A metric we need to monitor to ensure we didn't just shift the problem elsewhere (e.g., we increased signups but broke the server).
- **The "It Failed If..." Statement**: A clear observational threshold where we agree to kill or revert the feature.

Make these metrics specific to this exact problem, not generic SaaS metrics.
```

## What to do with the output
Pick *one* leading indicator to be your primary success metric for the prototype. Take the "It Failed If" statement and put it in your launch checklist.

## Common failure modes
- **Agent suggests metrics you can't track**: If the agent suggests tracking "time spent on page" but you don't have analytics installed, reply: "We don't have client-side analytics. Give me metrics we can measure purely via database state changes."
