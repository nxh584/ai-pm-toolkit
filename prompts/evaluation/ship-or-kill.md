# Ship or Kill

## When to use this
Use this when you have built a prototype, tested it (either technically or with users), and need to make a firm decision. This prompt prevents "sunk cost fallacy" iteration loops where you keep tweaking a mediocre idea forever.

## What to feed it
- The output of the prototype or the test results.
- The Success Criteria defined in your `project-context.md` or `prd.md`.
- `@skills/evaluation.md`.

## The Prompt

```markdown
Review the recent test results and the original success criteria in the attached context docs. 

Act as a ruthless Executive sponsor. Your job is to prevent us from carrying technical debt or shipping mediocre features. 

Evaluate the current state of this project against the success criteria. Then, provide a definitive, structured recommendation choosing ONE of the following three paths:

1. **SHIP**: It meets the core success criteria. The remaining bugs are cosmetic or low-severity edge cases. 
2. **ITERATE**: It shows strong directional promise but fails a hard constraint or critical edge case. (List exactly what must be fixed to flip this to Ship).
3. **KILL**: It technically works, but the fundamental hypothesis is flawed. The user doesn't care, or the technical debt isn't worth the value. We should delete the code.

Provide your recommendation and a 3-sentence justification grounded entirely in user impact.
```

## What to do with the output
If the agent recommends KILL, take it seriously. Document the failure in your `product-context.md` under "Institutional Memory" so you never build it again, then delete the branch.

## Common failure modes
- **Agent recommends "Iterate" indefinitely**: If the agent tells you to iterate just to polish minor UI details, push back. Say: "We are optimising for learning, not perfection. Change your recommendation to Ship if the core loop works."
