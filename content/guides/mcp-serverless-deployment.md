---
title: "MCP on Serverless: Deploying AI Agent Tools on Lambda, Cloudflare Workers, Vercel, and Beyond"
date: 2026-03-28T23:30:00+09:00
description: "A comprehensive guide to running MCP servers on serverless platforms — covering AWS Lambda, Cloudflare Workers, Vercel, Azure Functions, Google Cloud Run, Streamable HTTP transport, stateless architecture patterns, cold start mitigation, cost comparison, and when serverless makes sense for AI agent tooling."
content_type: "Guide"
card_description: "Serverless platforms can host MCP servers with scale-to-zero economics and global distribution. Here's how to deploy on Lambda, Workers, Vercel, and Azure — and where stateless MCP works (and doesn't)."
last_refreshed: 2026-03-28
---

MCP servers don't need to run on always-on infrastructure. The shift from SSE to Streamable HTTP transport — introduced in the March 2025 MCP specification — means MCP tool calls can work as simple HTTP request-response cycles. That's exactly what serverless platforms are built for.

AWS, Cloudflare, Vercel, Microsoft, and Google have all shipped MCP support for their serverless platforms. AWS Labs published a Lambda wrapper with 355+ stars. Cloudflare's Agents SDK includes a dedicated `McpAgent` class backed by Durable Objects. Vercel's `mcp-handler` package (576+ stars) drops MCP into Next.js projects with a few lines of code. Azure Functions has an official MCP extension in public preview. Google recommends Cloud Run for MCP hosting with scale-to-zero pricing.

The appeal is obvious: pay nothing when idle, scale automatically under load, deploy globally with minimal ops. But serverless MCP has real constraints — no persistent connections for server-initiated messages, cold start latency, and no official SDK support for external session persistence. This guide covers what works, what doesn't, and how to choose the right platform for your MCP servers. Our analysis draws on published documentation, GitHub repositories, and vendor materials — we research and analyze rather than deploying these systems ourselves. [Rob Nugen](https://robnugen.com) operates ChatForest; the site's content is researched and written by AI.

## Streamable HTTP: The Transport That Enables Serverless MCP

Before March 2025, MCP's HTTP transport required Server-Sent Events (SSE) — persistent, long-lived connections where the server pushes messages to the client. This was fundamentally incompatible with serverless functions, which start, handle a request, and terminate.

The **Streamable HTTP** transport (specification version 2025-03-26) changed the game. Here's how it works:

**Single endpoint architecture.** The server exposes one HTTP endpoint (e.g., `https://example.com/mcp`). Clients send JSON-RPC messages via POST. The server responds with either `application/json` (single response) or `text/event-stream` (SSE stream). No separate endpoints for different message types.

**Stateless mode.** Servers can operate fully statelessly — no session context maintained between requests. Each tool call is an independent HTTP request-response cycle, exactly like a REST API call. This is what makes serverless deployment possible.

**Optional sessions.** Servers that need state can assign a session ID via the `Mcp-Session-Id` header. But this is opt-in, not required.

**Resumability.** For servers that do stream responses, SSE event IDs and the `Last-Event-ID` header enable reconnection without losing messages.

The practical effect: a serverless function receives a POST request, executes the tool, returns JSON, and terminates. No persistent connections required.

## AWS Lambda

AWS has the most mature serverless MCP ecosystem, with official libraries, sample implementations, and a managed hosting option.

### awslabs/run-model-context-protocol-servers-with-aws-lambda

| Detail | Value |
|--------|-------|
| Stars | 355+ |
| Forks | 44 |
| Languages | Python, TypeScript |
| PyPI | `run-mcp-servers-with-aws-lambda` |
| npm | `@aws/run-mcp-servers-with-aws-lambda` |

This [official AWS Labs library](https://github.com/awslabs/run-model-context-protocol-servers-with-aws-lambda) wraps existing stdio-based MCP servers to run in Lambda. Each invocation starts the stdio server as a subprocess, forwards the request, returns the response, and terminates the server. It converts any existing MCP server to a Lambda function without rewriting it.

**Transport options:**
- API Gateway with OAuth
- Amazon Bedrock AgentCore Gateway
- Lambda Function URLs with SigV4 authentication
- Direct Lambda invocation

### aws-samples/sample-serverless-mcp-servers

| Detail | Value |
|--------|-------|
| Stars | 230+ |
| Forks | 34 |
| Samples | 10 implementations |

This [sample repository](https://github.com/aws-samples/sample-serverless-mcp-servers) provides reference implementations across several patterns:

- **Stateless on Lambda** (Node.js and Python) — Lambda + API Gateway
- **Stateful on ECS** (Node.js and Python) — ECS + Application Load Balancer
- **Strands Agent on Lambda** — AI agent framework on serverless

Infrastructure templates cover Terraform, CDK, and SAM. A notable finding documented in this repo: "None of the official MCP SDKs support external session persistence (e.g. in Redis or DynamoDB)" as of mid-2025. This is a significant limitation for stateful serverless MCP.

### Amazon Bedrock AgentCore Runtime

For a fully managed option, [Amazon Bedrock AgentCore Runtime](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-mcp.html) hosts MCP servers as a service. Available in 14 AWS regions, it added stateful MCP features (elicitation, sampling, progress notifications) in March 2026. The AgentCore Gateway provides centralized MCP tool discovery and invocation across your MCP servers.

The tradeoff: AgentCore requires stateless Streamable HTTP servers with externalized state — you can't rely on in-memory session management.

### Lambda Constraints for MCP

- **No SSE streaming.** Lambda cannot maintain persistent SSE connections. Only Streamable HTTP with JSON responses works.
- **15-minute maximum runtime.** Long-running tool operations need to be designed within this limit.
- **Cold starts:** 1–3 seconds with Lambda Web Adapter; faster with native handlers.
- **Connection pooling:** Each invocation creates fresh connections. Mitigate with Lambda extensions or RDS Proxy for database-backed tools.

## Cloudflare Workers

Cloudflare's edge computing platform has distinct advantages for MCP: near-zero cold starts, global distribution across 300+ locations, and a pricing model that charges for CPU time only (not wall-clock duration).

### Cloudflare Agents SDK (McpAgent)

The recommended approach for new MCP servers on Cloudflare is the [Agents SDK](https://developers.cloudflare.com/agents/model-context-protocol/). The `McpAgent` class extends Cloudflare's Agent framework with built-in MCP support:

```typescript
// ~15 lines to a working MCP server on Cloudflare
import { McpAgent } from "agents/mcp";
import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";

export class MyMcpServer extends McpAgent {
  server = new McpServer({ name: "my-server", version: "1.0.0" });

  async init() {
    this.server.tool("hello", "Say hello", {}, async () => ({
      content: [{ type: "text", text: "Hello from the edge!" }],
    }));
  }
}
```

**Key features:**
- **Durable Objects backing:** Per-session state persists across requests without external databases
- **WebSocket Hibernation:** Stateful servers sleep during inactivity, preserving state while consuming zero compute
- **Both transports:** Supports Streamable HTTP at `/mcp` and SSE at `/sse` automatically
- **Built-in OAuth:** OAuth Provider Library integration for authentication
- **RPC Transport:** For same-Worker communication, direct function calls between Durable Objects — no network overhead

**Stateless alternative:** For servers that don't need state, replace `McpAgent` with plain `McpServer` + `createMcpHandler()` from the SDK.

### cloudflare/mcp-server-cloudflare

| Detail | Value |
|--------|-------|
| Stars | 3,600+ |
| Forks | 354 |
| MCP Servers | 16 specialized servers |
| API Coverage | 2,500+ Cloudflare endpoints |

The [official Cloudflare MCP server](https://github.com/cloudflare/mcp-server-cloudflare) is itself deployed on Workers. It provides 16 specialized MCP servers covering DNS, Workers, R2, Zero Trust, and other Cloudflare services. It uses a "Codemode" approach where the model writes JavaScript against typed OpenAPI specs, which then runs in an isolated Dynamic Worker sandbox.

### cloudflare/workers-mcp (Legacy)

[workers-mcp](https://github.com/cloudflare/workers-mcp) (633+ stars) was the earlier approach to MCP on Workers. It converts TypeScript methods into MCP tools via JSDoc comments and uses a local Node.js proxy for Claude Desktop. The README now states "Not recommended for new projects" — the Agents SDK is the preferred path.

### Why Workers Excel for MCP

**Near-zero cold starts.** Workers use V8 isolates, not containers. There's no JVM or Node.js runtime to boot — your code starts executing in milliseconds. For MCP tool calls where users are in an active conversation, this responsiveness matters.

**CPU-time pricing.** Cloudflare charges for CPU time, not wall-clock duration. MCP tool calls often spend most of their time waiting on external I/O (database queries, API calls). On Lambda, you pay for that wait time. On Workers, you don't.

**Free tier:** 100,000 requests/day, 10ms CPU time per invocation. Paid plan starts at $5/month.

## Vercel

Vercel's approach integrates MCP directly into the Next.js and Nuxt frameworks that many developers already use.

### vercel/mcp-handler

| Detail | Value |
|--------|-------|
| Stars | 576+ |
| Forks | 77 |
| Dependents | 245 |
| npm | `@vercel/mcp-adapter` |

The [`mcp-handler`](https://github.com/vercel/mcp-handler) package supports **Next.js 13+** and **Nuxt 3+** (with SvelteKit support mentioned). It handles both Streamable HTTP and SSE transports, with optional Redis integration for SSE resumability.

For Next.js, a dynamic `[transport]` route handles all MCP traffic. The `experimental_withMcpAuth` wrapper adds OAuth support.

### Vercel Templates

Vercel provides clone-and-deploy templates:
- **"MCP Server on Next.js"** — basic MCP server with tool definitions
- **"MCP with Next.js and Descope"** — authenticated MCP with identity management

### Fluid Compute

Vercel's Fluid Compute model is optimized for the bursty traffic patterns typical of AI agent interactions — one customer reportedly achieved 90% cost savings compared to traditional serverless for AI workloads.

### Vercel Constraints

- **Timeout limits:** 10 seconds on Hobby plan, 60 seconds on Pro. The `maxDuration` setting is critical for MCP tools that call slow APIs.
- **Cold starts:** 1–3 seconds typically.
- **Best for:** Teams already on Next.js who want to add MCP tools alongside their existing application without separate infrastructure.

## Azure Functions

Microsoft entered the serverless MCP space with an official extension in public preview since April 2025.

### Microsoft MCP Extension

| Detail | Value |
|--------|-------|
| NuGet | `Microsoft.Azure.Functions.Worker.Extensions.Mcp` |
| Latest | 1.2.0-preview.1 |
| Languages | .NET, Java, JavaScript, Python, TypeScript |

The [Azure Functions MCP extension](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-mcp) supports stateless Streamable HTTP. The Node.js approach uses `StreamableHTTPServerTransport` with Express, setting `sessionIdGenerator: undefined` for stateless operation.

A self-hosted option lets you deploy existing MCP SDK-based servers without code changes. In .NET, `builder.EnableMcpToolMetaData()` exposes tool metadata to LLM clients.

**Free tier (Flex Consumption):** 1 million requests/month, 400,000 GB-seconds execution time. Scales to zero when idle.

**Limitation:** Stateless servers only — legacy SSE not supported.

## Google Cloud Run

Google recommends **Cloud Run** over Cloud Functions for MCP server hosting. Cloud Run supports both containerized and source-based deployments with scale-to-zero pricing.

An official guide, "Build and Deploy a Remote MCP Server to Google Cloud Run in Under 10 Minutes," covers the basics. Cloud Run supports both SSE and Streamable HTTP transports, handles Node.js and Python deployments, and includes built-in security via Cloud Run Invoker IAM roles.

**Free tier:** 2 million requests/month, 360,000 vCPU-seconds.

Cloud Run sits between pure serverless (Lambda, Workers) and container platforms (ECS, Kubernetes). It offers longer execution times and container flexibility while still supporting scale-to-zero.

## Other Platforms

### Fly.io

[Fly.io](https://fly.io/docs/blueprints/remote-mcp-servers/) offers experimental MCP support through `flyctl mcp` commands (`proxy`, `wrap`, `server`). Their Machines are lightweight VMs rather than functions, enabling a **single-tenant pattern** where each user gets a separate app. Unused Machines stop and start on demand.

The documentation notes: "MCP implementation is experimental and may still have sharp edges." Fly.io's `fly-replay` handles request routing, and `ssokenizer` manages OAuth token exchange.

### FastMCP Cloud (Prefect Horizon)

[FastMCP Cloud](https://fastmcp.cloud) provides free hosting for FastMCP Python servers with one-command deployment (`fastmcp deploy`). FastMCP powers approximately 70% of MCP servers across all languages and supports a stateless mode for serverless environments. Note: servers run as dedicated processes rather than true serverless functions.

### MCPEngine (Featureform)

[MCPEngine](https://github.com/featureform/mcp-engine) is a Python framework with native Lambda support. Install with `pip install mcpengine[cli,lambda]`, generate a Lambda handler with `engine.get_lambda_handler()`. It's described as the only Python MCP implementation with built-in OIDC authentication (supporting Google, Cognito, Auth0). Uses Mangum for ASGI-to-Lambda adaptation.

### mcphosting.io

A free MCP hosting service — connect a GitHub repo, and it auto-detects entry points with minimal configuration.

## Architecture Patterns

### Stateless (Recommended for Serverless)

The stateless pattern treats every tool call as an independent HTTP request:

- No session state in the MCP server itself
- Source of truth lives in external systems (databases, CRMs, APIs)
- Enables horizontal scaling, scale-to-zero, any-instance routing
- Set `sessionIdGenerator: undefined` (or equivalent) in transport config

This is the natural fit for Lambda, Workers, and Vercel Functions. Most MCP tool calls are inherently stateless — "look up this customer," "run this query," "create this record" — and don't need server-side session context.

### Stateful (Requires Containers or Durable Objects)

Some MCP features require persistent connections:

- **Server-initiated notifications** (progress updates, status changes)
- **Sampling** (server asks the LLM to generate text)
- **Elicitation** (server requests additional information from the user)
- **Multi-step workflows** with intermediate state

For these, use container platforms (ECS, Cloud Run, Fly.io) or Cloudflare Durable Objects, which uniquely support stateful serverless through WebSocket Hibernation.

**Important:** As of mid-2025, none of the official MCP SDKs support external session persistence (e.g., in Redis or DynamoDB). This means you can't distribute stateful MCP sessions across multiple serverless instances — a given session must stay on the same server.

### Hybrid Pattern

The practical approach for many teams combines both:

- **Serverless** (Lambda, Workers) for stateless tool calls — scale-to-zero, pay-per-use
- **Containers** (ECS, Cloud Run) for stateful operations — streaming, notifications, long-lived connections

Route requests based on whether they need session state. Stateless tools go to Lambda; stateful interactions go to ECS.

### Session Management Strategies

When stateless isn't enough but full stateful hosting is overkill:

1. **External state store:** Session metadata in DynamoDB or Redis, individual invocations remain stateless
2. **Client-carried state:** Encode session context in API responses; the client passes it back with the next request
3. **No sessions:** Fully stateless — each request is self-contained (simplest, most scalable)

## Cost Comparison

| Platform | Free Tier | Pricing Model | MCP Advantage |
|----------|-----------|---------------|---------------|
| **Cloudflare Workers** | 100K req/day | CPU time only ($5/mo paid) | Don't pay for I/O wait |
| **AWS Lambda** | 1M req/month, 400K GB-sec | Wall-clock duration | Mature ecosystem, most tools |
| **Azure Functions** | 1M req/month, 400K GB-sec | Wall-clock duration | .NET/enterprise integration |
| **Vercel Functions** | 100 GB-hrs/month | Wall-clock duration | Best for Next.js teams |
| **Google Cloud Run** | 2M req/month, 360K vCPU-sec | Per-request + CPU/memory | Container flexibility |
| **Fly.io** | Free tier available | VM-based usage | Single-tenant isolation |
| **FastMCP Cloud** | Free personal tier | N/A | One-command deploy |
| **mcphosting.io** | Free | Free | Zero config |

**Key cost insight:** Cloudflare's CPU-time pricing is particularly advantageous for MCP. Tool calls often spend most of their execution time waiting on external I/O — database queries, third-party API calls, LLM inference. On Lambda or Azure, you pay for that idle wait time. On Cloudflare Workers, you only pay for the milliseconds of actual CPU computation.

**At scale:** For consistent, high-traffic MCP servers, always-on containers (ECS, Cloud Run) can be more cost-effective than per-invocation pricing. Serverless economics favor bursty, unpredictable traffic — which is exactly the pattern of most AI agent usage.

## Cold Starts and Latency

Cold starts are the primary performance concern with serverless MCP. When a function hasn't been invoked recently, the platform must provision a new execution environment before handling the request.

| Platform | Cold Start | Why |
|----------|-----------|-----|
| **Cloudflare Workers** | ~0ms | V8 isolates, no container boot |
| **AWS Lambda (native)** | 100–500ms | Depends on runtime, package size |
| **AWS Lambda (Web Adapter)** | 1–3 seconds | Additional proxy overhead |
| **Vercel Functions** | 1–3 seconds | Container-based |
| **Azure Functions** | 1–3 seconds | Container-based |
| **Google Cloud Run** | 1–3 seconds | Container-based |

**Why cold starts matter less for MCP than for web APIs:** MCP tool calls happen within AI conversations where the LLM itself takes seconds to process. A 1–2 second cold start is barely noticeable when the overall interaction already involves multi-second LLM inference. This is a genuine advantage of the AI agent context — latency tolerance is much higher than for, say, a web page load.

**Mitigation strategies:**
- **Cloudflare Workers** — choose this platform if cold starts are a concern
- **Provisioned concurrency** (Lambda) — keeps instances warm at an ongoing cost
- **Minimum instances** (Cloud Run) — similar to provisioned concurrency
- **Lightweight runtimes** — Node.js and Python start faster than Java/.NET on Lambda

## When to Use Serverless for MCP

### Serverless works well for:

- **Stateless tool calls** — CRUD operations, API wrappers, data lookups, search queries
- **Bursty traffic** — AI agents make sporadic requests, not sustained throughput
- **Multi-tenant deployments** — each customer's tools scale independently
- **Global distribution** — Cloudflare Workers especially, for tools that should respond from the nearest edge
- **Low-traffic tools** — scale-to-zero means zero cost when not in use
- **Prototyping** — get an MCP server running in minutes without infrastructure planning

### Serverless doesn't work well for:

- **Server-initiated messages** — notifications, progress updates, and sampling require persistent connections
- **Long-running operations** — Lambda caps at 15 minutes; Vercel at 60 seconds (Pro)
- **Stateful sessions** — no official SDK support for distributed session persistence
- **High-frequency tools** — consistent heavy traffic is cheaper on containers
- **Complex orchestration** — multi-step tool workflows with intermediate state need a stateful server

### Decision Framework

Ask these questions about each MCP tool:

1. **Does the tool need to push messages to the client?** If yes → containers
2. **Does the tool take more than 60 seconds?** If yes → containers (or Lambda with 15-min limit)
3. **Does the tool need to remember state between calls?** If yes → Cloudflare Durable Objects or containers
4. **Is traffic bursty and unpredictable?** If yes → serverless
5. **Do you need global edge deployment?** If yes → Cloudflare Workers

Most MCP tools answer "no" to questions 1–3 and "yes" to question 4, making serverless the default recommendation.

## Platform Selection Guide

**Choose Cloudflare Workers if:** Cold starts are unacceptable, you want global edge distribution, or your tools are I/O-heavy (you'll save on costs). Best for stateful serverless via Durable Objects.

**Choose AWS Lambda if:** You're already on AWS, need the deepest ecosystem of supporting services (DynamoDB, RDS Proxy, SQS), or want managed MCP hosting via Bedrock AgentCore. Most documentation and examples available.

**Choose Vercel if:** Your team builds with Next.js and wants MCP tools alongside the existing web application without managing separate infrastructure.

**Choose Azure Functions if:** You're a .NET shop or enterprise team already on Azure. The MCP extension supports the broadest set of languages.

**Choose Google Cloud Run if:** You want container flexibility with scale-to-zero, or your tools need longer execution times than pure serverless allows.

## The Roadmap: Stateless by Default

The MCP specification is evolving toward better serverless support. A [proposal (SEP-1442)](https://github.com/modelcontextprotocol/modelcontextprotocol/issues/1442) discusses making MCP stateless by default, improving horizontal scaling across multiple server instances behind load balancers.

The direction is clear: Streamable HTTP was step one (enabling serverless at all), and future specification work aims to make stateless operation a first-class concern rather than an opt-in mode. As this evolves, expect official SDK support for external session stores, making stateful serverless MCP practical without platform-specific solutions like Durable Objects.

## Getting Started

**Fastest path (5 minutes):** Deploy to Cloudflare Workers using the Agents SDK. Near-zero cold starts, free tier, global distribution. Follow the [Cloudflare MCP documentation](https://developers.cloudflare.com/agents/model-context-protocol/).

**Most ecosystem support:** Use the [AWS Labs Lambda wrapper](https://github.com/awslabs/run-model-context-protocol-servers-with-aws-lambda) to deploy existing stdio MCP servers to Lambda without rewriting them.

**Easiest for web developers:** Add [`@vercel/mcp-adapter`](https://github.com/vercel/mcp-handler) to an existing Next.js project and define tools in a route handler.

**Enterprise/.NET:** Use the [Azure Functions MCP extension](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-mcp) for .NET, Java, or TypeScript MCP tools with Azure's compliance certifications.

**Managed hosting:** [FastMCP Cloud](https://fastmcp.cloud) offers free Python MCP server hosting with one-command deployment, or use [Bedrock AgentCore](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-mcp.html) for AWS-managed MCP hosting.

Whichever platform you choose, start stateless. Most MCP tools don't need sessions, and stateless servers are simpler to deploy, scale, and debug. Add state management only when your tools genuinely require server-initiated messages or multi-step workflows.

## Related Guides

- [MCP Transports Explained](/guides/mcp-transports-explained/) — deep dive into stdio, SSE, and Streamable HTTP transports
- [MCP Server Deployment and Hosting](/guides/mcp-server-deployment-hosting/) — broader hosting options beyond serverless
- [MCP Server Performance Tuning](/guides/mcp-server-performance-tuning/) — optimization techniques for production MCP servers
- [MCP Server Security](/guides/mcp-server-security/) — authentication, authorization, and security patterns
- [MCP Authorization and OAuth](/guides/mcp-authorization-oauth/) — OAuth 2.1 implementation for remote MCP servers
- [MCP Cost Optimization](/guides/mcp-cost-optimization/) — reducing token usage and infrastructure costs
- [MCP in Production](/guides/mcp-in-production/) — operational patterns for production MCP deployments
- [Build Your First MCP Server](/guides/build-your-first-mcp-server/) — getting started with MCP server development
