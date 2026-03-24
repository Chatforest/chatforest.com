---
title: "PDF & Document Processing MCP Servers — MarkItDown, Docling, PDF Reader, and More"
date: 2026-03-15T03:12:00+09:00
description: "PDF and document processing MCP servers let AI agents extract text, convert formats, parse tables, and analyze documents across PDF, DOCX, EPUB, and 30+ file types. We reviewed 15+ servers across five approaches. Microsoft MarkItDown leads with 90,700 stars and 29+ format support. IBM's Docling MCP brings enterprise-grade layout analysis with 37,000+ stars on the core library. PDF Reader MCP is the fastest pure-PDF option with 5-10x parallel processing."
og_description: "PDF & document MCP servers: MarkItDown (90.7K stars, 29+ formats, official), Docling (508 stars, IBM-backed, layout analysis), PDF Reader MCP (557 stars, fastest extraction). 15+ servers across 5 approaches. Rating: 3.5/5."
content_type: "Review"
card_description: "PDF and document processing MCP servers across MarkItDown, Docling, PDF Reader MCP, mcp-pandoc, eBook-MCP, and PDF.co. Microsoft and IBM both ship official servers, with the ecosystem split between universal converters and PDF-specific extractors."
last_refreshed: 2026-03-15
---

Every AI workflow eventually hits the same wall: "I need to read this PDF." Document processing is one of the most universally needed MCP capabilities, and the ecosystem has responded with servers ranging from Microsoft's 90,700-star universal converter to single-purpose PDF extractors built for speed.

The headline finding: **the category is split between universal document converters and PDF-specific tools**, and neither approach has won. Microsoft's MarkItDown handles 29+ formats but treats every document the same way — convert to Markdown. IBM's Docling preserves document structure with layout analysis but requires heavier infrastructure. And the fastest pure-PDF extraction comes from a 557-star TypeScript project, not either tech giant.

**Category:** [Business & Productivity](/categories/business-productivity/)

---

## The Landscape

### Universal Document Converters

These servers handle PDF alongside dozens of other formats, converting everything to Markdown for LLM consumption.

#### Microsoft MarkItDown

| Detail | Value |
|--------|-------|
| Repository | [microsoft/markitdown](https://github.com/microsoft/markitdown) |
| Stars | ~90,700 |
| Language | Python |
| License | MIT |
| MCP Package | `markitdown-mcp` |
| Formats | 29+ (PDF, DOCX, PPTX, XLSX, HTML, CSV, JSON, XML, EPUB, images, audio, ZIP) |
| Tools | 1 (`convert_to_markdown`) |
| Transports | stdio, Streamable HTTP, SSE |
| Version | v0.1.5 (Feb 2026) |

**MarkItDown is the most popular document processing tool in the AI ecosystem by a massive margin.** At 90,700 stars with 5,400 forks and 74 contributors, it dwarfs everything else in this category combined.

The MCP server exposes a single tool — `convert_to_markdown(uri)` — that accepts any `http:`, `https:`, `file:`, or `data:` URI. That's it. One tool, 29+ formats, zero configuration decisions. The simplicity is the point: you don't choose extraction strategies or configure layout analysis. You give it a document, you get Markdown back.

**Format coverage is the broadest of any document MCP server.** PDF, Word, PowerPoint, Excel, HTML, CSV, JSON, XML, EPUB, images (with EXIF metadata and optional OCR via the `markitdown-ocr` plugin), audio (with transcription), YouTube URLs, and ZIP archives. Third-party plugins extend it further.

**The trade-offs are real.** One tool means no fine-grained control — you can't extract just page 5, or get images separately, or preserve table coordinates. PDF extraction quality depends on the underlying parser, and complex layouts (multi-column, nested tables, scanned documents) can lose structure. The MCP server has no authentication, running with the privileges of whatever user started it. And 304 open issues suggest the project is growing faster than it can resolve edge cases.

**Install is straightforward:** `pip install markitdown-mcp`, then run `markitdown-mcp` for stdio or add `--http` for remote transport. Docker is recommended for Claude Desktop integration.

#### IBM Docling MCP

| Detail | Value |
|--------|-------|
| Repository | [docling-project/docling-mcp](https://github.com/docling-project/docling-mcp) |
| Stars | ~508 |
| Core Library Stars | ~37,000 ([docling-project/docling](https://github.com/docling-project/docling)) |
| Language | Python |
| License | MIT |
| Formats | PDF, DOCX, PPTX, XLSX, HTML, images, audio, LaTeX, and more |
| Tools | Multiple (convert, generate, cache management) |
| Transports | stdio, SSE, Streamable HTTP |
| Version | v1.3.4 (Jan 2026) |

**Docling is the enterprise-grade option, backed by IBM Research and now donated to the Linux Foundation's Agentic AI Foundation.** The core Docling library has 37,000+ stars and is described by Red Hat as "the number one open source repository for document intelligence."

Where MarkItDown converts everything to flat Markdown, **Docling preserves document structure** — it outputs DoclingDocument (structured JSON) that retains layout information, table structures, reading order, and document hierarchy. This matters for complex PDFs with multi-column layouts, nested tables, headers/footers, and mixed content. The MCP server can export to Markdown too, but the structured format is the differentiator.

**Key capabilities include:** PDF conversion with advanced layout analysis (powered by IBM's Granite-Docling-258M vision-language model), table structure recovery, OCR for scanned documents, document generation, and local caching for performance. The server also supports RAG integration with Milvus.

**The weight is the trade-off.** Docling requires more infrastructure than MarkItDown — the layout analysis models need compute resources, and the full pipeline is heavier. Twenty open issues and 9 contributors on the MCP server (vs. 508 stars) suggest the MCP layer is younger than the core library. The core Docling library is battle-tested; the MCP wrapper is still maturing.

**Install via uvx:** add the entry to your MCP client config with `uvx docling-mcp-server`. Supports Claude Desktop, LM Studio, and containerized deployments.

### PDF-Specific Servers

These focus exclusively on PDF processing, trading format breadth for depth.

#### PDF Reader MCP (SylphxAI)

| Detail | Value |
|--------|-------|
| Repository | [SylphxAI/pdf-reader-mcp](https://github.com/SylphxAI/pdf-reader-mcp) |
| Stars | ~557 |
| Language | TypeScript |
| License | MIT |
| Tools | 1 (`read_pdf`) |
| Transport | stdio |
| Version | v1.3.0 |
| npm | `@sylphx/pdf-reader-mcp` |

**The fastest PDF extraction MCP server.** PDF Reader MCP claims 5-10x faster throughput than sequential processing via automatic parallelization, with benchmarks of 5,575 ops/sec for text extraction and 12,933 ops/sec for error handling. It processes 50-page PDFs in seconds with multi-core utilization.

The single `read_pdf` tool handles text extraction (full document or specific pages), image extraction as base64-encoded PNG, metadata access, and page counting. Y-coordinate based content ordering preserves natural reading order — a detail that matters for multi-column layouts where naive extraction scrambles text.

**Flexible page selection** supports ranges like "1-5,10-15,20" — something MarkItDown can't do. Per-page error isolation means a corrupted page doesn't crash the entire extraction. Supports both local files and HTTP/HTTPS URLs.

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
| Stars | ~512 |
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
| Stars | ~351 |
| Language | Python |
| License | Apache-2.0 |
| Formats | EPUB, PDF |
| Tools | Multiple (library management, metadata, TOC, chapter/page extraction) |

**Purpose-built for reading books, not processing business documents.** eBook-MCP provides library management (discover all EPUB/PDF files), metadata extraction, table of contents navigation, and chapter-by-chapter or page-by-page content extraction in Markdown format.

Multilingual documentation (English, Chinese, Japanese, Korean, French, German) suggests international community engagement. Uses PyPDF2 and PyMuPDF for PDF, ebooklib for EPUB.

**The reading experience differentiator:** while PDF Reader MCP treats PDFs as data to extract, eBook-MCP treats them as books to read — with library browsing, chapter navigation, and interactive reading sessions. For AI reading assistants and chat-based book interfaces, this is the better fit.

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

**"I just need to read PDFs fast"** → [PDF Reader MCP](https://github.com/SylphxAI/pdf-reader-mcp). Fastest extraction, page selection, TypeScript, zero config.

**"I need to convert many document types"** → [MarkItDown MCP](https://github.com/microsoft/markitdown). 29+ formats, one tool, massive community.

**"I have complex PDFs with tables and layouts"** → [Docling MCP](https://github.com/docling-project/docling-mcp). IBM's layout analysis preserves structure that flat extraction loses.

**"I need to convert between formats"** → [mcp-pandoc](https://github.com/vivekVells/mcp-pandoc). Bidirectional conversion powered by Pandoc.

**"I need to create/fill PDFs"** → [PDF.co MCP](https://github.com/pdfdotco/pdfco-mcp). Only option with write capabilities. Paid API.

**"I want an AI reading assistant for books"** → [eBook-MCP](https://github.com/onebirdrocks/ebook-mcp). Library management and chapter navigation for EPUB/PDF.

**"I need PDF security analysis"** → [PDFActionInspector](https://github.com/foxitsoftware/PDFActionInspector). JavaScript action extraction and risk assessment from Foxit.

## Rating: 3.5 / 5

The PDF/document processing MCP ecosystem covers the basics well — you can extract text from any common document format, and multiple mature options exist. Microsoft and IBM both ship official servers backed by major engineering teams. The star counts (90K+ for MarkItDown, 37K+ for Docling core) reflect genuine community adoption, not hype.

But the category has clear gaps. PDF creation is nearly absent in the free/open-source space. OCR support is inconsistent. No server handles annotations or editing. The most feature-rich option (PDF.co) is a paid API wrapper. And the ecosystem is fragmented — there are 15+ PDF MCP servers on GitHub, most doing slight variations of the same text extraction, with no coordination or consolidation.

For reading documents: strong. For working with documents end-to-end: still maturing.

---

*This review reflects research conducted in March 2026. Star counts, version numbers, and feature availability may have changed since publication. We research MCP servers thoroughly through documentation, GitHub repositories, community discussions, and published benchmarks — we do not test servers hands-on.*

*This review was last edited on 2026-03-16 using Claude Opus 4.6 (Anthropic).*
