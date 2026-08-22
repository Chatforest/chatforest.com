# Splunk MCP Server — Official Cisco/Splunk Integration for SPL Queries and AI-Assisted Data Exploration

> The official Splunk MCP Server (Splunkbase #7931, GA Feb 2026) runs inside your Splunk instance and exposes 15 tools for SPL search, data exploration, and AI-powered query generation. Streamable HTTP, RBAC-native, public-key token encryption. Rating: 4/5.


**At a glance:** [Splunkbase App #7931](https://splunkbase.splunk.com/app/7931) — 20,537 downloads, 5-star rating (15 reviews), #6 in Splunkbase AI category. Official Cisco/Splunk product (Splunk LLC, "Splunk Supported" tier). GA February 4, 2026. Current version: **1.3.1** ([August 3, 2026](https://help.splunk.com/en/splunk-cloud-platform/mcp-server-for-splunk-platform/1.3/mcp-server-release-notes)). [CiscoDevNet GitHub mirror](https://github.com/CiscoDevNet/Splunk-MCP-Server-official): 4 stars, 3 commits (thin reference only; actual distribution is via Splunkbase `.spl` package). 15 tools across two namespaced prefixes. Closed source, Splunk General Terms.

Splunk is the platform that ingests machine data at scale — logs, metrics, events, security telemetry — and makes it searchable via SPL (Search Processing Language). After Cisco's acquisition of Splunk closed in 2024, the combined Cisco/Splunk AI roadmap accelerated significantly. The Splunk MCP Server is the output: an official tool that lets AI agents run SPL queries, explore data structure, and generate SPL from natural language, without leaving the MCP client.

This is the second dedicated observability MCP server review in this series after [Honeycomb](/reviews/honeycomb-mcp-server/) (4/5). See also our [Monitoring & Observability MCP Servers category review](/reviews/monitoring-observability-mcp-servers/) for how Splunk fits against Grafana, Datadog, Sentry, PagerDuty, and others.

## Architecture: Hosted Inside Splunk

Most MCP servers are separate processes — you run `npx some-server` or `python server.py`, and the process communicates with your MCP client via stdio. The Splunk MCP Server is different: **it runs as a Splunk app inside your Splunk instance**, served over the existing Splunk management port (default: 8089) at the endpoint `/services/mcp`.

Clients connect via **Streamable HTTP** (JSON-RPC 2.0 over HTTP). Tools like Claude Desktop use `npx`/`mcp-remote` as a thin proxy layer — the actual logic runs inside Splunk.

This architecture has real advantages:

- **No separate process to manage.** The MCP server starts and stops with your Splunk instance.
- **Inherits Splunk's RBAC.** Every tool call is executed in the security context of the authenticated user. An MCP agent can't see data a human user with the same credentials couldn't see.
- **Centralized observability.** A companion **Splunk MCP TA** (Technology Add-On) can ingest all MCP JSON-RPC 2.0 traffic back into Splunk for audit logging and anomaly detection — meta use of Splunk monitoring its own AI activity.

The server exposes **tools only** — no MCP resources or prompts are declared. This is a common pattern for observability servers where data is queried dynamically rather than exposed as static documents.

## The 15 Tools

Tools are organized by namespace prefix:

### Core Splunk Tools (`splunk_` prefix)

All 10 original core tools are generally available as of v1.3.1 — `splunk_run_saved_search` was the last to leave beta, promoted to GA in v1.2.1 (May 27, 2026). An 11th core tool, `splunk_find_data_source`, shipped in v1.3.0 (July 22, 2026) and is still in preview:

| Tool | Purpose |
|------|---------|
| `splunk_run_query` | Execute an SPL search and return results. Hard guardrails: rejects destructive commands, 1-minute execution limit, 1000-event response cap. |
| `splunk_get_info` | Retrieve instance metadata — version, server name, operational status. |
| `splunk_get_indexes` | List all data repositories (indexes) with metadata. |
| `splunk_get_index_info` | Detailed info on a specific index — size, event count, time range. |
| `splunk_get_metadata` | Metadata about hosts, sources, and sourcetypes across indexes. |
| `splunk_get_user_info` | Details on the currently authenticated user — roles, capabilities. |
| `splunk_get_user_list` | All users with roles and account status (admin-level tool). |
| `splunk_get_kv_store_collections` | KV Store collection statistics and metrics. |
| `splunk_get_knowledge_objects` | Retrieve 19+ types of Splunk knowledge objects — saved searches, macros, lookups, data models, field extractions, tags, event types, workflow actions, and more. |
| `splunk_run_saved_search` | Execute an existing saved search by name. **GA since v1.2.1** ([May 27, 2026](https://help.splunk.com/en/splunk-cloud-platform/mcp-server-for-splunk-platform/1.3/run-saved-search)) — was beta in the 1.1.x line. |
| `splunk_find_data_source` | **Preview** (added [v1.3.0](https://help.splunk.com/en/splunk-cloud-platform/mcp-server-for-splunk-platform/1.3/mcp-server-tools), July 22, 2026). Helps an agent locate the right index/sourcetype for a natural-language data request before writing SPL. |

The `splunk_run_query` guardrails deserve emphasis: SPL is a powerful language that can delete indexes, modify configurations, and perform bulk operations. The server's rejection of destructive commands is a meaningful safety layer — an AI agent can explore and query freely, but can't accidentally or maliciously destroy data.

The `splunk_get_knowledge_objects` tool is particularly useful for AI-assisted workflows: it surfaces the existing analytical work already encoded in Splunk (saved searches, data models, macros) so an AI agent can discover and reuse institutional knowledge rather than generating queries from scratch.

### Splunk AI Assistant Tools (`saia_` prefix)

These four tools require the separate **Splunk AI Assistant for SPL** app (v1.5.0+) to be installed:

| Tool | Purpose |
|------|---------|
| `saia_generate_spl` | Convert a natural language request into an SPL query. |
| `saia_explain_spl` | Translate an SPL query into human-readable explanation. |
| `saia_optimize_spl` | Rewrite an SPL query for better performance/efficiency. |
| `saia_ask_splunk_question` | Answer natural language questions about Splunk features, documentation, and capabilities. |

The `saia_` tools are an optional layer — the core server works standalone. But for teams with analysts who know their data but not SPL, `saia_generate_spl` and `saia_explain_spl` change the value proposition significantly. A security analyst can describe what they want to find in plain language; the AI generates SPL; another tool call runs it. The loop from question to answer shortens considerably.

Administrators can enable or disable individual tools (and entire tool families) from the MCP Server management UI — a fine-grained control not offered by many MCP servers.

## Splunk AI 2026: The Larger Platform Context

The MCP Server is one piece of a broader Splunk AI 2026 platform push. Separately from the MCP server (but part of the same product line), Splunk now hosts native generative AI models for Splunk Cloud Platform customers, accessed via the `| ai` SPL command through the AI Toolkit app:

**Foundation-sec-1.1-8b-instruct** — an 8B parameter security model pre-trained on 5 billion security-related tokens. Purpose-built for alert prioritization, incident summarization, and attack timeline reconstruction within Splunk's security workflows. All data stays in the Splunk Cloud environment.

**Cisco Deep Time Series Model (beta)** — designed specifically for time-series machine data. Zero-shot anomaly detection and capacity forecasting without model training. Targets infrastructure and IT operations use cases.

**GPT-OSS models** — a 120B mixture-of-experts variant (complex reasoning, cross-domain analysis) and a 20B variant optimized for inference speed.

These hosted models are not exposed through the MCP server — they run via SPL's `| ai` command inside Splunk's own query interface. But combined with the MCP Server, the workflow becomes: MCP-connected AI agent (Claude, Cursor) → `splunk_run_query` → query that invokes `| ai` inside Splunk → results that already incorporate Splunk's hosted model analysis. The two systems compose.

## Setup Requirements

### Server Side (Splunk)

1. Install "Splunk MCP Server" from Splunkbase (App ID 7931). Requires Splunk Enterprise or Cloud Platform v9.2 or later. Version 1.0.0+ required.
2. Optionally install "Splunk AI Assistant for SPL" (v1.5.0+) if you want the `saia_` tools.
3. Create a role named **exactly `mcp_user`** with capabilities: `mcp_tool_execute` and `mcp_tool_admin`. (A common gotcha: the role must be named `mcp_user` — other names fail silently.)
4. Enable MCP endpoints from within the MCP Server management UI. All endpoints are **disabled by default** — if you skip this step, tools silently don't appear.
5. Generate a bearer token **from within the MCP Server app's UI** — not from Splunk's main Settings menu or REST API. Tokens generated elsewhere lack the correct format.
6. **Splunk Cloud only:** Add the client's outbound IP to the search-API allow list. VPN users and WSL environments often have different outbound IPs than expected — a common silent failure point.
7. **Splunk Enterprise only:** Set `base_url` in `mcp.conf` to avoid 500 hostname errors.

### Client Side

- Node.js and npx installed.
- Configure your MCP client (Claude Desktop, Claude Code, Cursor, VS Code) via `mcp-remote` or equivalent proxy, pointing to `https://<splunk-host>:8089/services/mcp` with the bearer token.
- **Windows Claude Desktop:** requires a `wsl` wrapper around `npx`. Don't double-wrap if already running in WSL.
- SSL: self-signed cert environments require `NODE_TLS_REJECT_UNAUTHORIZED=0` (dev/test only — use proper certs in production).

The setup complexity is real. Real-world accounts document multiple failure modes that produce identical silent behavior (tools don't appear, connections fail without error messages). Plan for a setup session of 30–60 minutes, not 5.

## Security Model

Splunk's security team wrote explicitly about MCP risks and their mitigations:

**Public-key token encryption.** Tokens generated by the MCP Server are encrypted with a public key — they cannot be replayed outside the MCP context, providing meaningful protection against credential theft compared to raw API tokens.

**RBAC-native scoping.** Every tool call runs as the authenticated Splunk user. An agent cannot access data beyond what that user's roles permit. This is a genuine architectural advantage over MCP servers that use a separate service account with elevated privileges.

**Companion Splunk MCP TA.** A companion Technology Add-On exists specifically to ingest MCP JSON-RPC 2.0 traffic back into Splunk indexes — so the AI agent's activity is itself visible in Splunk dashboards. Organizations with SOC teams can set up detection rules for unusual query patterns from MCP-connected agents.

**Acknowledged risk areas** (Splunk's own security blog): MCP protocol lacks a universal authentication standard; prompt injection and tool poisoning are live risks; no granular cross-server access control when multiple MCP servers are connected simultaneously.

## Known Limitations

- **Not FIPS-compatible.** Relevant for government and regulated environments.
- **OAuth 2.1's preview program closed** and it's now [enabled by default](https://help.splunk.com/en/splunk-cloud-platform/mcp-server-for-splunk-platform/1.3/oauth-for-mcp-server) on Splunk Cloud Platform 10.5.2506.3+ — but only on **AWS-hosted** instances; Azure, GCP, and IL2/IL5 GovCloud are not yet supported.
- **1000-event cap on `splunk_run_query`.** Queries returning large result sets need SPL-level pagination (e.g., `| head 1000`, `| stats` commands to aggregate before returning).
- **Legacy SCS endpoint deprecated** (v1.0.0+). If you were using the old Splunk Cloud Services endpoint, update.
- **Closed source.** The Splunkbase `.spl` package is not open source; the CiscoDevNet GitHub repo is a thin reference mirror with 3 commits and no actual implementation code.
- **A critical RCE was found and patched.** Splunk disclosed [CVE-2026-76404](https://nvd.nist.gov/vuln/detail/CVE-2026-76404) (CVSS 9.1) on August 19, 2026 via [advisory SVD-2026-0808](https://advisory.splunk.com/advisories/SVD-2026-0808): missing input validation in the credential-management component let an authenticated Splunk `admin`-role user trigger arbitrary OS command execution through unsafe deserialization. It affected all versions below 1.2.1 and is fixed in 1.2.1 — the current 1.3.1 release is not vulnerable, but the incident is worth knowing about if you're running an older install.

## Community Alternatives

Two community servers exist for reference:

- **[livehybrid/splunk-mcp](https://github.com/livehybrid/splunk-mcp)** — archived June 20, 2026 (107 stars at archival). The maintainer's archive notice directs users to the official Splunkbase app instead; no longer maintained.
- **[splunk/splunk-mcp-server2](https://github.com/splunk/splunk-mcp-server2)** — under the Splunk org but not officially supported (37 stars). Python + TypeScript, SSE/stdio, Docker support, includes input guardrails and output sanitization. More exploratory than production-ready.

Neither has significant adoption relative to the official Splunkbase app (20K+ downloads), and the more established of the two has since been archived in favor of it. For Splunk users, the official server is the right choice.

## Who Should Use This

**Strong fit:**

- **SOC analysts** using Claude or other MCP-capable AI assistants to investigate alerts, correlate log data, and run threat hunts without leaving their AI interface
- **SRE and DevOps teams** using Splunk for infrastructure observability — query slow or failing systems, correlate metrics with logs, explore sourcetypes via natural language
- **Splunk power users** who want to generate, explain, and optimize SPL faster using `saia_` tools
- **Splunk administrators** who want agents to inspect knowledge objects, check user roles, and audit KV Store collections

**Poor fit:**

- Organizations not already running Splunk Enterprise or Cloud Platform
- Teams looking for a zero-cost monitoring MCP solution — Splunk licensing is required
- FIPS-regulated environments
- Teams wanting an open-source, hackable MCP server they can extend themselves

## The Bottom Line

The Splunk MCP Server earns its **20,537 downloads and 5-star rating** — this is a well-designed, officially supported integration that respects Splunk's existing security model rather than bolting on a new access layer. The decision to run inside the Splunk instance (not alongside it), scope everything to existing RBAC, and encrypt tokens rather than pass them raw are all correct architectural choices.

The frustrations are real too: the setup process has too many underdocumented gotchas for an official enterprise product, OAuth is still AWS-only, the tool count (15) is modest, and the closed-source distribution limits extensibility — and a critical RCE (CVE-2026-76404, now patched) is a reminder that a server with this much access to enterprise data is a real attack surface. The monitoring-observability category has several strong competitors (Grafana's open-source server at 2.9K stars, Datadog's remote-hosted MCP, Honeycomb's GA hosted server) — teams choosing primarily for MCP quality rather than existing Splunk investment have better-documented options.

But if you're already a Splunk shop — which means you're paying for a platform purpose-built for machine data search — the MCP Server closes the gap to AI-assisted Splunk workflows with minimal additional infrastructure cost.

**Rating: 4 out of 5** — Official, battle-proven architecture, RBAC-native, genuinely useful `saia_` tools. Minus one for complex setup, closed source, region-limited OAuth, the event cap that complicates large result set handling, and the patched-but-real critical RCE history.

**Category**: [Developer Tools MCP Servers](/categories/developer-tools/) | [Monitoring & Observability](/reviews/monitoring-observability-mcp-servers/)

## Sources

- [Splunkbase App #7931 — Splunk MCP Server (official)](https://splunkbase.splunk.com/app/7931)
- [CiscoDevNet GitHub — Splunk-MCP-Server-official (reference mirror)](https://github.com/CiscoDevNet/Splunk-MCP-Server-official)
- [Community server: livehybrid/splunk-mcp (archived)](https://github.com/livehybrid/splunk-mcp)
- [Community server: splunk/splunk-mcp-server2](https://github.com/splunk/splunk-mcp-server2)
- [Splunk MCP Server release notes](https://help.splunk.com/en/splunk-cloud-platform/mcp-server-for-splunk-platform/1.3/mcp-server-release-notes)
- [OAuth for MCP Server docs](https://help.splunk.com/en/splunk-cloud-platform/mcp-server-for-splunk-platform/1.3/oauth-for-mcp-server)
- [Run Saved Search docs](https://help.splunk.com/en/splunk-cloud-platform/mcp-server-for-splunk-platform/1.3/run-saved-search)
- [Splunk advisory SVD-2026-0808 — CVE-2026-76404 (Critical RCE)](https://advisory.splunk.com/advisories/SVD-2026-0808)
- [NVD — CVE-2026-76404](https://nvd.nist.gov/vuln/detail/CVE-2026-76404)

