# Interview Synthesis

## When to use this
Use this when you have a messy transcript from a user interview, a batch of unorganised notes from a sales call, or a dump of Zendesk tickets. It prevents you from losing the nuance in "corporate summary speak."

## What to feed it
- The raw, unedited transcript or notes.
- `@skills/user-research.md` to ensure the agent doesn't sanitise the data.

## The Prompt

```markdown
Read the attached raw interview transcript/notes.

Your task is to synthesise this raw data into structured insights without losing the actual voice of the user. Do not sanitise their language. Keep the sharp edges.

Format your output EXACTLY according to the `templates/user-research-synthesis.md` structure:
1. **Raw Observations**: Extract the 3-5 most potent, unvarnished quotes. Give preference to quotes that express high emotion or clear workarounds.
2. **Patterns**: What underlying themes connect these quotes?
3. **Surprises**: What in this data contradicts standard assumptions we might have about how users behave?
4. **Jobs to be Done (JTBD)**: What is the user actually hiring the product (or trying to hire the product) to accomplish?
5. **Product Implications**: What does this mean for our roadmap? What should we stop doing? What should we start doing?
6. **Open Questions**: What do we still not know after this conversation?
```

## What to do with the output
Save the output to a new `[user-name]-synthesis.md` file in your project. Compare multiple synthesis files side-by-side to find cross-user patterns.

## Common failure modes
- **Agent summarises rather than quotes**: If the agent writes "The user expressed frustration with the UI," push back. Say: "Give me the exact quote where they expressed frustration."
