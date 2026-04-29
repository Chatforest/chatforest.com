---
title: "Serverless & FaaS MCP Servers — AWS Lambda, Cloudflare Workers, Azure Functions, Google Cloud Run, Vercel, Firebase, and More"
date: 2026-03-16T22:00:00+09:00
description: "Serverless and FaaS MCP servers help AI agents deploy, manage, and invoke serverless functions across major cloud platforms via the Model Context Protocol."
og_description: "Serverless & FaaS MCP servers: awslabs/mcp (8,900 stars — official AWS serverless toolkit + MCP Lambda Handler), cloudflare/mcp-server-cloudflare (3,700 stars — 14 Cloudflare MCP servers), cloudflare/mcp SURGED 263→412 stars (Code Mode 2,500+ endpoints), gcloud-mcp (761 stars — 66+ tools), vercel/mcp-handler (592 stars), cloud-run-mcp (598 stars + Cloud Run Skills). NEW aws-samples/sample-serverless-mcp-servers (233 stars, 9 deployment patterns), NEW awslabs/agent-plugins (634 stars, aws-serverless plugin). Azure Functions MCP GA v1.5.0. 30+ servers reviewed. Rating: 4.5/5."
content_type: "Review"
card_description: "Serverless and FaaS MCP servers for AI-powered function deployment, invocation, and management across AWS Lambda, Cloudflare Workers, Azure Functions, Google Cloud Run, Vercel, and Firebase. **The official AWS serverless toolkit** — awslabs/mcp (8,900 stars, Python/TypeScript, Apache-2.0) includes the AWS Serverless MCP Server for complete serverless application lifecycle management via SAM CLI, plus the Lambda Tool MCP Server that exposes Lambda functions as MCP tools. New MCP Lambda Handler library (on PyPI) for serverless HTTP handlers with pluggable session management (NoOp or DynamoDB). SSE transport removed across all servers in favor of Streamable HTTP. Enterprise-grade with API Gateway OAuth, Bedrock AgentCore Gateway, and IAM authentication. **NEW: AWS Agent Plugins** — awslabs/agent-plugins (634 stars, Feb 2026) packages AWS expertise into 6 compound plugins including aws-serverless (combining MCP servers, agent skills, hooks, and reference docs). Works with Claude Code, Codex, and Cursor. **NEW: AWS Serverless MCP Samples** — aws-samples/sample-serverless-mcp-servers (233 stars) provides 9 reference implementations: stateless MCP on Lambda (Node.js/Python), stateless/stateful MCP on ECS, Strands Agent on Lambda, and lambda-ops-mcp-server. **Run any stdio MCP server on Lambda** — awslabs/run-model-context-protocol-servers-with-aws-lambda (362 stars, Python/TypeScript, Apache-2.0) wraps existing stdio-based MCP servers into Lambda functions. Now supports MCP Streamable HTTP transport via API Gateway. 1,562 commits — very actively maintained. Compatible with Cursor, Cline, and Claude Desktop. **Lambda-to-LLM bridge** — danilop/MCP2Lambda (110 stars, Python, MIT) runs any AWS Lambda function as an LLM tool without code changes. Two modes: pre-discovery (registers functions as individual tools at startup) and generic mode (two universal tools). Security architecture enforces separation of duties — models invoke functions but cannot access AWS services directly. Auto-discovers Lambda functions matching configurable naming patterns (default prefix: mcp2lambda-). Compatible with Claude Desktop and Amazon Bedrock. **Middy middleware for Lambda MCP** — fredericbarthelet/middy-mcp (39 stars, TypeScript, MIT) integrates MCP server hosting into AWS Lambda via the popular Middy middleware framework (v6.0.0+). v0.1.6 latest. Supports API Gateway v1/v2 and ALB proxy integrations. **Cloudflare's comprehensive MCP ecosystem** — cloudflare/mcp-server-cloudflare (3,700 stars, TypeScript, Apache-2.0) provides 14 specialized remote MCP servers across Cloudflare services: Documentation, Workers Bindings, Workers Builds, Observability, Radar, Container, Browser Rendering, Logpush, AI Gateway, Audit Logs, DNS Analytics, Digital Experience Monitoring, CASB, and GraphQL. All hosted as remote MCP servers at *.mcp.cloudflare.com. v0.20.4 latest. Cloudflare published enterprise MCP architecture guidance (April 2026) covering authentication via Cloudflare Access with SSO/MFA, centralized server deployment, and governance patterns. **Token-efficient Cloudflare API access SURGED** — cloudflare/mcp (412 stars — up 57% from 263, TypeScript, Apache-2.0) covers 2,500+ Cloudflare API endpoints through just two tools (search and execute), reducing token consumption from ~2 million to 1,069 tokens via Code Mode. The fastest-growing repo in the category. Supports Workers, KV, R2, D1, Pages, DNS, Firewall, Load Balancers, Stream, Images, AI Gateway, Vectorize, Access. Single URL: mcp.cloudflare.com/mcp. **Worker-to-MCP bridge** — cloudflare/workers-mcp (634 stars, TypeScript, Apache-2.0) converts TypeScript Worker methods into MCP tools via a build step. Now includes guidance recommending remote MCP servers over local implementations. **Azure Functions MCP extension GA** — Azure/azure-functions-mcp-extension (35 stars, C#, MIT) reached General Availability with v1.5.0 (April 2026). Major updates: v1.3.0 structured content support, v1.4.0 resource templates and prompts, v1.5.0-preview.1 fluent API for building MCP Apps with UI views and static assets, v1.5.0 GA output schemas and prompt argument validation. Streamable HTTP transport replaces SSE. On-behalf-of (OBO) authentication with Microsoft Entra. Samples in C#, Python, TypeScript, and Java. **Deploy to Google Cloud Run** — GoogleCloudPlatform/cloud-run-mcp (598 stars, JavaScript, Apache-2.0) enables AI agents to deploy applications to Cloud Run. v1.10.0 latest. New Cloud Run Skills feature leverages gcloud CLI for comprehensive operations through natural language. Works with Gemini CLI, Claude Desktop, Cursor, VS Code. IAM authentication and OAuth. Can itself run on Cloud Run for remote access. **Google Cloud CLI via MCP** — googleapis/gcloud-mcp (761 stars, TypeScript, Apache-2.0) expanded to 66+ tools across four MCP servers: gcloud (CLI interaction), observability (11 tools — logs/metrics/traces), storage (25 tools — bucket/object management), and backupdr (30+ tools). v0.5.1 (April 28, 2026) with 238 commits and 25 releases — very active development. **Vercel MCP adapter** — vercel/mcp-handler (592 stars, TypeScript, Apache-2.0) is an adapter for building MCP servers on Next.js 13+ and Nuxt 3+. v1.1.0 (March 2026). Supports Streamable HTTP and SSE transports with optional Redis for SSE resumability. Full TypeScript support with Zod schema validation. **Vercel deployment management** — Quegenx/vercel-mcp-server (61 stars, TypeScript) lets AI assistants manage Vercel infrastructure: team/project management, deployment creation/monitoring, domain/DNS configuration, environment variables, Edge Config, access control. **Firebase services via MCP** — gannonh/firebase-mcp (244 stars, TypeScript, MIT) connects AI assistants to Firestore, Cloud Storage, and Firebase Auth. HTTP transport for multi-client connections. Emulator support for testing. 201 commits. **Lightweight serverless MCP framework** — fiberplane/mcp-lite (107 stars, TypeScript) is a zero-dependency MCP framework built on the Fetch API. Type-safe tool definitions via Standard Schema validators. Runs on Node, Bun, Cloudflare Workers, Deno, and Supabase Edge Functions. DNS rebinding protection built in. **NEW: Scaleway Functions MCP** — cyclimse/mcp-scaleway-functions (4 stars, unofficial) manages Scaleway serverless functions via MCP — the first European cloud provider FaaS MCP server. **Serverless Framework template** — eleva/serverless-mcp-server (17 stars, JavaScript, MIT) provides a minimal MCP server deployed on AWS Lambda via API Gateway using the Serverless Framework. **Cloudflare MCP template** — mahmoudfazeli/cloudflare-mcp-template (2 stars, TypeScript, MIT) is a reusable template for building serverless MCP servers with provider plugin architecture. OAuth 2.1 support. **Gaps are narrowing but persist** — no unified multi-cloud serverless management tool spanning AWS/Azure/GCP/Cloudflare from a single MCP interface. No serverless cost optimization or billing analysis tools. No cold start analysis or performance benchmarking servers. No OpenFaaS, Knative, or other open-source FaaS platform MCP servers. Serverless CI/CD pipeline integration improving via agent plugins but still limited. Step Functions/Durable Functions management is minimal but improving (Azure fluent API, AWS agent plugins reference Step Functions). No edge function performance monitoring across providers. The category earns **4.5/5** — serverless MCP servers have crossed from 'rapidly maturing' to 'enterprise production-ready.' AWS dominates with a three-tier ecosystem: official monorepo (8,900 stars), agent plugins (634 stars), and reference samples (233 stars). Cloudflare's Code Mode pattern (412 stars, +57%) is the fastest-growing approach. Azure Functions MCP reached GA with fluent API and OBO auth. Google Cloud gcloud-mcp expanded to 66+ tools with very active development. Streamable HTTP is now the standard transport across AWS and Azure."
last_refreshed: 2026-04-29
---

Serverless and FaaS (Function-as-a-Service) MCP servers let AI assistants deploy, invoke, and manage serverless functions across major cloud platforms through the Model Context Protocol. Instead of navigating cloud consoles or memorizing CLI commands, AI agents can manage serverless infrastructure conversationally.

This review covers the **serverless and FaaS** ecosystem — AWS Lambda tools, Cloudflare Workers integration, Azure Functions support, Google Cloud Run deployment, Vercel adapters, Firebase services, and serverless MCP frameworks. For related servers, see our [Cloud Platform review](/reviews/cloud-storage-mcp-servers/) and [Container/Docker/Kubernetes review](/reviews/container-docker-kubernetes-mcp-servers/).

The headline findings: **AWS dominates with a three-tier ecosystem** — official monorepo (8,900 stars), agent plugins (634 stars), and reference samples (233 stars). **Cloudflare's Code Mode pattern surged 57%** (263→412 stars) as the most token-efficient API approach. **Azure Functions MCP reached GA** with fluent API, OBO auth, and Streamable HTTP. **Google Cloud gcloud-mcp expanded to 66+ tools** across four servers. **Streamable HTTP is now the standard transport** replacing SSE across AWS and Azure. Part of our **[Cloud & Infrastructure MCP category](/categories/cloud-infrastructure/)**.

## AWS Lambda & Serverless

### awslabs/mcp — AWS Serverless MCP Server (Official)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [AWS Serverless MCP Server](https://github.com/awslabs/mcp) | 8,900 | Python/TypeScript | Apache-2.0 | 14+ servers |

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
| [agent-plugins](https://github.com/awslabs/agent-plugins) | 634 | Multi | Apache-2.0 | 6 |

**Compound agent plugins** that package AWS expertise (MCP servers + agent skills + hooks + reference docs) into installable units:

- **aws-serverless** — serverless development expertise with Lambda, API Gateway, EventBridge, Step Functions
- **deploy-on-aws** — deployment patterns and best practices
- **databases-on-aws** — database service guidance
- **sagemaker-ai**, **aws-amplify**, **amazon-location-service**

Works with Claude Code, Codex, and Cursor. Created February 2026 — rapidly adopted.

### aws-samples/sample-serverless-mcp-servers (Reference Implementations) *(New)*

| Server | Stars | Language | License | Samples |
|--------|-------|----------|---------|---------|
| [sample-serverless-mcp-servers](https://github.com/aws-samples/sample-serverless-mcp-servers) | 233 | Python/TypeScript | MIT-0 | 9 |

**9 reference implementations** demonstrating different serverless MCP deployment patterns:

- **Stateless MCP on Lambda** — Node.js and Python variants
- **Stateless/Stateful MCP on ECS** — Node.js and Python variants
- **Strands Agent on Lambda** — AI Agent using Strands SDK with MCP Server
- **lambda-ops-mcp-server** — local MCP server for Lambda operations
- Demonstrates trade-offs between stateful and stateless architectures with session management

### awslabs/run-model-context-protocol-servers-with-aws-lambda (stdio-to-Lambda Bridge)

| Server | Stars | Language | License | Transports |
|--------|-------|----------|---------|------------|
| [run-mcp-servers-with-lambda](https://github.com/awslabs/run-model-context-protocol-servers-with-aws-lambda) | 362 | Python/TypeScript | Apache-2.0 | 4 |

**Run any existing stdio-based MCP server on Lambda** — wraps local MCP servers into Lambda functions accessible via HTTPS:

- **Four deployment options** — MCP Streamable HTTP via API Gateway (OAuth), Bedrock AgentCore Gateway, Lambda function URLs with SigV4 auth, direct Lambda Invoke API
- **Complete lifecycle management** — each invocation handles startup, initialization, request forwarding, response, and shutdown
- **Very active** — 1,562 commits, available on both PyPI and npm
- **IDE compatible** — works with Cursor, Cline, and Claude Desktop

### danilop/MCP2Lambda (Lambda-to-LLM Bridge)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [MCP2Lambda](https://github.com/danilop/MCP2Lambda) | 110 | Python | MIT | Auto-discovered |

**Run any Lambda function as an LLM tool without code changes:**

- **Two modes** — pre-discovery (registers functions as individual tools) and generic mode (two universal tools for any function)
- **Security by design** — models invoke Lambda functions but cannot directly access AWS services (segregation of duties)
- **Auto-discovery** — finds Lambda functions matching configurable naming patterns (default prefix: `mcp2lambda-`)
- **Compatible** with Claude Desktop and Amazon Bedrock

### fredericbarthelet/middy-mcp (Middleware)

| Server | Stars | Language | License | Integrations |
|--------|-------|----------|---------|--------------|
| [middy-mcp](https://github.com/fredericbarthelet/middy-mcp) | 39 | TypeScript | MIT | 3 |

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
| [mcp-scaleway-functions](https://github.com/cyclimse/mcp-scaleway-functions) | 4 | — | — | Scaleway FaaS |

**The first European cloud provider FaaS MCP server** — unofficial community project for managing Scaleway serverless functions via MCP. Covers deployment and management of functions on Scaleway's FaaS platform. Small but notable as it expands the category beyond the US hyperscalers.

## Cloudflare Workers

### cloudflare/mcp-server-cloudflare (16 Specialized Servers)

| Server | Stars | Language | License | Servers |
|--------|-------|----------|---------|---------|
| [mcp-server-cloudflare](https://github.com/cloudflare/mcp-server-cloudflare) | 3,700 | TypeScript | Apache-2.0 | 14 |

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

All hosted as remote MCP servers at `*.mcp.cloudflare.com` — no local installation required. Cloudflare published enterprise MCP architecture guidance (April 2026) covering centralized deployment, authentication via Cloudflare Access with SSO/MFA, and governance patterns for enterprise adoption.

### cloudflare/mcp (Token-Efficient API Access)

| Server | Stars | Language | License | Endpoints |
|--------|-------|----------|---------|-----------|
| [mcp](https://github.com/cloudflare/mcp) | 412 | TypeScript | Apache-2.0 | 2,500+ |

**The most token-efficient approach to API access — and the fastest-growing repo in the category** (263→412 stars, +57%):

- **`search`** — discover API endpoints by natural language
- **`execute`** — make authenticated API calls

Uses a "Code Mode" pattern where agents write JavaScript executed server-side. Reduces token consumption from ~2 million (raw OpenAPI spec) to just **1,069 tokens**. Supports Workers, KV, R2, D1, Pages, DNS, Firewall, Load Balancers, Stream, Images, and more. Single URL: `mcp.cloudflare.com/mcp`. Enterprise adoption accelerated after Cloudflare's April 2026 MCP architecture blog post.

### cloudflare/workers-mcp (Worker-to-MCP Bridge)

| Server | Stars | Language | License | Features |
|--------|-------|----------|---------|----------|
| [workers-mcp](https://github.com/cloudflare/workers-mcp) | 634 | TypeScript | Apache-2.0 | Auto-conversion |

**Automatically converts TypeScript Worker methods into MCP tools** via a build step. Local Node.js proxy handles stdio transport. Now includes prominent guidance recommending Cloudflare's remote MCP server approach for new projects. Still useful for existing stdio-based workflows.

## Azure Functions

### Azure/azure-functions-mcp-extension (Official — Now GA)

| Server | Stars | Language | License | Languages |
|--------|-------|----------|---------|-----------|
| [azure-functions-mcp-extension](https://github.com/Azure/azure-functions-mcp-extension) | 35 | C# | MIT | 5 |

**Microsoft's official MCP extension for Azure Functions — reached General Availability with v1.5.0 (April 2026):**

- **v1.3.0** (March 2026) — structured content support for tools
- **v1.4.0** (April 2026) — resource templates and prompts functionality
- **v1.5.0-preview.1** — fluent API for building MCP Apps with UI views, static assets, and visibility controls
- **v1.5.0 GA** (April 27, 2026) — output schemas, validation for required prompt arguments
- **Streamable HTTP transport** replaces SSE (recommended for new projects)
- **On-behalf-of (OBO) authentication** — tools access downstream services using user identity via Microsoft Entra
- Samples in **C#, Python, TypeScript, Java**, and JavaScript
- **Self-hosted option** — deploy existing MCP SDK-based servers without code changes

Rapid release cadence (4 releases in 6 weeks) signals strong investment from Microsoft.

## Google Cloud

### GoogleCloudPlatform/cloud-run-mcp (Cloud Run Deployment)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [cloud-run-mcp](https://github.com/GoogleCloudPlatform/cloud-run-mcp) | 598 | JavaScript | Apache-2.0 | 6+ |

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
| [gcloud-mcp](https://github.com/googleapis/gcloud-mcp) | 761 | TypeScript | Apache-2.0 | 66+ |

**Natural language Google Cloud management** via four MCP servers — expanded significantly:

- **gcloud** — CLI interaction for any Google Cloud operation (1 tool)
- **observability** — logs, metrics, and traces querying (11 tools)
- **storage** — GCS bucket and object management (25 tools)
- **backupdr** — backup and disaster recovery (30+ tools)

v0.5.1 (April 28, 2026) with 238 commits and 25 releases — very active development. Permission controls restrict dangerous commands. Service account impersonation for least-privilege operations. Supports Gemini CLI, Claude Desktop, Cursor, and VS Code.

## Vercel

### vercel/mcp-handler (Framework Adapter)

| Server | Stars | Language | License | Frameworks |
|--------|-------|----------|---------|------------|
| [mcp-handler](https://github.com/vercel/mcp-handler) | 592 | TypeScript | Apache-2.0 | Next.js, Nuxt |

**The official Vercel adapter for building MCP servers** on serverless frameworks (v1.1.0, March 2026):

- **Next.js 13+** and **Nuxt 3+** support
- **Streamable HTTP** and **SSE** transports
- Optional **Redis** for SSE resumability
- **Zod** schema validation for type-safe tool definitions
- 29 releases, 127 commits — actively maintained
- Compatible with Claude Desktop, Cursor, and Windsurf

Ideal for teams building MCP servers as part of their Next.js or Nuxt applications.

### Quegenx/vercel-mcp-server (Deployment Management)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [vercel-mcp-server](https://github.com/Quegenx/vercel-mcp-server) | 61 | TypeScript | — | 20+ |

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
| [firebase-mcp](https://github.com/gannonh/firebase-mcp) | 244 | TypeScript | MIT | 10+ |

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
| [mcp-lite](https://github.com/fiberplane/mcp-lite) | 107 | TypeScript | — | 5+ |

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

**Rating: 4.5/5** — Serverless MCP servers have crossed from "rapidly maturing" to "enterprise production-ready." AWS dominates with a three-tier ecosystem: official monorepo (8,900 stars), agent plugins (634 stars), and reference samples (233 stars) — no other category has this depth. Cloudflare's Code Mode pattern (412 stars, +57%) is the fastest-growing approach for token-efficient API access. Azure Functions MCP reached GA with fluent API, OBO auth, and 4 releases in 6 weeks. Google Cloud gcloud-mcp expanded to 66+ tools with 25 releases. Streamable HTTP has replaced SSE as the standard transport across AWS and Azure. Vercel provides the best developer experience for Next.js/Nuxt teams. The main gaps — cross-cloud management, cost optimization, and open-source FaaS platform support — are narrowing but not yet closed.

*This review was last edited on 2026-04-29 using Claude Opus 4.6 (Anthropic).*
