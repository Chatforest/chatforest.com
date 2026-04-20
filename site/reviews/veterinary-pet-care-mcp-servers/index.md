# Veterinary & Pet Care MCP Servers — Animal Health, Livestock Genetics, Pet Management, and More

> Veterinary and pet care MCP servers let AI agents work with animal health data, livestock genetics, pet management, and species databases.


Veterinary and pet care MCP servers would let AI agents access animal health records, manage livestock genetics, search species databases, track pet vaccinations, and integrate with veterinary practice management systems. The operative word is "would" — this ecosystem barely exists yet.

This review covers the **veterinary and pet care** vertical — animal health, livestock genetics, pet management, species databases, and agricultural data tangentially related to animals. For human healthcare, see our [Healthcare & Medical MCP review](/reviews/healthcare-medical-mcp-servers/). For agriculture broadly, see our [Agriculture & Farming MCP review](/reviews/agriculture-farming-mcp-servers/).

The headline finding: **this is one of the thinnest MCP ecosystems we've reviewed.** Out of thousands of MCP servers cataloged across the ecosystem, we found exactly one server with genuine veterinary/agricultural utility — a sheep genetic evaluation tool. Everything else is either a toy project or tangentially related. No major veterinary software company (IDEXX, Covetrus, Vetspire, ezyVet, PetDesk) has adopted MCP.

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

## Pet Simulation (Toy Projects)

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

### Fish MCP Server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [cozy-corner/fish-mcp-server](https://github.com/cozy-corner/fish-mcp-server) | 0 | TypeScript | ISC | 2 |

Searches **35,700+ fish species** from the FishBase database:

- **Search by name** — common or scientific names in English and Japanese
- **Search by features** — physical characteristics, habitat, behavior

Uses SQLite FTS5 for fast local full-text search. Useful for aquarium hobbyists, marine biologists, or anyone who needs to quickly identify or look up fish species. The data is comprehensive — FishBase is the world's largest fish database.

## Agricultural Data (Tangentially Related)

### AgroBR MCP

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [bruno-portfolio/agrobr-mcp](https://github.com/bruno-portfolio/agrobr-mcp) | 21 | Python | MIT | 10 |

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

**Animal shelter and rescue** — No integration with Petfinder, Adopt-a-Pet, or shelter management systems. No adoption matching or animal welfare databases.

**Veterinary diagnostics** — No integration with IDEXX Reference Labs, Antech, or other diagnostic services. Lab results are a core part of veterinary workflow, and none of it is accessible via MCP.

**Pet insurance** — No integration with Trupanion, Nationwide Pet, Embrace, or other pet insurers. Claims, coverage lookups, and policy management are all absent.

**Wildlife and conservation** — No wildlife tracking, endangered species databases, or conservation data accessible through MCP.

**Equine management** — Horse health, training, breeding, and competition records — nothing exists.

**Pet nutrition** — No pet food ingredient databases, dietary recommendation engines, or recall tracking.

**Veterinary telemedicine** — No telehealth platform integration for remote veterinary consultations.

## The bottom line

**Rating: 2.5/5** — The veterinary and pet care MCP ecosystem is almost nonexistent. The NSIP sheep genetics server is a genuinely useful tool for its narrow audience, and the FishBase server fills a real data gap, but that's essentially the entire ecosystem. Everything else is a virtual pet toy or tangentially related agricultural data.

This represents one of the **largest untapped opportunities** in the MCP landscape. Veterinary practices generate enormous amounts of structured data — patient records, lab results, prescriptions, vaccination schedules, billing — that AI agents could meaningfully process. Pet owners manage vaccinations, feeding schedules, medications, and health histories that would benefit from AI assistance. Livestock operations deal with genetics, nutrition, health monitoring, and regulatory compliance data at scale.

The reason for the gap is likely structural: veterinary software is a smaller, more fragmented market than human healthcare, with less venture funding and fewer developer-focused companies. The IDEXX/Covetrus duopoly in vet diagnostics hasn't shown interest in open AI integrations. Pet-tech startups are focused on consumer apps rather than developer tools.

If you're building in this space, the opportunity is wide open. A veterinary practice management MCP server that connects to even one major platform would instantly become the most important tool in this category.

| Subcategory | Best option | Stars | Tools | Verdict |
|------------|-------------|-------|-------|---------|
| Livestock genetics | [epicpast/nsip-api-client](https://github.com/epicpast/nsip-api-client) | 1 | 15 | Only serious tool — sheep EBVs and mating plans |
| Pet simulation | [shreyaskarnik/mcpet](https://github.com/shreyaskarnik/mcpet) | 10 | 6 | Fun toy, not veterinary software |
| Species data | [cozy-corner/fish-mcp-server](https://github.com/cozy-corner/fish-mcp-server) | 0 | 2 | 35,700+ fish species from FishBase |
| Agricultural data | [bruno-portfolio/agrobr-mcp](https://github.com/bruno-portfolio/agrobr-mcp) | 21 | 10 | Brazilian ag data, tangentially relevant |
| Pet business | Time To Pet (Zapier) | — | 5 triggers | Notification triggers only |

*This review was last edited on 2026-03-16 using Claude Opus 4.6 (Anthropic).*

