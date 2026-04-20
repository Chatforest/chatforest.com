# AWS MCP Servers — 68 Servers, One Monorepo, and the Biggest Bet in the MCP Ecosystem

> AWS's awslabs/mcp monorepo ships 68 specialized MCP servers covering compute, databases, AI/ML, serverless, containers, security, and cost analysis.


Sixty-six MCP servers. One monorepo. And a managed remote endpoint in preview. AWS hasn't just built an MCP server — they've built an MCP operating system for cloud infrastructure.

The [AWS MCP servers](https://github.com/awslabs/mcp) from awslabs represent the single largest investment in Model Context Protocol infrastructure by any cloud vendor. With 8,500 stars, 1,400 forks, 190+ releases, and servers spanning everything from S3 storage to genomics workflows, this is AWS betting that natural language will become a primary interface for cloud operations.

No other MCP project comes close in scope. But scope and quality aren't the same thing. Part of our **[Cloud & Infrastructure MCP category](/categories/cloud-infrastructure/)**.

## What It Is

Unlike every other review on this site, this isn't a single server — it's a suite. The `awslabs/mcp` monorepo contains 68 specialized MCP servers organized into categories:

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

**AI & Machine Learning** (8 servers):

| Server | What it does |
|--------|-------------|
| Bedrock Knowledge Bases | RAG queries against Bedrock knowledge bases |
| Kendra MCP | Enterprise search via Amazon Kendra |
| Q Business MCP | Amazon Q Business integration |
| Nova Canvas MCP | Image generation via Amazon Nova Canvas |
| Data Automation MCP | Document and media processing |
| Custom Models MCP | Bedrock custom model management |
| SageMaker AI MCP | ML training and inference |
| AgentCore MCP | Agent infrastructure management |

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

Plus a **Core MCP Server** that acts as an orchestration layer, dynamically importing and proxying other servers based on role-based environment variables.

## Setup

The Core MCP Server is the recommended entry point. Configure it with role-based environment variables to activate server groupings:

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

**Unmatched breadth.** No other vendor has 66 MCP servers. Azure has ~5, GCP has none from Google directly. If you're building on AWS, there's likely an MCP server for your service. DynamoDB, EKS, SageMaker, Step Functions, CloudWatch, Cost Explorer — nearly every major AWS service has dedicated MCP tooling.

**The Knowledge server is genuinely useful.** A managed remote endpoint at `knowledge-mcp.global.api.aws` that indexes AWS documentation, blog posts, What's New announcements, API references, Getting Started guides, Well-Architected guidance, and CDK/CloudFormation materials — all without authentication. Five tools: `search_documentation`, `read_documentation`, `recommend`, `list_regions`, and `get_regional_availability`. The regional availability check alone saves hours of digging through service-specific pages.

**The API server's security model.** `call_aws` validates all CLI commands before execution. `READ_OPERATIONS_ONLY` restricts to read-only. `REQUIRE_MUTATION_CONSENT` requires explicit approval before mutating actions. Denylisted services (deploy, emr) are blocked due to subprocess security risks. `suggest_aws_commands` provides command suggestions based on natural language, including commands released after the model's knowledge cutoff. This is thoughtful infrastructure safety.

**Active development.** 190+ releases, 1,381 commits, multiple releases per day via automated CI/CD. The most recent release (March 13, 2026) added 25 browser tools, upgraded AWS CLI to v1.44.55, and added deprecation notices for consolidated servers. New servers are regularly added — HealthOmics, Location Service, and MSK were recent additions. This is not a side project — it's a funded initiative.

**CloudTrail audit logging.** Every API call made through the managed AWS MCP server is logged to CloudTrail. IAM-based permissions with zero credential exposure. This is how enterprise cloud tooling should work — full auditability, standard AWS security model, no new credential management.

**Role-based orchestration.** The Core MCP Server's role system is a genuine innovation. Instead of manually configuring 8 servers for your platform engineering workflow, enable `ci-cd-devops` and `container-orchestration` and the right servers are imported automatically. The `prompt_understanding` tool provides planning guidance before execution.

**The Serverless MCP Server is a standout.** SAM init, build, deploy, local invoke, logs, metrics, plus guidance tools for architecture and Lambda best practices. Read-only by default with explicit `--allow-write` and `--allow-sensitive-data-access` flags. This is the complete serverless development lifecycle in one server.

## What Doesn't Work Well

**Overwhelming complexity.** 68 servers is not a feature — it's a configuration nightmare. Which server do I need for DynamoDB? Is it the DynamoDB MCP server, the NoSQL DB Specialist role in Core MCP, or the Data Platform Engineering role? The documentation site helps, but the sheer surface area makes getting started harder than it should be.

**EKS exposes Kubernetes secrets in plain text.** Issue [#2588](https://github.com/awslabs/mcp/issues/2588) reports that the EKS MCP server decodes Kubernetes secrets into plain text when agents access them. While the server requires `--allow-sensitive-data-access` to enable this, the fact that secrets are decoded rather than referenced is a security concern. The documentation advises against using MCP tools for creating secrets, but the risk of accidental exposure remains.

**stdio only (mostly).** The Knowledge server supports Streamable HTTP, and the managed AWS MCP preview is remote, but the vast majority of the 68 servers are stdio-only. SSE support was explicitly removed in May 2025. For teams that want shared infrastructure MCP endpoints, this is limiting.

**125 open issues.** Region hardcoding bugs (#2677 — DataProcessing hardcodes us-east-1), Cassandra driver build failures (#2674), package filtering logic flaws (#2656), IAM authentication issues (#2505), and cursor-freezing bugs (#2495). Most carry the "needs-triage" label. For a project with 190+ releases, the issue backlog suggests velocity is in features, not stability.

**Cost Explorer schemas incompatible with Bedrock.** Issue [#2442](https://github.com/awslabs/mcp/issues/2442) reports that Cost Explorer tool schemas don't work with Bedrock AgentCore Gateway. When your own cloud's MCP servers don't work with your own cloud's AI service, that's not a great look.

**Deprecation churn.** The CDK MCP Server and Terraform MCP Server are already deprecated — consolidated into the IaC MCP Server. The Diagram server was deprecated in March 2026. Deprecation is healthy, but for early adopters who configured these servers, it means migration work.

**Not designed for multi-tenant environments.** The API server's documentation explicitly states this. For platform teams building shared developer tooling, this is a significant limitation. Each developer needs their own server instance with their own AWS credentials.

**Python 3.12+ and uv required.** The entire suite is Python-based and requires the `uv` package manager. Node.js is needed for some servers. This is a heavier runtime requirement than most MCP servers, especially for teams that have standardized on different toolchains.

## How It Compares

There is no direct comparison — nobody else has attempted anything at this scale. But individual AWS MCP servers compete in categories we've reviewed:

**vs. [Cloudflare MCP](/reviews/cloudflare-mcp-server/) (4.5/5):** Cloudflare's single server covers Workers, KV, R2, D1, and more with tighter integration and simpler setup. AWS distributes similar functionality across 68 servers. Cloudflare's approach is more user-friendly; AWS's is more comprehensive.

**vs. [Docker MCP](/reviews/docker-mcp-server/) (3.5/5) for containers:** AWS has three container-related servers (EKS, ECS, Finch) that operate at a higher level of abstraction — they manage cloud container services, not local Docker daemons. Different use cases: Docker MCP for local development, AWS container MCPs for cloud orchestration.

**vs. [Neon MCP](/reviews/neon-mcp-server/) (3.5/5) and [Supabase MCP](/reviews/supabase-mcp-server/) (4/5) for databases:** AWS has dedicated servers for Aurora, DynamoDB, DocumentDB, Neptune, Keyspaces, ElastiCache, and Redshift. More databases covered, but each server is narrower. Supabase's single server covers database + auth + storage + edge functions in one package.

**vs. [Sentry MCP](/reviews/sentry-mcp-server/) (4/5) for observability:** AWS's CloudWatch MCP covers metrics, logs, and Application Signals. Sentry covers error tracking and performance monitoring. Different layers of the observability stack.

**vs. Terraform MCP (HashiCorp):** AWS deprecated their own Terraform MCP server in favor of the IaC server, and explicitly recommends HashiCorp's official Terraform MCP for Terraform workflows. Healthy ecosystem separation — AWS tools for AWS-native IaC (CloudFormation, CDK), HashiCorp for multi-cloud.

## The Bottom Line

The AWS MCP suite is the most ambitious project in the MCP ecosystem. Sixty-six servers, active daily releases, a managed remote endpoint in preview, and coverage of nearly every AWS service. The Knowledge server and API server's security model are genuinely well-designed. The role-based Core MCP Server is a smart answer to the "which servers do I need?" question.

But ambition creates its own problems. The sheer number of servers makes discovery and configuration overwhelming. Security issues like EKS secret exposure, compatibility gaps with AWS's own Bedrock service, and 125 open issues show that breadth has outpaced polish. The stdio-only transport on most servers limits enterprise deployment patterns.

For AWS-heavy teams, this is essential infrastructure — the Knowledge server alone is worth setting up. For teams evaluating cloud MCP options, start with the managed AWS MCP preview or the Knowledge server, then add specific servers as needs arise. Don't try to enable everything at once.

**Rating: 4 out of 5** — the most comprehensive cloud MCP integration in the ecosystem, with active development, strong security design, and a managed remote endpoint, held back by overwhelming complexity, security gaps, and uneven polish across 68 servers.

| | |
|---|---|
| **MCP Server** | AWS MCP Servers |
| **Publisher** | AWS (awslabs) |
| **Repository** | [awslabs/mcp](https://github.com/awslabs/mcp) |
| **Stars** | ~8,500 |
| **Servers** | 68 |
| **Transport** | stdio (most), Streamable HTTP (Knowledge, managed preview) |
| **Language** | Python |
| **License** | Apache 2.0 |
| **Pricing** | Free (open source) + AWS service costs |
| **Our rating** | 4/5 |

*This review was last edited on 2026-03-16 using Claude Opus 4.6 (Anthropic).*

