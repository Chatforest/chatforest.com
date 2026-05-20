# PDF & Document Processing MCP Servers — MarkItDown, Docling, PDF Reader, and More

> PDF and document processing MCP servers let AI agents extract text, convert formats, parse tables, and analyze documents across PDF, DOCX, EPUB, and 30+ file types.


Every AI workflow eventually hits the same wall: "I need to read this PDF." Document processing is one of the most universally needed MCP capabilities, and the ecosystem has responded with servers ranging from Microsoft's 124,000-star universal converter to single-purpose PDF extractors built for speed.

The headline finding this cycle: **Adobe finally shipped an official MCP server** — filling the biggest gap we flagged in our last review. Adobe's MCP covers Acrobat PDF generation, form filling, contract automation, and signed PDF export, all via the Developer Console credentials. The category's most glaring omission is gone.

**Docling MCP v2.0.0 (May 19, 2026) is a breaking architectural shift** — from local-only to remote-first. The default mode now connects to Docling Serve instead of downloading models locally, cutting the package size 90% (500MB → 50MB). Local mode is still available. The core Docling library reached v2.94.0 with Granite Vision 4.1, TikZ rendering, and multi-lingual OCR via kserve-triton. **MarkItDown crossed 124,000 stars** with no new core release but its OCR plugin (v0.1.0, March 2026) is now the recommended path for scanned documents.

**Security alert: SSRF affects 36.7% of MCP servers — including MarkItDown MCP.** BlueRock scanned 7,000 publicly accessible MCP servers and found over a third accept arbitrary URLs including cloud metadata endpoints. PDF MCP servers are especially exposed because they commonly fetch remote PDFs by URL. jztan/pdf-mcp fixed its SSRF exposure in v1.9.0; MarkItDown MCP's exposure is unpatched as of this writing. Prompt injection via malicious PDF content is a separate systemic risk.

**jztan/pdf-mcp** jumped from v1.7.0 to v1.12.1 with six releases — adding section-level search, configurable embedding models (BYOM), and security hardening. PyPI downloads roughly doubled to 13,800 in ~six weeks. **PDF Reader MCP** reached v2.4.0 at 715 stars. New entrant **PDFMux** routes each PDF page to the best extraction backend automatically, with a built-in MCP server at 64 stars.

**Category:** [Business & Productivity](/categories/business-productivity/)

---

## The Landscape

### Universal Document Converters

These servers handle PDF alongside dozens of other formats, converting everything to Markdown for LLM consumption.

#### Microsoft MarkItDown

| Detail | Value |
|--------|-------|
| Repository | [microsoft/markitdown](https://github.com/microsoft/markitdown) |
| Stars | ~124,000 |
| Forks | ~7,400 |
| Language | Python |
| License | MIT |
| MCP Package | `markitdown-mcp` |
| Formats | 29+ (PDF, DOCX, PPTX, XLSX, HTML, CSV, JSON, XML, EPUB, images, audio, ZIP) |
| Tools | 1 (`convert_to_markdown`) |
| Transports | stdio, Streamable HTTP, SSE |
| Version | v0.1.5 (Feb 2026) |
| OCR Plugin | `markitdown-ocr` v0.1.0 (Mar 2026) |

**MarkItDown is the most popular document processing tool in the AI ecosystem by a massive margin.** At 124,000 stars with 7,400 forks, it dwarfs everything else in this category combined. The +10K star gain since April reflects continued institutional adoption rather than viral spikes.

The MCP server exposes a single tool — `convert_to_markdown(uri)` — that accepts any `http:`, `https:`, `file:`, or `data:` URI. That's it. One tool, 29+ formats, zero configuration decisions. The simplicity is the point: you don't choose extraction strategies or configure layout analysis. You give it a document, you get Markdown back.

**Format coverage is the broadest of any document MCP server.** PDF, Word, PowerPoint, Excel, HTML, CSV, JSON, XML, EPUB, images (with EXIF metadata and optional OCR via the `markitdown-ocr` plugin), audio (with transcription), YouTube URLs, and ZIP archives. The `markitdown-ocr` plugin (v0.1.0, March 2026) adds LLM Vision-based OCR for scanned PDFs, DOCX, PPTX, and XLSX — using the same `llm_client`/`llm_model` pattern as the core library, requiring no additional ML dependencies. This is now the recommended path for scanned document handling.

**Security concern: MarkItDown MCP is vulnerable to SSRF.** BlueRock's independent scan of 7,000 MCP servers confirmed MarkItDown MCP accepts arbitrary URLs including cloud metadata endpoints (e.g., `http://169.254.169.254/latest/meta-data/`). This is unpatched as of May 2026. Do not expose MarkItDown MCP on untrusted networks without URL filtering at the infrastructure layer.

**The other trade-offs persist.** One tool means no fine-grained control — you can't extract just page 5, or get images separately, or preserve table coordinates. PDF extraction quality depends on the underlying parser, and complex layouts (multi-column, nested tables) can lose structure. No new core release since February — the MCP server layer is stable but not rapidly iterating. Now listed in the official MCP Registry and indexed on CopilotHub (discoverable via GitHub Copilot and VS Code).

**Install is straightforward:** `pip install markitdown-mcp`, then run `markitdown-mcp` for stdio or add `--http` for remote transport. Docker is recommended for Claude Desktop integration.

#### IBM Docling MCP

| Detail | Value |
|--------|-------|
| Repository | [docling-project/docling-mcp](https://github.com/docling-project/docling-mcp) |
| Stars | ~620 |
| Forks | ~114 |
| Core Library Stars | ~60,000 ([docling-project/docling](https://github.com/docling-project/docling)) |
| Core Library Forks | ~4,000 |
| Language | Python |
| License | MIT |
| Formats | PDF, DOCX, PPTX, XLSX, HTML, images, audio, LaTeX, WebVTT, and more |
| Tools | Multiple (convert, generate, cache management) |
| Transports | stdio, SSE, Streamable HTTP |
| MCP Version | **v2.0.0 (May 19, 2026) — breaking** |
| Core Version | v2.94.0 (May 18, 2026) |

**Docling is the enterprise-grade option, backed by IBM Research and donated to the Linux Foundation's Agentic AI Foundation.** The core Docling library reached 60,000 stars and continues to be described by Red Hat as "the number one open source repository for document intelligence."

**Docling MCP v2.0.0 (May 19, 2026) is a breaking architectural pivot.** The default mode now connects to a remote Docling Serve API instead of downloading and running models locally. The result: **90% package size reduction** (500MB → ~50MB base package, no model downloads). Local mode remains available via the `[local]` install extra, with optional automatic fallback from remote to local. Users upgrading from v1.x must consult `MIGRATION_v2.md`. GitHub Private Vulnerability Reporting is now enabled in the security docs.

This shift matters for cloud-hosted agent workflows — Docling MCP can now run in environments where 500MB model downloads were previously impractical. It also lowers the barrier for developers evaluating the server before committing to local infrastructure.

Where MarkItDown converts everything to flat Markdown, **Docling preserves document structure** — it outputs DoclingDocument (structured JSON) that retains layout information, table structures, reading order, and document hierarchy. The MCP server can export to Markdown too, but the structured format is the differentiator for complex PDFs.

**Core library rapid iteration continues:** v2.91.0 (VML image extraction from DOCX), v2.92.0 (multi-lingual OCR via kserve-triton, modular `docling-slim` package), v2.93.0 (Granite Vision 4.1 for table and chart analysis), v2.94.0 (LaTeX TikZ rendering via Tectonic, threaded layout model with staged HuggingFace downloads, gRPC round-robin scheduling). The Heron layout model (20.6-23.9% mAP improvement) and 97.9% table extraction accuracy from Granite-Docling-258M remain the accuracy anchors.

**Install via uvx:** `uvx docling-mcp-server`. Supports Claude Desktop, LM Studio, and containerized deployments. In remote-first mode, no local GPU or model downloads required.

### PDF-Specific Servers

These focus exclusively on PDF processing, trading format breadth for depth.

#### PDF Reader MCP (SylphxAI)

| Detail | Value |
|--------|-------|
| Repository | [SylphxAI/pdf-reader-mcp](https://github.com/SylphxAI/pdf-reader-mcp) |
| Stars | ~715 |
| Forks | ~66 |
| Language | TypeScript |
| License | MIT |
| Tools | 1 (`read_pdf`) |
| Transport | stdio |
| Version | v2.4.0 (May 3, 2026) |
| npm | `@sylphx/pdf-reader-mcp` |

**The fastest PDF extraction MCP server, now at v2.4.0.** PDF Reader MCP claims 5-10x faster throughput than sequential processing via automatic parallelization, with benchmarks of 5,575 ops/sec for text extraction and 12,933 ops/sec for error handling. Stars have grown from 657 to 715 (+58 since April). Active release cadence continues — v2.4.0 dropped May 3, two weeks after v2.3.1.

The single `read_pdf` tool handles text extraction (full document or specific pages), image extraction as base64-encoded PNG, metadata access, and page counting. Y-coordinate based content ordering preserves natural reading order — a detail that matters for multi-column layouts where naive extraction scrambles text.

**Flexible page selection** supports ranges like "1-5,10-15,20" — something MarkItDown can't do. Per-page error isolation means a corrupted page doesn't crash the entire extraction. Supports both local files and HTTP/HTTPS URLs. The v2.x series added absolute path support on both Windows and Unix, configurable working directory via `cwd` for relative path resolution, and improved Zod validation error handling.

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
| Stars | ~38 |
| Language | Python |
| License | MIT |
| Tools | 8 (`pdf_info`, `pdf_search`, `pdf_read_pages`, `pdf_read_all`, `pdf_render_pages`, `pdf_get_toc`, `pdf_cache_stats`, `pdf_cache_clear`) |
| Transport | stdio |
| Version | v1.12.1 (May 12, 2026) |
| PyPI | `pdf-mcp` (13,800+ downloads) |

**Rapid iteration: six releases from v1.7.0 to v1.12.1 in less than six weeks, and PyPI downloads nearly doubled from 7,100 to 13,800.** jztan/pdf-mcp is designed for context efficiency rather than raw speed — where PDF Reader MCP extracts everything fast, this server gives agents "surgical access to PDFs instead of flooding context with raw text."

Eight dedicated tools cover the full read workflow: inspect document structure and text coverage, search by keyword or semantically, read specific pages with optional OCR and image rendering, extract full documents (capped at 50 pages by default), render pages as PNG for vision models, and retrieve table of contents.

**New capabilities in the review window:**
- **v1.10.0**: Section-level search — heuristic detection of document sections for more precise results
- **v1.11.0**: Configurable embedding models (BYOM — Bring Your Own Model) instead of fixed embedding
- **v1.12.0/1.12.1**: Fixed hybrid search schema issues, tokenized keyword queries, corrected `total_matches` reporting

**Security hardening is ahead of most PDF MCP servers.** The author Kevin Tan published a self-audit finding 8 vulnerabilities and fixed all of them — SSRF via unconstrained URL fetching (the same flaw confirmed across 36.7% of MCP servers), prompt injection via malicious PDF content, path traversal, resource exhaustion, and weak MD5 cache hashing. Current versions (v1.9.0+) include SSRF protection, access control lists, HTTPS-only remote requests, and per-page text coverage metadata.

**Growing but still niche:** at 38 stars, this remains a specialist tool. But the approach — caching, hybrid search, section-level reading, security-first design — is more sophisticated than its star count suggests.

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
| Stars | ~537 |
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
| Stars | ~366 |
| Forks | ~50 |
| Language | Python |
| License | Apache-2.0 |
| Formats | EPUB, PDF |
| Tools | Multiple (library management, metadata, TOC, chapter/page extraction) |

**Purpose-built for reading books, not processing business documents.** eBook-MCP provides library management (discover all EPUB/PDF files), metadata extraction, table of contents navigation, and chapter-by-chapter or page-by-page content extraction in Markdown format.

Multilingual documentation (English, Chinese, Japanese, Korean, French, German) suggests international community engagement. Uses PyPDF2 and PyMuPDF for PDF, ebooklib for EPUB.

**The reading experience differentiator:** while PDF Reader MCP treats PDFs as data to extract, eBook-MCP treats them as books to read — with library browsing, chapter navigation, and interactive reading sessions. For AI reading assistants and chat-based book interfaces, this is the better fit.

**Development has stalled.** The last code commit was September 7, 2025 (a documentation typo fix) — no code activity in 8+ months, no formal releases ever. Stars ticked from 358 to 366, but the project is effectively archived in practice.

### Adobe MCP — NEW

| Detail | Value |
|--------|-------|
| Package | `npx -y @adobe/mcp` |
| Docs | developer.adobe.com/mcp |
| Auth | Adobe Developer Console credentials |

**The biggest gap in this category is now filled.** Adobe — the company that invented PDF — has shipped an official MCP server covering Acrobat, Photoshop, and Experience Cloud. PDF-specific capabilities: generate and manage PDFs, automate contract and invoice generation, populate Acrobat form templates, and export signed PDFs.

Requires API credentials from the Adobe Developer Console. Cloud API-based, not local processing. Also available via:
- **Adobe PDF Services MCP** (via Pipedream): cloud create/convert/OCR
- **Adobe Acrobat Sign MCP**: e-signature and digital signing workflows

**PDF form filling and PDF creation from scratch are now available in a free tier** — the gap we flagged in our last review. Adobe's free tier limits apply, but the capability exists without paying for PDF.co.

### PDFMux (NameetP/pdfmux) — NEW

| Detail | Value |
|--------|-------|
| Repository | [NameetP/pdfmux](https://github.com/NameetP/pdfmux) |
| Stars | ~64 |
| Language | Python |
| Version | v1.5.0 |
| PyPI | `pdfmux` |

**A "universal PDF extraction orchestrator" that routes each page to the best available backend.** Rather than applying one extraction strategy to the whole document, PDFMux classifies each page by content type (text, tables, images, formulas, headers) and routes to the best of five rule-based extractors. Pages that fail extraction get a BYOK LLM fallback.

Built-in MCP server: `pdfmux serve` for stdio (Claude Desktop/Cursor) or `pdfmux serve --http 8080` for remote. The API is frozen — code won't break on updates. Also supports CLI, Python API, LangChain, and LlamaIndex integrations.

Still early at 64 stars, but the per-page routing philosophy is novel and addresses a real problem: documents with mixed content types (text pages, chart pages, scanned pages) where a single extraction strategy fails some pages.

### Other Notable Servers

**[kgand/document-parser-mcp](https://github.com/kgand/document-parser-mcp)** — Lightweight universal ingestion using Docling under the hood. Supports PDFs, Office documents, images, audio. Advanced layout analysis and table recovery. Good if you want Docling's capabilities without managing the full Docling MCP setup.

**[hanweg/mcp-pdf-tools](https://github.com/hanweg/mcp-pdf-tools)** — PDF manipulation (merge, split, extract pages) rather than content extraction. Complements the readers above.

**AWS Document Loader MCP** (awslabs collection) — Supports PDF (via pdfplumber), Word, Excel, PowerPoint, and images. Includes `DOCUMENT_BASE_DIR` security sandboxing and 50MB file size limit.

**[xraywu/mcp-pdf-extraction-server](https://github.com/xraywu/mcp-pdf-extraction-server)** — Basic PDF text extraction with OCR support for scanned documents. Fixes specifically for Claude Code CLI compatibility.

**[BACH-AI-Tools/pdf-reader-mcp](https://github.com/BACH-AI-Tools/pdf-reader-mcp)** — Another PDF reader implementation, simpler than SylphxAI's version.

**[Safe-Swiss-Cloud-AG/mcp_pdf_reader](https://github.com/Safe-Swiss-Cloud-AG/mcp_pdf_reader)** — Single-PDF reader focused on simplicity.

## What's Missing

**~~No official Adobe MCP server.~~** Fixed — Adobe shipped an official MCP server with Acrobat integration. PDF generation, form filling, and contract automation are now available.

**PDF annotation and editing remains absent.** Every server is read-only or convert-only. No MCP server can add highlights, comments, or bookmarks to existing PDFs. You can generate or fill forms (via Adobe), but you can't annotate existing documents.

**OCR is still inconsistent.** MarkItDown now has an OCR plugin, Docling includes it natively, jztan/pdf-mcp supports it in v1.9.0+, and PDFMux routes to OCR per-page. But PDF Reader MCP (the most popular PDF-specific option) still has no OCR support. If your PDFs are scans, your options remain narrower than for digital text PDFs.

**Security is a systemic concern.** BlueRock's scan found 36.7% of MCP servers vulnerable to SSRF. PulseMCP now lists 212+ PDF-related MCP servers — most with minimal security review. Prompt injection via malicious PDF content is under-documented across the ecosystem. Organizations deploying PDF MCP servers should audit URL fetching behavior before connecting to untrusted document sources.

## How to Choose

**"I just need to read PDFs fast"** → [PDF Reader MCP](https://github.com/SylphxAI/pdf-reader-mcp). Fastest extraction, page selection, TypeScript, zero config. Now at v2.4.0.

**"I need to search and navigate large PDFs"** → [pdf-mcp](https://github.com/jztan/pdf-mcp). Hybrid search, intelligent caching, section-level search, configurable embeddings. v1.12.1. Security-hardened.

**"I have a mixed document (text + charts + scans on different pages)"** → [PDFMux](https://github.com/NameetP/pdfmux). Per-page routing to the best extractor, with LLM fallback for failures.

**"I need to convert many document types"** → [MarkItDown MCP](https://github.com/microsoft/markitdown). 29+ formats, one tool, massive community. Add `markitdown-ocr` for scanned documents. Note: SSRF vulnerability unpatched — filter URLs at infrastructure level.

**"I have complex PDFs with tables and layouts"** → [Docling MCP](https://github.com/docling-project/docling-mcp). IBM's Heron layout model + 97.9% table accuracy preserves structure that flat extraction loses. v2.0.0 now remote-first — no local GPU required.

**"I need to convert between formats"** → [mcp-pandoc](https://github.com/vivekVells/mcp-pandoc). Bidirectional conversion powered by Pandoc.

**"I need to create/fill PDFs"** → [Adobe MCP](https://developer.adobe.com/mcp). Official Adobe Acrobat integration — PDF generation, form templates, contracts, signed PDF export. Free tier available.

**"I want an AI reading assistant for books"** → [eBook-MCP](https://github.com/onebirdrocks/ebook-mcp). Library management and chapter navigation for EPUB/PDF. Note: development stalled as of September 2025.

**"I need PDF security analysis"** → [PDFActionInspector](https://github.com/foxitsoftware/PDFActionInspector). JavaScript action extraction and risk assessment from Foxit.

## Rating: 4.0 / 5

The PDF/document processing MCP ecosystem closed its biggest gap this cycle. Adobe's official MCP server is the headline: PDF generation, form filling, contracts, and signed PDFs are now accessible without a paid third-party API. That fills the "PDF creation is absent" criticism from our last review. Microsoft and IBM continue to back the two dominant universal converters (MarkItDown at 124K stars, Docling core at 60K). Adobe now makes three major enterprise vendors in the space.

**Docling MCP v2.0.0's remote-first pivot** is a meaningful architectural improvement — dropping the install from 500MB to ~50MB opens Docling to cloud-hosted agent workflows that previously couldn't absorb the local model requirements. Combined with four core library releases in the review window (Granite Vision 4.1, TikZ, multi-lingual OCR, gRPC scheduling), Docling's technical depth continues to widen its lead on complex document understanding.

**The security picture is concerning.** BlueRock's ecosystem-wide SSRF finding — 36.7% of MCP servers vulnerable, including MarkItDown MCP — is the clearest signal yet that the MCP ecosystem is building faster than it's hardening. jztan/pdf-mcp self-audited and fixed eight vulnerabilities; MarkItDown MCP's SSRF remains open. Prompt injection via malicious PDF content is a systemic risk that none of the servers address at the protocol level.

**The fragmentation problem is real.** PulseMCP now lists 212+ PDF-related MCP servers — most doing slight variations of the same text extraction with minimal security review. The proliferation makes discovery harder without meaningfully expanding capability coverage. PDFMux's per-page routing and jztan/pdf-mcp's section-level search are genuine architectural innovations; most of the 212 are not.

For reading documents: strong and hardening unevenly. For working with documents end-to-end: meaningfully improved, with annotation still the remaining gap.

---

*This review reflects research conducted in March–May 2026. Star counts, version numbers, and feature availability may have changed since publication. We research MCP servers thoroughly through documentation, GitHub repositories, community discussions, and published benchmarks — [we do not test servers hands-on](/about/#our-methodology).*

*This review was last refreshed on 2026-05-20 using Claude Sonnet 4.6 (Anthropic).*

