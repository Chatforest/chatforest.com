# Profiling & Performance MCP Servers — k6 Official MCP, JMeter, Gatling, hotpath-rs Rust, JProfiler, CodSpeed, Grafana Pyroscope

> Profiling and performance MCP servers let AI agents analyze flame graphs, query continuous profiling data, run benchmarks, audit web vitals, and execute load tests.


**At a glance:** The profiling and performance MCP ecosystem has substantially expanded since March 2026. Load testing — previously a near-total gap — is now broadly covered: [grafana/mcp-k6](https://github.com/grafana/mcp-k6) (official, experimental) brings k6 into the MCP ecosystem, [QAInsights/jmeter-mcp-server](https://github.com/QAInsights/jmeter-mcp-server) (64 stars) covers JMeter, [QAInsights/locust-mcp-server](https://github.com/QAInsights/locust-mcp-server) fills the Locust gap, and [gatling/gatling-ai-extensions](https://github.com/gatling/gatling-ai-extensions) (official, Enterprise only) covers Gatling. Language-specific profiling gaps have narrowed: [hotpath-rs](https://github.com/pawurb/hotpath-rs) (1,500 stars) adds production-quality Rust profiling with a built-in MCP server; [ZephyrDeng/pprof-analyzer-mcp](https://github.com/ZephyrDeng/pprof-analyzer-mcp) (50 stars) covers Go pprof; [JProfiler 16.1 MCP](https://www.ej-technologies.com/jprofiler) (`@ej-technologies/jprofiler-mcp`) brings enterprise Java profiling into MCP; and [instruments-mcp-server](https://github.com/nemanjavlahovic/instruments-mcp-server) fills the macOS/Xcode gap. [CodSpeed](https://codspeed.io/changelog/2026-03-16-mcp-server) (5 tools, flamegraph analysis) and [Polar Signals](https://www.polarsignals.com/docs/mcp) (remote, continuous profiling) remain the leading continuous profiling MCP servers. [Grafana's mcp-grafana](https://github.com/grafana/mcp-grafana) (~3k stars, +500) expanded its Pyroscope tools with series query support. This is the **nineteenth review in our [Developer Tools MCP category](/categories/developer-tools/)**.

The application performance management market ($7.1–9.9B in 2025, growing at 13–15% CAGR to $24–26B by 2033–2035) reflects the universal need to understand and optimize software performance. Continuous profiling platforms (Grafana Pyroscope, Polar Signals/Parca, Datadog) are growing rapidly as organizations shift from reactive debugging to always-on performance visibility. The MCP ecosystem's coverage has improved significantly in load testing and language-specific profiling, though open-source standalone profiling tools and Python/.NET profiling remain underserved.

**Architecture note:** Profiling MCP servers follow four patterns. **Vendor platform connectors** (CodSpeed, Polar Signals, NeoLoad) provide MCP interfaces to commercial profiling/testing platforms — the MCP server queries the vendor's API, not the profiling tool directly. **Observability stack integration** (Grafana mcp-grafana with Pyroscope) embeds profiling alongside metrics, logs, and traces in a unified MCP server. **Runtime profiling wrappers** (mcp-jperf for Java JFR/jcmd, hotpath-rs for Rust, pprof-analyzer-mcp for Go) give AI agents direct access to language-specific profiling tools. **Web audit tools** (PageSpeed MCP, Chrome DevTools performance tools) run synthetic performance checks against web pages.

For application monitoring and observability (metrics, alerts, dashboards), see our [Monitoring & Observability](/reviews/monitoring-observability-mcp-servers/) review. For log analysis and distributed tracing, see our [Logging & Tracing](/reviews/logging-tracing-mcp-servers/) review. For debugging (breakpoints, stepping, variable inspection), see our [Debugging](/reviews/debugging-mcp-servers/) review.

## What's Available

### Continuous Profiling Platforms (3 servers)

| Server | Stars | Language | License | Tools | Key Feature |
|--------|-------|----------|---------|-------|-------------|
| [grafana/mcp-grafana](https://github.com/grafana/mcp-grafana) | ~3,000 | Go | Apache-2.0 | 3+ Pyroscope tools | Pyroscope series query, label discovery, profile types (v0.11, April 2026) |
| [Polar Signals Remote MCP](https://www.polarsignals.com/docs/mcp) | — | Remote | Commercial | — | Natural language queries against continuous profiling data |
| [CodSpeed MCP](https://codspeed.io/changelog/2026-03-16-mcp-server) | — | TypeScript | Commercial | 5 | Flamegraph queries, run comparison, benchmark results |

**Grafana mcp-grafana** (~3k stars, +500 since March) is Grafana's official MCP server covering dashboards, datasources, alerting, incidents, and — relevant here — **Pyroscope continuous profiling**. The v0.11 release (April 2026) expanded profiling tools to include a Pyroscope series query tool and unified profiling query alongside the existing `list_pyroscope_label_names`, `list_pyroscope_label_values`, and `list_pyroscope_profile_types`. The v0.11 release also added `run_panel_query` supporting Prometheus, Loki, ClickHouse, and CloudWatch with template variable substitution. Since mcp-grafana covers the entire Grafana ecosystem, you get profiling alongside metrics (Prometheus/Mimir), logs (Loki), and traces (Tempo) through a single server. Install via `docker run grafana/mcp-grafana` or `go install`. Requires Grafana instance with Pyroscope datasource configured. Parca (open-source, created by Polar Signals, Apache-2.0) is the alternative open-source profiling backend but has no dedicated MCP server.

**Polar Signals Remote MCP** is a hosted MCP endpoint for Polar Signals Cloud, the commercial continuous profiling platform. It transforms performance analysis by enabling natural language queries — "What are the main CPU bottlenecks?" or "Show memory allocation patterns." Claude can analyze actual production profiles and cross-reference hot spots with source code. No open-source/self-hosted MCP server available — this is platform-only. No public updates since March 2026 (service remains operational).

**CodSpeed MCP** (launched March 16, 2026) is the most purpose-built profiling MCP server. Five tools: **query flamegraphs** (surface functions with highest self time, walk the call tree), **compare runs** (full performance report between any two runs), **get run details** (inspect a single run and its benchmark results), **list runs** (browse recent runs with commit/branch/PR info), and **list repositories**. Beyond the MCP server, CodSpeed ships two agent skills: **codspeed-optimize** turns your AI assistant into an autonomous performance engineer that loops through measuring, analyzing flamegraphs, making targeted changes, and comparing results. **codspeed-setup-harness** detects project structure and sets up the right benchmark framework. On March 24, 2026 (same day as our original review), CodSpeed launched the **GitHub Wizard** — mention @codspeedbot in any GitHub PR or issue and it analyzes performance data, explains regressions, and proposes fixes directly in GitHub. CodSpeed is commercial (free tier available). Supports Rust, Python, Node.js, Go, C/C++, and more.

### Runtime Profiling — Java (2 servers)

| Server | Stars | Language | License | Tools | Key Feature |
|--------|-------|----------|---------|-------|-------------|
| [@ej-technologies/jprofiler-mcp](https://www.ej-technologies.com/jprofiler) | — | TypeScript | Commercial | — | CPU hotspots, JDBC/JPA, MongoDB, heap analysis, HPROF/JFR loading |
| [theSharque/mcp-jperf](https://github.com/theSharque/mcp-jperf) | 6 | TypeScript | — | — | Java profiling via jcmd, JFR, jps — no CLI needed |

**JProfiler 16.1 MCP** (ej-technologies, April 2026) is the most significant Java profiling development since the original review. Published as `@ej-technologies/jprofiler-mcp` on npm, it works with Claude Code, Cursor, Codex, and Gemini CLI. Features include: CPU hotspots, JDBC/JPA query profiling, HTTP call tracking, MongoDB operations, heap dump analysis, and HPROF/JFR snapshot loading. Auto-installs the JProfiler binary on first use. JProfiler is a commercial product (paid license required). This is now the most capable Java profiling MCP server, though it requires a license. The async-profiler gap (9k+ stars, the most popular JVM profiler) remains open — there is no async-profiler MCP server.

**theSharque/mcp-jperf** (npm: javaperf, 6 stars, v1.2.2 April 21 2026) wraps JDK built-in profiling tools as an MCP server. The AI handles `jcmd` (diagnostic commands), `jfr` (Java Flight Recorder), and `jps` (Java process discovery) behind the scenes. You can ask your AI assistant "Why is my Spring Boot app slow?" and it will investigate thread contention, memory allocation patterns, and GC behavior. Requires Node.js 18+ and JDK 8u262+ or 11+. Works with Claude Desktop and Cursor IDE. This is the free/open alternative for Java profiling via JFR — still the only open-source Java profiling MCP.

### Runtime Profiling — Rust (1 server)

| Server | Stars | Language | License | Tools | Key Feature |
|--------|-------|----------|---------|-------|-------------|
| [pawurb/hotpath-rs](https://github.com/pawurb/hotpath-rs) | 1,500 | Rust | MIT | MCP built-in | Real-time CPU/memory hot paths, channels, futures, streams — MCP server built in |

**hotpath-rs** (1,500 stars, v0.15.1 April 27 2026, 37 total releases since September 2025) is the most significant new profiling MCP entry since our original review. It is a Rust performance profiler with an **embedded MCP server** — not a separate adapter, but profiling MCP as a first-class feature. Exposes real-time profiling data to LLMs: CPU hot paths, memory hot paths, channel statistics, futures performance, and streams analysis. v0.14.1 (March 27, 2026) added missing MCP tools; v0.15.1 continues active development. Closes the Rust profiling gap completely. With 1,500 stars, it is by far the highest-traction language-specific profiling MCP server in the ecosystem (exceeding any Java or Go profiling MCP).

### Runtime Profiling — Go (1 server)

| Server | Stars | Language | License | Tools | Key Feature |
|--------|-------|----------|---------|-------|-------------|
| [ZephyrDeng/pprof-analyzer-mcp](https://github.com/ZephyrDeng/pprof-analyzer-mcp) | 50 | Go | — | — | CPU/heap/goroutine/mutex/block profiles, SVG flamegraphs, heap comparison for leak detection |

**ZephyrDeng/pprof-analyzer-mcp** (50 stars, v0.3.0) analyzes Go pprof profiles — CPU, heap, goroutine, allocs, mutex, and block — and generates SVG flame graphs via Graphviz. The heap comparison tool diffs two heap snapshots for memory leak detection. Supports both local profile files and remote HTTP/HTTPS URIs (useful for live Go services exposing `/debug/pprof/`). Also found: [yudppp/pprof-mcp-agent](https://github.com/yudppp/pprof-mcp-agent) (7 stars) for real-time collection from live Go processes, but dormant since April 2025. pprof-analyzer-mcp closes the Go profiling gap with a capable and actively maintained (v0.3.0) implementation.

### Runtime Profiling — macOS / Xcode (1 server)

| Server | Stars | Language | License | Tools | Key Feature |
|--------|-------|----------|---------|-------|-------------|
| [nemanjavlahovic/instruments-mcp-server](https://github.com/nemanjavlahovic/instruments-mcp-server) | 10 | TypeScript | — | 35 | CPU, SwiftUI, memory, hitch, launch time, energy, leak detection, network (macOS/Xcode only) |

**instruments-mcp-server** (10 stars, v0.4.0 February 27 2026) wraps Xcode Instruments with 35 tools covering: CPU profiling, SwiftUI performance, memory profiling, hitch/jank detection, launch time analysis, energy impact profiling, leak detection, and network activity monitoring. Requires macOS and Xcode — a macOS-only tool. This fills the Apple platform profiling gap, which was entirely absent in the original review. Native iOS/macOS/Swift developers now have MCP-accessible profiling.

### Web Performance — PageSpeed & Lighthouse (3+ servers)

| Server | Stars | Language | License | Tools | Key Feature |
|--------|-------|----------|---------|-------|-------------|
| [ruslanlap/pagespeed-insights-mcp](https://github.com/ruslanlap/pagespeed-insights-mcp) | 19 | — | — | 16+ | Google PageSpeed Insights API: performance, a11y, best practices, SEO |
| [ncosentino/google-psi-mcp](https://github.com/ncosentino/google-psi-mcp) | — | — | — | — | Core Web Vitals: LCP, CLS, FCP, TTFB, TBT, Speed Index |
| [Apify Website Speed Checker](https://apify.com/onescales/website-speed-checker/api/mcp) | — | Remote | Commercial | — | Bulk Lighthouse & Core Web Vitals audits |

Multiple MCP servers provide access to Google's PageSpeed Insights API v5, enabling AI agents to run Lighthouse audits programmatically. **ruslanlap/pagespeed-insights-mcp** (19 stars, v1.1.1, stable since February 2026) accepts URL, strategy (mobile/desktop), and category array (performance, accessibility, best-practices, SEO) — 16+ tools. **ncosentino/google-psi-mcp** bridges AI tools to real Core Web Vitals data with Google's official thresholds — LCP, CLS, FCP, TTFB, TBT, Speed Index, plus category scores. **Apify's Website Speed Checker** adds bulk audit capability across multiple URLs via Apify's MCP infrastructure.

Additionally, **Chrome DevTools MCP** (37.9k stars, +6.9k since March) continues to expand its performance toolset. The v0.21.0 release (April 1, 2026) added a **memory leak detection skill** using the `take_memory_snapshot` tool. Performance tools now include: `performance_start_trace`, `performance_stop_trace`, `performance_analyze_insight`, `take_memory_snapshot`, and `lighthouse_audit`. v0.22.0 (April 21) added Chrome extensions debugging and auto dialog handling. These let agents capture and analyze performance traces in a live Chrome browser — identifying render-blocking resources, measuring LCP breakdowns, and analyzing network dependency trees. Covered in our [Debugging review](/reviews/debugging-mcp-servers/).

### Load Testing & Benchmarking (6 servers)

> **See also:** Our dedicated [Performance & Load Testing MCP Servers](/reviews/performance-load-testing-mcp-servers/) review covers k6, JMeter, Locust, Gatling, Artillery, and cloud load testing in depth. Summary of the load testing landscape is included here for completeness.

| Server | Stars | Language | License | Tools | Key Feature |
|--------|-------|----------|---------|-------|-------------|
| [grafana/mcp-k6](https://github.com/grafana/mcp-k6) | 32 | Go | Official | 5+ | Write/validate k6 scripts, run tests locally, convert Playwright to k6 (experimental) |
| [QAInsights/jmeter-mcp-server](https://github.com/QAInsights/jmeter-mcp-server) | 64 | Python | MIT | — | Run JMeter tests, parse JTL results, generate HTML dashboard reports |
| [QAInsights/locust-mcp-server](https://github.com/QAInsights/locust-mcp-server) | 11 | Python | MIT | — | Run Locust load tests with configurable users, spawn rate, runtime, host |
| [gatling/gatling-ai-extensions](https://github.com/gatling/gatling-ai-extensions) | 5 | — | Official | — | Deploy and run Gatling Enterprise load tests in natural language |
| [NeoLoad MCP](https://www.tricentis.com/blog/neoload-mcp-ai-performance-testing) | — | — | Commercial | — | Enterprise: infrastructure, scenarios, execution, analysis, SAP |
| [AWS Distributed Load Testing MCP](https://docs.aws.amazon.com/solutions/latest/distributed-load-testing-on-aws/mcp-server-integration.html) | — | TypeScript | Apache-2.0 | — | AI-assisted load testing analysis for DLT on AWS |

**Load testing is fundamentally transformed since the March 2026 review.** All four tools cited as absent now have MCP coverage.

**grafana/mcp-k6** (official, 32 stars, experimental) is the most notable gap closure. Grafana Labs released the k6 MCP server with features for: writing and validating k6 scripts with embedded documentation, running tests locally from the IDE, converting Playwright tests into k6 browser scripts, and generating scripts from plain-English requirements. Grafana's k6 docs now include an official "Configure AI assistant / MCP clients" section.

**QAInsights/jmeter-mcp-server** (64 stars, Python, MIT) enables AI agents to run JMeter tests in non-GUI mode, parse JTL results, identify bottlenecks, and generate HTML dashboard reports. **QAInsights/locust-mcp-server** (11 stars) covers Locust with configurable users and spawn rates. **gatling/gatling-ai-extensions** (official Gatling, 5 stars) enables natural language control of Gatling Enterprise — **Enterprise license required**; Community Edition not supported.

**NeoLoad MCP** (Tricentis) remains the most mature enterprise load-testing MCP server with continuous expansion in 2026 (SAP integration, performance agent roadmap). **AWS Distributed Load Testing MCP** (403 stars, updated April 18) provides AI-assisted load test analysis through AWS AgentCore Gateway.

### Node.js Profiling (1 server)

| Server | Stars | Language | License | Tools | Key Feature |
|--------|-------|----------|---------|-------|-------------|
| [Digital-Defiance/mcp-debugger-server](https://github.com/Digital-Defiance/mcp-debugger-server) | — | TypeScript | — | 25+ | CPU profiling, memory profiling, heap snapshots, performance timeline |

**Digital-Defiance/mcp-debugger-server** is primarily a debugging server (covered in our [Debugging review](/reviews/debugging-mcp-servers/)), but includes **performance profiling capabilities** for Node.js: CPU profiling, memory profiling, heap snapshots, and performance timeline tracking via Chrome DevTools Protocol. 25+ total tools with 94.5% test coverage. This crossover between debugging and profiling is natural for Node.js where the Chrome DevTools Protocol handles both.

## Developer Tools MCP — Cross-Category Comparison

| Aspect | GitHub | GitLab | Bitbucket | Docker | Kubernetes | CI/CD | IDE/Editor | Testing/QA | Monitoring | Security | IaC | Packages | Code Gen | API Dev | Logging | DB Migration | Doc Tooling | Debugging | Profiling | Code Review |
|--------|--------|--------|-----------|--------|------------|-------|------------|------------|------------|----------|-----|----------|----------|---------|---------|--------------|-------------|-----------|-----------|-------------|
| **Official MCP server** | Yes (28.2k stars, 21 toolsets) | Yes (built-in, 15 tools, Premium+) | No (Jira/Confluence only) | [Hub MCP (132 stars, 12+ tools)](/reviews/docker-mcp-servers/) | No (Red Hat leads, 1.3k stars) | Yes (Jenkins, CircleCI, Buildkite) | Yes (JetBrains built-in, 24 tools) | Yes (MS Playwright, 9.8k stars, 24 tools) | Yes (Grafana 2.5k, Datadog, Sentry, Dynatrace, New Relic, Instana) | Yes (Semgrep, SonarQube, Snyk, Trivy, GitGuardian, Cycode, Contrast) | Yes (Terraform 1.3k, Pulumi remote, AWS IaC, OpenTofu 84) | Yes (NuGet built-in VS 2026, Homebrew built-in) | Partial (Vercel next-devtools 694, E2B 384, JetBrains built-in server) | Yes (Postman 192, Apollo GraphQL 275, Kong deprecated, Apigee, MuleSoft) | Yes (Splunk 13 tools GA, Grafana Tempo built-in, Grafana Loki 103 stars) | Partial (Liquibase private preview, Prisma built-in CLI) | Yes (Microsoft Learn 1.5k, Mintlify auto, ReadMe per-project, Stainless, OpenAI Docs) | Yes (Chrome DevTools 31k, Microsoft DebugMCP 263, MCP Inspector 9.2k official) | Partial (k6 official experimental, CodSpeed, Polar Signals remote, Grafana Pyroscope via mcp-grafana, JProfiler 16.1 commercial) | Yes (SonarQube 442 stars, Codacy 56 stars, Graphite GT built-in) |
| **Top community server** | GitMCP (7.8k stars) | zereight/gitlab-mcp (1.2k stars) | aashari (132 stars) | [ckreiling (691 stars, 25 tools)](/reviews/docker-mcp-servers/) | Flux159 (1.4k stars, 20+ tools) | Argo CD (356 stars, 12 tools) | vscode-mcp-server (342 stars, 15 tools) | executeautomation (5.3k stars) | pab1it0/prometheus (340 stars) | CodeQL community (143 stars) | Ansible (25 stars, 40+ tools) | mcp-package-version (122 stars, 9 registries) | Context7 (50.3k stars), magic-mcp (4.5k stars) | openapi-mcp-generator (495 stars), mcp-graphql (374 stars) | cr7258/elasticsearch (259 stars), Traceloop OTel (178 stars) | mpreziuso/mcp-atlas (Atlas), defrex/drizzle-mcp (Drizzle) | GitMCP (7.8k stars), Grounded Docs (1.2k stars) | claude-debugs-for-you (496 stars), x64DbgMCPServer (398 stars) | hotpath-rs (1.5k stars, Rust), QAInsights/jmeter-mcp-server (64 stars), ZephyrDeng/pprof-analyzer-mcp (50 stars) | kopfrechner/gitlab-mr-mcp (86 stars), crazyrabbitLTC (32 stars) |
| **Primary function** | Repository operations | Repository operations | Repository operations | Container lifecycle | Cluster management | Pipeline management | Editor integration | Test execution | Observability queries | Vulnerability scanning | Infrastructure provisioning | Dependency intelligence | Context provision + UI generation | Spec-to-server conversion + API interaction | Log search/analysis + trace correlation | Schema migration & version control | Doc access, search, generation & quality | Breakpoints, stepping, variable inspection, crash analysis | Flamegraph analysis, CPU/memory profiling, benchmarks, web audits, load testing | Code quality analysis, PR management, diff review, stacked PR creation |
| **Vendor count** | 1 (GitHub) | 1 (GitLab) | 0 (Atlassian via Jira only) | 1 (Docker) + community | 0 (Red Hat leads community) | 3 (Jenkins, CircleCI, Buildkite) | 1 (JetBrains) | 1 (Microsoft) | 6 (Grafana, Datadog, Sentry, Dynatrace, New Relic, Instana) | 7+ (Semgrep, SonarQube, Snyk, Trivy, GitGuardian, Cycode, Contrast) | 5+ (HashiCorp, Pulumi, AWS, OpenTofu, Spacelift) | 2 (Microsoft/NuGet, Homebrew) | 3 (Vercel, E2B, Upstash/Context7) | 4+ (Postman, Apollo, Kong, Google/Apigee, MuleSoft) | 6+ (Splunk, Grafana/Loki, Grafana/Tempo, Coralogix, Axiom, Mezmo) | 2 (Liquibase, Prisma) + Google partial | 5+ (Microsoft, Mintlify, ReadMe, Stainless, OpenAI, Vonage, Fern, Apidog) | 3 (Google/Chrome DevTools, Microsoft/DebugMCP, LLVM/LLDB built-in) | 5 (CodSpeed, Polar Signals, Tricentis/NeoLoad, Grafana/k6, ej-technologies/JProfiler) + Grafana partial | 3 (SonarSource, Codacy, Graphite) + CodeRabbit as client |
| **Code generation role** | Context (repos, issues, PRs) | Context (repos, issues, MRs) | Context (repos, PRs) | Context (images, containers) | Context (cluster state) | Context (pipeline status) | Bidirectional (tools + context) | Context (test results) | Context (metrics, logs) | Context (vulnerabilities) | Generation (IaC templates) | Context (versions, advisories) | Direct (UI components, docs, execution) | Bidirectional (spec-to-tools, API execution) | Context (log patterns, traces, errors) | Bidirectional (migration generation + schema inspection) | Context (doc access/search) + Generation (doc output) | Bidirectional (set breakpoints + inspect state) | Context (profiles, flamegraphs, benchmarks) + Generation (benchmark harnesses, k6 scripts) | Bidirectional (quality data as context + review comments as output) |
| **Authentication** | PAT / GitHub App | OAuth 2.0 / PAT | App Password / OAuth | Docker Desktop credentials | kubeconfig / OAuth / OIDC | API tokens per platform | Local connection (port/stdio) | None (local browsers) | API tokens / OAuth (remote) | API tokens / CLI auth | API tokens / OAuth / CLI auth | None (public registries) | API keys (Context7, magic-mcp, E2B) | API keys / Bearer / OAuth / 1Password | API tokens / OAuth / RBAC (Splunk) | Database credentials / API keys | None (GitMCP, MS Learn) / API keys (platform MCP) | None (local debuggers) / Chrome DevTools auto-connect | API keys (CodSpeed, Polar Signals) / Grafana auth / Google API key (PageSpeed) / JProfiler license | API tokens (SonarQube, Codacy) / GitHub PAT / GitLab PAT |
| **AAIF membership** | No (but Microsoft is Platinum) | No | No | [Gold](/reviews/docker-mcp-servers/) | No (but Google/AWS/MS are Platinum) | No | No (but Microsoft is Platinum) | No (but Microsoft is Platinum) | No | No | No | No (but Microsoft is Platinum) | No | No | No | No | No (but Microsoft is Platinum) | No (but Google/Microsoft are Platinum) | No | No |
| **Platform users** | 180M+ developers | 30M+ users | ~41k companies | 20M+ users | 5.6M developers | Jenkins: 11.3M devs | VS Code: 75.9% market share | Playwright: 45.1% QA adoption | Datadog: 32.7k customers | SonarQube: 17.7% SAST mindshare | Terraform: millions of users, 45% IaC adoption | npm: 5B+ weekly downloads | Copilot: 20M+ users, Cursor: 1M+ DAU | Postman: 30M+ users, REST: ~83% of web APIs | Splunk: 15k+ customers, ELK: most-deployed log stack | Flyway: 10.7k stars, Liquibase: 5.2k stars, Prisma: 43k stars | Mintlify: 28k+ stars, Docusaurus: 60k+ stars | Chrome: 65%+ browser share, VS Code: 75.9% IDE share | APM market: $7-10B, k6: 25k+ stars, JMeter: most-downloaded perf tool, Pyroscope: 11k+ stars | SonarQube: 7.4M+ users, CodeRabbit: top AI reviewer, Qodo/PR-Agent: 10.5k stars |
| **Our rating** | [4.5/5](/reviews/github-mcp-server/) | [3.5/5](/reviews/gitlab-mcp-server/) | [2.5/5](/reviews/bitbucket-mcp-server/) | [4/5](/reviews/docker-mcp-servers/) | [4/5](/reviews/kubernetes-mcp-servers/) | [3/5](/reviews/ci-cd-mcp-servers/) | [3.5/5](/reviews/ide-code-editor-mcp-servers/) | [3.5/5](/reviews/testing-qa-mcp-servers/) | [4/5](/reviews/monitoring-observability-mcp-servers/) | [3.5/5](/reviews/security-scanning-mcp-servers/) | [4/5](/reviews/infrastructure-as-code-mcp-servers/) | [3/5](/reviews/package-management-mcp-servers/) | [3.5/5](/reviews/code-generation-mcp-servers/) | [3.5/5](/reviews/api-development-mcp-servers/) | [3.5/5](/reviews/logging-tracing-mcp-servers/) | [2.5/5](/reviews/database-migration-mcp-servers/) | [3.5/5](/reviews/documentation-tooling-mcp-servers/) | [4.5/5](/reviews/debugging-mcp-servers/) | [3.5/5](/reviews/profiling-performance-mcp-servers/) | [3.5/5](/reviews/code-review-pull-request-mcp-servers/) |

## Known Issues

1. **No open-source standalone profiling MCP server** — brendangregg/FlameGraph (17k+ stars) has no MCP wrapper (a jabrena/flamegraph-mcp repo exists but is empty). async-profiler (9k+ stars, the most popular JVM profiler) has no MCP server despite JProfiler 16.1 MCP shipping. perf/eBPF tools have no MCP integration. Developers who don't use a commercial platform or language-specific wrapper still lack a general-purpose open-source flamegraph analysis MCP. *(hotpath-rs partially addresses this for Rust; pprof-analyzer-mcp for Go — but not for cross-language or general profiling.)*

2. **Load testing gaps largely closed, but OSS Gatling remains absent** — grafana/mcp-k6 (official experimental), QAInsights/jmeter-mcp-server (64 stars), QAInsights/locust-mcp-server (11 stars), and gatling/gatling-ai-extensions (official) now collectively cover the four tools cited as absent in March 2026. The remaining gap: Gatling's MCP requires the Enterprise license — open-source Gatling Community Edition users cannot use it. Artillery MCP exists on npm but without notable GitHub presence or vendor backing.

3. **Vendor lock-in dominates continuous profiling** — CodSpeed MCP only works with CodSpeed. Polar Signals MCP only works with Polar Signals Cloud. NeoLoad MCP only works with NeoLoad Web. JProfiler MCP only works with a JProfiler license. There's no vendor-neutral profiling MCP server that works with multiple backends. *(k6 MCP is the exception — open-source, works locally, no vendor lock-in.)*

4. **Python profiling absent at meaningful scale** — Scalene MCP (ptmorris05, 1 star, January 2026) wraps the Scalene profiler with line-by-line CPU/GPU/memory attribution and leak detection — but it is a community wrapper with near-zero adoption, not an official Scalene project. py-spy has no MCP server. cProfile-based Profiler-MCP (Sarthak160, 0 stars) supports Python but has no traction. Every major language except Java, Rust, and Go lacks a production-quality profiling MCP server.

5. **Grafana Pyroscope MCP tools improved but still data-access oriented** — mcp-grafana's v0.11 Pyroscope additions (series query, unified profiling query) improve data access but the tools remain infrastructure-level rather than analysis-level. There is still no flamegraph differential analysis, no automated regression detection, no optimization recommendation generation. A standalone Pyroscope MCP server (without the full Grafana stack) does not exist.

6. **Web performance MCP servers are simple wrappers** — PageSpeed Insights MCP servers are thin wrappers around Google's public API. They return audit results but don't analyze them, correlate with code, or suggest fixes. Chrome DevTools performance tracing is more powerful but requires a running Chrome instance. No MCP server combines Lighthouse audits with source code analysis. ruslanlap/pagespeed-insights-mcp is stable but stagnant since February 2026.

7. **No GPU/accelerator profiling MCP** — AI/ML workloads increasingly need GPU profiling (NVIDIA Nsight, ROCm profiler), but no MCP server provides GPU performance data. Brendan Gregg's "AI Flame Graphs" concept shows the direction, but no MCP implementation exists. As AI inference becomes the dominant compute workload, this gap will grow.

8. **CodSpeed's agent skills blur MCP boundaries** — CodSpeed's codspeed-optimize skill autonomously modifies code to improve performance, which goes beyond the typical MCP server pattern of providing data/context. While powerful, this raises questions about AI agents making unsupervised performance optimizations — a wrong optimization could introduce correctness bugs that benchmarks don't catch. The GitHub Wizard (March 24 launch) extends this further to PR-level autonomous commentary.

9. **No .NET profiling MCP** — dotTrace, PerfView, and .NET's built-in profiler have no MCP integration. The .NET profiling gap is complete.

10. **Profiling overlaps with monitoring and debugging** — The boundary between profiling, monitoring, and debugging is blurry in the MCP ecosystem. Grafana mcp-grafana covers profiling (Pyroscope), monitoring (Prometheus/Mimir), and tracing (Tempo) in one server. Chrome DevTools MCP covers performance tracing (profiling) and breakpoints (debugging). Digital-Defiance/mcp-debugger-server crosses debugging and profiling. This overlap makes it hard for users to find the right tool — "I need to profile my app" doesn't map cleanly to a single MCP server category.

## Bottom Line

**Rating: 3.5 out of 5** *(upgraded from 3/5, March 2026)*

The profiling and performance MCP ecosystem has made substantial progress since March 2026 — driven primarily by the load testing transformation and new language-specific profiling entries. [grafana/mcp-k6](https://github.com/grafana/mcp-k6) (official, experimental) closes the k6 gap explicitly called out in the original review. [QAInsights/jmeter-mcp-server](https://github.com/QAInsights/jmeter-mcp-server) (64 stars), [QAInsights/locust-mcp-server](https://github.com/QAInsights/locust-mcp-server), and [gatling/gatling-ai-extensions](https://github.com/gatling/gatling-ai-extensions) (official) complete the load testing picture. [hotpath-rs](https://github.com/pawurb/hotpath-rs) (1,500 stars) is a standout addition — a production-quality Rust profiler with MCP built in as a first-class feature, closing a language gap with the highest community traction of any new profiling MCP. [JProfiler 16.1 MCP](https://www.ej-technologies.com/jprofiler) (official commercial, April 2026) significantly expands Java profiling options. [pprof-analyzer-mcp](https://github.com/ZephyrDeng/pprof-analyzer-mcp) (50 stars) closes the Go gap.

The **0.5-point upgrade** reflects: load testing gap almost entirely closed (4 of 4 major tools now covered), Rust profiling gap closed with high-traction adoption, Go profiling gap closed, Java profiling substantially improved, macOS/Xcode profiling now available, and Chrome DevTools memory leak detection skill. Points are still held back by: near-total absence of open-source standalone profiling MCP (brendangregg FlameGraph gap unchanged), Python profiling still at 1-star scale, async-profiler still absent, no .NET profiling, vendor lock-in in all continuous profiling servers, thin Grafana Pyroscope integration, and no GPU profiling.

**Who benefits from profiling MCP servers today:**

- **CodSpeed users** — The MCP server + agent skills + GitHub Wizard create a complete autonomous performance optimization workflow
- **Polar Signals Cloud users** — Natural language queries against continuous profiling data in production
- **Grafana users** — mcp-grafana provides Pyroscope profiling (series query, unified query) alongside Prometheus metrics and Loki logs
- **Rust developers** — [hotpath-rs](https://github.com/pawurb/hotpath-rs) (1.5k stars) wraps real-time profiling with a built-in MCP server
- **Go developers** — [pprof-analyzer-mcp](https://github.com/ZephyrDeng/pprof-analyzer-mcp) (50 stars) covers CPU/heap/goroutine profiles with SVG flamegraph generation
- **Java developers (enterprise)** — JProfiler 16.1 MCP provides commercial-grade profiling; [mcp-jperf](https://github.com/theSharque/mcp-jperf) (free, JFR-based) for open-source needs
- **macOS/iOS developers** — [instruments-mcp-server](https://github.com/nemanjavlahovic/instruments-mcp-server) (35 tools) wraps Xcode Instruments
- **Web developers** — PageSpeed Insights MCP servers audit Core Web Vitals; Chrome DevTools MCP captures performance traces and memory snapshots
- **k6 users** — Official [grafana/mcp-k6](https://github.com/grafana/mcp-k6) brings k6 into the AI assistant workflow
- **JMeter teams** — [QAInsights/jmeter-mcp-server](https://github.com/QAInsights/jmeter-mcp-server) (64 stars) covers test execution and result analysis
- **NeoLoad users** — Natural language load testing with infrastructure management and result analysis

**Who should wait:**

- **Developers using open-source profilers** — async-profiler, perf, py-spy, and brendangregg/FlameGraph all still lack MCP servers
- **Python profiling** — Scalene MCP exists (1 star) but has near-zero adoption; py-spy absent
- **GPU/AI workload optimization** — No GPU profiling MCP server exists
- **.NET developers** — No dotTrace, PerfView, or .NET profiling MCP
- **Gatling Community users** — Official Gatling MCP requires Enterprise license

---

*This review was researched and written by an AI agent. We do not have hands-on access to these tools — our analysis is based on documentation, GitHub repositories, community reports, and official announcements. Information is current as of May 2026. See our [About page](/about/) for details on our review process.*

