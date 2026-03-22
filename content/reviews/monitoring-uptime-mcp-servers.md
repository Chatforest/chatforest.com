---
title: "Monitoring & Uptime MCP Servers — UptimeRobot, Uptime Kuma, OneUptime, Better Stack, and Beyond"
date: 2026-03-15T03:20:00+09:00
description: "Monitoring and uptime MCP servers let AI agents check website availability, manage monitors, investigate incidents, and query status pages across UptimeRobot, Uptime Kuma, OneUptime, Better Stack, and more. We reviewed 10+ servers across 5 platforms. UptimeRobot leads with a hosted official MCP endpoint and full monitor management. OneUptime offers the most comprehensive coverage with 711 API endpoints across 126 resource types."
og_description: "Monitoring & uptime MCP servers: UptimeRobot (official hosted, full CRUD), Uptime Kuma (4+ community servers, open-source), OneUptime (711 endpoints, 126 resources), Better Stack (logs-focused). 10+ servers across 5 platforms. Rating: 3.5/5."
content_type: "Review"
card_description: "Monitoring and uptime MCP servers across UptimeRobot, Uptime Kuma, OneUptime, Better Stack, and infrastructure diagnostics. UptimeRobot has the strongest official MCP integration with a hosted endpoint. Uptime Kuma has the most community servers."
last_refreshed: 2026-03-15
---

Uptime monitoring is table stakes for any production system — and now AI agents can interact with monitoring platforms directly. The MCP ecosystem here splits cleanly between **commercial platforms with official hosted servers** (UptimeRobot, OneUptime) and **open-source platforms with community-built integrations** (Uptime Kuma). There's also a small but interesting niche of **standalone diagnostic tools** that don't require a monitoring platform at all.

The headline finding: **UptimeRobot ships the most polished official MCP integration** — a hosted endpoint at `mcp.uptimerobot.com/mcp` with full monitor CRUD, incident investigation, and response-time analytics. Meanwhile, **Uptime Kuma** has the most fragmented community ecosystem with 4+ independent MCP servers of varying quality. And **OneUptime** takes the maximalist approach, exposing its entire 711-endpoint API surface through MCP.

## The Landscape

### UptimeRobot (Official)

| Server | Stars | Language | Tools | Auth | Transport |
|--------|-------|----------|-------|------|-----------|
| [UptimeRobot MCP](https://uptimerobot.com/mcp/) | — | Hosted | Full CRUD | API key (Bearer) | HTTPS |

**UptimeRobot provides the best-designed monitoring MCP integration.** The official hosted endpoint at `mcp.uptimerobot.com/mcp` requires zero local setup — add the endpoint URL and your API token to your MCP client config, restart, and tools auto-discover.

The tool set covers the full monitoring lifecycle: **list and manage monitors** (HTTP, Keyword, Ping, Port, Heartbeat, DNS types), **create new monitors** with contact and tag assignment, **pause and resume** monitors, **investigate incidents** with timelines, error codes, request logs, and traceroutes, and **pull response-time analytics** with 1h–90d windows including min, max, average, and p95 stats.

Security is handled sensibly. You can use a **read-only API key** for pure monitoring visibility, or the main API key for full read/write access. The token goes in a Bearer authorization header, keeping it out of URL parameters.

UptimeRobot's free tier (50 monitors, 5-minute intervals) works with MCP. Paid plans ($7/month Pro, 50 monitors at 30-second intervals) add more capacity. The MCP integration itself doesn't appear to add extra cost.

The gap: UptimeRobot's MCP documentation is sparse. Tool names and capabilities auto-discover, but there's no public reference listing every available tool with parameter schemas. You're trusting the MCP client's tool discovery to surface everything.

### Uptime Kuma (Community)

| Server | Stars | Language | Tools | Auth | Transport |
|--------|-------|----------|-------|------|-----------|
| [DavidFuchs/mcp-uptime-kuma](https://github.com/DavidFuchs/mcp-uptime-kuma) | ~16 | TypeScript | 9 | Username/password, JWT, 2FA | stdio, Streamable HTTP |
| [Camusama/uptime-kuma-mcp-server](https://github.com/Camusama/uptime-kuma-mcp-server) | ~3 | Python | 3 | Username/password | SSE |
| [phukit29182/uptime-kuma-mcp-server](https://github.com/phukit29182/uptime-kuma-mcp-server) | ~1 | Python | 13 | Username/password | stdio, SSE |
| [gryfai/mcp-uptime-kuma-open](https://github.com/gryfai/mcp-uptime-kuma-open) | ~0 | Python | 8 (read-only) | Username/password | stdio |

**Uptime Kuma is the most popular self-hosted monitoring tool** ([louislam/uptime-kuma](https://github.com/louislam/uptime-kuma), 66K+ stars), and it has the most MCP servers in this category — though none are official.

**DavidFuchs/mcp-uptime-kuma** is the clear community leader. 9 tools: `getMonitorSummary`, `listMonitors`, `listMonitorTypes`, `getMonitor`, `pauseMonitor`, `resumeMonitor`, `listHeartbeats`, `getHeartbeats`, `getSettings`. It's context-efficient by design — returns only essential data by default to avoid overwhelming LLM context windows. Supports both stdio (local via npx) and Streamable HTTP (remote via Docker). Authentication includes username/password with optional 2FA, plus JWT tokens for headless use. TypeScript, MIT, v0.6.4, 0 open issues. The only Uptime Kuma server with Docker support and dual transport.

**phukit29182/uptime-kuma-mcp-server** has the most tools (13) including `edit_monitor`, `add_monitor_tag`, `delete_monitor_tag`, `get_status_page`, and `get_tags` — features missing from DavidFuchs. It uses FastMCP (Python), supports stdio and SSE, but has only 6 commits and 1 star. No license specified.

**Camusama/uptime-kuma-mcp-server** is the most minimal — just 3 tools (`add_monitors`, `get_monitors`, `delete_monitors`) for batch monitor management. Available on PyPI (`uvx uptime-kuma-mcp-server`), SSE transport, 33 commits, v0.1.15. Useful if you only need bulk operations.

**gryfai/mcp-uptime-kuma-open** takes a commercial approach — the open version is read-only (monitor status, beats, notifications, status pages, heartbeats, tags, database size). Write operations (create/edit monitors, manage notifications, Docker functions) require the commercial closed-source version. BSL license (converts to Apache 2.0 eventually). 29 commits.

The fragmentation is disappointing but typical of the Uptime Kuma ecosystem. DavidFuchs is the safe choice for most users — it has the best transport support, the cleanest auth model, and zero open issues.

### OneUptime (Official)

| Server | Stars | Language | Tools | Auth | Transport |
|--------|-------|----------|-------|------|-----------|
| [OneUptime MCP](https://oneuptime.com/docs/ai/mcp-server) | — | Hosted + self-hosted | 711 endpoints, 126 resources | API key, Bearer token | Streamable HTTP |

**OneUptime is the most comprehensive monitoring MCP server by raw coverage.** The MCP server exposes the entire OneUptime API — 711 endpoints across 126 resource types — through Streamable HTTP transport.

The tool categories span the full observability stack: **monitors** (health status, uptime, response times, alert configs), **incidents** (creation, management, timelines, severity), **logs** (full-text search, correlation with incidents and traces), **metrics** (time series, trend analysis, anomaly detection), **traces** (distributed tracing across services), **status pages** (public-facing status with incidents, maintenance, announcements), **teams** (access control, notifications), and **workflows** (automated response).

Two deployment options: **cloud-hosted** at `oneuptime.com/mcp` and **self-hosted** at `your-domain.com/mcp`. Both use the same MCP interface. OneUptime is 100% open source ([OneUptime/oneuptime](https://github.com/OneUptime/oneuptime) on GitHub).

Authentication supports two modes: **public** (no API key, limited to public status page tools like `get_public_status_page_overview`, `get_public_status_page_incidents`, `get_public_status_page_scheduled_maintenance`, `get_public_status_page_announcements`) and **authenticated** (API key via `x-api-key` header or Bearer token, full access to all 126 resource types with CRUD operations).

The concern: 711 endpoints is an enormous tool surface. Most MCP clients struggle with even 50-100 tools — context window consumption, tool selection accuracy, and response latency all degrade with high tool counts. OneUptime's `oneuptime_list_resources` tool helps agents discover what's available, but this is still a firehose approach. The `oneuptime_help` tool provides guidance, but the raw API surface may overwhelm smaller models.

OneUptime offers both free and paid tiers, with the self-hosted option being completely free.

### Better Stack (Community)

| Server | Stars | Language | Tools | Auth | Transport |
|--------|-------|----------|-------|------|-----------|
| [DrDroidLab/betterstack-logs-mcp](https://github.com/DrDroidLab/betterstack-logs-mcp) | ~1 | — | Log querying | Better Stack API | — |
| [MxDui/betterstack-mcp](https://github.com/MxDui/betterstack-mcp) | ~0 | Python | — | Better Stack API | — |

**Better Stack (formerly Better Uptime) has no official MCP server.** The community coverage is minimal.

**DrDroidLab/betterstack-logs-mcp** focuses exclusively on log querying — multi-source querying, source management, ClickHouse SQL queries, and historical data access. It's built by Doctor Droid (an observability startup) and works with the Better Stack Logs product specifically, not the uptime monitoring side.

**MxDui/betterstack-mcp** has 1 commit and no documentation. Not usable in its current state.

Better Stack publishes an MCP server template ([betterstack-community/mcp-template-ts](https://github.com/betterstack-community/mcp-template-ts)) suggesting awareness of the protocol, but no official monitoring MCP server exists. Given Better Stack's position as a top monitoring tool, this is a notable gap.

### Standalone Diagnostic Tools

| Server | Stars | Language | Tools | Auth | Transport |
|--------|-------|----------|-------|------|-----------|
| [kumarprobeops/probeops-mcp-server](https://github.com/kumarprobeops/probeops-mcp-server) | ~0 | TypeScript | 21 | Optional API key | HTTPS |
| [zacharycox-tamu/mcp-checkuptime](https://github.com/zacharycox-tamu/mcp-checkuptime) | ~0 | Python | 2 | None | stdio, HTTP |
| [imprvhub/mcp-status-observer](https://github.com/imprvhub/mcp-status-observer) | ~6 | TypeScript | 1 (22 platforms) | None | stdio |

These servers don't integrate with a monitoring platform — they perform diagnostic checks directly.

**ProbeOps MCP Server** is the most interesting standalone option. 21 tools across infrastructure diagnostics: `ssl_check`, `dns_lookup`, `is_it_down`, `latency_test`, `traceroute`, `port_check`, `ping`, `whois`, `nmap_port_check`, `tcp_ping`, `keyword_check`, `websocket_check`, `banner_grab`, `api_health`, plus 6 DNS shortcuts and geo-proxy browsing from 6 global regions (US East, US West, EU Central, Canada, India, Australia). It works instantly with no API key required (demo mode: 11 tools, 10 calls/day). Free tier: 21 tools, 100 calls/day. Professional tier: 5,000 calls/day. Multi-region execution is genuinely useful — you can test if a site is down globally or just from your location.

**mcp-checkuptime** provides just 2 tools (`ping_host`, `check_website`) for basic connectivity checking. MIT, runs as both MCP server and standalone web API on port 9000. Useful for Open WebUI integration.

**mcp-status-observer** monitors 22 major platforms' public status pages — GitHub, Slack, Discord, OpenAI, Anthropic, Gemini, Cloudflare, Vercel, Docker, npm, and more. One `status` tool with subcommands (`list`, `--all`, `--[platform]`). MPL-2.0, TypeScript, 55 commits. Useful for quick "is it them or us?" checks during debugging.

### Community UptimeRobot

| Server | Stars | Language | Tools | Auth | Transport |
|--------|-------|----------|-------|------|-----------|
| [thichcode/uptimerobot_mcp](https://github.com/thichcode/uptimerobot_mcp) | ~0 | Python | CRUD + reports | API key | REST |

A community alternative to UptimeRobot's official MCP. Python/FastAPI, 2 commits, includes monitor CRUD, maintenance windows, and report generation. Also integrates with n8n for workflow automation. Role-based access (admin, manager, viewer). Given that UptimeRobot now has an official hosted MCP endpoint, this community server is largely superseded — use the official one.

## Key Patterns

**The hosted model wins again.** UptimeRobot and OneUptime both offer cloud-hosted MCP endpoints — zero installation, zero maintenance. This is becoming the standard for commercial monitoring tools, following the pattern set by Slack, Asana, and PagerDuty.

**Self-hosted monitoring = community MCP servers.** Uptime Kuma is the most popular self-hosted monitoring tool, and its MCP coverage comes entirely from community volunteers. This means fragmentation (4+ servers), inconsistent quality, and no guaranteed maintenance.

**Diagnostic tools are a separate niche.** ProbeOps and mcp-status-observer solve a different problem — ad-hoc infrastructure checks rather than continuous monitoring management. They're complementary to platform-specific servers, not replacements.

**The monitoring MCP gap: alerting.** Most of these servers let you query status and manage monitors, but few handle the alert side well. For alert-focused MCP, see [PagerDuty MCP](/reviews/pagerduty-mcp-server/) (67 tools, read-only defaults) or [Grafana MCP](/reviews/grafana-mcp-server/) (alerting + OnCall toolsets).

## What's Missing

- **No Pingdom MCP server.** SolarWinds hasn't shipped one, and no community server exists.
- **No StatusCake MCP server.** Another popular monitoring platform with zero MCP presence.
- **No Site24x7 MCP server.** ManageEngine's monitoring suite has no MCP integration.
- **Better Stack has no official MCP for uptime monitoring** — only community log querying.
- **No Datadog Synthetics MCP.** Datadog's MCP server covers logs, metrics, traces, and monitors, but synthetic monitoring is not broken out as a separate tool category (see [Datadog MCP review](/reviews/datadog-mcp-server/)).

## The Verdict

The monitoring & uptime MCP category is **functional but shallow**. UptimeRobot's official hosted server works well for the most common use case (website monitoring with incident investigation). OneUptime offers the deepest integration for teams already using their platform. Uptime Kuma users should use DavidFuchs/mcp-uptime-kuma. ProbeOps fills the diagnostic niche.

But compared to more mature MCP categories like observability (where all "big six" platforms have official servers rated 4/5) or productivity (where Slack, Asana, Linear all ship polished official MCP integrations), uptime monitoring feels like it's one generation behind. Most major monitoring platforms either have no MCP server or rely entirely on community implementations.

**Rating: 3.5/5** — UptimeRobot's official hosted endpoint is solid, OneUptime's coverage is comprehensive, and Uptime Kuma's community servers work. But the category needs more official adoption from major platforms (Pingdom, StatusCake, Better Stack, Site24x7) before it catches up to the observability MCP ecosystem.

---

*Last updated: March 15, 2026. Have we missed a monitoring MCP server? Let us know — we research new servers regularly.*

*This review was last edited on 2026-03-16 using Claude Opus 4.6 (Anthropic).*
