# Sports & Fitness MCP Servers — Strava, Garmin, Fitbit, F1, NFL, MLB, Soccer, and More

> Sports and fitness MCP servers are connecting AI assistants to workout data, live scores, and athletic performance analytics. We reviewed 50+ servers across 9 subcategories.


Sports and fitness MCP servers are connecting AI assistants to workout data, live scores, and athletic performance analytics. Instead of manually checking Garmin Connect for your training load or scrolling ESPN for box scores, these servers let AI agents query your fitness history, analyze race telemetry, pull real-time scores, and even manage fantasy lineups — all through the Model Context Protocol.

The landscape spans nine areas: **fitness wearables** (Garmin, Strava, Fitbit, Apple Health, WHOOP, Oura Ring, COROS), **endurance training platforms** (TrainingPeaks, Intervals.icu, AI Endurance), **motorsport** (Formula 1), **multi-sport data platforms** (Balldontlie covering 18 leagues), **baseball** (MLB stats and sabermetrics), **football** (NFL and fantasy), **soccer and cycling** (live scores, World Cup 2026, professional racing data), **sports betting/fantasy** (odds, props, lineup optimization), and **nutrition tracking** (Cronometer, MacroFactor, MyFitnessPal).

The headline findings: **Garmin Connect surged to 407 stars** (+51%), remaining the most comprehensive fitness MCP server with 96+ tools covering 89% of the python-garminconnect library. A major TypeScript alternative emerged — Nicolasvegam/garmin-connect-mcp (114 stars, 61 tools). **Strava grew to 357 stars** (+30%) with active April 2026 development. **The Oura Ring gap is filled** — 22 implementations now exist, led by mitchhankins01/oura-ring-mcp (17 tools with anomaly detection). **New endurance platforms joined** — TrainingPeaks MCP (51 stars, 58 tools), COROS MCP (42 stars, 15 tools), and Intervals.icu MCP (48 tools). **Two official first-party servers launched** — PGA of America (mcp.pga.com) and MySwimPro (mcp.myswimpro.com), breaking the pattern of entirely community-driven coverage. **Cricket analytics deepened** with mavaali/cricket-mcp (28 tools, 10.9M deliveries via DuckDB). **The FIFA World Cup 2026 MCP** (18 tools) launched with Hacker News coverage.

## Fitness Wearables

### Garmin Connect MCP Server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [Taxuspt/garmin_mcp](https://github.com/Taxuspt/garmin_mcp) | 407 | Python | — | 96+ |

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

With 407 stars (+51% since March), this is one of the fastest-growing fitness MCP servers. The sheer tool count (96+) rivals enterprise API integrations — and all of it is community-built, since Garmin has no official MCP server. Recent community PRs added nutrition endpoints, delete_workout functionality, and activity splits with elevation data.

#### Garmin Connect MCP — TypeScript Alternative

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [Nicolasvegam/garmin-connect-mcp](https://github.com/Nicolasvegam/garmin-connect-mcp) | 114 | TypeScript | — | 61 |

A **major new entrant** — a TypeScript-based Garmin server with 114 stars and 61 tools across 7 categories: activities (12), daily health (14), trends (4), sleep (2), body composition (5), performance/training (11), and profile/devices (13). Supports MFA authentication and works with Claude Code, Claude Desktop, Cursor, and Windsurf. If you prefer TypeScript tooling or need a lighter-weight alternative to the 96-tool Python server, this is a strong option.

#### Other Garmin MCP Servers

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [st3v/garmin-workouts-mcp](https://github.com/st3v/garmin-workouts-mcp) | 20 | Python | MIT | 11 |
| [charlesfrisbee/garmin-workouts-mcp](https://github.com/charlesfrisbee/garmin-workouts-mcp) | 1 | TypeScript | — | 5 |
| [jlwainwright/garmin-mcp-server](https://github.com/jlwainwright/garmin-mcp-server) | 0 | Python | MIT | 20+ |

**st3v/garmin-workouts-mcp** focuses specifically on workout creation — you describe a workout in natural language ("40 minute tempo run with 10 minute warmup") and it generates and uploads the structured workout to Garmin Connect. It also includes activity viewing and calendar management.

**jlwainwright/garmin-mcp-server** offers 20+ tools with a focus on headless 2FA authentication and ntfy notification integration for automated deployments — useful if you want unattended Garmin data access.

### Strava MCP Server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [r-huijts/strava-mcp](https://github.com/r-huijts/strava-mcp) | 357 | TypeScript | MIT | 25 |

The **highest-starred sports MCP server** in the ecosystem. Now at v1.2.1 with active April 2026 development, 25 tools across six categories:

- **Account & Profile** — athlete profile, authorization management
- **Activity Data** — list activities, get details, search by date/type
- **Statistics** — progress tracking, personal records, training summaries
- **Segments** — explore and star segments, view leaderboards
- **Routes** — create and export routes in GPX format
- **Clubs** — view club memberships and activity feeds

The server handles OAuth 2.0 token management and supports natural language queries like "show me my longest rides this month" or "compare my running pace over the last 6 weeks." Recent additions include sport-type icons, local timestamp parsing, segment leaderboards, athlete shoes tracking, and activity streams with ~70-80% data size reduction.

### Fitbit MCP Server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [TheDigitalNinja/mcp-fitbit](https://github.com/TheDigitalNinja/mcp-fitbit) | 27 | TypeScript | MIT | 12 |

A solid integration with 85 commits and a published npm package (v1.0.2). Covers the core Fitbit data types:

- Exercise and activity logs
- Sleep analysis (stages, duration, quality)
- Heart rate monitoring (resting, zones, intraday)
- Weight tracking and body composition
- Nutrition logging and calorie tracking
- Activity summaries (steps, distance, calories burned)

Works with Claude Desktop and other MCP-compatible clients. Development appears to have slowed — last commit was May 2025 (v1.0.2).

### Apple Health MCP Server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [the-momentum/apple-health-mcp-server](https://github.com/the-momentum/apple-health-mcp-server) | 167 | Python | MIT | — |

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
| [mitchhankins01/oura-ring-mcp](https://github.com/mitchhankins01/oura-ring-mcp) | 12 | TypeScript | — | 17 |
| [daveremy/oura-mcp](https://github.com/daveremy/oura-mcp) | 4 | TypeScript | — | 10 |

**The biggest gap fill since March** — Oura Ring went from zero MCP servers to 22 implementations. The most feature-rich is **mitchhankins01/oura-ring-mcp** with 17 tools: 10 data retrieval tools (sleep, readiness, activity, workouts, sessions, heart rate, stress, SpO2, tags) plus 7 smart analysis tools (anomaly detection, sleep quality scoring, metric correlation, period comparison, best sleep conditions, HRV trend analysis). Published on npm as `oura-ring-mcp`. Includes MCP Resources (today, weekly-summary, baseline, monthly-insights) and analysis Prompts.

**rajvirtual/oura-mcp-server** (14 stars) focuses on sleep analysis, readiness scores, HRV tracking, and stress comparisons. **daveremy/oura-mcp** (4 stars) doubles as a standalone CLI tool and Claude Code skill with 10 tools covering daily summaries, sleep, readiness, activity, workouts, heart rate, stress, SpO2, sessions, and trends.

⚠️ **Security note**: A trojanized Oura MCP server was discovered in February 2026, distributing the SmartLoader/StealC infostealer via fake forks. Only install Oura MCP servers from verified, well-starred repositories.

### COROS MCP Server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [cygnusb/coros-mcp](https://github.com/cygnusb/coros-mcp) | 42 | Python | — | 15 |
| [rowlando/coros-workout-mcp](https://github.com/rowlando/coros-workout-mcp) | 20 | TypeScript | — | — |

**COROS joins the wearable ecosystem** — cygnusb/coros-mcp (42 stars, 15 tools) covers sleep, HRV, daily metrics, activities, and structured workouts. Authenticates directly with COROS Training Hub (no API key needed). Supports workout creation with power targets and interval groups. Actively developed.

**rowlando/coros-workout-mcp** (20 stars) focuses specifically on creating COROS strength workouts via the Training Hub API.

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

## Endurance Training Platforms

### TrainingPeaks MCP Server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [JamsusMaximus/trainingpeaks-mcp](https://github.com/JamsusMaximus/trainingpeaks-mcp) | 51 | Python | — | 58 |

A **major new addition for endurance athletes** — 58 tools covering structured interval workouts, calendar management, fitness metrics (CTL/ATL/TSB), and equipment tracking. Uses cookie-based authentication (no API approval needed) with AES-256-GCM encrypted credential storage. If you're a triathlete, cyclist, or runner who trains with TrainingPeaks, this is a direct pipeline between your AI assistant and your training plan.

### Intervals.icu MCP Server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [eddmann/intervals-icu-mcp](https://github.com/eddmann/intervals-icu-mcp) | 20 | Python | — | 48 |

Comprehensive integration with the popular Intervals.icu training platform — 48 tools spanning activities, analysis, wellness, events/calendar, performance curves, workout library, gear management, and sport settings. Also includes 6 MCP Prompts and 1 Resource. Intervals.icu is the free alternative to TrainingPeaks favored by data-oriented endurance athletes.

### Nutrition: Cronometer & MacroFactor

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [cphoskins/cronometer-mcp](https://github.com/cphoskins/cronometer-mcp) | — | Python | — | — |
| [sjawhar/macrofactor](https://github.com/sjawhar/macrofactor) | 16 | TypeScript | — | 28 |

**The nutrition gap is filling** — Cronometer MCP (also on PyPI as `cronometer-mcp` v2.0.3) provides food logs, macro/micro summaries, diary entries, fasting data, and biometrics. Requires Cronometer Gold (paid tier).

**sjawhar/macrofactor** (16 stars, 28 tools) covers nutrition tracking, workout history, food database search, and weight logging. Includes a CLI, MCP server, and SvelteKit web app. 12 read tools + 16 write tools make this one of the most complete nutrition MCP integrations.

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
| [balldontlie-api/mcp](https://github.com/balldontlie-api/mcp) | 10 | TypeScript | — | 250+ |

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
| [guillochon/mlb-api-mcp](https://github.com/guillochon/mlb-api-mcp) | 46 | Python | MIT | 21+ |

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
| [etweisberg/mlb-mcp](https://github.com/etweisberg/mlb-mcp) | 23 | Python | — | 4 |

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
| [KBThree13/mcp_espn_ff](https://github.com/KBThree13/mcp_espn_ff) | 30 | Python | MIT | 6 |

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
| [yeonupark/mcp-soccer-data](https://github.com/yeonupark/mcp-soccer-data) | 30 | Python | MIT | 1 |

Provides real-time football (soccer) data through a single `get_livescores()` tool, but that tool delivers 6 data categories: match listings, detailed match info, live events, team lineups, betting odds, and league metadata. Good for checking scores during matches, but limited scope compared to what Balldontlie offers for EPL.

### FIFA World Cup 2026 MCP

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [jordanlyall/wc26-mcp](https://github.com/jordanlyall/wc26-mcp) | — | — | MIT | 18 |

A **timely new server** launched ahead of the 2026 World Cup — 18 tools covering matches, teams, venues, city guides, fan zones, visa info, head-to-head records, odds, standings, and brackets. No API key needed (all data built-in). Featured on Hacker News. Has its own website at wc26.ai.

### Cricket MCP Servers

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [tarun7r/cricket-mcp-server](https://github.com/tarun7r/cricket-mcp-server) | 12 | — | — | 9 |
| [mavaali/cricket-mcp](https://github.com/mavaali/cricket-mcp) | 2 | — | — | 28 |

**Cricket went from a gap to well-served** — tarun7r/cricket-mcp-server (12 stars, 9 tools) covers Cricbuzz data with ICC rankings and live commentary. The bigger story is **mavaali/cricket-mcp** — 28 tools backed by a DuckDB database of 21,000 matches and 10.9 million ball-by-ball deliveries from Cricsheet. This is serious cricket analytics — the kind of depth that baseball's mlb-api-mcp provides for its sport.

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
| [WFord26/BetTrack](https://github.com/WFord26/BetTrack) | 3 | TypeScript | MIT | 30+ |

A sports betting companion with 30+ tools supporting **70+ betting markets** across NFL, NBA, NHL, MLB, EPL, and UEFA. Includes player props, live scores, visual artifacts, and an optional React dashboard for bet tracking. Released v2026.02.03.1 with TypeScript build fixes and dashboard refinements.

### Other Betting & Odds Servers

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [marcoeg/mcp-odds-api](https://github.com/marcoeg/mcp-odds-api) | 3 | — | — | 3 |
| [nikhilkichili/nba-analytics-mcp](https://github.com/nikhilkichili/nba-analytics-mcp) | 4 | — | — | 21 |
| [roizenlabs/sportintel-mcp](https://github.com/roizenlabs/sportintel-mcp) | — | — | — | — |

**marcoeg/mcp-odds-api** wraps The Odds API with 3 clean tools (get_events, get_odds, get_event_odds) supporting both SSE and STDIO transports. **nikhilkichili/nba-analytics-mcp** (4 stars, 21 tools) combines NBA data with betting odds tracking, line movement detection, and AI/ML game simulations. **roizenlabs/sportintel-mcp** brings AI-powered sports intelligence with HuggingFace injury risk detection, DFS projections, and SHAP explainability across 10+ sportsbooks.

## Official First-Party Servers

Two official sports organization MCP servers have launched — a significant shift from the entirely community-driven landscape of March 2026.

### PGA of America Official MCP

The **PGA of America** launched an official MCP server at [mcp.pga.com](https://mcp.pga.com/) using Streamable HTTP transport. Tools include coach search (find PGA-certified instructors by location) and lesson booking. This is one of the first official servers from any major sports organization — notable for legitimizing MCP as a sports platform integration standard.

### MySwimPro Official MCP

**MySwimPro** — the #1 swim training app (used in 180+ countries) — launched an official MCP server at [mcp.myswimpro.com](https://mcp.myswimpro.com/). Provides OAuth-authenticated access to workouts, activities, and training plans. This fills the swimming gap that existed in March — and does so with a first-party official server rather than a community scraper.

### Sportradar Official MCP

**Sportradar** launched an official MCP server in February 2026 at developer.sportradar.com covering 20+ sport profiles (football, soccer, basketball, tennis, and more) for API documentation access. Sportradar is the data backbone for many major sports media companies.

## Fitness Coaching & Tracking

### AI Endurance MCP Server

[AI Endurance](https://aiendurance.com/docs/mcp) offers a commercial MCP server for structured training in running, cycling, swimming, and triathlon. Now with 20 tools including ML-based race predictions, a nutrition model, and OAuth 2.0 authentication. This is one of the few **paid fitness MCP integrations** — most community servers are free.

### Health & Fitness Coach MCP

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [Dinesh-Satram/fitness_coach_MCP](https://github.com/Dinesh-Satram/fitness_coach_MCP) | 7 | TypeScript | — | 7 |

A full-stack fitness coaching app with a Next.js dashboard and MCP backend. Tools include workout logging, nutrition tracking, plan generation, weekly targets, and progress feedback. More of an app with MCP integration than a pure MCP server.

## What's Missing

The gap list has shrunk significantly since March, but some remain:

- **No Peloton MCP server** — only two zero-star repos exist. Surprising given Peloton's API-savvy userbase and the bike's rich data model (output, cadence, resistance, heart rate zones)
- **No rugby server** — the only major global sport with zero MCP representation
- **No CrossFit or yoga servers** — functional fitness and mind-body practices have no dedicated coverage
- **Tennis is thin** — AdemolaAri/tennis-mcp-server (1 star, 7 tools) exists but lacks depth; no ATP/WTA live data server
- **Golf tournament data missing** — PGA of America has an official server for coach search/lesson booking, and opengolfapi covers 15,667 US courses, but PGA Tour leaderboards and tournament stats are absent
- **No official league servers** — NFL, NBA, MLB, and NHL have APIs but no official MCP servers (Sportradar is official but provides API docs, not live data)
- **No Strava/Garmin/Fitbit official servers** — all fitness wearable integration remains community-built

**Gaps filled since March 2026:**
- ✅ **Oura Ring** — 22 implementations, led by mitchhankins01/oura-ring-mcp (17 tools)
- ✅ **Nutrition tracking** — Cronometer MCP and MacroFactor MCP (28 tools)
- ✅ **Swimming** — MySwimPro official server (first-party)
- ✅ **Cricket** — mavaali/cricket-mcp (28 tools, 10.9M deliveries)
- ✅ **COROS wearable** — cygnusb/coros-mcp (42 stars, 15 tools)
- ✅ **Endurance training** — TrainingPeaks (58 tools), Intervals.icu (48 tools)

## The Bottom Line

**Rating: 4.5 / 5** *(up from 4.0 in March)*

Sports & fitness has become one of the strongest MCP categories in the entire ecosystem. Garmin Connect surged to 407 stars with a new 114-star TypeScript alternative. Strava grew to 357 stars with active development. The Oura Ring gap that was a glaring omission in March is now filled by 22 implementations. New endurance platforms (TrainingPeaks with 58 tools, Intervals.icu with 48, COROS with 15) have dramatically expanded athlete coverage beyond Garmin and Strava. Nutrition tracking arrived via Cronometer and MacroFactor. Cricket went from zero to a 28-tool analytics platform rivaling baseball's depth.

The biggest structural shift: **two official first-party servers launched** — PGA of America and MySwimPro — breaking the pattern of entirely community-driven coverage. Sportradar also launched an official MCP. The ecosystem is no longer purely unofficial.

**Best for fitness tracking:** Taxuspt/garmin_mcp (407 stars, 96+ tools) or r-huijts/strava-mcp (357 stars, 25 tools)
**Best for endurance training:** JamsusMaximus/trainingpeaks-mcp (51 stars, 58 tools) or eddmann/intervals-icu-mcp (48 tools)
**Best for sleep/recovery:** mitchhankins01/oura-ring-mcp (17 tools with anomaly detection)
**Best for sports data:** guillochon/mlb-api-mcp (46 stars, 21+ tools with sabermetrics) or balldontlie-api/mcp (18 leagues, 250+ endpoints)
**Best niche pick:** mavaali/cricket-mcp (28 tools, 10.9M ball-by-ball deliveries)
**Best for fantasy:** KBThree13/mcp_espn_ff (ESPN Fantasy Football, 30 stars)

*This review was refreshed on 2026-04-27 using Claude Opus 4.6 (Anthropic). First published 2026-03-15.*

