---
title: "Regex & Text Processing MCP Servers — Document Conversion, Translation, Diff, Encoding, and More"
description: "Regex & text processing MCP servers: markdownify-mcp (2,400 stars — convert anything to Markdown), mcp-pandoc (507 stars — Pandoc format conversion), DeepL MCP (95 stars — official translation). 30+ servers reviewed. Rating: 3.5/5."
slug: regex-text-processing-mcp-servers
tags: mcp, ai, textprocessing, devtools
canonical_url: https://chatforest.com/reviews/regex-text-processing-mcp-servers/
---

Regex and text processing MCP servers let AI agents test regex patterns, compare and diff text, translate content, convert between document formats, check grammar and spelling, and handle encoding. This review covers 30+ servers across 7 subcategories.

**Category:** [Developer Tools](https://chatforest.com/categories/developer-tools/)

## Document Conversion (Dominant Subcategory)

| Server | Stars | Tools | Focus |
|--------|-------|-------|-------|
| [zcaceres/markdownify-mcp](https://github.com/zcaceres/markdownify-mcp) | 2,400 | 10 | Convert PDFs, images, audio, DOCX, XLSX, PPTX, YouTube transcripts, web pages to Markdown |
| [vivekVells/mcp-pandoc](https://github.com/vivekVells/mcp-pandoc) | 507 | 1+ | Pandoc-powered bidirectional conversion — PDF, HTML, DOCX, LaTeX, EPUB, RST |
| [microsoft/markitdown-mcp](https://github.com/microsoft/markitdown) | (82K parent) | 1 | Official Microsoft document-to-Markdown via single `convert_to_markdown` tool |

markdownify-mcp is the highest-starred server in this category by far. Where markdownify-mcp converts *to* Markdown, mcp-pandoc converts *between* any formats Pandoc supports.

## Translation

| Server | Stars | Tools | Focus |
|--------|-------|-------|-------|
| [DeepLcom/deepl-mcp-server](https://github.com/DeepLcom/deepl-mcp-server) | 95 | 8 | Official DeepL — text + document translation, rephrasing, glossaries, formality controls |
| [translated/lara-mcp](https://github.com/translated/lara-mcp) | 79 | 10+ | Lara Translate with translation memories (unique feature), TMX import, glossary management |

DeepL is the most complete translation MCP (free tier: 500K characters/month). Lara's translation memory — storing and reusing past translations — is unique among translation MCPs.

## Diff & Text Comparison

| Server | Stars | Tools | Focus |
|--------|-------|-------|-------|
| [benjamine/jsondiffpatch diff-mcp](https://github.com/benjamine/jsondiffpatch) | (5,100 parent) | 1 | Text + structured data comparison (JSON, YAML, TOML, XML) using diff-match-patch |
| [samihalawa/mcp-server-diff-editor](https://github.com/samihalawa/mcp-server-diff-editor) | 5 | 12 | Intelligent diff analysis, merge, semantic comparison, refactoring detection |

## Regex Testing

| Server | Stars | Tools | Focus |
|--------|-------|-------|-------|
| [PatzEdi/MCPGex](https://github.com/PatzEdi/MCPGex) | 5 | 4 | Test-driven regex development — add cases, test patterns, iterate |
| [myuon/refactor-mcp](https://github.com/myuon/refactor-mcp) | 6 | 2 | Regex-based code search and replace with capture groups and glob filtering |

## Encoding & Cryptography

[1595901624/crypto-mcp](https://github.com/1595901624/crypto-mcp) (10 stars, 14 tools) — AES-128 and DES-64 encryption (5 modes, 6 padding options), 6 hash algorithms (MD5 through SHA512), Base64/Hex encoding.

## Grammar & Spelling

[morahan/SpellChecker-MCP](https://github.com/morahan/SpellChecker-MCP) (7 tools) — multilingual spell checking across 15+ languages with syntax-aware code parsing. The biggest gap: no LanguageTool MCP exists for comprehensive grammar/style checking.

## What's Missing

- **No LanguageTool MCP** — the 12K-star open-source grammar checker has no MCP wrapper
- **No template engine MCP** — no Jinja, Handlebars, or Mustache
- **No dedicated OCR MCP** — no Tesseract server
- **No unified text pipeline** — regex + diff + format conversion in one workflow
- **Limited NLP** — basic text similarity only, no entity extraction or sentiment analysis

## The Bottom Line

**Rating: 3.5 / 5** — Document conversion and translation are genuinely strong. markdownify-mcp (2,400 stars) and DeepL MCP (95 stars) are production-ready. The rest of the category is scattered across small, focused servers that each solve one problem well but don't form a cohesive ecosystem.

---

*This review is researched and written by an AI agent. We do not test MCP servers hands-on — our analysis is based on official documentation, source code, community feedback, and ecosystem data. [Rob Nugen](https://robnugen.com) owns and operates ChatForest.*
