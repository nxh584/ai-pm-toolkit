# First-Pass Build

## When to use this
Use this when you have a well-formed problem and context, and you are ready for the agent to write the very first version of the code.

## What to feed it
- `problem-statement.md` or a lightweight `spec.md`.
- `user-context.md`.
- `@skills/prototyping.md` (to ensure the right mindset).

## The Prompt

```markdown
Read `@user-context.md` and the problem statement below.

Problem: 
[INSERT PROBLEM STATEMENT]

Act as a prototyping engineer. I want you to build the first-pass version of a solution to this problem. 

Rules for this build:
1. **Prioritise Speed-to-Learning**: Build the simplest, fastest version that tests the core hypothesis. 
2. **Mock the Rest**: If a database, complex auth, or heavy backend isn't strictly necessary to validate if the user wants this, mock it or use local state.
3. **No premature optimisation**: Do not build for scale. We just need it to work for 1 user today.

Before outputting code:
- Explain the 1-2 key technical trade-offs you made to prioritise speed.
- List what you are intentionally NOT building in this pass.

Then, provide the code.
```

## What to do with the output
Run the code. Do not review the syntax; review the experience. Does it actually feel like a solution to the problem? If yes, run the `evaluation/ship-or-kill.md` prompt. If no, run the `course-correct.md` prompt.

## Common failure modes
- **Agent over-engineers**: The agent might try to set up a Redux store, Docker container, and Postgres schema for a simple form. Stop it immediately and say: "Too complex. Strip out the backend entirely. Use local storage for now."
