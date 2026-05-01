# Google Cloud MCP Servers — 50+ Servers, 22+ GA, MCP Toolbox v1.0, Workspace Preview, and the Cloud-Native MCP Play

> Google Cloud ships 50+ managed remote MCP servers (22+ GA) plus open-source ones covering databases, compute, security, observability, AI/ML, Maps, and Workspace.


Google Cloud hasn't just shipped MCP servers — they've shipped managed MCP *endpoints*. While AWS built 68 servers in a monorepo that you run locally, Google took a different approach: remote MCP servers hosted on googleapis.com that your agent connects to directly. No local binaries, no Docker, no Node.js. Just an HTTP endpoint and your Google Cloud credentials.

The [google/mcp](https://github.com/google/mcp) repository (4,000 stars, 448 forks) is the hub, but the real story is the architecture. Google is betting that MCP servers belong in the cloud, not on your laptop. Part of our **[Cloud & Infrastructure MCP category](/categories/cloud-infrastructure/)**.

> **🔄 Refreshed 2026-05-02** — Cloud Next '26 (April 28) transformed this ecosystem. 18 managed servers → **50+ servers**. 2 GA → **22+ GA**. MCP Toolbox hit **v1.0.0** (first stable release). Google Workspace MCP entered **Developer Preview**. google/mcp-security launched with **4 security servers**. Agent Registry enables **dynamic MCP discovery**. Apigee MCP is **GA**. MCP servers are now **enabled by default** — no manual opt-in required. Rating upgraded 4→**4.5/5**.

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

### google/mcp-security — NEW Repository

The [google/mcp-security](https://github.com/google/mcp-security) repository launched with **4 security-focused MCP servers**, each installable via `uvx`:

- **Google Security Operations (Chronicle)** — threat detection, investigation, hunting
- **Security Operations SOAR** — security orchestration, automation, response (with per-integration enabling: CSV, OKTA, etc.)
- **Google Threat Intelligence (GTI)** — Google's threat intelligence data
- **Security Command Center (SCC)** — cloud security and risk management

### The Toolbox for Databases — v1.0.0 GA

The [MCP Toolbox for Databases](https://github.com/googleapis/mcp-toolbox) (14,900 stars, 1,500 forks — renamed from genai-toolbox) hit its **first stable release v1.0.0** on April 10, 2026, followed by v1.1.0 on April 13.

**What's new since v0.30.0:**
- **v1.0.0** (April 10) — First stable release. MCP OAuth 2.1 authorization support. Skills (modular reusable task packages with autogeneration). Semantic search for BigQuery SQL tools. ES/QL query execution for Elasticsearch. MySQL table statistics. OpenTelemetry with official MCP semantic conventions
- **v1.1.0** (April 13) — Vector assist tools for Cloud SQL Postgres. Knowledge Catalog integration. Looker flat-format YAML
- **v0.32.0** (April 8) — MCP tool annotations on all tools. BigQuery conversational analytics. Looker agent management. Claude Code support in generated scripts. Skills via npx
- **v0.31.0** (March 26) — Generic authService for MCP. Protected Resource Metadata endpoint. Dataplex lookup context tool

Now supports **15+ databases** beyond Google Cloud: PostgreSQL, MySQL, SQL Server, Oracle, MongoDB, Redis, Elasticsearch, CockroachDB, ClickHouse, Couchbase, Neo4j, Snowflake, and Trino.

### Apigee MCP — GA

Apigee MCP is now **Generally Available**. Turn your existing APIs into MCP tools using OpenAPI Specifications — create an MCP proxy with `/mcp` basepath, point it at `mcp.apigee.internal`, and include your OpenAPI spec. No local MCP servers or additional infrastructure needed. Works with the Agent Registry for discovery.

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

## What Doesn't Work Well

**No unified server — still 50+ separate endpoints.** AWS has a managed remote server (`mcp.global.api.aws`) that combines multiple services. Google has 50+ separate endpoints. If your agent needs BigQuery, GKE, and Cloud Logging, it's connecting to three different servers. This gap is more pronounced now at 50+ servers than it was at 18.

**Google Cloud lock-in is real.** These servers are deeply integrated with Google Cloud's IAM, networking, and service architecture. If your infrastructure is on AWS or Azure, these servers offer you almost nothing. Even the open-source ones assume Google Cloud credentials and APIs. This is a Google Cloud tool for Google Cloud users.

**Workspace is Developer Preview only.** The most broadly useful servers (Gmail, Drive, Calendar) require enrollment in a preview program and carry no SLA. For production Workspace automation, the community-built [google_workspace_mcp](https://github.com/taylorwilsdon/google_workspace_mcp) may still be more practical.

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

{{< verdict rating="4.5" summary="The cloud-native MCP architecture, now production-ready for Google Cloud users" >}}
Cloud Next '26 transformed Google Cloud's MCP story from "promising but Preview" to "production-ready." 22+ servers graduated to GA (up from 2), the MCP Toolbox hit v1.0.0 with OAuth 2.1 and 15+ database support (14,900 stars), Google Workspace entered Developer Preview with 30 tools across Drive/Gmail/Calendar/Chat, and google/mcp-security launched 4 specialized security servers. The managed remote endpoint architecture remains the most sound approach to cloud MCP integration — and now it has the GA status to back it up. The main weaknesses remain: no unified server (50+ separate endpoints vs. Azure's single server), full GCP lock-in, and Workspace still in preview. But for Google Cloud teams, this is now the most comprehensive and production-ready cloud MCP ecosystem available. google/mcp: 4,000 stars (+18%), 448 forks (+23%).
{{< /verdict >}}

*This review was researched and written on 2026-03-20 and refreshed on 2026-05-02 using Claude Opus 4.6 (Anthropic).*

