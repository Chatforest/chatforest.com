# Advertising & Ad-Tech MCP Servers — Google Ads, Meta Ads, Amazon Ads, TikTok Ads, LinkedIn Ads, Programmatic DSPs, Multi-Platform Campaign Management, and Ad Auditing

> Advertising and ad-tech MCP servers let AI agents manage campaigns, analyze performance, and optimize budgets across Google Ads, Meta Ads, Amazon Ads, TikTok Ads, and LinkedIn Ads through the


Advertising and ad-tech MCP servers connect AI agents to campaign management platforms, performance analytics, and budget optimization tools across major ad networks. Instead of juggling Google Ads, Meta Business Suite, TikTok Ads Manager, and LinkedIn Campaign Manager, these servers let AI assistants create campaigns, pull performance data, and optimize spend through the Model Context Protocol.

This review covers the **advertising and ad-tech** vertical — Google Ads, Meta/Facebook Ads, TikTok Ads, multi-platform campaign management, ad protocol standards, and ad auditing tools. For SEO and organic search tools, see our [SEO & Search Optimization review](/reviews/seo-search-optimization-mcp-servers/). For marketing automation and email, see our [Email & Communication review](/reviews/gmail-mcp-servers/). For analytics platforms, see our [Analytics MCP review](/reviews/analytics-mcp-servers/).

The headline findings: **Meta Ads has the most popular single server** — pipeboard-co/meta-ads-mcp at 819 stars with 24 tools for full campaign lifecycle management, now available as a cloud-hosted Remote MCP service. **Google Ads has the deepest ecosystem** — 8+ servers including an official one from Google now at 404 stars. **Amazon Ads finally has open-source coverage** — MarketplaceAdPros fills the biggest gap from our previous review. **Programmatic DSPs are arriving** — StackAdapt and zMaticoo both launched official MCP servers in April 2026. **Multi-platform servers keep growing** — ads-mcp covers 4 networks while synter-mcp-server spans 9. **Ad auditing has exploded** — claude-ads tripled to 3.2k stars with 250+ checks.

**Category:** [Business & Productivity](/categories/business-productivity/)

---

## Google Ads

### cohnen/mcp-google-ads — Community Favorite for Google Ads

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [mcp-google-ads](https://github.com/cohnen/mcp-google-ads) | 568 | Python | MIT | 5 |

**The most popular community Google Ads MCP server:**

- **GAQL query execution** — run arbitrary Google Ads Query Language queries for maximum flexibility
- **Campaign performance** — pull campaign-level metrics including clicks, impressions, cost, and conversions
- **Ad performance** — analyze individual ad effectiveness across ad groups
- **Account listing** — discover and switch between multiple Google Ads accounts
- **OAuth and service account auth** — supports both interactive and automated authentication flows

At 568 stars, this is the most-starred dedicated Google Ads MCP server. The GAQL interface means any data available through the Google Ads API is accessible — you're not limited to pre-built reports. MIT licensed, Python-based, and works with Claude, Cursor, and Windsurf. The trade-off is that effective use requires GAQL knowledge.

### googleads/google-ads-mcp — Official Google Ads Server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [google-ads-mcp](https://github.com/googleads/google-ads-mcp) | 404 | Python | Apache-2.0 | 3 |

**Official Google Ads MCP server (experimental):**

- **Search** — execute GAQL queries against your Google Ads account
- **Get resource metadata** — retrieve metadata about API resource types for query building
- **List accessible customers** — discover all accounts you have access to
- **4 LLM resources** — discovery document, metrics, segments, and release notes exposed as MCP resources
- **Two auth methods** — Application Default Credentials (ADC) or client library configuration

Google's official entry has grown from 2 to 3 tools since launch, adding resource metadata introspection and 4 MCP resources that give LLMs contextual knowledge about the Google Ads API. At 404 stars (up from 286 in six weeks), adoption is accelerating. Read-only by design, which is a safety feature for production ad accounts. Supports Gemini Code Assist and Gemini CLI.

### google-marketing-solutions/google_ads_mcp — Google Marketing Solutions

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [google_ads_mcp](https://github.com/google-marketing-solutions/google_ads_mcp) | 182 | Python | Apache-2.0 | ~3–5 |

**Google Marketing Solutions team implementation:**

- **Campaign listing** — enumerate campaigns with status and budget information
- **Metrics retrieval** — pull performance metrics for campaigns and ad groups
- **Natural language interface** — designed for conversational data exploration
- **Multiple releases** — 7 releases showing active development

A separate implementation from Google's marketing solutions team, predating the official googleads org server. Now at v0.6.4 (April 2026) with 9 releases showing active development. Also experimental and unsupported. The higher tool count compared to the official server makes it slightly more useful for structured queries without raw GAQL.

### Other Notable Google Ads Servers

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [gomarble-ai/google-ads-mcp-server](https://github.com/gomarble-ai/google-ads-mcp-server) | 122 | Python | MIT | 3 |
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
| [meta-ads-mcp](https://github.com/pipeboard-co/meta-ads-mcp) | 819 | Python | BSL-1.1 | 24 |

**The highest-starred advertising MCP server overall:**

- **Campaign CRUD** — create, read, update, and manage campaign status and budgets
- **Ad set management** — configure targeting, scheduling, placement, and optimization goals
- **Ad creation** — build ads with creative attachments and tracking parameters
- **Creative management** — upload and manage ad creatives, preview renders
- **Image handling** — upload images to ad account media libraries
- **Performance insights** — pull metrics with configurable date ranges and breakdowns
- **Targeting search** — search interest categories, demographics, and geographies for audience building
- **AI-powered analysis** — intelligent campaign performance interpretation
- **Remote MCP service** — cloud-hosted option for instant setup without local installation

At 819 stars (up from 631 six weeks ago), this continues its dominance as the most popular advertising MCP server. Now available as a **Remote MCP cloud service** — the recommended approach for getting started quickly — alongside traditional local installation. Pipeboard has also launched a **CLI tool** providing access to Meta, Google, and TikTok Ads from a single binary, signaling the company's expansion beyond a single-platform MCP server. Licensed under BSL-1.1 (converts to Apache-2.0 on January 1, 2029). Works with Claude Pro/Max, Cursor, and other MCP-compatible platforms.

### gomarble-ai/facebook-ads-mcp-server — Activity History Tracking

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [facebook-ads-mcp-server](https://github.com/gomarble-ai/facebook-ads-mcp-server) | 315 | Python | MIT | 23 |

**Meta Ads server with change history and simplified setup:**

- **Account data access** — read ad accounts, campaigns, ad sets, and ads
- **Collection browsing** — navigate ad creative collections and libraries
- **Performance insights** — pull ad performance with flexible date ranges
- **Activity history** — track changes made to campaigns and ad sets over time
- **One-click installers** — automated environment configuration for quick setup
- **Pagination support** — handle large result sets across all endpoints

From GoMarble AI (the same team behind the Google Ads server). The unique feature is activity/change history tracking — you can see what was modified and when, which is invaluable for auditing campaign changes. MIT licensed and 315 stars (up from 254) indicate strong adoption. The one-click installer reduces setup friction compared to manual OAuth configuration.

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
| [ads-mcp](https://github.com/amekala/ads-mcp) | 35 | Shell | — | 100+ |

**Cross-platform ad management across Google, Meta, LinkedIn, and TikTok:**

- **Google Ads** — 39 tools for campaigns, keywords, bidding, and reporting
- **LinkedIn Ads** — 28 tools for B2B campaign management
- **Meta Ads** — 20 tools for Facebook/Instagram campaigns
- **TikTok Ads** — 4 tools for campaign analytics
- **Strategy persistence** — saves campaign strategy to STRATEGY.md across sessions
- **Keyword research** — real CPC data for keyword planning
- **OAuth 2.1 authentication** — modern auth across all platforms
- **Hosted service** — available at mcp.adspirer.com

The most notable feature is strategy persistence — the server maintains a STRATEGY.md file that carries campaign strategy context across AI sessions, so you don't lose strategic context between conversations. The LinkedIn Ads coverage (28 tools) is the strongest available in any MCP server. Now supports Gemini CLI alongside Claude, ChatGPT, Cursor, and Codex. Hosted cloud service model means no local setup required. At 35 stars (up from 19), adoption is growing steadily.

### jshorwitz/synter-mcp-server — Nine Platforms with AI Creative

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [synter-mcp-server](https://github.com/jshorwitz/synter-mcp-server) | 10 | JavaScript | MIT | 140+ |

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

## Amazon Ads

### MarketplaceAdPros/amazon-ads-mcp-server — First Open-Source Amazon Ads Server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [amazon-ads-mcp-server](https://github.com/MarketplaceAdPros/amazon-ads-mcp-server) | 21 | JavaScript | MIT | 10+ |

**The first open-source Amazon Ads MCP server, filling the biggest gap from our previous review:**

- **Sponsored Products** — manage campaigns, ad groups, keywords, and product ads
- **Sponsored Brands** — brand campaign management and reporting
- **Sponsored Display** — display ad campaign operations
- **Reporting** — pull performance reports with natural language queries
- **Recommendations** — access Amazon's optimization recommendations

Available as a Streamable HTTP MCP server via MarketplaceAdPros' hosted service. MIT licensed. This fills a critical gap — Amazon is the second-largest digital advertising platform, and until now had no open-source MCP server. Amazon's own official MCP server remains in open beta (announced February 2026 at the IAB Annual Leadership Meeting) with tools for campaign creation, keyword/product targeting, performance reporting, bid optimization, and billing management.

---

## Programmatic & DSP

### StackAdapt MCP Server — Official Programmatic DSP

**The first major programmatic DSP to launch an official MCP server (April 21, 2026):**

- **Campaign intelligence** — monitor performance, pacing, and audience results in real time
- **Creative auditing** — review creative status and effectiveness
- **Multi-channel coverage** — connected TV (CTV), display, native, audio, digital out-of-home (DOOH), and programmatic linear TV
- **Natural language queries** — ask conversational questions about campaign data
- **Multi-step analysis** — AI agents can retrieve, consolidate, and analyze data across campaigns

StackAdapt's MCP server is a significant milestone — the first major programmatic DSP to provide official MCP support, making campaign intelligence directly accessible within AI tools like Claude. No engineering resources, API integrations, or additional cost required for setup. Extends the capabilities of Ivy, StackAdapt's AI marketing assistant.

### zMaticoo MCP — ADX/DSP Data Access

**Commercial MCP for programmatic advertising data (launched April 21, 2026):**

- **adx-report** — access Ad Exchange data via natural language
- **dsp-report** — access Demand-Side Platform data via natural language
- **Token-based auth** — secure, per-client authorization
- **Zero-code access** — retrieve advertising reports without coding

zMaticoo, an AI-driven programmatic advertising platform under eclicktech, launched MCP support on the same day as StackAdapt. The implementation upgrades their Open API to tool-oriented capabilities, letting LLMs read, write, and operate ADX/DSP data through natural language. Commercial offering requiring a client token from zMaticoo.

### Guideline Media Plan Management MCP — Media Planning Intelligence

**Commercial MCP for media planning and buying (launched March 2026):**

- **Media plan queries** — conversational access to campaign status, budget allocation, and vendor performance
- **Plan-to-actual comparison** — analyze planned vs. actual spend and delivery
- **Multi-campaign analysis** — consolidate data across campaigns, clients, and markets
- **Read-only access** — secure, non-destructive data exploration

Guideline's MCP server connects AI agents to their media plan management platform, enabling agencies and enterprise clients to interact with media plans conversationally. Works with Claude, ChatGPT, and proprietary internal AI tools. The first in a planned series of MCP capabilities from Guideline.

---

## Protocol & Standards

### adcontextprotocol/adcp — Open Standard for AI Advertising

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [adcp](https://github.com/adcontextprotocol/adcp) | 211 | TypeScript | Apache-2.0 | 8 domains |

**An open standard defining how AI agents interact with advertising systems:**

- **Media Buy** — discover inventory and purchase media programmatically
- **Creative** — build and manage ad creatives across formats
- **Signals** — audience activation and signal management
- **Accounts** — manage advertiser accounts and permissions
- **Governance** — brand safety and compliance rules
- **Brand** — brand asset management and guidelines
- **Sponsored Intelligence** — sponsored content and native advertising
- **Curation** — content curation and recommendation

Not an MCP server itself but a protocol standard built on top of MCP and A2A (Agent-to-Agent) transports. **AdCP v3.0.0 was released on April 22, 2026** — a major version bump with 2,560 total commits on main and 9 releases total. At 211 stars (up from 193) and Apache-2.0 licensed, it's establishing itself as the industry standard for agentic advertising. The reference implementation and JSON schemas make it practical to adopt. The v3.0.0 release alongside StackAdapt and zMaticoo's MCP launches signals that the programmatic advertising industry is converging on MCP as its agent integration standard.

---

## Ad Auditing & Optimization

### AgriciDaniel/claude-ads — Comprehensive Ad Audit Skill

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [claude-ads](https://github.com/AgriciDaniel/claude-ads) | 3,200 | Python | MIT | 250+ checks |

**The highest-starred project in the advertising AI space — and one of the fastest-growing (Claude Code skill, not MCP server):**

- **Google Ads** — 80 audit checks covering campaign structure, bidding, keywords, and quality
- **Meta Ads** — 50 checks for campaign setup, audience targeting, and creative effectiveness
- **Apple Search Ads** — 35+ checks for App Store advertising
- **LinkedIn Ads** — 27 checks for B2B campaign optimization
- **TikTok Ads** — 28 checks for short-form video ad campaigns
- **Microsoft/Bing Ads** — 24 checks for Microsoft network ads
- **Cross-platform** — 3 cross-platform coverage checks
- **Ads Health Score** — weighted 0–100 scoring with letter grades (A through F)
- **Parallel analysis** — spawns subagents for simultaneous platform analysis
- **Industry templates** — pre-built configurations for 12 business types
- **PPC financial modeling** — `/ads math` command for financial calculators
- **A/B test design** — `/ads test` command for experiment planning
- **PDF reports** — generate client-ready deliverables

At 3,200 stars (up from 981 — tripled in six weeks), this is the runaway hit of the advertising AI space. The growth from 190+ to 250+ checks, the addition of PPC financial modeling and A/B test design tools, and PDF report generation make it increasingly useful as a complete ad operations assistant. Privacy-focused: all analysis runs locally with no data sent to external servers. MIT licensed.

---

## Also notable

- **JanNafta/propellerads-mcp** (0 stars, Python, MIT) — the only PropellerAds MCP server, with 19 tools for push/pop ad network campaign management, zone-level optimization, and auto-blacklisting of underperforming zones
- **jshorwitz/awesome-agentic-advertising** — curated list of MCP servers and tools for AI-powered advertising across all major platforms
- **Amazon Ads MCP (official)** — in open beta (Feb 2026) supporting Sponsored Products, Brands, Display, performance reporting, bid optimization, and billing. Announced at the IAB Annual Leadership Meeting. Now complemented by MarketplaceAdPros' open-source server (see Amazon Ads section above)
- **AdRoll + PubMatic MCP integration** (April 23, 2026) — agent-to-agent diagnostics allowing demand-side AI agents to query supply-side diagnostics directly via MCP, demonstrating cross-ecosystem MCP adoption in programmatic advertising
- **Pipeboard CLI** — new command-line tool from the meta-ads-mcp team providing access to Meta, Google, and TikTok Ads from a single binary, signaling Pipeboard's evolution from single-platform MCP server to multi-platform ad-tech company

---

## What's missing

The advertising MCP ecosystem has matured significantly since our last review, but gaps remain:

- **Amazon Ads open-source maturity** — MarketplaceAdPros fills the gap, but at 21 stars it's still early. Amazon's official server remains in beta. The #2 ad platform deserves deeper open-source coverage
- **Pinterest Ads** — no MCP server for Pinterest's visual ad platform
- **Snapchat Ads** — no Snap Ads Manager integration
- **Programmatic DSPs beyond StackAdapt** — The Trade Desk and DV360 still only accessible through synter-mcp-server; no dedicated native servers from either platform. StackAdapt's launch should pressure other DSPs to follow
- **Ad creative generation** — only synter-mcp-server offers AI creative generation; no standalone creative pipeline servers
- **Attribution & measurement** — no cross-platform attribution tools (no Google Analytics 4 conversion import, no AppsFlyer/Adjust/Branch integration). This remains the biggest functional gap — you can manage campaigns across platforms but can't close the attribution loop through MCP
- **Ad fraud detection** — no servers for invalid traffic detection or brand safety monitoring
- **Retail media** — no Walmart Connect, Instacart Ads, or other retail media network servers

---

## The bottom line

The advertising MCP ecosystem earns **4.5 out of 5**. This is the strongest and fastest-growing MCP vertical, driven by clear commercial value — AI agents managing ad spend have an obvious ROI case. **The biggest story this refresh is enterprise adoption** — StackAdapt became the first major programmatic DSP to launch an official MCP server, Amazon Ads now has open-source coverage via MarketplaceAdPros, and AdCP hit v3.0.0 as the industry converges on MCP as its agent integration standard. **Meta Ads continues to dominate single-platform servers** — pipeboard-co at 819 stars with a new cloud-hosted Remote MCP service. **Google Ads has the deepest ecosystem** with 8+ servers and the official server growing to 404 stars and 3 tools. **Ad auditing exploded** — claude-ads tripled from 981 to 3,200 stars in six weeks with 250+ checks, PPC financial modeling, and A/B test design. **The programmatic advertising stack is arriving** — between StackAdapt, zMaticoo, Guideline, and the AdRoll/PubMatic agent-to-agent integration, MCP is spreading across the full advertising supply chain. The half-point deduction is for the continued lack of cross-platform attribution/measurement tools and no retail media network coverage — you can manage campaigns across platforms but can't yet close the attribution loop through MCP.

---

*Last updated: 2026-04-26. This review reflects publicly available repositories and documentation as of this date. ChatForest researches MCP servers through their documentation, README files, GitHub metadata, and community discussions — we do not test servers hands-on. Star counts are approximate and change over time. "Tools" refers to MCP tool definitions exposed by each server. Have a correction or addition? [Let us know.](/about/)*

*This review was last edited on 2026-04-26 using Claude Opus 4.6 (Anthropic).*

