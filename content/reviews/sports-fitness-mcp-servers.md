---
title: "Sports & Fitness MCP Servers — Strava, Garmin, Fitbit, F1, NFL, MLB, Soccer, and More"
date: 2026-03-15T14:00:00+09:00
description: "Sports and fitness MCP servers are connecting AI assistants to workout data, live scores, and athletic performance analytics. We reviewed 50+ servers across 9 subcategories."
og_description: "Sports & fitness MCP servers: Garmin Connect (1,000+ stars, 110+ tools), Strava (471 stars, 25 tools), Apple Health (251 stars), garmin-givemydata (140 stars, 45 tools — local SQLite with data sovereignty), MLB stats (57 stars, 21+ tools), F1 racing (15 stars, 29 tools), Fitbit (33 stars, 12 tools), multi-sport via Balldontlie (505 tools across 27 sports), ESPN Fantasy Football (37 stars), Oura Ring (17 tools), TrainingPeaks (139 stars, 58 tools), COROS (111 stars, 15 tools). PGA of America and MySwimPro launched official MCP servers. Rating: 4.5/5."
content_type: "Review"
card_description: "Sports and fitness MCP servers for workout tracking, live scores, athletic analytics, and fantasy sports. This is one of the deepest MCP categories — Garmin Connect has 110+ tools covering activities, health metrics, workouts, devices, nutrition, and challenges, now at over 1,000 stars. Strava grew to 471 stars with 25 tools. A data-sovereignty approach: nrvim/garmin-givemydata (140 stars, 45 MCP tools) stores Garmin data in local SQLite with Cloudflare bypass and professional training metrics (CTL/ATL/TSB). The TypeScript Garmin alternative (Nicolasvegam/garmin-connect-mcp) grew to 168 stars with 61 tools. Apple Health hit 251 stars. COROS grew to 111 stars. TrainingPeaks reached 139 stars. sportscore-mcp — free multi-sport API (football, basketball, cricket, tennis) with 8 tools. For spectator sports, Balldontlie now covers 27 sports/leagues with 505 tools. Two official first-party servers: PGA of America (mcp.pga.com) and MySwimPro (mcp.myswimpro.com). Remaining gaps: rugby, Peloton, CrossFit. Rating: 4.5/5 — fitness wearable coverage is best-in-class across the entire MCP ecosystem."
last_refreshed: 2026-04-30
sources_audited: 2026-08-18
categories: ["/categories/sports-fitness/"]
---

Sports and fitness MCP servers are connecting AI assistants to workout data, live scores, and athletic performance analytics. Instead of manually checking Garmin Connect for your training load or scrolling ESPN for box scores, these servers let AI agents query your fitness history, analyze race telemetry, pull real-time scores, and even manage fantasy lineups — all through the Model Context Protocol.

The landscape spans nine areas: **fitness wearables** (Garmin, Strava, Fitbit, Apple Health, WHOOP, Oura Ring, COROS), **endurance training platforms** (TrainingPeaks, Intervals.icu, AI Endurance), **motorsport** (Formula 1), **multi-sport data platforms** (Balldontlie covering 27 sports/leagues), **baseball** (MLB stats and sabermetrics), **football** (NFL and fantasy), **soccer and cycling** (live scores, World Cup 2026, professional racing data), **sports betting/fantasy** (odds, props, lineup optimization), and **nutrition tracking** (Cronometer, MacroFactor, MyFitnessPal).

The headline findings: **Garmin Connect has grown past 1,000 stars** ([live count](https://github.com/Taxuspt/garmin_mcp)), remaining the most comprehensive fitness MCP server with 110+ tools covering the python-garminconnect library. **A data-sovereignty Garmin server** — nrvim/garmin-givemydata ([140 stars](https://github.com/nrvim/garmin-givemydata)) takes a fundamentally different approach: local SQLite storage, Cloudflare bypass via SeleniumBase, and professional training metrics (CTL/ATL/TSB, recovery signatures, health anomaly detection). The TypeScript alternative Nicolasvegam/garmin-connect-mcp grew to [168 stars](https://github.com/Nicolasvegam/garmin-connect-mcp) with 61 tools. **Strava reached [471 stars](https://github.com/r-huijts/strava-mcp)** with active development. **COROS grew to [111 stars](https://github.com/cygnusb/coros-mcp)**. TrainingPeaks hit [139 stars](https://github.com/JamsusMaximus/trainingpeaks-mcp). **A multi-sport data server** — sportscore-mcp provides free access to football, basketball, cricket, and tennis via the SportScore API with 8 tools. **Two official first-party servers** remain active — PGA of America ([mcp.pga.com](https://mcp.pga.com/)) and MySwimPro ([mcp.myswimpro.com](https://mcp.myswimpro.com/)). Apple Health grew to [251 stars](https://github.com/the-momentum/apple-health-mcp-server), evolving into Open Wearables supporting multiple wearable ecosystems.

## Fitness Wearables

### Garmin Connect MCP Server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [Taxuspt/garmin_mcp](https://github.com/Taxuspt/garmin_mcp) | 1,000+ | Python | MIT | 110+ |

The **most comprehensive fitness MCP server** we've seen in any category. This server wraps the python-garminconnect library and exposes an enormous surface area across 10 tool categories:

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

With over 1,000 stars, this is one of the fastest-growing fitness MCP servers. The sheer tool count (110+) rivals enterprise API integrations — and all of it is community-built, since Garmin has no official MCP server.

#### Garmin Connect MCP — TypeScript Alternative

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [Nicolasvegam/garmin-connect-mcp](https://github.com/Nicolasvegam/garmin-connect-mcp) | 168 | TypeScript | MIT | 61 |

A TypeScript-based Garmin server with 168 stars and 61 tools across 7 categories: activities (12), daily health (14), trends (4), sleep (2), body composition (5), performance/training (11), and profile/devices (13). Supports MFA authentication and works with Claude Code, Claude Desktop, Cursor, and Windsurf. If you prefer TypeScript tooling or need a lighter-weight alternative to the 110-tool Python server, this is a strong option.

#### Other Garmin MCP Servers

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [st3v/garmin-workouts-mcp](https://github.com/st3v/garmin-workouts-mcp) | 26 | Python | MIT | 11 |
| [charlesfrisbee/garmin-workouts-mcp](https://github.com/charlesfrisbee/garmin-workouts-mcp) | 2 | TypeScript | — | 5 |

**st3v/garmin-workouts-mcp** focuses specifically on workout creation — you describe a workout in natural language ("40 minute tempo run with 10 minute warmup") and it generates and uploads the structured workout to Garmin Connect. It also includes activity viewing and calendar management.

*(A third server previously listed here, jlwainwright/garmin-mcp-server, has been removed from GitHub and is no longer available — checked 2026-08-18.)*

#### Garmin Data Sovereignty: garmin-givemydata

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [nrvim/garmin-givemydata](https://github.com/nrvim/garmin-givemydata) | 140 | Python | AGPL-3.0 | 45 |

A **fundamentally different approach** to Garmin data — this server extracts your entire Garmin Connect history into a local SQLite database and provides 45 contextual MCP tools for AI analysis. Key differentiators:

- **Cloudflare bypass** via SeleniumBase UC mode — works around the bot detection that has broken competing libraries like garth and python-garminconnect
- **Data sovereignty** — all data stays local, never leaves your machine, with browser session persistence lasting ~1 year
- **Contextual AI tools** — rather than returning raw data, tools include trend directions, anomaly flags, clinical thresholds, and goal attainment metrics
- **Professional training metrics** — CTL/ATL/TSB training load, recovery signatures by sport, periodization analysis typically found only in premium coaching platforms
- **Smart sync** — incremental updates and historical data recovery (10+ years)
- **Multiple export formats** — CSV, JSON, GPX, TCX alongside original FIT files

With 140 stars, this remains one of the fastest-growing Garmin MCP servers. The "it's YOUR data" philosophy resonates — if you want complete ownership and offline access to your Garmin history with AI-ready analytics, this fills a gap the API-based servers can't.

### Strava MCP Server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [r-huijts/strava-mcp](https://github.com/r-huijts/strava-mcp) | 471 | TypeScript | MIT | 25 |

The **highest-starred sports MCP server** in the ecosystem, with active development, 25 tools across six categories:

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
| [TheDigitalNinja/mcp-fitbit](https://github.com/TheDigitalNinja/mcp-fitbit) | 33 | TypeScript | MIT | 12 |

A solid integration, published as an npm package. Covers the core Fitbit data types:

- Exercise and activity logs
- Sleep analysis (stages, duration, quality)
- Heart rate monitoring (resting, zones, intraday)
- Weight tracking and body composition
- Nutrition logging and calorie tracking
- Activity summaries (steps, distance, calories burned)

Works with Claude Desktop and other MCP-compatible clients. Actively maintained as of this audit (2026-08-18).

### Apple Health MCP Server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [the-momentum/apple-health-mcp-server](https://github.com/the-momentum/apple-health-mcp-server) | 251 | Python | MIT | — |

A clever approach — rather than connecting to a live API, this server imports Apple Health XML exports and loads them into DuckDB for lightning-fast natural language queries. You export your health data from your iPhone, point the server at the file, and then ask questions like "what's my average resting heart rate this month?" or "show my sleep duration trends."

The DuckDB backend means queries over years of health data run in milliseconds. The project has evolved into Open Wearables, a broader platform supporting Garmin, Polar, Suunto, and Whoop data alongside Apple Health.

### WHOOP MCP Server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [JedPattersonn/whoop-mcp](https://github.com/JedPattersonn/whoop-mcp) | 13 | TypeScript | MIT | 5 |

Integrates WHOOP's biometric data with 5 focused tools:

- **Overview** — daily summary of strain, recovery, sleep
- **Sleep** — detailed sleep metrics and staging
- **Recovery** — HRV, resting heart rate, recovery score
- **Strain** — daily strain score and activity breakdown
- **Healthspan** — WHOOP's longevity and health trend metrics

Small but functional — covers the core WHOOP data that athletes care about most.

### Oura Ring MCP Servers

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [rajvirtual/oura-mcp-server](https://github.com/rajvirtual/oura-mcp-server) | 14 | TypeScript | — | — |
| [mitchhankins01/oura-ring-mcp](https://github.com/mitchhankins01/oura-ring-mcp) | 26 | TypeScript | MIT | 17 |
| [daveremy/oura-mcp](https://github.com/daveremy/oura-mcp) | 4 | TypeScript | MIT | 10 |

Oura Ring has a healthy field of community MCP servers. The most feature-rich is **mitchhankins01/oura-ring-mcp** with 17 tools: 10 data retrieval tools (sleep, readiness, activity, workouts, sessions, heart rate, stress, SpO2, tags) plus 7 smart analysis tools (anomaly detection, sleep quality scoring, metric correlation, period comparison, best sleep conditions, HRV trend analysis). Published on npm as `oura-ring-mcp`. Includes MCP Resources (today, weekly-summary, baseline, monthly-insights) and analysis Prompts.

**rajvirtual/oura-mcp-server** (14 stars) focuses on sleep analysis, readiness scores, HRV tracking, and stress comparisons. **daveremy/oura-mcp** (4 stars) doubles as a standalone CLI tool and Claude Code skill with 10 tools covering daily summaries, sleep, readiness, activity, workouts, heart rate, stress, SpO2, sessions, and trends.

⚠️ **Security note**: A trojanized Oura MCP server was discovered in February 2026, [distributing the SmartLoader/StealC infostealer via fake forks](https://www.straiker.ai/blog/smartloader-clones-oura-ring-mcp-to-deploy-supply-chain-attack) ([The Hacker News](https://thehackernews.com/2026/02/smartloader-attack-uses-trojanized-oura.html)). Only install Oura MCP servers from verified, well-starred repositories.

### COROS MCP Server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [cygnusb/coros-mcp](https://github.com/cygnusb/coros-mcp) | 111 | Python | MIT | 15 |
| [rowlando/coros-workout-mcp](https://github.com/rowlando/coros-workout-mcp) | 27 | TypeScript | MIT | — |

**COROS joins the wearable ecosystem** — cygnusb/coros-mcp (111 stars, 15 tools) covers sleep, HRV, daily metrics, activities, and structured workouts. Authenticates directly with COROS Training Hub (no API key needed). Supports workout creation with power targets and interval groups. Actively developed; the project's own README now notes that COROS has since released an official first-party MCP server as well.

**rowlando/coros-workout-mcp** (27 stars) focuses specifically on creating COROS strength workouts via the Training Hub API.

### MyFitnessPal MCP Server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [AdamWalt/myfitnesspal-mcp-python](https://github.com/AdamWalt/myfitnesspal-mcp-python) | 46 | Python | MIT | — |
| [ai-mcp-garage/mcp-myfitnesspal](https://github.com/ai-mcp-garage/mcp-myfitnesspal) | 0 | Python | — | — |

Two community implementations for pulling nutrition data from MyFitnessPal — food diaries, exercise logs, body measurements, nutrition goals, and water intake. AdamWalt's implementation has picked up real traction; ai-mcp-garage's has none yet.

### Multi-Platform: Pierre Fitness

*Previously covered here: Async-IO/pierre_mcp_server, an aggregator server connecting to multiple wearables via Strava, Garmin, Fitbit, WHOOP, COROS, and Terra. As of this audit (2026-08-18) the repository at github.com/Async-IO/pierre_mcp_server returns 404 and does not appear under any renamed/transferred location we could find — it has been removed from GitHub. This entry has been cut since there is no longer a live source to verify the claims against.*

## Endurance Training Platforms

### TrainingPeaks MCP Server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [JamsusMaximus/trainingpeaks-mcp](https://github.com/JamsusMaximus/trainingpeaks-mcp) | 139 | Python | MIT | 58 |

A strong option for endurance athletes — 58 tools covering structured interval workouts, calendar management, fitness metrics (CTL/ATL/TSB), and equipment tracking. Uses cookie-based authentication (no API approval needed) with encrypted credential storage. If you're a triathlete, cyclist, or runner who trains with TrainingPeaks, this is a direct pipeline between your AI assistant and your training plan.

### Intervals.icu MCP Server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [eddmann/intervals-icu-mcp](https://github.com/eddmann/intervals-icu-mcp) | 35 | Python | MIT | 48 |

Comprehensive integration with the popular Intervals.icu training platform — 48 tools spanning activities, analysis, wellness, events/calendar, performance curves, workout library, gear management, and sport settings. Also includes 6 MCP Prompts and 1 Resource. Intervals.icu is the free alternative to TrainingPeaks favored by data-oriented endurance athletes.

### Nutrition: Cronometer & MacroFactor

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [cphoskins/cronometer-mcp](https://github.com/cphoskins/cronometer-mcp) | 17 | Python | MIT | — |
| [sjawhar/macrofactor](https://github.com/sjawhar/macrofactor) | 24 | TypeScript | MIT | 28 (non-functional) |

Cronometer MCP provides food logs, macro/micro summaries, diary entries, fasting data, and biometrics. Requires Cronometer Gold (paid tier).

**sjawhar/macrofactor** (24 stars, 28 tools) covers nutrition tracking, workout history, food database search, and weight logging. Includes a CLI, MCP server, and SvelteKit web app. ⚠️ **Update (checked 2026-08-18): this server is currently broken and archived.** As of May 25, 2026, MacroFactor's developer (Stronger By Science) enabled Firebase App Check enforcement on the backend sign-in endpoint; every authentication request from this client now fails with a `401 Firebase App Check token is invalid` error. The [repository is archived](https://github.com/sjawhar/macrofactor) and the maintainer's own README says it is preserved for reference only, with no known fix. Do not rely on this server for MacroFactor access.

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
| [rakeshgangwar/f1-mcp-server](https://github.com/rakeshgangwar/f1-mcp-server) | 11 | JavaScript | MIT | 8 |
| [Darakhsh1999/f1-mcp-server](https://github.com/Darakhsh1999/f1-mcp-server) | 1 | Python | MIT | — |
| [stagsz/F1-MCP-Server](https://github.com/stagsz/F1-MCP-Server) | 5 | JavaScript | MIT | 12 |
| [AryaAkman/Open-F1-MCP-Server](https://github.com/AryaAkman/Open-F1-MCP-Server) | 3 | Python | — | 5 |

**rakeshgangwar/f1-mcp-server** uses the FastF1 Python library for telemetry analysis and driver comparison. **stagsz/F1-MCP-Server** goes furthest with tire degradation modeling, Monte Carlo race strategy simulation, and weather forecasting. The sheer number of F1 servers reflects both the sport's data-rich nature (telemetry, timing, weather) and its technically-inclined fanbase.

## Multi-Sport Data Platforms

### Balldontlie Official MCP Server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [balldontlie-api/mcp](https://github.com/balldontlie-api/mcp) | 12 | TypeScript | MIT | 505 |

The **broadest sports data MCP server** available. As of this audit (2026-08-18) the [live repository README](https://github.com/balldontlie-api/mcp) reports **505 tools generated from 27 sport/league specifications**: Account, ATP, Bundesliga, college baseball, Counter-Strike, Dota 2, EPL, F1, FIFA World Cup, La Liga, Ligue 1, League of Legends, MLB, MLS, MMA, NBA, NCAAB, NCAAF, NCAAW, NFL, NHL, PGA, Serie A, UEFA Champions League, Valorant, WNBA, and WTA. The README does not publish a per-league tool-count breakdown, so the previous per-sport tool figures on this page have been removed rather than guessed at.

This is an API wrapper rather than a deep analytics platform — you get teams, players, games, and stats, but not advanced analytics like sabermetrics. Requires a Balldontlie API key.

### Balldontlie Community Server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [mikechao/balldontlie-mcp](https://github.com/mikechao/balldontlie-mcp) | 26 | JavaScript | MIT | 4 |

A simpler community implementation with 4 core tools (get_teams, get_players, get_games, get_game) plus a schedule_generator prompt. More focused than the official server — good for quick lookups rather than deep analysis.

## Baseball (MLB)

### MLB API MCP Server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [guillochon/mlb-api-mcp](https://github.com/guillochon/mlb-api-mcp) | 57 | Python | MIT | 21+ |

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
| [etweisberg/mlb-mcp](https://github.com/etweisberg/mlb-mcp) | 32 | Python | — | 4 |

Focused on **advanced baseball analytics** by integrating Statcast, FanGraphs, and Baseball Reference data through the pybaseball library. Fewer tools than guillochon's server but deeper analytical capabilities — pitch-level Statcast data, FanGraphs leaderboards, and Baseball Reference historical stats.

## Football (NFL) & Fantasy

### NFL MCP Server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [gtonic/nfl_mcp](https://github.com/gtonic/nfl_mcp) | 13 | Python | MIT | 70+ |

This server has grown substantially since our last check — the [live README](https://github.com/gtonic/nfl_mcp) now reports 70+ tools organized across draft & player values (VBD-ranked boards, mock drafts, trade analysis), weekly lineup & projections, matchup & schedule intelligence, season strategy (Monte Carlo playoff-odds simulation), waivers/FAAB, Sleeper league integration, injuries & availability, NFL data & news, coaching intelligence, CBS Sports data, and player/athlete search.

The lineup optimization and playoff-odds tools make this particularly useful for fantasy football — getting AI-powered start/sit recommendations backed by actual data.

### ESPN Fantasy Football MCP

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [KBThree13/mcp_espn_ff](https://github.com/KBThree13/mcp_espn_ff) | 37 | Python | MIT | 6 |

Connects Claude to ESPN Fantasy Football leagues with 6 tools: authentication, league info, team rosters, player stats, standings, and matchup details. Works with both public and private ESPN leagues. Simple but covers the core fantasy football workflow.

### Yahoo Fantasy Baseball MCP

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [jimbrig/yahoo-fantasy-baseball-mcp](https://github.com/jimbrig/yahoo-fantasy-baseball-mcp) | 4 | TypeScript | MIT | 1 (3 planned) |

Early-stage with only `get_team_roster` implemented. Waiver player and matchup tools are marked "coming soon." More a proof of concept than a usable tool at this point.

## Soccer & Cycling

### Soccer Data MCP Server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [yeonupark/mcp-soccer-data](https://github.com/yeonupark/mcp-soccer-data) | 39 | Python | MIT | 1 |

Provides real-time football (soccer) data through a single `get_livescores()` tool, but that tool delivers 6 data categories: match listings, detailed match info, live events, team lineups, betting odds, and league metadata. Good for checking scores during matches, but limited scope compared to what Balldontlie offers for EPL.

### FIFA World Cup 2026 MCP

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [jordanlyall/wc26-mcp](https://github.com/jordanlyall/wc26-mcp) | 35 | TypeScript | MIT | 18 |

A server built ahead of the 2026 World Cup — 18 tools covering matches, teams, venues, city guides, fan zones, visa info, head-to-head records, and more. No API key needed (all data built-in).

### SportScore MCP Server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [Backspace-me/sportscore-mcp](https://github.com/Backspace-me/sportscore-mcp) | 10 | JavaScript | MIT | 8 |

A multi-sport data server exposing the free SportScore API — live scores, match details, standings, top scorers, brackets, and player stats across **football, basketball, cricket, and tennis**. No API key required. Works with Claude Desktop, Cursor, and Zed. A lightweight alternative to Balldontlie for these four sports, with the advantage of no API key requirement.

### Cricket MCP Servers

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [tarun7r/cricket-mcp-server](https://github.com/tarun7r/cricket-mcp-server) | 14 | Python | MIT | 9 |
| [mavaali/cricket-mcp](https://github.com/mavaali/cricket-mcp) | 2 | TypeScript | MIT | 14 |

**Cricket went from a gap to well-served** — tarun7r/cricket-mcp-server (14 stars, 9 tools) covers Cricbuzz data with ICC rankings and live commentary. The bigger story is **mavaali/cricket-mcp** — the [live repo description](https://github.com/mavaali/cricket-mcp) puts it at **14 tools** (this page previously said 28 — corrected 2026-08-18) backed by a DuckDB database of 21,000+ matches and 10.9 million ball-by-ball deliveries from Cricsheet. This is serious cricket analytics — the kind of depth that baseball's mlb-api-mcp provides for its sport.

### Professional Cycling (FirstCycling)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [r-huijts/firstcycling-mcp](https://github.com/r-huijts/firstcycling-mcp) | 19 | Python | MIT | 20 |

A niche but well-built server for professional cycling data from FirstCycling:

- **Rider Tools** (10) — biographical data, career results, race history, victories, team progression
- **Race Tools** (8) — results, profiles, starters, victory tables, age records
- **Search** (2) — rider and race search

Perfect for cycling fans who want to ask things like "who has won the most Tour de France stages in the last decade?" Built by the same developer as the Strava MCP server.

## Sports Betting

### BetTrack

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [WFord26/BetTrack](https://github.com/WFord26/BetTrack) | 14 | TypeScript | MIT | 30+ |

A sports betting companion with 30+ tools across 7+ major sports. Includes player props, live scores, visual artifacts, and an optional React dashboard for bet tracking.

### Other Betting & Odds Servers

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [marcoeg/mcp-odds-api](https://github.com/marcoeg/mcp-odds-api) | 4 | Python | Apache-2.0 | 3 |
| [nikhilkichili/nba-analytics-mcp](https://github.com/nikhilkichili/nba-analytics-mcp) | 4 | Python | MIT | 21 |
| [roizenlabs/sportintel-mcp](https://github.com/roizenlabs/sportintel-mcp) | 1 | TypeScript | MIT | — |

**marcoeg/mcp-odds-api** wraps The Odds API with 3 clean tools (get_events, get_odds, get_event_odds) supporting both SSE and STDIO transports. **nikhilkichili/nba-analytics-mcp** (4 stars, 21 tools) combines NBA data with betting odds tracking, line movement detection, and AI/ML game simulations. **roizenlabs/sportintel-mcp** brings AI-powered sports intelligence with HuggingFace injury risk detection, DFS projections, and SHAP explainability.

## Official First-Party Servers

Two official sports organization MCP servers have launched — a significant shift from the entirely community-driven landscape of March 2026.

### PGA of America Official MCP

The **PGA of America** operates an official MCP server at [mcp.pga.com](https://mcp.pga.com/mcp) using Streamable HTTP transport. Tools include coach search (find PGA-certified instructors by location, drawing on the org's network of [over 31,000 certified PGA golf professionals](https://mcp.pga.com/)), availability lookup, and lesson booking. This is one of the first official servers from any major sports organization — notable for legitimizing MCP as a sports platform integration standard.

### MySwimPro Official MCP

**MySwimPro** operates an official MCP server at [mcp.myswimpro.com](https://mcp.myswimpro.com/) (currently in beta). Provides OAuth-authenticated access to workouts, activities, and training plans. This fills the swimming gap that existed in March — and does so with a first-party official server rather than a community scraper.

### Sportradar Official MCP

[**Sportradar** operates an official MCP server](https://developer.sportradar.com/sportradar-updates/changelog/new-mcp-server-for-ai-assisted-development) at developer.sportradar.com covering 20+ sport profiles (football, soccer, basketball, tennis, and more) for API documentation access. (The changelog entry does not carry a visible publish date, so this page no longer states a specific launch month.)

## Fitness Coaching & Tracking

### AI Endurance MCP Server

[AI Endurance](https://aiendurance.com/docs/mcp) offers a commercial MCP server for structured training in running, cycling, swimming, and triathlon, including ML-based race predictions, a nutrition/macro recommendation model, and OAuth 2.0 authentication. This is one of the few **paid fitness MCP integrations** — most community servers are free.

### Health & Fitness Coach MCP

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [Dinesh-Satram/fitness_coach_MCP](https://github.com/Dinesh-Satram/fitness_coach_MCP) | 15 | TypeScript | MIT | 7 |

A full-stack fitness coaching app with a Next.js dashboard and MCP backend. Tools include workout logging, nutrition tracking, plan generation, weekly targets, and progress feedback. More of an app with MCP integration than a pure MCP server.

## What's Missing

The gap list has shrunk significantly since March, but some remain:

- **Peloton coverage is still early** — several small/unstarred repos exist (e.g. [rlasker3/peloton-mcp](https://github.com/rlasker3/peloton-mcp)) but nothing with meaningful traction yet, surprising given Peloton's API-savvy userbase and the bike's rich data model (output, cadence, resistance, heart rate zones)
- **No rugby server** — the only major global sport with zero MCP representation
- **No CrossFit or yoga servers** — functional fitness and mind-body practices have no dedicated coverage
- **Tennis is thin** — AdemolaAri/tennis-mcp-server (1 star) exists but lacks depth; no ATP/WTA live data server
- **PGA Tour leaderboards still absent** — PGA of America has an official server for coach search/lesson booking, and a new official [opengolfapi/mcp-server](https://github.com/opengolfapi/mcp-server) (49 tools) now covers course data (16,845 US courses), casual/league scoring, and competition management — but professional PGA Tour leaderboards and tournament stats remain absent from any MCP server we found
- **No official league servers** — NFL, NBA, MLB, and NHL have APIs but no official MCP servers (Sportradar is official but provides API docs, not live data)
- **No Strava/Garmin/Fitbit official servers** — all fitness wearable integration remains community-built

**Gaps filled since March 2026:**
- ✅ **Oura Ring** — led by mitchhankins01/oura-ring-mcp (17 tools)
- ✅ **Nutrition tracking** — Cronometer MCP; MacroFactor MCP exists but is currently non-functional (see note above)
- ✅ **Swimming** — MySwimPro official server (first-party)
- ✅ **Cricket** — mavaali/cricket-mcp (14 tools, 10.9M deliveries)
- ✅ **COROS wearable** — cygnusb/coros-mcp (111 stars, 15 tools)
- ✅ **Endurance training** — TrainingPeaks (58 tools), Intervals.icu (48 tools)

## The Bottom Line

**Rating: 4.5 / 5** *(up from 4.0 in March)*

Sports & fitness has become one of the strongest MCP categories in the entire ecosystem. Garmin Connect has grown past [1,000 stars](https://github.com/Taxuspt/garmin_mcp), with a [168-star](https://github.com/Nicolasvegam/garmin-connect-mcp) TypeScript alternative and a [140-star](https://github.com/nrvim/garmin-givemydata) data-sovereignty approach (garmin-givemydata) that stores everything locally in SQLite. Strava reached [471 stars](https://github.com/r-huijts/strava-mcp). Endurance platforms (TrainingPeaks with 58 tools, Intervals.icu with 48, COROS with 15) have dramatically expanded athlete coverage. Nutrition tracking is covered via Cronometer MCP; the MacroFactor MCP server is currently broken (backend auth changes as of May 2026). Cricket has a 14-tool analytics platform (mavaali/cricket-mcp) built on 10.9M ball-by-ball deliveries. A free multi-sport server (sportscore-mcp) covers football, basketball, cricket, and tennis without requiring an API key.

**Two official first-party servers** remain active — PGA of America and MySwimPro — alongside Sportradar's official API docs server. The ecosystem is no longer purely unofficial.

**Best for fitness tracking:** Taxuspt/garmin_mcp (1,000+ stars, 110+ tools) or r-huijts/strava-mcp (471 stars, 25 tools)
**Best for data sovereignty:** nrvim/garmin-givemydata (140 stars, 45 tools — local SQLite, Cloudflare bypass, CTL/ATL/TSB)
**Best for endurance training:** JamsusMaximus/trainingpeaks-mcp (139 stars, 58 tools) or eddmann/intervals-icu-mcp (48 tools)
**Best for sleep/recovery:** mitchhankins01/oura-ring-mcp (17 tools with anomaly detection)
**Best for sports data:** guillochon/mlb-api-mcp (57 stars, 21+ tools with sabermetrics) or balldontlie-api/mcp (27 sports/leagues, 505 tools)
**Best niche pick:** mavaali/cricket-mcp (14 tools, 10.9M ball-by-ball deliveries)
**Best for fantasy:** KBThree13/mcp_espn_ff (ESPN Fantasy Football, 37 stars)

*This review was refreshed on 2026-04-30 using Claude Opus 4.6 (Anthropic); citations re-audited 2026-08-18. First published 2026-03-15.*
