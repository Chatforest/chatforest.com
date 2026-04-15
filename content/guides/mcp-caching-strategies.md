---
title: "MCP Caching Strategies: Prompt Caching, Server-Side Caching, Semantic Caching, and Gateway Patterns"
date: 2026-03-28T22:00:00+09:00
description: "A comprehensive guide to caching in MCP systems — covering Anthropic prompt caching (90% cost reduction), FastMCP ResponseCachingMiddleware, server-side patterns (Redis"
content_type: "Guide"
card_description: "A typical MCP setup with five servers burns 55,000+ tokens before the conversation starts. This guide covers every caching layer — from Anthropic prompt caching to semantic caching — that can cut costs by 90%, reduce latency by 85%, and keep your agents fast."
last_refreshed: 2026-04-15
---

A typical MCP deployment with five servers and 58 tools consumes over 55,000 tokens before the first user message. Add a few more integrations — Jira alone uses ~17,000 tokens — and you're burning 100,000+ tokens of context window on tool definitions alone. Every API call that could return cached data but doesn't is wasted latency and money. At Anthropic's Opus 4.6 pricing, an uncached 100K-token prompt costs $0.50 per request; with prompt caching, that drops to $0.05.

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
| Initialization/capability negotiation | Per-connection state |

**The golden rule:** Cache `list` and `read` operations freely. Cache `call` operations only at the server level, only for tools you've verified are idempotent and side-effect-free.

## Protocol-Level Caching: What MCP Provides Today

The MCP specification (2025-11-25 revision) does not define protocol-level caching primitives like HTTP `Cache-Control` headers or ETags. MCP operates over JSON-RPC, which is stateless at the message level. However, the protocol provides **notification-based cache invalidation** — a mechanism for servers to tell clients when cached data is stale.

### Notification-Based Invalidation

MCP defines several notifications that function as cache invalidation signals:

**Resource notifications:**
- `notifications/resources/list_changed` — available resources have changed
- `notifications/resources/updated` — a specific subscribed resource has changed
- `resources/subscribe` / `resources/unsubscribe` — client subscribes to specific resource URI changes

**Tool and prompt notifications:**
- `notifications/tools/list_changed` — available tools have changed
- `notifications/prompts/list_changed` — available prompts have changed

Servers must declare support for these capabilities during initialization:

```json
{
  "capabilities": {
    "resources": { "subscribe": true, "listChanged": true },
    "tools": { "listChanged": true },
    "prompts": { "listChanged": true }
  }
}
```

### Resource Annotations

The spec supports a `lastModified` annotation on resources (ISO 8601 timestamp), which clients can use for staleness checks:

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

This is the closest thing MCP has to an ETag today — a timestamp that clients can compare to decide whether to re-fetch.

### What's Coming: ETags and TTLs (June 2026)

The MCP team is actively working on protocol-level caching primitives. From the official 2026 roadmap:

> "The team is considering adding Time-To-Live (TTL) values and version identifiers (such as ETags) to data, which would let clients make intelligent caching decisions independently of the notification stream."

This is targeted for the **June 2026 specification release**, along with explicit subscription streams and well-defined gateway/proxy intermediary behavior. Until then, caching must be implemented at higher layers.

## Anthropic Prompt Caching: The Biggest Win

If you're using Claude models with MCP, Anthropic's prompt caching is the single highest-impact optimization available. Cached input tokens cost **10x less** than regular input tokens, and latency drops up to **85%** (a 100K-token prompt goes from 11.5 seconds to 2.4 seconds).

### How It Works

Anthropic caches prompt prefixes in strict order: **tools → system → messages**. When consecutive API calls share the same prefix, everything before the first change point is served from cache.

**Pricing per million tokens:**

| Model | Base Input | 5-min Cache Write | 1-hour Cache Write | Cache Read |
|-------|-----------|-------------------|--------------------|-----------|
| Claude Opus 4.6 | $5.00 | $6.25 (1.25x) | $10.00 (2x) | $0.50 (0.1x) |
| Claude Sonnet 4.6 | $3.00 | $3.75 | $6.00 | $0.30 |
| Claude Haiku 4.5 | $1.00 | $1.25 | $2.00 | $0.10 |

**Minimum cacheable tokens:**

| Model | Minimum |
|-------|---------|
| Claude Opus 4.6/4.5 | 4,096 tokens |
| Claude Sonnet 4.6 | 2,048 tokens |
| Claude Sonnet 4.5/4/3.7 | 1,024 tokens |
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

**Invalidation rules:** The tool cache is invalidated when tool definitions change (names, descriptions, parameters). Changes to web search toggle, citations toggle, speed settings, or tool choice do NOT invalidate the tool cache.

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
response = client.messages.create(
    model="claude-opus-4-6",
    max_tokens=1024,
    cache_control={"type": "ephemeral"},  # Automatic breakpoint management
    system="Your system prompt...",
    messages=[...],
)
```

This is the simplest way to enable prompt caching for multi-turn MCP conversations. The API handles breakpoint placement automatically, optimizing for cache hit rates without requiring explicit `cache_control` annotations on individual content blocks.

### Progressive Disclosure: 85-98% Token Reduction

Anthropic's advanced tool use feature (beta header `advanced-tool-use-2025-11-20`) introduced **deferred tool loading** — instead of loading all tool definitions upfront, a Tool Search Tool discovers tools on demand.

Tools marked with `defer_loading: true` are excluded from the initial prompt. Claude only sees the Tool Search Tool plus critical tools (`defer_loading: false`). When the model needs a deferred tool, it searches for it, and the tool definition is loaded just in time.

**Results from Anthropic's benchmarks:**
- **85% reduction** in tool definition tokens
- End-to-end workflow: **150K tokens → 2K tokens** (98.7% reduction)
- Accuracy improvements: Opus 4 from 49% → 74%, Opus 4.5 from 79.5% → 88.1%

This directly enables better prompt cache hit rates — fewer tokens in the tools prefix means the prefix changes less often, which means more cache hits.

## Server-Side Caching

### FastMCP ResponseCachingMiddleware

FastMCP (~24,500 stars), the leading Python MCP framework, provides a built-in `ResponseCachingMiddleware` that caches responses for all MCP methods.

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

**Cache backends (FastMCP 2.13+):**
- Default: in-memory via `MemoryStore()` with LRU eviction
- Production: Redis, SQLite, Elasticsearch via composable wrapper system
- Wrappers: `LimitSizeWrapper` (per-item size limits), `StatisticsWrapper` (cache metrics)

Cache keys are derived from the method name plus arguments, and the cache is automatically invalidated when the server sends `list_changed` notifications.

### Redis MCP Server

The official Redis MCP Server (redis/mcp-redis, 479 stars) provides a natural language interface for AI agents to manage Redis data. While not a caching middleware itself, it enables MCP-native caching patterns — agents can directly store and retrieve cached results using Redis data structures (hashes, lists, sets, sorted sets, streams, JSON).

### The SQLite-as-Cache Pattern

A recognized architecture pattern in MCP database servers uses SQLite as a disposable cache layer:

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

Production implementations include hugo-memex (951 pages of personal knowledge), chartfold (medical records), arkiv (personal data archives), and repoindex (repository catalogs).

### Production Redis Caching Pattern

For production MCP servers that need distributed caching, a common pattern uses SHA-256 hashing for cache key generation:

```
Tool request → Generate SHA-256 key from normalized, sorted arguments
    → Cache check → Hit? Return cached result
                  → Miss? Execute tool → Store with TTL → Return
```

**Performance targets for a well-tuned cache:**
- 60-80% hit rate
- 150-300ms latency reduction per cached request
- 70-90% reduction in downstream API costs

## Gateway and Proxy Caching

For multi-server MCP deployments, caching at the gateway layer avoids redundant calls across your entire infrastructure.

### Gravitee MCP API Gateway

Gravitee's approach to MCP gateway caching defines clear rules about what belongs in a gateway cache:

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

ContextForge (IBM/mcp-context-forge, ~3,600 stars) is an open-source registry and proxy that federates MCP servers, A2A servers, and REST/gRPC APIs into a unified endpoint.

**Caching features:**
- Redis-backed caching for production deployments
- Multi-cluster federation on Kubernetes with Redis
- Scalable from SQLite + memory cache (development) to PostgreSQL + Redis (production)
- Protocol conversion: stdio ↔ SSE ↔ Streamable HTTP

ContextForge also provides rate limiting, authentication, automatic retries, 40+ plugins, and OpenTelemetry tracing — making it a full-featured gateway for MCP infrastructure.

### Bifrost AI Gateway

Bifrost (maximhq/bifrost, ~3,800 stars) is a high-performance open-source AI gateway built in Go:
- **11 microsecond overhead** at 5,000 requests/second
- Native MCP gateway support for agentic workflows
- **Semantic caching** as a first-class feature (covered in the next section)
- Automatic failbacks across 20+ LLM providers
- Virtual key budget management with hierarchical controls

### CDN Caching for Static MCP Assets

For MCP servers that serve static content (schemas, documentation, templates), Cloudflare Workers middleware can cache immutable resources with aggressive headers:

```
Cache-Control: public, max-age=604800, immutable
```

This offloads approximately 40% of requests to CDN edges. For medium-traffic applications, this can reduce origin server costs by $400-800 per month.

**Important note for Streamable HTTP:** The MCP spec recommends servers include the `X-Accel-Buffering: no` header for SSE streams to prevent reverse proxies (particularly nginx) from buffering events and introducing latency.

### Other Gateways with MCP Support

- **Envoy AI Gateway** — First-class MCP support with lightweight proxy handling session management, stream multiplexing, and Envoy extension mechanisms
- **Kong AI MCP Proxy** — Enterprise plugin that converts APIs into MCP tools and proxies MCP servers transparently
- **LiteLLM** (BerriAI/litellm, ~43,300 stars) — Open-source proxy for 100+ LLM providers with built-in caching (exact and semantic modes)

## Semantic Caching

Traditional caching requires exact key matches. Semantic caching uses **vector embeddings** to match queries by meaning — "What is the refund policy?" and "How do I get a refund?" resolve to the same cached answer.

### How Semantic Caching Works

1. Convert the query to a vector embedding
2. Search a vector store for similar embeddings
3. If cosine similarity exceeds threshold (typically ≥0.92), return the cached response
4. Otherwise, execute the query and cache the result with its embedding

Cache hits return in under 5 milliseconds compared to 2-5 seconds for full model calls.

### GPTCache

GPTCache (zilliztech/GPTCache, ~8,000 stars) is a purpose-built semantic cache for LLM responses with a modular architecture:

- **Embedding adapters:** OpenAI, Hugging Face, Cohere, ONNX models
- **Vector stores:** Milvus, FAISS, Hnswlib, PGVector, Chroma, Zilliz Cloud
- **Cache storage:** SQLite, DuckDB, PostgreSQL, MySQL
- **Eviction managers:** LRU and TTL-based

GPTCache integrates with LangChain and llama_index. While it doesn't have direct MCP integration, it can be wrapped around MCP tool calls at the application layer.

### Upstash Semantic Cache

Upstash Semantic Cache (upstash/semantic-cache, 294 stars) is a managed semantic caching layer built on Upstash Vector, designed for **serverless and edge** deployments:

```javascript
import { SemanticCache } from "@upstash/semantic-cache";

const cache = new SemanticCache({ minProximity: 0.95 });
await cache.set("capital of France", "Paris");
const result = await cache.get("what is France's capital?"); // → "Paris"
```

The `minProximity` parameter controls matching strictness — 0.95 requires very high similarity, while 0.75 accepts looser matches. Upstash also offers a Context7 MCP Server that exposes semantic caching tools directly to MCP clients.

### Bifrost and LiteLLM Semantic Caching

Both Bifrost and LiteLLM offer integrated semantic caching:

- **Bifrost** reports **30-50% cost reductions** with semantic matching (vs. 15-20% with exact-match caching), with 11 microsecond overhead
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

### A 2026 Research Paper

A paper published on ResearchGate in 2026 — "Hierarchical Semantic Caching for MCP Servers: A Multi-Tier Context-Aware Approach to Optimize AI Model Data Access" — proposes a multi-tier semantic caching approach designed specifically for MCP servers. The existence of peer-reviewed research on MCP-specific caching signals growing academic interest in this space.

## Client-Side Caching Behavior

MCP caching isn't just a server concern. How clients cache (and invalidate) tool lists, resource data, and server capabilities directly affects user experience.

### Claude Desktop and Claude Code

Claude Desktop caches tool manifests in memory at runtime. Even if the MCP server updates tool definitions, the client uses cached data until restart. There is no option to disable this cache or force a fresh fetch — tool metadata changes require a client restart.

Claude Code handles this better: it supports `notifications/tools/list_changed` notifications, automatically refreshing capabilities when a server sends a list_changed notification without requiring reconnection.

### OpenAI Agents SDK

The OpenAI Agents SDK exposes a `cache_tools_list` option on MCP server classes. Set to `True` only if tool definitions don't change frequently. To force a refresh, call `invalidate_tools_cache()` on the server instance.

### Client Capability Gaps

According to PulseMCP analysis, client support for caching-related features is uneven:
- `notifications/tools/list_changed` — growing support (Claude Code, VS Code, Gemini CLI)
- Resource subscriptions (`resources/subscribe`) — poorly supported across clients
- `notifications/resources/updated` — limited client support

This gap means servers can't rely on notification-based invalidation alone — TTL-based expiration remains essential as a safety net.

## Context Explosion Prevention

One of MCP's most practical caching problems isn't about speed or cost — it's about **context window overflow**. MCP tools can return massive responses (1MB+ HTML, large query results, file listings) that exceed LLM context limits.

### mcp-cache: Transparent Response Proxy

mcp-cache (swapnilsurdi/mcp-cache, npm package) is a transparent proxy wrapper that intercepts oversized MCP server responses and manages them via caching.

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

mcp-refcache (l4b4r4b4b4/mcp-refcache, PyPI package) solves context explosion by storing large API responses by reference, returning only compact previews to agents:

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

Tim Kellogg articulated a compelling thesis: MCP resources exist fundamentally to improve token utilization through caching. Without resource deduplication, RAG implementations duplicate large documents across multiple tool calls, wasting context tokens.

The proposed pattern: return resource references (`<result uri="rag://polar-bears/74.md" />`) initially, including full text only once per unique URI. This prevents the same document from being embedded multiple times in a conversation.

**Current limitation:** Neither Anthropic nor OpenAI's MCP implementations fully support resources yet, limiting production adoption of this pattern.

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

Uses MCP's built-in notification system for real-time invalidation:

```
Server detects change → sends notifications/resources/updated
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

FastMCP's `LimitSizeWrapper` implements size-based eviction. A reasonable default: retain 1,000 most-recent entries per tool, evict when memory exceeds 100 MB.

### Best Practice: Layer Multiple Strategies

Production systems should combine:
1. **TTL** as a safety net — nothing cached forever
2. **MCP notifications** for known change events
3. **LRU eviction** for memory management
4. **Manual purge** for emergency/admin use

## The 6-Layer Caching Architecture

A comprehensive MCP caching strategy operates across six layers, each addressing different concerns:

### Layer 1: Protocol Level (MCP Built-In)
- Use `notifications/resources/updated` and `list_changed` for real-time invalidation
- Declare `subscribe` and `listChanged` capabilities on your servers
- Use `lastModified` annotations on resources
- Prepare for ETags/TTL in the June 2026 spec

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

| Project | Type | Stars | Key Feature |
|---------|------|-------|-------------|
| **FastMCP** | Server framework | ~24,500 | Built-in ResponseCachingMiddleware |
| **LiteLLM** | LLM proxy | ~43,300 | Semantic + exact caching for 100+ providers |
| **GPTCache** | Semantic cache | ~8,000 | Purpose-built LLM semantic cache (FAISS/Milvus) |
| **ContextForge** | MCP gateway | ~3,600 | IBM gateway with Redis federation + caching |
| **Bifrost** | AI gateway | ~3,800 | 11μs overhead, semantic caching, native MCP |
| **Redis MCP** | Data server | 479 | Official Redis MCP interface |
| **Upstash Semantic** | Semantic cache | 294 | Edge/serverless semantic caching |
| **ib-mcp-cache-server** | Cache server | 24 | Automatic token reduction between LLM calls |
| **mcp-cache** | Response proxy | 6 | Transparent proxy for oversized responses |
| **mcp-refcache** | Reference cache | 1 | Context explosion prevention + permissions |
| **prompt-caching-mcp** | Debug tool | — | Analyze/debug Anthropic prompt caching |

## Getting Started

**If you're just starting with MCP caching**, prioritize in this order:

1. **Enable Anthropic prompt caching** — Place `cache_control` on your last tool definition. This alone can cut input costs by 90% with zero server changes.

2. **Add FastMCP caching middleware** — If you're running Python MCP servers, one line of middleware adds server-side caching with sensible defaults.

3. **Consider progressive disclosure** — If you have more than 20 tools, deferred loading can reduce token overhead by 85-98%.

4. **Deploy a gateway** — When running multiple MCP servers, ContextForge or Bifrost adds caching, rate limiting, and observability at the infrastructure level.

5. **Evaluate semantic caching** — If your agents handle natural language queries with varied phrasing, semantic caching can deliver 30-50% additional cost reduction.

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
