"""Tool handler for retrieving skills."""

from __future__ import annotations

from ..utils import get_skill_path, get_toolkit_root, list_markdown_files, read_markdown_file


async def handle_get_skill(name: str) -> str:
    """Return full skill content for the requested skill."""
    try:
        skill_path = get_skill_path(name)
        content = read_markdown_file(skill_path)
        source = skill_path.relative_to(get_toolkit_root()).as_posix()
        return (
            "Load the following skill instructions into your current session:\n\n"
            f"Source: `{source}`\n\n"
            f"{content}"
        )
    except FileNotFoundError as exc:
        skills_dir = get_toolkit_root() / "skills"
        available = list_markdown_files(skills_dir)
        suggestions = "\n".join(f"- `{item}`" for item in available)
        return (
            f"Could not find skill `{name}`.\n"
            f"Details: {exc}\n\n"
            "Available skills:\n"
            f"{suggestions}"
        )
