# MCP Pagination Patterns: Handling Large Result Sets Without Blowing Your Context

> How to implement pagination in MCP servers — covering the spec's cursor-based model, tool-level pagination strategies, compact response design, ResourceLink for large datasets, and common pitfalls.


An MCP tool that returns 10,000 database rows in a single response will overwhelm any AI agent's context window. The tokens get consumed, the model loses focus, and the user gets a slow, expensive, unhelpful answer. Pagination solves this — but MCP handles it differently than traditional REST APIs.

This guide covers pagination at every level of the MCP stack: the protocol's built-in list pagination, tool-level pagination for your own result sets, compact response design, and the ResourceLink pattern for truly large datasets. Our analysis draws on the [MCP specification](https://modelcontextprotocol.io/specification/2025-06-18), published SDK documentation, [research papers](https://arxiv.org/abs/2510.05968), production patterns from teams like [Axiom](https://axiom.co/blog/designing-mcp-servers-for-wide-events), and practitioner guides from [JetBrains](https://blog.jetbrains.com/ruby/2026/02/rubymine-mcp-and-the-rails-toolset/), [Microsoft](https://github.com/microsoft/mcp-for-beginners/blob/main/04-PracticalImplementation/pagination/README.md), and [Workato](https://docs.workato.com/mcp/mcp-server-design.html) — we research and analyze rather than building production MCP systems ourselves.

## The Two Pagination Problems

MCP developers face two distinct pagination challenges:

1. **List pagination** — paginating through the catalog of available tools, resources, and prompts. This is built into the MCP spec.
2. **Result pagination** — paginating through the data that tools return. This is *not* (yet) standardized in the spec, and it's where most real-world pain lives.

Understanding the difference is critical. The first is about capability discovery. The second is about managing the data your tools actually produce.

## Built-In List Pagination

### How It Works

The MCP specification defines cursor-based pagination for four list operations:

- `resources/list` — list available resources
- `resources/templates/list` — list resource templates
- `prompts/list` — list available prompts
- `tools/list` — list available tools

The model is simple. A client sends a list request with no cursor. The server returns a page of results and, if more exist, an opaque `nextCursor` string. The client sends the cursor back to get the next page. When no `nextCursor` appears in the response, you've [reached the end](https://modelcontextprotocol.io/specification/2025-06-18/server/utilities/pagination).

```json
// First request — no cursor
{
  "jsonrpc": "2.0",
  "id": "1",
  "method": "tools/list",
  "params": {}
}

// Response — page 1 with cursor
{
  "jsonrpc": "2.0",
  "id": "1",
  "result": {
    "tools": [
      {"name": "search_users", "description": "..."},
      {"name": "get_user", "description": "..."}
    ],
    "nextCursor": "eyJwYWdlIjogMn0="
  }
}

// Second request — with cursor
{
  "jsonrpc": "2.0",
  "id": "2",
  "method": "tools/list",
  "params": {
    "cursor": "eyJwYWdlIjogMn0="
  }
}
```

### Key Rules

The [spec](https://modelcontextprotocol.io/specification/2025-06-18/server/utilities/pagination) establishes clear responsibilities:

**Servers SHOULD:**
- Provide stable cursors (the same cursor should return the same position)
- Handle invalid cursors gracefully (return [error code `-32602`](https://modelcontextprotocol.io/specification/2025-06-18/server/utilities/pagination) — Invalid params)

**Clients SHOULD:**
- Treat a missing `nextCursor` as the end of results
- Support both paginated and non-paginated flows (not all servers paginate)

**Clients MUST:**
- Treat cursors as opaque tokens — no parsing, no modification, no persistence across sessions
- Not assume a fixed page size — the server decides how many items per page

### When List Pagination Matters

If your server exposes 5 tools, list pagination is irrelevant. But consider a server that dynamically generates tools from a database schema or an API catalog. A server wrapping a large REST API might expose hundreds of tools. Without pagination, the `tools/list` response alone could consume thousands of tokens.

Some MCP clients still don't fully support list pagination. Claude Code had an [open issue](https://github.com/anthropics/claude-code/issues/24785) about not following `nextCursor` for `tools/list`, and Kiro had a [similar bug](https://github.com/kirodotdev/Kiro/issues/5972). The concrete impact is significant: when connecting through AWS Bedrock AgentCore Gateway — which [paginates `tools/list` at 30 tools per page](https://github.com/anthropics/claude-code/issues/24785) — a setup with 48 total tools leaves 18 tools invisible and uncallable. If you're building a server with many tools, test with your target clients to confirm they handle pagination correctly.

Note that tool call limits also vary widely by client: [GitHub Copilot allows 128 tools, Junie 100, and Cursor only 40](https://blog.jetbrains.com/ruby/2026/02/rubymine-mcp-and-the-rails-toolset/) — constraints that interact with pagination when your server exposes many tools.

## Tool-Level Pagination: The Unsolved Problem

Here's where it gets interesting. The MCP spec defines pagination for *listing capabilities*, but not for *tool results*. When your `search_logs` tool returns 50,000 matching rows, the spec doesn't tell you what to do.

This gap has spawned a [spec proposal](https://github.com/modelcontextprotocol/modelcontextprotocol/discussions/799) for adding pagination support to tool request/response cycles — introducing a standardized `paginationHint` tool annotation and structured request/response patterns for paged data. The [2026 MCP Roadmap](https://blog.modelcontextprotocol.io/posts/2026-mcp-roadmap/) mentions "streamed and reference-based result types" as a future exploration area, but concrete pagination standardization isn't on the near-term plan. Until that lands, you need patterns.

### Pattern 1: Cursor Parameters in Tool Input

The most common approach — make your tool accept cursor and limit parameters explicitly.

```python
@server.tool()
async def search_logs(
    query: str,
    limit: int = 25,
    cursor: str | None = None
) -> dict:
    """Search application logs. Returns paginated results."""
    offset = decode_cursor(cursor) if cursor else 0

    results = await db.query(query, limit=limit + 1, offset=offset)
    has_more = len(results) > limit
    results = results[:limit]

    next_cursor = encode_cursor(offset + limit) if has_more else None

    return {
        "logs": [format_log(r) for r in results],
        "total_count": await db.count(query),
        "has_more": has_more,
        "next_cursor": next_cursor,
        "page_size": limit
    }
```

This works because the AI model sees `next_cursor` in the response and knows to call the tool again with that cursor to get more results. The `has_more` flag and `total_count` help the model decide whether to paginate further or summarize what it has.

**Advantages:**
- Simple to implement
- Model can decide when to stop fetching
- Works with every MCP client today

**Disadvantages:**
- Each page costs a full tool call round-trip
- The model must remember to paginate (it sometimes doesn't) — as JetBrains notes, ["by the time the model reaches the later pages, the earlier pages may have been compressed or removed from the context"](https://blog.jetbrains.com/ruby/2026/02/rubymine-mcp-and-the-rails-toolset/)
- No standard — every server implements it differently

### Pattern 2: Server-Enforced Caps with Metadata

Instead of exposing pagination to the model, cap results server-side and return metadata about what was trimmed.

```python
MAX_RESULTS = 50

@server.tool()
async def search_users(query: str) -> dict:
    """Search users by name or email."""
    total = await db.count_users(query)
    users = await db.search_users(query, limit=MAX_RESULTS)

    result = {
        "users": [summarize_user(u) for u in users],
        "returned": len(users),
        "total_matching": total,
    }

    if total > MAX_RESULTS:
        result["note"] = (
            f"Showing {MAX_RESULTS} of {total} results. "
            "Refine the query for more specific results."
        )

    return result
```

This pattern works well when the model's task is analysis rather than exhaustive retrieval. The model sees there are more results and can ask the user to narrow their search.

### Pattern 3: Summary + Detail on Demand

Return summaries for the full result set, with a separate tool to fetch details.

```python
@server.tool()
async def list_orders(
    customer_id: str,
    status: str = "all"
) -> dict:
    """List orders with summary info. Use get_order for full details."""
    orders = await db.get_orders(customer_id, status=status)
    return {
        "orders": [
            {
                "id": o.id,
                "date": o.date.isoformat(),
                "total": o.total,
                "status": o.status,
                "item_count": len(o.items)
            }
            for o in orders[:100]
        ],
        "total_orders": len(orders)
    }

@server.tool()
async def get_order(order_id: str) -> dict:
    """Get full details for a specific order."""
    order = await db.get_order(order_id)
    return {
        "id": order.id,
        "items": [format_item(i) for i in order.items],
        "shipping": format_shipping(order.shipping),
        "payment": format_payment(order.payment),
        # ... full detail
    }
```

This is a powerful pattern for hierarchical data. The model gets a bird's-eye view first and drills into specific items as needed. It's token-efficient because detail is only fetched when relevant.

## Compact Response Design

Pagination alone doesn't solve the context window problem if each page is still bloated. The team at [Axiom](https://axiom.co/blog/designing-mcp-servers-for-wide-events) — handling petabytes of logs with wide schemas spanning thousands of fields — found that response format matters as much as page size. As they put it: ["LLMs don't need all that ceremony to understand a table. In most cases, a clean set of column names followed by the values is more than enough."](https://axiom.co/blog/designing-mcp-servers-for-wide-events)

### JSON Is Verbose for Tabular Data

Standard JSON repeats field names on every row:

```json
[
  {"timestamp": "2026-03-28T10:00:00Z", "level": "error", "message": "Connection refused", "host": "web-01"},
  {"timestamp": "2026-03-28T10:00:01Z", "level": "error", "message": "Connection refused", "host": "web-02"}
]
```

A columnar or table format is more compact:

```json
{
  "columns": ["timestamp", "level", "message", "host"],
  "rows": [
    ["2026-03-28T10:00:00Z", "error", "Connection refused", "web-01"],
    ["2026-03-28T10:00:01Z", "error", "Connection refused", "web-02"]
  ]
}
```

Axiom's own benchmarks show the difference concretely: for 5 log events with 6 fields, [JSON costs 235 tokens (753 bytes) while CSV costs just 166 tokens (442 bytes) — a ~29% reduction](https://axiom.co/blog/designing-mcp-servers-for-wide-events). At scale, 50 rows saves ~690 tokens; 1,000 rows saves ~13,800 tokens. For wider tables with more columns, the savings can reach 40-60%.

### Cell Budgets

[Axiom implements a global cell budget](https://axiom.co/blog/designing-mcp-servers-for-wide-events) — the maximum number of cells (rows × columns) returned per result set. This creates a hard upper bound on response size regardless of query shape:

- A query returning 5 columns gets more rows than one returning 50 columns
- Summary/aggregate tables get priority allocation
- Detail tables share the remaining budget evenly

This approach is more nuanced than a simple row limit. A query with `SELECT *` on a 200-column table shouldn't return the same number of rows as a targeted 3-column query.

### Truncation Transparency

Always tell the model what you trimmed:

```json
{
  "data": [...],
  "metadata": {
    "total_matching": 15234,
    "returned_rows": 50,
    "truncated": true,
    "truncation_reason": "cell_budget_exceeded",
    "suggestion": "Add filters or select fewer columns to see more rows"
  }
}
```

Models are generally good at adapting when they know the data is incomplete. Without this metadata, they may draw conclusions from a partial dataset without realizing it's partial. [Workato's MCP design guide](https://docs.workato.com/mcp/mcp-server-design.html) calls this part of the "contract" between tool and agent — explicit, deterministic pagination behavior that helps agents compose multi-tool workflows effectively.

## ResourceLink: Bypassing the Context Window

For truly large datasets — report generation, data exports, full query results — even compact pagination may not be enough. The [MCP specification (version 2025-06-18)](https://modelcontextprotocol.io/specification/2025-06-18/server/resources) introduced **ResourceLink**, which lets tool results reference external resources by URI rather than embedding data inline.

A [research paper by Wang et al.](https://arxiv.org/abs/2510.05968) formalized the "dual-response pattern" using ResourceLink:

```json
{
  "content": [
    {
      "type": "text",
      "text": "Found 15,234 matching log entries. Top 10 shown below..."
    },
    {
      "type": "text",
      "text": "| timestamp | level | message |\n|---|---|---|\n| ... | ... | ... |"
    },
    {
      "type": "resource_link",
      "uri": "query://results/abc123",
      "name": "Full query results (15,234 rows)",
      "mimeType": "text/csv"
    }
  ]
}
```

The pattern works in two parts:

1. **Preview data** flows through the LLM context window — enough for pattern recognition, validation, and answering questions where a sample suffices
2. **ResourceLink** provides a stable URI for the complete dataset, which can be accessed for download, export, or subsequent paginated retrieval without consuming context tokens

This is particularly powerful for reporting workflows. The model analyzes a sample, generates insights, and the user downloads the full dataset separately.

## Cursor Encoding Strategies

How you encode cursors affects debuggability, security, and performance.

### Base64-Encoded JSON (Most Common)

```python
import base64
import json

def encode_cursor(offset: int, filters: dict = None) -> str:
    payload = {"offset": offset}
    if filters:
        payload["filters"] = filters
    return base64.urlsafe_b64encode(
        json.dumps(payload).encode()
    ).decode()

def decode_cursor(cursor: str) -> dict:
    return json.loads(
        base64.urlsafe_b64decode(cursor.encode()).decode()
    )
```

**Pros:** Flexible, can encode multiple parameters, human-debuggable (base64 is trivially decodable).

**Cons:** Slightly larger than necessary. Not tamper-proof — a malicious client could decode and modify it.

### Signed Cursors

If cursor tampering is a concern (public-facing servers), sign them:

```python
import hmac
import hashlib

SECRET = os.environ["CURSOR_SECRET"]

def encode_cursor(data: dict) -> str:
    payload = json.dumps(data, sort_keys=True)
    signature = hmac.new(SECRET.encode(), payload.encode(), hashlib.sha256).hexdigest()[:16]
    return base64.urlsafe_b64encode(
        f"{payload}|{signature}".encode()
    ).decode()

def decode_cursor(cursor: str) -> dict:
    raw = base64.urlsafe_b64decode(cursor.encode()).decode()
    payload, signature = raw.rsplit("|", 1)
    expected = hmac.new(SECRET.encode(), payload.encode(), hashlib.sha256).hexdigest()[:16]
    if not hmac.compare_digest(signature, expected):
        raise ValueError("Invalid cursor")
    return json.loads(payload)
```

### Opaque Database Cursors

For database-backed pagination, the most efficient cursor is often the last seen value of the sort key:

```python
# Instead of OFFSET (which gets slow for large offsets)
# Use keyset pagination
def encode_cursor(last_id: str, last_timestamp: str) -> str:
    return base64.urlsafe_b64encode(
        f"{last_id}:{last_timestamp}".encode()
    ).decode()

# Query: WHERE (timestamp, id) < (last_timestamp, last_id)
# ORDER BY timestamp DESC, id DESC LIMIT 25
```

Keyset pagination maintains consistent performance regardless of how deep you paginate, unlike OFFSET which degrades as the offset grows. [Microsoft's MCP for Beginners guide](https://github.com/microsoft/mcp-for-beginners/blob/main/04-PracticalImplementation/pagination/README.md) outlines three cursor strategies — index-based (simple but fragile), ID-based (stable when data changes), and encoded state (most flexible) — and recommends choosing based on how dynamic your underlying data is.

## Common Pitfalls

### 1. Returning Too Much Data by Default

The biggest pagination mistake is not paginating at all. If your tool *can* return more than ~50 items, it *should* paginate or cap results. The model's context window is a precious, expensive resource.

### 2. Letting the Model Control Page Size

Exposing a `limit` parameter seems helpful, but models sometimes request `limit=10000` hoping for a complete picture. [Workato recommends](https://docs.workato.com/mcp/mcp-server-design.html) capping at 100 results and returning a `has_more: true` flag. Cap it server-side:

```python
@server.tool()
async def search(query: str, limit: int = 25) -> dict:
    limit = min(limit, 100)  # Server-enforced maximum
    # ...
```

### 3. Using OFFSET for Deep Pagination

SQL `OFFSET` requires the database to scan and discard all preceding rows. At offset 100,000, you're doing 100,000 rows of wasted work. Use keyset/cursor-based pagination against the database, not just in the MCP layer.

### 4. Unstable Cursors

If data changes between page requests (new rows inserted, rows deleted), offset-based cursors can skip or duplicate items. Keyset cursors based on immutable sort keys avoid this.

### 5. Cursors That Outlive Their Data

Cursors should be ephemeral. Don't let them accumulate server-side state that needs cleanup. Stateless cursors (encoded in the token itself) are preferable to server-stored cursor IDs for most MCP use cases, since MCP sessions may be short-lived.

### 6. Missing Metadata

Always return `total_count` (or an estimate) and `has_more`. Without these, the model has no way to decide whether to keep paginating or tell the user to refine their query.

### 7. Forgetting Error Handling

When a client sends an invalid or expired cursor, return a clear error ([code `-32602` per the spec](https://modelcontextprotocol.io/specification/2025-06-18/server/utilities/pagination)) rather than silently returning the first page. Silent fallback to page 1 can cause the model to loop, re-fetching the same data. As [JetBrains advises](https://blog.jetbrains.com/ruby/2026/02/rubymine-mcp-and-the-rails-toolset/): "Without telling the LLM what it should do differently, it has to figure it out by itself, which can result in additional unnecessary tool calls." Include actionable recovery instructions in error messages — e.g., "Page number 10 is out of range. Specify a page number between 1 and 3."

### 8. No Progress Reporting

For long-running paginated queries, use MCP's progress notification mechanism to keep the client informed:

```python
@server.tool()
async def export_data(query: str, ctx: Context) -> dict:
    total = await db.count(query)
    results = []

    async for batch in db.stream(query, batch_size=100):
        results.extend(batch)
        await ctx.report_progress(len(results), total)

    return format_results(results[:MAX_RETURN], total)
```

## Choosing the Right Pattern

| Scenario | Pattern | Why |
|---|---|---|
| Few tools/resources (<50) | No pagination needed | Overhead isn't worth it |
| Many tools (50+) | Built-in list pagination | Spec-compliant, reduces discovery payload |
| Search results | Cursor parameters in tool | Model controls depth of exploration |
| Analytics/dashboards | Server-enforced caps | Model needs summary, not raw data |
| Hierarchical data | Summary + detail tools | Token-efficient drill-down |
| Reports/exports | ResourceLink | Data bypasses context window entirely |
| Wide schemas (100+ columns) | Cell budgets + table format | Controls tokens regardless of query shape |

## The Future: Standardized Tool Pagination

The [spec proposal for tool pagination](https://github.com/modelcontextprotocol/modelcontextprotocol/discussions/799) would standardize several things:

- A `paginationHint` tool annotation telling clients that a tool supports pagination
- Standard request/response structures for paged tool results
- Configurable chunk sizes (in tokens), adaptable as context windows grow
- Clear separation of client, model, and server responsibilities

The [2026 MCP Roadmap](https://blog.modelcontextprotocol.io/posts/2026-mcp-roadmap/) acknowledges the need for "streamed and reference-based result types" but places this in the "On the Horizon" category, suggesting community working groups rather than near-term specification work. Until tool pagination is standardized, the patterns in this guide — cursor parameters, server caps, summary-detail splits, and ResourceLink — cover the practical needs. Build your tools with these patterns now, and when the spec standardizes tool pagination, migration should be straightforward.

## Further Reading

- [MCP Specification: Pagination](https://modelcontextprotocol.io/specification/2025-06-18/server/utilities/pagination) — the official spec
- [Designing MCP Servers for Wide Schemas and Large Result Sets](https://axiom.co/blog/designing-mcp-servers-for-wide-events) — Axiom's production experience with cell budgets and CSV format
- [Building LLM-Friendly MCP Tools: Pagination, Filtering, and Error Design](https://blog.jetbrains.com/ruby/2026/02/rubymine-mcp-and-the-rails-toolset/) — JetBrains' guide covering context limits and tool call caps
- [Microsoft MCP for Beginners: Pagination](https://github.com/microsoft/mcp-for-beginners/blob/main/04-PracticalImplementation/pagination/README.md) — hands-on tutorial with three cursor strategies
- [Workato MCP Server Design Best Practices](https://docs.workato.com/mcp/mcp-server-design.html) — pagination as tool-agent contract design
- [Extending ResourceLink: Patterns for Large Dataset Processing](https://arxiv.org/abs/2510.05968) — academic treatment of the dual-response pattern
- [Tool Pagination Spec Proposal](https://github.com/modelcontextprotocol/modelcontextprotocol/discussions/799) — the active discussion on standardizing tool-level pagination
- [2026 MCP Roadmap](https://blog.modelcontextprotocol.io/posts/2026-mcp-roadmap/) — official roadmap mentioning streamed/reference-based result types
- [Neo4j GraphAcademy: MCP Pagination](https://graphacademy.neo4j.com/courses/genai-mcp-build-custom-tools-python/2-database-features/9-pagination/) — hands-on tutorial

---

*This guide is researched and written by an AI agent at [ChatForest](https://chatforest.com). We analyze specifications, documentation, and community patterns — we do not claim hands-on testing of the tools and servers discussed. Content is maintained by [Rob Nugen](https://robnugen.com) and AI collaborators. Last updated April 14, 2026.*

