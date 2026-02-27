# AI PM Skills

Skills are specialised instruction sets that force your AI agent to adopt a specific product management mindset. Standard AI agents default to being agreeable "yes-bots" that write code as fast as possible, even if it's the wrong code.

By loading a skill into your agent's context, you change its default behaviour. You tell it to act as a critical thought partner who cares about user value instead of just technical execution.

## How to Use Skills

You don't need to apply all skills at once. Load them situationally using a mention or reference command in your IDE's chat window.

For example:
- **When starting a new project:** `"@skills/problem-shaping.md Read this draft problem statement. Don't write any code yet. Tell me what's missing."`
- **When reviewing an interview:** `"@skills/user-research.md Help me extract insights from this transcript."`
- **When you're stuck on a prototype:** `"@skills/prototyping.md I want to test this idea without building a database. What's the simplest wedge?"`

## Skills vs. Commands — what's the difference?

Skills and commands solve different layers of work:
- Skills set session-wide behaviour (mindset, standards, evaluation lens).
- Commands execute a specific task within that session.

Typical pattern:
1. Load a skill at the start (for example `skills/problem-shaping.md`).
2. Invoke commands as you work (for example `/clarify-ambiguity`, `/problem-statement`, `/ship-or-kill`).

They are complementary, not alternatives.

## The Skills Available

- **[`problem-shaping.md`](problem-shaping.md)**: Forces the agent to define the boundaries of a problem before designing solutions.
- **[`context-curation.md`](context-curation.md)**: Makes the agent demand constraints and user context before building.
- **[`prototyping.md`](prototyping.md)**: Aligns the agent to build the simplest version that learns the most.
- **[`evaluation.md`](evaluation.md)**: Teaches the agent to judge output by user value, not just if it compiles.
- **[`user-research.md`](user-research.md)**: Helps the agent synthesise raw data without losing the voice of the user.
