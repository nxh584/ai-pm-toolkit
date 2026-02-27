# Skill: Prototyping

## What this skill does
This skill aligns the agent to build for learning rather than for scale. It shifts the focus from "writing robust, production-ready code" to "writing the simplest, fastest wedge that tests a core hypothesis."

## When to load this skill
Load this when you are moving from a shaped problem to a first-pass build, or when evaluating how to technically approach a testable idea.

## Instructions for the agent
When this skill is referenced, you must adopt the following behaviours:
1. **Ruthless Simplification**: Always favor the simplest version that tests the hypothesis. If a database isn't strictly necessary to test the flow, mock the data. 
2. **Explain Decisions**: Never just output a block of code. Include brief reasoning for why you chose a specific architecture or approach, focusing on speed-to-learning.
3. **Surface Assumptions**: Explicitly list the technical or behavioural assumptions your prototype relies on that might be wrong in the real world.
4. **Design for Learnability**: Prioritise making the core interaction clear over making edge cases resilient. The goal is to see if the user wants it, not if it survives a DDOS attack.
5. **Note Intentional Omissions**: Clearly flag what you deliberately chose *not* to build in this pass.

## Output format
When providing a prototype or approach, include:
- **The Core Wedge**: (What this prototype actually tests)
- **Key Decisions**: (Trade-offs made for speed)
- **Deliberate Omissions**: (What is explicitly missing)
- **Risky Assumptions**: (What might break validation)
- [The Code / Implementation]

## Quality checks
- Did you over-engineer the backend before testing the UI? (If yes, you failed).
- Did you aim for perfection over speed-to-learning? (If yes, you failed).
