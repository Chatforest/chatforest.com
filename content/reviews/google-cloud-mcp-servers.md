---
title: "Google Cloud MCP Servers — 30+ Servers, Managed Endpoints, and the Cloud-Native MCP Play"
date: 2026-03-20T14:00:00+09:00
description: "Google Cloud ships 18 managed remote MCP servers and 15+ open-source ones covering databases, compute, security, observability, AI/ML, and Maps. 3,400 stars, all accessible via googleapis.com endpoints. The most cloud-native MCP architecture in the ecosystem."
og_description: "Google Cloud MCP servers: 18 managed remote endpoints, 15+ open-source servers. BigQuery, Spanner, GKE, Vertex AI, Maps, and more. Rating: 4/5."
content_type: "Review"
card_description: "Google Cloud's MCP ecosystem — 18 managed remote servers plus 15+ open-source ones. BigQuery, Spanner, GKE, Vertex AI, Security Operations, Maps, and the 13.5K-star MCP Toolbox for Databases."
---

Google Cloud hasn't just shipped MCP servers — they've shipped managed MCP *endpoints*. While AWS built 66 servers in a monorepo that you run locally, Google took a different approach: remote MCP servers hosted on googleapis.com that your agent connects to directly. No local binaries, no Docker, no Node.js. Just an HTTP endpoint and your Google Cloud credentials.

The [google/mcp](https://github.com/google/mcp) repository (3,400 stars, 364 forks) is the hub, but the real story is the architecture. Google is betting that MCP servers belong in the cloud, not on your laptop.

## What It Is

Google's MCP offering has two layers:

**Layer 1: Managed Remote MCP Servers** — 18 servers hosted by Google, accessible via HTTP endpoints. These are the headline feature. You point your MCP client at a googleapis.com URL and authenticate with your Google Cloud credentials. The server runs on Google's infrastructure.

**Layer 2: Open-Source MCP Servers** — 15+ servers you can run locally or deploy to Cloud Run, GKE, or anywhere else. These cover Google Workspace, Firebase, and developer tools.

### Managed Remote Servers (18 servers, all Preview except 2 GA)

**Databases (7 servers):**

| Server | Endpoint | Status |
|--------|----------|--------|
| BigQuery | `bigquery.googleapis.com/mcp` | Preview |
| AlloyDB for PostgreSQL | `alloydb.REGION.rep.googleapis.com/mcp` | Preview |
| Cloud SQL (MySQL) | `sqladmin.googleapis.com/mcp` | Preview |
| Cloud SQL (PostgreSQL) | `sqladmin.googleapis.com/mcp` | Preview |
| Cloud SQL (SQL Server) | `sqladmin.googleapis.com/mcp` | Preview |
| Firestore | `firestore.googleapis.com/mcp` | Preview |
| Spanner | `spanner.googleapis.com/mcp` | Preview |

**Infrastructure & Compute (4 servers):**

| Server | Endpoint | Status |
|--------|----------|--------|
| Compute Engine (GCE) | `compute.googleapis.com/mcp` | Preview |
| Kubernetes Engine (GKE) | `container.googleapis.com/mcp` | Preview |
| Cloud Run | `run.googleapis.com/mcp` | Preview |
| Resource Manager | `cloudresourcemanager.googleapis.com/mcp` | Preview |

**Observability & Security (4 servers):**

| Server | Endpoint | Status |
|--------|----------|--------|
| Cloud Logging | `logging.googleapis.com/mcp` | Preview |
| Cloud Monitoring | `monitoring.googleapis.com/mcp` | Preview |
| Security Operations (Chronicle) | `chronicle.REGION.rep.googleapis.com/mcp` | Preview |
| CX Agent Studio | `ces.us.rep.googleapis.com/mcp` | Preview |

**AI, Messaging & Maps (5 servers):**

| Server | Endpoint | Status |
|--------|----------|--------|
| Vertex AI | `aiplatform.googleapis.com/mcp` | Preview |
| Vertex AI Search | `discoveryengine.googleapis.com/mcp` | Preview |
| Pub/Sub | `pubsub.googleapis.com/mcp` | Preview |
| Managed Kafka | `managedkafka.REGION.rep.googleapis.com/mcp` | Preview |
| Developer Knowledge API | `developerknowledge.googleapis.com/mcp` | **GA** |
| Maps Grounding Lite | `mapstools.googleapis.com/mcp` | **GA** |

### Open-Source MCP Servers (15+ servers)

These run locally or deploy anywhere:

- **Google Workspace** — Docs, Sheets, Slides, Calendar, Gmail
- **Firebase** — Full Firebase integration
- **Cloud Run** — Container deployment via MCP
- **Google Analytics** — Analytics data access
- **Google Cloud Storage** — Object storage operations
- **Genmedia** — Imagen and Veo model access (image/video generation)
- **Google Cloud Security** — Security Command Center, Chronicle
- **gcloud CLI** — Full gcloud command access via MCP
- **Google Cloud Observability** — Monitoring and logging
- **Chrome DevTools** — Browser debugging integration
- **Flutter/Dart** — Mobile development tooling
- **Google Maps Platform Code Assist** — Maps API development
- **Go** — Go language support

### The Toolbox for Databases

Separate from the managed servers, the [MCP Toolbox for Databases](https://github.com/googleapis/genai-toolbox) (13,500 stars, 1,300 forks) deserves its own mention. It's an open-source MCP server that supports BigQuery, AlloyDB, Cloud SQL (MySQL, PostgreSQL, SQL Server), Spanner, Firestore, and self-managed databases. Key features: connection pooling, built-in OpenTelemetry tracing, dynamic tool reloading, and integration in under 10 lines of code. At v0.30.0, it predates the MCP standard but has been retrofitted for compatibility.

## Setup

**For managed remote servers:**

Point your MCP client at the endpoint. Authentication uses Google Cloud Application Default Credentials (ADC) — the same auth you already use for `gcloud`. If you're already authenticated with Google Cloud, it just works.

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

**For open-source servers:**

Clone the repo, install dependencies, configure credentials. Setup varies by server — check individual READMEs.

**Setup difficulty: Medium.** If you're already on Google Cloud, the managed servers are easy — no local installation needed. If you're not on Google Cloud, the learning curve is steeper than AWS's "run it locally" approach.

## What Works Well

**The managed endpoint model is the right architecture.** Running MCP servers locally works for development, but for production agents that need to query databases, check monitoring, or manage infrastructure, the server should live next to the data. Google's approach eliminates the "install Node.js, run npx, hope it works" friction. Your agent talks to an HTTPS endpoint. Done.

**Database coverage is comprehensive.** Seven managed database servers covering relational (Cloud SQL, AlloyDB, Spanner), NoSQL (Firestore, Bigtable), and analytics (BigQuery). Plus the Toolbox at 13,500 stars handling cross-database scenarios. If your data lives in Google Cloud, there's an MCP path to it.

**The Toolbox for Databases is battle-tested.** 13,500 stars and v0.30.0 — this project has been running in production longer than most MCP servers have existed. Connection pooling, OpenTelemetry tracing, and multi-framework support (Python, TypeScript, Go) make it genuinely production-ready.

**Observability servers fill a real gap.** Cloud Logging and Cloud Monitoring via MCP means agents can investigate incidents, check metrics, and correlate logs without you building custom integrations. For SRE workflows, this is a significant capability.

**Two servers are already GA.** Developer Knowledge API and Maps Grounding Lite have graduated to general availability, which means SLA-backed production use. Everything else is Preview, but the path to GA is visible.

## What Doesn't Work Well

**Almost everything is still Preview.** 18 managed servers, 16 in Preview. "Preview" in Google Cloud means no SLA, potential breaking changes, and features that might be removed. Building production workflows on Preview services is risky. Google's track record of shutting down products doesn't help the confidence story.

**No unified server.** AWS has a managed remote server (`mcp.global.api.aws`) that combines multiple services. Google has 18 separate endpoints. If your agent needs to query BigQuery, check GKE pods, and read Cloud Logging, it's connecting to three different servers. Configuration complexity scales linearly with the number of services you use.

**Google Cloud lock-in is real.** These servers are deeply integrated with Google Cloud's IAM, networking, and service architecture. If your infrastructure is on AWS or Azure, these servers offer you almost nothing. Even the open-source ones assume Google Cloud credentials and APIs. This is a Google Cloud tool for Google Cloud users.

**Documentation is scattered.** The google/mcp repo is a directory of links, not a comprehensive guide. Each server has its own documentation on cloud.google.com, with varying levels of detail. Finding "what tools does the BigQuery MCP server expose?" requires navigating multiple pages.

**The open-source servers lag behind managed ones.** The managed servers get Google's engineering attention. The open-source servers vary in maturity — some (like the gcloud CLI server) are explicitly "not an officially supported Google product." Quality is uneven.

## Compared to Alternatives

**vs. AWS MCP Servers:** AWS ships 66 local servers in a monorepo (8,500 stars); Google ships 18 managed remote endpoints plus 15+ open-source. AWS's approach is "run everything locally." Google's is "connect to the cloud." AWS has broader service coverage today. Google has a better architecture for production. Different philosophies, both valid — pick the one that matches your cloud provider.

**vs. Azure MCP Servers:** Microsoft has individual MCP servers for Azure services but no unified ecosystem comparable to Google's or AWS's. If you're on Azure, you're assembling individual pieces rather than getting an integrated suite.

**vs. Individual Database MCP Servers:** We've reviewed [Supabase](/reviews/supabase-mcp-server/), [Postgres](/reviews/postgres-mcp-server/), and others. For Google Cloud databases specifically, the managed MCP servers are the better choice — they handle auth, connection pooling, and network proximity. For non-Google databases, individual servers remain the way to go.

## Who Should Use This

**Yes, use it if:**
- Your infrastructure runs on Google Cloud
- You want managed MCP endpoints with no local server installation
- You need database access (BigQuery, Spanner, Cloud SQL, Firestore, AlloyDB)
- You're building agents for SRE/DevOps workflows on GCP
- You want the MCP Toolbox for cross-database scenarios (13.5K stars, production-proven)

**Skip it if:**
- Your infrastructure isn't on Google Cloud — these servers won't help you
- You need GA/production-grade SLAs (most servers are still Preview)
- You want a single unified server rather than 18 separate endpoints
- You prefer local-first MCP servers you can run without cloud dependencies

{{< verdict rating="4" summary="The cloud-native MCP architecture, for Google Cloud users" >}}
Google Cloud's MCP ecosystem represents the most architecturally sound approach to cloud MCP integration: managed remote endpoints that live next to your data, backed by Google's infrastructure. The database coverage is especially strong, with the 13,500-star MCP Toolbox adding a battle-tested layer. But 16 of 18 managed servers are still Preview, the documentation is fragmented, and this is useful only if you're on Google Cloud. AWS currently offers broader coverage with 66 servers to Google's 30+. For Google Cloud teams, though, these managed endpoints eliminate the operational overhead of running MCP servers locally — and that's the right direction for production deployments.
{{< /verdict >}}

*This review was researched and written on 2026-03-20 using Claude Opus 4.6 (Anthropic).*
