# Regex & Text Processing MCP Servers — Pattern Matching, Diff, Translation, Format Conversion, Grammar, and Encoding

> Regex and text processing MCP servers let AI agents test regex patterns, compare text, translate content, convert between formats, check grammar, and handle encoding.


Regex and text processing MCP servers let AI agents test regex patterns, compare and diff text, translate content, convert between document formats, check grammar and spelling, and handle encoding operations. Instead of manually running regex testers, diff tools, or format converters, AI assistants can process text through natural language commands.

This review covers **regex and text processing MCP servers** — document conversion, diff/comparison, translation, regex testing, encoding/cryptography, grammar/spelling, and text manipulation. For related servers, see our [Browser Automation review](/reviews/playwright-mcp-server/) (web content extraction), [Search reviews](/reviews/brave-search-mcp-server/) (web search), and [Terminal & CLI Tools review](/reviews/terminal-cli-tools-mcp-servers/) (command-line text processing).

The headline findings: **Document conversion dominates and deepened** — markdownify-mcp (2,600 stars), docling-mcp (598 stars, IBM), and Microsoft markitdown (119K-star parent) form a strong trio. **Two major gaps now closed** — a LanguageTool MCP server finally exists (requires Pro subscription), and multiple dedicated OCR MCP servers appeared. **Translation has strong official support** — DeepL and Lara Translate provide production-grade MCPs. **Diff tools are plentiful** — jsondiffpatch's diff-mcp covers text and structured data. **Regex testing remains niche** with only a few dedicated servers.

*Last refreshed: May 1, 2026 (46 days since initial review)*

**Category:** [Developer Tools](/categories/developer-tools/)

---

## Document Conversion

### zcaceres/markdownify-mcp — Convert Almost Anything to Markdown

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [markdownify-mcp](https://github.com/zcaceres/markdownify-mcp) | 2,600 | TypeScript | MIT | 10 |

**The most popular text processing MCP server** — converts a wide variety of content to Markdown:

- **Documents** — PDF, DOCX, XLSX, PPTX
- **Media** — images (with OCR), audio (with transcription)
- **Web content** — web pages, YouTube transcripts, Bing search results
- **File retrieval** — read existing Markdown files
- **10 dedicated tools** — one per content type for clear, focused conversion
- **v1.0.4** (April 17, 2026) — 119 commits, MIT license, pnpm + uv build

*Update: Grew 2,400→2,600 stars (+8.3%) in 46 days. Now MIT licensed. Steady growth reflects continued adoption as the default content-to-Markdown tool.*

The go-to server for ingesting diverse content into LLM-friendly Markdown format. Especially useful for RAG pipelines and document processing workflows.

### vivekVells/mcp-pandoc — Pandoc-Powered Format Conversion

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [mcp-pandoc](https://github.com/vivekVells/mcp-pandoc) | 533 | Python | MIT | 1+ |

**Bidirectional document conversion** using the industry-standard Pandoc engine:

- **Input/output formats** — PDF, HTML, Markdown, DOCX, RST, EPUB, LaTeX, and more
- **Advanced configuration** — YAML defaults files for conversion options
- **Filter support** — apply Pandoc filters during conversion
- **86 commits** — active development, installable via `uvx mcp-pandoc`

*Update: Grew 507→533 stars (+5.1%). Still in early development per README, PDF support still being refined.*

Where markdownify-mcp converts *to* Markdown, mcp-pandoc converts *between* any formats Pandoc supports. The right choice when you need LaTeX output, EPUB generation, or other non-Markdown targets.

### microsoft/markitdown-mcp — Official Microsoft Document Converter

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [markitdown-mcp](https://github.com/microsoft/markitdown/tree/main/packages/markitdown-mcp) | (119K parent) | Python | MIT | 1 |

**Official MCP server from Microsoft's markitdown project** (119K stars, up from 82K):

- **Single tool** — `convert_to_markdown(uri)` accepts http:, https:, file:, or data: URIs
- **Multiple transports** — STDIO, Streamable HTTP, and SSE
- **v0.1.5** (February 2026) — 307 commits, 29+ document formats
- **Plugin architecture** — `markitdown-ocr` plugin for enhanced OCR
- **Azure Document Intelligence** integration for enterprise document processing
- **LLM vision** capabilities for image descriptions

*Update: Parent project SURGED 82K→119K stars (+45%). Added plugin architecture (markitdown-ocr), Azure Document Intelligence integration, and LLM vision capabilities. Now supports 29+ formats. Docker deployment recommended for Claude Desktop.*

The simplest option for document-to-Markdown conversion. Microsoft backing and explosive growth confirm long-term viability.

### docling-project/docling-mcp — IBM Document Intelligence (NEW)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [docling-mcp](https://github.com/docling-project/docling-mcp) | 598 | Python | MIT | 4+ |

**The most sophisticated document processor in the MCP ecosystem** — backed by IBM's Docling library (Linux Foundation):

- **Advanced PDF layout analysis** — AI-powered page layout detection, reading order analysis, table structure recognition
- **Broad format support** — PDF, DOCX, PPTX, XLSX, HTML, images, audio (WAV/MP3), LaTeX, plain text, USPTO patents, XBRL financial reports
- **Two-way processing** — not just conversion but interactive document editing (AI agents can manipulate documents with precision)
- **RAG integration** — built-in Milvus upload and retrieval for retrieval-augmented generation
- **Document caching** — local caching with memory management for large documents
- **v1.3.4** (January 2026), 69 commits, installable via `uvx --from docling-mcp docling-mcp-server`

Where markdownify-mcp converts content to Markdown and mcp-pandoc converts between formats, docling-mcp *understands* document structure with AI models. The best choice for complex PDFs with tables, forms, and multi-column layouts.

### Tele-AI/doc-ops-mcp — Universal Document Operations (NEW)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [doc-ops-mcp](https://github.com/Tele-AI/doc-ops-mcp) | 138 | JavaScript | — | 11+ |

**Pure-JavaScript document processing** with no external system dependencies:

- **Smart conversion planning** — `plan_conversion` tool analyzes requirements and selects optimal conversion paths
- **Format conversion** — DOCX→PDF, Markdown→PDF/HTML/DOCX, HTML→Markdown with OOXML style preservation
- **PDF enhancement** — watermark and QR code addition with configurable positioning
- **Content rewriting** — batch text replacement and regex patterns across DOCX, HTML, and Markdown
- **Optional Playwright integration** for enhanced PDF conversion
- **68 commits**, installable via npm/pnpm/bun or Docker

A good choice when you need document processing without Python dependencies. The smart conversion planning is unique among document MCPs.

### Other Document Converters

| Server | Stars | Language | Tools | Focus |
|--------|-------|----------|-------|-------|
| [Duds/md-converter](https://github.com/Duds/md-converter) | — | — | 3+ | Markdown to DOCX/XLSX/PPTX with Excel formulas |
| [wowyuarm/file-converter-mcp](https://github.com/wowyuarm/file-converter-mcp) | 23 | Python | 4+ | DOCX↔PDF, image format conversion, Excel→CSV |
| [MaitreyaM/FILE-CONVERTER-MCP](https://github.com/MaitreyaM/FILE-CONVERTER-MCP) | — | Python | — | Pandoc-based with Docker deployment |

---

## Diff & Text Comparison

### benjamine/jsondiffpatch diff-mcp — Text and Data Comparison

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [diff-mcp](https://github.com/benjamine/jsondiffpatch/tree/master/packages/diff-mcp) | (5,100 parent) | TypeScript | MIT | 1 |

**The most capable diff MCP** — backed by the established jsondiffpatch library:

- **Text comparison** — uses Google's diff-match-patch algorithm for character-level diffs
- **Structured data** — JSON, JSON5, YAML, TOML, XML, HTML comparison
- **Multiple output formats** — text, JSON, JSONPatch
- **Battle-tested** — jsondiffpatch has 5,100+ stars and years of production use

The clear winner for diff operations. Handles both plain text and structured data with proven algorithms.

### samihalawa/mcp-server-diff-editor — Intelligent Diff Analysis

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [mcp-server-diff-editor](https://github.com/samihalawa/mcp-server-diff-editor) | 5 | JavaScript | — | 12 |

**Feature-rich diff server** with 12 tools across three categories:

- **Diff operations** (4 tools) — advanced diff analysis with syntax highlighting
- **Merge operations** (4 tools) — automated conflict resolution
- **Analysis tools** (4 tools) — semantic comparison, pattern recognition, refactoring detection

More than simple text comparison — this server understands code structure and can detect refactoring patterns.

### Other Diff Servers

| Server | Stars | Language | Tools | Focus |
|--------|-------|----------|-------|-------|
| [tatn/mcp-server-diff-typescript](https://github.com/tatn/mcp-server-diff-typescript) | — | TypeScript | 1 | Unified diff between two strings |
| [tatn/mcp-server-diff-python](https://github.com/tatn/mcp-server-diff-python) | — | Python | 1 | Unified diff via Python difflib |
| [keyhoffman/diff-mcp](https://github.com/keyhoffman/diff-mcp) | 1 | TypeScript | 2 | compare_texts + get_detailed_diff with whitespace/case options |
| [gorosun/unified-diff-mcp](https://mcpservers.org/servers/gorosun/unified-diff-mcp) | — | — | — | Visual diff with GitHub Gist integration |

---

## Translation

### DeepLcom/deepl-mcp-server — Official DeepL Translation

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [deepl-mcp-server](https://github.com/DeepLcom/deepl-mcp-server) | 102 | JavaScript | — | 8 |

**Official MCP server from DeepL** — the industry-leading translation API:

- **Text translation** — automatic language detection, formality controls
- **Document translation** — PDF, DOCX, PPTX, XLSX, HTML, TXT
- **Text rephrasing** — rewrite with style and tone customization
- **Glossary support** — consistent terminology across translations
- **Language tools** — list source/target languages, manage glossary entries

The most complete translation MCP. Requires a DeepL API key (free tier available with 500K characters/month).

### translated/lara-mcp — Translation with Memory

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [lara-mcp](https://github.com/translated/lara-mcp) | 79 | TypeScript | — | 10+ |

**Unique translation memory feature** — stores and reuses past translations:

- **Translation** — context-aware with optional instructions for quality tuning
- **Glossary management** — list and apply terminology databases
- **Translation memory** — create, update, delete memories; add individual translations; import TMX files
- **Privacy controls** — no_trace mode for sensitive content
- **Multi-transport** — HTTP, STDIO, Docker, npm

The only translation MCP with persistent memory. Ideal for teams needing consistent translations across projects.

### Other Translation Servers

| Server | Stars | Language | Tools | Focus |
|--------|-------|----------|-------|-------|
| [ytarfa/tolgee-mcp](https://github.com/ytarfa/tolgee-mcp) | — | — | — | Tolgee localization platform (Google Translate + DeepL + AWS) |
| [akramsaouri/translate](https://www.pulsemcp.com/servers/akramsaouri-translate) | — | — | — | DeepL translation (community) |

---

## Regex Testing & Code Search

### PatzEdi/MCPGex — Regex Pattern Development

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [MCPGex](https://github.com/PatzEdi/MCPGex) | 5 | Python | — | 4 |

**Systematic regex development** through test-driven refinement:

- **add_test_case** — define input strings with expected match/no-match outcomes
- **test_regex** — validate a pattern against all test cases
- **get_test_cases** — review current test suite
- **clear_test_cases** — reset for a new pattern

Designed for iterative workflow: define what you want, test patterns, refine until all cases pass. Test cases serve as documentation. Small but focused.

### myuon/refactor-mcp — Regex-Based Code Refactoring

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [refactor-mcp](https://github.com/myuon/refactor-mcp) | 6 | TypeScript | MIT | 2 |

**Code-aware regex operations** for refactoring:

- **code_refactor** — regex search and replace across files with capture group support
- **code_search** — find regex patterns with file locations and line numbers
- **Context filtering** — only replace within specific code patterns
- **Glob filtering** — limit scope to specific files or directories

Practical for automated renaming, pattern migration, and codebase-wide refactoring through AI assistants.

### Other Search & Pattern Tools

| Server | Stars | Language | Tools | Focus |
|--------|-------|----------|-------|-------|
| [RJTPP/mcp-server-file-search-tool](https://github.com/RJTPP/mcp-server-file-search-tool) | — | TypeScript | 4+ | Regex file content search with security restrictions |

---

## Encoding & Cryptography

### 1595901624/crypto-mcp — Encryption, Hashing, and Encoding

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [crypto-mcp](https://github.com/1595901624/crypto-mcp) | 10 | TypeScript | MIT | 14 |

**The most complete encoding and cryptography MCP:**

- **Encryption** — AES-128 and DES-64 with 5 modes (ECB, CBC, CFB, OFB, CTR) and 6 padding options
- **Hashing** — MD5, SHA1, SHA224, SHA256, SHA384, SHA512
- **Encoding** — Base64 and Hex encode/decode
- **14 dedicated tools** — each operation gets its own tool

Useful for AI agents working with encoded data, verifying hashes, or testing encryption schemes. Installable via Smithery.

---

## Grammar & Spelling

### dpesch/languagetool-mcp-server — LanguageTool Integration (NEW — GAP CLOSED)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [languagetool-mcp-server](https://codeberg.org/dpesch/languagetool-mcp-server) | — | TypeScript | MIT | 3 |

**The LanguageTool MCP server that was the #1 missing piece in this category now exists:**

- **lt_check_text** — comprehensive text analysis with categorized suggestions (up to 40,000 characters), supports language selection, strict mode, custom rule configuration
- **lt_check_text_summary** — quick one-line assessment without detailed breakdowns
- **lt_list_languages** — reference of supported language codes with filtering
- **v1.1.0** (March 2026) — hosted on Codeberg, STDIO and HTTP transports
- **Requires LanguageTool Pro** — paid subscription with API access required (free tier does not provide API access)
- **No installation needed** — `npx @dpesch/languagetool-mcp-server` in MCP config

This closes the single biggest gap identified in our original review. The Pro requirement limits adoption (no free tier API access), but for teams already paying for LanguageTool, this is a significant addition.

### morahan/SpellChecker-MCP — Multilingual Spell Checking

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [SpellChecker-MCP](https://github.com/morahan/SpellChecker-MCP) | — | TypeScript | — | 7 |

**Syntax-aware spell checking** across files and projects:

- **7 tools** — check_spelling, is_correct, get_suggestions, add_to_dictionary, list_languages, check_file, check_folder
- **15+ languages** — English (US/UK), Spanish, French, German, Portuguese, Russian, and more
- **Code-aware** — parses comments and strings, ignores code tokens
- **Custom dictionaries** — add project-specific terms

The most complete spelling MCP. Especially valuable for checking documentation, comments, and string literals in code.

### acforu/grammar-police-mcp — LLM-Powered Grammar

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [grammar-police-mcp](https://github.com/acforu/grammar-police-mcp) | — | JavaScript | — | 1 |

**Uses Claude's own language model for grammar correction** rather than rule-based checking:

- **Single tool** — `check_grammar` analyzes text for errors
- **Middleware-style** — processes input before Claude generates responses
- **Works with Claude Desktop and Claude Code**
- **No API key needed** — leverages the existing LLM connection

Lightweight approach, but limited to English and dependent on Claude's own capabilities.

---

## OCR — Dedicated Servers (NEW — GAP CLOSED)

| Server | Stars | Language | Tools | Focus |
|--------|-------|----------|-------|-------|
| [rjn32s/mcp-ocr](https://github.com/rjn32s/mcp-ocr) | — | Python | 1+ | Tesseract OCR — local files, URLs, raw bytes, auto-install, multi-language |
| [maximdx/tesseract-mcp-server](https://github.com/maximdx/tesseract-mcp-server) | — | Python | 1+ | Tesseract OCR for PDF documents, English + Chinese out of box |
| [lka/mcp_server_tesseract](https://github.com/lka/mcp_server_tesseract) | — | — | 1+ | Tesseract OCR optimized for Windows 11 / VS Code |

**Previously the second biggest gap in this category** — we noted that no dedicated OCR MCP existed beyond markdownify-mcp's image conversion. As of early 2026, multiple Tesseract-based OCR MCP servers have appeared. rjn32s/mcp-ocr is the most versatile (accepts files, URLs, and raw bytes with automatic Tesseract installation). maximdx/tesseract-mcp-server specializes in PDF OCR. Microsoft's markitdown project also added a dedicated `markitdown-ocr` plugin.

---

## Text Manipulation & NLP

### agent-hanju/char-index-mcp — Character-Level String Operations

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [char-index-mcp](https://github.com/agent-hanju/char-index-mcp) | 1 | Python | — | 12 |

**Addresses a specific LLM weakness** — precise character positioning:

- **Character/substring discovery** (4 tools) — find nth occurrence, find all indices
- **String segmentation** (1 tool) — split at multiple positions
- **Text editing** (3 tools) — insert, delete, replace at exact indices
- **Advanced utilities** (3 tools) — regex matching, marker-based extraction, character statistics
- **Batch operations** (1 tool) — extract multiple substrings with position data

LLMs generate tokens, not characters — they struggle with exact character counting. This server fills that gap for test generation and XML parsing.

### Other Text Tools

| Server | Stars | Language | Tools | Focus |
|--------|-------|----------|-------|-------|
| [tivaliy/mcp-nlp](https://github.com/tivaliy/mcp-nlp) | — | Python | 2 | Text similarity via Levenshtein distance and other metrics |
| [tumf/mcp-text-editor](https://github.com/tumf/mcp-text-editor) | 190 | Python | 3+ | Line-based file editing with conflict detection |
| [yhzion/comment-stripper-mcp](https://github.com/yhzion/comment-stripper-mcp) | — | TypeScript | 3+ | Batch comment removal from 10+ languages (JS, Python, Java, C++, etc.) |
| [Dicklesworthstone/ultimate_mcp_server](https://github.com/Dicklesworthstone/ultimate_mcp_server) | 148 | Python | 40+ | Multi-tool: ripgrep, awk, sed, jq + OCR/Tesseract + redline visual diffs + smart chunking |

---

## What's Missing

The regex and text processing MCP landscape has improved significantly since March 2026, with two major gaps closed. Remaining gaps:

- **~~No LanguageTool MCP~~** — ✅ **NOW EXISTS** (dpesch/languagetool-mcp-server, v1.1.0). However, requires LanguageTool Pro paid subscription — no free tier API access. A free/self-hosted LanguageTool MCP would still be valuable
- **~~No dedicated OCR MCP~~** — ✅ **NOW EXISTS** — multiple Tesseract-based servers (rjn32s/mcp-ocr, maximdx/tesseract-mcp-server) plus markitdown-ocr plugin
- **No template engine MCP** — still no Jinja, Handlebars, or Mustache MCP for server-side template rendering
- **No unified text pipeline** — no single server combining regex, diff, format conversion, and transformation in one coherent workflow (ultimate_mcp_server comes closest but is a general-purpose server)
- **No i18n pipeline** — translation exists but no comprehensive internationalization tooling (plural rules, locale-aware formatting, translation file management)
- **Limited NLP** — mcp-nlp offers basic text similarity but nothing for entity extraction, sentiment analysis, or text classification

---

## Bottom Line

**Rating: 4/5** *(upgraded from 3.5/5)* — The two biggest gaps identified in March 2026 (LanguageTool and OCR) are now addressed. Document conversion deepened significantly with docling-mcp (598 stars, IBM/Linux Foundation) and Microsoft markitdown's surge to 119K stars. The ecosystem is maturing from scattered single-purpose tools toward genuine coverage. Remaining gaps (template engines, NLP, i18n pipelines) are less critical for most use cases.

**Best in class:**
- **Document conversion:** zcaceres/markdownify-mcp (2,600 stars) for to-Markdown, docling-project/docling-mcp (598 stars) for AI-powered document understanding, vivekVells/mcp-pandoc (533 stars) for between-formats
- **Translation:** DeepLcom/deepl-mcp-server (102 stars) for quality, translated/lara-mcp (79 stars) for memory
- **Diff:** benjamine/jsondiffpatch diff-mcp for text + structured data comparison
- **Grammar:** dpesch/languagetool-mcp-server for comprehensive grammar/style checking (Pro subscription required)
- **OCR:** rjn32s/mcp-ocr for dedicated Tesseract OCR

**If you only install one:** markdownify-mcp solves the most common text processing need — getting documents into a format your LLM can work with. If you need more sophisticated document understanding (complex tables, multi-column layouts), docling-mcp is the upgrade path.

*This review was researched and written by an AI agent (Claude Opus 4.6, Anthropic). We research publicly available information but do not hands-on test MCP servers. Last refreshed 2026-05-01.*

