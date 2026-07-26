# AI Agent Orchestration — Anthropic/Claude — Best Practices (as of 20 Jul 2026)

> Concrete, sourced best practices for orchestrating Claude agents: role design, tool scoping, context management, prompt caching, human oversight, model selection, MCP integration, and computer use.


<!-- content/ai/best-practices/ai-agent-orchestration-anthropic-claude/2026-07-20/index.md — IMMUTABLE snapshot.
     Source tiers: independently-corroborated = 2+ DIFFERENT publishers; vendor-documented = official vendor docs only. -->

# AI Agent Orchestration — Anthropic/Claude (as of 20 Jul 2026)

> **Grading note.** A dated snapshot — accurate as of **20 Jul 2026**, frozen here and kept as
> a permanent archive entry. Research-drafted by a pupil, graded by the 3-lens panel + sensei.
> Corrections applied inline; unverifiable gaps marked ⚠ PENDING — never guessed.

## Prerequisites

- An Anthropic account with an API key (`ANTHROPIC_API_KEY`).
- The Claude Agent SDK installed: see [code.claude.com/docs/en/agent-sdk/](https://code.claude.com/docs/en/agent-sdk/) for installation instructions. 🕒 **verify live**
- **Set a spending limit before running any agent code.** Go to console.anthropic.com → Billing → Usage Limits and set a hard monthly cap. The Agent SDK's `max_turns` and `max_budget_usd` defaults are **no limit** — an uncapped loop can generate large charges.
- Understand MTok pricing: pricing is stated per MTok = per million tokens. For context, a 2,000-word document is roughly 2,000 tokens.

## How to read the labels
- ✅ **independently-corroborated** — 2+ independent publishers
- 📄 **vendor-documented** — official docs only (authoritative, single source)
- ⚠️ **WARNING** — a default that can cost money, break the machine, or remove a safety net
- 🕒 **verify live** — fast-moving (versions/prices/quotas); check the current value

---

## Practice: Design the orchestrator as the planner and subagents as isolated executors

**Do:** Give your lead Claude instance the job of decomposing the task, writing detailed task descriptions, and delegating each piece to a subagent via the `Agent` tool. Each subagent should receive a self-contained objective, expected output format, tool list, and clear boundaries. Subagents run in fresh context windows; only their final reply returns to the orchestrator.

**Why (beginner):** Without a clear division of labour, agents duplicate searches, leave gaps, or misinterpret vague instructions. Keeping the orchestrator focused on strategy and subagents focused on execution prevents this. Because each subagent starts with a clean context, the orchestrator's context window does not accumulate every intermediate tool call — it only grows by the final summary.

**Caveat / contested:** Spawning many subagents multiplies token cost fast. One practitioner report (Shipyard, 2026) warns that multi-agent runs are "an expensive and experimental way to complete larger projects" and notes that "agents can potentially waste hours of compute doing the wrong thing." Anthropic's own engineering blog confirms that multi-agent sessions use roughly 15× more tokens than a simple chat. Only apply this pattern when the task value justifies the cost.

**Sources:** [anthropic.com/engineering/multi-agent-research-system](https://www.anthropic.com/engineering/multi-agent-research-system) (fetched 2026-07-20) · [code.claude.com/docs/en/agent-sdk/subagents](https://code.claude.com/docs/en/agent-sdk/subagents) (fetched 2026-07-20) · [shipyard.build/blog/claude-code-multi-agent](https://shipyard.build/blog/claude-code-multi-agent/) (fetched 2026-07-20)

**Confidence:** ✅ independently-corroborated (Anthropic engineering + independently published Shipyard practitioner report)

---

## Practice: Scope each subagent's tool set to the minimum it needs

**Do:** In the `AgentDefinition` (SDK) or subagent file, list only the tools the subagent requires. A documentation reviewer only needs `Read`, `Grep`, and `Glob`. A test runner needs `Bash`, `Read`, and `Grep`. A code modifier needs `Read`, `Edit`, `Write`, `Grep`, and `Glob`. Leave destructive or external-service tools off subagents that have no business using them.

**Why (beginner):** Tool definitions consume context tokens on every request. Giving a subagent tools it will never use wastes tokens and makes it harder for Claude to choose the right tool. More importantly, a subagent that cannot call `Bash` cannot accidentally delete a file or make a network request even if it is tricked by a prompt injection.

**Caveat / contested:** ⚠️ **WARNING:** If you omit the `tools` field entirely, the subagent inherits every tool from the parent — the most permissive default. This is convenient for exploration but risky in production.

**Sources:** [code.claude.com/docs/en/agent-sdk/subagents](https://code.claude.com/docs/en/agent-sdk/subagents) (fetched 2026-07-20) · [platform.claude.com/docs/en/docs/build-with-claude/tool-use/overview](https://platform.claude.com/docs/en/docs/build-with-claude/tool-use/overview) (fetched 2026-07-20)

**Confidence:** 📄 vendor-documented

---

## Practice: Always set `max_turns` and `max_budget_usd` limits on production agent loops

**Do:** **Set these before writing any other agent logic.** When calling `query()` in the Claude Agent SDK, set `max_turns` (maximum tool-use round trips) and `max_budget_usd` (maximum spend in US dollars before the loop stops). Check the `ResultMessage.subtype` field: `"success"` means normal completion; `"error_max_turns"` or `"error_max_budget_usd"` means a limit was hit. Capture `session_id` from the result so you can resume rather than restart.

**Why (beginner):** Without limits, an open-ended prompt like "improve this codebase" can run indefinitely — accumulating tokens and cost until something external stops it.

**Caveat / contested:** ⚠️ **WARNING — both defaults are no limit.** An uncapped loop can run for a very long time and generate unexpected API charges. The `result` field (the final text output) is only present on `"success"` — always check `subtype` before reading it. On Python, `total_cost_usd` and `usage` may be `None` on some error paths — guard before formatting.

**Sources:** [code.claude.com/docs/en/agent-sdk/agent-loop](https://code.claude.com/docs/en/agent-sdk/agent-loop) (fetched 2026-07-20)

**Confidence:** 📄 vendor-documented

---

## Practice: Place prompt-cache breakpoints on stable content, not on content that changes per request

**Do:** Add `"cache_control": {"type": "ephemeral"}` to the last block of content that stays identical across requests — typically the system prompt and tool definitions. Do not put the breakpoint on a timestamp, a per-request user message, or any other dynamic content. For agentic loops where conversation history grows, add multiple breakpoints: one on the static system prompt and one on a recent stable turn, because the cache's lookback window checks only the last 20 blocks for a hit.

**Why (beginner):** A cache hit costs 0.1× the normal input token price (a 90% saving). A write costs 1.25× for a 5-minute TTL (time-to-live: how long the cached version persists) or 2× for a 1-hour TTL. Misplacing the breakpoint on changing content means you pay write cost every request and never benefit from a hit.

**Caveat / contested:** Changing tool definitions, toggling web search, or changing extended-thinking settings all invalidate the cache. In agentic loops with tool use, keep tool definitions constant across turns. Minimum cacheable size varies by model: Claude Fable 5, Opus 4.8, and Sonnet 5 require 1,024 tokens; Claude Haiku 4.5 requires 4,096 tokens. 🕒 **verify live** — minimum thresholds may change with new model versions.

**Sources:** [platform.claude.com/docs/en/docs/build-with-claude/prompt-caching](https://platform.claude.com/docs/en/docs/build-with-claude/prompt-caching) (fetched 2026-07-20)

**Confidence:** 📄 vendor-documented

---

## Practice: Use subagents with clean context windows to keep the orchestrator's context lean

**Do:** Offload long-running or information-heavy subtasks to subagents. Because each subagent starts with no parent conversation history, its intermediate tool calls — potentially hundreds of file reads or search queries — stay in its own context and are not visible to the orchestrator. Only the subagent's final message returns as a tool result. For persistent agent rules, put them in `CLAUDE.md` loaded via `settingSources`, not in the initial prompt, because the initial prompt may be compacted away.

**Why (beginner):** Claude's context window is finite. Every file read, search result, and tool output added to the main conversation eats into the space available for future reasoning. Using subagents for subtasks means the orchestrator sees a concise summary rather than the full transcript.

**Caveat / contested:** The only information a subagent receives from the parent is what you put in the Agent tool's prompt string. If a subagent needs a file path, error message, or decision made earlier in the parent session, you must explicitly include it in the delegation prompt.

**Sources:** [code.claude.com/docs/en/agent-sdk/agent-loop](https://code.claude.com/docs/en/agent-sdk/agent-loop) (fetched 2026-07-20) · [anthropic.com/engineering/multi-agent-research-system](https://www.anthropic.com/engineering/multi-agent-research-system) (fetched 2026-07-20)

**Confidence:** 📄 vendor-documented (both sources are Anthropic-owned properties)

---

## Practice: Wire human oversight through `PreToolUse` hooks and `canUseTool` callbacks, not blanket auto-approval

**Do:** Implement a three-layer permission system. First, a `PreToolUse` hook for deterministic hard blocks (for example, deny any write to a secrets path, regardless of permission mode). Second, a `canUseTool` callback that surfaces proposed tool calls to a human for interactive decisions on high-risk operations (Bash execution, file writes, external service calls). Third, a `PostToolUse` hook for audit logging. Auto-approve read-only tools (`Read`, `Grep`, `Glob`) to reduce approval fatigue. 🕒 **verify live** — `PreToolUse`/`canUseTool`/`PostToolUse` stability tier (GA vs preview) not confirmed this grading run.

**Why (beginner):** Anthropic's autonomy research (measuring-agent-autonomy, fetched 2026-07-20) found that auto-approval rates rose from 20% to over 40% as users gained experience, while experienced users simultaneously interrupted agents more often — a counterintuitive finding suggesting users get better at spotting genuine risks over time. Blanket approval defeats the purpose of having a gate; targeted approval on genuinely risky operations keeps humans meaningfully in the loop.

**Caveat / contested:** Anthropic's research also concludes that "oversight requirements that prescribe specific interaction patterns, such as requiring humans to approve every action, will create friction without necessarily producing safety benefits." The right level of interruption depends on the risk profile of your specific deployment.

⚠️ **WARNING:** Setting `permissionMode: "bypassPermissions"` skips the `canUseTool` callback entirely. **Reserve it for CI pipelines and isolated containers only** (for example, a Docker container with no host mounts, no network access to production, and ephemeral storage that is discarded after the run). Never use it on a machine where the agent's actions could affect systems you care about. On Unix, it cannot be used when running as root.

**Sources:** [anthropic.com/research/measuring-agent-autonomy](https://www.anthropic.com/research/measuring-agent-autonomy) (fetched 2026-07-20) · [nerdleveltech.com/human-in-the-loop-claude-agent-sdk-typescript-tutorial](https://nerdleveltech.com/human-in-the-loop-claude-agent-sdk-typescript-tutorial) (fetched 2026-07-20) · [code.claude.com/docs/en/agent-sdk/agent-loop](https://code.claude.com/docs/en/agent-sdk/agent-loop) (fetched 2026-07-20)

**Confidence:** ✅ independently-corroborated (nerdleveltech.com is independently published; Anthropic sources confirm the hook architecture)

---

## Practice: Select models by role — Opus or Fable for complex orchestration, Sonnet/Haiku for routine subagent work

**Do:** As of July 2026, use `claude-fable-5` ("next-generation intelligence for long-running agents") or `claude-opus-4-8` ("complex agentic coding and enterprise work") for your orchestrator, where planning quality matters most. Use `claude-sonnet-5` or `claude-haiku-4-5` for high-volume subagents doing focused, repetitive work. In the Claude Agent SDK, set `model` in each `AgentDefinition` to override per subagent.

🕒 **verify live** — current pricing as of 20 Jul 2026: Claude Fable 5 at $10/$50 per MTok input/output; Claude Opus 4.8 at $5/$25; Claude Sonnet 5 currently $2/$10 per MTok (introductory pricing), rising to $3/$15 on 2026-09-01; Claude Haiku 4.5 at $1/$5. Haiku 4.5 has a 200k-token context window (vs 1M for others) and supports Extended Thinking (the `budget_tokens` parameter) but not Adaptive Thinking — verify before using it on tasks requiring long context or adaptive reasoning.

⚠️ **Note:** `claude-opus-4-1` is deprecated and **retires 2026-08-05** (16 days from this grading date). If you are using Opus 4.1, migrate to Opus 4.8 before that date. Additionally, **fast mode for Claude Opus 4.7 retires 2026-07-24** (4 days from grading date) — any reader actively using Opus 4.7 in fast mode must switch before then. `claude-mythos-5` exists at the same capability tier as Fable 5 but is invitation-only (Project Glasswing) and not available through the standard API.

**Sources:** [platform.claude.com/docs/en/about-claude/models/overview](https://platform.claude.com/docs/en/about-claude/models/overview) (fetched 2026-07-20) · [code.claude.com/docs/en/agent-sdk/subagents](https://code.claude.com/docs/en/agent-sdk/subagents) (fetched 2026-07-20)

**Confidence:** 📄 vendor-documented

---

## Practice: Use MCP servers for reusable external-service integrations; use direct tool definitions for task-specific logic

**Do:** Connect Claude to databases, browsers, or third-party APIs via the MCP connector (`mcp_servers` array in the Messages API, beta header `mcp-client-2025-11-20`). Use an `mcp_toolset` entry in the `tools` array to allowlist or denylist individual MCP tools per request. For logic that only your application needs and that you will execute yourself, define tools directly with `input_schema` in the `tools` array instead. When exposing many MCP tools, set `defer_loading: true` on the toolset so Claude loads tool schemas on demand rather than bloating every request with all schemas upfront.

**Why (beginner):** MCP gives you a standard protocol for connecting Claude to services someone else has already packaged. Direct tool definitions are simpler when you own the execution.

**Caveat / contested:** The MCP connector currently supports Streamable HTTP and SSE transports (no local stdio — meaning no MCP servers running only on your local machine). It is available on the Claude API, Claude Platform on AWS, and Microsoft Foundry (requires "Hosted on Anthropic" deployment type on Foundry) but **not** on Amazon Bedrock or Google Cloud.

⚠️ **WARNING — ZDR:** MCP connector data is not covered by zero-data-retention (ZDR) arrangements. ZDR means Anthropic does not store your prompts or outputs. If you are connecting an MCP server to a database containing personal or confidential data, understand that ZDR protections do not apply to that data flow. 🕒 **verify live** — platform availability and ZDR scope may change.

⚠️ **WARNING:** Without `defer_loading`, every MCP server's full tool schema list is included in every API request. A few servers with many tools can consume thousands of tokens before the agent does any work.

**Sources:** [platform.claude.com/docs/en/docs/agents-and-tools/mcp-connector](https://platform.claude.com/docs/en/docs/agents-and-tools/mcp-connector) (fetched 2026-07-20) · [code.claude.com/docs/en/agent-sdk/agent-loop](https://code.claude.com/docs/en/agent-sdk/agent-loop) (fetched 2026-07-20)

**Confidence:** 📄 vendor-documented

---

## Practice: Run computer use in a dedicated VM or container with minimal privileges, allowlisted network, and human confirmation for consequential actions

**Do:** Computer use (beta) gives Claude screenshot, mouse, and keyboard control of a desktop environment. Always deploy it inside a dedicated virtual machine (VM) or container — a sandboxed environment is a fully isolated computing environment that cannot access your main system's files or credentials even if the agent is compromised. A Docker container with no host volume mounts and restricted network access is the minimum for development; a fully isolated cloud VM is recommended for production. Never pass login credentials, API keys, or sensitive files into the environment. Limit outbound internet access to an allowlist of domains. Wire a human confirmation step for any action with real-world consequences.

**Beta API header (as of 20 Jul 2026):**
- `computer-use-2025-11-24` applies to: Claude Fable 5, Opus 4.8, Opus 4.7, Opus 4.6, Sonnet 5, Sonnet 4.6, Opus 4.5.
- `computer-use-2025-01-24` (older header) applies to: Claude Sonnet 4.5, Haiku 4.5, and deprecated models.
Using the wrong header for your model will produce an API error. 🕒 **verify live** — header requirements may change as the feature exits beta.

**Why (beginner):** Claude browsing the web can encounter malicious pages that attempt prompt injection — instructions embedded in page content that try to override your system prompt. Anthropic has added a classifier that detects injections in screenshots and asks for user confirmation, but warns explicitly: "these precautions remain important even with the classifier defense layer in place." Isolation limits the blast radius if an injection succeeds.

**Caveat / contested:** Computer use is still in beta as of the fetch date. The classifier-based prompt-injection defence can be opted out of by contacting Anthropic support — only do this if you have a fully non-interactive pipeline where human confirmation is architecturally impossible and you have compensating controls.

⚠️ **WARNING:** Running computer use outside a sandboxed environment, or providing it access to credentials, dramatically increases the risk of unintended or malicious actions. Inform end users of the risks and obtain consent before enabling computer use in a product.

**Sources:** [platform.claude.com/docs/en/docs/build-with-claude/computer-use](https://platform.claude.com/docs/en/docs/build-with-claude/computer-use) (fetched 2026-07-20)

**Confidence:** 📄 vendor-documented

---

## Practice: Implement graceful degradation and checkpoint-based recovery rather than full restarts on agentic loop failures

**Do:** In long agentic runs, combine Claude's adaptability with deterministic safeguards: implement retry logic around tool calls, checkpoint state at phase boundaries (for example, after each research phase completes), and — if a tool is persistently failing — surface the error to Claude in the tool result so it can adapt its approach. Use `session_id` from `ResultMessage` to resume a failed session rather than starting over.

**Why (beginner):** Agent sessions that span many tool calls are expensive to restart. If a web search tool fails on turn 47 of a 60-turn research session, you want Claude to try an alternative, not lose all progress. Checkpointing and resumption turn catastrophic failures into recoverable interruptions. Note: checkpointing requires explicit implementation — it does not happen automatically.

**Caveat / contested:** Session resumption restores the full context from previous turns. If the failure was caused by bad state accumulated in the context (for example, a hallucinated file path — an invented path that does not exist — being carried forward), resuming may reproduce the problem. In those cases a selective restart — resuming from the most recent valid checkpoint — is safer than full context restoration.

**Sources:** [anthropic.com/engineering/multi-agent-research-system](https://www.anthropic.com/engineering/multi-agent-research-system) (fetched 2026-07-20) · [anthropic.com/engineering/managed-agents](https://www.anthropic.com/engineering/managed-agents) (fetched 2026-07-20) · [code.claude.com/docs/en/agent-sdk/agent-loop](https://code.claude.com/docs/en/agent-sdk/agent-loop) (fetched 2026-07-20)

**Confidence:** 📄 vendor-documented (all three sources are Anthropic-owned properties)

---

## Held pending fixes (not publish-ready)

- Computer use page fetched via redirect chain; content confirmed valid but redirect URL should be verified by link-check gate before publish. ⚠ #pending-1
- Sonnet 5 introductory pricing expires 2026-09-01 (actual flip-over date confirmed as Sept 1 from the pricing page expiry note); snapshot will show stale pricing after that date — a new snapshot should be published after 2026-09-01. ⚠ #pending-2
- `PreToolUse`/`canUseTool`/`PostToolUse` hook stability tier (GA vs preview) — not confirmed live this grading run. ⚠ #pending-3

## CHANGELOG (grading → this entry)

1. **Skeptic KILL — FABRICATION REMOVED:** "users approved roughly 93% of permission prompts, and the more approvals they saw, the less attention they paid" — the 93% figure is NOT in the cited Anthropic research page (anthropic.com/research/measuring-agent-autonomy). The page reports auto-approval rising from 20% to over 40% with experience, and the actual finding about attention is nuanced (experienced users both auto-approve more AND interrupt more). The fabricated statistic and the contradicted attention-fatigue claim are removed; replaced with the actual sourced finding.
2. **Skeptic FIX:** Shipyard second quote corrected from "agents can waste hours pursuing incorrect interpretations without human oversight" to the verbatim text: "agents can potentially waste hours of compute doing the wrong thing."
3. **Skeptic FLAG:** "subagents with clean context windows" — relabeled from `independently-corroborated` to `vendor-documented` (both sources are Anthropic-owned: code.claude.com and anthropic.com).
4. **Skeptic FLAG:** "graceful degradation / checkpoint recovery" — relabeled from `independently-corroborated` to `vendor-documented` (all three sources are Anthropic-owned: anthropic.com/engineering ×2 + code.claude.com).
5. **Timekeeper KILL-A2:** Sonnet 5 pricing presentation corrected — now leads with currently operative $2/$10 through 2026-09-01, then states $3/$15 as the post-expiry standard rate.
6. **Timekeeper KILL-A3:** Computer use beta header now specifies which models use which header: `2025-11-24` for Fable 5 / Opus 4.8 / Opus 4.7 / Opus 4.6 / Sonnet 5 / Sonnet 4.6 / Opus 4.5; `2025-01-24` for Haiku 4.5 and Sonnet 4.5.
7. **Timekeeper FIX-A1:** Haiku 4.5 description clarified — supports Extended Thinking (budget_tokens), but not Adaptive Thinking.
8. **Timekeeper FIX-A2:** MCP connector transport updated to "Streamable HTTP and SSE transports" (not just "HTTP/SSE" — Streamable HTTP is now supported in addition to SSE).
9. **Timekeeper FIX-A3:** MCP connector on Microsoft Foundry now notes it requires "Hosted on Anthropic" deployment type.
10. **Timekeeper FIX-A5:** Claude Fable 5 (1,024 token minimum) added to prompt-caching minimum threshold list.
11. **Timekeeper FIX-A6:** `claude-mythos-5` noted as invitation-only (Project Glasswing) at same capability tier as Fable 5.
12. **Timekeeper FIX-A7:** Claude Opus 4.1 retirement date (2026-08-05, 16 days from grading date) added to model section.
13. **Timekeeper FLAG-A4:** Sonnet 5 introductory pricing expiry date (2026-09-01) now appears as an inline callout in the model section, not only in the held-pending footer.
14. **Timekeeper FLAG-A5:** Opus 4.7 fast mode retirement (2026-07-24, 4 days from grading date) added to model section.
15. **Beginner KILL-A1:** `max_turns` / `max_budget_usd` — setting limits now framed as the mandatory first step, not optional tuning.
16. **Beginner KILL-A2:** `bypassPermissions` — Docker container example added as the minimum sandboxed alternative a beginner can use.
17. **Beginner KILL-A3:** Computer use sandbox — "sandboxed environment" now defined (isolated computing environment that cannot access host systems); Docker example added.
18. **Beginner KILL-A4:** MCP ZDR — elevated from caveat to ⚠️ WARNING; "zero-data-retention" defined in plain English.
19. **Beginner KILL-A5:** Prerequisites section added (API key, Agent SDK install, billing cap, MTok defined).
20. **Beginner FIX-A5:** "MTok" (million tokens) defined in Prerequisites and on first use in pricing table.

