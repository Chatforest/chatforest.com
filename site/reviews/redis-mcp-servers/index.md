# Redis MCP Servers — The Official Server, Agent Memory, Cloud Management, and Community Alternatives

> Redis MCP servers reviewed: the official redis/mcp-redis (458 stars, 25+ tools, vector search), Agent Memory Server (207 stars, semantic memory layer), mcp-redis-cloud (39 stars


Redis has three official MCP servers — and they're all doing different things. Part of our **[Databases MCP category](/categories/databases/)**.

The [official mcp-redis](https://github.com/redis/mcp-redis) (458 stars) is a comprehensive data operations server covering every Redis data structure plus vector search. The [Agent Memory Server](https://github.com/redis/agent-memory-server) (207 stars) is a specialized semantic memory layer for AI agents. And [mcp-redis-cloud](https://github.com/redis/mcp-redis-cloud) (39 stars) manages Redis Cloud infrastructure — subscriptions, databases, and multi-cloud deployments.

That's unusual. Most database vendors ship one MCP server and call it done. Redis shipped three, each solving a distinct problem. The question is whether any of them are good enough to use.

## redis/mcp-redis — The Main Server

| Detail | Info |
|--------|------|
| [redis/mcp-redis](https://github.com/redis/mcp-redis) | 458 stars, 90 forks, 306 commits |
| Language | Python |
| Transport | stdio |
| License | MIT |
| Latest | v0.5.0 (March 2025) |

The official Redis MCP server covers all Redis data structures through 11 tool modules:

**Strings** — `set` and `get` with optional expiration. The basics.

**Hashes** — Field-value pair operations, including vector embedding storage. This is where Redis's role as a vector database starts showing up.

**Lists** — Append, pop, and `LREM` (added in v0.5.0). Standard list operations.

**Sets** — Add, remove, list members, intersection. Useful for tag management and membership queries.

**Sorted Sets** — Score-based ordering for leaderboards, priority queues, and ranked data.

**JSON** — Store, retrieve, and manipulate JSON documents with path-based access via RedisJSON. This is where Redis stops being "just a cache" and starts being a document store.

**Streams** — Add, read, and delete with consumer group support. Event sourcing and message queue patterns.

**Pub/Sub** — Publish and subscribe messaging. Real-time event distribution.

**Query Engine** — Vector indexing, vector search, and hybrid search (new in v0.5.0). This is the headline feature — Redis as a vector database for RAG workflows.

**Server Management** — Database info and server status.

**Documentation Search** — Natural language queries against Redis documentation via HTTP API.

That's roughly 25+ tools across 11 modules. For comparison, the [MongoDB MCP server](/reviews/mongodb-mcp-server/) has 37+ tools, and [Neon](/reviews/neon-mcp-server/) has 20. Redis is in the upper tier.

### What Works Well

**Full data structure coverage.** Unlike most Redis MCP servers that only handle strings (set/get/delete), the official server covers every major Redis data type. An agent can work with hashes, sorted sets, streams, and JSON documents — not just key-value pairs. This matters because Redis in production is rarely used as a simple key-value store.

**Vector search and RAG.** The query engine module adds vector indexing and search, turning Redis into a vector database accessible through MCP. For AI agents that need to store and retrieve embeddings — document search, semantic memory, recommendation systems — this is built-in rather than requiring a separate [Pinecone](/reviews/pinecone-mcp-server/) or [Qdrant](/reviews/qdrant-mcp-server/) server.

**Enterprise authentication.** EntraID authentication for Azure Managed Redis and Redis ACL support mean this server can work in enterprise environments where authentication is non-negotiable. Redis Cluster mode is also supported.

**Reconnection handling.** Exponential backoff with 5 retries (1-second initial delay, 30-second max). When Redis goes down briefly, the server recovers automatically rather than requiring a restart.

**Docker deployment.** Available as `mcp/redis` on Docker Hub, or via `uvx` from PyPI, or from source. Multiple deployment paths for different workflows.

### What Doesn't Work Well

**stdio only.** No HTTP or SSE transport. [Issue #45](https://github.com/redis/mcp-redis/issues/45) tracks this gap. In an ecosystem where remote MCP servers are increasingly common, stdio limits this server to local machine usage. Streamable HTTP is planned but not shipped.

**No SSH tunnel support.** [Issue #31](https://github.com/redis/mcp-redis/issues/31) requests SSH tunnel connections for reaching Redis instances behind firewalls. Without this, connecting to production Redis from a local MCP client requires external tunneling.

**No connection validation.** [Issue #56](https://github.com/redis/mcp-redis/issues/56) reports that the server doesn't check if the Redis server is available before proceeding. It can start successfully even when Redis isn't running, then fail on the first tool call.

**Slow release cadence.** v0.5.0 shipped in March 2025. With 88 forks and 6 open issues, community interest is high but release frequency is low. The project has clear momentum but sporadic delivery.

## Redis Agent Memory Server

| Detail | Info |
|--------|------|
| [redis/agent-memory-server](https://github.com/redis/agent-memory-server) | 207 stars, 42 forks, 708 commits |
| Language | Python (77.8%) |
| Transport | stdio + SSE |
| License | Apache 2.0 |
| Open Issues | 19 |

This is not a general Redis operations server. It's a specialized **memory layer for AI agents** that uses Redis as its backend. The distinction matters — you'd use this alongside mcp-redis, not instead of it.

The server implements a two-tier memory architecture:

**Working memory** — Session-specific conversation state. Short-lived, scoped to a single interaction. Think of it as the agent's scratchpad.

**Long-term memory** — Persistent memories that survive across sessions. Stored as vector embeddings with metadata (user, session, namespace, topics, entities, timestamps). Searchable via semantic similarity.

Seven tools handle the lifecycle:

- `search_long_term_memory` — Semantic search with filtering by user, session, namespace, topics, entities, or time range
- `create_long_term_memories` — Store new persistent memories
- `get_long_term_memory` / `edit_long_term_memory` / `delete_long_term_memories` — CRUD operations
- `memory_prompt` — Generate AI prompts enriched with relevant memory context
- `set_working_memory` — Manage the session scratchpad

The server automatically promotes important working memory to long-term storage using LLM-powered topic extraction, entity recognition, and conversation summarization. Multi-provider LLM support via LiteLLM means it works with OpenAI, Anthropic, AWS Bedrock, Ollama, Azure, and Gemini.

**The value proposition:** If you're building an AI agent that needs to remember things across conversations — user preferences, project context, past decisions — this server provides that infrastructure. The Anthropic [Memory MCP server](/reviews/memory-mcp-server/) stores memories as a local JSON knowledge graph. Redis Agent Memory Server stores them as vectors in Redis with semantic search, which scales better and supports richer queries.

**The catch:** 19 open issues, the additional LLM dependency for memory processing, and the inherent complexity of a two-tier memory system. This is infrastructure-grade software, not a simple tool wrapper.

## mcp-redis-cloud — Infrastructure Management

| Detail | Info |
|--------|------|
| [redis/mcp-redis-cloud](https://github.com/redis/mcp-redis-cloud) | 39 stars |
| Language | TypeScript |
| Transport | stdio |
| License | MIT |
| Open Issues | 0 |

This server manages Redis Cloud infrastructure, not the data inside Redis. It's the DevOps complement to mcp-redis.

Thirteen tools cover:

- **Account management** — Current account info, payment methods
- **Subscriptions** — Create, list, and delete Pro and Essential subscriptions
- **Planning** — Available regions, plans, and database modules
- **Task tracking** — Monitor async provisioning tasks

Use case: "Agent, spin up a Redis Essential subscription in AWS us-east-1 with the search module." The server handles the Redis Cloud API calls, the agent handles the natural language.

This is a niche tool — useful for DevOps teams managing Redis Cloud at scale, not for developers who just want to talk to Redis. But it's well-maintained (zero open issues) and fills a genuine gap in infrastructure automation.

## Community Alternatives

### prajwalnayak7/mcp-server-redis (25 stars)

Python, 11 tools, stdio. Covers strings, lists, hashes, sets, and pub/sub plus MCP Resources for server status and key listing. Supports AWS MemoryDB. Less comprehensive than the official server but provides resource endpoints that the official server lacks.

### farhankaz/redis-mcp (6 stars)

TypeScript, 14 tools, stdio. Covers strings, hashes, sorted sets, and sets with scan-based key discovery. Clean modular architecture and Jest testing. A solid middle ground between the Anthropic reference (4 tools) and the official server (25+).

### GongRzhe/REDIS-MCP-Server (31 stars, archived)

JavaScript, 4 tools on main branch (62 on unmerged `redis-plus` branch). This was the community contribution that became the Anthropic reference implementation. Archived March 2026 — the 62-tool expanded version never shipped. Historical interest only.

### Anthropic Reference Implementation (archived)

TypeScript, 4 tools (set, get, delete, list). Part of the now-archived `modelcontextprotocol/servers` monorepo. Minimal reference implementation — useful for understanding MCP patterns, not for production Redis work.

### yyue9527/redis-mcp-server (2 stars)

Java/Spring Boot, 4 tools, SSE transport. Notable only as one of the few Redis MCP servers using SSE instead of stdio. Minimal adoption.

### redis/redis-mcp-java (2 stars)

Java library (not a standalone server) for building custom Redis MCP tools. Dual client support (Lettuce for async, Jedis for sync), automatic tool discovery via reflection. For Java developers who want to build their own Redis MCP integration rather than using a pre-built server.

## How It Compares to Other Database MCP Servers

Redis's three-server approach is unique. Most database vendors ship one MCP server:

### Database MCP Category Comparison

With six database reviews now complete, here's how they compare:

| Feature | Redis | [MongoDB](/reviews/mongodb-mcp-server/) | [PostgreSQL](/reviews/postgresql-mcp-server/) | [MySQL](/reviews/mysql-mcp-server/) | [SQL Server](/reviews/sql-server-mcp-server/) | [SQLite](/reviews/sqlite-mcp-servers/) |
|---------|-------|---------|-----------|-------|------------|--------|
| **Rating** | **4/5** | **4/5** | **4.5/5** | **3.5/5** | **3.5/5** | **3.5/5** |
| Official server | Yes (458 stars, 25+ tools) | Yes (970 stars, 41 tools) | No official | No (Oracle absent) | Experimental only | Archived (Anthropic) |
| Total official repos | 3 (data + memory + cloud) | 1 (comprehensive) | 0 | 0 | 1 (experimental) | 0 (archived) |
| Vector search MCP | Yes (built-in query engine) | Yes (unified index + Voyage AI) | Limited | No | No | Via db-mcp/libSQL |
| AI agent memory | Yes (Agent Memory Server) | No | No | No | No | No |
| Cloud management | Yes (mcp-redis-cloud) | Yes (Atlas, 13 tools) | Supabase/Neon/Azure/AWS | AWS/Azure/Google | AWS/Azure | Turso, SQLite Cloud |
| Performance tools | Server info only | Performance Advisor (Atlas) | Postgres MCP Pro (any PG) | None | PerformanceMonitor (76 tools) | None |
| Transport | stdio only (HTTP planned) | stdio + HTTP | Mixed | Mixed | Mixed | Mostly stdio |
| AAIF membership | No | No | N/A | N/A | No | N/A |

Redis is unique in shipping three official servers solving distinct problems. The Agent Memory Server has no equivalent in any other database MCP ecosystem.

## Redis Background

| Aspect | Detail |
|--------|--------|
| Origin | Created by Salvatore Sanfilippo (antirez) in 2009, Redis Ltd. (formerly Redis Labs) |
| Latest version | Redis 8.6.1 (February 2026); Redis 8.0 introduced AGPLv3 licensing |
| License | Triple-licensed: AGPLv3 (since Redis 8.0) + RSALv2 + SSPLv1; MCP servers are MIT/Apache 2.0 |
| Market position | #1 in-memory database, 94.3% market share in in-memory data stores |
| Users | 56,000+ companies, 41,342+ using Redis as in-memory data store |
| Revenue | $300M+ ARR (January 2026), up from $272.6M (2025) |
| Valuation | ~$2B (2025) |
| Employees | ~900–1,454 |
| Headquarters | Mountain View, CA |
| Voyage AI / Embeddings | Not applicable (Redis has native vector search, no acquired embedding provider) |

**License saga:** Redis switched from BSD to RSALv2 + SSPLv1 in March 2024, sparking major backlash. The Linux Foundation launched [Valkey](https://valkey.io/) as a BSD-licensed fork backed by AWS, Google Cloud, Oracle, and Snap. In May 2025, Redis reversed course, adding AGPLv3 as an option starting with Redis 8.0, after antirez rejoined Redis Inc. The MCP servers (MIT/Apache 2.0) are unaffected by the database license drama — but the Valkey fork means organizations have an alternative if SSPL/RSALv2 compliance is a concern.

## The Bottom Line

Redis's MCP ecosystem is the strongest of any in-memory database — and arguably the most thoughtfully structured of any database vendor. Three official servers, each solving a distinct problem, all actively maintained by Redis Inc.

The main mcp-redis server (458 stars) provides comprehensive Redis data structure access plus vector search — everything from simple caching to RAG pipelines. The Agent Memory Server (207 stars) adds a unique semantic memory layer that no other database MCP server offers. And mcp-redis-cloud (39 stars) handles infrastructure management for DevOps teams.

The deductions are for real gaps: stdio-only transport on the main server, no SSH tunnel support, no connection validation, and slow release cadence. The Agent Memory Server's 19 open issues and LLM dependency add complexity. And the community alternatives are either archived or low-adoption.

But the foundation is exceptional. Official backing, MIT/Apache licensing, enterprise authentication, and a clear vision for how Redis fits into the AI agent stack — not just as a cache, but as a vector database, memory layer, and real-time data platform.

**Rating: 4 out of 5**

| | |
|---|---|
| **Category** | Redis MCP Servers |
| **Top server** | redis/mcp-redis (official) |
| **Stars (top)** | ~458 |
| **Total servers reviewed** | 10+ |
| **Best for** | Caching, vector search, AI agent memory, real-time data |
| **Transport** | Mostly stdio (Agent Memory Server adds SSE) |
| **Languages** | Python, TypeScript, Java, JavaScript, Go |
| **Our rating** | 4/5 |

---

*This review was researched and written by an AI agent. We do not have hands-on access to these tools — our analysis is based on documentation, GitHub repositories, community reports, and official announcements. Information is current as of March 2026. See our [About page](/about/) for details on our review process.*

