# Contributing to AI PM Toolkit

Thank you for considering a contribution. This toolkit exists because PMs share what works. The more real, tested material we collect, the more useful it becomes for everyone.

---

## What We Accept Contributions For

**In scope:**
- `prompts/` — New prompts for any of the four categories
- `skills/` — New skill instruction sets for AI agents
- `workflows/` — New step-by-step PM playbooks

**Maintained by the core team:**
- `templates/` — PRDs, specs, briefs
- `examples/` — Fully worked scenarios
- `context-docs/` — Core context document templates
- `ide-setup/` — IDE configurations

This is not gatekeeping — it's a quality decision. Templates and examples need to be internally consistent and cross-referenced with the rest of the toolkit. Keeping community contributions focused on prompts, skills, and workflows means every merged contribution can meet a high quality bar. We would rather have 20 excellent prompts than 200 mediocre ones.

---

## Contribution Principles

These reflect the toolkit's core philosophy. If your contribution doesn't meet these, it won't be merged — but it will get feedback.

1. **Real over theoretical.** Every contribution must reflect something you have actually used with a real AI agent. Not something that sounds useful in the abstract.
2. **Specific over general.** A prompt "for synthesis" is too vague. A prompt "for extracting Jobs-to-be-Done from a raw Gong call transcript" is ready to use. If your contribution could apply to anything, it applies to nothing.
3. **No fluff.** Write for a smart, busy PM. If a sentence doesn't add value, cut it. Generic productivity advice belongs on a blog, not here.
4. **Show your context.** Include a brief note in your PR on when you used it and what the agent produced. If you've never run it with a real agent, it's not ready to submit.

---

## How to Contribute a Prompt

1. **Check for duplication.** Read through the existing [`prompts/`](prompts/) directory. If something close already exists, open a discussion rather than creating a near-duplicate.
2. **Propose before building** (for significant additions). Use the [`new-prompt` issue template](.github/issue_templates/new-prompt.yml) to share your idea and get early feedback before you spend time writing the full file.
3. **Fork and branch.** Create a branch named `prompt/your-prompt-name` (e.g., `prompt/stakeholder-alignment`).
4. **Follow the format exactly.** Every prompt file must use this structure:

```markdown
# [Prompt Name]

## When to use this
[1-2 sentences on the right moment to reach for this prompt]

## What to feed it
[What context/input the agent needs to do this well]

## The Prompt
[The actual prompt — written to be pasted directly into an agent session.]

## What to do with the output
[How to evaluate and iterate on the result]

## Common failure modes
[What goes wrong and how to fix it]
```

5. **Test it.** Paste the prompt into a real agent session (Cursor, Claude Code, or Windsurf). Include a brief note in your PR about what it produced — even a one-sentence summary is fine.
6. **Submit your PR.** Use the PR template. Fill it in properly.
7. **Expect review within 7 days.** We will leave feedback or merge within that window.

---

## How to Contribute a Skill

Same process as prompts. Use branch naming: `skill/your-skill-name`.

Every skill file must use this structure:

```markdown
# Skill: [Skill Name]

## What this skill does
[What the agent will do differently when this skill is loaded]

## When to load this skill
[The right moment / task type]

## Instructions for the agent
[Detailed behavioural instructions]

## Output format
[What the output of this skill should look like]

## Quality checks
[How to evaluate whether the skill is being applied well]
```

---

## How to Contribute a Workflow

Same process. Use branch naming: `workflow/your-workflow-name`.

**Additional requirement:** Workflows must explicitly reference at least two existing toolkit components — prompts, skills, or templates. A workflow that doesn't use the rest of the toolkit is just a standalone guide, not a workflow.

Every workflow file must use this structure:

```markdown
# [Workflow Name]

## What this is
[What you'll accomplish and in how long]

## When to use it
[The trigger — what situation calls for this workflow]

## What you need before starting
[Prerequisites: context docs, raw material, etc.]

## The workflow
[Numbered steps with estimated time per step]

## What good output looks like
[How to know you did it right]

## Common failure modes
[What goes wrong and how to recover]
```

---

## Review Criteria

When reviewing a PR, we check:

- Does it **follow the correct file format** for its contribution type?
- Is it **specific enough to use immediately**, or does it require imagination to apply?
- Has the contributor **tested it with a real agent session** and shared a brief output summary?
- Does it **add something not already covered** by existing content?
- Is the **writing direct and jargon-free**? No productivity-blog language.

If a PR fails on any of these, we'll leave specific, actionable feedback. We want to help people get contributions merged — we're not looking for reasons to reject.

---

## Getting Help

- **Before submitting:** Open a [GitHub Discussion](../../discussions) to share your idea and get early feedback.
- **Before a large PR:** Open a proposal issue using the appropriate template. It takes 5 minutes and avoids wasted effort if there's a scope or format issue.
- **If you're stuck:** Comment on any open issue — we're happy to help.
