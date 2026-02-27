# AI-Era Product Requirements Document (PRD)

*Instructions: This is a modern, lightweight PRD. It is not a 20-page waterfall document. It is designed to be fed into an AI agent to bound scope and define success before implementation begins.*

## 1. Problem
[What is physically broken, missing, or painful, and for whom? Detail the friction without describing the solution yet.]

## 2. Why Now
[Why does this matter enough to solve at this exact moment? What happens if we do nothing for 6 months?]

## 3. Users
[Link to a specific `user-context.md` file, or provide a brief summary of who we are building this for. Focus on behaviours, not demographics.]

## 4. Success Criteria
[How will we mathematically or observationally know this worked? E.g., "Time spent on the reconciliation page drops by 50%" or "30% of new signups complete the onboarding flow."]

## 5. Scope
- **In Scope:** [What we are absolutely accountable for shipping]
- **Explicitly Out of Scope:** [What we are deliberately choosing NOT to build, even if it seems related. E.g., "We are NOT building a way to edit past invoices."]

## 6. Open Questions
[Unresolved decisions that need answers before the agent writes code. E.g., "Do we need to support legacy PDF formats, or just CSV?"]

## 7. Constraints
[Hard technical, time, or resource limits. E.g., "Must be shipped by Friday," "Cannot change the database schema," "Must work on mobile Safari."]

---

## 8. Approach
*(Fill this out only after the above sections are complete and agreed upon)*
[What we are actually going to build. The high-level technical or UX direction. E.g., "A single 'Export' button on the dashboard that triggers an async worker to email the user a zipped CSV."]

## 9. Edge Cases to Handle
[The unhappy paths the agent needs to code for. E.g., "What happens if the async worker fails?", "What happens if the export is larger than 25MB?"]

## 10. How We'll Ship and Measure
[The rollout plan. E.g., "We'll deploy this behind a feature flag to 10 power users on Tuesday, monitor Error logs for 48 hours, then roll out to 100%."]
