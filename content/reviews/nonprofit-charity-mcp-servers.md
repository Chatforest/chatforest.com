---
title: "Nonprofit & Charity MCP Servers — Donor Management, Humanitarian Data, Charity Verification, and Volunteer Impact"
date: 2026-03-15T14:30:00+09:00
description: "Nonprofit and charity MCP servers let AI agents look up charity tax status, access donor CRM data, query humanitarian datasets, and measure volunteer impact. We found 15+ servers across 7 subcategories. Charity Verification: briancasteel/charity-mcp-server (22 stars, TypeScript, MIT — IRS EIN lookup, tax-deductible status), asachs01/propublica-mcp (ProPublica Nonprofit Explorer, Form 990 data, financial trend analysis). Donor Management: Blackbaud Claude Connector (official Raiser's Edge NXT integration, donor profiles, giving history, event records), CData Blackbaud MCP (commercial, natural language queries). Nonprofit CRM: Salesforce MCP (official + 5+ community implementations, works with NPSP/Nonprofit Cloud), CiviCRM via Pipedream (14,000+ nonprofit orgs use CiviCRM). Nonprofit Discovery: Benevity MCP (2.4M+ verified nonprofits worldwide), Candid MCP (funder search, leadership demographics, free). Volunteer Impact: Goodera MCP (50,000+ nonprofit partners, 2M+ volunteers, impact reporting). Humanitarian: dividor/hdx-mcp (33 tools, Python, MIT — UN OCHA Humanitarian Data Exchange, refugees, food security, conflict data). Civic Engagement: mikeomlor/nb-mcp (NationBuilder API, community management). Gaps: no grant writing/management server, no DonorPerfect or Bloomerang integration, no standalone volunteer scheduling. Rating: 3/5."
og_description: "Nonprofit & charity MCP servers: charity-mcp-server (22 stars, IRS lookup), propublica-mcp (Form 990 data), Blackbaud connector (donor CRM), Benevity (2.4M nonprofits), hdx-mcp (33 tools, humanitarian data), Goodera (volunteer impact). 15+ servers across 7 categories. Rating: 3/5."
content_type: "Review"
card_description: "Nonprofit and charity MCP servers for AI-powered donor management, charity verification, humanitarian data access, and social impact measurement. This category is shaped by Anthropic's 'Claude for Nonprofits' initiative more than any organic open-source movement. **Charity verification has two solid open-source options** — briancasteel/charity-mcp-server (22 stars, TypeScript, MIT) does IRS EIN lookups with tax-deductible status verification and guided research workflows, while asachs01/propublica-mcp accesses ProPublica's Nonprofit Explorer for Form 990 data with financial trend analysis across multiple years and similar organization discovery. **Donor management is dominated by commercial integrations** — Blackbaud's official Claude Connector (announced December 2025) connects to Raiser's Edge NXT for constituent profiles, giving history, event records, and AI-drafted thank-you notes. CData offers a separate commercial MCP for Blackbaud with natural language query support. **Salesforce MCP servers work for nonprofits** — while not nonprofit-specific, the official Salesforce DX MCP and 5+ community implementations can connect to Salesforce NPSP/Nonprofit Cloud instances, giving the 40,000+ nonprofits on Salesforce an MCP integration path. CiviCRM (used by FSF, Creative Commons, Wikimedia, CERN) is accessible via Pipedream MCP. **Nonprofit discovery platforms are well-served** — Benevity's MCP provides access to 2.4M+ verified nonprofits worldwide with cause-based search and verified donation links. Candid's free MCP connector offers funder search, leadership demographics, and research reports. Both are Claude Connectors, not open-source. **Humanitarian data stands out** — dividor/hdx-mcp (33 tools, Python, MIT) accesses the UN OCHA Humanitarian Data Exchange covering refugees, IDPs, food security, conflict events, and funding data across hundreds of countries. The humanitarian-mcp server adds structured negotiation frameworks for aid workers. **Volunteer impact measurement** — Goodera's commercial MCP aggregates data from 50,000+ nonprofit partners, 25,000+ events, and 2M+ volunteers with instant impact report generation. **Civic engagement** — mikeomlor/nb-mcp provides NationBuilder API access for community management and fundraising. Additional platforms (Donorbox, Givebutter, Little Green Light) are accessible through Zapier/Pipedream MCP wrappers rather than dedicated servers. **Gaps are significant** — no grant writing or grant management server, no DonorPerfect or Bloomerang integration, no standalone volunteer scheduling tool, no impact measurement frameworks beyond Goodera's commercial offering. The category earns 3/5 — Anthropic's nonprofit initiative has brought major platforms into the ecosystem, but open-source options are thin and most production-ready integrations are commercial or hosted."
---

Nonprofit and charity MCP servers let AI assistants look up charity tax status, access donor CRM data, query humanitarian datasets, discover nonprofit organizations, and measure volunteer impact. Instead of manually searching IRS databases, navigating donor management platforms, or compiling humanitarian reports, these servers let AI agents verify tax-deductible status, pull giving histories, analyze Form 990 financials, and generate impact reports — all through the Model Context Protocol.

This review covers the **nonprofit and charity** vertical — charity verification and IRS data, donor management CRMs, nonprofit discovery platforms, humanitarian data, volunteer impact measurement, and civic engagement tools. For general CRM servers, see our [CRM MCP review](/reviews/crm-mcp-servers/). For Salesforce-specific coverage, see the [Salesforce section in our CRM review](/reviews/crm-mcp-servers/).

The headline findings: **Anthropic's "Claude for Nonprofits" initiative drives this category** — Blackbaud, Benevity, and Candid all launched as official Claude Connectors in late 2025. **Open-source charity verification works** with two GitHub projects covering IRS and ProPublica data. **Humanitarian data has the strongest open-source entry** with HDX MCP's 33 tools covering UN OCHA data. **Donor management is entirely commercial.** **No grant management or volunteer scheduling servers exist yet.**

## Charity Verification & Data Lookup

### briancasteel/charity-mcp-server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [briancasteel/charity-mcp-server](https://github.com/briancasteel/charity-mcp-server) | 22 | TypeScript | MIT | 4 |

The **most complete open-source nonprofit lookup server**. Provides IRS-based charity verification through CharityAPI.org:

- **EIN lookup** — verify any US nonprofit by Employer Identification Number
- **Tax-deductible status** — confirm 501(c)(3) and other tax-exempt classifications
- **Organization search** — find nonprofits by name and filter results
- **Guided research** — 14 prompt templates for structured charity investigation workflows

Uses stdio transport. Requires a CHARITY_API_KEY environment variable from CharityAPI.org. TypeScript with full type safety and comprehensive error handling. The prompt templates are a nice touch — they guide agents through multi-step research workflows rather than just exposing raw data lookups.

### asachs01/propublica-mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [asachs01/propublica-mcp](https://github.com/asachs01/propublica-mcp) | — | — | — | 5 |

Accesses **ProPublica's Nonprofit Explorer API** for Form 990 data — the gold standard for US nonprofit financial transparency:

- **search_nonprofits** — find organizations by name and location
- **get_organization** — detailed nonprofit profile with mission, revenue, assets
- **get_organization_filings** — historical Form 990 filings with financial details
- **analyze_nonprofit_financials** — multi-year trend analysis of revenue, expenses, and assets
- **search_similar_nonprofits** — discover comparable organizations by NTEE code and geography

Implements the MCP 2025-03-26 Streamable HTTP transport. Docker deployment option available. Works with Claude Desktop and Cursor. The financial trend analysis tool is particularly valuable — it surfaces revenue trajectories and spending patterns across multiple filing years, something that would take significant manual effort on ProPublica's website.

### conorheffron/mcp-charity

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [conorheffron/mcp-charity](https://github.com/conorheffron/mcp-charity) | — | — | — | 1 |

A **sample/demonstration MCP server** for charity search. Includes a `query_charities` tool to search by name, location, and cause. More of a learning project than a production tool, but useful as a starting point for anyone building their own nonprofit MCP server.

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
| [dividor/hdx-mcp](https://github.com/dividor/hdx-mcp) | — | Python | MIT | 33 |

The **standout open-source server in this entire category**. Accesses the UN OCHA Humanitarian Data Exchange — one of the most important humanitarian data platforms in the world:

- **Refugees & displacement** — refugee populations, internally displaced persons (IDPs), returnee data by country
- **Demographics** — baseline population data across hundreds of countries
- **Food security** — food security indicators and crisis-level assessments
- **Conflict** — conflict event data with location, type, and casualties
- **Funding** — humanitarian funding flows, appeals, and operational presence
- **Auto-generated tools** — 33 tools generated from HDX's OpenAPI specification

Docker deployment supported. Requires an HDX API app identifier. The breadth is remarkable — with 33 tools covering the full spectrum of humanitarian data, this server could genuinely accelerate research, reporting, and coordination for aid organizations. Written up on Medium by the author with detailed implementation notes.

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

## Civic Engagement & Advocacy

### mikeomlor/nb-mcp (NationBuilder)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [mikeomlor/nb-mcp](https://github.com/mikeomlor/nb-mcp) | — | TypeScript | — | Multiple |

Community-built connector for **NationBuilder** — a platform widely used by political campaigns, advocacy organizations, and community groups:

- **People management** — CRUD operations for supporter records
- **Tag management** — assign, remove, list popular/recent/system tags
- **Search** — advanced multi-criteria search across the supporter database

NationBuilder is also accessible via Pipedream and Zapier MCP wrappers. While not strictly a "charity" tool, many nonprofits use NationBuilder for advocacy campaigns, membership management, and grassroots fundraising.

## Platform-Aggregated Access

Several nonprofit platforms lack dedicated MCP servers but are accessible through integration platform wrappers:

| Platform | Via | Use Case |
|----------|-----|----------|
| **Donorbox** | Zapier MCP | Fundraising, donation management |
| **Givebutter** | Zapier/Pipedream MCP | Free fundraising platform ($150M+ in donations processed) |
| **Little Green Light** | Zapier MCP | Donor management CRM for small nonprofits |
| **NationBuilder** | Pipedream/Zapier MCP | Community management, advocacy |
| **CiviCRM** | Pipedream MCP | Open-source nonprofit CRM |

These are not standalone MCP servers — they're API wrappers that expose platform actions as MCP tools through Zapier's or Pipedream's MCP integration layer. They work, but you're adding a dependency on a third-party integration platform.

## What's Missing

The nonprofit MCP space has significant gaps:

- **Grant management** — no server for grant discovery, application tracking, or grant writing assistance (Candid provides funder search but not application management)
- **DonorPerfect / Bloomerang** — two major nonprofit CRMs with no MCP integration of any kind
- **Volunteer scheduling** — no tool for shift management, skill matching, or availability coordination
- **Impact measurement frameworks** — no open-source server implementing Theory of Change, logic models, or standardized outcome metrics (Goodera is commercial only)
- **Nonprofit accounting** — no integration with Fund Accounting systems (Sage Intacct, Blackbaud Financial Edge)
- **Peer-to-peer fundraising** — no MCP server for crowdfunding campaign management
- **GuideStar / Charity Navigator ratings** — no direct MCP access to charity rating data (Candid provides profiles but not the rating systems themselves)

## Rating: 3/5

**What works:** Anthropic's "Claude for Nonprofits" initiative has brought major platforms (Blackbaud, Benevity, Candid) into the MCP ecosystem faster than organic open-source development would have. The HDX humanitarian data server is genuinely excellent with 33 tools and MIT licensing. Charity verification works well with two open-source options covering IRS and ProPublica data. Salesforce MCP provides an integration path for the 40,000+ nonprofits on that platform.

**What doesn't:** The open-source landscape is thin — only about 6 truly nonprofit-focused GitHub projects exist, most with low star counts. The most polished integrations are all commercial or hosted. No grant management server exists despite grants being fundamental to nonprofit operations. The gap between what commercial platforms offer and what's available open-source is stark. CiviCRM — the most widely-used open-source nonprofit CRM — has no dedicated MCP server.

**Who should care:** Nonprofit development officers who want AI-assisted donor communications and research, humanitarian data analysts working with UN OCHA data, charity evaluators needing quick IRS and Form 990 lookups, and anyone building AI tools for the social impact sector.

**Bottom line:** This category reveals how Anthropic's enterprise partnerships can bootstrap an MCP vertical faster than organic open-source growth. The Blackbaud, Benevity, and Candid connectors are genuinely useful for nonprofits already on Claude. But for organizations not using Claude or wanting self-hosted solutions, the pickings are slim. The HDX server is the crown jewel of the open-source side. A well-built CiviCRM MCP server would fill the biggest gap.
