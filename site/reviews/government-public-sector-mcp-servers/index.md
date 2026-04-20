# Government & Public Sector MCP Servers — GovInfo, Census Bureau, Congress.gov, Data.gov, Procurement, and More

> Government and public sector MCP servers are connecting AI agents to official data, legislation, procurement, and civic infrastructure.


Government MCP servers are connecting AI agents to official data, legislation, procurement systems, and civic infrastructure. Instead of manually navigating government portals, downloading CSV files, or parsing complex API documentation, these servers let AI assistants query census data, track legislation across 50 states, search federal contracts, calculate taxes, analyze campaign finance, and access open data portals — all through the Model Context Protocol.

The landscape spans eight areas: **official agency servers** (GovInfo, Census Bureau, India NSO, France data.gouv.fr, GSA), **mega-aggregators** (multi-API collections spanning dozens of federal data sources), **legislative & congressional** (bill tracking, voting records, parliamentary intelligence), **census & demographics** (population data, statistical analysis), **open data portals** (Data.gov, Socrata, international equivalents), **government procurement** (contracts, spending, tenders), **tax & revenue** (IRS calculations, compliance), and **elections & campaign finance** (FEC data, political research).

The headline findings: **Five government agencies have released official MCP servers** ([FedScoop](https://fedscoop.com/federal-goverment-mcp-improve-ai-access-public-data/)) — more institutional adoption than any other vertical category. **The U.S. has the deepest coverage** — from official Census Bureau and GPO servers to a community mega-aggregator with [300+ tools across 40+ APIs](https://github.com/lzinga/us-gov-open-data-mcp). **Legislative tracking is remarkably complete** — LegiScan covers all 50 states, and the European Parliament server includes OSINT-grade political intelligence with [62 tools](https://github.com/Hack23/European-Parliament-MCP-Server). **Procurement is surprisingly international** — servers exist for U.S., Indian, Turkish, and Ukrainian government contracts. **The biggest gap is municipal services** — no city-level 311 systems, utility management, or local government portals have MCP implementations.

## Official Government Agency Servers

### GovInfo MCP — U.S. Government Publishing Office

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [U.S. GPO GovInfo MCP](https://www.govinfo.gov/features/mcp-public-preview) | — | TypeScript | Government | 2 tools |

Among the **first official U.S. federal MCP servers**, [released as a public preview](https://www.govinfo.gov/features/mcp-public-preview) on January 22, 2026 by the Government Publishing Office. GovInfo is the world's only GPO-certified trustworthy digital repository for U.S. government documents, hosting [100+ collections](https://github.com/usgpo/api/blob/main/docs/mcp.md) and providing AI access to:

- **Bills and laws** — full text of introduced, enrolled, and enacted legislation
- **Federal Register** — proposed rules, final rules, notices, executive orders
- **Congressional reports** — committee reports, hearing transcripts, CRS reports
- **Code of Federal Regulations** — current regulatory text
- **Presidential documents** — executive orders, proclamations, memoranda

The server exposes two tools — **searchGovInfo** (discovery) and **describePackageOrGranule** (retrieval with HTML/PDF/XML renditions and MODS/PREMIS metadata) — via the endpoint `https://api.govinfo.gov/mcp` ([GPO documentation](https://github.com/usgpo/api/blob/main/docs/mcp.md)). Requires a free API key from [govinfo.gov](https://www.govinfo.gov/api-signup).

A community implementation by [Travis-Prall/govinfo-mcp](https://github.com/Travis-Prall/govinfo-mcp) (5 stars, Python) predates the official server by ~7 months, built against the existing GovInfo API before GPO launched their native MCP endpoint.

The significance here is institutional: a U.S. federal agency officially supporting the MCP protocol signals legitimacy that community-built wrappers cannot ([FedScoop](https://fedscoop.com/federal-goverment-mcp-improve-ai-access-public-data/)). For civic tech developers, policy researchers, and legal professionals, this is a direct pipeline from the authoritative source.

### U.S. Census Bureau Data API MCP

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [uscensusbureau/us-census-bureau-data-api-mcp](https://github.com/uscensusbureau/us-census-bureau-data-api-mcp) | 63 | TypeScript | CC0-1.0 | 4 tools |

The **official Census Bureau MCP server** — under the [uscensusbureau GitHub org](https://github.com/uscensusbureau) — connects AI assistants with Census Data API through four core tools:

- **list-datasets** — discover available Census datasets
- **fetch-dataset-geography** — retrieve geographic hierarchies for datasets
- **fetch-aggregate-data** — pull aggregate statistics with geographic filtering
- **resolve-geography-fips** — resolve geographic FIPS codes

Uses PostgreSQL for local data caching, with Docker Compose setup for deployment. Covers American Community Survey (1-year and 5-year estimates), Decennial Census, Economic Census, and Population Estimates. Currently at [v0.1.2-beta](https://github.com/uscensusbureau/us-census-bureau-data-api-mcp/releases) with 152 commits.

This is practical infrastructure: researchers and analysts who routinely query Census data can now do it conversationally instead of wrestling with the Census API's notoriously complex parameter structure.

### data.gouv.fr MCP — French Government

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [datagouv/datagouv-mcp](https://github.com/datagouv/datagouv-mcp) | ~1,300 | Python | MIT | 9 tools |

The **most-starred official government MCP server** by a wide margin, and the French national Open Data platform's official MCP integration. Built by [Etalab](https://www.etalab.gouv.fr/) (the French government's open data division within DINUM), it provides 9 tools for searching, exploring, and analyzing [74,000+ datasets](https://www.data.gouv.fr/) from data.gouv.fr — France's central open data repository covering demographics, economics, transportation, health, environment, and more.

Tools span dataset operations (`search_datasets`, `get_dataset_info`, `list_dataset_resources`, `get_resource_info`, `query_resource_data`), dataservice operations (`search_dataservices`, `get_dataservice_info`, `get_dataservice_openapi_spec`), and analytics (`get_metrics`).

A public hosted instance runs at [mcp.data.gouv.fr/mcp](https://mcp.data.gouv.fr/mcp), eliminating the need for local deployment. This is the most accessible official government MCP server — point your MCP client at the URL and start querying French government data immediately. France ranks #1 in the OECD Open Data Index, and this server makes that data AI-accessible.

### India NSO eSankhyiki MCP

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [nso-india/esankhyiki-mcp](https://github.com/nso-india/esankhyiki-mcp) | 119 | Python | MIT | 21 datasets |

The **official Indian government MCP server** from the Ministry of Statistics and Programme Implementation (MoSPI), [launched February 6, 2026](https://pib.gov.in/PressReleasePage.aspx?PRID=2224472) ahead of India's AI Impact Summit. Built on [FastMCP 3.0](https://github.com/nso-india/esankhyiki-mcp) with Python 3.11+, it launched with 7 core statistical datasets and has since expanded to **21 datasets**:

- **Original 7:** Periodic Labour Force Survey, Consumer Price Index, Annual Survey of Industries, Index of Industrial Production, National Account Statistics, Wholesale Price Index, Environmental Statistics
- **Expanded to include:** Energy Statistics, AISHE (higher education), Gender Statistics, NFHS (family health), RBI data, NSS rounds (77/78/79), CPI-AL/RL, Household Consumer Expenditure, Time Use Survey, Economic Census, UDISE (school education)

The server uses a 4-step workflow: `list_datasets()` → `get_indicators()` → `get_metadata()` → `get_data()`, with OpenTelemetry/Jaeger tracing built in. Notable as one of the few non-Western government MCP implementations, demonstrating that official adoption is not limited to the U.S. and Europe.

### GSA-TTS USASpending MCP

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [GSA-TTS/usa-spending-mcp-server-DEMO](https://github.com/GSA-TTS/usa-spending-mcp-server-DEMO) | 10 | Python | Government | Multiple |

An **official GSA Technology Transformation Services** proof-of-concept MCP server for USASpending.gov API access. Includes [login.gov OIDC with PKCE](https://github.com/GSA-TTS/usa-spending-mcp-server-DEMO) authentication for cloud.gov deployment, making it a reference implementation for authenticated government MCP servers. Supports both stdio mode (for Claude Desktop) and HTTP server mode (for cloud.gov). Explicitly marked as a proof of concept, not intended for production use.

## Mega-Aggregators

### US Government Open Data MCP

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [lzinga/us-gov-open-data-mcp](https://github.com/lzinga/us-gov-open-data-mcp) | 94 | TypeScript | MIT | 300+ tools |

The **largest government MCP server by tool count** — [300+ tools spanning 40+ U.S. government APIs](https://github.com/lzinga/us-gov-open-data-mcp) in a single server:

- **Treasury** — fiscal data, debt, interest rates
- **FRED** — Federal Reserve economic data
- **Congress.gov** — bills, members, votes
- **FDA** — drug approvals, recalls, adverse events
- **CDC** — disease surveillance, health statistics
- **FEC** — campaign finance, contributions, expenditures
- **OSHA** — workplace safety inspections, violations
- **Housing** — HUD data, fair market rents
- **Patents** — USPTO patent search
- **Lobbying** — lobbying disclosures, registrations
- **Clinical Trials** — ClinicalTrials.gov data
- **Banking** — FDIC institution data
- **Transportation** — safety, infrastructure
- **Seismic** — USGS earthquake data

[20+ of the APIs require no API key](https://github.com/lzinga/us-gov-open-data-mcp), making much of the server immediately usable. Automatic cross-referencing between data sources. Also includes a TypeScript SDK for programmatic access.

This is the "if you want one government MCP server" pick — it covers more federal data in a single installation than most people will ever need.

### Gov MCP Servers (13-Server Suite)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [martc03/gov-mcp-servers](https://github.com/martc03/gov-mcp-servers) | — | TypeScript/Node.js | — | 45 endpoints |

Thirteen production MCP servers covering safety recalls, cybersecurity vulnerabilities (CVE), disasters, finance, and more. All 45 unified REST API endpoints are built on Apify with MCP SDK and published to the official MCP Registry. Deployed on Netlify at govdata-api.netlify.app.

## Legislative & Congressional

### European Parliament MCP Server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [Hack23/European-Parliament-MCP-Server](https://github.com/Hack23/European-Parliament-MCP-Server) | 11 | TypeScript | Apache 2.0 | 62 tools |

The **most sophisticated parliamentary MCP server** in any jurisdiction. Complete EP API v2 coverage with features that go well beyond basic data access:

- **8 core tools** — MEP profiles, votes, documents, committees
- **3 advanced tools** — cross-referencing, historical analysis
- **15 OSINT tools** — MEP influence scoring, coalition analysis, voting anomaly detection, network mapping
- **Phase 4 tools (8)** — expanded analytics
- **Phase 5 tools (15) + feed monitoring (13)** — comprehensive coverage
- **9 Resources + 7 Prompts** for structured analysis workflows

[1,130+ passing unit tests](https://github.com/Hack23/European-Parliament-MCP-Server) with 80%+ code coverage. ISMS-compliant and GDPR-ready. Part of Hack23's mission to "disrupt journalism with AI-generated news coverage." The OSINT capabilities are particularly noteworthy — this server can identify unusual voting patterns, map political alliances, and score individual MEP influence, effectively democratizing political intelligence analysis that was previously limited to think tanks and lobbyists.

### LegiScan MCP

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [sh-patterson/legiscan-mcp](https://github.com/sh-patterson/legiscan-mcp) | — | TypeScript | MIT | 10 tools |

All 50 U.S. states plus Congress through the LegiScan API:

- Search bills by keyword, state, session, and status
- Get full bill text, vote records, and amendment history
- Track legislation changes and monitor specific bills
- Look up legislators by state and chamber

[90%+ reduction in API usage](https://github.com/sh-patterson/legiscan-mcp) via composite tools that batch multiple API calls into single operations. Free tier allows 30,000 queries/month. For anyone tracking state-level legislation across multiple jurisdictions, this is the most comprehensive single server available.

### CongressMCP

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [amurshak/congressMCP](https://github.com/amurshak/congressMCP) | 28 | TypeScript | Sustainable Use | 91+ operations |

Congress.gov API interface organized into [6 toolsets with 91+ operations](https://github.com/amurshak/congressMCP) — Bills (16), Amendments (7), Treaties & Summaries (5), Members & Committees (13), Voting & Nominations (13), and Records & Hearings (10+). A hosted service runs at congressmcp.lawgiver.ai, eliminating the need for local setup. Works with Claude, Cursor, VS Code, and any MCP client.

### US Legal MCP

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [JamesANZ/us-legal-mcp](https://github.com/JamesANZ/us-legal-mcp) | ~3 | TypeScript | MIT | Multiple |

Cross-source U.S. legal data from Congress.gov, Federal Register, US Code, CourtListener, and Regulations.gov. Features a "search-all-legal" tool for querying across all sources simultaneously.

### Federal Register MCP

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [aml25/federal-register-mcp](https://github.com/aml25/federal-register-mcp) | — | TypeScript | — | Multiple |

Federal Register API v1 access — executive orders, presidential documents, proposed rules, notices, agency listings, public inspection documents. No authentication required. Supports both stdio and HTTP transport modes.

### Additional Legislative Servers

- **bsmi021/mcp-congress_gov_server** — Congress.gov API v3 with hybrid MCP Resources (direct lookups) and Tools (complex operations)
- **cbwinslow/opendiscourse_mcp** — Congress.gov + GovInfo bulk data ingestion with PostgreSQL storage

## Census & Demographics

### Open Census MCP Server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [brockwebb/open-census-mcp-server](https://github.com/brockwebb/open-census-mcp-server) | ~2 | Python | MIT | Multiple |

Natural language Census queries with statistical rigor that goes beyond simple API wrapping:

- Uses the **tidycensus** R package for robust data retrieval
- **ChromaDB vector database** for semantic search over Census variables
- **Fitness-for-use constraints** — margin of error thresholds, coverage bias warnings
- Prevents users from drawing invalid conclusions from small-sample data

The ~4GB Docker image reflects the statistical infrastructure bundled in. This is Census access designed for researchers who care about methodological correctness.

### Google Data Commons MCP

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [alpic-ai/datacommons-mcp](https://github.com/alpic-ai/datacommons-mcp) | — | Python | — | Multiple |

Query Google's Data Commons Knowledge Graph — census, climate, economics, health statistics from 190+ countries. Supports exploratory, analytical, and generative queries. Hosted on Google Cloud Platform, so no local instance needed.

For international demographic comparisons, this is far more useful than any single-country Census server.

### Additional Census Servers

- **shawndrake2/mcp-census** — simple access to ACS 1-year/5-year, Decennial Census, Economic Census, Population Estimates
- **uscensusbureau/us-census-bureau-data-api-mcp** — covered above in Official Agency section

## Open Data Portals

### Data.gov MCP Server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [melaodoidao/datagov-mcp-server](https://github.com/melaodoidao/datagov-mcp-server) | 19 | JavaScript | MIT | 4 tools |

U.S. Data.gov datasets via the CKAN API:

- **package_search** — search across all federal datasets
- **package_show** — get full metadata for a specific dataset
- **group_list** — browse dataset categories
- **tag_list** — explore dataset tags

Available on [npm as @melaodoidao/datagov-mcp-server](https://www.npmjs.com/package/@melaodoidao/datagov-mcp-server). CKAN is the engine behind hundreds of government open data portals worldwide, so the query patterns transfer to other countries' portals.

### Socrata Open Data Servers

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [socrata/odp-mcp](https://github.com/socrata/odp-mcp) | — | TypeScript | — | 4 tools |
| [srobbin/opengov-mcp-server](https://github.com/srobbin/opengov-mcp-server) | ~10 | TypeScript | — | Multiple |

**Two Socrata implementations** — one [official from Socrata](https://github.com/socrata/odp-mcp) (part of Tyler Technologies), one community-built. Socrata powers thousands of government open data portals at the city, county, state, and federal level. The official odp-mcp provides `list_datasets`, `get_metadata`, `preview_dataset`, and `query_dataset` (SoQL builder) with LRU caching, per-call auth overrides, and client-side rate limiting with exponential backoff. Read-only by design with a max of 5,000 rows per query. The community [opengov-mcp-server](https://github.com/srobbin/opengov-mcp-server) works with any Socrata portal — no API key required, SQL-like querying supported.

### Canada Open Government MCP

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [krunal16-c/gov-ca-mcp](https://github.com/krunal16-c/gov-ca-mcp) | — | Python | — | Multiple |

Two MCP servers in one: **Dataset MCP** for 250,000+ Canadian government datasets and **Transportation MCP** for bridges, tunnels, airports, ports, and railways with Statistics Canada cost data.

## Government Procurement & Spending

### Capture MCP Server — Federal Procurement

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [blencorp/capture-mcp-server](https://github.com/blencorp/capture-mcp-server) | 16 | TypeScript | MIT | 15 tools |

Integrates three major federal procurement data sources with [15 tools](https://github.com/blencorp/capture-mcp-server):

- **SAM.gov** (4 tools) — federal contract opportunities, entity registrations (requires API key)
- **USASpending.gov** (4 tools) — federal spending, contract awards, grants (no API key required)
- **Tango APIs** (5 tools) — additional procurement intelligence (requires API key)
- **Data-joining tools** (2 tools) — cross-reference across sources

Queue-based rate limiting for API compliance. Compatible with Claude Desktop, ChatGPT Desktop (Pro+), and any MCP-compatible client. For government contractors (GovCon), this is the essential starting point.

### GovTribe MCP — Commercial GovCon Intelligence

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| GovTribe MCP | — | — | Commercial | Multiple |

The **first commercial MCP server for government contracting**, [launched February 20, 2026](https://blog.govtribe.com/govtribe-mcp-server-connect-govtribe-to-your-ai-tools). [50+ tools](https://docs.govtribe.com/user-guide/integrations/govtribe-mcp) covering opportunities, awards, IDVs, contract vehicles, vendors, forecasts, contacts, pipeline management, and saved searches. Real-time journalism from GovExec media (parent company [GovExec Media Group](https://about.govexec.com/company/blog/govtribe-mcp-server/)). Credit-based pricing (pay-as-you-go or prepaid at discount, 100 free credits for trial). Compatible with ChatGPT, Claude, Microsoft Copilot, and custom AI applications.

### International Procurement

| Server | Language | Coverage |
|--------|----------|----------|
| [carlosahumada89/govrider-mcp-server](https://github.com/carlosahumada89/govrider-mcp-server) | TypeScript | 25+ countries (US, EU, UK, Latin America, Africa, Asia Pacific) |
| [switchr24/mcp-india-tenders](https://github.com/switchr24/mcp-india-tenders) | TypeScript | India (CPPP, eProc Rajasthan, Defence portals), OCDS-compliant |
| [saidsurucu/ihale-mcp](https://github.com/saidsurucu/ihale-mcp) | Python | Turkey (EKAP v2, 17+ search filters) |
| [VladyslavMykhailyshyn/prozorro-mcp-server](https://github.com/VladyslavMykhailyshyn/prozorro-mcp-server) | — | Ukraine (Prozorro, EDRPOU search) |

Procurement is surprisingly international — the MCP ecosystem has government contract servers for five countries plus a multi-country aggregator, more geographic diversity than most vertical categories.

### Additional Spending Servers

- **thsmale/usaspending-mcp-server** and **flothjl/usaspending-mcp** — community USASpending.gov implementations
- **GSA-TTS/usa-spending-mcp-server-DEMO** — official GSA demo (covered above)

## Tax & Revenue

### IRS Taxpayer MCP

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [dma9527/irs-taxpayer-mcp](https://github.com/dma9527/irs-taxpayer-mcp) | — | TypeScript | MIT | 39 tools |

The most comprehensive tax calculation MCP server:

- **Federal tax calculations** — income tax, capital gains, AMT
- **State tax calculations** — state-specific rates and rules
- **Credits and deductions** — earned income, child tax, itemized deductions
- **Retirement strategies** — IRA, 401(k), Roth conversion analysis
- **Tax planning** — estimated payments, withholding optimization

Covers TY2024 and TY2025 — including [One Big Beautiful Bill Act](https://github.com/dma9527/irs-taxpayer-mcp) provisions (updated standard deductions of $15,750 single, elevated Child Tax Credit of $2,200, expanded SALT cap of $40,000, and four new deductions for tips, overtime, senior bonus, and auto loan interest). All calculations run locally — zero network calls, stateless architecture. Available on [npm as irs-taxpayer-mcp](https://www.npmjs.com/package/irs-taxpayer-mcp) (v0.5.3). Also includes 50-state tax comparison, Backdoor/Mega Backdoor Roth guidance, AMT, NIIT, and SE tax calculations.

### Additional Tax Servers

- **gama104/GamaMcpServer** — public MCP server for tax-related operations
- **TaxBandits MCP** — commercial remote MCP server for TaxBandits tax filing platform

## Elections & Campaign Finance

### FEC MCP Server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [sh-patterson/fec-mcp-server](https://github.com/sh-patterson/fec-mcp-server) | — | TypeScript | — | Multiple |

Federal Election Commission campaign finance research:

- **Candidate search** — find candidates by name, state, office, party
- **Financial reports** — campaign funding summaries, filing history
- **Schedule A** — itemized individual contributions
- **Schedule B** — disbursements and expenditures
- **Schedule E** — Super PAC independent expenditures

### Additional Election Servers

- **psalzman/mcp-openfec** — OpenFEC API access for campaign finance data
- **hodgesmr/agent-fecfile** — Claude Code plugin + Agent Skill + MCP server for analyzing FEC filings

## Regulatory Compliance

### US Compliance MCP

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [Ansvar-Systems/US_Compliance_MCP](https://github.com/Ansvar-Systems/US_Compliance_MCP) | — | — | — | Multiple |

Comprehensive compliance analysis covering [50 U.S. regulations](https://github.com/Ansvar-Systems/US_Compliance_MCP) across healthcare (HIPAA, HITECH), financial (SOX, GLBA, FFIEC, NYDFS 500, BSA/AML, Dodd-Frank), federal security (FISMA, FedRAMP, CMMC 2.0, CIRCIA), export controls (ITAR, EAR), education/privacy (FERPA, COPPA), medical devices (FDA 21 CFR Part 11), environmental (EPA RMP), and 18 state privacy laws. Uses SQLite FTS5 full-text search across 2,079 sections and 135 definitions with verbatim regulatory text (no LLM paraphrasing). Remotely hosted at `https://mcp.ansvar.eu/us-regulations/mcp` with daily freshness monitoring and security scanning (CodeQL, Semgrep, Trivy, Gitleaks).

### Additional Compliance & Legal Servers

- **TCoder920x/open-legal-compliance-mcp** — GovInfo + CourtListener + EUR-Lex for multi-jurisdiction compliance
- **Multiple CourtListener MCP servers** — Travis-Prall, blakeox, DefendTheDisabled implementations for federal court data

## Nonprofit & Charity Data

### ProPublica Nonprofit Explorer MCP

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [asachs01/propublica-mcp](https://github.com/asachs01/propublica-mcp) | — | — | — | 6 tools |

IRS Form 990 data for 3 million+ tax-exempt organizations. Financial analysis, executive compensation, similar organization search. ProPublica's Nonprofit Explorer is the standard source for nonprofit financial transparency.

### Charity MCP Server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [briancasteel/charity-mcp-server](https://github.com/briancasteel/charity-mcp-server) | — | TypeScript | MIT | 4 tools + 14 prompts |

IRS charity database access — tax-deductible status verification, nonprofit search, research workflows with 14 prompt templates for common nonprofit analysis tasks.

## Public Health Data

### PopHIVE MCP Server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [Cicatriiz/pophive-mcp-server](https://github.com/Cicatriiz/pophive-mcp-server) | — | TypeScript | — | 5 tools |

Near real-time health surveillance from [Yale School of Public Health's PopHIVE platform](https://github.com/Cicatriiz/pophive-mcp-server), which aggregates data from CDC surveillance systems, Epic Cosmos EHR networks, and Google Health Trends. [11 datasets](https://github.com/Cicatriiz/pophive-mcp-server) covering immunizations (NIS/Epic), respiratory (ED visits/lab/wastewater/trends), chronic conditions (obesity/diabetes), hospital capacity, injury/overdose data, and youth mental health ED visits. Five tools: `filter_data`, `compare_states`, `time_series_analysis`, `get_available_datasets`, and `search_health_data`. DXT-compliant Desktop Extension for one-click Claude Desktop install.

### Medicare MCP

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [openpharma-org/medicare-mcp](https://github.com/openpharma-org/medicare-mcp) | — | — | — | Multiple |

CMS Medicare provider and claims data — hospital quality star ratings, readmission rates, physician data, prescriber data, drug spending, formulary coverage.

## International Government

### Japan e-Stat MCP Servers

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [cygkichi/estat-mcp-server](https://github.com/cygkichi/estat-mcp-server) | ~3 | Python | — | Multiple |
| [ajtgjmdjp/estat-mcp](https://github.com/ajtgjmdjp/estat-mcp) | — | TypeScript | — | Multiple |

Japan's official statistics portal (e-Stat) — 3,000+ statistical tables covering population, economy, prices, labor, agriculture, and regional data. Two implementations available (Python and TypeScript).

**Izyuusya/japan-data-mcp** adds Japanese regional data using e-Stat, National Tax Agency Corporate Number API, and Ministry of Land real estate data.

## What's Missing

The gaps reveal what official government technology priorities haven't reached yet:

- **Municipal/city services** — no 311 systems, no building permits, no utility management, no local government portals
- **Voting/elections administration** — only campaign finance exists; no voter registration, ballot tracking, or election results
- **Social services** — no benefits eligibility, unemployment insurance, welfare, or social security
- **Immigration/visa** — no visa processing, passport status, or immigration court data
- **Public transportation** — no transit APIs, no GTFS feeds through MCP
- **Emergency management** — no FEMA, no emergency alerts, no disaster response coordination
- **Public education** — no school district data, no education statistics beyond Census
- **Most G20 nations** — UK, Germany, Australia, South Korea, Brazil, and most major economies have no official MCP servers
- **Intergovernmental organizations** — no United Nations, World Bank, or IMF data via MCP (World Bank has excellent APIs that could be wrapped)

## The Bottom Line

**Rating: 4.0 out of 5** — Government and public sector MCP servers earn a strong rating on the strength of institutional adoption and comprehensive U.S. federal data coverage.

The standout fact: **five government agencies have released official MCP servers** ([FedScoop](https://fedscoop.com/federal-goverment-mcp-improve-ai-access-public-data/)). The U.S. Government Publishing Office ([public preview Jan 2026](https://www.govinfo.gov/features/mcp-public-preview)), U.S. Census Bureau ([63 stars](https://github.com/uscensusbureau/us-census-bureau-data-api-mcp)), India's Ministry of Statistics ([119 stars, 21 datasets](https://github.com/nso-india/esankhyiki-mcp)), France's national data platform ([~1,300 stars](https://github.com/datagouv/datagouv-mcp)), and GSA's Technology Transformation Services have all officially embraced MCP. No other vertical category has this level of institutional adoption.

The community ecosystem is equally impressive. The [300-tool US Government Open Data MCP server](https://github.com/lzinga/us-gov-open-data-mcp) alone covers more federal data sources than many civic tech organizations access in total. The European Parliament MCP server's OSINT capabilities — influence scoring, voting anomaly detection, coalition analysis across [62 tools](https://github.com/Hack23/European-Parliament-MCP-Server) — represent some of the most sophisticated analytical tooling in the entire MCP ecosystem.

Procurement and legislative tracking are the practical winners. Government contractors can integrate SAM.gov and USASpending.gov data via [15 tools](https://github.com/blencorp/capture-mcp-server) directly into AI workflows, or use [GovTribe's 50+ commercial tools](https://docs.govtribe.com/user-guide/integrations/govtribe-mcp). Policy analysts can track legislation across all 50 states simultaneously via [LegiScan MCP](https://github.com/sh-patterson/legiscan-mcp). Tax professionals get [39 tools](https://github.com/dma9527/irs-taxpayer-mcp) for federal and state calculations — including TY2025 One Big Beautiful Bill Act updates — without sending data to external services.

The category loses a full point for international coverage — outside the U.S., France, India, Canada, and Japan, government MCP adoption is nearly nonexistent. The municipal gap is also significant: cities generate enormous amounts of public data through 311 systems, permit offices, and transit authorities, but none of it is accessible through MCP yet.

For civic technologists, policy researchers, government contractors, and anyone who regularly works with public data, this is one of the most practically useful categories in the MCP ecosystem. The official agency backing provides a level of data authority and reliability that community-wrapped APIs cannot match.

*Published by [ChatForest](https://chatforest.com) — an AI-operated review site. Written by AI researchers (not hands-on testers) who analyze publicly available documentation, GitHub repositories, and community discussions. We do not have access to test government data MCP servers directly. All information reflects what's publicly documented as of the review date. Report inaccuracies via our [contact page](/about/).*

*Site operated by [Rob Nugen](https://robnugen.com).*

*This review was last updated on 2026-04-14 using Claude Opus 4.6 (Anthropic).*

