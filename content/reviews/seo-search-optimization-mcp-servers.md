---
title: "SEO & Search Optimization MCP Servers — Google Search Console, Ahrefs, Semrush, DataForSEO, SE Ranking, Frase, Moz, Screaming Frog, and Google Trends"
date: 2026-03-17T07:00:00+09:00
description: "SEO and search optimization MCP servers let AI agents perform keyword research, analyze backlinks, audit site performance, and pull Google Search Console data through the Model Context Protocol."
og_description: "SEO MCP servers: mcp-gsc SURGED 428→700+ stars, Semrush NOW OFFICIAL hosted OAuth MCP, SE Ranking expanded 160+ tools + Claude Skills + AI Search visibility, Frase content optimization MCP full pipeline $39/mo, Moz gap FILLED metehan777 13+ tools, Screaming Frog gap FILLED 20 stars 8 tools, Google Trends 4+ servers. 30+ servers. Rating upgraded 4→4.5/5."
content_type: "Review"
card_description: "SEO and search optimization MCP servers for keyword research, backlink analysis, rank tracking, site audits, content optimization, and search console data through AI assistants. **FOUR MAJOR GAPS FILLED** since March — Moz, Screaming Frog, Google Trends, and content optimization all now have MCP servers. **Semrush launched an official hosted MCP server** at mcp.semrush.com with OAuth — joining Ahrefs, DataForSEO, and SE Ranking as the fourth major SEO platform with an official MCP. **mcp-gsc SURGED to 700+ stars** — added uvx zero-install method, get_capabilities tool, and a hosted version with GA4 integration. **SE Ranking expanded to 160+ tools** with 7 ready-to-use Claude Skills and AI Search share of voice tracking across ChatGPT, Gemini, Perplexity, and AI Overviews. **Frase launched the first content optimization MCP** — full pipeline from research through writing, optimization, monitoring, and auto-fix with dual SEO+GEO scoring at $39/mo. **Moz gap filled** — metehan777/moz-mcp (11 stars, 13+ tools) covers Domain Authority, keyword research, link analysis, and competitive intelligence. **Screaming Frog gap filled** — bzsasson/screaming-frog-mcp (20 stars, 8 tools) provides crawl, export, and audit data access. **Google Trends gap filled** — 4+ implementations including jmanek/google-news-trends-mcp and Apify scraper. **Google Business Profile MCP appeared** — local SEO gap narrowing. **Ahrefs fully remote** — Streamable HTTP at api.ahrefs.com, local server deprecated. **cnych/seo-mcp grew** to 225 stars. The category expanded from 20+ to 30+ servers with unprecedented enterprise adoption — every major SEO platform now has MCP connectivity. Rating upgraded to **4.5/5**."
last_refreshed: 2026-05-02
next_priority: "med"
categories: ["/categories/web-search-scraping/"]
---

SEO and search optimization MCP servers connect AI agents to keyword research platforms, backlink analyzers, rank trackers, and search console data. Instead of switching between Ahrefs, Semrush, Google Search Console, and PageSpeed Insights, these servers let AI assistants pull SEO data, analyze performance, and identify opportunities through the Model Context Protocol.

This review covers the **SEO and search optimization** vertical — Google Search Console integration, all-in-one SEO platforms (Ahrefs, Semrush, DataForSEO, SE Ranking), keyword research tools, and technical SEO/PageSpeed analysis. For web scraping and crawling tools that support SEO workflows, see our [Web Scraping & Crawling review](/reviews/web-scraping-crawling-mcp-servers/). For analytics platforms, see our [Analytics MCP review](/reviews/analytics-mcp-servers/).

The headline findings: **Google Search Console surged to 700+ stars** — mcp-gsc is now one of the most popular domain-specific MCP servers anywhere, with uvx zero-install setup and a hosted version adding GA4. **Semrush launched an official hosted MCP** at mcp.semrush.com with OAuth — the fourth major SEO platform to go official. **SE Ranking expanded to 160+ tools** with 7 Claude Skills and AI Search visibility tracking across ChatGPT, Gemini, Perplexity, and AI Overviews. **Frase launched the first content optimization MCP** — research, write, optimize, audit, monitor, and auto-fix with dual SEO+GEO scoring. **Four major March gaps filled** — Moz (13+ tools), Screaming Frog (8 tools), Google Trends (4+ servers), and content optimization (Frase) all now have MCP servers. **Google Business Profile MCP appeared** — local SEO is no longer completely absent. **Every major SEO platform now has MCP connectivity.**

---

## Google Search Console

### AminForou/mcp-gsc — GSC Insights for SEOs

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [mcp-gsc](https://github.com/AminForou/mcp-gsc) | 700+ | Python | — | 19+ |

**The most feature-rich Google Search Console MCP server — and one of the most popular domain-specific MCP servers in the entire ecosystem:**

- **Search analytics** — clicks, impressions, CTR, and position data with flexible date ranges
- **URL inspection** — check indexing status, crawl errors, and coverage issues for any page
- **Sitemap management** — review sitemap status and submit new sitemaps
- **Cannibalization detection** — identify pages competing for the same keywords
- **Multi-dimension filtering** — query by page, country, device, search appearance
- **Data freshness** — freshness indicators so you know how current your data is
- **Flexible row limits** — pull exactly the amount of data you need
- **Multi-client support** — manage multiple GSC properties in one session
- **uvx zero-install** — NEW: `uvx mcp-gsc` downloads and runs the server automatically, no cloning, no Python setup, no virtual environments. OAuth browser flow fixed for uvx subprocess mode
- **get_capabilities tool** — NEW: retrieve full list of available tools and current auth status
- **Hosted version available** — NEW: one-click Google sign-in, no terminal needed, adds GA4 tools. Works in Claude.ai, ChatGPT, Cursor, Claude Desktop

Surged from 428 to 700+ stars since March — the dominant GSC MCP server by a wide margin. The uvx method eliminates the biggest friction point (Python environment setup), and the hosted version makes it accessible to non-technical SEOs. The GSC MCP ecosystem has grown from ~6 to 20+ implementations.

### ahonn/mcp-server-gsc — Enhanced GSC Analytics

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [mcp-server-gsc](https://github.com/ahonn/mcp-server-gsc) | 157 | TypeScript | MIT | Multiple |

**Power-user GSC server with enhanced data extraction:**

- **25,000 row extraction** — pull up to 25K rows of performance data per query
- **Regex filtering** — use regular expressions in query and page filters
- **Multiple filter operators** — contains, exact match, regex, and more
- **Quick wins detection** — automatically identifies optimization opportunities
- **Rich dimensions** — query, page, country, device, and search appearance analysis

The key differentiator is data volume — while the standard GSC API limits data, this server pushes extraction to 25,000 rows, making it suitable for large sites with thousands of pages. MIT licensed, TypeScript-based, and uses service account authentication for a more stable connection than OAuth browser flow.

---

## All-in-One SEO Platforms

### ahrefs/ahrefs-mcp-server — Official Ahrefs Integration

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [ahrefs-mcp-server](https://github.com/ahrefs/ahrefs-mcp-server) | 94 | — | — | Multiple |

**Official Ahrefs MCP server — fully remote, OAuth-only:**

- **Backlink statistics** — retrieve backlink data for any domain or URL
- **Domain rating** — Ahrefs DR metric measuring website authority (0-100 scale)
- **Search volume** — keyword search volume data across different countries
- **Keyword explorer** — find keyword phrases with difficulty, volume, and traffic potential
- **External linking domains** — analyze who links to any site
- **Streamable HTTP** — hosted at `api.ahrefs.com/mcp/mcp` (recommended transport)
- **Legacy SSE** — `api.ahrefs.com/mcp/mcpSse` (deprecated in many clients)

Ahrefs has fully deprecated local setup — the remote MCP server uses OAuth with no API key required. Requires Lite plan or higher. The local repo (94 stars) remains available but is not maintained. This is now the cleanest onboarding experience of any enterprise SEO MCP: just add the URL to your MCP client config and authorize via browser.

### dataforseo/mcp-server-typescript — Official DataForSEO API

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [mcp-server-typescript](https://github.com/dataforseo/mcp-server-typescript) | 150 | TypeScript | — | Hundreds |

**The broadest SEO API coverage through a single MCP server:**

- **SERP API** — real-time search results from Google, Bing, and Yahoo
- **Keywords Data API** — keyword research with search volume, CPC, and clickstream data
- **On-Page API** — crawl websites for on-page SEO metrics and technical issues
- **DataForSEO Labs API** — proprietary algorithms for keyword and domain analysis

At hundreds of exposed tools, this is the most comprehensive SEO MCP server by raw capability. DataForSEO aggregates data from multiple sources, so you get SERP data, keyword metrics, backlink analysis, and on-page crawling through one integration. Requires DataForSEO credentials (paid API). The 150-star count and 95 forks suggest significant production adoption.

### seranking/seo-data-api-mcp-server — Official SE Ranking

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [seo-data-api-mcp-server](https://github.com/seranking/seo-data-api-mcp-server) | — | Node.js | — | 160+ |

**The most complete SEO workflow in a single server — massively expanded since March:**

- **Keyword research** — search volume, difficulty, CPC, and related keywords
- **Domain analysis** — organic and paid traffic, top pages, competitor discovery
- **Backlink data** — referring domains, anchor text, new/lost links
- **SERP analysis** — search result features, rankings, and SERP structure
- **Website audits** — technical SEO crawling and issue detection
- **Project management** — manage SE Ranking projects from within AI assistants
- **Rank tracking** — monitor keyword positions over time
- **Backlink monitoring** — track link acquisition and loss
- **AI Search share of voice** — NEW: track brand mentions and visibility across ChatGPT, Gemini, Perplexity, AI Overviews, and AI Mode. This is a unique capability — SE Ranking is the first SEO MCP to bridge traditional search and AI search monitoring
- **7 Claude Skills** — NEW: ready-to-use MIT-licensed skills wrap the MCP into finished deliverables: content briefs, AI Search share of voice, audit change logs, backlink gap analysis, keyword clusters, competitor gap analysis, and demand-gen landing pages
- **Remote MCP support** — connects natively in Claude, Cursor, and other clients; mcp-remote module available for backwards compatibility

SE Ranking expanded from a strong workflow tool to the **most ambitious SEO MCP offering** with 160+ tools. The AI Search visibility feature is genuinely novel — it tracks how your brand appears in AI-generated answers, not just traditional SERPs. The Claude Skills are also a differentiator: pre-built workflows that turn raw MCP data into actionable deliverables. Requires SE Ranking API access.

### cnych/seo-mcp — Free Ahrefs Data Scraper

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [seo-mcp](https://github.com/cnych/seo-mcp) | 225 | Python | — | Multiple |

**Free access to Ahrefs data without an API key:**

- **Backlink analysis** — domain rating, backlink count, referring domains, anchor text
- **Keyword research** — keyword ideas, difficulty scores, search volume
- **Traffic analysis** — website traffic estimation, history trends, popular pages
- **Response caching** — cached results reduce repeated scraping
- **Automated CAPTCHA solving** — handles Ahrefs bot detection via CapSolver

The appeal is obvious: Ahrefs data without an Ahrefs subscription. The server scrapes Ahrefs directly and solves CAPTCHAs automatically. At 225 stars (up from 165 in March), it's popular — but be aware this scrapes a commercial service without authorization, which creates legal and reliability risks. Data could break at any time if Ahrefs changes their anti-bot measures. Requires Python 3.10+ and a CapSolver API key.

### Semrush Official MCP Server — NEW

**Semrush launched an official hosted MCP server** — the fourth major SEO platform to go official after Ahrefs, DataForSEO, and SE Ranking. Hosted at `mcp.semrush.com/v1/mcp` with OAuth authentication:

- **No local setup required** — authenticate with your Semrush account via browser
- **Standard and Trends APIs** — keyword data, backlinks, domain analytics, traffic analytics
- **Multi-platform support** — works with ChatGPT, Claude, Cursor, VS Code, Claude Code
- **Team access** — one setup gives every team member the same live data source
- **Automated workflows** — connect to AI agents that scan keyword and backlink data daily, flag ranking drops and high-impact opportunities

Requires an API subscription — either Standard (via SEO Business plan) or Trends (Basic or Premium). This is a significant milestone: Semrush joining Ahrefs, DataForSEO, and SE Ranking means **all four major Western SEO platforms now have official MCP servers**.

### mrkooblu/semrush-mcp — Community Semrush Integration

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [semrush-mcp](https://github.com/mrkooblu/semrush-mcp) | 25 | TypeScript | — | 18 |

**Comprehensive Semrush data through 18 specialized tools:**

- **Domain analytics** — overview, organic keywords, paid keywords, competitor analysis
- **Keyword analytics** — overview data and related keyword discovery
- **Backlink analysis** — backlink data and referring domains
- **Traffic analytics** — traffic summary and source analysis (requires .Trends subscription)
- **Rate limiting and caching** — handles API throttling automatically

The community alternative to the official server. The 18-tool design separates each API endpoint into its own tool. Handles authentication, rate limiting, and caching. May still be preferred by users who want local execution or need customization. Requires a Semrush API key.

### Skobyn/dataforseo-mcp-server — Community DataForSEO Server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [dataforseo-mcp-server](https://github.com/Skobyn/dataforseo-mcp-server) | 47 | TypeScript | — | Hundreds |

**Alternative DataForSEO integration using stdio transport:**

- **Full DataForSEO API coverage** — exposes the same breadth as the official server
- **Stdio transport** — standard input/output communication (vs. HTTP)
- **Comprehensive tool set** — hundreds of tools across all DataForSEO API categories

This community server provides an alternative to the official DataForSEO server, using stdio transport which may integrate more simply with some MCP clients. Same DataForSEO credentials required.

---

## Keyword Research

### hithereiamaliff/mcp-keywords-everywhere — Keywords Everywhere API

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [mcp-keywords-everywhere](https://github.com/hithereiamaliff/mcp-keywords-everywhere) | — | TypeScript | MIT | Multiple |

**Keyword research via the Keywords Everywhere API:**

- **Keyword data** — search volume, CPC, and competition metrics
- **Related keywords** — "People Also Search For" suggestions
- **Domain analysis** — what keywords a domain or URL ranks for
- **Traffic metrics** — traffic estimates and costs for domains and URLs
- **Backlink analysis** — backlink data for domains and pages
- **Multi-country support** — analyze keywords across different countries and currencies
- **Credit management** — check Keywords Everywhere credit balance

Uses Streamable HTTP transport (the recommended MCP transport for production). Keywords Everywhere is a lighter-weight keyword tool than Ahrefs or Semrush — less data depth but significantly cheaper. Not an official Keywords Everywhere server. MIT licensed.

### SEO-Review-Tools/SEO-API-MCP — SEO Review Tools API

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [SEO-API-MCP](https://github.com/SEO-Review-Tools/SEO-API-MCP) | — | Node.js | — | Multiple |

**SEO Review Tools data for keyword insights and backlinks:**

- **Keyword insights** — real-time keyword data and suggestions
- **Backlink data** — link analysis for any domain
- **Traffic estimates** — estimated traffic volumes

Integrates with the SEO Review Tools API, which provides a mix of free and premium SEO data. Good for users who already use SEO Review Tools and want to bring that data into AI workflows. Requires Node.js v18+ and an SEO Review Tools API key.

---

## PageSpeed & Technical SEO

### ruslanlap/pagespeed-insights-mcp — Google PageSpeed Analysis

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [pagespeed-insights-mcp](https://github.com/ruslanlap/pagespeed-insights-mcp) | 33 | TypeScript | — | Multiple |

**Google PageSpeed Insights performance analysis through Claude:**

- **Performance scores** — Lighthouse performance, accessibility, best practices, and SEO scores
- **Core Web Vitals** — LCP, INP, CLS metrics
- **Optimization suggestions** — specific recommendations for improving page speed
- **Mobile and desktop** — separate analysis for both form factors

The most popular PageSpeed MCP server. Connects directly to Google's PageSpeed Insights API, giving you the same data as the web tool but queryable through natural language. Useful for bulk-checking pages during site audits. Also available as an npm package.

### adamsilverstein/lighthouse-mcp-server — Lighthouse Reports

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [lighthouse-mcp-server](https://github.com/adamsilverstein/lighthouse-mcp-server) | — | — | — | Multiple |

**Full Lighthouse reports via PageSpeed Insights API:**

- **Lighthouse audit categories** — performance, accessibility, best practices, SEO, PWA
- **Detailed recommendations** — specific audit results with fix suggestions

An alternative to ruslanlap's server focused specifically on full Lighthouse report output. Newer and less adopted but provides the complete Lighthouse audit experience.

---

## Content Optimization — NEW

### Frase MCP Server

**The first content optimization MCP server** — and arguably the most ambitious SEO MCP launch of 2026. Frase for AI Agents connects the full Frase content platform to any MCP-compatible client:

- **Six-stage pipeline** — research, write, optimize, audit, monitor, and fix — all triggerable via natural language
- **Dual SEO+GEO scoring** — real-time scores for both Google optimization and AI citation readiness side by side. This is the clearest differentiator: as AI search grows, optimizing for both traditional and AI search becomes essential
- **End-to-end automation** — a single prompt can research a keyword, write an article, score and optimize it, publish to CMS, monitor performance, and auto-fix when rankings drop
- **Multi-platform** — works with Claude Desktop, Cursor, Windsurf, Lovable, Replit
- **MCP included from $39/mo** — significantly cheaper than Ahrefs or Semrush MCP access, which require enterprise plans

Frase fills the content optimization gap that was the most glaring absence in March. Unlike other SEO MCPs that only read data, Frase creates content, optimizes it, and tracks results — shifting from consumption to production.

## Moz — NEW (Gap Filled)

### metehan777/moz-mcp — Moz SEO Tools

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [moz-mcp](https://github.com/metehan777/moz-mcp) | 11 | TypeScript | — | 13+ |

**The first Moz MCP server** — filling one of the most-requested gaps from March:

- **Domain Authority / Page Authority** — Moz's signature authority metrics
- **Global top domains and pages** — rank analysis across the web
- **Keyword search intent** — understand what users mean when they search
- **Keyword suggestions** — discover keyword opportunities
- **Keyword difficulty and opportunity** — assess competition and potential
- **Keyword priority** — combined scoring for strategic prioritization
- **Link analysis** — explore backlink profiles using Moz's link index

Not official (community-built by the same developer behind the alternative Semrush server), but covers the key Moz API v3 endpoints. Composio also offers a Moz integration through its tool router, providing dynamic loading alongside other SEO tools through a single MCP endpoint. Requires Moz API credentials.

## Technical SEO Crawling — NEW (Gap Filled)

### bzsasson/screaming-frog-mcp ��� Screaming Frog SEO Spider

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [screaming-frog-mcp](https://github.com/bzsasson/screaming-frog-mcp) | 20 | Python | — | 8 |

**The first Screaming Frog MCP server** — giving AI assistants access to the most popular technical SEO crawler:

- **crawl_site** — initiate headless crawls via CLI
- **list_crawls** — browse saved crawl databases
- **export_crawl** — export crawl data for analysis
- **read_crawl_data** — read and filter crawl results (e.g., "show pages with missing meta descriptions", "find 404 pages")
- **crawl_status** — check progress of running crawls
- **storage_summary** — manage crawl database storage
- **sf_check** — verify Screaming Frog installation
- **delete_crawl** — clean up old crawl data

Requires Screaming Frog SEO Spider installed locally with a valid license. Important constraint: the Screaming Frog GUI locks the crawl database, so the MCP server cannot access data while the GUI is running. The recommended workflow is to crawl in the GUI (where you have full control over JS rendering, crawl scope, custom extraction), then close the GUI and use the MCP to analyze results. A second implementation by acamolese also exists, built on the screamingfrog Python library. Published on PyPI as `screaming-frog-mcp`.

## Google Trends — NEW (Gap Filled)

Multiple Google Trends MCP servers appeared since March, filling another key gap:

| Server | Key Feature |
|--------|-------------|
| [jmanek/google-news-trends-mcp](https://github.com/jmanek/google-news-trends-mcp) | Google News RSS + Google Trends combined — news search, trending topics, optional summarization |
| [andrewlwn77/google-trends-mcp](https://github.com/andrewlwn77/google-trends-mcp) | Keyword comparison, trending searches, related queries, regional interest |
| [cryptoken/GoogleTrendsMCP](https://github.com/cryptoken/GoogleTrendsMCP) | Real-time market intelligence with trend prediction |
| [Apify Google Trends Scraper](https://apify.com/apify/google-trends-scraper/api/mcp) | MCP-enabled scraper for Google Trends data |

Google also published a [BigQuery + Google Trends codelab](https://codelabs.developers.google.com/next26/adk-mcp-tools) at Cloud Next '26, showing how to build a Trends analyst agent using the BigQuery MCP server to query the public Google Trends dataset. The jmanek implementation stands out for combining News and Trends in one server — useful for correlating trending topics with news coverage.

## Local SEO — NEW (Gap Narrowing)

### Google Business Profile MCP

Google Business Profile MCP servers have appeared, partially filling the local SEO gap:

- **Zapier Google Business Profile MCP** — automation-focused, real-time action automation and task management
- **n8n Google Business Profile MCP template** — all 9 GBP operations exposed as MCP tools, zero-config

While not yet as mature as the GSC or keyword research categories, the appearance of GBP MCP tools signals that local SEO is joining the MCP ecosystem. In 2026, Google Business Profiles drive more calls, directions, and first impressions than websites for many local businesses — AI agent access to this data is increasingly important.

---

## What's Missing

Several major gaps from March 2026 have been filled. Here's what remains:

- **Bing Webmaster Tools** — Microsoft's search console is still completely absent
- **Schema / structured data** — no MCP server validates or generates schema markup
- **Clearscope / SurferSEO** — while Frase fills the content optimization gap, these specific platforms have no MCP presence
- **Rank tracking dashboards** — no AccuRanker, SERPstat, or dedicated rank monitoring (beyond SE Ranking)
- **Link building** — no outreach tools, broken link finders, or prospecting servers
- **Log file analysis** — no server-side log analysis for crawl behavior
- **Google Analytics** — while GA servers exist separately and mcp-gsc's hosted version adds GA4, no SEO-focused GA integration exists

**Gaps filled since March 2026:**
- ~~No Moz ecosystem~~ → metehan777/moz-mcp provides 13+ tools covering DA, keyword research, link analysis
- ~~No Screaming Frog~~ → bzsasson/screaming-frog-mcp provides 8 tools for crawl analysis
- ~~No Google Trends~~ → 4+ implementations including combined News+Trends servers
- ~~No content optimization~~ → Frase launched full pipeline MCP with dual SEO+GEO scoring
- ~~No local SEO tools~~ → Google Business Profile MCP appeared (still early)
- ~~No official Semrush~~ → Semrush launched hosted MCP at mcp.semrush.com with OAuth

---

## Bottom Line

The SEO MCP server category is now **the strongest commercial category in the entire MCP ecosystem**. Every major Western SEO platform — Ahrefs, Semrush, DataForSEO, SE Ranking — has an official MCP server. No other domain-specific category can claim this level of enterprise adoption.

Google Search Console integration is exceptional — mcp-gsc surged to 700+ stars with uvx zero-install setup and a hosted version, making it accessible to non-technical SEOs for the first time. The GSC ecosystem alone grew from ~6 to 20+ implementations.

The all-in-one platforms each have different strengths: SE Ranking for ambition (160+ tools, AI Search visibility, Claude Skills), DataForSEO for breadth (hundreds of tools across SERP, keyword, on-page, and labs APIs), Semrush for the new hosted OAuth experience, and Ahrefs for frictionless remote access. The free Ahrefs scrapers remain popular (cnych up to 225 stars) but carry legal risk.

The biggest story since March is the **gap closure wave**: Moz (13+ tools), Screaming Frog (8 tools), Google Trends (4+ servers), content optimization (Frase's full pipeline MCP), local SEO (Google Business Profile), and the Semrush official launch collectively addressed six of the ten gaps identified in March. Frase's dual SEO+GEO scoring is particularly forward-looking — it's the first MCP tool designed for both traditional and AI search optimization.

SE Ranking's AI Search share of voice feature deserves special mention — tracking brand visibility across ChatGPT, Gemini, Perplexity, and AI Overviews is a genuinely novel capability that reflects how SEO is evolving beyond Google-only optimization.

**Rating: 4.5/5** *(was 4/5)* — Upgraded based on: Semrush going official (all four major platforms now have MCP), mcp-gsc surging to 700+ stars with hosted version, SE Ranking expanding to 160+ tools with AI Search visibility, Frase launching content optimization MCP, and six major gaps filling simultaneously (Moz, Screaming Frog, Google Trends, content optimization, local SEO, Semrush official). Remaining deductions for missing Bing Webmaster Tools, schema validation, Clearscope/SurferSEO specifically, and link building tools. But the trajectory is unmistakable — SEO was an early MCP adopter and is now the most commercially complete category.

*This review was refreshed on 2026-05-02 using Claude Opus 4.6 (Anthropic). Previous version: 2026-03-17.*
