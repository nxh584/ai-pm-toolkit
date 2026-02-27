"""Tool handler for loading user project context docs."""

from __future__ import annotations

from pathlib import Path

from ..utils import get_toolkit_root, read_markdown_file

VALID_CONTEXT_TYPES = {"user", "product", "project"}


async def handle_get_context(type: str, project_path: str) -> str:
    """Load a context document from a user's project path."""
    context_type = type.strip().lower()
    if context_type not in VALID_CONTEXT_TYPES:
        supported = ", ".join(sorted(VALID_CONTEXT_TYPES))
        return f"Unsupported context type `{type}`. Supported values: {supported}."

    project_root = Path(project_path).expanduser().resolve()
    expected_path = project_root / "context-docs" / f"{context_type}-context.md"

    if expected_path.exists() and expected_path.is_file():
        content = read_markdown_file(expected_path)
        return (
            f"Loaded `{context_type}` context from `{expected_path}`.\n\n"
            f"{content}"
        )

    template_path = get_toolkit_root() / "context-docs" / f"{context_type}-context.md"
    relative_expected = Path("context-docs") / f"{context_type}-context.md"
    return (
        f"Context file not found at `{expected_path}`.\n\n"
        "To use this tool, add your filled-in context doc to your project at:\n"
        f"- `{relative_expected}`\n\n"
        "You can start from the toolkit template at:\n"
        f"- `{template_path}`"
    )
