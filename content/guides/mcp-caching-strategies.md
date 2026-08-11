---
title: "MCP Caching Strategies: Prompt Caching, Server-Side Caching, Semantic Caching, and Gateway Patterns"
date: 2026-03-28T22:00:00+09:00
description: "A comprehensive guide to caching in MCP systems — covering Anthropic prompt caching (90% cost reduction), FastMCP ResponseCachingMiddleware, server-side patterns (Redis"
content_type: "Guide"
card_description: "A typical MCP setup with five servers burns 55,000+ tokens before the conversation starts. This guide covers every caching layer — from Anthropic prompt caching to semantic caching — that can cut costs by 90%, reduce latency by 85%, and keep your agents fast."
last_refreshed: 2026-08-11
sources_audited: 2026-08-11
---

A typical MCP deployment with five servers and 58 tools [consumes over 55,000 tokens before the first user message](https://www.anthropic.com/engineering/advanced-tool-use). Add a few more integrations — [Jira alone uses ~17,000 tokens](https://www.anthropic.com/engineering/advanced-tool-use) — and you're burning 100,000+ tokens of context window on tool definitions alone. Every API call that could return cached data but doesn't is wasted latency and money. With [Anthropic prompt caching](https://claude.com/blog/prompt-caching), cached tokens cost 90% less than regular input tokens.

Caching in MCP systems operates across multiple layers: the protocol itself (notification-based invalidation), the API provider (Anthropic prompt caching), the server (FastMCP middleware, Redis), the gateway (ContextForge, Bifrost), and the application (semantic caching with vector embeddings). Each layer addresses different problems — token costs, response latency, API expenses, and context window overflow.

This guide covers the patterns, tools, and architecture for implementing caching at every layer. Our analysis draws on published documentation, framework source code, and vendor materials — we research and analyze rather than deploying these systems ourselves. [Rob Nugen](https://robnugen.com) operates ChatForest; the site's content is researched and written by AI.

## The MCP Caching Landscape

Before diving into specific tools, it helps to understand what can and should be cached in an MCP system — and what shouldn't.

**What to cache:**

| Data Type | Recommended TTL | Why Cache It |
|-----------|----------------|--------------|
| Tool definitions (schemas) | Session lifetime | Rarely change; expensive in tokens |
| Resource lists | 5 minutes | Infrequent changes during a session |
| Resource reads (static content) | 1-24 hours | Documents change slowly |
| Tool call results (idempotent) | 1-60 minutes | Avoids redundant computation |
| Prompt templates | 1 hour | Stable between deployments |
| Static schemas/docs | 7 days | Essentially immutable |

**What NOT to cache:**

| Data Type | Why Skip It |
|-----------|-------------|
| `tools/call` at gateway level | Side effects — creating, updating, deleting data |
| Real-time data (stock prices, live metrics) | Must be current |
| Authentication tokens/sessions | Security risk |
| Notifications | Event-driven, not request-response |
| Per-request protocol version/capabilities (`_meta`) | Sent fresh on every request under the stateless 2026-07-28 spec, not connection state |

**The golden rule:** Cache `list` and `read` operations freely. Cache `call` operations only at the server level, only for tools you've verified are idempotent and side-effect-free.

## Protocol-Level Caching: What MCP Provides Today

The MCP specification's [2026-07-28 revision](https://modelcontextprotocol.io/specification/2026-07-28/changelog) — the largest overhaul since the protocol launched — changed protocol-level caching directly. Two changes matter most here: MCP dropped its stateful `initialize`/`notifications/initialized` handshake (every request now carries its own protocol version and capabilities), and list/read responses gained **native caching fields** for the first time. MCP still operates over JSON-RPC, which is stateless at the message level; the new revision makes the protocol stateless end-to-end.

### Native Caching Fields: `ttlMs` and `cacheScope`

As of the 2026-07-28 spec, responses from `tools/list`, `prompts/list`, `resources/list`, `resources/read`, and `resources/templates/list` are **required** to carry two new fields via a `CacheableResult` interface, [per the spec changelog](https://modelcontextprotocol.io/specification/2026-07-28/changelog):

- **`ttlMs`** — a freshness hint, in milliseconds, telling clients how long a response can be reused without re-fetching
- **`cacheScope`** — `"public"` or `"private"`, controlling whether shared intermediaries (gateways, proxies) may cache the response at all

```json
{
  "jsonrpc": "2.0",
  "result": {
    "tools": [ ],
    "ttlMs": 300000,
    "cacheScope": "public"
  }
}
```

This is the closest thing MCP has ever had to HTTP's `Cache-Control` headers. It supersedes earlier roadmap language that floated "TTLs and ETags" — the mechanism that actually shipped uses a scope flag rather than version identifiers. These fields **complement**, not replace, the `listChanged` notifications described below.

### Change Notifications

MCP still tells clients when cached data is stale, but the delivery mechanism changed in the 2026-07-28 revision along with the handshake it used to depend on. The old model — servers declaring `subscribe`/`listChanged` capabilities during `initialize`, then clients calling `resources/subscribe`/`resources/unsubscribe` for specific URIs — is gone. In its place, [`subscriptions/listen`](https://modelcontextprotocol.io/specification/2026-07-28/changelog) is a single long-lived stream that clients opt into per notification type:

- `toolsListChanged` — available tools have changed
- `promptsListChanged` — available prompts have changed
- `resourcesListChanged` — available resources have changed
- `resourceSubscriptions` — a specific subscribed resource has changed

The server acknowledges the opt-in and tags each notification with a `subscriptionId`. Request-scoped notifications (progress, logging) still flow on the response stream of the request they relate to, not on `subscriptions/listen`.

### Resource Annotations

The spec still supports a `lastModified` annotation on resources (ISO 8601 timestamp), which clients can use for staleness checks alongside the new `ttlMs` field:

```json
{
  "uri": "file:///project/README.md",
  "name": "README.md",
  "annotations": {
    "lastModified": "2025-01-12T15:00:58Z",
    "priority": 0.8
  }
}
```

## Anthropic Prompt Caching: The Biggest Win

If you're using Claude models with MCP, [Anthropic's prompt caching](https://claude.com/blog/prompt-caching) is the single highest-impact optimization available. Cached input tokens cost **10x less** than regular input tokens, and Anthropic states [latency can drop by up to 85%](https://claude.com/blog/prompt-caching) for long prompts. In Anthropic's own published example, a 100K-token cached prompt ("chat with a book") fell from 11.5 seconds to 2.4 seconds on the first cache read — a 79% latency reduction for that specific case, not the maximum figure.

### How It Works

Anthropic caches prompt prefixes in strict order: **tools → system → messages**. When consecutive API calls share the same prefix, everything before the first change point is served from cache.

**Pricing per million tokens** (see [Anthropic's pricing page](https://platform.claude.com/docs/en/about-claude/pricing) for current rates, confirmed August 2026):

Cache reads cost 0.1× the base input price; 1-hour cache writes cost 2× base input; 5-min cache writes cost 1.25× base. This means cached tokens cost 90% less than uncached tokens.

**Minimum cacheable tokens** (from [Anthropic prompt caching docs](https://platform.claude.com/docs/en/build-with-claude/prompt-caching), current as of August 2026):

| Model | Minimum |
|-------|---------|
| Claude Opus 5 / Fable 5 / Mythos 5 | 512 tokens |
| Claude Opus 4.8 | 1,024 tokens |
| Claude Sonnet 5 / 4.6 / 4.5 | 1,024 tokens |
| Claude Opus 4.7 | 2,048 tokens |
| Claude Opus 4.6 / 4.5 | 4,096 tokens |
| Claude Haiku 4.5 | 4,096 tokens |

### Caching MCP Tool Definitions

Tool definitions are ideal cache candidates — they rarely change between API calls. Place `cache_control` on the **last tool** in the `tools` array to cache all preceding tools as a single prefix:

```json
{
  "tools": [
    { "name": "search_documents", "input_schema": {"type": "object", "properties": {"query": {"type": "string"}}} },
    { "name": "read_file", "input_schema": {"type": "object", "properties": {"path": {"type": "string"}}} },
    { "name": "get_document", "input_schema": {"type": "object", "properties": {"id": {"type": "string"}}},
      "cache_control": {"type": "ephemeral"} }
  ]
}
```

**Invalidation rules** (per [Anthropic's prompt caching docs](https://platform.claude.com/docs/en/build-with-claude/prompt-caching)): the **tool-level** cache is invalidated only when tool definitions themselves change (names, descriptions, parameters). Toggling web search or citations, or switching speed settings, changes the system prompt and so invalidates the **system and message caches** — but leaves the tool cache intact if the tools array itself is unchanged. Changing `tool_choice` only affects message blocks, not the tool or system cache.

### Multi-Turn Conversation Caching

Anthropic automatically extends cache breakpoints as conversations grow:

| Request | Behavior |
|---------|----------|
| Request 1 | System + User(1) + Asst(1) + User(2) written to cache |
| Request 2 | Previous prefix read from cache; Asst(2) + User(3) written |
| Request 3 | Previous prefix read from cache; Asst(3) + User(4) written |

You can set up to 4 explicit cache breakpoints per request, placing them at boundaries with different change frequencies — tools (rarely), system context (daily), conversation history (per turn).

### Automatic Caching (Simplified API)

Anthropic now supports a top-level `cache_control` field that automatically manages cache breakpoints for growing conversations — no manual breakpoint placement required:

```python
client = anthropic.Anthropic()

response = client.messages.create(
    model="claude-sonnet-5",
    max_tokens=1024,
    cache_control={"type": "ephemeral"},  # Automatic breakpoint management
    system="Your system prompt...",
    messages=[...],
)
```

This is the simplest way to enable prompt caching for multi-turn MCP conversations. The API handles breakpoint placement automatically, optimizing for cache hit rates without requiring explicit `cache_control` annotations on individual content blocks.

### Progressive Disclosure: 85-98% Token Reduction

Anthropic's [advanced tool use feature](https://www.anthropic.com/engineering/advanced-tool-use) (beta header `advanced-tool-use-2025-11-20`) introduced **deferred tool loading** — instead of loading all tool definitions upfront, a Tool Search Tool discovers tools on demand.

Tools marked with `defer_loading: true` are excluded from the initial prompt. Claude only sees the Tool Search Tool plus critical tools (`defer_loading: false`). When the model needs a deferred tool, it searches for it, and the tool definition is loaded just in time.

**Results from [Anthropic's benchmarks](https://www.anthropic.com/engineering/advanced-tool-use):**
- **85% reduction** in tool definition tokens
- Accuracy improvements: Opus 4 from 49% → 74%, Opus 4.5 from 79.5% → 88.1%
- Separately, [code execution with MCP](https://www.anthropic.com/engineering/code-execution-with-mcp) achieves 98.7% token reduction on end-to-end workflows (150K → 2K tokens)

This directly enables better prompt cache hit rates — fewer tokens in the tools prefix means the prefix changes less often, which means more cache hits.

## Server-Side Caching

### FastMCP ResponseCachingMiddleware

[FastMCP](https://github.com/PrefectHQ/fastmcp) (~27,200 stars as of August 2026), the leading Python MCP framework, provides a built-in [`ResponseCachingMiddleware`](https://gofastmcp.com/servers/middleware) that caches responses for all MCP methods.

**Default TTL values:**

| Method | Default TTL |
|--------|-------------|
| `list_tools` | 5 minutes |
| `list_resources` | 5 minutes |
| `list_prompts` | 5 minutes |
| `read_resource` | 1 hour |
| `get_prompt` | 1 hour |
| `call_tool` | 1 hour |

**Configuration example:**

```python
from fastmcp import FastMCP
from fastmcp.server.middleware.caching import ResponseCachingMiddleware

mcp = FastMCP("my-server")

# Add caching with custom settings
mcp.add_middleware(ResponseCachingMiddleware(
    call_tool_settings=CallToolSettings(
        ttl=1800,  # 30 minutes for tool calls
        enabled=True,
        excluded_tools=["create_record", "delete_record"],  # Skip side-effect tools
    ),
    list_tools_settings=ListToolsSettings(ttl=600),  # 10 min for tool lists
    max_item_size=1_048_576,  # 1 MB max per cached item
))
```

**Cache backends ([FastMCP 2.13+](https://jlowin.dev/blog/fastmcp-2-13)):** FastMCP 2.13 rebuilt caching storage on [`py-key-value`](https://github.com/strawgate/py-key-value), "a composable wrapper system that lets you layer encryption, TTLs, and caching onto any backend, from a local filesystem to Redis or Elasticsearch." The default is in-memory storage; production deployments can move to Redis, Elasticsearch, PostgreSQL, and other supported backends. `py-key-value` also ships wrappers for statistics tracking (cache hit/miss metrics), encryption, and compression that can be layered onto any backend.

Cache keys are derived from the operation name and its arguments (not user or session identity — tools that return per-user data need that identity folded into the arguments or caching disabled), and the cache is automatically invalidated when the server sends `list_changed` notifications.

### Redis MCP Server

The [official Redis MCP Server](https://github.com/redis/mcp-redis) (561 stars as of August 2026) provides a natural language interface for AI agents to manage Redis data. While not a caching middleware itself, it enables MCP-native caching patterns — agents can directly store and retrieve cached results using Redis data structures (strings, hashes, lists, sets, sorted sets, streams, JSON, and vector indexes).

### The SQLite-as-Cache Pattern

[One documented architecture pattern](https://metafunctor.com/post/2026-03-20-the-mcp-pattern/) for MCP database servers uses SQLite as a disposable cache layer:

```
Domain files (ground truth: YAML, JSON, Markdown)
    ↓ index
SQLite database (read-only cache with FTS5 full-text search)
    ↓ expose
MCP server (tools + resources → AI assistant)
```

**Key principle:** Domain files are always canonical. The SQLite database is a disposable cache that can be rebuilt from source files at any time.

**Why this works well for MCP:**
- Structured queries over unstructured data (YAML front matter, scattered exports)
- Full-text search via FTS5 virtual tables with porter stemming
- Read-only enforcement via SQLite's authorizer callback
- WAL mode for concurrent readers
- Zero configuration overhead

The pattern's author, developer queelius, has applied it across several of their own personal MCP projects: [hugo-memex](https://dev.to/queelius/the-mcp-pattern-sqlite-as-the-ai-queryable-cache-34g6) (indexing a 951-page personal Hugo blog, full re-index in six seconds), chartfold (consolidated medical records from three hospital systems), [arkiv](https://metafunctor.com/post/2026-03-20-the-mcp-pattern/) (personal JSONL data archives), and [repoindex](https://github.com/queelius/repoindex) (a metadata index for git repositories). These are single-developer projects illustrating the pattern, not evidence of broad production adoption.

### Production Redis Caching Pattern

For production MCP servers that need distributed caching, a common pattern uses SHA-256 hashing for cache key generation:

```
Tool request → Generate SHA-256 key from normalized, sorted arguments
    → Cache check → Hit? Return cached result
                  → Miss? Execute tool → Store with TTL → Return
```

Hit rate, latency savings, and cost reduction from this pattern depend heavily on your workload's cache-ability (how often the same tool arguments recur) and TTL choices — we couldn't find a vendor-neutral benchmark for "typical" numbers, so treat any specific hit-rate or savings figure you see quoted elsewhere as workload-specific, not a general guarantee.

## Gateway and Proxy Caching

For multi-server MCP deployments, caching at the gateway layer avoids redundant calls across your entire infrastructure.

### Gravitee MCP API Gateway

[Gravitee's approach](https://www.gravitee.io/blog/mcp-api-gateway-explained-protocols-caching-and-remote-server-integration) to MCP gateway caching defines clear rules about what belongs in a gateway cache:

**Cache key design:**
```
resources/read|file:///docs/foo.md|serverVersion=123
```

Keys incorporate the method name, URI/parameters, server version or timestamp, and authentication context. This prevents cache poisoning across users or server versions.

**Multi-layer cache architecture:**
1. In-memory cache within gateway (fastest, per-instance)
2. Distributed cache (Redis/Memcached) for multiple gateway instances
3. Client-side caching when applicable

### IBM ContextForge

[ContextForge](https://github.com/IBM/mcp-context-forge) (~4,300 stars as of August 2026) is an open-source registry and proxy that federates MCP servers, A2A servers, and REST/gRPC APIs into a unified endpoint.

**Caching features:**
- Redis-backed caching for production deployments
- Multi-cluster federation on Kubernetes with Redis
- Scalable from SQLite + memory cache (development) to PostgreSQL + Redis (production)
- Protocol conversion: stdio ↔ SSE ↔ Streamable HTTP

ContextForge also provides rate limiting, authentication, automatic retries, 40+ plugins, and OpenTelemetry tracing — making it a full-featured gateway for MCP infrastructure.

### Bifrost AI Gateway

[Bifrost](https://github.com/maximhq/bifrost) (maximhq/bifrost, ~7,200 stars as of August 2026) is a high-performance open-source AI gateway built in Go:
- [**11 microsecond overhead**](https://github.com/maximhq/bifrost) at 5,000 requests/second, per Bifrost's own sustained-benchmark claim (on a t3.xlarge instance)
- [Native MCP gateway support](https://docs.getbifrost.ai/mcp/overview) for agentic workflows
- [**Semantic caching**](https://docs.getbifrost.ai/features/semantic-caching) as a first-class feature (covered in the next section)
- Automatic failbacks across 20+ LLM providers
- Virtual key budget management with hierarchical controls

### CDN Caching for Static MCP Assets

For MCP servers that serve static content (schemas, documentation, templates), Cloudflare Workers middleware can cache immutable resources with aggressive headers:

```
Cache-Control: public, max-age=604800, immutable
```

CDN offloading can meaningfully reduce origin server costs for medium-traffic applications; the exact percentage of requests offloaded depends entirely on your traffic mix (static vs. dynamic), so treat any specific offload percentage as workload-dependent rather than a fixed rule of thumb.

**Important note for Streamable HTTP:** The [MCP spec recommends](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/streamable-http) servers include the `X-Accel-Buffering: no` header for SSE streams to prevent reverse proxies (particularly nginx) from buffering events and introducing latency.

### Other Gateways with MCP Support

- **[Envoy AI Gateway](https://aigateway.envoyproxy.io/blog/mcp-implementation/)** — First-class MCP support with a lightweight proxy handling session management, server multiplexing (aggregating multiple MCP servers behind one endpoint with tool routing and collision detection), and Envoy's extension mechanisms
- **[Kong AI MCP Proxy](https://developer.konghq.com/plugins/ai-mcp-proxy/)** — Plugin that converts REST APIs into MCP tools and proxies MCP servers transparently, applying Kong's existing auth, traffic control, and observability to MCP traffic
- **[LiteLLM](https://github.com/BerriAI/litellm)** (~56,100 stars as of August 2026) — Open-source proxy/gateway for 100+ LLM providers with built-in caching (exact and semantic modes)

## Semantic Caching

Traditional caching requires exact key matches. Semantic caching uses **vector embeddings** to match queries by meaning — "What is the refund policy?" and "How do I get a refund?" resolve to the same cached answer.

### How Semantic Caching Works

1. Convert the query to a vector embedding
2. Search a vector store for similar embeddings
3. If cosine similarity exceeds threshold (typically ≥0.92), return the cached response
4. Otherwise, execute the query and cache the result with its embedding

Cache hits are typically single-digit milliseconds against seconds for a full model call — one published [Redis-backed semantic cache benchmark](https://aiechoes.substack.com/p/benchmarking-llm-exact-and-semantic) measured 3.84ms average cache latency versus 341.06ms average LLM latency. Exact figures vary by vector store, embedding model, and network path, so treat these as illustrative rather than a guaranteed number for your stack.

### GPTCache

[GPTCache](https://github.com/zilliztech/GPTCache) (~8,100 stars as of August 2026) is a purpose-built semantic cache for LLM responses with a modular architecture:

- **Embedding adapters:** OpenAI, Hugging Face, Cohere, ONNX models
- **Vector stores:** Milvus, FAISS, Hnswlib, PGVector, Chroma, Zilliz Cloud
- **Cache storage:** SQLite, DuckDB, PostgreSQL, MySQL
- **Eviction managers:** LRU and TTL-based

GPTCache integrates with LangChain and llama_index. While it doesn't have direct MCP integration, it can be wrapped around MCP tool calls at the application layer.

### Upstash Semantic Cache

[Upstash Semantic Cache](https://github.com/upstash/semantic-cache) (299 stars as of August 2026) is a managed semantic caching layer built on [Upstash Vector](https://upstash.com/docs/vector), designed for **serverless and edge** deployments. Its README example requires an Upstash Vector index:

```javascript
import { SemanticCache } from "@upstash/semantic-cache";
import { Index } from "@upstash/vector";

const index = new Index(); // reads UPSTASH_VECTOR_REST_URL / TOKEN from env
const cache = new SemanticCache({ index, minProximity: 0.95 });
await cache.set("capital of France", "Paris");
const result = await cache.get("what is France's capital?"); // → "Paris"
```

The `minProximity` parameter (0-1) controls matching strictness — 0.95 requires very high similarity, while lower values accept looser matches. Separately, Upstash also offers [Context7](https://upstash.com/blog/context7-llmtxt-cursor), a documentation-retrieval MCP server for AI coding tools; internally it uses semantic embedding, reranking, and Redis-backed caching, but it is a documentation lookup product, not a general-purpose semantic caching layer for arbitrary MCP tool calls.

### Bifrost and LiteLLM Semantic Caching

Both Bifrost and LiteLLM offer integrated semantic caching:

- **[Bifrost](https://github.com/maximhq/bifrost)** provides semantic caching with its stated [11 microsecond gateway overhead](https://github.com/maximhq/bifrost) at 5,000 requests/second
- **LiteLLM** supports `redis-semantic` and `qdrant-semantic` cache modes with configurable similarity thresholds

### When to Use Semantic Caching with MCP Tools

**Good candidates:**
- Database query tools (natural language → SQL, where phrasing varies)
- Search tools (similar search intents)
- Documentation/FAQ tools (paraphrased questions)
- Financial reporting tools ("show revenue" ≈ "display sales data")

**Poor candidates:**
- Tools with side effects (create, update, delete)
- Tools where exact parameters matter (specific IDs, dates)
- Real-time data tools (stock prices, live metrics)

### A 2025 Research Paper

A paper posted to ResearchGate in November 2025 — ["Hierarchical Semantic Caching for MCP Servers: A Multi-Tier Context-Aware Approach to Optimize AI Model Data Access"](https://www.researchgate.net/publication/397793353_Hierarchical_Semantic_Caching_for_MCP_Servers_A_Multi_Tier_Context_Aware_Approach_to_Optimize_AI_Model_Data_Access) — proposes a multi-tier semantic caching approach designed specifically for MCP servers. We could not confirm the venue's peer-review rigor, so treat this as an early academic proposal rather than a validated result; its existence does show the topic has reached academic attention, but it is one paper, not a body of research.

## Client-Side Caching Behavior

MCP caching isn't just a server concern. How clients cache (and invalidate) tool lists, resource data, and server capabilities directly affects user experience.

### Claude Desktop and Claude Code

Claude Desktop caches the `tools/list` response for each connector in memory at runtime; server-side tool schema updates are not reflected without a manual reconnect or restart, [per user-reported behavior tracked in the Claude Code issue tracker](https://github.com/anthropics/claude-code/issues/38324) (Claude Desktop and Claude Code share the same MCP client stack).

[Claude Code's documentation states](https://code.claude.com/docs/en/mcp) it supports `notifications/tools/list_changed` and automatically refreshes a server's tools, prompts, and resources when it receives one — without requiring reconnection. In practice this has been inconsistent: multiple open issues report cases where Claude Code does not refresh on receiving the notification (e.g. [#13646](https://github.com/anthropics/claude-code/issues/13646)). Treat list-changed notifications as a nice-to-have signal, not a guarantee, and don't design a caching strategy that depends on it firing reliably.

### OpenAI Agents SDK

The [OpenAI Agents SDK](https://openai.github.io/openai-agents-python/mcp/) exposes a `cache_tools_list` option on MCP server classes. Set to `True` only if tool definitions don't change frequently. To force a refresh, call `invalidate_tools_cache()` on the server instance.

### Client Capability Gaps

[PulseMCP's analysis of the MCP client ecosystem](https://www.pulsemcp.com/posts/mcp-client-capabilities-gap) argues that dynamic-update features like `list_changed` notifications and resource subscriptions are missing from the capability information clients expose during setup, forcing server authors to design for "the lowest common denominator" client rather than relying on any specific client's notification support. PulseMCP doesn't publish a definitive per-client support matrix for these features (support varies by client and changes quickly), so don't assume any specific client — including Claude's own — reliably supports notification-based invalidation; treat TTL-based expiration as the safety net that has to work regardless.

## Context Explosion Prevention

One of MCP's most practical caching problems isn't about speed or cost — it's about **context window overflow**. MCP tools can return massive responses (1MB+ HTML, large query results, file listings) that exceed LLM context limits.

### mcp-cache: Transparent Response Proxy

[mcp-cache](https://github.com/swapnilsurdi/mcp-cache) (swapnilsurdi/mcp-cache, npm package, 9 stars as of August 2026) is a transparent proxy wrapper that intercepts oversized MCP server responses and manages them via caching.

**The problem it solves:** MCP servers frequently return responses exceeding the 1,048,576-byte limit, causing "Response exceeds maximum length" errors.

**How it works:**
```bash
npx mcp-cache <your-mcp-server-command>
```

The proxy wraps any MCP server without modifications. It caches oversized responses (1-hour TTL with 5-minute cleanup) and injects six tools for accessing cached data: `query_response()` (search with text, JSONPath, regex), `get_chunk()` (retrieve specific chunks), `list_responses()`, `get_response_info()`, `refresh_response()`, and `delete_response()`.

**Configuration via environment variables:**
- `MCP_CACHE_MAX_TOKENS=25000` (client-aware: Claude Desktop 25K, Cursor 30K, Cline 25K)
- `MCP_CACHE_CHUNK_SIZE=10000`
- `MCP_CACHE_TTL=3600`

Latency overhead is under 10 milliseconds.

### mcp-refcache: Reference-Based Caching

[mcp-refcache](https://github.com/l4b4r4b4b4/mcp-refcache) (l4b4r4b4b4/mcp-refcache, PyPI package, 3 stars as of August 2026) solves context explosion by storing large API responses by reference, returning only compact previews to agents:

```json
{
  "ref_id": "a1b2c3",
  "preview": "[User(id=1), User(id=2), ... and 9998 more]",
  "total_items": 10000,
  "namespace": "session:abc123"
}
```

Instead of dumping 500KB of JSON into the agent's context, the cache returns a reference ID and preview. The agent can then request specific items or ranges.

**Three cache backends:** Memory (default), SQLite (persistent, WAL mode), Redis/Valkey (distributed)

**Namespace system for scope control:**

| Type | Scope | TTL | Use Case |
|------|-------|-----|----------|
| `public` | Global | Hours/days | API responses, static data |
| `session:<id>` | Single conversation | Minutes | Conversation context |
| `user:<id>` | User across sessions | Hours | Preferences, history |
| `org:<id>` | Organization | Long | Shared resources |

**Permission model:** Five flags (READ, WRITE, UPDATE, DELETE, EXECUTE) allow fine-grained access. The EXECUTE flag is particularly interesting — it allows agents to use values in computation WITHOUT seeing them, enabling private computation patterns.

```python
from mcp_refcache import RefCache, Namespace

cache = RefCache(namespaces=[Namespace.PUBLIC, Namespace.session("conv-123")])

@mcp.tool()
@cache.cached(namespace="session:conv-123")
async def get_large_dataset(query: str) -> dict:
    return await fetch_huge_data(query)  # 500KB → compact reference
```

### MCP Resources as Cache Optimization

[Tim Kellogg articulated a thesis](https://timkellogg.me/blog/2025/06/05/mcp-resources) (June 2025): MCP resources exist fundamentally to improve token utilization through caching. Without resource deduplication, RAG implementations duplicate large documents across multiple tool calls, wasting context tokens.

The proposed pattern: return resource references (`<result uri="rag://polar-bears/74.md" />`) initially, including full text only once per unique URI. This prevents the same document from being embedded multiple times in a conversation.

**Limitation as of Kellogg's original 2025 post:** neither Anthropic's nor OpenAI's MCP implementations fully supported resources at that time, limiting production adoption of this pattern. We couldn't independently confirm current (August 2026) resource-support status for either vendor's MCP client, so check each vendor's own MCP documentation before relying on this pattern in production.

## Cache Invalidation Patterns

Cache invalidation remains one of the hardest problems in computer science. MCP systems use several complementary strategies.

### Pattern 1: TTL-Based Expiration

The simplest and most essential strategy. Every cached item has a maximum lifetime:

| Data Type | Recommended TTL | Rationale |
|-----------|----------------|-----------|
| Tool/resource lists | 5 minutes | Rarely change during session |
| Tool call results (weather) | 1-30 minutes | Data freshness varies |
| Database query results | 5 minutes | May change frequently |
| Static resources (schemas) | 7 days | Essentially immutable |
| User profiles | 24 hours | Infrequent changes |

### Pattern 2: Event-Driven (MCP Notifications)

Uses MCP's built-in notification system for real-time invalidation. Under the [2026-07-28 spec](https://modelcontextprotocol.io/specification/2026-07-28/changelog), clients that have opted into `resourceSubscriptions` on the `subscriptions/listen` stream see:

```
Server detects change → sends a resourceSubscriptions notification on subscriptions/listen
→ Client receives notification → invalidates specific cache entry
→ Client sends resources/read → gets fresh data
```

### Pattern 3: Stale-While-Revalidate

Serve stale cached content immediately while revalidating in the background:

```
Request → Cache hit (stale but within grace period)?
  → Return stale data immediately
  → Background: fetch fresh data, update cache
```

The **refresh-ahead variant** proactively reloads data before it expires — when a cached item is accessed and nearing expiration, the cache refreshes it in the background.

### Pattern 4: LRU Eviction

FastMCP's caching middleware supports a `max_item_size` limit and can be layered with size- and statistics-tracking wrappers from [`py-key-value`](https://github.com/strawgate/py-key-value) for size-based eviction. A reasonable starting default for most workloads: retain around 1,000 most-recent entries per tool, evict when memory exceeds 100 MB — tune both numbers to your actual traffic and item sizes rather than treating them as fixed targets.

### Best Practice: Layer Multiple Strategies

Production systems should combine:
1. **TTL** as a safety net — nothing cached forever
2. **MCP notifications** for known change events
3. **LRU eviction** for memory management
4. **Manual purge** for emergency/admin use

## The 6-Layer Caching Architecture

A comprehensive MCP caching strategy operates across six layers, each addressing different concerns:

### Layer 1: Protocol Level (MCP Built-In)
- Use the `subscriptions/listen` stream (`resourceSubscriptions`, `toolsListChanged`, etc.) for real-time invalidation, per the [2026-07-28 spec](https://modelcontextprotocol.io/specification/2026-07-28/changelog)
- Read the required `ttlMs` and `cacheScope` fields on `list`/`read` responses and honor them
- Use `lastModified` annotations on resources
- Don't rely on notifications alone — treat them as a hint layered on top of TTL, not a replacement for it

### Layer 2: Prompt Caching (Anthropic API)
- Place `cache_control` on the last tool definition to cache all tools as a prefix
- Use progressive disclosure / deferred tool loading for large tool sets (85-98% token reduction)
- Structure prompts in cache-friendly order: tools → system → messages
- Use up to 4 breakpoints for different change frequencies

### Layer 3: Server-Side Caching
- Use FastMCP `ResponseCachingMiddleware` for Python servers
- Configure per-method TTLs (5 min for lists, 1 hour for reads/calls)
- Exclude tools with side effects from caching
- Use Redis or SQLite for persistent/distributed deployments

### Layer 4: Gateway/Proxy Caching
- Deploy ContextForge or Envoy AI Gateway for multi-server setups
- Cache `resources/list`, `prompts/list`, `tools/list` at the gateway
- Never cache `tools/call` at the gateway level
- Use CDN caching for static MCP schemas and documentation

### Layer 5: Semantic Caching
- Apply to natural language tool inputs (search, queries, Q&A)
- Use GPTCache, Upstash, or Bifrost depending on deployment model
- Set similarity threshold ≥ 0.92 to avoid false matches
- Exclude tools with side effects or exact-parameter requirements

### Layer 6: Context Window Optimization
- Use mcp-refcache for reference-based responses (prevent context explosion)
- Use mcp-cache as a proxy for oversized response management
- Implement the SQLite-as-cache pattern for document-based MCP servers
- Monitor token usage via prompt-caching-mcp

## Ecosystem at a Glance

Star counts below were checked against the GitHub API on August 11, 2026.

| Project | Type | Stars | Key Feature |
|---------|------|-------|-------------|
| **[FastMCP](https://github.com/PrefectHQ/fastmcp)** | Server framework | ~27,200 | Built-in ResponseCachingMiddleware |
| **[LiteLLM](https://github.com/BerriAI/litellm)** | LLM proxy/gateway | ~56,100 | Semantic + exact caching for 100+ providers |
| **[GPTCache](https://github.com/zilliztech/GPTCache)** | Semantic cache | ~8,100 | Purpose-built LLM semantic cache (FAISS/Milvus) |
| **[ContextForge](https://github.com/IBM/mcp-context-forge)** | MCP gateway | ~4,300 | IBM gateway with Redis federation + caching |
| **[Bifrost](https://github.com/maximhq/bifrost)** | AI gateway | ~7,200 | 11μs overhead (per vendor benchmark), semantic caching, native MCP |
| **[Redis MCP](https://github.com/redis/mcp-redis)** | Data server | 561 | Official Redis MCP interface |
| **[Upstash Semantic](https://github.com/upstash/semantic-cache)** | Semantic cache | 299 | Edge/serverless semantic caching |
| **[mcp-cache](https://github.com/swapnilsurdi/mcp-cache)** | Response proxy | 9 | Transparent proxy for oversized responses |
| **[mcp-refcache](https://github.com/l4b4r4b4b4/mcp-refcache)** | Reference cache | 3 | Context explosion prevention + permissions |
| **[prompt-caching](https://github.com/flightlesstux/prompt-caching)** | Debug tool | — | Analyze/debug Anthropic prompt caching in Claude Code |

## Getting Started

**If you're just starting with MCP caching**, prioritize in this order:

1. **Enable Anthropic prompt caching** — Place `cache_control` on your last tool definition. This alone can cut input costs by 90% with zero server changes.

2. **Add FastMCP caching middleware** — If you're running Python MCP servers, one line of middleware adds server-side caching with sensible defaults.

3. **Consider progressive disclosure** — If you have more than 20 tools, deferred loading can reduce token overhead by 85-98%.

4. **Deploy a gateway** — When running multiple MCP servers, ContextForge or Bifrost adds caching, rate limiting, and observability at the infrastructure level.

5. **Evaluate semantic caching** — If your agents handle natural language queries with varied phrasing, semantic caching can meaningfully cut cost and latency on top of exact-match/prompt caching. Published case studies report a wide range (roughly 30% to over 70% cost reduction) depending on how repetitive your query patterns are — there's no single number to plan around, so measure your own hit rate before committing to it.

6. **Address context overflow** — If your tools return large responses, wrap them with mcp-cache or mcp-refcache to prevent context window exhaustion.

## Further Reading

For related topics covered in other ChatForest guides:

- **[MCP Server Performance Tuning](/guides/mcp-server-performance-tuning/)** — Latency optimization, connection pooling, and benchmarking
- **[MCP Cost Optimization](/guides/mcp-cost-optimization/)** — Budget management, token efficiency, and cost monitoring
- **[MCP Gateway and Proxy Patterns](/guides/mcp-gateway-proxy-patterns/)** — Gateway architectures and proxy deployment
- **[MCP in Production](/guides/mcp-in-production/)** — Production deployment patterns and reliability
- **[MCP Server Deployment and Hosting](/guides/mcp-server-deployment-hosting/)** — Infrastructure and hosting options
- **[MCP Edge Computing Patterns](/guides/mcp-edge-computing-patterns/)** — Edge caching and CDN integration
- **[MCP Serverless Deployment](/guides/mcp-serverless-deployment/)** — Serverless function caching strategies
- **[MCP AI Safety and Guardrails](/guides/mcp-ai-safety-guardrails/)** — Security considerations for cached data
