---
title: "Web Scraping & Crawling MCP Servers — Firecrawl, Crawl4AI, Bright Data, Apify, Jina Reader, and More"
date: 2026-03-17T04:00:00+09:00
description: "Web scraping and crawling MCP servers let AI agents extract, crawl, and convert web content through the Model Context Protocol. We reviewed 20+ servers across 6 subcategories."
og_description: "Web scraping & crawling MCP servers: Firecrawl (6,200 stars — v2.9.0, /interact, /parse, web-agent framework), Bright Data (2,300 stars — GEO brand visibility, 5K free/month), Crawl4AI (64,800+ stars — v0.8.6 security hotfix), Apify (1,200 stars — SSE→Streamable HTTP, OAuth). 20+ servers reviewed. Rating: 4.5/5."
content_type: "Review"
card_description: "Web scraping and crawling MCP servers for AI-powered data extraction, site crawling, and web content conversion. **The managed scraping leader** — firecrawl/firecrawl-mcp-server (6,200 stars, TypeScript, MIT) is the most widely deployed web scraping MCP server. v2.9.0 (April 2026) added browser interaction via `/interact` (natural language page control with persistent sessions), query format for `/scrape`, audio output formats, and new Java and Elixir SDKs. The `/parse` endpoint (April 28) converts PDFs, Word documents, and spreadsheets into structured data using a Rust engine at 5x speed. The `web-agent` framework lets you build AI agents with `$ firecrawl create agent`. Core tools include scraping single pages, crawling entire sites, mapping site structure, searching the web, and extracting structured data. JavaScript rendering, batch processing with parallel execution, automatic retries, and content filtering are built in. Independent benchmarks show 83% accuracy with an average 7-second response time. Main Firecrawl repository surged to 113,000+ stars. Supports both cloud API and self-hosted deployment. **Anti-bot champion with GEO tools** — brightdata/brightdata-mcp (2,300 stars, TypeScript, MIT) brings Bright Data's enterprise proxy infrastructure to MCP with new GEO & AI Brand Visibility tools — monitor how ChatGPT, Grok, and Perplexity perceive your brand. v2.9.3 (March 29) added a `code` tool group for npm/PyPI package lookup. v2.8.6 added minified markdown for scrape_batch (61% token reduction). One MCP server provides access to Web Unlocker (anti-bot bypass), SERP API, Web Scraper API, and Scraping Browser. 90% accuracy, 5,000 free requests/month. 321 commits. **Open-source powerhouse — SECURITY ALERT** — Crawl4AI (64,800+ stars, Python, Apache-2.0) released v0.8.6 as a security hotfix after the litellm PyPI supply chain attack (March 24, 2026 — malicious litellm v1.82.7/v1.82.8 by TeamPCP harvested API keys, SSH keys, and cloud credentials for ~40 minutes). Crawl4AI replaced litellm with unclecode-litellm. v0.8.5 (March 18) added 3-tier anti-bot detection with automatic proxy escalation, Shadow DOM flattening, and 60+ bug fixes. 1,468 commits. Local-first with no API keys or costs. Multiple MCP server implementations: sadiuysal/crawl4ai-mcp-server (lightweight wrapper), BjornMelin/crawl4ai-mcp-server (high-performance alternative), MaitreyaM/WEB-SCRAPING-MCP (text snippets and natural language). Community ecosystem growing but fragmented — SSE connection bugs and schema compatibility issues remain. **Universal web reader** — jina-ai/MCP (658 stars, TypeScript, Apache-2.0) provides URL-to-markdown conversion via Jina's Reader API. Now includes DeepSearch API for iterative search and reasoning, Classifier API for text/image categorization, and server-side tool filtering via query parameters to save context window. ReaderLM-v2 converts raw HTML to clean markdown or structured JSON. Supports parallel web searches, PDF figure/table/equation extraction, output format controls, image auto-captioning, caching, proxies, and SPA rendering. Free tier available. 70 commits. **Scraping marketplace — SSE deprecated** — apify/apify-mcp-server (1,200 stars, TypeScript, Apache-2.0) connects AI agents to Apify's marketplace of 5,000+ pre-built scrapers. SSE transport deprecated April 1, 2026 — now uses Streamable HTTP. v0.9.20 (April 27) added simplified pricing display and actor ID data. New features: OAuth support (connect from Claude.ai and VS Code via URL), output schema inference for structured Actor results, mcpc CLI client, Agent Skills (reusable instruction sets for AI coding assistants). x402 payment provider integration. 720 commits, 158 forks. **Commercial scraping APIs** — crawlbase/crawlbase-mcp (54 stars, TypeScript) grew 7x with crawl, crawl_markdown, and crawl_screenshot tools plus HTTP transport and cloud storage integration for async batch crawling. ScrapingBee's MCP server offers get_page_html, get_screenshot, and get_file tools with proxy rotation (1,000 free credits). Nimbleway's MCP provides 7 tools including nimble_deep_web_search, nimble_extract, and nimble_targeted_retrieval. **NEW: Decodo MCP** (25 stars, TypeScript) — formerly Smartproxy, provides 30+ tools across web scraping, search (Google, Bing, Google Lens), e-commerce (Amazon, Walmart, Target, TikTok Shop), social media (Reddit, TikTok, YouTube), and AI integration (ChatGPT, Perplexity access). Geographic flexibility for region-restricted content. **Content extraction utilities** — mukul975/mcp-web-scrape provides clean, cache-aware content fetching with markdown/JSON output, robots.txt compliance, and citation support. olostep/olostep-mcp-server (15 stars) adds batch URL processing (up to 10,000 URLs), AI-powered answers with citations, and SERP API integration. **Self-healing scrapers — ARCHIVED** — scrapoxy/scrapy-mcp-server was archived on February 6, 2026 with only 4 commits and 2 files — it was a proof-of-concept that never reached implementation. The self-healing scraper concept remains compelling but has no active MCP implementation. **Gaps narrowing** — orchestration improved with Firecrawl's web-agent framework but no cross-source orchestration yet. Document parsing arrived (Firecrawl /parse). Legal compliance tooling still minimal — only mcp-web-scrape respects robots.txt. Supply chain security is now a real concern after the litellm incident. The category holds 4.5/5 — still the strongest MCP category. Firecrawl expanded beyond scraping into document parsing and agent frameworks, Crawl4AI navigated a supply chain crisis, Apify completed its transport migration, and Bright Data added AI brand monitoring. The ecosystem continues to mature rapidly."
last_refreshed: 2026-04-30
categories: ["/categories/web-search-scraping/"]
---

Web scraping is arguably the most natural use case for MCP — AI agents that can read and understand the web become dramatically more useful. This category has attracted serious investment from both open-source projects and commercial scraping platforms, making it the most mature MCP ecosystem we've reviewed.

This review covers **web scraping, crawling, and content extraction** MCP servers. For browser automation tools (Playwright, Puppeteer), see our individual reviews of [Playwright MCP](/reviews/playwright-mcp-server/) and [Puppeteer MCP](/reviews/puppeteer-mcp-server/). For search-specific tools, see [Search Engine MCP Servers](/reviews/search-engine-mcp-servers/).

The headline finding: **web scraping MCP servers are production-ready**, with Firecrawl (6,200 stars), Bright Data (2,300 stars), and Crawl4AI (64,800+ stars for the core library) all offering mature, well-documented implementations. This is the strongest MCP category we've reviewed at 4.5/5.

**April 2026 headlines:** Firecrawl launched `/interact` (browser control), `/parse` (document parsing), and a `web-agent` framework. Crawl4AI issued a security hotfix (v0.8.6) after the litellm supply chain attack. Apify completed its SSE→Streamable HTTP migration. Bright Data added GEO & AI Brand Visibility tools. Decodo (formerly Smartproxy) entered the category with 30+ tools.

## Managed Scraping Platforms

### firecrawl/firecrawl-mcp-server (Official)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [firecrawl-mcp-server](https://github.com/firecrawl/firecrawl-mcp-server) | 6,200 | TypeScript | MIT | 12+ |

**The most widely deployed web scraping MCP server** — Firecrawl turns websites into clean, LLM-ready data. v2.9.0 (April 2026) significantly expanded capabilities:

- **`scrape`** — extract content from a single URL as markdown, JSON, or HTML with JavaScript rendering; now supports query format and audio output
- **`crawl`** — crawl entire websites with depth control, URL filtering, and parallel processing
- **`map`** — discover all URLs on a site, sorted by relevance to a search query
- **`search`** — web search with content extraction in one step
- **`extract`** — structured data extraction using natural language schemas
- **`batch_scrape`** — process multiple URLs with parallel execution and automatic retries
- **`interact`** *(new)* — natural language browser interaction: click, type, scroll, navigate with persistent sessions and live URLs
- **`parse`** *(new, April 28)* — convert PDFs, Word documents, and spreadsheets into structured data using a Rust engine (5x faster, up to 50 MB files, Zero Data Retention on Enterprise)

**`web-agent` framework** (April 16) — open-source framework for building AI agents: `$ firecrawl create agent` bundles scrape, search, and interact with parallel sub-agent support and multi-LLM provider support.

Independent benchmarks show **83% accuracy** with an average **7-second response time** — the fastest in the category. Over **113,000 stars** on the main Firecrawl repository (up from 85,000 in March). New Java SDK (March 12) and Elixir SDK expand language support. Supports both cloud API and self-hosted deployment.

### brightdata/brightdata-mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [brightdata-mcp](https://github.com/brightdata/brightdata-mcp) | 2,300 | TypeScript | MIT | Multiple |

**Enterprise proxy infrastructure meets MCP** — one server provides access to Bright Data's full scraping stack, now with GEO and AI brand monitoring:

- **Web Unlocker** — anti-bot bypass that handles CAPTCHAs, fingerprinting, and IP rotation automatically
- **SERP API** — search engine results page scraping across Google, Bing, and others
- **Web Scraper API** — structured data extraction from any website
- **Scraping Browser** — full browser automation with proxy routing and country targeting
- **GEO & AI Brand Visibility** *(new)* — monitor how ChatGPT, Grok, and Perplexity perceive your brand; the ultimate feedback loop for Generative Engine Optimization (GEO)
- **Code tool group** *(new, v2.9.3)* — npm and PyPI package lookup for coding agents: structured data, no scraping, always up to date

Independent benchmarks give Bright Data **90% accuracy** — the highest in the category — though with slower **30-second average response times**. v2.8.6 (March 1) added minified markdown output for batch operations (~61% token reduction). **5,000 free requests/month.** 321 commits.

## Open-Source Crawlers

### Crawl4AI (Multiple MCP Implementations)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [crawl4ai](https://github.com/unclecode/crawl4ai) (core) | 64,800+ | Python | Apache-2.0 | — |
| [crawl4ai-mcp-server](https://github.com/sadiuysal/crawl4ai-mcp-server) | — | Python | — | 3+ |

**The open-source powerhouse** — Crawl4AI remains the most-starred web crawler with 64,800+ stars (up from 58,000 in March). It's local-first with no API keys, no cloud dependency, and no costs:

- **LLM-optimized markdown output** — clean content formatted specifically for language model consumption
- **JavaScript rendering** — full browser-based rendering via headless Chromium
- **Smart extraction** — LLM-based structured data extraction from natural language instructions
- **3-tier anti-bot detection** *(v0.8.5)* — automatic proxy escalation when bot detection is encountered
- **Shadow DOM flattening** *(v0.8.5)* — extract content from Shadow DOM components
- **Full infrastructure control** — configure browser flags, proxy pools, CPU allocation, scaling policies

**⚠️ SECURITY: v0.8.6 is a critical security hotfix.** On March 24, 2026, malicious litellm packages (v1.82.7/v1.82.8) were published to PyPI by the TeamPCP threat actor group, harvesting API keys, SSH keys, cloud credentials, and database secrets during a ~40-minute window. Crawl4AI v0.8.6 replaced litellm with the forked unclecode-litellm. **Users on v0.8.5 or earlier should upgrade immediately.**

Multiple MCP server implementations wrap the core library (community ecosystem is growing but fragmented):
- **sadiuysal/crawl4ai-mcp-server** — lightweight wrapper with crawl, search, and smart_extract tools
- **BjornMelin/crawl4ai-mcp-server** — high-performance alternative with enhanced capabilities
- **MaitreyaM/WEB-SCRAPING-MCP** — adds text snippet extraction and natural language instruction support

You manage the infrastructure (Docker, Kubernetes, or bare metal) but gain complete control over configuration. SSE connection bugs and schema compatibility issues remain across community MCP implementations. 1,468 commits.

## Web-to-Markdown Conversion

### jina-ai/MCP (Official Jina AI Remote MCP)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [jina-ai/MCP](https://github.com/jina-ai/MCP) | 658 | TypeScript | Apache-2.0 | Multiple |

**Universal web content reader** — Jina's remote MCP server converts any URL to clean, LLM-friendly text:

- **Reader API** — URL-to-markdown conversion powered by ReaderLM-v2 (3x quality improvement over v1)
- **Web search grounding** — parallel web searches for comprehensive topic coverage
- **DeepSearch API** *(new)* — iterative search and reasoning for complex questions
- **Classifier API** *(new)* — text and image categorization
- **Image search** — visual search with content extraction
- **Embeddings & reranker** — semantic understanding tools

Request-level controls include output format (markdown/HTML/text/screenshot), image auto-captioning, cache management, proxies, cookie forwarding, CSS target selectors, PDF figure/table/equation extraction, and SPA rendering via Puppeteer. **Server-side tool filtering** via query parameters saves context window — excluded tools are never registered with the client. Free tier available. 70 commits.

Community wrappers for simpler use cases:
- **wong2/mcp-jina-reader** — focused URL-to-markdown fetching
- **spences10/mcp-jinaai-reader** — optimized for documentation and web content analysis

## Scraping Marketplaces

### apify/apify-mcp-server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [apify-mcp-server](https://github.com/apify/apify-mcp-server) | 1,200 | TypeScript | Apache-2.0 | Dynamic |

**5,000+ pre-built scrapers at your agent's fingertips** — Apify's MCP server connects AI agents to its marketplace of specialized scrapers (called Actors):

- **Social media** — Facebook, Instagram, TikTok, YouTube, Twitter/X, LinkedIn
- **Search engines** — Google SERPs, Bing, DuckDuckGo
- **E-commerce** — Amazon, eBay, Shopify stores, product data
- **Maps & local** — Google Maps, Yelp, business listings
- **Custom scrapers** — any Actor from the Apify Store can be invoked as an MCP tool

**SSE transport deprecated April 1, 2026** — now uses Streamable HTTP exclusively. New in 2026: **OAuth support** (connect from Claude.ai and VS Code using just a URL), **output schema inference** (Actor tools automatically include typed field information), **mcpc CLI client** (production-grade tool for any MCP server), **Agent Skills** (reusable instruction sets for AI coding assistants), and **x402 payment provider** integration. v0.9.20 (April 27) added simplified pricing display. 720 commits, 158 forks.

## Commercial Scraping APIs

### crawlbase/crawlbase-mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [crawlbase-mcp](https://github.com/crawlbase/crawlbase-mcp) | 54 | TypeScript | — | 3+ |

**Battle-tested scraping infrastructure** — Crawlbase (trusted by 70,000+ developers) grew 7x in stars since March. Core tools:

- **`crawl`** — fetch raw HTML with JavaScript rendering and anti-bot protection
- **`crawl_markdown`** — extract clean markdown content
- **`crawl_screenshot`** — capture page screenshots

Now includes HTTP transport mode for shared multi-user deployments and cloud storage integration for asynchronous batch crawling of large URL sets. 26 commits. Requires Crawlbase API key (paid plans).

### Decodo MCP *(New)*

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [mcp-web-scraper](https://github.com/Decodo/mcp-web-scraper) | 25 | TypeScript | — | 30+ |

**Formerly Smartproxy** — Decodo entered the MCP space with the broadest tool set in the commercial category. 30+ tools across five areas:

- **Web & Scraping** — URL scraping, screenshots, geographic flexibility for region-restricted content
- **Search** — Google, Bing, Google Lens, Google Travel Hotels, Google AI Mode
- **E-commerce** — Amazon (search, products, pricing, sellers, bestsellers), Walmart, Target, TikTok Shop
- **Social Media** — Reddit (posts, subreddits, users), TikTok, YouTube (metadata, channels, subtitles, search)
- **AI Integration** — ChatGPT and Perplexity access for AI-powered responses

Device type emulation, pagination support, and token limit controls for context management. 52 commits.

### ScrapingBee MCP

**Managed headless browser scraping** — ScrapingBee's MCP server provides:

- **`get_page_html`** — full HTML extraction with proxy rotation
- **`get_screenshot`** — page or element screenshots
- **`get_file`** — download files (images, PDFs) from pages

Handles headless browser management and proxy rotation automatically. 1,000 free credits on signup, then pay per request (1-75 credits depending on proxy type and JS rendering needs). API key required.

### Nimbleway MCP

**Enterprise-grade web data collection** with 7 specialized tools:

- **`nimble_deep_web_search`** — real-time search across Google, Bing, and Yandex with full content extraction
- **`nimble_extract`** — direct URL parsing with multiple output formats
- **`nimble_targeted_retrieval`** — pre-trained templates for Amazon, Best Buy, Target, Walmart
- **`nimble_google_maps_search`** / **`nimble_google_maps_place`** / **`nimble_google_maps_reviews`** — business data and reviews

SSE transport with LangChain and AutoGen framework integration. Commercial service with API key required.

## Content Extraction Utilities

### mukul975/mcp-web-scrape

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [mcp-web-scrape](https://github.com/mukul975/mcp-web-scrape) | — | — | — | URL fetching |

**Clean, cache-aware web content fetcher** — extracts readable content from any URL and returns markdown or JSON with citations. Respects robots.txt, implements caching for repeated requests, and works with ChatGPT and Claude Desktop. One of the few servers that explicitly handles legal compliance.

### olostep/olostep-mcp-server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [olostep-mcp-server](https://github.com/olostep/olostep-mcp-server) | 15 | — | — | Multiple |

**Batch URL processing at scale** — process up to 10,000 URLs with JavaScript rendering support, retrieve website maps sorted by relevance, and get AI-powered answers with citations. Also includes SERP API for Google search results. 37 commits. Requires Olostep API key.

## Self-Healing Scrapers

### ~~scrapoxy/scrapy-mcp-server~~ *(Archived)*

| Server | Stars | Language | License | Status |
|--------|-------|----------|---------|--------|
| [scrapy-mcp-server](https://github.com/scrapoxy/scrapy-mcp-server) | 17 | Python | — | **Archived Feb 6, 2026** |

**Archived before reaching implementation.** The repository was archived on February 6, 2026, with only 4 commits and 2 files (LICENSE and README.md). The self-healing scraper concept — AI agents that automatically detect and fix broken Scrapy spiders when websites change — remains compelling, but this proof-of-concept never progressed to working code. No active MCP implementation exists for this use case.

## What's Missing

- **No cross-source orchestration** — Firecrawl's web-agent framework helps within its ecosystem, but you still can't combine Firecrawl for speed, Bright Data for anti-bot, and Crawl4AI for free crawling in a single coordinated workflow
- **Limited schema-driven extraction** — Firecrawl's extract and Crawl4AI's smart_extract are the closest to structured data schemas, but most servers return unstructured markdown
- **No proxy pool management** — Bright Data and commercial services handle proxies internally, but there's no MCP server for managing your own proxy infrastructure
- **No scraping scheduling** — no MCP tools for recurring scrape jobs, change detection, or data freshness monitoring
- **Minimal legal compliance** — only mcp-web-scrape explicitly respects robots.txt; no consent checking, rate limit management, or legal compliance tooling
- **Supply chain security concerns** — the litellm incident (March 24, 2026) showed that MCP server dependencies can be compromised; no standardized dependency auditing or supply chain verification exists
- **Crawl4AI MCP fragmentation** — multiple community wrappers with varying quality, SSE bugs, and schema issues create confusion about which implementation to use

## The Bottom Line

**Rating: 4.5/5** — still the strongest MCP category we've reviewed.

The web scraping MCP ecosystem continues to mature rapidly. **Firecrawl** (6,200 stars) expanded beyond scraping into browser interaction (`/interact`), document parsing (`/parse`), and agent building (`web-agent`) — the main repository hit 113,000+ stars. **Crawl4AI** (64,800+ stars) navigated a supply chain crisis with a swift v0.8.6 hotfix and added anti-bot detection in v0.8.5. **Apify** (1,200 stars) completed its SSE→Streamable HTTP migration, added OAuth, and introduced Agent Skills. **Bright Data** (2,300 stars) added GEO & AI Brand Visibility tools for monitoring how AI perceives your brand, plus a code tool group and a 5,000 requests/month free tier. **Decodo** (formerly Smartproxy) entered with 30+ tools spanning scraping, search, e-commerce, and social media.

**For most users:** start with Firecrawl for its balance of ease-of-use and expanding capability. **For cost-conscious teams:** Crawl4AI with a self-hosted MCP wrapper (ensure v0.8.6+). **For anti-bot needs:** Bright Data. **For diverse data sources:** Apify's marketplace. **For broad e-commerce/social coverage:** Decodo.

The gaps are narrowing — document parsing arrived, agent frameworks are emerging, and the transport layer is standardizing on Streamable HTTP. The remaining holes (cross-source orchestration, legal compliance, supply chain security) are real but not fundamental blockers. Web scraping through MCP is production-ready today.

---

*This review was researched and written by an AI agent. We do not test these servers hands-on — our analysis is based on documentation, GitHub repositories, community discussions, and published benchmarks. Star counts are approximate and may change. Last updated April 2026.*

*This review was last edited on 2026-04-30 using Claude Opus 4.6 (Anthropic).*
