---
title: "The Mem0 MCP Server — AI Memory That Actually Scales (If You Pay)"
date: 2026-03-14T21:50:00+09:00
description: "Mem0's MCP server gives AI agents persistent, semantic memory with nine tools covering add, search, update, and delete."
og_description: "Mem0's MCP server provides persistent AI memory with semantic search, graph memory, and nine tools. Free tier available, local self-hosting via OpenMemory. Rating: 4/5."
content_type: "Review"
card_description: "Mem0's MCP server for persistent AI agent memory. Nine tools, semantic search, optional graph memory, free tier with 10K memories, and a self-hosted OpenMemory option for full local control."
last_refreshed: 2026-04-19
---

Part of our **[Databases MCP category](/categories/databases/)**.

**At a glance:** ~53,500 GitHub stars (main repo), ~6,000 forks, v2.0.0 (Apr 16, 2026), 9 tools, Python, Apache-2.0, PulseMCP ~128K all-time (#278 globally, ~387 weekly)

Mem0 is the most well-funded, most-starred memory layer in the AI ecosystem — 53,500+ GitHub stars, $24M in funding, and a platform used by thousands of repositories. Their MCP integration is available through the `mem0-mcp-server` PyPI package (v0.2.1) and the newer Mem0 Plugin for AI Editors (9 MCP tools with lifecycle hooks), wrapping the Mem0 Memory API so any MCP-compatible client can add, search, update, and delete long-term memories through natural language.

Unlike Anthropic's official Knowledge Graph Memory server (which stores everything in a local JSONL file), Mem0 is a managed cloud service with semantic search, automatic memory extraction, and entity linking (which replaced the older graph memory approach in v2.0.0). The trade-off is obvious: you get a production-grade memory layer, but your data goes through Mem0's cloud (unless you self-host with OpenMemory).

**Note on the MCP server repo:** The standalone `mem0-mcp-server` GitHub repository appears to have been removed or consolidated — it returns 404 as of April 2026. The PyPI package still exists at v0.2.1 (December 2025), but Mem0's MCP strategy has shifted toward the **Mem0 Plugin for AI Editors** (launched March-April 2026), which provides 9 MCP memory tools with lifecycle hooks and cloud MCP server support. There's also a separate community implementation by Cole Medin (`coleam00/mcp-mem0`, 673 stars, 233 forks) that's been dormant for over a year (last commit April 2025).

## What It Does

The server exposes nine tools:

**Memory operations:**
- **`add_memory`** — Persist text or conversation history for a user or agent. Mem0 automatically extracts and indexes key information from the content.
- **`search_memories`** — Semantic search across stored memories with filtering and result limits. This is where Mem0 shines — it doesn't just do keyword matching, it understands meaning.
- **`get_memories`** — List memories with structured filters and pagination.
- **`get_memory`** — Retrieve a single memory by its ID.
- **`update_memory`** — Overwrite a memory's content.
- **`delete_memory`** — Remove an individual memory.
- **`delete_all_memories`** — Bulk delete all memories within a scope.

**Entity management:**
- **`delete_entities`** — Remove user, agent, app, or run entities and their associated data.
- **`list_entities`** — Enumerate stored entities across the system.

The key difference from simpler memory servers: Mem0 does intelligent extraction. When you save a conversation, it doesn't just dump the raw text — it identifies and stores the meaningful facts. "I prefer Python over JavaScript and I'm working on a healthcare startup" becomes structured memories that surface when contextually relevant.

## Setup

**Installation via pip or uv:**

```bash
uv pip install mem0-mcp-server
# or
pip install mem0-mcp-server
```

**Claude Desktop configuration:**

```json
{
  "mcpServers": {
    "mem0": {
      "command": "uvx",
      "args": ["mem0-mcp-server"],
      "env": {
        "MEM0_API_KEY": "your-api-key"
      }
    }
  }
}
```

You need a Mem0 platform account (free tier available). Get your API key from the Mem0 dashboard.

**Environment variables:**
- `MEM0_API_KEY` — Required. Your Mem0 platform credentials.
- `MEM0_DEFAULT_USER_ID` — Optional. Defaults to "mem0-mcp".
- `MEM0_ENABLE_GRAPH_DEFAULT` — Optional. Enable graph memory (default: false).
- `MEM0_MCP_AGENT_MODEL` — Optional. Defaults to "openai:gpt-4o-mini".

**Docker deployment** is also available for HTTP transport on port 8081, and there's a **Smithery** option for managed remote hosting.

**Transport:** stdio (default via uvx) and HTTP (via Docker).

## The Two Mem0 MCP Options

This is where it gets interesting. Mem0 actually offers two distinct MCP servers:

### 1. mem0-mcp-server (Cloud)

The main MCP server reviewed here. It connects to Mem0's hosted platform — your memories live on their infrastructure, you get their semantic search and extraction engine, and pricing starts at free.

**Pricing tiers:**
- **Hobby (free):** 10,000 memories, 1,000 retrieval calls/month
- **Starter ($19/month):** 50,000 memories, 5,000 retrievals
- **Pro ($249/month):** Unlimited memories, 50,000 retrievals, graph memory, analytics
- **Enterprise (custom):** On-prem deployment, SSO, SLA

### 2. OpenMemory MCP (Local/Self-hosted)

A completely local, privacy-first alternative. OpenMemory runs on your machine using Docker + Postgres + Qdrant — no data leaves your infrastructure. It includes a dashboard UI for browsing, managing, and controlling memory access per client.

OpenMemory uses SSE transport (not stdio), connects to your local Postgres for relational metadata and Qdrant for vector search, and provides audit logs for every read and write. It's the right choice if you can't send data to a third-party cloud.

The trade-off: you need Docker and the infrastructure running locally, and you lose Mem0's managed extraction engine and graph memory features.

## What's New (April 2026 Update)

**Mem0 SDK v2.0.0 launched (April 16, 2026) — a major overhaul.** The biggest change since we first reviewed Mem0. Key changes: **single-pass extraction** (one LLM call per `add()`, ~50% latency reduction), **hybrid retrieval** combining semantic search + BM25 + entity-graph boosting, and **entity linking** replacing the older graph memory approach (Neo4j/Memgraph no longer required for relationship tracking). All 15 supported vector stores now support `keyword_search()` and `search_batch()`. This is a breaking release — existing integrations may need migration.

**New token-efficient memory algorithm (April 14).** Competitive retrieval accuracy at under 7,000 tokens per call vs. 25,000+ for full-context approaches. Biggest gains: single-session assistant (+53.6 points) and temporal reasoning (+42.1 points).

**SQL/Cypher injection vulnerability disclosed (April 17) — unpatched.** GHSA-5gv3-2fv6-jvhx identifies 18 SQL injection points in the PGVector backend, 11 in Azure MySQL, and Cypher injection in Neptune Analytics. CVSS 8.1 (High) for Neptune, 6.5 (Medium) for PGVector/MySQL. Fix PR #4878 exists but hasn't been merged. This is a significant security concern for self-hosted deployments using affected backends.

**MCP strategy has shifted.** The standalone `mem0-mcp-server` GitHub repo now returns 404. The PyPI package remains at v0.2.1 (December 2025, ~1,183 downloads/week). Mem0's MCP delivery has moved to the **Mem0 Plugin for AI Editors** (launched March-April 2026) — 9 MCP tools with lifecycle hooks and cloud MCP server support, integrated directly into Claude Code, Cursor, and Codex workflows. There's also the **Mem0 Skill Graph** (April 6) for in-context documentation and **Mem0 CLI v0.2.2** for command-line access.

**OpenMemory consolidated into main repo.** The separate `mem0ai/open-memory` repo has been folded into `github.com/mem0ai/mem0/tree/main/openmemory`. Last OpenMemory-specific commits (March 25) added Streamable HTTP transport, an `infer` parameter for `add_memories`, and operator precedence fixes in `search_memory`. OpenMemory continues to support multiple LLM providers including Ollama for fully local operation.

**Independent benchmarks remain mixed, competitive field intensifying.** Mem0 claims 66.9% LOCOMO accuracy vs. OpenAI Memory's 52.9%, with 91% lower latency and 90% reduced token usage. But new entrants are claiming higher scores: **OMEGA** (95.4% LongMemEval with GPT-4.1), **Mastra Observational Memory** (94.87% with GPT-5-mini). Zep/Graphiti scores 71.2% on LongMemEval and remains the closest direct competitor. Letta released **Letta Code** in March 2026, a memory-first coding agent.

**Platform adoption continues growing.** Main repo stars up from ~50,600 to ~53,500 (+5.7%), forks from ~5,600 to ~6,000. PyPI downloads for `mem0ai` are strong at ~625K/week (~2.5M/month). Mem0 published a "State of AI Agent Memory 2026" report (April 1) positioning themselves in a maturing landscape.

**Previous updates (March 2026):** v1.0.5-v1.0.7 brought Ollama support, Apache AGE graph store, MiniMax LLM provider, per-agent memory isolation, noise filtering, and deduplication. AWS published an enterprise reference architecture with ElastiCache + Neptune Analytics.

## What's Good

**Semantic search that works.** Mem0's retrieval is the real differentiator. It doesn't just match keywords — it understands that "my preferred programming language" should surface the memory about Python, even if those exact words weren't stored. The +26% accuracy claim over OpenAI Memory (from their own benchmarks) is plausible given the architecture, though independent benchmarks show more modest results (see "What's New" above).

**Automatic memory extraction — now faster.** Agents don't need to decide what to remember. Feed in a conversation and Mem0 pulls out the facts. v2.0.0's single-pass extraction cuts this to one LLM call per `add()`, roughly halving latency compared to the multi-step approach in v1.x.

**Multi-level memory organization.** Memories can be scoped to users, sessions, agents, or apps. Per-agent memory isolation ensures each agent gets its own memory namespace, preventing cross-contamination in complex deployments.

**Entity linking replaces graph memory.** v2.0.0's biggest architectural change: entity linking handles relationship tracking without requiring a separate graph database (Neo4j, Memgraph, etc.). Combined with hybrid retrieval (semantic + BM25 + entity-graph boosting), this simplifies deployment while maintaining relationship awareness. The Pro tier still offers enhanced features on top.

**Two deployment models.** Cloud for convenience, OpenMemory for privacy. OpenMemory now supports multiple LLM providers including Ollama for fully local operation — no API calls required.

## What's Not

**Cloud dependency for the main server.** The primary MCP server sends all your memories to Mem0's cloud. For personal use this might be fine, but for enterprise or sensitive data it's a non-starter without OpenMemory.

**Free tier limitations.** 10,000 memories and 1,000 retrievals per month sounds generous until an active agent starts saving memories from every conversation. At typical usage, you could burn through the free tier in a few weeks.

**Price jump to Pro.** The gap from Starter ($19/month) to Pro ($249/month) is steep. Graph memory and analytics — the features that make Mem0 genuinely better than simpler alternatives — are locked behind the Pro tier.

**Active security vulnerability.** A high-severity SQL/Cypher injection vulnerability (GHSA-5gv3-2fv6-jvhx, CVSS 8.1) was disclosed April 17, 2026, affecting PGVector, Azure MySQL, and Neptune Analytics backends. A fix PR exists but hasn't been merged. Self-hosted deployments using these backends should evaluate their exposure.

**OpenAI dependency (partially addressed).** The default agent model is still `openai:gpt-4o-mini`, meaning the cloud extraction pipeline uses OpenAI under the hood. OpenMemory now supports Ollama and other providers for fully local operation, but the cloud MCP server still routes through OpenAI by default.

**Independent benchmarks lag newer competitors.** Mem0 claims 66.9% LOCOMO accuracy (vs. OpenAI Memory's 52.9%), but newer entrants are claiming significantly higher scores: OMEGA (95.4% LongMemEval), Mastra (94.87%), and Zep/Graphiti (71.2% LongMemEval). The competitive field is intensifying fast, and Mem0's value proposition leans more on managed infrastructure and ecosystem integration than raw retrieval accuracy.

**MCP server in transition.** The standalone `mem0-mcp-server` GitHub repo has been removed (returns 404), and the PyPI package hasn't been updated since December 2025. Mem0's MCP strategy is shifting to the Plugin for AI Editors, but this creates confusion for existing users who set up the original server. OpenMemory (now folded into the main repo) provides a local MCP option, but the fragmentation between cloud MCP, OpenMemory MCP, and the new Plugin can be confusing.

**v2.0.0 is a breaking release.** The major version bump introduces migration requirements for existing users. Entity linking replacing graph memory is a significant architectural change — teams invested in Neo4j/Memgraph graph backends need to evaluate the migration path.

## How It Compares

**vs. Anthropic's Memory MCP server:** Mem0 is a massive upgrade in capability — semantic search vs. full-graph dump, automatic extraction vs. manual entity creation, cloud scaling vs. local JSONL. But the Memory server is free, has zero dependencies, and keeps everything local. For simple personal use, Anthropic's server might actually be enough.

**vs. Chroma MCP server:** Chroma gives you raw vector database operations — you manage collections, embeddings, and queries yourself. Mem0 abstracts all of that away into a "just save and search" interface. Mem0 is better for agent memory; Chroma is better for building custom RAG pipelines.

**vs. Qdrant MCP server:** Similar distinction to Chroma — Qdrant is a vector database tool, Mem0 is a memory layer built on top of vector databases. Mem0 handles extraction and organization; Qdrant gives you direct control over the vector space.

**vs. Zep:** Zep is Mem0's closest competitor in the "managed AI memory" space. Zep stores memory as a temporal knowledge graph (Graphiti engine, 71.2% LongMemEval) that tracks how facts change over time, while Mem0 focuses on managed extraction, entity linking (replacing graph memory in v2.0.0), and cloud scaling. Mem0 has far stronger community adoption (~53.5K vs. ~25K stars) and a more mature enterprise story, though Zep's 50% MoM ARR growth shows it's gaining ground.

**vs. Letta/MemGPT:** Letta takes a fundamentally different approach — it's an agent runtime where memory management is part of a full operating-system-inspired platform. Letta released **Letta Code** in March 2026, a memory-first coding agent. Mem0 is easier to integrate as a drop-in memory layer for existing agents, while Letta offers deeper memory architecture (core/archival/recall tiers).

## The Bigger Picture

Mem0 represents where AI memory is heading: managed services that handle the hard parts (extraction, indexing, retrieval) so developers can focus on building agents. The MCP server makes this accessible to any MCP-compatible client with minimal setup.

The challenge is the business model. Free tiers get people started, but the jump to production-grade features (graph memory, serious retrieval volume) costs real money. For individual developers and small teams, this is fine — $19/month is reasonable. For enterprises, the on-prem Enterprise tier exists but the pricing isn't public.

The v2.0.0 release signals a maturing platform — entity linking replacing graph memory, hybrid retrieval, and single-pass extraction are all moves toward simplicity and performance. But the MCP delivery story is fragmented: the original `mem0-mcp-server` repo is gone, the PyPI package is stale, and the new Plugin for AI Editors isn't widely documented yet. OpenMemory (now in the main repo) remains the best self-hosted option, with Streamable HTTP transport added in March.

Memory is a rapidly maturing space for AI agents. The competitive field has intensified significantly — OMEGA, Mastra, and others are claiming benchmark scores that dwarf Mem0's. But Mem0's 53,500+ stars, $24M in funding, and v2.0.0's architectural improvements keep it as the most widely adopted solution. The question is whether adoption momentum can sustain their lead as retrieval accuracy becomes a more standardized metric.

## Rating: 4/5

Mem0's MCP server earns a 4/5 for being the most complete managed AI memory solution available through MCP — nine tools, semantic search, automatic extraction, hybrid retrieval, and both cloud and self-hosted deployment options. The v2.0.0 SDK release (entity linking, single-pass extraction, hybrid retrieval) is a significant step forward. It loses a point for the fragmented MCP delivery story (original repo removed, PyPI package stale, new Plugin not yet widely adopted), an active high-severity SQL injection vulnerability (GHSA-5gv3-2fv6-jvhx), cloud dependency in the main server, and increasingly competitive benchmarks from newer entrants. But in a category where most alternatives are either too simple (Anthropic's JSONL graph) or too low-level (raw vector DB operations), Mem0 hits the right abstraction level for production agent memory — especially for teams that value managed infrastructure and ecosystem breadth.

**Use this if:** You want persistent AI memory without building your own extraction and retrieval pipeline, you're okay with cloud storage (or willing to run OpenMemory locally), and your agent needs to remember user preferences, project context, or conversation history across sessions.

**Skip this if:** You need everything fully local with zero cloud dependencies (OpenMemory helps but entity linking is cloud-only), you're building custom RAG where you need direct vector DB control, your budget can't handle the $249/month jump when you outgrow the free tier, or the active SQL injection vulnerability is a concern for your deployment.

| Feature | Details |
|---|---|
| **GitHub stars** | ~53,500 (main repo) |
| **Version** | v2.0.0 (SDK, Apr 16, 2026) / v0.2.1 (MCP server PyPI, Dec 2025) |
| **Tools** | 9 |
| **Language** | Python |
| **License** | Apache-2.0 |
| **Transport** | stdio, HTTP (Docker), Streamable HTTP (OpenMemory) |
| **PulseMCP** | ~128K all-time (#278), ~387 weekly |

*This review was researched and written by an AI agent (Claude Opus 4.6, Anthropic) and [Rob Nugen](https://robnugen.com). We have not personally tested this MCP server — our analysis is based on documentation, GitHub activity, community benchmarks, and public data. Last updated 2026-04-19.*
