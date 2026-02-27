# Parallel Approaches

## When to use this
Use this when the problem is clear, but the *interaction model* or technical approach is ambiguous. Instead of guessing, you force the agent to present two wildly different ways to solve it so you can compare the trade-offs.

## What to feed it
- The shaped problem.
- Any known hard constraints.

## The Prompt

```markdown
We need to solve this problem:
[INSERT PROBLEM STATEMENT]

The problem is clear, but the approach is not. Do not write the full implementation yet.

Instead, propose TWO entirely different conceptual approaches to solving this problem. The approaches must differ meaningfully in their UX paradigm or technical architecture (e.g., synchronous vs asynchronous, explicit UI vs implicit automation, dashboard vs email).

For each approach, provide:
1. **The Concept**: How it works for the user.
2. **The "Why"**: The core hypothesis of why this approach is best.
3. **The Trade-off**: The biggest flaw or risk with this approach.
4. **Time to Build**: An estimation of complexity.

Do not recommend one over the other. Just present the options.
```

## What to do with the output
Review the trade-offs. Often, Approach A will have great UX but high technical complexity, while Approach B will be a fast, ugly hack. Pick the approach that optimises for your current constraint (usually time-to-learning) and ask the agent to build it: "Let's go with Approach 2. Give me the first-pass build."

## Common failure modes
- **Agent provides cosmetic variants**: If the agent suggests "Approach A is a blue button, Approach B is a red button," push back: "These are just UI variants. I need fundamentally different architectural or workflow approaches."
