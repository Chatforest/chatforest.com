---
title: "Best Vector Database MCP Servers in 2026"
date: 2026-03-22T18:00:00+09:00
description: "Chroma vs Qdrant vs Pinecone vs Milvus — which vector database MCP server should you use? We compare every official server, their tool counts, transport support, and real tradeoffs."
og_description: "The vector DB MCP space is young and fragmented. Here's the honest comparison: Chroma leads on tools, Qdrant on adoption, Pinecone on search, and Milvus on breadth. Rating, tradeoffs, and recommendations."
content_type: "Comparison"
card_description: "Which vector database MCP server should you use? We compare Chroma, Qdrant, Pinecone, Milvus, Weaviate, and LanceDB — tools, transport, tradeoffs, and honest recommendations."
last_refreshed: 2026-03-22
---

Vector databases are the infrastructure behind RAG, semantic search, and AI memory — and every major vendor now has an MCP server. The problem: they're all at different stages of maturity, with wildly different approaches to what "vector database MCP" even means.

Some give you full collection management. Others give you two tools and call it done. Some only work with their own cloud service. Others run locally with zero infrastructure. The right choice depends on what you're actually trying to do — and whether the MCP server can keep up with the database behind it.

We've [reviewed Chroma](/reviews/chroma-mcp-server/) (3.5/5), [Milvus](/reviews/milvus-mcp-server/) (3.5/5), [Qdrant](/reviews/qdrant-mcp-server/) (3/5), and [Pinecone](/reviews/pinecone-mcp-server/) (3/5) in depth. Here's how every vector database MCP server compares.

## The Contenders

| Server | Stars | Tools | Transport | Best For |
|--------|-------|-------|-----------|----------|
| [Chroma MCP](/reviews/chroma-mcp-server/) | 515 | 12 | stdio | Full vector DB management |
| [Qdrant MCP](/reviews/qdrant-mcp-server/) | 1,300 | 2 | stdio, SSE, Streamable HTTP | Semantic memory layer |
| [Pinecone MCP](/reviews/pinecone-mcp-server/) | 59 | 9 | stdio | Cloud vector search with reranking |
| [Milvus MCP](/reviews/milvus-mcp-server/) (Zilliz) | 223 | 12 | stdio, SSE | Self-hosted vector operations |
| Zilliz Cloud MCP | 32 | 16 | stdio, Streamable HTTP | Managed Milvus with cloud controls |
| Weaviate MCP | 161 | 2 | stdio | Nothing yet (proof of concept) |
| LanceDB MCP | 23 | 3 | stdio | Nothing yet (reference only) |

## Two Philosophies, One Category

The vector database MCP space splits into two camps, and understanding the divide saves you from picking the wrong server.

**Database management servers** give your agent full control: create collections, configure indexes, insert documents, query, update, delete. Chroma (12 tools) and Milvus (12 tools) take this approach. Your agent can build and manage vector infrastructure from scratch.

**Semantic memory servers** hide the database entirely. Your agent stores text and retrieves it by meaning. Qdrant (2 tools) is the purest version of this — there's no collection management, no index configuration, no delete. The server handles embeddings, storage, and retrieval behind the scenes.

Pinecone (9 tools) sits between the two. You can list and describe indexes, but creation is limited to Pinecone's integrated embedding models. The focus is on search quality — cascading search across indexes, built-in reranking — not infrastructure management.

Which philosophy you want depends on your use case. Building a RAG pipeline that needs careful tuning? You want database management. Adding persistent memory to a coding agent? Semantic memory is simpler and sufficient.

## The Reviewed Servers

### Chroma MCP — Most Comprehensive (3.5/5)

**[Read our full review](/reviews/chroma-mcp-server/)**

[Chroma's official MCP server](https://github.com/chroma-core/chroma-mcp) has 12 tools — tied with Milvus for the most in the category. Seven handle collection management (create, list, peek, get info, count, modify, delete), five handle document operations (add, query, get, update, delete). It's the only server that lets your agent configure HNSW index parameters at collection creation time.

**What sets it apart:**
- Four deployment modes: ephemeral (in-memory), persistent (local files), self-hosted HTTP, and Chroma Cloud
- Six embedding providers: Default, Cohere, OpenAI, Jina, VoyageAI, Roboflow
- Combined semantic + full-text + regex search through a single `query_documents` tool

**The catch:** Stdio-only transport means no remote MCP connections. Python-only. Currently at v0.2.6 (August 2025) with development slowing. Query results can bloat your context window — a single query returns full document text, metadata, embeddings, and distances without any way to limit fields.

**Best for:** Developers who need full vector database management through their agent and are comfortable with local Python tooling.

### Qdrant MCP — Most Adopted (3/5)

**[Read our full review](/reviews/qdrant-mcp-server/)**

[Qdrant's official MCP server](https://github.com/qdrant/mcp-server-qdrant) takes the opposite approach from Chroma. Two tools: `qdrant-store` and `qdrant-find`. That's it. No collection management, no document updates, no deletes, no index tuning.

**What sets it apart:**
- Only vector DB MCP server supporting all three transports: stdio, SSE, and Streamable HTTP
- Local embedded mode via `QDRANT_LOCAL_PATH` — zero infrastructure semantic memory
- Extensible `QdrantMCPServer` class for building custom servers on top
- Customizable tool descriptions via environment variables
- 1,300 GitHub stars and 243 forks — most adopted by far

**The catch:** Two tools is genuinely limiting. You can't delete stored information (open issues [#74](https://github.com/qdrant/mcp-server-qdrant/issues/74) and [#101](https://github.com/qdrant/mcp-server-qdrant/issues/101)). No collection management means you can't organize information by project or topic through the MCP interface. FastEmbed-only embedding by default.

**Best for:** Adding persistent semantic memory to coding agents. Not for managing vector infrastructure.

### Pinecone MCP — Best Search Quality (3/5)

**[Read our full review](/reviews/pinecone-mcp-server/)**

[Pinecone's official Developer MCP server](https://github.com/pinecone-io/pinecone-mcp) (59 stars, v0.2.1) sits between the database-management and semantic-memory philosophies. Nine tools focus on search quality over infrastructure control — cascading search across indexes, built-in reranking, and documentation search without authentication.

**What sets it apart:**
- `cascading-search` — the only vector DB MCP server with cross-index search and automatic deduplication
- `rerank-documents` — built-in reranking using Pinecone's specialized models
- `search-docs` — query Pinecone documentation without an API key (like Stripe's doc search)
- Integrated embedding means zero embedding configuration — pass text, Pinecone handles the rest

**The catch:** Cloud-only with no local mode. Only works with integrated embedding indexes — existing indexes with custom embeddings (OpenAI, Cohere, etc.) are invisible to the server. No delete, no update, no namespace management. Stdio transport for a cloud-only service. Three separate Pinecone MCP servers (Developer, Assistant, Claude Code Plugin) create confusion.

**Best for:** Pinecone users with integrated embedding indexes who want AI-assisted search with reranking and cross-index queries.

### Milvus MCP — Best Hybrid Search (3.5/5)

**[Read our full review](/reviews/milvus-mcp-server/)**

[Zilliz's Milvus MCP server](https://github.com/zilliztech/mcp-server-milvus) (223 stars) brings the most popular open-source vector database (40,000+ GitHub stars) to MCP with 12 tools — the second-highest tool count in the category after Chroma's 13.

**What sets it apart:**
- Five search modes — text, vector, hybrid, text similarity, filter queries — more than any other vector DB MCP server
- Native hybrid search combining keyword precision with semantic recall in one query (Milvus 2.5+)
- Memory management controls (`load_collection`, `release_collection`) — unique in the category
- Full delete capability via filter expressions (unlike Qdrant and Pinecone)
- Works identically with self-hosted Milvus and Zilliz Cloud
- Stdio and SSE transport

**The catch:** No embedded/local mode — requires a running Milvus instance (Docker or Zilliz Cloud). No document update (must delete and re-insert). Pre-release maturity (35 commits, no versioned releases, last updated December 2025). Known service hang bug after errors (#51). No Streamable HTTP transport. Python-only.

Zilliz also maintains a separate [Zilliz Cloud MCP server](https://github.com/zilliztech/zilliz-mcp-server) (32 stars, 16 tools) that adds cloud management — cluster creation, suspension, metrics — plus Streamable HTTP transport.

**Best for:** Teams running Milvus in production who want AI-assisted vector operations, especially hybrid search combining keyword and semantic retrieval.

## The Unreviewed Servers

### Weaviate MCP — Too Early

[Weaviate's official MCP server](https://github.com/weaviate/mcp-server-weaviate) (161 stars) has two tools: `insert_one` and `query`. One commit. No releases. Written in Go, which is unusual for MCP servers. The README shows placeholder JSON examples.

Despite 161 GitHub stars (likely from Weaviate's brand recognition), this is a proof of concept, not a usable server. The community [sajal2692/mcp-weaviate](https://github.com/sajal2692/mcp-weaviate) alternative has 11 tools and is more functional, but has minimal adoption.

**Best for:** Nothing yet. Wait for Weaviate to invest in this properly.

### LanceDB MCP — Reference Only

[LanceDB's official MCP server](https://github.com/lancedb/lancedb-mcp-server) (23 stars) has three tools: `ingest_docs`, `retrieve_docs`, and `get_table_details`. Three commits. No releases. Explicitly described as a reference implementation.

LanceDB itself is excellent — embedded, serverless, multimodal, Rust-powered — but the MCP tooling is the weakest in this comparison. There's an [open issue](https://github.com/lancedb/lancedb/issues/2341) requesting a more capable server with full CRUD tools.

**Best for:** Nothing yet. The database deserves better MCP support than it currently has.

## Feature Comparison

| Feature | Chroma | Qdrant | Pinecone | Milvus | Weaviate | LanceDB |
|---------|--------|--------|----------|--------|----------|---------|
| **Tools** | 12 | 2 | 9 | 12 | 2 | 3 |
| **Collection CRUD** | Full | None | Read-only | Full | Insert only | Read-only |
| **Document insert** | Yes | Yes | Yes | Yes | Yes | Yes |
| **Document delete** | Yes | No | No | Yes | No | No |
| **Document update** | Yes | No | No | No | No | No |
| **Semantic search** | Yes | Yes | Yes | Yes | Yes | Yes |
| **Full-text search** | Yes | No | No | Yes | No | No |
| **Hybrid search** | No | No | No | Yes | Yes | No |
| **Reranking** | No | No | Yes | No | No | No |
| **Embedding config** | 6 providers | FastEmbed | Integrated | External | External | Built-in |
| **Local/embedded mode** | Yes | Yes | No | No | Yes | Yes |
| **Cloud mode** | Yes | Yes | Yes (only) | Yes | Yes | No |
| **stdio** | Yes | Yes | Yes | Yes | Yes | Yes |
| **SSE** | No | Yes | No | Yes | No | No |
| **Streamable HTTP** | No | Yes | No | No | No | No |
| **OAuth** | No | No | No | No | No | No |
| **GitHub stars** | 515 | 1,300 | 59 | 223 | 161 | 23 |
| **Language** | Python | Python | TypeScript | Python | Go | Python |
| **Rating** | 3.5/5 | 3/5 | 3/5 | 3.5/5 | — | — |
| **Maturity** | v0.2.6 | Stable | v0.2.1 | Pre-release | PoC | Reference |

## The pgvector Gap

Notably absent from this comparison: a dedicated pgvector MCP server. PostgreSQL's vector extension is one of the most popular ways to add vector search to existing applications, but there's no clear winner in the MCP space.

The options are fragmented: [yusuf/mcp-pgvector-server](https://lobehub.com/mcp/yusuf-mcp-pgvector-server) for dedicated pgvector search, [neverinfamous/postgres-mcp](https://github.com/neverinfamous/postgres-mcp) for full Postgres with pgvector as one of many supported extensions, and [Knuckles-Team/vector-mcp](https://github.com/Knuckles-Team/vector-mcp) (9 stars) as a multi-database MCP supporting pgvector alongside ChromaDB, Qdrant, and MongoDB.

If you're already using PostgreSQL with pgvector, your best option today is a general Postgres MCP server rather than a dedicated vector database MCP server. This gap will likely close as the ecosystem matures.

## Our Recommendations

### For full vector database management: Chroma MCP

If you need your agent to create collections, configure indexes, manage documents, and run queries — Chroma is the only server that covers the full lifecycle. Twelve tools, four deployment modes, six embedding providers. The stdio-only transport and stalling development are real concerns, but nothing else comes close on capability.

### For semantic memory: Qdrant MCP

If you want to add persistent memory to a coding agent without thinking about vector infrastructure, Qdrant's two-tool approach is the right abstraction. Store text, find it later by meaning. The broadest transport support (stdio, SSE, Streamable HTTP) means it works in more deployment scenarios than any competitor. Just accept that you can't delete anything yet.

### For search quality: [Pinecone MCP](/reviews/pinecone-mcp-server/)

If search quality matters more than flexibility — cascading search across indexes, built-in reranking, integrated embeddings — Pinecone's server is purpose-built for this. The limitation to Pinecone's integrated embedding models is significant, but if you're starting fresh on Pinecone, the search experience is the best in the category.

### For self-hosted infrastructure: [Milvus MCP](/reviews/milvus-mcp-server/)

If you're running Milvus and need full management through MCP — collections, inserts, deletes, hybrid search — the [Milvus server](/reviews/milvus-mcp-server/) (3.5/5) has the best self-hosted story. Twelve tools with category-leading five search modes and both stdio and SSE transport. The lack of versioned releases is a concern, but the tool coverage is solid.

### For everything else: Wait

Weaviate and LanceDB both have MCP servers that aren't ready for real use. If you're committed to either database, use their native SDKs and check back in six months. The community alternatives are more functional but lack the maintenance guarantees of first-party servers.

## Decision Flowchart

**What's your primary use case?**

→ **Adding memory to a coding agent?** Use [Qdrant MCP](/reviews/qdrant-mcp-server/) for the simplest path, or [Chroma MCP](/reviews/chroma-mcp-server/) if you need to organize memories into collections.

→ **Building a RAG pipeline?** Use [Chroma MCP](/reviews/chroma-mcp-server/) for local development with full collection management, [Milvus MCP](/reviews/milvus-mcp-server/) for hybrid search (keyword + semantic), or [Pinecone MCP](/reviews/pinecone-mcp-server/) for cloud deployment with reranking.

→ **Managing existing vector infrastructure?** Match the server to your database: [Milvus MCP](/reviews/milvus-mcp-server/) for Milvus, [Pinecone MCP](/reviews/pinecone-mcp-server/) for Pinecone (integrated embeddings only), Qdrant MCP for Qdrant. Chroma MCP covers Chroma across all four deployment modes.

→ **Need remote MCP (not stdio)?** [Qdrant MCP](/reviews/qdrant-mcp-server/) is the only option with all three transports. [Milvus MCP](/reviews/milvus-mcp-server/) has SSE. Zilliz Cloud MCP has Streamable HTTP. Everyone else is stdio-only.

→ **Need zero infrastructure?** [Qdrant MCP](/reviews/qdrant-mcp-server/) with `QDRANT_LOCAL_PATH` or [Chroma MCP](/reviews/chroma-mcp-server/) in persistent mode — both run embedded without a separate server process.

## The Bottom Line

The vector database MCP space is young. The two best servers here — Chroma and [Milvus](/reviews/milvus-mcp-server/) at 3.5/5 each — are now tied at 12 tools apiece but have significant gaps (Chroma: no remote transport; Milvus: no local mode, pre-release maturity). The most adopted server — Qdrant at 1,300 stars — has just two tools. No server in this category supports OAuth authentication. None have reached 1.0.

But the trajectory is clear. Every major vector database vendor has planted a flag in the MCP ecosystem. The servers that invest in tool coverage, transport flexibility, and developer experience will pull ahead. Right now, Chroma leads on deployment flexibility, Milvus leads on search breadth (hybrid search), Qdrant leads on simplicity and reach, and Pinecone leads on search quality.

Pick the server that matches your database. If you don't have a database yet and want the most capable MCP experience, start with [Chroma](/reviews/chroma-mcp-server/). If you just want semantic memory with zero friction, start with [Qdrant](/reviews/qdrant-mcp-server/).

For how vector databases fit into the broader MCP ecosystem, see our [mega-comparison of all MCP servers](/guides/best-mcp-servers/) and our [database MCP server comparison](/guides/best-database-mcp-servers/).
