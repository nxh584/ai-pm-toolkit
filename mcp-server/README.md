# MCP Server

The AI PM Toolkit MCP server exposes the toolkit as callable tools inside MCP-compatible clients. Its headline feature is `build_session`: one call that assembles a complete, context-rich session opener from your skills, context docs, and a chosen prompt.

---

## Not using MCP yet?

No problem. The [`commands/`](../commands/) directory provides manual equivalents of every tool this server offers. Specifically, [`/build-session`](../commands/build-session.md) is the manual version of `build_session`. Start there and add the MCP server later when you want automated context injection.

---

## What it does

The server exposes five tools:

| Tool | What it does |
|---|---|
| `build_session` | Assembles a skill, context docs, and a prompt into one ready-to-run session opener |
| `list_toolkit` | Lists available prompts, skills, workflows, and templates with one-line descriptions |
| `get_prompt` | Loads a specific prompt file by category and name |
| `get_skill` | Loads a specific skill as behavioural instructions for the current session |
| `get_context` | Loads `user`, `product`, or `project` context docs from your project directory |

---

## Prerequisites

- Python 3.10 or above
- An MCP-compatible client (Claude Code or Cursor with MCP support)
- `uv` is recommended for installation (faster and simpler), but standard `pip` works too

---

## Installation

### With `uv` (recommended)

```bash
cd mcp-server
uv pip install -e .
```

### With `pip`

```bash
cd mcp-server
pip install -e .
```

---

## Connecting to Claude Code

1. Install the server as above.
2. Open your Claude Code MCP config file:
   - **macOS / Linux:** `~/.claude/claude_desktop_config.json`
   - **Windows:** `%APPDATA%\Claude\claude_desktop_config.json`
3. Add the server entry:

```json
{
  "mcpServers": {
    "ai-pm-toolkit": {
      "command": "ai-pm-toolkit-mcp"
    }
  }
}
```

4. Restart Claude Code.

Because the server is installed as a package script, no absolute path is needed. If your client can't find the command (for example, because it's installed in a virtual environment), use the full path instead:

```json
{
  "mcpServers": {
    "ai-pm-toolkit": {
      "command": "/absolute/path/to/mcp-server/.venv/bin/ai-pm-toolkit-mcp"
    }
  }
}
```

---

## Connecting to Cursor

1. Open Cursor settings and find the MCP servers section.
2. Add a server named `ai-pm-toolkit` with the same config as above.
3. Save and restart Cursor.

---

## Tool reference

| Tool | Key inputs |
|---|---|
| `build_session` | `skill`, `context_types`, `prompt_category`, `prompt_name`, `project_path` |
| `list_toolkit` | `section` |
| `get_prompt` | `category`, `name` |
| `get_skill` | `name` |
| `get_context` | `type`, `project_path` |

---

## Example usage

### Discover available prompts

```json
{
  "tool": "list_toolkit",
  "arguments": { "section": "prompts" }
}
```

### Load context and a skill before building

```json
{
  "tool": "get_context",
  "arguments": {
    "type": "product",
    "project_path": "/Users/you/projects/my-project"
  }
}
```

```json
{
  "tool": "get_skill",
  "arguments": { "name": "prototyping" }
}
```

### Build a complete session opener in one call

```json
{
  "tool": "build_session",
  "arguments": {
    "skill": "problem-shaping",
    "context_types": ["user", "product", "project"],
    "prompt_category": "problem-shaping",
    "prompt_name": "define-success",
    "project_path": "/Users/you/projects/my-project"
  }
}
```

This returns a single ready-to-paste message that includes the skill instructions, all three context documents, and the prompt. Everything the agent needs to start working.

---

## Troubleshooting

### `command not found: ai-pm-toolkit-mcp`

The package isn't installed in the environment your client is using, or that environment isn't active.

**Fix:**
- Reinstall from `mcp-server/` with `uv pip install -e .` or `pip install -e .`
- If using a virtual environment, activate it before installing
- Or set `command` to the full absolute path of the binary in your venv

### Context docs not found

The server looks for context docs at:
- `<project_path>/context-docs/user-context.md`
- `<project_path>/context-docs/product-context.md`
- `<project_path>/context-docs/project-context.md`

If they're missing, copy the templates from the toolkit's [`context-docs/`](../context-docs/) directory into your project and fill them in.

### Server not appearing in Claude Code

- Double-check the config file path:
  - macOS / Linux: `~/.claude/claude_desktop_config.json`
  - Windows: `%APPDATA%\Claude\claude_desktop_config.json`
- Validate the JSON (a single trailing comma will break loading)
- Restart Claude Code after saving any changes to the config
