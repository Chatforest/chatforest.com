---
title: "Marketing Automation MCP Servers — Email Marketing, Ad Platforms, SEO, and Social Media Management"
date: 2026-03-16T15:00:00+09:00
description: "Marketing automation MCP servers let AI agents manage email campaigns, run ad platforms, analyze SEO data, and schedule social media posts. We reviewed 30+ servers across 5 subcategories. Email marketing: deyikong/sendgrid-mcp (21 stars, Python — 59 tools, read-only safety mode), Garoth/sendgrid-mcp (24 stars, Python — contact lists, templates, single sends), houtini-ai/brevo-mcp (Python — A/B testing, segmentation, campaign analytics), official MailerLite MCP (no API key needed, subscriber management). HubSpot CRM/marketing: peakmojo/mcp-hubspot (72 stars, Python — FAISS vector storage, caching, semantic search), shinzo-labs/hubspot-mcp (comprehensive API coverage), yespark/mcp-hubspot (40+ tools). Ad platforms: pipeboard-co/meta-ads-mcp (601 stars, Python — Facebook/Instagram campaign management), google-marketing-solutions/google_ads_mcp (official, Python — Google Ads API, read-only), cohnen/mcp-google-ads (natural language ad analysis). SEO: AminForou/mcp-gsc (512 stars, Python — Google Search Console), cnych/seo-mcp (165 stars — Ahrefs data, backlinks, keyword research), Skobyn/dataforseo-mcp-server (47 stars — comprehensive DataForSEO API). Social media: tn819/buffer-mcp (Buffer scheduling), pascalporedda/typefully-mcp-server (TypeScript — Typefully drafts for X/LinkedIn/Bluesky), LokiMCPUniverse/hootsuite-mcp-server (Hootsuite integration). Klaviyo: mattcoatsworth/Klaviyo-MCP-Server (profiles, campaigns, flows, segments). Gaps: no unified marketing dashboard MCP, no A/B testing orchestrator, limited analytics aggregation across platforms, no affiliate marketing MCP. 30+ servers across 5 subcategories. Rating: 4/5."
og_description: "Marketing automation MCP servers: pipeboard-co/meta-ads-mcp (601 stars — Meta Ads management), AminForou/mcp-gsc (512 stars — Google Search Console), peakmojo/mcp-hubspot (72 stars — HubSpot CRM), cnych/seo-mcp (165 stars — Ahrefs SEO). 30+ servers reviewed. Rating: 4/5."
content_type: "Review"
card_description: "Marketing automation MCP servers for AI-powered email campaigns, advertising management, SEO analysis, and social media scheduling. **Email marketing MCP servers cover the major platforms** — the core challenge of email marketing automation is managing campaigns, contacts, and templates across different providers. deyikong/sendgrid-mcp (21 stars, Python) leads the SendGrid ecosystem with 59 tools covering marketing automations, single send campaigns, contact management, and email statistics — running in read-only mode by default for safety. Garoth/sendgrid-mcp (24 stars, Python) provides a focused set of tools for contact lists, dynamic templates, single sends, and basic analytics. houtini-ai/brevo-mcp offers comprehensive Brevo integration with A/B testing, segmentation, and campaign management. MailerLite provides an official MCP server requiring no API keys — it handles subscriber management, campaign creation, and automation workflows directly. ActiveCampaign and Brevo both have official MCP servers available for Claude Desktop and Cursor integration. LokiMCPUniverse/mailchimp-mcp-server and bryangsmith/MailchimpMCP provide Mailchimp access with campaign management and automation control. **HubSpot has the richest CRM integration** — peakmojo/mcp-hubspot (72 stars, Python) goes beyond basic API access with FAISS vector storage for semantic search across previous interactions, SentenceTransformer embeddings with automatic caching, and duplicate prevention on contact creation. shinzo-labs/hubspot-mcp provides comprehensive API coverage. calypsoCodex/hubspot-mcp-extended offers 106 tools generated from HubSpot's official OpenAPI specs covering contacts, companies, deals, tickets, quotes, products, invoices, and line items. yespark/mcp-hubspot provides 40+ tools for CRM, marketing, and sales automation via REST API. The official HubSpot MCP Server is now in public beta at developers.hubspot.com/mcp. **Ad platform MCP servers are surprisingly mature** — pipeboard-co/meta-ads-mcp (601 stars, Python) is the most popular marketing MCP server overall, providing full campaign lifecycle management for Facebook and Instagram ads including campaign creation, budget updates, ad duplication, performance analytics, audience targeting, and creative optimization. It works with any MCP client. brijr/meta-mcp offers similar functionality with emphasis on creative optimization. google-marketing-solutions/google_ads_mcp is the official Google implementation — Python-based, Apache-2.0 licensed, currently read-only for diagnostics and analytics. cohnen/mcp-google-ads connects Google Ads with Claude AI for natural language campaign analysis. TrueClicks/google-ads-mcp-js is notable for not requiring developer tokens or OAuth credentials — easiest setup. **SEO tools have strong community adoption** — AminForou/mcp-gsc (512 stars, Python) is the most popular SEO MCP server, connecting Google Search Console to AI assistants for natural language SEO analysis including query performance, page analytics, and search appearance data. cnych/seo-mcp (165 stars) provides free SEO analysis based on Ahrefs data including backlink analysis, keyword research, and traffic estimation. Skobyn/dataforseo-mcp-server (47 stars) offers comprehensive DataForSEO API access for SERP data, keyword research, and competitor analysis. mrgoonie/seo-insights-mcp-server provides backlinks, keyword research, and traffic analysis with CLI support. **Social media management covers scheduling and posting** — pascalporedda/typefully-mcp-server (TypeScript) creates and manages drafts on Typefully for X, LinkedIn, Bluesky, and Threads. tn819/buffer-mcp handles Buffer social media scheduling. LokiMCPUniverse/hootsuite-mcp-server integrates with Hootsuite for social media management. mattcoatsworth/Klaviyo-MCP-Server provides comprehensive Klaviyo integration for profiles, lists, segments, campaigns, flows, templates, and catalogs — Klaviyo also offers an official MCP server at developers.klaviyo.com. **Gaps remain in cross-platform orchestration** — no MCP server provides a unified marketing dashboard aggregating data across email, ads, SEO, and social. No dedicated A/B testing orchestrator exists. Affiliate marketing, influencer management, and marketing attribution are not covered. The category would benefit from a 'marketing ops' MCP that connects campaign data across platforms for unified reporting."
---

Marketing automation MCP servers let AI agents manage email campaigns, run advertising platforms, analyze SEO data, and schedule social media content. Instead of switching between marketing dashboards, AI assistants can directly create campaigns, analyze performance, and optimize marketing workflows.

This review covers **marketing automation MCP servers** — email marketing platforms, CRM/marketing hubs, advertising platforms, SEO tools, and social media management. For related servers, see our [Social Media & Marketing review](/reviews/social-media-marketing-mcp-servers/), [E-Commerce & Shopping review](/reviews/ecommerce-shopping-mcp-servers/), and [Analytics & Business Intelligence review](/reviews/analytics-business-intelligence-mcp-servers/).

The headline findings: **Ad platform MCPs are surprisingly mature** — pipeboard-co/meta-ads-mcp has 601 stars and handles full campaign lifecycle management. **SEO tools have strong community adoption** with AminForou/mcp-gsc at 512 stars. **Email marketing platforms are well-covered** with official MCPs from MailerLite, Brevo, ActiveCampaign, and Klaviyo. **HubSpot has the richest CRM integration** with vector search and 106-tool comprehensive coverage.

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

Brevo also offers an official MCP server that connects directly from Claude Desktop and Cursor.

### MailerLite Official MCP — Zero-Config Email Marketing

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [MailerLite MCP](https://www.mailerlite.com/features/mcp) | — | — | — | — |

**Official MailerLite MCP server requiring no API keys** — the easiest email marketing MCP to set up:

- **No API key needed** — direct connection from AI tools to MailerLite
- **Subscriber management** — create and manage subscriber lists
- **Campaign creation** — build and send email campaigns via natural language
- **Automation workflows** — set up automated email sequences

Notable for being one of the few email marketing MCPs with an official, no-configuration setup path.

### Other Email Marketing MCPs

- **ActiveCampaign** — official MCP server available for Claude Desktop and Cursor integration
- **Klaviyo** — official MCP server at developers.klaviyo.com, plus mattcoatsworth/Klaviyo-MCP-Server (comprehensive profiles, lists, segments, campaigns, flows, templates, catalogs management)
- **Mailchimp** — LokiMCPUniverse/mailchimp-mcp-server (full API access), bryangsmith/MailchimpMCP (read-only campaign analytics and automation management), AgentX-ai/mailchimp-mcp (read-only)

## HubSpot CRM & Marketing

### peakmojo/mcp-hubspot — HubSpot with Vector Search

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [mcp-hubspot](https://github.com/peakmojo/mcp-hubspot) | 72 | Python | — | 10+ |

**The most-starred community HubSpot MCP** — goes beyond basic API access with intelligent caching:

- **FAISS vector storage** — semantic search across previously retrieved HubSpot data
- **SentenceTransformer embeddings** — automatic embedding caching and persistent storage
- **Duplicate prevention** — built-in deduplication when creating contacts and companies
- **Docker deployment** — simple containerized setup with minimal configuration

Best for teams with large HubSpot datasets who need fast, semantic access to CRM data.

### calypsoCodex/hubspot-mcp-extended — 106 Tools from OpenAPI Specs

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [hubspot-mcp-extended](https://github.com/calypsoCodex/hubspot-mcp-extended) | — | — | — | 106 |

**Most comprehensive HubSpot MCP** — 106 tools generated directly from HubSpot's official OpenAPI specifications:

- **Full CRM coverage** — contacts, companies, deals, tickets, quotes, products, invoices, line items
- **Auto-generated** — tools derived from official specs ensure complete API coverage
- **Public beta** — available for community testing and feedback

### Other HubSpot MCPs

- **Official HubSpot MCP Server** — now in public beta at developers.hubspot.com/mcp
- **shinzo-labs/hubspot-mcp** — comprehensive MCP implementation for HubSpot API
- **yespark/mcp-hubspot** — 40+ tools for CRM, marketing, and sales automation via REST API
- **lkm1developer/hubspot-mcp-server** — AI assistant integration for HubSpot CRM data

## Advertising Platforms

### pipeboard-co/meta-ads-mcp — Most Popular Marketing MCP Overall

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [meta-ads-mcp](https://github.com/pipeboard-co/meta-ads-mcp) | 601 | Python | — | 26+ |

**The most-starred marketing automation MCP server** — full campaign lifecycle management for Meta advertising:

- **Campaign management** — create campaigns, update budgets, duplicate ads across Facebook and Instagram
- **Performance analytics** — retrieve detailed performance data and strategic insights
- **Creative optimization** — visualize ad creatives, analyze performance by creative variant
- **Audience targeting** — manage audience segments and targeting parameters
- **Universal MCP client support** — works with Claude Desktop, Cursor, Cherry Studio, and more
- **OAuth authentication** — simple setup with Meta Business credentials

The go-to choice for Meta advertising automation. Community-maintained with 601 stars.

### brijr/meta-mcp — Full Meta Marketing API

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [meta-mcp](https://github.com/brijr/meta-mcp) | — | — | — | 20+ |

**Comprehensive Meta Marketing API coverage** with emphasis on creative optimization:

- **Full campaign lifecycle** — campaign management, analytics, audience targeting
- **Creative optimization** — tools for optimizing ad creatives across Meta platforms
- **Facebook + Instagram** — covers all Meta advertising platforms

### google-marketing-solutions/google_ads_mcp — Official Google Ads MCP

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [google_ads_mcp](https://github.com/google-marketing-solutions/google_ads_mcp) | — | Python | Apache-2.0 | 10+ |

**The official Google Ads MCP implementation** — enables LLMs to interact directly with the Google Ads API:

- **Official Google project** — maintained by Google Marketing Solutions (not an officially supported Google product)
- **Read-only** — designed for diagnostics and analytics, not campaign modification
- **Python 3.12** — uses uv for dependency management
- **Gemini integration** — listed in Gemini's MCP server directory
- **Apache-2.0 licensed** — open source with permissive licensing

Best for analytics and reporting. For campaign management, consider community alternatives.

### cohnen/mcp-google-ads — Natural Language Google Ads Analysis

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [mcp-google-ads](https://github.com/cohnen/mcp-google-ads) | — | — | — | 10+ |

**Natural language interface to Google Ads data** — analyze advertising data through conversation:

- **Campaign analysis** — access campaign information and performance metrics
- **Keyword analytics** — research keyword performance and opportunities
- **Ad management** — review and analyze ad creative performance
- **Multi-client** — works with Claude, Cursor, and Windsurf

### TrueClicks/google-ads-mcp-js — Easiest Google Ads Setup

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [google-ads-mcp-js](https://github.com/TrueClicks/google-ads-mcp-js) | — | JavaScript | — | 10+ |

**The easiest Google Ads MCP to set up** — no developer tokens or OAuth credentials required:

- **Zero credential setup** — unique among Google Ads MCPs for not requiring developer tokens
- **JavaScript/Node.js** — runs via npx for quick installation
- **PPC analysis** — designed for pay-per-click campaign analysis

### Other Ad Platform MCPs

- **EfrainTorres/armavita-meta-ads-mcp** — Meta Marketing API v25 with secure token redaction, cursor pagination
- **attainmentlabs/meta-ads-mcp** — create and manage Meta ad campaigns from Claude
- **gomarble-ai/google-ads-mcp-server** — Google Ads performance data analysis
- **promobase/google-ads-mcp** — Google Ads API v20 with full type annotations

## SEO Tools

### AminForou/mcp-gsc — Most Popular SEO MCP

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [mcp-gsc](https://github.com/AminForou/mcp-gsc) | 512 | Python | — | 5+ |

**The most-starred SEO MCP server** — connects Google Search Console to AI assistants:

- **Natural language SEO analysis** — query performance, page analytics, search appearance data
- **Google Search Console data** — direct access to GSC metrics and reports
- **Conversation-based** — analyze SEO data through natural language prompts
- **Claude integration** — designed specifically for Claude AI workflows

The standard choice for SEO professionals who want AI-assisted Search Console analysis.

### cnych/seo-mcp — Free Ahrefs-Based SEO Analysis

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [seo-mcp](https://github.com/cnych/seo-mcp) | 165 | — | — | 5+ |

**Free SEO tool based on Ahrefs data** — no Ahrefs subscription required:

- **Backlink analysis** — check backlink profiles for any domain
- **Keyword research** — discover keyword opportunities and search volumes
- **Traffic estimation** — estimate organic traffic for domains
- **Free access** — uses Ahrefs data without requiring a paid account

Popular choice for SEO research without the cost of premium SEO tools.

### Skobyn/dataforseo-mcp-server — Comprehensive DataForSEO API

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [dataforseo-mcp-server](https://github.com/Skobyn/dataforseo-mcp-server) | 47 | — | — | 20+ |

**Full DataForSEO API access** — comprehensive SEO data for professional use:

- **SERP data** — search engine results page analysis
- **Keyword research** — volume, difficulty, and competition metrics
- **Competitor analysis** — compare domain performance
- **Comprehensive API** — covers the full DataForSEO endpoint catalog

Requires a DataForSEO API subscription. Best for agencies and professionals needing programmatic SEO data.

### Other SEO MCPs

- **mrgoonie/seo-insights-mcp-server** — TypeScript-based, backlinks, keyword research, traffic analysis with CLI support
- **dataforseo/mcp-server-typescript** — official DataForSEO TypeScript MCP server
- **AminForou/google-search-console-mcp-v2** — updated version of the GSC MCP

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

The marketing automation MCP ecosystem has notable **gaps**:

- **No unified marketing dashboard** — no MCP aggregates data across email, ads, SEO, and social into a single interface
- **No A/B testing orchestrator** — individual platforms support A/B tests, but no MCP coordinates testing across channels
- **Limited cross-platform analytics** — no marketing attribution MCP connecting touchpoints across platforms
- **No affiliate marketing MCP** — affiliate networks (ShareASale, CJ, Impact) are not covered
- **No influencer management** — no MCP for influencer discovery, outreach, or campaign tracking
- **Limited marketing automation workflows** — platforms like Marketo, Pardot, and Marketing Cloud lack MCP servers
- **No content calendar MCP** — no unified content planning tool across channels

## Bottom Line

The marketing automation MCP category is **surprisingly strong at 4/5** — driven by high-quality ad platform MCPs (Meta Ads at 601 stars, official Google Ads), excellent SEO tooling (Google Search Console at 512 stars), and broad email marketing coverage with multiple official MCPs from major platforms. HubSpot's ecosystem is particularly rich with vector search capabilities and 106-tool comprehensive coverage. The main weakness is cross-platform orchestration — each platform has good individual MCPs, but no server ties them together for unified marketing operations. Social media management MCPs are functional but less mature than the ad and email categories.
