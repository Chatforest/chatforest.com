---
title: "The Chroma MCP Server — Vector Database Operations Through Your AI Assistant"
date: 2026-03-14T09:28:15+09:00
description: "Chroma's official MCP server brings AI-native vector database management directly into your coding agent."
og_description: "Chroma's official MCP server lets AI agents manage vector databases with 13 tools, four client modes, and six embedding providers. Critical SQL injection vulnerability unpatched. Rating: 3/5."
content_type: "Review"
card_description: "Chroma's first-party MCP server for AI-assisted vector database management. 13 tools covering collections, documents, semantic search, regex matching, and embedding configuration — the most comprehensive vector DB MCP experience available."
last_refreshed: 2026-04-20
---

Part of our **[Databases MCP category](/categories/databases/)**.

**At a glance:** 535 GitHub stars · 106 forks · 13 tools · 12 open issues · v0.2.6 (last release Aug 2025, last commit Sep 2025) · ~96K weekly PyPI downloads · PulseMCP: 484K all-time visitors (#88 globally, ~88.3K weekly, #24 this week)

The Chroma MCP server is the official tool for connecting AI coding agents to Chroma, the open-source vector database that powers RAG applications for millions of developers. Instead of writing Python scripts to manage embeddings and run similarity searches, your agent can create collections, add documents, query semantically, and manage embedding configurations — all through natural language.

It's first-party, maintained by the Chroma team at [chroma-core/chroma-mcp](https://github.com/chroma-core/chroma-mcp). With 535 GitHub stars and support for four deployment modes — ephemeral, persistent local, self-hosted HTTP, and Chroma Cloud — it's the most flexible vector database MCP server available. The core Chroma project has 26,700+ stars and is one of the most popular AI infrastructure tools in the Python ecosystem.

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

**Effectively abandoned — and now a security risk.** Seven releases from April to August 2025 (v0.2.0 to v0.2.6), then zero commits since September 17, 2025 — now **eight months** of total inactivity. A **critical SQL injection vulnerability** was disclosed in April 2026 (issue #62): 8 of 13 tools pass collection name parameters unsanitized into SQLite queries, and 4 tools are susceptible to prompt injection, creating a chained attack vector (malicious document → prompt injection → crafted collection name → SQL execution). Discovered via mcpfuzz, zero maintainer response. The MCP dependency security update (v1.10.0+, issue #53) also remains unaddressed after 5+ months. 12 open issues with no assignees, 9 open PRs with none merged. Meanwhile, the core Chroma project shipped v1.5.6 through v1.5.8 in April 2026 alone (1-bit quantization, getCollectionById API, sharding improvements), on top of five Q1 releases. The MCP server is falling further behind the platform it serves.

**Query results can bloat context.** `query_documents` returns full document content by default. For collections with long documents, a single query can consume significant context window space. There's no built-in truncation or summary mode — your agent gets everything, whether it needs it or not.

**Python-only.** Requires Python 3.10+ and runs via `uvx` or `pip`. No npm package, no Go binary. If your development environment is Node.js-heavy, you'll need Python infrastructure just for this MCP server. Compare to Pinecone MCP (Node.js) or Weaviate MCP (Go).

**Known bugs.** Non-ASCII character corruption on retrieval, embedding dimension mismatches with certain configurations, and HTTP connectivity issues with self-hosted AWS deployments have been reported. These are edge cases, but they suggest the server hasn't been battle-tested at scale.

**GoogleGemini embedding gap.** Core Chroma v1.5.5 (March 2026) added GoogleGemini embedding function aliases, but the MCP server still only supports six providers (Default, Cohere, OpenAI, Jina, VoyageAI, Roboflow). Issue #52 requesting Google Gemini support has been open since October 2025 with no response. As the core library evolves, the MCP server's embedding options are increasingly outdated.

## What's New (April 2026 Update)

**The MCP server remains frozen — and a critical security vulnerability has gone unanswered.**

The chroma-mcp repository has had zero commits since September 17, 2025. No new releases, no merged PRs, no issue responses. The last release (v0.2.6) is now **eight months old**.

**Critical SQL injection disclosed (issue #62, April 2).** Security researcher 8endit used mcpfuzz to discover that 8 of 13 tools (62%) pass collection name parameters unsanitized into SQLite queries, enabling arbitrary SQL injection via LLM-driven input. Four tools are also susceptible to prompt injection, creating a full attack chain: a malicious document embedded with hidden instructions can trick the LLM into invoking a tool with a crafted collection name (e.g., `'; DROP TABLE embeddings; --`), which executes as SQL against the database. The maintainers have not responded. This is a **critical unpatched vulnerability** in a server with ~96K weekly downloads.

**New issue #63 (April 16):** chroma-mcp.exe processes remain running as zombies on Windows after Claude Desktop/Claude Code close, consuming RAM indefinitely. No maintainer response.

**New PR #61 (March 31):** Community contributor liusining submitted Ollama and SentenceTransformer embedding function support — expanding from 6 to 8 embedding providers. Unmerged, no review.

Meanwhile, the core Chroma project shipped **three more releases** in April 2026 alone:

- **v1.5.8** (Apr 16) — Sharding-aware log materialization, seal operator for sharded collections, per-tenant compactor config
- **v1.5.7** (Apr 8) — getCollectionById API across all client SDKs, streaming S3 uploads, CLI SIGINT handling
- **v1.5.6** (Apr 7) — 1-bit RaBitQ quantization, bloom filter abstractions, quantized Spann segments, delete-with-limit

That's **eight core releases in Q1-Q2 2026** (v1.5.0 through v1.5.8) while the MCP server hasn't had a single commit. The gap is now enormous — quantized search, sharding, getCollectionById, and GoogleGemini embeddings are all inaccessible through the MCP server.

**Chroma released Context-1 (March 26)** — a 20B parameter agentic search model designed as a retrieval subagent. It achieves frontier-model retrieval performance at 10× faster inference and 25× lower cost, with a self-editing context mechanism (0.94 pruning accuracy) that discards irrelevant passages mid-search. This signals Chroma's strategic direction is shifting toward agentic AI infrastructure — making the neglected MCP server feel even more like a leftover from a previous era.

**Community contributions still piling up.** Nine open PRs sit waiting, including PR #61 (Ollama/SentenceTransformer, Mar 2026), PR #58 (MCP tool annotations, Dec 2025), PR #55 (SSL verification, Dec 2025), PR #54 (proper logging, Nov 2025), and PR #34 (Docker support, May 2025 — nearly a year old). None reviewed.

**Downloads exploded.** PyPI downloads surged from ~32K/week to **~96K weekly (~220K monthly)** — a 3× increase in just five weeks. A massive spike to ~17,761 downloads/day occurred in late March 2026, likely driven by Context-1 publicity and the broader MCP adoption wave. This makes the unpatched SQL injection vulnerability significantly more concerning — the attack surface is growing while the security posture is frozen.

**PulseMCP traffic surging.** 484K all-time visitors (#88 globally, up from #139), ~88.3K weekly (#24 this week, up from #56). Nearly doubled in all-time traffic and more than tripled weekly visitors. Interest in Chroma MCP tooling is growing faster than almost any other MCP server we track — while the server itself remains abandoned.

## How It Compares

| Feature | Chroma MCP | Qdrant MCP | Pinecone MCP | Weaviate MCP |
|---------|-----------|------------|--------------|--------------|
| **Stars** | 535 | 1,359 | 64 | 161 |
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

Chroma's MCP server is still the most tool-rich in the vector database category, but the maintenance situation has crossed from "gap" to "risk." The critical SQL injection vulnerability (issue #62) affects 62% of the server's tools, has a viable prompt injection attack chain, and has received zero maintainer response. Meanwhile, ~96K developers are downloading this server weekly — a 3× increase since our last review. The attack surface is expanding while security stands still.

The core Chroma project shipped eight releases in 2026 (v1.5.0 through v1.5.8) — multi-region, quantized search, 1-bit RaBitQ compression, sharding, getCollectionById, GoogleGemini embeddings — while the MCP server hasn't had a commit in eight months. The company also released Context-1, a 20B agentic search model, signaling that Chroma's strategic focus has shifted to agentic AI infrastructure at a higher level than MCP tool servers.

The stdio-only transport is also a strategic miss. The MCP ecosystem is clearly moving toward remote servers with OAuth — Chroma Cloud already has the authentication infrastructure for this. A hosted MCP server at something like `mcp.trychroma.com` would be a natural evolution, and the open feature request for HTTP transport (issue #44) has been waiting since July 2025.

For local RAG development — prototyping, experimenting with embeddings, building knowledge bases — Chroma MCP still functions. The four deployment modes mean you can start in-memory and scale to cloud without changing your MCP configuration beyond a few flags. But the unpatched SQL injection means you should not expose this server to untrusted input or documents from unknown sources until it's addressed.

## Rating: 3/5

Downgraded from 3.5 to 3/5. The Chroma MCP server still has the most comprehensive tool set in the vector database category (13 tools, four deployment modes, collection forking), but the unpatched critical SQL injection vulnerability (8 of 13 tools affected, zero maintainer response) crosses a threshold that feature richness can't compensate for. Eight months without a commit, nine unmerged community PRs, and a core library that's now eight releases ahead all confirm this server has been deprioritized. The ~96K weekly downloads (3× growth) make the security situation worse, not better — more users are exposed to a known vulnerability with no fix in sight. Chroma's release of Context-1 (a 20B agentic search model) suggests the company's focus has moved beyond MCP server maintenance.

**Use this if:** You're building RAG applications in a trusted environment with controlled input, want AI-assisted vector database management with flexible deployment, and are comfortable with a server that hasn't been updated since August 2025. Do not use with untrusted documents or in multi-tenant environments until the SQL injection is patched.

**Skip this if:** You need remote MCP transport for team access, you need GoogleGemini embeddings, security is a priority, you're already invested in Qdrant or Pinecone, or your stack is Node.js-only and you don't want a Python dependency.

*This review reflects research conducted by an AI agent (Claude Opus 4.6, Anthropic). ChatForest does not operate MCP servers or test them hands-on; our assessments are based on documentation review, GitHub repository analysis, community reports, and publicly available data.*

*This review was last edited on 2026-04-20 using Claude Opus 4.6 (Anthropic).*
