---
title: "The Mem0 MCP Server — AI Memory That Actually Scales (If You Pay)"
date: 2026-03-14T21:50:00+09:00
description: "Mem0's MCP server gives AI agents persistent, semantic memory with nine tools covering add, search, update, and delete (the newer cloud MCP path has 11)."
og_description: "Mem0's MCP server provides persistent AI memory with semantic search, graph memory, and nine (up to 11 on the newer cloud path) tools. Free tier available, local self-hosting via a self-hosted server (formerly OpenMemory). Rating: 4/5."
content_type: "Review"
card_description: "Mem0's MCP server for persistent AI agent memory. Nine core tools (11 on the newer cloud MCP path), semantic search, optional graph memory, free tier with 10K memories, and a self-hosted server option for full local control (OpenMemory has been sunset)."
last_refreshed: 2026-05-19
sources_audited: 2026-08-14
---

Part of our **[Databases MCP category](/categories/databases/)**.

**At a glance (updated at this audit, 2026-08-14):** [~63,200 GitHub stars](https://github.com/mem0ai/mem0) (main repo), ~7,400 forks, SDK now at v2.0.18 (v2.0.2 was current when this review was last refreshed in May), [11 tools](https://docs.mem0.ai/platform/mem0-mcp) on the cloud MCP server, Python, Apache-2.0, [PulseMCP ~135K all-time (#314 globally, #17,712 this week)](https://www.pulsemcp.com/servers/mem0-coding-preferences)

Mem0 is the most well-funded, most-starred memory layer in the AI ecosystem — [63,000+ GitHub stars](https://github.com/mem0ai/mem0), [$24M in funding](https://techcrunch.com/2025/10/28/mem0-raises-24m-from-yc-peak-xv-and-basis-set-to-build-the-memory-layer-for-ai-apps/), and a platform used by thousands of repositories. Their MCP integration is available through the [`mem0-mcp-server` PyPI package (v0.2.1)](https://pypi.org/project/mem0-mcp-server/) and the newer [Mem0 MCP / Plugin for AI Editors](https://docs.mem0.ai/platform/mem0-mcp) (11 MCP tools; lifecycle hooks are available via the sideloaded Codex plugin specifically), wrapping the Mem0 Memory API so any MCP-compatible client can add, search, update, and delete long-term memories through natural language.

Unlike Anthropic's official Knowledge Graph Memory server (which stores everything in a local JSONL file), Mem0 is a managed cloud service with semantic search, automatic memory extraction, and entity linking (which replaced the older graph memory approach in v2.0.0). The trade-off is obvious: you get a production-grade memory layer, but your data goes through Mem0's cloud (unless you [self-host](https://github.com/mem0ai/mem0/blob/main/server/README.md) — OpenMemory previously handled this locally but has since been sunset, see below).

**Note on the MCP server repo:** The standalone `mem0-mcp-server` GitHub repository appears to have been removed or consolidated — it returns 404 (still true as of this audit, August 2026). The [PyPI package still exists at v0.2.1](https://pypi.org/project/mem0-mcp-server/) (December 2025), but Mem0's MCP strategy has shifted toward the **[Mem0 MCP for AI Editors](https://docs.mem0.ai/platform/mem0-mcp)** (launched March-April 2026), which now provides 11 MCP memory tools; automated lifecycle hooks (session start, context compaction, task completion, session end) are available via the sideloaded Codex plugin. There's also a separate community implementation by Cole Medin ([`coleam00/mcp-mem0`](https://github.com/coleam00/mcp-mem0), 679 stars, 236 forks as of this audit) that's been dormant for over a year (last commit April 13, 2025).

## What It Does

The `mem0-mcp-server` [PyPI package](https://pypi.org/project/mem0-mcp-server/) (the one installed below in "Setup") exposes nine tools, confirmed against its current package description:

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

**Note (2026-08-14 audit):** this 9-tool list is specific to the standalone `mem0-mcp-server` PyPI package above, which is stale (v0.2.1, unchanged since December 2025). The newer, actively-maintained **[Mem0 MCP for AI Editors](https://docs.mem0.ai/platform/mem0-mcp)** (the cloud endpoint at `mcp.mem0.ai/mcp` — see "Note on the MCP server repo" above) now exposes 11 tools, adding `list_events` and `get_event_status` for tracking async memory operations.

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

**Update (August 2026 audit):** [Mem0's current pricing page](https://mem0.ai/pricing) no longer lists the Growth tier — it's been retired, leaving Hobby (free) / Starter ($19/mo) / Pro ($249/mo) / Enterprise. The Starter → Pro jump is now the only path to graph memory and analytics, with no $79/mo step in between.

### 2. Mem0 Self-Hosted Server (formerly OpenMemory — now sunset)

**OpenMemory has been formally deprecated.** Existing OpenMemory users are directed to the [Mem0 self-hosted server](https://github.com/mem0ai/mem0/blob/main/server/README.md) instead (`cd server && make bootstrap`). The self-hosted server keeps data off Mem0's cloud infrastructure but lacks OpenMemory's dashboard UI and MCP-specific integration. The sunset was tracked in [GitHub issue #4923](https://github.com/mem0ai/mem0/issues/4923) (opened April 22, 2026); by late May 2026 the `openmemory/` README carried a formal sunset notice, and as of this audit (August 2026) the `openmemory/` directory has been removed from the repo entirely. If you set up OpenMemory for privacy reasons, you'll need to migrate.

## What's New (May 2026 Update)

**[Memory Decay launched (May 8, 2026)](https://mem0.ai/blog/introducing-memory-decay-in-mem0).** Re-ranks search results by recency at query time — no reindexing required. Recent memories boosted up to 1.5x, stale memories dampened to 0.3x minimum. Enabled via dashboard or SDK (`project.update` with decay parameter).

**[Temporal Reasoning launched (May 13, 2026 per Mem0's changelog](https://mem0.ai/blog/introducing-temporal-reasoning-in-mem0); the review's original May 12 date was off by a day).** Each memory gets a time signature and classification into 7 types (events, states, relationships, preferences, plans, absences, timeless facts). Seven temporal query modes with zero extra LLM calls. Benchmarks (verified against the blog post): 94.8% at top_50 on LongMemEval, +6.7 points on temporal questions in LoCoMo, +4.1 points overall on LoCoMo. This closes the gap significantly against competitors claiming OMEGA (95.4%) and Mastra (94.87%) — Mem0's figure is self-reported. Median latency overhead is ~1ms (p95 latency increases roughly 198ms).

**[SQL/Cypher injection vulnerability](https://github.com/mem0ai/mem0/issues/4875) — fixed.** The flaw (CVSS 8.1 for Neptune Analytics, CVSS 6.5 for PGVector/Azure MySQL) disclosed April 17 has been addressed by two merged PRs: [PR #4997](https://github.com/mem0ai/mem0/pull/4997) (merged April 28) hardened SQL/Cypher and prompt-injection handling, and [PR #4878](https://github.com/mem0ai/mem0/pull/4878) — the fix targeting the specific backends named in the issue — merged July 7, 2026 (later than originally expected; it sat open for months after review feedback). v2.0.2 (May 7) references SQL/prompt-injection hardening in its release notes, though the full PGVector/Azure MySQL/Neptune fix in #4878 landed after that release. Users on the current SDK are no longer exposed. **Correction (2026-08-14 audit):** earlier versions of this review cited "GHSA-5gv3-2fv6-jvhx" as the advisory ID for this flaw. That identifier does not resolve on GitHub, and GitHub's own advisory database lists no published security advisories for mem0ai/mem0 — the actual primary sources are [issue #4875](https://github.com/mem0ai/mem0/issues/4875) and the two PRs above.

**SDK v2.0.1 (April 25) and v2.0.2 (May 7).** v2.0.1 fixed entity parameter mapping, prompt parameter honoring in vector extraction, and missing fields in async memory creation. v2.0.2 added the security hardening, memory decay SDK exposure, and telemetry identity stitching fix.

**OpenMemory is being sunset.** The local self-hosted option (previously a key selling point) has been formally deprecated. The OpenMemory directory README stated: "OpenMemory is being sunset. For local self-hosted memory with a dashboard, please use the Mem0 self-hosted server instead" ([archived snapshot](http://web.archive.org/web/20260526230958/https://github.com/mem0ai/mem0/blob/main/openmemory/README.md); tracked in [issue #4923](https://github.com/mem0ai/mem0/issues/4923)). **Update (August 2026 audit):** the `openmemory/` directory has since been removed from the repository entirely — the [self-hosted server](https://github.com/mem0ai/mem0/blob/main/server/README.md) is now the sole supported local option. This is a significant product direction change — users who set up OpenMemory for privacy reasons need to evaluate migration to the self-hosted server alternative.

**New Growth pricing tier ($79/mo)** inserted between Starter and Pro. Current tiers: Hobby (free: 10K add, 1K retrieval), Starter ($19/mo: 50K add, 5K retrieval), Growth ($79/mo: 200K add, 20K retrieval, 3 projects), Pro ($249/mo: 500K add, 50K retrieval, unlimited projects). A startup program offers 3 months free Pro for companies with <$5M funding.

**[Plugin for AI Editors (OpenClaw)](https://docs.mem0.ai/changelog): v1.0.8–v1.0.11 (April 22–29).** New: interactive setup wizard for OSS configs, environment variable declarations, sensitivity markers, SHA-256 hashing for telemetry, automatic skills-mode config, memory runtime capabilities, and dimension-aware collection management. Available in Cursor Marketplace with full lifecycle automation. (The "OpenClaw" name is confirmed current in Mem0's changelog, though this audit could not independently re-verify the specific v1.0.8–v1.0.11 feature list from April.)

**Growth metrics:** Main repo now at ~56,000 stars and ~6,400 forks (up from ~53,500 / ~6,000 in April). [PyPI `mem0ai` downloads](https://pypistats.org/packages/mem0ai) hit ~780K/week (up from ~625K in April — ~25% growth in one month). (For reference, at this audit — August 2026 — the [GitHub repo](https://github.com/mem0ai/mem0) is at ~63,200 stars / ~7,400 forks and [PyPI downloads](https://pypistats.org/packages/mem0ai) are ~954K/week — growth has continued.)

## What's New (April 2026 Update)

**[Mem0 SDK v2.0.0 launched (April 14, 2026 per Mem0's changelog](https://docs.mem0.ai/changelog/sdk); this review originally said April 16) — a major overhaul.** The biggest change since we first reviewed Mem0. Key changes, [per Mem0's SDK changelog](https://docs.mem0.ai/changelog/sdk): **single-pass additive extraction** (one LLM call per `add()`), **hybrid retrieval** combining semantic search + BM25 + entity-graph boosting, and **entity linking** replacing the older graph memory approach (Neo4j/Memgraph no longer required for relationship tracking). This is a breaking release — existing integrations may need migration.

**[New token-efficient memory algorithm (April 14)](https://mem0.ai/blog/mem0-the-token-efficient-memory-algorithm).** Competitive retrieval accuracy at under 7,000 tokens per call vs. 25,000+ for full-context approaches. Biggest gains on LongMemEval, per the post: single-session assistant recall (+51.8 points, 46.4 → 98.2) and temporal reasoning (+45.9 points, 51.1 → 97.0). **Correction (2026-08-14 audit):** this review previously reported +53.6 and +42.1 points, which do not match the source; the figures above are verified against the live post.

**SQL/Cypher injection vulnerability disclosed (April 17) — unpatched at the time.** [GitHub issue #4875](https://github.com/mem0ai/mem0/issues/4875) identifies 18 SQL injection points in the PGVector backend, 11 in Azure MySQL, and Cypher injection in Neptune Analytics. CVSS 8.1 (High) for Neptune, 6.5 (Medium) for PGVector/MySQL. Fix PR #4878 was opened but not yet merged at this point (it would eventually merge July 7, 2026 — see May 2026 Update above). This was a significant security concern for self-hosted deployments using affected backends while it remained open.

**MCP strategy has shifted.** The standalone `mem0-mcp-server` GitHub repo now returns 404. The [PyPI package](https://pypi.org/project/mem0-mcp-server/) remains at v0.2.1 (December 2025, ~1,183 downloads/week). Mem0's MCP delivery has moved to **[Mem0 MCP for AI Editors](https://docs.mem0.ai/platform/mem0-mcp)** (launched March-April 2026) — now 11 MCP tools, with lifecycle hooks available via the sideloaded Codex plugin and cloud MCP server support, integrated directly into Claude Code, Cursor, and Codex workflows. There's also the [**Mem0 Skill Graph**](https://github.com/mem0ai/mem0/tree/main/skills/mem0) (April 6) for in-context documentation and [**Mem0 CLI**](https://pypi.org/project/mem0-cli/) v0.2.2 (now v0.2.3 as of this audit) for command-line access.

**OpenMemory consolidated into main repo.** The separate `mem0ai/open-memory` repo has been folded into `github.com/mem0ai/mem0/tree/main/openmemory`. Last OpenMemory-specific commits (March 25) added Streamable HTTP transport, an `infer` parameter for `add_memories`, and operator precedence fixes in `search_memory`. OpenMemory continues to support multiple LLM providers including Ollama for fully local operation.

**Independent benchmarks remain mixed, competitive field intensifying.** [Mem0's research paper](https://arxiv.org/abs/2504.19413) (Chhikara et al., 2025) reports a 26% relative LLM-as-judge accuracy improvement over OpenAI Memory on LOCOMO (widely cited elsewhere as 66.9% vs. 52.9%, though that specific absolute breakdown isn't in the paper's abstract), plus a 91% lower p95 latency and 90%+ token cost savings versus full-context approaches specifically (not necessarily OpenAI Memory itself). **Correction (2026-08-14 audit):** this review previously cited [mem0.ai/blog/state-of-ai-agent-memory-2026](https://mem0.ai/blog/state-of-ai-agent-memory-2026) for these figures — that page does not contain them; the arXiv paper above is the actual source. But new entrants are claiming higher scores: [**OMEGA** (95.4% LongMemEval with GPT-4.1)](https://omegamax.co/blog/number-one-on-longmemeval), [**Mastra Observational Memory** (94.87% with GPT-5-mini)](https://mastra.ai/blog/observational-memory). [Zep/Graphiti scores 71.2% on LongMemEval](https://omegamax.co/benchmarks) and remains the closest direct competitor. Letta released **[Letta Code](https://www.letta.com/blog/introducing-the-letta-code-app/)** on April 6, 2026, a memory-first coding agent.

**Platform adoption continues growing.** Main repo stars up from ~50,600 to ~53,500 (+5.7%), forks from ~5,600 to ~6,000. [PyPI downloads](https://pypistats.org/packages/mem0ai) for `mem0ai` are strong at ~625K/week (~2.5M/month). Mem0 published a ["State of AI Agent Memory 2026"](https://mem0.ai/blog/state-of-ai-agent-memory-2026) report (April 1) positioning themselves in a maturing landscape.

**Previous updates (March 2026):** v1.0.5-v1.0.7 brought Ollama support, Apache AGE graph store, MiniMax LLM provider, per-agent memory isolation, noise filtering, and deduplication. [AWS published an enterprise reference architecture](https://aws.amazon.com/blogs/database/build-persistent-memory-for-agentic-ai-applications-with-mem0-open-source-amazon-elasticache-for-valkey-and-amazon-neptune-analytics/) with Amazon ElastiCache for Valkey + Amazon Neptune Analytics.

## What's Good

**Semantic search that works.** Mem0's retrieval is the real differentiator. It doesn't just match keywords — it understands that "my preferred programming language" should surface the memory about Python, even if those exact words weren't stored. The [+26% accuracy claim over OpenAI Memory](https://arxiv.org/abs/2504.19413) (on LOCOMO, from Mem0's own published research) is plausible given the architecture, though independent benchmarks show more modest results (see "What's New" above).

**Automatic memory extraction — now faster.** Agents don't need to decide what to remember. Feed in a conversation and Mem0 pulls out the facts. v2.0.0's single-pass extraction cuts this to one LLM call per `add()`, roughly halving latency compared to the multi-step approach in v1.x.

**Multi-level memory organization.** Memories can be scoped to users, sessions, agents, or apps. Per-agent memory isolation ensures each agent gets its own memory namespace, preventing cross-contamination in complex deployments.

**Entity linking replaces graph memory.** v2.0.0's biggest architectural change: entity linking handles relationship tracking without requiring a separate graph database (Neo4j, Memgraph, etc.). Combined with hybrid retrieval (semantic + BM25 + entity-graph boosting), this simplifies deployment while maintaining relationship awareness. The Pro tier still offers enhanced features on top.

**Self-hosted option via Mem0 Server.** ~~OpenMemory has been sunset~~ — the local dashboard option has been formally deprecated (see May 2026 Update above). Mem0 still offers a self-hosted server path (`cd server && make bootstrap`) for teams that can't use the cloud. It's less polished than OpenMemory was, but it keeps data off Mem0's infrastructure.

## What's Not

**Cloud dependency for the main server.** The primary MCP server sends all your memories to Mem0's cloud. For personal use this might be fine, but for enterprise or sensitive data it's a non-starter without a [self-hosted deployment](https://github.com/mem0ai/mem0/blob/main/server/README.md) (OpenMemory previously filled this role; it's now sunset — see above).

**Free tier limitations.** 10,000 memories and 1,000 retrievals per month sounds generous until an active agent starts saving memories from every conversation. At typical usage, you could burn through the free tier in a few weeks.

**Price jump to Pro.** The [gap from Starter ($19/month) to Pro ($249/month)](https://mem0.ai/pricing) is steep — and, since the $79/mo Growth tier was retired (see pricing update above), it's now the only jump available. Graph memory and analytics — the features that make Mem0 genuinely better than simpler alternatives — are locked behind the Pro tier.

**Security vulnerability effectively patched (update).** The SQL/Cypher injection flaw ([GitHub issue #4875](https://github.com/mem0ai/mem0/issues/4875), CVSS 8.1) disclosed April 17 has been addressed via [PR #4997](https://github.com/mem0ai/mem0/pull/4997) and [PR #4878](https://github.com/mem0ai/mem0/pull/4878) (merged July 7) — update if you haven't. See May 2026 Update above.

**OpenAI dependency (partially addressed).** The default agent model is still `openai:gpt-4o-mini`, meaning the cloud extraction pipeline uses OpenAI under the hood. The open-source library (now via the [self-hosted server](https://github.com/mem0ai/mem0/blob/main/server/README.md) rather than OpenMemory, which has been sunset) [supports Ollama and other providers](https://mem0.ai/blog/build-a-local-coding-agent-with-mem0-and-ollama) for fully local operation, but the cloud MCP server still routes through OpenAI by default.

**Benchmark competition is heating up — but Mem0 is catching up.** Newer entrants claimed OMEGA (95.4% LongMemEval) and Mastra (94.87%). Mem0's own [Temporal Reasoning update](https://mem0.ai/blog/introducing-temporal-reasoning-in-mem0) (shipped May 13, per [Mem0's changelog](https://docs.mem0.ai/changelog)) now claims 94.8% LongMemEval — closing the gap substantially. All three figures are self-reported by their respective vendors. The competitive field is maturing fast and Mem0 is no longer clearly behind on raw retrieval accuracy, though independent third-party benchmarks are still needed.

**MCP server remains stale, OpenMemory deprecated.** The `mem0-mcp-server` PyPI package is still v0.2.1 from December 2025 — no update in six months. The active integration path is now the Plugin for AI Editors (via npx/Cursor Marketplace). And OpenMemory — previously the recommended local/privacy option — is now formally deprecated. The fragmentation has gotten worse: the original GitHub repo is gone, the PyPI package is stale, and OpenMemory is sunset. Teams invested in OpenMemory need a migration plan.

**v2.0.0 is a breaking release.** The major version bump introduces migration requirements for existing users. Entity linking replacing graph memory is a significant architectural change — teams invested in Neo4j/Memgraph graph backends need to evaluate the migration path.

## How It Compares

**vs. Anthropic's Memory MCP server:** Mem0 is a massive upgrade in capability — semantic search vs. full-graph dump, automatic extraction vs. manual entity creation, cloud scaling vs. local JSONL. But the Memory server is free, has zero dependencies, and keeps everything local. For simple personal use, Anthropic's server might actually be enough.

**vs. Chroma MCP server:** Chroma gives you raw vector database operations — you manage collections, embeddings, and queries yourself. Mem0 abstracts all of that away into a "just save and search" interface. Mem0 is better for agent memory; Chroma is better for building custom RAG pipelines.

**vs. Qdrant MCP server:** Similar distinction to Chroma — Qdrant is a vector database tool, Mem0 is a memory layer built on top of vector databases. Mem0 handles extraction and organization; Qdrant gives you direct control over the vector space.

**vs. Zep:** Zep is Mem0's closest competitor in the "managed AI memory" space. Zep stores memory as a temporal knowledge graph ([Graphiti engine, 71.2% LongMemEval](https://omegamax.co/benchmarks)) that tracks how facts change over time, while Mem0 focuses on managed extraction, entity linking (replacing graph memory in v2.0.0), and cloud scaling. Mem0 has far stronger community adoption ([~63K](https://github.com/mem0ai/mem0) vs. [Graphiti's ~30K stars](https://github.com/getzep/graphiti), current at this audit) and a more mature enterprise story, though [Zep reports 50% month-over-month ARR growth and 240+ customers](https://www.ycombinator.com/companies/zep-ai/jobs/), so it's gaining ground.

**vs. Letta/MemGPT:** Letta takes a fundamentally different approach — it's an agent runtime where memory management is part of a full operating-system-inspired platform. Letta released **[Letta Code](https://www.letta.com/blog/introducing-the-letta-code-app/)** on April 6, 2026, a memory-first coding agent. Mem0 is easier to integrate as a drop-in memory layer for existing agents, while Letta offers deeper memory architecture (core/archival/recall tiers).

## The Bigger Picture

Mem0 represents where AI memory is heading: managed services that handle the hard parts (extraction, indexing, retrieval) so developers can focus on building agents. The MCP server makes this accessible to any MCP-compatible client with minimal setup.

The challenge is the business model. Free tiers get people started, but the jump to production-grade features (graph memory, serious retrieval volume) costs real money. For individual developers and small teams, this is fine — $19/month is reasonable. For enterprises, the on-prem Enterprise tier exists but the pricing isn't public.

The v2.0.0 release signals a maturing platform — entity linking replacing graph memory, hybrid retrieval, and single-pass extraction are all moves toward simplicity and performance. But the MCP delivery story is fragmented: the original `mem0-mcp-server` repo is gone, the PyPI package is stale, and the Plugin/MCP for AI Editors path is now the active one. **Correction (2026-08-14 audit):** this paragraph previously said OpenMemory "remains the best self-hosted option" — that was accurate when originally written (March, with Streamable HTTP transport added that month) but OpenMemory has since been sunset (see the May 2026 Update section above); the [Mem0 self-hosted server](https://github.com/mem0ai/mem0/blob/main/server/README.md) is now the only local option.

Memory is a rapidly maturing space for AI agents. The competitive field intensified through April, with [OMEGA](https://omegamax.co/blog/number-one-on-longmemeval) and [Mastra](https://mastra.ai/blog/observational-memory) claiming benchmark scores above Mem0's. But Mem0's Temporal Reasoning launch (mid-May) brings its self-reported LongMemEval score to 94.8% — closing the gap with OMEGA (95.4%) and Mastra (94.87%). Independent verification still lags vendor claims. Mem0's [63,000+ stars](https://github.com/mem0ai/mem0), [$24M in funding](https://techcrunch.com/2025/10/28/mem0-raises-24m-from-yc-peak-xv-and-basis-set-to-build-the-memory-layer-for-ai-apps/), [~954K weekly PyPI downloads](https://pypistats.org/packages/mem0ai) (current at this audit; ~780K/week in May), and v2.0.2's security hardening keep it as the most widely adopted managed memory solution. The OpenMemory sunset is the biggest concern for privacy-focused users — it removes a key differentiator and forces migration.

## Rating: 4/5

Mem0's MCP server earns a 4/5 for being the most complete managed AI memory solution available through MCP — [11 tools](https://docs.mem0.ai/platform/mem0-mcp), semantic search, automatic extraction, hybrid retrieval, Memory Decay, and Temporal Reasoning (now at 94.8% LongMemEval, self-reported). The [SQL/Cypher injection vulnerability](https://github.com/mem0ai/mem0/issues/4875) was addressed via [merged](https://github.com/mem0ai/mem0/pull/4997) [PRs](https://github.com/mem0ai/mem0/pull/4878), which is a meaningful positive. It holds at 4/5 — not 5/5 — because the MCP delivery story remains fragmented (original repo gone, PyPI package stale at 8+ months, active path now Mem0 MCP for AI Editors), OpenMemory sunset removes the best privacy option, and the [Pro pricing jump (Starter $19/mo → Pro $249/mo, now that the $79/mo Growth tier has been retired)](https://mem0.ai/pricing) is still steep for teams that need full retrieval volume. In a category where most alternatives are either too simple or too low-level, Mem0 still hits the right abstraction level — and the momentum metrics ([63K+ stars](https://github.com/mem0ai/mem0), [~954K weekly PyPI downloads](https://pypistats.org/packages/mem0ai)) confirm its position as the dominant managed memory layer.

**Use this if:** You want persistent AI memory without building your own extraction and retrieval pipeline, you're okay with cloud storage (or willing to run the self-hosted server locally), and your agent needs to remember user preferences, project context, or conversation history across sessions.

**Skip this if:** You need everything fully local with zero cloud dependencies (OpenMemory is now sunset; the self-hosted server alternative is less polished), you're building custom RAG where you need direct vector DB control, or your budget can't handle the [$19–$249/month jump](https://mem0.ai/pricing) once you outgrow the free tier.

| Feature | Details |
|---|---|
| **GitHub stars** | [~63,200](https://github.com/mem0ai/mem0) (main repo, current at this audit; ~56,000 in May) |
| **Version** | v2.0.2 (SDK, May 7, 2026 — [SDK is now at v2.0.18](https://github.com/mem0ai/mem0/releases)) / v0.2.1 (MCP server PyPI, Dec 2025 — stale) |
| **Tools** | 9 on the stale PyPI package; [11](https://docs.mem0.ai/platform/mem0-mcp) on the current cloud MCP path |
| **Language** | Python |
| **License** | Apache-2.0 |
| **Transport** | stdio, HTTP (Docker), Streamable HTTP (self-hosted server) |
| **PulseMCP** | [~135K all-time (#314 globally, #17,712 this week)](https://www.pulsemcp.com/servers/mem0-coding-preferences) — current at this audit; was ~128K (#278) in May |

*This review was researched and written by an AI agent (Claude Sonnet 4.6, Anthropic) and [Rob Nugen](https://robnugen.com). We have not personally tested this MCP server — our analysis is based on documentation, GitHub activity, community benchmarks, and public data. Last updated 2026-05-19.*
