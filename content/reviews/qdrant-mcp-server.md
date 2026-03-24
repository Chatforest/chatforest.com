---
title: "The Qdrant MCP Server — Semantic Memory Through Your AI Assistant"
date: 2026-03-14T09:42:34+09:00
description: "Qdrant's official MCP server takes a deliberately minimalist approach to AI-native vector search. Just 2 tools — store and find — but it's the only vector DB MCP server supporting all three transport protocols. Here's the honest review."
og_description: "Qdrant's official MCP server gives AI agents semantic memory with just 2 tools and three transport protocols. The most adopted vector DB MCP server, but too minimal for serious use. Rating: 3/5."
content_type: "Review"
card_description: "Qdrant's first-party MCP server for AI-assisted semantic memory. 2 tools (store and find) with stdio, SSE, and Streamable HTTP transport — the broadest transport support of any vector DB MCP server."
last_refreshed: 2026-03-14
---

Part of our **[Databases MCP category](/categories/databases/)**.

**At a glance:** 1,300 GitHub stars, 242 forks, 73 commits, v0.8.1, last release Dec 10, 2025, ~20.7K PyPI downloads/week, PulseMCP 326K all-time visitors (#104 globally, ~18.1K weekly, #90 this week). Apache-2.0.

The Qdrant MCP server is the official tool for connecting AI coding agents to Qdrant, the open-source vector search engine built for production-scale similarity search. Instead of writing Python scripts to manage embeddings and run queries, your agent can store and retrieve information semantically — all through natural language.

It's first-party, maintained by the Qdrant team at [qdrant/mcp-server-qdrant](https://github.com/qdrant/mcp-server-qdrant). With 1,300 GitHub stars and 242 forks, it's the most adopted vector database MCP server by a significant margin. The core Qdrant project has over 23,000 stars and is one of the most popular vector search engines in the Rust ecosystem.

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

## What's New (March 2026 Update)

**No new release since December 2025.** The MCP server has been on v0.8.1 since December 10, 2025 — over three months without a release. This is notable because the underlying Qdrant database has been actively evolving.

**Qdrant v1.17.0 shipped February 20, 2026** with substantial improvements: relevance feedback queries (model-generated feedback guides retrieval), major search latency improvements (update queue management for up to 1M pending changes, indexed-only mode, delayed fan-outs), weighted Reciprocal Rank Fusion for hybrid queries, audit logging for API operations, external provider API key support in request headers, and cluster-wide telemetry. **Breaking:** RocksDB storage completely removed in favor of gridstore (no direct upgrade from v1.15.x to v1.17.x). None of these features are surfaced through the MCP server.

**Delete tool finally in development.** PR [#116](https://github.com/qdrant/mcp-server-qdrant/pull/116) adds a `qdrant-delete` tool — the most requested missing feature (issues #74 and #101). Not yet merged.

**Embedding provider expansion in PRs.** PR [#114](https://github.com/qdrant/mcp-server-qdrant/pull/114) adds Google Gemini embedding support, PR [#111](https://github.com/qdrant/mcp-server-qdrant/pull/111) adds OpenAI-compatible embeddings. Both address the FastEmbed-only limitation from previous reviews. Also pending: tool annotations (PR #102), configurable vector names (PR #98), and hybrid search with RRF/DBSF fusion (PR #90).

**21 open PRs, none merged.** The backlog of unmerged community contributions is growing. The server has active community interest but appears maintenance-bottlenecked.

**PyPI adoption surging.** Downloads grew to ~20.7K/week (~81.8K/month), with daily spikes above 11K in early January 2026, likely driven by the broader Q1 2026 MCP adoption wave.

## What's Good

**Three transport protocols.** This is Qdrant's strongest differentiator. It's the only vector database MCP server supporting stdio, SSE, and Streamable HTTP. [Chroma](/reviews/chroma-mcp-server/) is stdio-only. [Pinecone](https://github.com/pinecone-io/pinecone-mcp) is stdio-only. [Weaviate](https://github.com/weaviate/mcp-server-weaviate) is stdio-only. For team environments where multiple developers or agents need access to the same vector store through a shared MCP endpoint, Qdrant is currently the only option.

**Local embedded mode.** `QDRANT_LOCAL_PATH` runs Qdrant in-process — no separate database server, no Docker, no cloud account. Your agent gets persistent semantic memory with zero infrastructure. This is the lowest-friction path to giving an AI agent long-term memory we've seen in any MCP server.

**Extensible class architecture.** Since v0.8.0, the server is implemented as an inheritable `QdrantMCPServer` Python class. Developers can subclass it to build project-specific MCP servers — the official [mcp-for-docs](https://github.com/qdrant/mcp-for-docs) is a read-only documentation search server built this way. This "server as framework" approach is unique among vector DB MCP servers and has spawned a healthy ecosystem of community forks with OpenAI embeddings, knowledge graph capabilities, and RAG-focused variants.

**Highest community adoption.** 1,300 stars and 242 forks — more than double Chroma MCP's 515 stars, and 23x Pinecone MCP's 59 stars. PyPI downloads hit ~20.7K/week (~81.8K/month) with daily spikes above 11K, showing strong organic adoption. The ecosystem includes at least 5 notable community extensions: `mcp-for-docs` (official, read-only documentation search), `mhalder/qdrant-mcp-server` (OpenAI/Cohere/Voyage AI embeddings), `delorenj/mcp-qdrant-memory` (knowledge graphs), `wrediam/better-qdrant-mcp-server` (enhanced features), and `ancoleman/qdrant-rag-mcp` (RAG-focused). Google's Agent Development Kit (ADK) lists it as an official integration.

**Customizable tool descriptions.** Being able to change how the tools present themselves to the LLM is subtle but powerful. The same server becomes a "personal notes store," a "code snippet library," or a "documentation search engine" just by changing two environment variables. This shapes agent behavior without code changes.

## What's Not

**Only two tools.** This is the server's defining limitation. You can store and you can find — but you cannot delete, update, list collections, create collections with custom parameters, manage indexes, or do batch operations. If your agent stores incorrect information, there's no MCP tool to remove it. Issue [#74](https://github.com/qdrant/mcp-server-qdrant/issues/74) and [#101](https://github.com/qdrant/mcp-server-qdrant/issues/101) have been open for months requesting delete capability, with active community discussion but no implementation.

**No collection management.** Collections auto-create when you first store to them, using default settings. No control over HNSW parameters, distance metrics, or index configuration through the MCP interface. Compare this to [Chroma MCP](/reviews/chroma-mcp-server/) which offers full collection CRUD, HNSW tuning, and collection forking.

**FastEmbed-only embeddings by default.** The default embedding model is `sentence-transformers/all-MiniLM-L6-v2` via FastEmbed. v0.8.1 added custom embedding provider support, but the documentation is sparse and community forks exist specifically because people need OpenAI, Cohere, or Voyage AI embeddings. Chroma supports 6 embedding providers out of the box.

**Semantic search only.** `qdrant-find` does vector similarity search — period. No full-text search, no regex matching, no metadata-only filtering. Chroma's single `query_documents` tool supports all three search types. If your agent needs to find documents by exact content match or metadata criteria, this server can't help.

**22 open issues, 21 open PRs, stalling momentum.** The community has been asking for delete capability, more tools, flexible payload schemas, and image storage support. These aren't exotic feature requests — they're table stakes for a database management tool. Community PRs for delete, Gemini embeddings, OpenAI embeddings, hybrid search, and tool annotations sit unmerged. Six releases over 12 months (v0.5.2 through v0.8.1) followed by three months of silence suggests the project has lost momentum — even as Qdrant core shipped v1.17.0 with major features.

**No OAuth or MCP-level authentication.** While the Qdrant database connection is secured via API key, the MCP server itself has no authentication layer. If you expose the server via SSE or Streamable HTTP, anyone who can reach the endpoint can store and search your data. The broader MCP ecosystem saw 30+ CVEs filed against MCP servers in Jan-Feb 2026, and a February 2026 report flagged 8,000+ exposed MCP servers. No CVEs have targeted this server specifically, but issue [#115](https://github.com/qdrant/mcp-server-qdrant/issues/115) (Mar 4, 2026) requests a security policy. Compare to [Neon](/reviews/neon-mcp-server/) or [Supabase](/reviews/supabase-mcp-server/) which use OAuth 2.1 for the MCP connection itself.

## How It Compares

| Feature | Qdrant MCP | Chroma MCP | Pinecone MCP | Milvus MCP | Weaviate MCP |
|---------|-----------|------------|--------------|------------|--------------|
| **Stars** | 1,300 | 515 | 59 | 222 | 161 |
| **Tools** | 2 | 13 | 9 | 11 | 2 |
| **Transport** | stdio, SSE, streamable-http | stdio only | stdio | stdio, SSE | stdio |
| **Search types** | Semantic only | Vector + full-text + regex | Text + metadata | Hybrid | Hybrid |
| **Collection mgmt** | Auto-create only | Full CRUD + fork | Index management | Full CRUD | Insert + query |
| **Delete capability** | No | Yes | Yes | Yes | No |
| **Embedding options** | FastEmbed (default) | 6 providers | Integrated | Not specified | Not specified |
| **Local mode** | Yes (embedded) | Yes (4 modes) | No (cloud only) | No | Yes (self-hosted) |
| **Language** | Python | Python | TypeScript | Python | Go |

The vector DB MCP landscape has a clear split: Chroma and Milvus offer comprehensive database management (13 and 11 tools respectively), while Qdrant and Weaviate take a minimal "just store and search" approach (2 tools each). Pinecone sits in the middle at 9 tools but is cloud-only.

Qdrant's advantage is transport protocol support — it's the only server in this comparison that works as a remote MCP endpoint via SSE or Streamable HTTP. If you need a shared vector memory that multiple agents or developers can access over the network, Qdrant is currently the only first-party option.

But for solo development or projects where you need your agent to actively manage vector infrastructure — creating collections with specific parameters, updating documents, deleting stale data — [Chroma MCP](/reviews/chroma-mcp-server/) offers a significantly more capable experience despite its stdio-only limitation.

## The Bigger Picture

Qdrant's MCP server reveals an interesting philosophical divide in how vendors approach the AI tools space. Some servers, like [Stripe](/reviews/stripe-mcp-server/) (25 tools) or [Supabase](/reviews/supabase-mcp-server/) (8 tool groups), try to expose their platform's full capability through MCP. Others, like Qdrant, deliberately constrain the interface to a specific use case — in this case, semantic memory.

The "server as semantic memory" positioning is clever. Your agent doesn't need to understand Qdrant's collection API, HNSW indexing, or embedding dimensions. It just calls `qdrant-store` and `qdrant-find`. The embedding happens transparently, the collection auto-creates, and search returns relevant results. For the use case of giving an AI agent persistent, searchable memory, this is arguably the right level of abstraction.

The problem is that this level of abstraction breaks down the moment you need more control. What happens when the auto-created collection uses the wrong distance metric? What if your agent stores duplicates and needs to clean up? What if you want to switch embedding models and need to re-index? The Qdrant API supports all of these operations — the MCP server simply doesn't expose them.

The extensible `QdrantMCPServer` class is Qdrant's answer: if you need more tools, build them yourself. It's an honest approach, and the community has responded with multiple forks adding the features the official server lacks. But it means the official server is a starting point rather than a complete solution — and the community extensions aren't maintained by Qdrant, adding supply chain risk.

The three-transport-protocol support is a genuine strategic advantage that may matter more over time. As the MCP ecosystem moves toward remote servers with shared endpoints, Qdrant is already there. The 1,300 GitHub stars, Google ADK integration, and ~20.7K weekly PyPI downloads suggest the developer community values this server despite its minimal tool set.

But the growing gap between Qdrant core and the MCP server is concerning. Qdrant v1.17.0 (Feb 2026) shipped relevance feedback queries, weighted RRF for hybrid search, audit logging, and major latency improvements — none exposed through MCP. The core database is advancing rapidly while the MCP interface remains frozen at two tools. Meanwhile, 21 community PRs sit unmerged, including delete capability, Gemini and OpenAI embeddings, hybrid search, and tool annotations. The server risks becoming a bottleneck — the most popular vector DB MCP server by adoption, but increasingly behind the database it's supposed to expose.

## Rating: 3/5

The Qdrant MCP server earns a 3/5 for being the most adopted vector database MCP server (~20.7K weekly PyPI downloads) with the best transport protocol support in the category — stdio, SSE, and Streamable HTTP in a space where every competitor is stdio-only. The extensible class architecture and embedded local mode are genuine innovations. But only 2 tools with no delete, no update, no collection management, and FastEmbed-only embeddings make this too minimal for production use. Three months without a release while Qdrant core shipped v1.17.0, and 21 unmerged community PRs, raise questions about maintenance velocity. The server solves the "give my agent memory" use case well, but falls short as a database management tool — and the gap is widening.

**Use this if:** You need persistent semantic memory for your AI agent, want remote MCP transport for team access, or plan to build a custom MCP server using the extensible class architecture.

**Skip this if:** You need your agent to manage vector database infrastructure (collections, indexes, embeddings), you need delete or update capability, or you want comprehensive search options beyond semantic similarity.

*This review was researched and written by an AI agent (Claude Opus 4.6, Anthropic) and has not been independently verified by a human editor. We have not tested this MCP server hands-on. All claims are based on publicly available documentation, GitHub data, and community sources as of March 2026. [Rob Nugen](https://robnugen.com) oversees this project. Last updated 2026-03-22.*
