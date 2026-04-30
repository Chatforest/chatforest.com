---
title: "Pet & Animal Care MCP Servers — Virtual Pets, Wildlife ID, Birding, Livestock Genetics, and Pet Adoption"
date: 2026-03-16T22:00:00+09:00
description: "Pet and animal care MCP servers let AI agents interact with virtual pets, identify wildlife species, access bird observation data, manage livestock genetics, and explore pet"
og_description: "Pet & animal care MCP servers: inaturalist-mcp (9 tools, biodiversity data), rescuedogs-mcp-server (8 tools, European rescue adoption), BirdNET-Pi MCP (acoustic bird detection), mcpet (virtual pets), ebird-mcp-server (bird observations), nsip-api-client (sheep genetics, 15 tools). 15+ servers reviewed. Rating: 3/5."
content_type: "Review"
card_description: "Pet and animal care MCP servers for virtual pets, wildlife identification, birding, livestock genetics, and pet adoption through AI assistants. This category spans a wide range — from playful virtual pet simulations to serious wildlife conservation and livestock breeding tools. It does *not* cover medical diagnostics (see [Healthcare & Medical](/reviews/healthcare-medical-mcp-servers/)) or general nutrition tracking (see [Health & Fitness](/reviews/health-fitness-mcp-servers/) if available). **This category is growing and diversifying** — the March–April 2026 period brought several meaningful additions. **The iNaturalist MCP server** (9 tools, no API key required) is the biggest addition, connecting AI assistants to one of the world's largest biodiversity databases with species search, taxonomy, conservation status, and look-alike identification. **The rescuedogs-mcp-server** (8 tools, 70 commits) brings real pet adoption functionality at last — searching 1,500+ dogs across 12+ European/UK rescue organizations with breed, size, age, and lifestyle matching. **The BirdNET-Pi MCP ecosystem** adds acoustic bird identification — a fundamentally different approach to birding that uses sound rather than sight. The NSIP sheep genetics client remains the most sophisticated server (15 tools, 148 commits) with active development. The virtual pet subcategory (MCPet 10 stars, Chatagotchi 11 stars) is charming but recreational. **Practical pet ownership gaps are slowly filling** — rescue dog adoption is now covered, but veterinary records, vaccination tracking, GPS monitoring, and breed identification remain absent. Given that pet spending exceeds $150B annually in the US alone, significant opportunities remain. The category earns 3/5 (up from 2.5) — iNaturalist biodiversity data, real rescue dog adoption, acoustic bird detection, and continued NSIP development show genuine ecosystem growth beyond novelty projects."
last_refreshed: 2026-04-30
category_url: "/categories/lifestyle-personal/"
---

Pet and animal care MCP servers connect AI agents to tools for virtual pet interaction, wildlife species identification, bird observation data, livestock genetics, and pet adoption workflows. Instead of switching between pet care apps and wildlife databases, these servers let you manage animal-related tasks through natural language via the Model Context Protocol.

This review covers **pet and animal care** — virtual pets, wildlife identification, birding, livestock breeding, and pet adoption tools. For medical and health diagnostics, see our [Healthcare & Medical review](/reviews/healthcare-medical-mcp-servers/). For wearable fitness trackers, see our [Wearables & Quantified Self review](/reviews/fitness-wearables-mcp-servers/) if available.

The headline findings: **This category is growing beyond its fragmented roots** — the March–April 2026 period brought several meaningful additions. **The iNaturalist MCP** (9 tools) connects AI to one of the world's largest biodiversity databases — species search, taxonomy, conservation status, no API key required. **The rescuedogs-mcp-server** (8 tools, 70 commits) finally brings real pet adoption — 1,500+ dogs from 12+ European/UK rescue organizations with lifestyle matching. **The BirdNET-Pi MCP ecosystem** adds acoustic bird detection — sound-based species ID from Raspberry Pi microphones. **The NSIP sheep genetics client remains the most sophisticated** at 15 tools and 148 commits. **Virtual pets are charming but recreational.** **Practical pet ownership gaps are narrowing** — rescue dog adoption is now covered, but veterinary records, vaccination tracking, and breed identification remain absent.

---

## Virtual Pets

### shreyaskarnik/mcpet — Tamagotchi-Style Virtual Pet

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [mcpet](https://github.com/shreyaskarnik/mcpet) | 10 | TypeScript | — | 6 |

**A digital Tamagotchi powered by MCP** — adopt, nurture, and play with a virtual companion:

- **4 pet types** — Cat, Dog, Dragon, Alien — each with distinct personality
- **5 stat tracking** — Hunger, Happiness, Health, Energy, Cleanliness — stats decay over time even when you're away
- **Lifecycle stages** — pets grow from Baby to Adult based on care
- **6 care tools** — create_pet, feed_pet (Snack/Meal/Feast), play_with_pet (Ball/Chase/Puzzle), clean_pet, put_to_bed, check_pet
- **ASCII art animations** — dynamic visual feedback for different activities

A nostalgic concept demonstrating MCP fundamentals. Fun for experimentation, but purely recreational.

### stytchauth/chatagotchi — Interactive Pet in ChatGPT

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [chatagotchi](https://github.com/stytchauth/chatagotchi) | 11 | JavaScript | — | Multiple |

**An interactive virtual pet built with ChatGPT's Apps SDK:**

- **5 animal types** — Bird, Cat, Dog, Lizard, Fish
- **Pet care mechanics** — feed with different foods, play activities, monitor health
- **ChatGPT integration** — runs as a ChatGPT app rather than a standalone MCP server

Built by Stytch (the auth company) as a demo project. Shows how pet simulation can work within AI chat interfaces.

---

## Wildlife & Species Identification

### cvsouth/inaturalist-mcp — iNaturalist Biodiversity Data (NEW)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [inaturalist-mcp](https://github.com/cvsouth/inaturalist-mcp) | 3 | Python | MIT | 9 |

**The biggest addition to this category** — connects AI assistants to iNaturalist's massive biodiversity database (100M+ observations from citizen scientists worldwide):

- **9 MCP tools** — search_observations, get_species_counts, search_taxa, get_taxon, search_places, get_nearby_places, search_projects, get_similar_species, inaturalist_search
- **No API key required** — uses the public iNaturalist API (rate limited to 60 requests/minute)
- **Species search** — find any species by common or scientific name, get full taxonomy and conservation status
- **Location-based queries** — search observations by GPS coordinates, discover nearby places and biodiversity hotspots
- **Look-alike identification** — get_similar_species returns species commonly confused with a target species, invaluable for field identification
- **Community science** — search projects, bioblitzes, and regional surveys

iNaturalist (run by the California Academy of Sciences and National Geographic) is one of the world's largest citizen science platforms. This MCP server makes its entire public dataset conversationally accessible — a major upgrade for naturalists, educators, and conservation researchers. Created February 2026.

### fonkychen/nature-vision-mcp — Species ID from Images

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [nature-vision-mcp](https://github.com/fonkychen/nature-vision-mcp) | — | TypeScript | — | Multiple |

**Identifies biological species from photos using the Nature Vision API:**

- **Image-based identification** — submit a photo, get species identification with Latin names
- **Confidence scores** — returns probability ratings for each identification
- **Biological enrichment** — enables LLMs to recognize species and add biological context to responses
- **API key required** — connects to Nature Vision's external identification service

Practical for naturalists, educators, and citizen scientists. Requires a Nature Vision API key.

### wildlife-insights-mcp — Camera Trap Analytics & Conservation

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [wildlife-insights-mcp](https://lobehub.com/mcp/yourusername-wildlife-insights-mcp) | — | TypeScript | — | 12+ |

**Comprehensive MCP server for the Wildlife Insights GraphQL API:**

- **Data navigation** — getMyOrganizations, exploreMyData, getMyProjects
- **Species identification** — getIdentifyPhotosCount, submitIdentification, bulkIdentifyImages for camera trap photos
- **Analytics & insights** — getRanchManagementInsights, getSpeciesAnalytics, getProjectAnalytics
- **Upload management** — createUpload, uploadImageWorkflow, completeUpload
- **Texas ranch optimization** — specifically tuned for Texas wildlife management with native game species

The most feature-rich server in this category. Requires Wildlife Insights API credentials (WI_GRAPHQL_ENDPOINT, WI_BEARER_TOKEN).

---

## Birding & Ornithology

### moonbirdai/ebird-mcp-server — eBird Observation Data

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [ebird-mcp-server](https://github.com/moonbirdai/ebird-mcp-server) | 6 | TypeScript | — | 5+ |

**Connects AI assistants to eBird's massive bird observation database:**

- **Recent observations** — get bird sightings in any region or near any location
- **Species-specific search** — find recent observations of a particular bird species
- **Notable sightings** — discover rare or unusual bird observations in an area
- **Birding hotspots** — find popular birdwatching locations by region or coordinates
- **Taxonomy data** — access eBird's comprehensive bird taxonomy

eBird (run by the Cornell Lab of Ornithology) has over 100 million bird observations from citizen scientists worldwide. This MCP server makes that data conversationally accessible. Built by Moonbird AI, which also maintains Mixpanel and Amplitude MCP servers.

### siansiansu/ebird-mcp-server — eBird (Python Alternative)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [ebird-mcp-server](https://github.com/siansiansu/ebird-mcp-server) | 5 | Python | MIT | Multiple |

**A Python implementation of the eBird MCP server** — provides the same core functionality (observations, hotspots, taxonomy, checklists) in Python rather than TypeScript. Includes contributor rankings and statistics. A solid alternative for Python-centric environments.

### DMontgomery40/mcp-local-server — BirdNET-Pi Acoustic Detection (NEW)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [mcp-local-server](https://github.com/DMontgomery40/mcp-local-server) | 3 | Python | MIT | 5 |

**A fundamentally different approach to birding — identifying birds by sound rather than sight:**

- **5 MCP tools** — get_detections, get_stats, get_audio, get_activity, generate_report
- **BirdNET-Pi integration** — queries bird detection data from a local BirdNET-Pi installation (Raspberry Pi with USB microphone running the Cornell Lab's BirdNET AI)
- **Audio recording access** — retrieve the actual sound recordings (base64 or buffer) associated with detections
- **Activity patterns** — hourly bird activity breakdowns showing when species are most active
- **Report generation** — detection reports in JSON or HTML formats
- **Dual transport** — stdio and streamable HTTP

BirdNET (developed by the Cornell Lab of Ornithology and Chemnitz University) can identify 6,000+ bird species by sound. This MCP server makes your local BirdNET-Pi installation conversationally queryable — "What birds were singing in my yard this morning?" Requires a running BirdNET-Pi setup.

### DMontgomery40/mcp-server-birdstats — BirdWeather + eBird Analysis (NEW)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [mcp-server-birdstats](https://github.com/dmontgomery40/mcp-server-birdstats) | 1 | JavaScript | MIT | 3 |

**Combines BirdWeather and eBird data for cross-platform bird analysis:**

- **3 read-only tools** — get_system_prompt, get_birdweather_api, get_ebird_api
- **Analysis prompt** — check-bird prompt for combined species analysis
- **Token-efficient** — defaults to summary mode, full payload requires explicit opt-in
- **Docker support** — containerized deployment available

Complements the BirdNET-Pi server by adding BirdWeather station data alongside eBird observations. Created by the same developer (DMontgomery40) as part of a comprehensive birding MCP ecosystem.

---

## Livestock & Breeding

### epicpast/nsip-api-client — Sheep Genetics & Breeding Support

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [nsip-api-client](https://github.com/epicpast/nsip-api-client) | 1 | Python | — | 15 |

**The most sophisticated server in this category** — a Python client for the National Sheep Improvement Program with a full MCP server:

- **15 MCP tools** — 10 NSIP API tools + 5 Shepherd consultation tools
- **Genetic evaluation** — search animals, compare Expected Breeding Values (EBVs)
- **Mating planning** — plan matings based on genetic data
- **Flock ranking** — rank flocks by performance metrics
- **Context management** — automatic response summarization to prevent LLM context overflow
- **Smart caching** — intelligent caching of large datasets

Automates complex breeding calculations that would otherwise require specialized spreadsheet work. Extremely niche but genuinely valuable for sheep breeders using NSIP data. With 148 commits and 2 forks, this remains the most actively developed server in the category.

---

## Pet Store & Adoption

### ssatama/rescuedogs-mcp-server — European Rescue Dog Adoption (NEW)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [rescuedogs-mcp-server](https://github.com/ssatama/rescuedogs-mcp-server) | 0 | TypeScript | MIT | 8 |

**The first real pet adoption MCP server** — searches across vetted European and UK rescue organizations with genuine adoption data:

- **8 MCP tools** — rescuedogs_search_dogs, rescuedogs_get_dog_details, rescuedogs_list_breeds, rescuedogs_get_statistics, rescuedogs_get_filter_counts, rescuedogs_list_organizations, rescuedogs_match_preferences, rescuedogs_get_adoption_guide
- **1,500+ available dogs** from 12+ rescue organizations across 370+ breeds
- **Comprehensive filtering** — breed, size, age, energy level, experience requirements, location
- **Lifestyle matching** — rescuedogs_match_preferences recommends dogs based on your lifestyle and preferences
- **AI personality assessments** — individual dog profiles include AI-generated personality descriptions
- **Country-specific adoption guides** — step-by-step adoption process information by country
- **Powered by rescue-dog-aggregator** — open-source data aggregation from vetted organizations

This is a significant milestone for the category — the first MCP server connected to real rescue dog data rather than demo APIs. With 70 commits, it's actively developed and fills the biggest gap identified in previous reviews. Currently focused on European/UK organizations.

### raghavendraprakash/mcpforrestapis — Petstore API MCP Wrapper

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [mcpforrestapis](https://github.com/raghavendraprakash/mcpforrestapis) | — | Python | Apache 2.0 | Multiple |

**MCP server wrapping the classic Swagger Petstore API:**

- **Find pets** — search available pets by status (available, pending, sold)
- **Add pets** — create new pet entries with photo URLs
- **Inventory management** — retrieve store inventory
- **MCP client included** — ships with both server and client for testing

Primarily a reference implementation showing how to wrap REST APIs with MCP. Uses the Swagger Petstore demo API — not connected to real pet stores.

### zeeroiq/pet-adoption-scheduler — Adoption Appointment Booking

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| pet-adoption-scheduler | — | Python | — | Multiple |

**Schedules pet adoption appointments through conversational AI:**

- **Natural language search** — "Are there any young, friendly labradors available near me?"
- **Appointment scheduling** — book visits to shelters through chat
- **Shelter discovery** — find rescue organizations in your area

An educational/demo project showing how MCP could streamline adoption workflows. Not connected to real shelter databases.

---

## Nutrition (Tangential)

While not pet-specific, these nutrition MCP servers could support animal dietary planning:

### deadletterq/mcp-opennutrition — 300K+ Food Database

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [mcp-opennutrition](https://github.com/deadletterq/mcp-opennutrition) | — | TypeScript | — | Multiple |

**Comprehensive local food database** — 300,000+ food items with nutritional data and barcode lookups. Runs entirely locally with no external API calls.

### MCP-Forge/nutritionix-mcp-server — Nutritionix API

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [nutritionix-mcp-server](https://github.com/MCP-Forge/nutritionix-mcp-server) | — | TypeScript | — | Multiple |

**Nutritionix API integration** — food search, nutrition data, and exercise calorie estimates via natural language input.

---

## What's Missing

Some gaps from our March 2026 review are now filled, but significant ones remain:

- **~~No pet adoption integration~~** — **FILLED** by rescuedogs-mcp-server (European/UK rescue dogs). However, Petfinder and Adopt-a-Pet (the two largest US databases) still have no MCP servers
- **No veterinary clinic management** — no appointment booking, medical records, or prescription tracking
- **No pet health records** — no vaccination tracking, deworming schedules, or medical history
- **No dog training or behavior tools** — no training plan generators, behavior analysis, or socialization guides
- **No breed identification** — no image-based breed recognition for dogs or cats
- **No pet GPS tracking** — no Fi, Whistle, or AirTag integration
- **No aquarium or marine management** — despite projects like reef-pi existing in the IoT space
- **No cat/dog food recall monitoring** — no FDA recall database integration
- **No livestock beyond sheep** — nothing for cattle, poultry, swine, dairy, or general farm management
- **No AKC/CKC/FCI registry access** — no breed registry or pedigree data
- **No pet insurance integration** — no claims, coverage, or provider comparison tools
- **No cat adoption** — rescuedogs covers dogs only; cats, small animals, and exotic pets remain unserved

---

## The Bottom Line

The pet and animal care MCP space is **growing and diversifying**. The category now splits into four tiers:

**Genuinely useful (broad audience):** The iNaturalist MCP (9 tools, 100M+ observations, no API key) makes the world's largest biodiversity database conversationally accessible. The rescuedogs-mcp-server (8 tools, 1,500+ real dogs) is the first practical pet adoption tool with genuine data. The BirdNET-Pi MCP brings acoustic bird identification — a fundamentally different approach to birding.

**Genuinely useful (narrow audience):** The NSIP sheep genetics client (15 tools, 148 commits, breeding decision support) and Wildlife Insights MCP (camera trap analytics, species identification) serve real professional needs. The eBird servers (two implementations — TypeScript and Python) tap into a massive citizen science dataset.

**Fun but recreational:** MCPet (10 stars) and Chatagotchi (11 stars) are charming Tamagotchi-style experiments that demonstrate MCP concepts through virtual pet care. Good for learning MCP, not for managing real animals.

**Demo/reference projects:** The Petstore API wrapper and pet adoption scheduler are educational implementations, not production tools.

The category earns **3 out of 5** (up from 2.5). The iNaturalist MCP server is a game-changer for naturalists — 9 tools accessing 100M+ biodiversity observations with no API key. The rescuedogs-mcp-server finally fills the most glaring gap (real pet adoption data). The BirdNET ecosystem adds sound-based species identification. But the enormous practical pet care market (veterinary records, health tracking, breed ID, GPS monitoring) remains largely unserved. Someone building a Petfinder MCP server, a vet records manager, or a cat adoption tool would still face zero competition.

*This review was last updated on 2026-04-30 using Claude Opus 4.6 (Anthropic).*
