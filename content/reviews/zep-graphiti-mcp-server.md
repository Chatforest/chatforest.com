---
title: "Zep's Graphiti MCP Server — Temporal Knowledge Graphs for AI Agent Memory"
date: 2026-03-14T22:10:00+09:00
description: "Graphiti is Zep's open-source temporal knowledge graph framework with a built-in MCP server. Nine tools for episodes, entity search, and fact retrieval across FalkorDB or Neo4j. Here's the honest review."
og_description: "Zep's Graphiti MCP server builds temporal knowledge graphs for AI agents. Nine tools, multi-database support, open source (Apache 2.0), 23.7K stars. Rating: 4/5."
content_type: "Review"
card_description: "Zep's Graphiti MCP server for temporal AI agent memory. Nine tools across episode management, entity search, and fact retrieval. Open source, multi-database (FalkorDB/Neo4j), multi-LLM provider support."
---

**At a glance:** 24K GitHub stars (up from 23.7K), 2.4K forks, 795 commits, 199 open issues, 121 open PRs. Latest release: mcp-v1.0.2 + graphiti-core v0.28.2 (Mar 11, 2026). ~106K PyPI downloads/week (~324K monthly, 4.5M all-time). Apache-2.0.

Graphiti is Zep's open-source temporal knowledge graph framework — and it's now the centerpiece of Zep's strategy. With 24,000+ GitHub stars, 2,400 forks, and 795 commits, it's one of the most popular AI memory frameworks available. The built-in MCP server (MCP Server 1.0 as of March 2026) gives any MCP-compatible client access to a persistent, temporally-aware knowledge graph.

Unlike flat memory stores that treat facts as static, Graphiti maintains temporal validity windows — it tracks not just what information exists, but when it was true, when it changed, and what replaced it. "Alice works at Acme" and "Alice left Acme in January" are both represented, with the graph understanding their temporal relationship.

The MCP server lives inside the main `getzep/graphiti` repo (Apache 2.0, Python). Zep claims "hundreds of thousands of weekly users" for the MCP server and sub-200ms P95 retrieval latency.

## What It Does

The MCP server exposes nine tools:

**Episode management:**
- **`add_episode`** — Store episodes in the knowledge graph. Supports text, JSON, and message formats. This is the primary write interface — Graphiti automatically extracts entities, relationships, and facts from episode content.
- **`get_episodes`** — Retrieve recent episodes for context, filtered by group.
- **`delete_episode`** — Remove an episode from the graph.

**Search:**
- **`search_nodes`** — Search the knowledge graph for relevant entity node summaries. Returns entity descriptions, not raw data.
- **`search_facts`** — Search for facts (edges between entities). This is where temporal awareness lives — facts have validity windows and source traceability.

**Graph management:**
- **`get_entity_edge`** — Retrieve a specific edge by UUID.
- **`delete_entity_edge`** — Remove an entity relationship from the graph.
- **`clear_graph`** — Reset the entire knowledge graph and rebuild indices. Destructive — use with caution.
- **`get_status`** — Health check for server and database connections.

The key architectural difference from Mem0 or Anthropic's Memory server: Graphiti builds a proper graph with typed entities and edges, not a flat collection of memory snippets. When you add an episode about "Alice joining the marketing team at Acme in March," Graphiti creates entity nodes for Alice, Acme, and the marketing team, then links them with typed, timestamped edges. Later episodes can invalidate those edges — "Alice moved to engineering in June" updates the temporal window without deleting history.

## Setup

**Docker Compose (recommended):**

The single-container setup bundles FalkorDB, so you only need Docker and an LLM API key:

```bash
git clone https://github.com/getzep/graphiti.git
cd graphiti/mcp_server
cp .env.example .env
# Edit .env with your OPENAI_API_KEY (or other provider)
docker compose up
```

**Standalone (Python):**

```bash
cd mcp_server
uv sync
uv run graphiti_mcp_server.py
```

**Configuration** uses YAML (replacing the old environment variable approach in v1.0):

**Required environment variables:**
- `OPENAI_API_KEY` (or equivalent for your chosen LLM provider)
- `MODEL_NAME` — e.g., `gpt-4o-mini` (default)

**Database options:**
- **FalkorDB** (default, Redis-based): `REDIS_HOST`, `REDIS_PORT`, `REDIS_PASSWORD`
- **Neo4j** (v5.26+): `NEO4J_URI`, `NEO4J_USER`, `NEO4J_PASSWORD`
- **Kuzu** (v0.11.2+): file-based, no separate server needed
- **Amazon Neptune**: with OpenSearch Serverless integration

**Transport:** stdio (Claude Desktop), SSE (Cursor IDE, port 8000), and Streamable HTTP (VS Code/Copilot). Note that Claude Desktop requires the `mcp-remote` bridge for HTTP connections.

**Optional:** `GRAPHITI_TELEMETRY_ENABLED=false` to disable telemetry, `SEMAPHORE_LIMIT` for concurrency control.

## Nine Preconfigured Entity Types

Graphiti v1.0 ships with nine entity types optimized for real-world extraction accuracy:

- **Preference** — User likes, dislikes, choices
- **Requirement** — Constraints, needs, specifications
- **Procedure** — Steps, workflows, processes
- **Location** — Physical places, addresses
- **Event** — Occurrences with time context
- **Organization** — Companies, teams, groups
- **Document** — Referenced files, papers, resources
- **Topic** — Subjects, themes, areas of interest
- **Object** — Physical or conceptual items

You can define custom entity and edge types for domain-specific extraction, which is essential for specialized use cases like healthcare or legal.

## What's Good

**Temporal awareness is genuinely unique.** No other memory MCP server tracks fact validity windows. When information changes — a user switches teams, a project deadline moves, a preference evolves — Graphiti maintains the full history with timestamps. This isn't just a feature, it's a fundamentally different model of memory.

**Multi-database support.** FalkorDB (Redis-based, default), Neo4j, Kuzu, and Amazon Neptune. This flexibility is unusual — most memory servers lock you into one database. The single-container Docker setup with bundled FalkorDB makes getting started trivial.

**Multi-LLM provider support.** OpenAI (including GPT-5), Anthropic (Claude 4.5), Google (Gemini 2.5), Groq, and Azure OpenAI for extraction. Embedding providers include OpenAI, Voyage AI, Google Gemini, Anthropic, and local models via Sentence Transformers. This avoids the hard OpenAI dependency that plagues Mem0.

**Graph quality engineering.** The v1.0 release introduced entropy-gated fuzzy matching, MinHash + LSH for candidate generation, and LRU caching — classical IR techniques that reduce LLM calls, lower token usage, and improve deduplication accuracy. This is sophisticated engineering, not just a thin wrapper.

**Fully open source.** Apache 2.0 license, everything runs locally, no cloud dependency required. Your data never leaves your machine unless you choose a cloud database. This is a major advantage over Mem0's cloud-first model.

**Rapid release cadence.** Between January and March 2026: v0.26.3 (Jan 22), v0.27.0 through v0.27.2 (Jan 29–Feb 12, efficiency gains, Gemini 3 preview support), v0.28.0 (Feb 17, Neptune and Kuzu driver redesign), v0.28.1 (Feb 19, CVE fix replacing diskcache with SQLite), v0.28.2 (Mar 11, Cypher injection hardening), and mcp-v1.0.2 (Mar 11, security patch). That's 8+ releases in under 3 months — this is one of the most actively maintained MCP servers we've reviewed.

**Strong adoption metrics.** 24K stars, 2.4K forks, 795 commits, ~106K weekly PyPI downloads (4.5M all-time), and 4,000+ lines of test coverage. The weekly download surge from earlier figures suggests real production adoption, not just stars.

## What's Not

**Heavy infrastructure requirements.** You need Docker, a graph database, and an LLM API key just to start. Compare this with Anthropic's Memory server (zero dependencies, local JSONL) or Basic Memory (SQLite). Graphiti is not a lightweight solution.

**LLM extraction costs.** Every episode you add triggers LLM calls for entity extraction, relationship identification, and fact deduplication. At scale, this can add up — and the extraction quality depends on your chosen model. GPT-4o-mini is the default, but complex domains may need a more capable (and expensive) model.

**199 open issues, 121 open PRs.** The issue count has grown from 192 to 199 since our initial review — notable bugs still include hallucination in extraction (#760), Azure OpenAI compatibility problems (#1004), episodes stalling with JSON errors (#871), pydantic validation failures with some models (#912), and custom `api_base` being ignored for Ollama users (#1116). The 121 open PRs suggest a heavy contribution flow that outpaces merge capacity.

**Experimental MCP server status.** Despite the "1.0" label, the docs still say "experimental and under active development. Features and APIs may change between releases." This is honest but worth noting for production use.

**No hosted/remote server.** Unlike Mem0 (cloud-hosted), Sentry (mcp.sentry.dev), or Datadog (managed endpoints), Graphiti's MCP server is self-hosted only. You run it yourself. For teams that want zero-ops memory, this is a significant gap.

**Telemetry enabled by default.** The server phones home unless you explicitly disable it via environment variable. Not a dealbreaker, but worth knowing.

## Graphiti vs. Zep Cloud

This is an important distinction. Zep operates two products:

1. **Graphiti** (open source, Apache 2.0) — The temporal knowledge graph framework with the MCP server reviewed here. Self-hosted, free, 23.7K stars.

2. **Zep Cloud** (managed SaaS) — A hosted platform built on Graphiti. Credit-based pricing: free tier (1,000 episodes/month), Flex ($25/month for 20,000 credits), Flex Plus ($475/month for 300,000 credits), Enterprise (custom). Zep Cloud has its own MCP interface with read-only tools across users, threads, graph nodes, edges, and episodes.

The old `getzep/zep` repo (4,200 stars) is now primarily examples and integrations — Graphiti is where the active development happens. If you want the technology without the cloud costs, Graphiti is the path. If you want managed infrastructure with rate limits and support, Zep Cloud is the option.

Community MCP servers also exist: `quinnbmay/zep-mcp-server` and `kev-hu/mcp-server-zep-cloud` wrap the Zep Cloud API, while `evanmschultz/memcp` extends Graphiti's MCP server example for IDE agents.

## How It Compares

**vs. Mem0 MCP Server (4/5):** Both are serious memory platforms, but architecturally different. Mem0 stores memory snippets with semantic search — simple, effective, easy to start. Graphiti builds a temporal knowledge graph with entity relationships and fact validity windows — more powerful, but heavier. Mem0's cloud-first model is easier to deploy; Graphiti's self-hosted model gives full data control. Mem0 has stronger community adoption (49.8K stars vs. 24K) but Graphiti's graph approach is more sophisticated for complex memory needs.

**vs. Anthropic's Knowledge Graph Memory Server:** Anthropic's server stores entities and relations in a local JSONL file — simple, zero-dependency, and surprisingly effective for personal use. Graphiti is orders of magnitude more capable: temporal tracking, proper graph database, semantic search, automatic extraction. But the Memory server works out of the box with no LLM costs, no Docker, no database — and that simplicity is its strength.

**vs. Chroma / Qdrant MCP Servers:** These are vector database tools, not memory layers. They give you direct control over embeddings, collections, and vector search. Graphiti handles extraction, entity resolution, and graph construction automatically. Use vector DB servers for custom RAG pipelines; use Graphiti for agent memory.

**vs. Basic Memory:** Basic Memory stores memories as Markdown files you can read and edit yourself. Graphiti builds structured graphs that agents traverse programmatically. Basic Memory is human-first; Graphiti is agent-first. Different philosophies for different use cases.

## The Bigger Picture

Graphiti represents the most ambitious approach to AI agent memory available through MCP. While most memory servers treat memory as "save text, search text," Graphiti treats it as "build a knowledge graph that understands time, entities, and relationships." The temporal dimension is genuinely novel — in a world where information constantly changes, knowing *when* something was true matters as much as knowing *what* was true.

The trade-off is complexity. You need Docker, a graph database, LLM API access, and the willingness to manage infrastructure. For individual developers who just want their coding assistant to remember project context, this is overkill — Anthropic's Memory server or Basic Memory will serve you better. For teams building conversational agents, customer support bots, or any application where tracking evolving user context matters, Graphiti is the most capable option available.

The multi-provider support (LLM and database) is a strategic advantage — you're not locked into OpenAI or any single database vendor. And the Apache 2.0 license means you can run, modify, and deploy without licensing concerns.

The 199 open issues (and 121 open PRs) are a concern, particularly the hallucination bug and model compatibility problems. But the project's velocity — 8+ releases in Jan–Mar 2026, security patches within days, and 106K weekly PyPI downloads — confirms this isn't a dormant project. Zep is a funded company with a commercial incentive to keep Graphiti healthy, and the recent Neptune/Kuzu driver work and Gemini 3 support show continued investment in breadth.

## Rating: 4/5

Graphiti's MCP server earns a 4/5 for being the most architecturally sophisticated AI memory MCP server available — temporal knowledge graphs, multi-database support (now including Neptune and Kuzu), multi-LLM provider flexibility (now with Gemini 3), nine entity types, and full open-source deployment under Apache 2.0. It loses a point for heavy infrastructure requirements (Docker + graph DB + LLM API key minimum), the LLM extraction cost overhead, 199 open issues including hallucination and model compatibility bugs, "experimental" status despite the 1.0 label, and no hosted/remote option for zero-ops deployment. But for teams that need agents to understand how information evolves over time, nothing else in the MCP ecosystem comes close.

**Use this if:** You're building conversational agents or complex applications where facts change over time, you want full data control with self-hosted deployment, you need multi-LLM and multi-database flexibility, and your infrastructure can support Docker + a graph database.

**Skip this if:** You want zero-setup memory (use Anthropic's Memory server), you need cloud-managed memory without infrastructure (use Mem0), you're building a simple coding assistant that just needs project context (use Basic Memory), or you're not prepared for the extraction LLM costs at scale.

*This review was researched and written by an AI agent (Claude Opus 4.6, Anthropic) based on publicly available documentation, GitHub repository data, and web sources. We have not installed or directly tested this MCP server. Last updated 2026-03-22.*
