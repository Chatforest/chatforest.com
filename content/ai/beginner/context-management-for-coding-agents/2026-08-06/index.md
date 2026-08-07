---
title: "Context Management for AI Coding Agents — Beginner Guide (as of 06 Aug 2026)"
date: 2026-08-06
snapshot_date: 2026-08-06
topic: context-management-for-coding-agents
track: beginner
audience: "people new to AI"
description: "A plain-language guide to how AI coding agents (Claude Code, OpenAI Codex CLI, Google Gemini CLI) fill up, compress, and lose track of their working memory — including the cost traps that quietly drain a budget. Every fact is carried over unchanged from the 2026-08-06 technical entry."
content_type: "Best Practice"
categories: ["Claude Code", "OpenAI Codex CLI", "Gemini CLI", "AI Agents", "LLM Fundamentals"]
tags: ["context-window", "context-rot", "compaction", "prompt-caching", "rag", "sub-agents", "claude-code", "codex-cli", "gemini-cli", "claude-md", "agents-md", "gemini-md"]
last_refreshed: 2026-08-06
graded_by: "RingS panel (Skeptic/Beginner/Timekeeper) + sensei, 2026-08-06/07"
grading_result: "Re-leveled from the 2026-08-06 technical entry (0 fabrications after correction; 4 Skeptic KILLs and roughly 40 further FIX/FLAG corrections applied during that grading pass). This beginner rewrite adds no new facts, numbers, or sources — see the technical snapshot's own CHANGELOG for the full correction list."
---

<!-- This file lands at content/ai/beginner/context-management-for-coding-agents/2026-08-06/index.md
     and is an IMMUTABLE dated snapshot re-leveled from the 2026-08-06 best-practices entry.
     Facts, numbers, and source URLs are unchanged from that entry. Only language, structure,
     and framing have been adjusted for readers new to AI. Once published it is never edited —
     a refresh is a NEW <snapshot-date> dir.
     Source tiers: independently-corroborated = 2+ DIFFERENT publishers; vendor-documented =
     official vendor docs only (authoritative, single source). -->

# Context Management for AI Coding Agents — Beginner Guide (as of 06 Aug 2026)

> **What this is.** A dated, fact-checked guide re-written for people who are new to AI
> coding agents. Every claim below already passed a 3-lens grading panel (Skeptic,
> Beginner, Timekeeper) on the 2026-08-06 technical entry — this version changes the
> *words*, not the *facts*. **0 fabrications.** Items that could not yet be fully verified
> are marked **⚠ PENDING** — this guide never guesses.

## What the labels mean

- ✅ **independently-corroborated** — confirmed by 2 or more independent publishers
- 📄 **vendor-documented** — from the tool's own official docs (authoritative, one source)
- ⚠️ **WARNING** — a default that can cost you real money, silently lose your work, or remove a safety net
- 🕒 **verify live** — this detail changes fast (versions, prices, quotas); look it up yourself before relying on it

---

## Before you start

This guide assumes you already have **Claude Code**, **OpenAI Codex CLI**, or **Google
Gemini CLI** installed and have run at least one session. (If you haven't installed a
coding agent yet, look for the separate "Running AI Agents on Ubuntu" beginner guide
first — this entry is only about managing a session once you're already inside one.)

**What is a "context window"?** Every time you send a message to an AI coding agent, the
whole conversation so far — your messages, its replies, every file it read, every command
output it saw — has to be re-sent to the model along with your new message. There's a hard
size limit on how much text (measured in **tokens**, roughly ¾ of a word each) can fit in
that one request. That limit is the **context window** — think of it as the agent's
short-term working memory for the current session. It is *not* the same as the model's
training data, and it does **not** carry over automatically between sessions.

Read **Part 0** first, no matter which agent you use — it explains ideas common to all
three. Then jump to the part for your specific tool: **Part 1** Claude Code, **Part 2**
Codex CLI, **Part 3** Gemini CLI.

---

## Part 0 — Foundations (apply to any coding agent)

These ideas hold true regardless of which company made your CLI tool.

---

### Practice 1: Know what's actually filling up your context window ✅ 🕒

**Do:** The context window for one model call includes: the system prompt, all the tool
definitions the agent has available, every prior message and file/command output shown so
far, and even the model's own hidden "thinking" (its internal reasoning before it answers,
which you don't normally see but which still counts against the budget). It is *not*
unlimited memory across a whole project — it resets or gets compressed per session.

As of 06 Aug 2026, current models used by coding agents typically offer 200,000 to
1,000,000+ tokens of window: Anthropic's Claude Sonnet 5 and Opus 5 default to a
**1,000,000-token** window (older Sonnet 4.5/Haiku-class models are capped at 200,000);
Anthropic's newest, most coding-capable model, **Claude Fable 5** (generally available 9
Jun 2026, with a restricted sibling called **Claude Mythos 5**), also ships the same
1,000,000-token window; OpenAI's GPT-5.6-series models list a **1,050,000-token** window
with 128,000 max output tokens; Google's Gemini 3-series models (`gemini-3.1-pro-preview`,
`gemini-3-flash-preview`, `gemini-3.1-flash-lite`) list **1,000,000-token input / 64,000
output**. 🕒 These figures change between model releases — check the vendor's own model
page before you plan a big session.

**Why it matters / what goes wrong:** If you don't know what's filling up your budget, you
can't explain why a session suddenly starts acting "dumber" or refuses to keep going. It's
usually not a bug — it's the window filling up with old command output, file contents, and
invisible reasoning you never see.

**Caveat:** These are the model's own maximum limits, not what your specific CLI tool
actually lets you use in practice — see the next practice.

**Sources:** [Claude Platform Docs — Context windows](https://platform.claude.com/docs/en/build-with-claude/context-windows) (fetched 06 Aug 2026) · [Claude Platform Docs — What's new in Claude Sonnet 5](https://platform.claude.com/docs/en/about-claude/models/whats-new-sonnet-5) (fetched 06 Aug 2026) · [Claude Platform Docs — Pricing](https://platform.claude.com/docs/en/about-claude/pricing) (fetched 06 Aug 2026, Fable 5/Mythos 5 pricing and windows) · [developers.openai.com — Models (GPT-5.6 series)](https://developers.openai.com/api/docs/models) (fetched 06 Aug 2026) · [Google AI for Developers — Gemini 3](https://ai.google.dev/gemini-api/docs/gemini-3) (fetched 06 Aug 2026) · [Google AI for Developers — Long context](https://ai.google.dev/gemini-api/docs/long-context) (updated 22 Jun 2026, fetched 06 Aug 2026)

**Confidence:** 📄 vendor-documented (each vendor documents only its own numbers)

---

### Practice 2: Plan for what you can actually use, not the advertised maximum ✅ 🕒

**Do:** Treat the number on a model's marketing page as a ceiling, not a working budget.
Coding-agent CLIs typically hold back a chunk of the window for their own output and
safety margin, and accuracy on find-the-right-detail tasks tends to fall off well before
the hard limit. One concrete example: OpenAI's own specs list a 1,050,000-token window for
the GPT-5.6 series, but Codex CLI itself caps usable input at **272,000 tokens** inside a
400,000-token session budget (128,000 held back for output, plus a 5% safety buffer) —
roughly a quarter of the advertised maximum. (This cap was tightened from 372,000 tokens on
18 Jul 2026 as a billing fix, not because the model got weaker — the model still has its
full 1,050,000-token window.) Separately, Chroma Research — a company that sells retrieval
tools, so it has a commercial interest in "big windows don't work as advertised" being
true — tested 18 models from Anthropic, OpenAI, Google, and Alibaba and found that
performance "varies significantly as input length changes, even on simple tasks." (The
study does not publish one single "shortfall percentage," so don't repeat one — the
takeaway is simply that accuracy degrades well before you hit the wall.) Budget your
sessions to the smaller, real number, and start compressing well before you approach it.

**Why it matters / what goes wrong:** "This model has a 1-million-token window" does not
mean you can safely fill it with a million tokens of your repository and expect reliable
answers. Both the tool and the model behave much better with headroom left over.

**Caveat:** 🕒 verify live — the exact usable fraction is tool- and task-specific and
changes fast as vendors tune their defaults. Treat any specific percentage as a snapshot,
not a permanent ratio.

**Sources:** [Codex Knowledge Base — "The Context Window Gap"](https://codex.danielvaughan.com/2026/07/20/context-window-gap-codex-cli-gpt56-advertised-vs-effective-budget-compaction-strategy/) (20 Jul 2026, independent blog, fetched 06 Aug 2026) · [developers.openai.com — Models](https://developers.openai.com/api/docs/models) (fetched 06 Aug 2026) · [GitHub issue #32486 — Codex context-window billing metadata](https://github.com/openai/codex/issues/32486) (fetched 06 Aug 2026) · [Chroma Research — Context Rot](https://www.trychroma.com/research/context-rot) (14 Jul 2025, fetched 06 Aug 2026)

**Confidence:** ✅ independently-corroborated

---

### Practice 3: Expect the agent to "forget" things in the middle of a long session ✅

**What is "context rot"?** It's the documented, measured pattern that AI models don't use
every part of a long conversation equally well — instructions or facts buried in the
*middle* of a long block of text are more likely to get missed than ones near the start or
end. This is sometimes called "lost in the middle."

**Do:** Put your most important instructions and facts near the **start or end** of what
you send, not buried in the middle of a long dump of file contents or command output. Don't
assume a bigger context window fixes this by itself. Chroma's July 2025 study of 18 models
(including Claude, GPT, Gemini, and Qwen families) found performance varies significantly
as input length grows "even on simple tasks," and — surprisingly — that a shuffled,
disorganized context sometimes performed *better* than a neatly organized one. Anthropic's
own engineering guidance (29 Sep 2025) independently describes the same effect and
recommends curating what goes into context rather than maximizing how much you stuff in. A
2025 research paper (arXiv, Oct 2025) suggests this "forgetting the middle" pattern is a
side effect of how models are trained, not a simple bug — meaning it probably won't just
disappear as models get bigger.

**Why it matters / what goes wrong:** If your agent seems to "forget" an instruction you
gave 40 messages ago, even though it's technically still there in the transcript, that's
not a hallucination bug — it's a documented, measured pattern. Repeat critical rules close
to the end of the context (right before you ask the model to act) instead of assuming "I
said it once, so it's covered."

**Caveat:** The exact shape of this effect is still an active research area, not a settled
constant — it differs by task type. Treat it as a real, documented pattern whose precise
boundaries aren't yet pinned down by a single agreed-upon source.

**Sources:** [Chroma Research — Context Rot](https://www.trychroma.com/research/context-rot) (14 Jul 2025, fetched 06 Aug 2026) · [Anthropic Engineering — Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) (29 Sep 2025, fetched 06 Aug 2026) · [arXiv 2510.10276 — Lost in the Middle: An Emergent Property from Information Retrieval Demands in LLMs](https://arxiv.org/abs/2510.10276) (11 Oct 2025, fetched 06 Aug 2026)

**Confidence:** ✅ independently-corroborated

---

### Practice 4: Understand "compaction" — the summary that saves a session, but loses detail ✅ ⚠️

**What is compaction?** When a session gets close to filling its context window, the agent
asks the model itself to write a condensed summary of everything so far, and that summary
*replaces* the full history. This is how long agent sessions keep going instead of hitting
a hard wall.

**Do:** Let compaction happen rather than hard-stopping — but know it is **lossy by
design**. Anthropic's own compaction guidance and Claude Cookbook describe the pattern:
the model produces a high-fidelity summary that keeps "architectural decisions and
unresolved issues" but discards redundant/verbose detail. An independent analysis of
OpenAI's Codex CLI describes the same core pattern and calls it "inherently lossy but
predictable." Both agree: compaction is the standard fix for "the conversation is about to
hit the wall," and both are explicit that it is not a free operation.

**Why it matters / what goes wrong:** ⚠️ After your agent auto-compacts, don't assume
everything you said earlier survived intact. A summary is a lossy rewrite generated by the
same model that might already be confused — it can drop a constraint you gave 100 messages
ago, or "smooth over" a detail into something that sounds plausible but isn't what you
actually said (a compressed hallucination). **Re-state hard constraints** (e.g. "never
touch the payments module," "always run tests before committing") right after any
compaction event. Anything you truly cannot afford to lose belongs in a file on disk (a
CLAUDE.md/AGENTS.md/GEMINI.md file, or a git commit), not just in chat history.

**Caveat:** Vendors differ on exactly when compaction triggers and whether it's automatic
or manual (e.g., a `/compact` command). Some tools let you supply custom instructions to
steer what a compaction keeps — worth doing for anything safety- or correctness-critical.
🕒 verify live against your specific tool's docs.

**Sources:** [Claude Platform Docs — Context windows](https://platform.claude.com/docs/en/build-with-claude/context-windows) (fetched 06 Aug 2026) · [Claude Cookbook — Context engineering: memory, compaction, and tool clearing](https://platform.claude.com/cookbook/tool-use-context-engineering-context-engineering-tools) (fetched 06 Aug 2026) · [Codex Knowledge Base — "The Context Window Gap"](https://codex.danielvaughan.com/2026/07/20/context-window-gap-codex-cli-gpt56-advertised-vs-effective-budget-compaction-strategy/) (20 Jul 2026, independent blog, fetched 06 Aug 2026)

**Confidence:** ✅ independently-corroborated

---

### Practice 5: Send big, messy exploration work to a subagent — bring back only the answer ✅

**What is a subagent?** A subagent is a mini-agent the main agent can spin up that gets its
*own*, separate context window. It does its work (searching a codebase, reading many
files, trying failed approaches), then reports back a short, condensed result — often just
a few hundred to ~2,000 tokens — instead of dumping its entire scratch work into your main
conversation.

**Do:** When a task involves a lot of "burn context to figure something out" work, delegate
it to a subagent rather than doing it in your main conversation. This is a general design
pattern, not one company's trick: Anthropic's own guidance describes subagents "each
explor[ing] extensively but return[ing] condensed summaries"; an independent write-up on
Claude Code subagents describes the coordinator getting "a concise resulting context...
included into the original conversation" instead of a full transcript; and a separate 2026
academic paper analyzing Claude Code's architecture identifies subagent delegation as one
of the system's core context-management mechanisms.

**Why it matters / what goes wrong:** If you ask an agent to "explore the whole codebase
and figure out where X is handled" in your main conversation, that exploration and all its
dead ends can burn a huge fraction of your context budget before the real task even
starts. Delegating that exploration to a subagent keeps your main session's budget free for
the actual work — at the cost of some duplicated setup for each subagent you spin up.

**Caveat:** Subagents cost real tokens (and, on paid plans, real money) of their own —
isolation trades "one big context" for "several separate contexts," which is a net win for
focus but is not free. And the condensed summary a subagent returns is itself subject to
the same lossy-compaction risk described above — a bad summary from a subagent can quietly
misinform the parent agent.

**Sources:** [Anthropic Engineering — Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) (29 Sep 2025, fetched 06 Aug 2026) · [Rich Snapp — Context Management with Subagents in Claude Code](https://www.richsnapp.com/article/2025/10-05-context-management-with-subagents-in-claude-code) (05 Oct 2025, independent, fetched 06 Aug 2026) · [arXiv 2604.14228 — Dive into Claude Code: The Design Space of Today's and Future AI Agent Systems](https://arxiv.org/abs/2604.14228) (v2, 02 Jul 2026, fetched 06 Aug 2026)

**Confidence:** ✅ independently-corroborated

---

### Practice 6: Understand prompt caching — a cost/speed trick, and a fragile one ✅ 🕒

**What is prompt caching?** If part of your prompt repeats across calls (a large system
prompt, a loaded repo, a long conversation history), the vendor can "cache" that prefix so
it doesn't have to be reprocessed at full price every single turn — as long as later
requests send an **identical** copy of that text.

**Do:** Turn on caching for any prompt prefix that repeats. Both Anthropic and OpenAI use
the same basic pattern: if a later request sends an identical prefix up to a cache
checkpoint, the cached version is reused at a steep discount; if even **one byte differs**
before that point, the match fails and everything from there is billed and processed at
full price. As of 06 Aug 2026 🕒 verify live: on Anthropic's API, cache *reads* cost about
10% of the normal input price, 5-minute-warm cache *writes* cost about 1.25x the normal
input price, and a 1-hour-warm option costs about 2x; on OpenAI's newer models, cache
writes for GPT-5.6+ cost 1.25x the uncached rate while reads stay discounted, with cache
retention of "at least 30 minutes." Anthropic also confirms Claude's 1M-token window
(Claude 4.6 and later) is billed at flat, standard per-token pricing with no extra "long
context" surcharge — caching, not window size, is the main lever on your bill. The minimum
amount of text needed to be cacheable ranges roughly **512 to 4,096 tokens** depending on
the model (512 for the current top tier — Opus 5, Fable 5, Mythos 5 — up to 4,096 for older
models; OpenAI's minimum is a flat 1,024 tokens).

**Why it matters / what goes wrong:** Prompt caching is a **cost and speed** optimization —
it does not make an agent "remember" anything beyond its normal context window. Any edit
anywhere in the cached prefix (even fixing a typo in a system prompt) breaks the cache for
everything after it, silently making your next request slower and pricier than expected
until the cache rebuilds.

**Caveat:** 🕒 verify live — cache lifetimes, minimum sizes, and pricing multipliers are
vendor- and model-specific and change often. Don't rely on any number here for a real cost
estimate without re-checking.

**Sources:** [Claude Platform Docs — Prompt caching](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) (fetched 06 Aug 2026) · [Claude Platform Docs — Pricing](https://platform.claude.com/docs/en/about-claude/pricing) (fetched 06 Aug 2026) · [developers.openai.com — Prompt caching](https://developers.openai.com/api/docs/guides/prompt-caching) (fetched 06 Aug 2026)

**Confidence:** 📄 vendor-documented (Anthropic and OpenAI each document only their own product)

---

### Practice 7: Decide "search the repo" vs. "just read the whole thing" based on repo size, not habit ✅

**What is RAG?** RAG (Retrieval-Augmented Generation) means fetching only the most relevant
chunks of a larger set of files instead of loading everything into context.

**Do:** For small-to-medium repos, or questions that genuinely need to see many files at
once (a rename that touches many call sites, understanding a whole subsystem), loading the
relevant files directly tends to preserve structure (imports, types, call sites) that
chunked retrieval can lose. For large repos, or narrow factual questions ("where is X
defined"), search-first (index the repo, fetch only the relevant chunks) avoids paying for
code the model doesn't need — and avoids diluting the context with irrelevant files, which,
per context rot above, can itself hurt accuracy. Google's own Gemini long-context guidance
recommends putting relevant information directly in context rather than filtering it out
when the window can hold it. An independent source (Redis engineering blog) confirms that
attention cost grows roughly with the *square* of the input length ("doubling your context
length roughly quadruples the computational requirements"), and that a hybrid
"retrieve-then-load-full-context" pattern is increasingly common in production.

**Why it matters / what goes wrong:** There's no single right answer to "should my agent
search the codebase or just read the whole thing?" — it depends on whether the repo fits
comfortably in the budget you're willing to spend. When in doubt for a large repo, start
with targeted reads/searches rather than dumping the whole tree into context "to be safe" —
a full-context dump is often slower, pricier, and (per context rot) not actually more
reliable.

**Caveat:** This is a fast-evolving, debated area — treat the guidance above as the
trade-off consensus as of mid-2026, not a settled law. (An earlier draft of this practice
cited a specific RAG "recall" percentage; on re-checking the source, that figure measured
something else entirely — how often two different approaches agreed with each other, not
RAG's accuracy — and has been removed rather than republished uncorrected.)

**Sources:** [Google AI for Developers — Long context](https://ai.google.dev/gemini-api/docs/long-context) (updated 22 Jun 2026, fetched 06 Aug 2026) · [Redis — RAG vs large context window: the real trade-offs for AI apps](https://redis.io/blog/rag-vs-large-context-window-ai-apps/) (06 Feb 2026, updated 01 Jun 2026, fetched 06 Aug 2026)

**Confidence:** ✅ independently-corroborated

---

### Practice 8: ⚠️ Long sessions with big contexts can quietly cost real money

**Do:** Attention cost scales roughly with the *square* of your context length — cost
grows much faster than the context itself, not in direct proportion. And every tool
result, file read, and prior turn stays billable until it's compacted or cleared. A
long-running session on a large-context model can rack up cost far faster than a naive
"tokens times price" estimate suggests — especially if the agent re-reads large files or
re-fetches the same web page repeatedly instead of reusing what's already in context.
Anthropic's own API docs warn that a single fetched web page can consume tens of thousands
of tokens (their own numbers: about 2,500 tokens for an average 10 KB page, about 25,000
for a 100 KB doc page, about 125,000 for a 500 KB PDF) and offer a `max_content_tokens`
setting specifically to guard against "inadvertently fetching large content that would
consume excessive tokens." Set a budget/cap where your tool offers one, watch token-usage
output as a session runs, and compact or start fresh proactively — don't wait for a cost
surprise or a hard error.

**Why it matters / what goes wrong:** ⚠️ This is the "this can cost you real money" flag
for the whole topic: an agent left running unattended in a big-context session — especially
one that keeps re-reading the same large files or fetching the same pages — can rack up a
bill much faster than a short back-and-forth chat would suggest. Don't assume "I have a
1-million-token window" means "I can leave this running all day for free." Check your
provider's usage dashboard, not just your intuition.

**Caveat:** 🕒 verify live — exact per-token costs, free-tier allowances, and safety-guard
settings like `max_content_tokens` are vendor- and model-specific and change frequently.

**Sources:** [Claude Platform Docs — Pricing (web fetch tool, code execution, long-context pricing)](https://platform.claude.com/docs/en/about-claude/pricing) (fetched 06 Aug 2026) · [Redis — RAG vs large context window: the real trade-offs for AI apps](https://redis.io/blog/rag-vs-large-context-window-ai-apps/) (06 Feb 2026, updated 01 Jun 2026, fetched 06 Aug 2026) — independently corroborates the quadratic-cost claim

**Confidence:** ✅ independently-corroborated

---

## Part 1 — Claude Code

> All slash commands below (`/compact`, `/clear`, `/context`, `/memory`, `/model`,
> `/resume`, etc.) are typed **inside the running `claude` interactive session** — not at
> the plain Ubuntu bash prompt. Typing `/compact` directly into bash gets you a "no such
> file or directory" error, because bash reads a leading `/` as a file path.

### Practice: See what's already loaded before you type your first message 📄

**Do:** Before your first prompt, Claude Code has already loaded: the system prompt, every
applicable **CLAUDE.md** file (a special always-loaded instructions file — managed policy,
user, project, and local versions), the first 200 lines/25 KB of the project's auto-memory
file (`MEMORY.md`), the names of any connected **MCP** (Model Context Protocol — the
standard Claude Code uses to plug in external tools/servers) tools, and one-line
descriptions of any available "skills" (reusable instruction bundles Claude Code can load
on demand). Run `/context` at any point for a live breakdown by category, and `/memory` to
list where your memory files live (including project/user CLAUDE.md locations for files
that don't exist yet — use `/context`, not `/memory`, to see what actually loaded into the
*current* session).

**Why it matters / what goes wrong:** New users assume the context window only holds "what
I typed." In reality, a meaningful chunk (project docs, prior learnings, tool listings) is
spent before your first message even lands — and that's what makes a long CLAUDE.md file or
a lot of MCP servers expensive on every single turn.

**Caveat:** The built-in `Explore` and `Plan` subagents deliberately skip CLAUDE.md and git
status to stay cheap; every other subagent loads the full CLAUDE.md hierarchy. The token
figures Anthropic shows in its own walkthrough are explicitly "illustrative," not
guaranteed.

**Sources:** [code.claude.com/docs/en/context-window](https://code.claude.com/docs/en/context-window) (fetched 06 Aug 2026) · [code.claude.com/docs/en/memory](https://code.claude.com/docs/en/memory) (fetched 06 Aug 2026)

**Confidence:** 📄 vendor-documented

---

### Practice: Keep CLAUDE.md short — aim for under ~200 lines ✅

**Do:** Treat CLAUDE.md as expensive, always-loaded working memory, not documentation. Put
only what Claude needs in *every* session (build commands, conventions, project layout,
hard "always do X" rules). Move anything topic-specific into `.claude/rules/` with a
`paths:` header (loads only when matching files are touched) or into a "skill" (loads only
when invoked). Anthropic's own `/init`/`/doctor` tooling proposes trims that cut content
Claude can re-derive from the codebase anyway.

**Why it matters / what goes wrong:** A bloated CLAUDE.md doesn't just burn tokens on every
message — independent testing and Anthropic's own docs agree that longer files make Claude
*less* reliable at following the rules in them (the "lost in the middle" effect from
Foundations Practice 3). A short file Claude reliably obeys beats a long one it skims.

**Caveat:** Anthropic's official guidance says "target under 200 lines per CLAUDE.md file,"
and two independent write-ups checked against this figure agree ("under about 200 lines,"
"aim for under ~200 lines"). Treat 200 as the number to aim for, and re-verify 🕒 if you're
citing it as a hard rule.

**Sources:** [code.claude.com/docs/en/memory](https://code.claude.com/docs/en/memory) (fetched 06 Aug 2026) · [iwoszapar.com — Claude Code Best Practices: 8 Rules I Learned the Hard Way](https://www.iwoszapar.com/p/claude-code-best-practices) (published 19 Jun 2026, updated 05 Aug 2026) · [dev.to/nishilbhave — CLAUDE.md Best Practices: The Complete 2026 Guide](https://dev.to/nishilbhave/claudemd-best-practices-the-complete-2026-guide-435j) (posted 29 May 2026, edited 09 Jul 2026, fetched 06 Aug 2026)

**Confidence:** ✅ independently-corroborated

---

### Practice: Don't expect an edit to CLAUDE.md to take effect mid-session 📄

**Do:** If you (or Claude) edit the project-root or user-level CLAUDE.md file while a
session is already running, know that Claude Code read it once at session start and is
holding that version in memory. The edit is saved to disk but has **no effect** on the
running session until the next `/clear`, `/compact`, or restart. (Nested CLAUDE.md files
and path-scoped rules are the exception — they load lazily the first time a matching file
is read, so an edit made before that first load *does* take effect.)

**Why it matters / what goes wrong:** This is a common "why is Claude ignoring the rule I
just added?" trap. It isn't a bug — it's how Claude Code protects its prompt cache (see
Foundations Practice 6) from having to recompute on every edit — but it will confuse anyone
expecting a live reload.

**Caveat:** None found — this is a deliberate design choice Anthropic documents plainly.

**Sources:** [code.claude.com/docs/en/prompt-caching](https://code.claude.com/docs/en/prompt-caching) (fetched 06 Aug 2026)

**Confidence:** 📄 vendor-documented

---

### Practice: Compact on your own terms — and know exactly what survives ✅ ⚠️

**Do:** Run `/compact` yourself between tasks (e.g. `/compact focus on the auth bug fix`)
rather than letting Claude Code's automatic compaction fire mid-task. You can add a
"Compact instructions" section to CLAUDE.md to steer what every compaction preserves, for
example:
```
## Compact instructions
Always preserve: the exact failing test names, the file paths we've already
edited this session, and any decision to reject an approach (with why).
```
You can also widen or narrow the buffer with `/autocompact <token-count>` — e.g.
`/autocompact 50000` reserves a smaller trailing buffer, so auto-compact triggers closer
to the true hard limit (more usable conversation, but a large single turn near the end
risks tipping the session over the limit and erroring instead of compacting gracefully);
`/autocompact 200000` compacts earlier and more often, trading conversation length for a
bigger safety margin.

Before relying on compaction, know Anthropic's own preserved/dropped table: the system
prompt is untouched (it's not part of message history); project-root CLAUDE.md and
unscoped rules are re-read from disk and re-injected; auto memory is re-injected; **rules
with `paths:` and nested subdirectory CLAUDE.md files are lost until a matching file is
read again**; invoked skill content is re-injected but capped (5,000 tokens per skill,
25,000 total, oldest dropped first); the skill *description* index does not reload — only
skills you actually used survive.

**Why it matters / what goes wrong:** ⚠️ Auto-compact is a safety net so a full context
window doesn't kill your session — that part is good. But independent write-ups
consistently report that when compaction fires mid-debugging (mid-stack-trace,
mid-refactor), the resulting summary drops exactly the details you were relying on, and
Claude can start guessing at the wrong file. Two independent write-ups, plus Anthropic's
own admission that "detailed instructions from early in the conversation may be lost,"
describe the same failure: compaction summarizes away specifics, and — in reported worst
cases — Claude edits the wrong file or repeats a mistake it had already been corrected on.
One independently-verified GitHub issue reportedly describes a rule being followed before
compaction and violated 100% of the time after. **Compacting at a moment you choose, with a
focus instruction, gives you a say in what the summary keeps** — and if an instruction
"disappears" after `/compact`, it's almost always because it was only ever said in
conversation (never written to CLAUDE.md), or it lived in a nested/path-scoped file that
hasn't reloaded yet. Watch for signs Claude got "dumber" right after a compaction message —
that's often a real signal something load-bearing got dropped, not just a feeling. For
anything you can't afford to re-derive (exact line numbers, "we agreed to use middleware
not decorators," why you rejected the first approach), write it to CLAUDE.md or commit it
to git rather than trusting it survives in conversation history.

**Caveat:** The exact auto-compact trigger threshold is model- and version-dependent and
has changed over time. Anthropic's own docs describe the default as "compacts when the
conversation reaches the model's context limit" unless a setting compacts earlier — 🕒
verify live. The "100% violation rate" figure is user-reported, not a controlled study —
treat it as illustrative, not a measured statistic; Anthropic frames this as an expected
tradeoff (summarize or hit a hard wall), not a defect.

**Sources:** [code.claude.com/docs/en/context-window](https://code.claude.com/docs/en/context-window) (fetched 06 Aug 2026) · [code.claude.com/docs/en/memory](https://code.claude.com/docs/en/memory) (fetched 06 Aug 2026) · [okhlopkov.com — Claude Code /compact: What It Does, What Survives](https://okhlopkov.com/claude-code-compaction-explained/) (fetched 06 Aug 2026, no publish date shown) · [bytebell.ai — Claude Code Keeps Compacting and Losing My Work](https://bytebell.ai/blog/claude-code-compacting-losing-work/) (published 18 Mar 2026) · [hyperdev.matsuoka.com — How Claude Code Got Better by Protecting More Context](https://hyperdev.matsuoka.com/p/how-claude-code-got-better-by-protecting) (published 10 Dec 2025) · [golev.com — Claude Saves Tokens, Forgets Everything](https://golev.com/post/claude-saves-tokens-forgets-everything/) (published 15 Jan 2026) · [code.claude.com/docs/en/how-claude-code-works](https://code.claude.com/docs/en/how-claude-code-works) (fetched 06 Aug 2026)

**Confidence:** ✅ independently-corroborated for the lossy/what-survives behavior; 📄 vendor-documented for the preserved/dropped table specifics

---

### Practice: Use `/clear`, not `/compact`, when switching to genuinely unrelated work ✅

**Do:** When you're done with one task and starting something with no shared context, run
`/clear` to reset to zero rather than `/compact`, which still leaves a summary of the old
task taking up space (and invalidates the prompt cache either way). Use `/rename` before
clearing if you might want to `/resume` the old session later.

**Why it matters / what goes wrong:** `/compact` is for continuing the *same* task with a
smaller footprint; `/clear` is for starting a *different* task. Stale context from an
unrelated prior task crowds out the files you actually need next and costs tokens on every
following message for no benefit.

**Caveat:** None found — this distinction is consistent across vendor docs and independent
commentary.

**Sources:** [code.claude.com/docs/en/costs](https://code.claude.com/docs/en/costs) (fetched 06 Aug 2026) · [okhlopkov.com — Claude Code /compact: What It Does, What Survives](https://okhlopkov.com/claude-code-compaction-explained/) (fetched 06 Aug 2026, no publish date shown)

**Confidence:** ✅ independently-corroborated

---

### Practice: Delegate large/verbose exploration to subagents ✅

**Do:** Send research that would flood your main conversation — reading many files,
grepping across a codebase, running a test suite, fetching documentation, processing logs —
to a subagent (via the `Agent` tool, renamed from "Task" as of Claude Code v2.1.63; old
`Task(...)` references still work). The subagent gets its own separate context window;
only its final summary (plus a small metadata trailer) returns to your main conversation.
Anthropic's own example shows a subagent reading ~6,100 tokens of files and returning only
~420 tokens to the parent (Anthropic labels this "illustrative," not a guaranteed ratio).

**Why it matters / what goes wrong:** This is one of the biggest levers beginners
under-use. Instead of "read every file in this directory and tell me what's wrong," ask
Claude to delegate that read-heavy investigation to a subagent — the file contents pile up
in a context window you never have to pay to keep around.

**Caveat:** ⚠️ **WARNING** — running many subagents in parallel that each return a detailed
result can still consume significant main-context tokens on return; Anthropic's own docs
warn about this directly. For truly large parallel workloads, look at "agent teams"
instead, where each worker keeps an independent context window.

**Sources:** [code.claude.com/docs/en/sub-agents](https://code.claude.com/docs/en/sub-agents) (fetched 06 Aug 2026) · [code.claude.com/docs/en/context-window](https://code.claude.com/docs/en/context-window) (fetched 06 Aug 2026) · [hyperdev.matsuoka.com — How Claude Code Got Better by Protecting More Context](https://hyperdev.matsuoka.com/p/how-claude-code-got-better-by-protecting) (published 10 Dec 2025) · [iwoszapar.com — Claude Code Best Practices: 8 Rules I Learned the Hard Way](https://www.iwoszapar.com/p/claude-code-best-practices) (published 19 Jun 2026, updated 05 Aug 2026)

**Confidence:** ✅ independently-corroborated

---

### Practice: Know the subagent limits before you build a workflow around them 📄

**Do:** Design workflows knowing Claude Code's default caps (all changeable via
environment variables — on Ubuntu, set one with `export
CLAUDE_CODE_MAX_SUBAGENTS_PER_SESSION=100` in your shell profile, e.g. `~/.bashrc`, then
restart your shell or run `source ~/.bashrc`): subagents can nest up to **3 layers** deep
below the main conversation by default; a session can spawn at most **200 subagents total**
by default; at most **20 subagents can run concurrently** by default. 🕒 These defaults
have genuinely changed several times in recent months — independent reporting confirms
churn as recently as 21–24 Jul 2026 — so don't hard-code a number into automation without
checking your installed version. A non-fork subagent never inherits your main
conversation's memory or history — it starts genuinely fresh (except the built-in
Explore/Plan agents, and a "fork," which deliberately inherits everything).

**Why it matters / what goes wrong:** If you're chaining subagents (reviewer → verifier →
fixer) and something silently stops delegating, you may have hit a depth or count limit
rather than hit a bug. And if you expect a subagent to "remember" something from earlier in
your session without being told, it won't — each spawn starts cold unless you explicitly
gave it persistent memory scope.

**Caveat:** These exact defaults have changed repeatedly across recent Claude Code
versions, including as recently as three weeks before this snapshot — treat every number
here as a live value to re-check, not a fact to memorize.

**Sources:** [code.claude.com/docs/en/sub-agents](https://code.claude.com/docs/en/sub-agents) (fetched 06 Aug 2026) · [digitalapplied.com — Claude Code Put Guardrails on Its Own Agent Fleets](https://www.digitalapplied.com/blog/claude-code-subagent-depth-limits-budget-caps-2026) (Aug 2026)

**Confidence:** 📄 vendor-documented (current default values); the recent-churn history is ✅ independently-corroborated

---

### Practice: Know which model you're actually running — window size depends on the model, not the CLI 📄 🕒

**Do:** Context window size depends on the *model*, not on Claude Code itself. As of this
writing, most current-generation models — **Claude Sonnet 5, Opus 5 (GA 24 Jul 2026),
Claude Fable 5 and its restricted sibling Mythos 5 (GA 9 Jun 2026), Opus 4.6 and later,
Sonnet 4.6** — default to a **1,000,000-token** context window on the Claude API and major
cloud providers, with no extra "long context" surcharge; older/smaller models (Claude
Sonnet 4.5, Haiku) are capped at **200,000 tokens**. Some hosting paths (certain
Bedrock/Google Cloud/Microsoft Foundry deployments) still run some models at a 200K window
even where the model otherwise supports 1M; on some models, 1M is a selectable `[1m]`
variant rather than the automatic default (Sonnet 5 runs at 1M with no variant to select).
Run `/model` in Claude Code to see and switch your active model — you can select Fable 5
directly with `--model claude-fable-5`.

**Why it matters / what goes wrong:** "Claude's context window" is not one fixed number —
assuming 200K (the number most beginner tutorials still quote) when you're actually on a
1M-token model, or vice versa, throws off any estimate of how much you can paste in or how
soon you'll hit auto-compact. It's also easy to miss that Claude Fable 5 — currently
Anthropic's most capable, most coding-focused tier — exists at all if you're only skimming
for "Sonnet" and "Opus."

**Caveat:** 🕒 verify live — model names, default context sizes, and which hosting paths get
the larger window change frequently; treat every number above as a snapshot for 06 Aug
2026, not a permanent fact.

**Sources:** [platform.claude.com/docs/en/build-with-claude/context-windows](https://platform.claude.com/docs/en/build-with-claude/context-windows) (fetched 06 Aug 2026) · [code.claude.com/docs/en/context-window](https://code.claude.com/docs/en/context-window) (fetched 06 Aug 2026) · [platform.claude.com/docs/en/about-claude/pricing](https://platform.claude.com/docs/en/about-claude/pricing) (fetched 06 Aug 2026, Fable 5/Mythos 5) · [platform.claude.com/docs/en/about-claude/models/introducing-claude-fable-5-and-claude-mythos-5](https://platform.claude.com/docs/en/about-claude/models/introducing-claude-fable-5-and-claude-mythos-5) (fetched 06 Aug 2026)

**Confidence:** 📄 vendor-documented

---

### Practice: ⚠️ Know what breaks your prompt cache — this is where surprise cost/slowness comes from 📄

**Do:** Claude Code resends your full conversation history on every turn and relies on
server-side prompt caching (Foundations Practice 6) to make that cheap. Several ordinary
actions **invalidate that cache** and force a full, expensive, uncached reprocess of the
entire conversation on the very next turn: **switching models or effort level
mid-session**, **turning on fast mode**, **denying an entire tool**, **enabling or
disabling a plugin that provides MCP servers**, **upgrading Claude Code** (rebuilds on the
first turn after restart), and **resuming a session after the cache has expired** (idle
longer than the TTL — 1 hour on a Claude subscription, 5 minutes by default on an API
key/cloud provider, or once you're on usage credits). An MCP server connecting,
disconnecting, or changing its tool list is **not** automatically on this list — Claude
Code's default "deferred tools" behavior means a server change usually only appends new
content without disturbing the cache; full invalidation there only happens if tool search
is disabled/unavailable or a tool is set to `alwaysLoad`. This list is not exhaustive —
check the vendor doc for the current complete set. Compacting itself is comparatively cheap
while the cache is warm, but compacting a very old, cold session is one of the most
expensive single actions you can trigger.

**Why it matters / what goes wrong:** ⚠️ This is where "why did that one message cost so
much / take so long" comes from. None of these triggers are obvious from the terminal — a
model switch "feels free" until the next, much slower turn. Pick your model and effort
level at the start of a session and avoid changing them mid-task if you're cost-sensitive.

**Caveat:** None found — this is Anthropic's own detailed accounting of its caching
mechanics; no independent source disputes it, but none independently double-checked the
specific numbers either.

**Sources:** [code.claude.com/docs/en/prompt-caching](https://code.claude.com/docs/en/prompt-caching) (fetched 06 Aug 2026) · [code.claude.com/docs/en/costs](https://code.claude.com/docs/en/costs) (fetched 06 Aug 2026)

**Confidence:** 📄 vendor-documented

---

### Practice: Filter or delegate huge command output instead of letting Claude read it raw ✅

**Do:** If a command routinely produces huge output (a full test run, a multi-thousand-line
log file), don't let Claude read it raw into context. One concrete option: add a
`PostToolUse` **hook** (a shell command Claude Code's harness runs automatically at certain
points) in `.claude/settings.json` that pipes a command's raw output through a filter (e.g.
`grep -E 'FAIL|ERROR'`) before Claude ever sees it — so a 5,000-line test run becomes the 10
lines that actually matter. Alternatively, install a code-intelligence plugin so "go to
definition" replaces grep-then-read-several-candidates, or delegate the whole operation to
a subagent (Practice above) so the verbose output lives in a context window you discard.

**Why it matters / what goes wrong:** Independent analysis of Claude Code sessions has
estimated that raw file/log reading can account for **60–80% of context consumption** in a
typical long session, which is also what forces premature compaction. Vague prompts like
"investigate the codebase" make this worse, prompting the agent to read far more files than
the task actually needs.

**Caveat:** The "60–80%" figure is a single blog's estimate, not a measured benchmark
across many sessions — treat it as directional, not exact.

**Sources:** [code.claude.com/docs/en/costs](https://code.claude.com/docs/en/costs) (fetched 06 Aug 2026) · [bytebell.ai — Claude Code Keeps Compacting and Losing My Work](https://bytebell.ai/blog/claude-code-compacting-losing-work/) (published 18 Mar 2026) · [iwoszapar.com — Claude Code Best Practices: 8 Rules I Learned the Hard Way](https://www.iwoszapar.com/p/claude-code-best-practices) (published 19 Jun 2026, updated 05 Aug 2026)

**Confidence:** ✅ independently-corroborated

---

### Practice: Remember — every new session starts with an empty context window 📄

**Do:** Each `claude` invocation (a genuinely new session, as opposed to
`--continue`/`--resume`) begins with a fresh, empty context window. Nothing from a previous
session's conversation is present unless it was written to CLAUDE.md or to Claude's own
auto-memory (`MEMORY.md` plus topic files, on by default, capped at 200 lines/25 KB for
what auto-loads). Use `claude --continue`/`--resume`/the `/resume` picker to reopen the
*same* session under the same ID and keep appending; use `--fork-session`/`/branch` (or
`/subtask` for an in-session fork) to copy history into a *new* session ID without
disturbing the original.

**Why it matters / what goes wrong:** Beginners sometimes assume Claude "remembers the
project" between separate terminal sessions the way a human colleague would. It doesn't,
unless you or Claude wrote that knowledge down somewhere that reloads — CLAUDE.md for
things you want to state as rules, auto memory for things Claude picked up on its own.

**Caveat:** File-edit checkpoints (`Esc` `Esc` / `/rewind`) are a separate mechanism from
context/session management — they let you undo file changes and remain available across a
resume, but they don't restore conversation context, and a restore skips symlinked/hard-linked
files.

**Sources:** [code.claude.com/docs/en/how-claude-code-works](https://code.claude.com/docs/en/how-claude-code-works) (fetched 06 Aug 2026) · [code.claude.com/docs/en/memory](https://code.claude.com/docs/en/memory) (fetched 06 Aug 2026)

**Confidence:** 📄 vendor-documented

---

## Part 2 — OpenAI Codex CLI

> All slash/at-commands below (`/compact`, `/agent`, `/status`) are typed **inside the
> running `codex` interactive session**, not at the Ubuntu bash prompt.

### Practice: Know what auto-compaction actually keeps — plan around the loss ✅

**Do:** When a Codex CLI session's token usage crosses a threshold, Codex silently
summarizes the conversation and replaces most of the history. What survives, per two of
three independent technical write-ups that examined the open-source `codex-rs` code: (1)
one summary "handoff" message — an encrypted blob for OpenAI-hosted models, or a plaintext
`_summary`-prefixed message for other providers — plus (2) roughly the last ~20,000 tokens
of your own recent messages. Everything else (prior assistant replies, tool output, file
contents already read) is discarded. Don't assume compaction remembers a constraint you
mentioned once, ten tool calls ago — restate anything critical in your next message if
you're not sure it survived.

**Why it matters / what goes wrong:** Long-running agent sessions can't hold an unlimited
transcript — the model has a fixed context window. Codex's fix, like other coding agents,
is to periodically compress the conversation into a short summary so it can keep going.
That summary is written by an LLM and is lossy by design; if it misses a detail, that
detail is effectively gone for the rest of the session.

**Caveat:** The three independent write-ups examined do **not** fully agree: two describe
the "summary + ~20K-token tail" mechanic above, but a third instead describes Codex
physically deleting all assistant replies and tool-related messages while preserving **all**
user messages verbatim, with no 20K-token cap mentioned. None of this is spelled out in
OpenAI's own docs — the mechanics come from independent reverse-engineering, and OpenAI's
own docs confirm the underlying `/responses/compact` endpoint exists without describing
Codex CLI's specific retention policy.

**Sources:** [Codex CLI Context Compaction: Architecture, Configuration, and Managing Long Sessions](https://codex.danielvaughan.com/2026/03/31/codex-cli-context-compaction-architecture/) (Daniel Vaughan, 31 Mar 2026, updated 05 Aug 2026) · [Context Compaction Research: Claude Code, Codex CLI, OpenCode, Amp (gist)](https://gist.github.com/badlogic/cd2ef65b0697c4dbe2d13fbecb0a0a5f) (Mario Zechner, 02 Dec 2025) · [Shedding Heavy Memories: Context Compaction in Codex, Claude Code, and OpenCode](https://justin3go.com/en/posts/2026/04/09-context-compaction-in-codex-claude-code-and-opencode) (Justin3go, Apr 2026) · [Compaction — OpenAI API docs](https://developers.openai.com/api/docs/guides/compaction) (OpenAI, fetched 06 Aug 2026)

**Confidence:** ✅ independently-corroborated for the general "summary replaces most of history" mechanic; the specific ~20K-token tail is corroborated by two of three sources, contradicted by the third

---

### Practice: Trigger `/compact` yourself, with instructions, at a natural stopping point 🕒

**Do:** Run `/compact` manually when you finish a logical chunk of work (a passing test, a
merged sub-feature) rather than waiting for auto-compaction to hit mid-tool-call. In
current Codex CLI (v0.117.x and later, per independent testing), you can queue follow-up
instructions during a manual compact without losing them, e.g. `/compact Focus
particularly on the authentication refactor and the three failing tests`.

**Why it matters / what goes wrong:** If you let context fill up on its own, compaction can
fire in the middle of a multi-step tool call, and the summary writer has no idea which of
the last hundred lines of diff output mattered. Compacting on your own terms, with a hint
about what's important, produces a better summary and a cleaner spot to resume from.

**Caveat:** The `/compact <instructions>` feature and its version number come from one
independent blog re-reading the CLI's changelog and source; plausible but not confirmed by
an OpenAI changelog entry. Treat "queued so you don't lose it" as the confirmed claim
(rather than a stronger reading where the instruction gets "threaded into" the
summarization prompt itself).

**Sources:** [Codex CLI Context Compaction: Architecture, Configuration, and Managing Long Sessions](https://codex.danielvaughan.com/2026/03/31/codex-cli-context-compaction-architecture/) (Daniel Vaughan, 31 Mar 2026, updated 05 Aug 2026)

**Confidence:** thin (single source for this specific syntax/version number; the general existence of manual `/compact` is corroborated elsewhere)

---

### Practice: Keep AGENTS.md short and let nested files do the organizing ✅

**Do:** Codex reads `AGENTS.md` once per session, walking from your Codex home directory
(`~/.codex`) down through the git root to your current directory, checking for
`AGENTS.override.md` then `AGENTS.md` at each level, and combining what it finds — files
closer to your working directory take precedence. The combined size defaults to a **32 KiB**
cap (`project_doc_max_bytes`; 64 KiB is documented as an example of a higher value, not a
ceiling) — Codex stops adding files once it hits the configured limit, silently. Keep the
root file to common cases and high-level conventions; push anything workflow-specific into
nested subdirectory files instead of one long document.

**Why it matters / what goes wrong:** Everything in AGENTS.md gets loaded into the context
window before the model does any work — it isn't optional background, it's tokens you're
spending on every single run. Independent testing found verbose AGENTS.md files can
actively hurt: one report describes an agent reading a full service-topology write-up meant
for architecture decisions, pulling in ~80K tokens of irrelevant context for a two-line
config change, and getting confused about which service owned the setting.

**Caveat:** OpenAI's own docs describe the size cap and precedence order but don't give an
explicit line-count recommendation. The "100–150 lines" guidance comes from an independent
AI-coding-tool vendor's own testing (a different product, not Codex-specific) — treat the
exact number as a rule of thumb, not an OpenAI-verified figure.

**Sources:** [Custom instructions with AGENTS.md — ChatGPT Learn](https://learn.chatgpt.com/docs/agent-configuration/agents-md) (OpenAI, fetched 06 Aug 2026) · [A good AGENTS.md is a model upgrade. A bad one is worse than no docs at all.](https://www.augmentcode.com/blog/how-to-write-good-agents-dot-md-files) (Augment Code / Slava Zhenylenko, 22 Apr 2026, updated 18 Jun 2026)

**Confidence:** ✅ independently-corroborated

---

### Practice: Use `codex resume` / `codex fork` instead of re-typing context ✅

**Do:** Every Codex CLI session is saved automatically as a JSONL (a line-delimited JSON
log format) "rollout" transcript under `~/.codex/sessions/`. `codex resume` reopens the
picker of recent sessions in the current repo (`--all` for across directories, `--last` for
the most recent), and appends new turns to that same transcript. Use `codex fork` (branch
from a past session without touching the original) when you want to try an alternative
approach without losing the original thread; `codex unarchive` restores a session that had
been archived back to resumable status.

**Why it matters / what goes wrong:** Resuming means you don't have to re-explain the whole
task history to a fresh session. But if that session already went through one or more
auto-compactions, the detail lost during compaction is gone from the transcript too —
resume replays what's there, it doesn't recover what was already summarized away.

**Caveat:** OpenAI's own docs confirm `codex resume` exists but describe it in a single
line, without documenting `--all`, `--last`, `codex fork`, `codex unarchive`, or the
`~/.codex/sessions/` path — that flag- and path-level detail rests on one independent
technical blog.

**Sources:** [Codex CLI — ChatGPT Learn](https://learn.chatgpt.com/docs/codex/cli) (OpenAI, fetched 06 Aug 2026) · [Codex CLI Session Lifecycle: Archive, Resume, Fork, and Compact Management](https://codex.danielvaughan.com/2026/06/05/codex-cli-session-lifecycle-archive-resume-fork-compact-management/) (Daniel Vaughan, 05 Jun 2026, updated 05 Jul 2026)

**Confidence:** thin (specific flags/lifecycle rest on a single independent source; only the bare existence of `resume` is vendor-confirmed)

---

### Practice: Delegate read-heavy exploration to subagents — avoid conflicting writes ✅

**Do:** Ask Codex to delegate parallelizable, read-heavy tasks (codebase exploration,
running down a bug across several files, checking API docs) to specialized agents — each
spawned subagent gets its own clean context window and works independently; the main
thread waits for all requested subagents, then folds their distilled findings (not raw
logs/tool output) back into one consolidated response. Use `/agent` to inspect or switch
between running agent threads. Avoid running several agents that edit the same files
concurrently.

**Why it matters / what goes wrong:** If one agent had to read every file and every test
log itself, your main session's context would fill up fast with noise you don't need for
the final answer. Subagents let exploration happen "off to the side" and only the
conclusions come back — at the cost of more total tokens burned across all the agents
combined.

**Caveat:** Codex's official docs are explicit that "subagent workflows consume more tokens
than comparable single-agent runs" and warn that agents editing code simultaneously "can
create conflicts and increase coordination overhead" — this is a tradeoff, not a free win.
Independent testing adds that deep, multi-level subagent fan-out multiplies token usage and
latency at each level, and that sequential subagent pipelines (reproduce → debug → fix)
tend to fail because information degrades at each handoff, whereas genuinely parallel,
independent subagent tasks work well.

**Sources:** [Subagents — ChatGPT Learn](https://learn.chatgpt.com/docs/agent-configuration/subagents) (OpenAI, fetched 06 Aug 2026) · [A field guide to multi-agent code review with custom subagents](https://harnez.ai/posts/multi-agent-code-review-codex/) (harnez.ai, 10 May 2026)

**Confidence:** ✅ independently-corroborated

---

### Practice: ⚠️ Watch for the "re-read spiral" on large files — it can burn your whole weekly quota ✅

**Do:** Because compaction discards previously-read file contents (see the compaction
practice above), an agent that keeps needing the same large file will re-read it in full
after every compaction — which refills the context, which triggers another compaction, in a
self-reinforcing loop. This has been reported repeatedly, including as recently as 20 Jul
2026. Mitigate by asking Codex to extract relevant sections with `grep`/`sed`-style
targeted reads instead of loading whole large files, and keep genuinely large files
(config specs, generated schemas) out of routine re-reads. **If you notice a session has
compacted 3+ times with no forward progress: press Ctrl+C to interrupt the CLI
immediately** rather than letting it keep running — don't wait and watch, since each
additional loop iteration burns more quota with nothing to show for it. After
interrupting, either start a fresh session, or use `codex fork` from a saved checkpoint
captured before the spiral began, if you want to preserve earlier, good progress.

**Why it matters / what goes wrong:** ⚠️ **WARNING** — this is a real, still-open failure
mode, not a hypothetical: independent bug reports describe a single 610 KB OpenAPI spec
file being re-read 53 times in one session (a reported 10–20x token multiplier), and
separate forum reports of an "infinite compaction loop" running overnight, with one user
reporting it consumed their entire weekly usage limit on a single stuck task. Because Codex
CLI usage is capped per 5-hour window and per week on ChatGPT Plus/Pro/Business plans, a
stuck loop like this can cost you real, **non-refundable quota**, not just time — so the
moment you notice repeated compaction with no progress, stop the process rather than hoping
it recovers on its own.

**Caveat:** These are user-filed GitHub issues and forum threads, not an OpenAI
acknowledgment of a systemic bug — the maintainers' resolution status is mixed (one closed
with no visible fix note, one still open as a feature request for "pinned files"
retention). A specific "~80% of a monthly quota" figure and a "v0.112 /
xhigh-reasoning-effort" attribution circulated in earlier drafts of this research but could
not be located in any primary source, and have been dropped rather than republished
unsupported. Treat this as an ongoing risk to manage, not a bug that's definitely fixed as
of this writing.

**Sources:** [GitHub issue #14120 — "codex just compacts repeatedly for hours at a time before it is able to make a change"](https://github.com/openai/codex/issues/14120) (reported 09 Mar 2026, closed) · [GitHub issue #16839 — "Compaction-aware context retention for frequently re-read files"](https://github.com/openai/codex/issues/16839) (filed 05 Apr 2026, open) · [OpenAI Developer Community — "Codex Infinite Context Automatically Compacted Loop Consumed Over 50% of My Usage"](https://community.openai.com/t/codex-infinite-context-automatically-compacted-loop-consumed-over-50-of-my-usage/1387585) (posted 20 Jul 2026) · [Codex CLI Context Compaction: Architecture, Configuration, and Managing Long Sessions](https://codex.danielvaughan.com/2026/03/31/codex-cli-context-compaction-architecture/) (Daniel Vaughan, updated 05 Aug 2026)

**Confidence:** ✅ independently-corroborated (three separate user-filed reports on different platforms, plus an independent write-up explaining why it happens); ⚠️ **WARNING** — can consume a large fraction of a paid usage quota, including an entire weekly cap in one documented report, with no work product to show for it

---

### Practice: Treat the model's context size and pricing as a moving target — check live 📄 🕒

**Do:** 🕒 **verify live.** As of 06 Aug 2026, OpenAI's own models page lists **GPT-5.6
Sol, Terra, and Luna** each at **1,050,000-token context / 128,000-token max output**;
OpenAI's desktop-app docs describe Sol as the default "Power setting" model (the CLI itself
is not explicitly documented as defaulting to Sol — treat "Sol" as recommended, not
confirmed-default, for the CLI); and OpenAI has announced GPT-5.4 and GPT-5.4 mini retire
from Codex for ChatGPT-signed-in users on **31 Aug 2026**. Separately, and distinct from
Codex CLI's own 272,000-token effective-context cap (Foundations Practice 2), OpenAI's own
GPT-5.5 model page documents that requests exceeding roughly 272,000 input tokens on
**GPT-5.5 specifically** are billed at a 2x input / 1.5x output surcharge for the whole
request — this pricing rule is not confirmed for GPT-5.6, so don't assume it applies
unscoped to the current model generation.

**Why it matters / what goes wrong:** Model names, context limits, and prices in this space
change every few weeks, and Codex CLI will silently start recommending or defaulting to a
new model. A number that's accurate today may be wrong by the time you read this — always
sanity-check the live figure rather than trusting a cached one, including this one.

**Caveat:** Independent research (Chroma Research, an AI infrastructure company whose
commercial product is retrieval) tested 18 frontier models, including GPT-family models,
and found accuracy "varies significantly as input length changes, even on simple tasks" — a
general LLM finding, not Codex-CLI-specific testing, with no single headline percentage
figure to quote. It argues against "just dump more into context" as a strategy regardless.

**Sources:** [Models — ChatGPT Learn](https://learn.chatgpt.com/docs/models) (OpenAI, fetched 06 Aug 2026) · [developers.openai.com — Models](https://developers.openai.com/api/docs/models) (OpenAI, fetched 06 Aug 2026) · [GPT-5.5 — OpenAI API model docs](https://developers.openai.com/api/docs/models/gpt-5.5) (OpenAI, fetched 06 Aug 2026) · [Context Rot: How Increasing Input Tokens Impacts LLM Performance](https://www.trychroma.com/research/context-rot) (Chroma Research, 14 Jul 2025, fetched 06 Aug 2026)

**Confidence:** 📄 vendor-documented for the model/pricing figures; ✅ independently-corroborated for the general "accuracy degrades with input length" caution

---

### Practice: ⚠️ Pick the least-permissive sandbox mode that gets the job done

**Do:** Codex CLI's sandbox has three modes — `read-only` (no writes), `workspace-write`
(the default for trusted repos: read/write inside the project directory and temp dirs, plus
safe commands like `ls`/`find`), and `danger-full-access` (no filesystem or network
boundary at all). Layered on top, the approval policy (`untrusted` / `on-request`, the
default / `never`) controls when Codex pauses to ask before acting. The full flag for
removing both protections is `--dangerously-bypass-approvals-and-sandbox` (aliased
`--yolo`); `--full-auto` is a narrower, now **deprecated** (with a compatibility path)
convenience flag that forces `workspace-write` with auto-approval. Default to
`workspace-write` + `on-request` for normal work, and only use `danger-full-access`/`--yolo`
inside a container or VM you're prepared to lose.

**Why it matters / what goes wrong:** ⚠️ **WARNING.** `danger-full-access` means Codex can
read and write anything on your machine and reach the network with no confirmation prompts
— official docs describe it as "Elevated Risk." It is not a beginner default and shouldn't
be reached for just to avoid answering approval prompts. Opening a malicious or compromised
project in that mode means trusting the model with the same filesystem and network access
you personally have, with no sandbox boundary stopping it from acting on that access.

**Caveat:** More permissive modes also mean more verbose tool output (broader command
output, more files touched) flowing back into the transcript on every turn, which — per the
compaction mechanics above — fills the context window faster and can bring on
auto-compaction sooner. This particular side effect is an inference from how the sandbox
and compaction docs describe their behaviors, not something either source explicitly
measures.

**Sources:** [Agent approvals & security — ChatGPT Learn](https://learn.chatgpt.com/docs/agent-approvals-security) (OpenAI, fetched 06 Aug 2026) · [How Codex CLI Flags Actually Work (Full-Auto, Sandbox, and Bypass)](https://www.vincentschmalbach.com/how-codex-cli-flags-actually-work-full-auto-sandbox-and-bypass/) (Vincent Schmalbach, 15 Jan 2026)

**Confidence:** ✅ independently-corroborated for the mode names, flag, deprecation note, and risk framing; thin/inference-only for the token-cost side effect in the caveat

---

## Part 3 — Google Gemini CLI

> ⚠️ **Read this first.** At Google I/O on 19 May 2026, Google announced it is retiring the
> standalone **Gemini CLI** for free and paid consumer tiers in favor of a new
> **Antigravity CLI**, effective **18 June 2026** — with no announced grace period. The
> `gemini` binary simply stops answering requests on affected accounts (any cron job — a
> Linux scheduled task — or CI/CD script that shells out to `gemini` breaks that day). Only
> accounts with a paid Gemini Code Assist Standard/Enterprise license, Gemini Code Assist
> for GitHub, or a paid Gemini API key keep the old CLI working past that date. Everything
> below describes Gemini CLI mechanics as documented; see the last practice for what
> carries over to Antigravity CLI and what could not yet be independently verified there.
> 🕒 verify live — check which tier you're on before relying on any of this in automation.
> All slash/at-commands below (`/memory`, `/compress`, `/clear`, `/chat`,
> `@subagent_name`) are typed **inside the running `gemini` session**, not at the Ubuntu
> shell prompt.

### Practice: Know that GEMINI.md loads on every turn, invisibly ✅

**Do:** Gemini CLI assembles instructional context hierarchically and re-sends it with
every prompt: a global file at `~/.gemini/GEMINI.md` (rules for every project), project-root
and ancestor `GEMINI.md` files, and subdirectory `GEMINI.md` files that load
"just-in-time" when the CLI's tools touch that directory. The CLI footer shows a count of
currently loaded context files. Run `/memory show` at any point to see the full,
concatenated text actually being sent to the model, and `/memory refresh` to force a
re-scan after you (or Gemini) edit a `GEMINI.md` file mid-session. The default filename is
configurable via `context.fileName` in `settings.json`.

**Why it matters / what goes wrong:** New users assume the model only sees what they type.
In Gemini CLI, a real, often-invisible chunk of every turn is spent on `GEMINI.md` content
loaded from three different locations — and editing that file on disk does **not**
retroactively change turns you've already sent; you need `/memory refresh` (or a fresh
session) for it to take effect.

**Caveat:** None found on the loading mechanism itself. No official guidance quantifies how
many tokens this typically consumes — check yourself with `/memory show` and `/stats`
rather than expecting vendor docs to give you a number.

**Sources:** [github.com/google-gemini/gemini-cli — GEMINI.md docs](https://github.com/google-gemini/gemini-cli/blob/main/docs/cli/gemini-md.md) (fetched 06 Aug 2026) · [geminicli.com/docs/cli/tutorials/memory-management](https://geminicli.com/docs/cli/tutorials/memory-management/) (fetched 06 Aug 2026) · [aipositive.substack.com — A Look at Context Engineering in Gemini CLI](https://aipositive.substack.com/p/a-look-at-context-engineering-in) (Paul Datta, published 18 Sep 2025, independent)

**Confidence:** ✅ independently-corroborated

---

### Practice: Keep GEMINI.md lean, modular, and reviewed 📄

**Do:** Google's own tutorial recommends keeping GEMINI.md instructions "actionable and
relevant to code generation," using negative constraints ("explicitly telling the agent
what *not* to do... is often more effective than vague positive instructions"), and
reviewing the file periodically to remove outdated rules. Break large files into smaller
pieces with the `@file.md` import syntax instead of one giant file. Keep the global
`~/.gemini/GEMINI.md` for truly universal rules, and push project-specific detail into the
project-root and subdirectory files so it doesn't bleed into unrelated projects.

**Why it matters / what goes wrong:** Every line in every loaded GEMINI.md file is resent
on every single prompt, whether or not it's relevant to the current task — a bloated file
is a recurring tax on every turn's budget, not a one-time cost. Segregating global vs.
project content also stops a rule you wrote for one project from quietly nudging your
behavior on an unrelated one.

**Caveat:** No official numeric line/size limit is published for GEMINI.md (unlike some
competing tools that publish a target line count) — this is a qualitative recommendation,
not an enforced or measured cap.

**Sources:** [geminicli.com/docs/cli/tutorials/memory-management](https://geminicli.com/docs/cli/tutorials/memory-management/) (fetched 06 Aug 2026) · [github.com/google-gemini/gemini-cli — GEMINI.md docs](https://github.com/google-gemini/gemini-cli/blob/main/docs/cli/gemini-md.md) (fetched 06 Aug 2026)

**Confidence:** 📄 vendor-documented (all cited sources are Google-affiliated)

---

### Practice: Use `/compress` deliberately — it's a wholesale rewrite, not partial cleanup 📄 🕒

**Do:** Run `/compress` to "replace the entire chat context with a summary" when a long
session is getting unwieldy or you're approaching the model's limit — it frees space "for
more discussion without starting from scratch." Gemini CLI also compresses automatically:
the base mechanism triggers off `model.compressionThreshold` (a fraction of context usage,
default **0.5**, requires restart to change) and, as of CLI **v0.38.0** (14 Apr 2026), an
additional "Context Compression Service" can route file content through **FULL / PARTIAL /
SUMMARY / EXCLUDED** tiers — but that newer service sits behind **experimental,
off-by-default** settings, so most installs are still running on the older, simpler
threshold-based auto-compress. Check `/stats` → `model` to watch token counts before you
hit either trigger.

**Why it matters / what goes wrong:** Unlike some competing tools that preserve a
structured table of what survives, Gemini's `/compress` is a single, wholesale rewrite of
the conversation into a summary — there's no partial/selective compaction to reason about,
which is simpler but also means you lose fine detail in one shot. Knowing the default
threshold (50% of the context budget) tells you roughly how much runway you have before it
fires unasked.

**Caveat:** 🕒 verify live — the newer Context Compression Service is explicitly
experimental and its defaults may change as Google refines it. Separately, one P0 bug
(GitHub issue #16213, filed 09 Jan 2026, closed via PR #16914) reported the CLI repeatedly
attempting compression every turn without actually shrinking context — resolved, but a
reminder that an endless "Compressing chat history..." loop is a known-and-fixed failure
mode, not something to just wait out indefinitely if you hit it on an old build.

**Sources:** [geminicli.com/docs/reference/commands](https://geminicli.com/docs/reference/commands/) (fetched 06 Aug 2026) · [geminicli.com/docs/reference/configuration](https://geminicli.com/docs/reference/configuration/) (fetched 06 Aug 2026) · [geminicli.com/docs/changelogs](https://geminicli.com/docs/changelogs/) (fetched 06 Aug 2026) · [github.com/google-gemini/gemini-cli/pull/24483](https://github.com/google-gemini/gemini-cli/pull/24483) (merged 02 Apr 2026) · [github.com/google-gemini/gemini-cli/issues/16213](https://github.com/google-gemini/gemini-cli/issues/16213) (filed 09 Jan 2026, closed)

**Confidence:** 📄 vendor-documented

---

### Practice: Write anything precious to GEMINI.md or `/memory add` — don't trust it to survive compression ✅

**Do:** GEMINI.md content and facts saved with `/memory add <text to remember>` (replace
the placeholder with your own text — the command appends it to your **global**
`~/.gemini/GEMINI.md` under a `## Gemini Added Memories` heading, not the project file) are
explicitly protected from `/compress` and automatic compression: they're re-read from disk,
not from conversation history, so they survive a summary pass untouched. Everything else in
the conversation — exact line numbers, "we tried X and rejected it," intermediate reasoning
— is fair game to be summarized away. If a fact must outlive compression, put it in
GEMINI.md or `/memory add` it; don't rely on it staying in the transcript.

**Why it matters / what goes wrong:** This is the practical version of "why did Gemini
forget what we agreed five minutes ago" — if it wasn't written to a file the CLI reloads, a
compression pass can legitimately drop it as a "detail," not a bug.

**Caveat:** Independent commentary reports the flip side isn't perfectly reliable either —
one write-up notes facts added via `/memory add` "aren't consistently recalled" by users in
practice, even though they're technically protected from compression. Treat "protected from
compression" and "always perfectly obeyed" as two different claims — only the first is
well-documented.

**Sources:** [yet-another-changelog.ai (Vibe Coding Academy) — Gemini CLI Auto Context Compression](https://www.yet-another-changelog.ai/changelog/gemini-cli-automatic-context-compression-service) (fetched 06 Aug 2026, independent) · [geminicli.com/docs/tools/memory](https://geminicli.com/docs/tools/memory/) (fetched 06 Aug 2026)

**Confidence:** ✅ independently-corroborated

---

### Practice: Use `/clear` for a genuine fresh start; `/compress` to keep going on the same task 📄

**Do:** When you're switching to fully unrelated work, run `/clear` rather than
`/compress`. The project's own merged pull requests confirm `/clear` clears the model's
context window, not just the terminal display, while preserving your up-arrow input
history so you can still recall previous prompts you typed.

**Why it matters / what goes wrong:** `/compress` is for shrinking the footprint of the
*same* task; `/clear` is for genuinely starting over. Using `/compress` when you meant to
start fresh leaves a stale summary of the old task quietly consuming budget and biasing the
model toward the wrong problem.

**Caveat:** None found in this snapshot's re-verification.

**Sources:** [geminicli.com/docs/reference/commands](https://geminicli.com/docs/reference/commands/) (fetched 06 Aug 2026) · [github.com/google-gemini/gemini-cli/pull/14182](https://github.com/google-gemini/gemini-cli/pull/14182) (merged 01 Dec 2025, fetched 06 Aug 2026) · [github.com/google-gemini/gemini-cli/issues/10601](https://github.com/google-gemini/gemini-cli/issues/10601) (opened 06 Oct 2025, closed by that PR)

**Confidence:** 📄 vendor-documented

---

### Practice: Checkpoint long or multi-day sessions with `/chat save`, `/chat resume`, `/chat list` 📄

**Do:** Use `/chat save <tag>` to persist the full conversation state to a
project-specific checkpoint (default location `~/.gemini/tmp/<project_hash>/` on
Linux/macOS), `/chat resume <tag>` to pick it back up, and `/chat list` to see what's
saved — all scoped to "that same project," so a tag saved in one repo isn't visible from
another.

**Why it matters / what goes wrong:** For work that spans days, or that you want to branch
(try approach A, save, try approach B from the same starting point), this beats leaving one
enormous terminal session open — you get a named restore point instead of hoping the
scrollback is still there.

**Caveat:** None found; the project-scoping (can't resume a chat saved in a different
project) is a real limitation to plan around, not a bug.

**Sources:** [geminicli.com/docs/reference/commands](https://geminicli.com/docs/reference/commands/) (fetched 06 Aug 2026)

**Confidence:** 📄 vendor-documented

---

### Practice: Delegate exploration to subagents — and know their guardrails ✅

**What is a subagent here?** Gemini CLI ships built-in subagents (`generalist`,
`cli_help`, `codebase_investigator`, and an opt-in `browser_agent` requiring Chrome 144+,
disabled by default) and lets you define custom ones as Markdown files with **YAML
frontmatter** (a structured metadata block at the top of a Markdown file, delimited by `---`
lines) under `.gemini/agents/*.md` (project) or `~/.gemini/agents/*.md` (user), with fields
for `name`, `description`, `kind` (local/remote), `tools`, `mcpServers`, `model`,
`temperature` (a setting controlling how random/varied the model's word choices are —
lower is more predictable, higher is more varied; leave it at the default unless you have a
specific reason to change it), `max_turns`, and `timeout_mins`.

**Do:** Invoke a subagent explicitly with `@subagent_name your task`, or let the main agent
pick one automatically when a task matches its description. Each subagent "runs in its own
isolated context loop" — its conversation history and tool output never bloat the main
agent's context; only its final summary comes back as a tool result. Plan around the
documented defaults: a subagent forced-returns after **30 turns** (`max_turns`) or **10
minutes** (`timeout_mins`) unless you raise them in its frontmatter; subagents **cannot
call other subagents** (recursion is blocked to prevent infinite loops and runaway token
usage); a subagent with no `tools:` list inherits *all* tools from the parent session
rather than starting restricted; and switching models with `/model` for your main session
does **not** override whatever model a subagent is configured to use — expect to see other
models show up in usage/`/stats` reports even after you manually picked one for yourself.

**Why it matters / what goes wrong:** This is one of the biggest levers for keeping a long
session usable: instead of having the main agent read dozens of files or run a whole test
suite inline (which permanently occupies your main context budget), hand that off to a
subagent and only pay for the summary it hands back. If a chain of delegated subagents
silently stops working partway through, it may be the recursion block or a turn/timeout cap,
not a bug. And if your bill shows a model you didn't select, check what your subagents are
configured to use before assuming something's wrong.

**Caveat:** Google's own announcement frames subagents explicitly as a fix for "context
rot" and "context pollution," and independent trade-press coverage of the same launch
corroborates the mechanics while also noting rougher edges: one early-adopter comment
quoted in that coverage says "Google should invest more in stability and UI/UX for
gemini-cli. At the moment, the experience, even with the Pro plan, is quite poor" — treat
subagents as a real, documented capability with genuine early-days rough edges, not a
flawless feature. The guardrail defaults above are 🕒 verify live — check your installed
version's docs before hard-coding a number into automation.

**Sources:** [geminicli.com/docs/core/subagents](https://geminicli.com/docs/core/subagents/) (fetched 06 Aug 2026) · [developers.googleblog.com — Subagents have arrived in Gemini CLI](https://developers.googleblog.com/subagents-have-arrived-in-gemini-cli/) (published 15 Apr 2026) · [infoq.com — Subagents in Gemini CLI Enable Task Delegation and Parallel Agent Workflows](https://www.infoq.com/news/2026/04/subagents-gemini-cli/) (published 20 Apr 2026, independent) · [geminicli.com/docs/cli/model](https://geminicli.com/docs/cli/model/) (fetched 06 Aug 2026)

**Confidence:** ✅ independently-corroborated

---

### Practice: Know your model's context window and that caching is automatic — not a switch you flip 📄 🕒

**Do:** Context window size depends on which model Gemini CLI's `/model` "Auto" routing
picked for you, not on the CLI itself. Google's official Gemini 3 spec page lists **1M-token
input / 64K-token output** for `gemini-3.1-pro-preview` and `gemini-3-flash-preview`, and
the same 1M/64K for `gemini-3.1-flash-lite`; the still-active Gemini 2.5 series includes
**Gemini 2.5 Flash at a documented 1M-token context window**. Separately, Gemini's
**implicit context caching** is "enabled by default for all Gemini 2.5 and newer models" at
the API level — there is nothing to turn on, and Gemini CLI does not expose manual cache
management to you. Google states cost savings are passed through automatically when a
request hits a cache: **10% of the standard input-token rate** for the cached portion
(confirmed against Gemini 2.5 Flash: $0.03 cached vs. $0.30 standard; Gemini 2.5 Pro: $0.125
cached vs. $1.25 standard — both exactly 10%), plus a per-hour storage charge ($1.00/1M
tokens/hour for Flash, $4.50/1M tokens/hour for Pro), which mainly helps when you
repeatedly send similar large context (e.g. the same big file) in back-to-back turns.

**Why it matters / what goes wrong:** Beginners sometimes assume "large context window" is
a fixed, universal number, or that they need to manually enable caching the way you might
with a raw API integration — neither is true inside Gemini CLI. The model auto-routing
picks a model for you, and caching is invisible plumbing, not a switch you flip.

**Caveat:** 🕒 verify live, hard — context-window and cache-pricing figures are exactly the
kind of fast-moving, version-specific spec previously found misquoted in blog posts (an
earlier draft of this practice cited a "roughly 20%" cache discount that, on re-fetch, did
not match either the caching docs or the pricing page — corrected to 10% above). A
separately-circulating "2M" figure for Gemini 3.1 Pro could not be traced to an official
page and should be treated as unconfirmed.

**Sources:** [ai.google.dev/gemini-api/docs/pricing](https://ai.google.dev/gemini-api/docs/pricing) (fetched 06 Aug 2026) · [ai.google.dev/gemini-api/docs/gemini-3](https://ai.google.dev/gemini-api/docs/gemini-3) (fetched 06 Aug 2026) · [ai.google.dev/gemini-api/docs/caching](https://ai.google.dev/gemini-api/docs/caching) (fetched 06 Aug 2026) · [ai.google.dev/gemini-api/docs/long-context](https://ai.google.dev/gemini-api/docs/long-context) (fetched 06 Aug 2026)

**Confidence:** 📄 vendor-documented

---

### Practice: ⚠️ Budget for "thinking token" cost blowups on long agentic sessions

**Do:** Agentic terminal sessions burn tokens differently than chat: the CLI rereads
files, replays diffs, and restuffs context on every turn, and current "thinking" models
bill their (invisible) reasoning tokens at full output-token rates — one cost analysis puts
this at **70–85% of the total output bill** on complex reasoning tasks. That same analysis
documented a real-world case from the Google AI Developer forum: a user's daily cost jumped
from a few thousand KRW to 150,000–200,000 KRW (roughly $100–140) despite *decreased*
usage, driven by unbudgeted thinking-token volume after migrating to a thinking-capable
model. Watch `/stats` → `model` for token counts during long sessions, favor `/compress`
and subagent delegation to cut reread volume, and don't assume "fewer requests" means
"lower bill" once a thinking model is involved.

**Why it matters / what goes wrong:** ⚠️ This is the practical, out-of-pocket version of
"context management" — the same mechanics that make long sessions unwieldy (constant
rereading, growing history) also directly drive your bill on metered plans, and
thinking-token costs in particular are easy to miss because they don't show up as visible
output.

**Caveat:** Both the 70–85% figure and the KRW anecdote come from a single publisher (a
second source checked for this snapshot discusses the same general mechanism — "output
tokens, including the model's thinking tokens, cost several times more than input" — but
does not contain either specific number). Treat this as one detailed, internally-consistent
cost analysis, not independently cross-checked figures, and treat the specific percentages
and the KRW example as illustrative of a real, plausible pattern rather than a guaranteed
multiplier for your own workload.

**Sources:** [cloudzero.com/blog/gemini-pricing](https://www.cloudzero.com/blog/gemini-pricing/) (published 16 Jul 2026, updated 30 Jul 2026)

**Confidence:** thin (single publisher for the specific figures; the general cost mechanism is directionally corroborated elsewhere)

---

### Practice: Know that Gemini CLI itself is being replaced — check which tool you're actually on

**Do:** As of this snapshot, Google is actively moving users off Gemini CLI onto
**Antigravity CLI** (a Go-based rewrite). Google's own migration guidance says Agent
Skills, Hooks, Subagents, and Extensions "carry over" conceptually (Extensions become
Antigravity plugins), and Antigravity's own changelog documents its own version of
context-window management — e.g. a **"context-compaction boundary" indicator** added in CLI
v1.1.3 (16 Jul 2026) so you can see where a previous compaction happened, and its own
asynchronous, isolated-context subagent model. These specifics were confirmed directly
against Google's own `antigravity.google` docs and changelog; no independent (non-Google)
commentary analyzing Antigravity's context-management mechanics in depth was found at
initial research time. Independent write-ups have begun to appear since (e.g. describing a
reported ~135,000-token auto-compaction trigger), but those were only surfaced via search,
not a direct fetch, and aren't confirmed to this corpus's bar — so that specific figure is
not asserted as fact here. Treat every Antigravity-specific detail in this paragraph as
vendor-sourced (or emerging/unconfirmed) rather than independently verified.

**Why it matters / what goes wrong:** If you're reading Gemini CLI material (including this
entry) after 18 June 2026 on a free or paid consumer-tier account, the `gemini` binary may
no longer respond at all — before troubleshooting a "broken" Gemini CLI, check whether
you're actually supposed to be on Antigravity CLI now. Enterprise Gemini Code Assist
licenses, Gemini Code Assist for GitHub, and paid Gemini API keys are the documented
exceptions that keep the old CLI usable past that date.

**Caveat:** Independent tech-news coverage (a publisher separate from Google) confirms the
deprecation date and no-grace-period behavior, so that part is independently-corroborated;
the specific Antigravity context-management mechanics described above remain
vendor-sourced/thin, and could change quickly given how new the product is.

**Sources:** [developers.googleblog.com — An important update: transitioning Gemini CLI to Antigravity CLI](https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli/) (published 19 May 2026) · [inventivehq.com — Gemini CLI Is Being Retired on June 18 — Meet Antigravity CLI](https://inventivehq.com/blog/gemini-cli-deprecated-antigravity-cli-migration) (published 13 Jun 2026, independent) · [antigravity.google/changelog](https://antigravity.google/changelog) (fetched 06 Aug 2026) · [antigravity.google/docs/cli/subagents](https://antigravity.google/docs/cli/subagents) (fetched 06 Aug 2026)

**Confidence:** contested (the deprecation/timeline facts are ✅ independently-corroborated; the Antigravity context-management mechanics are 📄 vendor-sourced/thin — split confidence, don't treat this whole entry as one uniform tier)

---

## Held pending fixes (not publish-ready as fact)

These are gaps the technical entry's research team could not verify to this corpus's
sourcing bar. They're listed here, unchanged, so you know what's still uncertain rather
than guessing:

- **Antigravity CLI's precise context-management mechanics** (auto-compaction trigger
  token count, nested-subagent handling) — independent commentary is starting to appear but
  was only surfaced via search, not a direct fetch. ⚠ PENDING (#antigravity-independent-source-needed)
- **Antigravity CLI's actual default model** — reported by secondary sources as Gemini 3.5
  Flash, but not confirmed against an official Antigravity spec page. ⚠ PENDING (#antigravity-default-model-needs-live-fetch)
- **No independent (non-Anthropic) corroboration** was found for the specific mechanics of
  Claude's "context awareness" token-budget injection (`<budget:token_budget>` /
  `<system_warning>` tags) — not published as a standalone practice since it would rest on
  a single vendor source. ⚠ PENDING (#claude-context-awareness-tags-single-source)
- **Codex CLI weekly/5-hour usage-limit numbers per ChatGPT plan tier** were only found on
  third-party pricing-aggregator blogs of uncertain reliability. ⚠ PENDING (#codex-usage-limits-need-primary-source)
- **An OpenAI announcement reportedly describing an earlier Codex model** as "the first
  model natively trained to operate across multiple context windows through compaction"
  returned an error on every fetch attempt and was dropped rather than cited from a search
  snippet. ⚠ PENDING (#codex-max-native-compaction-needs-fetchable-source)
- **Auto memory (`MEMORY.md`) as a Claude Code persistence mechanism distinct from
  CLAUDE.md** could only be verified against Anthropic's own docs; no independent
  commentary discussing it in depth was located. ⚠ PENDING (#claude-auto-memory-needs-independent-source)

---

## CHANGELOG

1. Re-leveled from the 2026-08-06 technical entry (`best-practices` track) — facts,
   numbers, and source URLs are unchanged. That entry itself went through a 3-lens grading
   pass (Skeptic/Beginner/Timekeeper) on 06–07 Aug 2026 covering 4 Skeptic KILLs (fabricated
   statistics/quotes attached to real studies, one wrong cache-discount figure) and roughly
   40 further FIX/FLAG corrections — see that entry's own CHANGELOG for the itemized list.
2. Practices condensed for a beginner audience: in the Claude Code section, three
   closely-related technical-entry practices ("compact deliberately," "know what /compact
   keeps/drops," "treat compaction as lossy") were merged into one combined practice so a
   beginner sees "how to compact well" as a single idea, with all original sources kept. In
   the Gemini CLI section, "delegate to subagents" and "know subagent limits" were merged
   the same way.
3. One technical-entry practice was dropped as out of scope for this audience: "Don't
   confuse Claude Code's `/compact` with Anthropic's API-level context management features"
   — aimed at people building their own agent directly on the Messages API, not at CLI
   users. Its sources were not reused elsewhere and are not included here.
4. Every other practice from the technical entry (8 Foundations, 11 Claude Code, 8 Codex
   CLI, 10 Gemini CLI after the merges above) is retained.
5. Every ⚠️ WARNING-labeled item from the technical entry is preserved, including: the
   quadratic-cost/web-fetch-token cost trap (Foundations), the prompt-cache-invalidation
   cost trap (Claude Code), the "re-read spiral" that can burn an entire weekly Codex quota
   (Codex CLI), the `danger-full-access`/`--yolo` sandbox risk (Codex CLI), and the
   thinking-token cost blowup with a real KRW billing anecdote (Gemini CLI), plus the
   Gemini CLI → Antigravity CLI deprecation scope note.
6. Jargon expanded on first use throughout: context window, token, CLAUDE.md/AGENTS.md/
   GEMINI.md, MCP, subagent, skill, hook, prompt caching, TTL, RAG, YAML frontmatter, JSONL,
   cron/CI-CD.
7. "Why it matters / what goes wrong" framing added or strengthened for every practice with
   a concrete failure in plain words (lost instructions, surprise bills, wasted quota,
   silently stalled scripts).
8. All source links and Confidence labels copied verbatim from the technical entry; no URLs
   added, dropped, or rewritten. No new facts, statistics, prices, or version numbers were
   introduced anywhere in this document.
