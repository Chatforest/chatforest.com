---
title: "Note-Taking & Knowledge Management MCP Servers — Your Second Brain Meets AI Agents"
date: 2026-03-16T18:00:00+09:00
sources_audited: 2026-08-16
description: "Note-taking and knowledge management MCP servers connect AI agents to your personal knowledge bases. We reviewed 50+ servers across 11 subcategories including the new Bear Notes official MCP."
og_description: "Note-Taking & Knowledge Management MCP servers: 50+ servers across Obsidian (4,300 stars), Notion (4,600 stars, v2.0.0), Bear Notes (official MCP, shipped April 2026), Apple Notes, Evernote, Joplin, Roam, Logseq, Tana, Capacities, and knowledge graph memory systems (Graphiti 30k stars). Rating: 4.5/5."
content_type: "Review"
card_description: "Note-taking and knowledge management MCP servers across Obsidian, Notion, Bear Notes, Apple Notes, Evernote, Joplin, Roam Research, Logseq, Tana, Capacities, and knowledge graph memory systems. The category spans 50+ servers and covers every major PKM platform. BIGGEST UPDATE: Bear 2.8 shipped official CLI + MCP server + Claude connector (April 2026) and is now the shipping GA release, filling the largest gap we identified. Notion hit v2.0.0 with data sources abstraction and 22 tools (4,600 stars). Obsidian's top server reached 4,300 stars. Knowledge graph servers exploded — Graphiti/Zep crossed 30,000 stars and mcp-memory-service crossed 1,900 stars, while Supermemory's original free MCP server was deprecated in favor of a newer OAuth-gated hosted version. Rating: 4.5/5."
last_refreshed: 2026-08-16
---

Note-taking and knowledge management tools are where people store their most valuable thinking — research notes, project plans, meeting records, personal wikis, and the connective tissue between ideas. Connecting AI agents to these systems is one of the most natural MCP use cases: instead of copy-pasting context into prompts, an agent can search, read, and update your notes directly. Part of our **[Business & Productivity MCP category](/categories/business-productivity/)**.

The ecosystem has responded accordingly. Over 50 MCP servers now cover every major note-taking platform, from mainstream tools like Obsidian and Notion to niche PKM systems like Tana and Capacities. The landscape splits into two broad camps: **platform-specific servers** that connect to a particular app, and **knowledge graph servers** that provide platform-agnostic persistent memory for AI agents.

**April 2026 update — three major shifts since our initial review:**

1. **Bear Notes filled the biggest gap.** Bear 2.8 beta (April 22, 2026) ships an official CLI (`bearcli`), MCP server, and one-click Claude connector — making Bear the newest platform with official MCP support. We called this gap out in March; it's now closed.
2. **Notion shipped v2.0.0** with a breaking migration to "data sources" as the primary abstraction, 22 tools (up from 20), and is prioritizing its remote MCP at mcp.notion.com over the local server.
3. **Knowledge graph servers exploded.** Graphiti (by Zep) crossed 20,000 stars in April and has since passed 30,000. Two new entrants — mcp-memory-service (1,700 stars in April, now 1,900+) and Supermemory MCP (1,700 stars in April) — emerged as serious alternatives; Supermemory's free v1 server has since been deprecated in favor of an OAuth-gated hosted version (see the Knowledge Graph section below). The agent memory category now rivals platform-specific servers in combined star count.

The headline findings: **Obsidian has the most community servers** (8+) but no official one — three different architectural approaches compete (see [our dedicated Obsidian MCP review](/reviews/obsidian-mcp-servers/)). **Notion has the strongest official integration** with 22 tools and a v2.0.0 rewrite (see [our dedicated Notion review](/reviews/notion-mcp-server/)). **Bear Notes now has official MCP support** via Bear 2.8's built-in CLI and Claude connector. **Apple Notes gets surprisingly good MCP support** through RAG-powered semantic search. **Evernote and Joplin** both have functional MCP servers despite declining market share. **Roam Research, Logseq, and Tana** each have dedicated servers that respect their unique data models. **Knowledge graph memory servers** have evolved far beyond Anthropic's official implementation — Graphiti/Zep (30,000+ stars) leads with temporal context graphs, while mcp-memory-service has crossed 1,900 stars (Supermemory MCP's original free v1 server, also cited here in April, has since been deprecated — see below).

## Platform-Specific Servers

### Obsidian (8 servers)

Obsidian dominates the note-taking MCP space with eight community servers — more than any other platform. No official Obsidian MCP server exists, and Obsidian has made no public statements about MCP support. The community fills the gap through three architectural approaches: direct file access (reading vault Markdown files), REST API integration (via Obsidian's Local REST API plugin), and native plugin architecture (running inside Obsidian itself).

The most-starred server ([mcp-obsidian](https://github.com/MarkusPfundstein/mcp-obsidian) by MarkusPfundstein, 3,000→4,300+ stars) remains the default choice. **Correction (2026-08-16 audit):** this section previously said the server had "no updates since November 2024" — that was wrong even at the time of the April 2026 refresh; the repo's [commit history](https://github.com/MarkusPfundstein/mcp-obsidian/commits/main) shows active development throughout 2025 and into 2026, with the most recent commit May 15, 2026. The fastest-growing alternative is [obsidian-mcp](https://github.com/StevenStavrakis/obsidian-mcp) by StevenStavrakis (722 stars, 12 tools including vault management and tag operations) which has emerged as a strong contender. [cyanheads/obsidian-mcp-server](https://github.com/cyanheads/obsidian-mcp-server) provides the most polished REST API integration. **Correction (2026-08-16 audit):** previously listed as "474 stars, v2.0.7, 8 tools" — it has since grown to 660 stars, shipped v3.2.12 (released August 2025), and now exposes 14 tools. The recently renamed [@bitbonsai/mcpvault](https://github.com/bitbonsai/mcpvault) added soft-delete, AST-aware YAML preservation, and a list_all_tags tool — the most actively developed option, now at v0.15.0 (published August 9, 2026; previously listed here as v0.11.2/April 2026). [Obsidian requested the package rename](https://github.com/bitbonsai/mcpvault/blob/main/CHANGELOG.md) (v0.9.0, March 2026 changelog entry: "Package renamed to `@bitbonsai/mcpvault` on npm at Obsidian's request"), suggesting the company is engaged with the MCP ecosystem even without shipping an official server. For the full breakdown of all servers, architectures, and recommendations, see [our dedicated Obsidian MCP servers review](/reviews/obsidian-mcp-servers/).

### Notion (Official Server — v2.0.0, 4,600 stars)

Notion's official MCP server shipped a **major v2.0.0 release** with breaking changes. The migration introduces "data sources" as the primary abstraction for databases — replacing `database_id` with `data_source_id` across all database operations. The update added 7 new tools (including `query-data-source`, `move-page`, and `list-data-source-templates`) while removing 3 legacy database tools, bringing the total to 22 tools. The server now uses Notion API version 2025-09-03 and adds Client ID Metadata Document (CIMD) support per the MCP spec 2025-11-25 for OAuth.

Notably, **Notion is prioritizing its remote MCP at mcp.notion.com** and may sunset the local server — signaling a shift toward hosted MCP infrastructure. Comment update/delete endpoints are now GA, and database filters expanded with multi-value select and status support.

For our full analysis of the Notion MCP server, see [our dedicated Notion review](/reviews/notion-mcp-server/).

### Bear Notes (Official + Community — GAP FILLED)

**The biggest gap from our March review is now closed.** [Bear 2.8 was first announced as a TestFlight beta on April 22, 2026](https://community.bear.app/t/bear-2-8-beta-official-cli-claude-connector-and-mcp-server/19040) and [shipped as a full macOS release on April 29, 2026](https://blog.bear.app/2026/04/bear-2-8-bearcli-claude-connector-and-mcp-server/). **Correction (2026-08-16 audit):** this section previously called it "Bear 2.8 beta" — as of this audit it is no longer in beta; the official release note reads "Update Bear now on macOS to try it out." It ships an official command-line utility (`bearcli`), MCP server, and one-click Claude connector — all built into the macOS app. The official implementation supports reading, searching, creating, and editing notes using the same search engine as Bear's in-app search field. Encrypted notes can be listed but not read or edited. Setup is as simple as Help → Advanced → Install Claude Connector for Claude Desktop users, or connecting the MCP server for Claude Code and other MCP clients.

The community was already ahead of the announcement. [bear-notes-mcp](https://github.com/vasylenko/bear-notes-mcp) by vasylenko (206 stars, v3.0.1, MIT) provides 12 MCP tools for searching, reading, creating, and updating Bear Notes — available as both a Claude Desktop extension and standalone npm package. It reads Bear's SQLite database for fast search with OCR support and uses Bear's native API for writes. Fully local with no external network connections. It remains positioned as an unofficial, opinionated alternative to Bear's native MCP rather than something superseded by it.

Bear's entry into the official MCP space is significant: it's the first note-taking app to ship a CLI, MCP server, and Claude connector as a bundled package. The tight integration (same search engine, native API writes) sets a new bar for what "official MCP support" looks like.

### Apple Notes (2+ servers)

Apple Notes has no official MCP support, but community servers provide surprisingly capable access:

| Server | Approach | Key Feature |
|--------|----------|-------------|
| [mcp-apple-notes](https://github.com/RafalWilinski/mcp-apple-notes) (Rafal) | SQLite + embeddings | RAG over Apple Notes using MiniLM-L6-v2 on-device embeddings for semantic search |
| [apple-notes-mcp](https://github.com/sirmews/apple-notes-mcp) (Sirmews) — **archived** | SQLite direct | Reads Apple Notes' nested SQLite database directly from macOS filesystem |

The RAG approach from RafalWilinski is particularly interesting — it indexes your notes locally using on-device embeddings, meaning an AI agent can find semantically related notes, not just keyword matches. The trade-off is macOS-only (Apple Notes stores its database in a platform-specific location) and read-only access. No Apple Notes MCP server supports creating or editing notes — Apple's sandboxing makes write access extremely difficult without going through AppleScript. **Correction (2026-08-16 audit):** sirmews/apple-notes-mcp is now archived on GitHub (read-only, no further updates); RafalWilinski/mcp-apple-notes remains unarchived but has had no commits since December 2024, so both entries in this category are effectively dormant.

### Evernote (3+ servers)

Despite Evernote's declining market position, three MCP servers keep it connected to the AI agent ecosystem:

| Server | Language | Key Feature |
|--------|----------|-------------|
| [evernote-mcp-server](https://github.com/brentmid/evernote-mcp-server) (Brent) | TypeScript | Claude Desktop integration, natural language note queries |
| [mcp-evernote](https://github.com/verygoodplugins/mcp-evernote) (VeryGoodPlugins) | TypeScript | Full CRUD + sync, auto Markdown↔ENML conversion |
| [evernote_mcp](https://github.com/SqREL/evernote_mcp) (SqREL) | Python | Full CRUD for notes and notebooks, standardized MCP interface |

The VeryGoodPlugins implementation added automatic Markdown-to-ENML conversion — Markdown input gets rendered to ENML-safe HTML inside `<en-note>`, removing a significant pain point. SqREL's newer Python implementation provides a clean MCP interface for creating, reading, updating, and managing notes and notebooks. Evernote's API remains finicky with rate limits and authentication quirks — expect some friction during setup.

### Joplin (2+ servers)

[joplin-mcp](https://github.com/alondmnt/joplin-mcp) connects to the open-source Joplin note-taking app via its Python API (joppy). It's a FastMCP-based server with 26 tools covering notes, notebooks, tags, and links — including full CRUD operations, task filtering, and trash management. **Correction (2026-08-16 audit):** two things here were wrong. First, the tool count has grown from the "19+" previously listed to 26 (per the current README: "This MCP server provides 26 optimized tools for comprehensive Joplin integration"). Second, this section previously said the server "can be installed via Joplin's plugin marketplace (`/plugin marketplace add alondmnt/joplin-mcp`)" — that command actually installs an orchestration plugin into **Claude Code's** plugin marketplace, not Joplin's own in-app plugin marketplace; the two are unrelated systems and the claim conflated them. The server does support both STDIO and HTTP transports, including SSE. A second implementation by [dweigend](https://github.com/dweigend/joplin-mcp-server) offers a TypeScript alternative. Joplin's local-first, Markdown-based architecture remains one of the cleanest MCP integration stories in the PKM space.

### Roam Research (1 server)

[roam-research-mcp](https://github.com/2b3pro/roam-research-mcp) provides AI interaction with Roam Research graphs through a standardized MCP interface. It enables comprehensive API access for reading and querying Roam's unique graph-structured data. Roam's bidirectional linking and block-level referencing create a rich data model that AI agents can leverage for finding connections between ideas. The server supports advanced data retrieval patterns that map well to Roam's query syntax.

### Logseq (1 server)

[mcp-pkm-logseq](https://github.com/ruliana/mcp-pkm-logseq) facilitates interaction with Logseq's Personal Knowledge Management system through customizable instructions. Logseq's outliner-first, block-based architecture differs significantly from page-based tools like Obsidian or Notion — this server respects that structure. Like Obsidian, Logseq stores data as local Markdown files, so the MCP server can access vault contents directly.

### Tana (2 servers)

Tana has embraced AI integration more aggressively than most PKM tools, and its MCP presence reflects this:

| Server | Key Feature |
|--------|-------------|
| [tana-mcp](https://github.com/tim-mcdonnell/tana-mcp) | Desktop API bridge — reads structured outlines, voice notes, and connected knowledge |
| [tana-mcp-codemode](https://github.com/fabiogaliano/tana-mcp-codemode) | Code mode integration for programmatic access to Tana workspaces |

Tana's Desktop app exposes a local API that the MCP server bridges, allowing AI tools to operate on structured outlines and connected knowledge rather than flat text. Recent updates added an `open_node` tool for navigating to specific nodes in the Tana UI from external applications, plus `set_field_option` and `set_field_content` tools with append mode and multiple value support. Tana has leaned heavily into MCP as "the biggest shift in how AI tools talk to each other" — this is one of the few cases where the note-taking platform actively designed for AI interoperability. **Correction (2026-08-16 audit):** both repo links in the table above were broken — `tim-mcdonnell/tana` doesn't exist (the actual repo is `tim-mcdonnell/tana-mcp`) and `fabiogaliano/tana-codemode` doesn't exist (the actual repo is `fabiogaliano/tana-mcp-codemode`). Both are small projects (40 and 5 stars respectively) but the links are fixed above.

### Capacities (1 server)

[capacities-mcp](https://github.com/jem-computer/capacities-mcp) acts as a bridge between AI agents and the Capacities knowledge base platform. It provides access to spaces, content search with advanced filters, web link saving with metadata, and daily notes. Capacities' object-oriented data model (where notes are typed objects with properties) gives the MCP server richer semantics than flat-text alternatives. **Correction (2026-08-16 audit):** the previous link (`jemgold/capacities`) was broken — the repo is `jem-computer/capacities-mcp` (41 stars).

## Knowledge Graph & Memory Servers

Beyond platform-specific servers, a growing category of MCP servers provides platform-agnostic persistent memory for AI agents. These don't connect to an existing note-taking app — they *are* the knowledge store, built specifically for AI agent memory.

### Official Memory Server

Anthropic's official Memory MCP server (`@modelcontextprotocol/server-memory`) provides a JSONL-backed knowledge graph with entities, relations, and observations. It's the simplest option but has scaling limitations — `read_graph` dumps your entire graph into context, and there's no memory isolation between projects. For our full analysis, see [our dedicated Memory MCP server review](/reviews/memory-mcp-server/).

### Advanced Knowledge Graph Servers

The knowledge graph category has **exploded** since our March review. What was a niche category is now one of the most actively developed areas in the entire MCP ecosystem, with the top project crossing 30,000 stars.

| Server | Stars | Backend | Key Feature |
|--------|-------|---------|-------------|
| [Graphiti](https://github.com/getzep/graphiti) (by Zep) | 30,000+ | Neo4j | Temporal context graphs, tracks how facts change over time, prescribed + learned ontology |
| [mcp-memory-service](https://github.com/doobidoo/mcp-memory-service) | 1,900+ | SQLite + ONNX | REST API + knowledge graph + autonomous consolidation, 13+ platform support, Apache 2.0 |
| [supermemory-mcp](https://github.com/supermemoryai/supermemory-mcp/tree/main/apps/mcp) | 1,700 (legacy v1 repo) | Cloud/self-hosted | Deprecated free v1 superseded by an OAuth-authenticated hosted server at mcp.supermemory.ai |
| [memento-mcp](https://github.com/gannonh/memento-mcp) | 426 | Neo4j | Semantic retrieval + temporal awareness, vector search, embedding diagnostics |
| [mcp-engram-memory](https://github.com/wyckit/mcp-engram-memory) | — | SQLite | 52 MCP tools, hybrid BM25 + vector, expert routing, lifecycle management |
| [engram](https://github.com/199-biotechnologies/engram) | — | SQLite-vec | Graph intelligence engine, FTS5 + vector + RRF fusion, project scoping |
| [knowledgegraph-mcp](https://github.com/n-r-w/knowledgegraph-mcp) | 20 | PostgreSQL/SQLite | Multi-project separation, fuzzy search (author now recommends dynamic context approaches) |
| [mcp-knowledge-graph](https://github.com/shaneholloman/mcp-knowledge-graph) | — | Local files | Local-first, master database, persistent memory files |

**Graphiti (by Zep)** is the clear leader at 30,000+ stars — unlike static knowledge graphs, Graphiti's context graphs track how facts change over time, maintain provenance to source data, and support both prescribed and learned ontology. The MCP server gives Claude, Cursor, and other MCP clients persistent temporal knowledge graphs that work across sessions. This is purpose-built for agents operating on evolving, real-world data.

**mcp-memory-service** emerged as a serious open-source alternative (1,900+ stars, Apache 2.0) with hybrid BM25 + vector search, knowledge graph with typed edges (causes, fixes, contradicts), local ONNX embeddings, a web dashboard, and support for 13+ platforms including LangGraph, CrewAI, AutoGen, and Claude Desktop. It includes autonomous consolidation and D3.js visualization of memory relationships.

**Supermemory MCP** — **Correction (2026-08-16 audit):** this entry previously described the 1,700-star `supermemoryai/supermemory-mcp` repo as the current offering, "universal memory... no login required, completely free." That repo's own README now carries a deprecation notice: "MCP v1 is being deprecated. Please get the latest version from app.supermemory.ai." The active implementation has moved to [supermemoryai/supermemory](https://github.com/supermemoryai/supermemory/tree/main/apps/mcp), a hosted server at `mcp.supermemory.ai` that requires OAuth token authentication — the opposite of the old "no login required" pitch. The free, login-less v1 described here no longer represents the current product.

**Memento MCP** (426 stars) remains architecturally ambitious with Neo4j-backed semantic retrieval, now enhanced with embedding diagnostics that auto-generate missing embeddings and fall back to text search if vector search fails. Its last commit was October 2025, so treat it as stable rather than under active development.

**Engram** has forked into two projects: the original 199-biotechnologies version (now a graph intelligence engine with SQLite-vec, FTS5 + vector + RRF fusion) and wyckit/mcp-engram-memory (52 MCP tools with expert routing and lifecycle management).

## What's Missing

~~**No Bear Notes MCP server.**~~ **RESOLVED (April 2026).** Bear 2.8 ships official CLI + MCP server + Claude connector, and is now the shipping GA release rather than a beta. The community server by vasylenko (206 stars, 12 tools) also provides full coverage. This was the biggest gap in our March review — now closed.

**No Anytype MCP server.** Anytype's local-first, peer-to-peer architecture would benefit from MCP integration, but the protocol's complexity may deter community builders.

**No Dendron or Foam MCP servers.** [Dendron is in maintenance-only mode](https://randomgeekery.org/post/2023/02/dendron-is-officially-in-maintenance-mode/) (development ceased February 2023), and Foam's VS Code extension architecture doesn't lend itself to MCP integration.

**No standardized PKM interchange.** Each server speaks its platform's native language. There's no MCP server that provides a unified interface across multiple note-taking apps — you can't search Obsidian and Notion simultaneously through one MCP tool. Supermemory's "universal memory" approach partially addresses this by creating its own memory layer rather than searching across existing apps, though (as noted above) its free, login-less v1 server has since been deprecated in favor of an OAuth-gated hosted version.

**Write access improving but uneven.** Apple Notes still can't be written to via MCP. But Bear's official server supports full CRUD, Notion v2.0.0 expanded write capabilities, and the VeryGoodPlugins Evernote server added Markdown-to-ENML auto-conversion. The gap is narrowing.

**No real-time sync or collaboration.** All servers operate in request-response mode. You can't subscribe to note changes, get notified when a collaborator edits a shared document, or have an agent watch for updates. Notion's shift toward remote MCP at mcp.notion.com could eventually enable server-push patterns, but nothing exists yet.

## The Bigger Picture

The note-taking MCP space reveals a clear hierarchy of integration quality:

1. **Best:** Platforms with official MCP servers (Notion, Bear) — these have the deepest tool coverage and are most likely to stay maintained. Bear's entry in April 2026 raised the bar with its bundled CLI + MCP + Claude connector approach. **Correction (2026-08-16 audit):** Tana was previously grouped in this "official" tier — it doesn't belong there. Both Tana MCP servers described in this review (tana-mcp, tana-mcp-codemode) are third-party community projects built against Tana's local Desktop API, not something Tana Inc. ships or maintains itself.
2. **Good:** Platforms with active community servers (Obsidian, Roam, Logseq) — these work well but depend on volunteer maintenance. Obsidian's community ecosystem (4,300+ stars for the top server alone) partially compensates for the lack of official support.
3. **Functional:** Legacy platforms with basic MCP support (Evernote, Joplin) — Joplin's HTTP/SSE transport support and 26-tool coverage show these can still evolve.
4. **Dominant:** Knowledge graph servers purpose-built for AI (Graphiti/Zep, mcp-memory-service) — with 30,000+ stars for the leading project, this category has graduated from "emerging" to the largest and most active segment of the note-taking MCP ecosystem.

The most significant trend since March is the knowledge graph category's explosive growth. Graphiti's 30,000+ stars and temporal context graphs represent a fundamentally different vision of AI memory — one where agents don't just store facts but track how facts change over time. mcp-memory-service (1,900+ stars) has emerged as a viable local-first alternative with ONNX embeddings; Supermemory's original free, login-less MCP has since been deprecated in favor of an OAuth-gated hosted server, so it's a less clear-cut "third alternative" than it looked in April.

{{< verdict rating="4.5" summary="Bear fills biggest gap, knowledge graphs explode past 30k stars" >}}
The note-taking and knowledge management MCP ecosystem has matured significantly since our March review. Bear 2.8's official MCP support closed the largest platform gap we identified and has since gone GA (no longer beta). Notion's v2.0.0 rewrite with data sources abstraction shows the leading official server evolving rapidly (now 4,600+ stars). Obsidian's community continues to thrive despite no official server (4,300+ stars, 8+ implementations). But the real story is knowledge graph servers: Graphiti/Zep crossing 30,000 stars and mcp-memory-service passing 1,900 stars — the agent memory category now rivals platform-specific servers in combined stargazer count. Every major PKM platform has MCP coverage, write access is improving (Bear full CRUD, Notion expanded writes, Evernote auto-conversion), and the knowledge graph options have moved from "interesting experiment" to "production-grade infrastructure." The remaining gaps — Anytype, standardized PKM interchange, real-time sync — feel smaller against what's now available.
{{< /verdict >}}

*This review was refreshed on 2026-04-28 using Claude Opus 4.6 (Anthropic); citations and figures re-verified 2026-08-16 using Claude Sonnet 5 (Anthropic). Originally published 2026-03-16.*
