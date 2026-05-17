# ITSM & IT Service Management MCP Servers — ServiceNow Action Fabric, PagerDuty, Jira Service Management, Zendesk, and More

> ITSM and IT service management MCP servers reviewed: ServiceNow Action Fabric MCP (Knowledge 2026, workflow execution + AICT governance) + 7 community servers, PagerDuty official (20+ tools, read-only default), Atlassian JSM (official remote), Zendesk (79 stars, community), incident.io (official hosted remote), Rootly (Apache 2.0, similarity analysis), Freshworks MCP Gateway (official, 28 tools, bidirectional, May 2026), Opsgenie (Go, multi-transport), ManageEngine SDP (16 tools), FireHydrant (official), TOPdesk, MCP-ITSM multi-platform. Rating: 4.0/5.


IT Service Management (ITSM) is one of the most mature MCP categories, with **official support from seven major vendors** — ServiceNow, PagerDuty, Atlassian JSM, incident.io, FireHydrant, Rootly, and Freshworks. MCP servers in this space let AI agents manage incidents, query on-call schedules, create and update tickets, search knowledge bases, traverse CMDBs, and coordinate incident response workflows. The ecosystem is splitting between **MCP server providers** (exposing ITSM capabilities for any AI client) and **MCP client consumers** (like BMC HelixGPT, connecting their AI to external tools). Part of our **[DevOps & Infrastructure MCP category](/categories/devops-infrastructure/)**.

This review covers **enterprise ITSM platforms** (ServiceNow, BMC), **incident management** (PagerDuty, incident.io, Rootly, FireHydrant, Opsgenie), **IT helpdesk** (Zendesk, Freshservice, ManageEngine, TOPdesk), **service desk within dev platforms** (Jira Service Management), and **multi-platform ITSM** tools. For monitoring and observability, see our [Monitoring & Observability MCP Servers](/reviews/monitoring-observability-mcp-servers/) review. For DevOps CI/CD tooling, see [CI/CD Pipeline MCP Servers](/reviews/ci-cd-pipeline-mcp-servers/).

The headline finding: **ServiceNow has the richest ITSM MCP ecosystem** with native platform support (now expanded as Action Fabric at Knowledge 2026) plus 7+ community servers. **PagerDuty leads on safety** with read-only-by-default design. **incident.io pioneered hosted remote MCP** for zero-install ITSM integration. **Freshworks joined the official ranks in May 2026** with a bidirectional MCP Gateway (28 tools, inbound + outbound) and the Freddy AI Agent Studio no-code agent platform. **Action Fabric marks the shift from data access to workflow execution** — external agents can now trigger ServiceNow flows, playbooks, approvals, and catalogs under full AICT governance. **Hosted/remote MCP is becoming the default** deployment model for ITSM vendors.

## Enterprise ITSM Platforms

### ServiceNow (Official + Community)

| Server | Stars | Language | License | Tools | Official |
|--------|-------|----------|---------|-------|----------|
| ServiceNow Action Fabric MCP | — | Platform | — | Configurable | Yes |
| echelon-ai-labs/servicenow-mcp | ~162 | Python | — | Role-based packages | No |
| happy-platform-mcp | — | Node.js | — | 480+ auto-generated | No |
| ShunyaAI/snow-mcp | — | Python | — | 60+ tools | No |
| jschuller/mcp-server-servicenow | ~7 | Python | — | 19 tools + 5 resources | No |
| onlyflowstech/servicenow-mcp | — | TypeScript | — | 17 tools | No |
| michaelbuckner/servicenow-mcp | ~22 | Python | — | 3 tools | No |

ServiceNow has the deepest MCP ecosystem of any ITSM platform — an **official Action Fabric MCP server** (expanded at Knowledge 2026) plus at least **seven community servers** with different approaches.

**ServiceNow Action Fabric MCP** is the official platform integration, launched as "ServiceNow Native MCP" with the Zurich release (GA September 2025, Patch 4+) and expanded at Knowledge 2026 (May 5, 2026) into the branded **Action Fabric** product. Administrators create an MCP server within the Now Assist instance, select which skills to expose as tools, and configure OAuth authentication. Any MCP client — Claude, ChatGPT, Cursor, Copilot — can discover and invoke tools. Requires Now Assist or AI Native SKU (included at no additional cost as of Knowledge 2026). The server runs through AI Control Tower (AICT) governance: consumption metering, managed OAuth, enterprise audit trails, session management, and role-based tool packages.

The headline differentiation of Action Fabric: **"Others let agents read and write data. We let agents execute governed work."** External agents (including Claude via the Anthropic partnership announced at Knowledge 2026) can trigger ServiceNow **workflows, playbooks, approval chains, service catalog actions, and business rules** — not just query or update records. Every action is identity-verified, permission-scoped, and fully auditable. H2 2026 will add additional Action Fabric capabilities.

**echelon-ai-labs/servicenow-mcp** ([GitHub](https://github.com/echelon-ai-labs/servicenow-mcp), ~162 stars, Python) is the most popular community server. It organizes tools into **role-based packages**: service_desk (incidents), catalog_builder, change_coordinator, knowledge_author, platform_developer, system_administrator, and agile_management. This role-based approach means AI agents get only the tools relevant to their persona, reducing context window usage and preventing inappropriate operations. Authentication via Basic Auth / API credentials.

**Happy-Technologies happy-platform-mcp** ([GitHub](https://github.com/Happy-Technologies-LLC/mcp-servicenow-nodejs), Node.js, npm package) takes the most ambitious approach — it **auto-generates 480+ tools across 160+ tables** from ServiceNow instance metadata. Supports multi-instance connections (multiple ServiceNow environments simultaneously), OAuth 2.0 and Basic Auth, and automatic token refresh. The metadata-driven approach means every table and field in your instance becomes a tool without manual configuration.

**ShunyaAI/snow-mcp** ([GitHub](https://github.com/shunyaai/snow-mcp), Python) provides **60+ tools** organized by module: Incidents, Changes, Users, Service Catalog, and Projects. Production-ready with built-in retry logic and exponential backoff. Includes a CLI for listing available tools.

**jschuller/mcp-server-servicenow** ([GitHub](https://github.com/jschuller/mcp-server-servicenow), ~7 stars, Python, FastMCP 3.0) stands out for its **OAuth 2.1+PKCE** authentication — the most secure auth of any community ServiceNow MCP. Provides 19 tools for incidents, CMDB, and update sets plus 5 MCP resources. Works on Tokyo+ without requiring any additional entitlements. Supports Streamable HTTP transport and includes a Claude Code Plugin with 4 skills plus a background agent for long-running operations.

**onlyflowstech/servicenow-mcp** ([GitHub](https://github.com/onlyflowstech/servicenow-mcp), TypeScript) differentiates with **CMDB graph traversal** and **ATF test execution** tools. Full CRUD plus background script execution and automated testing distinguish it from the read-heavy competitors.

**michaelbuckner/servicenow-mcp** ([GitHub](https://github.com/michaelbuckner/servicenow-mcp), ~22 stars, Python) takes a simpler, NL-focused approach with just 3 core tools: natural_language_search, natural_language_update, and update_script. Good for basic search and update workflows without the complexity of dozens of specialized tools.

### BMC (MCP Client, Not Server)

BMC takes a fundamentally different approach from other ITSM vendors. Rather than exposing its capabilities as an MCP server, **BMC HelixGPT acts as an MCP client** — it consumes external MCP servers to extend its AI agents' capabilities. Available in BMC Helix 25.2+, administrators configure MCP connections to third-party tools, enabling HelixGPT agents to invoke external tools at runtime. BMC also supports A2A (Agent-to-Agent) for cross-platform AI workflows. No dedicated open-source BMC/Remedy MCP server exists on GitHub.

## Incident Management

### PagerDuty (Official)

| Server | Stars | Language | License | Tools | Official |
|--------|-------|----------|---------|-------|----------|
| PagerDuty MCP Server | — | TypeScript | Open source | 20+ (local) / 60+ (cloud) | Yes |

**PagerDuty's official MCP server** ([pagerduty/pagerduty-mcp-server](https://github.com/PagerDuty/pagerduty-mcp-server), TypeScript) is one of the most mature ITSM MCP implementations. The local server provides **20+ tools** covering incidents, services, schedules, on-call, and escalation policies. The **cloud-hosted version** (via developer.pagerduty.com) expands to **60+ tools** including event orchestration, incident workflows, and status pages.

PagerDuty's standout feature is **safety-first design**: the server is **read-only by default**. Write operations must be explicitly enabled with the `--enable-write-tools` flag. This prevents accidental incident creation, escalation, or status changes during AI exploration. PagerDuty published a blog post on lessons learned building their MCP server, making it a reference implementation for enterprise MCP safety patterns.

Authentication via API key. Deployment options include Docker container with stdio transport, or the cloud-hosted remote MCP endpoint.

A community alternative exists at wpfleger96/pagerduty-mcp-server for those wanting a different implementation.

### incident.io (Official)

| Server | Stars | Language | License | Tools | Official |
|--------|-------|----------|---------|-------|----------|
| incident.io MCP Server | — | Hosted | — | Multiple | Yes |

**incident.io** offers an **official hosted remote MCP server** at `mcp.incident.io/mcp` (Public Beta) — one of the first ITSM vendors to provide a fully hosted MCP endpoint requiring zero local installation. Tools cover querying incidents, analyzing alerts, checking on-call schedules, managing escalations, and operational analysis.

Authentication uses **OAuth for human users** and **API key (Bearer token) for programmatic agents**. The legacy local Go server ([incident-io/incidentio-mcp-golang](https://github.com/incident-io/incidentio-mcp-golang), 6 stars) was archived in March 2026 after being superseded by the hosted version.

### Rootly (Official)

| Server | Stars | Language | License | Tools | Official |
|--------|-------|----------|---------|-------|----------|
| rootly-mcp-server | — | Python | Apache 2.0 | Multiple | Yes |

**Rootly AI Labs** ships an official MCP server ([Rootly-AI-Labs/rootly-mcp-server](https://github.com/Rootly-AI-Labs/rootly-mcp-server), Apache 2.0, Python) with a distinctive capability: **TF-IDF similarity analysis** that finds related past incidents and mines their resolutions to suggest solutions. Tools include querying incidents, checking on-call schedules, and finding similar historical incidents. Auto-generates MCP resources from OpenAPI spec. Pagination defaults to 10 items to prevent context window overflow. Currently marked as a prototype.

### FireHydrant (Official)

| Server | Stars | Language | License | Tools | Official |
|--------|-------|----------|---------|-------|----------|
| firehydrant-mcp | ~2 | TypeScript | MIT | Multiple | Yes |

**FireHydrant's official MCP server** ([firehydrant/firehydrant-mcp](https://github.com/firehydrant/firehydrant-mcp), ~2 stars, TypeScript, MIT) is distributed via npm (`firehydrant-mcp`) and also as a `.mcpb` file for drag-and-drop Claude Desktop installation. Relatively new with low adoption so far.

### Opsgenie (Community)

| Server | Stars | Language | License | Tools | Official |
|--------|-------|----------|---------|-------|----------|
| giantswarm/mcp-opsgenie | — | Go 1.24 | Apache 2.0 | Multiple | No |
| burakdirin/mcp-opsgenie | — | Node.js | — | Multiple | No |
| burakdirin/opsgenie-mcp-server | — | TypeScript | — | Alert CRUD + notes + logs | No |

**giantswarm/mcp-opsgenie** ([GitHub](https://github.com/giantswarm/mcp-opsgenie), Go 1.24, Apache 2.0) is the most comprehensive Opsgenie MCP server. Built by Giant Swarm (a Kubernetes company), it covers alert management (list/get/acknowledge/unacknowledge), team management, and heartbeat monitoring with advanced alert filtering. Supports **three transport modes**: stdio, SSE, and Streamable HTTP. Includes a self-update capability.

**burakdirin/mcp-opsgenie** ([GitHub](https://github.com/burakdirin/mcp-opsgenie), Node.js) adds MCP resources and prompts for incident response and post-incident analysis. A second TypeScript implementation from the same developer focuses on alert CRUD, notes, logs, and custom details.

No official Opsgenie MCP server exists, though the Atlassian JSM tools in the official Atlassian MCP partially overlap with Opsgenie functionality.

## IT Helpdesk & Ticketing

### Zendesk (Community)

| Server | Stars | Language | License | Tools | Official |
|--------|-------|----------|---------|-------|----------|
| reminia/zendesk-mcp-server | ~79 | Python | — | Tickets, comments, Help Center | No |
| mattcoatsworth/zendesk-mcp-server | — | — | — | Support, Talk, Chat, Guide | No |
| wlaubernds/zendesk-mcp-server | — | — | — | Read-only | No |
| CDataSoftware/zendesk-mcp-server-by-cdata | — | — | — | Read-only (JDBC) | No |

**Zendesk has no official MCP server** but strong community coverage. **reminia/zendesk-mcp-server** ([GitHub](https://github.com/reminia/zendesk-mcp-server), ~79 stars, Python) is the most popular, covering ticket management, comments, Help Center article retrieval, and specialized prompts for ticket analysis and response drafting.

**mattcoatsworth/zendesk-mcp-server** provides the broadest Zendesk product coverage, spanning Support, Talk, Chat, and Guide. For security-conscious environments, **wlaubernds/zendesk-mcp-server** enforces **read-only access with zero write permissions**. **CDataSoftware's** enterprise-oriented version connects via JDBC drivers.

### Freshservice / Freshworks (Official MCP Gateway + Community)

| Server | Stars | Language | License | Tools | Official |
|--------|-------|----------|---------|-------|----------|
| Freshworks MCP Gateway (Inbound) | — | Hosted | Enterprise | 28 | Yes |
| Freshworks MCP Gateway (Outbound) | — | Hosted | Growth+ | External tools | Yes |
| effytech/freshservice_mcp | — | Python | MIT | Tickets, changes, assets | No |
| effytech/freshdesk_mcp | — | Python | MIT | Support operations | No |
| Enreign/freshdeck-mcp | — | TypeScript | — | Tickets, contacts, agents | No |

**Freshworks shipped an official bidirectional MCP Gateway** at Refresh 2026 (May 14, 2026), upgrading from community-only coverage to official support. The gateway operates in two directions:

**Inbound MCP** (Enterprise plan, Early Access) lets external AI clients — Claude, Cursor, VS Code, Microsoft Copilot Studio, ChatGPT, and Gemini — connect to Freshservice data. It exposes **28 tools across 6 categories**: tickets (fetch, create, update, add notes), assets (fetch, create, update), users/agents (lookup), onboarding/offboarding workflows, service catalog (placement and search), and knowledge base (categories, folders, articles). Rate limits during Early Access: 100 tool calls per minute, 5,000 per month.

The gateway's core security design: **hardcoded tools, not arbitrary LLM queries.** Freshworks enforces a defined operation set rather than allowing free-form AI queries against production data — a deliberate choice to prevent SQL injection risks and hallucinated queries. This mirrors PagerDuty's read-only-by-default safety philosophy, applied to tool scope.

**Outbound MCP** (Growth, Pro, and Enterprise plans with active Freddy AI Agent Studio) lets Freddy AI pull live context from third-party tools including Atlassian, Notion, Linear, and ClickUp — without custom integration code.

**Freddy AI Agent Studio**, the no-code agent-building platform powering outbound MCP, lets IT teams build custom agents from a visual interface, deploy pre-built templates, and push agents to Microsoft Teams, Slack, or employee portals. Freshworks cites their internal analysis: 47% of IT tickets arrive outside standard business hours, with after-hours response lag over an hour — the primary business case for autonomous agents.

**Amerisure** reduced daily ticket trend analysis from one hour to three minutes using Freddy Insights. Other named Freshservice customers include Bridgestone, New Balance, S&P Global, and Sony Music. Independent analysis by The Futurum Group cites 168% ROI over 3 years for Freshservice customers (general ITSM claim, not specific to Agent Studio).

The Freddy AI Agent Studio and Inbound MCP Gateway are in Early Access as of May 2026 — not generally available, with no public pricing disclosed for Agent Studio.

Community servers remain useful for non-Enterprise plans or simpler integrations: **effytech/freshservice_mcp** ([GitHub](https://github.com/effytech/freshservice_mcp), Python, MIT) covers ticket CRUD, change management, and asset management. The same developer maintains **effytech/freshdesk_mcp** for Freshdesk support operations. **Enreign/freshdeck-mcp** (TypeScript) adds automatic retry with exponential backoff.

### ManageEngine ServiceDesk Plus (Community + Official Beta)

| Server | Stars | Language | License | Tools | Official |
|--------|-------|----------|---------|-------|----------|
| PTTG-IT/SDP-MCP | — | — | MIT | 16 tools | No |
| SChinmaya15/Manage-Engine-MCP | — | — | — | SDP + EndpointCentral | No |
| Analytics Plus MCP | — | Hosted | — | Analytics/BI | Yes (Beta) |

**PTTG-IT/SDP-MCP** ([GitHub](https://github.com/PTTG-IT/SDP-MCP), MIT) provides **16 tools** for ServiceDesk Plus Cloud with full CRUD on all entities, email communication, and ticket conversations. OAuth with robust token management, rate limit protection, and a mock API server for testing. Reported 100% tool success rate.

**SChinmaya15/Manage-Engine-MCP** ([GitHub](https://github.com/SChinmaya15/Manage-Engine-MCP)) uniquely bridges **ITSM and endpoint management**, covering both ServiceDesk Plus (tickets, knowledge base) and EndpointCentral (software management, computer management, deployment) with OAuth2 for both products.

**ManageEngine Analytics Plus** offers an official beta MCP server focused on analytics and BI rather than ticketing.

### TOPdesk (Community)

| Server | Stars | Language | License | Tools | Official |
|--------|-------|----------|---------|-------|----------|
| dakpanbaviaan/topdeskmcp | — | TypeScript | — | Auto-generated from OpenAPI | No |
| GerbenRoebersen/Topdesk_MCP_python | — | Python | — | Tickets, search, attachments | No |

Two community servers cover TOPdesk. **dakpanbaviaan/topdeskmcp** (TypeScript) auto-generates tools from TOPdesk's OpenAPI spec. **GerbenRoebersen/Topdesk_MCP_python** (Python) uses the TOPdeskPy SDK for ticket listing, search, and attachment conversion to Markdown. A `topdesk-mcp` PyPI package is also available.

## Service Desk Within Dev Platforms

### Jira Service Management (Official)

| Server | Stars | Language | License | Tools | Official |
|--------|-------|----------|---------|-------|----------|
| Atlassian MCP Server (JSM tools) | — | Hosted | — | JSM alerts, on-call, teams | Yes |
| sooperset/mcp-atlassian | ~2,600 | Python | MIT | 72 tools (Jira + Confluence) | No |

The **Atlassian official remote MCP server** ([atlassian/atlassian-mcp-server](https://github.com/atlassian/atlassian-mcp-server)) includes dedicated **JSM tools**: `getJsmOpsAlerts` (query alerts by ID/alias/search), `updateJsmOpsAlert` (acknowledge/close/escalate), `getJsmOpsScheduleInfo` (on-call schedules and responders), and `getJsmOpsTeamInfo` (teams with escalation policies). Hosted on Cloudflare. JSM tools require API token auth (not OAuth). First official partner is Anthropic.

**sooperset/mcp-atlassian** ([GitHub](https://github.com/sooperset/mcp-atlassian), ~2,600 stars, Python, MIT) is the most popular community Atlassian MCP server with **72 tools** covering Jira and Confluence. Supports both Cloud and Server/Data Center.

**codeownersnet/atlas** combines Jira, Confluence, and Opsgenie in a single MCP server.

## Multi-Platform ITSM

### madosh/MCP-ITSM

| Server | Stars | Language | License | Tools | Official |
|--------|-------|----------|---------|-------|----------|
| MCP-ITSM | — | Node.js | — | Unified CRUD + KB search | No |

**madosh/MCP-ITSM** ([GitHub](https://github.com/madosh/MCP-ITSM), Node.js) provides **unified access to five ITSM platforms** — ServiceNow, Jira, Zendesk, Ivanti Neurons, and Cherwell — through consistent tool definitions. Includes intelligent routing to the appropriate ITSM system, so AI agents use the same tools regardless of the backend. Covers ticket creation, retrieval, updates, assignment, and knowledge base search. Supports HTTP and stdio transport.

## What's Missing

- **Squadcast** — no MCP server found despite being a growing incident management platform
- **xMatters** — no MCP server
- **SysAid** — no MCP server
- **Ivanti** — no dedicated server (only third-party connectors and MCP-ITSM multi-platform support)
- **Cherwell** — only via MCP-ITSM multi-platform
- **StatusPage.io** — no major dedicated server (PagerDuty cloud version includes status page tools)
- **Problem management** — ITIL problem management workflows (root cause analysis, known error databases) are underrepresented
- **CMDB** — only ServiceNow servers offer CMDB traversal; no standalone CMDB MCP servers
- **Change advisory board (CAB)** automation — no MCP server supports CAB workflows
- **SLA monitoring** — no server focuses specifically on SLA tracking and breach prediction

## Industry Trends

The ITSM MCP landscape reveals three deployment approaches:

1. **MCP Server providers** (ServiceNow, PagerDuty, incident.io, Atlassian JSM, Freshworks) — exposing ITSM capabilities for any AI client to consume
2. **MCP Client consumers** (BMC HelixGPT, Freshworks Freddy AI) — using MCP to connect their AI agents to external tools rather than (or in addition to) exposing their own
3. **Hosted/remote MCP** is emerging as the default — Atlassian, incident.io, PagerDuty, and Freshworks all offer cloud-hosted endpoints, reducing setup friction

Freshworks' May 2026 MCP Gateway is notable for being **bidirectional** — simultaneously a provider (inbound) and a consumer (outbound). This dual-mode architecture, where a platform both exposes capabilities and consumes external tools, represents an emerging pattern likely to be adopted by other enterprise ITSM vendors.

Safety patterns are maturing: PagerDuty's read-only default, ServiceNow's AI Control Tower governance, Rootly's pagination limits, and Freshworks' hardcoded-tools-only design all show the industry learning from early MCP security mistakes.

## Rating: 4.0 / 5

ITSM earns one of the highest ratings in our review series. **Seven vendors now have official MCP servers** — more than most enterprise categories. ServiceNow's native platform support plus deep community ecosystem sets the standard. PagerDuty's safety-first design is a model for other vendors. Freshworks' May 2026 bidirectional MCP Gateway added the seventh official vendor and introduced the dual-mode provider+consumer pattern. The main gaps are in the long tail — Squadcast, xMatters, and SysAid have no presence — and in ITIL process automation (problem management, CAB workflows, SLA monitoring). The shift toward hosted remote MCP shows the category maturing beyond developer-only tooling toward enterprise-ready AI integration.

