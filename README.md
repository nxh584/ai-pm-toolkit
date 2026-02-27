![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)
![Status: Active](https://img.shields.io/badge/Status-Active-success.svg)
![Made for: Cursor](https://img.shields.io/badge/Made%20for-Cursor-black.svg)
![Made for: Claude Code](https://img.shields.io/badge/Made%20for-Claude%20Code-orange.svg)
![Made for: Windsurf](https://img.shields.io/badge/Made%20for-Windsurf-blueviolet.svg)

# AI PM Toolkit

A practical toolkit for Product Managers who want to work effectively with AI agents. It gives you the prompts, templates, context documents, and structured workflows to move faster. From problem definition through to working prototypes without needing to write code yourself.

There's a shift in the product management landscape. The old cycle of writing specs, handing them off, and waiting for reviews is being replaced by something faster: PMs who can shape problems precisely, give agents the right context, and evaluate output critically. This toolkit helps you build exactly those skills and incorporate them into your daily workflow. Take what you need to improve your process, don't feel obligated to use everything. This is a living document and will be updated regularly as the landscape evolves.

---

## New here? Start in 5 minutes, no setup needed

You don't need to install anything, clone this repo, or understand how any of the tooling works to get immediate value.

**All you need is an AI tool — [Claude](https://claude.ai) (free), [Cursor](https://cursor.com) (free tier), or anything similar.**

**Do this right now:**

1. Open a new conversation in your AI tool of choice.
2. Browse to [`skills/problem-shaping.md`](./skills/problem-shaping.md) on GitHub and copy the raw text.
3. Paste it into your conversation with this message:

   > "I want to work through a product problem. Please read these instructions first and confirm you understand them: [paste the file contents here]"

4. Describe your problem. Let the agent ask you questions. Iterate.

That's it. No installation, no config, no code. You just turned your AI tool into a structured product thinking partner.

**Ready to go deeper?**

- The [QUICKSTART.md](./QUICKSTART.md) walks you through a focused 30-minute session that covers the full core workflow.
- The [CHEAT_SHEET.md](./CHEAT_SHEET.md) is a single-page reference of every useful command, prompt, and template — keep it open while you work.
- The [commands/](./commands/) directory has slash commands for Claude Code and Cursor. Copy the folder into your project and type `/clarify-ambiguity` to start a guided session.

---

## What's in this toolkit

Everything here is a plain text file — prompts, templates, and instructions. Use what you need and ignore the rest.

```text
ai-pm-toolkit/
├── README.md              # This file
├── QUICKSTART.md          # Guided 30-minute first session
├── CHEAT_SHEET.md         # Quick-reference card for commands, prompts, and templates
├── CONTRIBUTING.md        # How to contribute new content
├── CODE_OF_CONDUCT.md     # Community expectations
├── .github/               # PR templates, issue forms, and repo automation
├── ide-setup/             # Drop-in config files for Cursor, Claude Code, and Windsurf
├── context-docs/          # Templates for giving agents the right background
├── templates/             # PM document templates (PRD, spec, problem statement, etc.)
├── prompts/               # Reusable prompts organised by workflow stage
├── commands/              # Slash commands for use inside Claude Code and Cursor
├── skills/                # Agent instruction sets that shape how it behaves
├── workflows/             # Step-by-step playbooks for common PM tasks
├── examples/              # Fully worked, annotated worked examples
├── cli/                   # Optional CLI: discover and copy content via npx
└── mcp-server/            # Optional MCP server for Claude Code integration
```

---

## Pick your starting point

Jump to the section that matches what you want to do today.

### "I want to build something today"
→ Open [QUICKSTART.md](QUICKSTART.md) and follow the 30-minute path.
→ Then run the [Zero-to-Prototype workflow](workflows/zero-to-prototype.md).
→ When you're ready to generate a first implementation, invoke [`/first-pass-build`](commands/first-pass-build.md).

### "I use Cursor, Claude Code, or Windsurf"
→ Go to [ide-setup/](ide-setup/) and copy the config file for your IDE into your project root.
→ Copy [commands/](commands/) into the same project root to enable slash commands.
→ Your agent will now behave as a PM collaborator, not just a code generator.

### "I need better PM documents"
→ Use [templates/](templates/) for structured artefact formats (PRDs, specs, problem statements).
→ Use [prompts/](prompts/) to drive each stage: problem shaping, research, prototyping, and evaluation.

### "I just want to grab one thing quickly"
→ No clone needed. Use the CLI:
```bash
npx ai-pm-toolkit list prompts
npx ai-pm-toolkit search "clarify"
npx ai-pm-toolkit copy prompts/problem-shaping/clarify-ambiguity
```

---

## Philosophy

This toolkit is deliberately modular. You don't need to adopt everything — grab what's useful for the problem you're working on today and leave the rest.

The three core skills it's designed to strengthen are:

- **Problem shaping** — being precise about what you're actually trying to solve before involving an agent.
- **Context curation** — giving the agent the right background so it doesn't have to guess (and guess wrong).
- **Evaluation** — knowing how to judge agent output critically and iterate toward something useful.

These will compound and this workflow will start to feel more natural than the old way very quickly.

---

## IDE Setup

[ide-setup/](ide-setup/) contains ready-to-use configuration files for **Cursor**, **Claude Code**, and **Windsurf**. Copy the right file into your project root before starting a session. This shapes the agent's default behaviour so it asks better questions, respects scope, and surfaces tradeoffs rather than just generating output.

## MCP Server

The toolkit ships an installable MCP server that exposes its prompts, skills, workflows, templates, and context docs directly inside MCP-compatible clients. Its headline feature is `build_session`, which assembles a complete, context-rich opening message from skill instructions, selected context docs, and a prompt — in a single call.

If you're not using MCP yet, the [commands/](commands/) directory has manual equivalents of the same workflows, including [`/build-session`](commands/build-session.md). Setup and usage details are in [mcp-server/README.md](mcp-server/README.md).

## Contributing

Contributions welcome. See [CONTRIBUTING.md](CONTRIBUTING.md) for scope, file format requirements, and the review process.
