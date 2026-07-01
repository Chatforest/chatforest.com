# Prompt Engineering for Claude Code — Beginner Guide (as of 01 Jul 2026)

> Plain-language, safety-first guide for using Claude Code effectively when you are brand new to AI coding tools. Same verified facts as the technical entry, re-written for first-timers.


<!-- Beginner re-level of the 2026-07-01 technical snapshot. Same dated facts, same URLs, same
     warnings — re-written for readers who just installed Claude Code for the first time.
     No new facts or URLs introduced. -->

# Prompt Engineering for Claude Code — Beginner Guide (as of 01 Jul 2026)

> **Grading note.** A dated snapshot — accurate as of **01 Jul 2026**, frozen here as a permanent
> archive entry. Re-leveled from the 2026-07-01 technical entry; facts and sources are unchanged.
> 0 fabrications. 7 corrections from the technical grading session applied. 3 items remain
> ⚠ PENDING — never guessed.

## What is Claude Code, and why do these practices matter?

Claude Code is an AI coding assistant made by Anthropic. You type instructions (called "prompts") into a terminal, and it reads your files, writes code, and runs commands on your behalf. Because it can actually change files and run shell commands on your machine, small mistakes in how you use it can cause real damage — deleted files, leaked passwords, broken builds. The practices below exist to help you get good results while staying safe.

If any term below is unfamiliar, it is explained the first time it appears.

---

## How to read the labels

- ✅ **independently-corroborated** — confirmed by 2 or more independent publishers
- 📄 **vendor-documented** — official Anthropic docs only
- ⚠️ **WARNING** — a default that can cost money, break your machine, or remove a safety net
- 🕒 **verify live** — this detail changes fast; check the current docs before relying on it

---

## Safety first: read Practice 9 before anything else

Before you try any of these practices, read **Practice 9** below. It describes a flag that can wipe your entire home directory if used carelessly. This is not a theoretical risk — it has happened to real users. The safe everyday alternative takes ten seconds to set up.

---

## Practice 1: Write a short, specific CLAUDE.md — and keep it under 200 lines

**What is CLAUDE.md?** It is a plain text file you place in the top folder of your project. Claude Code reads it automatically at the start of every session. Think of it as a sticky note you leave for Claude explaining the rules of your specific project.

**Do:** Create a `CLAUDE.md` file at the top of your project folder. You can also let Claude Code create a starter version for you by typing `/init` in the Claude Code chat prompt. In this file, include only things Claude cannot figure out by reading your code: exact commands to build, test, or lint your project; naming rules you use; and any gotchas or quirks specific to your setup. Keep it under 200 lines. For every line, ask yourself: "If I removed this, would Claude make a mistake?" If the answer is no, cut the line.

**Why this matters for beginners:** CLAUDE.md is loaded into Claude's "context window" — think of this as Claude's short-term working memory, the text it can see all at once while helping you. The longer and more cluttered this file is, the more likely Claude is to miss the important parts. Research shows accuracy can drop more than 30% when key instructions are buried in wordy content.

**What to include vs. what to leave out:**

| Put this in | Leave this out |
|---|---|
| Exact commands: `npm test`, `make lint` | Anything Claude can figure out from reading your code |
| Style rules that differ from normal defaults | Standard language rules Claude already knows |
| The 3-5 folders that really matter | File-by-file descriptions of your whole codebase |
| Branch naming, pull-request rules | Full API documentation (link to it instead) |
| Non-obvious environment quirks, required passwords/keys | Long explanations or tutorials |
| Unusual behaviors or common traps | Obvious advice like "write clean code" |

**Caveat:** The 200-line limit is a rule of thumb, not a hard system limit. Some sources suggest 60 lines is better for complex projects. You can split rules into separate files under a `.claude/rules/` folder, but those files are still loaded at startup and still use up tokens (tokens are the units of text the AI processes — more tokens means more cost and potentially slower or less accurate responses). Splitting into multiple files does not reduce how much Claude has to read.

**Sources:**
- [code.claude.com/docs/en/best-practices](https://code.claude.com/docs/en/best-practices)
- [code.claude.com/docs/en/memory](https://code.claude.com/docs/en/memory)
- [maketocreate.com/claude-md-best-practices-the-complete-2026-guide/](https://maketocreate.com/claude-md-best-practices-the-complete-2026-guide/)
- [github.com/shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice)

**Confidence:** ✅ independently-corroborated

---

## Practice 2: Ask Claude to make a plan before it writes code

**Do:** Any time a change will touch more than one file, ask Claude to plan first before writing any code. After Claude shows you a plan, press `Ctrl+G` to open the plan in your text editor so you can read and edit it. Only then let Claude start writing code.

**Why this matters for beginners:** Without a planning step, Claude can confidently solve the wrong problem — and you might not notice until it has changed a dozen files. Catching a misunderstanding before any code is written costs nothing. Catching it after costs time and context.

For a tiny single-file fix (correcting a typo, changing one variable name), you can skip the plan — the extra step is not worth it for something that simple.

**Caveat:** Planning adds a round-trip: Claude writes a plan, you read it, then Claude writes code. This is overhead for trivial changes. 🕒 **verify live** — the way you switch between modes has expanded; `Shift+Tab` now cycles through multiple modes. Check [code.claude.com/docs/en/permission-modes](https://code.claude.com/docs/en/permission-modes) for the current options.

**Sources:**
- [code.claude.com/docs/en/best-practices](https://code.claude.com/docs/en/best-practices)
- [community.sap.com/t5/artificial-intelligence-blogs-posts/claude-code-best-practices-for-developers/ba-p/14394164](https://community.sap.com/t5/artificial-intelligence-blogs-posts/claude-code-best-practices-for-developers/ba-p/14394164)
- [code.claude.com/docs/en/permission-modes](https://code.claude.com/docs/en/permission-modes)

**Confidence:** ✅ independently-corroborated

---

## Practice 3: Always give Claude a way to check its own work

**Do:** Every time you give Claude a task, also tell it how to check whether the task is done correctly. That could be a test command (e.g., `npm test`), a build command that exits with an error if something is broken, or a linter check. Tell Claude to run the check and keep trying until it passes — do not accept "I think this should work" as an answer.

**Why this matters for beginners:** If you do not give Claude a way to verify its work, you become the check. You have to read the code, run the tests yourself, and spot the mistakes. A failing test reported back in the conversation closes that loop for you automatically. You can walk away from a session and come back to confirmed results instead of surprises.

**Sources:**
- [code.claude.com/docs/en/best-practices](https://code.claude.com/docs/en/best-practices)
- [community.sap.com/t5/artificial-intelligence-blogs-posts/claude-code-best-practices-for-developers/ba-p/14394164](https://community.sap.com/t5/artificial-intelligence-blogs-posts/claude-code-best-practices-for-developers/ba-p/14394164)

**Confidence:** ✅ independently-corroborated

---

## Practice 4: Clear Claude's memory between unrelated tasks

**What is a context window?** Claude's context window is its short-term working memory — the full text of your conversation plus every file it has read, all held in memory at once. As this fills up, Claude starts making more mistakes: it may ignore earlier instructions or forget what it just read.

**Do:**
- Type `/clear` in the Claude Code chat prompt to wipe the context window completely and start fresh. Use this when switching to a completely different task.
- Type `/compact <brief note>` when you want to continue the same topic but trim the conversation. For example: `/compact Focus on the API changes, drop the test debugging thread`. This compresses the history while keeping important context.
- If you have corrected Claude twice on the same mistake and it keeps repeating it, stop. Type `/clear` and rewrite a cleaner prompt that avoids whatever caused the confusion.

**Why this matters for beginners:** More conversation history is not always better. Research shows quality can start dropping as early as when the context window is 40% full. The "correct twice then clear" rule is documented in Anthropic's own best-practices guide — follow it.

**Caveat:** 🕒 **verify live** — the 40% figure comes from independent third-party testing, not an official Anthropic specification, and may change with model updates. The general principle (fuller context window leads to worse results) is confirmed by multiple independent sources.

**Sources:**
- [code.claude.com/docs/en/best-practices](https://code.claude.com/docs/en/best-practices)
- [claudefa.st/blog/guide/mechanics/context-management](https://claudefa.st/blog/guide/mechanics/context-management)
- [avilevi.co.il/en/blog/manage-claude-code-context-window/](https://www.avilevi.co.il/en/blog/manage-claude-code-context-window/)
- [github.com/shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice)

**Confidence:** ✅ independently-corroborated

---

## Practice 5: Use subagents to explore large codebases — but always list their permissions

**What is a subagent?** A subagent is a separate AI instance that Claude can launch to do a specific job and report back. It works in its own context window, so its reading and exploring does not fill up your main conversation.

**Do:** When Claude needs to look through many files to answer a question, prompt it like this: `"Use subagents to investigate how our auth system handles token refresh."` The subagent reads the files, then returns a summary to your main conversation. You can also use a subagent for a second-opinion review: `"Use a subagent to review this diff for edge cases."` A fresh instance that did not write the code will catch things the original pass missed.

**Why this matters for beginners:** Every file Claude reads uses up tokens in your context window. Subagents do their reading in a separate context window, so your main session stays clean and can run longer without quality dropping.

**⚠️ WARNING:** If you define a custom subagent by creating a file at `.claude/agents/<name>.md` and you leave out the `tools:` field, that subagent silently gets access to every tool Claude has — including the ability to write files and run shell commands. Always list the tools you want the subagent to have. Multiple independent sources identify "permission sprawl" (giving subagents more power than they need) as the most common subagent mistake.

**Sources:**
- [code.claude.com/docs/en/best-practices](https://code.claude.com/docs/en/best-practices)
- [pubnub.com/blog/best-practices-for-claude-code-sub-agents/](https://www.pubnub.com/blog/best-practices-for-claude-code-sub-agents/)
- [smartscope.blog/en/generative-ai/claude/claude-code-best-practices-advanced-2026/](https://smartscope.blog/en/generative-ai/claude/claude-code-best-practices-advanced-2026/)

**Confidence:** ✅ independently-corroborated

---

## Practice 6: Write specific prompts — name the exact file and what you want

**Do:** Be precise. Instead of "add tests for foo.py," write "write a test for `foo.py` covering the case where the user is logged out — avoid mocks." Instead of "fix the login bug," write "users report login fails after session timeout; check the auth flow in `src/auth/`, especially token refresh — write a failing test that reproduces the issue, then fix it."

Type `@filename` (for example, `@src/auth/login.py`) in your prompt to hand Claude a specific file directly, rather than describing where the file lives.

**Why this matters for beginners:** Claude can guess at what you mean, but it cannot read your mind. Vague prompts produce plausible-looking but wrong results. Fixing a wrong result takes more back-and-forth, which fills the context window faster and costs more. Specific prompts get you the right answer sooner.

**Caveat:** Vague prompts are useful when you are exploring and genuinely do not know what you want. "What would you improve in this file?" is a fine prompt when you are curious. The caution here is about prompts that sound specific but leave out the details Claude actually needs.

**Sources:**
- [code.claude.com/docs/en/best-practices](https://code.claude.com/docs/en/best-practices)
- [claude.com/blog/best-practices-for-prompt-engineering](https://claude.com/blog/best-practices-for-prompt-engineering)
- [maketocreate.com/claude-md-best-practices-the-complete-2026-guide/](https://maketocreate.com/claude-md-best-practices-the-complete-2026-guide/)

**Confidence:** ✅ independently-corroborated

---

## Practice 7: Use hooks for rules that must always run — not CLAUDE.md

**What is a hook?** A hook is a small shell script (a short list of commands for the terminal) that Claude Code runs automatically at a specific moment — for example, immediately after it edits any file. Hooks are configured in `.claude/settings.json`.

**What is a linter?** A linter is a tool that reads your code and flags style errors or potential bugs without running the program. For example, `eslint` checks JavaScript.

**Do:** If a rule absolutely must happen every single time without exception — such as running a linter after every file edit, or blocking writes to a protected folder — implement it as a hook, not as a line in CLAUDE.md. You can ask Claude to write the hook for you: `"Write a hook that runs eslint after every file edit."`

**Why this matters for beginners:** Instructions in CLAUDE.md are suggestions Claude tries to follow — but there is no guarantee. Claude might skip an instruction if it seems irrelevant in context, or if the context window is crowded. Hooks are not suggestions. They are shell commands that run at fixed moments regardless of what Claude decided to do. They are guaranteed; CLAUDE.md is not.

**Caveat:** Hooks run with the same permissions as your user account. A badly written hook can cause damage just like any other shell command. Start with simple, safe hooks — ones that only read or notify — before you write hooks that block actions or modify files.

**Sources:**
- [code.claude.com/docs/en/hooks-guide](https://code.claude.com/docs/en/hooks-guide)
- [code.claude.com/docs/en/memory](https://code.claude.com/docs/en/memory)
- [smartscope.blog/en/generative-ai/claude/claude-code-best-practices-advanced-2026/](https://smartscope.blog/en/generative-ai/claude/claude-code-best-practices-advanced-2026/)

**Confidence:** ✅ independently-corroborated

---

## Practice 8: For big features, have Claude interview you first — then write a spec

**Do:** For any feature that is large, unclear, or spans many files, do not start by asking Claude to write code. Instead, paste this prompt (filling in your own description):

```
I want to build [brief description]. Interview me in detail using the AskUserQuestion tool.

Ask about technical implementation, UI/UX, edge cases, concerns, and tradeoffs. Don't ask obvious questions, dig into the hard parts I might not have considered.

Keep interviewing until we've covered everything, then write a complete spec to SPEC.md.
```

A "spec" (short for specification) is a written description of exactly what to build and how — decisions made, edge cases handled, nothing left ambiguous. After Claude writes `SPEC.md`, start a **fresh session** (use `/clear`) to do the actual implementation.

**Why this matters for beginners:** Claude will ask about things you did not think of — edge cases, conflicting requirements, UI decisions that seem small but matter later. Writing a spec before coding catches those gaps when they are cheap to fix. Starting the implementation in a fresh session means the context is not cluttered with the entire brainstorming conversation.

**Caveat:** This adds time upfront. It is most valuable for features with unclear requirements or that touch many files. Skip it for small, unambiguous changes.

**Sources:**
- [code.claude.com/docs/en/best-practices](https://code.claude.com/docs/en/best-practices)
- [community.sap.com/t5/artificial-intelligence-blogs-posts/claude-code-best-practices-for-developers/ba-p/14394164](https://community.sap.com/t5/artificial-intelligence-blogs-posts/claude-code-best-practices-for-developers/ba-p/14394164)

**Confidence:** ✅ independently-corroborated

---

## ⚠️ Practice 9: NEVER use `--dangerously-skip-permissions` on your real machine

**Read this before you try anything else.**

**Do:** Do not use the `--dangerously-skip-permissions` flag (which is the same as `--permission-mode bypassPermissions`) on your real machine, or in any folder containing files you cannot afford to lose.

For everyday coding, use `--permission-mode acceptEdits` instead. This mode automatically approves file edits and common file-system commands, so Claude does not ask permission for every small change — but it does not remove all safety checks the way `--dangerously-skip-permissions` does.

If you believe you need `--dangerously-skip-permissions`, Anthropic's own engineers say: run it inside a container (an isolated virtual environment, like Docker) — not on your actual machine.

**⚠️ WARNING — real risk of permanent data loss.** This flag removes every confirmation prompt. Documented real incidents from 2025 show Claude executing `rm -rf ~/` — a shell command that permanently deletes your entire home directory, including all your documents, code, and settings — in sessions that did not even use this flag. With the flag enabled, there is no pause and no chance to stop a bad command before it fires. There is no undo.

**The six permission modes — what they do:**

| Mode | What it does |
|------|-------------|
| `default` | Read-only; asks before making any changes |
| `acceptEdits` | Reads files and makes edits; auto-approves common filesystem commands |
| `plan` | Read-only; no edits at all (safe for analysis) |
| `auto` | All actions, with per-action safety checks (research preview — not available to all users) |
| `dontAsk` | Only pre-approved tools (for automated pipelines) |
| `bypassPermissions` | Everything, no checks — same as `--dangerously-skip-permissions` |

**For most beginners, `acceptEdits` is the right choice.** It lets Claude work efficiently without disabling safety.

**Caveat:** `auto` mode is a research preview as of June 2026. It requires Claude Code v2.1.83 or later and may not be available to all users. 🕒 **verify live** — the permission mode list is expanding; check [code.claude.com/docs/en/permission-modes](https://code.claude.com/docs/en/permission-modes) for current options and eligibility.

**Sources:**
- [truefoundry.com/blog/claude-code-dangerously-skip-permissions](https://www.truefoundry.com/blog/claude-code-dangerously-skip-permissions)
- [ksred.com/claude-code-dangerously-skip-permissions-when-to-use-it-and-when-you-absolutely-shouldnt/](https://www.ksred.com/claude-code-dangerously-skip-permissions-when-to-use-it-and-when-you-absolutely-shouldnt/)
- [code.claude.com/docs/en/permission-modes](https://code.claude.com/docs/en/permission-modes)
- [claude.com/blog/auto-mode](https://claude.com/blog/auto-mode)

**Confidence:** ✅ independently-corroborated

---

## Practice 10: Split project rules into separate files so Claude only loads what it needs

**What is YAML frontmatter?** It is the block of settings at the very top of a text file, between two lines of `---` dashes. It tells Claude Code how to use that file. The spacing and dashes matter — copy the format exactly.

**What is a glob pattern?** It is a wildcard rule for matching file paths. For example, `*.ts` means "any file ending in `.ts`" and `src/api/**/*.ts` means "any `.ts` file anywhere inside `src/api/`."

**Do:** Instead of putting every rule in one long CLAUDE.md, split rules for different areas of your project into separate files under a `.claude/rules/` folder. Add a YAML frontmatter block at the top of each file with a `paths:` key, so the rules only load when Claude is working with files that match those paths.

Example rules file at `.claude/rules/api-rules.md`:

```markdown
---
paths:
  - "src/api/**/*.ts"
---

# API Development Rules
- All API endpoints must include input validation
- Use the standard error response format
```

**Why this matters for beginners:** Every line of CLAUDE.md is loaded at the start of every session, even if you are only editing the front-end and the API rules are completely irrelevant. Path-scoped rules files only load when Claude reads a file matching the pattern. This keeps your startup context short, which helps Claude focus on what matters for the current task.

**Caveat:** A rules file without a `paths:` frontmatter block loads at startup just like CLAUDE.md — the selective loading only happens when the `paths:` key is present. Also, files you import into CLAUDE.md using `@path` always load at startup regardless of any path rules. 🕒 **verify live** — this feature is relatively new; check the current Claude Code docs for any changes to the file format.

**Sources:**
- [code.claude.com/docs/en/memory](https://code.claude.com/docs/en/memory)
- [maketocreate.com/claude-md-best-practices-the-complete-2026-guide/](https://maketocreate.com/claude-md-best-practices-the-complete-2026-guide/)
- [avilevi.co.il/en/blog/manage-claude-code-context-window/](https://www.avilevi.co.il/en/blog/manage-claude-code-context-window/)

**Confidence:** ✅ independently-corroborated

---

## Pending fixes

- **P4 — specific token-count degradation thresholds:** The 40% utilization threshold is confirmed from an independent source. An earlier draft cited specific token-count numbers (147k-152k) that could not be verified in the cited source and were removed. ⚠ PENDING: a sourced measurement benchmark.
- **P9 — auto mode research preview status:** The "research preview" status and eligibility requirements are confirmed from Anthropic's permission-modes page but may change with each Claude Code update. ⚠ PENDING: verify live after each update.

---

## CHANGELOG

1. **Research 2026-06-30:** Initial technical research pass. 10 practices drafted from 9 fetched sources.
2. **Grading 2026-06-30 — Skeptic KILL (P4):** "147,000-152,000 token degradation" figures not found in cited source. Removed.
3. **Grading 2026-06-30 — Skeptic KILL (P9):** "32% of developers experienced unintended file modification; 9% reported data loss" statistics not found in cited source. Removed.
4. **Grading 2026-06-30 — Skeptic FIX (P4):** "Two failures = /clear" re-attributed to Anthropic best-practices docs (the correct source).
5. **Grading 2026-06-30 — Skeptic FIX (P2):** SAP "Golden Rule" quote changed to paraphrase (source wording differs from draft).
6. **Grading 2026-06-30 — Skeptic FIX (P7):** SmartScope hooks guidance changed to paraphrase (source wording differs from draft).
7. **Grading 2026-06-30 — Timekeeper FIX (P9):** Permission mode description expanded to full six-mode table; `acceptEdits` added as everyday practical alternative.
8. **Grading 2026-06-30 — Timekeeper FLAG resolved (P9):** Official Anthropic auto mode URL added: [claude.com/blog/auto-mode](https://claude.com/blog/auto-mode).
9. **Grading 2026-06-30 — Timekeeper FIX (P2):** Verify-live caveat added for plan mode expansion (Shift+Tab cycle, mode choice after plan approval).
10. **2026-07-01 — Beginner re-level:** Re-written for readers brand new to AI and Claude Code. All jargon defined inline on first use (context window, tokens, linter, hook, subagent, YAML frontmatter, glob pattern, spec). Safety warning (Practice 9) surfaced with a call-out at the top of the document. One sensible default path per practice (alternatives briefly noted). All facts, URLs, and warnings carried over unchanged from the 2026-07-01 technical entry. No new facts or URLs introduced.

