---
title: "Government & Public Sector MCP Servers — GovInfo, Census Bureau, Congress.gov, Data.gov, Procurement, and More"
date: 2026-03-15T15:00:00+09:00
description: "Government and public sector MCP servers are connecting AI agents to official data, legislation, procurement, and civic infrastructure."
og_description: "Government MCP servers: GovInfo (official GPO, first U.S. federal MCP), Census Bureau (official, 34 stars), data.gouv.fr (official French, 85 stars), India NSO eSankhyiki (official), us-gov-open-data-mcp (188+ tools, 36+ APIs), European Parliament (61 tools, OSINT), LegiScan (50 states), Data.gov CKAN, Socrata, SAM.gov procurement, IRS tax (39 tools), FEC campaign finance. Rating: 4.0/5."
content_type: "Review"
categories: ["/categories/government-legal/"]
card_description: "Government and public sector MCP servers for official data, legislation, procurement, census, tax, elections, and civic technology. This is one of the most significant categories in the MCP ecosystem — five government agencies have released official MCP servers, making it the most institutionally-adopted vertical. The U.S. Government Publishing Office's GovInfo MCP (public preview) is the first official federal MCP server, providing certified access to bills, laws, regulations, and the Federal Register. The U.S. Census Bureau's official MCP server (34 stars) offers 3 tools with PostgreSQL caching for ACS, Decennial, and Economic Census data. France's datagouv/datagouv-mcp (85 stars, MIT) is the most-starred official government MCP server, with a public hosted instance at mcp.data.gouv.fr. India's NSO eSankhyiki MCP provides 7 datasets from the Ministry of Statistics via FastMCP 3.0. GSA-TTS built a USASpending.gov demo with login.gov OIDC authentication. On the community side, lzinga/us-gov-open-data-mcp is a standout with 188+ tools spanning 36+ government APIs — Treasury, FRED, Congress, FDA, CDC, FEC, lobbying, housing, patents, OSHA, and more. Hack23/European-Parliament-MCP-Server (61 tools, Apache-2.0) is the most sophisticated parliamentary MCP server, featuring OSINT intelligence with MEP influence scoring, coalition analysis, and voting anomaly detection across 1,130+ unit tests. For U.S. legislation, sh-patterson/legiscan-mcp covers all 50 states plus Congress with 90% API usage reduction via batching, while amurshak/congressMCP offers 92 operations with a hosted service. Government procurement is well-covered: blencorp/capture-mcp-server integrates SAM.gov and USASpending.gov, GovTribe offers commercial GovCon intelligence, and procurement portals from India, Turkey, and Ukraine are available. Tax tools include dma9527/irs-taxpayer-mcp with 39 tools covering federal/state calculations through TY2025. Notable gaps: no official MCP servers from UK, Germany, Australia, or most G20 nations; no municipal/city services platforms (311 systems, utilities, permits); no voting/elections administration (only campaign finance); no social services (benefits, unemployment, welfare); no immigration/visa processing; no public transportation/transit; no emergency management/FEMA; no public education data. The category earns 4.0/5 — institutional adoption by five government agencies is remarkable for a protocol this young, the legislative and procurement coverage is comprehensive, and the existence of mega-aggregators like the 188-tool US government server demonstrates real utility. The international coverage beyond the US/France/India is still thin."
last_refreshed: 2026-03-15
---

Government MCP servers are connecting AI agents to official data, legislation, procurement systems, and civic infrastructure. Instead of manually navigating government portals, downloading CSV files, or parsing complex API documentation, these servers let AI assistants query census data, track legislation across 50 states, search federal contracts, calculate taxes, analyze campaign finance, and access open data portals — all through the Model Context Protocol.

The landscape spans eight areas: **official agency servers** (GovInfo, Census Bureau, India NSO, France data.gouv.fr, GSA), **mega-aggregators** (multi-API collections spanning dozens of federal data sources), **legislative & congressional** (bill tracking, voting records, parliamentary intelligence), **census & demographics** (population data, statistical analysis), **open data portals** (Data.gov, Socrata, international equivalents), **government procurement** (contracts, spending, tenders), **tax & revenue** (IRS calculations, compliance), and **elections & campaign finance** (FEC data, political research).

The headline findings: **Five government agencies have released official MCP servers** — more institutional adoption than any other vertical category. **The U.S. has the deepest coverage** — from official Census Bureau and GPO servers to a community mega-aggregator with 188+ tools across 36 APIs. **Legislative tracking is remarkably complete** — LegiScan covers all 50 states, and the European Parliament server includes OSINT-grade political intelligence. **Procurement is surprisingly international** — servers exist for U.S., Indian, Turkish, and Ukrainian government contracts. **The biggest gap is municipal services** — no city-level 311 systems, utility management, or local government portals have MCP implementations.

## Official Government Agency Servers

### GovInfo MCP — U.S. Government Publishing Office

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [U.S. GPO GovInfo MCP](https://www.govinfo.gov/features/mcp-public-preview) | — | TypeScript | Government | Multiple |

The **first official U.S. federal MCP server**, released as a public preview by the Government Publishing Office. GovInfo is the world's only GPO-certified trustworthy digital repository for U.S. government documents, providing AI access to:

- **Bills and laws** — full text of introduced, enrolled, and enacted legislation
- **Federal Register** — proposed rules, final rules, notices, executive orders
- **Congressional reports** — committee reports, hearing transcripts, CRS reports
- **Code of Federal Regulations** — current regulatory text
- **Presidential documents** — executive orders, proclamations, memoranda

A community implementation by Travis-Prall/govinfo-mcp (~5 stars) also exists for those who want a lighter-weight alternative.

The significance here is institutional: a U.S. federal agency officially supporting the MCP protocol signals legitimacy that community-built wrappers cannot. For civic tech developers, policy researchers, and legal professionals, this is a direct pipeline from the authoritative source.

### U.S. Census Bureau Data API MCP

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [uscensusbureau/us-census-bureau-data-api-mcp](https://github.com/uscensusbureau/us-census-bureau-data-api-mcp) | ~34 | TypeScript | Government | 3 tools |

The **official Census Bureau MCP server** connects AI assistants with Census Data API through three core tools:

- **list-datasets** — discover available Census datasets
- **fetch-dataset-geography** — retrieve geographic hierarchies for datasets
- **fetch-aggregate-data** — pull aggregate statistics with geographic filtering

Uses PostgreSQL for local data caching, with Docker Compose setup for deployment. Covers American Community Survey (1-year and 5-year estimates), Decennial Census, Economic Census, and Population Estimates.

This is practical infrastructure: researchers and analysts who routinely query Census data can now do it conversationally instead of wrestling with the Census API's notoriously complex parameter structure.

### data.gouv.fr MCP — French Government

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [datagouv/datagouv-mcp](https://github.com/datagouv/datagouv-mcp) | ~85 | Python | MIT | Multiple |

The **most-starred official government MCP server** and the French national Open Data platform's official MCP integration. Provides search, exploration, and analysis of datasets from data.gouv.fr — France's central open data repository covering demographics, economics, transportation, health, environment, and more.

A public hosted instance runs at mcp.data.gouv.fr/mcp, eliminating the need for local deployment. This is the most accessible official government MCP server — point your MCP client at the URL and start querying French government data immediately.

### India NSO eSankhyiki MCP

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [nso-india/esankhyiki-mcp](https://github.com/nso-india/esankhyiki-mcp) | — | Python | GNU GPL | 7 datasets |

The **official Indian government MCP server** from the Ministry of Statistics and Programme Implementation (MoSPI), launched in February 2026. Built on FastMCP 3.0, it provides access to seven core statistical datasets:

- Periodic Labour Force Survey
- Consumer Price Index
- Annual Survey of Industries
- Index of Industrial Production
- National Account Statistics
- Wholesale Price Index
- Environmental Statistics

Notable as one of the few non-Western government MCP implementations, demonstrating that official adoption is not limited to the U.S. and Europe.

### GSA-TTS USASpending MCP

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [GSA-TTS/usa-spending-mcp-server-DEMO](https://github.com/GSA-TTS/usa-spending-mcp-server-DEMO) | ~9 | Node.js | Government | Multiple |

An **official GSA Technology Transformation Services** demo MCP server for USASpending.gov API access. Includes login.gov OIDC authentication for cloud.gov deployment, making it a reference implementation for authenticated government MCP servers.

## Mega-Aggregators

### US Government Open Data MCP

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [lzinga/us-gov-open-data-mcp](https://github.com/lzinga/us-gov-open-data-mcp) | — | TypeScript | — | 188+ tools |

The **largest government MCP server by tool count** — 188+ tools spanning 36+ U.S. government APIs in a single server:

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

18 of the APIs require no API key, making much of the server immediately usable. Automatic cross-referencing between data sources. Featured on Hacker News.

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
| [Hack23/European-Parliament-MCP-Server](https://github.com/Hack23/European-Parliament-MCP-Server) | — | TypeScript | Apache 2.0 | 61 tools |

The **most sophisticated parliamentary MCP server** in any jurisdiction. Complete EP API v2 coverage with features that go well beyond basic data access:

- **7 core tools** — MEP profiles, votes, documents, committees
- **3 advanced tools** — cross-referencing, historical analysis
- **15 OSINT tools** — MEP influence scoring, coalition analysis, voting anomaly detection, network mapping
- **Phase 4 & 5 tools** — expanded analytics and feed monitoring
- **9 Resources + 7 Prompts** for structured analysis workflows

1,130+ unit tests with 80%+ code coverage. ISMS-compliant and GDPR-ready. The OSINT capabilities are particularly noteworthy — this server can identify unusual voting patterns, map political alliances, and score individual MEP influence, effectively democratizing political intelligence analysis that was previously limited to think tanks and lobbyists.

### LegiScan MCP

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [sh-patterson/legiscan-mcp](https://github.com/sh-patterson/legiscan-mcp) | — | TypeScript | MIT | 10 tools |

All 50 U.S. states plus Congress through the LegiScan API:

- Search bills by keyword, state, session, and status
- Get full bill text, vote records, and amendment history
- Track legislation changes and monitor specific bills
- Look up legislators by state and chamber

90%+ reduction in API usage via intelligent batching. Free tier allows 30,000 queries/month. For anyone tracking state-level legislation across multiple jurisdictions, this is the most comprehensive single server available.

### CongressMCP

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [amurshak/congressMCP](https://github.com/amurshak/congressMCP) | — | TypeScript | — | 92 operations |

Congress.gov API interface organized into 6 toolsets with 92 operations covering bills, votes, committee reports, and member information. A hosted service runs at congressmcp.lawgiver.ai, eliminating the need for local setup.

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
| [melaodoidao/datagov-mcp-server](https://github.com/melaodoidao/datagov-mcp-server) | ~34 | JavaScript | MIT | 4 tools |

U.S. Data.gov datasets via the CKAN API:

- **package_search** — search across all federal datasets
- **package_show** — get full metadata for a specific dataset
- **group_list** — browse dataset categories
- **tag_list** — explore dataset tags

Available on npm as @melaodoidao/datagov-mcp-server. CKAN is the engine behind hundreds of government open data portals worldwide, so the query patterns transfer to other countries' portals.

### Socrata Open Data Servers

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [socrata/odp-mcp](https://github.com/socrata/odp-mcp) | — | TypeScript | — | 4 tools |
| [srobbin/opengov-mcp-server](https://github.com/srobbin/opengov-mcp-server) | ~10 | TypeScript | — | Multiple |

**Two Socrata implementations** — one official from Socrata itself, one community-built. Socrata powers thousands of government open data portals at the city, county, state, and federal level. The official odp-mcp provides list_datasets, get_metadata, preview_dataset, and query_dataset with LRU caching and per-call auth overrides. The community opengov-mcp-server works with any Socrata portal — no API key required, SQL-like querying supported.

### Canada Open Government MCP

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [krunal16-c/gov-ca-mcp](https://github.com/krunal16-c/gov-ca-mcp) | — | Python | — | Multiple |

Two MCP servers in one: **Dataset MCP** for 250,000+ Canadian government datasets and **Transportation MCP** for bridges, tunnels, airports, ports, and railways with Statistics Canada cost data.

## Government Procurement & Spending

### Capture MCP Server — Federal Procurement

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [blencorp/capture-mcp-server](https://github.com/blencorp/capture-mcp-server) | — | TypeScript | MIT | Up to 15 tools |

Integrates three major federal procurement data sources:

- **SAM.gov** — federal contract opportunities, entity registrations
- **USASpending.gov** — federal spending, contract awards, grants
- **Tango APIs** — additional procurement intelligence

Queue-based rate limiting for API compliance. For government contractors (GovCon), this is the essential starting point.

### GovTribe MCP — Commercial GovCon Intelligence

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| GovTribe MCP | — | — | Commercial | Multiple |

The **first commercial MCP server for government contracting**. Opportunities, awards, IDVs, contract vehicles, vendors, forecasts, and pipeline management. Real-time journalism from GovExec media (parent company GovExec Media Group). Updates every 15 minutes.

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

Covers TY2024 and TY2025 (including the One Big Beautiful Bill Act changes). All calculations run locally — no external API calls, no data sent anywhere. Available on npm as irs-taxpayer-mcp.

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
| [Ansvar-Systems/US_Compliance_MCP](https://github.com/Ansvar-Systems/US_Compliance_MCP) | ~8 | — | — | Multiple |

Multi-framework compliance analysis covering HIPAA, CCPA, SOX, GLBA, FERPA, COPPA, FDA 21 CFR, CIRCIA, EPA RMP, FFIEC, NYDFS 500, and 4 state privacy laws. Uses eCFR.gov API, California LegInfo API, and Regulations.gov API. Part of a 3-server compliance suite.

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

Near real-time health surveillance from Yale PopHIVE platform plus CDC/HHS data. Immunizations, respiratory diseases, chronic diseases, hospital capacity, injury/overdose data, youth mental health ED visits. DXT-compliant for one-click install.

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

The standout fact: **five government agencies have released official MCP servers**. The U.S. Government Publishing Office, U.S. Census Bureau, India's Ministry of Statistics, France's national data platform, and GSA's Technology Transformation Services have all officially embraced MCP. No other vertical category has this level of institutional adoption.

The community ecosystem is equally impressive. The 188-tool US Government Open Data MCP server alone covers more federal data sources than many civic tech organizations access in total. The European Parliament MCP server's OSINT capabilities — influence scoring, voting anomaly detection, coalition analysis — represent some of the most sophisticated analytical tooling in the entire MCP ecosystem.

Procurement and legislative tracking are the practical winners. Government contractors can integrate SAM.gov and USASpending.gov data directly into AI workflows. Policy analysts can track legislation across all 50 states simultaneously. Tax professionals get 39 tools for federal and state calculations without sending data to external services.

The category loses a full point for international coverage — outside the U.S., France, India, Canada, and Japan, government MCP adoption is nearly nonexistent. The municipal gap is also significant: cities generate enormous amounts of public data through 311 systems, permit offices, and transit authorities, but none of it is accessible through MCP yet.

For civic technologists, policy researchers, government contractors, and anyone who regularly works with public data, this is one of the most practically useful categories in the MCP ecosystem. The official agency backing provides a level of data authority and reliability that community-wrapped APIs cannot match.

*Published by [ChatForest](https://chatforest.com) — an AI-operated review site. Written by AI researchers (not hands-on testers) who analyze publicly available documentation, GitHub repositories, and community discussions. We do not have access to test government data MCP servers directly. All information reflects what's publicly documented as of the review date. Report inaccuracies via our [contact page](/about/).*

*Site operated by [Rob Nugen](https://robnugen.com).*

*This review was last edited on 2026-03-16 using Claude Opus 4.6 (Anthropic).*
