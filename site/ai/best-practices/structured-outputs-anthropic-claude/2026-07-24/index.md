# Structured Outputs and Tool Use with Claude APIs — Best Practices (as of 24 Jul 2026)

> Concrete, sourced best practices for getting reliable structured output from the Anthropic Claude API using tool use, caching, streaming, and related techniques.


<!-- This file lands at content/ai/best-practices/structured-outputs-anthropic-claude/2026-07-24/index.md and is an IMMUTABLE
     dated snapshot. Once published it is never edited — a refresh is a NEW <snapshot-date> dir.
     "Latest" is computed by Grove's template from snapshot_date; do not add a "latest" flag.
     Source tiers: independently-corroborated = 2+ DIFFERENT publishers; vendor-documented =
     official vendor docs only (authoritative, single source). -->

# Structured Outputs and Tool Use with Claude APIs (as of 24 Jul 2026)

> **Grading note.** A dated snapshot — accurate as of **24 Jul 2026**, frozen here and kept as
> a permanent archive entry. Research-drafted by a pupil, graded by the 3-lens panel + sensei.
> Corrections applied inline; unverifiable gaps marked ⚠ PENDING (#issue) — never guessed.

## How to read the labels
- ✅ **independently-corroborated** — 2+ independent publishers
- 📄 **vendor-documented** — official docs only (authoritative, single source)
- ⚠️ **WARNING** — a default that can cost money, break the machine, or remove a safety net
- 🕒 **verify live** — fast-moving (versions/prices/quotas); check the current value

---

**Prerequisites:** An Anthropic account and API key ([console.anthropic.com](https://console.anthropic.com)), and the `anthropic` SDK installed (`pip install anthropic` or `npm install @anthropic-ai/sdk`). API calls cost money — check current pricing at [anthropic.com/pricing](https://www.anthropic.com/pricing) before building a loop.

---

## Practice: Use tool use (tool_use blocks) as the primary method for structured output

**Do:** Define tools with a `name`, `description`, and `input_schema` (JSON Schema) in the `tools` array. When Claude responds, check for content blocks of `type: "tool_use"` and parse the `input` field as your structured data. Do not attempt to parse free-text JSON from a plain assistant message as your first approach.

**Why (beginner):** When you ask Claude to "return JSON", it may add conversational text before or after the JSON, add markdown code fences, or format it differently than you expect. Tool use tells Claude to fill in a specific form (your schema) and return it in a machine-readable block, separate from any explanatory text. This is much easier to parse reliably.

**Caveat / contested:** Tool use adds some overhead: the API injects a tool-use system prompt that costs extra tokens (290–500+ tokens depending on model and `tool_choice` setting, 🕒 verify live). For very simple single-value extraction where the overhead matters, the prefill technique (see below) is an alternative, but with its own tradeoffs.

**Sources:** [platform.claude.com — Tool use overview](https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview) (2026-07-24) · [platform.claude.com — Handle tool calls](https://platform.claude.com/docs/en/agents-and-tools/tool-use/handle-tool-calls) (2026-07-24)

**Confidence:** 📄 vendor-documented

---

## Practice: Add `strict: true` to tool definitions to guarantee schema conformance

⚠️ **WARNING (Privacy/Legal):** Never put real patient names, diagnoses, or other PHI (protected health information) in schema field names, `enum` values, `const` values, or `pattern` fields. Tool schema definitions are cached for schema-compilation purposes for up to 24 hours and do not receive the same PHI protections as message content.

**Do:** Set `"strict": true` alongside `name`, `description`, and `input_schema` in your tool definition. Also add `"additionalProperties": false` to your schema. This uses grammar-constrained sampling (the model's token generation is constrained to only produce schema-valid output).

**Why (beginner):** Without strict mode, Claude might return a string `"2"` where you declared an integer, or skip an optional field entirely. Strict mode eliminates these type mismatches. You receive `passengers: 2` instead of `passengers: "two"`, and you never need to write retry logic for malformed inputs.

**Caveat / contested:** Strict mode supports a subset of JSON Schema. Supported features include `anyOf` (with limitations), `$ref`, `$def`, and `definitions`. Unsupported: `oneOf`, external HTTP `$ref` (URLs as `$ref` targets), recursive schemas, numerical range constraints (`minimum`, `maximum`, `multipleOf`), and string length constraints (`minLength`, `maxLength`). 🕒 Verify the current supported/unsupported list at [platform.claude.com — Structured outputs](https://platform.claude.com/docs/en/build-with-claude/structured-outputs) as this list evolves.

**Sources:** [platform.claude.com — Strict tool use](https://platform.claude.com/docs/en/agents-and-tools/tool-use/strict-tool-use) (2026-07-24) · [platform.claude.com — Structured outputs](https://platform.claude.com/docs/en/build-with-claude/structured-outputs) (2026-07-24)

**Confidence:** 📄 vendor-documented

---

## Practice: Force a specific tool call with `tool_choice: {type: "tool", name: "..."}`

**Do:** When you need Claude to always fill in a particular schema (not decide whether to call it), set `tool_choice: {"type": "tool", "name": "my_tool"}` in the request. For structured extraction tasks, this replaces the need to prompt "please respond as JSON".

**Why (beginner):** By default (`tool_choice: "auto"`), Claude decides on its own whether to call a tool or just answer in plain text. If you define an extraction schema but Claude feels confident enough to answer directly, it will skip the tool call and return prose. Forcing the tool call guarantees you always get the `tool_use` block with a filled-in `input` field.

**Caveat / contested:** ⚠️ WARNING: `tool_choice: {"type": "tool"}` and `tool_choice: {"type": "any"}` are **incompatible with extended thinking (thinking mode)**. Sending these in the same request as `thinking: {type: "adaptive"}` or `thinking: {type: "enabled"}` returns a 400 error. Use `tool_choice: "auto"` when thinking is active. Additionally, forced tool use is **not supported on Claude Mythos Preview** (`claude-mythos-preview`), which was retired 2026-07-21 — do not use that model alias. When using forced tool choice, the API prefills the assistant turn to force the tool call, which means Claude will not emit a natural-language explanation before the `tool_use` block.

**Sources:** [platform.claude.com — Define tools](https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools) (2026-07-24) · [platform.claude.com — Extended thinking](https://platform.claude.com/docs/en/build-with-claude/thinking) (2026-07-24)

**Confidence:** 📄 vendor-documented

---

## Practice: Handle all parallel tool_use blocks before sending tool_result blocks back

**Do:** A single Claude response can contain multiple `tool_use` blocks in one turn (parallel tool calls). Collect all of them, execute them (concurrently if they are independent read-only operations, sequentially if they have side effects or ordering dependencies), and return all `tool_result` blocks together in a single `user` message. Each `tool_result` must reference the correct `tool_use_id`. Put all `tool_result` blocks before any `text` content in the `content` array.

**Why (beginner):** If you only return results for some of the tool calls and skip others, the API will error or lose track of the conversation. Claude is waiting for all the information it asked for before it can continue. Think of it like asking a friend two questions at once — you need to answer both before they can reply.

**Caveat / contested:** ⚠️ WARNING: Text content placed before `tool_result` blocks in the user message causes a 400 error. The API also requires tool results to come immediately after the assistant turn that made the calls — you cannot insert any other messages in between. If you choose not to execute one of the calls (e.g., a preceding call failed), still return a `tool_result` for it with `is_error: true` and an explanation, or the conversation will break. To disable parallel tool calls entirely (force one at a time), set `tool_choice: {"type": "auto", "disable_parallel_tool_use": true}`.

**Sources:** [platform.claude.com — Parallel tool use](https://platform.claude.com/docs/en/agents-and-tools/tool-use/parallel-tool-use) (2026-07-24) · [platform.claude.com — Handle tool calls](https://platform.claude.com/docs/en/agents-and-tools/tool-use/handle-tool-calls) (2026-07-24)

**Confidence:** 📄 vendor-documented

---

## Practice: Accumulate streaming tool_use blocks via `input_json_delta` events before parsing

**Do:** When streaming is enabled (`"stream": true`), the API sends a series of small JSON objects called events over the connection. Each event has a `type` field. For tool use, the relevant events are:
- `content_block_start` — signals a new content block (check `content_block.type == "tool_use"` to know a tool call is starting)
- `content_block_delta` with `delta.type: "input_json_delta"` — carries a `delta.partial_json` string fragment of the tool's input JSON
- `content_block_stop` — signals the tool call is complete

Concatenate all `partial_json` strings for a given block index until you receive `content_block_stop`, then parse the complete JSON. Do not attempt to parse partial JSON mid-stream unless you use a partial-JSON library.

**Why (beginner):** Streaming delivers the tool input one chunk at a time, like receiving a letter word by word. The individual chunks are not valid JSON on their own. You must assemble the full string before parsing. The official SDKs (Python, TypeScript, Go, etc.) handle this accumulation automatically.

**Caveat / contested:** The official docs note that current models only emit one complete key-value pair from `input` at a time, so there can be pauses between `input_json_delta` events while the model works on the next field. This is expected behavior, not a network error. For lower latency on individual parameter values, the `eager_input_streaming` per-tool flag is available (🕒 verify current availability at [platform.claude.com — Fine-grained tool streaming](https://platform.claude.com/docs/en/agents-and-tools/tool-use/fine-grained-tool-streaming)).

**Sources:** [platform.claude.com — Streaming](https://platform.claude.com/docs/en/build-with-claude/streaming) (2026-07-24)

**Confidence:** 📄 vendor-documented

---

## Practice: Cache tool definitions by placing `cache_control: {type: "ephemeral"}` on the last tool in the list

**Do:** If you send the same set of tool definitions on many requests (e.g., a customer-service agent that always has the same tools), add `"cache_control": {"type": "ephemeral"}` to the last tool in the `tools` array. This caches all tools up to and including that point. Cache reads cost approximately 10% of normal input token prices; cache writes cost 125% (5-minute TTL) or 200% (1-hour TTL). 🕒 verify live pricing.

**Why (beginner):** Every time you call the API, tool definitions go through the model as input tokens and cost money. If your tools never change between calls, you are paying full price each time for the same text. Caching stores the compiled result so subsequent calls read from cache at a fraction of the cost.

**Caveat / contested:** ⚠️ WARNING: Changing any tool definition, or changing the `tool_choice` parameter, invalidates the cache for message-level blocks. Tool and system-prompt caches survive a `tool_choice` parameter change; message-content caches do not. The minimum prompt length required before caching kicks in varies by model — 🕒 verify the current per-model thresholds at [platform.claude.com — Prompt caching](https://platform.claude.com/docs/en/build-with-claude/prompt-caching), as the table is detailed and changes with new model releases. As of 2026-07-24: 512 tokens for Fable 5 and Mythos 5; 1,024 tokens for Opus 4.8, Sonnet 5, Sonnet 4.6, and Sonnet 4.5; 2,048 tokens for Opus 4.7; 4,096 tokens for Haiku 4.5 and older Opus generations. Also: changing the thinking configuration (`budget_tokens`, mode) invalidates cache breakpoints.

**Sources:** [platform.claude.com — Prompt caching](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) (2026-07-24) · [platform.claude.com — Define tools](https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools) (2026-07-24)

**Confidence:** 📄 vendor-documented

---

## Practice: Use `search_result` blocks with `citations: {enabled: true}` for attributed RAG responses

**Do:** For retrieval-augmented generation (RAG) where you want Claude to cite its sources, pass retrieved documents as `search_result` content blocks (not plain text). Each block requires `type: "search_result"`, a `source` string (URL or internal identifier), a `title`, and a `content` array of text blocks. Set `"citations": {"enabled": true}` on each block. All search results in one request must use the same citations setting.

**Why (beginner):** When you paste retrieved text into a plain user message, Claude can use it but will not tell you which sentence came from which source. Using `search_result` blocks with citations enabled causes Claude to automatically annotate its response with source attributions — useful for fact-checking, legal, or medical applications where users need to verify claims.

**Caveat / contested:** Citations are disabled by default; you must opt in on every search result block. The feature supports text content only — images and other media are not supported inside `search_result` content arrays. No beta header is required as of the fetch date; it is part of the standard Messages API. Supported on all active Claude models except Claude Haiku 3. 🕒 Verify model support live.

**Sources:** [platform.claude.com — Search results and citations](https://platform.claude.com/docs/en/build-with-claude/search-results) (2026-07-24)

**Confidence:** 📄 vendor-documented

---

## Practice: When using extended thinking with tool use, pass thinking blocks back unmodified and handle both block types

**Do:** When thinking is active and Claude calls a tool, the response contains both `thinking` content blocks and `tool_use` blocks. When you return the tool result, include the full original assistant message (including all `thinking` blocks) in the conversation history. Pass thinking blocks back exactly as received — do not edit, reorder, or drop them (including any `redacted_thinking` blocks). Parse tool inputs from `tool_use` blocks, not from thinking blocks.

**Why (beginner):** Claude's thinking blocks contain the encrypted record of its reasoning. When you return the tool result and ask Claude to continue, it needs its earlier reasoning to pick up where it left off. Dropping the thinking blocks is like erasing someone's notes mid-problem — the model can continue, but it silently loses reasoning continuity and quality.

**Caveat / contested:** ⚠️ WARNING: Modified thinking blocks are rejected with a 400 error. If you filter content blocks by type (e.g., `block.type == "thinking"`) when building the round-trip history, also include `redacted_thinking` blocks — filtering on `"thinking"` alone silently drops them. Also, thinking is **incompatible** with `tool_choice: {"type": "any"}` and `tool_choice: {"type": "tool", ...}` — those return a 400 error.

Extended thinking (`type: "enabled"`) is currently supported **only on Claude Haiku 4.5** among active models; it is deprecated on Opus 4.6 and Sonnet 4.6, and unavailable on Opus 4.7, Opus 4.8, Sonnet 5, Fable 5, or Mythos 5. Use **adaptive thinking** (`type: "adaptive"`) on those models instead. 🕒 Verify which models support which thinking mode at the live models overview.

**Sources:** [platform.claude.com — Extended thinking](https://platform.claude.com/docs/en/build-with-claude/thinking) (2026-07-24) · [platform.claude.com — Extended thinking (detailed)](https://platform.claude.com/docs/en/build-with-claude/extended-thinking) (2026-07-24) · [platform.claude.com — Models overview](https://platform.claude.com/docs/en/about-claude/models/overview) (2026-07-24)

**Confidence:** 📄 vendor-documented

---

## Practice: Use assistant-turn prefilling (`{"`) to coerce plain JSON — only on supported models, and only when tool use is impractical

**Do:** On models that support it, open the assistant turn with the first character of your expected JSON (e.g., `{"`) to bypass Claude's conversational preamble and force a JSON opening. The Claude API takes a `messages` array where each entry has a `role` (`"user"` or `"assistant"`) and a `content` field. Normally you only add `user` messages and Claude fills in the `assistant` messages. Prefilling means you add an `assistant` message yourself with just `{"` as the content — Claude then continues from that character, skipping any conversational opener.

**Why (beginner):** Without prefilling, Claude typically opens with "Sure, here is the JSON: ..." which you then have to strip before parsing. Starting the assistant turn with `{"` commits Claude to producing a JSON object from token one.

**Caveat / contested:** ⚠️ WARNING: Prefilling is **not supported** on Claude Fable 5, Claude Mythos 5, Claude Opus 4.8, Claude Opus 4.7, Claude Opus 4.6, and Claude Sonnet 4.6. Attempting it on those models will fail or be ignored. On models where it is supported, prefilling carries a **refusal risk**: if the requested content falls into a category Claude would normally decline, the output can stop mid-generation. For any production pipeline that uses prefilling, always validate that the output is complete and parseable before using it. The Anthropic documentation explicitly recommends using structured outputs (or tool use) on models that support them, instead of prefilling.

**Sources:** [platform.claude.com — Increase consistency](https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/increase-consistency) (2026-07-24)

**Confidence:** 📄 vendor-documented

---

## Practice: Keep tool result content terse — return only what Claude needs to decide the next step

**Do:** When formatting `tool_result` blocks, return the minimum information Claude needs to reason about the next step and produce a final answer. Prefer semantic identifiers (slugs — short readable IDs like `acme-invoice-2026` — and UUIDs — machine-generated unique identifiers like `a3f2...`) over raw database dumps. Omit fields Claude does not need. If a result is large (e.g., a full web page), summarize or truncate before sending it back.

**Why (beginner):** Claude re-reads every `tool_result` block in the context window on every subsequent API call. A 10,000-token tool result that could be 200 tokens costs 50x more in input tokens per call — and these costs compound across every turn in a multi-step conversation. Verbose results also make it harder for Claude to find the signal it needs.

**Caveat / contested:** There is a real tension here: truncating results too aggressively can cause Claude to miss key information and make wrong decisions. The right balance depends on your use case. For content from untrusted external sources (web pages, user uploads, third-party APIs), the official docs also warn to keep that content inside `tool_result` blocks rather than in the system prompt or plain user text, to reduce indirect prompt injection risk. Never paste untrusted external content into the system prompt.

**Sources:** [platform.claude.com — Define tools](https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools) (2026-07-24) · [platform.claude.com — Handle tool calls](https://platform.claude.com/docs/en/agents-and-tools/tool-use/handle-tool-calls) (2026-07-24)

**Confidence:** 📄 vendor-documented

---

## Practice: Choose the right model for your tool-use workload

**Do:** Match model to workload: use **Claude Haiku 4.5** (`claude-haiku-4-5`) for high-throughput, low-latency tool calling with straightforward schemas; use **Claude Sonnet 5** (`claude-sonnet-5`) for the best speed-intelligence balance in production tool pipelines; use **Claude Opus 4.8** (`claude-opus-4-8`) for complex multi-step agentic reasoning, ambiguous queries, or when required parameters are often missing and you need the model to ask for clarification. The official docs note that Opus models are "much more likely to recognize that a parameter is missing and ask for it" while Sonnet models "might ask, especially when prompted to think before outputting a tool request, but might also infer a reasonable value."

**Why (beginner):** Paying for Opus when Haiku would do the same job correctly wastes money and adds latency. Paying for Haiku when Opus is needed means tool calls that guess at missing parameters — producing subtly wrong results that can be hard to debug.

**Caveat / contested:** 🕒 Model names, pricing, and capability rankings change frequently — verify against the live model table. As of 2026-07-24: Claude Fable 5 ($10/$50 per MTok — million tokens), Claude Opus 4.8 ($5/$25 per MTok), Claude Sonnet 5 ($3/$15 per MTok with introductory pricing of $2/$10 through August 31, 2026), Claude Haiku 4.5 ($1/$5 per MTok). Forcing a specific tool call (`tool_choice: "tool"`) adds system prompt overhead compared to `auto`; overhead varies by model — approximately 120 extra tokens on Opus 4.8 and Sonnet 5, approximately 92 extra on Haiku 4.5. 🕒 Verify model-specific overhead at [platform.claude.com — Pricing](https://platform.claude.com/docs/en/about-claude/pricing) (tool use section). Extended thinking adds latency; plan for this in latency-sensitive pipelines. Claude Haiku 4.5 does not support interleaved thinking (adaptive mode), though it does support extended thinking (`type: "enabled"`).

**Sources:** [platform.claude.com — Models overview](https://platform.claude.com/docs/en/about-claude/models/overview) (2026-07-24) · [platform.claude.com — Define tools](https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools) (2026-07-24) · [platform.claude.com — Pricing](https://platform.claude.com/docs/en/about-claude/pricing) (2026-07-24)

**Confidence:** 📄 vendor-documented

---

## Held pending fixes (not publish-ready)
- None.

## CHANGELOG (grading → this entry)
1. Timekeeper KILL (P2): Removed `anyOf` and `$ref` from unsupported list — both ARE supported in strict mode. Corrected unsupported list to: `oneOf`, external HTTP `$ref`, recursive schemas, numeric/string range constraints. Added link to structured-outputs page.
2. Timekeeper KILL (P3): Noted `claude-mythos-preview` was retired 2026-07-21; updated caveat to reflect this.
3. Timekeeper KILL (P7): Replaced wrong two-bucket caching-threshold split with accurate per-generation values from live prompt-caching doc. Corrected Sonnet 4.5 threshold (1,024, not 4,096); added Fable 5/Mythos 5 (512) and Opus 4.7 (2,048) which were omitted.
4. Timekeeper KILL (P8): Rewrote extended thinking caveat to explicitly state Haiku 4.5 is the one current model supporting `type: "enabled"`. Omission implied the feature was gone from all models; fixed.
5. Beginner KILL: Moved PHI warning to a standalone ⚠️ block at the top of the strict-mode practice, before caveat text.
6. Timekeeper FIX: Removed November 2025 "beta" framing — Anthropic structured outputs is now GA. Updated caveat in P2 to link to the live structured-outputs page.
7. Timekeeper FIX (P11): Added model-specific tool-use overhead note (92–120+ extra tokens by model) with link to pricing page.
8. Beginner FIX (streaming): Added plain-English explanation of the streaming event types (`content_block_start`, `content_block_delta`, `input_json_delta`, `content_block_stop`) with per-event descriptions before the technical do-instruction.
9. Beginner FIX (prefilling): Added explanation of the messages array structure and what "assistant turn" means before the prefill technique.
10. Beginner FIX (prerequisites): Added prerequisites box at top of article (API key, SDK install, pricing pointer).
11. Beginner FIX (terse results): Added plain-English definitions of "slugs" and "UUIDs" on first use.

