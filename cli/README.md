# AI PM Toolkit CLI

## What this is

The AI PM Toolkit CLI is a lightweight npm package that lets you discover, fetch, search, and copy toolkit content directly from your terminal without cloning the repository. It pulls files live from GitHub, so you always get the latest version.

## Quick start

Run these commands in order to discover content and copy a prompt in under two minutes:

```bash
npx ai-pm-toolkit list prompts
npx ai-pm-toolkit search "clarify"
npx ai-pm-toolkit copy prompts/problem-shaping/clarify-ambiguity
```

## All commands

| Command | Arguments | What it does |
|---|---|---|
| `ai-pm-toolkit list [section]` | Optional section: `prompts`, `skills`, `workflows`, `templates`, `commands`, `all` | Lists toolkit resources with one-line descriptions. If omitted, shows summary counts. |
| `ai-pm-toolkit get <path>` | Toolkit path (with or without `.md`) | Fetches a file and prints terminal-friendly markdown output. |
| `ai-pm-toolkit search <query>` | Search string | Searches filenames and descriptions across prompts, skills, workflows, and commands. |
| `ai-pm-toolkit copy <path>` | Toolkit path (with or without `.md`) | Fetches a file and copies its full contents to your clipboard. |

## Using with Claude Code

A common pattern is to pull a skill or prompt into a local file, then bring that into your working session:

```bash
npx ai-pm-toolkit get skills/prototyping > session-context.md
```

You can then paste that content into Claude Code or attach the file as session context.

## Rate limiting

The CLI uses the GitHub API for directory reads. Unauthenticated GitHub API requests are rate-limited. If you hit limits, set a token and retry:

```bash
export GITHUB_TOKEN=your_token_here
```

Then rerun the same command. Raw file fetches and API calls will use the token automatically.

## Contributing

Contributions to CLI behaviour and content are welcome. See the main contribution guide: [../CONTRIBUTING.md](../CONTRIBUTING.md).
