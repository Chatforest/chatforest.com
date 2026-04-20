# News, Media & Journalism MCP Servers — RSS Feeds, Hacker News, News APIs, Podcasts, and Fact-Checking

> News and media MCP servers let AI agents aggregate RSS feeds, monitor Hacker News and Product Hunt, query news APIs, transcribe podcasts, and fact-check headlines.


*Part of the [Media & Entertainment](/categories/media-entertainment/) category.*

News and media MCP servers let AI assistants aggregate RSS feeds, monitor tech community discussions, query news APIs across regions and topics, transcribe podcasts, and fact-check headlines. Instead of manually checking multiple news sources, refreshing Hacker News, or subscribing to scattered RSS feeds, these servers let AI agents monitor, analyze, and summarize information flows — all through the Model Context Protocol.

This review covers the **news, media, and journalism** vertical — RSS feed aggregation, tech community platforms (Hacker News, Product Hunt), news API integrations, podcast discovery and transcription, and fact-checking tools. For social media platforms, see our [Social Media & Marketing MCP review](/reviews/social-media-marketing-mcp-servers/). For web scraping and content extraction, see our [CMS & Content Management MCP review](/reviews/cms-content-management-mcp-servers/).

The headline findings: **RSS has 10+ implementations** making it the most crowded subcategory. **Hacker News rivals YouTube** as one of the most MCP-served single platforms. **@newsmcp/server offers free real-time news** across 12 topics and 30+ regions with no API key. **Podcast transcription bridges audio to searchable text.** **Fact-checking exists but is a single implementation.** **No major news organizations have released official MCP servers yet.**

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
| [pedramamini/RSSidian](https://github.com/pedramamini/RSSidian) | 24 | Python | Not specified | 6+ |

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

The veithly/rss-mcp server deserves mention for its **RSSHub support** — RSSHub generates RSS feeds for websites that don't offer them natively, and this server includes a built-in list of public RSSHub instances with automatic failover. The kwp-lab implementation adds **full article content extraction**, not just feed summaries.

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

## News APIs & Aggregation

### @newsmcp/server

A **free, no-API-key news server** that clusters events from hundreds of sources:

- **12 topic categories** — automatically classified news events
- **30+ geographic regions** — global coverage with regional filtering
- **Event clustering** — related articles grouped into coherent events
- **Importance ranking** — stories ranked by significance
- **No authentication** — completely free to use

This is the easiest way to add real-time world news to an AI agent. The event clustering is the key differentiator — instead of getting a flat list of articles, you get semantically grouped events with multiple source perspectives.

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

A commercial service connecting LLMs to **rights-cleared, proprietary news data** from trusted sources. Covers news, sports, financial data, and crypto with proper licensing — important for applications where content rights matter.

## Product Hunt

### jaipandya/producthunt-mcp-server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [jaipandya/producthunt-mcp-server](https://github.com/jaipandya/producthunt-mcp-server) | — | — | Not specified | Multiple |

**Real-time access to Product Hunt** including trending posts, comments, collections, users, and product details. Useful for market research, competitive analysis, and tracking new product launches in the tech ecosystem.

## Multi-Source Intelligence

### mnemox-ai/idea-reality-mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [mnemox-ai/idea-reality-mcp](https://github.com/mnemox-ai/idea-reality-mcp) | — | — | Not specified | 1 |

A **pre-build reality check** for AI coding agents. Scans 5 real-time sources — GitHub, Hacker News, npm, PyPI, and Product Hunt — and returns a 0-100 "reality signal" with repo counts, star counts, top competitors, and pivot suggestions. Not a news server per se, but a creative use of news/community data for product validation.

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

### Other Podcast Servers

| Server | Key Feature |
|--------|-------------|
| [oscargullberg/apple-podcast-mcp-server](https://github.com/oscargullberg/apple-podcast-mcp-server) | Lightweight Apple iTunes Store API search |
| [infinitimeless/podcrawler-mcp](https://github.com/infinitimeless/podcrawler-mcp) | Podcast discovery via web crawling for RSS feeds |
| Pod Engine | Commercial hosted podcast MCP server |

The podcrawler-mcp approach is interesting — instead of relying on a fixed podcast directory, it crawls the web to discover podcast episodes and RSS feeds on specific topics.

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

## What's Missing

The gaps in this category are notable:

- **No official news organization servers** — Reuters, AP, Bloomberg, BBC, CNN, NYT (beyond the basic API wrapper), The Guardian, and every other major news outlet have no official MCP servers
- **No media monitoring dashboards** — tools like Meltwater, Cision, or Mention have no MCP presence
- **No editorial workflow tools** — no newsroom collaboration, story assignment, or publication pipeline servers
- **No social listening** — no servers focused on tracking news sentiment or public reaction across platforms
- **No wire service access** — no AP Newswire, Reuters Connect, or similar professional news feeds
- **No press release distribution** — no PR Newswire, BusinessWire, or GlobeNewswire integrations
- **No archive access** — no newspaper archive or historical news database servers (though the [Wayback Machine servers](/reviews/library-archive-museum-mcp-servers/) partially address this)

The category is heavily skewed toward **content consumption** (reading feeds, browsing HN) rather than **content production** (writing, editing, publishing). This makes sense — most MCP users are developers consuming news, not journalists producing it — but it means the journalism side of "news and media" is essentially unserved.

## Bottom Line

**Rating: 3.5/5** — Good coverage for RSS aggregation and tech community monitoring, with genuine utility in the RSS and Hacker News subcategories. The @newsmcp/server's free real-time news clustering is a standout. However, the ecosystem is fragmented (8+ near-identical HN implementations), journalism production tools are absent, and no major news organizations have embraced MCP yet. Best for developers who want to add news monitoring to AI workflows; not yet useful for professional journalists or newsrooms.

*This review was last edited on 2026-03-16 using Claude Opus 4.6 (Anthropic).*

