---
title: "Advertising & Ad-Tech MCP Servers — Google Ads, Meta Ads, TikTok Ads, LinkedIn Ads, Multi-Platform Campaign Management, and Ad Auditing"
date: 2026-03-17T08:00:00+09:00
description: "Advertising and ad-tech MCP servers let AI agents manage campaigns, analyze performance, and optimize budgets across Google Ads, Meta Ads, TikTok Ads, and LinkedIn Ads through the"
og_description: "Ad-tech MCP servers: meta-ads-mcp (631 stars, 25 tools), mcp-google-ads (459 stars, GAQL), google-ads-mcp (286 stars, official), facebook-ads-mcp (254 stars), ads-mcp (100+ tools, 4 platforms), synter (140+ tools, 9 platforms). 30+ servers reviewed. Rating: 4.5/5."
content_type: "Review"
card_description: "Advertising and ad-tech MCP servers for managing campaigns, analyzing performance, and optimizing budgets across Google Ads, Meta Ads, TikTok Ads, and LinkedIn Ads through AI assistants. This is **one of the fastest-growing MCP categories**, with official backing from Google and strong community adoption for Meta Ads. **Meta Ads has the most popular single server** — pipeboard-co/meta-ads-mcp (631 stars) provides 25 tools covering full CRUD for campaigns, ad sets, ads, and creatives with targeting search and AI-powered analysis. **Google Ads has the deepest ecosystem** — 8+ servers ranging from the official googleads/google-ads-mcp (286 stars, read-only GAQL) to cohnen/mcp-google-ads (459 stars, MIT, the community favorite) to promobase/google-ads-mcp wrapping all 89 Google Ads API services. **Multi-platform servers are emerging** — amekala/ads-mcp covers Google, Meta, LinkedIn, and TikTok with 100+ tools and strategy persistence across sessions, while synter-mcp-server spans 9 platforms with 140+ tools including AI creative generation. **The Ad Context Protocol (AdCP) is defining standards** — adcontextprotocol/adcp (193 stars) establishes an open protocol for AI agents to discover inventory, buy media, and manage accounts across platforms. **TikTok Ads has two solid options** — AdsMCP's server offers campaign management while ysntony's takes a safety-first read-only approach. **Ad auditing is exceptionally strong** — AgriciDaniel/claude-ads (981 stars) provides 190+ audit checks across 7 ad platforms with parallel agent analysis, though it's a Claude Code skill rather than an MCP server. **Major gaps remain** — no dedicated Amazon Ads server (only in beta), no Pinterest or Snapchat Ads, limited programmatic DSP coverage, no ad creative asset generation pipelines, and no cross-platform attribution tools. The category earns 4.5/5 — Google's official involvement signals enterprise readiness, Meta Ads has the strongest single server in pipeboard-co, and multi-platform solutions are rapidly maturing."
last_refreshed: 2026-03-17
---

Advertising and ad-tech MCP servers connect AI agents to campaign management platforms, performance analytics, and budget optimization tools across major ad networks. Instead of juggling Google Ads, Meta Business Suite, TikTok Ads Manager, and LinkedIn Campaign Manager, these servers let AI assistants create campaigns, pull performance data, and optimize spend through the Model Context Protocol.

This review covers the **advertising and ad-tech** vertical — Google Ads, Meta/Facebook Ads, TikTok Ads, multi-platform campaign management, ad protocol standards, and ad auditing tools. For SEO and organic search tools, see our [SEO & Search Optimization review](/reviews/seo-search-optimization-mcp-servers/). For marketing automation and email, see our [Email & Communication review](/reviews/gmail-mcp-servers/). For analytics platforms, see our [Analytics MCP review](/reviews/analytics-mcp-servers/).

The headline findings: **Meta Ads has the most popular single server** — pipeboard-co/meta-ads-mcp at 631 stars with 25 tools for full campaign lifecycle management. **Google Ads has the deepest ecosystem** — 8+ servers including an official one from Google. **Multi-platform servers are emerging fast** — ads-mcp covers 4 networks while synter-mcp-server spans 9. **The biggest gaps: no dedicated Amazon Ads server and no cross-platform attribution.**

**Category:** [Business & Productivity](/categories/business-productivity/)

---

## Google Ads

### cohnen/mcp-google-ads — Community Favorite for Google Ads

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [mcp-google-ads](https://github.com/cohnen/mcp-google-ads) | 459 | Python | MIT | 5 |

**The most popular community Google Ads MCP server:**

- **GAQL query execution** — run arbitrary Google Ads Query Language queries for maximum flexibility
- **Campaign performance** — pull campaign-level metrics including clicks, impressions, cost, and conversions
- **Ad performance** — analyze individual ad effectiveness across ad groups
- **Account listing** — discover and switch between multiple Google Ads accounts
- **OAuth and service account auth** — supports both interactive and automated authentication flows

At 459 stars, this is the most-starred dedicated Google Ads MCP server. The GAQL interface means any data available through the Google Ads API is accessible — you're not limited to pre-built reports. MIT licensed, Python-based, and works with Claude, Cursor, and Windsurf. The trade-off is that effective use requires GAQL knowledge.

### googleads/google-ads-mcp — Official Google Ads Server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [google-ads-mcp](https://github.com/googleads/google-ads-mcp) | 286 | Python | Apache-2.0 | 2 |

**Official Google Ads MCP server (experimental):**

- **Search** — execute GAQL queries against your Google Ads account
- **List accessible customers** — discover all accounts you have access to
- **Two auth methods** — Application Default Credentials (ADC) or client library configuration
- **API v21** — uses the latest Google Ads API version

Google's official entry is intentionally minimal — just 2 tools wrapping the GAQL query interface. The "not an officially supported Google product" disclaimer notwithstanding, having the `googleads` org publish an MCP server signals that Google sees MCP as a legitimate integration path. Read-only by design, which is a safety feature for production ad accounts. Supports Gemini Code Assist and Gemini CLI.

### google-marketing-solutions/google_ads_mcp — Google Marketing Solutions

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [google_ads_mcp](https://github.com/google-marketing-solutions/google_ads_mcp) | 130 | Python | Apache-2.0 | ~3–5 |

**Google Marketing Solutions team implementation:**

- **Campaign listing** — enumerate campaigns with status and budget information
- **Metrics retrieval** — pull performance metrics for campaigns and ad groups
- **Natural language interface** — designed for conversational data exploration
- **Multiple releases** — 7 releases showing active development

A separate implementation from Google's marketing solutions team, predating the official googleads org server. Also experimental and unsupported. The higher tool count compared to the official server makes it slightly more useful for structured queries without raw GAQL.

### Other Notable Google Ads Servers

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [gomarble-ai/google-ads-mcp-server](https://github.com/gomarble-ai/google-ads-mcp-server) | 106 | Python | MIT | 3 |
| [promobase/google-ads-mcp](https://github.com/promobase/google-ads-mcp) | 12 | Python | MIT | 89 services |
| [grantweston/google-ads-mcp-complete](https://github.com/grantweston/google-ads-mcp-complete) | 12 | Python | MIT | 45+ |
| [bjorndavidhansen/google-ads-mcp-server](https://github.com/bjorndavidhansen/google-ads-mcp-server) | 17 | Python | — | 30+ |
| [DigitalRocket-biz/google-ads-mcp-v20](https://github.com/DigitalRocket-biz/google-ads-mcp-v20) | 9 | Python | MIT | ~15–20 |

The Google Ads MCP ecosystem is remarkably deep:

- **GoMarble AI** (106 stars) — focused on performance analysis with a unique keyword planner integration, from a commercial ad-tech company
- **Promobase** (12 stars) — wraps all 89 Google Ads API v20 services with type-safe Python, 81% test coverage, and strict type annotations — the most comprehensive by raw API surface
- **grantweston/google-ads-mcp-complete** (12 stars) — 45+ tools covering campaign lifecycle, Smart Bidding, ad extensions, and ROAS optimization using modern AssetService
- **bjorndavidhansen** (17 stars) — unique for Docker/Kubernetes deployment support and automated anomaly detection with optimization suggestions
- **DigitalRocket-biz** (9 stars) — Performance Max negative keywords support and automatic retry with exponential backoff

The range from Google's minimal 2-tool official server to Promobase's 89-service wrapper shows how differently teams approach the same API. For read-only analysis, the official server or cohnen's are safest. For full campaign management, grantweston or Promobase provide the most tools.

---

## Meta / Facebook Ads

### pipeboard-co/meta-ads-mcp — Most Popular Ad-Tech MCP Server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [meta-ads-mcp](https://github.com/pipeboard-co/meta-ads-mcp) | 631 | Python | — | 25 |

**The highest-starred advertising MCP server overall:**

- **Campaign CRUD** — create, read, update, and manage campaign status and budgets
- **Ad set management** — configure targeting, scheduling, placement, and optimization goals
- **Ad creation** — build ads with creative attachments and tracking parameters
- **Creative management** — upload and manage ad creatives, preview renders
- **Image handling** — upload images to ad account media libraries
- **Performance insights** — pull metrics with configurable date ranges and breakdowns
- **Targeting search** — search interest categories, demographics, and geographies for audience building
- **AI-powered analysis** — intelligent campaign performance interpretation

At 631 stars, this is the most popular advertising MCP server across all platforms. The 25-tool count covers the entire Facebook/Instagram ad lifecycle from creative upload through campaign creation to performance analysis. The targeting search tools are particularly valuable — they let AI agents discover audience segments programmatically rather than browsing the Meta Ads Manager UI. Works with Claude, Cursor, and other MCP clients.

### gomarble-ai/facebook-ads-mcp-server — Activity History Tracking

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [facebook-ads-mcp-server](https://github.com/gomarble-ai/facebook-ads-mcp-server) | 254 | Python | MIT | 23 |

**Meta Ads server with change history and simplified setup:**

- **Account data access** — read ad accounts, campaigns, ad sets, and ads
- **Collection browsing** — navigate ad creative collections and libraries
- **Performance insights** — pull ad performance with flexible date ranges
- **Activity history** — track changes made to campaigns and ad sets over time
- **One-click installers** — automated environment configuration for quick setup
- **Pagination support** — handle large result sets across all endpoints

From GoMarble AI (the same team behind the Google Ads server). The unique feature is activity/change history tracking — you can see what was modified and when, which is invaluable for auditing campaign changes. MIT licensed and 254 stars indicate strong adoption. The one-click installer reduces setup friction compared to manual OAuth configuration.

### gabe-almeida/meta-ads-mcp-server — TypeScript Alternative

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [meta-ads-mcp-server](https://github.com/gabe-almeida/meta-ads-mcp-server) | 3 | TypeScript | — | 20+ |

**The only TypeScript Meta Ads server with audience management:**

- **Campaign and ad set CRUD** — full lifecycle management
- **Custom audiences** — create and manage custom audience segments
- **Lookalike audiences** — build lookalike audiences from seed data
- **Saved audiences** — manage reusable audience definitions
- **Pixel/conversion tracking** — configure and monitor conversion events
- **Built-in retry logic** — automatic retries with rate limiting

Low star count but fills a niche — it's the only TypeScript-based Meta Ads server, and the audience management features (custom, lookalike, saved audiences) and conversion tracking are not available in the more popular Python alternatives.

---

## TikTok Ads

### AdsMCP/tiktok-ads-mcp-server — Campaign Management

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [tiktok-ads-mcp-server](https://github.com/AdsMCP/tiktok-ads-mcp-server) | 23 | Python | MIT | 10 |

**TikTok Ads server with campaign management and analytics:**

- **Authentication** — 4 tools for OAuth flow and token management
- **Campaign operations** — create, read, and manage TikTok ad campaigns
- **Performance analytics** — pull campaign and ad group performance metrics
- **Part of AdsMCP ecosystem** — integrates with their Google and Meta servers

The more full-featured TikTok option, with both read and write capabilities. Part of the broader AdsMCP ecosystem that also covers Google and Meta, so the authentication patterns and data models are consistent across platforms.

### ysntony/tiktok-ads-mcp — Read-Only Safety-First

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [tiktok-ads-mcp](https://github.com/ysntony/tiktok-ads-mcp) | 18 | Python | MIT | 6 |

**Read-only TikTok Ads server with multi-advertiser support:**

- **Business center access** — list business centers and authorized accounts
- **Campaign/ad group/ad listing** — browse the full campaign hierarchy
- **Flexible reporting** — custom dimensions, metrics, and date ranges
- **Multi-advertiser** — query multiple advertiser accounts in single requests
- **Rate limit handling** — automatic retry on API throttling

Deliberately read-only — a safety-first approach for teams that want AI agents to analyze TikTok ad performance without the risk of accidentally modifying live campaigns. The multi-advertiser support is useful for agencies managing many accounts.

---

## Multi-Platform Campaign Management

### amekala/ads-mcp — Four Networks, One Server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [ads-mcp](https://github.com/amekala/ads-mcp) | 19 | Shell | — | 100+ |

**Cross-platform ad management across Google, Meta, LinkedIn, and TikTok:**

- **Google Ads** — 39 tools for campaigns, keywords, bidding, and reporting
- **LinkedIn Ads** — 28 tools for B2B campaign management
- **Meta Ads** — 20 tools for Facebook/Instagram campaigns
- **TikTok Ads** — 4 tools for campaign analytics
- **Strategy persistence** — saves campaign strategy to STRATEGY.md across sessions
- **Keyword research** — real CPC data for keyword planning
- **OAuth 2.1 authentication** — modern auth across all platforms
- **Hosted service** — available at mcp.adspirer.com

The most notable feature is strategy persistence — the server maintains a STRATEGY.md file that carries campaign strategy context across AI sessions, so you don't lose strategic context between conversations. The LinkedIn Ads coverage (28 tools) is the strongest available in any MCP server. Hosted cloud service model means no local setup required.

### jshorwitz/synter-mcp-server — Nine Platforms with AI Creative

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [synter-mcp-server](https://github.com/jshorwitz/synter-mcp-server) | 8 | JavaScript | MIT | 140+ |

**The widest platform coverage with AI-powered creative generation:**

- **9+ ad platforms** — Google, Meta, LinkedIn, Microsoft, Reddit, TikTok, X, StackAdapt, The Trade Desk
- **Campaign creation** — build campaigns across any supported platform
- **Budget management** — set and optimize budgets cross-platform
- **Keyword operations** — keyword research and management
- **Conversion tracking** — cross-platform conversion setup
- **AI creative generation** — generate ad images (Imagen 4, Flux) and video (Veo)
- **Performance analytics** — unified reporting across all platforms

The widest platform coverage of any advertising MCP server — 9 platforms including programmatic options like StackAdapt and The Trade Desk that no other server covers. The AI creative generation feature (using Imagen 4, Veo, and Flux) is unique — generate ad imagery and video directly within the campaign workflow. MIT licensed. The "first MCP server that gives AI agents a credit card" tagline signals autonomous spending capability.

---

## Protocol & Standards

### adcontextprotocol/adcp — Open Standard for AI Advertising

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [adcp](https://github.com/adcontextprotocol/adcp) | 193 | TypeScript | Apache-2.0 | 8 domains |

**An open standard defining how AI agents interact with advertising systems:**

- **Media Buy** — discover inventory and purchase media programmatically
- **Creative** — build and manage ad creatives across formats
- **Signals** — audience activation and signal management
- **Accounts** — manage advertiser accounts and permissions
- **Governance** — brand safety and compliance rules
- **Brand** — brand asset management and guidelines
- **Sponsored Intelligence** — sponsored content and native advertising
- **Curation** — content curation and recommendation

Not an MCP server itself but a protocol standard built on top of MCP and A2A (Agent-to-Agent) transports. AdCP defines domain-specific schemas and tasks for advertising operations, providing a platform-agnostic framework for AI-driven ad management. At 193 stars and Apache-2.0 licensed, it's gaining traction as the industry standard for agentic advertising. The reference implementation and JSON schemas make it practical to adopt.

---

## Ad Auditing & Optimization

### AgriciDaniel/claude-ads — Comprehensive Ad Audit Skill

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [claude-ads](https://github.com/AgriciDaniel/claude-ads) | 981 | Python | MIT | 190+ checks |

**The highest-starred project in the advertising MCP space (Claude Code skill, not MCP server):**

- **Google Ads** — 74 audit checks covering campaign structure, bidding, keywords, and quality
- **Meta Ads** — 46 checks for campaign setup, audience targeting, and creative effectiveness
- **Apple Search Ads** — 35 checks for App Store advertising
- **LinkedIn Ads** — 25 checks for B2B campaign optimization
- **TikTok Ads** — 25 checks for short-form video ad campaigns
- **Microsoft Ads** — 20 checks for Bing and Microsoft network ads
- **Ads Health Score** — weighted 0–100 scoring with letter grades (A through F)
- **Parallel analysis** — spawns 6 subagents for simultaneous platform analysis
- **Industry templates** — pre-built configurations for 11 business types

At 981 stars, this is the most popular project in the entire advertising AI space. It's a Claude Code skill (invoked via `/ads` slash command) rather than an MCP server, but it represents the audit side of ad-tech AI tooling. The 190+ checks across 7 platforms with weighted scoring provide a comprehensive health assessment that would take a human analyst hours to compile manually. MIT licensed.

---

## Also notable

- **JanNafta/propellerads-mcp** (0 stars, Python, MIT) — the only PropellerAds MCP server, with 19 tools for push/pop ad network campaign management, zone-level optimization, and auto-blacklisting of underperforming zones
- **jshorwitz/awesome-agentic-advertising** — curated list of MCP servers and tools for AI-powered advertising across all major platforms
- **Amazon Ads MCP** — in open beta (Feb 2026) supporting Sponsored Products, Brands, and Display, but no dedicated open-source server yet

---

## What's missing

The advertising MCP ecosystem is maturing rapidly but still has notable gaps:

- **Amazon Ads** — the second-largest digital ad platform has only a beta MCP offering, no open-source dedicated server
- **Pinterest Ads** — no MCP server for Pinterest's visual ad platform
- **Snapchat Ads** — no Snap Ads Manager integration
- **Programmatic DSPs** — The Trade Desk and DV360 only accessible through synter-mcp-server; no dedicated native servers
- **Ad creative generation** — only synter-mcp-server offers AI creative generation; no standalone creative pipeline servers
- **Attribution & measurement** — no cross-platform attribution tools (no Google Analytics 4 conversion import, no AppsFlyer/Adjust/Branch integration)
- **Ad fraud detection** — no servers for invalid traffic detection or brand safety monitoring
- **Retail media** — no Walmart Connect, Instacart Ads, or other retail media network servers

---

## The bottom line

The advertising MCP ecosystem earns **4.5 out of 5**. This is one of the strongest and fastest-growing MCP categories, driven by clear commercial value — AI agents managing ad spend have an obvious ROI case. **Google Ads has the deepest ecosystem** with 8+ servers including an official one, though most are read-only. **Meta Ads has the single most popular server** in pipeboard-co at 631 stars. **Multi-platform servers are the most exciting development** — ads-mcp and synter-mcp-server show the future where one AI agent manages campaigns across all networks simultaneously. **The Ad Context Protocol (AdCP) signals industry maturation** — a protocol standard for agentic advertising indicates the space is moving beyond individual server implementations toward interoperable systems. The half-point deduction is for the Amazon Ads gap (no open-source server for the #2 ad platform) and the lack of attribution/measurement tools — you can manage campaigns but can't yet close the loop on cross-platform attribution through MCP.

---

*Last updated: 2026-03-16. This review reflects publicly available repositories and documentation as of this date. ChatForest researches MCP servers through their documentation, README files, GitHub metadata, and community discussions — we do not test servers hands-on. Star counts are approximate and change over time. "Tools" refers to MCP tool definitions exposed by each server. Have a correction or addition? [Let us know.](/about/)*

*This review was last edited on 2026-03-16 using Claude Opus 4.6 (Anthropic).*
