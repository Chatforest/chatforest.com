---
title: "Sports & Fitness MCP Servers — Strava, Garmin, Fitbit, F1, NFL, MLB, Soccer, and More"
date: 2026-03-15T14:00:00+09:00
description: "Sports and fitness MCP servers are connecting AI assistants to workout data, live scores, and athletic performance analytics. We reviewed 35+ servers across 7 subcategories. Fitness Wearables: Taxuspt/garmin_mcp (270 stars, Python, 96+ tools — the most comprehensive fitness MCP server, covering 89% of Garmin Connect API), r-huijts/strava-mcp (274 stars, TypeScript, MIT, 25 tools — activity tracking, segments, routes, club data), TheDigitalNinja/mcp-fitbit (26 stars, TypeScript, MIT, 12 tools — weight, sleep, heart rate, nutrition). Apple Health: the-momentum/apple-health-mcp-server (133 stars, Python, MIT — DuckDB-powered natural language queries against HealthKit exports). WHOOP: JedPattersonn/whoop-mcp (10 stars, TypeScript, MIT, 5 tools — recovery, strain, sleep, healthspan). Formula 1: Panth1823/formula1-mcp (15 stars, TypeScript, 29 tools — live telemetry, OpenF1 + Ergast APIs), rakeshgangwar/f1-mcp-server (10 stars, Python/JS, MIT, 8 tools — FastF1 integration). Multi-Sport Data: balldontlie-api/mcp (7 stars, TypeScript, 250+ endpoints — NBA, NFL, MLB, NHL, EPL, MMA, esports across 18 leagues), mikechao/balldontlie-mcp (23 stars, JS, MIT, 4 tools). MLB: guillochon/mlb-api-mcp (39 stars, Python, MIT, 21+ tools — sabermetrics, boxscores, standings). NFL: gtonic/nfl_mcp (5 stars, Python, 30+ tools — ESPN news, Sleeper fantasy, lineup optimization). Soccer: yeonupark/mcp-soccer-data (28 stars, Python, MIT — live scores via SoccerDataAPI). Professional Cycling: r-huijts/firstcycling-mcp (18 stars, Python, MIT, 20 tools — rider bios, race results). Fantasy Sports: KBThree13/mcp_espn_ff (28 stars, Python, MIT, 6 tools — ESPN Fantasy Football), jimbrig/yahoo-fantasy-baseball-mcp (3 stars, TypeScript, MIT). Sports Betting: WFord26/BetTrack (2 stars, TypeScript, MIT, 30+ tools — odds for 70+ markets across NFL, NBA, NHL, MLB). Nutrition Tracking: AdamWalt/myfitnesspal-mcp-python (MyFitnessPal diary, exercises, nutrition goals). Multi-Platform: Async-IO/pierre_mcp_server (Strava, Garmin, Fitbit, WHOOP, COROS, Terra — 150+ wearables via MCP + A2A). Rating: 4.0/5."
og_description: "Sports & fitness MCP servers: Strava (274 stars, 25 tools), Garmin Connect (270 stars, 96+ tools), Apple Health (133 stars), MLB stats (39 stars, 21+ tools), F1 racing (15 stars, 29 tools), Fitbit (26 stars, 12 tools), multi-sport via Balldontlie (250+ endpoints across 18 leagues), ESPN Fantasy Football (28 stars). Rating: 4.0/5."
content_type: "Review"
card_description: "Sports and fitness MCP servers for workout tracking, live scores, athletic analytics, and fantasy sports. This is a surprisingly deep category — Garmin Connect alone has 96+ tools covering activities, health metrics, workouts, devices, nutrition, and challenges. Strava leads in stars (274) with 25 tools for activities, segments, and routes. Apple Health MCP (133 stars) enables natural language queries against HealthKit exports using DuckDB. For spectator sports, Balldontlie's official MCP server covers 18 leagues with 250+ endpoints spanning NBA, NFL, MLB, NHL, EPL, MMA, and esports. Formula 1 has the most implementations of any single sport — at least 5 independent F1 MCP servers exist, with Panth1823/formula1-mcp offering 29 tools including live telemetry. MLB is well-served with guillochon/mlb-api-mcp providing sabermetric stats (WAR, wOBA, wRC+). Fantasy sports has ESPN Fantasy Football (28 stars) and Yahoo Fantasy Baseball servers. The multi-platform Pierre Fitness server connects to 150+ wearables via Strava, Garmin, Fitbit, WHOOP, and COROS. Major gaps: no official servers from Strava, Garmin, Fitbit, Peloton, or any major sports league (NFL, NBA, MLB); no tennis, golf, or rugby MCP servers found; no Oura Ring dedicated server. The category earns 4.0/5 — exceptional community depth in fitness wearables and baseball, with F1 being the most over-served niche sport."
last_refreshed: 2026-03-15
---

Sports and fitness MCP servers are connecting AI assistants to workout data, live scores, and athletic performance analytics. Instead of manually checking Garmin Connect for your training load or scrolling ESPN for box scores, these servers let AI agents query your fitness history, analyze race telemetry, pull real-time scores, and even manage fantasy lineups — all through the Model Context Protocol.

The landscape spans seven areas: **fitness wearables** (Garmin, Strava, Fitbit, Apple Health, WHOOP), **motorsport** (Formula 1), **multi-sport data platforms** (Balldontlie covering 18 leagues), **baseball** (MLB stats and sabermetrics), **football** (NFL and fantasy), **soccer and cycling** (live scores and professional racing data), and **sports betting/fantasy** (odds, props, lineup optimization).

The headline findings: **Garmin Connect has the most comprehensive fitness MCP server in the entire ecosystem** — 270 stars, 96+ tools covering 89% of the python-garminconnect library, spanning activities, health metrics, workouts, devices, gear, nutrition, and challenges. **Strava leads in stars** (274) with 25 polished tools for activities, segments, and routes. **Formula 1 is the most over-served niche sport** — at least 5 independent F1 MCP servers exist, with live telemetry, historical data going back to 1950, and tire degradation modeling. **Balldontlie's official MCP server covers 18 leagues** with 250+ endpoints, making it the broadest sports data server available. **No major platform has an official MCP server** — not Strava, Garmin, Fitbit, Peloton, nor any professional sports league.

## Fitness Wearables

### Garmin Connect MCP Server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [Taxuspt/garmin_mcp](https://github.com/Taxuspt/garmin_mcp) | 270 | Python | — | 96+ |

The **most comprehensive fitness MCP server** we've seen in any category. This server wraps 89% of the python-garminconnect library (v0.2.38) and exposes an enormous surface area across 10 tool categories:

- **Activity Management** (14 tools) — list, detail, splits, GPS data, workout types
- **Health & Wellness** (31 tools) — steps, heart rate, sleep, stress, body battery, SpO2, respiration, hydration
- **Training & Performance** (9 tools) — training status, VO2 max, training load, race predictions
- **Workouts** (8 tools) — create, modify, schedule structured workouts
- **Devices** (7 tools) — device info, settings, solar intensity
- **Gear Management** (5 tools) — track shoes, bikes, and other equipment usage
- **Weight Tracking** (5 tools) — weight history, trends, goal tracking
- **Challenges & Badges** (10 tools) — active challenges, badge progress, social features
- **Nutrition** (8 tools) — calorie tracking, macro goals, meal logging
- **Women's Health & Profile** (3 tools) — menstrual cycle tracking, user profile

With 80 commits and 270 stars, this is a serious community project. The sheer tool count (96+) rivals enterprise API integrations — and all of it is community-built, since Garmin has no official MCP server.

#### Other Garmin MCP Servers

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [st3v/garmin-workouts-mcp](https://github.com/st3v/garmin-workouts-mcp) | 13 | Python | MIT | 10 |
| [charlesfrisbee/garmin-workouts-mcp](https://github.com/charlesfrisbee/garmin-workouts-mcp) | 1 | TypeScript | — | 5 |
| [jlwainwright/garmin-mcp-server](https://github.com/jlwainwright/garmin-mcp-server) | 0 | Python | MIT | 20+ |

**st3v/garmin-workouts-mcp** focuses specifically on workout creation — you describe a workout in natural language ("40 minute tempo run with 10 minute warmup") and it generates and uploads the structured workout to Garmin Connect. It also includes activity viewing and calendar management.

**jlwainwright/garmin-mcp-server** offers 20+ tools with a focus on headless 2FA authentication and ntfy notification integration for automated deployments — useful if you want unattended Garmin data access.

### Strava MCP Server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [r-huijts/strava-mcp](https://github.com/r-huijts/strava-mcp) | 274 | TypeScript | MIT | 25 |

The **highest-starred sports MCP server** in the ecosystem. With 96 commits and 25 tools across six categories, this is a polished integration:

- **Account & Profile** — athlete profile, authorization management
- **Activity Data** — list activities, get details, search by date/type
- **Statistics** — progress tracking, personal records, training summaries
- **Segments** — explore and star segments, view leaderboards
- **Routes** — create and export routes in GPX format
- **Clubs** — view club memberships and activity feeds

The server handles OAuth 2.0 token management and supports natural language queries like "show me my longest rides this month" or "compare my running pace over the last 6 weeks."

### Fitbit MCP Server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [TheDigitalNinja/mcp-fitbit](https://github.com/TheDigitalNinja/mcp-fitbit) | 26 | TypeScript | MIT | 12 |

A solid integration with 85 commits and a published npm package (v1.0.2). Covers the core Fitbit data types:

- Exercise and activity logs
- Sleep analysis (stages, duration, quality)
- Heart rate monitoring (resting, zones, intraday)
- Weight tracking and body composition
- Nutrition logging and calorie tracking
- Activity summaries (steps, distance, calories burned)

Works with Claude Desktop and other MCP-compatible clients. The 85 commits suggest active maintenance despite the moderate star count.

### Apple Health MCP Server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [the-momentum/apple-health-mcp-server](https://github.com/the-momentum/apple-health-mcp-server) | 133 | Python | MIT | — |

A clever approach — rather than connecting to a live API, this server imports Apple Health XML exports and loads them into DuckDB for lightning-fast natural language queries. You export your health data from your iPhone, point the server at the file, and then ask questions like "what's my average resting heart rate this month?" or "show my sleep duration trends."

The DuckDB backend means queries over years of health data run in milliseconds. The project has evolved into Open Wearables, a broader platform supporting Garmin, Polar, Suunto, and Whoop data alongside Apple Health.

### WHOOP MCP Server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [JedPattersonn/whoop-mcp](https://github.com/JedPattersonn/whoop-mcp) | 10 | TypeScript | MIT | 5 |

Integrates WHOOP's biometric data with 5 focused tools:

- **Overview** — daily summary of strain, recovery, sleep
- **Sleep** — detailed sleep metrics and staging
- **Recovery** — HRV, resting heart rate, recovery score
- **Strain** — daily strain score and activity breakdown
- **Healthspan** — WHOOP's longevity and health trend metrics

Small but functional — covers the core WHOOP data that athletes care about most.

### MyFitnessPal MCP Server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [AdamWalt/myfitnesspal-mcp-python](https://github.com/AdamWalt/myfitnesspal-mcp-python) | — | Python | — | — |
| [ai-mcp-garage/mcp-myfitnesspal](https://github.com/ai-mcp-garage/mcp-myfitnesspal) | — | Python | — | — |

Two community implementations for pulling nutrition data from MyFitnessPal — food diaries, exercise logs, body measurements, nutrition goals, and water intake. Neither has significant traction yet.

### Multi-Platform: Pierre Fitness

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [Async-IO/pierre_mcp_server](https://github.com/Async-IO/pierre_mcp_server) | — | — | — | — |

Pierre takes the aggregator approach, connecting to **150+ wearables** via Strava, Garmin, Fitbit, WHOOP, COROS, and Terra. Implements both MCP and A2A protocols with OAuth 2.0 and REST APIs. If you want a single MCP server that pulls from multiple fitness platforms, this is the only option — but it adds another dependency layer between you and your data.

## Formula 1

F1 is the **most over-served niche sport** in the MCP ecosystem — at least 5 independent implementations exist, which is remarkable for a single sport.

### Formula1-MCP (Panth1823)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [Panth1823/formula1-mcp](https://github.com/Panth1823/formula1-mcp) | 15 | TypeScript | — | 29 |

The most feature-rich F1 server with 29 tools spanning:

- **Live Data** (6 tools) — car telemetry, real-time positions, race control messages, team radio, weather, streaming management
- **Historical Data** (20+ tools) — lap times, standings, pit stops, circuit info, race results going back through Ergast API (1950–2024)
- **Cache Management** — smart caching for performance

Integrates both OpenF1 (2023–present, live data) and Ergast (1950–2024, historical records), giving comprehensive coverage across F1 history.

### Other F1 MCP Servers

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [rakeshgangwar/f1-mcp-server](https://github.com/rakeshgangwar/f1-mcp-server) | 10 | Python/JS | MIT | 8 |
| [Darakhsh1999/f1-mcp-server](https://github.com/Darakhsh1999/f1-mcp-server) | — | Python | — | — |
| [stagsz/F1-MCP-Server](https://github.com/stagsz/F1-MCP-Server) | — | — | — | — |
| [AryaAkman/Open-F1-MCP-Server](https://github.com/AryaAkman/Open-F1-MCP-Server) | — | — | — | — |

**rakeshgangwar/f1-mcp-server** uses the FastF1 Python library for telemetry analysis and driver comparison. **stagsz/F1-MCP-Server** goes furthest with tire degradation modeling and race strategy simulation. The sheer number of F1 servers reflects both the sport's data-rich nature (telemetry, timing, weather) and its technically-inclined fanbase.

## Multi-Sport Data Platforms

### Balldontlie Official MCP Server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [balldontlie-api/mcp](https://github.com/balldontlie-api/mcp) | 7 | TypeScript | — | 250+ |

The **broadest sports data MCP server** available, covering **18 leagues and sports**:

- **Major US Sports** — NBA (23 tools), NFL (17), MLB (14), NHL (16), WNBA (14), NCAAF (17), NCAAB (18)
- **European Football** — EPL (17), La Liga, Serie A, Bundesliga, Ligue 1, UEFA Champions League
- **Combat Sports** — MMA
- **Esports** — CS2, League of Legends, Dota 2
- **International** — FIFA World Cup 2026

With 250+ endpoints, this is an API wrapper rather than a deep analytics platform — you get teams, players, games, and stats, but not advanced analytics like sabermetrics. Requires a Balldontlie API key.

### Balldontlie Community Server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [mikechao/balldontlie-mcp](https://github.com/mikechao/balldontlie-mcp) | 23 | JavaScript | MIT | 4 |

A simpler community implementation with 4 core tools (get_teams, get_players, get_games, get_game) plus a schedule_generator prompt. More focused than the official server — good for quick lookups rather than deep analysis.

## Baseball (MLB)

### MLB API MCP Server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [guillochon/mlb-api-mcp](https://github.com/guillochon/mlb-api-mcp) | 39 | Python | MIT | 21+ |

The **most comprehensive single-sport analytics server** in the ecosystem. 21+ tools covering:

- Standings, schedules, and scores
- Player and team information
- Boxscores, linescores, and game highlights
- **Sabermetric statistics** — WAR, wOBA, wRC+ (advanced analytics that baseball fans actually want)
- Draft data and award history
- Game pace analysis and lineup data

This is what a sports MCP server should look like — it goes beyond basic API wrapping to provide the kind of analytical depth that makes AI-assisted research genuinely useful.

### MLB Stats MCP Server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [etweisberg/mlb-mcp](https://github.com/etweisberg/mlb-mcp) | 17 | Python | — | 4 |

Focused on **advanced baseball analytics** by integrating Statcast, FanGraphs, and Baseball Reference data through the pybaseball library. Fewer tools than guillochon's server but deeper analytical capabilities — pitch-level Statcast data, FanGraphs leaderboards, and Baseball Reference historical stats.

## Football (NFL) & Fantasy

### NFL MCP Server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [gtonic/nfl_mcp](https://github.com/gtonic/nfl_mcp) | 5 | Python | — | 30+ |

A surprisingly deep FastMCP 3.0 server with 30+ tools organized across:

- **NFL Information** (9 tools) — news, teams, depth charts, injuries, standings, schedules
- **Coaching Intelligence** (4 tools) — coaching staff, coaching trees, scheme classification
- **CBS Fantasy Football** (3 tools) — player news, projections, expert picks
- **Player Management** (4 tools) — athlete search, lookup, team rosters
- **Fantasy/Sleeper API** — league info, rosters, matchups, transactions, draft data
- **Lineup Optimization** (11 tools) — defense rankings, start/sit recommendations, Vegas line analysis

The lineup optimization tools make this particularly useful for fantasy football — getting AI-powered start/sit recommendations backed by actual data.

### ESPN Fantasy Football MCP

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [KBThree13/mcp_espn_ff](https://github.com/KBThree13/mcp_espn_ff) | 28 | Python | MIT | 6 |

Connects Claude to ESPN Fantasy Football leagues with 6 tools: authentication, league info, team rosters, player stats, standings, and matchup details. Works with both public and private ESPN leagues. Simple but covers the core fantasy football workflow.

### Yahoo Fantasy Baseball MCP

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [jimbrig/yahoo-fantasy-baseball-mcp](https://github.com/jimbrig/yahoo-fantasy-baseball-mcp) | 3 | TypeScript/JS | MIT | 1 (3 planned) |

Early-stage with only `get_team_roster` implemented. Waiver player and matchup tools are marked "coming soon." More a proof of concept than a usable tool at this point.

## Soccer & Cycling

### Soccer Data MCP Server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [yeonupark/mcp-soccer-data](https://github.com/yeonupark/mcp-soccer-data) | 28 | Python | MIT | 1 |

Provides real-time football (soccer) data through a single `get_livescores()` tool, but that tool delivers 6 data categories: match listings, detailed match info, live events, team lineups, betting odds, and league metadata. Good for checking scores during matches, but limited scope compared to what Balldontlie offers for EPL.

### Professional Cycling (FirstCycling)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [r-huijts/firstcycling-mcp](https://github.com/r-huijts/firstcycling-mcp) | 18 | Python | MIT | 20 |

A niche but well-built server for professional cycling data from FirstCycling:

- **Rider Tools** (10) — biographical data, career results, race history, victories, team progression
- **Race Tools** (8) — results, profiles, starters, victory tables, age records
- **Search** (2) — rider and race search

Perfect for cycling fans who want to ask things like "who has won the most Tour de France stages in the last decade?" Built by the same developer as the Strava MCP server.

## Sports Betting

### BetTrack

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [WFord26/BetTrack](https://github.com/WFord26/BetTrack) | 2 | TypeScript | MIT | 30+ |

A sports betting companion with 30+ tools supporting **70+ betting markets** across NFL, NBA, NHL, and MLB. Includes player props, live scores, visual artifacts, and an optional React dashboard for bet tracking. Very early stage (2 stars) but ambitious in scope.

## Fitness Coaching & Tracking

### AI Endurance MCP Server

[AI Endurance](https://aiendurance.com/docs/mcp) offers a commercial MCP server for structured training in running, cycling, and triathlon. It supports creating custom workout plans, strength training, yoga, hiking, and other non-endurance activities. This is one of the few **paid fitness MCP integrations** — most community servers are free.

### Health & Fitness Coach MCP

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [Dinesh-Satram/fitness_coach_MCP](https://github.com/Dinesh-Satram/fitness_coach_MCP) | 7 | TypeScript | — | 7 |

A full-stack fitness coaching app with a Next.js dashboard and MCP backend. Tools include workout logging, nutrition tracking, plan generation, weekly targets, and progress feedback. More of an app with MCP integration than a pure MCP server.

## What's Missing

Despite impressive depth in some areas, notable gaps remain:

- **No official platform servers** — Strava, Garmin, Fitbit, Peloton, and every major sports league have zero official MCP servers. Everything is community-built using unofficial APIs or OAuth integrations.
- **No Peloton MCP server** — surprising given Peloton's API-savvy userbase and the bike's rich data model (output, cadence, resistance, heart rate zones)
- **No Oura Ring server** — Oura's sleep and readiness data would be a natural fit for MCP
- **No tennis, golf, rugby, or cricket** — these major global sports have zero MCP representation
- **No nutrition-first platforms** — Cronometer, Lose It!, and Noom have no MCP servers
- **Limited real-time scoring** — most servers focus on historical data rather than live game updates
- **No official league APIs** — NFL, NBA, MLB, and NHL have APIs but no official MCP servers

## The Bottom Line

**Rating: 4.0 / 5**

Sports & fitness is a surprisingly deep MCP category with genuine standouts. Garmin Connect's 96-tool server is one of the most comprehensive MCP integrations in any domain. Strava's 274-star server shows strong community demand. Baseball has the best analytical depth of any spectator sport. F1's five independent servers demonstrate what happens when a data-rich sport meets a technically-inclined community.

The ecosystem is entirely community-driven — no major fitness platform or sports league has shipped an official MCP server. This means authentication relies on unofficial methods (screen scraping Garmin cookies, OAuth workarounds) and long-term reliability isn't guaranteed. But right now, if you want AI to analyze your Garmin training data or break down MLB sabermetrics, the tools exist and they work.

**Best for fitness tracking:** Taxuspt/garmin_mcp (96+ tools) or r-huijts/strava-mcp (274 stars, 25 tools)
**Best for sports data:** guillochon/mlb-api-mcp (21+ tools with sabermetrics) or balldontlie-api/mcp (18 leagues, 250+ endpoints)
**Best niche pick:** Panth1823/formula1-mcp (29 tools with live telemetry)
**Best for fantasy:** KBThree13/mcp_espn_ff (ESPN Fantasy Football, 28 stars)

*This review was last edited on 2026-03-16 using Claude Opus 4.6 (Anthropic).*
