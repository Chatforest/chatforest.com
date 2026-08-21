---
title: "MCP on Serverless: Deploying AI Agent Tools on Lambda, Cloudflare Workers, Vercel, and Beyond"
date: 2026-03-28T23:30:00+09:00
description: "A comprehensive guide to running MCP servers on serverless platforms — covering AWS Lambda, Cloudflare Workers, Vercel, Azure Functions, Google Cloud Run, Streamable HTTP"
content_type: "Guide"
card_description: "Serverless platforms can host MCP servers with scale-to-zero economics and global distribution. Here's how to deploy on Lambda, Workers, Vercel, and Azure — and where stateless MCP works (and doesn't)."
last_refreshed: 2026-08-12
sources_audited: 2026-08-12
---

MCP servers don't need to run on always-on infrastructure. The shift from SSE to Streamable HTTP transport — introduced in the March 2025 MCP specification — means MCP tool calls can work as simple HTTP request-response cycles. That's exactly what serverless platforms are built for.

AWS, Cloudflare, Vercel, Microsoft, and Google have all shipped MCP support for their serverless platforms. AWS Labs published a Lambda wrapper with 378+ stars. Cloudflare's Agents SDK includes a dedicated `McpAgent` class backed by Durable Objects. Vercel's `mcp-handler` package (645+ stars) drops MCP into Next.js projects with a few lines of code. Azure Functions has an official MCP extension, now stable and generally available after starting in public preview. Google publishes official guides for MCP hosting on Cloud Run with scale-to-zero pricing.

The appeal is obvious: pay nothing when idle, scale automatically under load, deploy globally with minimal ops. But serverless MCP has real constraints — no persistent connections for server-initiated messages, cold start latency, and no official SDK support for external session persistence. This guide covers what works, what doesn't, and how to choose the right platform for your MCP servers. Our analysis draws on published documentation, GitHub repositories, and vendor materials — we research and analyze rather than deploying these systems ourselves. [Rob Nugen](https://robnugen.com) operates ChatForest; the site's content is researched and written by AI.

## Streamable HTTP: The Transport That Enables Serverless MCP

Before March 2025, MCP's HTTP transport required Server-Sent Events (SSE) — persistent, long-lived connections where the server pushes messages to the client. This was fundamentally incompatible with serverless functions, which start, handle a request, and terminate.

The **Streamable HTTP** transport ([specification version 2025-03-26](https://modelcontextprotocol.io/specification/2025-03-26/basic/transports)) changed the game. Here's how it worked as documented in the [2025-06-18 transports spec](https://modelcontextprotocol.io/specification/2025-06-18/basic/transports), which is what most deployed servers and the platform docs cited throughout this guide still implement:

**Single endpoint architecture.** The server exposes one HTTP endpoint (e.g., `https://example.com/mcp`). Clients send JSON-RPC messages via POST. The server responds with either `application/json` (single response) or `text/event-stream` (SSE stream). No separate endpoints for different message types.

**Stateless mode.** Servers can operate fully statelessly — no session context maintained between requests. Each tool call is an independent HTTP request-response cycle, exactly like a REST API call. This is what makes serverless deployment possible.

**Optional sessions.** Servers that need state can assign a session ID via the `Mcp-Session-Id` header. But this is opt-in, not required.

**Resumability.** For servers that do stream responses, SSE event IDs and the `Last-Event-ID` header enable reconnection without losing messages.

The practical effect: a serverless function receives a POST request, executes the tool, returns JSON, and terminates. No persistent connections required.

**Update, August 2026:** the spec [went further with a release candidate dated 2026-07-28](https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/). It removes the `initialize`/`initialized` handshake and the `Mcp-Session-Id` header entirely — protocol version, client identity, and capabilities now travel with every request instead of being negotiated once, and "any MCP request can land on any server instance." The server-initiated interactions that used to justify holding an SSE stream open move to a stateless "Multi Round-Trip" pattern instead: the server returns an `InputRequiredResult` with an opaque `requestState`, and the client replies with `inputResponses` plus that same `requestState`, so any server instance can pick up the reply. In short, MCP is moving from *optionally* stateless (described above) to stateless *by default* — which is even better news for serverless than the picture painted in this guide. As of this writing the RC is only a few weeks old, and the platform SDKs and docs cited below still describe the 2025-06-18 session/resumability model; expect that to migrate over the next year as vendors adopt the new spec.

## AWS Lambda

AWS has the most mature serverless MCP ecosystem, with official libraries, sample implementations, and a managed hosting option.

### awslabs/run-model-context-protocol-servers-with-aws-lambda

| Detail | Value |
|--------|-------|
| Stars | 378+ |
| Forks | 46 |
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
| Stars | 242+ |
| Forks | 38 |
| Samples | 10 implementations |

This [sample repository](https://github.com/aws-samples/sample-serverless-mcp-servers) provides reference implementations across several patterns:

- **Stateless on Lambda** (Node.js and Python) — Lambda + API Gateway
- **Stateful on ECS** (Node.js and Python) — ECS + Application Load Balancer
- **Strands Agent on Lambda** — AI agent framework on serverless

Infrastructure templates cover Terraform, CDK, and SAM. A notable finding documented in this repo: "None of the official MCP SDKs support external session persistence (e.g. in Redis or DynamoDB)" as of mid-2025. This is a significant limitation for stateful serverless MCP.

### Amazon Bedrock AgentCore Runtime

For a fully managed option, [Amazon Bedrock AgentCore Runtime](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-mcp.html) hosts MCP servers as a service. Stateless mode (`stateless_http=True`) is the default and recommended starting point for basic servers; [as of March 2026, AgentCore Runtime also supports stateful MCP server features](https://aws.amazon.com/about-aws/whats-new/2026/03/amazon-bedrock-agentcore-runtime-stateful-mcp) — elicitation, sampling, and progress notifications — available in [14 AWS regions](https://aws.amazon.com/about-aws/whats-new/2026/03/amazon-bedrock-agentcore-runtime-stateful-mcp) at launch, with each stateful session running in its own dedicated microVM. The [AgentCore Gateway](https://aws.amazon.com/blogs/machine-learning/introducing-amazon-bedrock-agentcore-gateway-transforming-enterprise-ai-agent-tool-development/) provides a centralized tool server for MCP discovery and invocation across your MCP servers.

The tradeoff: stateful mode exists, but it's an opt-in exception, not the baseline. Design for stateless Streamable HTTP with externalized state by default, and reach for stateful mode only when a tool genuinely needs elicitation, sampling, or progress notifications.

### Lambda Constraints for MCP

- **No SSE streaming.** Lambda cannot maintain persistent SSE connections. Only Streamable HTTP with JSON responses works.
- **[15-minute (900-second) maximum runtime](https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html).** Long-running tool operations need to be designed within this limit.
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

**Key features** (see the [McpAgent API docs](https://developers.cloudflare.com/agents/model-context-protocol/apis/agent-api/)):
- **Durable Objects backing:** Per-session state persists across requests without external databases
- **WebSocket Hibernation:** Stateful servers sleep during inactivity, preserving state while consuming zero compute
- **Both transports:** Supports Streamable HTTP at `/mcp` and SSE at `/sse` automatically
- **Built-in OAuth:** OAuth Provider Library integration for authentication
- **[RPC Transport](https://developers.cloudflare.com/changelog/post/2026-02-25-agents-sdk-v0.6.0/):** For same-Worker communication (introduced in Agents SDK v0.6.0), an Agent can connect to an McpAgent via a Durable Object binding instead of an HTTP URL — no network round-trip or serialization overhead. Cloudflare marks this transport experimental.

**Stateless alternative:** For servers that don't need state, replace `McpAgent` with plain `McpServer` + `createMcpHandler()` from the SDK.

### cloudflare/mcp-server-cloudflare

| Detail | Value |
|--------|-------|
| Stars | 4,100+ |
| Forks | 476 |
| MCP Servers | 16 domain-specific servers |

The [official Cloudflare MCP server](https://github.com/cloudflare/mcp-server-cloudflare) is itself deployed on Workers. It provides 16 domain-specific MCP servers (DNS Analytics, Workers Builds, Workers Bindings, Browser Rendering, Observability, and others across Cloudflare's product line) — purpose-built tools for a specific product area each.

**Separately**, Cloudflare also runs a "[Code Mode](https://blog.cloudflare.com/code-mode-mcp/)" MCP server (launched February 20, 2026, backed by a different repo, [cloudflare/mcp](https://github.com/cloudflare/mcp), hosted at `mcp.cloudflare.com`) that takes a different approach: instead of many tools, it exposes just two — `search()` and `execute()` — and lets the model write JavaScript against the full Cloudflare OpenAPI spec (2,500+ endpoints) inside a sandboxed Workers isolate, cutting the token cost of broad API access by a claimed 99.9% versus one-tool-per-endpoint. Don't confuse the two: `mcp-server-cloudflare` is the multi-server, domain-scoped option; Code Mode is the broad-coverage, code-execution option.

### cloudflare/workers-mcp (Legacy)

[workers-mcp](https://github.com/cloudflare/workers-mcp) (644+ stars) was the earlier approach to MCP on Workers. It converts TypeScript methods into MCP tools via JSDoc comments and uses a local Node.js proxy for Claude Desktop. The README no longer recommends it for new projects — it now tells readers to "start [here](https://developers.cloudflare.com/agents/guides/remote-mcp-server/) instead — and build a **remote** MCP server," pointing to the Agents SDK as the preferred path.

### Why Workers Excel for MCP

**Near-zero cold starts.** Workers use V8 isolates, not containers. There's no JVM or Node.js runtime to boot — your code starts executing in milliseconds. For MCP tool calls where users are in an active conversation, this responsiveness matters.

**CPU-time pricing.** Cloudflare charges for CPU time, not wall-clock duration. MCP tool calls often spend most of their time waiting on external I/O (database queries, API calls). On Lambda, you pay for that wait time. On Workers, you don't.

**Free tier:** [100,000 requests/day, 10ms CPU time per invocation. Paid plan starts at $5/month.](https://developers.cloudflare.com/workers/platform/pricing/)

## Vercel

Vercel's approach integrates MCP directly into the Next.js and Nuxt frameworks that many developers already use.

### vercel/mcp-handler

| Detail | Value |
|--------|-------|
| Stars | 645+ |
| Forks | 88 |
| npm | `mcp-handler` |

The [`mcp-handler`](https://github.com/vercel/mcp-handler) package (npm package name is `mcp-handler`, not a scoped `@vercel/` name) supports **Next.js 13+** and **Nuxt 3+**, and can also be mounted in SvelteKit server routes. It handles both Streamable HTTP and SSE transports.

For Next.js, a dynamic `[transport]` route handles all MCP traffic. A `withMcpAuth` wrapper adds authorization support.

### Vercel Templates

Vercel provides clone-and-deploy templates:
- **["MCP Server on Next.js"](https://vercel.com/templates/next.js/model-context-protocol-mcp-with-next-js)** — basic MCP server with tool definitions, using the Vercel MCP Adapter
- **["MCP with Next.js and Descope"](https://vercel.com/templates/authentication/mcp-with-next-js-and-descope)** — authenticated MCP with Descope session validation

### Fluid Compute

Vercel's [Fluid Compute](https://vercel.com/docs/functions/fluid-compute) model is optimized for the bursty traffic patterns typical of AI agent interactions, with a pricing model designed to avoid paying for idle I/O wait time.

### Vercel Constraints

- **Timeout limits:** With [Fluid Compute](https://vercel.com/docs/fluid-compute) (the default for new projects since April 23, 2025), [default and maximum duration is 300 seconds (5 minutes) on Hobby; Pro and Enterprise default to 300 seconds with an 800-second maximum, and a 30-minute (1,800s) extended maximum is available in beta for supported Node.js/Python runtimes](https://vercel.com/docs/functions/configuring-functions/duration#duration-limits). (Older guidance citing a 10s Hobby / 60s Pro limit predates Fluid Compute and is no longer accurate.) The `maxDuration` setting is still worth setting explicitly for MCP tools that call slow APIs.
- **Cold starts:** 1–3 seconds typically.
- **Best for:** Teams already on Next.js who want to add MCP tools alongside their existing application without separate infrastructure.

## Azure Functions

Microsoft entered the serverless MCP space with an official extension that [began public preview in April 2025](https://www.nuget.org/packages/Microsoft.Azure.Functions.Worker.Extensions.Mcp/1.0.0-preview.1) and reached general availability with the [1.0.0 stable release in October 2025](https://www.nuget.org/packages/Microsoft.Azure.Functions.Worker.Extensions.Mcp/1.0.0).

### Microsoft MCP Extension

| Detail | Value |
|--------|-------|
| NuGet | [`Microsoft.Azure.Functions.Worker.Extensions.Mcp`](https://www.nuget.org/packages/Microsoft.Azure.Functions.Worker.Extensions.Mcp) |
| Latest | 1.6.0 (stable, July 2026) |
| Languages | .NET, Java, JavaScript, Python, TypeScript |

The [Azure Functions MCP extension](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-mcp) supports stateless Streamable HTTP. The Node.js approach uses `StreamableHTTPServerTransport` with Express, setting `sessionIdGenerator: undefined` for stateless operation.

A self-hosted option lets you deploy existing MCP SDK-based servers without code changes. In .NET, `builder.EnableMcpToolMetadata()` exposes tool metadata to LLM clients.

**Free tier (Flex Consumption):** [a monthly free grant of 250,000 executions and 100,000 GB-seconds of resource consumption per subscription.](https://azure.microsoft.com/pricing/details/functions/) Scales to zero when idle.

**Limitation:** Stateless servers only — legacy SSE not supported.

## Google Cloud Run

Google recommends **Cloud Run** over Cloud Functions for MCP server hosting. Cloud Run supports both containerized and source-based deployments with scale-to-zero pricing.

An official guide, ["Build and Deploy a Remote MCP Server to Google Cloud Run in Under 10 Minutes,"](https://cloud.google.com/blog/topics/developers-practitioners/build-and-deploy-a-remote-mcp-server-to-google-cloud-run-in-under-10-minutes) covers the basics, alongside [Google's own tutorial docs](https://docs.cloud.google.com/run/docs/tutorials/deploy-remote-mcp-server). Cloud Run supports both SSE and Streamable HTTP transports, handles Node.js and Python deployments, and includes built-in security via Cloud Run Invoker IAM roles.

**Free tier:** [2 million requests/month, 180,000 vCPU-seconds, and 360,000 GiB-seconds of memory.](https://cloud.google.com/run/pricing)

Cloud Run sits between pure serverless (Lambda, Workers) and container platforms (ECS, Kubernetes). It offers longer execution times and container flexibility while still supporting scale-to-zero.

## Other Platforms

### Fly.io

[Fly.io](https://fly.io/docs/blueprints/remote-mcp-servers/) offers experimental MCP support through `flyctl mcp` commands (`proxy`, `wrap`, `server`). Their Machines are lightweight VMs rather than functions, enabling a **single-tenant pattern** where each user gets a separate app. Unused Machines stop and start on demand.

The documentation notes: "MCP implementation is experimental and may still have sharp edges." Fly.io's `fly-replay` handles request routing, and `ssokenizer` manages OAuth token exchange.

### Prefect Horizon (formerly FastMCP Cloud)

**Update:** what this guide originally described as "FastMCP Cloud" has been folded into [Prefect Horizon](https://horizon.prefect.io/) — `fastmcp.cloud` now permanently redirects there. The free-hosting tier for personal FastMCP Python servers lives on as "Horizon Deploy": [connect a GitHub repo, point it at your server's entrypoint (e.g. `main.py:mcp`), and Horizon clones, builds, and deploys it to a `*.fastmcp.app` URL in under 60 seconds](https://gofastmcp.com/deployment/prefect-horizon), redeploying automatically on pushes to main. This is a GitHub-connected build pipeline, not a literal `fastmcp deploy` CLI command. Horizon [is free for personal projects](https://gofastmcp.com/deployment/prefect-horizon). Separately, the FastMCP framework itself — maintained by the Prefect team — [says some version of it "powers 70% of MCP servers across all languages"](https://github.com/PrefectHQ/fastmcp), a self-reported figure with no independent verification found. Servers on Horizon run as dedicated processes rather than true serverless functions.

### mcphosting.io

[A free MCP hosting service](https://mcphosting.io) supporting Python (FastMCP) and Node.js servers — connect a GitHub repo and it deploys on push, with a free tier available.

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
- **Sampling** (server asks the LLM to generate text) — note this capability was [deprecated in the 2026-07-28 spec release candidate](https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/) in favor of servers integrating directly with an LLM API; it keeps working through at least 2027 during the transition
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
| **Cloudflare Workers** | [100K req/day, 10ms CPU/invocation](https://developers.cloudflare.com/workers/platform/pricing/) | CPU time only ($5/mo paid) | Don't pay for I/O wait |
| **AWS Lambda** | [1M req/month, 400K GB-sec](https://aws.amazon.com/lambda/pricing/) | Wall-clock duration | Mature ecosystem, most tools |
| **Azure Functions** | [250K executions/month, 100K GB-sec](https://azure.microsoft.com/pricing/details/functions/) (Flex Consumption) | Wall-clock duration | .NET/enterprise integration |
| **Vercel Functions** | [4 Active CPU-hrs, 360 GB-hrs memory, 1M invocations/month](https://vercel.com/docs/functions/usage-and-pricing) | Active CPU + provisioned memory | Best for Next.js teams |
| **Google Cloud Run** | [2M req/month, 180K vCPU-sec, 360K GiB-sec](https://cloud.google.com/run/pricing) | Per-request + CPU/memory | Container flexibility |
| **Fly.io** | Free tier available | VM-based usage | Single-tenant isolation |
| **Prefect Horizon (FastMCP)** | [Free for personal projects](https://gofastmcp.com/deployment/prefect-horizon) | N/A | GitHub-push deploy |
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
- **Long-running operations** — Lambda caps at 15 minutes; Vercel Pro/Enterprise cap at 800 seconds by default (1,800s with the extended-duration beta)
- **Stateful sessions** — no official SDK support for distributed session persistence
- **High-frequency tools** — consistent heavy traffic is cheaper on containers
- **Complex orchestration** — multi-step tool workflows with intermediate state need a stateful server

### Decision Framework

Ask these questions about each MCP tool:

1. **Does the tool need to push messages to the client?** If yes → containers
2. **Does the tool take more than a few minutes?** If yes → containers (or Lambda, capped at 15 minutes)
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

## The Roadmap: Stateless by Default (Update: This Already Shipped as a Release Candidate)

This guide originally framed stateless-by-default MCP as a future direction, pointing to an early proposal, [SEP-1442](https://github.com/modelcontextprotocol/modelcontextprotocol/issues/1442), for discussion. That proposal has since evolved into [SEP-2575 ("Make MCP Stateless")](https://modelcontextprotocol.io/seps/2575-stateless-mcp), and as of the [2026-07-28 specification release candidate](https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/), it has shipped: the `initialize` handshake and `Mcp-Session-Id` header are removed from the core protocol, and "any MCP request can land on any server instance" without sticky routing or a shared session store.

The direction predicted here was correct — Streamable HTTP was step one, and stateless-by-default is now real, not speculative. What the guide got wrong is the mechanism: rather than adding official SDK support for *external* session stores (Redis, DynamoDB) to prop up stateful sessions across instances, the spec instead removed protocol-level sessions altogether. Applications that still need state now carry it as an explicit, client-passed handle (e.g., a `basket_id` returned in a tool result and threaded back as an argument) rather than relying on server-side session storage. As of this writing the RC is only a few weeks old and most vendor SDKs — including the ones covered throughout this guide — still implement the 2025-06-18 session model; expect a migration period before serverless MCP servers commonly built on the new stateless core.

## Getting Started

**Fastest path (5 minutes):** Deploy to Cloudflare Workers using the Agents SDK. Near-zero cold starts, free tier, global distribution. Follow the [Cloudflare MCP documentation](https://developers.cloudflare.com/agents/model-context-protocol/).

**Most ecosystem support:** Use the [AWS Labs Lambda wrapper](https://github.com/awslabs/run-model-context-protocol-servers-with-aws-lambda) to deploy existing stdio MCP servers to Lambda without rewriting them.

**Easiest for web developers:** Add [`mcp-handler`](https://github.com/vercel/mcp-handler) to an existing Next.js project and define tools in a route handler.

**Enterprise/.NET:** Use the [Azure Functions MCP extension](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-mcp) for .NET, Java, or TypeScript MCP tools with Azure's compliance certifications.

**Managed hosting:** [Prefect Horizon](https://horizon.prefect.io/) (formerly FastMCP Cloud) offers free Python MCP server hosting deployed via a connected GitHub repo, or use [Bedrock AgentCore](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-mcp.html) for AWS-managed MCP hosting.

Whichever platform you choose, start stateless. Most MCP tools don't need sessions, and stateless servers are simpler to deploy, scale, and debug. Add state management only when your tools genuinely require server-initiated messages or multi-step workflows.

## Related Guides

- [MCP Transports Explained](/guides/mcp-transports-explained/) — deep dive into stdio, SSE, and Streamable HTTP transports
- [MCP Server Deployment and Hosting](/guides/mcp-server-deployment-hosting/) — broader hosting options beyond serverless
- [MCP Server Performance Tuning](/guides/mcp-server-performance-tuning/) — optimization techniques for production MCP servers
- [MCP Server Security](/guides/mcp-server-security/) — authentication, authorization, and security patterns
- [MCP Authorization and OAuth](/guides/mcp-authentication-oauth/) — OAuth 2.1 implementation for remote MCP servers
- [MCP Cost Optimization](/guides/mcp-cost-optimization/) — reducing token usage and infrastructure costs
- [MCP in Production](/guides/mcp-in-production/) — operational patterns for production MCP deployments
- [Build Your First MCP Server](/guides/build-your-first-mcp-server/) — getting started with MCP server development
