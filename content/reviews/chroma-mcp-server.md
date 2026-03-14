---
title: "The Chroma MCP Server — Vector Database Operations Through Your AI Assistant"
date: 2026-03-14T09:28:15+09:00
description: "Chroma's official MCP server brings AI-native vector database management directly into your coding agent. 13 tools covering collections, documents, semantic search, and embedding management across four deployment modes. Here's the honest review."
og_description: "Chroma's official MCP server lets AI agents manage vector databases with 13 tools, four client modes, and six embedding providers. The most versatile vector DB MCP server available. Rating: 3.5/5."
content_type: "Review"
card_description: "Chroma's first-party MCP server for AI-assisted vector database management. 13 tools covering collections, documents, semantic search, regex matching, and embedding configuration — the most comprehensive vector DB MCP experience available."
---

The Chroma MCP server is the official tool for connecting AI coding agents to Chroma, the open-source vector database that powers RAG applications for millions of developers. Instead of writing Python scripts to manage embeddings and run similarity searches, your agent can create collections, add documents, query semantically, and manage embedding configurations — all through natural language.

It's first-party, maintained by the Chroma team at [chroma-core/chroma-mcp](https://github.com/chroma-core/chroma-mcp). With 515 GitHub stars and support for four deployment modes — ephemeral, persistent local, self-hosted HTTP, and Chroma Cloud — it's the most flexible vector database MCP server available. The core Chroma project has 26,600 stars and is one of the most popular AI infrastructure tools in the Python ecosystem.

This is our first vector database MCP server review, and it sets a solid baseline for the category — though it also reveals how young the vector DB MCP space still is.

## What It Does

The server exposes 13 tools organized across two categories:

**Collection Management (8 tools)**
- `list_collections` — browse collections with pagination
- `create_collection` — create with configurable HNSW parameters (space, construction_ef, search_ef, num_threads, M)
- `peek_collection` — preview collection contents
- `get_collection_info` — retrieve statistics and metadata
- `get_collection_count` — count documents in a collection
- `modify_collection` — rename or update collection metadata
- `delete_collection` — remove a collection entirely
- `chroma_fork_collection` — duplicate a collection for experimentation (added v0.2.6)

**Document Operations (5 tools)**
- `add_documents` — add documents with optional embeddings and metadata
- `query_documents` — semantic search with metadata filtering, full-text search, and regex support
- `get_documents` — retrieve by ID or metadata filter
- `update_documents` — modify existing documents
- `delete_documents` — remove documents by ID or filter

The standout feature is **collection forking** via `chroma_fork_collection`. No other vector database MCP server offers this. When your agent is experimenting with different embedding strategies or chunking approaches, it can fork a collection, modify the fork, compare results, and keep or discard — without touching the original data. It's a similar philosophy to Neon's branch-based migrations, applied to vector search.

The **search capabilities** are also notably broad. `query_documents` supports semantic (vector) search, full-text search, and regex matching — all through a single tool with metadata filtering. Most competing MCP servers offer semantic search only.

## Setup

Chroma offers four deployment modes through the same server binary:

**Ephemeral (in-memory, simplest — great for prototyping):**

```json
{
  "mcpServers": {
    "chroma": {
      "command": "uvx",
      "args": ["chroma-mcp"]
    }
  }
}
```

**Persistent (local file storage):**

```json
{
  "mcpServers": {
    "chroma": {
      "command": "uvx",
      "args": ["chroma-mcp", "--client-type", "persistent", "--data-dir", "/path/to/data"]
    }
  }
}
```

**Chroma Cloud:**

```json
{
  "mcpServers": {
    "chroma": {
      "command": "uvx",
      "args": ["chroma-mcp", "--client-type", "cloud", "--tenant", "YOUR_TENANT", "--database", "YOUR_DB", "--api-key", "YOUR_KEY"]
    }
  }
}
```

**Self-hosted HTTP server:**

```json
{
  "mcpServers": {
    "chroma": {
      "command": "uvx",
      "args": ["chroma-mcp", "--client-type", "http", "--host", "localhost", "--port", "8000"]
    }
  }
}
```

The four-mode design is genuinely useful. You can prototype with ephemeral mode (zero setup), develop with persistent local storage, test against a self-hosted instance, and deploy to Chroma Cloud — all with the same MCP server, just different flags. Environment variables (`CHROMA_CLIENT_TYPE`, `CHROMA_DATA_DIR`, etc.) and `.env` file support via `CHROMA_DOTENV_PATH` make configuration clean.

Six embedding providers are supported out of the box: Default (Chroma's built-in), Cohere, OpenAI, Jina, VoyageAI, and Roboflow. After Chroma v1.0.0, the embedding function is persisted with the collection — so you set it once at creation and don't need to remember which provider you used.

## What's Good

**Most comprehensive vector DB MCP server.** 13 tools versus 2 for Qdrant and Weaviate, 9 for Pinecone. Full CRUD on both collections and documents, plus forking, plus multi-search-type queries. This is the only vector DB MCP server that gives your agent genuine operational control rather than just query access.

**Four deployment modes.** No other MCP server in any category offers this level of deployment flexibility. Ephemeral mode is perfect for agent-driven prototyping — your agent can spin up an in-memory vector store, add documents, search, and discard, all within a single conversation. Persistent mode means your agent's knowledge base survives between sessions without needing cloud infrastructure.

**Collection forking.** Unique among vector DB MCP servers. When your agent is building a RAG pipeline — experimenting with chunk sizes, embedding models, or metadata schemas — forking lets it A/B test without destructive changes. This is a thoughtful feature for agent-driven development workflows.

**HNSW parameter control.** Your agent can configure the HNSW index parameters (distance metric, construction and search efficiency, thread count, connectivity) at collection creation. This is unusual — most MCP servers hide infrastructure configuration. For agents building and tuning RAG systems, this control matters.

**Embedding function persistence.** Since Chroma v1.0.0, the embedding function is stored with the collection. This prevents the dimension mismatch errors that plagued earlier versions (and still affect naive setups where the wrong embedding model gets applied to an existing collection).

## What's Not

**Stdio transport only.** This is the server's biggest limitation. While Chroma connects to remote databases (Cloud and HTTP modes), the MCP server itself only runs locally via stdio. No remote MCP server, no OAuth, no Streamable HTTP transport. Compare this to [Neon](/reviews/neon-mcp-server/) or [Supabase](/reviews/supabase-mcp-server/) which offer hosted remote servers. For team environments where multiple developers need MCP access to the same vector store, each developer needs their own local server instance.

**No official MCP directory listing.** Despite being first-party, chroma-mcp isn't listed in the official [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) directory. This limits discoverability — developers searching for vector database MCP servers might not find it.

**Beta status with signs of slowing.** Seven releases from April to August 2025 (v0.2.0 to v0.2.6), then nothing for seven months. 11 open issues with no assignees. The server works, but the development pace suggests it may not be a priority for the Chroma team. Critical issues like the MCP dependency needing a security update (v1.10.0+) remain unaddressed.

**Query results can bloat context.** `query_documents` returns full document content by default. For collections with long documents, a single query can consume significant context window space. There's no built-in truncation or summary mode — your agent gets everything, whether it needs it or not.

**Python-only.** Requires Python 3.10+ and runs via `uvx` or `pip`. No npm package, no Go binary. If your development environment is Node.js-heavy, you'll need Python infrastructure just for this MCP server. Compare to Pinecone MCP (Node.js) or Weaviate MCP (Go).

**Known bugs.** Non-ASCII character corruption on retrieval, embedding dimension mismatches with certain configurations, and HTTP connectivity issues with self-hosted AWS deployments have been reported. These are edge cases, but they suggest the server hasn't been battle-tested at scale.

## How It Compares

| Feature | Chroma MCP | Qdrant MCP | Pinecone MCP | Weaviate MCP |
|---------|-----------|------------|--------------|--------------|
| **Stars** | 515 | 1,300 | 56 | 161 |
| **Tools** | 13 | 2 | 9 | 2 |
| **Transport** | stdio only | stdio, SSE, streamable-http | stdio | stdio |
| **Deployment modes** | 4 (ephemeral, persistent, HTTP, cloud) | Remote + local | Cloud only | Self-hosted |
| **Search types** | Vector + full-text + regex | Semantic | Text + metadata | Hybrid |
| **Collection management** | Full CRUD + fork | Auto-create only | Index management | Insert + query |
| **Embedding options** | 6 providers | FastEmbed (auto) | Integrated | Not specified |
| **Free local use** | Yes (ephemeral + persistent) | Yes (local mode) | No (cloud only) | Yes (self-hosted) |

Chroma wins on tool count and deployment flexibility. Qdrant wins on transport support and community adoption (1,300 stars). Pinecone is the only serious competitor on tool count (9 tools) but is cloud-only. Weaviate's MCP server is minimal — essentially just insert and query.

For most developers building RAG applications, Chroma MCP is the strongest choice if you want local-first development with optional cloud scaling. If you need remote MCP transport or already have a Qdrant deployment, Qdrant MCP is the better pick despite having fewer tools.

## The Bigger Picture

Vector databases are the infrastructure backbone of RAG — retrieval-augmented generation — which is how most production AI applications ground their responses in real data. Having MCP access to your vector store means your coding agent can build, populate, query, and tune RAG pipelines without you writing boilerplate embedding code.

Chroma's MCP server is the most capable in this category, but the category itself is immature. Even Chroma's 13 tools feel basic compared to what first-party servers from [Stripe](/reviews/stripe-mcp-server/) (25 tools) or [Neon](/reviews/neon-mcp-server/) (20 tools) offer in their domains. There's no monitoring, no index optimization analysis, no pipeline orchestration. The server lets your agent manage collections and documents — but it doesn't help your agent reason about *how* to build a better RAG system.

The stdio-only transport is also a strategic miss. The MCP ecosystem is clearly moving toward remote servers with OAuth — Chroma Cloud already has the authentication infrastructure for this. A hosted MCP server at something like `mcp.trychroma.com` would be a natural evolution, and the open feature request for HTTP transport suggests the community wants it.

Still, for local RAG development — prototyping, experimenting with embeddings, building knowledge bases — Chroma MCP is the best tool available. The four deployment modes mean you can start in-memory and scale to cloud without changing your MCP configuration beyond a few flags. That's a genuinely good developer experience.

## Rating: 3.5/5

The Chroma MCP server earns a 3.5/5 for being the most comprehensive vector database MCP server available — 13 tools, four deployment modes, six embedding providers, and unique features like collection forking. It loses points for stdio-only transport (no remote MCP server), beta status with stalling development (no releases in 7 months), Python-only installation, and context-bloating query results. The vector DB MCP category is still young, and Chroma leads it — but with a gap between what this server offers and what modern first-party MCP servers in other categories have achieved.

**Use this if:** You're building RAG applications and want AI-assisted vector database management with flexible deployment from local prototyping to cloud production.

**Skip this if:** You need remote MCP transport for team access, you're already invested in Qdrant or Pinecone, or your stack is Node.js-only and you don't want a Python dependency.
