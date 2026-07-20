---
title: "AI Agent Orchestration — Anthropic/Claude — Beginner Guide (as of 20 Jul 2026)"
date: 2026-07-20
snapshot_date: 2026-07-20
topic: ai-agent-orchestration-anthropic-claude
track: beginner
audience: "people new to AI"
description: "Plain-language guide to running Claude agents safely: how to avoid runaway costs, keep agents from doing too much, and understand the main building blocks — written for people new to AI and the command line."
content_type: "Best Practice"
categories: ["Claude", "Anthropic", "Agent Orchestration"]
tags: ["claude", "agents", "orchestration", "mcp", "tool-use", "prompt-caching", "computer-use", "safety"]
last_refreshed: 2026-07-20
graded_by: "RingS panel (Skeptic/Beginner/Timekeeper) + sensei, 2026-07-20"
grading_result: "1 fabrication removed; 20 corrections applied; 0 project-33 issues filed"
---

<!-- content/ai/beginner/ai-agent-orchestration-anthropic-claude/2026-07-20/index.md — IMMUTABLE snapshot.
     Re-leveled from the 2026-07-20 technical entry. Facts and URLs unchanged. -->

# AI Agent Orchestration — Anthropic/Claude (as of 20 Jul 2026)

> **Grading note.** A dated snapshot — accurate as of **20 Jul 2026**, frozen here and kept as
> a permanent archive entry. Research-drafted by a pupil, graded by the 3-lens panel + sensei.
> Corrections applied inline; unverifiable gaps marked ⚠ PENDING — never guessed.

---

## What this page is about

An **AI agent** is a program that uses a language model (like Claude) to plan and carry out tasks on your behalf — reading files, running searches, writing code, and more. **Orchestrating** agents means deciding how those agents are organized: who is in charge, which tools each agent is allowed to use, and how you keep costs and risks under control.

This guide covers the most important safety and design practices for anyone building with the **Claude Agent SDK** (a software toolkit from Anthropic for building Claude-powered agents). Every practice here came from Anthropic's own documentation and independently published practitioner reports — no guessing.

---

## Before you start — Prerequisites

You need these four things in place before running any agent code:

1. **An Anthropic account with an API key.** Your API key (`ANTHROPIC_API_KEY`) is the password your code uses to talk to Claude. Keep it secret — treat it like a bank PIN.
2. **The Claude Agent SDK installed.** Installation instructions are at [code.claude.com/docs/en/agent-sdk/](https://code.claude.com/docs/en/agent-sdk/). 🕒 **verify live**
3. **A spending limit set before you write a single line of agent code.** Go to console.anthropic.com → Billing → Usage Limits and set a hard monthly cap. The Agent SDK's `max_turns` and `max_budget_usd` settings both default to **no limit** — a loop with no cap can run for a very long time and generate large, real charges. See the third practice below for how to set these in code.
4. **An understanding of MTok pricing.** Pricing is stated per MTok, which means per million tokens. A token is roughly one word. A 2,000-word document is roughly 2,000 tokens. One million tokens is a lot, but agents can burn through them quickly by making many tool calls in a loop.

---

## How to read the labels
- ✅ **independently-corroborated** — 2+ independent publishers
- 📄 **vendor-documented** — official docs only (authoritative, single source)
- ⚠️ **WARNING** — a default that can cost money, break the machine, or remove a safety net
- 🕒 **verify live** — fast-moving (versions/prices/quotas); check the current value

---

## Practice: Design one "planner" agent and separate "worker" agents — keep them distinct

**Do:** Give your main Claude instance (the **orchestrator**) one job: break the overall task into pieces and hand each piece to a **subagent**. A subagent is a separate Claude instance that gets one focused task, a list of allowed tools, and nothing else. Each subagent runs in a fresh conversation of its own; only its final answer comes back to the orchestrator.

**Why (beginner):** Without this separation, one Claude instance tries to do everything and the conversation grows huge — making it harder for the model to reason clearly and more expensive with every step. Giving the orchestrator a "manager" role and subagents a "worker" role keeps things organized and predictable. Because each subagent starts with a clean slate, all the intermediate steps (file reads, searches, partial results) stay in the subagent's conversation, not the main one.

**Caveat / contested:** Spawning many subagents multiplies token cost quickly. One practitioner report (Shipyard, 2026) calls multi-agent runs "an expensive and experimental way to complete larger projects" and notes that "agents can potentially waste hours of compute doing the wrong thing." Anthropic's own engineering blog confirms that multi-agent sessions use roughly 15x more tokens than a simple chat. Use this pattern only when the task value justifies the cost.

**Sources:** [anthropic.com/engineering/multi-agent-research-system](https://www.anthropic.com/engineering/multi-agent-research-system) (fetched 2026-07-20) · [code.claude.com/docs/en/agent-sdk/subagents](https://code.claude.com/docs/en/agent-sdk/subagents) (fetched 2026-07-20) · [shipyard.build/blog/claude-code-multi-agent](https://shipyard.build/blog/claude-code-multi-agent/) (fetched 2026-07-20)

**Confidence:** ✅ independently-corroborated (Anthropic engineering + independently published Shipyard practitioner report)

---

## Practice: Give each subagent only the tools it actually needs — nothing more

**Do:** When you define a subagent, list only the tools it needs for its specific job. Some examples:

- A **documentation reviewer** only needs `Read`, `Grep`, and `Glob` (tools that look at files but cannot change them).
- A **test runner** only needs `Bash`, `Read`, and `Grep`.
- A **code modifier** needs `Read`, `Edit`, `Write`, `Grep`, and `Glob`.

Leave out any tool that the subagent has no reason to use — especially tools that can delete files, make network requests, or call external services.

**Why (beginner):** There are two reasons. First, every tool definition listed takes up space in the context window (the working memory the model uses). Listing tools the subagent will never call wastes that space. Second — and more importantly — a subagent that is not given the `Bash` tool physically cannot run shell commands, even if something tricks it into trying. Limiting tools is a safety net, not just a tidiness preference.

**Caveat / contested:** ⚠️ **WARNING:** If you omit the `tools` field entirely when defining a subagent, the subagent inherits every tool from the parent agent — the most permissive possible default. This is convenient for quick experiments but risky in any real deployment.

**Sources:** [code.claude.com/docs/en/agent-sdk/subagents](https://code.claude.com/docs/en/agent-sdk/subagents) (fetched 2026-07-20) · [platform.claude.com/docs/en/docs/build-with-claude/tool-use/overview](https://platform.claude.com/docs/en/docs/build-with-claude/tool-use/overview) (fetched 2026-07-20)

**Confidence:** 📄 vendor-documented

---

## Practice: Always set `max_turns` and `max_budget_usd` — do this first, before anything else

**Do:** When you call `query()` in the Claude Agent SDK, set two limits:

- `max_turns` — the maximum number of tool-use round trips the agent is allowed to make before stopping.
- `max_budget_usd` — the maximum amount in US dollars the session is allowed to spend before stopping.

After the call finishes, check the `ResultMessage.subtype` field in the response:

- `"success"` means the agent finished normally.
- `"error_max_turns"` means it hit the turns limit.
- `"error_max_budget_usd"` means it hit the spending limit.

Also save the `session_id` from the result — you will need it to resume a stopped session rather than starting over from scratch.

**Why (beginner):** Without these limits, an open-ended instruction like "improve this codebase" can run indefinitely, burning through tokens and accumulating API charges with no natural stopping point. These two settings are your financial circuit breaker.

**Caveat / contested:** ⚠️ **WARNING — both defaults are no limit.** An uncapped loop can run for a very long time and generate unexpected API charges. The `result` field (the agent's final text answer) only appears when `subtype` is `"success"` — always check `subtype` before trying to read it. In Python, the `total_cost_usd` and `usage` fields may be `None` on some error paths — check for `None` before formatting them.

**Sources:** [code.claude.com/docs/en/agent-sdk/agent-loop](https://code.claude.com/docs/en/agent-sdk/agent-loop) (fetched 2026-07-20)

**Confidence:** 📄 vendor-documented

---

## Practice: Put prompt-cache markers on content that stays the same across requests

**Do:** The Claude API supports **prompt caching** — a way to avoid paying full price for content that does not change between requests. You mark stable content with `"cache_control": {"type": "ephemeral"}`. Place this marker on the last block of content that stays identical across all your requests — typically your system prompt and your tool definitions. Do not place it on a timestamp, a per-request user message, or anything else that changes each time.

For agent loops where the conversation grows over time, place two markers: one on the static system prompt and one on a recent stable turn. The cache checks only the last 20 conversation blocks for a match.

**Why (beginner):** A cache hit (when the cached version is found and reused) costs 10% of the normal input token price — a 90% saving. A cache write (when the content is stored for the first time) costs 1.25x for a 5-minute TTL (TTL = time-to-live, how long the cached version is kept) or 2x for a 1-hour TTL. If you put the cache marker on content that changes every request, you pay the write cost every single time and never benefit from a hit.

**Caveat / contested:** Changing tool definitions, toggling web search, or changing extended-thinking settings all invalidate the cache — meaning the stored version is thrown away and you pay the write cost again. In agent loops, keep tool definitions constant across turns. Minimum content size to be eligible for caching: Claude Fable 5, Opus 4.8, and Sonnet 5 require at least 1,024 tokens of stable content; Claude Haiku 4.5 requires at least 4,096 tokens. 🕒 **verify live** — minimum thresholds may change with new model versions.

**Sources:** [platform.claude.com/docs/en/docs/build-with-claude/prompt-caching](https://platform.claude.com/docs/en/docs/build-with-claude/prompt-caching) (fetched 2026-07-20)

**Confidence:** 📄 vendor-documented

---

## Practice: Use subagents to keep the orchestrator's working memory lean

**Do:** Hand off long or information-heavy subtasks to subagents. Because each subagent starts with no knowledge of the parent conversation, all the intermediate steps — potentially hundreds of file reads or search queries — stay inside the subagent's own context and never reach the orchestrator. Only the subagent's final message comes back as a result. For rules you want every agent session to follow, put them in a `CLAUDE.md` file loaded via `settingSources` rather than in the starting prompt, because the starting prompt can be compressed away during long sessions.

**Why (beginner):** Claude's context window — the working memory it uses to reason — is finite. Every file read, search result, or tool output added to the main conversation shrinks the space available for future reasoning. Subagents act as separate scratch pads; the orchestrator sees a clean summary instead of every intermediate step.

**Caveat / contested:** A subagent knows only what you explicitly put in the delegation prompt you send to it. If it needs a file path, an error message, or a decision that was made earlier in the parent session, you must include that information in the prompt string. The subagent cannot look it up on its own.

**Sources:** [code.claude.com/docs/en/agent-sdk/agent-loop](https://code.claude.com/docs/en/agent-sdk/agent-loop) (fetched 2026-07-20) · [anthropic.com/engineering/multi-agent-research-system](https://www.anthropic.com/engineering/multi-agent-research-system) (fetched 2026-07-20)

**Confidence:** 📄 vendor-documented (both sources are Anthropic-owned properties)

---

## Practice: Add human approval steps for risky actions — do not auto-approve everything

**Do:** Use a three-layer approval system built into the Claude Agent SDK:

1. A `PreToolUse` hook — a function that runs before any tool call and can block it immediately. Use this for hard rules that should never be broken regardless of context (for example: never write to a folder that contains secrets).
2. A `canUseTool` callback — a function that pauses the agent and asks a human "do you approve this action?" for high-risk operations such as running a shell command, writing a file, or calling an external service.
3. A `PostToolUse` hook — a function that runs after a tool call, useful for keeping an audit log of what the agent did.

For low-risk, read-only tools (`Read`, `Grep`, `Glob`), auto-approve to avoid interrupting yourself constantly.

🕒 **verify live** — the stability status (generally available vs. preview) of `PreToolUse`/`canUseTool`/`PostToolUse` was not confirmed at grading time.

**Why (beginner):** Anthropic's autonomy research (measuring-agent-autonomy, fetched 2026-07-20) found that auto-approval rates rose from 20% to over 40% as users gained experience, while experienced users simultaneously interrupted agents more often — a counterintuitive finding suggesting users get better at spotting genuine risks over time. Blanket approval defeats the purpose of having a gate; targeted approval on genuinely risky operations keeps humans meaningfully in the loop.

**Caveat / contested:** Anthropic's research also concludes that "oversight requirements that prescribe specific interaction patterns, such as requiring humans to approve every action, will create friction without necessarily producing safety benefits." The right level of interruption depends on the risk profile of your specific deployment.

⚠️ **WARNING:** Setting `permissionMode: "bypassPermissions"` skips the `canUseTool` callback entirely. **Reserve it for CI pipelines and isolated containers only** (for example, a Docker container with no host mounts, no network access to production, and ephemeral storage that is discarded after the run). Never use it on a machine where the agent's actions could affect systems you care about. On Unix, it cannot be used when running as root.

**Sources:** [anthropic.com/research/measuring-agent-autonomy](https://www.anthropic.com/research/measuring-agent-autonomy) (fetched 2026-07-20) · [nerdleveltech.com/human-in-the-loop-claude-agent-sdk-typescript-tutorial](https://nerdleveltech.com/human-in-the-loop-claude-agent-sdk-typescript-tutorial) (fetched 2026-07-20) · [code.claude.com/docs/en/agent-sdk/agent-loop](https://code.claude.com/docs/en/agent-sdk/agent-loop) (fetched 2026-07-20)

**Confidence:** ✅ independently-corroborated (nerdleveltech.com is independently published; Anthropic sources confirm the hook architecture)

---

## Practice: Choose the right Claude model for each role — smarter models for planning, faster models for repetitive work

**Do:** As of July 2026, Anthropic offers several Claude models. Use a more capable model for your orchestrator (where planning quality matters most) and a faster, cheaper model for high-volume subagents doing focused, repetitive work. In the Claude Agent SDK, set `model` in each `AgentDefinition` to choose a different model per subagent.

**Default path — start here:**

- **Orchestrator (the planner):** Use `claude-fable-5` (described as "next-generation intelligence for long-running agents") or `claude-opus-4-8` (for "complex agentic coding and enterprise work").
- **Subagents (the workers):** Use `claude-sonnet-5` or `claude-haiku-4-5` for focused, repetitive tasks.

**Pricing** 🕒 **verify live** (as of 20 Jul 2026, per MTok = per million tokens):

| Model | Input price | Output price |
|---|---|---|
| Claude Fable 5 | $10 / MTok | $50 / MTok |
| Claude Opus 4.8 | $5 / MTok | $25 / MTok |
| Claude Sonnet 5 | $2 / MTok (introductory, rises to $3 on 2026-09-01) | $10 / MTok (rises to $15 on 2026-09-01) |
| Claude Haiku 4.5 | $1 / MTok | $5 / MTok |

Note: Claude Haiku 4.5 has a 200,000-token context window (the others have 1 million). It supports Extended Thinking (the `budget_tokens` parameter) but not Adaptive Thinking — check the documentation before using it on tasks requiring long context or adaptive reasoning.

⚠️ **Note:** `claude-opus-4-1` is deprecated and **retires 2026-08-05** (16 days from this grading date). If you are using Opus 4.1, migrate to Opus 4.8 before that date. Additionally, **fast mode for Claude Opus 4.7 retires 2026-07-24** (4 days from grading date) — any reader actively using Opus 4.7 in fast mode must switch before then. `claude-mythos-5` exists at the same capability tier as Fable 5 but is invitation-only (Project Glasswing) and not available through the standard API.

**Sources:** [platform.claude.com/docs/en/about-claude/models/overview](https://platform.claude.com/docs/en/about-claude/models/overview) (fetched 2026-07-20) · [code.claude.com/docs/en/agent-sdk/subagents](https://code.claude.com/docs/en/agent-sdk/subagents) (fetched 2026-07-20)

**Confidence:** 📄 vendor-documented

---

## Practice: Use MCP servers to connect Claude to external services — understand what ZDR does and does not cover

**Do:** MCP stands for **Model Context Protocol** — a standard way to give Claude access to external tools and services (databases, browsers, third-party APIs) that someone else has already packaged. You connect these via the MCP connector (`mcp_servers` array in the Messages API, using the beta header `mcp-client-2025-11-20`). Use `mcp_toolset` in your `tools` array to control which specific MCP tools Claude is allowed to call for a given request.

For logic that only your own application needs and that you will execute yourself, define tools directly with `input_schema` in the `tools` array instead — this is simpler when you own the code that runs the tool. When connecting MCP servers that expose many tools, add `defer_loading: true` to the toolset so Claude only loads a tool's full definition when it needs it, rather than loading all definitions upfront on every request.

**Why (beginner):** MCP saves you from writing custom connectors for every service. Direct tool definitions are simpler when you own and run the logic yourself.

**Caveat / contested:** The MCP connector currently supports Streamable HTTP and SSE transports only — there is no support for local stdio, meaning MCP servers that run only on your local machine (not over a network) are not supported. It is available on the Claude API, Claude Platform on AWS, and Microsoft Foundry (requires "Hosted on Anthropic" deployment type on Foundry) but **not** on Amazon Bedrock or Google Cloud.

⚠️ **WARNING — ZDR:** MCP connector data is not covered by zero-data-retention (ZDR) arrangements. ZDR means Anthropic does not store your prompts or outputs. If you are connecting an MCP server to a database containing personal or confidential data, understand that ZDR protections do not apply to that data flow. 🕒 **verify live** — platform availability and ZDR scope may change.

⚠️ **WARNING:** Without `defer_loading`, every MCP server's full tool schema list is included in every API request. A few servers with many tools can consume thousands of tokens before the agent does any work.

**Sources:** [platform.claude.com/docs/en/docs/agents-and-tools/mcp-connector](https://platform.claude.com/docs/en/docs/agents-and-tools/mcp-connector) (fetched 2026-07-20) · [code.claude.com/docs/en/agent-sdk/agent-loop](https://code.claude.com/docs/en/agent-sdk/agent-loop) (fetched 2026-07-20)

**Confidence:** 📄 vendor-documented

---

## Practice: Run computer use only inside a sandboxed VM or container — never on your main machine

**Do:** Computer use (beta) is a feature that gives Claude screenshot, mouse, and keyboard control of a desktop environment — it can literally click buttons and type. This is powerful and risky.

Always deploy computer use inside a dedicated **virtual machine (VM) or container** — a sandboxed environment. A sandboxed environment is a fully isolated computing environment: even if something goes wrong, the agent cannot reach your main system's files, credentials, or other applications. A Docker container with no host volume mounts and restricted network access is the minimum for development; a fully isolated cloud VM is recommended for production.

Specifically:
- Never pass login credentials, API keys, or sensitive files into the computer use environment.
- Limit outbound internet access to an allowlist of specific domains.
- Wire a human confirmation step for any action with real-world consequences (making a purchase, sending an email, submitting a form).

**API headers** — computer use requires a specific beta header in your API call, and the header depends on which model you are using (as of 20 Jul 2026):

- Use `computer-use-2025-11-24` for: Claude Fable 5, Opus 4.8, Opus 4.7, Opus 4.6, Sonnet 5, Sonnet 4.6, Opus 4.5.
- Use `computer-use-2025-01-24` (older header) for: Claude Sonnet 4.5, Haiku 4.5, and deprecated models.

Using the wrong header for your model will produce an API error. 🕒 **verify live** — header requirements may change as the feature exits beta.

**Why (beginner):** When Claude browses the web, it can encounter malicious pages that attempt **prompt injection** — instructions hidden in a webpage's text that try to override your system prompt and make Claude do something you did not authorize. Anthropic has added a classifier that detects injections in screenshots and asks for user confirmation, but Anthropic warns explicitly: "these precautions remain important even with the classifier defense layer in place." Running in a sandbox limits the damage if an injection succeeds.

**Caveat / contested:** Computer use is still in beta as of the fetch date. The classifier-based prompt-injection defence can be opted out of by contacting Anthropic support — only do this if you have a fully non-interactive pipeline where human confirmation is architecturally impossible and you have compensating controls.

⚠️ **WARNING:** Running computer use outside a sandboxed environment, or providing it access to credentials, dramatically increases the risk of unintended or malicious actions. Inform end users of the risks and obtain consent before enabling computer use in a product.

**Sources:** [platform.claude.com/docs/en/docs/build-with-claude/computer-use](https://platform.claude.com/docs/en/docs/build-with-claude/computer-use) (fetched 2026-07-20)

**Confidence:** 📄 vendor-documented

---

## Practice: Save checkpoints as you go so a failure does not lose all your work

**Do:** For long agent runs, do not rely on a single uninterrupted session. Instead:

1. Save a **checkpoint** (a record of the agent's progress) after each major phase completes — for example, after each research phase.
2. If a tool call fails, include the error message in the tool result so Claude can see what went wrong and try a different approach, rather than stopping entirely.
3. If a session stops — whether from hitting `max_turns`, a tool error, or a network problem — use the `session_id` from the `ResultMessage` to **resume** the session rather than starting from scratch.

**Why (beginner):** Agent sessions that span many tool calls are expensive to restart. If a web search tool fails on turn 47 of a 60-turn research session, you want Claude to adapt and try something else, not lose all 47 turns of progress. Checkpointing turns a catastrophic failure into a recoverable interruption. Note: checkpointing requires explicit implementation in your code — it does not happen automatically.

**Caveat / contested:** Session resumption restores the full conversation context from before the failure. If the failure was caused by bad information that accumulated in the context — for example, a hallucinated file path (an invented file path that does not exist on disk) being carried forward and confusing later steps — then resuming may reproduce the same problem. In those cases, resuming from the most recent valid checkpoint is safer than restoring the full context.

**Sources:** [anthropic.com/engineering/multi-agent-research-system](https://www.anthropic.com/engineering/multi-agent-research-system) (fetched 2026-07-20) · [anthropic.com/engineering/managed-agents](https://www.anthropic.com/engineering/managed-agents) (fetched 2026-07-20) · [code.claude.com/docs/en/agent-sdk/agent-loop](https://code.claude.com/docs/en/agent-sdk/agent-loop) (fetched 2026-07-20)

**Confidence:** 📄 vendor-documented (all three sources are Anthropic-owned properties)

---

## Held pending fixes (not publish-ready)

- Computer use page fetched via redirect chain; content confirmed valid but redirect URL should be verified by link-check gate before publish. ⚠ #pending-1
- Sonnet 5 introductory pricing expires 2026-09-01 (actual flip-over date confirmed as Sept 1 from the pricing page expiry note); snapshot will show stale pricing after that date — a new snapshot should be published after 2026-09-01. ⚠ #pending-2
- `PreToolUse`/`canUseTool`/`PostToolUse` hook stability tier (GA vs preview) — not confirmed live this grading run. ⚠ #pending-3

## CHANGELOG

Re-leveled from the 2026-07-20 technical entry by rings-beginner-author; facts and URLs unchanged.

1. `track` changed from `best-practices` to `beginner`; `audience` changed to `"people new to AI"`.
2. Added a plain-English "What this page is about" section explaining what an AI agent and orchestration mean.
3. Prerequisites section retained from the technical entry; expanded with plain-English explanations (API key defined as "password", MTok explained as words-to-tokens).
4. All eight practices retained — none dropped as too advanced. Each was simplified and expanded as follows:
   - Practice 1 (planner/worker split): renamed heading to plain English; "orchestrator" and "subagent" defined on first use.
   - Practice 2 (tool scoping): restructured with concrete per-role examples in bullet form; ⚠️ WARNING retained verbatim.
   - Practice 3 (max_turns/max_budget_usd): promoted as "do this first"; step-by-step explanation of `subtype` field added; ⚠️ WARNING retained verbatim.
   - Practice 4 (prompt caching): "cache hit", "cache write", and "TTL" defined inline; ⚠️ implications of misplacement expanded.
   - Practice 5 (clean context windows): "context window" defined as "working memory"; delegation-prompt caveat retained verbatim.
   - Practice 6 (human oversight): three-layer system explained step by step; `bypassPermissions` ⚠️ WARNING retained verbatim; Docker example retained from technical entry.
   - Practice 7 (model selection): one default path (Fable 5 / Opus 4.8 for orchestrator, Sonnet 5 / Haiku 4.5 for subagents) leading, pricing table added for readability; all ⚠️ retirement notices retained verbatim.
   - Practice 8 (MCP connector): MCP acronym expanded and explained; ZDR ⚠️ WARNING retained verbatim; defer_loading ⚠️ WARNING retained verbatim.
   - Practice 9 (computer use): "sandboxed environment" defined inline; prompt injection defined inline; both ⚠️ WARNINGs retained verbatim; beta header table retained from technical entry.
   - Practice 10 (checkpoint recovery): "checkpoint" defined; "hallucinated file path" defined inline; ⚠️ caveat retained verbatim.
5. All `**Sources:**` lines and `**Confidence:**` labels reused verbatim from the technical entry.
6. All 🕒 **verify live** flags retained.
