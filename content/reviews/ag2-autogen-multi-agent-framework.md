---
title: "AG2 (AutoGen) — Community-Driven Python Multi-Agent Framework"
date: 2026-05-06T08:00:00+09:00
description: "AG2 reviewed: the Apache 2.0 community fork of Microsoft's AutoGen with v0.12.2, nine multi-agent orchestration patterns, MCP client support, and a major architectural rewrite underway. Rating: 4.0/5."
og_description: "AG2 (ag2ai/ag2, Apache 2.0, Python, v0.12.2) is the actively developed community fork of Microsoft's original AutoGen framework. The original microsoft/autogen (57.7K stars, MIT) entered maintenance mode in 2026 while ag2ai/ag2 (4.5K stars) carries forward with a major Beta rewrite launched March 2026: async-first event-driven architecture, Agent Harness lifecycle management, MemoryStream pub/sub event bus, and horizontal scaling via externalized state. Nine multi-agent patterns: ConversableAgent, GroupChat (6 speaker-selection modes), Swarm, Sequential/Nested Chats. MCP client support via autogen.mcp (create_toolkit, MCPClient, stdio+SSE transports). LangChain/CrewAI/PydanticAI tool interop. RAG: ChromaDB/pgvector/MongoDB/Qdrant. CVE-2025-69872 fixed v0.12.0. Rating: 4.0/5."
content_type: "Review"
card_description: "AG2 (ag2ai/ag2, 4.5K stars, Apache 2.0, Python, v0.12.2) is the active community fork of Microsoft's original AutoGen framework. The story matters: microsoft/autogen (57.7K stars, MIT) entered maintenance mode in early 2026, while ag2ai/ag2 carries forward under independent governance with a major architectural rewrite. The Beta API launched in March 2026 introduces an async-first event-driven architecture, a MemoryStream pub/sub event bus, and the Agent Harness — a four-stage lifecycle for stateful agents (Persistence → Assembly → Execution → Post-Processing) backed by in-memory, disk, SQLite, or Redis storage. The legacy ConversableAgent model remains fully supported with nine orchestration patterns including GroupChat (six speaker-selection modes), Swarm (tool-driven handoffs), and Nested Chats. MCP client support via the `autogen.mcp` module wraps any MCP server's tools into AG2 agents; MCP server capability (exposing AG2 agents as MCP endpoints) is not yet available. Framework interoperability is a standout: AG2 can natively use LangChain, CrewAI, and PydanticAI tools without rewrites. RAG support spans ChromaDB, PostgreSQL pgvector, MongoDB, Qdrant, and FalkorDB. Part of our **Developer Tools** category. Rating: 4.0/5."
last_refreshed: 2026-05-06
categories: ["/categories/developer-tools/"]
---

The AutoGen name carries weight in the Python agent community — it was one of the first frameworks to demonstrate that multi-agent conversations could produce results that single-agent prompting could not. In early 2026, that name split into two projects. Understanding the split is the first thing you need to know before choosing either one.

Part of our **[Developer Tools category](/categories/developer-tools/)**.

---

## The Split: Two AutoGen Repositories

**microsoft/autogen** — the original project, created by Microsoft Research
- **57,722 stars**, MIT license, Python + .NET
- **Status: maintenance mode** as of 2026 — no new features planned, Microsoft has shifted focus to its internal Microsoft Agent Framework (MAF) successor
- Last major Python release: v0.7.5 (September 2024)

**ag2ai/ag2** — the community fork that became an independent project
- **4,508 stars**, Apache 2.0 license, Python only (3.10–3.13)
- **Status: actively developed** — v0.12.2 released May 1, 2026; path to v1.0 announced
- Governs itself under an open governance structure established when the fork was created in November 2024

For anyone evaluating "AutoGen" as a framework to build on today, **ag2ai/ag2 is the living project**. The star count gap (57K vs. 4.5K) reflects inertia, not activity. This review covers ag2ai/ag2.

---

## At a Glance

| | |
|---|---|
| **Repo** | [ag2ai/ag2](https://github.com/ag2ai/ag2) |
| **Stars** | ~4,500 |
| **License** | Apache 2.0 |
| **Language** | Python (3.10–3.13) |
| **Version** | v0.12.2 (May 1, 2026) |
| **Install** | `pip install ag2` |
| **Maintainer** | ag2ai community organization (open governance) |
| **Original** | microsoft/autogen (57.7K stars, now maintenance mode) |

---

## What It Does

AG2 is a Python framework for building multi-agent systems. The foundational abstraction is the **ConversableAgent**: every agent in AG2 either is one or inherits from it. You define an agent with a name, a system message, and an `llm_config` specifying the model provider and parameters. Agents communicate through structured message passing, and orchestration logic controls which agents speak, when, and in what order.

The framework supports nine distinct orchestration patterns, ranging from two-agent conversations to complex group dynamics with LLM-driven speaker selection.

---

## Core Orchestration Patterns

### ConversableAgent / AssistantAgent / UserProxyAgent

The primitives. `AssistantAgent` is a pre-configured ConversableAgent for AI tasks. `UserProxyAgent` represents a human (or human-in-the-loop gate) in the conversation. Two-agent back-and-forth between these two is the simplest AG2 pattern and the one most tutorials start with.

### GroupChat

A **GroupChatManager** orchestrates conversations among multiple agents. Six speaker-selection modes determine who speaks next:

- **`auto`** — an LLM selects the next speaker based on context (most flexible, highest cost)
- **`manual`** — human input selects next speaker
- **`random`** — random selection
- **`round_robin`** — strict rotation
- **Custom callable** — your function receives conversation history and returns the next speaker
- **Graph-based transitions** — define an explicit graph of allowed speaker transitions with eligibility filters

### Swarm

Agents hand off to each other through `HandoffMessage` tool calls. Routing is localized and tool-driven rather than managed by a central orchestrator. Useful for workflows where context determines the next specialist.

### Sequential and Nested Chats

Chain multiple conversations in sequence, with each conversation's output passed as context to the next. Nested chats embed sub-conversations inside a parent agent's reasoning — useful for tool-augmented agents that need to spawn a focused sub-dialog to complete a step.

---

## The Beta Rewrite: What's Coming in v1.0

AG2's most significant recent development is the **Beta API** (`autogen.beta`), launched in v0.11.3 (March 2026) and expanded in v0.12.x. It runs alongside the legacy API without breaking changes and is the foundation for v1.0 (legacy API deprecated at v0.14).

### MemoryStream

A pub/sub event bus that isolates agent state from the conversation flow. Rather than sharing mutable state, agents publish to and subscribe from named streams. This enables real-time streaming, safe concurrent agent reuse, and clean separation of concerns.

### Agent Harness (v0.12.2)

Four-stage lifecycle management for stateful agents:

1. **Persistence** — load agent state from a store (memory, disk, SQLite, Redis, locked variants)
2. **Assembly** — compose context from the knowledge store; assembly policies control what gets included in each LLM call
3. **Execution** — run the agent with assembled context
4. **Post-Processing** — compact history, update memory, handle cleanup

Compaction strategies manage long-running agents without unbounded context growth. The design is explicit: "stateful by design" with all persistence behind clean protocols.

### Dependency Injection

Tools auto-generate JSON schemas from Python type hints via `fast_depends`. No manual schema writing required. A single `ModelConfig` covers all LLM providers.

---

## MCP Support

### As an MCP Client

MCP client support lives in `autogen.mcp`. Install with `pip install "ag2[mcp]"` (requires `mcp>=1.11.0`).

The primary entry point is `create_toolkit()`, which connects to an MCP server and returns AG2-compatible tools:

```python
from autogen import AssistantAgent
from autogen.mcp import create_toolkit, SseConfig

# Connect to a remote MCP server via SSE
toolkit = await create_toolkit(
    SseConfig(url="https://your-mcp-server/sse")
)

agent = AssistantAgent(
    name="assistant",
    llm_config={"model": "gpt-4o"},
    tools=toolkit.tools,
)
```

Two transports are supported:
- **`SseConfig`** — for remote SSE-based MCP servers
- **`StdioConfig`** — for local MCP servers running as subprocesses
- **`MCPConfig`** — multi-server container for connecting to multiple MCP servers simultaneously

The `MCPClient` and `MCPClientSessionManager` classes handle connection lifecycle. Security hardening in v0.11.4 added path traversal protection for MCP resource URIs.

### As an MCP Server

Exposing AG2 agents as an MCP server endpoint — so Cursor, Claude Desktop, or other MCP clients can call them — is **not yet implemented** in the open-source package. This is a meaningful gap vs. Mastra (bidirectional MCP OSS), Agno (AgentOS MCP server), and CrewAI Enterprise. There is an open community issue tracking demand for MCP server capability.

---

## Framework Interoperability

A standout feature: AG2 can use tools from other frameworks as drop-in tools without rewrites.

```bash
pip install "ag2[interop-langchain]"
pip install "ag2[interop-crewai]"
pip install "ag2[interop-pydantic-ai]"
```

This means an existing LangChain tool collection, a CrewAI tool, or a PydanticAI-defined tool can be passed directly to an AG2 agent's `tools` list. The framework converts the foreign tool interface automatically. This is genuinely useful for teams migrating to AG2 from another framework or mixing tools across ecosystems.

---

## Memory and RAG

### Memory (Beta API)

The Agent Harness knowledge stores provide structured persistence: in-memory, disk, SQLite, Redis, and locked variants. Assembly policies compose context per LLM call; compaction handles long-running sessions. The `MemoryTool` (v0.11.5) adds explicit memory read/write operations as callable tools.

### RAG (Legacy API)

The `RetrieveChat` capability connects agents to vector stores. Supported backends:

- **ChromaDB** (`ag2[retrievechat]`) — local default
- **PostgreSQL pgvector** — for teams already on Postgres
- **MongoDB** — document store RAG
- **Qdrant** — high-performance vector search
- **Couchbase** — for Couchbase deployments

The **DocAgent** is a higher-level abstraction: a pre-built agent that handles document loading, parsing, storage, and querying as a single unit. Graph RAG is available via Neo4j (`ag2[neo4j]`) and FalkorDB (`ag2[graph-rag-falkor-db]`).

---

## LLM Provider Support

Full multi-provider coverage via optional extras:
OpenAI, Anthropic, Google Gemini (+ Vertex AI), Mistral, Groq, Ollama, AWS Bedrock, DeepSeek, Alibaba DashScope (Qwen), Cohere, Cerebras, Together AI.

Multimodal inputs — Image, Document, Audio, Video — are supported across OpenAI, Gemini, and Anthropic providers.

---

## Security Notes

- **CVE-2025-69872** — DiskCache vulnerability, fixed in v0.12.0 (April 2026)
- **CVE-2026-23745, CVE-2026-23950, CVE-2026-24842** — three CVEs addressed in v0.10.5 (January 2026)
- **v0.11.4 hardening** — shell injection prevention in ShellExecutor, path traversal protection on MCP resource URIs, credential leakage fix in FileLogger

---

## What Works Well

- **Nine orchestration patterns** — from simple two-agent conversations to complex GroupChat dynamics with graph-defined transitions; more built-in patterns than any other reviewed framework
- **Framework interop** — native LangChain, CrewAI, and PydanticAI tool compatibility; migrate without rewriting tools
- **Apache 2.0 license** — permissive commercial use, no copyleft
- **Broad RAG support** — five vector store backends plus GraphRAG; stronger data retrieval story than most frameworks
- **Multi-provider LLM** — 12+ providers via optional extras; avoids vendor lock-in
- **Active Beta rewrite** — the v1.0 architecture (Agent Harness, MemoryStream, async-first) is a genuine maturation, not a rebrand
- **AG2 CLI** (v0.11.5) — command-line tooling for building and deploying multi-agent apps

---

## Limitations

- **Low star count vs. microsoft/autogen** — the 57.7K vs. 4.5K gap creates confusion; many tutorials and StackOverflow answers still reference the maintenance-mode original
- **No MCP server** — AG2 cannot expose itself as an MCP endpoint; bidirectional MCP requires enterprise solutions from competing frameworks
- **Python-only** — no TypeScript/JavaScript support; teams building Node.js applications need Mastra or another framework
- **Dual-track APIs** — the coexistence of the legacy ConversableAgent API and the new Beta API adds cognitive overhead; developers must understand which world they are operating in
- **v1.0 not yet released** — the Beta rewrite represents the future direction, but it is not yet the default; production teams building on the Beta API today are on preview code

---

## Compared to Other Frameworks Reviewed

| Framework | Language | Stars | MCP Client | MCP Server | License |
|---|---|---|---|---|---|
| CrewAI | Python | ~50,600 | Yes (MCPServerAdapter) | Enterprise only | MIT |
| Agno | Python | ~39,800 | Yes (MCPTools) | Yes (AgentOS OSS) | MPL-2.0 |
| **AG2** | **Python** | **~4,500** | **Yes (create_toolkit)** | **No** | **Apache 2.0** |
| Mastra | TypeScript | ~23,600 | Yes | Yes (MCPServer OSS) | Apache-2.0 (core) |
| mcp-agent | Python | ~8,100 | Yes (6 patterns) | No | Apache-2.0 |
| PydanticAI | Python | ~16,500 | Yes | Limited | MIT |

---

## Who Should Use AG2

AG2 fits teams that:

- Want the broadest multi-agent orchestration pattern library in Python OSS
- Need to reuse existing LangChain, CrewAI, or PydanticAI tools without rewrites
- Want Apache 2.0 licensing with strong commercial use rights
- Are building complex RAG pipelines and want multiple vector store options
- Can tolerate building on a project with lower community star count than the original and a Beta API still maturing toward v1.0

It is less suited for TypeScript shops, teams that need OSS bidirectional MCP, or developers who want to build on the most community-referenced "AutoGen" (the original microsoft/autogen) — which is in maintenance mode.

---

## Rating: 4.0 / 5

AG2 is technically strong — the nine orchestration patterns, the framework interoperability, and the Apache 2.0 license are all genuine differentiators. The Beta rewrite in March 2026 shows serious architectural thinking about production-scale stateful agents. What constrains the rating are the practical friction points: the star-count confusion with the maintenance-mode original makes onboarding harder, the missing MCP server capability limits integration with the broader MCP ecosystem, and the dual-track API situation (legacy + Beta) is unavoidable complexity for new adopters until v1.0 ships.

If you are already invested in the Python agent ecosystem and need the deepest orchestration pattern library available in OSS, AG2 rewards the investment. If you are starting fresh and want maximum community resources, tutorials, and integrations, CrewAI's 50,000+ stars community may be the more pragmatic choice.

*This review is based on publicly available documentation, GitHub repository analysis, and community reports. ChatForest researches but does not independently run or test the frameworks reviewed here.*
