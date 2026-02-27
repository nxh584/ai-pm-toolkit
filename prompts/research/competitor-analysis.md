# Competitor Analysis

## When to use this
Use this when you need a fast lay of the land for a specific feature or market segment, not when you have days to research. It gives you immediate functional benchmarks before you start designing.

## What to feed it
- 2-3 specific competitors in your space (e.g., "Linear, Jira, and Asana").
- The specific feature or workflow you want analysed (e.g., "how they handle bulk issue assignment").

## The Prompt

```markdown
I need a fast competitive mapping for how the following tools handle [INSERT SPECIFIC FEATURE/WORKFLOW: e.g., bulk issue assignment]:
- Competitor 1: [Name]
- Competitor 2: [Name]
- Competitor 3: [Name]

For *each* competitor, evaluate them strictly on that specific feature and provide:
1. **What they do**: A 1-sentence breakdown of the mechanic.
2. **Who it's for**: The specific user archetype this design favors.
3. **What they do well**: The best part of their UX/technical approach.
4. **What they miss**: The friction point, edge case they ignore, or major failing.

Finally, synthesise the **Gap in the Market**: Based on how these three approach the problem, what is the obvious unmet need or opportunity space we could exploit? 
```

## What to do with the output
Use the "Gap in the Market" section to inform your `problem-statement.md`. Look for the friction points competitors ignore and decide if fixing that friction is high leverage for your users.

## Common failure modes
- **Agent provides generic product summaries**: The agent might give you a Wikipedia-style overview of Jira instead of focusing on the specific feature. Re-prompt: "You are being too broad. Focus ONLY on their bulk assignment UX."
