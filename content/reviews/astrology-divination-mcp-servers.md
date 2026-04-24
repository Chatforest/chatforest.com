---
title: "Astrology & Divination MCP Servers — Natal Charts, Tarot, I Ching, BaZi, and Ephemeris"
date: 2026-04-24T17:00:00+09:00
description: "Astrology and divination MCP servers let AI agents cast natal charts, draw tarot cards, consult the I Ching, calculate BaZi pillars, and access ephemeris data."
og_description: "Astrology & divination MCP servers: bazi-mcp (364 stars, Four Pillars), AstroMCP (14 stars, natal charts), ephemeris.fyi (11 tools, free hosted), tarot-mcp (11 stars, 8 tools, 11 spreads), i-ching (11 stars, Rust, v1.0, 64 hexagrams), swiss-ephemeris (4 tools). 20+ servers across 8 categories. Vedic astrology wave emerging. Rating: 3.5/5."
content_type: "Review"
card_description: "Astrology and divination MCP servers for AI-powered chart casting, card readings, and ancient oracle consultation — from calculating natal charts with Swiss Ephemeris precision to drawing tarot spreads with cryptographic shuffling. This is one of the most culturally diverse MCP categories we've reviewed. **BaZi dominates by stars** — cantian-ai/bazi-mcp (364 stars, up from 271) is the highest-starred server in this space by a wide margin, calculating Chinese Four Pillars of Destiny with heavenly stems, earthly branches, Five Elements, Ten Gods, and major life phases. It's derived from a popular GPT Store app and represents the strongest bridge between traditional Chinese metaphysics and modern AI. **Western astrology has solid foundations** — simpolism/AstroMCP (14 stars) generates natal charts via Swiss Ephemeris, while dm0lz/swiss-ephemeris-mcp-server (7 stars, MIT) provides pure astronomical calculations for planetary positions, transits, synastry, and solar returns. The ephemeris.fyi server (9 stars, 11 tools) stands out as a free hosted remote MCP — no installation needed, just connect to the URL. **Tarot is surprisingly well-served** — fzlzjerry/tarot-mcp (11 stars, MIT, 8 tools) is the most feature-rich with 11 professional spreads, custom spread creation, elemental analysis, and cryptographically secure shuffling. abdul-hamid-achik/tarot-mcp (6 stars, MIT, 9 tools) and junebash/swift-tarot-mcp (6 stars, Swift, MIT) round out the options. **I Ching has a standout implementation** — threemachines/i-ching (11 stars, Rust, MIT, v1.0 on crates.io) uses the authoritative Wilhelm-Baynes translation with all 64 hexagrams, judgments, images, and line interpretations. MCP-Liuyao (6 stars) adds Liu Yao six-line divination with true solar time calculation. **Vedic astrology is emerging as a wave** — new in this refresh: degen0root/panchanga_api (2 stars, 24 tools, x402 USDC payments) and vedaksha (Rust, sub-arcsecond precision) join existing prokerala-mcp-server and astrovisor-mcp (now v4.2.5, cross-LLM interoperability). **Two commercial platforms offer MCP access** — Astrology-API.io provides 16 tools with 23 house systems and Swiss Ephemeris precision from a free tier, while RoxyAPI covers 8 mystical domains (astrology, tarot, numerology, I Ching, crystals, dream interpretation, angel numbers) with 110+ total endpoints and now has official TypeScript and Python SDKs. **Gaps are narrowing** — Vedic astrology now has standalone options, but no standalone numerology MCP server, no rune divination, no feng shui calculator, and no palmistry or face reading tools. The category earns 3.5/5 — diverse traditions are represented with genuine calculation depth, bazi-mcp's surge to 364 stars shows real demand, but most servers remain low-star individual projects."
last_refreshed: 2026-04-24
---

Astrology and divination MCP servers let AI assistants cast natal charts, draw tarot cards, consult the I Ching, calculate BaZi pillars, and access planetary ephemeris data. Instead of manually entering birth details into astrology websites, shuffling physical tarot decks, or looking up hexagram interpretations, these servers let AI agents perform precise astronomical calculations, generate readings with proper randomization, and interpret results across multiple traditions — all through the Model Context Protocol.

This review covers the **astrology and divination** vertical — Western astrology (natal charts, transits, synastry), Chinese astrology (BaZi, lunar calendar), tarot, I Ching, horoscopes, ephemeris data, Human Design, and commercial platforms. For astronomy and space data, see our [Aerospace & Defense MCP review](/reviews/aerospace-defense-mcp-servers/).

The headline findings: **BaZi dominates by stars** with cantian-ai/bazi-mcp (364 stars, up 34% since March) far ahead of everything else. **Western astrology has multiple calculation engines** built on Swiss Ephemeris. **Tarot has three solid implementations** with professional spreads and proper randomization. **I Ching hit v1.0** on crates.io with Claude Code plugin support. **Vedic astrology is emerging** — panchanga_api and vedaksha are new standalone options. **Two commercial platforms** (Astrology-API.io, RoxyAPI) offer the broadest feature coverage. RoxyAPI now has official TypeScript and Python SDKs. **No standalone numerology, rune, or feng shui servers exist yet.**

**Category:** [Lifestyle & Personal](/categories/lifestyle-personal/)

## BaZi / Chinese Astrology

### cantian-ai/bazi-mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [cantian-ai/bazi-mcp](https://github.com/cantian-ai/bazi-mcp) | 364 | TypeScript | Not specified | 1 |

The **highest-starred server in this entire category by a wide margin** — up from 271 to 364 stars (+34%) since March 2026. Billed as "the first AI-powered Bazi calculator," it computes the Four Pillars of Destiny (八字) from birth datetime:

- **Eight Characters** — heavenly stems and earthly branches for year, month, day, and hour pillars
- **Five Elements** — element distribution and balance analysis
- **Ten Gods** — relationship mapping between day master and other stems
- **Hidden stems** — auxiliary elements within each earthly branch
- **Major life phases** — decade-by-decade fortune periods
- **Compatibility** — element-based relationship analysis

Supports both solar and lunar datetime input. Despite having just one tool (`getBaziDetail`), the output is comprehensive. Derived from a popular GPT Store app and integrated with the cantian.ai commercial platform. Added streamable HTTP transport and migrated from JavaScript to TypeScript. The 364 stars show genuine and growing demand for Chinese metaphysical calculations in AI workflows.

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
| [rokoss21/astrovisor-mcp](https://github.com/rokoss21/astrovisor-mcp) | 2 | TypeScript/JavaScript | MIT | 50+ (dynamic) |

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
| [threemachines/i-ching](https://github.com/threemachines/i-ching) | 11 | Rust | MIT | 2+ |

The **highest-starred divination server** and the most culturally faithful I Ching implementation. Uses the authoritative **Wilhelm-Baynes translation** — the standard English reference. Three-coins casting method with all 64 hexagrams including:

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

### Additional Vedic Astrology

- **vedaksha** (1 star, Rust, April 2026) — astronomical ephemeris and Vedic astrology platform with clean-room Rust implementation and sub-arcsecond precision. Actively developed through April 2026.
- **adarshj322/rishi-ai-mcp** (0 stars, Python, MIT, March 2026) — chart casting, planetary transits, and compatibility analysis

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
- **Vedic astrology (standalone)** — ~~no fully open-source Jyotish server~~ **gap narrowing**: panchanga_api (24 tools), vedaksha (Rust, sub-arcsecond), and rishi-ai-mcp all appeared in March-April 2026, though none yet have significant community traction

## Rating: 3.5/5

**What works:** BaZi has a genuinely popular implementation (364 stars, up 34% in 40 days). Swiss Ephemeris provides astronomical rigor. Tarot servers have proper randomization and professional spreads — fzlzjerry/tarot-mcp grew to 11 stars. The I Ching server hit v1.0 on crates.io with Claude Code plugin support. ephemeris.fyi offers zero-setup remote access. Vedic astrology is emerging with three new standalone servers. Two commercial platforms provide comprehensive coverage, with RoxyAPI adding official SDKs.

**What doesn't:** Most servers are still low-star individual projects (under 15 stars). No standalone numerology, runes, or feng shui. The gap between the commercial offerings (100+ endpoints) and open-source (1-11 tools) remains the widest we've seen in any vertical. Human Design has a single zero-star server. Many repos are stagnant — simpolism/AstroMCP, dm0lz/swiss-ephemeris, and junebash/swift-tarot-mcp all have no commits since mid-2025.

**Who should care:** Developers building AI assistants with spiritual or wellness features, astrology app developers looking for MCP-powered backends, Chinese metaphysics practitioners wanting AI-assisted chart analysis, and anyone curious about connecting ancient divination systems to modern AI agents.

**Bottom line:** This category reveals genuine cultural diversity in the MCP ecosystem — Chinese, Western, Vedic, and cross-traditional systems all have representation. The BaZi server's surge to 364 stars proves real and growing demand. The Vedic astrology wave (panchanga_api, vedaksha, rishi-ai-mcp) is the biggest structural change since our last review — a previously commercial-only gap is getting open-source attention. But most open-source implementations remain thin individually, and anyone wanting production-grade coverage will still likely need a commercial API. The free ephemeris.fyi remote server is the easy on-ramp for experimentation.

*This review was last edited on 2026-04-24 using Claude Opus 4.6 (Anthropic).*
