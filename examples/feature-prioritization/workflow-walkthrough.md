# Workflow Walkthrough: Prioritising Under Pressure

*Context: This is a narrative walkthrough of a PM using the toolkit to make a hard prioritisation decision when data is scarce and stakeholder pressure is high. The PM has populated the `context-doc.md` and has a messy list of 12 backlog items.*

---

## 1. The Setup

The PM, Alex, is staring at a Jira board with 12 items. Sales wants SSO. Marketing wants a slick new onboarding flow. Engineering wants to refactor the database. Alex has 1 engineer and 10 days. 

Instead of guessing, Alex decides to use the AI agent as a sparring partner to force a clear decision.

## 2. Extracting the True Constraints

Alex opens Cursor, attaches the `context-doc.md` and the raw list of 12 features. 

**[Alex's Prompt]**
*(Using a modified `extract-constraints.md` prompt)*:
> `@context-doc.md` Read the context. Here are the 12 backlog items. Do not tell me what to build yet. First, filter this list. Remove any item that objectively violates our two hard constraints: 
> 1) Cannot be built by 1 backend engineer in 10 days. 
> 2) Does not align with the narrative: "Ease of Use for Solo Creators."

**[System Output (Summary)]**
The agent aggressively chops the list. 
- It kills the "SSO / SAML integration" immediately. (Reason: SSO is for enterprise teams, not "Solo Creators", failing Constraint 2).
- It kills the "Database Refactor". (Reason: Unlikely to finish in 10 days with testing, fails Constraint 1).
- It leaves exactly 3 features that fit the bounds:
  1. 1-Click Google Auth (Fast, fits solo creators).
  2. CSV bulk upload wizard (Frontend heavy, but possible in 10 days).
  3. Pre-made project templates (High marketing value, moderate effort).

## 3. Exploring Parallel Approaches

Alex now has 3 viable options. He isn't sure which is best. He uses the `parallel-approaches.md` tool to synthesise the trade-offs before deciding.

**[Alex's Prompt]**
> Out of those 3 remaining features, I need to pick one. Act as a ruthless Product Leader. Give me the strongest argument for building Google Auth, and the strongest argument for building Pre-made Templates. Tell me what the biggest risk of failure is for both.

**[System Output (Summary)]**
The agent outlines the trade-offs:
- **Google Auth:** Strongest argument: Directly removes friction at the top of the funnel (Ease of use). Biggest risk: Doesn't give marketing much to talk about beyond "sign up faster."
- **Pre-made Templates:** Strongest argument: Gives marketing a massive visual asset for the launch to show off what the product can do. Biggest risk: Requires design input which we don't have listed in our constraints (we only have 1 backend engineer).

## 4. The Decision and the Defense

Alex realises that "Pre-made Templates" is a trap. He has no designer. Building templates with just a backend engineer will look terrible and ruin the marketing launch. The choice must be Google Auth.

Now, Alex needs to deal with the Sales team, who will be furious about SSO being killed. He uses the agent to synthesise the defense.

**[Alex's Prompt]**
> We are choosing Google Auth. Now, act as a defensive PM. Write a 3-bullet Slack message to the Head of Sales explaining why we are NOT building SSO right now. Ground the reasoning in the constraints listed in `context-doc.md`. Do not apologise.

**[System Output]**
> "Hey [Sales Head], for the upcoming sprint, we are prioritising Google Auth over SSO/SAML. Here is why:
> 1. **Strategic Alignment:** Leadership mandated the Q3 launch narrative is 'Solo Creators.' SSO is an enterprise feature that actively distracts from that core messaging right now.
> 2. **Capacity:** We have exactly 1 backend engineer for 10 days. An enterprise-grade, secure SAML integration requires closer to 3 weeks and security reviews to not break existing accounts.
> 3. **The Compromise:** We will lock SSO into the very next sprint for Q4 Enterprise pushes, but it cannot fit in this 10-day window without jeopardising the launch."

## 5. Result

Alex used the toolkit not to write code, but to process variables faster than humanly possible. By strictly bounding the agent with the `context-doc.md`, he turned a stressful, political 12-item backlog into a clean binary decision, filtered out a trap (requiring a designer), and auto-generated the internal comms to defend the choice.
