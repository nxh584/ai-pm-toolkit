"""Tool handler for listing toolkit components with descriptions."""

from __future__ import annotations

from pathlib import Path

from ..utils import get_toolkit_root, list_markdown_files, parse_first_section, read_markdown_file

VALID_SECTIONS = {"prompts", "skills", "workflows", "templates", "all"}
PROMPT_CATEGORIES = ["problem-shaping", "prototyping", "research", "evaluation"]


def _normalise_line(text: str) -> str:
    compact = " ".join(text.split())
    return compact.rstrip(".") + "." if compact else ""


def _first_non_heading_paragraph(content: str) -> str:
    lines: list[str] = []
    for raw in content.splitlines():
        line = raw.strip()
        if not line:
            if lines:
                break
            continue
        if line.startswith("#"):
            continue
        lines.append(line)
    return _normalise_line(" ".join(lines))


def _description_for_file(path: Path, section: str) -> str:
    content = read_markdown_file(path)

    if section == "prompts":
        text = parse_first_section(content, "When to use this")
    elif section == "workflows":
        text = parse_first_section(content, "What this is")
    elif section == "skills":
        text = parse_first_section(content, "What this skill does")
        if not text:
            text = parse_first_section(content, "When to load this skill")
    else:
        text = ""

    description = _normalise_line(text)
    if description:
        return description

    fallback = _first_non_heading_paragraph(content)
    return fallback or "No description available."


def _filter_items(items: list[str]) -> list[str]:
    return [item for item in items if item.casefold() != "readme"]


def _render_prompts(root: Path) -> str:
    lines: list[str] = ["## Prompts"]
    for category in PROMPT_CATEGORIES:
        category_dir = root / "prompts" / category
        lines.append("")
        lines.append(f"### {category}")
        try:
            items = _filter_items(list_markdown_files(category_dir))
        except FileNotFoundError:
            lines.append("- No prompts found.")
            continue

        if not items:
            lines.append("- No prompts found.")
            continue

        for item in items:
            path = category_dir / f"{item}.md"
            lines.append(f"- `{item}`: {_description_for_file(path, 'prompts')}")

    return "\n".join(lines)


def _render_section(root: Path, section: str, heading: str) -> str:
    lines: list[str] = [f"## {heading}"]
    section_dir = root / section

    try:
        items = _filter_items(list_markdown_files(section_dir))
    except FileNotFoundError:
        return "\n".join(lines + ["", "- No files found."])

    if not items:
        return "\n".join(lines + ["", "- No files found."])

    for item in items:
        file_path = section_dir / f"{item}.md"
        lines.append(f"- `{item}`: {_description_for_file(file_path, section)}")

    return "\n".join(lines)


async def handle_list_toolkit(section: str = "all") -> str:
    """List toolkit components with one-line descriptions."""
    selected = (section or "all").strip().lower()
    if selected not in VALID_SECTIONS:
        supported = ", ".join(sorted(VALID_SECTIONS))
        return f"Unsupported section `{section}`. Supported values: {supported}."

    root = get_toolkit_root()

    if selected == "prompts":
        return _render_prompts(root)
    if selected == "skills":
        return _render_section(root, "skills", "Skills")
    if selected == "workflows":
        return _render_section(root, "workflows", "Workflows")
    if selected == "templates":
        return _render_section(root, "templates", "Templates")

    blocks = [
        _render_prompts(root),
        _render_section(root, "skills", "Skills"),
        _render_section(root, "workflows", "Workflows"),
        _render_section(root, "templates", "Templates"),
    ]
    return "\n\n".join(blocks)
