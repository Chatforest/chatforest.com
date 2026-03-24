---
title: "Observability & Monitoring MCP Servers — 10 Reviews Covering Grafana, Datadog, Sentry, PagerDuty, New Relic, Honeycomb, Log Management, Uptime Monitoring, and LLM Observability"
date: 2026-03-24T15:30:00+09:00
description: "Comprehensive reviews of 10 Observability & Monitoring MCP server categories — from full-stack platforms like Grafana, Datadog, and New Relic to error tracking, incident management, log aggregation, uptime monitoring, and LLM observability. 75+ servers evaluated across the entire observability stack."
og_description: "10 Observability & Monitoring MCP server reviews covering Grafana (2,600+ stars), Datadog (50+ tools), Sentry (603 stars), PagerDuty (60+ tools), New Relic, Honeycomb, log management, uptime monitoring, and LLM observability. 75+ servers evaluated."
content_type: "Category"
---

We've reviewed **10 categories** of Observability & Monitoring MCP servers, evaluating over **75 individual servers** across application performance monitoring, error tracking, incident management, log aggregation, uptime monitoring, and LLM observability. Each review covers architecture patterns, star counts, tool inventories, known issues, and honest ratings.

Observability is where MCP is seeing the strongest vendor adoption outside of cloud platforms. Grafana (2,600+ stars, 252K+ Docker Hub pulls) leads the ecosystem by a wide margin, while Datadog, Sentry, PagerDuty, Honeycomb, and New Relic have all shipped official first-party servers. The pattern is clear — observability vendors understand that AI agents need production context, and MCP is the interface they're betting on.

---

## Full-Stack Observability Platforms

The major observability platforms that provide unified dashboards, metrics, traces, and alerting. All five vendors in this group ship official first-party MCP servers — the highest vendor adoption rate of any subcategory.

| Review | Rating | Key Servers |
|--------|--------|-------------|
| [Grafana](/reviews/grafana-mcp-server/) | 4/5 | mcp-grafana (2,600+ stars, 303 forks, v0.11.3), 252K+ Docker Hub pulls, 40+ tools across 15 categories, ~595K all-time PulseMCP visitors (#66 globally) |
| [Datadog](/reviews/datadog-mcp-server/) | 4/5 | Official Datadog MCP (22 stars, GA since March 9 2026), 50+ tools across 14 modular toolsets, ~10.8K weekly PulseMCP visitors |
| [New Relic](/reviews/newrelic-mcp-server/) | 4/5 | Remote-hosted at mcp.newrelic.com (Streamable HTTP), 35+ tools across 6 categories, Public Preview, 20.2K all-time PulseMCP visitors |
| [New Relic NRQL & Alerts](/reviews/new-relic-mcp-server/) | 3.5/5 | Official first-party (4 stars, Public Preview), 15+ observability tools across 6 categories — NRQL queries, alerts, entity discovery, log analysis |
| [Honeycomb](/reviews/honeycomb-mcp-server/) | 4/5 | Official hosted MCP (replaced deprecated self-hosted, 41 stars, 12 forks), 14 tools, GA since Sep 2025, Agent Skills + Automated Investigations launched Mar 2026 |

## Error Tracking & Incident Management

The tools teams reach for when things break — from error monitoring to on-call coordination. Both Sentry and PagerDuty ship official servers with deep write capabilities.

| Review | Rating | Key Servers |
|--------|--------|-------------|
| [Sentry](/reviews/sentry-mcp-server/) | 4/5 | sentry-mcp (603 stars, 93 forks, v0.30.0), ~19.4K weekly npm downloads, ~302K all-time PulseMCP visitors (#113 globally), ~20 tools |
| [PagerDuty](/reviews/pagerduty-mcp-server/) | 4/5 | pagerduty-mcp (57 stars, 30 forks, v0.15.1, 270 commits), 60+ tools, ~809 PyPI downloads/month, 126K all-time PulseMCP visitors |

## Log Management & Uptime Monitoring

Log aggregation across Splunk, Elasticsearch, Loki, and CloudWatch, plus uptime and status monitoring with UptimeRobot, Uptime Kuma, and Better Stack.

| Review | Rating | Key Servers |
|--------|--------|-------------|
| [Log Management](/reviews/log-management-mcp-servers/) | 4/5 | 25+ servers across 12 platforms — Grafana mcp-grafana leads (2,500 stars, 6 Loki tools), Elasticsearch official (626 stars, deprecated), Splunk official + community (94 stars, 13 tools), CloudWatch, Graylog |
| [Monitoring & Uptime](/reviews/monitoring-uptime-mcp-servers/) | 3.5/5 | 10+ servers across 5 platforms — UptimeRobot (official hosted), Uptime Kuma (4+ community servers), OneUptime (711 endpoints across 126 resource types), Better Stack, Checkly |

## LLM Observability & MLOps

The emerging subcategory where observability meets AI — tracking LLM traces, prompt performance, model evaluation, and ML pipeline orchestration.

| Review | Rating | Key Servers |
|--------|--------|-------------|
| [LLM Observability & MLOps Pipeline](/reviews/llm-observability-mlops-pipeline-mcp-servers/) | 3.5/5 | 10+ servers across 5 subcategories — Opik (200 stars, LLM traces/evals), OpenTelemetry MCP (175 stars, Jaeger/Tempo/Traceloop), Langfuse (158 stars, prompt management), LangSmith (89 stars), ZenML (43 stars, pipeline orchestration) |

---

## Category Overview

**10 reviews. 75+ servers. Average rating: 3.9/5.**

### What stands out

**Vendor adoption is extraordinary.** Grafana, Datadog, Sentry, PagerDuty, Honeycomb, and New Relic all ship official first-party MCP servers. That's six major observability vendors — a higher official adoption rate than almost any other MCP category. The message is clear: observability companies see AI agents as first-class consumers of production telemetry.

**Grafana is the runaway star count leader.** At 2,600+ stars and 252K+ Docker Hub pulls, mcp-grafana dwarfs every other observability MCP server. Its 40+ tools across 15 categories cover dashboards, alerting, Loki logs, Prometheus queries, and more. It's also the backbone of the log management ecosystem, providing the most mature Loki integration.

**Sentry and PagerDuty prove write-capable MCP is production-ready.** Sentry's 603-star server lets agents debug production errors without leaving the editor. PagerDuty's 60+ tools make it the most comprehensive write API in the incident management space — agents can create, acknowledge, and resolve incidents, manage on-call schedules, and coordinate response teams.

**Honeycomb pioneered the hosted-MCP model.** When Honeycomb deprecated its self-hosted server in favor of a hosted MCP endpoint, it became one of the first observability vendors to treat MCP as a managed service. The March 2026 launch of Agent Skills and Automated Investigations suggests the future: vendors won't just expose data through MCP — they'll ship autonomous investigation capabilities on top of it.

**LLM observability is the newest frontier.** With Opik, Langfuse, LangSmith, and OpenTelemetry all shipping MCP servers, a dedicated ecosystem is forming around tracking LLM traces, evaluating prompt performance, and orchestrating ML pipelines. This subcategory barely existed six months ago — it's now one of the fastest-growing areas in MCP.
