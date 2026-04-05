---
title: "Best Vector Database MCP Servers in 2026"
date: 2026-03-22T18:00:00+09:00
description: "Chroma vs Qdrant vs Pinecone vs Milvus — which vector database MCP server should you use? We compare every official server, their tool counts, transport support, and real tradeoffs."
og_description: "The vector DB MCP space is young and fragmented. Here's the honest comparison: Chroma leads on tools, Qdrant on adoption, Pinecone on search, and Milvus on breadth. Rating, tradeoffs, and recommendations."
content_type: "Comparison"
card_description: "Which vector database MCP server should you use? We compare Chroma, Qdrant, Pinecone, Milvus, Weaviate, and LanceDB — tools, transport, tradeoffs, and honest recommendations."
last_refreshed: 2026-04-05
---

Vector databases are the infrastructure behind RAG, semantic search, and AI memory — and every major vendor now has an MCP server. The problem: they're all at different stages of maturity, with wildly different approaches to what "vector database MCP" even means.

Some give you full collection management. Others give you two tools and call it done. Some only work with their own cloud service. Others run locally with zero infrastructure. The right choice depends on what you're actually trying to do — and whether the MCP server can keep up with the database behind it.

**⚠️ Security note (April 2026):** This category has active security concerns. Chroma's MCP server has an unpatched SQL injection vulnerability affecting 8 of its tools. The underlying Milvus database has CVE-2026-26190 (CVSS 9.8), an unauthenticated REST API exploit. An [ecosystem-wide audit](https://arxiv.org/abs/2504.03767) of 8,000+ MCP servers found 36.7% had SSRF vulnerabilities. See individual server sections for details.

We've [reviewed Chroma](/reviews/chroma-mcp-server/) (3.5/5), [Milvus](/reviews/milvus-mcp-server/) (3.5/5), [Qdrant](/reviews/qdrant-mcp-server/) (3/5), and [Pinecone](/reviews/pinecone-mcp-server/) (3/5) in depth. Here's how every vector database MCP server compares.

## The Contenders

| Server | Stars | Tools | Transport | Best For |
|--------|-------|-------|-----------|----------|
| [Chroma MCP](/reviews/chroma-mcp-server/) | 529 | 12 | stdio | Full vector DB management ⚠️ |
| [Qdrant MCP](/reviews/qdrant-mcp-server/) | 1,321 | 2 | stdio, SSE, Streamable HTTP | Semantic memory layer |
| [Pinecone MCP](/reviews/pinecone-mcp-server/) | 62 | 9 | stdio | Cloud vector search with reranking |
| [Milvus MCP](/reviews/milvus-mcp-server/) (Zilliz) | 224 | 14 | stdio, SSE | Self-hosted vector operations |
| Zilliz Cloud MCP | 32 | 16 | stdio, Streamable HTTP | Managed Milvus with cloud controls |
| MongoDB MCP | 989 | 39 | stdio | Full database + vector search |
| Weaviate MCP | 160 | 2 | stdio | Nothing yet (proof of concept) |
| LanceDB MCP | 25 | 3 | stdio | Nothing yet (reference only) |

## Two Philosophies, One Category

The vector database MCP space splits into two camps, and understanding the divide saves you from picking the wrong server.

**Database management servers** give your agent full control: create collections, configure indexes, insert documents, query, update, delete. Chroma (12 tools), Milvus (14 tools), and MongoDB (39 tools, though not vector-specific) take this approach. Your agent can build and manage vector infrastructure from scratch.

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

**⚠️ Security warning (April 2026):** A critical [SQL injection vulnerability](https://github.com/chroma-core/chroma-mcp/issues/62) was reported on April 2, 2026. Eight of the server's tools (62%) pass collection name parameters unsanitized into SQLite queries, enabling a prompt-injection-to-SQL-injection attack chain. This is **unpatched** — the repo has had no commits since September 2025. Additionally, the pinned MCP SDK dependency (v1.6.0) contains known vulnerabilities (CVE-2025-53365, CVE-2025-53366), fixed in MCP SDK v1.10.0+.

**The catch:** Stdio-only transport means no remote MCP connections. Python-only. Currently at v0.2.6 (August 2025) with development effectively **dormant for 7 months**. No community PRs are being merged (4 open PRs pending since late 2025). Query results can bloat your context window — a single query returns full document text, metadata, embeddings, and distances without any way to limit fields.

**Best for:** Developers who need full vector database management through their agent and are comfortable with local Python tooling. **Exercise caution** — sanitize collection names in your workflow until the SQL injection is patched.

### Qdrant MCP — Most Adopted (3/5)

**[Read our full review](/reviews/qdrant-mcp-server/)**

[Qdrant's official MCP server](https://github.com/qdrant/mcp-server-qdrant) takes the opposite approach from Chroma. Two tools: `qdrant-store` and `qdrant-find`. That's it. No collection management, no document updates, no deletes, no index tuning.

**What sets it apart:**
- Only vector DB MCP server supporting all three transports: stdio, SSE, and Streamable HTTP
- Local embedded mode via `QDRANT_LOCAL_PATH` — zero infrastructure semantic memory
- Extensible `QdrantMCPServer` class for building custom servers on top
- Customizable tool descriptions via environment variables
- 1,321 GitHub stars and 256 forks — most adopted by far

**The catch:** Two tools is genuinely limiting. You can't delete stored information (open issues [#74](https://github.com/qdrant/mcp-server-qdrant/issues/74) and [#101](https://github.com/qdrant/mcp-server-qdrant/issues/101)) — though community PRs for [delete](https://github.com/qdrant/mcp-server-qdrant/pull/116) and [edit](https://github.com/qdrant/mcp-server-qdrant/pull/121) tools were submitted in late March 2026 and await review. No collection management means you can't organize information by project or topic through the MCP interface. FastEmbed-only embedding by default. Last release (v0.8.1) was December 2025.

**Best for:** Adding persistent semantic memory to coding agents. Not for managing vector infrastructure.

### Pinecone MCP — Best Search Quality (3/5)

**[Read our full review](/reviews/pinecone-mcp-server/)**

[Pinecone's official Developer MCP server](https://github.com/pinecone-io/pinecone-mcp) (62 stars, v0.2.1) sits between the database-management and semantic-memory philosophies. Nine tools focus on search quality over infrastructure control — cascading search across indexes, built-in reranking, and documentation search without authentication.

**What sets it apart:**
- `cascading-search` — the only vector DB MCP server with cross-index search and automatic deduplication
- `rerank-documents` — built-in reranking using Pinecone's specialized models
- `search-docs` — query Pinecone documentation without an API key (like Stripe's doc search)
- Integrated embedding means zero embedding configuration — pass text, Pinecone handles the rest

**The catch:** Cloud-only with no local mode. Only works with integrated embedding indexes — existing indexes with custom embeddings (OpenAI, Cohere, etc.) are invisible to the server. No delete, no update, no namespace management. Stdio transport for a cloud-only service. Three separate Pinecone MCP servers (Developer, Assistant, Claude Code Plugin) create confusion.

**Best for:** Pinecone users with integrated embedding indexes who want AI-assisted search with reranking and cross-index queries.

### Milvus MCP — Best Hybrid Search (3.5/5)

**[Read our full review](/reviews/milvus-mcp-server/)**

[Zilliz's Milvus MCP server](https://github.com/zilliztech/mcp-server-milvus) (224 stars) brings the most popular open-source vector database (40,000+ GitHub stars) to MCP with 14 tools — the highest tool count among dedicated vector database MCP servers.

**What sets it apart:**
- Six search modes — text, vector, hybrid, text similarity, filter queries, plus the new `get_collection_info` tool — more than any other vector DB MCP server
- Native hybrid search combining keyword precision with semantic recall in one query (Milvus 2.5+)
- Memory management controls (`load_collection`, `release_collection`) — unique in the category
- Full delete capability via filter expressions (unlike Qdrant and Pinecone)
- Database-level management (`list_databases`, `use_database`) for multi-tenant setups
- Works identically with self-hosted Milvus and Zilliz Cloud
- Stdio and SSE transport

**⚠️ Security warning (April 2026):** The underlying Milvus database has two critical vulnerabilities. [CVE-2026-26190](https://github.com/milvus-io/milvus/security/advisories/GHSA-7ppg-37fh-vcr6) (CVSS 9.8) allows unauthenticated access to the REST API on metrics port 9091, enabling data exfiltration, credential theft, and potential RCE. [CVE-2025-64513](https://github.com/milvus-io/milvus/security/advisories/GHSA-mhjq-8c7m-3f7p) is an authentication bypass via forged HTTP headers. Both are patched in Milvus 2.5.27+ and 2.6.10+. **Ensure your Milvus instance is updated before connecting an MCP server to it.**

**The catch:** No embedded/local mode — requires a running Milvus instance (Docker or Zilliz Cloud). No document update (must delete and re-insert). Pre-release maturity (no versioned releases, only dev builds on PyPI, last commit December 2025). The service hang bug ([#51](https://github.com/zilliztech/mcp-server-milvus/issues/51)) has a workaround merged (try-except blocks in PR #54) but the issue remains technically open. No Streamable HTTP transport. Python-only.

Zilliz also maintains a separate [Zilliz Cloud MCP server](https://github.com/zilliztech/zilliz-mcp-server) (32 stars, 16 tools) that adds cloud management — cluster creation, suspension, metrics — plus Streamable HTTP transport. Both repos have been dormant through Q1 2026.

**Best for:** Teams running Milvus in production who want AI-assisted vector operations, especially hybrid search combining keyword and semantic retrieval. **Patch your Milvus instance first.**

## The Unreviewed Servers

### Weaviate MCP — Too Early

[Weaviate's official MCP server](https://github.com/weaviate/mcp-server-weaviate) (160 stars, 43 forks) has two tools: `insert_one` and `query`. No releases. Written in Go, which is unusual for MCP servers. The README shows placeholder JSON examples. Weaviate has also launched a separate [Docs MCP Server](https://docs.weaviate.io/weaviate/mcp/docs-mcp-server) for documentation access, but the core data server remains unchanged.

Despite the star count (likely from Weaviate's brand recognition), this is a proof of concept, not a usable server. The community [sajal2692/mcp-weaviate](https://github.com/sajal2692/mcp-weaviate) alternative has 11 tools and is more functional, but has minimal adoption.

**Best for:** Nothing yet. Wait for Weaviate to invest in this properly.

### LanceDB MCP — Reference Only

[LanceDB's official MCP server](https://github.com/lancedb/lancedb-mcp-server) (25 stars) has three tools: `ingest_docs`, `retrieve_docs`, and `get_table_details`. Three commits. No releases. Explicitly described as a reference implementation. A community alternative exists at [adiom-data/lance-mcp](https://github.com/adiom-data/lance-mcp).

LanceDB itself is excellent — embedded, serverless, multimodal, Rust-powered — but the MCP tooling is the weakest in this comparison. There's an [open issue](https://github.com/lancedb/lancedb/issues/2341) requesting a more capable server with full CRUD tools.

**Best for:** Nothing yet. The database deserves better MCP support than it currently has.

### MongoDB MCP — General-Purpose with Strong Vector Search

[MongoDB's official MCP server](https://github.com/mongodb-js/mongodb-mcp-server) (989 stars, 211 forks) isn't a dedicated vector database server — it's a full MongoDB MCP with ~39 tools covering database management, Atlas cloud operations, and local cluster management. But its vector search capabilities are increasingly competitive.

**What sets it apart:**
- **Automatic embedding generation** via Voyage AI on insert — no need to pre-compute embeddings, dramatically lowering the barrier to vector search
- Unified vector search index creation alongside regular indexes (behind a feature flag)
- Full CRUD across collections, plus Atlas-specific tools (Performance Advisor, cluster management)
- The sheer breadth: 22 database tools, 14 Atlas tools, 3 local management tools

**The catch:** This is a general-purpose MongoDB server, not a purpose-built vector database MCP. If you only need vector search, the tool surface is overwhelming. Requires MongoDB Atlas for vector search features (the vector search index type is an Atlas feature). No dedicated semantic memory abstraction like Qdrant's store/find simplicity.

**Best for:** Teams already using MongoDB who want to add vector search alongside their existing document database operations. Not ideal if vector search is your primary use case.

### Elasticsearch MCP — Deprecated

[Elastic's official MCP server](https://github.com/elastic/mcp-server-elasticsearch) (639 stars) had 5 tools including full-text search, ES|QL, and mapping inspection. However, as of Elasticsearch 9.2+, **this server is deprecated** in favor of the built-in [Elastic Agent Builder MCP endpoint](https://www.elastic.co/docs/solutions/search/mcp). Only critical security fixes will be applied to the standalone server.

This signals a broader trend: vector databases are beginning to embed MCP support directly into their products rather than maintaining separate MCP server repositories.

**Best for:** Migrate to the Elastic Agent Builder endpoint if you're on Elasticsearch 9.2+.

## Feature Comparison

| Feature | Chroma | Qdrant | Pinecone | Milvus | MongoDB | Weaviate | LanceDB |
|---------|--------|--------|----------|--------|---------|----------|---------|
| **Tools** | 12 | 2 | 9 | 14 | 39 | 2 | 3 |
| **Collection CRUD** | Full | None | Read-only | Full | Full | Insert only | Read-only |
| **Document insert** | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| **Document delete** | Yes | No | No | Yes | Yes | No | No |
| **Document update** | Yes | No | No | No | Yes | No | No |
| **Semantic search** | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| **Full-text search** | Yes | No | No | Yes | Yes | No | No |
| **Hybrid search** | No | No | No | Yes | Yes | Yes | No |
| **Reranking** | No | No | Yes | No | No | No | No |
| **Auto-embeddings** | 6 providers | FastEmbed | Integrated | External | Voyage AI | External | Built-in |
| **Local/embedded mode** | Yes | Yes | No | No | Yes (local) | Yes | Yes |
| **Cloud mode** | Yes | Yes | Yes (only) | Yes | Yes (Atlas) | Yes | No |
| **stdio** | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| **SSE** | No | Yes | No | Yes | No | No | No |
| **Streamable HTTP** | No | Yes | No | No | No | No | No |
| **OAuth** | No | No | No | No | No | No | No |
| **Security issues** | ⚠️ SQLi | None | None | ⚠️ CVEs | None | None | None |
| **GitHub stars** | 529 | 1,321 | 62 | 224 | 989 | 160 | 25 |
| **Language** | Python | Python | TypeScript | Python | TypeScript | Go | Python |
| **Rating** | 3.5/5 | 3/5 | 3/5 | 3.5/5 | — | — | — |
| **Maturity** | v0.2.6 ⚠️ | v0.8.1 | v0.2.1 | Pre-release | Active | PoC | Reference |

## The pgvector Gap

Notably absent from this comparison: a dedicated pgvector MCP server. PostgreSQL's vector extension is one of the most popular ways to add vector search to existing applications, but there's no clear winner in the MCP space.

The options are fragmented: [yusuf/mcp-pgvector-server](https://lobehub.com/mcp/yusuf-mcp-pgvector-server) for dedicated pgvector search, [neverinfamous/postgres-mcp](https://github.com/neverinfamous/postgres-mcp) for full Postgres with pgvector and 8 extensions support, [stuzero/pg-mcp-server](https://github.com/stuzero/pg-mcp-server) for enhanced Postgres with pgvector awareness, and [Knuckles-Team/vector-mcp](https://github.com/Knuckles-Team/vector-mcp) (9 stars) as a multi-database MCP supporting pgvector alongside ChromaDB, Qdrant, Couchbase, and MongoDB.

If you're already using PostgreSQL with pgvector, your best option today is a general Postgres MCP server rather than a dedicated vector database MCP server. This gap will likely close as the ecosystem matures — and the emergence of unified/federated MCP servers like [Knuckles-Team/vector-mcp](https://github.com/Knuckles-Team/vector-mcp) and MindsDB's universal MCP (which federates across Pinecone, Weaviate, and Qdrant) suggests the future may be multi-backend rather than vendor-specific.

## Our Recommendations

### For full vector database management: Chroma MCP (with caveats)

If you need your agent to create collections, configure indexes, manage documents, and run queries — Chroma has the most complete lifecycle coverage. Twelve tools, four deployment modes, six embedding providers. **However**, the unpatched SQL injection vulnerability (April 2026) and 7 months of dormancy are serious concerns. If you use Chroma MCP, sanitize collection name inputs in your workflow and monitor [issue #62](https://github.com/chroma-core/chroma-mcp/issues/62) for a fix. Milvus MCP (14 tools) is now a viable alternative for full management if you can run a Milvus instance.

### For semantic memory: Qdrant MCP

If you want to add persistent memory to a coding agent without thinking about vector infrastructure, Qdrant's two-tool approach is the right abstraction. Store text, find it later by meaning. The broadest transport support (stdio, SSE, Streamable HTTP) means it works in more deployment scenarios than any competitor. Just accept that you can't delete anything yet.

### For search quality: [Pinecone MCP](/reviews/pinecone-mcp-server/)

If search quality matters more than flexibility — cascading search across indexes, built-in reranking, integrated embeddings — Pinecone's server is purpose-built for this. The limitation to Pinecone's integrated embedding models is significant, but if you're starting fresh on Pinecone, the search experience is the best in the category.

### For self-hosted infrastructure: [Milvus MCP](/reviews/milvus-mcp-server/)

If you're running Milvus and need full management through MCP — collections, inserts, deletes, hybrid search — the [Milvus server](/reviews/milvus-mcp-server/) (3.5/5) has the best self-hosted story. Fourteen tools with category-leading six search modes and both stdio and SSE transport. The lack of versioned releases is a concern, but the tool coverage is solid. **Critical: ensure your Milvus instance is updated to 2.5.27+ or 2.6.10+ to patch CVE-2026-26190.**

### For existing MongoDB users: MongoDB MCP

If you're already on MongoDB Atlas and want to add vector search alongside your existing database operations, the [MongoDB MCP server](https://github.com/mongodb-js/mongodb-mcp-server) (989 stars, ~39 tools) is the most actively maintained server in this category. Automatic embedding generation via Voyage AI removes the biggest friction point in vector search setup. Overkill if vector search is your only need.

### For everything else: Wait

Weaviate and LanceDB both have MCP servers that aren't ready for real use. If you're committed to either database, use their native SDKs and check back in six months. The community alternatives are more functional but lack the maintenance guarantees of first-party servers.

## Decision Flowchart

**What's your primary use case?**

→ **Adding memory to a coding agent?** Use [Qdrant MCP](/reviews/qdrant-mcp-server/) for the simplest path, or [Chroma MCP](/reviews/chroma-mcp-server/) if you need to organize memories into collections.

→ **Building a RAG pipeline?** Use [Chroma MCP](/reviews/chroma-mcp-server/) for local development with full collection management, [Milvus MCP](/reviews/milvus-mcp-server/) for hybrid search (keyword + semantic), or [Pinecone MCP](/reviews/pinecone-mcp-server/) for cloud deployment with reranking.

→ **Managing existing vector infrastructure?** Match the server to your database: [Milvus MCP](/reviews/milvus-mcp-server/) for Milvus (patch your instance first), [Pinecone MCP](/reviews/pinecone-mcp-server/) for Pinecone (integrated embeddings only), Qdrant MCP for Qdrant, [MongoDB MCP](https://github.com/mongodb-js/mongodb-mcp-server) for MongoDB Atlas. Chroma MCP covers Chroma across all four deployment modes (watch the SQL injection issue).

→ **Need remote MCP (not stdio)?** [Qdrant MCP](/reviews/qdrant-mcp-server/) is the only option with all three transports. [Milvus MCP](/reviews/milvus-mcp-server/) has SSE. Zilliz Cloud MCP has Streamable HTTP. Everyone else is stdio-only.

→ **Need zero infrastructure?** [Qdrant MCP](/reviews/qdrant-mcp-server/) with `QDRANT_LOCAL_PATH` or [Chroma MCP](/reviews/chroma-mcp-server/) in persistent mode — both run embedded without a separate server process.

## The Bottom Line

The vector database MCP space is young — and April 2026 reveals a category under strain. The two highest-rated dedicated servers — Chroma and [Milvus](/reviews/milvus-mcp-server/) at 3.5/5 each — both have active security concerns (Chroma: unpatched SQL injection; Milvus: critical CVEs on the underlying database). Chroma has been dormant for 7 months. Milvus hasn't committed since December 2025. The most adopted server — Qdrant at 1,321 stars — still has just two tools, with delete/edit PRs waiting for review. No dedicated vector DB MCP server in this category supports OAuth. None have reached 1.0.

Two trends are emerging. First, **general-purpose database MCP servers are eating into this category** — MongoDB's 39-tool server with automatic Voyage AI embeddings is more actively maintained than any dedicated vector DB server here. Elasticsearch has deprecated its standalone MCP server entirely in favor of built-in Agent Builder support. The future may not be "vector database MCP servers" as a separate category. Second, **federated/multi-backend approaches** like Knuckles-Team's vector-mcp and MindsDB's universal MCP are abstracting away the vendor choice entirely.

Pick the server that matches your database — but check the security warnings first. If you don't have a database yet, [Qdrant](/reviews/qdrant-mcp-server/) remains the safest starting point for semantic memory. For full management, [Milvus](/reviews/milvus-mcp-server/) (14 tools) now edges out Chroma on capability — just ensure your instance is patched. And if you're already on MongoDB, its MCP server may be all you need.

For how vector databases fit into the broader MCP ecosystem, see our [mega-comparison of all MCP servers](/guides/best-mcp-servers/) and our [database MCP server comparison](/guides/best-database-mcp-servers/).
