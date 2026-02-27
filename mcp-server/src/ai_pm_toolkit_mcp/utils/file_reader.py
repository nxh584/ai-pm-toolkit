"""File and markdown parsing helpers."""

from __future__ import annotations

import re
from pathlib import Path


def read_markdown_file(path: Path) -> str:
    """Read a markdown file from disk."""
    if not path.exists() or not path.is_file():
        raise FileNotFoundError(f"Markdown file not found at: {path}")
    return path.read_text(encoding="utf-8")


def list_markdown_files(directory: Path) -> list[str]:
    """List markdown file names in a directory without extensions."""
    if not directory.exists() or not directory.is_dir():
        raise FileNotFoundError(f"Directory not found at: {directory}")

    return sorted(
        entry.stem
        for entry in directory.iterdir()
        if entry.is_file() and entry.suffix.lower() == ".md"
    )


def parse_first_section(content: str, heading: str) -> str:
    """Extract text under a specific H2 heading from markdown content."""
    target = re.sub(r"^#+\s*", "", heading).strip().casefold()
    if not target:
        return ""

    lines = content.splitlines()
    in_section = False
    collected: list[str] = []

    for line in lines:
        match = re.match(r"^##\s+(.+?)\s*$", line)
        if match:
            current = match.group(1).strip().casefold()
            if in_section:
                break
            if current == target:
                in_section = True
                continue

        if in_section:
            collected.append(line)

    return "\n".join(collected).strip()
