# AI Agent Memory and State Management — Anthropic/Claude (Beginner Guide, as of 07 Jul 2026)

> A plain-English guide to giving Claude-based agents a memory that survives between conversations: how to choose a storage approach, avoid surprise costs, and keep your data safe — accurate as of July 2026.


<!-- This file lands at content/ai/beginner/ai-agent-memory-and-state-anthropic/2026-07-07/index.md and is an IMMUTABLE
     dated snapshot. Once published it is never edited — a refresh is a NEW <snapshot-date> dir.
     "Latest" is computed by Grove's template from snapshot_date; do not add a "latest" flag.
     Source tiers: independently-corroborated = 2+ DIFFERENT publishers; vendor-documented =
     official vendor docs only (authoritative, single source). -->

# AI Agent Memory and State Management — Anthropic/Claude Ecosystem (Beginner Guide, as of 07 Jul 2026)

> **Grading note.** A dated snapshot — accurate as of **07 Jul 2026**, frozen here and kept as
> a permanent archive entry. Research-drafted by a pupil, graded by the 3-lens panel + sensei.
> Corrections applied inline; unverifiable gaps marked ⚠ PENDING — never guessed.

## What this guide is about

When you chat with Claude in a browser, each new conversation starts fresh — Claude remembers nothing from yesterday. But if you are building a program (called an **agent**) that uses Claude to do work automatically, you often need it to remember things across many conversations. This guide explains the main approaches and the traps to avoid.

You do not need to be a programmer to read this, but some practices include short code examples. Treat those examples as illustrations of the concept — you do not need to run them to understand the idea.

## How to read the labels
- ✅ **independently-corroborated** — 2+ independent publishers
- 📄 **vendor-documented** — official docs only (authoritative, single source)
- ⚠️ **WARNING** — a default that can cost money, break the machine, or remove a safety net
- 🕒 **verify live** — fast-moving (versions/prices/quotas); check the current value

---

## Practice: Before writing any code, decide WHERE each piece of information will live

**Do:** Think of your agent's information as belonging to one of four "places" (called memory tiers):

1. **In-context** — facts you type directly into the conversation right now (the system prompt or the message itself). Easy to start with, but the space is limited and you pay for every word on every request.
2. **External storage** — a database, a set of files, or a vector store (a searchable collection of text) that your agent looks up when it needs something. Scales well but adds extra steps and possible failure points.
3. **In-weights** — knowledge already baked into the model when Anthropic trained it. Your agent can use this knowledge for free, but you cannot update it at runtime. It goes out of date as the world changes.
4. **Cache memory** — a speed-and-cost optimisation where the API remembers a prompt you have sent before, so you pay less to re-read it. (More on this in later practices.)

Choose the right tier for each piece of data based on how long it needs to last and how often it changes — not based on what is quickest to code.

**Why (beginner):** Most beginners put everything into the conversation (in-context) because it feels natural. This works fine for small projects. But as the agent's history grows, you pay for every past message on every new request, and the agent's accuracy drops. Planning ahead prevents a refactor later.

**Caveat:** This four-tier framing is a useful mental model drawn from Anthropic engineering writing and practitioner experience — it is not an official Anthropic API term. Anthropic's own engineering pages discuss these concepts but do not use the exact "four tiers" label.

**Sources:** [anthropic.com/engineering/effective-context-engineering-for-ai-agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) (fetched 2026-07-07) · [anothercodingblog.com/p/persistent-memory-for-claude-agents](https://www.anothercodingblog.com/p/persistent-memory-for-claude-agents) (fetched 2026-07-07)

**Confidence:** ✅ independently-corroborated (the "four tiers" label is a synthesized mental model, not directly stated in either source; sources confirm the underlying tiers as concepts)

---

## Practice: Treat the conversation history as a limited budget — trim it, do not let it pile up

**What is a context window?** Every time you send a message to Claude, the entire conversation so far — every message, every tool result, every system instruction — is sent along with it. The maximum amount of text that can be included in a single request is called the **context window**, measured in **tokens** (roughly, one token equals about three-quarters of an English word).

**Do:** Keep an eye on how many tokens you are using. The Anthropic Python SDK gives you this information after every response in a field called `usage`:

- `response.usage.input_tokens` — tokens you sent
- `response.usage.output_tokens` — tokens Claude sent back

You can also call the token-counting API endpoint before sending a long prompt to estimate cost before committing. As the conversation grows, remove or summarise old messages that are no longer relevant to the current task. Keep tool definitions (instructions that tell Claude what tools it can use) as short as possible — they count against the budget even when the tools are never used.

**Why (beginner):** You are billed for every input token on every request. A conversation that started with a 10 000-token history now sends 10 000 extra tokens every single turn — even for a one-word reply. This adds up fast and can produce a large unexpected bill. Additionally, a very long context window does not help Claude think better; accuracy and recall can actually get worse as the history grows, even before you hit the hard limit.

**Caveat / ⚠️ WARNING:** Current flagship models (Fable 5, Opus 4.8, Sonnet 5, Sonnet 4.6 [legacy], Mythos 5) have a default context window of 1 million tokens — large enough that you can accidentally accumulate a huge history before hitting a wall. Every token in that history is billed on every request. Also note: Opus 4.7 and newer models (Fable 5, Sonnet 5) use a new tokeniser that produces approximately 30% more tokens for the same text than earlier models — so your costs can jump when you upgrade. Haiku 4.5 has a smaller 200k context window (not 1M). 🕒 **verify live** — model lineup and context window sizes change frequently; check [platform.claude.com/docs/en/build-with-claude/context-windows](https://platform.claude.com/docs/en/build-with-claude/context-windows) before building.

**Sources:** [platform.claude.com/docs/en/build-with-claude/context-windows](https://platform.claude.com/docs/en/build-with-claude/context-windows) (fetched 2026-07-07) · [anthropic.com/engineering/effective-context-engineering-for-ai-agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) (fetched 2026-07-07)

**Confidence:** ✅ independently-corroborated

---

## Practice: Use server-side compaction to automatically summarise long conversations — do not build your own summariser

**What is compaction?** When a conversation gets very long, the API can automatically summarise the older parts and replace them with a compact summary. This is called **compaction**. It frees up space in the context window so the conversation can continue. You enable it through your code rather than doing it manually.

**What is a beta header?** Some Anthropic features are in preview ("beta") and must be explicitly opted into. You do this by adding a special line to your API request called a **beta header**. In Python it looks like this:

```python
client.messages.create(
    ...,
    extra_headers={"anthropic-beta": "compact-2026-01-12"}
)
```

**Do:** For conversations that regularly approach their context window limit, enable the `compact_20260112` strategy via the `context_management` parameter (beta header: `anthropic-beta: compact-2026-01-12`). Always append the full API response — including the `compaction` block — to your message list when you continue the conversation; the API automatically treats everything before the compaction block as summarised. To control costs, track compaction events and cap total spending with a cumulative token budget. If you also use prompt caching (where a cached system prompt is stored so you pay less to re-send it), a cached system prompt stays cached even after compaction.

**Why (beginner):** Writing your own summariser means you have to tune the summary prompt, test edge cases, and keep the summary in sync with the real conversation. Server-side compaction moves all of that complexity to the API. Supported models as of 2026-07-07 include Fable 5, Mythos 5, Mythos Preview, Opus 4.8, Opus 4.7, Opus 4.6, Sonnet 5, and Sonnet 4.6 — check the docs for the current list. 🕒 **verify live.**

**Caveat / ⚠️ WARNING — Hidden billing trap:** Compaction triggers an additional processing step that is billed as extra tokens. The summary step's token costs are NOT included in the top-level `input_tokens` and `output_tokens` fields of the API response — those fields show only the main request. To see your real total bill you must sum all entries in the `usage.iterations` array:

```python
total_tokens = sum(
    it.get("input_tokens", 0) + it.get("output_tokens", 0)
    for it in response.usage.iterations
)
```

If you only check the top-level fields, you will undercount your bill. 🕒 **verify live** — supported model list and response shape may change; check the compaction docs.

**Sources:** [platform.claude.com/docs/en/build-with-claude/compaction](https://platform.claude.com/docs/en/build-with-claude/compaction) (fetched 2026-07-07) · [anthropic.com/engineering/effective-context-engineering-for-ai-agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) (fetched 2026-07-07)

**Confidence:** ✅ independently-corroborated

---

## Practice: Use the memory tool to give your agent a file-based notepad that survives between conversations

⚠️ **WARNING — Path traversal (read this before you implement anything):** When your agent writes to or reads from files, a malicious path like `/memories/../../secrets.env` can escape the intended folder and reach files that contain API keys or other secrets. Your code must check that every path starts with `/memories` and stays inside that folder. Use your language's built-in path utilities (for example, Python's `pathlib.Path.resolve()` and `relative_to()`) and reject any path containing `../` or the URL-encoded version `%2e%2e%2f`. The SDK does not do this check for you — it is your responsibility. Failure here means an attacker (or a confused agent) could read or overwrite your environment files and steal your API keys.

**What is the memory tool?** It is a built-in tool you can add to your agent. Once added, Claude can read and write a set of small text files — its "notepad" — so it can pick up where it left off in the next conversation.

**Do:** Add `{"type": "memory_20250818", "name": "memory"}` to your tools list. Then implement a handler — a piece of your code that actually saves and loads the files — that supports six commands: `view`, `create`, `str_replace`, `insert`, `delete`, and `rename`. The storage location is under your control: a local folder, a database, or a cloud bucket. Apply path validation as described in the warning above. The SDK ships a ready-made local filesystem implementation (`BetaLocalFilesystemMemoryTool` for Python and TypeScript) so you do not have to write the handler from scratch. Tell Claude to read the `/memories` directory at the start of every session, and to write progress notes as it works. Store many small focused files rather than one big file.

**Why (beginner):** Without memory files, every new conversation starts completely blank. The agent re-reads the whole codebase, re-asks questions you already answered, and may undo work from the previous session. The memory tool solves this by giving the agent a place to store exactly the facts it needs for next time. You own the storage, so you can read, edit, or delete the files at any time. The API automatically adds an instruction to Claude's system prompt telling it to check the memory directory first — you do not need to write that instruction yourself.

**Caveat:** The memory tool works only on Claude 4 and later models. No beta header is required for the tool definition itself. The SDK helper runner (`client.beta.messages.tool_runner`) lives in a beta namespace even though the tool itself is generally available — 🕒 **verify live** that the SDK namespace has not changed in a recent release.

**Sources:** [platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool](https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool) (fetched 2026-07-07) · [leoniemonigatti.com/blog/claude-memory-tool.html](https://www.leoniemonigatti.com/blog/claude-memory-tool.html) (fetched 2026-07-07) · [anothercodingblog.com/p/persistent-memory-for-claude-agents](https://www.anothercodingblog.com/p/persistent-memory-for-claude-agents) (fetched 2026-07-07)

**Confidence:** ✅ independently-corroborated

---

## Practice: For Managed Agents (a hosted agent service), use memory stores and keep each memory file under 100 kB

**What are Managed Agents memory stores?** Managed Agents is an Anthropic hosted service for running agents. It provides **memory stores** — a managed, versioned place to keep persistent data across agent sessions. Every time your agent writes a memory, the old version is preserved so you can recover it. This is safer than raw files for production use.

**Do:** Create a memory store with `client.beta.memory_stores.create(...)`. This requires the beta header `managed-agents-2026-04-01` — add it to requests as `extra_headers={"anthropic-beta": "managed-agents-2026-04-01"}`. Attach the store to a session via the `resources[]` array when you create the session — you cannot add or remove stores while a session is already running. Set `access: "read_only"` for reference material the agent should read but must not overwrite. Keep each memory file small and focused: the hard limit is 100 kB (roughly 25 000 tokens) per memory and 2 000 memories per store. Use the `content_sha256` precondition when updating a memory to avoid two processes overwriting each other's changes at the same time. A maximum of 8 memory stores can be attached per session.

**PII** means personally identifiable information — names, email addresses, phone numbers, location data. Be deliberate about what PII you store in a memory store.

**Archiving a store** is an explicit API call (`.archive()`). It does not happen automatically. Once archived, the store becomes read-only and cannot be unarchived; the data is preserved but can no longer be written to.

**Why (beginner):** Memory stores give you an auditable, versioned history of everything your agent has remembered. If the agent accidentally overwrites something important, you can retrieve the previous version. This is especially valuable when multiple agents run in parallel and might write to the same memory at the same time.

**Caveat / ⚠️ WARNING — Prompt injection:** Memory stores attached with the default `read_write` permission are vulnerable to **prompt injection** — an attack where malicious text in the agent's input (a user message, a webpage the agent fetches, output from a third-party tool) tricks the agent into writing harmful content into the memory store. Future sessions then read that harmful content as if it were trusted memory. To reduce this risk, set `access: "read_only"` for any store the agent does not genuinely need to write to. 🕒 **verify live** — beta header and feature availability may change. Check whether your plan tier includes this feature — free and developer tiers may not.

**Sources:** [platform.claude.com/docs/en/managed-agents/memory](https://platform.claude.com/docs/en/managed-agents/memory) (fetched 2026-07-07) · [anothercodingblog.com/p/persistent-memory-for-claude-agents](https://www.anothercodingblog.com/p/persistent-memory-for-claude-agents) (fetched 2026-07-07)

**Confidence:** ✅ independently-corroborated

---

## Practice: Use the Files API to upload large documents once instead of re-sending them on every request

**What is the Files API?** It is a way to upload a file (a PDF, a text document, an image) to Anthropic's servers once, get back a short ID, and then refer to that ID in future requests instead of re-sending the whole file every time.

**Do:** Upload a document once with `client.beta.files.upload(...)` and save the `file_id` it returns. In later requests, refer to the file using that ID as a `document`, `image`, or `container_upload` content block instead of sending the raw bytes again. Note: file content is still billed as input tokens each time you reference it in a request; the upload, list, and delete operations themselves are free. Delete files you no longer need so you stay within your organisation's storage quota. Add the beta header `"anthropic-beta: files-api-2025-04-14"` to your requests.

**Why (beginner):** If your agent refers to the same user manual or knowledge base on every turn, re-uploading it each time wastes bandwidth and slows down the response. The Files API lets you upload it once and reference it cheaply. Files up to 500 MB are supported.

**Caveat / ⚠️ WARNING — No ZDR:** **Zero Data Retention (ZDR)** is an enterprise contract option where Anthropic promises not to store your prompts or outputs on their servers after the API call finishes. The Files API is explicitly NOT eligible for ZDR. This means that if your use case requires ZDR — for example, because you are handling sensitive user data — you must not use the Files API. Your uploaded files are retained under Anthropic's standard data retention policy. Check [anthropic.com/privacy](https://www.anthropic.com/privacy) for current data handling details. Free and developer plan tiers do not include ZDR at all.

**Caveat:** Files you upload have `"downloadable": false` — you cannot retrieve the raw bytes back through the API later. The Files API is still in beta as of 2026-07-07 (beta header required) and is not yet available on Amazon Bedrock or Google Cloud. 🕒 **verify live** — availability and limits may change.

**Sources:** [platform.claude.com/docs/en/build-with-claude/files](https://platform.claude.com/docs/en/build-with-claude/files) (fetched 2026-07-07)

**Confidence:** 📄 vendor-documented

---

## Practice: Use context editing to automatically clear out old, used-up tool results during long agent runs

**What are tool results?** When your agent uses a tool — for example, it searches the web or reads a file — the result of that search or file read gets added to the conversation history. Over a long agent run, dozens of these results pile up in the context window even though the agent has already acted on them and does not need them anymore.

**What is context editing?** It is a server-side feature (meaning the API handles it, not your code) that removes old tool results from the prompt before it reaches the model, freeing up context window space.

**What are thinking blocks?** Some models can show their internal reasoning steps (called **thinking blocks** or **extended thinking**). These also accumulate in the context window as tokens that cost money.

**Do:** For agent workflows with heavy tool use, add a `clear_tool_uses_20250919` edit to your `context_management` configuration (beta header: `anthropic-beta: context-management-2025-06-27`). Set a `trigger` token threshold (for example, 30 000 tokens) and a `keep` count of recent results to preserve. If you are using extended or adaptive thinking, add a `clear_thinking_20251015` edit BEFORE the tool-result clearing edit — order matters. Pair context editing with the memory tool so Claude can write important findings to memory before old tool results are cleared.

**Why (beginner):** Without context editing, old tool results pile up and waste your token budget. Context editing clears them on the server side before billing, freeing space for the current task. Your application always keeps the full unmodified history — only the copy sent to the model is trimmed.

**Caveat:** Use `clear_at_least` to make sure clearing is worth the cost it triggers (clearing can invalidate your prompt cache, which means you pay to re-cache). Context editing currently works best with custom tools; token counting may be inaccurate for server-side tools. This feature is still in beta as of 2026-07-07.

**Sources:** [platform.claude.com/docs/en/build-with-claude/context-editing](https://platform.claude.com/docs/en/build-with-claude/context-editing) (fetched 2026-07-07) · [platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool](https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool) (fetched 2026-07-07, see "Using with compaction" section)

**Confidence:** 📄 vendor-documented

---

## Practice: Use adaptive thinking for complex single-request reasoning — it does not replace memory between sessions

**What is adaptive thinking?** Some Claude models can be told to "think harder" about a difficult problem before answering. This is called **adaptive thinking** (or extended thinking). The model works through reasoning steps internally, and you can choose how much effort it puts in. It is useful for complex multi-step problems.

**Do:** For current flagship models (Fable 5, Opus 4.8, Sonnet 5), enable adaptive thinking with `"thinking": {"type": "adaptive"}` and an `effort` level — choose from `"low"`, `"medium"`, `"high"`, or `"max"` — for genuinely complex requests such as proofs, intricate analysis, or choosing between tools:

```python
response = client.messages.create(
    model="claude-fable-5-20260609",
    max_tokens=16000,
    thinking={"type": "adaptive"},
    effort="high",
    messages=[...]
)
```

Do not rely on thinking blocks to carry information across sessions — they are isolated to a single request and disappear when it ends. When passing thinking blocks back in a tool-use loop, include them exactly as received and completely unmodified — the API cryptographically signs them and returns a 400 error if you alter them. For work that needs memory across multiple sessions, combine adaptive thinking with the memory tool or memory stores.

**Why (beginner):** Adaptive thinking makes Claude better at hard problems within one request. But it is not a memory system — as soon as the request is done, the thinking is gone. If you need the agent to remember something for next time, write it to a memory file instead.

**Caveat / ⚠️ WARNING — You are billed for thinking even when you hide it:** If you use `display: "omitted"` to suppress the thinking steps from the response (so you do not see them), you are still charged for all the thinking tokens. There is no cost saving from hiding thinking.

**Caveat — Legacy API:** An older way to enable thinking used `{"type": "enabled", "budget_tokens": N}`. This still works on Claude Opus 4.5, Sonnet 4.5, Haiku 4.5, Sonnet 4.6, and Opus 4.6. However, it is deprecated on Sonnet 4.6 and Opus 4.6, and it is completely unsupported on Fable 5, Opus 4.8, Sonnet 5, and all subsequent flagship models. If you are using a current model and you pass `budget_tokens`, you will receive a 400 error. Migrate to the `effort` / adaptive API shown above.

🕒 **verify live** — model support and thinking mechanics change with new model releases; check [platform.claude.com/docs/en/build-with-claude/extended-thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking) before building.

**Sources:** [platform.claude.com/docs/en/build-with-claude/extended-thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking) (fetched 2026-07-07) · [platform.claude.com/docs/en/about-claude/models/overview](https://platform.claude.com/docs/en/about-claude/models/overview) (fetched 2026-07-07)

**Confidence:** 📄 vendor-documented

---

## Practice: For agents that run in multiple sessions, set up a "notes file" in a short first session before the real work begins

**Do:** Before your main agent loop starts, run a short "initialiser" session. Have the agent create:

- A **progress log** — what has been done and what comes next.
- A **task checklist** — each feature or task with an explicit pass/fail status.
- A **reference to any environment-setup script** — so later sessions know how the environment was prepared.

Have every subsequent "worker" session begin by reading those memory files before doing anything else. At the end of each session, update the progress log. Commit code changes with descriptive messages using **git** — a version-control tool that tracks every file change and lets you roll back to any earlier state — to give the agent a recoverable audit trail. Work on one feature at a time and mark it complete only after end-to-end verification, not just after the code is written.

**Why (beginner):** Without an initialiser session, each new session re-explores the codebase from scratch, wastes tokens re-discovering decisions already made, and risks duplicating or reversing earlier work. Anthropic's engineering team documents this pattern as the recommended approach for long-running autonomous coding agents. One practitioner reported that "Session 2 cost five times less than Session 1 because the agent read existing notes instead of recomputing."

**Caveat:** This pattern is most valuable when sessions are interrupted or run on a schedule. For work that completes in a single run, the initialiser adds overhead and may not be worth it. The progress file is only as good as the discipline applied to updating it — if the agent skips the update step (which can happen on model errors), the next session starts with stale notes.

**Sources:** [anthropic.com/engineering/effective-harnesses-for-long-running-agents](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents) (fetched 2026-07-07) · [anothercodingblog.com/p/persistent-memory-for-claude-agents](https://www.anothercodingblog.com/p/persistent-memory-for-claude-agents) (fetched 2026-07-07) · [platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool](https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool) (fetched 2026-07-07, see "Multi-session software development pattern" section)

**Confidence:** ✅ independently-corroborated

---

## Held pending fixes (not publish-ready)

- MCP knowledge-graph memory server (`@modelcontextprotocol/server-memory`) — GitHub repo listing confirmed the server exists but detailed capabilities, limits, and best practices require fetching the `/src/memory` subdirectory or dedicated docs page. Holding as thin. ⚠ PENDING

## CHANGELOG (grading → this entry)

**Re-leveled by rings-beginner-author for beginner track** (2026-07-07). All facts, source URLs, and Confidence labels are unchanged from the technical entry dated 2026-07-07. No new facts or URLs were introduced.

Summary of re-leveling changes:

1. Front matter updated: `track: beginner`, `audience: "people new to AI"`, title updated to include "Beginner Guide".
2. Added a plain-English introduction section explaining what the guide covers and who it is for.
3. Expanded every jargon term on first use: context window, tokens, beta header, ZDR (Zero Data Retention), compaction, thinking blocks / extended thinking / adaptive thinking, prompt injection, PII, memory stores, tool results, context editing, git.
4. Each practice now leads with a plain "What is X?" paragraph before the Do/Why/Caveat structure, so readers understand the concept before they see implementation details.
5. Strengthened "Why (beginner)" sections with concrete failure descriptions: unexpected billing, stale agent state, stolen API keys, prompt injection, hidden compaction costs.
6. All ⚠️ WARNING blocks preserved verbatim in content, with additional plain-English framing of the concrete harm each warning prevents.
7. All 🕒 verify live tags preserved.
8. Held pending section carried over unchanged.
9. Inherited CHANGELOG items 1–12 from the technical entry are represented by the grading_result field; this CHANGELOG entry covers only the re-leveling step.

