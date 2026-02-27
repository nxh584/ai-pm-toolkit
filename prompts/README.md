# Prompts

Ready-to-use prompts for each stage of the product development process. These aren't meant to replace your thinking. They structure how you collaborate with an AI agent so you get more useful output at each stage.

---

## How each prompt is structured

Every prompt file follows the same format:

1. **When to use this**: the right moment to reach for it
2. **What to feed it**: what context or inputs the agent needs
3. **The prompt**: the exact text to paste into your session
4. **What to do with the output**: how to evaluate and act on the result
5. **Common failure modes**: what tends to go wrong and how to fix it

Two prompts use a conversational loop format instead of producing one-shot output:
- `problem-shaping/clarify-ambiguity.md`
- `prototyping/course-correct.md`

These follow the same structure but instruct the agent to guide a back-and-forth conversation rather than returning a single response.

---

## Prompts vs. Commands

- **Use prompts** when you're starting a fresh session. Paste one as your opening instruction and it sets the tone and structure for everything that follows.
- **Use commands** (in [`commands/`](../commands/)) when a session is already running and you want to invoke a specific workflow step without restarting the conversation.

Some prompts have direct command equivalents:
- `problem-shaping/clarify-ambiguity.md` → [`/clarify-ambiguity`](../commands/clarify-ambiguity.md)
- `prototyping/course-correct.md` → [`/review-output`](../commands/review-output.md) followed by [`/first-pass-build`](../commands/first-pass-build.md)

---

## Categories

### [Problem Shaping](problem-shaping/)
Prompts for clarifying ambiguity, defining success criteria, and establishing the real scope of a problem. Use these before any building work, when you have an idea but aren't yet confident you're solving the right thing.

### [Prototyping](prototyping/)
Prompts to guide first-pass builds, explore parallel approaches, and course-correct when output veers off track. Use these to turn a shaped problem into a testable, minimal prototype.

### [Research](research/)
Prompts for synthesising interview notes, analysing the competitive landscape, and extracting Jobs-to-be-Done from qualitative data. Use these to process what you've learned without losing the nuance.

### [Evaluation](evaluation/)
Prompts for reviewing agent output critically and making structured ship-or-kill decisions. Use these to make sure what was built actually solves the user's problem, not just a version of it.
