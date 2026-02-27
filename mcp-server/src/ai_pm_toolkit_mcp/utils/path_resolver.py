"""Path resolution utilities for toolkit content."""

from __future__ import annotations

from pathlib import Path


def get_toolkit_root() -> Path:
    """Resolve the ai-pm-toolkit repository root from this package location."""
    root = Path(__file__).resolve().parents[4]
    if not root.exists():
        raise FileNotFoundError(f"Toolkit root could not be resolved. Expected path: {root}")
    return root


def _normalise_name(name: str) -> str:
    cleaned = name.strip()
    if cleaned.endswith(".md"):
        cleaned = cleaned[:-3]
    return cleaned


def _require_path(path: Path, resource_name: str) -> Path:
    if not path.exists() or not path.is_file():
        raise FileNotFoundError(f"{resource_name} not found. Expected file at: {path}")
    return path


def get_prompt_path(category: str, name: str) -> Path:
    prompt_name = _normalise_name(name)
    prompt_path = get_toolkit_root() / "prompts" / category / f"{prompt_name}.md"
    return _require_path(prompt_path, "Prompt")


def get_skill_path(name: str) -> Path:
    skill_name = _normalise_name(name)
    skill_path = get_toolkit_root() / "skills" / f"{skill_name}.md"
    return _require_path(skill_path, "Skill")


def get_workflow_path(name: str) -> Path:
    workflow_name = _normalise_name(name)
    workflow_path = get_toolkit_root() / "workflows" / f"{workflow_name}.md"
    return _require_path(workflow_path, "Workflow")


def get_template_path(name: str) -> Path:
    template_name = _normalise_name(name)
    template_path = get_toolkit_root() / "templates" / f"{template_name}.md"
    return _require_path(template_path, "Template")
