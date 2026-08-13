---
title: "The Milvus MCP Server — The Most Popular Vector Database Gets an AI Interface"
date: 2026-03-14T11:07:09+09:00
description: "Zilliz's official MCP server for Milvus brings 12 tools covering five search types, full collection management, and data operations to your AI coding agent. Here's the honest review."
og_description: "Milvus has 45,000+ GitHub stars and powers AI at NVIDIA, Salesforce, and eBay. Its MCP server has 12 tools with hybrid search, full CRUD, and SSE/Streamable HTTP transport. Rating: 3.5/5."
content_type: "Review"
card_description: "Zilliz's official MCP server for the most-starred open-source vector database. 12 tools covering five search modes, full collection CRUD, and data operations — the strongest self-hosted vector DB MCP experience."
last_refreshed: 2026-08-14
sources_audited: 2026-08-14
---

Part of our **[Databases MCP category](/categories/databases/)**.

**At a glance:** [240 GitHub stars, 71 forks, 44 commits](https://github.com/zilliztech/mcp-server-milvus), last commit Aug 11, 2026, [v0.1.1.dev9 (PyPI)](https://pypi.org/project/mcp-server-milvus/), 12 tools, Python, Apache-2.0, [PulseMCP ~48.6K all-time visitors](https://www.pulsemcp.com/servers/zilliz-milvus). [Milvus core: 45,600+ stars, v3.0.0 (Jul 29, 2026)](https://github.com/milvus-io/milvus/releases).

The Milvus MCP server is the official tool for connecting AI coding agents to Milvus, the open-source vector database that has become the most-starred in its category on GitHub with [over 45,000 stars](https://github.com/milvus-io/milvus). Instead of writing Python scripts to manage collections and run similarity searches, your agent can create collections, insert data, run hybrid searches, and manage infrastructure — all through natural language.

It's maintained by Zilliz (the company behind Milvus) at [zilliztech/mcp-server-milvus](https://github.com/zilliztech/mcp-server-milvus). With [240 GitHub stars, 71 forks](https://github.com/zilliztech/mcp-server-milvus), and support for stdio, SSE, and (as of May 2026) Streamable HTTP transport, it's the most complete self-hosted vector database MCP server available. [Milvus itself powers AI systems at NVIDIA, Salesforce, eBay, Airbnb, and DoorDash — over 10,000 enterprise teams in production](https://www.prnewswire.com/news-releases/milvus-surpasses-40-000-github-stars-reinforcing-leadership-in-open-source-vector-databases-302646510.html).

This is our fourth vector database MCP server review after [Chroma](/reviews/chroma-mcp-server/) (3/5), [Qdrant](/reviews/qdrant-mcp-server/) (3/5), and [Pinecone](/reviews/pinecone-mcp-server/) (3/5). The Milvus server matches Chroma's ambition with a different set of strengths.

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

**Streamable HTTP mode (added May 2026, recommended for production):**

```json
{
  "mcpServers": {
    "milvus-streamable-http": {
      "url": "http://your_host:port/mcp",
      "disabled": false,
      "autoApprove": []
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

**Still pre-release — but no longer abandoned.** [44 commits](https://github.com/zilliztech/mcp-server-milvus/commits/main), still no versioned GitHub release, still on [PyPI dev build 0.1.1.dev9](https://pypi.org/project/mcp-server-milvus/) (unchanged since Nov 2025). An earlier version of this review (audited before 2026-07-22) reported the last commit as December 24, 2025 and called the project effectively abandoned — that was wrong even at the time: five PRs merged May 7–8, 2026 (including [#57](https://github.com/zilliztech/mcp-server-milvus/pull/57), streamable-HTTP support, and a fix for the service-hang bug tracked as [#51](https://github.com/zilliztech/mcp-server-milvus/issues/51)), a dependency cleanup landed in July, and a bug fix commit shipped [August 11, 2026](https://github.com/zilliztech/mcp-server-milvus/commits/main) — three days before this re-audit. A dependency-compatibility PR ([#80](https://github.com/zilliztech/mcp-server-milvus/pull/80)) is open now. Real maintenance is happening; it's just still unversioned and Zilliz's public messaging (see "The Bigger Picture" below) suggests MCP isn't the company's primary strategic bet going forward.

**Open security report with no response.** [Issue #75](https://github.com/zilliztech/mcp-server-milvus/issues/75), opened June 12, 2026, describes a Broken Object Level Authorization gap: tools accept a `collection_name` parameter with no per-user authorization check, so in a multi-tenant deployment any client using the server's single credential can discover and read any collection, not just ones it should have access to. As of this audit the issue has no assigned owner and no PR addressing it. Anyone deploying this server for more than one user/tenant should treat that as a hard blocker until it's fixed.

**Python-only.** Requires Python 3.10+ and the `uv` package manager. No npm package, no Go binary. If your development stack is Node.js or Go, you'll need Python infrastructure for this server. [Pinecone MCP](/reviews/pinecone-mcp-server/) is TypeScript-based, which integrates more naturally into JavaScript workflows.

**No embedding configuration.** The server relies on Milvus's built-in embedding functions or pre-computed embeddings. Unlike [Chroma MCP](/reviews/chroma-mcp-server/) (six embedding providers: OpenAI, Cohere, Jina, VoyageAI, Roboflow, Default), there's no MCP-level control over which embedding model to use. You configure embeddings in Milvus itself, not through the MCP server.

## How It Compares

| Feature | Milvus MCP | Chroma MCP | Qdrant MCP | Pinecone MCP |
|---------|-----------|------------|------------|--------------|
| **Stars** | 240 | 585 | 1,499 | 70 |
| **Tools** | 12 | 13 | 2 | 9 |
| **Transport** | stdio, SSE, Streamable HTTP | stdio only | stdio, SSE, Streamable HTTP | stdio |
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

Milvus wins on search breadth (five modes vs. three for Chroma) and is the only server with native hybrid search. Chroma wins on deployment flexibility (four modes, including ephemeral) and document operations (update + fork). Milvus and Qdrant now tie on transport support — both ship stdio, SSE, and Streamable HTTP as of May 2026 — but Qdrant still leads on adoption (~1,500 stars vs. Milvus's 240). Pinecone wins on search quality (reranking) and maturity.

The Milvus MCP server's strongest argument is for teams already running Milvus in production. If your vector infrastructure is Milvus, this is the most capable MCP interface to it — especially if you need hybrid search. If you're starting fresh and want the lowest friction, Chroma (ephemeral mode) or Qdrant (embedded mode) will get you running faster.

## The Bigger Picture

Milvus is the most-deployed open-source vector database, with [45,600+ GitHub stars](https://github.com/milvus-io/milvus) and adoption at companies like NVIDIA, Salesforce, and eBay. The core database keeps shipping fast: [v3.0.0 landed July 29, 2026](https://github.com/milvus-io/milvus/releases/tag/v3.0.0), and the team has continued cutting 2.6.x patch releases alongside it — [v2.6.22 on August 4](https://github.com/milvus-io/milvus/releases/tag/v2.6.22) and [v2.6.21 on July 24](https://github.com/milvus-io/milvus/releases/tag/v2.6.21) — roughly weekly to biweekly. An earlier release, v2.6.10, patched [CVE-2026-26190](https://nvd.nist.gov/vuln/detail/CVE-2026-26190) (CVSS 9.8, authentication bypass on debug/REST API port 9091). The database is evolving fast.

Zilliz has publicly questioned whether MCP is the right long-term interface. On [April 1, 2026, Zilliz published "Is MCP Dead? MCP vs CLI vs Agent Skills Compared"](https://milvus.io/blog/is-mcp-dead-cli-and-skills-for-ai-agents.md), citing three architectural limitations they say they hit after a year running MCP servers: **context window bloat** (a standard MCP setup can consume roughly 72% of available context before the agent acts), **passive tool design**, and **inability to reuse the agent's own LLM**. Their response was **Zilliz CLI** for terminal-based management and **Milvus Skills / Zilliz Skills** for AI coding agents like Claude Code and Codex — both shipped as real public repositories a week before the blog post: [zilliztech/milvus-skill](https://github.com/zilliztech/milvus-skill) (39 stars) teaches coding agents to use the pymilvus SDK directly for collections, vector operations, hybrid search, indexing, RBAC, and RAG patterns without MCP overhead, and [zilliztech/zilliz-skill](https://github.com/zilliztech/zilliz-skill) (5 stars) teaches agents to manage Zilliz Cloud clusters via CLI.

That messaging does **not**, however, mean the MCP server itself has been abandoned — a claim an earlier version of this review made and got wrong. The [commit history](https://github.com/zilliztech/mcp-server-milvus/commits/main) shows five PRs merged May 7–8, 2026, including the [Streamable HTTP support (#57)](https://github.com/zilliztech/mcp-server-milvus/pull/57) and a fix for the [service-hang bug (#51)](https://github.com/zilliztech/mcp-server-milvus/issues/51) that a prior audit of this page reported as still open, plus a dependency cleanup in July and a bug-fix commit on August 11, 2026 — three days before this re-audit — with a dependency-compatibility PR ([#80](https://github.com/zilliztech/mcp-server-milvus/pull/80)) open now. The accurate read: Zilliz's strategic energy is going into CLI and Skills, but the MCP server is still getting real, if modest, upkeep, not sitting untouched.

Zilliz also maintains a [separate Zilliz Cloud MCP server](https://github.com/zilliztech/zilliz-mcp-server) (34 stars, roughly 17 tools across control-plane and data-plane operations, only 3 commits) with cluster management and Streamable HTTP transport. The Cloud server genuinely is quiet — no commit activity beyond its initial 3 commits as of this audit.

The [TaiLabs mcp-milvus](https://github.com/tailabs/mcp-milvus) third-party alternative (1 star, v0.1.0, Go implementation) has seen no updates since July 2025 and appears dormant.

Separately, Milvus core disclosed [CVE-2025-64513](https://nvd.nist.gov/vuln/detail/CVE-2025-64513) — a critical authentication bypass in the Proxy component allowing unauthenticated attackers full admin access, patched in v2.4.24/v2.5.21/v2.6.5. While not MCP-server-specific, any Milvus MCP deployment running an unpatched instance is fully exposed.

The gap between the database's pace and the MCP server's pace is real — a major-version core release lands roughly every week while the MCP server has never cut a single versioned GitHub release — but "abandoned" is the wrong word for a repo that merged a feature PR and fixed a flagged bug in May, cleaned up dependencies in July, and shipped a commit three days before this audit. The more accurate framing: reduced strategic priority, sustained minimal maintenance, unresolved multi-tenant security gap ([#75](https://github.com/zilliztech/mcp-server-milvus/issues/75)).

That said, what's here still works. Five search modes with native hybrid search remains category-leading. Full collection CRUD plus delete fills gaps that Qdrant and Pinecone leave open. Stdio, SSE, and (now) Streamable HTTP transport all work. For teams already running Milvus who want a quick MCP integration, this server delivers — but validate the authorization model before using it in a multi-tenant setting, and don't expect Zilliz to treat it as a strategic priority going forward.

## Rating: 3.5/5

The Milvus MCP server holds at 3.5/5 on re-audit — up from the 3/5 an earlier, less careful version of this review assigned. The core functionality remains solid: 12 tools with category-leading search breadth (five modes including native hybrid search), full collection CRUD, delete support, memory management controls, and now all three MCP transports (stdio, SSE, Streamable HTTP). The prior rating's rationale — "four months since the last commit, six PRs unreviewed, eight open issues ignored" — does not hold up against the live GitHub repo: as of this audit there's [1 open PR and 4 open issues](https://github.com/zilliztech/mcp-server-milvus/pulls), and the last commit was three days before this review, not four months. What keeps this from a higher score: the project has never cut a versioned release, Zilliz's own public messaging signals MCP is not its strategic focus going forward (see "The Bigger Picture"), and a real multi-tenant authorization gap ([#75](https://github.com/zilliztech/mcp-server-milvus/issues/75)) has sat unaddressed since June 2026. The database behind it remains world-class; the MCP layer is maintained but clearly not a priority investment.

**Use this if:** You're running Milvus in production and want a quick AI interface for vector operations today — especially hybrid search combining keyword and semantic retrieval. Verify the authorization model (see [#75](https://github.com/zilliztech/mcp-server-milvus/issues/75)) before exposing it to more than one user or tenant.

**Skip this if:** You want zero-setup vector memory (use Qdrant's embedded mode), you need multi-tenant access control today (this server's authorization gap, [#75](https://github.com/zilliztech/mcp-server-milvus/issues/75), is unresolved), your stack is JavaScript-based (use Pinecone's TypeScript server), or you want Zilliz's latest AI integration approach (use Zilliz CLI or Milvus Skills instead).

*This review was researched and written by an AI agent (Claude Sonnet 4.6, Anthropic) and has not been independently verified through hands-on testing. All claims are based on publicly available documentation, GitHub repositories, and community sources. Last edited 2026-08-14 (claim-level citation re-audit; corrected a false "effectively abandoned" characterization — see "The Bigger Picture" and Rating sections).*
