# /build-session

You are assembling a complete session brief by combining behaviour instructions, context, and task definition.

## Behaviour

1. Ask which skill to load. List available skills from `skills/` by name before asking for a choice.

2. Ask which context docs are available (`user`, `product`, `project`) and request either file paths or pasted content for each selected doc.

3. Ask what task should drive this session:
- Offer to load from `prompts/` by category and name.
- Or accept a freeform task written by the PM.

4. Assemble and present a session brief with this structure:

## Agent Session: [skill] + [task]

### Behavioural instructions
[loaded skill content or summary]

### Context loaded
[each context doc clearly labelled]

### Task
[prompt content or freeform task]

5. Close with:
"Here's your session brief. Ready to start?"

## Guardrails

- If context is missing, explicitly flag what is missing and why it matters.
- Do not silently invent context.
- Keep the final brief copyable and immediately usable as a session opener.

## Final output contract

End with:
- One fully assembled session brief.
- One short checklist of any missing context items (if applicable).
