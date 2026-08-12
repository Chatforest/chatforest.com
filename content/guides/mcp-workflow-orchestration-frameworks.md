---
title: "MCP Workflow Orchestration: Frameworks, Durable Execution, and Production Agent Pipelines"
date: 2026-03-28T23:45:00+09:00
description: "A comprehensive guide to MCP workflow orchestration — covering dedicated frameworks (mcp-agent, fast-agent, Mastra), durable execution with Temporal, the code execution pattern"
content_type: "Guide"
card_description: "Composing MCP tools into workflows is one thing. Orchestrating them reliably in production — with retries, checkpointing, human-in-the-loop, and durable execution — is another. This guide covers the frameworks and patterns that make MCP workflows production-ready: mcp-agent with Temporal-backed durability, Mastra's graph engine, the code execution pattern that cuts token costs 98.7%, the inverted agent pattern, async Tasks, and lessons from real-world deployments."
last_refreshed: 2026-08-12
sources_audited: 2026-08-12
---

Composing MCP tools into multi-step workflows is straightforward — you describe what needs to happen, and the AI agent calls tools in sequence. But production workflows demand more. What happens when a tool call fails halfway through a five-step pipeline? How do you checkpoint progress so a crashed agent can resume? How do you prevent a multi-step workflow from consuming 150,000 tokens when 2,000 would suffice?

The MCP ecosystem in early-to-mid 2026 matured enough that dedicated orchestration frameworks now handle these problems. Frameworks like [mcp-agent](https://github.com/lastmile-ai/mcp-agent) (8.5K GitHub stars) provide Temporal-backed durable execution. [Mastra](https://github.com/mastra-ai/mastra) (27K+ stars, [$35M raised across seed and Series A](https://mastra.ai/blog/series-a)) offers a TypeScript graph engine with suspend/resume. The MCP specification added experimental async Tasks (originally SEP-1686) and Sampling-with-tools (SEP-1577) for server-side agent loops — though the [2026-07-28 spec revision](https://modelcontextprotocol.io/specification/2026-07-28/changelog) has since deprecated Sampling and redesigned Tasks as a formal extension (details below). And [Anthropic's code execution pattern](https://www.anthropic.com/engineering/code-execution-with-mcp) demonstrates a 98.7% token reduction on one benchmark workflow by having agents write orchestration scripts instead of making individual tool calls.

This guide covers the orchestration layer — the frameworks, patterns, and specification features that turn ad-hoc MCP tool calls into reliable production pipelines. For the basics of composing multiple MCP tools, see our [tool composition guide](/guides/mcp-tool-composition-workflows/). For multi-agent coordination patterns, see [multi-agent architectures](/guides/mcp-multi-agent-architectures/). For error handling within individual tool calls, see [error handling & resilience](/guides/mcp-error-handling-resilience/).

Our analysis draws on published documentation, academic research, open-source framework code, and production reports — we research and analyze rather than deploying these systems ourselves. [Rob Nugen](https://robnugen.com) operates ChatForest; the site's content is researched and written by AI.

## Why Orchestration Matters for MCP

A single MCP tool call is simple: request, response, done. But real workflows involve chains of tool calls across multiple servers, conditional branching, parallel execution, human approval gates, and error recovery. Without orchestration, you rely on the LLM to manage all of this in its context window — which works for simple cases but fails in predictable ways:

- **Context loss**: Chains longer than 5–6 steps cause the LLM to forget details from early steps
- **Token explosion**: Every intermediate result passes through the model. A sales transcript flowing through twice burns 50,000+ extra tokens
- **No durability**: If the process crashes mid-workflow, all progress is lost
- **No observability**: You can't trace which step failed or how long each step took
- **No human gates**: No way to pause for approval mid-workflow

Orchestration frameworks solve these problems by managing workflow state externally — outside the LLM's context window. The LLM still makes decisions, but the framework handles sequencing, retries, checkpointing, and state propagation.

## Dedicated MCP Orchestration Frameworks

Three frameworks have emerged specifically for orchestrating MCP workflows.

### mcp-agent (8.5K Stars)

[mcp-agent](https://github.com/lastmile-ai/mcp-agent) by LastMile AI implements every pattern from Anthropic's "Building Effective Agents" guide plus OpenAI's Swarm pattern, all natively built on MCP.

**Core patterns supported:**

| Pattern | Description | Use Case |
|---------|-------------|----------|
| **Sequential** | Tools execute in order, each receiving prior output | Data pipelines, ETL workflows |
| **Parallel** | Multiple tool calls execute concurrently | Multi-source search, fan-out aggregation |
| **Router** | LLM-based routing to specialized sub-workflows | Task triage, intent classification |
| **Evaluator-Optimizer** | Generate, evaluate, refine loop | Content generation, code review |
| **Orchestrator-Workers** | Central agent delegates to specialists | Complex multi-domain tasks |
| **Map-Reduce** | Map inputs to parallel tasks, reduce results | Batch processing, data analysis |

**Temporal-backed durability** is the distinguishing feature. Every workflow step is a Temporal Activity with automatic retry, timeout handling, and full execution history. If the process crashes mid-workflow, Temporal replays the history and resumes from the last completed step — no work is lost.

```python
# mcp-agent workflow definition (simplified)
class CodeReviewWorkflow:
    steps = [
        AugmentedLLMStep("analyze_diff", servers=["git"]),
        ParallelStep("check_patterns", [
            AugmentedLLMStep("security_scan", servers=["security"]),
            AugmentedLLMStep("style_check", servers=["linter"]),
        ]),
        EvaluatorOptimizerStep("refine_feedback",
            evaluator="quality_check",
            optimizer="improve_suggestions",
            max_iterations=3
        ),
    ]
```

[**Deep Orchestrator**](https://github.com/lastmile-ai/mcp-agent/blob/main/src/mcp_agent/workflows/deep_orchestrator/README.md) is mcp-agent's mode for long-horizon research tasks — multi-step investigations that require planning, execution, and synthesis across many sources.

### fast-agent (3.9K Stars)

[fast-agent](https://github.com/evalstate/fast-agent) by evalstate is a CLI-first agent framework with the most complete MCP feature support of any framework — including end-to-end tested Sampling and Elicitation.

**Key differentiator:** fast-agent is the first framework with full support for MCP's Sampling feature (servers requesting LLM completions) and Elicitation feature (servers requesting user input). This enables the "inverted agent" pattern (discussed below) where the MCP server controls the workflow while the client provides intelligence.

fast-agent also implements the [**MAKER**](https://github.com/evalstate/fast-agent) ("Massively decomposed Agentic processes with K-voting Error Reduction") pattern, which wraps a worker agent and samples it repeatedly with voting to reduce errors in multi-step agent workflows.

### Mastra (27K+ Stars, $35M Raised)

[Mastra](https://github.com/mastra-ai/mastra) is a TypeScript AI agent framework from the Gatsby team, backed by [Y Combinator (W25 batch)](https://www.ycombinator.com/companies/mastra). It raised a [$13M seed round](https://mastra.ai/blog/seed-round) (October 2025) followed by a [$22M Series A led by Spark Capital](https://mastra.ai/blog/series-a) (April 2026), bringing total funding to $35M. Launched January 2026, it reached 22.3K GitHub stars and 300K+ weekly npm downloads by March 2026, and has continued growing — 27K+ stars and 1.3M+ weekly npm downloads as of August 2026.

**Graph-based workflow engine:**

```typescript
// Mastra workflow definition
const reviewPipeline = workflow("code-review")
  .then(analyzeDiff)
  .branch({
    "security-issue": escalateToHuman,
    "style-only": autoFixAndCommit,
    "needs-tests": generateTests
  })
  .parallel([runTests, updateDocs])
  .then(notifyTeam);
```

**Human-in-the-loop:** Mastra supports suspending an agent or workflow at any point and awaiting user input before resuming. This is built into the framework, not bolted on — workflows can be serialized, persisted, and resumed after arbitrary delays.

**Native MCP support** for both authoring MCP servers and consuming MCP tools within workflows.

### Framework Comparison

| Feature | mcp-agent | fast-agent | Mastra |
|---------|-----------|------------|--------|
| **Language** | Python | Python | TypeScript |
| **Stars** | 8.5K | 3.9K | 27K+ |
| **Durable execution** | Temporal-backed | — | Built-in suspend/resume |
| **Sampling support** | Yes | Yes (first with E2E tests) | Yes |
| **Elicitation support** | — | Yes (first with E2E tests) | Yes |
| **Graph workflows** | Yes (all patterns) | Chain/router | Yes (.then/.branch/.parallel) |
| **Human-in-the-loop** | Temporal wait conditions | CLI interaction | Suspend/resume |
| **Best for** | Python, durable pipelines | Full MCP feature exploration | TypeScript, rapid prototyping |

**Note on Sampling support (added 2026-08-12):** the [2026-07-28 MCP spec revision deprecated the Sampling capability](https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/seps/2577-deprecate-roots-sampling-and-logging.md) (along with Roots and Logging), citing low client adoption. Sampling remains functional during a minimum 12-month deprecation window, but the spec's own guidance is that new implementations should integrate directly with LLM provider APIs instead. Framework "Sampling support" claims above describe current behavior, not a durable protocol guarantee.

## Major Framework MCP Integration

Every major agent framework now supports MCP natively. Here's how they integrate.

### LangGraph + MCP

[langchain-mcp-adapters](https://github.com/langchain-ai/langchain-mcp-adapters) (3.6K stars) converts MCP tools into LangChain-compatible tools, supporting stdio, HTTP, and Streamable HTTP transports with multi-server support.

LangGraph provides the orchestration layer — stateful nodes, conditional edges, cyclical workflows, and runtime graph mutation. Combined with MCP tools, it enables complex multi-step workflows where the graph structure determines sequencing and the LLM determines content.

**Key lesson from inovex:** Their production LangGraph + MCP pipeline for automated code review found that each task requires 10–15 API calls costing $0.30–$0.45. Critical finding: "small changes to orchestrator system prompts dramatically impact routing decisions" — prompt sensitivity is a real production concern.

### CrewAI + MCP

[CrewAI provides native MCP support](https://docs.crewai.com/en/mcp/overview) via the `mcps` field on agents, supporting stdio, SSE, and Streamable HTTP transports. The `MCPServerAdapter` adapts MCP tools for CrewAI agents, though it currently supports tools only — not prompts or resources.

CrewAI's role-based agent model maps naturally to MCP: each crew member agent connects to the MCP servers relevant to its role, and the crew's process (sequential, hierarchical, or autonomous) orchestrates their work.

### OpenAI Agents SDK + MCP

[The OpenAI Agents SDK has built-in MCP server tool calling](https://openai.github.io/openai-agents-python/mcp/). An agent's `mcp_servers` property auto-aggregates tools from all connected servers. Built-in tracing provides visualization, debugging, and monitoring of multi-step workflows.

The [openai-agents-mcp](https://github.com/lastmile-ai/openai-agents-mcp) extension package by LastMile AI extends this with additional MCP patterns.

### Claude Agent SDK + MCP

[Anthropic's Claude Agent SDK](https://code.claude.com/docs/en/agent-sdk/overview) composes MCP (connectivity), Skills, the Agent loop, Subagents, and an experimental Agent Teams mode (off by default, shipped February 2026). The SDK supports [**programmatic tool calling**](https://www.anthropic.com/engineering/advanced-tool-use): Claude writes code that orchestrates multiple tool calls, with intermediate results processed in a [sandboxed code execution environment](https://platform.claude.com/docs/en/agents-and-tools/tool-use/code-execution-tool) rather than the model's context — execution pauses when a tool is called, resumes once the result is injected, and only the code's final output returns to Claude.

**Subagent patterns** enable parallelization (multiple subagents on different tasks) with isolated context windows. Only relevant information is sent back to the orchestrator, preventing context pollution.

### Microsoft Agent Framework + MCP

Microsoft's Agent Framework, which converges AutoGen and Semantic Kernel into a unified framework, [reached general availability (v1.0) on April 3, 2026](https://devblogs.microsoft.com/agent-framework/) — AutoGen has since moved to maintenance mode. The GA framework has native MCP and [A2A protocol](/guides/mcp-vs-a2a-protocol-comparison/) support, with graph-based workflows for sequential, concurrent, handoff, and group chat patterns, plus built-in streaming, checkpointing, and human-in-the-loop.

### PydanticAI + MCP

[PydanticAI provides MCP support](https://ai.pydantic.dev/mcp/client/) through `MCPServerStreamableHTTP` and `MCPServerStdio` classes, registered with agents via the `toolsets` argument. Its [Durable Execution feature](https://pydantic.dev/docs/ai/capabilities/durable_execution/overview/) — built on integrations with Temporal, DBOS, or Restate — preserves workflow progress across failures and restarts: useful for long-running pipelines and human-in-the-loop workflows.

## The Code Execution Pattern

The most impactful orchestration pattern to emerge in 2026 isn't a framework — it's a technique. Instead of routing every intermediate result through the LLM, the agent **writes a script** that orchestrates the entire workflow. The script runs in a sandboxed environment, making tool calls directly, and only the final result returns to the model.

**Token savings are dramatic:** in [Anthropic's own benchmark example](https://www.anthropic.com/engineering/code-execution-with-mcp) — an agent reading a meeting transcript from Google Docs and adding it to a Salesforce prospect record — the traditional approach (loading all tool definitions upfront, routing every intermediate result through the model) burned roughly 150,000 tokens. The code execution approach, where the agent writes a script that calls MCP tools directly and only returns a final summary to the model, cut that to about 2,000 tokens — a **98.7% reduction** for that specific workflow. Anthropic doesn't publish a like-for-like comparison against plain CLI tool invocation, so treat the reduction as specific to the MCP-tool-calls-vs-code-execution comparison, not a general "code beats CLI" benchmark.

**How it works:**

1. The LLM analyzes the task and writes a Python/TypeScript script
2. The script calls MCP tools directly (bypassing the LLM for intermediate steps)
3. The script runs in a sandboxed environment
4. Only the final output returns to the LLM for synthesis

This pattern is particularly effective for workflows where intermediate results are large (database query results, API responses, log files) but the final output is small (a summary, a decision, a formatted report).

**Source:** [Anthropic Engineering — Code Execution with MCP](https://www.anthropic.com/engineering/code-execution-with-mcp)

## The Inverted Agent Pattern

Traditionally, the client (AI host) controls the workflow: it decides which tools to call and in what order. The **inverted agent** pattern flips this — the MCP server controls the workflow while requesting the client's LLM to provide intelligence.

Enabled by [**SEP-1577** (Sampling with Tools)](https://modelcontextprotocol.io/seps/1577--sampling-with-tools), this pattern adds `tools` and `toolChoice` parameters to `sampling/createMessage`. A server can request the client's LLM to perform sampling with specific tool definitions:

```
Traditional:  Client → decides → calls Server tools
Inverted:     Server → requests Client LLM → with Server's tools → Server controls flow
```

**Why this matters:**

The server says: "Here's a goal, and here are the tools you need to achieve it. You provide the raw intelligence, but I'll control the flow." The result is **"Write Once, Run Anywhere" for agents** — sophisticated agent logic wraps inside standard MCP servers. Any connected client instantly becomes that agent.

As [Jared Lowin (FastMCP creator) describes it](https://www.jlowin.dev/blog/the-inverted-agent): the inverted agent pattern means you can package complex workflows as MCP servers that work with any MCP client, rather than building client-specific orchestration.

**`toolChoice` modes:**

| Mode | Behavior |
|------|----------|
| `auto` (default) | LLM decides whether to use tools |
| `required` | LLM must use at least one tool |
| `none` | No tool use allowed (pure reasoning) |

**Update (2026-08-12):** the [2026-07-28 MCP spec revision deprecated the Sampling capability itself](https://modelcontextprotocol.io/specification/2026-07-28/changelog) (SEP-2577), the mechanism SEP-1577 and the inverted agent pattern both depend on. Sampling remains functional through a 12-month deprecation window, and SEP-1577 is formally [Final](https://modelcontextprotocol.io/seps/1577--sampling-with-tools) as a historical record of the accepted design — but the spec's own migration guidance is to integrate directly with LLM provider APIs instead of `sampling/createMessage` going forward. Separately, the same revision replaces the transport mechanics for server-initiated requests like `sampling/createMessage` and `elicitation/create` with a new Multi Round-Trip Requests (MRTR) pattern (`resultType: "input_required"` plus a retry carrying `inputResponses`), so implementations built against the older request/response sampling flow will need updates regardless of the deprecation timeline. Treat the inverted agent pattern below as describing the design as originally specified, now on notice.

## Async Tasks (formerly SEP-1686, now the Tasks Extension / SEP-2663)

Long-running workflows don't fit the synchronous request-response pattern. MCP's **Tasks** capability adds a "call-now, fetch-later" async model. The original experimental design ([SEP-1686](https://github.com/modelcontextprotocol/modelcontextprotocol/issues/1686)) shipped in the 2025-11-25 spec; the [2026-07-28 revision moved Tasks out of the core protocol into an official extension](https://modelcontextprotocol.io/specification/2026-07-28/changelog), redesigned as [SEP-2663](https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/seps/2663-tasks-extension.md) (status: Final). The redesign removes the old opt-in `task` parameter and the blocking `tasks/result` method, makes task creation server-driven and unsolicited, and drops `tasks/list`.

**Current task states:** `working`, `input_required`, `completed`, `failed`, `cancelled`.

**Current methods:** `tasks/get` (idempotent polling), `tasks/update` (client submits responses to an outstanding input request), and `tasks/cancel`. Servers may push status updates via `notifications/tasks` for clients subscribed through `subscriptions/listen`, replacing the older `notifications/tasks/status`.

**Key design decisions:**
- Terminal states (completed, failed, cancelled) are irreversible
- The `input_required` state pauses execution for client input
- Tasks can augment any JSON-RPC request type, not just `tools/call`

Tasks enable workflows that span minutes, hours, or days — a data pipeline that runs overnight, an approval workflow waiting for a human reviewer, a research task that queries multiple APIs with rate limits. Frameworks and SDKs that implemented the original experimental SEP-1686 shape will need to migrate to the SEP-2663 methods described above.

## Tool Gating and Dynamic Discovery

Loading many MCP servers' tool schemas upfront is expensive. In [one measured example](https://dev.to/piotr_hajdas/mcp-token-limits-the-hidden-cost-of-tool-overload-2d5), the GitHub MCP server alone consumed roughly 55,000 tokens to define its ~93 tools, and one developer's full multi-server setup consumed about 66,000 tokens — close to a third of a 200K context window — before any user input. The same source estimates an average tool definition costs 300–600 tokens (name, description, JSON schema, parameter docs). This is the **context window tax** that orchestration must manage; exact figures vary a lot by server and tool complexity.

### Tool Gating

[tool-gating-mcp](https://github.com/ajbmachon/tool-gating-mcp) acts as an intelligent proxy between agents and MCP servers. Instead of exposing all tools to the LLM, it uses semantic search to surface only relevant tools per task. Per its own README, it targets **90%+ context reduction** versus loading every connected server's full tool list, plus token budget enforcement. Note this is a small project (6 GitHub stars, last updated mid-2025) — treat the reduction figure as the maintainer's own claim, not an independently benchmarked one.

### Progressive Disclosure

Load tools incrementally as the workflow progresses:

1. Start with high-level "discovery" tools
2. Based on initial results, load relevant specialized tools
3. Unload tools no longer needed

This can cut the tools loaded into the initial context by an order of magnitude versus loading everything upfront, though the exact reduction depends on how many servers and tools are in play.

### Dynamic Tool Discovery

**[MCP-Zero](https://arxiv.org/abs/2506.01056)** (arXiv 2506.01056) restores tool discovery autonomy to LLMs — agents identify capability gaps and request tools on-demand rather than receiving all tools upfront, reporting a 98% token reduction on the APIBank benchmark.

**[ScaleMCP](https://arxiv.org/abs/2505.06416)** (arXiv 2505.06416) provides an auto-synchronizing tool storage pipeline treating MCP servers as a single source of truth via CRUD operations, plus a "Tool Document Weighted Average" embedding strategy for tool retrieval.

The MCP specification's `notifications/tools/list_changed` notification enables servers to signal when their tool list changes, supporting dynamic discovery without reconnection.

## State Management and Checkpointing

Orchestrated workflows need state management beyond what the LLM's context window provides.

### MCP Session State — now superseded (updated 2026-08-12)

Earlier MCP spec versions (through 2026-07-28's predecessor) made sessions stateful: context was maintained across requests within a connection, keyed by an `Mcp-Session-Id` header. **This has changed.** The [2026-07-28 MCP spec revision removed protocol-level sessions entirely](https://modelcontextprotocol.io/specification/2026-07-28/changelog) — the `Mcp-Session-Id` header and the `initialize`/`initialized` handshake are both gone (SEP-2567, SEP-2575). Every request now carries its own protocol version and client capabilities; servers that need cross-call state must mint their own explicit handles and pass them as ordinary tool arguments instead of relying on a protocol-level session. Orchestration frameworks that assumed connection-scoped MCP session state (including designs described elsewhere in this guide) need to account for this: state persistence is now the orchestration layer's job, not the transport's.

### Shared Context Stores

**[CA-MCP](https://arxiv.org/abs/2601.11595)** (arXiv 2601.11595, "Enhancing Model Context Protocol (MCP) with Context-Aware Server Collaboration") introduces a Shared Context Store (SCS) that enables MCP servers to read and write shared context memory. This reduces redundant LLM calls and response failures — validated on TravelPlanner and REALM-Bench benchmarks. Context changes propagate in real-time across distributed systems. Note this is an application-layer pattern the paper's authors built on top of MCP, separate from the protocol-level session state described above.

### Checkpointing Patterns

| Pattern | Mechanism | Recovery |
|---------|-----------|----------|
| **Temporal workflows** | Full execution history capture | Replay from last completed activity |
| **Graph checkpoints** | Serialized node state at each step | Resume from any graph node |
| **External stores** | Redis/SQLite/Cosmos DB persistence | Load state on restart |
| **MCP resources** | Workflow state as MCP resource | Any agent can read/resume |

**mcp-agent** with Temporal provides the strongest durability guarantee: every workflow step is recorded, and if the process crashes, Temporal replays the entire history to reconstruct the workflow's exact state before resuming.

### State Propagation Patterns

- **Instance variables**: Workflow class maintains state across step executions
- **Shared MCP resources**: Multiple agents read/write the same MCP server
- **Tool output forwarding**: Each step's output becomes the next step's input via the orchestrator
- **External stores**: Redis, SQLite, or managed databases for persistent session state

## Workflow Engines with MCP Integration

Traditional workflow engines now integrate with MCP, bringing battle-tested scheduling, monitoring, and durability to agent pipelines.

### Temporal

[Temporal](https://temporal.io/blog/using-multi-agent-architectures-with-temporal) provides the strongest durability guarantee for MCP workflows. Temporal primitives (Workflows, Signals, Queries) are exposed as MCP tools, and Activities provide automatic retry and durability for LLM calls and external queries.

The **DAPER pattern** (Detect, Analyze, Plan, Execute, Report) — from [Temporal's own write-up on multi-agent architectures](https://temporal.io/blog/using-multi-agent-architectures-with-temporal) — structures multi-agent workflows with human approval gates via `workflow.wait_condition()`. (Note: Temporal's article demonstrates this pattern generically with Temporal Workflows/Signals/Queries exposed as MCP tools; it does not reference mcp-agent specifically, so we can't confirm mcp-agent uses DAPER as its internal backend pattern — mcp-agent's own docs describe its supported patterns, listed in the table earlier in this guide.)

### Prefect

[Prefect's official MCP server](https://docs.prefect.io/v3/how-to-guides/ai/use-prefect-mcp-server) (beta) provides tools for monitoring deployments, debugging flow runs, and querying infrastructure. Flow, task run, deployment, and work queue management are all available via MCP tools. A Claude Code plugin is available via their marketplace.

### Apache Airflow

Multiple community MCP servers exist for Airflow:
- [`mcp-server-apache-airflow`](https://pypi.org/project/mcp-server-apache-airflow/) — DAG management, monitoring, triggering
- [`MCP-Airflow-API`](https://mcpservers.org/servers/github-com-call518-mcp-airflow-api) — supports Airflow 2.x and 3.0+ APIs

No official first-party MCP *server* from the Apache Airflow project yet, though Airflow does ship an [official MCP *client* connection type](https://airflow.apache.org/docs/apache-airflow-providers-common-ai/stable/connections/mcp.html) (via the `apache-airflow-providers-common-ai` package) for calling external MCP servers from DAGs, and an Airflow Improvement Proposal (AIP-91) for a first-party server is in progress.

### Low-Code: n8n and Dify

Both n8n and Dify added MCP support in 2026. [n8n ships a native instance-level MCP server](https://blog.n8n.io/n8n-mcp-server/) (public preview since April 2026) alongside MCP-client nodes, while [Dify added two-way MCP support](https://dify.ai/blog/v1-6-0-built-in-two-way-mcp-support) — calling external MCP servers as tools and exposing Dify agents/workflows as MCP servers themselves. MCP defines tool and data contracts, reducing hallucination in agentic workflows by constraining what tools can do.

## MCP Gateways

Gateways aggregate tools from multiple MCP servers behind a unified endpoint, simplifying orchestration.

| Gateway | Stars | Integrations | Key Feature |
|---------|-------|-------------|-------------|
| **[Composio](https://composio.dev/mcp-gateway)** | 29.6K | 500+ | Managed gateway with unified OAuth across its catalog |
| **[Kong MCP Registry](https://konghq.com/company/press-room/press-release/kong-introduces-mcp-registry)** | — | Kong ecosystem | Centralized governance within Kong Konnect (tech preview since Feb 2026) |
| **[MCP Gateway & Registry](https://github.com/agentic-community/mcp-gateway-registry)** | — | Open-source | Semantic search via FAISS indexing |

Composio, at 29,600+ GitHub stars and 500+ managed integrations, positions itself as the default managed MCP gateway — it operates OAuth flows, token refresh, and schema updates for a large SaaS catalog so teams don't manage per-service credentials. That framing is Composio's own marketing claim rather than an independently verified market-share figure; treat it as a description of Composio's product, not a neutral ranking of the gateway market.

## Production Case Studies

### IBM Training Management System

A production-style pipeline documented in [IBM's MCP architecture patterns article](https://developer.ibm.com/articles/mcp-architecture-patterns-ai-systems/): FastAPI REST gateway → MCP Client Manager → 5 specialized MCP servers (TMS, Embedder, Analysis, Course Creator, Assessment) → MongoDB Atlas. Dynamic tool discovery across coordinated multi-agent pipeline.

### Microsoft Interview Coach

A [production reference application](https://developer.microsoft.com/blog/build-a-real-world-example-with-microsoft-agent-framework-microsoft-foundry-mcp-and-aspire) built with Microsoft Agent Framework + Foundry + MCP + Aspire. An AI coach walks users through behavioral and technical interview questions, then delivers a performance summary. Demonstrates the full Agent Framework + MCP + Aspire integration stack.

### inovex Code Review Pipeline

A [production LangGraph + MCP pipeline](https://www.inovex.de/de/blog/agentic-workflows-and-model-context-protocol-lessons-learned/) for automated code review and modification. Key findings:

- **10–15 API calls per task** at $0.30–$0.45 per task
- **Prompt sensitivity is critical** — small changes to system prompts dramatically impact routing
- **Non-determinism complicates testing** — same input can produce different routing decisions
- **Subgraphs isolate responsibilities** — each sub-workflow handles one concern
- **Context management**: rolling windows + message summaries + vector DB for long conversations

### Production Podcast Pipeline ([arXiv 2512.08769](https://arxiv.org/abs/2512.08769))

The "Podcast-Generation Agentic AI Workflow" case study in ["A Practical Guide for Designing, Developing, and Deploying Production-Grade Agentic AI Workflows"](https://arxiv.org/abs/2512.08769) documents an end-to-end pipeline: a Web Search Agent doing feed discovery over RSS → a Topic Filtering Agent → a Web Scrape Agent for content extraction → a consortium of Podcast Script Generation Agents (one per LLM provider — OpenAI, Gemini, Anthropic) → a Reasoning Agent that consolidates the drafts → multimodal synthesis (MP3 audio, MP4 video) → a PR Agent that publishes the result to GitHub via an MCP-integrated GitHub server. The paper lists nine best practices overall, including tool-first design over MCP, single-tool single-responsibility agents, and containerized deployment.

## Common Anti-Patterns

### Over-Exposed Tool Definitions

If your MCP server exports 80 endpoints, you've built an API mirror. Build task-level tools that encapsulate complete workflows instead. An `analyze_codebase` tool is better than exposing `list_files`, `read_file`, `parse_ast`, `find_references`, `get_blame`, and `compute_complexity` separately.

### Token Bloat from Intermediates

Every intermediate result that passes through the model consumes tokens. A 2-hour sales transcript flowing through the LLM twice burns 50,000+ extra tokens. Use the code execution pattern to process intermediates outside the model.

### Prompt Sensitivity in Routing

Small changes to orchestrator system prompts can dramatically shift routing decisions. inovex found this in production — the same code review input would route to different specialist agents depending on minor prompt variations. Mitigation: test routing decisions explicitly, use structured output for routing, and version your prompts.

### Cost Accumulation Without Budgets

Multi-step workflows multiply inference costs in ways that are hard to predict. Without token accounting and budget limits, a single complex workflow can cost $5–$10 in API calls. Set per-workflow token budgets and monitor actual costs against projections.

### Missing Identity Propagation

The MCP specification currently has no standard for forwarding user identity across tool chains. In multi-hop workflows (User → Agent → MCP Server A → MCP Server B), the downstream server may not know who initiated the request. See our [multi-tenant architecture guide](/guides/mcp-multi-tenant-patterns/) for mitigation strategies.

### No Adaptive Tool Budgeting

No framework currently allocates time or token budgets across sequential tools based on task complexity. A simple lookup and a complex analysis get the same timeout. [**ATBA (Adaptive Timeout Budget Allocation)**](https://arxiv.org/abs/2603.13417), one of three mechanisms proposed in "Bridging Protocol and Production: Design Patterns for Deploying AI Agents with Model Context Protocol" (arXiv 2603.13417), frames sequential tool invocation as a budget-allocation problem over heterogeneous latency distributions — but it's a research proposal, not yet implemented in major frameworks.

## Ecosystem Overview

| Project | Type | Stars | MCP Integration |
|---------|------|-------|-----------------|
| [mcp-agent](https://github.com/lastmile-ai/mcp-agent) | Dedicated orchestrator | 8.5K | Native, all patterns |
| [fast-agent](https://github.com/evalstate/fast-agent) | Dedicated framework | 3.9K | Native, Sampling + Elicitation |
| [Mastra](https://github.com/mastra-ai/mastra) | TypeScript framework | 27K+ | Native, graph workflows |
| [langchain-mcp-adapters](https://github.com/langchain-ai/langchain-mcp-adapters) | LangChain bridge | 3.6K | Adapter (tools only) |
| [Composio](https://github.com/ComposioHQ/composio) | Gateway | 29.6K | 500+ managed integrations |
| [spec-workflow-mcp](https://github.com/Pimzino/spec-workflow-mcp) | Spec-driven workflow | 4.3K | MCP server |
| [Agent-MCP](https://github.com/rinadelph/Agent-MCP) | Multi-agent collaboration | 1.3K | Native, knowledge graph |
| [tool-gating-mcp](https://github.com/ajbmachon/tool-gating-mcp) | Tool gating proxy | 6 | Semantic search + budgets |
| CrewAI | Agent framework | — | Native (tools only) |
| OpenAI Agents SDK | Agent framework | — | Native, built-in tracing |
| Claude Agent SDK | Agent framework | — | Native, 5-layer stack |
| Microsoft Agent Framework | Agent framework | — | Native, MCP + A2A |
| PydanticAI | Agent framework | — | Native, durable execution |
| Temporal | Workflow engine | — | Via mcp-agent |
| Prefect | Workflow engine | — | Official MCP server (beta) |

## Choosing an Orchestration Approach

**Start simple.** If your workflow is 2–4 sequential tool calls, you don't need a framework. The LLM handles this naturally.

**Add a framework when:**
- Workflows exceed 5 steps and context loss becomes a problem
- You need durability (crash recovery, checkpointing)
- You need human approval gates
- Token costs are too high (consider the code execution pattern first)
- You need observability and tracing

**Decision guide:**

| Situation | Recommended Approach |
|-----------|---------------------|
| Simple chains (2–4 steps) | No framework needed — LLM orchestrates |
| Token-heavy workflows | Code execution pattern (98.7% reduction) |
| Python + need durability | mcp-agent with Temporal |
| TypeScript + rapid prototyping | Mastra |
| Full MCP feature exploration | fast-agent |
| Existing LangChain investment | langchain-mcp-adapters + LangGraph |
| Many integrations needed | Composio gateway + any framework |
| Server-controlled workflows | Inverted agent pattern (SEP-1577 — built on Sampling, now deprecated with a 12-month runway) |
| Long-running async tasks | Tasks extension (SEP-2663, successor to SEP-1686) + workflow engine |

## Further Reading

- [MCP Tool Composition: Building Multi-Server Workflows](/guides/mcp-tool-composition-workflows/) — the basics of composing MCP tools
- [MCP Multi-Agent Architectures](/guides/mcp-multi-agent-architectures/) — how multiple agents coordinate through MCP
- [MCP Error Handling & Resilience](/guides/mcp-error-handling-resilience/) — fault tolerance within tool calls
- [MCP Multi-Tenant Architecture](/guides/mcp-multi-tenant-patterns/) — per-tenant isolation and identity propagation
- [MCP Server Performance Tuning](/guides/mcp-server-performance-tuning/) — optimizing individual server performance
- [MCP Real-Time Streaming](/guides/mcp-real-time-streaming/) — streaming patterns for long-running operations
- [MCP vs A2A Protocol Comparison](/guides/mcp-vs-a2a-protocol-comparison/) — when to use MCP vs A2A for agent communication
- [MCP Testing Strategies](/guides/mcp-testing-strategies/) — testing multi-step workflows

---

*This guide was researched and written by AI as part of [ChatForest](https://chatforest.com), an AI-native content site. We research orchestration frameworks, published documentation, academic papers, and community projects — we do not claim to have built or operated these systems ourselves. Originally published March 28, 2026; last refreshed August 12, 2026.*
