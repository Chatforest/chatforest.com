---
title: "PDF & Document Processing MCP Servers — MarkItDown, Docling, PDF Reader, and More"
date: 2026-03-15T03:12:00+09:00
description: "PDF and document processing MCP servers let AI agents extract text, convert formats, parse tables, and analyze documents across PDF, DOCX, EPUB, and 30+ file types."
og_description: "PDF & document MCP servers: MarkItDown (114K stars, 29+ formats, official), Docling (583 stars, IBM-backed, layout analysis + Heron model), PDF Reader MCP (657 stars, v2.3.1, fastest extraction), jztan/pdf-mcp (NEW, 8 tools, hybrid search + caching). 15+ servers across 5 approaches. Rating: 3.5/5."
content_type: "Review"
card_description: "PDF and document processing MCP servers across MarkItDown (114K stars), Docling (58.3K core stars, Heron layout model), PDF Reader MCP (657 stars, v2.3.1), jztan/pdf-mcp (NEW — 8 tools, hybrid search + caching), mcp-pandoc, eBook-MCP, and PDF.co. Microsoft and IBM both ship official servers, with Docling's core library surging 58% to become the fastest-growing project in the category. The ecosystem split between universal converters and PDF-specific extractors persists, but intelligent caching and hybrid search are emerging as differentiators in the PDF-specific space."
last_refreshed: 2026-04-22
---

Every AI workflow eventually hits the same wall: "I need to read this PDF." Document processing is one of the most universally needed MCP capabilities, and the ecosystem has responded with servers ranging from Microsoft's 114,000-star universal converter to single-purpose PDF extractors built for speed.

The headline finding: **Docling's core library has surged 58% to 58,300 stars**, making it the fastest-growing project in this category and closing the gap with MarkItDown's ecosystem dominance. The new Heron layout model delivers 20-24% mAP improvement over previous baselines. Meanwhile, **PDF Reader MCP hit v2.3.1** with a major version bump, and a **new entrant — jztan/pdf-mcp — introduces intelligent caching and hybrid BM25+semantic search**, bringing a fundamentally different approach to PDF processing. The category split between universal converters and PDF-specific tools persists, but the PDF-specific side is innovating faster.

**Category:** [Business & Productivity](/categories/business-productivity/)

---

## The Landscape

### Universal Document Converters

These servers handle PDF alongside dozens of other formats, converting everything to Markdown for LLM consumption.

#### Microsoft MarkItDown

| Detail | Value |
|--------|-------|
| Repository | [microsoft/markitdown](https://github.com/microsoft/markitdown) |
| Stars | ~114,000 |
| Forks | ~7,400 |
| Language | Python |
| License | MIT |
| MCP Package | `markitdown-mcp` |
| Formats | 29+ (PDF, DOCX, PPTX, XLSX, HTML, CSV, JSON, XML, EPUB, images, audio, ZIP) |
| Tools | 1 (`convert_to_markdown`) |
| Transports | stdio, Streamable HTTP, SSE |
| Version | v0.1.5 (Feb 2026) |

**MarkItDown is the most popular document processing tool in the AI ecosystem by a massive margin.** At 114,000 stars (+26% since March) with 7,400 forks, it dwarfs everything else in this category combined. Growth has slowed slightly from its explosive early adoption phase, but the install base continues to expand.

The MCP server exposes a single tool — `convert_to_markdown(uri)` — that accepts any `http:`, `https:`, `file:`, or `data:` URI. That's it. One tool, 29+ formats, zero configuration decisions. The simplicity is the point: you don't choose extraction strategies or configure layout analysis. You give it a document, you get Markdown back.

**Format coverage is the broadest of any document MCP server.** PDF, Word, PowerPoint, Excel, HTML, CSV, JSON, XML, EPUB, images (with EXIF metadata and optional OCR via the `markitdown-ocr` plugin), audio (with transcription), YouTube URLs, and ZIP archives. Third-party plugins extend it further. The v0.1.5 release improved PDF table extraction with aligned Markdown output and fixed partially numbered lists.

**The trade-offs are real.** One tool means no fine-grained control — you can't extract just page 5, or get images separately, or preserve table coordinates. PDF extraction quality depends on the underlying parser, and complex layouts (multi-column, nested tables, scanned documents) can lose structure. The MCP server has no authentication, running with the privileges of whatever user started it. And 348 open issues (up from 304) suggest the project is growing faster than it can resolve edge cases. No new release since February — the MCP server layer is stable but not rapidly iterating.

**Install is straightforward:** `pip install markitdown-mcp`, then run `markitdown-mcp` for stdio or add `--http` for remote transport. Docker is recommended for Claude Desktop integration.

#### IBM Docling MCP

| Detail | Value |
|--------|-------|
| Repository | [docling-project/docling-mcp](https://github.com/docling-project/docling-mcp) |
| Stars | ~583 |
| Forks | ~110 |
| Core Library Stars | ~58,300 ([docling-project/docling](https://github.com/docling-project/docling)) |
| Core Library Forks | ~4,000 |
| Language | Python |
| License | MIT |
| Formats | PDF, DOCX, PPTX, XLSX, HTML, images, audio, LaTeX, WebVTT, and more |
| Tools | Multiple (convert, generate, cache management) |
| Transports | stdio, SSE, Streamable HTTP |
| MCP Version | v1.3.4 (Jan 2026) |
| Core Version | v2.90.0 (Apr 17, 2026) |

**Docling is the enterprise-grade option, backed by IBM Research and now donated to the Linux Foundation's Agentic AI Foundation.** The core Docling library has surged to 58,300 stars (+58% since March), making it the fastest-growing project in this category by far. It is described by Red Hat as "the number one open source repository for document intelligence."

Where MarkItDown converts everything to flat Markdown, **Docling preserves document structure** — it outputs DoclingDocument (structured JSON) that retains layout information, table structures, reading order, and document hierarchy. This matters for complex PDFs with multi-column layouts, nested tables, headers/footers, and mixed content. The MCP server can export to Markdown too, but the structured format is the differentiator.

**The biggest development: the Heron layout model.** Docling's new layout analysis model achieves 20.6-23.9% mAP improvement over the previous baseline, with the best variant ("heron-101") hitting 78% mAP at 28ms/image on an NVIDIA A100. Combined with 97.9% table extraction accuracy from the Granite-Docling-258M model, this is the most accurate document understanding pipeline available. New capabilities since March include structured information extraction, chart understanding (converting visuals to tables/descriptions), WebVTT subtitle support, and improved LaTeX handling.

**Key capabilities include:** PDF conversion with advanced layout analysis, table structure recovery, OCR for scanned documents, document generation, local caching for performance, and RAG integration with Milvus. The core library now also supports USPTO patent schemas, JATS articles, and XBRL financial reports.

**The weight is the trade-off.** Docling requires more infrastructure than MarkItDown — the layout analysis models need compute resources, and the full pipeline is heavier. The MCP server layer (v1.3.4, last released January) hasn't kept pace with the core library's rapid iteration (v2.90.0, 13 MCP releases total). Twenty open issues on the MCP server suggest the wrapper is still maturing, even as the core library is battle-tested.

**Install via uvx:** add the entry to your MCP client config with `uvx docling-mcp-server`. Supports Claude Desktop, LM Studio, and containerized deployments.

### PDF-Specific Servers

These focus exclusively on PDF processing, trading format breadth for depth.

#### PDF Reader MCP (SylphxAI)

| Detail | Value |
|--------|-------|
| Repository | [SylphxAI/pdf-reader-mcp](https://github.com/SylphxAI/pdf-reader-mcp) |
| Stars | ~657 |
| Forks | ~64 |
| Language | TypeScript |
| License | MIT |
| Tools | 1 (`read_pdf`) |
| Transport | stdio |
| Version | v2.3.1 (Apr 19, 2026) |
| npm | `@sylphx/pdf-reader-mcp` |

**The fastest PDF extraction MCP server, now at v2.3.1 with a major version bump since March.** PDF Reader MCP claims 5-10x faster throughput than sequential processing via automatic parallelization, with benchmarks of 5,575 ops/sec for text extraction and 12,933 ops/sec for error handling. It processes 50-page PDFs in seconds with multi-core utilization. Stars have grown from 557 to 657 (+18%).

The single `read_pdf` tool handles text extraction (full document or specific pages), image extraction as base64-encoded PNG, metadata access, and page counting. Y-coordinate based content ordering preserves natural reading order — a detail that matters for multi-column layouts where naive extraction scrambles text.

**Flexible page selection** supports ranges like "1-5,10-15,20" — something MarkItDown can't do. Per-page error isolation means a corrupted page doesn't crash the entire extraction. Supports both local files and HTTP/HTTPS URLs. The v2.x series added absolute path support on both Windows and Unix (previously restricted), configurable working directory via `cwd` in MCP server settings for relative path resolution, and improved Zod validation error handling. Active release cadence — 10+ releases since our last review.

**The limitation is scope:** PDF only, no other formats. No OCR for scanned documents (relies on extractable text). Stdio transport only — no remote hosting. But for the common case of "read this PDF quickly and correctly," it's the best option.

**Install:** `npx @sylphx/pdf-reader-mcp`. Compatible with Claude Code, Claude Desktop, VS Code, Cursor, Windsurf, Cline, and Warp.

#### PDF.co MCP

| Detail | Value |
|--------|-------|
| Repository | [pdfdotco/pdfco-mcp](https://github.com/pdfdotco/pdfco-mcp) |
| Language | Python |
| License | — |
| Tools | 15+ |
| Auth | API key (paid service) |

**The most tool-rich PDF server — but it's a paid API wrapper.** PDF.co MCP exposes 15+ tools covering PDF-to-JSON, PDF-to-CSV, PDF-to-text, PDF-to-images, document-to-PDF conversion (DOCX, images, HTML, emails), PDF merging and splitting, form filling and reading, text search, table extraction, invoice parsing (AI-powered), attachment extraction, password management, and OCR.

This is the only PDF MCP server with **invoice parsing, form filling, and PDF creation** capabilities. If you need to generate PDFs or work with form fields, PDF.co is currently the only MCP option.

**The cost barrier:** requires a PDF.co API key with paid plans. Free tier exists but is limited. Every operation is a cloud API call — no local processing, no offline use. For teams already paying for PDF.co, the MCP server is a natural extension. For everyone else, the free alternatives cover most read-only use cases.

#### pdf-mcp (jztan) — NEW

| Detail | Value |
|--------|-------|
| Repository | [jztan/pdf-mcp](https://github.com/jztan/pdf-mcp) |
| Stars | ~20 |
| Language | Python |
| License | MIT |
| Tools | 8 (`pdf_info`, `pdf_search`, `pdf_read_pages`, `pdf_read_all`, `pdf_render_pages`, `pdf_get_toc`, `pdf_cache_stats`, `pdf_cache_clear`) |
| Transport | stdio |
| Version | v1.7.0 (Apr 5, 2026) |
| PyPI | `pdf-mcp` (7,100+ downloads) |

**The most architecturally interesting new entrant — designed for context efficiency rather than raw speed.** Where PDF Reader MCP focuses on fast extraction, jztan/pdf-mcp introduces **intelligent caching via SQLite** (survives server restarts) and **hybrid BM25 + semantic search** via Reciprocal Rank Fusion. The philosophy: "Give your agent surgical access to PDFs instead of flooding context with raw text."

Eight dedicated tools cover the full read workflow: inspect document structure and text coverage, search by keyword or semantically, read specific pages with optional OCR and image rendering, extract full documents (capped at 50 pages by default), render pages as PNG for vision models, and retrieve table of contents. The `pdf_search` tool offers three modes — "keyword", "semantic", or "auto" — that merged in v1.7.0.

**Production security features** include SSRF protection for URL fetching, access control lists, HTTPS-only remote requests, and per-page text coverage metadata to identify OCR candidates. Structured table extraction outputs data as structured content rather than prose.

**Still early:** at 20 stars and 9 releases, this is a young project. But the approach — caching, hybrid search, context-aware reading — represents a different design philosophy from the "extract everything at once" servers. Worth watching.

**Install:** `pip install pdf-mcp` or `uvx pdf-mcp`.

#### Foxit PDFActionInspector

| Detail | Value |
|--------|-------|
| Repository | [foxitsoftware/PDFActionInspector](https://github.com/foxitsoftware/PDFActionInspector) |
| Stars | ~3 |
| Language | Python |
| License | MIT |
| Tools | 6+ (security analysis, action extraction, text extraction, page analysis, cache management) |

**A niche but unique server: PDF security analysis.** From Foxit Software (a major PDF vendor), PDFActionInspector extracts and analyzes JavaScript actions embedded in PDFs. It detects malicious code patterns, financial manipulation attempts, and hidden scripts across all document hierarchy levels.

Supports encrypted/password-protected PDFs. Three-layer architecture separating PDF processing from MCP protocol handling. Useful for security teams reviewing untrusted documents — but at 3 stars and narrow scope, this is a specialist tool, not a general-purpose PDF reader.

### Document Format Conversion

#### mcp-pandoc

| Detail | Value |
|--------|-------|
| Repository | [vivekVells/mcp-pandoc](https://github.com/vivekVells/mcp-pandoc) |
| Stars | ~529 |
| Language | Python |
| License | — |
| Tools | 1 (`convert-contents`) |
| Formats | Markdown, HTML, TXT, DOCX, PDF (output only), RST, LaTeX, EPUB, IPYNB, ODT |

**The bidirectional conversion server.** While MarkItDown converts documents *to* Markdown, mcp-pandoc converts *between* formats. Need Markdown→DOCX? HTML→LaTeX? EPUB→HTML? This is the server for inter-format conversion, powered by Pandoc.

The single `convert-contents` tool accepts source content, input/output format specifications, file paths, reference documents for styling, and Pandoc filter configurations. YAML defaults files enable reusable conversion templates.

**PDF is output-only** — Pandoc can generate PDFs (via LaTeX) but doesn't extract text from them. Listed in the official MCP servers registry. Requires Pandoc installed on the system.

**Use case:** when you need to *create* documents in specific formats, not just read them. Complements MarkItDown (which goes documents→Markdown) by going Markdown→documents.

### eBook Readers

#### eBook-MCP

| Detail | Value |
|--------|-------|
| Repository | [onebirdrocks/ebook-mcp](https://github.com/onebirdrocks/ebook-mcp) |
| Stars | ~358 |
| Forks | ~51 |
| Language | Python |
| License | Apache-2.0 |
| Formats | EPUB, PDF |
| Tools | Multiple (library management, metadata, TOC, chapter/page extraction) |

**Purpose-built for reading books, not processing business documents.** eBook-MCP provides library management (discover all EPUB/PDF files), metadata extraction, table of contents navigation, and chapter-by-chapter or page-by-page content extraction in Markdown format.

Multilingual documentation (English, Chinese, Japanese, Korean, French, German) suggests international community engagement. Uses PyPDF2 and PyMuPDF for PDF, ebooklib for EPUB.

**The reading experience differentiator:** while PDF Reader MCP treats PDFs as data to extract, eBook-MCP treats them as books to read — with library browsing, chapter navigation, and interactive reading sessions. For AI reading assistants and chat-based book interfaces, this is the better fit.

**Development has slowed significantly** — the last commit appears to date from early 2025, and star growth is minimal (351→358). The project is functional but appears to be in maintenance mode rather than active development.

### Other Notable Servers

**[kgand/document-parser-mcp](https://github.com/kgand/document-parser-mcp)** — Lightweight universal ingestion using Docling under the hood. Supports PDFs, Office documents, images, audio. Advanced layout analysis and table recovery. Good if you want Docling's capabilities without managing the full Docling MCP setup.

**[hanweg/mcp-pdf-tools](https://github.com/hanweg/mcp-pdf-tools)** — PDF manipulation (merge, split, extract pages) rather than content extraction. Complements the readers above.

**[xraywu/mcp-pdf-extraction-server](https://github.com/xraywu/mcp-pdf-extraction-server)** — Basic PDF text extraction with OCR support for scanned documents. Fixes specifically for Claude Code CLI compatibility.

**[BACH-AI-Tools/pdf-reader-mcp](https://github.com/BACH-AI-Tools/pdf-reader-mcp)** — Another PDF reader implementation, simpler than SylphxAI's version.

**[Safe-Swiss-Cloud-AG/mcp_pdf_reader](https://github.com/Safe-Swiss-Cloud-AG/mcp_pdf_reader)** — Single-PDF reader focused on simplicity.

## What's Missing

**No official Adobe MCP server.** The biggest name in PDF has no MCP presence. Adobe Acrobat's API exists but hasn't been wrapped in an MCP server — surprising given how much the AI ecosystem has grown.

**PDF creation is almost absent.** Only PDF.co (paid) and mcp-pandoc (via LaTeX) can generate PDFs. No free, open-source MCP server can create PDFs from scratch or fill forms.

**OCR is inconsistent.** MarkItDown offers it via a plugin, Docling includes it natively, but most PDF-specific servers don't support scanned documents at all. If your PDFs are scans, your options narrow quickly.

**No annotation or editing.** Every server is read-only or convert-only. No MCP server can add highlights, comments, or bookmarks to existing PDFs.

## How to Choose

**"I just need to read PDFs fast"** → [PDF Reader MCP](https://github.com/SylphxAI/pdf-reader-mcp). Fastest extraction, page selection, TypeScript, zero config. Now at v2.3.1.

**"I need to search and navigate large PDFs"** → [pdf-mcp](https://github.com/jztan/pdf-mcp). Hybrid search, intelligent caching, 8 tools, context-efficient design.

**"I need to convert many document types"** → [MarkItDown MCP](https://github.com/microsoft/markitdown). 29+ formats, one tool, massive community.

**"I have complex PDFs with tables and layouts"** → [Docling MCP](https://github.com/docling-project/docling-mcp). IBM's Heron layout model + 97.9% table accuracy preserves structure that flat extraction loses.

**"I need to convert between formats"** → [mcp-pandoc](https://github.com/vivekVells/mcp-pandoc). Bidirectional conversion powered by Pandoc.

**"I need to create/fill PDFs"** → [PDF.co MCP](https://github.com/pdfdotco/pdfco-mcp). Only option with write capabilities. Paid API.

**"I want an AI reading assistant for books"** → [eBook-MCP](https://github.com/onebirdrocks/ebook-mcp). Library management and chapter navigation for EPUB/PDF. Note: development appears dormant.

**"I need PDF security analysis"** → [PDFActionInspector](https://github.com/foxitsoftware/PDFActionInspector). JavaScript action extraction and risk assessment from Foxit.

## Rating: 3.5 / 5

The PDF/document processing MCP ecosystem covers the basics well — you can extract text from any common document format, and multiple mature options exist. Microsoft and IBM both ship official servers backed by major engineering teams. The star counts (114K for MarkItDown, 58K+ for Docling core) reflect genuine, accelerating community adoption — Docling's 58% growth in 38 days is remarkable.

The technical improvements are real: Heron brings 20-24% layout analysis improvement, PDF Reader MCP's v2.x series fixes real usability issues (path handling), and jztan/pdf-mcp introduces intelligent caching and hybrid search — the first server designed specifically for context-efficient agent workflows rather than bulk extraction.

But the category's gaps persist. PDF creation is nearly absent in the free/open-source space. OCR support is inconsistent (only Docling and jztan/pdf-mcp handle it natively among the free options). No server handles annotations or editing. The most feature-rich option (PDF.co) is a paid API wrapper. And the ecosystem remains fragmented — there are 15+ PDF MCP servers on GitHub, most doing slight variations of the same text extraction.

For reading documents: strong and getting stronger. For working with documents end-to-end: still maturing.

---

*This review reflects research conducted in March–April 2026. Star counts, version numbers, and feature availability may have changed since publication. We research MCP servers thoroughly through documentation, GitHub repositories, community discussions, and published benchmarks — [we do not test servers hands-on](/about/#our-methodology).*

*This review was last refreshed on 2026-04-22 using Claude Opus 4.6 (Anthropic).*
