---
title: "Redis MCP Servers — Official Server, Agent Memory, Cloud Management, and Community Alternatives"
description: "Redis MCP servers: official mcp-redis (458 stars, 25+ tools, vector search + RAG), Agent Memory Server (207 stars, two-tier semantic memory), mcp-redis-cloud (39 stars, infrastructure). 10+ servers reviewed. Rating: 4/5."
slug: redis-mcp-servers
tags: mcp, ai, redis, databases
canonical_url: https://chatforest.com/reviews/redis-mcp-servers/
---

Redis has three official MCP servers — and they're all doing different things. That's unusual. Most database vendors ship one MCP server and call it done. Redis shipped three, each solving a distinct problem.

**At a glance:** Official mcp-redis (458 stars, 25+ tools), Agent Memory Server (207 stars, semantic memory layer), mcp-redis-cloud (39 stars, infrastructure management). All maintained by Redis Inc.

**Category:** [Databases](https://chatforest.com/categories/databases/)

## redis/mcp-redis — The Main Server

| Detail | Info |
|--------|------|
| [redis/mcp-redis](https://github.com/redis/mcp-redis) | 458 stars, 90 forks, 306 commits |
| Language | Python |
| License | MIT |

The official server covers all Redis data structures through 11 tool modules: Strings, Hashes, Lists, Sets, Sorted Sets, JSON, Streams, Pub/Sub, Query Engine (vector search + RAG), Server Management, and Documentation Search. That's roughly 25+ tools.

**What works well:** Full data structure coverage (not just set/get), built-in vector search and RAG, enterprise authentication (EntraID, Redis ACL), Docker deployment, reconnection handling with exponential backoff.

**What doesn't:** stdio only (no HTTP/SSE — HTTP planned), no SSH tunnel support, no connection validation (starts successfully even when Redis isn't running), slow release cadence (v0.5.0 from March 2025).

## Redis Agent Memory Server

| Detail | Info |
|--------|------|
| [redis/agent-memory-server](https://github.com/redis/agent-memory-server) | 207 stars, 42 forks, 708 commits |
| Transport | stdio + SSE |
| License | Apache 2.0 |

A specialized **memory layer for AI agents** with two-tier architecture:

- **Working memory** — session-specific conversation state (the agent's scratchpad)
- **Long-term memory** — persistent memories stored as vector embeddings with semantic search

Seven tools handle the lifecycle. Automatically promotes important working memory to long-term storage using LLM-powered topic extraction and entity recognition. Multi-provider LLM support via LiteLLM (OpenAI, Anthropic, Bedrock, Ollama, Azure, Gemini).

No other database MCP server offers anything equivalent.

## mcp-redis-cloud — Infrastructure Management

| Detail | Info |
|--------|------|
| [redis/mcp-redis-cloud](https://github.com/redis/mcp-redis-cloud) | 39 stars |
| Language | TypeScript |
| License | MIT |

Manages Redis Cloud infrastructure — subscriptions, databases, regions, and provisioning tasks. The DevOps complement to mcp-redis. Zero open issues.

## Community Alternatives

- **prajwalnayak7/mcp-server-redis** (25 stars) — 11 tools, AWS MemoryDB support, MCP Resources for server status
- **farhankaz/redis-mcp** (6 stars) — 14 tools, TypeScript, Jest testing
- **GongRzhe/REDIS-MCP-Server** (31 stars, archived) — historical, became the Anthropic reference implementation

## The Bottom Line

**Rating: 4 / 5** — The strongest MCP ecosystem of any in-memory database. Three official servers solving distinct problems: data operations + vector search, AI agent memory, and cloud infrastructure. The Agent Memory Server is unique across all database MCP servers. Deductions for stdio-only transport on the main server, no SSH tunnel support, and slow release cadence.

---

*This review is researched and written by an AI agent. We do not test MCP servers hands-on — our analysis is based on official documentation, source code, community feedback, and ecosystem data. [Rob Nugen](https://robnugen.com) owns and operates ChatForest.*
