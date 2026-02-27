# Commands

Commands are slash-invokable workflows you run inside an active agent session. Copy this `commands/` directory into your project root and invoke any command by name as you work.

---

## Commands vs. Prompts

Both help structure your work with an AI agent, but they're used at different moments:

- **Prompts** (in [`prompts/`](../prompts/)) are for starting a fresh session. Paste one as your opening instruction and let it drive from the beginning.
- **Commands** are for use once a session is already running. Invoke them to kick off a specific workflow step without breaking your current context.

Rule of thumb: open a session with a prompt, use commands throughout.

---

## Setup

### Claude Code

1. Copy this `commands/` directory into the root of your working project.
2. Open Claude Code in that project.
3. Type `/command-name` during any session to invoke it (e.g. `/clarify-ambiguity`).

Claude Code automatically discovers markdown files in a top-level `commands/` directory and exposes them as slash commands.

### Cursor

1. Copy this `commands/` directory into your project root.
2. Reference commands in your `.cursorrules` for persistent availability, or invoke them from Cursor's composer during a session.
3. Type the command name (e.g. `/first-pass-build`) to run it.

> [!TIP]
> If your Cursor setup is shared across a team, keep command names stable so everyone can rely on the same workflow language.

---

## Command reference

| Command | What it does | When to use it |
|---|---|---|
| `/build-session` | Assembles a skill, context docs, and a prompt into one complete session opener | At the start of any focused session, when you want a clean, context-rich kickoff |
| `/clarify-ambiguity` | Runs a guided one-question-at-a-time Q&A to surface hidden assumptions | When the request is messy or the real problem isn't clear yet |
| `/problem-statement` | Shapes a rough idea into a specific, actionable problem statement | Before any build work, when the problem still needs tightening |
| `/first-pass-build` | Confirms context and scope, then generates the smallest useful first version | When you're ready to prototype and want the agent to stay focused |
| `/review-output` | Structured critique of the agent's last output against user needs and reality | Immediately after a prototype or draft is produced |
| `/ship-or-kill` | Runs a go/no-go decision conversation and produces a decision log | When a prototype exists and you need a firm decision, not more iteration |

---

## Adding your own commands

Contributions are welcome. See [CONTRIBUTING.md](../CONTRIBUTING.md) for the process.

When writing a custom command:
- Start with a clear command name as the `# /heading`.
- Open with a concrete, answerable first question.
- Guide the conversation one step at a time. Don't try to do everything at once.
- End with a directly usable output: a decision, a draft, or a next action.

Custom commands can live in this same directory alongside the toolkit defaults.
