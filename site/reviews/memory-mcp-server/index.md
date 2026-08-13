# The Memory MCP Server — A Knowledge Graph That Needs a Better Brain

> The official Knowledge Graph Memory MCP server gives agents persistent memory across conversations.


Part of our **[Databases MCP category](/categories/databases/)**.

**At a glance:** [89,500+ GitHub stars (monorepo)](https://github.com/modelcontextprotocol/servers), [~102,000 weekly npm downloads](https://www.npmjs.com/package/@modelcontextprotocol/server-memory) (this figure swings widely week to week — npm's own API shows single-week counts ranging from ~62,000 to ~236,000 over the past several months), [v2026.7.4](https://github.com/modelcontextprotocol/servers/releases/tag/2026.7.4) (released July 4, 2026, ending a roughly five-month gap since v2026.1.26), 9 tools, maintained, ~103,000 weekly PulseMCP visitors (#26 globally, ~3.9M all-time)

The Memory MCP server ([`@modelcontextprotocol/server-memory`](https://www.npmjs.com/package/@modelcontextprotocol/server-memory)) is Anthropic's official solution for giving AI agents persistent memory across conversations. It maintains a local knowledge graph — entities, relations, and observations stored as JSONL — that agents can read and update over time. The idea is simple: your agent remembers who you are, what you're working on, and what you've told it before.

It's one of the most popular MCP servers, pulling six-figure weekly npm downloads and ranking in [PulseMCP's](https://www.pulsemcp.com/servers/modelcontextprotocol-memory) top 30 globally with millions of estimated all-time visitors. Unlike the archived SQLite and PostgreSQL reference servers, Memory is still maintained in the main `servers` repository. And the core concept works — agents that remember context are genuinely more useful than ones that start fresh every session.

But the landscape hasn't just shifted — it's leapt ahead. The LongMemEval benchmark era has arrived, and purpose-built memory systems are scoring 95-99% on standardized recall tests. Meanwhile, the Memory server has no scores on any version of that benchmark — [its first release since January 2026 shipped July 4, 2026](https://github.com/modelcontextprotocol/servers/releases/tag/2026.7.4), a five-month gap. OWASP's MCP Top 10 context over-sharing risk still applies. Alternatives like [Graphiti](https://github.com/getzep/graphiti) (~29,900 stars), [mem0](https://github.com/mem0ai/mem0) (SDK v2.0.2+, ~63,200 stars), OMEGA, agentmemory, and Supermemory have all matured dramatically. The Memory server still works for small personal use cases, but it's now being measured against systems with 25-29 MCP tools, temporal knowledge graphs, and verified benchmark scores — and it has no answer.

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

## What's New (May 2026 Update)

**Update (August 2026 re-audit):** the release drought described in the May 2026 snapshot below has since ended, and two of the pending PRs it flagged did not survive to make it into a release. Details follow.

**Four months without a release, then one arrived — but two other memory fixes never landed.** The last published npm version sat at v2026.1.26 (January 2026) for the entire May 2026 review window — four months without a published release at that point. That gap ultimately reached just over five months before [v2026.7.4 shipped on July 4, 2026](https://github.com/modelcontextprotocol/servers/releases/tag/2026.7.4). That release folded in [PR #4109 — "npm audit fix for high/medium security alerts"](https://github.com/modelcontextprotocol/servers/pull/4109) (merged May 16, 2026), so npm users are no longer running a version that predates that dependency maintenance. Two other memory-specific PRs that were open as of the original review did not make it in: [PR #4049](https://github.com/modelcontextprotocol/servers/pull/4049) (atomic file writes for `saveGraph()` + expanded tool descriptions) was closed without merging on May 30, 2026 when the contributor deleted the source branch, and [PR #4090](https://github.com/modelcontextprotocol/servers/pull/4090) (a `type`-field validation fix) was closed June 4, 2026 after the maintainer addressed the underlying issue a different way in a separate merged PR. [Issue #4117](https://github.com/modelcontextprotocol/servers/issues/4117) — a broader security-hardening audit (safer storage defaults, atomic writes, quotas, secret redaction, destructive-operation guardrails), filed May 6, 2026 — remains open and unaddressed as of this re-audit.

**npm downloads surged despite stagnation.** Weekly downloads jumped from ~44,500 to ~68,500 — a 54% increase in 30 days. This is counterintuitive: the server has received no new features and no new release, yet substantially more people are downloading it. The most likely explanation is increased AI assistant adoption generally, with the Memory server benefiting as a simple, zero-configuration starting point for agent memory. Growth at the top of the funnel, even if sophisticated users move on quickly.

**[LongMemEval-V2](https://arxiv.org/abs/2605.12493) launched May 12, 2026.** A second-generation benchmark for agent memory evaluation (Di Wu, Zixiang Ji, et al.) launched with 451 manually curated questions covering five core memory abilities, with test histories up to 500 trajectories (~115M tokens). This is a substantially harder benchmark than the original. Early scores on LME-V2 show top performers in the 69–73% range — a reset that may make some prior LME-v1 score comparisons less directly applicable. The Memory server still has no benchmark scores on either version.

**The original LongMemEval leaderboard remains unchanged.** The benchmark positions from the April review stand:
- **Supermemory** claims ~99% using ASMR (parallel LLM agents) — experimental
- **[agentmemory](https://github.com/JordanMcCann/agentmemory)** (Jordan McCann) [scored 96.2% (481/500)](https://dev.to/jordanmccann/how-i-built-a-memory-system-that-scores-962-on-longmemeval-1-in-the-world-41n), built solo in 16 days for ~$1K
- **[OMEGA](https://github.com/omega-memory/omega-memory)** [scored 95.4%](https://omegamax.co/benchmarks) — local-first, zero external dependencies, 25 MCP tools, AES-256-GCM encryption
- **Mem0 Temporal Reasoning** scored 94.8% (launched May 12)
- **Mastra Observational Memory** scored 94.87% using GPT-5-mini
- **Zep/Graphiti** scored 71.2% — "lower" scorer that still vastly outperforms string-matching retrieval
- The Memory server has no benchmark scores on any version of this test

**[OWASP MCP Top 10](https://owasp.org/www-project-mcp-top-10/) active, context over-sharing persists.** The [OWASP MCP Top 10 project](https://github.com/OWASP/www-project-mcp-top-10) received updates as recently as May 11, 2026 (references and tooling additions). The context over-sharing threat category — which the Memory server's `read_graph` tool exemplifies — remains formally documented. No mitigations have been added to the Memory server.

**Alternatives landscape updates.** Key changes since April 19:
- **[Graphiti/Zep](https://github.com/getzep/graphiti)** grew to ~26,200 GitHub stars (+1,100) as of the May 2026 review; now ~29,900 stars as of this August 2026 re-audit. v0.29.0 released April 27: major efficiency improvements, cheaper ingestion, search pipeline rework, saga abstraction
- **[mem0](https://github.com/mem0ai/mem0)** reached ~56,000 GitHub stars as of May 2026; now ~63,200 as of this re-audit. A SQL/Cypher injection vulnerability across the PGVector, Azure MySQL, and Neptune Analytics backends ([GitHub issue #4875](https://github.com/mem0ai/mem0/issues/4875), CVSS 8.1 for Neptune / 6.5 for PGVector and MySQL, CWE-89) was filed April 17, 2026. **Correction:** the original review cited a GHSA advisory ID (GHSA-5gv3-2fv6-jvhx) that does not resolve to any real advisory, and claimed the fix shipped in v2.0.2 (May 7) — it did not. The actual fix, [PR #4878](https://github.com/mem0ai/mem0/pull/4878), merged July 7, 2026, roughly two months later than originally reported. CLI v0.2.5 (May 14) adds `mem0 init --agent` for instant unclaimed API key setup
- **Letta** v0.16.8 (May 14): security fix — switched from pickle to JSON for sandbox-to-server tool result transport; v0.16.7 increased context window default from 32K to 128K tokens
- **Mastra** continues active releases (v1.33.0–v1.35.0, May 13–15) with focus on token estimation accuracy and message replay fixes
- **MemPalace** (29 MCP tools) and **agentmemory** remain competitive; no major updates found in this window

**PulseMCP traffic stabilizing.** Weekly visitors: ~71,400 (down from ~74,600 in April). All-time: ~2.7M (up from ~2.4M). Global rank: #24 (down from #20) — the Memory server's relative position is eroding as newer, specialized memory servers gain traction on PulseMCP.

## What Works Well

**The entity-relation-observation model is intuitive.** It maps naturally to how people think about memory: things (entities), how they connect (relations), and what we know about them (observations). Agents pick this up without much prompting — they naturally create entities for people, projects, and concepts they encounter, then link them together. No schema design required.

**Persistence across conversations is genuinely useful.** The killer feature is simple: your agent remembers your name, your preferences, your current projects, and what you discussed last week. This transforms the experience from "explaining everything every time" to "picking up where we left off." For personal assistant use cases, this alone justifies the server.

**The JSONL format is inspectable and portable.** Your memories are stored in a plain text file you can read, edit, grep through, or back up. No proprietary database, no cloud sync, no lock-in. If you want to see exactly what your agent has stored about you, open the file. If you want to delete something, edit the file. This transparency matters.

**Search works well for targeted retrieval.** The `search_nodes` tool matches against entity names, types, and observation text. For queries like "what do I know about ProjectX?" or "find all people entities," it returns focused results — typically 200-500 tokens instead of dumping the whole graph. This is the right way to access memory in most cases.

**Still maintained, not archived — and releases resumed in July.** Unlike the archived SQLite and Postgres MCP servers, Memory lives in the main `modelcontextprotocol/servers` repository. [v2026.7.4 (July 4, 2026)](https://github.com/modelcontextprotocol/servers/releases/tag/2026.7.4) ended a five-month release gap, but the server still shows no new tools, no architectural improvements, no response to the OWASP context over-sharing concerns, and no engagement with the LongMemEval benchmark standard that now defines the competitive landscape.

## What Doesn't Work Well

**`read_graph` is a context bomb — and now an OWASP-recognized risk.** This tool dumps your entire knowledge graph into the conversation context. For a small personal graph (50-100 entities), that's manageable — maybe 2,000-3,000 tokens. But knowledge graphs grow fast. Users with months of accumulated memory report 14,000+ token dumps from a single `read_graph` call. That's a significant chunk of your context window consumed by memory retrieval, leaving less room for the actual conversation. The recommended workaround — starting each chat with "Remembering..." to trigger a full graph load — makes this worse by front-loading the context cost. As of March 2026, the [OWASP MCP Top 10](https://owasp.org/www-project-mcp-top-10/) formally identifies "context over-sharing" as a security risk category. The `read_graph` pattern — dumping unscoped, persistent context into shared sessions — is exactly what OWASP warns about.

**No memory isolation between projects or contexts.** All entities live in one flat graph. If you use the same Memory server for work projects and personal notes, your agent sees everything mixed together. Community benchmarks found that the system "couldn't separate the contexts of two projects," confusing memories when similar projects existed. It works for single-context use; it falls apart when you need boundaries.

**No deduplication or conflict resolution.** Create the same entity twice? You get two entities. Add contradictory observations ("Prefers tabs" and "Prefers spaces")? Both persist. The server doesn't merge, deduplicate, or flag conflicts — that burden falls entirely on the agent, which may or may not handle it well depending on the model and prompt.

**JSONL doesn't scale.** Every read operation loads the entire file. Every write operation rewrites it. With hundreds of entities, this is fine. With thousands, you'll notice latency. There's no indexing, no partial reads, no pagination. The storage format that makes the server simple also makes it slow at scale.

**No semantic search.** `search_nodes` does string matching — it finds "Python" in observations but won't connect "snake_case" to Python conventions. For a knowledge graph, the lack of embedding-based or semantic retrieval is a significant gap. You can only find what you can match textually.

**No access controls or encryption.** The JSONL file is plaintext on disk. Anyone with file access can read everything your agent has memorized about you. For a personal tool on your own machine, this is probably fine. For any shared or team environment, it's a non-starter.

## Compared to Alternatives

**vs. [Zep/Graphiti](https://github.com/getzep/graphiti) (~29,900 GitHub stars, MCP Server 1.0):** Zep has repositioned as a "context engineering platform" built on Graphiti, a temporal knowledge graph engine where time is a first-class dimension. [50% month-over-month ARR growth and 240+ customers including Fortune 500](https://www.ycombinator.com/companies/zep-ai/jobs) (Zep's own YC jobs-page claim, as of the May 2026 review — unverified beyond Zep's own statement). v0.29.0 (April 27) delivered major efficiency improvements, cheaper ingestion, and a reworked search pipeline. Scores [71.2% on LongMemEval](https://blog.getzep.com/state-of-the-art-agent-memory/) — far below the frontier but still dramatically better than what string-matching retrieval can achieve. The clear winner for anything beyond personal use. See our [Zep/Graphiti review](/reviews/zep-graphiti-mcp-server/).

**vs. [mem0](https://github.com/mem0ai/mem0) (~63,200 GitHub stars, SDK v2.0.2+):** SDK v2.0.0 launched April 16 with single-pass extraction (~50% latency reduction), hybrid retrieval (semantic + BM25 + entity-graph boosting), and entity linking replacing graph memory — Neo4j no longer required. Graph features still paywalled at $249/month (Pro tier). OpenMemory (self-hosted local option) was sunset, with users directed to the Mem0 self-hosted server. A SQL/Cypher injection vulnerability ([issue #4875](https://github.com/mem0ai/mem0/issues/4875), CVSS 8.1) was fixed via [PR #4878](https://github.com/mem0ai/mem0/pull/4878), merged July 7, 2026 — corrected from this review's earlier claim of a May 7 fix under a GHSA ID that does not exist. Temporal Reasoning now scores 94.8% on LongMemEval. See our [mem0 review](/reviews/mem0-mcp-server/).

**vs. [OMEGA](https://github.com/omega-memory/omega-memory) (95.4% LongMemEval):** Local-first, zero external dependencies (no API keys, no cloud, no Docker, no Neo4j). Uses SQLite + ONNX for local embeddings with AES-256-GCM encryption at rest. 25 core memory tools. The strongest argument for "simple doesn't mean limited" — OMEGA is as easy to set up as the Memory server but dramatically more capable. (Note: OMEGA's own [benchmarks page](https://omegamax.co/benchmarks) lists a lower, approximate "12 tools" figure dated Feb 2026 in a comparison table; the GitHub repo's more current count is used here.)

**vs. [agentmemory](https://github.com/JordanMcCann/agentmemory) (96.2% LongMemEval):** Built solo in 16 days for ~$1K by a single developer. A complete memory operating system with retrieval engine, knowledge graph, consolidation pipeline, and evaluation harness. Demonstrates that the Memory server's simplicity isn't a design virtue — it's just missing features.

**vs. Letta (formerly MemGPT):** A full agent runtime where agents actively manage their own memory using an OS-inspired tiered architecture — core memory, archival memory, and recall memory. v0.16.8 (May 14) added a security fix switching from pickle to JSON for tool result transport; v0.16.7 increased the default context window from 32K to 128K tokens. A community-built (not official) [high-performance Rust-based MCP server](https://github.com/oculairmedia/Letta-MCP-server) provides 7 consolidated tools covering 103 operations with 68-96% response size reduction. A fundamentally different approach: instead of a memory *tool*, Letta is a memory *platform*. Overkill for personal assistant memory; worth considering for agentic workflows.

**vs. [Hindsight](https://github.com/vectorize-io/hindsight) (91.4% LongMemEval):** Offers all four retrieval strategies — vector, graph, temporal, and keyword — at every tier, including the free self-hosted option. Provides more retrieval depth than mem0 Pro without the price jump, plus Python, TypeScript, and Go SDKs with MCP-first integration. Worth evaluating if you want graph + temporal memory without Zep's infrastructure requirements.

**vs. [Chroma MCP Server](https://github.com/chroma-core/chroma-mcp):** Vector database-backed retrieval with full-text search, metadata filtering, and multiple embedding functions (Cohere, OpenAI, Jina, Voyage). Different paradigm — more document retrieval than knowledge graph. Better for finding relevant context from a large corpus; less structured than entity-relation approaches.

**vs. [Basic Memory](https://github.com/basicmachines-co/basic-memory):** Focuses on note-taking and document memory rather than entity-relation graphs. Stores memories as Markdown files, which integrate naturally with tools like Obsidian. If your "memory" is more like notes than a graph of entities, Basic Memory may fit better.

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
The Memory MCP server still solves a real problem — agents that remember are dramatically more useful than agents that don't. The entity-relation-observation model is intuitive, the JSONL storage is transparent and portable, and setup takes 30 seconds. Weekly npm downloads run in six figures (though the figure is noisy week to week), suggesting it remains many developers' first stop for agent memory — and for good reason. For personal use with a small knowledge graph in a single context, it works and it's not archived.

The multi-month release drought is over: [v2026.7.4 shipped July 4, 2026](https://github.com/modelcontextprotocol/servers/releases/tag/2026.7.4), five months after v2026.1.26, and it carried in the May 16 security-dependency fix from PR #4109. But the underlying competitive gap hasn't closed. The LongMemEval-V2 benchmark launched in May 2026 raises the bar further, and the Memory server has no scores on any version, original or V2. OMEGA scores 95.4% on original LongMemEval with zero external dependencies. agentmemory hit 96.2% built by a solo developer in 16 days. One resumed release doesn't answer a competitive field that now includes a second-generation benchmark.

If you're starting a new project, start with OMEGA (for local-first simplicity with real benchmarks), Zep/Graphiti (for temporal graphs), Hindsight (for multi-strategy retrieval), or Letta (for agent-managed memory). The official server proved the concept; the ecosystem has built the production-ready implementations — and the benchmarks to prove it.
{{< /verdict >}}

---

**Sources:** [modelcontextprotocol/servers (GitHub)](https://github.com/modelcontextprotocol/servers) · [@modelcontextprotocol/server-memory (npm)](https://www.npmjs.com/package/@modelcontextprotocol/server-memory) · [Release 2026.7.4](https://github.com/modelcontextprotocol/servers/releases/tag/2026.7.4) · [PR #4109 — npm audit fix](https://github.com/modelcontextprotocol/servers/pull/4109) · [Issue #4117 — memory security hardening](https://github.com/modelcontextprotocol/servers/issues/4117) · [LongMemEval-V2 (arXiv 2605.12493)](https://arxiv.org/abs/2605.12493) · [OWASP MCP Top 10](https://owasp.org/www-project-mcp-top-10/) · [mem0 issue #4875 — SQL/Cypher injection](https://github.com/mem0ai/mem0/issues/4875) · [mem0 PR #4878 — injection fix](https://github.com/mem0ai/mem0/pull/4878) · [getzep/graphiti (GitHub)](https://github.com/getzep/graphiti) · [mem0ai/mem0 (GitHub)](https://github.com/mem0ai/mem0)

*ChatForest does not test MCP servers hands-on. This review is based on documentation analysis, source code review, GitHub issue tracking, npm download data, PulseMCP analytics, community benchmarks, OWASP MCP Top 10 security framework analysis, and comparative research across the agent memory ecosystem. We have no affiliation with Anthropic, Zep, mem0, Letta, or any memory server vendor.*

*This review was last updated on 2026-08-14 (citation and fact re-audit; original review 2026-05-19) using Claude Sonnet 5 (Anthropic).*

