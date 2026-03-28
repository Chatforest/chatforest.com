# Research: MCP Caching Strategies and Patterns

**Research Date:** 2026-03-28
**Purpose:** Comprehensive research for writing a technical guide on MCP caching

---

## 1. MCP Protocol-Level Caching

### Current Spec (2025-06-18): No Built-In Cache Headers

The MCP specification does **not** define protocol-level caching primitives like HTTP Cache-Control headers, ETags, or If-None-Match. MCP operates over JSON-RPC, which is inherently stateless at the message level. However, the spec provides **notification-based cache invalidation** mechanisms.

### Notification-Based Cache Invalidation (In Spec)

The protocol defines several notifications that serve as cache invalidation signals:

**Resource notifications:**
- `notifications/resources/list_changed` — Server sends when available resources change (requires `listChanged` capability)
- `notifications/resources/updated` — Server sends when a subscribed resource changes
- `resources/subscribe` / `resources/unsubscribe` — Client subscribes to specific resource URI changes

**Tool notifications:**
- `notifications/tools/list_changed` — Server sends when available tools change (requires `listChanged` capability)

**Prompt notifications:**
- `notifications/prompts/list_changed` — Server sends when available prompts change

**Capability declaration** (server must declare support):
```json
{
  "capabilities": {
    "resources": { "subscribe": true, "listChanged": true },
    "tools": { "listChanged": true },
    "prompts": { "listChanged": true }
  }
}
```

**Resource annotations with `lastModified`:**
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

### Planned Protocol-Level Caching (2026 Roadmap)

The MCP team is actively exploring adding **TTL values and version identifiers (ETags)** to data. From the official roadmap blog:

> "The team is considering adding Time-To-Live (TTL) values and version identifiers (such as ETags) to data, which would let clients make intelligent caching decisions independently of the notification stream."

This is targeted for the **June 2026 specification release**, with SEPs (Spec Enhancement Proposals) being finalized in Q1 2026.

Additional roadmap items related to caching:
- **Explicit subscription streams** to replace the general-purpose GET stream
- **Session management at the data model layer** (cookie-like mechanism)
- **Gateway and proxy patterns** with well-defined intermediary behavior

**Sources:**
- MCP Resources Spec: https://modelcontextprotocol.io/specification/2025-06-18/server/resources
- MCP Tools Spec: https://modelcontextprotocol.io/specification/2025-06-18/server/tools
- MCP 2026 Roadmap: https://blog.modelcontextprotocol.io/posts/2026-mcp-roadmap/
- MCP Transport Future: https://blog.modelcontextprotocol.io/posts/2025-12-19-mcp-transport-future/

---

## 2. MCP Server-Side Caching

### FastMCP ResponseCachingMiddleware (Python)

**Repository:** PrefectHQ/fastmcp — 24,088 stars
**PyPI:** `fastmcp`
**Docs:** https://gofastmcp.com/python-sdk/fastmcp-server-middleware-caching

FastMCP (the leading Python MCP framework) provides a built-in `ResponseCachingMiddleware` that caches responses for all MCP methods.

**Cacheable wrapper classes:**
- `CachableResourceContent` / `CachableResourceResult` — wrap resource responses
- `CachableToolResult` — wraps tool execution results
- `CachableMessage` / `CachablePromptResult` — wraps prompt results

**Default TTL values:**
| Method | Default TTL |
|--------|-------------|
| `list_tools` | 5 minutes (300s) |
| `list_resources` | 5 minutes (300s) |
| `list_prompts` | 5 minutes (300s) |
| `read_resource` | 1 hour (3600s) |
| `get_prompt` | 1 hour (3600s) |
| `call_tool` | 1 hour (3600s) |

**Configuration options:**
- Per-method settings: `ListToolsSettings`, `CallToolSettings`, `ReadResourceSettings`, `GetPromptSettings`
- `ttl` — cache lifetime in seconds
- `enabled` — boolean toggle
- `included_tools` / `excluded_tools` — filter which tools get cached
- `max_item_size` — max size for cacheable items (default 1 MB)

**Cache backend:**
- Default: in-memory via `MemoryStore()`
- Wrapped with `LimitSizeWrapper` (enforces per-item size) and `StatisticsWrapper` (tracks metrics)
- Cache keys derived from method name + arguments
- Cache invalidation via server notifications

**Storage backends (FastMCP 2.13+):**
FastMCP's composable wrapper system supports layering encryption, TTLs, and caching onto any backend: local filesystem, Redis, Elasticsearch, SQLite.

### Redis MCP Server (Official)

**Repository:** redis/mcp-redis — 465 stars
**Docs:** https://redis.io/docs/latest/integrate/redis-mcp/

The official Redis MCP Server provides a natural language interface for AI agents to manage Redis data. While not a caching middleware itself, it enables MCP-native caching patterns:

**Use cases:**
- Session management and conversation history
- Real-time caching of tool results
- Rate limiting
- Semantic search for RAG via Redis Vector Search

**Supported data structures:** Hashes, lists, sets, sorted sets, streams, JSON

### Production Redis Caching Pattern for MCP

From the MakeAIHQ guide, a production-ready `MCPCacheManager` pattern:

**Cache key generation:** SHA-256 hashing of normalized, sorted arguments
- "weather in NYC" and "show NYC weather" generate identical cache keys
- Default TTLs vary by tool type (weather: 30 min, database queries: 5 min)

**Architecture flow:**
```
Tool request → Cache check → Hit? Return cached
                           → Miss? Execute tool → Store with TTL → Return
```

**Performance targets:**
- 60-80% hit rate
- 150-300ms latency reduction per cached request
- 70-90% cost reduction in API expenses

### Database Query Caching: The SQLite-as-Cache Pattern

**Source:** https://dev.to/queelius/the-mcp-pattern-sqlite-as-the-ai-queryable-cache-34g6

A recognized pattern in MCP database servers uses a three-layer architecture:

```
Domain files (ground truth)
    ↓ index
SQLite database (read-only cache with FTS5)
    ↓ expose
MCP server (tools + resources → AI assistant)
```

**Key principle:** Domain files are always canonical; the database is a disposable cache rebuilt from them at any time.

**Benefits:**
- Structured queries over unstructured data (YAML front matter, JSON, scattered exports)
- Full-text search via FTS5 virtual tables with porter stemming
- Read-only enforcement via SQLite's authorizer callback
- WAL mode for concurrent readers
- Zero configuration overhead

**Production implementations:** hugo-memex (951 pages), chartfold (medical records), arkiv (personal data), repoindex (repository catalogs)

**Sources:**
- FastMCP Caching: https://gofastmcp.com/python-sdk/fastmcp-server-middleware-caching
- FastMCP Source: https://github.com/jlowin/fastmcp/blob/main/src/fastmcp/server/middleware/caching.py
- Redis MCP: https://redis.io/blog/introducing-model-context-protocol-mcp-for-redis/
- MakeAIHQ Guide: https://makeaihq.com/guides/cluster/mcp-server-caching-strategies
- SQLite Pattern: https://dev.to/queelius/the-mcp-pattern-sqlite-as-the-ai-queryable-cache-34g6

---

## 3. MCP Client-Side Caching

### Claude Desktop / Claude Code

**Tool list caching:** Claude Desktop caches the MCP tool manifest/tools data in memory at runtime. Even if the MCP server updates tool definitions, the client continues using cached data until restart.

**Known limitation:** There is no option in the client or config to disable this cache or force a fresh fetch. Tool metadata requires a client restart to reflect changes (tracked in GitHub issue anthropics/claude-code#7519).

**list_changed notifications:** Claude Code supports MCP `notifications/tools/list_changed` notifications, allowing servers to dynamically update available tools, prompts, and resources without requiring reconnection. The client automatically refreshes capabilities when a list_changed notification is received.

### OpenAI Agents SDK

**`cache_tools_list` option:** The OpenAI Agents SDK exposes `cache_tools_list` on MCP server classes. Set to `True` only if tool definitions don't change frequently. To force a fresh list, call `invalidate_tools_cache()` on the server instance.

### Cursor

**More dynamic:** Unlike Claude Desktop, Cursor picks up MCP config changes automatically without restart.

### Spring AI MCP Client

**Notification support:** Spring AI doesn't maintain internal state about updated tools by default, but provides a customization listener to implement smart tool caching. Supports `notifications/tools/list_changed` for dynamic tool updates.

### Client Capability Support Gap

From PulseMCP analysis, many MCP clients don't fully support all notification types:
- Resource subscriptions (`resources/subscribe`) — poorly supported across clients
- `notifications/resources/updated` — limited client support
- `notifications/tools/list_changed` — growing support (Claude Code, VS Code, Gemini CLI all adding it)

**Sources:**
- Claude Code Issue: https://github.com/anthropics/claude-code/issues/7519
- Spring AI Dynamic Tools: https://spring.io/blog/2025/05/04/spring-ai-dynamic-tool-updates-with-mcp/
- PulseMCP Client Gap: https://www.pulsemcp.com/posts/mcp-client-capabilities-gap
- Gemini CLI Issue: https://github.com/google-gemini/gemini-cli/issues/13850
- LibreChat Issue: https://github.com/danny-avila/LibreChat/issues/7117

---

## 4. Token/Context Caching

### Anthropic Prompt Caching

**Docs:** https://platform.claude.com/docs/en/docs/build-with-claude/prompt-caching

Anthropic's prompt caching is directly relevant to MCP because tool definitions consume significant tokens.

**The problem:** A five-server MCP setup with 58 tools consumes ~55K tokens before conversation starts. Adding more servers (e.g., Jira alone uses ~17K tokens) quickly reaches 100K+ token overhead.

**How prompt caching works:**
- Cache prefixes created in strict order: **tools → system → messages**
- Cached input tokens are **10x cheaper** than regular input tokens
- Latency reduction up to **85%** (100K-token prompt: 11.5s → 2.4s)

**Pricing (per million tokens):**

| Model | Base Input | 5m Cache Write | 1h Cache Write | Cache Read |
|-------|-----------|----------------|----------------|------------|
| Claude Opus 4.6 | $5.00 | $6.25 (1.25x) | $10.00 (2x) | $0.50 (0.1x) |
| Claude Sonnet 4.6 | $3.00 | $3.75 | $6.00 | $0.30 |
| Claude Haiku 4.5 | $1.00 | $1.25 | $2.00 | $0.10 |

**TTL options:**
- 5-minute cache (default) — free refresh on cache hits
- 1-hour cache — 2x write cost, for less frequently used prompts

**Minimum cacheable tokens:**

| Model | Minimum |
|-------|---------|
| Claude Opus 4.6/4.5 | 4,096 tokens |
| Claude Sonnet 4.6 | 2,048 tokens |
| Claude Sonnet 4.5/4/3.7 | 1,024 tokens |
| Claude Haiku 4.5 | 4,096 tokens |

**Tool definitions caching strategy:**
Place `cache_control` on the **last tool** in the `tools` array to cache all preceding tools:
```json
{
  "tools": [
    { "name": "search_documents", "input_schema": {...} },
    { "name": "get_document", "input_schema": {...},
      "cache_control": {"type": "ephemeral"} }
  ]
}
```

**Cache invalidation rules:** Tool cache is invalidated when tool definitions change (names, descriptions, parameters). Changes to web search toggle, citations toggle, speed settings, or tool choice do NOT invalidate tool cache.

### Anthropic's Progressive Disclosure / Deferred Tool Loading

**Source:** https://www.anthropic.com/engineering/advanced-tool-use
**Beta header:** `advanced-tool-use-2025-11-20`

Instead of loading all tool definitions upfront, the **Tool Search Tool** discovers tools on-demand:

- Tools marked with `defer_loading: true` are discoverable but not loaded into context initially
- Claude only sees the Tool Search Tool plus critical tools (`defer_loading: false`)
- Deferred tools excluded from initial prompt, so system prompt and core tools remain cacheable

**Results:**
- **85% reduction** in token usage for tool definitions
- End-to-end workflow: **150K tokens → 2K tokens** (98.7% reduction)
- Accuracy improvements: Opus 4 from 49% → 74%, Opus 4.5 from 79.5% → 88.1%

**Announced:** January 14, 2026 by Thariq Shihipar

### Multi-Turn Conversation Caching Strategy

Automatic caching moves the breakpoint forward as conversations grow:

| Request | Behavior |
|---------|----------|
| Request 1 | System + User(1) + Asst(1) + User(2) written to cache |
| Request 2 | Previous read from cache; Asst(2) + User(3) written |
| Request 3 | Previous read from cache; Asst(3) + User(4) written |

Up to 4 explicit cache breakpoints per request for fine-grained control over different change frequencies (tools rarely change, context updates daily, conversation grows per turn).

**Sources:**
- Prompt Caching: https://platform.claude.com/docs/en/docs/build-with-claude/prompt-caching
- Advanced Tool Use: https://www.anthropic.com/engineering/advanced-tool-use
- Geeky Gadgets: https://www.geeky-gadgets.com/progressive-disclosure-mcp/
- Token Bloat Article: https://medium.com/ai-software-engineer/anthropic-just-solved-ai-agent-bloat-150k-tokens-down-to-2k-code-execution-with-mcp-8266b8e80301

---

## 5. MCP Gateway/Proxy Caching

### Gravitee MCP API Gateway

**Source:** https://www.gravitee.io/blog/mcp-api-gateway-explained-protocols-caching-and-remote-server-integration

**What to cache:**
- `resources/read` results (relatively static data)
- `resources/list`, `resources/templates/list` results
- `prompts/list` and `prompts/get`
- `tools/list` (if tool sets don't change frequently)

**What NOT to cache:**
- `tools/call` (side effects)
- Notifications
- Initialization and capability negotiation

**Cache key design:**
```
resources/read|file:///docs/foo.md|serverVersion=123
```
Keys incorporate: method name, URI/parameters, server version/timestamp, authentication context.

**Cache invalidation strategies:**
1. TTL — expiring entries after a duration
2. Versioning/ETags — upstream servers include version; gateway checks validity
3. Notifications — servers notify gateway via subscription mechanisms

**Multi-layer cache architecture:**
- In-memory cache within gateway (fastest, per-instance)
- Distributed cache (Redis/Memcached) for multiple gateway instances
- Client-side caching when applicable

### IBM ContextForge MCP Gateway

**Repository:** IBM/mcp-context-forge — 3,489 stars
**PyPI:** `mcp-contextforge-gateway`
**Docs:** https://ibm.github.io/mcp-context-forge/

An open-source registry and proxy that federates MCP servers, A2A servers, and REST/gRPC APIs into a unified endpoint.

**Caching features:**
- Redis-backed caching for production deployments
- Multi-cluster federation on Kubernetes with Redis
- Scalable from SQLite + memory cache (dev) to PostgreSQL + Redis (production)
- Protocol conversion: stdio ↔ SSE ↔ Streamable HTTP

**Additional features:** Rate limiting, auth, retries, 40+ plugins, OpenTelemetry tracing

### Envoy AI Gateway

**Source:** https://aigateway.envoyproxy.io/blog/mcp-implementation/

First-class MCP support, leveraging Envoy's architecture:
- Lightweight MCP Proxy handling session management
- Multiplexes streams
- Bridges stateful JSON-RPC with Envoy extension mechanisms
- Serves MCP servers at HTTP endpoints as Streamable HTTP MCP servers

### Kong AI MCP Proxy

**Docs:** https://developer.konghq.com/plugins/ai-mcp-proxy/

**Features:**
- Convert APIs into MCP tools
- Proxy MCP servers transparently
- Expose multiple MCP tools for AI clients
- Observe MCP traffic in real time

### CDN Caching for Static MCP Assets

From the MakeAIHQ guide, Cloudflare Workers middleware can cache immutable MCP resources:

**Targets:** MCP schemas, documentation, widget templates (rarely updated)
**Headers:** `"public, max-age=604800, immutable"` (7-day retention)
**Impact:** Offloads ~40% of requests to CDN edges, reducing origin server costs $400-800/month for medium-traffic applications

**Important Streamable HTTP note:** The MCP spec recommends servers include `X-Accel-Buffering: no` header for SSE streams to prevent reverse proxies (nginx) from buffering events and introducing latency.

### Bifrost AI Gateway

**Repository:** maximhq/bifrost — 3,293 stars

High-performance open-source AI gateway built in Go by Maxim AI:
- **Native MCP gateway support** for agentic workflows
- **Semantic caching** as a first-class feature (see Section 8)
- 11 microsecond overhead at 5,000 req/s
- Automatic failbacks across 20+ LLM providers
- Virtual key budget management with hierarchical controls

### LiteLLM

**Repository:** BerriAI/litellm — 41,296 stars

Open-source proxy for 100+ LLM providers behind OpenAI-compatible API:
- Caching system stores and reuses LLM responses
- Supports `redis-semantic` and `qdrant-semantic` cache modes
- Compare prompt embeddings for semantically similar queries

**Sources:**
- Gravitee: https://www.gravitee.io/blog/mcp-api-gateway-explained-protocols-caching-and-remote-server-integration
- ContextForge: https://github.com/IBM/mcp-context-forge
- Envoy AI Gateway: https://aigateway.envoyproxy.io/blog/mcp-implementation/
- Kong MCP Proxy: https://developer.konghq.com/plugins/ai-mcp-proxy/
- Bifrost: https://github.com/maximhq/bifrost
- LiteLLM: https://docs.litellm.ai/docs/proxy/caching

---

## 6. Cache Invalidation Patterns

### Pattern 1: Time-Based (TTL)

The most common pattern. Different data types warrant different TTLs:

| Data Type | Recommended TTL | Rationale |
|-----------|----------------|-----------|
| Tool/resource lists | 5 minutes | Rarely change during session |
| Tool call results (weather) | 1-30 minutes | Data freshness varies |
| Database query results | 5 minutes | May change frequently |
| Static resources (schemas) | 7 days | Essentially immutable |
| User profiles | 24 hours | Infrequent changes |
| Real-time data | 1 minute or no cache | Must be current |

### Pattern 2: Event-Driven Invalidation (MCP Notifications)

Uses MCP's built-in notification system:

```
Server detects change → sends notification/resources/updated
→ Client receives notification → invalidates specific cache entry
→ Client sends resources/read → gets fresh data
```

**Subscription flow:**
1. Client sends `resources/subscribe` with resource URI
2. Server tracks subscription
3. On resource change, server sends `notifications/resources/updated`
4. Client invalidates cache and re-fetches

### Pattern 3: Versioning / ETags (Future)

Planned for June 2026 spec release. Will allow:
- Server includes version/ETag with responses
- Client stores version alongside cached data
- On subsequent request, client sends version for comparison
- Server returns 304-like "not modified" or fresh data

### Pattern 4: LRU (Least Recently Used) Eviction

FastMCP's `LimitSizeWrapper` implements size-based eviction. Recommended: retain 1,000 most-recent entries per tool, evict when memory exceeds configured limit (default 100 MB for ib-mcp-cache-server).

### Pattern 5: Stale-While-Revalidate

Serve stale cached content immediately, then revalidate in background:

```
Request → Cache hit (stale but within grace period)?
  → Return stale data immediately
  → Background: fetch fresh data, update cache
```

**Refresh-ahead variant:** Proactively load data before it expires. When a cached item is accessed and nearing expiration, the cache refreshes it in the background while returning the current value.

### Pattern 6: Manual/Admin Invalidation

Expose admin endpoints for cache purging:
- Purge by specific cache key
- Purge by tool name pattern
- Purge all caches
- CDN purge APIs (Cloudflare, Fastly)

### Pattern 7: Event-Driven Invalidation (Application Events)

Beyond MCP notifications, application-level events trigger invalidation:
- User profile update → invalidate `get_user_profile` cache
- Database write → invalidate related query caches
- Deployment → invalidate all caches

### Best Practice: Combine Multiple Strategies

Production systems should layer strategies:
1. **TTL** as safety net (nothing cached forever)
2. **Notifications** for known change events
3. **LRU** for memory management
4. **Manual purge** for emergency/admin use

**Sources:**
- MCP Resources Spec: https://modelcontextprotocol.io/specification/2025-06-18/server/resources
- Gravitee Guide: https://www.gravitee.io/blog/mcp-api-gateway-explained-protocols-caching-and-remote-server-integration
- GitHub Best Practices Gist: https://gist.github.com/eonist/16f74dea1e0110cee3ef6caff2a5856c

---

## 7. Real-World Caching Implementations

### mcp-cache (Response Management Proxy)

**Repository:** swapnilsurdi/mcp-cache — 5 stars, 4 forks
**npm:** `mcp-cache`
**License:** MIT

A transparent proxy wrapper that intercepts oversized MCP server responses (>900KB) and manages them via caching.

**Problem solved:** MCP servers frequently return massive responses (1MB+ HTML, large file listings) that exceed LLM context windows, causing "Error: Response exceeds maximum length of 1048576 bytes."

**Features:**
- Transparent proxy — works with ANY MCP server, zero modifications
- Smart caching with 1-hour TTL and automatic 5-minute cleanup
- Automatic chunking of large responses
- Client-aware token limits (Claude Desktop: 25K, Cursor: 30K, Cline: 25K)
- <10ms latency overhead

**Injected tools (6):**
1. `query_response()` — search cached data (text, JSONPath, regex)
2. `get_chunk()` — retrieve specific chunks
3. `list_responses()` — view all cached responses
4. `get_response_info()` — metadata about cached response
5. `refresh_response()` — extend TTL
6. `delete_response()` — manual removal

**Usage:**
```bash
npx mcp-cache <your-mcp-server-command>
```

**Environment variables:**
- `MCP_CACHE_MAX_TOKENS=25000`
- `MCP_CACHE_CHUNK_SIZE=10000`
- `MCP_CACHE_TTL=3600`
- `MCP_CACHE_ENABLE_INDEXING=true`

### mcp-refcache (Reference-Based Caching for FastMCP)

**Repository:** l4b4r4b4b4/mcp-refcache — 1 star, 61 commits
**PyPI:** `mcp-refcache`
**License:** MIT

Solves context explosion by storing large API responses by reference, returning only previews to agents.

**Core concept:** Instead of returning 500KB JSON to an agent's context, return a compact reference:
```json
{
  "ref_id": "a1b2c3",
  "preview": "[User(id=1), User(id=2), ... and 9998 more]",
  "total_items": 10000,
  "namespace": "session:abc123"
}
```

**Three cache backends:**
1. **Memory** (default) — in-process, no dependencies, lost on restart
2. **SQLite** — persistent, cross-process sharing, WAL mode, zero external deps
3. **Redis/Valkey** — distributed, native TTL, connection pooling, horizontal scaling

**Namespace system:**

| Type | Scope | TTL | Use Case |
|------|-------|-----|----------|
| `public` | Global | Hours/days | API responses, static data |
| `session:<id>` | Single conversation | Minutes | Conversation context |
| `user:<id>` | User across sessions | Hours | Preferences, history |
| `org:<id>` | Organization | Long | Shared org resources |

**Permission model (5 flags):**
- READ, WRITE, UPDATE, DELETE, EXECUTE
- EXECUTE allows agents to use values in computation WITHOUT seeing them (private computation)

**FastMCP integration:**
```python
from mcp_refcache import RefCache, Namespace

cache = RefCache(namespaces=[Namespace.PUBLIC, Namespace.session("conv-123")])

@mcp.tool()
@cache.cached(namespace="session:conv-123")
async def get_large_dataset(query: str) -> dict:
    return await fetch_huge_data(query)  # 500KB → compact reference
```

### ib-mcp-cache-server (Memory Cache Server)

**Repository:** ibproduct/ib-mcp-cache-server — 24 stars, 8 forks
**Language:** JavaScript/TypeScript

Reduces token consumption by automatically caching data between LLM interactions.

**Configuration:**

| Setting | Default | Purpose |
|---------|---------|---------|
| maxEntries | 1000 | Items before oldest removal |
| maxMemory | 100 MB | Bytes before LRU eviction |
| defaultTTL | 3600s | Cache item lifespan |
| checkInterval | 60s | Expiration check frequency |

**Auto-caches:** File contents, computation results, frequently accessed data. Operates transparently without user intervention.

### prompt-caching-mcp (npm package)

**npm:** `prompt-caching-mcp`

An MCP plugin that helps developers understand, optimize, and debug Anthropic's prompt caching:
- Inject `cache_control` breakpoints
- Analyze cacheability of prompts
- Track real-time cache savings

### FastMCP TypeScript (Tool List Caching)

**Repository:** punkpeye/fastmcp
**Supports:** MCP Specification 2025-03-26 and 2025-06-18

TypeScript MCP framework with built-in tool list caching support.

**Sources:**
- mcp-cache: https://github.com/swapnilsurdi/mcp-cache
- mcp-refcache: https://github.com/l4b4r4b4b4/mcp-refcache
- ib-mcp-cache-server: https://github.com/ibproduct/ib-mcp-cache-server
- prompt-caching-mcp: https://www.npmjs.com/package/prompt-caching-mcp

---

## 8. Semantic Caching

### What Is Semantic Caching?

Traditional caching requires exact key matches. Semantic caching uses **vector embeddings** to match queries by meaning, so "What is the refund policy?" and "How do I get a refund?" resolve to the same cached answer.

**How it works:**
1. Convert query to vector embedding
2. Search vector store for similar embeddings
3. If cosine similarity exceeds threshold (typically 0.92), return cached response
4. Otherwise, execute query and cache result with embedding

**Performance:** Cache hits return in <5ms vs. 2-5 seconds for full model calls.

### GPTCache (by Zilliz)

**Repository:** zilliztech/GPTCache — 7,971 stars
**PyPI:** `gptcache`
**Paper:** ACL 2023 NLP-OSS Workshop

Purpose-built semantic cache for LLM responses with modular architecture.

**Components:**
- **Embedding adapters:** OpenAI, Hugging Face, Cohere, ONNX models
- **Vector stores:** Milvus, FAISS, Hnswlib, PGVector, Chroma, Zilliz Cloud
- **Cache storage:** SQLite, DuckDB, PostgreSQL, MySQL
- **Eviction managers:** LRU and TTL-based

**Integration:** Fully integrated with LangChain and llama_index. No direct MCP integration documented, but can be wrapped around MCP tool calls at the application layer.

### Upstash Semantic Cache

**Repository:** upstash/semantic-cache — 294 stars
**npm:** `@upstash/semantic-cache`
**Also:** `upstash/semantic-cache-py` (Python)

Managed semantic caching layer built on Upstash Vector, designed for **serverless and edge** deployments.

**Configuration:**
- `minProximity` parameter: 0.95 = very high similarity required, 0.75 = low similarity
- Hosted vector database with lightweight SDK (JS/TS and Python)

**MCP integration:** Upstash Context7 MCP Server exposes semantic caching and context management tools to MCP clients.

### Bifrost Semantic Caching

**Repository:** maximhq/bifrost — 3,293 stars

Open-source AI gateway with semantic caching as a first-class feature:
- Understands when different queries carry similar meaning
- Teams report **30-50% cost reductions** (vs. 15-20% with exact-match caching)
- 11 microsecond overhead at 5,000 req/s
- Native MCP gateway support for agentic workflows

### LiteLLM Semantic Caching

**Repository:** BerriAI/litellm — 41,296 stars

Supports `redis-semantic` and `qdrant-semantic` cache modes:
- Compare prompt embeddings to identify semantically similar queries
- Configurable similarity thresholds
- Works with all 100+ supported LLM providers

### Applying Semantic Caching to MCP Tool Calls

Semantic caching is especially powerful for MCP tool calls where users ask the same question differently:

**Pattern:**
```python
# Semantic cache wrapper for MCP tools
class SemanticMCPCache:
    def __init__(self, embedding_model, vector_store, threshold=0.92):
        self.embedding_model = embedding_model
        self.vector_store = vector_store
        self.threshold = threshold

    async def cached_tool_call(self, tool_name, arguments):
        # Generate cache key from tool name + arguments
        query = f"{tool_name}:{json.dumps(arguments, sort_keys=True)}"
        embedding = self.embedding_model.embed(query)

        # Search for similar cached calls
        results = self.vector_store.search(embedding, threshold=self.threshold)
        if results:
            return results[0].cached_response  # Cache hit

        # Cache miss — execute tool and store
        response = await execute_tool(tool_name, arguments)
        self.vector_store.store(embedding, response, ttl=3600)
        return response
```

**Best use cases for semantic caching with MCP:**
- Database query tools (natural language → SQL)
- Search tools (similar search intents)
- Documentation/FAQ tools (paraphrased questions)
- Financial reporting tools ("show revenue" ≈ "display sales data")

**Less suitable:**
- Tools with side effects (create, update, delete)
- Tools where exact parameters matter (specific IDs, dates)
- Real-time data tools (stock prices, weather)

### Research Paper: Hierarchical Semantic Caching for MCP Servers

**Publication:** ResearchGate, 2026
**Title:** "Hierarchical Semantic Caching for MCP Servers: A Multi-Tier Context-Aware Approach to Optimize AI Model Data Access"

Proposes a multi-tier semantic caching approach specifically designed for MCP servers. (Full text behind paywall, but the existence of this paper confirms academic interest in MCP-specific caching.)

**Sources:**
- GPTCache: https://github.com/zilliztech/GPTCache
- Upstash: https://github.com/upstash/semantic-cache
- Bifrost: https://www.getmaxim.ai/articles/top-5-ai-gateways-with-semantic-caching-to-cut-llm-api-calls/
- LiteLLM Caching: https://docs.litellm.ai/docs/proxy/caching
- Hierarchical Paper: https://www.researchgate.net/publication/397793353
- MakeAIHQ Semantic Guide: https://makeaihq.com/guides/cluster/mcp-server-caching-strategies

---

## 9. MCP Resources as Cache Optimization

### Tim Kellogg's Thesis: "MCP Resources Are For Caching"

**Source:** https://timkellogg.me/blog/2025/06/05/mcp-resources

**Core argument:** MCP resources exist fundamentally to improve token utilization through caching. Without resource deduplication, RAG implementations duplicate large documents across multiple tool calls, wasting context tokens.

**Proposed implementation:**
- Track resource URIs as cache keys to identify previously-seen documents
- Separate results from full content: return resource references initially, include full text only once
- Use URI references like `<result uri="rag://polar-bears/74.md" />` with full text included separately

**Critical gap noted:** Neither Anthropic nor OpenAI's official MCP implementations currently support resources fully, limiting production-grade RAG caching.

---

## 10. Ecosystem Summary Table

| Project | Type | Stars | Language | Cache Backend | Key Feature |
|---------|------|-------|----------|---------------|-------------|
| **FastMCP** | Server framework | 24,088 | Python | Memory, Redis, SQLite, ES | Built-in ResponseCachingMiddleware |
| **LiteLLM** | LLM proxy | 41,296 | Python | Redis, Qdrant (semantic) | Semantic + exact caching for 100+ providers |
| **GPTCache** | Semantic cache | 7,971 | Python | SQLite, PG, MySQL + FAISS, Milvus | Purpose-built LLM semantic cache |
| **ContextForge** | MCP gateway | 3,489 | Python | Redis, SQLite, PostgreSQL | IBM gateway with federation + caching |
| **Bifrost** | AI gateway | 3,293 | Go | Redis (semantic) | 11μs overhead, native MCP gateway |
| **Redis MCP** | Data server | 465 | TypeScript | Redis | Official Redis MCP interface |
| **Upstash Semantic** | Semantic cache | 294 | TS/Python | Upstash Vector | Edge/serverless semantic cache |
| **ib-mcp-cache-server** | Cache server | 24 | JS/TS | Memory (LRU) | Auto token reduction between LLM calls |
| **mcp-cache** | Response proxy | 5 | Node.js | File system | Transparent proxy for oversized responses |
| **mcp-refcache** | Reference cache | 1 | Python | Memory, SQLite, Redis | Context explosion prevention + permissions |
| **prompt-caching-mcp** | Debug tool | — | Node.js | — | Analyze/debug Anthropic prompt caching |

---

## 11. Architecture Recommendations

### Layer 1: Protocol Level (Built-in)
- Use MCP notifications (`list_changed`, `resources/updated`) for real-time invalidation
- Declare `subscribe` and `listChanged` capabilities
- Use `lastModified` annotations on resources
- Watch for ETags/TTL in June 2026 spec

### Layer 2: Anthropic Prompt Caching
- Cache tool definitions by placing `cache_control` on last tool
- Use progressive disclosure / deferred tool loading for large tool sets
- Structure prompts: tools → system → messages for optimal cache prefix
- Use multiple breakpoints for different change frequencies

### Layer 3: Server-Side Caching
- Use FastMCP ResponseCachingMiddleware for Python servers
- Configure per-method TTLs (5 min for lists, 1 hour for reads/calls)
- Exclude tools with side effects from caching
- Use Redis for distributed/production deployments

### Layer 4: Gateway/Proxy Caching
- Deploy ContextForge or Envoy AI Gateway for multi-server setups
- Cache `resources/list`, `prompts/list`, `tools/list` at gateway
- Never cache `tools/call` at gateway level (side effects)
- Use CDN for static MCP schemas/documentation

### Layer 5: Semantic Caching
- Apply to natural language tool inputs (search, queries, Q&A)
- Use GPTCache, Upstash, or Bifrost depending on deployment model
- Set similarity threshold ≥ 0.92 to avoid false matches
- Exclude tools with side effects or exact-parameter requirements

### Layer 6: Context Window Optimization
- Use mcp-refcache for reference-based responses (prevent context explosion)
- Use mcp-cache proxy for oversized response management
- Implement the SQLite-as-cache pattern for database MCP servers
- Track and monitor token usage via prompt-caching-mcp

---

## 12. Key Insights for Guide Writing

1. **MCP has no built-in cache headers** — but has notification-based invalidation that serves a similar purpose. ETags/TTLs are coming in June 2026.

2. **The biggest caching win is Anthropic prompt caching** — 90% cost reduction on cached tool definitions. This is the #1 optimization for any MCP deployment.

3. **Progressive disclosure is transformative** — 85-98% token reduction by loading tools on-demand rather than all upfront. Directly enables better prompt cache hit rates.

4. **FastMCP is the de facto standard** for server-side caching in Python — built-in middleware with sensible defaults.

5. **Gateway caching is critical for production** — ContextForge (IBM, 3.5K stars) and Bifrost (3.3K stars) are the leading options with Redis-backed caching.

6. **Semantic caching is the frontier** — 30-50% cost reduction for natural language tool inputs. GPTCache (8K stars) is mature; Bifrost and LiteLLM offer integrated solutions.

7. **Cache what's safe, skip what has side effects** — Golden rule: cache `list` and `read` operations, never cache `call` operations at the gateway level (though individual tool results can be cached at the server level for idempotent tools).

8. **Client caching support is uneven** — Claude Code handles `list_changed` well, but many clients cache tool lists aggressively and don't support resource subscriptions.

9. **SQLite-as-cache is an underappreciated pattern** — Particularly powerful for MCP servers that expose file-based or document data.

10. **Context explosion prevention is a caching problem** — mcp-refcache's reference-based approach and mcp-cache's chunking proxy are novel MCP-specific solutions.
