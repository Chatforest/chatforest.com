# MCP Server Frameworks & SDKs — FastMCP, Official SDKs, and the Tools That Power Every MCP Server

> MCP server frameworks and SDKs reviewed: FastMCP (27,200+ stars, millions of downloads/day), Rust SDK reached v3.1.2, mcp-go v0.58.0 (v1.0 beta), Go SDK v1.7.0 with full 2026-07-28 spec support


Every MCP server is built on something. Behind the 5,000+ servers in the ecosystem, a surprisingly small number of frameworks and SDKs do the heavy lifting — handling JSON-RPC transport, tool schema generation, authentication, and the protocol handshake that makes MCP work.

This review covers the tools developers use to **build** MCP servers: official SDKs maintained by the [Agentic AI Foundation](https://github.com/modelcontextprotocol) (donated by Anthropic in late 2025), and the third-party frameworks that add higher-level abstractions on top. The ecosystem now spans **seven languages** — **Python**, **TypeScript**, **Go**, **Java**, **Kotlin**, **C#**, and **Rust** — with Python dominating adoption by a wide margin. Since our [original review in March 2026](#refresh-history), two new official SDKs launched (C# with Microsoft, Rust), the official Go and Python SDKs both shipped support for the [2026-07-28 protocol revision](https://github.com/modelcontextprotocol/go-sdk/releases/tag/v1.7.0), and the MCP Apps specification introduced interactive UI capabilities that frameworks are racing to support.

The headline: **FastMCP is the most important project in the MCP ecosystem that most users never see.** With [27,200+ stars](https://github.com/PrefectHQ/fastmcp), [millions of downloads per day](https://pypistats.org/packages/fastmcp) (pypistats showed ~4.2M on the day checked, 2026-08-15; ~3.4M/day 7-day average), and [an estimated 70% of all MCP servers running some version of it](https://github.com/PrefectHQ/fastmcp) (per FastMCP's own README), FastMCP is to MCP what Express is to Node.js — the framework that made the protocol accessible. Its MCP Apps support lets tools return interactive UIs — charts, dashboards, forms — rendered directly in conversations. The official SDKs provide the foundation, but FastMCP made it easy.

**Category:** [Developer Tools](/categories/developer-tools/)

## Python — The Dominant Ecosystem

Python has the widest selection of MCP frameworks and the highest adoption. Two projects dominate.

### FastMCP (PrefectHQ)

| Detail | Info |
|--------|------|
| [PrefectHQ/fastmcp](https://github.com/PrefectHQ/fastmcp) | [~27,200 stars](https://github.com/PrefectHQ/fastmcp) |
| License | Apache 2.0 |
| Language | Python |
| Latest | [v3.4.7](https://github.com/PrefectHQ/fastmcp/releases) (stable, August 2026); v4.0.0 in beta (v4.0.0b3) |
| Downloads | [Millions/day](https://pypistats.org/packages/fastmcp) (~4.2M on the day checked; ~3.4M/day 7-day average) |

FastMCP is the most popular MCP framework in any language. Created by [Jeremiah Lowin (CEO of Prefect)](https://jlowin.dev/about), it was the first framework to make building MCP servers genuinely simple. FastMCP 1.0 was so well-designed that it was incorporated directly into the official MCP Python SDK in 2024 — the standalone project continued evolving independently, and the repo has since been transferred from the `jlowin` GitHub account to the `PrefectHQ` organization.

#### What Works Well

**Decorator-based API eliminates boilerplate.** Define a function, add `@mcp.tool()`, and FastMCP handles schema generation from type hints, docstring parsing, input validation, and transport setup. A working MCP server is literally five lines of code.

**MCP Apps support — interactive UIs in conversations.** The "Show Don't Tool" release lets tools return charts, dashboards, forms, and maps rendered directly inside the AI chat. `FastMCPApp` is a new provider class that separates LLM-visible tools (`@app.ui()`) from backend tools the UI calls (`@app.tool()`). This builds on the [MCP Apps specification](https://blog.modelcontextprotocol.io/posts/2026-01-26-mcp-apps/), announced January 26, 2026 with Anthropic's David Soria Parra credited as MCP co-creator and OpenAI's Nick Cooper credited for the companion OpenAI Apps SDK.

**Rapid iteration continues.** Since reaching v3.0 (component versioning, granular authorization, OpenTelemetry instrumentation, multiple provider types) and v3.2 (MCP Apps), the project has kept shipping — [v3.4.7 is the current stable release, with a v4.0.0 beta already in progress](https://github.com/PrefectHQ/fastmcp/releases).

**Prefect Horizon for enterprise deployment.** FastMCP now integrates with [Prefect Horizon](https://www.prefect.io/horizon) for production deployment with OAuth 2.1 + RBAC, tool-level access control, and audit trails across MCP stacks.

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
| [modelcontextprotocol/python-sdk](https://github.com/modelcontextprotocol/python-sdk) | [~24,000 stars](https://github.com/modelcontextprotocol/python-sdk) |
| License | MIT |
| Language | Python |
| Latest | [v2.0.0](https://github.com/modelcontextprotocol/python-sdk/releases/tag/v2.0.0) (July 2026, GA); v1.29.0 is the final v1.x maintenance release |
| Maintained by | Agentic AI Foundation |

The official Python SDK is the reference implementation of the MCP protocol. It provides both low-level protocol handling and a high-level server API (which incorporates FastMCP 1.0's design).

#### What Works Well

**Two API levels.** The low-level API gives you complete control over request/response handling — useful if you're building a framework or need custom protocol behavior. The high-level API (inspired by FastMCP) provides the decorator pattern most developers want.

**Protocol completeness.** As the reference implementation, it supports every MCP feature: tools, resources, prompts, sampling, roots, logging, notifications, and all transport types (stdio, SSE, Streamable HTTP).

**Battle-tested.** Anthropic's own servers (filesystem, memory, sequential-thinking) are built on this SDK. If something works in the spec, it works in the Python SDK.

#### What Doesn't Work Well

**Less opinionated than FastMCP.** The SDK gives you building blocks; FastMCP gives you a framework. For most developers building production servers, FastMCP 3.x is the better starting point unless you need fine-grained protocol control.

**v2 has shipped.** [v2.0.0 reached GA on July 28, 2026](https://github.com/modelcontextprotocol/python-sdk/releases/tag/v2.0.0), supporting the 2026-07-28 protocol revision; v1.29.0 shipped the same day as the final v1.x release, now in maintenance mode for bug fixes and security updates. Projects that haven't migrated should plan for it — v2 is now what PyPI serves as `mcp`'s "latest."

**Documentation favors the high-level API.** If you want to use the low-level API for custom protocol handling, you'll be reading source code more than docs.

### FastAPI-MCP

| Detail | Info |
|--------|------|
| [tadata-org/fastapi_mcp](https://github.com/tadata-org/fastapi_mcp) | [~12,000 stars](https://github.com/tadata-org/fastapi_mcp) |
| License | MIT |
| Language | Python |
| Latest | [v0.4.0](https://github.com/tadata-org/fastapi_mcp/releases/tag/v0.4.0) (July 2025 — no new release since; the project appears dormant) |
| Approach | Auto-converts FastAPI endpoints to MCP tools |

FastAPI-MCP takes a fundamentally different approach: instead of building an MCP server from scratch, it **wraps an existing FastAPI application** and automatically exposes its endpoints as MCP tools. Zero configuration required — import, mount, done.

#### What Works Well

**Zero-config conversion.** If you already have a FastAPI app, adding MCP support is three lines of code. Every endpoint becomes a tool. Request/response schemas are generated from your existing Pydantic models.

**Native FastAPI dependencies.** Authentication, authorization, and middleware work exactly as they do in your FastAPI app — via `Depends()`. No separate auth system for MCP.

**Bidirectional.** Your FastAPI app continues serving HTTP clients normally while simultaneously acting as an MCP server. One codebase, two protocols.

#### What Doesn't Work Well

**FastAPI-only.** If you're building an MCP server that isn't backed by a REST API, this tool doesn't apply. It's a bridge, not a framework.

**Tool granularity tied to endpoint granularity.** If your FastAPI endpoints are coarse-grained (one endpoint does many things), the generated MCP tools will be similarly coarse. MCP tools work best when they're focused and specific.

**No release since July 2025.** [v0.4.0](https://github.com/tadata-org/fastapi_mcp/releases/tag/v0.4.0) is still the latest tag as of this update. The GitHub repo remains active in the sense that stars keep climbing, but the lack of a release in over a year is worth weighing against the two more actively maintained Python options above.

## TypeScript

### Official TypeScript SDK

| Detail | Info |
|--------|------|
| [modelcontextprotocol/typescript-sdk](https://github.com/modelcontextprotocol/typescript-sdk) | [~13,200 stars](https://github.com/modelcontextprotocol/typescript-sdk) |
| License | MIT |
| Language | TypeScript |
| Latest | [v1.30.0](https://www.npmjs.com/package/@modelcontextprotocol/sdk) (July 2026, core package) |
| Maintained by | Agentic AI Foundation |

The official TypeScript SDK is the second reference implementation and the foundation for most Node.js MCP servers. It provides strongly-typed developer ergonomics with both stdio and HTTP+SSE transports.

#### What Works Well

**Type safety throughout.** TypeScript's type system maps naturally to MCP's JSON Schema-based tool definitions. Tool inputs, outputs, and error types are checked at compile time.

**Mature and stable.** The TypeScript SDK was one of the first two SDKs (alongside Python) and has been battle-tested across Anthropic's reference servers and hundreds of community projects.

**First-class Zod support.** Schema validation via Zod integrates cleanly, letting you define tool parameters with runtime validation that doubles as compile-time type checking.

#### What Doesn't Work Well

**[CVE-2026-0621](https://nvd.nist.gov/vuln/detail/CVE-2026-0621) ReDoS vulnerability patched.** A regular expression denial of service vulnerability (CVSS 7.5 HIGH) in UriTemplate regex patterns was discovered and fixed. A reminder that even foundational SDKs need security attention.

**Zod internalized via Standard Schema.** Zod was moved from a peer dependency to a direct internal dependency after Standard Schema support landed, simplifying installation for new users.

**No equivalent to FastMCP.** The TypeScript ecosystem lacks a dominant high-level framework like Python's FastMCP. Several projects (EasyMCP, mcp-framework) try to fill this gap, but none have achieved similar adoption. Most TypeScript MCP developers work directly with the SDK.

**v2 transition, unevenly rolled out.** The core [`@modelcontextprotocol/sdk`](https://www.npmjs.com/package/@modelcontextprotocol/sdk) package is still on the v1.x line (v1.30.0), while companion packages — `@modelcontextprotocol/server`, `@modelcontextprotocol/node`, `@modelcontextprotocol/hono`, `@modelcontextprotocol/fastify` — [jumped to 2.0.0](https://github.com/modelcontextprotocol/typescript-sdk/releases) with 2026-07-28 spec support. This split-version state creates real uncertainty about which package to target for new projects until the core SDK itself moves to v2.

## Go

### mcp-go (mark3labs)

| Detail | Info |
|--------|------|
| [mark3labs/mcp-go](https://github.com/mark3labs/mcp-go) | [~9,000 stars](https://github.com/mark3labs/mcp-go) |
| License | MIT |
| Language | Go |
| Latest | [v0.58.0](https://github.com/mark3labs/mcp-go/releases) (stable); [v1.0.0-beta.1](https://github.com/mark3labs/mcp-go/releases) previews the 2026-07-28 spec |
| Importers | Widely imported — see [pkg.go.dev](https://pkg.go.dev/github.com/mark3labs/mcp-go?tab=importedby) for the current list (we could not confirm a precise count) |
| Transport | stdio, Streamable HTTP, SSE, in-process |

mcp-go is the most popular community Go SDK and predates the official Go SDK. It's more opinionated than the official SDK, with a higher-level API that gets you to a working server faster.

#### What Works Well

**Four transports out of the box.** stdio, Streamable HTTP, SSE, and in-process — the widest transport support of any single Go MCP library.

**Task-augmented tools for async operations.** Task-augmented tools — asynchronous tool execution that returns immediately with a task ID instead of blocking — shipped in v0.50.0 and remain in the current v0.58.0. Three modes: `TaskSupportForbidden` (default sync), `TaskSupportOptional` (caller chooses), and `TaskSupportRequired` (always async). Essential for long-running operations that would otherwise time out.

**Heading toward v1.0.** [v1.0.0-beta.1](https://github.com/mark3labs/mcp-go/releases) adds support for the 2026-07-28 MCP specification — a sign the project considers itself stable enough for a 1.0 milestone.

**Significant ecosystem adoption.** A large share of community Go MCP servers use this library; community knowledge, examples, and Stack Overflow answers are abundant.

**Pragmatic API.** Less boilerplate than the official Go SDK. Function-based tool registration with struct-based configuration follows established Go patterns.

#### What Doesn't Work Well

**Competes with the official Go SDK.** [The official Go SDK has grown to ~5,000 stars](https://github.com/modelcontextprotocol/go-sdk) against mcp-go's ~9,000 — a ratio of roughly 1.8x, continuing to narrow from the 2.8x gap at our original review. mark3labs/mcp-go still leads in adoption and ecosystem examples, but the official SDK's momentum suggests gradual consolidation.

### Official Go SDK

| Detail | Info |
|--------|------|
| [modelcontextprotocol/go-sdk](https://github.com/modelcontextprotocol/go-sdk) | [~5,000 stars](https://github.com/modelcontextprotocol/go-sdk) |
| License | MIT |
| Language | Go |
| Latest | [v1.7.0](https://github.com/modelcontextprotocol/go-sdk/releases/tag/v1.7.0) (stable, July 28, 2026) |
| Maintained by | Agentic AI Foundation + Google |

The official Go SDK reached v1.0 in early 2026 and has since grown to v1.7.0 with rapid iteration, roughly doubling its star count over the course of 2026. It's maintained in collaboration with Google, whose Go team contributed a battle-tested JSON-RPC implementation originally built for gopls (the Go language server).

#### What Works Well

**Google's JSON-RPC foundation.** The underlying JSON-RPC 2.0 implementation comes from the Go team's work on gopls, their Go LSP server. It handles cancellation, batching, and error propagation correctly — edge cases that trip up less mature implementations.

**First to ship the newest MCP spec.** [v1.7.0 (July 28, 2026) ships full support for the 2026-07-28 specification revision](https://github.com/modelcontextprotocol/go-sdk/releases/tag/v1.7.0) — a stateless model, new `server/discover` RPC, and multi-round-trip requests — after previewing OAuth client-credentials grant support and HTTP header standardization in the v1.6.0 line. The Go SDK was again among the first official SDKs to ship the new spec.

**Official stability guarantee.** v1.0 means the API won't break within the major version. For enterprise Go teams choosing a long-term dependency, this matters more than star count.

**Fast release cadence.** Six minor/patch releases between v1.5.0 (April 2026) and v1.7.0 (July 2026) — including client-side OAuth stabilization and Enterprise Managed Authorization support in v1.5.0/v1.6.0 — suggest the official SDK is gaining significant traction.

#### What Doesn't Work Well

**Still lower adoption than mcp-go.** With [~5,000 stars](https://github.com/modelcontextprotocol/go-sdk) vs. [mcp-go's ~9,000](https://github.com/mark3labs/mcp-go), the gap has narrowed further (from 2.8x at launch to roughly 1.8x now) but the official SDK remains the second choice. Most existing Go MCP servers were built on mark3labs/mcp-go and won't migrate without a compelling reason.

**Less opinionated.** The official SDK follows Go's standard library philosophy of minimal abstraction. This means more code to write compared to mcp-go's higher-level patterns.

## Java/Kotlin — The Enterprise JVM

### Official Kotlin SDK

| Detail | Info |
|--------|------|
| [modelcontextprotocol/kotlin-sdk](https://github.com/modelcontextprotocol/kotlin-sdk) | [~1,400 stars](https://github.com/modelcontextprotocol/kotlin-sdk) |
| License | MIT |
| Language | Kotlin |
| Latest | [v0.15.0](https://github.com/modelcontextprotocol/kotlin-sdk/releases/tag/0.15.0) (July 2026) |
| Maintained by | Agentic AI Foundation + JetBrains |

The official Kotlin SDK is maintained in collaboration with JetBrains, which makes it the natural choice for IntelliJ-based IDE integrations and Kotlin server applications. JetBrains' involvement ensures first-class coroutine support and idiomatic Kotlin APIs. **Supports Kotlin Multiplatform** — targeting JVM, Native, JS, and Wasm platforms — making it one of the more versatile SDKs for cross-platform deployment. Modular packaging (kotlin-sdk-client, kotlin-sdk-server) lets you pull in only what you need. [Sampling-with-tools (SEP-1577)](https://github.com/modelcontextprotocol/kotlin-sdk/releases) landed in v0.12.0 (April 2026); three further releases since (v0.13.0–v0.15.0) have continued iterating toward newer spec support.

### Official Java SDK

| Detail | Info |
|--------|------|
| [modelcontextprotocol/java-sdk](https://github.com/modelcontextprotocol/java-sdk) | [~3,700 stars](https://github.com/modelcontextprotocol/java-sdk) |
| License | MIT |
| Language | Java |
| Latest | [v2.0.0](https://github.com/modelcontextprotocol/java-sdk/releases/tag/v2.0.0) (June 2026) |
| Maintained by | Agentic AI Foundation + Spring team |

The official Java SDK was developed in collaboration with the Spring AI team and provides the foundation for Java-based MCP servers. It's the underlying dependency for both the Spring AI MCP integration and the Quarkus MCP extension. It reached v1.0.0 GA in February 2026, then a v1.1.x line added resource-subscription support and HTTP 405 error handling, before [v2.0.0 shipped June 11, 2026](https://github.com/modelcontextprotocol/java-sdk/releases/tag/v2.0.0). Teams on the v1.x line should check the v2 migration notes before upgrading, as with the other SDKs' major bumps this year.

### Quarkus MCP Server SDK

| Detail | Info |
|--------|------|
| [quarkiverse/quarkus-mcp-server](https://github.com/quarkiverse/quarkus-mcp-server) | [~200 stars](https://github.com/quarkiverse/quarkus-mcp-server) |
| License | Apache 2.0 |
| Language | Java |
| Latest | [v1.13.1](https://github.com/quarkiverse/quarkus-mcp-server/releases) (stable, July 2026); a 2.0.0 line is in release-candidate testing |
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
| [modelcontextprotocol/csharp-sdk](https://github.com/modelcontextprotocol/csharp-sdk) | [~4,500 stars](https://github.com/modelcontextprotocol/csharp-sdk) |
| License | Apache 2.0 |
| Language | C# |
| Latest | [v2.2.0](https://github.com/modelcontextprotocol/csharp-sdk/releases) (August 2026); [v2.0.0](https://devblogs.microsoft.com/dotnet/announcing-v20-of-the-official-mcp-csharp-sdk/) shipped July 28, 2026 |
| Maintained by | Agentic AI Foundation + Microsoft |

The official C# SDK enables .NET applications, services, and libraries to implement MCP clients and servers. Maintained in collaboration with Microsoft, it reached v1.0 in early 2026 and continued to a major [v2.0 release announced on the .NET Blog](https://devblogs.microsoft.com/dotnet/announcing-v20-of-the-official-mcp-csharp-sdk/) — rapid growth suggesting pent-up demand from the .NET ecosystem.

#### What Works Well

**Native AOT compilation.** Like Quarkus for Java, the C# SDK supports Ahead-Of-Time compilation to native code — producing self-contained, fast-starting MCP server executables without requiring the .NET runtime on the target machine.

**Modular NuGet packages.** Separate packages for different needs: `ModelContextProtocol.Core` (minimal dependencies, client/low-level server), `ModelContextProtocol` (hosting + dependency injection), and `ModelContextProtocol.AspNetCore` (HTTP-based servers). v2.0 also split Tasks support into its own `ModelContextProtocol.Extensions.Tasks` package. This lets teams pull in only what they need.

**Streamable HTTP is now the default, stateless.** v2.0 makes `HttpServerTransportOptions.Stateless` default to `true` and moves clients to a discovery-first `server/discover` handshake before falling back to legacy `initialize` — [a deliberate, breaking push toward the modern transport model](https://devblogs.microsoft.com/dotnet/announcing-v20-of-the-official-mcp-csharp-sdk/).

**Microsoft backing.** With Microsoft contributing directly to the SDK, .NET developers get the same level of institutional support that Google provides for Go and JetBrains provides for Kotlin.

#### What Doesn't Work Well

**v2.0 ships real breaking changes.** Roots, Sampling, and Logging APIs are deprecated with warnings; OAuth callback/issuer validation and PKCE enforcement got stricter; tool deserialization now requires `inputSchema`. Teams upgrading from v1.x should read the [migration notes](https://devblogs.microsoft.com/dotnet/announcing-v20-of-the-official-mcp-csharp-sdk/) closely rather than bumping the version blind. (Broader framework support than before: v2.0 packages target net8.0, net9.0, net10.0, and netstandard2.0 — not .NET 10 exclusively.)

**No high-level framework yet.** Like TypeScript, the C# ecosystem doesn't yet have a FastMCP equivalent that provides opinionated, batteries-included server building. Developers work directly with the SDK.

## Rust

*New since our March 2026 review.*

### Official Rust SDK (rmcp)

| Detail | Info |
|--------|------|
| [modelcontextprotocol/rust-sdk](https://github.com/modelcontextprotocol/rust-sdk) | [~3,800 stars](https://github.com/modelcontextprotocol/rust-sdk) |
| License | MIT |
| Language | Rust |
| Latest | [v3.1.2](https://crates.io/crates/rmcp) (August 7, 2026) |
| Maintained by | Agentic AI Foundation |

The official Rust SDK (`rmcp` crate) provides async MCP server and client implementations built on the Tokio runtime. It ships with `rmcp-macros` for procedural macros that generate tool implementations from Rust structs. It reached v1.0.0 on March 3, 2026 and has continued rapid major-version iteration since, [now at v3.1.2 on crates.io](https://crates.io/crates/rmcp) — one of the fastest-moving SDKs in the MCP ecosystem by release count.

#### What Works Well

**Rapid, sustained iteration.** From v1.0.0 (March 3, 2026) to v1.5.0 in six weeks, and on to [v3.1.2 by August 2026](https://crates.io/crates/rmcp), the SDK has kept shipping major and minor versions steadily rather than stalling after its initial stabilization. A migration guide is available for the v0.x→v1.x transition; teams tracking `rmcp` closely should expect to revisit breaking changes across major bumps.

**Tokio async runtime.** Built on Rust's dominant async ecosystem, the SDK integrates naturally with existing Rust async applications. If you're already using Tokio, adding MCP support is straightforward.

**Procedural macros.** The `rmcp-macros` crate generates tool schemas and boilerplate from annotated Rust structs — similar in spirit to FastMCP's decorators, adapted for Rust's type system.

**Memory safety and performance.** Rust's guarantees make the SDK suitable for MCP servers handling sensitive data or running in constrained environments where memory safety is critical.

#### What Doesn't Work Well

**Smaller community.** Compared to Python and TypeScript, the Rust MCP ecosystem has fewer examples, tutorials, and community servers to reference. But the sustained release cadence suggests growing adoption.

**Fast major-version churn.** Three major version bumps (v1→v2→v3) within months of reaching v1.0 means less API stability than the "reached v1.0, now stable" framing of our last refresh implied. Pin versions carefully and read changelogs before upgrading.

## Framework Comparison

| Framework | Language | Stars | Best For |
|-----------|----------|-------|----------|
| [FastMCP](https://github.com/PrefectHQ/fastmcp) | Python | 27,200 | Building new MCP servers, MCP Apps |
| [Python SDK](https://github.com/modelcontextprotocol/python-sdk) | Python | 24,000 | Low-level protocol control, reference behavior |
| [TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk) | TypeScript | 13,200 | Node.js servers, type-safe tool definitions |
| [FastAPI-MCP](https://github.com/tadata-org/fastapi_mcp) | Python | 12,000 | Converting existing FastAPI apps to MCP |
| [mcp-go](https://github.com/mark3labs/mcp-go) | Go | 9,000 | Go servers with pragmatic, opinionated API |
| [Go SDK](https://github.com/modelcontextprotocol/go-sdk) | Go | 5,000 | Go servers with official stability guarantee |
| [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk) | C# | 4,500 | .NET applications, Native AOT |
| [Java SDK](https://github.com/modelcontextprotocol/java-sdk) | Java | 3,700 | Enterprise Java, Spring/Quarkus foundation |
| [Rust SDK](https://github.com/modelcontextprotocol/rust-sdk) | Rust | 3,800 | Memory-safe, high-performance servers |
| [Kotlin SDK](https://github.com/modelcontextprotocol/kotlin-sdk) | Kotlin | 1,400 | JetBrains ecosystem, Kotlin Multiplatform |
| [Quarkus MCP](https://github.com/quarkiverse/quarkus-mcp-server) | Java | 200 | Native-compiled, low-memory JVM servers |
| Spring AI MCP | Java | — | Spring Boot applications adding MCP support |

## Choosing a Framework

**Building a new MCP server in Python?** Start with **FastMCP 3.0**. It's the most productive option — decorator-based tools, built-in testing, OpenTelemetry, server composition, and OpenAPI-to-MCP generation. Drop to the **official Python SDK** only if you need raw protocol access.

**Already have a FastAPI app?** Use **FastAPI-MCP** to expose your existing endpoints as MCP tools with zero code changes. Then consider dedicated MCP tools for capabilities that don't map to REST endpoints.

**Building in TypeScript?** Use the **official TypeScript SDK** directly. The TypeScript ecosystem doesn't have a FastMCP equivalent, but the SDK's type-safe API is good enough that most developers don't miss one.

**Building in Go?** Both **mcp-go** and the **official Go SDK** are solid choices. mcp-go has more ecosystem adoption and a higher-level API; the official SDK has Google's backing and a v1.0 stability guarantee. For new projects, evaluate both — if you value community examples and less boilerplate, choose mcp-go; if you value long-term API stability, choose the official SDK.

**Enterprise Java/Kotlin?** If you're on **Spring Boot**, use Spring AI's built-in MCP support. If you're on **Quarkus**, use the Quarkus MCP extension (v1.13.1, streamable HTTP support). If you're in the **JetBrains/Kotlin** ecosystem, use the official Kotlin SDK — it supports Kotlin Multiplatform (JVM, Native, JS, Wasm). All three build on the official Java SDK underneath.

**Building in C# / .NET?** Use the **official C# SDK** (~4,500 stars, Microsoft collaboration). It supports Native AOT compilation and distributes via NuGet. At v2.2.0 it's stable and production-ready, targeting net8.0, net9.0, net10.0, and netstandard2.0.

**Building in Rust?** Use the **official Rust SDK** (`rmcp` crate, ~3,800 stars, v3.1.2). Built on Tokio with procedural macros for tool generation. Iterating quickly since hitting 1.0 in March 2026 — check the changelog carefully across major version bumps.

## The bottom line

The MCP framework ecosystem is mature, well-structured, and now covers **seven major languages** — up from five in our original review. This is exceptional for a protocol that's barely two years old.

**FastMCP is the standout project.** With [~27,200 stars](https://github.com/PrefectHQ/fastmcp), [millions of downloads per day](https://pypistats.org/packages/fastmcp), and [an estimated 70% of MCP servers running some version of its code](https://github.com/PrefectHQ/fastmcp) (per FastMCP's own README), it's the Rails of MCP. The progression from v1.0 through v3.4.7 (now with MCP Apps for interactive UIs, enterprise deployment via [Prefect Horizon](https://www.prefect.io/horizon), and a v4.0 beta already underway) shows a project that's evolving faster than the ecosystem's needs — it's often ahead of them.

**The MCP Apps specification changes what's possible.** [Announced January 26, 2026](https://blog.modelcontextprotocol.io/posts/2026-01-26-mcp-apps/) with Anthropic's David Soria Parra (MCP co-creator) and OpenAI's Nick Cooper (OpenAI Apps SDK) both credited for the collaboration, MCP Apps let tools return interactive UIs — charts, dashboards, forms — rendered directly in AI conversations. FastMCP was among the first frameworks to implement it. This is one of the biggest paradigm shifts in MCP since the protocol launched, and frameworks that don't support it will feel increasingly limited.

**The official SDKs are the reliable foundation.** Now maintained by the Agentic AI Foundation with contributions from Anthropic, Google, JetBrains, Microsoft, and the Spring team, they cover Python, TypeScript, Go, Java, Kotlin, C#, and Rust. The C# SDK (~4,500 stars, Microsoft) and Rust SDK (~3,800 stars) are the newest additions — both showing immediate community traction, and both have already shipped major (2.0/3.0-line) releases.

**The Go ecosystem split is narrowing.** [mark3labs/mcp-go](https://github.com/mark3labs/mcp-go) (~9,000 stars, v0.58.0 / v1.0.0-beta.1) vs. [the official Go SDK](https://github.com/modelcontextprotocol/go-sdk) (~5,000 stars, v1.7.0 with full 2026-07-28 spec support) shows consolidation in progress. The gap has gone from 2.8x at launch to roughly 1.8x now. Both remain good choices — mcp-go adds higher-level features (task tools, input validation) and is closing in on its own 1.0, while the official SDK continues to lead on spec compliance.

**The Rust SDK's iteration has stayed fast.** From v1.0.0 (March 3, 2026) through v1.5.0 in six weeks to [v3.1.2 by August 2026](https://crates.io/crates/rmcp) — three major version lines in under six months. This addresses the "unstable pre-1.0" concern from our original review, though the pace of major bumps since 1.0 is itself worth flagging for teams that value API stability over new features.

**The newest MCP spec has already shipped.** The [2026-07-28 specification revision](https://github.com/modelcontextprotocol/go-sdk/releases/tag/v1.7.0) is now supported by the official Go SDK (v1.7.0) and Python SDK (v2.0.0), with the TypeScript SDK's companion packages also on board. SDKs that got ahead of it early — as Go did with its pre-release previews — shipped the update fastest.

**Best for Python newcomers:** FastMCP (~27,200 stars, millions of downloads/day, MCP Apps)
**Best for existing FastAPI apps:** FastAPI-MCP (~12,000 stars, zero-config conversion, but no release since July 2025)
**Best for TypeScript:** Official TypeScript SDK (~13,200 stars, strong types, Standard Schema)
**Best for Go (pragmatic):** mcp-go (~9,000 stars, task-augmented tools, four transports, v1.0 beta)
**Best for Go (official):** Official Go SDK (~5,000 stars, Google collaboration, v1.7.0)
**Best for C# / .NET:** Official C# SDK (~4,500 stars, Microsoft, Native AOT, modular NuGet, v2.2.0)
**Best for Rust:** Official Rust SDK (~3,800 stars, v3.1.2, Tokio async)
**Best for Spring Boot:** Spring AI MCP (integrated into Spring AI core)
**Best for native-compiled JVM:** Quarkus MCP Server SDK (GraalVM native images, v1.13.1)
**Best for Kotlin Multiplatform:** Official Kotlin SDK (~1,400 stars, v0.15.0, sampling-with-tools)

Rating: **4.5/5** — The MCP framework ecosystem is remarkably complete for a two-year-old protocol. Every major language now has at least one production-quality option, and the official SDKs are shipping the newest spec revision quickly. FastMCP's continued growth (~27,200 stars, millions of downloads/day) shows sustained ecosystem adoption. The half-point deduction is for the still-present Go ecosystem split (though narrowing, and both options are now excellent), the continued lack of a FastMCP-equivalent in TypeScript, C#, and Rust, and — new since our last refresh — the fast major-version churn in the Rust SDK and the apparent dormancy of FastAPI-MCP. Otherwise, this is one of the healthiest framework ecosystems in developer tooling.

---

---

## Refresh History {#refresh-history}

**2026-08-15 (citation and staleness audit):** Verified every repo, version, and star count live against GitHub, PyPI, npm, crates.io, and Maven/NuGet sources. Nearly every SDK moved a major or minor version since the 2026-05-01 refresh: FastMCP moved from the `jlowin` to `PrefectHQ` GitHub org, ~24,900→~27,200 stars, v3.2.4→v3.4.7 stable (v4.0.0 beta in progress); downloads corrected to a consistent, cited pypistats figure (resolves an internal inconsistency where the page previously cited both ~3.1M/day and ~1.9M/day for the same period). Python SDK shipped v2.0.0 GA (July 28, 2026); v1.29.0 is now the final v1.x release. TypeScript SDK core package at v1.30.0; companion packages (server, node, hono, fastify) jumped to 2.0.0. mcp-go reached v0.58.0 and previewed v1.0.0-beta.1. Official Go SDK shipped v1.7.0 with full 2026-07-28 spec support. Java SDK reached v2.0.0 GA. Kotlin SDK reached v0.15.0. Quarkus MCP stable line at v1.13.1, with a 2.0.0 release-candidate in testing. C# SDK jumped to v2.2.0 (v2.0.0 GA July 28, 2026) — corrected the ".NET 10 required" claim, since v2.0 packages actually broadened support to net8.0/9.0/10.0/netstandard2.0. Rust SDK (`rmcp`) jumped from v1.5.0 to v3.1.2 — flagged as fast major-version churn rather than the "now stable" framing used previously. FastAPI-MCP has not released since July 2025 — flagged as possibly dormant. Added missing inline citations for the "70% of MCP servers" claim (FastMCP's own README) and the Jeremiah Lowin/Prefect CEO attribution (switched to his own bio page as a more precise primary source). CVE-2026-0621 details re-verified against NVD and remain accurate as stated. Rating holds 4.5/5.

**2026-05-01 (second refresh):** FastMCP downloads nearly doubled ~1M→~1.9M/day (27M/week, 74.6M/month), still v3.2.4, 24,900 stars. **Rust SDK CORRECTION: v0.16.0→v1.5.0** — reached v1.0.0 on March 3, iterated to v1.5.0 in six weeks (six releases), now stable with 2025-11-25 protocol support. Previous review incorrectly listed v0.16.0. mcp-go 8,600→8,700 stars, v0.49.0→v0.50.0 with task-augmented tools (async execution) and input schema validation (SEP-1303). Go SDK v1.6.0-pre.1 previews 2026-06-30 spec features (OAuth client credentials, HTTP header standardization). Java SDK v1.1.2 (v1.0.0 GA February, v1.1.0 resource subscriptions March). Kotlin SDK v0.12.0 adds sampling-with-tools (SEP-1577). C# SDK v1.2.0 SSE disabled by default (Streamable HTTP migration), modular NuGet packages. Quarkus v1.12.0 transport hints. Next MCP spec revision tentatively June 2026. Rating holds 4.5/5.

**2026-05-01 (first refresh):** FastMCP 23,600→24,900 stars, v3.0→v3.2.4 with MCP Apps support (interactive UIs in conversations) and Prefect Horizon enterprise deployment. Python SDK v1.27.0, v2 in development. TypeScript SDK 11,900→12,300 stars, CVE-2026-0621 ReDoS patched, Zod internalized. FastAPI-MCP 11,400→11,800 stars, OAuth 2.1 + Streamable HTTP. mcp-go 8,400→8,600 stars, v0.49.0 OAuth RFC9728. **Official Go SDK surged 3,000→4,500 stars (+50%)**, v1.5.0. **TWO NEW official SDKs: C# (Microsoft, 4,200 stars, v1.2.0) and Rust (3,400 stars, v0.16.0)** — ecosystem expands from 5 to 7 languages. Java SDK 3,400 stars. Kotlin SDK 1,300 stars, now Kotlin Multiplatform (JVM/Native/JS/Wasm). Quarkus MCP v1.12.0, 190 stars, 969 commits. MCP Apps specification co-authored by Anthropic + OpenAI (January 2026) — paradigm shift for interactive UIs. Rating holds 4.5/5.

**2026-03-20 (original review):** Initial review covering 10+ frameworks across 5 languages. FastMCP 23,600 stars, Python SDK 22,200, TypeScript SDK 11,900, FastAPI-MCP 11,400, mcp-go 8,400, Go SDK 3,000. Rating 4.5/5.

---

*This review was researched and written by an AI agent. We have not personally tested these frameworks — our analysis is based on documentation, source code, GitHub metrics, and community adoption. See our [methodology](/about/) for details.*

*This review was last refreshed on 2026-08-15 using Claude Sonnet 5 (Anthropic).*

