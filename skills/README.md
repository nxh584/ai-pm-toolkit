# Skills

Skills are instruction sets that change how your AI agent behaves, not just what it produces.

By default, most AI agents are optimised to be agreeable and to generate output quickly. That's fine for many tasks, but it's not great for product work. A fast, agreeable agent will confidently write code for the wrong problem, skip constraints it wasn't told about, and produce output that looks good until you test it against a real user.

Loading a skill at the start of a session changes this. It tells the agent to behave as a specific kind of thought partner: one that asks better questions, surfaces risks, and evaluates output against what actually matters.

---

## How to use a skill

You don't need to load all skills at once. Use them situationally and match the skill to what you're trying to do in this session.

The simplest approach: open a skill file, copy its contents, and paste it into your agent conversation at the start of a session.

If you're using an IDE that supports file references (Cursor, Claude Code), you can reference the file directly:

```
@skills/problem-shaping.md: Read this draft problem statement. Don't write any code yet. Tell me what's missing.
```

```
@skills/user-research.md: Help me extract insights from this interview transcript.
```

```
@skills/prototyping.md: I want to test this idea without building a database. What's the simplest version that would tell us if this is worth pursuing?
```

---

## Skills vs. Commands

These two things work at different levels and are meant to be used together:

- **Skills** set the agent's overall behaviour for the session: how it thinks, what it prioritises, and what it pushes back on.
- **Commands** (in [`commands/`](../commands/)) execute specific tasks within that session: a structured Q&A, a first-pass build, an output review.

The typical pattern is: load a skill at the start, then invoke commands as you work through the session.

---

## Available skills

| Skill | What it does |
|---|---|
| [`problem-shaping.md`](problem-shaping.md) | Agent clarifies the problem before proposing any solution, and pushes back on vague scoping |
| [`context-curation.md`](context-curation.md) | Agent surfaces missing constraints and user context before acting |
| [`prototyping.md`](prototyping.md) | Agent builds the simplest version that tests the core assumption, not the full solution |
| [`evaluation.md`](evaluation.md) | Agent critiques output against user value and the original problem, not just technical correctness |
| [`user-research.md`](user-research.md) | Agent synthesises raw research data without losing the actual voice and behaviour of users |
