# MCP and Real Estate: How AI Agents Connect to MLS Data, Property Valuations, Mortgage Systems, Smart Buildings, Transaction Management, and Geographic Intelligence

> A comprehensive guide to MCP integrations for real estate — covering MLS/property data, valuations, mortgage/lending, commercial real estate, smart buildings, document/transaction


AI agents are changing how properties are searched, valued, bought, sold, and managed. What once required a team of specialists — each with access to separate, siloed systems — can increasingly be coordinated by a single AI agent pulling from multiple data sources simultaneously. A buyer's agent AI can query MLS listings, pull neighborhood demographic data, run a mortgage pre-qualification, check flood risk, and generate a comparative market analysis, all without switching applications.

This transformation is happening against a backdrop of significant investment. The AI in real estate market was estimated at $303 billion in 2025 and is projected to approach $1 trillion by 2029. Commercial real estate companies running AI pilots grew from 5% to 92% in just three years. The challenge has been integration: real estate data is fragmented across hundreds of MLS systems, dozens of public records databases, proprietary valuation engines, lender rate sheets, and building management platforms.

The Model Context Protocol (MCP) is emerging as a standard for connecting AI agents to these fragmented systems. Rather than every AI product building custom integrations to every data source, MCP lets any compliant AI agent communicate with any compliant data provider through a common protocol. January 2026 saw ATTOM — one of the largest U.S. property data companies — launch what it described as the first large-scale real estate data MCP server. Enterprise valuation firm PriceHubble entered beta the same quarter. MLS platforms began building their own servers. The ecosystem is early but accelerating.

This guide is research-based. We survey the MCP servers that exist, what they expose, and how they fit together in architectural patterns for real estate applications. We do not claim to have tested or used any of these servers hands-on. [Rob Nugen](https://robnugen.com), the operator of this site, has established ChatForest as a research and documentation resource for the AI ecosystem. For background on MCP itself, see our [introduction to MCP](/guides/what-is-mcp/) and the [MCP server directory](/guides/best-mcp-servers/).


## Why Real Estate Needs MCP

Real estate is structurally complex in ways that make AI integration harder than most industries. Five fundamental challenges explain why MCP matters here.

**Data fragmentation.** Property data exists across roughly 600 MLS systems in the United States alone, each with separate authorization rules, data schemas, and access mechanisms. Public records — deed transfers, tax assessments, foreclosures, permits — are maintained at the county level across thousands of jurisdictions. Environmental risk, flood zone maps, and zoning data come from yet more sources. An AI agent attempting to answer a question like "what are the tax-assessed values of homes sold in this zip code in the past 90 days" would historically require custom code linking multiple disparate systems. MCP servers that wrap these data sources let agents query them through a standard interface.

**Transaction complexity.** A residential real estate transaction involves, at minimum, a buyer, seller, buyer's agent, listing agent, lender, appraiser, title company, and escrow officer — often more. Each participant has their own software, their own documents, and their own timeline. MCP enables multi-agent workflows where specialized agents handle mortgage calculations, document review, and eSignature orchestration while a coordinating agent maintains transaction state.

**Valuation intelligence.** Automated Valuation Models (AVMs) require real-time access to comparable sales, market trends, and property characteristics. Traditional AVM integration means custom API contracts. With MCP, an agent can pull Zestimate data from a Zillow-connected MCP server, ATTOM AVM data from another server, and RentCast rent estimates from a third — and synthesize them in a single response.

**Geographic context.** Location is foundational to real estate value, but geographic analysis requires specialized tools: spatial queries, proximity calculations, demographic overlays, flood zone intersections, school district boundaries. GIS toolkits like GeoPandas and Shapely are powerful but complex. MCP servers wrapping these libraries make geographic intelligence accessible to AI agents without requiring expertise in spatial programming.

**Document workflows.** Real estate generates substantial paperwork: purchase agreements, disclosures, loan estimates, closing disclosures, inspection reports, title commitments. Parsing, reviewing, and routing these documents is a significant operational burden. MCP servers connecting to DocuSign and other document platforms let AI agents participate in these workflows directly.


## MLS and Property Data

### ATTOM MCP Server

ATTOM launched its MCP server on January 29, 2026, making it the first large-scale real estate data company to do so. The server covers 158 million U.S. properties — approximately 99% of the U.S. population. Data types include property details, AVMs, comparable sales, sales history, tax records, deed and mortgage data, foreclosure status, environmental risk, natural hazard assessments, and neighborhood and geospatial boundaries.

The ATTOM MCP server is a commercial product, not open source. It requires an ATTOM API key and is positioned as enterprise-grade infrastructure. Data is linked across sources through a unique ATTOM ID for each property, and the underlying data goes through a 20-step validation process. ATTOM serves real estate, fintech, government, and insurance clients. Because it covers AVMs as well as raw property data, it appears in both the property data and valuation sections of this analysis.

### Cotality MCP Server

Cotality (formerly CoreLogic) — one of the largest global property data companies — launched its MCP server on March 31, 2026. Cotality describes it as a "universal connector" between AI models and its property data foundation, which covers virtually every U.S. address. The MCP server is designed for production-grade workflows including underwriting, valuation, and risk analysis.

Key capabilities include CLIP ID access (Cotality's unique property identifiers for unambiguous cross-system matching), comprehensive property details and characteristics, climate risk assessments, and real-time market trends. Cotality also announced "AI-Ready Data" assets — structured data designed specifically for AI model consumption, acting as a "translator" that helps AI models understand the meaning behind property data values rather than just the raw numbers.

The server is built on the open MCP standard and supports ChatGPT, Claude, Gemini, and other MCP-compatible clients. Authentication is required and access is governed through Cotality's commercial platform. The combination of MCP server (connectivity) and AI-Ready Data (semantic enrichment) differentiates Cotality's approach from competitors that expose raw API endpoints. For organizations already in the Cotality ecosystem — which includes most major lenders, servicers, and insurers — this is the most direct path to AI-powered property intelligence.

Cotality's entry alongside ATTOM means the two largest U.S. property data providers now both have MCP servers, establishing MCP as the standard integration layer for enterprise real estate AI.

### BatchData MCP Server

BatchData's MCP server (GitHub: zellerhaus/batchdata-mcp-real-estate, 28 stars) provides access to 155+ million U.S. properties through 8 tools organized into two groups. Address tools handle verification, autocomplete, geocoding, and reverse geocoding. Property tools handle individual property lookup, search, boundary-based search, and property counts.

The server is built in TypeScript with Node.js and requires a BatchData API key. It is MIT-licensed and installable via Smithery. Property data includes characteristics, ownership records, transaction history, tax assessments, and mortgage details. With 28 stars and 7 forks, it has the most community traction of any property data MCP server after ATTOM.

### Zillow MCP Server

The community-built Zillow MCP server (GitHub: sap156/zillow-mcp-server, 34 stars) exposes 7 tools: search_properties, get_property_details, get_zestimate, get_market_trends, calculate_mortgage, check_health, and get_server_tools. It is built in Python using FastMCP and connects via the Zillow Bridge API, which requires a separate API key.

An important constraint: the server performs dynamic queries only and does not cache or store data locally, in compliance with Zillow's terms of service. The Zestimate tool is significant — Zillow's proprietary valuation model is one of the most-recognized AVMs in the U.S. consumer market, and having it accessible via MCP enables direct integration into agent workflows.

### Constellation1 MCP Server

Constellation1 provides technology infrastructure to brokerages, franchises, and MLSs across North America. Its MCP server exposes two tools: reso_query (for querying RESO-standardized entities including properties, agents, offices, media, and market analytics via OData) and reso_help (field references and best practice guidance).

Coverage is 100% of the U.S. market and 90% of Canada. Authentication requires a Constellation1 client ID and secret. The server is production-grade. Notably, Redfin chose Constellation1 for MLS data aggregation in 2022, which gives some indication of the platform's position in the market.

### UNLOCK RESO Reference Implementation

David Gumpper — WAV Group technology consulting lead and former CTO of Michael Saunders and Company — built a reference MCP server (GitHub: GumpperGroup/unlock-reso-mcp-remote) demonstrating how an MLS could expose data through the protocol. It implements the RESO Data Dictionary 2.0 via Bridge Interactive's RESO Web API.

The 4-tool implementation (search_properties, get_property_details, analyze_market, find_agent) includes support for natural language queries like "3 bedroom house under $500k in Austin TX" and 8 resource endpoints covering property types, market analysis guides, agent search, and workflow patterns. This is a reference and demonstration project, not a production MLS deployment, but it establishes a pattern other MLSs can follow.

### Real Estate MCP (agentic-ops)

The comprehensive community server at agentic-ops/real-estate-mcp (30 stars, 10 forks) is the most feature-complete open-source real estate MCP implementation. It exposes 30+ tools across six categories: Property Management (7 tools for search, filtering, and insights), Agent Operations (6 tools for profiles and portfolio management), Market Analysis (7 tools for price analytics and opportunity assessment), Client Management (3 tools for preference matching and recommendations), Area Intelligence (9 tools for school, park, healthcare, and amenity data), and System Management.

The server also includes 10 resource endpoints and 11 prompts covering property analysis, client consultation, investment analysis, and market reports. It is built in Python with FastMCP, supports both stdio and SSE transport, and includes GitHub Actions for CI. Its primary value is as a demonstration of what a full-featured real estate MCP implementation looks like architecturally, rather than as a production data source.

### Real Estate Intelligence (DanielJandric)

This specialized server (GitHub: DanielJandric/realestatemcp) solves a specific problem: AI-powered management of a European property portfolio. The dataset includes 31,605 document chunks with OpenAI embeddings, covering 8 properties, 463 units, 95 leases, and 653+ documents including 68 land registry extracts.

Seven tools support semantic search, property analytics, servitude analysis (a European legal concept involving property rights), complex queries, document categorization, tenant retrieval, and maintenance contract analysis. The architecture — Supabase with pgvector plus Azure Document Intelligence for OCR — is production-ready for its target use case. It operates entirely locally without external API dependencies at query time.

### RentCast MCP Server

RentCast provides AVM and rental market data for 140+ million U.S. properties. Its MCP server integration (community-built) exposes tools for property data retrieval, property valuation, rent estimation, market statistics by ZIP code, and property listings. The rent estimate tool provides a range with comparable listings, which is more useful for investment analysis than a point estimate alone.

### MLS Servers Under Development

Two MLSs were reported to be building production MCP servers as of late 2025. UtahRealEstate.com was the first MLS to publicly announce an MCP server launch (September 2025), with CEO Brad Bjelke describing the initiative in terms of "technology sovereignty" — MLSs controlling their own AI infrastructure rather than ceding it to third parties. NorthstarMLS was reported close to completion through a partnership with reDataExport, a venture founded by UtahRealEstate.com in January 2025. Neither was production-live in the field as of early 2026.


## Valuation and Appraisal

### PriceHubble

PriceHubble entered early-access beta with an MCP server in Q1 2026. The platform serves 800+ enterprise clients across 11 countries with capabilities including automated property valuations (AVM), market forecasts, portfolio optimization, and energy performance assessments. Compliance certifications include ISO 27001 and GDPR, plus alignment with the NIST AI Risk Management Framework.

The 11-country coverage makes PriceHubble particularly relevant for firms operating across European markets, where valuation standards and data availability differ significantly from the U.S.

### ATTOM, Zillow, and RentCast (Valuation Components)

All three property data MCP servers discussed in the previous section include valuation capabilities. ATTOM exposes AVMs alongside comparable sales data. Zillow provides Zestimate access through the get_zestimate tool. RentCast provides both home value estimates and rent estimates with comparable listings.

### The Appraisal Gap

No dedicated MCP server exists for traditional appraisal workflows. The distinction matters: AVMs are statistical models that produce instant estimates, while appraisals are regulated professional opinions of value that follow methodologies like the URAR (Uniform Residential Appraisal Report) form, requiring adjustment grids, comparable selection reasoning, and certification. Appraisal management companies (AMCs) and appraisal software platforms have not announced MCP integrations. This is a notable gap, particularly as lenders and GSEs experiment with appraisal modernization.


## Mortgage and Lending

### Confer Solutions MCP Mortgage Server

The Confer MCP server (GitHub: confersolutions/mcp-mortgage-server, 2 stars) focuses on TRID compliance — the mortgage disclosure rules that govern Loan Estimates (LE) and Closing Disclosures (CD). Its 4 tools parse LE and CD PDFs into MISMO-compliant JSON with LLM-enriched context, and compare LE and CD documents to flag discrepancies.

The server was substantially rewritten at version 2.0.0 and includes production-grade security features: HTTPS-only URLs, domain whitelisting to prevent SSRF attacks, 10MB document size limits, and 30-second timeouts. MISMO (Mortgage Industry Standards Maintenance Organization) compliance means the output format is interoperable with other mortgage industry systems. This is a narrow but genuinely useful capability — mortgage professionals reviewing TRID compliance spend significant time on these comparisons.

### RateSpot

RateSpot provides real-time mortgage rates from 4,300+ lenders through an MCP-compatible API. The service aggregates from established rate comparison platforms including Bankrate, Icanbuy, and Zillow. Tools support fetching current rates, comparing loan products, calculating monthly payment breakdowns, and retrieving lender information. Primary use cases are AI-powered financial advisors and mortgage chatbots.

### RateAPI

RateAPI (rateapi.dev) offers native MCP support for Claude with a free tier of 50 requests per month. Beyond mortgages, it covers auto loans, HELOCs, personal loans, and credit cards — which matters for real estate contexts where buyers are evaluating their full debt picture alongside a mortgage.

### Homebuyer.com

Homebuyer.com's developer platform provides 8 mortgage tools free for non-commercial use. Seven tools require no API key. The eighth, which queries HMDA (Home Mortgage Disclosure Act) data through BigQuery, requires a free API key and provides access to 121 million mortgage records. HMDA data is significant for fair lending analysis — it contains loan-level data on race, ethnicity, income, and loan outcomes that regulators use to identify discriminatory lending patterns.

### TinyFn

TinyFn provides general financial calculation tools via MCP, including mortgage calculation and loan amortization. It is a supporting tool rather than a specialized mortgage MCP server, but it enables AI agents to do on-the-fly payment calculations without dedicated mortgage API access.


## Commercial Real Estate

### LoopNet MCP Server

The only CRE-specific MCP server found in research is a community scraper for LoopNet (GitHub: johnstenner/LoopnetMCP, 1 star). The server exposes 3 tools — property search, property details, and market overview — across all major property types: office, retail, industrial, multifamily, land, hospitality, special-purpose, and healthcare.

Because LoopNet has no public API, the server relies on scraping through curl_cffi and nodriver (headless Chrome), with logic to handle Akamai Bot Manager's TLS fingerprint checks and JavaScript challenges. Practical limitations are significant: results are first-page only, there is a 5-minute cache TTL, and CAPTCHAs may cause intermittent failures.

### The CRE Platform Gap

The major commercial real estate data platforms — CoStar, ARGUS, Yardi Matrix, RCA Analytics — have not announced MCP servers. CoStar launched AI-powered conversational search on Homes.com in February 2026 through Microsoft Foundry, but this is a consumer product rather than a programmatic data API. ARGUS, widely used for DCF modeling of income-producing properties, has no MCP integration.

The gap in CRE is more significant than in residential. CRE transactions are larger, more complex, and involve more data types (rent rolls, CAM reconciliations, lease abstracts, NOI statements) where AI assistance would add substantial value. The absence of major platform MCP support reflects both the relative insularity of CRE data markets and the earlier adoption curve.


## Smart Buildings and PropTech

### ProptechOS

ProptechOS is the most significant smart building platform to adopt MCP. The platform uses the RealEstateCore open standard for building data harmonization, then exposes that data through MCP for AI agent access. Building data — from BMS systems, BIM models, and IoT devices — is organized into a digital twin that AI agents can query and act on.

Capabilities include energy optimization, indoor climate monitoring, building availability queries, ESG compliance reporting, and tenant experience management. ProptechOS describes its approach as "Agentic Proptech" — AI agents that investigate conditions, reason about them, and take action across portfolios. The platform is in production with commercial clients.

The combination of RealEstateCore (a semantic data model for buildings) and MCP (a communication protocol for AI agents) is a meaningful architectural pattern. RealEstateCore provides the ontology — what concepts like "room," "energy meter," and "occupancy sensor" mean in a building context — while MCP provides the protocol layer for AI agents to query and act on that ontology.

### The BMS Vendor Gap

The major building management system vendors — Siemens, Honeywell, and Johnson Controls — have not announced MCP support. These three companies collectively manage a substantial share of large commercial building infrastructure. Their absence from the MCP ecosystem means that most deployed smart building infrastructure is not yet accessible to AI agents through a standard protocol.


## Document and Transaction Management

### DocuSign (Official)

DocuSign released an official MCP server in beta, available through the Claude Connectors Directory. It covers IAM and eSignature capabilities: document sending, agreement status tracking, template management, and workflow automation. The server operates within DocuSign's established authentication and permission boundaries. It also powers DocuSign's ChatGPT integration.

For real estate, DocuSign is the dominant eSignature platform. Listing agreements, purchase contracts, disclosure packages, and addenda are routinely executed through DocuSign. An MCP-connected agent can check document status, trigger send workflows, and manage templates without manual intervention.

### DocuSign (Community Implementations)

Three community implementations cover DocuSign as well. CData Software's server (GitHub: CDataSoftware/docusign-mcp-server-by-cdata) provides read-only access via JDBC drivers, useful for audit and reporting workflows. Luther Systems built a FastMCP-based server (GitHub: luthersystems/mcp-server-docusign) using JWT server-to-server authentication, suitable for automated backend workflows. Composio's DocuSign integration exposes the same capabilities through their multi-platform MCP hub, supporting Claude, ChatGPT, Cursor, and other clients.

### The Transaction Management Gap

Real estate-specific transaction management platforms — Dotloop (owned by Zillow Group), SkySlope, and Glide — have not announced MCP support. Dotloop connects to approximately 200 MLS and realtor association feeds and manages the document workflow for a large share of U.S. residential transactions. The absence of MCP support means agents working in these platforms cannot currently integrate AI assistance into the transaction workflow at the platform level.


## Geographic and Location Intelligence

### GIS MCP Server

The GIS MCP server (GitHub: mahdin75/gis-mcp, 126 stars, 41 forks) is the most-starred GIS tool in the MCP ecosystem. Version 0.14.0 beta exposes 95 tools across five Python geospatial libraries:

- **Shapely** (29 tools): Geometry operations — creating, measuring, and analyzing geometric shapes
- **PyProj** (13 tools): Coordinate system transformations between geographic reference systems
- **GeoPandas** (13 tools): Spatial data analysis combining pandas DataFrames with geometry
- **Rasterio** (20 tools): Raster data processing for satellite imagery, elevation models, and spatial grids
- **PySAL** (18 tools): Spatial statistics including autocorrelation, clustering, and regional analysis

For real estate, the most relevant capabilities are PySAL's spatial clustering (useful for neighborhood segmentation and market area definition), GeoPandas overlays (combining property boundaries with other spatial datasets), and buffer analysis (measuring what's within a given distance of a property). The server supports stdio, HTTP, and SSE transports.

### CARTO

CARTO's official MCP server bridges geospatial workflows with AI agents by exposing CARTO Workflows as MCP tools. The real estate use case CARTO highlights is site selection: "Which Maryland counties have high income, favorable demographics, and limited competition?" An agent can run that query against CARTO's data platform and receive a ranked list with supporting analytics and interactive map output.

Other RE applications include investment analysis with demographic overlays, retail site planning, and neighborhood market characterization. CARTO is an enterprise platform with governance controls, making it suitable for institutional real estate analytics.

### ArcGIS Location Services

The ArcGIS community MCP server provides 6+ tools covering geocoding, reverse geocoding, nearby places, directions, elevation data, and basemap tiles via Esri's ArcGIS Location Platform. Real estate applications include property address verification at scale, commute time analysis, elevation data for flood risk assessment, and point-of-interest proximity for neighborhood scoring.

Authentication requires an ArcGIS Developer API key. The server is installable via Smithery.

### Google Maps

Multiple community MCP servers expose the Google Maps platform. The comprehensive version (vicpeacock/google-maps-comprehensive-mcp) provides 8 tools. An extended version (cablate/mcp-google-map) expands to 18 tools including batch geocoding of up to 50 addresses simultaneously. The standard tool set covers geocoding, reverse geocoding, place search, place details, distance matrix calculations, elevation, and directions.

For real estate agents, commute time is one of the most common buyer questions. An agent AI with Google Maps MCP access can answer "what's the commute from this property to downtown during rush hour" directly, without requiring the buyer to open a separate application.

### The Neighborhood Data Gap

Walk Score, GreatSchools, NeighborhoodScout, and the EPA's Smart Location Database (which provides 90+ neighborhood walkability and location efficiency indicators) lack dedicated MCP servers. U.S. Census demographic data, critical for investment analysis and fair housing compliance work, also has no direct MCP adapter. Some data is accessible through general GIS MCP servers or web scraping tools, but the absence of structured MCP coverage for neighborhood quality data is a notable gap given how central these metrics are to real estate decisions.


## Data Aggregators

### Apify Real Estate Aggregator

The sovereigntaylor Real Estate Aggregator on Apify scrapes and unifies data from Zillow, Redfin, and Realtor.com. It de-duplicates listings by address and provides unified analytics including median price, price per square foot, and days on market. Pricing is pay-per-event at $0.01 per tool call, making it accessible for low-volume research without a subscription.

Additional Apify MCP servers target specific platforms: a Redfin scraper for property details, pricing, and photos; a Zillow scraper for listings and prices; and a harvestlabs AI Real Estate Agent for Realtor.com data including agent profiles.

### Bright Data

Bright Data's MCP server (GitHub: brightdata/brightdata-mcp, 60+ tools) provides commercial-grade web data extraction with proxy rotation, CAPTCHA solving, and anti-blocking infrastructure. Bright Data also maintains a dedicated real estate AI agent repository (brightdata/real-estate-ai-agent) demonstrating structured property data extraction using AI agents plus Bright Data MCP. For applications requiring reliable, at-scale data extraction from property sites that don't offer official APIs, Bright Data represents the most robust available option.

### Real Estate Investment MCP

The ericnsibley/GenAI_MCP project stores Zillow Housing Value Indices (ZHVI), Zillow Home Value Forecasts (ZHVF), Zillow Observed Rent Indices (ZORI), and Zillow Observed Rent Forecasts (ZORF) in a local SQLite database accessible via MCP. While limited in scope, it demonstrates how time-series market data can be made queryable by AI agents for investment analysis and forecasting workflows.


## Real Estate CRM

### HubSpot

HubSpot's official MCP server (production) provides 100+ tools covering contacts, companies, deals, and other CRM objects. Access is currently read-only. HubSpot is widely used by real estate teams and brokerages as a general-purpose CRM. The MCP server enables agents to query deal pipeline, retrieve contact histories, and analyze company relationships — useful for transaction coordination and client management.

### Salesforce

Salesforce's official MCP server provides 60+ tools with full CRUD capability, but access is restricted to Agentforce, Salesforce's own AI agent framework. Large brokerages and commercial real estate firms using Salesforce CRM cannot currently integrate external AI agents via MCP without going through Agentforce.

### The RE CRM Gap

Real estate-specific CRMs — Follow Up Boss, kvCORE (now Lofty), LionDesk, Real Geeks, and Wise Agent — have not announced MCP servers. These platforms are purpose-built for real estate agent workflows including lead capture, drip campaigns, showing schedules, and client communication tracking. Their absence from the MCP ecosystem means agents on these platforms must work around the gap with general CRM MCP servers or wait for platform-level integrations.


## Comparison Table

| Server | Category | Stars | Tools | Type | Maturity |
|---|---|---|---|---|---|
| ATTOM | MLS/Property Data | N/A | Multiple | Official/Commercial | Production |
| Constellation1 | MLS/Property Data | N/A | 2 | Official/Commercial | Production |
| BatchData | MLS/Property Data | 28 | 8 | Community | Production-quality |
| Zillow (sap156) | MLS/Property Data | 34 | 7 | Community | Active |
| Real Estate MCP (agentic-ops) | MLS/Property Data | 30 | 30+ | Community/Demo | Demo |
| UNLOCK RESO (GumpperGroup) | MLS/Property Data | 1 | 4 | Community/Reference | Reference |
| Real Estate Intelligence (DanielJandric) | Property Mgmt | 0 | 7 | Community | Production (niche) |
| RentCast | MLS/Valuation | N/A | 5 | Community/Commercial | Active |
| PriceHubble | Valuation | N/A | Multiple | Official/Commercial | Beta |
| Confer Mortgage | Mortgage/Lending | 2 | 4 | Community/Commercial | Production-ready |
| RateSpot | Mortgage/Lending | N/A | Multiple | Commercial | Production |
| RateAPI | Mortgage/Lending | N/A | Multiple | Commercial | Production |
| Homebuyer.com | Mortgage/Lending | N/A | 8 | Official | Production |
| TinyFn | Financial Calc | N/A | Multiple | Commercial | Production |
| LoopNet MCP | Commercial RE | 1 | 3 | Community/Scraper | Experimental |
| ProptechOS | Smart Buildings | N/A | Multiple | Official/Commercial | Production |
| DocuSign (official) | Documents | N/A | Multiple | Official | Beta |
| DocuSign (CData) | Documents | N/A | Multiple | Community | Active |
| DocuSign (Luther) | Documents | N/A | Multiple | Community | Active |
| DocuSign (Composio) | Documents | N/A | Multiple | Platform | Production |
| GIS MCP | Geographic/GIS | 126 | 95 | Community | Beta |
| CARTO | Geographic/GIS | N/A | Multiple | Official/Commercial | Production |
| ArcGIS | Geographic/GIS | N/A | 6+ | Community | Active |
| Google Maps (vicpeacock) | Geographic/GIS | N/A | 8 | Community | Active |
| Google Maps (cablate) | Geographic/GIS | N/A | 18 | Community | Active |
| Apify RE Aggregator | Aggregator | N/A | Multiple | Commercial | Production |
| Bright Data | Aggregator | N/A | 60+ | Commercial | Production |
| RE Investment (ericnsibley) | Aggregator/Indices | 1 | Multiple | Community | Demo |
| HubSpot | CRM | N/A | 100+ | Official | Production |
| Salesforce | CRM | N/A | 60+ | Official | Production (restricted) |


## Architecture Patterns

### Property Search and Valuation Pipeline

This pattern coordinates three MCP servers — an MLS data source, a valuation engine, and a geographic intelligence server — to answer complex buyer queries with synthesized responses.

```
User Query: "Find 3BR homes under $600k in zip 98103,
            good walkability, <30min commute to downtown"
                    |
                    v
          [Coordinating RE Agent]
                    |
        +-----------+----------+
        |           |          |
        v           v          v
  [MLS MCP]   [Valuation]  [Geo MCP]
  BatchData   RentCast AVM  Google Maps
  (listings)  (value est.)  (commute)
        |           |          |
        +-----------+----------+
                    |
                    v
          [Agent synthesizes:
           filtered listings +
           value vs. ask price +
           commute time per property]
                    |
                    v
          Ranked results with
          AVM delta and commute
```

The agent first queries the MLS server for listings matching location, price, and bedroom criteria. It then calls the valuation server for each result to compare asking price to AVM estimate, flagging potential over/underpricing. Simultaneously, it queries the geographic server for commute times from each property address to the destination. Final output synthesizes all three data streams into a ranked result set.

For production use, this pattern benefits from the [tool composition patterns](/guides/mcp-tool-composition-workflows/) described in our guide on MCP workflows, particularly for handling partial failures when one data source is unavailable.

### Mortgage Pre-Qualification Workflow

This pattern uses document parsing, rate lookup, and property data tools to automate the initial pre-qualification assessment.

```
Input: Property address + borrower financials
                    |
                    v
        [Mortgage Agent]
                    |
        +-----------+-----------+
        |           |           |
        v           v           v
  [Confer MCP]  [RateSpot]  [ATTOM MCP]
  Parse LE/CD   Live rates   Property tax
  TRID check    4300+lenders  assessment
        |           |           |
        +-----------+-----------+
                    |
                    v
        [Agent calculates:
         max loan at current rates +
         PITI (principal, interest,
         taxes, insurance) +
         debt-to-income ratio]
                    |
                    v
        Pre-qual assessment with
        rate scenarios and
        TRID compliance notes
```

The Confer server handles document parsing for any existing loan documents. RateSpot provides current market rates for loan product comparison. ATTOM provides tax assessment data for PITI calculation. The agent synthesizes a pre-qualification picture including multiple rate scenarios.

### Commercial Real Estate Intelligence

This pattern addresses the data gap in CRE by combining available tools with data aggregation capabilities.

```
Query: "Analyze office market in downtown Austin —
        vacancy, pricing trends, comparable deals"
                    |
                    v
     [CRE Research Agent]
                    |
        +-----------+------------+
        |           |            |
        v           v            v
  [LoopNet MCP]  [CARTO MCP]  [Bright Data]
  Current       Demographic   Deep web
  listings      overlays      extraction
  (limited)     (official)    (fallback)
        |           |            |
        +-----------+------------+
                    |
                    v
        [Agent synthesizes available data,
         notes gaps where CoStar/ARGUS
         data would be required,
         flags limitations explicitly]
```

Because CRE MCP coverage is thin, this pattern must be transparent about limitations. The LoopNet scraper provides current listing data with known reliability constraints. CARTO provides demographic and market analytics context. Bright Data fills gaps through structured web extraction. The agent should explicitly note when critical data (CoStar comparable transaction data, ARGUS pro forma analysis) is unavailable through MCP.

### Smart Building Operations Center

This pattern applies to building operators and property managers using MCP-connected building management data.

```
Query: "Building portfolio energy performance
        vs. benchmarks — flag outliers"
                    |
                    v
    [Building Ops Agent]
                    |
        +-----------+-----------+
        |           |           |
        v           v           v
 [ProptechOS]   [GIS MCP]    [DocuSign]
 Building data  Spatial      Lease docs
 energy, HVAC   clustering   tenant data
 occupancy      portfolio    obligations
        |           |           |
        +-----------+-----------+
                    |
                    v
        [Agent identifies:
         buildings above median EUI +
         correlates with occupancy +
         checks lease terms for
         tenant energy obligations]
                    |
                    v
        Prioritized intervention list
        with supporting data
```

ProptechOS provides the building telemetry. GIS MCP enables portfolio-wide spatial analysis, including clustering buildings by geographic submarket for appropriate benchmarking. DocuSign access allows the agent to cross-reference energy performance against lease provisions that may assign energy cost responsibility to tenants.


## Security and Compliance

Real estate MCP integrations carry several compliance dimensions beyond the general security guidance in our [MCP security guide](/guides/mcp-server-security/).

**Fair housing compliance.** AI agents querying property and demographic data can inadvertently violate fair housing laws if they use protected class characteristics (race, religion, national origin, sex, disability, familial status) to filter, score, or rank properties or buyers. MCP servers exposing HMDA data, demographic overlays, or neighborhood profiles should not expose these attributes in ways that enable steering. Any agent using demographic data should be designed with explicit fair housing review.

**Data licensing and MLS rules.** MLS data is licensed, not public domain. Operators using community-built MCP servers that scrape MLS data may be violating their MLS subscriber agreement. Servers connecting to official MLS APIs (Constellation1, UNLOCK RESO, the emerging UtahRealEstate.com server) operate within authorized access. Scraping-based servers (LoopNet, some Apify tools) involve legal risk that varies by jurisdiction and the target platform's terms of service.

**Financial data protection.** Mortgage workflows handled by Confer and similar servers involve TRID-regulated documents containing borrower financial information. The TRID regulation (Truth in Lending Act / RESPA Integrated Disclosure) governs how loan cost information must be disclosed. MCP servers parsing these documents must enforce strict access controls. The Confer server's SSRF prevention and HTTPS-only requirements reflect awareness of this sensitivity.

**PII handling.** Mortgage documents contain Social Security numbers, birth dates, and income information. Document-parsing MCP servers should never log document content, should enforce minimum-necessary access, and should not retain parsed data beyond the immediate session. Our [credential and secret management guide](/guides/mcp-credential-secret-management/) covers general patterns applicable here.

**Credential management.** Real estate MCP servers typically require API keys (ATTOM, BatchData, RentCast, RateSpot) or OAuth tokens (HubSpot, DocuSign). These credentials should be stored in environment variables or secrets managers, never in configuration files that may be committed to version control. Constellation1 client credentials provide access to MLS data at scale and warrant particular care.

**Rate limiting.** Several real estate MCP servers sit on top of commercial APIs with usage-based pricing. Agents that loop across large property sets without rate limit awareness can generate unexpected API costs. The RateAPI free tier of 50 requests/month and Apify's pay-per-event model require explicit budget controls in production deployments.


## Ecosystem Gaps

The current real estate MCP ecosystem covers residential property data, valuations, mortgage calculations, and geographic analysis reasonably well. Significant gaps remain:

**Property management platforms.** AppFolio, Yardi, and Buildium collectively manage tens of millions of rental units, yet none have MCP servers. Lease management, maintenance ticketing, rent collection, and tenant communication workflows remain outside the MCP-accessible ecosystem.

**Real estate-specific CRMs.** Follow Up Boss, kvCORE/Lofty, LionDesk, Real Geeks, and Wise Agent all lack MCP support. Residential agents spend substantial time in these platforms, making them high-value targets for AI integration.

**Construction and permitting.** Procore (construction project management), municipal permit APIs, and zoning data sources have no MCP adapters. Zoning data is particularly fragmented — thousands of local jurisdictions maintain separate databases with varying formats and access mechanisms.

**CRE data platforms.** CoStar, ARGUS, and Yardi Matrix have no MCP servers. The absence of CoStar — the dominant institutional CRE data source — is the most significant single gap in the ecosystem.

**Appraisal workflows.** No MCP server supports the production of URAR appraisal forms, adjustment grid analysis, or appraisal management company (AMC) workflows. As appraisal modernization initiatives progress at Fannie Mae and Freddie Mac, this gap may attract developer attention.

**Transaction management.** Dotloop, SkySlope, and Glide manage real estate transaction documents and checklists for a large share of U.S. residential transactions. DocuSign MCP provides eSignature but not the full transaction workflow management these platforms offer.

**Neighborhood quality data.** Walk Score, GreatSchools, NeighborhoodScout, and the EPA Smart Location Database are among the most commonly referenced neighborhood data sources in real estate search. None have dedicated MCP servers.

**Census and demographics.** The U.S. Census Bureau's APIs provide detailed demographic, income, and housing data critical for investment analysis and fair housing compliance work. No structured MCP adapter exists.

**HOA management.** Homeowners association platforms (Condo Control, HOA Warrior, CINC Systems) are relevant to a large share of U.S. properties. No MCP server coverage exists.

**Insurance and risk.** Property insurance APIs, flood risk assessments, and climate risk scoring platforms (First Street Foundation, ClimateCheck) lack MCP servers. Climate risk is increasingly relevant to mortgage underwriting and property valuation.


## Getting Started

The appropriate entry point depends on your role and use case.

**Residential real estate agents** should start with BatchData or the Zillow MCP server for property data access, Google Maps MCP for commute and location queries, and DocuSign's official MCP server for transaction document workflows. HubSpot MCP provides CRM integration if your brokerage uses that platform.

**Commercial brokers** face thinner MCP coverage. The LoopNet MCP server provides access to current listings with noted limitations. CARTO MCP offers the strongest available option for market analysis and site selection. Bright Data can fill data gaps through structured extraction where official APIs are absent.

**Mortgage professionals** will find the most mature tooling in this category. Homebuyer.com's server is the lowest-friction starting point — 7 of 8 tools require no API key. Confer's server handles TRID document parsing for compliance review. RateSpot and RateAPI provide live rate data for product comparison.

**Property managers** will find the weakest MCP coverage. The DanielJandric server demonstrates what a custom MCP implementation for portfolio management can look like, and provides a useful reference for teams considering building their own server against AppFolio, Yardi, or Buildium APIs while official MCP support is absent.

**PropTech developers** building AI-powered real estate products should evaluate ATTOM as a data foundation — its 158M property coverage and multi-sourced validation makes it the most comprehensive option for U.S. residential applications. For MCP server development patterns, our [FastMCP production guide](/guides/fastmcp-production-guide/) and [MCP tool design patterns](/guides/mcp-tool-design-patterns/) are relevant starting points.

**Real estate investors** can combine RentCast (rent estimates and market statistics), ATTOM (property data and AVMs), the Zillow MCP server (Zestimate and market trends), and GIS MCP (spatial analysis and clustering) to build research workflows. The ericnsibley RE Investment server offers a simpler starting point for index-based market analysis.

The real estate MCP ecosystem is approximately where the broader MCP ecosystem was 12-18 months ago: sufficient tooling exists to build meaningful prototypes and early production systems, but coverage is uneven and major platform gaps remain. The next wave — MLS servers coming to production, property management platforms adding support, and CRE data providers entering the market — will determine whether MCP becomes the standard integration layer for real estate AI or one approach among many.

For broader context on MCP adoption across industries, see our guides on [MCP in healthcare](/guides/mcp-healthcare-fhir/), [MCP in manufacturing](/guides/mcp-manufacturing-industrial/), and [MCP in financial services](/guides/mcp-finance-fintech/).

