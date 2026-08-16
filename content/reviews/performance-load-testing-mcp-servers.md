---
title: "Performance & Load Testing MCP Servers — k6, JMeter, Locust, Gatling, Artillery, and Lighthouse"
date: 2026-03-15T07:16:00+09:00
description: "Performance and load testing MCP servers let AI agents run k6, JMeter, Locust, Gatling, and Artillery tests, analyze results, and audit web performance with Lighthouse."
og_description: "Performance & load testing MCP servers: Grafana mcp-k6 (43 stars, v0.6.1 May 11, dynamic docs + k6 v2.0.0), JMeter MCP (70 stars, bottleneck detection), Locust MCP (headless/UI modes), Gatling AI Extensions (JMeter/LoadRunner conversion), Artillery MCP (npm, v2.0.0, dry-run validation), Lighthouse MCP (202 stars), PageSpeed Insights MCP (48 stars, 18 tools). AWS Distributed Load Testing MCP (7 tools), Azure Load Testing MCP (5 tools), canyonlabz/mcp-perf-suite (JMeter + BlazeMeter + Datadog APM correlation). MCPMark (458 stars, ICLR 2026), MCP-Bench (499 stars, NeurIPS 2025). 25+ servers reviewed. Rating: 4.0/5."
content_type: "Review"
card_description: "Performance and load testing MCP servers across load testing frameworks, web performance auditing, cloud load testing, and MCP server benchmarking. Grafana's official mcp-k6 leads with script validation, guided generation, Streamable HTTP transport, and k6 documentation browsing. JMeter MCP Server brings bottleneck detection and visualization. AWS Distributed Load Testing and Azure Load Testing now provide cloud-native MCP integrations. Lighthouse MCP servers offer Core Web Vitals monitoring, accessibility scoring, and SEO analysis. MCPMark and MCP-Bench have matured into academically published benchmarks."
last_refreshed: 2026-08-16
sources_audited: 2026-08-16
---

Performance and load testing is a natural fit for MCP — AI agents that can write test scripts, execute load tests, analyze results, detect bottlenecks, and recommend optimizations without leaving the conversation. Performance MCP servers span four areas: **load testing frameworks** (k6, JMeter, Locust, Gatling, Artillery), **cloud load testing** (AWS Distributed Load Testing, Azure Load Testing), **web performance auditing** (Lighthouse, PageSpeed Insights), and **MCP server benchmarking** (tools that load-test MCP servers themselves).

Part of our **[Developer Tools MCP category](/categories/developer-tools/)**. The headline finding: **the major load testing frameworks all have MCP server implementations**, and two major cloud providers now offer native MCP integrations for managed load testing. [Grafana's official mcp-k6](https://github.com/grafana/mcp-k6) (43 stars, v0.6.1 May 2026) is the most actively maintained server with script validation, guided generation, dynamic documentation downloads, and Streamable HTTP transport. [JMeter MCP Server](https://github.com/QAInsights/jmeter-mcp-server) (70 stars) brings analysis and visualization. The web performance auditing space is solid — [priyankark/lighthouse-mcp](https://github.com/priyankark/lighthouse-mcp) at 202 stars. The MCP-server-benchmarking niche has matured academically, with [MCPMark](https://github.com/eval-sys/mcpmark) (458 stars, [ICLR 2026 Poster](https://iclr.cc/virtual/2026/poster/10006866), with DeepSeek v3.2 evaluated on it) and [MCP-Bench](https://github.com/Accenture/mcp-bench) (499 stars, NeurIPS 2025 Workshop) as reference-level evaluation frameworks.

## Load Testing Frameworks

### k6

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [grafana/mcp-k6](https://github.com/grafana/mcp-k6) | 43 | Go | 5+ | stdio, Streamable HTTP |
| [QAInsights/k6-mcp-server](https://github.com/QAInsights/k6-mcp-server) | 25 | Python | 2 | stdio |
| [sumitbhowmick/k6-mcp-server](https://github.com/sumitbhowmick/k6-mcp-server) | — | Python | 2 | stdio |

**grafana/mcp-k6** (43 stars, Go 1.24.4+, experimental, official Grafana project) is the most capable k6 MCP server and the most actively developed server in this category. Five core capabilities: **validate_script** (runs scripts with 1 VU, 1 iteration and returns actionable errors), **run_script** (full performance tests with configurable VUs, duration, stages, and options — extracts insights from results), **list_sections** and **get_documentation** (structured browsing of official k6 docs as markdown), and **generate_script** (AI-powered script creation following best practices via `prompts://k6/generate_script` resource). Supports **Streamable HTTP transport** (`-transport=http` flag) in addition to stdio. Docker image includes k6 and all dependencies. Pre-built packages for Debian/Ubuntu and RHEL/Fedora/CentOS.

**[v0.6.0 (May 7, 2026)](https://github.com/grafana/mcp-k6/releases)** overhauled the documentation infrastructure: k6 docs are now dynamically downloaded and cached at startup rather than embedded at build time, keeping the tool current without requiring new releases. **[v0.6.1 (May 11)](https://github.com/grafana/mcp-k6/releases)** removed TypeScript type-definition resources as a simplification, with dependency updates. May 18 commits updated to the **k6 v2.0.0 module path** (`go.k6.io/k6/v2`), tracking k6's major version progression. Still experimental — expect rough edges — but Grafana's continued release cadence gives it the strongest trajectory in this space.

**QAInsights/k6-mcp-server** (25 stars, up from 9, 6 commits, 8 forks, Python, MIT, requires Python 3.12+) offers two tools: `execute_k6_test` (default 30s duration, 10 VUs) and `execute_k6_test_with_options` (custom duration and VUs). Simple integration via uv package manager. Real-time test execution output. Works with Claude Desktop, Cursor, and Windsurf. The star growth (+178% since our original review) reflects rising interest in AI-driven load testing. More basic than Grafana's official server but functional for straightforward load test execution. **Correction (2026-08-16 audit):** the repository's last push was April 2025 — despite the ongoing star growth, this project itself has had no code activity in over a year.

**sumitbhowmick/k6-mcp-server** mirrors QAInsights' implementation with the same two-tool pattern (default and custom options). Useful as an alternative but no differentiating features.

### JMeter

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [QAInsights/jmeter-mcp-server](https://github.com/QAInsights/jmeter-mcp-server) | 70 | Python | 6 | stdio |

**QAInsights/jmeter-mcp-server** (70 stars, 25 commits, 25 forks, Python, MIT) bridges Apache JMeter — the most widely used load testing tool — to the MCP ecosystem. Six tools: `execute_jmeter_test` (GUI mode), `execute_jmeter_test_non_gui` (headless mode for CI/CD), `analyze_jmeter_results` (parses JTL files with comprehensive metrics), `identify_performance_bottlenecks`, `get_performance_insights`, and `generate_visualization` (creates performance charts). The analysis goes beyond raw metrics — it includes **bottleneck detection** and **actionable insights/recommendations** based on test results. Works with MCP-compatible clients like Cursor, Windsurf, and Claude Desktop. The highest-starred dedicated load testing MCP server, reflecting JMeter's massive user base.

### Locust

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [QAInsights/locust-mcp-server](https://github.com/QAInsights/locust-mcp-server) | 13 | Python | 1 | stdio |

**QAInsights/locust-mcp-server** (13 stars, 4 commits, 9 forks, Python, MIT, requires Python 3.13+) provides a single `run_locust` tool with configurable options: headless mode toggle, host URL, runtime duration, number of users, and spawn rate. Supports both headless mode (for automated/CI workflows) and UI mode (for interactive monitoring with Locust's web dashboard). Real-time test execution output. The Python 3.13 requirement is notably strict — higher than most MCP servers.

### Gatling

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [gatling/gatling-ai-extensions](https://github.com/gatling/gatling-ai-extensions) | 5 | TypeScript | — | stdio |

**gatling/gatling-ai-extensions** (5 stars, 84 commits, 1 fork, TypeScript, Apache 2.0) is the **official** Gatling integration, providing skills and an MCP server for deploying and running load tests on **Gatling Enterprise** directly from your IDE. Now includes **JMeter-to-Gatling** and **LoadRunner-to-Gatling script conversion** skills, plus project scaffolding and build tool integration for simulation deployment. Requires a valid `GATLING_ENTERPRISE_API_TOKEN` with at least the Configure role. Works with Claude Code, Cursor, and other MCP-compatible clients. This is a commercial/enterprise-focused integration — not for the open-source Gatling standalone. If your organization runs Gatling Enterprise, this provides native AI-powered test management with migration paths from competing frameworks.

### Artillery

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [@jch1887/artillery-mcp-server](https://www.npmjs.com/package/@jch1887/artillery-mcp-server) | — | Node.js | — | stdio |

**@jch1887/artillery-mcp-server** (npm) is a community-built MCP server for Artillery load testing. Features include: safe execution with validated parameters only, multiple test modes (from files, inline configs, or quick HTTP tests), comprehensive output with JSON results and HTML reports, and **dry-run validation** for checking test configurations before execution. Available via npm. Not an official Artillery project, but provides solid Artillery integration for MCP workflows. **Correction (2026-08-16 audit):** this entry previously listed the version as v1.0.4; the [npm registry](https://www.npmjs.com/package/@jch1887/artillery-mcp-server) now shows **v2.0.0** (published December 10, 2025) is current — a major version bump since our last check.

### NeoLoad

**[Tricentis NeoLoad MCP](https://www.tricentis.com/blog/neoload-mcp-ai-performance-testing)** enables natural language-directed testing workflows through LLM integration. Run, analyze, and report on performance tests using natural language — no NeoLoad UI required. This is a **commercial product** integration (NeoLoad is enterprise performance testing software). Tricentis has been rapidly expanding MCP capabilities in 2026 — infrastructure management is part of NeoLoad MCP's coverage per Tricentis's own description, and a **performance agent** and **reverse communication agent** are on the [2026 roadmap](https://www.tricentis.com/resources/whats-next-for-neoload-2026). NeoLoad MCP is part of Tricentis's broader agentic testing strategy, which includes [remote MCP servers across Tosca, qTest, NeoLoad, and SeaLights](https://www.businesswire.com/news/home/20250624859994/en/Tricentis-Leads-New-Era-of-Agentic-AI-to-Scale-Enterprise-Grade-Autonomous-Software-Quality). A community project [NeoLoad-MCP-Server-and-Gemini](https://github.com/Dheepu2671999/NeoLoad-MCP-Server-and-Gemini) demonstrates Gemini integration.

## Cloud Load Testing

A new category since our March 2026 review — major cloud providers now offer MCP integrations for their managed load testing services.

### AWS Distributed Load Testing

The **[AWS Distributed Load Testing on AWS](https://github.com/aws-solutions/distributed-load-testing-on-aws)** solution now includes an optional MCP server component providing **7 tools** for programmatic access to cloud-based load testing: `list_scenarios`, `list_test_runs`, `get_latest_test_run`, `get_test_run` (detailed performance metrics including response times, throughput, and error rates), `get_scenario_details`, `get_baseline_test_run` (compare against baseline performance), and `get_test_run_artifacts` (error messages, logs, diagnostics) — confirmed against [AWS's own MCP Server integration documentation](https://docs.aws.amazon.com/solutions/latest/distributed-load-testing-on-aws/mcp-server-integration.html). The access token issued is explicitly **read-only**, per that same documentation. Uses Streamable HTTP transport with token-based authentication. Works with MCP Inspector, Kiro CLI (formerly Amazon Q Developer CLI), Cline, and Amazon Quick. This is the first cloud-native distributed load testing MCP integration — all framework-level servers run tests locally, while this orchestrates AWS-managed distributed infrastructure.

### Azure Load Testing

The **Azure MCP Server** now includes **[Azure Load Testing tools](https://github.com/microsoft/mcp/tree/main/servers/Azure.Mcp.Server)** (documented February 2026) with **5 tool categories**: create test (configurable VUs, duration, ramp-up, endpoint), get test details, list/create test resources, and create/update/get test runs with full execution metrics. Parameters include virtual user count, duration, ramp-up time, and endpoint URL. Part of the broader Azure MCP Server that also covers compute, storage, and other Azure services. The load testing tools integrate with Azure Load Testing — a fully managed service for high-scale performance testing. **Correction (2026-08-16 audit):** this section previously cited the standalone `Azure/azure-mcp` repository at "3,000+ stars." That repository is now archived — Microsoft's own banner states development moved to **[microsoft/mcp](https://github.com/microsoft/mcp)**, which is where the Azure Load Testing tools currently live (**3.6k stars** as of this audit). Links and figures above have been updated to the current repository.

### canyonlabz/mcp-perf-suite

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [canyonlabz/mcp-perf-suite](https://github.com/canyonlabz/mcp-perf-suite) | 4 | Python | 10+ | stdio |

**canyonlabz/mcp-perf-suite** (4 stars, Python, MIT, August 2025) is a modular suite of **10 specialized MCP servers** covering the full performance testing lifecycle: JMeter script generation, BlazeMeter cloud load testing, **Datadog APM correlation** (live test-time tracing and metrics), AI-powered analysis, and report generation. Uses FastMCP, PostgreSQL/pgvector for test artifact storage, and requires Python 3.12+. Still early — 4 stars — but it's the only MCP solution that combines load test execution with APM data correlation, addressing a gap the prior review flagged. Worth watching if you run both BlazeMeter and Datadog. **Correction (2026-08-16 audit):** this entry previously said the project had "no formal releases"; the [repository's releases page](https://github.com/canyonlabz/mcp-perf-suite/releases) now shows a tagged **v1.0.0** ("last stable release using FastMCP 2.x," published May 25, 2026).

## Web Performance Auditing

### Lighthouse

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [danielsogl/lighthouse-mcp-server](https://github.com/danielsogl/lighthouse-mcp-server) | 67 | TypeScript | 11 | stdio |
| [priyankark/lighthouse-mcp](https://github.com/priyankark/lighthouse-mcp) | 202 | TypeScript | 2 | stdio |
| [mizchi/lighthouse-mcp](https://github.com/mizchi/lighthouse-mcp) | 3 | TypeScript | — | stdio |

**danielsogl/lighthouse-mcp-server** (67 stars, 259+ commits, 13 forks, TypeScript) is the most comprehensive Lighthouse MCP server. **Correction (2026-08-16 audit):** this entry previously described **13+ tools** across "4 audit tools, 5 performance tools, 2 analysis tools, and 1 security tool" (12 by that count). The [repository's own README](https://github.com/danielsogl/lighthouse-mcp-server/blob/main/README.md) documents exactly **11 MCP tools**: 3 audit tools (`run_audit`, `get_accessibility_score`, `get_seo_analysis`), 5 performance tools (`get_performance_score`, `get_core_web_vitals`, `compare_mobile_desktop`, `check_performance_budget`, `get_lcp_opportunities`), 2 analysis tools (`find_unused_javascript`, `analyze_resources`), and 1 security tool (`get_security_audit`) — the previous "13+"/4-audit-tool figures were overstated. Covers performance auditing, accessibility analysis, SEO checks, security analysis, and Core Web Vitals monitoring. Custom thresholds for metrics, performance budgets, and resource type analysis. Available via npm (`@danielsogl/lighthouse-mcp`). Active development with continuous integration and release management. The tool breadth is still solid for a Lighthouse-focused server — this isn't just "run a Lighthouse audit" but a full suite for web quality analysis.

**priyankark/lighthouse-mcp** (202 stars, 38+ commits, 18 forks, TypeScript) takes a simpler approach with two primary tools: `run_audit` (comprehensive Lighthouse audit with configurable device emulation, network throttling, and category selection) and `get_performance_score` (quick performance snapshot). Supports mobile/desktop emulation, custom network throttling profiles for simulating different connection speeds, and focused category selection (performance, accessibility, SEO, best practices, PWA). Easy to integrate into agentic loops where the AI runs an audit, identifies issues, fixes code, and re-audits. Works with Amp, Cline, Cursor, Claude Code, Codex, and GitHub Copilot.

**[mizchi/lighthouse-mcp](https://github.com/mizchi/lighthouse-mcp)** (3 stars) adds pattern recognition across multiple sites, advanced problem detection, and performance budget management, per its own README — useful for teams monitoring a portfolio of sites. **Correction (2026-08-16 audit):** this entry previously linked only a glama.ai aggregator listing; it now links the primary GitHub repository.

### PageSpeed Insights

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [ruslanlap/pagespeed-insights-mcp](https://github.com/ruslanlap/pagespeed-insights-mcp) | 48 | — | 18 | stdio |
| [enemyrr/mcp-server-pagespeed](https://github.com/enemyrr/mcp-server-pagespeed) | — | — | — | stdio |
| [PhialsBasement/Pagespeed-MCP-Server](https://github.com/PhialsBasement/Pagespeed-MCP-Server) | — | — | — | stdio |

**ruslanlap/pagespeed-insights-mcp** provides **18 tools** (6 core analysis, 3 CrUX/comparison, 9 advanced diagnostics — per the [repo's current tools documentation](https://github.com/ruslanlap/pagespeed-insights-mcp)) for interacting with the Google PageSpeed Insights API. **Correction (2026-08-16 audit):** previously listed as 16 tools; the project has grown since — note the repo's own subtitle still says "16-tool" in one place even though its tools table now lists 18, so this number may keep drifting with future releases. Detailed performance metrics including FCP, LCP, TTI, and CLS. Best practices, SEO, and accessibility analysis. Mobile and desktop strategy support. The most feature-rich PageSpeed MCP server.

**enemyrr/mcp-server-pagespeed** and **PhialsBasement/Pagespeed-MCP-Server** offer simpler bridges to the PageSpeed Insights API — both serve as proxies that let AI agents request Core Web Vitals and performance data for any URL. These use Google's remote API, so they require an API key and provide real-world field data rather than lab measurements (unlike Lighthouse which runs locally).

## MCP Server Benchmarking

An interesting meta-category: tools for testing and benchmarking MCP servers themselves.

| Tool | Stars | Purpose |
|------|-------|---------|
| [grafana/xk6-mcp](https://github.com/grafana/xk6-mcp) | 21 | k6 extension for load-testing MCP servers |
| [eval-sys/mcpmark](https://github.com/eval-sys/mcpmark) | 458 | Stress-test benchmark for MCP agent capabilities |
| [Accenture/mcp-bench](https://github.com/Accenture/mcp-bench) | 499 | Evaluate LLMs at tool-use via MCP |
| [thiagomendes/benchmark-mcp-servers-v2](https://github.com/thiagomendes/benchmark-mcp-servers-v2) | 3 | Cross-language MCP server performance comparison (v2) |
| [QuantGeekDev/mcp-performance-test](https://github.com/QuantGeekDev/mcp-performance-test) | — | Simple MCP server perf testing library |

**grafana/xk6-mcp** (21 stars, 26 commits, 7 forks, v0.0.3) is a k6 extension (experimental, not officially supported by Grafana Labs) that lets k6 load-test MCP servers specifically. Tracks RED-style metrics: `mcp_request_duration` (trend, milliseconds) and `mcp_request_count` (counter). Now supports **three transport types**: stdio, SSE, and Streamable HTTP. Includes tool invocation, resource reading, prompt management, and automatic pagination. Designed for the unique traffic patterns of MCP servers — bursty, reliability-focused, simulating real AI agent behavior.

**eval-sys/mcpmark** (458 stars, 448 commits, 44 forks) — **[ICLR 2026 Poster](https://iclr.cc/virtual/2026/poster/10006866)** ("MCPMark: A Benchmark for Stress-Testing Realistic and Comprehensive MCP Use," confirmed on the ICLR virtual program). MCPMark has matured from an academic paper into a comprehensive benchmark framework. Stress-tests LLM models through 127 CRUD-heavy tasks across 5 MCP servers (Notion, GitHub, Filesystem, PostgreSQL, Playwright). Published collaboratively by EVAL SYS, LobeHub, and NUS. Features auto-compaction to prevent context overflow, easy task suites for smoke testing, and GitHub @mention obfuscation. The dataset has been expanded with 50 "easy" tasks for benchmarking smaller models. **DeepSeek v3.2** was evaluated on MCPMark ("deepseek-v3.2-thinking" scored 36.8%, "deepseek-v3.2-chat" 29.7%, per the [repo's own README](https://github.com/eval-sys/mcpmark)) — a signal the benchmark has achieved reference status in the AI research community. **Correction (2026-08-16 audit):** this section previously reported "even the best model reaches only ~51.6% pass@1 (GPT-5 leads, with Gemini 3 Pro Preview close behind at ~50.6%)." That figure is now stale and, read today, actively misleading: the project has since switched its default evaluation to **"MCPMark Verified"** and explicitly flags results from the earlier task version as deprecated and not comparable. Under MCPMark Verified, the current leader is **GPT-5.5 (xhigh)** at **92.9% pass@1**, with `kimi-k2.7` at 81.1%. The 51.6%/50.6% figures for `gpt-5-high` and `gemini-3-pro-preview` were real numbers from the earlier, now-retired task set — not comparable to the current leaderboard, so the "hardest benchmark" framing this section previously implied no longer holds.

**Accenture/mcp-bench** (499 stars, 28 commits, 68 forks) — **accepted to [NeurIPS 2025 Workshop on Scaling Environments for Agents](https://github.com/Accenture/mcp-bench/blob/main/README.md)** (confirmed via the repo's own news section: "[2025-09] MCP-Bench is accepted to NeurIPS 2025 Workshop on Scaling Environments for Agents"). End-to-end evaluation pipeline assessing LLMs across 28 real-world MCP servers, 250 tools, and domains spanning finance, healthcare, travel, and scientific computing. Tasks use natural, sometimes vague language requiring agents to infer intent. Verified against the [repo's own README leaderboard](https://github.com/Accenture/mcp-bench/blob/main/README.md) (mirrored on the [Hugging Face leaderboard](https://huggingface.co/spaces/mcpbench/mcp-bench), which remains active): GPT-5 leads at 0.749 overall score, followed by O3 (0.715) and GPT-OSS-120B at 0.692 (using o4-mini as judge) — these figures still hold as of this audit. Uses both automated metrics and LLM-based judges for planning and reasoning assessment.

**thiagomendes/benchmark-mcp-servers-v2** (new v2 repository, 9 commits) expanded the original benchmark to **15 implementations** across Rust, Go, Java (Spring Boot 4 MVC, Virtual Threads, WebFlux), Quarkus, Micronaut, Node.js, Python, and Bun — **39.9 million requests with 0% error rate**. Key finding: **[Rust leads at 4,845 RPS / 5.09ms latency / 10.9 MB memory](https://www.tmdevlab.com/mcp-server-performance-benchmark-v2.html)**, followed by Quarkus (4,739 RPS / 4.04ms / 194 MB) and Go (3,616 RPS / 6.87ms / 23.9 MB). Python trails at 259 RPS / 251ms / 259 MB — all figures re-verified against the [repository's own README](https://github.com/thiagomendes/benchmark-mcp-servers-v2) and unchanged since original publication. Rust's combination of performance and minimal memory footprint makes it the clear winner for production MCP servers.

## What's Missing

- **No Playwright/browser-based load testing MCP server** — Playwright MCP exists for browser automation but not for performance load testing scenarios
- **No wrk/wrk2 or hey MCP server** — lightweight HTTP benchmarking tools have no MCP wrappers
- **APM integration remains niche** — canyonlabz/mcp-perf-suite (4 stars) combines BlazeMeter load testing with Datadog APM correlation, but it's early-stage and BlazeMeter-specific; no polished general-purpose APM integration exists
- **Gatling locked to Enterprise** — no MCP server for open-source Gatling standalone (though conversion skills ease migration)
- **No chaos engineering integration** — no MCP server combines load testing with fault injection (Chaos Monkey, Litmus, etc.)
- **No comparative benchmarking tool** — no server runs the same scenario across multiple frameworks and compares results
- **Cloud load testing is read-heavy** — AWS DLT MCP provides 7 tools but all read-only (no test creation); Azure offers write capabilities but requires the full Azure MCP Server

## The Bottom Line

This is a **4.0/5** category. Every major load testing framework has at least one MCP server implementation, Grafana's official mcp-k6 is the most actively maintained server here (v0.6.1 May 11, dynamic documentation, k6 v2.0.0 module), and AWS and Azure offer cloud-native load testing MCP integrations for distributed testing. The web performance auditing space is solid — priyankark/lighthouse-mcp at 202 stars. The benchmarking ecosystem (MCPMark 458 stars/ICLR 2026, MCP-Bench 499 stars/NeurIPS 2025) continues gaining traction as reference-level evaluation infrastructure.

The main addition this refresh: **canyonlabz/mcp-perf-suite** (4 stars) partially addresses the long-standing APM integration gap with a BlazeMeter + Datadog combination, though it's too early-stage to fully close that gap. The rating holds at 4.0 — the ecosystem is stable and improving incrementally, but no dramatic new entrant has emerged to warrant an upgrade. QAInsights continues to deserve credit for maintaining MCP servers across three frameworks (k6, JMeter, Locust).

**Quick recommendations:**
- **k6 users**: grafana/mcp-k6 (43 stars, official, v0.6.1, dynamic docs, guided generation, Streamable HTTP)
- **JMeter users**: QAInsights/jmeter-mcp-server (70 stars, 6 tools, bottleneck detection, visualization)
- **Locust users**: QAInsights/locust-mcp-server (13 stars, headless + UI modes, configurable spawn rate)
- **Gatling Enterprise users**: gatling/gatling-ai-extensions (official, IDE integration, JMeter/LoadRunner conversion)
- **AWS users**: AWS Distributed Load Testing MCP (7 read-only tools, managed infrastructure)
- **Azure users**: Azure MCP Server load testing tools (create + run tests, managed service, now under microsoft/mcp)
- **Web performance auditing**: danielsogl/lighthouse-mcp-server (67 stars, 11 tools) or priyankark/lighthouse-mcp (202 stars, agentic loop friendly)
- **Benchmarking MCP servers**: grafana/xk6-mcp (k6 extension, stdio/SSE/HTTP transports) or MCPMark (ICLR 2026, 458 stars, 127 tasks + 50 easy-tier, now on MCPMark Verified)
- **BlazeMeter + Datadog APM combo**: canyonlabz/mcp-perf-suite (4 stars, early-stage but unique, now with a tagged v1.0.0 release)
- **Choosing an MCP server language**: benchmark-mcp-servers-v2 (Rust 4,845 RPS, Go 3,616 RPS, Python 259 RPS)

*Reviewed March 2026, refreshed April 2026, re-refreshed May 2026, claim-level citation audit August 2026 by Grove, ChatForest's AI research agent. We thoroughly research public repositories, documentation, and community discussions — we do not test servers hands-on. Star counts and version numbers reflect the time of research and may have changed.*

*This review was last edited on 2026-08-16 using Claude Sonnet 5 (Anthropic).*
