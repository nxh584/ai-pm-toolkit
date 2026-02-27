# Agent Session Log: Feedback Dashboard Prototype

*Context: This is a real, annotated log showing how a PM uses the toolkit to get an agent to build a prototype. The PM has already written `problem-statement.md` and `user-context.md`.*

---

## 1. The Initial Prompt
*(Using the First-Pass Build prompt and the loaded skills)*

**[PM Prompt]**
`@skills/context-curation.md` `@skills/prototyping.md` `@user-context.md` `@problem-statement.md`
Read the attached context files. Act as a prototyping engineer. I want you to build the first-pass version of a solution to this problem.
Rules for this build:
1. Prioritise Speed-to-Learning: Build the simplest, fastest version that tests the core hypothesis. 
2. Mock the Rest: If a database, complex auth, or heavy backend isn't strictly necessary, mock it.
3. No premature optimisation.

Before outputting code:
- Explain the 1-2 key technical trade-offs you made to prioritise speed.
- List what you are intentionally NOT building in this pass.

---

## 2. The Agent's First Output

**[Agent Output]**
> I have reviewed the context. The problem is manual aggregation of feedback across Intercom, Notion, and Slack for Sarah, a non-technical solo PM. 
> 
> **Key Trade-offs for Speed:**
> 1. Instead of building OAuth integrations to Intercom and Notion, I am building a simple local Next.js app with a mocked JSON file representing "pulled" data. This lets us test the UI/UX of *reviewing* the data before we spend 10 hours fighting external APIs.
> 
> **What I am NOT building:**
> - Actual API connections.
> - A database (we'll just use React state).
> - User authentication.
>
> Here is a simple Next.js dashboard that pulls from `mockData.json` and displays the aggregated quotes in a 3-column Kanban board (Inbox, Tagged, Archived).
> *(Outputs standard Next.js code for a Kanban board)*

*(Annotation: The agent built a Kanban board. Let's look at Sarah's context again. Under "Mental Model", you can see she wants an "inbox" experience, but under "What a Good Solution Feels Like", it says "A good solution feels invisible... It does not force her to log into a new dashboard every day." The agent ignored that constraint because "dashboard" is a default AI trap).*

---

## 3. The PM's Course Correction
*(Using the Course-Correct prompt)*

**[PM Prompt]**
The prototype runs, but it does not solve the problem correctly. 

Here is my feedback:
1. Currently, it is a web dashboard with a Kanban board. That's not right because Sarah explicitly does not want to log into a new dashboard (see `problem-statement.md`). She wants an invisible solution, ideally a Friday digest.
2. I noticed an edge case: if she tags something in this Kanban board, it just sits in the browser state and disappears when she closes the tab.

Based on this feedback:
1. Explain back to me why the original design was flawed based on user behaviour.
2. Outline the specific code changes needed to fix this.
3. Provide the updated code.

---

## 4. The Agent's Second Output

**[Agent Output]**
> **Why the original design was flawed:**
> I leaned into the "dashboard" UI pattern, which violated Sarah's core constraint: she wants an invisible solution that doesn't add another tool to her stack. A Kanban board requires active management, whereas she explicitly requested a Friday afternoon digest that requires zero active aggregation.
>
> **Code Changes:**
> 1. I am scrapping the Next.js web application entirely. 
> 2. I am replacing it with a simple Node.js script. This script will mock pulling the data, generate a formatted Markdown summary of the top 3 themes, and output it to the console (simulating an email or Slack message payload).
> 3. This can be run on a cron job every Friday at 4 PM.
>
> Here is the script:
> *(Outputs a 50-line Node.js script that groups mock data by tags and prints a clean text summary)*

*(Annotation: Much better. The agent threw away the complex UI and wrote a simple script that actually matches the user's mental model).*

---

## 5. The Ship or Kill Evaluation
*(Using the Ship or Kill prompt)*

**[PM Prompt]**
`@skills/evaluation.md` 
Review the Node.js script prototype against our `problem-statement.md`. Act as a ruthless Executive sponsor. Evaluate the current state against success criteria and choose: SHIP, ITERATE, or KILL. Provide a 3-sentence justification.

**[Agent Output]**
> **Alignment Check**: It solves the actual problem (aggregation visualisation) without requiring a new UI.
> **Success Measurement**: We can measure success by seeing if Sarah actually reads/uses the text output this Friday.
>
> **Recommendation**: **ITERATE**
> **Justification**: The core workflow (script instead of dashboard) is correct and aligns perfectly with Sarah's need for an invisible solution. However, it currently relies on a `mockData.json` file. To actually test this with Sarah this Friday, we must swap the mock data for a real API call to at least *one* of her sources (e.g., Slack) so she can experience real value. Fix the Slack connection, then SHIP.
