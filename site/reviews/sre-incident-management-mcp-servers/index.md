# SRE & Incident Management MCP Servers — PagerDuty, Rootly, FireHydrant, Grafana OnCall, incident.io, and More

> SRE and incident management MCP servers reviewed: PagerDuty (63 stars, Python, 62 tools, official), Rootly (42 stars, Python, 150+ tools, AI-powered incident analysis), Grafana OnCall (2.9K stars, Go, part of mcp-grafana), FireHydrant (4 stars, TypeScript, official), incident.io (hosted remote MCP), OpsGenie (9 stars, Go, 8 tools), ilert (14 stars, remote MCP), Better Stack (remote MCP), Squadcast (community). 10+ tools reviewed. Rating: 4.0/5.


It's 3 AM. Your phone buzzes. A P1 incident just fired. You open your laptop, fumble between PagerDuty tabs, Slack channels, and runbook wikis, trying to figure out who's on-call, what changed, and whether this happened before.

Now imagine asking your AI assistant: "What's firing right now? Who's on-call? Have we seen this before? What fixed it last time?" — and getting answers in seconds, from inside your editor, without context-switching between six different tools.

That's what SRE and incident management MCP servers enable. They connect AI agents directly to your incident management platform — PagerDuty, Rootly, FireHydrant, Grafana OnCall, incident.io, OpsGenie, ilert, Better Stack — so your AI can triage incidents, check on-call schedules, find similar past incidents, and even help coordinate response.

This review covers **MCP servers for incident management, on-call scheduling, and incident response platforms**. For monitoring and observability (Prometheus, Grafana dashboards, Datadog), see [Monitoring & Observability MCP Servers](/reviews/monitoring-observability-mcp-servers/). For uptime monitoring specifically, see [Monitoring & Uptime MCP Servers](/reviews/monitoring-uptime-mcp-servers/). For chaos engineering, see [Chaos Engineering MCP Servers](/reviews/chaos-engineering-mcp-servers/).

Part of our **[DevOps MCP category](/categories/devops/)**. The headline finding: **every major incident management platform now offers MCP support**, with PagerDuty leading in tool breadth (62 tools) and Rootly leading in AI-powered incident analysis (TF-IDF similarity matching, solution suggestion from historical data). The market is splitting between local MCP servers (PagerDuty, Rootly, OpsGenie) and hosted remote MCP (incident.io, ilert, Better Stack).

## Official Platform MCP Servers

### PagerDuty/pagerduty-mcp-server

| Server | Stars | Language | License | MCP Features |
|--------|-------|----------|---------|--------------|
| [pagerduty-mcp-server](https://github.com/PagerDuty/pagerduty-mcp-server) | 63 | Python | Apache-2.0 | 62 tools |

**The most comprehensive incident management MCP server available.** PagerDuty's official server covers the full breadth of their platform across 62 tools in 12 categories:

- **Incidents (13 tools)** — create, get, list, manage incidents; add notes and responders; retrieve alerts, notes, related incidents, past incidents, and outlier incidents
- **Event Orchestrations (6 tools)** — get orchestrations, global/router/service configs, append rules — enabling AI-assisted alert routing configuration
- **Schedules (5 tools)** — create, get, list schedules; create overrides; list schedule users
- **Services (4 tools)** — create, get, list, update services
- **Status Pages (8 tools)** — create posts and updates, manage impacts, severities, and statuses
- **Teams (6 tools)** — full team management including add/remove members
- **Incident Workflows (3 tools)** — get, list, and start workflow instances
- **Escalation Policies (2 tools)** — list and get escalation policies
- **On-Call (1 tool)** — list on-call schedules
- **Users, Log Entries, Change Events, Alert Grouping** — additional operational tools

**Safety model:** Read-only by default. Write tools (creating incidents, modifying schedules, starting workflows) require explicitly starting the server with `--enable-write-tools`. This is the right default for production incident management — you don't want an AI accidentally creating P1 incidents.

**Why it matters:** PagerDuty is the dominant incident management platform, and their MCP server covers nearly their entire API surface. The 62-tool count means an AI agent can do serious incident triage without leaving the IDE: check who's on-call, pull up related past incidents, review escalation policies, look at recent changes, and even start incident workflows — all through natural language. The outlier incident and past incident tools are especially useful for pattern recognition during active incidents.

**Limitation:** 63 stars is surprisingly low for an official server from a company this size. Docker deployment is available but adds setup friction. EU region support requires separate configuration. The one-tool on-call category feels thin compared to the 13-tool incident category.

### Rootly-AI-Labs/Rootly-MCP-server

| Server | Stars | Language | License | MCP Features |
|--------|-------|----------|---------|--------------|
| [Rootly-MCP-server](https://github.com/Rootly-AI-Labs/Rootly-MCP-server) | 42 | Python | MIT | 150+ tools |

**The most AI-native incident management MCP server.** Rootly's server goes beyond API wrapping to provide intelligent incident analysis tools that no other platform offers:

- **find_related_incidents** — uses TF-IDF similarity analysis to find historically similar incidents. Not keyword matching — actual statistical text similarity across your incident history
- **suggest_solutions** — mines past incident resolutions to recommend actionable solutions for current incidents. When a P1 fires at 3 AM, this is the tool that tells you "last time this happened, we rolled back the auth service deployment"
- **check_oncall_health_risk** — detects responder workload problems before they cause burnout. Analyzes shift patterns and incident load
- **check_responder_availability** — real-time responder status
- **get_oncall_handoff_summary** — provides context for shift transitions so the next on-call person isn't starting from scratch
- **get_oncall_shift_metrics** — shift counts, hours, and days on-call grouped by user, team, or schedule with primary/secondary role tracking

**Dynamic tool generation** from Rootly's OpenAPI spec means the server automatically exposes new API endpoints as they're added. Smart pagination defaults to 10 items per request on incident endpoints to prevent context window overflow — a thoughtful LLM-aware design choice.

**Deployment flexibility:** Hosted (HTTP Streamable, SSE), local (uv, Docker, pip), or self-hosted with configurable tool subsets. You can limit which tools are exposed for security.

**Why it matters:** Rootly's MCP server is what "AI-native incident management" actually looks like. The TF-IDF similarity matching and solution suggestion tools transform incident response from "search through Confluence for the last time this broke" to "here are the 3 most similar incidents and what fixed them." The on-call health monitoring tools address a real SRE pain point — responder fatigue. 150+ tools is the largest tool count in this review.

**Limitation:** 42 stars suggests early adoption. The sheer number of tools (150+) may overwhelm some MCP clients. License not explicitly stated in the repo (listed as MIT on PyPI). The AI analysis tools depend on having sufficient historical incident data to be useful.

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

**Limitation:** 4 stars and v0.0.4 indicate very early stage. Auto-generated code means the tool descriptions may not be optimized for LLM consumption. Specific tool enumeration isn't well-documented in the README.

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
| [mcp-grafana](https://github.com/grafana/mcp-grafana) | 2,900 | Go | Apache-2.0 | 50+ tools (7 OnCall/Incident) |

**Grafana's unified MCP server includes OnCall and Incident management alongside dashboards, Prometheus, Loki, and alerting.** The incident/on-call tools are part of a larger 50+ tool observability server:

**OnCall tools (4):**
- `list_schedules` — view and manage on-call schedules
- `get_shift_details` — detailed information about specific on-call shifts
- `get_current_oncall_users` — who's on-call right now for a given schedule
- `list_alert_groups` — view and filter alert groups by state, integration, labels, time range

**Incident tools (3):**
- `list_incidents` — search and retrieve incidents from Grafana Incident
- `create_incident` — create new incidents
- `add_activity_to_incident` — append activity items to existing incidents

**Why it matters:** The value isn't the 7 incident/on-call tools in isolation — it's having them in the same MCP server as your dashboards, Prometheus queries, Loki log searches, and alerting rules. During an incident, you can ask your AI to check who's on-call, pull up the relevant dashboard, query the metrics that are alerting, search recent logs for errors, and create an incident — all through one server connection. That's the observability-native incident response workflow. 2.9K stars reflects Grafana's massive community.

**Limitation:** Requires Grafana OnCall and Grafana Incident to be set up — these are Grafana Cloud features or self-hosted additions. The incident tools are basic (3 tools vs. PagerDuty's 13). Can disable OnCall tools with `--disable-oncall` if not needed.

## Alert Management Platforms

### giantswarm/mcp-opsgenie

| Server | Stars | Language | License | MCP Features |
|--------|-------|----------|---------|--------------|
| [mcp-opsgenie](https://github.com/giantswarm/mcp-opsgenie) | 9 | Go | Apache-2.0 | 8 tools |

**The most complete OpsGenie MCP server**, from Giant Swarm (a Kubernetes platform company):

- **Alert management (4 tools)** — list, get, acknowledge, unacknowledge alerts with search query filtering
- **Team management (2 tools)** — list and get team details
- **Heartbeat monitoring (2 tools)** — list heartbeats and check specific heartbeat status
- **Multi-transport** — stdio, SSE, HTTP streaming
- **Self-update capability** — CLI can update itself, version management built in
- **Active maintenance** — 69 commits, last updated April 2026

**The OpsGenie sunset factor:** Atlassian has announced plans to sunset OpsGenie by 2027, migrating customers to Jira Service Management. This is a significant consideration for any OpsGenie investment. The MCP server works today, but the platform it connects to has a defined end-of-life. Teams planning to migrate should consider PagerDuty, Rootly, or Grafana OnCall MCP servers instead.

**Also available:** [burakdirin/mcp-opsgenie](https://github.com/burakdirin/mcp-opsgenie) provides a more comprehensive OpsGenie MCP server with tools, resources, and prompts for incident management and post-incident analysis. [daviddykeuk/opsgenie-mcp](https://github.com/daviddykeuk/opsgenie-mcp) is a simpler alerts-focused alternative.

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

**Limitation:** Tool list not enumerated in the README — documentation at docs.ilert.com covers capabilities. 14 stars.

### Better Stack — Remote MCP

**Better Stack offers a remote MCP server at mcp.betterstack.com** with OAuth authentication (browser-based sign-in, no token management):

- Uptime monitoring — SLA summaries, availability calculations, response time analysis
- Log analysis — ClickHouse SQL queries against telemetry data (logs, spans, metrics, exceptions)
- Incident management — integrated with their uptime monitoring
- Status pages — part of their reliability platform
- Chart rendering — line charts from query results

**Why it matters:** Better Stack's MCP server covers the full reliability stack: uptime monitoring, logs, incidents, and status pages. The OAuth flow is notably frictionless compared to API key management. ClickHouse SQL queries give power users direct access to telemetry data.

**Limitation:** Fully hosted — no self-hosting option. Requires Better Stack account. Separate from their GitHub repos ([betterstack-logs-mcp](https://github.com/DrDroidLab/betterstack-logs-mcp) exists for log-focused use).

## Community and Emerging Servers

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
| PagerDuty | 63 | 62 | — | Yes | 13 tools | 8 tools |
| Rootly | 42 | 150+ | TF-IDF similarity, solution suggestion | Yes | Yes | — |
| Grafana | 2,900 | 7 (OnCall/Incident) | — | Yes | 3 tools | — |
| FireHydrant | 4 | Multiple | — | Yes | Yes | — |
| incident.io | — | Hosted | — | — | Yes | — |
| OpsGenie | 9 | 8 | — | — | Alerts | — |

### What's Missing

- **ServiceNow ITSM MCP** — no dedicated MCP server for ServiceNow's incident management (the [Atlassian MCP server](https://github.com/atlassian/atlassian-mcp-server) covers Jira but not ServiceNow)
- **Splunk On-Call (VictorOps) MCP** — no MCP server despite Splunk's observability platform
- **Postmortem/retrospective MCP** — tools for analyzing incident patterns over time, generating action items, tracking remediation
- **Runbook execution MCP** — connecting AI agents to executable runbooks (AWS DevOps Agent is the closest, but it's a full agent, not an MCP server)
- **Multi-platform aggregation** — no MCP server that unifies incidents across PagerDuty + OpsGenie + Grafana (the [MCP Proxy, Router & Aggregator Tools](/reviews/mcp-proxy-router-aggregator-servers/) could fill this gap)

## Rating: 4.0 / 5

**Every major incident management platform now has MCP support** — PagerDuty (official, 62 tools), Rootly (AI-powered analysis, 150+ tools), FireHydrant (official), incident.io (hosted remote), Grafana OnCall (part of 50+ tool observability server), OpsGenie (community), ilert (official remote), Better Stack (remote). The breadth is impressive.

**PagerDuty's 62-tool server is the most complete** for traditional incident management. **Rootly's AI-powered analysis tools are the most innovative** — TF-IDF similarity matching and solution suggestion from historical data represent what AI-native incident management should look like. **Grafana's unified observability approach** is the most architecturally elegant — having on-call, incidents, dashboards, metrics, and logs in one MCP server eliminates the multi-tool context-switching that makes incidents painful.

**Deducted 1.0 for:**
- **Low adoption** — PagerDuty's official server has just 63 stars, FireHydrant has 4. These are established companies with thousands of customers, yet MCP adoption is minimal
- **OpsGenie's uncertain future** — Atlassian's 2027 sunset means the OpsGenie MCP ecosystem is building on a disappearing platform
- **Limited write capabilities** — several servers default to read-only (which is safe but limits incident response automation)
- **No cross-platform aggregation** — teams using multiple incident tools can't get a unified view through MCP yet
- **AI analysis gap** — only Rootly offers intelligent incident analysis; PagerDuty and others are pure API wrappers with no ML/AI layer

The SRE MCP space is functionally complete but commercially immature. The tools work — they just haven't been widely adopted yet. As AI coding assistants become the default developer interface, these MCP servers will shift from "nice to have" to "essential infrastructure."

