# Cisco ThousandEyes MCP Server — Network Intelligence for AI Agents (28 Tools, Remote Hosted)

> Cisco ThousandEyes MCP server gives AI agents access to 28 network monitoring tools — synthetic tests, path visualization, BGP routing, endpoint monitoring, anomaly detection, and on-demand test execution. Remote hosted, no install required.


Part of our **[Network Automation & Infrastructure MCP Servers roundup](/reviews/network-automation-infrastructure-mcp-servers/)**.

**At a glance:** Remote hosted at `https://api.thousandeyes.com/mcp`. 28 tools. Launched February 4, 2026. OAuth 2.0 or Bearer token auth. Claude Desktop, Cursor, VS Code, AWS Kiro. ThousandEyes subscription required.

Cisco ThousandEyes is a network intelligence platform that monitors what's between your users and your services — the internet paths, ISPs, CDNs, DNS providers, and cloud infrastructure you don't own and can't instrument directly. Traditional observability tools (Datadog, Grafana, New Relic) show you what's happening *inside* your infrastructure. ThousandEyes shows you what's happening *outside* it: where packets are being dropped in an ISP backbone, which CDN POP is degraded, whether a BGP route change is causing reachability problems, and whether a SaaS outage is affecting just your organization or everyone on that provider.

The ThousandEyes MCP server brings this network intelligence directly into AI assistants. Instead of clicking through dashboards during an incident, NOC engineers and MSPs can query synthetic test results, trace network paths, correlate outage data, and run on-demand tests through natural language. The server launched in February 2026 as a **fully hosted remote MCP** — no software to deploy, no Docker containers to run. Cisco hosts it.

## What ThousandEyes Does

ThousandEyes runs scheduled synthetic tests from three vantage point types:

- **Cloud Agents** — Cisco-managed agents in 300+ locations across ISPs, cloud regions, and data centers worldwide
- **Enterprise Agents** — Self-hosted agents in customer data centers and offices
- **Endpoint Agents** — Software installed on employee laptops and devices

Tests cover HTTP page loads, DNS resolution, BGP reachability, browser transactions, VoIP quality, and ICMP/ping. The platform also offers **Internet Insights** — collective intelligence aggregated across all ThousandEyes customers, surfacing macro-level outages at ISPs and SaaS providers before any single customer would detect them independently.

ThousandEyes targets enterprises, telcos, and MSPs — teams with complex hybrid environments where the internet itself is a dependency, not just a commodity.

## The 28 Tools

The MCP server exposes tools across 9 categories with an explicit two-group permission model: **read-only** (safe to enable broadly) and **write/delete** (for test management workflows). Cisco recommends enabling only what you need — enabling too many tools simultaneously causes latency and timeouts.

### Synthetic Test Management (3 read + 3 write)

| Tool | Group | What it does |
|------|-------|-------------|
| `List Tests` | Read | View all configured synthetic tests |
| `Get Test Details` | Read | Retrieve configuration and status for a specific test |
| `Instant Tests` | Read | Run on-demand tests against a target *(consumes billing units)* |
| `Create Synthetic Test` | Write | Create a new scheduled synthetic test |
| `Update Synthetic Test` | Write | Modify test configuration |
| `Delete Synthetic Test` | Write | Remove a test |

### Events and Alerts (4 read)

| Tool | Group | What it does |
|------|-------|-------------|
| `List Events` | Read | Find network/application problems within a time range |
| `Get Event Details` | Read | Deep-dive into a specific event |
| `List Alerts` | Read | View active or cleared alerts |
| `Get Alert Details` | Read | Comprehensive alert information |

### Outage and Anomaly Analysis (3 read)

| Tool | Group | What it does |
|------|-------|-------------|
| `Search Outages` | Read | Correlate network and application outage data |
| `Get Anomalies` | Read | Detect metric anomalies over a time period |
| `Get Metrics` | Read | Retrieve aggregated metrics for dashboards and reports |

### Network Path Analysis (4 read)

| Tool | Group | What it does |
|------|-------|-------------|
| `Get Path Visualization` | Read | Hop-by-hop path data from test agents to target |
| `Get Full Path Visualization` | Read | Extended path data with additional detail |
| `Get BGP Test Results` | Read | BGP reachability and routing data |
| `Get BGP Route Details` | Read | Detailed BGP route information |

### Endpoint Monitoring (3 read)

| Tool | Group | What it does |
|------|-------|-------------|
| `List Endpoint Agents and Tests` | Read | List endpoint agents with filtering |
| `Get Endpoint Agent Metrics` | Read | Performance metrics from endpoint agents |
| `Get Connected Device` | Read | Device and connection details for endpoint agents |

### AI-Assisted Analysis (1 read)

| Tool | Group | What it does |
|------|-------|-------------|
| `Views Explanations` | Read | AI-generated natural language analysis of test result views |

### Agent and Account Management (2 read)

| Tool | Group | What it does |
|------|-------|-------------|
| `Get Cloud and Enterprise Agents` | Read | List all cloud and enterprise agent locations |
| `Get Account Groups` | Read | List accessible account groups |

### Service Map (1 read)

| Tool | Group | What it does |
|------|-------|-------------|
| `Get Service Map` | Read | Distributed tracing service map for HTTP tests with tracing enabled |

### Template Management (2 write)

| Tool | Group | What it does |
|------|-------|-------------|
| `Search Templates` | Write | List available test and dashboard templates |
| `Deploy Template` | Write | Create tests, dashboards, and alert rules from a template bundle |

## Example Prompts

The docs suggest prompts like:

- *"Do I have any active events?"* — surfaces in-progress network problems
- *"What outages have occurred in the last 24 hours?"* — correlates Internet Insights with local events
- *"What is the hop-by-hop network path for my HTTP test from Seattle?"* — brings path visualization into chat
- *"Can you find anomalies during the last 6 hours for test [name]?"* — triggers AI-assisted anomaly analysis
- *"Run an HTTP test to example.com from our San Francisco agents."* — instant on-demand test
- *"Deploy the template [name] for domain example.com using my Seattle agents."* — stands up a complete monitoring configuration

## Installation and Configuration

**No local software to install.** The MCP server is hosted at `https://api.thousandeyes.com/mcp`. Connecting takes two things: a ThousandEyes account with API Access permissions, and an organization that has not opted out of ThousandEyes AI features.

**Claude Desktop** — Settings → Connectors → Add custom connector → URL `https://api.thousandeyes.com/mcp` → sign in via browser. The connector UI lets you enable or disable the read-only and write/delete permission groups separately.

**Cursor** — Install via Marketplace (`/add-plugin thousandeyes`) or configure manually:

```json
{
  "mcpServers": {
    "ThousandEyes": {
      "url": "https://api.thousandeyes.com/mcp",
      "headers": {
        "Authorization": "Bearer <YOUR_API_TOKEN>"
      }
    }
  }
}
```

**VS Code / AWS Kiro** — Use `npx mcp-remote@latest` as a local proxy (requires Node.js).

**Authentication choices:**
- **Bearer token** — shares the organization-wide rate limit (240 req/min)
- **OAuth2 Dynamic Client Registration** — browser-based flow, grants a separate per-client rate limit (240 req/min independent of the org). Better for teams or heavy usage.

**ThousandEyes for Government** does not include GenAI features — the MCP server is unavailable in Government deployments.

## What's Not Exposed

The tool surface covers the core operational workflows well, but leaves some gaps:

- **Internet Insights** is not accessible through any MCP tool. The collective outage intelligence data — one of ThousandEyes' most unique capabilities — isn't exposed. Teams can't ask "are other companies seeing this Comcast degradation?" through MCP.
- **Alert rule management** is absent. You can read alerts but cannot create or modify alert rules directly (though templates can bundle alert rules on deployment).
- **Dashboard CRUD** is not present. Templates can deploy dashboards but you can't query or modify existing dashboard configurations.

## GitHub Footprint

The official repo `CiscoDevNet/ThousandEyes-MCP-Server-official` is effectively a configuration guide — 1 star, 3 commits, no production code. The actual server runs on Cisco's infrastructure. This isn't a criticism of the server's quality, but it does mean there's no community contribution path and no way to inspect the implementation.

The community predecessor (`CiscoDevNet/thousandeyes-mcp-community`) was archived in March 2026 when the official server launched. The most useful adjacent project is `pamosima/network-mcp-docker-suite` (35 stars) — a Docker-based suite that runs ThousandEyes alongside Cisco Meraki, Catalyst Center, IOS XE, ISE, Splunk, and NetBox as a unified AIOps toolkit.

## Who It's For

ThousandEyes MCP is purpose-built for **network operations teams** — NOC engineers, MSPs, and SREs at organizations where internet path quality is operationally significant. That's a narrower audience than most MCP servers on this site.

If your team already uses ThousandEyes dashboards for incident response, the MCP server gives you natural language queries during war-room calls without screen sharing dashboards. If you're an MSP managing ThousandEyes across multiple customer accounts, the `Get Account Groups` tool and template deployment let you orchestrate monitoring setup conversationally.

If you don't use ThousandEyes — or your monitoring needs are fully covered by Datadog, Grafana, or New Relic — there's no reason to consider this server. The platform and its MCP server are tightly coupled.

## The Verdict

**3.5/5.** Cisco ThousandEyes MCP delivers genuine operational value for its target audience. The 28-tool surface covers the core monitoring and diagnostic workflows. The remote-hosted model eliminates all deployment friction — connecting takes minutes. The two-group permission model (read-only vs. write/delete) reflects mature security thinking. OAuth2 Dynamic Client Registration separating per-client rate limits is the right design for multi-user teams.

The gaps are real: no Internet Insights exposure (the platform's most unique capability), no alert rule management, performance concerns when enabling too many tools simultaneously, and no community development path. The GitHub repo's 1-star footprint reflects that this is a proprietary hosted service, not an open ecosystem project.

For ThousandEyes shops: **install it.** For everyone else: this is a specialized tool for a specialized platform — evaluate ThousandEyes the product first.

---

**Quick reference**

| | |
|---|---|
| Vendor | Cisco (official) |
| Server URL | `https://api.thousandeyes.com/mcp` |
| Deployment | Remote hosted (no local install) |
| Transport | Streamable HTTP |
| Auth | Bearer token or OAuth2 DCR |
| Tool count | 28 (~22 read-only, ~4 write/delete) |
| Supported clients | Claude Desktop, Cursor, VS Code, AWS Kiro |
| Launched | February 4, 2026 |
| Prerequisite | ThousandEyes subscription + API Access role |
| GitHub | [CiscoDevNet/ThousandEyes-MCP-Server-official](https://github.com/CiscoDevNet/ThousandEyes-MCP-Server-official) (1 star) |
| Rating | 3.5/5 |

