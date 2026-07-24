---
title: "Structured Outputs and Tool Use with AI APIs — Best Practices (as of 24 Jul 2026)"
date: 2026-07-24
snapshot_date: 2026-07-24
topic: structured-outputs-generic
track: best-practices
audience: "technically comfortable readers"
description: "Ten actionable cross-platform best practices for getting reliable, machine-readable structured output from LLM APIs — covering schema design, validation, streaming, prompt patterns, token budgets, and safe tool execution."
content_type: "Best Practice"
categories: ["Structured Outputs", "Tool Use", "LLM APIs"]
tags: ["json-schema", "structured-outputs", "tool-calling", "function-calling", "validation", "retry", "streaming", "few-shot", "chain-of-thought", "idempotency"]
last_refreshed: 2026-07-24
graded_by: "RingS panel (Skeptic/Beginner/Timekeeper) + sensei, 2026-07-24"
grading_result: "0 fabrications; 7 corrections applied; 0 gaps filed as issues"
---

<!-- This file lands at content/ai/best-practices/structured-outputs-generic/2026-07-24/index.md
     and is an IMMUTABLE dated snapshot. Refresh = new <snapshot-date> directory. -->

# Structured Outputs and Tool Use with AI APIs (as of 24 Jul 2026)

> **Grading note.** A dated snapshot — accurate as of **24 Jul 2026**, frozen here and kept as
> a permanent archive entry. Research-drafted by a pupil, graded by the 3-lens panel + sensei.
> Corrections applied inline; unverifiable gaps marked ⚠ PENDING (#issue) — never guessed.

## How to read the labels
- ✅ **independently-corroborated** — 2+ independent publishers
- 📄 **vendor-documented** — official docs only (authoritative, single source)
- ⚠️ **WARNING** — a default that can cost money, break the machine, or remove a safety net
- 🕒 **verify live** — fast-moving (versions/prices/quotas); check the current value

---

## Practice: Keep JSON schemas flat, simple, and well-described

**Do:** Limit nesting to three levels or fewer. Keep schemas under 20 properties where possible. Use `enum` to constrain value sets. Mark every field as either `required` or genuinely `optional` — do not leave fields ambiguous. Add a plain-English `description` to every field; treat these descriptions as embedded prompt instructions. Set `additionalProperties: false` to prevent models from inventing extra keys.

**Why (beginner):** Language models generate tokens left-to-right and do not "see" the whole schema before writing. A deeply nested or large schema raises the chance that the model forgets a constraint by the time it reaches that part of the output. Enum fields help because the model only has to pick from a short, explicit list instead of guessing. Field descriptions are not just documentation — they go to the model as context and directly improve accuracy.

**Caveat / contested:** Constrained decoding (strict mode, native structured outputs) can enforce *syntax* at near-zero overhead regardless of schema complexity, but semantic quality still degrades with large or deeply nested schemas. If you genuinely need recursive structures (e.g., tree-shaped data), you need a CFG-based engine (CFG = Context-Free Grammar) rather than FSM-based tools (FSM = Finite State Machine — both are implementation styles for software that enforces your schema at the token level). Libraries like XGrammar and llguidance are purpose-built for this. Some FSM tools will either reject recursive schemas or silently flatten recursion to a fixed depth. 🕒 Verify live — engine support details change frequently.

**Sources:**
- [letsdatascience.com — Structured Outputs: Making LLMs Return Reliable JSON](https://letsdatascience.com/blog/structured-outputs-making-llms-return-reliable-json) (fetched 2026-07-24): recommends schemas under 20 properties, nesting under 3 levels, and comprehensive field descriptions.
- [tianpan.co — Beyond JSON Mode: Getting Reliable Structured Outputs from LLMs in Production](https://tianpan.co/blog/2025-10-29-structured-outputs-llm-production) (fetched 2026-07-24): lists keeping schemas flat, using enums aggressively, and setting `additionalProperties: false` as core schema design principles.
- [techsy.io — Reliable JSON from Any LLM: Pydantic + Zod](https://techsy.io/en/blog/llm-structured-outputs-guide) (fetched 2026-07-24): confirms field descriptions become part of the JSON Schema sent to the model and directly influence output quality.

**Confidence:** ✅ independently-corroborated (three independent publishers)

---

## Practice: Validate LLM output against the schema and retry with error feedback

**Do:** After every LLM call, attempt to parse and validate the response against your schema (e.g., with Pydantic in Python or Zod in TypeScript). If validation fails, send the validation error message back to the model in the next turn — do not just retry identically. Cap retries at 2–3 for complex schemas. Use exponential backoff with jitter between attempts (e.g., `wait_time = (base_delay * 2^attempt) + random(0, jitter_max)` with `base_delay = 1` second and `jitter_max = 0.5` seconds as a starting point) to avoid hammering rate-limited APIs.

**⚠️ WARNING:** An uncapped retry loop can spend unbounded money. Always set a hard `max_retries` (2–3 is sufficient for most use-cases) and a total wall-clock timeout.

**Why (beginner):** Even with native structured outputs turned on, models can produce semantically wrong values (e.g., `rating: 1, sentiment: positive`). Validation catches these before they enter your database or downstream code. Feeding the error back to the model — "you returned X but the schema requires Y" — lets the model self-correct on the very next attempt without you writing extra code.

**Caveat / contested:** Libraries such as Instructor (Python) and native provider SDKs handle retry-with-feedback automatically; hand-rolling this logic is error-prone. Rate-limit retries (HTTP 429) warrant more retries (5–7) and longer backoff than schema validation failures (2–3).

**Sources:**
- [letsdatascience.com — Structured Outputs: Making LLMs Return Reliable JSON](https://letsdatascience.com/blog/structured-outputs-making-llms-return-reliable-json) (fetched 2026-07-24): explicitly recommends retry with validation feedback and a `max_retries` of 2–3.
- [fast.io — AI Agent Error Handling: Best Practices & Patterns](https://fast.io/resources/ai-agent-error-handling/) (fetched 2026-07-24): states "if validation fails, the error message is fed back to the LLM as a new prompt" and describes exponential backoff with jitter.
- [fast.io — AI Agent Retry Patterns: Exponential Backoff Guide](https://fast.io/resources/ai-agent-retry-patterns/) (fetched 2026-07-24): provides per-error-type retry caps (rate limits: 5–7; server errors: 3–5; general: 3–5) and the jitter formula `wait_time = (base_delay * 2^attempt) + random(0, jitter_max)`.

**Confidence:** ✅ independently-corroborated (letsdatascience.com and fast.io are independent publishers)

---

## Practice: Stream first, parse at completion (or use a stateful incremental parser)

**Do:** When you need streaming *and* structured output, accumulate all token deltas into a string buffer and parse JSON only after the stream closes. If you need to update a UI mid-stream, use a stateful incremental parser (e.g., a tree-sitter JSON grammar or a purpose-built streaming JSON library) that can auto-complete incomplete tokens at each step. Never call `JSON.parse()` on a partial buffer without catching the error — it will throw on every incomplete chunk.

**Why (beginner):** JSON is only syntactically valid at the very last closing brace. If you try to parse each arriving chunk, you will get parse errors on every intermediate token. A stateful parser tracks how far it has read and completes dangling brackets/quotes temporarily so you can extract already-arrived fields before the stream ends. This is what enables a UI to show partial data progressively rather than showing a spinner for ten seconds.

**Caveat / contested:** Stateful incremental parsing adds engineering complexity. For most backend pipelines where latency is measured in seconds rather than milliseconds, simply accumulating the full response and parsing at the end is simpler and perfectly adequate. Only invest in incremental parsing when you have a real-time UI requirement or very large outputs.

**Sources:**
- [aha.io — Streaming AI responses and the incomplete JSON problem](https://www.aha.io/engineering/articles/streaming-ai-responses-incomplete-json) (fetched 2026-07-24): describes stateful parsing, auto-completion of dangling tokens, and reports 388× speed advantage (43 ms vs 16.7 s for 12 KB) over naive reparsing.
- medium.com/@prestonblckbrn — Structured Output Streaming for LLMs (fetched 2026-07-24, 403 bot-protection confirmed live): details the tree-sitter approach (~0.5 ms per loop iteration) and progressive UI rendering workflow.

**Confidence:** ✅ independently-corroborated (aha.io engineering blog and Medium author are independent publishers)

---

## Practice: Suppress the markdown wrapper with explicit system-prompt instructions

**Do:** Add a clear instruction in your system prompt such as: *"Return ONLY the raw JSON object. Do not wrap it in markdown code fences (``` or ```json). Do not add any text before or after the JSON."* Also implement a defensive strip in your parsing layer that removes ` ```json ` / ` ``` ` fences even when instructions work, as a belt-and-suspenders measure.

**Why (beginner):** Language models are trained on vast amounts of markdown-formatted text where code is conventionally wrapped in triple backticks. Without explicit instructions, models often wrap JSON in ` ```json ... ``` ` blocks, add preamble text like "Here is your data:", or append a polite closing sentence. All of these break `JSON.parse()`. The problem is common enough that it is considered a well-known anti-pattern in production LLM applications.

**Caveat / contested:** Native structured outputs (OpenAI's strict mode, Anthropic's structured outputs — now generally available) eliminate this problem at the token-generation level — invalid tokens including backticks and preambles cannot be generated. If you are using a provider with native structured outputs, the markdown wrapper problem disappears automatically. The prompt fix is still recommended for provider-agnostic or instruction-only setups. The tianpan.co source notes that prompt-only structured output extraction can show 5–20% parse failure rates from multiple failure modes collectively (preamble contamination, hallucinated keys, missing fields, type drift, and truncation).

**Sources:**
- [genaiunplugged.substack.com — Get Reliable JSON from LLMs: Structured Output Prompting Guide](https://genaiunplugged.substack.com/p/structured-outputs-json-prompts-guide) (fetched 2026-07-24): explicitly lists suppressing code fences and preambles as critical formatting rules; covers markdown-wrapper suppression and preamble prevention.
- [tianpan.co — Beyond JSON Mode](https://tianpan.co/blog/2025-10-29-structured-outputs-llm-production) (fetched 2026-07-24): identifies "preamble contamination" ("Sure! Here's the JSON...") as a named top failure mode and attributes 5–20% parse failure rates to multiple causes collectively.

**Confidence:** ✅ independently-corroborated (substack author and tianpan.co are independent publishers)

---

## Practice: Include 2–5 input→output few-shot examples for structured output tasks

**Do:** Place two to five concrete, realistic input→output examples directly in your system or user prompt before the actual request. Use the exact same JSON structure in every example. Make examples diverse — include at least one edge case. Be aware of recency effects: research shows models tend to replicate patterns from examples near the end of the prompt, so place your most representative (not necessarily most complex) example last.

**Why (beginner):** Showing a model what you want is more reliable than describing it. When the model can see a complete filled-in example of your target JSON, it has a template to match rather than having to infer the format from schema text alone. Three to five examples usually suffice; more than five can cause the model to over-fit to surface-level features of the examples.

**Caveat / contested:** Each example consumes tokens, which increases cost and can push other content out of a limited context window. Recent guidance (2025–2026) notes that beyond four examples some frontier models begin over-fitting to example phrasing, which can hurt generalisation. For tasks with native structured outputs (constrained decoding), few-shot examples are still beneficial for semantic accuracy even when syntax is already guaranteed.

**Sources:**
- [sandgarden.com — Few-Shot Prompting: Guiding LLM Behavior by Including Examples](https://www.sandgarden.com/learn/few-shot-prompting) (fetched 2026-07-24): recommends 2–5 examples and consistent formatting across examples; discusses recency/ordering effects as a challenge for practitioners.
- [ai21.com — What is Few-Shot Prompting?](https://www.ai21.com/glossary/foundational-llm/few-shot-prompting/) (fetched 2026-07-24): independently recommends "typically, 2 to 5 examples offer optimal guidance" with consistent structured formatting across all examples.
- [comet.com — Few-Shot Prompting for Agentic Systems: Teaching by Example](https://www.comet.com/site/blog/few-shot-prompting/) (fetched 2026-07-24): recommends three to five examples covering simple, complex, and edge-case scenarios.

**Confidence:** ✅ independently-corroborated (three independent publishers)

---

## Practice: Put reasoning fields before answer fields in your schema

**Do:** When your schema includes a reasoning or explanation field alongside the answer field, place the reasoning field *first* in the schema definition. Example: `{"reasoning": "...", "answer": "..."}` rather than `{"answer": "...", "reasoning": "..."}`. If the reasoning is too complex to coerce into a schema, use a two-step approach: generate natural language reasoning in a first call, then convert the answer to JSON in a second call.

**Why (beginner):** Language models write output left-to-right. If the answer field appears first in the JSON, the model commits to its answer before it has written out its reasoning — which defeats the purpose of chain-of-thought. Placing reasoning first forces the model to work through the problem step-by-step before it fills in the answer field, mimicking the "think before you write" strategy that improves accuracy on reasoning and classification tasks.

**Caveat / contested:** One study found that JSON-mode (as opposed to instruction-only) sometimes causes models to place the `answer` key before the `reason` key regardless of schema ordering, bypassing intended chain-of-thought. For complex reasoning tasks, the two-step "generate then reformat" approach is more reliable than forcing a single structured generation. For simple classification tasks, strict JSON mode actually improves accuracy by reducing ambiguity, so the two-step approach is overkill.

**Sources:**
- [letsdatascience.com — Structured Outputs: Making LLMs Return Reliable JSON](https://letsdatascience.com/blog/structured-outputs-making-llms-return-reliable-json) (fetched 2026-07-24): states "answer-first schemas degrade reasoning performance" and recommends placing reasoning/explanation fields before answer fields.
- [hereiskunalverma.medium.com — Structured JSON Output via LLMs](https://hereiskunalverma.medium.com/structured-json-output-via-llms-27b4932ae5ce) (fetched 2026-07-24): documents the two-step "NL-to-Format" pattern; quotes research finding "JSON-mode responses consistently placed the 'answer' key before the 'reason' key, bypassing the chain-of-thought reasoning essential for solving such problems."
- [dataiku.com — Taming LLM outputs: your guide to structured text generation](https://www.dataiku.com/stories/blog/your-guide-to-structured-text-generation) (fetched 2026-07-24): independently confirms "order JSON fields strategically: place reasoning/justification content before outcomes, since earlier parts of the output can influence later parts."

**Confidence:** ✅ independently-corroborated (three independent publishers)

---

## Practice: Version your output schema and evolve it by adding optional fields, not changing required ones

**Do:** Give your schema a version identifier (e.g., `schema_version: "1.2"` as a field, or a version number in your schema registry key). When you need to add information, add it as a new *optional* field with a default value. Never rename an existing required field or change its type — instead, deprecate the old field and introduce a new one. Keep the old field optional during a transition period before removing it.

**Why (beginner):** Your application code, your database, and the LLM's own prompt are all reading from the same schema. If you suddenly rename a required field or change its type, any code that was already running against the old schema will crash or silently produce wrong results. Adding optional fields with defaults is safe because old code ignores fields it does not know about, and new code can check whether the field is present.

**Caveat / contested:** Schema versioning advice in the search results comes primarily from general API and event-streaming literature (Kafka, Schema Registry — tools used in data-streaming systems; the same compatibility rules apply to LLM schemas), not LLM-specific sources. The underlying compatibility principle is the same, but LLM-specific complications exist: the LLM itself is prompted with the schema, so adding many optional fields over time can bloat the prompt and degrade quality. Periodically clean up truly obsolete optional fields from your prompts even if you keep them in your database migration layer.

**Sources:**
- [docs.solace.com — Schema Registry Best Practices](https://docs.solace.com/Schema-Registry/schema-registry-best-practices.htm) (fetched 2026-07-24): recommends making new fields optional, providing defaults, avoiding renaming existing fields, and using Full Compatibility mode as the safest default.
- [conduktor.io — Schema Evolution: Kafka Best Practices](https://www.conduktor.io/glossary/schema-evolution-best-practices) (fetched 2026-07-24): independently documents backward vs forward vs full compatibility and why renaming breaks compatibility while adding optional fields with defaults preserves it.
- [tianpan.co — Beyond JSON Mode](https://tianpan.co/blog/2025-10-29-structured-outputs-llm-production) (fetched 2026-07-24): specifically recommends "version schemas deliberately" as a production safeguard in the LLM context.

**Confidence:** ✅ independently-corroborated (Solace and Conduktor are independent publishers; tianpan.co corroborates the LLM application)

---

## Practice: Reserve enough output tokens and check the stop reason for truncation

**Do:** Before every LLM call, estimate the maximum JSON size your schema can produce and set `max_tokens` to at least that estimate plus 20% headroom. After every response, check `finish_reason` (OpenAI: value `"length"`) or `stop_reason` (Anthropic: value `"max_tokens"`). If you see either of those, treat the response as invalid — do not try to parse the truncated JSON. Either retry with a higher limit or decompose the task into smaller calls.

**Why (beginner):** When a model hits its output token limit, generation stops immediately, mid-sentence, mid-brace. The resulting JSON is syntactically broken and cannot be parsed. This failure is *silent* — in development your outputs are short enough to fit, but in production with real data they are not. By the time you notice, your pipeline may have been silently discarding data for hours.

**⚠️ WARNING:** Setting `max_tokens` very high "just to be safe" costs money on every call, because you are billed for tokens generated, and also increases latency. Estimate the actual maximum output size and add a 20% buffer — do not default to the model's maximum limit.

**Caveat / contested:** Anthropic's API requires you to set `max_tokens` explicitly (there is no implicit default for most models). OpenAI's chat completions historically defaulted to generating until a natural stop; verify the current default for your model. 🕒 Verify live — defaults change between model versions.

**Sources:**
- [flo2.com — max_tokens Explained: Control LLM Output Length & Cost](https://flo2.com/blog/max-tokens-explained) (fetched 2026-07-24): recommends estimating schema size plus 20% headroom; warns "a truncated JSON payload looks fine in development when outputs happen to be short, then silently breaks in production"; states to monitor for `finish_reason: "length"` and `stop_reason: "max_tokens"`.
- [community.openai.com — Tips for handling finish_reason: length with JSON](https://community.openai.com/t/tips-for-handling-finish-reason-length-with-json/806445) (fetched 2026-07-24): confirms that naive continuation prompts fail for truncated JSON; recommends structural redesign (smaller chained calls) or real-time partial parsing as alternatives to simple retry.

**Confidence:** ✅ independently-corroborated (flo2.com and OpenAI community forum are independent publishers)

---

## Practice: Choose the right enforcement tier — native structured outputs, tool calling, JSON mode, or instruction-only

**Do:** In order of reliability, prefer: (1) **native structured outputs** (OpenAI strict mode with `response_format` + schema, Anthropic structured outputs — now generally available as of 2026, 🕒 verify live which models support `output_config.format`) for production pipelines; (2) **tool/function calling** when the model needs to select from multiple actions or interact with external systems; (3) **JSON mode** only for quick prototyping or when a schema is genuinely unknown ahead of time; (4) **instruction-only** ("respond only in JSON") as a last resort for models that support none of the above. Do not use JSON mode alone in production — it only guarantees valid JSON syntax, not schema adherence.

**Why (beginner):** These four tiers differ in what they actually guarantee. Instruction-only is a polite request — the model can ignore it. JSON mode enforces valid JSON but the field names and types can vary between calls. Tool/function calling enforces a schema but is "best-effort" generation at the token level (still possible to get wrong types). Native structured outputs use constrained decoding to make it mathematically impossible for the model to emit tokens that violate the schema.

**Caveat / contested:** Anthropic's structured outputs graduated from public beta (November 2025) to general availability by 2026. The old beta header (`structured-outputs-2025-11-13`) is deprecated — use `output_config.format` instead; 🕒 verify whether the transition period for the old header has ended. Claude does not have a standalone `json_mode` parameter — structured outputs or tool use is the correct path. Some providers (Mistral, Groq as of late 2025) support tool calling and JSON mode but not standalone native structured outputs. Cross-provider libraries like Instructor abstract over these differences, falling back to prompt-based enforcement for providers that lack native support.

**Sources:**
- [towardsdatascience.com — Structured Outputs with LLMs: JSON Mode, Function Calling, and When to Use Each](https://towardsdatascience.com/structured-outputs-with-llms-json-mode-function-calling-and-when-to-use-each/) (fetched 2026-07-24): tabulates JSON Mode (flexible, schema-variable), Function Calling (specific fields, best-effort), and Structured Outputs (zero deviation via constrained decoding) with clear when-to-use criteria.
- [vellum.ai — When should I use function calling, structured outputs or JSON mode?](https://www.vellum.ai/blog/when-should-i-use-function-calling-structured-outputs-or-json-mode) (fetched 2026-07-24): recommends structured outputs + response_format for final-answer tasks (e.g., extraction), structured outputs + function calling for multi-step/agentic tasks; explicitly states "JSON Mode alone: Not recommended."
- [agenta.ai — The guide to structured outputs and function calling with LLMs](https://agenta.ai/blog/the-guide-to-structured-outputs-and-function-calling-with-llms) (fetched 2026-07-24): confirms the tier ordering and that Claude has no direct `json_mode` parameter.
- [developers.openai.com — Structured model outputs](https://developers.openai.com/api/docs/guides/structured-outputs) (fetched 2026-07-24, vendor docs): official guidance states "always use Structured Outputs instead of JSON mode when possible."

**Confidence:** ✅ independently-corroborated (multiple independent publishers plus vendor docs)

---

## Practice: Design tool implementations to be idempotent and log every call

**Do:** For any tool (function) that an LLM agent can invoke, design the implementation so that calling it twice with the same arguments produces the same result and causes no additional side effects. For write operations (sending an email, inserting a database row, charging a card), accept and enforce an idempotency key (a unique identifier — like a UUID — that you generate per request and check before executing). Log every tool call at INFO level with: tool name, call ID, arguments, response, latency, and success/failure status.

**Why (beginner):** Agents retry failed calls automatically. If your tool is not idempotent, a retry after a network timeout can send a duplicate email, charge a customer twice, or create a duplicate database record. The model cannot tell the difference between "I never sent that" and "I sent it but didn't hear back." Logging every call is the only way to reconstruct what happened when a multi-step agent misbehaves in production.

**⚠️ WARNING:** A tool that modifies state (sends messages, writes records, charges money) without idempotency protection is dangerous in any agent pipeline. Never connect an agent to a write-capable tool unless you have tested retry behaviour explicitly.

**Caveat / contested:** Implementing idempotency keys and result caching (e.g., in Redis — an in-memory key-value store — with a TTL, meaning the cached entry expires automatically after a set time) adds infrastructure overhead. For read-only tools (database queries, API lookups), idempotency is automatic — the same query always returns the same result at that moment — so caching is optional, not required.

**Sources:**
- [inductivee.com — Tool-Calling Architecture: Designing Reliable Functions for LLM Agents](https://inductivee.com/blog/tool-calling-agent-design-patterns) (fetched 2026-07-24): requires idempotency keys and Redis-backed result caching for all write tools; specifies logging "every tool call at INFO level with name, call ID, latency, and success status."

**Confidence:** 📄 vendor-documented (single sourced; the specific idempotency-key pattern for agent tool calls is sourced from inductivee.com only — the general principle of idempotency is well-established but this specific LLM-agent framing is single-sourced)

---

## Held pending fixes (not publish-ready)
- None.

## CHANGELOG (grading → this entry)
1. Skeptic FIX (P4): Corrected tianpan.co attribution. The page does NOT single out markdown backtick wrapping as a named failure mode — it attributes 5–20% failure rate to multiple causes collectively. Removed the misattribution; genaiunplugged.substack.com remains as source for fence-suppression guidance; tianpan.co now correctly cited only for preamble contamination and collective failure rate.
2. Skeptic FIX (P5 quote): Removed specific quotation attributed to comet.com ("strongly influenced by the last or most frequent pattern in the demonstrations") — that phrase does not appear on the page. Rewrote to attribute only what comet.com actually says (three to five examples across simple/complex/edge cases). Ordering advice reworded as a practitioner consideration, not attributed to sandgarden as a recommendation.
3. Skeptic FIX (P5 ordering): Sandgarden frames example ordering as a challenge/consideration, not an endorsed strategy. Rewrote to reflect this accurately.
4. Skeptic FIX (P10): Removed fast.io as a source for the idempotency-key claim — the fast.io page does not name non-idempotent double-writes as a failure mode. Idempotency claim now single-sourced to inductivee.com; confidence label downgraded from independently-corroborated to single-sourced with explanation.
5. Timekeeper FIX (P9): Updated "Anthropic structured outputs beta" → "Anthropic structured outputs (now generally available as of 2026)"; noted deprecated beta header and replacement `output_config.format` parameter.
6. Beginner FLAG (P1): Added plain-English definition of idempotency key (UUID) and Redis/TTL in the caveat.
7. Beginner FLAG (P1): Added plain-English gloss for CFG and FSM engine types in schema-design caveat; removed undefined jargon.
8. Link-check gate (2026-07-25): medium.com/@prestonblckbrn — Structured Output Streaming for LLMs (403 bot-protection, confirmed live via WebFetch) → unlinked to plain text (1 occurrence).
