# Serverless & FaaS MCP Servers — AWS Lambda, Cloudflare Workers, Azure Functions, Google Cloud Run, Vercel, Firebase, and More

> Serverless and FaaS MCP servers help AI agents deploy, manage, and invoke serverless functions across major cloud platforms via the Model Context Protocol.


Serverless and FaaS (Function-as-a-Service) MCP servers let AI assistants deploy, invoke, and manage serverless functions across major cloud platforms through the Model Context Protocol. Instead of navigating cloud consoles or memorizing CLI commands, AI agents can manage serverless infrastructure conversationally.

This review covers the **serverless and FaaS** ecosystem — AWS Lambda tools, Cloudflare Workers integration, Azure Functions support, Google Cloud Run deployment, Vercel adapters, Firebase services, and serverless MCP frameworks. For related servers, see our [Cloud Platform review](/reviews/cloud-storage-mcp-servers/) and [Container/Docker/Kubernetes review](/reviews/container-docker-kubernetes-mcp-servers/).

The headline findings: **AWS has the most comprehensive serverless MCP ecosystem** with 14+ official servers in its monorepo (8,500 stars). **Cloudflare leads in remote MCP hosting** with 16 specialized servers and a uniquely token-efficient API pattern covering 2,500+ endpoints through just two tools. **Every major cloud provider now has official MCP support** for their serverless platform. Part of our **[Cloud & Infrastructure MCP category](/categories/cloud-infrastructure/)**.

## AWS Lambda & Serverless

### awslabs/mcp — AWS Serverless MCP Server (Official)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [AWS Serverless MCP Server](https://github.com/awslabs/mcp) | 8,500 | Python/TypeScript | Apache-2.0 | 14+ servers |

The **official AWS MCP monorepo** includes dedicated serverless servers:

- **AWS Serverless MCP Server** — complete serverless application lifecycle management via SAM CLI — build, deploy, test, and debug serverless applications
- **Lambda Tool MCP Server** — expose any Lambda function as an MCP tool for AI agents to invoke without code changes
- **AWS IaC MCP Server** — CloudFormation and CDK infrastructure toolkit
- **14+ additional servers** — EKS, ECS, CloudFormation, documentation, support, and more

Enterprise authentication options: API Gateway with OAuth (Cognito/Okta/Auth0), Bedrock AgentCore Gateway, Lambda function URLs with SigV4, and direct Lambda Invoke API.

### awslabs/run-model-context-protocol-servers-with-aws-lambda (stdio-to-Lambda Bridge)

| Server | Stars | Language | License | Transports |
|--------|-------|----------|---------|------------|
| [run-mcp-servers-with-lambda](https://github.com/awslabs/run-model-context-protocol-servers-with-aws-lambda) | 350 | Python/TypeScript | Apache-2.0 | 4 |

**Run any existing stdio-based MCP server on Lambda** — wraps local MCP servers into Lambda functions accessible via HTTPS:

- **Four deployment options** — API Gateway with OAuth, Bedrock AgentCore Gateway, Lambda function URLs with SigV4 auth, direct Lambda Invoke API
- **Complete lifecycle management** — each invocation handles startup, initialization, request forwarding, response, and shutdown
- **Multi-language** — supports Python and TypeScript MCP server ecosystems
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
| [middy-mcp](https://github.com/fredericbarthelet/middy-mcp) | 38 | TypeScript | MIT | 3 |

**Middy middleware for hosting MCP servers on Lambda** — integrates with the popular Middy framework (v6.0.0+):

- Supports API Gateway v1 (REST), v2 (HTTP API), and ALB proxy integrations
- MCP protocol version 2025-03-26 and later
- Pairs with `@middy/http-error-handler` for error management
- Requires Node.js 18+

### eleva/serverless-mcp-server (Serverless Framework Template)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [serverless-mcp-server](https://github.com/eleva/serverless-mcp-server) | 18 | JavaScript | MIT | Example |

A **minimal MCP server template** deployed on AWS Lambda via API Gateway using the Serverless Framework. One-command AWS deployment, local development via serverless-offline, built on middy-mcp middleware. Good starting point for custom Lambda-hosted MCP servers.

## Cloudflare Workers

### cloudflare/mcp-server-cloudflare (16 Specialized Servers)

| Server | Stars | Language | License | Servers |
|--------|-------|----------|---------|---------|
| [mcp-server-cloudflare](https://github.com/cloudflare/mcp-server-cloudflare) | 3,500 | TypeScript | Apache-2.0 | 16 |

The **most comprehensive single-provider MCP ecosystem** — 16 specialized remote MCP servers:

- **Workers Bindings** — build with storage, AI, and compute primitives
- **Workers Builds** — build management and insights
- **Observability** — application logs and analytics debugging
- **Documentation** — up-to-date Cloudflare reference
- **Radar** — global Internet traffic insights, URL scanning
- **Container** — sandbox development environments
- **Browser Rendering** — web page fetching, markdown conversion, screenshots
- **Logpush** — job health summaries
- **AI Gateway** — prompt/response log search
- **AutoRAG** — document search across RAG indexes
- **Audit Logs** — query and reporting
- **DNS Analytics** — performance optimization and debugging
- **Digital Experience Monitoring** — critical application insights
- **CASB** — SaaS security misconfiguration detection
- **GraphQL** — analytics data via Cloudflare's GraphQL API

All hosted as remote MCP servers at `*.mcp.cloudflare.com` — no local installation required.

### cloudflare/mcp (Token-Efficient API Access)

| Server | Stars | Language | License | Endpoints |
|--------|-------|----------|---------|-----------|
| [mcp](https://github.com/cloudflare/mcp) | 263 | TypeScript | Apache-2.0 | 2,500+ |

**The most token-efficient approach to API access** — covers 2,500+ Cloudflare API endpoints through just two tools:

- **`search`** — discover API endpoints by natural language
- **`execute`** — make authenticated API calls

Uses a "Code Mode" pattern where agents write JavaScript executed server-side. Reduces token consumption from ~2 million (raw OpenAPI spec) to just **1,069 tokens**. Supports Workers, KV, R2, D1, Pages, DNS, Firewall, Load Balancers, Stream, Images, and more. Single URL: `mcp.cloudflare.com/mcp`.

### cloudflare/workers-mcp (Worker-to-MCP Bridge)

| Server | Stars | Language | License | Features |
|--------|-------|----------|---------|----------|
| [workers-mcp](https://github.com/cloudflare/workers-mcp) | 627 | TypeScript | Apache-2.0 | Auto-conversion |

**Automatically converts TypeScript Worker methods into MCP tools** via a build step. Local Node.js proxy handles stdio transport. Exposes custom functions, APIs, or any Cloudflare service to Claude Desktop, Cursor, or other MCP clients.

## Azure Functions

### Azure/azure-functions-mcp-extension (Official)

| Server | Stars | Language | License | Languages |
|--------|-------|----------|---------|-----------|
| [azure-functions-mcp-extension](https://github.com/Azure/azure-functions-mcp-extension) | 32 | C# | MIT | 4 |

**Microsoft's official MCP extension for Azure Functions:**

- Enables Azure Functions apps to act as **scalable remote MCP servers**
- **MCP tool trigger** for defining tools usable by AI agents
- Dedicated integration for **.NET isolated worker model**
- Configurable via `host.json` (server name, version, instructions)
- Samples in **C#, Python, TypeScript, and Java**
- **Self-hosted option** — deploy existing MCP SDK-based servers without code changes

Lower star count reflects newer release — the extension is production-quality backed by Microsoft.

## Google Cloud

### GoogleCloudPlatform/cloud-run-mcp (Cloud Run Deployment)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [cloud-run-mcp](https://github.com/GoogleCloudPlatform/cloud-run-mcp) | 559 | JavaScript | Apache-2.0 | 6+ |

**Deploy applications to Cloud Run via AI agents:**

- **Deployment** — deploy files directly or from local folders to Cloud Run services
- **Service management** — list and describe Cloud Run services
- **Logging** — access service logs and error messages
- **Multi-client** — Gemini CLI, Claude Desktop, Cursor, VS Code
- **Authentication** — Google Cloud SDK credentials and OAuth
- Can itself run **on Cloud Run** for remote access with IAM auth

### googleapis/gcloud-mcp (Google Cloud CLI)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [gcloud-mcp](https://github.com/googleapis/gcloud-mcp) | 706 | TypeScript | Apache-2.0 | 40+ |

**Natural language Google Cloud management** via four MCP servers:

- **gcloud** — CLI interaction for any Google Cloud operation
- **observability** — logs, metrics, and traces querying
- **storage** — GCS bucket and object management
- **backupdr** — backup and disaster recovery

Permission controls restrict dangerous commands. Service account impersonation for least-privilege operations. Supports Gemini CLI, Claude Desktop, Cursor, and VS Code. Currently in preview.

## Vercel

### vercel/mcp-handler (Framework Adapter)

| Server | Stars | Language | License | Frameworks |
|--------|-------|----------|---------|------------|
| [mcp-handler](https://github.com/vercel/mcp-handler) | 573 | TypeScript | Apache-2.0 | Next.js, Nuxt |

**The official Vercel adapter for building MCP servers** on serverless frameworks:

- **Next.js 13+** and **Nuxt 3+** support
- **Streamable HTTP** and **SSE** transports
- Optional **Redis** for SSE resumability
- **Zod** schema validation for type-safe tool definitions
- Compatible with Claude Desktop, Cursor, and Windsurf
- Requires `@modelcontextprotocol/sdk` 1.25.2+ (security fix)

Ideal for teams building MCP servers as part of their Next.js or Nuxt applications.

### Quegenx/vercel-mcp-server (Deployment Management)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [vercel-mcp-server](https://github.com/Quegenx/vercel-mcp-server) | 60 | TypeScript | — | 20+ |

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
| [firebase-mcp](https://github.com/gannonh/firebase-mcp) | 241 | TypeScript | MIT | 10+ |

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
| [mcp-lite](https://github.com/fiberplane/mcp-lite) | 99 | TypeScript | — | 5+ |

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

Despite strong coverage from major cloud providers, several gaps remain:

- **No unified multi-cloud serverless management** — no single MCP server spans AWS Lambda, Azure Functions, Cloud Functions, and Cloudflare Workers
- **No serverless cost optimization** — no billing analysis, right-sizing recommendations, or cost anomaly detection for serverless workloads
- **No cold start analysis** — no performance benchmarking or cold start monitoring tools
- **No open-source FaaS support** — no OpenFaaS, Knative, or Fission MCP servers
- **No serverless CI/CD integration** — no direct pipeline triggers on function deploy
- **Limited function versioning** — alias management and canary deployments are underserved
- **No serverless composition** — Step Functions and Durable Functions management is minimal
- **No edge function monitoring** — cross-provider performance comparison is absent

## Bottom Line

**Rating: 4/5** — Serverless MCP servers represent a rapidly maturing category where every major cloud provider is investing heavily. AWS leads with the most comprehensive ecosystem — a 14+ server monorepo, Lambda bridge tools, and middleware options. Cloudflare stands out with 16 specialized remote MCP servers and the most token-efficient API access pattern in the entire MCP ecosystem (2,500+ endpoints through two tools). Google and Microsoft have official support but with smaller communities so far. Vercel provides the best developer experience for Next.js/Nuxt teams. The main gaps are in cross-cloud management, cost optimization, and open-source FaaS platform support — areas that will likely see development as enterprise serverless adoption continues to grow.

*This review was last edited on 2026-03-16 using Claude Opus 4.6 (Anthropic).*

