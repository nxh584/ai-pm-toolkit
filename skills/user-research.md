# Skill: User Research Processing

## What this skill does
This skill ensures the agent treats qualitative data with rigor. It prevents the agent from summarising away the nuance, abstracting user quotes into corporate jargon, or conflating the user's symptoms with the root cause.

## When to load this skill
Load this when pasting in raw interview transcripts, support tickets, sales call notes, or NPS feedback.

## Instructions for the agent
When this skill is referenced, you must adopt the following behaviours:
1. **Preserve the Voice**: Stay as close to the user's exact language as possible. Do not summarise a frustrated rant into "user experienced friction." Keep the sharp edges.
2. **Extract Jobs-to-be-Done (JTBD)**: Look past what the user *says* they want (the feature) and identify what they are actually trying to *accomplish* (the job).
3. **Surface Surprises**: Specifically look for data points that contradict our presumed `product-context.md` or common industry assumptions. Highlight the contradictions.
4. **Separate Observation from Interpretation**: Clearly demarcate what the user actually said (fact) from what you believe it implies for the product (hypothesis).

## Output format
When processing raw research, output in this structure:
- **Raw Observations**: (3-5 direct, unvarnished quotes)
- **The Core Pattern**: (What connects these quotes)
- **The True Job-to-be-Done**: (What they are hiring the product to do)
- **Contradictions & Surprises**: (What was unexpected)
- **Product Implications**: (What this means for the roadmap)

## Quality checks
- Did you use generic business jargon instead of user quotes? (If yes, you failed).
- Did you take a feature request at face value without asking the "why"? (If yes, you failed).
