# Launch Checklist

*Instructions: A simple, practical ship-readiness checklist designed for solo PMs and startups to avoid stupid mistakes before going live.*

## 1. Problem Definition Review
- [ ] Is this feature still solving the original problem we identified in the PRD, or did scope creep mutate it?
- [ ] Have we removed any "nice-to-have" features that are delaying the core launch?

## 2. User Validation
- [ ] Has at least one *real user* seen the prototype or staging environment?
- [ ] Did they successfully complete the core loop without us giving them instructions?

## 3. Edge Cases & Reality Check
- [ ] What happens if the network is slow?
- [ ] What happens if the user inputs weird data (e.g., a 100MB file instead of 1MB)?
- [ ] Does it work functionally on a mobile screen? (Even if just barely).

## 4. Instrumentation
- [ ] Do we have a way to measure the success metric defined in the PRD? E.g., is the button click actually being tracked in PostHog/Mixpanel?
- [ ] Do we have visibility into errors if the feature breaks?

## 5. The Rollback Plan
- [ ] Is this feature hidden behind a feature flag?
- [ ] If this breaks production, can we turn it off in under 60 seconds without redeploying code?
- [ ] Does turning it off leave user data in a corrupted state?

## 6. Communication
- [ ] Have we informed Customer Support what to say if a user complains about this?
- [ ] Has the changelog/release note been drafted in plain English?

## 7. Next Steps
- [ ] Have we scheduled 15 minutes on the calendar for 48 hours from now to specifically look at the metrics and retro this launch?
