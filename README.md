![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)
![Status: Active](https://img.shields.io/badge/Status-Active-success.svg)
![Made for: Cursor](https://img.shields.io/badge/Made%20for-Cursor-black.svg)
![Made for: Claude Code](https://img.shields.io/badge/Made%20for-Claude%20Code-orange.svg)
![Made for: Windsurf](https://img.shields.io/badge/Made%20for-Windsurf-blueviolet.svg)

# AI PM Toolkit

The `ai-pm-toolkit` is a comprehensive GitHub repository designed primarily for Product Managers who are looking to adopt an AI native workflow. The modern PM's bottleneck is quickly moving away from the cycle of translating requirements that get handed off to developers, reviewing, and then iterating on them, to PM's who are able to quickly prototype and validate themselves. This toolkit provides resources to quickly help you adopt the core skills of the AI-era PM: problem shaping, context curation, and evaluation, empowering you to effectively collaborate with AI agents and ship better products.

## Not a developer? Start here.

You don't need to write code, clone this repo, or understand how any of the tooling works to get value from this toolkit. Everything here is text — prompts you paste into an AI tool, templates you copy into a doc, instructions you give to an agent.

**The fastest path to value (under 5 minutes, no setup):**

1. Install an AI tool if you don't have one. The toolkit works best with [Claude](https://claude.ai) (free tier is fine) or [Cursor](https://cursor.com) if you want the full experience. Both have free tiers.

2. Open a new conversation and paste this to start:

   > "I want to work on a product problem. Before I describe it,
   > please read these instructions and confirm you understand
   > them: [paste the contents of skills/problem-shaping.md]"

   Not sure where to find that file? Run this in any terminal:

   ```bash
   npx ai-pm-toolkit get skills/problem-shaping
   ```

   Or just browse to it on GitHub and copy the raw text.

3. Describe your problem. Let the agent ask you questions. Iterate.

That's it. No installation. No config. No code.

**When you're ready for more:**

- The [commands/](./commands/) directory has slash commands that work in Claude Code and Cursor. Copy the whole directory into your project and type `/clarify-ambiguity` to start a guided problem-shaping session.
- The [context-docs/](./context-docs/) templates help you get dramatically better output by giving the agent the right background before you start.
- The [QUICKSTART.md](./QUICKSTART.md) walks through a 30-minute session that covers the core workflow end-to-end.

The more of this you use, the more natural it becomes. Most PMs who engage with this toolkit seriously find that within a week, the workflow feels more natural than writing specs the old way.

## Philosophy

You do not need to adopt everything here to get value out of this toolkit. The approach is fundamentally modular, so grab exactly what you need for the problem at hand and leave the rest. Whether you're looking to refine how you shape a problem, need a better context document to ground your AI agent, or want a structured workflow for going from discovery to an actionable spec, you can integrate these pieces into your existing process. The goal is to augment your PM skills, not to force you into a rigid new framework. Feel free to add or remove things here depending on your needs and workflow as these will be different for everyone.

## Directory Map

```text
ai-pm-toolkit/
├── README.md            # Main project overview and onboarding paths
├── QUICKSTART.md        # 30-minute guided setup and first workflow
├── CONTRIBUTING.md      # Contribution scope, standards, and process
├── CODE_OF_CONDUCT.md   # Community conduct expectations
├── .github/             # PR templates, issue forms, and repo automation
├── ide-setup/           # Drop-in config files for Cursor, Claude Code, and Windsurf
├── context-docs/        # Templates for feeding rich context to agents
├── templates/           # PM artefact templates (PRD, spec, problem statement)
├── prompts/             # Reusable prompts organised by workflow stage
├── commands/            # Slash commands for in-session use in Claude Code and Cursor
├── skills/              # Agent instruction sets for PM-mode behaviour
├── workflows/           # End-to-end playbooks for common PM tasks
├── examples/            # Fully worked, annotated examples
├── cli/                 # npx CLI for discovering and copying toolkit content
└── mcp-server/          # Python MCP server for Claude Code integration
```

## Start Here

Depending on what you want to achieve today, jump into the right section:

- **"I want to build something today"** → Start with [QUICKSTART.md](QUICKSTART.md), then run the [zero-to-prototype workflow](workflows/zero-to-prototype.md), and use [`/first-pass-build`](commands/first-pass-build.md) when you are ready to generate the first implementation.
- **"I use Cursor, Claude Code, or Windsurf"** → Go to [ide-setup/](ide-setup/) for environment rules, then copy [commands/](commands/) into your project for reusable in-session slash workflows.
- **"I want templates for my PM docs"** → Use [templates/](templates/) for artefact structure and [prompts/](prompts/) to drive each stage of the work.
- **"I just want to try one thing right now"** → No clone required. Run:
  ```bash
  npx ai-pm-toolkit list prompts
  npx ai-pm-toolkit search "clarify"
  npx ai-pm-toolkit copy prompts/problem-shaping/clarify-ambiguity
  ```

## IDE Setup

The [ide-setup/](ide-setup/) directory includes ready-to-use configuration files for Cursor, Claude Code, and Windsurf. These files are designed to make your AI agent behave more like a PM collaborator and less like a generic coding assistant.

## MCP Server

The toolkit includes an installable MCP server that brings prompts, skills, workflows, templates, and project context docs directly into MCP-compatible clients. Its headline feature is `build_session`, which assembles a full, context-rich opening message by combining skill instructions, selected context docs, and a prompt in one call. If you are not using MCP yet, the [commands/](commands/) directory gives you interactive manual equivalents of the same workflows, including [`/build-session`](commands/build-session.md). For setup and usage, see [mcp-server/README.md](mcp-server/README.md).

## Contributing

If you want to contribute new prompts, skills, workflows, or slash commands, start with [CONTRIBUTING.md](CONTRIBUTING.md) for contribution scope, file format requirements, and review criteria.
