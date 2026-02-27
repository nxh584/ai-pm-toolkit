# CLI

A lightweight command-line tool for discovering, fetching, and copying toolkit content without cloning the repository. It pulls files live from GitHub, so you always get the latest version.

You need Node.js installed, but you don't need to install the CLI itself. `npx` handles that automatically.

---

## Quick start

```bash
# See what prompts are available
npx ai-pm-toolkit list prompts

# Search for something specific
npx ai-pm-toolkit search "clarify"

# Copy a prompt to your clipboard
npx ai-pm-toolkit copy prompts/problem-shaping/clarify-ambiguity
```

---

## All commands

| Command | What it does |
|---|---|
| `npx ai-pm-toolkit list [section]` | Lists available content with one-line descriptions. Section can be: `prompts`, `skills`, `workflows`, `templates`, `commands`, or `all`. Omit for a summary count. |
| `npx ai-pm-toolkit get <path>` | Fetches a file and prints it to the terminal. Path can be with or without `.md`. |
| `npx ai-pm-toolkit search <query>` | Searches filenames and descriptions across prompts, skills, workflows, and commands. |
| `npx ai-pm-toolkit copy <path>` | Fetches a file and copies its full contents to your clipboard. |

---

## Common patterns

**Save a skill to a local file before a session:**
```bash
npx ai-pm-toolkit get skills/prototyping > session-context.md
```
Then paste the contents into your agent session, or attach the file directly.

**Find the right prompt when you're not sure which one to use:**
```bash
npx ai-pm-toolkit search "problem"
npx ai-pm-toolkit search "evaluate"
```

**Grab a template and open it for editing:**
```bash
npx ai-pm-toolkit copy templates/prd
```
Then paste it into your editor or directly into your agent session.

---

## Rate limiting

The CLI uses the GitHub API for directory listings. Unauthenticated requests have a rate limit. If you hit it:

```bash
export GITHUB_TOKEN=your_token_here
```

Then rerun the same command. File fetches and API calls will use the token automatically.

---

## Contributing

Contributions to CLI behaviour are welcome. See [CONTRIBUTING.md](../CONTRIBUTING.md) for the process.
