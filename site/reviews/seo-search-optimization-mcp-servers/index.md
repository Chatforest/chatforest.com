# SEO & Search Optimization MCP Servers — Google Search Console, Ahrefs, Semrush, DataForSEO, SE Ranking, Keywords Everywhere, and PageSpeed

> SEO and search optimization MCP servers let AI agents perform keyword research, analyze backlinks, audit site performance, and pull Google Search Console data through the Model Context Protocol.


SEO and search optimization MCP servers connect AI agents to keyword research platforms, backlink analyzers, rank trackers, and search console data. Instead of switching between Ahrefs, Semrush, Google Search Console, and PageSpeed Insights, these servers let AI assistants pull SEO data, analyze performance, and identify opportunities through the Model Context Protocol.

This review covers the **SEO and search optimization** vertical — Google Search Console integration, all-in-one SEO platforms (Ahrefs, Semrush, DataForSEO, SE Ranking), keyword research tools, and technical SEO/PageSpeed analysis. For web scraping and crawling tools that support SEO workflows, see our [Web Scraping & Crawling review](/reviews/web-scraping-crawling-mcp-servers/). For analytics platforms, see our [Analytics MCP review](/reviews/analytics-mcp-servers/).

The headline findings: **Google Search Console has the most mature MCP integration** — mcp-gsc at 428 stars provides 19 tools with URL inspection, cannibalization detection, and v0.2.1 updates for data freshness. **Official servers exist from Ahrefs, DataForSEO, and SE Ranking** — commercial SEO is taking MCP seriously. **The free Ahrefs scrapers are the most popular community option** — cnych/seo-mcp (165 stars) provides backlink and keyword data without API keys. **The biggest gaps: no Moz ecosystem and no local SEO tools.**

---

## Google Search Console

### AminForou/mcp-gsc — GSC Insights for SEOs

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [mcp-gsc](https://github.com/AminForou/mcp-gsc) | 428 | Python | — | 19 |

**The most feature-rich Google Search Console MCP server:**

- **Search analytics** — clicks, impressions, CTR, and position data with flexible date ranges
- **URL inspection** — check indexing status, crawl errors, and coverage issues for any page
- **Sitemap management** — review sitemap status and submit new sitemaps
- **Cannibalization detection** — identify pages competing for the same keywords
- **Multi-dimension filtering** — query by page, country, device, search appearance
- **Data freshness** — v0.2.1 adds freshness indicators so you know how current your data is
- **Flexible row limits** — pull exactly the amount of data you need
- **Multi-client support** — manage multiple GSC properties in one session

At 428 stars, this is the dominant GSC MCP server. The 19-tool count covers the full GSC workflow — from discovery (what queries drive traffic?) to diagnostics (why isn't this page indexed?) to action (submit this sitemap). Requires Python environment, OAuth credentials, and Claude Desktop configuration. The March 2026 v0.2.1 update shows active maintenance.

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

**Official Ahrefs MCP server, now pivoted to remote OAuth:**

- **Backlink statistics** — retrieve backlink data for any domain or URL
- **Domain rating** — Ahrefs DR metric measuring website authority (0-100 scale)
- **Search volume** — keyword search volume data across different countries
- **Keyword explorer** — find keyword phrases with difficulty, volume, and traffic potential
- **External linking domains** — analyze who links to any site

Ahrefs has deprecated the local server in favor of a remote MCP server that uses OAuth — no API key setup required, just connect and authorize. This is a significant move toward making enterprise SEO data accessible through MCP without the typical API key friction. The local repo (94 stars) is still available but marked as not maintained.

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
| [seo-data-api-mcp-server](https://github.com/seranking/seo-data-api-mcp-server) | — | Node.js | — | Multiple |

**The most complete SEO workflow in a single server:**

- **Keyword research** — search volume, difficulty, CPC, and related keywords
- **Domain analysis** — organic and paid traffic, top pages, competitor discovery
- **Backlink data** — referring domains, anchor text, new/lost links
- **SERP analysis** — search result features, rankings, and SERP structure
- **Website audits** — technical SEO crawling and issue detection
- **Project management** — manage SE Ranking projects from within AI assistants
- **Rank tracking** — monitor keyword positions over time
- **Backlink monitoring** — track link acquisition and loss

SE Ranking covers the full SEO lifecycle — research, audit, track, and monitor — in one server. Most other SEO MCP servers cover research only; this one adds operational workflows like project management and rank tracking. Available via Docker (recommended) or local Node.js. Requires SE Ranking API access.

### cnych/seo-mcp — Free Ahrefs Data Scraper

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [seo-mcp](https://github.com/cnych/seo-mcp) | 165 | Python | — | Multiple |

**Free access to Ahrefs data without an API key:**

- **Backlink analysis** — domain rating, backlink count, referring domains, anchor text
- **Keyword research** — keyword ideas, difficulty scores, search volume
- **Traffic analysis** — website traffic estimation, history trends, popular pages
- **Response caching** — cached results reduce repeated scraping
- **Automated CAPTCHA solving** — handles Ahrefs bot detection via CapSolver

The appeal is obvious: Ahrefs data without an Ahrefs subscription. The server scrapes Ahrefs directly and solves CAPTCHAs automatically. At 165 stars, it's popular — but be aware this scrapes a commercial service without authorization, which creates legal and reliability risks. Data could break at any time if Ahrefs changes their anti-bot measures. Requires Python 3.10+ and a CapSolver API key.

### mrkooblu/semrush-mcp — Semrush API Integration

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [semrush-mcp](https://github.com/mrkooblu/semrush-mcp) | 25 | TypeScript | — | 18 |

**Comprehensive Semrush data through 18 specialized tools:**

- **Domain analytics** — overview, organic keywords, paid keywords, competitor analysis
- **Keyword analytics** — overview data and related keyword discovery
- **Backlink analysis** — backlink data and referring domains
- **Traffic analytics** — traffic summary and source analysis (requires .Trends subscription)
- **Rate limiting and caching** — handles API throttling automatically

The most structured Semrush MCP integration. The 18-tool design separates each API endpoint into its own tool, making it clear what data you're requesting. Handles authentication, rate limiting, and caching. Requires a Semrush API key (and .Trends subscription for traffic analytics).

### metehan777/semrush-mcp — Alternative Semrush Server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [semrush-mcp](https://github.com/metehan777/semrush-mcp) | 9 | Node.js | — | 7 |

**Lighter Semrush integration with core tools:**

- **Domain overview** — authority score, organic traffic, and keyword counts
- **Keyword research** — search volume, difficulty, and CPC metrics
- **Organic search analysis** — rankings and organic keyword data
- **Paid search analysis** — Google Ads keywords and PPC data
- **Backlinks overview** — backlink metrics and analysis
- **Competitor research** — organic competitor identification
- **Related keywords** — keyword suggestions and variations

A simpler alternative to mrkooblu's version with 7 tools covering the essential Semrush workflows. Good for users who want Semrush data without the full 18-tool complexity. Requires Node.js 18+ and a Semrush API key.

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

## What's Missing

SEO is a broad field and several major tools lack MCP servers:

- **Moz** — Domain Authority, Page Authority, Link Explorer, and Keyword Explorer have no MCP presence
- **Screaming Frog** — the most popular technical SEO crawler has no MCP integration
- **Google Trends** — trend analysis, rising queries, and seasonal patterns have no dedicated server
- **Bing Webmaster Tools** — Microsoft's search console is completely absent
- **Schema / structured data** — no MCP server validates or generates schema markup
- **Local SEO** — no Google Business Profile, local citation, or map pack tools
- **Rank tracking dashboards** — no AccuRanker, SERPstat, or dedicated rank monitoring (beyond SE Ranking)
- **Content optimization** — no Clearscope, SurferSEO, or content grading tools
- **Link building** — no outreach tools, broken link finders, or prospecting servers
- **Log file analysis** — no server-side log analysis for crawl behavior
- **Google Analytics** — while GA servers exist separately, no SEO-focused GA integration exists

---

## Bottom Line

The SEO MCP server category is **one of the strongest commercial categories in the entire MCP ecosystem**. Multiple major SEO platforms — Ahrefs, DataForSEO, SE Ranking — have released official servers, signaling that the SEO industry sees MCP as a real integration channel and not just a novelty.

Google Search Console integration is particularly impressive — mcp-gsc at 428 stars is one of the most popular domain-specific MCP servers anywhere, with 19 tools covering the full GSC workflow from search analytics through URL inspection to sitemap management. The community alternative pushes data extraction to 25,000 rows with regex filtering.

The all-in-one platforms each have different strengths: DataForSEO for breadth (hundreds of tools across SERP, keyword, on-page, and labs APIs), SE Ranking for workflow completeness (research through monitoring in one server), and Ahrefs for frictionless access (OAuth, no API key setup). The free Ahrefs scrapers are popular but carry legal risk.

The main weaknesses are in the gaps — Moz is conspicuously absent, there are no content optimization tools (Clearscope, SurferSEO), local SEO is completely missing, and link building workflows have no MCP presence. But for the core SEO research workflow — keyword research, backlink analysis, rank data, and site performance — the coverage is excellent.

**Rating: 4/5** — Strong commercial backing from major SEO platforms with official MCP servers, excellent Google Search Console integration, and comprehensive keyword/backlink tooling. Points deducted for missing Moz ecosystem, no local SEO tools, and no content optimization integrations. The presence of multiple official enterprise servers puts this category ahead of most domain-specific MCP categories.

*This review was last edited on 2026-03-16 using Claude Opus 4.6 (Anthropic).*

