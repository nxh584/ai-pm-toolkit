# Contributing to AI PM Toolkit

Thanks for contributing. This project is built by PMs and builders sharing workflows they actually use, and the goal is practical quality over volume.

## What we accept contributions for

We currently accept contributions for:
- `prompts/`
- `skills/`
- `workflows/`

Templates and examples are maintained by the core team.

Why this scope exists:
- It keeps review focused and fast.
- It protects consistency in foundational docs used across the toolkit.
- It keeps the quality bar high. Better to have 20 excellent prompts than 200 mediocre ones.

This is a quality decision, not a gatekeeping decision. If you have a strong template or example idea, open a Discussion first.

## Contribution principles

- Real over theoretical: submit what you have actually used, not what sounds good in theory.
- Specific over general: target a concrete PM moment in a real workflow.
- No fluff: write for a smart, busy PM. If a sentence does not add value, cut it.
- Show your context: include where you used it and what it produced.

## How to contribute a prompt

1. Check existing prompts to avoid duplication.
2. For significant additions, open a proposal using the `New Prompt Proposal` issue template before building.
3. Fork the repo and create a branch named `prompt/your-prompt-name`.
4. Follow the prompt format exactly (see [File format requirements](#file-format-requirements)).
5. Test it in a real agent session. Include a short note in your PR about what it produced.
6. Submit a PR using the PR template.
7. Expect review within 7 days.

## How to contribute a skill

1. Check existing skills to avoid overlap.
2. For significant additions, open a proposal using the `New Skill Proposal` issue template before building.
3. Fork the repo and create a branch named `skill/your-skill-name`.
4. Follow the skill format exactly (see [File format requirements](#file-format-requirements)).
5. Test it in a real agent session and include what changed in agent behavior.
6. Submit a PR using the PR template.
7. Expect review within 7 days.

## How to contribute a workflow

1. Check existing workflows to avoid duplication.
2. For significant additions, open a proposal using the `New Workflow Proposal` issue template before building.
3. Fork the repo and create a branch named `workflow/your-workflow-name`.
4. Follow the workflow format exactly (see [File format requirements](#file-format-requirements)).
5. Ensure the workflow references at least two existing toolkit components (`prompts/`, `skills/`, or `templates/`).
6. Test it end-to-end in a real working session and include what you shipped or decided.
7. Submit a PR using the PR template.
8. Expect review within 7 days.

## File format requirements

Use these structures exactly so contributions are easy to review and consistent to use.

### Prompt file format

This is the canonical format from `prompts/README.md`:

1. `## When to use this`
2. `## What to feed it`
3. `## The Prompt`
4. `## What to do with the output`
5. `## Common failure modes`

Also include a clear H1 title at the top:
- `# <Prompt Name>`

### Skill file format

Required headings:

1. `## What this skill does`
2. `## When to load this skill`
3. `## Instructions for the agent`
4. `## Output format`
5. `## Quality checks`

Also include a clear H1 title at the top:
- `# Skill: <Skill Name>`

### Workflow file format

Required headings:

1. `## What this is`
2. `## When to use it`
3. `## What you need before starting`
4. Step sections (`## Step 1: ...`, `## Step 2: ...`, etc.)
5. `## What good output looks like`
6. `## Common failure modes`

Also include a clear H1 title at the top:
- `# <Workflow Name> Workflow`

## Review criteria

Reviewers check:
- Does it follow the format exactly?
- Is it specific enough to use immediately?
- Has it been tested in a real agent session?
- Does it add something not already covered?
- Is the writing direct and jargon-free?

## Getting help

Use GitHub Discussions for questions before submitting.

If you are planning a large PR, opening an issue first is always appreciated.
