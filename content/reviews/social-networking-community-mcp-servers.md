---
title: "Social Networking & Community MCP Servers — Twitter/X, Bluesky, LinkedIn, Reddit, Discord, Mastodon, YouTube, TikTok, and More"
date: 2026-03-16T19:30:00+09:00
sources_audited: 2026-08-16
description: "Social networking and community MCP servers are giving AI agents direct access to social platforms — posting, reading feeds, managing communities, and analyzing content via the Model Context Protocol."
og_description: "Social Networking & Community MCP servers: xiaohongshu-mcp (15,300+ stars — Chinese social EXPLOSION), reddit-mcp-buddy (795 stars — new Reddit leader), linkedin-mcp-server (3,100+ stars — 30+ tools), twitter-mcp (402 stars), activitypub-mcp (v3.2.1). FOUR GAPS FILLED: Threads, Pinterest, Twitch, Chinese platforms. 80+ servers. Rating: 5/5."
content_type: "Review"
card_description: "Social networking and community MCP servers for AI-powered social media management, community administration, content analysis, and platform integration. **REFRESH April 28 2026, re-audited August 16 2026 — CHINESE SOCIAL PLATFORM EXPLOSION + FOUR GAPS FILLED.** xpzouying/xiaohongshu-mcp (15,300+ stars, Go) is one of the highest-starred MCP servers in ANY category — 11 tools for Xiaohongshu/RedNote posting, search, engagement. iFurySt/RedNote-MCP (1,100 stars) and yzfly/douyin-mcp-server (1,200 stars, archived) round out the Chinese platform coverage. mcp-trends-hub (267 stars, ByteDance engineer) aggregates trending from Weibo, Zhihu, Douyin, Bilibili. wechat-mcp (15 stars, Go) enables WeChat messaging via WeChatFerry. **Threads gap FILLED** — baguskto/threads-mcp (12 stars, 20+ tools) and mikusnuz/meta-mcp (57 tools covering Threads+Instagram). **Pinterest gap FILLED** — collactivelabs/pinterest-mcp-server (18 stars, 7 tools). **Twitch chat gap FILLED** — mtane0412/twitch-mcp-server (13 tools via Helix API). **Reddit EXPLOSION** — karanb192/reddit-mcp-buddy (795 stars, TypeScript) is the new leader with zero-setup mode and 3-tier auth. adhikasp/mcp-reddit (419 stars). Hawstein 66→184. Arindam200/reddit-mcp (298 stars, 13 tools). eliasbiondo (146 stars, zero-config). king-of-the-grackles/reddit-research-mcp (229 stars, semantic search 20K+ subreddits). **LinkedIn leadership changed** — stickerdaniel/linkedin-mcp-server (3,100+ stars, 30+ tools, v4.22.0, Python) now dominates. **YouTube leaders emerged** — kimtaeyoon83/mcp-server-youtube-transcript (582 stars), anaisbetts/mcp-youtube (540 stars), eat-pray-ai/yutu (616 stars, Go, 20+ tools full API). **Twitter/X fragmented** — EnesCinr 402 stars, adhikasp/mcp-twikit 234 stars, nirholas/XActions 451 stars 140+ tools multi-platform. Infatoshi/x-mcp 51 stars 15 tools. **Discord reshuffled** — SaseQ/discord-mcp (452 stars, Java, 60+ tools) now leads. v-3/discordmcp (224 stars). hanweg/mcp-discord (163 stars). **ActivityPub grew** — cameronrye/activitypub-mcp now at v3.2.1 with full read/authenticated/write tool coverage (a precise current tool-count figure could not be reverified). **TikTok** — Seym0n/tiktok-mcp 191 stars. **Cross-platform matured** — Postiz (34,700+ stars, open source, AGPL-3.0) now has native MCP (11 tools) for multi-platform scheduling. Ayrshare MCP 75+ tools 13+ platforms. runesleo/x-reader (953 stars) universal reader for WeChat+XHS+Telegram+YouTube+Bilibili+X+RSS. **Facebook** — HagaiHen/facebook-mcp-server (207 stars, 33 tools) for Page management and comment moderation. **Social listening emerging** — socialanalytics-mcp-rapidapi 20+ tools, dwarvesf/mcp-social-listening. **Remaining gaps** — no dedicated influencer management MCP, Snapchat consumer features (ads only), no unified cross-platform analytics dashboard. Rating upgraded 4.5→5/5 — four major gaps filled, Chinese social explosion with a 15K+ star server, Reddit growth, cross-platform matured with Postiz 34K+ stars, 80+ servers covering every major global social platform."
last_refreshed: 2026-08-16
---

Social networking and community MCP servers let AI assistants post content, read feeds, manage communities, analyze engagement, and interact with social platforms. Instead of switching between apps or building custom integrations, you can wire social media capabilities directly into your AI workflow through the Model Context Protocol.

This review covers the **social networking and community** vertical — Twitter/X, Bluesky, LinkedIn, Reddit, Discord, Mastodon/Fediverse, YouTube, TikTok, and Hacker News. For communication platforms (Slack, Teams), see our [Communication MCP review](/reviews/slack-mcp-server/). For content creation tools, see our [Content & Copywriting review](/reviews/cms-content-management-mcp-servers/).

The headline findings: **Chinese social platforms exploded** — xiaohongshu-mcp at 15,300+ stars is one of the highest-starred MCP servers in any category. **Four major gaps filled** since our initial review — Threads, Pinterest, Twitch chat, and Chinese platforms all now have MCP servers. **Reddit grew substantially** with reddit-mcp-buddy (795 stars) as the new leader. **LinkedIn leadership changed** — stickerdaniel's server hit 3,100+ stars with 30+ tools. **Cross-platform matured** — Postiz (34,700+ stars) now has native MCP support (11 tools, per its own docs). **ActivityPub grew its tool surface substantially**, though we could not reverify a precise current total. This is now the deepest MCP category we've reviewed, with 80+ servers covering every major global social platform.

**Category:** [Communication & Collaboration](/categories/communication-collaboration/)

## Twitter / X

### EnesCinr/twitter-mcp (Most Popular)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [twitter-mcp](https://github.com/EnesCinr/twitter-mcp) | 402 | TypeScript | — | 2 |

The **most starred dedicated Twitter MCP server** — enables posting tweets and searching Twitter through a clean TypeScript implementation. It remains the star leader for Twitter-specific servers. *Correction (2026-08-16): star count updated to the current live figure (402), verified via GitHub.*

### crazyrabbitLTC/mcp-twitter-server (Most Tools)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [mcp-twitter-server](https://github.com/crazyrabbitLTC/mcp-twitter-server) | 25 | TypeScript | — | 53 |

The **most feature-rich Twitter MCP server** — 53 total tools combining standard Twitter API and enhanced research:

- **33 Twitter API tools** — post, delete, search tweets, analytics, user info, lists, likes, retweets, engagement
- **20 SocialData.tools research tools** — bypass typical API tier restrictions for deeper research
- **5 workflow prompts** — pre-built automation templates
- **6 dynamic resources** — real-time API documentation and status

Requires Twitter API credentials. SocialData.tools API key optional for enhanced research. The most complete Twitter MCP implementation by a wide margin.

### adhikasp/mcp-twikit (No Official API Needed)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [mcp-twikit](https://github.com/adhikasp/mcp-twikit) | 234 | Python | MIT | 2 |

Uses the **Twikit library** to interact with Twitter without official API access — now at 234 stars, making it the **second most-starred Twitter MCP server**. Good for users who don't want to pay for Twitter API tiers. Uses session-based authentication.

### nirholas/XActions (Multi-Platform, Most Tools) — NEW

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [XActions](https://github.com/nirholas/XActions) | 451 | JavaScript | Apache-2.0 | 140+ |

The **most ambitious social MCP project** — 140+ tools covering X/Twitter, Bluesky, Mastodon, and Threads. No API key required — uses browser extension + CLI + MCP architecture. A significant multi-platform entrant that blurs the line between Twitter-specific and cross-platform. *Correction (2026-08-16): star count corrected from 228 to 451 (verified via GitHub); the "v3.1.0 / 58K+ lines of code" figures from the prior audit could not be reverified in the current README and have been removed rather than repeated unverified.*

### Infatoshi/x-mcp — NEW

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [x-mcp](https://github.com/Infatoshi/x-mcp) | 51 | TypeScript | MIT | 15 |

Created February 2026 — a clean **15-tool design** covering the full Twitter API surface: post, read, engage, media, analytics, and bookmarks. Supports Claude Code, Codex CLI, and Cursor. The most modern Twitter-specific implementation.

### Other Twitter/X Servers

- **rafaljanicki/x-twitter-mcp-server** (30 stars) — Twitter API v2, rate limit handling, user/tweet/search/bookmarks
- **taazkareem/twitter-mcp-server** (20 stars) — media upload support, MIT
- **lord-dubious/x-mcp** — bridges LLMs to Twitter via Twikit
- **BioInfo/x-mcp-server** — X API v2, posts and threads
- **Dishant27/twitter-mcp** — CRUD operations via Twitter API

*Correction (2026-08-16): a previously-listed entry, ryanmac/agent-twitter-client-mcp, has been removed from this review — GitHub has disabled the repository for a Terms of Service violation and it is no longer accessible.*

## Bluesky / AT Protocol

### semioz/bluesky-mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [bluesky-mcp](https://github.com/semioz/bluesky-mcp) | 7 | TypeScript | — | ~6 |

A straightforward Bluesky MCP server. Supports:

- **Posting** — create posts via AT Protocol
- **Engagement** — like/unlike posts, repost
- **Timeline** — read your feed
- **Profiles** — view profile information

Requires BLUESKY_IDENTIFIER and BLUESKY_PASSWORD environment variables. Installable via Smithery. *Correction (2026-08-16): the prior "featured in the official MCP server repository" claim came from the project's own README and could not be independently verified — it does not appear in the [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) reference README or the [official MCP registry](https://registry.modelcontextprotocol.io/), so the claim has been removed rather than repeated unverified.*

### cameronrye/atproto-mcp (Full AT Protocol)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [atproto-mcp](https://github.com/cameronrye/atproto-mcp) | 8 | — | — | ~8 |

**Broader AT Protocol access** — not limited to Bluesky. Enables LLMs to interact with any AT Protocol-based social network through standardized MCP tools, resources, and prompts. Future-proof if the AT Protocol ecosystem grows beyond Bluesky.

### brianellin/bsky-mcp-server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [bsky-mcp-server](https://github.com/brianellin/bsky-mcp-server) | 49 | — | — | ~5 |

**Search-focused Bluesky server** — includes URL-to-AT-URI conversion, post search, people search, and time range filtering for fetching posts from timelines, lists, feeds, or profiles.

### Other Bluesky Servers

- **morinokami/mcp-server-bluesky** — general Bluesky interaction
- **berlinbra/BlueSky-MCP** — user profiles and social graph data

## LinkedIn

### stickerdaniel/linkedin-mcp-server (Most Popular — NEW Leader)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [linkedin-mcp-server](https://github.com/stickerdaniel/linkedin-mcp-server) | 3,100+ | Python | — | 30+ |

The **new star leader** for LinkedIn MCP — explosive growth to 3,100+ stars, now at release v4.22.0. Covers profiles, companies, jobs, messages, and profile editing. Very active development with frequent releases. Previously listed as a scraping option in our March review — it has since become the dominant LinkedIn MCP server. *Correction (2026-08-16): star count corrected from 1,100+ to 3,100+ and version from v4.9.3 to v4.22.0 (both verified live on GitHub); the language was also corrected from TypeScript to **Python** — the prior audit had this wrong.*

### Other LinkedIn Servers

- **alinaqi/mcp-linkedin-server** (54 stars) — 5 tools, browser automation via FastMCP
- **fredericbarthelet/linkedin-mcp-server** — LinkedIn Community Management API, MCP OAuth 2.0 third-party auth flow
- **felipfr/linkedin-mcpserver** — official LinkedIn API with OAuth 2.0
- **anysiteio/anysite-mcp-server** — multi-platform (LinkedIn + Instagram + Reddit + Twitter) via Anysite API

*Correction (2026-08-16): a previously-listed entry, adhikasp/mcp-linkedin, has been removed — the repository now returns a 404 on GitHub (deleted or renamed) and could not be reverified.*

## Reddit — EXPLOSION

### karanb192/reddit-mcp-buddy (Most Popular — NEW Leader)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [reddit-mcp-buddy](https://github.com/karanb192/reddit-mcp-buddy) | 795 | TypeScript | MIT | 5 |

The **new Reddit MCP leader** at 795 stars — zero-setup anonymous mode (no API key needed for basic use), 3-tier authentication (10/60/100 requests per minute), in-memory caching up to 50MB. Tools: browse_subreddit, search_reddit, get_post_details, user_analysis, reddit_explain. NPM installable. The fastest-growing Reddit MCP server.

### adhikasp/mcp-reddit

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [mcp-reddit](https://github.com/adhikasp/mcp-reddit) | 419 | Python | MIT | 2 |

Grew massively to 419 stars — fetches hot threads and gets post content with comments. 52 forks. Simple but effective.

### Arindam200/reddit-mcp (Write Support)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [reddit-mcp](https://github.com/Arindam200/reddit-mcp) | 298 | Python | MIT | 13 |

**13 tools** including 4 authenticated write tools — one of the few Reddit MCP servers supporting post creation and replies alongside 9 read-only tools.

### Hawstein/mcp-server-reddit

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [mcp-server-reddit](https://github.com/Hawstein/mcp-server-reddit) | 184 | Python | MIT | 8 |

Grew from 66 to 184 stars — no longer the leader but still solid. Fetches frontpage posts, subreddit info, hot/new/top/rising posts, post details, and comments via redditwarp.

### eliasbiondo/reddit-mcp-server (Zero Config)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [reddit-mcp-server](https://github.com/eliasbiondo/reddit-mcp-server) | 146 | Python | MIT | 6 |

**No API keys or authentication needed** — now at 146 stars. PyPI installable as `reddit-no-auth-mcp-server`. Search posts, browse subreddits, scrape user activity.

### king-of-the-grackles/reddit-research-mcp — NEW

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [reddit-research-mcp](https://github.com/king-of-the-grackles/reddit-research-mcp) | 229 | Python | MIT | 13 |

**Research-focused** — semantic search across 20,000+ subreddits. Zero-setup hosted solution with OAuth2 via Descope. Uses a 3-tool discovery pattern (5 Reddit operations + 5 feed operations). Designed for competitive analysis and market research. v1.0.1 with 103 commits.

### Other Reddit Servers

- **jordanburke/reddit-mcp-server** — posts, comments, user info, content creation
- **zicochaos/reddit-mcp** — caching, rate limiting, robust error handling

## Discord

### SaseQ/discord-mcp (Most Popular — NEW Leader)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [discord-mcp](https://github.com/SaseQ/discord-mcp) | 452 | Java | MIT | 60+ |

The **new Discord MCP star leader** at 452 stars — Java (Spring Boot + JDA), 60+ tools across 14 categories including server info, users, messages, channels, webhooks, roles, moderation (7 tools), voice/stage channels, events, permissions, invites, forums, and emojis. 89 commits (verified live). *Correction (2026-08-16): the previous "v1.0.0... expanded from 30 to 65 tools in the March 2026 release" detail could not be reverified against the current README/release history and has been removed.*

### v-3/discordmcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [discordmcp](https://github.com/v-3/discordmcp) | 224 | TypeScript | MIT | 2 |

**Minimal but popular** — only 2 tools (send-message, read-messages) but 224 stars. Proof that simple, focused servers can attract adoption.

### hanweg/mcp-discord

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [mcp-discord](https://github.com/hanweg/mcp-discord) | 163 | Python | MIT | 14 |

**14 tools** across 4 categories (server info, messages, channels, roles). Python-based with 25 commits. Solid mid-range option.

### HardHeadHackerHead/discord-mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [discord-mcp](https://github.com/HardHeadHackerHead/discord-mcp) | 24 | TypeScript | — | 139 |

**139 admin tools** across 20 categories with interactive setup wizard. Works with Claude Code, Claude Desktop, Cursor, Windsurf. Feature-rich but low star count relative to tool depth.

### barryyip0625/mcp-discord

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [mcp-discord](https://github.com/barryyip0625/mcp-discord) | 102 | TypeScript | MIT | 33 |

33 tools across 7 categories, 163 commits. The original barryyip/discord-mcp appears to have been moved to this account.

### glittercowboy/discord-mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [discord-mcp](https://github.com/glittercowboy/discord-mcp) | 35 | Python | — | 128 |

Grew from 10 to 35 stars. **128 operations** across 28 categories including dedicated moderation. Uses a 3-tool discovery pattern (discord_discover, discord_get_schema, discord_execute).

## Fediverse / Mastodon — MAJOR UPGRADE

### cameronrye/activitypub-mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [activitypub-mcp](https://github.com/cameronrye/activitypub-mcp) | 17 | TypeScript | MIT | 20+ |

**Expanded from a small read-only server** into a much broader tool surface — the current README ([verified 2026-08-16](https://github.com/cameronrye/activitypub-mcp)) lists public read tools (discover-actor, fetch-timeline, get-post-thread, get-instance-info, search, discover-instances, and more), authenticated read tools (list-accounts, get-home-timeline, get-notifications, get-bookmarks, get-favourites, and more), and an opt-in write tool set (post, reply, delete, boost, favourite, bookmark, follow, mute, block, vote, media upload, and scheduled posts):

- **Full write capabilities** — create posts, reply, boost, favorite, bookmark (was read-only)
- **Multi-account support** with secure credential storage
- **Media upload**, **poll voting**, **post scheduling**
- **Content export**, audit logging, rate limiting, instance blocklist support

Works with **Mastodon, Pleroma, Misskey**, and any ActivityPub-compatible platform. This is architecturally significant — one server covers the entire federated network. *Correction (2026-08-16): the previous "v1.1.0 — 53 Tools" figures could not be reverified — the [latest release is v3.2.1](https://github.com/cameronrye/activitypub-mcp/releases) and the current README does not state a total tool count, so the precise "53" and the "21/28/4" category breakdown have been removed rather than repeated unverified.*

### Groupthink-dev/mastodon-blade-mcp — NEW

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [mastodon-blade-mcp](https://github.com/Groupthink-dev/mastodon-blade-mcp) | — | Python | MIT | 45 |

"Security-first, token-efficient MCP server for Mastodon" — **45 tools** (25 read, 20 write) across timelines, statuses, notifications, search, and social interactions. Created April 2026. Notable for its tool count rivaling the ActivityPub server.

## YouTube — Leaders Emerged

### kimtaeyoon83/mcp-server-youtube-transcript (Most Popular)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [mcp-server-youtube-transcript](https://github.com/kimtaeyoon83/mcp-server-youtube-transcript) | 582 | TypeScript | — | ~3 |

The **most starred YouTube MCP server** — transcript download with language fallback, timestamp support, and ad/sponsorship filtering. Neck-and-neck with anaisbetts for the top spot.

### anaisbetts/mcp-youtube

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [mcp-youtube](https://github.com/anaisbetts/mcp-youtube) | 540 | TypeScript | — | ~3 |

**540 stars** — yt-dlp-based subtitle download and exposure. Simple, focused, and widely adopted. Steady growth.

### eat-pray-ai/yutu (Most Complete)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [yutu](https://github.com/eat-pray-ai/yutu) | 616 | Go | — | 20+ |

The **most comprehensive YouTube MCP server** — 20+ command categories covering nearly all YouTube API resources: videos, playlists, captions, channels, comments, subscriptions, search, members, i18n, and channel banners. CLI + MCP server + AI agent in one package. *Correction (2026-08-16): star count updated from 440 to 616; the prior "ranked 19th among all MCP servers" claim does not appear in the current README and no independent ranking source could be found, so it has been cut.*

### dannySubsense/youtube-mcp-server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [youtube-mcp-server](https://github.com/dannySubsense/youtube-mcp-server) | 12 | Python | — | 14 |

**14 tools via YouTube Data API v3** — search, analyze, retrieve video/channel/playlist info. Includes technology freshness scoring. Feature-rich but low adoption at 12 stars.

### Other YouTube Servers

| Server | Stars | Focus |
|--------|-------|-------|
| [ZubeidHendricks/youtube-mcp-server](https://github.com/ZubeidHendricks/youtube-mcp-server) | 563 | Video management, Shorts, analytics |
| [minbang930/Youtube-Vision-MCP](https://github.com/minbang930/Youtube-Vision-MCP) | 6 | Gemini Vision API — describe/summarize videos |
| [nattyraz/youtube-mcp](https://github.com/nattyraz/youtube-mcp) | 5 | Caption extraction, markdown conversion |

YouTube MCP servers are split between **content consumption** (subtitles, analysis) and **channel management** (uploads, analytics). The transcript-focused servers lead in stars, while eat-pray-ai/yutu leads in feature completeness.

## TikTok

### Seym0n/tiktok-mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [tiktok-mcp](https://github.com/Seym0n/tiktok-mcp) | 191 | JavaScript | MIT | 3 |

**191 stars** — AI-native TikTok analysis with 3 tools: subtitle extraction, post details, and search. Uses TikNeuron API.

### Other TikTok Servers

- **yap-audio/tiktok-mcp** (74 stars) — hashtag-based video discovery and trending content
- **AdsMCP/tiktok-ads-mcp-server** (48 stars) — TikTok Ads campaign management
- **ysntony/tiktok-ads-mcp** (40 stars) — TikTok Business API for AI-first ad management
- **gyoridavid/short-video-maker** (1,300+ stars) — creates short videos for TikTok, Instagram Reels, and YouTube Shorts

## Hacker News

| Server | Stars | Description |
|--------|-------|-------------|
| [erithwik/mcp-hn](https://github.com/erithwik/mcp-hn) | 75 | **Star leader** — Hackernews data access |
| [pskill9/hn-server](https://github.com/pskill9/hn-server) | 40 | JavaScript HN server |
| [paabloLC/mcp-hacker-news](https://github.com/paabloLC/mcp-hacker-news) | 33 | Bridge between HN API and AI tools |
| [devabdultech/hn-mcp](https://github.com/devabdultech/hn-mcp) | 19 | JavaScript HN integration |
| [Malayke/hackernews-mcp](https://github.com/Malayke/hackernews-mcp) | 1 | Token-efficient LLM formatting |

erithwik/mcp-hn leads at 75 stars. Multiple implementations for fetching stories, discussions, and comments.

## Chinese Social Platforms — EXPLOSION (Gap Filled)

This is the biggest story in this refresh. Chinese social platforms went from zero MCP servers to having one of the highest-starred MCP servers in any category.

### xpzouying/xiaohongshu-mcp (15,300+ Stars — Breakout)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [xiaohongshu-mcp](https://github.com/xpzouying/xiaohongshu-mcp) | 15,300 | Go | — | 11 |

**15,300 stars** — one of the highest-starred MCP servers in ANY category. 11 tools: login, publish image/text/video, search, recommendation feed, post details, commenting, user profiles, replies, like/unlike, bookmark/unbookmark. Multiple deployment options (binary, Docker). Xiaohongshu (RedNote/XHS) is China's leading lifestyle and social commerce platform; monthly active users were reported above 350 million as of late 2024/early 2025 by data platform [Sacra](https://sacra.com/c/xiaohongshu/) ("As of end-2024, monthly active users exceeded 350 million") and by marketing agency [The Egg](https://www.theegg.com/social/china/xiaohongshu-red-chinas-rising-social-platform-impact-user-demographics-and-marketing-solutions/); Xiaohongshu has not published an audited primary-source figure as of this writing, so this should be read as third-party reporting rather than a confirmed company disclosure.

### iFurySt/RedNote-MCP

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [RedNote-MCP](https://github.com/iFurySt/RedNote-MCP) | 1,100 | TypeScript | MIT | 5 |

**1,100 stars** — auth management, keyword search, CLI init, note retrieval, comment access. Uses Playwright for browser automation.

### Other Chinese Platform Servers

| Server | Stars | Platform | Description |
|--------|-------|----------|-------------|
| [yzfly/douyin-mcp-server](https://github.com/yzfly/douyin-mcp-server) | 1,200 | Douyin | Watermark-free video extraction + AI transcription (ARCHIVED July 2, 2026) |
| [baranwang/mcp-trends-hub](https://github.com/baranwang/mcp-trends-hub) | 267 | Multi | Trending from Weibo, Zhihu, Douyin, Bilibili, Douban, Toutiao, 36kr (by ByteDance engineer) |
| [wopal-cn/mcp-hotnews-server](https://github.com/wopal-cn/mcp-hotnews-server) | 201 | Multi | Hot trending from Zhihu, Baidu, Bilibili, Weibo, Douyin, Hupu, Douban |
| [aicu-icu/xhs-mcp-server](https://github.com/aicu-icu/xhs-mcp-server) | 177 | Xiaohongshu | JavaScript XHS integration |
| [lancelin111/douyin-mcp-server](https://github.com/lancelin111/douyin-mcp-server) | 35 | Douyin | Automated video uploads, TypeScript |
| [lw396/wechat-mcp](https://github.com/lw396/wechat-mcp) | 15 | WeChat | 20 tools via WeChatFerry: messages, contacts, groups (Windows only) |
| Weibo MCP Server | 14 | Weibo | Basic trending/hot topics |

### runesleo/x-reader (Universal Content Reader)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [x-reader](https://github.com/runesleo/x-reader) | 953 | Python | — | ~7 |

**953 stars** — universal content reader supporting WeChat, Xiaohongshu, Telegram, YouTube, Bilibili, X/Twitter, and RSS. MCP server + Claude Code skills. Created February 2026. Bridges Chinese and Western platforms.

## Threads (Meta) — Gap Filled

### baguskto/threads-mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [threads-mcp](https://github.com/baguskto/threads-mcp) | 12 | TypeScript | — | 20+ |

**20+ tools** across 5 categories: profile management, content management (create/delete/search), interactions (replies, mentions, threaded chains), analytics (demographics, engagement trends, follower growth), and setup validation. Phase 3 roadmap includes hashtag suggestions, scheduling, and carousel posts.

### mikusnuz/meta-mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [meta-mcp](https://github.com/mikusnuz/meta-mcp) | 19 | TypeScript | — | 57 |

**57 tools** covering Instagram (33 tools) and Threads (18 tools) plus Meta platform tools (6). Threads tools include: publish text/images/videos/carousels with polls, GIFs, topic tags, link attachments, alt text, spoiler flags; manage replies; search posts; view insights. Uses Graph API v25.0. The most comprehensive Meta platform MCP server.

## Facebook — NEW

### HagaiHen/facebook-mcp-server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [facebook-mcp-server](https://github.com/HagaiHen/facebook-mcp-server) | 207 | Python | — | 33 |

**33 tools** for Facebook Page management: content management, comment moderation (delete, hide, bulk operations), analytics, user interactions, direct messaging, and sentiment filtering. The first significant Facebook MCP server.

## Pinterest — Gap Filled

### collactivelabs/pinterest-mcp-server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [pinterest-mcp-server](https://github.com/collactivelabs/pinterest-mcp-server) | 18 | JavaScript | — | 7 |

**7 tools**: user info, list/create/get boards, list/create/get pins. Pinterest API v5 integration. The first Pinterest MCP server fills a notable gap.

## Twitch Chat — Gap Filled

### mtane0412/twitch-mcp-server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [twitch-mcp-server](https://github.com/mtane0412/twitch-mcp-server) | 3 | TypeScript | — | 13 |

**13 tools** via Twitch Helix API: channel info, stream details, top games, game/channel search, live stream filtering, global emotes, chat badges, user info, clips, chat settings, channel videos, and video comments (GraphQL). The most complete Twitch MCP server.

### TomCools/twitch-mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [twitch-mcp](https://github.com/TomCools/twitch-mcp) | 10 | Java | — | ~3 |

Java (Quarkus) — connects MCP clients to Twitch Chat via Apache Camel integration.

## Cross-Platform Tools — MATURED

### Postiz (gitroomhq/postiz-app) — Open Source Scheduler + MCP

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [postiz-app](https://github.com/gitroomhq/postiz-app) | 34,700+ | TypeScript | AGPL-3.0 | 11 |

**34,700+ stars** — the only open-source social media scheduler we've found with **native MCP server support**. Per Postiz's own documentation, its [MCP server exposes 11 tools](https://docs.postiz.com/mcp/introduction) covering integration/group listing, post scheduling, image/video generation, and posts listing. Posts to Twitter/X, Bluesky, Mastodon, Discord, and more. This is the most significant cross-platform development since our initial review. *Correction (2026-08-16): star count updated from 28,000+ to 34,700+ and license corrected from Apache-2.0 to **AGPL-3.0** (both verified live on GitHub) — the prior license was wrong.*

### Ayrshare MCP (vanman2024/ayrshare-mcp)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [ayrshare-mcp](https://github.com/vanman2024/ayrshare-mcp) | — | Python | — | 75+ |

**75+ tools** across 15 API categories. Posts to **13+ platforms**: Facebook, Instagram, Twitter/X, LinkedIn, TikTok, YouTube, Pinterest, Reddit, Snapchat, Telegram, Threads, Bluesky, Google Business Profile. Multi-user SaaS management. Requires commercial Ayrshare API key.

### Other Cross-Platform Tools

- **blacktwist/social-media-skills** (417 stars) — Claude Code skills for Bluesky, LinkedIn, Threads, Twitter
- **tayler-id/social-media-mcp** (22 stars) — create posts, get trending topics for Twitter/X, Mastodon, LinkedIn
- **Alemusica/social-cli-mcp** (7 stars) — Twitter/X, Reddit, LinkedIn, Instagram + email outreach + Telegram bot
- **Publora** — commercial MCP-native, $5.40/month, 10-12 platforms
- **anysiteio/anysite-mcp-server** — LinkedIn, Instagram, Reddit, Twitter through single API
- **rhdeck/youtube-channel-handle-mcp** — check handle availability across YouTube, Instagram, TikTok, X

## Social Listening & Analytics — EMERGING

- **lama-assaf/socialanalytics-mcp-rapidapi** (3 stars) — 20+ tools: LinkedIn analytics (16), Facebook (3), Instagram (3), Google Search (2). Covers profile analytics, content performance, competitive analysis via RapidAPI
- **dwarvesf/mcp-social-listening** (3 stars) — social listening system with Supabase backend, v1.9.0, 24 releases
- **smithery-ai/social-listening** — Syften API integration for social mention analysis with webhooks

## What's Still Missing

The gap list has shrunk dramatically since March:

- ~~No Threads~~ → **FILLED** (baguskto/threads-mcp, mikusnuz/meta-mcp)
- ~~No Pinterest~~ → **FILLED** (collactivelabs/pinterest-mcp-server)
- ~~No Chinese platforms~~ → **FILLED** (xiaohongshu-mcp 15,300+ stars, RedNote 1,100, Douyin 1,200, WeChat, Weibo)
- ~~No Twitch chat~~ → **FILLED** (mtane0412/twitch-mcp-server 13 tools)
- ~~No community moderation~~ → **PARTIALLY FILLED** (SaseQ/discord-mcp moderation tools, facebook-mcp-server comment moderation)
- ~~No social listening~~ → **EMERGING** (socialanalytics-mcp, mcp-social-listening)
- **No Snapchat consumer** — ads-only integration exists, no Stories/messaging
- **No unified cross-platform analytics dashboard** — analytics exist per-platform but no aggregator
- **No influencer management** — no dedicated outreach, campaign tracking, or creator tools
- **No WhatsApp** — despite being the world's most-used messaging app

## The Bottom Line

**Rating: 5/5** — This is now the **deepest and most complete MCP category we've reviewed**. The transformation since March 2026 is remarkable:

**Chinese social platforms exploded from zero to 15,300+ stars** — xiaohongshu-mcp is one of the highest-starred MCP servers in any category. **Four major gaps filled** — Threads, Pinterest, Twitch chat, and Chinese platforms all now have working MCP servers. **Reddit grew substantially** with reddit-mcp-buddy hitting 795 stars. **LinkedIn got a new leader** at 3,100+ stars with 30+ tools. **Cross-platform matured** — Postiz (34,700+ stars) now has native MCP support (11 tools) for multi-platform scheduling. **ActivityPub expanded its tool surface** to full read/write/multi-account capability, though we could not reverify a precise current tool total.

The category now covers **every major global social platform** — Western (Twitter/X, LinkedIn, Reddit, Discord, YouTube, TikTok, Bluesky, Mastodon, Facebook, Threads, Pinterest, Twitch) and Eastern (Xiaohongshu, Douyin, WeChat, Weibo, Bilibili). With 80+ servers, this is an extraordinary level of ecosystem coverage. The only remaining gaps are Snapchat consumer features, unified cross-platform analytics, and dedicated influencer management tools.

**Best for Twitter/X:** nirholas/XActions (451 stars, 140+ tools, multi-platform) or EnesCinr/twitter-mcp (402 stars, simpler)
**Best for LinkedIn:** stickerdaniel/linkedin-mcp-server (3,100+ stars, 30+ tools, v4.22.0)
**Best for Reddit:** karanb192/reddit-mcp-buddy (795 stars, zero-setup) or Arindam200/reddit-mcp (298 stars, write support)
**Best for Discord:** SaseQ/discord-mcp (452 stars, 60+ tools, Java)
**Best for Fediverse:** cameronrye/activitypub-mcp (v3.2.1, full read/authenticated/write tool set)
**Best for YouTube:** eat-pray-ai/yutu (616 stars, 20+ tools, full API) or kimtaeyoon83/mcp-server-youtube-transcript (582 stars, transcripts)
**Best for Chinese platforms:** xpzouying/xiaohongshu-mcp (15,300+ stars) or runesleo/x-reader (953 stars, multi-platform reader)
**Best for cross-platform:** Postiz (34,700+ stars, open source scheduler + MCP)

*This review was refreshed on 2026-04-28 using Claude Opus 4.6 (Anthropic). Initial review: 2026-03-16. Citations and figures re-audited claim-by-claim on 2026-08-16 against live GitHub data; see inline corrections above.*
