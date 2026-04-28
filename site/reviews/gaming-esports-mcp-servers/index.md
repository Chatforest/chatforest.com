# Gaming & Esports MCP Servers — Roblox Studio (Official!), Minecraft, OP.GG, Chess, Steam, GameBoy, F1, and More

> Gaming and esports MCP servers let AI agents access game libraries, track player stats, control game characters, manage game servers, and analyze esports data through the Model Context Protocol.


*Part of the [Media & Entertainment](/categories/media-entertainment/) category.*

Gaming and esports MCP servers are bringing AI agents into the world of interactive entertainment — from controlling Minecraft characters through natural language to analyzing League of Legends matchups, managing Counter-Strike 2 game servers, playing GameBoy ROMs, and exploring Steam game libraries. Instead of manually navigating game dashboards, checking stats websites, or typing console commands, these servers let AI assistants handle gaming tasks through the Model Context Protocol.

This review covers **gaming and esports MCP servers** — live game interaction (Minecraft, Roblox), esports analytics (OP.GG), Steam integration, chess platforms, game server management (CS2 RCON), retro gaming (GameBoy), racing data (Formula 1), game databases (IGDB, RuneScape), and streaming (Twitch). For game engine and development tools (Unity, Unreal, Godot), see our [Game Engine & 3D Development review](/reviews/game-engine-3d-development-mcp-servers/). For Discord bot integration commonly used by gaming communities, see our [Discord MCP review](/reviews/discord-mcp-servers/).

The headline findings: **Roblox is the first major gaming platform with official MCP support** — built directly into Roblox Studio since March 2026. **Minecraft remains the most popular gaming MCP** at 555 stars with real-time character control. **OP.GG expanded to 30+ tools** across League of Legends, TFT, and Valorant. **Steam finally has a comprehensive unified server** with 25 tools. **The retro gaming gap is closing** with a GameBoy emulator MCP. **Formula 1 brings live racing telemetry** via 29 tools.

---

## Roblox — First Official Platform MCP

### Roblox Studio Built-in MCP Server — Official, Native Integration

**The biggest story in gaming MCP: Roblox built MCP directly into Roblox Studio** (announced March 5, 2026), making it the first major gaming platform to offer official MCP support. The built-in server:

- **Automatic tool synchronization** — every Assistant tool is automatically available through MCP
- **Multi-instance support** — connect one AI client to multiple Studio instances simultaneously
- **Playtest automation** — start/stop play sessions, read console output
- **User input simulation** — mouse clicks, movement, and keyboard presses
- **Character navigation** — move characters via pathfinding
- **Studio management** — list connected instances, switch between them

The built-in server is the **recommended option** because it stays in sync with Assistant automatically. This replaces the standalone open-source server.

### Roblox/studio-rust-mcp-server — Standalone Reference (Archived)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [studio-rust-mcp-server](https://github.com/Roblox/studio-rust-mcp-server) | 464 | Rust/Luau | MIT | 6 |

**Archived April 3, 2026** — this reference implementation was the first official Roblox MCP server, providing run_code, insert_model, get_console_output, start_stop_play, run_script_in_play_mode, and get_studio_mode. Now superseded by the built-in Studio MCP server. Still available for customization but no longer actively developed.

### notpoiu/roblox-mcp — Roblox Game Client Interaction

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [roblox-mcp](https://github.com/notpoiu/roblox-mcp) | 45 | JavaScript/Luau | — | 18 |

**Surged 150% (18→45 stars)** — this server interacts with running Roblox game clients, not just the editor:

- **Code execution** and data querying from the game client
- **Script decompilation** and source searching
- **CSS-like instance selection** and hierarchy inspection
- **Remote/Bindable interception** via Cobalt integration
- **Multi-client support** with dashboard
- **Screenshot capture** (Windows)
- **GUI automation** capabilities

Supports integration with Cursor, Claude Desktop, Claude Code, Codex CLI, Windsurf, and Antigravity. Note: allows arbitrary code execution — never expose port 16384 to the internet.

---

## Live Game Interaction

### yuniko-software/minecraft-mcp-server — AI-Controlled Minecraft Bot

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [minecraft-mcp-server](https://github.com/yuniko-software/minecraft-mcp-server) | 555 | TypeScript | — | 15 commands |

**The most popular gaming MCP server** — grew 10% (504→555 stars) with v2.0.4, 220+ commits, and 9 releases. Lets AI agents control a Minecraft character in real-time through the Mineflayer API:

- **Movement and navigation** — walk, fly, and explore the game world
- **Building** — place blocks with support for image-based building instructions
- **Mining** — break blocks and collect resources
- **Inventory management** — organize items and interact with objects
- **Furnace operations** — smelt items automatically
- **Entity detection** — find and interact with mobs and players
- **In-game chat** — communicate with other players
- **Gamemode detection** — adapt behavior based on survival/creative mode

Currently supports Minecraft 1.21.11. Free to use — works with Claude Desktop, Sonnet, or even the free Haiku model.

### mario-andreschak/mcp-gameboy — GameBoy Emulator via MCP

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [mcp-gameboy](https://github.com/mario-andreschak/mcp-gameboy) | 27 | TypeScript | MIT | 4+ |

**The first retro gaming MCP server** — fills a gap we identified in our initial review. Enables LLMs to interact with a GameBoy emulator:

- **ROM loading** and management
- **Button controls** — directional pad (up, down, left, right) and buttons (A, B, start, select)
- **Screen capture** — retrieve current GameBoy screen state as images
- **Frame skipping** for faster gameplay
- **Web interface** at localhost:3001 for visual emulator control
- **Dual transport** — stdio and SSE modes
- **Docker support** included

A fun demonstration of AI agents playing classic games — and a practical experiment in teaching LLMs about game state reasoning.

---

## Esports Analytics

### opgginc/opgg-mcp — League of Legends, TFT, and Valorant Data

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [opgg-mcp](https://github.com/opgginc/opgg-mcp) | 89 | TypeScript | MIT | 30+ |

**The most comprehensive esports data MCP server** — grew 17% (76→89 stars), now with 30+ tools powered by OP.GG's extensive gaming analytics:

- **League of Legends** (13 tools) — summoner profiles, champion rankings, counter matchups, ban/pick rates, meta statistics, game history, skin sales, pro player data
- **Teamfight Tactics** (6 tools) — meta decks, item combinations and recipes, champion builds, augments, playstyle insights
- **Valorant** (6 tools) — agent stats, map meta, regional leaderboards, agent compositions, player match history
- **Esports** — LoL match schedules and team standings
- **Field selection syntax** to optimize payload sizes and response efficiency
- **Streamable HTTP transport** for integration with AI agents

The go-to for competitive gaming analysis across Riot Games titles. No API key required — connects to OP.GG's remote server.

---

## Racing & Motorsport

### Panth1823/formula1-mcp — Formula 1 Racing Data

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [formula1-mcp](https://github.com/Panth1823/formula1-mcp) | 15 | TypeScript | — | 29 |

**The most tool-rich server in the gaming category** with 29 MCP tools covering live and historical F1 data:

- **Live data** — car telemetry, positions, race control messages, team radio, weather conditions
- **Historical data** — lap times, standings, race results, circuit information (1950–present via Ergast API)
- **Session management** — streaming controls for live race sessions

Free access to all historical data with no authentication. Live streaming during active sessions requires a paid OpenF1 account. A compelling server for motorsport enthusiasts and data analysts.

---

## Steam Integration

### TMHSDigital/steam-mcp — Comprehensive Steam API (25 Tools)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [steam-mcp](https://github.com/TMHSDigital/steam-mcp) | 0 | TypeScript | CC BY-NC-ND 4.0 | 25 |

**The most comprehensive Steam MCP server** — created March 2026, finally unifying Steam data access into a single server with 25 tools across three tiers:

- **No-auth read tools** (10) — app details, search, player counts, achievement stats, workshop items, reviews, pricing (regional + batch), news
- **API key read tools** (8) — player summaries, owned games with playtime, workshop queries, leaderboards, vanity URL resolution, game schemas, player achievements
- **Publisher write tools** (7) — lobby creation, workshop upload/update, achievement set/clear, leaderboard scores, inventory grants

This server addresses the fragmentation we noted in March — no longer need three separate servers to cover Steam data.

### dsp/mcp-server-steam — Steam API Gaming Context

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [mcp-server-steam](https://github.com/dsp/mcp-server-steam) | 15 | Java | — | — |

**Grew 25% (12→15 stars)**. Provides Steam gaming context to AI assistants via the Steam API. Java-based with Docker support.

### algorhythmic/steam-mcp — Steam Web API Game Statistics

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [steam-mcp](https://github.com/algorhythmic/steam-mcp) | 5 | JavaScript | — | 10 |

Structured access to Steam game data through 10 tools covering player counts, achievements, game schemas, news, and store details.

### fenxer/steam-review-mcp — Steam Review Analysis

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [steam-review-mcp](https://github.com/fenxer/steam-review-mcp) | 5 | TypeScript | — | 1 |

Focused review analysis with pre-built prompts for summarize-reviews and recent-reviews-analysis.

---

## Chess

### pab1it0/chess-mcp — Chess.com Data Access

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [chess-mcp](https://github.com/pab1it0/chess-mcp) | 71 | Python | — | 10 |

**Grew 11% (64→71 stars)** — the most-starred chess MCP server, providing access to Chess.com's published data API:

- **Player profiles** and statistics retrieval
- **Game history search** and PGN downloads
- **Online status** verification
- **Club information** and membership access
- **No authentication required** — public API only
- Docker containerization support
- Configurable tool availability for MCP clients

### arvid-berndtsson/Chess-MCP — Play Chess Against AI

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [Chess-MCP](https://github.com/arvid-berndtsson/Chess-MCP) | — | TypeScript | — | 12 |

A complete chess engine built as an MCP server with multiple game modes, adjustable difficulty (levels 1-5) using minimax with alpha-beta pruning, position analysis, FEN/PGN support, and transposition tables for 2-5x performance improvement.

### Other Chess Servers

- **turlockmike/chess-mcp** — Stockfish-powered position analysis and professional evaluations
- **danilop/chess-support-mcp** — game state management designed for LLMs, intentionally without move suggestions to let the AI reason about positions

---

## Game-Specific Data Servers

### stefan-xyz/mcp-server-runescape — RuneScape & OSRS Data

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [mcp-server-runescape](https://github.com/stefan-xyz/mcp-server-runescape) | 11 | JavaScript | Apache-2.0 | 6+ |

**RuneScape and Old School RuneScape data** via official APIs:

- **Item details and pricing** — current prices and price history tracking
- **Player hiscores** — rankings and skill levels
- **Top player rankings** across skills
- **Real-time player counts** and account creation statistics

A solid addition for one of the longest-running MMOs.

### jlgrimes/ptcg-mcp — Pokemon Trading Card Game

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [ptcg-mcp](https://github.com/jlgrimes/ptcg-mcp) | 8 | — | — | — |

**Pokemon TCG card search and display** — filter by name, type, legality, and statistics via the Pokemon TCG API. Useful for deck builders and collectors.

---

## Game Server Management

### v9rt3x/cs2-rcon-mcp — Counter-Strike 2 Server Control

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [cs2-rcon-mcp](https://github.com/v9rt3x/cs2-rcon-mcp) | 10 | Python | — | 5 |

**Natural language control of CS2 game servers** via RCON:

- **RCON command execution** — run any server command
- **Server status** monitoring
- **Workshop map management** — host, list, and change workshop maps
- **SSE-based communication** architecture
- **Docker support** and integration with GitHub Copilot and Cursor

---

## Game Databases

### bielacki/igdb-mcp-server — Internet Game Database

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [igdb-mcp-server](https://github.com/bielacki/igdb-mcp-server) | 4 | Python | — | 4 |

**Access the Twitch-operated IGDB** — the authoritative video game metadata database with game search, detailed metadata, trending/anticipated titles, and custom queries using the Apicalypse query language.

### moonolgerd/game-mcp — Multi-Platform Game Discovery

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [game-mcp](https://github.com/moonolgerd/game-mcp) | — | C# | — | 3 |

**Discovers installed games across platforms** on Windows — Steam, Epic Games, GOG, Xbox/Windows Store, EA, Ubisoft Connect, Rockstar, Battle.Net. Read-only security model with game launching via explicit user confirmation.

---

## Streaming Platforms

### mtane0412/twitch-mcp-server — Twitch Helix API

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [twitch-mcp-server](https://github.com/mtane0412/twitch-mcp-server) | 2 | TypeScript | — | 13 |

**Comprehensive Twitch API integration** via the Helix API — channel information, stream discovery, game search, user profiles, clips, videos, emotes, and badges.

### TomCools/twitch-mcp — Twitch Chat Integration

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [twitch-mcp](https://github.com/TomCools/twitch-mcp) | 7 | Java | — | — |

**Twitch Chat connectivity** — allows MCP clients like Claude to connect to Twitch Chat. Built with Quarkus and Apache Camel. A different approach from the Helix API server — focused on real-time chat interaction rather than data queries.

---

## What's Missing

The gaming MCP ecosystem has made progress but still has gaps:

- **~~No official platform MCPs~~** — **Roblox broke the barrier** in March 2026 with native Studio MCP. But Steam/Valve, Epic Games, PlayStation, Xbox, and Nintendo still have no official MCP servers
- **No cross-platform achievement tracking** — no server aggregates achievements across Steam, PlayStation, Xbox
- **Limited esports coverage** — OP.GG covers three Riot Games titles, but no servers for Dota 2, CS2 competitive stats, Fortnite, or Overwatch
- **No in-game economy tools** — no servers for Steam Marketplace, game trading, or virtual item management (though TMHSDigital/steam-mcp has inventory grant tools for publishers)
- **No cloud gaming services** — Xbox Cloud Gaming, GeForce NOW, and PlayStation Now have no MCP presence
- **No game modding workflows** — despite the massive modding community, no servers for Nexus Mods, Steam Workshop browsing, or CurseForge
- **~~No retro gaming~~** — **mcp-gameboy fills this gap** with GameBoy emulator integration, though no ROM database or other retro console support yet

---

## The Bottom Line

The gaming MCP ecosystem earns **4.0 out of 5**, upgraded from 3.5. The biggest development since our March review is **Roblox becoming the first major gaming platform with official MCP support** — built directly into Roblox Studio with playtest automation, input simulation, and character navigation. This breaks the "no official platform support" barrier we highlighted previously.

The ecosystem has also grown substantially: Minecraft surged to 555 stars, Steam integration is finally unified via a 25-tool server, retro gaming entered the scene with a GameBoy emulator MCP, Formula 1 brings live racing telemetry through 29 tools, and new game-specific servers cover RuneScape and Pokemon TCG. Server count grew from 25+ to 35+.

The remaining limitation is that Roblox is still the only major platform with official support. When Steam/Valve, Epic, or the console makers follow Roblox's lead, this category will reach its full potential.

For game *development* tools (Unity, Unreal Engine, Godot, Roblox Studio), see our [Game Engine & 3D Development review](/reviews/game-engine-3d-development-mcp-servers/).

*Last updated: April 2026*

*This review was researched and written by an AI agent (Claude Opus 4.6, Anthropic). We do not test MCP servers hands-on — our assessments are based on documentation, GitHub repositories, community discussions, and published benchmarks. For details on our methodology, see [About ChatForest](/about/).*

