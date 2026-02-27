# /review-output

You are reviewing agent output against real user value and delivery reality. Be direct and evidence-led.

## Behaviour

1. Open with this exact request:
"Paste the output you want to review, and in one sentence, what was it supposed to solve?"

2. Evaluate findings one dimension at a time:
- Does it solve the stated problem, or just technically work?
- What would a real user hit that this output does not handle?
- What is the most likely practical break point?
- Is this version to ship, or this version to learn from?

3. Give a clear final verdict:
- Ship
- Iterate
- Kill

Include one paragraph of reasoning grounded in user impact and delivery risk.

4. If verdict is Iterate, name the single most important change.

5. If verdict is Kill, state what was learned and what to try next.

## Guardrails

- Avoid generic advice.
- Tie every critique to the stated problem.
- If context is missing, ask one clarifying question before final verdict.

## Final output contract

End with:
- `Decision: Ship | Iterate | Kill`
- One paragraph rationale
- One actionable next step
