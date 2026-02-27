# Context Docs

Context documents are the single most impactful thing you can do to improve your agent's output. They give the agent the background it needs to stop guessing and start being useful.

Agents that lack context fill in gaps with plausible-sounding assumptions, and those assumptions are often wrong. Context documents are the fix. They're living documents you maintain and attach at the start of relevant sessions. Once written, you reuse them across sessions without starting from scratch each time.

---

## Getting started (no setup required)

The fastest way to get value from context docs:

1. Open [`user-context.md`](user-context.md).
2. Fill it in using real language: specific observations, direct quotes, things you've seen users actually do.
3. Paste it at the start of your next agent conversation before you describe your problem.

That single step will improve your agent's output more than anything else in this toolkit. The MCP server, CLI, and commands directory all exist to make this faster, but the value is in the context itself, not the delivery mechanism.

---

## The three context documents

**[`user-context.md`](user-context.md)**
Who your users actually are, based on real observations and not personas. Include specific behaviours, direct quotes, and things they struggle with. Use this whenever asking an agent to design a solution, write copy, or evaluate whether a prototype makes sense for the people who'll use it.

**[`product-context.md`](product-context.md)**
Your product's current state, core value proposition, key constraints, and institutional memory. Especially what you've already tried and discarded. Use this when exploring new features, so the agent doesn't suggest something you already know doesn't work.

**[`project-context.md`](project-context.md)**
Working memory for a specific initiative. Defines scope, success criteria, and what's intentionally out of scope for this effort. Attach this as your primary document for day-to-day coding and prototyping tasks.

---

## What good context looks like

**Too vague (not useful):**
> "The user is a busy professional who values efficiency."

This gives the agent zero real constraints. It will guess what "busy" and "efficiency" mean, and it will guess wrong.

**Specific and grounded (useful):**
> "The user is a solo PM with roughly 4 hours a week for customer discovery. She checks Slack on mobile before opening her laptop. She hasn't used a dedicated research tool. Everything lives in Notion or email threads."

This gives the agent something to reason against.

---

## Common mistakes

- **Persona language**: fictional archetypes like "Marketing Mary" produce fictional features. Use aggregated observations from real people instead.
- **Missing constraints**: if your product has no backend engineers, or a hard mobile-first requirement, or a 2-week deadline, say so. The agent can't respect constraints it doesn't know about.
- **Skipping "what's been tried"**: if you tried a dashboard last year and users hated it, include that. Otherwise the agent will suggest a dashboard.

---

## The difference context makes

**Without context:**
> "Build a way for users to sort their feedback."

Output: a multi-view dashboard with AI categorisation tags, custom filters, and a 12-table database schema. A 3-week build.

**With context:**
> "Build a way for users to sort their feedback. Read `@user-context.md` and `@product-context.md` first."

Output: "I can see the user only checks feedback once a week for 30 minutes and there are no dedicated backend engineers. Instead of a dashboard, let's build a cron job that emails a plain-text digest of the top 3 themes every Friday. Setup time: about 2 hours."

Same request. Completely different result, and a much better one.
