# Publishing & Typesetting MCP Servers — LaTeX, Overleaf, Pandoc, eBooks, Print-on-Demand, InDesign, and More

> Publishing and typesetting MCP servers let AI agents compile LaTeX documents, convert between document formats, manage eBook libraries, create print-on-demand products, and


Publishing and typesetting MCP servers give AI agents the ability to compile LaTeX documents, convert between dozens of document formats, manage eBook libraries, create print-on-demand products, and automate desktop publishing workflows through natural language. Instead of wrestling with LaTeX syntax, configuring Pandoc command-line flags, or navigating InDesign's menus, an AI agent can handle it conversationally: "Take my Markdown draft, convert it to a professionally formatted PDF with proper typography, then prepare an EPUB version for distribution."

This review covers the **publishing and typesetting** vertical — LaTeX compilation, document format conversion, eBook management, book discovery, print-on-demand, desktop publishing, and PDF tools. For content management systems (WordPress, Ghost, Substack), see our [CMS & Content Management MCP review](/reviews/cms-content-management-mcp-servers/). For audio/video processing, see our [Audio & Video Processing MCP review](/reviews/audio-video-processing-mcp-servers/). For PDF reading/extraction specifically, see our [PDF & Document MCP review](/reviews/pdf-document-mcp-servers/).

The landscape spans eight areas: **LaTeX, Overleaf & Typst** (academic typesetting, Overleaf project integration, arXiv paper access, Typst conversion), **document format conversion** (Pandoc, Markdown-to-PDF, universal-to-Markdown), **eBooks & reading** (EPUB/PDF reading, Calibre library management, Apple Books highlights), **book discovery & metadata** (Open Library, Google Books), **print-on-demand** (Printify, Lulu Print), **desktop publishing** (Adobe InDesign, Affinity, Canva), and **PDF tools** (merge, extract, manipulate).

The headline findings: **Document conversion remains the strongest subcategory** — markdownify-mcp (2,600 stars, v1.0.4) is the single most popular server in this review. **Two major gaps from the initial review have been filled** — Typst (johannesbrandenburger/typst-mcp, 144 stars) and Affinity Publisher (tacyan/AffinityMCP, 18 stars, Rust) were both explicitly called out as missing and now have functional MCP servers. **OverleafMCP surged** 73→110 stars (+51%) while the Overleaf space expanded further to 7+ implementations. **Apple Books MCP got a significant update** (v0.7.3) with chapter position tracking, highlight context anchors, and reading analytics. **eBook management remains mature** — ebook-mcp (361 stars) continues to grow. **Desktop publishing diversified** beyond Adobe-only with the Affinity MCP server, though still macOS-primary.

**Category:** [Design & Creative](/categories/design-creative/)

---

## LaTeX, Overleaf & Typst

### OverleafMCP (Read-Only)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [mjyoo2/OverleafMCP](https://github.com/mjyoo2/OverleafMCP) | 110 | JavaScript | MIT | 6 |

The **most established Overleaf integration**, providing read-only access to Overleaf projects through Git:

- **list_projects** — enumerate all Overleaf projects linked to the user's account
- **list_files** — browse files within a specific project
- **read_file** — retrieve the contents of any LaTeX file
- **get_sections** — parse LaTeX document structure into section headings
- **get_section_content** — extract content from specific sections by title
- **status_summary** — overview of project state

Requires an Overleaf account with Git access (premium feature). Connects through Git rather than Overleaf's API, which means it works with self-hosted Overleaf instances too. Multiple projects can be managed simultaneously.

### OverleafMCP-rw (Read/Write)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [hiufungleung/overleafMCP-rw](https://github.com/hiufungleung/overleafMCP-rw) | 2 | JavaScript | MIT | 11 |

Extends the read-only OverleafMCP with **full write capabilities** via Git workflow:

All 6 read tools from OverleafMCP, plus:
- **write_file** — create or modify LaTeX files in the project
- **delete_file** — remove files from the project
- **commit_changes** — commit modifications with custom messages
- **push_changes** — push commits back to Overleaf
- **git_status** — check repository status before committing

This is the only Overleaf MCP server that enables AI agents to actually edit documents and push changes back, making it suitable for AI-assisted academic writing workflows.

### Other Overleaf Implementations

| Server | Stars | Language | Notes |
|--------|-------|----------|-------|
| [YounesBensafia/overleaf-mcp-server](https://github.com/YounesBensafia/overleaf-mcp-server) | 26 | Python | **NEW** (March 2026). MIT. 4 tools: list, read, write, sync. Read/write with Git sync |
| [gswxp2/overleaf-mcp-helper](https://github.com/gswxp2/overleaf-mcp-helper) | 2 | JS/TS | **NEW** (March 2026). MIT. VSCode plugin + MCP. Safe editing with substring matching, regex search, compile log parsing. No full-file overwrites |
| [GhoshSrinjoy/Overleaf-mcp](https://github.com/GhoshSrinjoy/Overleaf-mcp) | — | — | Read/analyze LaTeX files |
| [unnipv/overleaf-mcp](https://github.com/unnipv/overleaf-mcp) | — | — | AI-assisted LaTeX editing |
| [M-H-Amini/Overleaf-MCP-Server](https://github.com/M-H-Amini/Overleaf-MCP-Server) | — | — | Another Overleaf integration |

The Overleaf MCP space has grown to at least **7 implementations** with varying levels of maturity. YounesBensafia's server (26 stars) stands out among the newer entries for its clean read/write/sync workflow, while gswxp2's overleaf-mcp-helper takes a safety-first approach with substring editing (no full-file overwrites) and leverages Overleaf's built-in version history as a recovery mechanism.

### TeXFlow

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [aaronsb/texflow-mcp](https://github.com/aaronsb/texflow-mcp) | 22 | Python | MIT | 6 |

A **structured document authoring system** that takes a fundamentally different approach from other LaTeX servers — AI agents work with a semantic document model (sections, paragraphs, figures, tables) while TeXFlow handles all LaTeX mechanics:

- **document** — scaffold new documents or ingest existing Markdown
- **layout** — configure page layout, fonts, and formatting
- **edit** — modify document elements at the structural level
- **render** — compile to PDF, PNG page previews, or .tex export
- **reference** — searchable LaTeX commands, symbols, packages, and error documentation
- **queue** — batch multiple operations in a single call

Key design decision: the document auto-saves as JSON, and LaTeX is only ever an output artifact. This means AI agents never need to understand LaTeX syntax — they work in a structured model and get professionally typeset output. Supports PDF compilation, PNG page previews, and raw .tex export.

### TeXstudio LaTeX MCP Server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [axiomlogicnexus/TeXstudio-LaTeX-MCP-Server](https://github.com/axiomlogicnexus/TeXstudio-LaTeX-MCP-Server) | 1 | TypeScript | MIT | 30+ |

The **deepest LaTeX IDE integration**, connecting to TeXstudio with a full toolchain:

- **Editor integration** — launch TeXstudio at specific file positions with session management
- **Compilation** — latexmk-based PDF generation with engine fallbacks and Perl diagnostics
- **Code quality** — linting via chktex and formatting using latexindent
- **Project intelligence** — root document detection, dependency graphing, out-of-date analysis
- **Bibliography management** — automated biber/bibtex processing
- **PDF tools** — optimization and metadata inspection
- **Package management** — discover and install LaTeX packages
- **Container support** — optional Docker-based compilation workflows

Cross-platform (Windows, macOS, Linux) with path containment security and shell-escape policies. Despite low star count, the tool coverage is remarkably comprehensive — more LaTeX toolchain features than any other server in this review.

### Other LaTeX Servers

| Server | Stars | Language | License | Tools | Notes |
|--------|-------|----------|---------|-------|-------|
| [RobertoDure/mcp-latex-server](https://github.com/RobertoDure/mcp-latex-server) | 6 | Python | — | 6 | Create/edit/validate LaTeX with templates |
| [Yeok-c/latex-mcp-server](https://github.com/Yeok-c/latex-mcp-server) | — | — | — | — | pdflatex/xelatex compilation via latexmk |
| [TheTailorRetailored/latex-mcp](https://github.com/TheTailorRetailored/latex-mcp) | — | — | — | — | Secure compilation with template management |

### arXiv LaTeX MCP

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [takashiishida/arxiv-latex-mcp](https://github.com/takashiishida/arxiv-latex-mcp) | 127 | Python | MIT | 4 |

A **critical academic publishing tool** that fetches arXiv paper LaTeX source code directly — far more useful than PDF extraction for math-heavy papers where equation rendering matters:

- **get_paper_prompt** — retrieve full flattened LaTeX source for a paper
- **get_paper_abstract** — extract just the abstract
- **list_paper_sections** — enumerate section headings
- **get_paper_section** — extract a specific section's content

Particularly valuable for computer science, mathematics, and engineering where precise interpretation of mathematical expressions is crucial. Available as a Claude Desktop Extension (.dxt) for easy installation. Uses arxiv-to-prompt under the hood for LaTeX processing. **v0.2.2** released March 18, 2026.

### Typst MCP

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [johannesbrandenburger/typst-mcp](https://github.com/johannesbrandenburger/typst-mcp) | 144 | Python | MIT | 5 |

**NEW — fills a major gap from the initial review.** Typst is the modern LaTeX alternative that's growing rapidly in academic publishing, and this MCP server brings it into the AI ecosystem:

- **LaTeX-to-Typst conversion** — convert LaTeX code to Typst using Pandoc, with batch conversion support for multiple snippets
- **Syntax validation** — validate Typst code before submission, with batch checking capability
- **Image rendering** — render Typst markup to PNG images for visual verification by multimodal AI models
- **Documentation explorer** — list all chapters in the Typst documentation
- **Chapter retriever** — access specific documentation chapters for reference

At 144 stars, this is one of the most popular servers in this entire review — reflecting the strong and growing interest in Typst as an alternative to LaTeX. The LaTeX-to-Typst conversion tool is particularly valuable for academics migrating existing papers. Supports integration with Claude, GPT, Gemini, and VS Code agent mode.

## Document Format Conversion

### markdownify-mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [zcaceres/markdownify-mcp](https://github.com/zcaceres/markdownify-mcp) | 2,600 | TypeScript | MIT | 10 |

The **most popular server in this entire review** and a cornerstone of the document conversion MCP ecosystem. Converts virtually anything into Markdown:

- **PDF, DOCX, XLSX, PPTX** — full document conversion with structure preservation
- **Images** — metadata extraction and content description
- **Audio** — transcription to Markdown text
- **YouTube** — transcript extraction from video URLs
- **Bing search results** — web content to Markdown
- **Existing Markdown files** — retrieval with optional directory restrictions

At 2,600 stars (v1.0.4, April 2026), this is one of the most-used MCP servers across all categories. The practical value is clear — it serves as the universal ingest pipeline for getting documents into AI workflows, regardless of their original format. Supports integration with Claude Desktop, Cursor, and other MCP clients via Docker or direct configuration.

### mcp-pandoc

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [vivekVells/mcp-pandoc](https://github.com/vivekVells/mcp-pandoc) | 531 | Python | — | 1 |

Wraps the venerable **Pandoc** document converter in an MCP interface, providing bidirectional format conversion through a single powerful tool:

- **convert-contents** — transform between Markdown, HTML, PDF, DOCX, RST, LaTeX, EPUB, TXT, IPYNB, ODT

Key features: **Defaults files** (YAML configuration) for reusable conversion templates. **Pandoc filter integration** for enhanced processing. **Reference document support** for custom styling in DOCX output. The only MCP server offering true multi-format output including EPUB generation.

PDF is output-only (PDF → other formats unsupported) and requires TeX Live installation. Currently in early development, but functional for the core conversion workflow. A fork at [Omniscience-Labs/mcp-pandoc-omni](https://github.com/Omniscience-Labs/mcp-pandoc-omni) adds additional features.

### markdown2pdf-mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [2b3pro/markdown2pdf-mcp](https://github.com/2b3pro/markdown2pdf-mcp) | 34 | JavaScript | MIT | 1 |

Focused **Markdown-to-PDF conversion** with professional output features:

- Syntax highlighting for code blocks
- Custom CSS styling
- Mermaid diagram rendering
- Configurable page numbers
- Flexible watermark placement (position, opacity, rotation)
- Dynamic timeout adjustment for large files

Uses Chrome's rendering engine (Puppeteer) for modern PDF generation, producing high-quality output without requiring LaTeX installation.

### Other Conversion Servers

| Server | Stars | Language | Notes |
|--------|-------|----------|-------|
| [MaitreyaM/FILE-CONVERTER-MCP](https://github.com/MaitreyaM/FILE-CONVERTER-MCP) | 6 | Python | Pandoc + Docker, MIT |
| [jwingnut/docconvert-mcp](https://github.com/jwingnut/docconvert-mcp) | — | — | Universal format conversion |
| [patrickshomo/markdown-mcp](https://github.com/patrickshomo/markdown-mcp) | — | — | Markdown to Word (DOCX) |
| [ldangelo/website-to-pdf-mcp](https://github.com/ldangelo/website-to-pdf-mcp) | — | — | Website to PDF with link traversal |
| [rmcendarfer2017/MCP-server-PDF--Conversion](https://github.com/rmcendarfer2017/MCP-server-PDF--Conversion) | — | — | HTML to PDF |

## eBooks & Reading

### ebook-mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [onebirdrocks/ebook-mcp](https://github.com/onebirdrocks/ebook-mcp) | 361 | Python | Apache-2.0 | 10+ |

The **most comprehensive eBook interaction server**, transforming how users engage with digital books through AI:

- **Smart library management** — scan and organize eBook collections
- **Content discovery** — search across books by topic, keyword, or theme
- **Interactive reading** — AI-powered conversations about book content
- **Active learning** — quizzes and explanations generated from book content
- **Natural language navigation** — move through chapters and sections conversationally

Supports **EPUB** (with metadata, table of contents, chapter extraction) and **PDF** (with advanced page-level and chapter-based processing). Content is extracted with Markdown formatting for clean AI consumption. At 361 stars, this is by far the most popular eBook MCP server.

### calibre-mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [trieloff/calibre-mcp](https://github.com/trieloff/calibre-mcp) | 30 | Shell | Apache-2.0 | 4 |

Bridges AI assistants to **Calibre**, the most popular open-source eBook management application:

- **search-fulltext** — full-text search with automatic phrase matching and fuzzy fallback
- **search-author** — find books by author with partial matching
- **search-title** — title-based search with partial matching
- **get-excerpt** — extract text excerpts with keyword highlighting and pagination

A pure bash implementation using the `calibredb` CLI. Generates Calibre deep links and file URLs for direct book access. Simple but effective for anyone with an existing Calibre library.

### Apple Books MCP

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [vgnshiyer/apple-books-mcp](https://github.com/vgnshiyer/apple-books-mcp) | 48 | Python | Apache-2.0 | 12 |

Enables AI integration with **Apple Books** libraries on macOS. **v0.7.3** (April 24, 2026) across 17 releases has significantly expanded functionality:

- **"Pick up where you left off"** — chapter position tracking so AI knows exactly where you are in a book
- **Highlight context retrieval** — highlights marked with `«...»` anchors for precise referencing
- **Reading analytics** — patterns across your personal library
- **Non-DRM EPUB content access** — read the actual text of non-Store books
- **Resource attachment** for "Currently Reading" books
- **Pre-built prompts** for weekly reading digests and library reflection
- Summarize recent reading highlights, organize books by genre, generate recommendations
- Search highlights by color, text content, or notes
- Full-text search across all annotations

A powerful tool for readers who use Apple Books — the v0.7.3 update with chapter position tracking transforms it from a highlight extraction tool into a genuine reading companion.

### BookLife MCP

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [andylbrummer/booklife-mcp](https://github.com/andylbrummer/booklife-mcp) | 2 | Go | — | 27 |

A **unified reading management platform** connecting three services into one MCP interface:

- **Hardcover** — reading tracker (currently reading, want to read, finished)
- **Libby/OverDrive** — library catalog search and hold management
- **Open Library** — book metadata and enrichment

Features automatic reading analytics (genres, authors, patterns, streaks), content-based recommendations using enriched metadata, and one-command synchronization across platforms. The 27 tools across 10 categories make this the most feature-rich reading management MCP server, though the low star count suggests it's still early-stage.

### Other eBook & Reading Servers

| Server | Stars | Language | Notes |
|--------|-------|----------|-------|
| [wahiggins3/send-to-kindle-mcp](https://github.com/wahiggins3/send-to-kindle-mcp) | 1 | Python | Convert text/Markdown to EPUB, send to Kindle via email |
| [kinshukk/book-fetch-mcp](https://github.com/kinshukk/book-fetch-mcp) | 4 | Python | Access published books via Gemini 1.5 |

## Book Discovery & Metadata

### mcp-open-library

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [8enSmith/mcp-open-library](https://github.com/8enSmith/mcp-open-library) | 71 | TypeScript | MIT | 6 |

Connects AI assistants to the **Internet Archive's Open Library** — a free, open catalog of every book ever published:

- Search for books by title
- Search for authors by name
- Retrieve detailed author biographical information
- Get book cover images by various identifier types
- Access author photos using Open Library IDs (OLIDs)

At 71 stars, this is the most popular book discovery MCP server. Open Library's catalog is massive (covering millions of books), making this a valuable research tool for AI agents that need bibliographic information.

### Other Book Discovery Servers

| Server | Stars | Language | Notes |
|--------|-------|----------|-------|
| [juanbeniteza/mcp-google-books](https://github.com/juanbeniteza/mcp-google-books) | — | TypeScript | Google Books API search by title/author |
| [uysalserkan/openlibrary-mcp](https://github.com/uysalserkan/openlibrary-mcp) | — | Python | Alternative Open Library implementation |
| [VmLia/books-mcp-server](https://github.com/VmLia/books-mcp-server) | 5 | Python | Book querying for Cherry Studio and other clients |

## Print-on-Demand

### Printify MCP

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [TSavo/printify-mcp](https://github.com/TSavo/printify-mcp) | 25 | TypeScript | — | 15+ |

Integrates AI assistants with **Printify's print-on-demand platform** for creating and managing custom products:

- **Shop management** — list and switch between Printify shops
- **Product operations** — create, read, update, delete, and publish products
- **Blueprint browsing** — explore available product types and variants
- **Image uploads** — upload designs directly to Printify
- **AI image generation** — generate product designs using Replicate's Flux 1.1 Pro model
- **Step-by-step product creation guides** built into the tool documentation

The AI image generation integration is notable — agents can design products end-to-end without human intervention, from generating artwork to uploading it to a product listing. Available via npm, npx, Docker, or from source.

A second implementation at [jeffkimble/printify-mcp-server](https://github.com/jeffkimble/printify-mcp-server) (JavaScript, MIT, 11 tools) provides a lighter alternative focused on the core Printify API.

### Lulu Print MCP

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [devlimelabs/lulu-print-mcp](https://github.com/devlimelabs/lulu-print-mcp) | 1 | TypeScript | — | 20+ |

Integration with the **Lulu Print API** for book printing and publishing:

- **Print job management** — create, update, cancel, and track orders through delivery
- **File validation** — validate interior and cover PDFs with dimension checking and error reporting
- **Cost calculation** — compute product costs including shipping and tax breakdowns
- **Shipping management** — access available shipping options by destination with multiple service levels
- **Webhooks** — subscribe to print job status changes with endpoint management
- **Statistics & reporting** — track print jobs over time with daily/weekly/monthly grouping

Supports both sandbox and production environments, making it suitable for testing workflows before committing to real print jobs. Lulu is a major player in self-publishing and print-on-demand books, so this integration enables AI-assisted book publishing workflows.

## Desktop Publishing

### InDesign MCP Servers

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [zachshallbetter/indesign-mcp-server](https://github.com/zachshallbetter/indesign-mcp-server) | 10 | JavaScript | — | 135+ |
| [lucdesign/indesign-mcp-server](https://github.com/lucdesign/indesign-mcp-server) | 16 | JavaScript | MIT | 35+ |
| [chris-enea/indesign-mcp](https://github.com/chris-enea/indesign-mcp) | 9 | Python | — | 4 |

Three implementations target **Adobe InDesign**, the industry-standard desktop publishing application:

**zachshallbetter/indesign-mcp-server** (10 stars, 135+ tools) is the most ambitious — covering document lifecycle management, page manipulation, text frames with professional typography, graphics with precise scaling, tables, layers, master spreads, styles, colors, and multi-document book creation. Designed for automated report generation, brand asset management, and multi-page publication workflows.

**lucdesign/indesign-mcp-server** (16 stars, MIT, 35+ tools) focuses on practical publishing workflows — document management with standard page formats (A4/A5/Letter/Legal/Custom), advanced typography controls (leading, tracking, optical margin alignment), CSV data integration for tables, professional PDF export presets, EPUB export, and print production packaging. Includes custom ExtendScript execution for advanced automation.

**chris-enea/indesign-mcp** (9 stars, Python, 4 tools) provides minimal text manipulation — insert, find/replace, delete, and retrieve text through ExtendScript API.

All InDesign servers require **macOS with Adobe InDesign 2025+** installed, as they communicate with InDesign through AppleScript or ExtendScript. This limits practical use to designers who already have InDesign on their machines.

### AffinityMCP

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [tacyan/AffinityMCP](https://github.com/tacyan/affinitymcp) | 18 | Rust | — | 9 |

**NEW — fills a major gap from the initial review.** Affinity Publisher was explicitly listed as missing, and this Rust-based MCP server provides automation for the entire Affinity suite:

- **open_file** — open files in Affinity Photo, Designer, or Publisher
- **create_new** — create new documents in any Affinity application
- **export** — export in multiple formats (PDF, PNG, JPEG, SVG, etc.)
- **apply_filter** — apply filters and effects to documents
- **get_active_document** — retrieve information about the current document
- **close_document** — close documents
- **batch operations** — process up to 16 files simultaneously in parallel

Supports Affinity Photo, Affinity Designer, and **Affinity Publisher** — the leading InDesign alternative that uses a one-time purchase model instead of subscriptions. Currently macOS-primary with Windows support under development. Compatible with Claude Desktop, Cursor, and VS Code via standard MCP configuration.

### Adobe Creative Suite MCP

| Server | Language | Notes |
|--------|----------|-------|
| [matrayu/adobe-mcp](https://github.com/matrayu/adobe-mcp) | — | Unified server for Photoshop, Premiere Pro, Illustrator, and InDesign |

A unified MCP server targeting the entire Adobe Creative Suite, though with less depth per application than dedicated InDesign servers.

### Canva MCP

| Server | Language | Tools | Notes |
|--------|----------|-------|-------|
| [EmilyThaHuman/canva-mcp-server](https://github.com/EmilyThaHuman/canva-mcp-server) | TypeScript | 20 | OAuth 2.0, AI design generation |
| [mattcoatsworth/canva-mcp-server](https://github.com/mattcoatsworth/canva-mcp-server) | TypeScript | — | Alternative implementation |
| [universal-mcp/canva](https://github.com/universal-mcp/canva) | — | — | Universal MCP framework version |

**EmilyThaHuman/canva-mcp-server** provides 20 tools for Canva's design platform:

- **Design search and management** — search, retrieve details, extract content, view pages
- **AI design generation** — create designs from natural language descriptions
- **Design editing** — transaction-based editing with title updates, text/media replacement
- **Folder organization** — create folders, move items, browse with filtering
- **Collaboration** — comment on designs, reply to threads
- **Asset management** — upload from URLs, retrieve metadata with thumbnails

Requires a Canva Developer account and OAuth 2.0 authentication with 10+ required scopes. More accessible than InDesign (no desktop app required), but limited to Canva's design paradigm.

## PDF Tools

### mcp-pdf-tools

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [hanweg/mcp-pdf-tools](https://github.com/hanweg/mcp-pdf-tools) | 74 | Python | Unlicense | 5 |

Focused **PDF manipulation** for common document operations:

- **Combine PDFs** — merge multiple documents into unified files
- **Merge in sequence** — combine PDFs in user-specified order
- **Extract pages** — pull specific pages from PDF documents
- **Search PDFs** — find PDF files across the filesystem
- **Consolidate** — identify and merge related PDFs using text extraction and regex matching

At 74 stars, this is the most popular PDF manipulation MCP server. The Unlicense means it's effectively public domain — no licensing restrictions whatsoever.

For PDF reading and text extraction, see our dedicated [PDF & Document MCP review](/reviews/pdf-document-mcp-servers/) which covers the much larger ecosystem of PDF reading servers (SylphxAI/pdf-reader-mcp, document-edit-mcp, and many others).

## What's Missing

The publishing and typesetting MCP space has narrowed its gaps since the initial review, but significant ones remain:

- **No EPUB authoring** — servers can read EPUBs and convert to EPUB via Pandoc, but no dedicated EPUB creation/editing MCP tools exist (smerchek/claude-epub-skill exists as a Claude Skill for markdown-to-EPUB3 conversion at 110 stars, but it's not an MCP server)
- **No Amazon KDP integration** — Kindle Direct Publishing is the dominant self-publishing platform, with no MCP server (automation tools like ekr0/auto-kdp exist but don't use MCP)
- **No newspaper/magazine layout** — InDesign servers handle generic layout but nothing targets periodical publishing workflows
- **No book cover design tools** — cover creation is a critical self-publishing need with no dedicated MCP solution
- **No ISBN/metadata management** — no tools for managing ISBNs, BISAC codes, or publishing metadata
- **No Kobo/Apple Books publishing** — only Amazon Kindle gets a send-to-device tool; no publishing platform integrations for other e-readers
- **No QuarkXPress** — the legacy desktop publishing tool has no MCP presence
- **No collaborative editing** — real-time co-authoring (Google Docs-style) through MCP doesn't exist

**Gaps filled since the initial review:** Typst (johannesbrandenburger/typst-mcp, 144 stars) and Affinity Publisher (tacyan/AffinityMCP, 18 stars) were both explicitly called out as missing and now have functional MCP servers.

## The Bottom Line

Publishing and typesetting MCP servers cover a wide range of document production needs — from LaTeX compilation to print-on-demand — and the ecosystem has strengthened meaningfully since the initial review in March 2026.

**Best in class:** markdownify-mcp (2,600 stars, v1.0.4) remains the standout — a genuine best-in-class tool for getting any document format into AI workflows. mcp-pandoc (531 stars) is the go-to for multi-format conversion including EPUB output. ebook-mcp (361 stars) provides the most comprehensive eBook reading experience.

**Major gap fills:** typst-mcp (144 stars) brings the modern LaTeX alternative into the MCP ecosystem with LaTeX-to-Typst conversion, syntax validation, and image rendering — a significant addition for academic publishing. AffinityMCP (18 stars, Rust) provides the first MCP server for the leading InDesign alternative, with batch processing and multi-app support.

**Solid foundations:** TeXFlow (22 stars) offers an elegant structured approach to LaTeX authoring. arxiv-latex-mcp (127 stars, v0.2.2) continues to solve a real pain point for academic researchers. Apple Books MCP (48 stars, v0.7.3) has evolved into a genuine reading companion with chapter tracking and reading analytics. OverleafMCP (110 stars, +51%) has gained significant traction.

**Ambitious but limited:** InDesign servers remain technically impressive but require macOS + Adobe InDesign, limiting their audience. Overleaf integrations have expanded to 7+ implementations with continued fragmentation.

The category earns **4 out of 5**, upgraded from 3.5. Two explicitly-called-out gaps have been filled (Typst and Affinity Publisher), document conversion remains best-in-class infrastructure, OverleafMCP surged in popularity, and Apple Books MCP got a transformative update. The academic publishing pipeline (arXiv → LaTeX → Typst → PDF) is now significantly stronger. Remaining deductions for continued Overleaf fragmentation, no EPUB authoring tools, no Amazon KDP integration, no newspaper/magazine layout tools, and desktop publishing still being macOS-primary. The self-publishing pipeline still has gaps, but the authoring and typesetting side of publishing is now well-covered.

*This review was refreshed on 2026-04-27 using Claude Opus 4.6 (Anthropic). Originally published 2026-03-15.*

