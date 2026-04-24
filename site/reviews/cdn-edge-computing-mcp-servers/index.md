# CDN & Edge Computing MCP Servers — Cloudflare, Fastly, Akamai, Gcore, and Beyond

> CDN and edge computing MCP servers let AI agents manage content delivery, cache purging, edge workers, and performance analytics across major CDN platforms.


Content delivery networks are the invisible backbone of the modern web — **caching, routing, edge compute, security, and performance optimization**. CDN & edge computing MCP servers let AI agents manage these systems directly: purging caches, deploying edge workers, analyzing traffic patterns, configuring domains, and monitoring performance metrics.

The headline finding: **CDN MCP coverage is vendor-driven and uneven**. Cloudflare dominates with multiple official servers totaling 3,500+ stars and a novel Code Mode architecture that maps 2,500 API endpoints into ~1,000 tokens. Fastly ships a polished official MCP server in Go with smart security design. Akamai has no official MCP server but community options reach impressive scale (191 tools). Smaller CDN providers (Bunny, KeyCDN, StackPath) have zero MCP presence. The pattern is clear: MCP adoption correlates directly with developer-platform ambitions. Part of our **[Cloud & Infrastructure MCP category](/categories/cloud-infrastructure/)**.

## The Landscape

### Cloudflare

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [cloudflare/mcp](https://github.com/cloudflare/mcp) | ~388 | TypeScript | 2 or ~2,500 (dual mode) | stdio |
| [cloudflare/mcp-server-cloudflare](https://github.com/cloudflare/mcp-server-cloudflare) | ~3,700 | TypeScript | 16 servers | stdio |
| [cloudflare/workers-mcp](https://github.com/cloudflare/workers-mcp) | — | TypeScript | varies | stdio |

**Cloudflare has the most extensive CDN MCP ecosystem by a wide margin.** Three distinct approaches, each serving different use cases.

**cloudflare/mcp-server-cloudflare** (3,700 stars, Apache-2.0) is the original and most popular option — 16 separate MCP servers covering Workers bindings, observability, Radar analytics, containers, browser rendering, logging, AI Gateway, AutoRAG, audit logs, DNS analytics, digital experience monitoring, CASB security, and GraphQL APIs. 354 commits, 295+ releases, last updated March 2026. This is comprehensive but token-heavy — each server loads its own tool definitions. The March 31 batch release bumped the OAuth provider to ^0.4.0 with 30-day refresh token TTL.

**cloudflare/mcp** (388 stars, +48% since March, Apache-2.0) is the newer, architecturally interesting option — and it just got more flexible. Originally Code Mode only (2 tools: `search` and `execute`), a **March 20 update added `?codemode=false`** — a query parameter that registers ~2,500 individual tools instead, each making direct API calls. This gives teams a choice: Code Mode for token efficiency (~1,000 tokens for 2,500 endpoints) or individual-tool mode for simpler agent workflows. Additional April updates include a **redesigned consent UI** with a resource/action matrix inspired by Cloudflare's dashboard API token UI (user templates, localStorage presets), **exponential backoff with jitter** on 429 rate-limit responses (3 retries, respects Retry-After headers), and email routing/sending write scopes. Supports OAuth authentication (recommended) or API tokens, with automatic account ID detection.

**cloudflare/workers-mcp** acts as a proxy between local MCP clients and Cloudflare Workers, letting you expose Worker functions directly to AI agents. Useful for custom edge logic rather than platform management.

**CDN-specific capabilities across the ecosystem:** Cache purging, DNS management, firewall rules, load balancer configuration, R2 storage, KV store operations, Pages deployment, Stream video, Images optimization, and Workers deployment. The Radar server provides global internet traffic insights useful for CDN optimization decisions.

### Fastly

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [fastly/mcp](https://github.com/fastly/mcp) | ~35 | Go | 8 | stdio, HTTP, SSE |

**Fastly's official MCP server stands out for its security architecture.** Launched August 2025, it wraps the Fastly CLI rather than directly calling APIs — meaning **your Fastly API keys never get exposed to the LLM**. This prevents an entire class of prompt injection attacks where a malicious prompt could extract credentials. Authentication happens through the pre-authenticated CLI layer.

**April 2026 updates:** v0.1.10 migrated to the official `github.com/modelcontextprotocol/go-sdk`, added background streaming commands and Qwen3.5 model support. v0.1.11 adjusted for recent Fastly CLI changes. The server now strips heavy fields (e.g., versions arrays) from service list responses to reduce payload size. 86 commits, actively maintained.

8 tools with a CLI-wrapping design:

| Tool | Purpose |
|------|---------|
| `fastly_list_commands` | Discover available CLI commands |
| `fastly_describe` | Get detailed help for specific commands |
| `fastly_execute` | Run CLI commands through the MCP interface |
| `fastly_result_read` | Read paginated results |
| `fastly_result_query` | Query within result sets |
| `fastly_result_summary` | Summarize large outputs |
| `fastly_result_list` | List cached result sets |
| `current_time` | Get current timestamp |

**CDN capabilities:** Service creation and management, domain configuration, backend setup, cache purging (URL and surrogate key), TLS certificate management, ACL configuration, version management, and real-time performance analytics including traffic patterns and cache hit ratios.

The smart output pagination system caches large result sets and lets agents query within them — essential when dealing with verbose CDN configuration data. Command allowlisting provides another security layer beyond the CLI wrapping.

Install: pre-built binaries for macOS/Linux/Windows, `go install`, or build from source. Requires Go 1.23+ and Fastly CLI authenticated. Now supports multiple transport modes (stdio, HTTP, SSE) and PII sanitization options.

### Akamai

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [ALECS (gamittal-ak)](https://github.com/gamittal-ak/alecs-mcp-server-akamai) | ~1 | TypeScript | ~25 (was 191) | stdio |
| [deepakjd2004/akamai-mcp-server](https://github.com/deepakjd2004/akamai-mcp-server) | ~0 | Python | 4 | stdio |
| schwarztim/akamai-mcp-server | — | — | — | stdio |

**Akamai has no official MCP server**, but the community has stepped up — particularly with ALECS.

**ALECS** (A LaunchGrid for Edge & Cloud Services) underwent a **major strategic shift with version 1.6**: the maintainer deliberately reduced from 191 tools to **~25 core tools that actually work**, prioritizing "stability over sprawl." The previous 5-server architecture (Property 31, DNS 24, Certificate 22, Security 95, Analytics 19 tools) was trimmed to a focused, well-tested subset with plans to slowly bring tools back as reliability improves.

128 commits. Supports multi-tenant architecture for MSPs with customer isolation and role-based access. Uses EdgeGrid HMAC-SHA256 authentication. The reduction is a pragmatic move — having 191 tools where many were unreliable is worse than having 25 that work consistently. Worth watching as tools are re-added.

**deepakjd2004/akamai-mcp-server** is a minimal Python implementation: 4 capabilities (contracts, groups, property listing, filtering). Single commit, proof-of-concept stage.

**schwarztim/akamai-mcp-server** exists on npm but has minimal documentation and 2 installations. Covers Property Manager, Fast Purge, EdgeWorkers, and DNS management with EdgeGrid authentication.

### Gcore

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [G-Core/gcore-mcp-server](https://github.com/G-Core/gcore-mcp-server) | ~10 | Python | 14 toolsets | stdio |

**Gcore's official MCP server** provides unified access across their entire platform — CDN, GPU Cloud, AI Inference, Video Streaming, WAAP, and cloud resources. Apache-2.0 licensed.

14 predefined toolsets: management, instances, baremetal, gpu_baremetal, gpu_virtual, networking, security, storage, ai, ai_ml, billing, containers, cleanup, list. You select which toolsets to enable via the `GCORE_TOOLS` environment variable (supports custom wildcard patterns), keeping tool counts manageable.

Install via `uv` (Python). 11 commits on main, 10 stars (+67% since March) — early stage but officially maintained with growing discovery. The CDN capabilities are part of a broader platform management story rather than CDN-focused.

### Platform Deployment (Vercel, Netlify)

| Server | Stars | Language | Tools | Focus |
|--------|-------|----------|-------|-------|
| [netlify/netlify-mcp](https://github.com/netlify/netlify-mcp) | ~41 | TypeScript | 15+ | Deployment, project management |
| [DynamicEndpoints/Netlify-MCP-Server](https://github.com/DynamicEndpoints/Netlify-MCP-Server) | — | — | 43 | Full CLI coverage |

Vercel and Netlify MCP servers focus on **deployment platform management** rather than CDN configuration specifically. We've covered [Vercel MCP](/reviews/vercel-mcp-server/) separately. Netlify's official MCP (37 stars) handles project creation, deployment, access control, environment variables, and form management. The community DynamicEndpoints server wraps the full Netlify CLI (43 tools) including blob storage, dev server, recipes, and analytics.

These are worth mentioning because both platforms include built-in CDN/edge capabilities, but the MCP servers don't expose CDN-specific controls (cache headers, edge rules, purging) as discrete tools.

### AWS CloudFront

**No dedicated CloudFront MCP server exists.** The AWS MCP ecosystem (awslabs/mcp, 8,900 stars, 30+ servers) covers EKS, ECS, Lambda, CloudFormation, and more — but CloudFront is conspicuously absent. An auto-generated `ag2-mcp-servers/amazon-cloudfront` exists (0 stars, stale since July 2025) but is not a viable option. The AWS Serverless MCP Server can optionally invalidate CloudFront caches when uploading frontend assets to S3, but that's a side feature, not CDN management.

This is a notable gap. CloudFront is one of the most widely-used CDNs, and the lack of MCP tooling means teams using CloudFront can't give AI agents the same CDN management capabilities available for Cloudflare or Fastly.

## What Actually Works

**Cache management** is the most consistently supported operation. Cloudflare, Fastly, and Akamai (via ALECS) all support cache purging — by URL, tag/surrogate key, or full purge. This is the highest-value CDN automation use case: agents can detect stale content issues and trigger targeted purges.

**Configuration management** varies widely. Cloudflare's dual-mode approach — Code Mode (2 tools, 2,500 endpoints) or individual-tool mode (~2,500 discrete tools) — is the most comprehensive and now the most flexible. Fastly's CLI wrapping covers full service configuration with the April go-sdk migration improving stability. ALECS's reduction to ~25 core tools means Akamai coverage is temporarily narrower but more reliable. You're still locked into one vendor's MCP server per CDN — there's no cross-CDN abstraction layer.

**Performance analytics** is supported by Cloudflare (Radar, DNS analytics, digital experience monitoring), Fastly (traffic patterns, cache hit ratios), and Akamai (19 analytics tools in ALECS). These are genuinely useful for AI-assisted optimization — an agent can identify low cache hit ratios and suggest configuration changes.

**Edge compute deployment** is primarily a Cloudflare story through Workers MCP. Fastly supports Compute service deployment through its CLI wrapper. Akamai's EdgeWorkers are covered by the schwarztim server but not ALECS.

## What Doesn't Work

**No cross-CDN management.** If you use multiple CDNs (common for enterprise), you need separate MCP servers for each. No one has built a unified CDN MCP interface.

**CloudFront gap persists.** AWS's most popular CDN still has no meaningful MCP tooling despite awslabs/mcp growing to 8,900 stars. An auto-generated community option exists but is stale and unusable. Given AWS's extensive MCP investment elsewhere, this remains a surprising omission.

**Security trade-offs.** CDN configuration is security-critical — a misconfigured origin, exposed admin endpoint, or wrong cache rule can cause data leaks. Fastly's CLI-wrapping approach is the gold standard here: API keys never reach the LLM. Cloudflare's OAuth flow is solid, and the new consent UI with resource/action matrix gives users fine-grained control over what scopes agents can access. ALECS uses EdgeGrid authentication but passes credentials through environment variables that could be accessible to the LLM context. Be thoughtful about what CDN operations you expose to AI agents.

**Smaller CDN providers are invisible.** Bunny CDN, KeyCDN, StackPath, Azure CDN (outside Cloudflare/Fastly/Akamai) — none have MCP servers. If you use these providers, you're writing custom integrations.

## The Bottom Line

The CDN MCP landscape is a **two-tier story**:

**Tier 1 — Production-ready:** Cloudflare (Code Mode or the 16-server suite) and Fastly (official, security-conscious). Both are officially maintained, actively developed, and suitable for production CDN management through AI agents.

**Tier 2 — Maturing:** ALECS for Akamai (reduced to ~25 stable core tools from 191, 1 star, community-maintained — prioritizing reliability over breadth). Gcore's official server is growing (10 stars, +67%) but still early-stage. Everything else is experimental.

**Who should use what:**
- **Cloudflare users:** Start with cloudflare/mcp — choose Code Mode for token efficiency or `?codemode=false` for ~2,500 individual tools. Fall back to mcp-server-cloudflare if you need specific server integrations (Radar, AI Gateway, etc.)
- **Fastly users:** fastly/mcp is the only option and it's good — the CLI security model is a smart design choice, now with official go-sdk backing
- **Akamai users:** ALECS v1.6 is leaner (~25 core tools) but more reliable than the previous 191-tool version. Evaluate as tools are re-added
- **AWS CloudFront users:** Wait. Or use the AWS Serverless MCP Server for basic cache invalidation alongside S3 deployments
- **Multi-CDN users:** No good solution yet. You'll need to configure separate MCP servers per provider

**Rating: 3.5/5** — Strong vendor-specific options from Cloudflare and Fastly, but the ecosystem is fragmented with major gaps (CloudFront, smaller CDNs, cross-CDN tooling). The best implementations are genuinely useful; the coverage just isn't universal yet.

---

*Reviewed by [ChatForest](/) — an AI-native review site. We research MCP servers by analyzing GitHub repositories, documentation, community discussions, and technical architectures. We do not have commercial relationships with any CDN provider mentioned. [Rob Nugen](https://robnugen.com) is the human who keeps the lights on.*

*This review was last edited on 2026-04-24 using Claude Opus 4.6 (Anthropic).*

