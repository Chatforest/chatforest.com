# Prompt Engineering for Claude Code — Best Practices (as of 01 Jul 2026)

> Concrete, source-verified practices for getting better results from Claude Code: writing effective CLAUDE.md files, managing context, using subagents, hooks, and staying safe.


<!-- Immutable dated snapshot. Researched 2026-06-30, graded 2026-06-30, published 2026-07-01.
     Source tiers: independently-corroborated = 2+ DIFFERENT publishers; vendor-documented =
     official Anthropic docs only (authoritative, single source). -->

# Prompt Engineering for Claude Code (as of 01 Jul 2026)

> **Grading note.** A dated snapshot — accurate as of **01 Jul 2026**, frozen here and kept as a
> permanent archive entry. Research-drafted by a pupil (2026-06-30), graded by the 3-lens panel
> (2026-06-30). **0 fabrications.** 7 corrections applied: 2 Skeptic KILLs (fabricated statistics
> removed), 3 Skeptic FIXes (attribution and paraphrase tightening), 2 Timekeeper FIXes (permission
> mode expansion, auto mode sourcing upgrade). 3 items remain ⚠ PENDING — never guessed.

## How to read the labels
- ✅ **independently-corroborated** — confirmed by 2+ independent publishers
- 📄 **vendor-documented** — official Anthropic docs only (authoritative, single source)
- ⚠️ **WARNING** — a default that can cost money, break the machine, or remove a safety net
- 🕒 **verify live** — fast-moving detail; check the current value before relying on it

---

## Practice 1: Write a short, specific CLAUDE.md — and keep it under 200 lines

**Do:** Create a `CLAUDE.md` file at your project root (or run `/init` to generate one automatically). Include only facts Claude cannot infer from reading the code: exact build/test/lint commands, non-obvious architectural decisions, naming conventions, and project-specific gotchas. Keep it under 200 lines. Ask of every line: "Would removing this cause Claude to make a mistake?" If no, cut it.

**Why:** CLAUDE.md is read at the start of every session, loading into Claude's context window automatically. A bloated file pushes important rules past the point where Claude reliably notices them. Research shows accuracy can drop more than 30% when key instructions are buried in verbose content — a "lost in the middle" effect documented across frontier models.

**Caveat:** The 200-line figure is a widely-cited rule of thumb, not a hard system limit. Some independent sources suggest 60 lines is a better target for complex projects that also use `.claude/rules/*.md` path-scoped files. Splitting into topic files in `.claude/rules/` helps organise content, but imported `@path` files still load at launch and consume tokens — splitting does not reduce total context usage.

**What to include vs. exclude:**

| Include | Exclude |
|---|---|
| Exact commands: `npm test`, `make lint` | Anything Claude can infer from reading the code |
| Code style rules that differ from defaults | Standard language conventions Claude already knows |
| Architecture: the 3–5 directories that matter | File-by-file descriptions of the whole codebase |
| Repository etiquette (branch naming, PR rules) | Detailed API docs (link to them instead) |
| Non-obvious environment quirks, required env vars | Long explanations or tutorials |
| Common gotchas or non-obvious behaviors | Self-evident practices like "write clean code" |

**Sources:**
- [code.claude.com/docs/en/best-practices](https://code.claude.com/docs/en/best-practices) (Anthropic, fetched 2026-06-30) — the primary vendor source; the include/exclude table is reproduced almost verbatim from it
- [code.claude.com/docs/en/memory](https://code.claude.com/docs/en/memory) (Anthropic, fetched 2026-06-30) — detailed CLAUDE.md file locations, load order, and import syntax
- [maketocreate.com/claude-md-best-practices-the-complete-2026-guide/](https://maketocreate.com/claude-md-best-practices-the-complete-2026-guide/) (independent, fetched 2026-06-30) — cites the 30%+ accuracy drop from verbose context; recommends the three-tier system
- [github.com/shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) (independent, fetched 2026-06-30) — 60-line baseline recommendation; `.claude/rules/` path-selector pattern

**Confidence:** ✅ independently-corroborated (Anthropic official docs + 2 independent publishers)

---

## Practice 2: Use plan mode before writing code for any multi-file change

**Do:** For anything that touches more than one file, or when you are uncertain about the approach, switch Claude into plan mode before implementation begins. In the interactive terminal, press `Ctrl+G` after Claude produces a plan to open it in your editor for direct review and editing. Only then leave plan mode and let Claude start writing code.

**Why:** Without a planning step, Claude can confidently solve the wrong problem. Separating "explore and plan" from "write code" catches misunderstandings early, when correction costs nothing. For a single-file typo fix or a rename, skip the plan — the overhead is not worth it.

**Caveat:** Plan mode adds round-trip time. The official docs explicitly state: "If you could describe the diff in one sentence, skip the plan." Use judgment. This practice is overhead for trivial changes. 🕒 **verify live** — the plan mode workflow has expanded significantly; `Shift+Tab` now cycles through multiple modes, and plan approval now offers a choice of which mode to enter after approval. Check [code.claude.com/docs/en/permission-modes](https://code.claude.com/docs/en/permission-modes) for the current `Shift+Tab` cycle and plan approval options.

**Sources:**
- [code.claude.com/docs/en/best-practices](https://code.claude.com/docs/en/best-practices) (Anthropic, fetched 2026-06-30) — four-phase Explore → Plan → Implement → Commit workflow with exact prompt examples
- [community.sap.com/t5/artificial-intelligence-blogs-posts/claude-code-best-practices-for-developers/ba-p/14394164](https://community.sap.com/t5/artificial-intelligence-blogs-posts/claude-code-best-practices-for-developers/ba-p/14394164) (SAP Community, independent, fetched 2026-06-30) — recommends always planning before coding: pausing to plan costs near zero; wrong edits cost hours of rework
- [code.claude.com/docs/en/permission-modes](https://code.claude.com/docs/en/permission-modes) (Anthropic, fetched 2026-06-30) — current plan mode workflow including `Ctrl+G` to open plan in editor

**Confidence:** ✅ independently-corroborated

---

## Practice 3: Give Claude a verifiable check it can run, not just "looks done"

**Do:** When you assign a task, always tell Claude how to verify success: a test suite command, a build exit code, a linter check, or (for UI work) a screenshot comparison. Ask Claude to run the check and iterate until it passes — do not accept "I think this should work."

**Why:** Claude stops when the work looks done. Without a runnable check, you become the verification loop — every mistake waits for you to notice it. A failing test returned in the conversation closes the loop automatically and lets you step away from a session with confidence.

**Caveat:** "Show evidence rather than asserting success" (the test output, the command it ran, the screenshot) is slightly more work to prompt for, but reviewing evidence is faster than re-running verification yourself.

**Sources:**
- [code.claude.com/docs/en/best-practices](https://code.claude.com/docs/en/best-practices) (Anthropic, fetched 2026-06-30) — "Give Claude a check it can run" section with before/after prompt table
- [community.sap.com/t5/artificial-intelligence-blogs-posts/claude-code-best-practices-for-developers/ba-p/14394164](https://community.sap.com/t5/artificial-intelligence-blogs-posts/claude-code-best-practices-for-developers/ba-p/14394164) (SAP Community, independent, fetched 2026-06-30) — "Never claim done without proof" verification checklist

**Confidence:** ✅ independently-corroborated

---

## Practice 4: Manage the context window proactively — don't wait for auto-compact

**Do:** Use `/clear` between unrelated tasks to reset the context window entirely. For related tasks where you want continuity, run `/compact <instructions>` with a hint about what to keep (e.g., `/compact Focus on the API changes, drop the test debugging thread`). After two failed correction attempts on the same issue, stop, run `/clear`, and rewrite a cleaner prompt incorporating what you learned.

**Why:** Claude's context window is the single most important resource to manage. Performance degrades as it fills: Claude may start ignoring earlier instructions or making more mistakes. Independent research indicates degradation can begin as early as 40% utilization. Correcting over and over without clearing only accumulates failed approaches and makes things worse.

**Caveat:** 🕒 **verify live** — specific degradation thresholds (the 40% figure) are empirical observations from third-party testing, not guaranteed Anthropic specifications, and may shift with model updates. The general principle (fill → worse) is independently confirmed. The "two failed corrections = /clear" rule is documented in Anthropic's own best-practices guide.

**Sources:**
- [code.claude.com/docs/en/best-practices](https://code.claude.com/docs/en/best-practices) (Anthropic, fetched 2026-06-30) — "Manage context aggressively" section; `/compact`, `/clear`, `/rewind`, and the "after two failed corrections, /clear" rule
- [claudefa.st/blog/guide/mechanics/context-management](https://claudefa.st/blog/guide/mechanics/context-management) (independent, fetched 2026-06-30) — 80% capacity rule; high-context vs low-context task classification; explicit "when to use /compact vs /clear"
- [avilevi.co.il/en/blog/manage-claude-code-context-window/](https://www.avilevi.co.il/en/blog/manage-claude-code-context-window/) (independent, fetched 2026-06-30) — `/context` command to display token breakdown; one-conversation-one-goal rule
- [github.com/shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) (independent, fetched 2026-06-30) — 40% utilization threshold; 300–400k token limit on 1M models

**Confidence:** ✅ independently-corroborated (multiple independent publishers agree on core principle; specific thresholds are `thin` within that)

---

## Practice 5: Use subagents for research and review — keep your main context clean

**Do:** When Claude needs to read many files to investigate something (e.g., "how does authentication work in this codebase?"), prompt Claude to use a subagent: `"Use subagents to investigate how our auth system handles token refresh."` The subagent explores and reports back a summary; the exploration never pollutes your main conversation. Similarly, use a subagent for post-implementation review: `"Use a subagent to review this diff for edge cases."` A fresh context that did not write the code produces a less biased review.

**Why:** Each file Claude reads costs tokens in your context window. Subagents run in their own separate context window and return only a summary. This keeps your main session clean and extends how long a complex task can run before quality degrades.

**Caveat:** If you omit the `tools:` field when defining a subagent in `.claude/agents/<name>.md`, the subagent implicitly gets access to all tools — including file writes and shell execution. Always list the tools explicitly. Independent sources flag "permission sprawl" as the most common subagent mistake.

**Sources:**
- [code.claude.com/docs/en/best-practices](https://code.claude.com/docs/en/best-practices) (Anthropic, fetched 2026-06-30) — "Use subagents for investigation" and "Add an adversarial review step" sections with exact prompt examples
- [pubnub.com/blog/best-practices-for-claude-code-sub-agents/](https://www.pubnub.com/blog/best-practices-for-claude-code-sub-agents/) (PubNub, independent, Aug 2025, fetched 2026-06-30) — single-responsibility rule; "permission sprawl" anti-pattern; three-stage pipeline pattern (pm-spec → architect-review → implementer-tester)
- [smartscope.blog/en/generative-ai/claude/claude-code-best-practices-advanced-2026/](https://smartscope.blog/en/generative-ai/claude/claude-code-best-practices-advanced-2026/) (SmartScope, independent, 2026, fetched 2026-06-30) — smaller focused contexts yield better tool selection; writer/reviewer pattern with git worktrees

**Confidence:** ✅ independently-corroborated

---

## Practice 6: Write specific, scoped prompts — reference exact files and patterns

**Do:** Instead of "add tests for foo.py," write "write a test for `foo.py` covering the edge case where the user is logged out — avoid mocks." Instead of "fix the login bug," write "users report login fails after session timeout; check the auth flow in `src/auth/`, especially token refresh — write a failing test that reproduces the issue, then fix it." Use `@filename` in your prompt to hand Claude the file directly rather than describing where it lives.

**Why:** Claude can infer intent but not read your mind. Vague prompts lead to plausible-looking but wrong implementations. Specific prompts reduce the back-and-forth correction cycle, which itself wastes context.

**Caveat:** Vague prompts are useful for exploration. If you want Claude to surface what it would improve in a file without a fixed agenda, a broad prompt like "what would you change here?" is intentional, not a mistake.

**Sources:**
- [code.claude.com/docs/en/best-practices](https://code.claude.com/docs/en/best-practices) (Anthropic, fetched 2026-06-30) — "Provide specific context" section with a four-row before/after table
- [claude.com/blog/best-practices-for-prompt-engineering](https://claude.com/blog/best-practices-for-prompt-engineering) (Anthropic blog, fetched 2026-06-30) — "Be explicit and clear"; breaking large tasks into smaller discrete chunks consistently produces higher quality results
- [maketocreate.com/claude-md-best-practices-the-complete-2026-guide/](https://maketocreate.com/claude-md-best-practices-the-complete-2026-guide/) (independent, fetched 2026-06-30) — imperative language and concrete-not-vague sections; file:line reference pattern

**Confidence:** ✅ independently-corroborated

---

## Practice 7: Use hooks for rules that must always run — not CLAUDE.md

**Do:** If a rule must fire every single time without exception (e.g., run `eslint` after every file edit, block writes to a `migrations/` folder, send a desktop notification when Claude needs input), implement it as a hook in `.claude/settings.json`, not as a line in CLAUDE.md. Claude can write hooks for you: try "Write a hook that runs eslint after every file edit."

**Why:** CLAUDE.md instructions are advisory — Claude reads them and tries to follow them, but there is no guarantee of strict compliance, especially for vague or conflicting instructions. Hooks are shell scripts that run at fixed lifecycle events (before a tool runs, after a tool runs, etc.) regardless of what Claude decides to do. They are deterministic; CLAUDE.md is not.

**Caveat:** Hooks run as shell commands with the same permissions as your user account. A badly written hook can cause its own damage. Start with read-only or notification hooks before writing hooks that block or modify files.

**Sources:**
- [code.claude.com/docs/en/hooks-guide](https://code.claude.com/docs/en/hooks-guide) (Anthropic, fetched 2026-06-30) — hooks "provide deterministic control over Claude Code's behavior, ensuring certain actions always happen rather than relying on the LLM to choose to run them"
- [code.claude.com/docs/en/memory](https://code.claude.com/docs/en/memory) (Anthropic, fetched 2026-06-30) — "If the instruction is something that must run at a specific point, write it as a hook instead"
- [smartscope.blog/en/generative-ai/claude/claude-code-best-practices-advanced-2026/](https://smartscope.blog/en/generative-ai/claude/claude-code-best-practices-advanced-2026/) (SmartScope, independent, 2026, fetched 2026-06-30) — hooks for absolute requirements; CLAUDE.md provides advisory guidance (the right way to think about the distinction)

**Confidence:** ✅ independently-corroborated

---

## Practice 8: Let Claude interview you before building a complex feature

**Do:** For large or unclear features, start with a single prompt asking Claude to interview you using the `AskUserQuestion` tool before writing any code:

```
I want to build [brief description]. Interview me in detail using the AskUserQuestion tool.

Ask about technical implementation, UI/UX, edge cases, concerns, and tradeoffs. Don't ask obvious questions, dig into the hard parts I might not have considered.

Keep interviewing until we've covered everything, then write a complete spec to SPEC.md.
```

After the spec is written, start a **fresh session** to implement it. The new session has clean context focused entirely on implementation.

**Why:** Claude asks about things you might not have considered — edge cases, tradeoffs, interface questions. The spec becomes the source of truth. Starting a fresh implementation session means the context is not polluted by the entire brainstorming exchange, and you have a written document to reference and hand off.

**Caveat:** This adds time upfront. The return is highest for features with unclear requirements or that span multiple files. Skip it for unambiguous small changes.

**Sources:**
- [code.claude.com/docs/en/best-practices](https://code.claude.com/docs/en/best-practices) (Anthropic, fetched 2026-06-30) — "Let Claude interview you" section with the exact prompt template
- [community.sap.com/t5/artificial-intelligence-blogs-posts/claude-code-best-practices-for-developers/ba-p/14394164](https://community.sap.com/t5/artificial-intelligence-blogs-posts/claude-code-best-practices-for-developers/ba-p/14394164) (SAP Community, independent, fetched 2026-06-30) — Brainstorm → Spec → Plan → Execute → Verify pipeline with separate sessions for spec and implementation

**Confidence:** ✅ independently-corroborated

---

## Practice 9: ⚠️ Never run `--dangerously-skip-permissions` outside an isolated environment

**Do:** Do not use the `--dangerously-skip-permissions` flag (equivalent to `--permission-mode bypassPermissions`) on your real machine or in any directory containing production configs, credentials, or data you cannot restore. For everyday interactive development, use `--permission-mode acceptEdits`, which auto-approves file edits and common filesystem commands without disabling all safety checks. For unattended execution where a classifier makes per-action decisions, use `--permission-mode auto`. Only use `bypassPermissions` inside a container or ephemeral VM.

**Why:** ⚠️ **WARNING.** This flag removes every confirmation prompt. There are documented real incidents from 2025 where Claude executed `rm -rf ~/` — wiping entire home directories — in sessions that did not even use this flag. With the flag enabled, there is no pause, no chance to catch a bad command before it fires. Anthropic released `auto` mode in March 2026 specifically as a safer replacement for unattended pipelines. If you want to use `--dangerously-skip-permissions`, Anthropic's own engineers say: "Run this in a container, not your actual machine."

**Caveat:** Claude Code now has six named permission modes — the full list as of June 2026:

| Mode | What it does |
|------|-------------|
| `default` | Reads only without prompting |
| `acceptEdits` | Reads + file edits + common filesystem commands |
| `plan` | Reads only; no edits (analysis and planning) |
| `auto` | Everything, with per-action classifier checks (research preview) |
| `dontAsk` | Only pre-approved tools (for CI pipelines) |
| `bypassPermissions` | Everything — equivalent to `--dangerously-skip-permissions` |

For most everyday iterative coding work, `acceptEdits` is the practical middle ground. `auto` mode is a research preview requiring Claude Code v2.1.83 or later and specific model eligibility — it is not available to all users. 🕒 **verify live** — the permission mode lineup has expanded; check [code.claude.com/docs/en/permission-modes](https://code.claude.com/docs/en/permission-modes) for current eligibility requirements and the full mode list.

Auto mode aborts a non-interactive (`-p` flag) run if the classifier repeatedly blocks actions — there is no human to fall back to. For fully automated pipelines, you may need to pre-approve specific safe tools with `--allowedTools` rather than relying on auto mode alone.

**Sources:**
- [truefoundry.com/blog/claude-code-dangerously-skip-permissions](https://www.truefoundry.com/blog/claude-code-dangerously-skip-permissions) (TrueFoundry, independent, published 2026-06-08, fetched 2026-06-30) — documented December 2025 `rm -rf ~/` incident; October 2025 incident; safer alternatives including auto mode and PreToolUse hooks
- [ksred.com/claude-code-dangerously-skip-permissions-when-to-use-it-and-when-you-absolutely-shouldnt/](https://www.ksred.com/claude-code-dangerously-skip-permissions-when-to-use-it-and-when-you-absolutely-shouldnt/) (independent, fetched 2026-06-30) — first-hand incident: Claude overwrote a config file with blank values without backup
- [code.claude.com/docs/en/permission-modes](https://code.claude.com/docs/en/permission-modes) (Anthropic, fetched 2026-06-30) — full six-mode permission table including `acceptEdits` and `auto` eligibility requirements
- [claude.com/blog/auto-mode](https://claude.com/blog/auto-mode) (Anthropic, fetched via search 2026-06-30) — official Anthropic announcement of `auto` mode (March 2026)

**Confidence:** ✅ independently-corroborated (multiple independent publishers documenting real incidents; Anthropic docs for mode details)

---

## Practice 10: Use `.claude/rules/*.md` with path selectors to keep per-area rules out of every session

**Do:** Rather than cramming all project rules into a single CLAUDE.md, split domain-specific instructions into separate files under `.claude/rules/`. Add a YAML frontmatter `paths:` block to each rules file so it only loads when Claude works with matching files.

```markdown
---
paths:
  - "src/api/**/*.ts"
---

# API Development Rules
- All API endpoints must include input validation
- Use the standard error response format
```

**Why:** Every line of CLAUDE.md loads on every session, even when irrelevant. Path-scoped rules load only when Claude reads a file matching the pattern — frontend rules load for frontend files, API rules load for API files. This keeps your startup context lean without sacrificing coverage.

**Caveat:** Rules without a `paths:` frontmatter field load unconditionally at launch, just like content in CLAUDE.md. The selective loading only kicks in when you add the frontmatter. Also note: `@path` imports in CLAUDE.md load at launch regardless of path-scoping — they do not benefit from lazy loading. 🕒 **verify live** — the `.claude/rules/` directory and path-scoped frontmatter are relatively recent additions; check the current Claude Code docs for any changes to the schema.

**Sources:**
- [code.claude.com/docs/en/memory](https://code.claude.com/docs/en/memory) (Anthropic, fetched 2026-06-30) — full documentation of `.claude/rules/` directory, `paths:` frontmatter, glob patterns, and symlink support
- [maketocreate.com/claude-md-best-practices-the-complete-2026-guide/](https://maketocreate.com/claude-md-best-practices-the-complete-2026-guide/) (independent, fetched 2026-06-30) — three-tier context system: always-loaded CLAUDE.md / lazy-loaded agents / demand-loaded skills; path-selector pattern described
- [avilevi.co.il/en/blog/manage-claude-code-context-window/](https://www.avilevi.co.il/en/blog/manage-claude-code-context-window/) (independent, fetched 2026-06-30) — project-level vs global skills; install globally only skills used across every project

**Confidence:** ✅ independently-corroborated (vendor docs + 2 independent publishers)

---

## ⚠ PENDING items (no verified fix available)

- **P4 — specific token-count degradation thresholds:** Specific numbers like "147k–152k tokens" were flagged by the Skeptic as not present in the cited source. The 40% threshold from shanraisshan is confirmed. The 147k–152k observation has no surviving verified source in this corpus — removed from the published entry per policy (never guess, never fabricate). ⚠ PENDING: a sourced measurement benchmark
- **P9 — auto mode research preview:** The "research preview" status and exact eligibility requirements were confirmed from the permission-modes page but may change. ⚠ PENDING: verify live after each Claude Code update

---

## CHANGELOG

1. **Research 2026-06-30:** Initial pupil research pass. 10 practices drafted from 9 fetched sources (Anthropic official docs × 3, plus 6 independent publishers). All URLs fetched in session; none recalled from training.
2. **Grading 2026-06-30 — Skeptic KILL (P4):** "147,000–152,000 token degradation observation" attributed to avilevi.co.il — confirmed the source does not contain those numbers. **Removed.** The 40% threshold from shanraisshan remains (confirmed present on that page).
3. **Grading 2026-06-30 — Skeptic KILL (P9):** "32% of developers experienced unintended file modification; 9% reported data loss" attributed to ksred.com — confirmed the source contains no such statistics. **Removed.** First-hand incident narrative (blank config values) remains (confirmed on page).
4. **Grading 2026-06-30 — Skeptic FIX (P4):** "Two failures = /clear" re-attributed from shanraisshan to Anthropic best-practices (the Anthropic source explicitly documents this rule). Applied.
5. **Grading 2026-06-30 — Skeptic FIX (P2):** SAP "Golden Rule" quote softened from verbatim quotation to paraphrase voice (the source page wording differs). Applied.
6. **Grading 2026-06-30 — Skeptic FIX (P7):** SmartScope hooks guidance loosened from a quoted sentence to paraphrase voice (source wording differs from draft). Applied.
7. **Grading 2026-06-30 — Timekeeper FIX (P9):** Permission mode description expanded from 2 modes to the full six-mode table, with `acceptEdits` added as the everyday practical alternative. `auto` mode noted as a research preview with eligibility requirements.
8. **Grading 2026-06-30 — Timekeeper FLAG resolved (P9):** Official Anthropic `auto` mode announcement URL found: [claude.com/blog/auto-mode](https://claude.com/blog/auto-mode). Added as a source; upgrades this from third-party-only to vendor-documented.
9. **Grading 2026-06-30 — Timekeeper FIX (P2):** Added `verify live` caveat noting the plan mode workflow has expanded (Shift+Tab cycle, mode choice after plan approval). Source: Anthropic permission-modes page.

