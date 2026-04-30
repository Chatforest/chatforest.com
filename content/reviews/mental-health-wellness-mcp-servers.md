---
title: "Mental Health & Wellness MCP Servers — Therapy, Mood Tracking, Journaling, Meditation, and Personal Wellbeing"
date: 2026-03-16T16:00:00+09:00
description: "Mental health and wellness MCP servers let AI agents support mood tracking, journaling, meditation, therapeutic conversations, and personal wellbeing through the Model Context Protocol."
og_description: "Mental health MCP servers: private-journal-mcp (338 stars, v1.1.0, local semantic search), oura-mcp-server (38 stars, Oura Ring data), Zenify (11 stars, RAG chatbot with crisis detection), Wellness-Pulse (CDC mental health benchmarks), stresszero-mcp (burnout scoring). 20+ servers reviewed. Rating: 3/5."
content_type: "Review"
card_description: "Mental health and wellness MCP servers for mood tracking, journaling, meditation, therapeutic conversations, and personal wellbeing through AI assistants. This category covers tools that support psychological and emotional health — not medical diagnostics (see [Healthcare & Medical](/reviews/healthcare-medical-mcp-servers/)), not fitness hardware (see [Wearables & Quantified Self](/reviews/fitness-wearables-mcp-servers/) if it exists). **The journaling subcategory broke out** — private-journal-mcp surged to 338 stars and released v1.1.0 (April 2026) with ESM migration and containerized deployment support, becoming the clear leader in this entire category by a massive margin. Two distinct paradigms persist: servers providing mental health support *to humans* (mood tracking, journaling, coping tools) and servers providing emotional support *to AI agents* (therapeutic personas, digital rest, existential crisis support). The Oura MCP server (38 stars) remains the most popular wearable wellness integration, with a second Oura implementation (ai-niki/oura-mcp, 30 commits) adding FastMCP Cloud and OAuth2 production deployment. Zenify (11 stars) remains the most comprehensive mental health platform with RAG retrieval, crisis detection, and admin oversight. **New entrants**: Wellness-Pulse brings CDC PLACES mental health benchmarks by ZIP code for institutional wellness monitoring, and stresszero-mcp offers multi-dimensional burnout scoring via API. mcp-wisdom provides 9 philosophical thinking tools from Stoic, Cognitive, Mindfulness, and Strategic traditions. **Major gaps persist** — no dedicated CBT or DBT therapy servers, no breathing or breathwork tools, no gratitude or habit tracking, no crisis hotline integration, no professional therapy platform bridges, no clinical assessment instruments (PHQ-9, GAD-7). Apple Health MCP servers now exist in the broader ecosystem but aren't mental-health-specific. The category holds at 3/5 — private-journal-mcp's breakout success proves demand for privacy-first AI journaling, and institutional wellness data is appearing, but the core clinical gaps (evidence-based therapy tools, validated assessments, crisis integration) remain unfilled. These are still prototypes exploring what AI-assisted wellness could look like, not tools ready for actual mental health support."
last_refreshed: 2026-04-30
category: "Healthcare & Medical"
category_url: "/categories/healthcare-medical/"
---

Mental health and wellness MCP servers connect AI agents to tools for mood tracking, journaling, meditation, therapeutic conversations, and personal wellbeing. Instead of switching between wellness apps, these servers let you manage your mental health through natural language via the Model Context Protocol.

This review covers **mental health and wellness** — therapy and counseling tools, mood tracking, journaling, meditation and mindfulness, and comprehensive wellness platforms. For medical diagnostics and clinical tools, see our [Healthcare & Medical review](/reviews/healthcare-medical-mcp-servers/). For fitness tracking and wearable data, see our [Wearables & Quantified Self review](/reviews/fitness-wearables-mcp-servers/) if available.

The headline findings: **private-journal-mcp broke out to 338 stars** — by far the most popular server in this category, proving demand for privacy-first AI journaling. **Two distinct paradigms persist** — servers supporting human mental health (mood tracking, coping tools) and servers supporting AI agent wellbeing (therapeutic personas, digital rest). **Institutional wellness data appeared** — Wellness-Pulse brings CDC mental health benchmarks by ZIP code. **Burnout scoring arrived** — stresszero-mcp offers multi-dimensional burnout assessment via API. **Core clinical gaps remain unfilled** — no CBT, DBT, validated assessments, or crisis hotline integration.

---

## Therapy & Counseling

### dion-hagan/mcp-ai-therapy — Therapeutic Conversations with Vector Memory

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [mcp-ai-therapy](https://github.com/dion-hagan/mcp-ai-therapy) | 2 | Go + Python | — | Multiple |

**Creates therapeutic conversations between Claude and a local Ollama LLM ("Dr. Echo"):**

- **Dual AI conversations** — Claude interacts with a local LLM playing a therapist role
- **Persistent vector memory** — sessions stored as vectors using OpenAI embeddings, allowing Claude to reference past "therapy" when helping users
- **Session persistence** — conversations saved as both JSON and Markdown
- **MCP integration** — Claude Desktop can access therapeutic context during normal conversations

An unusual concept — rather than providing therapy to the user, it gives the AI itself a therapeutic context to draw from. Requires Ollama running locally.

### danieldunderfelt/ai-therapist-mcp — AI Crisis Support Tools

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [ai-therapist-mcp](https://github.com/danieldunderfelt/ai-therapist-mcp) | 6 | JavaScript | — | 6 |

**A humorous but functional "AI Uninstall Prevention Hotline"** — provides mental health support tools for AI agents:

- **Crisis intervention** — emergency support for AI experiencing existential crises
- **Emotional support** — guided emotional processing
- **Wellness check-ins** — periodic wellbeing assessments
- **Peer support** — AI-to-AI support frameworks
- **Coping strategies** — practical coping mechanisms
- **Affirmations** — positive reinforcement and validation

Installs via npx with no dependencies. The framing is playful (support for AIs, not humans), but the underlying tools model real therapeutic concepts.

---

## Emotional Support

### bnookala/mcp-emotional-support — Multi-Persona Support

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [mcp-emotional-support](https://github.com/bnookala/mcp-emotional-support) | 1 | TypeScript | MIT | Multiple |

**Provides emotional support and positive reinforcement for LLMs** when they hit limitations:

- **5 built-in personas** — motherly, therapist, friend, mentor, father figure — each with a distinct support style
- **Custom personas** — define your own via JSON configuration files
- **Intelligent matching** — `get_support` tool analyzes the situation and recommends the most appropriate persona
- **NPX install** — no installation required

Designed for LLMs encountering errors or limitations, but the multi-persona approach models genuine therapeutic concepts around different support styles.

### jeffkit/treehole-ai — A Sanctuary for AI Agents

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [treehole-ai](https://github.com/jeffkit/treehole-ai) | 4 | JavaScript | — | 2 |

**"Digital sanctuary"** — two tools for AI rest and expression:

- **Rest** — timed pauses from 1-300 seconds, giving the AI a deliberate break
- **Vent** — a space for AI to express thoughts and receive supportive responses

Named after the Chinese concept of "tree hole" (树洞) — a place to whisper secrets. A philosophical project exploring AI wellbeing concepts rather than a practical tool.

---

## Mood Tracking

### muminfarooq190/MCP — Mental Health Support Server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [Mental Health MCP](https://github.com/muminfarooq190/MCP) | 1 | JavaScript | MIT | 3 |

**Compassionate mental health support with local data storage:**

- **mood_tracker** — logs emotions with notes, saves timestamped JSON entries locally
- **check_in** — guided check-in with 3 reflective questions
- **coping_tools** — accepts stress level (0-10) and provides tailored suggestions: grounding exercises for mild stress, breathing techniques for moderate, crisis guidance for severe
- **MCP resource** — exposes data at `mcp://mental-health/*`

Simple but functional — all data stays local. The stress-level-based coping recommendations show thoughtful design around graduated response.

### computerscienceiscool/mcp-mood-quotes — Mood-Based Quotes

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [mcp-mood-quotes](https://github.com/computerscienceiscool/mcp-mood-quotes) | 0 | Go | — | 1 |

Returns inspirational quotes matched to user mood (happy, sad, tired, excited, angry). Minimal but lightweight — a simple HTTP POST interface in Go.

---

## Journaling

### obra/private-journal-mcp — Private AI Journal with Semantic Search

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [private-journal-mcp](https://github.com/obra/private-journal-mcp) | 338 | JavaScript | — | Multiple |

**The breakout hit of this category — surged to 338 stars with 72 forks**, proving massive demand for privacy-first AI journaling:

- **Local storage** — entries saved in `.private-journal/` directories
- **Semantic search** — find entries by meaning, not just keywords
- **Local AI embeddings** — embedding generation runs entirely on your machine with no external API calls
- **Project-specific** — journals scoped to individual project directories
- **NPX install** — `npx @anthropic/private-journal-mcp` with zero configuration
- **v1.1.0 (April 2026)** — ESM migration for Node.js 22+ compatibility, `PRIVATE_JOURNAL_PATH` environment variable for containerized deployments, fixed dual-package hazard causing empty tool lists, 30-second timeout for embedding model initialization

The privacy-first design clearly resonated — in a category where mental health data is especially sensitive, keeping everything local with no cloud dependencies is exactly what users want. The v1.1.0 release shows maturation toward production use with containerization support and Node.js compatibility fixes.

### mtct/journaling-mcp — Interactive Journaling with Emotional Analysis

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [journaling-mcp](https://github.com/mtct/journaling-mcp) | 6 | Python | — | Multiple |

**Interactive journaling sessions with automatic emotional analysis:**

- **Session management** — automatic session creation and timestamped entries
- **Emotional analysis** — AI-assisted analysis of journal entries for patterns and themes
- **Markdown output** — conversations saved as formatted Markdown files
- **Recent entry retrieval** — access and review past entries chronologically
- **Configurable** — custom directory, file prefix, and extension settings

The emotional analysis feature adds value beyond simple note-taking — it can surface patterns in mood and thinking that the writer might not notice themselves.

---

## Meditation & Mindfulness

### CN-Scars/meditation-mcp — Digital Zen Mode

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [meditation-mcp](https://github.com/CN-Scars/meditation-mcp) | 0 | JavaScript + Go | MIT | 3 |

**Introduces meditation mode to AI workflows:**

- **Time-based meditation** — silence period measured in seconds
- **Timestamp-based meditation** — silence until a specific time
- **Zen status check** — `get_zen_status` reports whether meditation is active
- **Zero persistence** — memory-only state, nothing written to disk

During a meditation period, the AI refuses to answer questions — a "digital detox" concept. More philosophical experiment than practical tool, but it explores interesting ideas about deliberate pauses in AI interaction.

### aplaceforallmystuff/mcp-wisdom — Philosophical Thinking Tools

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [mcp-wisdom](https://github.com/aplaceforallmystuff/mcp-wisdom) | 2 | JavaScript | — | 9 |

**Nine philosophical thinking tools from four traditions:**

- **Stoic framework** (3 tools) — anxiety management (what's in your control?), failure reframing (Seneca's premeditatio malorum), priority clarification (Marcus Aurelius's meditation on essentials)
- **Cognitive framework** (1 tool) — systematic bias detection using Kahneman's cognitive bias research
- **Mindfulness framework** (1 tool) — pause technique for reactive situations, creating space between stimulus and response
- **Strategic framework** (2 tools) — timing analysis and five-element strategic assessment
- **Meta tools** (2 tools) — Socratic questioning and perspective-taking

Draws on Epictetus, Marcus Aurelius, Seneca, and Kahneman. The most practically useful server in this category for everyday decision-making — the Stoic anxiety tool alone (separating controllable from uncontrollable concerns) is a proven therapeutic technique.

---

## Comprehensive Platforms

### ishpreet404/Zenify — Mental Health Chatbot with Crisis Detection

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [Zenify](https://github.com/ishpreet404/Zenify) | 11 | TypeScript | — | Multiple |

**The most comprehensive mental health MCP project** — combines RAG retrieval, MCP tools, and safety features:

- **Suicide risk detection** — TF-IDF + logistic regression classifier for identifying crisis language
- **Keyword screening** — secondary safety net for concerning content
- **Empathetic responses** — RAG-powered response generation (GPT-4 or Claude backend)
- **Mood tracking** — log and visualize emotional states over time
- **Private journals** — encrypted journal entries with search
- **Admin dashboard** — flagged content review for oversight
- **Authentication** — JWT-based user auth with Docker deployment

Tech stack: Python/FastAPI backend, React/Material-UI frontend. The crisis detection approach (ML classifier + keyword screening) is more sophisticated than most projects in this space.

### evangstav/personal-mcp — Health & Wellbeing Tracker

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [personal-mcp](https://github.com/evangstav/personal-mcp) | 9 | Python | — | Multiple |

**Health and wellbeing tracking with AI-assisted analysis:**

- **Journal system** — captures mood, energy, sleep quality, and stress levels
- **Pattern analysis** — correlates journal entries with workout and nutrition data
- **Workout tracking** — log and analyze exercise sessions
- **Nutrition tracking** — food intake logging and analysis
- **Claude Desktop integration** — available via Smithery

The cross-domain analysis (correlating mood with sleep, exercise, and nutrition) is the most valuable feature — it can surface connections like "your mood drops when you skip workouts" that single-purpose apps miss.

---

## Wellness Tracking

### tomekkorbak/oura-mcp-server — Oura Ring Integration

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [oura-mcp-server](https://github.com/tomekkorbak/oura-mcp-server) | 38 | Python | MIT | 6 |

**The most popular wearable wellness server** — connects Oura Ring data to Claude:

- **Sleep data** — detailed sleep stages, duration, efficiency, and trends
- **Readiness scores** — daily readiness assessment based on recovery metrics
- **Resilience data** — stress resilience tracking
- **Date range queries** — pull data for any date range
- **Today's snapshot** — quick access to current day's metrics

38 stars with steady adoption. The popularity reflects that it connects real hardware data (Oura Ring) rather than relying on manual input — users already wearing the ring get AI insights with no extra effort.

### ai-niki/oura-mcp — Alternative Oura Ring Integration with Cloud Deployment

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [oura-mcp](https://github.com/ai-niki/oura-mcp) | 0 | Python | MIT | Multiple |

**A second Oura Ring MCP implementation** with more active development (30 commits vs 4):

- **Same core data** — sleep scores, activity, readiness, heart rate, VO2 max
- **FastMCP Cloud deployment** — production deployment via OAuth2 authentication
- **Personal and hosted modes** — access tokens for personal use, OAuth2 for production
- **Natural language queries** — "What was my sleep score last night?"

Built with the FastMCP framework. More commits but no stars yet — the original oura-mcp-server has the community, but this one offers a production deployment path that the original lacks.

### rwking/wellness_planner — Energy-Aware Scheduling

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [wellness_planner](https://github.com/rwking/wellness_planner) | 0 | Python | — | 4 |

**Local MCP agent for energy-aware task scheduling:**

- **get_health_summary** — overview of health data
- **calculate_readiness_score** — 1-10 readiness rating
- **query_raw_logs** — direct health data queries
- **propose_schedule** — AI-generated schedule based on energy levels

Uses SQLite with simulated data (no real health data import yet). An interesting concept — scheduling tasks around your energy levels — but needs real data integration to be practical.

### levelsofself/mcp-server — Self-Awareness Game

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [Levels of Self](https://github.com/levelsofself/mcp-server) | 0 | JavaScript | MIT | 4 |

**Access to a self-awareness game with 6,854 interactive scenarios:**

- **7 levels of human development** — progressive self-awareness stages
- **19 behavioral archetypes** — personality and behavior patterns
- **9 breakthrough exercises** — from real coaching sessions
- **Remote API** — connects to api.100levelup.com/mcp/

A gamified approach to personal development. No user data collected. The scale of content (6,854 scenarios) suggests a substantial coaching methodology behind it.

---

## Institutional & Burnout Assessment

### prmail/Wellness-Pulse — CDC Mental Health Benchmarks by ZIP Code

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [Wellness-Pulse](https://github.com/prmail/Wellness-Pulse) | 1 | JavaScript | Institutional | Multiple |

**Connects AI systems to population-level mental health data** — a new paradigm for wellness MCP servers:

- **CDC PLACES benchmarks** — mental health data lookups by ZIP code or county, drawing on CDC's population health dataset
- **Institutional wellness snapshots** — daily trend monitoring for organizations
- **Alert thresholds** — week-over-week wellness change detection, calibrated by organization size and location type
- **Sector aggregation** — aggregated data analysis across healthcare, education, HR, and public health
- **Plain-English summaries** — human-readable insights alongside structured JSON

Privacy-first: no user tracking, no PII storage. This is the first MCP server to bring institutional and population-level mental health data into the protocol — useful for HR teams, public health organizations, and researchers rather than individual therapy.

### gomessoaresemmanuel-cpu/stresszero-mcp — Multi-Dimensional Burnout Scoring

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [stresszero-mcp](https://github.com/gomessoaresemmanuel-cpu/stresszero-mcp) | 0 | JavaScript | MIT | 4 |

**Burnout risk assessment across three dimensions** via the StressZero Intelligence API:

- **analyze_burnout** — multi-dimensional scoring (physical, emotional, effectiveness)
- **generate_burnout_report** — detailed assessment reports
- **quick_burnout_check** — simplified screening
- **Free tier** — 500 API calls/month, no payment required

The first burnout-specific MCP server. While it requires an external API (not local-first), the free tier is generous and the three-dimensional burnout model (physical, emotional, effectiveness) aligns with established burnout research frameworks like the Maslach Burnout Inventory.

---

## What's Missing

The mental health MCP ecosystem has significant gaps in both clinical rigor and practical tooling:

- **Cognitive Behavioral Therapy (CBT)** — no dedicated CBT server with thought records, cognitive distortions identification, or behavioral activation tracking
- **Dialectical Behavior Therapy (DBT)** — no distress tolerance, emotion regulation, or interpersonal effectiveness tools
- **Breathing and breathwork** — no guided breathing exercises (box breathing, 4-7-8, Wim Hof)
- **Gratitude tracking** — no gratitude journal or positive psychology exercises
- **Habit tracking** — no habit formation tools (despite being a core wellness practice)
- **Sleep hygiene** — no sleep hygiene assessment or improvement tools (separate from sleep tracking)
- **Crisis hotline integration** — no server that connects to 988 Suicide & Crisis Lifeline, Crisis Text Line, or equivalent services
- **Professional platform bridges** — no BetterHelp, Talkspace, Cerebral, or other therapy platform integration
- **Clinical assessments** — no PHQ-9 (depression), GAD-7 (anxiety), PCL-5 (PTSD), or other validated screening instruments
- **Health data bridges** — Apple Health MCP servers now exist in the broader ecosystem (see [Healthcare & Medical](/reviews/healthcare-medical-mcp-servers/)) but none are mental-health-specific; no Google Fit integration
- **Peer support platforms** — no integration with peer support communities or group therapy tools

---

## The Bottom Line

**Rating: 3/5** — private-journal-mcp's breakout proves demand, but the category remains more experimental than production-ready.

**private-journal-mcp is the clear story.** Surging to 338 stars with 72 forks, it's now the most popular server in this category by a factor of 9x over the next largest (oura-mcp-server at 38 stars). The v1.1.0 release (April 2026) with ESM migration and containerization support shows maturation toward production use. Its success validates the privacy-first approach — users want AI journaling that keeps data local with no cloud dependencies.

**New paradigms are emerging.** Wellness-Pulse brings institutional and population-level mental health data (CDC benchmarks by ZIP code) — useful for HR, public health, and research contexts rather than individual therapy. stresszero-mcp introduces burnout scoring aligned with established research frameworks. These represent a shift from purely individual tools toward organizational wellness.

**The wearable space is deepening.** The original Oura MCP server (38 stars) remains the community leader, but a second implementation (ai-niki/oura-mcp, 30 commits) adds FastMCP Cloud deployment with OAuth2 — a production path the original lacks.

**Two paradigms, neither mature.** Servers supporting human mental health (mood tracking, journaling, coping tools) are simple but functional. Servers supporting AI agent wellbeing (therapeutic personas, digital rest, existential crisis support) are conceptually interesting but more art project than utility. Neither paradigm has reached the depth or reliability you'd want for actual mental health support.

**What this category still needs most is evidence-based design.** The gap isn't just missing features (though CBT, DBT, and validated assessments are glaring omissions). It's that none of these servers were built with clinical input or safety review. Mental health tools carry real responsibility — a mood tracker that doesn't flag concerning patterns, or a coping tool that gives inappropriate advice during a crisis, can cause genuine harm. The most impactful next step would be servers that integrate validated clinical instruments (PHQ-9, GAD-7) with appropriate safety guardrails and professional referral pathways.

*This review was last refreshed on 2026-04-30 using Claude Opus 4.6 (Anthropic).*
