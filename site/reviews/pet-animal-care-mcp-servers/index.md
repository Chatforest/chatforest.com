# Pet & Animal Care MCP Servers — Virtual Pets, Wildlife ID, Birding, Livestock Genetics, and Pet Adoption

> Pet and animal care MCP servers let AI agents interact with virtual pets, identify wildlife species, access bird observation data, manage livestock genetics, and explore pet


Pet and animal care MCP servers connect AI agents to tools for virtual pet interaction, wildlife species identification, bird observation data, livestock genetics, and pet adoption workflows. Instead of switching between pet care apps and wildlife databases, these servers let you manage animal-related tasks through natural language via the Model Context Protocol.

This review covers **pet and animal care** — virtual pets, wildlife identification, birding, livestock breeding, and pet adoption tools. For medical and health diagnostics, see our [Healthcare & Medical review](/reviews/healthcare-medical-mcp-servers/). For wearable fitness trackers, see our [Wearables & Quantified Self review](/reviews/fitness-wearables-mcp-servers/) if available.

The headline findings: **This is an extremely fragmented category** — servers span virtual pets, wildlife conservation, birding, and sheep genetics with no connecting ecosystem. **The NSIP sheep genetics client is the most sophisticated** with 15 MCP tools for breeding decisions. **Wildlife Insights provides real conservation value** with camera trap photo ID and species analytics. **Virtual pets are charming but recreational.** **Practical pet ownership tools are almost entirely absent** — no vet records, no vaccination tracking, no Petfinder integration.

---

## Virtual Pets

### shreyaskarnik/mcpet — Tamagotchi-Style Virtual Pet

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [mcpet](https://github.com/shreyaskarnik/mcpet) | — | TypeScript | — | 6 |

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
| [chatagotchi](https://github.com/stytchauth/chatagotchi) | — | JavaScript | — | Multiple |

**An interactive virtual pet built with ChatGPT's Apps SDK:**

- **5 animal types** — Bird, Cat, Dog, Lizard, Fish
- **Pet care mechanics** — feed with different foods, play activities, monitor health
- **ChatGPT integration** — runs as a ChatGPT app rather than a standalone MCP server

Built by Stytch (the auth company) as a demo project. Shows how pet simulation can work within AI chat interfaces.

---

## Wildlife & Species Identification

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
| [ebird-mcp-server](https://github.com/moonbirdai/ebird-mcp-server) | — | TypeScript | — | 5+ |

**Connects AI assistants to eBird's massive bird observation database:**

- **Recent observations** — get bird sightings in any region or near any location
- **Species-specific search** — find recent observations of a particular bird species
- **Notable sightings** — discover rare or unusual bird observations in an area
- **Birding hotspots** — find popular birdwatching locations by region or coordinates
- **Taxonomy data** — access eBird's comprehensive bird taxonomy

eBird (run by the Cornell Lab of Ornithology) has over 100 million bird observations from citizen scientists worldwide. This MCP server makes that data conversationally accessible. Built by Moonbird AI, which also maintains Mixpanel and Amplitude MCP servers.

---

## Livestock & Breeding

### epicpast/nsip-api-client — Sheep Genetics & Breeding Support

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [nsip-api-client](https://github.com/epicpast/nsip-api-client) | — | Python | — | 15 |

**The most sophisticated server in this category** — a Python client for the National Sheep Improvement Program with a full MCP server:

- **15 MCP tools** — 10 NSIP API tools + 5 Shepherd consultation tools
- **Genetic evaluation** — search animals, compare Expected Breeding Values (EBVs)
- **Mating planning** — plan matings based on genetic data
- **Flock ranking** — rank flocks by performance metrics
- **Context management** — automatic response summarization to prevent LLM context overflow
- **Smart caching** — intelligent caching of large datasets

Automates complex breeding calculations that would otherwise require specialized spreadsheet work. Extremely niche but genuinely valuable for sheep breeders using NSIP data.

---

## Pet Store & Adoption

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

The gaps in this category are striking — especially given the size of the pet industry ($150B+ annually in the US alone):

- **No Petfinder or Adopt-a-Pet API integration** — the two largest pet adoption databases have no MCP servers
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

---

## The Bottom Line

The pet and animal care MCP space is **extremely early and fragmented**. The category splits into three tiers:

**Genuinely useful (narrow audience):** The NSIP sheep genetics client (15 tools, breeding decision support) and Wildlife Insights MCP (camera trap analytics, species identification) serve real professional needs. The eBird server taps into a massive citizen science dataset.

**Fun but recreational:** MCPet and Chatagotchi are charming Tamagotchi-style experiments that demonstrate MCP concepts through virtual pet care. Good for learning MCP, not for managing real animals.

**Demo/reference projects:** The Petstore API wrapper and pet adoption scheduler are educational implementations, not production tools.

The category earns **2.5 out of 5**. There's genuine innovation in wildlife conservation and livestock genetics, but the enormous practical pet care market is almost entirely unserved. Someone building a Petfinder MCP server, a vet records manager, or a pet health tracker would be addressing real demand with zero competition in the MCP ecosystem.

*This review was last edited on 2026-03-16 using Claude Opus 4.6 (Anthropic).*

