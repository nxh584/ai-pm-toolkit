# Feature Spec

*Instructions: This is a lightweight spec for smaller features and agent tasks where a full PRD is overkill.*

## 1. What We're Building
[One sentence. E.g., "A cron job that soft-deletes inactive user accounts after 90 days."]

## 2. Why
[One paragraph explaining the user or business value. E.g., "Our database costs are ballooning because we keep thousands of abandoned freemium accounts active in the cache. By soft-deleting them, we save $500/mo and improve query performance for active users."]

## 3. Input / Output
- **Input:** [What triggers this? E.g., "Daily trigger at 00:00 UTC."]
- **Output:** [What is the result? E.g., "Database `is_deleted` flag set to true; email sent to user; webhook fired to marketing."]

## 4. Acceptance Criteria
[Bulleted, testable statements.]
- Must run automatically once every 24 hours.
- Must ignore users who have logged in within the last 89 days.
- Must successfully set the `deleted_at` timestamp.
- Must send warning email 7 days before deletion.

## 5. Edge Cases
[The ones that actually matter.]
- What if a user logs in *while* the deletion job is running?
- What happens to paying customers whose credit cards failed last month? (They should be excluded from this job).

## 6. What We're Not Building
[Explicit boundaries. E.g., "We are NOT building a way for users to self-restore their accounts in the UI. They have to email support."]

## 7. Open Questions
[E.g., "Do we need to hard-delete the data later for GDPR compliance?"]
