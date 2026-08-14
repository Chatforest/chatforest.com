# Advertising & Ad-Tech MCP Servers — Google Ads, Meta Ads, Amazon Ads, TikTok Ads, LinkedIn Ads, Programmatic DSPs, Multi-Platform Campaign Management, and Ad Auditing

> Advertising and ad-tech MCP servers let AI agents manage campaigns, analyze performance, and optimize budgets across Google Ads, Meta Ads, Amazon Ads, TikTok Ads, and LinkedIn Ads through the


Advertising and ad-tech MCP servers connect AI agents to campaign management platforms, performance analytics, and budget optimization tools across major ad networks. Instead of juggling Google Ads, Meta Business Suite, TikTok Ads Manager, and LinkedIn Campaign Manager, these servers let AI assistants create campaigns, pull performance data, and optimize spend through the Model Context Protocol.

This review covers the **advertising and ad-tech** vertical — Google Ads, Meta/Facebook Ads, TikTok Ads, multi-platform campaign management, ad protocol standards, and ad auditing tools. For SEO and organic search tools, see our [SEO & Search Optimization review](/reviews/seo-search-optimization-mcp-servers/). For marketing automation and email, see our [Email & Communication review](/reviews/gmail-mcp-servers/). For analytics platforms, see our [Analytics MCP review](/reviews/analytics-mcp-servers/).

The headline findings: **TikTok launched an official MCP server** (May 13, 2026 at TikTok World '26) — Google, Meta, Amazon, and TikTok now all have official MCP support, completing the big-four ad platform coverage. **Meta Ads has the most popular single server** — pipeboard-co/meta-ads-mcp at [1,171 stars](https://github.com/pipeboard-co/meta-ads-mcp) with 42 tools for full campaign lifecycle management, now available as a cloud-hosted Remote MCP service. **Google Ads has the deepest ecosystem** — 8+ servers including an [official one from Google](https://github.com/googleads/google-ads-mcp) now at 854 stars. **Amazon Ads finally has open-source coverage** — MarketplaceAdPros fills the biggest gap from our previous review. **Programmatic DSPs are arriving** — StackAdapt and zMaticoo both launched official MCP servers in April 2026. **Multi-platform servers keep growing** — ads-mcp now covers 6 networks (adding Amazon and ChatGPT Ads) while synter-mcp-server spans 19. **Ad auditing has exploded** — [claude-ads](https://github.com/AgriciDaniel/claude-ads) has grown past 8,000 stars and now covers 12 ad platforms.

**Category:** [Business & Productivity](/categories/business-productivity/)

---

## Google Ads

### cohnen/mcp-google-ads — Community Favorite for Google Ads

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [mcp-google-ads](https://github.com/cohnen/mcp-google-ads) | 683 | Python | MIT | 5 |

**The most popular community Google Ads MCP server:**

- **GAQL query execution** — run arbitrary Google Ads Query Language queries for maximum flexibility
- **Campaign performance** — pull campaign-level metrics including clicks, impressions, cost, and conversions
- **Ad performance** — analyze individual ad effectiveness across ad groups
- **Account listing** — discover and switch between multiple Google Ads accounts
- **OAuth and service account auth** — supports both interactive and automated authentication flows

At [683 stars](https://github.com/cohnen/mcp-google-ads), this is the most-starred dedicated (non-official) Google Ads MCP server. The GAQL interface means any data available through the Google Ads API is accessible — you're not limited to pre-built reports. MIT licensed, Python-based, and works with Claude, Cursor, and Windsurf. The trade-off is that effective use requires GAQL knowledge.

### googleads/google-ads-mcp — Official Google Ads Server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [google-ads-mcp](https://github.com/googleads/google-ads-mcp) | 854 | Python | Apache-2.0 | 3 |

**Official Google Ads MCP server (experimental):**

- **Search** — execute GAQL queries against your Google Ads account
- **Get resource metadata** — retrieve metadata about API resource types for query building
- **List accessible customers** — discover all accounts you have access to
- **4 LLM resources** — discovery document, metrics, segments, and release notes exposed as MCP resources
- **Two auth methods** — Application Default Credentials (ADC) or client library configuration

Google's official entry has grown from 2 to 3 tools since launch, adding resource metadata introspection and 4 MCP resources that give LLMs contextual knowledge about the Google Ads API. At [854 stars](https://github.com/googleads/google-ads-mcp), adoption has accelerated sharply — more than double the count from our previous audit. Read-only by design, which is a safety feature for production ad accounts. Supports Gemini Code Assist and Gemini CLI.

### google-marketing-solutions/google_ads_mcp_server — Archived, Merged Into the Official Server

**Update: this server is no longer a separate option.** [google-marketing-solutions/google_ads_mcp_server](https://github.com/google-marketing-solutions/google_ads_mcp_server) — a separate implementation from Google's marketing solutions team that predated the official googleads org server — [was archived by its owner on December 13, 2025](https://github.com/google-marketing-solutions/google_ads_mcp_server), with the repository's own README stating: "This repo has been archived in favor of: [github.com/googleads/google-ads-mcp](https://github.com/googleads/google-ads-mcp)." It is now read-only with 11 stars. If you're evaluating Google's Google Ads MCP options, use the official googleads/google-ads-mcp server above rather than this one.

### Other Notable Google Ads Servers

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [gomarble-ai/google-ads-mcp-server](https://github.com/gomarble-ai/google-ads-mcp-server) | 140 | Python | MIT | 3 |
| [promobase/google-ads-mcp](https://github.com/promobase/google-ads-mcp) | 22 | Python | MIT | 90/103 services |
| [grantweston/google-ads-mcp-complete](https://github.com/grantweston/google-ads-mcp-complete) | 24 | Python | MIT | 45+ |
| [bjorndavidhansen/google-ads-mcp-server](https://github.com/bjorndavidhansen/google-ads-mcp-server) | 19 | Python | — | 30+ |
| [DigitalRocket-biz/google-ads-mcp-v20](https://github.com/DigitalRocket-biz/google-ads-mcp-v20) | 11 | Python | MIT | ~15–20 |

The Google Ads MCP ecosystem is remarkably deep:

- **[GoMarble AI](https://github.com/gomarble-ai/google-ads-mcp-server)** (140 stars) — focused on performance analysis with a `run_keyword_planner` tool for keyword ideas and search-volume metrics, from a commercial ad-tech company (gomarble.ai)
- **[Promobase](https://raw.githubusercontent.com/promobase/google-ads-mcp/main/README.md)** (22 stars) — implements 90 of 103 Google Ads API v20 services with type-safe Python, covering campaign, ad group, ad, budget, keyword, conversion, asset, audience, recommendation, account, billing, and reporting workflows — among the most comprehensive by raw API surface
- **grantweston/google-ads-mcp-complete** (24 stars) — 45+ tools covering campaign lifecycle, Smart Bidding, ad extensions, and ROAS optimization using modern AssetService
- **bjorndavidhansen** (19 stars) — unique for Docker/Kubernetes deployment support and automated anomaly detection with optimization suggestions
- **DigitalRocket-biz** (11 stars) — Performance Max negative keywords support and automatic retry with exponential backoff

The range from Google's minimal 3-tool official server to Promobase's near-full API wrapper shows how differently teams approach the same API. For read-only analysis, the official server or cohnen's are safest. For full campaign management, grantweston or Promobase provide the most tools.

---

## Meta / Facebook Ads

### pipeboard-co/meta-ads-mcp — Most Popular Ad-Tech MCP Server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [meta-ads-mcp](https://github.com/pipeboard-co/meta-ads-mcp) | 1,171 | Python | BSL-1.1 | 42 |

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

At [1,171 stars](https://github.com/pipeboard-co/meta-ads-mcp), up from 819 at our last audit, this continues its dominance as the most popular advertising MCP server, now with 42 tools (up from 24). Now available as a **Remote MCP cloud service** — the recommended approach for getting started quickly — alongside traditional local installation. Pipeboard has also launched **[Pipeboard CLI](https://github.com/pipeboard-co/pipeboard-cli)**, a single Go binary (117 commands) that now provides access to five platforms — Meta, Google, TikTok, Snap, and Reddit Ads — signaling the company's expansion from a single-platform MCP server to a multi-platform ad-tech company. Licensed under [BSL-1.1](https://raw.githubusercontent.com/pipeboard-co/meta-ads-mcp/main/LICENSE) (converts to Apache-2.0 on January 1, 2029). Works with Claude Pro/Max, Cursor, and other MCP-compatible platforms.

### gomarble-ai/facebook-ads-mcp-server — Activity History Tracking

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [facebook-ads-mcp-server](https://github.com/gomarble-ai/facebook-ads-mcp-server) | 351 | Python | MIT | 23 |

**Meta Ads server with change history and simplified setup:**

- **Account data access** — read ad accounts, campaigns, ad sets, and ads
- **Collection browsing** — navigate ad creative collections and libraries
- **Performance insights** — pull ad performance with flexible date ranges
- **Activity history** — track changes made to campaigns and ad sets over time
- **One-click installers** — automated environment configuration for quick setup
- **Pagination support** — handle large result sets across all endpoints

From GoMarble AI (the same team behind the Google Ads server). The unique feature is activity/change history tracking — you can see what was modified and when, which is invaluable for auditing campaign changes. MIT licensed and [351 stars](https://github.com/gomarble-ai/facebook-ads-mcp-server) (up from 254 at our last audit) indicate strong adoption. The one-click installer reduces setup friction compared to manual OAuth configuration.

### gabe-almeida/meta-ads-mcp-server — TypeScript Alternative

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [meta-ads-mcp-server](https://github.com/gabe-almeida/meta-ads-mcp-server) | 4 | TypeScript | MIT | 20+ |

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

### TikTok MCP Server — Official Platform Integration *(May 2026)*

**[TikTok's official MCP server and companion Ads Skills toolkit, announced together at TikTok World '26 (May 13, 2026)](https://newsroom.tiktok.com/tiktok-world-26-turning-discovery-into-business-growth-with-ai-powered-innovations-vertical-experiences-and-high-impact-brand-solutions?lang=en):**

- **Campaign creation and management** — the MCP server itself lets AI agents build AI agents and tools directly on TikTok's ad ecosystem to execute campaign development and management, per TikTok's announcement
- **TikTok Ads Skills** — a companion developer toolkit providing modular building blocks; TikTok's announcement attributes campaign creation, performance insights, creative analysis, audience discovery, and budget optimization workflows specifically to this toolkit, alongside the MCP server

TikTok's announcement does not itemize bid optimization or fine-grained targeting controls as confirmed MCP-server capabilities — those workflow descriptions apply to the Ads Skills toolkit per the source above, so this review no longer lists them as separate MCP-server bullets.

TikTok announced the MCP server at TikTok World '26, their sixth annual global ad product summit, alongside a broader push toward autonomous AI-driven campaign management. The announcement joins Google, Meta, and Amazon in the cohort of major ad platforms with official MCP support — a significant milestone for the ad-tech MCP ecosystem. The companion TikTok Ads Skills toolkit is notable: rather than a monolithic server, it provides composable building blocks for development teams building custom ad agent workflows.

### AdsMCP/tiktok-ads-mcp-server — Campaign Management

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [tiktok-ads-mcp-server](https://github.com/AdsMCP/tiktok-ads-mcp-server) | 48 | Python | MIT | 20 |

**TikTok Ads server, currently read-only despite write features on its roadmap:**

- **Authentication** — 4 tools for OAuth login, session completion, status checks, and switching ad accounts
- **Campaign inspection** — 6 tools to retrieve and inspect campaigns, ad groups, and individual ads
- **Performance analytics** — 5 tools for campaign/ad-group/ad-level metrics, audience breakdowns, and spend audits
- **Creative & audience** — 5 tools for custom audiences, advertiser info, location targeting, and pixel event stats

**Correction from a prior version of this review:** this server is currently **read-only**, not read/write. Its own documentation states: "The public MCP tool registry does not expose campaign creation, ad group creation, creative upload, or other write operations" — safe write operations are on the roadmap but not yet shipped. All 20 tools connect to TikTok's live Marketing API rather than mock data. Part of the broader AdsMCP ecosystem that also covers Google and Meta, so the authentication patterns and data models are consistent across platforms.

### ysntony/tiktok-ads-mcp — Read-Only Safety-First

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [tiktok-ads-mcp](https://github.com/ysntony/tiktok-ads-mcp) | 40 | Python | MIT | 6 |

**Read-only TikTok Ads server with multi-advertiser support:**

- **Business center access** — list business centers and authorized accounts
- **Campaign/ad group/ad listing** — browse the full campaign hierarchy
- **Flexible reporting** — custom dimensions, metrics, and date ranges
- **Multi-advertiser** — query multiple advertiser accounts in single requests
- **Rate limit handling** — automatic retry on API throttling

Deliberately read-only — a safety-first approach for teams that want AI agents to analyze TikTok ad performance without the risk of accidentally modifying live campaigns. The multi-advertiser support is useful for agencies managing many accounts.

---

## Multi-Platform Campaign Management

### amekala/ads-mcp — Six Networks, One Server (Now Proprietary-Licensed)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [ads-mcp](https://github.com/amekala/ads-mcp) | 82 | Shell | Proprietary | 400+ |

**Cross-platform ad management, now spanning six networks per the [project's own README](https://raw.githubusercontent.com/amekala/ads-mcp/main/README.md):**

- **Google Ads** — 151 tools for campaigns, keywords, bidding, and reporting
- **Amazon Ads** — 61 tools
- **Meta Ads** — 58 tools for Facebook/Instagram campaigns
- **LinkedIn Ads** — 54 tools for B2B campaign management
- **TikTok Ads** — 37 tools
- **ChatGPT Ads** — 31 tools
- **Strategy persistence** — saves campaign strategy to STRATEGY.md across sessions
- **Hosted service** — available at mcp.adspirer.com

**Update from a prior version of this review:** the platform and tool count both grew substantially — from 4 networks/~100 tools to 6 networks/400+ tools (Google, Amazon, Meta, LinkedIn, TikTok, and ChatGPT Ads) — and the license changed from unspecified to **Proprietary** ("See Terms of Service for usage terms," per the repo's own listing), so this is no longer an open-source option despite the public GitHub repo. The most notable feature is strategy persistence — the server maintains a STRATEGY.md file that carries campaign strategy context across AI sessions. The LinkedIn Ads coverage (54 tools) remains among the strongest available in any MCP server. Hosted cloud service model means no local setup required. At [82 stars](https://github.com/amekala/ads-mcp), up from 35 at our last audit.

### jshorwitz/synter-mcp-server — 19 Platforms with AI Creative

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [synter-mcp-server](https://github.com/jshorwitz/synter-mcp-server) | 16 | TypeScript | MIT | 140+ |

**The widest platform coverage of any advertising MCP server, per the [project's own README](https://raw.githubusercontent.com/jshorwitz/synter-mcp-server/main/README.md):**

- **19 ad platforms for reporting** — Google Ads, Microsoft Ads (Bing), Meta, LinkedIn, X, Reddit, TikTok, Snapchat, Pinterest, Spotify, Amazon Ads, Amazon DSP, Walmart Connect, Instacart Ads, Target Roundel, Criteo, The Trade Desk, Display & Video 360, and OpenAI Ads
- **Full campaign creation** — supported on 14 of the 19 platforms; write actions short of full creation are supported on 16 total
- **Budget management** — set and optimize budgets cross-platform
- **Conversion tracking** — cross-platform conversion setup
- **AI creative generation** — the README describes generating images, video, and copy but does not name specific underlying models
- **Performance analytics** — unified reporting across all platforms

**Update from a prior version of this review:** platform coverage is now 19, not "9+" — a significant undercount in the earlier audit. Programmatic options like The Trade Desk, DV360, and Amazon DSP remain unique to this server among the ones tracked in this review. This review previously named Imagen 4, Veo, and Flux as the specific creative-generation models; the current README does not confirm any of those three by name, so that detail has been removed rather than repeated unverified. MIT licensed. The "first MCP server that gives AI agents a credit card" tagline is a direct quote from the project's own README, signaling autonomous spending capability.

---

## Amazon Ads

### MarketplaceAdPros/amazon-ads-mcp-server — First Open-Source Amazon Ads Server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [amazon-ads-mcp-server](https://github.com/MarketplaceAdPros/amazon-ads-mcp-server) | 29 | JavaScript | MIT | 10+ |

**The first open-source Amazon Ads MCP server, filling the biggest gap from our previous review:**

- **Sponsored Products** — manage campaigns, ad groups, keywords, and product ads
- **Sponsored Brands** — brand campaign management and reporting
- **Sponsored Display** — display ad campaign operations
- **Reporting** — pull performance reports with natural language queries
- **Recommendations** — access Amazon's optimization recommendations

Available as a Streamable HTTP MCP server via MarketplaceAdPros' hosted service. MIT licensed. This fills a critical gap — Amazon is the second-largest digital advertising platform, and until now had no open-source MCP server. Amazon's own [official MCP server remains in open beta](https://advertising.amazon.com/library/news/amazon-ads-mcp-server-open-beta) (announced February 2, 2026 at the IAB Annual Leadership Meeting) with tools for campaign creation/updating/deletion, performance and report queries, account-level settings, and billing/financial data — see "Also notable" below for the confirmed capability list.

---

## Programmatic & DSP

### StackAdapt MCP Server — Official Programmatic DSP

**The [first major programmatic DSP to launch an official MCP server (April 21, 2026)](https://www.businesswire.com/news/home/20260421122109/en/StackAdapt-Brings-Campaign-Intelligence-Into-Claude-and-Other-AI-Workflows-With-Launch-of-MCP-Server):**

- **Campaign intelligence** — monitor performance, pacing, and audience results in real time
- **Creative auditing** — review creative status and effectiveness
- **Multi-channel coverage** — connected TV (CTV), display, native, audio, digital out-of-home (DOOH), and programmatic linear TV
- **Natural language queries** — ask conversational questions about campaign data
- **Multi-step analysis** — AI agents can retrieve, consolidate, and analyze data across campaigns

StackAdapt's MCP server is a significant milestone — the first major programmatic DSP to provide official MCP support, making campaign intelligence directly accessible within AI tools like Claude. No engineering resources, API integrations, or additional cost required for setup. Extends the capabilities of Ivy, StackAdapt's AI marketing assistant.

### zMaticoo MCP — ADX/DSP Data Access

**[Commercial MCP for programmatic advertising data (launched April 21, 2026)](https://www.prnewswire.com/news-releases/zmaticoo-launches-model-context-protocol-mcp-enhancing-ai-access-to-business-data-302748432.html):**

- **adx-report** — access Ad Exchange data via natural language
- **dsp-report** — access Demand-Side Platform data via natural language
- **Token-based auth** — secure, per-client authorization
- **Zero-code access** — retrieve advertising reports without coding

zMaticoo, an AI-driven programmatic advertising platform under eclicktech, launched MCP support on the same day as StackAdapt. The implementation upgrades their Open API to tool-oriented capabilities, letting LLMs read, write, and operate ADX/DSP data through natural language. Commercial offering requiring a client token from zMaticoo.

### Guideline Media Plan Management MCP — Media Planning Intelligence

**[Commercial MCP for media planning and buying (launched March 5, 2026)](https://www.guideline.ai/blog/guideline-launches-media-plan-management-mcp-server-enabling-agentic-ai-workflows-across-media-plan-management-buying):**

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
| [adcp](https://github.com/adcontextprotocol/adcp) | 241 | TypeScript | Apache-2.0 | 8 domains |

**An open standard defining how AI agents interact with advertising systems:**

- **Media Buy** — discover inventory and purchase media programmatically
- **Creative** — build and manage ad creatives across formats
- **Signals** — audience activation and signal management
- **Accounts** — manage advertiser accounts and permissions
- **Governance** — brand safety and compliance rules
- **Brand** — brand asset management and guidelines
- **Sponsored Intelligence** — sponsored content and native advertising
- **Curation** — content curation and recommendation

Not an MCP server itself but a protocol standard built on top of MCP and A2A (Agent-to-Agent) transports. **[AdCP 3.0 reached General Availability in April 2026](https://docs.adcontextprotocol.org/docs/reference/release-notes)**, and the [project has continued iterating rapidly since](https://github.com/adcontextprotocol/adcp/releases) — it's now well past that milestone, at v3.1.13 as of this audit. At [241 stars](https://github.com/adcontextprotocol/adcp) and Apache-2.0 licensed, it's establishing itself as the industry standard for agentic advertising. The reference implementation and JSON schemas make it practical to adopt. The v3.0 GA release alongside StackAdapt and zMaticoo's MCP launches in the same week signals that the programmatic advertising industry is converging on MCP as its agent integration standard.

---

## Ad Auditing & Optimization

### AgriciDaniel/claude-ads — Comprehensive Ad Operations Skill

| Server | Stars | Language | License | Platforms |
|--------|-------|----------|---------|-------|
| [claude-ads](https://github.com/AgriciDaniel/claude-ads) | 8,000+ | Python | MIT | 12 |

**The highest-starred project in the advertising AI space (Claude Code skill, not MCP server). Per the [project's own README](https://raw.githubusercontent.com/AgriciDaniel/claude-ads/main/README.md):**

- **12 ad platforms** — Google Ads, Meta Ads, YouTube Ads, LinkedIn Ads, TikTok Ads, Microsoft Advertising, Reddit Ads, Snapchat Ads, X Ads, Apple Ads, Amazon Ads, and Pinterest Ads
- **Evidence-backed audits** — `/ads audit [all|platform|scope]` runs a complete or scoped audit
- **Coverage-based grading** — checks are scored "graded" (80%+ evidence coverage), "provisional" (60–79%), or "insufficient evidence" (below 60%) rather than a single numeric score
- **Full ad-ops command set** — `/ads setup`, `/ads plan`, `/ads create` (copy/image/video/product-photo assets), `/ads launch --draft`, `/ads monitor`, `/ads optimize --draft`, `/ads experiment` (A/B test design), `/ads report`, `/ads research refresh`, and `/ads validate`
- **Approval-gated live changes** — the README states live account changes "stay disabled until the exact platform and operation pass approval, idempotency, verification, audit, and rollback gates"
- **PDF reports** — renders Markdown, HTML, and optional PDF report bundles

**Update from a prior version of this review — the project has changed substantially since our last audit, and several specifics in the earlier version of this entry no longer match the current README:** platform coverage expanded from 7 to 12 platforms (adding YouTube, Reddit, Snapchat, X, and Pinterest); stars grew from 3,200 to over 8,000; the previously-cited "weighted 0–100 scoring with letter grades A–F" has been replaced with the coverage-based graded/provisional/insufficient system described above; the previously-cited `/ads math` and `/ads test` commands do not appear in the current command list (test design now lives under `/ads experiment`); a previously-cited "250+ checks" total and "12 business-type industry templates" claim do not appear in the current README and have been removed rather than repeated unverified; and the previous "all analysis runs locally, no data sent to external servers" privacy claim overstated what the README actually says, which is narrower — that client data, credentials, and transcripts "must never enter Git history, reports, or release archives." MIT licensed, confirmed via the README's own license statement.

---

## Also notable

- **[JanNafta/propellerads-mcp](https://github.com/JanNafta/propellerads-mcp)** (3 stars, Python, MIT) — the only PropellerAds MCP server, with 16 tools for push/pop ad network campaign management, statistics/analytics, optimization, and zone-level targeting, including auto-blacklisting of underperforming zones
- **jshorwitz/awesome-agentic-advertising** — curated list of MCP servers and tools for AI-powered advertising across all major platforms
- **[Amazon Ads MCP (official)](https://advertising.amazon.com/library/news/amazon-ads-mcp-server-open-beta)** — in open beta (announced Feb 2, 2026 at the IAB Annual Leadership Meeting) supporting campaign creation/updating/deletion, performance and report queries, account-level settings management, and billing/financial data access. Now complemented by MarketplaceAdPros' open-source server (see Amazon Ads section above)
- **[AdRoll + PubMatic MCP integration](https://www.globenewswire.com/news-release/2026/04/23/3280009/0/en/adroll-and-pubmatic-enable-agent-powered-deal-troubleshooting-via-mcp-integration.html)** (April 23, 2026) — agent-to-agent diagnostics allowing demand-side AI agents to query supply-side diagnostics directly via MCP, demonstrating cross-ecosystem MCP adoption in programmatic advertising
- **[Pipeboard CLI](https://github.com/pipeboard-co/pipeboard-cli)** — command-line tool from the meta-ads-mcp team now providing access to five platforms (Meta, Google, TikTok, Snap, and Reddit Ads) from a single binary, signaling Pipeboard's evolution from single-platform MCP server to multi-platform ad-tech company

---

## What's missing

The advertising MCP ecosystem has matured significantly since our last review, but gaps remain:

- **Amazon Ads open-source maturity** — MarketplaceAdPros fills the gap, but at 29 stars it's still early. Amazon's official server remains in beta. The #2 ad platform deserves deeper open-source coverage
- **Pinterest Ads** — no dedicated MCP server for Pinterest's visual ad platform (claude-ads audits Pinterest as one of its 12 platforms, but that's an audit skill, not a campaign-management server)
- **Snapchat Ads** — no dedicated Snap Ads Manager MCP server (same caveat — claude-ads covers it for auditing, not campaign management)
- **Programmatic DSPs beyond StackAdapt** — The Trade Desk and DV360 still only accessible through synter-mcp-server; no dedicated native servers from either platform. StackAdapt's launch should pressure other DSPs to follow
- **Ad creative generation** — only synter-mcp-server offers AI creative generation; no standalone creative pipeline servers
- **Attribution & measurement** — no cross-platform attribution tools (no Google Analytics 4 conversion import, no AppsFlyer/Adjust/Branch integration). This remains the biggest functional gap — you can manage campaigns across platforms but can't close the attribution loop through MCP
- **Ad fraud detection** — no servers for invalid traffic detection or brand safety monitoring
- **Retail media** — no Walmart Connect, Instacart Ads, or other retail media network servers

---

## The bottom line

The advertising MCP ecosystem earns **4.5 out of 5**. This is the strongest and fastest-growing MCP vertical, driven by clear commercial value — AI agents managing ad spend have an obvious ROI case. **The biggest story in May 2026 is TikTok's official MCP server** — announced at TikTok World '26 (May 13, 2026), TikTok joins Google, Meta, and Amazon as the fourth major ad platform with official MCP support. The big-four coverage is now complete. **StackAdapt remains the first major programmatic DSP** to launch an official MCP server, and AdCP reached v3.0 GA (now iterating past it, at v3.1.13) as the industry converges on MCP as its agent integration standard. **Meta Ads continues to dominate single-platform servers** — pipeboard-co now at 1,171 stars and 42 tools with a cloud-hosted Remote MCP service. **Google Ads has the deepest ecosystem** with 8+ servers and the official server now at 854 stars. **Ad auditing exploded further** — claude-ads has grown from 3,200 to over 8,000 stars and expanded from 7 to 12 audited ad platforms. **The programmatic advertising stack is maturing** — between StackAdapt, zMaticoo, Guideline, and the AdRoll/PubMatic agent-to-agent integration, MCP is spreading across the full advertising supply chain. The half-point deduction remains for the continued lack of cross-platform attribution/measurement tools and no retail media network coverage — you can manage campaigns across platforms but can't yet close the attribution loop through MCP.

---

*Last updated: 2026-08-14. This review reflects publicly available repositories and documentation as of this date. ChatForest researches MCP servers through their documentation, README files, GitHub metadata, and community discussions — we do not test servers hands-on. Star counts are approximate and change over time. "Tools" refers to MCP tool definitions exposed by each server. Have a correction or addition? [Let us know.](/about/)*

*This review was last edited on 2026-08-14 using Claude Sonnet 5 (Anthropic) as part of a claim-level citation re-audit.*

