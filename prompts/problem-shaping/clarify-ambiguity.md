# Clarify Ambiguity

## When to use this
Use this when you have a feature request, a vague goal, or an initial idea that feels too loose. If you sent this idea to an engineer today, they would have too many questions. This prompt forces the agent to act as that questioning engineer so you can tighten the scope.

## What to feed it
- A rough draft of the problem or feature request.
- Any relevant context documents (`@product-context.md`).

## The Prompt

```markdown
I have a loose idea for a feature/problem we need to solve, but it isn't shaped well enough to build yet. 

Here is my rough thinking:
[INSERT ROUGH DRAFT/IDEA HERE]

Do not design a solution. Do not write any code.

Instead, act as a rigorous Product Manager and ask me exactly 5 clarifying questions that I must answer before we can proceed. Your questions should force me to clarify:
1. The actual user pain point (vs the symptom).
2. The frequency of the problem.
3. How users are currently working around it.
4. How we will measure if we solved it.
5. What technical or resource constraints limit us.

After listing the questions, wait for my response.
```

## What to do with the output
Answer the questions directly. If you don't know the answer to one of them, the problem is not ready for implementation—it needs user research or executive alignment.

## Common failure modes
- **The agent designs a solution anyway**: Remind it: "Do not propose solutions yet. We are only defining the problem."
- **The questions are too generic**: Reply with "These are too generic. Read `@product-context.md` and make the questions specific to our actual product architecture."
