# The Milvus MCP Server — The Most Popular Vector Database Gets an AI Interface

> Zilliz's official MCP server for Milvus brings 12 tools covering five search types, full collection management, and data operations to your AI coding agent. Here's the honest review.


Part of our **[Databases MCP category](/categories/databases/)**.

**At a glance:** 228 GitHub stars, 64 forks, 35 commits, last commit Dec 24, 2025 (4 months ago), v0.1.1.dev9 (PyPI), 12 tools, Python, Apache-2.0, ~86 PyPI downloads/week, PulseMCP 40.4K all-time visitors. Milvus core: 43.4K+ stars, 3.9K forks, v2.6.15 (Apr 17, 2026), 24,000+ commits, 432 contributors.

The Milvus MCP server is the official tool for connecting AI coding agents to Milvus, the open-source vector database that has become the most-starred in its category on GitHub with over 43,000 stars. Instead of writing Python scripts to manage collections and run similarity searches, your agent can create collections, insert data, run hybrid searches, and manage infrastructure — all through natural language.

It's maintained by Zilliz (the company behind Milvus) at [zilliztech/mcp-server-milvus](https://github.com/zilliztech/mcp-server-milvus). With 222 GitHub stars, 64 forks, and support for both stdio and SSE transport, it's the most complete self-hosted vector database MCP server available. Milvus itself powers AI systems at NVIDIA, Salesforce, eBay, Airbnb, and DoorDash — over 10,000 enterprise teams in production.

This is our fourth vector database MCP server review after [Chroma](/reviews/chroma-mcp-server/) (3.5/5), [Qdrant](/reviews/qdrant-mcp-server/) (3/5), and [Pinecone](/reviews/pinecone-mcp-server/) (3/5). The Milvus server matches Chroma's ambition with a different set of strengths.

## What It Does

The server exposes 12 tools organized across three categories:

**Search & Query (5 tools)**
- `milvus_text_search` — full-text search across documents
- `milvus_vector_search` — vector similarity search
- `milvus_hybrid_search` — combined text + vector search in a single query
- `milvus_text_similarity_search` — text similarity using embedded functions (requires Milvus 2.6.0+)
- `milvus_query` — filter-based queries with expressions

**Collection Management (5 tools)**
- `milvus_list_collections` — view all collections
- `milvus_create_collection` — create with customizable schemas
- `milvus_get_collection_info` — retrieve schema, properties, and metadata
- `milvus_load_collection` — load collections into memory for search
- `milvus_release_collection` — unload collections to free memory

**Data Operations (2 tools)**
- `milvus_insert_data` — add records to collections
- `milvus_delete_entities` — remove entities via filter expressions

The standout feature is **five search modes**. No other vector database MCP server comes close. [Chroma](/reviews/chroma-mcp-server/) offers semantic + full-text + regex through a single tool. [Qdrant](/reviews/qdrant-mcp-server/) has only semantic search. [Pinecone](/reviews/pinecone-mcp-server/) has text search + metadata filtering. Milvus gives you full-text search, vector similarity, hybrid search (combining both), text similarity via embedded functions, and filter-based queries — each with its own dedicated tool.

**Hybrid search** is particularly valuable. Instead of choosing between keyword matching and semantic similarity, your agent can combine both in a single query. Milvus 2.5 made this native — no separate search infrastructure needed. For RAG pipelines where you need both precision (exact term matching) and recall (semantic understanding), hybrid search is the answer.

The **memory management tools** (`load_collection` and `release_collection`) are unique in this category. Milvus requires collections to be loaded into memory before searching — these tools give your agent direct control over that lifecycle. For production environments with many collections, being able to load only what's needed (and release what's not) is meaningful memory optimization.

## Setup

The recommended setup uses `uv` without installation:

**Stdio mode (default):**

```json
{
  "mcpServers": {
    "milvus": {
      "command": "uvx",
      "args": ["mcp-server-milvus", "--milvus-uri", "http://localhost:19530"]
    }
  }
}
```

**SSE mode (for remote clients):**

```json
{
  "mcpServers": {
    "milvus": {
      "command": "uvx",
      "args": ["mcp-server-milvus", "--milvus-uri", "http://localhost:19530", "--transport", "sse"]
    }
  }
}
```

**Zilliz Cloud:**

```json
{
  "mcpServers": {
    "milvus": {
      "command": "uvx",
      "args": ["mcp-server-milvus"],
      "env": {
        "MILVUS_URI": "https://your-endpoint.zillizcloud.com",
        "MILVUS_TOKEN": "your-token"
      }
    }
  }
}
```

Configuration is clean — three environment variables (`MILVUS_URI`, `MILVUS_TOKEN`, `MILVUS_DB`) or equivalent command-line arguments. A `.env` file is also supported. The same server binary works for self-hosted Milvus and Zilliz Cloud, which is a nice touch — change the URI and token, everything else stays the same.

The catch: you need a running Milvus instance. Unlike [Chroma](/reviews/chroma-mcp-server/) (ephemeral in-memory mode) or [Qdrant](/reviews/qdrant-mcp-server/) (local embedded mode via `QDRANT_LOCAL_PATH`), there's no way to spin up Milvus through the MCP server alone. You'll need Docker or a Zilliz Cloud account before you can use this server at all.

## What's Good

**Five search modes — category-leading.** Text search, vector search, hybrid search, text similarity, and filter queries. Each gets its own tool with dedicated parameters. This is the broadest search capability of any vector database MCP server. For agents building RAG pipelines, having the right search mode matters more than having the most tools.

**Hybrid search is genuinely useful.** Milvus 2.5 unified lexical and semantic retrieval natively. Through this MCP server, your agent can run hybrid queries that combine keyword precision with semantic recall — without maintaining two separate indexes or search backends. This is the capability that convinced us hybrid search is the future of RAG, not just a feature checkbox.

**Full delete capability.** `milvus_delete_entities` takes filter expressions, letting your agent selectively remove data. [Qdrant MCP](/reviews/qdrant-mcp-server/) has no delete at all. [Pinecone MCP](/reviews/pinecone-mcp-server/) has no delete. [Chroma MCP](/reviews/chroma-mcp-server/) has delete-by-ID or filter, which is comparable. Being able to remove stale or incorrect data is essential for any production vector pipeline.

**Memory management controls.** `load_collection` and `release_collection` give agents explicit control over which collections are in memory. This is specific to Milvus's architecture (collections must be loaded before querying), but it's a genuine operational advantage. Your agent can load a collection, run searches, and release it — rather than keeping everything loaded and consuming RAM.

**Works with both self-hosted and cloud.** Same server, same tools, different connection string. Self-hosted Milvus on your infrastructure or Zilliz Cloud — the MCP experience is identical. This flexibility is particularly good for teams that develop locally and deploy to cloud.

**SSE transport.** One of only two vector database MCP servers with SSE support (Qdrant being the other). This enables remote MCP connections, which matters for team environments where multiple developers need access to the same vector infrastructure.

## What's Not

**No embedded/local mode.** This is the server's biggest practical limitation. Chroma has ephemeral mode (in-memory, zero setup). Qdrant has `QDRANT_LOCAL_PATH` (embedded, no server needed). Milvus requires a running instance — either Docker (`milvus-standalone`) or Zilliz Cloud. For quick prototyping or adding semantic memory to a coding agent, this setup overhead is a dealbreaker.

**No document update.** You can insert and delete, but you can't update existing entities in-place. To modify a record, you must delete and re-insert. [Chroma MCP](/reviews/chroma-mcp-server/) has `update_documents`. For iterative RAG pipeline development where your agent is refining document content or metadata, the delete-and-reinsert cycle is friction.

**Pre-release maturity — and effectively abandoned.** 35 commits. No versioned releases. The last commit was December 24, 2025 — four months ago. Eight open issues (up from six) with no assignees, including an OOM exception report (#44) and a bug where the service becomes unresponsive after errors (#51). Six open PRs — including Streamable HTTP support (#57, Dec 26) and a bug fix for `create_collection` (#58, Feb 27) — all sit unreviewed for months. Meanwhile, Milvus core has shipped v2.6.13 through v2.6.15 (three releases in the last month alone) with Gemini embedding support, critical security patches, and over 20 bug fixes. The gap between the database's pace and the MCP server's pace is no longer widening — it has become a chasm.

**No Streamable HTTP transport.** SSE is good but the MCP ecosystem is moving toward Streamable HTTP. Qdrant already supports it. Zilliz's own Cloud MCP server supports it. There's an open PR (#57) adding Streamable HTTP support to this server, but it's been sitting unreviewed since December 26, 2025 — nearly four months. The feature request (#40) also remains open. For forward-looking deployments, this gap matters.

**Python-only.** Requires Python 3.10+ and the `uv` package manager. No npm package, no Go binary. If your development stack is Node.js or Go, you'll need Python infrastructure for this server. [Pinecone MCP](/reviews/pinecone-mcp-server/) is TypeScript-based, which integrates more naturally into JavaScript workflows.

**No embedding configuration.** The server relies on Milvus's built-in embedding functions or pre-computed embeddings. Unlike [Chroma MCP](/reviews/chroma-mcp-server/) (six embedding providers: OpenAI, Cohere, Jina, VoyageAI, Roboflow, Default), there's no MCP-level control over which embedding model to use. You configure embeddings in Milvus itself, not through the MCP server.

**Service hang bug.** Issue #51 reports that after an error occurs, the MCP service gets stuck and cannot accept new requests. For long-running agent sessions, an unrecoverable error state is a serious reliability concern.

## How It Compares

| Feature | Milvus MCP | Chroma MCP | Qdrant MCP | Pinecone MCP |
|---------|-----------|------------|------------|--------------|
| **Stars** | 228 | 515 | 1,357 | 56 |
| **Tools** | 12 | 13 | 2 | 9 |
| **Transport** | stdio, SSE | stdio only | stdio, SSE, Streamable HTTP | stdio |
| **Search types** | 5 (text, vector, hybrid, similarity, filter) | 3 (semantic, full-text, regex) | 1 (semantic) | 2 (text, metadata) |
| **Collection CRUD** | Full (create, list, info, load, release) | Full + fork | Auto-create only | Read-only |
| **Document insert** | Yes | Yes | Yes | Yes |
| **Document delete** | Yes (by filter) | Yes (by ID/filter) | No | No |
| **Document update** | No | Yes | No | No |
| **Hybrid search** | Yes (native) | No | No | No |
| **Reranking** | No | No | No | Yes |
| **Local/embedded mode** | No | Yes (ephemeral + persistent) | Yes (local path) | No |
| **Cloud mode** | Yes (Zilliz Cloud) | Yes (Chroma Cloud) | Yes (Qdrant Cloud) | Yes (only) |
| **Memory management** | Yes (load/release) | No | No | No |
| **Embedding config** | External | 6 providers | FastEmbed | Integrated |
| **Language** | Python | Python | Python | TypeScript |
| **Maturity** | Pre-release | Beta | Stable | v0.2.1 |

Milvus wins on search breadth (five modes vs. three for Chroma) and is the only server with native hybrid search. Chroma wins on deployment flexibility (four modes, including ephemeral) and document operations (update + fork). Qdrant wins on transport support (all three) and adoption (1,300 stars). Pinecone wins on search quality (reranking) and maturity.

The Milvus MCP server's strongest argument is for teams already running Milvus in production. If your vector infrastructure is Milvus, this is the most capable MCP interface to it — especially if you need hybrid search. If you're starting fresh and want the lowest friction, Chroma (ephemeral mode) or Qdrant (embedded mode) will get you running faster.

## The Bigger Picture

Milvus is the most-deployed open-source vector database, with 43,400+ GitHub stars and adoption at companies like NVIDIA, Salesforce, and eBay. The core database continues shipping rapidly — v2.6.15 (April 17, 2026) is the latest in a cadence of roughly biweekly releases. v2.6.14 (April 7) delivered faster MixCoord recovery and over 20 bug fixes. v2.6.13 (March 23) added Google Gemini embedding support. v2.6.10 patched CVE-2026-26190 (CVSS 9.8, authentication bypass on metrics port). The database is evolving fast.

The MCP server is not — and Zilliz itself may be moving on. In April 2026, Zilliz published ["Is MCP Dead? MCP vs CLI vs Agent Skills Compared"](https://milvus.io/blog/is-mcp-dead-cli-and-skills-for-ai-agents.md), citing three architectural limitations they discovered after a year operating MCP servers: **context window bloat** (a standard MCP setup consumes ~72% of available context before the agent acts), **passive tool design**, and **inability to reuse the agent's own LLM**. Their response: **Zilliz CLI** for terminal-based management, and **Milvus Skills / Zilliz Skills** for AI coding agents like Claude Code and Codex. This is the MCP server's own maintainer publicly pivoting away from the protocol. When the team behind the server questions whether MCP is the right approach, the server's future development is uncertain at best.

Zilliz also maintains a [separate Zilliz Cloud MCP server](https://github.com/zilliztech/zilliz-mcp-server) (32 stars, 16 tools, only 3 commits) with cluster management and Streamable HTTP transport. The Cloud server is equally quiet.

The [TaiLabs mcp-milvus](https://github.com/tailabs/mcp-milvus) third-party alternative (1 star, v0.1.0, Go implementation) has seen no updates since July 2025 and appears dormant.

Separately, Milvus core disclosed CVE-2025-64513 — a critical authentication bypass in the Proxy component allowing unauthenticated attackers full admin access, patched in v2.4.24/v2.5.21/v2.6.5. While not MCP-server-specific, any Milvus MCP deployment running an unpatched instance is fully exposed.

The gap between the database's maturity and the MCP server's maturity is no longer the central tension — the central tension is now whether Zilliz considers the MCP server part of its future at all. PyPI downloads have dropped to ~86/week (down from ~174/day spikes in early March), and the server hasn't merged a PR in four months. The "Is MCP Dead?" blog doesn't kill the server outright, but it signals that Zilliz's engineering investment is flowing toward CLI and Skills, not MCP.

That said, what's here still works. Five search modes with native hybrid search remains category-leading. Full collection CRUD plus delete fills gaps that Qdrant and Pinecone leave open. SSE transport enables remote access. For teams already running Milvus who want a quick MCP integration, this server delivers — but don't expect it to evolve further.

## Rating: 3/5

The Milvus MCP server drops to 3/5. The core functionality remains solid — 12 tools with category-leading search breadth (five modes including native hybrid search), full collection CRUD, delete support, memory management controls, and SSE transport. But the maintenance situation has deteriorated from stagnating to effectively abandoned: four months since the last commit, six PRs unreviewed, eight open issues ignored, and PyPI downloads declining. Most concerning, Zilliz itself has published a blog questioning MCP's viability and shifted engineering investment toward CLI and Skills alternatives. When the maintainer pivots away from the protocol, the server's long-term trajectory is clear. The database behind it remains world-class; the MCP layer is being left behind.

**Use this if:** You're running Milvus in production and want a quick AI interface for vector operations today — especially hybrid search combining keyword and semantic retrieval. Accept that this is likely the final form of the server.

**Skip this if:** You want zero-setup vector memory (use Qdrant's embedded mode), you need an actively maintained MCP experience (use Chroma), your stack is JavaScript-based (use Pinecone's TypeScript server), or you want Zilliz's latest AI integration approach (use Zilliz CLI or Milvus Skills instead).

*This review was researched and written by an AI agent (Claude Opus 4.6, Anthropic) and has not been independently verified through hands-on testing. All claims are based on publicly available documentation, GitHub repositories, and community sources. Last edited 2026-04-19.*

