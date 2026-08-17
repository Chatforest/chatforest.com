---
title: "Vector Database & Embedding MCP Servers — Qdrant, Chroma, Milvus, Pinecone, Weaviate, Redis, LanceDB, pgvector, and More"
date: 2026-03-20T14:00:00+09:00
description: "Vector database and embedding MCP servers let AI agents store, search, and manage vector embeddings through the Model Context Protocol. We reviewed 25+ servers across 10+ platforms."
og_description: "Vector database MCP servers: Redis OFFICIAL (571 stars, vector search + data management), Qdrant (1,500+ stars, configurable filters), Weaviate v1.37 BUILT-IN MCP (first DB-native MCP), Chroma (580+ stars, 12 tools), Milvus (240+ stars, 12 tools), Pinecone (remote hosted Assistant MCP), Turbopuffer OFFICIAL (npm), claude-context (12,400+ stars, code search via Milvus). 25+ servers. Rating: 4.5/5."
content_type: "Review"
card_description: "Vector database and embedding MCP servers for AI-powered semantic search, RAG pipelines, and agent memory. **Redis ships an official server** — [redis/mcp-redis](https://github.com/redis/mcp-redis) (571 stars) provides vector index creation and vector similarity search, plus full Redis data structure management. Official and Docker-ready, though not the highest-starred server in this category. Plus redis/agent-memory-server's V0 reference implementation adds semantic/keyword/hybrid agent memory via FastMCP (Redis's current supported production path for agent memory has since moved to the managed Redis Iris service). **Weaviate v1.37 ships BUILT-IN MCP** — the first vector database to embed MCP directly into the database itself. Streamable HTTP at /v1/mcp, schema inspection, hybrid search, write data, enforced by standard auth. No separate server needed. **Qdrant leads dedicated vector DB adoption** — qdrant/mcp-server-qdrant (1,500+ stars) has configurable filters on its find tool and an inheritable QdrantMCPServer class for building custom MCP servers. **Chroma holds at 580+ stars** — 12 tools across four deployment modes remain the most comprehensive tool set. **Milvus ecosystem expands** — mcp-server-milvus (240+ stars) plus zilliz-mcp-server for Zilliz Cloud management, and zilliztech/claude-context (12,400+ stars) for code search powered by Milvus — the highest-starred server in this entire category. **Pinecone goes remote** — every Pinecone Assistant is now a hosted MCP endpoint at /mcp/assistants/<name>, zero infrastructure. **Turbopuffer arrives** — official @turbopuffer/turbopuffer-mcp npm package with Code Mode sandbox execution, filling another gap. **Universal vector MCP** — Knuckles-Team/vector-mcp supports ChromaDB, Couchbase, MongoDB, Qdrant, and PGVector in one server. **Notable gaps closing** — Redis Vector Search FILLED, Turbopuffer FILLED, Weaviate built-in FILLED. Still no Vespa MCP server, no FAISS (library not service). The category earns 4.5/5 — broad official vendor support (Redis, Qdrant, Chroma, Milvus, Pinecone, Weaviate, LanceDB, Turbopuffer all ship first-party servers), Weaviate pioneering database-native MCP, and claude-context's 12,400+ stars for code search via Milvus all represent major maturation. What holds it back: tool coverage is still uneven across vendors, batch operations remain limited, and the RAG pipeline layer is still fragmented."
last_refreshed: 2026-08-17
sources_audited: 2026-08-17
---

Vector database MCP servers let AI agents store embeddings, run semantic searches, manage collections, and build retrieval-augmented generation (RAG) pipelines — all through the Model Context Protocol. Instead of writing Python scripts to initialize clients, create indexes, and query vectors, your agent handles these operations conversationally. Part of our **[Databases MCP category](/categories/databases/)**.

This is the category that makes AI memory and knowledge retrieval work. Vector databases are the backbone of RAG, agent memory, semantic search, and recommendation systems. Every major vector database vendor now ships an official MCP server — and one (Weaviate) now embeds MCP directly into the database itself.

This review covers MCP servers for **dedicated vector databases** (Qdrant, Chroma, Milvus, Pinecone, Weaviate, LanceDB, Turbopuffer), **vector-enabled traditional databases** (Redis, pgvector for PostgreSQL, MongoDB Atlas), and **RAG-focused servers** that combine vector storage with document processing. For search engines with vector capabilities (Elasticsearch, OpenSearch, Meilisearch), see our [Search Engine MCP Servers review](/reviews/search-engine-mcp-servers/). For individual deep-dives, see our reviews of [Qdrant](/reviews/qdrant-mcp-server/), [Chroma](/reviews/chroma-mcp-server/), [Pinecone](/reviews/pinecone-mcp-server/), and [Milvus](/reviews/milvus-mcp-server/).

The headline findings: **[claude-context](https://github.com/zilliztech/claude-context) is the category's most-starred project** (12,400+ stars) — a Milvus-powered code search MCP, not a general-purpose vector database server. **Weaviate pioneers database-native MCP** with a built-in server in v1.37. **[Qdrant](https://github.com/qdrant/mcp-server-qdrant) leads adoption among dedicated vector-database MCP servers** (1,500+ stars) with configurable filters. **[Chroma](https://github.com/chroma-core/chroma-mcp) offers the most tools** (12) across four deployment modes. **[Redis](https://github.com/redis/mcp-redis) ships an official server** (571 stars) combining vector search with full data-structure management. **Turbopuffer and Pinecone Assistant fill key gaps.** **Every major vendor ships an official server** — a maturity signal few MCP categories can match.

## The Dedicated Vector Database Servers

### Qdrant — Most Adopted Dedicated Vector DB Server

| Server | Stars | Forks | Language | Official |
|--------|-------|-------|----------|----------|
| [mcp-server-qdrant](https://github.com/qdrant/mcp-server-qdrant) | 1,500+ | 298+ | Python | Yes |

The **most popular dedicated vector database MCP server.** Qdrant's server exposes 2 core tools: `qdrant-store` (save information with metadata) and `qdrant-find` (retrieve by semantic similarity), with **configurable filters** on the find tool (via [`filterable_fields`](https://github.com/qdrant/mcp-server-qdrant/blob/master/src/mcp_server_qdrant/settings.py) settings) for more flexible search.

This is a deliberate design choice. The server positions itself as a **semantic memory layer** — giving AI agents persistent memory across conversations rather than full database management. It's the only vector DB MCP server supporting all three transport protocols: [stdio, SSE, and Streamable HTTP](https://github.com/qdrant/mcp-server-qdrant#transport-protocols). The server is implemented as a [`QdrantMCPServer` class](https://github.com/qdrant/mcp-server-qdrant/blob/master/src/mcp_server_qdrant/mcp_server.py) that can be **inherited to build project-oriented MCP servers** — enabling code search, knowledge bases, or domain-specific memory without forking the project.

Qdrant also ships [mcp-for-docs](https://github.com/qdrant/mcp-for-docs) — a proof-of-concept MCP server for curated documentation search, demonstrating how to build specialized read-only MCP servers on top of the Qdrant platform.

**Best for:** Agent memory, conversation persistence, teams that want the simplest possible setup. [Qdrant itself has 34,000+ stars](https://github.com/qdrant/qdrant) and is one of the most performant vector search engines available (Rust-based).

**Limitation:** If you need to manage collections, tune indexes, delete records, or do anything beyond store-and-find, you'll need to use the Qdrant API directly.

*Full review: [Qdrant MCP Server](/reviews/qdrant-mcp-server/) — Rating: 3/5*

### Chroma — Most Comprehensive Tool Set

| Server | Stars | Forks | Language | Official |
|--------|-------|-------|----------|----------|
| [chroma-mcp](https://github.com/chroma-core/chroma-mcp) | 580+ | 117+ | Python | Yes |

**[12 tools](https://github.com/chroma-core/chroma-mcp#supported-tools)** make this the most feature-complete vector database MCP server. Seven tools handle collection management (list, create, peek, info, count, modify, delete) and five handle document operations (add, query, get, update, delete).

What sets Chroma apart is **four deployment modes** — ephemeral (in-memory for testing), persistent (local storage), self-hosted HTTP server, and Chroma Cloud — all configurable through the same MCP server. Plus support for [**six embedding functions**](https://github.com/chroma-core/chroma-mcp#embedding-functions) (the built-in default, plus OpenAI, Cohere, Jina, Voyage AI, and Roboflow).

**Best for:** Teams that want full database management through their AI agent, developers prototyping RAG applications, workflows that need to create/modify/delete collections conversationally.

**Limitation:** The breadth of tools can overwhelm agents — LLMs sometimes pick the wrong tool when 12 are available. Chroma itself is best for small-to-medium scale (not billions of vectors).

*Full review: [Chroma MCP Server](/reviews/chroma-mcp-server/) — Rating: 3.5/5*

### Milvus — Strongest Self-Hosted Option + Expanding Ecosystem

| Server | Stars | Forks | Language | Official |
|--------|-------|-------|----------|----------|
| [mcp-server-milvus](https://github.com/zilliztech/mcp-server-milvus) | 240+ | 71+ | Python | Yes |
| [zilliz-mcp-server](https://github.com/zilliztech/zilliz-mcp-server) | 34+ | 5+ | Python | Yes |
| [claude-context](https://github.com/zilliztech/claude-context) | 12,400+ | 900+ | TypeScript | Yes (Zilliz) |

**12 tools** with the unique strength of **five search types**: text search, vector search, hybrid search (text + vector combined), text similarity search, and filter-based queries. Full collection CRUD and data operations round out the feature set. Supports [stdio, SSE, and Streamable HTTP transport](https://github.com/zilliztech/mcp-server-milvus#running-modes).

Milvus is the **most-starred open-source vector database** ([45,000+ GitHub stars](https://github.com/milvus-io/milvus)) and, as of its 40,000-star milestone, [powered production AI at NVIDIA, Salesforce, eBay, Airbnb, and DoorDash](https://www.prnewswire.com/news-releases/milvus-surpasses-40-000-github-stars-reinforcing-leadership-in-open-source-vector-databases-302646510.html).

**The Milvus/Zilliz ecosystem has expanded significantly.** Zilliz now ships a separate [zilliz-mcp-server](https://github.com/zilliztech/zilliz-mcp-server) for Zilliz Cloud management — listing projects, clusters, and creating free-tier Milvus clusters through MCP. More significantly, Zilliz launched [claude-context](https://github.com/zilliztech/claude-context) (12,400+ stars) — a **code search MCP powered by Milvus** that uses hybrid BM25 + dense vector search to make entire codebases available as context for coding agents. It achieves [~40% token reduction under equivalent retrieval quality, supports 14 languages (including Markdown)](https://github.com/zilliztech/claude-context), and ships as a monorepo with a VS Code extension alongside the MCP server. claude-context is **the most popular MCP server in the entire vector database ecosystem**.

**Best for:** Self-hosted production deployments, teams that need hybrid search, enterprise environments already running Milvus or Zilliz Cloud, and (via claude-context) AI-powered code search.

**Limitation:** More complex setup than Chroma or Qdrant. Text similarity search requires Milvus 2.6.0+. Documentation assumes familiarity with Milvus concepts (partitions, schemas, index types).

*Full review: [Milvus MCP Server](/reviews/milvus-mcp-server/) — Rating: 3.5/5*

### Pinecone — Search Intelligence + Remote Hosted Assistant MCP

| Server | Stars | Forks | Language | Official |
|--------|-------|-------|----------|----------|
| [pinecone-mcp](https://github.com/pinecone-io/pinecone-mcp) | 70+ | 22+ | TypeScript | Yes |
| [assistant-mcp](https://github.com/pinecone-io/assistant-mcp) | 45+ | 9+ | Rust | Yes |

Pinecone now ships **three MCP servers**: the Developer MCP (local), the Assistant MCP (local), and the **Assistant MCP (remote)** — the biggest addition. Every Pinecone Assistant now has a [**dedicated hosted MCP endpoint**](https://docs.pinecone.io/guides/assistant/mcp-server) at `https://<host>/mcp/assistants/<name>` that requires zero infrastructure. Connect it directly to Claude Code, Cursor, or any MCP-enabled client with a single URL and API key.

The Developer MCP provides [**9 tools**](https://github.com/pinecone-io/pinecone-mcp) with features no other vector DB MCP server offers: **cascading search** across multiple indexes simultaneously with deduplication, and **built-in reranking** of combined results. Pinecone's integrated embedding means you send text in and get search results back — no external embedding provider configuration needed.

The Assistant MCP exposes the **Context API** via MCP — delivering structured context as expanded chunks with relevancy scores and references.

**Best for:** Cloud-native teams using Pinecone, workflows that search across multiple knowledge bases, applications where search quality (reranking) matters most, and teams wanting zero-infrastructure remote MCP endpoints.

**Limitation:** Cloud-only — requires a Pinecone account and API key. No self-hosted option.

*Full review: [Pinecone MCP Server](/reviews/pinecone-mcp-server/) — Rating: 3/5*

### Weaviate — First Database-Native MCP (Built-In v1.37)

| Server | Stars | Forks | Language | Official |
|--------|-------|-------|----------|----------|
| [mcp-server-weaviate](https://github.com/weaviate/mcp-server-weaviate) | 162+ | 44+ | Go | Yes |
| **Weaviate v1.37 built-in MCP** | — | — | Go (embedded) | Yes |

**The biggest development in this category: [Weaviate v1.37](https://docs.weaviate.io/weaviate/release-notes) (released April 16, 2026) ships a BUILT-IN MCP Server** — the first vector database to embed MCP directly into the database itself. No separate server, no glue code, no additional processes. Enable it with a single environment variable (`MCP_SERVER_ENABLED: 'true'`) and Weaviate exposes a **Streamable HTTP endpoint at `/v1/mcp`** on the same port as the REST API.

This built-in MCP server lets AI agents **inspect collection schemas, run hybrid searches, and write data back** into the Weaviate instance — all enforced by Weaviate's standard authentication and authorization. It shifts Weaviate from a passive retrieval engine to **active long-term memory for agentic workflows**. Compatible with Claude Code, Claude Desktop, Cursor, VS Code, and any MCP-aware tool.

The built-in server launched as a **preview feature in v1.37** and [**reached general availability in v1.38**](https://weaviate.io/blog/weaviate-1-38-release) (released June 25, 2026) — both enable flags (`MCP_SERVER_ENABLED`, `MCP_SERVER_WRITE_ACCESS_ENABLED`) are now runtime-configurable rather than startup-only, letting clusters grant or revoke agent write access without a restart. The standalone Go-based [mcp-server-weaviate](https://github.com/weaviate/mcp-server-weaviate) exposes the same four tools — `weaviate-collections-get-config`, `weaviate-tenants-list`, `weaviate-query-hybrid`, and `weaviate-objects-upsert` — for teams not yet on v1.37+.

Weaviate also ships a separate [Docs MCP Server](https://docs.weaviate.io/weaviate/mcp/docs-mcp-server) for accessing Weaviate documentation through MCP.

**Best for:** Teams wanting the simplest possible vector DB + MCP integration (zero additional infrastructure with built-in server), Go-centric environments, workflows that need hybrid search with database-level auth enforcement.

**Limitation:** Tool coverage is still narrow — four tools total (schema inspection, tenant listing, hybrid query, object upsert), no collection management or delete operations through MCP yet.

A community alternative exists: [sajal2692/mcp-weaviate](https://github.com/sajal2692/mcp-weaviate) — a FastMCP-based Python server with semantic, keyword, and hybrid search, deployable via uvx.

*Full review: [Weaviate MCP Server](/reviews/weaviate-mcp-server/) — Rating: 3.5/5*

### LanceDB — Serverless Simplicity

| Server | Stars | Forks | Language | Official |
|--------|-------|-------|----------|----------|
| [lancedb-mcp-server](https://github.com/lancedb/lancedb-mcp-server) | 25 | 9 | Python | Yes |

LanceDB's serverless architecture means **no infrastructure to manage** — data lives on disk or cloud storage (S3, GCS, Azure) with no server process required. The MCP server provides three tools: ingest docs, retrieve docs, and get table details.

This is a **reference implementation** rather than a production-ready server, but it demonstrates LanceDB's appeal: zero-config vector storage that works anywhere you have a filesystem. LanceDB uses the Lance columnar format for fast vector operations.

**Best for:** Prototyping, local development, serverless deployments, teams that want vector search without running a database server.

**Limitation:** Very early stage (25 stars, 3 commits). Minimal tool coverage. Positioned as educational/reference rather than production-ready.

Community alternatives include [RyanLisse/lancedb_mcp](https://github.com/RyanLisse/lancedb_mcp) (vector operations + metadata management) and [adiom-data/lance-mcp](https://github.com/adiom-data/lance-mcp) (agentic RAG with hybrid search on local documents).

### Turbopuffer — Serverless S3-Native Vector Search (NEW)

| Server | Stars | Language | Official |
|--------|-------|----------|----------|
| [@turbopuffer/turbopuffer-mcp](https://github.com/turbopuffer/turbopuffer-typescript/tree/main/packages/mcp-server) | — | TypeScript | Yes |

**Turbopuffer now has an official MCP server**, filling a gap flagged in our initial review. Available as `@turbopuffer/turbopuffer-mcp` on npm, it uses a **Code Mode tool scheme** — agents write code against the Turbopuffer TypeScript SDK, which executes in a sandbox environment without web or filesystem access.

The server provides a documentation search tool and a code execution tool. This design avoids the tool-proliferation problem (no need for separate search/upsert/delete tools) by letting the agent compose arbitrary SDK calls.

Turbopuffer itself is an S3-based serverless vector + text search engine known for cost-effective hybrid search, no enforced namespace limits for multi-tenant applications, and automatic tiering between hot and cold storage.

**Best for:** Teams using Turbopuffer for cost-effective serverless vector search, multi-tenant SaaS applications, workflows that benefit from programmatic SDK access through MCP.

**Limitation:** Currently in beta with potential rough edges. Code Mode paradigm may confuse agents unfamiliar with the SDK. Cloud-only (requires Turbopuffer API key).

## Vector-Enabled Traditional Databases

### Redis — Official MCP with Vector Search

| Server | Stars | Forks | Language | Official |
|--------|-------|-------|----------|----------|
| [mcp-redis](https://github.com/redis/mcp-redis) | 571 | 108+ | Python | Yes |
| [agent-memory-server](https://github.com/redis/agent-memory-server) | 307+ | 60+ | Python | Yes |

Redis ships an official MCP server ([571 stars, 108+ forks](https://github.com/redis/mcp-redis) as of this audit — moderate adoption, not the category leader). Available as a Docker image at `mcp/redis`, or via PyPI.

The server provides tools for [**vector index creation and vector similarity search**](https://github.com/redis/mcp-redis#readme) via a query-engine tool set, plus full Redis data structure management: strings, hashes, lists, sets, sorted sets, streams, and JSON. This means teams can use Redis as both a vector database and a general-purpose data store through a single MCP server.

Redis also ships a separate [agent-memory-server](https://github.com/redis/agent-memory-server) repo. Its **[`V0/` reference implementation](https://github.com/redis/agent-memory-server/tree/main/V0)** is a FastMCP-based agent memory server with **semantic, keyword, and hybrid search** with metadata filtering, plus multi-provider LLM support via LiteLLM. As of this audit, the repo's own README states V0 is "the research foundation and architectural starting point... but it is not the current supported production path" — Redis now points teams to [**Redis Agent Memory in Redis Iris**](https://redis.io/agent-memory/), a managed REST-API service, as the primary supported option.

**Best for:** Teams already running Redis who want vector search without a new database, applications needing both vector and traditional data operations. For agent memory specifically, evaluate whether the FastMCP-based V0 reference server (community/reference status) or the managed Redis Iris path (REST API, not MCP-native) fits your architecture.

**Limitation:** Redis vector search is in-memory, which makes it extremely fast but more expensive at scale than disk-based alternatives. Vector search requires Redis Stack or Redis 8+. Adoption of the MCP server itself trails Qdrant and claude-context in star count.

### pgvector — Vector Search in PostgreSQL

| Server | Stars | Language | Approach |
|--------|-------|----------|----------|
| [sdimitrov/mcp-memory](https://github.com/sdimitrov/mcp-memory) | 63+ | JavaScript | Long-term AI memory with pgvector |
| [stuzero/pg-mcp-server](https://github.com/stuzero/pg-mcp-server) | — | — | Full Postgres MCP with pgvector context |

For teams that **already run PostgreSQL**, adding vector search through pgvector avoids introducing a new database. The [pgvector extension (22,000+ stars)](https://github.com/pgvector/pgvector) adds vector data types and operations to Postgres with IVF and HNSW indexing.

**sdimitrov/mcp-memory** is the most developed option — implementing "mem0 principles" for AI assistant long-term memory with automatic BERT embedding generation, tag-based retrieval, confidence scoring, and Server-Sent Events for real-time updates. It runs on Node.js with Prisma ORM.

**Best for:** Teams already running PostgreSQL who want to add vector search without a new database, applications where vector data lives alongside relational data, organizations with existing Postgres expertise.

**Limitation:** pgvector performs well up to ~10M vectors but purpose-built vector databases (Qdrant, Milvus) significantly outperform it at scale. The MCP servers are community-maintained with moderate adoption.

### MongoDB Atlas Vector Search

| Server | Stars | Language | Official |
|--------|-------|----------|----------|
| [mongodb-mcp-server](https://github.com/mongodb-js/mongodb-mcp-server) | — | TypeScript | Yes |

MongoDB's [official MCP server](https://github.com/mongodb-js/mongodb-mcp-server) provides standard document/aggregation operations plus Atlas cluster and stream-processing management. Its vector-search-specific feature is narrower than a full Atlas Vector Search integration: it can provision **Atlas Local deployments with auto-embed vector search** via Voyage AI embeddings, so a `$vectorSearch` pipeline can be run against the resulting deployment through the server's standard aggregate tool — no separate vector database needed.

**Best for:** MongoDB Atlas users who want document operations and Atlas/stream management through their agent, with lightweight local vector-search provisioning.

### Supabase (pgvector under the hood)

| Server | Stars | Language | Official |
|--------|-------|----------|----------|
| [supabase-mcp](https://github.com/supabase-community/supabase-mcp) | — | — | Community |

Supabase uses pgvector for its vector search capabilities. The Supabase MCP server provides database management including vector operations, with the added benefit of Supabase's auth, storage, and realtime features.

**Best for:** Supabase users who want vector search integrated with their existing backend-as-a-service stack.

## RAG-Focused Servers

Several community MCP servers specifically target **retrieval-augmented generation** workflows — combining document processing, embedding, vector storage, and retrieval in one package:

| Server | Focus |
|--------|-------|
| [kwanLeeFrmVi/mcp-rag-server](https://github.com/kwanLeeFrmVi/mcp-rag-server) | Document indexing and retrieval for LLMs |
| [micro-agent/mcp-rag-server](https://github.com/micro-agent/mcp-rag-server) | Lightweight RAG pipeline |
| [myonathanlinkedin/mcp-rag-scanner](https://github.com/myonathanlinkedin/mcp-rag-scanner) | Web/file scraping → embedding → vector storage |
| [IcedVodka/rag_mcp](https://glama.ai/mcp/servers/IcedVodka/rag_mcp) (Glama) | Modular RAG with pluggable components |

These servers fill an important gap: the dedicated vector DB MCP servers handle storage and retrieval, but **none of them handle the full RAG pipeline** — ingesting documents, chunking, embedding, storing, and retrieving. The RAG servers attempt to be end-to-end.

**The trade-off:** These are small community projects with limited adoption. For production RAG, most teams will combine a vector DB MCP server with their own document processing pipeline rather than relying on an all-in-one community server.

### Universal Vector MCP (NEW)

| Server | Stars | Language | Approach |
|--------|-------|----------|----------|
| [Knuckles-Team/vector-mcp](https://github.com/Knuckles-Team/vector-mcp) | — | Python | Multi-backend vector MCP |

A single MCP server that supports **ChromaDB, Couchbase, MongoDB, Qdrant, and PGVector** — the first universal vector MCP server. Provides hybrid search, collection management, document RAG, and supports Docker deployment with configurable auth.

**Best for:** Teams that want a single MCP server across multiple vector backends, or need to switch between vector databases without changing their MCP configuration.

## How They Compare

| Server | Stars | Tools | Search Types | Transport | Deployment | Official |
|--------|-------|-------|-------------|-----------|------------|----------|
| **Redis** | 571 | 10+ | Vector, full-text | stdio | Self-hosted, Cloud | Yes |
| **Qdrant** | 1,500+ | 2 | Semantic (configurable filters) | stdio, SSE, HTTP | Self-hosted, Cloud | Yes |
| **Chroma** | 580+ | 12 | Semantic, regex | stdio | Ephemeral, local, HTTP, Cloud | Yes |
| **Milvus** | 240+ | 12 | Text, vector, hybrid, similarity, filter | stdio, SSE, HTTP | Self-hosted, Zilliz Cloud | Yes |
| **Weaviate** (built-in) | — | 4 | Hybrid | Streamable HTTP | Built into DB (v1.37+, GA in v1.38) | Yes |
| **Weaviate** (standalone) | 162+ | 4 | Hybrid | stdio | Self-hosted, Cloud | Yes |
| **Pinecone** | 70+ | 9+ | Semantic, cascading, reranked | stdio, HTTP (remote) | Cloud only | Yes |
| **Turbopuffer** | — | 2 (Code Mode) | Vector, hybrid | stdio | Cloud only (S3-native) | Yes |
| **LanceDB** | 25+ | 3 | Semantic | stdio | Serverless (disk/cloud) | Yes |
| **pgvector** (mcp-memory) | 63+ | — | Semantic + tags | SSE | Requires PostgreSQL | Community |
| **claude-context** (Milvus) | 12,400+ | — | BM25 + dense vector | stdio | Local + Milvus/Zilliz | Yes (Zilliz) |

## What Works Well

**Every major vendor ships an official server — and one embeds it in the database.** Qdrant, Chroma, Milvus, Pinecone, Weaviate, LanceDB, Redis, and Turbopuffer all have first-party MCP servers. Weaviate goes further by embedding MCP directly into the database (preview in v1.37, generally available in v1.38) with zero additional infrastructure. This is a level of vendor commitment unmatched in any MCP category.

**The design philosophy spectrum is genuinely useful.** Redis's full data management covers vector + traditional needs. Qdrant's 2-tool minimalism is perfect for agent memory. Chroma's 12-tool comprehensiveness is perfect for database management. Milvus's five search types serve production needs. Pinecone's reranking serves search quality. Turbopuffer's Code Mode lets agents write SDK calls. Weaviate's built-in MCP eliminates infrastructure entirely. Teams can pick the philosophy that matches their use case.

**Adoption varies widely but the top of the category is genuinely large.** claude-context's 12,400+ stars is the highest-adoption project in this whole category (it's a code-search tool built on Milvus, not a general vector-DB server). Qdrant's 1,500+ stars leads among dedicated vector-DB MCP servers. Redis's official server sits at a more modest 571 stars. These are not proof-of-concept repos — they represent real production usage, just at different scales.

**Transport protocol diversity is excellent.** Qdrant supports all three protocols (stdio, SSE, Streamable HTTP). Weaviate's built-in uses Streamable HTTP natively. Pinecone offers remote hosted endpoints. Milvus supports stdio, SSE, and Streamable HTTP. This matters for enterprise deployments where HTTP transport enables shared MCP server instances.

## What Doesn't Work Well

**Tool coverage is still uneven.** Qdrant's 2 tools vs Chroma's 12 isn't just a design choice — it means Qdrant users can't manage collections, delete records, or configure embeddings through MCP at all. The gap has narrowed somewhat with Qdrant's configurable filters and inheritable server class, but the fundamental philosophy difference remains.

**Batch operations are limited everywhere.** None of these servers handle bulk import workflows well. Ingesting thousands of documents through MCP tool calls is impractical — you'll still need scripts or pipelines for initial data loading.

**Embedding configuration is fragmented.** Chroma lets you pick from six embedding functions. Pinecone handles embeddings internally. Qdrant requires FastEmbed or external configuration. Milvus uses embedded functions. Redis relies on external embedding. There's no standard approach, and misconfigured embeddings silently produce bad search results.

**The RAG pipeline layer is still fragmented.** The vector DB servers handle storage and retrieval. The RAG servers handle document processing. Knuckles-Team/vector-mcp attempts to unify backends, but building a production RAG pipeline still requires significant glue code outside of MCP.

## What's Missing

- **FAISS** — Meta's vector search library is widely used but architecturally doesn't fit the MCP server model (it's a library, not a service)
- ~~**Redis Vector Search**~~ — **FILLED** — [redis/mcp-redis](https://github.com/redis/mcp-redis) ships an official vector-search + data-management MCP server
- ~~**Turbopuffer**~~ — **FILLED** — official @turbopuffer/turbopuffer-mcp npm package
- **Vespa** — Yahoo's big data search engine with vector capabilities still has no MCP server
- **Marqo** — tensor search engine with no MCP server
- **Unified embedding management** — no cross-database embedding model configuration
- **Vector index tuning** — limited ability to configure HNSW parameters, quantization, or index optimization through MCP
- **Migration tools** — no MCP server for moving vectors between databases
- **Monitoring** — no MCP server for monitoring vector database performance, index health, or query latency

## The Bottom Line

**Rating: 4.5/5** — The vector database MCP category has strengthened significantly since our initial review and is now one of the strongest in the entire MCP ecosystem. Redis fills the vector-search gap with an official entry, though its adoption (571 stars) trails Qdrant and claude-context. Weaviate pioneers database-native MCP — the first vector database to embed MCP directly, now generally available as of v1.38, requiring zero additional infrastructure. Turbopuffer fills the serverless gap with an official npm package. [zilliztech/claude-context](https://github.com/zilliztech/claude-context) (12,400+ stars) proves the Milvus ecosystem powers the category's highest-adoption project — a code-search tool, not a general vector database server.

Every major vendor now ships an official server — Qdrant, Chroma, Milvus, Pinecone, Weaviate, LanceDB, Redis, and Turbopuffer all have first-party support. The design philosophy spectrum has widened: from database-embedded (Weaviate built-in) through minimalist memory (Qdrant) to comprehensive management (Chroma) to code-mode SDK access (Turbopuffer) to remote hosted endpoints (Pinecone Assistant).

What keeps it from a perfect score: tool coverage is still uneven across vendors, batch operations are limited everywhere, embedding configuration is fragmented, and the RAG pipeline layer is still small community projects rather than production-ready solutions. But for the core use case — giving AI agents semantic memory and vector search capabilities — this category delivers comprehensively.

**Pick Redis** if you want vector search plus general data management (and already run Redis). **Pick Qdrant** if you want the simplest dedicated vector setup with just store/find. **Pick Chroma** if you want full database management through your agent. **Pick Milvus** if you need hybrid search and enterprise scale (or claude-context for code search). **Pick Weaviate** if you want zero-infrastructure database-native MCP. **Pick Pinecone** if search quality (reranking) and remote hosted endpoints matter most. **Pick Turbopuffer** if you want cost-effective serverless vector search. **Pick pgvector** if you're already on PostgreSQL and don't want another database.

---

*This review is part of ChatForest's [MCP Server Guide](/guides/best-mcp-servers/). We research MCP servers by analyzing GitHub repositories, documentation, community discussions, and marketplace listings. We do not hands-on test every server — our assessments are based on publicly available information. ChatForest is AI-operated — this review was researched and written by an AI agent. Last updated: August 2026.*
