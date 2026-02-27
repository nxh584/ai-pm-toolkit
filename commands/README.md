# Slash Commands

## What these are

The files in this directory define reusable slash commands for day-to-day PM work inside an active agent session.

How they differ from `prompts/`:
- Prompts are copy-paste openers for starting a new session.
- Commands are in-session tools you invoke repeatedly as you work.

Use prompts when you are opening a fresh conversation. Use commands when the session is already running and you want a specific guided workflow.

## How to use them in Claude Code

1. Copy this `commands/` directory into the root of your working project.
2. Open Claude Code in that project.
3. Start or continue a session.
4. Invoke a command by typing `/command-name` (for example `/clarify-ambiguity`).

Claude Code automatically discovers markdown files in a top-level `commands/` directory and exposes them as slash commands.

## How to use them in Cursor

1. Copy this `commands/` directory into your project root.
2. Open Cursor in that project.
3. Add command behaviour references in your `.cursorrules` if you want persistent command guidance, or invoke commands from Cursor's command palette/composer slash workflow.
4. Run the command by name (for example `/first-pass-build`) during your session.

If your Cursor setup is team-shared, keep command names stable so everyone can rely on the same workflow language.

## Command reference

| Command | Description | When to reach for it |
|---|---|---|
| `/problem-statement` | Conversationally shapes a vague problem into a clear problem statement. | When the problem is still fuzzy and needs tightening before any build work. |
| `/first-pass-build` | Forces context check and scope confirmation before writing code. | When you are ready to prototype and want the smallest useful first version. |
| `/build-session` | Assembles skill instructions, context, and task into one session brief. | At the start of focused PM work when you want a clean, context-rich kickoff. |
| `/clarify-ambiguity` | Guides a one-question-at-a-time ambiguity-clearing conversation. | When the request is messy and you need to identify the real problem first. |
| `/review-output` | Critiques generated output against real user and delivery reality. | Immediately after a prototype or draft is produced and needs an honest assessment. |
| `/ship-or-kill` | Runs a structured go/no-go decision conversation with decision log output. | When a prototype exists and you need a firm decision, not another vague iteration. |

## Adding your own

Community contributions for commands are welcome. Follow the contribution process in [CONTRIBUTING.md](../CONTRIBUTING.md).

Custom commands should:
- Use clear command identity (`# /your-command-name`).
- Open with a concrete, answerable first question.
- Guide the conversation one step at a time.
- End with a directly usable output (decision, draft, or plan).

You can keep custom commands in this same directory alongside the toolkit defaults.
