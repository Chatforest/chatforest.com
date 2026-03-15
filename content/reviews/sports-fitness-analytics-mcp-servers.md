---
title: "Sports & Fitness Analytics MCP Servers — Live Scores, F1 Telemetry, Betting Odds, Strava, Garmin, and Workout Tracking"
date: 2026-03-16T23:00:00+09:00
description: "Sports and fitness analytics MCP servers let AI agents access live scores, race telemetry, betting odds, workout data, and fitness tracking through the Model Context Protocol. We reviewed 25+ servers across 6 subcategories. Multi-sport data platforms (4 servers): michaelfromorg/mcp-sports (TypeScript — ESPN-based real-time scores, standings, schedules for NFL/NBA/MLB/NHL/NCAA/Premier League), apify ESPN MCP servers (12 specialized tools for scores, standings, odds, rosters, news), sportdb.dev (free API + MCP for live scores, fixtures, standings across major leagues), cloudbet/sports-mcp-server (10 stars, TypeScript — Cloudbet API, fuzzy-match competition search, live odds for soccer, basketball, tennis, esports). Formula 1 racing (6+ servers): rakeshgangwar/f1-mcp-server (7 stars, Python — FastF1, race calendar, driver analysis, telemetry, performance comparison), Panth1823/formula1-mcp (TypeScript — real-time and historical F1 data), stagsz/F1-MCP-Server (live timing, analysis, race simulation), Machine-To-Machine/f1-mcp-server (event schedules, driver info, championship standings), plus 3+ more F1 implementations. Sports betting (3 servers): WFord26/BetTrack (Python — 30+ tools, 70+ betting markets, player props, live scores, React dashboard), cloudbet/sports-mcp-server (live market data, natural-language odds queries), apify sportsbook-odds-scraper (scraping betting odds). Strava & endurance (3+ servers): r-huijts/strava-mcp (238 stars, TypeScript — 24 tools for Strava API v3, activity streams, segments, route export), tomekkorbak/strava-mcp-server (TypeScript — Strava API integration), yorrickjansen/strava-mcp (TypeScript — Strava interaction). Fitness & wearables (6+ servers): gesteves/domestique (TypeScript — Intervals.icu + Whoop + TrainerRoad, power curves, pace analysis, recovery), Nicolasvegam/garmin-connect-mcp (61 health/fitness/activity tools from Garmin Connect), Async-IO/pierre_mcp_server (Strava + Garmin + Fitbit + WHOOP + COROS + 150+ wearables via Terra, training load, race predictions), ai-endurance/mcp (running/cycling/triathlon training plans, performance predictions, recovery metrics), ewongz/fitness-mcp-server (30+ sport types, power curves, wellness tracking), tomekkorbak/oura-mcp-server (37 stars, Oura Ring data). Workout management (4+ servers): chrisdoc/hevy-mcp (Hevy workout app, routines, exercise templates, session management), Juxsta/wger-mcp (wger API, 400+ exercises, workout routines, nutrition), idjohnson/workoutMakerMCP (workout content generation, Markdown exercise pages), Dinesh-Satram/fitness_coach_MCP (AI fitness coaching). Niche sports (3+ servers): pab1it0/chess-mcp (Chess.com API, player data, game records), cycling-data MCP (firstcycling.com race data, results, start lists), squiggle-afl MCP (Australian Football League teams, ladder, tips, power rankings). Gaps: no tennis-specific servers (ATP/WTA data), no golf scoring or PGA Tour stats, no cricket (ICC/IPL), no rugby, no Olympic data, no swimming/track & field, no fantasy sports league management (ESPN/Yahoo), no sports video analysis, no referee/officiating tools, no e-sports beyond Cloudbet odds, no marathon/race registration, no youth sports management. Rating: 4/5."
og_description: "Sports & fitness analytics MCP servers: mcp-sports (ESPN live scores for 6+ leagues), r-huijts/strava-mcp (238 stars, 24 tools), F1 servers (6+ implementations with telemetry), BetTrack (70+ betting markets), garmin-connect-mcp (61 tools), domestique (Whoop + TrainerRoad). 25+ servers reviewed. Rating: 4/5."
content_type: "Review"
card_description: "Sports and fitness analytics MCP servers for live scores, Formula 1 telemetry, betting odds, Strava integration, Garmin health data, and workout tracking through AI assistants. This is one of the more vibrant MCP categories — the combination of publicly available sports APIs and the fitness tracking ecosystem has produced a surprisingly rich set of servers. **Formula 1 stands out with 6+ independent implementations**, more than almost any other single sport, likely driven by the excellent FastF1 Python library and the OpenF1 API. **Strava dominates the endurance space** with r-huijts/strava-mcp leading at 238 stars and 24 tools covering activities, segments, and route exports. **The Garmin Connect MCP server is remarkably comprehensive** with 61 tools spanning health, fitness, and activity data — one of the highest tool counts in any sports server. **Fitness platform aggregation is emerging** — the Pierre server connects to 150+ wearables through Terra, while domestique unifies Intervals.icu, Whoop, and TrainerRoad into a single MCP interface with power curve analysis and recovery tracking. **Sports betting has strong representation** with BetTrack offering 30+ tools across 70+ markets including player props. The multi-sport data servers (ESPN-based mcp-sports, SportDB.dev, Cloudbet) provide broad coverage across major leagues. **The biggest gap is individual sports** — tennis, golf, cricket, rugby, and swimming have essentially zero dedicated MCP servers despite massive global followings. Fantasy sports management (ESPN/Yahoo leagues) is also entirely absent, which is surprising given the popularity of fantasy leagues. Chess has multiple implementations but other board games and esports are thin. The category earns 4/5 — strong coverage of team sports scores, excellent F1 depth, robust fitness tracking ecosystem, and emerging betting tools, with individual sports and fantasy being the main gaps."
---

Sports and fitness analytics MCP servers connect AI agents to live scores, race telemetry, betting odds, workout data, and fitness tracking platforms. Instead of manually checking scores, switching between fitness apps, or browsing betting lines, these servers let you query sports data through natural language via the Model Context Protocol.

This review covers **sports data, fitness analytics, and workout management** — live scores, F1 racing, sports betting, Strava/Garmin integration, and exercise tracking. For mental health and wellness tracking, see our [Mental Health & Wellness review](/reviews/mental-health-wellness-mcp-servers/). For wearable device data beyond fitness, see our [Wearables & Quantified Self review](/reviews/wearables-quantified-self-mcp-servers/) if available.

The headline findings: **Formula 1 has the deepest coverage of any single sport** with 6+ independent MCP server implementations. **Strava leads the fitness space** with 238 stars and 24 tools in the top server. **Garmin Connect MCP offers 61 tools** spanning health, fitness, and activity data. **Multi-sport platforms cover all major US leagues** plus Premier League and NCAA. **Sports betting is well-represented** with 70+ markets in BetTrack. **Individual sports (tennis, golf, cricket) are almost entirely absent.**

---

## Multi-Sport Data Platforms

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
| [strava-mcp](https://github.com/r-huijts/strava-mcp) | 238 | TypeScript | — | 24 |

**The most popular Strava MCP server with 24 tools for the full API:**

- **Activity data** — recent activities, detailed activity streams (power, heart rate, cadence, GPS)
- **Segment exploration** — view, star, and manage Strava segments
- **Route management** — list routes, view details, export GPX/TCX files
- **Compact format** — get-activity-streams reduces payload size by 70-80%
- **Full Strava API v3** — comprehensive coverage of the Strava ecosystem

At 238 stars, this is one of the highest-starred sports MCP servers overall. Essential for runners, cyclists, and triathletes who use Strava.

### Other Strava Implementations

- **[tomekkorbak/strava-mcp-server](https://github.com/tomekkorbak/strava-mcp-server)** — Strava API integration for querying athlete activities
- **[yorrickjansen/strava-mcp](https://github.com/yorrickjansen/strava-mcp)** — another Strava interaction server

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
| [garmin-connect-mcp](https://github.com/Nicolasvegam/garmin-connect-mcp) | — | TypeScript | — | 61 |

**Remarkably comprehensive access to Garmin Connect data:**

- **61 tools** — one of the highest tool counts in any sports/fitness MCP server
- **Health data** — heart rate, sleep, stress, body composition, hydration
- **Activity data** — workouts, steps, calories, active minutes
- **Device management** — Garmin device information and settings
- **Training metrics** — training status, load, recovery, VO2 max

If you're a Garmin user, this server exposes essentially your entire Garmin Connect dashboard to AI analysis.

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

### tomekkorbak/oura-mcp-server — Oura Ring Data

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [oura-mcp-server](https://github.com/tomekkorbak/oura-mcp-server) | 37 | — | — | Multiple |

**Access Oura Ring health and sleep data:**

- **Sleep tracking** — detailed sleep stage analysis
- **Readiness scores** — recovery and readiness metrics
- **Activity data** — daily activity and movement tracking

At 37 stars, this shows strong interest in wearable-to-AI integration.

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

Also available as [meimakes/hevy-mcp-server](https://github.com/meimakes/hevy-mcp-server) — a second implementation connecting to the same Hevy API.

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

### Other Sports

- **Cycling data MCP** — firstcycling.com race data, results, and start lists
- **Squiggle AFL MCP** — Australian Football League teams, ladder standings, results, tips, and power rankings
- **[ESPN Fantasy Football MCP](https://agenthotspot.com/connectors/oss/espn-fantasy-football)** — ESPN Fantasy Football API for league and player data

---

## What's Missing

Despite strong coverage in team sports and fitness tracking, several significant gaps remain:

- **Tennis** — no ATP/WTA rankings, match data, or draw bracket servers
- **Golf** — no PGA Tour stats, scoring, or course information servers
- **Cricket** — no ICC, IPL, or county cricket data servers despite massive global following
- **Rugby** — no World Rugby, Six Nations, or Super Rugby servers
- **Olympic sports** — no swimming, track & field, or Olympic data servers
- **Fantasy sports management** — no ESPN/Yahoo fantasy league management (only read-only ESPN Fantasy Football)
- **Sports video analysis** — no computer vision or play-by-play video analysis
- **Youth sports** — no youth league management, travel team scheduling
- **Marathon/race registration** — no integration with RunSignUp, Athlinks, or similar platforms
- **E-sports** — minimal coverage beyond Cloudbet odds (no dedicated League of Legends, Valorant, or CS2 data servers)
- **Sports news/journalism** — no sports news aggregation beyond ESPN scraping

---

## Bottom Line

The sports and fitness analytics MCP category earns **4 out of 5**. This is a notably strong category driven by three factors: excellent public sports APIs (ESPN, FastF1, OpenF1, Strava), the fitness wearable ecosystem's API-friendly culture, and genuine developer enthusiasm (see: 6+ independent F1 implementations). The Strava MCP server at 238 stars is one of the most popular in any sports domain. The Garmin Connect server with 61 tools provides extraordinary depth. The fitness aggregation servers (Pierre, domestique) show sophisticated multi-platform integration that's ahead of most other MCP categories. Team sports live data is well-covered for major leagues. The main weaknesses are the complete absence of individual sports like tennis, golf, and cricket — surprising given their global popularity — and the lack of fantasy sports management tools. For sports fans and fitness enthusiasts, this is one of the more useful MCP categories available today.
