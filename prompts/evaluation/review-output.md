# Review Output

## When to use this
Use this immediately after the agent (or an engineer) gives you a functional prototype or a block of code. Before you commit to the approach, use this to force the agent to honestly critique its own work against reality.

## What to feed it
- The generated code or prototype.
- The `problem-statement.md` and `project-context.md`.
- `@skills/evaluation.md`.

## The Prompt

```markdown
Read `@problem-statement.md` and `@project-context.md`.

You just provided the attached output/code. Switch roles from Creator to Critic. Be ruthless. Answer the following questions about your own output:

1. **Alignment:** Does this solve the *actual* stated problem, or does it just technically run without errors?
2. **Unhandled Edge Cases:** Identify 3 specific edge cases a real-world user will inevitably hit that this code currently ignores.
3. **Maturity:** Is this a fragile prototype meant for learning, or is it robust enough to ship to 10% of users tomorrow?
4. **User Friction:** What is the most annoying or confusing part of UX/workflow you just designed?
5. **Breaking Points:** What is the most likely way this specific implementation breaks in production?

Wait for my instruction before writing any fixes.
```

## What to do with the output
If the critique surfaces critical edge cases or UX friction, reply with: "Fix the UX friction you identified in #4 and handle the first edge case in #2. Leave the rest as is for now."

## Common failure modes
- **Agent gets defensive or overly positive**: The agent might say "This code is highly robust and solves the problem perfectly." If so, reply: "Try again. Act as a Staff Engineer reviewing a Junior Engineer's PR. Find the flaws."
