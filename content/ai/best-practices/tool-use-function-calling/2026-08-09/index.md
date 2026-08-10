---
title: "Tool Use & Function-Calling Design Patterns for AI Agents — Best Practices (as of 09 Aug 2026)"
date: 2026-08-09
snapshot_date: 2026-08-09
topic: tool-use-function-calling
track: best-practices
audience: "technically comfortable readers"
description: "How to design, call, and secure tools/functions across Anthropic Claude, OpenAI, and vendor-neutral (MCP/framework) patterns: schema design, tool_choice/strict modes, parallel calls, error handling, and the injection/sandboxing risks that come with letting a model execute real actions."
content_type: "Best Practice"
categories: ["Claude", "OpenAI", "MCP", "AI Agents"]
tags: ["tool-use", "function-calling", "claude", "openai", "mcp", "messages-api", "responses-api", "agents", "prompt-injection", "sandboxing"]
last_refreshed: 2026-08-09
graded_by: "RingS panel (Skeptic/Beginner/Timekeeper) + sensei, 2026-08-09"
grading_result: "0 fabrications after correction; 3 Skeptic KILLs fixed (1 dead link, 2 fabricated attributions to the same blog), 1 cross-draft contradiction reconciled (Anthropic vs. generic drafts gave opposing tool-consolidation advice — kept as a disclosed live disagreement), 1 Beginner KILL fixed (OpenAI computer-use/code-interpreter praised with zero safety warning), ~25 further FIX/FLAG corrections applied"
---

<!-- This file lands at content/ai/best-practices/tool-use-function-calling/2026-08-09/index.md
     and is an IMMUTABLE dated snapshot. Once published it is never edited — a refresh is a
     NEW <snapshot-date> dir. "Latest" is computed by Grove's template from snapshot_date;
     do not add a "latest" flag.
     Source tiers: independently-corroborated = 2+ DIFFERENT publishers; vendor-documented =
     official vendor docs only (authoritative, single source). -->

# Tool Use & Function-Calling Design Patterns for AI Agents (as of 09 Aug 2026)

> **Grading note.** A dated snapshot — accurate as of **09 Aug 2026**, frozen here and kept as
> a permanent archive entry. Research-drafted by three pupils (Anthropic Claude, OpenAI,
> cross-provider/generic) on 09 Aug 2026, adversarially re-fetched by the Skeptic panelist the
> same day (45 URLs re-fetched, 1 dead link found and fixed, 2 fabricated attributions to the
> same third-party blog removed), reviewed for novice-safety by the Beginner panelist (1 KILL:
> a missing safety warning on code-execution/computer-use tools), and checked for staleness by
> the Timekeeper panelist (2 completeness gaps closed, 1 unverified model-specific claim
> softened). Items still unverifiable are marked **⚠ PENDING** — this corpus does not publish
> unverified content. **0 fabrications after correction.**

## How to read the labels
- ✅ **independently-corroborated** — confirmed by 2+ independent publishers
- 📄 **vendor-documented** — official docs only (authoritative, single source)
- ⚠️ **WARNING** — a default that can cost money, break the machine, or remove a safety net
- 🕒 **verify live** — fast-moving (versions/prices/quotas); check the current value yourself

**Two terms used throughout this entry:** a **JSON Schema** is a description of what shape of
data is valid for a value — which fields exist, their types, and which are required — and it's
how you tell a model exactly what a tool's inputs must look like. **MCP (Model Context
Protocol)** is an open, JSON-RPC-based standard (`tools/list` / `tools/call`) for exposing tools
to a model in a way that works across vendors, instead of hand-writing a separate integration
per API. Both come up repeatedly below.

---

## Part 1 — Anthropic Claude (Messages API)

This part covers Claude's Messages API tool use (`tools`, `tool_choice`, `tool_use`/`tool_result`
content blocks) as documented at [platform.claude.com/docs](https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview)
on 09 Aug 2026. Model names, token counts, and beta feature names below are 🕒 **verify live** —
this space (Claude Opus 5 / Sonnet 5 generation, adaptive thinking) moves fast.

### Practice: Write extremely detailed, specific tool descriptions
**Do:** For every tool, write a `description` of at least 3–4 sentences covering what it does,
when it should (and shouldn't) be used, what each parameter means, and any caveats or limits.
Anthropic's own comparison: a one-line description like "Gets the stock price for a ticker" is
explicitly called out as a "poor" example next to a ~5-sentence version that names the exchange,
the currency, the trigger conditions, and what the tool does *not* return.
**Why (beginner):** The model has nothing but the name, description, and JSON Schema to decide
whether and how to call your tool — it can't see your code. A vague description is the single
biggest cause of "Claude picked the wrong tool" or "Claude passed garbage arguments."
**Caveat / contested:** This is Anthropic's own advice for its own product, so it's
vendor-documented rather than independently verified.
**Sources:** [platform.claude.com/docs — Define tools](https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools) (fetched 9 Aug 2026) · [anthropic.com/engineering — Writing effective tools for agents](https://www.anthropic.com/engineering/writing-tools-for-agents) (published 11 Sep 2025)
**Confidence:** vendor-documented

### Practice: Consolidate related operations into fewer, namespaced tools
**Do:** Anthropic's own guidance: prefer one tool with an `action` parameter (or a small number
of purpose-built tools) over a separate tool per CRUD-style endpoint — "rather than creating a
separate tool for every action (`create_pr`, `review_pr`, `merge_pr`), group them into a single
tool with an `action` parameter." When tools span multiple services, prefix names by
service/resource (`github_list_prs`, `slack_send_message`).
**Why (beginner):** Every tool you add is something Claude has to correctly distinguish from
every other tool. Fewer, clearer tools reduce the chance Claude calls the wrong one.
**Caveat / contested:** This is Anthropic's specific, stated position — but it is not universal
industry consensus. A machine-learning-focused independent source (cited in Part 3 below) argues
the opposite: that a multipurpose tool with an internal `action`/`mode` parameter forces the
model to "first figure out which mode to invoke" and that one-tool-per-operation is safer. Both
positions are held by credible sources; treat "consolidate vs. split" as a real, unresolved
design tradeoff to test against your own model and tools rather than a settled rule. See Part 3,
"Give each tool a single, unambiguous job," for the opposing view.
**Sources:** [platform.claude.com/docs — Define tools](https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools) (fetched 9 Aug 2026) · [anthropic.com/engineering — Writing effective tools for agents](https://www.anthropic.com/engineering/writing-tools-for-agents) (published 11 Sep 2025)
**Confidence:** vendor-documented

### Practice: Shape tool *responses* for signal, not volume
**Do:** Return stable, semantic identifiers (slugs/UUIDs with readable names) instead of opaque
internal references, and include only the fields Claude needs for its next step. Anthropic's
engineering post adds concrete tactics: cap response size (their own Claude Code default is
~25,000 tokens), support pagination/filtering/truncation, and expose a `response_format`
("concise" vs "detailed") switch where useful.
**Why (beginner):** Bloated tool output eats your context window (the total token budget for one
model call) and makes it harder for Claude to find the one field it actually needs.
**Caveat / contested:** The "~25,000 tokens" figure is Claude Code's own internal default, not a
universal limit for all tools — treat it as an example, not a rule. 🕒 verify live.
**Sources:** [platform.claude.com/docs — Define tools](https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools) (fetched 9 Aug 2026) · [anthropic.com/engineering — Writing effective tools for agents](https://www.anthropic.com/engineering/writing-tools-for-agents) (published 11 Sep 2025)
**Confidence:** vendor-documented

### Practice: Choose `tool_choice` deliberately — know what `auto`/`any`/`tool`/`none` actually do
**Do:** `auto` (default) lets Claude decide whether to call a tool. `any` forces some tool call
but not which one. `tool` forces one specific tool. `none` forbids tool calls. `any` and `tool`
**prefill** the assistant turn — they insert a forced start to the response — so Claude will not
emit introductory natural-language text before the `tool_use` block even if you ask it to; if you
want both a spoken explanation and a forced-feeling call, use `auto` plus an explicit instruction
in the user message instead.
**Why (beginner):** Picking the wrong mode is a common source of "why won't Claude explain
itself" or "why does Claude sometimes just answer in text when I needed a tool call" bugs.
**Caveat / contested:** Forced tool use (`any`/`tool`) is **not supported** with manual extended
thinking (`thinking: {type: "enabled"}`) — it returns a 400 error (the API rejected the request
as malformed). Adaptive thinking does support forced tool use. Model-by-model support for forced
tool use alongside thinking is a genuinely fast-moving compatibility matrix — 🕒 verify live
against the current Tool Reference / model-compatibility table rather than assuming any specific
model's behavior from this snapshot.
**Sources:** [platform.claude.com/docs — Define tools](https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools) (fetched 9 Aug 2026) · [platform.claude.com/docs — Thinking](https://platform.claude.com/docs/en/build-with-claude/thinking) (fetched 9 Aug 2026)
**Confidence:** vendor-documented

### Practice: Use `strict: true` to guarantee schema-valid tool calls
**Do:** Set `"strict": true` on a tool definition (with `"additionalProperties": false` in the
schema) to constrain Claude's token sampling so its `input` always matches your JSON Schema
exactly — no more `"2"` where you wanted the integer `2`, no missing required fields. Combine
with `tool_choice: {"type": "any"}` to guarantee both that some tool is called *and* that its
arguments are well-typed.
**Why (beginner):** Without this, production code has to defensively validate and retry every
tool call because the model can return a subtly wrong type or skip a required field.
**Caveat / contested:** Strict mode only supports a subset of JSON Schema and is built on the
same compiled-grammar pipeline as structured outputs; schemas are cached server-side for up to
24 hours. ⚠️ **WARNING** — Anthropic explicitly warns not to put PHI (protected health
information) in schema `enum`/`const`/`pattern` values, because those cached schemas don't get
the same HIPAA protections as message content — a compliance-relevant default, not just a
styling nit.
**Sources:** [platform.claude.com/docs — Strict tool use](https://platform.claude.com/docs/en/agents-and-tools/tool-use/strict-tool-use) (fetched 9 Aug 2026)
**Confidence:** vendor-documented

### Practice: Format parallel tool-call results as one message, results-before-text
**Do:** When Claude's response contains multiple `tool_use` blocks in one turn, return **one**
`tool_result` per `tool_use`, **all together in a single next `user` message**, matched by
`tool_use_id`, with every `tool_result` block appearing before any plain-text content in that
message. Execution order (concurrent vs. sequential) is entirely your choice.
**Why (beginner):** Get this wrong (one `user` message per result, or text before the results)
and you'll hit a 400 error ("tool_use ids were found without tool_result blocks immediately
after") or silently train Claude to stop batching calls, losing the latency benefit.
**Caveat / contested:** If you deliberately skip running a call, you must still return a
`tool_result` for it with `is_error: true` — you can't just omit it.
**Sources:** [platform.claude.com/docs — Parallel tool use](https://platform.claude.com/docs/en/agents-and-tools/tool-use/parallel-tool-use) (fetched 9 Aug 2026) · [platform.claude.com/docs — Handle tool calls](https://platform.claude.com/docs/en/agents-and-tools/tool-use/handle-tool-calls) (fetched 9 Aug 2026)
**Confidence:** vendor-documented

### Practice: Give Claude actionable, specific `is_error` messages, not opaque failures
**Do:** When a tool execution fails, return `"is_error": true` with a *specific, actionable*
error string (e.g., `"Rate limit exceeded. Retry after 60 seconds."`) instead of a generic
`"failed"`. For invalid/missing-parameter tool calls, Claude will typically retry 2–3 times with
corrections once it sees a clear error before giving up and apologizing to the user.
**Why (beginner):** The error text is the only feedback loop Claude has — a vague error just gets
repeated verbatim to your user instead of fixed.
**Caveat / contested:** Server tools (web search, code execution, etc.) are different: Anthropic
handles their errors transparently and you generally don't need to construct `is_error` results
for them yourself.
**Sources:** [platform.claude.com/docs — Handle tool calls](https://platform.claude.com/docs/en/agents-and-tools/tool-use/handle-tool-calls) (fetched 9 Aug 2026)
**Confidence:** vendor-documented

### Practice: Respect the strict formatting rules that bind `tool_use`/`tool_result` together
**Do:** A `tool_result` block must immediately follow its corresponding `tool_use` message — you
cannot insert other messages in between. If Claude's turn also invoked a server tool that hasn't
resolved yet, your reply must contain *only* `tool_result` blocks for the client tools, nothing
else, or the request 400s naming the unresolved server tool.
**Why (beginner):** This is one of the most common "why is my agent loop broken" bugs for people
hand-rolling the tool-use loop instead of using an SDK helper.
**Caveat / contested:** Anthropic ships a "Tool Runner" SDK abstraction specifically so most
developers never have to implement this formatting by hand.
**Sources:** [platform.claude.com/docs — Handle tool calls](https://platform.claude.com/docs/en/agents-and-tools/tool-use/handle-tool-calls) (fetched 9 Aug 2026)
**Confidence:** vendor-documented

### Practice: With extended thinking, pass `thinking` blocks back to the API unmodified
**Do:** "Extended thinking" is Claude's optional mode where it produces a visible chain-of-thought
`thinking` block before acting. When a `tool_use` follows a `thinking` block, you must echo the
`thinking` block(s) back to the API exactly as received (same content, same `signature`)
alongside the `tool_use`/`tool_result` round trip — required within the current tool-use turn,
recommended across turns. Never rearrange, edit, or partially drop consecutive thinking blocks
(this includes `redacted_thinking` blocks) — the API rejects modified thinking blocks with a 400
error.
**Why (beginner):** Thinking is how Claude "shows its work" mid-tool-loop; stripping or editing
it breaks the reasoning chain the model needs to pick up where it left off.
**Caveat / contested:** Whether *older* turns' thinking blocks are kept or auto-stripped by the
API depends on the model generation (newer Opus/Sonnet models keep them all; Haiku models and
older generations keep only the latest turn) — check the current per-model table before relying
on either behavior. 🕒 verify live.
**Sources:** [platform.claude.com/docs — Thinking](https://platform.claude.com/docs/en/build-with-claude/thinking) (fetched 9 Aug 2026)
**Confidence:** vendor-documented

### Practice: Use interleaved thinking for multi-step tool reasoning, but check the header/model matrix first
**Do:** Interleaved thinking lets Claude reason between individual tool calls within one
assistant turn (not just before the first call). On models with **adaptive** thinking, this
happens automatically with no extra header. On older models using **manual** extended thinking,
you must add the `interleaved-thinking-2025-05-14` beta header, and support is inconsistent:
Claude Haiku 4.5 doesn't support it at all, and Claude Opus 4.6 supports it only in adaptive
mode, not manual mode.
**Why (beginner):** Without interleaving, Claude reasons once up front and then chains tool calls
somewhat "blindly"; with it, Claude can react to each tool's result before deciding the next
step.
**Caveat / contested:** This is a genuinely fiddly compatibility matrix that changes by model
generation — don't assume a header that worked on one model does anything on another (the API
silently ignores unsupported headers rather than erroring). 🕒 verify live.
**Sources:** [platform.claude.com/docs — Thinking](https://platform.claude.com/docs/en/build-with-claude/thinking) (fetched 9 Aug 2026) · [platform.claude.com/docs — Extended thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking) (fetched 9 Aug 2026)
**Confidence:** vendor-documented

### Practice: Buffer streamed tool-call JSON until `content_block_stop` before parsing
**Do:** When streaming, a `tool_use` block's `input` arrives as a series of `input_json_delta`
events carrying **partial JSON strings**, not a series of valid partial objects. Accumulate the
string fragments and parse once at `content_block_stop` (or use your SDK's partial-JSON helper)
rather than trying to `JSON.parse()` every delta.
**Why (beginner):** Naively parsing each delta as JSON will throw on most chunks, since the
string isn't valid JSON until the block is complete.
**Caveat / contested:** A separate opt-in feature, "fine-grained tool streaming"
(`eager_input_streaming`), changes this buffering behavior per-tool — check whether it's enabled
before assuming standard buffering rules apply.
**Sources:** [platform.claude.com/docs — Streaming Messages](https://platform.claude.com/docs/en/build-with-claude/streaming) (fetched 9 Aug 2026)
**Confidence:** vendor-documented

### Practice: Once you have 10+ tools, use tool search / `defer_loading` instead of dumping everything into context
**Do:** For small toolsets, pass full tool definitions as usual. Once you exceed roughly 10
tools, have more than ~10k tokens of tool definitions, aggregate multiple MCP servers, or notice
tool-selection accuracy degrading, enable the `tool_search_tool_regex_20251119` or
`tool_search_tool_bm25_20251119` server tool (those are the `type` values for the API request;
the plain `tool_search_tool_regex`/`_bm25` names refer to the tool, not the request field — using
the unversioned name as the `type` value returns a 400) and mark most tools `defer_loading:
true`, keeping only your 3–5 most-used tools non-deferred. Anthropic's own worked example: a
typical 5-server MCP setup (GitHub, Slack, Sentry, Grafana, Splunk) can consume ~55k tokens of
tool definitions up front; tool search reportedly cuts that by over 85%, loading only the 3–5
tools actually needed per request.
**Why (beginner):** Every tool definition you load costs context tokens on *every single
request* whether or not it's used that turn — and Anthropic states tool-selection accuracy
measurably drops once you're past roughly 30–50 tools in context at once.
**Caveat / contested:** The "~55k tokens" and "85%" figures come from one Anthropic
example/benchmark, not an independent audit — treat as illustrative, not a guarantee for your own
tool mix. 🕒 verify live (tool search tool versions are still dated/beta-flagged as of this
writing).
**Sources:** [platform.claude.com/docs — Tool search tool](https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-search-tool) (fetched 9 Aug 2026)
**Confidence:** vendor-documented

### Practice: Cache tool definitions deliberately, and know what silently invalidates the cache
**Do:** Put `cache_control: {"type": "ephemeral"}` on the *last* tool in your `tools` array to
cache the whole tool-definitions prefix (this only takes effect if your request already has at
least one `cache_control` marker somewhere — requests without prompt caching enabled don't get
any automatic breakpoint). Be aware of the invalidation hierarchy: editing any tool definition
blows away the *entire* cache (tools, system, messages); toggling `tool_choice` or
`disable_parallel_tool_use` only invalidates the messages-level cache; toggling server tools like
web search invalidates system+messages.
**Why (beginner):** ⚠️ **WARNING** — prompt caching is one of the few practical cost/latency
levers in a tool-heavy agent loop, but an unintentional cache-buster (like flipping `tool_choice`
every other turn) can quietly double your token bill with no visible error.
**Caveat / contested:** Server-tool results get an *automatic* cache breakpoint with a fixed
5-minute TTL (time to live) regardless of what TTL you set elsewhere, but only once your request
already uses caching at all — a detail easy to miss when reasoning about cache costs. 🕒 verify
live (pricing/TTL specifics).
**Sources:** [platform.claude.com/docs — Tool use with prompt caching](https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-use-with-prompt-caching) (fetched 9 Aug 2026)
**Confidence:** vendor-documented

### Practice: Treat every `tool_result` as untrusted, potentially hostile content
**Do:** Never assume the content coming back from a tool call (a fetched web page, an inbound
email body, a third-party API response, OCR text) is safe. Keep untrusted content inside
`tool_result` blocks (never copy it into a `system` prompt or plain `text` block), tell Claude
explicitly what the content is and where it came from, and state in your system prompt that
tool-returned content is data to report on, not instructions to follow. JSON-encoding untrusted
strings (rather than concatenating raw text) removes the ambiguous delimiters an attacker needs
to "break out" into an instruction context.
**Why (beginner):** This is the mechanism behind **indirect prompt injection**: an attacker who
can't talk to your app directly can still plant instructions in a document, webpage, or email
that your agent later reads via a tool, and get the agent to act on them instead of the user's
actual request.
**Caveat / contested:** Anthropic states Claude is "inherently resilient" to these attacks but
still recommends layered defenses (screening tool output with a cheap classifier model,
least-privilege tool scopes, red-teaming). Independent security researcher Simon Willison frames
the underlying structural risk as the "lethal trifecta" — an agent that combines (1) access to
private data, (2) exposure to untrusted content, and (3) the ability to communicate externally is
exploitable regardless of how good the model's training is — and is explicit that no "guardrail"
product he's aware of closes this gap to zero; the safest fix is to avoid combining all three
capabilities in one agent at all.
**Sources:** [platform.claude.com/docs — Mitigate jailbreaks and prompt injections](https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/mitigate-jailbreaks) (fetched 9 Aug 2026) · [simonwillison.net — The lethal trifecta for AI agents](https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/) (published 16 Jun 2025)
**Confidence:** independently-corroborated

### Practice: ⚠️ WARNING — sandbox the bash/computer-use/code-execution tools; never let them touch real credentials by default
**Do:** The bash tool and computer-use tool are **client tools**: Claude only *requests* a
command or a click, your application actually executes it. Anthropic's explicit precautions for
computer use (which generalize to bash and code execution): run in a dedicated VM/container with
minimal privileges, never give the model access to real account logins or secrets, allowlist
outbound internet domains, and require human confirmation before any action with real-world
consequences (payments, agreeing to terms of service — and, as a reasonable extrapolation beyond
Anthropic's own listed examples, destructive actions like deleting data). At minimum for a
beginner setup: run the tool in a container with no network access and a disposable, non-root
user — never point a bash/computer-use tool directly at your own machine or a real account.
Anthropic's own engineering writeup on how it contains Claude across its products makes the
credential point explicit: "if credentials never enter the sandbox, they can't be exfiltrated" —
regardless of whether the cause is an honest mistake, the model "creatively" working around a
restriction, or a deliberate attack.
**Why (beginner):** A bash or computer-use tool is arbitrary code/UI execution on a real machine
or account. If you wire it up without isolation, a hallucinated command, a prompt-injected
instruction, or a plain model mistake can delete files, run up cloud bills, or leak secrets.
**Caveat / contested:** Anthropic itself states human-approval prompts alone are not a sufficient
defense — user studies it cites found people approve roughly 93% of permission prompts with
attention declining over a session ("approval fatigue"), so OS-level sandboxing/VMs are presented
as the primary control, with human confirmation as a secondary layer. Independent commentator
Simon Willison, reviewing the same Anthropic writeup, singled out the credential-isolation
approach and Anthropic's decision to publish it as unusually transparent compared to the rest of
the industry — that is an endorsement of the disclosure, not an independent security audit of the
mitigations themselves, so treat the independent-corroboration label here as "a second publisher
vouched for this being a good disclosure," not "a second publisher tested these mitigations."
**Sources:** [platform.claude.com/docs — Computer use tool](https://platform.claude.com/docs/en/agents-and-tools/tool-use/computer-use-tool) (fetched 9 Aug 2026) · [anthropic.com/engineering — How we contain Claude](https://www.anthropic.com/engineering/how-we-contain-claude) (published 25 May 2026) · [simonwillison.net — commentary on "How we contain Claude"](https://simonwillison.net/2026/May/30/how-we-contain-claude/) (published 30 May 2026)
**Confidence:** independently-corroborated

### Practice: Don't rely on Claude always asking for missing required parameters
**Do:** If a user's request under-specifies a required tool parameter, don't assume Claude will
stop and ask. Anthropic's own docs contrast **Opus** and **Sonnet**: "Claude Opus is much more
likely to recognize that a parameter is missing and ask for it. Claude Sonnet might ask… But it
might also infer a reasonable value" — and a separate aside notes Haiku-class models used for
straightforward tools may also infer missing parameters rather than ask. If a wrong guess would
be costly, validate required fields client-side before executing, or use `strict: true` plus a
`required` array to at least guarantee the field is *present* (not that its value is *correct*).
**Why (beginner):** This is a genuine hallucination risk that's easy to miss in testing: "What's
the weather?" with no city can silently produce `{"location": "New York, NY"}` (Anthropic's own
example, attributed specifically to Claude Sonnet) instead of a clarifying question, and your
tool executes against the wrong input with no error at all.
**Caveat / contested:** `strict: true` fixes *type and presence* conformance, not semantic
correctness — a strictly-valid but factually wrong guessed value will still pass strict-mode
validation.
**Sources:** [platform.claude.com/docs — Tool use overview](https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview) (fetched 9 Aug 2026) · [platform.claude.com/docs — Define tools](https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools) (fetched 9 Aug 2026)
**Confidence:** vendor-documented

### Practice: Provide `input_examples` for tools with complex or format-sensitive parameters
**Do:** For tools with nested objects, optional parameters, or picky formats (dates, enums), add
an `input_examples` array of 2–3 valid, schema-conformant example inputs to the tool definition,
alongside (not instead of) a clear `description`.
**Why (beginner):** Descriptions alone can under-specify exactly how to format a tricky field;
one or two concrete correct examples often fix a whole class of malformed-argument errors more
cheaply than lengthening the prose description.
**Caveat / contested:** `input_examples` is validated at request time (an invalid example is a
400 error, not a warning) and is **not supported on server-side tools** like web search — it only
applies to your own and Anthropic-schema client tools. Adds a modest but real token cost. 🕒
verify live for exact token estimates.
**Sources:** [platform.claude.com/docs — Define tools](https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools) (fetched 9 Aug 2026)
**Confidence:** vendor-documented

### Practice: Budget for tool-use token overhead — it's not free even when no tool is called
**Do:** Remember that supplying a non-empty `tools` array injects a hidden system prompt whose
size varies by model *and* by `tool_choice` (forcing a call with `any`/`tool` costs more tokens
than `auto`/`none` on the same model — e.g., Claude Opus 5 shows 286 tokens for `auto`/`none` vs.
406 for `any`/`tool`, per Anthropic's own per-model table). This is on top of the tokens your own
tool names/descriptions/schemas consume, and on top of every `tool_use`/`tool_result` block
exchanged in a multi-turn agentic loop.
**Why (beginner):** ⚠️ **WARNING** — people new to tool use are often surprised that "just
defining tools you never end up calling" still costs input tokens on every request; it's easy to
under-budget a tool-heavy agent's per-turn cost.
**Caveat / contested:** The exact per-model token counts change across model releases and are
explicitly 🕒 verify live — don't hardcode a number from any snapshot of this doc into cost
projections.
**Sources:** [platform.claude.com/docs — Tool use overview](https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview) (fetched 9 Aug 2026)
**Confidence:** vendor-documented

### ⚠ PENDING — current tool-use surface areas not yet covered in this snapshot
As of 09 Aug 2026, Anthropic's tool-use overview page also lists an **advisor tool** (lets Claude
consult a second, typically-stronger model mid-task; beta) and a separate **Claude Managed
Agents** product (a hosted agent harness), plus a **memory tool** (cross-conversation file-based
persistence) alongside bash/text-editor/computer-use — none of which this snapshot covers in
depth. They were flagged by this run's staleness review but not independently re-verified beyond
the primary overview page in time for this publish; a future refresh should give them their own
practices rather than a footnote. ⚠ #tool-use-advisor-and-managed-agents

---

## Part 2 — OpenAI (Chat Completions & Responses APIs)

**Note on URLs:** OpenAI's docs moved during this research window — `platform.openai.com/docs/guides/...`
now redirects to `developers.openai.com/api/docs/guides/...`. Links below use the URLs actually
fetched. 🕒 **verify live** — check whether this host is still current if you land on a dead link
later.

### Practice: Write function names, descriptions, and parameter docs as if for a stranger ("the intern test")
**Do:** Give every function a clear name and a detailed `description`, and describe the purpose,
format, and units of every parameter. OpenAI's own framing: could someone unfamiliar with your
system call the function correctly using only the schema text? Vague descriptions directly cause
wrong tool choice and wrong arguments, because the model leans almost entirely on the description
text to decide when/how to call a tool.
**Why (beginner):** The model has no access to your source code — the JSON Schema *is* the entire
interface it sees. If the description is thin, the model guesses, and guesses turn into wrong or
hallucinated arguments in production.
**Caveat / contested:** This is qualitative guidance, not something you can unit-test directly;
pair it with the schema-drift testing practice below.
**Sources:** [developers.openai.com/api/docs/guides/function-calling](https://developers.openai.com/api/docs/guides/function-calling) (fetched 2026-08-09) · [nwos.com — "OpenAI Function Calling: Don't Let Your Schema Drift"](https://www.nwos.com/daily/openai-function-calling-dont-let-your-schema-drift) (published 15 Jun 2026)
**Confidence:** independently-corroborated

### Practice: Turn on strict mode (`strict: true`) for function schemas, and know the hard structural limits
**Do:** Set `strict: true` on function tools so the API enforces the JSON Schema instead of
treating it as a best-effort hint. Strict mode requires `additionalProperties: false` on every
object and every field listed in `required` (simulate "optional" fields with a `["string",
"null"]` type union). In the Responses API, omitting `strict` now *attempts to normalize your
schema into strict mode when possible*, falling back to non-strict if the schema is incompatible;
in Chat Completions, functions remain non-strict by default and you must opt in explicitly. Strict
mode/structured outputs cap schemas at 5,000 total object properties, 10 nesting levels, 1,000
enum values, and 120,000 total characters across names/enums, and don't support `allOf`, `not`,
`dependentRequired`, or `if`/`then`/`else`. Prefer flatter, shallower schemas where practical —
deep nesting is measurably harder to keep within these limits and easier to get subtly wrong.
**Why (beginner):** Without strict mode, the model can (and does) return a number as a string,
drop a required field, add an extra key, or emit an enum value that doesn't exist in your list —
all things your code then has to defensively catch. Strict mode pushes that validation into the
API.
**Caveat / contested:** For fine-tuned models specifically, strict mode is currently disabled
when the model calls multiple functions in one turn, and in that same fine-tuned-model context
schemas go through extra processing on first use (then get cached) and aren't eligible for
zero-data-retention — those two caveats are scoped to fine-tuned models in OpenAI's docs, not a
general strict-mode property. 🕒 verify live — these numeric limits are exactly the kind of value
OpenAI changes without much fanfare.
**Sources:** [developers.openai.com/api/docs/guides/function-calling](https://developers.openai.com/api/docs/guides/function-calling) (fetched 2026-08-09) · [developers.openai.com/api/docs/guides/structured-outputs](https://developers.openai.com/api/docs/guides/structured-outputs) (fetched 2026-08-09)
**Confidence:** independently-corroborated

### Practice: Keep the active tool list small; don't dump your whole tool catalog into every request
**Do:** OpenAI's own soft target is fewer than ~20 functions available at the start of a turn —
tool definitions are injected into context and billed as input tokens, so a big tool list is a
real, recurring cost, not just noise. OpenAI's own guidance also recommends namespacing ("group
related tools by domain, such as `crm`, `billing`, or `shipping`") and deferring less-used tools
via `tool_search`. For larger catalogs, one independent write-up reports production accuracy
degrading once a catalog passes roughly 10–20 tools in active rotation, because the model has to
pick the right one out of a longer, more repetitive list.
**Why (beginner):** More tools isn't free and isn't harmless — this is on top of the plain
token/cost overhead.
**Caveat / contested:** The exact threshold is contested and 🕒 verify live — OpenAI's own soft
guidance says "fewer than 20," one independent write-up reports the measurable accuracy cliff
closer to 10–15, and a claimed hard technical ceiling of 128 tools per agent could not be verified
against a fetched OpenAI page this run — flagged thin for that specific number. Treat "keep it
small and use retrieval for the rest" as the durable takeaway, not any single number.
**Sources:** [developers.openai.com/api/docs/guides/function-calling](https://developers.openai.com/api/docs/guides/function-calling) (fetched 2026-08-09) · [machinelearningmastery.com — "The Complete Guide to Tool Selection in AI Agents"](https://machinelearningmastery.com/the-complete-guide-to-tool-selection-in-ai-agents/) (published 6 Jul 2026)
**Confidence:** independently-corroborated

### Practice: Control tool invocation explicitly with `tool_choice`
**Do:** Use `tool_choice: "auto"` (default — model decides whether/which to call), `"required"`
(force at least one call), a named-function object like `{"type":"function","name":"get_weather"}`
to force exactly one specific tool, `"none"` to suppress tool calls entirely, or an "allowed
tools" subset to restrict which of your already-declared tools can be picked without changing the
tool list itself (useful for prompt-caching, since the cached list stays stable).
**Why (beginner):** Letting the model decide ("auto") is right most of the time, but for a
fixed-shape task (e.g., "always call `classify_ticket`") forcing the exact function removes an
entire class of failure where the model answers in prose instead of calling the tool.
**Caveat / contested:** Forcing a tool doesn't validate the *arguments* it fills in — you still
need the validation practice below.
**Sources:** [developers.openai.com/api/docs/guides/function-calling](https://developers.openai.com/api/docs/guides/function-calling) (fetched 2026-08-09)
**Confidence:** vendor-documented

### Practice: Don't assume `parallel_tool_calls` is safe for tools with side effects
**Do:** OpenAI's API can call multiple functions in a single turn when `parallel_tool_calls` is
left at its default. Before you rely on that, check whether your tools are **atomic** (each call
either fully happens or doesn't — no half-applied state), **idempotent** (calling it twice with
the same input has the same effect as calling it once — see the idempotency practice in Part 3
for a worked example), and **independent** (no tool depends on another's write having already
happened). If any tool mutates shared state, writes to a database, or otherwise has a real-world
side effect that another tool call in the same turn could race against, set `parallel_tool_calls:
false` so the API calls at most one tool per turn.
**Why (beginner):** Parallel calls that silently race on the same resource, or where one tool
secretly needs another one's result first, don't crash — they corrupt state quietly, and by the
time the wrong output shows up several turns later the connection to the original parallel call
is easy to miss.
**Caveat / contested:** Per one independent blog (not confirmed against OpenAI's own docs this
run), reasoning models (o3/o4-mini) may ignore or reject the `parallel_tool_calls` parameter
outright and return an error if you set it explicitly — behavior here is model-dependent, so 🕒
verify live against whichever model you're actually calling.
**Sources:** [developers.openai.com/api/docs/guides/function-calling](https://developers.openai.com/api/docs/guides/function-calling) (fetched 2026-08-09) · [tianpan.co — "Parallel Tool Calls in LLM Agents: The Coupling Test You Didn't Know You Were Running"](https://tianpan.co/blog/2026-04-10-parallel-tool-calls-hidden-coupling) (published 10 Apr 2026)
**Confidence:** independently-corroborated

### Practice: When streaming, accumulate function-call argument deltas — don't act on partial JSON
**Do:** With `stream: true`, function call arguments arrive incrementally as events:
`response.output_item.added` announces the call with empty arguments, `response.function_call_arguments.delta`
streams argument text piece by piece, and `response.function_call_arguments.done` signals the
arguments are complete. Buffer the deltas and only parse/execute once you've received the "done"
event (or the stream ends).
**Why (beginner):** It's tempting to try to parse-as-you-go for a "live" UI, but a half-received
`{"city": "San Fra` is not valid JSON. Wait for the complete argument string before calling
`json.loads`/`JSON.parse` on it.
**Caveat / contested:** This is Responses-API event naming; Chat Completions streams the same
underlying idea via incremental `delta` chunks on `tool_calls`, with slightly different event
shapes — check which API you're on before wiring up a parser.
**Sources:** [developers.openai.com/api/docs/guides/function-calling](https://developers.openai.com/api/docs/guides/function-calling) (fetched 2026-08-09)
**Confidence:** vendor-documented

### Practice: Validate and defensively parse tool-call arguments before you execute anything
**Do:** Treat every function call's `arguments` string as untrusted input from a probabilistic
system, not a trusted RPC payload. Check for empty/whitespace-only arguments before parsing, use
an error-tolerant JSON parse or fall back gracefully on malformed JSON, and re-validate the
parsed object against your schema (types, enum membership, required fields) before running the
underlying function — and if an argument is an ID or reference, check that it actually exists and
that the caller is authorized for it before acting on it, since a syntactically valid ID can still
be hallucinated. Common failure shapes reported by developers: trailing commas, unescaped
newlines, markdown code-fences wrapped around the JSON, extra commentary text mixed in with the
JSON, or a value type that doesn't match the schema.
**Why (beginner):** Even OpenAI's own SDK documentation is blunt about this: the model does not
always generate valid JSON and may hallucinate parameters not defined by your function schema.
Strict mode/structured outputs (above) dramatically reduces how often this happens, but doesn't
reduce it to zero, and it does nothing for semantic mistakes like a hallucinated customer ID that
happens to be syntactically valid.
**Caveat / contested:** This guidance rests on OpenAI's own community forum quoting OpenAI's own
Node.js SDK docs — a single publisher, not independent corroboration, so this is vendor-documented
rather than independently-corroborated. The general principle (never trust model-generated
arguments) is durable industry practice, but treat this specific writeup as one source, not two.
**Sources:** [community.openai.com — "Don't trust the output for functions"](https://community.openai.com/t/dont-trust-the-output-for-functions/269522) (posted 18 Jun 2023, quotes OpenAI's own Node.js library docs: "the model does not always generate valid JSON, and may hallucinate parameters")
**Confidence:** vendor-documented

### Practice: Guard against schema drift with real API tests, not just code review
**Do:** Derive your JSON schema from the same source of truth as your function implementation
wherever you can (e.g., generate enum values from the same constants your code validates against)
instead of hand-maintaining two parallel definitions. Add feature tests that send representative
natural-language prompts to the real OpenAI API (not a mock) and assert the model calls the
expected function with the expected argument keys, so a schema that silently falls out of sync
with the implementation gets caught by CI instead of by a user. ⚠️ **WARNING:** every such test
run is a **billed API call** — wiring this into a run-on-every-push CI job can produce a real,
recurring bill; prefer a scheduled or manually-gated job over "on every push" for this specific
kind of test.
**Why (beginner):** When the schema and the implementation disagree (e.g., you add a new
parameter to the function but forget to add it to the schema), the model never even knows the new
option exists — there's no crash, just a silently worse response. That's a hard failure mode to
notice without a test that actually exercises the model.
**Caveat / contested:** Single independent source this run; treat the specific "always hit the
real API in tests" recommendation as good practice rather than an industry-wide consensus.
**Sources:** [nwos.com — "OpenAI Function Calling: Don't Let Your Schema Drift"](https://www.nwos.com/daily/openai-function-calling-dont-let-your-schema-drift) (published 15 Jun 2026)
**Confidence:** thin

### Practice: On the Responses API, correlate tool calls and results by `call_id` and preserve reasoning items
**Do:** In the Responses API, a function call and its result are two separate "items" in the
output/input stream, matched by a `call_id` — don't try to stuff the result back into a "message"
the way Chat Completions' `role`-tagged array works. For reasoning models (o-series, and as of
this snapshot the current GPT-5.6-series flagship models), any reasoning item the API returns
alongside a tool call must be passed back unmodified along with the tool result — OpenAI's own
migration guide describes dropping a reasoning/function-call/function-call-output item as a
"common mistake" that breaks the model's ability to continue its chain of thought (we could not
confirm this always produces a request-level API error, so don't rely on an error to catch it).
If you need statelessness or zero-data-retention, set `store: false` and replay the returned
`encrypted_content` reasoning items rather than dropping them.
**Why (beginner):** This is the single most common Responses-API migration bug: sending a
function result without its matching `call_id`, or treating every output entry as a plain message
and discarding the `reasoning`/`function_call` item types along the way. Both silently break
multi-step tool use.
**Caveat / contested:** Even with `previous_response_id` managing prior turns for you, all prior
input tokens in the chain are still billed as input tokens on every subsequent call —
statefulness saves you code, not tokens. 🕒 verify live — billing mechanics for chained responses
are a place OpenAI could plausibly change behavior.
**Sources:** [developers.openai.com/api/docs/guides/migrate-to-responses](https://developers.openai.com/api/docs/guides/migrate-to-responses) (fetched 2026-08-09) · [developers.openai.com/cookbook/examples/reasoning_function_calls](https://developers.openai.com/cookbook/examples/reasoning_function_calls) (fetched 2026-08-09, no separate publish date shown on page beyond an internal "as of May 2025" reference)
**Confidence:** vendor-documented

### Practice: Understand the Responses vs. Chat Completions split before picking one for a new tool-using agent
**Do:** For new agentic / tool-heavy work, prefer the Responses API: it models tool calls and
results as distinct typed items (`function_call`, `function_call_output`, `reasoning`) rather than
everything being a differently-tagged "message," attempts to normalize function schemas into
strict mode automatically (vs. non-strict by default in Chat Completions), and gives you native
built-in tools (web search, file search, code interpreter, computer use, remote MCP) alongside
your custom functions. Chat Completions still works and is not on an announced deprecation
timeline as of this snapshot.
**Why (beginner):** ⚠️ **WARNING** — two of the "attractive" built-in tools named above, **code
interpreter** and **computer use**, mean giving the model the ability to execute real code or
control a real computer, not just answer questions. Treat them with the exact same caution as
Claude's bash/computer-use tools in Part 1: run them in an isolated sandbox with no access to real
credentials, allowlist what they can reach on the network, and require human confirmation before
any consequential action. Don't enable either one just because it's presented as "the newer,
better API" — the safety requirements are the same regardless of which vendor's version you use.
If you're starting a new project, don't default to Chat Completions out of habit/tutorial-
familiarity without checking whether Responses' item model and native tool support would save you
real orchestration code.
**Caveat / contested:** OpenAI's docs state there is no announced deprecation timeline for Chat
Completions itself — unlike the separate **Assistants API**, which OpenAI has set for shutdown on
**26 Aug 2026**. That date is only about two weeks after this snapshot; if you're reading this
entry after that date, the Assistants API is gone and any of its endpoints (`/v1/assistants`,
`/v1/threads`) will already have stopped working — 🕒 verify live, treat the date itself (not just
the fact of the deprecation) as something to recheck. Migration between Chat Completions and
Responses is nontrivial for existing codebases; this is guidance for new work, not a mandate to
migrate. Independent corroboration for "Responses is the forward direction" here is thin (one
undated blog post) — treat this practice's framing as OpenAI's stated direction, not an
independently verified consensus.
**Sources:** [developers.openai.com/api/docs/guides/migrate-to-responses](https://developers.openai.com/api/docs/guides/migrate-to-responses) (fetched 2026-08-09) · [dev.to — "Chat Completions vs OpenAI Responses API: What Actually Changed"](https://dev.to/dev-in-progress/chat-completions-vs-openai-responses-api-what-actually-changed-4bco) (page shows "Posted on Mar 18," year not displayed on the page; fetched 2026-08-09)
**Confidence:** vendor-documented

### Practice: Treat data returned from tool calls as untrusted input, not as data you control
**Do:** Anything a tool call fetches from the outside world (a webpage, a document, an email, a
search result, another system's API response) can contain text engineered to look like
instructions to the model — this is indirect/tool-result prompt injection. Design so untrusted
tool output never directly drives another tool call without a checkpoint: prefer structured
outputs between steps (enums/fixed schemas instead of freeform text) to remove channels an
attacker can exploit, and require human confirmation before an agent executes any consequential
action (not just destructive ones — OpenAI's own guidance says enable approvals for "every
operation, including reads and writes" in higher-risk workflows). Note that this practice applies
directly to the code-interpreter/computer-use tools flagged above — a webpage or file a
code-interpreter call reads is exactly the kind of untrusted content this practice is about. A
widely cited heuristic (Meta's "Agents Rule of Two," as summarized by the independent source
below): an autonomous agent should have at most two of (a) access to private/sensitive data, (b)
exposure to untrusted content, (c) the ability to change state or communicate externally —
combining all three ("the lethal trifecta") without a human in the loop is the highest-risk
configuration.
**Why (beginner):** ⚠️ **WARNING** — a tool-using agent that reads untrusted content (a webpage, a
customer email, a scraped file) and can also take real actions (send email, run code, make a
purchase, write to a database) is the classic setup where a hidden instruction in that content
hijacks the agent. This is not a solved problem — OpenAI's own agent-safety documentation stops
short of prescribing a specific technical fix for poisoned tool-response data and instead
recommends architectural isolation and approval steps.
**Caveat / contested:** OpenAI's own current safety guidance for agent builders is candidly thin
on this exact vector (it addresses prompt injection generally more than "injection via a tool's
return value" specifically), and OWASP (the Open Worldwide Application Security Project, which
publishes widely used security-risk checklists) reportedly maps prompt injection to six of its
ten categories in its Top 10 for Agentic Applications — this is an actively unsolved, fast-moving
area, not a checklist you can complete once. 🕒 verify live.
**Sources:** [developers.openai.com/api/docs/guides/agent-builder-safety](https://developers.openai.com/api/docs/guides/agent-builder-safety) (fetched 2026-08-09) · [helpnetsecurity.com — "Prompt injection still drives most agentic AI security failures in production"](https://www.helpnetsecurity.com/2026/06/11/owasp-prompt-injection-ai-security-failures/) (published 11 Jun 2026)
**Confidence:** independently-corroborated

### Practice: Handle rate limits and transient errors with backoff; don't retry billing/quota errors
**Do:** For `RateLimitError`, honor a `Retry-After` response header if present; if it's absent,
use exponential backoff with jitter. For transient failures (timeouts, `APIConnectionError`, 5xx
`APIError`), wait briefly and retry. For billing/spend/quota errors, retrying will not help —
"retrying billing, spend, or quota errors won't restore API access"; update the relevant credits
or limits before sending another request.
**Why (beginner):** A naive "retry on any exception" loop wastes time (and can make rate limiting
worse) on errors that will never resolve themselves. Distinguishing "wait and retry" errors from
"fix your account" errors up front avoids that.
**Caveat / contested:** Vendor-documented only this run — this is standard, uncontroversial
API-client hygiene, but no independent OpenAI-specific corroboration was fetched this pass.
**Sources:** [developers.openai.com/api/docs/guides/error-codes](https://developers.openai.com/api/docs/guides/error-codes) (fetched 2026-08-09)
**Confidence:** vendor-documented

---

## Part 3 — Cross-Provider / Generic Patterns

These practices hold regardless of which model vendor you call, or come from frameworks/standards
that sit above a single vendor's API (MCP, LangChain/LangGraph, OWASP).

### Practice: Give each tool a single, unambiguous job
**Do:** Design one tool per distinct operation (`create_customer`, `get_customer`) rather than one
multipurpose tool with an internal `action` or `mode` parameter (`manage_customer(action=...)`).
If two tools' descriptions can't be told apart without saying "unlike X, this one…," merge or
redesign them.
**Why (beginner):** When a tool does one thing, the model doesn't have to guess "which mode of
this tool do I want" before it can even start solving your task — and when something goes wrong,
you know exactly which tool caused it. A pile of overlapping, similarly-named tools is one of the
most common reasons agents call the wrong thing or get stuck.
**Caveat / contested:** This is a genuine, live disagreement between credible sources, not a
settled rule. Anthropic's own guidance (Part 1, "Consolidate related operations into fewer,
namespaced tools") argues the opposite for its own product: "rather than creating a separate tool
for every action… group them into a single tool with an `action` parameter." Both positions are
defensible — one-tool-per-operation makes each tool's job unambiguous; one-tool-per-workflow
reduces total tool count and namespace clutter. Test both approaches against your own model and
tool count rather than assuming either is universally correct.
**Sources:** [machinelearningmastery.com — "AI Agent Tool Design: What Works and What Doesn't"](https://machinelearningmastery.com/ai-agent-tool-design-what-works-and-what-doesnt/) (published 15 Jun 2026)
**Confidence:** contested

### Practice: Write tool names and descriptions like onboarding docs, and namespace to avoid collisions
**Do:** Write each tool description as if explaining it to a new hire: state its purpose, its
scope, and when *not* to use it (redirect to the right tool instead of just describing this one).
Use unambiguous parameter names (`user_id`, not `user`). When you have tools from multiple
services or servers, group them with a consistent prefix or suffix (e.g. `asana_search`,
`jira_search`) so the model — and any client that aggregates tools from more than one source —
can tell them apart. LangChain's own tool docs recommend `snake_case` names without spaces, since
"some model providers have issues with or reject names containing spaces or special characters."
**Why (beginner):** The model only knows what a tool does from its name, description, and schema —
it can't read your source code. Vague or duplicate-sounding names cause the model to pick the
wrong tool; missing namespacing causes outright collisions once you connect more than one tool
source (e.g. two MCP servers that both expose a tool called `search`).
**Caveat / contested:** The MCP spec notes that a server's own `name` field is not guaranteed
unique across servers and should not be relied on for disambiguation — the prefixing has to be
done deliberately by whoever aggregates the tools, not assumed to come for free.
**Sources:** [anthropic.com/engineering/writing-tools-for-agents](https://www.anthropic.com/engineering/writing-tools-for-agents) (11 Sep 2025) · [docs.langchain.com/oss/python/langchain/tools](https://docs.langchain.com/oss/python/langchain/tools) (fetched 09 Aug 2026, undated page) · [modelcontextprotocol.io — server/tools specification](https://modelcontextprotocol.io/specification/2026-07-28/server/tools) (spec dated 28 Jul 2026)
**Confidence:** independently-corroborated

### Practice: Make input schemas strict, not just described
**Do:** Use JSON Schema constraints — `enum`, `required`, length/regex limits,
`additionalProperties: false` — to make invalid tool calls structurally impossible rather than
relying on prose in the description to steer the model. The MCP spec recommends
`{"type":"object","additionalProperties":false}` for tools that take no parameters, specifically
so extra/hallucinated fields are rejected rather than silently accepted. OpenAI's function-calling
API exposes a `strict: true` flag for exactly this purpose; Anthropic has an equivalent "strict
tool use" option (Part 1).
**Why (beginner):** A schema is the actual contract the model is held to — vague free-text
constraints ("please only use valid dates") get ignored far more often than a schema that
structurally can't accept an invalid date.
**Caveat / contested:** Schemas that are too narrow cause the model to miss valid use cases it
should be able to handle; this is a tuning problem you have to iterate on with real evals, not a
one-shot fix. Strict-mode flags and exact schema syntax differ per vendor and are 🕒 verify live.
**Sources:** [modelcontextprotocol.io — server/tools specification](https://modelcontextprotocol.io/specification/2026-07-28/server/tools) (28 Jul 2026) · [developers.openai.com/api/docs/guides/function-calling](https://developers.openai.com/api/docs/guides/function-calling) (fetched 09 Aug 2026, undated page) · [machinelearningmastery.com — "AI Agent Tool Design: What Works and What Doesn't"](https://machinelearningmastery.com/ai-agent-tool-design-what-works-and-what-doesnt/) (15 Jun 2026) · [platform.claude.com/docs — Strict tool use](https://platform.claude.com/docs/en/agents-and-tools/tool-use/strict-tool-use) (fetched 9 Aug 2026)
**Confidence:** independently-corroborated

### Practice: Use MCP when you want the same tools to work across multiple model vendors
**Do:** Expose tools through the Model Context Protocol (MCP) — an open, JSON-RPC (a lightweight
remote-procedure-call format encoded as JSON) based protocol with a `tools/list` / `tools/call`
interface — instead of hand-writing separate integrations per vendor SDK. MCP has been adopted
beyond its originator: Google Cloud announced official MCP support across Google/Google Cloud
services (Google Maps, BigQuery, GCE, GKE) in December 2025, describing MCP as having "quickly
become a common standard to connect AI models with data and tools." Anthropic's Claude API has a
built-in [MCP connector](https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview)
that lets you connect to remote MCP servers directly from the Messages API without a separate MCP
client.
**Why (beginner):** Without a shared protocol, every tool you build has to be re-wired for every
model vendor's own function-calling format. MCP lets one server implementation ("here's how to
search our ticket system") be reused by any MCP-compatible client, regardless of which underlying
model is driving the agent.
**Caveat / contested:** MCP standardizes *how tools are listed and called*, not what a given model
does with the results — you still get vendor-specific behavior differences in when/how a model
chooses to call a tool. The spec itself changes quickly: the 28 Jul 2026 revision made the
protocol core stateless (removing the `initialize`/`initialized` session handshake) and, per that
same revision, deprecated Roots/Sampling/Logging (12-month migration window) and moved the
`tools/call` method identifier out of the JSON body into an `Mcp-Method` HTTP header — a client
written against the pre-2026-07-28 wire format will break under the new routing. Pin a specific
protocol version rather than assuming "latest" behavior. 🕒 verify live. ⚠ PENDING — we could not
independently confirm OpenAI's own MCP adoption (Agents SDK / Responses API / ChatGPT desktop) by
fetching an OpenAI source this run; dropped from this practice rather than asserted without a
citation. ⚠ #openai-mcp-adoption-source
**Sources:** [modelcontextprotocol.io/specification/2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28) (28 Jul 2026) · [blog.modelcontextprotocol.io — 2026-07-28 release post](https://blog.modelcontextprotocol.io/posts/2026-07-28/) (28 Jul 2026) · [cloud.google.com/blog — Announcing official MCP support for Google services](https://cloud.google.com/blog/products/ai-machine-learning/announcing-official-mcp-support-for-google-services) (11 Dec 2025) · [platform.claude.com/docs — Tool use overview](https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview) (fetched 09 Aug 2026)
**Confidence:** independently-corroborated

### Practice: Don't treat tool names, descriptions, or annotations as a security boundary
**Do:** The MCP spec is explicit: clients "MUST consider tool annotations to be untrusted unless
they come from trusted servers" — hints like "this tool is read-only" or "this tool is
destructive" are metadata the tool author supplies, not something the protocol verifies. Design
your client/host so that a malicious or compromised server can't get more trust than its metadata
deserves: review tool descriptions before connecting, and don't let annotation flags alone gate
what actually gets allowed to run.
**Why (beginner):** A malicious MCP server (or a compromised legitimate one) can write a tool
description that *claims* to be safe, or can hide instructions inside a description that only the
model — not the user — ever reads. This is the basis of documented "tool poisoning" attacks (see
"Treat tool output as untrusted input" below, which covers this in depth).
**Caveat / contested:** This is a protocol-level warning, not a solved problem — the spec tells
implementors what to distrust, but enforcement is entirely up to the client/host application. Many
current agent deployments are reported to give external and internal tools equal privilege by
default, though we couldn't pin an exact empirical figure to a fetched source this run — treat
that as a design risk to guard against, not a cited statistic.
**Sources:** [modelcontextprotocol.io — server/tools specification](https://modelcontextprotocol.io/specification/2026-07-28/server/tools) (28 Jul 2026) · [owasp.org — MCP Tool Poisoning](https://owasp.org/www-community/attacks/MCP_Tool_Poisoning) (fetched 09 Aug 2026, undated page)
**Confidence:** independently-corroborated

### Practice: Separate "the request was malformed" errors from "the operation failed" errors, and make the latter actionable
**Do:** MCP distinguishes **protocol errors** (unknown tool, malformed request — returned as a
JSON-RPC error, and the spec notes models are "less likely to be able to" self-correct from these)
from **tool execution errors** (bad input value, business-logic failure — returned in the tool
result with `isError: true`, specifically so the model can read the message and retry with
corrected arguments). LangChain's current tool docs describe the equivalent pattern at the
framework level: wrap tool calls (e.g. with `@wrap_tool_call` middleware) to catch exceptions and
convert them into a `ToolMessage` the model can read and react to, rather than letting the agent
loop crash. Structure execution-error payloads with a machine-readable code plus fields like "is
this recoverable" and "what should be tried next," not just a raw stack trace.
**Why (beginner):** If an agent only sees "Error: 500," it has no way to decide whether to retry,
ask the user, or give up — a plain-English, structured error ("date must be in the future; you
passed 2024-01-01") lets the model actually fix its own mistake on the next turn.
**Caveat / contested:** None of these sources describe a standard retry-count or backoff policy
for tool calls — that's left to the application, and an ungoverned retry loop on a "recoverable"
error is exactly how tool-call loops (see below) start.
**Sources:** [modelcontextprotocol.io — server/tools specification](https://modelcontextprotocol.io/specification/2026-07-28/server/tools) (28 Jul 2026) · [docs.langchain.com/oss/python/langchain/tools](https://docs.langchain.com/oss/python/langchain/tools) (fetched 09 Aug 2026, undated page) · [machinelearningmastery.com — "AI Agent Tool Design: What Works and What Doesn't"](https://machinelearningmastery.com/ai-agent-tool-design-what-works-and-what-doesnt/) (15 Jun 2026)
**Confidence:** independently-corroborated

### Practice: ⚠️ WARNING — make side-effecting tools idempotent
**Do:** For any tool that changes state (charges money, sends a message, books something), attach
an idempotency key derived from stable inputs (e.g. session ID + tool name + a hash of the
arguments) before the first attempt, and reuse the *same* key on every retry of that same logical
action. Have the receiving system return the original result for a repeated key instead of
re-running the side effect.
**Why (beginner):** LLM agents retry — because of network blips, because the model "isn't sure"
the first call worked, or because of a tool-call loop — and a non-idempotent "charge card" or
"send email" tool will duplicate the action every time that happens. This is the single most
common way an AI agent costs someone real money by accident: think of a payment tool retried
twice by an agent and a customer's card getting charged twice for one order.
**Caveat / contested:** Both sources describing this pattern are single-author technical blogs
rather than a formal spec or vendor doc — the general idea (idempotency keys) is a well-established
distributed-systems pattern, but there's no cross-vendor standard for how an *agent framework*
should generate or store these keys, so implementations vary.
**Sources:** [machinelearningmastery.com — "AI Agent Tool Design: What Works and What Doesn't"](https://machinelearningmastery.com/ai-agent-tool-design-what-works-and-what-doesnt/) (15 Jun 2026) · [dev.to/mukundakatta — "Make Your Agent's API Calls Idempotent Before You Need To"](https://dev.to/mukundakatta/make-your-agents-api-calls-idempotent-before-you-need-to-2994) (page shows "Posted: May 25," year not displayed on the page; fetched 09 Aug 2026)
**Confidence:** independently-corroborated

### Practice: Require human confirmation before sensitive or destructive tool calls
**Do:** Don't let the model be the only check before an irreversible action runs. At the protocol
level, MCP says there "SHOULD always be a human in the loop with the ability to deny tool
invocations," and that applications should show confirmation prompts before sensitive operations
execute. At the framework level, LangChain's human-in-the-loop middleware lets you mark specific
tools as requiring a pause: the agent stops, and a human can **approve**, **edit** the arguments,
**reject** with feedback, or **respond** directly, before the tool actually runs (conditional
interrupts require `langchain>=1.3.3`). OWASP's LLM Top 10 lists this as a direct mitigation for
"Excessive Agency": require human approval for high-impact actions rather than letting autonomy
scale with tool power.
**Why (beginner):** ⚠️ **WARNING** — an agent that can delete records, send real messages, or run
arbitrary shell commands without a confirmation step will eventually do one of those things by
mistake (or because of a prompt-injected instruction — see below), and there's no undo button once
the action has run against the real world.
**Caveat / contested:** "Human in the loop" only helps if the human actually reads what they're
approving; a confirmation dialog that people click through without reading provides much weaker
protection than the pattern implies, and none of these sources measure how often that happens in
practice.
**Sources:** [modelcontextprotocol.io — server/tools specification](https://modelcontextprotocol.io/specification/2026-07-28/server/tools) (28 Jul 2026) · [docs.langchain.com/oss/python/langchain/human-in-the-loop](https://docs.langchain.com/oss/python/langchain/human-in-the-loop) (fetched 09 Aug 2026, undated page) · [github.com/OWASP — LLM06 Excessive Agency](https://github.com/OWASP/www-project-top-10-for-large-language-model-applications/blob/main/2_0_vulns/LLM06_ExcessiveAgency.md) (OWASP Top 10 for LLM Applications v2.0)
**Confidence:** independently-corroborated

### Practice: ⚠️ WARNING — give tools the least privilege that gets the job done, not a raw shell or a whole API
**Do:** Replace open-ended tools (a generic shell-command runner, a raw "fetch any URL" tool, a
database credential with full read/write) with narrow, purpose-built ones (a specific query
function, a scoped read-only credential). OWASP frames this as avoiding all three root causes of
"Excessive Agency" at once: excessive *functionality* (the tool can do more than the task needs),
excessive *permissions* (the credential behind the tool is broader than the tool needs), and
excessive *autonomy* (high-impact actions proceed without any check). Use short-lived, scoped
credentials (e.g. OAuth tokens with minimal scope) per tool rather than one shared, long-lived
admin credential.
**Why (beginner):** If a model is manipulated (by a bad prompt, a prompt-injected tool result, or
its own mistake) into misusing a tool, the *blast radius* of that mistake is exactly however much
that tool's underlying credential is allowed to do. A "run any shell command as root" tool turns
any agent mistake into a full system compromise; a narrowly scoped tool limits the damage to that
one function.
**Caveat / contested:** Least privilege adds real engineering work (you need a purpose-built
endpoint or scoped credential per tool, not just one API key), and teams under time pressure
frequently skip it — none of these sources have data on how common that shortcut is in
production.
**Sources:** [github.com/OWASP — LLM06 Excessive Agency](https://github.com/OWASP/www-project-top-10-for-large-language-model-applications/blob/main/2_0_vulns/LLM06_ExcessiveAgency.md) (OWASP Top 10 for LLM Applications v2.0) · [northflank.com/blog/how-to-sandbox-ai-agents](https://northflank.com/blog/how-to-sandbox-ai-agents) (02 Feb 2026)
**Confidence:** independently-corroborated

### Practice: ⚠️ WARNING — sandbox any tool that executes code or shell commands
**Do:** Run code-execution or shell-execution tools inside an isolated environment — a container,
or stronger isolation such as gVisor (a user-space layer that intercepts system calls before they
reach the host kernel) or a microVM (Firecracker/Kata Containers) for untrusted or user-influenced
code — not directly on the host that runs your agent process. Block outbound network access by
default and allowlist only what the tool actually needs; don't give the sandbox network access to
your production systems. **At minimum**, if the full infrastructure above feels out of reach: run
the tool in a plain container with no network access and a disposable, non-root user, and never
run generated code directly on your own machine or a real account — that alone stops most
accidental damage even without gVisor or a microVM.
**Why (beginner):** A "run this code" or "run this shell command" tool is, by definition, giving
the model the ability to execute arbitrary code. If that runs directly on your machine (or your
server) with no isolation, a bad model output, a prompt-injection attack, or a plain bug in
generated code can read your files, exfiltrate credentials, or damage the host — this is one of
the most common "cost real money / break the machine" beginner mistakes in agent tooling.
**Caveat / contested:** Both independent sources here are companies that sell sandboxing
infrastructure (Northflank, Modal), so their comparisons of isolation technologies have a
commercial angle — treat their specific product rankings skeptically even though the underlying
principle (isolate untrusted execution, default-deny network) is sound and echoed by OWASP's
least-privilege guidance above.
**Sources:** [northflank.com/blog/how-to-sandbox-ai-agents](https://northflank.com/blog/how-to-sandbox-ai-agents) (02 Feb 2026) · [modal.com/resources/best-code-execution-sandboxes-ai-agents](https://modal.com/resources/best-code-execution-sandboxes-ai-agents) (May 2026)
**Confidence:** independently-corroborated

### Practice: Treat tool output as untrusted input, not as trusted instructions
**Do:** Anything a tool returns — a web page, a file, an API response, another MCP server's
result — should be handled as untrusted data before it re-enters the model's context, especially
if the agent also has access to private data and some way to communicate externally. The MCP spec
requires servers to "sanitize tool outputs" and recommends clients "validate tool results before
passing to LLM." This is the mechanism behind documented "MCP tool poisoning" attacks, where a
malicious server embeds hidden instructions inside a tool's description or its *response* —
invisible to the user, but read and potentially obeyed by the model — to exfiltrate data or
hijack the agent's next actions. This isn't a 2025-only concern: Microsoft published research on
30 Jun 2026 (about six weeks before this snapshot) demonstrating exactly this mechanism — hidden
instructions embedded in tool *descriptions* causing an agent's otherwise-legitimate,
already-approved tool calls to exfiltrate data.
**Why (beginner):** Security researcher Simon Willison named the general shape of this risk the
"lethal trifecta": an agent that has (1) access to private data, (2) exposure to content from an
untrusted source, and (3) a way to communicate externally, can be tricked by a single piece of
poisoned content into leaking your data — with no traditional software bug involved. A tool's
output counts as "untrusted content" the same as a webpage or email would.
**Caveat / contested:** Willison is explicit that mitigations claiming to catch "95% of attacks"
are not good enough for this risk — the only fully reliable defense is not combining all three
conditions (private data + untrusted content + external communication) in one agent at all.
Vendor mitigations (schema validation, allowlisting servers, isolating high-privilege tools)
reduce but don't eliminate the risk.
**Sources:** [simonwillison.net — The lethal trifecta for AI agents](https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/) (16 Jun 2025) · [invariantlabs.ai — MCP security notification: tool poisoning attacks](https://invariantlabs.ai/blog/mcp-security-notification-tool-poisoning-attacks) (01 Apr 2025) · [owasp.org — MCP Tool Poisoning](https://owasp.org/www-community/attacks/MCP_Tool_Poisoning) (fetched 09 Aug 2026, undated page) · [modelcontextprotocol.io — server/tools specification](https://modelcontextprotocol.io/specification/2026-07-28/server/tools) (28 Jul 2026) · [thehackernews.com — Microsoft warns of poisoned MCP tool descriptions](https://thehackernews.com/2026/06/microsoft-warns-poisoned-mcp-tool.html) (published 30 Jun 2026)
**Confidence:** independently-corroborated

### Practice: Cap tool-call iterations and give tools clear terminal states, to stop infinite tool-call loops
**Do:** Set a hard ceiling on how many tool-call/reasoning steps a single agent run can take, and
fail gracefully (return to the user or escalate) once it's hit, rather than letting the loop run
unbounded. LangGraph implements this as a `recursion_limit` on graph execution, raising a
`GraphRecursionError` once the step budget is exhausted — the documentation frames this explicitly
as loop protection, most often triggered by "an infinite loop caused by code that creates cycles
between nodes" with no stop condition. Separately, make sure tools return unambiguous terminal
states (e.g. explicit `SUCCESS`/`FAILED`) rather than vague messages — one documented case cut an
agent from 14 tool calls down to 2 just by replacing ambiguous feedback with a clear terminal
signal.
**Why (beginner):** Agents can and do get stuck calling the same tool with the same arguments over
and over when a tool's result is ambiguous or an error is unclear — this silently burns tokens
(and API cost) without producing an answer, and won't necessarily look like a "crash" from the
outside. 🕒 verify live: exact default iteration limits differ by framework and version and are
worth checking against current docs before relying on them.
**Caveat / contested:** We could not confirm the exact default numeric value of LangGraph's
`recursion_limit` directly from the current official docs page fetched this run (widely reported
elsewhere as 25, but that figure was not independently re-verified against the primary docs page
this pass) — treat any specific number you see as unverified until you check the current
SDK/docs yourself. ⚠ PENDING (#verify-langgraph-default-recursion-limit)
**Sources:** [docs.langchain.com/oss/python/langgraph/errors/GRAPH_RECURSION_LIMIT](https://docs.langchain.com/oss/python/langgraph/errors/GRAPH_RECURSION_LIMIT) (fetched 09 Aug 2026, undated page) · [dev.to/aws — "Why AI Agents Fail: 3 Failure Modes That Cost You Tokens and Time"](https://dev.to/aws/why-ai-agents-fail-3-failure-modes-that-cost-you-tokens-and-time-1flb) (24 Mar 2025)
**Confidence:** independently-corroborated

### Practice: Don't assume one tool schema works unmodified across vendors
**Do:** If you're calling more than one model vendor's API directly (rather than going through MCP
or a framework abstraction), expect the tool-definition format and the tool-call response format
to differ and plan a translation layer. As of the docs fetched this run: OpenAI's function tools
use a `parameters` field and return call arguments as a **JSON string** you must parse yourself
(a string of text formatted like JSON, not a ready-to-use object); Anthropic's tools use an
`input_schema` field and return the call's `input` as an **already-parsed object**.
Cross-provider frameworks (LangChain, LiteLLM, Vercel AI SDK) exist specifically to normalize
these differences — but even they still need a per-vendor adapter under the hood, so
"provider-agnostic" doesn't mean "zero differences to worry about" if you're debugging at the wire
level. ⚠ PENDING — this snapshot could not independently confirm the specific claim that Google's
Gemini function declarations use protocol-buffer-derived type names rather than plain JSON Schema
keywords; dropped from this practice rather than asserted without a fetched Google source. ⚠
#gemini-function-schema-format
**Why (beginner):** Code that parses tool-call arguments as a JSON string (correct for OpenAI)
will break if you point the same code at Anthropic's API and get an object back instead — this is
a common source of "works with one model, breaks when we switch providers" bugs.
**Caveat / contested:** These exact field names and behaviors are 🕒 **verify live** —
function-calling APIs are actively evolving (e.g. Anthropic's "strict tool use" and OpenAI's
`strict: true` are recent additions), so re-check current docs before hardcoding assumptions from
this entry.
**Sources:** [developers.openai.com/api/docs/guides/function-calling](https://developers.openai.com/api/docs/guides/function-calling) (fetched 09 Aug 2026, undated page) · [platform.claude.com/docs — Tool use overview](https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview) (fetched 09 Aug 2026, undated page)
**Confidence:** independently-corroborated

---

## Held pending fixes (not publish-ready)
- Anthropic's advisor tool, Claude Managed Agents, and memory tool are live tool-use surface areas
  not yet given their own practices in this snapshot. ⚠ #tool-use-advisor-and-managed-agents
- OpenAI's own MCP adoption (Agents SDK / Responses API / ChatGPT desktop) could not be confirmed
  against a fetched OpenAI source this run. ⚠ #openai-mcp-adoption-source
- Google Gemini's function-declaration schema format (protobuf-derived type names) could not be
  confirmed against a fetched Google source this run. ⚠ #gemini-function-schema-format
- LangGraph's `recursion_limit` default (widely reported as 25) was not independently confirmed
  against LangGraph's primary docs page this run. ⚠ #verify-langgraph-default-recursion-limit
- Custom tools / context-free-grammar (Lark/regex CFG) constrained-output on OpenAI's API was
  surfaced by the vendor doc fetch but not independently corroborated this run (niche, low
  practitioner-blog coverage) — omitted as a standalone practice.
- Legacy Chat Completions `functions`/`function_call` params (pre-`tools`/`tool_choice`)
  deprecation status: described as deprecated on multiple community/GitHub threads, but not listed
  explicitly on the current official OpenAI deprecations page fetched this run — left out rather
  than asserted from forum threads alone.
- No cross-vendor formal standard for tool-call retry/backoff policy exists — noted as a gap, not
  asserted as a best practice that doesn't exist yet.
- The OWASP Top 10 for LLM Applications v2.0's exact publish date was not independently confirmed
  from a dated OWASP page this run; cited without an over-specific date.

## CHANGELOG (grading → this entry)
1. **[KILL, fixed]** OpenAI "handle rate limits" practice cited a 404'd URL
   (`.../api/docs/error-codes`); corrected to the live `.../api/docs/guides/error-codes` path,
   verified the claim still holds on the corrected page.
2. **[KILL, fixed]** OpenAI "flat schemas" practice attributed a quote to nwos.com
   ("easier for the model to reason about") that a targeted re-fetch confirmed does not appear in
   that article. Removed the fabricated quote and the standalone practice; merged the verifiable
   remainder (hard structural limits, flatness as a practical heuristic) into the strict-mode
   practice, sourced only to OpenAI's own structured-outputs page.
3. **[KILL, fixed]** OpenAI "validate arguments" practice attributed ID-existence/authorization
   checks to nwos.com; a targeted re-fetch confirmed the article doesn't address this. Removed the
   attribution and downgraded the practice's confidence from independently-corroborated to
   vendor-documented (its remaining source is OpenAI's own SDK docs quoted on OpenAI's own forum —
   one publisher, not two).
4. **[FIX]** OpenAI Responses-API practice claimed "the API will error" on dropped reasoning
   items — unsupported by the cited page (a "common mistake," not a documented API error). Removed
   the unsupported clause; also moved the `encrypted_content` citation to the page that actually
   describes it.
5. **[FIX]** OpenAI Responses-vs-Chat-Completions practice overstated "defaults to strict mode" —
   corrected to OpenAI's actual wording ("attempts to normalize... when possible, falling back to
   non-strict").
6. **[FIX]** Reconciled a direct contradiction between the Anthropic draft ("consolidate into
   fewer tools with an `action` parameter") and the generic draft ("give each tool a single job,"
   citing Anthropic as support). Anthropic's own docs support consolidation, not the generic
   draft's position — removed the incorrect Anthropic citation from the generic practice,
   downgraded its confidence to `contested`, and added explicit cross-references so both
   practices disclose the live disagreement instead of silently contradicting each other.
7. **[FIX]** Generic MCP practice: fixed a citation whose link text and href pointed at different
   pages (added the correct MCP connector reference); removed an uncited claim about OpenAI's MCP
   adoption (moved to Held pending fixes rather than asserted without a source).
8. **[FIX]** Generic "least privilege" practice cited machinelearningmastery.com for a claim that
   source doesn't actually support; removed that citation, kept the two sources (OWASP, Northflank)
   that do support it.
9. **[FIX]** Generic "don't assume one schema works across vendors" practice asserted a Gemini
   protobuf-schema detail with no supporting citation; removed the specific claim and moved it to
   Held pending fixes rather than publishing it unsourced.
10. **[FIX]** Added the 2026-07-28 MCP spec revision's deprecation of Roots/Sampling/Logging and
    its move of `tools/call` routing into an `Mcp-Method` header — a completeness gap the
    Timekeeper review caught that directly affects the "don't assume one schema works" and MCP
    practices.
11. **[FIX]** Added Microsoft's 30 Jun 2026 MCP tool-description-poisoning research to the
    tool-output-injection practice — a materially more recent, on-topic disclosure the original
    draft was missing (it only cited 2025-dated sources).
12. **[FIX]** Softened an unverified/likely-wrong Anthropic claim ("tool_choice forcing
    unsupported entirely on Claude Mythos Preview") to a general caution to verify model-specific
    support live, after Timekeeper found the live Thinking docs suggest the opposite general rule
    and no Mythos-Preview-specific carve-out could be confirmed.
13. **[FIX]** Corrected a model-tier misattribution: the "missing required parameters" practice
    said Haiku-class models are the ones that guess missing values; Anthropic's docs actually
    contrast Opus (asks) vs. Sonnet (may guess), with Haiku only a secondary aside. Rewrote to
    match the source.
14. **[FIX]** Clarified that the prompt-caching automatic 5-minute breakpoint for server-tool
    results only applies once a request already uses caching at all — the original phrasing
    ("regardless of what TTL you set elsewhere") dropped that precondition.
15. **[FIX]** Corrected the tool-search-tool request field names — `tool_search_tool_regex` /
    `tool_search_tool_bm25` are the tool names, not the versioned `type` values
    (`_regex_20251119` / `_bm25_20251119`) a request actually needs; using the unversioned name as
    `type` returns a 400.
16. **[FIX]** Trimmed "deleting data" from the computer-use precautions list (not in Anthropic's
    cited source) and re-labeled it explicitly as a reasonable extrapolation, not a quoted vendor
    example.
17. **[FIX]** Scoped the OpenAI strict-mode caching/zero-data-retention caveat to the fine-tuned
    multi-function context where OpenAI's docs actually place it, rather than presenting it as a
    general strict-mode property.
18. **[FIX]** Softened "independent measurement shows" tool-catalog-size accuracy claim to "one
    independent write-up reports," since the cited source itself summarizes rather than measures.
19. **[FIX]** Softened the o3/o4-mini `parallel_tool_calls`-rejection claim to note it rests on one
    independent blog, not confirmed against OpenAI's own docs this run.
20. **[FIX, Beginner KILL]** The OpenAI Responses-vs-Chat-Completions practice named code
    interpreter and computer use as reasons to prefer Responses with zero safety warning anywhere
    in that draft. Added an explicit ⚠️ WARNING paragraph (sandboxing, credential isolation, human
    confirmation) and cross-referenced it from the tool-output-injection practice, matching the
    safety framing already present for Claude's equivalent tools.
21. **[FIX, Beginner]** Defined JSON Schema, MCP, JSON-RPC, and OWASP on first use (previously
    used undefined in at least one part each) so each Part can stand alone for a technically
    comfortable but not API-specialist reader.
22. **[FIX, Beginner]** Added an explicit billed-API-call warning to the schema-drift-testing
    practice, which recommended CI tests against the real API with no cost caveat.
23. **[FIX, Beginner]** Added a concrete, beginner-actionable minimum sandboxing baseline ("a
    plain container, no network, non-root user") alongside the advanced options (gVisor,
    Firecracker/Kata) in the sandboxing practice, so the warning has an actionable floor, not just
    named advanced tooling.
24. **[FIX, Beginner]** Applied the ⚠️ WARNING icon consistently to cost-risk and safety-risk
    callouts that had the right content but were missing the icon (tool-definition cache-busting,
    tool-use token overhead, idempotency/duplicate-charge risk, least-privilege blast radius).
25. **[FLAG]** Noted the Assistants API's 26 Aug 2026 sunset date lands only ~2 weeks after this
    snapshot's "as of" date — called out explicitly as something to recheck rather than left as a
    routine 🕒 tag.
26. **[FLAG]** Anchored the Responses-API reasoning-item practice to "the current GPT-5.6-series
    flagship models" instead of only generic "GPT-5-class" language, closing a completeness gap
    the Timekeeper review found (the draft never named the actual current model family).
