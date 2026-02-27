# Quickstart Guide

A focused 30-minute session to get from zero to a working first prototype — with your AI agent doing most of the heavy lifting.

> [!NOTE]
> **Not comfortable with terminals yet?**
> Skip ahead to Step 2. You don't need a terminal to get value from the toolkit. Come back to Step 1 when you're ready to go deeper.

---

## Before you begin

You need one of the following:
- [Claude](https://claude.ai) — free tier is fine, Claude 3.5 Sonnet or above recommended
- [Cursor](https://cursor.com) — free tier works for this session
- [Windsurf](https://codeium.com/windsurf) — free tier works for this session

You don't need to clone this repo. The session will work by copying individual files from GitHub.

---

## Step 1 — Set up your AI environment (5 min)

*Skip this step if you're using Claude via the web browser — it's not needed there.*

If you're using **Cursor**, **Claude Code**, or **Windsurf**, setting up IDE rules takes 2 minutes and makes your agent significantly more useful for PM work. Without this, you'll get a generic coding assistant. With it, you'll get an agent that asks clarifying questions, respects scope, and calls out risks.

**What to do:**

1. Open the [`ide-setup/`](./ide-setup/) directory in this repo.
2. Copy the file that matches your IDE into the **root folder of whatever project you're working in**:
   - **Cursor** → `.cursorrules`
   - **Claude Code** → `CLAUDE.md`
   - **Windsurf** → `.windsurfrules`
3. Also copy the entire [`commands/`](./commands/) directory into the same project root. This gives you slash commands you can invoke during your session.

That's it. Next time you open a session in that project, your agent will pick up the rules automatically.

> [!TIP]
> If you're not working in a specific project yet, just create a temporary folder (e.g. `my-pm-session/`) and copy both things there. The agent will still pick them up.

---

## Step 2 — Ground your agent in context (10 min)

This is the most important step. AI agents hallucinate when they don't have context — they fill in blanks with plausible-sounding guesses that are often wrong. The fix is to give them the right background upfront.

**What to do:**

1. Find the user context template at [`context-docs/user-context.md`](./context-docs/user-context.md). Copy its contents.
2. Fill it out for the **primary user** of the thing you're building or improving today.

**How to fill it out well (this matters):**
- Use real, specific observations — not idealisations. "She checks Slack on her phone first thing before opening her laptop" is useful. "She is a busy professional who values efficiency" is not.
- Include direct quotes where you have them.
- Note what the user *doesn't* do or doesn't know — constraints are as important as goals.
- You only need 3–5 solid observations to make a meaningful difference.

3. Paste the completed context doc at the start of your agent conversation with this message:

   > "Here's the context for my current project. Please keep this in mind for everything we discuss today. Ask me if anything is unclear."

---

## Step 3 — Shape the problem (10 min)

Before asking the agent to build anything, you need to be precise about what problem you're actually solving. This step will feel slow the first time. It gets faster — and it prevents you from spending an hour generating output for the wrong problem.

**What to do:**

1. Open [`templates/problem-statement.md`](./templates/problem-statement.md) and copy it into your conversation.
2. Tell your agent:

   > "Help me fill out this problem statement for [describe your problem in a sentence]. Ask me questions to help me be more specific."

3. Let the agent drive. Answer its questions. Push back if something feels off. The goal is a problem statement specific enough that the agent could act on it without asking you more questions.

**Alternatively**, use the clarify-ambiguity slash command if you set up commands in Step 1:

```
/clarify-ambiguity
```

This runs a structured Q&A session to surface hidden assumptions and constraints in your problem.

> [!TIP]
> If your problem statement has more than one core problem in it, split it. Agents perform best when the scope is tight.

---

## Step 4 — Generate a first pass (5 min)

You now have a grounded agent (context) and a specific problem (problem statement). This is the moment to generate your first output.

**What to do:**

1. Tell your agent:

   > "Based on the context and problem statement we've discussed, give me a first-pass [prototype / spec / brief / plan]. Keep it focused on the core problem only — don't over-engineer this first version."

   Or, if you set up commands in Step 1:

   ```
   /first-pass-build
   ```

2. Review the output. Don't just accept it. Ask yourself:
   - Does this address the actual problem, or a simplified version of it?
   - What assumptions is the agent making that I haven't confirmed?
   - What's missing?

3. Use [`/review-output`](./commands/review-output.md) or the prompts in [`prompts/evaluation/`](./prompts/evaluation/) to structure your evaluation.

---

## Step 5 — Reflect before you close (5 min)

This step is easy to skip and worth doing. Five minutes of reflection now will make your next session noticeably better.

**What to do:**

1. Open [`templates/retrospective.md`](./templates/retrospective.md).
2. Answer the key questions honestly — no need to write essays:
   - Where did the agent do well?
   - Where did it go wrong, and why? (Almost always: missing context or a fuzzy problem statement.)
   - What's one thing you'll change about how you set up your next session?

---

## What to expect

A few things worth knowing going in:

- **The first output is a sketch, not a final answer.** That's by design. Use it to surface assumptions and identify what needs sharpening — not to ship immediately.
- **Agents are very literal.** If your problem statement is vague, the output will be confidently wrong rather than usefully approximate. The more precise your input, the closer the output.
- **Context is the main lever.** Most cases where an agent gives bad output come down to missing constraints — things you knew but didn't tell it. Good context docs fix this.

---

## Where to go next

Based on what you found in this session:

| If you struggled with… | Go here |
|---|---|
| Articulating the problem clearly | [`prompts/problem-shaping/`](./prompts/problem-shaping/) and [`/clarify-ambiguity`](./commands/clarify-ambiguity.md) |
| Output that felt disconnected from real users | [`context-docs/`](./context-docs/) — add more specificity to your user context |
| Turning a prototype into a proper spec | [`workflows/discovery-to-spec.md`](./workflows/discovery-to-spec.md) |
| Deciding whether to continue or cut a feature | [`workflows/ship-or-kill.md`](./workflows/ship-or-kill.md) |
| Keeping up a regular AI-native PM practice | [`workflows/weekly-pm-routine.md`](./workflows/weekly-pm-routine.md) |

---

## If you want to go further in this session

The [CHEAT_SHEET.md](./CHEAT_SHEET.md) has every command, prompt, template, and workflow on one page — useful to keep open while you work.
