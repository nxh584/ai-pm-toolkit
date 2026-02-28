# Cursor first session guide

This guide assumes you have never used a code editor before. Follow each step in order.

## Step 1: Download and install Cursor

Cursor is a text editor - like Microsoft Word, but designed for working with AI on technical projects. You do not need to know how to code to use it for what we are doing here.

Go to [cursor.com](https://cursor.com), download the version for your operating system, and install it.

## Step 2: Download the starter project

Go to the GitHub repository page for this toolkit. Click the green **Code** button, then click **Download ZIP**.

Save the ZIP file somewhere easy to find, then unzip it. Inside the unzipped folder, locate `toolkit/first-ide-session/starter-project/`.

## Step 3: Open the starter project in Cursor

In Cursor, choose **File > Open Folder** and select the unzipped `starter-project` folder.

When it opens:
- The panel on the left shows files in your project
- The main area is where you will read and edit files

Don't worry about anything else for now.

## Step 4: Open the AI panel

Open Cursor's AI chat panel from the sidebar chat icon (or the AI/Chat button in the interface).

This is where you describe what you want to build. Cursor reads your project files and uses that context to produce something useful.

## Step 5: Run your first session

Open `project-context.md` in the starter project and fill in:
- Who you are building for
- What problem you are trying to solve
- What good output would look like

Then paste this exact prompt into the AI panel:

```text
Please read the project-context.md file in this project before doing anything else. Once you have read it, confirm back to me in two sentences what you understand the problem to be and what I am trying to build. Then ask me one clarifying question before you start.
```

What to expect: Cursor will read your context file, summarize it back to you, and ask a question. This is it working correctly. Answer the question and let it proceed.

## Step 6: Evaluate what comes out

After Cursor gives first output, run this prompt:

```text
Before I review this - does it solve the problem described in project-context.md, or does it just technically work? What's the most important thing missing? What would you change if you were building this for real?
```

This prompt turns Cursor into a critic of its own work. The answer will tell you more about what to fix than looking at the output yourself.

## Step 7: Iterate once

Respond to Cursor's self-critique with:

```text
Fix the most important thing you identified. Explain what you changed and why.
```

You have now completed one full loop: describe, build, evaluate, improve. This is the core of the AI-native PM workflow. Everything in the main toolkit is built around this loop.

You are no longer a non-technical PM figuring out AI tools. You are a PM who just ran a complete agent-assisted workflow. The rest of the toolkit is yours to explore.
