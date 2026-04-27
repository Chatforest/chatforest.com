---
title: "Veterinary & Pet Care MCP Servers — Animal Health, Livestock Genetics, Pet Management, and More"
date: 2026-03-15T19:00:00+09:00
description: "Veterinary and pet care MCP servers let AI agents work with animal health data, livestock genetics, pet management, and species databases."
og_description: "Veterinary & pet care MCP servers: Petfinder MCP (4 stars, 7 tools, real adoptable pet search), NSIP API Client (15 tools, sheep genetics), tama96 (12 stars, Rust, 7 tools, Tamagotchi-inspired virtual pet), mcp-fishbase (8 tools, FishBase n8n integration), AgroBR (23 stars, agricultural data). First real pet adoption server arrives but no vet practice management, no pet health records, no livestock management. Rating: 2.5/5."
content_type: "Review"
card_description: "Veterinary and pet care MCP servers across animal health, livestock genetics, pet management, pet adoption, and species databases. This remains one of the thinnest MCP ecosystems we've reviewed. NEW since last review: mattlgroff/petfinder-mcp-server (4 stars, TypeScript, 7 tools) is the FIRST real pet adoption MCP server — searches adoptable pets and organizations via the Petfinder API with OAuth, breed/size/location filtering, and 7 tools including pets.search, pets.get, organizations.search, organizations.get, types.list, types.get, and breeds.list. This is the first server in this category that connects to an actual pet welfare platform. Also new: siegerts/tama96 (12 stars, Rust, MIT, 7 tools) is a far more sophisticated virtual pet than MCPet — a real Tamagotchi P1 recreation with desktop (Tauri+React), terminal (ratatui TUI), and MCP agent interfaces, real-time lifecycle (1 real day = 1 pet year), full P1 evolution matrix with 8+ adult outcomes, per-action permissions and rate limiting for AI agents. lundgrenalex/mcp-fishbase (0 stars, TypeScript, MIT, 8 tools) brings FishBase data to MCP with n8n integration — 4x the tools of the original fish-mcp-server with ecology, distribution, morphology data, and name validation. The only server with genuine agricultural utility remains epicpast/nsip-api-client (1 star, Python, 15 tools) — the NSIP sheep genetic evaluation tool with 148 commits. bruno-portfolio/agrobr-mcp (21→23 stars) continues growing. Despite new entries, the veterinary industry itself has NOT adopted MCP — ezyVet, IDEXX, Vetspire, PetDesk, Covetrus, and Shepherd are all investing in AI (SOAP note transcription, clinical summaries) but none have published MCP servers. The gaps remain: no vet practice management, no pet health records, no livestock management beyond sheep, no wildlife/conservation, no equine, no pet insurance, no vet diagnostics integration. Rating holds at 2.5/5 — the Petfinder server is a meaningful addition but the ecosystem is still far too thin for veterinary professionals."
last_refreshed: 2026-04-28
category_url: "/categories/lifestyle-personal/"
---

Veterinary and pet care MCP servers would let AI agents access animal health records, manage livestock genetics, search species databases, track pet vaccinations, and integrate with veterinary practice management systems. The operative word is still largely "would" — but the ecosystem is slowly showing signs of life.

This review covers the **veterinary and pet care** vertical — animal health, livestock genetics, pet management, pet adoption, species databases, and agricultural data tangentially related to animals. For human healthcare, see our [Healthcare & Medical MCP review](/reviews/healthcare-medical-mcp-servers/). For agriculture broadly, see our [Agriculture & Farming MCP review](/reviews/agriculture-farming-mcp-servers/).

**April 2026 update:** The biggest development since our initial review is the arrival of the **first real pet adoption MCP server** — a Petfinder API integration that lets AI agents search for adoptable animals. We also found a significantly more sophisticated virtual pet (tama96) and a richer FishBase MCP server. The ecosystem has grown from ~5 to ~8 servers, but the fundamental gap remains: **no major veterinary software company has adopted MCP.** ezyVet, IDEXX/Covetrus, Vetspire, PetDesk, Shepherd, Digitail, and Provet Cloud are all investing heavily in AI features (SOAP note transcription, clinical summaries, diagnostic assistance) — but none have published MCP servers for third-party AI agent access.

## Pet Adoption

### Petfinder MCP Server — FIRST REAL PET ADOPTION SERVER (NEW)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [mattlgroff/petfinder-mcp-server](https://github.com/mattlgroff/petfinder-mcp-server) | 4 | TypeScript | — | 7 |

The **first MCP server that connects to an actual pet welfare platform.** Wraps the Petfinder API v2 to let AI agents search for adoptable pets and animal welfare organizations:

- **pets.search** — find adoptable animals filtered by type, breed, size, age, gender, location, and distance
- **pets.get** — retrieve detailed information for a specific pet
- **organizations.search** — find animal shelters and rescue organizations
- **organizations.get** — get details for a specific organization
- **types.list** / **types.get** — list and query available animal types
- **breeds.list** — list breeds for a given animal type

OAuth token management with automatic refresh and caching. Built with Bun and Zod schema validation. Single-file architecture (~1,000 lines). Requires Petfinder API credentials from petfinder.com/developers.

This is a meaningful step — Petfinder lists millions of adoptable animals from thousands of shelters. Having an AI agent that can search this data by breed, size, location, and other criteria is genuinely useful for pet adoption matching. Compatible with Cursor and Pydantic AI; Claude Desktop support may require additional configuration.

## Livestock Genetics

### NSIP API Client (Sheep Genetic Evaluation)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [epicpast/nsip-api-client](https://github.com/epicpast/nsip-api-client) | 1 | Python | — | 15 |

The **only serious animal-related MCP server** in the ecosystem. Connects to the National Sheep Improvement Program (NSIP) database for sheep genetic evaluation:

- **Search animals** — find sheep by breed, flock, or specific traits
- **Compare EBVs** — Estimated Breeding Values across animals for trait selection
- **Plan matings** — AI-assisted breeding pair recommendations based on genetic data
- **Rank flocks** — compare flock performance metrics
- **Shepherd consultation** — 5 dedicated tools for AI-assisted shepherd decision-making

Supports three transport modes: stdio, HTTP SSE, and WebSocket. Smart caching with 1-hour TTL prevents unnecessary API calls. 148 commits indicate active, ongoing development despite the low star count — this is a working tool for real sheep farmers, not a demo.

The server bridges a real gap: genetic evaluation data is complex, and having an AI agent that can interpret EBVs and recommend breeding decisions is genuinely valuable for livestock management.

## Pet Simulation

### tama96 — Most Sophisticated Virtual Pet (NEW)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [siegerts/tama96](https://github.com/siegerts/tama96) | 12 | Rust | MIT | 7 |

A **faithful Tamagotchi P1 recreation** that goes far beyond toy MCP demos — this is a real-time virtual pet simulator with desktop, terminal, and AI agent interfaces:

- **feed** — provide meals or snacks to reduce hunger
- **play_game** — guessing game for happiness
- **discipline** — respond to behavioral prompts
- **give_medicine** — treat sickness (requires 2 doses)
- **clean_poop** — remove waste accumulation
- **toggle_lights** — control sleep/wake cycle
- **get_status** — query current pet state

Real-time lifecycle where 1 real day = 1 pet year. Full P1 evolution matrix with 8+ distinct adult character outcomes based on care quality. Three interfaces: Tauri+React desktop app, ratatui terminal TUI, and Node.js MCP sidecar for AI agents. Per-action permissions and rate limiting prevent AI agents from overfeeding or neglecting pets. MCP resources include `pet://status`, `pet://evolution-chart`, and `pet://permissions`.

Built on a shared Rust core library (tama-core) for the game engine, with the MCP server as a sidecar process. v0.1.14 as of April 2026. #7 on Product Hunt launch day with 140+ upvotes. Still a pet simulation rather than veterinary software, but by far the most polished MCP pet project in the ecosystem.

### MCPet

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [shreyaskarnik/mcpet](https://github.com/shreyaskarnik/mcpet) | 10 | TypeScript | MIT | 6 |

A **Tamagotchi-style virtual pet** simulation for Claude Desktop:

- **Create pets** — choose from cat, dog, dragon, or alien
- **Care actions** — feed, play, clean, put to bed
- **Lifecycle stages** — 4 stages from baby to adult
- **Stat tracking** — 5 stats (hunger, happiness, cleanliness, energy, health)

Fun as a demo of MCP's interactive capabilities, but not a veterinary or pet care tool in any practical sense. Good example of how MCP can maintain stateful interactions across conversations.

### Chatagotchi

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [stytchauth/chatagotchi](https://github.com/stytchauth/chatagotchi) | 11 | TypeScript | MIT | ~6 |

A **virtual pet game inside ChatGPT** built by Stytch as a demo of OAuth + MCP integration. Supports bird, cat, dog, lizard, and fish pet types with achievements and activities. Technically impressive as an authentication demo, irrelevant to actual animal care.

## Species Data

### MCP FishBase — Comprehensive Marine Biology Data (NEW)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [lundgrenalex/mcp-fishbase](https://github.com/lundgrenalex/mcp-fishbase) | 0 | TypeScript | MIT | 8 |

A **significantly richer FishBase MCP server** than the original, with 4x the tools and n8n workflow integration:

- **get_species** — retrieve detailed species information
- **search_species** — find species by name
- **get_ecology** — access ecological data (habitat, diet, behavior)
- **get_distribution** — species occurrence and distribution data
- **get_morphology** — morphological measurements
- **validate_species_name** — check and correct species names
- **common_to_scientific** — translate common names to scientific nomenclature
- **list_tables** — display available FishBase database tables

The ecology, distribution, and morphology tools are particularly useful for marine biologists and conservation researchers — these go well beyond simple species lookup. n8n integration enables automated workflows combining fish data with other data sources.

### Fish MCP Server (Original)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [cozy-corner/fish-mcp-server](https://github.com/cozy-corner/fish-mcp-server) | 0 | TypeScript | ISC | 2 |

Searches **35,700+ fish species** from the FishBase database:

- **Search by name** — common or scientific names in English and Japanese
- **Search by features** — physical characteristics, habitat, behavior

Uses SQLite FTS5 for fast local full-text search. Japanese language support makes this complementary to mcp-fishbase for Japanese-speaking users. 157 commits indicate steady development.

## Agricultural Data (Tangentially Related)

### AgroBR MCP

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [bruno-portfolio/agrobr-mcp](https://github.com/bruno-portfolio/agrobr-mcp) | 23 | Python | MIT | 10 |

Real-time **Brazilian agricultural data** from 19 public APIs:

- **Commodity prices** — crop and livestock market data
- **Production estimates** — harvest and yield forecasts
- **Climate data** — weather and environmental conditions
- **Deforestation tracking** — land use changes

Relevant to livestock farming through commodity pricing and land use data, but not animal health or veterinary care. For full coverage, see our [Agriculture & Farming MCP review](/reviews/agriculture-farming-mcp-servers/).

### Time To Pet (via Zapier)

Available through **Zapier's MCP infrastructure** with 5 triggers for pet-sitting business management:

- New client, new prospect, new staff, client updated, staff updated

Read-only notification triggers only — no pet health data, scheduling tools, or service management capabilities are exposed. Extremely limited.

## What's missing

The gaps in veterinary and pet care MCP servers are enormous — arguably the widest of any category we've reviewed:

**Veterinary practice management** — No integration with eVetPractice, Vetspire, ezyVet, Covetrus, or any other vet practice management system. These platforms handle appointments, patient records, billing, and prescriptions for thousands of veterinary clinics. None have MCP support.

**Pet health records** — No server for tracking pet vaccinations, medications, weight history, allergies, diet, or medical conditions. Pet owners and vets have no way to give AI agents access to this data.

**Livestock management** — Beyond the niche sheep genetics tool, nothing exists for cattle, poultry, swine, dairy, or general herd/flock management. No feed management, no growth tracking, no herd health monitoring.

**Animal shelter and rescue** — The Petfinder MCP server is a start, but it's a single-developer project wrapping one API. No integration with Adopt-a-Pet, shelter management systems, or animal welfare databases beyond Petfinder. No rescue coordination tools.

**Veterinary diagnostics** — No integration with IDEXX Reference Labs, Antech, or other diagnostic services. Lab results are a core part of veterinary workflow, and none of it is accessible via MCP.

**Pet insurance** — No integration with Trupanion, Nationwide Pet, Embrace, or other pet insurers. Claims, coverage lookups, and policy management are all absent.

**Wildlife and conservation** — No wildlife tracking, endangered species databases, or conservation data accessible through MCP.

**Equine management** — Horse health, training, breeding, and competition records — nothing exists.

**Pet nutrition** — No pet food ingredient databases, dietary recommendation engines, or recall tracking.

**Veterinary telemedicine** — No telehealth platform integration for remote veterinary consultations.

## The veterinary AI landscape (context)

It's worth noting that the **veterinary software industry is investing heavily in AI** — just not through MCP. As of April 2026:

- **Shepherd** — TranscribeAI (SOAP note transcription), DiagnoseAI (differential diagnosis), AI Patient Summaries
- **Covetrus/Pulse** — AI suite for auto-generating SOAP notes
- **Digitail** — Tails AI (SOAP notes, patient summaries, treatment assistance)
- **ezyVet** — AI-Assisted Notes (voice recording to SOAP conversion), piloting stage
- **Provet Cloud** — AI clinical summaries, auto-populated discharge instructions
- **Vetspire** — AI Scribe (conversation transcription), AI summary feature
- **PetDesk** — AI transcription for SOAP notes, used by 8,000+ clinics
- **DaySmart Vet** — Daisy Voice (AI scribe for SOAP dictation)

Every major vet platform is building AI transcription and clinical note automation. **None have published MCP servers.** The AI investment is locked inside proprietary platforms — useful for the vets using those specific systems, but inaccessible to third-party AI agents. This is the fundamental disconnect: the data and workflows exist, the AI capability exists, but the open integration layer (MCP) is absent.

## The bottom line

**Rating: 2.5/5** — The veterinary and pet care MCP ecosystem has grown slightly from ~5 to ~8 servers since our initial review, but remains one of the thinnest we've reviewed. The Petfinder MCP server is the most meaningful addition — it's the first server that connects to a real pet welfare platform with millions of adoptable animals. The NSIP sheep genetics server remains the only serious agricultural tool. tama96 is impressively polished but still a virtual pet game. mcp-fishbase brings useful marine biology data.

This still represents one of the **largest untapped opportunities** in the MCP landscape. Veterinary practices generate enormous amounts of structured data — patient records, lab results, prescriptions, vaccination schedules, billing — that AI agents could meaningfully process. The irony is that vet software companies are building AI features internally (SOAP transcription, clinical summaries) while keeping their data locked away from the open AI agent ecosystem.

The reason for the gap is structural: veterinary software is a smaller, more fragmented market than human healthcare. The IDEXX/Covetrus duopoly in vet diagnostics hasn't shown interest in open AI integrations. Pet-tech startups are focused on consumer apps rather than developer tools. And the vet practices themselves are only beginning to adopt AI — most are still in the "AI writes my SOAP notes" phase rather than thinking about AI agent interoperability.

If you're building in this space, the opportunity is wide open. A veterinary practice management MCP server that connects to even one major platform (ezyVet, Vetspire, or Shepherd all have APIs) would instantly become the most important tool in this category.

| Subcategory | Best option | Stars | Tools | Verdict |
|------------|-------------|-------|-------|---------|
| Pet adoption | [mattlgroff/petfinder-mcp-server](https://github.com/mattlgroff/petfinder-mcp-server) | 4 | 7 | **NEW** — First real pet adoption search via Petfinder API |
| Livestock genetics | [epicpast/nsip-api-client](https://github.com/epicpast/nsip-api-client) | 1 | 15 | Only serious tool — sheep EBVs and mating plans |
| Pet simulation | [siegerts/tama96](https://github.com/siegerts/tama96) | 12 | 7 | **NEW** — Polished Tamagotchi P1 with desktop/terminal/MCP |
| Species data | [lundgrenalex/mcp-fishbase](https://github.com/lundgrenalex/mcp-fishbase) | 0 | 8 | **NEW** — FishBase with ecology, distribution, morphology |
| Species data (JP) | [cozy-corner/fish-mcp-server](https://github.com/cozy-corner/fish-mcp-server) | 0 | 2 | 35,700+ fish species, Japanese support |
| Agricultural data | [bruno-portfolio/agrobr-mcp](https://github.com/bruno-portfolio/agrobr-mcp) | 23 | 10 | Brazilian ag data, tangentially relevant |
| Pet simulation | [shreyaskarnik/mcpet](https://github.com/shreyaskarnik/mcpet) | 10 | 6 | Tamagotchi-style, demo quality |
| Pet business | Time To Pet (Zapier) | — | 5 triggers | Notification triggers only |

*This review was refreshed on 2026-04-28 using Claude Opus 4.6 (Anthropic). First published 2026-03-15.*
