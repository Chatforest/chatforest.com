---
title: "Social Media & Marketing MCP Servers — Twitter/X, Bluesky, Instagram, LinkedIn, Meta Ads, Google Ads, SEO, and More"
date: 2026-03-15T09:55:00+09:00
description: "Social media and marketing MCP servers are turning AI agents into social media managers, ad campaign operators, and SEO analysts — letting them post content, analyze engagement"
og_description: "Social Media & Marketing MCP servers: XActions (203 stars, 51+ tools, no API fees — most comprehensive X/Twitter toolkit), pipeboard-co/meta-ads-mcp (791 stars, 489 commits, 133 releases — enterprise Meta Ads), DataWhisker/x-mcp-server (65 stars, 16 tools), mcpware/instagram-mcp (23 tools, TypeScript rewrite), cameronrye/atproto-mcp (57 tools for Bluesky/AT Protocol), google_ads_mcp (read-only GAQL, v23.1 API), cnych/seo-mcp (225 stars, Ahrefs scraper), Ahrefs remote MCP (mcp.ahrefs.com, paid Lite+), HubSpot MCP GA (read+write CRM, marketing content), Iterable (26-105 tools), Buffer MCP (10 tools, GraphQL API), PostPlanify/Publora multi-platform scheduling. 50+ servers reviewed. Rating: 3.5/5."
content_type: "Review"
card_description: "Social media and marketing MCP servers across posting, analytics, advertising, SEO, and email marketing. The landscape has matured significantly since March 2026: Meta Ads MCP hit 791 stars with 133 releases, XActions emerged as a 203-star no-API-fee Twitter toolkit with 51+ tools, HubSpot MCP went GA with read+write CRM access, Ahrefs moved to a paid remote MCP server at mcp.ahrefs.com, Google Ads MCP is officially read-only by design, and new multi-platform scheduling servers (PostPlanify, Publora, Buffer MCP) bring AI-native social management to every major platform. Instagram's mcpware rewrite delivers 23 Graph API tools. Twitter/X still has no official server but the community now offers 10+ alternatives."
last_refreshed: 2026-04-22
---

Social media and marketing MCP servers are turning AI agents into social media managers, ad campaign operators, and SEO analysts. Instead of toggling between dashboards and scheduling tools, these servers let agents post content, analyze engagement, manage ad campaigns, track rankings, and coordinate multi-platform publishing — all through the Model Context Protocol.

The landscape spans six areas: **Twitter/X posting and analytics** (the most fragmented category with 10+ competing servers, now led by XActions at 203 stars), **Bluesky and decentralized social** (the AT Protocol's developer-friendly ecosystem), **Instagram and LinkedIn** (business-focused integrations via Graph API and community servers), **advertising and paid media** (Meta Ads dominates at 791 stars with 133 releases), **SEO and content marketing** (Ahrefs moved to paid remote MCP, community scrapers persist), and **email marketing and scheduling** (Iterable's official 105-tool server plus new multi-platform scheduling entrants).

The headline findings: **Meta Ads MCP remains the category leader** at 791 stars with 489 commits and 133 releases — the most actively developed server in this category. **XActions is the new Twitter/X powerhouse** at 203 stars with 51+ MCP tools and no API fees, using browser automation to bypass the $100/month API barrier. **HubSpot MCP went GA** with read+write CRM access and marketing content objects. **Ahrefs killed its local MCP server** in favor of a paid remote server at api.ahrefs.com/mcp. **Multi-platform scheduling via MCP is now real** — PostPlanify, Publora, Buffer, and Oktopost all ship production MCP servers for AI-native social media management. **Twitter/X still has no official server**, but the community now offers 10+ alternatives with overlapping features.

**Category:** [Business & Productivity](/categories/business-productivity/)

## Twitter/X — Still Fragmented, But Deepening

### nirholas/XActions (NEW — Most Comprehensive)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [nirholas/XActions](https://github.com/nirholas/XActions) | 203 | JavaScript | Open Source | 51+ |

The biggest new entrant in this category. XActions is a complete X/Twitter automation toolkit that includes an MCP server alongside scrapers, CLI, and browser scripts. **51+ MCP tools** covering scraping, posting, engagement, analytics, streaming, and more — all **without API fees**. Uses browser automation instead of the official Twitter API, bypassing the $100/month Basic tier entirely.

This is a significant shift: the most popular Twitter MCP server is no longer the one with the simplest API wrapper, but the one that removes the API cost barrier entirely. The trade-off is reliability — browser automation can break when Twitter changes their frontend.

### DataWhisker/x-mcp-server (NEW — Most Polished API Server)

| Server | Stars | Language | Tools |
|--------|-------|----------|-------|
| [DataWhisker/x-mcp-server](https://github.com/DataWhisker/x-mcp-server) | 65 | — | 16 |

A well-designed X MCP server with **16 tools** covering timeline reading, post management (create/reply/quote/delete), engagement (like/unlike/retweet/bookmark), user lookup, search, and media upload (images and videos). Designed for Claude Desktop and other MCP clients. More polished than EnesCinr's 2-tool server, though it still requires API credentials.

### EnesCinr/twitter-mcp (Previously Most Popular)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [EnesCinr/twitter-mcp](https://github.com/EnesCinr/twitter-mcp) | 345 | TypeScript | MIT | 2 |

Stars dropped slightly from 375 to 345. Still the most starred pure-API Twitter MCP server, but its 2-tool simplicity (post_tweet, search_tweets) is increasingly outmatched. Last updated January 2026. Requires Twitter API v2 credentials.

### taazkareem/twitter-mcp-server (Most Complete API Server)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [taazkareem/twitter-mcp-server](https://github.com/taazkareem/twitter-mcp-server) | 19 | JavaScript | MIT | 11 |

The most feature-rich Twitter MCP server using the official API, with 11 tools across four categories:

- **Reading** — get_tweets, get_profile, search_tweets
- **Interaction** — like_tweet, retweet, post_tweet, create_thread
- **Timeline** — get_timeline, get_list_tweets, get_trends
- **User management** — get_user_relationships, follow_user

### Other Notable Twitter Servers

- **adhikasp/mcp-twikit** — uses the unofficial Twikit library to bypass the $100/month API Basic tier. Risk: unofficial API access can break or get accounts suspended
- **armatrix/x-twitter-mcp-server** (NEW, March 2026) — hybrid API architecture using twitterapi.io for cost-effective reads and official X API for writes
- **Infatoshi/x-mcp** (NEW) — gives AI agents the ability to post, search, read, and engage on X
- **crazyrabbitLTC/mcp-twitter-server** — professional workflow automation with enhanced error handling
- **0xGval/twitter-X-mcp-server** — lightweight Claude Desktop integration with advanced search operators
- **6551Team/opentwitter-mcp** — user profiles, tweet search, follower events, KOL tracking
- **miles0sage Twitter/X Playwright MCP** (NEW, March 2026) — reads tweets, posts, searches, and tracks trending topics via browser automation

The fragmentation has intensified: **Twitter still has no official MCP server**, and the community has now built at least **10+ alternatives**. The trend is moving away from the $100/month API toward browser automation (XActions, mcp-twikit, Playwright-based servers) and hybrid approaches (armatrix's split read/write architecture).

## Bluesky & AT Protocol — The Developer-Friendly Alternative

### cameronrye/atproto-mcp (57 Tools)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [cameronrye/atproto-mcp](https://github.com/cameronrye/atproto-mcp) | 6 | TypeScript | MIT | 57 |

Still the most ambitious social media MCP server across any platform. **57 tools** organized into categories:

- **Social operations** — create posts, like, repost, follow, unfollow
- **Data retrieval** — search posts, view profiles, access feeds, get followers
- **Content management** — upload media, delete posts, manage threads
- **List and moderation** — create/manage lists, moderation tools
- **Real-time streaming** — live data feeds from the AT Protocol firehose
- **Batch operations** — follow, like, or repost up to 25 items at once
- **Analytics and insights** — engagement metrics, follower analysis
- **OAuth management** — authentication handling

Works in both authenticated and unauthenticated modes. The AT Protocol's open architecture makes comprehensive tooling possible without API cost barriers. Production-ready with Docker support, Kubernetes readiness, Prometheus metrics, and Grafana dashboards.

The low star count (6) still belies the server's depth — this remains the most comprehensive single-platform social server we've reviewed.

### semioz/bluesky-mcp (Official Repo Featured)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [semioz/bluesky-mcp](https://github.com/semioz/bluesky-mcp) | 7 | JavaScript | — | 11 |

Featured in the official MCP server repository. Covers the essentials: authentication, posts (create/get/list/delete), interactions (like/unlike/repost/unrepost), profile and timeline. Simpler than atproto-mcp but with official recognition.

**Why Bluesky matters for MCP:** The AT Protocol was built as an open, federated system — there are no API rate limit paywalls like Twitter's $100/month tier. Any developer can build on it freely, which explains why the tooling is already sophisticated despite Bluesky's smaller user base.

## Instagram — Now With 23-Tool Rewrite

### mcpware/instagram-mcp (NEW — TypeScript Rewrite)

| Server | Stars | Language | Tools |
|--------|-------|----------|-------|
| [mcpware/instagram-mcp](https://github.com/mcpware/instagram-mcp) | — | TypeScript | 23 |

A TypeScript rewrite of jlbadano/ig-mcp that expands coverage to **23 Graph API tools**: posts, comments, DMs, stories, hashtags, reels, carousels, and analytics. Install with `npx @mcpware/instagram-mcp`.

**Key limitations:** Business/Creator accounts only, long-lived tokens expire after 60 days, 200 API calls/hour, 25 posts/day, DMs require Advanced Access from Meta, hashtag search limited to 30 unique per 7 days.

### jlbadano/ig-mcp (Original)

| Server | Stars | Language | Tools |
|--------|-------|----------|-------|
| [jlbadano/ig-mcp](https://github.com/jlbadano/ig-mcp) | 88 | Python | 8 |

Still the most starred Instagram MCP server, built on the Graph API for Business accounts. Eight tools covering profile retrieval, media management, engagement analytics, page management, and direct messaging. The mcpware TypeScript rewrite above extends this foundation significantly.

### Other Instagram Servers

- **arjun1194/insta-mcp** (NEW) — Instagram analytics, insights, and account management
- **Bob-lance/instagram-engagement-mcp** — engagement tracking, demographic insights, lead generation
- **anand-kamble/mcp-instagram** — profiles, timelines, stories, smart engagement
- **CDataSoftware/instagram-mcp-server-by-cdata** — read-only via CData JDBC Drivers
- **taskmaster-ai/insta-mcp** (NEW) — another Instagram MCP server entrant
- **trypeggy/instagram_dm_mcp** — focused specifically on Direct Message sending

## LinkedIn

| Server | Focus | Language |
|--------|-------|----------|
| [adhikasp/mcp-linkedin](https://github.com/adhikasp/mcp-linkedin) | Feeds & Job API | Python |
| [felipfr/linkedin-mcpserver](https://github.com/felipfr/linkedin-mcpserver) | Profile search, jobs, messaging | Python |
| [eliasbiondo/linkedin-mcp-server](https://github.com/eliasbiondo/linkedin-mcp-server) | People/company/job search | — |
| [Rayyan9477/linkedin_mcp](https://github.com/Rayyan9477/linkedin_mcp) | Job search, resume generation | — |
| [rugvedp/linkedin-mcp](https://github.com/rugvedp/linkedin-mcp) | Profile analysis, post management | — |

LinkedIn still has no official MCP server. The community implementations face LinkedIn's heavily restricted API. Most servers focus on job searching, profile viewing, post management, and AI-powered resume/cover letter generation.

The Rayyan9477/linkedin_mcp server stands out for combining job search with AI-generated resumes and cover letters — turning the MCP server into a job application assistant.

## Multi-Platform Social & Video

### anaisbetts/mcp-youtube (Most Starred Video Server)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [anaisbetts/mcp-youtube](https://github.com/anaisbetts/mcp-youtube) | 503 | JavaScript | MIT | 1 |

Still does exactly one thing: **extract subtitles from YouTube videos** using yt-dlp. Last updated February 2026 with improvements to strip non-text content (timestamps), enabling longer videos. No API key required.

The massive gap remains — there's no comprehensive YouTube MCP server with upload, analytics, channel management, or comment moderation capabilities.

### Seym0n/tiktok-mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [Seym0n/tiktok-mcp](https://github.com/Seym0n/tiktok-mcp) | ~148 | JavaScript | MIT | 3 |

Stars up from 137 to ~148. Still read-only with three tools (subtitle retrieval, post details, search). No posting or account management.

### Multi-Platform Scheduling Servers (NEW Category)

The biggest shift since our original review: **AI-native social media scheduling** is now a real product category with multiple production MCP servers.

| Server | Platforms | Key Feature |
|--------|-----------|-------------|
| **PostPlanify** | 10 (IG, FB, X, LinkedIn, TikTok, YouTube, Threads, Pinterest, Bluesky, GBP) | create_post tool for cross-platform scheduling from any MCP client |
| **Publora** | 10-12 (LinkedIn, X, IG, Threads, TikTok, YouTube, FB, Bluesky, Mastodon, Telegram) | Budget-friendly ($5.40/mo), clean MCP tool surface, LinkedIn analytics |
| **Buffer MCP** | Multiple | 10 tools on GraphQL API (public beta Feb 2026), batch scheduling up to 25 posts |
| **Oktopost** | B2B-focused | Launched early 2026 exclusively for B2B marketing teams |
| **OpenTweet** | Twitter/X | 12 tools covering full tweet lifecycle — drafting to publishing to analytics |

These servers represent a shift from "API wrapper" to "AI-native social media manager" — you describe what you want in chat and the AI calls the right tools.

### vanman2024/ayrshare-mcp (13 Platforms, One Server)

| Server | Stars | Language | Tools | Platforms |
|--------|-------|----------|-------|-----------|
| [vanman2024/ayrshare-mcp](https://github.com/vanman2024/ayrshare-mcp) | 1 | Python | 75+ | 13 |

Still the most ambitious multi-platform server: **75+ tools across 13 social networks**. Built on the Ayrshare paid API. Breadth is staggering but adoption remains minimal.

## Advertising & Paid Media

### pipeboard-co/meta-ads-mcp (Category Leader — Now 791 Stars)

| Server | Stars | Commits | Releases | Language | License | Tools |
|--------|-------|---------|----------|----------|---------|-------|
| [pipeboard-co/meta-ads-mcp](https://github.com/pipeboard-co/meta-ads-mcp) | 791 | 489 | 133 | Python | BSL 1.1 → Apache 2.0 (2029) | 26 |

Stars up from 628 to **791** (+26%). Commits up from unknown to **489** on main. **133 releases** — extraordinary for a single-platform MCP. Now supports Streamable HTTP transport alongside stdio. The most mature Meta Ads MCP server in the ecosystem.

**26 tools** covering account/campaign management, creative operations, performance analytics, targeting, budget management, and OAuth. Note: legacy objectives (BRAND_AWARENESS, LINK_CLICKS, CONVERSIONS, APP_INSTALLS) are no longer valid for new campaigns — use OUTCOME-based objectives.

### Adspirer (NEW — Unified Paid Media)

| Server | Platforms | Pricing |
|--------|-----------|---------|
| [Adspirer](https://www.adspirer.com/) | Google, Meta, LinkedIn, TikTok | Free: 15 calls/mo, Plus: $49/mo, Pro: $99/mo, Max: $199/mo |

A new commercial entrant offering a **unified remote MCP server** for all four major ad platforms. No API keys or coding required — connect through OAuth. Works with Claude, ChatGPT, Cursor, Codex, and Windsurf. The emerging competitor to Pipeboard for teams running ads across multiple platforms.

### google-marketing-solutions/google_ads_mcp (Official — Read-Only by Design)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [google-marketing-solutions/google_ads_mcp](https://github.com/google-marketing-solutions/google_ads_mcp) | 129 | Python | Apache-2.0 | 2 |

Important clarification since our last review: the official Google Ads MCP server is **intentionally read-only**. It exposes just two tools: `list_accessible_customers` and `search` (raw GAQL queries). **Cannot modify bids, pause campaigns, or create assets** — mutations stay in the REST API. This is the safety model by design.

Now runs on Google Ads API v23.1 (February 25, 2026), which adds programmatic control of AI-generated ad copy via Campaign.text_guidelines. Discord discussion on v24 features planned for April 23.

A separate repo at **googleads/google-ads-mcp** provides an alternative local implementation.

### amekala/ads-mcp (Cross-Platform Ads)

| Server | Stars | Language | License | Platforms |
|--------|-------|----------|---------|-----------|
| [amekala/ads-mcp](https://github.com/amekala/ads-mcp) | 19 | Shell | Proprietary | 4 |

**100+ tools** across Google Ads (39), LinkedIn Ads (28), Meta Ads (20), and TikTok Ads (4). The proprietary license limits adoption, but the cross-platform coverage is unique. Also available as the commercial Adspirer product (see above).

### Other Ad Servers

- **gomarble-ai/facebook-ads-mcp-server** — programmatic Facebook Ads access
- **attainmentlabs/meta-ads-mcp** — campaign creation and management
- **brijr/meta-mcp** — comprehensive Meta Marketing API
- **trypeggy/facebook-ads-library-mcp** — search Facebook's public Ads Library to see competitor ads (no ad account needed)

## SEO & Content Marketing

### cnych/seo-mcp (Free Ahrefs Data — Updated April 2026)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [cnych/seo-mcp](https://github.com/cnych/seo-mcp) | 225 | Python | MIT | 4 |

Stars up slightly from 224 to 225. Last updated **April 13, 2026** — actively maintained. Still provides free access to Ahrefs data through four tools (backlinks, keyword generation, traffic estimation, keyword difficulty) via scraping with automatic CAPTCHA solving. The fragility caveat remains: this can break if Ahrefs changes their frontend.

### Ahrefs Remote MCP (Official — Paid, Local Server Archived)

The local ahrefs-mcp-server repository is now **officially deprecated and not recommended**. Ahrefs has fully transitioned to a remote MCP server:

- **Streamable HTTP (recommended):** `https://api.ahrefs.com/mcp/mcp`
- **Legacy SSE (deprecated):** `https://api.ahrefs.com/mcp/mcpSse`

Requires **Ahrefs Lite plan or higher** — no free tier or trial. Covers rank tracking, keyword research, batch analysis, search volume data, and competitor insights. Zero local setup, works directly in AI tools.

### metehan777/semrush-mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [metehan777/semrush-mcp](https://github.com/metehan777/semrush-mcp) | 12 | TypeScript | MIT | 7 |

Semrush API integration with seven tools. Requires a Semrush API key (paid plans only).

## Email Marketing & CRM

### HubSpot MCP (Official — Now GA With Read+Write)

The biggest email/CRM update since our last review. **HubSpot's remote MCP server graduated from beta to GA**, adding significant new capabilities:

- **Write access** to CRM objects: Contacts, Companies, Deals, Tickets, Line Items, Products, and all Engagement types (Calls, Meetings, Notes, Tasks, Emails)
- **Read-only access** to marketing content: Campaigns, landing pages, website pages, blog posts
- **Self-service MCP Auth Apps** — build and manage custom AI connectors to HubSpot MCP with OAuth 2.1

A separate **Developer MCP Server (local)** also went GA on February 19, 2026 — download via HubSpot CLI for building HubSpot apps using natural language in Claude Code or Cursor.

HubSpot now combines CRM and marketing in a single MCP server with proper permissions, making it the most comprehensive official vendor MCP server in this category.

### Iterable/mcp-server (Official — Most Comprehensive Email)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [Iterable/mcp-server](https://github.com/Iterable/mcp-server) | 3 | TypeScript | MIT | 26–105 |

Still the standout email marketing server with tiered permissions from 26 tools (read-only) to **105 tools** (full access with PII, writes, and sends). Iterable describes MCP as part of their "Agentic Marketing Suite" — natural language prompts generate templates, localized content, variants, and journey steps using live customer and performance signals.

### Mailchimp Servers

- **AgentX-ai/mailchimp-mcp** — TypeScript, MIT, read-only access. Safe for exploration
- **LokiMCPUniverse/mailchimp-mcp-server** — Python, comprehensive with rate limiting and retry logic
- **mattcoatsworth/mailchip-mcp-server** — campaigns, lists, templates, reports, automations

### Social Media Management Platforms

- **LokiMCPUniverse/hootsuite-mcp-server** — Python, Hootsuite API integration with async support
- **tn819/buffer-mcp** — Buffer scheduling integration
- **jakemeany523/buffer-mcp** (NEW) — Buffer GraphQL API, 10 tools, batch scheduling up to 25 posts

## The Pattern: Breadth With Deepening Pockets

The social media and marketing MCP ecosystem remains the broadest we've reviewed. Since March 2026, the pattern has shifted: while most individual platform servers are still thin, **commercial multi-platform servers** and **vendor-backed official servers** are filling the depth gap.

**What's deepened:**
- **Meta Ads MCP** went from 628 to 791 stars with 133 releases — approaching enterprise maturity
- **HubSpot MCP** went GA with write access — the CRM+marketing gold standard
- **XActions** brought 51+ tools to Twitter/X without API fees
- **Instagram** got a 23-tool TypeScript rewrite
- **Multi-platform scheduling** is now a real category (PostPlanify, Publora, Buffer, Oktopost, OpenTweet)
- **Ahrefs** committed to remote MCP as its primary AI integration path

**What hasn't changed:**
- **Twitter/X** still has no official server (10+ community alternatives)
- **YouTube** (503 stars) still only extracts subtitles
- **TikTok** is still read-only
- **LinkedIn** still has no official server
- **Google Ads** is intentionally read-only

## What's Missing

- **Official Twitter/X MCP server** — the most fragmented category with no vendor support
- **YouTube upload and analytics** — the 503-star server only reads subtitles
- **TikTok posting** — only read-only analysis available
- **LinkedIn official server** — one of the largest professional networks with no official MCP support
- **Cross-platform analytics dashboard** — no server aggregates metrics across social platforms
- **Organic social scheduling with analytics** — new scheduling servers exist but analytics coverage is thin

## Rating: 3.5 / 5

The social media and marketing MCP space holds at **3.5/5** — the breadth continues to impress with 50+ servers covering every major platform and marketing channel, and the depth has genuinely improved in key areas. Meta Ads MCP at 791 stars with 133 releases is approaching enterprise maturity. HubSpot MCP going GA with read+write CRM access sets a new standard for vendor commitment. XActions' 51-tool, no-API-fee approach to Twitter/X is a creative solution to the API cost barrier. The emergence of multi-platform scheduling servers (PostPlanify, Publora, Buffer MCP) adds a practical new layer.

The deductions remain: **Twitter fragmentation** (10+ servers, no official one, API cost barrier driving browser automation workarounds), **YouTube's single-tool limitation** (most starred server only extracts subtitles — the biggest gap relative to platform importance), **read-only video platforms** (no posting to YouTube or TikTok), **Google Ads is intentionally read-only**, and **LinkedIn's complete absence of official support**. The Ahrefs shift to paid-only remote MCP narrows free SEO tooling options.

For **social media managers**, the new multi-platform scheduling servers (PostPlanify, Publora) plus Buffer MCP provide genuine AI-native workflows. For **ad campaign managers**, Meta Ads MCP is enterprise-ready and Adspirer offers unified cross-platform coverage. For **SEO professionals**, Ahrefs remote MCP is the cleanest path if you have a paid plan; cnych/seo-mcp still works for free but is scraper-dependent. For **email marketers and CRM teams**, HubSpot GA + Iterable set the standard. The category would jump to 4.0 if YouTube, TikTok, and LinkedIn provided official MCP servers with write capabilities.

*This review was last edited on 2026-04-22 using Claude Opus 4.6 (Anthropic).*
