# Note-Taking & Knowledge Management MCP Servers — Your Second Brain Meets AI Agents

> Note-taking and knowledge management MCP servers connect AI agents to your personal knowledge bases. We reviewed 40+ servers across 10 subcategories.


Note-taking and knowledge management tools are where people store their most valuable thinking — research notes, project plans, meeting records, personal wikis, and the connective tissue between ideas. Connecting AI agents to these systems is one of the most natural MCP use cases: instead of copy-pasting context into prompts, an agent can search, read, and update your notes directly. Part of our **[Business & Productivity MCP category](/categories/business-productivity/)**.

The ecosystem has responded accordingly. Over 40 MCP servers now cover every major note-taking platform, from mainstream tools like Obsidian and Notion to niche PKM systems like Tana and Capacities. The landscape splits into two broad camps: **platform-specific servers** that connect to a particular app, and **knowledge graph servers** that provide platform-agnostic persistent memory for AI agents.

The headline findings: **Obsidian has the most community servers** (8) but no official one — three different architectural approaches compete (see [our dedicated Obsidian MCP review](/reviews/obsidian-mcp-servers/)). **Notion has the strongest official integration** with 20+ tools from Notion themselves (see [our dedicated Notion review](/reviews/notion-mcp-server/)). **Apple Notes gets surprisingly good MCP support** through RAG-powered semantic search. **Evernote and Joplin** both have functional MCP servers despite declining market share. **Roam Research, Logseq, and Tana** each have dedicated servers that respect their unique data models. **Knowledge graph memory servers** have evolved far beyond Anthropic's official implementation, with Memento MCP offering Neo4j-backed semantic retrieval and Engram providing hybrid search across three algorithms.

## Platform-Specific Servers

### Obsidian (8 servers)

Obsidian dominates the note-taking MCP space with eight community servers — more than any other platform. No official Obsidian MCP server exists, and Obsidian has made no public statements about MCP support. The community fills the gap through three architectural approaches: direct file access (reading vault Markdown files), REST API integration (via Obsidian's Local REST API plugin), and native plugin architecture (running inside Obsidian itself).

The most-starred server (mcp-obsidian by MarkusPfundstein, 3,000 stars) hasn't been updated since November 2024. The most technically sophisticated (obsidian-mcp-plugin by aaronsb, 256 stars) runs as an Obsidian plugin with bearer token auth. For the full breakdown of all eight servers, architectures, and recommendations, see [our dedicated Obsidian MCP servers review](/reviews/obsidian-mcp-servers/).

### Notion (Official Server)

Notion is one of the few note-taking platforms to ship an official MCP server. It provides 20+ tools covering pages, databases, comments, search, and user management through Notion's API. The server handles authentication via Notion integration tokens and supports both personal and workspace-level access.

For our full analysis of the Notion MCP server, see [our dedicated Notion review](/reviews/notion-mcp-server/).

### Apple Notes (2+ servers)

Apple Notes has no official MCP support, but community servers provide surprisingly capable access:

| Server | Approach | Key Feature |
|--------|----------|-------------|
| [mcp-apple-notes](https://github.com/RafalWilinski/mcp-apple-notes) (Rafal) | SQLite + embeddings | RAG over Apple Notes using MiniLM-L6-v2 on-device embeddings for semantic search |
| [apple-notes-mcp](https://github.com/sirmews/apple-notes-mcp) (Sirmews) | SQLite direct | Reads Apple Notes' nested SQLite database directly from macOS filesystem |

The RAG approach from RafalWilinski is particularly interesting — it indexes your notes locally using on-device embeddings, meaning an AI agent can find semantically related notes, not just keyword matches. The trade-off is macOS-only (Apple Notes stores its database in a platform-specific location) and read-only access. No Apple Notes MCP server supports creating or editing notes — Apple's sandboxing makes write access extremely difficult without going through AppleScript.

### Evernote (2+ servers)

Despite Evernote's declining market position, two MCP servers keep it connected to the AI agent ecosystem:

| Server | Language | Key Feature |
|--------|----------|-------------|
| [evernote-mcp-server](https://github.com/brentmid/evernote-mcp-server) (Brent) | TypeScript | Claude Desktop integration, natural language note queries |
| [mcp-evernote](https://github.com/verygoodplugins/mcp-evernote) (VeryGoodPlugins) | TypeScript | Full CRUD + sync, note management and organization |

Both servers use Evernote's API for authenticated access. The VeryGoodPlugins implementation offers more complete coverage with note creation, editing, and synchronization, while Brent's focuses on read-heavy search workflows. Evernote's API has historically been finicky with rate limits and authentication quirks — expect some friction during setup.

### Joplin (1 server)

[joplin-mcp](https://github.com/alondmnt/joplin-mcp) connects to the open-source Joplin note-taking app via its Python API (joppy). It's a FastMCP-based server that supports reading, searching, and managing notes, notebooks, and tags. Joplin's local-first, Markdown-based architecture makes it a natural fit for MCP — the data model maps cleanly to MCP tools. The server requires Joplin's Web Clipper service to be running for API access.

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

Tana's Desktop app exposes a local API that the MCP server bridges, allowing AI tools to operate on structured outlines and connected knowledge rather than flat text. This is one of the few cases where the note-taking platform actively designed for AI interoperability.

### Capacities (1 server)

[capacities-mcp](https://github.com/jemgold/capacities) acts as a bridge between AI agents and the Capacities knowledge base platform. It provides access to spaces, content search with advanced filters, web link saving with metadata, and daily notes. Capacities' object-oriented data model (where notes are typed objects with properties) gives the MCP server richer semantics than flat-text alternatives.

## Knowledge Graph & Memory Servers

Beyond platform-specific servers, a growing category of MCP servers provides platform-agnostic persistent memory for AI agents. These don't connect to an existing note-taking app — they *are* the knowledge store, built specifically for AI agent memory.

### Official Memory Server

Anthropic's official Memory MCP server (`@modelcontextprotocol/server-memory`) provides a JSONL-backed knowledge graph with entities, relations, and observations. It's the simplest option but has scaling limitations — `read_graph` dumps your entire graph into context, and there's no memory isolation between projects. For our full analysis, see [our dedicated Memory MCP server review](/reviews/memory-mcp-server/).

### Advanced Knowledge Graph Servers

| Server | Stars | Backend | Key Feature |
|--------|-------|---------|-------------|
| [memento-mcp](https://github.com/gannonh/memento-mcp) | — | Neo4j | Semantic retrieval + temporal awareness, vector search |
| [engram](https://github.com/199-biotechnologies/engram) | — | SQLite + Jina v5 | Hybrid BM25 + ColBERT + knowledge graph search |
| [knowledgegraph-mcp](https://github.com/n-r-w/knowledgegraph-mcp) | — | PostgreSQL/SQLite | Multi-project separation, fuzzy search, enhanced official fork |
| [mcp-knowledge-graph](https://github.com/shaneholloman/mcp-knowledge-graph) | — | Local files | Local-first, master database, persistent memory files |
| [SuperLocalMemoryV2](https://github.com/) | — | Local | Zero cloud dependency, 17+ AI tool compatibility, pattern learning |

**Memento MCP** is the most architecturally ambitious — it uses Neo4j as a graph database with vector search capabilities, enabling both structural graph queries and semantic similarity search. It also tracks temporal relationships, so an agent can reason about when information was added or changed.

**Engram** takes a different approach with hybrid search: BM25 for keyword matching, ColBERT for semantic understanding, and knowledge graph for relational queries. Using SQLite with temporal fields and Jina v5 embeddings, it aims for the best of all search paradigms in a single server.

**knowledgegraph-mcp** enhances Anthropic's official implementation with practical features: PostgreSQL or SQLite backends (instead of flat JSONL), project separation (so different codebases get different memory spaces), and fuzzy search.

## What's Missing

**No Bear Notes MCP server.** Bear has a loyal macOS/iOS user base and a clean Markdown-based data model, but no dedicated MCP server exists beyond generic SQLite access patterns.

**No Anytype MCP server.** Anytype's local-first, peer-to-peer architecture would benefit from MCP integration, but the protocol's complexity may deter community builders.

**No Dendron or Foam MCP servers.** Dendron is in maintenance-only mode (development ceased February 2023), and Foam's VS Code extension architecture doesn't lend itself to MCP integration.

**No standardized PKM interchange.** Each server speaks its platform's native language. There's no MCP server that provides a unified interface across multiple note-taking apps — you can't search Obsidian and Notion simultaneously through one MCP tool.

**Write access is limited.** Many servers are read-only or read-heavy. Apple Notes can't be written to at all via MCP. Evernote write operations are API-limited. Even Obsidian servers vary widely in their write capabilities. The pattern is clear: reading notes is solved; reliably creating and editing them is still hard.

**No real-time sync or collaboration.** All servers operate in request-response mode. You can't subscribe to note changes, get notified when a collaborator edits a shared document, or have an agent watch for updates. This limits the utility for team knowledge bases.

## The Bigger Picture

The note-taking MCP space reveals a clear hierarchy of integration quality:

1. **Best:** Platforms with official MCP servers (Notion, Tana) — these have the deepest tool coverage and are most likely to stay maintained
2. **Good:** Platforms with active community servers (Obsidian, Roam, Logseq) — these work well but depend on volunteer maintenance
3. **Functional:** Legacy platforms with basic MCP support (Evernote, Joplin) — these exist but may not keep pace with MCP spec changes
4. **Emerging:** Knowledge graph servers purpose-built for AI (Memento, Engram) — these may eventually replace platform-specific servers as the "canonical" way AI agents store and retrieve knowledge

The most interesting trend is the knowledge graph servers evolving beyond simple memory into sophisticated retrieval systems. Memento MCP's temporal awareness and Engram's hybrid search suggest that AI agent memory won't converge on any existing note-taking platform — it'll become its own category entirely.

{{< verdict rating="4" summary="Every major platform covered, knowledge graphs point to the future" >}}
The note-taking and knowledge management MCP ecosystem is one of the broadest in the entire MCP landscape. Every major PKM platform has at least one MCP server, and the knowledge graph category is innovating faster than the platforms themselves. Obsidian leads in sheer number of servers but lacks official support. Notion leads in official integration quality. The advanced knowledge graph servers (Memento, Engram) are where the most ambitious engineering is happening. The main limitations are inconsistent write access, no cross-platform unified search, and the read-only constraint on Apple Notes. If you use any note-taking tool, there's almost certainly an MCP server for it — and if you want AI-native memory, the knowledge graph options are getting genuinely sophisticated.
{{< /verdict >}}

*This review was last edited on 2026-03-16 using Claude Opus 4.6 (Anthropic).*

