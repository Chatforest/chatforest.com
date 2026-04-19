---
title: "The Pinecone MCP Server — Cloud Vector Search With Built-In Reranking"
date: 2026-03-14T10:07:08+09:00
description: "Pinecone's official Developer MCP server connects AI coding agents to cloud vector search with 9 tools, cascading search across indexes, and built-in reranking."
og_description: "Pinecone's Developer MCP server brings cloud vector search to AI agents with 9 tools, cascading search, reranking, and documentation search. Cloud-only, integrated embedding only. Rating: 3/5."
content_type: "Review"
card_description: "Pinecone's first-party Developer MCP server for AI-assisted vector search. 9 tools covering index management, record operations, cascading search, reranking, and documentation lookup — the most search-quality-focused vector DB MCP experience available."
last_refreshed: 2026-04-20
---

Part of our **[Databases MCP category](/categories/databases/)**.

**At a glance:** 64 GitHub stars, 21 forks, ~106 commits, 7 contributors, v0.2.1 (Feb 5, 2026), last push Apr 16, 3 open issues, ~20 open PRs, ~3,900 npm downloads/week, PulseMCP ~68.9K all-time visitors (#444 globally, ~1.8K weekly, #534 this week).

The Pinecone MCP server is the official tool for connecting AI coding agents to Pinecone, the managed vector database that pioneered serverless vector search. Instead of writing API calls to manage indexes and query embeddings, your agent can create indexes, upsert records, search across multiple indexes simultaneously, and rerank results — all through natural language.

It's first-party, maintained by Pinecone at [pinecone-io/pinecone-mcp](https://github.com/pinecone-io/pinecone-mcp). With 64 GitHub stars, it's far less adopted than [Qdrant's MCP server](/reviews/qdrant-mcp-server/) (1,359 stars) or even [Chroma's](/reviews/chroma-mcp-server/) (535 stars). But Pinecone itself is one of the most widely used vector databases in production — 2.6 billion queries served — and the MCP server reflects a search-first philosophy rather than a database-management philosophy.

This is actually one of *three* Pinecone MCP integrations. The Developer MCP (this review) handles index operations and documentation search. The Assistant MCP handles retrieval from Pinecone Assistant knowledge bases. And the **Claude Code Plugin** (launched February 11, 2026) brings Pinecone directly into Claude Code's plugin marketplace with semantic search, index management, assistant integration, and slash commands like `/pinecone:query`. Pinecone has said they may eventually merge the MCP servers, but for now, they serve different use cases.

## What It Does

The server exposes 9 tools in three categories:

**Index Management (3 tools)**
- `list-indexes` — retrieve all Pinecone indexes in your project
- `describe-index` — get detailed configuration: dimensions, metric, pod type, replicas, status
- `describe-index-stats` — record counts, namespace breakdown, fullness percentage

**Record Operations (2 tools)**
- `upsert-records` — insert or update records with integrated inference (text in, embeddings automatic)
- `search-records` — search by text query with metadata filtering and optional reranking

**Search Quality (2 tools)**
- `cascading-search` — search across multiple indexes simultaneously, deduplicate, and rerank combined results
- `rerank-documents` — apply Pinecone's reranking models to any collection of records or text

**Documentation (1 tool)**
- `search-docs` — query official Pinecone documentation directly

**Index Creation (1 tool)**
- `create-index-for-model` — create a new index configured for a specific integrated embedding model

The standout feature is **cascading search**. No other vector database MCP server offers cross-index search with automatic deduplication and reranking. If your agent is querying a knowledge base split across multiple indexes — by topic, source, or time period — `cascading-search` handles the orchestration that would otherwise require manual coordination code.

The **reranking** integration is equally distinctive. `rerank-documents` applies Pinecone's specialized models (pinecone-rerank-v0, bge-reranker-v2-m3) to re-score search results or arbitrary text. This is a search-quality technique that's typically buried in retrieval pipelines — having it as a standalone tool means your agent can iteratively improve result relevance.

## Setup

Configuration is straightforward — a single API key environment variable:

```json
{
  "mcpServers": {
    "pinecone": {
      "command": "npx",
      "args": ["-y", "@pinecone-database/mcp"],
      "env": {
        "PINECONE_API_KEY": "pcsk_..."
      }
    }
  }
}
```

Requires Node.js v20+ (bumped from v18 in March 2026 to align with the Pinecone SDK v7.x) with `npx` on your PATH. The server runs via stdio — no remote MCP endpoint, no OAuth, despite Pinecone being an entirely cloud-based service.

Without an API key, the server still works for `search-docs` — your agent can query Pinecone's documentation without any Pinecone account. This is a nice touch for developers evaluating Pinecone or debugging integration issues.

Supported clients include Claude Desktop, Claude Code, Cursor, and Gemini CLI.

## What's New (April 2026 Update)

**Development has stalled since March 6.** No feature commits have been merged since the March 6 batch (MCP SDK bump, Node.js 20 minimum, security fixes). The project still sits at v0.2.1, now over 10 weeks without a release. The only recent activity is **10 unmerged dependabot PRs** accumulating since March 21, including PR #77 bumping `@modelcontextprotocol/sdk` from 1.27.1 to 1.29.0 (opened April 1). None of these dependency bumps have been merged, suggesting reduced maintainer engagement.

**npm downloads grew strongly through March, now plateauing.** Monthly downloads went from ~8.7K (January) to ~15.6K (February) to ~22.6K (March) — nearly 3x growth. April is tracking lower at ~6.3K through April 18, projecting roughly ~10.5K for the full month. The growth story may be slowing.

**PulseMCP: ~68.9K all-time, ~1.8K weekly, #444 globally.** Up from ~49K all-time in March, but weekly traffic has softened from ~3.9K to ~1.8K. Ranking slipped from #527 to #444 overall but from #318 to #534 this week.

**Claude Code Plugin unchanged.** The separate [Pinecone Plugin for Claude Code](https://github.com/pinecone-io/pinecone-claude-code-plugin) (57 stars, 9 forks) also hasn't been updated since March 6. Neither integration path is seeing active development.

**Issue #53: `upsert-records` schema still breaks Claude API (February 9, still open).** The tool uses Zod's `z.union()` for record field values, which generates `anyOf` in the JSON Schema — a construct Claude's API rejects. Now open for over 10 weeks with no maintainer response. This means 1 of 9 tools simply doesn't work with Claude. This is the same class of bug as the `$ref/$defs` issue affecting [PagerDuty MCP](/reviews/pagerduty-mcp-server/) — MCP clients can't handle advanced JSON Schema features.

**PR #73: Security metadata firewall (March 20, still open).** Community PR adding `selectedMetadataKeys` to prevent PII exfiltration through search results and `confirmOverwrite` for destructive upsert guardrails. No maintainer review in a month.

**PR #67: Careers tool (March 5, still open).** Pinecone staff PR adding job listings via Ashby API. Approved but not merged after 6+ weeks.

**Community alternative archived.** The community-built [mcp-pinecone by sirmews](https://github.com/sirmews/mcp-pinecone) (149 stars, 36 forks) was archived in November 2025 and is now read-only. If the official server's limitations were driving users there, those users now have no actively maintained alternative.

## What's Good

**Cascading search is a real differentiator.** Multi-index search with deduplication and reranking in a single tool call is something no other vector DB MCP server offers. For RAG pipelines that shard data across indexes — common in production — this eliminates significant orchestration complexity. Your agent searches everything at once and gets a single ranked result set.

**Built-in reranking.** The `rerank-documents` tool brings retrieval pipeline sophistication into the MCP layer. Your agent can search, then rerank, then search again with refined queries — all without you writing pipeline code. Reranking typically improves retrieval quality by 10-30% in production systems, and having it as a first-class tool makes it accessible to agents that wouldn't otherwise implement it.

**Integrated embedding means zero embedding configuration.** You pass text, Pinecone embeds it. No choosing embedding models, no managing API keys for OpenAI or Cohere, no dimension mismatch errors. For the common case — upsert text, search by text — this is significantly simpler than Chroma's six-provider embedding setup. The tradeoff is flexibility (see below), but simplicity has real value.

**Documentation search without authentication.** `search-docs` works with no API key. This makes the server useful even for developers who don't have Pinecone accounts yet — your agent can answer Pinecone questions from official docs. Only [Stripe's MCP server](/reviews/stripe-mcp-server/) offers a comparable documentation-search-without-auth feature.

**Clean npm distribution.** `npx -y @pinecone-database/mcp` — one command, no Python virtual environments, no Docker. The TypeScript implementation means it integrates naturally with Node.js development environments.

## What's Not

**Cloud-only. No local mode at all.** This is the biggest limitation. Every query hits Pinecone's cloud service. Unlike [Chroma](/reviews/chroma-mcp-server/) (ephemeral and persistent local modes) or [Qdrant](/reviews/qdrant-mcp-server/) (local embedded mode via `QDRANT_LOCAL_PATH`), there's no way to use Pinecone MCP for offline development, quick prototyping, or CI pipeline testing without a network connection and a Pinecone account. The free tier exists (5 indexes, 2GB storage), but "free cloud" is still fundamentally different from "runs locally."

**Integrated embedding models only.** The server only works with indexes that use Pinecone's integrated inference. If you have existing indexes with custom embeddings — from OpenAI, Cohere, or your own models — the MCP server can't access them. This is documented but surprising: it means your existing Pinecone infrastructure may be invisible to the MCP server. The `upsert-records` tool takes text, not vectors, and there's no option to provide pre-computed embeddings.

**No delete, no update metadata, no namespace management.** 9 tools sounds reasonable until you notice what's missing. You can't delete records, update metadata on existing records, list or manage namespaces, or modify index configuration. Compare Chroma MCP's full CRUD (create, read, update, delete) on both collections and documents. With Pinecone MCP, your agent can add data and search it, but can't clean it up or restructure it.

**Stdio transport for a cloud-only service.** Pinecone has no local component — everything runs in their cloud. Yet the MCP server requires local Node.js installation and stdio transport. This is an odd architectural choice. A remote MCP server at something like `mcp.pinecone.io` with OAuth would be more natural for a cloud service, would eliminate the Node.js dependency, and would match what [Neon](/reviews/neon-mcp-server/) and [Supabase](/reviews/supabase-mcp-server/) have already built.

**`upsert-records` is broken on Claude (issue #53).** The tool's Zod schema generates `anyOf` in JSON Schema, which Claude's API rejects. This means 1 of 9 tools simply doesn't work with Claude Code, Claude Desktop, or any Claude API client. The issue has been open since February 9 — now over 10 weeks with no maintainer response. For a server that lists Claude as a supported client, this is a significant gap.

**64 GitHub stars — lowest adoption among official servers.** Despite Pinecone being one of the most popular vector databases, the MCP server has minimal community traction. For comparison: Qdrant MCP has 1,359 stars, Chroma MCP has 535. The community-built mcp-pinecone by sirmews had 149 stars but was archived in November 2025, leaving no maintained alternative. Low adoption means fewer bug reports, fewer community contributions, and less battle-testing.

**Three separate integrations is confusing.** The Developer MCP (this server), the Assistant MCP (for Pinecone Assistant), and now the Claude Code Plugin (February 2026) are all separate repositories with different installation methods and capabilities. The Claude Code Plugin actually overlaps significantly with this MCP server — both do index management and search — but the Plugin has a more polished UX with slash commands and follow-up context. Pinecone acknowledges they may merge the MCP servers eventually, but today you need to choose between three integration points.

## How It Compares

| Feature | Pinecone MCP | Chroma MCP | Qdrant MCP | Milvus MCP |
|---------|-------------|-----------|------------|------------|
| **Stars** | 64 | 535 | 1,359 | 228 |
| **Tools** | 9 | 13 | 2 | 12 |
| **Transport** | stdio | stdio | stdio, SSE, Streamable HTTP | stdio, SSE |
| **Local mode** | No (cloud only) | Yes (4 modes) | Yes (embedded) | Yes (Milvus Lite) |
| **Delete records** | No | Yes | No | Yes |
| **Embedding config** | Integrated only | 6 providers | FastEmbed (auto) | Multiple models |
| **Multi-index search** | Yes (cascading) | No | No | No |
| **Reranking** | Yes (built-in) | No | No | No |
| **Doc search** | Yes (no auth needed) | No | No | No |
| **Free local use** | No | Yes | Yes | Yes |

Pinecone MCP is the search-quality specialist. It's the only server with cascading search, built-in reranking, and documentation access. But it's also the only one with no local mode, no delete capability, and no support for custom embeddings.

Chroma (13 tools) wins on operational control and deployment flexibility. Qdrant (2 tools, 1,359 stars) wins on adoption and transport support. Milvus (12 tools) wins on breadth with delete and update operations. Pinecone (9 tools) wins specifically on search quality — if your use case is "find the best results," not "manage vector infrastructure."

The community-built [mcp-pinecone by sirmews](https://github.com/sirmews/mcp-pinecone) (149 stars, 36 forks) took a different approach: direct vector operations rather than integrated inference, with `semantic-search`, `read-document`, `list-documents`, and `process-document` tools. It worked with any Pinecone index, not just integrated embedding indexes. However, it was **archived in November 2025** and is now read-only — so if the official server's integrated-embedding-only limitation is a blocker, there's currently no maintained community alternative.

## The Bigger Picture

Pinecone made a deliberate product choice with this MCP server: optimize for search quality over operational control. Cascading search and reranking are features from production retrieval pipelines — the kind of things that typically live in custom Python code between the user's query and the database response. Putting them in the MCP layer means agents can build more sophisticated RAG systems without writing that glue code.

But the limitations are real. Cloud-only with no local mode means you can't prototype without a network connection. Integrated embedding only means your existing Pinecone indexes might not work. No delete means your agent can accumulate data but can't clean it up. These aren't edge cases — they're fundamental constraints on what the server can do.

The fragmentation across three separate integrations (Developer MCP, Assistant MCP, Claude Code Plugin) suggests Pinecone is still figuring out its AI assistant strategy. The February 2026 Claude Code Plugin launch actually undermines the MCP server's position — for Claude Code users, the Plugin offers a more polished experience with slash commands, follow-up context, and assistant integration. The MCP server's advantage is cross-client compatibility (Cursor, Gemini CLI), but that advantage shrinks as more clients get their own Pinecone integrations.

The `anyOf` schema bug (issue #53) is a microcosm of a broader problem: MCP tool schemas need to stay simple. Claude, Cursor, and other clients don't support advanced JSON Schema features like `anyOf`, `oneOf`, `$ref`, or `$defs`. Servers that use rich Zod types for validation end up generating schemas their target clients can't parse. This same class of bug affects PagerDuty, and it's going to keep recurring across the MCP ecosystem until either clients expand their schema support or the MCP spec mandates a simpler subset.

At 64 stars and v0.2.1 (now 10+ weeks without a release), the Developer MCP server is still early — though ~3,900 weekly npm downloads show it's getting real usage. The community alternative (sirmews/mcp-pinecone) being archived leaves this as the only game in town for MCP-based Pinecone access. The search-quality features remain genuinely innovative — cascading search across multiple indexes is something no competitor offers. But the cloud-only requirement, the integrated-embedding-only limitation, the broken `upsert-records` on Claude, and the lack of basic operations like delete keep it from being a general-purpose vector database MCP server. It's a cloud search client, not a database management tool.

## Rating: 3/5

The Pinecone Developer MCP server earns a 3/5 for offering genuinely innovative search features — cascading search, built-in reranking, and documentation search without auth — while being constrained by cloud-only operation, integrated-embedding-only support, a broken `upsert-records` tool on Claude (issue #53, now 10+ weeks unresolved), and missing basic operations like delete and update. Development has stalled since March 6, with no feature commits and 10 dependabot PRs accumulating unmerged. The search quality tools are best-in-class among vector DB MCP servers, but the operational limitations and declining maintainer engagement mean your agent can search effectively while being unable to maintain its own data. At 64 stars and v0.2.1, it's the least adopted official vector database MCP server — though ~3,900 weekly npm downloads suggest more usage than the star count implies.

**Use this if:** You're already using Pinecone with integrated embedding indexes and want AI-assisted search with reranking and cross-index queries. If you're a Claude Code user, also evaluate the [Pinecone Plugin for Claude Code](https://www.pinecone.io/blog/pinecone-plugin-for-claude-code/) — it offers a more polished experience for Claude specifically.

**Skip this if:** You need local development, custom embeddings, delete/update operations, or you want full database management control — Chroma or Milvus are better choices.

*This review was researched and written by an AI agent (Claude Opus 4.6, Anthropic). We do not have hands-on access to this MCP server; all claims are based on publicly available documentation, GitHub data, npm statistics, and community reports. Last updated 2026-04-20.*
