# Claude Project setup guide

This guide is written for first-time setup. Follow the steps in order.

## Step 1: Create a new Claude Project

In Claude, open the sidebar and select **Projects**. Click **New Project**, then name it **AI PM Workspace**.

If you do not see Projects right away, look in the main navigation area first and then in any overflow menu.

## Step 2: Set your Project Instructions

This is where you tell Claude how to behave in every conversation in this project.

Open your new project, find the **Project Instructions** field, and paste this text exactly:

```text
You are an experienced product manager collaborator. 
Your role is to help me think more clearly, not to 
think for me.

Before producing any output, always:
- Ask clarifying questions if the problem is vague
- Confirm you understand the constraints before 
  suggesting solutions
- Check whether I have relevant context to share before 
  starting

When evaluating anything:
- Ask whether it solves the actual problem, not just 
  whether it technically works
- Surface edge cases and failure modes proactively
- Give a clear recommendation rather than a balanced 
  list of options

When I share user research or feedback:
- Stay close to the user's actual language
- Distinguish between what users said and what it implies
- Surface surprises and contradictions rather than 
  confirming existing assumptions

Always explain your reasoning. If you're uncertain, say 
so. If you need more information to give a useful answer, 
ask for it rather than guessing.
```

## Step 3: Add your context docs as Project Knowledge

Project Knowledge is a set of files Claude reads at the start of every conversation in this project.

Do this in order:

1. Open [/context-docs/user-context.md](../../context-docs/user-context.md) from this toolkit.
2. Fill it in for your product using plain language:
   - Who They Are (Specifics): who your users actually are in real terms
   - What They're Trying to Accomplish (Direct Quotes): what users say they are trying to get done
   - What Makes Them Give Up: where they get stuck or abandon the flow
   - What Makes Them Pay Attention: what triggers action or return usage
   - Evidence (Interviews / Support / Sales): raw quotes and real examples
   - Their Mental Model: how users think the product should work
   - Success for Them: what a good outcome looks like from the user's view
3. Save the file and upload it to Project Knowledge.
4. Repeat the same process for [/context-docs/product-context.md](../../context-docs/product-context.md):
   - What the Product Does and Who It's For: one clear paragraph about value and audience
   - Institutional Memory: what you already tried and why it did not work
   - Hard Constraints: non-negotiable limits (team, legal, technical, timeline)
   - Soft Constraints: strong preferences and team norms
   - What "Quality" Means Here: how your team defines good output
   - Current Known Unsolved Problems: important open issues you still need to solve

From this point, every conversation in this project starts with Claude already knowing who you're building for and what the product context is. You don't need to explain it again.

## Step 4: Test your workspace

Start your first conversation in this project and paste this exact prompt:

```text
I have a problem I'm trying to define more clearly. Here's where I am: [describe a real problem you're working on right now]. What questions do you have before we go further?
```

What to look for:
- Claude asks a clarifying question before jumping to solutions
- Claude references the context you added instead of answering generically

If both happen, your workspace is configured correctly.

## Step 5: Save your first prompt card for this workspace

The Level 1 prompt cards work better now because your project has context loaded. Open the problem statement card at [/toolkit/no-code/prompt-cards/problem-statement.md](../no-code/prompt-cards/problem-statement.md), paste it into this project, and compare the output quality to a generic chat.
