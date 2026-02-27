# Problem Statement: Feedback Aggregation

## The Situation
Feedback for our B2B SaaS product currently lives in three silos: Intercom (support), Notion (sales call notes), and a #customer-feedback Slack channel (internal chatter).

## The Pain
Our Solo PM (Sarah) has no single view of this data. Currently, she spends roughly 3 hours every Friday afternoon manually reading through these three tools, copying quotes, pasting them into a master Google Sheet, and manually adding feature tags.

## The Impact
Because manual aggregation is tedious, she frequently delays it or skips it if she is busy. As a result, product prioritisation decisions are often made based on whoever complained the loudest in Slack that morning, rather than objective aggregated data. Furthermore, she struggles to justify roadmap decisions to the CEO because surfacing the supporting quotes takes too long.

## The Constraint
- **Technical**: Sarah is non-technical and cannot write Python scripts or maintain complex Zapier chains. 
- **Resource**: She has zero engineering capacity to build an internal tool.
- **Budget**: The startup will not pay $500/mo for a heavy enterprise feedback tool like DoveTail or Productboard.

## What a Good Solution Feels Like
A good solution feels invisible. Sarah finishes her week, and at 4:00 PM on Friday, the quotes from Intercom, Notion, and Slack have already been aggregated, deduplicated, and roughly categorised into a single readable list that she can skim in 10 minutes. It does not force her to log into a new dashboard every day.

## Explicitly NOT Asking For
- We are NOT asking for a complex multi-view web application dashboard.
- We are NOT asking for an AI to automatically reply to customers or close tickets.
- We are NOT asking for a bidirectional sync back to Intercom. We just want a one-way aggregation.
