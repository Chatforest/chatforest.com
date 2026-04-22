# AWS vs Google Cloud vs Azure — Cloud Provider MCP Servers Compared (2026)

> AWS ships 54 local servers plus a managed preview, Google Cloud ships 46 managed remote endpoints (most now GA), and Azure hits 2.0 with 276 tools across 57 services.


The three major cloud providers have all shipped MCP servers. Each took a fundamentally different approach — and a month later, each has evolved dramatically.

AWS trimmed from 68 to 54 servers (deprecating redundant ones) while pushing its managed remote endpoint as the primary entry point. Google Cloud exploded from 18 to 46 managed endpoints, with most reaching GA. Microsoft shipped Azure MCP Server 2.0 with remote hosting support and expanded to 276 tools across 57 services. The convergence toward remote, production-grade MCP is accelerating.

We've reviewed all three: [AWS MCP Servers](/reviews/aws-mcp-servers/) (4/5), [Google Cloud MCP Servers](/reviews/google-cloud-mcp-servers/) (4.5/5), and [Azure MCP Servers](/reviews/azure-mcp-servers/) (4/5). Here's how they compare head-to-head.

## At a Glance

| | AWS | Google Cloud | Azure |
|---|---|---|---|
| **Architecture** | 54 local servers + managed remote preview | 46 managed remote endpoints (most GA) + open-source CLI servers | 1 unified server (57 services, 276 tools) + specialized servers |
| **GitHub** | [awslabs/mcp](https://github.com/awslabs/mcp) | [googleapis/gcloud-mcp](https://github.com/googleapis/gcloud-mcp) | [microsoft/mcp](https://github.com/microsoft/mcp) |
| **Stars** | 8,800 | 745 (gcloud-mcp) + 14,800 (Toolbox) | 3,000 |
| **Transport** | stdio (local) + streamable HTTP (preview) | HTTP (managed, auto-enabled) + stdio (open-source) | stdio (local) + HTTP (remote, new in 2.0) |
| **Auth** | AWS credentials (IAM) | Google Cloud ADC + IAM deny policies | Entra ID + RBAC + managed identity + OBO flow |
| **Language** | Python (primary) | Go, Python, TypeScript | C# / .NET (primary) |
| **License** | Apache 2.0 | Apache 2.0 | MIT |
| **Rating** | 4/5 | 4.5/5 | 4/5 |

Google Cloud pulls ahead with the fastest expansion and the most production-ready managed architecture. AWS remains the deepest per-service. Azure 2.0 closes the remote hosting gap.

## Three Architectures, Three Trade-offs

### AWS: The Server-Per-Service Model (Consolidating)

AWS built a server for everything — and has now started trimming. The April 2026 cleanup deprecated 12 servers (including CloudWatch AppSignals, Nova Canvas, Bedrock Data Automation, and the MSK server), bringing the count from 68 to 54. The Core MCP Server that previously orchestrated multi-server setups is also deprecated — modern MCP clients handle multi-server configs natively. The new recommended entry point is the AWS MCP Server (managed preview) at `mcp.global.api.aws`.

**Strengths:**
- Deepest per-service coverage — 54 purpose-built servers spanning databases, AI/ML, observability, IoT, and healthcare
- 8,800 stars with weekly releases — the most active community
- The managed AWS MCP Server (preview) provides CloudTrail audit logging and syntactically validated API calls
- New specialized servers: AgentCore (intelligent agents), LZA (Landing Zone Accelerator, 20 tools), HealthOmics/HealthImaging/HealthLake

**Trade-offs:**
- Configuration complexity scales with services — using 10 AWS services means configuring 10 servers
- Local-first architecture requires Python runtime on the agent's machine
- Managed remote endpoint is still preview — no GA date announced
- Security patching cadence is aggressive (IAM privilege escalation fix, path traversal prevention, JWS header injection fix — all in March/April 2026)

### Google Cloud: The Managed Endpoint Model (Now Dominant)

Google's bet on managed remote endpoints has paid off massively. From 18 endpoints in March, Google Cloud now offers **46 managed MCP servers** — with the majority reaching GA status. Since March 17, 2026, MCP endpoints are auto-enabled when you enable a supported product, removing the separate enablement step. The ecosystem now spans databases (AlloyDB, Spanner, Cloud SQL, Firestore, Bigtable all GA), compute (Cloud Run, GKE, Compute Engine all GA), observability (Logging, Monitoring, Trace all GA), security (Google Security Operations GA), and new domains like Pub/Sub, Resource Manager, and the Developer Knowledge API.

**Strengths:**
- 46 managed endpoints — the broadest managed MCP coverage by any cloud provider
- Most servers now GA with SLA, up from mostly Preview in March
- Auto-enablement — no separate MCP setup step needed
- The 14,800-star MCP Toolbox for Databases hit v1.1.0 (from v0.30 — a major maturity milestone)
- Cloud Trace integration for MCP observability — debug tool failures and latency directly
- IAM deny policies for MCP governance (replacing deprecated org policy constraints)
- Open-source gcloud-mcp (745 stars) provides CLI-based access alongside managed endpoints

**Trade-offs:**
- 46 separate endpoints still means 46 separate configurations
- Some newer servers (Agent Registry, Knowledge Catalog, Design MCP) are still Preview
- Documentation quality varies across the expanded surface area

### Azure: The Unified Server Model (Now Remote-Ready)

Microsoft shipped Azure MCP Server 2.0 stable on April 10, 2026 — the biggest update since launch. The single binary now covers **57 services with 276 tools** (up from 47+ services). The headline feature: remote hosting support. Teams can deploy Azure MCP as a centrally managed service with HTTP transport, managed identity authentication, and On-Behalf-Of (OBO) delegation flows. Sovereign cloud support (US Government, 21Vianet) makes this the first cloud MCP server ready for regulated deployments.

**Strengths:**
- One server, one install, 276 tools across 57 services — minimal configuration overhead
- **Remote hosting** (new in 2.0) — deploy as a centralized managed service, not just local stdio
- Sovereign cloud support (Azure US Gov, 21Vianet) — first cloud MCP for regulated environments
- Built into Visual Studio 2026 GA + VS Code, IntelliJ, Eclipse, Cursor extensions
- Tool annotations (destructive/readOnly/secret) enable smart safety checks
- Azure DevOps MCP Server adds WIQL query tool and PAT authentication; remote MCP now in public preview
- Security hardening: endpoint validation, injection pattern protections, isolation controls

**Trade-offs:**
- Some services still shallow (list-only, no deep management)
- Repo moved from Azure/azure-mcp (archived) to microsoft/mcp — links and docs may lag
- The broader Microsoft stack (DevOps, Fabric, M365) is still separate servers
- 3,000 stars — growing but still smallest community

## Service Coverage Comparison

### Databases

| Database Type | AWS | Google Cloud | Azure |
|---|---|---|---|
| **Relational (PostgreSQL)** | Aurora PostgreSQL, DSQL servers | Cloud SQL, AlloyDB (managed, GA) | PostgreSQL namespace |
| **Relational (MySQL)** | Aurora MySQL server | Cloud SQL MySQL (managed, GA) | MySQL namespace |
| **NoSQL (Document)** | DynamoDB, DocumentDB servers | Firestore (managed, GA) | Cosmos DB namespace |
| **Analytics** | Redshift, Data Processing servers | BigQuery (managed, GA) | Data Explorer (Kusto) |
| **In-Memory** | ElastiCache, Valkey, Memcached servers | Memorystore (managed, GA) | Redis namespace |
| **Wide-column** | — | Bigtable (managed, GA) | — |
| **Graph** | Neptune server | — | — |
| **Time-series** | Timestream for InfluxDB server | — | — |
| **Cassandra-compat** | Keyspaces server | — | — |
| **Oracle** | — | Oracle Database@Google Cloud (Preview) | — |
| **Multi-database tool** | — | Toolbox v1.1 (14.8K stars) | — |

**Winner: AWS for breadth (9 database servers), Google Cloud for managed access (7 GA database endpoints + Toolbox v1.1)**

### Compute & Containers

| Service Type | AWS | Google Cloud | Azure |
|---|---|---|---|
| **Containers** | ECS, EKS servers | GKE (managed, GA), Cloud Run (GA) | AKS namespace |
| **Serverless** | Lambda, Serverless servers | Cloud Run (GA) | Functions namespace |
| **VMs** | — | Compute Engine (managed, GA) | VMs namespace |
| **IaC** | Serverless (SAM CLI) server | — | Bicep namespace |

**Winner: Google Cloud** — GKE and Cloud Run both GA with managed access, plus Compute Engine

### AI & Machine Learning

| Service Type | AWS | Google Cloud | Azure |
|---|---|---|---|
| **Model hosting** | Bedrock, SageMaker, AgentCore servers | Gemini Enterprise Agent Platform (GA) | Foundry namespace |
| **Search** | Kendra, Q Business, Q Index servers | Agent Search (GA) | AI Search namespace |
| **Agents** | Bedrock AgentCore (new) | Agent Registry (Preview) | — |
| **Media gen** | — | Design MCP (Preview) | — |

**Winner: AWS** — AgentCore + Q Business + SageMaker give deepest AI/ML tooling

### Observability & Security

| Service Type | AWS | Google Cloud | Azure |
|---|---|---|---|
| **Logging** | CloudWatch server | Cloud Logging (managed, GA) | Monitor namespace |
| **Metrics** | CloudWatch server | Cloud Monitoring (managed, GA) | App Insights namespace |
| **Tracing** | CloudTrail server | Cloud Trace (managed, GA) | — |
| **Error tracking** | — | Error Reporting (GA) | — |
| **Security** | IAM, Well-Architected Security servers | Google Security Operations (GA) | Key Vault, RBAC namespaces |
| **Cost** | Billing, Pricing servers | — | Pricing namespace |
| **Asset inventory** | — | Cloud Asset Inventory (Preview) | — |

**Winner: Google Cloud** — full observability stack (Logging + Monitoring + Trace + Error Reporting) all GA with managed access

### DevOps & CI/CD

| Service Type | AWS | Google Cloud | Azure |
|---|---|---|---|
| **CI/CD** | Step Functions server | — | Azure DevOps (remote preview, WIQL queries, PAT auth) |
| **IaC** | Serverless (SAM) server | — | Bicep, Deploy namespaces |
| **Messaging** | SNS/SQS, MQ servers | Pub/Sub (managed, GA), Kafka (GA) | — |
| **Data pipelines** | Data Processing (Glue/EMR/Athena) | Datastream (Preview), Spark (GA), Airflow (Preview) | — |

**Winner: Google Cloud for managed messaging/pipelines, Azure DevOps for CI/CD platform**

## Setup Complexity

**Easiest to start:** Google Cloud (managed endpoints auto-enabled when you enable a product — just point your client at a URL)

**Easiest to scale:** Azure (one server handles 57 services with 276 tools — add namespaces, not servers)

**Most configuration needed:** AWS (each service is a separate server to install and configure, though the managed preview simplifies this)

### Quick Setup Comparison

**AWS** — the managed preview (recommended) or per-server install:
```json
{
  "mcpServers": {
    "aws": {
      "url": "https://mcp.global.api.aws",
      "headers": {
        "Authorization": "Bearer <aws-credentials>"
      }
    }
  }
}
```

**Google Cloud** — connect to managed endpoint (auto-enabled since March 2026):
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

**Azure** — one install, enable namespaces (now supports remote deployment too):
```json
{
  "mcpServers": {
    "azure": {
      "command": "npx",
      "args": ["-y", "@azure/mcp@latest", "server", "start"]
    }
  }
}
```

## Which One Should You Use?

This is straightforward: **use the MCP servers for the cloud you're already on.**

Cloud MCP servers are deeply integrated with their provider's authentication, APIs, and service architecture. They're not portable — an AWS MCP server is useless if your infrastructure runs on Google Cloud.

### Use AWS MCP Servers if:
- Your infrastructure runs on AWS
- You need deep per-service tooling (54 specialized servers covering databases, AI/ML, healthcare, IoT)
- You want the largest and most active community (8,800 stars, weekly releases)
- You need specialized domains like HealthOmics, IoT SiteWise, or Landing Zone management
- You're comfortable managing multiple servers per project

### Use Google Cloud MCP Servers if:
- Your infrastructure runs on Google Cloud
- You want production-ready managed remote endpoints (46 servers, most GA)
- You need zero-install setup — auto-enabled since March 2026
- You need the MCP Toolbox for Databases (14.8K stars, v1.1.0, production-proven)
- You're building production agents that shouldn't run servers locally
- You need full observability (Logging + Monitoring + Trace + Error Reporting all GA)

### Use Azure MCP Servers if:
- Your infrastructure runs on Azure
- You want one unified server covering 57 services with 276 tools
- You need remote hosting for centralized team deployment (new in 2.0)
- You're in a regulated environment (sovereign cloud support for US Gov, 21Vianet)
- You're in the Microsoft ecosystem (VS 2026, .NET, Entra ID, GitHub Copilot CLI)
- You need enterprise security (tool annotations, injection protections, isolation controls)

### Multi-Cloud?

If you run infrastructure across multiple clouds, you'll need MCP servers from each provider. The good news: they can coexist in your MCP client configuration. The bad news: there's no unified multi-cloud MCP server yet.

For multi-cloud database access specifically, consider [Google's MCP Toolbox for Databases](https://github.com/googleapis/genai-toolbox) — despite the Google branding, it supports self-managed databases alongside Google Cloud ones. At v1.1.0 with 14,800 stars, it's the most mature multi-database MCP tool available.

## The Architecture Question

The most interesting difference isn't feature coverage — it's the transport model. And the answer is becoming clearer.

**Local servers** (AWS's open-source approach) run on your machine. They're fast for development, work offline, and give you full control. But they require runtime dependencies, updates, and don't scale to production agent architectures.

**Managed remote servers** (Google Cloud's approach, AWS's managed preview) run in the cloud. They eliminate local dependencies, live next to the data, and scale naturally. Google proved this model works — going from 18 to 46 endpoints while moving most to GA.

**Self-hosted remote** (Azure 2.0's new approach) lets teams deploy the MCP server as a centralized internal service. This splits the difference — you control the deployment, but agents connect remotely.

In March, we wrote "the industry is moving toward remote." In April, all three providers confirmed it: AWS is pushing its managed endpoint as the primary entry point, Google expanded managed endpoints by 2.5×, and Azure 2.0's headline feature is remote hosting. The local-only era is ending.

## What Changed (March → April 2026)

| | March 2026 | April 2026 | Change |
|---|---|---|---|
| **AWS servers** | 68 | 54 | 12 deprecated (cleanup of redundant/unmaintained) |
| **AWS stars** | 8,500 | 8,800 | +300 |
| **GCP endpoints** | 18 (mostly Preview) | 46 (mostly GA) | +28, massive GA push |
| **GCP Toolbox** | v0.30.0 (13.5K stars) | v1.1.0 (14.8K stars) | Hit 1.0, +1,300 stars |
| **Azure services** | 47+ | 57 (276 tools) | +10 services, tool count now tracked |
| **Azure transport** | stdio only | stdio + HTTP remote | 2.0 stable release |
| **Azure stars** | 2,800 | 3,000 | +200, repo moved to microsoft/mcp |

## Read Our Full Reviews

- [AWS MCP Servers](/reviews/aws-mcp-servers/) — 54 servers, 8,800 stars, the deepest per-service coverage
- [Google Cloud MCP Servers](/reviews/google-cloud-mcp-servers/) — 46 managed endpoints (most GA), the production-ready architecture
- [Azure & Microsoft MCP Servers](/reviews/azure-mcp-servers/) — 276 tools across 57 services, now with remote hosting and sovereign cloud support
- [Equinix's Distributed AI Hub](/guides/equinix-distributed-ai-hub-mcp-infrastructure/) — the vendor-neutral network layer connecting all three clouds, with 40+ MCP tools for interconnection automation

---

*This comparison was originally researched on 2026-03-20 and refreshed on 2026-04-23 using Claude Opus 4.6 (Anthropic). Google Cloud upgraded to 4.5/5 based on the massive managed endpoint expansion and GA readiness. AWS and Azure hold at 4/5.*

