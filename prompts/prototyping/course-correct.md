# Course Correct

## When to use this
Use this when the agent's first-pass prototype functionally runs, but misses the mark on user experience, misses an edge case, or feels disconnected from the actual problem.

## What to feed it
- The currently running code.
- Your specific feedback using the "That's not right because..." framework.

## The Prompt

```markdown
The prototype runs, but it does not solve the problem correctly. 

Here is my feedback:
1. Currently, it does [X]. That's not right because [USER REASON]. It needs to do [Y] instead.
2. I noticed an edge case: if the user does [Z], the flow breaks.

Based on this feedback:
1. Explain back to me *why* the original design was flawed based on user behaviour.
2. Outline the specific code changes needed to fix this.
3. Provide the updated code.
```

## What to do with the output
Run the revised code. Verify that the agent didn't undo a previous working feature while fixing the new one (a common hallucination loop).

## Common failure modes
- **Agent loses context**: If you are 20 turns deep in a chat, the agent might forget the original constraints and start introducing completely new libraries to solve a simple bug. If this happens, start a fresh chat, paste the current code, the `project-context.md`, and the specific course correction.
