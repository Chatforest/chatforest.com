---
title: "Prompt Engineering for GitHub Copilot — Beginner Guide (as of 01 Jul 2026)"
date: 2026-07-01
snapshot_date: 2026-07-01
topic: prompt-engineering-github-copilot
track: beginner
audience: "people new to AI"
description: "Plain-language practices for getting better results from GitHub Copilot — written for someone who just installed Copilot and has never used an AI coding tool before."
content_type: "Best Practice"
categories: ["GitHub Copilot", "Prompt Engineering"]
tags: ["github-copilot", "prompt-engineering", "copilot-chat", "agent-mode", "vs-code", "ai-credits"]
last_refreshed: 2026-07-01
graded_by: "RingS panel (Skeptic/Beginner/Timekeeper) + sensei, 2026-06-30; published 2026-07-01"
grading_result: "0 fabrications; 5 corrections applied; 2 items remain ⚠ PENDING; beginner re-level by rings-beginner-author"
---

<!-- This file lands at content/ai/beginner/prompt-engineering-github-copilot/2026-07-01/index.md and is an IMMUTABLE
     dated snapshot. Once published it is never edited — a refresh is a NEW <snapshot-date> dir.
     "Latest" is computed by Grove's template from snapshot_date; do not add a "latest" flag. -->


# Getting Better Results from GitHub Copilot — Beginner Guide (as of 01 Jul 2026)

> **Grading note.** A dated snapshot — accurate as of **01 Jul 2026**, frozen here and kept as
> a permanent archive entry. Research-drafted by a pupil, graded by the 3-lens panel + sensei.
> Corrections applied inline; unverifiable gaps marked ⚠ PENDING — never guessed.
> Re-leveled for beginners from the 2026-07-01 technical entry; facts unchanged.

## What is GitHub Copilot and why do these practices matter?

GitHub Copilot is an AI assistant built into your code editor (most commonly VS Code — Visual Studio Code). It watches what you type and suggests code completions, answers questions in a chat window, and — in its most powerful mode — can write and run code entirely on its own. Think of it as an eager new colleague who works very fast but sometimes makes mistakes, can accidentally expose your passwords, and can run up a bill without warning you first.

These practices exist to help you get useful suggestions, keep your project safe, and avoid surprises. Each one is short and concrete. Read them before you rely on Copilot for anything important.

## How to read the labels

- ✅ **independently-corroborated** — confirmed by 2 or more independent sources
- 📄 **vendor-documented** — official GitHub or Microsoft documentation (authoritative, single source)
- ⚠️ **WARNING** — a default that can cost real money, break something, or create a security hole
- 🕒 **verify live** — prices, quotas, or features that change often; check the link for the current value

---

## Practice 1: Create a .github/copilot-instructions.md file — tell Copilot what your project is

**Do:** In the root folder of your project, create a file at exactly this path: `.github/copilot-instructions.md`. Write five short sections inside it:

1. What your app does (one or two sentences)
2. Your tech stack (for example: "Python 3.12, Flask, PostgreSQL")
3. Coding guidelines (for example: "use type hints everywhere")
4. Project structure (which folders hold which things)
5. Available tools (any scripts or helpers a developer would use)

Keep the whole file to two pages or less. Save the file, then commit it — committing means running `git add .github/copilot-instructions.md` followed by `git commit -m "Add Copilot instructions"` to permanently save the file into your project's version history. Everyone on your team will benefit once it is committed.

**Why (beginner):** Copilot reads this file at the start of every Chat session. Without it, Copilot is guessing your tech stack and your rules — and it guesses wrong. A two-minute file saves you hours of correcting bad suggestions.

**What goes wrong without it:** Copilot suggests code for the wrong framework, ignores your team's naming conventions, and gives you answers that look correct but do not fit your project.

**Sources:**
- [github.blog/ai-and-ml/github-copilot/5-tips-for-writing-better-custom-instructions-for-copilot/](https://github.blog/ai-and-ml/github-copilot/5-tips-for-writing-better-custom-instructions-for-copilot/) (GitHub Blog, published 2025-09-03, updated 2026-06-14)
- [github.blog/ai-and-ml/github-copilot/onboarding-your-ai-peer-programmer-setting-up-github-copilot-coding-agent-for-success/](https://github.blog/ai-and-ml/github-copilot/onboarding-your-ai-peer-programmer-setting-up-github-copilot-coding-agent-for-success/) (GitHub Blog, 2025-07-31)
- [docs.github.com/en/copilot/get-started/best-practices](https://docs.github.com/en/copilot/get-started/best-practices)

**Confidence:** 📄 vendor-documented

---

## Practice 2: Add folder-specific instruction files for different parts of your project

**Do:** If your project has separate folders for different languages or tools — for example, a `src/components/` folder with TypeScript files — you can create extra instruction files that only apply to those folders.

Create a file inside `.github/instructions/` with a name ending in `.instructions.md`, for example `.github/instructions/react-components.instructions.md`. At the very top of that file, add a YAML frontmatter block — a small header between two lines of three dashes — that tells Copilot which files it applies to:

```yaml
---
applyTo: "src/components/**/*.ts,src/components/**/*.tsx"
---
```

The `**` is a glob pattern — a wildcard that means "match any folder at any depth." The `*.ts` part means "any file ending in .ts."

Then turn the feature on in VS Code: open your settings (File > Preferences > Settings, or press Ctrl+, on Windows/Linux), search for `useInstructionFiles`, and enable `github.copilot.chat.codeGeneration.useInstructionFiles`. You can also add this line to your `.vscode/settings.json` file:

```json
{"github.copilot.chat.codeGeneration.useInstructionFiles": true}
```

**Why (beginner):** The global `.github/copilot-instructions.md` sets the rules for your whole project. These per-folder files let you give Copilot extra rules that only apply in one part of your codebase — without cluttering the main file.

**Caveat:** This feature was introduced in July 2025. 🕒 verify live.

**Sources:**
- [github.blog/ai-and-ml/github-copilot/unlocking-the-full-power-of-copilot-code-review-master-your-instructions-files/](https://github.blog/ai-and-ml/github-copilot/unlocking-the-full-power-of-copilot-code-review-master-your-instructions-files/)
- [smartscope.blog/en/generative-ai/github-copilot/github-copilot-custom-instructions-guide/](https://smartscope.blog/en/generative-ai/github-copilot/github-copilot-custom-instructions-guide/)

**Confidence:** ✅ independently-corroborated

---

## Practice 3: In Copilot Chat, give it context about your project with @workspace or #file

**Do:** When you ask Copilot a question in the Chat panel (the sidebar with the Copilot logo), start your message with `@workspace` to let Copilot search across all your project files for context. If you want to focus on one specific file, type `#file:` followed by the path — for example `#file:src/auth/login.ts`.

Always start a fresh thread for each new task. In the Chat panel, click the `+` button (top of the panel) to open a new conversation. This clears out the old context — the window of recent messages and code that Copilot remembers — so old tasks do not confuse the new one.

**Why (beginner):** Copilot only "sees" what is in its context window — a limited amount of text it can hold in mind at once. Without `@workspace` or `#file`, it is answering based only on what you typed, not your actual code. Giving it the right context is the single biggest thing you can do to improve answer quality.

**What goes wrong without it:** Copilot invents function names, imports, and variable names that do not exist in your project. You paste the code in and get errors immediately.

**Sources:**
- [docs.github.com/en/copilot/concepts/prompting/prompt-engineering](https://docs.github.com/en/copilot/concepts/prompting/prompt-engineering)
- [docs.github.com/copilot/get-started/getting-started-with-prompts-for-copilot-chat](https://docs.github.com/copilot/get-started/getting-started-with-prompts-for-copilot-chat)
- Versent Tech Blog — "The Secret Weapon for Better GitHub Copilot Results: Context" (medium.com/versent-tech-blog, 2025-10-29; panel-confirmed 200 on 2026-06-30; Medium returns 403 to headless requests — link removed per link-check policy)

**Confidence:** ✅ independently-corroborated

---

## Practice 4: Guide inline completions with a specific comment above your cursor

**Do:** Before you start typing a new function, write a comment directly above where your cursor is sitting. Be specific. For example:

```
// Validate username and password against the users table; return a JWT token if valid; throw AuthenticationException if credentials are wrong.
```

The inline completion — the grey text that appears as Copilot suggests your next lines — reads that comment and uses it to generate code.

**Important caveat:** Inline completions do NOT read your `.github/copilot-instructions.md` file. That file only applies to Chat and Agent mode. So for completions, this comment is the only instruction Copilot gets.

**Why (beginner):** A vague comment like `// login function` produces a vague, generic result. A specific comment produces code that matches exactly what you need — fewer edits, fewer bugs.

**What goes wrong without it:** Copilot fills in code that is technically valid but does the wrong thing — a very common source of bugs that are hard to spot because the code looks fine at first glance. This is sometimes called hallucination — when an AI produces plausible-sounding output that is actually wrong.

**Sources:**
- [docs.github.com/en/copilot/concepts/completions/code-suggestions](https://docs.github.com/en/copilot/concepts/completions/code-suggestions)
- Wipro Tech Blogs — "Mastering GitHub Copilot: Best Practices" (wiprotechblogs.medium.com, 2026-03-11; panel-confirmed 200; Medium 403 to headless — link removed per link-check policy)
- [smartscope.blog/en/generative-ai/github-copilot/github-copilot-custom-instructions-guide/](https://smartscope.blog/en/generative-ai/github-copilot/github-copilot-custom-instructions-guide/)

**Confidence:** ✅ independently-corroborated

---

## Practice 5: Keep your personal Copilot instructions short — 2 to 3 rules only

**Do:** In VS Code, you can set personal preferences that apply to every project you open, not just one repo. Keep those personal preferences to 2 or 3 high-impact rules. Do not copy rules from your `.github/copilot-instructions.md` into your personal settings — that causes duplication and confusion.

To find personal instructions in VS Code: open Settings (Ctrl+,), search for "custom instructions," and look for the Copilot user-level instructions field.

**Why (beginner):** More rules do not mean better results. A long list dilutes Copilot's attention. Two clear, important rules work better than ten vague ones.

**Sources:**
- [dev.to/anchildress1/all-ive-learned-about-github-copilot-instructions-so-far-5bm7](https://dev.to/anchildress1/all-ive-learned-about-github-copilot-instructions-so-far-5bm7)

**Confidence:** thin

---

## ⚠️ Practice 6 — DANGER: The Copilot Coding Agent Works Completely on Its Own

> ⚠️ **READ THIS BEFORE YOU USE AGENT MODE OR ASSIGN A GITHUB ISSUE TO COPILOT.**

**What the coding agent is:** GitHub's Copilot coding agent is a feature where you assign a GitHub Issue — a task description on your project's issue tracker — to Copilot, and it then works entirely on its own with no input from you. It can execute terminal commands, write files, and push commits (saved changes) to your branch, all without asking you. It keeps going until it opens a pull request — a request for a human reviewer to look at and approve the changes.

**Do:** When you first try the coding agent, use it only for small, isolated tasks: fixing a single bug, adding tests for one function, or updating documentation. These are low-risk. If it goes wrong, the damage is limited and easy to reverse.

Review every pull request the agent opens before you click Merge. Read what it actually did — do not just assume it followed your instructions.

Do NOT assign the coding agent to tasks that touch security, authentication, payment processing, or anything that runs in production.

⚠️ **WARNING — Disabling the firewall that limits what the agent can access online is a dangerous default. It exposes your environment to data exfiltration** — meaning the agent could send your code or credentials to an outside server. Do not disable the firewall unless you fully understand the consequences.

**Why (beginner):** Most beginners imagine the agent will pause and ask for permission when it is unsure. It does not. It keeps going. By the time you notice something is wrong, it may have already committed broken code or run a destructive command.

**Sources:**
- [docs.github.com/copilot/how-tos/agents/copilot-coding-agent/best-practices-for-using-copilot-to-work-on-tasks](https://docs.github.com/copilot/how-tos/agents/copilot-coding-agent/best-practices-for-using-copilot-to-work-on-tasks)
- [github.blog/ai-and-ml/github-copilot/onboarding-your-ai-peer-programmer-setting-up-github-copilot-coding-agent-for-success/](https://github.blog/ai-and-ml/github-copilot/onboarding-your-ai-peer-programmer-setting-up-github-copilot-coding-agent-for-success/)

**Confidence:** 📄 vendor-documented

---

## Practice 7: Create a setup file so the coding agent can install your dependencies

**Do:** If you use the coding agent (see Practice 6), create a file at `.github/workflows/copilot-setup-steps.yml`. Inside it, define a job named exactly `copilot-setup-steps`. This file — written in YAML, a plain-text format for configuration — tells the agent how to prepare your project's environment before it starts working: installing libraries, setting environment variables, and so on.

**Caveat:** 🕒 verify live — the agent's network configuration changed in February 2026. Check the current firewall settings at [docs.github.com/copilot/customizing-copilot/customizing-or-disabling-the-firewall-for-copilot-coding-agent](https://docs.github.com/copilot/customizing-copilot/customizing-or-disabling-the-firewall-for-copilot-coding-agent) before you set this up.

**Why (beginner):** Without this file the agent may fail immediately because it cannot find the libraries your project needs. A few lines of setup prevents wasted agent runs — and wasted AI Credits (see Practice 9).

**Sources:**
- [github.blog/ai-and-ml/github-copilot/onboarding-your-ai-peer-programmer-setting-up-github-copilot-coding-agent-for-success/](https://github.blog/ai-and-ml/github-copilot/onboarding-your-ai-peer-programmer-setting-up-github-copilot-coding-agent-for-success/)
- [docs.github.com/copilot/customizing-copilot/customizing-or-disabling-the-firewall-for-copilot-coding-agent](https://docs.github.com/copilot/customizing-copilot/customizing-or-disabling-the-firewall-for-copilot-coding-agent)

**Confidence:** 📄 vendor-documented

---

## ⚠️ Practice 8 — DANGER: Read Every Line Copilot Suggests. Never Commit a Secret.

> ⚠️ **This is the most common way beginners get burned. Take it seriously.**

**Do:** Before you accept any Copilot suggestion and commit it to your project, read every line it produced. Look for three specific problems:

1. **Hardcoded secrets** — an API key, password, database connection string, or token written directly into the code. Example of what NOT to let through: `password = "mySecretPassword123"`. If Copilot writes something like this, delete it and use an environment variable instead.

2. **SQL injection** — SQL injection is an attack where a malicious user types database commands into a form field, and your code passes those commands straight to the database, letting the attacker read or delete your data. Copilot sometimes writes database queries that are vulnerable to this. Look for code that builds a query by pasting user input directly into a string.

3. **Logic flaws** — code that compiles and runs but does the wrong thing. Read the logic, do not just run it and assume it works.

**Specific security warning — CVE-2025-53773:** A CVE (Common Vulnerabilities and Exposures) is a public record of a known security bug with an official ID number. CVE-2025-53773 showed that malicious text inside a GitHub Issue could trick Copilot — through a technique called prompt injection (where hidden instructions in data hijack what an AI does) — into automatically approving terminal commands without asking you first. This led to remote code execution, meaning an attacker could run commands on your machine. This bug was patched in August 2025. Keep your Copilot VS Code extension updated to the latest version. To check: in VS Code, open the Extensions panel (Ctrl+Shift+X), search for "GitHub Copilot," and make sure it shows "Up to date."

⚠️ **NEVER commit API keys, passwords, or tokens in your code.** Once a secret is committed to a git repository, it is in the history forever — even if you delete the line later. Anyone with access to the repo can find it.

**Sources:**
- [docs.github.com/en/copilot/get-started/best-practices](https://docs.github.com/en/copilot/get-started/best-practices)
- [prompt.security/blog/securing-enterprise-data-in-the-face-of-github-copilot-vulnerabilities](https://prompt.security/blog/securing-enterprise-data-in-the-face-of-github-copilot-vulnerabilities)
- [embracethered.com/blog/posts/2025/github-copilot-remote-code-execution-via-prompt-injection/](https://embracethered.com/blog/posts/2025/github-copilot-remote-code-execution-via-prompt-injection/)

**Confidence:** ✅ independently-corroborated

---

## ⚠️ Practice 9 — DANGER: In Agent Mode, Read Every Terminal Command. Never Click "Allow All."

> ⚠️ **Agent mode can spend real money and run destructive commands. This warning protects your wallet and your machine.**

**What agent mode is:** In VS Code's Copilot Chat panel, you can switch from "Chat" to "Agent" mode using the dropdown at the bottom of the chat input box. In agent mode, Copilot does not just answer questions — it takes actions: running terminal commands (text commands that control your computer directly), editing files, and making changes across your project.

**Do:** Each time Copilot wants to run a terminal command, VS Code shows you an approval dialog — a popup listing the exact command. Read it. If the command does something you do not recognize or did not expect, click Deny and ask Copilot to explain what it is about to do.

⚠️ **WARNING — Do NOT click "Allow All" or enable any checkbox that stops VS Code from asking you about terminal commands.** If you do, you are giving Copilot permission to run any command, without showing you first. A mistaken or malicious command could delete files, install software, or send data off your machine.

**Billing warning — AI Credits:**

⚠️ **WARNING — Agent mode consumes GitHub AI Credits.** AI Credits are GitHub's billing unit for Copilot usage, introduced on 2026-06-01. They are real money. The current monthly allotments by plan are:

| Plan | Price | Monthly AI Credits |
|---|---|---|
| Free | $0 | Limited |
| Pro | $10/month | 1,500 credits |
| Pro+ | $39/month | 7,000 credits |
| Max | $100/month | 20,000 credits |

Agent mode uses credits much faster than regular Chat. A single agent run on a complex task can consume a significant portion of your monthly allotment.

🕒 Verify live — these numbers change: [docs.github.com/en/copilot/get-started/plans](https://docs.github.com/en/copilot/get-started/plans)

**What goes wrong without this practice:** You enable "Allow All" once to save time, forget about it, and Copilot later runs a destructive command in the background. Or you run agent mode heavily for a week and receive an unexpected bill.

**Sources:**
- [code.visualstudio.com/blogs/2025/02/24/introducing-copilot-agent-mode](https://code.visualstudio.com/blogs/2025/02/24/introducing-copilot-agent-mode)
- [learn.microsoft.com/en-us/visualstudio/ide/copilot-agent-mode](https://learn.microsoft.com/en-us/visualstudio/ide/copilot-agent-mode)
- [github.blog/changelog/2026-06-01-updates-to-github-copilot-billing-and-plans/](https://github.blog/changelog/2026-06-01-updates-to-github-copilot-billing-and-plans/)
- [github.blog/news-insights/company-news/github-copilot-individual-plans-introducing-flex-allotments-in-pro-and-pro-and-a-new-max-plan/](https://github.blog/news-insights/company-news/github-copilot-individual-plans-introducing-flex-allotments-in-pro-and-pro-and-a-new-max-plan/)

**Confidence:** 📄 vendor-documented

---

## Practice 10: Break complex Chat requests into steps — do not ask for everything at once

**Do:** For any task that involves more than one or two files, or more than one logical change, do it in stages:

1. First, ask Copilot to outline its approach: "Describe the steps you would take to implement X — do not write any code yet."
2. Read the outline. If something looks wrong, correct it now, before any code is written.
3. Then ask Copilot to implement one step at a time: "Now implement step 1 only."
4. Review that step, then move on to step 2.

Open a new thread (click the `+` button at the top of the Chat panel) for each separate task. This clears the context window — the working memory Copilot uses — so older conversations do not bleed into and confuse new ones.

**Why (beginner):** When you ask for everything at once, Copilot makes assumptions to fill gaps, and those assumptions compound. By the time it finishes, the result may look complete but contain several hidden mistakes. Reviewing one step at a time keeps mistakes small and catchable.

**Sources:**
- [docs.github.com/en/copilot/concepts/prompting/prompt-engineering](https://docs.github.com/en/copilot/concepts/prompting/prompt-engineering)
- Wipro Tech Blogs — "Mastering GitHub Copilot: Best Practices" (medium, 2026-03-11; link removed — see P4 note)
- Versent Tech Blog — "The Secret Weapon for Better GitHub Copilot Results: Context" (medium, 2025-10-29; link removed — see P3 note)

**Confidence:** ✅ independently-corroborated

---

## Pending fixes

- P5 — 2–3 rule limit: single independent source only. ⚠ PENDING
- P8 — 29% statistic: primary study not directly fetched. ⚠ PENDING

---

## CHANGELOG

1. Research 2026-06-30; grading 2026-06-30.
2. P1: length threshold corrected ("2 pages" not "1,000 lines").
3. P8: CVE fixed (embracethered.com source; RCE via auto-approval, not secrets exfiltration).
4. P9: Quota warning rewritten for AI Credits billing model (effective 2026-06-01).
5. P9: Copilot Max plan added ($100/mo, 20,000 credits).
6. P6: quote softened to paraphrase.
7. Publish-time: 2 Medium URLs unlinked (403 bot-detection; panel-confirmed 200 on 2026-06-30).
8. 2026-07-01: Re-leveled from the 2026-07-01 technical entry for beginner audience (track: beginner, audience: "people new to AI"); all facts unchanged; jargon defined inline; warnings for P6, P8, P9 made more prominent; UI guidance added; intro paragraph added; no new facts or URLs introduced.
