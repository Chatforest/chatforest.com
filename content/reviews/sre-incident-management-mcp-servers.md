---
title: "SRE & Incident Management MCP Servers — PagerDuty, Rootly, FireHydrant, Grafana OnCall, incident.io, and More"
date: 2026-04-25T21:30:00+09:00
description: "SRE and incident management MCP servers reviewed: PagerDuty (69 stars, Python, 69 tools, official, 5 MCP Apps), Rootly (43 stars, Python, 150+ tools, v2.3.8 perf improvements, AI-powered analysis), Grafana OnCall (3K stars, Go, v0.14.0, mcp-grafana), FireHydrant (4 stars, stalled), incident.io (hosted remote MCP), OpsGenie archived, ilert (14 stars, dormant), Better Stack (remote MCP), ServiceNow (252 stars, echelon-ai-labs). Rating: 4.0/5."
og_description: "SRE & incident management MCP servers: PagerDuty (69 stars, 69 tools, 5 MCP Apps), Rootly (43 stars, 150+ tools, v2.3.8), Grafana (3K stars, v0.14.0), ServiceNow (252 stars, new), OpsGenie archived. Rating: 4.0/5."
content_type: "Review"
card_description: "SRE and incident management tools for AI-assisted on-call, alerting, and incident response through MCP servers — enabling AI agents to triage incidents, check who's on-call, find related past incidents, and coordinate response without leaving the IDE. **Most tools** — PagerDuty/pagerduty-mcp-server (69 stars, Apache-2.0, Python) is the official PagerDuty MCP server with 69 tools plus 5 embedded MCP Apps (Incident Command Center with AI similar incident detection, On-Call Manager, Compensation Report, Service Dependency Graph, Onboarding Wizard). Read-only by default with explicit --enable-write-tools flag. **AI-powered analysis** — Rootly-AI-Labs/Rootly-MCP-server (43 stars, Python, v2.3.8) provides 150+ tools: find_related_incidents (TF-IDF similarity), suggest_solutions (historical resolution mining), check_oncall_health_risk, get_oncall_handoff_summary. v2.3.8 optimized alert lookup from 41s→200ms. OAuth2 primary auth. **Observability platform** — grafana/mcp-grafana (3K stars, Go, v0.14.0) includes 7 OnCall tools and 4 Incident tools as part of its 50+ tool observability server. New generic API request tool. Amazon Athena, Snowflake, VictoriaMetrics support added. **Enterprise ITSM** — echelon-ai-labs/servicenow-mcp (252 stars, Python) covers ServiceNow incidents, service catalog, change management, agile, workflows, knowledge base with RBAC packages. Leading community ServiceNow MCP. **Reliability platform** — firehydrant/firehydrant-mcp (4 stars, MIT, TypeScript, stalled Feb 2026). Incident management, alert tracking, retrospective generation. **Hosted remote MCP** — incident.io hosted MCP (superseded open-source prototype archived April 2026). Full incident lifecycle. **Alert management** — giantswarm/mcp-opsgenie (9 stars, Go, ARCHIVED May 12, 2026) — 8 tools, archived ahead of OpsGenie's April 2027 EOL. **Alerting platform** — iLert/mcp-ilert (14 stars, MIT, dormant since Sep 2025) remote Streamable HTTP. **Observability stack** — Better Stack remote MCP at mcp.betterstack.com, OAuth auth, ClickHouse SQL queries. Rating: 4.0/5 — PagerDuty's 69-tool server + MCP Apps and Rootly's v2.3.8 performance improvements strengthen the category. ServiceNow gap filled by echelon-ai-labs (252 stars). Negatives: mcp-opsgenie archived, iLert/FireHydrant stalled, overall adoption still low."
last_refreshed: 2026-05-21
---

It's 3 AM. Your phone buzzes. A P1 incident just fired. You open your laptop, fumble between PagerDuty tabs, Slack channels, and runbook wikis, trying to figure out who's on-call, what changed, and whether this happened before.

Now imagine asking your AI assistant: "What's firing right now? Who's on-call? Have we seen this before? What fixed it last time?" — and getting answers in seconds, from inside your editor, without context-switching between six different tools.

That's what SRE and incident management MCP servers enable. They connect AI agents directly to your incident management platform — PagerDuty, Rootly, FireHydrant, Grafana OnCall, incident.io, OpsGenie, ilert, Better Stack — so your AI can triage incidents, check on-call schedules, find similar past incidents, and even help coordinate response.

This review covers **MCP servers for incident management, on-call scheduling, and incident response platforms**. For monitoring and observability (Prometheus, Grafana dashboards, Datadog), see [Monitoring & Observability MCP Servers](/reviews/monitoring-observability-mcp-servers/). For uptime monitoring specifically, see [Monitoring & Uptime MCP Servers](/reviews/monitoring-uptime-mcp-servers/). For chaos engineering, see [Chaos Engineering MCP Servers](/reviews/chaos-engineering-mcp-servers/).

Part of our **[DevOps MCP category](/categories/devops/)**. The headline finding: **every major incident management platform now offers MCP support**, with PagerDuty leading in tool breadth (62 tools) and Rootly leading in AI-powered incident analysis (TF-IDF similarity matching, solution suggestion from historical data). The market is splitting between local MCP servers (PagerDuty, Rootly, OpsGenie) and hosted remote MCP (incident.io, ilert, Better Stack).

## Official Platform MCP Servers

### PagerDuty/pagerduty-mcp-server

| Server | Stars | Language | License | MCP Features |
|--------|-------|----------|---------|--------------|
| [pagerduty-mcp-server](https://github.com/PagerDuty/pagerduty-mcp-server) | 69 | Python | Apache-2.0 | 69 tools + 5 MCP Apps |

**The most comprehensive incident management MCP server available.** PagerDuty's official server now covers 69 tools across 13 categories — up from 62 — with Status Pages expanded to 9 tools and Teams to 7:

- **Incidents (13 tools)** — create, get, list, manage incidents; add notes and responders; retrieve alerts, notes, related incidents, past incidents, and outlier incidents
- **Status Pages (9 tools)** — create posts and updates, manage impacts, severities, and statuses (added one tool since April)
- **Teams (7 tools)** — full team management including add/remove members (added one tool)
- **Event Orchestrations (6 tools)** — get orchestrations, global/router/service configs, append rules
- **Schedules (6 tools)** — create, get, list schedules; create overrides; list schedule users
- **Services (4 tools)** — create, get, list, update services
- **Incident Workflows (3 tools)** — get, list, and start workflow instances
- **Escalation Policies (2 tools)** — list and get escalation policies
- **On-Call (1 tool)** — list on-call schedules
- **Users, Log Entries, Change Events, Alert Grouping** — additional operational tools

**MCP Apps (new, May 2026):** PagerDuty launched five embedded React UI apps that render directly inside IDEs — no separate HTTP server needed:
- **Incident Command Center** — includes AI-powered similar incident detection
- **On-Call Manager** — schedule visualization and override management
- **On-Call Compensation Report** — shift analytics and compensation tracking
- **Service Dependency Graph** — visual service relationship mapping
- **Onboarding Wizard** — guided first-time setup

**Safety model:** Read-only by default. Write tools require explicitly starting the server with `--enable-write-tools`. This is the right default for production incident management.

**Why it matters:** PagerDuty now has the most tool breadth in this category (69 tools) plus embedded UI apps — a significant leap beyond pure API wrapping. The Incident Command Center's AI-powered similar incident detection means PagerDuty is starting to close the gap with Rootly's intelligence features. The outlier incident and past incident tools remain especially useful for pattern recognition during active incidents.

**Limitation:** 69 stars remains low for an official server from a company this size. Docker deployment adds setup friction. EU region support requires separate configuration. The one-tool on-call category still feels thin.

### Rootly-AI-Labs/Rootly-MCP-server

| Server | Stars | Language | License | MCP Features |
|--------|-------|----------|---------|--------------|
| [Rootly-MCP-server](https://github.com/Rootly-AI-Labs/Rootly-MCP-server) | 43 | Python | MIT | 150+ tools |

**The most AI-native incident management MCP server.** Rootly's server goes beyond API wrapping to provide intelligent incident analysis tools that no other platform offers:

- **find_related_incidents** — uses TF-IDF similarity analysis to find historically similar incidents. Not keyword matching — actual statistical text similarity across your incident history
- **suggest_solutions** — mines past incident resolutions to recommend actionable solutions for current incidents. When a P1 fires at 3 AM, this is the tool that tells you "last time this happened, we rolled back the auth service deployment"
- **check_oncall_health_risk** — detects responder workload problems before they cause burnout. Analyzes shift patterns and incident load
- **check_responder_availability** — real-time responder status
- **get_oncall_handoff_summary** — provides context for shift transitions so the next on-call person isn't starting from scratch
- **get_oncall_shift_metrics** — shift counts, hours, and days on-call grouped by user, team, or schedule with primary/secondary role tracking

**v2.3.8 (May 2026) — significant performance improvements:** Alert lookup optimized from **41 seconds to ~200ms** (parallelized pagination). Cold-cache on-call lookups dropped from ~15s to ~1s. A critical tool duplication bug was fixed — the `listIncidents`/`list_incidents` naming conflict was causing LLM client errors in some configurations. OAuth2 is now the primary authentication method (previously secondary). MCPcat analytics integration added for usage tracking.

**Tool subsets now documented by workflow:** Incident Response (25 tools), On-Call Management (35 tools), Monitoring/Alerting (40 tools), Post-Incident Analysis (30 tools), Analytics/Reporting (15 tools) — making it easier to limit which tools are exposed.

**Dynamic tool generation** from Rootly's OpenAPI spec means the server automatically exposes new API endpoints as they're added. Smart pagination defaults to 10 items per request on incident endpoints to prevent context window overflow.

**Deployment flexibility:** Hosted (HTTP Streamable, SSE), local (uv, Docker, pip), or self-hosted with configurable tool subsets.

**Why it matters:** Rootly's MCP server remains the most AI-native option. The v2.3.8 performance work matters in practice — nobody wants to wait 41 seconds for an alert lookup during an active incident. The TF-IDF similarity matching and solution suggestion tools transform incident response from "search through Confluence" to "here are the 3 most similar incidents and what fixed them." 150+ tools is still the largest tool count in this review.

**Limitation:** 43 stars suggests continued early adoption. The sheer number of tools (150+) may overwhelm some MCP clients. The AI analysis tools depend on having sufficient historical incident data to be useful.

### firehydrant/firehydrant-mcp

| Server | Stars | Language | License | MCP Features |
|--------|-------|----------|---------|--------------|
| [firehydrant-mcp](https://github.com/firehydrant/firehydrant-mcp) | 4 | TypeScript | MIT | Incident + alert tools |

**Official FireHydrant MCP server for their all-in-one reliability platform.** Auto-generated via Speakeasy from FireHydrant's API spec:

- Incident management — list, search, create, and manage incidents
- Alert tracking — view and search alerts from monitoring integrations
- Retrospective support — access post-incident data for review
- Multi-IDE support — Claude Desktop, Cursor, VS Code, Windsurf
- NPM package (`firehydrant-mcp`) with drag-and-drop bundle for Claude Desktop

**Why it matters:** FireHydrant combines alerting, on-call, and incident management into one platform. Their MCP server brings that unified view to AI assistants. The Speakeasy auto-generation means the MCP server stays current with API changes automatically.

**Limitation:** 4 stars, v0.0.4, and **no commits since February 24, 2026** — development appears stalled. Auto-generated code means tool descriptions may not be optimized for LLM consumption. Specific tool enumeration isn't well-documented in the README.

### incident.io — Hosted Remote MCP

**incident.io launched an officially supported hosted MCP server in March 2026**, superseding their open-source prototype ([incidentio-mcp-golang](https://github.com/incident-io/incidentio-mcp-golang), 30 stars, Go, archived April 1, 2026).

The hosted server connects via remote MCP — no local server installation needed. Configure your MCP client to point at incident.io's endpoint with your API key and you're connected. Full incident lifecycle management: create, update, close incidents, manage alerts, run workflows.

**Why it matters:** incident.io's move from open-source local server to hosted remote MCP is the direction the industry is heading. Remote MCP eliminates local setup friction, ensures you're always on the latest version, and lets the vendor control security and performance. The open-source prototype had 30 stars and 21 forks — meaningful community interest — but the hosted version is now the supported path.

**Limitation:** Vendor-hosted means you're dependent on incident.io's infrastructure. No self-hosting option for the current MCP server. The archived prototype leaves users who contributed to it without a maintained fork.

**Documentation:** [docs.incident.io/ai/remote-mcp](https://docs.incident.io/ai/remote-mcp)

## Observability Platform Integration

### grafana/mcp-grafana (OnCall + Incident)

| Server | Stars | Language | License | MCP Features |
|--------|-------|----------|---------|--------------|
| [mcp-grafana](https://github.com/grafana/mcp-grafana) | 3,000 | Go | Apache-2.0 | 50+ tools (11 OnCall/Incident) |

**Grafana's unified MCP server includes OnCall and Incident management alongside dashboards, Prometheus, Loki, and alerting.** v0.14.0 (May 8, 2026) significantly expanded the server — six new datasources (Amazon Athena, Snowflake, OpenSearch, VictoriaMetrics/VictoriaLogs, InfluxDB, Graphite) and a generic API request tool. The incident/on-call tool count grew from 7 to 11:

**OnCall tools (7, up from 4):**
- `list_schedules` — view and manage on-call schedules
- `get_shift_details` — detailed information about specific on-call shifts
- `get_current_oncall_users` — who's on-call right now for a given schedule
- `list_alert_groups` — view and filter alert groups by state, integration, labels, time range
- `get_alert_group` — detailed alert group data (new)
- `list_oncall_teams` — enumerate OnCall teams (new)
- `list_oncall_users` — list all OnCall users (new)

**Incident tools (4, up from 3):**
- `list_incidents` — search and retrieve incidents from Grafana Incident
- `create_incident` — create new incidents
- `add_activity_to_incident` — append activity items to existing incidents
- `get_incident` — retrieve a specific incident by ID (new)

**Generic API request tool (new in v0.14.0):** Acts like `gh api` for Grafana — allows LLMs to hit any Grafana API endpoint without needing a dedicated tool implementation. Effectively an escape hatch for any Grafana operation not yet covered by named tools.

**Why it matters:** The value isn't the 11 incident/on-call tools in isolation — it's having them in the same MCP server as your dashboards, Prometheus queries, Loki log searches, and alerting rules. During an incident, you can check who's on-call, pull up the relevant dashboard, query the metrics that are alerting, search recent logs for errors, and create an incident — all through one server connection. The generic API tool now makes any remaining Grafana operation accessible. VictoriaMetrics support extends this to Grafana-adjacent observability stacks. 3K stars reflects Grafana's massive community.

**Changes in v0.13.0:** `search_logs` tool removed (was broken — if you relied on it, use Loki query tools instead). Memory protection added via `io.LimitReader` to prevent exhaustion from oversized API responses.

**Limitation:** Requires Grafana OnCall and Grafana Incident to be set up — Grafana Cloud features or self-hosted additions. The incident tools are still basic (4 tools vs. PagerDuty's 13). Can disable OnCall tools with `--disable-oncall` if not needed.

## Alert Management Platforms

### giantswarm/mcp-opsgenie

| Server | Stars | Language | License | MCP Features |
|--------|-------|----------|---------|--------------|
| [mcp-opsgenie](https://github.com/giantswarm/mcp-opsgenie) | 9 | Go | Apache-2.0 | 8 tools — **ARCHIVED** |

**⚠️ ARCHIVED May 12, 2026.** Giant Swarm archived the repository (read-only, no new development). The archival timing aligns with OpsGenie's approaching end-of-life: Atlassian has confirmed **OpsGenie will be sunset on April 5, 2027**, with customers migrating to Jira Service Management.

The server's final state (8 tools) remains functional for existing OpsGenie users: alert management (list, get, acknowledge, unacknowledge), team management (list, get), heartbeat monitoring (list, get). Multi-transport (stdio, SSE, HTTP) and self-update capability were maintained to the end.

**The OpsGenie sunset factor:** With the EOL date confirmed for April 2027 and the primary community MCP server now archived, any new investment in OpsGenie MCP tooling is inadvisable. Teams should consider migrating to PagerDuty, Rootly, Grafana OnCall, or ilert.

**Also available (maintained status unknown):** [burakdirin/mcp-opsgenie](https://github.com/burakdirin/mcp-opsgenie) — tools, resources, and prompts for OpsGenie incident management. [daviddykeuk/opsgenie-mcp](https://github.com/daviddykeuk/opsgenie-mcp) — simpler alerts-focused alternative.

### iLert/mcp-ilert

| Server | Stars | Language | License | MCP Features |
|--------|-------|----------|---------|--------------|
| [mcp-ilert](https://github.com/iLert/mcp-ilert) | 14 | — | MIT | Remote Streamable HTTP |

**Official ilert MCP server using remote Streamable HTTP transport.** ilert is a European alerting and incident management platform (GDPR-compliant, EU-hosted):

- Remote MCP server — no local installation, connect directly via Streamable HTTP
- API key authentication
- Supports MCP clients that support remote servers natively; `mcp-remote` wrapper available for clients that don't
- Full alerting and incident management capabilities

**Why it matters:** ilert's remote MCP approach mirrors incident.io's — vendor-hosted, zero-friction setup. For European teams with data sovereignty requirements, ilert's EU hosting is a differentiator over US-based platforms.

**Limitation:** **Dormant since September 4, 2025** — no GitHub commits in over 8 months. The server is remote-hosted (iLert's own infrastructure), so users may still be on a current version even without GitHub activity, but the repository itself shows no active development. Tool list not enumerated in the README. 14 stars.

### Better Stack — Remote MCP

**Better Stack offers a remote MCP server at mcp.betterstack.com** with OAuth authentication (browser-based sign-in, no token management):

- Uptime monitoring — SLA summaries, availability calculations, response time analysis
- Log analysis — ClickHouse SQL queries against telemetry data (logs, spans, metrics, exceptions)
- Incident management — integrated with their uptime monitoring
- Status pages — part of their reliability platform
- Chart rendering — line charts from query results

**Why it matters:** Better Stack's MCP server covers the full reliability stack: uptime monitoring, logs, incidents, and status pages. The OAuth flow is notably frictionless compared to API key management. ClickHouse SQL queries give power users direct access to telemetry data.

**Limitation:** Fully hosted — no self-hosting option. Requires Better Stack account. Separate from their GitHub repos ([betterstack-logs-mcp](https://github.com/DrDroidLab/betterstack-logs-mcp) exists for log-focused use).

## ServiceNow / ITSM

ServiceNow was listed as a gap in our previous review. That gap has been meaningfully filled:

### echelon-ai-labs/servicenow-mcp

| Server | Stars | Language | License | MCP Features |
|--------|-------|----------|---------|--------------|
| [servicenow-mcp](https://github.com/echelon-ai-labs/servicenow-mcp) | 252 | Python | — | Incidents, service catalog, changes, workflows, knowledge base |

**The leading community ServiceNow MCP server** by a significant margin. Covers the full ITSM surface:

- **Incidents** — create, retrieve, update, close incidents; query by status, priority, assignment group
- **Service Catalog** — browse and submit service requests
- **Change Management** — create and manage change requests
- **Agile (Epics/Stories)** — access agile development work items
- **Workflows** — trigger and monitor automated workflows
- **Knowledge Base** — search and retrieve articles
- **RBAC** — role-based tool packages so agents only see what they're authorized to access
- **Active maintenance** — updated within the last month; 252 stars puts it well above most incident management servers in this category

**Why it matters:** ServiceNow is the dominant ITSM platform in enterprise environments — it's where IT incidents, change requests, and service tickets live for a huge portion of Global 2000 companies. Having a well-maintained MCP server means AI agents can create, update, and query ServiceNow records without custom integration work. The RBAC packaging makes this viable for real enterprise deployments where you need to control what the AI can access.

**Also available:**
- **[Happy-Technologies-LLC/happy-platform-mcp](https://github.com/Happy-Technologies-LLC/happy-platform-mcp)** (43 stars) — Multi-Instance ServiceNow MCP Server v3.1, JavaScript, active maintenance
- **[aartiq/servicenow-mcp](https://github.com/aartiq/servicenow-mcp)** (27 stars) — TypeScript, ITOM/ITSM/CMDB, OAuth support
- **[jschuller/mcp-server-servicenow](https://github.com/jschuller/mcp-server-servicenow)** (10 stars) — 19 tools, OAuth 2.1+PKCE

## Community and Emerging Servers

### FlashDuty

- **[futuretea/flashduty-mcp-server](https://github.com/futuretea/flashduty-mcp-server)** — Very new (May 2026). [FlashDuty](https://flashduty.com/) is an incident management platform competing with PagerDuty. Tools cover list/create/acknowledge/resolve/reopen/snooze incidents, alert management, MTTA/MTTR analytics, on-call schedules, and similar incident discovery. Worth monitoring as an emerging alternative — especially for teams in Asia-Pacific where FlashDuty has stronger market presence.

### Additional PagerDuty Servers

- **[wpfleger96/pagerduty-mcp-server](https://github.com/wpfleger96/pagerduty-mcp-server)** — community PagerDuty MCP server predating the official release
- **[naveen09/mcp_pagerduty](https://github.com/naveen09/mcp_pagerduty)** — lightweight PagerDuty MCP integration

### Additional OpsGenie Servers

- **[burakdirin/mcp-opsgenie](https://github.com/burakdirin/mcp-opsgenie)** — comprehensive OpsGenie server with tools, resources, and prompts for incident management
- **[burakdirin/opsgenie-mcp-server](https://github.com/burakdirin/opsgenie-mcp-server)** — alert management capabilities (list, create, acknowledge, close)
- **[daviddykeuk/opsgenie-mcp](https://github.com/daviddykeuk/opsgenie-mcp)** — simple alerts-focused OpsGenie integration

### Squadcast

- **[DEEJ4Y/squadcast-mcp-server](https://github.com/DEEJ4Y/squadcast-mcp-server)** (0 stars, TypeScript) — basic Squadcast integration for personal use. On-call lookup, incident management (retrieve, acknowledge, resolve), status page updates, schedule creation. Requires NodeJS v20.19.0.

### AWS DevOps Agent

AWS announced general availability of a DevOps Agent for automated incident investigation in April 2026. It integrates with CloudWatch, PagerDuty, Datadog, Dynatrace, New Relic, Splunk, Grafana, GitHub, GitLab, and Azure DevOps via MCP. When an incident triggers (CloudWatch alarm, PagerDuty alert, ServiceNow ticket), the agent investigates immediately, accessing runbook libraries and executing predefined remediation actions. This represents the next evolution: AI agents that don't just read incident data but actively investigate and remediate.

## Market Landscape

### Local vs. Remote MCP

The SRE tooling space is splitting into two deployment models:

| Approach | Examples | Pros | Cons |
|----------|----------|------|------|
| Local MCP server | PagerDuty, Rootly, OpsGenie | Self-hosted, audit-friendly, offline capable | Setup friction, version management |
| Remote hosted MCP | incident.io, ilert, Better Stack | Zero setup, always current, vendor-managed | Vendor dependency, requires connectivity |

incident.io's shift from open-source local (archived) to hosted remote (supported) signals where the market is heading. Expect PagerDuty and Rootly to add remote MCP options.

### Tool Breadth Comparison

| Platform | Stars | Tools | AI Analysis | On-Call | Incidents | Status Pages |
|----------|-------|-------|-------------|--------|-----------|--------------|
| PagerDuty | 69 | 69 + 5 Apps | AI similar incidents (Incident Command Center) | Yes | 13 tools | 9 tools |
| Rootly | 43 | 150+ | TF-IDF similarity, solution suggestion | Yes | Yes | — |
| Grafana | 3,000 | 11 (OnCall/Incident) | — | 7 tools | 4 tools | — |
| ServiceNow | 252 | Incidents, catalog, changes, KB | — | — | Yes | — |
| FireHydrant | 4 | Multiple (stalled) | — | Yes | Yes | — |
| incident.io | — | Hosted | — | — | Yes | — |
| OpsGenie | 9 | 8 (ARCHIVED) | — | — | Alerts | — |

### What's Missing

- **Splunk On-Call (VictorOps) MCP** — still no MCP server despite Splunk's observability platform presence
- **Postmortem/retrospective MCP** — tools for analyzing incident patterns over time, generating action items, tracking remediation
- **Runbook execution MCP** — connecting AI agents to executable runbooks (AWS DevOps Agent is the closest, but it's a full agent, not an MCP server)
- **Multi-platform aggregation** — no MCP server that unifies incidents across PagerDuty + Grafana + ServiceNow (the [MCP Proxy, Router & Aggregator Tools](/reviews/mcp-proxy-router-aggregator-servers/) could fill this gap)
- **ServiceNow ITSM MCP** — partially filled: echelon-ai-labs/servicenow-mcp (252 stars) covers the main ITSM surface, though no official ServiceNow-published server exists yet

## Rating: 4.0 / 5

**Every major incident management platform now has MCP support** — PagerDuty (official, 69 tools + 5 MCP Apps), Rootly (AI-powered analysis, 150+ tools, v2.3.8 performance), FireHydrant (official, stalled), incident.io (hosted remote), Grafana OnCall (v0.14.0, 11 incident/oncall tools), ServiceNow (community, 252 stars), ilert (official remote, dormant), Better Stack (remote). The breadth is impressive and expanding.

**PagerDuty's 69-tool server is now the most complete** for traditional incident management, with the new MCP Apps (Incident Command Center, On-Call Manager, Compensation Report, Service Dependency Graph) adding UI capabilities that go beyond pure API access. **Rootly's AI-powered analysis tools remain the most innovative** — TF-IDF similarity matching and solution suggestion from historical data, with v2.3.8 eliminating the painful 41-second alert lookup latency. **Grafana's unified observability approach** is the most architecturally elegant — v0.14.0 expanded to 11 incident/oncall tools plus a generic API escape hatch. **ServiceNow's community ecosystem** (echelon-ai-labs leading at 252 stars) fills the previously missing enterprise ITSM gap.

**Deducted 1.0 for:**
- **Low adoption** — PagerDuty's official server has 69 stars, FireHydrant has 4. These are established companies with thousands of customers, yet MCP adoption remains minimal
- **OpsGenie archival** — giantswarm/mcp-opsgenie archived May 12, 2026, ahead of OpsGenie's April 2027 EOL. A platform disappearing and its leading MCP server archived within months of review is a concrete negative
- **iLert and FireHydrant stalled** — iLert's GitHub repository dormant since September 2025; FireHydrant no commits since February 2026. Remote hosted servers may still work, but dark repos erode confidence
- **Limited write capabilities** — several servers default to read-only (safe, but limits incident response automation)
- **No cross-platform aggregation** — teams using PagerDuty + ServiceNow + Grafana can't get a unified incident view through MCP yet

The SRE MCP space is functionally complete and maturing. The tools work, the performance is improving (Rootly v2.3.8), and the feature sets are expanding (PagerDuty MCP Apps, Grafana v0.14.0). The remaining gap is adoption — these MCP servers should be table stakes for incident response workflows, but most teams haven't made that shift yet.
