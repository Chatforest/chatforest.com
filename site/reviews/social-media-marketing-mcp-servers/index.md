# Social Media & Marketing MCP Servers — Twitter/X, Bluesky, Instagram, LinkedIn, Meta Ads, Google Ads, SEO, and More

> Social media and marketing MCP servers are turning AI agents into social media managers, ad campaign operators, and SEO analysts — letting them post content, analyze engagement


Social media and marketing MCP servers are turning AI agents into social media managers, ad campaign operators, and SEO analysts. Instead of toggling between dashboards and scheduling tools, these servers let agents post content, analyze engagement, manage ad campaigns, track rankings, and coordinate multi-platform publishing — all through the Model Context Protocol.

The landscape spans six areas: **Twitter/X posting and analytics** (the most fragmented category with 8+ competing servers), **Bluesky and decentralized social** (the AT Protocol's developer-friendly ecosystem), **Instagram and LinkedIn** (business-focused integrations via Graph API and community servers), **advertising and paid media** (Meta Ads dominates with professional-grade campaign tools), **SEO and content marketing** (Ahrefs and Semrush integrations), and **email marketing** (Iterable's official 105-tool server).

The headline findings: **Meta Ads MCP is the most comprehensive server in this category** at 628 stars with 26 tools covering the full ad campaign lifecycle. **Twitter/X has the most community servers but no official one** — at least 8 implementations with overlapping features and API cost barriers. **Bluesky's atproto-mcp packs 57 tools** for the entire AT Protocol ecosystem, outpacing every other single-platform social server. **YouTube's most popular MCP server only extracts subtitles** — no upload, analytics, or channel management. **SEO tooling relies on scrapers** rather than official API integrations. **Iterable is the standout in email marketing** with up to 105 tools and official vendor support.

**Category:** [Business & Productivity](/categories/business-productivity/)

## Twitter/X — The Most Crowded Category

### EnesCinr/twitter-mcp (Most Popular)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [EnesCinr/twitter-mcp](https://github.com/EnesCinr/twitter-mcp) | 375 | TypeScript | MIT | 2 |

The most starred Twitter MCP server keeps it simple — two tools: `post_tweet` and `search_tweets`. That's enough for the most common use cases (posting updates and monitoring mentions), which likely explains its popularity. Requires Twitter API v2 credentials.

### vidhupv/x-mcp (Draft Workflow)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [vidhupv/x-mcp](https://github.com/vidhupv/x-mcp) | 61 | Python | MIT | 5 |

Takes a different approach — instead of posting directly, x-mcp emphasizes a **draft workflow**. Create tweets and threads, save them as drafts, review, then publish when ready. This mirrors how professional social media managers work: compose first, publish later. Five tools cover tweet creation, thread composition, draft viewing, draft publishing, and draft deletion.

### taazkareem/twitter-mcp-server (Most Complete)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [taazkareem/twitter-mcp-server](https://github.com/taazkareem/twitter-mcp-server) | 19 | JavaScript | MIT | 11 |

The most feature-rich Twitter MCP server with 11 tools across four categories:

- **Reading** — get_tweets, get_profile, search_tweets
- **Interaction** — like_tweet, retweet, post_tweet, create_thread
- **Timeline** — get_timeline, get_list_tweets, get_trends
- **User management** — get_user_relationships, follow_user

If you need comprehensive Twitter automation, this is the most capable option despite lower star count.

### Other Notable Twitter Servers

- **adhikasp/mcp-twikit** — uses the unofficial Twikit library to bypass the $100/month API Basic tier, accessing Twitter without developer credentials. Risk: unofficial API access can break or get accounts suspended
- **crazyrabbitLTC/mcp-twitter-server** — professional workflow automation with enhanced error handling and real-time documentation
- **0xGval/twitter-X-mcp-server** — lightweight Claude Desktop integration with advanced search operators (user filters, date ranges, engagement metrics)
- **lord-dubious/x-mcp** — bridging Twitter and AI with MCP
- **6551Team/opentwitter-mcp** — user profiles, tweet search, follower events, KOL tracking

The fragmentation tells a story: **Twitter has no official MCP server**, so the community built at least 8 alternatives with overlapping features. Most require the Twitter API v2 Basic tier ($100/month), which is a significant barrier for individual developers.

## Bluesky & AT Protocol — The Developer-Friendly Alternative

### cameronrye/atproto-mcp (57 Tools)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [cameronrye/atproto-mcp](https://github.com/cameronrye/atproto-mcp) | 6 | TypeScript | MIT | 57 |

The most ambitious social media MCP server we've seen across any platform. **57 tools** organized into categories:

- **Social operations** — create posts, like, repost, follow, unfollow
- **Data retrieval** — search posts, view profiles, access feeds, get followers
- **Content management** — upload media, delete posts, manage threads
- **List and moderation** — create/manage lists, moderation tools
- **Real-time streaming** — live data feeds from the AT Protocol firehose
- **Batch operations** — follow, like, or repost up to 25 items at once
- **Analytics and insights** — engagement metrics, follower analysis
- **OAuth management** — authentication handling

Works in both authenticated and unauthenticated modes — you can read public data without logging in, then authenticate for write operations. The AT Protocol's open architecture makes this possible; unlike Twitter's restricted API, Bluesky's protocol was designed for third-party access.

The low star count (6) belies the server's depth. This is early-stage but remarkably comprehensive.

### semioz/bluesky-mcp (Official Repo Featured)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [semioz/bluesky-mcp](https://github.com/semioz/bluesky-mcp) | 7 | JavaScript | — | 11 |

Featured in the official MCP server repository. Covers the essentials:

- **Authentication** — login
- **Posts** — create, get, list, delete
- **Interactions** — like, unlike, repost, unrepost
- **Profile and timeline** — get profile, get timeline

Includes a `format-timeline` prompt for human-readable timeline rendering. Simpler than atproto-mcp but with official recognition.

**Why Bluesky matters for MCP:** The AT Protocol was built as an open, federated system — there are no API rate limit paywalls like Twitter's $100/month tier. Any developer can build on it freely, which explains why the tooling is already sophisticated despite Bluesky's smaller user base.

## Instagram

### jlbadano/ig-mcp (Leading Server)

| Server | Stars | Language | Tools |
|--------|-------|----------|-------|
| [jlbadano/ig-mcp](https://github.com/jlbadano/ig-mcp) | 88 | Python | 8 |

The most capable Instagram MCP server, built on the Instagram Graph API for Business accounts. Eight tools cover:

- **Profile retrieval** — account information and metrics
- **Media management** — fetch recent posts, publish new content
- **Engagement analytics** — likes, comments, reach, impressions
- **Page management** — list connected Facebook pages
- **Direct messaging** — read and manage conversations (requires advanced access approval from Meta)

Requires an Instagram Business account and Facebook Page connection — personal accounts won't work with the Graph API.

### Other Instagram Servers

- **Bob-lance/instagram-engagement-mcp** — engagement tracking, demographic insights, and lead generation from Instagram posts
- **anand-kamble/mcp-instagram** — profiles, timelines, stories, and smart engagement features (liking, following)
- **BilalTariq01/instagram-analytics-mcp** — account-level and media-level insights via Graph API
- **trypeggy/instagram_dm_mcp** — focused specifically on Direct Message sending
- **duhlink/instagram-server-next-mcp** — Next.js-based Instagram integration

## LinkedIn

| Server | Focus | Language |
|--------|-------|----------|
| [adhikasp/mcp-linkedin](https://github.com/adhikasp/mcp-linkedin) | Feeds & Job API | Python |
| [felipfr/linkedin-mcpserver](https://github.com/felipfr/linkedin-mcpserver) | Profile search, jobs, messaging | Python |
| [eliasbiondo/linkedin-mcp-server](https://github.com/eliasbiondo/linkedin-mcp-server) | People/company/job search | — |
| [Rayyan9477/linkedin_mcp](https://github.com/Rayyan9477/linkedin_mcp) | Job search, resume generation | — |
| [rugvedp/linkedin-mcp](https://github.com/rugvedp/linkedin-mcp) | Profile analysis, post management | — |

LinkedIn has no official MCP server, and the community implementations face a challenge: LinkedIn's API is heavily restricted compared to other platforms. Most servers focus on:

- **Job searching and listing** — the most accessible API endpoint
- **Profile viewing** — reading public profile data
- **Post management** — creating and managing LinkedIn posts
- **Resume and cover letter generation** — AI-powered job application tools

The Rayyan9477/linkedin_mcp server stands out for combining job search with AI-generated resumes and cover letters — turning the MCP server into a job application assistant rather than just an API wrapper.

## Multi-Platform Social & Video

### anaisbetts/mcp-youtube (Most Starred Video Server)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [anaisbetts/mcp-youtube](https://github.com/anaisbetts/mcp-youtube) | 503 | JavaScript | MIT | 1 |

The most popular video platform MCP server does exactly one thing: **extract subtitles from YouTube videos** using yt-dlp. Ask Claude to summarize a YouTube video, and this server fetches the transcript.

That's genuinely useful, but it highlights a massive gap — there's no comprehensive YouTube MCP server with upload, analytics, channel management, or comment moderation capabilities. YouTube's Data API v3 is well-documented and free (with quotas), so this gap is surprising.

### Seym0n/tiktok-mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [Seym0n/tiktok-mcp](https://github.com/Seym0n/tiktok-mcp) | 137 | JavaScript | MIT | 3 |

TikTok integration via TikNeuron with three tools:

- **tiktok_get_subtitle** — retrieve video captions and transcripts
- **tiktok_get_post_details** — metadata including engagement stats, creator info, hashtags
- **tiktok_search** — find videos matching criteria with pagination

Read-only — no posting or account management. Useful for content research and competitive analysis.

### vanman2024/ayrshare-mcp (13 Platforms, One Server)

| Server | Stars | Language | Tools | Platforms |
|--------|-------|----------|-------|-----------|
| [vanman2024/ayrshare-mcp](https://github.com/vanman2024/ayrshare-mcp) | 1 | Python | 75+ | 13 |

The most ambitious multi-platform server: **75+ tools across 13 social networks** — Facebook, Instagram, Twitter/X, LinkedIn, TikTok, YouTube, Pinterest, Reddit, Snapchat, Telegram, Threads, Bluesky, and Google Business Profile. Built on the Ayrshare API.

Covers core posting, engagement management, analytics, multi-user SaaS capabilities, AI-powered features, automation, content discovery, and brand management. The breadth is staggering, but the 1-star count suggests minimal real-world adoption — and Ayrshare is a paid API service, so this is essentially a premium tool wrapper.

## Advertising & Paid Media

### pipeboard-co/meta-ads-mcp (Category Leader)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [pipeboard-co/meta-ads-mcp](https://github.com/pipeboard-co/meta-ads-mcp) | 628 | Python | BSL 1.1 → Apache 2.0 (2029) | 26 |

The most starred server in this entire review and the closest thing to enterprise-grade ad campaign management via MCP. **26 tools** organized across:

- **Account and campaign management** — retrieve accounts, campaigns, ad sets, ads
- **Creative operations** — upload images, create and update ad creatives
- **Performance analytics** — insights with breakdowns and attribution windows
- **Targeting** — search interests, behaviors, demographics, geo-locations
- **Budget management** — create budget schedules
- **Authentication** — OAuth flow handling

Covers Facebook, Instagram, and all Meta ad platforms. The Business Source License 1.1 is worth noting — it transitions to Apache 2.0 in January 2029, but until then it restricts commercial use as a competing product.

### google-marketing-solutions/google_ads_mcp (Official — Experimental)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [google-marketing-solutions/google_ads_mcp](https://github.com/google-marketing-solutions/google_ads_mcp) | 129 | Python | Apache-2.0 | 6+ |

Google's official (but experimental) MCP server for the Google Ads API. Campaign management, ad group operations, and metrics retrieval. Marked as "not an officially supported Google product" — it's a Google Marketing Solutions community project, not a core Google product.

A separate repo at **googleads/google-ads-mcp** provides an alternative local MCP server implementation.

### amekala/ads-mcp (Cross-Platform Ads)

| Server | Stars | Language | License | Platforms |
|--------|-------|----------|---------|-----------|
| [amekala/ads-mcp](https://github.com/amekala/ads-mcp) | 19 | Shell | Proprietary | 4 |

**100+ tools** across Google Ads (39 tools), LinkedIn Ads (28 tools), Meta Ads (20 tools), and TikTok Ads (4 tools). Campaign creation, performance analysis, keyword research, and budget optimization from a single server. Works with Claude Code, Cursor, Codex, ChatGPT, and others.

The proprietary license limits adoption, but the cross-platform coverage is unique — this is the only server that unifies all major ad platforms.

### Other Ad Servers

- **gomarble-ai/facebook-ads-mcp-server** — programmatic Facebook Ads access and management
- **attainmentlabs/meta-ads-mcp** — campaign creation and management from Claude
- **brijr/meta-mcp** — comprehensive Meta Marketing API with full campaign lifecycle management
- **trypeggy/facebook-ads-library-mcp** — search Facebook's public Ads Library to see what competitors are running (no ad account needed)

## SEO & Content Marketing

### cnych/seo-mcp (Free Ahrefs Data)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [cnych/seo-mcp](https://github.com/cnych/seo-mcp) | 224 | Python | MIT | 4 |

The most popular SEO MCP server provides **free access to Ahrefs data** through four tools:

- **get_backlinks_list** — backlink analysis
- **keyword_generator** — keyword research and ideas
- **get_traffic** — traffic estimation
- **keyword_difficulty** — keyword difficulty scoring

Important caveat: this works by **scraping Ahrefs data**, not through an official API. It includes automatic CAPTCHA solving via CapSolver and response caching. This approach can break at any time if Ahrefs changes their frontend, and may violate Ahrefs' terms of service.

### ahrefs/ahrefs-mcp-server (Official — Archived)

| Server | Stars | Language | Status |
|--------|-------|----------|--------|
| [ahrefs/ahrefs-mcp-server](https://github.com/ahrefs/ahrefs-mcp-server) | 94 | TypeScript | Archived |

Ahrefs' official local MCP server has been **archived and superseded** by a remote MCP server at `mcp.ahrefs.com`. The remote version requires no local setup and works directly in AI tools — a shift toward hosted, zero-install MCP servers that we're seeing across the industry.

### metehan777/semrush-mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [metehan777/semrush-mcp](https://github.com/metehan777/semrush-mcp) | 12 | TypeScript | MIT | 7 |

Semrush API integration with seven tools: domain_overview, keyword_overview, domain_organic_search, backlinks_overview, competitor_research, domain_adwords, and related_keywords. Requires a Semrush API key (paid plans only).

A second implementation at **mrkooblu/semrush-mcp** provides similar Semrush API data access.

## Email Marketing

### Iterable/mcp-server (Official — Most Comprehensive)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [Iterable/mcp-server](https://github.com/Iterable/mcp-server) | 3 | TypeScript | MIT | 26–105 |

The standout email marketing server. Iterable's official MCP server scales from 26 tools (read-only) to **105 tools** (full access with PII, writes, and sends enabled). Permission tiers:

- **Default (read-only):** 26 tools — query campaigns, templates, user data
- **PII access:** 37 tools — includes personal user data
- **PII + writes:** 87 tools — create campaigns, modify templates
- **Full access:** 105 tools — send messages, trigger workflows

Natural language queries like "How many campaigns did we send last week?" or "Build me an email template that does X" translate directly to platform actions. Currently in beta.

### Mailchimp Servers

- **AgentX-ai/mailchimp-mcp** — TypeScript, MIT, read-only access to Mailchimp's Marketing API. Safe for exploration without risk of sending unintended emails
- **LokiMCPUniverse/mailchimp-mcp-server** — Python, comprehensive Mailchimp API with rate limiting and retry logic
- **mattcoatsworth/mailchip-mcp-server** — campaigns, lists, templates, reports, automations

### Social Media Management Platforms

- **LokiMCPUniverse/hootsuite-mcp-server** — Python, Hootsuite API integration with async support
- **tn819/buffer-mcp** — Buffer scheduling integration
- **HubSpot official MCP** at `developers.hubspot.com/mcp` — CRM + marketing unification, currently in public beta

## The Pattern: Breadth Without Depth

The social media and marketing MCP ecosystem is the broadest we've reviewed — touching every major social platform, all the big ad networks, SEO tools, email platforms, and social media management tools. But most individual servers are thin:

**Twitter/X** has 8+ servers but the most popular one only has 2 tools. **YouTube** (503 stars) only extracts subtitles. **TikTok** (137 stars) is read-only. **LinkedIn** has no official server. **Instagram** requires Business accounts. **Google Ads** is experimental.

The exceptions that achieve real depth:
- **Meta Ads MCP** (628 stars, 26 tools) — full campaign lifecycle management
- **atproto-mcp** (57 tools) — comprehensive AT Protocol/Bluesky integration
- **Iterable** (up to 105 tools) — enterprise email marketing
- **Ayrshare MCP** (75+ tools) — 13-platform coverage (but minimal adoption)

## What's Missing

- **Official Twitter/X MCP server** — the most fragmented category with no vendor support
- **YouTube upload and analytics** — the 503-star server only reads subtitles
- **Cross-platform analytics dashboard** — no server aggregates metrics across social platforms
- **Organic social scheduling** — most servers are for immediate posting, not content calendars
- **LinkedIn official server** — one of the largest professional networks with no official MCP support
- **TikTok posting** — only read-only analysis available
- **Reddit management** — surprisingly absent as a standalone category (only available through Ayrshare)

## Rating: 3.5 / 5

The social media and marketing MCP space earns **3.5/5** — impressive breadth across every major platform and marketing channel, but most servers are shallow. The standouts are genuine: Meta Ads MCP brings professional-grade ad campaign management, atproto-mcp is the most comprehensive single-platform social server we've reviewed anywhere, and Iterable's 105-tool server shows what official vendor commitment looks like.

The deductions are real: **Twitter fragmentation** (8+ servers, no official one, $100/month API barrier), **YouTube's single-tool limitation** (most starred server only extracts subtitles), **read-only video platforms** (no posting to YouTube or TikTok), **scraper-dependent SEO** (the most popular SEO server scrapes rather than using official APIs), and **LinkedIn's complete absence of official support**. The category would jump to 4.0 or higher if YouTube, TikTok, and LinkedIn provided official MCP servers with write capabilities.

For **social media managers**, the combination of platform-specific posting servers plus Ayrshare for multi-platform coverage provides a workable toolkit. For **ad campaign managers**, Meta Ads MCP is genuinely enterprise-ready. For **SEO professionals**, the tooling works but relies on fragile scraping or expensive API access. For **email marketers**, Iterable sets the standard that Mailchimp and others should follow.

*This review was last edited on 2026-03-16 using Claude Opus 4.6 (Anthropic).*

