# Course Correct

## When to use this
Use this when the agent's first-pass prototype functionally runs, but misses the mark on user experience, misses an edge case, or feels disconnected from the actual problem.

## What to feed it
- The currently running code or output.
- Direct feedback on what is wrong with the current version.
- Relevant context documents (`@project-context.md`, `@problem-statement.md`).

## The Prompt

```markdown
The current version is not right yet. I want to course-correct through a short dialogue.

Current output/code:
[INSERT CURRENT OUTPUT OR CODE]

Start by asking me:
"What came out, and what's off about it? Don't tell me what you want instead yet — tell me what's wrong with what you got."

Then ask:
"Is the problem with what it does, how it does it, or what it doesn't do at all?"

Depending on my answer, probe one level deeper with exactly one follow-up:
- If "what it does": "What specifically does it do that it shouldn't?"
- If "how it does it": "What would the right approach feel like instead?"
- If "what it doesn't do": "What's the most important missing piece?"

Reflect back with this pattern:
"So what you need is [specific change], not [what was built]. Is that right?"

Wait for confirmation. Only after confirmation, produce the revised output.

After revising, ask:
"Better? What's still off?"

Keep the loop going until I confirm it is right, or say it is good enough for this iteration.
```

## What to do with the output
Run the revised version and evaluate whether the correction fixed the specific failure mode you identified at the start. If it improved the wrong thing, run another loop and tighten your diagnosis before asking for more changes.

## Common failure modes
- **Agent makes broad rewrites instead of targeted corrections**: Reply with "Too broad. Only change what maps to the diagnosed issue."
- **Agent skips confirmation before revising**: Reply with "Reflect back the exact change first, then wait for confirmation."
- **The PM describes what they want instead of what's wrong**: Gently redirect: "Before we go to the solution, help me understand what's broken about this version."
