# Context Documents

The quality of an AI agent's output is directly proportional to the quality of the context you provide. Agents hallucinate, invent fake requirements, and propose naive solutions when they are not grounded in reality. Context documents are the antidote. 

Instead of writing a massive prompt every time you start a session, maintain these living documents and attach them (or reference them) when you need an agent to act on a problem.

## Types of Context Docs

1. **[`user-context.md`](user-context.md)**: Describes real users based on actual data, quotes, and behaviours. *Use this when prompting an agent to design a solution, draft copy, or evaluate a prototype's usability.*
2. **[`product-context.md`](product-context.md)**: Captures your product's core value proposition, known constraints, and institutional memory (what you've already tried). *Use this when prompting an agent to explore new features to ensure it doesn't suggest architectures or ideas you've already discarded.*
3. **[`project-context.md`](project-context.md)**: Your working memory for a specific, bounded initiative. It defines scope, success criteria, and what's deliberately left unbuilt. *Use this as the primary attachment for day-to-day coding and prototyping tasks.*

## Common Mistakes

- **Being too vague**: Stating "the user is a busy professional" provides zero constraints. Say: "The user is a Solo PM who has 4 hours a week for customer discovery."
- **Using persona language**: Fictional personas (like "Marketing Mary") lead to fictional features. Use real quotes and aggregated behaviours from real people instead.
- **Skipping the "what's been tried" section**: If you don't tell the agent that you tried a dashboard last year and users hated it, the agent *will* suggest a dashboard.

## The Difference Context Makes

**Bad Prompt (No Context)**
> "Build a feature that helps users sort their feedback."
> *Output*: A complex, multi-view dashboard with filtering, AI categorisation tags, and a 12-table relational database schema that takes 3 weeks to build.

**Good Prompt (Context-Informed)**
> "I need to build a way for users to sort feedback. Read `@user-context.md` and `@product-context.md` first. Propose a first-pass prototype."
> *Output*: "I see the user only checks feedback once a week for 30 minutes, and our primary constraint is having no dedicated backend engineers. Instead of a complex dashboard, let's build a simple cron job that emails them a plain-text digest of the top 3 themes every Friday morning. Setting this up takes 2 hours."
