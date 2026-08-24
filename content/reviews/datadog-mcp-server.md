---
title: "The Datadog MCP Server — Enterprise Observability With Agent-Native Tool Design"
date: 2026-03-14T13:35:10+09:00
description: "Datadog's official MCP server puts 140+ tools across 17+ modular toolsets at your agent's fingertips — logs, metrics, traces, APM, alerting, case management, workflows, database"
og_description: "Datadog's official MCP server: 140+ tools, 17+ modular toolsets and growing, GA since March 2026. 43 GitHub stars. Kubernetes toolset added. Rating: 4/5."
content_type: "Review"
card_description: "Datadog's official MCP server for AI-assisted observability. 140+ tools across 17+ modular toolsets covering logs, metrics, traces, APM, DDSQL, alerting, case management, workflows, database monitoring, error tracking, feature flags, LLM observability, synthetics, Kubernetes, and more. Code Security MCP for shift-left scanning. Remote-first, Streamable HTTP, GA since March 9, 2026."
categories: ["/categories/observability-monitoring/"]
last_refreshed: 2026-08-24
sources_audited: 2026-08-24
---

**At a glance:** [43 GitHub stars, 33 commits, MIT license](https://github.com/datadog-labs/mcp-server) (as of August 24, 2026), 140+ tools across 17+ modular toolsets (see August 2026 note — [Datadog's live tools reference](https://docs.datadoghq.com/mcp_server/tools/) now lists more), [GA since March 9 2026](https://www.globenewswire.com/news-release/2026/03/09/3251890/0/en/Datadog-Launches-MCP-Server-to-Provide-AI-Agents-with-Secure-Real-Time-Access-to-Unified-Observability-Data.html), [Azure SRE Agent](https://techcommunity.microsoft.com/blog/appsonazureblog/get-started-with-datadog-mcp-server-in-azure-sre-agent/4497123) + [OpenAI Codex CLI](https://www.datadoghq.com/blog/openai-datadog-ai-devops-agent/) + Gemini CLI integrations, [Code Security MCP](https://github.com/datadog-labs/datadog-code-security-mcp) (Preview)

The Datadog MCP server gives AI agents direct access to your Datadog platform — logs, metrics, traces, dashboards, monitors, incidents, hosts, services, events, notebooks, and more. Everything your team sees in the Datadog web UI, your agent can now query programmatically.

It's official. Datadog builds and maintains it at [datadog-labs/mcp-server](https://github.com/datadog-labs/mcp-server). The GitHub repo is minimal ([43 stars, 33 commits](https://github.com/datadog-labs/mcp-server), MIT license, as of August 24, 2026) because Datadog hosts the server itself — there's nothing to install, fork, or self-host. The MCP server is **[generally available](https://www.globenewswire.com/news-release/2026/03/09/3251890/0/en/Datadog-Launches-MCP-Server-to-Provide-AI-Agents-with-Secure-Real-Time-Access-to-Unified-Observability-Data.html)** as of March 9, 2026, having graduated from preview status.

This is the third observability MCP server we've reviewed after [Sentry](/reviews/sentry-mcp-server/) (4/5) and [Grafana](/reviews/grafana-mcp-server/) (4/5). Where Sentry is deep and narrow (error tracking) and Grafana is open-source and multi-vendor, Datadog is the enterprise full-stack play. It covers more operational surface than any other observability MCP server — and it's the only one with toolsets for LLM observability, feature flags, database monitoring, and synthetic testing.

## What's New (May 2026 Update)

**Tool count surged: 80+ → 140+ across 17 toolsets.** [The Datadog MCP documentation](https://docs.datadoghq.com/mcp_server/tools/) now lists 140+ total tools across 17 toolsets (as of May 2026) — a near-doubling from the 80+ tools at the April review. This reflects both deeper toolsets and a new 17th toolset added since then. (This count is already out of date again — see the August 2026 note below.)

**Kubernetes toolset added (17th).** A new Kubernetes toolset (3 tools, GA) gives agents direct access to Kubernetes workload data from within Datadog — extending the server's operational surface into container orchestration. This means agents can now correlate infrastructure-level Kubernetes state with logs, APM traces, and monitors without switching tools.

**DBM toolset deepened: 11 tools.** The Database Monitoring toolset expanded significantly — now 11 tools (GA), up from the generic "query database plans and samples" coverage in the April review. Agents can drill into slow query analysis, wait event breakdowns, and database host performance with more granularity.

**Security toolset: 7 tools.** The Security toolset grew from 5 to 7 tools, adding additional security signals and findings capabilities. Combined with the companion Code Security MCP (local scanning), Datadog's security MCP surface is now the broadest of any observability vendor.

**Client support expanded to 13 named clients.** The official client list now includes Gemini CLI, Kiro (Amazon's new AI IDE), Devin, and OpenCode — additions since the April review. The full confirmed list: Cursor, Claude Code, Claude Desktop, Gemini CLI, VS Code, Warp, Devin, JetBrains, Codex CLI, Goose, OpenCode, GitHub Copilot, Kiro. Rapid client integration across competing AI ecosystems suggests Datadog is treating MCP client breadth as a competitive priority.

**GitHub: official repo 32 → 37 stars.** Modest growth; still no versioned releases since the server is fully remote-managed by Datadog. The community server (winor30) moved fractionally: 141 → 142 stars, 70 → 71 forks, still v1.7.0 (October 2025, no new release).

**PulseMCP traffic growth.** Official server: ~127K → ~134K all-time (+5.5%), ~530 → ~834 weekly (+57%). Community server (winor30): ~319K → ~390K all-time (+22%), ~13.5K → ~19.7K weekly (+46%), now ranked #110 weekly — accelerating faster than the official server.

**Datadog publishing MCP security research.** Datadog's Security Labs published [a case study on SQL injection in the (Anthropic reference) PostgreSQL MCP server](https://securitylabs.datadoghq.com/articles/mcp-vulnerability-case-study-SQL-injection-in-the-postgresql-mcp-server/), and the Datadog blog published [a guide on building SIEM detection rules for MCP servers](https://www.datadoghq.com/blog/mcp-detection-rules/). This positions Datadog as both an MCP vendor and an MCP security analyst — a smart dual role that builds credibility while cross-selling Cloud SIEM.

**[DASH 2026: June 9-10, NYC](https://www.globenewswire.com/news-release/2026/02/18/3240498/0/en/Datadog-Announces-DASH-2026-the-AI-and-Observability-Event-of-the-Year.html).** Datadog's annual conference is under 3 weeks away. No specific MCP pre-announcements have been made, but DASH has historically been when Datadog reveals major product updates. Bits AI, DDSQL GA status, and additional toolset additions are all plausible announcements. *(See the August 2026 update below for what was actually announced.)*

## August 2026 correction and update

This review's numbers were last refreshed May 18, 2026. Re-verifying them for this claim-level audit (August 13, 2026) turned up real drift and one internal inconsistency — corrected here rather than silently:

- **GitHub stars/commits corrected.** The figures quoted above the May update (22 stars, 13 commits) were a stale leftover from an earlier draft that never got updated — they contradicted this same page's own "at a glance" line (37 stars, 21 commits). The verified current count, as of the August 13 audit, was **43 stars, 30 commits**; re-checked for this August 24 audit, it's now **[43 stars, 33 commits](https://github.com/datadog-labs/mcp-server)** (stars unchanged, three more commits).
- **Toolset/tool count has grown again.** [Datadog's live tools reference](https://docs.datadoghq.com/mcp_server/tools/) now documents toolsets beyond the 17 catalogued below — including `audit-trail`, `cost`, `code-exec`, `data-observability`, `experiments`, `forms`, `product-analytics`, `profiling`, and `remote-actions` — so both the toolset count and total tool count exceed the "140+ across 17" figure used throughout this review. Check the live reference for current totals rather than treating the numbers below as current.
- **Code Security MCP grew from 4 tools to 6.** The companion server's [README](https://github.com/datadog-labs/datadog-code-security-mcp) now lists `datadog_code_security_scan` (combined SAST/secrets/SCA/IaC) and `datadog_sast_scan` in addition to the four tools described in the April 2026 entry below.
- **The community server (winor30) is not stalled at v1.7.0 anymore.** It shipped [v1.8.0 on June 22, 2026](https://github.com/winor30/mcp-server-datadog/releases) (MCP SDK upgrade, `DATADOG_STORAGE_TIER` support), after eight months of dormancy. Current count: **[143 stars, 76 forks](https://github.com/winor30/mcp-server-datadog)**.
- **DASH 2026 happened as scheduled.** Per [Datadog's own DASH 2026 feature roundup](https://www.datadoghq.com/blog/dash-2026-new-feature-roundup-keynote/), the event's AI-agent announcements centered on the broader Bits AI product line (Bits Code reaching GA, plus previews of Bits Detection, Memories, Remediation, Infrastructure Operations, and Release/Testing agents) rather than new MCP server toolsets specifically.
- **Client list has grown past 13.** [Datadog's setup docs](https://docs.datadoghq.com/mcp_server/setup/) now list around 15 named clients, adding ChatGPT and Copilot CLI to the list described below.
- **PulseMCP traffic estimates removed.** This review previously cited specific PulseMCP all-time/weekly visitor figures for both the official and community servers. Re-checking them for this audit found the official server's reported all-time figure had dropped from ~134K to ~9.8K between the May and August checks — a swing too large to be organic and a sign these third-party estimates are too volatile to state as fact. Specific PulseMCP numbers have been removed from this review; the qualitative point that the community server draws substantially more traffic than the official one still holds per PulseMCP's own listings ([official](https://www.pulsemcp.com/servers/datadog), [community](https://www.pulsemcp.com/servers/winor30-datadog)), but treat any specific number there as a rough, moving estimate rather than a citable fact.

### August 24, 2026 follow-up — per-toolset tool counts checked against the live reference

This claim-level re-audit went further than the August 13 pass: instead of just confirming the toolset list had grown, it read [Datadog's live tools reference](https://docs.datadoghq.com/mcp_server/tools/) tool-by-tool for the toolsets this review states specific counts for. Most held up; three didn't, and one differentiator claim (LLM observability) gets a firmer source:

- **APM toolset: 11 tools, not 15.** The live reference lists 11 APM tools (`apm_search_spans`, `apm_query_trace`, `apm_discover_span_tags`, `apm_get_primary_tag_keys`, `apm_search_watchdog_stories`, `apm_get_watchdog_story`, `apm_latency_bottleneck_summary`, `get_change_stories`, `semantic_search_change_stories`, `apm_search_recommendations`, `apm_get_recommendation`) — down from the "15 tools" this review has stated since the April update. Whether Datadog consolidated tools or the original count was inflated isn't verifiable from the doc alone; either way, 11 is the current, checkable figure.
- **Security toolset: 17 tools, not 7.** The live reference now lists 17 Security tools (secrets scanning plus a full signals/IOC/detection-rule/suppression set: `get_datadog_security_signals_schema`, `search_datadog_security_signals`, `analyze_datadog_security_signals`, `get_datadog_security_signal`, `update_datadog_security_signals_triage`, `search_datadog_security_ioc_indicators`, `get_datadog_security_ioc_indicator`, `update_datadog_security_ioc_indicator_triage`, `get_datadog_security_ioc_schema`, `get_datadog_security_detection_rules_schema`, `get_datadog_security_detection_rules`, `create_datadog_security_detection_rule`, `update_datadog_security_detection_rule`, `delete_datadog_security_detection_rules`, `get_datadog_security_suppressions`, `create_datadog_security_suppression`, plus `datadog_secrets_scan`) — more than double the "7 tools" figure this review has carried since May.
- **Reference Tables toolset: 6 tools, not 4.** The live reference lists `list_reference_tables`, `list_reference_table_rows`, `get_reference_table_rows`, `append_reference_table_rows`, `upsert_reference_table_rows`, `create_reference_table` — up from the 4 described below.
- **Confirmed unchanged (verified tool-by-tool against the live reference):** Alerting (6), Cases (9), Dashboards (6), DDSQL (6), Feature Flags (8), Kubernetes (3), Networks (4), Onboarding (7), Database Monitoring (11), Core (~20-21).
- **LLM observability is a real, separately-documented toolset (`llmobs`).** This review has claimed "LLM observability" as a Datadog differentiator since March without ever citing a dedicated toolset for it — the toolset breakdown below only lists LLM observability as one target of the Onboarding toolset's guided setup. Datadog documents an `llmobs` toolset with its own tools (trace/span search, experiment analysis, evaluator management) on a **separate** docs page, [Agent Observability MCP and Skills](https://docs.datadoghq.com/llm_observability/mcp_server/), not the main tools reference — which is why earlier passes missed it. This strengthens rather than undercuts the differentiator claim, but the citation was missing until now.
- **Total toolset count is at least 27, not fully enumerable.** Combining the main tools reference's 24 documented toolset sections (core, alerting, apm, audit-trail, cases, cost, code-exec, dashboards, data-observability, dbm, ddsql, error-tracking, experiments, feature-flags, forms, kubernetes, networks, onboarding, product-analytics, profiling, reference-tables, remote-actions, rum, security) with software-delivery and synthetics (confirmed still present, documented on adjacent pages) and llmobs (documented separately, above) gives at least 27. Datadog does not publish a single running total anywhere we could find — the "check the live reference for current totals" guidance in the note above still stands.
- **Client list: 15 confirmed, adding Cline.** [Datadog's setup docs](https://docs.datadoghq.com/mcp_server/setup/) currently list exactly 15 named clients: ChatGPT, Claude, Claude Code, Codex CLI, Copilot CLI, Cursor, Devin, Gemini CLI, Goose, JetBrains IDEs, Kiro, OpenCode, VS Code, Warp, and **Cline** — Cline is a new addition not previously noted in this review.

### Previous updates (April 2026)



**Code Security MCP launched (April 7, 2026).** Datadog released a **separate** MCP server focused on security scanning of AI-generated code. The [Code Security MCP](https://github.com/datadog-labs/datadog-code-security-mcp) (5 GitHub stars, Go, Preview) runs locally via stdio and provides 4 tools: `datadog_secrets_scan` (hardcoded credentials), `datadog_sca_scan` (dependency CVEs), `datadog_iac_scan` (infrastructure-as-code misconfigurations), and `datadog_generate_sbom` (software bill of materials — no auth required). Installs via Homebrew or GitHub releases. Supports Claude Code, Claude Desktop, Cursor, VS Code. Requires DD_API_KEY and DD_APP_KEY for most scans. This is Datadog's answer to shift-left security for the AI coding era — catching vulnerabilities before they reach a pull request.

**Toolsets expanded from 14 to 16.** Three new toolsets have been added since our last review:
- **DDSQL (Preview)** — SQL querying against Datadog data: schema search, column inspection, unstructured field search, query execution, and shareable link creation
- **Onboarding** — guided setup for browser monitoring, devices, Kubernetes, LLM observability, test optimization, serverless, and source map uploads
- **Reference Tables** — CRUD operations for Datadog reference tables (list, get rows, append rows, create)

**Existing toolsets significantly expanded.** The APM toolset now has 15 tools (up from generic "in-depth trace analysis"), including latency bottleneck analysis, tag-level latency decomposition, Watchdog stories, change detection, recommendations, and a structured investigation methodology. Dashboards gained full CRUD (upsert, delete, widget reference, validation, widget expert). Alerting added monitor creation, SLO search, and monitor coverage analysis. Feature Flags expanded to 8 tools with environment management, allocation sync, and implementation checking. Security now includes secrets scanning and structured findings analysis. Software Delivery added code coverage and flaky test tools. Synthetics gained editing and a wizard tool. Total tool count is now 80+ across 16 toolsets.

**[Fair-use rate limits published.](https://docs.datadoghq.com/bits_ai/mcp_server/)** The MCP server now enforces documented limits: 50 requests per 10-second burst and 50,000 monthly tool calls. All tool calls are recorded in the Datadog Audit Trail with metadata including tool names and user identity. Two metrics track usage: `datadog.mcp.session.starts` and `datadog.mcp.tool.calls`.

**14 supported clients.** The official client list now includes Cursor, Claude Code, Claude Desktop, GitHub Copilot, JetBrains IDEs, VS Code, Warp, and others — up from the original ~8 clients at launch.

**Bits AI next-gen agents.** [Bits AI SRE Agent got a major upgrade](https://www.datadoghq.com/blog/bits-ai-sre-deeper-reasoning/): deeper reasoning, approximately 2x faster (completing investigations in ~3-4 minutes, per Datadog), and broader data access now covering source code, events, RUM, Database Monitoring, Network Path, and Continuous Profiler. [Bits AI Security Analyst reached GA in Cloud SIEM](https://www.datadoghq.com/blog/bits-ai-security-analyst/) ([press release](https://www.datadoghq.com/about/latest-news/press-releases/bits-ai-security-analyst-reduces-threat-investigation-time/)). [Bits AI Dev Agent can now propose code fixes from SRE-identified root causes and create merge-ready PRs](https://investors.datadoghq.com/news-releases/news-release-details/datadog-unveils-latest-ai-agents-rapidly-resolve-application).

**Datadog Experiments GA (April 2, 2026).** Built on the [Eppo acquisition](https://www.datadoghq.com/blog/datadog-acquires-eppo/), this new product embeds A/B testing into observability — connecting product experiments to business metrics, APM, logs, and RUM with real-time guardrails. Relevant for MCP users who can now query experiment results alongside operational data.

**DASH 2026 announced.** Datadog's annual conference is set for June 9–10 at North Javits Center, NYC. Expect MCP server and Bits AI agent updates.

**GitHub repo growth.** Stars 22 → 32 (+45%), commits 13 → 21. Still primarily examples and documentation — the server itself is hosted by Datadog. Zero open PRs, no releases published (server updates happen server-side).

**PulseMCP traffic.** The official Datadog MCP server now has its own PulseMCP listing: ~127K all-time visitors, ~530 weekly, #279 globally. The community server (winor30) continues to outpace it: ~319K all-time, ~13.5K weekly, #134 globally (141 stars, 70 forks, 18 open PRs, still v1.7.0).

### Previous updates (March 2026)

**[General availability (March 9, 2026).](https://www.globenewswire.com/news-release/2026/03/09/3251890/0/en/Datadog-Launches-MCP-Server-to-Provide-AI-Agents-with-Secure-Real-Time-Access-to-Unified-Observability-Data.html)** Datadog officially graduated the MCP server from Preview to GA, meaning it's now covered by standard Datadog support and SLA commitments. The announcement came with a press release, dedicated product page, and two blog posts — the use cases blog documenting four enterprise patterns and the [engineering blog detailing agent-native tool design lessons](https://www.datadoghq.com/blog/engineering/mcp-server-agent-tools/).

**Two new toolsets: Cases and Workflows.** Case Management tools let agents create, search, update, and manage cases — linking Jira issues, escalating priority, and tracking investigations. The Workflows toolset adds automation capabilities: listing, inspecting, executing, and configuring Datadog Workflow Automations from within an agent.

**Azure SRE Agent integration (February 25, 2026).** [Microsoft published an official guide](https://techcommunity.microsoft.com/blog/appsonazureblog/get-started-with-datadog-mcp-server-in-azure-sre-agent/4497123) for connecting the Datadog MCP server to Azure SRE Agent, with pre-populated header keys in the Azure portal for streamlined setup.

**OpenAI Codex CLI embedding.** [OpenAI and Datadog partnered](https://www.datadoghq.com/blog/openai-datadog-ai-devops-agent/) to embed the MCP server within OpenAI's Codex CLI agent.

**Cohesity partnership.** [New integration](https://www.cohesity.com/newsroom/press/cohesity-partners-with-datadog-to-deliver-ai-agent-resilience/) focused on automated incident recovery for production AI environments.

**[Engineering blog (March 4, 2026)](https://www.datadoghq.com/blog/engineering/mcp-server-agent-tools/).** "Designing MCP tools for agents" — quantifying agent-native design decisions: CSV format achieves ~50% fewer tokens than JSON, YAML saves ~20% vs JSON, field trimming achieves 5x data density improvement.

## What It Does

The server exposes 140+ tools organized into **modular toolsets** — capability groups you enable or disable via the `?toolsets=` query parameter. This is Datadog's answer to context window management: don't load tools you don't need. *(The toolset breakdown below reflects the May 2026 update. As of this audit, [Datadog's live tools reference](https://docs.datadoghq.com/mcp_server/tools/) lists more toolsets than the 17 described here — see the August 2026 note above for specifics — so treat individual tool counts below as historical rather than current.)*

**Core Toolset** (enabled by default, ~20 tools)
- `analyze_datadog_logs` / `search_datadog_logs` — log analysis with SQL queries
- `search_datadog_spans` / `get_datadog_trace` — distributed trace investigation
- `search_datadog_metrics` / `get_datadog_metric` / `get_datadog_metric_context` — metrics discovery and querying
- `search_datadog_monitors` — monitor retrieval and configuration
- `search_datadog_incidents` / `get_datadog_incident` — incident management
- `search_datadog_dashboards` — dashboard discovery
- `search_datadog_hosts` — host information
- `search_datadog_services` / `search_datadog_service_dependencies` — service catalog and dependency mapping
- `search_datadog_events` — event stream queries
- `search_datadog_rum_events` — Real User Monitoring data
- `get_datadog_notebook` / `search_datadog_notebooks` / `create_datadog_notebook` / `edit_datadog_notebook` — notebook CRUD

**Alerting Toolset** (opt-in, 6 tools)
- Validate and create monitors, search monitor groups, retrieve templates, search SLOs, get monitor coverage analysis

**APM Toolset** (opt-in, Preview, 15 tools)
- Span search, trace exploration and comparison, trace metrics analysis, tag discovery, Watchdog stories and change detection, latency bottleneck and tag analysis, recommendations, structured investigation methodology

**Cases Toolset** (opt-in, 9 tools)
- Create, search, update, and manage cases; add comments; link Jira issues; manage projects; search users

**Dashboards Toolset** (opt-in, 6 tools)
- Full dashboard CRUD: get, upsert, delete; widget reference, validation, and widget expert assistant

**Database Monitoring Toolset** (opt-in, 11 tools)
- Slow query analysis, wait event breakdowns, database host performance, query plans and samples

**DDSQL Toolset** (opt-in, Preview, 6 tools) — *new*
- SQL querying against Datadog data: schema search, column inspection, unstructured field search, query execution, shareable link creation

**Error Tracking Toolset** (opt-in)
- Search and retrieve error tracking issues

**Feature Flags Toolset** (opt-in, 8 tools)
- List, get, create flags; manage environments and allocations; check implementation; sync allocations

**Networks Toolset** (opt-in, 4 tools)
- Cloud network monitoring analysis, NDM device and interface search

**Onboarding Toolset** (opt-in, 7 tools) — *new*
- Guided setup for browser monitoring, devices, Kubernetes, LLM observability, test optimization, serverless, source map uploads

**Reference Tables Toolset** (opt-in, 4 tools) — *new*
- List, get rows, append rows, create reference tables

**Kubernetes Toolset** (opt-in, 3 tools) — *new*
- Kubernetes workload data access, correlating container orchestration state with Datadog observability

**Security Toolset** (opt-in, 7 tools)
- Secrets scanning, security signals, security findings schema/analysis/search, Cloud SIEM detection

**Software Delivery Toolset** (opt-in, 7 tools)
- CI pipeline event search and aggregation, flaky tests, test event aggregation/search, code coverage by branch and commit

**Synthetics Toolset** (opt-in, 3 tools)
- Get, edit synthetic tests; test creation wizard

**Workflows Toolset** (opt-in, 5 tools)
- List, inspect, execute workflows; get workflow instances; configure agent triggers

That's 17 toolsets (4 new since March), each adding specialized capabilities. The modular design means a debugging-focused agent can load just core + APM + error-tracking, while an SRE agent might load core + alerting + database monitoring + synthetics. You choose what fits the workflow.

## Setup

Datadog's setup is the simplest of any observability MCP server — there's nothing to install:

**For Claude Code:**

```bash
claude mcp add --transport http datadog https://mcp.datadoghq.com/api/unstable/mcp-server/mcp
```

**Via `.mcp.json`:**

```json
{
  "mcpServers": {
    "datadog": {
      "type": "http",
      "url": "https://mcp.datadoghq.com/api/unstable/mcp-server/mcp",
      "headers": {
        "DD-API-KEY": "<your-api-key>",
        "DD-APPLICATION-KEY": "<your-application-key>"
      }
    }
  }
}
```

**To enable specific toolsets, append them to the URL:**

```
https://mcp.datadoghq.com/api/unstable/mcp-server/mcp?toolsets=core,apm,alerting
```

**Regional endpoints:**

| Region | URL |
|--------|-----|
| US1 (default) | `mcp.datadoghq.com` |
| US3 | `mcp.us3.datadoghq.com` |
| US5 | `mcp.us5.datadoghq.com` |
| EU1 | `mcp.datadoghq.eu` |
| AP1/AP2 | Region-specific variants |

The server uses **Streamable HTTP** transport exclusively — no stdio, no local process. Authentication supports **OAuth 2.0** for interactive flows and **API key + application key** via HTTP headers for server-to-server or headless setups.

The server works with 13 named clients including Claude Code, Claude Desktop, Cursor, Gemini CLI, OpenAI Codex, GitHub Copilot, JetBrains IDEs, VS Code, Warp, Goose, Devin, OpenCode, and Kiro — plus a custom agent option. (As of this August 24, 2026 audit, [Datadog's setup docs](https://docs.datadoghq.com/mcp_server/setup/) confirm exactly 15 named clients: ChatGPT, Claude, Claude Code, Codex CLI, Copilot CLI, Cursor, Devin, Gemini CLI, Goose, JetBrains IDEs, Kiro, OpenCode, VS Code, Warp, and Cline — Cline is a new addition since this list was last checked.)

## What's Good

**The broadest observability tool surface in the MCP ecosystem.** No other single MCP server covers logs, metrics, traces, APM, alerting, case management, workflow automation, database monitoring, error tracking, feature flags, LLM observability, product analytics, networks, security, software delivery, synthetic testing, DDSQL querying, Kubernetes, and onboarding. [Grafana MCP](/reviews/grafana-mcp-server/) (40+ tools) is comprehensive for open-source stacks, but Datadog's 140+ tools across 17+ modular toolsets (and still growing — see [Datadog's live tools reference](https://docs.datadoghq.com/mcp_server/tools/)) cover operational surface that no other server touches — particularly LLM observability, feature flags, DDSQL, case management, workflows, synthetics, and Kubernetes workload correlation.

**Agent-native tool design, not an API wrapper.** [Datadog's engineering blog](https://www.datadoghq.com/blog/engineering/mcp-server-agent-tools/) details how they rethought tool design specifically for agents. Key decisions: CSV output instead of JSON (50% fewer tokens for tabular data), field trimming to remove unused data, and **token-budget pagination** — the server cuts off responses after a configurable token budget and returns a cursor for more, instead of paginating by record count. This prevents the "one huge log eats the entire context window" problem that plagues other observability servers. They also support SQL-like queries against logs (`SELECT service, COUNT(*) FROM logs WHERE status='error' GROUP BY service`), achieving 40% cost reduction in evaluation scenarios compared to raw log retrieval.

**Modular toolsets prevent context window waste.** Like Grafana's `--disable-<category>` flags, Datadog's toolset system lets you load only the capabilities your agent needs. But Datadog takes it further: toolsets are URL-parameterized (`?toolsets=core,apm`), meaning you can have multiple MCP server configurations — one for debugging, one for incident response, one for performance analysis — all pointing to the same server with different toolset combinations. With 16 toolsets now available, this modularity matters even more.

**Code Security MCP for shift-left scanning.** The new Code Security MCP (April 2026, Preview) is a separate local server that scans AI-generated code for vulnerabilities in real time — SAST, SCA, secrets detection, and IaC scanning in a single tool. This is a smart architectural choice: keeping security scanning local (stdio) while observability stays remote (Streamable HTTP) means security scans never leave your machine. No other observability vendor offers a companion security MCP server.

**Zero-install remote hosting.** While Grafana requires you to run the MCP server yourself and Sentry hosts at `mcp.sentry.dev`, Datadog provides managed endpoints across multiple regions. There's no process to keep running, no Docker container to manage, no version to update. The server is always the latest version because Datadog maintains it.

**Actionable error messages.** When an agent writes a bad query (e.g., misspelling a field name), [the server returns suggestions](https://www.datadoghq.com/blog/engineering/mcp-server-agent-tools/): "unknown field 'stauts' — did you mean 'status'?" This kind of agent-aware error handling reduces retry loops and wasted tool calls. Server instructions also guide agents to documentation when they're uncertain about query syntax.

**RBAC-aware security.** The server inherits your existing Datadog RBAC controls — agents can only access what the authenticated user or service account can access. This means you don't need to build a separate permission model for AI access. It also [supports HIPAA-eligible use under a signed BAA](https://www.datadoghq.com/legal/hipaa-eligible-services/) ([HIPAA compliance docs](https://docs.datadoghq.com/data_security/hipaa_compliance/)), which is rare for MCP servers.

**GA status.** Most observability MCP servers are in preview, beta, or pre-1.0. Datadog's is generally available, meaning it's covered by Datadog's standard support and SLA commitments. For enterprise teams evaluating MCP servers, GA status matters.

## What's Not

**API key authentication by default.** While OAuth 2.0 is available for interactive flows, most setups use `DD-API-KEY` and `DD-APPLICATION-KEY` headers. These are organization-level and user-level credentials respectively — more powerful than Sentry's scoped OAuth tokens. If an agent config file is compromised, the attacker gets broad Datadog API access. Sentry's browser-based OAuth flow is more secure by design.

**Datadog's pricing is the real barrier.** The MCP server itself doesn't cost extra, but it requires an existing Datadog subscription. [Datadog's pricing](https://www.datadoghq.com/pricing/) is notoriously complex — per-host infrastructure monitoring ($15/host/mo Pro, $23/host/mo Enterprise, annual billing), log ingestion at $0.10/GB plus indexing at roughly $1.70-2.50 per million events depending on retention, APM with trace retention pricing, and each product adds another line item. There's a [14-day free trial](https://docs.datadoghq.com/integrations/guide/aws-marketplace-datadog-trial/), but no permanent free tier that covers enough for meaningful MCP use. Compare this to [Sentry](https://sentry.io/pricing/) (free tier: 5K errors/mo, not 10K as this review previously said), [New Relic](https://newrelic.com/pricing/free-tier) (free 100GB/mo ingest), or [Grafana Cloud](https://grafana.com/pricing/) (free tier: 10K metrics series, 50GB each of logs/traces/profiles, 14-day retention).

**Not GovCloud compatible.** ["The Datadog MCP Server is not GovCloud compatible,"](https://docs.datadoghq.com/mcp_server/) per Datadog's own documentation. Government and defense teams using Datadog's GovCloud offering cannot use the MCP server.

**Closed source, no self-hosting option.** The [GitHub repo](https://github.com/datadog-labs/mcp-server) (43 stars as of August 2026) contains examples and documentation, not the server code. You cannot fork it, extend it, audit the code, or run it on your own infrastructure. For teams with strict data sovereignty requirements or those who want to customize tool behavior, this is a hard constraint. Grafana's MCP server (Apache 2.0) is the opposite approach.

**[Fair-use rate limits](https://docs.datadoghq.com/bits_ai/mcp_server/) may constrain heavy users.** The server enforces a 50-request per 10-second burst limit and 50,000 monthly tool calls. For a single developer this is generous, but automated agent workflows running multiple investigations per day could exhaust the monthly cap — especially if each investigation involves 20-30 tool calls across multiple toolsets.

**"Unstable" API path.** The endpoint URL contains `/api/unstable/` — Datadog's signal that the API surface may change without notice. Despite GA status, the underlying MCP protocol integration is still evolving. Tool names, response formats, and toolset boundaries could shift between updates.

**Requires anticipating toolset needs.** You configure toolsets at connection time via URL parameters. If your agent encounters a scenario needing a toolset you didn't enable (e.g., you loaded core but need APM trace analysis), you can't dynamically add it mid-conversation. You need to disconnect and reconnect with the right toolsets. Grafana has the same limitation, but since Grafana runs locally, reconnecting is faster.

**Incident timeline data missing.** The incident tools can list and retrieve incidents, but the timeline data (the chronological record of actions taken during an incident) is not yet available. For incident post-mortems, this is a significant gap.

**Community alternatives are fragmented.** The most popular community Datadog MCP server ([winor30/mcp-server-datadog](https://github.com/winor30/mcp-server-datadog), 143 stars, 76 forks, on [v1.8.0 as of June 22, 2026](https://github.com/winor30/mcp-server-datadog/releases)) predates the official server and covers different ground — host muting, downtime scheduling, RUM analysis. It draws substantially more traffic than the official server per [PulseMCP's estimates](https://www.pulsemcp.com/servers/winor30-datadog) (these third-party traffic figures fluctuate significantly run to run and shouldn't be read as precise) because it supports local stdio deployment. If you need capabilities the official server doesn't have (like muting hosts or scheduling downtimes), you'd need to run both, doubling your context window cost.

## Alternatives

**[Sentry MCP Server](/reviews/sentry-mcp-server/)** (4/5) — if you need deep error tracking with AI root cause analysis (Seer), OAuth 2.0 authentication, and zero-install remote hosting. Sentry is narrower (errors only) but deeper in its niche. Use Sentry for debugging specific errors, Datadog for full-stack observability.

**[Grafana MCP Server](/reviews/grafana-mcp-server/)** (4/5) — the open-source alternative with 40+ tools, multi-vendor data source support (any Grafana backend), and self-hosting. If you want vendor independence, code auditability, or run a LGTM stack, Grafana is the natural choice. Datadog has more tools, but Grafana works with your existing infrastructure regardless of vendor.

**[winor30/mcp-server-datadog](https://github.com/winor30/mcp-server-datadog)** (143 stars, 76 forks, [v1.8.0](https://github.com/winor30/mcp-server-datadog/releases) as of June 2026) — the most popular community Datadog MCP server with 20+ tools including host management (mute/unmute), downtime scheduling, and RUM analysis. TypeScript, Apache 2.0, stdio transport. Draws substantially more [PulseMCP-estimated traffic](https://www.pulsemcp.com/servers/winor30-datadog) than the official server, though the exact multiplier is volatile and shouldn't be quoted precisely. Useful if you need local deployment, capabilities the official server doesn't cover, or want to avoid rate limits. It went eight months without a release (October 2025 to June 2026) before v1.8.0 shipped, so check the releases page for how actively it's maintained before depending on it.

**New Relic MCP Server** — 27 tools with natural language to NRQL translation. [More accessible pricing](https://newrelic.com/pricing/free-tier) (100GB/mo free tier). Still in Public Preview.

**Honeycomb MCP** — event-based observability with high-cardinality debugging. A fundamentally different approach — better for distributed system investigations, weaker for traditional APM dashboarding.

## Who Should Use This

**Use the Datadog MCP server if:**
- You're already on Datadog and want your agent to query logs, metrics, traces, and dashboards
- You need the broadest operational context — LLM observability, feature flags, database monitoring, synthetics
- You want zero-install setup with managed regional endpoints
- You need GA status and enterprise support guarantees
- You want agent-native tool design with token-budget pagination and SQL-like log queries

**Skip it if:**
- You don't have a Datadog subscription — the MCP server is free but the platform is not
- You need open-source code auditability or self-hosting — Grafana is the choice
- You're in a GovCloud environment — not supported
- You want OAuth-first security — Sentry and PagerDuty are better here
- You need incident timeline data — not yet available

{{< verdict rating="4" summary="The most feature-rich observability MCP server, purpose-built for enterprise teams already on Datadog" >}}
The Datadog MCP server is what happens when the largest commercial observability platform designs an MCP integration from the ground up — not wrapping their API, but rethinking tool design for AI agents. The token-budget pagination, CSV-over-JSON formatting, SQL-like log queries, and modular toolsets show a team that understands agent constraints. With 140+ tools across 17+ modular toolsets (and growing — see the August 2026 note above) — including DDSQL querying, Kubernetes workload correlation, a deepened DBM toolset (11 tools), expanded Security toolset, and support for 13+ named AI clients including Gemini CLI and Kiro — it covers more operational surface than any other MCP server. The Code Security MCP companion server (Preview) adds shift-left security scanning, and Datadog is now publishing MCP security research, positioning itself as both vendor and ecosystem watchdog. The 4/5 rating reflects what's genuinely best-in-class (broadest tool coverage, agent-native design, zero-install remote hosting, GA status, RBAC-aware security, growing Bits AI agent ecosystem, broad client support across competing AI ecosystems) balanced against real constraints ([Datadog's complex pricing](https://www.datadoghq.com/pricing/) as the true barrier to entry, [fair-use rate limits](https://docs.datadoghq.com/bits_ai/mcp_server/) at 50,000 monthly tool calls, API key auth by default, closed-source code, unstable API path, no GovCloud support, and a community server that reportedly draws substantially more traffic than the official one, per volatile third-party estimates). For enterprise teams already paying for Datadog, this is the obvious integration. For everyone else, the platform cost — not the MCP server — is what keeps the door closed.
{{< /verdict >}}

*Disclosure: We research MCP servers using publicly available documentation, GitHub repositories, changelogs, community discussions, and web sources. We do not test MCP servers hands-on or connect to live instances. All claims reflect what we can verify from public information.*

**Category**: [Observability & Monitoring](/categories/observability-monitoring/)

*This review's citations were last audited on 2026-08-24 using Claude Sonnet 5 (Anthropic). Content was last substantively refreshed 2026-05-18.*
