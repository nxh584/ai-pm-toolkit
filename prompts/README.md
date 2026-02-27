# AI PM Prompts

This directory contains ready-to-use prompts designed for different stages of the product development lifecycle. They are not meant to replace your thinking, but to structure your collaboration with an AI agent.

## How to Use These Prompts

Each prompt file follows a consistent structure:
1. **When to use this**: The right moment to reach for the prompt.
2. **What to feed it**: The context or inputs the agent needs to succeed.
3. **The Prompt**: The exact text to paste into your agent session.
4. **What to do with the output**: How to evaluate and iterate on the result.
5. **Common failure modes**: What goes wrong and how to fix it.

Two prompts now use conversational loops inside the same structure:
- `problem-shaping/clarify-ambiguity.md`
- `prototyping/course-correct.md`

They still fit this format, but they instruct the agent to run guided back-and-forth instead of returning one-shot output.

## Prompts vs. Commands — which to use?

Prompts in this directory are best for starting a new session. You paste one as your opening instruction set and let it drive the session from turn one.

Commands in [../commands/](../commands/) are for use within an active working session. You invoke them by name to run a specific workflow step without restarting context.

Rule of thumb:
- Use prompts when you're starting fresh.
- Use commands when you're already mid-session.

Equivalent in-session command alternatives include:
- `clarify-ambiguity` prompt -> [`/clarify-ambiguity`](../commands/clarify-ambiguity.md)
- `course-correct` prompt -> use [`/review-output`](../commands/review-output.md) followed by [`/first-pass-build`](../commands/first-pass-build.md) if needed

## Categories

- **[Problem Shaping](problem-shaping/)**: Prompts to clarify ambiguity, define success, and extract constraints. Use these when you have a loose idea but need to define the boundaries before building.
- **[Prototyping](prototyping/)**: Prompts to guide the agent in building first-pass prototypes, parallel approaches, and course corrections. Use these to turn a shaped problem into a testable wedge.
- **[Research](research/)**: Prompts to synthesise interviews, analyse competitors, and extract Jobs-to-be-Done. Use these to process qualitative data rigorously.
- **[Evaluation](evaluation/)**: Prompts to review agent output and make structured ship-or-kill decisions. Use these to ensure what was built actually solved the user problem.
