# Social Networking & Community MCP Servers — Twitter/X, Bluesky, LinkedIn, Reddit, Discord, Mastodon, YouTube, TikTok, and More

> Social networking and community MCP servers are giving AI agents direct access to social platforms — posting, reading feeds, managing communities, and analyzing content via the Model Context Protocol.


Social networking and community MCP servers let AI assistants post content, read feeds, manage communities, analyze engagement, and interact with social platforms. Instead of switching between apps or building custom integrations, you can wire social media capabilities directly into your AI workflow through the Model Context Protocol.

This review covers the **social networking and community** vertical — Twitter/X, Bluesky, LinkedIn, Reddit, Discord, Mastodon/Fediverse, YouTube, TikTok, and Hacker News. For communication platforms (Slack, Teams), see our [Communication MCP review](/reviews/slack-mcp-server/). For content creation tools, see our [Content & Copywriting review](/reviews/cms-content-management-mcp-servers/).

The headline findings: **Twitter/X has 8+ independent MCP servers** — the most of any social platform. **Bluesky is featured in the official MCP repo**. **Discord has 134+ admin tools** in a single server. **LinkedIn covers feeds and jobs** with 177 stars. **Reddit has 6+ implementations** including zero-config options. **The Fediverse gets proper ActivityPub support**. This is one of the deepest MCP categories we've reviewed.

**Category:** [Communication & Collaboration](/categories/communication-collaboration/)

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

