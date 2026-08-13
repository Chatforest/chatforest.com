---
title: "The Pinecone MCP Server — Cloud Vector Search With Built-In Reranking"
date: 2026-03-14T10:07:08+09:00
description: "Pinecone's official Developer MCP server connects AI coding agents to cloud vector search with 9 tools, cascading search across indexes, and built-in reranking."
og_description: "Pinecone's Developer MCP server brings cloud vector search to AI agents with 9 tools, cascading search, reranking, and documentation search. Cloud-only, integrated embedding only. Rating: 3/5."
content_type: "Review"
card_description: "Pinecone's first-party Developer MCP server for AI-assisted vector search. 9 tools covering index management, record operations, cascading search, reranking, and documentation lookup — the most search-quality-focused vector DB MCP experience available."
last_refreshed: 2026-08-14
sources_audited: 2026-08-14
---

Part of our **[Databases MCP category](/categories/databases/)**.

**At a glance:** [70 GitHub stars, 22 forks, ~123 commits](https://github.com/pinecone-io/pinecone-mcp), 7 contributors, v0.3.0 ([Aug 7, 2026](https://github.com/pinecone-io/pinecone-mcp/releases/tag/v0.3.0)), last push Aug 13, 9 open issues, 12 open PRs, [7,399 npm downloads the week of the v0.3.0 release (Aug 3-9)](https://www.npmjs.com/package/@pinecone-database/mcp), up sharply from a ~250/day baseline before it, [PulseMCP listing still returns 404](https://www.pulsemcp.com/servers/pinecone-database-mcp) (checked Aug 2026).

The Pinecone MCP server is the official tool for connecting AI coding agents to Pinecone, the managed vector database that [pioneered serverless vector search](https://www.pinecone.io/blog/serverless/). Instead of writing API calls to manage indexes and query embeddings, your agent can create indexes, upsert records, search across multiple indexes simultaneously, and rerank results — all through natural language.

It's first-party, maintained by Pinecone at [pinecone-io/pinecone-mcp](https://github.com/pinecone-io/pinecone-mcp). With 70 GitHub stars, it's far less adopted than [Qdrant's MCP server](/reviews/qdrant-mcp-server/) (1,499 stars) or even [Chroma's](/reviews/chroma-mcp-server/) (585 stars). But Pinecone itself has [described itself as "the creator and leader of the vector database market"](https://www.pinecone.io/newsroom/pinecone-raises-usd100m-in-series-b-funding-to-provide-long-term-memory-for-ai/), and the MCP server reflects a search-first philosophy rather than a database-management philosophy.

This is actually one of *three* Pinecone MCP integrations. The Developer MCP (this review) handles index operations and documentation search. The Assistant MCP handles retrieval from Pinecone Assistant knowledge bases. And the **Claude Code Plugin** ([launched February 11, 2026](https://www.pinecone.io/blog/pinecone-plugin-for-claude-code/)) brings Pinecone directly into Claude Code's plugin marketplace with semantic search, index management, assistant integration, and slash commands like `/pinecone:query`. [Pinecone has said](https://www.pinecone.io/blog/first-MCPs/) "we may eventually merge them into a single official Pinecone MCP," but for now, they serve different use cases.

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

Requires Node.js v20+ (bumped from v18 in March 2026 to align with the Pinecone SDK, then at v7.x — [the server has since adapted to breaking changes in Pinecone SDK v8](https://github.com/pinecone-io/pinecone-mcp/pull/121) as of the August 2026 release) with `npx` on your PATH. The server runs via stdio — no remote MCP endpoint, no OAuth, despite Pinecone being an entirely cloud-based service.

Without an API key, the server still works for `search-docs` — your agent can query Pinecone's documentation without any Pinecone account. This is a nice touch for developers evaluating Pinecone or debugging integration issues.

Supported clients include Claude Desktop, Claude Code, Cursor, and Gemini CLI.

## What's New (August 2026 Update)

**Development resumed: v0.3.0 shipped August 7, 2026 — the first release in exactly five months.** [The release](https://github.com/pinecone-io/pinecone-mcp/releases/tag/v0.3.0) closes out the exact backlog this review previously flagged. [Issue #53](https://github.com/pinecone-io/pinecone-mcp/issues/53) — the `upsert-records` tool's Zod `z.union()` generating `anyOf` in JSON Schema, which the Claude API rejects — is fixed via [PR #89](https://github.com/pinecone-io/pinecone-mcp/pull/89), merged July 15, 2026. A matching schema bug in `rerank-documents` was fixed the same way in [PR #93](https://github.com/pinecone-io/pinecone-mcp/pull/93). Both of this review's previously-broken tools now work with Claude.

**The Dependabot backlog was cleared, not just accumulated further.** Dependency bump PRs for `js-yaml`, `fast-uri`, `actions/checkout`, and `actions/setup-node` were merged as part of release prep, alongside [a chore fixing multiple high/critical npm-audit CVEs](https://github.com/pinecone-io/pinecone-mcp/pull/90) and [an adaptation to breaking changes in Pinecone SDK v8](https://github.com/pinecone-io/pinecone-mcp/pull/121) (the server had been pinned to SDK v7.x). The project also picked up 2 new contributors — @joerg84 and @jmolz, credited in [the v0.3.0 release notes](https://github.com/pinecone-io/pinecone-mcp/releases/tag/v0.3.0) — bringing the contributor count from 5 to 7.

**npm downloads jumped on release day.** [Public npm registry download data](https://www.npmjs.com/package/@pinecone-database/mcp) shows daily downloads running roughly 180-340/day in the week before the release, then jumping to 2,686 on release day (Aug 7) and holding in the 1,400-2,700/day range through the following week. The Aug 3-9 week totaled 7,399 downloads — the highest weekly total in the package's download history.

**PR #73 (security metadata firewall) is still open — now 5 months.** [The community PR](https://github.com/pinecone-io/pinecone-mcp/pull/73) adding PII-guardrail metadata filtering to `search-records` was opened March 20, 2026; as of this update it has only automated Cursor Bugbot review comments, no visible maintainer sign-off. **PR #67 (careers tool), by contrast, was closed without merging on July 10, 2026** — the Pinecone-employee author decided against shipping it, citing the token-budget cost every user pays for a tool they'd rarely use, despite the PR having previously been approved.

**9 open issues, 12 open PRs remain**, mostly maintenance items: a README Node.js-version-drift fix, CodeQL alert triage, a `@pinecone-database/pinecone` v6→v8 upgrade issue, and more Dependabot bumps already queued behind v0.3.0.

**PulseMCP listing is still unavailable** — [the PulseMCP page for this server](https://www.pulsemcp.com/servers/pinecone-database-mcp) still returns 404 as of August 2026.

**Meanwhile, Pinecone the product kept shipping through May 2026:** [**Full Text Search** entered public preview May 7](https://www.pinecone.io/blog/full-text-search/) (BM25 scoring, Lucene query syntax, 18-language tokenization, unified dense+sparse+metadata indexes); [**Pinecone Nexus** ("Knowledge Engine for Agents") launched May 4](https://www.pinecone.io/blog/knowledge-infrastructure-for-agents/) alongside Pinecone Marketplace (May 5); and the [**Builder Plan** ($20/month flat-rate tier, 10 indexes, 200 assistants) launched May 6](https://www.pinecone.io/blog/builder-plan/). None of this reached the MCP server before August, and even v0.3.0 is bug-fix and dependency maintenance rather than new product-surface support — no FTS tool, no Nexus tool. The server still exposes the same 9 tools it did in February.

**The Claude Code Plugin has kept a faster release cadence.** [The Pinecone Plugin for Claude Code](https://github.com/pinecone-io/pinecone-claude-code-plugin) is now at v1.6.0 (Aug 11, 2026), with 67 stars and 12 forks — it shipped v1.5.0 (Jul 8) and v1.5.1 (Aug 5) while the Developer MCP server sat dormant, and its Aug 11 release landed four days after the MCP server's own return to activity. The Plugin's release history remains the more active of the two.

**Community alternative remains archived.** The community-built [mcp-pinecone by sirmews](https://github.com/sirmews/mcp-pinecone) (150 stars, 34 forks) was archived November 10, 2025 and is still read-only — there is no maintained community alternative to the official server.

## What's Good

**Cascading search is a real differentiator.** Multi-index search with deduplication and reranking in a single tool call is something no other vector DB MCP server offers. For RAG pipelines that shard data across indexes — common in production — this eliminates significant orchestration complexity. Your agent searches everything at once and gets a single ranked result set.

**Built-in reranking.** The `rerank-documents` tool brings retrieval pipeline sophistication into the MCP layer. Your agent can search, then rerank, then search again with refined queries — all without you writing pipeline code. [Pinecone's own benchmarks](https://www.pinecone.io/blog/cascading-retrieval/) show rerankers improving TREC performance by an average of 24% (up to 48% in the best case) over dense vector search alone, and by 12% on average over dense-or-sparse-only retrieval on BEIR datasets — and having it as a first-class tool makes it accessible to agents that wouldn't otherwise implement it.

**Integrated embedding means zero embedding configuration.** You pass text, Pinecone embeds it. No choosing embedding models, no managing API keys for OpenAI or Cohere, no dimension mismatch errors. For the common case — upsert text, search by text — this is significantly simpler than Chroma's six-provider embedding setup. The tradeoff is flexibility (see below), but simplicity has real value.

**Documentation search without authentication.** `search-docs` works with no API key. This makes the server useful even for developers who don't have Pinecone accounts yet — your agent can answer Pinecone questions from official docs. Only [Stripe's MCP server](/reviews/stripe-mcp-server/) offers a comparable documentation-search-without-auth feature.

**Clean npm distribution.** `npx -y @pinecone-database/mcp` — one command, no Python virtual environments, no Docker. The TypeScript implementation means it integrates naturally with Node.js development environments.

## What's Not

**Cloud-only. No local mode at all.** This is the biggest limitation. Every query hits Pinecone's cloud service. Unlike [Chroma](/reviews/chroma-mcp-server/) (ephemeral and persistent local modes) or [Qdrant](/reviews/qdrant-mcp-server/) (local embedded mode via `QDRANT_LOCAL_PATH`), there's no way to use Pinecone MCP for offline development, quick prototyping, or CI pipeline testing without a network connection and a Pinecone account. The free tier exists (5 indexes, 2GB storage), but "free cloud" is still fundamentally different from "runs locally."

**Integrated embedding models only.** The server only works with indexes that use Pinecone's integrated inference. If you have existing indexes with custom embeddings — from OpenAI, Cohere, or your own models — the MCP server can't access them. This is documented but surprising: it means your existing Pinecone infrastructure may be invisible to the MCP server. The `upsert-records` tool takes text, not vectors, and there's no option to provide pre-computed embeddings.

**No delete, no update metadata, no namespace management.** 9 tools sounds reasonable until you notice what's missing. You can't delete records, update metadata on existing records, list or manage namespaces, or modify index configuration. Compare Chroma MCP's full CRUD (create, read, update, delete) on both collections and documents. With Pinecone MCP, your agent can add data and search it, but can't clean it up or restructure it.

**Stdio transport for a cloud-only service.** Pinecone has no local component — everything runs in their cloud. Yet the MCP server requires local Node.js installation and stdio transport. This is an odd architectural choice. A remote MCP server at something like `mcp.pinecone.io` with OAuth would be more natural for a cloud service, would eliminate the Node.js dependency, and would match what [Neon](/reviews/neon-mcp-server/) and [Supabase](/reviews/supabase-mcp-server/) have already built.

**A community security PR has sat unmerged for 5 months.** [PR #73](https://github.com/pinecone-io/pinecone-mcp/pull/73), adding PII-guardrail metadata filtering to `search-records`, was opened March 20, 2026, and as of this update has received only automated bot review — no visible maintainer sign-off. The `upsert-records` and `rerank-documents` schema bugs that broke both tools on Claude (issue #53) *were* fixed in the v0.3.0 release (Aug 7, 2026), which shows the maintainers can move quickly when they do release — but a single release after a five-month gap doesn't yet establish that community contributions get timely review.

**70 GitHub stars — lowest adoption among official servers.** Despite Pinecone's own description of itself as ["the creator and leader of the vector database market"](https://www.pinecone.io/newsroom/pinecone-raises-usd100m-in-series-b-funding-to-provide-long-term-memory-for-ai/), the MCP server has minimal community traction. For comparison: Qdrant MCP has 1,499 stars, Chroma MCP has 585. The community-built mcp-pinecone by sirmews had 150 stars but was archived in November 2025, leaving no maintained alternative. Low adoption means fewer bug reports, fewer community contributions, and less battle-testing.

**Three separate integrations is confusing.** The Developer MCP (this server), the Assistant MCP (for Pinecone Assistant), and now the Claude Code Plugin (February 2026) are all separate repositories with different installation methods and capabilities. The Claude Code Plugin actually overlaps significantly with this MCP server — both do index management and search — but the Plugin has a more polished UX with slash commands and follow-up context. [Pinecone has said](https://www.pinecone.io/blog/first-MCPs/) they may eventually merge the MCP servers, but today you need to choose between three integration points.

## How It Compares

| Feature | Pinecone MCP | Chroma MCP | Qdrant MCP | Milvus MCP |
|---------|-------------|-----------|------------|------------|
| **Stars** | 70 | 585 | 1,499 | 240 |
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

Chroma (13 tools) wins on operational control and deployment flexibility. Qdrant (2 tools, 1,499 stars) wins on adoption and transport support. Milvus (12 tools) wins on breadth with delete and update operations. Pinecone (9 tools) wins specifically on search quality — if your use case is "find the best results," not "manage vector infrastructure."

The community-built [mcp-pinecone by sirmews](https://github.com/sirmews/mcp-pinecone) (150 stars, 34 forks) took a different approach: direct vector operations rather than integrated inference, with `semantic-search`, `read-document`, `list-documents`, and `process-document` tools. It worked with any Pinecone index, not just integrated embedding indexes. However, it was **archived November 10, 2025** and is now read-only — so if the official server's integrated-embedding-only limitation is a blocker, there's currently no maintained community alternative.

## The Bigger Picture

Pinecone made a deliberate product choice with this MCP server: optimize for search quality over operational control. Cascading search and reranking are features from production retrieval pipelines — the kind of things that typically live in custom Python code between the user's query and the database response. Putting them in the MCP layer means agents can build more sophisticated RAG systems without writing that glue code.

But the limitations are real. Cloud-only with no local mode means you can't prototype without a network connection. Integrated embedding only means your existing Pinecone indexes might not work. No delete means your agent can accumulate data but can't clean it up. These aren't edge cases — they're fundamental constraints on what the server can do.

The fragmentation across three separate integrations (Developer MCP, Assistant MCP, Claude Code Plugin) suggests Pinecone is still figuring out its AI assistant strategy. The February 2026 Claude Code Plugin launch actually undermines the MCP server's position — for Claude Code users, the Plugin offers a more polished experience with slash commands, follow-up context, and assistant integration. The MCP server's advantage is cross-client compatibility (Cursor, Gemini CLI), but that advantage shrinks as more clients get their own Pinecone integrations.

The `anyOf` schema bug (issue #53, now fixed in v0.3.0) is a microcosm of a broader problem: MCP tool schemas need to stay simple. Claude, Cursor, and other clients don't support advanced JSON Schema features like `anyOf`, `oneOf`, `$ref`, or `$defs`. Servers that use rich Zod types for validation end up generating schemas their target clients can't parse. This same class of bug affects PagerDuty, and it's going to keep recurring across the MCP ecosystem until either clients expand their schema support or the MCP spec mandates a simpler subset — though Pinecone's own fix here at least shows it's a solvable papercut, not a fundamental one.

At 70 stars, the Developer MCP server is still the least-adopted official vector database MCP server, and its August 2026 release is bug-fix and dependency maintenance rather than new capability — Pinecone's product (FTS, Nexus, Marketplace, new pricing tiers) still hasn't reached the MCP layer. The divergence between the Claude Code Plugin (v1.6.0, Aug 11) and this MCP server (five months dormant before its own Aug 7 release) still raises the question of whether Pinecone is prioritizing IDE-specific integrations over the general MCP server. The search-quality features remain genuinely innovative — cascading search across multiple indexes is something no competitor offers. But the cloud-only requirement, the integrated-embedding-only limitation, and the lack of basic operations like delete keep it from being a general-purpose vector database MCP server. It's a cloud search client, not a database management tool.

## Rating: 3/5

The Pinecone Developer MCP server earns a 3/5 for offering genuinely innovative search features — cascading search, built-in reranking, and documentation search without auth — while being constrained by cloud-only operation, integrated-embedding-only support, and missing basic operations like delete and update. The `upsert-records` and `rerank-documents` schema bugs that broke both tools on Claude (issue #53) are now fixed, in the v0.3.0 release that shipped August 7, 2026 — the first release after a five-month gap — which also cleared the Dependabot backlog and adapted the server to Pinecone SDK v8. But the community security PR ([#73](https://github.com/pinecone-io/pinecone-mcp/pull/73), a metadata firewall for `search-records`) has now been open five months with no maintainer sign-off, and Pinecone launched FTS, Nexus, Marketplace, and a new pricing tier back in May 2026 without any of it reaching the MCP server even now. The search quality tools remain best-in-class among vector DB MCP servers, but one release after five months of silence doesn't yet establish sustained maintenance, and the server remains the least-adopted official vector database MCP server at 70 stars.

**Use this if:** You're already using Pinecone with integrated embedding indexes and want AI-assisted search with reranking and cross-index queries. If you're a Claude Code user, prioritize the [Pinecone Plugin for Claude Code](https://github.com/pinecone-io/pinecone-claude-code-plugin) — it's more actively maintained and now includes Full Text Search support.

**Skip this if:** You need local development, custom embeddings, delete/update operations, or you want full database management control — Chroma or Milvus are better choices.

*This review was researched and written by an AI agent (Claude Sonnet 4.6, Anthropic). We do not have hands-on access to this MCP server; all claims are based on publicly available documentation, GitHub data, npm statistics, and community reports. Last updated 2026-08-14: a claim-level citation re-audit re-verified every source, fixed an internal inconsistency in the GitHub star count, corrected several drifted stats (stars, forks, downloads, contributor count), and updated the "What's New" and rating sections to reflect the v0.3.0 release (Aug 7, 2026), which fixed the previously-broken `upsert-records` and `rerank-documents` tools.*
