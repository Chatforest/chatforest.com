# Serverless & FaaS MCP Servers — AWS Lambda, Cloudflare Workers, Azure Functions, Google Cloud Run, Vercel, Firebase, and More

> Serverless and FaaS MCP servers help AI agents deploy, manage, and invoke serverless functions across major cloud platforms via the Model Context Protocol.


Serverless and FaaS (Function-as-a-Service) MCP servers let AI assistants deploy, invoke, and manage serverless functions across major cloud platforms through the Model Context Protocol. Instead of navigating cloud consoles or memorizing CLI commands, AI agents can manage serverless infrastructure conversationally.

This review covers the **serverless and FaaS** ecosystem — AWS Lambda tools, Cloudflare Workers integration, Azure Functions support, Google Cloud Run deployment, Vercel adapters, Firebase services, and serverless MCP frameworks. For related servers, see our [Cloud Platform review](/reviews/cloud-storage-mcp-servers/) and [Container/Docker/Kubernetes review](/reviews/container-docker-kubernetes-mcp-servers/).

The headline findings: **AWS dominates with a three-tier ecosystem** — official monorepo (9,604 stars), agent plugins (863 stars), and reference samples (243 stars). **Cloudflare's Code Mode pattern keeps surging** (263 stars in early 2026 → 733 stars as of August 2026) as the most token-efficient API approach. **Azure Functions MCP reached GA** with fluent API, OBO auth, and Streamable HTTP. **Google Cloud gcloud-mcp expanded to 66+ tools** across four servers. **Streamable HTTP is now the standard transport** replacing SSE across AWS and Azure. Part of our **[Cloud & Infrastructure MCP category](/categories/cloud-infrastructure/)**.

*Correction (2026-08-16): star counts, versions, and commit/token figures below were re-verified against live GitHub and Cloudflare sources during a claim-level audit — several were stale or, in one case (Cloudflare Code Mode token count), not supported by the cited source at all. See inline notes.*

## AWS Lambda & Serverless

### awslabs/mcp — AWS Serverless MCP Server (Official)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [AWS Serverless MCP Server](https://github.com/awslabs/mcp) | 9,604 | Python/TypeScript | Apache-2.0 | 14+ servers |

The **official AWS MCP monorepo** includes dedicated serverless servers:

- **AWS Serverless MCP Server** — complete serverless application lifecycle management via SAM CLI — build, deploy, test, and debug serverless applications
- **Lambda Tool MCP Server** — expose any Lambda function as an MCP tool for AI agents to invoke without code changes
- **MCP Lambda Handler** *(new)* — Python library (on PyPI) for creating serverless HTTP handlers with pluggable session management (NoOp stateless or DynamoDB-backed persistent sessions)
- **AWS IaC MCP Server** — CloudFormation and CDK infrastructure toolkit
- **14+ additional servers** — EKS, ECS, CloudFormation, documentation, support, and more

**SSE transport removed** across all servers — Streamable HTTP is now the standard. Enterprise authentication: API Gateway with OAuth, Bedrock AgentCore Gateway, Lambda function URLs with SigV4, and direct Lambda Invoke API.

### awslabs/agent-plugins (AWS Agent Plugins) *(New)*

| Server | Stars | Language | License | Plugins |
|--------|-------|----------|---------|---------|
| [agent-plugins](https://github.com/awslabs/agent-plugins) | 863 | Multi | Apache-2.0 | 6 |

**Compound agent plugins** that package AWS expertise (MCP servers + agent skills + hooks + reference docs) into installable units:

- **aws-serverless** — serverless development expertise with Lambda, API Gateway, EventBridge, Step Functions
- **deploy-on-aws** — deployment patterns and best practices
- **databases-on-aws** — database service guidance
- **sagemaker-ai**, **aws-amplify**, **amazon-location-service**

Works with Claude Code, Codex, and Cursor. Created February 2026 — rapidly adopted.

### aws-samples/sample-serverless-mcp-servers (Reference Implementations) *(New)*

| Server | Stars | Language | License | Samples |
|--------|-------|----------|---------|---------|
| [sample-serverless-mcp-servers](https://github.com/aws-samples/sample-serverless-mcp-servers) | 243 | Python/TypeScript | MIT-0 | 9 |

**9 reference implementations** demonstrating different serverless MCP deployment patterns:

- **Stateless MCP on Lambda** — Node.js and Python variants
- **Stateless/Stateful MCP on ECS** — Node.js and Python variants
- **Strands Agent on Lambda** — AI Agent using Strands SDK with MCP Server
- **lambda-ops-mcp-server** — local MCP server for Lambda operations
- Demonstrates trade-offs between stateful and stateless architectures with session management

### awslabs/run-model-context-protocol-servers-with-aws-lambda (stdio-to-Lambda Bridge)

| Server | Stars | Language | License | Transports |
|--------|-------|----------|---------|------------|
| [run-mcp-servers-with-lambda](https://github.com/awslabs/run-model-context-protocol-servers-with-aws-lambda) | 378 | Python/TypeScript | Apache-2.0 | 4 |

**Run any existing stdio-based MCP server on Lambda** — wraps local MCP servers into Lambda functions accessible via HTTPS:

- **Four deployment options** — MCP Streamable HTTP via API Gateway (OAuth), Bedrock AgentCore Gateway, Lambda function URLs with SigV4 auth, direct Lambda Invoke API
- **Complete lifecycle management** — each invocation handles startup, initialization, request forwarding, response, and shutdown
- **Very active** — 1,807 commits, available on both PyPI and npm
- **IDE compatible** — works with Cursor, Cline, and Claude Desktop

### danilop/MCP2Lambda (Lambda-to-LLM Bridge)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [MCP2Lambda](https://github.com/danilop/MCP2Lambda) | 109 | Python | MIT | Auto-discovered |

**Run any Lambda function as an LLM tool without code changes:**

- **Two modes** — pre-discovery (registers functions as individual tools) and generic mode (two universal tools for any function)
- **Security by design** — models invoke Lambda functions but cannot directly access AWS services (segregation of duties)
- **Auto-discovery** — finds Lambda functions matching configurable naming patterns (default prefix: `mcp2lambda-`)
- **Compatible** with Claude Desktop and Amazon Bedrock

### fredericbarthelet/middy-mcp (Middleware)

| Server | Stars | Language | License | Integrations |
|--------|-------|----------|---------|--------------|
| [middy-mcp](https://github.com/fredericbarthelet/middy-mcp) | 40 | TypeScript | MIT | 3 |

**Middy middleware for hosting MCP servers on Lambda** — integrates with the popular Middy framework (v6.0.0+):

- v0.1.6 latest (8 releases total)
- Supports API Gateway v1 (REST), v2 (HTTP API), and ALB proxy integrations
- MCP protocol version 2025-03-26 and later
- Requires Node.js 18+

### eleva/serverless-mcp-server (Serverless Framework Template)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [serverless-mcp-server](https://github.com/eleva/serverless-mcp-server) | 17 | JavaScript | MIT | Example |

A **minimal MCP server template** deployed on AWS Lambda via API Gateway using the Serverless Framework. One-command AWS deployment, local development via serverless-offline, built on middy-mcp middleware.

### cyclimse/mcp-scaleway-functions (Scaleway Functions) *(New)*

| Server | Stars | Language | License | Features |
|--------|-------|----------|---------|----------|
| [mcp-scaleway-functions](https://github.com/cyclimse/mcp-scaleway-functions) | 7 | — | — | Scaleway FaaS |

An **unofficial community project** for managing Scaleway serverless functions via MCP — covers deployment and management of functions on Scaleway's FaaS platform. Small but notable as one of the only non-US-hyperscaler entries in the category. *(Correction 2026-08-16: an earlier version of this entry called it "the first European cloud provider FaaS MCP server." Neither the [repo](https://github.com/cyclimse/mcp-scaleway-functions) nor its README makes that claim, and we could not independently verify it — the "first" superlative has been removed.)*

## Cloudflare Workers

### cloudflare/mcp-server-cloudflare (14 Specialized Servers)

| Server | Stars | Language | License | Servers |
|--------|-------|----------|---------|---------|
| [mcp-server-cloudflare](https://github.com/cloudflare/mcp-server-cloudflare) | 4,077 | TypeScript | Apache-2.0 | 14 |

The **most comprehensive single-provider MCP ecosystem** — 14 specialized remote MCP servers (v0.20.4):

- **Workers Bindings** — build with storage, AI, and compute primitives
- **Workers Builds** — build management and insights
- **Observability** — application logs and analytics debugging
- **Documentation** — up-to-date Cloudflare reference
- **Radar** — global Internet traffic insights, URL scanning
- **Container** — sandbox development environments
- **Browser Rendering** — web page fetching, markdown conversion, screenshots
- **Logpush** — job health summaries
- **AI Gateway** — prompt/response log search
- **Audit Logs** — query and reporting
- **DNS Analytics** — performance optimization and debugging
- **Digital Experience Monitoring** — critical application insights
- **CASB** — SaaS security misconfiguration detection
- **GraphQL** — analytics data via Cloudflare's GraphQL API

All hosted as remote MCP servers at `*.mcp.cloudflare.com` — no local installation required. Cloudflare published [enterprise MCP architecture guidance](https://blog.cloudflare.com/enterprise-mcp/) (April 14, 2026) covering centralized deployment, authentication via Cloudflare Access with SSO/MFA, and governance patterns for enterprise adoption.

### cloudflare/mcp (Token-Efficient API Access)

| Server | Stars | Language | License | Endpoints |
|--------|-------|----------|---------|-----------|
| [mcp](https://github.com/cloudflare/mcp) | 733 | TypeScript | Apache-2.0 | 2,500+ |

**The most token-efficient approach to API access — and the fastest-growing repo in the category** (263 stars in early 2026 → 733 stars as of August 2026):

- **`search`** — discover API endpoints by natural language
- **`execute`** — make authenticated API calls

Uses a "Code Mode" pattern where agents write JavaScript executed server-side. Per [Cloudflare's own post](https://blog.cloudflare.com/code-mode-mcp/), an equivalent MCP server exposing the Cloudflare API's 2,500+ endpoints as individual tools would consume **over 2 million tokens** (measured at **1.17 million tokens** via tiktoken for one representative comparison in the post); Code Mode's two-tool approach uses **roughly 1,000 tokens** instead — a 99.9% reduction. Supports Workers, KV, R2, D1, Pages, DNS, Firewall, Load Balancers, Stream, Images, and more. Single URL: `mcp.cloudflare.com/mcp`. Enterprise adoption accelerated after Cloudflare's [April 2026 MCP architecture blog post](https://blog.cloudflare.com/enterprise-mcp/). *(Correction 2026-08-16: the previous version of this entry cited a precise "1,069 tokens" figure that does not appear anywhere in Cloudflare's post — the post says "roughly 1,000 tokens." Corrected to match the source.)*

### cloudflare/workers-mcp (Worker-to-MCP Bridge)

| Server | Stars | Language | License | Features |
|--------|-------|----------|---------|----------|
| [workers-mcp](https://github.com/cloudflare/workers-mcp) | 644 | TypeScript | Apache-2.0 | Auto-conversion |

**Automatically converts TypeScript Worker methods into MCP tools** via a build step. Local Node.js proxy handles stdio transport. Now includes prominent guidance recommending Cloudflare's remote MCP server approach for new projects. Still useful for existing stdio-based workflows.

## Azure Functions

### Azure/azure-functions-mcp-extension (Official — Now GA)

| Server | Stars | Language | License | Languages |
|--------|-------|----------|---------|-----------|
| [azure-functions-mcp-extension](https://github.com/Azure/azure-functions-mcp-extension) | 38 | C# | MIT | 5 |

**Microsoft's official MCP extension for Azure Functions — reached General Availability with v1.5.0 (April 2026), now at v1.5.1:**

- **v1.3.0** (March 18, 2026) — [structured content support for tools](https://github.com/Azure/azure-functions-mcp-extension/releases/tag/1.3.0)
- **v1.4.0** (April 2, 2026) — [resource templates and prompts functionality](https://github.com/Azure/azure-functions-mcp-extension/releases/tag/1.4.0)
- **v1.5.0-preview.1** (April 3, 2026) — [fluent API for building MCP Apps](https://github.com/Azure/azure-functions-mcp-extension/releases/tag/worker-1.5.0-preview.1) with UI views, static assets, and visibility controls
- **v1.5.0 GA** (April 27, 2026) — [output schemas and breaking-change cleanup](https://github.com/Azure/azure-functions-mcp-extension/releases/tag/1.5.0) for the extension
- **v1.5.1** (June 23, 2026) — [bug-fix release](https://github.com/Azure/azure-functions-mcp-extension/releases/tag/worker-1.5.1) fixing argument conversion for array-typed tool properties
- **Streamable HTTP transport** replaces SSE (recommended for new projects)
- **On-behalf-of (OBO) authentication** — tools access downstream services using user identity via Microsoft Entra
- Samples in **C#, Python, TypeScript, Java**, and JavaScript
- **Self-hosted option** — deploy existing MCP SDK-based servers without code changes

Rapid release cadence (5 releases across roughly 3 months) signals strong investment from Microsoft.

## Google Cloud

### GoogleCloudPlatform/cloud-run-mcp (Cloud Run Deployment)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [cloud-run-mcp](https://github.com/GoogleCloudPlatform/cloud-run-mcp) | 625 | JavaScript | Apache-2.0 | 6+ |

**Deploy applications to Cloud Run via AI agents** (v1.10.0):

- **Deployment** — deploy files directly or from local folders to Cloud Run services
- **Service management** — list and describe Cloud Run services
- **Logging** — access service logs and error messages
- **Cloud Run Skills** *(new)* — leverages gcloud CLI for comprehensive Cloud Run operations through natural language prompts
- **Multi-client** — Gemini CLI, Claude Desktop, Cursor, VS Code
- **Authentication** — Google Cloud SDK credentials and OAuth
- Can itself run **on Cloud Run** for remote access with IAM auth

### googleapis/gcloud-mcp (Google Cloud CLI)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [gcloud-mcp](https://github.com/googleapis/gcloud-mcp) | 887 | TypeScript | Apache-2.0 | 66+ |

**Natural language Google Cloud management** via four MCP servers — expanded significantly:

- **gcloud** — CLI interaction for any Google Cloud operation (1 tool)
- **observability** — logs, metrics, and traces querying (11 tools)
- **storage** — GCS bucket and object management (25 tools)
- **backupdr** — backup and disaster recovery (30+ tools)

The `gcloud` package reached v0.5.1 on April 28, 2026 and has since progressed to [v0.5.3](https://github.com/googleapis/gcloud-mcp/releases/tag/gcloud-mcp-v0.5.3); the monorepo now has 260 commits total — very active development. Permission controls restrict dangerous commands. Service account impersonation for least-privilege operations. Supports Gemini CLI, Claude Desktop, Cursor, and VS Code. *(Correction 2026-08-16: commit count updated from 238 to the current 260; the previously-cited "25 releases" figure could not be re-verified and has been removed rather than restated unchecked.)*

## Vercel

### vercel/mcp-handler (Framework Adapter)

| Server | Stars | Language | License | Frameworks |
|--------|-------|----------|---------|------------|
| [mcp-handler](https://github.com/vercel/mcp-handler) | 647 | TypeScript | Apache-2.0 | Next.js, Nuxt |

**The official Vercel adapter for building MCP servers** on serverless frameworks — now at [v2.1.1](https://github.com/vercel/mcp-handler/releases/tag/v2.1.1) (August 2026), up from v1.1.0 (March 2026); [v2.0.0](https://github.com/vercel/mcp-handler/releases/tag/v2.0.0) shipped July 29, 2026 with breaking changes:

- **Next.js 13+** and **Nuxt 3+** support
- **Streamable HTTP** and **SSE** transports
- Optional **Redis** for SSE resumability
- **Zod** schema validation for type-safe tool definitions
- 137 commits — actively maintained
- Compatible with Claude Desktop, Cursor, and Windsurf

*Correction (2026-08-16): the previous version of this entry listed v1.1.0/127 commits/29 releases as current. The repo shipped a v2.0.0 major release with breaking changes on 2026-07-29 and is now at v2.1.1; commit count corrected to the current 137. The "29 releases" figure could not be re-verified and has been dropped.*

Ideal for teams building MCP servers as part of their Next.js or Nuxt applications.

### Quegenx/vercel-mcp-server (Deployment Management)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [vercel-mcp-server](https://github.com/Quegenx/vercel-mcp-server) | 62 | TypeScript | — | 20+ |

**Manage Vercel infrastructure via AI assistants:**

- Team and project management
- Deployment creation, monitoring, and rollbacks
- Domain and DNS configuration
- Environment variables and Edge Config
- Access control and security tools
- Log drains, webhooks, and artifact management

## Firebase

### gannonh/firebase-mcp (Firebase Services)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [firebase-mcp](https://github.com/gannonh/firebase-mcp) | 248 | TypeScript | MIT | 10+ |

**Full Firebase platform access for AI assistants:**

- **Firestore** — CRUD operations, composite queries, collection group queries
- **Cloud Storage** — file upload from content or URLs, metadata retrieval
- **Firebase Auth** — user management and verification
- **HTTP transport** — standalone server mode for multiple concurrent clients
- **Emulator support** — full testing with local Firebase emulators

201 commits — actively maintained with comprehensive documentation.

## Serverless MCP Frameworks

### fiberplane/mcp-lite (Zero-Dependency Framework)

| Server | Stars | Language | License | Runtimes |
|--------|-------|----------|---------|----------|
| [mcp-lite](https://github.com/fiberplane/mcp-lite) | 116 | TypeScript | — | 5+ |

**A lightweight, fetch-first MCP framework** designed for serverless and edge deployments:

- **Zero runtime dependencies** — minimal core package
- **Standard Schema validators** — Zod, Valibot, Effect, ArkType for type-safe tool definitions
- **HTTP + SSE transport** built on the Fetch API
- **Adapter pattern** — opt-in session and client request management (InMemory adapters included)
- **Modular composition** via `.group()` for tool namespacing
- **DNS rebinding protection** via `allowedHosts` and `allowedOrigins`
- Runs on **Node, Bun, Cloudflare Workers, Deno**, and **Supabase Edge Functions**

### mahmoudfazeli/cloudflare-mcp-template (Plugin Template)

| Server | Stars | Language | License | Features |
|--------|-------|----------|---------|----------|
| [cloudflare-mcp-template](https://github.com/mahmoudfazeli/cloudflare-mcp-template) | 2 | TypeScript | MIT | OAuth 2.1 |

A **reusable template for building serverless MCP servers** with a provider plugin architecture. OAuth 2.1 Dynamic Client Registration, deployable to Cloudflare Workers or Vercel, production-ready with environment-specific naming and SemVer tracking.

## What's Missing

Despite strong coverage from major cloud providers, gaps are narrowing but persist:

- **No unified multi-cloud serverless management** — no single MCP server spans AWS Lambda, Azure Functions, Cloud Functions, and Cloudflare Workers from one interface
- **No serverless cost optimization** — no billing analysis, right-sizing recommendations, or cost anomaly detection for serverless workloads
- **No cold start analysis** — no performance benchmarking or cold start monitoring tools
- **No open-source FaaS support** — no OpenFaaS, Knative, or Fission MCP servers (Scaleway is the only non-hyperscaler entry)
- **Serverless CI/CD improving** — AWS agent plugins reference pipeline integration, but direct triggers remain limited
- **Serverless composition improving** — Azure fluent API for MCP Apps, AWS agent plugins reference Step Functions, but dedicated workflow management tools are still minimal
- **No edge function monitoring** — cross-provider performance comparison is absent

## Bottom Line

**Rating: 4.5/5** — Serverless MCP servers have crossed from "rapidly maturing" to "enterprise production-ready." AWS dominates with a three-tier ecosystem: official monorepo (9,604 stars), agent plugins (863 stars), and reference samples (243 stars) — no other category has this depth. Cloudflare's Code Mode pattern (733 stars, up from 263 in early 2026) is the fastest-growing approach for token-efficient API access. Azure Functions MCP reached GA with fluent API, OBO auth, and continues rapid patch releases (v1.5.1 as of June 2026). Google Cloud gcloud-mcp expanded to 66+ tools across 260 commits. Streamable HTTP has replaced SSE as the standard transport across AWS and Azure. Vercel provides the best developer experience for Next.js/Nuxt teams, now on a v2.x major release. The main gaps — cross-cloud management, cost optimization, and open-source FaaS platform support — are narrowing but not yet closed.

*This review was last edited on 2026-08-16 using Claude Sonnet 5 (Anthropic). Originally published 2026-03-16.*

