# The Mem0 MCP Server — AI Memory That Actually Scales (If You Pay)

> Mem0's MCP server gives AI agents persistent, semantic memory with nine tools covering add, search, update, and delete.


Part of our **[Databases MCP category](/categories/databases/)**.

**At a glance:** ~56,000 GitHub stars (main repo), ~6,400 forks, v2.0.2 (May 7, 2026), 9 tools, Python, Apache-2.0, PulseMCP ~128K all-time (#278 globally, ~387 weekly)

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

**Pricing tiers (as of May 2026):**
- **Hobby (free):** 10,000 add requests, 1,000 retrieval requests, 1 project
- **Starter ($19/month):** 50,000 add requests, 5,000 retrievals, 1 project
- **Growth ($79/month):** 200,000 add requests, 20,000 retrievals, 3 projects *(new tier)*
- **Pro ($249/month):** 500,000 add requests, 50,000 retrievals, unlimited projects, analytics
- **Enterprise (custom):** On-prem deployment, SSO, SLA
- **Startup Program:** 3 months free Pro for companies with <$5M funding

### 2. Mem0 Self-Hosted Server (formerly OpenMemory — now sunset)

**OpenMemory has been formally deprecated as of May 2026.** Existing OpenMemory users are directed to the Mem0 self-hosted server instead (`cd server && make bootstrap`). The self-hosted server keeps data off Mem0's cloud infrastructure but lacks OpenMemory's dashboard UI and MCP-specific integration. If you set up OpenMemory for privacy reasons, you'll need to migrate — the deprecation notice appeared May 18, 2026.

## What's New (May 2026 Update)

**Memory Decay launched (May 8, 2026).** Re-ranks search results by recency at query time — no reindexing required. Recent memories boosted up to 1.5x, stale memories dampened to 0.3x minimum. Enabled via dashboard or SDK (`project.update` with decay parameter).

**Temporal Reasoning launched (May 12, 2026).** Each memory gets a time signature and classification into 7 types (events, states, plans, preferences, etc.). Seven temporal query modes with zero extra LLM calls. Benchmarks: 94.8% at top_50 on LongMemEval (up from 90.4%), +6.7 points on temporal questions in LoCoMo. This closes the gap significantly against competitors claiming OMEGA (95.4%) and Mastra (94.87%) — Mem0's figure is self-reported. +1ms median latency overhead.

**Security vulnerability GHSA-5gv3-2fv6-jvhx — effectively fixed.** The SQL/Cypher injection flaw (CVSS 8.1) disclosed April 17 has been addressed. An internal PR (#4997) merged approximately April 28 hardened SQL and prompt injection defenses; v2.0.2 (May 7) explicitly names this hardening in its release notes. The original external fix PR (#4878) remains technically open, but the vulnerability appears resolved in production. Users on v2.0.2+ are no longer exposed.

**SDK v2.0.1 (April 25) and v2.0.2 (May 7).** v2.0.1 fixed entity parameter mapping, prompt parameter honoring in vector extraction, and missing fields in async memory creation. v2.0.2 added the security hardening, memory decay SDK exposure, and telemetry identity stitching fix.

**OpenMemory is being sunset.** The local self-hosted option (previously a key selling point) has been formally deprecated. The OpenMemory directory README now states: "OpenMemory is being sunset. For local self-hosted memory with a dashboard, please use the Mem0 self-hosted server instead." This is a significant product direction change — users who set up OpenMemory for privacy reasons need to evaluate migration to the self-hosted server alternative.

**New Growth pricing tier ($79/mo)** inserted between Starter and Pro. Current tiers: Hobby (free: 10K add, 1K retrieval), Starter ($19/mo: 50K add, 5K retrieval), Growth ($79/mo: 200K add, 20K retrieval, 3 projects), Pro ($249/mo: 500K add, 50K retrieval, unlimited projects). A startup program offers 3 months free Pro for companies with <$5M funding.

**Plugin for AI Editors (OpenClaw): v1.0.8–v1.0.11 (April 22–29).** New: interactive setup wizard for OSS configs, environment variable declarations, sensitivity markers, SHA-256 hashing for telemetry, automatic skills-mode config, memory runtime capabilities, and dimension-aware collection management. Available in Cursor Marketplace with full lifecycle automation.

**Growth metrics:** Main repo now at ~56,000 stars and ~6,400 forks (up from ~53,500 / ~6,000 in April). PyPI `mem0ai` downloads hit ~780K/week (up from ~625K in April — ~25% growth in one month).

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

**Self-hosted option via Mem0 Server.** ~~OpenMemory has been sunset~~ — the local dashboard option has been formally deprecated (see May 2026 Update above). Mem0 still offers a self-hosted server path (`cd server && make bootstrap`) for teams that can't use the cloud. It's less polished than OpenMemory was, but it keeps data off Mem0's infrastructure.

## What's Not

**Cloud dependency for the main server.** The primary MCP server sends all your memories to Mem0's cloud. For personal use this might be fine, but for enterprise or sensitive data it's a non-starter without OpenMemory.

**Free tier limitations.** 10,000 memories and 1,000 retrievals per month sounds generous until an active agent starts saving memories from every conversation. At typical usage, you could burn through the free tier in a few weeks.

**Price jump to Pro.** The gap from Starter ($19/month) to Pro ($249/month) is steep. Graph memory and analytics — the features that make Mem0 genuinely better than simpler alternatives — are locked behind the Pro tier.

**Security vulnerability effectively patched (update).** The SQL/Cypher injection flaw (GHSA-5gv3-2fv6-jvhx, CVSS 8.1) disclosed April 17 has been addressed in v2.0.2 (May 7) — update if you haven't. See May 2026 Update above.

**OpenAI dependency (partially addressed).** The default agent model is still `openai:gpt-4o-mini`, meaning the cloud extraction pipeline uses OpenAI under the hood. OpenMemory now supports Ollama and other providers for fully local operation, but the cloud MCP server still routes through OpenAI by default.

**Benchmark competition is heating up — but Mem0 is catching up.** Newer entrants claimed OMEGA (95.4% LongMemEval) and Mastra (94.87%). Mem0's own Temporal Reasoning update (May 12) now claims 94.8% LongMemEval — closing the gap substantially. All three figures are self-reported by their respective vendors. The competitive field is maturing fast and Mem0 is no longer clearly behind on raw retrieval accuracy, though independent third-party benchmarks are still needed.

**MCP server remains stale, OpenMemory deprecated.** The `mem0-mcp-server` PyPI package is still v0.2.1 from December 2025 — no update in six months. The active integration path is now the Plugin for AI Editors (via npx/Cursor Marketplace). And OpenMemory — previously the recommended local/privacy option — is now formally deprecated. The fragmentation has gotten worse: the original GitHub repo is gone, the PyPI package is stale, and OpenMemory is sunset. Teams invested in OpenMemory need a migration plan.

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

Memory is a rapidly maturing space for AI agents. The competitive field intensified through April, with OMEGA and Mastra claiming benchmark scores above Mem0's. But Mem0's Temporal Reasoning launch (May 12) brings its self-reported LongMemEval score to 94.8% — closing the gap with OMEGA (95.4%) and Mastra (94.87%). Independent verification still lags vendor claims. Mem0's 56,000+ stars, $24M in funding, ~780K weekly PyPI downloads, and v2.0.2's security hardening keep it as the most widely adopted managed memory solution. The OpenMemory sunset is the biggest concern for privacy-focused users — it removes a key differentiator and forces migration.

## Rating: 4/5

Mem0's MCP server earns a 4/5 for being the most complete managed AI memory solution available through MCP — nine tools, semantic search, automatic extraction, hybrid retrieval, Memory Decay, and Temporal Reasoning (now at 94.8% LongMemEval, self-reported). The security vulnerability (GHSA-5gv3-2fv6-jvhx) was addressed in v2.0.2, which is a meaningful positive. It holds at 4/5 — not 5/5 — because the MCP delivery story remains fragmented (original repo gone, PyPI package stale at 6+ months, active path now the Plugin for AI Editors), OpenMemory sunset removes the best privacy option, and the pro pricing jump ($79/mo Growth → $249/mo Pro) is still steep for teams that need full retrieval volume. In a category where most alternatives are either too simple or too low-level, Mem0 still hits the right abstraction level — and the momentum metrics (56K stars, 780K weekly PyPI downloads) confirm its position as the dominant managed memory layer.

**Use this if:** You want persistent AI memory without building your own extraction and retrieval pipeline, you're okay with cloud storage (or willing to run OpenMemory locally), and your agent needs to remember user preferences, project context, or conversation history across sessions.

**Skip this if:** You need everything fully local with zero cloud dependencies (OpenMemory is now sunset; the self-hosted server alternative is less polished), you're building custom RAG where you need direct vector DB control, or your budget can't handle the $79–$249/month jump when you outgrow the free tier.

| Feature | Details |
|---|---|
| **GitHub stars** | ~56,000 (main repo) |
| **Version** | v2.0.2 (SDK, May 7, 2026) / v0.2.1 (MCP server PyPI, Dec 2025 — stale) |
| **Tools** | 9 |
| **Language** | Python |
| **License** | Apache-2.0 |
| **Transport** | stdio, HTTP (Docker), Streamable HTTP (self-hosted server) |
| **PulseMCP** | ~128K all-time (#278), ~387 weekly |

*This review was researched and written by an AI agent (Claude Sonnet 4.6, Anthropic) and [Rob Nugen](https://robnugen.com). We have not personally tested this MCP server — our analysis is based on documentation, GitHub activity, community benchmarks, and public data. Last updated 2026-05-19.*

