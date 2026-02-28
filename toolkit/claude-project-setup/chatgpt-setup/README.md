# ChatGPT setup (Level 2 equivalent)

This is the ChatGPT version of the Claude Project setup. The goal is the same: configure behavior once, keep useful context persistent, and stop starting every session from scratch.

## Claude vs ChatGPT: what's equivalent

- **Claude Project Instructions** -> **ChatGPT Custom Instructions**
- **Claude Project Knowledge** -> **ChatGPT Memory** (plus context files you paste or upload when needed)

## Where the experience differs

- Claude Projects are project-scoped by design. ChatGPT Memory can be broader, so confirm what it should remember and what it should not.
- Claude Project Knowledge uses attached project files directly. In ChatGPT, you may still need to paste or upload context docs at the start of an important conversation.
- Both can deliver strong PM collaboration quality when configured intentionally.

## Step 1: Set Custom Instructions

In ChatGPT settings, open **Custom Instructions** and paste this text:

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

## Step 2: Set Memory with your core context

Use [/context-docs/user-context.md](../../../context-docs/user-context.md) and [/context-docs/product-context.md](../../../context-docs/product-context.md) as your source files.

- Fill both files with real details about your users, product, and constraints.
- In a new chat, share the most important points and ask ChatGPT to remember them.
- Keep memory focused on stable facts (audience, constraints, quality bar), not temporary project details.

## Step 3: Run the same workspace test

Paste this prompt in a new chat:

```text
I have a problem I'm trying to define more clearly. Here's where I am: [describe a real problem you're working on right now]. What questions do you have before we go further?
```

A good result looks like this:
- ChatGPT asks a clarifying question first
- It reflects your saved context instead of giving a generic answer

## Step 4: Use Level 1 prompt cards in this setup

Open [/toolkit/no-code/prompt-cards/problem-statement.md](../../no-code/prompt-cards/problem-statement.md), paste it into your configured chat, and compare the quality against an unconfigured chat.

If the configured version asks better questions and gives more grounded output, your setup is working.
