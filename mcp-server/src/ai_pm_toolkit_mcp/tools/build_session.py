"""Tool handler for composing full agent session openers."""

from __future__ import annotations

from .get_context import handle_get_context
from .get_prompt import handle_get_prompt
from .get_skill import handle_get_skill

VALID_CONTEXT_TYPES = {"user", "product", "project"}


async def handle_build_session(
    skill: str,
    context_types: list[str],
    prompt_category: str,
    prompt_name: str,
    project_path: str,
) -> str:
    """Assemble a full agent session block from toolkit components."""
    session_title = f"## Agent Session: {skill} + {prompt_name}"

    skill_block = await handle_get_skill(skill)
    prompt_block = await handle_get_prompt(prompt_category, prompt_name)

    requested_contexts = context_types or []
    context_sections: list[str] = []
    warnings: list[str] = []

    for item in requested_contexts:
        context_type = item.strip().lower()
        if context_type not in VALID_CONTEXT_TYPES:
            warnings.append(
                f"Unsupported context type `{item}` skipped. Supported values: user, product, project."
            )
            continue

        context_result = await handle_get_context(context_type, project_path)
        if context_result.startswith("Context file not found"):
            warnings.append(context_result)
            context_sections.append(
                f"#### {context_type} context\nWarning: could not load this context. See warnings below."
            )
        else:
            context_sections.append(f"#### {context_type} context\n{context_result}")

    if not context_sections:
        context_sections.append("No context documents were loaded for this session.")

    parts = [
        session_title,
        "",
        "### Your behavioral instructions for this session:",
        skill_block,
        "",
        "---",
        "",
        "### Context loaded for this session:",
        "\n\n".join(context_sections),
        "",
        "---",
        "",
        "### Your task:",
        prompt_block,
    ]

    if warnings:
        warning_lines = "\n\n".join(f"- {warning}" for warning in warnings)
        parts.extend([
            "",
            "---",
            "",
            "### Warnings",
            warning_lines,
        ])

    return "\n".join(parts)
