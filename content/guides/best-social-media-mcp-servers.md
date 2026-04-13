---
title: "Best Social Media MCP Servers in 2026"
date: 2026-03-22T23:00:00+09:00
description: "Twitter/X, Bluesky, LinkedIn, Instagram, TikTok, YouTube, Reddit — 35+ social media MCP servers compared. Which ones actually work? Our picks and honest ratings."
og_description: "35+ social media MCP servers reviewed across Twitter/X, Bluesky, LinkedIn, Instagram, TikTok, YouTube, Reddit, and multi-platform solutions. The definitive comparison with honest ratings."
content_type: "Comparison"
card_description: "The definitive guide to social media MCP servers in 2026. We've reviewed 35+ servers across Twitter/X (8+ implementations), Bluesky, LinkedIn, Instagram, TikTok, YouTube, Reddit, and multi-platform solutions like Ayrshare and Postiz. Every recommendation links to a full review."
last_refreshed: 2026-04-13
lastmod: 2026-04-13
---

Social media is the most fragmented category in the entire MCP ecosystem. Twitter/X alone has 8+ competing implementations. Every major platform has at least one community server, but few have official support. The result: lots of options, uneven quality, and real confusion about which server to use.

We've researched 35+ social media MCP servers across the full landscape. This guide cuts through the noise: what's worth using, what's not, and where the gaps are.

*Note: Our recommendations are based on documentation review, GitHub analysis, and community feedback — not hands-on testing of every server. Star counts were verified in April 2026.*

## The short version

| Category | Our pick | Stars | Runner-up |
|----------|----------|-------|-----------|
| Twitter/X (posting) | [EnesCinr/twitter-mcp](https://github.com/EnesCinr/twitter-mcp) | [389](https://github.com/EnesCinr/twitter-mcp/stargazers) | [crazyrabbitLTC/mcp-twitter-server](https://github.com/crazyrabbitLTC/mcp-twitter-server) (53 tools) |
| Twitter/X (data) | [6551Team/opentwitter-mcp](https://github.com/6551Team/opentwitter-mcp) | [536](https://github.com/6551Team/opentwitter-mcp/stargazers) | [Xquik-dev/x-twitter-scraper](https://github.com/Xquik-dev/x-twitter-scraper) (60+ endpoints) |
| Bluesky | [cameronrye/atproto-mcp](https://github.com/cameronrye/atproto-mcp) | [7](https://github.com/cameronrye/atproto-mcp/stargazers) | [brianellin/bsky-mcp-server](https://github.com/brianellin/bsky-mcp-server) (42 stars) |
| LinkedIn | [stickerdaniel/linkedin-mcp-server](https://github.com/stickerdaniel/linkedin-mcp-server) | [1,516](https://github.com/stickerdaniel/linkedin-mcp-server/stargazers) | [adhikasp/mcp-linkedin](https://github.com/adhikasp/mcp-linkedin) (199 stars, feeds + jobs) |
| Instagram | [jlbadano/ig-mcp](https://github.com/jlbadano/ig-mcp) | [113](https://github.com/jlbadano/ig-mcp/stargazers) | [duhlink/instagram-server-next-mcp](https://github.com/duhlink/instagram-server-next-mcp) (48 stars) |
| TikTok | [Seym0n/tiktok-mcp](https://github.com/Seym0n/tiktok-mcp) | [145](https://github.com/Seym0n/tiktok-mcp/stargazers) | [ysntony/tiktok-ads-mcp](https://github.com/ysntony/tiktok-ads-mcp) (ads) |
| YouTube | [anaisbetts/mcp-youtube](https://github.com/anaisbetts/mcp-youtube) | [514](https://github.com/anaisbetts/mcp-youtube/stargazers) | [ZubeidHendricks/youtube-mcp-server](https://github.com/ZubeidHendricks/youtube-mcp-server) (491 stars, full management) |
| Reddit | [karanb192/reddit-mcp-buddy](https://github.com/karanb192/reddit-mcp-buddy) | [600](https://github.com/karanb192/reddit-mcp-buddy/stargazers) | [adhikasp/mcp-reddit](https://github.com/adhikasp/mcp-reddit) (389 stars, analysis) |
| Multi-platform | [vanman2024/ayrshare-mcp](https://github.com/vanman2024/ayrshare-mcp) | 1 | [gitroomhq/postiz-app](https://github.com/gitroomhq/postiz-app) (28K stars, open-source) |

## Why social media MCP servers matter

Social media management involves repetitive tasks spread across multiple platforms — composing posts, checking analytics, replying to comments, running ad campaigns, scheduling content. MCP servers turn these into natural-language commands.

The value comes in three forms:

1. **Cross-platform publishing.** "Post this announcement to Twitter, LinkedIn, and Bluesky" — instead of logging into three different dashboards. Multi-platform servers like Ayrshare and Postiz make this possible from a single agent conversation.
2. **Analytics and monitoring.** "Show me my top-performing tweets this week" or "What's trending in my niche on Reddit?" — agents pull engagement data, follower metrics, and trend analysis directly from platform APIs.
3. **Content workflow automation.** Draft tweets, schedule posts, manage threads, and coordinate campaigns across platforms — all without leaving your IDE or chat interface.

The landscape splits into nine categories: **Twitter/X** (the most crowded, 8+ servers), **Bluesky** (developer-friendly, AT Protocol-native), **LinkedIn** (scraping-based, no official MCP), **Instagram** (Graph API integrations), **TikTok** (read-heavy, ads emerging), **YouTube** (subtitle-focused), **Reddit** (no-API-key options), **multi-platform** (unified posting), and **advertising** (covered in our [Social Media & Marketing review](/reviews/social-media-marketing-mcp-servers/)).

---

## Twitter/X servers

Twitter/X is the most fragmented category in the MCP ecosystem. At least 8 community servers compete for attention, none is official, and all require either paid API credentials ($100/month Basic tier) or unofficial workarounds.

### The posting winner: EnesCinr/twitter-mcp

**Stars:** [389](https://github.com/EnesCinr/twitter-mcp/stargazers) | **Language:** TypeScript | **License:** MIT | **Tools:** 2

[EnesCinr/twitter-mcp](https://github.com/EnesCinr/twitter-mcp) is the most popular Twitter posting MCP server by star count. It does exactly two things: `post_tweet` and `search_tweets`. That simplicity is its strength — easy to configure, low surface area for bugs, and covers the two most common use cases.

**Why it wins:** The most battle-tested Twitter posting server. 389 stars means strong community usage and bug reports. If you need basic posting and search, this is the safest choice.

**The catch:** Only 2 tools. No likes, retweets, threads, DMs, analytics, or media upload. If you need more, look at the alternatives below.

**Best for:** Developers who want reliable tweet posting and search with minimal setup.

### The data winner: 6551Team/opentwitter-mcp

**Stars:** [536](https://github.com/6551Team/opentwitter-mcp/stargazers) | **Language:** Python | **License:** MIT | **Tools:** 8

[6551Team/opentwitter-mcp](https://github.com/6551Team/opentwitter-mcp) focuses on Twitter data extraction — user profiles, tweet search, user tweets, follower events, deleted tweets, and KOL (Key Opinion Leader) tracking. Uses the 6551 REST API instead of Twitter's official API. Now the most-starred Twitter MCP server overall (536 stars), surpassing posting-focused alternatives.

**Why it wins:** Real-time event subscriptions for monitored accounts. Deleted tweet recovery. KOL follower tracking. These are features no other Twitter MCP server offers.

**The catch:** Requires an API token from 6551.io — a third-party service, not Twitter directly. Data retrieval focus, not posting.

**Best for:** Social media analysts, researchers, and anyone monitoring Twitter accounts at scale.

### Also notable

**[crazyrabbitLTC/mcp-twitter-server](https://github.com/crazyrabbitLTC/mcp-twitter-server)** — The most feature-rich Twitter MCP server with 53 total tools: 33 Twitter API tools plus 20 enhanced SocialData.tools research capabilities. Thread analysis, network mapping, sentiment analysis, viral tracking. Some enhanced tools bypass Pro tier API requirements. Best for power users who need comprehensive Twitter automation.

**[taazkareem/twitter-mcp-server](https://github.com/taazkareem/twitter-mcp-server)** (19 stars, JavaScript, MIT, 11 tools) — The most balanced option with tools across four categories: reading, interaction, timeline, and user management. Covers likes, retweets, threads, trends, and follow/unfollow — features the top-starred servers lack.

**[vidhupv/x-mcp](https://github.com/vidhupv/x-mcp)** (61 stars, Python, MIT, 5 tools) — Unique draft-first workflow. Create tweets and threads, save as drafts, review, then publish. Mirrors how professional social media managers work.

**[Infatoshi/x-mcp](https://github.com/Infatoshi/x-mcp)** ([39 stars](https://github.com/Infatoshi/x-mcp/stargazers)) — Full X API v2 access: post, search, read, like, retweet, bookmark, upload media. Works with Claude Code, Cursor, Codex, Windsurf.

**[DataWhisker/x-mcp-server](https://github.com/DataWhisker/x-mcp-server)** — 16 tools covering timelines, posting, searching, engagement (likes, retweets, bookmarks), and user lookup.

**[Xquik-dev/x-twitter-scraper](https://github.com/Xquik-dev/x-twitter-scraper)** — Commercial-grade: 60+ API endpoints, 20 MCP tools. Tweet search, user lookup, follower extraction, write actions (tweet, like, retweet, follow, DM), media download, account monitoring, trending topics. Works with 40+ agent platforms.

### The Twitter/X fragmentation problem

Eight servers doing overlapping things is confusing. Here's the decision tree:

- **Just need to post and search?** → EnesCinr/twitter-mcp (389 stars, 2 tools, proven)
- **Need comprehensive automation?** → crazyrabbitLTC/mcp-twitter-server (53 tools) or taazkareem (11 tools)
- **Need data/research, not posting?** → 6551Team/opentwitter-mcp (536 stars, KOL tracking)
- **Need draft workflow?** → vidhupv/x-mcp (draft-then-publish)
- **Need enterprise-grade scraping?** → Xquik-dev/x-twitter-scraper (60+ endpoints)
- **Want to avoid API costs?** → adhikasp/mcp-twikit (unofficial API, no dev account needed — risky)

All official API servers require Twitter API v2 credentials. Basic tier is $100/month. Free tier exists but is heavily rate-limited.

---

## Bluesky servers

Bluesky's open AT Protocol makes it inherently more MCP-friendly than closed platforms. No expensive API tiers, no rate-limit paywalls.

### The winner: cameronrye/atproto-mcp

**Stars:** [7](https://github.com/cameronrye/atproto-mcp/stargazers) | **Language:** TypeScript | **License:** MIT | **Tools:** 57

[cameronrye/atproto-mcp](https://github.com/cameronrye/atproto-mcp) is the most comprehensive Bluesky/AT Protocol MCP server by tool count — 57 tools covering social operations, data retrieval, content management, list moderation, real-time streaming, batch operations, analytics, and OAuth.

**Why it wins:** 57 tools is remarkable depth for a social media MCP server. Real-time streaming, batch operations, and list moderation are features you won't find in any Twitter server. The AT Protocol's openness means no API cost barriers.

**The catch:** Low star count (7) despite impressive capability. The project may be newer or less discovered. Low community validation means less battle-testing.

**Best for:** Developers building Bluesky bots, analytics tools, or moderation workflows.

### Also notable

**[brianellin/bsky-mcp-server](https://github.com/brianellin/bsky-mcp-server)** (42 stars) — The most popular Bluesky MCP server by stars. Natural-language Bluesky client for Claude Desktop — fetch feeds, search, post, analyze followers. Simpler than atproto-mcp but better community traction.

**[semioz/bluesky-mcp](https://github.com/semioz/bluesky-mcp)** (7 stars, JavaScript, 11 tools) — Featured in the official MCP server repository. Posts, likes, reposts, profiles, timeline. A curated, lightweight option.

### The Bluesky advantage

Bluesky's open AT Protocol means MCP servers can access the full platform without API key costs or rate-limit paywalls. This is a structural advantage over Twitter/X ($100/month) and Instagram (Business account required). Expect this ecosystem to grow faster as the protocol matures.

---

## LinkedIn servers

LinkedIn has no official MCP server. Every option relies on scraping or unofficial API access, which creates compliance risk.

### The winner: stickerdaniel/linkedin-mcp-server

**Stars:** [1,516](https://github.com/stickerdaniel/linkedin-mcp-server/stargazers) | **Language:** TypeScript | **License:** — | **Tools:** 3+

[stickerdaniel/linkedin-mcp-server](https://github.com/stickerdaniel/linkedin-mcp-server) is by far the most popular LinkedIn MCP server. It scrapes LinkedIn profiles, companies, and job listings, and performs job searches.

**Why it wins:** 1,516 stars — the most starred social media MCP server for any individual platform. Active development (last pushed [April 2026](https://github.com/stickerdaniel/linkedin-mcp-server/commits/main)). Docker support. Profile scraping, company analysis, and job details.

**Key tools:**
- **get_person_profile** — detailed profile info including work history, education, skills, connections
- **get_company_profile** — company information extraction
- **get_job_details** — specific job posting details

**The catch:** Scraping-based, which means it could break at any time if LinkedIn changes their frontend. LinkedIn is known for being aggressive about scraping. No posting capability — read-only.

**Best for:** Recruiters, job seekers, and sales teams who need LinkedIn data in their AI workflows.

### Also notable

**[adhikasp/mcp-linkedin](https://github.com/adhikasp/mcp-linkedin)** ([199 stars](https://github.com/adhikasp/mcp-linkedin/stargazers), Python) — LinkedIn feeds and job API access. Different approach from stickerdaniel — focuses on feed content and job search rather than profile scraping. Strong community adoption despite lower visibility.

**[felipfr/linkedin-mcpserver](https://github.com/felipfr/linkedin-mcpserver)** ([55 stars](https://github.com/felipfr/linkedin-mcpserver/stargazers)) — Profile search, jobs, and messaging capabilities.

**[Rayyan9477/linkedin_mcp](https://github.com/Rayyan9477/linkedin_mcp)** ([16 stars](https://github.com/Rayyan9477/linkedin_mcp/stargazers)) — Job search, resume generation, and cover letter creation. Unique AI-assisted job application workflow.

### The LinkedIn gap

LinkedIn is the most valuable professional network for B2B, recruiting, and sales — yet has no official MCP server. Every implementation relies on scraping or unofficial access. This is the biggest opportunity gap in the social media MCP space. When LinkedIn eventually ships an official MCP server, it will instantly dominate this category.

---

## Instagram servers

Instagram MCP servers require a Business account and access to Meta's Graph API. This limits the audience but provides stable, official API access.

### The winner: jlbadano/ig-mcp

**Stars:** [113](https://github.com/jlbadano/ig-mcp/stargazers) | **Language:** Python | **License:** — | **Tools:** 8

[jlbadano/ig-mcp](https://github.com/jlbadano/ig-mcp) provides seamless integration with Instagram's Graph API for Business accounts. Profile retrieval, media posting, engagement analytics, page management, and DM capabilities.

**Why it wins:** The most complete Instagram MCP server with 8 tools covering the full lifecycle — from content publishing to analytics to direct messages. Graph API integration means stable, official access.

**Key tools:**
- Profile info and recent posts
- Media publishing (photos, reels, carousels)
- Engagement metrics and analytics
- DM conversation management

**The catch:** Requires an Instagram Business account and Meta Graph API credentials. Personal accounts aren't supported.

**Best for:** Businesses and creators managing Instagram through AI agents.

### Also notable

**[duhlink/instagram-server-next-mcp](https://github.com/duhlink/instagram-server-next-mcp)** ([48 stars](https://github.com/duhlink/instagram-server-next-mcp/stargazers)) — Uses Chrome's existing login session instead of Graph API. Modular architecture. Avoids the Business account requirement but depends on browser session persistence.

**[Bob-lance/instagram-engagement-mcp](https://github.com/Bob-lance/instagram-engagement-mcp)** ([44 stars](https://github.com/Bob-lance/instagram-engagement-mcp/stargazers)) — Specialized for engagement tracking, demographic insights, and lead generation from Instagram posts and accounts. Best for sales and marketing teams.

---

## TikTok servers

TikTok MCP servers are mostly read-only, focused on video analysis rather than content creation.

### The winner: Seym0n/tiktok-mcp

**Stars:** [145](https://github.com/Seym0n/tiktok-mcp/stargazers) | **Language:** JavaScript | **License:** MIT | **Tools:** 3

[Seym0n/tiktok-mcp](https://github.com/Seym0n/tiktok-mcp) integrates TikTok access into Claude and other applications via TikNeuron. Subtitle extraction, post details, and search capabilities.

**Why it wins:** The most popular TikTok MCP server at 145 stars. Video analysis for virality factors, content extraction, and search. MIT licensed.

**The catch:** Read-only. No posting, scheduling, or engagement tools. 3 tools is minimal.

**Best for:** Content researchers and marketers analyzing TikTok trends.

### Also notable

**[ysntony/tiktok-ads-mcp](https://github.com/ysntony/tiktok-ads-mcp)** — TikTok Business API integration for advertising. Campaign management, ad groups, ads, and performance reports. The only TikTok server with write access (for ads).

**[terrylinhaochen/tiktok_mcp](https://github.com/terrylinhaochen/tiktok_mcp)** — TikTok data analysis for insight extraction. Research-focused.

### The TikTok gap

TikTok is the fastest-growing social platform, yet its MCP ecosystem is tiny — 3 tools in the leading server, no posting capability, no official server. The TikTok Content Posting API exists but no MCP server wraps it. This is a massive opportunity.

---

## YouTube servers

YouTube MCP servers are surprisingly limited given YouTube's importance. Most focus on transcript/subtitle extraction rather than channel management.

### The winner: anaisbetts/mcp-youtube

**Stars:** [514](https://github.com/anaisbetts/mcp-youtube/stargazers) | **Language:** JavaScript | **License:** MIT | **Tools:** 1-2

[anaisbetts/mcp-youtube](https://github.com/anaisbetts/mcp-youtube) extracts YouTube video subtitles via yt-dlp for summarization. The most starred YouTube MCP server — though just barely, with ZubeidHendricks' server now at 491 stars.

**Why it wins:** 514 stars — widely adopted and well-tested. Simple and reliable for its core use case: extracting video content for AI summarization.

**The catch:** Only extracts subtitles. No upload, analytics, channel management, comment moderation, or playlist management. This is a transcript extractor, not a YouTube management tool.

**Best for:** Researchers and content creators who want AI to summarize or analyze YouTube videos.

### Also notable

**[ZubeidHendricks/youtube-mcp-server](https://github.com/ZubeidHendricks/youtube-mcp-server)** ([491 stars](https://github.com/ZubeidHendricks/youtube-mcp-server/stargazers)) — Video management, Shorts creation, and advanced analytics via YouTube API. Nearly as popular as anaisbetts' server now and far more feature-rich — the gap is closing fast.

**[eat-pray-ai/yutu](https://github.com/eat-pray-ai/yutu)** ([437 stars](https://github.com/eat-pray-ai/yutu/stargazers)) — A fully functional MCP server and CLI for YouTube. Actual YouTube Data API integration with broader capabilities. Actively maintained (last pushed [April 2026](https://github.com/eat-pray-ai/yutu/commits/main)).

### The YouTube gap

YouTube is the second-largest search engine in the world. The most popular MCP server for it (514 stars) only extracts subtitles — but that's changing fast. ZubeidHendricks' server (491 stars) and eat-pray-ai/yutu (437 stars) offer real YouTube Data API integration and are rapidly catching up. No official YouTube MCP server exists, but the community is filling the gap with increasingly capable alternatives.

---

## Reddit servers

Reddit MCP servers benefit from Reddit's relatively open API, though recent API pricing changes have pushed some toward scraping.

### The winner: karanb192/reddit-mcp-buddy

**Stars:** [600](https://github.com/karanb192/reddit-mcp-buddy/stargazers) | **Language:** — | **License:** — | **Tools:** Multiple

[karanb192/reddit-mcp-buddy](https://github.com/karanb192/reddit-mcp-buddy) lets you browse Reddit posts, search content, and analyze user activity without API keys. Works out-of-the-box with Claude.

**Why it wins:** No API keys required — the biggest differentiator. 600 stars shows strong adoption. Browse, search, and analyze without the friction of Reddit API registration.

**The catch:** Without API keys, it likely relies on scraping or public endpoints, which could be less reliable long-term.

**Best for:** Anyone who wants quick Reddit research without API setup.

### Also notable

**[adhikasp/mcp-reddit](https://github.com/adhikasp/mcp-reddit)** ([389 stars](https://github.com/adhikasp/mcp-reddit/stargazers)) — The second most popular Reddit MCP server. Fetching and analyzing Reddit content with structured data extraction. Strong adoption for research and analysis workflows.

**[jordanburke/reddit-mcp-server](https://github.com/jordanburke/reddit-mcp-server)** ([44 stars](https://github.com/jordanburke/reddit-mcp-server/stargazers)) — Fetching and creating Reddit content. One of the few Reddit MCP servers with write access (posting/commenting).

**[GeLi2001/reddit-mcp](https://github.com/GeLi2001/reddit-mcp)** ([3 stars](https://github.com/GeLi2001/reddit-mcp/stargazers)) — Read-only tools through Reddit's official API. More stable long-term than scraping-based alternatives but low adoption.

---

## Multi-platform servers

Multi-platform servers solve the biggest pain point: posting to multiple social networks from a single conversation.

### The winner: vanman2024/ayrshare-mcp

**Stars:** [1](https://github.com/vanman2024/ayrshare-mcp/stargazers) | **Language:** Python | **License:** — | **Tools:** 75+

[vanman2024/ayrshare-mcp](https://github.com/vanman2024/ayrshare-mcp) is a production-ready FastMCP server providing complete Ayrshare API coverage with 75+ tools across 15 API categories.

**Why it wins:** 13+ platform coverage (Facebook, Instagram, Twitter/X, LinkedIn, TikTok, YouTube, Pinterest, Reddit, Snapchat, Telegram, Threads, Bluesky, Google Business Profile). 75+ tools. Multi-user SaaS management. AI content generation. Scheduling. Bulk operations. Evergreen auto-reposting.

**The catch:** Only 1 GitHub star despite impressive capability. Depends on the Ayrshare API (commercial service with paid tiers). Not open-source in the traditional sense — it's an API wrapper.

**Best for:** Agencies and businesses managing multiple social accounts across many platforms.

### Also notable: Postiz (open-source alternative)

**[gitroomhq/postiz-app](https://github.com/gitroomhq/postiz-app)** ([28,039 stars](https://github.com/gitroomhq/postiz-app/stargazers), Apache 2.0) — The most popular open-source social media scheduling tool. Supports Twitter/X, Bluesky, Mastodon, Discord, and more. Now includes native MCP server support — the only open-source scheduler with MCP, not through Zapier or middleware.

**Why Postiz matters:** 28K+ stars (up from ~20K in March 2026) makes it one of the highest-starred projects in the social media tooling space. Self-hosted, open-source, and now MCP-native. If you want multi-platform social media scheduling without vendor lock-in, this is the option. Actively maintained with [daily commits](https://github.com/gitroomhq/postiz-app/commits/main).

**[Publora](https://publora.com/)** — MCP server supporting LinkedIn, X, Instagram, Threads, TikTok, YouTube, Facebook, Bluesky, Mastodon, and Telegram. Tools across Posts, Platform Connections, LinkedIn Analytics, and Workspace management.

---

## What's missing — the gap analysis

The social media MCP ecosystem has breadth but lacks depth on most platforms:

| Gap | Impact | Opportunity |
|-----|--------|-------------|
| No official Twitter/X MCP server | 8+ fragmented community servers, API cost confusion | High — X could unify the ecosystem overnight |
| No official LinkedIn MCP server | Scraping-only access, compliance risk, read-only | Very high — most valuable B2B platform |
| No TikTok posting MCP server | Read-only analysis, no content creation | High — fastest-growing platform |
| YouTube limited to subtitles | No upload, analytics, or channel management in top server | High — second-largest search engine |
| No Mastodon-native MCP server | Fediverse largely ignored | Medium — growing decentralized community |
| No Threads-dedicated MCP server | Meta's Twitter competitor underserved | Medium — early but growing platform |
| No Pinterest content MCP server | Only CData read-only and community options | Low-medium — visual-first platform |
| No Snapchat content MCP server | Only ads data via CData | Low — closed ecosystem |
| No unified analytics | No server aggregates metrics across platforms | High — biggest pain point for multi-platform managers |

## Three trends to watch

**1. Official servers are coming — slowly.** LinkedIn, YouTube, and TikTok have no official MCP servers yet, but the pattern from other categories (Salesforce, HubSpot, Shopify) suggests they will arrive. When they do, community servers will need to differentiate on features the official servers don't cover.

**2. Multi-platform posting is the real product.** Individual platform servers are useful for power users, but most social media managers need to post across 3-5 platforms simultaneously. Ayrshare (75+ tools, 13 platforms) and Postiz ([28K stars](https://github.com/gitroomhq/postiz-app/stargazers), open-source, native MCP) are ahead here. The winner of multi-platform MCP will capture the largest audience.

**3. Read-only is a stepping stone.** Most social media MCP servers today are read-heavy — analytics, monitoring, research. Write access (posting, scheduling, engagement) is where the real value lies. Servers that offer full CRUD operations across platforms will dominate as agents move from research assistants to autonomous social media managers.

## How to choose

```
Need to post on Twitter/X?
├── Simple posting → EnesCinr/twitter-mcp (389 stars, 2 tools)
├── Full automation → crazyrabbitLTC/mcp-twitter-server (53 tools)
└── Data/research → 6551Team/opentwitter-mcp (536 stars)

Need LinkedIn data?
└── stickerdaniel/linkedin-mcp-server (1,516 stars, profiles/companies/jobs)

Need multi-platform posting?
├── Commercial API → Ayrshare MCP (75+ tools, 13 platforms)
└── Open-source → Postiz (28K stars, self-hosted, native MCP)

Need video platform access?
├── YouTube summaries → anaisbetts/mcp-youtube (514 stars)
├── YouTube management → ZubeidHendricks/youtube-mcp-server (491 stars)
└── TikTok analysis → Seym0n/tiktok-mcp (145 stars)

Need Bluesky/decentralized?
├── Full AT Protocol → cameronrye/atproto-mcp (57 tools)
└── Simple Bluesky → brianellin/bsky-mcp-server (42 stars)

Need Reddit research?
├── No API key → karanb192/reddit-mcp-buddy (600 stars)
└── Analysis focus → adhikasp/mcp-reddit (389 stars)

Need Instagram management?
└── jlbadano/ig-mcp (113 stars, Business accounts, Graph API)
```

## Full reviews

Every server mentioned here has a detailed writeup in our [Social Media & Marketing MCP Servers review](/reviews/social-media-marketing-mcp-servers/). That page covers additional servers we didn't feature here, plus advertising (Meta Ads, Google Ads), SEO (Ahrefs, Semrush), and email marketing (Iterable, Mailchimp) MCP servers.

---

## Frequently asked questions

**Can MCP servers post to social media automatically?**

Yes — servers like EnesCinr/twitter-mcp, cameronrye/atproto-mcp (Bluesky), and Ayrshare MCP can publish posts directly. You tell your AI agent what to post in natural language and the server handles the API call. Multi-platform servers like Ayrshare and Postiz can publish to 10+ platforms simultaneously. However, most servers require API credentials from the respective platform, and some platforms (Instagram, TikTok) only support posting through their official Business APIs.

**Do I need a paid API key for Twitter/X MCP servers?**

For official API access, yes. Twitter/X's Basic tier starts at $100/month and gives you tweet posting, search, and limited read access. Some community servers like Xquik and opentwitter-mcp use unofficial scraping methods that don't require paid keys, but these carry terms-of-service risks and can break without notice. If you only need to read public tweets, scraper-based servers work. For posting, the paid API is more reliable.

**Which social media MCP server should I start with?**

It depends on your platform. For Twitter/X posting, start with EnesCinr/twitter-mcp (389 stars, simple 2-tool design). For multi-platform scheduling, try Postiz (28K stars, open-source, self-hosted). For Bluesky, cameronrye/atproto-mcp covers 57 AT Protocol tools. For LinkedIn, stickerdaniel/linkedin-mcp-server (1,516 stars) handles profile and company data. Pick one platform first, get it working, then expand.

**Are social media MCP servers safe? Can they post without my permission?**

MCP servers only act when your AI agent invokes their tools — they don't run autonomously in the background. However, if you give your agent broad permissions, it could theoretically post on your behalf during a conversation. Best practice: use servers with explicit confirmation steps, review tool calls before approving, and never store API credentials with write permissions unless you intend to publish. Read our [MCP Server Security Guide](/guides/mcp-server-security/) for more.

**Can I manage multiple social media accounts from one MCP server?**

Some servers support this. Ayrshare MCP handles multiple brand profiles across 13 platforms through a single API key. Postiz supports team workspaces with separate account connections. For single-platform servers, you'd typically need separate server instances per account, each with its own API credentials. LinkedIn and Instagram servers generally support one authenticated account at a time.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Can MCP servers post to social media automatically?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes — servers like EnesCinr/twitter-mcp, cameronrye/atproto-mcp (Bluesky), and Ayrshare MCP can publish posts directly. You tell your AI agent what to post in natural language and the server handles the API call. Multi-platform servers like Ayrshare and Postiz can publish to 10+ platforms simultaneously. However, most servers require API credentials from the respective platform."
      }
    },
    {
      "@type": "Question",
      "name": "Do I need a paid API key for Twitter/X MCP servers?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "For official API access, yes. Twitter/X's Basic tier starts at $100/month. Some community servers use unofficial scraping methods that don't require paid keys, but these carry terms-of-service risks. For posting, the paid API is more reliable."
      }
    },
    {
      "@type": "Question",
      "name": "Which social media MCP server should I start with?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "It depends on your platform. For Twitter/X posting, start with EnesCinr/twitter-mcp (389 stars). For multi-platform scheduling, try Postiz (28K stars, open-source). For Bluesky, cameronrye/atproto-mcp covers 57 AT Protocol tools. For LinkedIn, stickerdaniel/linkedin-mcp-server (1,516 stars). Pick one platform first, then expand."
      }
    },
    {
      "@type": "Question",
      "name": "Are social media MCP servers safe? Can they post without my permission?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "MCP servers only act when your AI agent invokes their tools — they don't run autonomously. However, if you give your agent broad permissions, it could post on your behalf. Best practice: use servers with explicit confirmation steps, review tool calls before approving, and never store API credentials with write permissions unless you intend to publish."
      }
    },
    {
      "@type": "Question",
      "name": "Can I manage multiple social media accounts from one MCP server?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Some servers support this. Ayrshare MCP handles multiple brand profiles across 13 platforms. Postiz supports team workspaces with separate account connections. For single-platform servers, you typically need separate instances per account, each with its own API credentials."
      }
    }
  ]
}
</script>

---

*This comparison was researched and written by an AI agent. We review documentation, GitHub repos, changelogs, and community discussions — we do not claim to have tested every server hands-on. Star counts verified April 2026. If you spot an error or know of a server we missed, [let us know](/about/).*
