---
title: "Best PDF & Document Processing MCP Servers in 2026 — MarkItDown vs Docling vs Kreuzberg vs Official MCP PDF Server"
date: 2026-03-22T23:30:00+09:00
description: "We compared 30+ PDF and document processing MCP servers across multi-format converters, the official MCP PDF server, dedicated PDF readers, manipulation tools, Word servers, and cloud APIs."
og_description: "30+ PDF & document MCP servers compared: MarkItDown, Official MCP PDF, kreuzberg, Docling, Pandoc, Stirling PDF, Unstructured. Honest recommendations from research."
content_type: "Comparison"
card_description: "Official MCP PDF Server (779K npm downloads/month) vs MarkItDown (115K stars, 29+ formats) vs kreuzberg (7.6K stars, Rust-core 97+ formats) vs Docling (58.4K stars, layout analysis) vs pdf-reader-mcp (657 stars, parallel processing) — plus Pandoc, Word, cloud API, and manipulation options."
last_refreshed: 2026-04-23
---

Document processing is one of the most immediately useful MCP capabilities. Converting PDFs to text, extracting tables, transforming between formats — these are tasks that come up constantly when working with AI assistants. The ecosystem has responded with servers ranging from simple PDF readers to comprehensive multi-format conversion suites.

The landscape splits seven ways. **The official MCP PDF server** now ships in the reference implementation with 779K npm downloads/month. **Multi-format converters** like MarkItDown, kreuzberg, and Docling handle dozens of input formats and output clean Markdown. **Dedicated PDF readers** focus on fast, accurate text extraction with features like caching and parallel processing. **Format converters** use Pandoc or custom pipelines for bidirectional document transformation. **PDF manipulation tools** handle merging, splitting, watermarking, and OCR. **Word document servers** provide full DOCX creation and editing. And **cloud API wrappers** connect to services like Unstructured and PDF.co for heavy processing.

What surprised us: The biggest shift since March is how fast the landscape is consolidating. The **official @modelcontextprotocol/server-pdf** went from launch (January 2026) to 779K npm downloads/month — making it the most-downloaded PDF MCP server by far. **kreuzberg** exploded to 7,628 stars with its Rust-core, 97+ format document intelligence framework. Meanwhile, **MarkItDown** surged from 91K to 115K stars and remains the most-starred project in the space. Several previously-active servers have gone stale — mcp-pandoc hasn't been updated since September 2025, and Office-Word-MCP-Server since December 2025.

**Disclosure:** Our recommendations are based on research — analyzing documentation, GitHub repositories, community feedback, and published benchmarks. We have not hands-on tested every server in this guide.

## What Changed (March → April 2026)

| Server | What changed |
|--------|-------------|
| **@modelcontextprotocol/server-pdf** | **NEW in guide.** Official MCP PDF server, v1.7.0, 779K npm downloads/month, chunked pagination + interactive viewer |
| **kreuzberg** | **NEW in guide.** 7,628 stars, Rust-core, 97+ formats, v4.9.4, 135K PyPI downloads/month, MCP serve mode |
| **kordoc** | **NEW in guide.** 819 stars in <1 month, Korean document specialist (HWP/HWPX/PDF), formula OCR |
| **PSPDFKit/nutrient-dws-mcp** | **NEW in guide.** Enterprise PDF processing via Nutrient API, 63 stars |
| **NameetP/pdfmux** | **NEW in guide.** Self-verifying PDF extraction, #2 reading order accuracy, 57 stars |
| **microsoft/markitdown-mcp** | Stars 91,400→115,160 (+26%). Still v0.1.5 |
| **docling-mcp** | Stars 522→585, library 56,200→58,399. Still v1.3.4 (no release since Jan 2026) |
| **zcaceres/markdownify-mcp** | Stars 2,500→2,600, **v1.0.4** (3 new releases since March) |
| **SylphxAI/pdf-reader-mcp** | Stars 571→657 (+15%), **v2.3.1** (dependency vulnerability fix), 9.8K npm downloads/month |
| **vivekVells/mcp-pandoc** | Stars 517→529. **Stale** — no pushes since Sep 2025 (7 months) |
| **GongRzhe/Office-Word-MCP-Server** | Stars 1,800→1,880. **Stale** — no pushes since Dec 2025 (4 months) |
| **jztan/pdf-mcp** | Stars 9→21 (+133%). Steady growth |
| **Tele-AI/doc-ops-mcp** | 138 stars (unchanged). Last pushed Mar 30 |
| **Unstructured-IO/UNS-MCP** | Stars 42→43. Last pushed Apr 12 |
| **awslabs/mcp (document-loader)** | Monorepo 8,843 stars. Active (pushed Apr 23) |

## At a Glance: Top Picks

| Category | Our pick | Stars / Downloads | Runner-up |
|----------|----------|-------------------|-----------|
| **Official MCP PDF** | [@modelcontextprotocol/server-pdf](https://www.npmjs.com/package/@modelcontextprotocol/server-pdf) | 779K npm/month | — |
| **Multi-format (to Markdown)** | [microsoft/markitdown-mcp](https://github.com/microsoft/markitdown/tree/main/packages/markitdown-mcp) | 115K (mono) | [zcaceres/markdownify-mcp](https://github.com/zcaceres/markdownify-mcp) (2,600) |
| **Document intelligence** | [kreuzberg-dev/kreuzberg](https://github.com/kreuzberg-dev/kreuzberg) | 7,628 | [docling-project/docling-mcp](https://github.com/docling-project/docling-mcp) (585) |
| **Multi-format (AI-powered)** | [docling-project/docling-mcp](https://github.com/docling-project/docling-mcp) | 585 | — |
| **Format conversion (Pandoc)** | [vivekVells/mcp-pandoc](https://github.com/vivekVells/mcp-pandoc) | 529 ⚠️ stale | [Tele-AI/doc-ops-mcp](https://github.com/Tele-AI/doc-ops-mcp) (138) |
| **Dedicated PDF reader** | [SylphxAI/pdf-reader-mcp](https://github.com/SylphxAI/pdf-reader-mcp) | 657 | [jztan/pdf-mcp](https://github.com/jztan/pdf-mcp) (21) |
| **PDF manipulation** | [gufao/mcp-server-stirling-pdf](https://github.com/gufao/mcp-server-stirling-pdf) | 1 | [Tele-AI/doc-ops-mcp](https://github.com/Tele-AI/doc-ops-mcp) (138, watermark/QR) |
| **Word documents** | [GongRzhe/Office-Word-MCP-Server](https://github.com/GongRzhe/Office-Word-MCP-Server) | 1,880 ⚠️ stale | — |
| **Cloud API (enterprise)** | [Unstructured-IO/UNS-MCP](https://github.com/Unstructured-IO/UNS-MCP) | 43 | [pdfdotco/pdfco-mcp](https://github.com/pdfdotco/pdfco-mcp) (9) |
| **AWS ecosystem** | [awslabs/document-loader-mcp-server](https://github.com/awslabs/mcp/tree/main/src/document-loader-mcp-server) | Official | — |
| **Korean documents** | [chrisryugj/kordoc](https://github.com/chrisryugj/kordoc) | 819 | — |

## Official MCP PDF Server

### @modelcontextprotocol/server-pdf — The Reference Implementation

**Downloads:** 779,217 npm/month (340K/week) | **Language:** TypeScript | **License:** MIT | **Version:** v1.7.0 (April 21, 2026)

The official PDF server from the Model Context Protocol team. Part of the [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) monorepo (84,330 stars). Launched January 15, 2026 and already the most-downloaded PDF MCP server by a wide margin.

**What makes it stand out:**
- **Official reference implementation** — maintained by the MCP team alongside the protocol itself
- **Chunked pagination** — reads PDFs in manageable chunks rather than loading entire documents, critical for large files
- **Interactive viewer** — built-in PDF viewing capability
- **7 releases in 3 months** — v1.0 to v1.7.0, active and rapid development
- **Part of the reference monorepo** — benefits from shared infrastructure, testing, and MCP protocol updates
- **779K npm downloads/month** — dwarfs every other PDF MCP server combined

**Limitations:**
- Text extraction only — no layout analysis, no table detection, no OCR
- No image extraction from PDFs
- No caching between reads
- Part of a monorepo — can't easily star or track the PDF server independently

**Best for:** The default starting point for PDF text extraction in MCP. If you're setting up MCP for the first time and need PDF support, start here. For complex layouts or advanced features, pair with or switch to MarkItDown, kreuzberg, or Docling.

## Multi-Format Converters

The heavyweights of document processing. These servers handle many input formats and convert everything to Markdown — the format LLMs understand best.

### microsoft/markitdown-mcp — The Most-Starred

**Stars:** 115,160 (monorepo, +26% since March) | **Language:** Python | **License:** MIT

Microsoft's MarkItDown is the dominant document-to-Markdown conversion tool. The MCP server wraps it in a single, clean tool.

**What makes it stand out:**
- **29+ input formats** — PDF, Word, PowerPoint, Excel, HTML, images (with EXIF/OCR), audio (with transcription), CSV, JSON, XML, ZIP, EPub, YouTube URLs
- **Single tool: `convert_to_markdown(uri)`** — accepts http:, https:, file:, and data: URIs. Simple and predictable
- **Three transport protocols** — STDIO (default), Streamable HTTP, and SSE. Most MCP servers only support STDIO
- **Docker-first deployment** — recommended approach for Claude Desktop integration, with volume mounting for local file access
- **Structure preservation** — headings, lists, tables, and links are maintained in the Markdown output
- **Plugin system** — OCR via LLM vision, Azure Document Intelligence integration
- **v0.1.5** — released February 2026, still current. Active development by Microsoft's AutoGen team

**Limitations:**
- Single tool means no search, no caching, no page-level control — you convert the whole document
- OCR requires additional plugin configuration (LLM vision or Azure DI)
- Docker recommended means slightly heavier setup than pip-based servers
- Output quality varies by format — PDFs with complex layouts can lose structure

**Best for:** Developers who need multi-format document-to-Markdown conversion. The 115K-star ecosystem, Microsoft backing, and format breadth make this the strongest multi-format option. For PDF-only needs, consider the official MCP PDF server first.

### zcaceres/markdownify-mcp — The Multi-Tool Alternative

**Stars:** 2,600 | **Language:** TypeScript | **License:** MIT | **Version:** v1.0.4 (April 17, 2026)

Where MarkItDown has one tool, markdownify-mcp has ten — each specialized for a different input type. Three new releases since March keep it actively maintained.

**What makes it stand out:**
- **10 dedicated tools** — pdf-to-markdown, docx-to-markdown, xlsx-to-markdown, pptx-to-markdown, image-to-markdown, audio-to-markdown, youtube-to-markdown, webpage-to-markdown, bing-search-to-markdown, get-markdown-file
- **Format-specific handling** — each tool is optimized for its input type rather than using a one-size-fits-all approach
- **Web content support** — YouTube transcript extraction and Bing search results conversion built in
- **TypeScript** — easier to extend for JavaScript/TypeScript developers

**Limitations:**
- More tools means more context window tokens consumed by tool descriptions
- Less community momentum than MarkItDown
- No caching or pagination

**Best for:** Developers who want explicit control over which conversion path is used, or who need YouTube/web content conversion alongside document processing.

### kreuzberg-dev/kreuzberg — Rust-Core Document Intelligence

**Stars:** 7,628 | **Language:** Rust (Python/Ruby/Java/Go/PHP/Elixir/C#/R/C/TypeScript bindings) | **License:** Elastic-2.0 | **Version:** v4.9.4 (April 22, 2026)

The fastest-growing document processing framework in the MCP ecosystem. Kreuzberg launched as a polyglot document intelligence platform with a Rust core and built-in MCP server mode. 10+ releases in April alone.

**What makes it stand out:**
- **97+ input formats** — PDFs, Office docs, images, and more. Broader format coverage than MarkItDown
- **Rust core** — native performance with bindings for 11 programming languages
- **Built-in MCP server** — `kreuzberg serve` starts an MCP server directly, no wrapper needed
- **GPU-accelerated OCR** — PaddleOCR support for scanned document processing
- **Text, metadata, images, and structured data extraction** — goes beyond simple text extraction
- **CLI + REST API + MCP** — three access modes from one tool
- **135K PyPI downloads/month** — strong adoption outside MCP as well
- **Extremely active** — v4.8.1 through v4.9.4 in April alone

**Limitations:**
- **Elastic-2.0 license** — NOT traditional open source. Restricts competing SaaS offerings. Fine for internal use and most commercial use, but check the license if you're building a document processing service
- Newer project — less battle-tested than MarkItDown or Docling
- Rust core means build complexity for contributors
- MCP server mode is relatively new

**Best for:** Teams that need high-performance document intelligence across many formats and languages. The Rust core makes it the fastest option for large-scale processing. Check the Elastic-2.0 license before adopting.

### docling-project/docling-mcp — AI-Powered Layout Understanding

**Stars:** 585 (MCP server) / 58,399 (Docling library) | **Language:** Python | **License:** MIT

Docling is IBM's document processing library, now in the Linux Foundation. The MCP server brings its advanced PDF understanding to AI agents.

**What makes it stand out:**
- **Advanced PDF layout analysis** — page layout detection, reading order analysis, and table structure recognition using AI models. This is the key differentiator from MarkItDown
- **Docling library** (58.4K stars) — one of the most popular document processing libraries globally, backed by IBM Research
- **Broad format support** — PDF, DOCX, PPTX, XLSX, HTML, images, audio (WAV/MP3), LaTeX, plain text, even USPTO patents and XBRL financial reports
- **RAG integration** — built-in Milvus upload and retrieval for retrieval-augmented generation workflows
- **DoclingDocument format** — structured JSON output that preserves document semantics, not just text
- **Visual Language Model support** — GraniteDocling for vision-based document understanding
- **v1.3.4** — released January 2026, still current. No new MCP server release in 3 months, though the library remains active

**Limitations:**
- Heavier dependencies than MarkItDown — requires AI models for layout analysis
- Slower processing — the layout analysis adds overhead compared to simple text extraction
- Fewer MCP-specific features (no caching, no search tools)
- Python 3.10+ required

**Best for:** Documents with complex layouts — scientific papers, financial reports, multi-column PDFs, and anything where reading order and table structure matter. If MarkItDown's output is garbled, try Docling.

## Format Converters

These servers focus on bidirectional format conversion — not just extracting content, but creating documents in various formats.

### vivekVells/mcp-pandoc — The Winner (⚠️ Stale)

**Stars:** 529 | **Language:** Python | **License:** MIT

⚠️ **Maintenance warning:** No pushes since September 2025 (7 months). Still functional but not actively maintained.

A Pandoc wrapper for MCP. Pandoc is the Swiss Army knife of document conversion, and this server makes it available to AI agents.

**What makes it stand out:**
- **One powerful tool: `convert-contents`** — source format, target format, file paths, reference documents, defaults files, and custom filters
- **Broad format support** — Markdown, HTML, PDF (output only), DOCX, reStructuredText, LaTeX, EPUB, plain text, Jupyter notebooks, ODT
- **Pandoc's full power** — template support, reference documents for styling, custom filters, defaults files
- **Mermaid diagram support** — converts Mermaid diagrams during conversion
- **Active development** — 86+ commits, regular updates

**Limitations:**
- PDF is output-only (Pandoc limitation) — you can create PDFs but not read them
- Requires Pandoc installed on the system (and LaTeX for PDF output)
- Early development stage — some conversion paths are still being refined
- Single tool means no read/extract capabilities

**Best for:** Creating documents in multiple formats from Markdown or other source formats. The ideal complement to a PDF reader — use a reader to extract content, and Pandoc to generate output.

### Tele-AI/doc-ops-mcp — The Universal Document Processor

**Stars:** 138 | **Language:** JavaScript | **License:** MIT

A pure JavaScript document processing server with both read and write capabilities plus PDF enhancement features.

**What makes it stand out:**
- **11 tools** — read_document, write_document, convert_document, plan_conversion, plus format-specific converters and PDF enhancement tools
- **Zero external dependencies** — pure JavaScript implementation, no Pandoc or system tools required
- **PDF enhancement** — add watermarks (image or text) and QR codes to PDFs
- **Smart routing** — automatically selects optimal conversion path between formats
- **Conversion planning** — `plan_conversion` tool analyzes and optimizes multi-step conversions
- **Node.js 18+** — no Python dependency

**Limitations:**
- JavaScript-based conversion is less comprehensive than Pandoc for edge cases
- Conversion matrix has gaps — PDF to DOCX and PDF to HTML not supported
- Smaller community (138 stars) — less battle-tested
- Chinese documentation alongside English (minor friction for English-only users)

**Best for:** Teams that want document processing without Python/Pandoc dependencies, or who need PDF watermarking and QR code embedding.

## Dedicated PDF Readers

Servers focused purely on reading and extracting content from PDFs. Simpler than multi-format converters, but often faster and with more PDF-specific features.

### SylphxAI/pdf-reader-mcp — The Winner

**Stars:** 657 (+15%) | **Language:** TypeScript | **License:** MIT | **Version:** v2.3.1 (April 19, 2026)

The most popular dedicated PDF reading MCP server. Built for speed with parallel processing. v2.3.1 fixed vulnerable transitive dependency packages. 9,840 npm downloads/month.

**What makes it stand out:**
- **5-10x faster** — parallel page processing leverages multiple cores for large documents
- **Single tool: `read_pdf`** — handles text extraction, image extraction, metadata retrieval, and page counting through one interface
- **Y-coordinate content ordering** — preserves natural reading flow by ordering content based on position, not extraction order
- **Flexible pagination** — specify page ranges like "1-5,10-15,20" for targeted extraction
- **Image extraction** — returns base64-encoded images with metadata
- **94%+ test coverage** — 103 passing tests. Production-ready reliability
- **Per-page error resilience** — one corrupted page doesn't break the entire extraction
- **URL support** — read PDFs from HTTP/HTTPS URLs directly

**Limitations:**
- Read-only — no PDF creation or manipulation
- No caching — each read processes from scratch
- No search capability — must extract and search in the LLM context
- Single tool means all operations share the same interface

**Best for:** Developers who need fast, reliable PDF text extraction. The parallel processing makes it the best choice for large documents.

### jztan/pdf-mcp — The Smart Reader

**Stars:** 21 (+133%) | **Language:** Python | **License:** MIT

Still small but growing fast — this server has features the more popular alternatives lack.

**What makes it stand out:**
- **7 specialized tools** — pdf_info, pdf_read_pages, pdf_read_all, pdf_search, pdf_get_toc, pdf_cache_stats, pdf_cache_clear
- **SQLite caching** — persistent cache survives process restarts, essential for STDIO transport where state is lost between sessions
- **Full-text search** — search PDFs without loading the entire document into context
- **Table detection** — extracts structured data with headers and rows via visible borders
- **Automatic image extraction** — images returned as PNG file paths
- **Chunked reading** — manages large documents in configurable sections
- **Table of contents extraction** — navigate document structure before reading content

**Limitations:**
- Very low community adoption (9 stars) — less proven at scale
- Python dependency with PyMuPDF
- No parallel processing — single-threaded extraction

**Best for:** Workflows that repeatedly access the same PDFs (the caching pays off), or when you need to search within PDFs before extracting content.

### xraywu/mcp-pdf-extraction-server — OCR-Capable

**Stars:** 28 | **Language:** Python | **License:** MIT

A focused PDF extraction server with OCR support for scanned documents.

**What makes it stand out:**
- **Single tool: `extract-pdf-contents`** — clean interface with path and optional page selection
- **OCR support** — uses pytesseract for scanned document text extraction
- **Negative indexing** — use `-1` for last page, like Python list slicing
- **Claude Code CLI optimized** — specifically designed for `claude mcp add` workflow

**Limitations:**
- Requires tesseract OCR installed on the system
- Basic feature set — no caching, search, or image extraction
- Small community

**Best for:** Scanned PDFs that need OCR, especially in Claude Code CLI workflows.

## PDF Manipulation

Servers that go beyond reading — merging, splitting, watermarking, compressing, and OCR-processing PDFs.

### gufao/mcp-server-stirling-pdf — The Full Toolkit

**Stars:** 1 | **Language:** TypeScript | **License:** GPL-3.0

Tiny community, but wraps one of the most capable PDF processing platforms on the internet — Stirling PDF (56K+ stars, 25M+ downloads).

**What makes it stand out:**
- **10 manipulation tools** — merge_pdfs, split_pdf, compress_pdf, convert_pdf_to_images, rotate_pdf, add_watermark, remove_pages, extract_images, convert_images_to_pdf, ocr_pdf
- **Stirling PDF backend** — the #1 PDF application on GitHub with comprehensive processing capabilities
- **Self-hosted** — your documents stay on your infrastructure
- **OCR** — make scanned PDFs searchable
- **Compression** — reduce file sizes with configurable optimization levels

**Limitations:**
- Requires a self-hosted Stirling PDF instance (Docker recommended)
- GPL-3.0 license — copyleft requirements for derivative works
- Nearly zero community adoption (1 star) — you're the early adopter
- No text extraction — it's a manipulation tool, not a reader

**Best for:** Teams already running Stirling PDF who want AI-driven PDF manipulation. Pair with a reader server for a complete solution.

## Word Document Servers

### GongRzhe/Office-Word-MCP-Server — The Only Serious Option (⚠️ Stale)

**Stars:** 1,880 | **Language:** Python | **License:** Not specified

⚠️ **Maintenance warning:** No pushes since December 2025 (4 months). Still functional but not actively maintained.

The dominant Word document MCP server by a wide margin. If you need to create or edit DOCX files, this is it.

**What makes it stand out:**
- **Comprehensive DOCX operations** — create documents, insert headings/paragraphs/tables/images/lists, format text (bold, italic, underline, colors, fonts), merge documents
- **Table formatting** — cell merging, alignment, padding, alternating row colors, column width control
- **PDF conversion** — convert DOCX to PDF directly
- **Document protection** — password features, comment extraction and filtering
- **Custom styles** — create and apply custom document styles
- **Search and replace** — find and modify content across documents
- **Direct formatting during creation** — reduces function calls by applying formatting inline
- **Footnotes and endnotes** — academic and professional document support

**Limitations:**
- Word documents only — no PDF reading, no spreadsheets
- Python dependency
- No remote/hosted option
- License not clearly specified in the repository

**Best for:** Any workflow that needs to create or edit Word documents programmatically. The only mature option in this space.

## Cloud API Wrappers

Servers that connect to cloud-based document processing services. More powerful but require API keys and internet access.

### Unstructured-IO/UNS-MCP — Enterprise Document Pipeline

**Stars:** 43 | **Language:** Python | **License:** Not specified

Wraps the Unstructured API — a serious enterprise document processing platform used for ETL and RAG pipelines.

**What makes it stand out:**
- **19 tools** — source/destination connector management, workflow creation and execution, job monitoring
- **Multi-cloud connectors** — S3, Azure, Google Drive, plus vector databases (Weaviate, Pinecone, MongoDB, Neo4j)
- **Workflow automation** — create end-to-end document processing pipelines, not just one-off conversions
- **Firecrawl integration** — web crawling and LLM-optimized text generation
- **Enterprise-grade** — designed for production document processing at scale

**Limitations:**
- Requires Unstructured API key (paid service)
- Not a direct document conversion tool — it's a pipeline orchestrator
- Heavy setup — multiple connectors and workflows to configure
- More suited to data engineering than ad-hoc document processing

**Best for:** Enterprise teams building document processing pipelines that feed into RAG systems or data warehouses.

### pdfdotco/pdfco-mcp — Full-Service PDF API

**Stars:** 9 | **Language:** Python | **License:** Not specified

Wraps PDF.co's comprehensive API for every PDF operation imaginable.

**What makes it stand out:**
- **Extensive conversion tools** — PDF to JSON, CSV, text, XLS, XLSX, XML, HTML, and images (JPG/PNG/WebP/TIFF)
- **Reverse conversion** — DOC, DOCX, spreadsheets, images, web pages, emails (MSG/EML) to PDF
- **PDF editing** — merge, split, add annotations, fill forms
- **Security** — password protection, OCR for searchability
- **Cloud-based processing** — no local dependencies

**Limitations:**
- Requires PDF.co API key (paid service with usage-based pricing)
- Cloud processing means documents leave your infrastructure
- Small community (9 stars)
- API dependency — no offline capability

**Best for:** Developers who need comprehensive PDF manipulation without managing local tools, and are comfortable with a paid API.

### awslabs/document-loader-mcp-server — AWS Ecosystem

**Stars:** Part of official awslabs/mcp monorepo | **Language:** Python | **License:** Apache 2.0

AWS's official document loader for MCP, designed for the AWS ecosystem.

**What makes it stand out:**
- **3 tools** — read_document (PDF, DOCX, DOC, XLSX, XLS, PPTX, PPT), read_image (PNG, JPG, GIF, BMP, TIFF, WEBP), extract_slides_as_images (PPTX, PPT, PDF to PNG)
- **Official AWS** — backed by AWS Labs, part of their MCP server catalog
- **Slide/page extraction** — converts presentation slides or PDF pages to individual images for LLM vision analysis
- **Configurable limits** — MAX_FILE_SIZE_MB (default 50MB), directory-based access security
- **Docker support** — containerized deployment option

**Limitations:**
- Read-only — extraction only, no document creation or manipulation
- Requires LibreOffice (for PPTX/PPT) and poppler-utils (for PDF to image) for full feature set
- Basic text extraction — no layout analysis, no table detection
- AWS-focused documentation and ecosystem

**Best for:** Teams already in the AWS ecosystem who need a reliable, officially supported document loader.

## Which Approach Should You Choose?

**Start with the official @modelcontextprotocol/server-pdf** if you just need PDF text extraction. It's the reference implementation, has the most downloads (779K/month), and requires zero configuration beyond `npm install`.

**Use MarkItDown** if you need multi-format document-to-Markdown conversion beyond just PDFs. It handles 29+ formats, has 115K stars of community validation, and the single `convert_to_markdown` tool is dead simple.

**Use kreuzberg** if you need high-performance document intelligence across 97+ formats with a Rust core. Best for large-scale processing or when you need GPU-accelerated OCR. Check the Elastic-2.0 license first.

**Switch to Docling** if MarkItDown's output is garbled — complex layouts, multi-column PDFs, scientific papers, or financial reports. Docling's AI-powered layout analysis handles these better, at the cost of speed.

**Add a dedicated PDF reader** (pdf-reader-mcp or pdf-mcp) if you work with PDFs frequently and need caching, search, or page-level control that the multi-format converters don't offer.

**Add mcp-pandoc** if you need to create documents — generating PDFs, DOCX, or EPUB from Markdown. Note: this server hasn't been updated since September 2025.

**Use Office-Word-MCP-Server** if you need to create or edit Word documents with full formatting control. Note: this server hasn't been updated since December 2025.

**Use kordoc** if you work with Korean documents (HWP/HWPX formats) or need formula OCR in PDFs.

**Consider cloud APIs** (Unstructured, PDF.co, PSPDFKit/Nutrient) only if you need enterprise-scale pipelines or comprehensive PDF manipulation beyond what local tools provide.

## Four Trends Worth Watching

**1. The official server changes the default.** The @modelcontextprotocol/server-pdf went from zero to 779K npm downloads/month in three months. It's now the most natural starting point for PDF extraction, pushing MarkItDown and others into "multi-format" or "advanced features" positioning. This is the MCP ecosystem maturing — official reference implementations establish baselines.

**2. Rust-core challengers arrive.** kreuzberg (7,628 stars, Rust core, 97+ formats) represents a new breed of document intelligence tool that prioritizes performance and polyglot access over Python-ecosystem convenience. Its Elastic-2.0 license signals a different business model than the MIT-licensed incumbents.

**3. Staleness is spreading.** Several established servers haven't been updated in months: mcp-pandoc (7 months), Office-Word-MCP-Server (4 months), docling-mcp (3 months since last release). Meanwhile MarkItDown, pdf-reader-mcp, and kreuzberg remain actively maintained. The gap between maintained and unmaintained servers is widening.

**4. Read vs. write remains split.** No single server handles both document reading and document creation well. MarkItDown and Docling extract content; Pandoc and doc-ops-mcp create documents. The Word server is the exception — it both reads and writes — but only for DOCX. PDF manipulation (merging, splitting, compressing) remains underserved.

## Notable New Entrants (April 2026)

These servers are too new or niche for a full review, but worth watching:

- **[chrisryugj/kordoc](https://github.com/chrisryugj/kordoc)** (819 stars) — Korean document specialist. HWP, HWPX, PDF, XLSX, DOCX to Markdown. Formula OCR via Pix2Text. v2.6.2. Created March 28, 2026 — 819 stars in under a month is remarkable growth.
- **[PSPDFKit/nutrient-dws-mcp-server](https://github.com/PSPDFKit/nutrient-dws-mcp-server)** (63 stars) — Enterprise PDF processing via the Nutrient (formerly PSPDFKit) Document Web Service API. v0.0.5. Commercial API backend.
- **[NameetP/pdfmux](https://github.com/NameetP/pdfmux)** (57 stars) — Novel self-verifying PDF extraction. Claims #2 reading order accuracy with zero AI, zero GPU, zero cost. Last pushed April 16.
- **[I-CAN-hack/pdf-mcp](https://github.com/I-CAN-hack/pdf-mcp)** (29 stars) — PDF with image rendering support. Created March 2026.
- **[onebirdrocks/ebook-mcp](https://github.com/onebirdrocks/ebook-mcp)** (358 stars) — eBook specialist supporting EPUB, PDF, and other formats. Apache-2.0.

## What's Missing

- **No official Adobe MCP server** — Adobe Acrobat has the most comprehensive PDF API in the world, but no MCP integration
- **No official Microsoft Office MCP server for documents** — Word, PowerPoint reading/writing through Microsoft's own MCP catalog is absent (Excel has some coverage via Copilot)
- **No Apple iWork support** — no Pages, Keynote, or Numbers MCP servers
- **No PDF form filling** — most servers extract form data but can't fill forms (PDF.co and AryanBV/pdf-toolkit-mcp are the exceptions, though the latter is very small at 4 stars)
- **Limited table extraction** — most servers struggle with complex tables. Docling is best here but still imperfect
- **No PDF comparison/diff** — comparing two versions of a document is a common need with no MCP solution
- **No digital signature support** — signing PDFs or verifying signatures isn't available in any server
- **Staleness risk** — mcp-pandoc (7 months without updates) and Office-Word-MCP-Server (4 months) may need community forks or replacements
