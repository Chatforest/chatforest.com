---
title: "Nonprofit & Charity MCP Servers — Grant Discovery, Donor Management, Humanitarian Data, Charity Verification, Civic Data, and Volunteer Impact"
date: 2026-03-15T14:30:00+09:00
lastmod: 2026-04-27T09:00:00+09:00
description: "Nonprofit and charity MCP servers let AI agents discover grants, look up charity tax status, access donor CRM data, query humanitarian datasets, search civic open data, and measure volunteer impact."
og_description: "Nonprofit & charity MCP servers: grants-mcp (8 stars, government grants), Granted AI (87K+ grants free), us-gov-open-data-mcp (94 stars, 300+ tools 40+ APIs), mcp-civic-data (110 tools 33 APIs), hdx-mcp (7 stars, humanitarian data), Blackbaud/Benevity/Candid connectors, Goodera (volunteer impact). Grant discovery gap filled. 20+→30+ servers. Rating: 3→3.5/5."
content_type: "Review"
card_description: "Nonprofit and charity MCP servers for AI-powered grant discovery, donor management, charity verification, humanitarian data access, civic open data, and social impact measurement. **Grant discovery arrived — the biggest gap is partially filled.** Tar-ive/grants-mcp (8 stars, Python, MIT, 3 tools) searches government grants via the Simpler Grants API with opportunity discovery, agency landscape mapping, and funding trend analysis. Granted AI's free MCP server goes further — 87,000+ searchable grants, 133,000+ foundation profiles, 5 tools, zero authentication required. Neither does grant *writing*, but discovery is no longer absent. **Civic and government open data exploded.** lzinga/us-gov-open-data-mcp (94 stars, TypeScript, MIT) covers 40+ US government APIs with 300+ tools — Treasury, FRED, Congress, FDA, CDC, FEC, lobbying, and more. Featured on Hacker News. EricGrill/mcp-civic-data (2 stars, Python, MIT) provides 110 tools across 33 free APIs including FEMA disasters, CDC health, Census demographics, EPA compliance, and clinical trials. **Anthropic's 'Claude for Nonprofits' still drives commercial integrations** — up to 75% discount on Team/Enterprise, same three connectors (Blackbaud, Benevity, Candid). The broader Claude connector directory grew to 200+ integrations by April 2026. **Charity verification upgraded** — asachs01/propublica-mcp shipped v1.0.0 with MCP 2025-03-26 Streamable HTTP transport and DXT extension format. conorheffron/mcp-charity (3 stars, Python, GPL-3.0) released v1.0.6 on Python 3.14 + fastmcp 3. briancasteel/charity-mcp-server dropped to 2 stars and hasn't been updated since January 2025. **Humanitarian data** — dividor/hdx-mcp (7 stars) added Docker MCP Toolkit support for easier onboarding. **NationBuilder MCP deleted** — mikeomlor/nb-mcp repo removed, user has no public repos. **Goodera-Benevity API integration went live** — streaming volunteer data between platforms. **Remaining gaps** — no grant *writing* assistance, no DonorPerfect/Bloomerang integration, no volunteer scheduling, no open-source impact measurement, CiviCRM still lacks a dedicated MCP server. Rating upgraded 3→3.5/5 — grant discovery and civic open data brought significant new capability, though the open-source nonprofit-specific landscape remains thin."
last_refreshed: 2026-04-27
---

Nonprofit and charity MCP servers let AI assistants discover grants, look up charity tax status, access donor CRM data, query humanitarian datasets, search government open data, discover nonprofit organizations, and measure volunteer impact. Instead of manually searching grant databases, navigating IRS records, compiling humanitarian reports, or cross-referencing government data sources, these servers let AI agents find funding opportunities, verify tax-deductible status, pull giving histories, analyze Form 990 financials, query 40+ federal data APIs, and generate impact reports — all through the Model Context Protocol.

This review covers the **nonprofit and charity** vertical — grant discovery, charity verification and IRS data, donor management CRMs, nonprofit discovery platforms, humanitarian data, civic and government open data, volunteer impact measurement, and civic engagement tools. For general CRM servers, see our [CRM MCP review](/reviews/crm-mcp-servers/). For Salesforce-specific coverage, see the [Salesforce section in our CRM review](/reviews/crm-mcp-servers/).

The headline findings: **Grant discovery arrived** — Tar-ive/grants-mcp (government grants) and Granted AI (87K+ grants, 133K+ foundations, free) fill the biggest gap from our original review. **Civic open data exploded** — us-gov-open-data-mcp (94 stars, 300+ tools across 40+ federal APIs) and mcp-civic-data (110 tools, 33 APIs) bring massive government data access. **Anthropic's "Claude for Nonprofits" still drives commercial integrations** with 75% discounts and three connectors. **Humanitarian data remains strong** with HDX MCP now on Docker MCP Toolkit. **Donor management is still entirely commercial.** **NationBuilder MCP was deleted.**

**Category:** [Government & Legal](/categories/government-legal/)

---

## Grant Discovery *(new section)*

### Tar-ive/grants-mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [Tar-ive/grants-mcp](https://github.com/Tar-ive/grants-mcp) | 8 | Python | MIT | 3 |

**The first open-source grant discovery MCP server** — filling the biggest gap from our original review. Powered by the Simpler Grants API for US government grants:

- **opportunity_discovery** — search and filter grants by keywords, agencies, funding categories, and eligibility criteria
- **agency_landscape** — map government agencies and their funding focus areas with opportunity analysis
- **funding_trend_scanner** — analyze historical funding patterns and identify emerging opportunities

Built with FastMCP. Dual transport support (stdio + HTTP). Docker/Docker Compose ready with cloud deployment guides (Google Cloud Run, AWS ECS). Intelligent caching with configurable TTL. 56 commits on main. Phase 3 (containerization) complete; upcoming phases include intelligent scoring, multi-agency tools, and grant application assistance. Grant *writing* is not yet implemented, but discovery is no longer absent.

### Granted AI MCP Server

| Server | Type | Tools |
|--------|------|-------|
| [Granted AI MCP](https://grantedai.com/mcp) | Commercial (free, no auth) | 5 |

The **most comprehensive grant discovery MCP server available** — and it's completely free with no API keys or account creation required:

- **search_grants** — query across 87,000+ grants by keyword, topic, funder, or eligibility
- **get_grant** — complete details for specific grant opportunities
- **search_funders** — explore 133,000+ foundation profiles by name, location, or giving focus
- **get_funder** — foundation profiles with financials and grant history
- **get_past_winners** — federal grant recipients for competitive intelligence

Uses Granted's AI-powered discovery pipeline with live web search and 15-feature grant scoring. Streamable HTTP + SSE transport. Works with Claude Desktop, Cursor, and any MCP-compatible client. Setup takes under a minute. This is the stronger of the two grant discovery options — the 133K+ foundation profiles and past winners data give nonprofits genuine research capability that previously required expensive databases like Foundation Directory Online.

## Charity Verification & Data Lookup

### briancasteel/charity-mcp-server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [briancasteel/charity-mcp-server](https://github.com/briancasteel/charity-mcp-server) | 2 | TypeScript | MIT | 4 |

Provides IRS-based charity verification through CharityAPI.org:

- **EIN lookup** — verify any US nonprofit by Employer Identification Number
- **Tax-deductible status** — confirm 501(c)(3) and other tax-exempt classifications
- **Organization search** — find nonprofits by name and filter results
- **Guided research** — 14 prompt templates for structured charity investigation workflows

Uses stdio transport. Requires a CHARITY_API_KEY environment variable from CharityAPI.org. TypeScript with full type safety and comprehensive error handling. *Note: Stars dropped from 22 to 2 since our March review, and the last commit was January 2025. This project appears inactive.*

### asachs01/propublica-mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [asachs01/propublica-mcp](https://github.com/asachs01/propublica-mcp) | 1 | Python | — | 5 |

Accesses **ProPublica's Nonprofit Explorer API** for Form 990 data — the gold standard for US nonprofit financial transparency:

- **search_nonprofits** — find organizations by name and location
- **get_organization** — detailed nonprofit profile with mission, revenue, assets
- **get_organization_filings** — historical Form 990 filings with financial details
- **analyze_nonprofit_financials** — multi-year trend analysis of revenue, expenses, and assets
- **search_similar_nonprofits** — discover comparable organizations by NTEE code and geography

**Updated to v1.0.0** with MCP 2025-03-26 Streamable HTTP transport (breaking change — single `/` endpoint replaces separate `/sse` and `/messages` endpoints). New DXT extension format for easier installation. Docker, DigitalOcean, and Cloudflare Workers deployment options. 58 commits. Works with Claude Desktop and Cursor.

### conorheffron/mcp-charity

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [conorheffron/mcp-charity](https://github.com/conorheffron/mcp-charity) | 3 | Python | GPL-3.0 | 1 |

A **sample/demonstration MCP server** for charity search. Includes a `query_charities` tool to search by name, location, and cause. **Updated to v1.0.6** (April 4, 2026) — now running Python 3.14 + fastmcp 3 with HTTP endpoints. 64 commits. More of a learning project than a production tool, but actively maintained.

## Donor Management & Fundraising CRM

### Blackbaud Claude Connector (Official)

| Server | Type | Tools |
|--------|------|-------|
| [Blackbaud Connector](https://claude.com/connectors/blackbaud) | Claude Connector (commercial) | 4 |

The **first major nonprofit CRM to offer native MCP integration**, announced December 2025 as a partnership between Blackbaud and Anthropic. Connects to Raiser's Edge NXT — the dominant fundraising CRM used by thousands of nonprofits:

- **Get Constituent Profiles** — donor contact information, demographics, engagement history
- **Find/View Events** — fundraising event records, attendance, revenue
- **View Gifts** — giving history, donation amounts, recurring gift status
- **Generate Communications** — AI-drafted thank-you notes and outreach emails referencing actual donor data

No code required — works as a Claude Connector for "Claude for Nonprofits" users. This is significant because Blackbaud controls roughly 40% of the nonprofit CRM market. The ability to query donor data and draft personalized communications through natural language is a genuine productivity gain for development officers.

### CData MCP Server for Blackbaud

| Server | Type | Tools |
|--------|------|-------|
| [CData Blackbaud MCP](https://cdn.cdata.com/help/JZK/mcp/) | Commercial | Multiple |

CData's commercial offering exposes Raiser's Edge NXT data as MCP tools with natural language query support. Part of CData's broader MCP server product line. Built-in authentication flow. An alternative to the official Blackbaud Connector for organizations that want more granular data access or already use CData for other integrations.

### Salesforce MCP (for Nonprofit Cloud / NPSP)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [salesforcecli/mcp](https://github.com/salesforcecli/mcp) | — | TypeScript | — | Multiple |

While not nonprofit-specific, **Salesforce's official MCP server** (Developer Preview, announced June 2025) works with Salesforce Nonprofit Cloud and NPSP instances. SOQL queries, CRUD operations, metadata management, and Apex execution — meaning any data in a nonprofit's Salesforce org is accessible. Five or more community implementations exist as well (tsmztech, AiondaDotCom, LokiMCPUniverse, advancedcommunities, and others).

Over 40,000 nonprofits use Salesforce. If your organization is already on Salesforce NPSP or Nonprofit Cloud, these MCP servers give you immediate AI access to your donor, program, and volunteer data.

### CiviCRM via Pipedream

| Server | Type | Tools |
|--------|------|-------|
| [CiviCRM MCP (Pipedream)](https://mcp.pipedream.com/app/civicrm) | Hosted (Pipedream) | Multiple |

**CiviCRM is the leading open-source CRM for nonprofits** — used by the Free Software Foundation, Creative Commons, Wikimedia Foundation, and CERN, with 14,000+ organizations worldwide. Pipedream wraps CiviCRM's API as MCP tools with managed authentication.

Not a standalone open-source MCP server, but a practical integration path for the thousands of nonprofits running CiviCRM. The fact that the most widely-used open-source nonprofit CRM lacks a dedicated MCP server is one of this category's biggest gaps — a well-built CiviCRM MCP server would serve a large audience.

## Nonprofit Discovery & Donation

### Benevity MCP (Claude Connector)

| Server | Type | Tools |
|--------|------|-------|
| [Benevity MCP](https://causeshelp.benevity.org/hc/en-us/articles/43364091494164) | Claude Connector (commercial) | 3 |

Access to **2.4 million+ verified nonprofit organizations worldwide**:

- **Nonprofit search** — find organizations by cause, interest, location, or name
- **Organization details** — mission, programs, verified status
- **Donation links** — verified links to each nonprofit's donation page

Returns up to 10 results per query. No PII shared — all data is public information. Available for Claude Pro users. Part of the "Claude for Nonprofits" initiative. Benevity powers corporate giving programs for many Fortune 500 companies, so their nonprofit database is exceptionally comprehensive and well-maintained.

### Candid MCP Connector (Free)

| Server | Type | Tools |
|--------|------|-------|
| [Candid MCP](https://claude.com/connectors/candid) | Claude Connector (free) | 3 |

**Free to use** — the most accessible nonprofit data connector in the MCP ecosystem:

- **Organization search** — find nonprofits and foundations by name, mission, location, and leadership demographics
- **Profile linking** — automatic links to official Candid (formerly GuideStar) profiles
- **Knowledge access** — Candid's research reports, training materials, and sector analysis

Announced on GivingTuesday. Candid's data comes from primary sources (IRS filings, nonprofit self-reports) and is widely trusted in the philanthropic sector. The leadership demographics search is unique — you can find organizations led by specific demographic groups, which is valuable for equity-focused grantmaking.

## Volunteer Impact & Social Good

### Goodera MCP Server

| Server | Type | Tools |
|--------|------|-------|
| [Goodera MCP](https://www.goodera.com/blog/goodera-launches-mcp-server) | Commercial (hosted) | Multiple |

Self-described as the **"first social impact company to launch an MCP server."** Provides real-time volunteering and impact data:

- **Scale** — data from 50,000+ nonprofit partners, 25,000+ events, 2M+ volunteers, 1,000+ cities
- **Impact reporting** — instant generation of impact reports from volunteering program data
- **Geographic analysis** — trend analysis for volunteering opportunities by region
- **Integrations** — connects with Canva, Box, Slack, Microsoft Teams, Tableau

Enterprise-grade security with no PII exposure. All queries are traceable for compliance. This is the only MCP server we've found focused specifically on volunteer program management and social impact measurement at scale.

## Humanitarian Data & Aid

### dividor/hdx-mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [dividor/hdx-mcp](https://github.com/dividor/hdx-mcp) | 7 | Python | MIT | 33+ |

The **standout open-source server in this entire category**. Accesses the UN OCHA Humanitarian Data Exchange — one of the most important humanitarian data platforms in the world:

- **Refugees & displacement** — refugee populations, internally displaced persons (IDPs), returnee data by country
- **Demographics** — baseline population data across hundreds of countries
- **Food security** — food security indicators and crisis-level assessments
- **Conflict** — conflict event data with location, type, and casualties
- **Funding** — humanitarian funding flows, appeals, and operational presence
- **Auto-generated tools** — 33 tools generated from HDX's OpenAPI specification
- **Custom tools** — 3 additional tools: `hdx_server_info`, `hdx_get_dataset_info`, `hdx_search_locations`

Docker deployment supported via Docker Desktop's MCP Toolkit (v4.43+) for streamlined onboarding. Also deployable via UV or direct Claude Desktop integration. Requires an HDX API app identifier (free). The breadth is remarkable — with 33+ tools covering the full spectrum of humanitarian data, this server could genuinely accelerate research, reporting, and coordination for aid organizations. Written up on Medium by the author with detailed implementation notes.

### Humanitarian Negotiation MCP

| Server | Type | Tools |
|--------|------|-------|
| [humanitarian-mcp](https://glama.ai/mcp/servers/@escenariosparalatransformacion/humanitarian-mcp) | Open source | 4 |

A **highly specialized server** for humanitarian negotiators, mediators, and aid workers:

- **Island of Agreement** — identify contested vs. agreed-upon facts between parties
- **Iceberg & Common Shared Space** — reveal hidden positions, motivations, and shared ground
- **Stakeholder Analysis** — map and prioritize stakeholders with influence assessments
- **Leverage Analysis** — develop strategic engagement plans with leverage point identification

Not a data server but a structured analytical framework. Useful for organizations negotiating access to conflict zones, coordinating with governments, or mediating between humanitarian actors. One of the most niche MCP servers we've reviewed in any category.

## Civic & Government Open Data *(new section)*

### lzinga/us-gov-open-data-mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [lzinga/us-gov-open-data-mcp](https://github.com/lzinga/us-gov-open-data-mcp) | 94 | TypeScript | MIT | 300+ |

**The largest government data MCP server by far** — 300+ tools covering 40+ US federal data APIs. Featured on Hacker News. Created February 2026, v2026.4.11:

- **Economic** — Treasury fiscal data, FRED economic indicators, BLS labor statistics
- **Legislative** — Congress.gov bills and votes, Federal Register regulations
- **Financial** — FEC campaign finance, SEC filings, FDIC banking data
- **Health & Safety** — CDC disease surveillance, FDA recalls, CMS healthcare costs, NIH clinical trials
- **Environment** — EPA compliance, NOAA weather, USGS water/earthquakes
- **Plus** — Education, Energy, Housing, Patents, Transportation, Lobbying, and more

Available via NPM as `us-gov-open-data-mcp`. Dual transport (stdio + HTTP Stream). WASM-sandboxed JavaScript execution reduces context window usage by 98-100% for large responses. Selective module loading — load only the APIs you need. Disk-backed caching with rate limiting and retry logic. 20+ APIs require no key; the rest use free keys. Also usable as a standalone TypeScript SDK without MCP. This server is valuable for any nonprofit doing policy research, advocacy, or grant applications that require federal data.

### EricGrill/mcp-civic-data

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [EricGrill/mcp-civic-data](https://github.com/EricGrill/mcp-civic-data) | 2 | Python | MIT | 110 |

**110 tools across 33 free, authoritative public data APIs** — focused on environmental, health, economic, and government data. Python 3.11+, pip installable:

- **Environmental** — NOAA weather, OpenAQ air quality, USGS water, wildfires, space weather, EPA compliance
- **Health** — CDC public health, clinical trials, CMS healthcare costs, FDA data
- **Emergency** — FEMA disaster declarations, CISA cybersecurity advisories
- **Demographics** — Census data, education statistics
- **Economics** — BLS data, energy, agriculture, transportation, finance
- **Open Data Catalogs** — Data.gov, EU Open Data, NASA FIRMS

22 of the 33 APIs require no keys at all. Includes CI/CD, contributing guidelines, and security policy. 142 commits. While overlapping with us-gov-open-data-mcp in some areas, this server uniquely covers EU Open Data, Safecast radiation, and CISA cybersecurity — useful for international nonprofits.

## Civic Engagement & Advocacy

### NationBuilder MCP *(removed)*

The previously listed mikeomlor/nb-mcp NationBuilder MCP server has been **deleted** — the repository no longer exists and the author has no public repos. NationBuilder remains accessible via Pipedream and Zapier MCP wrappers, but there is no longer a standalone open-source NationBuilder MCP server.

## Platform-Aggregated Access

Several nonprofit platforms lack dedicated MCP servers but are accessible through integration platform wrappers:

| Platform | Via | Use Case |
|----------|-----|----------|
| **Donorbox** | Zapier MCP | Fundraising, donation management |
| **Givebutter** | Zapier/Pipedream MCP | Free fundraising platform ($150M+ in donations processed) |
| **Little Green Light** | Zapier MCP | Donor management CRM for small nonprofits |
| **NationBuilder** | Pipedream/Zapier MCP | Community management, advocacy (standalone MCP deleted) |
| **CiviCRM** | Pipedream MCP | Open-source nonprofit CRM |

These are not standalone MCP servers — they're API wrappers that expose platform actions as MCP tools through Zapier's or Pipedream's MCP integration layer. They work, but you're adding a dependency on a third-party integration platform.

## What's Missing

The nonprofit MCP space has narrowed its gaps but several remain:

- **Grant writing & application management** — grant *discovery* is now covered (grants-mcp, Granted AI), but no server helps with grant *writing*, application tracking, or compliance reporting
- **DonorPerfect / Bloomerang** — two major nonprofit CRMs still have no MCP integration of any kind
- **CiviCRM dedicated MCP** — the most widely-used open-source nonprofit CRM (FSF, Creative Commons, Wikimedia, CERN, 14K+ orgs) still has no standalone MCP server — only Pipedream wrapper access
- **Volunteer scheduling** — no tool for shift management, skill matching, or availability coordination
- **Impact measurement frameworks** — no open-source server implementing Theory of Change, logic models, or standardized outcome metrics (Goodera is commercial only)
- **Nonprofit accounting** — no integration with Fund Accounting systems (Sage Intacct, Blackbaud Financial Edge)
- **Peer-to-peer fundraising** — no MCP server for crowdfunding campaign management
- **GuideStar / Charity Navigator ratings** — no direct MCP access to charity rating data (Candid provides profiles but not the rating systems themselves)

## Rating: 3.5/5

**What works:** Grant discovery arrived — Granted AI's free MCP (87K+ grants, 133K+ foundations) and Tar-ive/grants-mcp (government grants) fill what was the biggest gap. Civic open data exploded with us-gov-open-data-mcp's 300+ tools across 40+ federal APIs — any nonprofit doing policy research, advocacy, or federal grant applications now has exceptional data access. Anthropic's "Claude for Nonprofits" initiative continues to bring major platforms in with 75% discounts. HDX humanitarian data remains the open-source crown jewel. ProPublica MCP upgraded to Streamable HTTP transport. The Claude connector directory grew to 200+ integrations.

**What doesn't:** The open-source *nonprofit-specific* landscape is still thin — charity-mcp-server appears abandoned (2 stars, no commits since Jan 2025), and the NationBuilder MCP was deleted entirely. CiviCRM (14K+ orgs) still has no dedicated MCP server. No grant *writing* assistance exists. DonorPerfect and Bloomerang remain unconnected. Volunteer scheduling and open-source impact measurement are still absent.

**What changed since March 2026:** Grant discovery (2 new servers), civic/government data (2 major new servers with 300+ and 110 tools respectively), propublica-mcp v1.0.0 with Streamable HTTP, mcp-charity v1.0.6 on Python 3.14, HDX added Docker Toolkit support, NationBuilder MCP deleted, charity-mcp-server went inactive. Net: 15+→30+ servers, significant new capability in grant discovery and civic data.

**Who should care:** Nonprofit development officers who want AI-assisted donor communications and grant research, policy researchers and advocates needing federal data access, humanitarian data analysts working with UN OCHA data, charity evaluators needing quick IRS and Form 990 lookups, and anyone building AI tools for the social impact sector.

**Bottom line:** The category shifted from "commercial connectors plus thin open-source" to a more balanced landscape. Grant discovery and civic open data brought the strongest new open-source contributions — us-gov-open-data-mcp (94 stars) is now the highest-starred server touching this vertical. The commercial side (Blackbaud, Benevity, Candid, Goodera, Granted AI) remains polished. The remaining frontier: grant writing, CiviCRM, volunteer scheduling, and impact measurement.

*This review was refreshed on 2026-04-27 using Claude Opus 4.6 (Anthropic). Original review: 2026-03-15.*
