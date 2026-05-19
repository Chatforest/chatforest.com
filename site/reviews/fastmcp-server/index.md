# FastMCP — The Python Framework Powering 70% of MCP Servers

> FastMCP is the dominant Python framework for building MCP servers and clients. 25.2K GitHub stars, 15.9M+ PyPI downloads per week, decorator-based API, proxy servers, OpenAPI providers, and OAuth support. Created by Prefect's CEO.


Part of our **[Agent Orchestration MCP category](/categories/agent-orchestration/)**.

*At a glance: 25,200 GitHub stars, 2,000 forks, Apache-2.0 license, Python 3.10+, v3.3.1 (May 15, 2026). PyPI ~15.9M downloads/week (~65M/month). Created by Jeremiah Lowin (Prefect founder/CEO). Powers an estimated 70% of MCP servers across all languages. Originally created days after the MCP spec was announced. FastMCP Python ranks #6 on best-of-mcp-servers vs official Python SDK at #262. 100th release shipped in May 2026.*

FastMCP isn't an MCP server — it's the framework most MCP servers are built with. When the Model Context Protocol specification was released in late 2024, Jeremiah Lowin (founder and CEO of [Prefect](https://www.prefect.io/), the workflow orchestration platform) built FastMCP within days. The project was quickly incorporated into the official MCP Python SDK, and today some version of FastMCP powers roughly 70% of all MCP servers across all languages. It's downloaded roughly 16 million times per week from PyPI — making it one of the most downloaded AI infrastructure packages in the Python ecosystem.

The pitch is simple: building MCP servers with the raw SDK requires extensive boilerplate — JSON schemas, handler registration, transport configuration. FastMCP replaces all of that with Python decorators. You write `@mcp.tool()` on a function, and FastMCP infers the JSON schema from type hints, registers the handler, and manages the transport. This reduces setup code by roughly 70% compared to the raw SDK.

## What It Does

FastMCP is built around three core primitives:

**Tools** — Python functions exposed to LLMs via MCP. Decorate with `@mcp.tool()` and FastMCP handles schema generation from type hints:

```python
from fastmcp import FastMCP

mcp = FastMCP("My Server")

@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers."""
    return a + b
```

**Resources** — Read-only data endpoints (files, database records, configs, dynamic content) exposed via `@mcp.resource()`.

**Prompts** — Reusable interaction templates that guide LLMs on how to use your server's capabilities, via `@mcp.prompt()`.

### Provider Architecture (v3.0+)

FastMCP 3.0 (released January 19, 2026) introduced a provider-based architecture that unifies how components are sourced:

- **FileSystemProvider** — Discovers decorated functions from directories with optional hot-reload
- **OpenAPIProvider** — Wraps any REST API's OpenAPI spec as MCP tools automatically
- **ProxyProvider** — Proxies remote MCP servers, converting between transport protocols (e.g., expose a stdio server via SSE)
- **SkillsProvider** — Delivers agent skill files as MCP resources

### Code Mode (v3.1)

FastMCP 3.1 shipped "Code Mode" — the most requested feature since launch. Instead of making sequential tool calls, the LLM writes Python code that calls your tools as functions, and FastMCP executes it. This dramatically reduces round-trips for complex workflows.

### Authorization

Granular authorization on individual components with async auth checks, server-wide policies via `AuthMiddleware`, and scope-based access control. Supports OAuth (including CIMD, Static Client Registration, Azure OBO), JWT audience validation, and confused-deputy protections.

### Client Support

FastMCP includes a full MCP client implementation, not just the server side. You can use it to connect to any MCP server programmatically from Python.

## Setup

```bash
pip install fastmcp
```

Create a server:

```python
from fastmcp import FastMCP

mcp = FastMCP("Demo")

@mcp.tool()
def greet(name: str) -> str:
    """Greet someone."""
    return f"Hello, {name}!"
```

Run it:

```bash
fastmcp run server.py
```

Or install in Claude Desktop:

```bash
fastmcp install server.py
```

For optional extras: `pip install fastmcp[openai,anthropic,azure,code-mode,apps,tasks]`

## What's Good

**Developer experience** — FastMCP's decorator API is genuinely excellent. If you've used FastAPI, you already know how to use FastMCP. Type hints become JSON schemas, docstrings become tool descriptions. The mental model is immediately familiar to Python developers.

**Ecosystem dominance** — ~16M weekly PyPI downloads, 100th release shipped May 2026, 84%+ issue close rate. This isn't a side project — it's infrastructure. The project hit its 100th total release this month, with a sustained cadence that briefly paused for v3.3.0's development sprint before shipping three versions in four days (v3.3.0b1 through v3.3.1, May 11–15).

**Provider architecture** — The v3.0 provider system is a genuine architectural innovation. OpenAPIProvider alone is transformative — point it at any REST API's OpenAPI spec and get MCP tools automatically. ProxyProvider enables protocol bridging between stdio, SSE, and Streamable HTTP.

**Code Mode** — Letting LLMs write Python that calls tools as functions instead of making individual tool calls is a meaningful latency and context-window optimization.

**Transport flexibility** — Supports stdio, SSE, and Streamable HTTP out of the box. Convert between them with ProxyProvider.

**fastmcp-slim (v3.3.0)** — A new lightweight PyPI distribution strips out Starlette and Uvicorn for use in CI environments, agents, or libraries that only need client-side functionality. `pip install fastmcp-slim[client]` — same `from fastmcp import Client` API, far smaller footprint. This is an architecturally thoughtful move that avoids forcing heavy server dependencies on client-only users.

**OTEL and observability** — v3.3.0 added full MCP semantic convention compliance. List operations and proxy delegate spans are now instrumented, making FastMCP servers first-class citizens in OpenTelemetry-based observability stacks.

**Active leadership** — Jeremiah Lowin is publicly visible, doing podcast interviews and maintaining the project alongside Prefect. The project has a clear roadmap and responsive maintainership.

## What's Not

**SSRF & Path Traversal in OpenAPIProvider (patched v3.2.0)** — The `_build_url()` method didn't URL-encode path parameters, allowing directory traversal to arbitrary backend endpoints. Patched in v3.2.0 (released March 2026). Anyone using OpenAPIProvider with user-controlled path parameters before v3.2.0 was vulnerable. Upgrade if you haven't.

**DNS Rebinding Protection Gap (issue #3643, open)** — FastMCP's HTTP server lacks DNS rebinding protection, allowing attacker-controlled DNS to redirect requests through a victim's running server. Issue opened March 27, 2026 and still open as of mid-May. Mitigated in practice by binding to localhost (the default), but worth noting for deployments that expose FastMCP on accessible network interfaces.

**Code Mode sandbox limits (PR #4170, pending)** — A pending PR adds default sandbox resource limits and per-execution tool-call caps to Code Mode. Without it, a crafted prompt can cause runaway code execution within the sandbox. The fix is in review but not yet merged.

**Complexity growth** — FastMCP started as an elegant, minimal abstraction. With v3.0's providers, transforms, code mode, agents, and multiple auth strategies, the surface area has expanded significantly. The documentation is good but the learning curve is steeper than it was — and the docs site changelog is conspicuously out of date (last entry: v3.1.1, March 14), so users tracking v3.2.x and v3.3.x changes need to read GitHub release notes directly.

**Not a server itself** — FastMCP is a framework, not a ready-to-use MCP server. You still need to write the actual tool implementations. This is by design, but worth noting for users looking for plug-and-play solutions.

**Python-only** — Despite powering a majority of MCP servers, FastMCP is Python-only. TypeScript developers need different frameworks (EasyMCP, MCP-Framework, or the TypeScript SDK directly). There is a separate "FastMCP" TypeScript project but it's unrelated.

## Licensing

Apache-2.0 license. Interesting history: in v0.4, the code was temporarily relicensed to MIT to facilitate inclusion in the official MCP Python SDK. The standalone project returned to Apache-2.0.

## The Ecosystem Context

FastMCP vs the official MCP Python SDK is not really a competition anymore. FastMCP *wraps* the official SDK. The question is whether you write raw SDK code or use FastMCP's abstractions. For most use cases, FastMCP is the obvious choice — it ships the same spec compliance with dramatically less boilerplate.

The main alternatives in the Python ecosystem:
- **Official MCP Python SDK** (`mcp` on PyPI) — More control, more boilerplate
- **FastAPI-MCP** — For teams already running FastAPI who want to expose endpoints as MCP tools
- **Pydantic AI** — Includes MCP client/server support as part of a broader agent framework (16.4K stars)

In other languages:
- **MCP TypeScript SDK** — The official reference implementation
- **Foxy Contexts** (Go), **Quarkus MCP** (Java) — Language-specific alternatives

## Who's Behind It

Created by **Jeremiah Lowin**, founder and CEO of [Prefect](https://www.prefect.io/) (formerly Prefect.io). Lowin built FastMCP within days of the MCP spec release. Before Prefect, he worked in quantitative finance at King Street Capital and as an ML consultant.

Prefect is a well-funded workflow orchestration company. In January 2026, they launched **Prefect Horizon** — a platform for managing the "context layer" where AI agents interface with business systems, with FastMCP as the technical foundation.

FastMCP is stewarded by PrefectHQ but accepts community contributions (208+ contributors). The project has its own documentation site at [gofastmcp.com](https://gofastmcp.com) and active [GitHub Discussions](https://github.com/PrefectHQ/fastmcp/discussions).

## Bottom Line

FastMCP is the most important project in the MCP ecosystem that isn't the spec itself. It's the de facto standard for building MCP servers in Python, with adoption numbers that dwarf every other framework and most individual servers. The decorator-based API is a genuinely good abstraction, the v3.0 provider architecture enables powerful composition patterns, and the project is actively maintained with a clear roadmap.

v3.3.0 "Slim Reaper" (May 15, 2026) adds two particularly useful things: the `fastmcp-slim` package that removes the Starlette/Uvicorn dependency for client-only use, and full OTEL semantic convention compliance that makes FastMCP servers observable without custom instrumentation. The open DNS rebinding issue and pending Code Mode sandbox limits are worth watching, but neither is a blocker for typical deployments.

The growing complexity is a natural consequence of the project's scope expanding from "simple decorator wrapper" to "full MCP application framework." As long as the core `@mcp.tool()` experience stays clean — and it does — this is a healthy evolution.

If you're building MCP servers in Python, you should be using FastMCP unless you have a specific reason not to.

**ChatForest rating: 4.5 out of 5**

*We research MCP servers from public sources — GitHub repos, documentation, issue trackers, npm/PyPI registries, PulseMCP analytics, and security advisories. We don't test servers hands-on. Ratings reflect our assessment of maintenance quality, security posture, community traction, and practical utility based on available evidence. See our [methodology](/about/methodology/) for details.*

