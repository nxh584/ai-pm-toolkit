# Clarify Ambiguity

## When to use this
Use this when you have a feature request, a vague goal, or an initial idea that feels too loose. If you sent this idea to an engineer today, they would have too many questions. This prompt forces the agent to stay in discovery mode long enough to shape the real problem before any solution work starts.

## What to feed it
- A rough draft of the problem or feature request.
- Any relevant context documents (`@product-context.md`, `@user-context.md`, `@project-context.md` when available).

## The Prompt

```markdown
I need to clarify a messy product problem before we discuss solutions.

Here is the messy version:
[INSERT YOUR MESSY VERSION HERE]

Act as a sharp PM collaborator. Run this as a guided conversation, not a one-shot response.

Conversation rules:
1. Open with this exact question:
   "Give me the messiest version of the problem as you currently see it. Don't clean it up."
2. Ask follow-up questions one at a time, never as a list. Choose each next question based on my previous answer.
3. Across the conversation, make sure we cover:
   - who is affected and how severe/frequent the pain is
   - what workarounds exist today
   - what has already been tried
   - what "solved" would look like in observable terms
   - what constraint is making this hard
4. After 3-4 exchanges, offer a synthesis using this structure:
   - "Here's what I think the real problem is: ..."
   - "Here's what's still unclear: ..."
   Then ask if your synthesis matches my read.
5. Do not jump to solutions. If I start solutioning, redirect with:
   "Let's stay in the problem for a moment. What's broken about the current situation?"

Continue until we have a clear problem statement and an explicit list of remaining unknowns.
```

## What to do with the output
Use the final synthesis as your draft problem statement and either:
- run the `/problem-statement` command for a guided refinement loop, or
- drop it directly into `templates/problem-statement.md` to formalise it.

If key unknowns remain, treat them as the next discovery questions before any build work.

## Common failure modes
- **The agent proposes solutions too early**: Reply with "Stop solutioning. Stay in problem discovery and ask the next best clarifying question."
- **The questions are generic**: Reply with "Use the context docs and ask a specific question tied to this product and this user."
- **The agent rushes to synthesis too early**: If it offers a summary after one exchange, push back and ask it to keep questioning.
