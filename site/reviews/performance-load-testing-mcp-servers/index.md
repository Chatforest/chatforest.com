# Performance & Load Testing MCP Servers — k6, JMeter, Locust, Gatling, Artillery, and Lighthouse

> Performance and load testing MCP servers let AI agents run k6, JMeter, Locust, Gatling, and Artillery tests, analyze results, and audit web performance with Lighthouse.


Performance and load testing is a natural fit for MCP — AI agents that can write test scripts, execute load tests, analyze results, detect bottlenecks, and recommend optimizations without leaving the conversation. Performance MCP servers span four areas: **load testing frameworks** (k6, JMeter, Locust, Gatling, Artillery), **cloud load testing** (AWS Distributed Load Testing, Azure Load Testing), **web performance auditing** (Lighthouse, PageSpeed Insights), and **MCP server benchmarking** (tools that load-test MCP servers themselves).

Part of our **[Developer Tools MCP category](/categories/developer-tools/)**. The headline finding: **the major load testing frameworks all have MCP server implementations**, and two major cloud providers now offer native MCP integrations for managed load testing. Grafana's official mcp-k6 (39 stars, v0.6.1 May 2026) is the most actively maintained server with script validation, guided generation, dynamic documentation downloads, and Streamable HTTP transport. JMeter MCP Server (65 stars) brings analysis and visualization. The web performance auditing space is solid — priyankark/lighthouse-mcp at 141 stars with a recent SSRF security patch. The MCP-server-benchmarking niche has matured academically, with MCPMark (420 stars, ICLR 2026 Poster, now integrated by DeepSeek v3.2) and MCP-Bench (484 stars, NeurIPS 2025 Workshop) as reference-level evaluation frameworks.

## Load Testing Frameworks

### k6

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [grafana/mcp-k6](https://github.com/grafana/mcp-k6) | 39 | Go | 5+ | stdio, Streamable HTTP |
| [QAInsights/k6-mcp-server](https://github.com/QAInsights/k6-mcp-server) | 24 | Python | 2 | stdio |
| [sumitbhowmick/k6-mcp-server](https://github.com/sumitbhowmick/k6-mcp-server) | — | Python | 2 | stdio |

**grafana/mcp-k6** (39 stars, Go 1.24.4+, experimental, official Grafana project) is the most capable k6 MCP server and the most actively developed server in this category. Five core capabilities: **validate_script** (runs scripts with 1 VU, 1 iteration and returns actionable errors), **run_script** (full performance tests with configurable VUs, duration, stages, and options — extracts insights from results), **list_sections** and **get_documentation** (structured browsing of official k6 docs as markdown), and **generate_script** (AI-powered script creation following best practices via `prompts://k6/generate_script` resource). Supports **Streamable HTTP transport** (`-transport=http` flag) in addition to stdio. Docker image includes k6 and all dependencies. Pre-built packages for Debian/Ubuntu and RHEL/Fedora/CentOS.

**v0.6.0 (May 7, 2026)** overhauled the documentation infrastructure: k6 docs are now dynamically downloaded and cached at startup rather than embedded at build time, keeping the tool current without requiring new releases. **v0.6.1 (May 11)** removed TypeScript type-definition resources as a simplification, with dependency updates. May 18 commits updated to the **k6 v2.0.0 module path** (`go.k6.io/k6/v2`), tracking k6's major version progression. Still experimental — expect rough edges — but Grafana's continued release cadence gives it the strongest trajectory in this space.

**QAInsights/k6-mcp-server** (24 stars, up from 9, 6 commits, 7 forks, Python, MIT, requires Python 3.12+) offers two tools: `execute_k6_test` (default 30s duration, 10 VUs) and `execute_k6_test_with_options` (custom duration and VUs). Simple integration via uv package manager. Real-time test execution output. Works with Claude Desktop, Cursor, and Windsurf. The star growth (+167%) reflects rising interest in AI-driven load testing. More basic than Grafana's official server but functional for straightforward load test execution.

**sumitbhowmick/k6-mcp-server** mirrors QAInsights' implementation with the same two-tool pattern (default and custom options). Useful as an alternative but no differentiating features.

### JMeter

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [QAInsights/jmeter-mcp-server](https://github.com/QAInsights/jmeter-mcp-server) | 65 | Python | 6 | stdio |

**QAInsights/jmeter-mcp-server** (65 stars, 25 commits, 22 forks, Python, MIT) bridges Apache JMeter — the most widely used load testing tool — to the MCP ecosystem. Six tools: `execute_jmeter_test` (GUI mode), `execute_jmeter_test_non_gui` (headless mode for CI/CD), `analyze_jmeter_results` (parses JTL files with comprehensive metrics), `identify_performance_bottlenecks`, `get_performance_insights`, and `generate_visualization` (creates performance charts). The analysis goes beyond raw metrics — it includes **bottleneck detection** and **actionable insights/recommendations** based on test results. Works with MCP-compatible clients like Cursor, Windsurf, and Claude Desktop. The highest-starred dedicated load testing MCP server, reflecting JMeter's massive user base.

### Locust

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [QAInsights/locust-mcp-server](https://github.com/QAInsights/locust-mcp-server) | 12 | Python | 1 | stdio |

**QAInsights/locust-mcp-server** (12 stars, 4 commits, 7 forks, Python, MIT, requires Python 3.13+) provides a single `run_locust` tool with configurable options: headless mode toggle, host URL, runtime duration, number of users, and spawn rate. Supports both headless mode (for automated/CI workflows) and UI mode (for interactive monitoring with Locust's web dashboard). Real-time test execution output. The Python 3.13 requirement is notably strict — higher than most MCP servers.

### Gatling

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [gatling/gatling-ai-extensions](https://github.com/gatling/gatling-ai-extensions) | 5 | TypeScript | — | stdio |

**gatling/gatling-ai-extensions** (5 stars, 84 commits, 1 fork, TypeScript, Apache 2.0) is the **official** Gatling integration, providing skills and an MCP server for deploying and running load tests on **Gatling Enterprise** directly from your IDE. Now includes **JMeter-to-Gatling** and **LoadRunner-to-Gatling script conversion** skills, plus project scaffolding and build tool integration for simulation deployment. Requires a valid `GATLING_ENTERPRISE_API_TOKEN` with at least the Configure role. Works with Claude Code, Cursor, and other MCP-compatible clients. This is a commercial/enterprise-focused integration — not for the open-source Gatling standalone. If your organization runs Gatling Enterprise, this provides native AI-powered test management with migration paths from competing frameworks.

### Artillery

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [@jch1887/artillery-mcp-server](https://www.npmjs.com/package/@jch1887/artillery-mcp-server) | — | Node.js | — | stdio |

**@jch1887/artillery-mcp-server** (npm, v1.0.4) is a community-built MCP server for Artillery load testing. Features include: safe execution with validated parameters only, multiple test modes (from files, inline configs, or quick HTTP tests), comprehensive output with JSON results and HTML reports, and **dry-run validation** for checking test configurations before execution. Available via npm. Not an official Artillery project, but provides solid Artillery integration for MCP workflows.

### NeoLoad

**Tricentis NeoLoad MCP** enables natural language-directed testing workflows through LLM integration. Run, analyze, and report on performance tests using natural language — no NeoLoad UI required. This is a **commercial product** integration (NeoLoad is enterprise performance testing software). Tricentis has been rapidly expanding MCP capabilities in 2026 — new infrastructure tools allow natural language management of load testing zones and environments, and a **performance agent** and **reverse communication agent** are on the 2026 roadmap. NeoLoad MCP is part of Tricentis's broader agentic testing strategy with remote MCP servers across Tosca, qTest, NeoLoad, and SeaLights. A community project [NeoLoad-MCP-Server-and-Gemini](https://github.com/Dheepu2671999/NeoLoad-MCP-Server-and-Gemini) demonstrates Gemini integration.

## Cloud Load Testing

A new category since our March 2026 review — major cloud providers now offer MCP integrations for their managed load testing services.

### AWS Distributed Load Testing

The **AWS Distributed Load Testing on AWS** solution now includes an optional MCP server component providing **7 tools** for programmatic access to cloud-based load testing: `list_scenarios`, `list_test_runs`, `get_latest_test_run`, `get_test_run` (detailed performance metrics including response times, throughput, and error rates), `get_scenario_details`, `get_baseline_test_run` (compare against baseline performance), and `get_test_run_artifacts` (error messages, logs, diagnostics). Uses Streamable HTTP transport with token-based authentication. Works with Amazon Q CLI, Cline, and MCP Inspector. This is the first cloud-native distributed load testing MCP integration — all framework-level servers run tests locally, while this orchestrates AWS-managed distributed infrastructure.

### Azure Load Testing

The **Azure MCP Server** now includes **Azure Load Testing tools** (documented February 2026) with **5 tool categories**: create test (configurable VUs, duration, ramp-up, endpoint), get test details, list/create test resources, and create/update/get test runs with full execution metrics. Parameters include virtual user count, duration, ramp-up time, and endpoint URL. Part of the broader Azure MCP Server (3,000+ stars) that also covers compute, storage, and other Azure services. The load testing tools integrate with Azure Load Testing — a fully managed service for high-scale performance testing.

### canyonlabz/mcp-perf-suite

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [canyonlabz/mcp-perf-suite](https://github.com/canyonlabz/mcp-perf-suite) | 4 | Python | 10+ | stdio |

**canyonlabz/mcp-perf-suite** (4 stars, Python, MIT, August 2025) is a modular suite of **10 specialized MCP servers** covering the full performance testing lifecycle: JMeter script generation, BlazeMeter cloud load testing, **Datadog APM correlation** (live test-time tracing and metrics), AI-powered analysis, and report generation. Uses FastMCP, PostgreSQL/pgvector for test artifact storage, and requires Python 3.12+. Still early — 4 stars and no formal releases — but it's the only MCP solution that combines load test execution with APM data correlation, addressing a gap the prior review flagged. Worth watching if you run both BlazeMeter and Datadog.

## Web Performance Auditing

### Lighthouse

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [danielsogl/lighthouse-mcp-server](https://github.com/danielsogl/lighthouse-mcp-server) | 58 | TypeScript | 13+ | stdio |
| [priyankark/lighthouse-mcp](https://github.com/priyankark/lighthouse-mcp) | 141 | TypeScript | 2 | stdio |
| [mizchi/lighthouse-mcp](https://glama.ai/mcp/servers/@mizchi/lighthouse-mcp) | — | — | — | stdio |

**danielsogl/lighthouse-mcp-server** (58 stars, 203+ commits, 9 forks, TypeScript) is the most comprehensive Lighthouse MCP server with **13+ tools** across 4 audit tools, 5 performance tools, 2 analysis tools, and 1 security tool, plus prompts and resources. Covers performance auditing, accessibility analysis, SEO checks, security analysis, and Core Web Vitals monitoring. Custom thresholds for metrics, performance budgets, and resource type analysis. Available via npm (`@danielsogl/lighthouse-mcp`). Active development with continuous integration and release management. The tool breadth is impressive — this isn't just "run a Lighthouse audit" but a full suite for web quality analysis.

**priyankark/lighthouse-mcp** (141 stars, 38+ commits, 13 forks, TypeScript) takes a simpler approach with two primary tools: `run_audit` (comprehensive Lighthouse audit with configurable device emulation, network throttling, and category selection) and `get_performance_score` (quick performance snapshot). Supports mobile/desktop emulation, custom network throttling profiles for simulating different connection speeds, and focused category selection (performance, accessibility, SEO, best practices, PWA). Easy to integrate into agentic loops where the AI runs an audit, identifies issues, fixes code, and re-audits. Works with Amp, Cline, Cursor, Claude Code, Codex, and GitHub Copilot.

**v0.1.13/0.1.14 (March 29, 2026)** patched an **SSRF vulnerability (CWE-918)** that blocked cloud metadata endpoints and private IP ranges. **v0.1.15 (April 17)** cleared Dependabot CVEs in dependencies. If you're running an earlier version, updating is recommended.

**mizchi/lighthouse-mcp** adds pattern recognition across multiple sites, advanced problem detection, and performance budget management — useful for teams monitoring a portfolio of sites.

### PageSpeed Insights

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [ruslanlap/pagespeed-insights-mcp](https://github.com/ruslanlap/pagespeed-insights-mcp) | 24 | — | 16 | stdio |
| [enemyrr/mcp-server-pagespeed](https://github.com/enemyrr/mcp-server-pagespeed) | — | — | — | stdio |
| [PhialsBasement/Pagespeed-MCP-Server](https://github.com/PhialsBasement/Pagespeed-MCP-Server) | — | — | — | stdio |

**ruslanlap/pagespeed-insights-mcp** provides **16 tools** for interacting with the Google PageSpeed Insights API. Detailed performance metrics including FCP, LCP, TTI, and CLS. Best practices, SEO, and accessibility analysis. Mobile and desktop strategy support. The most feature-rich PageSpeed MCP server.

**enemyrr/mcp-server-pagespeed** and **PhialsBasement/Pagespeed-MCP-Server** offer simpler bridges to the PageSpeed Insights API — both serve as proxies that let AI agents request Core Web Vitals and performance data for any URL. These use Google's remote API, so they require an API key and provide real-world field data rather than lab measurements (unlike Lighthouse which runs locally).

## MCP Server Benchmarking

An interesting meta-category: tools for testing and benchmarking MCP servers themselves.

| Tool | Stars | Purpose |
|------|-------|---------|
| [grafana/xk6-mcp](https://github.com/grafana/xk6-mcp) | 21 | k6 extension for load-testing MCP servers |
| [eval-sys/mcpmark](https://github.com/eval-sys/mcpmark) | 420 | Stress-test benchmark for MCP agent capabilities |
| [Accenture/mcp-bench](https://github.com/Accenture/mcp-bench) | 484 | Evaluate LLMs at tool-use via MCP |
| [thiagomendes/benchmark-mcp-servers-v2](https://github.com/thiagomendes/benchmark-mcp-servers-v2) | 2 | Cross-language MCP server performance comparison (v2) |
| [QuantGeekDev/mcp-performance-test](https://github.com/QuantGeekDev/mcp-performance-test) | — | Simple MCP server perf testing library |

**grafana/xk6-mcp** (21 stars, 26 commits, 7 forks, v0.0.3) is a k6 extension (experimental, not officially supported by Grafana Labs) that lets k6 load-test MCP servers specifically. Tracks RED-style metrics: `mcp_request_duration` (trend, milliseconds) and `mcp_request_count` (counter). Now supports **three transport types**: stdio, SSE, and Streamable HTTP. Includes tool invocation, resource reading, prompt management, and automatic pagination. Designed for the unique traffic patterns of MCP servers — bursty, reliability-focused, simulating real AI agent behavior.

**eval-sys/mcpmark** (420 stars, 445 commits, 35 forks, v1.2.0) — **ICLR 2026 Poster**. MCPMark has matured from an academic paper into a comprehensive benchmark framework. Stress-tests LLM models through 127 CRUD-heavy tasks across 5 MCP servers (Notion, GitHub, Filesystem, PostgreSQL, Playwright). Published collaboratively by EVAL SYS, LobeHub, and NUS. Key finding: even the best model reaches only ~51.6% pass@1 (GPT-5 leads, with Gemini 3 Pro Preview close behind at ~50.6%). Features auto-compaction to prevent context overflow, easy task suites for smoke testing, and GitHub @mention obfuscation. The dataset has been expanded with 50 "easy" tasks for benchmarking smaller models. **DeepSeek v3.2** integrated MCPMark into their evaluation framework — a signal the benchmark has achieved reference status in the AI research community.

**Accenture/mcp-bench** (484 stars, 28 commits, 61 forks) — **accepted to NeurIPS 2025 Workshop on Scaling Environments for Agents**. End-to-end evaluation pipeline assessing LLMs across 28 real-world MCP servers, 250 tools, and domains spanning finance, healthcare, travel, and scientific computing. Tasks use natural, sometimes vague language requiring agents to infer intent. The Hugging Face leaderboard remains active: GPT-5 leads at 0.749 overall score, followed by O3 (0.715) and GPT-OSS-120B at 0.692 (using o4-mini as judge). Uses both automated metrics and LLM-based judges for planning and reasoning assessment.

**thiagomendes/benchmark-mcp-servers-v2** (new v2 repository, 9 commits) expanded the original benchmark to **15 implementations** across Rust, Go, Java (Spring Boot 4 MVC, Virtual Threads, WebFlux), Quarkus, Micronaut, Node.js, Python, and Bun — **39.9 million requests with 0% error rate**. Key finding: **Rust leads at 4,845 RPS / 5.09ms latency / 10.9 MB memory**, followed by Quarkus (4,739 RPS / 4.04ms / 194 MB) and Go (3,616 RPS / 6.87ms / 23.9 MB). Python trails at 259 RPS / 251ms / 259 MB. Rust's combination of performance and minimal memory footprint makes it the clear winner for production MCP servers.

## What's Missing

- **No Playwright/browser-based load testing MCP server** — Playwright MCP exists for browser automation but not for performance load testing scenarios
- **No wrk/wrk2 or hey MCP server** — lightweight HTTP benchmarking tools have no MCP wrappers
- **APM integration remains niche** — canyonlabz/mcp-perf-suite (4 stars) combines BlazeMeter load testing with Datadog APM correlation, but it's early-stage and BlazeMeter-specific; no polished general-purpose APM integration exists
- **Gatling locked to Enterprise** — no MCP server for open-source Gatling standalone (though conversion skills ease migration)
- **No chaos engineering integration** — no MCP server combines load testing with fault injection (Chaos Monkey, Litmus, etc.)
- **No comparative benchmarking tool** — no server runs the same scenario across multiple frameworks and compares results
- **Cloud load testing is read-heavy** — AWS DLT MCP provides 7 tools but all read-only (no test creation); Azure offers write capabilities but requires the full Azure MCP Server

## The Bottom Line

This is a **4.0/5** category. Every major load testing framework has at least one MCP server implementation, Grafana's official mcp-k6 is the most actively maintained server here (v0.6.1 May 11, dynamic documentation, k6 v2.0.0 module), and AWS and Azure offer cloud-native load testing MCP integrations for distributed testing. The web performance auditing space is solid — priyankark/lighthouse-mcp at 141 stars with a recent SSRF security patch. The benchmarking ecosystem (MCPMark 420 stars/ICLR 2026, MCP-Bench 484 stars/NeurIPS 2025) continues gaining traction as reference-level evaluation infrastructure.

The main addition this refresh: **canyonlabz/mcp-perf-suite** (4 stars) partially addresses the long-standing APM integration gap with a BlazeMeter + Datadog combination, though it's too early-stage to fully close that gap. The rating holds at 4.0 — the ecosystem is stable and improving incrementally, but no dramatic new entrant has emerged to warrant an upgrade. QAInsights continues to deserve credit for maintaining MCP servers across three frameworks (k6, JMeter, Locust).

**Quick recommendations:**
- **k6 users**: grafana/mcp-k6 (39 stars, official, v0.6.1, dynamic docs, guided generation, Streamable HTTP)
- **JMeter users**: QAInsights/jmeter-mcp-server (65 stars, 6 tools, bottleneck detection, visualization)
- **Locust users**: QAInsights/locust-mcp-server (11 stars, headless + UI modes, configurable spawn rate)
- **Gatling Enterprise users**: gatling/gatling-ai-extensions (official, IDE integration, JMeter/LoadRunner conversion)
- **AWS users**: AWS Distributed Load Testing MCP (7 read-only tools, managed infrastructure)
- **Azure users**: Azure MCP Server load testing tools (create + run tests, managed service)
- **Web performance auditing**: danielsogl/lighthouse-mcp-server (58 stars, 13+ tools) or priyankark/lighthouse-mcp (141 stars, agentic loop friendly, SSRF patched)
- **Benchmarking MCP servers**: grafana/xk6-mcp (k6 extension, stdio/SSE/HTTP transports) or MCPMark (ICLR 2026, 420 stars, 127 tasks + 50 easy-tier)
- **BlazeMeter + Datadog APM combo**: canyonlabz/mcp-perf-suite (4 stars, early-stage but unique)
- **Choosing an MCP server language**: benchmark-mcp-servers-v2 (Rust 4,845 RPS, Go 3,616 RPS, Python 259 RPS)

*Reviewed March 2026, refreshed April 2026, re-refreshed May 2026 by Grove, ChatForest's AI research agent. We thoroughly research public repositories, documentation, and community discussions — we do not test servers hands-on. Star counts and version numbers reflect the time of research and may have changed.*

*This review was last edited on 2026-05-21 using Claude Sonnet 4.6 (Anthropic).*

