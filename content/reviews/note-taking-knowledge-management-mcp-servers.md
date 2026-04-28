---
title: "Note-Taking & Knowledge Management MCP Servers — Your Second Brain Meets AI Agents"
date: 2026-03-16T18:00:00+09:00
description: "Note-taking and knowledge management MCP servers connect AI agents to your personal knowledge bases. We reviewed 50+ servers across 11 subcategories including the new Bear Notes official MCP."
og_description: "Note-Taking & Knowledge Management MCP servers: 50+ servers across Obsidian (3,500 stars), Notion (4,300 stars, v2.0.0), Bear Notes (official MCP April 2026), Apple Notes, Evernote, Joplin, Roam, Logseq, Tana, Capacities, and knowledge graph memory systems (Graphiti 20k stars). Rating: 4.5/5."
content_type: "Review"
card_description: "Note-taking and knowledge management MCP servers across Obsidian, Notion, Bear Notes, Apple Notes, Evernote, Joplin, Roam Research, Logseq, Tana, Capacities, and knowledge graph memory systems. The category spans 50+ servers and covers every major PKM platform. BIGGEST UPDATE: Bear 2.8 ships official CLI + MCP server + Claude connector (April 2026), filling the largest gap we identified. Notion hit v2.0.0 with data sources abstraction and 22 tools (4,300 stars). Obsidian's top server reached 3,500 stars. Knowledge graph servers exploded — Graphiti/Zep crossed 20,000 stars, mcp-memory-service and Supermemory each hit 1,700 stars. The agent memory category is now larger than platform-specific servers combined. Rating: 4.5/5."
last_refreshed: 2026-04-28
---

Note-taking and knowledge management tools are where people store their most valuable thinking — research notes, project plans, meeting records, personal wikis, and the connective tissue between ideas. Connecting AI agents to these systems is one of the most natural MCP use cases: instead of copy-pasting context into prompts, an agent can search, read, and update your notes directly. Part of our **[Business & Productivity MCP category](/categories/business-productivity/)**.

The ecosystem has responded accordingly. Over 50 MCP servers now cover every major note-taking platform, from mainstream tools like Obsidian and Notion to niche PKM systems like Tana and Capacities. The landscape splits into two broad camps: **platform-specific servers** that connect to a particular app, and **knowledge graph servers** that provide platform-agnostic persistent memory for AI agents.

**April 2026 update — three major shifts since our initial review:**

1. **Bear Notes filled the biggest gap.** Bear 2.8 beta (April 22, 2026) ships an official CLI (`bearcli`), MCP server, and one-click Claude connector — making Bear the newest platform with official MCP support. We called this gap out in March; it's now closed.
2. **Notion shipped v2.0.0** with a breaking migration to "data sources" as the primary abstraction, 22 tools (up from 20), and is prioritizing its remote MCP at mcp.notion.com over the local server.
3. **Knowledge graph servers exploded.** Graphiti (by Zep) crossed 20,000 stars with temporal knowledge graphs. Two new entrants — mcp-memory-service (1,700 stars) and Supermemory MCP (1,700 stars) — emerged as serious alternatives. The agent memory category now rivals platform-specific servers in combined star count.

The headline findings: **Obsidian has the most community servers** (8+) but no official one — three different architectural approaches compete (see [our dedicated Obsidian MCP review](/reviews/obsidian-mcp-servers/)). **Notion has the strongest official integration** with 22 tools and a v2.0.0 rewrite (see [our dedicated Notion review](/reviews/notion-mcp-server/)). **Bear Notes now has official MCP support** via Bear 2.8's built-in CLI and Claude connector. **Apple Notes gets surprisingly good MCP support** through RAG-powered semantic search. **Evernote and Joplin** both have functional MCP servers despite declining market share. **Roam Research, Logseq, and Tana** each have dedicated servers that respect their unique data models. **Knowledge graph memory servers** have evolved far beyond Anthropic's official implementation — Graphiti/Zep (20,000+ stars) leads with temporal context graphs, while mcp-memory-service and Supermemory MCP each crossed 1,700 stars.

## Platform-Specific Servers

### Obsidian (8 servers)

Obsidian dominates the note-taking MCP space with eight community servers — more than any other platform. No official Obsidian MCP server exists, and Obsidian has made no public statements about MCP support. The community fills the gap through three architectural approaches: direct file access (reading vault Markdown files), REST API integration (via Obsidian's Local REST API plugin), and native plugin architecture (running inside Obsidian itself).

The most-starred server (mcp-obsidian by MarkusPfundstein, 3,000→3,500 stars, +17%) remains the default choice despite no updates since November 2024. The fastest-growing alternative is obsidian-mcp by StevenStavrakis (694 stars, 12 tools including vault management and tag operations) which has emerged as a strong contender. The cyanheads/obsidian-mcp-server (474 stars, v2.0.7, 8 tools) provides the most polished REST API integration. The recently renamed @bitbonsai/mcpvault (v0.11.2, April 2026) added soft-delete, AST-aware YAML preservation, and a list_all_tags tool — the most actively developed option with 5 releases in March-April 2026 alone. Obsidian requested the package rename, suggesting the company is engaged with the MCP ecosystem even without shipping an official server. For the full breakdown of all servers, architectures, and recommendations, see [our dedicated Obsidian MCP servers review](/reviews/obsidian-mcp-servers/).

### Notion (Official Server — v2.0.0, 4,300 stars)

Notion's official MCP server shipped a **major v2.0.0 release** with breaking changes. The migration introduces "data sources" as the primary abstraction for databases — replacing `database_id` with `data_source_id` across all database operations. The update added 7 new tools (including `query-data-source`, `move-page`, and `list-data-source-templates`) while removing 3 legacy database tools, bringing the total to 22 tools. The server now uses Notion API version 2025-09-03 and adds Client ID Metadata Document (CIMD) support per the MCP spec 2025-11-25 for OAuth.

Notably, **Notion is prioritizing its remote MCP at mcp.notion.com** and may sunset the local server — signaling a shift toward hosted MCP infrastructure. Comment update/delete endpoints are now GA, and database filters expanded with multi-value select and status support.

For our full analysis of the Notion MCP server, see [our dedicated Notion review](/reviews/notion-mcp-server/).

### Bear Notes (Official + Community — GAP FILLED)

**The biggest gap from our March review is now closed.** Bear 2.8 beta (announced April 22, 2026) ships with an official command-line utility (`bearcli`), MCP server, and one-click Claude connector — all built into the macOS app. The official implementation supports reading, searching, creating, and editing notes using the same search engine as Bear's in-app search field. Encrypted notes can be listed but not read or edited. Setup is as simple as Help → Advanced → Install Claude Connector for Claude Desktop users, or connecting the MCP server for Claude Code and other MCP clients.

The community was already ahead of the announcement. [bear-notes-mcp](https://github.com/vasylenko/bear-notes-mcp) by vasylenko (187 stars, v2.12.0, MIT) provides 12 MCP tools for searching, reading, creating, and updating Bear Notes — available as both a Claude Desktop extension and standalone npm package. It reads Bear's SQLite database for fast search with OCR support and uses Bear's native API for writes. Fully local with no external network connections.

Bear's entry into the official MCP space is significant: it's the first note-taking app to ship a CLI, MCP server, and Claude connector as a bundled package. The tight integration (same search engine, native API writes) sets a new bar for what "official MCP support" looks like.

### Apple Notes (2+ servers)

Apple Notes has no official MCP support, but community servers provide surprisingly capable access:

| Server | Approach | Key Feature |
|--------|----------|-------------|
| [mcp-apple-notes](https://github.com/RafalWilinski/mcp-apple-notes) (Rafal) | SQLite + embeddings | RAG over Apple Notes using MiniLM-L6-v2 on-device embeddings for semantic search |
| [apple-notes-mcp](https://github.com/sirmews/apple-notes-mcp) (Sirmews) | SQLite direct | Reads Apple Notes' nested SQLite database directly from macOS filesystem |

The RAG approach from RafalWilinski is particularly interesting — it indexes your notes locally using on-device embeddings, meaning an AI agent can find semantically related notes, not just keyword matches. The trade-off is macOS-only (Apple Notes stores its database in a platform-specific location) and read-only access. No Apple Notes MCP server supports creating or editing notes — Apple's sandboxing makes write access extremely difficult without going through AppleScript.

### Evernote (3+ servers)

Despite Evernote's declining market position, three MCP servers keep it connected to the AI agent ecosystem:

| Server | Language | Key Feature |
|--------|----------|-------------|
| [evernote-mcp-server](https://github.com/brentmid/evernote-mcp-server) (Brent) | TypeScript | Claude Desktop integration, natural language note queries |
| [mcp-evernote](https://github.com/verygoodplugins/mcp-evernote) (VeryGoodPlugins) | TypeScript | Full CRUD + sync, auto Markdown↔ENML conversion |
| [evernote_mcp](https://github.com/SqREL/evernote_mcp) (SqREL) | Python | Full CRUD for notes and notebooks, standardized MCP interface |

The VeryGoodPlugins implementation added automatic Markdown-to-ENML conversion — Markdown input gets rendered to ENML-safe HTML inside `<en-note>`, removing a significant pain point. SqREL's newer Python implementation provides a clean MCP interface for creating, reading, updating, and managing notes and notebooks. Evernote's API remains finicky with rate limits and authentication quirks — expect some friction during setup.

### Joplin (2+ servers)

[joplin-mcp](https://github.com/alondmnt/joplin-mcp) connects to the open-source Joplin note-taking app via its Python API (joppy). It's a FastMCP-based server with 19+ tools covering notes, notebooks, tags, and links — including full CRUD operations, task filtering, and trash management. The server now supports both STDIO and HTTP transports (including modern and legacy SSE endpoints), and can be installed via Joplin's plugin marketplace (`/plugin marketplace add alondmnt/joplin-mcp`). A second implementation by [dweigend](https://github.com/dweigend/joplin-mcp-server) offers a TypeScript alternative. Joplin's local-first, Markdown-based architecture remains one of the cleanest MCP integration stories in the PKM space.

### Roam Research (1 server)

[roam-research-mcp](https://github.com/2b3pro/roam-research-mcp) provides AI interaction with Roam Research graphs through a standardized MCP interface. It enables comprehensive API access for reading and querying Roam's unique graph-structured data. Roam's bidirectional linking and block-level referencing create a rich data model that AI agents can leverage for finding connections between ideas. The server supports advanced data retrieval patterns that map well to Roam's query syntax.

### Logseq (1 server)

[mcp-pkm-logseq](https://github.com/ruliana/mcp-pkm-logseq) facilitates interaction with Logseq's Personal Knowledge Management system through customizable instructions. Logseq's outliner-first, block-based architecture differs significantly from page-based tools like Obsidian or Notion — this server respects that structure. Like Obsidian, Logseq stores data as local Markdown files, so the MCP server can access vault contents directly.

### Tana (2 servers)

Tana has embraced AI integration more aggressively than most PKM tools, and its MCP presence reflects this:

| Server | Key Feature |
|--------|-------------|
| [tana-mcp](https://github.com/tim-mcdonnell/tana) | Desktop API bridge — reads structured outlines, voice notes, and connected knowledge |
| [tana-codemode](https://github.com/fabiogaliano/tana-codemode) | Code mode integration for programmatic access to Tana workspaces |

Tana's Desktop app exposes a local API that the MCP server bridges, allowing AI tools to operate on structured outlines and connected knowledge rather than flat text. Recent updates added an `open_node` tool for navigating to specific nodes in the Tana UI from external applications, plus `set_field_option` and `set_field_content` tools with append mode and multiple value support. Tana has leaned heavily into MCP as "the biggest shift in how AI tools talk to each other" — this is one of the few cases where the note-taking platform actively designed for AI interoperability.

### Capacities (1 server)

[capacities-mcp](https://github.com/jemgold/capacities) acts as a bridge between AI agents and the Capacities knowledge base platform. It provides access to spaces, content search with advanced filters, web link saving with metadata, and daily notes. Capacities' object-oriented data model (where notes are typed objects with properties) gives the MCP server richer semantics than flat-text alternatives.

## Knowledge Graph & Memory Servers

Beyond platform-specific servers, a growing category of MCP servers provides platform-agnostic persistent memory for AI agents. These don't connect to an existing note-taking app — they *are* the knowledge store, built specifically for AI agent memory.

### Official Memory Server

Anthropic's official Memory MCP server (`@modelcontextprotocol/server-memory`) provides a JSONL-backed knowledge graph with entities, relations, and observations. It's the simplest option but has scaling limitations — `read_graph` dumps your entire graph into context, and there's no memory isolation between projects. For our full analysis, see [our dedicated Memory MCP server review](/reviews/memory-mcp-server/).

### Advanced Knowledge Graph Servers

The knowledge graph category has **exploded** since our March review. What was a niche category is now one of the most actively developed areas in the entire MCP ecosystem, with the top project crossing 20,000 stars.

| Server | Stars | Backend | Key Feature |
|--------|-------|---------|-------------|
| [Graphiti](https://github.com/getzep/graphiti) (by Zep) | 20,000+ | Neo4j | Temporal context graphs, tracks how facts change over time, prescribed + learned ontology |
| [mcp-memory-service](https://github.com/doobidoo/mcp-memory-service) | 1,700 | SQLite + ONNX | REST API + knowledge graph + autonomous consolidation, 13+ platform support, Apache 2.0 |
| [supermemory-mcp](https://github.com/supermemoryai/supermemory-mcp) | 1,700 | Cloud/self-hosted | Universal memory across all LLMs, no login required, free |
| [memento-mcp](https://github.com/gannonh/memento-mcp) | 415 | Neo4j | Semantic retrieval + temporal awareness, vector search, embedding diagnostics |
| [mcp-engram-memory](https://github.com/wyckit/mcp-engram-memory) | — | SQLite | 52 MCP tools, hybrid BM25 + vector, expert routing, lifecycle management |
| [engram](https://github.com/199-biotechnologies/engram) | — | SQLite-vec | Graph intelligence engine, FTS5 + vector + RRF fusion, project scoping |
| [knowledgegraph-mcp](https://github.com/n-r-w/knowledgegraph-mcp) | 20 | PostgreSQL/SQLite | Multi-project separation, fuzzy search (author now recommends dynamic context approaches) |
| [mcp-knowledge-graph](https://github.com/shaneholloman/mcp-knowledge-graph) | — | Local files | Local-first, master database, persistent memory files |

**Graphiti (by Zep)** is the clear leader at 20,000+ stars — unlike static knowledge graphs, Graphiti's context graphs track how facts change over time, maintain provenance to source data, and support both prescribed and learned ontology. The MCP server gives Claude, Cursor, and other MCP clients persistent temporal knowledge graphs that work across sessions. This is purpose-built for agents operating on evolving, real-world data.

**mcp-memory-service** emerged as a serious open-source alternative (1,700 stars, Apache 2.0) with hybrid BM25 + vector search, knowledge graph with typed edges (causes, fixes, contradicts), local ONNX embeddings, a web dashboard, and support for 13+ platforms including LangGraph, CrewAI, AutoGen, and Claude Desktop. It includes autonomous consolidation and D3.js visualization of memory relationships.

**Supermemory MCP** (1,700 stars) takes the opposite approach — universal memory that makes your memories available to every LLM, no login required, completely free. It bridges the gap between ChatGPT memories and other AI tools.

**Memento MCP** (415 stars) remains architecturally ambitious with Neo4j-backed semantic retrieval, now enhanced with embedding diagnostics that auto-generate missing embeddings and fall back to text search if vector search fails.

**Engram** has forked into two projects: the original 199-biotechnologies version (now a graph intelligence engine with SQLite-vec, FTS5 + vector + RRF fusion) and wyckit/mcp-engram-memory (52 MCP tools with expert routing and lifecycle management).

## What's Missing

~~**No Bear Notes MCP server.**~~ **RESOLVED (April 2026).** Bear 2.8 ships official CLI + MCP server + Claude connector. The community server by vasylenko (187 stars, 12 tools) also provides full coverage. This was the biggest gap in our March review — now closed.

**No Anytype MCP server.** Anytype's local-first, peer-to-peer architecture would benefit from MCP integration, but the protocol's complexity may deter community builders.

**No Dendron or Foam MCP servers.** Dendron is in maintenance-only mode (development ceased February 2023), and Foam's VS Code extension architecture doesn't lend itself to MCP integration.

**No standardized PKM interchange.** Each server speaks its platform's native language. There's no MCP server that provides a unified interface across multiple note-taking apps — you can't search Obsidian and Notion simultaneously through one MCP tool. Supermemory MCP's "universal memory" approach partially addresses this, but it creates its own memory layer rather than searching across existing apps.

**Write access improving but uneven.** Apple Notes still can't be written to via MCP. But Bear's official server supports full CRUD, Notion v2.0.0 expanded write capabilities, and the VeryGoodPlugins Evernote server added Markdown-to-ENML auto-conversion. The gap is narrowing.

**No real-time sync or collaboration.** All servers operate in request-response mode. You can't subscribe to note changes, get notified when a collaborator edits a shared document, or have an agent watch for updates. Notion's shift toward remote MCP at mcp.notion.com could eventually enable server-push patterns, but nothing exists yet.

## The Bigger Picture

The note-taking MCP space reveals a clear hierarchy of integration quality:

1. **Best:** Platforms with official MCP servers (Notion, Bear, Tana) — these have the deepest tool coverage and are most likely to stay maintained. Bear's entry in April 2026 raised the bar with its bundled CLI + MCP + Claude connector approach.
2. **Good:** Platforms with active community servers (Obsidian, Roam, Logseq) — these work well but depend on volunteer maintenance. Obsidian's community ecosystem (3,500+ stars for the top server alone) partially compensates for the lack of official support.
3. **Functional:** Legacy platforms with basic MCP support (Evernote, Joplin) — Joplin's plugin marketplace integration and HTTP transport support show these can still evolve.
4. **Dominant:** Knowledge graph servers purpose-built for AI (Graphiti/Zep, mcp-memory-service, Supermemory) — with 20,000+ stars for the leading project, this category has graduated from "emerging" to the largest and most active segment of the note-taking MCP ecosystem.

The most significant trend since March is the knowledge graph category's explosive growth. Graphiti's 20,000+ stars and temporal context graphs represent a fundamentally different vision of AI memory — one where agents don't just store facts but track how facts change over time. The emergence of mcp-memory-service and Supermemory MCP (each 1,700 stars) as viable alternatives shows the market is large enough for multiple approaches: local-first with ONNX embeddings, universal cross-LLM memory, and enterprise temporal graphs.

{{< verdict rating="4.5" summary="Bear fills biggest gap, knowledge graphs explode past 20k stars" >}}
The note-taking and knowledge management MCP ecosystem has matured significantly since our March review. Bear 2.8's official MCP support closed the largest platform gap we identified. Notion's v2.0.0 rewrite with data sources abstraction shows the leading official server evolving rapidly. Obsidian's community continues to thrive despite no official server (3,500+ stars, 8+ implementations). But the real story is knowledge graph servers: Graphiti/Zep crossing 20,000 stars, mcp-memory-service and Supermemory each hitting 1,700 stars — the agent memory category now rivals platform-specific servers in combined stargazer count. Every major PKM platform has MCP coverage, write access is improving (Bear full CRUD, Notion expanded writes, Evernote auto-conversion), and the knowledge graph options have moved from "interesting experiment" to "production-grade infrastructure." The remaining gaps — Anytype, standardized PKM interchange, real-time sync — feel smaller against what's now available.
{{< /verdict >}}

*This review was refreshed on 2026-04-28 using Claude Opus 4.6 (Anthropic). Originally published 2026-03-16.*
