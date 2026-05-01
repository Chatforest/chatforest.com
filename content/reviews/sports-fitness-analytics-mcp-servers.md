---
title: "Sports & Fitness Analytics MCP Servers — Live Scores, F1 Telemetry, Betting Odds, Strava, Garmin, and Workout Tracking"
date: 2026-03-16T23:00:00+09:00
description: "Sports and fitness analytics MCP servers let AI agents access live scores, race telemetry, betting odds, workout data, and fitness tracking through the Model Context Protocol."
og_description: "Sports & fitness analytics MCP servers: Sportradar OFFICIAL (20+ sport profiles), r-huijts/strava-mcp (368 stars, 25 tools), Open Wearables (1.5K stars, 6+ ecosystems), F1 servers (6+ implementations), Flaim fantasy (ESPN+Yahoo+Sleeper), garmin-connect-mcp (120 stars, 61 tools), OP.GG esports. 35+ servers reviewed. Rating: 4.5/5."
content_type: "Review"
card_description: "Sports and fitness analytics MCP servers for live scores, Formula 1 telemetry, betting odds, Strava integration, Garmin health data, fantasy sports, and workout tracking through AI assistants. This is one of the most vibrant MCP categories — the combination of publicly available sports APIs and the fitness tracking ecosystem has produced a rich and rapidly growing set of servers. **Sportradar launched an official MCP server in February 2026** with 20+ sport-specific profiles covering tennis, golf, cricket, rugby, and more — partially closing what was the biggest gap in this category. **Formula 1 stands out with 6+ independent implementations**, driven by FastF1 and OpenF1 APIs. **Strava dominates the endurance space** with r-huijts/strava-mcp surging to 368 stars and 25 tools. **Open Wearables has emerged as the unified fitness platform** at 1.5K stars, connecting Garmin, Polar, Suunto, Apple HealthKit, Samsung Health, and Google Health Connect through a single self-hosted API with built-in MCP server. **The Garmin Connect MCP server has 120 stars** with 61 tools spanning health, fitness, and activity data. **Fantasy sports — previously absent — now has real coverage** with Flaim connecting ESPN, Yahoo, and Sleeper leagues to AI assistants across football, baseball, basketball, and hockey. **Esports coverage is improving** with OP.GG's official LoL esports MCP server. **Sports betting remains strong** with BetTrack, Wagyu Sports, and Cloudbet. **Oura Ring has exploded** from 1 to 6+ MCP server implementations, though a trojanized Oura MCP server deploying StealC infostealer was discovered in February 2026 — a security wake-up call for the fitness MCP ecosystem. The category earns 4.5/5 — Sportradar's official launch, the Open Wearables unification platform, fantasy sports arrival, and Strava's community growth all represent significant maturation since the initial review."
last_refreshed: 2026-05-02
next_priority: med
categories: ["/categories/sports-fitness/"]
---

Sports and fitness analytics MCP servers connect AI agents to live scores, race telemetry, betting odds, workout data, and fitness tracking platforms. Instead of manually checking scores, switching between fitness apps, or browsing betting lines, these servers let you query sports data through natural language via the Model Context Protocol.

This review covers **sports data, fitness analytics, and workout management** — live scores, F1 racing, sports betting, Strava/Garmin integration, fantasy sports, and exercise tracking. For mental health and wellness tracking, see our [Mental Health & Wellness review](/reviews/mental-health-wellness-mcp-servers/). For wearable device data beyond fitness, see our [Wearables & Quantified Self review](/reviews/fitness-wearables-mcp-servers/) if available.

The headline findings: **Sportradar launched an official MCP server** with 20+ sport profiles covering tennis, cricket, golf, rugby, and more. **Formula 1 has the deepest coverage of any single sport** with 6+ independent implementations. **Strava leads the fitness space** — r-huijts/strava-mcp surged to 368 stars with 25 tools. **Open Wearables (1.5K stars) unifies 6+ wearable ecosystems** with a built-in MCP server. **Garmin Connect MCP has 120 stars** with 61 tools. **Fantasy sports — previously absent — now has real coverage** via Flaim (ESPN+Yahoo+Sleeper). **Esports is improving** with OP.GG's official LoL MCP. **A trojanized Oura MCP server** deploying malware was discovered in February 2026 — verify your sources.

---

## Multi-Sport Data Platforms

### Sportradar MCP Server — Official Sports Data Provider *(NEW — February 2026)*

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [Sportradar MCP](https://developer.sportradar.com/getting-started/docs/mcp-server) | — | — | Commercial | 20+ profiles |

**Sportradar — one of the world's largest sports data providers — launched an official MCP server on February 11, 2026:**

- **20+ sport-specific profiles** — football, soccer, basketball, tennis, cricket, golf, rugby, hockey, MMA, racing, volleyball, darts, snooker, squash, table tennis, handball, futsal, field hockey, and more
- **Structured API access** — endpoints, parameters, schemas, authentication details, and code snippets
- **AI tool integration** — works with Cursor, Windsurf, Claude, Codex, and other AI development platforms
- **Developer Portal integration** — connects directly to Sportradar's comprehensive API documentation

This is a significant development for the sports MCP ecosystem. Sportradar's coverage of individual sports like tennis, golf, cricket, and rugby partially closes what was the biggest gap in this category. Note: this is primarily a developer documentation MCP server for building Sportradar API integrations, not a direct data access server — you still need a Sportradar API key for actual sports data.

### michaelfromorg/mcp-sports — ESPN-Based Real-Time Sports

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [mcp-sports](https://github.com/michaelfromorg/mcp-sports) | — | TypeScript | — | Multiple |

**Real-time sports data powered by ESPN:**

- **Multi-league coverage** — NFL, NBA, MLB, NHL, NCAA Football, NCAA Basketball, Premier League
- **Live scores and standings** — current game states, league tables, team records
- **Schedules and team info** — upcoming games, rosters, team details
- **Fantasy and betting context** — data useful for fantasy analysis and betting decisions

A solid general-purpose sports data server for major North American leagues plus Premier League soccer.

### SportDB.dev — Free Sports API + MCP Server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [SportDB.dev](https://sportdb.dev) | — | — | — | Multiple |

**A free REST API and MCP server for sports data:**

- **Live scores and fixtures** — real-time match data across major leagues
- **Standings and player profiles** — league tables, transfer information
- **Multi-sport coverage** — football, basketball, tennis, hockey, and more
- **Dual access** — both REST API and MCP server for flexible integration

Useful as a free alternative to paid sports data APIs.

### Apify ESPN MCP Servers — Scraped ESPN Data

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [ESPN MCP Server](https://apify.com/mrbridge/espn-mcp-server) | — | — | — | 12 |

**Multiple Apify actors exposing ESPN data as MCP servers:**

- **12 specialized tools** — scores, standings, team info, rosters, schedules, game analysis, betting odds, athlete profiles, rankings, news, live scoreboards
- **No ESPN API key required** — scrapes publicly available data
- **Sport-specific variants** — separate actors for NBA stats, general ESPN scraping
- **AI-optimized formatting** — structured results designed for LLM consumption

Commercial Apify platform, but provides comprehensive ESPN coverage through scraping.

### cloudbet/sports-mcp-server — Live Betting Markets

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [sports-mcp-server](https://github.com/cloudbet/sports-mcp-server) | 10 | TypeScript | — | 1 |

**Cloudbet's official MCP server for live sports and betting data:**

- **Fuzzy competition search** — natural-language queries mapped to live market data
- **Multi-sport coverage** — soccer, basketball, tennis, esports, and more
- **Live odds and markets** — upcoming events with primary market data
- **Single-tool design** — `findEventsAndMarketsByCompetition` handles all queries

A minimal but functional implementation. Primarily educational/demo purpose, but connects to real live data.

---

## Formula 1 Racing

F1 has remarkably strong MCP representation — more independent server implementations than almost any other single sport domain.

### rakeshgangwar/f1-mcp-server — FastF1 Data Access

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [f1-mcp-server](https://github.com/rakeshgangwar/f1-mcp-server) | 7 | Python | — | 7 |

**Formula One racing data via the FastF1 Python library:**

- **Race calendar** — get event schedules for any season
- **Grand Prix details** — detailed information about specific events
- **Session results** — qualifying, sprint, race results
- **Driver analysis** — performance analysis for specific sessions
- **Driver comparison** — compare multiple drivers' performance head-to-head
- **Telemetry data** — speed, throttle, brake, gear data for specific laps
- **Championship standings** — driver and constructor standings

Well-structured with 7 distinct tools. FastF1 is a respected library in the F1 data community.

### Panth1823/formula1-mcp — TypeScript F1 Data

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [formula1-mcp](https://github.com/Panth1823/formula1-mcp) | — | TypeScript | — | Multiple |

**TypeScript-based F1 server with real-time and historical data:**

- **Real-time data** — live timing and session information
- **Historical records** — past race results, championship data
- **TypeScript implementation** — alternative to Python-based servers for JS ecosystems

### stagsz/F1-MCP-Server — Live Timing & Simulation

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [F1-MCP-Server](https://github.com/stagsz/F1-MCP-Server) | — | — | — | Multiple |

**Comprehensive F1 data with advanced features:**

- **Live timing** — real-time telemetry processing during sessions
- **Race analysis** — post-race performance breakdowns
- **Race simulation** — strategy simulation features
- **The most feature-rich F1 MCP server** — goes beyond data retrieval into analysis

### Other F1 Implementations

Several additional F1 MCP servers exist:

- **[Machine-To-Machine/f1-mcp-server](https://github.com/Machine-To-Machine/f1-mcp-server)** — event schedules, driver info, telemetry, race results, championship standings
- **[Darakhsh1999/f1-mcp-server](https://github.com/Darakhsh1999/f1-mcp-server)** — FastF1 + OpenF1 API, Gradio-based framework
- **[AryaAkman/Open-F1-MCP-Server](https://github.com/AryaAkman/Open-F1-MCP-Server)** — OpenF1 API access
- **[AbhiJ2706/f1-mcp](https://github.com/AbhiJ2706/f1-mcp)** — another F1 data implementation

The abundance of F1 servers likely reflects both the excellent open APIs (FastF1, OpenF1) and the data-heavy nature of motorsport — F1 generates more telemetry data per race than most sports generate in a season.

---

## Sports Betting

### WFord26/BetTrack — Comprehensive Betting Analytics

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [BetTrack](https://github.com/WFord26/BetTrack) | — | Python | — | 30+ |

**A full-featured sports betting MCP server with dashboard:**

- **30+ MCP tools** — extensive query capabilities for odds and scores
- **70+ betting markets** — game lines, player props across NFL, NBA, NHL, MLB
- **Live scores and schedules** — ESPN data integration alongside betting data
- **React dashboard** — optional web app for bet tracking and analytics
- **Line movement visualization** — track how odds change over time
- **Futures betting** — long-term market tracking
- **PostgreSQL backend** — persistent bet history and analytics

The most comprehensive sports betting MCP server available. Requires an Odds API key and Node.js 20+ for the dashboard.

### Wagyu Sports / The Odds API MCP *(NEW)*

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [wagyu-sports](https://playbooks.com/mcp/hrgarber-wagyu-sports) | — | — | — | Multiple |

**Structured access to The Odds API for sports betting data:**

- **Available sports listing** — query which sports currently have active odds
- **Odds comparison** — compare lines across bookmakers
- **API quota tracking** — monitor usage in both test and live modes
- **Multi-bookmaker coverage** — aggregated odds from major sportsbooks

### Apify Sportsbook Odds Scraper

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [Sportsbook Odds Scraper](https://apify.com/harvest/sportsbook-odds-scraper/api/mcp) | — | — | — | Multiple |

**Scrapes betting odds from sportsbooks via Apify:**

- **Multi-sportsbook scraping** — aggregates odds from multiple sources
- **MCP server exposure** — access scraped data through the Model Context Protocol
- **Commercial platform** — runs on Apify infrastructure

---

## Strava & Endurance Sports

### r-huijts/strava-mcp — The Leading Strava Integration

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [strava-mcp](https://github.com/r-huijts/strava-mcp) | 368 *(was 238)* | TypeScript | — | 25 |

**The most popular Strava MCP server with 25 tools for the full API:**

- **Activity data** — recent activities, detailed activity streams (power, heart rate, cadence, GPS)
- **Segment exploration** — view, star, and manage Strava segments
- **Route management** — list routes, view details, export GPX/TCX files
- **Compact format** — get-activity-streams reduces payload size by 70-80%
- **Smart chunking** — large activities split into ~50KB chunks with optional downsampling
- **Full Strava API v3** — comprehensive coverage of the Strava ecosystem
- **npm package** — `@r-huijts/strava-mcp-server` for easy installation

At 368 stars (+55% since March), this is one of the fastest-growing sports MCP servers. Essential for runners, cyclists, and triathletes who use Strava.

### MariyaFilippova/mcp-strava — Kotlin/Java Strava MCP *(NEW)*

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [mcp-strava](https://github.com/MariyaFilippova/mcp-strava) | — | Kotlin | — | Multiple |

**A JVM-based Strava MCP server (v2.1.0) with advanced analytics:**

- **Month-over-month comparison** — compare activity data between any two months (e.g., Jan 2025 vs Jan 2026)
- **Heart rate data** — detailed HR streams and analysis
- **Full data streams** — HR, pace, altitude, cadence, power, and GPS
- **Lap splits** — per-lap breakdown of activities
- **Route suggestions** — find popular Strava segments nearby
- **JAR deployment** — runs as a Java application, alternative to Node.js-based servers

A good option for teams already running JVM infrastructure who want Strava integration without a Node.js dependency.

### Other Strava Implementations

- **[tomekkorbak/strava-mcp-server](https://github.com/tomekkorbak/strava-mcp-server)** — Strava API integration for querying athlete activities
- **[yorrickjansen/strava-mcp](https://github.com/yorrickjansen/strava-mcp)** — another Strava interaction server
- **[strava-activity-mcp-server](https://pypi.org/project/strava-activity-mcp-server/)** — Python package on PyPI (v0.3.2, January 2026)
- **[Zapier Strava MCP](https://zapier.com/mcp/strava)** — no-code Strava integration through Zapier's MCP platform
- **[Pipedream Strava MCP](https://mcp.pipedream.com/app/strava)** — Strava MCP via Pipedream's managed infrastructure

---

## Fitness Tracking & Wearables

### gesteves/domestique — Unified Fitness Platform

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [domestique](https://github.com/gesteves/domestique) | — | TypeScript | — | Multiple |

**Unified access to Intervals.icu, Whoop, and TrainerRoad:**

- **Daily snapshots** — recovery, sleep, HRV, strain, fitness metrics (CTL/ATL/TSB), wellness, completed workouts with Whoop data, planned workouts
- **Athlete profiles** — sport-specific settings, FTP, training zones for cycling/running/swimming
- **Power curve analysis** — best watts at various durations with W/kg and estimated FTP
- **Pace curve analysis** — running/swimming best times at key distances
- **Recovery and wellness trends** — longitudinal tracking across platforms
- **Docker deployment** — Docker Compose with hot reload for development

A sophisticated server for serious endurance athletes who use multiple platforms. The three-platform integration (Intervals.icu + Whoop + TrainerRoad) is uniquely valuable.

### Nicolasvegam/garmin-connect-mcp — 61 Garmin Tools

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [garmin-connect-mcp](https://github.com/Nicolasvegam/garmin-connect-mcp) | 120 | TypeScript | — | 61 |

**Remarkably comprehensive access to Garmin Connect data:**

- **61 tools across 7 categories** — activities, daily health, trends, sleep, body composition, performance/training, and profile/devices
- **Health data** — heart rate, sleep, stress, body composition, hydration
- **Activity data** — workouts, steps, calories, active minutes
- **Device management** — Garmin device information and settings
- **Training metrics** — training status, load, recovery, VO2 max
- **Multi-platform support** — Claude Code, Claude Desktop, Cursor, and Windsurf

At 120 stars, this server exposes essentially your entire Garmin Connect dashboard to AI analysis.

### Async-IO/pierre_mcp_server — 150+ Wearable Aggregator

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [pierre_mcp_server](https://github.com/Async-IO/pierre_mcp_server) | — | Python | — | Multiple |

**Fitness intelligence platform connecting 150+ wearables:**

- **Multi-platform** — Strava, Garmin, Fitbit, WHOOP, COROS, and 150+ wearables via Terra
- **Training load management** — monitor and optimize training intensity
- **Race predictions** — estimate finish times based on training data
- **Sleep and recovery scoring** — aggregate recovery metrics
- **Nutrition planning** — integrate nutrition with training
- **Pattern detection** — AI-powered identification of training patterns
- **Protocol support** — MCP, A2A, OAuth 2.0, and REST APIs

The broadest wearable integration available. Uses Terra as an aggregation layer to connect to a vast array of devices.

### the-momentum/open-wearables — Unified Wearable Health Platform *(NEW)*

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [open-wearables](https://github.com/the-momentum/open-wearables) | 1,500 | Python/TypeScript | MIT | Multiple |

**The largest open-source wearable health data unification platform, with built-in MCP server:**

- **6+ wearable ecosystems** — Garmin, Polar, Suunto (cloud-based), plus Apple HealthKit, Samsung Health, Google Health Connect (mobile SDK)
- **Built-in MCP server** — added in v0.3 (February 2026), connects wearable data to Claude, ChatGPT, and other AI assistants
- **Self-hosted** — full data control with FastAPI backend, PostgreSQL, Redis, Celery
- **Health Insights & Automations** — natural language conditions for health-triggered actions
- **Mobile Sync SDKs** — iOS, Android, Flutter, and React Native
- **Developer portal** — user and API key management
- **v0.5.0** (April 29, 2026) — latest release, Product Hunt launch

At 1,500 stars and 237 forks, Open Wearables is the fastest-growing project in the fitness MCP space. The self-hosted model with MIT license makes it attractive for developers who want wearable data unification without third-party dependencies. Oura Ring, Fitbit, and Google Fit integrations are on the roadmap.

### ai-endurance/mcp — AI Endurance Training

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [AI Endurance MCP](https://github.com/ai-endurance/mcp) | — | — | — | Multiple |

**AI-powered training plans for endurance athletes:**

- **Training plans** — personalized plans for running, cycling, triathlon
- **Activity history** — analyze past workout data
- **Performance predictions** — estimate future capabilities
- **Recovery metrics** — monitor readiness and fatigue
- **Training zones** — personalized heart rate and power zones

A remote MCP server focused on the coaching/planning side of endurance sports rather than raw data access.

### ewongz/fitness-mcp-server — Broad Sport Coverage

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [fitness-mcp-server](https://github.com/ewongz/fitness-mcp-server) | — | — | — | Multiple |

**Fitness analytics spanning 30+ sport types:**

- **30+ sports** — cycling, running, swimming, triathlon, walking, hiking, cross-training, and more
- **Power curve analysis** — detailed power output analytics
- **Workout analysis** — individual session breakdowns
- **Wellness tracking** — comprehensive health metrics

### Oura Ring MCP Servers — Rapid Ecosystem Growth

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [tomekkorbak/oura-mcp-server](https://github.com/tomekkorbak/oura-mcp-server) | 37 | — | — | Multiple |
| [daveremy/oura-mcp](https://github.com/daveremy/oura-mcp) | — | — | — | Multiple |
| [mitchhankins01/oura-ring-mcp](https://github.com/mitchhankins01/oura-ring-mcp) | — | — | — | Multiple |

**Oura Ring has gone from 1 to 6+ MCP server implementations since March:**

- **tomekkorbak/oura-mcp-server** (37 stars) — the original, sleep/readiness/activity data
- **daveremy/oura-mcp** — standalone CLI + MCP server + Claude Code skill, covers sleep, readiness, activity, heart rate, stress, SpO2, workouts, and sessions via Oura API v2
- **mitchhankins01/oura-ring-mcp** — human-readable insights about sleep, readiness, and activity with smart analysis tools
- **rajvirtual/oura-mcp-server**, **elizabethtrykin/oura-mcp**, **hemantkamalakar/oura-mcp-server**, **meimakes/oura-mcp-server** — additional implementations

**⚠ Security warning:** In February 2026, threat actors created a trojanized Oura MCP server (SmartLoader attack) that deployed the StealC infostealer. The attackers built fake GitHub forks and contributor profiles to manufacture credibility. **Always verify you are installing from a legitimate, well-known repository** — check stars, commit history, and contributor profiles before trusting any health data MCP server.

---

## Workout Management

### chrisdoc/hevy-mcp — Hevy Workout App Integration

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [hevy-mcp](https://github.com/chrisdoc/hevy-mcp) | — | — | — | Multiple |

**Manage workouts through the Hevy fitness app:**

- **Workout sessions** — create and update workout sessions
- **Routines** — manage workout routines and templates
- **Exercise templates** — search and browse exercises
- **Folders** — organize workout plans
- **Sync** — stay up to date with changes in the Hevy app

Also available as [meimakes/hevy-mcp-server](https://github.com/meimakes/hevy-mcp-server) — a second implementation. Additional implementations from [jcjiron](https://glama.ai/mcp/servers/jcjiron/hevy-mcp), [zachsai](https://glama.ai/mcp/servers/zachsai/hevy-mcp), and [SrdjanCodes](https://glama.ai/mcp/servers/SrdjanCodes/hevy-mcp) have appeared. As of v1.18.0, the main hevy-mcp supports stdio transport only (HTTP/SSE removed).

### Juxsta/wger-mcp — Open Source Workout Manager

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [wger-mcp](https://github.com/Juxsta/wger-mcp) | — | — | — | Multiple |

**Connect AI assistants to the wger fitness API:**

- **400+ exercises** — comprehensive exercise database
- **Workout routines** — create and manage workout plans
- **Nutrition tracking** — food logging and nutritional data
- **Open source** — based on the wger open-source fitness platform

### Other Workout Servers

- **[idjohnson/workoutMakerMCP](https://github.com/idjohnson/workoutMakerMCP)** — generates workout content with Markdown exercise pages and step-by-step instructions
- **[Dinesh-Satram/fitness_coach_MCP](https://github.com/Dinesh-Satram/fitness_coach_MCP)** — AI fitness coaching with MCP-enabled data interaction

---

## Fantasy Sports *(NEW — Previously a Major Gap)*

Fantasy sports management was entirely absent in the March review. That gap has been substantially closed.

### jdguggs10/flaim — Multi-Platform Fantasy Sports *(NEW)*

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [flaim](https://github.com/jdguggs10/flaim) | 5 | — | — | 9 |

**The first comprehensive fantasy sports MCP platform, connecting three major league providers to AI:**

- **ESPN** — Football, Baseball, Basketball, Hockey (via Chrome extension or manual cookies)
- **Yahoo** — Football, Baseball, Basketball, Hockey (OAuth 2.0)
- **Sleeper** — Football, Basketball (username authentication)
- **9 MCP tools** — query your actual team, matchup, standings, and waiver wire
- **Read-only** — no trades, drops, or roster changes — advisory only
- **Multi-AI support** — works with ChatGPT, Claude, and Gemini CLI
- **v1.0.1** (March 12, 2026) — first stable release

The arrival of Flaim closes one of the most conspicuous gaps in the sports MCP space. Fantasy football alone has over 60 million players in the US — this was overdue.

### Yahoo Fantasy MCP Servers *(NEW)*

Multiple Yahoo Fantasy MCP implementations have appeared:

- **[derekrbreese/fantasy-football-mcp-public](https://github.com/derekrbreese/fantasy-football-mcp-public)** — Yahoo Fantasy Football with lineup optimization, draft assistance, and league management
- **[spilchen/yahoo_fantasy_mcp](https://github.com/spilchen/yahoo_fantasy_mcp)** — Yahoo Fantasy League MCP server
- **[cketcham/fantasy-football-mcp](https://github.com/cketcham/fantasy-football-mcp)** — another Yahoo Fantasy Football implementation with advanced features
- **[jimbrig/yahoo-fantasy-baseball-mcp](https://github.com/jimbrig/yahoo-fantasy-baseball-mcp)** — Yahoo Fantasy Sports API for baseball
- **[league-analysis-mcp-server](https://pypi.org/project/league-analysis-mcp-server/)** — PyPI package with historical analysis and manager profiling

### Fantasy Premier League *(NEW)*

- **[rishijatia/fantasy-premier-league](https://www.pulsemcp.com/servers/rishijatia-fantasy-premier-league)** — Fantasy Premier League data via MCP

---

## Niche Sports

### Soccer-Specific Servers

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [mcp-soccer-data](https://github.com/yeonupark/mcp-soccer-data) | — | — | — | Multiple |

- **[yeonupark/mcp-soccer-data](https://github.com/yeonupark/mcp-soccer-data)** — real-time football data via SoccerDataAPI, match information
- **[obinopaul/api-football](https://www.pulsemcp.com/servers/obinopaul-api-football)** — API-Football bridge for league standings, team fixtures, player statistics, live match info

### Chess

Multiple chess MCP servers exist:

- **[pab1it0/chess-mcp](https://github.com/pab1it0/chess-mcp)** — Chess.com Published Data API, player data, game records, search and analysis
- **[turlockmike/chess-mcp](https://github.com/turlockmike/chess-mcp)** — various chess functionality
- **[arvid-berndtsson/Chess-MCP](https://github.com/arvid-berndtsson/Chess-MCP)** — Stockfish chess engine, position analysis, play against AI
- **[alexandreroman/mcp-chess](https://github.com/alexandreroman/mcp-chess)** — play chess via MCP

Chess is well-represented, with servers for both playing (via Stockfish engine) and analyzing (via Chess.com data).

### Esports *(Updated)*

Esports coverage has improved significantly since the March review:

- **[OP.GG Esports MCP](https://www.pulsemcp.com/servers/opgginc-esports)** *(NEW)* — **official** OP.GG server for League of Legends esports data — upcoming match schedules, leagues, scores, and direct links (7 stars)
- **[Apify LoL MCP Server](https://apify.com/mrbridge/lol-mcp-server)** *(NEW)* — League of Legends player profiles, ranked stats, match history, champion mastery, live game data, and AI-powered coaching
- **[OP.GG Game Data](https://glama.ai/mcp/servers?query=league+of+legends)** — broader LoL, TFT, Valorant game data access

### Other Sports

- **Cycling data MCP** — firstcycling.com race data, results, and start lists
- **Squiggle AFL MCP** — Australian Football League teams, ladder standings, results, tips, and power rankings

---

## What's Missing

The gap landscape has shifted significantly since March. Several former gaps are now partially addressed, but others remain:

### Gaps Partially Closed
- **Tennis, golf, cricket, rugby** — Sportradar's MCP server provides developer API access to data for all of these sports, but no dedicated servers exist yet for direct data access (e.g., live ATP rankings, PGA leaderboards, IPL match data). The Sportradar server is a documentation/integration tool, not a live data feed.
- **Fantasy sports** — now has real coverage via Flaim (ESPN+Yahoo+Sleeper) and multiple Yahoo Fantasy servers. ESPN Fantasy Football has read-only access. Still no dedicated fantasy basketball or fantasy baseball management beyond Yahoo.
- **Esports** — OP.GG's official LoL esports MCP and Apify's LoL server represent real progress. Valorant and CS2 still lack dedicated MCP servers.

### Gaps Still Open
- **Olympic sports** — no swimming, track & field, or Olympic data servers
- **Sports video analysis** — no computer vision or play-by-play video analysis
- **Youth sports** — no youth league management, travel team scheduling
- **Marathon/race registration** — no integration with RunSignUp, Athlinks, or similar platforms
- **Sports news/journalism** — no sports news aggregation beyond ESPN scraping
- **Dedicated individual sport servers** — while Sportradar enables building them, nobody has shipped a standalone tennis, golf, or cricket MCP server yet

---

## Bottom Line

The sports and fitness analytics MCP category earns **4.5 out of 5**, upgraded from 4/5 in March. This category has matured rapidly in 47 days. **Sportradar's official MCP server** brings professional-grade sports data infrastructure to the ecosystem, covering 20+ sports including tennis, golf, cricket, and rugby. **Open Wearables at 1,500 stars** is the standout new arrival — a self-hosted platform unifying 6+ wearable ecosystems with a built-in MCP server, representing the kind of ambitious infrastructure project that signals category maturation. **Strava's 55% star growth** (238→368) shows sustained community enthusiasm. **Fantasy sports going from zero to multiple implementations** (Flaim covering ESPN+Yahoo+Sleeper across 4 sports) closes what was one of the most conspicuous gaps. **Oura Ring's explosion from 1 to 6+ servers** demonstrates the wearable MCP ecosystem's vitality, though the trojanized Oura MCP server incident is a sobering reminder that security verification matters in the health data space. The remaining gaps — dedicated individual sport data servers, Olympic sports, sports video analysis — are real but narrowing. For sports fans and fitness enthusiasts, this is now one of the strongest MCP categories available.

*This review was refreshed on 2026-05-02 (first refresh since 2026-03-16) using Claude Opus 4.6 (Anthropic).*
