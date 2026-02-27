"""MCP server entry point for the AI PM Toolkit."""

from __future__ import annotations

import sys
from typing import Any

import mcp
from mcp.types import TextContent, Tool

from .tools import TOOLS

server = mcp.Server("ai-pm-toolkit")
TOOL_REGISTRY = {tool.name: handler for tool, handler in TOOLS}


@server.list_tools()
async def list_tools() -> list[Tool]:
    """Return all registered MCP tools."""
    return [tool for tool, _handler in TOOLS]


@server.call_tool()
async def call_tool(name: str, arguments: dict[str, Any] | None) -> list[TextContent]:
    """Call an MCP tool by name."""
    if name not in TOOL_REGISTRY:
        return [TextContent(type="text", text=f"Unknown tool: `{name}`")]

    handler = TOOL_REGISTRY[name]
    args = arguments or {}

    try:
        result = await handler(**args)
    except TypeError as exc:
        result = f"Invalid arguments for `{name}`: {exc}"
    except Exception as exc:  # pragma: no cover - defensive boundary
        result = f"Tool `{name}` failed: {exc}"

    return [TextContent(type="text", text=result)]


def main() -> None:
    """Run the MCP server over stdio transport."""
    try:
        mcp.run(server, transport="stdio")
    except Exception as exc:  # pragma: no cover - top-level process guard
        print(f"Failed to start ai-pm-toolkit MCP server: {exc}", file=sys.stderr)
        raise SystemExit(1) from exc


if __name__ == "__main__":
    main()
