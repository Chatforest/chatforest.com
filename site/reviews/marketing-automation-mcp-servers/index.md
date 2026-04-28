# Marketing Automation MCP Servers — Email Marketing, Ad Platforms, SEO, and Social Media Management

> Marketing automation MCP servers let AI agents manage email campaigns, run ad platforms, analyze SEO data, and schedule social media posts.


Marketing automation MCP servers let AI agents manage email campaigns, run advertising platforms, analyze SEO data, and schedule social media content. Instead of switching between marketing dashboards, AI assistants can directly create campaigns, analyze performance, and optimize marketing workflows. Part of our **[Business & Productivity MCP category](/categories/business-productivity/)**.

This review covers **marketing automation MCP servers** — email marketing platforms, CRM/marketing hubs, advertising platforms, SEO tools, and social media management. For related servers, see our [Social Media & Marketing review](/reviews/social-media-marketing-mcp-servers/), [E-Commerce & Shopping review](/reviews/ecommerce-shopping-mcp-servers/), and [Analytics & Business Intelligence review](/reviews/analytics-mcp-servers/).

The headline findings: **Ad platforms are now the most mature MCP category** — Amazon Ads launched its official MCP (February 2026), googleads/google-ads-mcp hit 404 stars, and pipeboard-co/meta-ads-mcp surged to 823 stars. **Cross-platform orchestration gap is closing** — Synter Media covers 14 ad platforms, amekala/ads-mcp covers 4 with 175+ tools. **HubSpot official MCP went GA** with write access (April 13, 2026). **Intuit and Anthropic announced a multi-year partnership** bringing Mailchimp MCP integrations in spring 2026. **SEO tools surged** — GSC at 748 stars (+46%), Ahrefs SEO at 239 stars (+45%).

## Email Marketing

### deyikong/sendgrid-mcp — Most Comprehensive SendGrid MCP

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [sendgrid-mcp](https://github.com/deyikong/sendgrid-mcp) | 21 | Python | — | 59 |

**The most feature-complete SendGrid MCP server** — covers every aspect of email management and performance analysis:

- **59 tools** — marketing automations, single send campaigns, contact management, email statistics, and more
- **Read-only safety mode** — runs in read-only mode by default, with all mutable operations blocked at runtime
- **Marketing + transactional** — covers both marketing campaigns and transactional email operations
- **Analytics** — detailed performance analysis with engagement metrics

Good default choice for SendGrid users who want comprehensive API access with safety guardrails.

### Garoth/sendgrid-mcp — Focused SendGrid Marketing API

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [sendgrid-mcp](https://github.com/Garoth/sendgrid-mcp) | 24 | Python | — | 10+ |

**Streamlined SendGrid marketing integration** — focuses on the most common email marketing operations:

- **Contact list management** — create, update, and organize contacts and lists
- **Dynamic templates** — generate and use SendGrid dynamic templates for personalized emails
- **Single sends** — create and send email campaigns to contact lists
- **Basic analytics** — retrieve sending statistics and validation information

Better choice when you want a simpler, more focused SendGrid integration without the full 59-tool surface.

### houtini-ai/brevo-mcp — Brevo Email Marketing Platform

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [brevo-mcp](https://github.com/houtini-ai/brevo-mcp) | — | Python | — | 15+ |

**Comprehensive Brevo integration** with campaign management, analytics, and automation:

- **A/B testing** — create sophisticated email campaigns with A/B test variants
- **Segmentation** — target campaigns with contact segmentation
- **Campaign lifecycle** — create, update, and send test emails before launching
- **Multi-channel** — Brevo covers email and SMS marketing

Brevo now offers an **official MCP server** hosted at mcp.brevo.com — works with Claude Desktop, Cursor, Windsurf, VS Code, and more. Community BusyBee3333/brevo-mcp-2026-complete provides 55+ tools and 14 interactive apps.

### MailerLite Official MCP — Zero-Config Email Marketing

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [MailerLite MCP](https://www.mailerlite.com/features/mcp) | — | — | — | 8 |

**Official MailerLite MCP server requiring no API keys** — the easiest email marketing MCP to set up:

- **No API key needed** — direct connection from AI tools to MailerLite at mcp.mailerlite.com
- **8 tools** — subscriber management, campaign creation, group management, activity tracking
- **Remote MCP** — hosted server, no downloads or code required
- **Automation workflows** — set up automated email sequences

Notable for being one of the few email marketing MCPs with an official, no-configuration setup path.

### Other Email Marketing MCPs

- **ActiveCampaign** — official remote MCP server at mcp.activecampaign.com with 9 tools, **first marketing platform in Claude's official directory**. Works with all MCP-compatible AI tools
- **Klaviyo** — official MCP server now **GA** with enhanced reporting and remote server accessibility. Available as a Claude connector (Settings > Connectors). Plus mattcoatsworth/Klaviyo-MCP-Server (comprehensive profiles, lists, segments, campaigns, flows, templates, catalogs management)
- **Mailchimp** — **Intuit and Anthropic announced a multi-year partnership** (February 2026) bringing MCP integrations for Mailchimp, TurboTax, QuickBooks, and Credit Karma, rolling out to users in spring 2026. Community servers: LokiMCPUniverse/mailchimp-mcp-server (full API access), bryangsmith/MailchimpMCP (read-only campaign analytics), AgentX-ai/mailchimp-mcp (read-only)

## HubSpot CRM & Marketing

### HubSpot Official MCP — Now Generally Available

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [HubSpot MCP](https://developers.hubspot.com/mcp) | — | — | — | — |

**The official HubSpot remote MCP server graduated from beta to GA on April 13, 2026** — the most significant CRM MCP milestone:

- **Write capabilities added** — read and write to your CRM through natural conversation (was read-only in beta)
- **Engagement history** — access contact and company engagement data
- **Marketing content objects** — manage marketing assets directly
- **Permission-aware** — respects existing HubSpot user permissions throughout
- **Developer MCP also GA** — build HubSpot apps using natural language via `hs mcp setup`
- **Self-service MCP Auth Apps** — build and manage your own AI connectors to HubSpot MCP

The definitive choice for HubSpot users. Remote MCP means no local setup required.

### peakmojo/mcp-hubspot — HubSpot with Vector Search

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [mcp-hubspot](https://github.com/peakmojo/mcp-hubspot) | 121 | Python | — | 7 |

**The most-starred community HubSpot MCP** — surged from 72 to 121 stars (+68%) since March:

- **FAISS vector storage** — semantic search across previously retrieved HubSpot data
- **SentenceTransformer embeddings** — automatic embedding caching and persistent storage
- **Duplicate prevention** — built-in deduplication when creating contacts and companies
- **Docker deployment** — simple containerized setup with minimal configuration

Best for teams who want semantic search across CRM data — complements the official MCP with capabilities HubSpot's server doesn't offer.

### calypsoCodex/hubspot-mcp-extended — 106 Tools from OpenAPI Specs

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [hubspot-mcp-extended](https://github.com/calypsoCodex/hubspot-mcp-extended) | — | — | — | 106 |

**Most comprehensive HubSpot MCP** — 106 tools generated directly from HubSpot's official OpenAPI specifications:

- **Full CRM coverage** — contacts, companies, deals, tickets, quotes, products, invoices, line items
- **Auto-generated** — tools derived from official specs ensure complete API coverage
- **Public beta** — available for community testing and feedback

### Other HubSpot MCPs

- **shinzo-labs/hubspot-mcp** — comprehensive MCP implementation for HubSpot API
- **yespark/mcp-hubspot** — 40+ tools for CRM, marketing, and sales automation via REST API
- **lkm1developer/hubspot-mcp-server** — AI assistant integration for HubSpot CRM data

## Advertising Platforms

### pipeboard-co/meta-ads-mcp — Most Popular Marketing MCP Overall

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [meta-ads-mcp](https://github.com/pipeboard-co/meta-ads-mcp) | 823 | Python | BSL-1.1 | 25+ |

**The most-starred marketing automation MCP server** — surged from 601 to 823 stars (+37%) with Pipeboard expanding beyond Meta:

- **Campaign management** — create campaigns, update budgets, duplicate ads across Facebook and Instagram
- **Performance analytics** — retrieve detailed performance data and strategic insights
- **Creative optimization** — visualize ad creatives, analyze performance by creative variant
- **Audience targeting** — manage audience segments, interests, demographics, and locations
- **Remote MCP recommended** — streamable HTTP transport via Pipeboard cloud for most users
- **Pipeboard CLI** — unified command-line tool now supporting **Meta Ads + Google Ads + TikTok Ads** from a single binary

The go-to choice for Meta advertising automation. Pipeboard's expansion to Google and TikTok makes it the first multi-platform ad MCP ecosystem.

### Amazon Ads MCP Server — Official, Open Beta

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [Amazon Ads MCP](https://advertising.amazon.com/library/news/amazon-ads-mcp-server-open-beta) | — | — | — | 10+ |

**Amazon Ads launched its official MCP server in open beta (February 2, 2026)** — the biggest new entrant in ad platform MCPs:

- **End-to-end campaign creation** — create campaigns, ad groups, and ads in a single workflow (previously 3+ separate operations)
- **Performance reporting** — pull reports and analytics through natural language
- **Budget optimization** — adjust bids and budgets across campaigns
- **Global availability** — available to all Amazon Ads partners with active API credentials
- **Multi-AI support** — works with Claude, ChatGPT, Gemini, Amazon Q, and others

The first official Amazon advertising MCP. Covered by AdExchanger, Digiday, and AdWeek — signals enterprise ad platform MCP adoption accelerating.

### googleads/google-ads-mcp — Official Google Ads MCP (New Home)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [google-ads-mcp](https://github.com/googleads/google-ads-mcp) | 404 | Python | Apache-2.0 | 3 tools + 4 resources |

**Google's official MCP server migrated to the googleads organization** — 404 stars, the authoritative Google Ads MCP:

- **3 core tools** — `search` (account info retrieval), `get_resource_metadata` (API structure), `list_accessible_customers` (customer IDs)
- **4 resources** — discovery document, metrics info, segments info, release notes
- **v0.6.4** — latest release April 23, 2026 with 9 total releases
- **83 commits** — actively maintained with rapid iteration
- **Apache-2.0 licensed** — fully open source

Note: google-marketing-solutions/google_ads_mcp (183 stars) remains active alongside this repo. The older google_ads_mcp_server has been archived in favor of this repo.

### Cross-Platform Ad MCPs — The Gap Is Closing

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [ads-mcp](https://github.com/amekala/ads-mcp) | 37 | Multi | Proprietary | 175+ |

**Cross-platform ad management is emerging** — the biggest gap identified in our March review is now closing:

- **amekala/ads-mcp** (37 stars) — 175+ tools across Google Ads (75+), Meta Ads (36), LinkedIn Ads (45), TikTok Ads (31). Works with ChatGPT, Claude, Gemini CLI, Cursor, Codex, and Windsurf. Proprietary license.
- **Synter Media AI** — 160+ tools across **14 ad platforms** (Google, Meta, LinkedIn, TikTok, Reddit, Pinterest, Snapchat, X, Microsoft, Taboola, and more). First unified cross-platform MCP with full read/write access. Commercial at ~$199/month.
- **Pipeboard CLI** — supports Meta + Google + TikTok from a single binary alongside the meta-ads-mcp server.

### LinkedIn Ads MCPs — New Category

Multiple LinkedIn Ads MCP servers emerged since March 2026:

- **ZLeventer/linkedin-campaign-manager-mcp** (4 stars, TypeScript, MIT) — 25 read-only tools covering ad accounts, campaigns, creatives, performance analytics, demographics, video analytics, budget pacing, Lead Gen Forms, conversions, and targeting. v1.1.1 April 2026
- **danielpopamd/linkedin-ads-mcp** — access and analyze LinkedIn Ads data with Claude
- **radiateb2b/mcp-linkedin-ads** — performance analysis with benchmark comparisons and optimization recommendations
- **CDataSoftware/linkedin-ads-mcp-server-by-cdata** — read-only via CData JDBC Drivers

### TikTok Ads MCPs — New Category

TikTok Ads MCP servers emerged alongside the platform's growing ad business:

- **AdsMCP/tiktok-ads-mcp-server** (MIT) — OAuth authentication, campaign retrieval, ad group management, performance metrics
- **ysntony/tiktok-ads-mcp** — comprehensive TikTok Business API integration, campaign/ad group/ad management and reporting

### Other Ad Platform MCPs

- **brijr/meta-mcp** — full Meta Marketing API with creative optimization focus
- **google-marketing-solutions/google_ads_mcp** (183 stars) — v0.6.4, Python, Apache-2.0, still active
- **cohnen/mcp-google-ads** — natural language Google Ads analysis with Claude, Cursor, Windsurf
- **TrueClicks/google-ads-mcp-js** — easiest Google Ads setup, no developer tokens required
- **EfrainTorres/armavita-meta-ads-mcp** — Meta Marketing API v25 with secure token redaction
- **gomarble-ai/google-ads-mcp-server** — Google Ads performance data analysis
- **promobase/google-ads-mcp** — Google Ads API v20 with full type annotations

## Enterprise Marketing Automation

### Adobe Marketo Engage MCP — Closed Beta

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [Marketo MCP](https://experienceleague.adobe.com/en/docs/marketo-developer/marketo/mcp-server) | — | — | — | 100+ |

**Adobe launched its Marketo Engage MCP server in closed beta (April 2026)** — the first enterprise marketing automation platform with MCP:

- **100+ operations** — forms, programs, smart campaigns, leads, emails, snippets, lists, and folders
- **No server-side software needed** — executes REST API calls on your behalf via MCP
- **Enterprise AI integration** — works with Claude, Copilot, and other MCP-compatible systems
- **Campaign creation via prompts** — "Create a new smart campaign for my next webinar" replaces manual UI clicks

The biggest gap filler for enterprise marketing — Marketo was the most notable absence in our March review.

## SEO Tools

### AminForou/mcp-gsc — Most Popular SEO MCP

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [mcp-gsc](https://github.com/AminForou/mcp-gsc) | 748 | Python | MIT | 20 |

**The most-starred SEO MCP server** — surged from 512 to 748 stars (+46%) with significant improvements:

- **20 tools** (up from 5+) — comprehensive Google Search Console coverage
- **v0.3.2** (April 2026) — fixed OAuth browser flow for uvx, added `get_capabilities` tool
- **uvx installation** — no cloning, no Python setup, no virtual environments needed
- **Multi-client** — works with Claude Desktop, Cursor, Codex CLI, Gemini CLI, Antigravity
- **MIT licensed** — fully open source

The standard choice for SEO professionals. The 46% star growth confirms strong community demand.

### cnych/seo-mcp — Free Ahrefs-Based SEO Analysis

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [seo-mcp](https://github.com/cnych/seo-mcp) | 239 | Python | MIT | 4 |

**Free SEO tool based on Ahrefs data** — surged from 165 to 239 stars (+45%):

- **4 tools** — backlink analysis, keyword generation, traffic estimation, keyword difficulty
- **Automated CAPTCHA solving** — handles Ahrefs authentication automatically
- **Caching** — optimized for repeated queries
- **Free access** — uses Ahrefs data without requiring a paid account

Popular choice for SEO research without the cost of premium SEO tools.

### Skobyn/dataforseo-mcp-server — Comprehensive DataForSEO API

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [dataforseo-mcp-server](https://github.com/Skobyn/dataforseo-mcp-server) | 75 | TypeScript | MIT | 20+ |

**Full DataForSEO API access** — surged from 47 to 75 stars (+60%) with new capabilities:

- **SERP data** — search engine results page analysis
- **Keyword research** — volume, difficulty, and competition metrics
- **Local Falcon integration** — local ranking analysis and Google My Business search (new)
- **Tool filtering** — enable specific modules via environment variables to reduce context window usage
- **Zod type-safe** — built with TypeScript and Zod schemas

Requires a DataForSEO API subscription. Best for agencies and professionals needing programmatic SEO data.

### Other SEO MCPs

- **mrgoonie/seo-insights-mcp-server** — TypeScript-based, backlinks, keyword research, traffic analysis with CLI support
- **dataforseo/mcp-server-typescript** — official DataForSEO TypeScript MCP server
- **AminForou/google-search-console-mcp-v2** — updated version of the GSC MCP
- **egebese/seo-research-mcp** — free SEO research using Ahrefs data, optimized for AI-powered IDEs

## Social Media Management

### pascalporedda/typefully-mcp-server — Typefully Social Media Drafts

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [typefully-mcp-server](https://github.com/pascalporedda/typefully-mcp-server) | — | TypeScript | — | 5+ |

**Create social media content via AI and push to Typefully** for scheduling:

- **Multi-platform** — drafts for X (Twitter), LinkedIn, Bluesky, and Threads
- **Draft management** — create posts and push them to Typefully for review and scheduling
- **NPX compatible** — easy installation via npx
- **Claude Desktop integration** — designed for use with Claude Desktop

### tn819/buffer-mcp — Buffer Social Media Scheduling

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [buffer-mcp](https://github.com/tn819/buffer-mcp) | — | — | — | 5+ |

**Buffer integration for social media scheduling** — manage your Buffer posting queue through AI:

- **Post scheduling** — queue posts across social media platforms
- **Buffer API** — direct integration with Buffer's scheduling API

### Other Social Media MCPs

- **LokiMCPUniverse/hootsuite-mcp-server** — Hootsuite social media management integration
- **muhammedsamal/typefully-mcp** — alternative Typefully MCP for tweets, threads, and content management
- **pepuscz/typefully-mcp-server** — another Typefully API integration

## What's Missing

The marketing automation MCP ecosystem has narrowed its **gaps** significantly since March:

- **~~No unified marketing dashboard~~** — **CLOSING**: Synter Media covers 14 platforms, amekala/ads-mcp covers 4, but email+SEO+social still not unified
- **No A/B testing orchestrator** — individual platforms support A/B tests, but no MCP coordinates testing across channels
- **~~Limited cross-platform analytics~~** — **CLOSING**: cross-platform ad servers now aggregate performance data across platforms
- **No affiliate marketing MCP** — affiliate networks (ShareASale, CJ, Impact) are not covered
- **No influencer management** — no MCP for influencer discovery, outreach, or campaign tracking
- **~~Limited marketing automation workflows~~** — **CLOSING**: Marketo MCP in closed beta, HubSpot GA, ActiveCampaign official
- **No content calendar MCP** — no unified content planning tool across channels

## Bottom Line

The marketing automation MCP category **upgraded to 4.5/5** — driven by explosive growth across every sub-category. Ad platforms saw the biggest leap: Amazon Ads went official (open beta February 2026), Google Ads moved to googleads org with 404 stars, Meta Ads surged to 823 stars, and cross-platform solutions emerged from Synter and amekala. HubSpot's official MCP graduating to GA with write access is a CRM milestone. The Intuit/Anthropic multi-year partnership signals Mailchimp MCP is imminent. SEO tools saw 45-60% star growth across the board. Adobe Marketo's entry closes the enterprise marketing automation gap. The remaining weaknesses are affiliate marketing, influencer management, and a truly unified cross-channel content calendar — but the trajectory from March to April is the strongest improvement of any marketing category.

*This review was refreshed on 2026-04-28 using Claude Opus 4.6 (Anthropic). Previous version: 2026-03-16.*

