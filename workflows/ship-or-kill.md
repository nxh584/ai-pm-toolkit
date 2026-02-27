# Ship or Kill Workflow

## What this is
A rigorous, unemotional process for deciding what to do with a prototype or beta feature. With AI, it is so easy to build software that we often forget we have to maintain it. This workflow stops you from shipping technical debt into production out of momentum. 

## When to use it
When an AI agent or engineer has completed a build/prototype, and you are feeling the pressure to simply hit "merge" and move on. Run this before merging.

## What you need before starting
- The test results (technical monitoring, usability testing, or personal dogfooding).
- The original `project-context.md` containing the success metrics.
- The `prompts/evaluation/ship-or-kill.md` tool.

---

## Step 1: Force a Rigid Evaluation (15 min)
*Bypass your own bias.*
1. Do not ask yourself "Is it good enough?"
2. Open your IDE or chat window. Paste the test results or prototype code, invoke the `@skills/evaluation.md` skill, and run the **[`prompts/evaluation/ship-or-kill.md`](../prompts/evaluation/ship-or-kill.md)** prompt.
3. Force the agent to categorically choose: Ship, Iterate, or Kill based *only* on the definition of success in your context docs.

## Step 2: Handle the "Iterate" Trap (10 min)
*If the agent/team recommends "Iterate," be intensely skeptical.*
1. If the iteration is to fix a cosmetic issue or a low-frequency edge case, override the decision to **Ship**. We don't iterate for perfection.
2. If the iteration is to fix a critical failure in the core user flow, keep the "Iterate" status but put a strict timebox on it (e.g., "Agent, you have one pass to fix the core flow. If it takes more than 1 hour to fix, we Kill the project").
3. Do not remain stuck in Iterate indefinitely. If it takes three tries to fix the UX, the hypothesis is wrong. Move to Kill.

## Step 3: Handle the "KILL" Decision (20 min)
*Killing a feature is a success if you document it.*
1. If the project missed its success criteria or introduced too much complexity, accept the Kill. Do not try to salvage it.
2. Open **[`context-docs/product-context.md`](../context-docs/product-context.md)**. Go to the "Institutional Memory / What we've tried" section.
3. Write two sentences explaining *why* you killed this (e.g., "Aug 2024: Prototyped full-text search on feedback. Killed it. It was too slow, and users only ever searched via exact tags anyway. Do not build full-text search without an explicit, validated need.")
4. Delete the branch. Delete the code. Close the tickets.

## Step 4: Handle the "SHIP" Decision (30 min)
*Ship responsibly.*
1. Open the **[`templates/launch-checklist.md`](../templates/launch-checklist.md)** document.
2. Focus specifically on the Rollback Plan and Instrumentation sections. Ensure the metrics defined in step 1 are actually wired up to Mixpanel/PostHog.
3. Write your release notes directly from the `problem-statement.md` file (Start with: "Previously you struggled with [Pain]. Now you can [Solution].")
4. Merge and deploy.

---

## What good output looks like
A binary decision made in under an hour, with zero lingering "maybe we'll fix it next week" branches clogging up your repository. 

## Common failure modes
- **Sunk Cost Fallacy**: You spent 4 hours prompting an agent to build a dashboard. It's beautiful, but it doesn't solve the core problem. You ship it anyway because it feels like a waste to delete it. *Correction: Remember that the maintenance cost over 2 years will be 50x higher than the 4 hours you spent today.*
