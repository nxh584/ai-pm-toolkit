# Discovery to Spec Workflow

## What this is
A playbook for bridging the gap between raw qualitative research (talking to users) and actionable development specifications (handing off to an agent or engineering team).

## When to use it
When you have collected a batch of user interviews, support tickets, or sales calls, but the engineering team (or AI agent) needs clear boundaries on what exactly to build next sprint.

## What you need before starting
- A transcript tool output, Gong call notes, or Zendesk export.
- A blank text editor.

---

## Step 1: Synthesise Raw Research (30 min)
*Don't trust your memory. Process the raw data.*
1. Take the transcript of your most recent call or batch of tickets.
2. Run it through the **[`prompts/research/interview-synthesis.md`](../prompts/research/interview-synthesis.md)** prompt. Focus heavily on not sanitising the quotes. Focus heavily on extracting the Jobs-to-be-Done.
3. Save this output using the **[`templates/user-research-synthesis.md`](../templates/user-research-synthesis.md)** format. Do this for 2-3 users if you can.

## Step 2: Extract the Core Job (15 min)
1. Review the synthesised documents. Use the **[`prompts/research/jtbd-extraction.md`](../prompts/research/jtbd-extraction.md)** prompt if you are having trouble separating emotional jobs from functional jobs.
2. Identify the single highest-leverage Job-to-be-Done that spans your user group (e.g., "Help me feel less anxious about missing a high-priority SLA").
3. Discard the rest for now. 

## Step 3: Define the Problem (20 min)
*Translate the job into a structured problem.*
1. Open the **[`templates/problem-statement.md`](../templates/problem-statement.md)** file.
2. Based *only* on the Job-to-be-Done you selected, write out the situation, pain, and impact.
3. Write the "What we're explicitly NOT asking for" section. This is vital. Guard against the obvious, complex solutions. (e.g., "We are NOT asking for AI sentiment analysis of tickets. We just want a massive red bell icon when SLA dips below 2 hours").

## Step 4: Write the Lightweight Spec (25 min)
1. Open the **[`templates/spec.md`](../templates/spec.md)** document.
2. Determine the core "Input / Output." What triggers the feature? What is the resulting state?
3. Turn the constraints from step 3 into bulleted Acceptance Criteria. This needs to be testable by an agent (e.g., "Must fire webhook when SLA drops below 120 minutes").
4. Brainstorm 2-3 edge cases. (e.g., "What if the ticket priority is escalated mid-flight?"). Paste them into section 5.

## Step 5: Final Sanity Check (5 min)
*Can an agent read this?*
Take your completed `spec.md` and read it from top to bottom. If any line requires insider context that isn't documented in your `product-context.md`, delete it or clarify it.

---

## What good output looks like
A 1-page `spec.md` document that is directly traceable back to a raw user quote, completely devoid of prescriptive architecture, but thick with testable acceptance criteria.

## Common failure modes
- **Over-Scoping**: You tried to solve all 4 distinct Jobs-to-be-Done identified in the research in a single spec. Force yourself to throw away three and write a spec for only the most painful one.
- **Solution Bias**: The spec tells the agent "Add a Redis cache layer" instead of telling the agent "The response time must be under 50ms."
