# Translation & Localization MCP Servers — DeepL, Crowdin, Phrase, Lokalise, Smartling, and More

> Translation and localization MCP servers are turning AI agents into multilingual content managers — letting them translate text, manage translation projects, sync localization


Translation and localization MCP servers are turning AI agents into multilingual content managers. Instead of copying text between translation dashboards, managing locale files manually, and hunting for missing translations, these servers let agents translate content, manage translation projects, sync localization files, and maintain terminology glossaries — all through the Model Context Protocol.

The landscape spans five areas: **translation API wrappers** (DeepL leads with the most starred server), **enterprise TMS platforms** (Crowdin, Phrase, Lokalise, and Smartling with massive tool counts), **developer i18n tools** (framework-specific translation file management), **platform-specific localization** (Xcode, Android, Figma), and **local translation engines** (offline models for privacy-sensitive workflows).

The headline findings: **DeepL's official server is the most popular translation MCP server** at 95 stars with text, document, and glossary support. **Crowdin's hosted MCP server exposes 200+ tools** — one of the largest tool counts in any MCP category. **Intlayer leads developer i18n tools by stars** (627) with per-component internationalization across React, Next.js, Vue, and Svelte. **Lara Translate uniquely offers full translation memory management** through MCP. **Google Cloud Translation has no MCP server** despite Google's broad MCP investment elsewhere. **Most TMS servers are official vendor implementations** — a refreshing contrast with categories where fragmented community servers dominate.

**Category:** [Education & Learning](/categories/education-learning/)

## Translation API Servers

### DeepLcom/deepl-mcp-server (Most Popular)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [DeepLcom/deepl-mcp-server](https://github.com/DeepLcom/deepl-mcp-server) | 95 | JavaScript | MIT | 8+ |

The official DeepL MCP server and the most starred translation server in the category. Provides text translation between 30+ languages, document translation (PDF, DOCX, PPTX, XLSX, HTML, TXT, and more), and text rephrasing with tone/style customization (business, academic, casual).

Key features beyond basic translation:

- **Glossary support** — list, retrieve, and use glossaries for consistent terminology across projects
- **Formality control** — adjust output formality level for languages that distinguish formal/informal registers
- **Language detection** — automatic source language identification
- **Document translation** — preserves formatting across file types

DeepL's free API tier allows 500,000 characters per month at no cost, making this accessible for experimentation. Integrates with Claude Desktop, Claude Code, and other MCP clients. 83 commits show active maintenance.

### translated/lara-mcp (Translation Memory Pioneer)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [translated/lara-mcp](https://github.com/translated/lara-mcp) | 79 | TypeScript | MIT | 11 |

Lara Translate's MCP server stands out with **full translation memory management** — a capability no other translation MCP server offers. While most servers treat translation as a stateless API call, Lara Translate lets agents build and maintain translation memories over time:

- **translate** — core translation with language detection, context awareness, glossary, and TM integration
- **list_memories / create_memory / update_memory / delete_memory** — full CRUD for translation memories
- **add_translation / delete_translation** — manage individual translation units within memories
- **import_tmx / check_import_status** — bulk import from TMX files (industry-standard format)
- **list_glossaries / get_glossary** — terminology management

Lara Translate's models are trained on professional translation data, emphasizing performance on non-English language pairs where general-purpose MT often struggles. Supports both HTTP and STDIO protocols with Docker deployment.

### neosun100/translategemma (Local/Private Translation)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [neosun100/translategemma](https://github.com/neosun100/translategemma) | 2 | Python | — | 1+ |

The only fully local translation MCP server, powered by Google's TranslateGemma models. For organizations that can't send content to external APIs — healthcare, legal, government — this is the only MCP option:

- **55 language support** from TranslateGemma's multilingual models
- **Multiple model sizes** — 4B, 12B, and 27B parameters with Q4 and Q8 quantization
- **All-in-one Docker image** (82GB) with all 6 models embedded, or lightweight image with on-demand download
- **Smart text chunking** for handling documents longer than the model's context window
- Web UI + REST API + MCP integration

The tradeoff is size and speed — an 82GB Docker image is impractical for casual use, and local inference on consumer hardware will be slower than API calls. But for air-gapped or privacy-sensitive environments, this is currently the only game in town.

### intento/mcp-intento-translate (Multi-Engine Aggregation)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [intento/mcp-intento-translate](https://github.com/intento/mcp-intento-translate) | 2 | Python | Apache-2.0 | 1 |

Intento's MCP server provides **multi-engine translation aggregation** — instead of committing to one translation provider, Intento routes requests to the best-performing engine for each language pair. A single `translate` tool accepts text, target language, and optional source language (auto-detected if omitted). Language support is always up-to-date with the Intento API, with a `language-codes` resource providing ISO code mappings.

## Enterprise Translation Management Systems

### Crowdin MCP Server (Largest Tool Count)

Crowdin's official hosted MCP server is one of the most comprehensive MCP servers in any category, exposing **200+ tools** that cover the full localization lifecycle:

- **Project management** — create, configure, and monitor translation projects
- **File operations** — upload source files, download translations, manage file structures
- **Team coordination** — assign translators, track progress, manage permissions
- **Terminology management** — maintain glossaries across projects
- **Translation memory** — leverage past translations for consistency and efficiency
- **Reporting** — generate analytics, progress reports, and workflow summaries
- **Pre-translation** — automated translation using TM, MT, or AI engines

The server connects via Crowdin's hosted infrastructure — no local installation required. Works with Claude Desktop, Cursor, and other MCP-compatible clients. Crowdin is also building an MCP marketplace in the Crowdin Store for third-party localization MCPs.

Crowdin (the platform) has 500,000+ users and supports 100+ file formats, making this the most battle-tested TMS behind any MCP server.

### phrase/phrase-mcp-server (Official, Dual-Product)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [phrase/phrase-mcp-server](https://github.com/phrase/phrase-mcp-server) | 3 | TypeScript | MIT | 65 |

Phrase's official MCP server covers both of their products:

**Phrase Strings (47 tools):**
- Project management — create, list, configure translation projects
- Job operations — create, manage, and track translation jobs
- Locale management — add, remove, and configure target languages
- Glossary creation and terminology maintenance
- Key and translation CRUD operations
- File upload and download

**Phrase TMS (18 tools):**
- Project creation and management
- Async file downloads for large translation sets
- Job searching and filtering
- Translation workflow operations

Supports configurable product selection (enable Strings, TMS, or both), regional deployment (EU/US), and per-product API token authentication. 104 commits indicate active development.

### AbdallahAHO/lokalise-mcp (Most Automated)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [AbdallahAHO/lokalise-mcp](https://github.com/AbdallahAHO/lokalise-mcp) | 4 | TypeScript | MIT | 59 |

An unofficial but impressively comprehensive Lokalise MCP server with **59 tools across 11 domains** and **17 pre-built automation templates**:

- **Strategic management** — portfolio analysis, project health monitoring, team coordination
- **Content operations** — bulk key operations (1,000+ simultaneously), filename filtering, platform tagging
- **Global expansion** — language addition, progress tracking, completion analytics
- **Team orchestration** — user groups, permissions, workload distribution
- **Workflow automation** — file processing, TM + MT integration, multi-stage review pipelines
- **Real-time monitoring** — process dashboards, audit trails, bulk operation tracking
- **Enterprise security** — multi-layer authentication, secure token handling, rate limiting

The 17 prompt templates cover project management (4), localization workflows (3), advanced automation (4), and enterprise operations (5). One-click installation via Smithery. 118 commits show sustained development.

### Jacobolevy/smartling-mcp-server (Enterprise TMS)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [Jacobolevy/smartling-mcp-server](https://github.com/Jacobolevy/smartling-mcp-server) | 0 | TypeScript | MIT | 10+ |

Smartling's MCP server covers 10 capability areas for enterprise localization:

- Project management, file operations, job management
- String operations for searching and filtering translation content
- Quality assurance checks on translations
- Locale management for project languages
- Glossary and terminology tools
- Context management for sharing visual references with translators
- Webhook configuration for event notifications
- Reporting and analytics

141 commits suggest substantial development despite zero GitHub stars — likely because Smartling's enterprise customer base uses it through Smartling's platform rather than discovering it on GitHub.

### Nativ-Technologies/nativ-mcp (Brand-Aware Translation)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [Nativ-Technologies/nativ-mcp](https://github.com/Nativ-Technologies/nativ-mcp) | 1 | Python | MIT | 8 |

Nativ's MCP server focuses on **brand-consistent localization** with 8 tools:

- **translate / translate_batch** — single and multi-text translation with TM, style guide, and brand voice integration
- **search_translation_memory** — fuzzy-search existing translations for consistency
- **add_translation_memory_entry** — build TM quality over time
- **get_languages** — access configured languages with formality settings
- **get_translation_memory_stats** — TM metrics and breakdown
- **get_style_guides / get_brand_voice** — retrieve brand guidelines for consistent output

The brand voice integration is unique — most translation servers treat every text identically, while Nativ ensures translations match your organization's established tone and terminology.

## Developer i18n Tools

### aymericzip/intlayer (Most Starred)

| Server | Stars | Language | License | Commits |
|--------|-------|----------|---------|---------|
| [aymericzip/intlayer](https://github.com/aymericzip/intlayer) | 627 | TypeScript | Apache-2.0 | 5,207 |

Intlayer is a comprehensive i18n framework for React, Next.js, Vue, and Svelte with a built-in MCP server for IDE automation. The MCP server is one component of a larger platform that includes:

- **Per-component content declaration** — define translations alongside your components
- **MCP-powered IDE automation** — run `intlayer dictionaries build` and `intlayer dictionaries fill` commands through AI assistants
- **231 language support** via AI-powered translation
- **TypeScript autocompletion** for translation keys
- **Visual editor** for non-technical team members
- **CDN delivery** via Cloudflare for instant translation updates without rebuilding
- **Tree-shakable dictionaries** — only ship translations that are actually used

At 627 stars and 5,207 commits, this is by far the most mature project in the i18n MCP space, though the MCP server is a relatively recent addition to an established framework.

### gtrias/i18next-mcp-server (Most Developer-Focused)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [gtrias/i18next-mcp-server](https://github.com/gtrias/i18next-mcp-server) | 12 | TypeScript | MIT | 12 |

A purpose-built MCP server for managing i18next translation files with 12 tools across four areas:

**Core:** `get_project_info`, `health_check`, `scan_code_for_missing_keys`
**Key management:** `add_translation_key`, `sync_missing_keys`, `get_missing_keys`
**File operations:** `list_files`, `validate_files`, `export_data`
**Analysis:** `coverage_report`, `usage_analysis`, `quality_analysis`

The `scan_code_for_missing_keys` tool is particularly valuable — it analyzes your codebase for translation function calls and identifies keys that exist in code but not in your translation files. Combined with `coverage_report`, this gives a complete picture of your localization completeness. Configured via environment variables for project root, locales path, default language, and supported languages.

### reinier-millo/i18n-mcp-server (Chunk-Based Translation)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [reinier-millo/i18n-mcp-server](https://github.com/reinier-millo/i18n-mcp-server) | 9 | TypeScript | AGPL-3.0 | 4 |

Takes a pragmatic approach to translating JSON language files: instead of sending entire files to a translation model at once (which can exceed context limits), it breaks translations into configurable chunks:

1. Read the base language file and list of supported languages
2. Extract chunks of strings (recommended: 250 entries per chunk)
3. Translate each chunk sequentially
4. Cache translations in memory during the workflow
5. Save completed translations to language-specific JSON files

Tested with GPT-4.1 — the developer recommends generating one language at a time for faster results. The chunk-based approach makes it practical for large translation files that would otherwise exceed token limits.

### better-i18n/oss (CDN-Powered)

| Server | Stars | Language | License | Commits |
|--------|-------|----------|---------|---------|
| [better-i18n/oss](https://github.com/better-i18n) | 8 | TypeScript | — | — |

Better i18n bundles its MCP server into a broader TypeScript SDK for Next.js, React, and Expo/React Native. Key differentiators:

- **GitHub Sync** — translations live in your repo, changes create PRs
- **Context-aware AI translation** using Google Gemini (not word-by-word machine translation)
- **Cloudflare CDN delivery** — serve translations from the edge, update without rebuilding
- **MCP server** for AI coding agents to manage translations through natural language

The MCP server enables agents in Cursor, Claude Code, Windsurf, Zed, and Codex to interact with the translation workflow. Runs locally via `npx @better-i18n/mcp`.

## Platform-Specific Localization

### zhangyu1818/xcode-i18n-mcp (iOS/macOS)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [zhangyu1818/xcode-i18n-mcp](https://github.com/zhangyu1818/xcode-i18n-mcp) | 3 | TypeScript | MIT | 3 |

Three focused tools for Xcode String Catalog (`.xcstrings`) localization:

- **getKnownRegions** — extract supported languages from `.pbxproj` files
- **getStringsToTranslate** — identify untranslated strings for specific language codes
- **updateTranslations** — write translated strings back to String Catalog files

Supports Xcode 15+ String Catalog format (JSON-based). Type-safe implementation with Zod schema validation and comprehensive error handling. The entire codebase was generated through AI assistance.

### realskyrin/android-i18n-mcp (Android)

Android localization through Git-aware string resource management:

- **Change detection** — uses Git diff to identify modified strings in default `strings.xml` files across all modules
- **28 language support** — configurable via `TRANSLATION_LANGUAGES` environment variable
- **Auto-creation** — creates missing language directories and populates them with translations

Practical for teams that want to keep translations in sync with code changes — when you modify a string in your default locale, the server detects the change and translates it to all configured languages.

### doubleA411/figma-i18n-mcp (Design-to-i18n)

Extracts text from Figma frames and designs into i18n-ready JSON format:

- Automatically extracts all visible text nodes from Figma files
- Organizes text into structured JSON grouped by frames and components
- Outputs ready for direct use with i18n libraries

Bridges the gap between design and development localization — designers define text in Figma, this server extracts it into a format developers can use directly in their i18n setup.

## What's Missing

The translation and localization MCP landscape has meaningful gaps:

**No Google Cloud Translation MCP server.** Despite Google's extensive MCP investment (Gemini, Vertex AI, Cloud tools), there's no official or prominent community MCP server for Google Cloud Translation. This is a surprising omission given that Google Translate is one of the most widely used translation services.

**No Transifex or Mozilla Pontoon MCP servers.** Two major open-source localization platforms have no MCP presence. Transifex serves large open-source projects, and Pontoon powers Mozilla's extensive localization ecosystem.

**Limited local translation options.** TranslateGemma is the only fully local option, and its 82GB Docker image makes it impractical for most development workflows. There's room for lighter-weight local translation servers using smaller models.

**No cross-TMS abstraction.** Organizations using multiple TMS platforms (common during migrations or with different teams) have no way to manage translations across Crowdin, Phrase, and Lokalise through a unified MCP interface.

**No subtitle/caption localization server.** Despite the popularity of video content, there's no MCP server focused on subtitle translation and timing synchronization.

**Limited right-to-left (RTL) tooling.** No server specifically addresses RTL language challenges — bidirectional text handling, layout mirroring, or Arabic/Hebrew-specific translation quality checks.

## The Bottom Line

The translation and localization MCP ecosystem earns **3.5 out of 5**. Enterprise TMS platforms are impressively comprehensive — Crowdin's 200+ tools and Phrase's 65 tools rival the most complete MCP servers in any category. DeepL provides a solid, well-maintained translation API wrapper. Developer i18n tools are practical and growing, with Intlayer and i18next-mcp-server addressing real workflow pain points.

**Best translation API wrapper:** DeepL MCP Server — official, 95 stars, glossary support, document translation, free tier available.

**Best TMS integration:** Crowdin MCP Server — 200+ tools covering the full localization lifecycle, hosted infrastructure, battle-tested platform.

**Best developer i18n tool:** i18next-mcp-server — 12 focused tools for missing key detection, coverage analysis, and automated sync.

**Best for privacy:** TranslateGemma — the only fully local option with 55-language support via Google's open models.

**Best for brand consistency:** Nativ MCP — unique brand voice and style guide integration for on-brand translations.

The category's strength is vendor participation — most servers are official or semi-official, which means better maintenance and alignment with platform capabilities. The weakness is adoption: outside DeepL and Intlayer, most servers have minimal GitHub stars, suggesting the translation industry is still early in MCP adoption. As more development teams integrate AI assistants into their workflows, expect rapid growth in this category.

*This review was last edited on 2026-03-16 using Claude Opus 4.6 (Anthropic).*

