"""MCP tool definitions and handler registration."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Awaitable, Callable

try:
    from mcp.types import Tool
except ModuleNotFoundError:  # pragma: no cover - local fallback before dependency install
    @dataclass
    class Tool:  # type: ignore[override]
        name: str
        description: str
        inputSchema: dict[str, Any]

from .build_session import handle_build_session
from .get_context import handle_get_context
from .get_prompt import handle_get_prompt
from .get_skill import handle_get_skill
from .list_toolkit import handle_list_toolkit

Handler = Callable[..., Awaitable[str]]

TOOLS: list[tuple[Tool, Handler]] = [
    (
        Tool(
            name="get_prompt",
            description="Retrieve a prompt from the toolkit, ready to paste into an agent session.",
            inputSchema={
                "type": "object",
                "properties": {
                    "category": {
                        "type": "string",
                        "enum": ["problem-shaping", "prototyping", "research", "evaluation"],
                        "description": "The prompt category",
                    },
                    "name": {
                        "type": "string",
                        "description": "The prompt filename without .md extension",
                    },
                },
                "required": ["category", "name"],
            },
        ),
        handle_get_prompt,
    ),
    (
        Tool(
            name="get_skill",
            description="Retrieve a skill file to load into an agent session.",
            inputSchema={
                "type": "object",
                "properties": {
                    "name": {
                        "type": "string",
                        "description": "The skill name (e.g. problem-shaping, prototyping)",
                    }
                },
                "required": ["name"],
            },
        ),
        handle_get_skill,
    ),
    (
        Tool(
            name="get_context",
            description=(
                "Read a user, product, or project context doc from a project directory "
                "for session context injection."
            ),
            inputSchema={
                "type": "object",
                "properties": {
                    "type": {
                        "type": "string",
                        "enum": ["user", "product", "project"],
                        "description": "Which context doc to retrieve",
                    },
                    "project_path": {
                        "type": "string",
                        "description": "Absolute path to the project directory containing context-docs/",
                    },
                },
                "required": ["type", "project_path"],
            },
        ),
        handle_get_context,
    ),
    (
        Tool(
            name="list_toolkit",
            description="List toolkit components with practical one-line descriptions.",
            inputSchema={
                "type": "object",
                "properties": {
                    "section": {
                        "type": "string",
                        "enum": ["prompts", "skills", "workflows", "templates", "all"],
                        "description": "Which section to list. Use 'all' for full overview.",
                        "default": "all",
                    }
                },
                "required": [],
            },
        ),
        handle_list_toolkit,
    ),
    (
        Tool(
            name="build_session",
            description=(
                "Assemble a complete context-rich agent opener by combining a skill, "
                "project context docs, and a prompt."
            ),
            inputSchema={
                "type": "object",
                "properties": {
                    "skill": {
                        "type": "string",
                        "description": "Skill name to load as behavioral instructions",
                    },
                    "context_types": {
                        "type": "array",
                        "items": {
                            "type": "string",
                            "enum": ["user", "product", "project"],
                        },
                        "description": "Which context docs to inject",
                    },
                    "prompt_category": {
                        "type": "string",
                        "enum": ["problem-shaping", "prototyping", "research", "evaluation"],
                        "description": "Category of the prompt to use as the task",
                    },
                    "prompt_name": {
                        "type": "string",
                        "description": "Name of the prompt to use as the task",
                    },
                    "project_path": {
                        "type": "string",
                        "description": "Absolute path to the project with context-docs/",
                    },
                },
                "required": [
                    "skill",
                    "context_types",
                    "prompt_category",
                    "prompt_name",
                    "project_path",
                ],
            },
        ),
        handle_build_session,
    ),
]

__all__ = ["TOOLS"]
