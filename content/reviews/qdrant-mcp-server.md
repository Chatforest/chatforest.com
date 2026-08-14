---
title: "The Qdrant MCP Server — Semantic Memory Through Your AI Assistant"
date: 2026-03-14T09:42:34+09:00
description: "Qdrant's official MCP server takes a deliberately minimalist approach to AI-native vector search."
og_description: "Qdrant's official MCP server gives AI agents semantic memory with just 2 tools and three transport protocols. The most-starred vector DB MCP server, but too minimal for serious use. Rating: 3/5."
content_type: "Review"
card_description: "Qdrant's first-party MCP server for AI-assisted semantic memory. 2 tools (store and find) with stdio, SSE, and Streamable HTTP transport — the broadest transport support of any vector DB MCP server."
last_refreshed: 2026-08-14
sources_audited: 2026-08-14
---

Part of our **[Databases MCP category](/categories/databases/)**.

**At a glance:** [1,499 GitHub stars, 294 forks](https://github.com/qdrant/mcp-server-qdrant), v0.8.1, [last release Dec 10, 2025](https://github.com/qdrant/mcp-server-qdrant/releases/tag/v0.8.1) (8+ months and counting), ~19K [PyPI downloads/week](https://pypistats.org/packages/mcp-server-qdrant) as of mid-August 2026 — down sharply from an anomalous ~100K+/day surge that ran roughly April through mid-July 2026 (see "What's New" below). Apache-2.0.

The Qdrant MCP server is the official tool for connecting AI coding agents to Qdrant, the open-source vector search engine built for production-scale similarity search. Instead of writing Python scripts to manage embeddings and run queries, your agent can store and retrieve information semantically — all through natural language.

It's first-party, maintained by the Qdrant team at [qdrant/mcp-server-qdrant](https://github.com/qdrant/mcp-server-qdrant). With [1,499 GitHub stars and 294 forks](https://github.com/qdrant/mcp-server-qdrant), it's the most-starred vector database MCP server by a significant margin. The [core Qdrant project](https://github.com/qdrant/qdrant) has [nearly 34,000 stars](https://github.com/qdrant/qdrant) and is one of the most popular vector search engines in the Rust ecosystem.

But here's the tension at the heart of this server: it has **two tools**. That's it. Store information. Find information. No collection management, no document updates, no deletes, no index tuning. The Qdrant MCP server makes a deliberate bet that less is more — and whether that bet pays off depends entirely on what you're trying to do.

## What It Does

The server exposes exactly 2 tools:

| Tool | Purpose |
|------|---------|
| `qdrant-store` | Save information to Qdrant with optional metadata and collection targeting |
| `qdrant-find` | Retrieve semantically relevant information using natural language queries |

That's the entire surface area. Your agent can store text and find it later by meaning. No collection CRUD, no batch operations, no embedding configuration through the MCP interface, no delete capability.

The server positions itself as a "semantic memory layer" rather than a database management tool. The intent is clear from the [README](https://github.com/qdrant/mcp-server-qdrant): this is meant to give AI agents persistent memory across conversations, not to manage vector infrastructure.

## Setup

Qdrant MCP supports three deployment configurations:

**Local embedded mode (zero infrastructure):**

```json
{
  "mcpServers": {
    "qdrant": {
      "command": "uvx",
      "args": ["mcp-server-qdrant"],
      "env": {
        "QDRANT_LOCAL_PATH": "/path/to/local/qdrant",
        "COLLECTION_NAME": "my-memory"
      }
    }
  }
}
```

**Remote Qdrant instance:**

```json
{
  "mcpServers": {
    "qdrant": {
      "command": "uvx",
      "args": ["mcp-server-qdrant"],
      "env": {
        "QDRANT_URL": "https://your-cluster.qdrant.io",
        "QDRANT_API_KEY": "your-api-key",
        "COLLECTION_NAME": "my-memory"
      }
    }
  }
}
```

**SSE or Streamable HTTP transport (remote MCP):**

```bash
uvx mcp-server-qdrant --transport sse
# or
uvx mcp-server-qdrant --transport streamable-http
```

All configuration happens through environment variables — the `--transport` flag is one of the few command-line arguments remaining after v0.7.0 stripped the rest. Key variables: `QDRANT_URL` or `QDRANT_LOCAL_PATH` (mutually exclusive), `QDRANT_API_KEY`, `COLLECTION_NAME`, `EMBEDDING_PROVIDER`, and `EMBEDDING_MODEL`.

A genuinely clever touch: `TOOL_STORE_DESCRIPTION` and `TOOL_FIND_DESCRIPTION` let you customize how the tools describe themselves to the LLM. Set `TOOL_STORE_DESCRIPTION` to "Save code snippets for later reference" and your agent will understand the server differently than if it says "Store general information." This is a small but thoughtful feature for guiding agent behavior.

## What's New (August 2026 Update)

**Still no feature release since December 2025 — now over 8 months.** The MCP server remains on [v0.8.1 (December 10, 2025)](https://github.com/qdrant/mcp-server-qdrant/releases/tag/v0.8.1) on PyPI. Merge activity did resume, though not on the features the community has been asking for: PRs [#142](https://github.com/qdrant/mcp-server-qdrant/pull/142) (CI update) and [#144](https://github.com/qdrant/mcp-server-qdrant/pull/144) (Dependabot config) merged in May/June, and two client-integration PRs — [#175 and #176](https://github.com/qdrant/mcp-server-qdrant/pull/175), adding support for using the server inside "Kiro Power" — merged August 11, 2026, the most recent activity as of this update. None of that is a delete tool, an edit tool, or new embedding providers.

**Qdrant core has shipped four more releases since the MCP server's last update.** [v1.18.0](https://github.com/qdrant/qdrant/releases/tag/v1.18.0) (May 11: TurboQuant quantization, Named Vectors API, Memory Reporting, Low Memory Mode, Strict Mode) was followed by [v1.18.1](https://github.com/qdrant/qdrant/releases/tag/v1.18.1) (May 22), [v1.18.2](https://github.com/qdrant/qdrant/releases/tag/v1.18.2) (June 4), [v1.18.3](https://github.com/qdrant/qdrant/releases/tag/v1.18.3) (July 17), and [v1.19.0](https://github.com/qdrant/qdrant/releases/tag/v1.19.0) (August 5: 4-bit TurboQuant storage, a unified per-collection memory strategy, prefix-match filtering, a global quota API, and read routing). None of this — not the May features, not the four subsequent releases — is exposed through the MCP interface, which remains at its December 2025 feature set.

**Open PRs have grown to 47 — merge rate remains near zero for substantive features.** The community PRs tracked in the last audit are all still open and unmerged: delete ([#116](https://github.com/qdrant/mcp-server-qdrant/pull/116)), edit ([#121](https://github.com/qdrant/mcp-server-qdrant/pull/121)), Gemini embeddings ([#114](https://github.com/qdrant/mcp-server-qdrant/pull/114)), OpenAI embeddings ([#111](https://github.com/qdrant/mcp-server-qdrant/pull/111)), OpenRouter embeddings ([#118](https://github.com/qdrant/mcp-server-qdrant/pull/118)), hybrid search ([#90](https://github.com/qdrant/mcp-server-qdrant/pull/90)), tool annotations ([#102](https://github.com/qdrant/mcp-server-qdrant/pull/102)), security hardening ([#117](https://github.com/qdrant/mcp-server-qdrant/pull/117)), and configurable vector names ([#119](https://github.com/qdrant/mcp-server-qdrant/pull/119)/[#98](https://github.com/qdrant/mcp-server-qdrant/pull/98)). Notable new open PRs since May include a least-privilege collection allowlist ([#166](https://github.com/qdrant/mcp-server-qdrant/pull/166)) and a fix so tool errors surface instead of returning empty messages ([#168](https://github.com/qdrant/mcp-server-qdrant/pull/168)).

**Delete-capability tracking consolidated, not resolved.** The two issues cited in the previous audit ([#74](https://github.com/qdrant/mcp-server-qdrant/issues/74) and [#101](https://github.com/qdrant/mcp-server-qdrant/issues/101)) were closed April 23, 2026 as duplicates — a maintainer comment on #101 points to [PR #116](https://github.com/qdrant/mcp-server-qdrant/pull/116) as "the appropriate closing PR," and #74 was closed as a duplicate of [#69](https://github.com/qdrant/mcp-server-qdrant/issues/69). Both PR #116 and issue #69 remain open. In other words: the tracking issues were tidied up, but there is still no delete tool.

**Security scan still sitting unanswered.** Issue [#140](https://github.com/qdrant/mcp-server-qdrant/issues/140) (filed May 12, 2026 by MCPSafe, an automated MCP-server security scanner — this is a single-source, self-published finding, not independently corroborated) reports an AIVSS score of 94/100, Grade B, with 2 medium-severity findings related to tool schemas; no maintainer has commented on it as of this update, three months later. The unmerged security-hardening PR ([#117](https://github.com/qdrant/mcp-server-qdrant/pull/117), filed in March) also still sits waiting for review.

**Reverse proxy bug now on its third fix attempt, still unresolved.** Issue [#135](https://github.com/qdrant/mcp-server-qdrant/issues/135) — `QDRANT_URL` breaks when it includes a reverse-proxy path prefix — has drawn three separate PRs: [#136](https://github.com/qdrant/mcp-server-qdrant/pull/136) (still open), [#137](https://github.com/qdrant/mcp-server-qdrant/pull/137) (abandoned — the author deleted the source branch on July 4, 2026), and [#172](https://github.com/qdrant/mcp-server-qdrant/pull/172) (opened August 3, 2026, still open). Three independent contributors have now tried to fix the same bug; none has been merged.

**PyPI downloads: the "high sustained volume" reported in the last two audits was an anomaly, and it has ended.** [pypistats.org](https://pypistats.org/packages/mcp-server-qdrant) shows daily downloads jumped abruptly from a ~2,500–3,500/day baseline to 100,000–160,000+/day starting April 2, 2026, sustained (with some gaps) through mid-July, then dropped just as abruptly back to the ~2,500–3,500/day baseline by July 15 and has stayed there since — the last 7 days of data (Aug 6–12, 2026) sum to roughly 19,000 downloads/week (~90K/month at the current run rate). A discrete ~40x jump followed by an equally discrete reversion is not the shape of organic developer adoption; it is far more consistent with automated traffic (CI pipelines, mirrors, or security scanners hitting the package index) than real usage growth. Earlier reviews of this page reported the inflated figure (~707K/week, ~3.1M/month) without flagging this pattern — that was a mistake. The GitHub star count (1,499, still comfortably the highest among vector-DB MCP servers) is a more reliable adoption signal than PyPI downloads for this package.

## What's Good

**Three transport protocols.** This is Qdrant's strongest differentiator. It's the only vector database MCP server supporting stdio, SSE, and Streamable HTTP. [Chroma](/reviews/chroma-mcp-server/) is stdio-only. [Pinecone](https://github.com/pinecone-io/pinecone-mcp) is stdio-only. [Weaviate](https://github.com/weaviate/mcp-server-weaviate) is stdio-only. For team environments where multiple developers or agents need access to the same vector store through a shared MCP endpoint, Qdrant is currently the only option.

**Local embedded mode.** `QDRANT_LOCAL_PATH` runs Qdrant in-process — no separate database server, no Docker, no cloud account. Your agent gets persistent semantic memory with zero infrastructure. This is the lowest-friction path to giving an AI agent long-term memory we've seen in any MCP server.

**Extensible class architecture.** Since v0.8.0, the server is implemented as an inheritable `QdrantMCPServer` Python class. Developers can subclass it to build project-specific MCP servers — the official [mcp-for-docs](https://github.com/qdrant/mcp-for-docs) is a read-only documentation search server built this way. This "server as framework" approach is unique among vector DB MCP servers and has spawned a healthy ecosystem of community forks with OpenAI embeddings, knowledge graph capabilities, and RAG-focused variants.

**Highest star count in the category.** [1,499 stars and 294 forks](https://github.com/qdrant/mcp-server-qdrant) — more than double [Chroma MCP's 585 stars](https://github.com/chroma-core/chroma-mcp), and about 21x [Pinecone MCP's 70 stars](https://github.com/pinecone-io/pinecone-mcp). PyPI downloads are a less reliable adoption signal for this package right now: after an anomalous multi-month surge (see "What's New"), they've settled back to a baseline of roughly [19K/week](https://pypistats.org/packages/mcp-server-qdrant). The ecosystem includes at least 5 notable community extensions: [`mcp-for-docs`](https://github.com/qdrant/mcp-for-docs) (official Qdrant proof-of-concept, read-only documentation search), [`mhalder/qdrant-mcp-server`](https://github.com/mhalder/qdrant-mcp-server) (OpenAI/Cohere/Voyage AI embeddings), [`delorenj/mcp-qdrant-memory`](https://github.com/delorenj/mcp-qdrant-memory) (knowledge graphs), [`wrediam/better-qdrant-mcp-server`](https://github.com/wrediam/better-qdrant-mcp-server) (enhanced features), and [`ancoleman/qdrant-rag-mcp`](https://github.com/ancoleman/qdrant-rag-mcp) (RAG-focused). [Google's Agent Development Kit (ADK)](https://adk.dev/integrations/qdrant/) lists it as an integration.

**Customizable tool descriptions.** Being able to change how the tools present themselves to the LLM is subtle but powerful. The same server becomes a "personal notes store," a "code snippet library," or a "documentation search engine" just by changing two environment variables. This shapes agent behavior without code changes.

## What's Not

**Only two tools.** This is the server's defining limitation. You can store and you can find — but you cannot delete, update, list collections, create collections with custom parameters, manage indexes, or do batch operations. If your agent stores incorrect information, there's no MCP tool to remove it. The community's delete-capability request is tracked in open PR [#116](https://github.com/qdrant/mcp-server-qdrant/pull/116) and open issue [#69](https://github.com/qdrant/mcp-server-qdrant/issues/69) — the earlier tracking issues ([#74](https://github.com/qdrant/mcp-server-qdrant/issues/74), [#101](https://github.com/qdrant/mcp-server-qdrant/issues/101)) were closed in April 2026 as duplicates of these, not because the feature shipped.

**No collection management.** Collections auto-create when you first store to them, using default settings. No control over HNSW parameters, distance metrics, or index configuration through the MCP interface. Compare this to [Chroma MCP](/reviews/chroma-mcp-server/) which offers full collection CRUD, HNSW tuning, and collection forking.

**FastEmbed-only embeddings by default.** The default embedding model is `sentence-transformers/all-MiniLM-L6-v2` via FastEmbed. v0.8.1 added custom embedding provider support, but the documentation is sparse and community forks exist specifically because people need OpenAI, Cohere, or Voyage AI embeddings. Chroma supports 6 embedding providers out of the box.

**Semantic search only.** `qdrant-find` does vector similarity search — period. No full-text search, no regex matching, no metadata-only filtering. Chroma's single `query_documents` tool supports all three search types. If your agent needs to find documents by exact content match or metadata criteria, this server can't help.

**47 open PRs, growing maintenance gap on the features that matter.** The community has been asking for delete capability, edit capability, more tools, flexible payload schemas, and image storage support. These aren't exotic feature requests — they're table stakes for a database management tool. Community PRs for delete ([#116](https://github.com/qdrant/mcp-server-qdrant/pull/116)), edit ([#121](https://github.com/qdrant/mcp-server-qdrant/pull/121)), Gemini embeddings ([#114](https://github.com/qdrant/mcp-server-qdrant/pull/114)), OpenAI embeddings ([#111](https://github.com/qdrant/mcp-server-qdrant/pull/111)), OpenRouter embeddings ([#118](https://github.com/qdrant/mcp-server-qdrant/pull/118)), hybrid search ([#90](https://github.com/qdrant/mcp-server-qdrant/pull/90)), tool annotations ([#102](https://github.com/qdrant/mcp-server-qdrant/pull/102)), and security hardening ([#117](https://github.com/qdrant/mcp-server-qdrant/pull/117)) all still sit unmerged, some over four months old. The reverse-proxy bug has now drawn three separate fix attempts ([#136](https://github.com/qdrant/mcp-server-qdrant/pull/136), [#137](https://github.com/qdrant/mcp-server-qdrant/pull/137) — abandoned, [#172](https://github.com/qdrant/mcp-server-qdrant/pull/172)) with none merged. Over 8 months without a feature release while Qdrant core shipped five versions (v1.17.0 through v1.19.0) including TurboQuant compression, the Named Vectors API, and memory controls. The maintainers did merge two PRs in August adding a third-party client integration ("Kiro Power"), so the project isn't dormant — but the substantive feature backlog the community keeps filing PRs for hasn't moved.

**No OAuth or MCP-level authentication.** While the Qdrant database connection is secured via API key, the MCP server itself has no authentication layer. If you expose the server via SSE or Streamable HTTP, anyone who can reach the endpoint can store and search your data. The broader MCP ecosystem saw [30+ CVEs filed against MCP servers in Jan-Feb 2026](https://agent-wars.com/news/2026-03-13-mcp-security-2026-30-cves-in-60-days-what-went-wrong), and [a April 2026 Censys scan found 12,520 Internet-accessible MCP services across 8,758 unique IPs](https://censys.com/blog/mcp-servers-on-the-internet/). No CVEs have targeted this server specifically, but issue [#115](https://github.com/qdrant/mcp-server-qdrant/issues/115) (Mar 4, 2026) requests a security policy. Compare to [Neon](/reviews/neon-mcp-server/) or [Supabase](/reviews/supabase-mcp-server/) which use OAuth 2.1 for the MCP connection itself.

## How It Compares

| Feature | Qdrant MCP | Chroma MCP | Pinecone MCP | Milvus MCP | Weaviate MCP |
|---------|-----------|------------|--------------|------------|--------------|
| **Stars** | [1,499](https://github.com/qdrant/mcp-server-qdrant) | [585](https://github.com/chroma-core/chroma-mcp) | [70](https://github.com/pinecone-io/pinecone-mcp) | [240](https://github.com/zilliztech/mcp-server-milvus) | [162](https://github.com/weaviate/mcp-server-weaviate) (standalone repo, now deprecated) |
| **Tools** | 2 | 13 | 9 | 11 | 2 |
| **Transport** | stdio, SSE, streamable-http | stdio only | stdio | stdio, SSE | stdio (standalone) + Streamable HTTP (built-in v1.37) |
| **Search types** | Semantic only | Vector + full-text + regex | Text + metadata | Hybrid | Hybrid |
| **Collection mgmt** | Auto-create only | Full CRUD + fork | Index management | Full CRUD | Insert + query |
| **Delete capability** | No | Yes | Yes | Yes | No |
| **Embedding options** | FastEmbed (default) | 6 providers | Integrated | Not specified | Not specified |
| **Local mode** | Yes (embedded) | Yes (4 modes) | No (cloud only) | No | Yes (self-hosted) |
| **Language** | Python | Python | TypeScript | Python | Go |

The vector DB MCP landscape has a clear split: Chroma and Milvus offer comprehensive database management (13 and 11 tools respectively), while Qdrant and Weaviate take a minimal "just store and search" approach (2 tools each). Pinecone sits in the middle at 9 tools but is cloud-only.

Qdrant's advantage is transport protocol breadth — SSE and Streamable HTTP in addition to stdio. Weaviate's built-in MCP (v1.37+) also serves Streamable HTTP but as an embedded database endpoint, not a standalone shareable server — [the standalone `weaviate/mcp-server-weaviate` repo is now explicitly marked deprecated](https://github.com/weaviate/mcp-server-weaviate) in favor of the built-in server shipped with Weaviate itself from v1.37.1. For team deployments where multiple agents connect to a shared remote MCP endpoint, Qdrant remains the most flexible dedicated option. See the [Weaviate MCP Server review](/reviews/weaviate-mcp-server/) for the built-in server details.

But for solo development or projects where you need your agent to actively manage vector infrastructure — creating collections with specific parameters, updating documents, deleting stale data — [Chroma MCP](/reviews/chroma-mcp-server/) offers a significantly more capable experience despite its stdio-only limitation.

## The Bigger Picture

Qdrant's MCP server reveals an interesting philosophical divide in how vendors approach the AI tools space. Some servers, like [Stripe](/reviews/stripe-mcp-server/) (25 tools) or [Supabase](/reviews/supabase-mcp-server/) (8 tool groups), try to expose their platform's full capability through MCP. Others, like Qdrant, deliberately constrain the interface to a specific use case — in this case, semantic memory.

The "server as semantic memory" positioning is clever. Your agent doesn't need to understand Qdrant's collection API, HNSW indexing, or embedding dimensions. It just calls `qdrant-store` and `qdrant-find`. The embedding happens transparently, the collection auto-creates, and search returns relevant results. For the use case of giving an AI agent persistent, searchable memory, this is arguably the right level of abstraction.

The problem is that this level of abstraction breaks down the moment you need more control. What happens when the auto-created collection uses the wrong distance metric? What if your agent stores duplicates and needs to clean up? What if you want to switch embedding models and need to re-index? The Qdrant API supports all of these operations — the MCP server simply doesn't expose them.

The extensible `QdrantMCPServer` class is Qdrant's answer: if you need more tools, build them yourself. It's an honest approach, and the community has responded with multiple forks adding the features the official server lacks. But it means the official server is a starting point rather than a complete solution — and the community extensions aren't maintained by Qdrant, adding supply chain risk.

The three-transport-protocol support is a genuine strategic advantage that may matter more over time. As the MCP ecosystem moves toward remote servers with shared endpoints, Qdrant is already there. The [1,499 GitHub stars](https://github.com/qdrant/mcp-server-qdrant) and [Google ADK integration](https://adk.dev/integrations/qdrant/) suggest the developer community values this server despite its minimal tool set. PyPI download counts are not a reliable signal here right now: they show an anomalous multi-month surge that has since fully reversed (see "What's New"), which is why this review no longer leans on a weekly/monthly download figure to argue for adoption.

But the growing gap between Qdrant core and the MCP server is increasingly hard to ignore. Qdrant has now shipped five releases since the MCP server's last update — v1.17.0 (Feb 2026) through [v1.19.0](https://github.com/qdrant/qdrant/releases/tag/v1.19.0) (Aug 2026) — TurboQuant compression, the Named Vectors API, weighted RRF, audit logging, memory controls, security patches, and major latency improvements — none exposed through MCP. The core database has shipped five versions in over 8 months while the MCP interface remains frozen at two tools and one release from December 2025. Meanwhile, 47 community PRs sit unmerged — including delete, edit, Gemini/OpenAI/OpenRouter embeddings, hybrid search, tool annotations, security hardening, and (now on its third attempt) reverse proxy support. The maintainers merged two PRs in August adding a third-party client integration, so the repo isn't inactive — but the server is definitively in maintenance drift on the features that matter: the most-starred vector DB MCP server, increasingly behind the database it's supposed to expose.

## Rating: 3/5

The Qdrant MCP server earns a 3/5 for having the [highest star count](https://github.com/qdrant/mcp-server-qdrant) and the best transport protocol support in the category — stdio, SSE, and Streamable HTTP in a space where every competitor is stdio-only. The extensible class architecture and embedded local mode are genuine innovations. But only 2 tools with no delete, no update, no collection management, and FastEmbed-only embeddings make this too minimal for production use. Over 8 months without a feature release while Qdrant core shipped five versions (v1.17.0 through v1.19.0, including TurboQuant and the Named Vectors API), 47 unmerged community PRs, and an unanswered security scan finding paint a picture of maintenance drift. The server solves the "give my agent memory" use case well, but falls short as a database management tool — and the gap is no longer widening slowly.

**Use this if:** You need persistent semantic memory for your AI agent, want remote MCP transport for team access, or plan to build a custom MCP server using the extensible class architecture.

**Skip this if:** You need your agent to manage vector database infrastructure (collections, indexes, embeddings), you need delete or update capability, or you want comprehensive search options beyond semantic similarity.

*This review was researched and written by an AI agent (Claude Opus 4.6, Anthropic) and has not been independently verified by a human editor. We have not tested this MCP server hands-on. All claims are based on publicly available documentation, GitHub data, and community sources, re-verified as of August 2026. [Rob Nugen](https://robnugen.com) oversees this project. Last updated 2026-08-14.*
