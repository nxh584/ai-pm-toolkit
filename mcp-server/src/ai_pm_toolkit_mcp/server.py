"""MCP server entry point for the AI PM Toolkit."""

from __future__ import annotations

import argparse
import asyncio
import sys
from typing import Any

from mcp import NotificationOptions
from mcp.server.lowlevel import Server
from mcp.server.models import InitializationOptions
from mcp.server.stdio import stdio_server
from mcp.types import TextContent, Tool

from .tools import TOOLS

server = Server("ai-pm-toolkit")
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


async def run_stdio_server() -> None:
    """Run the MCP server over stdio transport."""
    async with stdio_server() as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            InitializationOptions(
                server_name="ai-pm-toolkit",
                server_version="1.0.0",
                capabilities=server.get_capabilities(
                    notification_options=NotificationOptions(),
                    experimental_capabilities={},
                ),
            ),
        )


def main(argv: list[str] | None = None) -> None:
    """CLI entry point for running the MCP server."""
    parser = argparse.ArgumentParser(
        prog="ai-pm-toolkit-mcp",
        description="Run the AI PM Toolkit MCP server over stdio.",
    )
    parser.add_argument(
        "--transport",
        choices=["stdio"],
        default="stdio",
        help="Transport to run. Only stdio is currently supported.",
    )
    parser.parse_args(argv)

    try:
        asyncio.run(run_stdio_server())
    except KeyboardInterrupt:
        # Graceful local shutdown.
        return
    except Exception as exc:  # pragma: no cover - top-level process guard
        print(f"Failed to start ai-pm-toolkit MCP server: {exc}", file=sys.stderr)
        raise SystemExit(1) from exc


if __name__ == "__main__":
    main()
