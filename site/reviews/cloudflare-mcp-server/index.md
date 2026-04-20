# The Cloudflare MCP Server — 2,500 API Endpoints in 1,000 Tokens

> Cloudflare's MCP server ecosystem gives AI assistants access to their entire platform — over 2,500 API endpoints across Workers, R2, D1, DNS, Zero Trust, and more.


**At a glance:** 3,600 stars (product servers) / 357 stars (Code Mode), 371 forks, ~19K npm monthly downloads, 16 specialized servers, ~122K estimated all-time PulseMCP visitors, last release March 31, 2026. Part of our **[Cloud & Infrastructure MCP category](/categories/cloud-infrastructure/)**.

The Cloudflare MCP server is the most ambitious MCP implementation we've reviewed. Instead of one server with a fixed set of tools, Cloudflare ships an entire ecosystem: a main API server that covers 2,500+ endpoints through a novel "Code Mode" approach, plus 16 specialized product servers for everything from Workers builds to DNS analytics to browser rendering.

The main server lives at `mcp.cloudflare.com/mcp` — a remote server with OAuth authentication. It exposes just two tools: `search()` and `execute()`. The agent writes JavaScript against a typed OpenAPI specification, and the code runs in a V8 sandbox. The result: access to every Cloudflare API endpoint while consuming roughly 1,000 tokens of context. A traditional MCP server exposing those same endpoints as individual tools would consume 1.17 million tokens — more than most models' entire context window.

The key question: is this code-generation approach actually practical for everyday use, or is it an impressive demo that falls apart in production workflows?

## What It Does

Cloudflare's MCP ecosystem has two layers:

### The Main API Server (Code Mode)

Two tools that cover the entire Cloudflare platform:

- `search()` — the agent writes JavaScript to query a typed representation of Cloudflare's OpenAPI specification. It can filter by product, path, tags, or metadata to find the right endpoints without loading the full spec into context.
- `execute()` — the agent writes JavaScript to make authenticated API calls using the Cloudflare API client. The code runs in a Dynamic Worker isolate — a lightweight V8 sandbox with no filesystem access and controlled network permissions.

This covers Workers, KV, R2, D1, Pages, DNS, Queues, Durable Objects, Zero Trust, WAF, DDoS protection, SSL/TLS, Load Balancing, Spectrum, Argo, and every other Cloudflare product — over 2,500 endpoints in total.

### Product-Specific Servers (16 servers)

Each has its own URL and focused toolset:

| Server | URL | Purpose |
|--------|-----|---------|
| Documentation | docs.mcp.cloudflare.com | Search Cloudflare docs |
| Workers Bindings | bindings.mcp.cloudflare.com | Build with storage, AI, compute primitives |
| Workers Builds | builds.mcp.cloudflare.com | Manage Workers CI/CD builds |
| Observability | observability.mcp.cloudflare.com | Debug with logs and analytics |
| Radar | radar.mcp.cloudflare.com | Internet traffic insights and URL scanning |
| Container | containers.mcp.cloudflare.com | Sandbox development environments |
| Browser Rendering | browser.mcp.cloudflare.com | Fetch pages, convert to markdown, screenshots |
| Logpush | logs.mcp.cloudflare.com | Log delivery job health summaries |
| AI Gateway | ai-gateway.mcp.cloudflare.com | Search AI logs, view prompts and responses |
| AI Search (AutoRAG) | autorag.mcp.cloudflare.com | List and search indexed documents |
| Audit Logs | auditlogs.mcp.cloudflare.com | Query account audit trails |
| DNS Analytics | dns-analytics.mcp.cloudflare.com | DNS query analytics and debugging |
| Digital Experience | dex.mcp.cloudflare.com | Application experience monitoring |
| CASB | casb.mcp.cloudflare.com | SaaS security misconfiguration scanning |
| GraphQL | graphql.mcp.cloudflare.com | Analytics via Cloudflare's GraphQL API |
| Agents SDK Docs | agents.cloudflare.com | SDK documentation search |

All servers are remote-first with OAuth authentication at their respective `/mcp` endpoints.

## Setup

The main API server has the simplest possible setup:

```json
{
  "mcpServers": {
    "cloudflare": {
      "url": "https://mcp.cloudflare.com/mcp"
    }
  }
}
```

First connection opens a browser for OAuth. You select permissions, and you're connected. That's it — two tools, 2,500 endpoints.

**Adding product-specific servers:**

```json
{
  "mcpServers": {
    "cloudflare": {
      "url": "https://mcp.cloudflare.com/mcp"
    },
    "cloudflare-observability": {
      "url": "https://observability.mcp.cloudflare.com/mcp"
    },
    "cloudflare-browser": {
      "url": "https://browser.mcp.cloudflare.com/mcp"
    }
  }
}
```

You can mix and match. The main server gives you everything; product servers give you deeper, more focused interactions for specific workflows.

**API token authentication (for CI/CD):**

Both OAuth and API token authentication are supported. For headless environments, pass a bearer token in the Authorization header. Account-scoped tokens auto-detect your account ID.

## What's New (April 2026 Update)

Since our last review, Cloudflare has been exceptionally active across the MCP ecosystem — shipping enterprise architecture, fixing reliability issues, and growing adoption significantly.

**Enterprise MCP reference architecture (April 14).** Cloudflare published a comprehensive enterprise deployment guide using Access, AI Gateway, and a new concept: MCP Server Portals. Portal Code Mode collapses tool definitions across *multiple* connected MCP servers into just two portal tools (`portal_codemode_search` and `portal_codemode_execute`), achieving a 94% reduction in context tokens. They also launched **Shadow MCP Detection** — Cloudflare Gateway can now detect unauthorized remote MCP server usage via hostname patterns, URI detection, and DLP body inspection with JSON-RPC regex rules.

**`?codemode=false` parameter for traditional tool mode (March 20).** The Code Mode server now supports a query parameter that disables code generation entirely, exposing all ~2,500 API endpoints as individual MCP tools. This gives users a fallback when their agent struggles with JavaScript code generation — a direct response to the "agent competency" limitation we flagged in our initial review.

**Exponential backoff on rate limits (April 16).** The Code Mode server now implements proper exponential backoff when hitting Cloudflare API 429 responses. Previously, rate limit errors were surfaced to the agent without retry logic. This addresses the rate limit documentation gap we noted earlier.

**OAuth provider hardened to v0.4.0 (March 31).** All 10 product servers received coordinated releases bumping `workers-oauth-provider` to ^0.4.0, adding refresh token TTL management and migration flags. This followed an intermediate bump to 0.3.2. The coordinated release across workers-observability, workers-builds, workers-bindings, logpush, graphql, docs-vectorize, docs-autorag, docs-ai-search, dns-analytics, and dex-analysis shows mature release management.

**Dynamic Workers blog post (March 24).** Cloudflare detailed the V8 sandbox technology powering Code Mode — Dynamic Workers achieve 100x faster startup than traditional containers with millisecond cold starts. This gives technical depth to the sandboxing claims in our initial review.

**GraphQL injection still unpatched (#320).** A string interpolation vulnerability in `fetchTypeDetails` was reported on March 15 with two fix PRs (#321 and #330) submitted, but neither has been merged after 34 days. This is a regression from our earlier assessment of "active security attention."

**New bugs: audit log validation (#352) and Claude Code auth (#95).** The audit log server's Zod schema fails when Cloudflare's API returns `actor.context = "api"` — a new value not in the enum — blocking SOC 2 continuous monitoring workflows. Separately, API Token mode doesn't work with Claude Code because it initiates OAuth discovery before forwarding custom Authorization headers. No workaround available for either issue.

**High-severity dependency vulnerabilities fixed (#333).** Seven high-severity vulnerabilities from outdated dependencies were patched on March 29.

**Stars grew from 3,557 to ~3,600** (product servers) and **277 to 357** (Code Mode, +29%). NPM downloads surged from ~11K to ~19K/month (+73%). PulseMCP shows ~122K all-time estimated visitors (up from ~102K). The Code Mode repo's faster star growth rate suggests the architectural approach is gaining traction.

## What's Good

**Code Mode is genuinely innovative.** This is the first MCP server we've reviewed that solves the "too many tools" problem architecturally rather than by limiting scope. Traditional MCP servers face a fundamental tension: more tools means more capability but more context consumption. An MCP server with 2,500 individual tool definitions would be unusable — 1.17 million tokens just for tool schemas. Code Mode collapses that to ~1,000 tokens by having the agent write code against a typed API instead. It's the difference between giving someone a menu with 2,500 items versus giving them a search bar and a kitchen.

**V8 sandbox execution is properly secure.** The Dynamic Worker isolate runs generated code with no filesystem access, no environment variable exposure, and controlled network permissions. The OAuth flow uses Workers OAuth Provider to downscope tokens to only the permissions the user approved. This is real sandboxing, not just input validation.

**16 specialized servers for depth.** The product-specific servers aren't just thin wrappers — they provide focused interactions tuned for specific workflows. The Observability server gives you structured log queries. The Browser Rendering server converts pages to markdown and takes screenshots. The Radar server provides internet traffic insights. You're not limited to the Code Mode approach when a specialized server does the job better.

**The broadest platform coverage of any MCP server.** No other vendor comes close. AWS has 60+ specialized servers, but they're separate projects with varying quality. Cloudflare ships one unified API server that covers everything, plus 16 curated product servers — all maintained by the same team, all using the same auth model, all remote-first.

**Remote-first architecture across the board.** Every server uses Streamable HTTP transport and OAuth. No npm packages to install, no stdio processes to manage, no API keys to rotate. This is where the MCP ecosystem is heading, and Cloudflare is ahead of the curve.

**Also a platform for building MCP servers.** Cloudflare doesn't just provide MCP servers — they provide the infrastructure for building them. Their Workers platform, `mcp-handler` package, and Agents SDK let you deploy your own MCP servers to the edge. This dual role (server provider + hosting platform) is unique in the MCP ecosystem.

## What's Not

**Code Mode requires agent JavaScript competency — but there's now a fallback.** The `search()` and `execute()` tools work because the agent writes JavaScript against typed APIs. If your AI assistant struggles with JavaScript code generation — or if the task requires complex multi-step API interactions — Code Mode can produce incorrect or suboptimal code. The March 2026 addition of `?codemode=false` provides an escape hatch by exposing all ~2,500 endpoints as individual tools, but at the cost of massive context consumption. The quality of the experience still depends heavily on the agent's coding ability.

**357 stars on the Code Mode repo vs 3,600 on the product servers.** The `cloudflare/mcp` repository (Code Mode) has grown from 277 to 357 stars (+29%) in five weeks — a faster growth rate than the product servers — but the gap remains large. Code Mode adoption is accelerating, with community PRs for Gemini CLI support and improved tool descriptions, but the gap means fewer reports on Code Mode edge cases compared to the product servers.

**The ecosystem is fragmented across repositories.** Three GitHub repositories (`cloudflare/mcp`, `cloudflare/mcp-server-cloudflare`, `cloudflare/workers-mcp`) serve overlapping purposes. The `workers-mcp` package is the original stdio-based approach, `mcp-server-cloudflare` contains the product-specific servers, and `cloudflare/mcp` is the Code Mode API server. Documentation clarifies this, but the history creates confusion about which approach to use.

**Cloudflare-only lock-in.** Like [Vercel's MCP server](/reviews/vercel-mcp-server/), this only works with Cloudflare's platform. If your infrastructure is on AWS, GCP, or bare metal, none of these servers help you. The breadth of coverage is impressive, but it's breadth within one vendor's ecosystem.

**IP address filtering not supported.** API tokens with Client IP Address Filtering enabled don't work. If your organization requires IP-restricted tokens for security compliance, you'll need to use OAuth instead — which requires a browser and doesn't work in headless environments.

**API Token mode broken with Claude Code (#95).** Custom Authorization headers are never forwarded because Claude Code initiates OAuth discovery first. There's no workaround — Claude Code users must use OAuth, which requires a browser and doesn't work in headless environments. This is a significant gap for one of the most popular MCP clients.

**Unpatched GraphQL injection (#320, 34 days open).** A string interpolation vulnerability in the GraphQL server's `fetchTypeDetails` has had two community fix PRs (#321, #330) submitted but neither merged after over a month. The previous review praised "active security attention" — that assessment needs qualification now.

**Audit log schema validation failure (#352).** The audit log server crashes when Cloudflare's own API returns `actor.context = "api"` — a value not in the Zod schema enum. This blocks SOC 2 continuous monitoring workflows. The issue highlights a broader fragility: hardcoded enums break when the upstream API evolves.

## How It Compares

| Feature | Cloudflare MCP | Vercel MCP | AWS MCP (60+ servers) |
|---------|---------------|------------|----------------------|
| **Endpoints** | 2,500+ (one server) | 13 tools | Varies per server |
| **Approach** | Code Mode (2 tools) | Individual tools | Individual tools |
| **Context cost** | ~1,000 tokens | ~3,000 tokens | Varies (adds up fast) |
| **Auth** | OAuth + API token | OAuth | IAM / various |
| **Transport** | Remote (Streamable HTTP) | Remote (Streamable HTTP) | Mostly stdio |
| **Product servers** | 16 specialized | 1 | 60+ separate repos |
| **Maintained by** | Cloudflare | Vercel | AWS (varying teams) |
| **GitHub stars** | 357 (Code Mode) / 3,600 (product) | 403 (mcp-handler) | Varies |
| **Hosting platform** | Yes (Workers) | Yes (Vercel) | Yes (Lambda) |

Cloudflare's Code Mode approach is fundamentally different from how Vercel and AWS handle MCP. Vercel exposes 13 individual tools covering ~20% of their platform. AWS ships 60+ separate servers that each need their own configuration. Cloudflare collapses everything into two tools that cover 100% of their platform while consuming less context than Vercel's 13 tools.

The tradeoff is abstraction level. Vercel's individual tools are predictable — `list_deployments` always returns the same structured data. Cloudflare's `execute()` depends on the agent writing correct JavaScript, which introduces a layer of variability. When Code Mode works (which is most of the time with capable agents), it's dramatically more efficient. When it fails, debugging generated code adds friction.

For a broader comparison, see our [Best DevOps & Infrastructure MCP Servers](/guides/best-devops-mcp-servers/) guide.

## The Bigger Picture

Code Mode represents a potential paradigm shift in how MCP servers handle large APIs. The traditional approach — expose each endpoint as a separate tool — doesn't scale past a few dozen tools before context window pressure becomes a problem. Cloudflare's solution is elegant: keep the API specification on the server, let the agent write code against it, and execute that code in a sandbox.

This matters beyond Cloudflare. Any platform with hundreds or thousands of API endpoints faces the same scaling problem. Cloudflare is already extending the pattern: their April 2026 MCP Server Portals apply Code Mode across *multiple* connected MCP servers, collapsing all their tools into two portal-level tools with a 94% context reduction. If this proves reliable, the idea of connecting to dozens of MCP servers simultaneously — currently impractical due to context pressure — becomes feasible. Cloudflare has open-sourced the pattern, and their `mcp-handler` package makes it easier for others to build servers using the same architecture on Cloudflare Workers.

The 16 product-specific servers show that Cloudflare isn't betting everything on Code Mode either. Some workflows are better served by focused, specialized tools. The Observability server for log queries, the Browser Rendering server for page screenshots, the Radar server for traffic analysis — these provide structured interfaces that Code Mode's free-form approach can't always match.

The dual role as both MCP server provider and MCP hosting platform is strategically significant. Cloudflare isn't just connecting AI to their infrastructure — they're positioning Workers as the default deployment target for MCP servers generally. The remote-first, OAuth-authenticated, edge-deployed architecture they've built is a template for the entire ecosystem.

## Rating: 4.5/5

The Cloudflare MCP server earns a 4.5/5 — our highest rating — for solving the fundamental scalability problem in MCP with Code Mode, providing the broadest platform coverage of any single MCP server (2,500+ endpoints), and backing it with 16 specialized product servers that are all remote-first with proper OAuth authentication. The V8 sandbox execution model is genuinely secure, the `?codemode=false` fallback addresses agent competency concerns, and the enterprise architecture with Portal Code Mode and Shadow MCP Detection shows Cloudflare thinking about real deployment scenarios. It loses half a point for the unpatched GraphQL injection (#320, 34 days), the Claude Code auth incompatibility (#95), the audit log schema fragility (#352), and the still-fragmented repository structure. The innovation and execution velocity remain exceptional — npm downloads up 73%, Code Mode stars up 29% — but the security response time needs to improve to maintain this rating.

**Use this if:** You manage Cloudflare infrastructure and want AI-assisted operations across Workers, R2, D1, DNS, security, or any of their 2,500+ API endpoints.

**Skip this if:** Your infrastructure isn't on Cloudflare, or your AI assistant struggles with JavaScript code generation (stick to product-specific servers in that case).

## Related Guides

- **[Cloudflare's EmDash: The AI-Native CMS That Puts an MCP Server in Every Website](/guides/cloudflare-emdash-mcp-server-wordpress-successor/)** — Cloudflare's WordPress successor ships a built-in MCP server with every instance, sandboxed plugins via Dynamic Workers, and x402 native payments

*Disclosure: We research MCP servers using publicly available documentation, GitHub repositories, community discussions, and ecosystem data. We do not test or install MCP servers hands-on. All claims are based on published sources.*

*This review was last updated on 2026-04-18 using Claude Opus 4.6 (Anthropic).*

