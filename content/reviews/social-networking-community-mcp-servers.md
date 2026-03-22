---
title: "Social Networking & Community MCP Servers — Twitter/X, Bluesky, LinkedIn, Reddit, Discord, Mastodon, YouTube, TikTok, and More"
date: 2026-03-16T19:30:00+09:00
description: "Social networking and community MCP servers are giving AI agents direct access to social platforms — posting, reading feeds, managing communities, and analyzing content via the Model Context Protocol. We reviewed 50+ servers across 8 subcategories. Twitter/X (most implementations): EnesCinr/twitter-mcp (373 stars, TypeScript — posting/searching), crazyrabbitLTC/mcp-twitter-server (53 tools — 33 Twitter API + 20 SocialData.tools research, workflow automation), adhikasp/mcp-twikit (Python — Twikit library, no API key needed), ryanmac/agent-twitter-client-mcp (elizaOS integration, no API access required), lord-dubious/x-mcp (Twikit bridge), 5+ more implementations. Bluesky / AT Protocol: semioz/bluesky-mcp (featured in official MCP repo — posting/liking/reposting/timeline/profiles via AT Protocol), cameronrye/atproto-mcp (full AT Protocol ecosystem access), brianellin/bsky-mcp-server (URL-to-URI conversion, search, time range filtering), morinokami/mcp-server-bluesky. LinkedIn: adhikasp/mcp-linkedin (177 stars, Python — feeds and job API), felipfr/linkedin-mcpserver (official API, OAuth 2.0, profile/job search), anysiteio/anysite-mcp-server (multi-platform: LinkedIn + Instagram + Reddit + Twitter), stickerdaniel/linkedin-mcp-server (profile/company/job scraping), Dishant27/linkedin-mcp-server. Reddit: Hawstein/mcp-server-reddit (66 stars, Python — frontpage/subreddits/posts/comments via redditwarp), eliasbiondo/reddit-mcp-server (zero-config, no API keys), adhikasp/mcp-reddit (content analysis), aflekkas/reddit-mcp-server (fetch + create content), 3+ more. Discord: HardHeadHackerHead/discord-mcp (134 tools across 20 categories), glittercowboy/discord-mcp (128 operations — messages/moderation/channels/roles/events), SaseQ/discord-mcp (Discord API integration), barryyip/discord-mcp (71 stars). Fediverse / Mastodon: cameronrye/activitypub-mcp (ActivityPub protocol — works with Mastodon/Pleroma/Misskey). YouTube: anaisbetts/mcp-youtube (yt-dlp subtitles), dannySubsense/youtube-mcp-server (14 tools, YouTube Data API v3), ZubeidHendricks/youtube-mcp-server (video management, Shorts, analytics), minbang930/Youtube-Vision-MCP (Gemini Vision API). TikTok: Seym0n/tiktok-mcp (virality analysis, video content, ASR), yap-audio/tiktok-mcp (hashtag search, trending content), AdsMCP/tiktok-ads-mcp-server (campaign management). Hacker News: 5+ implementations for fetching discussions and articles. Gaps: no Threads (Meta), no Pinterest, no Snapchat, no WeChat/Weibo, no Twitch chat, no community moderation AI, no cross-platform analytics dashboards, no influencer management, no social listening aggregation. 50+ servers across 8 subcategories. Rating: 4.5/5."
og_description: "Social Networking & Community MCP servers: twitter-mcp (373 stars — posting/searching), mcp-twitter-server (53 tools — workflow automation), bluesky-mcp (official repo — AT Protocol), mcp-linkedin (177 stars — feeds/jobs), mcp-server-reddit (66 stars — frontpage/comments), discord-mcp (134 tools). 50+ servers reviewed. Rating: 4.5/5."
content_type: "Review"
card_description: "Social networking and community MCP servers for AI-powered social media management, community administration, content analysis, and platform integration. **Twitter/X has the most MCP server implementations of any social platform** — at least 8 independent servers exist. EnesCinr/twitter-mcp (373 stars, TypeScript) is the most popular, enabling posting tweets and searching Twitter. crazyrabbitLTC/mcp-twitter-server is the most feature-rich with 53 total tools: 33 standard Twitter API tools plus 20 enhanced SocialData.tools research capabilities that bypass typical API restrictions. Features include post/delete/manage tweets, search, analytics, user management, likes, retweets, and 5 pre-built workflow automation prompts. adhikasp/mcp-twikit (Python) uses the Twikit library to interact with Twitter without official API access. ryanmac/agent-twitter-client-mcp integrates the elizaOS agent-twitter-client package for API-free Twitter interaction. lord-dubious/x-mcp bridges LLMs to Twitter via Twikit. Multiple additional implementations exist from BioInfo, Dishant27, and Rakibulislamsarkar. **Bluesky gets first-class MCP support** — semioz/bluesky-mcp is featured in the official MCP server repository and provides posting, liking, reposting, timeline management, and profile operations via the AT Protocol. cameronrye/atproto-mcp provides broader AT Protocol ecosystem access, working with any AT Protocol-based network. brianellin/bsky-mcp-server adds URL-to-AT-URI conversion, post search, and time range filtering. morinokami/mcp-server-bluesky and berlinbra/BlueSky-MCP round out the options. **LinkedIn has strong job + feed integration** — adhikasp/mcp-linkedin (177 stars, Python) provides tools for LinkedIn feeds and job API interaction. felipfr/linkedin-mcpserver uses the official LinkedIn API with OAuth 2.0 for profile search, profile retrieval, and advanced job search filters. anysiteio/anysite-mcp-server is a multi-platform server covering LinkedIn, Instagram, Reddit, and Twitter through the Anysite API. stickerdaniel/linkedin-mcp-server enables scraping LinkedIn profiles, companies, and jobs. alinaqi/mcp-linkedin-server focuses on local automation. **Reddit has 6+ MCP server implementations** — Hawstein/mcp-server-reddit (66 stars, Python) is the most popular, fetching frontpage posts, subreddit info, hot posts, post details, and comments via the redditwarp library. eliasbiondo/reddit-mcp-server is notable for requiring zero configuration and no API keys — built on the redd library. adhikasp/mcp-reddit adds content analysis capabilities. aflekkas/reddit-mcp-server and jordanburke/reddit-mcp-server support both fetching and creating content. zicochaos/reddit-mcp adds caching, rate limiting, and comprehensive error handling. **Discord administration is comprehensive** — HardHeadHackerHead/discord-mcp provides 134 admin tools across 20 categories with an interactive setup wizard for managing entire Discord servers from Claude Code, Claude Desktop, Cursor, or Windsurf. glittercowboy/discord-mcp offers 128 operations covering messages, moderation, channels, roles, events, and more. barryyip/discord-mcp (71 stars) and SaseQ/discord-mcp provide simpler Discord API integration. hanweg/mcp-discord implements Discord bot functionality. **The Fediverse gets ActivityPub support** — cameronrye/activitypub-mcp is a comprehensive MCP server enabling LLMs to explore and interact with the Fediverse through standardized tools, resources, and prompts. Works with Mastodon, Pleroma, Misskey, and any ActivityPub-compatible platform. The only MCP server supporting federated social networking. **YouTube has multiple MCP approaches** — anaisbetts/mcp-youtube uses yt-dlp to download and expose subtitles. dannySubsense/youtube-mcp-server provides 14 tools via YouTube Data API v3 including search, analytics, and technology freshness scoring. ZubeidHendricks/youtube-mcp-server enables video management, Shorts creation, and advanced analytics. minbang930/Youtube-Vision-MCP uses Google Gemini Vision API to describe, summarize, and extract key moments from videos. nattyraz/youtube-mcp adds caption extraction with markdown conversion. **TikTok gets AI-native tools** — Seym0n/tiktok-mcp analyzes TikTok videos for virality factors, extracts content with automatic speech recognition, and retrieves engagement metrics. yap-audio/tiktok-mcp provides hashtag-based video discovery and trending content analysis. AdsMCP/tiktok-ads-mcp-server enables full TikTok Ads campaign management. gyoridavid/short-video-maker creates short videos for TikTok, Instagram Reels, and YouTube Shorts. **Instagram is mostly ads-focused** — jlbadano/ig-mcp provides production-ready Instagram Business account interaction via the Graph API. pipeboard-co/meta-ads-mcp manages Facebook and Instagram Ads (Meta Ads). The Anysite server also covers Instagram data. No consumer Instagram MCP server for posting personal content exists. **Hacker News has 5+ implementations** — koki-develop/hacker-news-mcp-server, Malayke/hackernews-mcp (token-efficient formatting), rawveg/hacker-news-mcp, erithwik/mcp-hn, paabloLC/mcp-hacker-news, and YinTokey/mcp_hackernews. All fetch discussions, stories, and comments from the HN API. **Cross-platform tools exist** — anysiteio/anysite-mcp-server covers LinkedIn, Instagram, Reddit, and Twitter through a single API. rhdeck/youtube-channel-handle-mcp checks handle availability across YouTube, Instagram, TikTok, and X. kristoff-it/simplex enables posting to Twitter, Mastodon, Bluesky, and LinkedIn with a single CLI command (though not MCP-native). **Major gaps persist** — no Threads (Meta) MCP server despite the platform's rapid growth. No Pinterest for visual discovery. No Snapchat integration. No Chinese social platforms (WeChat, Weibo, Douyin, Xiaohongshu). No Twitch chat integration (separate from video streaming). No community moderation AI tools. No cross-platform analytics dashboards. No influencer management or outreach tools. No social listening aggregation across platforms. The category earns 4.5/5 — this is one of the deepest MCP categories we've reviewed. Twitter/X alone has 8+ implementations. Every major Western social platform has at least one MCP server. The Fediverse gets proper ActivityPub support. Discord administration tools are genuinely comprehensive at 134 tools. LinkedIn covers both professional networking and job search. Reddit servers range from zero-config to full CRUD. The main weakness is the absence of Meta's newer platforms (Threads) and Asian social networks. For social media management and community administration via AI, the tooling is remarkably mature."
last_refreshed: 2026-03-16
---

Social networking and community MCP servers let AI assistants post content, read feeds, manage communities, analyze engagement, and interact with social platforms. Instead of switching between apps or building custom integrations, you can wire social media capabilities directly into your AI workflow through the Model Context Protocol.

This review covers the **social networking and community** vertical — Twitter/X, Bluesky, LinkedIn, Reddit, Discord, Mastodon/Fediverse, YouTube, TikTok, and Hacker News. For communication platforms (Slack, Teams), see our [Communication MCP review](/reviews/slack-mcp-server/). For content creation tools, see our [Content & Copywriting review](/reviews/content-copywriting-mcp-servers/).

The headline findings: **Twitter/X has 8+ independent MCP servers** — the most of any social platform. **Bluesky is featured in the official MCP repo**. **Discord has 134+ admin tools** in a single server. **LinkedIn covers feeds and jobs** with 177 stars. **Reddit has 6+ implementations** including zero-config options. **The Fediverse gets proper ActivityPub support**. This is one of the deepest MCP categories we've reviewed.

## Twitter / X

### EnesCinr/twitter-mcp (Most Popular)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [twitter-mcp](https://github.com/EnesCinr/twitter-mcp) | 373 | TypeScript | — | ~8 |

The **most starred Twitter MCP server** — enables posting tweets and searching Twitter through a clean TypeScript implementation. Good for basic Twitter automation — post, search, and interact.

### crazyrabbitLTC/mcp-twitter-server (Most Tools)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [mcp-twitter-server](https://github.com/crazyrabbitLTC/mcp-twitter-server) | — | TypeScript | — | 53 |

The **most feature-rich Twitter MCP server** — 53 total tools combining standard Twitter API and enhanced research:

- **33 Twitter API tools** — post, delete, search tweets, analytics, user info, lists, likes, retweets, engagement
- **20 SocialData.tools research tools** — bypass typical API tier restrictions for deeper research
- **5 workflow prompts** — pre-built automation templates
- **6 dynamic resources** — real-time API documentation and status

Requires Twitter API credentials. SocialData.tools API key optional for enhanced research. The most complete Twitter MCP implementation by a wide margin.

### adhikasp/mcp-twikit (No Official API Needed)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [mcp-twikit](https://github.com/adhikasp/mcp-twikit) | — | Python | — | ~6 |

Uses the **Twikit library** to interact with Twitter without official API access. Good for users who don't want to pay for Twitter API tiers. Uses session-based authentication.

### ryanmac/agent-twitter-client-mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [agent-twitter-client-mcp](https://github.com/ryanmac/agent-twitter-client-mcp) | — | TypeScript | — | ~6 |

Integrates the **elizaOS agent-twitter-client** package for Twitter interaction without direct API access. Part of the broader elizaOS AI agent ecosystem.

### Other Twitter/X Servers

- **lord-dubious/x-mcp** — bridges LLMs to Twitter via Twikit
- **BioInfo/x-mcp-server** — X API v2, posts and threads
- **Dishant27/twitter-mcp** — CRUD operations via Twitter API
- **Rakibulislamsarkar/twitter-mcp** — posting and searching

## Bluesky / AT Protocol

### semioz/bluesky-mcp (Official Repo Featured)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [bluesky-mcp](https://github.com/semioz/bluesky-mcp) | — | TypeScript | — | ~6 |

**Featured in the official MCP server repository** — the most recognized Bluesky MCP server. Supports:

- **Posting** — create posts via AT Protocol
- **Engagement** — like/unlike posts, repost
- **Timeline** — read your feed
- **Profiles** — view profile information

Requires BLUESKY_IDENTIFIER and BLUESKY_PASSWORD environment variables. Installable via Smithery.

### cameronrye/atproto-mcp (Full AT Protocol)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [atproto-mcp](https://github.com/cameronrye/atproto-mcp) | — | — | — | ~8 |

**Broader AT Protocol access** — not limited to Bluesky. Enables LLMs to interact with any AT Protocol-based social network through standardized MCP tools, resources, and prompts. Future-proof if the AT Protocol ecosystem grows beyond Bluesky.

### brianellin/bsky-mcp-server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [bsky-mcp-server](https://github.com/brianellin/bsky-mcp-server) | — | — | — | ~5 |

**Search-focused Bluesky server** — includes URL-to-AT-URI conversion, post search, people search, and time range filtering for fetching posts from timelines, lists, feeds, or profiles.

### Other Bluesky Servers

- **morinokami/mcp-server-bluesky** — general Bluesky interaction
- **berlinbra/BlueSky-MCP** — user profiles and social graph data

## LinkedIn

### adhikasp/mcp-linkedin (Most Popular)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [mcp-linkedin](https://github.com/adhikasp/mcp-linkedin) | 177 | Python | — | ~5 |

The **most starred LinkedIn MCP server** — provides tools to interact with LinkedIn's Feeds and Job API. Browse your feed, search for jobs, and engage with content. Uses unofficial LinkedIn API.

### felipfr/linkedin-mcpserver (Official API)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [linkedin-mcpserver](https://github.com/felipfr/linkedin-mcpserver) | — | — | — | ~4 |

Uses the **official LinkedIn API** with OAuth 2.0 authentication for profile search, profile retrieval, and job search with advanced filters. More reliable long-term than unofficial approaches.

### Other LinkedIn Servers

- **anysiteio/anysite-mcp-server** — multi-platform (LinkedIn + Instagram + Reddit + Twitter) via Anysite API
- **stickerdaniel/linkedin-mcp-server** — scrape profiles, companies, and jobs
- **Dishant27/linkedin-mcp-server** — LinkedIn API integration
- **alinaqi/mcp-linkedin-server** — local automation focus

## Reddit

### Hawstein/mcp-server-reddit (Most Popular)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [mcp-server-reddit](https://github.com/Hawstein/mcp-server-reddit) | 66 | Python | — | ~5 |

The **most starred Reddit MCP server** — fetches frontpage posts, subreddit information and hot posts, post details, and comments. Uses the redditwarp library for Reddit's public API.

### eliasbiondo/reddit-mcp-server (Zero Config)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [reddit-mcp-server](https://github.com/eliasbiondo/reddit-mcp-server) | — | — | — | ~5 |

**No API keys or authentication needed** — built on the redd library for zero-config access to Reddit data. Search posts, browse subreddits, scrape user activity, and get structured data. The easiest Reddit MCP to set up.

### Other Reddit Servers

- **adhikasp/mcp-reddit** — content fetching and analysis
- **aflekkas/reddit-mcp-server** — fetch + create content
- **jordanburke/reddit-mcp-server** — posts, comments, user info, content creation
- **zicochaos/reddit-mcp** — caching, rate limiting, robust error handling
- **Arindam200/reddit-mcp** — general Reddit integration

## Discord

### HardHeadHackerHead/discord-mcp (Most Tools)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [discord-mcp](https://github.com/HardHeadHackerHead/discord-mcp) | — | — | — | 134 |

The **most comprehensive Discord MCP server** — 134 admin tools across 20 categories:

- Messages, moderation, channels, roles, events
- Interactive setup wizard included
- Works with Claude Code, Claude Desktop, Cursor, Windsurf

Full Discord server administration from your AI assistant.

### glittercowboy/discord-mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [discord-mcp](https://github.com/glittercowboy/discord-mcp) | 10 | — | — | 128 |

**128 operations** for messages, moderation, channels, roles, events, and more. Similar scope to HardHeadHackerHead's version with slightly different tool organization.

### Other Discord Servers

- **barryyip/discord-mcp** — 71 stars, Discord integration
- **SaseQ/discord-mcp** — Discord API integration for MCP-compatible apps
- **hanweg/mcp-discord** — Discord bot functionality

## Fediverse / Mastodon

### cameronrye/activitypub-mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [activitypub-mcp](https://github.com/cameronrye/activitypub-mcp) | — | — | — | ~8 |

The **only Fediverse-native MCP server** — a comprehensive ActivityPub implementation enabling LLMs to explore and interact with the entire Fediverse through standardized MCP tools, resources, and prompts:

- Works with **Mastodon, Pleroma, Misskey**, and any ActivityPub-compatible platform
- Not locked to a single instance or implementation
- Federated social networking through AI

This is architecturally significant — instead of building separate servers for each Mastodon instance, one ActivityPub server covers the entire federated network.

## YouTube

### dannySubsense/youtube-mcp-server (Most Complete)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [youtube-mcp-server](https://github.com/dannySubsense/youtube-mcp-server) | — | — | — | 14 |

**14 tools via YouTube Data API v3** — search, analyze, and retrieve detailed information about videos, channels, playlists. Includes technology freshness scoring for knowledge base curation.

### Other YouTube Servers

| Server | Focus |
|--------|-------|
| [anaisbetts/mcp-youtube](https://github.com/anaisbetts/mcp-youtube) | yt-dlp subtitle download |
| [ZubeidHendricks/youtube-mcp-server](https://github.com/ZubeidHendricks/youtube-mcp-server) | Video management, Shorts, analytics |
| [minbang930/Youtube-Vision-MCP](https://github.com/minbang930/Youtube-Vision-MCP) | Gemini Vision API — describe/summarize videos |
| [nattyraz/youtube-mcp](https://github.com/nattyraz/youtube-mcp) | Caption extraction, markdown conversion |
| [adhikasp/mcp-youtube](https://github.com/adhikasp/mcp-youtube) | Subtitle download for LLMs |

YouTube MCP servers are split between **content consumption** (subtitles, analysis) and **channel management** (uploads, analytics). Most focus on the consumption side.

## TikTok

### Seym0n/tiktok-mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [tiktok-mcp](https://github.com/Seym0n/tiktok-mcp) | — | — | — | ~5 |

**AI-native TikTok analysis** — analyze videos for virality factors, extract content with automatic speech recognition, retrieve engagement metrics (views, likes, shares), and search by keywords. Uses TikNeuron under the hood.

### Other TikTok Servers

- **yap-audio/tiktok-mcp** — hashtag-based video discovery and trending content
- **AdsMCP/tiktok-ads-mcp-server** — TikTok Ads campaign management
- **ysntony/tiktok-ads-mcp** — TikTok Business API for AI-first ad management
- **gyoridavid/short-video-maker** — creates short videos for TikTok, Instagram Reels, and YouTube Shorts

## Hacker News

| Server | Description |
|--------|-------------|
| [koki-develop/hacker-news-mcp-server](https://github.com/koki-develop/hacker-news-mcp-server) | HN API access for AI agents |
| [Malayke/hackernews-mcp](https://github.com/Malayke/hackernews-mcp) | Token-efficient LLM formatting |
| [rawveg/hacker-news-mcp](https://github.com/rawveg/hacker-news-mcp) | HN API integration |
| [erithwik/mcp-hn](https://github.com/erithwik/mcp-hn) | Hackernews data access |
| [paabloLC/mcp-hacker-news](https://github.com/paabloLC/mcp-hacker-news) | Bridge between HN API and AI tools |

Five or more implementations for fetching stories, discussions, and comments. Malayke/hackernews-mcp stands out for its token-efficient formatting optimized for LLM consumption.

## Cross-Platform Tools

- **anysiteio/anysite-mcp-server** — LinkedIn, Instagram, Reddit, Twitter through single Anysite API
- **rhdeck/youtube-channel-handle-mcp** — check handle availability across YouTube, Instagram, TikTok, X
- **gyoridavid/short-video-maker** — create short-form video for TikTok, Reels, and Shorts

## What's Missing

Despite being one of the deepest MCP categories:

- **No Threads (Meta)** — despite rapid platform growth, zero MCP servers
- **No Pinterest** — visual discovery and bookmarking unrepresented
- **No Snapchat** — no messaging or Stories integration
- **No Chinese platforms** — WeChat, Weibo, Douyin, Xiaohongshu all absent
- **No Twitch chat** — live streaming chat interaction (separate from video)
- **No community moderation AI** — no automated moderation or toxicity detection tools
- **No cross-platform analytics** — no unified dashboards across social networks
- **No influencer management** — no outreach, campaign tracking, or creator tools
- **No social listening** — no aggregated monitoring across platforms

## The Bottom Line

**Rating: 4.5/5** — This is one of the deepest MCP categories we've reviewed. Twitter/X alone has 8+ independent implementations, with crazyrabbitLTC's 53-tool server being genuinely comprehensive. Every major Western social platform has at least one MCP server — and most have several. Bluesky's AT Protocol gets first-class support in the official MCP repo. Discord administration is remarkably mature at 134 tools. LinkedIn covers both professional networking and job search. Reddit ranges from zero-config to full CRUD. The Fediverse gets proper ActivityPub support that works across the entire federated network.

The gaps are in Meta's newer platforms (Threads), Asian social networks (WeChat, Weibo), and advanced features like cross-platform analytics and social listening. For social media management and community administration via AI, the tooling is mature and ready for production use.

**Best for Twitter/X:** crazyrabbitLTC/mcp-twitter-server (53 tools) or EnesCinr/twitter-mcp (373 stars, simpler)
**Best for decentralized social:** semioz/bluesky-mcp (official) or cameronrye/activitypub-mcp (full Fediverse)
**Best for professional networking:** adhikasp/mcp-linkedin (177 stars, feeds + jobs)
**Best for community management:** HardHeadHackerHead/discord-mcp (134 admin tools)
**Best for research:** Hawstein/mcp-server-reddit (66 stars) + Hacker News servers

*This review was last edited on 2026-03-16 using Claude Opus 4.6 (Anthropic).*
