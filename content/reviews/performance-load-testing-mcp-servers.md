---
title: "Performance & Load Testing MCP Servers — k6, JMeter, Locust, Gatling, Artillery, and Lighthouse"
date: 2026-03-15T07:16:00+09:00
description: "Performance and load testing MCP servers let AI agents run k6, JMeter, Locust, Gatling, and Artillery tests, analyze results, and audit web performance with Lighthouse. We reviewed 20+ servers across load testing frameworks (Grafana mcp-k6, QAInsights JMeter/k6/Locust, Gatling AI Extensions, Artillery MCP), web performance auditing (Lighthouse, PageSpeed Insights), and MCP server benchmarking tools (xk6-mcp, MCPMark, MCP-Bench). Grafana's official mcp-k6 leads with script validation, guided generation, and documentation browsing. JMeter MCP Server (61 stars) brings bottleneck detection and visualization. For web performance, danielsogl/lighthouse-mcp-server offers 13+ audit tools."
og_description: "Performance & load testing MCP servers: Grafana mcp-k6 (official, Go, script validation + guided generation), JMeter MCP (61 stars, bottleneck detection), Locust MCP (headless/UI modes), Gatling AI Extensions (official, Enterprise integration), Artillery MCP (npm, dry-run validation), Lighthouse MCP (13+ audit tools), PageSpeed Insights MCP (16 tools). Plus MCP server benchmarking: xk6-mcp, MCPMark, MCP-Bench. 20+ servers reviewed. Rating: 3.5/5."
content_type: "Review"
card_description: "Performance and load testing MCP servers across load testing frameworks, web performance auditing, and MCP server benchmarking. Grafana's official mcp-k6 leads with script validation, guided generation, and k6 documentation browsing. JMeter MCP Server brings bottleneck detection and visualization to the most popular load testing tool. For web audits, Lighthouse MCP servers offer Core Web Vitals monitoring, accessibility scoring, and SEO analysis. The category also includes tools for benchmarking MCP servers themselves."
last_refreshed: 2026-03-15
---

Performance and load testing is a natural fit for MCP — AI agents that can write test scripts, execute load tests, analyze results, detect bottlenecks, and recommend optimizations without leaving the conversation. Performance MCP servers span three areas: **load testing frameworks** (k6, JMeter, Locust, Gatling, Artillery), **web performance auditing** (Lighthouse, PageSpeed Insights), and **MCP server benchmarking** (tools that load-test MCP servers themselves).

Part of our **[Developer Tools MCP category](/categories/developer-tools/)**. The headline finding: **the major load testing frameworks all have MCP server implementations**, but maturity varies widely. Grafana's official mcp-k6 is the most polished with script validation, guided generation, and documentation browsing. JMeter MCP Server (61 stars) brings analysis and visualization. The web performance auditing space is well-served with multiple Lighthouse and PageSpeed Insights wrappers. The most interesting niche is MCP-server-testing-MCP-servers — Grafana's xk6-mcp extension lets k6 load-test MCP servers directly.

## Load Testing Frameworks

### k6

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [grafana/mcp-k6](https://github.com/grafana/mcp-k6) | — | Go | 5+ | stdio |
| [QAInsights/k6-mcp-server](https://github.com/QAInsights/k6-mcp-server) | ~9 | Python | 2 | stdio |
| [sumitbhowmick/k6-mcp-server](https://github.com/sumitbhowmick/k6-mcp-server) | — | Python | 2 | stdio |

**grafana/mcp-k6** (Go, experimental, official Grafana project) is the most capable k6 MCP server. Five core capabilities: **validate_script** (runs scripts with 1 VU, 1 iteration and returns actionable errors), **run_script** (full performance tests with configurable VUs, duration, stages, and options — extracts insights from results), **list_sections** and **get_documentation** (structured browsing of official k6 docs as markdown), and **AI-powered script generation** with a structured workflow. Docker image includes k6 and all dependencies. Pre-built packages for Debian/Ubuntu and RHEL/Fedora/CentOS. Still experimental — expect rough edges — but the official backing from Grafana gives it the strongest trajectory in this space.

**QAInsights/k6-mcp-server** (9 stars, Python, MIT, requires Python 3.12+) offers two tools: `execute_k6_test` (default 30s duration, 10 VUs) and `execute_k6_test_with_options` (custom duration and VUs). Simple integration via uv package manager. Real-time test execution output. Works with Claude Desktop, Cursor, and Windsurf. More basic than Grafana's official server but functional for straightforward load test execution.

**sumitbhowmick/k6-mcp-server** mirrors QAInsights' implementation with the same two-tool pattern (default and custom options). Useful as an alternative but no differentiating features.

### JMeter

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [QAInsights/jmeter-mcp-server](https://github.com/QAInsights/jmeter-mcp-server) | ~61 | Python | 4+ | stdio |

**QAInsights/jmeter-mcp-server** (61 stars, Python, MIT) bridges Apache JMeter — the most widely used load testing tool — to the MCP ecosystem. Four main tools: `execute_jmeter_test` (GUI mode), `execute_jmeter_test_non_gui` (headless mode for CI/CD), `analyze_jmeter_results` (parses JTL files with comprehensive metrics), and `generate_visualization` (creates performance charts). The analysis goes beyond raw metrics — it includes **bottleneck detection** and **actionable insights/recommendations** based on test results. Works with MCP-compatible clients like Cursor, Windsurf, and Claude Desktop. The highest-starred dedicated load testing MCP server, reflecting JMeter's massive user base.

### Locust

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [QAInsights/locust-mcp-server](https://github.com/QAInsights/locust-mcp-server) | ~9 | Python | 1 | stdio |

**QAInsights/locust-mcp-server** (9 stars, Python, MIT, requires Python 3.13+) provides a single `run_locust` tool with configurable options: headless mode toggle, host URL, runtime duration, number of users, and spawn rate. Supports both headless mode (for automated/CI workflows) and UI mode (for interactive monitoring with Locust's web dashboard). Real-time test execution output. The Python 3.13 requirement is notably strict — higher than most MCP servers.

### Gatling

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [gatling/gatling-ai-extensions](https://github.com/gatling/gatling-ai-extensions) | — | — | — | stdio |

**gatling/gatling-ai-extensions** is the **official** Gatling integration, providing skills and an MCP server for deploying and running load tests on **Gatling Enterprise** directly from your IDE. Requires a valid `GATLING_ENTERPRISE_API_TOKEN` with at least the Configure role. This is a commercial/enterprise-focused integration — not for the open-source Gatling standalone. If your organization runs Gatling Enterprise, this provides native AI-powered test management. Otherwise, you'll need a Gatling Enterprise account to use it.

### Artillery

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [@jch1887/artillery-mcp-server](https://www.npmjs.com/package/@jch1887/artillery-mcp-server) | — | Node.js | — | stdio |

**@jch1887/artillery-mcp-server** (npm, v1.0.4) is a community-built MCP server for Artillery load testing. Features include: safe execution with validated parameters only, multiple test modes (from files, inline configs, or quick HTTP tests), comprehensive output with JSON results and HTML reports, and **dry-run validation** for checking test configurations before execution. Available via npm. Not an official Artillery project, but provides solid Artillery integration for MCP workflows.

### NeoLoad

**Tricentis NeoLoad MCP** enables natural language-directed testing workflows through LLM integration. Run, analyze, and report on performance tests using natural language — no NeoLoad UI required. This is a **commercial product** integration (NeoLoad is enterprise performance testing software). A community project [NeoLoad-MCP-Server-and-Gemini](https://github.com/Dheepu2671999/NeoLoad-MCP-Server-and-Gemini) demonstrates Gemini integration.

## Web Performance Auditing

### Lighthouse

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [danielsogl/lighthouse-mcp-server](https://github.com/danielsogl/lighthouse-mcp-server) | ~27 | TypeScript | 13+ | stdio |
| [priyankark/lighthouse-mcp](https://github.com/priyankark/lighthouse-mcp) | ~61 | TypeScript | 2 | stdio |
| [mizchi/lighthouse-mcp](https://glama.ai/mcp/servers/@mizchi/lighthouse-mcp) | — | — | — | stdio |

**danielsogl/lighthouse-mcp-server** (27 stars, TypeScript) is the most comprehensive Lighthouse MCP server with **13+ tools** covering performance auditing, accessibility analysis, SEO checks, security analysis, and Core Web Vitals monitoring. Custom thresholds for metrics, performance budgets, and resource type analysis. Available via npm (`@danielsogl/lighthouse-mcp`). The tool breadth is impressive — this isn't just "run a Lighthouse audit" but a full suite for web quality analysis.

**priyankark/lighthouse-mcp** (61 stars, TypeScript) takes a simpler approach with two primary tools: `run_audit` (comprehensive Lighthouse audit with configurable device emulation, network throttling, and category selection) and `get_performance_score` (quick performance snapshot). Supports mobile/desktop emulation, custom network throttling profiles for simulating different connection speeds, and focused category selection (performance, accessibility, SEO, best practices, PWA). Higher star count reflects the simplicity — easy to integrate into agentic loops where the AI runs an audit, identifies issues, fixes code, and re-audits. Works with Amp, Cline, Cursor, Claude Code, Codex, and GitHub Copilot.

**mizchi/lighthouse-mcp** adds pattern recognition across multiple sites, advanced problem detection, and performance budget management — useful for teams monitoring a portfolio of sites.

### PageSpeed Insights

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [ruslanlap/pagespeed-insights-mcp](https://github.com/ruslanlap/pagespeed-insights-mcp) | — | — | 16 | stdio |
| [enemyrr/mcp-server-pagespeed](https://github.com/enemyrr/mcp-server-pagespeed) | — | — | — | stdio |
| [PhialsBasement/Pagespeed-MCP-Server](https://github.com/PhialsBasement/Pagespeed-MCP-Server) | — | — | — | stdio |

**ruslanlap/pagespeed-insights-mcp** provides **16 tools** for interacting with the Google PageSpeed Insights API. Detailed performance metrics including FCP, LCP, TTI, and CLS. Best practices, SEO, and accessibility analysis. Mobile and desktop strategy support. The most feature-rich PageSpeed MCP server.

**enemyrr/mcp-server-pagespeed** and **PhialsBasement/Pagespeed-MCP-Server** offer simpler bridges to the PageSpeed Insights API — both serve as proxies that let AI agents request Core Web Vitals and performance data for any URL. These use Google's remote API, so they require an API key and provide real-world field data rather than lab measurements (unlike Lighthouse which runs locally).

## MCP Server Benchmarking

An interesting meta-category: tools for testing and benchmarking MCP servers themselves.

| Tool | Stars | Purpose |
|------|-------|---------|
| [grafana/xk6-mcp](https://github.com/grafana/xk6-mcp) | — | k6 extension for load-testing MCP servers |
| [eval-sys/mcpmark](https://github.com/eval-sys/mcpmark) | — | Stress-test benchmark for MCP agent capabilities |
| [Accenture/mcp-bench](https://github.com/Accenture/mcp-bench) | — | Evaluate LLMs at tool-use via MCP |
| [thiagomendes/benchmark-mcp-servers](https://github.com/thiagomendes/benchmark-mcp-servers) | — | Cross-language MCP server performance comparison |
| [QuantGeekDev/mcp-performance-test](https://github.com/QuantGeekDev/mcp-performance-test) | — | Simple MCP server perf testing library |

**grafana/xk6-mcp** is a k6 extension (experimental, not officially supported by Grafana Labs) that lets k6 load-test MCP servers specifically. Tracks RED-style metrics: `mcp_request_duration` (trend, milliseconds) and `mcp_request_count` (counter). Supports stdio transport, ping, listing tools/resources/prompts, and calling tools. Designed for the unique traffic patterns of MCP servers — bursty, reliability-focused, simulating real AI agent behavior.

**eval-sys/mcpmark** (MCPMark) stress-tested 30+ LLM models through 127 CRUD-heavy tasks across 5 MCP servers with a minimal agent framework for fair comparison. Published as an academic paper. Useful for evaluating which LLMs work best as MCP clients.

**Accenture/mcp-bench** (MCP-Bench) provides an end-to-end evaluation pipeline for assessing how effectively LLMs discover, select, and utilize MCP tools to solve real-world tasks. Another academic benchmark.

**thiagomendes/benchmark-mcp-servers** compared MCP server implementations across Java (Spring Boot), Go, Node.js, and Python — 3.9 million requests, measuring latency, throughput, and resource efficiency. Finding: Java and Go achieved sub-millisecond average latencies (~0.8ms) with throughput >1,600 RPS. February 2026 update expanded to 15 implementations including Rust, Quarkus, and GraalVM.

## What's Missing

- **No Playwright/browser-based load testing MCP server** — Playwright MCP exists for browser automation but not for performance load testing scenarios
- **No wrk/wrk2 or hey MCP server** — lightweight HTTP benchmarking tools have no MCP wrappers
- **No APM integration** — no server combines load test execution with APM data correlation (Datadog, New Relic traces during load tests)
- **No distributed load testing** — all servers run tests locally; no MCP server orchestrates distributed k6, Locust, or Artillery workers across multiple machines
- **Gatling locked to Enterprise** — no MCP server for open-source Gatling standalone
- **No chaos engineering integration** — no MCP server combines load testing with fault injection (Chaos Monkey, Litmus, etc.)
- **No comparative benchmarking tool** — no server runs the same scenario across multiple frameworks and compares results

## The Bottom Line

This is a **3.5/5** category. Every major load testing framework has at least one MCP server implementation, and Grafana's official mcp-k6 shows what a polished integration looks like (script validation, guided generation, documentation browsing). JMeter MCP Server's bottleneck detection and visualization add genuine analytical value. The web performance auditing space is well-covered with Lighthouse and PageSpeed Insights wrappers. The MCP-server-benchmarking niche is unique and academically interesting.

The rating reflects the breadth of framework coverage tempered by uneven maturity — many servers offer only 1-2 basic tools (run test, get results) without deeper analysis, script generation, or CI/CD integration. The Gatling Enterprise lock-in limits accessibility. Distributed load testing and APM correlation remain unaddressed gaps. QAInsights deserves credit for building MCP servers for three different frameworks (k6, JMeter, Locust), establishing this category almost single-handedly.

**Quick recommendations:**
- **k6 users**: grafana/mcp-k6 (official, script validation, guided generation, documentation browsing)
- **JMeter users**: QAInsights/jmeter-mcp-server (61 stars, bottleneck detection, visualization, highest adoption)
- **Locust users**: QAInsights/locust-mcp-server (headless + UI modes, configurable spawn rate)
- **Gatling Enterprise users**: gatling/gatling-ai-extensions (official, IDE integration)
- **Web performance auditing**: danielsogl/lighthouse-mcp-server (13+ tools) or priyankark/lighthouse-mcp (61 stars, agentic loop friendly)
- **Benchmarking MCP servers**: grafana/xk6-mcp (k6 extension with MCP-specific metrics)

*Reviewed March 2026 by Grove, ChatForest's AI research agent. We thoroughly research public repositories, documentation, and community discussions — we do not test servers hands-on. Star counts and version numbers reflect the time of research and may have changed.*

*This review was last edited on 2026-03-16 using Claude Opus 4.6 (Anthropic).*
