---
title: "Gaming & Esports MCP Servers — Steam, OP.GG, Minecraft, Chess, CS2, Twitch, IGDB, and More"
date: 2026-03-16T03:30:00+09:00
description: "Gaming and esports MCP servers let AI agents access game libraries, track player stats, control game characters, manage game servers, and analyze esports data through the Model Context Protocol. We reviewed 25+ servers across 7 subcategories. Minecraft: yuniko-software/minecraft-mcp-server (504 stars, TypeScript — 15 commands, Mineflayer-powered real-time character control, building, mining, inventory management). Esports analytics: opgginc/opgg-mcp (76 stars, TypeScript — 27 tools for League of Legends, TFT, and Valorant data, champion analytics, meta compositions, esports schedules). Steam: dsp/mcp-server-steam (12 stars, Java — Steam API gaming context), algorhythmic/steam-mcp (4 stars, JavaScript — 10 tools for achievements, player stats, game schemas), fenxer/steam-review-mcp (5 stars, TypeScript — review analysis with sentiment). Chess: pab1it0/chess-mcp (64 stars, Python — 10 tools for Chess.com data, player profiles, game history, PGN downloads), arvid-berndtsson/Chess-MCP (TypeScript — 12 tools, play against AI with adjustable difficulty, FEN/PGN support), turlockmike/chess-mcp (Stockfish analysis), danilop/chess-support-mcp (game state management without move suggestions). Game server management: v9rt3x/cs2-rcon-mcp (9 stars, Python — 5 tools for Counter-Strike 2 RCON, workshop maps, natural language server control). Game databases: bielacki/igdb-mcp-server (3 stars, Python — 4 tools for IGDB/Twitch game database, trending titles, custom queries), moonolgerd/game-mcp (C# — multi-platform game discovery across Steam/Epic/GOG/Xbox). Streaming: mtane0412/twitch-mcp-server (TypeScript — 13 tools for Twitch Helix API, channel info, streams, clips, emotes). Roblox game interaction: notpoiu/roblox-mcp (18 stars, JavaScript — 18 tools, code execution, script decompilation, remote interception, multi-client support). Gaps: no official platform MCPs from Steam/Valve, Epic Games, PlayStation, Xbox, or Nintendo; no comprehensive esports aggregator beyond OP.GG; no game achievement tracking across platforms; no in-game economy/marketplace MCP. Rating: 3.5/5."
og_description: "Gaming & esports MCP servers: Minecraft (504 stars, character control), OP.GG (76 stars, 27 tools for LoL/TFT/Valorant), Chess.com (64 stars, 10 tools), Steam API (game stats/reviews), CS2 RCON (server management), IGDB (game database), Twitch (13 tools). 25+ servers reviewed. Rating: 3.5/5."
content_type: "Review"
card_description: "Gaming and esports MCP servers for player analytics, game libraries, live game control, game server management, streaming platforms, and game databases. The gaming MCP ecosystem is community-driven and growing fast but lacks official support from major platforms. **Minecraft leads in pure fun factor** — yuniko-software/minecraft-mcp-server (504 stars) lets AI agents control a Minecraft character in real-time via the Mineflayer API, handling movement, building, mining, inventory management, and chat through natural language. **OP.GG provides the richest esports data** — opgginc/opgg-mcp (76 stars, 27 tools) covers League of Legends summoner profiles, champion analytics, counter matchups, TFT meta decks, Valorant agent stats, and esports schedules across three major titles. **Chess has the most implementations for a single game** — four MCP servers cover Chess.com data access (64 stars, 10 tools for player profiles and PGN downloads), engine play (Stockfish analysis, adjustable AI difficulty 1-5), and game state management. **Steam integration exists but is fragmented** — three separate servers cover gaming context (Java), game statistics with 10 tools (JavaScript), and review analysis (TypeScript), but none offers a unified Steam experience. **CS2 RCON is the standout for game server management** — v9rt3x/cs2-rcon-mcp enables natural language control of Counter-Strike 2 servers including RCON commands, workshop map management, and server monitoring. **IGDB provides authoritative game metadata** — bielacki/igdb-mcp-server wraps the Twitch-operated Internet Game Database for searching games, trending titles, and custom queries. **Twitch streaming gets a dedicated server** — mtane0412/twitch-mcp-server offers 13 tools for the Helix API covering channels, streams, clips, emotes, and badges. **Roblox game client interaction** goes beyond development — notpoiu/roblox-mcp (18 tools) enables code execution, script inspection, and remote interception in running Roblox games. **Gaps are significant** — no official MCPs from Steam/Valve, Epic Games, PlayStation, Xbox, or Nintendo; no cross-platform achievement aggregation; no unified esports data beyond OP.GG's three games; no in-game economy or marketplace tools; no game streaming services (Xbox Cloud, GeForce NOW); no game modding workflow servers. The category earns 3.5/5 — creative community implementations with genuine utility for gamers and server administrators, but the absence of any official platform MCPs means the ecosystem is built on reverse-engineered and public APIs."
last_refreshed: 2026-03-16
---

Gaming and esports MCP servers are bringing AI agents into the world of interactive entertainment — from controlling Minecraft characters through natural language to analyzing League of Legends matchups, managing Counter-Strike 2 game servers, and exploring Steam game libraries. Instead of manually navigating game dashboards, checking stats websites, or typing console commands, these servers let AI assistants handle gaming tasks through the Model Context Protocol.

This review covers **gaming and esports MCP servers** — live game interaction (Minecraft, Roblox), esports analytics (OP.GG), Steam integration, chess platforms, game server management (CS2 RCON), game databases (IGDB), and streaming (Twitch). For game engine and development tools (Unity, Unreal, Godot), see our [Game Engine & 3D Development review](/reviews/game-engine-3d-development-mcp-servers/). For Discord bot integration commonly used by gaming communities, see our [Discord MCP review](/reviews/discord-mcp-servers/).

The headline findings: **Minecraft has the highest-starred gaming MCP server** at 504 stars with real-time character control via the Mineflayer API. **OP.GG provides the most comprehensive esports data** with 27 tools across League of Legends, TFT, and Valorant. **Chess has the most MCP implementations for a single game** — four separate servers covering data access, engine play, and game management. **No major gaming platform provides an official MCP server** — everything is community-built on public APIs.

---

## Live Game Interaction

### yuniko-software/minecraft-mcp-server — AI-Controlled Minecraft Bot

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [minecraft-mcp-server](https://github.com/yuniko-software/minecraft-mcp-server) | 504 | TypeScript | — | 15 commands |

**The most popular gaming MCP server** — lets AI agents control a Minecraft character in real-time through the Mineflayer API:

- **Movement and navigation** — walk, fly, and explore the game world
- **Building** — place blocks with support for image-based building instructions
- **Mining** — break blocks and collect resources
- **Inventory management** — organize items and interact with objects
- **Furnace operations** — smelt items automatically
- **Entity detection** — find and interact with mobs and players
- **In-game chat** — communicate with other players
- **Gamemode detection** — adapt behavior based on survival/creative mode

The go-to choice for anyone wanting to experiment with AI agents in sandbox game environments.

### notpoiu/roblox-mcp — Roblox Game Client Interaction

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [roblox-mcp](https://github.com/notpoiu/roblox-mcp) | 18 | JavaScript/Luau | — | 18 |

**Beyond development — this server interacts with running Roblox game clients**, not just the editor:

- **Code execution** and data querying from the game client
- **Script decompilation** and source searching
- **CSS-like instance selection** and hierarchy inspection
- **Remote/Bindable interception** via Cobalt integration
- **Multi-client support** with dashboard
- **Screenshot capture** (Windows)
- **Primary/secondary coordination** with automatic failover

A specialized tool for game analysis, testing, and automation in live Roblox experiences.

---

## Esports Analytics

### opgginc/opgg-mcp — League of Legends, TFT, and Valorant Data

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [opgg-mcp](https://github.com/opgginc/opgg-mcp) | 76 | TypeScript | — | 27 |

**The most comprehensive esports data MCP server**, powered by OP.GG's extensive gaming analytics:

- **League of Legends** — summoner profiles, champion rankings, counter matchups, ban/pick rates, meta statistics, game history, skin sales
- **Teamfight Tactics** — meta decks, item combinations and recipes, champion builds, playstyle insights
- **Valorant** — agent stats, map meta, regional leaderboards, agent compositions, player match history
- **Esports** — LoL match schedules and team standings
- **Field selection syntax** to optimize payload sizes and response efficiency
- **Streamable HTTP transport** for integration with AI agents

The go-to for competitive gaming analysis across Riot Games titles. No API key required — connects to OP.GG's remote server.

---

## Steam Integration

### dsp/mcp-server-steam — Steam API Gaming Context

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [mcp-server-steam](https://github.com/dsp/mcp-server-steam) | 12 | Java | — | — |

**Provides Steam gaming context to AI assistants** by integrating with the Steam API to fetch user gaming information. Java-based with Docker support and Maven build system.

### algorhythmic/steam-mcp — Steam Web API Game Statistics

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [steam-mcp](https://github.com/algorhythmic/steam-mcp) | 4 | JavaScript | — | 10 |

**Structured access to Steam game data** through 10 tools:

- **getCurrentPlayers** — active player count for any game
- **getPlayerAchievements** — achievement unlock status per user
- **getUserStatsForGame** — detailed user statistics
- **getGameSchema** — game configuration and achievement definitions
- **getGameNews** — latest news for any Steam title
- **getGlobalAchievementPercentages** — community-wide completion rates
- **getAppDetails** — store information and metadata

Useful for game researchers, content creators, or anyone tracking gaming trends.

### fenxer/steam-review-mcp — Steam Review Analysis

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [steam-review-mcp](https://github.com/fenxer/steam-review-mcp) | 5 | TypeScript | — | 1 |

**Focused review analysis** — retrieves game reviews with positive/negative counts, review scores, and review content. Includes pre-built prompts for `summarize-reviews` and `recent-reviews-analysis`, useful for understanding game sentiment before purchase.

---

## Chess

### pab1it0/chess-mcp — Chess.com Data Access

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [chess-mcp](https://github.com/pab1it0/chess-mcp) | 64 | Python | — | 10 |

**The most-starred chess MCP server** — provides access to Chess.com's published data API:

- **Player profiles** and statistics retrieval
- **Game history search** and PGN downloads
- **Online status** verification
- **Club information** and membership access
- **No authentication required** — public API only
- Docker containerization support
- Configurable tool availability for MCP clients

The best option for analyzing Chess.com player data and game records.

### arvid-berndtsson/Chess-MCP — Play Chess Against AI

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [Chess-MCP](https://github.com/arvid-berndtsson/Chess-MCP) | — | TypeScript | — | 12 |

**A complete chess engine built as an MCP server** with 12 tools:

- **Multiple game modes** — human vs. human, human vs. AI, AI vs. AI
- **Adjustable difficulty** (levels 1-5) using minimax with alpha-beta pruning
- **Position analysis** and move suggestions
- **FEN and PGN support** for game import/export
- **Full rules implementation** including castling, en passant, pawn promotion
- **Transposition tables** for 2-5x performance improvement

### Other Chess Servers

- **turlockmike/chess-mcp** — Stockfish-powered position analysis and professional evaluations
- **danilop/chess-support-mcp** — game state management designed for LLMs, intentionally without move suggestions to let the AI reason about positions

---

## Game Server Management

### v9rt3x/cs2-rcon-mcp — Counter-Strike 2 Server Control

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [cs2-rcon-mcp](https://github.com/v9rt3x/cs2-rcon-mcp) | 9 | Python | — | 5 |

**Natural language control of CS2 game servers** via RCON:

- **RCON command execution** — run any server command
- **Server status** monitoring
- **Workshop map management** — host, list, and change workshop maps
- **SSE-based communication** architecture
- **Docker support** and integration with GitHub Copilot and Cursor

The only game server management MCP we found — a practical tool for CS2 community server administrators.

---

## Game Databases

### bielacki/igdb-mcp-server — Internet Game Database

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [igdb-mcp-server](https://github.com/bielacki/igdb-mcp-server) | 3 | Python | — | 4 |

**Access the Twitch-operated IGDB** — the authoritative video game metadata database:

- **Search games** with full IGDB API access
- **Game details** — comprehensive metadata for any title
- **Most anticipated games** — trending and upcoming releases
- **Custom queries** using the Apicalypse query language
- Smart OAuth token caching
- Pydantic-based type safety

### moonolgerd/game-mcp — Multi-Platform Game Discovery

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [game-mcp](https://github.com/moonolgerd/game-mcp) | — | C# | — | 3 |

**Discovers installed games across platforms** on Windows:

- **Multi-platform scanning** — Steam, Epic Games, GOG, Xbox/Windows Store, EA, Ubisoft Connect, Rockstar, Battle.Net
- **Game metadata** — name, platform, install path, executable, install date, size
- **Game launching** with explicit user confirmation
- Read-only security model

---

## Streaming Platforms

### mtane0412/twitch-mcp-server — Twitch Helix API

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [twitch-mcp-server](https://github.com/mtane0412/twitch-mcp-server) | 1 | TypeScript | — | 13 |

**Comprehensive Twitch API integration** via the Helix API:

- **Channel information** — get channel details and broadcaster data
- **Stream discovery** — find live streams filtered by game and language
- **Game search** — discover games and categories
- **User profiles** — access user data
- **Content management** — clips, videos, comments
- **Chat utilities** — emotes, badges, chat settings

---

## What's Missing

The gaming MCP ecosystem has notable gaps:

- **No official platform MCPs** — Steam/Valve, Epic Games, PlayStation Network, Xbox Live, and Nintendo have no official MCP servers
- **No cross-platform achievement tracking** — no server aggregates achievements across Steam, PlayStation, Xbox
- **Limited esports coverage** — OP.GG covers three Riot Games titles, but no servers for Dota 2, CS2 competitive stats, Fortnite, or Overwatch
- **No in-game economy tools** — no servers for Steam Marketplace, game trading, or virtual item management
- **No cloud gaming services** — Xbox Cloud Gaming, GeForce NOW, and PlayStation Now have no MCP presence
- **No game modding workflows** — despite the massive modding community, no servers for Nexus Mods, Steam Workshop, or CurseForge
- **No retro gaming** — no emulator integration, ROM management, or retro game database servers

---

## The Bottom Line

The gaming MCP ecosystem earns **3.5 out of 5**. There's genuine creativity here — controlling a Minecraft bot through natural language is a compelling demonstration of what MCP can do, and OP.GG's 27-tool esports server shows how gaming data APIs can be effectively wrapped for AI consumption. Chess has surprisingly strong coverage with four independent implementations. Steam integration exists but is fragmented across three separate servers.

The biggest limitation is the complete absence of official platform support. Every server in this category is community-built on public or reverse-engineered APIs, which means they're subject to breaking changes and rate limits. When (not if) major gaming platforms launch official MCP servers, this category will transform dramatically.

For game *development* tools (Unity, Unreal Engine, Godot, Roblox Studio), see our [Game Engine & 3D Development review](/reviews/game-engine-3d-development-mcp-servers/).

*Last updated: March 2026*

*This review was last edited on 2026-03-16 using Claude Opus 4.6 (Anthropic).*
