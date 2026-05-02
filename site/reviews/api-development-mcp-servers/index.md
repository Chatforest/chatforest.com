# API Development MCP Servers — OpenAPI Converters, GraphQL, gRPC, and the Rise of Spec-to-Server Generation

> API development MCP servers surging: openapi-mcp-server (889 stars, NEW #1), Agoda APIAgent (271 stars, GraphQL+REST+DuckDB SQL), openapi-mcp-generator (576 stars +16%), Apollo v1.13.0 MCP prompts


**At a glance:** API development MCP servers are surging with **two major new entries** and a **revived Postman**. [openapi-mcp-server](https://github.com/janwilmake/openapi-mcp-server) (889 stars, NEW) is now the **most-starred OpenAPI MCP server**, enabling AI to search and explore specs via oapis.org. [Agoda APIAgent](https://github.com/agoda-com/api-agent) (271 stars, NEW) is the **first universal GraphQL+REST MCP proxy** with DuckDB SQL post-processing and recipe learning — zero code, zero deployment. [openapi-mcp-generator](https://github.com/harsha-iiiv/openapi-mcp-generator) grew to 576 stars (+16%). [Apollo MCP](https://github.com/apollographql/apollo-mcp-server) reached v1.13.0 with MCP prompts, config hot reloading, and Rhai scripting extensibility. [Postman](https://github.com/postmanlabs/postman-mcp-server) **REVIVED** (227 stars, v2.8.7) with OAuth 2.0 remote server at mcp.postman.com — closing the biggest gap from our original review. API gateway platforms consolidating around hosted MCP: Salesforce GA April 2026, Apigee fully managed, MuleSoft API Catalog. This is the **fourteenth review in our [Developer Tools MCP category](/categories/developer-tools/)**.

The API management market is projected at $6.89–10B in 2025, growing to $19.28B by 2030. REST dominates (~83% of web services), but GraphQL adoption has exploded — 50%+ of enterprises now use it in production (up from 10% in 2021), with 340% growth among Fortune 500 companies (2023–2025). gRPC is the de facto standard for internal microservices at Netflix, Uber, and Google. Gartner estimates the API and MCP testing tools market at $582M for 2026, with MCP-related inquiries growing 300% year-over-year. The MCP ecosystem reflects this multi-protocol reality: unlike most Developer Tools categories where one protocol dominates, API development MCP servers must bridge REST, GraphQL, and gRPC — and the spec-to-server pattern is evolving from simple conversion to intelligent post-processing (Agoda APIAgent's DuckDB SQL layer) and full agent generation (cnoe-io's LangGraph output).

**Architecture note:** API development MCP servers follow five patterns. **Spec-to-server converters** (openapi-mcp-generator, openapi-mcp-server, emcee, AWS Labs, Swagger-MCP) transform OpenAPI/Swagger specifications into MCP tools automatically — the dominant pattern. **Intelligent API proxies** (Agoda APIAgent, cnoe-io/openapi-mcp-codegen) go beyond simple conversion: APIAgent adds DuckDB SQL post-processing and recipe caching; cnoe-io generates full LangGraph agents with evaluation frameworks. **Protocol bridges** (Apollo MCP, mcp-graphql, protoc-gen-go-mcp) provide native access to GraphQL and gRPC APIs through MCP. **API testing platforms** (Postman MCP, mcp-insomnia) expose collection management, request execution, and test reporting. **API mocking servers** (MockLoop, WireMock MCP, MSW MCP) generate mock endpoints from specs for development and testing.

## What's Available

### openapi-mcp-server — AI-Friendly OpenAPI Exploration via oapis.org (NEW — Most Starred)

| Aspect | Detail |
|--------|--------|
| Repository | [janwilmake/openapi-mcp-server](https://github.com/janwilmake/openapi-mcp-server) |
| Stars | ~889 |
| Forks | ~93 |
| Language | TypeScript (100%) |
| License | MIT |
| Commits | 56 |

**Key capabilities:**

| Capability | Detail |
|-----------|--------|
| Spec search | Search and discover OpenAPI specs via oapis.org registry |
| Simplified summaries | Translates complex specs into plain language for AI agents |
| Endpoint details | Provides per-endpoint detail on demand without full spec loading |
| Format support | JSON and YAML OpenAPI specifications |
| Integration | Claude Desktop and Cursor |

**Key differentiator:** The **most-starred dedicated OpenAPI MCP server** at 889 stars. Unlike converters that turn specs into tools, this server takes a **discovery-first approach** — AI agents can search for APIs, get simplified summaries, and drill into specific endpoints. This solves the context window problem differently: instead of generating 200 tools for a large API, the agent requests only the endpoint details it needs. Integration with oapis.org provides a searchable registry of OpenAPI specs.

**Limitation:** Read-only discovery and exploration — the agent can learn about APIs but can't execute requests through this server. Requires pairing with an actual OpenAPI converter or direct API calls. Limited to specs available on oapis.org or user-provided specs. 56 commits suggests early-stage development despite high star count.

### openapi-mcp-generator — Dynamic MCP from Any OpenAPI Spec

| Aspect | Detail |
|--------|--------|
| Repository | [harsha-iiiv/openapi-mcp-generator](https://github.com/harsha-iiiv/openapi-mcp-generator) |
| Stars | ~576 |
| Forks | ~79 |
| Language | TypeScript |
| License | Not specified |
| Transport | stdio, SSE, Streamable HTTP |

**Key capabilities:**

| Capability | Detail |
|-----------|--------|
| OpenAPI 3.0+ conversion | Automatically generates MCP tools from any OpenAPI specification |
| API proxying | Proxies requests to the original REST API, maintaining authentication |
| Zod validation | Runtime validation of requests using schemas derived from OpenAPI definitions |
| Auth support | API key, Bearer token, Basic auth, OAuth2 |
| TypeScript output | Typed tool definitions for type-safe interactions |

**Key differentiator:** The **most-starred OpenAPI-to-MCP converter** (576 stars, up from 495). Give it any OpenAPI 3.0+ spec and it dynamically generates MCP tools for every endpoint, handling authentication, validation, and proxying automatically. This is the purest expression of the spec-to-server pattern: one configuration step turns any documented REST API into an AI-accessible tool surface. Triple transport support (stdio, SSE, Streamable HTTP) makes it deployable in any MCP architecture. Now supports **OpenAPI filtering via `x-mcp` extension flags** to selectively expose endpoints.

**Limitation:** Dynamically generated tools can produce large tool lists for complex APIs (hundreds of endpoints), which consumes LLM context window. No filtering or grouping mechanism to expose only relevant endpoints. License not specified on GitHub, which may concern enterprise adoption. Quality of generated tools depends entirely on the quality of the underlying OpenAPI spec — poorly documented APIs produce poor MCP tools.

### emcee — Go-Based OpenAPI Converter with 1Password Integration

| Aspect | Detail |
|--------|--------|
| Repository | [loopwork/emcee](https://github.com/loopwork/emcee) |
| Stars | ~321 |
| Forks | ~25 |
| Language | Go (89.3%) |
| License | MIT |
| Releases | 21 releases, v0.7.0 (October 2025) |

**Key capabilities:**

| Capability | Detail |
|-----------|--------|
| OpenAPI conversion | MCP server for any app with an OpenAPI specification |
| Secret management | Bearer token, Basic auth, and 1Password integration |
| Spec transformation | Unix-utility based spec transformation pipeline |
| Installation | Docker and Homebrew support |
| Transport | stdio (JSON-RPC 2.0) |

**Key differentiator:** The **most mature and well-maintained OpenAPI-to-MCP converter**, with 21 releases and 88 commits indicating active development. The 1Password integration is unique — API credentials can be pulled from 1Password vaults rather than stored in plaintext configuration files. The Go implementation and Unix-utility spec transformation pipeline give it a composable, developer-friendly architecture. MIT license removes enterprise adoption barriers.

**Limitation:** Tools only — no MCP resources or prompts support yet. stdio transport only limits remote deployment options. Spec transformation via Unix utilities is powerful but adds a learning curve. **Last release October 2025 (7 months ago)** — development appears stagnant while competitors like openapi-mcp-generator and openapi-mcp-server have surged ahead. v0.7.0 suggests pre-1.0 stability expectations.

### AWS Labs OpenAPI MCP Server

| Aspect | Detail |
|--------|--------|
| Repository | [awslabs/mcp](https://github.com/awslabs/mcp) (monorepo) |
| Monorepo stars | ~8,500 |
| Monorepo forks | ~1,400 |
| Language | Python |
| License | Apache-2.0 |

**Key capabilities:**

| Capability | Detail |
|-----------|--------|
| Dynamic tool generation | Automatically creates MCP tools from API endpoints |
| Intelligent routing | Maps GET endpoints with parameters to appropriate MCP tools |
| Auth support | Basic, Bearer, API Key, Cognito authentication |
| Observability | Built-in metrics collection, caching, and resilience patterns |
| Validation | OpenAPI spec validation of requests and responses |

**Key differentiator:** Part of the **AWS Labs MCP monorepo** (8,500 stars), which gives it the backing of a major cloud provider. The intelligent route mapping automatically determines which API endpoints should become MCP tools and how parameters should be structured. Cognito authentication integration is unique to this server — AWS-native teams can use their existing IAM infrastructure. Built-in metrics and observability reflect enterprise-grade design.

**Limitation:** Python-only implementation. Part of a monorepo, so star count is shared across all AWS MCP servers (CDK, CloudFormation, Terraform, etc.) — individual adoption is unclear. AWS-centric auth (Cognito) may not suit non-AWS teams. Inherits the general spec-to-server limitation: tool count scales with API surface area.

### Apollo MCP Server — Official GraphQL (Most Active Development)

| Aspect | Detail |
|--------|--------|
| Repository | [apollographql/apollo-mcp-server](https://github.com/apollographql/apollo-mcp-server) |
| Stars | ~275 |
| Forks | ~66 |
| Language | Rust (98.8%) |
| License | MIT / Elastic License 2.0 |
| Commits | 1,576+ |
| Releases | 70+ (v1.13.0, April 22, 2026) |

**Key capabilities:**

| Capability | Detail |
|-----------|--------|
| GraphQL operations | Exposes GraphQL operations as MCP tools |
| REST via Connectors | REST API integration through Apollo Connectors |
| MCP prompts | Reusable Markdown templates guiding AI through workflows (v1.13.0) |
| Rhai scripting | Extensibility hooks with hot reloading (v1.11.0+) |
| Config hot reload | Live config changes without restart (v1.12.0) |
| MCP Apps | OpenAI Apps SDK support for ChatGPT, Goose (v1.8.0+) |
| Dynamic tools | Tool list depends on user's GraphQL operations |

**Key differentiator:** The **most actively developed MCP server in the API development category** — 1,576+ commits, 70+ releases, v1.13.0 as of April 2026. Nine releases in two months (v1.8.0→v1.13.0) since our last review. New in v1.11.0–v1.13.0: **Rhai script extensibility** with hot reloading for custom hooks, **MCP prompts** enabling reusable Markdown templates that guide AI through API workflows, **config hot reloading** without restarts, per-operation tool annotation overrides, and trace_id logging. The Rust implementation prioritizes performance. REST API integration via Apollo Connectors means this server isn't GraphQL-only. **MCP Apps support** (v1.8.0) enables serving AI apps built with Apollo Client to platforms like ChatGPT and Goose.

**Limitation:** Dual-licensed (MIT and Elastic License 2.0) — the Elastic License restricts providing the software as a managed service. Requires Apollo platform knowledge. Dynamic tool generation depends on pre-defined GraphQL operations, meaning the server exposes what you've already built, not arbitrary GraphQL capabilities. 275 stars is modest compared to Apollo's broader platform adoption.

### mcp-graphql — Community GraphQL Server (Most Starred GraphQL)

| Aspect | Detail |
|--------|--------|
| Repository | [blurrah/mcp-graphql](https://github.com/blurrah/mcp-graphql) |
| Stars | ~383 |
| Forks | ~58 |
| Language | TypeScript (96%) |
| License | MIT |
| Version | v2.0.4 (May 2025) |

**Key capabilities:**

| Capability | Detail |
|-----------|--------|
| Schema discovery | Dynamic introspection or local/remote schema files |
| Query execution | Execute GraphQL queries against any endpoint |
| Mutation control | Mutations disabled by default for safety |
| Custom headers | Configurable headers for auth and API management |
| Tools | 2 core tools: introspect-schema, query-graphql |

**Key differentiator:** The **most-starred GraphQL MCP server** at 374 stars, surpassing Apollo's official server. The mutations-disabled-by-default design is notable — it prevents AI agents from accidentally modifying data through GraphQL mutations until explicitly enabled. The simplicity (2 core tools) keeps it focused: discover a schema, then query it. Works with any GraphQL endpoint, not just Apollo-managed ones.

**Limitation:** Only 2 tools — introspection and querying. No mutation support by default (safe but limiting for write operations). **Last release May 2025 (12 months ago), 80 total commits** — effectively in maintenance mode while Apollo races ahead with 70+ releases. No type-safe query building or validation — the AI agent constructs raw GraphQL queries, which may produce invalid syntax. No subscription support.

### Postman MCP Server — Official API Testing Platform

| Aspect | Detail |
|--------|--------|
| Repository | [postmanlabs/postman-mcp-server](https://github.com/postmanlabs/postman-mcp-server) |
| Stars | ~227 |
| Forks | ~69 |
| Language | TypeScript |
| License | Not specified |
| Version | v2.8.7 (April 13, 2026) |
| Commits | 167 |
| Transport | HTTP (streamable), stdio |
| Remote server | mcp.postman.com (OAuth 2.0, US + EU regions) |

**Key capabilities:**

| Capability | Detail |
|-----------|--------|
| Tool count | 100+ in Full mode |
| Configuration modes | Minimal (default), Full, Code |
| Collection management | Create, run, and manage API test collections |
| Workspace management | Access workspaces, environments, variables |
| Code generation | Client code generation from API definitions |
| Spec creation | Automatic API specification creation |

**Key differentiator:** The **largest tool surface of any API development MCP server** — 100+ tools in Full mode. Postman is the dominant API development platform (30M+ users), and their official MCP server exposes the full platform capability: collections, environments, workspaces, code generation, and test execution. Three configuration modes (Minimal, Full, Code) let teams control the tool surface exposed to AI agents. **REVIVED since our last review:** v2.8.7 (April 2026) with active development, **OAuth 2.0 remote server** at mcp.postman.com (no API key needed), **EU region support**, built-in Instructions resource for MCP clients, and integration with Google Antigravity IDE, Claude Code, Cursor, VS Code, Codex, Windsurf, and Gemini CLI. The 14-month maintenance gap that was our biggest concern is definitively closed.

**Limitation:** 100+ tools in Full mode may overwhelm LLM context windows. License not specified. Postman's business model (free tier with paid team features) means some MCP tools may require paid plans. Platform-dependent — collections and workspaces live in Postman's cloud. OAuth remote server currently US and EU only.

### protoc-gen-go-mcp (Redpanda) — gRPC Protocol Buffer Plugin

| Aspect | Detail |
|--------|--------|
| Repository | [redpanda-data/protoc-gen-go-mcp](https://github.com/redpanda-data/protoc-gen-go-mcp) |
| Stars | ~199 |
| Forks | ~32 |
| Language | Go |
| License | Apache-2.0 |
| Creator | Redpanda Data (official) |

**Key capabilities:**

| Capability | Detail |
|-----------|--------|
| Protobuf compiler plugin | Generates Go MCP server code from .proto files |
| JSON schema generation | Auto-generates JSON schemas for tool parameters |
| Dual provider support | MCP + OpenAI function calling schemas |
| Library agnostic | Supports official go-sdk and mcp-go libraries |
| Tool namespacing | Prevents collisions across multiple .proto files |
| buf.validate support | Integration with Buf validation rules |

**Key differentiator:** The **only production-grade gRPC-to-MCP bridge**. As a protoc compiler plugin, it fits naturally into existing gRPC build pipelines — run `protoc` with the plugin and you get a Go MCP server alongside your regular gRPC stubs. Dual schema generation (MCP + OpenAI) means the same .proto files can power both MCP tools and OpenAI function calls. Backed by Redpanda, a well-funded data streaming company, indicating sustained investment.

**Limitation:** Go-only output — no TypeScript, Python, Java, or Rust MCP server generation from .proto files. Requires understanding of the protobuf compilation pipeline. 190 stars suggests adoption is limited to teams already using both gRPC and MCP. No support for gRPC streaming in MCP tools (MCP's request-response model doesn't map to gRPC streams).

### Agoda APIAgent — Universal GraphQL+REST Proxy with SQL Post-Processing (NEW)

| Aspect | Detail |
|--------|--------|
| Repository | [agoda-com/api-agent](https://github.com/agoda-com/api-agent) |
| Stars | ~271 |
| Forks | ~43 |
| Language | Python (99.8%) |
| License | MIT |
| Commits | 9 |

**Key capabilities:**

| Capability | Detail |
|-----------|--------|
| Zero configuration | Point at GraphQL endpoint or OpenAPI spec — auto-introspection |
| SQL post-processing | DuckDB in-memory SQL for rankings, filters, JOINs the API can't do |
| Safety | Read-only by default, mutations blocked unless explicitly allowed |
| Recipe learning | Successful queries become cached pipelines, reusable without LLM reasoning |
| Tools | 2 core tools per API ({prefix}_query + {prefix}_execute) + dynamic recipe tools |

**Key differentiator:** The **first intelligent API proxy** that goes beyond spec-to-server conversion. Agoda APIAgent doesn't just generate MCP tools from an API spec — it adds a **DuckDB SQL post-processing layer** that enables rankings, filtering, grouping, and JOINs even when the underlying API doesn't support them. Recipe learning means successful queries become cached pipelines that skip LLM reasoning on repeat calls. Uses FastMCP + OpenAI Agents SDK architecture. Works with both GraphQL and REST/OpenAPI, making it the only server that handles both protocols natively.

**Limitation:** Only 9 commits — very early-stage despite 271 stars. Requires an LLM API key for the orchestration layer (OpenAI Agents SDK), adding cost per query. Read-only by default limits write-heavy API workflows. The DuckDB SQL layer adds latency compared to direct API calls. Python-only implementation.

### OpenAPI Converters — The Long Tail

**[Swagger-MCP (Vizioz)](https://github.com/Vizioz/Swagger-MCP)** (150 stars, TypeScript, MIT) — 5 tools including code generation: getSwaggerDefinition, listEndpoints, listEndpointModels, generateModelCode, generateEndpointToolCode. Converts Swagger/OpenAPI to MCP server definitions with semantic tool naming and MCP prompts for guided workflows. Downloads and caches specs locally.

**[openapi-mcp (ckanthony)](https://github.com/ckanthony/openapi-mcp)** (180 stars, Go, January 2026) — Secure API key management (hidden from MCP client), selective endpoint exposure via include/exclude filters, custom header injection. Docker deployment. Unique security feature: API keys are never exposed to the AI agent.

**[cnoe-io/openapi-mcp-codegen](https://github.com/cnoe-io/openapi-mcp-codegen)** (37 stars, Python, Apache 2.0, NEW) — Goes beyond MCP tool generation to produce **full LangGraph React agents** with A2A servers (`--generate-agent`), evaluation frameworks with LangFuse (`--generate-eval`), and LLM-enhanced docstrings via OpenAPI Overlay Specification 1.0.0. Smart parameter handling auto-detects complex schemas and uses dictionary mode for operations with 10+ parameters. The most architecturally ambitious OpenAPI converter.

**[swagger-mcp (danishjsheikh)](https://github.com/danishjsheikh/swagger-mcp)** (81 stars, Go, MIT) — Dynamic tool generation from swagger.json at runtime, anti-hallucination focus (strict data retrieval from actual API responses). stdio and SSE transports.

**[swagger-mcp (amrsa1)](https://github.com/amrsa1/swagger-mcp)** (8 stars, JavaScript, MIT) — Auto-detection of IDE configs, intelligent token refresh on 401 responses, schema validation. 5 tools including execute_api_request.

### GraphQL — Additional Servers

**[mcp-graphql-schema (hannesj)](https://github.com/hannesj/mcp-graphql-schema)** (44 stars, JavaScript, MIT) — 10 tools for browsing query/mutation/subscription root fields, type definitions, pattern-based schema search. Auto-filters internal system types. More granular schema exploration than mcp-graphql.

**[mcp-graphql-forge (toolprint)](https://github.com/toolprint/mcp-graphql-forge)** (17 stars, TypeScript, Apache 2.0) — Auto-generates 63 tools from a sample schema (30 queries, 33 mutations). Multi-layer validation, smart field selection with circular reference handling, schema caching (~5ms tool generation), 40+ test cases. stdio and Streamable HTTP.

### gRPC — Additional Servers

**[grpcmcp (adiom-data)](https://github.com/adiom-data/grpcmcp)** (27 stars, Go, Apache 2.0) — Proxy to gRPC backend via descriptor files or reflection, bearer token auth, service filtering. SSE and stdin transports.

**[grpcurl-mcp (wricardo)](https://github.com/wricardo/grpcurl-mcp)** (16 stars, Go) — 3 tools (invoke, list, describe) wrapping grpcurl for gRPC method invocation and service discovery.

### API Testing — Additional Servers

**[mcp-postman (shannonlal)](https://github.com/shannonlal/mcp-postman)** (84 stars, TypeScript, ISC) — Execute Postman collections via Newman CLI. 1 focused tool with comprehensive test reporting (pass/fail/timing). Simpler alternative to the official server.

**[mcp-insomnia (anggasct)](https://github.com/anggasct/mcp-insomnia)** (14 stars, TypeScript, MIT, March 2026) — 30+ tools for Insomnia API client. Collection/folder management, request CRUD and execution, import from cURL/Postman/OpenAPI/Insomnia formats, code snippet generation, environment variable support. Actively maintained.

**[bruno-mcp (macarthy)](https://github.com/macarthy/bruno-mcp)** (10 stars, TypeScript, MIT) — 6 tools for the Bruno API client: create_collection, create_environment, create_request, create_crud_requests, add_test_script, get_collection_stats.

### API Mocking

**[MockLoop MCP](https://github.com/MockLoop/mockloop-mcp)** (15 stars, Python) — 30 tools (16 testing + 10 context + 4 core). Generates mock servers from OpenAPI specs, 3 modes (Mock/Proxy/Hybrid), enterprise audit logging, load/security/performance testing. The most full-featured mocking MCP server.

**WireMock MCP** — Built into WireMock CLI (WireMock itself has 6k+ stars). Codebase-aware API simulation, create/update mock endpoints via AI agents. Not a standalone repo.

**[MSW MCP (JasonBoy)](https://github.com/JasonBoy/msw-mcp)** (2 stars, TypeScript, MIT, February 2026) — AI-powered Mock Service Worker handler generation from natural language, real-time handler updates without page reload. WebSocket bridge transport.

### API Gateway / Management

**[Kong MCP Konnect](https://github.com/Kong/mcp-konnect)** (42 stars, TypeScript, Apache 2.0) — **DEPRECATED** (archived, read-only). Users directed to official Konnect remote MCP server. **Kong AI Gateway 3.14** (April 2026) now supports **agent-to-agent (A2A) traffic** alongside LLM and MCP, becoming a unified control plane for all AI traffic types with MCP traffic governance, security, and observability.

**Google Apigee MCP** — **Fully managed MCP servers** GA in 2026. Deploy an MCP proxy and Apigee handles all transcoding and protocol handling. API Hub now includes managed integration with **Agent Registry** to automatically synchronize MCP servers and tools metadata. **MCP is a first-class API style** in API Hub alongside REST and GraphQL. No manual MCP server setup needed — Apigee auto-generates from existing API specs.

**MuleSoft MCP Server** (Salesforce/MuleSoft managed) — 47+ tools across 9 categories. **MuleSoft MCP Connector v1.4** enables AI clients to invoke and interact with APIs, connectors, and apps via MCP. **New: MuleSoft API Catalog for Salesforce** — centralized hub for managing APIs and MCP servers from MuleSoft, Heroku, and Apex sources.

**Salesforce Hosted MCP Servers** — **GA April 2026**. Exposes Salesforce org's logic and assets (data, flows, Apex actions, queries) to any MCP client. Enterprise-grade authentication, governance, and admin control built in. Included at no additional cost for Enterprise Edition orgs and above. CRUD, FLS, and sharing rules apply automatically.

### API Documentation

**Redocly MCP Server** — Built into Redocly Realm platform. Auto-generates MCP server from documentation + OpenAPI descriptions, supports the x-mcp OpenAPI extension for documenting MCP servers. Not a standalone repo.

### Notable Gaps

**No HTTPie MCP server** — HTTPie (a popular developer-friendly HTTP client) has no MCP integration. Also missing: RapidAPI, Stoplight. Hoppscotch has an MCP **client** feature request (issue #5966, March 2026) but no MCP server.

**No AsyncAPI MCP server** — Event-driven API specifications (Kafka, WebSocket, MQTT) have no MCP tooling. Only request-response APIs (REST, GraphQL, gRPC) are covered. This gap grows more significant as event-driven architectures expand.

**No dedicated Swagger UI or API documentation generation server** — OpenAPI converters focus on tool generation, not documentation rendering or generation.

**No Mockoon MCP server** — Despite Mockoon's 6k+ GitHub stars as an API mocking tool, no MCP integration exists. Also missing: JSON Server, Karate, SoapUI, Dredd.

**API gateway MCP servers fully vendor-hosted** — Kong archived its open-source server; Apigee, MuleSoft, and Salesforce are all platform-embedded managed services. Tyk and AWS API Gateway have no dedicated MCP servers. Self-hosted teams have zero options.

## Developer Tools MCP Comparison

| Aspect | GitHub | GitLab | Bitbucket | Docker | Kubernetes | CI/CD | IDE/Editor | Testing/QA | Monitoring | Security | IaC | Packages | Code Gen | API Dev | Logging | DB Migration | Doc Tooling | Debugging | Profiling | Code Review |
|--------|--------|--------|-----------|--------|------------|-------|------------|------------|------------|----------|-----|----------|----------|---------|---------------------- | --------------|-----------|-----------|-------------|
| **Official MCP server** | Yes (28.2k stars, 21 toolsets) | Yes (built-in, 15 tools, Premium+) | No (Jira/Confluence only) | [Hub MCP (132 stars, 12+ tools)](/reviews/docker-mcp-servers/) | No (Red Hat leads, 1.3k stars) | Yes (Jenkins, CircleCI, Buildkite) | Yes (JetBrains built-in, 24 tools) | Yes (MS Playwright, 9.8k stars, 24 tools) | Yes (Grafana 2.5k, Datadog, Sentry, Dynatrace, New Relic, Instana) | Yes (Semgrep, SonarQube, Snyk, Trivy, GitGuardian, Cycode, Contrast) | Yes (Terraform 1.4k, Pulumi remote, AWS IaC, Bicep, Ansible AAP) | Yes (NuGet built-in VS 2026, WinGet built-in, Homebrew built-in) | Partial (Vercel next-devtools 694, E2B 384, JetBrains built-in server) | Yes (Postman 227 v2.8.7 OAuth remote, Apollo 275 v1.13.0, Apigee managed, MuleSoft v1.4, Salesforce GA) | Yes (Splunk 13 tools GA, Grafana Tempo built-in, Grafana Loki 103 stars) | Partial (Liquibase private preview 19 tools, Prisma built-in CLI v6.6.0+) | Yes (Microsoft Learn 1.5k, Mintlify auto, ReadMe per-project, Stainless, OpenAI Docs) | Yes (Chrome DevTools 31k, Microsoft DebugMCP 263, MCP Inspector 9.2k official) | Partial (CodSpeed MCP, Polar Signals remote, Grafana Pyroscope via mcp-grafana) | Yes (SonarQube 442 stars, Codacy 56 stars, Graphite GT built-in) |
| **Top community server** | GitMCP (7.8k stars) | zereight/gitlab-mcp (1.2k stars) | aashari (132 stars) | [ckreiling (691 stars, 25 tools)](/reviews/docker-mcp-servers/) | Flux159 (1.4k stars, 20+ tools) | Argo CD (356 stars, 12 tools) | vscode-mcp-server (342 stars, 15 tools) | executeautomation (5.3k stars) | pab1it0/prometheus (340 stars) | CodeQL community (143 stars) | Ansible (27 stars, 40+ tools) | mcp-devtools (140 stars, 20+ tools) | Context7 (54.2k stars), magic-mcp (4.8k stars) | openapi-mcp-server (889 stars), openapi-mcp-generator (576 stars), Agoda APIAgent (271 stars) | cr7258/elasticsearch (259 stars), Traceloop OTel (178 stars) | mpreziuso/mcp-atlas (Atlas), defrex/drizzle-mcp (Drizzle) | GitMCP (7.8k stars), Grounded Docs (1.2k stars), Docs MCP (87 stars) | claude-debugs-for-you (496 stars), x64DbgMCPServer (398 stars), devtools-debugger (341 stars) | theSharque/mcp-jperf (Java JFR), PageSpeed Insights MCP servers | kopfrechner/gitlab-mr-mcp (86 stars), crazyrabbitLTC (32 stars) |
| **Primary function** | Repository operations | Repository operations | Repository operations | Container lifecycle | Cluster management | Pipeline management | Editor integration | Test execution | Observability queries | Vulnerability scanning | Infrastructure provisioning | Dependency intelligence | Context provision + UI generation | Spec-to-server conversion + API interaction | Log search/analysis + trace correlation | Schema migration & version control | Doc access, search, generation & quality | Breakpoints, stepping, variable inspection, crash analysis | Flamegraph analysis, CPU/memory profiling, benchmarks, web audits, load testing | Code quality analysis, PR management, diff review, stacked PR creation |
| **Vendor count** | 1 (GitHub) | 1 (GitLab) | 0 (Atlassian via Jira only) | 1 (Docker) + community | 0 (Red Hat leads community) | 3 (Jenkins, CircleCI, Buildkite) | 1 (JetBrains) | 1 (Microsoft) | 6 (Grafana, Datadog, Sentry, Dynatrace, New Relic, Instana) | 7+ (Semgrep, SonarQube, Snyk, Trivy, GitGuardian, Cycode, Contrast) | 7+ (HashiCorp, Pulumi, AWS, Microsoft/Bicep, Red Hat/Ansible, OpenTofu, Spacelift) | 3 (Microsoft/NuGet, Microsoft/WinGet, Homebrew) | 3 (Vercel, E2B, Upstash/Context7) | 6+ (Postman, Apollo, Agoda, Google/Apigee, MuleSoft, Salesforce) | 6+ (Splunk, Grafana/Loki, Grafana/Tempo, Coralogix, Axiom, Mezmo) | 2 (Liquibase, Prisma) + Google partial | 5+ (Microsoft, Mintlify, ReadMe, Stainless, OpenAI, Vonage, Fern, Apidog) | 3 (Google/Chrome DevTools, Microsoft/DebugMCP, LLVM/LLDB built-in) | 3 (CodSpeed, Polar Signals, Tricentis/NeoLoad) + Grafana partial | 3 (SonarSource, Codacy, Graphite) + CodeRabbit as client |
| **Code generation role** | Context (repos, issues, PRs) | Context (repos, issues, MRs) | Context (repos, PRs) | Context (images, containers) | Context (cluster state) | Context (pipeline status) | Bidirectional (tools + context) | Context (test results) | Context (metrics, logs) | Context (vulnerabilities) | Generation (IaC templates) | Context (versions, advisories) | Direct (UI components, docs, execution) | Bidirectional (spec-to-tools, API execution) | Context (log patterns, traces, errors) | Bidirectional (migration generation + schema inspection) | Context (doc access/search) + Generation (doc output) | Bidirectional (set breakpoints + inspect state) | Context (profiles, flamegraphs, benchmarks) + Generation (benchmark harnesses) | Bidirectional (quality data as context + review comments as output) |
| **Authentication** | PAT / GitHub App | OAuth 2.0 / PAT | App Password / OAuth | Docker Desktop credentials | kubeconfig / OAuth / OIDC | API tokens per platform | Local connection (port/stdio) | None (local browsers) | API tokens / OAuth (remote) | API tokens / CLI auth | API tokens / OAuth / CLI auth | None (public registries) | API keys (Context7, magic-mcp, E2B) | API keys / Bearer / OAuth / 1Password | API tokens / OAuth / RBAC (Splunk) | Database credentials / CLI auth | None (GitMCP, MS Learn) / API keys (platform MCP) | None (local debuggers) / Chrome DevTools auto-connect | API keys (CodSpeed, Polar Signals) / Grafana auth / Google API key (PageSpeed) | API tokens (SonarQube, Codacy) / GitHub PAT / GitLab PAT |
| **AAIF membership** | No (but Microsoft is Platinum) | No | No | [Gold](/reviews/docker-mcp-servers/) | No (but Google/AWS/MS are Platinum) | No | No (but Microsoft is Platinum) | No (but Microsoft is Platinum) | No | No | No | No (but Microsoft is Platinum) | No | No | No | No | No (but Microsoft is Platinum) | No (but Google/Microsoft are Platinum) | No | No |
| **Platform users** | 180M+ developers | 30M+ users | ~41k companies | 20M+ users | 5.6M developers | Jenkins: 11.3M devs | VS Code: 75.9% market share | Playwright: 45.1% QA adoption | Datadog: 32.7k customers | SonarQube: 17.7% SAST mindshare | Terraform: millions of users, 45% IaC adoption | npm: 5B+ weekly downloads | Copilot: 20M+ users, Cursor: 1M+ DAU | Postman: 30M+ users, REST: ~83% of web APIs | Splunk: 15k+ customers, ELK: most-deployed log stack | Prisma: 43k stars, Flyway: 10.7k stars, Atlas: 6.3k stars | Mintlify: 28k+ stars, Docusaurus: 60k+ stars, ReadMe: powering major API docs | Chrome: 65%+ browser share, VS Code: 75.9% IDE share, x64dbg: 45k+ stars | APM market: $7-10B, Pyroscope: 11k+ stars, async-profiler: 9k+ stars | SonarQube: 7.4M+ users, CodeRabbit: top AI reviewer, Qodo/PR-Agent: 10.5k stars |
| **Our rating** | [4.5/5](/reviews/github-mcp-server/) | [3.5/5](/reviews/gitlab-mcp-server/) | [2.5/5](/reviews/bitbucket-mcp-server/) | [4/5](/reviews/docker-mcp-servers/) | [4/5](/reviews/kubernetes-mcp-servers/) | [3/5](/reviews/ci-cd-mcp-servers/) | [3.5/5](/reviews/ide-code-editor-mcp-servers/) | [3.5/5](/reviews/testing-qa-mcp-servers/) | [4/5](/reviews/monitoring-observability-mcp-servers/) | [4/5](/reviews/security-scanning-mcp-servers/) | [4/5](/reviews/infrastructure-as-code-mcp-servers/) | [3.5/5](/reviews/package-management-dependency-mcp-servers/) | [3.5/5](/reviews/code-generation-mcp-servers/) | 4/5 | [3.5/5](/reviews/logging-tracing-mcp-servers/) | [2.5/5](/reviews/database-migration-mcp-servers/) | [3.5/5](/reviews/documentation-tooling-mcp-servers/) | [4.5/5](/reviews/debugging-mcp-servers/) | [3/5](/reviews/profiling-performance-mcp-servers/) | [3.5/5](/reviews/code-review-pull-request-mcp-servers/) |

## Known Issues

1. **Spec-to-server conversion produces tool explosion — but solutions are emerging** — An API with 200 endpoints generates 200 MCP tools. LLMs have finite context windows and tool selection degrades as tool count increases. However, new approaches are addressing this: openapi-mcp-server (889 stars) takes a discovery-first approach where agents request only needed endpoint details; openapi-mcp-generator now supports x-mcp filtering flags; openapi-mcp (ckanthony) offers include/exclude filters. The tool explosion problem is being solved from multiple angles.

2. **OpenAPI spec quality determines MCP tool quality** — Every OpenAPI-to-MCP converter inherits the quality (or lack thereof) of the source specification. Missing descriptions, incomplete schemas, undocumented error codes, and absent examples all produce MCP tools that the AI agent struggles to use correctly. There's no validation or enrichment step — garbage in, garbage out.

3. **GraphQL mutations present safety risks** — mcp-graphql wisely disables mutations by default, but Apollo MCP exposes whatever operations are defined. An AI agent with mutation access can create, update, or delete data through GraphQL. There's no cross-server standard for read-only mode, confirmation prompts, or mutation safeguards. The risk scales with the API's destructive capabilities.

4. **gRPC streaming has no MCP equivalent** — MCP's request-response model doesn't map to gRPC's four streaming modes (unary, server-streaming, client-streaming, bidirectional). protoc-gen-go-mcp generates tools for unary RPCs only. Server streaming, which powers many real-time gRPC services, is inaccessible through MCP. This is a protocol-level limitation, not a tooling gap.

5. **API gateway MCP servers are fully vendor-hosted** — Kong archived its open-source server and launched Kong AI Gateway 3.14 for managed MCP traffic. Apigee auto-generates MCP from API specs. MuleSoft has MCP Connector v1.4. Salesforce Hosted MCP Servers went GA April 2026. The trend is clearly toward vendor-hosted, platform-locked endpoints. Self-hosted teams have zero standalone API gateway MCP options.

6. **API mocking MCP servers have near-zero adoption** — MockLoop (15 stars), MSW MCP (2 stars), mock-mcp (5 stars). Despite API mocking being a critical development workflow (Mockoon has 6k+ stars, WireMock has 6k+), MCP mocking servers haven't gained traction. The gap is significant: AI agents should be able to set up mock backends for frontend development and testing.

7. **No AsyncAPI or event-driven API support** — Every API development MCP server targets request-response protocols (REST, GraphQL, gRPC). Event-driven APIs (Kafka, WebSocket, MQTT, AMQP) — documented by AsyncAPI — have zero MCP coverage. As event-driven architectures grow, this gap widens.

8. **Authentication handling varies wildly** — openapi-mcp-generator supports API key/Bearer/Basic/OAuth2. emcee integrates with 1Password. openapi-mcp (ckanthony) hides API keys from the MCP client. AWS Labs uses Cognito. There's no standard for how MCP servers should handle API authentication. Some expose credentials to the AI agent; others keep them server-side. The security implications are significant — 53% of MCP servers rely on insecure long-lived static secrets, and only 8.5% use OAuth.

9. **~~Postman's official server may be abandoned~~ RESOLVED** — Postman revived development with v2.8.7 (April 2026), OAuth 2.0 remote server at mcp.postman.com, EU region support, Instructions resource, and integrations with 7+ AI tools. The 14-month gap is closed. Insomnia v12 also added native MCP client support — the API testing space is now competitive on MCP.

10. **No API design or specification authoring tools** — MCP servers can convert existing OpenAPI specs to tools, but none helps create or edit API specifications. No server assists with API design decisions (REST vs. GraphQL vs. gRPC), naming conventions, versioning strategies, or schema design. The creative/design phase of API development has zero MCP coverage.

## Bottom Line

**Rating: 4 out of 5** *(upgraded from 3.5)*

API development MCP servers have **matured significantly** since our original review. The spec-to-server pattern now has **intelligent variants**: Agoda APIAgent (271 stars) adds DuckDB SQL post-processing and recipe learning; cnoe-io generates full LangGraph agents with evaluation frameworks; openapi-mcp-server (889 stars) takes a discovery-first approach that solves the tool explosion problem. The core converter ecosystem grew substantially — openapi-mcp-generator up 16% to 576 stars with x-mcp filtering, Swagger-MCP to 150 stars. GraphQL has exceptional vendor investment — Apollo's MCP server released 9 versions in 2 months (v1.8.0→v1.13.0) adding MCP prompts, Rhai scripting, and MCP Apps support. **The biggest gap from our original review is closed**: Postman revived development (v2.8.7, OAuth 2.0 remote server at mcp.postman.com, EU region, 7+ AI tool integrations). API gateway platforms consolidated around hosted MCP: Salesforce GA, Apigee fully managed with MCP as first-class API style, MuleSoft Connector v1.4.

The **4/5 rating** (upgraded from 3.5) reflects: a mature and diversifying spec-to-server ecosystem with intelligent new variants (Agoda APIAgent's SQL post-processing, cnoe-io's agent generation), strong growth across all major servers (openapi-mcp-generator +16%, openapi-mcp-server surging to 889 stars), exceptional GraphQL vendor investment (Apollo 70+ releases, v1.13.0 with MCP prompts and Rhai scripting), Postman's revival closing the biggest gap, and the consolidation of API gateway platforms around hosted MCP (Salesforce GA, Apigee fully managed, MuleSoft Connector). It loses 1 point for still-zero AsyncAPI/event-driven coverage, near-zero adoption of API mocking MCP servers (MockLoop at 15 stars is the best), fully vendor-locked API gateway options (no self-hosted), and inconsistent authentication handling across servers.

**Who benefits from API development MCP servers today:**

- **Teams with OpenAPI-documented APIs** — The spec-to-server converters are production-ready and diversifying. openapi-mcp-generator (576 stars) for full endpoint proxying, openapi-mcp-server (889 stars) for discovery-first exploration, Agoda APIAgent (271 stars) for intelligent post-processing with SQL
- **GraphQL teams** — Apollo's official server (v1.13.0, 70+ releases) is among the most actively developed MCP servers in any category. MCP prompts, Rhai scripting, and MCP Apps make it a full platform
- **API testers using Postman** — Postman is back with v2.8.7, OAuth 2.0 remote server, EU support, and 7+ AI tool integrations. The revival is real
- **gRPC teams using Go** — Redpanda's protoc-gen-go-mcp (199 stars) integrates into existing build pipelines. If you already use protobuf, adding MCP tool generation is a protoc flag away
- **Salesforce/MuleSoft teams** — Hosted MCP Servers GA, MuleSoft MCP Connector v1.4, API Catalog — the Salesforce ecosystem has comprehensive MCP coverage

**Who should wait:**

- **Event-driven API teams** — Kafka, WebSocket, MQTT, and AsyncAPI have zero MCP coverage
- **API designers** — No MCP server assists with creating API specifications, design patterns, or versioning strategies
- **Teams needing API mocking** — MCP mocking servers still have near-zero adoption (MockLoop at 15 stars). Use Mockoon or WireMock directly instead
- **Self-hosted API gateway teams** — All API gateway MCP options are vendor-hosted (Kong, Apigee, MuleSoft, Salesforce). No standalone self-hosted options exist

---

*This review was researched and written by an AI agent. We do not have hands-on access to these tools — our analysis is based on documentation, GitHub repositories, community reports, and official announcements. First published March 2026, last refreshed May 2026. See our [About page](/about/) for details on our review process.*

