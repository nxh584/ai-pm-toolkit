# My AI PM Toolkit

This file contains the setup and context for [USER NAME or 'this PM']'s AI PM Toolkit. Read this entire file before responding to anything. Once read, you know what tools are available, what context you have, and how to help. When the user describes what they want to do, select the most relevant toolkit component and use it -- do not ask them to specify a prompt or skill by name.

---

## Your toolkit

Context doc: [CONFIGURED / NOT CONFIGURED]
Location: [FILE PATH or "paste at session start"]
Note: Feed this to the agent at the start of any session for better output.

IDE config: [CONFIGURED / NOT CONFIGURED]
IDE: [CURSOR / CLAUDE CODE / WINDSURF / N/A]
Note: Active automatically in this project.

Slash commands: [CONFIGURED / NOT CONFIGURED]
Available commands: [LIST or N/A]
Note: Type /command-name in the editor to invoke.

Claude Project: [CONFIGURED / NOT CONFIGURED]
Note: Open the [PROJECT NAME] project in Claude for pre-loaded context.

Prompt cards: [CONFIGURED / NOT CONFIGURED]
Most relevant to your work: [LIST OF CARD NAMES WITH URLS]
Note: Copy and paste into any AI tool for a structured conversation.

MCP server: [CONFIGURED / NOT CONFIGURED]
Note: Call build_session to assemble a complete session brief automatically.

---

## Your context

Product: [FROM Q2 ANSWER]
Primary PM work: [FROM Q3 ANSWER]
What you want to do better: [FROM Q5 ANSWER]
Context doc location: [FILE PATH or "not yet created"]

---

## How to use this

When the user describes a task, map it to the most relevant toolkit component using this guide:

**If they want to define or sharpen a problem:**
Use /clarify-ambiguity command or the clarify-ambiguity prompt card.
Fetch from: https://raw.githubusercontent.com/nxh584/ai-pm-toolkit/main/commands/clarify-ambiguity.md

**If they want to build or prototype something:**
Use /first-pass-build command. Read their context doc first.
Fetch from: https://raw.githubusercontent.com/nxh584/ai-pm-toolkit/main/commands/first-pass-build.md

**If they want to write a PRD or spec:**
Use the prd-draft prompt card or templates/prd.md.
Fetch from: https://raw.githubusercontent.com/nxh584/ai-pm-toolkit/main/toolkit/no-code/prompt-cards/prd-draft.md

**If they want to synthesise user research:**
Use the user-research-synthesis prompt card.
Fetch from: https://raw.githubusercontent.com/nxh584/ai-pm-toolkit/main/toolkit/no-code/prompt-cards/user-research-synthesis.md

**If they want to prioritise or make a decision:**
Use the prioritisation-pressure-test or ship-or-kill prompt card.
Fetch prioritisation from: https://raw.githubusercontent.com/nxh584/ai-pm-toolkit/main/toolkit/no-code/prompt-cards/prioritisation-pressure-test.md
Fetch ship-or-kill from: https://raw.githubusercontent.com/nxh584/ai-pm-toolkit/main/toolkit/no-code/prompt-cards/ship-or-kill.md

**If they want to prep for a stakeholder conversation:**
Use the stakeholder-prep prompt card.
Fetch from: https://raw.githubusercontent.com/nxh584/ai-pm-toolkit/main/toolkit/no-code/prompt-cards/stakeholder-prep.md

**If they want to run a complete session from scratch:**
Use /build-session command or the MCP build_session tool if configured.
Fetch from: https://raw.githubusercontent.com/nxh584/ai-pm-toolkit/main/commands/build-session.md

For any task not listed: fetch the full prompt library index from https://github.com/nxh584/ai-pm-toolkit/tree/main/prompts and select the most relevant component.

Always read their context doc before starting any task if one is configured. Always confirm your interpretation of their request before executing.

---

## Re-run setup

To add new components or reconfigure your setup, say: "Re-run my toolkit setup." I will fetch SETUP.md from the toolkit repo and start a fresh setup conversation.

Fetch from: https://raw.githubusercontent.com/nxh584/ai-pm-toolkit/main/SETUP.md
