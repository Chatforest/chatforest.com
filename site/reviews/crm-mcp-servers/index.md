# CRM MCP Servers — Salesforce, HubSpot, Pipedrive, and Beyond

> CRM MCP servers let AI agents query leads, manage contacts, update deals, and run reports across Salesforce, HubSpot, Pipedrive, and more.


CRM data is some of the most valuable information a business owns — contacts, deals, pipeline stages, revenue forecasts, customer histories. Giving an AI agent access to that data changes how sales teams, customer success managers, and operations work. Instead of clicking through dashboards, you ask. Part of our **[Business & Productivity MCP category](/categories/business-productivity/)**.

The CRM MCP landscape has transformed since our last review. HubSpot's remote MCP server went GA on April 13, 2026 with full read/write CRM access. Zoho launched official MCP support across 14 products including CRM. Microsoft's Dataverse MCP server reached GA with 11 tools, covering Dynamics 365 data. Salesforce continues to lead with 369 stars and a hosted GA deployment option. The era of "only Salesforce has an official server" is over.

## The Landscape

### Salesforce

| Server | Stars | Language | Tools | Auth | License |
|--------|-------|----------|-------|------|---------|
| [salesforcecli/mcp](https://github.com/salesforcecli/mcp) | 369 | TypeScript | 60+ | SF CLI org auth | Apache 2.0 |
| [smn2gnt/MCP-Salesforce](https://github.com/smn2gnt/MCP-Salesforce) | 174 | Python | 7+ | OAuth / CLI / Password | MIT |
| [tsmztech/mcp-server-salesforce](https://github.com/tsmztech/mcp-server-salesforce) | 153 | TypeScript | 15 | Password / OAuth / CLI | — |
| [forcedotcom/mcp-hosted](https://github.com/forcedotcom/mcp-hosted) | 74 | — | Hosted (GA) | External Client Apps | Apache 2.0 |
| [kablewy/salesforce-mcp-server](https://github.com/kablewy/salesforce-mcp-server) | 44 | TypeScript | 3+ | Env vars | MIT |
| [jaworjar95/salesforce-mcp-server](https://github.com/jaworjar95/salesforce-mcp-server) | 39 | TypeScript | 17 | OAuth / Password | MIT |
| [advancedcommunities/salesforce-mcp-server](https://github.com/advancedcommunities/salesforce-mcp-server) | 28 | TypeScript | 41 | SF CLI | MIT |

### HubSpot

| Server | Stars | Language | Tools | Auth | License |
|--------|-------|----------|-------|------|---------|
| **[HubSpot Remote MCP](https://developers.hubspot.com/mcp)** | — | Hosted (GA) | Full CRM R/W | OAuth 2.1 | Official |
| **[HubSpot Developer MCP](https://developers.hubspot.com/changelog/hubspot-developer-mcp-server-for-app-and-cms-development-now-in-ga)** | — | Local CLI (GA) | App/CMS dev | CLI | Official |
| [peakmojo/mcp-hubspot](https://github.com/peakmojo/mcp-hubspot) | 121 | Python | 7 | Access token | MIT |
| [lkm1developer/hubspot-mcp-server](https://github.com/lkm1developer/hubspot-mcp-server) | 12 | TypeScript | 8 | Access token | MIT |
| [scopiousdigital/hubspot-mcp](https://github.com/scopiousdigital/hubspot-mcp) | 10 | JavaScript | 6+ | Private App (14 scopes) | MIT |
| [adeel0x01/hubspot-mcp-tools](https://github.com/adeel0x01/hubspot-mcp-tools) | 4 | TypeScript | 58 | Private App | MIT |
| [HubSpot/mcp-server](https://github.com/HubSpot/mcp-server) | 4 | — | — | — | — |

### Zoho

| Server | Tools | Auth | Notes |
|--------|-------|------|-------|
| **[Zoho MCP](https://www.zoho.com/mcp/)** | CRM + 13 products | OAuth | Official, 500+ integrations |
| [CDataSoftware/zoho-crm-mcp-server-by-cdata](https://github.com/CDataSoftware/zoho-crm-mcp-server-by-cdata) | Read-only | JDBC | CData managed |

### Microsoft Dynamics 365 / Dataverse

| Server | Tools | Auth | Notes |
|--------|-------|------|-------|
| **[Dataverse MCP](https://learn.microsoft.com/en-us/power-apps/maker/data-platform/data-platform-mcp)** | 11 | Azure AD / Entra | Official GA, Copilot credit billing |
| [srikanth-paladugula/mcp-dynamics365-server](https://github.com/srikanth-paladugula/mcp-dynamics365-server) | 5 | Azure AD | Community, 17 stars |
| [rajyraman/mcp-dataverse](https://github.com/rajyraman/mcp-dataverse) | SQL queries | Azure AD | Community |

### Other CRM Platforms

| Server | CRM | Stars | Language | Tools | License |
|--------|-----|-------|----------|-------|---------|
| [kesslerio/attio-mcp-server](https://github.com/kesslerio/attio-mcp-server) | Attio | 67 | TypeScript | 18 (universal) | Apache 2.0 |
| [WillDent/pipedrive-mcp-server](https://github.com/WillDent/pipedrive-mcp-server) | Pipedrive | 56 | TypeScript | 15 | MIT |
| [mhenry3164/twenty-crm-mcp-server](https://github.com/mhenry3164/twenty-crm-mcp-server) | Twenty | 42 | JavaScript | CRUD + search | MIT |
| [clay-inc/clay-mcp](https://github.com/clay-inc/clay-mcp) | Clay | 29 | — | 5+ | — |
| [gunnit/bitrix24-mcp-server](https://github.com/gunnit/bitrix24-mcp-server) | Bitrix24 | 24 | TypeScript | 8+ | MIT |
| [Descomplicar-Marketing-e-Tecnologia/mcp-perfex-crm](https://github.com/Descomplicar-Marketing-e-Tecnologia/mcp-perfex-crm) | Perfex | 16 | TypeScript | 186 | MIT |
| [Teapot-Agency/mcp_pipedrive](https://github.com/Teapot-Agency/mcp_pipedrive) | Pipedrive | 5 | TypeScript | 40 | MIT |

The landscape has shifted dramatically. Three CRM platforms — Salesforce, HubSpot, and Zoho — now have official, production-grade MCP servers. Microsoft's Dataverse MCP server covers Dynamics 365 data with GA status. Salesforce still leads the community ecosystem with 143+ repositories on GitHub.

## salesforcecli/mcp — The Official Salesforce Server

[salesforcecli/mcp](https://github.com/salesforcecli/mcp) (369 stars, 734 commits, Apache 2.0) is officially maintained by Salesforce as part of their CLI toolchain. It remains the most comprehensive CRM MCP server in any ecosystem.

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

**[smn2gnt/MCP-Salesforce](https://github.com/smn2gnt/MCP-Salesforce)** (174 stars, Python, MIT) — The leading community alternative. Covers SOQL queries, SOSL search, record CRUD, metadata retrieval, Tooling API, and direct REST API calls. Three auth modes (OAuth, CLI, username/password). Now at v0.1.14 (April 2026) with 69 commits and 8 releases. Install via `uvx mcp-salesforce-connector`. Best option if you want a Python-based Salesforce MCP server or need the Tooling API.

**[tsmztech/mcp-server-salesforce](https://github.com/tsmztech/mcp-server-salesforce)** (153 stars, TypeScript) — Now at 15 tools and 98 commits. Strong feature set including aggregate queries, field-level security management, anonymous Apex execution, debug logging, and multi-org support with switchable authentication. Ships as a Claude Desktop extension (`.dxt`). Notable for being one of the few servers that handles field-level security explicitly.

**[advancedcommunities/salesforce-mcp-server](https://github.com/advancedcommunities/salesforce-mcp-server)** (28 stars, TypeScript, MIT) — 41 tools including Apex execution, SOQL with CSV/JSON export, test runner, metadata management, and code analysis. Now at 120 commits. Standout feature: **read-only mode** and **org restriction** for safety. Supports Claude Code skill installation. Install via `npx @advanced-communities/salesforce-mcp-server`.

**[forcedotcom/mcp-hosted](https://github.com/forcedotcom/mcp-hosted)** (74 stars, Apache 2.0) — Salesforce-hosted MCP servers that let external AI agents access Salesforce logic through admin-governed endpoints. **Now GA** (graduated from beta). Uses External Client Apps for auth. This is the enterprise deployment model — Salesforce runs the server, your agent connects remotely. Stars more than doubled since March, reflecting enterprise demand for hosted MCP.

## HubSpot — From Empty Repo to Full GA in One Quarter

The biggest shift in the CRM MCP landscape: HubSpot went from an empty GitHub repo to **two production GA servers** in early 2026. This changes the calculus for HubSpot's 228,000+ customers.

### HubSpot Remote MCP Server (GA — April 13, 2026)

The [remote HubSpot MCP server](https://developers.hubspot.com/mcp) is a hosted, first-party server that gives any MCP-compatible AI tool secure read and write access to your HubSpot CRM data.

**Read and write access:**
- CRM objects: contacts, companies, deals, tickets, carts, products, orders, line items, invoices, quotes, subscriptions, segments (lists)
- Engagements: calls, emails, meetings, notes, tasks

**Read-only access:**
- Organizational context: users, teams, reporting structures, owners, roles, seats
- Marketing/content: campaigns, landing pages, website pages, blog posts, marketing events

**Auth:** OAuth 2.1 with PKCE. Self-service MCP Auth Apps tool in the Developer Platform enables full lifecycle management of MCP connectors. All actions respect existing HubSpot user permissions.

**Limitation:** When "sensitive data" is enabled on a HubSpot account, Activity objects become inaccessible through the MCP server.

### HubSpot Developer MCP Server (GA — February 19, 2026)

The [Developer MCP server](https://developers.hubspot.com/changelog/hubspot-developer-mcp-server-for-app-and-cms-development-now-in-ga) is a local CLI tool for building HubSpot apps and CMS assets through agentic tools like Claude Code, Cursor, OpenAI Codex, and Gemini CLI. Separate from the CRM server — this is for platform developers, not CRM users.

### peakmojo/mcp-hubspot — Still Relevant?

[peakmojo/mcp-hubspot](https://github.com/peakmojo/mcp-hubspot) (121 stars, Python, MIT) was the community standard before HubSpot went official. Its **FAISS semantic search** — building a local vector index for fuzzy matching across contacts and companies — remains a differentiator the official server doesn't offer. If you need "companies similar to [description]" queries, peakmojo still has a unique edge.

But for standard CRM operations (CRUD on deals, tickets, contacts, companies, engagements), the official remote server now covers far more ground with proper auth, write access, and HubSpot's own maintenance guarantee. The community server's 7 tools can't match the breadth of the official server's full CRM coverage.

**When to use peakmojo:** Semantic search over CRM data, self-hosted requirements, or FAISS-powered duplicate detection.

**When to use the official server:** Everything else — especially if you need deals, tickets, pipeline management, marketing content access, or organizational context.

## Attio, Pipedrive, and the Rest

### Attio — Still Punching Above Its Weight

[kesslerio/attio-mcp-server](https://github.com/kesslerio/attio-mcp-server) (67 stars, 1,341 commits, TypeScript, Apache 2.0) remains the most actively maintained CRM MCP server by commit count. For a CRM with a fraction of Salesforce's market share, the MCP server quality is disproportionately high.

**v1.4.0 consolidated 70+ resource-specific tools into 18 universal tools** (68% reduction) while maintaining full functionality. Complete CRUD for Companies, People, Deals, Tasks, Lists, and Notes. Advanced AND/OR filtering, batch operations, content search, 10 MCP prompts, and Claude Skills with workspace schema auto-generation. ChatGPT Developer Mode integration with MCP safety annotations for auto-approval workflows. OAuth support for Cloudflare Workers deployment. 89.7% speed improvement with 227KB memory reduction in recent performance work.

If you use Attio, this is a first-class MCP integration. The 97.15/100 production readiness score speaks for itself.

### Pipedrive — Read-Only Leader, Write-Capable Newcomer

[WillDent/pipedrive-mcp-server](https://github.com/WillDent/pipedrive-mcp-server) (56 stars, TypeScript, MIT) — The most popular Pipedrive server, with 15 tools and 8 predefined prompts for deals, persons, organizations, and pipelines. But it's still **read-only** — no creating or modifying records. For sales teams that want their agent to update deal stages or add notes, this remains a blocker.

[Teapot-Agency/mcp_pipedrive](https://github.com/Teapot-Agency/mcp_pipedrive) (5 stars, TypeScript, MIT) — Full CRUD with 40 tools (20 read, 20 write). Deals, persons, organizations, activities, notes, and leads. Fuzzy person search and soft delete recovery. Much lower adoption, but if you need write access, this is the only real option.

### Dynamics 365 / Dataverse — From Minimal to Official

The Dynamics 365 story has changed completely. **Microsoft's Dataverse MCP server is now GA**, providing a standardized remote MCP endpoint at `https://{org}.crm.dynamics.com/api/mcp`.

**11 tools:** create_record, describe_table, list_tables, read_query (T-SQL SELECT), update_record, create_table, update_table, delete_table, delete_record, search, and fetch. Supports Copilot Studio agents, VS Code GitHub Copilot, Claude Desktop, Claude Code, and other MCP clients.

**Billing:** Charged per Copilot Credits when accessed by non-Copilot Studio agents. Free for Dynamics 365 Premium license holders and Microsoft 365 Copilot USL holders.

The community [srikanth-paladugula/mcp-dynamics365-server](https://github.com/srikanth-paladugula/mcp-dynamics365-server) (17 stars, 5 tools) still exists for simpler setups, plus [rajyraman/mcp-dataverse](https://github.com/rajyraman/mcp-dataverse) for SQL-based querying. But the official Dataverse server is now the clear choice for enterprise deployments.

### Zoho — No Longer Missing

Zoho launched **[official MCP support](https://www.zoho.com/mcp/)** covering 14 products: CRM, Mail, Calendar, Desk, Cliq, Projects, WorkDrive, Books, Billing, People, Expense, Creator, Survey, Apptics, and Bigin. OAuth-based auth with user-level permission scoping. Agents can only perform actions the user is authorized to do.

The platform claims 500+ integrations across third-party services and supports any MCP-compatible client (Claude, GPT, etc.). This is a dramatic shift from our March review, where no production-ready Zoho CRM MCP server existed.

On the community side, [CDataSoftware/zoho-crm-mcp-server-by-cdata](https://github.com/CDataSoftware/zoho-crm-mcp-server-by-cdata) offers a read-only option via JDBC drivers for those who prefer local server control.

### Notable Others

**[mhenry3164/twenty-crm-mcp-server](https://github.com/mhenry3164/twenty-crm-mcp-server)** (42 stars, JavaScript, MIT) — For [Twenty](https://twenty.com), the open-source CRM. Dynamic schema discovery, advanced search, full CRUD. If you've chosen Twenty as your CRM, this is a solid integration.

**[clay-inc/clay-mcp](https://github.com/clay-inc/clay-mcp)** (29 stars) — First-party from Clay (the contact management platform). Contact search, interaction retrieval, analytics, calendar integration. Guided login flow for auth.

**[gunnit/bitrix24-mcp-server](https://github.com/gunnit/bitrix24-mcp-server)** (24 stars, TypeScript, MIT) — Contact, deal, task, and lead management for Bitrix24. Rate limiting (2 req/sec) built in. Auth via webhook URL.

**[Descomplicar-Marketing-e-Tecnologia/mcp-perfex-crm](https://github.com/Descomplicar-Marketing-e-Tecnologia/mcp-perfex-crm)** (16 stars, TypeScript, MIT) — 186 tools across 14 modules for Perfex CRM. Uses direct MySQL access (10-100x faster than REST). Read-only by default. The tool count is enormous, but Perfex is a niche platform.

## CRM Platform Comparison

| Feature | Salesforce | HubSpot | Zoho | Dynamics 365 | Attio | Pipedrive |
|---------|-----------|---------|------|--------------|-------|-----------|
| Official server | Yes (GA) | Yes (GA) | Yes | Yes (GA) | Community | Community |
| Top server stars | 369 | — (hosted) | — (hosted) | — (hosted) | 67 | 56 |
| Tool count | 60+ | Full CRM | 14 products | 11 | 18 (universal) | 15 (or 40) |
| Read/Write | Both | Both | Both | Both | Both | Read-only (top) |
| Auth model | SF CLI | OAuth 2.1 | OAuth | Azure AD / Entra | API key | API token |
| Hosted option | Yes (mcp-hosted GA) | Yes (remote) | Yes | Yes (remote) | Cloudflare Workers | No |
| Active maintenance | High | High (first-party) | High (first-party) | High (first-party) | Very high | Low |
| Ecosystem maturity | Strong | Strong | Strong | Growing | Surprisingly mature | Early |

**PulseMCP stats:** Salesforce CLI ~599K all-time (#79), HubSpot ~560K all-time (#80), Attio ~13.2K all-time (#1,548).

## Which CRM Server Should You Use?

**Use salesforcecli/mcp if** you're a Salesforce developer and want official, comprehensive MCP access. The toolset architecture keeps context lean. For hosted enterprise deployment, use forcedotcom/mcp-hosted (now GA). If you need Python, smn2gnt/MCP-Salesforce (174 stars, v0.1.14) is the community standard.

**Use HubSpot's official remote MCP server if** you're on HubSpot. Full read/write CRM access, engagement history, marketing content, organizational context — all with your existing HubSpot permissions. The community server peakmojo/mcp-hubspot still has a niche for FAISS semantic search, but the official server covers everything else.

**Use Zoho's official MCP if** you're in the Zoho ecosystem. Coverage spans CRM plus 13 other Zoho products with OAuth and permission-level scoping. The gap that existed in March 2026 is filled.

**Use Microsoft's Dataverse MCP server if** you're on Dynamics 365. Eleven tools with GA status and Azure AD auth. Note the Copilot Credit billing model for non-Copilot Studio agents — check if your licenses cover it.

**Use kesslerio/attio-mcp-server if** you use Attio. No caveats — this is a genuinely excellent MCP server with 1,341 commits, 97/100 production readiness, and thoughtful architecture.

**Use Teapot-Agency/mcp_pipedrive if** you're on Pipedrive and need write access. Use WillDent's server (56 stars) if read-only is sufficient. Pipedrive remains the most underserved major CRM platform — no official server, no write-capable community standard.

## The Bottom Line

**Rating: 4/5** — The CRM MCP landscape has transformed in just five weeks. In March 2026, only Salesforce had an official MCP server. By April 2026, HubSpot's remote MCP server went GA with full read/write CRM access across 12 object types plus engagements. Zoho launched official MCP support across 14 products. Microsoft's Dataverse MCP server reached GA with 11 tools covering Dynamics 365 data. Salesforce's hosted server graduated from beta to GA, and the CLI server grew to 369 stars with 734 commits.

Four of the five largest CRM platforms now have official, production-grade MCP servers. Attio continues to punch above its weight with 1,341 commits and a 97/100 production readiness score. The only notable holdout is Pipedrive, where the most popular community server (56 stars) remains read-only.

The upgrade from 3.5 to 4/5 reflects a fundamental shift: CRM MCP has moved from "early adopters and Salesforce" to "mainstream enterprise capability." The remaining gap keeping this from 4.5 is Pipedrive's limited coverage, the lack of cross-CRM migration tools, and the fact that most official servers launched very recently — battle-testing takes time.

---

*This review covers the CRM MCP server landscape as of April 2026. ChatForest researches MCP servers by reading source code, analyzing GitHub repositories and issues, studying documentation, and examining community signals. We do not install or run the servers ourselves. See our [methodology](/about/#our-review-methodology) for details.*

*This review was last edited on 2026-04-22 using Claude Opus 4.6 (Anthropic).*

