# JTBD Extraction

## When to use this
Use this when you have a feature request or user complaint, and you need to figure out the underlying "Job to be Done." This prevents you from building a feature that solves the symptom but misses the actual goal of the user.

## What to feed it
- Raw user quotes, support tickets, or feature requests.

## The Prompt

```markdown
Review the following user feedback:
[INSERT RAW FEEDBACK/TICKETS]

Do not suggest features to solve this yet. Instead, act as an expert in the Jobs-to-be-Done (JTBD) framework. Extract the core jobs these users are trying to hire our product to do.

Format your extraction into three categories:
1. **Functional Job**: What is the practical, objective task they are trying to complete? (e.g., "Sort my emails by sender").
2. **Emotional Job**: How do they want to feel while doing this, or what negative feeling are they trying to avoid? (e.g., "Feel confident I didn't miss a message from my boss").
3. **Social Job**: How does completing this task change how others perceive them? (e.g., "Appear highly responsive to the rest of the executive team").

For each job you identify, provide the specific evidence from the raw text that supports it.
```

## What to do with the output
If the emotional or social jobs are stronger than the functional job, your solution might be a UX copy change or a notification tweak rather than a heavy functional feature. Feed the extracted JTBD directly into your `problem-statement.md`.

## Common failure modes
- **Agent provides generic jobs**: If the agent says the job is "To save time," push back. "Saving time is a benefit, not a job. What specific task are they trying to accomplish faster?"
