# AI PM Toolkit — Cheat Sheet

A single-page reference for everything in the toolkit. Keep this open while you work.

---

## Slash Commands

Use these inside **Cursor**, **Claude Code**, or **Windsurf** after copying the [`commands/`](./commands/) directory into your project root.

| Command | What it does |
|---|---|
| `/build-session` | Assembles a full, context-rich opening message from your skills, context docs, and a chosen prompt |
| `/clarify-ambiguity` | Runs a structured Q&A to surface hidden assumptions and constraints in your problem |
| `/problem-statement` | Guides you through writing a clear, specific problem statement |
| `/first-pass-build` | Generates a first-pass prototype or plan based on the current context and problem |
| `/review-output` | Structured evaluation of the agent's last output — what's good, what's off, what to change |
| `/ship-or-kill` | Runs a structured decision framework: is this worth continuing, and why? |

---

## Prompts by Stage

Use these by copying the file contents into your AI conversation, or via `npx ai-pm-toolkit copy <path>`.

### Problem Shaping
| File | When to use it |
|---|---|
| [`prompts/problem-shaping/clarify-ambiguity.md`](./prompts/problem-shaping/clarify-ambiguity.md) | Your problem description feels vague or you're not sure where to start |
| [`prompts/problem-shaping/reframe-problem.md`](./prompts/problem-shaping/reframe-problem.md) | You want to challenge whether you're solving the right problem |
| [`prompts/problem-shaping/scope-reduction.md`](./prompts/problem-shaping/scope-reduction.md) | The problem is too broad and you need to focus it |

### Research
| File | When to use it |
|---|---|
| [`prompts/research/synthesise-notes.md`](./prompts/research/synthesise-notes.md) | You have raw research notes and want themes and insights pulled out |
| [`prompts/research/interview-debrief.md`](./prompts/research/interview-debrief.md) | You've just done a user interview and want to extract the key points |
| [`prompts/research/assumption-mapping.md`](./prompts/research/assumption-mapping.md) | You want to map out what you're assuming vs. what you know |

### Prototyping
| File | When to use it |
|---|---|
| [`prompts/prototyping/first-pass.md`](./prompts/prototyping/first-pass.md) | Ready to generate a first prototype or plan |
| [`prompts/prototyping/iterate.md`](./prompts/prototyping/iterate.md) | You have a first pass and want to improve a specific part of it |
| [`prompts/prototyping/edge-cases.md`](./prompts/prototyping/edge-cases.md) | You want the agent to stress-test your solution against edge cases |

### Evaluation
| File | When to use it |
|---|---|
| [`prompts/evaluation/review-output.md`](./prompts/evaluation/review-output.md) | Structured critique of agent output before deciding next steps |
| [`prompts/evaluation/ship-or-kill.md`](./prompts/evaluation/ship-or-kill.md) | Decision framework for whether a feature or idea should continue |

---

## Templates

Copy these into a doc or paste them into your AI conversation to structure your PM artefacts.

| Template | What it's for |
|---|---|
| [`templates/problem-statement.md`](./templates/problem-statement.md) | Clear, structured definition of what you're solving and why |
| [`templates/prd.md`](./templates/prd.md) | Full Product Requirements Document |
| [`templates/spec.md`](./templates/spec.md) | Lightweight technical or feature spec |
| [`templates/discovery-brief.md`](./templates/discovery-brief.md) | Framing document before starting a discovery sprint |
| [`templates/user-research-synthesis.md`](./templates/user-research-synthesis.md) | Organising what you learned from user research |
| [`templates/launch-checklist.md`](./templates/launch-checklist.md) | Pre-launch readiness checklist |
| [`templates/retrospective.md`](./templates/retrospective.md) | Session or sprint retrospective |

---

## Context Docs

Fill these out and paste them at the start of any agent session. Good context = dramatically better output.

| File | What it captures |
|---|---|
| [`context-docs/user-context.md`](./context-docs/user-context.md) | Who your user is, what they do, what they struggle with |
| [`context-docs/project-context.md`](./context-docs/project-context.md) | What the product is, its current state, and key constraints |
| [`context-docs/team-context.md`](./context-docs/team-context.md) | Team setup, working norms, and relevant technical constraints |

> [!TIP]
> You don't need to fill out every field. Three or four specific, real observations are worth more than ten vague ones.

---

## Skills

Skills are instruction sets that shape how your agent behaves. Load one by pasting its contents into your conversation at the start of a session.

| Skill | Agent behaviour it enables |
|---|---|
| [`skills/problem-shaping.md`](./skills/problem-shaping.md) | Agent asks probing questions to clarify your problem before acting |
| [`skills/context-curation.md`](./skills/context-curation.md) | Agent helps you identify and fill gaps in your context documents |
| [`skills/prototyping.md`](./skills/prototyping.md) | Agent builds iteratively and flags assumptions as it goes |
| [`skills/evaluation.md`](./skills/evaluation.md) | Agent critiques output against the original problem and user needs |
| [`skills/user-research.md`](./skills/user-research.md) | Agent helps synthesise research and extract actionable insights |

---

## Workflows

End-to-end playbooks for common PM tasks. Follow the steps in order or use them as a reference.

| Workflow | When to use it |
|---|---|
| [`workflows/zero-to-prototype.md`](./workflows/zero-to-prototype.md) | Starting from a problem with nothing built yet |
| [`workflows/discovery-to-spec.md`](./workflows/discovery-to-spec.md) | Turning early-stage discovery into a spec ready for development |
| [`workflows/ship-or-kill.md`](./workflows/ship-or-kill.md) | Deciding whether to continue shipping a feature or cut it |
| [`workflows/weekly-pm-routine.md`](./workflows/weekly-pm-routine.md) | A regular weekly rhythm for working with AI tools |

---

## IDE Setup

Copy these into the root of your project before starting a session.

| IDE | File to copy |
|---|---|
| Cursor | [`ide-setup/.cursorrules`](./ide-setup/.cursorrules) |
| Claude Code | [`ide-setup/CLAUDE.md`](./ide-setup/CLAUDE.md) |
| Windsurf | [`ide-setup/.windsurfrules`](./ide-setup/.windsurfrules) |

---

## CLI Quick Reference

If you have Node.js installed, you can use `npx` to explore and copy toolkit content without cloning the repo.

```bash
# See what's available
npx ai-pm-toolkit list prompts
npx ai-pm-toolkit list templates
npx ai-pm-toolkit list skills

# Search across all content
npx ai-pm-toolkit search "problem"

# Copy a file's contents to your clipboard
npx ai-pm-toolkit copy prompts/problem-shaping/clarify-ambiguity
npx ai-pm-toolkit copy skills/problem-shaping
npx ai-pm-toolkit copy templates/prd
```

---

## Quick Recipes

Common tasks and the fastest way to do them.

### "I need to define a problem clearly"
1. Paste [`skills/problem-shaping.md`](./skills/problem-shaping.md) into your conversation  
2. Say: "Help me define this problem: [your description]"  
3. Let the agent ask questions — answer them honestly

### "I need to write a PRD fast"
1. Paste your completed [`context-docs/project-context.md`](./context-docs/project-context.md) and [`templates/prd.md`](./templates/prd.md)  
2. Say: "Use the context to help me fill out this PRD. Ask me for anything that's missing."

### "I have research notes and need to make sense of them"
1. Paste your raw notes  
2. Paste [`prompts/research/synthesise-notes.md`](./prompts/research/synthesise-notes.md)  
3. Say: "Apply this to my notes above."

### "The agent's output isn't good enough — what do I improve?"
1. Run [`/review-output`](./commands/review-output.md) or paste [`prompts/evaluation/review-output.md`](./prompts/evaluation/review-output.md)  
2. The agent will identify the gaps — usually: missing context or scope that was too broad

### "I want to start a really well-grounded session from scratch"
1. Copy [`ide-setup/`](./ide-setup/) config for your IDE into your project  
2. Fill in [`context-docs/user-context.md`](./context-docs/user-context.md) and [`context-docs/project-context.md`](./context-docs/project-context.md)  
3. Run `/build-session` — it assembles everything into a single opening message

---

## Core Principles (the short version)

- **Precise problems get better output.** Fuzzy problem statements produce confident but wrong answers.
- **Context is the main lever.** If the agent makes bad assumptions, your context doc was probably missing something.
- **The first output is a starting point.** Evaluate it, note what's off, and iterate — don't just accept or reject.
- **Narrow scope on purpose.** One clear problem per session beats trying to solve three things at once.
- **Skills shape behaviour.** Load a skill at the start of a session to change how the agent works, not just what it produces.
