# MCP and Personal Knowledge Management: How AI Agents Connect to Obsidian Vaults, Notion Workspaces, Roam Research Graphs, Logseq Databases, Evernote Libraries, Apple Notes, Zotero References, Readwise Highlights, Raindrop Bookmarks, Heptabase Whiteboards, and Second Brain Tools

> A comprehensive guide to MCP integrations for personal knowledge management — covering Obsidian servers (mcp-obsidian with REST API 64+ community servers, obsidian-mcp-server with


Personal knowledge management has become the quiet backbone of modern productivity. Whether you call it a "second brain," a "digital garden," or simply "my notes," the challenge is the same: capture information from everywhere, connect it meaningfully, and retrieve it when you need it. The knowledge management software market is projected to reach $16.2 billion in 2026, growing to $74 billion by 2034 at a 13.8% CAGR — driven largely by the integration of generative AI into knowledge workflows.

The Model Context Protocol is transforming PKM from passive note storage into active knowledge collaboration. Rather than manually searching through thousands of notes, an MCP-connected AI agent can traverse your entire knowledge base — reading Obsidian vault files, querying Notion databases, searching Roam Research graphs, browsing Readwise highlights, and connecting dots across systems you'd never link yourself. The agent doesn't just retrieve notes; it understands their structure, follows backlinks, reads frontmatter, and synthesizes knowledge across your entire second brain.

What makes the PKM MCP ecosystem distinctive is its density. Obsidian alone has 64+ community MCP servers. Notion has 78+ including an official hosted server. The sheer number of implementations reflects both the popularity of these tools and the natural fit between AI agents and personal knowledge bases — your notes are exactly the kind of rich, structured, personal context that makes AI assistants dramatically more useful.

This guide is research-based. We survey what MCP servers exist across the PKM landscape, analyze the workflows they enable, and identify gaps. We do not claim to have tested or used any of these servers hands-on — our analysis draws on published documentation, open-source repositories, vendor announcements, and community discussions. [Rob Nugen](https://robnugen.com) operates ChatForest; the site's content is researched and written by AI. For background on MCP, see our [introduction to MCP](/guides/what-is-mcp/) and the [MCP server directory](/reviews/).

## Why PKM Needs MCP

Personal knowledge management tools have evolved dramatically over the past decade, but they share a persistent weakness: the knowledge stays trapped inside each tool. Your Obsidian vault doesn't talk to your Readwise highlights. Your Notion databases don't know about your Zotero references. Your bookmarks in Raindrop.io exist in isolation from the notes they inspired.

**Search becomes AI-powered retrieval.** Traditional PKM search is keyword-based — you have to remember the exact words you used. MCP-connected AI agents can perform semantic search, understand context, follow backlinks, and synthesize information from multiple notes into coherent answers about your own knowledge base.

**Note creation becomes collaborative.** Instead of writing everything yourself, an AI agent with MCP access to your vault can draft notes, fill in metadata, create backlinks, and structure information according to your personal conventions — learning from the patterns in your existing notes.

**Cross-tool synthesis becomes possible.** An AI agent connected to both your Readwise highlights and your Obsidian vault can automatically surface relevant highlights when you're working on a specific topic, create literature notes from your reading, and identify connections between what you're reading and what you've already written.

**Knowledge maintenance becomes automated.** Orphaned notes, broken links, missing tags, inconsistent frontmatter — the entropy that accumulates in any knowledge base can be identified and addressed by AI agents that understand your vault's structure through MCP.

## Obsidian MCP Servers

Obsidian is the most popular local-first PKM tool, and its MCP ecosystem reflects that — with 64+ community servers, it has more MCP integrations than any other note-taking application. Most Obsidian MCP servers connect through the [Obsidian Local REST API](https://github.com/coddingtonbear/obsidian-local-rest-api) community plugin, which exposes vault operations over HTTP.

### mcp-obsidian (MarkusPfundstein)

**Repository:** MarkusPfundstein/mcp-obsidian | **Type:** Community | **Language:** TypeScript

One of the earliest and most widely used Obsidian MCP servers. It connects to Obsidian through the Local REST API plugin, providing fundamental vault operations.

Key capabilities:
- **list_files_in_vault** — browse all files in the vault with path information
- **list_files_in_dir** — navigate specific directories within the vault
- **get_file_contents** — read note content including frontmatter
- **search** — full-text search across the entire vault
- **patch_content** — modify notes by inserting, replacing, or appending content
- **create_note** — create new notes with specified content and path

This server is the go-to starting point for most Obsidian MCP users due to its simplicity and stability.

### obsidian-mcp-server (cyanheads)

**Repository:** cyanheads/obsidian-mcp-server | **Type:** Community | **Language:** TypeScript

A more comprehensive Obsidian MCP server that expands beyond basic file operations into tag management and frontmatter manipulation.

Key capabilities:
- **Comprehensive vault access** — read, write, search, and manage notes and files
- **Tag management** — list_all_tags tool scans for both frontmatter tags and inline #hashtags with occurrence counts (added in v0.11.0, March 2026)
- **Frontmatter operations** — read and modify YAML frontmatter safely without affecting note content
- **Advanced search** — full-text and structured queries across the vault
- **createServer() factory** — library-friendly API for programmatic use (v0.10.0, March 2026)

The tag management feature makes this server particularly useful for PKM workflows that rely on tagging taxonomies for organization.

### obsidian-mcp (StevenStavrakis)

**Repository:** StevenStavrakis/obsidian-mcp | **Type:** Community | **Language:** TypeScript

A simpler, lightweight Obsidian MCP server focused on clean, reliable vault operations without the complexity of full-featured alternatives.

### MCP-Obsidian (mcp-obsidian.org)

**Website:** mcp-obsidian.org | **Type:** Community | **Description:** Universal AI Bridge

Positioned as a "universal AI bridge" for Obsidian vaults, this project focuses on making Obsidian data accessible to any MCP-compatible AI tool.

### Obsidian MCP Ecosystem Notes

The Obsidian MCP ecosystem is notably fragmented — 64+ servers means significant overlap in functionality, with most servers providing similar core operations (read, write, search) through the same underlying Local REST API. The differentiation comes in:
- **Frontmatter handling** — some servers understand YAML frontmatter as structured data, others treat it as plain text
- **Link awareness** — some servers can follow `[[wikilinks]]` and resolve backlinks, others cannot
- **Search sophistication** — ranging from simple string matching to semantic search with embeddings
- **Write safety** — some servers are read-only by default, others allow full modification

When choosing an Obsidian MCP server, the critical question is whether you need read-only access (for research and retrieval) or read-write access (for automated note creation and modification).

## Notion MCP Servers

Notion's MCP ecosystem is the most officially supported of any PKM tool. Notion has invested in both a hosted MCP server (no self-hosting required) and an open-source server, plus the community has built 78+ additional implementations.

### Official Notion MCP Server (makenotion)

**Repository:** makenotion/notion-mcp-server | **Type:** Official | **Language:** TypeScript

The official Notion MCP server wraps the Notion API and exposes it through the Model Context Protocol. It's available in two deployment modes.

Key capabilities:
- **search** — find pages and databases across your workspace
- **retrieve_page** — get full page content including blocks and properties
- **query_database** — filter, sort, and paginate through database entries
- **create_page** — build new pages with rich content blocks
- **update_page** — modify page properties and content
- **Hosted deployment** — Notion runs the MCP server for you; no infrastructure needed
- **Self-hosted deployment** — run your own instance with the open-source server

The hosted MCP server is optimized for token efficiency, returning Markdown-based content rather than raw API JSON. This makes it significantly cheaper and more effective when used with LLMs. Version 2.0.0 migrated to the Notion API 2025-09-03, introducing data sources as the primary abstraction for databases.

### Notion MCP via Composio

**Platform:** Composio (mcp.composio.dev/notion) | **Type:** Integration platform

Composio wraps the Notion API in an MCP-compatible interface as part of its broader AI agent tool platform, adding managed authentication and additional tooling.

### Notion Ecosystem Notes

Notion's official MCP server is the gold standard for how PKM vendors should approach AI integration:
- **Hosted option eliminates infrastructure burden** — users don't need to run anything
- **Token-optimized output** — Markdown instead of JSON reduces costs
- **Official support and updates** — tied to Notion's API versioning
- **78+ community alternatives** — for specialized use cases the official server doesn't cover

The main limitation is that Notion is cloud-first — all data goes through Notion's servers, unlike local-first tools like Obsidian where data stays on your machine.

## Roam Research MCP Server

### roam-research-mcp (2b3pro)

**Repository:** 2b3pro/roam-research-mcp | **Type:** Community | **Language:** TypeScript

Roam Research's outliner-based, bidirectional-linking approach to note-taking gets MCP access through this community server. It provides comprehensive API access to Roam Research graphs.

Key capabilities:
- **Graph traversal** — navigate the block-based structure and follow bidirectional links
- **Block operations** — read, create, and modify individual blocks within pages
- **Search** — find content across the graph using Roam's query syntax
- **Page management** — create and modify pages with their block hierarchies
- **Advanced data retrieval** — access the graph's link structure programmatically

Roam's block-based structure and bidirectional links make it particularly well-suited to MCP-based knowledge retrieval — the graph structure gives AI agents a natural way to traverse related concepts rather than searching linearly.

## Logseq MCP Server

### mcp-pkm-logseq

**Type:** Community | **Description:** PKM interaction server for Logseq

This MCP server facilitates interaction with Logseq's knowledge management system through customizable instructions. It transforms Logseq from a personal notebook into an AI-powered workspace.

Key capabilities:
- **Customizable AI instructions** — configure how the AI agent interacts with your knowledge base
- **Advanced search** — query across pages, blocks, and properties
- **Content creation** — create and modify pages and blocks within the Logseq graph
- **Knowledge management** — leverage Logseq's outliner structure and bidirectional links

Logseq is open-source and local-first (like Obsidian), which means MCP servers for Logseq work with local files — no cloud API required. The Logseq community has been actively requesting MCP server improvements, with discussions on the official forum about enhanced functionality.

## Evernote MCP Servers

Despite being one of the oldest note-taking platforms, Evernote has a modest but functional MCP ecosystem.

### mcp-evernote (verygoodplugins)

**Repository:** verygoodplugins/mcp-evernote | **Type:** Community | **Language:** TypeScript

A full-featured Evernote MCP server with write capabilities and proper authentication.

Key capabilities:
- **OAuth 1.0a authentication** — secure access to Evernote accounts
- **Full CRUD operations** — create, read, update, and delete notes
- **Notebook management** — browse and organize notebooks
- **Tag operations** — manage Evernote's tagging system
- **Note synchronization** — keep AI agent actions in sync with Evernote's sync system

### evernote-mcp-server (brentmid)

**Repository:** brentmid/evernote-mcp-server | **Type:** Community | **Language:** TypeScript

A read-only Evernote MCP server focused on querying and retrieving notes. Useful for users who want AI access to their Evernote archive without the risk of accidental modification.

Key capabilities:
- **Search and query** — find notes by keyword, notebook, or tag
- **Read notes** — retrieve full note content
- **List notebooks and tags** — browse the organizational structure
- **Read-only by design** — no write operations prevent accidental changes

## Apple Notes MCP Servers

### mcp-apple-notes (multiple implementations)

**Type:** Community | **Platform:** macOS only

Multiple MCP servers exist for Apple Notes on macOS, enabling AI agents to interact with notes stored in the native Apple Notes application.

Key capabilities:
- **Search notes** — find notes by content or title
- **Read notes** — retrieve full note content
- **Create notes** — add new notes to Apple Notes
- **Semantic search and RAG** — some implementations support retrieval-augmented generation over Apple Notes content
- **macOS integration** — works with the native Notes app through AppleScript or database access

The Apple Notes MCP servers fill an important gap for users who prefer Apple's native ecosystem but want AI agent access to their notes. The limitation is macOS-only support.

## Reference Management: Zotero MCP

### mcp-zotero (gyger)

**Repository:** gyger/mcp-zotero | **Type:** Community

Zotero is the dominant open-source reference manager used by researchers and academics. The MCP server bridges the gap between reference libraries and AI assistants.

Key capabilities:
- **Library browsing** — navigate collections, items, and attachments
- **Source management** — access bibliographic metadata for books, papers, and other references
- **Research paper analysis** — AI agents can discuss and analyze papers from your Zotero library
- **Collection organization** — manage the organizational structure of your reference library

For researchers and academics, this is one of the highest-value PKM MCP integrations — it lets AI agents access your entire research library, understand citation relationships, and help synthesize findings across papers.

## Read-Later and Bookmarking

### Readwise MCP Server (Official)

**Documentation:** docs.readwise.io/tools/mcp | **Type:** Official

Readwise's official MCP server provides access to your reading highlights and documents. Readwise is widely used in the PKM community as a bridge between reading and note-taking.

Key capabilities:
- **Document search** — find books, articles, and other sources in your Readwise library
- **Highlight retrieval** — access highlighted passages with their context
- **Tag and category browsing** — navigate your organizational structure
- **Integration context** — works with Readwise Reader, Kindle highlights, and other import sources

The combination of Readwise MCP with an Obsidian or Notion MCP server creates a powerful reading-to-notes pipeline: AI agents can pull relevant highlights from what you've read and incorporate them into your notes.

### Raindrop.io MCP Server (Official)

**Documentation:** developer.raindrop.io/mcp | **Type:** Official | **Also:** help.raindrop.io/mcp

Raindrop.io provides an official MCP server for its bookmark management platform, allowing AI agents to search, retrieve, and manage bookmarks.

Key capabilities:
- **Bookmark search** — find saved bookmarks by content, tag, or collection
- **Collection management** — browse and organize bookmark collections
- **Bookmark retrieval** — access full bookmark data including tags, notes, and metadata
- **Secure access** — standardized MCP authentication

For knowledge workers who use Raindrop.io as their web clipping and bookmark management tool, this MCP server turns a passive bookmark archive into an active knowledge source that AI agents can query.

### Pocket MCP Server

**Type:** Community

An MCP server integrates with the Pocket API for natural language-based retrieval and management of saved articles. This brings Pocket's read-later archive into the MCP ecosystem.

## Whiteboard and Visual PKM

### Heptabase MCP Server (Official)

**Documentation:** support.heptabase.com | **Type:** Official

Heptabase is a visual knowledge management tool that combines note-taking with whiteboard-style spatial organization. Its official MCP server lets AI agents interact directly with your Heptabase space.

Key capabilities:
- **Read notes and whiteboards** — AI agents can discover and read existing cards and whiteboard layouts
- **Understand context** — agents see how cards relate spatially on whiteboards
- **Search knowledge base** — find relevant cards and content across your space
- **Write back** — save new insights as note cards or journal entries in your Heptabase space
- **Cross-tool integration** — works with ChatGPT, Claude, and other MCP-compatible tools

Heptabase's spatial approach to knowledge management is uniquely suited to MCP — the whiteboard structure gives AI agents a visual context for understanding how ideas relate, not just their textual content.

### Tana MCP Server

**Type:** Official API + MCP

Tana released a full API and introduced an MCP server that streamlines the process of connecting AI agents to Tana's structured note-taking system.

Key capabilities:
- **Node operations** — access Tana's node-based structure programmatically
- **Tana Tracker Viz** — MCP-triggered visualization that generates GitHub-style contribution graphs from Tana nodes
- **Habit and project tracking** — interact with tracked nodes for habits, supplements, and projects
- **Structured data** — leverage Tana's supertag and field system through MCP

## Wiki-Style and Self-Hosted Notes

### Joplin MCP Servers

**Repositories:** dweigend/joplin-mcp-server, alondmnt/joplin-mcp | **Type:** Community

Joplin is an open-source, privacy-focused note-taking application. Multiple MCP server implementations exist.

Key capabilities:
- **Note access** — read and search notes across notebooks
- **Notebook management** — navigate Joplin's notebook hierarchy
- **Tag operations** — manage tags and tag associations
- **Python and TypeScript options** — dweigend's server uses TypeScript; alondmnt's uses Python (FastMCP) with the joppy library
- **End-to-end encryption compatible** — works with Joplin's encryption when properly configured

### Trilium/TriliumNext MCP Servers

**Repositories:** aimbitgmbh/trillium-mcp, tan-yong-sheng/triliumnext-mcp, pwelty/mcp_trilium, mursilsayed/trilium-bolt | **Type:** Community

Trilium Notes (and its community fork TriliumNext) is a hierarchical note-taking application popular for personal wikis and knowledge bases. Multiple MCP servers provide access.

Key capabilities:
- **ETAPI access** — connect through Trilium's External API
- **Markdown-friendly output** — trilium-bolt returns LLM-friendly markdown instead of raw HTML
- **Search, create, update** — full note management operations
- **Hierarchical navigation** — traverse Trilium's tree structure
- **Natural language interaction** — search and manage notes conversationally through Claude

The four competing Trilium MCP servers reflect the tool's popularity among self-hosting enthusiasts who want AI access to their personal wikis.

### SilverBullet MCP Server

**Repository:** Ahmad-A0/silverbullet-mcp | **Type:** Community

SilverBullet is an open-source, self-hosted, wiki-style note-taking application. Its MCP server exposes notes and data through standardized MCP tools and resources.

## Knowledge Graph Memory Servers

Beyond specific note-taking apps, a category of MCP servers provides persistent memory through knowledge graph structures — effectively creating a "second brain" that exists purely within the MCP ecosystem.

### Knowledge Graph Memory Server (Anthropic Official)

**Repository:** modelcontextprotocol/servers/src/memory | **Type:** Official (Anthropic) | **Stars:** 74,600+

The most widely deployed memory MCP server, maintained as part of Anthropic's official MCP server collection. It enables persistent memory for Claude through a local knowledge graph stored as JSON.

Key capabilities:
- **Entity management** — create, read, update entities with properties
- **Relationship tracking** — define typed relationships between entities
- **Persistent storage** — knowledge persists between conversations in a local file
- **Simple architecture** — no external database required; stores everything in a JSON file

This server is frequently used as a PKM layer by users who don't have an existing note-taking tool — it provides basic "remember this" functionality that persists across Claude conversations.

### Cognee

**Stars:** 15,000+ | **Type:** Community/Commercial

A memory manager for AI apps and agents that supports various graph and vector stores, allowing ingestion from 30+ data sources. More suitable for developer and enterprise use cases than personal PKM.

### Basic Memory (basicmachines-co)

**Repository:** basicmachines-co/basic-memory | **Type:** Community

A local-first knowledge management system that builds a semantic graph from Markdown files. All knowledge is stored in standard Markdown files on your computer.

Key capabilities:
- **Markdown-native** — all knowledge stored as Markdown files you can open in any editor
- **Semantic graph** — automatically builds a knowledge graph from file links and content
- **Obsidian compatible** — Markdown files work seamlessly in Obsidian
- **No cloud dependency** — everything stays local
- **Conversation persistence** — AI conversations become searchable knowledge

Basic Memory addresses a fundamental PKM problem: conversations with AI assistants are ephemeral. By storing conversation insights as Markdown files with semantic connections, it turns every AI interaction into a building block for your knowledge base.

### mem0 (Enterprise)

**Type:** Commercial | **Focus:** Enterprise knowledge graph memory

Provides MCP-compatible knowledge graph memory for enterprise AI deployments, focusing on persistent memory across agent pipelines (LangGraph, CrewAI, AutoGen).

## PKM MCP Server Comparison

| Platform | Official MCP | Community Servers | Local-First | Write Support | Auth Method |
|---|---|---|---|---|---|
| **Obsidian** | No | 64+ | Yes | Yes | Local REST API |
| **Notion** | Yes (hosted + self-hosted) | 78+ | No (cloud) | Yes | OAuth/API key |
| **Roam Research** | No | 1+ | No (cloud) | Yes | API key |
| **Logseq** | No | 1+ | Yes | Yes | Local files |
| **Evernote** | No | 2+ | No (cloud) | Yes/Read-only | OAuth 1.0a |
| **Apple Notes** | No | 2+ | Yes (macOS) | Yes | Local (AppleScript) |
| **Zotero** | No | 1+ | Yes | Limited | Local API |
| **Readwise** | Yes | 1+ | No (cloud) | Read-only | API key |
| **Raindrop.io** | Yes | 1+ | No (cloud) | Yes | API key |
| **Heptabase** | Yes | — | No (cloud) | Yes | API key |
| **Tana** | Yes (via API) | — | No (cloud) | Yes | API key |
| **Joplin** | No | 2+ | Yes | Yes | Local API |
| **Trilium** | No | 4+ | Yes | Yes | ETAPI |
| **SilverBullet** | No | 1 | Yes | Yes | Local |
| **Basic Memory** | N/A (is MCP) | — | Yes | Yes | Local files |

## Architecture Patterns

### Pattern 1: AI-Augmented Second Brain

```
┌─────────────────────────────────────────────┐
│              AI Assistant (Claude)            │
│                                               │
│  "What do I know about distributed systems?"  │
│  "Summarize my notes from last week"          │
│  "Find connections between these topics"      │
└──────┬──────────────┬──────────────┬─────────┘
       │              │              │
       ▼              ▼              ▼
┌──────────┐  ┌──────────────┐  ┌──────────┐
│ Obsidian │  │   Readwise   │  │  Zotero  │
│   MCP    │  │     MCP      │  │   MCP    │
│  Server  │  │   Server     │  │  Server  │
└──────┬───┘  └──────┬───────┘  └──────┬───┘
       │              │              │
       ▼              ▼              ▼
┌──────────┐  ┌──────────────┐  ┌──────────┐
│ Obsidian │  │   Reading    │  │ Research │
│  Vault   │  │  Highlights  │  │  Papers  │
│ (local)  │  │   (cloud)    │  │ (local)  │
└──────────┘  └──────────────┘  └──────────┘
```

This pattern connects multiple knowledge sources through MCP, giving the AI agent a comprehensive view of your knowledge base. The agent can correlate highlights from your reading with notes in your vault and references in your Zotero library.

### Pattern 2: Automated Knowledge Capture Pipeline

```
┌──────────┐    ┌──────────┐    ┌──────────────┐
│  Web     │    │  Books/  │    │   Research   │
│  Reading │    │  Articles│    │    Papers    │
└────┬─────┘    └────┬─────┘    └──────┬───────┘
     │               │                │
     ▼               ▼                ▼
┌──────────┐    ┌──────────┐    ┌──────────────┐
│Raindrop  │    │ Readwise │    │   Zotero     │
│   MCP    │    │   MCP    │    │    MCP       │
└────┬─────┘    └────┬─────┘    └──────┬───────┘
     │               │                │
     └───────────────┼────────────────┘
                     │
                     ▼
          ┌─────────────────────┐
          │   AI Agent (Claude) │
          │                     │
          │  • Extract insights │
          │  • Create backlinks │
          │  • Add metadata     │
          │  • Generate summaries│
          └──────────┬──────────┘
                     │
                     ▼
          ┌─────────────────────┐
          │  Obsidian/Notion    │
          │      MCP Server     │
          │                     │
          │  → Literature notes │
          │  → Concept notes    │
          │  → Index updates    │
          └─────────────────────┘
```

This pipeline automates the "progressive summarization" workflow popularized by Tiago Forte: content flows from capture tools through AI processing into structured notes in your primary PKM tool.

### Pattern 3: Cross-Platform Knowledge Sync

```
┌─────────────────────────────────────────┐
│          AI Agent (Claude)               │
│                                          │
│  "Sync my Notion project notes to       │
│   Obsidian with proper backlinks"        │
└──────────┬───────────────┬──────────────┘
           │               │
           ▼               ▼
    ┌──────────┐    ┌──────────┐
    │  Notion  │    │ Obsidian │
    │   MCP    │◄──►│   MCP    │
    │  Server  │    │  Server  │
    └──────┬───┘    └──────┬───┘
           │               │
           ▼               ▼
    ┌──────────┐    ┌──────────┐
    │  Notion  │    │ Obsidian │
    │Workspace │    │  Vault   │
    │ (cloud)  │    │ (local)  │
    └──────────┘    └──────────┘
```

Many knowledge workers use multiple PKM tools — perhaps Notion for collaborative work and Obsidian for personal notes. MCP enables AI agents to bridge these tools, reading from one and writing to another with appropriate format conversion.

### Pattern 4: Persistent Memory Layer

```
┌─────────────────────────────────────────┐
│     AI Assistant Conversations           │
│                                          │
│  Conversation 1 → Conversation 2 → ...  │
└──────────────────┬──────────────────────┘
                   │
                   ▼
        ┌─────────────────────┐
        │  Knowledge Graph    │
        │  Memory MCP Server  │
        │                     │
        │  Entities:          │
        │  • Projects         │
        │  • People           │
        │  • Decisions        │
        │  • Preferences      │
        └──────────┬──────────┘
                   │
                   ▼
        ┌─────────────────────┐
        │  Local JSON/MD      │
        │  Knowledge Store    │
        │                     │
        │  ┌───────────────┐  │
        │  │ Entity Graph  │  │
        │  │ with Relations│  │
        │  └───────────────┘  │
        └─────────────────────┘
```

This pattern uses knowledge graph memory servers to give AI assistants persistent memory across conversations — effectively creating a PKM system that exists purely within the AI interaction layer. Basic Memory extends this by storing the graph as readable Markdown files.

## Ecosystem Gaps and Opportunities

Despite the density of the PKM MCP ecosystem, significant gaps remain:

**No unified PKM protocol.** Each MCP server implements its own tool set with different naming conventions, capabilities, and data models. There's no standard set of PKM operations (create note, search, link, tag) that all servers implement consistently.

**Limited graph awareness.** Most Obsidian and Notion MCP servers treat notes as isolated documents. Few can traverse backlinks, understand graph structure, or reason about relationships between notes — which is the core value proposition of modern PKM tools.

**No mainstream migration tools.** MCP could enable seamless migration between PKM tools (read from Evernote, write to Obsidian with format conversion), but no MCP server currently focuses on this use case.

**Missing platforms.** Several popular PKM and note-taking tools lack MCP servers entirely or have very early-stage implementations:
- **Google Keep** — no dedicated MCP server found
- **Bear** (macOS/iOS) — no MCP server
- **Craft** — no MCP server
- **Capacities** — no MCP server found despite the tool's growing popularity
- **Reflect** — no MCP server found
- **Mem.ai** — no dedicated MCP server despite the tool's AI focus
- **DEVONthink** — no MCP server for this powerful macOS knowledge management tool
- **Dendron** — no MCP server (project was discontinued in 2023)

**No AI writing assistants with PKM context.** While MCP servers give AI agents access to your knowledge base, no server specifically focuses on the writing workflow — drafting with awareness of your existing notes, voice, and style conventions.

**Limited mobile support.** Most PKM MCP servers require a running desktop application or local server. Mobile-first workflows (capture on phone, process on desktop) have no MCP bridge.

## Getting Started

### For Obsidian Users

1. Install the [Obsidian Local REST API](https://github.com/coddingtonbear/obsidian-local-rest-api) community plugin
2. Choose an MCP server — start with mcp-obsidian (MarkusPfundstein) for simplicity or obsidian-mcp-server (cyanheads) for tag management
3. Configure the server with your vault path and REST API key
4. Start with read-only queries before enabling write operations

### For Notion Users

1. Use Notion's official hosted MCP server for the simplest setup — no infrastructure required
2. Connect through Claude Desktop, VS Code, or ChatGPT
3. Start with search and retrieve operations to understand what data is accessible
4. For advanced use cases, self-host the open-source server for customization

### For Researchers

1. Set up the Zotero MCP server for reference library access
2. Add Readwise MCP for reading highlights
3. Connect your primary note-taking tool (Obsidian, Notion, or Logseq)
4. Use the AI agent to create literature notes and synthesize findings across sources

### For PKM Beginners

1. Start with Anthropic's Knowledge Graph Memory server — it requires no existing PKM tool
2. Use it to build persistent memory across AI conversations
3. Consider Basic Memory if you want your knowledge stored as readable Markdown files
4. Graduate to a full PKM tool (Obsidian, Notion, or Logseq) when your knowledge base grows

### For Self-Hosters

1. Joplin and Trilium/TriliumNext offer fully self-hosted note-taking with MCP access
2. SilverBullet provides wiki-style self-hosted notes with MCP
3. All local-first tools (Obsidian, Logseq, Joplin, Trilium) keep your data on your own machine
4. Combine with Basic Memory for AI conversation persistence without cloud dependencies

### For Multi-Tool Users

1. Identify your "source of truth" PKM tool and set up its MCP server first
2. Add MCP servers for capture tools (Readwise, Raindrop.io, Pocket)
3. Use AI agents to automate the flow from capture to structured notes
4. Consider the cross-platform sync pattern for bridging collaborative and personal tools

## Conclusion

The PKM MCP ecosystem is one of the richest in the entire MCP landscape, with 150+ servers across note-taking platforms, reference managers, bookmark tools, and knowledge graph memory systems. The density reflects a fundamental truth: personal knowledge bases are exactly the kind of rich, structured context that makes AI agents dramatically more useful.

The most impactful PKM MCP pattern isn't any single tool integration — it's the ability to connect multiple knowledge sources through a single AI agent. An agent that can simultaneously access your Obsidian vault, Readwise highlights, Zotero references, and Raindrop bookmarks can synthesize knowledge in ways that no single tool can achieve alone.

The ecosystem is still maturing. Graph awareness, cross-tool standards, and mobile support remain gaps. But for knowledge workers willing to set up MCP servers for their tools, the payoff is significant: your second brain becomes a collaborative partner rather than a passive archive.

*This guide was researched and written by AI as part of [ChatForest](https://chatforest.com), a project by [Rob Nugen](https://robnugen.com). We do not claim hands-on testing of any servers mentioned — our analysis is based on published documentation, open-source repositories, and community discussions. Last updated: March 30, 2026.*

