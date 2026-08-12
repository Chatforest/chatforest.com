# CRM MCP Servers — Salesforce, HubSpot, Pipedrive, and Beyond

> CRM MCP servers let AI agents query leads, manage contacts, update deals, and run reports across Salesforce, HubSpot, Pipedrive, and more.


CRM data is some of the most valuable information a business owns — contacts, deals, pipeline stages, revenue forecasts, customer histories. Giving an AI agent access to that data changes how sales teams, customer success managers, and operations work. Instead of clicking through dashboards, you ask. Part of our **[Business & Productivity MCP category](/categories/business-productivity/)**.

The CRM MCP landscape has transformed since early 2026. HubSpot's [remote MCP server went GA on April 13](https://developers.hubspot.com/changelog/remote-hubspot-mcp-server-is-now-generally-available) with read/write access on core CRM objects (contacts, companies, deals, tickets, line items, products) and read-only access to the rest of the CRM. [Zoho launched official MCP support](https://www.zoho.com/mcp/) across 15 products including CRM. Microsoft's Dataverse MCP server reached GA, and Microsoft has been building out a **[management MCP server](https://learn.microsoft.com/en-us/microsoft-copilot-studio/mcp-management)** (currently a preview feature) that lets developers discover connectors — reportedly [1,470+ of them](https://m365admin.handsontek.net/microsoft-dataverse-discover-build-customize-extend-management-mcp-server/) — and build custom MCP servers from them. Salesforce leads the community with [455 stars on its official CLI server](https://github.com/salesforcecli/mcp) (it crossed 400 in May 2026), and its hosted server ([forcedotcom/mcp-hosted](https://github.com/forcedotcom/mcp-hosted)) has reached 132 stars as enterprises embrace hosted MCP endpoints. [Attio's community server](https://github.com/kesslerio/attio-mcp-server) has passed 1,400 commits and continues rapid iteration (v1.6.x as of May 2026), and [smn2gnt/MCP-Salesforce](https://github.com/smn2gnt/MCP-Salesforce) added OAuth 2.0 Client Credentials support for server-to-server integrations.

## The Landscape

### Salesforce

| Server | Stars | Language | Tools | Auth | License |
|--------|-------|----------|-------|------|---------|
| [salesforcecli/mcp](https://github.com/salesforcecli/mcp) | 455 | TypeScript | 60+ | SF CLI org auth | Apache 2.0 |
| [smn2gnt/MCP-Salesforce](https://github.com/smn2gnt/MCP-Salesforce) | 179 | Python | 7+ | OAuth / CLI / Password | MIT |
| [tsmztech/mcp-server-salesforce](https://github.com/tsmztech/mcp-server-salesforce) | 166 | TypeScript | 15 | Password / OAuth / CLI | MIT |
| [forcedotcom/mcp-hosted](https://github.com/forcedotcom/mcp-hosted) | 132 | — | Hosted (GA) | External Client Apps | Apache 2.0 |
| [kablewy/salesforce-mcp-server](https://github.com/kablewy/salesforce-mcp-server) | 45 | TypeScript | 5 | Env vars | MIT |
| [jaworjar95/salesforce-mcp-server](https://github.com/jaworjar95/salesforce-mcp-server) | 43 | TypeScript | 17 | OAuth / Password | MIT |
| [advancedcommunities/salesforce-mcp-server](https://github.com/advancedcommunities/salesforce-mcp-server) | 31 | TypeScript | 41 | SF CLI | MIT |

### HubSpot

| Server | Stars | Language | Tools | Auth | License |
|--------|-------|----------|-------|------|---------|
| **[HubSpot Remote MCP](https://developers.hubspot.com/mcp)** | — | Hosted (GA) | Full CRM R/W | OAuth 2.1 | Official |
| **[HubSpot Developer MCP](https://developers.hubspot.com/changelog/hubspot-developer-mcp-server-for-app-and-cms-development-now-in-ga)** | — | Local CLI (GA) | App/CMS dev | CLI | Official |
| [peakmojo/mcp-hubspot](https://github.com/peakmojo/mcp-hubspot) | 127 | Python | 6 | Access token | MIT |
| [lkm1developer/hubspot-mcp-server](https://github.com/lkm1developer/hubspot-mcp-server) | 13 | TypeScript | 8 | Access token | MIT |
| [scopiousdigital/hubspot-mcp](https://github.com/scopiousdigital/hubspot-mcp) | 10 | JavaScript | 17 | Private App (14 scopes) | MIT |
| [adeel0x01/hubspot-mcp-tools](https://github.com/adeel0x01/hubspot-mcp-tools) | 4 | TypeScript | 87+ | Private App | MIT |
| [HubSpot/mcp-server](https://github.com/HubSpot/mcp-server) | 5 | — | — | — | — |

### Zoho

| Server | Tools | Auth | Notes |
|--------|-------|------|-------|
| **[Zoho MCP](https://www.zoho.com/mcp/)** | CRM + 14 products | OAuth | Official, 500+ third-party integrations |
| [CDataSoftware/zoho-crm-mcp-server-by-cdata](https://github.com/CDataSoftware/zoho-crm-mcp-server-by-cdata) | Read-only | JDBC | CData managed |

### Microsoft Dynamics 365 / Dataverse

| Server | Tools | Auth | Notes |
|--------|-------|------|-------|
| **[Dataverse MCP](https://learn.microsoft.com/en-us/power-apps/maker/data-platform/data-platform-mcp)** | 15 | Azure AD / Entra | Official GA, Copilot credit billing |
| [srikanth-paladugula/mcp-dynamics365-server](https://github.com/srikanth-paladugula/mcp-dynamics365-server) | 5 | Azure AD | Community, 21 stars |
| [rajyraman/mcp-dataverse](https://github.com/rajyraman/mcp-dataverse) | SQL queries | Azure AD | Community |

### Other CRM Platforms

| Server | CRM | Stars | Language | Tools | License |
|--------|-----|-------|----------|-------|---------|
| [kesslerio/attio-mcp-server](https://github.com/kesslerio/attio-mcp-server) | Attio | 69 | TypeScript | 19 (universal) | Apache 2.0 |
| [WillDent/pipedrive-mcp-server](https://github.com/WillDent/pipedrive-mcp-server) | Pipedrive | 60 | TypeScript | 15 | MIT |
| [mhenry3164/twenty-crm-mcp-server](https://github.com/mhenry3164/twenty-crm-mcp-server) | Twenty | 88 | JavaScript | CRUD + search | MIT |
| [clay-inc/clay-mcp](https://github.com/clay-inc/clay-mcp) | Clay | 34 | — | 10+ | — |
| [gunnit/bitrix24-mcp-server](https://github.com/gunnit/bitrix24-mcp-server) | Bitrix24 | 33 | TypeScript | 40+ | MIT |
| [Descomplicar-Marketing-e-Tecnologia/mcp-perfex-crm](https://github.com/Descomplicar-Marketing-e-Tecnologia/mcp-perfex-crm) | Perfex | 28 | TypeScript | 186 | MIT |
| [Teapot-Agency/mcp_pipedrive](https://github.com/Teapot-Agency/mcp_pipedrive) | Pipedrive | 6 | TypeScript | 40 | MIT |

The landscape has shifted dramatically. Four CRM platforms — Salesforce, HubSpot, Zoho, and Microsoft — now have official, production-grade MCP servers. Microsoft's management MCP server (preview) adds a meta-layer for building custom MCP servers from a large connector catalog. Salesforce still leads the community ecosystem.

## salesforcecli/mcp — The Official Salesforce Server

[salesforcecli/mcp](https://github.com/salesforcecli/mcp) (455 stars, Apache 2.0) is officially maintained by Salesforce as part of their CLI toolchain. It crossed 400 stars in May 2026 and remains the most comprehensive CRM MCP server in any ecosystem. It reached [v0.30.9 on May 7, 2026](https://github.com/salesforcecli/mcp/releases); as of this audit the [latest release is v0.30.15](https://github.com/salesforcecli/mcp/releases) (July 9, 2026).

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

**[smn2gnt/MCP-Salesforce](https://github.com/smn2gnt/MCP-Salesforce)** (179 stars, Python, MIT) — The leading community alternative. Covers SOQL queries, SOSL search, record CRUD, metadata retrieval, Tooling API, and direct REST API calls. Three auth modes (OAuth, CLI, username/password). Recent additions include **OAuth 2.0 Client Credentials** for server-to-server integrations and [bulk operations support](https://github.com/smn2gnt/MCP-Salesforce) (bulk create/update/delete). Install via `uvx mcp-salesforce-connector`. Best option if you want a Python-based Salesforce MCP server or need the Tooling API.

**[tsmztech/mcp-server-salesforce](https://github.com/tsmztech/mcp-server-salesforce)** (166 stars, TypeScript, MIT) — 15 tools ([full list on GitHub](https://github.com/tsmztech/mcp-server-salesforce)) covering search, describe, query, aggregate query, DML, object/field management, field permissions, and Apex read/write/execute/trigger operations. Strong feature set including aggregate queries, field-level security management, anonymous Apex execution, and multi-org support with switchable authentication. Notable for being one of the few servers that handles field-level security explicitly.

**[advancedcommunities/salesforce-mcp-server](https://github.com/advancedcommunities/salesforce-mcp-server)** (31 stars, TypeScript, MIT) — 41 tools including Apex execution, SOQL with CSV/JSON export, test runner, metadata management, and code analysis. Reached [v1.6.5 in April 2026](https://github.com/advancedcommunities/salesforce-mcp-server/tags) (now at v1.6.6, May 2026). Standout feature: **read-only mode** and **org restriction** for safety. Supports Claude Code skill installation. Install via `npx @advanced-communities/salesforce-mcp-server`.

**[forcedotcom/mcp-hosted](https://github.com/forcedotcom/mcp-hosted)** (132 stars, Apache 2.0) — Salesforce-hosted MCP servers that let external AI agents access Salesforce logic through admin-governed endpoints. **GA** (graduated from beta). Uses External Client Apps for auth. This is the enterprise deployment model — Salesforce runs the server, your agent connects remotely.

## HubSpot — From Empty Repo to Full GA in One Quarter

The biggest shift in the CRM MCP landscape: HubSpot went from an empty GitHub repo to **two production GA servers** in early 2026. This changes the calculus for [HubSpot's 288,706 customers (as of December 31, 2025)](https://ir.hubspot.com/news-releases/news-release-details/hubspot-reports-strong-q4-and-full-year-2025-results).

### HubSpot Remote MCP Server (GA — April 13, 2026)

The [remote HubSpot MCP server](https://developers.hubspot.com/changelog/remote-hubspot-mcp-server-is-now-generally-available) is a hosted, first-party server that gives any MCP-compatible AI tool secure read and write access to your HubSpot CRM data.

**Create/update access:** [contacts, companies, deals, tickets, line items, and products](https://developers.hubspot.com/changelog/remote-hubspot-mcp-server-is-now-generally-available), plus activity logging (calls, meetings, notes, tasks, emails).

**Read-only access:**
- Additional CRM objects: carts, orders, invoices, quotes, subscriptions, segments (lists)
- Organizational context: users, teams, reporting structures, owners, roles, seats
- Marketing/content: campaigns, landing pages, website pages, blog posts, marketing events

**Auth:** OAuth 2.1 with PKCE. Self-service MCP Auth Apps tool in the Developer Platform enables full lifecycle management of MCP connectors. All actions respect existing HubSpot user permissions.

**Limitation:** When "sensitive data" is enabled on a HubSpot account, Activity objects become inaccessible through the MCP server.

### HubSpot Developer MCP Server (GA — February 19, 2026)

The [Developer MCP server](https://developers.hubspot.com/changelog/hubspot-developer-mcp-server-for-app-and-cms-development-now-in-ga) is a local CLI tool for building HubSpot apps and CMS assets through agentic tools like Claude Code, Cursor, OpenAI Codex, and Gemini CLI. Separate from the CRM server — this is for platform developers, not CRM users.

### peakmojo/mcp-hubspot — Still Relevant?

[peakmojo/mcp-hubspot](https://github.com/peakmojo/mcp-hubspot) (127 stars, Python, MIT) was the community standard before HubSpot went official. Its **FAISS semantic search** — building a local vector index for fuzzy matching across contacts and companies — remains a differentiator the official server doesn't offer. If you need "companies similar to [description]" queries, peakmojo still has a unique edge.

But for standard CRM operations (CRUD on deals, tickets, contacts, companies, engagements), the official remote server now covers far more ground with proper auth, write access, and HubSpot's own maintenance guarantee. The community server's 6 tools can't match the breadth of the official server's full CRM coverage.

**When to use peakmojo:** Semantic search over CRM data, self-hosted requirements, or FAISS-powered duplicate detection.

**When to use the official server:** Everything else — especially if you need deals, tickets, pipeline management, marketing content access, or organizational context.

## Attio, Pipedrive, and the Rest

### Attio — Still Punching Above Its Weight

[kesslerio/attio-mcp-server](https://github.com/kesslerio/attio-mcp-server) (69 stars, 1,402 commits, TypeScript, Apache 2.0) has been in intensive, rapid-release development — it's [now at v1.6.1 (May 14, 2026)](https://github.com/kesslerio/attio-mcp-server/tags), up from v1.0.0 back in [September 2025](https://github.com/kesslerio/attio-mcp-server). It remains the most actively maintained CRM MCP server by commit count. For a CRM with a fraction of Salesforce's market share, the MCP server quality is disproportionately high.

The server's [universal-tools architecture](https://github.com/kesslerio/attio-mcp-server) consolidates 40+ resource-specific tools into a smaller set of universal operations (currently 19 universal operations, ~41 tools total) while maintaining full functionality. Complete CRUD for Companies, People, Deals, Tasks, Lists, and Notes. Advanced AND/OR filtering, batch operations, and content search. The README reports an **89.7% speed improvement with 227KB memory reduction** from recent performance work (PR #483).

If you use Attio, this is a first-class MCP integration. The [97.15/100 production readiness score](https://github.com/kesslerio/attio-mcp-server) (self-reported in the README) speaks for itself.

### Pipedrive — Read-Only Leader, Write-Capable Newcomer

[WillDent/pipedrive-mcp-server](https://github.com/WillDent/pipedrive-mcp-server) (60 stars, TypeScript, MIT) — The most popular Pipedrive server, with 15 tools and 8 predefined prompts for deals, persons, organizations, and pipelines. It's [**read-only by default**](https://github.com/WillDent/pipedrive-mcp-server) — two narrowly-scoped write tools can be enabled explicitly via an environment variable and stay preview-first. For sales teams that want broad write access to update deal stages or add notes, this remains limited.

[Teapot-Agency/mcp_pipedrive](https://github.com/Teapot-Agency/mcp_pipedrive) (6 stars, TypeScript, MIT) — Full CRUD with 40 tools (20 read, 20 write). Deals, persons, organizations, activities, notes, and leads. Fuzzy person search and soft delete recovery. **v2.1** added documented search improvements. Much lower adoption, but if you need write access, this is the only real option.

### Dynamics 365 / Dataverse — From Minimal to Official, Now a Platform

The Dynamics 365 story has changed completely. **Microsoft's Dataverse MCP server is now GA**, providing a standardized remote MCP endpoint at `https://{org}.crm.dynamics.com/api/mcp`.

**15 tools** (as of this audit — [the tool surface changed since this server launched](https://learn.microsoft.com/en-us/power-apps/maker/data-platform/data-platform-mcp)): search_data, search, create_record, update_record, delete_record, create_table, update_table, delete_table, read_query (Dataverse SQL SELECT), describe, upsert_skill, delete_skill, init_file_upload, commit_file_upload, and file_download. Microsoft's docs note the older `describe_table`, `list_tables`, and `fetch` tools were removed and replaced by `describe`, and the original data-search `search` tool was renamed `search_data`. Supports Copilot Studio agents, VS Code GitHub Copilot, Claude Desktop, Claude Code, and other MCP clients.

**Management MCP server (preview):** Microsoft is also building a [management MCP server](https://learn.microsoft.com/en-us/microsoft-copilot-studio/mcp-management) — currently a preview feature, not yet GA — as a meta-level capability: a central API-based foundation for discovering and building custom MCP servers. Per Microsoft's own materials it lets developers query and explore [over 1,470 connectors](https://m365admin.handsontek.net/microsoft-dataverse-discover-build-customize-extend-management-mcp-server/) and their individual actions, discover custom APIs available in their organization, and build new MCP servers by selecting connector actions and reusable tools. This positions Dataverse not just as a CRM MCP server but as a **platform for building MCP servers** — once it reaches general availability.

**Billing:** Charged per Copilot Credits when accessed by non-Copilot Studio agents. Free for Dynamics 365 Premium license holders and Microsoft 365 Copilot USL holders.

The community [srikanth-paladugula/mcp-dynamics365-server](https://github.com/srikanth-paladugula/mcp-dynamics365-server) (21 stars, 5 tools) still exists for simpler setups, plus [rajyraman/mcp-dataverse](https://github.com/rajyraman/mcp-dataverse) for SQL-based querying. But the official Dataverse server — now with the Management MCP layer — is the clear choice for enterprise deployments.

### Zoho — No Longer Missing

Zoho launched **[official MCP support](https://www.zoho.com/mcp/)** covering 15 products: CRM, Mail, Calendar, Desk, Cliq, Projects, WorkDrive, Books, Billing, People, Expense, Creator, Survey, Apptics, and Bigin. OAuth-based auth with user-level permission scoping. Agents can only perform actions the user is authorized to do.

The platform's own site states it [connects to 500+ third-party apps](https://www.zoho.com/mcp/) and supports any MCP-compatible client (Claude, GPT, etc.). This is a dramatic shift from our March review, where no production-ready Zoho CRM MCP server existed.

**New in 2026:** Zoho Analytics shipped a [**Remote MCP Server**](https://www.zoho.com/analytics/api/v2/zoho-analytics-mcp-server/remote-mcp.html) setup — a single centrally managed instance shared over HTTPS, eliminating per-user Docker installs and local credential management. The [Analytics MCP Server is also published on NPM](https://www.npmjs.com/package/zoho-analytics-mcp-server), simplifying deployment further.

On the community side, [CDataSoftware/zoho-crm-mcp-server-by-cdata](https://github.com/CDataSoftware/zoho-crm-mcp-server-by-cdata) offers a read-only option via JDBC drivers for those who prefer local server control.

### Notable Others

**[mhenry3164/twenty-crm-mcp-server](https://github.com/mhenry3164/twenty-crm-mcp-server)** (88 stars, JavaScript, MIT) — For [Twenty](https://twenty.com), the open-source CRM. Dynamic schema discovery, advanced search, full CRUD. Stars continue to climb as Twenty's open-source CRM community grows.

**[clay-inc/clay-mcp](https://github.com/clay-inc/clay-mcp)** (34 stars) — First-party from Clay (the contact management platform). Contact search, interaction retrieval, contact statistics, calendar integration. Guided login flow for auth.

**[gunnit/bitrix24-mcp-server](https://github.com/gunnit/bitrix24-mcp-server)** (33 stars, TypeScript, MIT) — Contact, deal, task, and lead management for Bitrix24, with 40+ tools. [Rate limiting (2 requests/second) built in](https://github.com/gunnit/bitrix24-mcp-server). Auth via webhook URL.

**[Descomplicar-Marketing-e-Tecnologia/mcp-perfex-crm](https://github.com/Descomplicar-Marketing-e-Tecnologia/mcp-perfex-crm)** (28 stars, TypeScript, MIT) — 186+ tools across 14 modules for Perfex CRM. Reached [**v1.0.0-stable**](https://github.com/Descomplicar-Marketing-e-Tecnologia/mcp-perfex-crm) with zero warnings in ESLint and TypeScript. Uses direct MySQL access, which the README documents as roughly [10x faster in its benchmark example](https://github.com/Descomplicar-Marketing-e-Tecnologia/mcp-perfex-crm) (getting 100 customers: 2.3s via REST vs. 0.23s via MySQL) — the README's broader claim is "10-100x faster than REST API" depending on the query. Read-only by default. The tool count is enormous, but Perfex is a niche platform.

## CRM Platform Comparison

| Feature | Salesforce | HubSpot | Zoho | Dynamics 365 | Attio | Pipedrive |
|---------|-----------|---------|------|--------------|-------|-----------|
| Official server | Yes (GA) | Yes (GA) | Yes | Yes (GA) | Community | Community |
| Top server stars | 455 | — (hosted) | — (hosted) | — (hosted) | 69 | 60 |
| Tool count | 60+ | Full CRM | 15 products | 15 + Mgmt MCP (preview) | 19 (universal) | 15 (or 40) |
| Read/Write | Both | Both (core objects; rest read-only) | Both | Both | Both | Read-only by default (top) |
| Auth model | SF CLI | OAuth 2.1 | OAuth | Azure AD / Entra | API key | API token |
| Hosted option | Yes (mcp-hosted GA) | Yes (remote) | Yes | Yes (remote) | Cloudflare Workers | No |
| Active maintenance | High | High (first-party) | High (first-party) | High (first-party) | Very high | Low |
| Ecosystem maturity | Strong | Strong | Strong | Growing | Surprisingly mature | Early |

## Which CRM Server Should You Use?

**Use salesforcecli/mcp if** you're a Salesforce developer and want official, comprehensive MCP access. The toolset architecture keeps context lean; it's iterating quickly (v0.30.9 in May, v0.30.15 by July 2026). For hosted enterprise deployment, use forcedotcom/mcp-hosted (GA, 132 stars). If you need Python, smn2gnt/MCP-Salesforce (179 stars) added OAuth 2.0 Client Credentials for server-to-server integrations and bulk operations support.

**Use HubSpot's official remote MCP server if** you're on HubSpot. Write access on core CRM objects, read access across the rest of the CRM plus engagement history, marketing content, and organizational context — all with your existing HubSpot permissions. The community server peakmojo/mcp-hubspot still has a niche for FAISS semantic search, but the official server covers everything else.

**Use Zoho's official MCP if** you're in the Zoho ecosystem. Coverage spans CRM plus 14 other Zoho products with OAuth and permission-level scoping. The gap that existed in March 2026 is filled.

**Use Microsoft's Dataverse MCP server if** you're on Dynamics 365. 15 tools with GA status and Azure AD auth. Microsoft's management MCP server — still a **preview** feature, not GA — adds a discovery and builder layer on top, reportedly covering 1,470+ connectors. Note the Copilot Credit billing model for non-Copilot Studio agents — check if your licenses cover it.

**Use kesslerio/attio-mcp-server if** you use Attio. No caveats — rapid release cadence (v1.6.1 as of May 2026), 1,400+ commits, a self-reported 97/100 production-readiness score, and thoughtful architecture.

**Use Teapot-Agency/mcp_pipedrive if** you're on Pipedrive and need write access (its README documents v2.1 search improvements). Use WillDent's server (60 stars) if read-only is sufficient. Pipedrive remains the most underserved major CRM platform — no official server, no write-capable community standard with meaningful adoption.

## The Bottom Line

**Rating: 4/5** — The CRM MCP landscape continues to consolidate around official servers. Salesforce's CLI server crossed **400 stars** in May 2026 and now sits at 455, while the hosted server (forcedotcom/mcp-hosted) has climbed to 132 stars. The smn2gnt community server added OAuth 2.0 Client Credentials and bulk operations support, making it a serious choice for Python shops. HubSpot's remote MCP server remains GA, with write access on core CRM objects and read access elsewhere. Zoho and Microsoft Dataverse continue to provide official coverage.

Microsoft's management MCP server (still preview, not GA) provides a meta-layer for discovering connectors — reportedly 1,470+ of them — and building custom MCP servers. Attio's community server keeps shipping fast: it reached v1.0.0 back in September 2025 and has climbed to v1.6.1 by May 2026, now the most commit-dense CRM MCP server (1,400+ commits) in the ecosystem.

Four of the five largest CRM platforms now have official, production-grade MCP servers. The only notable holdout is Pipedrive, where the most popular community server (60 stars) is read-only by default.

The rating holds at 4/5. The remaining gap: Pipedrive's limited official coverage, the absence of cross-CRM migration tools, and the fact that most official servers — while demonstrably growing — still need more battle-testing at enterprise scale.

---

*This review covers the CRM MCP server landscape as of May 2026, with citations re-verified against live sources on 2026-08-12. ChatForest researches MCP servers by reading source code, analyzing GitHub repositories and issues, studying documentation, and examining community signals. We do not install or run the servers ourselves. See our [methodology](/about/#our-review-methodology) for details.*

*This review was last edited on 2026-08-12 using Claude Sonnet 5 (Anthropic).*

