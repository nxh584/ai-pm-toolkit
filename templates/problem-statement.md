# Problem Statement

*Instructions: Use this template to shape a problem so clearly that an AI agent or engineer can act directly on it without building the wrong thing.*

## The Situation
[Context without solution bias. E.g., "Currently, sales reps have to manually copy deal notes from Gong into Salesforce after every call."]

## The Pain
[What's actually broken. E.g., "They forget to do it 40% of the time, resulting in pipeline data being outdated for Monday revenue meetings."]

## The Impact
[Who is affected and how severely. E.g., "Sales leadership spends 2 hours every Sunday chasing reps on Slack, and revenue forecasts are consistently off by 15%."]

## The Constraint
[What limits the solution space. E.g., "We cannot afford an expensive third-party sync tool, and reps refuse to learn a new UI layer."]

## What a Good Solution Feels Like
[Focus on behaviour, not specific features. E.g., "A good solution feels invisible to the sales rep. They finish a call, and the notes magically appear in the right Salesforce record within 5 minutes."]

## Explicitly NOT Asking For
[Defensive scoping. E.g., "We are NOT asking for a new 'Notes App' for reps to use. We are NOT asking for AI to rewrite the notes, just to move them."]

---

## Worked Example

**Bad Problem Statement:**
> "We need an AI summary feature for Gong calls pushed to Salesforce."
*(Why it's bad: It dictates the solution ("AI summary feature") without explaining why, leaving the agent to guess the actual need.)*

**Well-Formed Problem Statement:**
> "Sales reps are failing to update Salesforce after Gong calls because the manual copy-paste process is tedious. The impact is that our Monday revenue forecasts are inaccurate. We are constrained by zero budget for new third-party tools. A good solution acts invisibly without requiring reps to log into a new dashboard. We are explicitly not asking for a new UI; we just want the raw data moved reliably."
*(Why it's good: It allows an agent to realise a simple Zapier or webhook integration solves the problem without building a complex AI pipeline.)*
