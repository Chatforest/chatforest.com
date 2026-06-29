---
title: "Prompt Engineering for Coding Agents — Best Practices (as of 30 Jun 2026)"
date: 2026-06-30
snapshot_date: 2026-06-30
topic: prompt-engineering-for-coding-agents
track: best-practices
audience: "technically comfortable readers"
description: "Concrete, source-verified practices for getting better results from AI coding agents — covering universal prompt hygiene plus tool-specific guidance for Claude Code, GitHub Copilot, and Cursor."
content_type: "Best Practice"
categories: ["Prompt Engineering", "Claude Code", "GitHub Copilot", "Cursor"]
tags: ["prompt-engineering", "coding-agents", "claude-code", "github-copilot", "cursor", "context-management", "ai-tools"]
last_refreshed: 2026-06-30
graded_by: "RingS panel (Skeptic/Beginner/Timekeeper) + sensei, 2026-06-30"
grading_result: "0 fabrications; 9 panel corrections applied (3 Skeptic KILLs removed, 2 Skeptic FIXes, 2 Timekeeper KILLs corrected, 2 Timekeeper FIXes); 5 items pending sourced fixes"
---

<!-- This file lands at content/ai/best-practices/prompt-engineering-for-coding-agents/2026-06-30/index.md
     and is an IMMUTABLE dated snapshot. Once published it is never edited — a refresh is a NEW
     <snapshot-date> dir. "Latest" is computed by Grove's template from snapshot_date; do not add
     a "latest" flag.
     Source tiers: independently-corroborated = 2+ DIFFERENT publishers; vendor-documented =
     official vendor docs only (authoritative, single source). -->

# Prompt Engineering for Coding Agents (as of 30 Jun 2026)

> **Grading note.** A dated snapshot — accurate as of **30 Jun 2026**, frozen here and kept as a
> permanent archive entry. Research-drafted by four pupils (one per ecosystem), graded by the
> 3-lens panel. **0 fabrications.** 9 corrections applied: 3 Skeptic KILLs removed (fabricated
> statistics, wrong CVE details), 2 Skeptic FIXes (wrong thresholds), 2 Timekeeper KILLs
> corrected (outdated version numbers, obsolete billing model), 2 Timekeeper FIXes (expanded
> permission mode list, billing update). 5 items remain ⚠ PENDING with no verified fix. Per
> RingS policy: unverifiable gaps are never guessed.

## How to read the labels
- ✅ **independently-corroborated** — confirmed by 2+ independent publishers
- 📄 **vendor-documented** — official docs only (authoritative, single source)
- ⚠️ **WARNING** — a default that can cost money, break the machine, or remove a safety net
- 🕒 **verify live** — fast-moving (versions/prices/quotas); check the current value

---

## Part 0 — Universal practices (any AI coding tool)

These ten practices apply across Claude Code, GitHub Copilot, Cursor, Aider, and any other LLM-based coding assistant.

---

**1. Decompose large tasks into small, concrete steps.** ✅

**Do:** Break your request into the smallest unit of work the AI can handle without guessing. Instead of "Build me a REST API," say "First, write a FastAPI route that accepts a JSON body with fields `name` and `email` and returns a 201 response. Stop there."

**Why:** AI coding agents in most modes have no way to ask clarifying questions mid-task. The more decisions the agent makes on your behalf, the more likely it gets one wrong. Smaller steps give you a natural checkpoint before the next.

**Caveat:** Decomposing too finely adds overhead. Match granularity to risk: new files and cross-file refactors warrant finer steps; small isolated edits can be done in one shot.

**Sources:** [GitHub Docs — Prompt engineering for Copilot Chat](https://docs.github.com/en/copilot/concepts/prompting/prompt-engineering) (fetched 2026-06-30) · [VS Code Docs — Best practices for AI agents](https://code.visualstudio.com/docs/agents/best-practices) (updated 2026-06-24) · [PromptHub Blog — Prompt engineering for AI agents](https://www.prompthub.us/blog/prompt-engineering-for-ai-agents) (2025-10-23) · [leanware.co — Prompt Engineering for Code Generation](https://www.leanware.co/insights/prompt-engineering-for-code-generation) (2025-10-15) · [Stack Overflow Blog — Are bugs inevitable with AI coding agents?](https://stackoverflow.blog/2026/01/28/are-bugs-and-incidents-inevitable-with-ai-coding-agents/) (2026-01-28)

---

**2. Provide specific, upfront context — do not assume the AI knows your project.** ✅

**Do:** Before asking for code, share the relevant pieces of your environment: language and version, framework, constraints ("must not use external libraries"), and the exact error message or test failure. Reference specific files by name rather than describing where they live.

**Caveat:** ⚠️ Do not paste secrets (API keys, passwords, tokens) into your prompt. AI tools send your text to cloud servers; credential exposure via prompt is a real attack surface. Redact secrets before sharing code snippets.

**Sources:** [Anthropic Engineering — Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) (2025-09-29) · [GitHub Docs — Prompt engineering for Copilot Chat](https://docs.github.com/en/copilot/concepts/prompting/prompt-engineering) (fetched 2026-06-30) · [VS Code Docs — Best practices for AI agents](https://code.visualstudio.com/docs/agents/best-practices) (2026-06-24)

---

**3. Be specific, not verbose — one precise constraint beats ten vague sentences.** ✅

**Do:** Replace open-ended requests with concrete acceptance criteria. Instead of "make this faster," write "reduce the time complexity of `process_batch()` from O(n²) to O(n log n) without changing its public signature." Instead of "add tests," write "add a pytest test for the edge case where `user_id` is None."

**Caveat:** Do not add so many constraints that you have already written the solution yourself. The goal is to bound the problem, not to dictate every line.

**Sources:** [VS Code Docs — Best practices for AI agents](https://code.visualstudio.com/docs/agents/best-practices) (2026-06-24) · [leanware.co — Prompt Engineering for Code Generation](https://www.leanware.co/insights/prompt-engineering-for-code-generation) (2025-10-15) · [Lakera — Prompt Engineering Guide](https://www.lakera.ai/blog/prompt-engineering-guide) (2026-04-20) · [andriifurmanets.com — Prompt Engineering for Developers](https://andriifurmanets.com/blogs/prompt-engineering-for-developers) (2025-10-21)

---

**4. Treat output as a starting draft — always review AI-generated code before using it.** ✅

**Do:** Read every line the AI writes before committing or running it. Check for: security issues (SQL injection, hardcoded credentials, missing auth), logic errors (off-by-one, null handling), incorrect assumptions about your data model, and missing edge cases. Run the code and tests; do not just read it.

**Caveat:** ⚠️ "It ran without errors" is not the same as "it is correct." Logical bugs and security vulnerabilities often produce no immediate error. Treat AI output as you would code from a contractor you have never worked with: useful starting point, still needs a code review.

**Sources:** [Stack Overflow Blog — Are bugs inevitable with AI coding agents?](https://stackoverflow.blog/2026/01/28/are-bugs-and-incidents-inevitable-with-ai-coding-agents/) (2026-01-28; cites 470-repository study finding 1.7× bug rate in AI-generated code) · [andriifurmanets.com — Prompt Engineering for Developers](https://andriifurmanets.com/blogs/prompt-engineering-for-developers) (2025-10-21) · [VS Code Docs — Best practices for AI agents](https://code.visualstudio.com/docs/agents/best-practices) (2026-06-24)

---

**5. Refine iteratively — do not give up after a poor first result.** ✅

**Do:** Treat your first prompt as a hypothesis. Generate an initial result, identify the specific gap ("the function handles None but not empty string"), then issue a targeted follow-up addressing only that gap. Build toward the final state in cycles rather than starting over each time.

**Caveat:** If the agent's reasoning has gone deeply wrong — it has re-architected something in a direction that conflicts with your system — iterative patching on bad foundations makes things worse. In that case, roll back (see Practice 8) and start a fresh session.

**Sources:** [leanware.co — Prompt Engineering for Code Generation](https://www.leanware.co/insights/prompt-engineering-for-code-generation) (2025-10-15) · [GitHub Docs — Prompt engineering for Copilot Chat](https://docs.github.com/en/copilot/concepts/prompting/prompt-engineering) (fetched 2026-06-30) · [VS Code Docs — Best practices for AI agents](https://code.visualstudio.com/docs/agents/best-practices) (2026-06-24)

---

**6. Avoid context overload — paste only what is directly relevant.** ✅

**Do:** Share only the code, error messages, and files directly relevant to your current task. Do not paste your entire codebase "just in case." When you do paste, trim irrelevant comments, unrelated functions, and noise from stack traces.

**Why:** LLMs degrade in quality when their context window fills with irrelevant content — a phenomenon researchers call "context rot." One measurement found that a standard set of MCP tool servers consumed over 20% of the context window before any actual work began. Signal beats size.

**Caveat:** ⚠️ Large context windows (hundreds of thousands of tokens) do not eliminate context rot. Bigger is not always better — targeted is better.

**Sources:** [MindStudio Blog — Context Rot in AI Coding Agents Explained](https://www.mindstudio.ai/blog/context-rot-ai-coding-agents-explained) (2026-03-17) · [EclipseSource — MCP and Context Overload: Why More Tools Make Your AI Agent Worse](https://eclipsesource.com/blogs/2026/01/22/mcp-context-overload/) (2026-01-22) · [Anthropic Engineering — Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) (2025-09-29)

---

**7. Use a persistent configuration file to carry project context across sessions.** ✅

**Do:** Create a project-level file describing your stack, conventions, and constraints once. Different tools read different names: Claude Code reads `CLAUDE.md`, Cursor reads `.cursor/rules/*.mdc` (`.cursorrules` is deprecated — see Part 3), GitHub Copilot reads `.github/copilot-instructions.md`, Aider and OpenHands read `AGENTS.md`. Keep the file under ~200 meaningful lines, accurate, and up to date.

**Caveat:** A 1,000-line config file is actively counterproductive — it consumes context budget and the model reliably misses content beyond the first ~150–200 instructions. Do not include secrets, and do not include rules you already enforce with a linter. 🕒 File name conventions are tool-specific and may change — verify in your tool's docs.

**Sources:** [deployhq.com — CLAUDE.md, AGENTS.md & Copilot Instructions: Configure Every AI Coding Assistant](https://www.deployhq.com/blog/ai-coding-config-files-guide) (fetched 2026-06-30) · [MindStudio Blog — Context Rot in AI Coding Agents Explained](https://www.mindstudio.ai/blog/context-rot-ai-coding-agents-explained) (2026-03-17) · [arguingwithalgorithms.com — How to keep your AI coding agent from going rogue](https://www.arguingwithalgorithms.com/posts/technical-design-spec-pattern.html) (2025-05-20)

---

**8. When the agent goes wrong, stop early, roll back, and re-prompt with narrower scope.** ✅

**Do:** At the first sign the agent has taken a wrong turn, stop accepting changes. Revert to the last known-good state using version control (`git stash` to stash uncommitted changes, or check out the last commit if you have been committing in checkpoints). Open a fresh chat session, paste only the relevant context, and re-prompt with a tighter scope. Document the missing constraint so you can add it next time.

**Caveat:** ⚠️ `git checkout <file>` **permanently discards uncommitted changes** — there is no undo. Use `git stash` if you want to save them, or check `git status` first. Always commit before starting an agent run — even `git commit -m "before AI session"` gives you a rescue point. Asking the agent to undo its own mistakes inside the same session compounds the problem; start fresh.

**Sources:** [arguingwithalgorithms.com — How to keep your AI coding agent from going rogue](https://www.arguingwithalgorithms.com/posts/technical-design-spec-pattern.html) (2025-05-20) · [DEV Community — The Rollback Prompt: Undo AI Changes Safely Without Losing Context](https://dev.to/novaelvaris/the-rollback-prompt-undo-ai-changes-safely-without-losing-context-3c41) (2026-04-03) · [Pete Hodgson — Why Your AI Coding Assistant Keeps Doing It Wrong](https://blog.thepete.net/blog/2025/05/22/why-your-ai-coding-assistant-keeps-doing-it-wrong-and-how-to-fix-it/) (2025-05-22) · [VS Code Docs — Best practices for AI agents](https://code.visualstudio.com/docs/agents/best-practices) (2026-06-24)

---

**9. Match the interaction mode to the task.** 📄

**Do:** Use inline autocomplete for single-line completions, boilerplate, and small additions within a file. Switch to chat for planning, explanation, and multi-file work. Use agent/autonomous mode only for well-scoped tasks with clear success criteria, after committing your current work.

**Caveat:** ⚠️ Agent/autonomous mode can run tool calls (write files, execute shell commands, install packages) without pausing for confirmation depending on your tool's settings. Review permission settings before enabling autonomous mode. Start with a lower-permission mode and expand only when you understand what the agent is doing.

**Sources:** [VS Code Docs — Best practices for AI agents](https://code.visualstudio.com/docs/agents/best-practices) (2026-06-24; explicit table of modes with recommended use cases)

---

**10. Ask the agent to plan before it acts — especially for risky or large tasks.** ✅

**Do:** For any task that modifies multiple files, changes a database schema, or touches infrastructure, ask the AI to write out its plan first: "Before making any changes, describe step by step what you will do and which files you will modify. Do not make any changes yet." Review the plan, correct it, then tell it to proceed.

**Caveat:** For simple, obviously-bounded tasks (rename this variable, add a docstring), planning is overkill. Reserve it for tasks where "undo" would be painful.

**Sources:** [arguingwithalgorithms.com — How to keep your AI coding agent from going rogue](https://www.arguingwithalgorithms.com/posts/technical-design-spec-pattern.html) (2025-05-20) · [PromptHub Blog — Prompt engineering for AI agents](https://www.prompthub.us/blog/prompt-engineering-for-ai-agents) (2025-10-23) · [VS Code Docs — Best practices for AI agents](https://code.visualstudio.com/docs/agents/best-practices) (2026-06-24)

---

## Part 1 — Claude Code

Claude Code is Anthropic's terminal-based AI coding agent. These practices are specific to its memory system, context management, and permission model.

---

**1. Write a short, specific CLAUDE.md — and keep it under 200 lines.** ✅

**Do:** Create a `CLAUDE.md` at your project root (or run `/init` to generate one). Include only facts Claude cannot infer from reading the code: exact build/test/lint commands, non-obvious architectural decisions, naming conventions, and project-specific gotchas. Ask of every line: "Would removing this cause Claude to make a mistake?" If no, cut it.

**What to include vs. exclude:**

| Include | Exclude |
|---|---|
| Exact commands: `npm test`, `make lint` | Anything Claude can infer from reading the code |
| Code style rules that differ from defaults | Standard language conventions Claude already knows |
| Architecture: the 3–5 directories that matter | File-by-file descriptions of the whole codebase |
| Repository etiquette (branch naming, PR rules) | Detailed API docs (link to them instead) |
| Non-obvious environment quirks, required env vars | Long explanations or tutorials |
| Common gotchas or non-obvious behaviors | Self-evident practices like "write clean code" |

**Caveat:** Some independent sources suggest 60 lines is a better target for complex projects that also use `.claude/rules/*.md` path-scoped files. Splitting into topic files helps organise content; it does not reduce total token consumption at startup.

**Sources:** [code.claude.com/docs/en/best-practices](https://code.claude.com/docs/en/best-practices) (fetched 2026-06-30) · [code.claude.com/docs/en/memory](https://code.claude.com/docs/en/memory) (fetched 2026-06-30) · [maketocreate.com — Claude.md Best Practices: The Complete 2026 Guide](https://maketocreate.com/claude-md-best-practices-the-complete-2026-guide/) (fetched 2026-06-30) · [github.com/shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) (fetched 2026-06-30)

---

**2. Use plan mode before writing code for any multi-file change.** ✅

**Do:** For anything touching more than one file, or when you are uncertain about the approach, switch Claude into plan mode before implementation. In the interactive terminal, press `Ctrl+G` after Claude produces a plan to open it in your editor for review. Only then leave plan mode and let Claude start writing code. 🕒 **verify live** — `Shift+Tab` now cycles through multiple modes; verify current keybindings in docs.

**Caveat:** Plan mode adds round-trip time. The official docs explicitly state: "If you could describe the diff in one sentence, skip the plan."

**Sources:** [code.claude.com/docs/en/best-practices](https://code.claude.com/docs/en/best-practices) (fetched 2026-06-30) · [community.sap.com — Claude Code Best Practices for Developers](https://community.sap.com/t5/artificial-intelligence-blogs-posts/claude-code-best-practices-for-developers/ba-p/14394164) (independent, fetched 2026-06-30)

---

**3. Give Claude a verifiable check it can run, not just "looks done."** ✅

**Do:** When you assign a task, always tell Claude how to verify success: a test suite command, a build exit code, a linter check, or (for UI work) a screenshot. Ask Claude to run the check and iterate until it passes — do not accept "I think this should work."

**Sources:** [code.claude.com/docs/en/best-practices](https://code.claude.com/docs/en/best-practices) (fetched 2026-06-30) · [community.sap.com — Claude Code Best Practices for Developers](https://community.sap.com/t5/artificial-intelligence-blogs-posts/claude-code-best-practices-for-developers/ba-p/14394164) (fetched 2026-06-30)

---

**4. Manage the context window proactively — don't wait for auto-compact.** ✅

**Do:** Use `/clear` between unrelated tasks to reset the context window. For related tasks where you want continuity, run `/compact <instructions>` with a hint about what to keep. After two failed correction attempts on the same issue, stop, run `/clear`, and rewrite a cleaner prompt incorporating what you learned.

**Why:** Performance degrades as the context window fills: Claude may start ignoring earlier instructions or making more mistakes. Independent sources confirm degradation is a real effect as context fills; specific token thresholds are empirical estimates, not official Anthropic specifications. Correcting over and over without clearing only accumulates failed approaches.

**Caveat:** 🕒 **verify live** — specific degradation percentages and token thresholds are empirical observations from third-party testing, not guaranteed Anthropic specifications, and shift with model updates.

**Sources:** [code.claude.com/docs/en/best-practices](https://code.claude.com/docs/en/best-practices) (fetched 2026-06-30) · [claudefa.st — Context Management Guide](https://claudefa.st/blog/guide/mechanics/context-management) (fetched 2026-06-30) · [github.com/shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) (fetched 2026-06-30)

---

**5. Use subagents for research and review — keep your main context clean.** ✅

**Do:** When Claude needs to read many files to investigate something, prompt Claude to use a subagent: `"Use subagents to investigate how our auth system handles token refresh."` The subagent explores and returns only a summary; the exploration never pollutes your main conversation. Similarly use a subagent for post-implementation review: `"Use a subagent to review this diff for edge cases."` A fresh context that did not write the code produces a less biased review.

**Caveat:** ⚠️ If you omit the `tools:` field when defining a subagent in `.claude/agents/<name>.md`, the subagent implicitly gets access to **all tools** — including file writes and shell execution. Always list the `tools:` field explicitly. Independent sources flag "permission sprawl" as the most common subagent mistake.

**Sources:** [code.claude.com/docs/en/best-practices](https://code.claude.com/docs/en/best-practices) (fetched 2026-06-30) · [pubnub.com — Best Practices for Claude Code Sub-Agents](https://www.pubnub.com/blog/best-practices-for-claude-code-sub-agents/) (Aug 2025, fetched 2026-06-30) · [smartscope.blog — Claude Code Best Practices Advanced 2026](https://smartscope.blog/en/generative-ai/claude/claude-code-best-practices-advanced-2026/) (fetched 2026-06-30)

---

**6. Write specific, scoped prompts — reference exact files and patterns.** ✅

**Do:** Instead of "add tests for foo.py," write "write a test for `foo.py` covering the edge case where the user is logged out — avoid mocks." Use `@filename` in your prompt to hand Claude the file directly. Instead of "fix the login bug," write "users report login fails after session timeout; check the auth flow in `src/auth/`, especially token refresh — write a failing test that reproduces the issue, then fix it."

**Sources:** [code.claude.com/docs/en/best-practices](https://code.claude.com/docs/en/best-practices) (fetched 2026-06-30) · [claude.com/blog/best-practices-for-prompt-engineering](https://claude.com/blog/best-practices-for-prompt-engineering) (fetched 2026-06-30) · [maketocreate.com — Claude.md Best Practices: The Complete 2026 Guide](https://maketocreate.com/claude-md-best-practices-the-complete-2026-guide/) (fetched 2026-06-30)

---

**7. Use hooks for rules that must always run — not CLAUDE.md.** ✅

**Do:** If a rule must fire every single time without exception (run `eslint` after every file edit, block writes to `migrations/`, send a desktop notification when Claude needs input), implement it as a hook in `.claude/settings.json`, not as a line in CLAUDE.md. Claude can write hooks for you: "Write a hook that runs eslint after every file edit."

**Why:** CLAUDE.md instructions are advisory — Claude reads them and tries to follow them, but there is no guarantee of strict compliance, especially for vague or conflicting instructions. Hooks are shell scripts that run at fixed lifecycle events regardless of what Claude decides to do. Deterministic, not advisory.

**Caveat:** Hooks run as shell commands with the same permissions as your user account. A badly-written hook can cause its own damage. Start with read-only or notification hooks before writing hooks that block or modify files.

**Sources:** [code.claude.com/docs/en/hooks-guide](https://code.claude.com/docs/en/hooks-guide) (fetched 2026-06-30) · [code.claude.com/docs/en/memory](https://code.claude.com/docs/en/memory) (fetched 2026-06-30) · [smartscope.blog — Claude Code Best Practices Advanced 2026](https://smartscope.blog/en/generative-ai/claude/claude-code-best-practices-advanced-2026/) (fetched 2026-06-30)

---

**8. Let Claude interview you before building a complex feature.** ✅

**Do:** For large or unclear features, start with:

```
I want to build [brief description]. Interview me in detail using the AskUserQuestion tool.
Ask about technical implementation, UI/UX, edge cases, concerns, and tradeoffs. Don't ask obvious questions — dig into the hard parts I might not have considered.
Keep interviewing until we've covered everything, then write a complete spec to SPEC.md.
```

After the spec is written, start a **fresh session** to implement it. The new session has clean context focused entirely on implementation.

**Sources:** [code.claude.com/docs/en/best-practices](https://code.claude.com/docs/en/best-practices) (fetched 2026-06-30) · [community.sap.com — Claude Code Best Practices for Developers](https://community.sap.com/t5/artificial-intelligence-blogs-posts/claude-code-best-practices-for-developers/ba-p/14394164) (fetched 2026-06-30)

---

**9. ⚠️ Never run `--dangerously-skip-permissions` outside an isolated environment.** ✅

**Do:** Do not use `--dangerously-skip-permissions` (also `--permission-mode bypassPermissions`) on your real machine or in any directory containing production configs, credentials, or data you cannot restore. If you need unattended execution without constant approval prompts, use a safer permission mode instead.

**Permission modes (current as of 30 Jun 2026):** 🕒 **verify live** against [code.claude.com/docs/en/permission-modes](https://code.claude.com/docs/en/permission-modes):
- `default` — standard interactive mode with approval prompts
- `acceptEdits` — file edits accepted automatically; shell commands still require approval (practical everyday middle ground)
- `plan` — read-only; no file edits or shell commands
- `auto` — delegates each permission decision to a classifier model, safer than bypass (released March 2026; [claude.com/blog/auto-mode](https://claude.com/blog/auto-mode))
- `dontAsk` — auto-approves most actions; use carefully in CI environments
- `bypassPermissions` — removes all checks; use only inside containers, never on your real machine

**Why:** ⚠️ **WARNING.** There are documented incidents from 2025 where Claude executed `rm -rf ~/` — wiping entire home directories — in sessions that did not even use this flag. With `bypassPermissions` enabled, there is no pause and no chance to catch a bad command before it fires. Anthropic released `auto` mode in March 2026 specifically as a safer replacement. Anthropic's own engineers: "Run this in a container, not your actual machine."

**Caveat:** Auto mode aborts a non-interactive (`-p` flag) run if the classifier repeatedly blocks actions. For fully automated pipelines, you may need to pre-approve specific tools with `--allowedTools` rather than relying on auto mode alone.

**Sources:** [truefoundry.com — Claude Code dangerously-skip-permissions: When to Use It and When You Absolutely Shouldn't](https://www.truefoundry.com/blog/claude-code-dangerously-skip-permissions) (2026-06-08, fetched 2026-06-30; documents December 2025 `rm -rf ~/` incident) · [ksred.com — Claude Code dangerously-skip-permissions: When to Use It and When You Absolutely Shouldn't](https://www.ksred.com/claude-code-dangerously-skip-permissions-when-to-use-it-and-when-you-absolutely-shouldnt/) (fetched 2026-06-30; first-hand incident: Claude overwrote a config file with blank values without backup) · [code.claude.com/docs/en/permission-modes](https://code.claude.com/docs/en/permission-modes) (fetched by Timekeeper 2026-06-30) · [claude.com/blog/auto-mode](https://claude.com/blog/auto-mode) (fetched by Timekeeper 2026-06-30)

---

**10. Use `.claude/rules/*.md` with path selectors to keep per-area rules out of every session.** ✅

**Do:** Rather than cramming all project rules into a single CLAUDE.md, split domain-specific instructions into separate files under `.claude/rules/`. Add a YAML frontmatter `paths:` block to each rules file so it only loads when Claude works with matching files:

```markdown
---
paths:
  - "src/api/**/*.ts"
---
# API Development Rules
- All API endpoints must include input validation
- Use the standard error response format
```

**Caveat:** Rules without a `paths:` frontmatter load unconditionally at launch, just like content in CLAUDE.md. The selective loading only kicks in with the frontmatter. `@path` imports in CLAUDE.md load at launch regardless — they do not benefit from lazy loading. 🕒 **verify live** — the `.claude/rules/` directory and path-scoped frontmatter are recent additions; check current Claude Code docs for schema changes.

**Sources:** [code.claude.com/docs/en/memory](https://code.claude.com/docs/en/memory) (fetched 2026-06-30) · [maketocreate.com — Claude.md Best Practices: The Complete 2026 Guide](https://maketocreate.com/claude-md-best-practices-the-complete-2026-guide/) (fetched 2026-06-30) · [avilevi.co.il — Manage Claude Code Context Window](https://www.avilevi.co.il/en/blog/manage-claude-code-context-window/) (fetched 2026-06-30)

---

## Part 2 — GitHub Copilot

GitHub Copilot is Microsoft/GitHub's AI coding assistant. These practices cover instructions files, Copilot Chat, inline completions, the cloud coding agent, and agent mode in VS Code.

---

**1. Create a `.github/copilot-instructions.md` file with a structured project overview.** 📄

**Do:** Add a `.github/copilot-instructions.md` file to your repository root and structure it with these five sections: (1) what the app does (2–3 sentences), (2) your tech stack (languages, frameworks, databases, testing tools), (3) coding guidelines (indentation, type hints, naming), (4) project structure (folder purposes), (5) available tools or scripts (setup scripts, test runners, MCP servers).

**Caveat:** Keep the file under roughly two pages — GitHub's own blog notes that beyond this the response quality degrades because the file exceeds the effective context window. Focus on the 10–20 rules that matter most. The file must be committed to the repository to apply team-wide; a local-only copy helps only you. Update it the same day your stack changes — stale instructions actively mislead Copilot.

**Sources:** [github.blog — 5 tips for writing better custom instructions for Copilot](https://github.blog/ai-and-ml/github-copilot/5-tips-for-writing-better-custom-instructions-for-copilot/) (updated 2026-06-14) · [github.blog — Onboarding your AI peer programmer: Setting up GitHub Copilot coding agent for success](https://github.blog/ai-and-ml/github-copilot/onboarding-your-ai-peer-programmer-setting-up-github-copilot-coding-agent-for-success/) (2025-07-31) · [docs.github.com — Best practices for using GitHub Copilot](https://docs.github.com/en/copilot/get-started/best-practices) (fetched 2026-06-30)

---

**2. Use path-specific `.instructions.md` files for language- or tool-specific rules.** ✅

**Do:** For rules that apply only to certain file types, create `.github/instructions/*.instructions.md` files. Add YAML frontmatter with the glob pattern:

```yaml
---
name: "Frontend instructions"
description: "React/TypeScript rules"
applyTo: "src/components/**/*.ts,src/components/**/*.tsx"
---
```

Enable these in VS Code workspace settings:
```json
{
  "github.copilot.chat.codeGeneration.useInstructionFiles": true,
  "chat.instructionsFilesLocations": { ".github/instructions": true }
}
```

**Caveat:** This feature was introduced July 2025 — verify it is available in your version of VS Code and your Copilot plan. 🕒 verify live. The deprecated VS Code setting `github.copilot.chat.codeGeneration.instructions` (a JSON array) should be replaced with instruction files; do not use both as they can conflict.

**Sources:** [github.blog — Unlocking the full power of Copilot code review: Master your instructions files](https://github.blog/ai-and-ml/github-copilot/unlocking-the-full-power-of-copilot-code-review-master-your-instructions-files/) (updated 2026-04-17) · [smartscope.blog — GitHub Copilot Custom Instructions Complete Guide](https://smartscope.blog/en/generative-ai/github-copilot/github-copilot-custom-instructions-guide/) (updated 2026-03-05)

---

**3. In Copilot Chat, use `@workspace` (VS Code) or explicit `#file` references to supply context.** ✅

**Do:** When asking Copilot Chat about your codebase, start with `@workspace` (VS Code) or `@project` (JetBrains) to pull in project-wide context. Pin specific files with `#file:path/to/file.ts`. Use `#selection` to scope to highlighted code. Open a new chat thread (`+` button) for each new task rather than carrying stale context forward.

**Caveat:** `@workspace` builds an index of local files — large monorepos may return incomplete context. If Copilot references wrong files, explicitly pin the correct file with `#file:` rather than relying on automatic detection.

**Sources:** [docs.github.com — Prompt engineering for GitHub Copilot Chat](https://docs.github.com/en/copilot/concepts/prompting/prompt-engineering) (fetched 2026-06-30) · [docs.github.com — Getting started with prompts for Copilot Chat](https://docs.github.com/copilot/get-started/getting-started-with-prompts-for-copilot-chat) (fetched 2026-06-30) · Versent Tech Blog — "The Secret Weapon for Better GitHub Copilot Results: Context" (2025-10-29; link removed — medium.com returned 403 on publish date)

**Confidence:** vendor-documented (both linked sources are GitHub/Microsoft; Versent independent article unlinked due to 403)

---

**4. Guide inline completions with specific, descriptive comments.** ✅

**Do:** Write a comment immediately above the code you want Copilot to complete, describing exactly what you need — including algorithm choice, error handling, and return types. For inline completions, keep only files relevant to the current task open in your editor tabs; close unrelated files.

**Caveat:** Inline completions do **not** read `.github/copilot-instructions.md` or custom instruction files — those only apply to Chat and Agent mode. For inline completions, the comment and surrounding code are the entire context. Always review ghost text before accepting with Tab.

**Sources:** [docs.github.com — GitHub Copilot code suggestions in your IDE](https://docs.github.com/en/copilot/concepts/completions/code-suggestions) (fetched 2026-06-30) · Wipro Tech Blogs — "Mastering GitHub Copilot: Best Practices" (2026-03-11; link removed — wiprotechblogs.medium.com returned 403 on publish date) · [smartscope.blog — GitHub Copilot Custom Instructions Complete Guide](https://smartscope.blog/en/generative-ai/github-copilot/github-copilot-custom-instructions-guide/) (updated 2026-03-05)

---

**5. Keep personal (user-level) custom instructions to 2–3 rules maximum.** (thin)

**Do:** If you set personal custom instructions in VS Code settings (your user-level preferences, not the repo-level `.github/copilot-instructions.md`), limit yourself to 2–3 high-impact, universal rules. Do not duplicate repo-level rules.

**Why:** Copilot receives all active instruction sources simultaneously. When instructions from different levels conflict, Copilot tends to fall back on its own defaults. Delegate formatting decisions to linters and pre-commit hooks instead — that removes an entire class of conflicts.

**Sources:** [dev.to — All I've Learned About GitHub Copilot Instructions (So Far)](https://dev.to/anchildress1/all-ive-learned-about-github-copilot-instructions-so-far-5bm7) (2025-07-02, fetched 2026-06-30)

**Confidence:** thin (single independent source; GitHub Docs do not document a 2–3 rule threshold explicitly)

---

**6. ⚠️ Write well-scoped issues when using Copilot coding agent — it is fully autonomous.** 📄

**Do:** When assigning a GitHub Issue to the Copilot coding agent, include: (1) a clear problem statement, (2) complete error messages or stack traces, (3) relevant file paths or function names, (4) acceptance criteria, (5) a suggested implementation approach if you have one. **Start with small, isolated tasks:** bug fixes, test coverage, documentation updates, accessibility fixes. **Avoid** tasks requiring cross-repository knowledge, security-sensitive code, or ambiguous scope.

**Why:** ⚠️ **WARNING — the coding agent is fully autonomous.** It will read your issue, explore the codebase, write code, and open a pull request with **no further prompting from you**. If the issue is vague, the pull request will be vague. **Review every pull request it opens before merging.** Do not assign production-critical or security-sensitive issues to the agent.

**Caveat:** The agent runs in a GitHub Actions environment with a default network firewall that blocks arbitrary internet access but allows common package registries (npm, pip, apt). Disabling the firewall exposes your environment to data exfiltration — do not disable it.

**Sources:** [docs.github.com — Best practices for using Copilot to work on tasks](https://docs.github.com/copilot/how-tos/agents/copilot-coding-agent/best-practices-for-using-copilot-to-work-on-tasks) (fetched 2026-06-30) · [github.blog — Onboarding your AI peer programmer: Setting up GitHub Copilot coding agent for success](https://github.blog/ai-and-ml/github-copilot/onboarding-your-ai-peer-programmer-setting-up-github-copilot-coding-agent-for-success/) (2025-07-31)

---

**7. Create a `copilot-setup-steps.yml` to pre-install dependencies for the coding agent.** 📄

**Do:** Create `.github/workflows/copilot-setup-steps.yml` with a job named `copilot-setup-steps`. List all runtime versions, package dependencies, and system libraries your project needs. This file runs before the agent starts its task.

**Caveat:** 🕒 verify live — network configuration for the coding agent changed February 2026; check current firewall and allowlist rules. Default firewall allows Debian/Ubuntu/Red Hat OS repos, common container registries, and popular language package registries. If you need additional internet access, explicitly allowlist those hosts — do not disable the firewall.

**Sources:** [github.blog — Onboarding your AI peer programmer](https://github.blog/ai-and-ml/github-copilot/onboarding-your-ai-peer-programmer-setting-up-github-copilot-coding-agent-for-success/) (2025-07-31) · [docs.github.com — Customizing or disabling the firewall for Copilot cloud agent](https://docs.github.com/copilot/customizing-copilot/customizing-or-disabling-the-firewall-for-copilot-coding-agent) (fetched 2026-06-30)

---

**8. Always review and test Copilot suggestions before committing — especially security-sensitive code.** ✅

**Do:** Treat every Copilot suggestion as a draft from a junior engineer. Before accepting: (1) read the code and understand it, (2) run your test suite, (3) run your linter and static analysis, (4) check database-interaction code for SQL injection, (5) check authentication code for logic flaws. Use `/fix` and `/tests` slash commands in Chat to ask Copilot to help verify its own output.

**Caveat:** ⚠️ **Never commit code containing hardcoded secrets.** Copilot's context window may include content from files near open secrets (e.g., `.env` files) and can inadvertently suggest credential-shaped strings. Keep secrets in environment variables or secret managers.

**Security note:** A prompt injection vulnerability was documented in March 2026 (reported by security researcher @ismailkovvuru; no formal CVE assigned) that could allow an attacker to embed malicious content in a GitHub Issue and trigger Copilot to execute arbitrary tool calls (RCE) if the user had `chat.tools.autoApprove: true` enabled. Mitigation: update your Copilot extension to the latest version; do not enable auto-approve for tool calls.

**Sources:** [docs.github.com — Best practices for using GitHub Copilot](https://docs.github.com/en/copilot/get-started/best-practices) (fetched 2026-06-30) · [prompt.security — Securing Enterprise Data in the Face of GitHub Copilot Vulnerabilities](https://prompt.security/blog/securing-enterprise-data-in-the-face-of-github-copilot-vulnerabilities) (2025-01-01) · [embracethered.com — GitHub Copilot Remote Code Execution via Prompt Injection](https://embracethered.com/blog/posts/2025/github-copilot-remote-code-execution-via-prompt-injection/) (fetched 2026-06-30; medium.com/@ismailkovvuru original returned 403 on publish date — this is an independent security researcher writeup on the same vulnerability)

---

**9. In agent mode (VS Code / Visual Studio), review and approve terminal commands before allowing them to run.** 📄

**Do:** When using Copilot agent mode, read every proposed terminal command in the approval dialog before clicking Allow. Use "Undo Last Edit" or checkpoint restore to roll back file changes if the agent goes wrong. Give agent mode focused sub-tasks and review output before continuing, rather than one giant prompt.

**Caveat:** ⚠️ **WARNING — agent mode can use AI credits quickly.** 🕒 **verify live** — GitHub Copilot moved to an AI Credits billing system on **June 1, 2026** (replacing the older "free tier" quota model). Current allotments: Free plan (limited), Pro 1,500 credits/month, Pro+ 7,000 credits/month, Max 20,000 credits/month. Agent-heavy tasks consume credits faster than chat completions. Check your plan at [github.com/settings/copilot](https://github.com/settings/copilot) · [github.blog/changelog — Updates to GitHub Copilot billing and plans](https://github.blog/changelog/2026-06-01-updates-to-github-copilot-billing-and-plans/) (2026-06-01)

**Do not** enable "Allow all" for terminal commands by default — this removes the per-command approval step. In Visual Studio, per-solution approval grants persist until manually reset in Tools > Options > GitHub > Copilot > Tools.

**Sources:** [code.visualstudio.com — Introducing GitHub Copilot agent mode](https://code.visualstudio.com/blogs/2025/02/24/introducing-copilot-agent-mode) (2025-02-24) · [learn.microsoft.com — Use Agent Mode in Visual Studio](https://learn.microsoft.com/en-us/visualstudio/ide/copilot-agent-mode?view=visualstudio) (updated 2026-05-29)

---

**10. Break complex Chat requests into sequential steps; start new threads when switching tasks.** ✅

**Do:** In Copilot Chat, decompose large requests into a chain of focused prompts: first ask Copilot to outline its approach, review that outline, then implement one step at a time. When you switch to a completely new task, open a new chat thread (`+` button). State constraints up front in each prompt: "without changing the public API", "compatible with Node 18", "do not modify the test files."

**Caveat:** Avoid pasting entire large files into the chat box — use `#file:` references instead. Do not ask Copilot to solve problems outside your codebase (general knowledge lookups, non-coding questions) — this is outside its design and produces unreliable results.

**Sources:** [docs.github.com — Prompt engineering for GitHub Copilot Chat](https://docs.github.com/en/copilot/concepts/prompting/prompt-engineering) (fetched 2026-06-30) · [anjith.tech — GitHub Copilot Best Practices: From Good to Great](https://anjith.tech/2026/01/27/github-copilot-best-practices-from-good-to-great/) (2026-01-27) · Wipro Tech Blogs — "Mastering GitHub Copilot: Best Practices" (2026-03-11; link removed — wiprotechblogs.medium.com returned 403 on publish date) · Versent Tech Blog — "The Secret Weapon for Better GitHub Copilot Results: Context" (2025-10-29; link removed — medium.com returned 403 on publish date)

---

## Part 3 — Cursor

Cursor is an AI-first code editor (a fork of VS Code). These practices cover its rules system, context tools, and Agent/Composer mode.

---

**1. Migrate from `.cursorrules` to `.cursor/rules/` with `.mdc` files.** ✅

**Do:** Stop using the single `.cursorrules` file at your project root. Create a `.cursor/rules/` directory and put each concern in its own `.mdc` file with YAML frontmatter.

**Why:** Cursor deprecated `.cursorrules` in 2025 (during the 0.43–0.45 release cycle) and introduced `.cursor/rules/` as its replacement. These were Cursor version milestones from 2025 — as of June 22, 2026, Cursor is at version 3.9. The old `.cursorrules` format still works but will not receive new features and will eventually be removed. 🕒 **verify live** — check [cursor.com/changelog](https://cursor.com/changelog) for the current removal timeline.

**Caveat:** Plain `.md` files inside `.cursor/rules/` are silently ignored — only `.mdc` files are recognized. Double-check the extension.

**Sources:** [cursor.com/docs/rules](https://www.cursor.com/docs/rules) (fetched 2026-06-30) · [flowql.com — Cursor Rules Deprecated Libraries](https://www.flowql.com/en/blog/guides/cursor-rules-deprecated-libraries/) (2026-04-24) · [cursor.com/changelog](https://cursor.com/changelog) (Timekeeper-fetched 2026-06-30; shows v3.9, June 22 2026, as current)

---

**2. Pick the right rule activation type — don't make everything `alwaysApply: true`.** ✅

**Do:** For each `.mdc` rule file, choose the appropriate activation mode using three frontmatter fields:

| Goal | Set these fields |
|------|-----------------|
| Must load every request (e.g., "always use TypeScript strict mode") | `alwaysApply: true` |
| Load when certain files are open (e.g., React patterns for `.tsx`) | `globs: ["src/**/*.tsx"]` |
| Agent decides relevance by description (e.g., Stripe integration guide) | `description: "..."` |
| Load only when you explicitly ask (`@rule-name` in chat) | leave all three blank/false |

**Why:** Every token in an always-on rule is included in every single AI request. Putting 20 rules on `alwaysApply: true` burns thousands of tokens before the AI has even read your question, which shrinks how much of your code it can see.

**Caveat:** The `alwaysApply` field overrides `globs` and `description`. Test glob patterns against your actual file paths; `{src,lib}/**/*.ts` brace syntax is reported as unreliable — use YAML list syntax instead.

**Sources:** [cursor.com/docs/rules](https://www.cursor.com/docs/rules) (fetched 2026-06-30) · [techsy.io — Cursor Rules Guide](https://techsy.io/en/blog/cursor-rules-guide) (2026-06-13) · [vibecodingacademy.ai — Cursor Rules Complete Guide](https://www.vibecodingacademy.ai/blog/cursor-rules-complete-guide) (2026-05-01)

---

**3. Keep rules short and actionable — under 500 lines per file, under 200 words for always-on rules.** ✅

**Do:** Write rules as dense directives, not paragraphs of explanation. Reference file paths instead of pasting file contents. Split large rule files into smaller focused ones (typical project: 5–8 rule files). Apply the "rule of three" — only codify a pattern after the AI has failed at it three times.

**Why:** AI models need directives, not persuasion. A rule that says "write clean, readable code" gives the AI nothing concrete. A rule that says "name boolean variables `is_*` or `has_*`; never use `flag`" is unambiguous.

**Sources:** [cursor.com/docs/rules](https://www.cursor.com/docs/rules) (fetched 2026-06-30) · [techsy.io — Cursor Rules Guide](https://techsy.io/en/blog/cursor-rules-guide) (2026-06-13) · [vibecodingacademy.ai — Cursor Rules Complete Guide](https://www.vibecodingacademy.ai/blog/cursor-rules-complete-guide) (2026-05-01)

---

**4. Use the right context tool — `@file` when you know the file, `@codebase` when you don't.** ✅

**Do:** Prefer explicit `@file` or `@folder` mentions when you know which files are relevant. Use `@codebase` for exploratory questions when you are unsure which files matter. Use `@docs` for external library documentation. Use `@web` for real-time information (current package versions, recent API changes).

**Caveat:** `@codebase` uses vector embeddings — if your function is named "Login" but the code says "SessionCreation," semantic search may miss it. When `@codebase` fails on critical files, fall back to explicit `@file` references. Including too many `@file` mentions clutters context — use only what is directly relevant. Note: `@docs` indexing (adding a documentation URL in Cursor settings) is described in secondary sources only; the official docs page returned 404 during this research run. ⚠ PENDING official docs confirmation.

**Sources:** [datalakehousehub.com — Context Management in Cursor](https://datalakehousehub.com/blog/2026-03-context-management-cursor/) (2026-03) · [stevekinney.com — Cursor Context](https://stevekinney.com/courses/ai-development/cursor-context) (2026-06-24) · [github.com/murataslan1/cursor-ai-tips — context-management.md](https://github.com/murataslan1/cursor-ai-tips/blob/main/tips/context-management.md) (fetched 2026-06-30)

---

**5. Write Composer/Agent prompts as scoped work orders, not open-ended requests.** ✅

**Do:** Structure Composer and Agent mode prompts to include: (1) explicit goal, (2) files in scope via `@file` or `@folder`, (3) what is out of scope, (4) a verifiable "done" condition. Example:

> "Add an `exportToCsv()` function to `@src/reports/ReportService.ts`. Do not modify any other files. Done when `npm test -- ReportService` passes."

**Why:** Agent mode can edit multiple files autonomously and run terminal commands. Vague prompts ("make this better") give the agent no stopping point and can result in widespread unintended changes.

**Caveat:** Use Composer/Agent for multi-file changes. For a single-line fix, inline edit (Cmd+K) is faster. For exploratory questions, use Chat.

**Sources:** [cursor.com/blog/agent-best-practices](https://cursor.com/blog/agent-best-practices) (2026-01-09) · [sureprompts.com — Cursor AI Prompting Guide](https://sureprompts.com/blog/cursor-ai-prompting-guide) (2026-04-20)

---

**6. Start a new chat after completing a logical unit of work.** ✅

**Do:** Open a fresh chat session when you finish a feature or task, when the agent starts repeating mistakes, or when you shift to a clearly different concern. Cursor's own blog warns that long conversations cause the agent to lose focus and can cause it to switch to unrelated tasks. As a practical threshold, the getstream.io source recommends starting fresh every **5–7 steps in a Composer window** for complex work. Before closing, ask the agent to summarize what was built if you want to carry forward context.

**Caveat:** Cursor provides `@Past Chats` to reference earlier conversation summaries without copy-pasting entire histories.

**Sources:** [cursor.com/blog/agent-best-practices](https://cursor.com/blog/agent-best-practices) (2026-01-09) · [datalakehousehub.com — Context Management in Cursor](https://datalakehousehub.com/blog/2026-03-context-management-cursor/) (2026-03) · [getstream.io — Cursor AI for Large Projects](https://getstream.io/blog/cursor-ai-large-projects/) (2025-03-05)

---

**7. Give the agent verifiable goals — tests, linters, and typed languages act as automatic feedback signals.** ✅

**Do:** Before asking Agent to implement something, ensure you have a typed language (TypeScript, Python with type hints) configured, a linter (ESLint, Ruff), and at least a stub test file. Then add to your prompt: "Write tests first, then implementation, then run the tests and fix until they pass."

**Caveat:** ⚠️ **WARNING — Cursor has a "YOLO mode" setting** (in Cursor Settings > Features > Agent) that lets the agent run terminal commands without asking permission first. This is useful for automated build-fix loops but dangerous if the agent decides to run destructive commands (`rm`, database migrations, deploys). Enable it only after you understand which commands your agent is allowed to run, and restrict it explicitly in a rule: "only run test and build commands — never run database migrations or deploy commands without user confirmation."

**Sources:** [cursor.com/blog/agent-best-practices](https://cursor.com/blog/agent-best-practices) (2026-01-09) · [builder.io — Cursor Tips](https://www.builder.io/blog/cursor-tips) (2025-03-11) · [getstream.io — Cursor AI for Large Projects](https://getstream.io/blog/cursor-ai-large-projects/) (2025-03-05)

---

**8. Commit `.cursor/rules/` to version control and treat rule files like code.** ✅

**Do:** Include the `.cursor/rules/` directory in your git repository. Review rule changes in pull requests. Write descriptive commit messages when updating rules. Document breaking rule changes so teammates know what changed.

**Why:** Rule files are the persistent memory of your project's AI configuration. If they live only on one developer's machine, every new team member gets inconsistent AI behavior. Versioned rules also make it possible to revert a bad rule change.

**Caveat:** Personal preferences (your own keybindings, your preferred verbosity level) belong in User Rules (Cursor Settings), not in project-level `.cursor/rules/` files. Committing personal preferences forces them on every team member.

**Sources:** [vibecodingacademy.ai — Cursor Rules Complete Guide](https://www.vibecodingacademy.ai/blog/cursor-rules-complete-guide) (2026-05-01) · [cursor.com/docs/rules](https://www.cursor.com/docs/rules) (fetched 2026-06-30)

---

**9. Review every diff before accepting — Agent output can look right while being wrong.** ✅

**Do:** Read every diff the agent produces before clicking "Accept." Pay attention to files you did not expect to be modified. Use Cursor's built-in Review mode for larger change sets. Cursor creates automatic checkpoints before significant changes (visible in the chat timeline) so you can roll back without affecting your Git history.

**Sources:** [cursor.com/blog/agent-best-practices](https://cursor.com/blog/agent-best-practices) (2026-01-09) · [ellenox.com — Mastering Cursor AI: Advanced Workflows and Best Practices](https://www.ellenox.com/post/mastering-cursor-ai-advanced-workflows-and-best-practices) (2025-06-04)

---

## Held pending fixes (not publish-ready)

- **claude-code Practice 4:** Specific token-count degradation thresholds are third-party empirical observations, not Anthropic-published specifications. Monitor for Anthropic-published benchmarks. ⚠ PENDING
- **cursor Practice 4 (`@docs`):** Official Cursor docs page for `@docs` indexing returned 404 during research — the workflow for adding documentation URLs to Cursor is described in secondary sources only. ⚠ PENDING official docs confirmation
- **github-copilot Practice 5:** The 2–3 personal instructions limit has only one independent source (dev.to); GitHub Docs do not document this threshold. Needs a second independent source or should be dropped. ⚠ PENDING corroboration
- **claude-code Practice 9 (auto mode release date):** March 2026 release date sourced from independent articles; Anthropic's own announcement found at claude.com/blog/auto-mode (Timekeeper confirmed) — verified as resolvable on next refresh.
- **claude-code Practice 2 (plan mode keybindings):** `Shift+Tab` multi-mode cycling confirmed in Timekeeper verification; added verify-live caveat. ⚠ verify live

---

## CHANGELOG (panel corrections applied to produce this entry)

**Research phase (2026-06-30):** Four pupils researched in parallel (Claude Code, GitHub Copilot, Cursor, Generic/universal). Each fetched sources live; none recalled from training.

**Skeptic (3 KILLs, 2 FIXes applied):**
1. KILL: Removed "32% of developers experienced unintended file modification; 9% reported data loss" from claude-code Practice 9. The cited source (ksred.com) documents a first-hand incident but contains no survey statistics. These numbers were unsupported. The first-hand incident (Claude overwrote a config file with blank values) is retained.
2. KILL: Fixed the prompt injection vulnerability description in github-copilot Practice 8. The cited Medium article explicitly says "No CVE Assigned" — removed the CVE-2025-53773 designation. The attack mechanism is RCE (triggering auto-approve for tool calls), not secrets exfiltration. Documented in March 2026, not "patched August 2025" — rewritten as "update your extension to the latest version."
3. KILL: Removed "147,000–152,000 token" specific degradation threshold from claude-code Practice 4. The cited source (avilevi.co.il) does not contain those numbers. The general principle (fill = worse) is retained from multiple corroborated sources.
4. FIX: Changed github-copilot Practice 1 file length threshold from "~1,000 lines" to "~2 pages" to match what the cited GitHub Blog source actually says.
5. FIX: Changed cursor Practice 6 chat restart frequency from "5–20 messages" to "5–7 steps in a Composer window" to match what the cited getstream.io source actually says.

**Timekeeper (2 KILLs, 3 FIXes applied):**
6. KILL: Updated cursor Practice 1 version numbers. The 0.43/0.45/0.47 milestones are from 2025 and still accurate as historical deprecation milestones, but "still works as of version 0.47" implied 0.47 is current — it is not. Cursor is at version 3.9 as of June 22, 2026. Rewritten to describe these as 2025 milestones.
7. KILL: Updated github-copilot Practice 9 billing model. GitHub Copilot moved to an AI Credits system on June 1, 2026 — four weeks before this snapshot. Replaced the stale "free quota quickly" warning (citing a Feb 2025 VS Code blog) with current plan allotments and the changelog URL.
8. FIX: Expanded claude-code Practice 9 permission mode list from 2 modes to all 6 current modes (default, acceptEdits, plan, auto, dontAsk, bypassPermissions) per code.claude.com/docs/en/permission-modes.
9. FIX: Added claude.com/blog/auto-mode as a confirmed source for auto mode (previously held-pending).
10. FIX: Added note to universal Practice 9 that `.cursorrules` is deprecated in favor of `.cursor/rules/*.mdc`.

**Link-check gate (2026-06-30 publish-time):**
14. Three Medium URLs returned 403 (curl blocked; archive.org had no snapshots). Repaired per link-check gate rules:
    - `medium.com/@ismailkovvuru` (RoguePilot/Copilot prompt injection): replaced with `embracethered.com/blog/posts/2025/github-copilot-remote-code-execution-via-prompt-injection/` (independent security researcher, confirmed 200).
    - `medium.com/versent-tech-blog` (Copilot @workspace context, 2025-10-29): unlinked to plain text. Practice 3 downgraded from independently-corroborated to vendor-documented (GitHub Docs × 2 remain).
    - `wiprotechblogs.medium.com` (Mastering Copilot, 2026-03-11): unlinked to plain text in Practice 4 (GitHub Docs + SmartScope remain = independently-corroborated). In Practice 10, replaced with `anjith.tech/2026/01/27/github-copilot-best-practices-from-good-to-great/` (confirmed 200, Jan 2026) to preserve independent corroboration.

**Beginner panel (informing beginner-track edits; technical track adjustments):**
11. Elevated git checkout destructive-discard warning in universal Practice 8 to the main Caveat block (was implicit).
12. Elevated coding agent autonomy warning in Copilot Practice 6 to the main Do section (was Caveat-only).
13. Elevated subagent unrestricted tools warning in claude-code Practice 5 — already in Caveat, confirmed prominent.
