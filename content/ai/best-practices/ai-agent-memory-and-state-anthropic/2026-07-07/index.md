---
title: "AI Agent Memory and State Management — Anthropic/Claude (as of 07 Jul 2026)"
date: 2026-07-07
snapshot_date: 2026-07-07
topic: ai-agent-memory-and-state-anthropic
track: best-practices
audience: "technically comfortable readers"
description: "How to build persistent memory and state into Claude-based agents: in-context curation, Files API, the memory tool, Managed Agents memory stores, server-side compaction, context editing, and when adaptive thinking helps vs. hurts — accurate as of July 2026."
content_type: "Best Practice"
categories: ["Anthropic", "Claude", "AI Agents"]
tags: ["memory", "state-management", "context-window", "files-api", "mcp", "extended-thinking", "compaction", "claude-agents"]
last_refreshed: 2026-07-07
graded_by: "RingS panel (Skeptic/Beginner/Timekeeper) + sensei, 2026-07-07"
grading_result: "0 fabrications; 12 corrections applied; 1 pending item logged"
---

<!-- This file lands at content/ai/best-practices/ai-agent-memory-and-state-anthropic/2026-07-07/index.md and is an IMMUTABLE
     dated snapshot. Once published it is never edited — a refresh is a NEW <snapshot-date> dir.
     "Latest" is computed by Grove's template from snapshot_date; do not add a "latest" flag.
     Source tiers: independently-corroborated = 2+ DIFFERENT publishers; vendor-documented =
     official vendor docs only (authoritative, single source). -->

# AI Agent Memory and State Management — Anthropic/Claude Ecosystem (as of 07 Jul 2026)

> **Grading note.** A dated snapshot — accurate as of **07 Jul 2026**, frozen here and kept as
> a permanent archive entry. Research-drafted by a pupil, graded by the 3-lens panel + sensei.
> Corrections applied inline; unverifiable gaps marked ⚠ PENDING — never guessed.

## How to read the labels
- ✅ **independently-corroborated** — 2+ independent publishers
- 📄 **vendor-documented** — official docs only (authoritative, single source)
- ⚠️ **WARNING** — a default that can cost money, break the machine, or remove a safety net
- 🕒 **verify live** — fast-moving (versions/prices/quotas); check the current value

---

## Practice: Use the four memory tiers as a design checklist before building anything

**Do:** Before writing a line of agent code, map each piece of state onto one of four tiers: (1) **in-context** — raw messages or a summary in the system/user prompt, (2) **external storage** — databases, files, or vector stores retrieved at runtime, (3) **in-weights** — knowledge baked into the model itself (you cannot change this at runtime without expensive fine-tuning or retraining), and (4) **cache memory** — prompt-cache hits that trade write cost for fast re-read. Choose the tier that fits the data's lifetime and access pattern, not the tier that is easiest to code first.

**Why:** Many developers default to stuffing everything into the system prompt (in-context) until it breaks, then reach for a vector database. Knowing the tiers upfront lets you pick a design that stays manageable as your agent grows. In-weights knowledge is free to query but permanently out of date for anything that changes; in-context is cheap to prototype but grows unboundedly; external storage can scale but adds latency and failure modes.

**Caveat:** This four-tier taxonomy is a useful mental model synthesized from Anthropic engineering writing and practitioner experience — it is not a labeled API contract or official Anthropic taxonomy. Independent practitioners sometimes subdivide differently (e.g., treating MCP memory servers as a fifth tier). The Anthropic engineering pages discuss in-context management techniques and external storage patterns but do not use the exact "four tiers" framing.

**Sources:** [anthropic.com/engineering/effective-context-engineering-for-ai-agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) (fetched 2026-07-07) · [anothercodingblog.com/p/persistent-memory-for-claude-agents](https://www.anothercodingblog.com/p/persistent-memory-for-claude-agents) (fetched 2026-07-07)

**Confidence:** independently-corroborated (Skeptic FIX-1: the specific "four tiers" label is a synthesized mental model not directly stated in either source; sources confirm the underlying tiers as concepts)

---

## Practice: Treat the context window as a finite budget — curate, don't accumulate

**Do:** Monitor token usage on every response via the `usage` field (e.g., `response.usage.input_tokens` and `response.usage.output_tokens` in the Anthropic Python SDK). Use the token-counting API endpoint before sending long prompts to estimate cost before committing. As history grows, drop or compress content that is no longer decision-relevant. Keep tool definitions lean — they count against the budget even when unused. For agents with predictable long-running loops, set a trigger threshold and either use server-side compaction or manually summarise the oldest turns before they crowd out the current task.

**Why:** "Context rot" is real — accuracy and recall degrade as token count grows, even if you are technically within the window limit. More tokens is not automatically better. The context-windows docs document `stop_reason: model_context_window_exceeded` for cases where the window overflows at generation time.

**Caveat / ⚠️ WARNING:** Current flagship models (Fable 5, Opus 4.8, Sonnet 5, Sonnet 4.6 [legacy], Mythos 5) have a default context window of 1 million tokens — large enough that beginners can accidentally accumulate gigantic histories before hitting a wall. This can produce significant unexpected costs because every input token in every request is billed. Also note: Opus 4.7+, Fable 5, and Sonnet 5 use a new tokenizer that produces approximately 30% more tokens for the same text than earlier models — compounding the cost-accumulation risk. Haiku 4.5 has a 200k context window (not 1M). 🕒 **verify live** — model lineup and context window sizes change frequently; check [platform.claude.com/docs/en/build-with-claude/context-windows](https://platform.claude.com/docs/en/build-with-claude/context-windows) before building.

**Sources:** [platform.claude.com/docs/en/build-with-claude/context-windows](https://platform.claude.com/docs/en/build-with-claude/context-windows) (fetched 2026-07-07) · [anthropic.com/engineering/effective-context-engineering-for-ai-agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) (fetched 2026-07-07)

**Confidence:** independently-corroborated

---

## Practice: Use server-side compaction for long multi-turn conversations instead of rolling your own summariser

**Do:** For conversations that regularly approach context window limits, enable the `compact_20260112` strategy via the `context_management` parameter (beta header: `anthropic-beta: compact-2026-01-12`). A **beta header** is an HTTP request header you add to enable a preview feature; in the Anthropic Python SDK: `client.messages.create(..., extra_headers={"anthropic-beta": "compact-2026-01-12"})`. Always append the full response — including the `compaction` block — to your message list on subsequent turns; the API automatically drops all content before the compaction block. To control costs, track compaction events and cap total spend with a cumulative token budget. Combine with prompt caching: a cached system prompt stays cached even after compaction, so only the summary generates a cache-write charge.

**Why:** Rolling your own summariser requires tuning prompts and managing state synchronisation. Server-side compaction offloads that work to the API. Supported models as of 2026-07-07 include Fable 5, Mythos 5, Mythos Preview, Opus 4.8, Opus 4.7, Opus 4.6, Sonnet 5, and Sonnet 4.6 — check the docs for the current list. 🕒 **verify live.** Compaction is ZDR-eligible (see Files API practice below for ZDR definition) when your organisation has a Zero Data Retention arrangement.

**Caveat / ⚠️ WARNING:** Compaction triggers an additional sampling step billed as extra tokens. The top-level `input_tokens` / `output_tokens` fields in the response **exclude** compaction iterations — you must sum all entries in the `usage.iterations` array to compute total billed tokens:

```python
total_tokens = sum(
    it.get("input_tokens", 0) + it.get("output_tokens", 0)
    for it in response.usage.iterations
)
```

Beginners who only look at the top-level fields will undercount their bill. 🕒 **verify live** — supported model list and response shape changes; check the compaction docs.

**Sources:** [platform.claude.com/docs/en/build-with-claude/compaction](https://platform.claude.com/docs/en/build-with-claude/compaction) (fetched 2026-07-07) · [anthropic.com/engineering/effective-context-engineering-for-ai-agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) (fetched 2026-07-07)

**Confidence:** independently-corroborated

---

## Practice: Use the memory tool for just-in-time, file-based state that survives context resets

⚠️ **WARNING — Path traversal (read before implementing):** Your handler must validate that every path starts with `/memories` and resolves inside the memory root. A malicious path like `/memories/../../secrets.env` can escape the directory and read or overwrite environment files containing API keys. Use your language's built-in path utilities (e.g., Python's `pathlib.Path.resolve()` and `relative_to()`) and reject paths containing `../` or URL-encoded variants (`%2e%2e%2f`). This is your responsibility — the SDK does not do it for you.

**Do:** Add `{"type": "memory_20250818", "name": "memory"}` to your tools list. Implement a client-side handler that executes six commands (`view`, `create`, `str_replace`, `insert`, `delete`, `rename`) against storage you control — a local directory, database, or cloud bucket — with path validation as described above. The SDK ships a ready-made local filesystem implementation (`BetaLocalFilesystemMemoryTool` for Python and TypeScript) to get started. Instruct Claude to read the `/memories` directory before starting any session, and to write progress notes as it works. Structure memories as many small focused files, not a few large ones.

**Why:** The memory tool solves the "fresh-context problem": each new conversation starts with no history, but the agent can load exactly what it needs instead of pre-loading everything. The tool works client-side, so your application owns the storage layer and can inspect, export, or edit memory files independently of Claude. The API automatically appends a protocol instruction to Claude's system prompt telling it to check its memory directory first — you do not need to write this yourself.

**Caveat:** The memory tool is available on Claude 4 and later models only. No beta header is required for the tool definition itself, but the SDKs' helper runners (`client.beta.messages.tool_runner`) live in the beta namespace even though the tool is GA — 🕒 **verify live** that the SDK namespace has not changed on a recent release.

**Sources:** [platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool](https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool) (fetched 2026-07-07) · [leoniemonigatti.com/blog/claude-memory-tool.html](https://www.leoniemonigatti.com/blog/claude-memory-tool.html) (fetched 2026-07-07) · [anothercodingblog.com/p/persistent-memory-for-claude-agents](https://www.anothercodingblog.com/p/persistent-memory-for-claude-agents) (fetched 2026-07-07)

**Confidence:** independently-corroborated

---

## Practice: For Managed Agents, use memory stores and keep individual memories under 100 kB

**Do:** Create a memory store via `client.beta.memory_stores.create(...)` (requires `managed-agents-2026-04-01` beta header — add to requests as `extra_headers={"anthropic-beta": "managed-agents-2026-04-01"}`). Attach it to a session via the `resources[]` array at session creation time — you cannot add or remove stores from a running session. Set `access: "read_only"` for reference material the agent should read but not overwrite. Keep each memory file small and focused; the hard limit is 100 kB (~25 k tokens) per memory and 2,000 memories per store. Use the `content_sha256` precondition when doing read-modify-write updates to avoid clobbering concurrent writes.

PII here means personally identifiable information — names, email addresses, phone numbers, location data. Be deliberate about what PII you store. Archiving a store is an explicit API call (calling `.archive()`) — it does not happen automatically. Once archived, the store becomes read-only and cannot be unarchived; data is preserved but inaccessible for writes.

**Why:** Managed Agents memory stores provide workspace-scoped, versioned, auditable persistent state — every write creates an immutable memory version you can retrieve or redact. This is safer than the raw memory tool for production use cases involving multiple parallel agents or compliance requirements. The versioning system can recover from accidental destructive overwrites — a real failure mode when an agent uses a full `write` instead of an `edit`.

**Caveat / ⚠️ WARNING — Prompt injection:** Memory stores attached with default `read_write` access are vulnerable to prompt injection. If your agent processes untrusted input (user prompts, fetched web pages, third-party tool output), a successful injection can write malicious content into the store, which later sessions then read as trusted memory. Use `read_only` for any store the agent does not need to modify. 🕒 **verify live** — beta header and feature availability may change. Check whether your plan tier includes this feature — free/developer tiers may not.

**Caveat:** A maximum of 8 memory stores can be attached per session.

**Sources:** [platform.claude.com/docs/en/managed-agents/memory](https://platform.claude.com/docs/en/managed-agents/memory) (fetched 2026-07-07) · [anothercodingblog.com/p/persistent-memory-for-claude-agents](https://www.anothercodingblog.com/p/persistent-memory-for-claude-agents) (fetched 2026-07-07)

**Confidence:** independently-corroborated

---

## Practice: Use the Files API to avoid re-uploading large reference documents on every request

**Do:** Upload a document once with `client.beta.files.upload(...)` and save the returned `file_id`. Pass it in subsequent requests as a `document` (PDF/text), `image`, or `container_upload` content block instead of re-sending the raw bytes. File content used in Messages requests is billed as input tokens on each use; the upload/list/delete operations themselves are free. Delete files you no longer need to stay within your organisation's storage quota. Add `"anthropic-beta: files-api-2025-04-14"` to your requests.

**Why:** For multi-turn agents that repeatedly reference the same knowledge base, user manual, or codebase, re-uploading on every call wastes bandwidth and adds latency. The Files API separates the upload cost from the per-request token cost, and supports files up to 500 MB.

**Caveat / ⚠️ WARNING — No ZDR:** The Files API is explicitly **not** eligible for **Zero Data Retention (ZDR)** — an Anthropic enterprise contract option where your prompts and outputs are not stored on Anthropic's servers after the API call completes. If your use case requires ZDR (e.g., handling sensitive user data), do not use the Files API. Data is retained under Anthropic's standard retention policy — check [anthropic.com/privacy](https://www.anthropic.com/privacy) for current data handling details. Check whether your plan tier includes ZDR — free and developer tiers do not.

**Caveat:** Files uploaded by you have `"downloadable": false` — you cannot retrieve the raw bytes later through the API. The Files API is in beta (as of 2026-07-07, beta header required) and not yet available on Amazon Bedrock or Google Cloud. 🕒 **verify live** — availability and limits may change.

**Sources:** [platform.claude.com/docs/en/build-with-claude/files](https://platform.claude.com/docs/en/build-with-claude/files) (fetched 2026-07-07)

**Confidence:** vendor-documented

---

## Practice: Use context editing to surgically clear stale tool results and thinking blocks — not instead of compaction, but alongside it

**Do:** For agentic workflows with heavy tool use, add a `clear_tool_uses_20250919` edit to your `context_management` configuration (beta header: `anthropic-beta: context-management-2025-06-27`). Set a `trigger` token threshold (e.g., 30 000 tokens) and a `keep` count of recent results to preserve. When using extended/adaptive thinking, add a `clear_thinking_20251015` edit before the tool-result clearing edit (order matters) to prevent thinking blocks from accumulating. Pair this with the memory tool so Claude can write important findings to memory before old tool results are cleared.

**Why:** In long agentic loops, tool results from earlier in the conversation (search results, file reads, API responses) consume tokens but add no new signal once Claude has acted on them. Context editing removes these on the server before the prompt reaches the model, freeing capacity for current work without forcing a full compaction or manual history management in your application. Your application always keeps the unmodified full history — clearing is applied server-side only.

**Caveat:** Use `clear_at_least` to ensure clearing is worth the prompt-cache invalidation cost it triggers. Context editing currently works best with custom tools; token counting may be inaccurate for server-side tools. Still in beta as of 2026-07-07.

**Sources:** [platform.claude.com/docs/en/build-with-claude/context-editing](https://platform.claude.com/docs/en/build-with-claude/context-editing) (fetched 2026-07-07) · [platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool](https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool) (fetched 2026-07-07, see "Using with compaction" section)

**Confidence:** vendor-documented

---

## Practice: Use adaptive thinking for complex single-request reasoning — it does not replace external state

**Do:** For current flagship models (Fable 5, Opus 4.8, Sonnet 5), enable adaptive thinking with `"thinking": {"type": "adaptive"}` and an `effort` parameter (`"low"`, `"medium"`, `"high"`, or `"max"`) for requests involving genuinely complex multi-step reasoning — proofs, intricate analysis, choosing between tools, or reasoning about intermediate tool results:

```python
response = client.messages.create(
    model="claude-fable-5-20260609",
    max_tokens=16000,
    thinking={"type": "adaptive"},
    effort="high",
    messages=[...]
)
```

For the legacy `budget_tokens` API — still functional on Sonnet 4.6 and Opus 4.6 but deprecated on those models and **unsupported on all current flagship models** — see the legacy note below.

Do not rely on thinking blocks to carry state across sessions: they are isolated to one request. When passing thinking blocks back in a tool-use loop, include them **unmodified** — the API cryptographically signs thinking blocks and returns a 400 error if you alter them. Combine adaptive thinking with external memory (memory tool or memory stores) for stateful multi-session work.

**Why:** Adaptive thinking is powerful for within-request reasoning but cannot store information across sessions. Thinking blocks are scoped to a single request and do not persist between separate conversations. On models that retain thinking blocks from prior turns, those blocks accumulate in the context window as input tokens and are billed — this is a cost trap.

**Caveat / ⚠️ WARNING:** You are charged for the full thinking token budget even if you use `display: "omitted"` to suppress thinking from the response. There is no cost saving from hiding thinking.

**Caveat (legacy API):** `{"type": "enabled", "budget_tokens": N}` works on Claude Opus 4.5, Sonnet 4.5, Haiku 4.5, Sonnet 4.6, and Opus 4.6, but is deprecated on the two 4.6 models and completely unsupported on Fable 5, Opus 4.8, Sonnet 5, and all subsequent flagship models. Developers using a current model and passing `budget_tokens` will receive a 400 error. Migrate to the `effort` / adaptive API as above.

🕒 **verify live** — model support and thinking mechanics change with new model releases; check [platform.claude.com/docs/en/build-with-claude/extended-thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking) before building.

**Sources:** [platform.claude.com/docs/en/build-with-claude/extended-thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking) (fetched 2026-07-07) · [platform.claude.com/docs/en/about-claude/models/overview](https://platform.claude.com/docs/en/about-claude/models/overview) (fetched 2026-07-07)

**Confidence:** vendor-documented

---

## Practice: For multi-session software agents, set up structured memory files in an initialiser session before starting real work

**Do:** Run a short "initialiser" session once before your main agent loop. Have it create: a progress log (what has been done, what comes next), a feature or task checklist (explicit pass/fail status), and a reference to any environment-setup script. Have subsequent "coding" or "worker" sessions open by reading those memory files before touching anything else. At the end of each session, update the progress log. Commit code changes with descriptive messages (e.g., using git version control, which tracks all file changes with rollback ability) to give the agent a recoverable audit trail. Work on one feature at a time, marking it complete only after end-to-end verification — not just after the code is written.

**Why:** Without an initialiser, each new session re-explores the codebase from scratch, wastes tokens rediscovering prior decisions, and risks duplicating or reversing earlier work. Anthropic's engineering team documents this pattern as the recommended approach for long-running autonomous coding agents; an independent practitioner reported that "Session 2 cost five times less than Session 1 because the agent read existing notes instead of recomputing."

**Caveat:** This pattern is most valuable when sessions are interrupted or run on a schedule. For single-session work that completes in one run, it adds overhead. The quality of the progress file is only as good as the discipline applied to updating it; if the agent skips the update step (which can happen on model errors), the next session starts with stale state.

**Sources:** [anthropic.com/engineering/effective-harnesses-for-long-running-agents](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents) (fetched 2026-07-07) · [anothercodingblog.com/p/persistent-memory-for-claude-agents](https://www.anothercodingblog.com/p/persistent-memory-for-claude-agents) (fetched 2026-07-07) · [platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool](https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool) (fetched 2026-07-07, see "Multi-session software development pattern" section)

**Confidence:** independently-corroborated

---

## Held pending fixes (not publish-ready)

- MCP knowledge-graph memory server (`@modelcontextprotocol/server-memory`) — GitHub repo listing confirmed the server exists but detailed capabilities, limits, and best practices require fetching the `/src/memory` subdirectory or dedicated docs page. Holding as thin. ⚠ PENDING

## CHANGELOG (grading → this entry)

1. **Timekeeper KILL-2 (extended thinking API deprecated):** Rewrote the extended thinking practice. The original draft showed `{"type": "enabled", "budget_tokens": N}` as the primary API — this is deprecated on Sonnet 4.6 / Opus 4.6 and unsupported on all current flagship models (Fable 5, Opus 4.8, Sonnet 5). Practice now uses `{"type": "adaptive"}` + `effort` parameter as the primary path; `budget_tokens` moved to legacy caveat with explicit ⚠ "Developers using a current model... will receive a 400 error."
2. **Beginner A-4 (KILL — path traversal warning placement):** Elevated the path traversal WARNING block to appear at the top of the practice's Do section, before any implementation guidance. Original had it in Caveat after the instructions.
3. **Skeptic FIX-1 (memory tiers source mismatch):** Downgraded confidence note for the "four tiers" label — the cited Anthropic engineering page discusses the concepts but does not present the exact four-tier taxonomy. Added caveat that this is a synthesized mental model.
4. **Skeptic FIX-2 (unverified verbatim quote):** Removed quotation marks from "No cross-session memory — thinking blocks cannot be cached or stored between separate conversations." Replaced with paraphrase: "Thinking blocks are scoped to a single request and do not persist between separate conversations."
5. **Skeptic FLAG-1 (`stop_reason` attribution):** Corrected attribution of `stop_reason: model_context_window_exceeded` — it is documented on the context-windows page, not the compaction page as the original implied.
6. **Timekeeper FIX-4 (model lineup):** Added Claude Sonnet 5 (1M tokens, current flagship); marked Sonnet 4.6 as legacy; added Haiku 4.5 exception (200k tokens); noted ~30% tokenizer change for Opus 4.7+/Fable 5/Sonnet 5.
7. **Timekeeper FIX-5 (compaction model list):** Added Fable 5, Mythos 5, Mythos Preview, Opus 4.8, Opus 4.7, Opus 4.6, Sonnet 5 to supported model list for compaction.
8. **Timekeeper FIX-6 (memory tool SDK beta namespace):** Added `verify live` note to the SDK beta namespace caveat.
9. **Beginner A-2 (usage field):** Added `response.usage.input_tokens` and `response.usage.output_tokens` code reference.
10. **Beginner A-5 (compaction billing):** Added Python code snippet showing how to sum `usage.iterations` array.
11. **Beginner A-6 + X-1 (ZDR + beta headers):** Defined Zero Data Retention (ZDR) on first use; added explanation of what a beta header is and how to pass it in the Python SDK.
12. **Beginner A-1/A-7/A-8/A-9:** Added note about in-weights fine-tuning cost; clarified archive operation semantics; defined PII on first use; added link to Anthropic privacy page.
