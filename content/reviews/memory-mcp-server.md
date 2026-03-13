---
title: "The Memory MCP Server — A Knowledge Graph That Needs a Better Brain"
date: 2026-03-14
description: "The official Knowledge Graph Memory MCP server gives agents persistent memory across conversations. Nine tools, JSONL storage, and a simple entity-relation model — but scalability and context issues hold it back. Here's the honest review."
og_description: "The official Memory MCP server gives agents persistent memory via a knowledge graph. Simple and useful for small-scale memory, but scaling problems and context bloat limit it. Rating: 3.5/5."
content_type: "Review"
card_description: "Anthropic's knowledge graph memory server for persistent agent context. Simple, useful for small-scale memory, but read_graph dumps your entire context and there's no memory isolation."
---

The Memory MCP server (`@modelcontextprotocol/server-memory`) is Anthropic's official solution for giving AI agents persistent memory across conversations. It maintains a local knowledge graph — entities, relations, and observations stored as JSONL — that agents can read and update over time. The idea is simple: your agent remembers who you are, what you're working on, and what you've told it before.

It's one of the most popular MCP servers, pulling ~45,000 weekly npm downloads. Unlike the archived SQLite and PostgreSQL reference servers, Memory is still actively maintained in the main `servers` repository. And the core concept works — agents that remember context are genuinely more useful than ones that start fresh every session.

But there are real problems once you move past small-scale personal use.

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

## What Works Well

**The entity-relation-observation model is intuitive.** It maps naturally to how people think about memory: things (entities), how they connect (relations), and what we know about them (observations). Agents pick this up without much prompting — they naturally create entities for people, projects, and concepts they encounter, then link them together. No schema design required.

**Persistence across conversations is genuinely useful.** The killer feature is simple: your agent remembers your name, your preferences, your current projects, and what you discussed last week. This transforms the experience from "explaining everything every time" to "picking up where we left off." For personal assistant use cases, this alone justifies the server.

**The JSONL format is inspectable and portable.** Your memories are stored in a plain text file you can read, edit, grep through, or back up. No proprietary database, no cloud sync, no lock-in. If you want to see exactly what your agent has stored about you, open the file. If you want to delete something, edit the file. This transparency matters.

**Search works well for targeted retrieval.** The `search_nodes` tool matches against entity names, types, and observation text. For queries like "what do I know about ProjectX?" or "find all people entities," it returns focused results — typically 200-500 tokens instead of dumping the whole graph. This is the right way to access memory in most cases.

**Actively maintained.** Unlike the archived SQLite and Postgres MCP servers, Memory lives in the main `modelcontextprotocol/servers` repository with ongoing updates. Version 2026.1.26 is current, and the package sees regular maintenance.

## What Doesn't Work Well

**`read_graph` is a context bomb.** This tool dumps your entire knowledge graph into the conversation context. For a small personal graph (50-100 entities), that's manageable — maybe 2,000-3,000 tokens. But knowledge graphs grow fast. Users with months of accumulated memory report 14,000+ token dumps from a single `read_graph` call. That's a significant chunk of your context window consumed by memory retrieval, leaving less room for the actual conversation. The recommended workaround — starting each chat with "Remembering..." to trigger a full graph load — makes this worse by front-loading the context cost.

**No memory isolation between projects or contexts.** All entities live in one flat graph. If you use the same Memory server for work projects and personal notes, your agent sees everything mixed together. Community benchmarks found that the system "couldn't separate the contexts of two projects," confusing memories when similar projects existed. It works for single-context use; it falls apart when you need boundaries.

**No deduplication or conflict resolution.** Create the same entity twice? You get two entities. Add contradictory observations ("Prefers tabs" and "Prefers spaces")? Both persist. The server doesn't merge, deduplicate, or flag conflicts — that burden falls entirely on the agent, which may or may not handle it well depending on the model and prompt.

**JSONL doesn't scale.** Every read operation loads the entire file. Every write operation rewrites it. With hundreds of entities, this is fine. With thousands, you'll notice latency. There's no indexing, no partial reads, no pagination. The storage format that makes the server simple also makes it slow at scale.

**No semantic search.** `search_nodes` does string matching — it finds "Python" in observations but won't connect "snake_case" to Python conventions. For a knowledge graph, the lack of embedding-based or semantic retrieval is a significant gap. You can only find what you can match textually.

**No access controls or encryption.** The JSONL file is plaintext on disk. Anyone with file access can read everything your agent has memorized about you. For a personal tool on your own machine, this is probably fine. For any shared or team environment, it's a non-starter.

## Compared to Alternatives

**vs. Zep Knowledge Graph MCP:** Zep offers persistent, local knowledge graph memory with temporal awareness — it tracks when things were learned and can reason about time ("what was I working on last month?"). More sophisticated graph processing, still local-first. The better choice if you need time-aware memory or more advanced retrieval. Free and open-source.

**vs. mem0 (MemZero):** A managed memory layer that provides semantic search over memories using vector embeddings. Finds contextually relevant memories even when the words don't match. Cloud-hosted (with a self-hosted option via Qdrant + Neo4j + Ollama). Better retrieval quality, but adds cloud dependency and complexity.

**vs. Chroma MCP Server (512 GitHub stars):** Vector database-backed retrieval. If your primary need is finding relevant context from a large corpus of memories, Chroma's embedding-based search will outperform Memory's string matching significantly. Different paradigm — more document retrieval than knowledge graph.

**vs. Basic Memory:** Focuses on note-taking and document memory rather than entity-relation graphs. Stores memories as Markdown files, which integrate naturally with tools like Obsidian. If your "memory" is more like notes than a graph of entities, Basic Memory may fit better.

**vs. Our [SQLite MCP Server review](/reviews/sqlite-mcp-server/):** Both are official Anthropic reference implementations. Memory is actively maintained (SQLite is archived). Memory is more specialized (knowledge graph vs. general database). But both share the same limitation: simple design that works for demos and personal use but doesn't scale to production needs.

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

{{< verdict rating="3.5" summary="The right idea, not yet the right tool for serious use" >}}
The Memory MCP server solves a real problem — agents that remember are dramatically more useful than agents that don't. The entity-relation-observation model is intuitive, the JSONL storage is transparent and portable, and setup takes 30 seconds. For personal use with a small knowledge graph in a single context, it works well and it's actively maintained. But the scaling problems are real: `read_graph` dumps your entire context, there's no memory isolation between projects, no deduplication, no semantic search, and the JSONL storage becomes a bottleneck as your graph grows. The Memory server is a good starting point for personal agent memory, and the right choice if simplicity matters more than sophistication. But if you're building anything beyond a personal assistant, look at Zep (for temporal knowledge graphs), mem0 (for semantic retrieval), or Chroma (for embedding-based search). The official server proves the concept; the community has built the production-ready implementations.
{{< /verdict >}}
