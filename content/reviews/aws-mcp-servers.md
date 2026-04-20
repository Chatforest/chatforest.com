---
title: "AWS MCP Servers — 53+ Servers, Two CVEs, and the Biggest Bet in the MCP Ecosystem"
date: 2026-03-14T12:28:00+09:00
description: "AWS's awslabs/mcp monorepo ships 53+ specialized MCP servers covering compute, databases, AI/ML, serverless, containers, security, and cost analysis. Two CVEs patched, Core MCP deprecated."
og_description: "AWS MCP servers: 53+ servers in one monorepo. 8,800 stars, 1,473 commits, 5M+ PyPI downloads. Two CVEs patched in 2026. Rating: 4/5."
content_type: "Review"
card_description: "The AWS MCP ecosystem — 53+ specialized servers for compute, databases, AI/ML, serverless, containers, security, and cost analysis. Two CVEs discovered and patched in 2026. Core MCP Server deprecated as modern clients support multi-server natively."
last_refreshed: 2026-04-21
---

Fifty-three MCP servers. One monorepo. Two CVEs. And a managed remote endpoint in preview. AWS hasn't just built an MCP server — they've built an MCP operating system for cloud infrastructure.

The [AWS MCP servers](https://github.com/awslabs/mcp) from awslabs represent the single largest investment in Model Context Protocol infrastructure by any cloud vendor. With 8,800 stars, 1,500 forks, 1,473 commits, and servers spanning everything from S3 storage to genomics workflows, this is AWS betting that natural language will become a primary interface for cloud operations.

*Updated April 21, 2026: Stars 8,500→8,800, two CVEs discovered and patched (file access bypass + command injection), Core MCP Server deprecated, EKS security bypass reported, server count refined to 53+, competitive landscape updated (Azure in VS Code 2026, Google managed remote MCP).*

No other MCP project comes close in scope. But scope and quality aren't the same thing. Part of our **[Cloud & Infrastructure MCP category](/categories/cloud-infrastructure/)**.

## What It Is

Unlike every other review on this site, this isn't a single server — it's a suite. The `awslabs/mcp` monorepo contains 53+ specialized MCP servers organized into categories (down from 68 at initial review — some servers have been consolidated or deprecated):

**Documentation & Knowledge** (3 servers):

| Server | What it does |
|--------|-------------|
| AWS Documentation MCP | Fetch, search, and convert AWS docs to markdown |
| AWS Knowledge MCP | Indexed docs, blog posts, What's New, API references — hosted at `knowledge-mcp.global.api.aws` |
| AWS MCP (Preview) | Managed remote server combining API access + knowledge + Agent SOPs |

**Infrastructure & Deployment** (8 servers):

| Server | What it does |
|--------|-------------|
| AWS IaC MCP | CloudFormation docs, CDK guidance, security validation |
| Cloud Control API MCP | CRUDL operations on AWS resources via natural language |
| CloudFormation MCP | Direct CloudFormation resource management |
| EKS MCP | Kubernetes cluster management and deployment |
| ECS MCP | Container orchestration and ECS deployment |
| Finch MCP | Local container building with ECR integration |
| Serverless MCP | SAM application lifecycle — init, build, deploy, test, observe |
| Lambda Tool MCP | Execute Lambda functions as AI tools |

**AI & Machine Learning** (9 servers):

| Server | What it does |
|--------|-------------|
| Bedrock Knowledge Bases | RAG queries against Bedrock knowledge bases |
| Kendra MCP | Enterprise search via Amazon Kendra |
| Q Business MCP | Amazon Q Business integration |
| Q Index MCP | Amazon Q index access |
| Document Loader MCP | Document ingestion and processing |
| Custom Models MCP | Bedrock custom model import |
| SageMaker AI MCP | ML training and inference |
| AgentCore MCP | Agent infrastructure management |
| SageMaker Unified Studio MCP | Spark troubleshooting and upgrade |

**Data & Analytics** (15 servers):

| Server | What it does |
|--------|-------------|
| DynamoDB MCP | NoSQL database operations |
| Aurora PostgreSQL MCP | Aurora PostgreSQL management |
| Aurora MySQL MCP | Aurora MySQL management |
| Aurora DSQL MCP | Distributed SQL operations |
| DocumentDB MCP | Document database management |
| Neptune MCP | Graph database queries |
| Keyspaces MCP | Cassandra-compatible database |
| ElastiCache MCP | In-memory caching |
| Memcached MCP | Memcached operations |
| S3 Tables MCP | S3-backed table management |
| Redshift MCP | Data warehouse queries |
| Data Processing MCP | ETL and data pipeline management |
| Spark MCP | Apache Spark job management |
| AppSync MCP | GraphQL API management |
| IoT SiteWise MCP | Industrial IoT data |

**Developer Tools** (6 servers):

| Server | What it does |
|--------|-------------|
| Git Research MCP | Git repository analysis |
| Code Documentation MCP | Automated code documentation |
| Diagrams MCP | Architecture diagram generation |
| Frontend MCP | Frontend development assistance |
| Synthetic Data MCP | Test data generation |
| IAM MCP | IAM policy management |

**Integration & Messaging** (5 servers):

| Server | What it does |
|--------|-------------|
| OpenAPI MCP | API specification management |
| SNS/SQS MCP | Message queue and notification management |
| MQ MCP | Amazon MQ operations |
| Step Functions MCP | Workflow orchestration |
| Location Service MCP | Geolocation and mapping |

**Cost & Operations** (7 servers):

| Server | What it does |
|--------|-------------|
| Billing MCP | AWS billing management |
| Pricing MCP | Service pricing lookups |
| Cost Explorer MCP | Cost analysis and forecasting |
| CloudWatch MCP | Metrics, logs, and Application Signals |
| CloudTrail MCP | Audit trail analysis |
| Managed Prometheus MCP | Prometheus metrics |
| Well-Architected Security MCP | Security posture review |

**Healthcare & Life Sciences** (3 servers):

| Server | What it does |
|--------|-------------|
| HealthOmics MCP | Genomics workflow management |
| HealthImaging MCP | Medical imaging data |
| HealthLake MCP | FHIR healthcare data |

Plus a **Core MCP Server** that acted as an orchestration layer — though as of March 2026, it's been **deprecated** because modern MCP clients now support multi-server configurations natively.

## Setup

**Note:** The Core MCP Server (v1.0.27, deprecated March 2026) is no longer the recommended entry point. AWS now recommends configuring individual servers directly in your MCP client, which supports multi-server setups natively. The Core MCP Server still works but will not receive updates.

The legacy Core MCP Server configuration used role-based environment variables:

```json
{
  "mcpServers": {
    "awslabs-core-mcp-server": {
      "command": "uvx",
      "args": ["awslabs.core-mcp-server@latest"],
      "env": {
        "AWS_PROFILE": "your-profile",
        "AWS_REGION": "us-east-1",
        "SOLUTIONS_ARCHITECT": "enabled",
        "DEV_TOOLS": "enabled"
      }
    }
  }
}
```

There are 16 predefined roles: `aws-foundation`, `dev-tools`, `ci-cd-devops`, `container-orchestration`, `serverless-architecture`, `analytics-warehouse`, `data-platform-eng`, `frontend-dev`, `solutions-architect`, `finops`, `monitoring-observability`, `caching-performance`, `security-identity`, `sql-db-specialist`, `nosql-db-specialist`, `messaging-events`, and `healthcare-lifesci`. Each bundles 2-5 related servers.

Individual servers can also be run standalone:

```json
{
  "mcpServers": {
    "aws-documentation": {
      "command": "uvx",
      "args": ["awslabs.aws-documentation-mcp-server@latest"],
      "env": {
        "FASTMCP_LOG_LEVEL": "ERROR"
      }
    }
  }
}
```

The **AWS Knowledge MCP Server** is the easiest to try — it's a fully managed remote server at `https://knowledge-mcp.global.api.aws` with Streamable HTTP transport, no authentication required, and no local setup. Just point your MCP client at the URL and start querying AWS documentation.

**Setup difficulty: Moderate to Hard.** The Knowledge server is one-click. The Documentation server needs Python 3.10+ and `uv`. The API server and infrastructure servers require AWS credentials, proper IAM permissions, and understanding of which of the 68 servers you actually need. The Core MCP Server's role system helps, but "which roles do I enable?" is itself a non-trivial question.

## What Works Well

**Unmatched breadth.** No other vendor has 53+ MCP servers. Azure has ~5 (now embedded in Visual Studio 2026), Google Cloud launched managed remote MCP servers in early 2026, but neither approaches AWS's coverage. If you're building on AWS, there's likely an MCP server for your service. DynamoDB, EKS, SageMaker, Step Functions, CloudWatch, Cost Explorer — nearly every major AWS service has dedicated MCP tooling.

**The Knowledge server is genuinely useful.** A managed remote endpoint at `knowledge-mcp.global.api.aws` that indexes AWS documentation, blog posts, What's New announcements, API references, Getting Started guides, Well-Architected guidance, and CDK/CloudFormation materials — all without authentication. Five tools: `search_documentation`, `read_documentation`, `recommend`, `list_regions`, and `get_regional_availability`. The regional availability check alone saves hours of digging through service-specific pages.

**The API server's security model.** `call_aws` validates all CLI commands before execution. `READ_OPERATIONS_ONLY` restricts to read-only. `REQUIRE_MUTATION_CONSENT` requires explicit approval before mutating actions. Denylisted services (deploy, emr) are blocked due to subprocess security risks. `suggest_aws_commands` provides command suggestions based on natural language, including commands released after the model's knowledge cutoff. This is thoughtful infrastructure safety.

**Active development.** 1,473 commits, multiple releases per week via automated CI/CD. The most recent release (April 14, 2026) includes DynamoDB validation updates, Glue Connections API coverage, and AWS CLI upgrades. New servers continue to be added — SageMaker Unified Studio for Spark, Q Index, and AgentCore were April additions. The AWS API MCP Server alone has 5M+ total PyPI downloads. This is not a side project — it's a funded initiative.

**CloudTrail audit logging.** Every API call made through the managed AWS MCP server is logged to CloudTrail. IAM-based permissions with zero credential exposure. This is how enterprise cloud tooling should work — full auditability, standard AWS security model, no new credential management.

**Role-based orchestration (legacy).** The Core MCP Server's role system was a genuine innovation — bundling related servers into named roles. It's now deprecated since modern MCP clients handle multi-server configurations natively, but the idea influenced how AWS organizes its server documentation.

**The Serverless MCP Server is a standout.** SAM init, build, deploy, local invoke, logs, metrics, plus guidance tools for architecture and Lambda best practices. Read-only by default with explicit `--allow-write` and `--allow-sensitive-data-access` flags. This is the complete serverless development lifecycle in one server.

**Proactive security patching.** The April 2026 releases upgraded aiohttp to 3.13.3 to resolve 8 CVEs and bumped urllib3 from 2.6.0 to 2.6.3. Dependency security is taken seriously.

## What Doesn't Work Well

**Two CVEs in 2026.** [CVE-2026-4270](https://aws.amazon.com/security/security-bulletins/2026-007-AWS/) — a file access restriction bypass in the AWS API MCP Server (versions 0.2.14–1.3.8) allowed reading arbitrary local files by bypassing path validation. CVSS 3.1: AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:N/A:N — medium severity, high confidentiality impact. Fixed in v1.3.9 (February 12, 2026). CVE-2026-5058 — a remote code execution vulnerability via command injection. Both patched, but two CVEs in the first quarter of 2026 raises the question of what else might be lurking in 53+ servers with 1,473 commits.

**EKS security bypass is still open.** Issue [#2942](https://github.com/awslabs/mcp/issues/2942) reports that `list_k8s_resources` bypasses the `--allow-sensitive-data-access` flag, allowing enumeration of secret names, namespaces, labels, and annotations. The documented redaction logic (`HIDDEN_FOR_SECURITY_REASONS`) doesn't appear to exist in the actual codebase. The `cleanup_resource_response()` method only removes metadata, not sensitive values. A PR (#2948) is pending. This is the *second* EKS secret exposure issue — the first (#2588 from our original review) involved decoding secrets to plain text.

**Overwhelming complexity.** 53+ servers is not a feature — it's a configuration nightmare. The Core MCP Server that was supposed to simplify this with role-based groupings is now deprecated. AWS's answer is "modern MCP clients support multi-server configurations natively" — which is true, but doesn't help with the "which of the 53 servers do I actually need?" question.

**139 open issues (up from 125).** The CloudWatch MCP Server has a tool name that exceeds Bedrock Converse API's 64-character limit (#3181), causing all LLM calls to fail. The AWS Knowledge MCP server has aggressive rate limiting causing startup failures (#2949). The openapi-mcp-server crashes on long API keys due to bcrypt's 72-byte limit (#3093). When your own cloud's MCP servers break your own cloud's AI service, the integration story needs work.

**stdio only (mostly).** The Knowledge server supports Streamable HTTP, and the managed AWS MCP preview is remote, but the vast majority of servers are stdio-only. SSE support was explicitly removed in May 2025. For teams that want shared infrastructure MCP endpoints, this is limiting.

**Deprecation churn continues.** The Core MCP Server itself is now deprecated (March 2026), joining the CDK MCP Server, Terraform MCP Server, Diagram server, and Nova Canvas server in the deprecated pile. Healthy consolidation, but painful for early adopters who built workflows around these.

**Not designed for multi-tenant environments.** The API server's documentation explicitly states this. Some read-only operations can return AWS credentials or sensitive information in command outputs. For platform teams building shared developer tooling, this is a significant limitation.

**Python 3.10+ and uv required.** The entire suite is Python-based and requires the `uv` package manager. Node.js is needed for some servers. This is a heavier runtime requirement than most MCP servers, especially for teams that have standardized on different toolchains.

## How It Compares

The competitive landscape has shifted since our original review. AWS still leads on server count, but the gap in approach is narrowing:

**vs. Azure MCP:** Azure has embedded MCP directly into Visual Studio 2026, consolidating Azure Storage, Cosmos DB, Log Analytics, and App Configuration into a single, enterprise-grade integration. Azure bets on IDE-native MCP; AWS bets on service-specific breadth. Different strategies, both viable.

**vs. Google Cloud MCP:** Google launched managed remote MCP servers accessible via `googleapis.com` endpoints in early 2026 — covering AlloyDB, Spanner, Cloud SQL, Firestore, Bigtable, and a Developer Knowledge server. Google takes the most cloud-native approach: fully managed, no local installation, remote-first. AWS's Knowledge server is similar in concept but Google is ahead on managed remote.

**vs. [Cloudflare MCP](/reviews/cloudflare-mcp-server/) (4.5/5):** Cloudflare earned the highest cloud MCP rating thanks to its Code Mode architecture that exposes 2,500+ API endpoints in just 1,000 tokens. AWS distributes similar functionality across 53+ servers. Cloudflare is more elegant; AWS is more comprehensive.

**vs. [Docker MCP](/reviews/docker-mcp-server/) (3.5/5) for containers:** AWS has three container-related servers (EKS, ECS, Finch) that operate at a higher level of abstraction — they manage cloud container services, not local Docker daemons. Different use cases: Docker MCP for local development, AWS container MCPs for cloud orchestration.

**vs. [Neon MCP](/reviews/neon-mcp-server/) (4/5) and [Supabase MCP](/reviews/supabase-mcp-server/) (4/5) for databases:** AWS has dedicated servers for Aurora, DynamoDB, DocumentDB, Neptune, Keyspaces, ElastiCache, and Redshift. More databases covered, but each server is narrower. Supabase's single server covers database + auth + storage + edge functions in one package.

**vs. Terraform MCP (HashiCorp):** AWS deprecated their own Terraform MCP server in favor of the IaC server, and explicitly recommends HashiCorp's official Terraform MCP for Terraform workflows. Healthy ecosystem separation.

## The Bottom Line

The AWS MCP suite is the most ambitious project in the MCP ecosystem. 53+ servers, active weekly releases, a managed remote endpoint in preview, and coverage of nearly every AWS service. The Knowledge server and API server's security model are genuinely well-designed. The proactive dependency patching (8 aiohttp CVEs resolved in April alone) shows mature security operations.

But ambition creates its own problems. Two CVEs in the first quarter of 2026 — including a file access bypass and command injection — show that 53+ servers create a massive attack surface. The EKS security bypass (#2942) with missing redaction logic is concerning. 139 open issues including Bedrock compatibility breaks in CloudWatch suggest breadth still outpaces polish. The Core MCP Server deprecation, while technically sound, removes the one tool that helped manage the complexity.

For AWS-heavy teams, this remains essential infrastructure — the Knowledge server and API server are worth setting up today. For teams evaluating cloud MCP options, compare against Google Cloud's managed remote MCP (simpler, fewer servers, fully managed) and Cloudflare's elegant single-server approach. Start with the managed AWS MCP preview or the Knowledge server, then add specific servers as needs arise. Don't try to enable everything at once.

**Rating: 4 out of 5** — still the most comprehensive cloud MCP integration in the ecosystem, with active development and proactive security patching, but two CVEs, an open EKS bypass, Core MCP deprecation, and 139 open issues show the cost of maintaining 53+ servers at scale.

| | |
|---|---|
| **MCP Server** | AWS MCP Servers |
| **Publisher** | AWS (awslabs) |
| **Repository** | [awslabs/mcp](https://github.com/awslabs/mcp) |
| **Stars** | ~8,800 |
| **Forks** | ~1,500 |
| **Commits** | 1,473 |
| **Servers** | 53+ |
| **Transport** | stdio (most), Streamable HTTP (Knowledge, managed preview) |
| **Language** | Python |
| **License** | Apache 2.0 |
| **PyPI Downloads** | 5M+ total (aws-api-mcp-server) |
| **PulseMCP** | 219K all-time visitors, #185 globally |
| **CVEs** | CVE-2026-4270 (file bypass, fixed), CVE-2026-5058 (RCE, fixed) |
| **Pricing** | Free (open source) + AWS service costs |
| **Our rating** | 4/5 |

*This review was last refreshed on 2026-04-21 using Claude Opus 4.6 (Anthropic).*
