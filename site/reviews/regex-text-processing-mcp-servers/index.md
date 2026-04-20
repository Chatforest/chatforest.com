# Regex & Text Processing MCP Servers — Pattern Matching, Diff, Translation, Format Conversion, Grammar, and Encoding

> Regex and text processing MCP servers let AI agents test regex patterns, compare text, translate content, convert between formats, check grammar, and handle encoding.


Regex and text processing MCP servers let AI agents test regex patterns, compare and diff text, translate content, convert between document formats, check grammar and spelling, and handle encoding operations. Instead of manually running regex testers, diff tools, or format converters, AI assistants can process text through natural language commands.

This review covers **regex and text processing MCP servers** — document conversion, diff/comparison, translation, regex testing, encoding/cryptography, grammar/spelling, and text manipulation. For related servers, see our [Browser Automation review](/reviews/playwright-mcp-server/) (web content extraction), [Search reviews](/reviews/brave-search-mcp-server/) (web search), and [Terminal & CLI Tools review](/reviews/terminal-cli-tools-mcp-servers/) (command-line text processing).

The headline findings: **Document conversion dominates** — markdownify-mcp (2,400 stars) and mcp-pandoc (507 stars) handle nearly any format. **Translation has strong official support** — DeepL and Lara Translate provide production-grade MCPs. **Diff tools are plentiful** — jsondiffpatch's diff-mcp covers text and structured data. **Regex testing is functional but niche** with only a few dedicated servers. **Grammar/spelling lacks a LanguageTool MCP**, leaving a significant gap.

**Category:** [Developer Tools](/categories/developer-tools/)

---

## Document Conversion

### zcaceres/markdownify-mcp — Convert Almost Anything to Markdown

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [markdownify-mcp](https://github.com/zcaceres/markdownify-mcp) | 2,400 | TypeScript | — | 10 |

**The most popular text processing MCP server** — converts a wide variety of content to Markdown:

- **Documents** — PDF, DOCX, XLSX, PPTX
- **Media** — images (with OCR), audio (with transcription)
- **Web content** — web pages, YouTube transcripts, Bing search results
- **File retrieval** — read existing Markdown files
- **10 dedicated tools** — one per content type for clear, focused conversion

The go-to server for ingesting diverse content into LLM-friendly Markdown format. Especially useful for RAG pipelines and document processing workflows.

### vivekVells/mcp-pandoc — Pandoc-Powered Format Conversion

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [mcp-pandoc](https://github.com/vivekVells/mcp-pandoc) | 507 | Python | MIT | 1+ |

**Bidirectional document conversion** using the industry-standard Pandoc engine:

- **Input/output formats** — PDF, HTML, Markdown, DOCX, RST, EPUB, LaTeX, and more
- **Advanced configuration** — YAML defaults files for conversion options
- **Filter support** — apply Pandoc filters during conversion
- **Installable via Smithery** — `npx -y @smithery/cli install mcp-pandoc --client claude`

Where markdownify-mcp converts *to* Markdown, mcp-pandoc converts *between* any formats Pandoc supports. The right choice when you need LaTeX output, EPUB generation, or other non-Markdown targets.

### microsoft/markitdown-mcp — Official Microsoft Document Converter

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [markitdown-mcp](https://github.com/microsoft/markitdown/tree/main/packages/markitdown-mcp) | (82K parent) | Python | MIT | 1 |

**Official MCP server from Microsoft's markitdown project** (82K+ stars):

- **Single tool** — `convert_to_markdown(uri)` accepts http:, https:, file:, or data: URIs
- **Multiple transports** — STDIO, Streamable HTTP, and SSE
- **Preserves structure** — headings, lists, tables, links maintained as Markdown
- **Lightweight** — minimal dependencies, focused on one job

The simplest option for document-to-Markdown conversion. Microsoft backing means long-term maintenance.

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
| [deepl-mcp-server](https://github.com/DeepLcom/deepl-mcp-server) | 95 | JavaScript | — | 8 |

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
| [tumf/mcp-text-editor](https://github.com/tumf/mcp-text-editor) | 177 | Python | 3+ | Line-based file editing with conflict detection |
| [yhzion/comment-stripper-mcp](https://github.com/yhzion/comment-stripper-mcp) | — | TypeScript | 3+ | Batch comment removal from 10+ languages (JS, Python, Java, C++, etc.) |
| [Dicklesworthstone/ultimate_mcp_server](https://github.com/Dicklesworthstone/ultimate_mcp_server) | 129 | Python | 40+ | Multi-tool server with ripgrep, awk, sed, jq text processing |

---

## What's Missing

The regex and text processing MCP landscape has solid coverage for document conversion and translation but notable gaps elsewhere:

- **No LanguageTool MCP** — the open-source grammar/style checker for 25+ languages has no MCP wrapper. This is the biggest gap — LanguageTool (12K+ stars) is the gold standard for multilingual proofreading
- **No template engine MCP** — no Jinja, Handlebars, or Mustache MCP for server-side template rendering
- **No dedicated OCR MCP** — markdownify-mcp handles some OCR through image conversion, but there's no Tesseract or dedicated OCR server
- **No unified text pipeline** — no single server combining regex, diff, format conversion, and transformation in one coherent workflow
- **No i18n pipeline** — translation exists but no comprehensive internationalization tooling (plural rules, locale-aware formatting, translation file management)
- **Limited NLP** — mcp-nlp offers basic text similarity but nothing for entity extraction, sentiment analysis, or text classification

---

## Bottom Line

**Rating: 3.5/5** — Document conversion and translation are genuinely strong. The rest of the category is scattered across small, focused servers that each solve one problem well but don't form a cohesive ecosystem.

**Best in class:**
- **Document conversion:** zcaceres/markdownify-mcp (2,400 stars) for to-Markdown, vivekVells/mcp-pandoc (507 stars) for between-formats
- **Translation:** DeepLcom/deepl-mcp-server (95 stars) for quality, translated/lara-mcp (79 stars) for memory
- **Diff:** benjamine/jsondiffpatch diff-mcp for text + structured data comparison

**If you only install one:** markdownify-mcp solves the most common text processing need — getting documents into a format your LLM can work with.

*This review was last edited on 2026-03-16 using Claude Opus 4.6 (Anthropic).*

