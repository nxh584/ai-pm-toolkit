# AI PM Toolkit MCP Server

The AI PM Toolkit MCP server exposes your toolkit as callable tools inside MCP-compatible clients. The headline feature is `build_session`: one call that assembles a complete, context-rich agent session from your toolkit, ready to paste into Claude Code.

## What this does

This server exposes five tools:

- `build_session`: Combine a skill, project context docs, and a prompt into a single ready-to-run session opener.
- `list_toolkit`: Discover available prompts, skills, workflows, and templates with one-line descriptions.
- `get_prompt`: Load a specific prompt file by category and name.
- `get_skill`: Load a specific skill file as behavioural instructions for the current session.
- `get_context`: Load `user`, `product`, or `project` context docs from your current project directory.

## Prerequisites

- Python 3.10+
- Recommended: `uv` (faster installs and simpler environment handling)
- An MCP-compatible client (Claude Code, Cursor with MCP support)

## Installation

### With `uv` (recommended)

```bash
cd mcp-server
uv pip install -e .
```

### With standard `pip`

```bash
cd mcp-server
pip install -e .
```

## Connecting to Claude Code

1. Install this server as shown above.
2. Open your Claude Code MCP config file:
- macOS/Linux: `~/.claude/claude_desktop_config.json`
- Windows: `%APPDATA%\Claude\claude_desktop_config.json`
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

Because the server is installed as a package script, no absolute path is required.

If you installed into a virtual environment and your client cannot see that environment's `PATH`, use the full command path instead:

```json
{
  "mcpServers": {
    "ai-pm-toolkit": {
      "command": "/absolute/path/to/mcp-server/.venv/bin/ai-pm-toolkit-mcp"
    }
  }
}
```

Then restart Claude Code.

## Connecting to Cursor

1. Open Cursor settings and find the MCP servers configuration area.
2. Add a server named `ai-pm-toolkit`.
3. Use the same command configuration:

```json
{
  "mcpServers": {
    "ai-pm-toolkit": {
      "command": "ai-pm-toolkit-mcp"
    }
  }
}
```

4. Save settings and restart Cursor so the server is reloaded.

If you are using a virtual environment, point `command` to the full path of that environment's `ai-pm-toolkit-mcp` binary.

## Tool reference

| Tool | Purpose | Key inputs |
|---|---|---|
| `build_session` | Build one complete session opener from skill + context + prompt | `skill`, `context_types`, `prompt_category`, `prompt_name`, `project_path` |
| `list_toolkit` | Discover toolkit components without leaving the IDE | `section` |
| `get_prompt` | Retrieve one prompt file for direct use | `category`, `name` |
| `get_skill` | Retrieve one skill file for behavioural instructions | `name` |
| `get_context` | Retrieve filled project context docs for injection | `type`, `project_path` |

## Example usage

### 1. Discover prompts

Request:

```json
{
  "tool": "list_toolkit",
  "arguments": {
    "section": "prompts"
  }
}
```

Representative output:

```markdown
## Prompts

### problem-shaping
- `clarify-ambiguity`: Use this when the request is broad and the constraints are unclear.
- `define-success`: Use this to convert vague goals into concrete success criteria.
```

### 2. Load context + skill before a build

Request 1:

```json
{
  "tool": "get_context",
  "arguments": {
    "type": "product",
    "project_path": "/Users/you/projects/customer-portal"
  }
}
```

Request 2:

```json
{
  "tool": "get_skill",
  "arguments": {
    "name": "prototyping"
  }
}
```

Representative result:
- Product context is loaded from `/Users/you/projects/customer-portal/context-docs/product-context.md`.
- Skill instructions are returned with a load note so they can be applied as session behaviour.

### 3. Build a full session opener

Request:

```json
{
  "tool": "build_session",
  "arguments": {
    "skill": "problem-shaping",
    "context_types": ["user", "product", "project"],
    "prompt_category": "problem-shaping",
    "prompt_name": "define-success",
    "project_path": "/Users/you/projects/customer-portal"
  }
}
```

Representative output:

```markdown
## Agent Session: problem-shaping + define-success

### Your behavioral instructions for this session:
Load the following skill instructions into your current session:
...

---

### Context loaded for this session:
#### user context
Loaded `user` context from `/Users/you/projects/customer-portal/context-docs/user-context.md`.
...

---

### Your task:
Source: `prompts/problem-shaping/define-success.md`
...
```

## Troubleshooting

### `command not found: ai-pm-toolkit-mcp`

Cause: the package is not installed in the environment your client uses, or that environment is not active.

Fix:
- Reinstall from `mcp-server/` with `uv pip install -e .` or `pip install -e .`.
- If using a virtual environment, activate it before installing.
- Alternatively set `command` to the absolute path of the venv binary.

### Context docs not found

The server looks for context docs in:
- `<project_path>/context-docs/user-context.md`
- `<project_path>/context-docs/product-context.md`
- `<project_path>/context-docs/project-context.md`

If missing, copy the toolkit templates from `context-docs/` and fill them in your project.

### Server not appearing in Claude Code

- Confirm the config file location is correct:
- macOS/Linux: `~/.claude/claude_desktop_config.json`
- Windows: `%APPDATA%\Claude\claude_desktop_config.json`
- Validate JSON syntax (a trailing comma will break loading).
- Restart Claude Code after saving the config.
