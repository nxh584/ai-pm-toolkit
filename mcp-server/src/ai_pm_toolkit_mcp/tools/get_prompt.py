"""Tool handler for retrieving prompts."""

from __future__ import annotations

from ..utils import get_prompt_path, get_toolkit_root, list_markdown_files, read_markdown_file


async def handle_get_prompt(category: str, name: str) -> str:
    """Return full prompt content for a given category and name."""
    try:
        prompt_path = get_prompt_path(category, name)
        content = read_markdown_file(prompt_path)
        source = prompt_path.relative_to(get_toolkit_root()).as_posix()
        return f"Source: `{source}`\n\n{content}"
    except FileNotFoundError as exc:
        category_dir = get_toolkit_root() / "prompts" / category
        try:
            available = list_markdown_files(category_dir)
        except FileNotFoundError:
            available = []

        if available:
            suggestions = "\n".join(f"- `{item}`" for item in available)
            return (
                f"Could not find prompt `{name}` in category `{category}`.\n"
                f"Details: {exc}\n\n"
                "Available prompts in this category:\n"
                f"{suggestions}"
            )

        return (
            f"Could not find prompt `{name}` in category `{category}`.\n"
            f"Details: {exc}\n\n"
            f"No prompts were found in `{category_dir}`."
        )
