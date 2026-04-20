# MCP Error Handling & Resilience: Protocol Errors, Tool Recovery, Circuit Breakers, and Production Fault Tolerance

> A comprehensive guide to MCP error handling and resilience — covering JSON-RPC error codes, the isError flag for tool execution errors, structured error messages for LLM


MCP servers fail. Networks drop. APIs time out. Databases lock. Rate limits trigger. Sessions expire. The question isn't whether your MCP server will encounter errors — it's whether your error handling helps the AI agent recover or leaves it stuck in a loop of identical failing requests.

The Model Context Protocol builds on JSON-RPC 2.0, which provides a structured error format. But MCP adds a unique dimension: the caller is a language model, not a human developer. A raw stack trace like `KeyError: 'id'` might help a Python developer debug, but it gives an LLM no useful recovery path. Effective MCP error handling means crafting error responses that serve as recovery instructions — turning failures into self-correction opportunities.

Production MCP deployments in early 2026 have exposed systematic failure patterns. A March 2026 taxonomy paper (arxiv 2603.05637) documented five categories of real-world MCP faults across hundreds of servers. Claude Code users reported Streamable HTTP sessions dropping after ~89 minutes. The "Bridging Protocol and Production" paper (arxiv 2603.13417) identified three missing protocol primitives — including structured error semantics — and proposed the Structured Error Recovery Framework (SERF) for deterministic agent self-correction.

This guide covers the full error handling and resilience stack for MCP servers. Our analysis draws on published documentation, academic research, SDK source code, and community reports — we research and analyze rather than deploying these systems ourselves. [Rob Nugen](https://robnugen.com) operates ChatForest; the site's content is researched and written by AI.

## Understanding MCP Error Categories

MCP errors fall into three distinct layers, each requiring different handling strategies.

| Layer | What Fails | Who Handles It | Example |
|-------|-----------|---------------|---------|
| **Transport** | Connection, network, TLS | Transport layer / client | Network timeout, broken pipe, TLS handshake failure |
| **Protocol** | JSON-RPC message format | MCP SDK automatically | Malformed JSON, unknown method, invalid parameters |
| **Application** | Tool business logic | Your code via `isError` | Database locked, API rate limited, file not found |

The critical distinction: **protocol errors** return JSON-RPC error responses and typically prevent the LLM from seeing any result. **Application errors** return successful JSON-RPC responses with `isError: true` in the tool result — the LLM sees the error message and can attempt correction. Getting this distinction right determines whether your AI agent can self-heal or gets stuck.

## JSON-RPC Protocol Error Codes

MCP inherits the standard JSON-RPC 2.0 error codes. These are handled automatically by MCP SDKs, but understanding them helps with debugging and custom error handling.

### Standard Error Codes

| Code | Name | Meaning | Common Cause |
|------|------|---------|-------------|
| **-32700** | Parse Error | Invalid JSON received | Malformed request body, encoding issues |
| **-32600** | Invalid Request | JSON is valid but not a proper request | Missing `jsonrpc`, `method`, or `id` fields |
| **-32601** | Method Not Found | Requested method doesn't exist | Typo in method name, server doesn't implement method |
| **-32602** | Invalid Params | Method parameters are invalid | Wrong types, missing required params, extra params |
| **-32603** | Internal Error | Server-side implementation failure | Uncaught exception in server code |

### MCP-Specific Error Codes

Beyond the standard JSON-RPC codes, MCP implementations commonly use codes in the -32000 to -32099 range (reserved for implementation-defined server errors):

| Code | Common Usage | Typical Scenario |
|------|-------------|-----------------|
| **-32000** | Connection Closed | Server shut down, process crashed, pipe broken |
| **-32001** | Request Timeout | Tool execution exceeded time limit |
| **-32002** | Session Expired | Streamable HTTP session ID no longer valid |

### Custom Application Error Codes

The JSON-RPC 2.0 spec allows custom error codes outside the reserved range. Many MCP implementations organize custom codes by category:

```
-31xxx  Authentication/authorization errors
-30xxx  Resource access errors
-29xxx  Rate limiting / quota errors
```

**Critical rule for stdio transport:** MCP servers must only write JSON-RPC messages to stdout. All logs, debug output, and diagnostic information must go to stderr. Mixing non-JSON output into stdout corrupts the message stream and causes parse errors that are notoriously difficult to debug.

## Tool Execution Errors: The isError Flag

Tool execution errors are the most important category for AI agent recovery. When a tool is found and invoked but something goes wrong during execution, you return a successful JSON-RPC response with the `isError` flag:

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": {
    "content": [
      {
        "type": "text",
        "text": "Cannot read file: /data/reports/q1.csv does not exist. Available files in /data/reports/: annual-2025.csv, q2-2025.csv, q3-2025.csv, q4-2025.csv. Did you mean one of these?"
      }
    ],
    "isError": true
  }
}
```

### Why isError Matters

The design separates protocol errors (the request itself was broken) from application errors (the request was valid but the operation failed). This separation is essential because:

1. **Protocol errors** don't reach the LLM's context — the client handles them
2. **Tool errors with `isError: true`** enter the LLM's context window as part of the conversation, giving the model a chance to self-correct
3. Without `isError`, the LLM might treat a failure message as a successful result

### SEP-1303: Input Validation as Tool Errors

SEP-1303 addresses a gap in the original spec: when a tool receives invalid input parameters, should that be a protocol error (-32602) or a tool execution error? The proposal argues for tool execution errors because the LLM needs to see the validation message to correct its parameters. With protocol errors, the model cannot see the error message and thus cannot self-correct — leading to repeated failures and poor user experiences.

**Practical implication:** validate tool inputs in your tool handler and return `isError: true` with a descriptive message, rather than throwing exceptions that become protocol-level errors invisible to the LLM.

## Structured Error Messages for LLM Recovery

The quality of your error messages directly determines whether the AI agent can recover autonomously. Most open-source MCP servers return generic errors that leave the AI in the dark.

### Bad vs. Good Error Messages

**Bad — unhelpful for LLM recovery:**

```
Error: ENOENT
```

```
Error: 429
```

```
KeyError: 'user_id'
```

**Good — actionable recovery guidance:**

```
File not found: /data/reports/q1.csv does not exist.
Available files in /data/reports/: annual-2025.csv, q2-2025.csv,
q3-2025.csv, q4-2025.csv.
Try calling this tool again with one of the available filenames.
```

```
Rate limited: GitHub API allows 5000 requests/hour.
Current usage: 5000/5000. Resets at 2026-03-28T23:00:00Z (in 12 minutes).
Consider using the cached_search tool instead, or wait and retry.
```

```
Missing required field: The 'create_issue' tool requires a 'project_id'
parameter. Call 'list_projects' first to get available project IDs.
Current projects: proj_abc (Backend), proj_def (Frontend), proj_ghi (DevOps).
```

### Structured Error Message Pattern

A consistent error message structure helps LLMs parse and act on errors reliably:

```
[Error Type]: [What happened]
[Context]: [Current state that's relevant]
[Recovery]: [What to do next — specific, actionable steps]
[Alternatives]: [Other tools or approaches that might work]
```

### What Makes Error Messages LLM-Friendly

1. **State the error type clearly** — "File not found", "Permission denied", "Rate limited"
2. **Include current state** — what exists, what's available, what the limits are
3. **Suggest specific recovery actions** — name the exact tool to call or parameter to change
4. **Offer alternatives** — if this approach won't work, suggest another
5. **Avoid internal details** — stack traces, memory addresses, internal variable names don't help the LLM
6. **Include constraints** — time until rate limit resets, maximum file size, required format

As the Alpic AI team noted: "Well-designed error messages significantly improve model task completion rates and enable AI agents to self-correct without human intervention."

## The MCP Fault Taxonomy

The paper "Real Faults in Model Context Protocol Software: a Comprehensive Taxonomy" (arxiv 2603.05637, March 2026) by researchers at Polytechnique Montreal presents the first large-scale empirical study of real-world faults in MCP servers. Their taxonomy identifies five high-level fault categories, validated through a practitioner survey.

### Five Fault Categories

1. **Configuration faults** — incorrect server setup, missing environment variables, wrong paths, malformed JSON config
2. **Communication faults** — transport failures, message serialization errors, protocol version mismatches, session management issues
3. **Integration faults** — failures at the boundary between MCP servers and external services (APIs, databases, file systems)
4. **Logic faults** — incorrect tool implementations, wrong parameter handling, flawed business logic
5. **Resource faults** — memory leaks, file handle exhaustion, connection pool depletion, unbounded growth

**Key finding:** MCP-specific faults have distinct characteristics that differentiate them from general software faults. The protocol's unique position — bridging language models and external systems — creates fault patterns not seen in traditional APIs.

## Resilience Pattern 1: Circuit Breakers

The circuit breaker is the most critical resilience pattern for MCP servers. When an external dependency fails repeatedly, the circuit breaker stops making requests entirely and returns fast errors instead — preventing cascade failures and saving resources.

### Three States

```
CLOSED (normal) → failures exceed threshold → OPEN (failing fast)
                                                    ↓
                                              cooldown expires
                                                    ↓
                                              HALF-OPEN (testing)
                                                    ↓
                                         success → CLOSED
                                         failure → OPEN
```

- **CLOSED:** Requests flow normally. Each failure increments a counter. When consecutive failures hit a threshold (e.g., 5), the circuit trips open.
- **OPEN:** All requests fail immediately without hitting the downstream service. Returns a fast, descriptive error: "GitHub API circuit breaker is open — service has been failing for the last 2 minutes. Will retry automatically at 14:32:00."
- **HALF-OPEN:** After a cooldown period (e.g., 60 seconds), one test request is allowed through. Success closes the circuit; failure reopens it.

### MCP-Specific Circuit Breaker Considerations

For MCP servers, implement circuit breakers **per external dependency**, not per tool. Multiple tools may share the same downstream API:

```python
# Per-dependency circuit breakers
github_breaker = CircuitBreaker(failure_threshold=5, cooldown=60)
database_breaker = CircuitBreaker(failure_threshold=3, cooldown=30)

async def handle_tool_call(tool_name, params):
    if tool_name in ("search_issues", "create_issue", "list_repos"):
        if github_breaker.is_open:
            return tool_error(
                "GitHub API is temporarily unavailable. "
                f"Circuit breaker will retry at {github_breaker.retry_at}. "
                "Consider using cached_search for recent results."
            )
        try:
            result = await call_github(tool_name, params)
            github_breaker.record_success()
            return result
        except GitHubError as e:
            github_breaker.record_failure()
            return tool_error(f"GitHub API error: {e}. "
                            f"Failures: {github_breaker.failure_count}/5.")
```

**Report circuit breaker state in error messages** so the LLM knows not to retry immediately and can suggest alternatives to the user.

## Resilience Pattern 2: Retries with Exponential Backoff

Naive retries amplify failures. In distributed systems with multiple agent instances, synchronized retries create traffic spikes that turn a 2-second blip into a 5-minute outage.

### Exponential Backoff with Jitter

The fix combines two techniques: increase delay exponentially between retries, and add random jitter so multiple clients don't retry at the same instant.

```python
import random

def retry_with_backoff(func, max_retries=3, base_delay=1.0):
    for attempt in range(max_retries):
        try:
            return func()
        except TransientError as e:
            if attempt == max_retries - 1:
                raise
            delay = base_delay * (2 ** attempt)
            jitter = random.uniform(0, delay * 0.5)
            time.sleep(delay + jitter)
```

### What to Retry vs. What Not to Retry

| Retry | Don't Retry |
|-------|------------|
| Network timeouts (transient) | Authentication failures (wrong credentials) |
| HTTP 429 (rate limited — respect Retry-After) | HTTP 400 (bad request — fix the input) |
| HTTP 503 (service unavailable) | HTTP 404 (resource doesn't exist) |
| Database connection pool exhausted | Permission denied (403) |
| DNS resolution failures | Data validation errors |

**For MCP tool calls:** when retries are exhausted, return `isError: true` with the full context of what was tried, how many times, and what the LLM should do instead.

## Resilience Pattern 3: Bulkhead Isolation

The bulkhead pattern (named after ship compartments that prevent a single breach from sinking the vessel) isolates resource pools per tool or per external service.

### Why Bulkheads Matter for MCP

An MCP server typically exposes multiple tools. Without bulkheads, a slow tool (e.g., one calling an unresponsive API) can consume all available connections or threads, blocking every other tool on the server.

```python
# Bulkhead: separate connection pools per dependency
github_semaphore = asyncio.Semaphore(10)   # max 10 concurrent GitHub calls
database_semaphore = asyncio.Semaphore(20)  # max 20 concurrent DB queries
search_semaphore = asyncio.Semaphore(5)     # max 5 concurrent search ops

async def github_tool(params):
    if not github_semaphore.locked():
        async with github_semaphore:
            return await call_github(params)
    else:
        return tool_error(
            "GitHub tools are at capacity (10/10 concurrent requests). "
            "Try again in a few seconds, or use an alternative tool."
        )
```

**Combine bulkheads with circuit breakers** for comprehensive fault isolation: the bulkhead limits concurrent requests while the circuit breaker detects persistent failures.

## Resilience Pattern 4: Rate Limiting

Rate limiting protects both your MCP server and the downstream services it calls.

### Server-Side Rate Limiting

Limit how many tool calls a client can make per time window:

```python
# Token bucket rate limiter
class RateLimiter:
    def __init__(self, rate, burst):
        self.rate = rate      # tokens per second
        self.burst = burst    # max burst size
        self.tokens = burst
        self.last_refill = time.time()

    def allow(self):
        self._refill()
        if self.tokens >= 1:
            self.tokens -= 1
            return True
        return False
```

### Downstream Rate Limit Awareness

When external APIs return rate limit information, propagate it in your error messages:

```
Rate limited by Slack API. Limit: 50 requests/minute.
Current window: 50/50 used. Resets in 34 seconds.
Retry-After: 34 seconds. Consider batching multiple operations
into a single tool call if possible.
```

## Timeout Budget Allocation

The "Bridging Protocol and Production" paper (arxiv 2603.13417) proposes Adaptive Timeout Budget Allocation (ATBA) — framing sequential tool invocation as a budget allocation problem.

### The Problem

An AI agent making a chain of 5 tool calls has an overall time budget (say, 30 seconds for the user to get a response). If the first tool takes 25 seconds, the remaining four tools have only 5 seconds combined — likely resulting in timeouts and a degraded experience.

### Timeout Budget Strategies

1. **Fixed per-tool timeout:** Simple but wasteful — fast tools don't need their full allocation
2. **Proportional allocation:** Divide the remaining budget based on historical latency percentiles for each tool
3. **Adaptive allocation:** Track p50/p95/p99 latencies per tool and allocate budgets dynamically, giving more time to tools that historically need it

```python
# Adaptive timeout budget
class TimeoutBudget:
    def __init__(self, total_budget_ms):
        self.remaining = total_budget_ms
        self.start = time.monotonic()

    def allocate(self, tool_name, latency_stats):
        elapsed = (time.monotonic() - self.start) * 1000
        self.remaining = self.remaining - elapsed
        # Give this tool its p95 latency, but cap at remaining budget
        p95 = latency_stats[tool_name]["p95"]
        return min(p95 * 1.2, self.remaining * 0.8)  # keep 20% reserve
```

**For MCP tool errors on timeout:** include the time spent and suggest alternatives — "Database query timed out after 5.2 seconds. Consider adding a LIMIT clause or querying a smaller date range."

## Session Recovery for Streamable HTTP

Streamable HTTP transport (the successor to SSE, with SSE deprecated April 1, 2026) introduces session management via the `Mcp-Session-Id` header. Sessions can be invalidated by server restarts, idle timeouts, or explicit termination — and recovery is a known pain point.

### Common Session Failure Modes

Production deployments have reported several systematic issues:

- **Session drop after ~89 minutes:** HTTP connections dropping with "No transport found for sessionId"
- **Stale session ID:** After server restart, client continues sending old `Mcp-Session-Id`, server returns 404, but client doesn't reinitialize
- **SSE 404 misinterpretation:** Some clients treat SSE 404 responses as "SSE not supported" rather than "session expired," preventing reconnection

### Recovery Strategies

1. **Client-side session monitoring:** Track session health, detect 404 responses as session expiration, and trigger reinitialization
2. **Exponential backoff reconnection:** On session loss, reconnect with backoff to avoid thundering herd
3. **Event replay via `Last-Event-ID`:** Streamable HTTP supports resumability — send the last received event ID to resume from where you left off
4. **Server-side session persistence:** Store session state in Redis or similar external store so sessions survive server restarts

### SEP-1442: Stateless Future

SEP-1442 proposes eliminating mandatory session state entirely — stateless-by-default with per-request capabilities. This would resolve many session recovery issues by removing the session concept from the critical path. As of March 2026, the proposal has 88+ comments and is actively discussed.

## Graceful Degradation Patterns

When services are unavailable, MCP servers should degrade gracefully rather than failing completely.

### Degradation Strategies

| Strategy | When to Use | Example |
|----------|------------|---------|
| **Cached fallback** | Data is available but stale | Return cached API response with "Data from 2 hours ago — live API is currently unavailable" |
| **Reduced functionality** | Some features work, others don't | "Full search is unavailable. Basic keyword search is still working." |
| **Alternative tool suggestion** | A different tool can accomplish similar goals | "GitHub API is down. You can still search the local git repository using the git_log tool." |
| **Partial results** | Some data retrieved before failure | "Retrieved 47 of 100 results before the connection dropped. Here are the partial results." |
| **Queue for later** | Operation can be deferred | "Cannot send the notification now. Added to retry queue — will be sent when Slack API recovers." |

### Implementing Graceful Degradation

```python
async def search_tool(query):
    try:
        # Primary: live API search
        results = await api_search(query)
        return format_results(results, source="live")
    except APIUnavailable:
        try:
            # Fallback 1: cached results
            cached = await cache.search(query)
            return format_results(cached, source="cache",
                note="Live search unavailable. Showing cached results "
                     f"from {cached.timestamp}. Results may be outdated.")
        except CacheMiss:
            # Fallback 2: local search
            local = await local_index.search(query)
            return format_results(local, source="local",
                note="Both live and cached search unavailable. "
                     "Showing results from local index only.")
```

## Interceptors: SEP-1763

SEP-1763 proposes an interceptor framework for MCP — hooks that can intercept, validate, and transform messages at various points in the protocol lifecycle. For error handling, interceptors enable:

- **Validation interceptors:** Validate tool inputs before execution, with severity levels (info, warn, error)
- **Error transformation interceptors:** Normalize error formats across different tools and servers
- **Observability interceptors:** Log all errors with consistent structure for monitoring and alerting
- **Recovery interceptors:** Automatically retry transient failures or apply fallback logic

Interceptors can be deployed on both client and server sides, supporting both synchronous validation and asynchronous observation.

## The SERF Framework

The Structured Error Recovery Framework (SERF), proposed in "Bridging Protocol and Production" (arxiv 2603.13417), addresses a fundamental gap: MCP has no standard way to express error semantics that enable deterministic agent self-correction.

### SERF's Approach

SERF extends JSON-RPC error responses with machine-readable failure semantics:

- **Error classification:** Is this transient, permanent, or requires human intervention?
- **Recovery actions:** Specific, machine-executable recovery steps
- **Retry policy:** Can this be retried? With what backoff? Maximum attempts?
- **Alternative tools:** Which other tools can accomplish the same goal?

### Why This Matters

Without structured error semantics, LLMs must interpret free-text error messages — which works sometimes but fails when errors are ambiguous, technical, or inconsistent across servers. SERF aims to make error recovery deterministic rather than probabilistic.

## The MCP Reliability Playbook

The MCP Reliability Playbook (github.com/alexey-tyurin/reliable-mcp) is a reference implementation that demonstrates nine resilience patterns through a working chatbot with two MCP servers, LangGraphJS agent orchestration, and comprehensive testing.

### Nine Patterns Implemented

1. Circuit breakers for external API calls
2. Retry with exponential backoff and jitter
3. Bulkhead isolation per dependency
4. Timeout management
5. Graceful degradation with cached fallbacks
6. Health check endpoints
7. Structured logging and observability
8. Chaos testing framework
9. Error response sanitization (never leak stack traces)

### Testing Approach

The playbook includes 317 tests and 63 evaluations, with 16 automated chaos tests covering scenarios like:

- LLM calls tools during weather API faults — graceful degradation
- Agent continues responding during Redis faults
- System remains responsive during compound failures
- Error responses never leak stack traces

## OpenAI Agents SDK: Built-In MCP Resilience

OpenAI's Agents SDK (v0.12.5+) includes built-in MCP retry and error normalization, reflecting how the ecosystem is standardizing error handling:

- Automatic retry for transient MCP connection failures
- Error normalization across different MCP server implementations
- Connection health monitoring and automatic reconnection

## Production Error Handling Checklist

### Transport Layer
- [ ] Handle connection timeouts with configurable limits
- [ ] Implement reconnection with exponential backoff
- [ ] For Streamable HTTP: handle session expiration (404) correctly
- [ ] For stdio: ensure only JSON-RPC goes to stdout, everything else to stderr
- [ ] Monitor connection health with periodic heartbeats

### Protocol Layer
- [ ] Return proper JSON-RPC error codes for protocol violations
- [ ] Handle all five standard error codes (-32700 through -32603)
- [ ] Define custom error codes for your application domain
- [ ] Validate incoming JSON structure before processing

### Application Layer
- [ ] Use `isError: true` for all tool execution failures (not protocol errors)
- [ ] Write error messages for LLM consumption, not human developers
- [ ] Include current state, recovery actions, and alternatives in error messages
- [ ] Return input validation errors as tool errors (per SEP-1303), not protocol errors
- [ ] Never expose stack traces, internal paths, or credentials in error messages

### Resilience
- [ ] Implement circuit breakers per external dependency
- [ ] Use exponential backoff with jitter for retries
- [ ] Apply bulkhead isolation for independent dependencies
- [ ] Set timeout budgets for multi-tool chains
- [ ] Implement graceful degradation with cached/partial/alternative responses

### Observability
- [ ] Log all errors to stderr (stdio) or structured logging (HTTP)
- [ ] Include correlation IDs for tracing requests across services
- [ ] Track error rates per tool, per dependency, per error type
- [ ] Set up alerts for circuit breaker state changes
- [ ] Record latency percentiles for timeout budget tuning

## Ecosystem: Error Handling Tools and Resources

| Project | What It Does | Stars/Status |
|---------|-------------|-------------|
| **MCP Reliability Playbook** | 9 resilience patterns with chaos testing | Reference impl, 317 tests |
| **MCPcat** | MCP debugging, error guides, serialization diagnosis | Active, multiple guides |
| **Alpic AI mcp-eval** | MCP server evaluation including error handling quality | Open source |
| **OpenAI Agents SDK** | Built-in MCP retry and error normalization (v0.12.5+) | Part of Agents SDK |
| **FastMCP** | Python framework with built-in error handling patterns | 24K+ stars |
| **MCPEx (Elixir)** | Protocol error module with all standard codes | v0.1.0 |
| **Resilience4j** | Circuit breaker / bulkhead / retry for JVM MCP servers | Mature, widely used |
| **SEP-1303** | Input validation as tool errors (proposed) | Under discussion |
| **SEP-1763** | Interceptor framework for validation/error transformation | Under discussion |
| **SEP-1391** | Long-running operations with error state management | Under discussion |
| **SERF** (arxiv 2603.13417) | Structured error recovery framework | Academic proposal |
| **Fault Taxonomy** (arxiv 2603.05637) | 5-category MCP fault classification | Empirical study |

## Getting Started

If you're building an MCP server today, prioritize in this order:

1. **Use `isError: true` correctly** — this is the single highest-impact change. Make sure tool failures return tool errors, not protocol errors
2. **Write LLM-friendly error messages** — include state, recovery actions, and alternatives. Test by asking: "Could an LLM reading this message know what to try next?"
3. **Add retries with backoff** — handle transient failures automatically before they reach the LLM
4. **Implement circuit breakers** — for any external API or database your server depends on
5. **Set up graceful degradation** — cached fallbacks, partial results, alternative tools
6. **Add observability** — you can't fix what you can't see. Log errors to stderr with structured context

The MCP error handling landscape is maturing rapidly. SEP-1303, SEP-1763, and the SERF proposal all aim to standardize patterns that are currently implemented ad hoc. Building on these patterns today means your servers will be ready when the protocol catches up.

## Further Reading

- [MCP Transports Explained](/guides/mcp-transports-explained/) — transport-level error handling and the stdio/HTTP/Streamable HTTP evolution
- [MCP Real-Time Streaming](/guides/mcp-real-time-streaming/) — session management, reconnection, and the stateless future (SEP-1442)
- [MCP AI Safety & Guardrails](/guides/mcp-ai-safety-guardrails/) — error handling in the context of security and incident response
- [MCP Testing Strategies](/guides/mcp-testing-strategies/) — testing error paths and failure scenarios
- [Building MCP Clients](/guides/building-mcp-clients/) — client-side error handling and retry logic
- [MCP Server Performance Tuning](/guides/mcp-server-performance-tuning/) — timeout tuning and resource management
- [MCP Microservices & Service Mesh](/guides/mcp-microservices-service-mesh/) — distributed error handling with circuit breakers and service mesh
- [Debugging MCP Servers](/guides/debugging-mcp-servers/) — diagnosing error causes with MCP Inspector and logging

