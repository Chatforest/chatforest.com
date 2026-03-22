---
title: "Library, Archive & Museum MCP Servers — Zotero, Calibre, Wayback Machine, and Museum Collections"
date: 2026-03-15T22:30:00+09:00
description: "Library, archive, and museum MCP servers let AI agents manage research libraries, search ebook collections, access archived websites, and explore museum art. We found 35+ servers across 5 subcategories. Reference Management: 54yyyu/zotero-mcp (1,800 stars, Python, MIT — 13+ tools, vector search, multi-embedding models), cookjohn/zotero-mcp (476 stars, TypeScript, MIT — 20 tools, Zotero plugin with write operations), 6 additional Zotero implementations. eBook Management: onebirdrocks/ebook-mcp (351 stars, Python, Apache 2.0 — EPUB + PDF, 10 tools for metadata, TOC, chapter extraction), trieloff/calibre-mcp (28 stars, Shell, Apache 2.0 — Calibre search with full-text and fuzzy matching), 5 additional Calibre implementations. Book Discovery: 8enSmith/mcp-open-library (62 stars, TypeScript, MIT — 6 tools for Internet Archive's Open Library API), juanbeniteza/mcp-google-books (Python, MIT — Google Books API). Internet Archive: Mearman/mcp-wayback-machine (17 stars, TypeScript — 4 tools, save/retrieve/search/status), sisilet/wayback-mcp (Python, MIT — CDX API + archive.org search). Museum Collections: r-huijts/rijksmuseum-mcp (65 stars, JavaScript/TypeScript, MIT — 7 tools with artist timelines and high-res images), mikechao/metmuseum-mcp (24 stars, TypeScript, MIT — 4 tools + interactive MCP App), molanojustin/smithsonian-mcp (8 stars, Python — 16 tools across all Smithsonian museums), mikechao/artic-mcp (TypeScript, MIT — Art Institute of Chicago, 6 tools + gallery generator), AlexLin1234/harvard-art-museums-mcp-server (Python, MIT — 224,000+ artworks). Gaps: no Library of Congress collections server, no Europeana or DPLA servers, no MARC/Dublin Core MCP servers, no ILS integrations. Rating: 3.5/5."
og_description: "Library, archive & museum MCP servers: zotero-mcp (1,800 stars, 13+ tools, vector search), ebook-mcp (351 stars, EPUB + PDF), calibre-mcp (28 stars, full-text search), mcp-open-library (62 stars, Open Library API), rijksmuseum-mcp (65 stars, 7 tools), metmuseum-mcp (24 stars, MCP App), smithsonian-mcp (16 tools), mcp-wayback-machine (17 stars). 35+ servers across 5 categories. Rating: 3.5/5."
content_type: "Review"
card_description: "Library, archive, and museum MCP servers for AI-powered research, reading, and cultural exploration — from managing Zotero citations to browsing the Smithsonian's 155 million objects. This category reveals a striking split: **reference management is mature** (Zotero alone has 8+ MCP implementations led by 54yyyu/zotero-mcp at 1,800 stars), while **traditional library systems have zero MCP presence**. No ILS vendor, no OPAC system, no cataloging standard has an MCP server. **Zotero dominates the category** with the highest-starred server (1,800 stars, MIT, 13+ tools including vector-based semantic search across your entire research library). The cookjohn/zotero-mcp plugin (476 stars, 20 tools) takes a different approach — running as a native Zotero plugin with Streamable HTTP, offering write operations for notes, tags, and metadata. With 8 independent implementations, Zotero is one of the most MCP-served applications in the entire ecosystem. **eBook management has two strong paths**: onebirdrocks/ebook-mcp (351 stars, Apache 2.0) handles EPUB and PDF files directly with chapter-level extraction, while 5+ Calibre servers bridge AI to the most popular ebook management application. trieloff/calibre-mcp (28 stars, Apache 2.0) is a pure bash implementation using calibredb with full-text search and fuzzy matching; sandraschi/calibremcp (21 tools) adds RAG and metadata indexing via LanceDB. **Book discovery spans multiple sources**: mcp-open-library (62 stars) connects to Internet Archive's Open Library API for books and authors, mcp-google-books provides Google Books search, and booklife-mcp (27 tools) unifies Hardcover, Libby/OverDrive, and Open Library into one reading assistant. **The Wayback Machine has dedicated MCP servers** — mcp-wayback-machine (17 stars) can save, retrieve, search, and check archive status without API keys, with built-in rate limiting. **Museum collections are surprisingly well-covered** — 5 major institutions have community-built MCP servers. The Rijksmuseum server (65 stars, 7 tools) is the most popular, with artist timeline generation and tile-based high-resolution image access. The Smithsonian server (16 tools) is the most comprehensive, spanning all 21 museums with on-view status checking and collection statistics. The Met Museum server features an interactive MCP App for browsing artworks directly in chat. **Major gaps remain**: no Library of Congress digital collections server (congress.gov API is legislative only), no Europeana or DPLA aggregator servers, no MARC/Dublin Core/Z39.50 bibliographic standard servers, no ILS (Koha, FOLIO, Alma) integrations, and no digital preservation servers. The category earns 3.5/5 — strong in personal research tools and museum exploration, absent from institutional library infrastructure."
last_refreshed: 2026-03-15
---

Library, archive, and museum MCP servers let AI assistants manage research citations, search ebook collections, retrieve archived web pages, and explore museum art. Instead of manually exporting Zotero bibliographies, navigating Calibre's interface, or browsing museum websites one artwork at a time, these servers let AI agents query your research library, extract ebook chapters, access historical snapshots of websites, and discover artworks across major museum collections — all through the Model Context Protocol.

This review covers the **library, archive, and museum** vertical — reference management (Zotero), ebook management (Calibre, EPUB/PDF), book discovery (Open Library, Google Books), web archiving (Wayback Machine), and museum collections (Rijksmuseum, Met, Smithsonian, Art Institute of Chicago, Harvard Art Museums). For academic paper search (arXiv, Semantic Scholar, PubMed), see our [Education & EdTech MCP review](/reviews/education-edtech-mcp-servers/). For government document access (Congress.gov, GovInfo), see our [Government & Public Sector MCP review](/reviews/government-public-sector-mcp-servers/).

The headline findings: **Zotero is the most MCP-served application in this category** with 8+ implementations led by 54yyyu/zotero-mcp (1,800 stars, 13+ tools with vector semantic search). **eBook management has two paths** — direct EPUB/PDF handling via ebook-mcp (351 stars) or Calibre library bridging via 5+ implementations. **Five major museums have community MCP servers** but no museum has built an official one. **Traditional library systems (ILS, OPAC, MARC) have zero MCP presence** — a significant gap given how many libraries exist worldwide.

## Reference Management (Zotero)

### 54yyyu/zotero-mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [54yyyu/zotero-mcp](https://github.com/54yyyu/zotero-mcp) | 1,800 | Python | MIT | 13+ |

The **most popular library MCP server by far** and one of the highest-starred MCP servers in any niche vertical. Connects your Zotero research library with AI assistants via the Zotero local API. Key capabilities:

- **Semantic search** — vector-based similarity search across your entire library with multiple embedding models (default free model, OpenAI, or Gemini)
- **Auto-updating database** — configurable sync schedules keep the search index current
- **Advanced search** — filter by collections, tags, authors, date ranges
- **Content extraction** — full-text retrieval, metadata access, and PDF annotation extraction including image annotations
- **Collection browsing** — navigate your library's organizational structure

The semantic search is the killer feature — instead of keyword matching, you can ask conceptual questions like "papers about transformer attention mechanisms" and get relevant results ranked by embedding similarity. The auto-sync means you don't need to manually rebuild the index after adding new papers.

### cookjohn/zotero-mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [cookjohn/zotero-mcp](https://github.com/cookjohn/zotero-mcp) | 476 | TypeScript | MIT | 20 |

Takes a fundamentally different architecture — runs as a **native Zotero plugin** rather than an external server. The plugin embeds an MCP server using Streamable HTTP protocol, so AI clients connect directly to Zotero. The 20 tools span four categories:

- **Search & Query** (7 tools) — library search, annotation search, full-text search, collection browsing, item details, abstracts, and content extraction with four detail levels (minimal/preview/standard/complete)
- **Collection Management** (4 tools) — collections, subcollections, collection items, and details
- **Semantic Search** (3 tools) — vector search with OpenAI or Ollama support, similarity matching, and index status
- **Write Operations** (4 tools) — create notes, add tags, update metadata, and write new items

The **write capability** is the key differentiator — 54yyyu's server is read-only, while cookjohn's can create notes, tag items, and update metadata directly in your Zotero library. The annotation system supports color and tag filtering. Includes a built-in client configuration generator.

### Additional Zotero Implementations

Six more Zotero MCP servers exist, each with a slightly different focus:

- **[swairshah/zotero-mcp-server](https://github.com/swairshah/zotero-mcp-server)** — exposes your local Zotero repository to MCP clients
- **[kujenga/zotero-mcp](https://github.com/kujenga/zotero-mcp)** — Python implementation using the Zotero API
- **[kaliaboi/mcp-zotero](https://github.com/kaliaboi/mcp-zotero)** — connector for Zotero Cloud collections and sources
- **[gyger/mcp-pyzotero](https://github.com/gyger/mcp-pyzotero)** — built on the pyzotero library for local Zotero integration
- **[masaki39/zotero-mcp](https://github.com/masaki39/zotero-mcp)** — integrates with Zotero's local API
- **[stephenstubbs/zotero-mcp](https://github.com/stephenstubbs/zotero-mcp)** — another Zotero integration

With 8 independent implementations, Zotero is one of the most MCP-served single applications in the entire ecosystem — rivaling even Slack and GitHub for community attention. The pattern is clear: researchers want their AI assistants to have direct access to their citation libraries.

## eBook Management

### onebirdrocks/ebook-mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [onebirdrocks/ebook-mcp](https://github.com/onebirdrocks/ebook-mcp) | 351 | Python | Apache 2.0 | 10 |

The **most popular ebook MCP server** — works directly with EPUB and PDF files without requiring any library management software. The 10 tools split across two format categories:

**EPUB tools:**
- `get_all_epub_files` — locate EPUB documents in specified directories
- `get_metadata` — extract publication info (title, author, publisher, language, ISBN)
- `get_toc` — retrieve table of contents structure
- `get_chapter_markdown` — convert chapter content to Markdown

**PDF tools:**
- `get_all_pdf_files` — discover PDF documents
- `get_pdf_metadata` — access document properties
- `get_pdf_toc` — extract outline and chapter structure
- `get_pdf_page_text` — retrieve plain text from specific pages
- `get_pdf_page_markdown` — convert pages to Markdown
- `get_pdf_chapter_content` — extract chapters by title with page references

The chapter-level extraction is the standout capability — instead of dumping an entire book into context, you can selectively pull specific chapters or pages. Uses ebooklib for EPUB, PyPDF2 and PyMuPDF for PDF, with BeautifulSoup and html2text for content conversion.

### trieloff/calibre-mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [trieloff/calibre-mcp](https://github.com/trieloff/calibre-mcp) | 28 | Shell | Apache 2.0 | 4 |

A **pure bash implementation** that uses the `calibredb` command-line interface — no Python or Node.js dependencies beyond Calibre itself. The four tools cover the essentials:

- **Full-text search** with automatic phrase matching and fuzzy fallback
- **Author search** with partial matching
- **Title search** with partial matching
- **Excerpt extraction** with keyword highlighting and pagination

Provides both Calibre deep links (`calibre://`) and file URLs (`file://`) for results. Includes timeout handling optimized for macOS. The bash-only approach makes it the simplest Calibre MCP server to install and understand.

### Additional Calibre Implementations

- **[sandraschi/calibremcp](https://github.com/sandraschi/calibremcp)** (Python, MIT, 21 tools) — the most feature-rich Calibre server with FastMCP, including RAG retrieval, LanceDB metadata indexing, natural language search, and agentic workflows
- **[ajtudela/calibre_mcp_server](https://github.com/ajtudela/calibre_mcp_server)** (Python) — search and retrieve book metadata through MCP
- **[ispyridis/calibre-mcp-nodejs](https://github.com/ispyridis/calibre-mcp-nodejs)** (Node.js) — supports EPUB, PDF, MOBI, AZW/AZW3, TXT, HTML and more formats
- **[THeK3nger/calibre-mcp](https://github.com/THeK3nger/calibre-mcp)** — queries Calibre via the Content Server, with full-text search and metadata retrieval
- **[pshap/mcp-neolibrarian](https://github.com/pshap/mcp-neolibrarian)** (Python, MIT, 14 tools) — read-only server with unified search, batch operations, content analysis, and FTS statistics

## Book Discovery

### 8enSmith/mcp-open-library

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [8enSmith/mcp-open-library](https://github.com/8enSmith/mcp-open-library) | 62 | TypeScript | MIT | 6 |

Connects to the **Internet Archive's Open Library API** — the largest open book database with records for over 20 million editions. The 6 tools cover:

- **Book search by title** — find books with metadata
- **Author search by name** — locate authors
- **Author info** — detailed author data via Open Library key
- **Author photo** — photo URLs via OLID
- **Book cover** — cover image URLs from ISBN, LCCN, OCLC, or OLID
- **Book by ID** — comprehensive details from multiple identifier types

No API key required — Open Library's API is free and open. A solid choice for book metadata enrichment, reading list creation, or bibliographic research.

### Additional Book Discovery Servers

- **[juanbeniteza/mcp-google-books](https://github.com/juanbeniteza/mcp-google-books)** (Python, MIT, 2 tools) — book and author search via Google Books API
- **[andylbrummer/booklife-mcp](https://github.com/andylbrummer/booklife-mcp)** (Go, 27 tools) — unifies **Hardcover** (reading tracker), **Libby/OverDrive** (library borrowing), and **Open Library** (metadata) into one reading assistant with a unified TBR list, reading history, and recommendations
- **[CodeDreamer06/BookDownloaderMCP](https://github.com/CodeDreamer06/BookDownloaderMCP)** (TypeScript) — search and download ebooks from LibGen mirrors with smart mirror discovery and failover

## Internet Archive & Wayback Machine

### Mearman/mcp-wayback-machine

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [Mearman/mcp-wayback-machine](https://github.com/Mearman/mcp-wayback-machine) | 17 | TypeScript | CC BY-NC-SA 4.0 | 4 |

An MCP server **and** CLI tool for the Wayback Machine — no API keys required. The 4 tools:

- **save_url** — archive a URL to the Wayback Machine, returns archived URL with timestamp
- **get_archived_url** — retrieve an archived version by URL and optional timestamp
- **search_archives** — query all available snapshots with date range filtering
- **check_archive_status** — archival statistics including first/last capture, total captures, and yearly breakdown

Built-in rate limiting at 15 requests per minute protects against API abuse. Works as both an MCP server for AI clients and a standalone CLI tool. The **CC BY-NC-SA license** is worth noting — it restricts commercial use, which may matter for some deployments.

### sisilet/wayback-mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [sisilet/wayback-mcp](https://github.com/sisilet/wayback-mcp) | 2 | Python | MIT | 3 |

A simpler alternative with MIT licensing. Uses the CDX API for snapshot retrieval and adds **archive.org item search** beyond just the Wayback Machine. Provides a `wayback://{url}/{timestamp}` resource protocol for direct access to archived content.

## Museum & Cultural Heritage Collections

### r-huijts/rijksmuseum-mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [r-huijts/rijksmuseum-mcp](https://github.com/r-huijts/rijksmuseum-mcp) | 65 | JavaScript/TypeScript | MIT | 7 |

The **most popular museum MCP server**. Provides access to the Rijksmuseum's collection through 7 tools:

- **search_artwork** — find artworks by text, artist, type, materials, periods, and colors
- **get_artwork_details** — comprehensive info including provenance and exhibition history
- **get_artwork_image** — high-resolution images with tile-based loading and multiple zoom levels
- **get_user_sets** — browse user-created collections and thematic groupings
- **get_user_set_details** — detailed info about curated sets
- **open_image_in_browser** — display artwork images for detailed viewing
- **get_artist_timeline** — chronological timeline of an artist's works tracking style evolution

The **artist timeline** and **tile-based image loading** are unique features not found in other museum MCP servers. Requires a Rijksmuseum API key (free to obtain).

### mikechao/metmuseum-mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [mikechao/metmuseum-mcp](https://github.com/mikechao/metmuseum-mcp) | 24 | TypeScript | MIT | 4 |

Access to The Metropolitan Museum of Art's collection with an **interactive MCP App** — a browsable art explorer that runs directly within MCP-compatible clients. The 4 tools:

- **list-departments** — all departments at The Met
- **search-museum-objects** — collection search with filters for images, departments, and pagination
- **get-museum-object** — detailed artwork info with optional base64-encoded images
- **open-met-explorer** — launches the interactive browsing application

The MCP App (`ui://met/explorer.html`) for in-chat browsing is the standout feature. Uses The Met's free public API — no key required.

### molanojustin/smithsonian-mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [molanojustin/smithsonian-mcp](https://github.com/molanojustin/smithsonian-mcp) | 8 | Python | — | 16 |

The **most comprehensive museum MCP server** with 16 tools spanning all 21 Smithsonian museums and their combined 155+ million objects. Organized into two categories:

**Search & Discovery** (11 tools) — smart sampling across museums, advanced filtering, museum-specific queries, on-view status checking, and object type browsing.

**Information & Context** (5 tools) — museum directory, collection statistics with per-museum breakdowns, and context retrieval for search results and objects.

The `get_objects_on_view` tool is unique — it can tell you what's currently exhibited in any Smithsonian museum, useful for trip planning or identifying objects you can actually go see.

### Additional Museum Servers

- **[mikechao/artic-mcp](https://github.com/mikechao/artic-mcp)** (TypeScript, MIT, 6 tools) — Art Institute of Chicago collection with full-text search, artist browsing, and an **art gallery prompt** that generates interactive HTML galleries
- **[AlexLin1234/harvard-art-museums-mcp-server](https://github.com/AlexLin1234/harvard-art-museums-mcp-server)** (Python, MIT, 5 tools) — access to 224,000+ artworks, artists, and museum objects with random artwork discovery

Five world-class museums now have community-built MCP servers. None has built an official one, but the community coverage is solid — these are all free public APIs wrapped in clean MCP interfaces.

## What's missing

The gaps in this category are significant:

- **No Library of Congress digital collections MCP** — congress.gov API covers legislative data only, not the LC's vast digital collections (prints, photographs, maps, manuscripts, recordings)
- **No Europeana or DPLA servers** — the two largest digital cultural heritage aggregators (60+ million items combined) have public APIs but no MCP servers
- **No MARC, Dublin Core, or Z39.50 servers** — zero MCP presence for bibliographic cataloging standards
- **No ILS integrations** — Koha, FOLIO, Alma, Sierra, and other library management systems have no MCP servers
- **No digital preservation servers** — no integration with preservation platforms like Archivematica, DSpace, or Fedora
- **No public library catalog access** — no way for an AI agent to search a local public library's collection via MCP

The absence of institutional library infrastructure MCP servers is the category's biggest gap. Libraries serve hundreds of millions of people worldwide, but the MCP ecosystem has focused entirely on personal tools (Zotero for researchers, Calibre for readers) rather than institutional systems.

## Bottom line

The library, archive, and museum MCP category earns **3.5/5**. It's deep where individuals need it — Zotero's 8 implementations and 1,800-star lead server rival the best-served applications in the entire MCP ecosystem, and Calibre's 5+ servers cover ebook management thoroughly. Museum collections have surprisingly good coverage across 5 major institutions. But the category completely lacks institutional library infrastructure — no ILS, no cataloging standards, no public library access, no major digital heritage aggregators. If you're a researcher with a Zotero library or a reader with a Calibre collection, you're well-served. If you work in library science or cultural heritage at an institutional level, MCP hasn't arrived yet.

*This review was last edited on 2026-03-16 using Claude Opus 4.6 (Anthropic).*
