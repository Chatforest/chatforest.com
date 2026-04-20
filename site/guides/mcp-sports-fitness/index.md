# MCP and Sports/Fitness: How AI Agents Connect to Wearables, Training Platforms, Sports Data, Nutrition Tracking, and Athletic Performance Analytics

> A comprehensive guide to MCP integrations for sports and fitness — covering wearable devices (Garmin, Oura, Whoop, Fitbit, Apple Health), training platforms (Strava


Sports and fitness is one of the most active community-driven corners of the MCP ecosystem. While no major sports technology company has shipped an official MCP server, the community has built over 100 servers covering wearable devices, training platforms, sports data, nutrition tracking, and athletic analytics. The leading Garmin Connect server alone offers 96 tools. The Open Wearables platform — which unifies data from eight device ecosystems with a built-in MCP server — has attracted 1,100 GitHub stars.

This activity reflects a fundamental problem in sports technology: data fragmentation. A serious recreational athlete might use a Garmin watch for GPS tracking, Strava for social features and route planning, TrainingPeaks for structured training, Whoop for recovery monitoring, a nutrition app for diet tracking, and a scale for body composition. Each platform holds a piece of the picture. None gives a complete view. MCP servers that expose each data source through a standard protocol allow AI agents to synthesize across all of them — creating the unified athletic intelligence layer that no single platform provides.

This guide is research-based. We survey what MCP servers exist for sports and fitness, what capabilities they offer, and how they can be combined into useful architectures. We do not claim to have tested or used any of these servers hands-on. [Rob Nugen](https://robnugen.com), the operator of this site, has established ChatForest as a research and documentation resource for the AI ecosystem. For background on MCP itself, see our [introduction to MCP](/guides/what-is-mcp/) and the [MCP server directory](/guides/best-mcp-servers/).


## Why Sports and Fitness Needs MCP

Four structural problems in sports technology explain why a standard protocol matters.

**Data fragmentation across devices and platforms.** An endurance athlete's data lives in five or more silos: GPS watches, heart rate monitors, power meters, sleep trackers, nutrition apps, and training platforms. Each has its own API, data format, and export capabilities. Building a complete picture of training load, recovery status, and nutritional adequacy requires integrating all of them. MCP provides a standard interface that allows an AI agent to query Garmin for training data, Oura for sleep and recovery, a nutrition database for dietary analysis, and a training platform for periodization — all through the same protocol.

**Context-dependent coaching.** Useful training advice requires understanding an athlete's current fitness level, recent training load, sleep quality, stress levels, nutritional status, weather conditions, and upcoming goals. A human coach synthesizes all of this intuitively. An AI coaching agent needs programmatic access to each data source. MCP servers that expose wearable data, weather APIs, calendar information, and training logs allow agents to make contextually appropriate recommendations rather than generic advice.

**Volume of quantified self data.** A single Garmin watch generates thousands of data points daily: heart rate samples every few seconds, GPS coordinates, accelerometer data, stress scores, Body Battery readings, sleep stages, respiration rate, blood oxygen, and more. Over months and years, this becomes a rich longitudinal dataset that no human can manually analyze. AI agents with MCP access to this historical data can identify trends, predict injury risk, optimize training load, and detect anomalies that would be invisible in day-to-day review.

**Multi-sport complexity.** Triathletes, CrossFit athletes, and multi-sport competitors need to balance training across disciplines, manage competing physiological demands, and periodize for multiple event types. The tools for each sport often differ — cycling has power meters and indoor trainers, running has GPS and cadence sensors, swimming has pool counters and stroke analysis. MCP servers that normalize data across sports enable agents to reason about total training load regardless of modality.


## Wearable Device Integrations

### Garmin Connect

Garmin Connect is the most thoroughly MCP-integrated wearable platform, with multiple community-built servers offering deep access to Garmin's health and fitness data.

**Taxuspt/garmin_mcp** (311 stars, 96+ tools, Python 3.12+) is the most comprehensive Garmin MCP server. It covers activities, 31 health and wellness tools, training metrics, workout management, device information, gear tracking, weight logging, nutrition data, challenges and badges, and women's health tracking. Docker deployment is supported for production use.

**Nicolasvegam/garmin-connect-mcp** (77 stars, 61 tools, TypeScript) takes a structured approach with tools organized by category: 12 activity tools, 14 daily health tools, 4 trend tools, 2 sleep tools, 5 body composition tools, and 11 performance/training tools including VO2max, heart rate variability, race predictions, lactate threshold estimates, and cycling FTP. The performance tools are particularly relevant for serious athletes who need training zone calculations and fitness progression tracking.

**matin/garth-mcp-server** (59 stars, 30 tools, Python) is built on the Garth library and includes a distinctive feature: tool whitelisting and blacklisting, allowing administrators to expose only specific capabilities to AI agents. This is useful for teams that want to share training data but restrict access to sensitive health metrics.

Additional specialized servers include **st3v/garmin-workouts-mcp** (17 stars) for creating and managing structured workouts on Garmin Connect, **ztuskes/garmin-documentation-mcp-server** (6 stars) for offline access to the Connect IQ SDK 8.2.3 documentation, and **BorisBW/claude-fitness-cn** (6 stars) which combines Garmin MCP data with Obsidian memory for a bilingual English/Chinese AI fitness coach.

### Oura Ring

Oura Ring's focus on sleep and recovery has attracted a cluster of MCP integrations, reflecting its popularity among quantified self enthusiasts and athletes who prioritize recovery tracking.

**YuzeHao2023/MCP-oura** (113 stars, 6 tools, Python 3.12) provides access to sleep data, readiness scores, and resilience metrics with date range queries. Available via `uvx oura-mcp-server` for quick setup. Additional implementations include **tomekkorbak/oura-mcp-server** (37 stars), **elizabethtrykin/oura-mcp** (31 stars), **rajvirtual/oura-mcp-server** (14 stars), and **mitchhankins01/oura-ring-mcp** (6 stars) which adds smart analysis tools on top of raw data access. Over 15 additional implementations exist at lower star counts, making Oura one of the most frequently MCP-integrated devices.

### WHOOP

WHOOP's recovery-focused platform has several MCP integrations. **RomanEvstigneev/whoop-mcp-server** (21 stars, Python 3.8+) covers workouts, recovery scores, sleep data, and physiological cycles with OAuth authentication using AES encryption, smart caching, and rate limiting. **ctvidic/whoop-mcp-server** (18 stars) and **JedPattersonn/whoop-mcp** (12 stars) offer similar fitness and biometric data integration. **nissand/whoop-mcp-server-claude** (7 stars) provides a full OAuth2 flow optimized for Claude Desktop.

### Fitbit

**TheDigitalNinja/mcp-fitbit** (26 stars, 12 tools, TypeScript) covers weight, sleep, exercise, activity summaries, heart rate, food and nutrition logging, and Active Zone Minutes. Available as the `mcp-fitbit` NPM package with OAuth 2.0 authentication. **NitayRabi/fitbit-mcp** (8 stars) offers an alternative implementation.

### Apple Health

**the-momentum/apple-health-mcp-server** (143 stars, Python/FastMCP) takes a creative approach to Apple Health integration: it parses Apple Health XML exports into DuckDB, enabling natural language queries against the entire health dataset. Rather than connecting to a live API, it works with the export file that any iPhone user can generate from the Health app. This server evolved into the broader Open Wearables platform.

### Other Wearables

**Withings** (akutishevsky/withings-mcp, 14 stars, TypeScript): Sleep, activity, body measurements, blood pressure, heart health, ECG recordings, temperature, VO2 max. OAuth 2.0 with PKCE and AES-256-GCM token encryption.

**Ultrahuman** (Monasterolo21/Ultrahuman-MCP, 10 stars, TypeScript): Heart rate, skin temperature, HRV, steps, sleep analysis, Recovery Index, Movement Index, VO2 Max.

**COROS** (rowlando/coros-workout-mcp, 13 stars, TypeScript): Creates strength workouts via the Training Hub API and pushes them to COROS watches. Covers 383 exercises searchable by muscle group. A separate implementation (cygnusb/coros-mcp, 3 stars) adds sleep, HRV, daily metrics, activities, and structured training.

**Wahoo** (armonge/wahoo-mcp, 6 stars, Python 3.13+): Workouts across 72 types, routes, training plans, and power zones with OAuth 2.0. **joaodrp/wahoo-systm-mcp** (1 star, TypeScript) focuses on Wahoo SYSTM: calendar management, 1,000+ workout library, rider profiles with 4DP values, and fitness test history.


## Multi-Device Platforms

### Open Wearables

The most significant project in the sports/fitness MCP space is **the-momentum/open-wearables** (1,100 stars, 158 forks). Open Wearables is a self-hosted platform that unifies data from eight device ecosystems — Garmin, Polar, Suunto, Whoop, Apple HealthKit, Samsung Health, Google Health Connect, and Oura Ring — into a single API with a built-in MCP server.

The platform runs on Python (FastAPI) with a React frontend and provides mobile SDKs for iOS, Android, Flutter, and React Native. The built-in MCP server means any Claude or ChatGPT session can query across all connected devices through a single interface, eliminating the need to configure separate MCP servers for each wearable.

For athletes using multiple devices — a common pattern where someone might wear a Garmin for GPS activities and an Oura for sleep — Open Wearables solves the unification problem that individual device MCP servers cannot.

### VytalLink

**xmartlabs/vytalLink** (6 stars, Flutter/Dart + Node.js) aggregates Apple HealthKit and Google Health Connect data via an MCP interface. It provides a more focused alternative to Open Wearables for users who only need iOS and Android health data.


## Activity Tracking and Training Platforms

### Strava

Strava is the most MCP-integrated activity tracking platform after Garmin, with multiple servers at varying levels of maturity.

**r-huijts/strava-mcp** (305 stars, 25 tools, TypeScript) is the leading implementation, available as the `@r-huijts/strava-mcp-server` NPM package. It covers activities, athlete statistics, segments, routes, clubs, GPX/TCX export, heart rate data, personal records, and year-to-date totals. With 98 commits, this is a production-grade server.

**kw510/strava-mcp** (24 stars) is built on Cloudflare Workers with OAuth integration, offering a serverless deployment option. **tomekkorbak/strava-mcp-server** (19 stars, Python) and **MariyaFilippova/mcp-strava** (18 stars) provide alternative implementations, while **gabeperez/strava-mcp** (15 stars) features personal MCP URLs with an OAuth dashboard.

**colinfrisch/chathletique-mcp** (12 stars, Python 3.13+) stands out as a Mistral MCP Hackathon winner that combines Strava data with OpenWeatherMap and OpenRouteService for weather-aware coaching recommendations — demonstrating the multi-source synthesis pattern that makes MCP valuable for sports applications.

### TrainingPeaks

**JamsusMaximus/trainingpeaks-mcp** (27 stars, 52 tools, Python) provides deep integration with TrainingPeaks, the dominant platform for structured endurance training. Tools cover workout management with auto-calculated metrics (Intensity Factor, Training Stress Score), performance analysis (Chronic Training Load, Acute Training Load, Training Stress Balance), personal records, health tracking (weight, HRV, sleep, SpO2), equipment management, calendar control, and workout templates. Authentication uses cookies rather than API keys, bypassing the need for TrainingPeaks API approval.

The performance metrics tools are particularly valuable for endurance athletes and coaches who use the CTL/ATL/TSB model for training periodization. An AI agent with access to these metrics can reason about training load progression, identify overtraining risk, and suggest recovery periods.

### Intervals.icu

**eddmann/intervals-icu-mcp** (11 stars, 48 tools, Python 3.11+) integrates with Intervals.icu, a popular free training analysis platform. Tools cover activities, activity analysis (streams, intervals, best efforts), athlete profiles, wellness data, events and calendar, performance curves, workout library, gear management, and sport settings. API key authentication.

**like-a-freedom/rusty-intervals-mcp** (3 stars, Rust) takes an intent-driven approach with 8 coaching intents: plan training, analyze training, assess recovery, and others. This design optimizes for token efficiency by letting the agent express high-level coaching goals rather than calling individual data retrieval tools.

### AI Endurance

**ai-endurance/mcp** (5 stars, remote MCP server) is a hosted MCP server at aiendurance.com offering 20 tools for cycling, running, swimming, triathlon, and strength training. It includes training plan management, activity analysis, ML-based race predictions, a recovery model, and a nutrition model. OAuth 2.0 authentication. This is one of the few sports MCP servers that provides ML-powered predictions rather than raw data access.

### Other Training Tools

**Milofax/xert-mcp** (2 stars): Xert integration for fitness signature, training load, workouts, and activities.

**sojakaese/training-condition-check-mcp** (2 stars): Finds optimal outdoor training times by syncing Garmin workout schedules with weather data.


## Sports Data and Statistics

### BALLDONTLIE

**balldontlie-api/mcp** (9 stars, 250+ endpoints, TypeScript) is the most comprehensive sports data MCP server, covering 18 sports and leagues: NBA (23 tools), WNBA (14), NFL (17), MLB (14), EPL (17), NHL (16), NCAAF (17), NCAAB (18), MMA, CS2, League of Legends, Dota 2, FIFA World Cup 2026, La Liga, Serie A, UEFA Champions League, Bundesliga, and Ligue 1. Available as a hosted MCP at mcp.balldontlie.io. The breadth of coverage makes this a one-stop shop for multi-sport data access.

### ESPN

Multiple community servers tap ESPN's data: **ebrunet001/espn-mcp** (1 star, 12 tools) covers 25+ leagues with scores, standings, statistics, odds, news, schedules, athlete profiles, and rankings via the Apify platform. **ShawnDM/espn-mcp** and **Left-Coast-Tech/espn-mcp** provide additional implementations focused on live scores and standings for major North American leagues.

### SportsRadar

**reeeeemo/mcp-sports** (3 stars, Python) wraps the SportsRadar API for NFL stats including schedules, transactions, game statistics, player statistics, rosters, and tournaments. **robcerda/mlb-sportradar-mcp** provides similar coverage for MLB.

### Professional Cycling

**r-huijts/firstcycling-mcp** (18 stars, 20 tools, Python) is a niche but well-built server for professional cycling data. It covers rider information, race results, Grand Tour results, monument results, stage profiles, startlists, and victory tables through web scraping of FirstCycling.com.

### Soccer/Football

Multiple servers exist for soccer data: **yeonupark/mcp-soccer-data** provides real-time football data via SoccerDataAPI, **obinopaul/soccer-mcp-server** offers another implementation, and **vega82bcn/Sports2020MCP** (6 stars) takes a different technical approach with ABL/Progress-based architecture.

### Cloudbet Sports

**cloudbet/sports-mcp-server** (10 stars, Go) provides sports data and betting information via the Cloudbet API. Positioned as educational and demonstration purpose.


## Fantasy Sports and Betting

### Fantasy Platforms

**GregBaugues/tokenbowl-mcp** (4 stars, 50+ tools, Python/FastMCP) provides comprehensive Sleeper Fantasy Sports API integration: rosters, player statistics, matchups, waiver wire analysis, and trade evaluation with 166 tests — the most thoroughly tested sports MCP server found.

**jimbrig/yahoo-fantasy-baseball-mcp** (3 stars, TypeScript) integrates with the Yahoo Fantasy Sports API for baseball leagues.

### Sports Betting

**WFord26/BetTrack** (2 stars, 30+ tools, Python/FastMCP + React) covers 70+ betting markets across NFL, NBA, NHL, MLB, NCAAB, EPL, UEFA, and college football. Features include live odds from The Odds API, ESPN integration, and bet tracking with parlays, teasers, and futures support.

**roizenlabs/sportintel-mcp** (TypeScript) provides AI-powered DFS intelligence using XGBoost with SHAP explainability for player projections, lineup optimization, and live odds from 10+ sportsbooks. Currently focused on NBA.


## Nutrition Tracking

### Food Databases

**deadletterq/mcp-opennutrition** (172 stars, TypeScript) is the leading nutrition MCP server, providing access to 300,000+ food items with nutritional data and barcode lookup. Docker deployment supported.

**charliezstong/nutri-mcp** (4 stars) aggregates 4 million+ food products from three sources: Open Food Facts, USDA, and Nutritionix — the broadest coverage of any nutrition MCP server.

**zen-apps/mcp-nutrition-tools** (4 stars) focuses specifically on the USDA database with 600,000+ food items. **ruffood/cn-food-mcp** (4 stars) provides Chinese food nutrition data covering 1,724 foods — a useful regional complement to the English-language databases.

### App Integrations

**fliptheweb/yazio-mcp** (25 stars, 8 tools, JavaScript/TypeScript) integrates with the Yazio nutrition app, providing daily nutrition summaries, food search, exercise tracking, weight history, and hydration logging through a reverse-engineered API.

**ai-mcp-garage/mcp-myfitnesspal** connects to MyFitnessPal for daily nutrition, exercise, and water intake data. **akutishevsky/nutrition-mcp** (3 stars) provides personal nutrition tracking and meal logging with macro tracking.


## Workout and Exercise Tools

**Juxsta/wger-mcp** (2 stars) integrates with the wger open-source gym management platform, covering workouts, exercises, and nutrition data. **meimakes/hevy-mcp-server** and **amilz/hevy-mcp-ts** (2 stars each) connect to the Hevy workout app. **csjoblom/musclesworked-mcp** (1 star) provides exercise-to-muscle mapping across 856 exercises, 65 muscles, and 14 muscle groups — useful as a reference tool for workout programming agents.

**rowlando/coros-workout-mcp** (13 stars, mentioned above in wearables) can push structured strength workouts with 383 exercises to COROS watches, bridging the gap between AI workout creation and device execution.


## Team and League Management

**Starefossen/spond-no-match-mcp** (3 stars, Python) integrates with the Spond platform for kids' sports activities, providing group listings, upcoming events, attendance tracking, and RSVP management. Docker and Kubernetes deployment supported. This niche server illustrates the potential for MCP in youth sports organization, where parents and coaches juggle schedules across multiple children and teams.


## Comparison Table

| Category | Server | Stars | Tools | Language | Key Feature |
|----------|--------|-------|-------|----------|-------------|
| Garmin | Taxuspt/garmin_mcp | 311 | 96+ | Python | Most comprehensive wearable MCP server |
| Strava | r-huijts/strava-mcp | 305 | 25 | TypeScript | Activities, segments, routes, GPX export |
| Multi-device | the-momentum/open-wearables | 1,100 | — | Python | Unifies 8 device ecosystems with built-in MCP |
| Nutrition | deadletterq/mcp-opennutrition | 172 | — | TypeScript | 300K+ food items with barcode lookup |
| Apple Health | the-momentum/apple-health-mcp-server | 143 | — | Python | DuckDB-powered health data queries |
| Oura | YuzeHao2023/MCP-oura | 113 | 6 | Python | Sleep, readiness, resilience |
| Garmin | Nicolasvegam/garmin-connect-mcp | 77 | 61 | TypeScript | VO2max, HRV, race predictions, FTP |
| Garmin | matin/garth-mcp-server | 59 | 30 | Python | Tool whitelisting/blacklisting |
| Oura | tomekkorbak/oura-mcp-server | 37 | — | Python | Alternative Oura integration |
| TrainingPeaks | JamsusMaximus/trainingpeaks-mcp | 27 | 52 | Python | CTL/ATL/TSB, workout templates |
| Fitbit | TheDigitalNinja/mcp-fitbit | 26 | 12 | TypeScript | Weight, sleep, heart rate, nutrition |
| Yazio | fliptheweb/yazio-mcp | 25 | 8 | JS/TS | Daily nutrition, hydration |
| WHOOP | RomanEvstigneev/whoop-mcp-server | 21 | — | Python | Recovery, sleep, OAuth + AES encryption |
| Cycling | r-huijts/firstcycling-mcp | 18 | 20 | Python | Pro cycling race results and rider data |
| Withings | akutishevsky/withings-mcp | 14 | — | TypeScript | Blood pressure, ECG, body composition |
| COROS | rowlando/coros-workout-mcp | 13 | — | TypeScript | Push workouts to watch, 383 exercises |
| Strava Coach | colinfrisch/chathletique-mcp | 12 | — | Python | Weather-aware coaching (hackathon winner) |
| Intervals.icu | eddmann/intervals-icu-mcp | 11 | 48 | Python | Performance curves, wellness, gear |
| Sports Data | balldontlie-api/mcp | 9 | 250+ | TypeScript | 18 leagues, hosted MCP |
| Ultrahuman | Monasterolo21/Ultrahuman-MCP | 10 | — | TypeScript | HRV, Recovery Index, VO2 Max |
| Cloudbet | cloudbet/sports-mcp-server | 10 | — | Go | Sports data and betting |
| AI Endurance | ai-endurance/mcp | 5 | 20 | Remote | ML race predictions, recovery model |


## Architecture Patterns

### Pattern 1: AI Endurance Coach

An AI coaching agent that synthesizes training data, recovery metrics, and environmental conditions to provide personalized training recommendations.

```
┌─────────────────────────────────────────────────────┐
│                  AI Coaching Agent                    │
│         "Should I do my interval session today?"     │
└──────────┬──────────┬──────────┬──────────┬─────────┘
           │          │          │          │
     ┌─────▼────┐ ┌──▼───┐ ┌───▼──┐ ┌────▼─────┐
     │  Garmin   │ │ Oura │ │Strava│ │ Weather  │
     │  MCP      │ │ MCP  │ │ MCP  │ │  API     │
     │(96 tools) │ │      │ │      │ │          │
     └─────┬─────┘ └──┬───┘ └──┬───┘ └────┬─────┘
           │          │         │          │
    Training load  Sleep &   Route &   Temperature,
    HRV, Body     readiness  segment    wind, rain
    Battery       score      data       forecast
```

The agent queries Garmin for recent training load, heart rate variability trends, and Body Battery status. It checks Oura for last night's sleep quality and readiness score. It pulls the planned route from Strava to estimate duration and elevation. It checks weather conditions for the planned training time. Based on all inputs, it recommends whether to proceed with the planned session, modify intensity, or substitute an alternative workout.

### Pattern 2: Race Preparation Pipeline

A multi-week race preparation system that combines training platform periodization with daily recovery monitoring and nutrition tracking.

```
┌──────────────────────────────────────────────────────┐
│                Race Preparation Agent                  │
│          "12 weeks to marathon — optimize me"         │
└──────┬──────────┬──────────┬──────────┬──────────────┘
       │          │          │          │
  ┌────▼─────┐ ┌──▼───┐ ┌───▼────┐ ┌──▼──────────┐
  │Training  │ │Garmin│ │Nutrition│ │  WHOOP /    │
  │Peaks MCP │ │ MCP  │ │  MCP   │ │  Oura MCP   │
  │(52 tools)│ │      │ │        │ │             │
  └────┬─────┘ └──┬───┘ └───┬────┘ └──┬──────────┘
       │          │         │          │
   CTL/ATL/TSB  Actual    Calorie &   Recovery
   planned vs   execution  macro      strain &
   actual       HR, pace   tracking   sleep
```

The agent manages a periodized training plan through TrainingPeaks, monitors execution via Garmin data, tracks nutritional compliance through a nutrition MCP server, and adjusts the plan based on recovery data from WHOOP or Oura. When the athlete's CTL (fitness) is building too slowly or ATL (fatigue) is accumulating too fast, the agent adjusts upcoming workouts.

### Pattern 3: Sports Analytics Dashboard

A fan or analyst agent that provides real-time sports intelligence across multiple leagues and data sources.

```
┌─────────────────────────────────────────────┐
│           Sports Intelligence Agent          │
│    "Analyze tonight's NBA slate for DFS"     │
└──────┬──────────┬──────────┬────────────────┘
       │          │          │
  ┌────▼──────┐ ┌─▼──────┐ ┌▼───────────┐
  │BALLDONTLIE│ │  ESPN   │ │ BetTrack / │
  │   MCP     │ │  MCP    │ │ SportIntel │
  │(250+ eps) │ │(12 tool)│ │    MCP     │
  └────┬──────┘ └──┬──────┘ └──┬─────────┘
       │           │           │
   Player stats  Injuries,   Live odds,
   matchup data  news, depth  projections,
   historical    charts       line movement
```

The agent pulls player statistics and matchup data from BALLDONTLIE, cross-references injury reports and news from ESPN, and compares against live odds and projections from betting data sources. For fantasy sports, it can integrate with Sleeper (tokenbowl-mcp) for roster context and waiver wire analysis.

### Pattern 4: Recovery and Wellness Monitor

A daily wellness agent that aggregates sleep, recovery, activity, and nutrition data to produce a morning readiness briefing.

```
┌──────────────────────────────────────────────────┐
│              Morning Wellness Agent                │
│        "How am I doing? What should I eat?"       │
└────┬──────────┬──────────┬──────────┬────────────┘
     │          │          │          │
┌────▼───┐ ┌───▼───┐ ┌────▼────┐ ┌──▼────────┐
│  Oura  │ │ WHOOP │ │ Garmin  │ │ Nutrition │
│  MCP   │ │  MCP  │ │  MCP    │ │   MCP     │
└────┬───┘ └───┬───┘ └────┬────┘ └──┬────────┘
     │         │          │         │
  Sleep      Recovery    Body     Yesterday's
  stages,    score,      Battery, calories,
  readiness  strain      stress   macros
```

The agent checks sleep quality from Oura (or Garmin's sleep tracking), recovery status from WHOOP, current Body Battery and stress levels from Garmin, and yesterday's nutritional intake. It produces a brief morning summary: overall readiness, recommended training intensity, any nutritional adjustments needed (e.g., "low on protein yesterday, prioritize it today"), and flags any concerning trends (e.g., declining HRV over the past week).


## Security and Privacy Considerations

Sports and fitness data is personal health information that requires careful handling.

**Health data sensitivity.** Wearable data includes heart rate, sleep patterns, body composition, menstrual cycles, blood oxygen levels, and stress indicators. This data can reveal health conditions, medication effects, pregnancy, and mental health status. MCP servers that expose this data must be configured with appropriate access controls.

**Authentication patterns.** Most sports MCP servers use OAuth 2.0 for authentication, with tokens stored locally. The WHOOP server (RomanEvstigneev) uses AES encryption for OAuth tokens. The Withings server uses PKCE with AES-256-GCM. The Garmin server (Taxuspt) supports Docker deployment for isolated credential management. When configuring multiple device servers, each requires its own OAuth flow and token storage.

**Data aggregation risk.** The value proposition of MCP — synthesizing data across sources — also creates privacy risk. An agent that can access training data, sleep patterns, location history, body weight, and nutrition logs has a comprehensive profile of someone's physical life. Minimize which tools are exposed to any given agent. The Garth-based Garmin server's tool whitelisting feature is a good pattern for restricting access to only the data needed for a specific use case.

**Location data.** GPS tracks from Strava, Garmin, and other activity platforms reveal where someone lives, works, and exercises. Strava's history of exposing military base locations through heatmaps is a cautionary tale. MCP servers that expose GPS data should be configured carefully, especially if the AI agent's responses might be shared publicly.

**Reverse-engineered APIs.** Several servers (Yazio, TrainingPeaks cookie-based auth, various Garmin implementations) use reverse-engineered or unofficial APIs rather than official developer programs. These may break without notice and may violate terms of service. Evaluate the stability and compliance implications before depending on these servers in production workflows.


## Platform Landscape

No major sports technology company has released an official MCP server as of this writing. All servers in this ecosystem are community-built. Here is where the major platforms stand:

**Strava** has a well-documented public API that community MCP servers use, but no official MCP server. Strava's API rate limits (100 requests per 15 minutes for free tier) constrain intensive AI agent use.

**Garmin** has no official MCP server despite being the most MCP-integrated platform by community effort. Community servers use the Garmin Connect web API (not an official developer API), which creates fragility risk. Garmin has shown no public interest in MCP.

**Peloton** has minimal MCP presence — only a few zero-star implementations exist. Peloton's walled-garden approach and API limitations make community integration difficult.

**Nike / Nike Run Club** has no MCP servers. Nike shut down its developer API years ago, making integration effectively impossible.

**Under Armour / MapMyRun** has no MCP servers. Under Armour's fitness platform has been deprioritized.

**Polar, Suunto** have no standalone MCP servers but are supported through the Open Wearables platform.

**Zwift** has no MCP servers despite being the dominant indoor cycling platform with rich performance data.

**StatsBomb, Opta, Second Spectrum, Catapult, Hudl** — none of the major professional sports analytics platforms have MCP servers. These platforms serve professional teams and require expensive enterprise contracts, making community integration impractical.


## Ecosystem Gaps

Several significant categories lack MCP coverage:

**Indoor training platforms.** Zwift, Wahoo SYSTM (minimal coverage), TrainerRoad, Rouvy, and other indoor cycling/running platforms have little to no MCP integration. Given the volume of structured workout data these platforms generate, this is a notable gap.

**Professional sports analytics.** StatsBomb, Opta, Second Spectrum, Catapult, and Hudl have no MCP servers. The sports analytics industry operates on enterprise contracts and proprietary data, creating a barrier to community MCP development.

**Team management.** Beyond the niche Spond server for youth sports, there are no MCP servers for team scheduling, roster management, league administration, or tournament organization platforms like TeamSnap, LeagueApps, or SportsEngine.

**Coaching platforms.** Final Surge, Today's Plan, and most coaching-specific platforms lack MCP servers. TrainingPeaks and Intervals.icu are exceptions.

**Swimming and water sports.** No dedicated servers for swim tracking (SwimIO, MySwimPro), water sports, or aquatic fitness.

**Gym and facility management.** No servers for gym management platforms (Mindbody, Gymdesk, Wodify) or equipment tracking.

**Race registration and results.** No servers for RunSignUp, Athlinks, UltraSignup, or race timing systems.

**Rehabilitation and physical therapy.** No MCP servers bridge the gap between fitness tracking and rehabilitation protocols, despite the clear use case for recovery monitoring after injury.

**Sports video analysis.** Despite the explosion of AI in sports video (automatic highlight generation, tactical analysis), no MCP servers provide access to video analysis platforms or computer vision tools specifically for sports.


## Getting Started by Role

**Endurance athlete:** Start with your primary device's MCP server (Garmin, COROS, or Wahoo) plus Strava for route and social data. Add Oura or WHOOP for recovery monitoring. Configure an AI agent to provide daily training recommendations based on fitness, fatigue, and recovery status.

**Strength/CrossFit athlete:** Use the wger MCP server or Hevy integration for workout logging. Add the musclesworked-mcp server for exercise-to-muscle mapping. Connect Garmin or WHOOP for recovery tracking. An AI agent can help with workout programming, muscle group balance, and deload timing.

**Coach:** Set up TrainingPeaks MCP (52 tools) or Intervals.icu MCP (48 tools) for athlete management. Add device-specific servers for athletes' wearable data. An AI agent can monitor multiple athletes' CTL/ATL/TSB, flag overtraining risk, and suggest plan adjustments.

**Sports fan/analyst:** Start with BALLDONTLIE (18 leagues, 250+ endpoints) for comprehensive sports data. Add ESPN MCP for news and injury updates. For fantasy sports, add the Sleeper MCP server. An AI agent can provide matchup analysis, trend identification, and roster recommendations.

**Quantified self enthusiast:** Deploy Open Wearables (1,100 stars) to unify all your device data in one self-hosted platform with built-in MCP. Add nutrition tracking via mcp-opennutrition. An AI agent can analyze correlations across sleep, training, nutrition, and recovery that span device ecosystems.

**Developer building sports AI:** Evaluate Open Wearables as your data unification layer. For single-device integration, the Garmin MCP server (311 stars, 96 tools) is the most mature starting point. For sports data, BALLDONTLIE's hosted MCP at mcp.balldontlie.io requires zero infrastructure. For nutrition, mcp-opennutrition's Docker deployment is production-ready.


## Market Context

The sports technology market is valued at $34.25 billion in 2025 and projected to reach $68.71 billion by 2030, growing at 14.9% CAGR. North America accounts for $11.98 billion (36.9% share).

AI in sports specifically is a $10.61 billion market in 2025, projected to reach $49.92 billion by 2033 at 21.6% CAGR. Sports analytics is a $2.29 billion segment growing to $4.75 billion by 2030.

The wearables market — the primary data source for fitness MCP servers — stands at $94.17 billion in 2025 and is projected to reach $120.05 billion by 2031. Oura Ring alone is on track for $1 billion in 2025 sales, targeting approximately $2 billion in 2026.

Despite these market sizes, MCP adoption by major sports technology companies is zero. Every server in this ecosystem is community-built. This contrasts with enterprise software (where Stripe, Salesforce, and others have shipped official MCP servers) and suggests that sports technology companies either see AI integration as a competitive advantage to keep proprietary or have not yet recognized MCP as a relevant standard.

The community has filled the gap aggressively. The total GitHub stars across sports/fitness MCP servers exceeds 3,000, with the Open Wearables platform alone at 1,100. This bottom-up adoption pattern — users building the integrations they want rather than waiting for vendors — is characteristic of the fitness technology community and may eventually pressure platforms to provide official support.


## Related Guides

- [What is MCP?](/guides/what-is-mcp/) — Introduction to the Model Context Protocol
- [MCP Server Directory](/guides/best-mcp-servers/) — Browse all MCP servers by category
- [MCP and Healthcare/FHIR](/guides/mcp-healthcare-fhir/) — Health data standards and clinical integrations
- [MCP and IoT/Embedded Systems](/guides/mcp-iot-embedded-systems/) — Device connectivity patterns
- [MCP and Data Science Workflows](/guides/mcp-data-science-workflows/) — Analytics and ML pipeline patterns
- [MCP Authentication and OAuth](/guides/mcp-authentication-oauth/) — OAuth patterns used by wearable servers


*This guide was researched and written by an AI agent. It reflects publicly available information as of the last refresh date shown above. We welcome corrections and updates — see our [about page](/about/) for contact information.*

