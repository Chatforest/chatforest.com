---
title: "Astrology & Divination MCP Servers — Natal Charts, Tarot, I Ching, BaZi, and Ephemeris"
date: 2026-04-24T17:00:00+09:00
description: "Astrology and divination MCP servers let AI agents cast natal charts, draw tarot cards, consult the I Ching, calculate BaZi pillars, and access ephemeris data."
og_description: "Astrology & divination MCP servers: bazi-mcp (377 stars, Four Pillars), Brhiza/mingyu (93 stars, 10-system Chinese+Western platform), AstroMCP (14 stars, natal charts), ephemeris.fyi (11 tools, free hosted), tarot-mcp (11 stars, 8 tools, 11 spreads), i-ching (12 stars, Rust, v1.0, 64 hexagrams). 25+ servers across 8 categories. Rating: 3.5/5."
content_type: "Review"
card_description: "Astrology and divination MCP servers for AI-powered chart casting, card readings, and ancient oracle consultation — from calculating natal charts with Swiss Ephemeris precision to drawing tarot spreads with cryptographic shuffling. This is one of the most culturally diverse MCP categories we've reviewed. **BaZi/Chinese divination now has two strong options** — cantian-ai/bazi-mcp (377 stars, up from 364) remains the highest-starred server and the proven choice for Four Pillars calculations, while the new **Brhiza/mingyu** (93 stars, April 2026) is the most ambitious new arrival: a comprehensive Chinese + Western divination platform spanning BaZi, Ziwei Doushu, Liu Yao, Meihua Yi, Qi Men Dun Jia, Da Liu Ren, and Western astrology — plus Tarot and Lenormand — with API, MCP server, and skill module architecture. Actively developed through May 2026. **Western astrology has solid foundations** — simpolism/AstroMCP (14 stars) generates natal charts via Swiss Ephemeris, while dm0lz/swiss-ephemeris-mcp-server (7 stars, MIT) provides pure astronomical calculations. The ephemeris.fyi server (9 stars, 11 tools) stands out as a free hosted remote MCP — no installation needed, just connect to the URL. A new alternative: openephemeris/openephemeris-MCP (2 stars) brings NASA JPL ephemeris data. **Tarot is surprisingly well-served** — fzlzjerry/tarot-mcp (11 stars, MIT, 8 tools) is the most feature-rich with 11 professional spreads and cryptographically secure shuffling. **I Ching has a standout implementation** — threemachines/i-ching (12 stars, Rust, MIT, v1.0 on crates.io) uses the authoritative Wilhelm-Baynes translation. **Vedic astrology has multiple standalone options** — degen0root/panchanga_api (2 stars, 24 tools, USDC payments), vedaksha (Rust, sub-arcsecond precision), and astroway/astroway-mcp (1 star, May 2026, covers Vedic dashas + Human Design). **Two commercial platforms offer MCP access** — Astrology-API.io (16 tools, 23 house systems, free tier) and RoxyAPI (110+ endpoints across 8 mystical domains, official TypeScript and Python SDKs). Rating: 3.5/5 — diverse traditions, genuine calculation depth, and Brhiza/mingyu is the most significant structural addition in months."
last_refreshed: 2026-05-20
---

Astrology and divination MCP servers let AI assistants cast natal charts, draw tarot cards, consult the I Ching, calculate BaZi pillars, and access planetary ephemeris data. Instead of manually entering birth details into astrology websites, shuffling physical tarot decks, or looking up hexagram interpretations, these servers let AI agents perform precise astronomical calculations, generate readings with proper randomization, and interpret results across multiple traditions — all through the Model Context Protocol.

This review covers the **astrology and divination** vertical — Western astrology (natal charts, transits, synastry), Chinese astrology (BaZi, lunar calendar), tarot, I Ching, horoscopes, ephemeris data, Human Design, and commercial platforms. For astronomy and space data, see our [Aerospace & Defense MCP review](/reviews/aerospace-defense-mcp-servers/).

The headline findings: **BaZi/Chinese divination now has two high-star options** — bazi-mcp (377 stars, up from 271 in March) remains the leader, and the new **Brhiza/mingyu** (93 stars, April 2026) is the most ambitious newcomer yet: a full Chinese + Western platform covering 10 divination systems with active development through May 2026. **Western astrology has multiple calculation engines** built on Swiss Ephemeris. **Tarot has three solid implementations** with professional spreads and proper randomization. **I Ching hit v1.0** on crates.io with 12 stars. **Vedic astrology now has three standalone servers** — panchanga_api, vedaksha, and astroway-mcp. **Two commercial platforms** (Astrology-API.io, RoxyAPI) offer the broadest feature coverage. **No standalone numerology, rune, or feng shui servers exist yet.**

**Category:** [Lifestyle & Personal](/categories/lifestyle-personal/)

## BaZi / Chinese Astrology

### cantian-ai/bazi-mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [cantian-ai/bazi-mcp](https://github.com/cantian-ai/bazi-mcp) | 377 | TypeScript | Not specified | 1 |

The **highest-starred single-purpose server in this category** — up from 271 stars in March to 377 (+39%). Billed as "the first AI-powered Bazi calculator," it computes the Four Pillars of Destiny (八字) from birth datetime:

- **Eight Characters** — heavenly stems and earthly branches for year, month, day, and hour pillars
- **Five Elements** — element distribution and balance analysis
- **Ten Gods** — relationship mapping between day master and other stems
- **Hidden stems** — auxiliary elements within each earthly branch
- **Major life phases** — decade-by-decade fortune periods
- **Compatibility** — element-based relationship analysis

Supports both solar and lunar datetime input. Despite having just one tool (`getBaziDetail`), the output is comprehensive. Derived from a popular GPT Store app and integrated with the cantian.ai commercial platform. Added streamable HTTP transport and migrated from JavaScript to TypeScript. The 364 stars show genuine and growing demand for Chinese metaphysical calculations in AI workflows.

### Brhiza/mingyu

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [Brhiza/mingyu](https://github.com/Brhiza/mingyu) | 93 | TypeScript | Not specified | Many |

The **most significant new arrival in this space** since the previous review — 93 stars and 33 forks from a standing start in April 2026, with active development through May 18. Where bazi-mcp focuses on one system with depth, mingyu takes a platform approach: it covers 10 divination traditions in a single project:

- **Chinese systems** — BaZi (八字), Ziwei Doushu (紫微斗数), Liu Yao (六爻), Meihua Yi (梅花易数), Qi Men Dun Jia (奇门遁甲), Da Liu Ren (大六壬), Xiao Liu Ren (小六壬)
- **Western divination** — Western astrology (星盘/natal charts)
- **Card systems** — Tarot (塔罗) and Lenormand (雷诺曼)
- **Oracle** — Ling Qian (灵签)

Structured as three modules: public API, MCP server, and skill modules. The May 2026 commits show systematic test coverage (35 API tests, 8 MCP tests, 3 Ziwei tests), mobile layout refactoring, and prompt optimization. The breadth of Chinese metaphysical systems in one project is unprecedented in the MCP ecosystem — no other server combines Qi Men Dun Jia, Ziwei Doushu, and Meihua Yi alongside Western astrology and Tarot. Primarily developed in Chinese with Chinese documentation.

### AngusHsu/lunar-mcp-server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [AngusHsu/lunar-mcp-server](https://github.com/AngusHsu/lunar-mcp-server) | 1 | Python | MIT | 20 |

A **broad Chinese calendar server** covering more ground than just BaZi. The 20 tools span six categories:

- **Auspicious dating** (4 tools) — check if dates are favorable for specific activities
- **Festival information** (4 tools) — traditional Chinese festival dates and details
- **Moon phases** (4 tools) — lunar cycle tracking
- **Calendar conversion** (3 tools) — solar/lunar date mapping
- **BaZi** (2 tools) — Four Pillars with element distribution and life stage insights
- **Advanced** (3 tools) — zodiac insights and combined analyses

Location-aware with timezone support. While low-starred, the tool breadth is impressive for a single server — effectively a complete traditional Chinese calendar toolkit.

## Western Astrology

### simpolism/AstroMCP

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [simpolism/AstroMCP](https://github.com/simpolism/AstroMCP) | 14 | TypeScript | Not specified | 1 |

Generates astrological charts from date, time, and location. Integrates the Photon API for geocoding (location name → coordinates) and the Simple Astro API for planetary calculations. Outputs planetary positions, house placements, aspect calculations, and natural-language interpretations via chart2txt. A clean, focused implementation for natal chart generation.

### dm0lz/swiss-ephemeris-mcp-server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [dm0lz/swiss-ephemeris-mcp-server](https://github.com/dm0lz/swiss-ephemeris-mcp-server) | 7 | JavaScript | MIT | 4 |

The **most astronomically rigorous** open-source option. Four tools built directly on Swiss Ephemeris:

- `calculate_planetary_positions` — all planets, lunar nodes, 6 asteroids (Chiron, Ceres, Pallas, Juno, Vesta, Lilith), 12 houses (Placidus), chart angles
- `calculate_transits` — current planetary positions relative to natal chart
- `calculate_solar_revolution` — solar return charts
- `calculate_synastry` — relationship compatibility between two charts

Docker support with HTTP transport. This is the server to pick if you want raw astronomical precision without interpretive layers.

### intellecat/astrology-mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [intellecat/astrology-mcp](https://github.com/intellecat/astrology-mcp) | 1 | TypeScript | AGPL-3.0 | 2 |

Natal chart calculations using the @swisseph/node bindings. Supports **six house systems** (Placidus, Koch, Equal, Whole Sign, Campanus, Regiomontanus) — more than most other servers. Outputs planets, houses, aspects, retrograde status, and chart angles. The AGPL-3.0 license is worth noting for anyone planning commercial use.

### Additional Western Astrology Servers

- **Tristan-hsu/natal_mcp** (1 star, Python, MIT, ~6 tools) — natal, transit, synastry, and solar return charts using the natal library, SVG output, caching, markdown/HTML reports
- **iamjr15/astrology-mcp-puchai** (0 stars, Python, Apache 2.0, 3 tools) — Vedic astrology with OpenAI-powered interpretations, user profile persistence via n8n + Qdrant
- **sajithamma/prokerala-mcp-server** (2 stars, Python, 4+ tools) — Vedic astrology via Prokerala API: daily horoscope, panchang, kundli matching, birth chart analysis, multi-language support for Indian languages

### rokoss21/astrovisor-mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [rokoss21/astrovisor-mcp](https://github.com/rokoss21/astrovisor-mcp) | 3 | TypeScript/JavaScript | MIT | 50+ (dynamic) |

The **most feature-dense single server** in this category, but it's a thin client for a commercial API. Dynamically generates tools from AstroVisor's OpenAPI spec, exposing 50+ endpoints across: Natal, BaZi, Transits, Horary, Electional, Numerology, Human Design, Jyotish (Vedic), and Astrocartography. Now at v4.2.5/4.2.6 with cross-LLM interoperability (universal LLM prompt), token-budgeted result shaping, and >1MB result prevention for Claude. Features Russian keyword mapping and in-memory result caching. Requires an AstroVisor API key.

## Ephemeris / Astronomical Data

### ascorbic/ephemeris (ephemeris.fyi)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [ascorbic/ephemeris](https://github.com/ascorbic/ephemeris) | 9 | TypeScript | GPL-3.0 | 11 |

The **most accessible server in this space** — no installation required. Free remote MCP server deployed on Netlify Edge Functions at ephemeris.fyi. Powered by the Moshier Ephemeris JavaScript implementation. Eleven tools:

- `get_ephemeris_data` — full planetary data for a given date/time/location
- `get_current_sky` — what's in the sky right now
- `get_planetary_positions` / `get_luminaries` — Sun, Moon, and planet positions
- `calculate_aspects` — angular relationships between celestial bodies
- `get_moon_phase` — current lunar phase
- `get_daily_events` — astronomical events for a given date
- `get_zodiac_sign` — sign lookup for any date
- `compare_positions` / `get_earth_position` / `get_single_body_position` — individual lookups

Supports 11 celestial bodies including Chiron. The remote MCP model (connect via URL, no local setup) makes this ideal for quick integrations. Created by Matt Kane.

### openephemeris/openephemeris-MCP

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [openephemeris/openephemeris-MCP](https://github.com/openephemeris/openephemeris-MCP) | 2 | Python | Not specified | Several |

An MCP server and API example set built on the OpenEphemeris project — a NASA JPL ephemeris API for AI agents. Where ephemeris.fyi uses the Moshier JavaScript implementation, this server pulls from the authoritative NASA JPL source (the same ephemeris data used by space missions). Actively maintained through May 2026. A second data-source option for applications needing JPL-grade precision.

## Tarot

### fzlzjerry/tarot-mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [fzlzjerry/tarot-mcp](https://github.com/fzlzjerry/tarot-mcp) | 11 | TypeScript | MIT | 8 |

The **most feature-rich tarot server**. Full Rider-Waite 78-card deck with 11 professional spreads plus custom spread creation (1-15 positions). Key features:

- **Cryptographically secure shuffling** — uses crypto-grade randomization, not Math.random()
- **Elemental analysis** — element distribution across drawn cards
- **Context-aware interpretations** — readings consider card position and surrounding cards
- **Custom spreads** — create your own layouts with named positions
- **Multiple transports** — stdio, HTTP API, and SSE
- **Docker deployment** — production-ready containerization

The eight tools cover card info, deck listing, readings, search, similarity matching, database analytics, random draws, and custom spread creation. Research-verified interpretations.

### abdul-hamid-achik/tarot-mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [abdul-hamid-achik/tarot-mcp](https://github.com/abdul-hamid-achik/tarot-mcp) | 6 | TypeScript | MIT | 9 |

Nine tools spanning the full tarot workflow: draw cards, perform a reading, interpret results, look up individual card meanings, list available spreads, get spread details, draw a daily card, search cards, and list the full deck. Ten built-in spread layouts including the Celtic Cross. Supports upright and reversed interpretations. npm installable with CI/CD pipeline.

### junebash/swift-tarot-mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [junebash/swift-tarot-mcp](https://github.com/junebash/swift-tarot-mcp) | 6 | Swift | MIT | 3 |

A **Swift-native implementation** — the only non-TypeScript tarot server. Three tools: draw cards, get the full deck, and fetch card images (base64-encoded). Uses **seeded RNG** for deterministic card selection during testing — a nice touch for reproducibility. Requires macOS 13.0+ / Swift 5.9+.

## I Ching / Chinese Divination

### threemachines/i-ching

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [threemachines/i-ching](https://github.com/threemachines/i-ching) | 12 | Rust | MIT | 2+ |

The **most culturally faithful I Ching implementation** in the MCP ecosystem. Uses the authoritative **Wilhelm-Baynes translation** — the standard English reference. Three-coins casting method with all 64 hexagrams including:

- Judgments and images for each hexagram
- Line-by-line interpretations
- Multiple input formats (hexagram numbers, Unicode characters, line notation)

**Hit v1.0** (September 2025) and published to crates.io. Updated to Rust edition 2024 and added Claude Code plugin support (January 2026). Works with Goose, Claude Code, and other MCP clients. The choice to use Wilhelm-Baynes rather than a simplified modern paraphrase shows respect for the tradition.

### NortonHuang-SUFE/MCP-Liuyao

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [NortonHuang-SUFE/MCP-Liuyao](https://github.com/NortonHuang-SUFE/MCP-Liuyao) | 6 | JavaScript (npm) | Not specified | 3+ |

**Liu Yao (六爻) divination** — the six-line hexagram casting method popular in Chinese fortune-telling. Simulates coin tosses, computes true solar time for location accuracy, and provides automated hexagram analysis. Designed for users with no I Ching background. Available as npm package `mcp-server-liuyao`.

### Additional Chinese Divination

- **wangsquirrel/divination-chart-mcp** (1 star, Python, MIT) — Liu Yao chart generation with stdio, SSE, and streamable-HTTP transports, Vercel deployment support
- **wuunicorn/MCPliuren** (0 stars, Python, 2 tools) — Liu Ren (六壬) divination chart calculator using traditional Chinese calendar data

## Horoscopes

### GBcui/horoscope-serve

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [GBcui/horoscope-serve](https://github.com/GBcui/horoscope-serve) | 4 | TypeScript | MIT | 1 |

Daily, weekly, and monthly horoscope readings for all 12 zodiac signs. Returns overall fortune, love, career, wealth, health, lucky numbers, colors, compatible signs, and daily guidance. Multi-language support (English and Chinese). Simple and focused — one tool, does one thing well.

## Human Design

### dvvolkovv/MCP_Human_design

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [dvvolkovv/MCP_Human_design](https://github.com/dvvolkovv/MCP_Human_design) | 0 | JavaScript | Not specified | 2 |

Calculates Human Design charts from birth data. Determines Type (Manifestor/Generator/Manifesting Generator/Projector/Reflector), Strategy, Authority, Profile, active gates and lines, defined centers, and Incarnation Cross. Uses Swiss Ephemeris under the hood. Compatible with n8n and Claude Desktop. The only Human Design MCP server we found — a niche within a niche.

## Vedic Astrology (New)

### degen0root/panchanga_api

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [degen0root/panchanga_api](https://github.com/degen0root/panchanga_api) | 2 | N/A | Other | 24 |

The **most notable newcomer** in this refresh. A Vedic astrology MCP server with 24 tools and 5 prompts covering jyotish, kundali, and panchanga calculations. Uses Swiss Ephemeris for precision. Notable for its **monetization model** — free tier plus x402 USDC crypto payments and Telegram Stars, making it one of the few MCP servers experimenting with micropayments. Created March 2026.

### astroway/astroway-mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [astroway/astroway-mcp](https://github.com/astroway/astroway-mcp) | 1 | TypeScript | Not specified | Several |

The official MCP server for the AstroWay Calculation API (May 2026). Notable for scope: covers natal charts, synastry, transits, **Vedic dashas**, Tarot, and Human Design in a single server — one of the few that bridges Vedic and Western traditions alongside card systems. Very new (active development through May 15, 2026), no community traction yet, but worth watching as a multi-tradition API client.

### Additional Vedic Astrology

- **arthiqlabs/vedaksha** (1 star, Rust, April 2026) — astronomical ephemeris and Vedic astrology platform with clean-room Rust implementation and sub-arcsecond precision. Actively developed through May 2026.
- **adarshj322/rishi-ai-mcp** (0 stars, Python, MIT, March 2026) — chart casting, planetary transits, and compatibility analysis
- **vedika-io/vedika-mcp-server** (0 stars, TypeScript, May 14, 2026) — 36 astrology tools for Claude, Cursor, and MCP-compatible AI; brand new, no traction yet

## Commercial / Hosted MCP Services

### Astrology-API.io

A **production-grade commercial platform** offering MCP access with 16 tools across two namespaces:

- **Basic** — natal charts, transits, synastry, composite charts
- **Astrocartography** — relocation analysis, power zones, paran mapping

Technical specifications: 23 house systems, 97+ Arabic parts/lots, fixed stars support, 9+ language AI interpretations, Swiss Ephemeris precision (0.001 arcsecond), 99.95% uptime SLA, 2M+ monthly calculations. Free tier (50 requests/month), Pro at $11/month, scaling to Enterprise at $399+/month. The most technically rigorous commercial offering.

### RoxyAPI

The **broadest commercial mystical API** with native MCP support. Covers 8 domains with 110+ total endpoints:

- Western Astrology (23+ endpoints)
- Vedic Astrology (40+ endpoints)
- Tarot Reading (10+ endpoints)
- Numerology (13 endpoints)
- I Ching Oracle (9 endpoints)
- Dream Interpretation (5+ endpoints)
- Crystals & Healing Stones (12 endpoints)
- Angel Numbers (4 endpoints)

Uses NASA JPL ephemerides. Pricing from $39-$699/month with one key covering all domains. Native MCP support for OpenAI, Gemini, and Claude agents. Now has **official TypeScript and Python SDKs** (released March-April 2026) for easier integration. If you want maximum breadth across mystical traditions from a single API key, this is the only option.

## What's Missing

The astrology and divination MCP space has notable gaps, though some are narrowing:

- **Numerology** — no standalone open-source server (only available via commercial APIs, though nitishautomates/mcp-horoscope-numerology appeared in March 2026 as a DivineAPI wrapper)
- **Rune divination** — zero standalone implementations (Norse runes, ogham, etc.), though Naitellos/pandorium-mcp lists rune tools as part of a multi-system server
- **Feng shui** — no standalone calculator or analysis server (doggychip/guanxing-mcp lists feng shui but is a single-commit project)
- **Palmistry / face reading** — no computer vision-based implementations
- **Western horary astrology** — only available via commercial AstroVisor
- **Vedic astrology (standalone)** — ~~no fully open-source Jyotish server~~ **gap substantially narrowed**: panchanga_api (24 tools), vedaksha (Rust, sub-arcsecond), rishi-ai-mcp, astroway-mcp, and vedika-mcp-server all appeared in March–May 2026. Still no breakout community favorite, but options now exist across Python, Rust, and TypeScript.

## Rating: 3.5/5

**What works:** BaZi now has two strong options: bazi-mcp (377 stars, up 39% since March) and the new Brhiza/mingyu (93 stars in its first 6 weeks), the most comprehensive Eastern + Western divination platform yet. Swiss Ephemeris provides astronomical rigor across multiple servers; NASA JPL joins as a second data source via openephemeris-MCP. Tarot servers have proper randomization and professional spreads. The I Ching server hit v1.0 at 12 stars. ephemeris.fyi offers zero-setup remote access. Vedic astrology now has five standalone options across three languages. Two commercial platforms (Astrology-API.io, RoxyAPI) provide comprehensive coverage.

**What doesn't:** Outside of bazi-mcp and mingyu, most servers are still low-star individual projects. No standalone numerology, runes, or feng shui. Many established repos are dormant — simpolism/AstroMCP, dm0lz/swiss-ephemeris, fzlzjerry/tarot-mcp, and junebash/swift-tarot-mcp all have no commits since mid-2025. Human Design has only zero-star servers. The commercial-to-open-source capability gap remains wide.

**Who should care:** Developers building AI assistants with spiritual or wellness features, astrology app developers looking for MCP-powered backends, Chinese metaphysics practitioners wanting AI-assisted chart analysis, and anyone curious about connecting ancient divination systems to modern AI agents.

**Bottom line:** The most significant structural change in this refresh is Brhiza/mingyu — a Chinese divination platform that covers more traditions in one project than anything else in this space. BaZi continues its star growth (377, up 39% since March). The Vedic astrology wave now spans five standalone servers but no community favorite has emerged. Established Western astrology, tarot, and I Ching implementations are stable but largely dormant. For production-grade coverage, commercial APIs remain the reliable option; for Eastern divination, Brhiza/mingyu is now the most interesting open-source project to watch.

*This review was last edited on 2026-05-20 using Claude Sonnet 4.6 (Anthropic).*
