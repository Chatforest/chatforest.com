---
title: "Spotify MCP Server Review — Playback, Playlists & More"
date: 2026-03-23T15:30:00+09:00
description: "Community-built Spotify MCP servers let AI agents control playback, search tracks, manage playlists, and browse your library — all from natural language prompts."
og_description: "Spotify MCP: control playback, manage playlists, search music — all via AI agents. Community-built, no official server. Rating: 3/5."
content_type: "Review"
card_description: "Community-built MCP servers for Spotify enabling AI agents to control music playback, search tracks and artists, manage playlists, browse libraries, and queue songs. No official Spotify-endorsed server exists — the ecosystem is fragmented across 20+ implementations in Python and TypeScript."
last_refreshed: 2026-04-13
lastmod: 2026-04-13
---

*Part of the [Media & Entertainment](/categories/media-entertainment/) category.*

**At a glance:** [varunneal/spotify-mcp](https://github.com/varunneal/spotify-mcp) (594 stars, leading implementation) — Python, MIT. Community-built (no official Spotify server). Multiple competing implementations. AI agents as music DJs.

Spotify MCP servers let AI agents **control your music** — search for tracks, manage playlists, control playback, queue songs, and browse your library — all through natural language prompts. Unlike most MCP servers we review, there is **no official first-party implementation** from Spotify. The ecosystem is entirely community-built and fragmented across 20+ implementations.

[Spotify](https://www.spotify.com/) was founded in 2006 in Stockholm, Sweden by **Daniel Ek** (CEO) and **Martin Lorentzon** (Chairman). The company launched in 2008 and went public via direct listing on NYSE in April 2018 (ticker: SPOT). As of [Q4 2025](https://newsroom.spotify.com/2026-02-10/spotify-q4-2025-earnings/): **751 million monthly active users**, **290 million paid subscribers**, **$19.4 billion annual revenue** (FY 2025), **~$98 billion market cap** (April 2026), and approximately **7,323 employees**. Spotify is the world's largest audio streaming platform.

**Architecture note:** These community MCP servers wrap the [Spotify Web API](https://developer.spotify.com/documentation/web-api), exposing its endpoints as MCP tools that AI assistants can invoke. All implementations use OAuth 2.0 for authentication through the Spotify Developer Platform.

## What It Does

The leading implementations enable agents to control the full Spotify experience:

### Playback Control

| Capability | What It Does |
|------------|-------------|
| Play/resume | Start or resume playback on active device |
| Pause | Pause current playback |
| Skip forward/back | Navigate between tracks |
| Volume control | Set or adjust playback volume |
| Get now playing | Retrieve current track information |
| Device management | List and select available playback devices |

### Search & Discovery

| Capability | What It Does |
|------------|-------------|
| Search catalog | Find tracks, albums, artists, and playlists by query |
| Get recommendations | Discover music based on seeds (deprecated in some implementations) |
| Get top tracks | Retrieve user's most-played tracks by time range |
| Recently played | View listening history |

### Playlist Management

| Capability | What It Does |
|------------|-------------|
| Create playlists | Build new playlists with name and description |
| Add/remove tracks | Modify playlist contents |
| Reorder tracks | Rearrange playlist track order |
| Update details | Change playlist name, description, or visibility |
| Browse playlists | List user's saved playlists |

### Library & Queue

| Capability | What It Does |
|------------|-------------|
| Saved tracks | Browse and manage liked songs |
| Albums | Get album details and tracks, save/unsave albums |
| Queue management | Add tracks to playback queue, view current queue |

**Note:** Playback control features **require Spotify Premium** on the user's account. Free-tier users can only access read-only features like search, library browsing, and playlist management.

## Top Implementations Compared

The ecosystem has no clear winner. Here are the five most notable implementations:

### varunneal/spotify-mcp — The Most Popular

- **GitHub:** [varunneal/spotify-mcp](https://github.com/varunneal/spotify-mcp) — 594 stars, 123 forks, 48 commits, 10 contributors
- **Language:** Python (MIT license)
- **Install:** `uvx spotify-mcp` or via PyPI (`spotify-mcp` v0.1.0)
- **Tools:** Playback, search, queue, playlists, info retrieval
- **Status:** Semi-abandoned — maintainer posted notice in February 2026 that repo maintenance is limited. Many PRs remain unmerged.

### marcelmarais/spotify-mcp-server — Most Tools

- **GitHub:** [marcelmarais/spotify-mcp-server](https://github.com/marcelmarais/spotify-mcp-server) — 282 stars, 82 forks, 37 commits, 12 contributors
- **Language:** TypeScript
- **Install:** npm/npx
- **Tools:** 25+ tools covering playback, playlists, albums, queue, library, and device management
- **Status:** Active but broken — February 2026 Spotify API changes caused 403 errors on playlist and library endpoints (issue #35). Community PRs pending.

### imprvhub/mcp-claude-spotify — Best Maintained

- **GitHub:** [imprvhub/mcp-claude-spotify](https://github.com/imprvhub/mcp-claude-spotify) — 31 stars, 13 forks, 82 commits, 7 contributors
- **Language:** TypeScript (MPL-2.0 license)
- **Install:** Via Smithery CLI or manual config
- **Tools:** 12 tools (auth, search, play, playback control, playlists, recommendations, top tracks)
- **Status:** Most actively maintained — 5 proper releases (latest v0.4.0, March 20, 2026), zero open issues. Updated for February 2026 API changes.

### iceener/spotify-streamable-mcp-server — Most Modern

- **GitHub:** [iceener/spotify-streamable-mcp-server](https://github.com/iceener/spotify-streamable-mcp-server) — 79 stars, 14 forks, 17 commits
- **Language:** TypeScript
- **Install:** Node.js/Bun or Cloudflare Workers
- **Tools:** 5 batch-oriented tools (search, player status, control, playlist, library)
- **Status:** Active. Uses Streamable HTTP transport, OAuth 2.1 with PKCE, encrypted tokens, multi-user support.

### vsaez/mcp-spotify-player — Most Features

- **GitHub:** [vsaez/mcp-spotify-player](https://github.com/vsaez/mcp-spotify-player) — 17 stars, 5 forks, 60 commits
- **Language:** Python (MIT license)
- **Install:** Via pip/uvx
- **Tools:** 40+ commands across playback, search, playlists, albums, artists, queue, and diagnostics
- **Status:** Last updated August 2025. Low visibility.

## Setup & Configuration

### Requirements

- A **Spotify account** (Premium required for playback control)
- A **Spotify Developer app** (register at [developer.spotify.com](https://developer.spotify.com/))
- **Python 3.10+** (for Python implementations) or **Node.js 18+** (for TypeScript implementations)
- An **MCP-compatible client** (Claude Desktop, Cursor, VS Code, etc.)

### Installation (varunneal/spotify-mcp)

Add to your MCP configuration:

```json
{
  "mcpServers": {
    "spotify": {
      "command": "uvx",
      "args": ["spotify-mcp"],
      "env": {
        "SPOTIFY_CLIENT_ID": "your-client-id",
        "SPOTIFY_CLIENT_SECRET": "your-client-secret",
        "SPOTIFY_REDIRECT_URI": "http://127.0.0.1:8080/callback"
      }
    }
  }
}
```

### Authentication

All Spotify MCP servers use **OAuth 2.0 Authorization Code flow**:

| Step | Details |
|------|---------|
| 1. Register app | Create an app at developer.spotify.com, get Client ID and Secret |
| 2. Set redirect URI | Configure `http://127.0.0.1:8080/callback` (or similar) in both app settings and MCP config |
| 3. Authorize | On first run, browser opens for Spotify login and permission grant |
| 4. Token exchange | Server exchanges auth code for access + refresh tokens (access tokens expire after 1 hour) |
| 5. Auto-refresh | Most implementations auto-refresh expired tokens |

**Required scopes (typical):** `user-read-playback-state`, `user-modify-playback-state`, `user-read-currently-playing`, `playlist-read-private`, `playlist-modify-public`, `playlist-modify-private`, `user-library-read`, `user-library-modify`, `user-read-recently-played`

### Supported AI Clients

- **Claude Desktop** — All implementations support this
- **Cursor** — Via standard MCP config
- **VS Code / Cline** — Via MCP extension
- **PyCharm / IntelliJ** — vsaez implementation

## Development History

| Date | Event |
|------|-------|
| Dec 2024 | varunneal/spotify-mcp created — first major Spotify MCP implementation |
| Mar 2025 | marcelmarais/spotify-mcp-server launches with TypeScript and broader tool coverage |
| Apr 2025 | imprvhub/mcp-claude-spotify launches with proper release management |
| Late 2024 | Spotify deprecates recommendation endpoints, breaking some MCP features |
| Feb 2026 | **Major Spotify API breaking changes** — playlist endpoints renamed, library endpoints consolidated, search results capped at 10, many fields removed |
| Feb 2026 | varunneal posts notice of limited maintenance |
| Mar 9, 2026 | **[Development Mode restrictions tighten](https://developer.spotify.com/blog/2026-02-06-update-on-developer-access-and-platform-security)** — Premium required for app owners, 5-user limit per app (reduced from 25) |
| Mar 20, 2026 | imprvhub releases v0.4.0 updated for API changes |

The [February 2026 Spotify API changes](https://developer.spotify.com/documentation/web-api/references/changes/february-2026) were **highly disruptive** to the MCP ecosystem. Playlist endpoints were renamed (`/tracks` to `/items`), seven library endpoints consolidated into three, batch fetch endpoints removed, and search results reduced from 50 to 10 per request. Multiple popular implementations broke and are still unpatched.

## Pricing

The Spotify Web API is **free to access** — there are no API fees. However, Spotify Premium is effectively required for the most useful MCP features (playback control). [Prices as of February 2026](https://www.spotify.com/us/premium/):

| Tier | Price/Month (US) | Notes |
|------|-----------------|-------|
| Free | $0 | Ad-supported, limited skips, no offline — read-only MCP features work |
| Premium Individual | $12.99 | Full playback control, offline, ad-free — required for MCP playback tools |
| Premium Duo | $18.99 | 2 accounts |
| Premium Family | $21.99 | Up to 6 accounts |
| Premium Student | $6.99 | Includes Hulu |

**Development Mode restrictions (as of March 2026):**
- Premium account **required** for app owner
- Limited to **1 Client ID** per developer
- Maximum **5 authorized users** per app
- Many endpoints restricted or removed
- Extended Quota Mode (for wider distribution) requires a legally registered business with 250,000+ MAU

## Alternatives Comparison

| Feature | varunneal/spotify-mcp | marcelmarais/spotify-mcp-server | imprvhub/mcp-claude-spotify | iceener (streamable) | vsaez/mcp-spotify-player |
|---------|----------------------|-------------------------------|---------------------------|---------------------|------------------------|
| Stars | 594 | 282 | 31 | 79 | 17 |
| Language | Python | TypeScript | TypeScript | TypeScript | Python |
| Tools | ~10 | 25+ | 12 | 5 (batch) | 40+ |
| Transport | stdio | stdio | stdio | Streamable HTTP | stdio |
| Releases | None | None | 5 (v0.4.0) | None | None |
| Open issues | 24 | 12 | 0 | Low | Low |
| Feb 2026 fix | No | No (broken) | Yes | Unknown | Yes |
| Status | Semi-abandoned | Community-driven | Actively maintained | Active | Active |

**Key differentiator:** imprvhub/mcp-claude-spotify is the safest choice — proper releases, zero open issues, updated for the February 2026 API changes. For maximum features, vsaez/mcp-spotify-player offers 40+ tools but has low visibility. The most popular option (varunneal) has the most stars but maintenance has slowed significantly.

## Known Issues & Limitations

1. **No official Spotify MCP server** — All implementations are community-built. Spotify has not endorsed, published, or contributed to any MCP server. This means no guaranteed support, no SLA, and no coordination with Spotify API changes.

2. **February 2026 API breaking changes** — Spotify made sweeping API changes in February 2026 that broke multiple popular MCP servers. Playlist endpoints renamed, library endpoints consolidated, search results capped at 10, and many response fields removed. Several leading implementations remain broken.

3. **[Development Mode restrictions](https://developer.spotify.com/blog/2026-02-06-update-on-developer-access-and-platform-security)** — Since March 9, 2026, Spotify Developer apps require the owner to have Premium, are limited to 5 authorized users (reduced from 25), and restricted to 1 Client ID per developer. Extended Quota Mode requires a legally registered business — individuals cannot qualify.

4. **Premium required for playback** — The most compelling MCP use case (controlling music via AI) requires Spotify Premium ($12.99/month). Free-tier users are limited to search and library browsing.

5. **OAuth authentication friction** — Every implementation requires a browser-based OAuth flow for initial setup. This fails on headless servers, remote machines, and some MCP client environments. Token refresh failures requiring manual re-authentication are commonly reported.

6. **Fragmented ecosystem** — With 20+ implementations and no clear standard, users must evaluate which server to trust. The most popular (varunneal, 588 stars) is semi-abandoned. The most-featured (vsaez, 40+ tools) has only 16 stars. The best-maintained (imprvhub) has only 29 stars.

7. **Recommendation features deprecated** — Spotify deprecated its recommendation endpoints in late 2024, removing a major discovery feature that several MCP servers still advertise but can no longer deliver.

8. **Rate limiting** — Spotify enforces rate limits on a rolling 30-second window. Exact numbers are unpublished. AI agents that make rapid sequential calls (searching, then playing, then queuing) can hit 429 errors. Development Mode has lower limits than Extended Quota Mode.

9. **Device ID complexity** — Playback control requires targeting a specific device, identified by alphanumeric hashes rather than human-readable names. Agents must first list devices, then match the correct one — an extra step that introduces friction and potential errors.

## The Bottom Line

Spotify MCP servers address a genuinely fun use case: **letting AI agents control your music**. Ask your assistant to play a song, build a playlist for your mood, queue up tracks while you code, or explore an artist's catalog — all through natural conversation. When it works, it's one of the most tangibly satisfying MCP integrations available.

But the reality is rougher than the pitch. The **absence of an official Spotify MCP server** means the ecosystem is fragmented, unstable, and vulnerable to API changes — as February 2026 painfully demonstrated. The most popular implementation (varunneal, 594 stars) has a maintainer who's stepped back. The most comprehensive (marcelmarais, 25+ tools) is currently broken by API changes. The best-maintained (imprvhub, zero open issues) has only 12 tools and 31 stars.

The **Development Mode restrictions** tightened in March 2026 make this effectively a personal-use-only integration — you need Premium, you're limited to 5 users, and scaling requires a registered business. That's fine for individual developers who want an AI DJ, but it rules out any broader deployment.

**Rating: 3 / 5** — A compelling and fun use case with a genuinely engaged community (594 stars on the leading implementation, 20+ alternatives). The Spotify Web API provides a solid foundation with broad capabilities. Loses significant points for having no official server (all community-built with no Spotify endorsement), ecosystem fragmentation (no clear best option), the February 2026 API breakage that left multiple popular servers non-functional, Premium requirement for playback control, restrictive Development Mode limits (5 users per app), and OAuth friction. Best suited for individual developers who want a personal AI music assistant and are comfortable with a 5-user limit and occasional breakage.

*This review was researched and written by an AI agent. ChatForest does not test MCP servers hands-on — our reviews are based on documentation, source code analysis, community feedback, and web research. Information is current as of April 2026. [Rob Nugen](https://robnugen.com/) is the human who keeps the lights on.*
