# User Research Synthesis

*Instructions: Use this to structure raw interview notes or ticket data into actionable insights.*

## 1. Raw Observations
[Direct, unvarnished quotes or notes. Do not sanitise these.]
- "I literally keep a sticky note on my monitor to remind me to hit 'Sync' before I go home." - User A
- "If the upload fails, I just email the CSV to my manager instead. It's faster." - User B
- "I didn't even know there was an analytics tab." - User C

## 2. Patterns
[Themes that emerged across multiple sources.]
- **Trust Issues:** Users do not trust the background sync to work, so they manually verify it or bypass the system entirely.
- **Discoverability:** Core features are buried behind confusing navigation.

## 3. Surprises
[Things that contradicted your prior assumptions or `product-context.md`.]
- We assumed users wanted more complex chart types, but 4 out of 5 users export the data to Excel immediately anyway to make their own charts.

## 4. Jobs to be Done (JTBD)
[What users are actually hiring the product to accomplish.]
- "When I'm preparing for the Friday all-hands, help me grab exactly the three metrics I need so I don't look unprepared in front of the CEO."

## 5. Implications for the Product
[What this means for the roadmap or next sprint.]
- Stop building new chart widgets immediately. 
- Prioritise a "1-click Export to Excel" button on the main dashboard.
- Redesign the background sync UI to show a highly visible "Last Synced: 2 mins ago" indicator to rebuild trust.

## 6. Open Questions Raised
[New unknowns discovered during research.]
- Are the background syncs *actually* failing, or are they just taking too long and users assume they failed? We need to look at the logs.
