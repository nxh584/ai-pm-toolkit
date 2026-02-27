# Extract Constraints

## When to use this
Use this after a stakeholder meeting or after drafting a PRD, when you need to separate the true "must-have" constraints from the "nice-to-have" preferences before handing the spec to an agent or engineer.

## What to feed it
- A draft of the PRD, project brief, or raw notes from a planning meeting.
- `product-context.md`.

## The Prompt

```markdown
Review the following project notes/draft:
[INSERT NOTES/DRAFT HERE]

Your job is to extract and categorise the constraints to prevent scope creep during implementation. 

Separate your extraction into two lists:
1. **Hard Constraints**: Things that will cause the project to fail technically, legally, or fundamentally if broken. (e.g., must be HIPAA compliant, must use Postgres).
2. **Soft Constraints**: Preferences, stylistic choices, or "nice to haves" that we can flex if they jeopardise the hard constraints.

If you believe a constraint is missing based on how similar features are built, explicitly call it out as an "Unknown Constraint."
```

## What to do with the output
Take the Hard Constraints list and paste it directly into the `project-context.md` file. Ignore the Soft Constraints for the first prototype. Answer the Unknown Constraints before building.

## Common failure modes
- **Agent confuses requirements with constraints**: A requirement is "It needs an export button." A constraint is "The export cannot take longer than 5 seconds to generate." Tell the agent to filter out functional requirements.
