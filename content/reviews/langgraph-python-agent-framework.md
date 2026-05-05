---
title: "LangGraph — Graph-Based Stateful Agent Orchestration for Python"
date: 2026-05-06T09:30:00+09:00
description: "LangGraph reviewed: the dominant production Python agent framework. StateGraph orchestration, Supervisor+Swarm multi-agent patterns, official MCP client via langchain-mcp-adapters v0.2.2, LangSmith observability, 34.5M monthly PyPI downloads. Rating: 4.5/5."
og_description: "LangGraph (langchain-ai/langgraph, 31.2K stars, MIT, Python+TypeScript, v1.1.10) is the graph-based stateful agent framework from LangChain Inc. Models agent workflows as directed state-machine graphs — StateGraph with typed state, nodes, conditional edges, and checkpointing backed by PostgreSQL or MongoDB. Two official multi-agent packages: langgraph-supervisor (hierarchical) and langgraph-swarm-py (peer handoff). MCP client via langchain-mcp-adapters v0.2.2 (MultiServerMCPClient, stdio/HTTP/SSE/WebSocket transports, 3.5K stars); no native MCP server support. Human-in-the-loop via interrupt() breakpoints with checkpointed state resumption. LangGraph 1.0 GA October 2025. 34.5M monthly PyPI downloads — highest volume of any agent framework. LangSmith Deployment for production (cloud/hybrid/self-hosted). Rating: 4.5/5."
content_type: "Review"
card_description: "LangGraph (langchain-ai/langgraph, 31.2K stars, MIT, Python, v1.1.10) is the graph-based stateful agent framework from LangChain Inc — the dominant production choice by download volume (34.5M monthly PyPI downloads) and enterprise adoption (34% of 1,000+ employee agent architecture citations). Where CrewAI gives you roles and tasks, LangGraph gives you explicit state machines: StateGraph defines typed shared state, nodes are functions that read and write that state, edges route between nodes, and checkpointing (PostgreSQL/MongoDB-backed) makes the whole graph resumable. Multi-agent is handled by two official packages: langgraph-supervisor for hierarchical routing and langgraph-swarm-py for peer-to-peer handoffs. MCP client support is official via langchain-mcp-adapters v0.2.2 (MultiServerMCPClient, stdio/HTTP/SSE/WebSocket). MCP server support — exposing LangGraph agents as MCP endpoints — is not natively available; competitors Agno and Mastra offer this out of the box. Human-in-the-loop is a first-class feature via interrupt() breakpoints that pause, checkpoint, and resume graph execution after human review. LangGraph 1.0 GA was declared October 22, 2025. LangGraph.js (TypeScript) exists but is less mature. Production deployment via LangSmith Deployment (formerly LangGraph Platform): cloud, hybrid, or fully self-hosted. Part of our **Developer Tools** category. Rating: 4.5/5."
last_refreshed: 2026-05-06
categories: ["/categories/developer-tools/"]
---

If you've been building Python AI agents since 2023, you've encountered LangChain. LangGraph is what LangChain built next — and it solves a different problem. LangChain gives you components: LLM interfaces, prompt templates, retrieval pipelines, tool-calling patterns. LangGraph gives you the graph: a stateful, inspectable, resumable execution model for workflows too complex to express as a linear chain.

Part of our **[Developer Tools category](/categories/developer-tools/)**.

---

## At a Glance

| | |
|---|---|
| **Repo** | [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) |
| **Stars** | ~31,200 |
| **Forks** | ~5,300 |
| **License** | MIT |
| **Language** | Python (3.9+), TypeScript (LangGraph.js, less mature) |
| **Version** | v1.1.10 (April 27, 2026) |
| **Next** | v1.2.0a7 alpha (May 4, 2026) |
| **GA date** | LangGraph 1.0: October 22, 2025 |
| **Install** | `pip install langgraph` |
| **Downloads** | 34.5M monthly PyPI downloads |
| **Maintainer** | LangChain Inc. |

---

## What It Does

LangGraph models agent workflows as **directed state-machine graphs**. The central abstraction is the `StateGraph`: you define a typed state schema (a Python `TypedDict`), then build a graph of nodes and edges over that state. Every node is a function that receives the current state and returns updates; edges route between nodes, either unconditionally or conditionally based on state values. The graph engine (inspired by Google's Pregel) runs the workflow superstep by superstep, checkpointing state between steps.

This is deliberately different from role-based frameworks like CrewAI, where you describe what agents *are* (role, goal, backstory) and the framework decides execution order. In LangGraph, you describe what agents *do* and how they connect. That extra control is also extra work — LangGraph is more boilerplate than CrewAI for simple use cases, and more powerful for complex ones.

---

## Core Abstractions

### StateGraph

The entry point for any LangGraph application. You define a typed state schema — a `TypedDict` or Pydantic model — that represents all working memory for the agent workflow. Nodes read from this state and return partial updates; the graph merges those updates according to reducer functions you define (append to a list, override a value, merge a dict).

```python
from typing import TypedDict, Annotated
from langgraph.graph import StateGraph, END
from langgraph.graph.message import add_messages

class State(TypedDict):
    messages: Annotated[list, add_messages]
    next_step: str

graph = StateGraph(State)
```

### Nodes

A node is any Python callable that takes `State` and returns a dict of updates. Nodes can call LLMs, invoke tools, run arbitrary logic, or call sub-graphs. They can also be `async` for non-blocking I/O.

### Edges and Conditional Routing

`add_edge(A, B)` always routes from A to B. `add_conditional_edges(A, router_fn)` calls `router_fn` on the current state and routes to different nodes based on the result — the mechanism for branching logic, retry loops, and multi-agent handoffs.

### Checkpointing

Every superstep is checkpointed to a persistent backend. Supported backends:
- **PostgreSQL** (recommended for production)
- **MongoDB**
- **In-memory** (development only)

Checkpointing is what enables human-in-the-loop (pause and resume), fault tolerance (resume after failure), and long-running threads (workflows spanning days or weeks). The v1.2 alpha introduces **DeltaChannel** — incremental delta storage instead of full snapshots — reducing checkpoint overhead for long-running threads.

---

## Multi-Agent Orchestration

LangGraph ships two official multi-agent packages beyond the core StateGraph primitives:

### langgraph-supervisor

Hierarchical orchestration: a **supervisor agent** receives tasks, decides which specialist sub-agent to invoke, inspects results, and decides what happens next. Sub-agents do not communicate directly — all messages route through the supervisor.

```
pip install langgraph-supervisor
```

Best for: workflows where a coordinating intelligence should own routing decisions and quality control. Higher token cost (supervisor "translates" between agents), stronger centralized control.

### langgraph-swarm-py

Peer-to-peer handoffs: agents pass control directly to each other via tool calls. The system remembers which agent is currently "active" and routes incoming messages to it. No central coordinator.

```
pip install langgraph-swarm-py
```

Best for: workflows where agents have clear specialization boundaries and the right next agent is obvious from the task state. Lower token overhead than supervisor for many tasks.

### Arbitrary Graph Topologies

Both patterns are built on the same StateGraph primitives, which you can compose freely. Sub-graphs embed as nodes within parent graphs. There is no prescribed limit on topology — supervisor hierarchies, swarm handoffs, sequential pipelines, and parallel fan-out/fan-in are all expressible.

---

## MCP Integration

### MCP Client: Yes (Official)

**Package**: `langchain-mcp-adapters`
**Version**: 0.2.2 (March 16, 2026)
**Stars**: ~3,500 (separate repo: `langchain-ai/langchain-mcp-adapters`)
**Install**: `pip install langchain-mcp-adapters`

The adapter converts MCP tool schemas into LangChain `BaseTool` objects, making them directly callable from any LangGraph node. The key class is `MultiServerMCPClient`, which manages simultaneous connections to multiple MCP servers.

**Supported transports**:
- `stdio` — subprocess-based local MCP servers
- `streamable_http` — the current MCP standard
- `sse` — Server-Sent Events (legacy support)
- `websocket`

**Authentication**: Custom headers are supported for SSE and HTTP transports, enabling API keys, OAuth tokens, and tracing headers at the transport level.

### MCP Server: No Native Support

LangGraph agents cannot expose themselves as MCP endpoints without additional tooling. The adapter documentation demonstrates using **FastMCP** as a separate layer to create MCP servers, but this is external to LangGraph itself.

This is the sharpest contrast with **Agno** and **Mastra**, both of which offer bidirectional MCP — consuming MCP servers as a client *and* exposing agents as MCP servers — natively in their open-source releases. CrewAI's MCP server capability is enterprise-only (CrewAI AMP), putting CrewAI and LangGraph roughly equivalent on this dimension.

**Practical impact**: if your goal is to make a LangGraph agent available to Claude Desktop, Cursor, or any other MCP client, you will need to write the MCP server layer yourself (e.g., via FastMCP wrapping LangGraph's HTTP endpoint) rather than getting it from the framework.

---

## Human-in-the-Loop

LangGraph's human-in-the-loop support is a first-class architectural feature, not an afterthought.

The mechanism is **interrupt breakpoints**:
- Define breakpoints before or after specific nodes via `interrupt_before` or `interrupt_after`
- When the graph reaches a breakpoint, execution pauses and the current state is checkpointed
- A human (or external system) can inspect the state, modify it, or simply approve it
- Resuming the graph (`graph.invoke(None, config={"configurable": {"thread_id": ...}})`) restores from the checkpoint and continues from the interruption point

This makes it possible to build workflows that require human approval at critical junctures — reviewing a generated document before sending, approving a code change before applying it, or confirming a financial action before executing it — with full state persistence between the pause and the resume.

LangSmith Deployment provides managed UI workflows for human-in-the-loop approval at the platform level.

---

## Streaming

LangGraph offers multiple streaming modes via `stream()` and `astream()` (async):

| Mode | What it emits |
|---|---|
| `values` | Full state after each superstep |
| `updates` | Only what changed after each node ran |
| `messages` | LLM tokens as they generate (requires LangGraph API) |
| `custom` | Arbitrary events emitted by nodes/tools |
| `events` | Fine-grained typed events via `astream_events()` |

The **v1.2 alpha** introduces Streaming API v3 — a content-block-centric protocol replacing dict events with typed per-channel projections. `ChatModelStream` provides dedicated sub-projections for text tokens and tool calls, making it significantly easier to build streaming UIs on top of LangGraph agents.

---

## The LangChain Ecosystem

LangGraph is one layer in a larger stack:

**LangChain** — foundational toolkit (LLM interfaces, chains, retrieval, tools, prompt management). LangGraph can use it but does not require it.

**LangGraph** — orchestration layer (stateful graph execution, multi-agent patterns, checkpointing).

**LangSmith** — observability (tracing, debugging, evaluation, analytics). Every LangGraph run can be automatically traced to LangSmith. The production incident data that informs LangGraph's roadmap comes from LangSmith telemetry.

**LangSmith Deployment** (formerly LangGraph Platform, renamed October 2025) — production infrastructure (1-click deploy, 30+ API endpoints, horizontal scaling, cron scheduling, webhooks, semantic memory, human-in-the-loop workflow management). Notably, LangSmith Deployment can host **any agent framework**, not just LangGraph.

**LangGraph Studio** — visual IDE for local debugging, inspecting graph structure, and iterating on state.

---

## LLM Support

LangGraph is model-agnostic. Via LangChain's 100+ model integrations (and LiteLLM as a gateway), supported providers include:

- **Anthropic** (Claude models) — first-class support
- **OpenAI** (GPT-4o, o-series)
- **Google** (Gemini)
- **AWS Bedrock** (Claude via Bedrock, Llama, Titan)
- **Azure OpenAI**
- **Groq, Cohere, HuggingFace Hub**
- **Local models** (Ollama, LlamaCPP, text-generation-webui)

Switching providers typically requires changing one config line; the graph logic is provider-agnostic.

---

## Production Deployment

**LangSmith Deployment** (the managed platform) offers:

- **Cloud (SaaS)**: fully managed; available on Plus and Enterprise plans
- **Hybrid**: SaaS control plane + self-hosted data plane; Enterprise only
- **Fully Self-Hosted**: entire platform within your own VPC; Enterprise only
- **Developer Plan**: free, up to 100K nodes/month for self-hosted infrastructure

Self-hosted infrastructure requirements: **Redis** (pub-sub for streaming) and **PostgreSQL** (required checkpointer backend). MongoDB is optional for checkpoint data.

Deployment tooling: `langgraph deploy` CLI (released March 2026, supersedes `langgraph up`). Supports Agent Registry with versioning and instant rollbacks.

---

## Limitations

**Steep learning curve.** LangGraph's explicit state machines, reducer functions, and graph compilation are significantly more complex than CrewAI's role-based DSL. Teams new to the framework commonly spend days debugging edge routing before building anything useful.

**No native MCP server.** Agents cannot be exposed as MCP endpoints without external glue (FastMCP or custom HTTP wrapping). Agno and Mastra ship this natively.

**State management complexity in production.** LangChain's own 2026 State of Agent Engineering report notes that over 60% of production agent incidents relate to state management — conflicts, persistence failures, deployment difficulties. LangGraph's power (full state control) creates responsibility (you have to manage that state correctly).

**Multi-agent debugging is hard.** Cascading failures across interconnected nodes in large multi-agent systems require distributed systems thinking to diagnose. LangSmith traces help significantly, but this is a non-trivial operational burden.

**Python-first.** LangGraph.js (TypeScript) exists and is actively maintained, but the Python version is more mature, more documented, and has a larger community. Teams building TypeScript-first applications may find Mastra a better fit.

**Self-orchestration challenge.** A University of Melbourne study (April 2026) found that frontier models given a full procedure in their system prompt — and left to self-orchestrate — consistently outperformed the same model orchestrated via LangGraph across procedural domains. The implication: LangGraph's overhead is only justified when the task genuinely requires state persistence, resumability, or explicit control flow that a single-prompt approach cannot provide.

---

## Compared to Other Frameworks

| Framework | Stars | MCP Client | MCP Server | Download Volume |
|---|---|---|---|---|
| **LangGraph** | 31.2K | Yes (official, 0.2.2) | No native | 34.5M/month (highest) |
| **CrewAI** | 50.6K | Yes (MCPServerAdapter) | Enterprise only | High |
| **Agno** | 39.8K | Yes (bidirectional) | Yes (native OSS) | Moderate |
| **Mastra** | 23.6K (TypeScript) | Yes (bidirectional) | Yes (native OSS) | ~300K npm/week |
| **AG2** | 4.5K | Yes (create_toolkit) | No | Lower |

LangGraph's 34.5 million monthly PyPI downloads and 34% enterprise architecture citation rate (Gartner, Q1 2026) reflect real production usage that star counts alone don't capture. This is the framework most large organizations have already committed to or evaluated seriously. That installed base is both its moat and its gravity — frameworks in this position tend to attract tooling, documentation, and talent that accelerates the gap.

---

## Who Should Use LangGraph

**Good fit for:**
- Teams already in the LangChain ecosystem
- Workflows requiring durable state across long execution spans
- Human-in-the-loop approval workflows
- Complex conditional branching that would be unreadable as a prompt
- Organizations needing LangSmith's observability from day one
- Multi-agent systems where fine-grained control over agent communication matters

**Better alternatives exist if:**
- You need agents to expose themselves as MCP servers (→ Agno or Mastra)
- You're building TypeScript-native (→ Mastra)
- You want rapid prototyping with a role-based DSL (→ CrewAI)
- Your workflow is simple enough for a single well-prompted agent (→ skip the framework)

---

## Rating: 4.5/5

LangGraph is the production-dominant Python agent framework. Its StateGraph model provides a level of control, inspectability, and resumability that role-based frameworks do not attempt. The LangSmith observability layer, human-in-the-loop support, and LangSmith Deployment platform give it a coherent production story from prototype to scale. MIT license. 34.5M monthly downloads. 1.0 GA declared.

The 0.5-point deduction reflects two concrete gaps: **no native MCP server support** (agents cannot be consumed as MCP endpoints without external tooling) and a **steep learning curve** that makes LangGraph a poor default for simple use cases where a single capable prompt would suffice. Agno and Mastra are ahead on MCP bidirectionality; CrewAI is ahead on time-to-prototype for role-based workflows.

For organizations building complex, stateful, production Python agents who need full control over execution flow — LangGraph is the established standard.
