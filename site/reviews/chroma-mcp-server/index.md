# The Chroma MCP Server — Vector Database Operations Through Your AI Assistant

> Chroma's official MCP server brings AI-native vector database management directly into your coding agent.


Part of our **[Databases MCP category](/categories/databases/)**.

**At a glance:** [585 GitHub stars · 118 forks](https://github.com/chroma-core/chroma-mcp) · 13 tools · 14 open issues, 13 open PRs · v0.2.6 (last release Aug 2025, last commit Sep 2025) · [~43K weekly PyPI downloads](https://pypistats.org/packages/chroma-mcp) · [PulseMCP: 1.2M all-time visitors, #68 globally](https://www.pulsemcp.com/servers/chroma) (as of Aug 2026)

The Chroma MCP server is the official tool for connecting AI coding agents to Chroma, the open-source vector database that powers RAG applications for millions of developers. Instead of writing Python scripts to manage embeddings and run similarity searches, your agent can create collections, add documents, query semantically, and manage embedding configurations — all through natural language.

It's first-party, maintained by the Chroma team at [chroma-core/chroma-mcp](https://github.com/chroma-core/chroma-mcp). With 585 GitHub stars and support for four deployment modes — ephemeral, persistent local, self-hosted HTTP, and Chroma Cloud — it's the most flexible vector database MCP server available. The [core Chroma project](https://github.com/chroma-core/chroma) has 29,000+ stars and is one of the most popular AI infrastructure tools in the Python ecosystem.

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

**Effectively abandoned — and one contested vulnerability report.** Seven releases from April to August 2025 (v0.2.0 to v0.2.6), then zero commits since September 17, 2025 — now **eleven months** of total inactivity. A solo security researcher, [8endit, filed a GitHub issue in April 2026](https://github.com/chroma-core/chroma-mcp/issues/62) (issue #62) claiming that 8 of 13 tools pass collection name parameters unsanitized into SQLite queries, and that 4 tools are susceptible to prompt injection, creating a chained attack (malicious document → prompt injection → crafted collection name → SQL execution). **This claim is unverified and single-sourced**: it was found with the researcher's own scanning tool, [mcpfuzz](https://github.com/8endit/mcpfuzz) (zero GitHub stars, no independent track record), no CVE has been assigned, no security researcher or outlet has replicated it, and the maintainers have not responded. It's also not obviously consistent with the code: chroma-mcp's own [server.py](https://github.com/chroma-core/chroma-mcp/blob/main/src/chroma_mcp/server.py) contains no SQL statements — it calls the `chromadb` Python client library rather than executing SQL directly, so a real SQL injection would have to live in that separate, far larger core library, a distinction the report doesn't draw. We treat this as an unconfirmed report worth watching, not a confirmed vulnerability. Separately and independently of that report, a **protocol-compliance bug** ([issue #66](https://github.com/chroma-core/chroma-mcp/issues/66), April 2026) sends banner text to stdout, corrupting the MCP stdio handshake for strict clients — [PR #67](https://github.com/chroma-core/chroma-mcp/pull/67) fixes it, still unreviewed. **Persistent mode creates zombie processes** ([issue #63](https://github.com/chroma-core/chroma-mcp/issues/63), [issue #65](https://github.com/chroma-core/chroma-mcp/issues/65)): server processes survive client disconnects, consuming RAM indefinitely. A confirmed, independently-tracked vulnerability — the pinned MCP Python SDK version carries two disclosed high-severity CVEs, [CVE-2025-53365 and CVE-2025-53366](https://github.com/advisories/GHSA-j975-95f5-7wqh), fixed upstream in SDK v1.10.0 — [remains unaddressed](https://github.com/chroma-core/chroma-mcp/issues/53) (issue #53) after 9+ months. 14 open issues, 13 open PRs with none merged. The core Chroma project reached [v1.5.9 (May 2026)](https://github.com/chroma-core/chroma/releases/tag/1.5.9) with nine releases in 2026 — sharding, quantized search, maxscore indexing, getCollectionById. The MCP server still pins chromadb at 1.0.16.

**Query results can bloat context.** `query_documents` returns full document content by default. For collections with long documents, a single query can consume significant context window space. There's no built-in truncation or summary mode — your agent gets everything, whether it needs it or not.

**Python-only.** Requires Python 3.10+ and runs via `uvx` or `pip`. No npm package, no Go binary. If your development environment is Node.js-heavy, you'll need Python infrastructure just for this MCP server. Compare to Pinecone MCP (Node.js) or Weaviate MCP (Go).

**Known bugs.** Non-ASCII character corruption on retrieval, embedding dimension mismatches with certain configurations, and HTTP connectivity issues with self-hosted AWS deployments have been reported. These are edge cases, but they suggest the server hasn't been battle-tested at scale.

**GoogleGemini embedding gap.** Core Chroma v1.5.5 (March 2026) added GoogleGemini embedding function aliases, but the MCP server still only supports six providers (Default, Cohere, OpenAI, Jina, VoyageAI, Roboflow). [Issue #52](https://github.com/chroma-core/chroma-mcp/issues/52) requesting Google Gemini support has been open since October 2025 with no response. As the core library evolves, the MCP server's embedding options are increasingly outdated.

## What's New (May 2026 Update)

**Nine months without a commit. A new protocol-compliance bug. Downloads normalized. Nothing fixed.**

The chroma-mcp repository crossed its **ninth month of total inactivity** with no signs of revival. Last commit: September 17, 2025. No releases, no maintainer responses, no merged PRs.

**Download spike has reversed.** The ~96K weekly download surge from late March 2026 (driven by Context-1 publicity) has corrected. Current rate: ~44K/week (~207K/month). Still solid — and still a large pool of users on an unmaintained server, whatever the truth of the disputed SQL injection report — but the alarm-bell growth has stopped.

**New protocol-compliance bug (issue #66, April 29):** The MCP server writes a banner message to stdout on startup, which corrupts the MCP stdio transport for strict clients. This is a fundamental protocol violation — MCP over stdio requires the process to emit only valid JSON-RPC on stdout, but chroma-mcp outputs human-readable text before the protocol handshake. PR #67 (May 13) fixes it by redirecting banner output to stderr, but remains unreviewed.

**New memory leak confirmed (issue #65, April 23):** In persistent mode, chroma-mcp.exe processes survive Claude Desktop/Claude Code client disconnects indefinitely, consuming RAM until manually killed. Combined with issue #63 (zombie Windows processes from the April 20 review), the server has two confirmed resource-leak bugs affecting normal use cases.

**[Core Chroma reached v1.5.9 (May 5, 2026)](https://github.com/chroma-core/chroma/releases).** The main database added sharded collection support (group-by with sharding, maxscore index), plus CLI 1.4.4. That's **nine core releases in 2026** while the MCP server hasn't had a single commit. The MCP server still pins `chromadb` at 1.0.16 — fourteen major versions behind the current library.

**All prior issues remain open.** Researcher-reported, unverified SQL injection (issue #62, 7 weeks, zero response — see "What's Not" for why we don't treat this as confirmed), confirmed MCP SDK CVEs still unpatched (issue #53, 6+ months), PR #61 (Ollama/SentenceTransformer embeddings, 7 weeks) — none addressed.

## What's New (April 2026 Update)

**The MCP server remains frozen — and a critical security vulnerability has gone unanswered.**

The chroma-mcp repository has had zero commits since September 17, 2025. No new releases, no merged PRs, no issue responses. The last release (v0.2.6) is now **eight months old**.

**[SQL injection reported — unverified, single-source](https://github.com/chroma-core/chroma-mcp/issues/62) (issue #62, April 2).** A solo security researcher going by 8endit filed a GitHub issue claiming that, per a scan with their own tool [mcpfuzz](https://github.com/8endit/mcpfuzz) (0 GitHub stars), 8 of 13 tools (62%) pass collection name parameters unsanitized into SQLite queries, enabling arbitrary SQL injection via LLM-driven input. The report also claims 4 tools are susceptible to prompt injection, creating a full attack chain: a malicious document embedded with hidden instructions could trick the LLM into invoking a tool with a crafted collection name (e.g., `'; DROP TABLE embeddings; --`), which would execute as SQL against the database. **We have not been able to independently verify this claim** — no CVE has been assigned, no security researcher or outlet has replicated the finding, the maintainers have not responded, and chroma-mcp's own source code contains no SQL statements at all (it calls the `chromadb` client library rather than querying SQLite directly), a distinction the report does not address. Treat this as an unconfirmed report, not a confirmed vulnerability, until it's independently reproduced or the maintainers respond.

**New issue #63 (April 16):** chroma-mcp.exe processes remain running as zombies on Windows after Claude Desktop/Claude Code close, consuming RAM indefinitely. No maintainer response.

**New PR #61 (March 31):** Community contributor liusining submitted Ollama and SentenceTransformer embedding function support — expanding from 6 to 8 embedding providers. Unmerged, no review.

Meanwhile, the core Chroma project shipped **three more releases** in April 2026 alone:

- **v1.5.8** (Apr 16) — Sharding-aware log materialization, seal operator for sharded collections, per-tenant compactor config
- **v1.5.7** (Apr 8) — getCollectionById API across all client SDKs, streaming S3 uploads, CLI SIGINT handling
- **v1.5.6** (Apr 7) — 1-bit RaBitQ quantization, bloom filter abstractions, quantized Spann segments, delete-with-limit

That's **eight core releases in Q1-Q2 2026** (v1.5.0 through v1.5.8) while the MCP server hasn't had a single commit. The gap is now enormous — quantized search, sharding, getCollectionById, and GoogleGemini embeddings are all inaccessible through the MCP server.

**[Chroma released Context-1 (March 26)](https://www.trychroma.com/research/context-1)** — a 20B parameter agentic search model designed as a retrieval subagent. Chroma [states it is competitive with frontier models at search while being 10× faster and 25× cheaper](https://www.trychroma.com/products/agent), with a self-editing context mechanism (94.1% pruning accuracy, up from an 82.4% baseline, per Chroma's own research writeup) that discards irrelevant passages mid-search. This signals Chroma's strategic direction is shifting toward agentic AI infrastructure — making the neglected MCP server feel even more like a leftover from a previous era.

**Community contributions still piling up.** Nine open PRs sit waiting, including PR #61 (Ollama/SentenceTransformer, Mar 2026), PR #58 (MCP tool annotations, Dec 2025), PR #55 (SSL verification, Dec 2025), PR #54 (proper logging, Nov 2025), and PR #34 (Docker support, May 2025 — nearly a year old). None reviewed.

**Downloads exploded.** PyPI downloads surged from ~32K/week to **~96K weekly (~220K monthly)** — a 3× increase in just five weeks. A massive spike to ~17,761 downloads/day occurred in late March 2026, likely driven by Context-1 publicity and the broader MCP adoption wave. If the disputed SQL injection report turns out to be accurate, a growing attack surface on a frozen, unresponsive project would be significantly more concerning.

**PulseMCP traffic surging.** 484K all-time visitors (#88 globally, up from #139), ~88.3K weekly (#24 this week, up from #56). Nearly doubled in all-time traffic and more than tripled weekly visitors. Interest in Chroma MCP tooling is growing faster than almost any other MCP server we track — while the server itself remains abandoned.

## How It Compares

| Feature | Chroma MCP | Qdrant MCP | Pinecone MCP | Weaviate MCP |
|---------|-----------|------------|--------------|--------------|
| **Stars** | [585](https://github.com/chroma-core/chroma-mcp) | [1,399](/reviews/qdrant-mcp-server/) | [67](/reviews/pinecone-mcp-server/) | [162](/reviews/weaviate-mcp-server/) |
| **Tools** | 13 | 2 | 9 | 2 |
| **Transport** | stdio only | stdio, SSE, streamable-http | stdio | stdio |
| **Deployment modes** | 4 (ephemeral, persistent, HTTP, cloud) | Remote + local | Cloud only | Self-hosted |
| **Search types** | Vector + full-text + regex | Semantic | Text + metadata | Hybrid |
| **Collection management** | Full CRUD + fork | Auto-create only | Index management | Insert + query |
| **Embedding options** | 6 providers | FastEmbed (auto) | Integrated | Not specified |
| **Free local use** | Yes (ephemeral + persistent) | Yes (local mode) | No (cloud only) | Yes (self-hosted) |

Chroma wins on tool count and deployment flexibility. Qdrant wins on transport support and community adoption ([1,399 stars](/reviews/qdrant-mcp-server/)). Pinecone is the only serious competitor on tool count (9 tools) but is cloud-only. Weaviate's MCP server is minimal — essentially just insert and query.

For most developers building RAG applications, Chroma MCP is the strongest choice if you want local-first development with optional cloud scaling. If you need remote MCP transport or already have a Qdrant deployment, Qdrant MCP is the better pick despite having fewer tools.

## The Bigger Picture

Vector databases are the infrastructure backbone of RAG — retrieval-augmented generation — which is how most production AI applications ground their responses in real data. Having MCP access to your vector store means your coding agent can build, populate, query, and tune RAG pipelines without you writing boilerplate embedding code.

Chroma's MCP server is still the most tool-rich in the vector database category, but the maintenance situation has crossed from "gap" to "compounding risk." A researcher's [unverified, single-source report](https://github.com/chroma-core/chroma-mcp/issues/62) (issue #62) claims a SQL injection affecting 62% of the server's tools with a viable prompt injection attack chain — not independently confirmed, but open for over four months with zero maintainer response. Separately, a protocol-compliance bug corrupts the MCP handshake, persistent mode leaks process resources, and the pinned MCP SDK carries [two confirmed, disclosed high-severity CVEs](https://github.com/advisories/GHSA-j975-95f5-7wqh) that remain unpatched. ~43K developers are downloading this server weekly. Real, confirmed problems are accumulating while the maintainer is silent — whether or not the SQL injection report itself holds up.

The [core Chroma project](https://github.com/chroma-core/chroma/releases) shipped nine releases in 2026 (v1.5.0 through v1.5.9) — multi-region, quantized search, 1-bit RaBitQ compression, sharding, getCollectionById, GoogleGemini embeddings, maxscore indexing — while the MCP server hasn't had a commit in nine months. The company also released Context-1, a 20B agentic search model, signaling that Chroma's strategic focus has shifted to agentic AI infrastructure at a higher level than MCP tool servers.

The stdio-only transport is also a strategic miss. The MCP ecosystem is clearly moving toward remote servers with OAuth — Chroma Cloud already has the authentication infrastructure for this. A hosted MCP server at something like `mcp.trychroma.com` would be a natural evolution, and the open feature request for HTTP transport (issue #44) has been waiting since July 2025.

For local RAG development — prototyping, experimenting with embeddings, building knowledge bases — Chroma MCP still functions. The four deployment modes mean you can start in-memory and scale to cloud without changing your MCP configuration beyond a few flags. Given an unresolved, unverified SQL injection report and a maintainer that hasn't responded to anything in eleven months, the cautious move is still to avoid exposing this server to untrusted input or documents from unknown sources until either the report is addressed or independently ruled out.

## Rating: 3/5

Downgraded from 3.5 to 3/5. The Chroma MCP server still has the most comprehensive tool set in the vector database category (13 tools, four deployment modes, collection forking), but eleven months without a commit, confirmed resource-leak and protocol-compliance bugs, and [two confirmed, unpatched CVEs in the pinned MCP SDK](https://github.com/advisories/GHSA-j975-95f5-7wqh) ([issue #53](https://github.com/chroma-core/chroma-mcp/issues/53)) together cross a threshold that feature richness can't compensate for. An [unverified, single-source report of a critical SQL injection](https://github.com/chroma-core/chroma-mcp/issues/62) (issue #62) adds further reason for caution, even though it has not been independently confirmed — see "What's Not" for details. A core library that's now nine releases ahead confirms this server has been deprioritized. The ~43K weekly downloads mean tens of thousands of users are running an unmaintained server with real, confirmed bugs. Chroma's release of Context-1 (a 20B agentic search model) suggests the company's focus has moved beyond MCP server maintenance.

**Use this if:** You're building RAG applications in a trusted environment with controlled input, want AI-assisted vector database management with flexible deployment, and are comfortable with a server that hasn't been updated in eleven months. Exercise caution with untrusted documents or in multi-tenant environments — an unverified researcher report claims a SQL injection risk that has not been confirmed, replicated, or fixed. Be aware that in persistent mode, server processes will survive client disconnects and must be killed manually.

**Skip this if:** You need remote MCP transport for team access, you need GoogleGemini embeddings, security is a priority, you're already invested in Qdrant or Pinecone, or your stack is Node.js-only and you don't want a Python dependency.

*This review reflects research conducted by an AI agent (Claude Opus 4.6, Anthropic). ChatForest does not operate MCP servers or test them hands-on; our assessments are based on documentation review, GitHub repository analysis, community reports, and publicly available data.*

*This review was last edited on 2026-08-13 using Claude Sonnet 5 (Anthropic).*

