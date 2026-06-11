---
title: "Google Cloud MCP Servers — 50+ Servers, 22+ GA, MCP Toolbox v1.4, Gemini 3.5 Flash MCP Optimization, and ADK 2.0"
date: 2026-03-20T14:00:00+09:00
description: "Google Cloud ships 50+ managed remote MCP servers (22+ GA) plus open-source ones covering databases, compute, security, observability, AI/ML, Maps, and Workspace."
og_description: "Google Cloud MCP servers: 50+ managed remote endpoints (22+ GA), MCP Toolbox v1.4.0, ADK 2.0, Gemini 3.5 Flash MCP Atlas 83.6%, Google Workspace Developer Preview. Rating: 4.5/5."
content_type: "Review"
card_description: "Google Cloud's MCP ecosystem — 50+ managed remote servers (22+ GA), MCP Toolbox v1.4.0 (14.9K+ stars), ADK 2.0 multi-language agent framework, Gemini 3.5 Flash MCP Atlas 83.6%, WebMCP origin trial, Gemini CLI deprecated → Antigravity CLI."
last_refreshed: 2026-06-11
---

Google Cloud hasn't just shipped MCP servers — they've shipped managed MCP *endpoints*. While AWS built 68 servers in a monorepo that you run locally, Google took a different approach: remote MCP servers hosted on googleapis.com that your agent connects to directly. No local binaries, no Docker, no Node.js. Just an HTTP endpoint and your Google Cloud credentials.

The [google/mcp](https://github.com/google/mcp) repository (4,000 stars, 448 forks) is the hub, but the real story is the architecture. Google is betting that MCP servers belong in the cloud, not on your laptop. Part of our **[Cloud & Infrastructure MCP category](/categories/cloud-infrastructure/)**.

> **🔄 Refreshed 2026-06-11** — Google I/O 2026 (May 19) added major new pieces to this ecosystem. **ADK 2.0** launched with graph-based execution engine and multi-language support (Python, TypeScript, Go, Java, Kotlin). **Gemini 3.5 Flash** ships with native MCP optimization (MCP Atlas score 83.6%, $1.50/M input tokens). **WebMCP** entered Chrome 149 origin trial — Booking, Shopify, Instacart, Intuit committed. **MCP Toolbox** hit **v1.4.0** (June 4). **Managed Agents API** launched in preview — but MCP server support is *not yet available* in preview (notable gap). **Gemini CLI deprecated** → migrate to Antigravity 2.0 CLI by June 18. Workspace remains Developer Preview. Rating holds **4.5/5**.
>
> **Previous milestone (2026-05-02):** Cloud Next '26 (April 28) transformed this ecosystem. 18 managed servers → **50+ servers**. 2 GA → **22+ GA**. MCP Toolbox hit **v1.0.0**. Google Workspace MCP entered **Developer Preview**. google/mcp-security launched with **4 security servers**. Apigee MCP **GA**.

## What It Is

Google's MCP offering has three layers now:

**Layer 1: Managed Remote MCP Servers** — **50+ servers** hosted by Google, accessible via HTTP endpoints. At Cloud Next '26, Google graduated the majority from Preview to GA. You point your MCP client at a googleapis.com URL and authenticate with your Google Cloud credentials. The server runs on Google's infrastructure. Since March 17, 2026, MCP servers are **enabled by default** when you enable a supported product — no separate opt-in required.

**Layer 2: Open-Source MCP Servers** — 15+ servers you can run locally or deploy to Cloud Run, GKE, or anywhere else. These cover Firebase, developer tools, and more.

**Layer 3: Google Workspace MCP Servers** — NEW. Drive, Gmail, Calendar, Chat, and People API via Developer Preview. Separate from the Cloud managed servers.

### Managed Remote Servers — Google Cloud (22+ GA, 10+ Preview)

**Databases (7+ servers):**

| Server | Endpoint | Status |
|--------|----------|--------|
| BigQuery | `bigquery.googleapis.com/mcp` | **GA** |
| AlloyDB for PostgreSQL | `alloydb.REGION.rep.googleapis.com/mcp` | **GA** |
| Cloud SQL (MySQL/PostgreSQL/SQL Server) | `sqladmin.googleapis.com/mcp` | **GA** |
| Firestore | `firestore.googleapis.com/mcp` | **GA** |
| Spanner | `spanner.googleapis.com/mcp` | **GA** |
| Bigtable | `bigtable.googleapis.com/mcp` | **GA** |
| Memorystore (Redis, Redis Cluster, Valkey) | endpoint varies | **GA** |

**Infrastructure & Compute (4+ servers):**

| Server | Endpoint | Status |
|--------|----------|--------|
| Compute Engine (GCE) | `compute.googleapis.com/mcp` | **GA** |
| Kubernetes Engine (GKE) | `container.googleapis.com/mcp` | **GA** |
| Cloud Run | `run.googleapis.com/mcp` | **GA** |
| Resource Manager | `cloudresourcemanager.googleapis.com/mcp` | **GA** |

**Observability & Operations (5+ servers):**

| Server | Endpoint | Status |
|--------|----------|--------|
| Cloud Logging | `logging.googleapis.com/mcp` | **GA** |
| Cloud Monitoring | `monitoring.googleapis.com/mcp` | **GA** |
| Cloud Trace | `cloudtrace.googleapis.com/mcp` | **GA** |
| Error Reporting | `clouderrorreporting.googleapis.com/mcp` | **GA** |
| Security Operations (Chronicle) | `chronicle.REGION.rep.googleapis.com/mcp` | Preview |

**Data & Analytics (NEW servers):**

| Server | Endpoint | Status |
|--------|----------|--------|
| Database Center | endpoint varies | **GA** |
| Managed Service for Apache Spark | endpoint varies | **GA** |
| BigQuery Migration Service | endpoint varies | Preview |
| BigQuery Data Transfer Service | endpoint varies | Preview |
| Datastream | endpoint varies | Preview |
| Database Migration Service | endpoint varies | Preview |
| Knowledge Catalog | endpoint varies | Preview |
| Managed Service for Apache Airflow | endpoint varies | Preview |
| Oracle Database@Google Cloud | endpoint varies | Preview |

**AI & Platform (servers):**

| Server | Endpoint | Status |
|--------|----------|--------|
| Gemini Enterprise Agent Platform | endpoint varies | **GA** |
| Agent Search (Vertex AI Search) | `discoveryengine.googleapis.com/mcp` | **GA** |
| Pub/Sub | `pubsub.googleapis.com/mcp` | **GA** |
| Cloud Storage | `storage.googleapis.com/mcp` | **GA** |
| Agent Registry | endpoint varies | Preview |
| Gemini Cloud Assist | endpoint varies | Preview |
| App Lifecycle Manager | endpoint varies | Preview |
| Cloud Asset Inventory | endpoint varies | Preview |
| Cloud Product Registry | endpoint varies | Preview |

### Managed Remote Servers — Google Services

| Server | Status |
|--------|--------|
| Developer Knowledge API | **GA** |
| Maps Grounding Lite | **GA** |
| Android Management API | **GA** |
| Stitch (Beta) | **GA** |
| Design MCP | Preview |
| Maps Code Assist | Preview |
| Google Pay and Wallet | Preview |

### Google Workspace MCP Servers (Developer Preview — NEW)

| Server | Tools | Status |
|--------|-------|--------|
| Drive | 7 tools | Developer Preview |
| Gmail | 10 tools | Developer Preview |
| Calendar | 8 tools | Developer Preview |
| Chat | 2 tools | Developer Preview |
| People API | 3 tools | Developer Preview |

Access requires enrollment in the [Workspace Public Developer Preview Program](https://developers.google.com/workspace/preview). An official Workspace CLI is coming soon.

### Open-Source MCP Servers (15+ servers)

These run locally or deploy anywhere:

- **Firebase** — Full Firebase integration
- **Cloud Run** — Container deployment via MCP
- **Google Analytics** — Analytics data access
- **Genmedia** — Imagen and Veo model access (image/video generation)
- **gcloud CLI** — Full gcloud command access via MCP
- **Chrome DevTools** — Browser debugging integration
- **Flutter/Dart** — Mobile development tooling
- **Google Maps Platform Code Assist** — Maps API development
- **Go** — Go language support
- **~~Gemini CLI~~** — **⚠️ DEPRECATED** as of May 19, 2026. Migrate to **Antigravity 2.0 CLI** by June 18, 2026. Migration window closes June 18; Gemini CLI EOL after that date. Antigravity 2.0 replaces it as the primary Google AI developer CLI and includes MCP tooling integration.

### google/mcp-security — NEW Repository

The [google/mcp-security](https://github.com/google/mcp-security) repository launched with **4 security-focused MCP servers**, each installable via `uvx`:

- **Google Security Operations (Chronicle)** — threat detection, investigation, hunting
- **Security Operations SOAR** — security orchestration, automation, response (with per-integration enabling: CSV, OKTA, etc.)
- **Google Threat Intelligence (GTI)** — Google's threat intelligence data
- **Security Command Center (SCC)** — cloud security and risk management

### The Toolbox for Databases — v1.4.0

The [MCP Toolbox for Databases](https://github.com/googleapis/mcp-toolbox) (14,900+ stars, 1,500+ forks — renamed from genai-toolbox) is now at **v1.4.0** (released June 4, 2026), with active development since the v1.0.0 GA in April.

**Recent releases since v1.1.0:**
- **v1.4.0** (June 4) — latest stable release
- **v1.1.0** (April 13) — Vector assist tools for Cloud SQL Postgres. Knowledge Catalog integration. Looker flat-format YAML
- **v1.0.0** (April 10) — First stable release. MCP OAuth 2.1 authorization support. Skills (modular reusable task packages). Semantic search for BigQuery SQL tools. ES/QL for Elasticsearch. OpenTelemetry with official MCP semantic conventions

Now supports **15+ databases** beyond Google Cloud: PostgreSQL, MySQL, SQL Server, Oracle, MongoDB, Redis, Elasticsearch, CockroachDB, ClickHouse, Couchbase, Neo4j, Snowflake, and Trino.

### Apigee MCP — GA

Apigee MCP is now **Generally Available**. Turn your existing APIs into MCP tools using OpenAPI Specifications — create an MCP proxy with `/mcp` basepath, point it at `mcp.apigee.internal`, and include your OpenAPI spec. No local MCP servers or additional infrastructure needed. Works with the Agent Registry for discovery.

### ADK 2.0 — Launched May 19, 2026

The Agent Development Kit 2.0 launched at Google I/O 2026 with a significantly expanded scope:

- **Workflow Runtime** — graph-based execution engine replacing the linear flow model
- **Collaborative Multi-Agent Workflows** — coordinator agent delegates to typed subagents; structured handoffs
- **Multi-language** — now available in Python, TypeScript, Go, Java, and Kotlin (previously Python-first)
- **MCP native** — MCP server discovery and tool invocation baked into the framework

ADK 2.0 is Google's answer to the [Agent Orchestration MCP category](/categories/agent-orchestration/) — it's the opinionated framework for building agents that consume Google Cloud MCP servers. Pairs with the managed remote MCP endpoints for end-to-end Google-native agent stacks.

### Gemini 3.5 Flash — MCP-Optimized (May 19, 2026)

[Gemini 3.5 Flash](https://deepmind.google/models/gemini/flash/) shipped May 19, 2026, with explicit MCP optimization:

- **MCP Atlas score: 83.6%** — this benchmark measures scaled MCP tool-use reliability across multi-step workflows
- **4× faster output tokens** vs. Gemini 3.1 Flash
- **$1.50 per million input tokens** — roughly half the cost of comparable models
- Designed for high-frequency MCP tool calls in production agents

For teams using Google Cloud managed MCP servers, Gemini 3.5 Flash is now the recommended model for cost-sensitive production workloads. Gemini 3.5 Pro (expected June 2026) will target the performance-first tier.

### Google Managed Agents API — Preview (MCP Not Yet Supported)

The **Managed Agents API** launched in preview at Google I/O 2026 — fully provisioned Linux sandboxes delivered via a single API call, with Google-managed compute and Google Search built in.

**Important for MCP users:** MCP server integration is **not yet available** in the Managed Agents API preview. The preview excludes: `file_search`, `computer_use`, `google_maps`, `function_calling`, and `mcp_server`. This is a notable gap — Google's flagship new agent runtime does not yet support the MCP tool ecosystem it has invested heavily in. Watch for MCP support in a future preview update before building production workflows on this.

### WebMCP — Chrome 149 Origin Trial

**WebMCP** — Google's browser-side MCP standard for exposing web tools — entered the Chrome 149 origin trial. Key findings:

- **67% fewer errors** and **45% better task completion** vs. visual scraping approaches
- **Industry commitments:** Booking.com, Shopify, Instacart, and Intuit committed to implementation before GA
- Gemini in Chrome support "coming soon"
- W3C Community Group draft in progress; not yet on the Standards Track

WebMCP is distinct from server-side MCP: it lets web pages expose structured tools directly to browser-based AI agents without scraping.

## Setup

**For managed remote servers:**

Point your MCP client at the endpoint. Authentication uses Google Cloud Application Default Credentials (ADC) — the same auth you already use for `gcloud`. If you're already authenticated with Google Cloud, it just works. **As of March 17, 2026, MCP servers are enabled by default** — no separate enablement step required.

```json
{
  "mcpServers": {
    "bigquery": {
      "url": "https://bigquery.googleapis.com/mcp/sse",
      "headers": {
        "Authorization": "Bearer $(gcloud auth print-access-token)"
      }
    }
  }
}
```

You can use **IAM deny policies** to control MCP use (replacing the deprecated organization policy constraint from February 2026). Use **Cloud Trace** to monitor MCP tool use, failures, and latency.

**For Workspace MCP servers:** Enroll in the Developer Preview Program, then configure endpoints for Drive, Gmail, Calendar, Chat, and People API.

**For open-source servers:** Clone the repo, install dependencies, configure credentials. Setup varies by server — check individual READMEs.

**Setup difficulty: Medium** (lower than before). The managed servers are now easier — enabled by default, most are GA, and Cloud Trace provides built-in monitoring. The Workspace servers add a developer preview enrollment step.

## What Works Well

**The managed endpoint model is the right architecture.** Running MCP servers locally works for development, but for production agents that need to query databases, check monitoring, or manage infrastructure, the server should live next to the data. Google's approach eliminates the "install Node.js, run npx, hope it works" friction. Your agent talks to an HTTPS endpoint. Done.

**22+ servers are now GA — the Preview problem is largely solved.** The original review's biggest weakness was "16 of 18 servers are Preview." Cloud Next '26 fixed this. BigQuery, AlloyDB, Cloud SQL, Firestore, Spanner, Bigtable, Memorystore, Compute Engine, GKE, Cloud Run, Resource Manager, Cloud Logging, Cloud Monitoring, Cloud Trace, Error Reporting, Pub/Sub, Cloud Storage, Database Center, Apache Spark, Agent Search, and Gemini Enterprise Agent Platform are all GA with SLAs. The Preview concern that dominated the original review is no longer the main story.

**Database coverage is the deepest of any cloud provider.** Seven+ managed GA database servers covering relational (Cloud SQL, AlloyDB, Spanner), NoSQL (Firestore, Bigtable), analytics (BigQuery), caching (Memorystore with Redis/Valkey), plus the Toolbox at 14,900 stars supporting 15+ additional databases including Oracle, MongoDB, Redis, Elasticsearch, Snowflake, and Neo4j. No competitor matches this breadth.

**The Toolbox for Databases hit v1.0.0 — genuinely production-ready.** 14,900 stars, OAuth 2.1 authorization, Skills for reusable task packages, semantic search for BigQuery, OpenTelemetry with official MCP semantic conventions. The rename from genai-toolbox to mcp-toolbox signals full commitment to the MCP standard. Four releases in three weeks (v0.31.0 through v1.1.0) shows active development.

**Google Workspace MCP fills a massive gap.** Drive (7 tools), Gmail (10 tools), Calendar (8 tools), Chat (2 tools), and People API (3 tools) in Developer Preview. This brings Google's consumer/enterprise productivity suite into the MCP ecosystem — previously only available through community-built servers.

**Observability is now comprehensive.** Cloud Logging, Cloud Monitoring, Cloud Trace, and Error Reporting are all GA. Plus you can use Cloud Trace to *monitor MCP tool use itself* — troubleshoot agent-to-service calls, identify tool failures, and track latency. Meta-observability for your MCP infrastructure.

**Agent Registry enables dynamic discovery.** Agents can discover other agents, MCP servers, and tools at runtime via the Agent Registry. Combined with Apigee API Hub integration, your organization's APIs become discoverable MCP tools automatically.

**ADK 2.0 closes the orchestration gap.** Google now has a production-grade multi-agent framework (graph-based, multi-language, MCP-native) purpose-built to consume Google Cloud MCP servers. Combined with the managed endpoints, it's a coherent end-to-end stack: ADK 2.0 → Managed Agents (when MCP support arrives) → managed remote MCP servers → Google Cloud data.

**Gemini 3.5 Flash raises the MCP tool-use bar.** MCP Atlas 83.6% is a meaningful benchmark — it measures reliability across multi-step tool chains, not single tool calls. At $1.50/M input tokens and 4× faster output, Gemini 3.5 Flash is now a compelling default for production Google Cloud MCP workloads.

## What Doesn't Work Well

**No unified server — still 50+ separate endpoints.** AWS has a managed remote server (`mcp.global.api.aws`) that combines multiple services. Google has 50+ separate endpoints. If your agent needs BigQuery, GKE, and Cloud Logging, it's connecting to three different servers. This gap is more pronounced now at 50+ servers than it was at 18.

**Managed Agents API doesn't support MCP — yet.** Google's flagship new agent runtime (launched preview, May 19) explicitly excludes MCP server support. `mcp_server` is listed as unavailable in the preview. This creates a contradiction: Google has one of the largest MCP server ecosystems in the industry, but its primary new agent compute platform can't use them. Watch this closely — MCP support will likely arrive in a future preview update, but it's not there now.

**Gemini CLI is deprecated.** As of May 19, 2026, Gemini CLI is EOL — migrate to Antigravity 2.0 CLI by June 18, 2026. Any workflows built on Gemini CLI need migration. This affects the open-source side of the ecosystem.

**Google Cloud lock-in is real.** These servers are deeply integrated with Google Cloud's IAM, networking, and service architecture. If your infrastructure is on AWS or Azure, these servers offer you almost nothing. Even the open-source ones assume Google Cloud credentials and APIs. This is a Google Cloud tool for Google Cloud users.

**Workspace is still Developer Preview only.** The most broadly useful servers (Gmail, Drive, Calendar) require enrollment in a preview program and carry no SLA. Rollout began May 1 but no GA date has been announced. For production Workspace automation, the community-built [google_workspace_mcp](https://github.com/taylorwilsdon/google_workspace_mcp) may still be more practical.

**Documentation remains scattered.** The google/mcp repo is a directory of links, not a comprehensive guide. With 50+ servers across multiple categories, finding specific tool documentation requires navigating many different pages on cloud.google.com.

**The open-source servers lag behind managed ones.** The managed servers get Google's engineering attention. The open-source servers vary in maturity — some (like the gcloud CLI server) are explicitly "not an officially supported Google product." Quality is uneven.

## Compared to Alternatives

**vs. AWS MCP Servers:** AWS ships 66 local servers in a monorepo (8,900 stars); Google ships 50+ managed remote endpoints plus 15+ open-source. AWS's approach is "run everything locally." Google's is "connect to the cloud." AWS has broader service coverage. Google has more servers at GA and a better architecture for production. AWS deprecated 9 servers recently; Google graduated 20+ to GA. Different philosophies — pick the one that matches your cloud provider.

**vs. Azure MCP Servers:** Microsoft ships a [unified Azure MCP Server](/reviews/azure-mcp-servers/) covering 57 services through 276 tools (3,100 stars), now with self-hosted remote deployment via v2.0 GA. Azure goes wider with one filterable server; Google goes cloud-native with individual managed remote endpoints per service. Azure has broader unified tooling; Google has deeper database coverage and more GA servers. Azure hit a critical CVE (CVSS 9.1); Google's managed approach reduces attack surface.

**vs. Individual Database MCP Servers:** We've reviewed [Supabase](/reviews/supabase-mcp-server/), [Postgres](/reviews/postgres-mcp-server/), and others. For Google Cloud databases specifically, the managed MCP servers are the better choice — they handle auth, connection pooling, and network proximity. The Toolbox at v1.0.0 with 15+ database support now competes with individual servers even for non-Google databases.

## Who Should Use This

**Yes, use it if:**
- Your infrastructure runs on Google Cloud
- You want managed MCP endpoints with no local server installation — now 22+ GA with SLAs
- You need database access (BigQuery, Spanner, Cloud SQL, Firestore, AlloyDB, Bigtable, Memorystore)
- You're building agents for SRE/DevOps workflows on GCP (full observability stack is GA)
- You want the MCP Toolbox for cross-database scenarios (14.9K stars, v1.0.0 stable, 15+ databases)
- You need security operations via MCP (Chronicle, SOAR, GTI, SCC via google/mcp-security)

**Skip it if:**
- Your infrastructure isn't on Google Cloud — these servers won't help you
- You want a single unified server rather than 50+ separate endpoints
- You prefer local-first MCP servers you can run without cloud dependencies
- You need production Workspace integration (still Developer Preview only)

{{< verdict rating="4.5" summary="The cloud-native MCP architecture, now with ADK 2.0 and Gemini 3.5 Flash's 83.6% MCP Atlas score" >}}
Google I/O 2026 deepened Google Cloud's MCP lead in two meaningful ways: ADK 2.0 (graph-based, multi-language, MCP-native) gives teams an opinionated framework for consuming managed MCP endpoints, and Gemini 3.5 Flash's 83.6% MCP Atlas score makes multi-step tool chains more reliable at lower cost ($1.50/M input tokens). MCP Toolbox is now at v1.4.0. The weaknesses are real: no unified server (50+ separate endpoints), Workspace still in Developer Preview, and — most notably — the flagship Managed Agents API preview doesn't support MCP servers yet. Gemini CLI is also deprecated (migrate to Antigravity 2.0 by June 18). Despite these gaps, for Google Cloud infrastructure teams, this remains the most comprehensive and production-ready cloud MCP ecosystem available. Rating holds 4.5/5.
{{< /verdict >}}

*This review was researched and written on 2026-03-20, refreshed on 2026-05-02 and 2026-06-11 using Claude Sonnet 4.6 (Anthropic).*
