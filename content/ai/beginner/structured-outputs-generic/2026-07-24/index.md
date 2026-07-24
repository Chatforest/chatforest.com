---
title: "Structured Outputs and Tool Use with AI APIs — Best Practices (Beginner Guide as of 24 Jul 2026)"
date: 2026-07-24
snapshot_date: 2026-07-24
topic: structured-outputs-generic
track: beginner
audience: "people new to AI"
description: "Ten plain-English best practices for getting reliable, machine-readable structured output from AI APIs — covering schema design, validation, streaming, prompt patterns, token budgets, and safe tool execution."
content_type: "Best Practice"
categories: ["Structured Outputs", "Tool Use", "LLM APIs"]
tags: ["json-schema", "structured-outputs", "tool-calling", "function-calling", "validation", "retry", "streaming", "few-shot", "chain-of-thought", "idempotency"]
last_refreshed: 2026-07-24
graded_by: "RingS panel (Skeptic/Beginner/Timekeeper) + sensei, 2026-07-24"
grading_result: "0 fabrications; 7 corrections applied; 0 gaps filed as issues; beginner re-level applied."
---

<!-- This file lands at content/ai/beginner/structured-outputs-generic/2026-07-24/index.md and is an IMMUTABLE
     dated snapshot. Once published it is never edited — a refresh is a NEW <snapshot-date> dir.
     "Latest" is computed by Grove's template from snapshot_date; do not add a "latest" flag. -->

# Structured Outputs and Tool Use with AI APIs (Beginner Guide as of 24 Jul 2026)

> **Grading note.** A dated snapshot — accurate as of **24 Jul 2026**, frozen here and kept as
> a permanent archive entry. Research-drafted by a pupil, graded by the 3-lens panel + sensei.
> Corrections applied inline; unverifiable gaps marked ⚠ PENDING (#issue) — never guessed.

## What is this and why should you care?

When you ask an AI chatbot a question, it normally answers in flowing prose — paragraphs of human-readable text. That is great for reading, but if you want a computer program to *use* the answer (store it in a database, feed it to another step, fill in a form), prose is hard to process reliably.

**Structured output** means asking the AI to reply in a fixed, predictable format — most often JSON (JavaScript Object Notation). JSON looks like this:

```json
{"name": "Alice", "score": 92, "passed": true}
```

Every field has a name and a value, and a computer can read that instantly without guessing.

**Tool use** (also called "function calling") means giving the AI the ability to call functions in your code — for example, "look up this customer in the database" or "send this email." The AI decides when to use a tool and what arguments to pass.

These two features together let you build real applications on top of AI: chatbots that actually update records, pipelines that extract structured data from documents, and agents that take multi-step actions. The practices below help you do that reliably and safely.

## How to read the labels
- ✅ **independently-corroborated** — 2+ independent publishers
- 📄 **vendor-documented** — official docs only (authoritative, single source)
- ⚠️ **WARNING** — a default that can cost money, break the machine, or remove a safety net
- 🕒 **verify live** — fast-moving (versions/prices/quotas); check the current value

---

## Practice: Keep JSON schemas flat, simple, and well-described

**What is a schema?** A schema is a description of the exact shape you want the AI's JSON to take. It lists every field, what type of value it holds (text, number, true/false), and which fields are required. You send this schema to the API alongside your request, and the AI tries to match it.

**Do:**
- Keep nesting shallow — no more than three levels deep. Deeply nested means something like `order.customer.address.street.line1`; try to avoid going that deep.
- Keep schemas small — under 20 fields where possible.
- Use `enum` to give the model a short list of allowed values for a field (for example, `"status": ["pending", "approved", "rejected"]`) instead of letting it write anything it likes.
- Mark every field as either `required` (must always be present) or `optional` (may be absent). Never leave it ambiguous.
- Write a plain-English `description` on every field. These descriptions go directly to the AI and act like extra instructions.
- Set `additionalProperties: false` to stop the AI from inventing fields you did not ask for.

**Why (beginner):** AI models generate output one word (token) at a time from left to right. By the time the model reaches a deeply nested field, it may have "forgotten" a constraint it read earlier. Keeping schemas small and flat reduces the chance of the model straying. Enum fields help even more — instead of guessing, the model just picks from your short list. The descriptions you write are not just notes for humans; the API sends them to the model as part of the prompt, so a good description like "customer's age in whole years, must be positive" directly improves accuracy.

**What goes wrong without this:** The model invents fields, nests data in unexpected places, or returns a value like `"active"` when you expected only `"yes"` or `"no"`. Your code then crashes trying to read a field that does not exist.

**Caveat / contested:** Constrained decoding (strict mode, native structured outputs) can enforce correct syntax regardless of schema complexity, but the *meaning* of values still degrades with very large schemas. For very complex recursive schemas (schemas that refer back to themselves, like a tree structure), you may need a specialized library — most beginners will not hit this. 🕒 Verify live — engine support details change frequently.

**Sources:**
- [letsdatascience.com — Structured Outputs: Making LLMs Return Reliable JSON](https://letsdatascience.com/blog/structured-outputs-making-llms-return-reliable-json) (fetched 2026-07-24): recommends schemas under 20 properties, nesting under 3 levels, and comprehensive field descriptions.
- [tianpan.co — Beyond JSON Mode: Getting Reliable Structured Outputs from LLMs in Production](https://tianpan.co/blog/2025-10-29-structured-outputs-llm-production) (fetched 2026-07-24): lists keeping schemas flat, using enums aggressively, and setting `additionalProperties: false` as core schema design principles.
- [techsy.io — Reliable JSON from Any LLM: Pydantic + Zod](https://techsy.io/en/blog/llm-structured-outputs-guide) (fetched 2026-07-24): confirms field descriptions become part of the JSON Schema sent to the model and directly influence output quality.

**Confidence:** ✅ independently-corroborated (three independent publishers)

---

## Practice: Validate LLM output against the schema and retry with error feedback

**What does "validate" mean?** After the AI responds, your code checks whether the response actually matches the schema — correct field names, correct types, required fields present. A library does this for you. In Python the common choice is **Pydantic**; in TypeScript it is **Zod**.

**⚠️ WARNING:** An uncapped retry loop can spend unbounded money. Always set a hard `max_retries` (2–3 is sufficient for most use-cases) and a total wall-clock timeout. Without this limit, a bug in your schema or prompt could cause your program to call the API hundreds of times and run up a large bill.

**Do:**
- After every AI call, parse and validate the response against your schema using Pydantic (Python) or Zod (TypeScript).
- If validation fails, send the validation error message back to the model in the next turn — do not just call the API again with the exact same prompt.
- Cap retries at 2–3 for complex schemas.
- Wait between retries using exponential backoff with jitter: `wait_time = (base_delay * 2^attempt) + random(0, jitter_max)` with `base_delay = 1` second and `jitter_max = 0.5` seconds as a starting point. This prevents all your retries from hitting the API at the same moment.

**Why (beginner):** Even when the API is told to return structured output, the AI can produce values that are syntactically valid JSON but semantically wrong — for example, `rating: 1` combined with `sentiment: "positive"`. Validation catches these mismatches before they reach your database. Feeding the error message back to the model gives it a specific description of what went wrong, which lets it self-correct on the next attempt. Simply retrying with the same prompt almost always fails again.

**What goes wrong without this:** Bad data enters your database silently. You only discover the problem weeks later when a query returns nonsensical results.

**Caveat / contested:** Libraries such as Instructor (Python) and native provider SDKs handle retry-with-feedback automatically; hand-rolling this logic is error-prone. Rate-limit retries (HTTP 429 — meaning "you sent too many requests") warrant more retries (5–7) and longer backoff than schema validation failures (2–3).

**Sources:**
- [letsdatascience.com — Structured Outputs: Making LLMs Return Reliable JSON](https://letsdatascience.com/blog/structured-outputs-making-llms-return-reliable-json) (fetched 2026-07-24): explicitly recommends retry with validation feedback and a `max_retries` of 2–3.
- [fast.io — AI Agent Error Handling: Best Practices & Patterns](https://fast.io/resources/ai-agent-error-handling/) (fetched 2026-07-24): states "if validation fails, the error message is fed back to the LLM as a new prompt" and describes exponential backoff with jitter.
- [fast.io — AI Agent Retry Patterns: Exponential Backoff Guide](https://fast.io/resources/ai-agent-retry-patterns/) (fetched 2026-07-24): provides per-error-type retry caps (rate limits: 5–7; server errors: 3–5; general: 3–5) and the jitter formula `wait_time = (base_delay * 2^attempt) + random(0, jitter_max)`.

**Confidence:** ✅ independently-corroborated (letsdatascience.com and fast.io are independent publishers)

---

## Practice: Stream first, parse at completion (or use a stateful incremental parser)

**What is streaming?** Instead of waiting for the entire response before showing anything, streaming sends you the AI's tokens one at a time as they are generated — like watching someone type in real time.

**Do:**
- When you need streaming AND structured output, collect all the arriving pieces (called "token deltas") into a single string buffer and parse the JSON only after the stream has fully closed.
- If you need to update a user interface while the stream is still arriving, use a stateful incremental parser — a specialized library that can handle incomplete JSON and fill in dangling brackets temporarily at each step.
- Never call `JSON.parse()` on a partial buffer without catching the error — it will throw an exception on every incomplete chunk.

**Why (beginner):** JSON is only valid at the very last closing brace `}`. If you try to parse each arriving piece, you will get errors on every intermediate token because the JSON is incomplete. A stateful parser (a library that tracks where it is in the JSON structure) can temporarily "complete" an unfinished object so you can read already-arrived fields while waiting for the rest. This is what allows a UI to progressively display data rather than showing a loading spinner for the entire duration.

**What goes wrong without this:** Your program crashes on every chunk, or you show the user a broken loading screen instead of smooth progressive content.

**Caveat / contested:** Stateful incremental parsing adds complexity. For most back-end pipelines where you are not building a real-time UI, simply waiting for the full response and parsing at the end is simpler and completely adequate. Only add incremental parsing when you have a real-time display requirement or very large outputs.

**Sources:**
- [aha.io — Streaming AI responses and the incomplete JSON problem](https://www.aha.io/engineering/articles/streaming-ai-responses-incomplete-json) (fetched 2026-07-24): describes stateful parsing, auto-completion of dangling tokens, and reports 388x speed advantage (43 ms vs 16.7 s for 12 KB) over naive reparsing.
- medium.com/@prestonblckbrn — Structured Output Streaming for LLMs (fetched 2026-07-24, 403 bot-protection confirmed live): details the tree-sitter approach (~0.5 ms per loop iteration) and progressive UI rendering workflow.

**Confidence:** ✅ independently-corroborated (aha.io engineering blog and Medium author are independent publishers)

---

## Practice: Suppress the markdown wrapper with explicit system-prompt instructions

**What is a system prompt?** The system prompt is a hidden set of instructions you send to the AI before the user's message. It sets the AI's behavior for the whole conversation. You write it; the user does not see it.

**Do:**
- Add a clear instruction in your system prompt such as: *"Return ONLY the raw JSON object. Do not wrap it in markdown code fences (``` or ```json). Do not add any text before or after the JSON."*
- Also add a defensive strip in your parsing code that removes ` ```json ` / ` ``` ` fences even when the instruction works — a safety net in case the model occasionally ignores it.

**Why (beginner):** AI models are trained on enormous amounts of text from the internet, where code is conventionally wrapped in triple backticks like this:

````
```json
{"name": "Alice"}
```
````

Without explicit instructions, models often wrap your JSON in those fences and add sentences like "Here is your data:" before it or "Let me know if you need anything else." after it. All of that extra text causes `JSON.parse()` to fail — it expects JSON to start with `{` or `[`, not words. This failure mode is common enough that it is considered a well-known problem in production AI applications.

**What goes wrong without this:** Your JSON parser throws an error on every response and your application breaks entirely, or silently discards data.

**Caveat / contested:** Native structured outputs (OpenAI's strict mode, Anthropic's structured outputs) eliminate this problem at the generation level — the model literally cannot emit backtick tokens when native structured outputs are active. If your API provider supports native structured outputs, the markdown wrapper problem goes away automatically. The prompt instruction is still recommended if you are using a provider without native structured output support, or if you are writing code that needs to work across multiple providers. Note: prompt-only approaches can show 5–20% parse failure rates from multiple failure modes collectively (preamble contamination, hallucinated keys, missing fields, type drift, and truncation).

**Sources:**
- [genaiunplugged.substack.com — Get Reliable JSON from LLMs: Structured Output Prompting Guide](https://genaiunplugged.substack.com/p/structured-outputs-json-prompts-guide) (fetched 2026-07-24): explicitly lists suppressing code fences and preambles as critical formatting rules; covers markdown-wrapper suppression and preamble prevention.
- [tianpan.co — Beyond JSON Mode](https://tianpan.co/blog/2025-10-29-structured-outputs-llm-production) (fetched 2026-07-24): identifies "preamble contamination" ("Sure! Here's the JSON...") as a named top failure mode and attributes 5–20% parse failure rates to multiple causes collectively.

**Confidence:** ✅ independently-corroborated (substack author and tianpan.co are independent publishers)

---

## Practice: Include 2–5 input-to-output few-shot examples for structured output tasks

**What is a few-shot example?** A "few-shot example" is a complete sample you include directly in your prompt to show the model what you want. You provide an example input and the exact JSON output you expect for that input, before presenting the real request. "Few-shot" just means "a small number of examples."

**Do:**
- Place two to five concrete, realistic input-to-output examples directly in your system or user prompt, before the actual request.
- Use the exact same JSON structure in every example.
- Make examples diverse — include at least one edge case (an unusual or tricky input).
- Put your most representative example last, because research shows models tend to replicate patterns from examples near the end of the prompt.

**Why (beginner):** Showing the model what you want is more reliable than only describing it. When the model can see a complete, filled-in example of your target JSON, it has a template to match rather than having to figure out the format from schema text alone. Three to five examples usually suffice. More than five can cause the model to copy surface-level features of the examples instead of understanding the underlying pattern.

**What goes wrong without this:** The model returns JSON that is technically valid but uses different field names, different value formats, or different nesting than you expected — even when you described the schema in words.

**Caveat / contested:** Each example consumes tokens, which increases cost and can push other content out of a limited context window. Recent guidance (2025–2026) notes that beyond four examples some frontier models begin over-fitting to example phrasing, which can hurt generalisation. For tasks with native structured outputs (constrained decoding), few-shot examples are still beneficial for semantic accuracy even when syntax is already guaranteed.

**Sources:**
- [sandgarden.com — Few-Shot Prompting: Guiding LLM Behavior by Including Examples](https://www.sandgarden.com/learn/few-shot-prompting) (fetched 2026-07-24): recommends 2–5 examples and consistent formatting across examples; discusses recency/ordering effects as a challenge for practitioners.
- [ai21.com — What is Few-Shot Prompting?](https://www.ai21.com/glossary/foundational-llm/few-shot-prompting/) (fetched 2026-07-24): independently recommends "typically, 2 to 5 examples offer optimal guidance" with consistent structured formatting across all examples.
- [comet.com — Few-Shot Prompting for Agentic Systems: Teaching by Example](https://www.comet.com/site/blog/few-shot-prompting/) (fetched 2026-07-24): recommends three to five examples covering simple, complex, and edge-case scenarios.

**Confidence:** ✅ independently-corroborated (three independent publishers)

---

## Practice: Put reasoning fields before answer fields in your schema

**What is chain-of-thought?** Chain-of-thought is when you ask the AI to show its reasoning steps before giving a final answer — like asking someone to "show their work." This often produces more accurate answers because the model has to think through the problem before committing to a response.

**Do:**
- When your schema includes both a reasoning field and an answer field, always place the reasoning field first.
  - Correct order: `{"reasoning": "...", "answer": "..."}`
  - Wrong order: `{"answer": "...", "reasoning": "..."}`
- If the reasoning is too complex to fit neatly into a schema field, use a two-step approach: generate natural-language reasoning in a first AI call, then convert the answer to JSON in a second AI call.

**Why (beginner):** The AI writes output from left to right, one token at a time — just like a person writing a sentence. If the `answer` field comes first in the JSON, the model commits to an answer before it has written any reasoning. That defeats the whole purpose of asking for reasoning. By putting the `reasoning` field first, you force the model to work through the problem step-by-step before it fills in the answer — which improves accuracy on reasoning and classification tasks.

**What goes wrong without this:** The model fills in the answer first, then invents reasoning that justifies the (possibly wrong) answer it already committed to, rather than using the reasoning to reach the right answer.

**Caveat / contested:** One study found that JSON mode sometimes causes models to place the `answer` key before the `reason` key regardless of schema ordering, bypassing the intended chain-of-thought. For complex reasoning tasks, the two-step "generate then reformat" approach is more reliable than forcing a single structured generation. For simple classification tasks, strict JSON mode actually improves accuracy by reducing ambiguity, so the two-step approach would be unnecessary overhead.

**Sources:**
- [letsdatascience.com — Structured Outputs: Making LLMs Return Reliable JSON](https://letsdatascience.com/blog/structured-outputs-making-llms-return-reliable-json) (fetched 2026-07-24): states "answer-first schemas degrade reasoning performance" and recommends placing reasoning/explanation fields before answer fields.
- [hereiskunalverma.medium.com — Structured JSON Output via LLMs](https://hereiskunalverma.medium.com/structured-json-output-via-llms-27b4932ae5ce) (fetched 2026-07-24): documents the two-step "NL-to-Format" pattern; quotes research finding "JSON-mode responses consistently placed the 'answer' key before the 'reason' key, bypassing the chain-of-thought reasoning essential for solving such problems."
- [dataiku.com — Taming LLM outputs: your guide to structured text generation](https://www.dataiku.com/stories/blog/your-guide-to-structured-text-generation) (fetched 2026-07-24): independently confirms "order JSON fields strategically: place reasoning/justification content before outcomes, since earlier parts of the output can influence later parts."

**Confidence:** ✅ independently-corroborated (three independent publishers)

---

## Practice: Version your output schema and evolve it by adding optional fields, not changing required ones

**What is schema versioning?** Schema versioning means giving your schema a version number (like `"1.2"`) and following rules about what you are allowed to change as your application grows.

**Do:**
- Add a version identifier to your schema, for example a field `schema_version: "1.2"` or a version number in your schema registry key.
- When you need to add new information, add it as a new *optional* field with a default value. Never make it required immediately.
- Never rename an existing required field or change its type. Instead, mark the old field as deprecated (optional) and introduce a new field alongside it.
- Keep the old field optional during a transition period before removing it entirely.

**Why (beginner):** Your application code, your database, and the AI's prompt are all reading from the same schema. If you suddenly rename a required field or change its type, any code written against the old schema will crash or silently produce wrong results. Adding optional fields with defaults is safe because old code simply ignores fields it does not know about, while new code can check whether the field is present.

**What goes wrong without this:** You rename a field to fix a typo, deploy the change, and discover that everything that was reading the old field name now returns null or crashes. This is a common source of production outages.

**Caveat / contested:** The schema versioning advice here comes from general API and data-streaming literature — the same compatibility rules apply to AI schemas. One AI-specific complication: adding many optional fields over time can bloat the prompt and degrade the AI's output quality. Periodically clean up truly obsolete optional fields from your prompts even if you keep them in your database migration layer.

**Sources:**
- [docs.solace.com — Schema Registry Best Practices](https://docs.solace.com/Schema-Registry/schema-registry-best-practices.htm) (fetched 2026-07-24): recommends making new fields optional, providing defaults, avoiding renaming existing fields, and using Full Compatibility mode as the safest default.
- [conduktor.io — Schema Evolution: Kafka Best Practices](https://www.conduktor.io/glossary/schema-evolution-best-practices) (fetched 2026-07-24): independently documents backward vs forward vs full compatibility and why renaming breaks compatibility while adding optional fields with defaults preserves it.
- [tianpan.co — Beyond JSON Mode](https://tianpan.co/blog/2025-10-29-structured-outputs-llm-production) (fetched 2026-07-24): specifically recommends "version schemas deliberately" as a production safeguard in the LLM context.

**Confidence:** ✅ independently-corroborated (Solace and Conduktor are independent publishers; tianpan.co corroborates the LLM application)

---

## Practice: Reserve enough output tokens and check the stop reason for truncation

**What are output tokens?** The AI generates output one "token" at a time (roughly 3–4 characters each). The API has a `max_tokens` parameter that sets a hard limit on how many tokens the AI can generate in a single response. When the AI hits that limit, it stops immediately — even mid-sentence, mid-brace.

**⚠️ WARNING:** Setting `max_tokens` very high "just to be safe" costs money on every call, because you are billed for tokens generated, and also increases latency. Estimate the actual maximum output size your schema can produce and add a 20% buffer — do not default to the model's absolute maximum limit.

**Do:**
- Before every AI call, estimate the maximum JSON size your schema can produce and set `max_tokens` to at least that estimate plus 20% headroom.
- After every response, check the stop reason the API returns:
  - OpenAI: check `finish_reason` — if the value is `"length"`, the output was cut off.
  - Anthropic: check `stop_reason` — if the value is `"max_tokens"`, the output was cut off.
- If you see either of those values, treat the response as invalid. Do not try to parse the truncated JSON. Either retry with a higher token limit, or break the task into smaller calls.

**Why (beginner):** When generation stops mid-brace, the resulting JSON is syntactically broken and `JSON.parse()` will throw an error. Worse, this failure is often invisible during development — your test inputs are short, so the output always fits. In production with real data, the outputs are longer, the truncation happens, and your pipeline silently discards data. You may not notice for hours.

**What goes wrong without this:** The AI generates half a JSON object, your parser crashes, and — if you do not check the stop reason — your code might swallow the error silently and move on, losing data.

**Caveat / contested:** Anthropic's API requires you to set `max_tokens` explicitly (there is no implicit default for most models). OpenAI's chat completions historically defaulted to generating until a natural stop; verify the current default for your model. 🕒 Verify live — defaults change between model versions.

**Sources:**
- [flo2.com — max_tokens Explained: Control LLM Output Length & Cost](https://flo2.com/blog/max-tokens-explained) (fetched 2026-07-24): recommends estimating schema size plus 20% headroom; warns "a truncated JSON payload looks fine in development when outputs happen to be short, then silently breaks in production"; states to monitor for `finish_reason: "length"` and `stop_reason: "max_tokens"`.
- [community.openai.com — Tips for handling finish_reason: length with JSON](https://community.openai.com/t/tips-for-handling-finish-reason-length-with-json/806445) (fetched 2026-07-24): confirms that naive continuation prompts fail for truncated JSON; recommends structural redesign (smaller chained calls) or real-time partial parsing as alternatives to simple retry.

**Confidence:** ✅ independently-corroborated (flo2.com and OpenAI community forum are independent publishers)

---

## Practice: Choose the right enforcement tier — native structured outputs, tool calling, JSON mode, or instruction-only

**The four options, from most reliable to least reliable:**

There are four ways to ask an AI API to return structured output. They differ in what they actually guarantee. Start with the most reliable option your provider supports.

1. **Native structured outputs** (most reliable) — The API enforces your schema at the token level, making it mathematically impossible for the model to emit tokens that violate the schema. Use this for all production pipelines. In practice: OpenAI strict mode with `response_format` + schema; Anthropic structured outputs using `output_config.format` (generally available as of 2026). 🕒 Verify live which models support this.

2. **Tool/function calling** (reliable, and needed for actions) — Use this when the AI needs to choose from multiple actions or interact with external systems. The API enforces a schema for the tool's arguments.

3. **JSON mode** (prototype only) — Guarantees that the response is valid JSON, but field names and types can vary between calls. Do not use JSON mode alone in production.

4. **Instruction-only** (last resort) — Adding "respond only in JSON" to your prompt. The model can ignore this. Only use this for providers that support none of the above.

**Do:** Default to native structured outputs for final-answer tasks (extracting data, filling forms). Use tool/function calling for multi-step or agentic tasks where the AI picks which action to take. Never rely on JSON mode alone in production.

**Why (beginner):** Each step down the list reduces the guarantee. Instruction-only is a polite request the model can ignore. JSON mode ensures the braces and quotes are balanced, but `{"name": 42}` is valid JSON even if `name` should be a string. Native structured outputs make a broken schema response impossible, the same way a typed programming language prevents you from assigning a number where a string is required.

**What goes wrong without this:** You use JSON mode in production thinking it is enough, and your application crashes on responses that are valid JSON but have wrong field names or missing required fields.

**Caveat / contested:** Anthropic's structured outputs graduated from public beta (November 2025) to general availability by 2026. The old beta header (`structured-outputs-2025-11-13`) is deprecated — use `output_config.format` instead; 🕒 verify whether the transition period for the old header has ended. Claude does not have a standalone `json_mode` parameter — structured outputs or tool use is the correct path. Some providers (Mistral, Groq as of late 2025) support tool calling and JSON mode but not standalone native structured outputs. Cross-provider libraries like Instructor abstract over these differences, falling back to prompt-based enforcement for providers that lack native support.

**Sources:**
- [towardsdatascience.com — Structured Outputs with LLMs: JSON Mode, Function Calling, and When to Use Each](https://towardsdatascience.com/structured-outputs-with-llms-json-mode-function-calling-and-when-to-use-each/) (fetched 2026-07-24): tabulates JSON Mode (flexible, schema-variable), Function Calling (specific fields, best-effort), and Structured Outputs (zero deviation via constrained decoding) with clear when-to-use criteria.
- [vellum.ai — When should I use function calling, structured outputs or JSON mode?](https://www.vellum.ai/blog/when-should-i-use-function-calling-structured-outputs-or-json-mode) (fetched 2026-07-24): recommends structured outputs + response_format for final-answer tasks (e.g., extraction), structured outputs + function calling for multi-step/agentic tasks; explicitly states "JSON Mode alone: Not recommended."
- [agenta.ai — The guide to structured outputs and function calling with LLMs](https://agenta.ai/blog/the-guide-to-structured-outputs-and-function-calling-with-llms) (fetched 2026-07-24): confirms the tier ordering and that Claude has no direct `json_mode` parameter.
- [developers.openai.com — Structured model outputs](https://developers.openai.com/api/docs/guides/structured-outputs) (fetched 2026-07-24, vendor docs): official guidance states "always use Structured Outputs instead of JSON mode when possible."

**Confidence:** ✅ independently-corroborated (multiple independent publishers plus vendor docs)

---

## Practice: Design tool implementations to be idempotent and log every call

**What does "idempotent" mean?** Idempotent (ih-dem-POH-tent) means "calling it twice with the same input has the same effect as calling it once." A read-only database query is naturally idempotent — reading the same row twice does nothing harmful. Sending an email is NOT naturally idempotent — doing it twice sends two emails.

**⚠️ WARNING:** A tool that modifies state (sends messages, writes records, charges money) without idempotency protection is dangerous in any agent pipeline. Never connect an agent to a write-capable tool unless you have tested retry behaviour explicitly.

**Do:**
- Design every tool the AI can call so that running it twice with the same arguments produces the same result and no extra side effects.
- For write operations (sending an email, inserting a database row, charging a payment card), accept and enforce an **idempotency key** — a unique identifier, like a UUID (a randomly generated ID such as `f47ac10b-58cc-4372-a567-0e02b2c3d479`), that you generate once per request. Before executing the write, check whether you have already processed that key. If yes, skip the action and return the earlier result.
- Log every tool call at INFO level with: tool name, call ID, arguments, response, latency, and success/failure status.

**Why (beginner):** AI agents automatically retry calls that appear to have failed — for example, after a network timeout. The agent cannot tell the difference between "the action never happened" and "the action happened but I did not receive confirmation." Without idempotency protection, a retry after a timeout can send a duplicate email, charge a customer twice, or create a duplicate database record. Logging every call is the only way to reconstruct what happened when a multi-step agent does something unexpected in production.

**What goes wrong without this:** A customer gets charged twice for one order. A user receives the same email three times. A database accumulates duplicate records. These errors are difficult to detect and painful to reverse.

**Caveat / contested:** Implementing idempotency keys and result caching (for example, in Redis — an in-memory key-value store — with a TTL, meaning the cached entry expires automatically after a set time) adds infrastructure overhead. For read-only tools (database queries, API lookups), idempotency is automatic — the same query always returns the same result at that moment — so caching is optional, not required.

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
8. Beginner re-level by rings-beginner-author, 2026-07-24.
9. Link-check gate (2026-07-25): medium.com/@prestonblckbrn — Structured Output Streaming for LLMs (403 bot-protection, confirmed live via WebFetch) → unlinked to plain text (1 occurrence).
