# New Relic MCP Server Review — 27 Tools, Free Tier

> New Relic's official MCP server puts 27 tools across 6 tag-based categories at your agent's fingertips — NRQL queries, entity management, alerting, incident response, performance analytics, and log analysis.


The New Relic MCP server gives AI agents direct access to your New Relic observability platform — entities, NRQL queries, alerts, incidents, deployments, logs, golden metrics, synthetic monitors, dashboards, and more. Ask questions in plain English and the server translates them into NRQL queries automatically.

[New Relic](https://newrelic.com/) was [founded in 2008 by Lew Cirne](https://en.wikipedia.org/wiki/New_Relic). The company was taken private in November 2023 when [Francisco Partners](https://www.franciscopartners.com/) and [TPG](https://www.tpg.com/) [completed a $6.5 billion acquisition at $87/share](https://newrelic.com/press-release/20231108). New Relic hasn't disclosed revenue publicly since going private — its last public trailing-twelve-month figure, from 2023, was [~$960M](https://companiesmarketcap.com/new-relic/revenue/). Third-party workforce trackers put current headcount at roughly 2,900-3,050 employees ([Tracxn: 3,040 as of Jun 30, 2026](https://tracxn.com/d/companies/new-relic/__qTQSKdFdcCdjn6XjUl6A23TnuDMRzDof9BJgDp01G6g); [Revelio Labs: ~2,985 as of Mar 2026](https://www.reveliolabs.com/companies/new-relic/employees)) — third-party estimates, not company-reported figures. [Michael Frendo was appointed CTO](https://newrelic.com/press-release/20260304) on March 4, 2026, and the platform was [named a Leader in the 2026 IDC MarketScape for AIOps](https://newrelic.com/blog/news/new-relic-named-a-leader-in-the-2026-idc-marketscape-for-worldwide-aiops) on March 24, 2026.

**At a glance:** [7 GitHub stars](https://github.com/newrelic/mcp-server), 0 forks, 2 commits, last commit Oct 2025, 4 open issues, remote-hosted at mcp.newrelic.com, Streamable HTTP, Public Preview, [27 tools across 6 tag-based categories](https://docs.newrelic.com/docs/agentic-ai/mcp/tool-reference/), [PulseMCP ~10.5K all-time visitors](https://www.pulsemcp.com/servers/newrelic) (~#2,132 globally, ~216 this week — as of 2026-08-23; these figures move week to week).

It's official. New Relic builds and maintains it at [newrelic/mcp-server](https://github.com/newrelic/mcp-server). The GitHub repo is minimal (7 stars, 2 commits) because New Relic hosts the server itself at `mcp.newrelic.com` — there's nothing to install locally. The MCP server has been in **Public Preview** since [its November 2025 launch](https://newrelic.com/blog/news/new-relic-ai-mcp-server-launch).

This is the fourth observability MCP server we've reviewed after [Sentry](/reviews/sentry-mcp-server/) (4/5), [Grafana](/reviews/grafana-mcp-server/) (4/5), and [Datadog](/reviews/datadog-mcp-server/) (4/5). Where Sentry is deep and narrow (error tracking), Grafana is open-source and multi-vendor, and Datadog is the enterprise full-stack play, New Relic is the accessible full-stack option — 27 tools with natural language querying and a [permanent free tier that includes 100GB/month of data ingestion](https://newrelic.com/pricing).

**April 2026 context:** New Relic launched the **[New Relic Agentic Platform](https://www.businesswire.com/news/home/20260224168375/en/)** (February 24, 2026), a [no-code platform for building observability AI agents](https://techcrunch.com/2026/02/24/new-relic-launches-new-ai-agent-platform-and-opentelemetry-tools/) with built-in MCP support. The MCP server itself also went GA as an integration for **[Atlassian Rovo Ops](https://community.atlassian.com/forums/Jira-Service-Management-articles/Announcing-GA-of-New-Relic-MCP-for-Rovo-Ops-Bring-observability/ba-p/3195727)** (February 23, 2026), enabling [natural language observability queries across Jira Service Management, Confluence, and IDEs](https://community.atlassian.com/forums/Jira-Service-Management-articles/Announcing-GA-of-New-Relic-MCP-for-Rovo-Ops-Bring-observability/ba-p/3195727) — New Relic's own [announcement post](https://newrelic.com/blog/news/atlassian-agentic-integration) covers the Jira Service Management workflow specifically. At [New Relic Advance 2026](https://newrelic.com/blog/news/new-relic-advance-2026), additional capabilities were announced including the SRE Agent, Intelligent RCA, and Performance Risks Inbox. The core MCP server remains in Public Preview.

## Recent Updates (May 2026)

**Azure SRE Agent integration (April 29, 2026)** — Microsoft added a native New Relic connector type in the Azure SRE Agent portal. It pre-populates the MCP endpoint URL and `Api-Key` header, so Azure's SRE Agent can call New Relic directly when an alert fires or a deployment rolls back — enabling natural language incident investigation without leaving Azure tooling. This makes New Relic one of the first observability platforms with a first-class integration in a cloud provider's AI SRE offering. Setup guide published in [Microsoft Tech Community](https://techcommunity.microsoft.com/blog/appsonazureblog/get-started-with-the-new-relic-mcp-server-in-azure-sre-agent/4515268).

**Amazon Quick integration (May 5, 2026)** — AWS's enterprise AI assistant now connects to New Relic via MCP. [AWS's own announcement](https://aws.amazon.com/about-aws/whats-new/2026/05/amazon-quick-new-relic/) says users can invoke New Relic's AI agents from a conversational prompt in Quick — including alert insights, user impact analysis, log analysis, transaction diagnostics, and natural language NRQL queries — and generate a root cause analysis document with evidence links in a single chat exchange. New Relic became [the first observability platform with a native, one-click integration in Amazon Quick](https://aws.amazon.com/about-aws/whats-new/2026/05/amazon-quick-new-relic/), adding to the growing list of supported MCP clients beyond Claude, Cursor, and GitHub Copilot.

**New Relic Knowledge (GA May 25, 2026)** — New Relic's most significant AI capability addition since Advance 2026. Knowledge fuses real-time telemetry with historical incident data, system change logs, and operational context to give AI agents richer diagnostic grounding. Published [May 5, 2026](https://www.businesswire.com/news/home/20260505650102/en/New-Relic-Unveils-Knowledge-Capability-to-Power-Agents-with-Real-Time-System-Understanding), general availability is May 25. It directly powers the MCP server's incident correlation and RCA capabilities by adding historical pattern matching — so when an agent calls `list_recent_issues` or `analyze_deployment_impact`, it can surface context from prior incidents with similar signatures, not just current telemetry.

## What It Does

Re-verified directly against the [live tool reference](https://docs.newrelic.com/docs/agentic-ai/mcp/tool-reference/) on 2026-08-21: the server currently exposes **27 tools** organized into **6 categories**, filterable using `include-tags` HTTP headers so you can present only the tools relevant to your agent's current task. The tool count has moved around in New Relic's own materials and in this review's own history — 19 tools at original review time, 30+ cited mid-2026 — so treat any specific figure as a snapshot; 27 is what the live reference showed on the audit date above.

**Discovery (4 tools)**
- `get_entity` — get entity details by GUID
- `search_entity_with_tag` — search entities using tag key/value pairs
- `list_related_entities` — find related entities for dependency mapping
- `list_available_new_relic_accounts` — list accessible accounts

**Data Access (4 tools)**
- `execute_nrql_query` — execute arbitrary NRQL queries against NRDB
- `natural_language_to_nrql_query` — convert plain English questions into NRQL, execute, and return results
- `list_recent_logs` — list recent logs with filtering
- `analyze_entity_logs` — analyze logs for a specific entity to identify error patterns and anomalous behavior

**Alerting (3 tools)**
- `list_alert_policies` — list alert policies, optionally filtering by name
- `list_alert_conditions` — list NRQL alert conditions for a specific policy
- `convert_time_period_to_epoch_ms` — utility for time-based queries

**Incident Response (5 tools)**
- `list_recent_issues` — list all open issues
- `search_incident` — search incidents with flexible filtering (both open and close events)
- `list_change_events` — list deployment and change events for an entity
- `analyze_deployment_impact` — analyze performance impact of a specific deployment
- `list_entity_error_groups` — get error groups from Errors Inbox

**Performance Analytics (6 tools)**
- `analyze_golden_metrics` — analyze throughput, response time, error rate, and saturation for an entity
- `analyze_transactions` — analyze transaction performance
- `analyze_entity_logs` — cross-referenced in data access for log-based performance analysis
- `analyze_kafka_metrics` — analyze Kafka consumer lag, producer throughput, message latency, and partition balance
- `analyze_threads` — analyze thread metric data including thread state, CPU usage, and memory consumption
- `list_garbage_collection_metrics` — list GC and memory metrics for an entity
- `list_entity_performance_risk_groups` — surface entities flagged with elevated performance risk (added since original review)

**Advanced Analysis & Reporting (3 tools)**
- `generate_alert_insights_report` — generate alert intelligence analysis reports
- `generate_user_impact_report` — generate end-user impact analysis for specific issues
- `list_synthetic_monitors` — list synthetic monitors for availability and performance checks

**Dashboards (2 tools)**
- `get_dashboard` — get dashboard details by ID
- `list_dashboards` — list all dashboards in your account

The `include-tags` header system lets you filter the tool corpus by category. Send `include-tags: discovery,data-access` and your agent only sees the 10 tools in those two categories — reducing the context window footprint and improving model focus.

## Setup

New Relic's setup is zero-install — the server is hosted remotely:

**For Claude Code:**

```bash
claude mcp add newrelic https://mcp.newrelic.com/mcp/ --transport http --header "Api-Key: NRAK-YOUR-KEY-HERE"
```

**Via `.mcp.json`:**

```json
{
  "mcpServers": {
    "newrelic": {
      "type": "http",
      "url": "https://mcp.newrelic.com/mcp/",
      "headers": {
        "Api-Key": "NRAK-YOUR-KEY-HERE"
      }
    }
  }
}
```

The server uses **Streamable HTTP** transport with Server-Sent Events capability — the most current version of the MCP specification. Authentication requires a [New Relic **User API Key**](https://docs.newrelic.com/docs/agentic-ai/mcp/overview/) (NRAK-prefixed). OAuth 2.0 is also supported for interactive flows.

The server works with [Claude, Cursor, VS Code (GitHub Copilot), ChatGPT](https://newrelic.com/blog/news/new-relic-ai-mcp-server-launch), Google's Gemini CLI, **Azure SRE Agent** (native connector as of April 29, 2026), **Amazon Quick** (as of May 5, 2026), and other MCP clients.

## What's Good

**Natural language to NRQL translation is genuinely useful.** NRQL is powerful but has a learning curve. New Relic's [`natural_language_to_nrql_query` tool](https://docs.newrelic.com/docs/agentic-ai/mcp/tool-reference/) lets you ask "show me the slowest transactions in the payments service this week" and the server converts that to valid NRQL, executes it, and returns results. This isn't just a prompt-engineering wrapper — it's a purpose-built translation pipeline. For teams where not everyone knows NRQL, this dramatically lowers the barrier to querying observability data through an agent.

**The best free tier in the observability MCP category.** New Relic offers [100GB/month of free data ingestion — permanently, no credit card required](https://newrelic.com/pricing), plus one full platform user with access to all 50+ capabilities and unlimited basic users. Compare this to Datadog (14-day trial, then pay-per-host/event), Sentry (10K events/month free), or Grafana Cloud (limited free tier). For smaller teams, side projects, or evaluating whether an observability MCP server is worth integrating, New Relic's free tier means you can actually use the MCP server without a procurement conversation.

**27 tools with genuine depth across the stack.** This isn't just NRQL queries. The tool set covers entity management, alerting, incident response (including deployment impact analysis and error groups from Errors Inbox), golden metrics analysis, synthetic monitors, dashboards, and log analysis. The `analyze_deployment_impact` tool is particularly valuable — it correlates deploy events with performance changes, answering "did this deploy make things worse?" without manual dashboard inspection.

**Remote-hosted with zero installation.** Like Datadog and Sentry, New Relic hosts the MCP server at `mcp.newrelic.com`. No local process, no Docker container, no version management. The server is always current.

**Tag-based tool filtering.** The [`include-tags` header system](https://docs.newrelic.com/docs/agentic-ai/mcp/overview/) lets you present subsets of tools to your agent. This is cleaner than Datadog's URL-parameter approach (no need to reconfigure the server URL) and more flexible than Grafana's CLI flags (can be set per-request, not per-session).

**RBAC-aware security.** The server [inherits your New Relic RBAC permissions](https://docs.newrelic.com/docs/agentic-ai/mcp/overview/). Agents can only access data, entities, and accounts that the corresponding user API key has been granted access to. No separate permission model needed for AI access.

**Golden metrics analysis is unique in the category.** The `analyze_golden_metrics` tool gives agents structured access to the four golden signals (throughput, response time, error rate, saturation) for any entity. This is the kind of high-level health check that most observability MCP servers force agents to derive from raw queries — New Relic surfaces it as a dedicated tool.

## What's Not

**Still in Public Preview.** Not GA like Datadog. New Relic [explicitly marks the MCP server as Public Preview](https://docs.newrelic.com/docs/agentic-ai/mcp/overview/) — meaning the API surface may change, SLA guarantees may not apply, and enterprise support may be limited. For production-critical agentic workflows, preview status introduces risk.

**No FedRAMP support; HIPAA status unclear.** New Relic's own docs state, verbatim: ["Due to security and compliance requirements, you must not use the New Relic AI MCP server if your accounts or data fall under FedRAMP compliance mandates. Use of this public preview feature with FedRAMP-regulated accounts is strictly prohibited."](https://docs.newrelic.com/docs/agentic-ai/mcp/overview/) (re-checked live 2026-08-21). Several third-party MCP directory sites also claim a HIPAA prohibition, but this reviewer could not find HIPAA-specific wording on any New Relic-owned page as of 2026-08-21 — treat the HIPAA claim as unconfirmed rather than repeating it as fact. Datadog's MCP server supports HIPAA-compliant environments. For FedRAMP-regulated accounts, New Relic's MCP server is a hard blocker regardless.

**API key authentication by default.** Most setups use a User API Key in the `Api-Key` header. These are user-scoped keys with broad access — if the key is exposed (e.g., in a committed config file), the attacker gets access to everything that user can see. [OAuth 2.0 is available](https://docs.newrelic.com/docs/agentic-ai/mcp/overview/) but isn't the primary setup path. Sentry's MCP server uses browser-based OAuth as the default, which is more secure.

**Minimal GitHub presence, and OAuth remains the recurring unresolved problem.** The [official repo](https://github.com/newrelic/mcp-server) has [7 stars, 0 forks, 2 commits from 1 contributor (nr-aks)](https://github.com/newrelic/mcp-server/graphs/contributors), and 4 open issues as of this 2026-08-21 audit. The repo itself contains only a README and a logo — the real server implementation is closed-source, hosted at `mcp.newrelic.com`, so a lack of repo commits doesn't necessarily mean the hosted service is frozen. New Relic staff did eventually engage on the tracker, weeks after issues were filed: on [Issue #3](https://github.com/newrelic/mcp-server/issues/3) (filed March 15, 2026 — JSON Schema validation error breaking Gemini 2.5 and OpenAI SDK strict-mode clients), nr-aks replied May 18, 2026 that "we've made some changes for this tool," but the issue remains open and it's unconfirmed whether the fix is complete. On [Issue #4](https://github.com/newrelic/mcp-server/issues/4) (filed April 8, 2026 — OAuth fails completely for accounts where New Relic itself enforces SSO), nr-aks asked for reproduction details May 18, 2026; a user supplied a detailed Cursor+JumpCloud repro on June 21, 2026, and **the issue is still open and unresolved as of 2026-08-21** — more than four months after it was filed. A feature request ([Issue #5](https://github.com/newrelic/mcp-server/issues/5), account-scoping via env var) was closed May 22, 2026 without the feature being built. Two more issues have opened since: [Issue #6](https://github.com/newrelic/mcp-server/issues/6) (May 20, 2026, self-hosted/Helm deployment request, open) and [Issue #7](https://github.com/newrelic/mcp-server/issues/7) (May 27, 2026) — a **second, distinct OAuth bug**, where the OAuth flow completes but never redirects back for custom connectors, also still open. Two separate open OAuth-related bugs, one of them enterprise-SSO-blocking for over four months, is the strongest signal against production readiness in this review. This mirrors Datadog's approach (hosted server, minimal repo), but it means you can't audit the code, file public bugs with any speed of resolution, or contribute. Grafana's open-source approach (2,500+ stars, 294 forks, 473 commits, Apache 2.0) is the opposite model.

**Complex platform pricing beyond the free tier.** The [free 100GB/month](https://newrelic.com/pricing) is generous for evaluation, but production workloads will exceed it. New Relic charges [$0.40/GB for standard data ingestion](https://newrelic.com/pricing) beyond the free limit ($0.60/GB for Data Plus with extended retention and compliance features). The pricing model is simpler than Datadog's per-host/per-event structure, but costs can still surprise at scale — especially with AI agents generating more queries than human users typically would.

**Permission errors can be opaque.** Users in custom groups without organization-level grants may see errors about "missing required capabilities." The troubleshooting path requires understanding New Relic's RBAC model, which isn't always intuitive. The error messages don't always point clearly to which specific permission is missing.

**Tool count trails Datadog and Grafana.** With 27 tools (verified live 2026-08-21; including Kafka, thread, GC, and performance-risk analysis tools not listed in the original announcement), New Relic is behind Datadog (50+ tools, 10+ toolsets) and Grafana (40+ tools, 15 categories). There are no tools for infrastructure monitoring, Kubernetes, or custom dashboard creation. The tool set is read-oriented — you can analyze and query, but not take action (no muting, no downtime scheduling, no alert acknowledgment through the official server).

**Multiple community alternatives suggest gaps.** At least 8 community-built New Relic MCP servers exist ([cloudbring/newrelic-mcp](https://github.com/cloudbring/newrelic-mcp) with 14 stars, 8 forks, 58 commits (verified live via GitHub API, 2026-08-21), and 19+ tools; [ulucaydin/mcp-server-newrelic](https://github.com/ulucaydin/mcp-server-newrelic); thrashy/mcp-newrelic; [ducduyn31/nr-mcp](https://github.com/ducduyn31/nr-mcp); [Ivlad003/mcp_newrelic](https://github.com/Ivlad003/mcp_newrelic); cvmoretti/new-relic-mcp; [xelber/newrelic-mcp](https://github.com/xelber/newrelic-mcp); [buallen/newrelic-mcp-server](https://github.com/buallen/newrelic-mcp-server); [piekstra/newrelic-mcp-server](https://github.com/piekstra/newrelic-mcp-server)). The community server from cloudbring adds deployment management, incident acknowledgment, browser monitor creation, and NerdGraph queries — capabilities the official server lacks.

## Alternatives

**[Datadog MCP Server](/reviews/datadog-mcp-server/)** (4/5) — the enterprise full-stack play. 50+ tools across 10+ modular toolsets covering surface area New Relic doesn't touch (LLM observability, feature flags, database monitoring, synthetics). GA status, agent-native tool design, token-budget pagination. But Datadog has no meaningful free tier and complex per-product pricing.

**[Grafana MCP Server](/reviews/grafana-mcp-server/)** (4/5) — the open-source alternative. 40+ tools, multi-vendor data source support, self-hostable, Apache 2.0. If you want vendor independence, code auditability, or run a LGTM stack. But requires running the server yourself, no hosted option.

**[Sentry MCP Server](/reviews/sentry-mcp-server/)** (4/5) — deep error tracking with Seer AI root cause analysis, OAuth-first security, zero-install remote hosting. Narrower (errors only) but deeper. Use Sentry for debugging specific errors, New Relic for full-stack observability.

**[cloudbring/newrelic-mcp](https://github.com/cloudbring/newrelic-mcp)** (14 stars, 58 commits, verified live 2026-08-21) — the most complete community alternative. 19+ tools including deployment management, incident acknowledgment, browser monitor creation, and NerdGraph queries. TypeScript, MIT, stdio transport. More actively developed than the official repo (58 commits vs 2). Useful if you need write operations or capabilities the official server doesn't cover.

**Honeycomb MCP** — event-based observability with high-cardinality debugging. A different approach — better for distributed system investigations where traditional APM metrics don't capture the problem.

## Who Should Use This

**Use the New Relic MCP server if:**
- You're already on New Relic and want your agent to query entities, alerts, logs, and metrics
- You want natural language to NRQL translation without learning query syntax
- You need an accessible free tier (100GB/month) to evaluate before committing
- You want zero-install remote hosting with Streamable HTTP transport
- You need golden metrics analysis as a first-class tool
- You use Atlassian tools — the [Rovo Ops integration is GA](https://community.atlassian.com/forums/Jira-Service-Management-articles/Announcing-GA-of-New-Relic-MCP-for-Rovo-Ops-Bring-observability/ba-p/3195727) and brings observability into JSM/Confluence
- You're on Azure — the Azure SRE Agent now has a native New Relic connector (April 2026)
- You use Amazon Quick — AWS enterprise AI assistant now integrates via MCP (May 2026)

**Skip it if:**
- You need GA status and enterprise SLA guarantees — Datadog is GA
- You're in a FedRAMP environment — explicitly prohibited by New Relic's own docs (HIPAA status is unconfirmed, not stated on any New Relic-owned page as of 2026-08-21)
- You need the broadest tool coverage — Datadog has 50+ tools with 10+ toolsets
- You want open-source code auditability or self-hosting — Grafana is the choice
- You need write operations (muting, downtime scheduling, alert acknowledgment) — the community server covers some of these

{{< verdict rating="3.5" summary="The most accessible full-stack observability MCP server on paper, held back by two still-open OAuth bugs that block SSO-enforced enterprise orgs" >}}
The New Relic MCP server is a strong entry in the observability category — [27 tools across 6 categories](https://docs.newrelic.com/docs/agentic-ai/mcp/tool-reference/) (verified live 2026-08-21) with genuinely useful natural language to NRQL translation, golden metrics analysis, deployment impact assessment, and remote hosting at mcp.newrelic.com. The [100GB/month free tier](https://newrelic.com/pricing) makes it the most accessible full-stack observability MCP server, lowering the barrier from "talk to procurement" to "just start using it." The broader New Relic ecosystem is expanding fast — the [Agentic Platform](https://www.businesswire.com/news/home/20260224168375/en/) (February 2026), [Rovo Ops GA integration](https://community.atlassian.com/forums/Jira-Service-Management-articles/Announcing-GA-of-New-Relic-MCP-for-Rovo-Ops-Bring-observability/ba-p/3195727), [Advance 2026 announcements](https://newrelic.com/blog/news/new-relic-advance-2026) (SRE Agent, Intelligent RCA, Performance Risks Inbox), a native Azure SRE Agent connector (April 2026), Amazon Quick integration (May 2026), and [New Relic Knowledge GA](https://www.businesswire.com/news/home/20260505650102/en/New-Relic-Unveils-Knowledge-Capability-to-Power-Agents-with-Real-Time-System-Understanding) (May 25, 2026) show serious and sustained investment in the agentic AI space, reinforced by being [named a Leader in the 2026 IDC MarketScape for AIOps](https://newrelic.com/blog/news/new-relic-named-a-leader-in-the-2026-idc-marketscape-for-worldwide-aiops) (March 2026). But the 3.5/5 rating — downgraded from 4/5 at original review — reflects a real, currently-unresolved problem: as of this 2026-08-21 audit, **two separate OAuth bugs remain open on the [official tracker](https://github.com/newrelic/mcp-server/issues)** — [Issue #4](https://github.com/newrelic/mcp-server/issues/4) (OAuth fails completely for SSO-enforced orgs, filed April 8, 2026, still open more than four months later) and [Issue #7](https://github.com/newrelic/mcp-server/issues/7) (OAuth completes but doesn't redirect back for custom connectors, filed May 27, 2026, still open). Combined with Public Preview status, a [FedRAMP prohibition](https://docs.newrelic.com/docs/agentic-ai/mcp/overview/), API key auth by default, a minimal closed-source repo (7 stars, 2 commits, 1 contributor), 27 tools trailing Datadog's 50+ and Grafana's 40+, a read-only orientation with no write operations, and 8+ community alternatives signaling gaps in the official offering, this is a server with real strengths that enterprise SSO users specifically cannot yet rely on. For teams already on New Relic without SSO-enforced auth — or evaluating which observability platform to wire into their agents — it remains the easiest on-ramp in the category; SSO-enforced orgs should wait for Issue #4 to close.
{{< /verdict >}}

**Category**: [Observability & Monitoring](/categories/observability-monitoring/)

*This review was researched and last updated on 2026-08-21, with a light freshness re-check on 2026-08-23, using Claude Sonnet 5 (Anthropic). We have not tested this server hands-on — our analysis is based on official documentation, the GitHub repository, community feedback, and public data sources including PulseMCP. Originally published March 2026; a second review that previously lived at `/reviews/new-relic-mcp-server/` was merged into this page 2026-08-21 (that URL now redirects here).*

