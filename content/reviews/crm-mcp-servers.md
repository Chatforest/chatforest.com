---
title: "CRM MCP Servers — Salesforce, HubSpot, Pipedrive, and Beyond"
date: 2026-03-15T02:05:00+09:00
description: "CRM MCP servers let AI agents query leads, manage contacts, update deals, and run reports across Salesforce, HubSpot, Pipedrive, and more. We reviewed 20+ servers across 8 CRM platforms. Salesforce dominates, HubSpot's official repo is empty, and Zoho lags behind."
og_description: "CRM MCP servers: Salesforce CLI (312 stars, official), HubSpot (116 stars community), Pipedrive, Attio, Dynamics 365, and more. 20+ servers reviewed. Rating: 3.5/5."
content_type: "Review"
card_description: "CRM MCP servers across Salesforce, HubSpot, Pipedrive, Attio, Dynamics 365, and more. Salesforce has the deepest ecosystem; most others are early-stage."
last_refreshed: 2026-03-15
---

CRM data is some of the most valuable information a business owns — contacts, deals, pipeline stages, revenue forecasts, customer histories. Giving an AI agent access to that data changes how sales teams, customer success managers, and operations work. Instead of clicking through dashboards, you ask.

The MCP ecosystem for CRM is uneven. Salesforce has a mature, officially-backed server with 60+ tools. HubSpot's official repo exists but is empty. Pipedrive's most popular server is read-only. Zoho, despite being one of the largest CRM platforms globally, has no production-ready MCP server. Here's the full picture.

## The Landscape

### Salesforce

| Server | Stars | Language | Tools | Auth | License |
|--------|-------|----------|-------|------|---------|
| [salesforcecli/mcp](https://github.com/salesforcecli/mcp) | 312 | TypeScript | 60+ | SF CLI org auth | Apache 2.0 |
| [smn2gnt/MCP-Salesforce](https://github.com/smn2gnt/MCP-Salesforce) | 166 | Python | 7+ | OAuth / CLI / Password | MIT |
| [tsmztech/mcp-server-salesforce](https://github.com/tsmztech/mcp-server-salesforce) | 139 | TypeScript | 10+ | Password / OAuth / CLI | — |
| [kablewy/salesforce-mcp-server](https://github.com/kablewy/salesforce-mcp-server) | 44 | TypeScript | 3+ | Env vars | MIT |
| [jaworjar95/salesforce-mcp-server](https://github.com/jaworjar95/salesforce-mcp-server) | 39 | TypeScript | 17 | OAuth / Password | MIT |
| [forcedotcom/mcp-hosted](https://github.com/forcedotcom/mcp-hosted) | 31 | — | Hosted | External Client Apps | Apache 2.0 |
| [advancedcommunities/salesforce-mcp-server](https://github.com/advancedcommunities/salesforce-mcp-server) | 23 | TypeScript | 40 | SF CLI | MIT |

### HubSpot

| Server | Stars | Language | Tools | Auth | License |
|--------|-------|----------|-------|------|---------|
| [peakmojo/mcp-hubspot](https://github.com/peakmojo/mcp-hubspot) | 116 | Python | 7 | Access token | MIT |
| [lkm1developer/hubspot-mcp-server](https://github.com/lkm1developer/hubspot-mcp-server) | 12 | TypeScript | 8 | Access token | MIT |
| [scopiousdigital/hubspot-mcp](https://github.com/scopiousdigital/hubspot-mcp) | 10 | JavaScript | 6+ | Private App (14 scopes) | MIT |
| [adeel0x01/hubspot-mcp-tools](https://github.com/adeel0x01/hubspot-mcp-tools) | 4 | TypeScript | 58 | Private App | MIT |
| [HubSpot/mcp-server](https://github.com/HubSpot/mcp-server) | 3 | — | — | — | — |

### Other CRM Platforms

| Server | CRM | Stars | Language | Tools | License |
|--------|-----|-------|----------|-------|---------|
| [kesslerio/attio-mcp-server](https://github.com/kesslerio/attio-mcp-server) | Attio | 58 | TypeScript | 14 | Apache 2.0 |
| [WillDent/pipedrive-mcp-server](https://github.com/WillDent/pipedrive-mcp-server) | Pipedrive | 46 | TypeScript | 16 | MIT |
| [mhenry3164/twenty-crm-mcp-server](https://github.com/mhenry3164/twenty-crm-mcp-server) | Twenty | 42 | JavaScript | CRUD + search | MIT |
| [clay-inc/clay-mcp](https://github.com/clay-inc/clay-mcp) | Clay | 29 | — | 5+ | — |
| [gunnit/bitrix24-mcp-server](https://github.com/gunnit/bitrix24-mcp-server) | Bitrix24 | 24 | TypeScript | 8+ | MIT |
| [srikanth-paladugula/mcp-dynamics365-server](https://github.com/srikanth-paladugula/mcp-dynamics365-server) | Dynamics 365 | 17 | TypeScript | 5 | MIT |
| [Descomplicar-Marketing-e-Tecnologia/mcp-perfex-crm](https://github.com/Descomplicar-Marketing-e-Tecnologia/mcp-perfex-crm) | Perfex | 16 | TypeScript | 186 | MIT |
| [Teapot-Agency/mcp_pipedrive](https://github.com/Teapot-Agency/mcp_pipedrive) | Pipedrive | 5 | TypeScript | 40 | MIT |

Salesforce dominates with 143 repositories found on GitHub. HubSpot has a growing ecosystem but no official backing. Everything else is early-stage with single-digit contributors.

## salesforcecli/mcp — The Official Salesforce Server

[salesforcecli/mcp](https://github.com/salesforcecli/mcp) (312 stars, Apache 2.0) is officially maintained by Salesforce as part of their CLI toolchain. It's by far the most comprehensive CRM MCP server in any ecosystem.

**60+ tools organized into toolsets:**

- **Metadata** — deploy, retrieve, list, describe metadata components
- **SOQL** — query Salesforce data using SOQL
- **Apex** — run tests, execute anonymous Apex, view test results
- **LWC** — Lightning Web Component development tools
- **Aura Migration** — tools for migrating Aura components to LWC
- **DevOps Center** — deployment and pipeline management
- **Mobile** — mobile development utilities
- **Code Analysis** — static analysis and quality checks

**Install:** Requires Salesforce CLI installed. Authenticate via `sf org login web` or VS Code SFDX extension.

**Dynamic tool loading:** Instead of exposing all 60+ tools to the LLM at once, the server uses a toolset system. You specify which toolset(s) to load, keeping your agent's context focused. This is a design pattern more MCP servers should adopt — most agents don't need metadata deployment tools when they're running SOQL queries.

### What works well

**Depth that matches the platform.** Salesforce is complex — objects, metadata, Apex, LWC, flows, permissions, multi-org setups. This server doesn't simplify that complexity away. It gives agents the same capabilities that Salesforce developers use daily. SOQL queries, Apex test execution, metadata deployment — these are real developer workflows, not toy wrappers.

**Official maintenance.** Salesforce actively maintains this. Recent commits, responsive issue tracking, beta status with clear documentation. When the Salesforce API changes, this server updates. Community servers lag.

**Toolset architecture.** The dynamic loading approach means an agent can start with just the `soql` toolset for data queries and never see the 40+ metadata and deployment tools. Compare this to [Softeria's ms-365-mcp-server](/reviews/outlook-mcp-servers/) which loads all Microsoft 365 tools by default.

### What doesn't

**Beta status.** Like Microsoft's Work IQ servers, this is subject to Salesforce's Beta Services Terms. Breaking changes are possible.

**CLI dependency.** You need the Salesforce CLI installed and authenticated before the MCP server works. For developers already in the Salesforce ecosystem, this is fine. For someone new to Salesforce, it's an extra layer of setup before the MCP server even enters the picture.

**Developer-focused, not user-focused.** The toolsets (metadata, Apex, LWC) target Salesforce developers, not sales reps or managers who want to query their pipeline. If you want "show me my open deals," you'll need to know the right SOQL query. There's no natural-language abstraction layer.

## Community Salesforce Servers

**[smn2gnt/MCP-Salesforce](https://github.com/smn2gnt/MCP-Salesforce)** (166 stars, Python, MIT) — The leading community alternative. Covers SOQL queries, SOSL search, record CRUD, metadata retrieval, Tooling API, and direct REST API calls. Three auth modes (OAuth, CLI, username/password). Install via `uvx mcp-salesforce-connector`. Five contributors, active releases. Best option if you want a Python-based Salesforce MCP server or need the Tooling API.

**[tsmztech/mcp-server-salesforce](https://github.com/tsmztech/mcp-server-salesforce)** (139 stars, TypeScript) — Strong feature set including aggregate queries, field-level security management, anonymous Apex execution, debug logging, and multi-org support. Ships as a Claude Desktop extension (`.dxt`). Notable for being one of the few servers that handles field-level security explicitly.

**[advancedcommunities/salesforce-mcp-server](https://github.com/advancedcommunities/salesforce-mcp-server)** (23 stars, TypeScript, MIT) — 40 tools including Apex execution, SOQL with CSV/JSON export, test runner, metadata management, and code analysis. Standout feature: **read-only mode** and **org restriction** for safety. Install via `npx @advanced-communities/salesforce-mcp-server`.

**[forcedotcom/mcp-hosted](https://github.com/forcedotcom/mcp-hosted)** (31 stars, Apache 2.0) — Salesforce-hosted MCP servers that let external AI agents access Salesforce logic through admin-governed endpoints. Open Beta. Uses External Client Apps for auth. This is the enterprise deployment model — Salesforce runs the server, your agent connects remotely.

## peakmojo/mcp-hubspot — The HubSpot Community Standard

HubSpot's own [mcp-server](https://github.com/HubSpot/mcp-server) repo (3 stars) exists on GitHub but contains zero code — no README, no implementation, just 4 open issues. The community has filled the gap.

[peakmojo/mcp-hubspot](https://github.com/peakmojo/mcp-hubspot) (116 stars, Python, MIT) is the most popular HubSpot MCP server and one of the more thoughtful designs in the CRM MCP space.

**7 tools:**

| Tool | What it does |
|------|-------------|
| `hubspot-create-contact` | Create contacts with duplicate prevention |
| `hubspot-create-company` | Create companies with duplicate prevention |
| `hubspot-get-contact-activity` | Retrieve contact engagement history |
| `hubspot-get-company-activity` | Retrieve company engagement history |
| `hubspot-get-active-companies` | List recently active companies |
| `hubspot-get-active-contacts` | List recently active contacts |
| `hubspot-get-recent-conversations` | Recent conversation threads |

**Install:** Docker, Smithery, or local Python build.

**Auth:** HubSpot access token with scopes for contacts (read/write), companies (read/write), and sales email read.

### What works well

**FAISS semantic search.** This is the standout feature. The server builds a local FAISS vector index of your HubSpot data, enabling semantic search across contacts and companies. Instead of exact-match queries, your agent can find "companies similar to [description]" or "contacts who work on [topic]." No other CRM MCP server offers this.

**Duplicate prevention built-in.** Both create tools check for duplicates before creating records. CRM data hygiene is a real problem — agents that blindly create duplicate contacts would make a mess fast. peakmojo handles this at the server level.

**Focused scope.** Seven tools that do their jobs well, rather than 50 tools that cover edge cases. For HubSpot users who want agent access to contacts, companies, and engagement history, this covers the core use case.

### What doesn't

**Limited CRM coverage.** No deals, no tickets, no pipeline management, no custom objects. HubSpot's CRM goes well beyond contacts and companies, but this server doesn't. If you need deal tracking or support ticket management, look at adeel0x01/hubspot-mcp-tools (58 tools, 4 stars) — lower adoption but much broader coverage.

**No official backing.** HubSpot hasn't endorsed or contributed to any community MCP server. The empty official repo suggests they may be working on something, but there's nothing to use today.

**Python-only.** In a CRM MCP space dominated by TypeScript, peakmojo's Python implementation may not match everyone's stack. The Docker option mitigates this.

## Attio, Pipedrive, and the Rest

### Attio — Punching Above Its Weight

[kesslerio/attio-mcp-server](https://github.com/kesslerio/attio-mcp-server) (58 stars, TypeScript, Apache 2.0) is the most actively maintained CRM MCP server by commit count — 1,291 commits. For a CRM with a fraction of Salesforce's market share, the MCP server quality is disproportionately high.

**14 universal tools** (consolidated from 40+ in earlier versions) covering complete CRUD for Companies, People, Deals, Tasks, Lists, and Notes. Advanced AND/OR filtering, batch operations, content search, 10 MCP prompts, and 3 Claude Skills. OAuth support for Cloudflare Workers deployment. Safety annotations for OpenAI compatibility.

If you use Attio, this is a first-class MCP integration. The architecture — consolidating 40+ specialized tools into 14 universal ones — is a pattern worth studying.

### Pipedrive — Read-Only Leader, Write-Capable Newcomer

[WillDent/pipedrive-mcp-server](https://github.com/WillDent/pipedrive-mcp-server) (46 stars, TypeScript, MIT) — The most popular Pipedrive server, with 16 tools and 8 predefined prompts for deals, persons, organizations, and pipelines. But it's **read-only** — no creating or modifying records. For sales teams that want their agent to update deal stages or add notes, this is a blocker.

[Teapot-Agency/mcp_pipedrive](https://github.com/Teapot-Agency/mcp_pipedrive) (5 stars, TypeScript, MIT) — Full CRUD with 40 tools (20 read, 20 write). Deals, persons, organizations, activities, notes, and leads. Fuzzy person search and soft delete recovery. Much lower adoption, but if you need write access, this is the only real option.

### Dynamics 365 — Minimal Coverage

[srikanth-paladugula/mcp-dynamics365-server](https://github.com/srikanth-paladugula/mcp-dynamics365-server) (17 stars, TypeScript, MIT) — The only Dynamics 365 MCP server found. Just 5 tools: get user info, fetch accounts, get opportunities, create account, update account. Azure AD auth (client ID/secret/tenant). For a platform of Dynamics 365's scale and enterprise adoption, this is a glaring gap.

### Zoho — The Missing Giant

Zoho CRM has over 250,000 businesses on its platform, but the MCP ecosystem doesn't reflect that. The most starred Zoho MCP server ([Officehub-Tech-LLC/MCP-Server](https://github.com/Officehub-Tech-LLC/MCP-Server), 11 stars) is primarily demo code with incomplete CRM integration. [LokiMCPUniverse/zoho-crm-mcp-server](https://github.com/LokiMCPUniverse/zoho-crm-mcp-server) (3 stars) claims comprehensive API coverage but has only 2 commits. No production-ready Zoho CRM MCP server exists today.

### Notable Others

**[mhenry3164/twenty-crm-mcp-server](https://github.com/mhenry3164/twenty-crm-mcp-server)** (42 stars, JavaScript, MIT) — For [Twenty](https://twenty.com), the open-source CRM. Dynamic schema discovery, advanced search, full CRUD. If you've chosen Twenty as your CRM, this is a solid integration.

**[clay-inc/clay-mcp](https://github.com/clay-inc/clay-mcp)** (29 stars) — First-party from Clay (the contact management platform). Contact search, interaction retrieval, analytics, calendar integration. Guided login flow for auth.

**[gunnit/bitrix24-mcp-server](https://github.com/gunnit/bitrix24-mcp-server)** (24 stars, TypeScript, MIT) — Contact, deal, task, and lead management for Bitrix24. Rate limiting (2 req/sec) built in. Auth via webhook URL.

**[Descomplicar-Marketing-e-Tecnologia/mcp-perfex-crm](https://github.com/Descomplicar-Marketing-e-Tecnologia/mcp-perfex-crm)** (16 stars, TypeScript, MIT) — 186 tools across 14 modules for Perfex CRM. Uses direct MySQL access (10-100x faster than REST). Read-only by default. The tool count is enormous, but Perfex is a niche platform.

## CRM Platform Comparison

| Feature | Salesforce (Official) | HubSpot (Community) | Pipedrive (Community) | Attio (Community) | Dynamics 365 |
|---------|----------------------|---------------------|----------------------|-------------------|--------------|
| Official server | Yes (beta) | Empty repo | No | No | No |
| Top server stars | 312 | 116 | 46 | 58 | 17 |
| Tool count | 60+ | 7 (or 58) | 16 (or 40) | 14 | 5 |
| Read/Write | Both | Both | Read-only (top) | Both | Both |
| Auth model | SF CLI | Access token | API token | API key | Azure AD |
| Hosted option | Yes (mcp-hosted) | No | No | Cloudflare Workers | No |
| Active maintenance | High | Medium | Low | Very high | Low |
| Ecosystem maturity | Strong | Growing | Early | Surprisingly mature | Minimal |

## Which CRM Server Should You Use?

**Use salesforcecli/mcp if** you're a Salesforce developer and want official, comprehensive MCP access. Accept beta status. The toolset architecture keeps context lean. If you need Python instead, smn2gnt/MCP-Salesforce is the community standard.

**Use peakmojo/mcp-hubspot if** you're on HubSpot and want agent access to contacts, companies, and engagement history with semantic search. For broader coverage (deals, tickets, pipelines), try adeel0x01/hubspot-mcp-tools despite its low star count — 58 tools across 9 categories.

**Use kesslerio/attio-mcp-server if** you use Attio. No caveats — this is a genuinely excellent MCP server with active maintenance and thoughtful architecture.

**Use Teapot-Agency/mcp_pipedrive if** you're on Pipedrive and need write access. Use WillDent's server if read-only is sufficient.

**Wait if** you're on Dynamics 365 or Zoho. The MCP coverage for both platforms is too thin for production use. Check back in 6 months — or consider contributing a server yourself.

## The Bottom Line

**Rating: 3.5/5** — The CRM MCP space is a tale of haves and have-nots. Salesforce has a legitimate, officially-maintained server with 60+ tools and thoughtful architecture (dynamic toolsets, hosted deployment option). The community Salesforce ecosystem runs deep with 140+ repositories. HubSpot's community fills the gap left by an empty official repo, led by peakmojo's semantic-search approach. Attio's server is unexpectedly excellent for a smaller platform.

But the gaps are significant. Pipedrive's most popular server is read-only. Dynamics 365 has 5 tools. Zoho has nothing production-ready. No CRM platform except Salesforce has an official, maintained MCP server. For the sales, support, and revenue operations teams that live in these tools daily, the agent era is only half-arrived.

The Salesforce ecosystem alone would rate 4/5. The broader CRM landscape — where most platforms have minimal or zero coverage — brings the average down. If you're on Salesforce or Attio, you're well-served. Everyone else is waiting.

---

*This review covers the CRM MCP server landscape as of March 2026. ChatForest researches MCP servers by reading source code, analyzing GitHub repositories and issues, studying documentation, and examining community signals. We do not install or run the servers ourselves. See our [methodology](/about/#our-review-methodology) for details.*

*This review was last edited on 2026-03-16 using Claude Opus 4.6 (Anthropic).*
