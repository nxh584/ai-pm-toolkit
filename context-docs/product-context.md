# Product Context Template

*Instructions: This document grounds the agent in your product's reality, preventing it from suggesting architectures you can't support or features you've already decided against.*

## 1. What the Product Does and Who It's For
[Write ONE clear paragraph explaining the core value proposition. e.g., "This product is an automated data-cleaning tool for solo data scientists. It ingests messy CSVs, normalises phone numbers and emails without manual mapping, and exports clean JSON."]

## 2. Institutional Memory (What we've tried that didn't work)
[List previous feature attempts, architectures, or designs that failed, and specifically *why* they failed. e.g., "We tried offering a visual flow-builder in 2023. Users hated it because it was slower than writing Python scripts. Do not suggest visual node-based editors."]

## 3. Hard Constraints
[List technical, legal, resource, or compliance boundaries that cannot be crossed. e.g., "We have zero backend engineers. Everything must be built with serverless functions and Supabase. No user data can leave the EU."]

## 4. Soft Constraints
[List preferences, style guidelines, and team norms. e.g., "We prefer boring technology. We use system fonts. If a feature requires a tutorial, it's too complex."]

## 5. What "Quality" Means Here
[Define quality for your specific product context. e.g., "Quality means speed. We will sacrifice advanced filtering options if it means the main dashboard loads in under 200ms."]

## 6. Current Known Unsolved Problems
[What are the big hairy issues you haven't figured out yet? e.g., "We still don't have a good way to handle multi-tenant authentication securely without forcing users to re-login every 24 hours."]
