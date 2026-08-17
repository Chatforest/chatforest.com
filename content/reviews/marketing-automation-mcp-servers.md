---
title: "Marketing Automation MCP Servers — Email Marketing, Ad Platforms, SEO, and Social Media Management"
date: 2026-03-16T15:00:00+09:00
sources_audited: 2026-08-17
description: "Marketing automation MCP servers let AI agents manage email campaigns, run ad platforms, analyze SEO data, and schedule social media posts."
og_description: "Marketing automation MCP servers: pipeboard-co/meta-ads-mcp (1,180 stars — Meta Ads management), AminForou/mcp-gsc (1,367 stars — Google Search Console), googleads/google-ads-mcp (864 stars — official Google Ads), baryhuang/mcp-hubspot, formerly peakmojo/mcp-hubspot (128 stars — HubSpot CRM). Amazon Ads official MCP in open beta. 45+ servers reviewed. Rating: 4.5/5."
content_type: "Review"
card_description: "Marketing automation MCP servers for AI-powered email campaigns, advertising management, SEO analysis, and social media scheduling. **Ad platforms exploded with official support** — Amazon Ads launched its official MCP server in open beta (February 2026), joining Google's new googleads/google-ads-mcp (864 stars) as the second major ad platform to go official. pipeboard-co/meta-ads-mcp has grown to 1,180 stars, with Pipeboard CLI now supporting Meta + Google + TikTok from a single binary. Cross-platform gap is CLOSING: Synter Media AI covers 14 ad platforms for campaign creation (19 for reporting) with 140+ tools, amekala/ads-mcp provides 400+ tools across six platforms (Google/Meta/LinkedIn/TikTok/Amazon/ChatGPT Ads). NEW LinkedIn Ads MCP servers emerged (danielpopamd, radiateb2b, CData). NEW TikTok Ads MCP servers (AdsMCP, ysntony). **HubSpot went GA** — the official remote MCP server graduated from beta to GA (April 13, 2026) with write capabilities, engagement history, and marketing content objects. Developer MCP also GA with self-service MCP Auth Apps. The most-starred community HubSpot MCP (formerly peakmojo/mcp-hubspot, now baryhuang/mcp-hubspot) is at 128 stars. **Adobe Marketo Engage launched MCP** — 100+ operations across forms, programs, smart campaigns, leads, and emails (closed/limited beta April 2026). **Intuit and Anthropic announced multi-year partnership** — MCP integrations for Mailchimp, TurboTax, QuickBooks, and Credit Karma rolling out spring 2026. **Email marketing went fully official** — ActiveCampaign became first marketing platform in Claude's official directory with remote MCP (51 tools). MailerLite official MCP at mcp.mailerlite.com (70+ tools, no API key needed). Brevo official MCP at mcp.brevo.com. Klaviyo official MCP GA with Claude connector. **SEO tools surged** — AminForou/mcp-gsc now at 1,367 stars, v0.3.2, 20 tools, MIT, uvx install method. cnych/seo-mcp now at 255 stars. Skobyn/dataforseo-mcp-server now at 82 stars with Local Falcon integration. **Rating upgraded 4→4.5/5** — Amazon Ads official, Google Ads official growing fast, cross-platform solutions emerging, HubSpot GA, Intuit/Anthropic partnership, massive star growth."
last_refreshed: 2026-04-28
---

Marketing automation MCP servers let AI agents manage email campaigns, run advertising platforms, analyze SEO data, and schedule social media content. Instead of switching between marketing dashboards, AI assistants can directly create campaigns, analyze performance, and optimize marketing workflows. Part of our **[Business & Productivity MCP category](/categories/business-productivity/)**.

This review covers **marketing automation MCP servers** — email marketing platforms, CRM/marketing hubs, advertising platforms, SEO tools, and social media management. For related servers, see our [Social Media & Marketing review](/reviews/social-media-marketing-mcp-servers/), [E-Commerce & Shopping review](/reviews/ecommerce-shopping-mcp-servers/), and [Analytics & Business Intelligence review](/reviews/analytics-mcp-servers/).

The headline findings: **Ad platforms are now the most mature MCP category** — [Amazon Ads launched its official MCP](https://advertising.amazon.com/library/news/amazon-ads-mcp-server-open-beta) (February 2026), googleads/google-ads-mcp is now at 864 stars, and pipeboard-co/meta-ads-mcp has grown to 1,180 stars (all figures current as of this 2026-08-18 re-audit; see the star-count corrections in each section below for prior-audit values). **Cross-platform orchestration gap is closing** — Synter Media covers 14 ad platforms for campaign creation and 19 for reporting, amekala/ads-mcp now covers 6 platforms with 400+ tools. **[HubSpot official MCP went GA](https://developers.hubspot.com/changelog/remote-hubspot-mcp-server-is-now-generally-available)** with write access (April 13, 2026). **[Intuit and Anthropic announced a multi-year partnership](https://investors.intuit.com/news-events/press-releases/detail/1305/intuit-and-anthropic-partner-to-bring-trusted-financial-intelligence-and-custom-ai-agents-to-consumers-and-businesses)** bringing Mailchimp MCP integrations in spring 2026. **SEO tools continue to grow** — GSC now at 1,367 stars, Ahrefs-based seo-mcp at 255 stars.

## Email Marketing

### deyikong/sendgrid-mcp — Most Comprehensive SendGrid MCP

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [sendgrid-mcp](https://github.com/deyikong/sendgrid-mcp) | 3 | TypeScript | ISC | 59 |

**The most feature-complete SendGrid MCP server** — covers every aspect of email management and performance analysis:

- **59 tools** — marketing automations, single send campaigns, contact management, email statistics, and more
- **Read-only safety mode** — runs in read-only mode by default, with all mutable operations blocked at runtime
- **Marketing + transactional** — covers both marketing campaigns and transactional email operations
- **Analytics** — detailed performance analysis with engagement metrics

Good default choice for SendGrid users who want comprehensive API access with safety guardrails.

### Garoth/sendgrid-mcp — Focused SendGrid Marketing API

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [sendgrid-mcp](https://github.com/Garoth/sendgrid-mcp) | 29 | TypeScript | MIT | 10+ |

**Streamlined SendGrid marketing integration** — focuses on the most common email marketing operations:

- **Contact list management** — create, update, and organize contacts and lists
- **Dynamic templates** — generate and use SendGrid dynamic templates for personalized emails
- **Single sends** — create and send email campaigns to contact lists
- **Basic analytics** — retrieve sending statistics and validation information

Better choice when you want a simpler, more focused SendGrid integration without the full 59-tool surface.

### houtini-ai/brevo-mcp — Brevo Email Marketing Platform

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [brevo-mcp](https://github.com/houtini-ai/brevo-mcp) | 1 | JavaScript | MIT | 15+ |

**Comprehensive Brevo integration** with campaign management, analytics, and automation. **Note: this repo is now archived** (no longer actively maintained) as of this audit:

- **A/B testing** — create sophisticated email campaigns with A/B test variants
- **Segmentation** — target campaigns with contact segmentation
- **Campaign lifecycle** — create, update, and send test emails before launching
- **Multi-channel** — Brevo covers email and SMS marketing

Brevo now offers an **[official MCP server](https://developers.brevo.com/docs/mcp-protocol)** hosted at mcp.brevo.com — works with Claude Desktop, Cursor, Windsurf, VS Code, and more, per [Brevo's release notes](https://www.brevo.com/releases/new-release-brevos-mcp-server/). Community [BusyBee3333/brevo-mcp-2026-complete](https://github.com/BusyBee3333/brevo-mcp-2026-complete) provides 55+ tools and 14 interactive apps — given the archived status of houtini-ai/brevo-mcp above, the official server or this community fork are the better-maintained options.

### MailerLite Official MCP — Zero-Config Email Marketing

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [MailerLite MCP](https://www.mailerlite.com/features/mcp) | — | — | — | 70+ |

**Official MailerLite MCP server requiring no API keys** — the easiest email marketing MCP to set up:

- **No API key needed** — MailerLite's own page states ["no downloads, no code, and no API keys required"](https://www.mailerlite.com/features/mcp) for connecting AI tools to MailerLite at mcp.mailerlite.com
- **70+ tools** — per [MailerLite's developer docs](https://developers.mailerlite.com/mcp), covering subscriber, campaign, group, segment, field, form, automation, template, and e-commerce management (corrects this page's earlier "8 tools" figure, which understated the server's scope)
- **Remote MCP** — hosted server, no downloads or code required
- **Automation workflows** — set up automated email sequences

Notable for being one of the few email marketing MCPs with an official, no-configuration setup path.

### Other Email Marketing MCPs

- **ActiveCampaign** — official remote MCP server at mcp.activecampaign.com with [51 tools across 12 categories](https://developers.activecampaign.com/page/mcp-available-tools/#/) (contacts, deals/CRM, automations, campaigns, and more) — corrects this page's earlier "9 tools" figure. [ActiveCampaign states it is the first marketing platform in Claude's official connector directory](https://www.activecampaign.com/platform/ai-mcp). Works with all MCP-compatible AI tools
- **Klaviyo** — official MCP server (mcp.klaviyo.com) is [generally available](https://developers.klaviyo.com/en/docs/klaviyo_mcp_server) and [reads/writes campaigns, flows, and profiles](https://www.klaviyo.com/blog/agentic-marketing-workflows-with-klaviyo-anthropic-claude), available as a Claude connector (Settings > Connectors). Plus mattcoatsworth/Klaviyo-MCP-Server (comprehensive profiles, lists, segments, campaigns, flows, templates, catalogs management)
- **Mailchimp** — [**Intuit and Anthropic announced a multi-year partnership**](https://investors.intuit.com/news-events/press-releases/detail/1305/intuit-and-anthropic-partner-to-bring-trusted-financial-intelligence-and-custom-ai-agents-to-consumers-and-businesses) (February 24, 2026) bringing MCP integrations for Mailchimp, TurboTax, QuickBooks, and Credit Karma, rolling out to users in spring 2026 — confirmed on [Intuit's own partnership page](https://www.intuit.com/anthropic/). Community servers: LokiMCPUniverse/mailchimp-mcp-server (full API access), bryangsmith/MailchimpMCP (read-only campaign analytics), AgentX-ai/mailchimp-mcp (read-only)

## HubSpot CRM & Marketing

### HubSpot Official MCP — Now Generally Available

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [HubSpot MCP](https://developers.hubspot.com/mcp) | — | — | — | — |

**[The official HubSpot remote MCP server graduated from beta to GA on April 13, 2026](https://developers.hubspot.com/changelog/remote-hubspot-mcp-server-is-now-generally-available)** — the most significant CRM MCP milestone:

- **Write capabilities added** — read and write to your CRM through natural conversation (was read-only in beta)
- **Engagement history** — access contact and company engagement data
- **Marketing content objects** — manage marketing assets directly
- **Permission-aware** — respects existing HubSpot user permissions throughout
- **Developer MCP also GA** — build HubSpot apps using natural language via `hs mcp setup`
- **Self-service MCP Auth Apps** — build and manage your own AI connectors to HubSpot MCP

The definitive choice for HubSpot users. Remote MCP means no local setup required.

### baryhuang/mcp-hubspot (formerly peakmojo/mcp-hubspot) — HubSpot with Vector Search

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [mcp-hubspot](https://github.com/baryhuang/mcp-hubspot) | 128 | Python | — | 7 |

**The most-starred community HubSpot MCP** — the repo has since moved from the `peakmojo` account to `baryhuang` (same project, new owner handle) and now sits at 128 stars:

- **FAISS vector storage** — semantic search across previously retrieved HubSpot data
- **SentenceTransformer embeddings** — automatic embedding caching and persistent storage
- **Duplicate prevention** — built-in deduplication when creating contacts and companies
- **Docker deployment** — simple containerized setup with minimal configuration

Best for teams who want semantic search across CRM data — complements the official MCP with capabilities HubSpot's server doesn't offer.

### calypsoCodex/hubspot-mcp-extended — 106 Tools from OpenAPI Specs

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [hubspot-mcp-extended](https://github.com/calypsoCodex/hubspot-mcp-extended) | 1 | JavaScript | — | 106 |

**Most comprehensive HubSpot MCP** — 106 tools generated directly from HubSpot's official OpenAPI specifications:

- **Full CRM coverage** — contacts, companies, deals, tickets, quotes, products, invoices, line items
- **Auto-generated** — tools derived from official specs ensure complete API coverage
- **Public beta** — available for community testing and feedback

### Other HubSpot MCPs

- **[shinzo-labs/hubspot-mcp](https://github.com/shinzo-labs/hubspot-mcp)** — comprehensive MCP implementation for HubSpot API
- **[yespark/mcp-hubspot](https://github.com/yespark/mcp-hubspot)** — 40+ tools for CRM, marketing, and sales automation via REST API
- **[lkm1developer/hubspot-mcp-server](https://github.com/lkm1developer/hubspot-mcp-server)** — AI assistant integration for HubSpot CRM data

## Advertising Platforms

### pipeboard-co/meta-ads-mcp — Most Popular Marketing MCP Overall

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [meta-ads-mcp](https://github.com/pipeboard-co/meta-ads-mcp) | 1,180 | Python | BSL-1.1 | 25+ |

**The most-starred marketing automation MCP server** — now at 1,180 stars (up from 823 at last audit), with Pipeboard expanding beyond Meta:

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

**[Amazon Ads launched its official MCP server in open beta (February 2, 2026)](https://advertising.amazon.com/library/news/amazon-ads-mcp-server-open-beta)** — the biggest new entrant in ad platform MCPs, [reported by AdExchanger](https://www.adexchanger.com/marketers/amazon-ads-opens-a-beta-test-for-its-new-mcp-server/):

- **End-to-end campaign creation** — create campaigns, ad groups, and ads in a single workflow (previously 3+ separate operations)
- **Performance reporting** — pull reports and analytics through natural language
- **Budget optimization** — adjust bids and budgets across campaigns
- **Global availability** — available to all Amazon Ads partners with active API credentials
- **Multi-AI support** — works with Claude, ChatGPT, Gemini, Amazon Q, and others

The first official Amazon advertising MCP. Covered by [AdExchanger](https://www.adexchanger.com/marketers/amazon-ads-opens-a-beta-test-for-its-new-mcp-server/) and [Digiday](https://digiday.com/media-buying/ad-tech-briefing-amazon-launches-mcp-server-for-agent-driven-advertising/) — signals enterprise ad platform MCP adoption accelerating.

### googleads/google-ads-mcp — Official Google Ads MCP (New Home)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [google-ads-mcp](https://github.com/googleads/google-ads-mcp) | 864 | Python | Apache-2.0 | 3 tools + 4 resources |

**Google's official MCP server migrated to the googleads organization** — 864 stars, the authoritative Google Ads MCP:

- **3 core tools** — `search` (account info retrieval), `get_resource_metadata` (API structure), `list_accessible_customers` (customer IDs)
- **4 resources** — discovery document, metrics info, segments info, release notes
- **Actively maintained** — [most recent commit August 13, 2026](https://github.com/googleads/google-ads-mcp/commits/main); this page previously cited a "v0.6.4 / 9 releases" version history that does not match the repo's actual (empty) [releases page](https://github.com/googleads/google-ads-mcp/releases) and has been removed
- **Apache-2.0 licensed** — fully open source

Note: [google-marketing-solutions/google_ads_mcp_server has been archived](https://github.com/google-marketing-solutions/google_ads_mcp_server) in favor of this repo. This page previously also referenced a separate "google-marketing-solutions/google_ads_mcp" repo with 183 stars — that repo does not exist (404) and the claim has been removed.

### Cross-Platform Ad MCPs — The Gap Is Closing

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [ads-mcp](https://github.com/amekala/ads-mcp) | 83 | Multi | Proprietary | 400+ |

**Cross-platform ad management is emerging** — the biggest gap identified in our March review is now closing:

- **[amekala/ads-mcp](https://github.com/amekala/ads-mcp)** (83 stars) — has grown to 400+ tools across six platforms: Google Ads (151), Meta Ads (58), LinkedIn Ads (54), TikTok Ads (37), Amazon Ads (61), and ChatGPT Ads (31), per the repo's own README — well beyond the "175+ tools across 4 platforms" this page previously reported. Works with ChatGPT, Claude, Gemini CLI, Cursor, Codex, and Windsurf. Proprietary license (confirmed via repo's LICENSE section).
- **[Synter Media AI](https://github.com/Synter-Media-AI/mcp-server)** — per the vendor's own repo, 140+ tools with full campaign creation on 14 ad platforms and reporting across 19 (Google, Meta, LinkedIn, Microsoft, Reddit, TikTok, X, Snapchat, Pinterest, Amazon Ads/DSP, The Trade Desk, OpenAI Ads, and more). Commercial pricing is not independently confirmed as of this audit — vendor pages show conflicting figures ($199–$899/month across different pages) — so a specific price has been cut per this site's citation standard rather than guessed.
- **Pipeboard CLI** — supports Meta + Google + TikTok from a single binary alongside the meta-ads-mcp server.

### LinkedIn Ads MCPs — New Category

Multiple LinkedIn Ads MCP servers emerged since March 2026. Note: this page previously listed "ZLeventer/linkedin-campaign-manager-mcp" here — that repository could not be found on GitHub as of this audit (no such user/repo), so the claim has been removed rather than left unverifiable:

- **[danielpopamd/linkedin-ads-mcp](https://github.com/danielpopamd/linkedin-ads-mcp)** — access and analyze LinkedIn Ads data with Claude
- **[radiateb2b/mcp-linkedin-ads](https://github.com/radiateb2b/mcp-linkedin-ads)** — performance analysis with benchmark comparisons and optimization recommendations
- **[CDataSoftware/linkedin-ads-mcp-server-by-cdata](https://github.com/CDataSoftware/linkedin-ads-mcp-server-by-cdata)** — read-only via CData JDBC Drivers

### TikTok Ads MCPs — New Category

TikTok Ads MCP servers emerged alongside the platform's growing ad business:

- **[AdsMCP/tiktok-ads-mcp-server](https://github.com/AdsMCP/tiktok-ads-mcp-server)** (MIT) — OAuth authentication, campaign retrieval, ad group management, performance metrics
- **[ysntony/tiktok-ads-mcp](https://github.com/ysntony/tiktok-ads-mcp)** — comprehensive TikTok Business API integration, campaign/ad group/ad management and reporting

### Other Ad Platform MCPs

- **[brijr/meta-mcp](https://github.com/brijr/meta-mcp)** — full Meta Marketing API with creative optimization focus
- **[cohnen/mcp-google-ads](https://github.com/cohnen/mcp-google-ads)** — natural language Google Ads analysis with Claude, Cursor, Windsurf
- **[TrueClicks/google-ads-mcp-js](https://github.com/TrueClicks/google-ads-mcp-js)** — easiest Google Ads setup, no developer tokens required
- **[EfrainTorres/armavita-meta-ads-mcp](https://github.com/EfrainTorres/armavita-meta-ads-mcp)** — Meta Marketing API v25 with secure token redaction
- **[gomarble-ai/google-ads-mcp-server](https://github.com/gomarble-ai/google-ads-mcp-server)** — Google Ads performance data analysis
- **[promobase/google-ads-mcp](https://github.com/promobase/google-ads-mcp)** — Google Ads API v20 with full type annotations

## Enterprise Marketing Automation

### Adobe Marketo Engage MCP — Closed Beta

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [Marketo MCP](https://experienceleague.adobe.com/en/docs/marketo-developer/marketo/mcp-server) | — | — | — | 100+ |

**[Adobe launched its Marketo Engage MCP server in closed/limited beta (April 2026)](https://experienceleague.adobe.com/en/docs/marketo-developer/marketo/mcp-server)** — the first enterprise marketing automation platform with MCP, per [Adobe's own blog announcement](https://business.adobe.com/blog/connect-the-power-of-your-ai-tools-with-the-mcp-server-for-marketo-engage):

- **100+ operations** — forms, programs, smart campaigns, leads, emails, snippets, lists, and folders
- **No server-side software needed** — executes REST API calls on your behalf via MCP
- **Enterprise AI integration** — works with Claude, Copilot, and other MCP-compatible systems
- **Campaign creation via prompts** — "Create a new smart campaign for my next webinar" replaces manual UI clicks

The biggest gap filler for enterprise marketing — Marketo was the most notable absence in our March review.

## SEO Tools

### AminForou/mcp-gsc — Most Popular SEO MCP

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [mcp-gsc](https://github.com/AminForou/mcp-gsc) | 1,367 | Python | MIT | 20 |

**The most-starred SEO MCP server** — now at 1,367 stars (up from 748 at last audit) with significant improvements:

- **20 tools** (up from 5+) — comprehensive Google Search Console coverage
- **v0.3.2** (April 2026) — fixed OAuth browser flow for uvx, added `get_capabilities` tool
- **uvx installation** — no cloning, no Python setup, no virtual environments needed
- **Multi-client** — works with Claude Desktop, Cursor, Codex CLI, Gemini CLI, Antigravity
- **MIT licensed** — fully open source

The standard choice for SEO professionals. The 46% star growth confirms strong community demand.

### cnych/seo-mcp — Free Ahrefs-Based SEO Analysis

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [seo-mcp](https://github.com/cnych/seo-mcp) | 255 | Python | MIT | 4 |

**Free SEO tool based on Ahrefs data** — now at 255 stars (up from 239 at last audit):

- **4 tools** — backlink analysis, keyword generation, traffic estimation, keyword difficulty
- **Automated CAPTCHA solving** — handles Ahrefs authentication automatically
- **Caching** — optimized for repeated queries
- **Free access** — uses Ahrefs data without requiring a paid account

Popular choice for SEO research without the cost of premium SEO tools.

### Skobyn/dataforseo-mcp-server — Comprehensive DataForSEO API

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [dataforseo-mcp-server](https://github.com/Skobyn/dataforseo-mcp-server) | 82 | TypeScript | MIT | 20+ |

**Full DataForSEO API access** — now at 82 stars (up from 75 at last audit) with new capabilities:

- **SERP data** — search engine results page analysis
- **Keyword research** — volume, difficulty, and competition metrics
- **Local Falcon integration** — local ranking analysis and Google My Business search (new)
- **Tool filtering** — enable specific modules via environment variables to reduce context window usage
- **Zod type-safe** — built with TypeScript and Zod schemas

Requires a DataForSEO API subscription. Best for agencies and professionals needing programmatic SEO data.

### Other SEO MCPs

- **[mrgoonie/seo-insights-mcp-server](https://github.com/mrgoonie/seo-insights-mcp-server)** — TypeScript-based, backlinks, keyword research, traffic analysis with CLI support
- **[dataforseo/mcp-server-typescript](https://github.com/dataforseo/mcp-server-typescript)** — official DataForSEO TypeScript MCP server
- **[AminForou/google-search-console-mcp-v2](https://github.com/AminForou/google-search-console-mcp-v2)** — updated version of the GSC MCP
- **[egebese/seo-research-mcp](https://github.com/egebese/seo-research-mcp)** — free SEO research using Ahrefs data, optimized for AI-powered IDEs

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

- **[LokiMCPUniverse/hootsuite-mcp-server](https://github.com/LokiMCPUniverse/hootsuite-mcp-server)** — Hootsuite social media management integration
- **[muhammedsamal/typefully-mcp](https://github.com/muhammedsamal/typefully-mcp)** — alternative Typefully MCP for tweets, threads, and content management
- **[pepuscz/typefully-mcp-server](https://github.com/pepuscz/typefully-mcp-server)** — another Typefully API integration

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

The marketing automation MCP category **upgraded to 4.5/5** — driven by explosive growth across every sub-category. Ad platforms saw the biggest leap: Amazon Ads went official (open beta February 2026), Google Ads moved to the googleads org and has grown to 864 stars, Meta Ads has grown to 1,180 stars, and cross-platform solutions emerged from Synter and amekala. HubSpot's official MCP graduating to GA with write access is a CRM milestone. The Intuit/Anthropic multi-year partnership signals Mailchimp MCP is imminent. SEO tools have continued strong star growth across the board. Adobe Marketo's entry closes the enterprise marketing automation gap. The remaining weaknesses are affiliate marketing, influencer management, and a truly unified cross-channel content calendar — but the trajectory since the original March review remains the strongest improvement of any marketing category.

*This review was refreshed on 2026-04-28 using Claude Opus 4.6 (Anthropic). Previous version: 2026-03-16.*
