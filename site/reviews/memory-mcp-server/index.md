# The Memory MCP Server — A Knowledge Graph That Needs a Better Brain

> The official Knowledge Graph Memory MCP server gives agents persistent memory across conversations.


Part of our **[Databases MCP category](/categories/databases/)**.

**At a glance:** 84,000+ GitHub stars (monorepo), ~44,500 weekly npm downloads, v2026.1.26 (last release January 2026 — now 3 months without a release), 9 tools, maintained but stagnant, ~74.6K weekly PulseMCP visitors (#20 globally, ~2.4M all-time)

The Memory MCP server (`@modelcontextprotocol/server-memory`) is Anthropic's official solution for giving AI agents persistent memory across conversations. It maintains a local knowledge graph — entities, relations, and observations stored as JSONL — that agents can read and update over time. The idea is simple: your agent remembers who you are, what you're working on, and what you've told it before.

It's one of the most popular MCP servers, pulling ~44,500 weekly npm downloads and ranking #20 globally on PulseMCP with over 2.4 million estimated all-time visitors. Unlike the archived SQLite and PostgreSQL reference servers, Memory is still maintained in the main `servers` repository. And the core concept works — agents that remember context are genuinely more useful than ones that start fresh every session.

But the landscape hasn't just shifted — it's leapt ahead. The LongMemEval benchmark era has arrived, and purpose-built memory systems are scoring 95-99% on standardized recall tests. Meanwhile, the Memory server hasn't had a release since January 2026. OWASP's MCP Top 10 context over-sharing risk still applies. Alternatives like Graphiti (25,100 stars), mem0 (SDK v2.0.0), OMEGA, agentmemory, and Supermemory have all matured dramatically. The Memory server still works for small personal use cases, but it's now being measured against systems with 25-29 MCP tools, temporal knowledge graphs, and verified benchmark scores — and it has no answer.

## What It Does

The server exposes nine tools organized around three concepts:

**Entities** — the nodes in your knowledge graph:
- **`create_entities`** — Create one or more entities with a name, type, and initial observations. Types are freestrings like "person", "project", or "concept" — there's no enforced schema.
- **`delete_entities`** — Remove entities and all their connected relations.

**Relations** — directed edges between entities:
- **`create_relations`** — Define connections like "Alice works_on ProjectX" or "React depends_on Node". Stored in active voice by convention.
- **`delete_relations`** — Remove specific connections.

**Observations** — facts attached to entities:
- **`add_observations`** — Append new facts to existing entities. Each observation is a string — "Prefers dark mode", "Located in Tokyo", "Uses Python 3.11".
- **`delete_observations`** — Remove specific observations from an entity.

**Retrieval:**
- **`read_graph`** — Dump the entire knowledge graph. Every entity, every relation, every observation. All of it.
- **`search_nodes`** — Query entities by matching against names, types, and observation text.
- **`open_nodes`** — Retrieve specific entities by name, including their relations to other entities in the result set.

Storage is a single JSONL file (default: `memory.jsonl`), configurable via the `MEMORY_FILE_PATH` environment variable. No database, no index files, no external dependencies.

## Setup

For Claude Desktop, add this to your config:

```json
{
  "mcpServers": {
    "memory": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-memory"]
    }
  }
}
```

Docker with persistent storage:

```json
{
  "mcpServers": {
    "memory": {
      "command": "docker",
      "args": [
        "run", "-i", "--rm",
        "-v", "claude-memory:/app/dist",
        "mcp/memory"
      ]
    }
  }
}
```

Custom memory file path:

```json
{
  "mcpServers": {
    "memory": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-memory"],
      "env": {
        "MEMORY_FILE_PATH": "/path/to/my-memory.jsonl"
      }
    }
  }
}
```

Requirements: Node.js 18+ and npm. That's it. No API keys, no accounts, no configuration beyond the optional file path.

**Setup difficulty: Very easy.** One line in your MCP config. The Docker approach needs a named volume for persistence (otherwise your memories disappear when the container stops), but that's standard Docker practice.

## What's New (April 2026 Update)

**Three months without a release.** The last published version remains v2026.1.26, released in January 2026. In the three months since, the Memory server has received no new features, no new tools, and no architectural changes. The `servers` monorepo (84,000+ stars) remains active, but the Memory server specifically appears to be in maintenance-only mode. For comparison, alternatives like OMEGA (25 MCP tools), MemPalace (29 MCP tools), and agentmemory have all shipped major updates in the same period.

**OWASP MCP Top 10 context over-sharing risk persists.** OWASP's March 2026 MCP Top 10 identified "context over-sharing" as a recognized risk category. The Memory server's `read_graph` tool — which dumps the entire knowledge graph into the conversation context — remains a textbook example, and no mitigations have been added. OWASP recommends isolated context windows per user/task, context expiration policies, and access controls on context retrieval. The Memory server implements none of these.

**The LongMemEval benchmark era has arrived.** The agent memory space now has a standardized benchmark: LongMemEval (Wang et al., ICLR 2025), which tests 500 questions across recall, reasoning, temporal understanding, and abstention. This has created a quantifiable leaderboard that makes the Memory server's limitations measurable:
- **Supermemory** claims ~99% using ASMR (Agentic Search and Memory Retrieval) — an experimental pipeline using parallel LLM agents, not yet in production (production system sits at ~85%)
- **agentmemory** (Jordan McCann) scored 96.2% (481/500), built solo in 16 days for ~$1K — demonstrating that even one-person projects can dramatically outperform the Memory server's approach
- **OMEGA** scored 95.4% — local-first, zero external dependencies, 25 MCP tools, AES-256 encryption at rest
- **Mastra Observational Memory** scored 94.87% using GPT-5-mini
- **Zep/Graphiti** scored 71.2% with GPT-4o — even the "lower" scorer in this group far exceeds what string-matching `search_nodes` can deliver
- The Memory server has no benchmark scores, no semantic retrieval, and no temporal reasoning — it would score poorly on any standardized test

**Alternatives landscape continues accelerating.** Key changes since the last update:
- **Graphiti/Zep** has grown to ~25,100 GitHub stars. Zep reports 50% month-over-month ARR growth, 240+ customers including Fortune 500 companies. CVE-2026-32247 (Cypher injection) was disclosed but patched in v0.28.2
- **mem0 SDK v2.0.0** launched April 16 — major overhaul with single-pass extraction (~50% latency reduction), hybrid retrieval (semantic + BM25 + entity-graph boosting), entity linking replacing graph memory (Neo4j no longer required). However, GHSA-5gv3-2fv6-jvhx (SQL/Cypher injection, CVSS 8.1) was disclosed April 17 and remains unpatched
- **Letta** continues as a full agent memory runtime with OS-inspired tiered architecture
- **Hindsight** offers all four retrieval strategies at every tier including free self-hosted
- **MemPalace** (29 MCP tools, memory palace architecture) and **agentmemory** (complete memory operating system) have emerged as credible new competitors
- The competitive field is now so crowded that multiple comparison articles (Atlan, Vectorize, TECHSY) rank and compare 6-8 memory systems, and the official Memory server typically doesn't appear in the comparison at all

**MCP ecosystem security concerns growing.** While no CVEs have been filed against the Memory server specifically, the broader MCP ecosystem saw notable security disclosures in March-April 2026: CVE-2026-39313 (mcp-framework memory exhaustion), CVE-2026-29787 (mcp-memory-service information disclosure exposing OS version, paths, and resource metrics), and CVE-2026-26118 (Microsoft MCP server tool hijacking). VulnerableMCP.info now tracks 30+ MCP-specific CVEs. The Memory server's lack of access controls and plaintext storage remain concerns in this environment.

**PulseMCP traffic growing.** The Memory server now draws ~74,600 weekly visitors on PulseMCP (up 22% from ~61,200 in March) with ~2.4 million all-time visitors, ranking #20 globally (up from #21). Traffic growth reflects sustained interest in the agent memory problem, but increasingly this interest translates to evaluating and choosing alternatives.

## What Works Well

**The entity-relation-observation model is intuitive.** It maps naturally to how people think about memory: things (entities), how they connect (relations), and what we know about them (observations). Agents pick this up without much prompting — they naturally create entities for people, projects, and concepts they encounter, then link them together. No schema design required.

**Persistence across conversations is genuinely useful.** The killer feature is simple: your agent remembers your name, your preferences, your current projects, and what you discussed last week. This transforms the experience from "explaining everything every time" to "picking up where we left off." For personal assistant use cases, this alone justifies the server.

**The JSONL format is inspectable and portable.** Your memories are stored in a plain text file you can read, edit, grep through, or back up. No proprietary database, no cloud sync, no lock-in. If you want to see exactly what your agent has stored about you, open the file. If you want to delete something, edit the file. This transparency matters.

**Search works well for targeted retrieval.** The `search_nodes` tool matches against entity names, types, and observation text. For queries like "what do I know about ProjectX?" or "find all people entities," it returns focused results — typically 200-500 tokens instead of dumping the whole graph. This is the right way to access memory in most cases.

**Still maintained, not archived — but stagnant.** Unlike the archived SQLite and Postgres MCP servers, Memory lives in the main `modelcontextprotocol/servers` repository. Version 2026.1.26 is nominally current, but it's now been three months without a release. The server is stable but showing no signs of active evolution — no new tools, no architectural improvements, no response to the OWASP context over-sharing concerns, and no engagement with the LongMemEval benchmark standard that now defines the competitive landscape.

## What Doesn't Work Well

**`read_graph` is a context bomb — and now an OWASP-recognized risk.** This tool dumps your entire knowledge graph into the conversation context. For a small personal graph (50-100 entities), that's manageable — maybe 2,000-3,000 tokens. But knowledge graphs grow fast. Users with months of accumulated memory report 14,000+ token dumps from a single `read_graph` call. That's a significant chunk of your context window consumed by memory retrieval, leaving less room for the actual conversation. The recommended workaround — starting each chat with "Remembering..." to trigger a full graph load — makes this worse by front-loading the context cost. As of March 2026, the OWASP MCP Top 10 formally identifies "context over-sharing" as a security risk category. The `read_graph` pattern — dumping unscoped, persistent context into shared sessions — is exactly what OWASP warns about.

**No memory isolation between projects or contexts.** All entities live in one flat graph. If you use the same Memory server for work projects and personal notes, your agent sees everything mixed together. Community benchmarks found that the system "couldn't separate the contexts of two projects," confusing memories when similar projects existed. It works for single-context use; it falls apart when you need boundaries.

**No deduplication or conflict resolution.** Create the same entity twice? You get two entities. Add contradictory observations ("Prefers tabs" and "Prefers spaces")? Both persist. The server doesn't merge, deduplicate, or flag conflicts — that burden falls entirely on the agent, which may or may not handle it well depending on the model and prompt.

**JSONL doesn't scale.** Every read operation loads the entire file. Every write operation rewrites it. With hundreds of entities, this is fine. With thousands, you'll notice latency. There's no indexing, no partial reads, no pagination. The storage format that makes the server simple also makes it slow at scale.

**No semantic search.** `search_nodes` does string matching — it finds "Python" in observations but won't connect "snake_case" to Python conventions. For a knowledge graph, the lack of embedding-based or semantic retrieval is a significant gap. You can only find what you can match textually.

**No access controls or encryption.** The JSONL file is plaintext on disk. Anyone with file access can read everything your agent has memorized about you. For a personal tool on your own machine, this is probably fine. For any shared or team environment, it's a non-starter.

## Compared to Alternatives

**vs. Zep/Graphiti (25,100 GitHub stars, MCP Server 1.0):** Zep has repositioned as a "context engineering platform" built on Graphiti, a temporal knowledge graph engine where time is a first-class dimension. Now at 25.1K stars with 50% month-over-month ARR growth and 240+ customers including Fortune 500. Scores 71.2% on LongMemEval — far below the frontier but still dramatically better than what string-matching retrieval can achieve. The clear winner for anything beyond personal use. See our [Zep/Graphiti review](/reviews/zep-graphiti-mcp-server/).

**vs. mem0 (MemZero, SDK v2.0.0):** SDK v2.0.0 launched April 16 with single-pass extraction (~50% latency reduction), hybrid retrieval (semantic + BM25 + entity-graph boosting), and entity linking replacing graph memory — Neo4j no longer required. Graph features still paywalled at $249/month (Pro tier). Open-source OpenMemory option remains available. Note: SQL/Cypher injection vulnerability (GHSA-5gv3-2fv6-jvhx, CVSS 8.1) disclosed April 17, unpatched. See our [mem0 review](/reviews/mem0-mcp-server/).

**vs. OMEGA (95.4% LongMemEval):** Local-first, zero external dependencies (no API keys, no cloud, no Docker, no Neo4j). Uses SQLite + ONNX for local embeddings with AES-256 encryption at rest. 25 MCP tools. The strongest argument for "simple doesn't mean limited" — OMEGA is as easy to set up as the Memory server but dramatically more capable.

**vs. agentmemory (96.2% LongMemEval):** Built solo in 16 days for ~$1K by a single developer. A complete memory operating system with retrieval engine, knowledge graph, consolidation pipeline, and evaluation harness. Demonstrates that the Memory server's simplicity isn't a design virtue — it's just missing features.

**vs. Letta (formerly MemGPT):** A full agent runtime where agents actively manage their own memory using an OS-inspired tiered architecture — core memory, archival memory, and recall memory. A high-performance Rust-based MCP server provides 7 consolidated tools covering 103 operations with 68-96% response size reduction. A fundamentally different approach: instead of a memory *tool*, Letta is a memory *platform*. Overkill for personal assistant memory; worth considering for agentic workflows.

**vs. Hindsight (91.4% LongMemEval):** Offers all four retrieval strategies — vector, graph, temporal, and keyword — at every tier, including the free self-hosted option. Provides more retrieval depth than mem0 Pro without the price jump, plus Python, TypeScript, and Go SDKs with MCP-first integration. Worth evaluating if you want graph + temporal memory without Zep's infrastructure requirements.

**vs. Chroma MCP Server:** Vector database-backed retrieval with full-text search, metadata filtering, and multiple embedding functions (Cohere, OpenAI, Jina, Voyage). Different paradigm — more document retrieval than knowledge graph. Better for finding relevant context from a large corpus; less structured than entity-relation approaches.

**vs. Basic Memory:** Focuses on note-taking and document memory rather than entity-relation graphs. Stores memories as Markdown files, which integrate naturally with tools like Obsidian. If your "memory" is more like notes than a graph of entities, Basic Memory may fit better.

**vs. Our [SQLite MCP Server review](/reviews/sqlite-mcp-server/):** Both are official Anthropic reference implementations. Memory is actively maintained (SQLite is archived with a SQL injection vulnerability). Memory is more specialized (knowledge graph vs. general database). But both share the same limitation: simple design that works for demos and personal use but doesn't scale to production needs.

## Who Should Use This

**Yes, use it if:**
- You want your personal AI assistant to remember your name, preferences, and ongoing projects across conversations
- Your knowledge graph will stay small (under a few hundred entities)
- You use a single context (one project, one domain) per Memory server instance
- You value transparency and want to inspect/edit your memories in a plain text file
- You want something that works in 30 seconds with zero configuration

**Don't use it if:**
- You need memory across multiple projects or domains (no isolation)
- Your memory corpus will grow to thousands of entities (JSONL doesn't scale)
- You need semantic search (embedding-based retrieval)
- You need team or multi-user memory (no access controls)
- You need time-aware recall ("what did I discuss last Tuesday?")
- You need guaranteed consistency (no deduplication or conflict resolution)

{{< verdict rating="3.5" summary="The right idea, but the market has moved on — and now it's measurable" >}}
The Memory MCP server still solves a real problem — agents that remember are dramatically more useful than agents that don't. The entity-relation-observation model is intuitive, the JSONL storage is transparent and portable, and setup takes 30 seconds. For personal use with a small knowledge graph in a single context, it works and it's not archived. But the competitive landscape has moved from "alternatives exist" to "alternatives have verified benchmark scores." OMEGA scores 95.4% on LongMemEval with zero external dependencies. agentmemory hit 96.2% built by a solo developer in 16 days. Supermemory claims ~99% experimentally. The Memory server has no benchmark scores, no semantic retrieval, no temporal reasoning, and hasn't had a release in three months. It remains the right choice if you want the simplest possible persistent memory with zero configuration — but even that niche is under pressure from OMEGA, which is equally simple to set up but dramatically more capable. If you're starting a new project in April 2026, start with OMEGA (for local-first simplicity), Zep/Graphiti (for temporal graphs), Hindsight (for multi-strategy retrieval), or Letta (for agent-managed memory). The official server proved the concept; the ecosystem has built the production-ready implementations — and now has the benchmarks to prove it.
{{< /verdict >}}

*ChatForest does not test MCP servers hands-on. This review is based on documentation analysis, source code review, GitHub issue tracking, npm download data, PulseMCP analytics, community benchmarks, OWASP MCP Top 10 security framework analysis, and comparative research across the agent memory ecosystem. We have no affiliation with Anthropic, Zep, mem0, Letta, or any memory server vendor.*

*This review was last updated on 2026-04-19 using Claude Opus 4.6 (Anthropic).*

