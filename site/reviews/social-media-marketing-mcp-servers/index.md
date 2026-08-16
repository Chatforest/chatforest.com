# Social Media & Marketing MCP Servers — Twitter/X, Bluesky, Instagram, LinkedIn, Meta Ads, Google Ads, SEO, and More

> Social media and marketing MCP servers are turning AI agents into social media managers, ad campaign operators, and SEO analysts — letting them post content, analyze engagement


Social media and marketing MCP servers are turning AI agents into social media managers, ad campaign operators, and SEO analysts. Instead of toggling between dashboards and scheduling tools, these servers let agents post content, analyze engagement, manage ad campaigns, track rankings, and coordinate multi-platform publishing — all through the Model Context Protocol.

The landscape spans six areas: **Twitter/X posting and analytics** (the most fragmented category with 10+ competing servers, now led by XActions at 451 stars), **Bluesky and decentralized social** (the AT Protocol's developer-friendly ecosystem), **Instagram and LinkedIn** (business-focused integrations via Graph API and community servers), **advertising and paid media** (Meta Ads dominates at 1.2k stars with 120+ releases), **SEO and content marketing** (Ahrefs moved to paid remote MCP, community scrapers persist), and **email marketing and scheduling** (Iterable's official 105-tool server plus new multi-platform scheduling entrants).

The headline findings: **TikTok launched an official Ads MCP server**, announced at [TikTok World '26](https://newsroom.tiktok.com/en-us/tiktok-world-26-turning-discovery-into-business-growth-with-ai-powered-innovations-vertical-experiences-and-high-impact-brand-solutions) (May 13, 2026) and publicly available since June 30, 2026 as [TikTok for Business MCP / Agentic Hub](https://ads.tiktok.com/business/en/blog/tiktok-agentic-hub-ai-agents-skills-mcp) — AI agents can create and manage ad campaigns, shift budgets, adjust targeting, and analyze creative performance via TikTok's Marketing API, accompanied by an AI Skills developer toolkit. **Meta Ads MCP remains the category leader** at [1.2k stars with 540 commits and 42 tools](https://github.com/pipeboard-co/meta-ads-mcp) — the most actively developed server in this category. **XActions is the new Twitter/X powerhouse** at [451 stars](https://github.com/nirholas/XActions) with 51+ MCP tools and no API fees, using browser automation to bypass the $100/month API barrier. **HubSpot MCP went GA** — the [remote CRM MCP server graduated from beta to GA on April 13, 2026](https://developers.hubspot.com/changelog/remote-hubspot-mcp-server-is-now-generally-available) with read+write access and marketing content objects. **Ahrefs [archived its local MCP server](https://github.com/ahrefs/ahrefs-mcp-server) on February 24, 2026** in favor of a paid remote server at api.ahrefs.com/mcp. **Multi-platform scheduling via MCP is now real** — PostPlanify, Publora, [Buffer](https://buffer.com/resources/buffer-api-is-here/), and [Oktopost](https://www.oktopost.com/blog/oktopost-mcp-server-ai-social-workflows/) all ship production MCP servers for AI-native social media management. **Twitter/X still has no official server**, but the community now offers 10+ alternatives with overlapping features.

**Category:** [Business & Productivity](/categories/business-productivity/)

## Twitter/X — Still Fragmented, But Deepening

### nirholas/XActions (NEW — Most Comprehensive)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [nirholas/XActions](https://github.com/nirholas/XActions) | 451 | JavaScript | Apache-2.0 | 51+ |

The biggest new entrant in this category. XActions is a complete X/Twitter automation toolkit that includes an MCP server alongside scrapers, CLI, and browser scripts. **51+ MCP tools** covering scraping, posting, engagement, analytics, streaming, and more — all **without API fees**. Uses browser automation instead of the official Twitter API, bypassing the $100/month Basic tier entirely.

This is a significant shift: the most popular Twitter MCP server is no longer the one with the simplest API wrapper, but the one that removes the API cost barrier entirely. The trade-off is reliability — browser automation can break when Twitter changes their frontend.

### DataWhisker/x-mcp-server (NEW — Most Polished API Server)

| Server | Stars | Language | Tools |
|--------|-------|----------|-------|
| [DataWhisker/x-mcp-server](https://github.com/DataWhisker/x-mcp-server) | 75 | TypeScript | 26 |

A well-designed X MCP server, now up to **26 tools** covering timelines, posting, searching, engagement (likes, retweets, bookmarks), user lookup, follower export, mentions, and lists. Designed for Claude Desktop and other MCP clients. More polished than EnesCinr's 2-tool server, though it still requires API credentials.

### EnesCinr/twitter-mcp (Previously Most Popular)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [EnesCinr/twitter-mcp](https://github.com/EnesCinr/twitter-mcp) | 402 | TypeScript | MIT | 2 |

*Correction (2026-08-16): stars are now 402, up from the 345 recorded in the prior audit — the earlier "dropped from 375" trend reversed.* Still the most starred pure-API Twitter MCP server, but its 2-tool simplicity (post_tweet, search_tweets) is increasingly outmatched. Requires Twitter API v2 credentials.

### taazkareem/twitter-mcp-server (Most Complete API Server)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [taazkareem/twitter-mcp-server](https://github.com/taazkareem/twitter-mcp-server) | 20 | TypeScript | MIT | 11 |

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

### cameronrye/atproto-mcp (51 Tools)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [cameronrye/atproto-mcp](https://github.com/cameronrye/atproto-mcp) | 8 | TypeScript | MIT | 51 |

Still the most ambitious social media MCP server across any platform. **51 tools** organized into categories:

- **Social operations** — create posts, like, repost, follow, unfollow
- **Data retrieval** — search posts, view profiles, access feeds, get followers
- **Content management** — upload media, delete posts, manage threads
- **List and moderation** — create/manage lists, moderation tools
- **Batch operations** — apply one action across up to 25 targets in a single call
- **Analytics and insights** — engagement metrics, follower analysis

Works in both authenticated (app-password) and unauthenticated modes; production-ready with Docker support. *Correction (2026-08-16): the prior version of this entry listed "real-time streaming from the AT Protocol firehose" and "OAuth management" as tool categories, and described the server as having Kubernetes readiness, Prometheus metrics, and Grafana dashboards. The [current README](https://github.com/cameronrye/atproto-mcp) explicitly states firehose streaming is **not** implemented ("a request/response tool cannot honestly expose a continuous stream"), that OAuth login is "on the roadmap but not yet functional" (app-password auth is the supported path today), and does not mention Kubernetes, Prometheus, or Grafana — those claims have been removed. Tool count and star count also corrected (57→51, 6→8).*

The low star count (8) still belies the server's depth — this remains the most comprehensive single-platform social server we've reviewed.

### semioz/bluesky-mcp (Official Repo Featured)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [semioz/bluesky-mcp](https://github.com/semioz/bluesky-mcp) | 7 | JavaScript | — | 11 |

Featured in the [official MCP server repository](https://github.com/modelcontextprotocol/servers). Covers the essentials: authentication, posts (create/get/list/delete), interactions (like/unlike/repost/unrepost), profile and timeline. Simpler than atproto-mcp but with official recognition.

**Why Bluesky matters for MCP:** The AT Protocol was built as an open, federated system — there are no API rate limit paywalls like Twitter's $100/month tier. Any developer can build on it freely, which explains why the tooling is already sophisticated despite Bluesky's smaller user base.

## Instagram — Now With 23-Tool Rewrite

### mcpware/instagram-mcp (NEW — TypeScript Rewrite)

| Server | Stars | Language | Tools |
|--------|-------|----------|-------|
| [mcpware/instagram-mcp](https://github.com/mcpware/instagram-mcp) | 29 | TypeScript | 23 |

A TypeScript rewrite of jlbadano/ig-mcp that expands coverage to **23 Graph API tools**: posts, comments, DMs, stories, hashtags, reels, carousels, and analytics. Install with `npx @mcpware/instagram-mcp`.

**Key limitations:** Business/Creator accounts only, long-lived tokens expire after 60 days, 200 API calls/hour, 25 posts/day, DMs require Advanced Access from Meta, hashtag search limited to 30 unique per 7 days.

### jlbadano/ig-mcp (Original)

| Server | Stars | Language | Tools |
|--------|-------|----------|-------|
| [jlbadano/ig-mcp](https://github.com/jlbadano/ig-mcp) | 174 | Python | 8 |

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
| [felipfr/linkedin-mcpserver](https://github.com/felipfr/linkedin-mcpserver) | Profile search, jobs, messaging | TypeScript |
| [eliasbiondo/linkedin-mcp-server](https://github.com/eliasbiondo/linkedin-mcp-server) | People/company/job search | Python |
| [Rayyan9477/linkedin_mcp](https://github.com/Rayyan9477/linkedin_mcp) | Job search, resume generation | — |
| [rugvedp/linkedin-mcp](https://github.com/rugvedp/linkedin-mcp) | Profile analysis, post management | Python |

*Correction (2026-08-16): adhikasp/mcp-linkedin, previously listed here, has been removed — the repository now returns 404 and no longer appears in the author's public repo list; it was likely deleted or made private.* LinkedIn still has no official MCP server. The community implementations face LinkedIn's heavily restricted API. Most servers focus on job searching, profile viewing, post management, and AI-powered resume/cover letter generation.

The Rayyan9477/linkedin_mcp server stands out for combining job search with AI-generated resumes and cover letters — turning the MCP server into a job application assistant.

## Multi-Platform Social & Video

### anaisbetts/mcp-youtube (Most Starred Video Server)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [anaisbetts/mcp-youtube](https://github.com/anaisbetts/mcp-youtube) | 540 | JavaScript | MIT | 1 |

Still does exactly one thing: **extract subtitles from YouTube videos** using yt-dlp. No API key required.

The massive gap remains — there's no comprehensive YouTube MCP server with upload, analytics, channel management, or comment moderation capabilities.

### TikTok Ads MCP Server — Official Platform Integration *(announced May 2026, launched June 2026)*

**TikTok's official MCP server was announced at [TikTok World '26](https://newsroom.tiktok.com/en-us/tiktok-world-26-turning-discovery-into-business-growth-with-ai-powered-innovations-vertical-experiences-and-high-impact-brand-solutions) (May 13, 2026) and became publicly available on June 30, 2026 as [TikTok for Business MCP, via the Agentic Hub marketplace](https://ads.tiktok.com/business/en/blog/tiktok-agentic-hub-ai-agents-skills-mcp):**

- **Campaign creation and management** — AI agents create, launch, and manage ad campaigns via TikTok's Marketing API
- **Budget management** — shift budgets across campaigns and ad groups without manual intervention
- **Targeting** — modify audience targeting parameters through conversational AI
- **Creative generation and optimization** — AI-powered creative analysis and generation
- **Performance analysis, diagnostics, and audience insights**
- **AI Skills** — a companion developer toolkit (branded "TikTok Ads Skills" at the May announcement) providing modular building blocks for custom ad agent workflows: campaign creation, performance insights, creative analysis, audience discovery, budget optimization
- **Partner-built Skills** — HubSpot, Wix, Constant Contact, WorkMagic, Innovid, Kochava, and others have published AI Skills on Agentic Hub; Constant Contact's are usable from any LLM client (ChatGPT, Claude, or TikTok's native AI), not locked to TikTok's own tooling

*Correction (2026-08-16): the prior version of this entry claimed "Google Analytics integration...supported at launch" and that the server is "compatible with Claude, ChatGPT...via TikTok Marketing API OAuth." Neither claim is supported by TikTok's own announcement or its June 30 Agentic Hub launch post — Claude/ChatGPT compatibility was actually a description of **Meta's** Ads MCP server in a secondary source, not TikTok's, and no primary source mentions Google Analytics. Both claims have been removed. The "bid optimization" bullet has been folded into "budget management," which is what TikTok's own materials describe; TikTok's announcement does not separately name bid adjustment as a capability. The unsourced "first official write-capable MCP server from TikTok" superlative has also been cut.* For a deeper dive into TikTok alongside Google, Meta, and Amazon, see our [Advertising & Ad-Tech MCP Servers](/reviews/advertising-ad-tech-mcp-servers/) category review.

### Seym0n/tiktok-mcp — Community Read-Only Server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [Seym0n/tiktok-mcp](https://github.com/Seym0n/tiktok-mcp) | 191 | TypeScript | MIT | 3 |

Still read-only with three tools (subtitle retrieval, post details, search). Predates the official TikTok Ads MCP. Useful for content analysis workflows that don't require ad management.

### Multi-Platform Scheduling Servers (NEW Category)

The biggest shift since our original review: **AI-native social media scheduling** is now a real product category with multiple production MCP servers.

| Server | Platforms | Key Feature |
|--------|-----------|-------------|
| **[PostPlanify](https://postplanify.com/mcp)** | 10 (IG, FB, X, LinkedIn, TikTok, YouTube, Threads, Pinterest, Bluesky, GBP) | 22-tool MCP server (posts, accounts, media, analytics, comments) for cross-platform scheduling from any MCP client |
| **[Publora](https://publora.com/)** | 10 (LinkedIn, X, IG, Threads, TikTok, YouTube, FB, Bluesky, Mastodon, Telegram) | 18 MCP tools; Pro plan from $2.99/mo per account, Premium from $5.99/mo per account (billed yearly) |
| **[Buffer MCP](https://buffer.com/resources/buffer-api-is-here/)** | Multiple | 10 tools on GraphQL API (public beta, Feb 2026), batch scheduling up to 25 posts |
| **[Oktopost](https://www.oktopost.com/blog/oktopost-mcp-server-ai-social-workflows/)** | B2B-focused | Launched early 2026 exclusively for B2B marketing teams; annual contracts from $8,000/yr |
| **[OpenTweet](https://opentweet.io/blog/best-mcp-servers-social-media-2026)** | Twitter/X | 12 tools covering full tweet lifecycle — drafting to publishing to analytics |

These servers represent a shift from "API wrapper" to "AI-native social media manager" — you describe what you want in chat and the AI calls the right tools.

### vanman2024/ayrshare-mcp (13 Platforms, One Server)

| Server | Stars | Language | Tools | Platforms |
|--------|-------|----------|-------|-----------|
| [vanman2024/ayrshare-mcp](https://github.com/vanman2024/ayrshare-mcp) | 2 | Python | 75+ | 13 |

Still the most ambitious multi-platform server: **75+ tools across 13 social networks**. Built on the Ayrshare paid API. Breadth is staggering but adoption remains minimal.

## Advertising & Paid Media

### pipeboard-co/meta-ads-mcp (Category Leader — Now 1.2k Stars)

| Server | Stars | Commits | Releases | Language | License | Tools |
|--------|-------|---------|----------|----------|---------|-------|
| [pipeboard-co/meta-ads-mcp](https://github.com/pipeboard-co/meta-ads-mcp) | 1.2k | 540+ | 120+ | Python | BSL 1.1 → Apache 2.0 (2029) | 42 |

*Correction (2026-08-16): stars up from the 819 recorded in the prior audit to **1.2k**; commits from 489+ to 540+; latest tagged release is v1.0.120 (previously cited as "133+ releases," which we could not re-confirm as an exact total — corrected to 120+ based on the current release tag); tool count from 26 to the README's current **42 tools**.* Now supports Streamable HTTP transport alongside stdio and is available as a cloud-hosted Remote MCP service. The most mature Meta Ads MCP server in the ecosystem.

**42 tools** — campaigns, ad sets, ads, creatives (including dynamic creative testing), image upload, insights, interest/behavior/demographic/geo targeting, and page management. Note: legacy objectives (BRAND_AWARENESS, LINK_CLICKS, CONVERSIONS, APP_INSTALLS) are no longer valid for new campaigns — use OUTCOME-based objectives.

### Adspirer (NEW — Unified Paid Media)

| Server | Platforms | Pricing |
|--------|-----------|---------|
| [Adspirer](https://www.adspirer.com/) | Google, Meta, LinkedIn, TikTok, Amazon, ChatGPT Ads | Free: 15 tasks/mo, Plus: $40/mo, Pro: $83/mo, Max: $167/mo, Enterprise: custom |

*Correction (2026-08-16): Adspirer now covers six ad platforms (added Amazon Ads and ChatGPT Ads since the prior audit) and current pricing is Free/$40/$83/$167 rather than the Free/$49/$99/$199 previously recorded.* A commercial entrant offering a **unified remote MCP server** for major ad platforms. No API keys or coding required — connect through OAuth. Works with Claude, ChatGPT, Cursor, Codex, and Windsurf. The emerging competitor to Pipeboard for teams running ads across multiple platforms.

### googleads/google-ads-mcp (Official — Read-Only by Design)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [googleads/google-ads-mcp](https://github.com/googleads/google-ads-mcp) | 861 | Python | Apache-2.0 | 2 |

*Correction (2026-08-16): the repo previously cited here, `google-marketing-solutions/google_ads_mcp`, has been [archived by its owner in favor of `googleads/google-ads-mcp`](https://github.com/google-marketing-solutions/google_ads_mcp_server) — the link above and the star count now point to the current official repo (861 stars), not the archived one (129 stars at the time of the prior audit).* The official Google Ads MCP server is **intentionally read-only**. It exposes just two tools: `list_accessible_customers` and `search` (raw GAQL queries). **Cannot modify bids, pause campaigns, or create assets** — mutations stay in the REST API. This is the safety model by design.

The underlying [Google Ads API](https://developers.google.com/google-ads/api/docs/release-notes) has since advanced to **v25** (released July 22, 2026); the v23.1 release (February 25, 2026) added programmatic control of AI-generated ad copy via `Campaign.text_guidelines`.

### amekala/ads-mcp (Cross-Platform Ads)

| Server | Stars | Language | License | Platforms |
|--------|-------|----------|---------|-----------|
| [amekala/ads-mcp](https://github.com/amekala/ads-mcp) | 83 | — | Proprietary | 6 |

*Correction (2026-08-16): the repo has grown substantially since the prior audit — stars from 19 to 83, and the README now advertises **400+ tools** across six platforms: Google Ads (151), Amazon Ads (61), Meta Ads (58), LinkedIn Ads (54), TikTok Ads (37), and ChatGPT Ads (31) — not the "100+ tools across 4 platforms" (Google 39, LinkedIn 28, Meta 20, TikTok 4) previously recorded here.* The proprietary license (see the repo's Terms of Service) limits adoption, but the cross-platform coverage is unique. Also available as the commercial Adspirer product (see above).

### Other Ad Servers

- **gomarble-ai/facebook-ads-mcp-server** — programmatic Facebook Ads access
- **attainmentlabs/meta-ads-mcp** — campaign creation and management
- **brijr/meta-mcp** — comprehensive Meta Marketing API
- **trypeggy/facebook-ads-library-mcp** — search Facebook's public Ads Library to see competitor ads (no ad account needed)

## SEO & Content Marketing

### cnych/seo-mcp (Free Ahrefs Data)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [cnych/seo-mcp](https://github.com/cnych/seo-mcp) | 255 | Python | MIT | 4 |

Stars up from the 225 recorded in the prior audit to 255. Still provides free access to Ahrefs data through four tools (backlinks, keyword generation, traffic estimation, keyword difficulty) via scraping with automatic CAPTCHA solving. The fragility caveat remains: this can break if Ahrefs changes their frontend.

### Ahrefs Remote MCP (Official — Paid, Local Server Archived)

The [local ahrefs-mcp-server repository](https://github.com/ahrefs/ahrefs-mcp-server) was **archived by Ahrefs on February 24, 2026** and is no longer maintained — the README states it "DOES NOT work with MCP keys," "IS NOT maintained," and is "OUTDATED." Ahrefs has fully transitioned to a [remote MCP server](https://ahrefs.com/mcp/) (see the [reference docs](https://docs.ahrefs.com/docs/mcp/reference/introduction)):

- **Streamable HTTP (recommended):** `https://api.ahrefs.com/mcp/mcp`
- **Legacy SSE (deprecated):** `https://api.ahrefs.com/mcp/mcpSse`

Requires **Ahrefs Lite plan or higher** — no free tier or trial. Covers rank tracking, keyword research, batch analysis, search volume data, and competitor insights. Zero local setup, works directly in AI tools.

### metehan777/semrush-mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [metehan777/semrush-mcp](https://github.com/metehan777/semrush-mcp) | 16 | TypeScript | MIT | 7 |

Semrush API integration with seven tools. Requires a Semrush API key (paid plans only).

## Email Marketing & CRM

### HubSpot MCP (Official — Now GA With Read+Write)

The biggest email/CRM update since our last review. **[HubSpot's remote MCP server graduated from beta to GA on April 13, 2026](https://developers.hubspot.com/changelog/remote-hubspot-mcp-server-is-now-generally-available)**, adding significant new capabilities:

- **Write access** to CRM objects: Contacts, Companies, Deals, Tickets, Line Items, Products, and Activity-type Engagements (Calls, Meetings, Notes, Tasks, Emails)
- **Read-only access** to marketing content: Campaigns, landing pages, website/site pages, blog posts, marketing events
- **Self-service MCP Auth Apps** — build and manage custom AI connectors to HubSpot MCP with OAuth 2.1 (with PKCE)

A separate **[Developer MCP Server (local) also went GA on February 19, 2026](https://developers.hubspot.com/changelog/hubspot-developer-mcp-server-for-app-and-cms-development-now-in-ga)** — download via HubSpot CLI for building HubSpot apps using natural language in Claude Code or Cursor.

HubSpot now combines CRM and marketing in a single MCP server with proper permissions, making it the most comprehensive official vendor MCP server in this category.

### Iterable/mcp-server (Official — Most Comprehensive Email)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [Iterable/mcp-server](https://github.com/Iterable/mcp-server) | 10 | TypeScript | MIT | 26–105 |

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
- **Meta Ads MCP** is now at 1.2k stars with 42 tools and 120+ releases — approaching enterprise maturity
- **HubSpot MCP** went GA with write access (remote CRM server, April 13, 2026) — the CRM+marketing gold standard
- **XActions** brought 51+ tools to Twitter/X without API fees
- **Instagram** got a 23-tool TypeScript rewrite
- **Multi-platform scheduling** is now a real category (PostPlanify, Publora, Buffer, Oktopost, OpenTweet)
- **Ahrefs** committed to remote MCP as its primary AI integration path, archiving its local server February 24, 2026

**What's changed since April 2026:**
- **TikTok now has an official Ads MCP server**, announced May 13, 2026 and publicly launched June 30, 2026 as TikTok for Business MCP / Agentic Hub — write-capable for ad campaigns

**What hasn't changed:**
- **Twitter/X** still has no official server (10+ community alternatives)
- **YouTube** (540 stars) still only extracts subtitles
- **TikTok organic posting** still unavailable — the official MCP is ad campaigns only
- **LinkedIn** still has no official server
- **Google Ads** is intentionally read-only

## What's Missing

- **Official Twitter/X MCP server** — the most fragmented category with no vendor support
- **YouTube upload and analytics** — the 540-star server only reads subtitles
- **TikTok organic posting** — the official TikTok MCP (May 2026) covers ad campaigns only; organic content creation and publishing via MCP remains unavailable
- **LinkedIn official server** — one of the largest professional networks with no official MCP support
- **Cross-platform analytics dashboard** — no server aggregates metrics across social platforms
- **Organic social scheduling with analytics** — new scheduling servers exist but analytics coverage is thin

## Rating: 3.5 / 5

The social media and marketing MCP space holds at **3.5/5** — the breadth continues to impress with 50+ servers covering every major platform and marketing channel, and the depth has genuinely improved in key areas. **TikTok's official Ads MCP server** (announced May 2026, publicly launched June 2026) closes a meaningful gap — AI agents can now create and manage TikTok ad campaigns without manual Ads Manager interaction, and its AI Skills toolkit makes it extensible for custom workflows. Meta Ads MCP at 1.2k stars with 120+ releases is approaching enterprise maturity, now available as a cloud-hosted Remote MCP service. HubSpot MCP going GA with read+write CRM access sets a new standard for vendor commitment. XActions' 51-tool, no-API-fee approach to Twitter/X is a creative solution to the API cost barrier. The emergence of multi-platform scheduling servers (PostPlanify, Publora, Buffer MCP) adds a practical new layer.

The deductions remain: **Twitter fragmentation** (10+ servers, no official one, API cost barrier driving browser automation workarounds), **YouTube's single-tool limitation** (most starred server only extracts subtitles — the biggest gap relative to platform importance), **TikTok organic posting still missing** (the official TikTok MCP covers ads only), **Google Ads is intentionally read-only**, and **LinkedIn's complete absence of official support**. The Ahrefs shift to paid-only remote MCP narrows free SEO tooling options.

For **social media managers**, the new multi-platform scheduling servers (PostPlanify, Publora) plus Buffer MCP provide genuine AI-native workflows. For **ad campaign managers**, Meta Ads MCP (Meta) and the new TikTok Ads MCP (TikTok) are the first-party choices; Adspirer and ads-mcp both now cover six ad platforms. For **SEO professionals**, Ahrefs remote MCP is the cleanest path if you have a paid plan; cnych/seo-mcp still works for free but is scraper-dependent. For **email marketers and CRM teams**, HubSpot GA + Iterable set the standard. The category would reach 4.0 when YouTube and LinkedIn join Google, Meta, Amazon, and TikTok with official write-capable MCP servers.

*This review was last edited on 2026-08-16 using Claude Sonnet 5 (Anthropic).*

