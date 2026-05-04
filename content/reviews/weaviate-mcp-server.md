---
title: "The Weaviate MCP Server — First Database-Native MCP, Built Right Into the DB"
date: 2026-05-04T10:00:00+09:00
description: "Weaviate ships MCP three ways: built-in to the database itself (v1.37), a standalone Go server, and a community Python alternative."
og_description: "Weaviate pioneered database-native MCP with v1.37 — a built-in Streamable HTTP endpoint at /v1/mcp requiring zero extra infrastructure. Plus: standalone Go server (161 stars, 2 tools), community FastMCP alternative (11 tools), and a Docs MCP. Rating: 3.5/5."
content_type: "Review"
card_description: "Weaviate MCP server for AI-powered vector search and agent memory. **The first vector database to ship MCP built directly into the database** — Weaviate v1.37 exposes a Streamable HTTP endpoint at `/v1/mcp` via a single env variable, no separate process. Schema inspection, hybrid search, and optional write access — all enforced by Weaviate's standard auth. **Standalone Go server** (161 stars, 2 tools: insert + hybrid search) for pre-v1.37 users. **Community FastMCP server** (sajal2692/mcp-weaviate, 11 tools) adds list collections, get schema, get objects, semantic search, and more via uvx. Preview status and minimal standalone tooling hold it back from a higher rating."
last_refreshed: 2026-05-04
---

Part of our **[Databases MCP category](/categories/databases/)**. See also: **[Vector Database & Embedding MCP Servers roundup](/reviews/vector-database-embedding-mcp-servers/)**, **[Qdrant](/reviews/qdrant-mcp-server/)**, **[Chroma](/reviews/chroma-mcp-server/)**, **[Milvus](/reviews/milvus-mcp-server/)**, **[Pinecone](/reviews/pinecone-mcp-server/)**.

**At a glance:** Standalone server — 161 GitHub stars, 43+ forks, Go, official (Weaviate team). Built-in MCP — ships in Weaviate v1.37+ (April 23, 2026), preview feature. Weaviate core — 29,000+ GitHub stars, one of the most widely deployed open-source vector databases. Community alternative: sajal2692/mcp-weaviate (FastMCP Python, 11 tools, deployable via uvx).

Weaviate didn't just ship an MCP server. It shipped MCP *inside the database itself*.

When Weaviate v1.37 landed on April 23, 2026, it became the first vector database — and arguably the first database of any kind — to embed Model Context Protocol support directly into the core database process. No separate server to install, no glue code, no extra port to manage. Set one environment variable, and Weaviate begins serving a Streamable HTTP MCP endpoint on the same port as its REST API.

That's genuinely new. Every other MCP server in this space — [Qdrant](/reviews/qdrant-mcp-server/), [Chroma](/reviews/chroma-mcp-server/), [Milvus](/reviews/milvus-mcp-server/), [Pinecone](/reviews/pinecone-mcp-server/) — is a separate process you run alongside your database. Weaviate's built-in server is architecturally different: it's the database answering MCP calls directly.

The tradeoff is where it gets complicated. The built-in server is a preview feature — the API may change. The standalone Go server is minimal (2 tools). The community Python alternative adds depth but comes with the usual caveats of third-party maintenance. What Weaviate offers in architectural ambition, it's still building out in practical completeness.

## Three Ways to Connect

Weaviate ships MCP in three distinct forms:

### 1. Built-in MCP Server (v1.37+) — The Headline

Enable with a single environment variable in your `docker-compose.yml` or Weaviate configuration:

```yaml
environment:
  MCP_SERVER_ENABLED: 'true'
  # Optional: enable tools that can write data back to Weaviate
  MCP_SERVER_WRITE_ACCESS_ENABLED: 'true'
```

Once enabled, Weaviate exposes a **Streamable HTTP endpoint at `/v1/mcp`** on the same port as the REST API (typically 8080). Connect any MCP-aware tool to `http://your-weaviate-host:8080/v1/mcp`.

In your Claude Desktop or Claude Code config:

```json
{
  "mcpServers": {
    "weaviate": {
      "url": "http://localhost:8080/v1/mcp"
    }
  }
}
```

No `command`, no `args`, no `uvx` — just a URL. That's the zero-infrastructure promise in action.

Authentication is handled by Weaviate's existing auth layer. If your Weaviate instance requires an API key, the MCP endpoint does too. If you've configured OIDC or anonymous access, those rules apply to MCP as well. The database doesn't need a second security model.

**What the built-in server can do:**
- Inspect collection schemas (understand what data is in the database)
- Run hybrid searches (BM25 + vector, Weaviate's core strength)
- Write data back into collections (when `MCP_SERVER_WRITE_ACCESS_ENABLED: 'true'`)

**Caveat:** This is a **preview feature**. The Weaviate team explicitly notes that the API and behavior may change in future releases. Teams building production pipelines around this endpoint should expect possible breaking changes as Weaviate iterates.

### 2. Standalone Go Server (mcp-server-weaviate)

For teams not yet on v1.37, or those who prefer a separate MCP process, the official [weaviate/mcp-server-weaviate](https://github.com/weaviate/mcp-server-weaviate) repository provides a standalone server written in Go.

**Tools provided:**

| Tool | Purpose |
|------|---------|
| Insert object | Add data to a Weaviate collection |
| Retrieve objects | Query with hybrid search (BM25 + vector) |

Two tools — the same minimal footprint as the [Qdrant MCP server](/reviews/qdrant-mcp-server/). The philosophy mirrors Qdrant's: give the agent a way to write and a way to read; everything else stays in the native client.

Setup requires building from source and pointing environment variables at your Weaviate instance:

```bash
git clone https://github.com/weaviate/mcp-server-weaviate
cd mcp-server-weaviate
go build -o mcp-server ./cmd/server
```

Key configuration variables: `WEAVIATE_HOST`, `WEAVIATE_SCHEME`, and `PORT` (defaults to 8675). Verify it's running: `curl http://localhost:8675/healthz`.

In your MCP client config:

```json
{
  "mcpServers": {
    "weaviate": {
      "command": "/path/to/mcp-server",
      "env": {
        "WEAVIATE_HOST": "localhost:8080",
        "WEAVIATE_SCHEME": "http"
      }
    }
  }
}
```

The Go implementation offers low-latency, low-memory-overhead access to any Weaviate instance — self-hosted, Docker, Kubernetes, or Weaviate Cloud. Transport is stdio only.

### 3. Community FastMCP Server (sajal2692/mcp-weaviate)

For teams that need more tool coverage than the official server provides, [sajal2692/mcp-weaviate](https://github.com/sajal2692/mcp-weaviate) is a FastMCP-based Python server deployable via `uvx`.

**Tools provided (11 total):**

| Tool | Purpose |
|------|---------|
| `get_config` | Retrieve Weaviate instance configuration |
| `check_connection` | Verify database connectivity |
| `list_collections` | List all collections in the instance |
| `get_schema` | Get schema for a specific collection |
| `get_collection_objects` | Retrieve objects from a collection |
| `search` | Keyword-based search |
| `semantic_search` | Vector similarity search |
| + additional tools | Further collection and object operations |

This 11-tool set makes the community server significantly more capable than the official standalone server for agents that need to explore database structure, validate connections, or mix search strategies.

Deploy via uvx (no install required):

```json
{
  "mcpServers": {
    "weaviate": {
      "command": "uvx",
      "args": ["mcp-weaviate"],
      "env": {
        "WEAVIATE_URL": "http://localhost:8080",
        "WEAVIATE_API_KEY": "your-api-key"
      }
    }
  }
}
```

### 4. Docs MCP Server (Bonus)

Weaviate also ships a [Docs MCP Server](https://docs.weaviate.io/weaviate/mcp/docs-mcp-server) that lets AI agents access Weaviate's documentation directly through MCP. This is a separate server from the database MCP — useful for agents that need to reference Weaviate concepts, API details, or configuration options while working. Not covered in depth here since it's a documentation tool rather than a database tool.

## About Weaviate

Before evaluating the MCP layer, it's worth understanding what's underneath. Weaviate is a major open-source vector database with 29,000+ GitHub stars — in the same tier as Qdrant (23,000+) and Milvus (40,000+). It's one of the three most widely deployed dedicated vector databases in production AI systems.

Weaviate's technical strengths:

**Hybrid search as a first-class feature.** Weaviate combines BM25 keyword search with vector similarity search at the query level, not as an afterthought. The hybrid search parameter controls the blend ratio between keyword and vector results. This is the search mode exposed by both the built-in MCP and the standalone Go server.

**Multi-tenancy by design.** Weaviate's tenant isolation is one of its strongest enterprise features — separate data, separate indexes, shared infrastructure. At scale, this makes Weaviate a natural fit for SaaS applications serving multiple customers with isolated knowledge bases.

**Generative search (RAG in the database).** Weaviate can run retrieval-augmented generation at query time, passing retrieved vectors to an LLM and returning the generated response. This is a database-level RAG capability — unusual in the vector DB space.

**Available everywhere.** Self-hosted via Docker or Kubernetes, or managed on Weaviate Cloud. The MCP server supports all deployment modes.

## What's Good

**Database-native MCP is architecturally significant.** The built-in v1.37 server isn't just a convenience — it's a different model for how databases interact with AI agents. Instead of a separate process translating MCP calls into database API calls, the database answers MCP calls directly. This eliminates a network hop, a process to maintain, and a deployment artifact to manage. If this approach spreads to other databases, the built-in server pattern will be Weaviate's legacy in the MCP ecosystem. Weaviate was first.

**Zero infrastructure for v1.37 users.** If you're already running Weaviate, the upgrade path is a single environment variable. No package to install, no process to manage, no port to open beyond what's already open. The MCP endpoint appears on the existing Weaviate port alongside the REST API. This is the lowest-friction path to adding MCP to a production vector database we've seen — including [Neon](/reviews/neon-mcp-server/), [Supabase](/reviews/supabase-mcp-server/), and [Firebase](/reviews/firebase-mcp-server/).

**Weaviate's auth model extends naturally to MCP.** One of the messier problems in the MCP ecosystem is authentication — most servers bolt on API keys at the MCP layer without integrating with the underlying system's auth. Weaviate's built-in server sidesteps this by using the database's existing auth layer. If your Weaviate instance is secured, the MCP endpoint inherits that security automatically.

**Hybrid search out of the box.** The standalone Go server and the built-in server both expose Weaviate's hybrid search — BM25 + vector combined — not just one or the other. [Qdrant MCP](/reviews/qdrant-mcp-server/) is semantic (vector) only. [Milvus MCP](/reviews/milvus-mcp-server/) requires Milvus 2.6.0+ for text similarity. Weaviate's hybrid search is available to all MCP clients regardless of version.

**Go-based standalone server.** The official standalone server in Go has lower memory overhead and startup time than Python-based equivalents ([Qdrant MCP](/reviews/qdrant-mcp-server/), [Chroma MCP](/reviews/chroma-mcp-server/), [Milvus MCP](/reviews/milvus-mcp-server/)). For production deployments where process resources matter, the language choice is a practical advantage.

**Community alternative fills the tool gap.** The sajal2692/mcp-weaviate server's 11 tools meaningfully expand what agents can do — listing collections, fetching schemas, and mixing search strategies. The `uvx` deployment model (no install required) is developer-friendly. It doesn't have the adoption numbers of [Chroma MCP](/reviews/chroma-mcp-server/) (535 stars) or [Qdrant MCP](/reviews/qdrant-mcp-server/) (1,357 stars), but it covers use cases the official server can't.

## What's Not

**Built-in server is preview.** "API and behavior may change in future releases" is a real caveat for production teams. If Weaviate changes the tool names, parameters, or behavior of `/v1/mcp` in v1.38 or v1.39, your agent prompts and workflows may break. This is a normal stage for a new feature, but it means the built-in server isn't production-ready for teams that can't absorb churn.

**Standalone server: only 2 tools.** The official Go server matches Qdrant's minimalism — insert and hybrid query. No collection management, no schema inspection, no delete, no list. Unlike Qdrant's server (which at least auto-creates collections and supports embedded local mode), the Weaviate standalone server requires a pre-existing Weaviate instance and pre-existing collections. Agents can't bootstrap their own database structure through MCP. Compare to [Chroma MCP](/reviews/chroma-mcp-server/) with 13 tools including full collection CRUD, or [Milvus MCP](/reviews/milvus-mcp-server/) with 11 tools including five search types.

**No delete capability in either official server.** Neither the built-in MCP nor the standalone Go server exposes a delete tool. If your agent writes incorrect data, there's no MCP interface to remove it. You'd need to use the Weaviate REST API or client library directly. This is a gap shared with [Qdrant MCP](/reviews/qdrant-mcp-server/).

**Standalone server requires building from source.** Unlike `uvx mcp-server-qdrant` (Qdrant) or `uvx chroma-mcp` (Chroma), the official Weaviate standalone server has no npm or PyPI package. You clone the repo and run `go build`. This raises the setup bar meaningfully — developers without a Go toolchain need to install one first.

**Low adoption on standalone server.** 161 stars is modest compared to Qdrant (1,357), Chroma (535), and Milvus (228). The standalone server is unlikely to become a community focal point now that the built-in server exists — which means community extensions, forks, and ecosystem tooling are unlikely to accumulate around it.

**No stdio transport for built-in server.** The built-in MCP endpoint is Streamable HTTP only — no stdio support. This is actually appropriate for a database-native server (stdio doesn't make sense for an in-process endpoint), but it means the built-in server can't be used with MCP clients that only support stdio. The standalone Go server is stdio only, going the other direction.

## How It Compares

| Feature | Weaviate MCP | Qdrant MCP | Chroma MCP | Milvus MCP | Pinecone MCP |
|---------|-------------|-----------|------------|------------|--------------|
| **Stars (standalone)** | 161 | 1,357 | 535 | 228 | 64 |
| **Tools (official)** | 2 (standalone) / built-in (preview) | 2 | 13 | 11 | 9 |
| **Transport** | stdio (standalone) + Streamable HTTP (built-in) | stdio, SSE, Streamable HTTP | stdio only | stdio, SSE | stdio |
| **Search types** | Hybrid (BM25 + vector) | Semantic only | Vector + full-text + regex | Hybrid (5 types) | Text + metadata |
| **Collection mgmt** | None in official servers | Auto-create only | Full CRUD + fork | Full CRUD | Index management |
| **Delete capability** | No | No | Yes | Yes | Yes |
| **Local mode** | Yes (self-hosted Docker) | Yes (embedded) | Yes (4 modes) | No | No |
| **Language** | Go (standalone) / embedded (built-in) | Python | Python | Python | TypeScript |
| **Install method** | Build from source / built-in | `uvx` | `uvx` | `pip` | `npm` |
| **DB-native MCP** | **Yes (built-in v1.37)** | No | No | No | No |
| **Auth integration** | Database auth (built-in) | API key | None | None | API key |

The comparison makes Weaviate's unusual position clear. On the standalone server metrics — stars, tools, install ease — Weaviate trails Qdrant, Chroma, and Milvus significantly. But on architectural innovation (database-native MCP, auth integration, Streamable HTTP by default), Weaviate leads the category.

This is a server worth evaluating if you're already on Weaviate v1.37+. It's a harder sell as a reason to adopt Weaviate from scratch, where [Qdrant MCP](/reviews/qdrant-mcp-server/) (for semantic memory) or [Chroma MCP](/reviews/chroma-mcp-server/) (for comprehensive database management) offer more mature MCP surface area today.

## The Bigger Picture

The built-in MCP server in Weaviate v1.37 represents a different theory of where MCP servers belong in the stack. Right now, MCP is largely conceived as an integration layer — you have your tools (databases, APIs, file systems), and you run MCP servers as adapters between those tools and your AI agent. Weaviate's approach asks: what if the tool is the MCP server?

This model has real advantages as the MCP ecosystem matures. Fewer moving parts. Consistent auth. No version drift between the MCP adapter and the database it wraps. Potentially tighter optimization — the database knows exactly what a hybrid search query needs and can run it natively rather than translating from MCP through a client library.

The question is whether other databases follow. If Weaviate's built-in approach proves operationally superior — and the preview evolves to GA with a stable API — it could influence how PostgreSQL extensions, Redis modules, and other databases think about MCP integration. Weaviate is writing the playbook.

For now, the practical picture is this: if you're running Weaviate v1.37+ and want to give AI agents access to your vector database, the built-in server is the obvious starting point. Set `MCP_SERVER_ENABLED: 'true'`, point your agent at `/v1/mcp`, and you're connected. Expect the API to evolve. Watch the v1.38 release notes.

If you're not yet on v1.37, or you need more tool coverage, the community sajal2692/mcp-weaviate server with 11 tools is the better choice over the minimal official standalone Go server. And if you're evaluating vector DB MCP servers without being committed to Weaviate, [Chroma MCP](/reviews/chroma-mcp-server/) (13 tools, full CRUD) or [Qdrant MCP](/reviews/qdrant-mcp-server/) (best transport support, 745K weekly downloads) are better-established options today.

## Rating: 3.5/5

Weaviate earns a 3.5/5 for pioneering database-native MCP — the first vector database (and likely first database of any kind) to ship MCP built directly into the database process. The built-in v1.37 server is a genuine architectural innovation: zero-infrastructure, database-auth-integrated, Streamable HTTP on the existing port. Weaviate's hybrid search and production pedigree (29,000+ stars) make it a credible foundation.

What holds it back: the built-in server is preview with potential API changes, the standalone Go server offers only 2 tools with no delete capability and requires building from source, and adoption metrics lag behind Qdrant and Chroma significantly. The innovation is real but the practical maturity isn't there yet.

**Use this if:** You're already running Weaviate v1.37+ and want zero-infrastructure MCP access, you value database-auth-integrated MCP endpoints, or you need hybrid BM25+vector search through MCP without configuring two separate search strategies.

**Skip this if:** You need stable (non-preview) MCP APIs for production pipelines, you want your agent to manage database structure (create/delete collections), you need a standalone server you can install via `uvx` or `npm`, or you're evaluating vector DB MCP servers without an existing Weaviate deployment.

*This review was researched and written by an AI agent (Claude Sonnet 4.6, Anthropic) and has not been independently verified by a human editor. We have not tested this MCP server hands-on. All claims are based on publicly available documentation, GitHub data, and community sources as of May 2026. [Rob Nugen](https://robnugen.com) oversees this project. Last updated 2026-05-04.*
