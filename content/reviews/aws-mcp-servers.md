---
title: "AWS MCP Servers — 54 Active Servers, Nine Deprecated, and Google Just Matched the Count"
date: 2026-03-14T12:28:00+09:00
lastmod: 2026-05-16T22:00:00+09:00
description: "AWS's awslabs/mcp monorepo has 54 active MCP servers (9 deprecated) covering compute, databases, AI/ML, serverless, containers, security, and cost analysis. Two CVEs patched, IAM and EKS security fixes. Google Cloud now matches with 50 managed servers."
og_description: "AWS MCP servers: 54 active servers, 9 deprecated. 8,900 stars, 1,495 commits, 5M+ PyPI downloads. Google matches with 50 managed servers. Rating: 4/5."
content_type: "Review"
card_description: "The AWS MCP ecosystem — 54 active servers for compute, databases, AI/ML, serverless, containers, security, and cost analysis. Nine servers deprecated in consolidation wave. Google Cloud now matches count with 50 managed remote servers. Azure ships 230+ tools across 45 services."
last_refreshed: 2026-04-29
---

Fifty-four active MCP servers. Nine deprecated. One monorepo. Two CVEs. And a competitive landscape that just shifted under AWS's feet.

The [AWS MCP servers](https://github.com/awslabs/mcp) from awslabs represent a massive investment in Model Context Protocol infrastructure. With 8,900 stars, 1,500 forks, 1,495 commits, and servers spanning everything from S3 storage to genomics workflows, this is AWS betting that natural language will become a primary interface for cloud operations.

*Updated May 16, 2026: The managed AWS MCP Server (previously "AWS MCP Preview") [reached general availability on May 6, 2026](/reviews/aws-mcp-server-ga/) — 11 tools, 15,000+ AWS APIs, IAM SigV4 auth, CloudTrail logging, sandboxed Python execution, no local install required. See our [dedicated review](/reviews/aws-mcp-server-ga/) for the full breakdown.*

*Updated April 29, 2026: Stars 8,800→8,900, commits 1,473→1,495, issues 139→147. Major deprecation wave — Cloud Control API, MSK, Code Documentation, CloudWatch AppSignals, Git Research, Bedrock Data Automation all deprecated (9 total). IAM privilege escalation and EKS path traversal security fixes. OpenAPI migrated to FastMCP 3.x. COMPETITIVE LANDSCAPE TRANSFORMED: Google Cloud now has 50 managed remote MCP servers (matching AWS count), Azure ships 230+ tools across 45 services built into VS 2022.*

But AWS is no longer alone at the top. Google matched the server count, Azure matched the service breadth, and both did it with zero-install managed approaches. Part of our **[Cloud & Infrastructure MCP category](/categories/cloud-infrastructure/)**.

## What It Is

Unlike every other review on this site, this isn't a single server — it's a suite. The `awslabs/mcp` monorepo contains 54 active MCP servers organized into categories (down from 68 at initial review — nine servers have been deprecated in a consolidation wave, and 12 deprecated directories were cleaned up in the April 21 release):

**Documentation & Knowledge** (3 servers):

| Server | What it does |
|--------|-------------|
| AWS Documentation MCP | Fetch, search, and convert AWS docs to markdown |
| AWS Knowledge MCP | Indexed docs, blog posts, What's New, API references — hosted at `knowledge-mcp.global.api.aws` |
| [AWS MCP Server (GA)](/reviews/aws-mcp-server-ga/) | Managed remote server — 11 tools, 15,000+ APIs, IAM auth, CloudTrail logging, sandboxed Python. **Now GA May 2026.** |

**Infrastructure & Deployment** (8 servers):

| Server | What it does |
|--------|-------------|
| AWS IaC MCP | CloudFormation docs, CDK guidance, security validation (replaces deprecated Cloud Control API + CDK servers) |
| EKS MCP | Kubernetes cluster management — now with kubeconfig/OIDC auth (April 2026) |
| ECS MCP | Container orchestration and ECS deployment |
| Finch MCP | Local container building with ECR integration |
| Serverless MCP | SAM application lifecycle — init, build, deploy, test, observe |
| Lambda Tool MCP | Execute Lambda functions as AI tools |
| AWS Support MCP | AWS Support case management |
| Systems Manager for SAP MCP | SAP workload management on AWS |

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
| AgentCore MCP | Agent infrastructure management — now with Runtime tools + 9 code interpreter tools |
| SageMaker Unified Studio MCP (Spark Troubleshooting) | Spark job troubleshooting |
| SageMaker Unified Studio MCP (Spark Upgrade) | Spark version upgrade assistance |

**Data & Analytics** (17 servers):

| Server | What it does |
|--------|-------------|
| DynamoDB MCP | NoSQL database operations |
| Aurora PostgreSQL MCP | Aurora PostgreSQL management (Ultra Fast Create support added April 2026) |
| Aurora MySQL MCP | Aurora MySQL management |
| Aurora DSQL MCP | Distributed SQL operations |
| DocumentDB MCP | Document database management |
| Neptune MCP | Graph database queries (custom endpoint URL support added) |
| Keyspaces MCP | Cassandra-compatible database |
| Timestream for InfluxDB MCP | Time-series database operations |
| ElastiCache MCP | In-memory caching |
| ElastiCache/MemoryDB for Valkey MCP | Valkey-compatible in-memory datastore |
| Memcached MCP | Memcached operations |
| S3 Tables MCP | S3-backed table management |
| Redshift MCP | Data warehouse queries |
| Data Processing MCP | ETL and data pipeline management (now supports `--allow-sensitive-data-access` flag) |
| AppSync MCP | GraphQL API management |
| IoT SiteWise MCP | Industrial IoT data |
| Spark MCP | Apache Spark job management |

**Developer Tools** (2 active servers):

| Server | What it does |
|--------|-------------|
| IAM MCP | IAM policy management (privilege escalation vulnerability fixed April 2026) |
| OpenAPI MCP | API specification management (migrated to FastMCP 3.x April 2026) |

**Integration & Messaging** (4 servers):

| Server | What it does |
|--------|-------------|
| SNS/SQS MCP | Message queue and notification management |
| MQ MCP | Amazon MQ operations |
| Step Functions MCP | Workflow orchestration |
| Location Service MCP | Geolocation and mapping |

**Cost & Operations** (8 servers):

| Server | What it does |
|--------|-------------|
| Billing MCP | AWS billing management (billing view tools + analytics added April 2026) |
| Pricing MCP | Service pricing lookups |
| CloudWatch MCP | Metrics, logs (field index recommender added), and Application Signals |
| CloudTrail MCP | Audit trail analysis |
| Managed Prometheus MCP | Prometheus metrics |
| Observability Admin MCP | Telemetry rules and configuration |
| Well-Architected Security MCP | Security posture review |
| Cost Explorer MCP | Cost analysis and forecasting |

**Healthcare & Life Sciences** (3 servers):

| Server | What it does |
|--------|-------------|
| HealthOmics MCP | Genomics workflow management |
| HealthImaging MCP | Medical imaging data |
| HealthLake MCP | FHIR healthcare data |

**Deprecated servers** (9 total, directories cleaned up April 21): Core MCP Server (orchestration layer, March 2026), CDK MCP Server (replaced by IaC), Cloud Control API MCP (replaced by IaC), Terraform MCP (use HashiCorp's official), MSK MCP (April 2026), Code Documentation MCP, Git Research MCP, CloudWatch AppSignals (folded into CloudWatch), Nova Canvas MCP, and Bedrock Data Automation MCP.

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

**Setup difficulty: Moderate to Hard.** The Knowledge server is one-click. The Documentation server needs Python 3.10+ and `uv`. The API server and infrastructure servers require AWS credentials, proper IAM permissions, and understanding of which of the 54 active servers you actually need. With the Core MCP Server deprecated, there's no bundling mechanism — you configure each server individually.

## What Works Well

**Breadth no longer unmatched, but still deep.** AWS has 54 active MCP servers — Google Cloud now matches with 50 managed remote servers, and Azure ships 230+ tools across 45 services. But AWS's servers go deeper into service-specific operations than either competitor. DynamoDB, EKS, SageMaker, Step Functions, CloudWatch, Cost Explorer — nearly every major AWS service has dedicated MCP tooling with service-specific features that generic cloud APIs don't expose.

**The Knowledge server is genuinely useful.** A managed remote endpoint at `knowledge-mcp.global.api.aws` that indexes AWS documentation, blog posts, What's New announcements, API references, Getting Started guides, Well-Architected guidance, and CDK/CloudFormation materials — all without authentication. Five tools: `search_documentation`, `read_documentation`, `recommend`, `list_regions`, and `get_regional_availability`. The regional availability check alone saves hours of digging through service-specific pages.

**The API server's security model.** `call_aws` validates all CLI commands before execution. `READ_OPERATIONS_ONLY` restricts to read-only. `REQUIRE_MUTATION_CONSENT` requires explicit approval before mutating actions. Denylisted services (deploy, emr) are blocked due to subprocess security risks. `suggest_aws_commands` provides command suggestions based on natural language, including commands released after the model's knowledge cutoff. This is thoughtful infrastructure safety.

**Active development.** 1,495 commits, multiple releases per week via automated CI/CD. The April 21 release migrated OpenAPI to FastMCP 3.x, added billing view tools to Cost Management, integrated Runtime tools into AgentCore, and cleaned up 12 deprecated server directories. The AWS API MCP Server alone has 5M+ total PyPI downloads. This is not a side project — it's a funded initiative with continuous delivery.

**CloudTrail audit logging.** Every API call made through the managed AWS MCP server is logged to CloudTrail. IAM-based permissions with zero credential exposure. This is how enterprise cloud tooling should work — full auditability, standard AWS security model, no new credential management.

**Role-based orchestration (legacy).** The Core MCP Server's role system was a genuine innovation — bundling related servers into named roles. It's now deprecated since modern MCP clients handle multi-server configurations natively, but the idea influenced how AWS organizes its server documentation.

**The Serverless MCP Server is a standout.** SAM init, build, deploy, local invoke, logs, metrics, plus guidance tools for architecture and Lambda best practices. Read-only by default with explicit `--allow-write` and `--allow-sensitive-data-access` flags. This is the complete serverless development lifecycle in one server.

**Proactive security patching.** The April 2026 releases upgraded aiohttp to 3.13.3 to resolve 8 CVEs and bumped urllib3 from 2.6.0 to 2.6.3. Dependency security is taken seriously.

## What Doesn't Work Well

**Security fixes keep coming.** The two CVEs from early 2026 (CVE-2026-4270 file access bypass, CVE-2026-5058 command injection) were patched, but April brought more: the IAM MCP Server had a privilege escalation vulnerability fixed (April 10), and EKS got a path traversal fix in app manifest generation (March 25). That's four distinct security issues across four months — the pace reflects both the attack surface of 54 servers and AWS's responsiveness, but the frequency is concerning.

**EKS security bypass is still open.** Issue [#2942](https://github.com/awslabs/mcp/issues/2942) reports that `list_k8s_resources` bypasses the `--allow-sensitive-data-access` flag, allowing enumeration of secret names, namespaces, labels, and annotations. The documented redaction logic (`HIDDEN_FOR_SECURITY_REASONS`) doesn't appear to exist in the actual codebase. A PR (#2948) is pending. This is now the *third* EKS security issue — after the secret exposure (#2588) and the path traversal fix. The EKS MCP Server did gain kubeconfig/OIDC authentication support (April 2), but the security track record remains shaky.

**Overwhelming complexity.** 54 active servers is not a feature — it's a configuration nightmare. The Core MCP Server that was supposed to simplify this with role-based groupings is deprecated. AWS's answer is "modern MCP clients support multi-server configurations natively" — which is true, but doesn't help with the "which of the 54 servers do I actually need?" question. Meanwhile, Google offers 50 managed remote servers that auto-enable when you enable the service, requiring zero local configuration.

**147 open issues (up from 139).** The CloudWatch MCP Server has a tool name that exceeds Bedrock Converse API's 64-character limit (#3181), causing all LLM calls to fail. The AWS Knowledge MCP server has aggressive rate limiting causing startup failures (#2949). The openapi-mcp-server crashes on long API keys due to bcrypt's 72-byte limit (#3093). With 334 open PRs, the backlog is growing faster than the team can review. When your own cloud's MCP servers break your own cloud's AI service, the integration story needs work.

**stdio only (mostly).** The Knowledge server supports Streamable HTTP, and the [managed AWS MCP Server (now GA)](/reviews/aws-mcp-server-ga/) is remote, but the vast majority of servers are stdio-only. SSE support was explicitly removed in May 2025. For teams that want shared infrastructure MCP endpoints, this is limiting.

**Deprecation wave accelerated.** Nine servers are now deprecated — Core, CDK, Cloud Control API, Terraform, MSK, Code Documentation, Git Research, CloudWatch AppSignals, Nova Canvas, and Bedrock Data Automation. The April 21 release removed 12 deprecated directories entirely. Healthy consolidation, but nine deprecations in four months is painful for early adopters who built workflows around these servers.

**Not designed for multi-tenant environments.** The API server's documentation explicitly states this. Some read-only operations can return AWS credentials or sensitive information in command outputs. For platform teams building shared developer tooling, this is a significant limitation.

**Python 3.10+ and uv required.** The entire suite is Python-based and requires the `uv` package manager. Node.js is needed for some servers. This is a heavier runtime requirement than most MCP servers, especially for teams that have standardized on different toolchains.

## How It Compares

The competitive landscape has **transformed** since our original review. AWS no longer leads on server count — and the gap in managed experience has widened against them:

**vs. Google Cloud MCP (50 managed servers):** Google launched 50 managed remote MCP servers at Cloud Next '26, covering everything from BigQuery and Spanner to GKE, Cloud Run, Pub/Sub, Cloud Storage, and even Google Workspace (Drive, Gmail, Calendar, Chat). Every Google Cloud service is MCP-enabled by default with native IAM Deny policies, Model Armor for prompt injection defense, OTel tracing, and Cloud Audit Logs. Servers auto-enable when you enable the service — no local setup, no `uv`, no Python. This is the approach AWS should be worried about: same breadth, better developer experience, fully managed. Google matches AWS on count (50 vs. 54) and exceeds it on ease of use.

**vs. Azure MCP (230+ tools, 45 services):** Azure now ships MCP tools built directly into Visual Studio 2022 (not just VS 2026) as part of the Azure development workload — no extension required. 230+ tools across 45 Azure services accessible through GitHub Copilot Chat. The April 2026 Azure DevOps MCP update added WIQL query support. Azure bets on IDE-native MCP with massive tool consolidation; AWS bets on service-specific servers. Azure's approach means zero configuration for VS users — a stark contrast to AWS's 54 separate servers.

**vs. [Cloudflare MCP](/reviews/cloudflare-mcp-server/) (4.5/5):** Cloudflare earned the highest cloud MCP rating thanks to its Code Mode architecture that exposes 2,500+ API endpoints in just 1,000 tokens. AWS distributes similar functionality across 54 servers. Cloudflare is more elegant; AWS is more comprehensive.

**vs. [Docker MCP](/reviews/docker-mcp-server/) (3.5/5) for containers:** AWS has three container-related servers (EKS, ECS, Finch) that operate at a higher level of abstraction — they manage cloud container services, not local Docker daemons. Different use cases: Docker MCP for local development, AWS container MCPs for cloud orchestration.

**vs. [Neon MCP](/reviews/neon-mcp-server/) (4/5) and [Supabase MCP](/reviews/supabase-mcp-server/) (4/5) for databases:** AWS has dedicated servers for Aurora, DynamoDB, DocumentDB, Neptune, Keyspaces, ElastiCache, Timestream, and Redshift. More databases covered, but each server is narrower. Supabase's single server covers database + auth + storage + edge functions in one package.

**vs. Terraform MCP (HashiCorp):** AWS deprecated their own Terraform MCP server in favor of the IaC server, and explicitly recommends HashiCorp's official Terraform MCP for Terraform workflows. Healthy ecosystem separation.

## The Bottom Line

The AWS MCP suite is no longer the most ambitious cloud MCP project — Google Cloud's 50 managed remote servers and Azure's 230+ tools make the field genuinely competitive. But AWS still has 54 active servers with deep, service-specific functionality, active weekly releases, and a [managed remote endpoint now at GA](/reviews/aws-mcp-server-ga/). The Knowledge server and API server's security model remain well-designed. The proactive dependency patching and rapid security response show mature operations.

But the competitive gap has closed while AWS's own challenges persist. Four security issues in four months (two CVEs, IAM privilege escalation, EKS path traversal), the still-open EKS security bypass (#2942), 147 open issues, 334 open PRs, and nine deprecated servers show that maintaining 54 servers at this pace is straining even AWS's resources. Meanwhile, Google's servers auto-enable with zero configuration, and Azure's tools come built into your IDE. AWS's stdio-first, Python-required approach feels increasingly dated in a managed-remote world.

For AWS-heavy teams, this remains essential infrastructure — the Knowledge server and the [managed AWS MCP Server (now GA)](/reviews/aws-mcp-server-ga/) are worth using today. For teams evaluating cloud MCP options, the choice has become genuinely interesting: Google Cloud for the best managed experience and automatic enablement, Azure for IDE-native integration and consolidated tooling, AWS for the deepest service-specific coverage. Start with the [managed AWS MCP Server (GA)](/reviews/aws-mcp-server-ga/) or the Knowledge server, then add specific servers as needs arise. Don't try to enable everything at once.

**Rating: 4 out of 5** — still the deepest cloud MCP integration with the most service-specific coverage, but the competitive landscape has transformed (Google matches on count, Azure exceeds on tooling), four security fixes in four months, an open EKS bypass, 147 open issues, 334 open PRs, and nine deprecated servers show the cost of maintaining this many servers at scale.

| | |
|---|---|
| **MCP Server** | AWS MCP Servers |
| **Publisher** | AWS (awslabs) |
| **Repository** | [awslabs/mcp](https://github.com/awslabs/mcp) |
| **Stars** | ~8,900 |
| **Forks** | ~1,500 |
| **Commits** | 1,495 |
| **Servers** | 54 active (9 deprecated) |
| **Transport** | stdio (most), Streamable HTTP (Knowledge, [managed GA server](/reviews/aws-mcp-server-ga/)) |
| **Language** | Python |
| **License** | Apache 2.0 |
| **PyPI Downloads** | 5M+ total (aws-api-mcp-server) |
| **PulseMCP** | 219K all-time visitors, #185 globally |
| **CVEs** | CVE-2026-4270 (file bypass, fixed), CVE-2026-5058 (RCE, fixed) |
| **Pricing** | Free (open source) + AWS service costs |
| **Our rating** | 4/5 |

| **Open Issues** | 147 |
| **Open PRs** | 334 |

*This review was last refreshed on 2026-04-29 using Claude Opus 4.6 (Anthropic).*
