# Cursor Prompt Engineering — Best Practices (as of 01 Jul 2026)

> Concrete, source-verified best practices for getting better results from Cursor AI — covering .cursor/rules/ files, activation types, Chat vs Agent mode, context tools (@codebase, @docs, @file, @web), and what to avoid.


<!-- Immutable dated snapshot. Researched 2026-06-30, graded 2026-06-30, published 2026-07-01.
     Source tiers: independently-corroborated = 2+ DIFFERENT publishers; vendor-documented =
     official vendor docs only (authoritative, single source). -->

# Cursor Prompt Engineering (as of 01 Jul 2026)

> **Grading note.** A dated snapshot — accurate as of **01 Jul 2026**, frozen here and kept as a
> permanent archive entry. Research-drafted by a pupil (2026-06-30), graded by the 3-lens panel
> (2026-06-30). **0 fabrications.** 4 corrections applied: stale Cursor version numbers removed
> (Cursor is now at 3.9, not 0.47); source conflict on deprecation versions disclosed; overstated
> "5–20 messages" range removed; @docs 404 note surfaced to practice body. 3 items remain ⚠ PENDING.

## How to read the labels
- ✅ **independently-corroborated** — confirmed by 2+ independent publishers
- 📄 **vendor-documented** — official docs only (authoritative, single source)
- ⚠️ **WARNING** — a default that can cost money, break the machine, or remove a safety net
- 🕒 **verify live** — fast-moving (versions/prices/quotas); check the current value

---

## Practice: Migrate from `.cursorrules` to `.cursor/rules/` with `.mdc` files

**Do:** Stop using the single `.cursorrules` file at your project root. Create a `.cursor/rules/` directory instead and put each concern in its own `.mdc` file with YAML frontmatter.

**Why:** Cursor deprecated `.cursorrules` during mid-2025 (around the 0.43–0.45 version series — two third-party sources disagree on the exact version, so treat those numbers as approximate). The old format loads everything globally with no scoping — every rule fires on every request. The new format lets you attach rules only to the files that need them (e.g., only load React patterns when you open a `.tsx` file). The old file still loads as of the current version (3.9 as of June 2026) but will not receive new features and will eventually be removed. 🕒 **verify live** — no official removal date has been announced; check [cursor.com/changelog](https://cursor.com/changelog) before publishing any tutorial that relies on `.cursorrules`.

**Caveat:** Plain `.md` files inside `.cursor/rules/` are silently ignored — only `.mdc` files (and a root-level `AGENTS.md`) are recognized. Double-check the extension; Cursor gives no error when it ignores a `.md` file.

**Sources:**
- [cursor.com/docs/rules](https://www.cursor.com/docs/rules) (Cursor official docs, fetched 2026-06-30)
- [flowql.com/en/blog/guides/cursor-rules-deprecated-libraries/](https://www.flowql.com/en/blog/guides/cursor-rules-deprecated-libraries/) (published 2026-04-24; fetched 2026-06-30) — says deprecated "as of version 0.43"
- [instructa.ai/blog/cursor-ai/everything-you-need-to-know-cursor-rules](https://www.instructa.ai/blog/cursor-ai/everything-you-need-to-know-cursor-rules) (published 2025-02-07; fetched 2026-06-30) — says deprecated "from 0.45"; these two sources disagree on the exact version number
- [cursor.com/changelog](https://cursor.com/changelog) (Cursor changelog, fetched 2026-06-30) — confirms current version is 3.9 (June 22, 2026); the 0.43–0.47 era was 2025

**Confidence:** ✅ independently-corroborated (official docs + 2 independent third-party sources)

---

## Practice: Pick the right rule activation type — don't make everything `alwaysApply: true`

**Do:** For each `.mdc` rule file, choose the appropriate activation mode using three frontmatter fields (`alwaysApply`, `description`, `globs`):

| Goal | Set these fields |
|------|-----------------|
| Must load every request (e.g., "always use TypeScript strict mode") | `alwaysApply: true` |
| Load when certain files are open (e.g., React patterns for `.tsx`) | `globs: ["src/**/*.tsx"]` |
| Agent decides relevance by description (e.g., Stripe integration guide) | `description: "..."` |
| Load only when you explicitly ask (`@rule-name` in chat) | leave all three blank/false |

**Why:** Every token in an always-on rule is included in every single AI request. If you put 20 rules on `alwaysApply: true` you burn thousands of tokens before the AI has even read your question, which shrinks how much of your code it can see and increases cost. One guide measured "2,000+ tokens per request" for 20 always-on rules.

**Caveat:** The `alwaysApply` field overrides `globs` and `description` — if `alwaysApply: true`, the other two are ignored. Test glob patterns against your actual file paths; `{src,lib}/**/*.ts` brace syntax is reported as unreliable. Use YAML list syntax instead:

```yaml
# Avoid — brace syntax reported unreliable:
globs: "{src,lib}/**/*.ts"

# Use this instead:
globs:
  - "src/**/*.ts"
  - "lib/**/*.ts"
```

**Sources:**
- [cursor.com/docs/rules](https://www.cursor.com/docs/rules) (Cursor official docs, fetched 2026-06-30)
- [techsy.io/en/blog/cursor-rules-guide](https://techsy.io/en/blog/cursor-rules-guide) (published 2026-06-13; fetched 2026-06-30)
- [vibecodingacademy.ai/blog/cursor-rules-complete-guide](https://www.vibecodingacademy.ai/blog/cursor-rules-complete-guide) (published 2026-05-01; fetched 2026-06-30)

**Confidence:** ✅ independently-corroborated (official docs + 2 independent third-party sources)

---

## Practice: Keep rules short and actionable — under 500 lines per file, under 200 words for always-on rules

**Do:** Write rules as dense directives, not paragraphs of explanation. Reference file paths instead of pasting file contents. Split large rule files into smaller focused ones (typical project: 5–8 rule files). Apply the "rule of three" — only codify a pattern after the AI has failed at it three times.

**Why:** AI models need directives, not persuasion. A rule that says "write clean, readable code" gives the AI nothing concrete to act on. A rule that says "name boolean variables `is_*` or `has_*`; never use `flag` or `b`" is unambiguous. Vague rules waste tokens without improving output.

**Caveat:** Cursor's own docs say to stay under 500 lines and avoid "documenting common commands" or "duplicating existing codebase documentation." Do not copy-paste your entire style guide — link or reference it instead, to prevent the rule from going stale when the guide changes.

**Sources:**
- [cursor.com/docs/rules](https://www.cursor.com/docs/rules) (Cursor official docs, fetched 2026-06-30)
- [techsy.io/en/blog/cursor-rules-guide](https://techsy.io/en/blog/cursor-rules-guide) (published 2026-06-13; fetched 2026-06-30)
- [vibecodingacademy.ai/blog/cursor-rules-complete-guide](https://www.vibecodingacademy.ai/blog/cursor-rules-complete-guide) (published 2026-05-01; fetched 2026-06-30)

**Confidence:** ✅ independently-corroborated

---

## Practice: Use the right context tool — `@file` when you know the file, `@codebase` when you don't

**Do:** Prefer explicit `@file` or `@folder` mentions when you know exactly which files are relevant. Use `@codebase` for exploratory questions when you are not sure which files matter. Use `@docs` for external library documentation (see caveat). Use `@web` for real-time information (current package versions, recent API changes).

**Why:** Each `@` tool works differently. `@codebase` runs a probabilistic semantic search (using vector embeddings) across your entire indexed project — it is powerful but not guaranteed to find everything, especially if naming is inconsistent. `@file` pins an exact file and is reliable. `@docs` lets Cursor reference current library docs rather than the AI's (potentially stale) training data — especially important for newer or rapidly-changing libraries. `@web` fetches live web results and should be used sparingly for factual lookups.

**Caveat:** Including too many `@file` mentions clutters context with irrelevant code and can confuse the AI about what is important. `@codebase` uses vector embeddings — if your function is named "Login" but the code says "SessionCreation," semantic search may miss it. When `@codebase` fails on critical files, fall back to explicit `@file` references. 🕒 **verify live** — the Cursor official docs page for `@docs` indexing returned a 404 at the time of research (2026-06-30); the `@docs` workflow is described in third-party sources only. Verify the current `@docs` feature status at [cursor.com/docs](https://www.cursor.com/docs) before relying on it.

**Sources:**
- [datalakehousehub.com/blog/2026-03-context-management-cursor/](https://datalakehousehub.com/blog/2026-03-context-management-cursor/) (published 2026-03; fetched 2026-06-30)
- [github.com/murataslan1/cursor-ai-tips/blob/main/tips/context-management.md](https://github.com/murataslan1/cursor-ai-tips/blob/main/tips/context-management.md) (fetched 2026-06-30) — confirms @Files exact content; @Codebase probabilistic search; Login/SessionCreation semantic-miss example

**Confidence:** ✅ independently-corroborated (two independent third-party sources; official Cursor docs URL for @docs was 404 at research time — see caveat)

---

## Practice: Write Composer/Agent prompts as scoped work orders, not open-ended requests

**Do:** Structure Composer and Agent mode prompts to include: (1) explicit goal, (2) files in scope via `@file` or `@folder`, (3) what is out of scope, and (4) a verifiable "done" condition (a test command, a lint check, or a grep search). Example:

> "Add an `exportToCsv()` function to `@src/reports/ReportService.ts`. Do not modify any other files. Done when `npm test -- ReportService` passes."

**Why:** Agent mode can edit multiple files autonomously and run terminal commands. Vague prompts ("make this better") give the agent no stopping point and can result in widespread unintended changes. Specific, checkable prompts let the agent know when it has succeeded.

**Caveat:** Use Composer/Agent for multi-file changes. For a single-line fix, inline edit (Ctrl+K on Windows/Linux, Cmd+K on Mac) is faster. For exploratory questions, use Chat. Using Agent for everything wastes compute and makes diffs harder to review. The Cursor blog explicitly recommends this task-routing approach.

**Sources:**
- [cursor.com/blog/agent-best-practices](https://cursor.com/blog/agent-best-practices) (Cursor blog, published 2026-01-09; fetched 2026-06-30)
- [sureprompts.com/blog/cursor-ai-prompting-guide](https://sureprompts.com/blog/cursor-ai-prompting-guide) (published 2026-04-20; fetched 2026-06-30)

**Confidence:** ✅ independently-corroborated

---

## Practice: Start a new chat after completing a logical unit of work — do not let conversations grow indefinitely

**Do:** Open a fresh chat session when you finish a feature or task, when the agent starts repeating mistakes, or when you shift to a clearly different concern. Before closing, ask the agent to summarize what was built if you want to carry forward context.

**Why:** Every message adds to the context window. After many turns, earlier instructions get diluted or summarized away. Cursor's own blog warns that "long conversations can cause the agent to lose focus" and that accumulated noise can cause the agent to "switch to unrelated tasks." Cursor provides `@Past Chats` as a way to reference earlier conversation summaries without copy-pasting entire histories.

**Caveat:** Cursor provides `@Past Chats` to reference earlier conversation summaries without copy-pasting long chat logs.

**Sources:**
- [cursor.com/blog/agent-best-practices](https://cursor.com/blog/agent-best-practices) (Cursor blog, published 2026-01-09; fetched 2026-06-30) — "Long conversations can cause the agent to lose focus" and "switch to unrelated tasks"
- [datalakehousehub.com/blog/2026-03-context-management-cursor/](https://datalakehousehub.com/blog/2026-03-context-management-cursor/) (published 2026-03; fetched 2026-06-30) — confirms starting new chat sessions when switching topics

**Confidence:** ✅ independently-corroborated

---

## Practice: Give the agent verifiable goals — tests, linters, and typed languages act as automatic feedback signals

**Do:** Before asking Agent to implement something, ensure you have: a typed language (TypeScript, Python with type hints) configured, a linter (ESLint for JavaScript, Ruff for Python), and at least a stub test file. Then add to your prompt: "Write tests first, then implementation, then run the tests and fix until they pass."

**Why:** The agent can run terminal commands and read their output. Type errors, lint failures, and test failures are signals the agent can act on without you needing to explain the problem. Without these signals the agent generates code that looks correct but has hidden bugs — and has no way to self-correct.

**Caveat:** ⚠️ **WARNING — YOLO mode.** Cursor has a setting (sometimes called "YOLO mode") that lets the agent run terminal commands without asking permission first. Despite the casual name, this setting disables all command-approval prompts — it can run `rm` commands, database migrations, and deploy scripts without pausing. Enable it only after you understand which commands your project's build and test tools run, and restrict it explicitly in a rule: "only run test and build commands — never run database migrations or deploy commands without user confirmation."

**Sources:**
- [cursor.com/blog/agent-best-practices](https://cursor.com/blog/agent-best-practices) (Cursor blog, published 2026-01-09; fetched 2026-06-30)
- [builder.io/blog/cursor-tips](https://www.builder.io/blog/cursor-tips) (builder.io, published 2025-03-11; fetched 2026-06-30) — confirms YOLO mode runs commands without per-command permission; diff approvals still required
- [getstream.io/blog/cursor-ai-large-projects/](https://getstream.io/blog/cursor-ai-large-projects/) (getstream.io, published 2025-03-05; fetched 2026-06-30)

**Confidence:** ✅ independently-corroborated

---

## Practice: Commit `.cursor/rules/` to version control and treat rule files like code

**Do:** Include the `.cursor/rules/` directory in your git repository. Review rule changes in pull requests. Write descriptive commit messages when updating rules. Document breaking rule changes (e.g., "changed naming convention from camelCase to snake_case") so teammates know what changed.

**Why:** Rule files are the persistent memory of your project's AI configuration. If they live only on one developer's machine, every new team member and CI environment gets inconsistent AI behavior. Versioned rules also make it possible to revert a bad rule change, just like reverting a bad code change.

**Caveat:** Personal preferences (your own keybindings, your preferred verbosity level) belong in User Rules (Cursor Settings), not in project-level `.cursor/rules/` files. Committing personal preferences forces them on every team member.

**Sources:**
- [vibecodingacademy.ai/blog/cursor-rules-complete-guide](https://www.vibecodingacademy.ai/blog/cursor-rules-complete-guide) (published 2026-05-01; fetched 2026-06-30)
- [cursor.com/docs/rules](https://www.cursor.com/docs/rules) (Cursor official docs, fetched 2026-06-30)

**Confidence:** ✅ independently-corroborated (official docs confirm version control; third party corroborates team workflow rationale)

---

## Practice: Review every diff before accepting — Agent output can look right while being wrong

**Do:** Read every diff the agent produces before clicking "Accept." Pay attention to files you did not expect to be modified. Use Cursor's built-in Review mode for larger change sets, and Bugbot for automated PR analysis when available. Cursor creates automatic checkpoints before significant changes (visible in the chat timeline) — you can roll back without affecting your Git history.

**Why:** AI code generation is fast and often correct at a surface level, but subtle bugs — wrong variable names, missing null checks, incorrect logic — can look plausible in a quick glance. Cursor's own documentation states that "AI-generated code can look right while being subtly wrong." The faster the agent works, the more important your review process becomes.

**Caveat:** Cursor's automatic checkpoints are a safety net, not a substitute for review.

**Sources:**
- [cursor.com/blog/agent-best-practices](https://cursor.com/blog/agent-best-practices) (Cursor blog, published 2026-01-09; fetched 2026-06-30)
- [ellenox.com/post/mastering-cursor-ai-advanced-workflows-and-best-practices](https://www.ellenox.com/post/mastering-cursor-ai-advanced-workflows-and-best-practices) (published 2025-06-04, updated 2025-07-03; fetched 2026-06-30)

**Confidence:** ✅ independently-corroborated

---

## ⚠ PENDING items (no verified fix available)

- **Practice 1 — `.cursorrules` removal timeline:** No official removal date has been announced by Cursor. 🕒 verify live against [cursor.com/changelog](https://cursor.com/changelog) on each refresh.
- **Context tool — `@docs` official docs URL:** The Cursor official docs URL for `@docs` indexing returned a 404 at research time (2026-06-30). The feature is described in third-party sources only. 🕒 verify live.
- **Exact token-per-word cost and context window size:** Third-party estimates used; not sourced from Cursor official docs this run. 🕒 verify live.

---

## CHANGELOG

1. **Research 2026-06-30:** Eight practices sourced from official Cursor docs, Cursor blog, and six independent third-party publishers. All URLs fetched this run; none recalled from training.
2. **Grading 2026-06-30 — Timekeeper KILL (P1 version numbers):** The draft stated "deprecated as of version 0.43 and introduced in version 0.45... still works as of version 0.47." Cursor is now at version 3.9 (June 22, 2026). The "still works as of 0.47" phrasing was actively misleading. Removed all three version numbers from the body. Replaced with: "deprecated during mid-2025 (around the 0.43–0.45 version series — two sources disagree); still loads as of the current version (3.9 as of June 2026)." Applied.
3. **Grading 2026-06-30 — Skeptic FIX (P1 conflicting sources):** flowql.com says "deprecated as of 0.43"; instructa.ai says "deprecated from 0.45." Sources disagree. Disclosed in practice body rather than presenting a confident single version number. Applied.
4. **Grading 2026-06-30 — Skeptic FIX (P6 new-chat numbers):** "Multiple independent sources suggest starting fresh every 5–20 messages" — the cited getstream.io source says "5–7 steps in a single composer window," a different concept. Removed the specific "5–20 messages" range from the body. The general principle (start fresh after a unit of work) remains well-sourced. Applied.
5. **Grading 2026-06-30 — Timekeeper FIX (P4 @docs sourcing):** Added inline caveat in the @docs guidance noting that the official Cursor docs URL for this feature returned a 404 at research time. Surfaced from the Held section to the practice body. Applied.
6. **Grading 2026-06-30 — Timekeeper FIX (P1 verify live):** Added `verify live` label in the practice body for the `.cursorrules` removal timeline (was only in the Held section). Applied.

