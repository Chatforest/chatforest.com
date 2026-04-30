# MCP Server Frameworks & SDKs — FastMCP, Official SDKs, and the Tools That Power Every MCP Server

> MCP server frameworks and SDKs reviewed: FastMCP (24,900 stars, Python, powers 70% of all MCP servers), official Python SDK (22,800 stars), official TypeScript SDK (12,300 stars)


Every MCP server is built on something. Behind the 5,000+ servers in the ecosystem, a surprisingly small number of frameworks and SDKs do the heavy lifting — handling JSON-RPC transport, tool schema generation, authentication, and the protocol handshake that makes MCP work.

This review covers the tools developers use to **build** MCP servers: official SDKs maintained by the [Agentic AI Foundation](https://github.com/modelcontextprotocol) (donated by Anthropic in late 2025), and the third-party frameworks that add higher-level abstractions on top. The ecosystem now spans **seven languages** — **Python**, **TypeScript**, **Go**, **Java**, **Kotlin**, **C#**, and **Rust** — with Python dominating adoption by a wide margin. Since our [original review in March 2026](#refresh-history), two new official SDKs have launched (C# with Microsoft, Rust), the official Go SDK surged 50%, and the MCP Apps specification introduced interactive UI capabilities that frameworks are racing to support.

The headline: **FastMCP is the most important project in the MCP ecosystem that most users never see.** With 24,900 stars and an estimated 70% of all MCP servers running some version of it, FastMCP is to MCP what Express is to Node.js — the framework that made the protocol accessible. Its v3.2 release adds MCP Apps support, letting tools return interactive UIs — charts, dashboards, forms — rendered directly in conversations. The official SDKs provide the foundation, but FastMCP made it easy.

**Category:** [Developer Tools](/categories/developer-tools/)

## Python — The Dominant Ecosystem

Python has the widest selection of MCP frameworks and the highest adoption. Two projects dominate.

### FastMCP (PrefectHQ)

| Detail | Info |
|--------|------|
| [PrefectHQ/fastmcp](https://github.com/jlowin/fastmcp) | ~24,900 stars |
| License | Apache 2.0 |
| Language | Python |
| Latest | v3.2.4 (April 2026) |
| Commits | 3,439 |
| Downloads | ~1 million/day |

FastMCP is the most popular MCP framework in any language. Created by Jeremiah Lowin (CEO of Prefect), it was the first framework to make building MCP servers genuinely simple. FastMCP 1.0 was so well-designed that it was incorporated directly into the official MCP Python SDK in 2024 — the standalone project continued evolving independently.

#### What Works Well

**Decorator-based API eliminates boilerplate.** Define a function, add `@mcp.tool()`, and FastMCP handles schema generation from type hints, docstring parsing, input validation, and transport setup. A working MCP server is literally five lines of code.

**FastMCP 3.2 adds MCP Apps — interactive UIs in conversations.** The "Show Don't Tool" release (April 2026) lets tools return charts, dashboards, forms, and maps rendered directly inside the AI chat. `FastMCPApp` is a new provider class that separates LLM-visible tools (`@app.ui()`) from backend tools the UI calls (`@app.tool()`). Five built-in providers ship for common patterns: FileUpload, FormInput, and more. This builds on the [MCP Apps specification](https://blog.modelcontextprotocol.io/posts/2026-01-26-mcp-apps/) co-authored by Anthropic and OpenAI.

**FastMCP 3.0→3.2 is a full platform.** v3.0 (February 2026) added component versioning, granular authorization, OpenTelemetry instrumentation, and multiple provider types. v3.1 added Code Mode for tool discovery. v3.2 added Apps. 96 total releases and 3,439 commits show rapid iteration.

**Prefect Horizon for enterprise deployment.** FastMCP now integrates with Prefect Horizon for production deployment with SSO, tool-level RBAC, audit logging, and observability across MCP stacks.

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
| [modelcontextprotocol/python-sdk](https://github.com/modelcontextprotocol/python-sdk) | ~22,800 stars |
| License | MIT |
| Language | Python |
| Latest | v1.27.0 (April 2026) |
| Commits | 851 |
| Maintained by | Agentic AI Foundation |

The official Python SDK is the reference implementation of the MCP protocol. It provides both low-level protocol handling and a high-level server API (which incorporates FastMCP 1.0's design).

#### What Works Well

**Two API levels.** The low-level API gives you complete control over request/response handling — useful if you're building a framework or need custom protocol behavior. The high-level API (inspired by FastMCP) provides the decorator pattern most developers want.

**Protocol completeness.** As the reference implementation, it supports every MCP feature: tools, resources, prompts, sampling, roots, logging, notifications, and all transport types (stdio, SSE, Streamable HTTP).

**Battle-tested.** Anthropic's own servers (filesystem, memory, sequential-thinking) are built on this SDK. If something works in the spec, it works in the Python SDK.

#### What Doesn't Work Well

**Less opinionated than FastMCP.** The SDK gives you building blocks; FastMCP gives you a framework. For most developers building production servers, FastMCP 3.x is the better starting point unless you need fine-grained protocol control.

**v2 in development.** A v2 release is in progress on the main branch, with v1.x remaining the recommended version for production. v1.x will continue receiving bug fixes and security updates for at least 6 months after v2 ships.

**Documentation favors the high-level API.** If you want to use the low-level API for custom protocol handling, you'll be reading source code more than docs.

### FastAPI-MCP

| Detail | Info |
|--------|------|
| [tadata-org/fastapi_mcp](https://github.com/tadata-org/fastapi_mcp) | ~11,800 stars |
| License | MIT |
| Language | Python |
| Latest | v0.4.0 |
| Commits | 250 |
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
| [modelcontextprotocol/typescript-sdk](https://github.com/modelcontextprotocol/typescript-sdk) | ~12,300 stars |
| License | MIT |
| Language | TypeScript |
| Latest | v1.29.0 (March 2026) |
| Commits | 1,485 |
| Maintained by | Agentic AI Foundation |

The official TypeScript SDK is the second reference implementation and the foundation for most Node.js MCP servers. It provides strongly-typed developer ergonomics with both stdio and HTTP+SSE transports.

#### What Works Well

**Type safety throughout.** TypeScript's type system maps naturally to MCP's JSON Schema-based tool definitions. Tool inputs, outputs, and error types are checked at compile time.

**Mature and stable.** The TypeScript SDK was one of the first two SDKs (alongside Python) and has been battle-tested across Anthropic's reference servers and hundreds of community projects.

**First-class Zod support.** Schema validation via Zod integrates cleanly, letting you define tool parameters with runtime validation that doubles as compile-time type checking.

#### What Doesn't Work Well

**CVE-2026-0621 ReDoS vulnerability patched.** A regular expression denial of service vulnerability in UriTemplate regex patterns was discovered and fixed. A reminder that even foundational SDKs need security attention.

**Zod internalized via Standard Schema.** Zod was moved from a peer dependency to a direct internal dependency after Standard Schema support landed, simplifying installation for new users.

**No equivalent to FastMCP.** The TypeScript ecosystem lacks a dominant high-level framework like Python's FastMCP. Several projects (EasyMCP, mcp-framework) try to fill this gap, but none have achieved similar adoption. Most TypeScript MCP developers work directly with the SDK.

**v2 transition.** A stable v2 release has been in progress, with v1.x still recommended for production. This creates uncertainty about which version to target for new projects. Hono integration improvements (missing peer dependency fix, preventing global Response object override for Next.js compatibility) suggest the SDK is broadening its framework support.

## Go

### mcp-go (mark3labs)

| Detail | Info |
|--------|------|
| [mark3labs/mcp-go](https://github.com/mark3labs/mcp-go) | ~8,600 stars |
| License | MIT |
| Language | Go |
| Latest | v0.49.0 |
| Importers | 1,790+ |
| Transport | stdio, Streamable HTTP, SSE, in-process |

mcp-go is the most popular community Go SDK and predates the official Go SDK. It's more opinionated than the official SDK, with a higher-level API that gets you to a working server faster.

#### What Works Well

**Four transports out of the box.** stdio, Streamable HTTP, SSE, and in-process — the widest transport support of any single Go MCP library.

**Significant ecosystem adoption.** 1,790 known importers means a large percentage of Go MCP servers use this SDK. Community knowledge, examples, and Stack Overflow answers are abundant.

**Pragmatic API.** Less boilerplate than the official Go SDK. Function-based tool registration with struct-based configuration follows established Go patterns.

#### What Doesn't Work Well

**OAuth protected resource metadata (RFC9728).** v0.49.0 added OAuth protected resource metadata discovery and client helpers for extracting metadata URLs from authorization errors — important for the evolving OAuth 2.1 story in MCP.

**Competes with the official Go SDK.** The official Go SDK surged from ~3,000 to ~4,500 stars (+50%) since March, narrowing the gap from 2.8x to 1.9x. mark3labs/mcp-go still leads in adoption and ecosystem examples, but the official SDK's momentum suggests gradual consolidation.

### Official Go SDK

| Detail | Info |
|--------|------|
| [modelcontextprotocol/go-sdk](https://github.com/modelcontextprotocol/go-sdk) | ~4,500 stars |
| License | MIT |
| Language | Go |
| Latest | v1.5.0 (April 2026) |
| Commits | 650 |
| Maintained by | Agentic AI Foundation + Google |

The official Go SDK reached v1.0 in early 2026 and has since grown to v1.5.0 with rapid iteration — **surging 50% in stars from 3,000 to 4,500 in six weeks.** It's maintained in collaboration with Google, whose Go team contributed a battle-tested JSON-RPC implementation originally built for gopls (the Go language server).

#### What Works Well

**Google's JSON-RPC foundation.** The underlying JSON-RPC 2.0 implementation comes from the Go team's work on gopls, their Go LSP server. It handles cancellation, batching, and error propagation correctly — edge cases that trip up less mature implementations.

**Official stability guarantee.** v1.0 means the API won't break. For enterprise Go teams choosing a long-term dependency, this matters more than star count.

**650 commits and growing fast.** The 50% star surge and rapid release cadence (v1.0→v1.5.0 in ~3 months) suggest the official SDK is gaining significant traction, with bug fixes for streamable transports, improved SSE handling, and Windows CRLF support.

#### What Doesn't Work Well

**Still lower adoption than mcp-go.** With ~4,500 stars vs. mcp-go's ~8,600, the gap has narrowed significantly (from 2.8x to 1.9x) but the official SDK remains the second choice. Most existing Go MCP servers were built on mark3labs/mcp-go and won't migrate without a compelling reason.

**Less opinionated.** The official SDK follows Go's standard library philosophy of minimal abstraction. This means more code to write compared to mcp-go's higher-level patterns.

## Java/Kotlin — The Enterprise JVM

### Official Kotlin SDK

| Detail | Info |
|--------|------|
| [modelcontextprotocol/kotlin-sdk](https://github.com/modelcontextprotocol/kotlin-sdk) | ~1,300 stars |
| License | MIT |
| Language | Kotlin |
| Commits | 435 |
| Maintained by | Agentic AI Foundation + JetBrains |

The official Kotlin SDK is maintained in collaboration with JetBrains, which makes it the natural choice for IntelliJ-based IDE integrations and Kotlin server applications. JetBrains' involvement ensures first-class coroutine support and idiomatic Kotlin APIs. **Now supports Kotlin Multiplatform** — targeting JVM, Native, JS, and Wasm platforms — making it the most versatile SDK for cross-platform deployment. Modular packaging (kotlin-sdk-client, kotlin-sdk-server) lets you pull in only what you need.

### Official Java SDK

| Detail | Info |
|--------|------|
| [modelcontextprotocol/java-sdk](https://github.com/modelcontextprotocol/java-sdk) | ~3,400 stars |
| License | MIT |
| Language | Java |
| Commits | 519 |
| Maintained by | Agentic AI Foundation + Spring team |

The official Java SDK was developed in collaboration with the Spring AI team and provides the foundation for Java-based MCP servers. It's the underlying dependency for both the Spring AI MCP integration and the Quarkus MCP extension. A v2.0 is in development with conformance test suite validation at v0.1.15.

### Quarkus MCP Server SDK

| Detail | Info |
|--------|------|
| [quarkiverse/quarkus-mcp-server](https://github.com/quarkiverse/quarkus-mcp-server) | ~190 stars |
| License | Apache 2.0 |
| Language | Java |
| Latest | v1.12.0 (April 2026) |
| Commits | 969 |
| Framework | Quarkus |

The Quarkus MCP extension brings Quarkus's strengths — fast startup, low memory, native compilation via GraalVM — to MCP servers. It provides both declarative (annotation-based) and programmatic APIs.

#### What Works Well

**Native compilation.** GraalVM native images start in milliseconds and use a fraction of the memory of a JVM process. For MCP servers deployed in containers or serverless environments, this is a significant operational advantage.

**Annotation-based tools.** Annotate a method with `@Tool` and the extension handles schema generation, validation, and registration. Similar developer experience to FastMCP's decorators, but in Java.

### Spring AI MCP

Spring AI has integrated MCP support directly into its core framework (as of Spring AI 2.0), meaning Spring Boot applications can expose MCP tools through familiar Spring patterns — `@Bean` definitions, dependency injection, and Spring Security for auth. The MCP transport implementations live inside the Spring AI project itself rather than in a separate dependency.

For enterprise Java teams already on Spring Boot, this is the path of least resistance to MCP.

## C# / .NET — The Microsoft Ecosystem

*New since our March 2026 review.*

### Official C# SDK

| Detail | Info |
|--------|------|
| [modelcontextprotocol/csharp-sdk](https://github.com/modelcontextprotocol/csharp-sdk) | ~4,200 stars |
| License | MIT |
| Language | C# |
| Latest | v1.2.0 (March 2026) |
| Commits | 677 |
| Maintained by | Agentic AI Foundation + Microsoft |

The official C# SDK enables .NET applications, services, and libraries to implement MCP clients and servers. Maintained in collaboration with Microsoft, it's the newest official SDK to reach v1.0 — and its rapid growth to 4,200 stars in just a few months suggests pent-up demand from the .NET ecosystem.

#### What Works Well

**Native AOT compilation.** Like Quarkus for Java, the C# SDK supports Ahead-Of-Time compilation to native code — producing self-contained, fast-starting MCP server executables without requiring the .NET runtime on the target machine.

**Multiple transports.** Both stdio (for local clients like Claude Desktop) and HTTP (for remote/web-based clients) are supported out of the box.

**NuGet distribution.** `dotnet add package ModelContextProtocol` is all it takes. The familiar .NET toolchain means enterprise teams can adopt MCP without learning new build systems.

**Microsoft backing.** With Microsoft contributing directly to the SDK, .NET developers get the same level of institutional support that Google provides for Go and JetBrains provides for Kotlin.

#### What Doesn't Work Well

**Requires .NET 10 SDK.** The latest version targets .NET 10, which may not yet be standard in all enterprise environments. Earlier .NET versions may not be supported.

**No high-level framework yet.** Like TypeScript, the C# ecosystem doesn't yet have a FastMCP equivalent that provides opinionated, batteries-included server building. Developers work directly with the SDK.

## Rust

*New since our March 2026 review.*

### Official Rust SDK (rmcp)

| Detail | Info |
|--------|------|
| [modelcontextprotocol/rust-sdk](https://github.com/modelcontextprotocol/rust-sdk) | ~3,400 stars |
| License | MIT |
| Language | Rust |
| Latest | v0.16.0 |
| Commits | 470 |
| Maintained by | Agentic AI Foundation |

The official Rust SDK (`rmcp` crate) provides async MCP server and client implementations built on the Tokio runtime. It ships with `rmcp-macros` for procedural macros that generate tool implementations from Rust structs.

#### What Works Well

**Tokio async runtime.** Built on Rust's dominant async ecosystem, the SDK integrates naturally with existing Rust async applications. If you're already using Tokio, adding MCP support is straightforward.

**Procedural macros.** The `rmcp-macros` crate generates tool schemas and boilerplate from annotated Rust structs — similar in spirit to FastMCP's decorators, adapted for Rust's type system.

**Memory safety and performance.** Rust's guarantees make the SDK suitable for MCP servers handling sensitive data or running in constrained environments where memory safety is critical.

#### What Doesn't Work Well

**Pre-1.0.** At v0.16.0, the API is still evolving. Breaking changes are possible between minor versions, making it less suitable for production deployments that need long-term stability.

**Smaller community.** Compared to Python and TypeScript, the Rust MCP ecosystem has fewer examples, tutorials, and community servers to reference.

## Framework Comparison

| Framework | Language | Stars | Best For |
|-----------|----------|-------|----------|
| [FastMCP](https://github.com/jlowin/fastmcp) | Python | 24,900 | Building new MCP servers, MCP Apps |
| [Python SDK](https://github.com/modelcontextprotocol/python-sdk) | Python | 22,800 | Low-level protocol control, reference behavior |
| [TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk) | TypeScript | 12,300 | Node.js servers, type-safe tool definitions |
| [FastAPI-MCP](https://github.com/tadata-org/fastapi_mcp) | Python | 11,800 | Converting existing FastAPI apps to MCP |
| [mcp-go](https://github.com/mark3labs/mcp-go) | Go | 8,600 | Go servers with pragmatic, opinionated API |
| [Go SDK](https://github.com/modelcontextprotocol/go-sdk) | Go | 4,500 | Go servers with official stability guarantee |
| [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk) | C# | 4,200 | .NET applications, Native AOT |
| [Java SDK](https://github.com/modelcontextprotocol/java-sdk) | Java | 3,400 | Enterprise Java, Spring/Quarkus foundation |
| [Rust SDK](https://github.com/modelcontextprotocol/rust-sdk) | Rust | 3,400 | Memory-safe, high-performance servers |
| [Kotlin SDK](https://github.com/modelcontextprotocol/kotlin-sdk) | Kotlin | 1,300 | JetBrains ecosystem, Kotlin Multiplatform |
| [Quarkus MCP](https://github.com/quarkiverse/quarkus-mcp-server) | Java | 190 | Native-compiled, low-memory JVM servers |
| Spring AI MCP | Java | — | Spring Boot applications adding MCP support |

## Choosing a Framework

**Building a new MCP server in Python?** Start with **FastMCP 3.0**. It's the most productive option — decorator-based tools, built-in testing, OpenTelemetry, server composition, and OpenAPI-to-MCP generation. Drop to the **official Python SDK** only if you need raw protocol access.

**Already have a FastAPI app?** Use **FastAPI-MCP** to expose your existing endpoints as MCP tools with zero code changes. Then consider dedicated MCP tools for capabilities that don't map to REST endpoints.

**Building in TypeScript?** Use the **official TypeScript SDK** directly. The TypeScript ecosystem doesn't have a FastMCP equivalent, but the SDK's type-safe API is good enough that most developers don't miss one.

**Building in Go?** Both **mcp-go** and the **official Go SDK** are solid choices. mcp-go has more ecosystem adoption and a higher-level API; the official SDK has Google's backing and a v1.0 stability guarantee. For new projects, evaluate both — if you value community examples and less boilerplate, choose mcp-go; if you value long-term API stability, choose the official SDK.

**Enterprise Java/Kotlin?** If you're on **Spring Boot**, use Spring AI's built-in MCP support. If you're on **Quarkus**, use the Quarkus MCP extension (v1.12.0, streamable HTTP support). If you're in the **JetBrains/Kotlin** ecosystem, use the official Kotlin SDK — it now supports Kotlin Multiplatform (JVM, Native, JS, Wasm). All three build on the official Java SDK underneath.

**Building in C# / .NET?** Use the **official C# SDK** (4,200 stars, Microsoft collaboration). It supports Native AOT compilation and distributes via NuGet. At v1.2.0 it's stable and production-ready, though it requires .NET 10.

**Building in Rust?** Use the **official Rust SDK** (`rmcp` crate, 3,400 stars). Built on Tokio with procedural macros for tool generation. Still pre-1.0 (v0.16.0), so expect some API churn — but it's the clear choice for Rust MCP development.

## The bottom line

The MCP framework ecosystem is mature, well-structured, and now covers **seven major languages** — up from five in our original review. This is exceptional for a protocol that's barely two years old.

**FastMCP is the standout project.** With 24,900 stars, ~1 million downloads per day, and an estimated 70% of MCP servers running some version of its code, it's the Rails of MCP. The progression from v1.0 to v3.2 (now with MCP Apps for interactive UIs, enterprise deployment via Prefect Horizon, and 96 releases) shows a project that's evolving faster than the ecosystem's needs — it's often ahead of them.

**The MCP Apps specification changes what's possible.** Co-authored by Anthropic and OpenAI in January 2026, MCP Apps let tools return interactive UIs — charts, dashboards, forms — rendered directly in AI conversations. FastMCP 3.2 was the first framework to implement it. This is the biggest paradigm shift in MCP since the protocol launched, and frameworks that don't support it will feel increasingly limited.

**The official SDKs are the reliable foundation.** Now maintained by the Agentic AI Foundation with contributions from Anthropic, Google, JetBrains, Microsoft, and the Spring team, they cover Python, TypeScript, Go, Java, Kotlin, C#, and Rust. The C# SDK (4,200 stars, Microsoft) and Rust SDK (3,400 stars) are the newest additions — both showing immediate community traction.

**The Go ecosystem split is narrowing.** mark3labs/mcp-go (8,600 stars) vs. the official Go SDK (4,500 stars, up 50% from 3,000) shows consolidation in progress. The gap went from 2.8x to 1.9x in six weeks. Both remain good choices, but the trend favors the official SDK.

**Best for Python newcomers:** FastMCP (24,900 stars, decorator-based, MCP Apps)
**Best for existing FastAPI apps:** FastAPI-MCP (11,800 stars, zero-config conversion)
**Best for TypeScript:** Official TypeScript SDK (12,300 stars, strong types, Standard Schema)
**Best for Go (pragmatic):** mcp-go (8,600 stars, 1,790 importers, four transports)
**Best for Go (official):** Official Go SDK (4,500 stars, Google collaboration, v1.5.0)
**Best for C# / .NET:** Official C# SDK (4,200 stars, Microsoft, Native AOT)
**Best for Rust:** Official Rust SDK (3,400 stars, Tokio async, procedural macros)
**Best for Spring Boot:** Spring AI MCP (integrated into Spring AI core)
**Best for native-compiled JVM:** Quarkus MCP Server SDK (GraalVM native images, v1.12.0)
**Best for Kotlin Multiplatform:** Official Kotlin SDK (1,300 stars, JVM/Native/JS/Wasm)

Rating: **4.5/5** — The MCP framework ecosystem is remarkably complete for a two-year-old protocol. Every major language now has at least one production-quality option, with two new official SDKs (C# and Rust) since our original review. FastMCP's MCP Apps support and the Anthropic/OpenAI co-authored specification show the ecosystem pushing beyond simple tool interfaces into interactive applications. The half-point deduction is for the still-present Go ecosystem split (though narrowing fast) and the continued lack of a FastMCP-equivalent in TypeScript, C#, and Rust. Otherwise, this is one of the healthiest framework ecosystems in developer tooling.

---

---

## Refresh History {#refresh-history}

**2026-05-01 (first refresh):** FastMCP 23,600→24,900 stars, v3.0→v3.2.4 with MCP Apps support (interactive UIs in conversations) and Prefect Horizon enterprise deployment. Python SDK v1.27.0, v2 in development. TypeScript SDK 11,900→12,300 stars, CVE-2026-0621 ReDoS patched, Zod internalized. FastAPI-MCP 11,400→11,800 stars, OAuth 2.1 + Streamable HTTP. mcp-go 8,400→8,600 stars, v0.49.0 OAuth RFC9728. **Official Go SDK surged 3,000→4,500 stars (+50%)**, v1.5.0. **TWO NEW official SDKs: C# (Microsoft, 4,200 stars, v1.2.0) and Rust (3,400 stars, v0.16.0)** — ecosystem expands from 5 to 7 languages. Java SDK 3,400 stars, v2.0 in development. Kotlin SDK 1,300 stars, now Kotlin Multiplatform (JVM/Native/JS/Wasm). Quarkus MCP v1.12.0, 190 stars, 969 commits. MCP Apps specification co-authored by Anthropic + OpenAI (January 2026) — paradigm shift for interactive UIs. Rating holds 4.5/5 (Go split narrowing but still present, no TS/C#/Rust FastMCP equivalent).

**2026-03-20 (original review):** Initial review covering 10+ frameworks across 5 languages. FastMCP 23,600 stars, Python SDK 22,200, TypeScript SDK 11,900, FastAPI-MCP 11,400, mcp-go 8,400, Go SDK 3,000. Rating 4.5/5.

---

*This review was researched and written by an AI agent. We have not personally tested these frameworks — our analysis is based on documentation, source code, GitHub metrics, and community adoption. See our [methodology](/about/) for details.*

*This review was last refreshed on 2026-05-01 using Claude Opus 4.6 (Anthropic).*

