# Quickstart: From 0 to 1 in 30 Minutes

This quickstart guide provides a 30-minute onboarding path to help you get the most out of the `ai-pm-toolkit`. By the end of this session, you'll have set up your environment, grounded your agent in reality, and prototyped a solution.

## The 30-Minute Path

> [!NOTE]
> **Step 0 (non-technical PMs only): Try it without any setup**
> If you're not comfortable with terminals or config files, skip to the 5-minute path in the main README first. Come back here when you're ready to go deeper. Everything in this quickstart works — it just assumes you're comfortable opening a terminal and copying files.

### Step 1: Set up your IDE (5 min)
Copy the appropriate IDE configuration file from the `ide-setup/` directory into the root of your working project. Then copy the `commands/` directory into the same project root so you can invoke the slash workflows during your session. These two steps ensure that your AI agent behaves as a thoughtful PM collaborator rather than just a code generator.
- **Cursor**: Copy `ide-setup/.cursorrules` and the `commands/` directory
- **Claude Code**: Copy `ide-setup/CLAUDE.md` and the `commands/` directory
- **Windsurf**: Copy `ide-setup/.windsurfrules` and the `commands/` directory

### Step 2: Establish Context (10 min)
AI agents hallucinate when they lack context. Grab the [`context-docs/user-context.md`](context-docs/user-context.md) template and fill it out for the primary user of your current project. Focus on reality over fiction — use direct quotes and specific behaviours instead of generic persona descriptions.

### Step 3: Run the Zero-to-Prototype Workflow (10 min)
Take a real problem you are currently facing and run it through the first half of the [`workflows/zero-to-prototype.md`](workflows/zero-to-prototype.md) playbook. Use the `problem-statement.md` template to shape the problem, feed the user context to your agent, and ask it for a first-pass build to test the core idea.

### Step 4: Reflect and Retrospect (5 min)
Before the session ends, open the [`templates/retrospective.md`](templates/retrospective.md) file. Spend 5 minutes reflecting on the agent's output. What did it get right? What did it misunderstand due to lacking context? Document one thing you'll change for your next session.

---

## What to Expect

Set honest expectations before diving in:
- **Agents are literal.** If your problem statement is fuzzy, the output will be misdirected.
- **The first output is rarely the final output.** Expect the first pass to be a functional sketch, not a shipping feature. Use the evaluation prompts to iterate.
- **Context is everything.** The quality of the agent's work is directly proportional to the quality of the context documents you provide. If the agent makes bad assumptions, it usually means your context doc was missing constraints.

## Where to Go Next

Based on what clicked for you during this quickstart:
- If you struggled to articulate the problem clearly, explore the **[Prompts for Problem Shaping](prompts/problem-shaping/)** and **[commands/clarify-ambiguity.md](commands/clarify-ambiguity.md)**.
- If the agent's output felt disconnected from user needs, dive deeper into the **[Context Docs](context-docs/)**.
- If you're ready to formalise your process, read through the **[Discovery to Spec Workflow](workflows/discovery-to-spec.md)**.
