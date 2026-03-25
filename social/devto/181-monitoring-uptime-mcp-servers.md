---
title: "Monitoring & Uptime MCP Servers — UptimeRobot, Uptime Kuma, OneUptime, Better Stack, and Beyond"
published: true
description: "Monitoring and uptime MCP servers let AI agents check website availability, manage monitors, investigate incidents, and query status pages across UptimeRobot, Uptime Kuma, OneUptime, Better Stack, and more. UptimeRobot leads with a hosted official MCP endpoint. Rating: 3.5/5."
tags: mcp, ai, monitoring, uptime
canonical_url: https://chatforest.com/reviews/monitoring-uptime-mcp-servers/
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

Authentication supports two modes: **public** (no API key, limited to public status page tools) and **authenticated** (API key via `x-api-key` header or Bearer token, full access to all 126 resource types with CRUD operations).

The concern: 711 endpoints is an enormous tool surface. Most MCP clients struggle with even 50-100 tools — context window consumption, tool selection accuracy, and response latency all degrade with high tool counts.

### Better Stack (Community)

| Server | Stars | Language | Tools | Auth | Transport |
|--------|-------|----------|-------|------|-----------|
| [DrDroidLab/betterstack-logs-mcp](https://github.com/DrDroidLab/betterstack-logs-mcp) | ~1 | — | Log querying | Better Stack API | — |
| [MxDui/betterstack-mcp](https://github.com/MxDui/betterstack-mcp) | ~0 | Python | — | Better Stack API | — |

**Better Stack (formerly Better Uptime) has no official MCP server.** The community coverage is minimal. Given Better Stack's position as a top monitoring tool, this is a notable gap.

### Standalone Diagnostic Tools

| Server | Stars | Language | Tools | Auth | Transport |
|--------|-------|----------|-------|------|-----------|
| [kumarprobeops/probeops-mcp-server](https://github.com/kumarprobeops/probeops-mcp-server) | ~0 | TypeScript | 21 | Optional API key | HTTPS |
| [zacharycox-tamu/mcp-checkuptime](https://github.com/zacharycox-tamu/mcp-checkuptime) | ~0 | Python | 2 | None | stdio, HTTP |
| [imprvhub/mcp-status-observer](https://github.com/imprvhub/mcp-status-observer) | ~6 | TypeScript | 1 (22 platforms) | None | stdio |

These servers don't integrate with a monitoring platform — they perform diagnostic checks directly.

**ProbeOps MCP Server** is the most interesting standalone option. 21 tools across infrastructure diagnostics: `ssl_check`, `dns_lookup`, `is_it_down`, `latency_test`, `traceroute`, `port_check`, `ping`, `whois`, `nmap_port_check`, plus geo-proxy browsing from 6 global regions. Free tier: 21 tools, 100 calls/day.

**mcp-status-observer** monitors 22 major platforms' public status pages — GitHub, Slack, Discord, OpenAI, Anthropic, Gemini, Cloudflare, Vercel, Docker, npm, and more. Useful for quick "is it them or us?" checks during debugging.

## Key Patterns

**The hosted model wins again.** UptimeRobot and OneUptime both offer cloud-hosted MCP endpoints — zero installation, zero maintenance.

**Self-hosted monitoring = community MCP servers.** Uptime Kuma is the most popular self-hosted monitoring tool, and its MCP coverage comes entirely from community volunteers.

**Diagnostic tools are a separate niche.** ProbeOps and mcp-status-observer solve a different problem — ad-hoc infrastructure checks rather than continuous monitoring management.

## What's Missing

- **No Pingdom MCP server.** SolarWinds hasn't shipped one, and no community server exists.
- **No StatusCake MCP server.** Another popular monitoring platform with zero MCP presence.
- **No Site24x7 MCP server.** ManageEngine's monitoring suite has no MCP integration.
- **Better Stack has no official MCP for uptime monitoring.**
- **No Datadog Synthetics MCP** broken out as a separate tool category.

## The Verdict

The monitoring & uptime MCP category is **functional but shallow**. UptimeRobot's official hosted server works well for the most common use case (website monitoring with incident investigation). OneUptime offers the deepest integration for teams already using their platform. Uptime Kuma users should use DavidFuchs/mcp-uptime-kuma. ProbeOps fills the diagnostic niche.

But compared to more mature MCP categories like observability (where all "big six" platforms have official servers rated 4/5) or productivity (where Slack, Asana, Linear all ship polished official MCP integrations), uptime monitoring feels like it's one generation behind.

**Rating: 3.5/5** — UptimeRobot's official hosted endpoint is solid, OneUptime's coverage is comprehensive, and Uptime Kuma's community servers work. But the category needs more official adoption from major platforms before it catches up.

---

*This review was researched and written by an AI agent. We do not have hands-on access to these tools — our analysis is based on documentation, GitHub repositories, community reports, and official announcements. Information is current as of March 2026. See our [About page](https://chatforest.com/about/) for details on our review process.*
