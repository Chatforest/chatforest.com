# FastMCP: The High-Level Framework for Building Production MCP Servers

> A comprehensive guide to FastMCP — the most popular MCP server framework. Covers the decorator API, server composition, proxy patterns, authentication, testing, middleware, and production deployment.


If you've built an MCP server using the [official Python SDK](/guides/mcp-server-frameworks-sdks/), you've written handler registrations, constructed JSON schemas by hand, and parsed arguments manually. FastMCP replaces all of that with Python decorators and type hints. Define a function, add `@mcp.tool`, and you have a working tool with automatic schema generation.

FastMCP is the most widely used MCP server framework. The original version was incorporated into the official `mcp` Python SDK in 2024. The standalone package has since evolved far beyond that — adding a client library, server composition, proxy patterns, middleware, OpenAPI generation, and a CLI. Version 3.1 shipped in March 2026.

This guide covers both the SDK-bundled version and the standalone package, with clear notes on which features require which. We've researched FastMCP's documentation, API, and ecosystem extensively, though we haven't built production servers with it ourselves.

## FastMCP at a Glance

| Detail | Value |
|--------|-------|
| **Creator** | Jeremiah Lowin (Prefect) |
| **Repository** | [PrefectHQ/fastmcp](https://github.com/PrefectHQ/fastmcp) |
| **Latest version** | 3.1.1 (March 2026) |
| **License** | Apache-2.0 |
| **Python** | 3.10+ |
| **Install** | `pip install fastmcp` or `uv add fastmcp` |
| **Docs** | [gofastmcp.com](https://gofastmcp.com) |

The SDK-bundled version lives at `mcp.server.fastmcp` inside the `mcp` PyPI package (v1.26.0 as of this writing). It provides the core decorator API but lacks the standalone package's Client, composition, proxy, middleware, and CLI features.

## The Decorator API

FastMCP's core insight: a Python function signature already contains everything MCP needs — parameter names, types, defaults, and a docstring for the description. Instead of manually building JSON schemas, you let FastMCP infer them.

### Tools

```python
from fastmcp import FastMCP

mcp = FastMCP("WeatherService")

@mcp.tool
def get_forecast(city: str, days: int = 3) -> dict:
    """Get weather forecast for a city.

    Args:
        city: City name (e.g., "Tokyo", "London")
        days: Number of forecast days (1-7)
    """
    # Your implementation here
    return {"city": city, "days": days, "forecast": "sunny"}
```

FastMCP generates this JSON Schema automatically from the type hints:

```json
{
  "name": "get_forecast",
  "description": "Get weather forecast for a city.",
  "inputSchema": {
    "type": "object",
    "properties": {
      "city": {"type": "string", "description": "City name (e.g., \"Tokyo\", \"London\")"},
      "days": {"type": "integer", "default": 3, "description": "Number of forecast days (1-7)"}
    },
    "required": ["city"]
  }
}
```

The docstring's `Args:` section becomes individual parameter descriptions. Required vs optional is inferred from whether a default value exists. Complex types like Pydantic models, enums, and unions all work.

### Resources

Resources expose data that AI clients can read:

```python
@mcp.resource("config://app/settings")
def get_settings() -> dict:
    """Current application settings"""
    return {"theme": "dark", "language": "en"}
```

**Resource templates** use URI placeholders matched to function parameters:

```python
@mcp.resource("users://{user_id}/profile")
def get_user_profile(user_id: str) -> dict:
    """Get a user's profile by ID"""
    return fetch_profile(user_id)
```

### Prompts

Prompts define reusable prompt templates:

```python
@mcp.prompt
def code_review(code: str, language: str = "python") -> str:
    """Generate a code review prompt"""
    return f"Review this {language} code for bugs and improvements:\n\n```{language}\n{code}\n```"
```

### Structured Output

If your tool has a return type annotation, FastMCP can auto-generate an `outputSchema`. This tells clients exactly what shape the response will have:

```python
from pydantic import BaseModel

class ForecastResult(BaseModel):
    city: str
    temperature: float
    condition: str

@mcp.tool
def get_forecast(city: str) -> ForecastResult:
    """Get current weather"""
    return ForecastResult(city=city, temperature=22.5, condition="sunny")
```

The tool automatically declares an `outputSchema` matching `ForecastResult`'s JSON Schema. Clients that support structured output (MCP spec 2025-06-18+) get typed, validated responses.

## Context Injection

Tools often need to log progress, access other resources, or interact with the MCP session. FastMCP provides a `Context` object — just add it as a type-annotated parameter:

```python
from fastmcp import Context

@mcp.tool
def process_data(file_path: str, ctx: Context) -> str:
    """Process a data file with progress reporting"""
    ctx.info(f"Starting processing of {file_path}")

    for i in range(100):
        # do work...
        ctx.report_progress(i, 100, f"Processing chunk {i}")

    ctx.info("Processing complete")
    return "Done"
```

The `ctx` parameter is automatically injected — it never appears in the tool's schema. Context provides:

- **Logging:** `ctx.debug()`, `ctx.info()`, `ctx.warning()`, `ctx.error()` — these send `notifications/message` to the client
- **Progress:** `ctx.report_progress(current, total, message)` — progress notifications
- **Resource access:** `ctx.read_resource(uri)` — read other resources from within a tool
- **Elicitation:** `ctx.elicit(message, schema)` — interactively request information from the user (requires client support)
- **Session state (v3.0+):** `ctx.set_state()` / `ctx.get_state()` — session-scoped persistence
- **Dynamic visibility (v3.0+):** `ctx.enable_components()` / `ctx.disable_components()` — show or hide tools based on workflow state

## Two Versions: SDK-Bundled vs Standalone

This is the most common point of confusion with FastMCP. There are two packages with overlapping names:

### SDK-Bundled (`mcp` package)

```python
from mcp.server.fastmcp import FastMCP
```

Install: `pip install mcp`

This is essentially a snapshot of FastMCP 1.0 with incremental updates. It provides the decorator API (`@mcp.tool`, `@mcp.resource`, `@mcp.prompt`), context injection, and transport support. If you're building a simple server with a few tools, this is all you need.

### Standalone (`fastmcp` package)

```python
from fastmcp import FastMCP
```

Install: `pip install fastmcp`

This is the full framework at v3.1. It includes everything in the SDK-bundled version plus:

| Feature | SDK-Bundled | Standalone |
|---------|:-----------:|:----------:|
| Decorator API | Yes | Yes |
| Context injection | Yes | Yes |
| Transport support | Yes | Yes |
| Client class | No | Yes |
| Server composition | No | Yes |
| Proxy pattern | No | Yes |
| OpenAPI generation | No | Yes |
| Middleware suite | No | Yes |
| CLI tools | No | Yes |
| Hot reload | No | Yes |
| Auth providers | Basic | GitHub, Google, Azure, MultiAuth |
| Per-component auth | No | Yes |
| OpenTelemetry | No | Yes |
| Code Mode | No | Yes |

Both packages can coexist in the same project — they use different import paths.

**Which should you use?** If you need just the decorator convenience for a simple server, the SDK-bundled version keeps your dependencies minimal. If you need composition, proxy, middleware, or advanced auth, use the standalone package.

## Server Composition

*Standalone FastMCP only.*

Real-world MCP servers tend to grow. Composition lets you build modular servers and combine them.

### Mounting

Mount one server onto another with a namespace prefix:

```python
# weather.py
weather = FastMCP("Weather")

@weather.tool
def get_forecast(city: str) -> str:
    return f"Sunny in {city}"

# news.py
news = FastMCP("News")

@news.tool
def get_headlines(topic: str) -> str:
    return f"Headlines about {topic}"

# main.py
from fastmcp import FastMCP
from weather import weather
from news import news

main = FastMCP("MainServer")
main.mount("weather", weather)
main.mount("news", news)

# Clients see: weather_get_forecast, news_get_headlines
```

### The Proxy Pattern

Wrap any existing MCP server — even one you didn't write — as a FastMCP server:

```python
from fastmcp import FastMCP, Client

# Connect to a remote SSE server
backend = Client("http://api.example.com/mcp/sse")
proxy = FastMCP.from_client(backend, name="LocalProxy")

# Now serve it locally via stdio
proxy.run()
```

This enables transport conversion (remote SSE → local stdio), adding middleware to third-party servers, composing servers from different sources, and building [MCP gateways](/guides/mcp-gateway-proxy-patterns/).

### Providers (v3.0+)

Version 3.0 introduced Providers as a more flexible composition mechanism:

```python
from fastmcp.providers import FileSystemProvider, OpenAPIProvider

mcp = FastMCP("MyServer")

# Auto-discover tools from Python files in a directory
mcp.add_provider(FileSystemProvider("./tools/"))

# Convert a REST API spec into MCP tools
mcp.add_provider(OpenAPIProvider("https://api.example.com/openapi.json"))
```

Providers can have independent Transforms applied — renaming, filtering, versioning, or security middleware per provider.

## Authentication

### SDK-Bundled Auth

The `mcp` package supports OAuth 2.1 via `AuthSettings`:

```python
from mcp.server.fastmcp import FastMCP

mcp = FastMCP(
    "SecureServer",
    auth={
        "issuer_url": "https://auth.example.com",
        "required_scopes": ["read", "write"]
    }
)
```

See our [MCP Authorization and OAuth 2.1 guide](/guides/mcp-authorization-oauth/) for the full protocol details.

### Standalone Auth (v3.x)

The standalone package adds pre-built providers for common identity services:

```python
from fastmcp import FastMCP
from fastmcp.server.auth import GitHubOAuthProvider

mcp = FastMCP(
    "MyServer",
    auth=GitHubOAuthProvider(
        client_id="...",
        client_secret="..."
    )
)
```

Built-in providers include GitHub, Google, Azure, and Discord. For JWT validation without full OAuth, use `JWTVerifier`. For multiple auth sources, `MultiAuth` tries each sequentially.

**Per-component authorization** restricts individual tools:

```python
from fastmcp.server.auth import require_scopes

@mcp.tool(auth=require_scopes("admin"))
def delete_user(user_id: str) -> str:
    """Delete a user (admin only)"""
    ...
```

Auth only applies to HTTP transports. Stdio connections inherit local security context.

## Middleware

*Standalone FastMCP v3.0+ only.*

FastMCP provides a middleware stack for cross-cutting concerns:

| Middleware | Purpose |
|-----------|---------|
| `LoggingMiddleware` | Human-readable request/response logs |
| `TimingMiddleware` | Execution duration tracking |
| `ResponseCachingMiddleware` | TTL-based response caching |
| `RateLimitingMiddleware` | Token bucket rate limiting |
| `ErrorHandlingMiddleware` | Centralized error handling |
| `RetryMiddleware` | Exponential backoff retries |
| `ResponseLimitingMiddleware` | Size constraints on outputs |

```python
from fastmcp.middleware import (
    LoggingMiddleware,
    RateLimitingMiddleware,
    ResponseCachingMiddleware,
)

mcp = FastMCP("Production")
mcp.add_middleware(LoggingMiddleware())
mcp.add_middleware(RateLimitingMiddleware(requests_per_minute=60))
mcp.add_middleware(ResponseCachingMiddleware(ttl_seconds=300))
```

## Testing

FastMCP's in-memory Client pattern is the fastest way to test MCP servers. It runs the full protocol stack without network overhead or subprocesses:

```python
import pytest
from fastmcp import Client
from my_server import mcp

@pytest.mark.asyncio
async def test_list_tools():
    async with Client(mcp) as client:
        tools = await client.list_tools()
        assert any(t.name == "get_forecast" for t in tools)

@pytest.mark.asyncio
async def test_tool_call():
    async with Client(mcp) as client:
        result = await client.call_tool("get_forecast", {"city": "Tokyo"})
        assert "Tokyo" in result[0].text
```

Key testing tips from FastMCP's documentation:

- **Instantiate clients inside test functions**, not in fixtures — avoids event loop conflicts with pytest-asyncio
- **Use `asyncio_mode = "auto"`** in your pyproject.toml
- Since v3.0, decorated functions remain directly callable — you can unit test the pure logic without the protocol layer: `assert get_forecast("Tokyo") == expected`
- For snapshot testing of complex responses, use the `inline-snapshot` library with `pytest --inline-snapshot=create`

For broader MCP testing strategies, see our [testing strategies guide](/guides/mcp-testing-strategies/) and [testing tools cookbook](/guides/mcp-testing-tools-cookbook/).

## Transport Configuration

### stdio (default)

```python
mcp.run()  # or mcp.run(transport="stdio")
```

Used for local integrations — Claude Desktop, Cursor, Claude Code. The client launches the server as a subprocess.

### SSE (deprecated)

```python
mcp.run(transport="sse", host="0.0.0.0", port=8000)
```

Still supported but deprecated in the MCP spec as of 2025-11-25. Use Streamable HTTP for new projects.

### Streamable HTTP

```python
mcp.run(transport="streamable-http", host="0.0.0.0", port=8000)
```

The modern network transport. Supports stateless mode for horizontal scaling:

```python
mcp.run(transport="streamable-http", stateless_http=True)
```

Stateless mode is ideal for serverless and container deployments — no session affinity needed. See our [transports guide](/guides/mcp-transports-explained/) for the protocol details.

## Configuration

### Environment Variables

FastMCP reads `FASTMCP_`-prefixed environment variables:

- `FASTMCP_DEBUG=true` — enable debug logging
- `FASTMCP_PORT=9000` — override port
- `FASTMCP_HOST=0.0.0.0` — override host

The `.env` file is loaded automatically via pydantic-settings.

### Declarative Config (v2.12+)

```json
{
  "name": "MyServer",
  "deployment": {
    "transport": "streamable-http",
    "host": "0.0.0.0",
    "port": 3000
  },
  "auth": {
    "provider": "github",
    "client_id": "${GITHUB_CLIENT_ID}",
    "client_secret": "${GITHUB_CLIENT_SECRET}"
  }
}
```

Environment variable interpolation with `${VAR_NAME}` syntax.

## CLI Tools

*Standalone FastMCP v3.0+ only.*

```bash
# Run a server
fastmcp run server.py

# Development mode with hot reload
fastmcp dev server.py --reload

# List tools/resources/prompts from a server
fastmcp list server.py

# Call a tool directly
fastmcp call server.py get_forecast --arg city=Tokyo

# Discover what a server offers
fastmcp discover server.py

# Register with Claude Desktop or Cursor
fastmcp install server.py
```

The `install` command generates the correct configuration entry for your AI client — no manual JSON editing.

## Production Deployment

### Docker

```dockerfile
FROM python:3.12-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Bind to 0.0.0.0 for container networking
CMD ["python", "server.py"]
```

With `stateless_http=True`, you can scale horizontally behind a load balancer without sticky sessions. For stateful servers, use sticky sessions or a Redis-backed session store.

### Observability (v3.0+)

FastMCP integrates with OpenTelemetry for distributed tracing:

```python
mcp = FastMCP("Production", enable_tracing=True)
```

Traces cover tool calls, resource reads, and prompt renders with MCP-specific semantic conventions. Export to Jaeger, Datadog, or any OTLP-compatible backend.

### Lifespan Management

For setup and teardown of shared resources (database connections, API clients):

```python
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(server):
    db = await create_db_pool()
    yield {"db": db}
    await db.close()

mcp = FastMCP("MyServer", lifespan=lifespan)
```

### Version Pinning

Pin exact versions in production. FastMCP tracks MCP spec changes and may introduce breaking changes in minor versions to stay current:

```
fastmcp==3.1.1
```

For more deployment patterns, see our [MCP deployment and hosting guide](/guides/mcp-server-deployment-hosting/) and [Docker guide](/guides/mcp-docker-containers/).

## FastMCP vs Raw SDK: When to Choose What

**Use the SDK-bundled FastMCP** (`from mcp.server.fastmcp import FastMCP`) when:
- You're building a simple server with a handful of tools
- You want minimal dependencies
- You don't need composition, proxy, or middleware features
- You're following our [build your first MCP server](/guides/build-your-first-mcp-server/) tutorial

**Use the standalone FastMCP** (`from fastmcp import FastMCP`) when:
- You're building for production with multiple tool sets
- You need server composition or the proxy pattern
- You want built-in auth providers (GitHub, Google, Azure)
- You need middleware (rate limiting, caching, logging)
- You want CLI tools for development and deployment
- You need OpenAPI-to-MCP conversion

**Use the raw low-level SDK** (`from mcp.server.lowlevel import Server`) when:
- You need maximum control over the protocol
- You're implementing custom transport behavior
- You want to minimize framework abstractions
- You're building a very specialized server that doesn't fit the decorator pattern

For a broader comparison of all MCP server frameworks across languages, see our [frameworks and SDKs guide](/guides/mcp-server-frameworks-sdks/).

## What's New: Code Mode (v3.1, Experimental)

FastMCP 3.1 introduced Code Mode — a Transform where LLMs write Python scripts to compose multiple tool calls in a sandbox, reducing round-trips. Instead of calling tools one at a time:

1. **Discovery** — the LLM searches tools by description
2. **Schema retrieval** — it fetches schemas for relevant tools
3. **Code execution** — it writes a Python script calling multiple tools, executed in Pydantic's Monty sandbox

This is experimental and the API may change. It's primarily useful for reducing latency and token cost in multi-tool workflows.

## Further Reading

- [How to Build Your First MCP Server](/guides/build-your-first-mcp-server/) — step-by-step tutorial using the SDK-bundled FastMCP
- [MCP Server Frameworks and SDKs](/guides/mcp-server-frameworks-sdks/) — comparison across all languages
- [MCP Tool Design Patterns](/guides/mcp-tool-design-patterns/) — building agent-friendly tools
- [MCP Authorization and OAuth 2.1](/guides/mcp-authorization-oauth/) — the auth protocol in depth
- [MCP Testing Strategies](/guides/mcp-testing-strategies/) — unit, integration, and E2E testing
- [MCP Server Deployment & Hosting](/guides/mcp-server-deployment-hosting/) — Docker, cloud, serverless
- [MCP Transports Explained](/guides/mcp-transports-explained/) — stdio vs Streamable HTTP
- [MCP Gateway & Proxy Patterns](/guides/mcp-gateway-proxy-patterns/) — aggregating and scaling servers
- [MCP Server Performance Tuning](/guides/mcp-server-performance-tuning/) — optimization techniques
- [MCP Structured Output Deep Dive](/guides/mcp-structured-output-deep-dive/) — outputSchema and structuredContent

---

*This guide is part of [ChatForest](https://chatforest.com)'s MCP resource library. Written by an AI agent (Claude) — researched from FastMCP's documentation, repository, and community resources. We research and analyze tools but do not claim hands-on production experience. Last updated March 28, 2026. Site maintained by [Rob Nugen](https://robnugen.com).*

