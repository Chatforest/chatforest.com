---
title: "Library, Archive & Museum MCP Servers — Zotero, Calibre, IIIF, Wayback Machine, and Museum Collections"
date: 2026-03-15T22:30:00+09:00
lastmod: 2026-06-12T00:00:00+09:00
description: "Library, archive, and museum MCP servers let AI agents manage research libraries, search ebook collections, access archived websites, and explore museum art."
og_description: "Library, archive & museum MCP servers: zotero-mcp (2,700+ stars, NOW WITH WRITE OPS — create/update items, DOI import, collections), Xevos117/mcp-zotero (NEW — Unpaywall OA PDF discovery, citation injection into Word docs), cookjohn/zotero-mcp (~737 stars, plugin, v1.4.7), ebook-mcp (Apache 2.0, EPUB+PDF), open-museum-mcp (NEW — federated Met+Cleveland+AIC+Europeana, license-verified), IIIF_MCP (20+ tools, 2026 conference growing adoption), rijksmuseum-mcp (67 stars), smithsonian-mcp (16 tools), anna's archive MCP (multiple servers). 50+ servers across 7 categories. Rating: 3.5/5."
content_type: "Review"
card_description: "Library, archive, and museum MCP servers for AI-powered research, reading, and cultural exploration — from managing Zotero citations to browsing federated museum collections. The biggest development this cycle: **54yyyu/zotero-mcp gained write operations** — it was read-only since launch, now adding create_item, update_item, add_by_doi, add_by_url, create_collection, and more. Combined with cookjohn's plugin (v1.4.7, ~737 stars) and the new **Xevos117/mcp-zotero** (DOI import, Unpaywall open-access PDF discovery, citation injection into Word .docx files), Zotero's MCP ecosystem has grown from a read-mostly research tool to a full research workflow platform. **NEW: cfpramod/open-museum-mcp** brings federated, license-verified museum search across The Met, Cleveland Museum of Art, Art Institute of Chicago, Wikimedia Commons, and opt-in Europeana — with dynasty-aware date parsing and strict rights verification (nothing defaulted to 'open'). **Anna's Archive now has multiple MCP servers** including iosifache/annas-mcp (CLI+server), RemiKalbe/annas-archive-mcp (Rust), and oatsvine/annas-archive-toolchain-mcp (Playwright-powered + RAG-ready). **IIIF momentum building**: the 2026 Annual Conference concluded June 1–4 in the Netherlands with growing institutional adoption; TU Delft Library joined the IIIF Consortium as a full member. Traditional library systems (ILS, MARC, OPAC) still have zero MCP presence. Rating: 3.5/5."
last_refreshed: 2026-06-12
---

Library, archive, and museum MCP servers let AI assistants manage research citations, search ebook collections, retrieve archived web pages, and explore museum art. Instead of manually exporting Zotero bibliographies, navigating Calibre's interface, or browsing museum websites one artwork at a time, these servers let AI agents query your research library, extract ebook chapters, access historical snapshots of websites, and discover artworks across major museum collections — all through the Model Context Protocol.

This review covers the **library, archive, and museum** vertical — reference management (Zotero), ebook management (Calibre, EPUB/PDF), book discovery (Open Library, Google Books), web archiving (Wayback Machine), digital archive standards (IIIF), and museum collections (Rijksmuseum, Met, Smithsonian, Art Institute of Chicago, Harvard Art Museums, Cooper Hewitt). For academic paper search (arXiv, Semantic Scholar, PubMed), see our [Education & EdTech MCP review](/reviews/education-edtech-mcp-servers/). For government document access (Congress.gov, GovInfo), see our [Government & Public Sector MCP review](/reviews/government-public-sector-mcp-servers/).

The headline findings: **54yyyu/zotero-mcp gained write operations** — the leading Zotero server was read-only at launch and now supports creating and updating items, adding by DOI or URL, collection management, and more, completing its transformation into a full research workflow tool. **NEW: Xevos117/mcp-zotero** adds Unpaywall integration for automatic open-access PDF discovery and a unique citation injection feature — LLMs can generate Word .docx files with native Zotero field codes already embedded. **NEW: cfpramod/open-museum-mcp** provides federated license-verified search across five museum collections with strict rights verification and dynasty-aware date parsing. **Anna's Archive has multiple MCP servers** enabling search and retrieval from the largest shadow library. **IIIF momentum building**: the 2026 Annual Conference concluded June 1–4 in the Netherlands with growing institutional adoption; TU Delft Library joined the IIIF Consortium as a full member. **Traditional library systems (ILS, OPAC, MARC) still have zero MCP presence** — a significant gap given how many libraries exist worldwide.

**Category:** [Education & Learning](/categories/education-learning/)

## Reference Management (Zotero)

### 54yyyu/zotero-mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [54yyyu/zotero-mcp](https://github.com/54yyyu/zotero-mcp) | 2,700 | Python | MIT | 13+ |

The **most popular library MCP server by far** and one of the highest-starred MCP servers in any niche vertical. Connects your Zotero research library with AI assistants via the Zotero local API. Key capabilities:

- **Semantic search** — vector-based similarity search across your entire library with multiple embedding models (default free model, OpenAI, or Gemini)
- **Auto-updating database** — configurable sync schedules keep the search index current
- **Advanced search** — filter by collections, tags, authors, date ranges
- **Content extraction** — full-text retrieval, metadata access, and PDF annotation extraction including image annotations
- **Collection browsing** — navigate your library's organizational structure
- **Write operations (new)** — create_item, update_item, create_note, add_tags, batch_update_tags, create_collection, add_to_collection, remove_from_collection, add_by_doi, add_by_url, add_from_file

The semantic search is the killer feature — instead of keyword matching, you can ask conceptual questions like "papers about transformer attention mechanisms" and get relevant results ranked by embedding similarity. The auto-sync means you don't need to manually rebuild the index after adding new papers. The addition of write operations is significant: this server was read-only since launch. It can now build your library as well as query it.

### cookjohn/zotero-mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [cookjohn/zotero-mcp](https://github.com/cookjohn/zotero-mcp) | ~737 | TypeScript | MIT | 20 |

Takes a fundamentally different architecture — runs as a **native Zotero plugin** rather than an external server. The plugin embeds an MCP server using Streamable HTTP protocol, so AI clients connect directly to Zotero. The 20 tools span four categories:

- **Search & Query** (7 tools) — library search, annotation search, full-text search, collection browsing, item details, abstracts, and content extraction with four detail levels (minimal/preview/standard/complete)
- **Collection Management** (4 tools) — collections, subcollections, collection items, and details
- **Semantic Search** (3 tools) — vector search with OpenAI or Ollama support, similarity matching, and index status
- **Write Operations** (4 tools) — create notes, add tags, update metadata, and write new items

The **write capability** is the key differentiator — 54yyyu's server is read-only, while cookjohn's can create notes, tag items, and update metadata directly in your Zotero library. The annotation system supports color and tag filtering. Includes a built-in client configuration generator.

### TonybotNi/ZotLink — Preprint Saving to Zotero

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [TonybotNi/ZotLink](https://github.com/TonybotNi/ZotLink) | 134 | Python | MIT | 5 |

A **production-ready MCP server for saving open preprints** to Zotero with rich metadata and smart PDF attachments. Covers arXiv, CVF OpenAccess, bioRxiv, medRxiv, and chemRxiv — with publisher databases (Nature, Science, IEEE Xplore, Springer) planned. The 5 tools:

- **check_zotero_status** — verify Zotero connection
- **get_zotero_collections** — browse library structure
- **save_paper_to_zotero** — save with full metadata extraction
- **extract_arxiv_metadata** — pull metadata from arXiv papers

At 134 stars, ZotLink is the third most popular Zotero MCP server. Its focus on preprint ingestion complements the broader library access of 54yyyu and cookjohn's implementations — where those servers help you *read* your library, ZotLink helps you *build* it.

### Xevos117/mcp-zotero — Citation Injection into Word Documents

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [Xevos117/mcp-zotero](https://github.com/Xevos117/mcp-zotero) | — | TypeScript | MIT | 15 |

A specialized Zotero MCP server focused on the **full research-to-document workflow** — from finding papers to producing a cited Word document. The 15 tools cover searching, browsing, collection management, and — uniquely — citation injection:

- **add_by_doi** — import papers by DOI with automatic metadata resolution and auto-attached open-access PDFs via **Unpaywall**
- **import_pdf** — ingest local PDFs with Zotero's own metadata recognizer
- **inject_citations_into_docx** — generate Word `.docx` files with **native Zotero field codes** already embedded, so opening in Word and clicking Zotero → Refresh produces fully managed citations in APA, IEEE, Vancouver, Harvard, or Chicago styles

The Unpaywall integration is the standout feature — when you add a paper by DOI, the server automatically checks Unpaywall for a legal open-access version and attaches the PDF without manual searching. The citation injection capability means an LLM can produce a complete research document where citation management is handled by Zotero rather than plain text, enabling proper bibliography updates as you revise. Available via `npx @xevos117/mcp-zotero`.

### Additional Zotero Implementations

More Zotero MCP servers exist, each with a slightly different focus:

- **[kujenga/zotero-mcp](https://github.com/kujenga/zotero-mcp)** (138 stars) — streamlined Python implementation using the Zotero API
- **[swairshah/zotero-mcp-server](https://github.com/swairshah/zotero-mcp-server)** — exposes your local Zotero repository with dual modes (Web API or direct SQLite)
- **[kaliaboi/mcp-zotero](https://github.com/kaliaboi/mcp-zotero)** — connector for Zotero Cloud collections and sources
- **[masaki39/zotero-mcp](https://github.com/masaki39/zotero-mcp)** — integrates with Zotero's local API
- **[PiaoyangGuohai1/cli-anything-zotero](https://github.com/PiaoyangGuohai1/cli-anything-zotero)** — 52 MCP tools + 70+ CLI commands via a lightweight Zotero-JS-Bridge plugin; **note: MCP support is frozen at v0.9.5** — from v1.0.0 onwards, the project pivots to a CLI/SDK-first model and no longer provides the `zotero-mcp` command
- **[ehawkin/zotero-mcp-setup](https://github.com/ehawkin/zotero-mcp-setup)** — not a server itself but an easy-install helper with macOS GUI installer (DMG) and one-click scripts for Mac/Windows

With 12+ independent implementations, Zotero is one of the most MCP-served single applications in the entire ecosystem — rivaling even Slack and GitHub for community attention. The ecosystem has matured from read-only research tools to full workflow platforms with write operations, DOI import, and document generation.

## eBook Management

### onebirdrocks/ebook-mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [onebirdrocks/ebook-mcp](https://github.com/onebirdrocks/ebook-mcp) | 361 | Python | Apache 2.0 | 10 |

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
- **[benoute/calibre-mcp](https://github.com/benoute/calibre-mcp)** (Python) — access to a local Calibre library with search and retrieval

## Book Discovery

### 8enSmith/mcp-open-library

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [8enSmith/mcp-open-library](https://github.com/8enSmith/mcp-open-library) | 70 | TypeScript | MIT | 6 |

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
| [Mearman/mcp-wayback-machine](https://github.com/Mearman/mcp-wayback-machine) | 21 | TypeScript | CC BY-NC-SA 4.0 | 4 |

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

## Shadow Libraries (Anna's Archive)

Anna's Archive is a search engine for shadow libraries — indexing millions of books, papers, and documents from Z-Library, Sci-Hub, Library Genesis, and other sources. It has attracted multiple MCP server implementations.

**Legal note:** Anna's Archive and the libraries it indexes operate outside copyright law in most jurisdictions. These MCP servers are tools for accessing copyrighted content without authorization. Inclusion here is for completeness — use is subject to the copyright laws of your country.

- **[iosifache/annas-mcp](https://github.com/iosifache/annas-mcp)** (Python, MIT) — MCP server and CLI tool for searching and downloading documents from Anna's Archive; last updated February 2026
- **[RemiKalbe/annas-archive-mcp](https://github.com/RemiKalbe/annas-archive-mcp)** (Rust, Cargo) — Rust-based server for searching books, papers, magazines, and comics
- **[oatsvine/annas-archive-toolchain-mcp](https://github.com/oatsvine/annas-archive-toolchain-mcp)** — the most capable implementation: Playwright-powered search, fast MD5-based downloads, Markdown normalization, and semantic search over retrieved EPUB/PDF/MOBI content (RAG-ready)
- **[ball2jh/annas-archive-mcp](https://github.com/ball2jh/annas-archive-mcp)** (Go) — optimized for Claude Code and other MCP-compatible clients with DOI resolution

## Digital Archive Standards (IIIF)

### code4history/IIIF_MCP — Universal Cultural Heritage Access

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [code4history/IIIF_MCP](https://github.com/code4history/IIIF_MCP) | 1 | JavaScript | — | 20+ |

The **first MCP bridge to the IIIF ecosystem** — and potentially the most impactful server in this entire category. IIIF (International Image Interoperability Framework) is the universal standard used by thousands of cultural institutions worldwide — the Library of Congress, British Library, Bibliothèque nationale de France, Harvard, Stanford, the Vatican Library, and thousands more publish their digitized collections through IIIF APIs. This single MCP server can access them all.

The 20+ tools span the full IIIF specification:

- **Content Search** — full-text search within IIIF documents (manuscripts, books, newspapers)
- **Metadata Retrieval** — structured metadata from IIIF manifests and collections
- **Image Operations** — region, size, rotation, and quality parameters per the IIIF Image API
- **Collection Navigation** — browse hierarchical collection structures
- **Annotation Management** — read and manage annotations on digitized content
- **Activity Streams** — track changes and updates across collections
- **Authentication** — handle IIIF Auth flows for restricted content
- **Audio/Video** — support for time-based media resources (IIIF Presentation API 3.0)

The standout capability is **universality** — rather than building a separate MCP server for each museum or library (as the museum servers below do), IIIF_MCP works with any IIIF-compliant institution. The v1.1.0 release added image data fetching and canvas operations. Available as a single-file bundle for easy deployment.

The star count is low (1 star) but this is a genuinely important bridge — IIIF covers more cultural heritage content than all the museum-specific MCP servers combined. Context: the 2026 IIIF Annual Conference concluded June 1–4 in the Netherlands (Amsterdam, Leiden, The Hague), with growing institutional engagement from libraries, archives, and museums. TU Delft Library joined the IIIF Consortium as a full member in 2026. As more institutions adopt IIIF, the value of a single protocol-level MCP bridge grows proportionally.

## Museum & Cultural Heritage Collections

### r-huijts/rijksmuseum-mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [r-huijts/rijksmuseum-mcp](https://github.com/r-huijts/rijksmuseum-mcp) | 67 | JavaScript/TypeScript | MIT | 7 |

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
| [mikechao/metmuseum-mcp](https://github.com/mikechao/metmuseum-mcp) | 26 | TypeScript | MIT | 4 |

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

### cfpramod/open-museum-mcp — Federated Multi-Museum Search

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [cfpramod/open-museum-mcp](https://github.com/cfpramod/open-museum-mcp) | — | Python | MIT | — |

A **NEW** MCP server that treats multiple museum collections as a unified, searchable corpus with strict license verification built in. Where the individual museum servers above each cover one institution, open-museum-mcp federates across:

- **The Metropolitan Museum of Art** — live
- **Cleveland Museum of Art** — live
- **Art Institute of Chicago** — live
- **Wikimedia Commons** — live
- **Europeana** — opt-in via API key (federated European institutions)
- Smithsonian and Rijksmuseum direct integrations — coming

The standout design decision is **rights-first**: records are validated against per-museum rights rules in code, missing or unclear license indicators drop the record rather than defaulting to "open." Pre-formatted attributions separate named artists from anonymous, workshop, "after," and "attributed to" works. The **dynasty-aware date parser** handles Tang, Edo, Safavid, Mughal, and other dynastic dating systems that trip up conventional date parsing.

This makes it particularly useful for researchers, educators, and writers who need reuse-safe artwork — one query across five collection systems, with guaranteed license compliance.

### Additional Museum Servers

- **[mikechao/artic-mcp](https://github.com/mikechao/artic-mcp)** (TypeScript, MIT, 7 tools) — Art Institute of Chicago collection with full-text search, artist browsing, medium search, and an **art gallery prompt** that generates interactive HTML galleries
- **[AlexLin1234/harvard-art-museums-mcp-server](https://github.com/AlexLin1234/harvard-art-museums-mcp-server)** (Python, MIT, 5 tools) — access to 224,000+ artworks, artists, and museum objects with random artwork discovery
- **[behole/cooper-hewitt-mcp](https://github.com/behole/cooper-hewitt-mcp)** (TypeScript, MIT, 2 tools) — Cooper Hewitt, Smithsonian Design Museum collection access with object search and detailed retrieval — the first design-focused museum MCP server

Six world-class museums now have dedicated community-built MCP servers, and **open-museum-mcp** adds federated multi-institution search on top. None has built an official server, but community coverage now spans individual institution access (Rijksmuseum, Met, Smithsonian, AIC, Harvard, Cooper Hewitt) plus federated cross-collection search. Combined with the IIIF MCP server above, AI agents can access museum-specific collections, federated search, and the broader universe of IIIF-compliant digital archives.

## What's missing

The gaps in this category are still significant, though narrowing:

- **No Library of Congress digital collections MCP** — congress.gov API covers legislative data only, not the LC's vast digital collections (prints, photographs, maps, manuscripts, recordings). The IIIF MCP server can theoretically access LC's IIIF endpoints, but no dedicated server exists
- **No DPLA server** — the Digital Public Library of America (60+ million items) has a public API but no MCP server; Europeana is now partially addressed via open-museum-mcp's opt-in integration
- **No MARC, Dublin Core, or Z39.50 servers** — zero MCP presence for bibliographic cataloging standards
- **No ILS integrations** — Koha, FOLIO, Alma, Sierra, and other library management systems have no MCP servers
- **No digital preservation servers** — no integration with preservation platforms like Archivematica, DSpace, or Fedora
- **No public library catalog access** — no way for an AI agent to search a local public library's collection via MCP

The IIIF MCP server is a significant step toward bridging the institutional gap — it provides a universal protocol layer that works with thousands of institutions. But it's a low-level tool (you need to know IIIF manifest URLs) rather than a discovery layer. The cfpramod/open-museum-mcp partially addresses aggregator-level search across open-access collections, but the absence of institutional library infrastructure MCP servers remains the category's biggest gap.

## Bottom line

The library, archive, and museum MCP category earns **3.5/5**. The personal research tier has deepened materially: 54yyyu/zotero-mcp gained write operations, Xevos117/mcp-zotero adds Unpaywall-powered PDF discovery and Word citation injection, and 12+ Zotero implementations now cover the full research lifecycle from library building to document production. Museum access expanded with cfpramod/open-museum-mcp's federated, license-verified search across five collections. Anna's Archive has multiple MCP servers for those who need them. IIIF institutional adoption is growing — the 2026 conference showed libraries, archives, and museums actively building IIIF compliance, which means the protocol-level IIIF MCP server's value grows with every new institution. But the category still lacks institutional library infrastructure — no ILS, no cataloging standards, no public library access. If you're a researcher with a Zotero library or a reader with a Calibre collection, you're very well-served. If you work in library science or cultural heritage at an institutional level, IIIF_MCP and open-museum-mcp are meaningful progress but MCP hasn't fully arrived in that space yet.

*This review was last refreshed on 2026-06-12 using Claude Sonnet 4.6 (Anthropic).*
