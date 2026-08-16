---
title: "OCR & Document Intelligence MCP Servers — PaddleOCR, MinerU, Docling, Marker, Mistral OCR, and More"
date: 2026-03-19T15:30:00+09:00
description: "OCR and document intelligence MCP servers let AI agents extract text from images, scanned PDFs, handwritten notes, and complex layouts."
og_description: "OCR MCP servers: PaddleOCR (official, 77K parent stars, 4 tools), MinerU (61.7K stars, highest PulseMCP traffic at May 2026 refresh), Docling (59K stars, Red Hat official MCP), Markdownify (2.6K stars, 10 tools), Mistral OCR MCP, ocr-mcp (10+ engines). Major cloud vendor gaps persist. Rating: 3.5/5."
content_type: "Review"
card_description: "OCR and document intelligence MCP servers across PaddleOCR, MinerU, Docling, Markdownify, Mistral OCR, and more. PaddleOCR and MinerU are the standout official servers; Docling has exploded to 59K stars. Major cloud vendors (Google Cloud Vision, AWS Textract, Azure) still absent."
last_refreshed: 2026-08-16
sources_audited: 2026-08-16
---

Every AI workflow that touches the physical world eventually needs OCR. Scanned contracts, handwritten notes, screenshots, receipts, whiteboards — if it's an image with text, you need a way to extract that text for an LLM to work with.

This review covers MCP servers specifically built for **optical character recognition and document intelligence** — extracting text from images and scanned documents where the text isn't already digital. For MCP servers that process digital PDFs, DOCX, and other native document formats, see our [PDF & Document Processing review](/reviews/pdf-document-mcp-servers/). There's overlap (Docling and MarkItDown both have OCR capabilities), but the servers here are purpose-built for recognition tasks.

The headline after 44 days: **the ecosystem is meaningfully stronger at the top**. PaddleOCR's MCP server doubled its tool count from 2 to 4 and added VLM-based models. MinerU — a 61,700-star document intelligence library — launched an official MCP server that had become the most-visited OCR server on PulseMCP as of that refresh (see the correction in the MinerU section below for current traffic, which has since dropped substantially). Docling grew from 35,000 to 59,000 stars with a flurry of releases. The major cloud vendor gap (Google Cloud Vision, AWS Textract, Azure Document Intelligence) remains open as of this audit.

**Category:** [Business & Productivity](/categories/business-productivity/)

---

## Official Vendor & Library Servers

### MinerU MCP (OpenDataLab) — Highest PulseMCP Traffic at May 2026 Refresh

| Detail | Info |
|--------|------|
| [opendatalab/MinerU](https://github.com/opendatalab/MinerU) | ~61,700 stars (~77,700 as of this audit) |
| License | [MinerU Open Source License](https://github.com/opendatalab/MinerU/releases/tag/mineru-3.1.0-released) — Apache-2.0-based, relicensed from AGPLv3 in v3.1.0 (April 17, 2026) |
| Language | Python / TypeScript / Go SDKs |
| Formats | PDF, DOCX, PPTX, XLSX → Markdown, JSON, HTML, LaTeX |
| PulseMCP weekly | ~1,200 at May 2026 refresh (see correction below) |

MinerU arrived on PulseMCP on March 18, 2026 — one day before the original version of this review was published — and had, as of the May 2026 refresh, become the most-visited OCR/document intelligence MCP server in the directory. The parent library's 61,700 stars (now ~77,700, per GitHub) make it the second most-starred OCR-adjacent project after PaddleOCR, and it focuses specifically on high-fidelity document-to-Markdown conversion at a level of accuracy that rivals commercial services.

**Correction (2026-08-16 audit):** the ~1,200 weekly-visitor figure above was accurate at the May 2026 refresh, shortly after MinerU's official MCP server launched. [PulseMCP's live listing](https://www.pulsemcp.com/servers/mineru) now shows roughly 122 weekly visitors, 622 total estimated visitors, and a #3,407 overall popularity rank as of this audit — a large drop consistent with an initial post-launch traffic spike fading, not a data error on our part. We can no longer independently confirm MinerU holds the highest PulseMCP traffic among OCR servers today; treat "most-visited" and "highest-traffic" language on this page as describing the May 2026 snapshot, not a current-state claim. Separately, the license row above has also been corrected: MinerU did not move to plain Apache-2.0, but to a custom "[MinerU Open Source License](https://github.com/opendatalab/MinerU/blob/master/LICENSE.md)" that is Apache-2.0-based but requires a separate commercial license from OpenDataLab once a deployment exceeds 100 million monthly active users or $20M/month in revenue.

### What Works Well

**Breadth of input formats.** PDF, DOCX, PPTX, and XLSX all convert natively to Markdown, JSON, or HTML. Native DOCX/PPTX/XLSX support was added in v3.0.0 (March 29) and v3.1.0 (April 17). Prior versions handled PDFs only.

**Multiple inference backends.** MinerU supports three modes — `pipeline` (lightweight), `hybrid-engine` (balanced), `vlm-engine` (highest accuracy). The VLM engine uses MinerU2.5-Pro-2604-1.2B, and the overall [MinerU pipeline achieved 86.2% on OmniDocBench v1.5](https://github.com/opendatalab/MinerU) (v3.0.0). Formula preservation (LaTeX output), chart handling, and table extraction are all addressed in dedicated pipeline stages.

**Multiple deployment options.** CLI, REST API, Docker, Gradio WebUI, and official SDKs for Python, Go, and TypeScript. This is infrastructure designed for production document processing, not just a weekend wrapper.

**Fast iteration.** Seven releases between March 29 and April 28 (v3.0.0 through v3.1.6), covering AMD/Ascend NPU support, timeout handling, DOCX/PPTX chart fixes, and office document bugs. Release cadence has continued since: as of this audit the project is up to the 3.4.x series (stable) with a 4.0.0 alpha in progress. The [April 17 relicensing from AGPLv3 to the MinerU Open Source License](https://github.com/opendatalab/MinerU/releases/tag/mineru-3.1.0-released) removes a significant license friction point for most users (see correction above on the license terms).

### What Doesn't Work Well

**Heavy infrastructure.** MinerU is not a lightweight tool. The VLM engine downloads a 1.2B-parameter model. The REST API deployment via Docker is the most practical MCP integration path.

**Young MCP layer.** The MCP server integration is newer than the underlying library. Documentation on the MCP-specific tools is less complete than the REST API and CLI documentation.

---

### PaddleOCR MCP (Baidu/PaddlePaddle)

| Detail | Info |
|--------|------|
| [PaddlePaddle/PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR) (MCP at `/mcp_server`) | ~77,000 stars (was ~72K) |
| License | Apache-2.0 |
| Language | Python |
| Tools | 4 (was 2) |
| Languages | 111 (was 100+) |
| Install | `pip install paddleocr-mcp` |
| Framework | FastMCP v2 |

The most significant OCR MCP server in the original review has grown substantially. The parent repo added 5,000 stars in six weeks, and the MCP server doubled its tool count from 2 to 4.

### What's Changed Since March 2026

**Two new VLM-based tools.** The MCP server now exposes:
- `OCR` — text detection + recognition on images/PDFs (original)
- `PP-StructureV3` — layout parsing, tables, titles to Markdown (original)
- `PaddleOCR-VL` — VLM-based document layout extraction to Markdown (new)
- `PaddleOCR-VL-1.5` — upgraded VL model with [94.5% accuracy on OmniDocBench v1.5](https://arxiv.org/abs/2601.21957) (new)

PP-OCRv5 models (mobile detection + recognition variants) are explicitly supported, with improved handling for seal recognition and cross-page table merging.

**v3.4.1 (April 14)** added AMD GPU and Intel Arc GPU support for PaddleOCR-VL. **v3.5.0 (April 21)** added deep Hugging Face Transformers integration (20 major models), native Word/Excel/PowerPoint to Markdown conversion, DOCX export, and **PaddleOCR.js** — a browser SDK enabling PP-OCRv5 inference entirely in-browser.

**111 language support** (up from 100+, adding Tibetan and Bengali).

### What Still Applies

Resource requirements for local mode (several hundred MB model download, GPU recommended). Sparse MCP-specific documentation relative to the full library. AIStudio cloud mode ties to Baidu's infrastructure.

---

### Docling (IBM Research / LF AI & Data Foundation)

| Detail | Info |
|--------|------|
| [docling-project/docling](https://github.com/docling-project/docling) | ~59,000 stars (was ~35K — +24K in 6 weeks); ~64,800 as of this audit |
| License | MIT |
| Language | Python |
| Official MCP | Red Hat GmbH listing on PulseMCP |
| Releases since review | v2.86–v2.92 (7 versions, weekly cadence) |

Docling's star growth is remarkable: from roughly 35,000 stars at the time of the original review to 59,000 six weeks later. The weekly release cadence has added capabilities that directly improve OCR and document intelligence:

- **Nanonets OCR2 integration** (v2.87.0, April 13) — third-party neural OCR backend option
- **GraniteVisionTableStructureModel** (v2.90.0, April 17) — VLM-based table extraction
- **EasyOCR model fix** (v2.91.0, April 23)
- **Multi-lingual OCR via kserve-triton** (v2.92.0, April 29)
- **Modular `docling-slim` package** (v2.92.0) — lighter install without optional dependencies

The Red Hat MCP server predates this review, but Docling's rapid expansion makes it a more prominent option than it appeared in March. Docling is now one of the highest-starred document processing libraries in the Python ecosystem, with strong LF AI & Data Foundation backing.

**Correction (2026-08-16 audit):** the repo has since moved from `DS4SD/docling` to `docling-project/docling` (the old URL redirects; link updated above). Its [current README](https://github.com/docling-project/docling) confirms it's still hosted under the LF AI & Data Foundation with IBM Research Zurich credited as the founding team — the "IBM Research / LF AI & Data Foundation" framing above still holds.

---

## Cloud API Wrappers

### Mistral OCR MCP

| Detail | Info |
|--------|------|
| [everaldo/mcp-mistral-ocr](https://github.com/everaldo/mcp-mistral-ocr) | ~37 stars |
| License | MIT |
| Language | Python |
| Tools | 1 |
| Auth | Mistral API key |
| Status | **Dormant** — no commits since February 21, 2026 |

The wrapper itself has been dormant since before the original review. No activity since February 2026.

The underlying [Mistral OCR 3 API](https://mistral.ai/news/mistral-ocr-3/) (model `mistral-ocr-2512`, December 2025) remains excellent — 74% win rate over its predecessor, with strong performance on handwriting, complex tables, and European documents at $2/1,000 pages. But this community wrapper has not kept pace. For Mistral OCR via MCP, you would need to implement your own wrapper or find a more actively maintained integration.

### Gemini OCR MCP

| Detail | Info |
|--------|------|
| [WindoC/gemini-ocr-mcp](https://github.com/WindoC/gemini-ocr-mcp) | ~5 stars |
| Language | Python |
| Tools | 2 (`ocr_image_file`, `ocr_image_base64`) |
| Auth | Google Gemini API key |

Negligible change since March. Still functional for file-path and base64-encoded image OCR using Gemini vision models. Low-volume use on Gemini's free tier is still the main appeal.

### AWS Document Loader MCP

| Detail | Info |
|--------|------|
| [awslabs/mcp](https://github.com/awslabs/mcp) (at `src/document-loader-mcp-server`) | ~8,900 stars (monorepo, was ~4,700) |
| License | Apache-2.0 |
| Language | Python |

The AWS MCP monorepo nearly doubled in stars (4,700 → 8,900) and now contains 56 MCP servers. The document loader remains a document ingestion utility (pdfplumber for PDFs, markitdown for Office formats, direct image loading) rather than a dedicated OCR server. **There is still no AWS Textract MCP server** — confirmed via monorepo directory scan. The `aws-dataprocessing-mcp-server` exists but does not expose Textract's table extraction or form parsing capabilities through MCP.

---

## New Commercial Entries

### PaperOffice Document AI

| Detail | Info |
|--------|------|
| [paperoffice.ai](https://paperoffice.ai) | Commercial |
| Tools | 300+ |
| Released | March 28, 2026 |
| Transport | Streamable HTTP |
| Auth | API key; free tier available |

Launched nine days after the original review, PaperOffice is one of the most tool-rich document intelligence servers in the MCP ecosystem. The 300+ tools cover OCR, Intelligent Document Processing (IDP), e-signatures, knowledge graphs, and document automation workflows, per [PaperOffice's own MCP-connect page](https://paperoffice.ai/en/ai-mcp-connect/). The sheer tool count reflects an enterprise-grade platform rather than a focused OCR engine.

**Correction (2026-08-16 audit):** this section previously said 357+ tools. PaperOffice's own current site — homepage, pricing page, and MCP-connect page — consistently states "300+" ("300+ MCP tools" / "300+ production endpoints"); we could not find "357" used anywhere on paperoffice.ai as of this audit. Updated above.

**Trade-off:** This is a proprietary, API-dependent commercial service. There is no open-source fallback. The free tier makes evaluation possible, but production use requires an ongoing API relationship.

### Docu-Scan (Spocont)

| Detail | Info |
|--------|------|
| [Spocont Docu-Scan](https://docu-scan.spocont.com) | Commercial |
| Released | April 12, 2026 |
| Transport | Streamable HTTP |
| Auth | API key; free trial |
| Capabilities | OCR text extraction, entity field extraction, signature detection, stamp/seal detection |
| PulseMCP weekly | ~398 at May 2026 refresh (unverified as of this audit — see note) |

A commercial OCR + entity-extraction API from Spocont, a financial/IFRS-automation vendor that separately runs an [official Spocont IFRS MCP server on PulseMCP](https://www.pulsemcp.com/servers/spocont-ifrs). Per [Spocont's own Docu-Scan product page](https://docu-scan.spocont.com), capabilities include full OCR text extraction, entity field extraction, signature detection, and stamp/seal detection, with a free trial available.

**Correction (2026-08-16 audit):** an earlier version of this section described Docu-Scan's backend as "Google Document AI" and titled the section "Google Document AI Backend." We could not verify that anywhere on re-audit — Spocont's own current Docu-Scan product page makes no mention of Google Document AI or any specific backend model, and no independent source confirms it. Per this site's "cite it or cut it" rule, that claim has been removed rather than re-sourced. The PulseMCP weekly-traffic figure (~398) also could not be re-verified this audit (the listing page wasn't reachable via search); treat it as an unconfirmed May 2026 data point.

---

## Local OCR Engines

### Markdownify MCP

| Detail | Info |
|--------|------|
| [zcaceres/markdownify-mcp](https://github.com/zcaceres/markdownify-mcp) | ~2,600 stars (was ~2,400) |
| License | MIT |
| Language | TypeScript |
| Tools | 10 |
| Latest | v1.1.0 (May 1, 2026) |
| Formats | PDF, images, DOCX, XLSX, PPTX, audio, YouTube, web pages |

Continued steady growth and active maintenance. Notable changes since March:

- **v1.0.4 (April 17)** — fixed ARM/Apple Silicon Docker crash (switched from `markitdown[all]` to `markitdown[pdf]` for ARM compatibility). Image OCR and audio transcription still require `markitdown[all]` extras.
- **v1.1.0 (May 1)** — Docker and non-standard path support; new `MARKITDOWN_PATH`, `REPOMIX_PATH`, `MD_ALLOWED_PATHS` env vars; security fix (removed `projectRoot` from MCP tool schema); fixed false-fatal stderr treatment.

Still the most adopted community option and the pragmatic choice if you need OCR alongside PDF, audio, web, and Office document conversion in a single server.

### EasyOCR MCP

| Detail | Info |
|--------|------|
| [WindoC/easyocr-mcp](https://github.com/WindoC/easyocr-mcp) | ~2 stars |
| Language | Python |
| Tools | 3 (base64, file, URL inputs) |
| Languages | 80+ |

No meaningful change since March. Still functional, still lightly adopted. The three input methods (base64, file path, URL) remain the main appeal. PaddleOCR's MCP server is the stronger choice for any serious local OCR use case.

### Tesseract MCP Server

| Detail | Info |
|--------|------|
| [maximdx/tesseract-mcp-server](https://github.com/maximdx/tesseract-mcp-server) | ~2 stars |
| Language | Python |
| Tools | 1 (`convert_pdf`) |

Effectively a proof of concept — one commit, no activity since publication. Tesseract (60K+ stars on the parent) remains without a quality MCP wrapper.

### RapidOCR MCP

Two new community implementations have emerged for RapidOCR (a cross-platform, ONNX-based PaddleOCR deployment):

- `z4none/rapidocr-mcp` — 5 stars, September 2025, "easy-to-use OCR interface"
- `bitfarer/rapidocr-mcp` — 1 star, active (updated April–May 2026), described as "high-performance OCR MCP server"

RapidOCR's appeal is its cross-platform deployment without a full PaddlePaddle dependency. Neither wrapper has significant adoption yet.

### Nougat OCR MCP (Meta's Academic PDF Model)

| Detail | Info |
|--------|------|
| [svretina/nougat-mcp](https://github.com/svretina/nougat-mcp) | ~3 stars |
| Language | Python |
| Tools | 2 (`parse_research_paper`, `get_output_settings`) |
| Specialty | Academic/scientific PDFs with LaTeX formula preservation |

Uses Meta's [Nougat](https://github.com/facebookresearch/nougat) model for academic paper PDF parsing. The model is specifically trained to preserve mathematical equations, tables, and document structure in research papers — which generic OCR engines handle poorly.

For teams processing academic literature through MCP, this fills a real niche. Low adoption, but the use case is genuinely underserved.

---

## Multi-Model and Specialized

### ocr-mcp (Multi-Model OCR)

| Detail | Info |
|--------|------|
| [sandraschi/ocr-mcp](https://github.com/sandraschi/ocr-mcp) | ~11 stars |
| License | MIT |
| Version | 0.2.0-alpha |
| Language | Python |
| Framework | FastMCP 3.1 |
| Models | 10+ (DeepSeek-OCR-2, PaddleOCR-VL-1.5, Mistral OCR, Florence-2, DOTS.OCR, Qwen-Image, and more) |

Expanded significantly from the original review. The model roster now includes Mistral OCR and DOTS.OCR alongside the original five, and the DeepSeek and PaddleOCR entries have been updated to versioned releases (DeepSeek-OCR-2, PaddleOCR-VL-1.5). A React frontend and FastAPI backend have been added (web UI on port 10858, API on 10859), along with WIA scanner integration for Windows hardware control.

Still alpha, still lightly adopted — but the multi-model concept continues to be the most architecturally interesting approach in this category.

### Handwriting OCR MCP

| Detail | Info |
|--------|------|
| [Handwriting-OCR/handwriting-ocr-mcp-server](https://github.com/Handwriting-OCR/handwriting-ocr-mcp-server) | ~15 stars |
| Language | TypeScript/Node.js |
| Tools | 3 (upload, check status, retrieve results) |
| Auth | Handwriting OCR Platform API token |

No change since March. Still the only MCP server focused specifically on handwritten text recognition. Requires a paid Handwriting OCR Platform account.

**New competition:** `lazyants/transkribus-mcp-server` (March 2026, 0 stars) integrates the Transkribus REST API — an academic HTR (Handwritten Text Recognition) platform widely used for historical documents and manuscripts. Zero adoption but potentially relevant for archival or historical document use cases.

### Unstructured MCP (Pipeline Orchestration)

| Detail | Info |
|--------|------|
| [Unstructured-IO/UNS-MCP](https://github.com/Unstructured-IO/UNS-MCP) | ~43 stars (was ~16) |
| Language | Python |
| Auth | Unstructured API key |

Nearly tripled in stars (16 → 43) without adding new tools. Notable post-review changes:

- **March 26** — MCP SDK upgraded 1.13.1 → 1.23.0 (DNS rebinding protection, task support, advanced auth flows)
- **April 12** — Security patch: aiohttp, pypdf, urllib3, and tornado CVE remediation

The 18-tool architecture (source connectors, destination connectors, workflow management, job monitoring) remains unchanged. Best suited for orchestrating document processing pipelines at scale.

---

## What's Missing

**No official Tesseract MCP server.** Still the same gap from March — the world's most widely deployed open-source OCR engine has only minimal community wrappers.

**No Google Cloud Vision official MCP server.** Community implementations exist, led by [KohenAvocats/mcp-server-google-vision](https://github.com/KohenAvocats/mcp-server-google-vision) (built by a Paris law firm for scanned/handwritten legal documents), but Google has shipped no official offering.

**No AWS Textract MCP server.** Confirmed missing from the 56-server AWS monorepo. No community implementations with meaningful adoption. Amazon Textract's table extraction, form parsing, and expense analysis capabilities remain inaccessible through MCP.

**No Azure Document Intelligence MCP server.** A 0-star community stub exists (linzhengen/azure-document-intelligence-mcp) but no official Microsoft offering despite Azure's active MCP presence in other domains.

**Receipt/invoice OCR is partially addressed.** `receiptconverter-mcp` (March 2026, 0 stars) and Space OCR MCP (April 30, 2026, 0 stars) both offer receipt/invoice templates, but both are early-stage commercial wrappers with no proven adoption.

**No real-time video OCR.** Still no MCP servers for screen text extraction, video subtitle extraction, or live camera OCR.

---

## How to Choose

**"I need the best document-to-Markdown conversion"** → [MinerU MCP](https://github.com/opendatalab/MinerU). 61,700-star library (now ~77,700), Apache-2.0-based license, supports PDF/DOCX/PPTX/XLSX, multiple inference backends. Had the highest PulseMCP traffic among OCR servers at the May 2026 refresh (see correction in the MinerU section — traffic has since dropped substantially).

**"I need the best open-source OCR with maximum language coverage"** → [PaddleOCR MCP](https://github.com/PaddlePaddle/PaddleOCR). Official vendor server, 111 languages, 4 tools including VLM-based extraction, runs locally.

**"I want one server for many conversion types"** → [Markdownify MCP](https://github.com/zcaceres/markdownify-mcp). OCR plus PDF, audio, web, and Office. 2,600 stars, MIT license, actively maintained.

**"I need the highest accuracy on scientific or complex structured documents"** → [Docling](https://github.com/docling-project/docling) (via Red Hat MCP server) or [MinerU MCP](https://github.com/opendatalab/MinerU) (VLM engine). Both are battle-tested libraries with strong table and formula handling.

**"I need handwriting recognition"** → [Handwriting OCR MCP](https://github.com/Handwriting-OCR/handwriting-ocr-mcp-server). Still the only purpose-built option. Requires API token.

**"I want to choose between multiple OCR engines per document type"** → [ocr-mcp](https://github.com/sandraschi/ocr-mcp). Now 10+ models. Alpha stage but architecturally sound.

**"I need enterprise-scale document processing pipelines"** → [Unstructured MCP](https://github.com/Unstructured-IO/UNS-MCP) for workflow orchestration, or [PaperOffice Document AI](https://paperoffice.ai) for 300+ tools.

**"I need a commercial OCR + entity-extraction API through MCP"** → [Docu-Scan](https://docu-scan.spocont.com) (commercial; OCR, entity extraction, signature/stamp detection — see correction above on backend claims). No official Google Cloud Vision or Google Document AI MCP offering exists.

---

## Rating: 3.5 / 5

Upgraded from 3.0 due to meaningful progress at the top of the ecosystem. MinerU's emergence as the then-highest-traffic OCR MCP server on PulseMCP (61,700-star library at the time, Apache-2.0-based license, seven rapid releases) represented a genuine step forward, though its PulseMCP traffic has since fallen well off that peak (see correction above). PaddleOCR's MCP server doubling its tool count with VLM-based models and 111-language support is a material improvement. Docling's explosion (35K → 59K stars with weekly releases) signals a growing community around high-quality document intelligence.

The bottom of the ecosystem remains thin — most servers beyond the top tier have single-digit stars, minimal documentation, and limited community testing. The major cloud providers (Google Cloud Vision, AWS Textract, Azure Document Intelligence) are still absent from MCP. Mistral OCR — one of the best cloud OCR APIs available — lacks a maintained MCP wrapper despite the underlying API's continued excellence.

The gap between the quality of underlying OCR engines and the quality of their MCP integrations is narrowing, but has not closed. Today, MinerU and PaddleOCR represent genuinely production-ready options; everything else requires careful evaluation.

---

*This review was originally published 2026-03-19 and refreshed 2026-05-02 (44 days) using Claude Sonnet 4.6 (Anthropic). Star counts, version numbers, and feature availability largely reflect research conducted in May 2026, except where corrections above note updates verified during the 2026-08-16 audit. We research MCP servers thoroughly through documentation, GitHub repositories, community discussions, and published benchmarks — we do not test servers hands-on.*

*This review's citations were re-audited claim-by-claim on 2026-08-16 using Claude Sonnet 5 (Anthropic).*
