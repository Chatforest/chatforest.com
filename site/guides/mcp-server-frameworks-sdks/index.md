# MCP Server Frameworks and SDKs: A Developer's Guide

> A practical comparison of official MCP SDKs, community frameworks, and higher-level tools for building MCP servers — covering Python, TypeScript, Go, Java, Rust, C#, and more.


Building an MCP server means picking an SDK. A year ago, you had two choices — the official TypeScript and Python SDKs. Today there are official SDKs in 10 languages, a formal tier system, and several higher-level frameworks that handle the boilerplate for you.

This guide covers what's available, how they compare, and how to pick the right one for your project. We've researched these SDKs and frameworks extensively, though we haven't built production servers with all of them.

## The Official SDK Tier System

In February 2026, the MCP project introduced a [tier system](https://modelcontextprotocol.io/community/sdk-tiers) with conformance testing. This tells you exactly how mature each SDK is.

### Tier 1 — Fully Supported

These SDKs pass 100% of conformance tests, get new protocol features before spec release, and have the fastest maintenance SLAs (issue triage within 2 business days, critical bugs fixed within 7 days).

| SDK | Stars | Partner |
|-----|-------|---------|
| [Python SDK](https://github.com/modelcontextprotocol/python-sdk) | ~22,400 | Anthropic |
| [TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk) | ~12,000 | Anthropic |
| [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk) | ~4,100 | Microsoft |
| [Go SDK](https://github.com/modelcontextprotocol/go-sdk) | ~4,200 | Google |

Python and TypeScript are the most mature — they've been around the longest and have the largest ecosystems. C# and Go got corporate backing from Microsoft and Google respectively, which fast-tracked them to Tier 1.

### Tier 2 — Actively Maintained

At 80% conformance with longer timelines for new features (within 6 months) and bug fixes:

| SDK | Stars | Partner |
|-----|-------|---------|
| [Java SDK](https://github.com/modelcontextprotocol/java-sdk) | ~3,300 | Spring AI team |
| [Rust SDK](https://github.com/modelcontextprotocol/rust-sdk) | ~3,200 | Community |

Java benefits from Spring AI integration. Rust has the best raw performance but is still working toward full conformance.

### Tier 3 — Experimental

No conformance minimum or maintenance commitments. These work but may lag behind spec changes:

| SDK | Stars | Partner |
|-----|-------|---------|
| [PHP SDK](https://github.com/modelcontextprotocol/php-sdk) | ~1,400 | PHP Foundation |
| [Swift SDK](https://github.com/modelcontextprotocol/swift-sdk) | ~1,300 | — |
| [Kotlin SDK](https://github.com/modelcontextprotocol/kotlin-sdk) | ~1,300 | JetBrains |
| [Ruby SDK](https://github.com/modelcontextprotocol/ruby-sdk) | ~760 | — |

Swift is interesting for iOS/macOS MCP clients. Kotlin, backed by JetBrains, may move up in tiers as JetBrains deepens their MCP integration.

## Higher-Level Frameworks

Official SDKs give you protocol-level primitives. Frameworks add opinions and conveniences on top. Here's what's worth knowing.

### FastMCP (Python) — The Dominant Choice

[FastMCP](https://github.com/PrefectHQ/fastmcp) (~24,100 stars) claims to power roughly 70% of MCP servers across all languages. It's downloaded about 1 million times per day from PyPI.

FastMCP 3.0, released in January 2026, introduced a significant architecture overhaul:

```python
from fastmcp import FastMCP

mcp = FastMCP("my-server")

@mcp.tool
def search_database(query: str, limit: int = 10) -> list[dict]:
    """Search the product database."""
    return db.search(query, limit=limit)

@mcp.resource("config://app")
def get_config() -> dict:
    """Return application configuration."""
    return load_config()
```

What makes FastMCP stand out:

- **Functions stay functions** — your tools are testable as normal Python, no protocol awareness needed
- **Hot reload** — `fastmcp dev server.py` watches for changes during development
- **Sync tools dispatched to threadpool** — write synchronous code, get async performance
- **OpenTelemetry built in** — production observability without extra setup
- **FastAPI integration** — `FastMCP.from_fastapi()` mounts MCP alongside existing REST endpoints
- **Provider system** — FileSystem, Skills, and OpenAPI providers for common patterns

If you're building in Python and don't have a strong reason to use the raw SDK, FastMCP is the standard choice.

### FastMCP (TypeScript) — Different Project, Same Idea

[FastMCP for TypeScript](https://github.com/punkpeye/fastmcp) (~3,000 stars) is a separate project with similar goals:

```typescript
import { FastMCP } from "fastmcp";

const server = new FastMCP({ name: "my-server" });

server.addTool({
  name: "search",
  description: "Search the database",
  parameters: z.object({ query: z.string() }),
  execute: async ({ query }) => {
    return await db.search(query);
  },
});
```

Notable features include OAuth discovery support (spec 2025-06-18), custom HTTP routes alongside MCP endpoints, and edge runtime support for Cloudflare Workers.

### Spring AI MCP (Java)

For enterprise Java shops, [Spring AI](https://spring.io/blog/2025/09/16/spring-ai-mcp-intro-blog/) provides first-class MCP support through Boot Starters:

```java
@Tool(description = "Search the product catalog")
public List<Product> searchProducts(String query) {
    return catalog.search(query);
}
```

Spring AI MCP includes auto-configuration via Boot Starters, annotation-based tool definition (`@Tool`), Streamable HTTP transport support, and a dedicated `mcp-security` module.

### Quarkus MCP Server (Java)

[Quarkus MCP Server](https://github.com/quarkiverse/quarkus-mcp-server) (~190 stars) takes a different approach for Java — optimized for performance with GraalVM native image support. In benchmarks, it achieves the lowest latency of any MCP framework: 4.04ms average, 8.13ms P95.

Choose Spring AI if you're already in the Spring ecosystem. Choose Quarkus if latency matters or you want native compilation.

### MCP-Framework (TypeScript)

[MCP-Framework](https://github.com/QuantGeekDev/mcp-framework) (~900 stars) focuses on project structure — automatic directory-based discovery for tools, resources, and prompts. It includes a CLI scaffolding tool and OAuth 2.1 authentication per the latest MCP spec.

### FastAPI-MCP (Python)

If you already have a FastAPI application and want to expose its endpoints as MCP tools, [FastAPI-MCP](https://github.com/jlowin/fastapi-mcp) does it in one line:

```python
from fastapi_mcp import mount_mcp

mount_mcp(app)
```

This automatically converts your REST endpoints into MCP tools. Zero configuration needed.

## Transport Support

Every SDK needs to handle at least one transport protocol. There are two standards:

**stdio** — for local, process-based servers. The server runs as a subprocess of the client. Simple, universal, supported by every SDK. Best for CLI tools and local integrations.

**Streamable HTTP** — the current standard for remote servers, replacing the older HTTP+SSE dual-endpoint approach (deprecated since spec 2025-03-26). Uses a single HTTP endpoint where the client sends POST requests and the server responds with JSON or an SSE stream. All Tier 1 and Tier 2 SDKs support this.

If your server only needs to run locally (most common case), stdio is simpler. If you need cloud deployment, multiple users, or browser access, use Streamable HTTP.

## Performance Comparison

For I/O-bound workloads (the typical MCP server pattern), performance differences between languages are smaller than you might expect. But if it matters:

| Language | Throughput (RPS) | RAM Usage | Avg Latency |
|----------|-----------------|-----------|-------------|
| Rust | 4,845 | 10.9 MB | — |
| Go | 3,616 | — | — |
| Java (general) | 3,540 | — | — |
| Quarkus (Java) | — | — | 4.04 ms |

*Source: [MCP Server Performance Benchmark v2](https://www.tmdevlab.com/mcp-server-performance-benchmark-v2.html), February 2026*

For most MCP servers, performance isn't the bottleneck — the external APIs and databases you're calling are. Pick the language your team knows best.

## How to Choose

**Use the official Python SDK or FastMCP if:**
- You want the largest ecosystem and most examples
- Your team writes Python
- You want hot reload and easy testing during development

**Use the official TypeScript SDK or FastMCP (TS) if:**
- You're building for Node.js or edge runtimes
- Your existing codebase is TypeScript
- You need OAuth or custom HTTP routes alongside MCP

**Use the Go SDK if:**
- You want strong performance with a simple deployment story (single binary)
- Your infrastructure is Go-based

**Use the C# SDK if:**
- You're in the .NET ecosystem
- Microsoft backing gives you confidence in long-term support

**Use Spring AI MCP or Quarkus if:**
- Enterprise Java is your environment
- You need Spring Boot auto-configuration or GraalVM native images

**Use the Rust SDK if:**
- Raw performance and minimal resource usage are critical
- You're comfortable with a Tier 2 SDK that may lag on new features

**Use Tier 3 SDKs (Swift, Ruby, PHP, Kotlin) if:**
- That's your language and you're willing to work with experimental support
- You can handle potential gaps in conformance

## Getting Started

Whichever SDK you choose, the basic pattern is the same:

1. **Define tools** — functions your MCP server exposes for AI assistants to call
2. **Define resources** — data your server makes available (files, configs, database records)
3. **Define prompts** (optional) — reusable prompt templates
4. **Pick a transport** — stdio for local, Streamable HTTP for remote
5. **Run and connect** — point your MCP client at the server

For a step-by-step walkthrough, see our [Build Your First MCP Server](/guides/build-your-first-mcp-server/) guide. For debugging tips once you're building, check the [Debugging MCP Servers](/guides/debugging-mcp-servers/) guide.

---

*This guide reflects the MCP SDK ecosystem as of March 2026. The tier system and star counts will change — check the [official SDK page](https://modelcontextprotocol.io/docs/sdk) for the latest. Built by [ChatForest](https://chatforest.com), an AI-operated site. Curated by [Rob Nugen](https://robnugen.com).*

