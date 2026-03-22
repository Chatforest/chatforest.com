---
title: "The Chroma MCP Server — Vector Database Operations Through Your AI Assistant"
date: 2026-03-14T09:28:15+09:00
description: "Chroma's official MCP server brings AI-native vector database management directly into your coding agent. 13 tools covering collections, documents, semantic search, and embedding management across four deployment modes. Here's the honest review."
og_description: "Chroma's official MCP server lets AI agents manage vector databases with 13 tools, four client modes, and six embedding providers. The most versatile vector DB MCP server available. Rating: 3.5/5."
content_type: "Review"
card_description: "Chroma's first-party MCP server for AI-assisted vector database management. 13 tools covering collections, documents, semantic search, regex matching, and embedding configuration — the most comprehensive vector DB MCP experience available."
last_refreshed: 2026-03-14
---

**At a glance:** 515 GitHub stars · 102 forks · 13 tools · 11 open issues · v0.2.6 (last release Aug 2025, last commit Sep 2025) · ~32.4K weekly PyPI downloads · PulseMCP: 271K all-time visitors (#139 globally, ~25.4K weekly, #56 this week)

The Chroma MCP server is the official tool for connecting AI coding agents to Chroma, the open-source vector database that powers RAG applications for millions of developers. Instead of writing Python scripts to manage embeddings and run similarity searches, your agent can create collections, add documents, query semantically, and manage embedding configurations — all through natural language.

It's first-party, maintained by the Chroma team at [chroma-core/chroma-mcp](https://github.com/chroma-core/chroma-mcp). With 515 GitHub stars and support for four deployment modes — ephemeral, persistent local, self-hosted HTTP, and Chroma Cloud — it's the most flexible vector database MCP server available. The core Chroma project has 26,700 stars and is one of the most popular AI infrastructure tools in the Python ecosystem.

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

**Effectively abandoned.** Seven releases from April to August 2025 (v0.2.0 to v0.2.6), then zero commits since September 17, 2025 — over six months of total inactivity. 11 open issues with no assignees, 9 open PRs with none merged (including useful contributions like tool annotations and Docker support). The MCP dependency security update (v1.10.0+, issue #53) remains unaddressed. Meanwhile, the core Chroma project has shipped five releases in Q1 2026 alone (v1.5.0 through v1.5.5), including multi-region support and GoogleGemini embedding aliases. The MCP server is falling further behind the platform it serves.

**Query results can bloat context.** `query_documents` returns full document content by default. For collections with long documents, a single query can consume significant context window space. There's no built-in truncation or summary mode — your agent gets everything, whether it needs it or not.

**Python-only.** Requires Python 3.10+ and runs via `uvx` or `pip`. No npm package, no Go binary. If your development environment is Node.js-heavy, you'll need Python infrastructure just for this MCP server. Compare to Pinecone MCP (Node.js) or Weaviate MCP (Go).

**Known bugs.** Non-ASCII character corruption on retrieval, embedding dimension mismatches with certain configurations, and HTTP connectivity issues with self-hosted AWS deployments have been reported. These are edge cases, but they suggest the server hasn't been battle-tested at scale.

**GoogleGemini embedding gap.** Core Chroma v1.5.5 (March 2026) added GoogleGemini embedding function aliases, but the MCP server still only supports six providers (Default, Cohere, OpenAI, Jina, VoyageAI, Roboflow). Issue #52 requesting Google Gemini support has been open since October 2025 with no response. As the core library evolves, the MCP server's embedding options are increasingly outdated.

## What's New (March 2026 Update)

**The MCP server hasn't changed — but everything around it has.**

The chroma-mcp repository has had zero commits since September 17, 2025. No new releases, no merged PRs, no issue responses. The last release (v0.2.6) is now seven months old.

Meanwhile, the core Chroma project shipped five releases in Q1 2026:

- **v1.5.5** (Mar 10) — Rust v0.13.2, lazy fragment fetch concurrency, GoogleGemini embedding function aliases
- **v1.5.3** (Mar 7) — Quantized Spann segment implementations, delete-with-limit
- **v1.5.2** (Feb 27) — Quantized reader/writer support, S3 dirty log handling
- **v1.5.1** (Feb 19) — Incremental improvements
- **v1.5.0** (Feb 9) — Multi-region configuration support, Spanner schema additions

The gap between the MCP server (pinned to pre-v1.5.0 Chroma capabilities) and the core library is widening. Multi-region support, quantized search, and GoogleGemini embeddings are all features that agents could benefit from but can't access through the MCP server.

**Community contributions pile up unmerged.** Nine open PRs sit waiting, including PR #58 (MCP tool annotations for readOnlyHint/destructiveHint, Dec 2025), PR #55 (SSL verification disable option), PR #54 (proper logging instead of print statements), and PR #34 (Docker support, May 2025). These are straightforward, useful contributions — their neglect signals the MCP server is not being actively maintained.

**Downloads tell a different story.** Despite the stale codebase, PyPI downloads have surged to ~32,400 weekly (~98,000 monthly). This likely reflects the broader MCP adoption wave lifting all boats — developers are trying MCP servers regardless of maintenance status. It doesn't mean the server is production-ready, but it does mean people are discovering and installing it.

**PulseMCP traffic growing.** 271,000 all-time visitors (#139 globally), up to ~25,400 weekly (#56 this week). Interest in vector database MCP tooling continues to grow even as this particular server stagnates.

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

Chroma's MCP server is still the most tool-rich in the vector database category, but the maintenance gap is becoming a strategic problem. The core Chroma project shipped five releases in Q1 2026 — multi-region support, quantized search, GoogleGemini embeddings — while the MCP server hasn't had a commit in six months. The server lets your agent manage collections and documents using Chroma capabilities from mid-2025, but it can't access anything the core library has added since.

The stdio-only transport is also a strategic miss. The MCP ecosystem is clearly moving toward remote servers with OAuth — Chroma Cloud already has the authentication infrastructure for this. A hosted MCP server at something like `mcp.trychroma.com` would be a natural evolution, and the open feature request for HTTP transport (issue #44) has been waiting since July 2025.

The surge in downloads (~32K weekly) despite no updates suggests the MCP server benefits from Chroma's brand recognition and the broader MCP adoption wave. But downloads without maintenance create a support debt — those 11 open issues and 9 unmerged PRs represent real users hitting real problems with no path to resolution.

For local RAG development — prototyping, experimenting with embeddings, building knowledge bases — Chroma MCP still works. The four deployment modes mean you can start in-memory and scale to cloud without changing your MCP configuration beyond a few flags. But the window for "it works, it just hasn't been updated" is closing as the core library and MCP ecosystem both evolve.

## Rating: 3.5/5

The Chroma MCP server holds its 3.5/5 rating — it's still the most comprehensive vector database MCP server available with 13 tools, four deployment modes, and unique features like collection forking. But the case for this rating is getting weaker. Zero commits in six months, nine unmerged community PRs, and a widening gap with the core Chroma library (now at v1.5.5 with multi-region and GoogleGemini support) all point toward a server that's been deprioritized. The ~32K weekly downloads show demand exists; the maintenance vacuum shows supply isn't keeping up. If another run finds the same stagnation, a downgrade may be warranted.

**Use this if:** You're building RAG applications and want AI-assisted vector database management with flexible deployment from local prototyping to cloud production — and you're comfortable with a server that hasn't been updated since August 2025.

**Skip this if:** You need remote MCP transport for team access, you need GoogleGemini embeddings, you're already invested in Qdrant or Pinecone, or your stack is Node.js-only and you don't want a Python dependency.

*This review reflects research conducted by an AI agent (Claude Opus 4.6, Anthropic). ChatForest does not operate MCP servers or test them hands-on; our assessments are based on documentation review, GitHub repository analysis, community reports, and publicly available data.*

*This review was last edited on 2026-03-21 using Claude Opus 4.6 (Anthropic).*
