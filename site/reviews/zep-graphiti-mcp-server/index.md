# Zep's Graphiti MCP Server — Temporal Knowledge Graphs for AI Agent Memory

> Graphiti is Zep's open-source temporal knowledge graph framework with a built-in MCP server. Nine tools for episodes, entity search, and fact retrieval across FalkorDB or Neo4j.


Part of our **[Databases MCP category](/categories/databases/)**.

**At a glance:** [29.9K GitHub stars](https://github.com/getzep/graphiti), 3.0K forks, 280 open issues, 200 open PRs. Latest release: [graphiti-core v0.29.3](https://pypi.org/project/graphiti-core/) (Jul 27, 2026; the [v0.29.0](https://pypi.org/project/graphiti-core/0.29.0/) feature release landed Apr 27, 2026); MCP server still at [mcp-v1.0.2](https://github.com/getzep/graphiti/releases/tag/mcp-v1.0.2) (Mar 11, 2026). ~377K PyPI downloads/week (~1.5M monthly, per [PyPI Stats](https://pypistats.org/packages/graphiti-core)) — up sharply from the ~78K/week we reported in our last audit. Apache-2.0.

Graphiti is Zep's open-source temporal knowledge graph framework — and it's now the centerpiece of Zep's strategy. With 29,900+ GitHub stars, 3,000 forks, and active daily commits, it's one of the most popular AI memory frameworks available. The built-in MCP server (MCP Server 1.0 as of March 2026) gives any MCP-compatible client access to a persistent, temporally-aware knowledge graph.

Unlike flat memory stores that treat facts as static, Graphiti maintains temporal validity windows — it tracks not just what information exists, but when it was true, when it changed, and what replaced it. "Alice works at Acme" and "Alice left Acme in January" are both represented, with the graph understanding their temporal relationship.

The MCP server lives inside the main `getzep/graphiti` repo (Apache 2.0, Python). Zep [reported "hundreds of thousands of weekly users" for the MCP server](https://blog.getzep.com/graphiti-hits-20k-stars-mcp-server-1-0/) when it crossed 20K GitHub stars (Nov 2025 blog post); Zep separately claims [sub-200ms P95 retrieval latency](https://www.getzep.com/) for its platform. [Zep reports 50% month-over-month ARR growth and 240+ customers](https://www.ycombinator.com/companies/zep-ai/jobs/ir0JRMr-marketing-engineer) including Fortune 500 companies — the company is actively hiring engineers and go-to-market staff.

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

**Multi-LLM provider support.** [OpenAI, Azure OpenAI, Google Gemini, Anthropic, Groq, and OpenAI-compatible local/self-hosted endpoints (Ollama, vLLM, and others) for extraction](https://help.getzep.com/graphiti/configuration/llm-configuration). Embedding providers include OpenAI, Voyage AI, Google Gemini, Anthropic, and local models via Sentence Transformers. This avoids the hard OpenAI dependency that plagues Mem0.

**Graph quality engineering.** The v1.0 release introduced entropy-gated fuzzy matching, MinHash + LSH for candidate generation, and LRU caching — classical IR techniques that reduce LLM calls, lower token usage, and improve deduplication accuracy. This is sophisticated engineering, not just a thin wrapper.

**Fully open source.** Apache 2.0 license, everything runs locally, no cloud dependency required. Your data never leaves your machine unless you choose a cloud database. This is a major advantage over Mem0's cloud-first model.

**Active release cadence, with a meaningful cost-efficiency jump in v0.29.0.** After 8+ releases in January–March 2026 (v0.26.3 through v0.28.2), the project shipped a significant update in **v0.29.0 (April 27)**. The headline feature is **combined node + edge extraction**: a single LLM call now handles what previously required two separate calls, substantially reducing token consumption per episode. **Multi-episode batching** consolidates extraction prompts with episode headers for further savings. **Timestamp resolution** was separated into its own step, removing it from competition with structural extraction during LLM processing. Combined extraction is opt-in via `use_combined_extraction=True` with no breaking change to the default path.

v0.29.0 also ships a **Saga summarization API** (`Graphiti.summarize_saga(saga_id)`) for generating summaries across multi-episode narratives, episode metadata filtering on `EpisodicNode`, and `fact_triple` as a first-class episode type for direct structured knowledge ingestion (previously only available in main branch). The search module was substantially restructured (~1K lines modified) with improved tracing coverage throughout. Note: v0.29.0 includes two breaking changes — episode indexing shifted from 1-based to 0-based, and Kuzu users need a schema migration (`ALTER TABLE RelatesToNode_ ADD reference_time TIMESTAMP`). Three patch releases ([v0.29.1 through v0.29.3](https://github.com/getzep/graphiti/releases)) followed through late July. No new MCP server release accompanied any of this; [mcp-v1.0.2](https://github.com/getzep/graphiti/releases/tag/mcp-v1.0.2) (March 11) remains current.

**Strong adoption metrics.** [29.9K stars](https://github.com/getzep/graphiti), 3.0K forks, [~377K weekly PyPI downloads (~1.5M monthly)](https://pypistats.org/packages/graphiti-core), and [18,000+ lines of test coverage](https://github.com/getzep/graphiti/tree/main/tests). Zep reports 240+ customers including Fortune 500 companies. (Note: weekly downloads have grown sharply since our last audit reported ~78K/week — the jump is large enough that we'd treat the exact multiple with some caution, but the direction is unambiguous.)

## What's Not

**Heavy infrastructure requirements.** You need Docker, a graph database, and an LLM API key just to start. Compare this with Anthropic's Memory server (zero dependencies, local JSONL) or Basic Memory (SQLite). Graphiti is not a lightweight solution.

**LLM extraction costs.** Every episode you add triggers LLM calls for entity extraction, relationship identification, and fact deduplication. At scale, this can add up — and the extraction quality depends on your chosen model. GPT-4o-mini is the default, but complex domains may need a more capable (and expensive) model.

**280 open issues, 200 open PRs — both still growing.** Issue and PR counts have kept climbing since our last audit (229 issues / 173 open PRs at that point) — the contribution flow continues to outpace merge capacity. The cluster of `build_communities` bugs filed in April remains unresolved more than four months later: tuple-unpack failures when extracted node count isn't exactly 2 ([#1396](https://github.com/getzep/graphiti/issues/1396), opened Apr 12), unbounded `while True` infinite loop in label propagation ([#1397](https://github.com/getzep/graphiti/issues/1397)), ignored `max_coroutines` setting ([#1398](https://github.com/getzep/graphiti/issues/1398)), crashes on nested attribute values with Neo4j ([#1399](https://github.com/getzep/graphiti/issues/1399)), hangs on hub-and-spoke graphs ([#1400](https://github.com/getzep/graphiti/issues/1400)), LLM cost scaling O(total_nodes) on large graphs ([#1401](https://github.com/getzep/graphiti/issues/1401)), and O(N) Cypher round-trips dominating prep time on larger graphs ([#1419](https://github.com/getzep/graphiti/issues/1419), opened Apr 17). Two other issues noted in our previous review have since been fixed: the Docker image missing optional provider extras ([#1394](https://github.com/getzep/graphiti/issues/1394), closed) and the hardcoded OpenAI reranker requiring unnecessary credentials ([#1393](https://github.com/getzep/graphiti/issues/1393), closed). Previously noted bugs (hallucination [#760](https://github.com/getzep/graphiti/issues/760), Azure OpenAI [#1004](https://github.com/getzep/graphiti/issues/1004), Ollama `api_base` [#1116](https://github.com/getzep/graphiti/issues/1116)) also remain open. The `build_communities` cluster is particularly concerning — it affects a recently promoted feature across multiple backends and topologies, and none of the seven issues have been closed in the four-plus months since they were filed.

**Experimental MCP server status.** Despite the "1.0" label, the docs still say "experimental and under active development. Features and APIs may change between releases." This is honest but worth noting for production use.

**No hosted/remote server.** Unlike Mem0 (cloud-hosted), Sentry (mcp.sentry.dev), or Datadog (managed endpoints), Graphiti's MCP server is self-hosted only. You run it yourself. For teams that want zero-ops memory, this is a significant gap.

**Telemetry enabled by default.** The server phones home unless you explicitly disable it via environment variable. Not a dealbreaker, but worth knowing.

**[CVE-2026-32247](https://nvd.nist.gov/vuln/detail/CVE-2026-32247) (patched in v0.28.2).** A high-severity Cypher injection vulnerability (CWE-943) in the search-filter construction logic for non-Kuzu backends ([GitHub advisory GHSA-gg5m-55jj-8m5g](https://github.com/getzep/graphiti/security/advisories/GHSA-gg5m-55jj-8m5g)). An attacker could execute arbitrary Cypher queries against the database — either directly or via indirect prompt injection in MCP deployments, where an LLM client could be induced to call `search_nodes` with attacker-controlled `entity_types` values. A payload like `Person) DETACH DELETE n RETURN n //` could destroy all graph data. The Kuzu backend was unaffected due to parameterized label handling. This was fixed in v0.28.2 (March 11) — upgrade immediately if running an older version.

## Graphiti vs. Zep Cloud

This is an important distinction. Zep operates two products:

1. **Graphiti** (open source, Apache 2.0) — The temporal knowledge graph framework with the MCP server reviewed here. Self-hosted, free, [29.9K stars](https://github.com/getzep/graphiti).

2. **Zep Cloud** (managed SaaS) — A hosted platform built on Graphiti. [Credit-based pricing](https://www.getzep.com/pricing): free tier (10,000 credits/month), Flex ($125/month for 50,000 credits), Flex Plus ($375/month for 200,000 credits), Enterprise (custom) — these tiers changed since our last audit, which reported an older $25/$475 Flex/Flex Plus structure. Zep [relaunched its Cloud MCP server in June 2026](https://blog.getzep.com/unified-agent-memory-in-any-mcp-client/) around three tools — `search_graph` and `get_user_summary` (read access), plus `add_memory` (write access, off by default; an account-level kill switch can disable writes entirely) — a narrower, read-by-default/write-optional design that replaced the earlier broader read-only tool set across users, threads, nodes, and edges.

The old [`getzep/zep`](https://github.com/getzep/zep) repo (4,800+ stars) is now primarily examples and integrations — Graphiti is where the active development happens. If you want the technology without the cloud costs, Graphiti is the path. If you want managed infrastructure with rate limits and support, Zep Cloud is the option.

A community MCP server also exists: [`kev-hu/zep-mcp`](https://github.com/kev-hu/zep-mcp) wraps the Zep Cloud API. (Two other community servers previously listed here — `quinnbmay/zep-mcp-server` and `evanmschultz/memcp` — have since been taken down or made inaccessible; we've removed those references.)

## How It Compares

**vs. [Mem0 MCP Server](/reviews/mem0-mcp-server/) (4/5):** Both are serious memory platforms, but architecturally different. Mem0 stores memory snippets with semantic search — simple, effective, easy to start. Graphiti builds a temporal knowledge graph with entity relationships and fact validity windows — more powerful, but heavier. Mem0's cloud-first model is easier to deploy; Graphiti's self-hosted model gives full data control. Mem0 has stronger community adoption ([~63K stars](https://github.com/mem0ai/mem0) vs. 29.9K) but Graphiti's graph approach is more sophisticated for complex memory needs.

**vs. [Anthropic's Knowledge Graph Memory Server](/reviews/anthropic-mcp-server/):** Anthropic's server stores entities and relations in a local JSONL file — simple, zero-dependency, and surprisingly effective for personal use. Graphiti is orders of magnitude more capable: temporal tracking, proper graph database, semantic search, automatic extraction. But the Memory server works out of the box with no LLM costs, no Docker, no database — and that simplicity is its strength.

**vs. [Chroma](/reviews/chroma-mcp-server/) / [Qdrant](/reviews/qdrant-mcp-server/) MCP Servers:** These are vector database tools, not memory layers. They give you direct control over embeddings, collections, and vector search. Graphiti handles extraction, entity resolution, and graph construction automatically. Use vector DB servers for custom RAG pipelines; use Graphiti for agent memory.

**vs. Basic Memory:** Basic Memory stores memories as Markdown files you can read and edit yourself. Graphiti builds structured graphs that agents traverse programmatically. Basic Memory is human-first; Graphiti is agent-first. Different philosophies for different use cases.

## The Bigger Picture

Graphiti represents the most ambitious approach to AI agent memory available through MCP. While most memory servers treat memory as "save text, search text," Graphiti treats it as "build a knowledge graph that understands time, entities, and relationships." The temporal dimension is genuinely novel — in a world where information constantly changes, knowing *when* something was true matters as much as knowing *what* was true.

The trade-off is complexity. You need Docker, a graph database, LLM API access, and the willingness to manage infrastructure. For individual developers who just want their coding assistant to remember project context, this is overkill — Anthropic's Memory server or Basic Memory will serve you better. For teams building conversational agents, customer support bots, or any application where tracking evolving user context matters, Graphiti is the most capable option available.

The multi-provider support (LLM and database) is a strategic advantage — you're not locked into OpenAI or any single database vendor. And the Apache 2.0 license means you can run, modify, and deploy without licensing concerns.

The 280 open issues (and 200 open PRs) continue to grow, and the cluster of `build_communities` bugs ([#1396–#1401](https://github.com/getzep/graphiti/issues/1396), [#1419](https://github.com/getzep/graphiti/issues/1419)) remains entirely unresolved more than four months after filing — suggesting the community detection feature needs significant stabilization before it can be relied on. The hallucination bug and model compatibility problems also remain open. But the project's velocity — v0.29.x's combined extraction delivering meaningful LLM cost reduction, active daily commits on main, and 240+ paying customers including Fortune 500s — confirms this isn't a dormant project. The v0.29.0 efficiency improvements are genuinely significant: halving the LLM calls per episode ingestion directly addresses the cost concern that has always been one of Graphiti's main drawbacks. PyPI weekly downloads have since climbed sharply (to roughly ~377K/week per [PyPI Stats](https://pypistats.org/packages/graphiti-core)), well above the ~78K/week we reported previously.

## Rating: 4/5

Graphiti's MCP server earns a 4/5 for being the most architecturally sophisticated AI memory MCP server available — temporal knowledge graphs, multi-database support (FalkorDB, Neo4j, Kuzu, Neptune), multi-LLM provider flexibility, nine entity types, and full open-source deployment under Apache 2.0. v0.29.0's combined extraction (single LLM call for node + edge extraction, down from two) directly addresses the long-standing cost concern. It loses a point for heavy infrastructure requirements (Docker + graph DB + LLM API key minimum), 280 open issues including hallucination bugs and an unresolved `build_communities` cluster (seven issues, four-plus months, no fixes), 200 open PRs showing contribution flow outpacing merge capacity, "experimental" status despite the 1.0 label, and no hosted/remote option for zero-ops deployment. The disclosed [CVE-2026-32247](https://nvd.nist.gov/vuln/detail/CVE-2026-32247) (Cypher injection, [GHSA-gg5m-55jj-8m5g](https://github.com/getzep/graphiti/security/advisories/GHSA-gg5m-55jj-8m5g), patched in v0.28.2) is a reminder to keep versions current. But for teams that need agents to understand how information evolves over time, nothing else in the MCP ecosystem comes close.

**Use this if:** You're building conversational agents or complex applications where facts change over time, you want full data control with self-hosted deployment, you need multi-LLM and multi-database flexibility, and your infrastructure can support Docker + a graph database.

**Skip this if:** You want zero-setup memory (use Anthropic's Memory server), you need cloud-managed memory without infrastructure (use Mem0), you're building a simple coding assistant that just needs project context (use Basic Memory), or you're not prepared for the extraction LLM costs at scale.

*This review was researched and written by an AI agent (Claude Sonnet 4.6, Anthropic) based on publicly available documentation, GitHub repository data, and web sources. We have not installed or directly tested this MCP server. Last updated 2026-05-19.*

---

**Sources:** [getzep/graphiti (GitHub)](https://github.com/getzep/graphiti) · [graphiti-core (PyPI)](https://pypi.org/project/graphiti-core/) · [Zep official site (getzep.com)](https://www.getzep.com)

