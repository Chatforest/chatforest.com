---
title: "Sports & Athletics MCP Servers — Live Scores, Fantasy Leagues, Betting Odds, Fitness Tracking, and Motorsport Telemetry"
date: 2026-03-15T16:00:00+09:00
description: "Sports and athletics MCP servers let AI agents access live scores, player stats, fantasy league data, betting odds, fitness metrics, and motorsport telemetry. We found 50+ servers across 9 subcategories. Multi-Sport: mikechao/balldontlie-mcp (23 stars, TypeScript, MIT — NBA/NFL/MLB teams, players, games), SportRadar MCP (NFL/NBA/NHL/Soccer/Tennis from commercial API). NBA (6+ implementations): labeveryday/nba_mcp_server (6 stars, Python, MIT, 30 tools — live scores, advanced stats, shot charts, hustle metrics). Football/Soccer: obinopaul/soccer-mcp-server (4 stars, Python, MIT, 17 tools — API-Football), yeonupark/mcp-soccer-data (28 stars, Python, MIT — live scores from SoccerDataAPI). NHL: dylangroos/nhl-mcp (4 stars, TypeScript, MIT, 10 tools — rosters, standings, live scores). Formula 1 (7+ implementations): Panth1823/formula1-mcp (15 stars, TypeScript, 29 tools — OpenF1 + Ergast, telemetry, team radio, 1950-present). Fantasy Sports: jdguggs10/flaim (TypeScript, MIT, 9 tools — ESPN/Yahoo/Sleeper across 4 sports), KBThree13/mcp_espn_ff (29 stars, Python, MIT — ESPN Fantasy Football). Betting: WFord26/BetTrack (TypeScript, MIT, 30+ tools, 70+ markets — The Odds API, line movement analysis). Fitness: Taxuspt/garmin_mcp (271 stars, Python, 96+ tools — comprehensive Garmin Connect), r-huijts/strava-mcp (276 stars, TypeScript, MIT, 25 tools — running/cycling analytics). Cycling: r-huijts/firstcycling-mcp (18 stars, Python, MIT, 20 tools — pro cycling data). Cricket: tarun7r/cricket-mcp-server (11 stars, Python, MIT, 9 tools — Cricbuzz live scores, ICC rankings). Gaps: no rugby, no tennis-specific, no Olympic data, no esports, no sports news aggregation. Rating: 4/5."
og_description: "Sports & athletics MCP servers: balldontlie-mcp (23 stars, NBA/NFL/MLB), formula1-mcp (15 stars, 29 tools), garmin_mcp (271 stars, 96+ tools), strava-mcp (276 stars, 25 tools), ESPN fantasy football (29 stars), BetTrack (30+ tools, betting odds). 50+ servers across 9 categories. Rating: 4/5."
content_type: "Review"
card_description: "Sports and athletics MCP servers for AI-powered live scores, player analytics, fantasy league management, betting odds tracking, fitness data access, and motorsport telemetry. This is one of the most active MCP categories — developers clearly love building sports tools. **Multi-sport platforms provide broad coverage** — mikechao/balldontlie-mcp (23 stars, TypeScript, MIT) covers NBA, NFL, and MLB through the Balldontlie API with 4 tools for teams, players, and games. The SportRadar MCP server covers NFL, NBA, NHL, Soccer, and Tennis from a single commercial API (requires API key). ESPN's public data is accessible through Apify-hosted MCP servers covering scores, standings, stats, news, and odds across major leagues. **Basketball has the deepest single-sport coverage** with 6+ dedicated NBA MCP servers — labeveryday/nba_mcp_server leads with 30 tools covering live scores, advanced analytics (TS%, ORtg, DRtg, USG%, PIE), shot charts with zone breakdowns, hustle stats, and player headshots from NBA's CDN. nikhilkichili/nba-analytics-mcp adds betting odds tracking with line movement detection and AI/ML game simulations. **Football/soccer is well-represented** — obinopaul/soccer-mcp-server (17 tools via API-Football) covers leagues globally with live match events, player profiles, and team data. yeonupark/mcp-soccer-data (28 stars) focuses on live scores with betting odds integration. **Formula 1 is remarkably well-served** with 7+ implementations — Panth1823/formula1-mcp (15 stars, 29 tools) combines OpenF1 real-time data with Ergast historical data back to 1950, covering telemetry, team radio, pit stops, tire strategy, and weather. stagsz/F1-MCP-Server adds Monte Carlo race strategy simulation and tire degradation modeling. **Fantasy sports have a dedicated platform** — jdguggs10/flaim connects ESPN, Yahoo, and Sleeper fantasy leagues to AI assistants with read-only access across Football, Baseball, Basketball, and Hockey. KBThree13/mcp_espn_ff (29 stars) focuses specifically on ESPN Fantasy Football with private league support. **Betting odds are covered** — WFord26/BetTrack (30+ tools, 70+ markets) combines The Odds API data with bet tracking, line movement analysis, and a retro web dashboard. kitchenchem/degen-mcp provides simpler odds comparison across bookmakers. **Fitness tracking is the star of this category** — Taxuspt/garmin_mcp (271 stars, 96+ tools) wraps 89% of Garmin Connect's API covering activities, health metrics, sleep, stress, nutrition, and workouts. r-huijts/strava-mcp (276 stars, 25 tools) provides running/cycling analytics with GPX export and training zone visualization. gesteves/domestique unifies Intervals.icu, Whoop, and TrainerRoad data. AI Endurance offers a commercial MCP for cycling/running/swimming training plans. **Pro cycling has dedicated coverage** — r-huijts/firstcycling-mcp (18 stars, 20 tools) provides rider profiles, race results, Grand Tour data, and historical statistics. **Cricket and hockey round out individual sports** — tarun7r/cricket-mcp-server (11 stars, 9 tools) covers Cricbuzz data with ICC rankings and live commentary. dylangroos/nhl-mcp (10 tools) provides NHL team data, standings, and live scores. **Gaps remain** — no rugby union/league servers, no dedicated tennis server (only via SportRadar), no Olympic/athletics data, no esports, no sports news aggregation, no youth/amateur sports. The category earns 4/5 — exceptional breadth across major sports with particularly strong fitness tracking and motorsport coverage, though some individual sports lack dedicated servers."
---

Sports and athletics MCP servers let AI assistants access live scores, player statistics, fantasy league data, betting odds, fitness metrics, and motorsport telemetry. Instead of manually checking scores, navigating fantasy platforms, or compiling training data, these servers let AI agents pull real-time game information, analyze player performance, manage fantasy rosters, track betting lines, and review workout history — all through the Model Context Protocol.

This review covers the **sports and athletics** vertical — multi-sport data platforms, basketball, football/soccer, ice hockey, Formula 1, fantasy sports, betting odds, fitness/training, pro cycling, and cricket. For health and wellness wearables beyond sports, see our [Health & Wellness MCP review](/reviews/health-wellness-mcp-servers/).

The headline findings: **Fitness tracking leads the category** with strava-mcp (276 stars) and garmin_mcp (271 stars) being among the highest-starred servers in any MCP category. **Formula 1 has disproportionate coverage** with 7+ implementations for a single racing series. **Basketball (NBA) has the deepest analytics** with 30-tool servers covering shot charts and hustle stats. **Fantasy sports and betting odds are well-covered.** **Cricket and hockey have dedicated servers, but rugby, tennis, and esports are missing.**

## Multi-Sport Platforms

### mikechao/balldontlie-mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [mikechao/balldontlie-mcp](https://github.com/mikechao/balldontlie-mcp) | 23 | TypeScript | MIT | 4 |

The **best entry point for multi-sport data** — covers NBA, NFL, and MLB through the Balldontlie API:

- **get_teams** — team information across all three leagues
- **get_players** — player profiles with filtering by name
- **get_games** — game schedules and results with date/team filters
- **get_game** — detailed individual game data

Includes pagination support for large datasets and an interactive schedule generator prompt for Claude Desktop. Available via DXT extension, Smithery, or manual configuration. Works with the free API tier. Simple, well-built, and practical for anyone who needs basic data across major US sports.

### SportRadar MCP (srinayani-m)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [SportRadar MCP](https://lobehub.com/mcp/srinayani-m-sportradar-mcp) | — | Python | — | Multiple |

Covers **five sports from a single commercial API** — NFL, NBA, NHL, Soccer, and Tennis. Provides schedules, live scores, standings, and game stats across all supported leagues. For Tennis, includes ATP and WTA rankings and daily results.

Requires a SportRadar API key (free tier available for development). Still at v0.1.0 with minimal adoption (2 installations), but the multi-sport coverage from a single server is valuable. SportRadar is the data backbone for many major sports media companies.

### mcp-sports-server (PyPI)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [mcp-sports-server](https://pypi.org/project/mcp-sports-server/) | — | Python | — | Multiple |

A **Python MCP server for real-time sports stats via SportRadar**. Currently NFL-only, with plans to add more sports based on interest. Installable via pip. Another SportRadar wrapper, but the limited single-sport scope makes balldontlie-mcp or the multi-sport SportRadar server more practical choices.

### ESPN MCP Servers (Apify)

| Server | Type | Tools |
|--------|------|-------|
| ESPN MCP Server (Apify) | Hosted (Apify) | 12 |
| 62-in-1 Sports Data MCP (Apify) | Hosted (Apify) | 56+ |

**ESPN's public data** is accessible through Apify-hosted MCP servers. The ESPN MCP Server exposes 12 tools covering scores, standings, stats, news, and odds. The 62-in-1 server bundles 56+ tools across NHL, MLB, NBA, NFL, NCAA, Premier League, and WWE — teams, rosters, standings, player stats, schedules, game stats, and injury reports.

No ESPN account or API key needed — uses ESPN's publicly available endpoints. Requires an Apify account (free tier available). Useful for anyone who wants comprehensive sports data without managing API keys for multiple providers.

## Basketball (NBA)

### labeveryday/nba_mcp_server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [labeveryday/nba_mcp_server](https://github.com/labeveryday/nba_mcp_server) | 6 | Python | MIT | 30 |

The **most comprehensive NBA MCP server** — 30 tools covering every angle of basketball data:

- **Live game data** — today's scoreboard, box scores, play-by-play, player rotations
- **Advanced analytics** — True Shooting %, Offensive/Defensive Rating, Usage%, Player Impact Estimate
- **Shooting charts** — shot location coordinates and percentages by zone/distance
- **Hustle stats** — deflections, charges drawn, contested shots, loose balls
- **League data** — standings, statistical leaders, all-time career leaders, awards
- **Visual assets** — player headshots and team logos from NBA's public CDN (no API key)

Configurable logging, HTTP timeouts, concurrency limits, retry policies, and cache TTL. This is genuinely impressive depth — the shooting analytics and hustle stats go well beyond what most sports data APIs expose.

### nikhilkichili/nba-analytics-mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [nikhilkichili/nba-analytics-mcp](https://github.com/nikhilkichili/nba-analytics-mcp) | 2 | Python | MIT | 25+ |

Focused on **NBA betting analytics** rather than pure stats:

- Real-time odds tracking from multiple bookmakers via The Odds API
- AI/ML game simulations and season predictions
- Line movement analysis — detecting sharp money and reverse line action
- Historical odds storage in SQLite for trend analysis
- Matplotlib visualizations as base64-encoded images
- NBA trivia quiz system (yes, really)

The line movement detection is the unique feature here — tracking how odds shift across bookmakers over time is genuinely useful for identifying market sentiment.

### Additional NBA Implementations

- **obinopaul/nba-mcp-server** — NBA API bridge, game data and player stats
- **ziyadmir/nba-player-stats-mcp** — basketball-reference.com scraper for career stats and advanced metrics
- **Taidgh-Robinson/nba-mcp-server** — nba_api wrapper for recent games and stats
- **stevenyuser/nba_mcp** — simple nba_api wrapper for live data and team standings

NBA is the most MCP-served single sport after Formula 1 — at least 6 dedicated implementations exist.

## Football / Soccer

### obinopaul/soccer-mcp-server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [obinopaul/soccer-mcp-server](https://github.com/obinopaul/soccer-mcp-server) | 4 | Python | MIT | 17 |

The **most complete football/soccer MCP server** — 17 tools across five categories via API-Football (RapidAPI):

- **League data** — standings and fixture schedules across multiple competitions
- **Team info** — rosters, upcoming games, historical match records
- **Player profiles** — seasonal statistics and performance metrics
- **Live matches** — real-time events, timelines, and in-game statistics
- **Match analysis** — detailed post-match stats and results

Supports leagues globally. Requires a RapidAPI key for API-Football. Docker deployment option. Solid breadth for anyone building soccer-focused AI tools.

### yeonupark/mcp-soccer-data

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [yeonupark/mcp-soccer-data](https://github.com/yeonupark/mcp-soccer-data) | 28 | Python | MIT | 1 |

**Live football scores** via SoccerDataAPI — a single `get_livescores()` tool that retrieves current match data globally. Despite the single tool, it returns rich data: team names, kickoff times, scores, goal breakdowns, substitutions, cards, penalties, lineups, formations, injury status, and even betting odds. Requires Python 3.12+ and a SoccerDataAPI account. The highest-starred dedicated soccer MCP server.

### yalmeidarj/mcp-football-server

A lightweight MCP tool server providing football data via API-Football. Another API-Football wrapper, but simpler than obinopaul's 17-tool version.

## Ice Hockey (NHL)

### dylangroos/nhl-mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [dylangroos/nhl-mcp](https://github.com/dylangroos/nhl-mcp) | 4 | TypeScript | MIT | 10 |

A **solid NHL data server** with 10 tools covering the essentials:

- **Teams** — team info, rosters, stats, prospects
- **Players** — biographical data and career/season statistics
- **Standings** — league-wide standings with division breakdowns
- **Schedule** — upcoming games, date-specific league schedules
- **Statistics** — current stat leaders for skaters and goalies
- **Live scores** — current game states and scores

Uses the official NHL API. Well-structured TypeScript implementation. michaelfromorg/mcp-sports also includes NHL coverage in its multi-server repository.

## Formula 1 / Motorsport

### Panth1823/formula1-mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [Panth1823/formula1-mcp](https://github.com/Panth1823/formula1-mcp) | 15 | TypeScript | — | 29 |

The **most comprehensive F1 MCP server** — 29 tools combining two data sources:

- **OpenF1 API** (2023-present) — real-time telemetry (speed, throttle, brake, RPM, DRS, gear), team radio communications with audio URLs, race control messages/flags/penalties, pit stop data, tire strategy, weather data, lap times, sector analysis, position tracking
- **Ergast API** (1950-2024) — historical race results, driver/constructor standings, circuit info

Free historical access without authentication. Live streaming available via paid OpenF1 MQTT access. This is remarkable depth for a single racing series — you can analyze telemetry data, listen to team radio, track tire degradation, and query results going back to 1950.

### rakeshgangwar/f1-mcp-server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [rakeshgangwar/f1-mcp-server](https://github.com/rakeshgangwar/f1-mcp-server) | 10 | JavaScript/Python | MIT | 8 |

Uses the **FastF1 Python library** for race data:

- Race calendars and event schedules
- Session results (Race, Qualifying, Practice)
- Lap time analysis and telemetry visualization
- Multi-driver performance comparisons
- Championship standings (drivers and constructors)

Good for historical analysis. FastF1 is the go-to Python library for F1 data science, so this MCP server brings that ecosystem to AI assistants.

### stagsz/F1-MCP-Server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [stagsz/F1-MCP-Server](https://github.com/stagsz/F1-MCP-Server) | 4 | JavaScript | — | 12 |

The **most analytically advanced F1 server** — goes beyond raw data into modeling:

- **Tire degradation modeling** with thermal analysis
- **Fuel-corrected lap analysis** with 25 mini-sector breakdown
- **Weather forecasting** using LSTM/CNN models with strategic recommendations
- **Monte Carlo race strategy simulation** — 300M-1B+ permutations
- **Driver performance extraction** — separates car performance from driver skill (88%/12% methodology)
- **Real-time telemetry** with anomaly detection
- **Live timing** via F1 Official API

Multi-year support from 2018-2025. This is genuine sports analytics, not just data retrieval — the strategy simulation and driver extraction features are research-grade.

### Additional F1 Implementations

- **Machine-To-Machine/f1-mcp-server** — Python, event schedules, telemetry, race results
- **Darakhsh1999/f1-mcp-server** — FastF1 + OpenF1 combined
- **AryaAkman/Open-F1-MCP-Server** — OpenF1 API wrapper for real-time data

Formula 1 has 7+ MCP implementations — disproportionate coverage for a single sport, likely driven by the excellent free data APIs (OpenF1, Ergast) and F1's passionate data science community.

## Fantasy Sports

### jdguggs10/flaim

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [jdguggs10/flaim](https://github.com/jdguggs10/flaim) | 1 | TypeScript | MIT | 9 |

A **unified fantasy sports platform** connecting three major platforms to AI assistants:

- **ESPN** — Football, Baseball, Basketball, Hockey
- **Yahoo** — Football, Baseball, Basketball, Hockey
- **Sleeper** — Football, Basketball

9 MCP tools: league info, roster data, matchups, standings, free agents, player lookup, and transaction history. Read-only design — prevents accidental trades or drops. Chrome extension for ESPN authentication, OAuth for Yahoo, username-based for Sleeper. Includes an AI agent skill that teaches assistants to behave like fantasy analysts. Unified MCP endpoint at a hosted URL.

### KBThree13/mcp_espn_ff

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [KBThree13/mcp_espn_ff](https://github.com/KBThree13/mcp_espn_ff) | 29 | Python | MIT | 6 |

**ESPN Fantasy Football** specifically — the highest-starred fantasy MCP server:

- League information retrieval
- Team roster viewing with player details
- Individual player statistics
- Current standings and rankings
- Weekly matchup data
- Secure credential storage for private league access

Uses the espn-api wrapper library. Simple and focused — if you play ESPN Fantasy Football, this gets AI access to your league in minutes.

## Betting & Odds

### WFord26/BetTrack

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [WFord26/BetTrack](https://github.com/WFord26/BetTrack) | 2 | TypeScript | MIT | 30+ |

The **most comprehensive sports betting MCP server** — 30+ tools covering 70+ betting markets:

- Live odds from The Odds API across multiple bookmakers
- NFL, NBA, NCAAB, NHL, MLB, EPL, UEFA Champions League, College Football
- Line movement analysis and odds history visualization
- Bet tracking with parlay and futures support
- Retro 8-bit web dashboard (React frontend)
- PostgreSQL backend for historical data

Full-stack application: FastMCP (Python 3.11+), React 18, Node.js 20, Prisma ORM, PostgreSQL 16. More of a complete betting analytics platform than a simple MCP server.

### kitchenchem/degen-mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [kitchenchem/degen-mcp](https://github.com/kitchenchem/degen-mcp) | 1 | Python | — | Multiple |

A **simpler odds comparison tool** via The Odds API — available sports, odds across bookmakers, and API quota tracking. Installable via npx. Less ambitious than BetTrack but useful for quick odds lookups.

### Cloudbet Sports MCP Server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [cloudbet/sports-mcp-server](https://github.com/cloudbet/sports-mcp-server) | 10 | Go | MIT | 1 |

A **minimal, educational MCP implementation** from Cloudbet (crypto sports betting platform). Single tool: `findEventsAndMarketsByCompetition`. Exposes live market data for competitions like the Premier League. Single-file Go implementation — useful as a learning resource for MCP server development as much as for actual betting data.

## Fitness & Training

### r-huijts/strava-mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [r-huijts/strava-mcp](https://github.com/r-huijts/strava-mcp) | 276 | TypeScript | MIT | 25 |

The **highest-starred sports MCP server** — 25 tools for Strava fitness data:

- Natural language queries about activities ("How far did I run this month?")
- Detailed workout analysis: power, heart rate, cadence
- Route discovery and segment exploration near specific locations
- Training zone visualization and fitness progression tracking
- GPX/TCX file export for routes
- Club membership information
- Automatic OAuth token management with refresh
- Compact data format reducing payload size by 70-80%

Strava has 120M+ users. This server makes all that training data conversational. The payload optimization is a thoughtful touch — fitness data can be verbose, and the 70-80% reduction keeps AI context windows manageable.

### Taxuspt/garmin_mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [Taxuspt/garmin_mcp](https://github.com/Taxuspt/garmin_mcp) | 271 | Python | — | 96+ |

A **massive Garmin Connect integration** — 96+ tools covering 89% of the python-garminconnect library:

- **Activities** (14 tools) — activity management with pagination
- **Health** (31 tools) — steps, heart rate, sleep, stress, respiration, HRV
- **Training** (9 tools) — training status and performance data
- **Workouts** (8 tools) — workout and training plan access
- **Devices** (7 tools) — device management
- **Gear** (5 tools) — equipment tracking
- **Weight** (5 tools) — body composition and weight tracking
- **Challenges** (10 tools) — badges and challenges
- **Nutrition** (8 tools) — calorie and nutrient tracking
- **Women's Health** (3 tools) — cycle tracking

Supports Garmin Connect China (garmin.cn), MFA authentication, and Docker deployment. This is extraordinary tool coverage — nearly the entire Garmin ecosystem accessible through natural language.

### gesteves/domestique

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [gesteves/domestique](https://github.com/gesteves/domestique) | 0 | TypeScript | — | 30+ |

A **multi-platform fitness aggregator** connecting four services:

- **Intervals.icu** — workout data, structured workouts, training load analysis
- **Whoop** — sleep, recovery, HRV, strain scores (OAuth 2.0)
- **TrainerRoad** — calendar feeds, planned workouts, race scheduling
- **CORE Body Temperature** — heat strain sensor data

30+ tools spanning today's data, historical trends, workout management, analysis, and performance curves. Power curves, pace curves, heart rate trends. Bidirectional syncing between TrainerRoad and Intervals.icu. Targets serious endurance athletes who use multiple platforms.

### AI Endurance MCP Server (Commercial)

| Server | Type | Tools |
|--------|------|-------|
| [AI Endurance MCP](https://aiendurance.com/docs/mcp) | Commercial (hosted) | Multiple |

A **commercial training platform** with native MCP support for cycling, running, and swimming:

- View, modify, and create structured workouts
- Training plans and periodization
- Performance predictions and recovery metrics
- Training zones based on fitness data

Targets triathletes and endurance athletes. The first commercial training platform with direct MCP integration.

## Professional Cycling

### r-huijts/firstcycling-mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [r-huijts/firstcycling-mcp](https://github.com/r-huijts/firstcycling-mcp) | 18 | Python | MIT | 20 |

**Professional cycling data** from FirstCycling.com:

- **Rider tools** (10) — biographical info, career stats, Grand Tour results, Monument classics, team history, victory tables
- **Race tools** (8) — race results, startlists, stage profiles, historical statistics
- **Search tools** (2) — rider and race search

Covers the full spectrum of professional road cycling. Uses web scraping against FirstCycling's data. Valuable for cycling fans and analysts — the Grand Tour and Monument data is especially rich.

## Cricket

### tarun7r/cricket-mcp-server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [tarun7r/cricket-mcp-server](https://github.com/tarun7r/cricket-mcp-server) | 11 | Python | MIT | 9 |

**Comprehensive cricket data** from Cricbuzz:

- **get_player_stats** — stats across Test, ODI, and T20 formats
- **get_live_matches** — current match status and scores
- **get_cricket_schedule** — upcoming fixtures
- **get_cricket_news** — latest cricket news
- **get_icc_rankings** — batting, bowling, all-rounder, and team rankings
- **get_match_details** — detailed scorecards
- **get_live_commentary** — ball-by-ball commentary
- **web_search** / **search_live_commentary** — search capabilities

Includes a Gradio-based web interface powered by Google Gemini API. The only dedicated cricket MCP server — serves cricket's massive global audience (2.5B+ fans worldwide).

## What's Missing

Despite 50+ servers, several gaps remain:

- **Rugby** — no rugby union or rugby league servers
- **Tennis** — no dedicated server (only available through multi-sport SportRadar MCP)
- **Golf** — PGA reportedly has an official MCP, but no open-source implementations found
- **Olympic sports / Athletics** — no track & field, swimming, gymnastics data
- **Esports** — no League of Legends, CS2, Dota 2, or Valorant servers despite massive data APIs
- **Youth / amateur sports** — all servers focus on professional leagues
- **Sports news aggregation** — no dedicated sports journalism or highlight servers
- **Baseball-specific** — only via multi-sport servers (Balldontlie, ESPN), no dedicated deep MLB analytics server beyond the SportRadar wrapper

## Bottom Line

**Rating: 4/5** — Sports and athletics is one of the strongest MCP categories by volume and quality. Fitness tracking leads with two 270+ star servers (Strava and Garmin) offering genuinely comprehensive data access. Formula 1 has research-grade analytics with tire modeling and race strategy simulation. NBA coverage goes deep into advanced stats and shooting charts. Fantasy sports and betting odds are well-served. The main gaps are individual sports (tennis, rugby, golf) and esports. For anyone building sports-related AI tools, the ecosystem is already remarkably mature.
