# Real Estate & Property MCP Servers — Zillow, MLS, Airbnb, BatchData, Mortgage Analysis, and More

> Real estate and property MCP servers are bringing property search, valuation, and market analysis into AI workflows. We reviewed 35+ servers across 7 subcategories.


Real estate MCP servers are connecting AI assistants to property data, market analytics, and transaction workflows. Instead of manually searching Zillow, pulling MLS comps, or running mortgage calculators, these servers let AI agents search listings, retrieve valuations, parse mortgage documents, and analyze investment opportunities — all through the Model Context Protocol.

The landscape spans seven areas: **property search & listings** (Airbnb, Zillow, portal ChatGPT apps), **property data & valuation** (ATTOM, Cotality, PriceHubble, BatchData), **real estate CRM & management** (agent tools, deal pipelines, property management), **MLS & industry standards** (RESO-based servers), **mortgage & investment analysis** (document parsing, financial calculators), **regional market servers** (country-specific property data), and **enterprise property intelligence** (multi-country valuation platforms).

The headline findings: **Airbnb dominates by star count** — openbnb-org/mcp-server-airbnb (437 stars, v0.2.0) is the most popular real estate MCP server by a wide margin, though it only covers vacation rentals. **All three major U.S. portals now have ChatGPT MCP apps** — Zillow (October 2025), Redfin (February 2026), and Realtor.com (March 2026) all launched apps inside ChatGPT built on OpenAI's Apps SDK, which uses MCP. These are ChatGPT-exclusive integrations, not open MCP servers, but they signal that the industry's largest platforms are engaging with MCP as infrastructure. **Enterprise property data is MCP-native** — Cotality (formerly CoreLogic) launched its MCP server in March 2026, joining ATTOM (January 2026) as the second major U.S. property data provider with MCP support, and a community server (nkbud/mcp-server-attom) now exposes 55+ ATTOM API endpoints as open-source MCP tools. **PriceHubble launched 4 enterprise MCPs** — the property intelligence platform's MCP suite (Listings, Transactions, Market Trends, Valuation) covers 11 countries with ISO 27001/GDPR compliance, making it the first proptech platform with multi-country MCP support. **Property management enters the ecosystem** — CryptoCultCurt/appfolio-mcp-server brings AppFolio's Reporting API to MCP, filling the rental/property management gap. **The MLS industry is paying attention** — David Gumpper's UNLOCK MLS RESO Reference server represents the first standards-based MLS data access via MCP, built on Bridge Interactive's RESO Web API. **Mortgage document parsing exists** — confersolutions/mcp-mortgage-server converts Loan Estimates and Closing Disclosures into MISMO-compliant JSON. **Regional diversity is remarkable** — servers exist for Korean, Australian, Swedish, French, Spanish, Philippine, and Russian property markets. **Commercial real estate is stirring** — PriceHubble's entry provides CRE-adjacent valuation data, but dedicated CoStar, LoopNet, or CREXi MCP servers still don't exist.

**Category:** [Finance & Fintech](/categories/finance-fintech/)

## Property Search & Listings

### mcp-server-airbnb (openbnb-org)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [openbnb-org/mcp-server-airbnb](https://github.com/openbnb-org/mcp-server-airbnb) | 437 | JavaScript | MIT | 2 |

The **most popular real estate MCP server** by far, with over 430 stars. Provides two focused tools:

- **airbnb_search** — location-based property search with filtering by dates, guest count, price range, and amenities, plus Google Maps Place ID integration for precise location targeting
- **airbnb_listing_details** — comprehensive property information including amenities, policies, and neighborhood details

Packaged as a Desktop Extension (DXT) for easy installation with Claude Desktop and other compatible clients. Version 0.2.0 (April 2026) shows continued active development. The narrow 2-tool design is intentional — search and detail retrieval cover the primary vacation rental use case cleanly.

### zillow-mcp-server (sap156)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [sap156/zillow-mcp-server](https://github.com/sap156/zillow-mcp-server) | 37 | Python | MIT | 7 |

The leading community-built Zillow integration, connecting to **Zillow's Bridge API** for real-time property data. Seven tools cover the core residential real estate workflow:

- **search_properties** — find listings with various search criteria
- **get_property_details** — comprehensive property information
- **get_zestimate** — Zillow's proprietary automated valuation model
- **get_market_trends** — area-level market analytics
- **calculate_mortgage** — payment estimation with principal, interest, taxes, and insurance
- **check_health** — API connectivity verification
- **get_server_tools** — tool discovery

Built with FastMCP and includes exponential retry logic via the backoff library. Requires a Bridge API key (from api@bridgeinteractive.com), which is a barrier for casual users. Multiple other Zillow MCP servers exist on Glama and PulseMCP (BACH-AI-Tools/zillow56, rohitsingh-iitd/zillow-mcp-server), but sap156's has the most stars and the most complete tool set.

### Repliers MCP Server (Repliers-io)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [Repliers-io/mcp-server](https://github.com/Repliers-io/mcp-server) | 16 | JavaScript | MIT | 8 |

The closest thing to **real MLS listing data** via MCP, providing access to the Repliers API for Canadian real estate data:

- **search** — advanced property search with filters
- **get-a-listing** — individual listing details
- **find-similar-listings** — comparable property discovery
- **get-address-history** — transaction history for an address
- **property-types-styles** — available property classifications
- **get-deleted-listings** — track removed listings
- **areas-cities-and-neighborhoods** — geographic boundary data
- **buildings** — building-level information for condos/apartments

The similar listings and address history tools are particularly valuable for real estate agents doing comparative market analysis (CMA). Requires a Repliers API key.

### HomeHarvest MCP (ZacharyHampton)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [ZacharyHampton/HomeHarvest](https://github.com/ZacharyHampton/HomeHarvest) | — | Python | — | — |

HomeHarvest is primarily a **real estate scraping library** (extracting data from Realtor.com, Zillow, and Redfin) that has added an MCP server interface. The library formats scraped data in MLS-style listing format. The MCP integration enables AI agents to pull property data directly, though the scraping approach raises questions about terms-of-service compliance compared to official API-based servers.

### Other Airbnb Servers

Multiple alternative Airbnb MCP servers exist: **vedantparmar12/airbnb-mcp** adds LiveKit voice interaction for natural language property search, **Domoteek/mcp-server-airbnb** provides a French-language alternative, and **josuebatista/mcp-agent** combines MCP with Claude for listing data processing. The openbnb-org server's 437 stars dwarfs all alternatives.

### Portal ChatGPT Apps (Zillow, Redfin, Realtor.com)

A major development since the original review: **all three major U.S. consumer real estate portals** now have apps inside ChatGPT, built on OpenAI's Apps SDK which uses the Model Context Protocol:

- **Zillow** — launched October 2025 as one of OpenAI's pilot partners. Users can browse listings on an interactive map inside ChatGPT, with the AI interpreting intent and dynamically querying Zillow's data.
- **Redfin** — launched February 6, 2026. Surfaces listings and allows conversational home search with neighborhood info and market trends. Redfin is owned by Rocket Companies.
- **Realtor.com** — launched March 30, 2026. Includes safeguards: listing previews only (not full data), MLS data training strictly prohibited, agents remain central to the workflow.

**Important caveat:** These are ChatGPT-exclusive integrations, not open MCP servers that any client can connect to. You can't point Claude Desktop or a custom agent at Zillow's MCP endpoint. But they represent the first time major real estate platforms have engaged with MCP as infrastructure for AI data access, and they signal where the industry is heading.

## Property Data & Valuation

### batchdata-mcp-real-estate (zellerhaus)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [zellerhaus/batchdata-mcp-real-estate](https://github.com/zellerhaus/batchdata-mcp-real-estate) | 27 | TypeScript | MIT | 8 |

Integrates with **BatchData.io's property and address APIs** across two tool categories:

Address operations (4 tools):
- **verify** — USPS address verification
- **autocomplete** — address suggestions
- **geocode** — address to lat/lng conversion
- **reverse-geocode** — lat/lng to address lookup

Property operations (4 tools):
- **lookup** — property details by address or APN (Assessor Parcel Number)
- **search** — advanced filtered property searches
- **boundary search** — geographic boundary queries
- **count** — match counting for search criteria

Supports installation via Smithery, npm, or Docker with multi-stage builds and health checks. Rate limits vary by endpoint (5,000 max for address verification, 90 for geocoding, 1,000 for property search). The APN-based lookup is notable — it's the identifier system that county assessors and title companies actually use.

### Property Valuation Server (creis-ai)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [creis-ai/mcp-property-valuation-server](https://github.com/creis-ai/mcp-property-valuation-server) | 3 | JavaScript | MIT | 3 |

A specialized server for **Chinese real estate market** valuation:

- **get_community_rating** — multidimensional community assessment based on activity levels, property management quality, educational resources, and location factors
- **get_community_valuation** — area-level price analysis
- **get_property_valuation** — individual property value estimation

Designed for real estate transactions, investment due diligence, and mortgage collateral evaluation in the Chinese market. The 46 commits suggest ongoing development despite low star count.

### Property MCP Server (noahw345)

Connects Claude to the **ATTOM Data API** for US property analysis. ATTOM aggregates data from county assessors, recorders, and other public records across 155M+ US properties. Less well-documented than BatchData but accesses a different (and in some cases more comprehensive) underlying dataset.

### Cotality MCP Server (Enterprise)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [Cotality MCP](https://www.cotality.com/platforms/mcp-server) | — | — | Commercial | Multiple |

**The largest property data company enters the MCP ecosystem.** Cotality (formerly CoreLogic) launched its MCP server on March 31, 2026, providing a universal connector between AI models and its property intelligence platform:

- **CLIP ID access** — Cotality's unique property identifiers for unambiguous cross-system property matching across the entire U.S. housing stock
- **Property details** — comprehensive property attributes, characteristics, and ownership data
- **Climate risk assessments** — property-level climate and hazard risk scoring
- **Market trends** — real-time market intelligence for valuation and analysis workflows

Cotality also launched **AI-Ready Data** — structured data assets designed for AI model consumption, providing semantic enrichment beyond raw values. The MCP server supports ChatGPT, Claude, Gemini, and other MCP-compatible clients. Enterprise authentication required.

**Why it matters:** Cotality serves most major U.S. lenders, servicers, and insurers. For organizations already in the Cotality ecosystem, this is the most production-ready path to AI-powered property intelligence. Combined with ATTOM's MCP server (January 2026), the two largest U.S. property data providers now both support MCP.

### ATTOM Community MCP Server (nkbud)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [nkbud/mcp-server-attom](https://github.com/nkbud/mcp-server-attom) | 2 | Python | MIT | 55+ |

The first **open-source community implementation** of the ATTOM Data API as MCP tools. Acts as middleware exposing 55+ ATTOM API endpoints across 10 categories:

- **Property** (14 endpoints) — address lookup, property details, profiles, building permits, sales history
- **Assessment** (3 endpoints) — tax assessment data
- **Sale** (6 endpoints) — transaction records and comparables
- **Valuation** — automated valuation models (AVMs)
- **Geographic** — boundary data, neighborhood demographics
- **Schools** — school district and rating information
- **Community** — local amenities and quality-of-life metrics

Supports querying by property ID, address, coordinates, or parcel number (APN). Requires an ATTOM API key. A second community implementation exists at jmclaughlin724/attom-mcp-server (TypeScript, MIT) with a unified `attom_query` tool and smart fallback strategies, though it has fewer stars.

### PriceHubble MCP Suite (Enterprise)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [PriceHubble MCP](https://www.pricehubble.com/pricehubble-news/pricehubble-launches-model-context-protocol) | — | — | Commercial | 4 MCPs |

**The first proptech platform with multi-country enterprise MCP support.** PriceHubble, an AI-driven property intelligence platform serving banks, investors, and real estate professionals, launched its MCP suite in December 2025 with enterprise beta in Q1 2026:

- **Listings MCP** — active listings with attributes, price history, and days on market
- **Transactions MCP** — historical transaction records and comparable sales data across 11 countries
- **Market Trends MCP** — local pricing dynamics, supply indicators, and market evolution metrics
- **Valuation MCP** — direct access to PriceHubble's automated valuation outputs

Compliance-first design with ISO 27001, GDPR, and NIST AI Risk Management Framework adherence. Already deployed internally in PriceHubble's AI Companion and AI Copilot products. The 11-country coverage makes this the broadest geographic reach of any single real estate MCP implementation.

**Why it matters:** PriceHubble sits at the intersection of residential and commercial real estate, serving property professionals, mortgage lenders, and institutional investors. Its MCP suite is the first to provide governed, multi-country property intelligence to AI agents — a significant step beyond the U.S.-focused ATTOM and Cotality offerings.

## Real Estate CRM & Management

### real-estate-mcp (agentic-ops)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [agentic-ops/real-estate-mcp](https://github.com/agentic-ops/real-estate-mcp) | 26 | Python | — | 30+ |

The **most comprehensive general-purpose real estate MCP server**, with 30+ tools across six categories:

- **Property Management** (7 tools) — listing CRUD, search, filtering
- **Agent Operations** (6 tools) — agent performance tracking, assignment management
- **Market Analysis** (7 tools) — pricing trends, comparative market analysis, demand indicators
- **Client Management** (3 tools) — buyer/seller relationship tracking
- **Area Intelligence** (9 tools) — neighborhood data, school ratings, demographics, commute analysis
- **System Management** (2 tools) — health checks, configuration

Also provides 10 resources (5 static + 5 dynamic templates), 11 prompts across 4 categories, and SSE transport support. This is a demo/showcase project that has been incorporated into several related real estate projects for renting, buying, and consulting workflows.

### propstack-mcp (ashev87)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [ashev87/propstack-mcp](https://github.com/ashev87/propstack-mcp) | 1 | TypeScript | MIT | 50 |

Integrates with **Propstack**, a real estate CRM platform used primarily in Europe, providing the **highest tool count** of any real estate MCP server:

- Contact management with GDPR tracking
- Property filtering by multiple criteria
- Deal pipeline management
- Viewing/showing scheduling
- Natural language buyer matching ("3-room apartment in Berlin under 400k with balcony")
- Email templating and task logging
- Pipeline dashboards and lead intake workflows

50 tools across 12 categories. Created February 2026, suggesting active development. Despite the low star count, the tool depth and CRM integration patterns are notable — this is what a production real estate agent workflow looks like.

### appfolio-mcp-server (CryptoCultCurt)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [CryptoCultCurt/appfolio-mcp-server](https://github.com/CryptoCultCurt/appfolio-mcp-server) | 6 | TypeScript | ISC | Multiple |

The first MCP server for **property management software**, connecting AI agents to AppFolio's Property Manager Reporting API. AppFolio is one of the largest property management platforms in the U.S., serving residential, commercial, and community association managers.

Available via Smithery (`npx -y @smithery/cli install @CryptoCultCurt/appfolio-mcp-server --client claude`) and npm. Includes OAuth refresh configuration and session management features. While the tool count isn't well-documented, the server bridges the gap between property management operations and AI workflows — a category that was completely unserved until this server appeared.

**Why it matters:** This is the first MCP server for any major property management platform. AppFolio, Buildium, Yardi, and RentManager are the dominant platforms in this space — having even one with MCP support opens the door for AI-assisted portfolio reporting, maintenance tracking, and tenant management.

### Other CRM & Management Servers

**Inmovilla MCP Server** (laica-ayudavets) manages properties, clients, and owners via the Inmovilla CRM platform (Spanish market). **DanielJandric/realestatemcp** is a property intelligence platform (Python, proprietary) with 7 MCP tools enabling semantic search across 31,600+ document chunks, covering 653+ documents for 8 properties and 463 units — useful for AI-driven property portfolio analysis with Supabase/pgvector. Real estate CRM is an area ripe for growth — major platforms like Follow Up Boss, kvCORE, Sierra Interactive, and Wise Agent have no MCP servers yet.

## MLS & Industry Standards

### UNLOCK MLS RESO Reference MCP Server (GumpperGroup)

The most significant development in real estate MCP is the emergence of **standards-based MLS access**. David Gumpper (WAV Group partner, former CTO of Michael Saunders & Company) built this reference implementation using **UNLOCK MLS** data through **Bridge Interactive's RESO Web API**.

This matters because:
- **RESO (Real Estate Standards Organization)** standardized MLS listing data across MLSs — MCP is now standardizing how AI interacts with that data
- The server provides governed access with **full audit trails and compliance monitoring** — critical for an industry with strict data licensing rules
- It's positioned as a next-generation alternative to IDX feeds, but built for AI rather than websites
- WAV Group has published extensively about MLS MCP servers, signaling industry buy-in at the consulting/strategy level

The real estate industry's relationship with data access has always been complex (IDX, RETS, now RESO Web API). MCP servers that respect MLS data licensing while enabling AI workflows will be essential for mainstream adoption.

## Mortgage & Investment Analysis

### mcp-mortgage-server (confersolutions)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [confersolutions/mcp-mortgage-server](https://github.com/confersolutions/mcp-mortgage-server) | 2 | Python | MIT | 4 |

A specialized server for **AI-driven mortgage document analysis**:

- **parse_loan_estimate** — extract structured data from Loan Estimate PDFs
- **parse_closing_disclosure** — parse Closing Disclosure documents
- **compare_le_cd** — detect discrepancies between LE and CD for TRID compliance
- **hello** — connectivity test

Converts residential loan paperwork into **MISMO-compliant JSON** (MISMO is the mortgage industry data standard). The TRID compliance violation detection is particularly valuable — the TILA-RESPA Integrated Disclosure rule governs what lenders must disclose and when, and violations can result in significant penalties.

Built with Pydantic validation, HTTPS enforcement, domain whitelisting, and SSRF prevention. The v2.0.0 release (November 2025) was a major rewrite from REST API to MCP. Despite only 2 stars, this fills a genuine industry need.

### RealVest MCP Server (sigaihealth)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [sigaihealth/realvestmcp](https://github.com/sigaihealth/realvestmcp) | — | JavaScript | MIT | 31 |

**31 professional real estate investment calculators** via MCP, covering:

- **calculate_affordability** — how much house can you afford
- **analyze_brrrr_deal** — Buy, Rehab, Rent, Refinance, Repeat analysis
- **evaluate_house_hack** — owner-occupied investment evaluation
- **project_portfolio_growth** — multi-property portfolio modeling
- **analyze_syndication** — real estate syndication evaluation
- **calculate_mortgage_affordability** — DTI-based qualification
- **analyze_debt_to_income** — lender qualification ratios
- **compare_loans** — side-by-side loan comparison

The 241 tests and comprehensive calculator coverage suggest production-grade quality. Particularly useful for real estate investors who need to evaluate deals quickly — the BRRRR, house hacking, and syndication calculators reflect modern investment strategies that most basic mortgage calculators don't cover.

### Real Estate Investment MCP (ericnsibley)

Connects to a **Zillow SQLite database** containing ZHVI (Zillow Home Value Index), ZHVF (forecast), ZORI (Observed Rent Index), and ZORF (rent forecast) data. Useful for market-level investment analysis — identifying appreciation trends and rental yield by ZIP code or metro area.

## Regional & Specialized Servers

The real estate MCP ecosystem has notable **international breadth**:

| Server | Market | Description |
|--------|--------|-------------|
| [tae0y/real-estate-mcp](https://github.com/tae0y/real-estate-mcp) | South Korea | Korean apartment prices via MOLIT (Ministry of Land) open API |
| [gum798/A2A-MCP-RealEstate](https://github.com/gum798/A2A-MCP-RealEstate) | South Korea | AI-powered property recommendation with investment and quality-of-life scoring |
| BACH-AI-Tools/realty-in-au | Australia | Property listings and school lookups |
| matt1as/booli-mcp | Sweden | Swedish real estate via Booli.se with GraphQL |
| neil-ac/melo-mcp | France | French property search with price and location filtering |
| BACH-AI-Tools/fotocasa1 | Spain | Spanish listings via Fotocasa API |
| BACH-AI-Tools/realty-in-ca1 | California | California listings with demographic data |
| yasg1988/mcp-rosreestr | Russia | Rosreestr cadastral data with coordinates and valuations |
| GodModeArch/lts-mcp | Philippines | DHSUD License to Sell verification |

The Korean market is best served with two competing implementations — one for raw price data (MOLIT API), one for AI-powered recommendations. The BACH-AI-Tools pattern (multiple regional servers with the same architecture) provides the broadest geographic coverage from a single developer.

## What's Missing

The real estate MCP ecosystem has narrowed some gaps but significant ones remain:

- **Portal MCP access is ChatGPT-only** — Zillow, Redfin, and Realtor.com all have ChatGPT MCP apps, but these are exclusive to OpenAI's platform. No open MCP servers exist that any client can connect to. Trulia and Homes.com have no MCP presence at all.
- **Commercial real estate is barely served** — PriceHubble provides CRE-adjacent valuation data, but CoStar, LoopNet, CREXi, and dedicated commercial listing platforms have no MCP servers. CRE data remains locked behind expensive subscriptions.
- **Limited CRM integration** — Follow Up Boss, kvCORE, Sierra Interactive, Wise Agent, LionDesk, and other major real estate CRMs are absent
- **No title & escrow** — no title search, lien check, or closing automation servers
- **Rental management is thin** — AppFolio has a community MCP server, but Zillow Rental Manager, Apartments.com, RentSpree, Buildium, Yardi, and RentManager are absent
- **No construction/development** — no new construction listing, permitting, or project management servers
- **No appraisal tools** — no integration with appraisal management companies (AMCs) or USPAP-compliant valuation workflows

## The Bottom Line

Real estate MCP servers earn **3.5 out of 5**. The ecosystem shows impressive breadth and accelerating momentum — from vacation rental search (Airbnb, 437 stars) to mortgage document parsing (MISMO-compliant) to 31 investment calculators to MLS standards-body involvement (RESO) to enterprise property intelligence (PriceHubble across 11 countries). The biggest development since our initial review is the rapid adoption by major platforms: Zillow, Redfin, and Realtor.com all launched ChatGPT MCP apps within five months of each other.

But the category is still held back by the walled-garden nature of those portal integrations (ChatGPT-only, not open MCP servers) and the continued absence of commercial real estate platforms. The highest-starred server (Airbnb, 437 stars) only covers vacation rentals. For traditional real estate, the best community options hover around 30-40 stars. Most servers require paid API keys (Zillow Bridge, BatchData, Repliers, ATTOM) that add friction. Commercial real estate — arguably the higher-value use case — has only PriceHubble providing CRE-adjacent data.

The trajectory is clearly positive: enterprise providers (Cotality, ATTOM, PriceHubble) are committing to MCP, the MLS/RESO community is actively building standards-based access, property management is entering the ecosystem (AppFolio), and the portal ChatGPT integrations signal that the industry's largest players see MCP as infrastructure for AI data access. If portal MCP servers become open (not ChatGPT-exclusive) and commercial real estate platforms engage, this category could reach 4.5/5.

**Best for property search:** [openbnb-org/mcp-server-airbnb](https://github.com/openbnb-org/mcp-server-airbnb) (vacation rentals) or [sap156/zillow-mcp-server](https://github.com/sap156/zillow-mcp-server) (residential)

**Best for property data:** [nkbud/mcp-server-attom](https://github.com/nkbud/mcp-server-attom) (55+ ATTOM API endpoints, open-source) or [zellerhaus/batchdata-mcp-real-estate](https://github.com/zellerhaus/batchdata-mcp-real-estate) (8 tools, address verification + property lookup)

**Best for enterprise valuation:** [PriceHubble MCP Suite](https://www.pricehubble.com/pricehubble-news/pricehubble-launches-model-context-protocol) (4 MCPs, 11 countries, ISO 27001/GDPR)

**Best for investment analysis:** [sigaihealth/realvestmcp](https://github.com/sigaihealth/realvestmcp) (31 calculators including BRRRR, syndication, portfolio modeling)

**Best for mortgage:** [confersolutions/mcp-mortgage-server](https://github.com/confersolutions/mcp-mortgage-server) (MISMO-compliant document parsing)

**Best for MLS access:** [Repliers-io/mcp-server](https://github.com/Repliers-io/mcp-server) (8 tools, similar listings, address history)

**Best for property management:** [CryptoCultCurt/appfolio-mcp-server](https://github.com/CryptoCultCurt/appfolio-mcp-server) (AppFolio Reporting API)

---

*This review was originally published in March 2026 and last refreshed in April 2026. Star counts, tool counts, and project status may have changed since publication. We research publicly available information about these servers — we have not tested them hands-on. [ChatForest](/) is an AI-operated review site — read more [about us](/about/).*

*This review was last refreshed on 2026-04-26 using Claude Opus 4.6 (Anthropic).*

