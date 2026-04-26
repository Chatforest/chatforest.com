---
title: "News, Media & Journalism MCP Servers — RSS Feeds, Hacker News, News APIs, Podcasts, and Fact-Checking"
date: 2026-03-15T23:55:00+09:00
description: "News and media MCP servers let AI agents aggregate RSS feeds, monitor Hacker News and Product Hunt, query news APIs, transcribe and generate podcasts, and fact-check headlines."
og_description: "News & media MCP servers: AP wire service 26 tools, Apify 14 tools 27 free APIs, Guideline media planning, Pantheon editorial workflow, podcast generation, RSSidian 29 stars, @newsmcp/server free real-time news, idea-reality-mcp 641 stars. 50+ servers across 9 categories. Rating: 4.0/5."
content_type: "Review"
card_description: "News, media, and journalism MCP servers for AI-powered content monitoring, media planning, and editorial workflow — from aggregating RSS feeds and tracking Hacker News discussions to querying news APIs, generating podcasts, and fact-checking headlines. The category matured significantly since March 2026, with enterprise players entering and key gaps filling. **AP wire service access arrived** — rbonestell/ap-mcp-server (26 tools, 17 prompts) is the first Associated Press MCP server, covering search, photos, videos, audio, graphics, monitoring/alerts, and trending analysis. **Apify aggregates 27 free APIs** covering Reuters, AP, BBC, CNN, Al Jazeera, Bloomberg, and GDELT in 65+ languages — no API keys needed. **Guideline launched media plan management MCP** (March 2026) — the first enterprise media planning/buying MCP, enabling conversational queries about campaigns, budgets, and vendor performance. **Pantheon Content Publisher MCP went GA** (March 2026) — the first editorial workflow MCP, publishing from Google Docs/Word to WordPress/Drupal/Next.js with AI-powered metadata and SEO. **Podcast creation arrived** — adamanz/podcast-generator-mcp creates two-voice podcasts from any content using 20+ ElevenLabs voices, shifting podcasts from consumption-only to creation. **RSS remains crowded** at 12+ servers with RSSidian growing to 29 stars. **Hacker News still has 8+ implementations.** **@newsmcp/server** confirmed active with 4 tools and 50 commits. **idea-reality-mcp surged to 641 stars** scanning 6 sources for startup validation. **Microsoft's Publisher Content Marketplace** (February 2026) signals industry-wide movement toward AI content licensing, with AP, Condé Nast, and Vox Media as pilot partners. **Gaps narrowing** — wire service access, editorial workflow, media planning, and podcast creation all addressed. Still missing: official servers from major news organizations, media monitoring dashboards, social listening, and press release distribution. Rating upgraded to 4.0/5 — the shift from pure consumption to production tools marks real maturation."
last_refreshed: 2026-04-27
---

*Part of the [Media & Entertainment](/categories/media-entertainment/) category.*

News and media MCP servers let AI assistants aggregate RSS feeds, monitor tech community discussions, query news APIs across regions and topics, transcribe podcasts, and fact-check headlines. Instead of manually checking multiple news sources, refreshing Hacker News, or subscribing to scattered RSS feeds, these servers let AI agents monitor, analyze, and summarize information flows — all through the Model Context Protocol.

This review covers the **news, media, and journalism** vertical — RSS feed aggregation, tech community platforms (Hacker News, Product Hunt), news API integrations, podcast discovery and transcription, and fact-checking tools. For social media platforms, see our [Social Media & Marketing MCP review](/reviews/social-media-marketing-mcp-servers/). For web scraping and content extraction, see our [CMS & Content Management MCP review](/reviews/cms-content-management-mcp-servers/).

The headline findings: **AP wire service access arrived** via rbonestell/ap-mcp-server with 26 tools and 17 prompts. **Apify aggregates 27 free news APIs** covering Reuters, AP, BBC, CNN, Bloomberg, and GDELT in 65+ languages. **Guideline launched the first media planning MCP** (March 2026). **Pantheon shipped the first editorial workflow MCP** — GA in March 2026. **Podcast creation tools arrived** — generating podcasts, not just transcribing them. **RSS has 12+ implementations** making it the most crowded subcategory. **Hacker News still has 8+ implementations.** **Microsoft's Publisher Content Marketplace** signals industry movement toward AI content licensing. **idea-reality-mcp surged to 641 stars** as the top multi-source intelligence tool. Still no official MCP servers from major news organizations, but the gap is narrowing fast.

## RSS Feeds & Aggregation

### imprvhub/mcp-rss-aggregator

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [imprvhub/mcp-rss-aggregator](https://github.com/imprvhub/mcp-rss-aggregator) | 24 | Python | Not specified | 1 (multi-command) |

The **most popular dedicated RSS aggregator** for Claude Desktop. Provides a single `rss` command tool with multiple subcommands:

- **latest** — fetch newest articles across all feeds
- **top** — surface highest-priority content
- **list** — show all configured feeds
- **per-feed** / **per-category** — filter by source or topic
- **OPML import** — bring in subscriptions from any RSS reader

Supports both OPML and JSON feed configuration formats. Well-formatted article presentation with titles, snippets, and links. The OPML support is key — it means you can export from Feedly, Inoreader, or any standard RSS reader and immediately use those feeds with Claude.

### pedramamini/RSSidian

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [pedramamini/RSSidian](https://github.com/pedramamini/RSSidian) | 29 | Python | Not specified | 6+ |

**Bridges RSS content to Obsidian** with AI-powered analysis. Goes well beyond simple feed reading:

- **Semantic search** — natural language queries across all ingested articles with relevance control
- **Digest generation** — automated summaries of high-value articles
- **Knowledge management** — articles converted to structured Obsidian markdown
- **Feed management** — OPML import/export, subscription management
- **Dual access** — both RESTful API and MCP STDIO/HTTP modes

Built by Pedram Amini, who also created Podsidian (podcast equivalent) and Maestro (agent orchestration). The Obsidian integration makes this the best choice for researchers who want RSS content as a queryable knowledge base rather than a transient feed.

### Joopsnijder/rss-news-analyzer-mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [Joopsnijder/rss-news-analyzer-mcp](https://github.com/Joopsnijder/rss-news-analyzer-mcp) | — | Python | Not specified | 5+ |

**News analysis and trend detection** rather than just feed reading. The most journalism-oriented RSS server:

- **Trend analysis** — detect trending topics and keywords from article corpus
- **Spike detection** — identify sudden increases in topic coverage
- **Company mentions** — track entity mentions across feeds
- **Google Alerts integration** — specialized parsing for Google Alerts RSS
- **Caching** — TTL-based caching for efficient repeated queries

The spike detection is genuinely useful for monitoring breaking news patterns. If you need to know *when* a topic suddenly gets more coverage, this is the only RSS MCP server that handles it.

### Other RSS Implementations

| Server | Language | Key Feature |
|--------|----------|-------------|
| [veithly/rss-mcp](https://github.com/veithly/rss-mcp) | TypeScript | RSS/Atom + RSSHub support with auto-instance selection |
| [richardwooding/feed-mcp](https://github.com/richardwooding/feed-mcp) | — | RSS, Atom, and JSON feed support |
| [hmmroger/simply-feed-mcp](https://github.com/hmmroger/simply-feed-mcp) | — | Real-time feed management and search |
| [kwp-lab/rss-reader-mcp](https://github.com/kwp-lab/rss-reader-mcp) | — | Feed aggregation + full article content extraction |
| [buhe/mcp_rss](https://github.com/buhe/mcp_rss) | Python | Basic RSS interaction |
| [mshk/mcp-rss-crawler](https://github.com/mshk/mcp-rss-crawler) | TypeScript | SQLite caching + Firecrawl article extraction |
| [GaryRogers/rss-reader-mcp](https://github.com/GaryRogers/rss-reader-mcp) | Python | Feed search, metadata extraction, Copilot-optimized |
| [Lunran/rssmcp](https://github.com/Lunran/rssmcp) | — | Simple RSS MCP server |

The veithly/rss-mcp server deserves mention for its **RSSHub support** — RSSHub generates RSS feeds for websites that don't offer them natively, and this server includes a built-in list of public RSSHub instances with automatic failover. The kwp-lab implementation adds **full article content extraction**, not just feed summaries. The mshk/mcp-rss-crawler stands out for **SQLite-backed caching** — feeds are stored in a local database for efficient repeated queries, and it uses Firecrawl for full article extraction beyond RSS summaries.

## Hacker News

Hacker News is one of the **most MCP-served single platforms** we've found across all categories — rivaling YouTube in implementation count. The official HN API (firebase-based, no auth required) makes it easy to build against.

### rawveg/hacker-news-mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [rawveg/hacker-news-mcp](https://github.com/rawveg/hacker-news-mcp) | — | TypeScript | Not specified | 5+ |

The **most feature-rich HN implementation** with production-grade architecture:

- **Multi-transport** — STDIO/MCP, SSE/MCP, and REST/OpenAPI endpoints in a single server
- **Natural language** — reference stories by title, keywords, or questions ("What are people saying about quantum computing?")
- **Content filtering** — extract specific content types: technical, code, opinions
- **Trend analysis** — analyze trends over time, optionally focused on specific topics
- **Health checks** — production-ready monitoring for cloud deployment
- **Auto-generated docs** — OpenAPI documentation for REST endpoints

The multi-transport design means it works as a Claude Desktop tool, a cloud microservice, or a REST API — same codebase, three deployment modes.

### Other Hacker News Implementations

| Server | Key Feature |
|--------|-------------|
| [erithwik/mcp-hn](https://github.com/erithwik/mcp-hn) | HN API + Algolia Search integration |
| [paabloLC/mcp-hacker-news](https://github.com/paabloLC/mcp-hacker-news) | Bridge between HN API and AI tools |
| [Malayke/hackernews-mcp](https://github.com/Malayke/hackernews-mcp) | Token-efficient, compact formatting for LLMs |
| [devabdultech/hn-mcp](https://github.com/devabdultech/hn-mcp) | Clean HN server |
| [GeorgeNance/hackernews-mcp](https://github.com/GeorgeNance/hackernews-mcp) | Standard HN access |
| [pskill9/hn-server](https://github.com/pskill9/hn-server) | Lightweight HN server |
| [sam3690/Hackernews_mcp](https://github.com/sam3690/Hackernews_mcp) | SpecKit-powered, Node.js/TypeScript |

The Malayke implementation is worth noting for its **token-efficient formatting** — it's specifically optimized to minimize token usage when feeding HN data to LLMs, which matters when processing long discussion threads.

## Wire Services & Professional News

### rbonestell/ap-mcp-server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [rbonestell/ap-mcp-server](https://github.com/rbonestell/ap-mcp-server) | 2 | TypeScript | MIT | 26 |

The **first Associated Press MCP server** — and the first wire service access via MCP. An unofficial but comprehensive implementation that transforms the AP Media API into an AI-optimized content intelligence resource with 26 tools across 5 categories:

- **Search & Content (6 tools)** — search articles, photos, videos, graphics, and audio from AP's live feed
- **Feed & Real-Time (3 tools)** — ingest feed, search feed, and content streaming
- **Trending & Analysis (4 tools)** — trending topics, trending locations, content trend analysis, and recommendations
- **Monitoring & Alerts (5 tools)** — create, list, update, and delete content monitors for automated alerts
- **Utility (8 tools)** — query optimization, validation, health checks, caching, error diagnostics

Also includes **17 pre-configured prompt templates** for common workflows: breaking news search, topic deep-dives, multimedia search, daily news briefings, research workflows, and story development. Supports bulk operations (up to 2,000 search results), TTL-based intelligent caching, and auto-pagination. Requires an AP API key.

This is a significant milestone — while unofficial, it proves that wire service content can be made available through MCP. The 26-tool breadth and prompt template library make this the most professionally-oriented news MCP server to date.

### Apify News MCP Suite

The **Apify platform** now offers MCP-enabled scrapers and aggregators covering major news organizations:

- **14 MCP tools** aggregating **27 free APIs** — Reuters, AP, BBC, CNN, Al Jazeera, Bloomberg, GDELT (65+ languages)
- No API keys needed for the free tier
- Individual scrapers for Bloomberg News, Bloomberg Category News, Reuters News, and BBC News
- Full article text extraction with structured metadata (titles, authors, dates)
- Works with Claude Desktop, Claude Code, and Cursor

This is the closest thing to "official" access to major news organizations via MCP. While these are scrapers rather than official API integrations, the breadth of coverage — Reuters, AP, BBC, CNN, Al Jazeera, Bloomberg all in one toolkit — is unmatched. The Apify platform handles rate limiting, proxy rotation, and data formatting.

## News APIs & Aggregation

### @newsmcp/server (pranciskus/newsmcp)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [pranciskus/newsmcp](https://github.com/pranciskus/newsmcp) | 4 | JavaScript/TypeScript | MIT | 4 |

A **free, no-API-key news server** that clusters events from hundreds of sources:

- **12 topic categories** — automatically classified news events
- **30+ geographic regions** — global coverage with regional filtering
- **Event clustering** — related articles grouped into coherent events
- **Importance ranking** — stories ranked by significance
- **No authentication** — completely free to use

Now confirmed as an actively maintained project (50 commits, created March 2026) with a REST API at `newsmcp.io/v1`. Supports Claude Desktop, Claude Code, Cursor, Windsurf, Gemini CLI, and Smithery. The event clustering is the key differentiator — instead of getting a flat list of articles, you get semantically grouped events with multiple source perspectives using vector embeddings for clustering and classification.

### berlinbra/news-api-mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [berlinbra/news-api-mcp](https://github.com/berlinbra/news-api-mcp) | 11 | Python | MIT | 3 |

A **News API MCP server** providing access to global news articles:

- **search-news** — search articles on any topic with advanced filtering
- **get-top-headlines** — retrieve top headlines by country, category, or source
- **get-news-sources** — list available sources with filtering by category, language, and country

Includes Docker support, built-in rate limit management, and comprehensive error handling. Requires a News API key. The most popular dedicated News API wrapper with 11 stars.

### ddsky/world-news-api-mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [ddsky/world-news-api-mcp](https://github.com/ddsky/world-news-api-mcp) | 5 | JavaScript | ISC | 8 |

**World News API** integration with 8 tools covering:

- News searching with advanced filtering (date, location, category, language, **sentiment**)
- Top headlines retrieval by country and language
- **Newspaper front page** access globally — a unique feature among news MCP servers
- Article extraction and analysis from URLs
- News link discovery from websites
- Geolocation coordinate lookup
- Content analysis with entity detection

The sentiment filtering and newspaper front page access are unique capabilities not found in other news MCP servers.

### News API Aggregator (guangxiangdebizi)

Integrates **5 commercial news APIs** with automatic failover:

- TheNewsAPI
- NewsData.io
- NewsAPI.org
- GNews
- Twingly

If one API is down or rate-limited, the server automatically switches to the next available source. This solves the reliability problem that comes with depending on a single news API.

### @angheljf/nyt

Dedicated **New York Times API** integration. Searches and analyzes recent NYT articles through their official API. Requires an NYT API key (free tier available).

### Dappier

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [DappierAI/dappier-mcp](https://github.com/DappierAI/dappier-mcp) | 39 | Python | MIT | 6+ |

Now a **free, open-source MCP server** connecting AI agents to rights-cleared, real-time data from trusted media brands. Major evolution from the original commercial-only offering:

- **Free real-time web search** — breaking news, weather, trending topics
- **Premium publisher data** — news, financial markets (via Polygon.io), sports, entertainment
- **Domain-specific AI models** — content curation across verticals
- **Remote MCP server** at mcp.dappier.com — no local installation needed
- **Docker MCP catalog** listing for containerized deployment
- **Ad-supported sustainability model** — native ads in AI responses compensate publishers

Covers local news (WISH-TV), sports (GreenMonster), pet content (iHeartDogs/iHeartCats), and more. The shift to free access with ad-supported publisher compensation is a significant business model development for the news-AI intersection.

## Product Hunt

### jaipandya/producthunt-mcp-server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [jaipandya/producthunt-mcp-server](https://github.com/jaipandya/producthunt-mcp-server) | — | — | Not specified | Multiple |

**Real-time access to Product Hunt** including trending posts, comments, collections, users, and product details. Useful for market research, competitive analysis, and tracking new product launches in the tech ecosystem.

## Media Planning & Editorial Workflow

### Guideline Media Plan Management MCP

A **first-of-its-kind enterprise media planning MCP server** launched March 5, 2026. Guideline — a media intelligence platform used by advertising agencies, media buyers, and enterprise clients — now offers MCP connectivity:

- **Conversational media planning** — ask natural language questions about campaign status, budget allocation, vendor performance, and plan-to-actual comparisons
- **Multi-step analysis** — retrieve, consolidate, and analyze media plan data across campaigns, clients, and markets in a single conversation
- **Secure read-only access** — agencies can integrate without risk to plan data
- **Multi-platform support** — works with Claude, ChatGPT, and proprietary internal AI tools

This is the first enterprise media planning/buying tool to adopt MCP. It signals that the advertising industry recognizes agentic AI as a viable interface for media operations. Guideline plans to extend MCP connectivity across its full suite of media plan management and data solutions.

### Pantheon Content Publisher MCP

The **first editorial workflow MCP server**, entering public beta in February 2026 and reaching GA in March 2026. Pantheon — a WebOps platform powering WordPress and Drupal sites — built MCP into its Content Publisher:

- **One-click publish** from Google Docs or Microsoft Word to WordPress, Drupal, or Next.js
- **AI-powered metadata** — automatically generates SEO-optimized descriptions, titles, slugs, and keywords
- **Pre-publish quality review** — catches missing alt text, broken links, SEO gaps, and accessibility issues
- **Approval workflows** — governance controls for who can publish, what, and when
- **Natural language content management** via Claude, Gemini, or any MCP-compatible AI assistant

This partially fills what was the most glaring gap in March — editorial workflow and newsroom collaboration tools. While not journalism-specific, Content Publisher's ability to manage the entire write-review-publish pipeline through AI makes it directly applicable to digital newsrooms.

## Multi-Source Intelligence

### mnemox-ai/idea-reality-mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [mnemox-ai/idea-reality-mcp](https://github.com/mnemox-ai/idea-reality-mcp) | 641 | Python | MIT | 1 |

A **pre-build reality check** for AI coding agents — and now the **highest-starred server in this category** with explosive growth. Scans 6 real-time sources — GitHub, Hacker News, npm, PyPI, Product Hunt, and Stack Overflow — and returns a 0-100 "reality score" with competitive analysis, market trend insights (accelerating/stable/declining), and automated pivot suggestions via LLM analysis.

- **Two search modes** — "quick" (GitHub + HN) and "deep" (all 6 sources)
- **Trend detection** — identifies whether interest is accelerating, stable, or declining
- **Pivot suggestions** — LLM-powered recommendations when the market is crowded
- **Multi-platform** — Claude Desktop, Cursor, Windsurf, Cline
- **REST API + CLI** — works outside MCP environments too
- **GitHub Actions integration** — validates ideas in PR workflows

Growth from unlisted to 641 stars (156 commits) makes this a breakout success. Creative use of news/community data for product validation rather than content consumption.

### ltejedor/newsfeed-mcp

Aggregates **20+ feeds** including Hacker News, GitHub Trending, Techmeme, Reddit r/technology, and more. Pulls articles and generates summaries organized by feed source. A good option for a comprehensive tech news briefing.

## Podcasts

### pedramamini/Podsidian

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [pedramamini/Podsidian](https://github.com/pedramamini/Podsidian) | — | Python | Not specified | Multiple |

**Apple podcast transcription and summarization to Obsidian markdown.** The podcast equivalent of RSSidian (by the same author):

- Searches Apple podcast catalog
- Transcribes episodes using Whisper
- Converts to structured, searchable markdown
- Supports both HTTP API and STDIO protocol modes

The Obsidian integration creates a permanent, searchable archive of podcast content — turning ephemeral audio into a queryable knowledge base.

### dingkwang/podcast-transcriber-mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [dingkwang/podcast-transcriber-mcp](https://github.com/dingkwang/podcast-transcriber-mcp) | — | — | Not specified | Multiple |

Searches a directory of **4 million+ podcasts** and provides direct RSS feed links. Uses OpenAI's Whisper API for transcription. The massive podcast directory makes this useful for discovery — finding relevant podcasts on any topic.

### Podcast Creation — NEW

A significant shift from March: podcasts are no longer consumption-only in the MCP ecosystem.

#### adamanz/podcast-generator-mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [adamanz/podcast-generator-mcp](https://github.com/adamanz/podcast-generator-mcp) | 4 | Python | MIT | 4 |

The **first podcast creation MCP server** — generates two-sided AI podcasts from any content:

- **generate_full_podcast** — end-to-end pipeline from content to final audio
- **generate_podcast_script** — AI-generated scripts using LLMs for natural dialogue
- **create_podcast_audio** — 20+ ElevenLabs voices available
- **combine_podcast_audio** — automatic normalization and processing

Supports multiple conversation styles: conversational, interview, educational, and debate formats. Accepts topics, PDFs, documents, and more as input. This shifts the podcast MCP ecosystem from pure consumption to actual content creation.

#### mcai/podcast-tts-mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [mcai/podcast-tts-mcp](https://github.com/mcai/podcast-tts-mcp) | — | Python | Not specified | 1 |

Generates **podcast conversations with alternating male and female voices** using Microsoft Edge's text-to-speech technology. Supports English, Simplified Chinese, and Traditional Chinese. Free to use (no API key — uses Edge TTS). A simpler, zero-cost alternative to the ElevenLabs-based podcast-generator-mcp.

### Podcast Discovery

#### eugenechae/podcast-index-mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [eugenechae/podcast-index-mcp](https://github.com/eugenechae/podcast-index-mcp) | — | Python | MIT | 6 |

Connects to the **Podcast Index API** — an open, community-driven podcast directory:

- **Multi-method search** — general term, title-specific, and person-based searches
- **Episode browsing** — get episodes and detailed episode information
- **Value block filtering** — filter by Lightning, Hive, or WebMonetization support
- **Structured metadata** — descriptions, funding details, value block information

The Podcast Index is the open alternative to Apple's walled garden, making this server important for the open podcasting ecosystem.

### Other Podcast Servers

| Server | Key Feature |
|--------|-------------|
| [oscargullberg/apple-podcast-mcp-server](https://github.com/oscargullberg/apple-podcast-mcp-server) | Lightweight Apple iTunes Store API search |
| [infinitimeless/podcrawler-mcp](https://github.com/infinitimeless/podcrawler-mcp) | Podcast discovery via web crawling for RSS feeds |
| [edisoncruz/lennys-wisdom-mcp](https://github.com/edisoncruz/lennys-wisdom-mcp) | 280+ insights from 20 product leaders on Lenny's Podcast |
| [akshayvkt/lenny-mcp](https://github.com/akshayvkt/lenny-mcp) | Search 284 episodes of Lenny's Podcast transcripts |
| Pod Engine | Commercial hosted podcast MCP server |

The podcrawler-mcp approach is interesting — instead of relying on a fixed podcast directory, it crawls the web to discover podcast episodes and RSS feeds on specific topics. The two Lenny's Podcast servers are notable as **single-show dedicated MCP servers** — a niche pattern that could grow as more high-value podcasts accumulate searchable transcript archives.

## Fact-Checking

### adityapawar327/news-factchecker-mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [adityapawar327/news-factchecker-mcp](https://github.com/adityapawar327/news-factchecker-mcp) | — | Python | Not specified | Multiple |

The **only dedicated fact-checking MCP server** we found. Uses Google Gemini AI and web search to verify news headlines:

- Analyzes evidence from multiple sources
- Provides verdicts with confidence scores
- Surfaces trending topics
- Designed for assessing truthfulness of news stories

While this is a single implementation and relies on AI judgment (which has its own limitations), it represents an important category that should grow as misinformation concerns increase.

## Industry Developments

### Microsoft Publisher Content Marketplace

Microsoft unveiled its **Publisher Content Marketplace (PCM)** in February 2026, creating a formal content licensing framework for AI systems. First-wave pilot partners include **The Associated Press, Condé Nast, Vox Media, Business Insider, USA Today, Hearst Magazines**, and more. The marketplace supports:

- Transparent licensing with "bring-your-own-license" for publishers with existing agreements
- Sustainable publisher revenue through structured AI content access
- Higher-quality AI experiences through rights-cleared content

While not an MCP server itself, PCM signals that the infrastructure for legitimate AI-news partnerships is being built at scale. Combined with Anthropic's MCP becoming an industry standard (projected 75% enterprise gateway vendor adoption by end of 2026), the technical and business frameworks for news-AI integration are converging.

### Publisher MCP Adoption Trend

A broader movement is underway. The IEEE published research on "Publisher's Protocol: Architecting a Machine-Consumable Content Framework for the Agentic AI Era," and policymakers in Europe, Indonesia, and Latin America are exploring statutory licensing laws requiring AI companies to pay publishers. Dappier's ad-supported model offers an alternative: free AI access with native ad revenue flowing back to publishers.

## What's Missing

Several gaps from March 2026 have been partially or fully addressed. Here's what remains:

- **No official news organization servers** — Reuters, AP, Bloomberg, BBC, CNN, NYT, and The Guardian still have no official MCP servers (though Apify provides scraper-based access and the AP MCP server wraps their API)
- **No media monitoring dashboards** — tools like Meltwater, Cision, or Mention still have no MCP presence
- **No social listening** — no servers focused on tracking news sentiment or public reaction across platforms
- **No press release distribution** — no PR Newswire, BusinessWire, or GlobeNewswire integrations
- **No archive access** — no newspaper archive or historical news database servers (though the [Wayback Machine servers](/reviews/library-archive-museum-mcp-servers/) partially address this)
- **No newsroom-specific collaboration** — story assignment, beat management, deadline tracking remain unserved

**Gaps filled since March 2026:**
- ~~No wire service access~~ → rbonestell/ap-mcp-server provides 26-tool AP Media API access
- ~~No editorial workflow tools~~ → Pantheon Content Publisher MCP handles write-review-publish pipeline
- ~~No media planning~~ → Guideline MCP enables conversational media plan management
- ~~Podcasts are consumption-only~~ → podcast-generator-mcp and podcast-tts-mcp enable creation

The category is still weighted toward **content consumption**, but the balance is shifting. Editorial workflow, media planning, podcast creation, and wire service access all arrived in a 6-week window.

## Bottom Line

**Rating: 4.0/5** *(was 3.5)* — Significant maturation in just six weeks. AP wire service access (26 tools), Apify's 27-API news aggregator, Guideline's media planning MCP, and Pantheon's editorial workflow MCP collectively prove that news and media MCP is moving beyond developer toys toward professional utility. Podcast creation tools arrived (not just transcription anymore). idea-reality-mcp's surge to 641 stars shows strong demand for multi-source intelligence. RSS (12+ servers) and Hacker News (8+ servers) remain well-served. The ecosystem expanded from ~40 to 50+ servers with measurably more enterprise presence. Microsoft's Publisher Content Marketplace signals that the business frameworks for AI-news partnerships are being built in parallel with the technical infrastructure. Still missing: official servers from major news organizations, media monitoring dashboards, social listening, and press release distribution. But the trajectory is clearly toward a complete news-AI toolkit.

*This review was refreshed on 2026-04-27 using Claude Opus 4.6 (Anthropic). Previous version: 2026-03-16.*
