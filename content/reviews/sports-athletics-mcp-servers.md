---
title: "Sports & Athletics MCP Servers — Live Scores, Fantasy Leagues, Betting Odds, Fitness Tracking, and Motorsport Telemetry"
date: 2026-03-15T16:00:00+09:00
description: "Sports and athletics MCP servers let AI agents access live scores, player stats, fantasy league data, betting odds, fitness metrics, and motorsport telemetry."
og_description: "Sports & athletics MCP servers: official Balldontlie MCP (10 stars, 18 leagues, 250+ endpoints, esports/WNBA/college), fantasy-football-mcp (34 stars, Yahoo FF lineup optimization), formula1-mcp (15 stars, 29 tools), garmin_mcp (407 stars, 96+ tools), strava-mcp (357 stars, 25 tools), ESPN fantasy football (30 stars), BetTrack (30+ tools). 70+ servers across 10 categories. Rating: 4.5/5."
content_type: "Review"
card_description: "Sports and athletics MCP servers for AI-powered live scores, player analytics, fantasy league management, betting odds tracking, fitness data access, and motorsport telemetry. This is one of the most active MCP categories — developers clearly love building sports tools. **The official Balldontlie MCP server (balldontlie-api/mcp, 10 stars) is a game-changer** — 250+ endpoints covering 18 leagues including NBA, WNBA, NFL, MLB, EPL, NHL, NCAAF, NCAAB, MMA, CS2, League of Legends, Dota 2, FIFA World Cup 2026, La Liga, Serie A, UEFA Champions League, Bundesliga, and Ligue 1. This single server fills the esports, WNBA, college sports, and European football gaps from the initial review. **Fantasy sports exploded** — derekrbreese/fantasy-football-mcp-public (34 stars) brings Yahoo Fantasy Football with advanced lineup optimization, VORP draft assistance, Reddit sentiment analysis, and multi-source projections. spilchen/yahoo_fantasy_mcp adds 24 tools for all Yahoo Fantasy sports. **Fitness tracking leads** with strava-mcp (357 stars, +29%) and garmin_mcp (407 stars, +50%) among the highest-starred servers in any MCP category. **Formula 1 reached 10+ implementations** — drivenrajat/f1 (36+ tools) and aashnakunk/fastf1-mcp (17 tools, 133 tests) join the lineup. **NHL expanded from 1 to 4+ implementations** with argotdev providing both TypeScript and Python versions. **Multi-sport platforms expanded** — sportscore-mcp (4 stars) covers football, basketball, cricket, and tennis via the free SportScore API; michaelfromorg/mcp-sports (5 stars) covers real-time data across multiple sports. **Cricket deepened** from 1 to 3+ implementations (see our [Sports & Fitness MCP review](/reviews/sports-fitness-mcp-servers/) for mavaali/cricket-mcp with 28 tools and 10.9M ball-by-ball deliveries). **Multiple gaps filled since initial review**: esports (CS2, LoL, Dota 2 via Balldontlie), baseball-specific analytics (MLB MCP servers), WNBA, college sports (NCAAF, NCAAB), tennis (via sportscore-mcp). Remaining gaps: rugby, golf (open-source), Olympic sports, dedicated esports servers. Rating upgraded to 4.5/5."
last_refreshed: 2026-04-27
categories: ["/categories/sports-fitness/"]
---

Sports and athletics MCP servers let AI assistants access live scores, player statistics, fantasy league data, betting odds, fitness metrics, and motorsport telemetry. Instead of manually checking scores, navigating fantasy platforms, or compiling training data, these servers let AI agents pull real-time game information, analyze player performance, manage fantasy rosters, track betting lines, and review workout history — all through the Model Context Protocol.

This review covers the **sports and athletics** vertical — multi-sport data platforms, basketball, football/soccer, ice hockey, Formula 1, fantasy sports, betting odds, fitness/training, pro cycling, and cricket. For health and wellness wearables and fitness-specific servers, see our [Sports & Fitness MCP review](/reviews/sports-fitness-mcp-servers/).

The headline findings: **The official Balldontlie MCP server is a game-changer** — 250+ endpoints across 18 leagues including esports (CS2, LoL, Dota 2), filling the biggest gaps from the initial review. **Fitness tracking leads the category** with strava-mcp (357 stars) and garmin_mcp (407 stars) being among the highest-starred servers in any MCP category. **Fantasy sports exploded** with a 34-star Yahoo Fantasy Football server offering lineup optimization and Reddit sentiment analysis. **Formula 1 reached 10+ implementations** for a single racing series. **NHL went from 1 to 4+ implementations.** **Esports, WNBA, college sports, and baseball-specific gaps are now filled.**

## Multi-Sport Platforms

### balldontlie-api/mcp (Official)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [balldontlie-api/mcp](https://github.com/balldontlie-api/mcp) | 10 | TypeScript | — | 250+ |

**The single most important addition to sports MCP** — the official Balldontlie API MCP server covers **18 leagues** from a single server:

- **US Professional** — NBA, WNBA, NFL, MLB, NHL
- **US College** — NCAAF (NCAA Football), NCAAB (NCAA Basketball)
- **European Football** — EPL, La Liga, Serie A, Bundesliga, Ligue 1, UEFA Champions League
- **Combat Sports** — MMA (Mixed Martial Arts)
- **Esports** — CS2, League of Legends, Dota 2
- **International** — FIFA World Cup 2026

250+ endpoints covering teams, players, games, standings, and statistics across all leagues. This single server fills four gaps identified in the initial review: esports, WNBA, college sports, and European football leagues beyond EPL. The breadth is unprecedented — no other sports MCP server comes close to this range.

### mikechao/balldontlie-mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [mikechao/balldontlie-mcp](https://github.com/mikechao/balldontlie-mcp) | 23 | TypeScript | MIT | 4 |

The **community Balldontlie wrapper** — covers NBA, NFL, and MLB through the Balldontlie API with 4 tools for teams, players, and games. Includes pagination support, interactive schedule generator prompt for Claude Desktop, and DXT extension availability. Simpler and lighter than the official server — good for quick multi-sport queries without the full 250+ endpoint surface.

### Backspace-me/sportscore-mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [Backspace-me/sportscore-mcp](https://github.com/Backspace-me/sportscore-mcp) | 4 | JavaScript | MIT | 8 |

**NEW.** A **free multi-sport platform** via the SportScore API — covers football, basketball, cricket, and tennis:

- **get_matches** / **get_match_detail** — live scores and detailed match data
- **get_team_schedule** — upcoming fixtures for any team
- **get_standings** — league tables and rankings
- **get_top_scorers** — scoring leaders
- **get_player** — player profiles and stats
- **get_bracket** — tournament brackets
- **get_tracker** — live match tracking

**Notably includes tennis** — partially filling the dedicated tennis gap. Works with Claude, Cursor, and Zed. No API key required (free tier). Active development (last commit April 2026).

### SportRadar MCP (srinayani-m)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [SportRadar MCP](https://lobehub.com/mcp/srinayani-m-sportradar-mcp) | — | Python | — | Multiple |

Covers **five sports from a single commercial API** — NFL, NBA, NHL, Soccer, and Tennis. Provides schedules, live scores, standings, and game stats across all supported leagues. For Tennis, includes ATP and WTA rankings and daily results. Requires a SportRadar API key (free tier available for development).

### michaelfromorg/mcp-sports

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [michaelfromorg/mcp-sports](https://github.com/michaelfromorg/mcp-sports) | 5 | — | — | Multiple |

**NEW.** A **real-time sports data server** covering multiple sports. Multi-server repository that includes NHL and other sports coverage. Another option for getting broad sports data through a single MCP interface.

### ESPN MCP Servers (Apify)

| Server | Type | Tools |
|--------|------|-------|
| ESPN MCP Server (Apify) | Hosted (Apify) | 12 |
| 62-in-1 Sports Data MCP (Apify) | Hosted (Apify) | 56+ |

**ESPN's public data** is accessible through Apify-hosted MCP servers. The ESPN MCP Server exposes 12 tools covering scores, standings, stats, news, and odds. The 62-in-1 server bundles 56+ tools across NHL, MLB, NBA, NFL, NCAA, Premier League, and WWE. No ESPN account or API key needed — uses ESPN's publicly available endpoints. Requires an Apify account (free tier available).

## Basketball (NBA)

### labeveryday/nba_mcp_server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [labeveryday/nba_mcp_server](https://github.com/labeveryday/nba_mcp_server) | 8 | Python | MIT | 30 |

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
| [nikhilkichili/nba-analytics-mcp](https://github.com/nikhilkichili/nba-analytics-mcp) | 4 | Python | MIT | 25+ |

Focused on **NBA betting analytics** rather than pure stats:

- Real-time odds tracking from multiple bookmakers via The Odds API
- AI/ML game simulations and season predictions
- Line movement analysis — detecting sharp money and reverse line action
- Historical odds storage in SQLite for trend analysis
- Matplotlib visualizations as base64-encoded images
- NBA trivia quiz system (yes, really)

Stars doubled from 2→4. The line movement detection is the unique feature here — tracking how odds shift across bookmakers over time is genuinely useful for identifying market sentiment.

### Additional NBA Implementations

- **Taidgh-Robinson/nba-mcp-server** (11 stars, +growth) — nba_api wrapper for recent games and stats
- **obinopaul/nba-mcp-server** (4 stars) — NBA API bridge, game data and player stats
- **ziyadmir/nba-player-stats-mcp** — basketball-reference.com scraper for career stats and advanced metrics
- **stevenyuser/nba_mcp** — simple nba_api wrapper for live data and team standings

NBA has at least 6 dedicated implementations plus WNBA coverage via the official Balldontlie server. Taidgh-Robinson's server grew notably to 11 stars.

## Football / Soccer

### obinopaul/soccer-mcp-server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [obinopaul/soccer-mcp-server](https://github.com/obinopaul/soccer-mcp-server) | 5 | Python | MIT | 17 |

The **most complete football/soccer MCP server** — 17 tools across five categories via API-Football (RapidAPI):

- **League data** — standings and fixture schedules across multiple competitions
- **Team info** — rosters, upcoming games, historical match records
- **Player profiles** — seasonal statistics and performance metrics
- **Live matches** — real-time events, timelines, and in-game statistics
- **Match analysis** — detailed post-match stats and results

Supports leagues globally. Requires a RapidAPI key for API-Football. Docker deployment option.

### yeonupark/mcp-soccer-data

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [yeonupark/mcp-soccer-data](https://github.com/yeonupark/mcp-soccer-data) | 30 | Python | MIT | 1 |

**Live football scores** via SoccerDataAPI — a single `get_livescores()` tool that retrieves current match data globally. Despite the single tool, it returns rich data: team names, kickoff times, scores, goal breakdowns, substitutions, cards, penalties, lineups, formations, injury status, and even betting odds. Stars grew 28→30. Still the highest-starred dedicated soccer MCP server.

### billychl1/footballbin-mcp-server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [billychl1/footballbin-mcp-server](https://github.com/billychl1/footballbin-mcp-server) | 0 | JavaScript | MIT | 1 |

**NEW.** AI-powered **football match predictions** for Premier League and UEFA Champions League:

- Half-time/full-time score predictions
- Next goal scorer predictions
- Corner count predictions
- Key player insights with reasoning

Team alias support for common club nicknames. Available via npm, npx, remote HTTPS endpoint, or Claude Desktop. A different angle — predictions rather than historical data.

### yalmeidarj/mcp-football-server

A lightweight MCP tool server providing football data via API-Football. Another API-Football wrapper, but simpler than obinopaul's 17-tool version.

**European football coverage greatly expanded** via the official Balldontlie MCP server — EPL, La Liga, Serie A, Bundesliga, Ligue 1, and UEFA Champions League are all now accessible.

## Ice Hockey (NHL)

### dylangroos/nhl-mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [dylangroos/nhl-mcp](https://github.com/dylangroos/nhl-mcp) | 5 | TypeScript | MIT | 10 |

A **solid NHL data server** with 10 tools covering the essentials:

- **Teams** — team info, rosters, stats, prospects
- **Players** — biographical data and career/season statistics
- **Standings** — league-wide standings with division breakdowns
- **Schedule** — upcoming games, date-specific league schedules
- **Statistics** — current stat leaders for skaters and goalies
- **Live scores** — current game states and scores

Uses the official NHL API. Stars grew 4→5.

### argotdev/nhl-mcp-ts

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [argotdev/nhl-mcp-ts](https://github.com/argotdev/nhl-mcp-ts) | 0 | JavaScript/TypeScript | MIT | 11 |

**NEW.** A **feature-rich NHL server** with 11 tools and natural language query capabilities:

- Live game scores and game details
- Standings with division/conference filtering
- Player and goalie statistics with sortable categories
- Playoff bracket tracking
- **Head-to-head team comparisons** — unique feature
- **Historical season-to-season analysis** — compare any two seasons
- **Winning/losing streak monitoring**

Also available as **argotdev/nhl-mcp-python** — an idiomatic Python implementation with the same feature set. The comparison and streak features go beyond basic data retrieval.

### sanchorelaxo/mcp-server-sandbox

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [sanchorelaxo/mcp-server-sandbox](https://github.com/sanchorelaxo/mcp-server-sandbox) | 3 | — | — | Multiple |

**NEW.** A **comprehensive NHL API MCP server** built with FastMCP, providing access to all documented NHL API endpoints through MCP tools. Broader endpoint coverage than the other NHL implementations.

**NHL went from 1 implementation to 4+** — the biggest proportional growth of any sport in this review.

## Formula 1 / Motorsport

### Panth1823/formula1-mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [Panth1823/formula1-mcp](https://github.com/Panth1823/formula1-mcp) | 15 | TypeScript | — | 29 |

The **most comprehensive F1 MCP server** — 29 tools combining two data sources:

- **OpenF1 API** (2023-present) — real-time telemetry (speed, throttle, brake, RPM, DRS, gear), team radio communications with audio URLs, race control messages/flags/penalties, pit stop data, tire strategy, weather data, lap times, sector analysis, position tracking
- **Ergast API** (1950-2024) — historical race results, driver/constructor standings, circuit info

Free historical access without authentication. Live streaming available via paid OpenF1 MQTT access. Remarkable depth for a single racing series.

### drivenrajat/f1

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [drivenrajat/f1](https://github.com/drivenrajat/f1) | 1 | Python | MIT | 36+ |

**NEW.** The **highest tool count F1 server** — 36+ tools integrating FastF1, Ergast API, and OpenF1 API:

- Race results, sprint races, qualifying progression, and DNF information
- Telemetry analysis with speed traces, gear shifts, braking, and DRS patterns
- Timing and lap data with sector times and consistency statistics
- Strategy information covering tire compounds, pit stops, and stints
- Championship standings for drivers and constructors
- Live session data including real-time positions and weather conditions
- Team radio links and race control messages
- Automatic caching for improved performance

Covers 2018-present. The most tools of any F1 server, combining all three major F1 data sources.

### aashnakunk/fastf1-mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [aashnakunk/fastf1-mcp](https://github.com/aashnakunk/fastf1-mcp) | 1 | Python | MIT | 17 |

**NEW.** A **well-tested F1 analytics server** — 17 tools backed by **133 tests** covering protocol, normalization, and tool execution:

- Session loading, results retrieval, lap timing analysis
- Pit stop tracking, telemetry access, comparative driver analysis
- Fuzzy input normalization for natural language queries about drivers and races
- Dual functionality as both MCP server and standalone Python library
- Data coverage from 2018 onwards (race, qualifying, sprint, practice)
- Caching system for instant subsequent loads

The test suite depth (133 tests) sets this apart — most F1 servers have minimal or no tests. No hosted API or credentials required — all local processing.

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

Multi-year support from 2018-2025. This is genuine sports analytics, not just data retrieval — the strategy simulation and driver extraction features are research-grade.

### Additional F1 Implementations

- **rakeshgangwar/f1-mcp-server** (10 stars) — FastF1 library for historical analysis
- **Machine-To-Machine/f1-mcp-server** — Python, event schedules, telemetry, race results
- **Darakhsh1999/f1-mcp-server** — FastF1 + OpenF1 combined
- **AryaAkman/Open-F1-MCP-Server** — OpenF1 API wrapper for real-time data
- **hydavinci/formula-1-schedule** — race schedules, standings, results for any year via FastMCP

Formula 1 now has **10+ MCP implementations** (up from 7+), making it the most MCP-served single sport. The 2026 F1 regulation changes (ground-effect aerodynamics, new power units) likely drive continued developer interest.

## Fantasy Sports

### derekrbreese/fantasy-football-mcp-public

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [derekrbreese/fantasy-football-mcp-public](https://github.com/derekrbreese/fantasy-football-mcp-public) | 34 | Python | MIT | 16+ |

**NEW.** Now the **highest-starred fantasy sports MCP server** — Yahoo Fantasy Football with advanced AI-driven features:

- **Intelligent lineup optimization** with matchup-aware algorithms and strategy modes (conservative, aggressive, balanced)
- **Draft assistant** with real-time recommendations and VORP (Value Over Replacement Player) calculations
- **Multi-source projections** combining Yahoo and Sleeper expert rankings
- **Reddit sentiment analysis** for player buzz and injury updates
- **Bye week detection** and performance flags (breakout candidates, trending players)
- **Position normalization** for smart FLEX decisions
- **Multi-league support** with automatic discovery of all associated Yahoo leagues

Built with Claude Code. Multiple deployment options (FastMCP, traditional MCP, Docker, cloud). Comprehensive caching with TTL management. This is the most sophisticated fantasy server by far — the combination of VORP calculations, Reddit sentiment, and strategy-based optimization goes well beyond basic data access.

### KBThree13/mcp_espn_ff

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [KBThree13/mcp_espn_ff](https://github.com/KBThree13/mcp_espn_ff) | 30 | Python | MIT | 6 |

**ESPN Fantasy Football** — league information, roster viewing, player stats, standings, weekly matchups, and secure private league access. Stars grew 29→30. Simple and focused — if you play ESPN Fantasy Football, this gets AI access to your league in minutes.

### spilchen/yahoo_fantasy_mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [spilchen/yahoo_fantasy_mcp](https://github.com/spilchen/yahoo_fantasy_mcp) | 1 | Python | MIT | 24 |

**NEW.** A **comprehensive Yahoo Fantasy wrapper** — 24 tools across six categories:

- **League Information** (8 tools) — settings, standings, scoreboard, teams, players
- **Matchups & Scoring** (2 tools) — weekly matchup data and scoring details
- **Team Management** (4 tools) — roster, lineup changes, waiver claims
- **Player Information** (4 tools) — search, stats, ownership, projections
- **Transactions** (1 tool) — league transaction history

Read-only access via the yahoo_fantasy_api library. Covers all Yahoo Fantasy sports (Football, Baseball, Basketball, Hockey). The broadest Yahoo Fantasy coverage available.

### jimbrig/yahoo-fantasy-baseball-mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [jimbrig/yahoo-fantasy-baseball-mcp](https://github.com/jimbrig/yahoo-fantasy-baseball-mcp) | 3 | TypeScript/JavaScript | MIT | 1+ |

**NEW.** Yahoo Fantasy Baseball specifically — OAuth 1.0a authentication, team roster and player statistics. Currently 1 tool (get_team_roster) with waiver wire and matchup tools coming soon. Early but focused.

### JayMishra-source/Fantasy-Football-AI-CoManager

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [Fantasy-Football-AI-CoManager](https://github.com/JayMishra-source/Fantasy-Football-AI-CoManager) | 1 | TypeScript | MIT | 10+ |

**NEW.** An **automated ESPN Fantasy Football management system** combining GitHub Actions with Claude Desktop MCP:

- Automated lineup optimization using projections and matchups
- Waiver wire analysis for breakout players
- Trade evaluation with projected impact
- FantasyPros rankings integration
- Discord webhook notifications
- Scheduled automation (daily at 8 AM ET, hourly during games)

Three deployment paths: automated GitHub Actions ("set and forget"), interactive Claude Desktop, and local web interface.

### jdguggs10/flaim

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [jdguggs10/flaim](https://github.com/jdguggs10/flaim) | 3 | TypeScript | MIT | 9 |

A **unified multi-platform fantasy connector** — ESPN, Yahoo, and Sleeper leagues in one MCP server covering Football, Baseball, Basketball, and Hockey. Read-only design prevents accidental trades. Stars tripled 1→3.

**Fantasy sports went from 2 servers to 7+** — the biggest category expansion in this refresh. Yahoo Fantasy went from zero dedicated coverage to three implementations. The derekrbreese server at 34 stars is now the highest-starred fantasy MCP server by a wide margin.

## Betting & Odds

### WFord26/BetTrack

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [WFord26/BetTrack](https://github.com/WFord26/BetTrack) | 3 | TypeScript | MIT | 30+ |

The **most comprehensive sports betting MCP server** — 30+ tools covering 70+ betting markets:

- Live odds from The Odds API across multiple bookmakers
- NFL, NBA, NCAAB, NHL, MLB, EPL, UEFA Champions League, College Football
- Line movement analysis and odds history visualization
- Bet tracking with parlay and futures support
- Player props across all major sports
- Retro 8-bit web dashboard (React frontend)
- PostgreSQL backend for historical data

Full-stack application: FastMCP (Python 3.11+), React 18, Node.js 20, Prisma ORM, PostgreSQL 16.

### kitchenchem/degen-mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [kitchenchem/degen-mcp](https://github.com/kitchenchem/degen-mcp) | 1 | Python | — | Multiple |

A **simpler odds comparison tool** via The Odds API — available sports, odds across bookmakers, and API quota tracking. Installable via npx. Less ambitious than BetTrack but useful for quick odds lookups.

### Cloudbet Sports MCP Server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [cloudbet/sports-mcp-server](https://github.com/cloudbet/sports-mcp-server) | 11 | Go | MIT | 1 |

A **minimal MCP implementation** from Cloudbet (crypto sports betting platform). Single tool: `findEventsAndMarketsByCompetition`. Exposes live market data for competitions including the Premier League. Stars grew 10→11.

## Fitness & Training

*Note: For comprehensive fitness and wearable coverage including Oura Ring (22 implementations), TrainingPeaks, COROS, Intervals.icu, MacroFactor, Cronometer, and updated Garmin/Strava data, see our dedicated [Sports & Fitness MCP review](/reviews/sports-fitness-mcp-servers/).*

### r-huijts/strava-mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [r-huijts/strava-mcp](https://github.com/r-huijts/strava-mcp) | 357 | TypeScript | MIT | 25 |

The **highest-starred sports MCP server** — 25 tools for Strava fitness data. Stars surged **276→357 (+29%)**. v1.2.1 with active April 2026 development. New features include sport-type icons, local timestamps, segment leaderboards, athlete shoes, and activity streams with ~70-80% data size reduction. Strava has 120M+ users.

### Taxuspt/garmin_mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [Taxuspt/garmin_mcp](https://github.com/Taxuspt/garmin_mcp) | 407 | Python | — | 96+ |

A **massive Garmin Connect integration** — 96+ tools covering 89% of the python-garminconnect library. Stars surged **271→407 (+50%)**. Community PRs added nutrition endpoints, delete_workout, and activity splits with elevation. Activities, health metrics (steps, heart rate, sleep, stress, respiration, HRV), training, workouts, devices, gear, weight, challenges, nutrition, and women's health.

### gesteves/domestique

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [gesteves/domestique](https://github.com/gesteves/domestique) | 0 | TypeScript | — | 30+ |

A **multi-platform fitness aggregator** connecting Intervals.icu, Whoop, TrainerRoad, and CORE Body Temperature sensors. 30+ tools spanning today's data, historical trends, workout management, and performance curves. Targets serious endurance athletes using multiple platforms.

### AI Endurance MCP Server (Commercial)

| Server | Type | Tools |
|--------|------|-------|
| [AI Endurance MCP](https://aiendurance.com/docs/mcp) | Commercial (hosted) | Multiple |

A **commercial training platform** with native MCP support for cycling, running, and swimming. Training plans, periodization, performance predictions, and recovery metrics. The first commercial training platform with direct MCP integration.

## Professional Cycling

### r-huijts/firstcycling-mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [r-huijts/firstcycling-mcp](https://github.com/r-huijts/firstcycling-mcp) | 18 | Python | MIT | 20 |

**Professional cycling data** from FirstCycling.com — rider profiles, career stats, Grand Tour results, Monument classics, team history, race results, startlists, and stage profiles. 10 rider tools, 8 race tools, 2 search tools. Covers the full spectrum of professional road cycling.

## Cricket

### tarun7r/cricket-mcp-server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [tarun7r/cricket-mcp-server](https://github.com/tarun7r/cricket-mcp-server) | 12 | Python | MIT | 9 |

**Comprehensive cricket data** from Cricbuzz — player stats across Test/ODI/T20 formats, live matches, schedules, news, ICC rankings, detailed scorecards, and ball-by-ball commentary. Includes a Gradio-based web interface. Stars grew 11→12.

Cricket coverage expanded significantly — see our [Sports & Fitness MCP review](/reviews/sports-fitness-mcp-servers/) for mavaali/cricket-mcp (28 tools, DuckDB, 21K matches, 10.9M ball-by-ball deliveries) and the FIFA World Cup 2026 MCP server (18 tools).

## What's Missing

The gap list shrank significantly since the initial review:

- ~~**Esports**~~ — **FILLED** via official Balldontlie MCP (CS2, League of Legends, Dota 2). No dedicated esports-only servers yet, but coverage exists.
- ~~**Baseball-specific**~~ — **FILLED** via official Balldontlie MCP (MLB) and dedicated servers like robcerda/mlb-sportradar-mcp.
- ~~**WNBA**~~ — **FILLED** via official Balldontlie MCP.
- ~~**College sports**~~ — **FILLED** via official Balldontlie MCP (NCAAF, NCAAB).
- ~~**Tennis**~~ — **PARTIALLY FILLED** via sportscore-mcp (live scores, standings) and SportRadar MCP. Tennis Warehouse MCP exists for product data. No dedicated match analytics server yet.
- **Rugby** — still no rugby union or rugby league servers
- **Golf** — PGA of America has an official MCP at mcp.pga.com (see [Sports & Fitness review](/reviews/sports-fitness-mcp-servers/)), but no open-source implementations
- **Olympic sports / Athletics** — no track & field, swimming, or gymnastics data
- **Youth / amateur sports** — all servers focus on professional leagues
- **Sports news aggregation** — no dedicated sports journalism or highlight servers

## Bottom Line

**Rating: 4.5/5** (upgraded from 4/5) — Sports and athletics is now one of the strongest MCP categories by both volume and quality. The official Balldontlie MCP server alone fills four major gaps (esports, WNBA, college sports, European football) with 250+ endpoints across 18 leagues. Fitness tracking continues to lead with two 350+ star servers (Strava 357, Garmin 407). Fantasy sports exploded from 2 to 7+ servers with a sophisticated 34-star Yahoo FF implementation. Formula 1 reached 10+ implementations. NHL went from 1 to 4+ servers. The only significant remaining gaps are rugby, golf (open-source), and Olympic sports. For anyone building sports-related AI tools, this ecosystem is remarkably comprehensive.

*This review was refreshed on 2026-04-27 using Claude Opus 4.6 (Anthropic). [Rob Nugen](https://robnugen.com) is the human behind ChatForest.*
