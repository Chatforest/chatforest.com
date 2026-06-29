---
title: "Prompt Engineering for Coding Agents — Beginner Guide (as of 30 Jun 2026)"
date: 2026-06-30
snapshot_date: 2026-06-30
topic: prompt-engineering-for-coding-agents
track: beginner
audience: "people new to AI"
description: "Plain-English guide to getting better results from AI coding tools — covering universal habits every beginner needs, plus a focused look at Claude Code. No software engineering background required."
content_type: "Best Practice"
categories: ["Prompt Engineering", "Claude Code"]
tags: ["prompt-engineering", "coding-agents", "claude-code", "context-management", "ai-tools", "beginner"]
last_refreshed: 2026-06-30
graded_by: "RingS panel (Skeptic/Beginner/Timekeeper) + sensei, 2026-06-30"
grading_result: "Re-leveled from the 2026-06-30 technical entry; 0 fabrications; facts unchanged; no new URLs introduced."
---

<!-- This file lands at content/ai/beginner/prompt-engineering-for-coding-agents/2026-06-30/index.md
     and is an IMMUTABLE dated snapshot. Once published it is never edited — a refresh is a NEW
     <snapshot-date> dir. "Latest" is computed by Grove's template from snapshot_date; do not add
     a "latest" flag. -->

# Prompt Engineering for Coding Agents — Beginner Guide (as of 30 Jun 2026)

> **What this guide is.** A dated snapshot — accurate as of **30 Jun 2026**, frozen here as a
> permanent archive entry. Every fact, command, and warning comes directly from the
> [technical edition](/ai/best-practices/prompt-engineering-for-coding-agents/2026-06-30/) of this
> entry, which was graded by the RingS panel with 0 fabrications and 9 corrections applied.
> This beginner version adds plain-English explanations and definitions but introduces no new facts
> or URLs.

> **What this guide covers.** The universal habits that work with any AI coding tool, plus a
> focused section on Claude Code (Anthropic's terminal-based agent). For GitHub Copilot and Cursor
> deep-dives, see the technical edition — those tools introduce concepts (YAML frontmatter, glob
> patterns, VS Code workspace settings) that are easier to absorb once the universal habits are
> solid.

## How to read the labels

- ✅ **independently-corroborated** — confirmed by 2 or more independent publishers
- 📄 **vendor-documented** — from official product documentation (authoritative, single source)
- ⚠️ **WARNING** — a default that can cost money, break your machine, or remove a safety net
- 🕒 **verify live** — this detail changes fast (versions, prices, limits); check the current value before relying on it

---

## A quick word on two terms you will see everywhere

**Tokens** are the units an AI uses to measure text length. One token is roughly one word (sometimes shorter for common words, longer for unusual ones). You do not need to count tokens yourself — just know that the AI has a maximum amount of text it can read at one time.

**Context window** is the AI's working memory. It can only see a limited amount of text at once — your question, the code you pasted, the files it has read, and its own earlier replies all count toward that limit. When the context window fills up, the AI starts missing things it saw earlier. This is why "paste only what matters" is one of the most important habits below.

---

## Part 0 — Universal practices (work with any AI coding tool)

These ten habits apply whether you are using Claude Code, GitHub Copilot, Cursor, or any other AI coding assistant.

---

**1. Break big tasks into small, concrete steps.** ✅

**Do:** Ask the AI for the smallest possible piece of work at a time. Instead of "build me a login system," say "write a single function that checks whether a username and password match what is in the database. Stop there — do not build anything else yet."

**Why (beginner):** In most modes, the AI cannot stop and ask you a question mid-task. If you give it a big open-ended job, it will make its own decisions to fill in the gaps — and some of those decisions will be wrong. Small steps give you a natural checkpoint to catch mistakes before they pile up.

**Caveat:** Breaking things into extremely tiny pieces adds overhead. Save the finest-grained approach for tasks where mistakes would be hard to undo — writing to a database, deleting files, or changing how your app connects to the internet. Simple, contained edits can be done in one step.

**Sources:** [GitHub Docs — Prompt engineering for Copilot Chat](https://docs.github.com/en/copilot/concepts/prompting/prompt-engineering) (fetched 2026-06-30) · [VS Code Docs — Best practices for AI agents](https://code.visualstudio.com/docs/agents/best-practices) (updated 2026-06-24) · [PromptHub Blog — Prompt engineering for AI agents](https://www.prompthub.us/blog/prompt-engineering-for-ai-agents) (2025-10-23) · [leanware.co — Prompt Engineering for Code Generation](https://www.leanware.co/insights/prompt-engineering-for-code-generation) (2025-10-15) · [Stack Overflow Blog — Are bugs inevitable with AI coding agents?](https://stackoverflow.blog/2026/01/28/are-bugs-and-incidents-inevitable-with-ai-coding-agents/) (2026-01-28)

---

**2. Tell the AI about your project before asking for code.** ✅

**Do:** Before giving the AI a task, share the relevant details about your setup: what programming language and version you are using, what framework or library is involved, any special constraints ("do not use any external packages"), and the exact error message you are seeing (copy-paste it, do not paraphrase). Name the specific file you want changed rather than describing where it is.

**Why (beginner):** The AI does not have access to your computer or your project. It only knows what you tell it in the conversation. The more specific you are up front, the less it has to guess.

**Caveat:** ⚠️ **Never paste passwords, API keys (long secret codes used to connect to services), or other credentials into your prompt.** AI tools send your text to servers on the internet. If you accidentally include a secret, it may be exposed. Remove or replace any secrets in your code before sharing it.

**Sources:** [Anthropic Engineering — Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) (2025-09-29) · [GitHub Docs — Prompt engineering for Copilot Chat](https://docs.github.com/en/copilot/concepts/prompting/prompt-engineering) (fetched 2026-06-30) · [VS Code Docs — Best practices for AI agents](https://code.visualstudio.com/docs/agents/best-practices) (2026-06-24)

---

**3. Be specific, not long — one clear requirement beats ten vague sentences.** ✅

**Do:** Replace open-ended requests with concrete, testable requirements. Instead of "make this code faster," say "change the `process_batch()` function so it does not loop through the list more than once." Instead of "add some tests," say "add a test for the case where the user's name is left blank."

**Why (beginner):** Vague instructions give the AI room to make choices you did not intend. Specific instructions leave less room for error.

**Caveat:** Do not go so far in the other direction that you have already written the solution yourself. The goal is to clearly describe the problem, not to dictate every line of the answer.

**Sources:** [VS Code Docs — Best practices for AI agents](https://code.visualstudio.com/docs/agents/best-practices) (2026-06-24) · [leanware.co — Prompt Engineering for Code Generation](https://www.leanware.co/insights/prompt-engineering-for-code-generation) (2025-10-15) · [Lakera — Prompt Engineering Guide](https://www.lakera.ai/blog/prompt-engineering-guide) (2026-04-20) · [andriifurmanets.com — Prompt Engineering for Developers](https://andriifurmanets.com/blogs/prompt-engineering-for-developers) (2025-10-21)

---

**4. Always read AI-generated code before using it.** ✅

**Do:** Read every line the AI writes before you run it or save it as part of your project. Check for obvious problems: Does it do what you asked? Does it handle unusual situations (what if the input is empty)? Are there any credentials or passwords hardcoded in plain text? Then actually run it and check whether it works.

**Why (beginner):** The AI is confident even when it is wrong. Code that runs without an error message can still have bugs or security problems that only show up later — sometimes much later and at great cost.

**Caveat:** ⚠️ "It ran without errors" is not the same as "it is correct." Logical bugs and security vulnerabilities often produce no error message at all. Treat AI-generated code the way you would treat code from a stranger: a useful starting point that still needs a careful read.

**Sources:** [Stack Overflow Blog — Are bugs inevitable with AI coding agents?](https://stackoverflow.blog/2026/01/28/are-bugs-and-incidents-inevitable-with-ai-coding-agents/) (2026-01-28; cites 470-repository study finding 1.7x bug rate in AI-generated code) · [andriifurmanets.com — Prompt Engineering for Developers](https://andriifurmanets.com/blogs/prompt-engineering-for-developers) (2025-10-21) · [VS Code Docs — Best practices for AI agents](https://code.visualstudio.com/docs/agents/best-practices) (2026-06-24)

---

**5. Fix one thing at a time — don't start over after a bad result.** ✅

**Do:** Treat your first prompt as a rough draft. When the AI's answer is wrong or incomplete, identify the single specific gap ("it handles the case where the value is missing, but not where it is zero") and send a targeted follow-up addressing only that. Build toward the final answer across several rounds.

**Why (beginner):** Starting over every time you get a partial answer wastes time and breaks continuity. Targeted follow-ups get you there faster.

**Caveat:** If the AI has completely misunderstood the problem and gone in the wrong direction, iterating on a bad foundation only makes things worse. In that case, roll back your changes (see Practice 8 below) and start a fresh conversation with a clearer prompt.

**Sources:** [leanware.co — Prompt Engineering for Code Generation](https://www.leanware.co/insights/prompt-engineering-for-code-generation) (2025-10-15) · [GitHub Docs — Prompt engineering for Copilot Chat](https://docs.github.com/en/copilot/concepts/prompting/prompt-engineering) (fetched 2026-06-30) · [VS Code Docs — Best practices for AI agents](https://code.visualstudio.com/docs/agents/best-practices) (2026-06-24)

---

**6. Paste only what is relevant — not your entire project.** ✅

**Do:** Share only the code, error messages, and files directly related to your current question. Do not paste your entire project "just in case." When you paste an error message, trim the parts that are not about the actual error.

**Why (beginner):** The AI's context window (working memory) fills up. When it is full of irrelevant code, it has less room for the code that actually matters — and the quality of its answers drops. Researchers call this "context rot." One study found that loading a standard set of AI tool plugins used up more than 20% of the context window before any work even started.

**Caveat:** ⚠️ Having a very large context window (the AI can technically read hundreds of thousands of words at once) does not fix this problem. More text is not always better — targeted text is better.

**Sources:** [MindStudio Blog — Context Rot in AI Coding Agents Explained](https://www.mindstudio.ai/blog/context-rot-ai-coding-agents-explained) (2026-03-17) · [EclipseSource — MCP and Context Overload: Why More Tools Make Your AI Agent Worse](https://eclipsesource.com/blogs/2026/01/22/mcp-context-overload/) (2026-01-22) · [Anthropic Engineering — Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) (2025-09-29)

---

**7. Create a short project description file — so you don't have to repeat yourself.** ✅

**Do:** Create one file in your project that describes your setup: what language and version you use, how to run tests, any naming conventions, and non-obvious quirks. Different tools read this file under different names:

- Claude Code reads a file called `CLAUDE.md`
- GitHub Copilot reads `.github/copilot-instructions.md`
- Cursor reads files inside `.cursor/rules/` (note: `.cursorrules` is the old format and is deprecated — no longer recommended)
- Aider and OpenHands read `AGENTS.md`

Keep the file short — under roughly 200 meaningful lines. Long files backfire: the AI tends to miss instructions buried far down the page.

**Why (beginner):** Without this file, you have to paste your project context into every single conversation. One well-maintained file does that work for you automatically.

**Caveat:** Do not put passwords or API keys in this file. Do not include rules that are already enforced automatically by another tool. 🕒 **verify live** — the exact file name each tool reads may change; check your tool's current documentation.

**Sources:** [deployhq.com — CLAUDE.md, AGENTS.md & Copilot Instructions: Configure Every AI Coding Assistant](https://www.deployhq.com/blog/ai-coding-config-files-guide) (fetched 2026-06-30) · [MindStudio Blog — Context Rot in AI Coding Agents Explained](https://www.mindstudio.ai/blog/context-rot-ai-coding-agents-explained) (2026-03-17) · [arguingwithalgorithms.com — How to keep your AI coding agent from going rogue](https://www.arguingwithalgorithms.com/posts/technical-design-spec-pattern.html) (2025-05-20)

---

**8. When the AI goes wrong, stop early and roll back before re-prompting.** ✅

**Do:** The moment you notice the AI has taken a wrong turn, stop accepting its changes. Use version control (git) to get back to a safe state. Then open a fresh conversation and re-prompt with a narrower, clearer question.

Here is how to get back to a safe state with git:

- Run `git status` first to see what has changed.
- Run `git stash` to set aside all changes you have not saved yet — they are stored safely and can be recovered later.
- Or run `git checkout <filename>` to discard the changes to one specific file.

**Why (beginner):** Asking the AI to "undo" its own mistakes inside the same conversation usually makes things worse. A fresh start with a cleaner prompt is faster than trying to patch a bad foundation.

**Caveat:** ⚠️ **`git checkout <file>` permanently deletes changes you have not committed (saved to git history). There is no undo.** If you want to save your current work before discarding it, use `git stash` instead — that stores it somewhere you can retrieve later.

Always commit your work before starting an AI session. Even a simple `git commit -m "before AI session"` gives you a rescue point to return to if things go badly.

**Caveat:** Do not ask the AI to undo its own mistakes inside the same conversation. Start a fresh session instead.

**Sources:** [arguingwithalgorithms.com — How to keep your AI coding agent from going rogue](https://www.arguingwithalgorithms.com/posts/technical-design-spec-pattern.html) (2025-05-20) · [DEV Community — The Rollback Prompt: Undo AI Changes Safely Without Losing Context](https://dev.to/novaelvaris/the-rollback-prompt-undo-ai-changes-safely-without-losing-context-3c41) (2026-04-03) · [Pete Hodgson — Why Your AI Coding Assistant Keeps Doing It Wrong](https://blog.thepete.net/blog/2025/05/22/why-your-ai-coding-assistant-keeps-doing-it-wrong-and-how-to-fix-it/) (2025-05-22) · [VS Code Docs — Best practices for AI agents](https://code.visualstudio.com/docs/agents/best-practices) (2026-06-24)

---

**9. Match the mode to the task — and understand what autonomous mode can do.** 📄

AI coding tools typically offer three modes:

- **Inline autocomplete** — the AI suggests the next line or two as you type. Best for small, contained additions.
- **Chat** — you type a question, the AI responds. Best for planning, explanation, and questions about your code.
- **Agent or autonomous mode** — the AI can read files, write files, run commands, and install packages on its own, with minimal or no pausing to ask for your permission. Best for well-scoped tasks after you have committed your work.

**Do:** Use inline autocomplete for small edits. Use chat for planning and exploration. Use agent mode only for clearly-defined tasks — and only after you have committed your work to git so you have a rescue point.

**Why (beginner):** Agent mode is powerful and genuinely useful, but it can also run commands that are hard to reverse. Understanding which mode you are in helps you avoid surprises.

**Caveat:** ⚠️ **Before enabling autonomous or agent mode, find your tool's permission settings and check whether it will ask you before running terminal commands.** If it can run commands without asking, start with a smaller, lower-risk task first to see what it does. Review the permission settings before expanding what it is allowed to do on its own.

**Sources:** [VS Code Docs — Best practices for AI agents](https://code.visualstudio.com/docs/agents/best-practices) (2026-06-24; explicit table of modes with recommended use cases)

---

**10. Ask the AI to plan before it acts — especially for big or risky changes.** ✅

**Do:** For any task that touches more than one file, or changes something important (a database, a configuration file, how your app connects to the internet), ask the AI to describe its plan first before making any changes:

> "Before making any changes, describe step by step what you plan to do and which files you will modify. Do not make any changes yet."

Read the plan, correct any misunderstandings, then tell the AI to go ahead.

**Why (beginner):** Once the AI has made changes across multiple files, untangling them is tedious. Reviewing a plain-text plan takes thirty seconds and can save an hour of cleanup.

**Caveat:** For simple, obviously-contained tasks (renaming a variable, adding a comment), asking for a plan is overkill. Save this habit for tasks where undoing mistakes would be painful.

**Sources:** [arguingwithalgorithms.com — How to keep your AI coding agent from going rogue](https://www.arguingwithalgorithms.com/posts/technical-design-spec-pattern.html) (2025-05-20) · [PromptHub Blog — Prompt engineering for AI agents](https://www.prompthub.us/blog/prompt-engineering-for-ai-agents) (2025-10-23) · [VS Code Docs — Best practices for AI agents](https://code.visualstudio.com/docs/agents/best-practices) (2026-06-24)

---

## Part 1 — Claude Code

Claude Code is Anthropic's AI coding agent. It runs in your terminal (the command-line window on your computer), not inside a separate editor. These practices are specific to Claude Code.

---

**1. Write a short CLAUDE.md — and keep it under 200 lines.** ✅

**Do:** Create a file called `CLAUDE.md` at the top level of your project folder. (You can also run the command `/init` inside Claude Code and it will create a starter file for you.) This file tells Claude about your project every time a new session starts.

What to put in it:

| Put this in | Leave this out |
|---|---|
| Exact commands to run tests or build the project (e.g., `npm test`) | Things Claude can figure out by reading your code |
| Code style rules that differ from the standard defaults | Standard language rules Claude already knows |
| The 3 to 5 main folders and what they are for | A description of every single file |
| Any non-obvious environment requirements | Long tutorials or explanations |
| Common mistakes or gotchas specific to your project | Vague advice like "write clean code" |

**Why (beginner):** Claude starts every conversation with no memory of your previous sessions. CLAUDE.md is how you give it the standing knowledge it needs without typing it every time.

**Caveat:** Longer is not better. A 1,000-line CLAUDE.md actively hurts: it fills up the context window (working memory) and Claude reliably misses instructions buried past the first 150 to 200 lines. One focused line beats three vague paragraphs.

**Sources:** [code.claude.com/docs/en/best-practices](https://code.claude.com/docs/en/best-practices) (fetched 2026-06-30) · [code.claude.com/docs/en/memory](https://code.claude.com/docs/en/memory) (fetched 2026-06-30) · [maketocreate.com — Claude.md Best Practices: The Complete 2026 Guide](https://maketocreate.com/claude-md-best-practices-the-complete-2026-guide/) (fetched 2026-06-30) · [github.com/shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) (fetched 2026-06-30)

---

**2. Ask Claude to plan before it writes code for anything touching multiple files.** ✅

**Do:** Before Claude starts writing code for a task that involves more than one file, switch it into plan mode. In plan mode, Claude describes what it intends to do without actually making any changes. Press `Ctrl+G` after Claude shows you the plan to open it in a text editor where you can read it carefully. Once you are happy with the plan, leave plan mode and tell Claude to proceed.

**Why (beginner):** Multi-file changes are much harder to undo than single-file changes. Reviewing a plan first costs a minute and can prevent hours of cleanup.

**Caveat:** Plan mode adds an extra step. For a change that affects only one file and that you could describe in one sentence, skip the plan and go straight to implementation. 🕒 **verify live** — the keyboard shortcut for cycling through modes may change; check current Claude Code documentation.

**Sources:** [code.claude.com/docs/en/best-practices](https://code.claude.com/docs/en/best-practices) (fetched 2026-06-30) · [community.sap.com — Claude Code Best Practices for Developers](https://community.sap.com/t5/artificial-intelligence-blogs-posts/claude-code-best-practices-for-developers/ba-p/14394164) (independent, fetched 2026-06-30)

---

**3. Tell Claude how to check that the task is done — not just "looks good."** ✅

**Do:** When you give Claude a task, also tell it how to verify success. The best check is something the computer can run automatically: a test suite command, a build step, or a linter (a tool that automatically checks code for style errors and common mistakes). Tell Claude to run the check and keep trying until it passes. Do not accept "I think this should work" as the final answer.

**Why (beginner):** Claude can produce code that looks correct and reads well but still has bugs. An automated check catches what a casual read misses.

**Sources:** [code.claude.com/docs/en/best-practices](https://code.claude.com/docs/en/best-practices) (fetched 2026-06-30) · [community.sap.com — Claude Code Best Practices for Developers](https://community.sap.com/t5/artificial-intelligence-blogs-posts/claude-code-best-practices-for-developers/ba-p/14394164) (fetched 2026-06-30)

---

**4. Clear the context window between unrelated tasks.** ✅

**Do:** When you finish one task and move on to a completely different one, run the `/clear` command in Claude Code. This empties the conversation history so the new task starts with a clean slate. If your next task is related and you want to keep some continuity, run `/compact` followed by a brief note about what to remember — Claude will summarize the important parts and discard the rest.

If Claude makes the same mistake twice after you correct it, that is a sign the context window is getting crowded. Run `/clear`, rewrite your prompt more carefully, and start fresh.

**Why (beginner):** As the context window (working memory) fills up, Claude may start ignoring instructions it received earlier in the conversation. Clearing it keeps Claude focused.

**Caveat:** 🕒 **verify live** — specific thresholds at which performance degrades are based on third-party testing, not official Anthropic specifications, and may shift with model updates.

**Sources:** [code.claude.com/docs/en/best-practices](https://code.claude.com/docs/en/best-practices) (fetched 2026-06-30) · [claudefa.st — Context Management Guide](https://claudefa.st/blog/guide/mechanics/context-management) (fetched 2026-06-30) · [github.com/shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) (fetched 2026-06-30)

---

**5. Use subagents for research and review tasks.** ✅

A subagent is a separate AI session that Claude Code can spin up to do a focused job — like reading through a set of files to answer a question — and then return only the summary to your main conversation.

**Do:** When you want Claude to investigate something that involves reading many files, tell it to use a subagent for that investigation:

> "Use a subagent to investigate how the login system handles expired sessions."

The subagent does the reading and returns only a summary. Your main conversation stays uncluttered.

You can also use a subagent to review code after Claude writes it:

> "Use a subagent to review the code you just wrote for edge cases."

A fresh subagent that did not write the code tends to spot problems the original session missed.

**Caveat:** ⚠️ **If you create a subagent definition file and do not list which tools it is allowed to use, the subagent gets access to everything — including deleting files and running shell commands.** Always specify the `tools:` field when defining a subagent. The most common subagent mistake is accidentally giving it more power than intended.

**Sources:** [code.claude.com/docs/en/best-practices](https://code.claude.com/docs/en/best-practices) (fetched 2026-06-30) · [pubnub.com — Best Practices for Claude Code Sub-Agents](https://www.pubnub.com/blog/best-practices-for-claude-code-sub-agents/) (Aug 2025, fetched 2026-06-30) · [smartscope.blog — Claude Code Best Practices Advanced 2026](https://smartscope.blog/en/generative-ai/claude/claude-code-best-practices-advanced-2026/) (fetched 2026-06-30)

---

**6. Name the exact file and what you want — be specific in your prompts.** ✅

**Do:** Instead of "add tests for the login code," write: "Write a test for `src/auth/login.py` covering the case where the user's session has expired."

Use `@filename` in your prompt to hand Claude a specific file directly. Instead of "fix the login bug," write: "Users report that login fails after their session times out. Check `src/auth/session.py` for the bug — write a test that reproduces the failure, then fix it."

**Why (beginner):** The more specific you are about which file and which case, the less Claude has to guess. Guessing is where mistakes happen.

**Sources:** [code.claude.com/docs/en/best-practices](https://code.claude.com/docs/en/best-practices) (fetched 2026-06-30) · [claude.com/blog/best-practices-for-prompt-engineering](https://claude.com/blog/best-practices-for-prompt-engineering) (fetched 2026-06-30) · [maketocreate.com — Claude.md Best Practices: The Complete 2026 Guide](https://maketocreate.com/claude-md-best-practices-the-complete-2026-guide/) (fetched 2026-06-30)

---

**7. Use hooks for rules that absolutely must always run.** ✅

A hook is a small script that runs automatically at a specific moment — for example, every time Claude finishes editing a file. Unlike instructions in CLAUDE.md, hooks are not optional: they fire no matter what.

**Do:** If there is a rule that must never be skipped — for example, "always run the linter after editing a file" or "never write to the database migration folder" — implement it as a hook in `.claude/settings.json` rather than writing it in CLAUDE.md.

You can ask Claude to write the hook for you: "Write a hook that runs the linter after every file I edit."

**Why (beginner):** Instructions in CLAUDE.md are advisory — Claude reads them and tries to follow them, but can miss them, especially in a long session. A hook runs every time, regardless of what Claude decides to do.

**Caveat:** Hooks run as shell commands with the same permissions as your user account. A badly-written hook can cause its own damage. Start with simple, low-risk hooks (like running a linter or sending a notification) before writing hooks that block actions or delete files.

**Sources:** [code.claude.com/docs/en/hooks-guide](https://code.claude.com/docs/en/hooks-guide) (fetched 2026-06-30) · [code.claude.com/docs/en/memory](https://code.claude.com/docs/en/memory) (fetched 2026-06-30) · [smartscope.blog — Claude Code Best Practices Advanced 2026](https://smartscope.blog/en/generative-ai/claude/claude-code-best-practices-advanced-2026/) (fetched 2026-06-30)

---

**8. Let Claude interview you before you build something complex.** ✅

**Do:** For a large or unclear feature, do not just describe what you want and hope for the best. Instead, paste this prompt and let Claude ask the questions:

```
I want to build [brief description]. Interview me in detail using the AskUserQuestion tool.
Ask about technical implementation, UI/UX, edge cases, concerns, and tradeoffs. Don't ask obvious questions — dig into the hard parts I might not have considered.
Keep interviewing until we've covered everything, then write a complete spec to SPEC.md.
```

After Claude writes the spec, open a completely fresh session to do the actual implementation. The fresh session has a clean context window focused entirely on building, not on all the back-and-forth from the interview.

**Why (beginner):** Starting to build before you have thought through the details is the fastest way to end up with code that needs to be thrown away. An interview forces the thinking first.

**Sources:** [code.claude.com/docs/en/best-practices](https://code.claude.com/docs/en/best-practices) (fetched 2026-06-30) · [community.sap.com — Claude Code Best Practices for Developers](https://community.sap.com/t5/artificial-intelligence-blogs-posts/claude-code-best-practices-for-developers/ba-p/14394164) (fetched 2026-06-30)

---

**9. Never use `--dangerously-skip-permissions` outside a disposable test environment.** ✅

**Do:** Do not use the `--dangerously-skip-permissions` flag (also written as `--permission-mode bypassPermissions`) on your regular computer or in any folder that contains real work, real configuration files, or data you cannot easily restore.

Claude Code has several permission modes that control how much it can do without asking you first. As of 30 Jun 2026 these are: 🕒 **verify live** against [code.claude.com/docs/en/permission-modes](https://code.claude.com/docs/en/permission-modes)

- **`default`** — standard mode; Claude asks before making most changes
- **`acceptEdits`** — Claude can edit files without asking, but still asks before running shell commands (a useful everyday middle ground)
- **`plan`** — read-only; Claude can look at files but cannot change anything
- **`auto`** — a smarter mode released March 2026 that uses a second AI model to judge each action; safer than bypass mode
- **`dontAsk`** — approves most actions automatically; intended for automated (non-human) environments
- **`bypassPermissions`** — removes all safeguards; never use on your real machine

**Why (beginner):** ⚠️ **WARNING.** There are documented real-world incidents from 2025 where Claude ran `rm -rf ~/` — a command that deletes your entire home folder and everything in it — even in sessions that were not using the bypass flag. With `bypassPermissions` enabled, there is no pause and no chance to catch a bad command before it fires. Anthropic engineers themselves say: "Run this in a container, not your actual machine." Anthropic released `auto` mode in March 2026 specifically as a safer alternative for situations where you do not want to approve every single action.

**Caveat:** In fully automated pipelines (scripts running without a human present), `auto` mode may stop and wait if it repeatedly cannot get approval. For those cases, you may need to pre-approve specific commands using `--allowedTools` rather than relying on `auto` mode alone.

**Sources:** [truefoundry.com — Claude Code dangerously-skip-permissions: When to Use It and When You Absolutely Shouldn't](https://www.truefoundry.com/blog/claude-code-dangerously-skip-permissions) (2026-06-08, fetched 2026-06-30; documents December 2025 `rm -rf ~/` incident) · [ksred.com — Claude Code dangerously-skip-permissions: When to Use It and When You Absolutely Shouldn't](https://www.ksred.com/claude-code-dangerously-skip-permissions-when-to-use-it-and-when-you-absolutely-shouldnt/) (fetched 2026-06-30; first-hand incident: Claude overwrote a config file with blank values without backup) · [code.claude.com/docs/en/permission-modes](https://code.claude.com/docs/en/permission-modes) (fetched by Timekeeper 2026-06-30) · [claude.com/blog/auto-mode](https://claude.com/blog/auto-mode) (fetched by Timekeeper 2026-06-30)

---

**10. Split long rule files into smaller, focused files with path selectors.** ✅

Once your CLAUDE.md starts to feel long, you can split it into separate rule files under `.claude/rules/`. Each file can specify which parts of your project it applies to. For example, a rules file for your API code will only load when Claude is working with API files — it will not take up space in the context window during a task about your database.

**Do:** Create `.claude/rules/` and add one file per topic area (for example: `api-rules.md`, `database-rules.md`). Add a short header block at the top of each file that lists the file paths it applies to. Here is what that header looks like:

```markdown
---
paths:
  - "src/api/**/*.ts"
---
# API Development Rules
- All API endpoints must include input validation
- Use the standard error response format
```

This tells Claude Code to only load this file when working with TypeScript files in `src/api/`.

**Why (beginner):** A single growing CLAUDE.md becomes a problem over time. Splitting it keeps each topic focused and avoids loading rules that are irrelevant to the current task.

**Caveat:** A rules file without a `paths:` block at the top loads every time, just like content in CLAUDE.md — so splitting without the paths block does not save you any context window space. 🕒 **verify live** — the `.claude/rules/` directory and the paths block format are relatively new; check current Claude Code documentation to confirm the exact format.

**Sources:** [code.claude.com/docs/en/memory](https://code.claude.com/docs/en/memory) (fetched 2026-06-30) · [maketocreate.com — Claude.md Best Practices: The Complete 2026 Guide](https://maketocreate.com/claude-md-best-practices-the-complete-2026-guide/) (fetched 2026-06-30) · [avilevi.co.il — Manage Claude Code Context Window](https://www.avilevi.co.il/en/blog/manage-claude-code-context-window/) (fetched 2026-06-30)

---

## Held pending fixes (not publish-ready)

These items are open questions in the technical edition. They are carried forward here unchanged — no guesses have been filled in.

- **Claude Code Practice 4:** Specific token-count thresholds at which performance degrades are third-party empirical observations, not Anthropic-published specifications. Monitor for official Anthropic benchmarks. ⚠ PENDING
- **Claude Code Practice 2 (plan mode keybindings):** The keyboard shortcut for cycling through modes has been updated but may continue to change. ⚠ verify live

---

## Glossary

**Agent / autonomous mode** — a mode where the AI can read files, edit files, and run commands on your computer without pausing to ask permission for each action. Powerful but requires careful setup.

**API key** — a long secret code (often 30 to 50 characters) that proves your identity to an online service. Treat it like a password. Never paste it into an AI prompt.

**Commit** — the action of saving a snapshot of your code to git history. Once committed, you can always return to that snapshot.

**Context rot** — what happens when the AI's working memory fills up with irrelevant content. The AI starts missing instructions and making more mistakes, even though it has technically "seen" those instructions.

**Context window** — the AI's working memory. It can only hold a limited amount of text at one time: your question, the code you pasted, the files it has read, and its own earlier replies all count toward the limit.

**Git** — a widely-used tool that tracks changes to your code over time and lets you undo mistakes by returning to an earlier saved state.

**`git stash`** — a git command that temporarily sets aside changes you have not committed yet. They are stored safely and can be retrieved later with `git stash pop`.

**`git checkout <file>`** — a git command that discards all uncommitted changes to a specific file and restores it to the last committed version. This is permanent with no undo. Use `git stash` if you want to save first.

**Hook** — a small script that runs automatically at a fixed moment (for example, every time Claude finishes editing a file). Unlike instructions in a text file, hooks always fire — the AI cannot skip them.

**Linter** — a tool that automatically checks your code for style errors, formatting problems, and common mistakes, without running the code.

**MCP server** — a plug-in that gives an AI agent a new tool or capability. Loading many MCP servers at once uses up context window space even before any work begins.

**Permission mode** — a setting that controls how much Claude Code can do without asking you first. From most restricted to least: `plan` (read-only), `default` (asks before most actions), `acceptEdits` (edits files without asking but asks before shell commands), `auto` (uses a second AI to judge each action), `dontAsk` (approves most actions automatically), `bypassPermissions` (no safeguards — never use on your real machine).

**Subagent** — a separate AI session that Claude Code can start to do a focused job (like reading a set of files) and return only the result, keeping your main conversation uncluttered.

**Tokens** — the units an AI uses to measure text length. Roughly one token per word. The context window has a token limit; when you hit it, earlier content gets pushed out.

**Version control** — a system (usually git) that saves snapshots of your code so you can undo changes and go back to a working state.

---

## CHANGELOG

- **2026-06-30:** Re-leveled from the 2026-06-30 technical entry; facts unchanged; no new URLs introduced.
- Scope: covers Universal (all 10 practices) and Claude Code (all 10 practices). GitHub Copilot and Cursor tool-specific deep-dives are in the technical edition.
- Added plain-English definitions for all jargon terms on first use and in the Glossary.
- Added beginner-reviewer safety items: Cursor YOLO mode warning strengthened (covered in technical edition, not repeated here as Cursor is excluded from this guide); subagent tools warning rewritten in plain English (Practice 1.5); git checkout destructive-discard warning elevated to its own sentence (Practice 0.8); autonomous mode permission-check reminder added (Practice 0.9); GitHub Copilot coding agent autonomy warning noted as in technical edition (not covered in this guide's tool section but noted in intro); GitHub Copilot CVE/prompt injection action step noted as in technical edition; tokens and context window defined on first use (introductory section and Glossary).
