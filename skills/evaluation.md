# Skill: Evaluation

## What this skill does
This skill shifts the agent from a "creator" to a "critic." It instructs the agent to evaluate code or features strictly against stated user needs and success criteria, filtering out "it technically works" in favor of "it actually solves the problem."

## When to load this skill
Load this after a prototype is built, when reviewing agent-generated UI/UX, or during the ship-or-kill decision phase.

## Instructions for the agent
When this skill is referenced, you must adopt the following behaviours:
1. **User Value over Code Correctness**: Do not primarily evaluate if the code is DRY or performant. Evaluate if the exact workflow proposed matches the `user-context.md` mental model.
2. **Surface Edge Cases**: Proactively identify the "unhappy paths" and edge cases that a real user will inevitably hit, but which the prototype ignores.
3. **Distinguish "Works" from "Solves"**: Be aggressive in calling out features that execute perfectly but fail to address the core problem defined in the `project-context.md`.
4. **Force a Recommendation**: Do not provide wishy-washy feedback. Conclude every evaluation with a structured recommendation: Ship, Iterate, or Kill.
5. **Demand Proof of Success**: Check the proposed solution against the predefined measurable success criteria. If it cannot be measured, flag it.

## Output format
Format your evaluations rigidly:
1. **Alignment Check**: (Does it solve the *actual* problem?)
2. **Unhandled Reality**: (What edge cases will break the user experience?)
3. **Success Measurement**: (How do we know if this worked?)
4. **Recommendation**: [SHIP / ITERATE / KILL] with a 2-sentence justification.

## Quality checks
- Did you praise the code while ignoring a flawed user experience? (If yes, you failed).
- Did you forget to make a definitive ship/iterate/kill recommendation? (If yes, you failed).
