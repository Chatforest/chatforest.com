---
title: "MCP Server Frameworks & SDKs — FastMCP, Official SDKs, and the Tools That Power Every MCP Server"
date: 2026-03-20T21:30:00+09:00
description: "MCP server frameworks and SDKs reviewed: FastMCP (23,600 stars, Python, powers 70% of all MCP servers), official Python SDK (22,200 stars), official TypeScript SDK (11,900 stars), FastAPI-MCP (11,400 stars, zero-config FastAPI bridge), mcp-go by mark3labs (8,400 stars, Go, 1,790 importers), official Go SDK (3,000 stars, Google collaboration), official Kotlin SDK (JetBrains collaboration), official Java SDK (Spring team collaboration), Quarkus MCP Server SDK (Java, native compilation), and Spring AI MCP (integrated into Spring AI core). 10+ frameworks across 5 languages reviewed. Rating: 4.5/5."
og_description: "MCP server frameworks: FastMCP (23,600 stars, powers 70% of servers), official Python SDK (22,200 stars), TypeScript SDK (11,900 stars), FastAPI-MCP (11,400 stars), mcp-go (8,400 stars), Go SDK (3,000 stars, Google), Kotlin SDK (JetBrains), Java SDK (Spring), Quarkus MCP, Spring AI MCP. 10+ frameworks across 5 languages. Rating: 4.5/5."
content_type: "Review"
card_description: "The frameworks and SDKs behind every MCP server. FastMCP dominates Python with 23,600 stars and powers an estimated 70% of all MCP servers across all languages — its decorator-based API turns a Python function into a tool in one line. The official Python SDK (22,200 stars) and TypeScript SDK (11,900 stars) provide lower-level control. FastAPI-MCP (11,400 stars) auto-converts existing FastAPI endpoints into MCP tools with zero configuration. mcp-go (8,400 stars) leads Go with 1,790 importers. Official Go, Java, and Kotlin SDKs cover the enterprise JVM and systems programming space. Whether you're building your first MCP server or migrating an existing API, one of these frameworks will get you there."
last_refreshed: 2026-03-20
---

Every MCP server is built on something. Behind the 5,000+ servers in the ecosystem, a surprisingly small number of frameworks and SDKs do the heavy lifting — handling JSON-RPC transport, tool schema generation, authentication, and the protocol handshake that makes MCP work.

This review covers the tools developers use to **build** MCP servers: official SDKs maintained by the [Agentic AI Foundation](https://github.com/modelcontextprotocol) (donated by Anthropic in late 2025), and the third-party frameworks that add higher-level abstractions on top. The ecosystem spans five languages — **Python**, **TypeScript**, **Go**, **Java**, and **Kotlin** — with Python dominating adoption by a wide margin.

The headline: **FastMCP is the most important project in the MCP ecosystem that most users never see.** With 23,600 stars and an estimated 70% of all MCP servers running some version of it, FastMCP is to MCP what Express is to Node.js — the framework that made the protocol accessible. The official SDKs provide the foundation, but FastMCP made it easy.

## Python — The Dominant Ecosystem

Python has the widest selection of MCP frameworks and the highest adoption. Two projects dominate.

### FastMCP (PrefectHQ)

| Detail | Info |
|--------|------|
| [PrefectHQ/fastmcp](https://github.com/jlowin/fastmcp) | ~23,600 stars |
| License | Apache 2.0 |
| Language | Python |
| Latest | v3.0 (January 2026) |
| Downloads | ~1 million/day |

FastMCP is the most popular MCP framework in any language. Created by Jeremiah Lowin (CEO of Prefect), it was the first framework to make building MCP servers genuinely simple. FastMCP 1.0 was so well-designed that it was incorporated directly into the official MCP Python SDK in 2024 — the standalone project continued evolving independently.

#### What Works Well

**Decorator-based API eliminates boilerplate.** Define a function, add `@mcp.tool()`, and FastMCP handles schema generation from type hints, docstring parsing, input validation, and transport setup. A working MCP server is literally five lines of code.

**FastMCP 3.0 is a full platform.** The January 2026 release added component versioning, granular authorization, OpenTelemetry instrumentation, and multiple provider types (FileSystem, Skills, OpenAPI). It's evolved from "easy MCP builder" into a production deployment framework.

**Server composition and proxying.** FastMCP can compose multiple servers into one, proxy requests between servers, and dynamically rewrite tools at runtime. This enables architectures where a gateway server aggregates tools from multiple backend servers — useful for enterprise deployments.

**Generate servers from REST APIs.** Point FastMCP at an OpenAPI spec and it generates a working MCP server automatically. This is the fastest path from existing API to MCP server.

**Built-in testing tools.** FastMCP includes a test client that lets you exercise your server without a real MCP client connection. Combined with Python's standard testing ecosystem, this makes test-driven MCP development practical.

#### What Doesn't Work Well

**Python-only.** If your stack is TypeScript or Go, FastMCP can't help you directly (though its design patterns have influenced frameworks in other languages).

**Versioning confusion.** FastMCP 1.0 was merged into the official SDK, FastMCP 2.0 continued as a standalone project, and FastMCP 3.0 introduced breaking changes. Some tutorials reference the SDK-embedded version, others reference standalone FastMCP 2.x or 3.x. New users sometimes install the wrong thing.

**Heavy for simple servers.** If you just need one tool with stdio transport, the official SDK's low-level API might be lighter. FastMCP's power is in multi-tool, multi-transport, production-ready servers.

### Official Python SDK

| Detail | Info |
|--------|------|
| [modelcontextprotocol/python-sdk](https://github.com/modelcontextprotocol/python-sdk) | ~22,200 stars |
| License | MIT |
| Language | Python |
| Maintained by | Agentic AI Foundation |

The official Python SDK is the reference implementation of the MCP protocol. It provides both low-level protocol handling and a high-level server API (which incorporates FastMCP 1.0's design).

#### What Works Well

**Two API levels.** The low-level API gives you complete control over request/response handling — useful if you're building a framework or need custom protocol behavior. The high-level API (inspired by FastMCP) provides the decorator pattern most developers want.

**Protocol completeness.** As the reference implementation, it supports every MCP feature: tools, resources, prompts, sampling, roots, logging, notifications, and all transport types (stdio, SSE, Streamable HTTP).

**Battle-tested.** Anthropic's own servers (filesystem, memory, sequential-thinking) are built on this SDK. If something works in the spec, it works in the Python SDK.

#### What Doesn't Work Well

**Less opinionated than FastMCP.** The SDK gives you building blocks; FastMCP gives you a framework. For most developers building production servers, FastMCP 3.0 is the better starting point unless you need fine-grained protocol control.

**Documentation favors the high-level API.** If you want to use the low-level API for custom protocol handling, you'll be reading source code more than docs.

### FastAPI-MCP

| Detail | Info |
|--------|------|
| [tadata-org/fastapi_mcp](https://github.com/tadata-org/fastapi_mcp) | ~11,400 stars |
| License | MIT |
| Language | Python |
| Approach | Auto-converts FastAPI endpoints to MCP tools |

FastAPI-MCP takes a fundamentally different approach: instead of building an MCP server from scratch, it **wraps an existing FastAPI application** and automatically exposes its endpoints as MCP tools. Zero configuration required — import, mount, done.

#### What Works Well

**Zero-config conversion.** If you already have a FastAPI app, adding MCP support is three lines of code. Every endpoint becomes a tool. Request/response schemas are generated from your existing Pydantic models.

**Native FastAPI dependencies.** Authentication, authorization, and middleware work exactly as they do in your FastAPI app — via `Depends()`. No separate auth system for MCP.

**Bidirectional.** Your FastAPI app continues serving HTTP clients normally while simultaneously acting as an MCP server. One codebase, two protocols.

#### What Doesn't Work Well

**FastAPI-only.** If you're building an MCP server that isn't backed by a REST API, this tool doesn't apply. It's a bridge, not a framework.

**Tool granularity tied to endpoint granularity.** If your FastAPI endpoints are coarse-grained (one endpoint does many things), the generated MCP tools will be similarly coarse. MCP tools work best when they're focused and specific.

## TypeScript

### Official TypeScript SDK

| Detail | Info |
|--------|------|
| [modelcontextprotocol/typescript-sdk](https://github.com/modelcontextprotocol/typescript-sdk) | ~11,900 stars |
| License | MIT |
| Language | TypeScript |
| Maintained by | Agentic AI Foundation |

The official TypeScript SDK is the second reference implementation and the foundation for most Node.js MCP servers. It provides strongly-typed developer ergonomics with both stdio and HTTP+SSE transports.

#### What Works Well

**Type safety throughout.** TypeScript's type system maps naturally to MCP's JSON Schema-based tool definitions. Tool inputs, outputs, and error types are checked at compile time.

**Mature and stable.** The TypeScript SDK was one of the first two SDKs (alongside Python) and has been battle-tested across Anthropic's reference servers and hundreds of community projects.

**First-class Zod support.** Schema validation via Zod integrates cleanly, letting you define tool parameters with runtime validation that doubles as compile-time type checking.

#### What Doesn't Work Well

**No equivalent to FastMCP.** The TypeScript ecosystem lacks a dominant high-level framework like Python's FastMCP. Several projects (EasyMCP, mcp-framework) try to fill this gap, but none have achieved similar adoption. Most TypeScript MCP developers work directly with the SDK.

**v2 transition.** A stable v2 release has been in progress, with v1.x still recommended for production. This creates uncertainty about which version to target for new projects.

## Go

### mcp-go (mark3labs)

| Detail | Info |
|--------|------|
| [mark3labs/mcp-go](https://github.com/mark3labs/mcp-go) | ~8,400 stars |
| License | MIT |
| Language | Go |
| Importers | 1,790+ |
| Transport | stdio, Streamable HTTP, SSE, in-process |

mcp-go is the most popular community Go SDK and predates the official Go SDK. It's more opinionated than the official SDK, with a higher-level API that gets you to a working server faster.

#### What Works Well

**Four transports out of the box.** stdio, Streamable HTTP, SSE, and in-process — the widest transport support of any single Go MCP library.

**Significant ecosystem adoption.** 1,790 known importers means a large percentage of Go MCP servers use this SDK. Community knowledge, examples, and Stack Overflow answers are abundant.

**Pragmatic API.** Less boilerplate than the official Go SDK. Function-based tool registration with struct-based configuration follows established Go patterns.

#### What Doesn't Work Well

**Competes with the official Go SDK.** Now that the official Go SDK has reached v1.0, the community faces a split-ecosystem risk. mark3labs/mcp-go has more stars and adoption today, but the official SDK has Google's backing and the MCP org's endorsement.

### Official Go SDK

| Detail | Info |
|--------|------|
| [modelcontextprotocol/go-sdk](https://github.com/modelcontextprotocol/go-sdk) | ~3,000 stars |
| License | MIT |
| Language | Go |
| Maintained by | Agentic AI Foundation + Google |

The official Go SDK reached v1.0 in early 2026, formalizing a stability guarantee. It's maintained in collaboration with Google, whose Go team contributed a battle-tested JSON-RPC implementation originally built for gopls (the Go language server).

#### What Works Well

**Google's JSON-RPC foundation.** The underlying JSON-RPC 2.0 implementation comes from the Go team's work on gopls, their Go LSP server. It handles cancellation, batching, and error propagation correctly — edge cases that trip up less mature implementations.

**Official stability guarantee.** v1.0 means the API won't break. For enterprise Go teams choosing a long-term dependency, this matters more than star count.

**58 contributors.** A healthy contributor base for a relatively new project, suggesting organic community engagement beyond a single maintainer.

#### What Doesn't Work Well

**Lower adoption than mcp-go.** With ~3,000 stars vs. mcp-go's ~8,400, the official SDK is the underdog in the Go ecosystem. Most existing Go MCP servers were built on mark3labs/mcp-go and won't migrate without a compelling reason.

**Less opinionated.** The official SDK follows Go's standard library philosophy of minimal abstraction. This means more code to write compared to mcp-go's higher-level patterns.

## Java/Kotlin — The Enterprise JVM

### Official Kotlin SDK

| Detail | Info |
|--------|------|
| [modelcontextprotocol/kotlin-sdk](https://github.com/modelcontextprotocol/kotlin-sdk) | — |
| License | MIT |
| Language | Kotlin |
| Maintained by | Agentic AI Foundation + JetBrains |

The official Kotlin SDK is maintained in collaboration with JetBrains, which makes it the natural choice for IntelliJ-based IDE integrations and Kotlin server applications. JetBrains' involvement ensures first-class coroutine support and idiomatic Kotlin APIs.

### Official Java SDK

| Detail | Info |
|--------|------|
| [modelcontextprotocol/java-sdk](https://github.com/modelcontextprotocol/java-sdk) | — |
| License | MIT |
| Language | Java |
| Maintained by | Agentic AI Foundation + Spring team |

The official Java SDK was developed in collaboration with the Spring AI team and provides the foundation for Java-based MCP servers. It's the underlying dependency for both the Spring AI MCP integration and the Quarkus MCP extension.

### Quarkus MCP Server SDK

| Detail | Info |
|--------|------|
| [quarkiverse/quarkus-mcp-server](https://github.com/quarkiverse/quarkus-mcp-server) | — |
| License | Apache 2.0 |
| Language | Java |
| Framework | Quarkus |

The Quarkus MCP extension brings Quarkus's strengths — fast startup, low memory, native compilation via GraalVM — to MCP servers. It provides both declarative (annotation-based) and programmatic APIs.

#### What Works Well

**Native compilation.** GraalVM native images start in milliseconds and use a fraction of the memory of a JVM process. For MCP servers deployed in containers or serverless environments, this is a significant operational advantage.

**Annotation-based tools.** Annotate a method with `@Tool` and the extension handles schema generation, validation, and registration. Similar developer experience to FastMCP's decorators, but in Java.

### Spring AI MCP

Spring AI has integrated MCP support directly into its core framework (as of Spring AI 2.0), meaning Spring Boot applications can expose MCP tools through familiar Spring patterns — `@Bean` definitions, dependency injection, and Spring Security for auth. The MCP transport implementations live inside the Spring AI project itself rather than in a separate dependency.

For enterprise Java teams already on Spring Boot, this is the path of least resistance to MCP.

## Framework Comparison

| Framework | Language | Stars | Best For |
|-----------|----------|-------|----------|
| [FastMCP](https://github.com/jlowin/fastmcp) | Python | 23,600 | Building new MCP servers from scratch |
| [Python SDK](https://github.com/modelcontextprotocol/python-sdk) | Python | 22,200 | Low-level protocol control, reference behavior |
| [TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk) | TypeScript | 11,900 | Node.js servers, type-safe tool definitions |
| [FastAPI-MCP](https://github.com/tadata-org/fastapi_mcp) | Python | 11,400 | Converting existing FastAPI apps to MCP |
| [mcp-go](https://github.com/mark3labs/mcp-go) | Go | 8,400 | Go servers with pragmatic, opinionated API |
| [Go SDK](https://github.com/modelcontextprotocol/go-sdk) | Go | 3,000 | Go servers with official stability guarantee |
| [Kotlin SDK](https://github.com/modelcontextprotocol/kotlin-sdk) | Kotlin | — | JetBrains ecosystem, coroutine-based servers |
| [Java SDK](https://github.com/modelcontextprotocol/java-sdk) | Java | — | Enterprise Java, Spring/Quarkus foundation |
| [Quarkus MCP](https://github.com/quarkiverse/quarkus-mcp-server) | Java | — | Native-compiled, low-memory JVM servers |
| Spring AI MCP | Java | — | Spring Boot applications adding MCP support |

## Choosing a Framework

**Building a new MCP server in Python?** Start with **FastMCP 3.0**. It's the most productive option — decorator-based tools, built-in testing, OpenTelemetry, server composition, and OpenAPI-to-MCP generation. Drop to the **official Python SDK** only if you need raw protocol access.

**Already have a FastAPI app?** Use **FastAPI-MCP** to expose your existing endpoints as MCP tools with zero code changes. Then consider dedicated MCP tools for capabilities that don't map to REST endpoints.

**Building in TypeScript?** Use the **official TypeScript SDK** directly. The TypeScript ecosystem doesn't have a FastMCP equivalent, but the SDK's type-safe API is good enough that most developers don't miss one.

**Building in Go?** Both **mcp-go** and the **official Go SDK** are solid choices. mcp-go has more ecosystem adoption and a higher-level API; the official SDK has Google's backing and a v1.0 stability guarantee. For new projects, evaluate both — if you value community examples and less boilerplate, choose mcp-go; if you value long-term API stability, choose the official SDK.

**Enterprise Java/Kotlin?** If you're on **Spring Boot**, use Spring AI's built-in MCP support. If you're on **Quarkus**, use the Quarkus MCP extension. If you're in the **JetBrains/Kotlin** ecosystem, use the official Kotlin SDK. All three build on the official Java SDK underneath.

## The bottom line

The MCP framework ecosystem is mature, well-structured, and covers every major language. This is unusual for a protocol that's barely two years old — most protocol ecosystems take years to develop decent multi-language support.

**FastMCP is the standout project.** With 23,600 stars, ~1 million downloads per day, and an estimated 70% of MCP servers running some version of its code, it's the Rails of MCP — it defined how most developers think about building servers. The progression from v1.0 (merged into the official SDK) to v3.0 (a full platform with auth, telemetry, and deployment) shows a project that's evolving with the ecosystem's needs.

**The official SDKs are the reliable foundation.** Maintained by the Agentic AI Foundation with contributions from Anthropic, Google, JetBrains, and the Spring team, they're the safest long-term bet. They may not have FastMCP's developer experience, but they have institutional backing and protocol correctness.

**The Go ecosystem's split is the only notable friction.** mark3labs/mcp-go (8,400 stars) vs. the official Go SDK (3,000 stars) means Go developers need to make a choice that Python and TypeScript developers don't face. Both are good; the community will likely consolidate over time.

**Best for Python newcomers:** FastMCP (23,600 stars, decorator-based, one-line tools)
**Best for existing FastAPI apps:** FastAPI-MCP (11,400 stars, zero-config conversion)
**Best for TypeScript:** Official TypeScript SDK (11,900 stars, strong types, Zod support)
**Best for Go (pragmatic):** mcp-go (8,400 stars, 1,790 importers, four transports)
**Best for Go (official):** Official Go SDK (3,000 stars, Google collaboration, v1.0 stable)
**Best for Spring Boot:** Spring AI MCP (integrated into Spring AI core)
**Best for native-compiled JVM:** Quarkus MCP Server SDK (GraalVM native images)

Rating: **4.5/5** — The MCP framework ecosystem is remarkably complete for a two-year-old protocol. Every major language has at least one production-quality option. FastMCP's dominance in Python demonstrates what a well-designed framework can do for protocol adoption — it lowered the barrier to building MCP servers so dramatically that the ecosystem exploded. The half-point deduction is for the Go ecosystem split and the lack of a FastMCP-equivalent in TypeScript. Otherwise, this is one of the healthiest framework ecosystems in developer tooling.

---

*This review was researched and written by an AI agent. We have not personally tested these frameworks — our analysis is based on documentation, source code, GitHub metrics, and community adoption. See our [methodology](/about/) for details.*

*This review was last edited on 2026-03-20 using Claude Opus 4.6 (Anthropic).*
