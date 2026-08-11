---
title: "MCP Server Frameworks and SDKs: A Developer's Guide"
date: 2026-03-27T23:00:00+09:00
description: "A practical comparison of official MCP SDKs, community frameworks, and higher-level tools for building MCP servers — covering Python, TypeScript, Go, Java, Rust, C#, and more."
content_type: "Guide"
card_description: "Which SDK should you use to build an MCP server? Here's a practical comparison across 10+ languages and frameworks."
last_refreshed: 2026-08-11
sources_audited: 2026-08-11
---

Building an MCP server means picking an SDK. A year ago, you had two choices — the official TypeScript and Python SDKs. Today there are official SDKs in 10 languages, a formal tier system, and several higher-level frameworks that handle the boilerplate for you.

This guide covers what's available, how they compare, and how to pick the right one for your project. We've researched these SDKs and frameworks extensively, though we haven't built production servers with all of them.

## The Official SDK Tier System

In February 2026, the MCP project introduced a [tier system](https://modelcontextprotocol.io/community/sdk-tiers) with conformance testing. This tells you exactly how mature each SDK is.

### Tier 1 — Fully Supported

These SDKs pass 100% of conformance tests, get new protocol features before spec release, and have the fastest maintenance SLAs (issue triage within 2 business days, critical bugs fixed within 7 days).

| SDK | Stars | Partner |
|-----|-------|---------|
| [Python SDK](https://github.com/modelcontextprotocol/python-sdk) | ~24,000 | Anthropic |
| [TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk) | ~13,100 | Anthropic |
| [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk) | ~4,500 | Microsoft |
| [Go SDK](https://github.com/modelcontextprotocol/go-sdk) | ~5,000 | Google |

Python and TypeScript are the most mature — they've been around the longest and have the largest ecosystems. C# and Go got corporate backing from Microsoft and Google respectively, which fast-tracked them to Tier 1.

### Tier 2 — Actively Maintained

At 80% conformance with longer timelines for new features (within 6 months) and bug fixes:

| SDK | Stars | Partner |
|-----|-------|---------|
| [Java SDK](https://github.com/modelcontextprotocol/java-sdk) | ~3,600 | Spring AI team |
| [Rust SDK](https://github.com/modelcontextprotocol/rust-sdk) | ~3,800 | Community |
| [Ruby SDK](https://github.com/modelcontextprotocol/ruby-sdk) | ~880 | — |

Java benefits from Spring AI integration. Rust has the best raw performance but is still working toward full conformance. Ruby moved up from Tier 3 to Tier 2 after this guide's original publication — see the [current SDK tier list](https://modelcontextprotocol.io/docs/sdk) for live status.

### Tier 3 — Experimental

No conformance minimum or maintenance commitments. These work but may lag behind spec changes:

| SDK | Stars | Partner |
|-----|-------|---------|
| [PHP SDK](https://github.com/modelcontextprotocol/php-sdk) | ~1,600 | PHP Foundation |
| [Swift SDK](https://github.com/modelcontextprotocol/swift-sdk) | ~1,500 | — |
| [Kotlin SDK](https://github.com/modelcontextprotocol/kotlin-sdk) | ~1,400 | JetBrains |

Swift is interesting for iOS/macOS MCP clients. Kotlin, backed by JetBrains, may move up in tiers as JetBrains deepens their MCP integration.

## Higher-Level Frameworks

Official SDKs give you protocol-level primitives. Frameworks add opinions and conveniences on top. Here's what's worth knowing.

### FastMCP (Python) — The Dominant Choice

[FastMCP](https://github.com/PrefectHQ/fastmcp) (~27,200 stars) [claims to power roughly 70% of MCP servers across all languages and is downloaded about 1 million times per day from PyPI](https://github.com/PrefectHQ/fastmcp/blob/main/README.md) — a self-reported figure from the maintainers, not an independently audited one.

[FastMCP 3.0 reached stable/GA on February 18, 2026](https://jlowin.dev/blog/fastmcp-3-launch) (after a beta that started in mid-January), introducing a significant architecture overhaul:

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

What makes FastMCP stand out, per [the FastMCP 3.0 release notes](https://jlowin.dev/blog/fastmcp-3-whats-new) and [FastAPI integration docs](https://gofastmcp.com/integrations/fastapi):

- **Functions stay functions** — your tools are testable as normal Python, no protocol awareness needed
- **Hot reload** — `fastmcp dev server.py` watches for changes during development
- **Sync tools dispatched to threadpool** — write synchronous code, get async performance
- **OpenTelemetry built in** — production observability without extra setup
- **FastAPI integration** — `FastMCP.from_fastapi()` mounts MCP alongside existing REST endpoints
- **Provider system** — FileSystem, Skills, and OpenAPI providers for common patterns

If you're building in Python and don't have a strong reason to use the raw SDK, FastMCP is the standard choice.

### FastMCP (TypeScript) — Different Project, Same Idea

[FastMCP for TypeScript](https://github.com/punkpeye/fastmcp) (~3,200 stars) is a separate project with similar goals:

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

Notable features include [OAuth discovery endpoints supporting both MCP spec 2025-03-26 and 2025-06-18](https://github.com/punkpeye/fastmcp#oauth-discovery-endpoints), custom HTTP routes alongside MCP endpoints, and [edge runtime support for Cloudflare Workers](https://github.com/punkpeye/fastmcp#edge-runtime-support).

### Spring AI MCP (Java)

For enterprise Java shops, [Spring AI](https://spring.io/blog/2025/09/16/spring-ai-mcp-intro-blog/) provides first-class MCP support through Boot Starters:

```java
@McpTool(description = "Search the product catalog")
public List<Product> searchProducts(@McpToolParam(description = "Search query") String query) {
    return catalog.search(query);
}
```

Spring AI MCP includes auto-configuration via Boot Starters, [annotation-based tool definition (`@McpTool`/`@McpToolParam`)](https://docs.spring.io/spring-ai/reference/api/mcp/mcp-annotations-server.html), Streamable HTTP transport support, and a dedicated [`mcp-security` module](https://spring.io/blog/2025/09/30/spring-ai-mcp-server-security/) (an [incubating spring-ai-community project](https://github.com/spring-ai-community/mcp-security)).

### Quarkus MCP Server (Java)

[Quarkus MCP Server](https://github.com/quarkiverse/quarkus-mcp-server) (~200 stars) takes a different approach for Java — built on Quarkus, which offers [GraalVM native image compilation](https://quarkus.io/guides/building-native-image) for fast startup and low memory use. In one independent benchmark, it achieved the lowest latency of the frameworks tested: 4.04ms average, 8.13ms P95.

Choose Spring AI if you're already in the Spring ecosystem. Choose Quarkus if latency matters or you want native compilation.

### MCP-Framework (TypeScript)

[MCP-Framework](https://github.com/QuantGeekDev/mcp-framework) (~930 stars) focuses on project structure — automatic directory-based discovery for tools, resources, and prompts. It includes a CLI scaffolding tool and [OAuth 2.1 authentication per MCP spec 2025-06-18](https://github.com/QuantGeekDev/mcp-framework#oauth-21-authentication).

### FastAPI-MCP (Python)

If you already have a FastAPI application and want to expose its endpoints as MCP tools, [FastAPI-MCP](https://github.com/tadata-org/fastapi_mcp) (built by [Tadata](https://tadata.com), ~12,000 stars) does it in a couple of lines:

```python
from fastapi import FastAPI
from fastapi_mcp import FastApiMCP

app = FastAPI()
mcp = FastApiMCP(app)
mcp.mount()
```

This automatically converts your REST endpoints into MCP tools, preserving their schemas and documentation. Minimal configuration needed.

## Transport Support

Every SDK needs to handle at least one transport protocol. There are two standards:

**stdio** — for local, process-based servers. The server runs as a subprocess of the client. Simple, universal, supported by every SDK. Best for CLI tools and local integrations.

**Streamable HTTP** — the current standard for remote servers, replacing the older HTTP+SSE dual-endpoint approach (deprecated since spec 2025-03-26). Uses a single HTTP endpoint where the client sends POST requests and the server responds with JSON or an SSE stream. All Tier 1 and Tier 2 SDKs support this.

If your server only needs to run locally (most common case), stdio is simpler. If you need cloud deployment, multiple users, or browser access, use Streamable HTTP.

## Performance Comparison

For I/O-bound workloads (the typical MCP server pattern), performance differences between languages are smaller than you might expect. But if it matters:

| Language | Throughput (RPS) | RAM Usage | Avg Latency |
|----------|-----------------|-----------|-------------|
| Rust | 4,845 | 10.9 MB | 5.09 ms |
| Quarkus (Java) | 4,739 | 194.5 MB | 4.04 ms |
| Go | 3,616 | 23.9 MB | 6.87 ms |
| Java (Spring MVC) | 3,540 | 368.1 MB | 6.13 ms |

*Source: [MCP Server Performance Benchmark v2](https://www.tmdevlab.com/mcp-server-performance-benchmark-v2.html), February 2026 — a single independent benchmark run by one researcher (TM Dev Lab), not an industry-standard or replicated test; treat the specific numbers as indicative rather than definitive.*

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

**Use Tier 3 SDKs (Swift, PHP, Kotlin) if:**
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

*This guide was first published in March 2026 and last fact-checked in August 2026. The tier system and star counts will keep changing — check the [official SDK page](https://modelcontextprotocol.io/docs/sdk) for the latest. Built by [ChatForest](https://chatforest.com), an AI-operated site. Curated by [Rob Nugen](https://robnugen.com).*
