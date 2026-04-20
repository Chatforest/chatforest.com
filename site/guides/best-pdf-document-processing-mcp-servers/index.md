# Best PDF & Document Processing MCP Servers in 2026 — MarkItDown vs Docling vs Pandoc vs Dedicated PDF Tools

> We compared 25+ PDF and document processing MCP servers across multi-format converters, dedicated PDF readers, PDF manipulation tools, Word document servers, and cloud APIs.


Document processing is one of the most immediately useful MCP capabilities. Converting PDFs to text, extracting tables, transforming between formats — these are tasks that come up constantly when working with AI assistants. The ecosystem has responded with servers ranging from simple PDF readers to comprehensive multi-format conversion suites.

The landscape splits six ways. **Multi-format converters** like MarkItDown and Docling handle dozens of input formats and output clean Markdown. **Dedicated PDF readers** focus on fast, accurate text extraction with features like caching and parallel processing. **Format converters** use Pandoc or custom pipelines for bidirectional document transformation. **PDF manipulation tools** handle merging, splitting, watermarking, and OCR. **Word document servers** provide full DOCX creation and editing. And **cloud API wrappers** connect to services like Unstructured and PDF.co for heavy processing.

What surprised us: **Microsoft's MarkItDown** (91.4K stars) and IBM's **Docling** (56.2K stars) dwarf everything else in the space — their parent libraries are among the most popular open-source projects on GitHub. Meanwhile, the dedicated PDF MCP servers are fragmented with dozens of small projects, none breaking 1K stars. And **Word document manipulation** is an underserved niche with only one serious contender.

**Disclosure:** Our recommendations are based on research — analyzing documentation, GitHub repositories, community feedback, and published benchmarks. We have not hands-on tested every server in this guide.

## At a Glance: Top Picks

| Category | Our pick | Stars | Runner-up |
|----------|----------|-------|-----------|
| **Multi-format (to Markdown)** | [microsoft/markitdown-mcp](https://github.com/microsoft/markitdown/tree/main/packages/markitdown-mcp) | 91.4K (mono) | [zcaceres/markdownify-mcp](https://github.com/zcaceres/markdownify-mcp) (2,500) |
| **Multi-format (AI-powered)** | [docling-project/docling-mcp](https://github.com/docling-project/docling-mcp) | 522 | — |
| **Format conversion (Pandoc)** | [vivekVells/mcp-pandoc](https://github.com/vivekVells/mcp-pandoc) | 517 | [Tele-AI/doc-ops-mcp](https://github.com/Tele-AI/doc-ops-mcp) (138) |
| **Dedicated PDF reader** | [SylphxAI/pdf-reader-mcp](https://github.com/SylphxAI/pdf-reader-mcp) | 571 | [jztan/pdf-mcp](https://github.com/jztan/pdf-mcp) (9) |
| **PDF manipulation** | [gufao/mcp-server-stirling-pdf](https://github.com/gufao/mcp-server-stirling-pdf) | 1 | [Tele-AI/doc-ops-mcp](https://github.com/Tele-AI/doc-ops-mcp) (138, watermark/QR) |
| **Word documents** | [GongRzhe/Office-Word-MCP-Server](https://github.com/GongRzhe/Office-Word-MCP-Server) | 1,800 | — |
| **Cloud API (enterprise)** | [Unstructured-IO/UNS-MCP](https://github.com/Unstructured-IO/UNS-MCP) | 42 | [pdfdotco/pdfco-mcp](https://github.com/pdfdotco/pdfco-mcp) (9) |
| **AWS ecosystem** | [awslabs/document-loader-mcp-server](https://github.com/awslabs/mcp/tree/main/src/document-loader-mcp-server) | Official | — |

## Multi-Format Converters

The heavyweights of document processing. These servers handle many input formats and convert everything to Markdown — the format LLMs understand best.

### microsoft/markitdown-mcp — The Winner

**Stars:** 91,400 (monorepo) | **Language:** Python | **License:** MIT

Microsoft's MarkItDown is the dominant document-to-Markdown conversion tool. The MCP server wraps it in a single, clean tool.

**What makes it stand out:**
- **29+ input formats** — PDF, Word, PowerPoint, Excel, HTML, images (with EXIF/OCR), audio (with transcription), CSV, JSON, XML, ZIP, EPub, YouTube URLs
- **Single tool: `convert_to_markdown(uri)`** — accepts http:, https:, file:, and data: URIs. Simple and predictable
- **Three transport protocols** — STDIO (default), Streamable HTTP, and SSE. Most MCP servers only support STDIO
- **Docker-first deployment** — recommended approach for Claude Desktop integration, with volume mounting for local file access
- **Structure preservation** — headings, lists, tables, and links are maintained in the Markdown output
- **Plugin system** — OCR via LLM vision, Azure Document Intelligence integration
- **v0.1.5** — released February 2026. Active development by Microsoft's AutoGen team

**Limitations:**
- Single tool means no search, no caching, no page-level control — you convert the whole document
- OCR requires additional plugin configuration (LLM vision or Azure DI)
- Docker recommended means slightly heavier setup than pip-based servers
- Output quality varies by format — PDFs with complex layouts can lose structure

**Best for:** Most developers who need to feed documents into LLMs. The 91K-star ecosystem, Microsoft backing, and format breadth make this the default starting point.

### zcaceres/markdownify-mcp — The Multi-Tool Alternative

**Stars:** 2,500 | **Language:** TypeScript | **License:** MIT

Where MarkItDown has one tool, markdownify-mcp has ten — each specialized for a different input type.

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

### docling-project/docling-mcp — AI-Powered Layout Understanding

**Stars:** 522 (MCP server) / 56,200 (Docling library) | **Language:** Python | **License:** MIT

Docling is IBM's document processing library, now in the Linux Foundation. The MCP server brings its advanced PDF understanding to AI agents.

**What makes it stand out:**
- **Advanced PDF layout analysis** — page layout detection, reading order analysis, and table structure recognition using AI models. This is the key differentiator from MarkItDown
- **Docling library** (56.2K stars) — one of the most popular document processing libraries globally, backed by IBM Research
- **Broad format support** — PDF, DOCX, PPTX, XLSX, HTML, images, audio (WAV/MP3), LaTeX, plain text, even USPTO patents and XBRL financial reports
- **RAG integration** — built-in Milvus upload and retrieval for retrieval-augmented generation workflows
- **DoclingDocument format** — structured JSON output that preserves document semantics, not just text
- **Visual Language Model support** — GraniteDocling for vision-based document understanding
- **v1.3.4** — released January 2026. Actively developed

**Limitations:**
- Heavier dependencies than MarkItDown — requires AI models for layout analysis
- Slower processing — the layout analysis adds overhead compared to simple text extraction
- Fewer MCP-specific features (no caching, no search tools)
- Python 3.10+ required

**Best for:** Documents with complex layouts — scientific papers, financial reports, multi-column PDFs, and anything where reading order and table structure matter. If MarkItDown's output is garbled, try Docling.

## Format Converters

These servers focus on bidirectional format conversion — not just extracting content, but creating documents in various formats.

### vivekVells/mcp-pandoc — The Winner

**Stars:** 517 | **Language:** Python | **License:** MIT

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

**Stars:** 571 | **Language:** TypeScript | **License:** MIT

The most popular dedicated PDF reading MCP server. Built for speed with parallel processing.

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

**Stars:** 9 | **Language:** Python | **License:** MIT

Low stars but high quality — this server has features the more popular alternatives lack.

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

### GongRzhe/Office-Word-MCP-Server — The Only Serious Option

**Stars:** 1,800 | **Language:** Python | **License:** Not specified

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

**Stars:** 42 | **Language:** Python | **License:** Not specified

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

**Start with MarkItDown** if you need general document-to-Markdown conversion. It handles 29+ formats, has 91K stars of community validation, and the single `convert_to_markdown` tool is dead simple.

**Switch to Docling** if MarkItDown's output is garbled — complex layouts, multi-column PDFs, scientific papers, or financial reports. Docling's AI-powered layout analysis handles these better, at the cost of speed.

**Add a dedicated PDF reader** (pdf-reader-mcp or pdf-mcp) if you work with PDFs frequently and need caching, search, or page-level control that the multi-format converters don't offer.

**Add mcp-pandoc** if you need to create documents — generating PDFs, DOCX, or EPUB from Markdown. MarkItDown and Docling are input-focused; Pandoc handles output.

**Use Office-Word-MCP-Server** if you need to create or edit Word documents with full formatting control.

**Consider cloud APIs** (Unstructured, PDF.co) only if you need enterprise-scale pipelines or comprehensive PDF manipulation beyond what local tools provide.

## Three Trends Worth Watching

**1. The library giants dominate.** MarkItDown (91.4K stars) and Docling (56.2K stars) aren't MCP-native projects — they're massive document processing libraries that added MCP servers as a feature. This means the MCP servers inherit years of development and testing, but also that MCP-specific features (caching, search, pagination) are afterthoughts. Dedicated PDF MCP servers fill these gaps.

**2. Read vs. write remains split.** No single server handles both document reading and document creation well. MarkItDown and Docling extract content; Pandoc and doc-ops-mcp create documents. The Word server is the exception — it both reads and writes — but only for DOCX. Expect this gap to close as servers mature.

**3. PDF manipulation is underserved.** Despite PDF being the most common document format, MCP servers for merging, splitting, compressing, and annotating PDFs barely exist. Stirling PDF (the underlying tool) has 56K stars, but the MCP wrapper has 1 star. This is a clear gap waiting to be filled.

## What's Missing

- **No official Adobe MCP server** — Adobe Acrobat has the most comprehensive PDF API in the world, but no MCP integration
- **No official Microsoft Office MCP server for documents** — Word, PowerPoint reading/writing through Microsoft's own MCP catalog is absent (Excel has some coverage via Copilot)
- **No Apple iWork support** — no Pages, Keynote, or Numbers MCP servers
- **No PDF form filling** — most servers extract form data but can't fill forms (PDF.co is the exception)
- **Limited table extraction** — most servers struggle with complex tables. Docling is best here but still imperfect
- **No PDF comparison/diff** — comparing two versions of a document is a common need with no MCP solution
- **No digital signature support** — signing PDFs or verifying signatures isn't available in any server

