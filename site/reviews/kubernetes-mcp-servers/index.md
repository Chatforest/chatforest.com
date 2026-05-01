# Kubernetes MCP Servers — Cluster Management Gets an AI Interface

> Kubernetes has a strong MCP ecosystem with two leading servers above 1,000 stars: Flux159/mcp-server-kubernetes (1,400 stars, TypeScript, 20+ tools) and Red Hat's


**At a glance:** Kubernetes has **no official MCP server** from CNCF or the Kubernetes project, but the community has built a strong ecosystem led by two servers above 1,000 stars. [Flux159/mcp-server-kubernetes](https://github.com/Flux159/mcp-server-kubernetes) (~1,400 stars, TypeScript, MIT, 20+ tools) provides kubectl-style operations with Helm support — **CVE-2026-39884 (High) argument injection patched in v3.5.0**. [containers/kubernetes-mcp-server](https://github.com/containers/kubernetes-mcp-server) (**1,500 stars, +15%**, Go, Apache-2.0) from Red Hat surged with **105 new commits**, adding **Tekton integration** and **Microsoft Entra ID** auth in v0.0.61. **SUSE Rancher Prime now ships a built-in MCP server** with multi-agent "Crew" architecture. CNCF published **Cloud Native Agentic Standards** explicitly referencing MCP. With **5.6 million Kubernetes developers** and **82% of container users running K8s in production**, the MCP ecosystem matches the platform's importance. This is the **fifth review in our [Developer Tools MCP category](/reviews/ide-code-editor-mcp-servers/)**. Part of our **[Cloud & Infrastructure MCP category](/categories/cloud-infrastructure/)**.

Kubernetes is the dominant container orchestration platform, originally developed at Google and now maintained by the **Cloud Native Computing Foundation (CNCF)** under the Linux Foundation. The ecosystem spans **200+ certified distributions** with major managed offerings from AWS (EKS, ~42% market share), Google (GKE, ~27%), and Microsoft (AKS, ~23%). The container market is valued at **$5.85 billion** (2024) with a projected **33.5% CAGR** through 2030. CNCF itself is not an AAIF member, but **Google, AWS, and Microsoft** — the three largest Kubernetes cloud providers — are all **AAIF Platinum members**. MCP is now governed by the **Agentic AI Foundation (AAIF)** under the Linux Foundation, with 170+ member organizations and 110M+ monthly MCP SDK downloads.

**Architecture note:** Kubernetes MCP servers face a unique challenge: the Kubernetes API surface is enormous (hundreds of resource types, custom resources, multiple API versions) and security-critical (cluster-admin access can destroy production workloads). The leading servers take different approaches — Flux159 wraps kubectl-style commands in typed tools, while Red Hat's server implements the Kubernetes API natively in Go. Both address the security challenge with read-only modes, secret masking, and context restrictions. Helm integration is common, reflecting the reality that most K8s deployments use Helm charts. **New in 2026:** CNCF's Cloud Native Agentic Standards recommend "narrowly scoped MCP server tooling access" — validating the read-only-by-default approach. Google has proposed a **stateless MCP transport** removing session pinning for horizontal scaling on Kubernetes and Cloud Run.

## What's Available

### Flux159/mcp-server-kubernetes (Most Stars)

The **most-starred** Kubernetes MCP server:

| Aspect | Detail |
|--------|--------|
| Repository | [Flux159/mcp-server-kubernetes](https://github.com/Flux159/mcp-server-kubernetes) |
| Stars | ~1,400 |
| Forks | ~241 |
| Commits | 785 |
| Language | TypeScript (Bun runtime) |
| License | MIT |
| Latest | v3.5.0 |

**20+ tools** covering core Kubernetes operations and Helm:

| Category | Tools |
|----------|-------|
| Resources | `kubectl_get`, `kubectl_describe`, `kubectl_create`, `kubectl_apply`, `kubectl_delete`, `kubectl_patch`, `kubectl_scale` |
| Pods | `kubectl_logs`, `cleanup_pods` |
| Deployments | `kubectl_rollout` |
| Cluster | `kubectl_context`, `kubectl_reconnect`, `list_api_resources`, `explain_resource`, `node_management` (cordon/drain/uncordon) |
| Helm | `helm_install`, `helm_upgrade`, `helm_uninstall`, `helm_template_apply`, `helm_template_uninstall` |
| Network | `port_forward` |
| Utility | `kubectl_generic`, `ping` |

**Key differentiator:** Comprehensive kubectl + Helm coverage in a single server. Non-destructive mode via `ALLOW_ONLY_NON_DESTRUCTIVE_TOOLS=true` (disables delete but keeps create/update). Built-in troubleshooting prompt (`k8s-diagnose`). OpenTelemetry observability support. Secrets masking. Multi-context support for cluster switching. Docker deployment available. **New `kubectl_reconnect` tool** for fixing stale API connections after EKS control plane upgrades. Constant-time comparison for auth tokens (timing attack prevention).

**Security alert: [CVE-2026-39884](https://github.com/Flux159/mcp-server-kubernetes/security/advisories) (CVSS 8.3, High)** — Argument injection in the `port_forward` tool. Space-splitting of user input allowed injection of `--address=0.0.0.0` (exposing internal services to network) and `-n` flags (cross-namespace access). Exploitable via prompt injection against connected AI agents. **Fixed in v3.5.0** with array-based argument passing. Versions < 3.5.0 are vulnerable — upgrade immediately. An open issue also flags residual command injection risk in `exec_in_pod`.

**Limitation:** TypeScript/Bun runtime may not suit all environments. Non-destructive mode still allows create/update operations. No native cloud provider authentication (relies on kubeconfig). **5 total security advisories** (CVE-2026-39884 High, CVE-2025-53355 High command injection, CVE-2025-66404 Moderate exec_in_pod, plus two for a similarly-named pip package) — the most CVEs of any K8s MCP server.

### containers/kubernetes-mcp-server (Red Hat)

The closest thing to an **official** Kubernetes MCP server, maintained by Red Hat — **surged 15% in stars** with 105 new commits:

| Aspect | Detail |
|--------|--------|
| Repository | [containers/kubernetes-mcp-server](https://github.com/containers/kubernetes-mcp-server) |
| Stars | **1,500** (up from 1,300, +15%) |
| Forks | 328 (up from 292) |
| Commits | **871** (up from 766, +105) |
| Language | Go |
| License | Apache-2.0 |
| Latest | **v0.0.61** (April 24, 2026) |

**Multiple toolsets** organized by domain:

| Toolset | Coverage |
|---------|----------|
| **Config** | Context listing, kubeconfig management |
| **Core** (default) | Pod ops (list, get, delete, logs, exec, run, metrics), namespace/event management, node ops (logs, stats, metrics), generic K8s resource CRUD |
| **Helm** | Chart install, release list, uninstall, **chart reference validation, registry configuration** |
| **KCP** | Workspace management |
| **Kiali** | Service mesh visualization |
| **KubeVirt** | Virtual machine management **(refactored to v2.25)** |
| **Tekton** | **NEW: Pipeline and task management** |

**Key differentiator:** Native Go implementation — not a kubectl wrapper. Single binary, no external dependencies. First-class OpenShift support (KCP, Kiali, KubeVirt, **Tekton** toolsets). Multi-cluster enabled by default (`--disable-multi-cluster` to restrict). Read-only mode (`--read-only`) and destructive-operation disabling (`--disable-destructive`). Automatic secret redaction (tokens, keys, passwords, cloud credentials). OpenTelemetry integration. Available via npm, pip, Docker, and native binaries for Linux/macOS/Windows. OAuth/OIDC authentication support. **Multi-architecture container images (s390x, ppc64le)**. **MCPB (bundle) distribution support**.

**New in v0.0.60–v0.0.61:**
- **Microsoft Entra ID support** with On-Behalf-Of token exchange — first K8s MCP server with Azure AD integration
- **Tekton toolset** — pipeline and task management for CI/CD-native K8s workflows
- **Confirmation rules system** for enhanced user interaction before destructive operations
- **Per-session rate limiting** via MCP middleware
- **`require_tls` config** to enforce HTTPS connections
- **Configurable tool description overrides** — customize how tools appear to LLMs
- **User-scoped targets** (breaking change: `provider.GetTargets` is now optionally user-scoped)
- **Read-only root filesystem** in default security context
- **Configurable ServiceAccount token auto-mounting**
- **Gateway API HTTPRoute support** in Helm charts
- **Default container resolution** for multi-container pods (KEP-2227)

**Security posture:** No published CVEs. Recent hardening: read-only root filesystem, configurable token auto-mounting, TLS enforcement. Two open issues (#1110, #1111) related to token exchange security (not classified as vulnerabilities). Issue #1113 targets hardening MCP resources surface for milestone 0.1.0.

**Limitation:** Pre-1.0 versioning (v0.0.61). OpenShift-specific toolsets add complexity for vanilla K8s users. 33 open issues. Breaking change in v0.0.60 (user-scoped targets) — API still unstable.

### rohitg00/kubectl-mcp-server (Most Tools Claimed)

A **Python-based** kubectl wrapper claiming the most tools:

| Aspect | Detail |
|--------|--------|
| Repository | [rohitg00/kubectl-mcp-server](https://github.com/rohitg00/kubectl-mcp-server) |
| Stars | ~877 (up from 854) |
| Forks | ~167 |
| Commits | 133 (up from 127) |
| Language | Python |
| License | MIT |
| Latest | v1.24.0 (February 2026) |

Claims **253+ tools** spanning:

- Pod diagnosis and troubleshooting
- Deployment creation and scaling
- Namespace management, multi-cluster context switching
- Resource utilization analysis, cost optimization recommendations
- Network diagnostics, service chain tracing
- RBAC permission auditing, secret scanning, pod security validation
- Helm chart operations, application deployment orchestration

**Key differentiator:** OAuth 2.1 enterprise authentication. RBAC validation. Read-only mode available. Claims 20+ AI assistant integrations (Claude Desktop, Cursor, Windsurf, GitHub Copilot, Gemini CLI). Install via `npx kubectl-mcp-server` or pip. **Interactive 3D cluster topology UI** (Three.js). Listed in **CNCF Landscape**. 8 workflow prompts and 8 data resources.

**Limitation:** The 253+ tool count could not be independently verified. Only 133 commits for that scope suggests many tools may be thin wrappers. Python kubectl wrapper adds overhead vs native API implementations. No new release since February 2026.

### alexei-led/k8s-mcp-server (Multi-CLI)

A **Docker-based** server that bridges LLMs with multiple Kubernetes CLI tools:

| Aspect | Detail |
|--------|--------|
| Repository | [alexei-led/k8s-mcp-server](https://github.com/alexei-led/k8s-mcp-server) |
| Stars | ~205 |
| Forks | ~37 |
| Commits | 111 |
| Language | Python |
| License | MIT |

Unique approach: bundles **kubectl, Helm, istioctl, argocd**, and Unix utilities (jq, grep, sed) in a Docker container. The LLM has access to the full CLI toolchain rather than individual MCP tools.

**Key differentiator:** Native cloud provider authentication — AWS (EKS via AWS_PROFILE), Google Cloud SDK (GKE), Azure credentials (AKS). Service mesh operations via istioctl. GitOps via argocd. Strict command validation by default (configurable to permissive). Runs as non-root. Streamable HTTP transport for remote access.

**Limitation:** Docker-only deployment. CLI wrapping means slower execution than native API calls. Large container image with multiple CLIs.

### strowk/mcp-k8s-go (Lightweight Go)

A **lightweight Go** implementation:

| Aspect | Detail |
|--------|--------|
| Repository | [strowk/mcp-k8s-go](https://github.com/strowk/mcp-k8s-go) |
| Stars | ~377 |
| Forks | ~57 |
| Commits | 361 |
| Language | Go |
| License | MIT |
| Latest | v0.6.1 (November 2025) |

Tools: list/get/create/modify any K8s resources, list nodes, retrieve events, pod logs, exec into pods. Custom resource mappings for common types. Context restriction via `--allowed-contexts`.

**Key differentiator:** Simple, focused implementation. Read-only mode (`--readonly`). Secret masking enabled by default. Available via npm, Docker, GitHub releases.

**Limitation:** **Dormant since November 2025** (6+ months without release). Fewer tools than the leaders. No Helm support. Stars flat at 379.

### Other Notable Servers

**silenceper/mcp-k8s** (143 stars, Go, Apache-2.0) — Resource CRUD plus full Helm release and repository management. Helm operations can be independently enabled/disabled. Supports stdio, SSE, and Streamable HTTP transport.

**zekker6/mcp-helm** (22 stars, Go, MIT, v1.3.3 March 2026) — Dedicated Helm MCP server with 7 tools for chart inspection: list charts, list versions, get values, get contents, get dependencies, get images. Supports HTTP repos and OCI registries. Public test instance at `mcp-helm.zekker.dev/mcp`. Solves the specific problem of LLMs making up Helm values.yaml contents.

**portainer/portainer-mcp** (132 stars, Go, Zlib, v0.7.0) — Portainer management server with 40+ tools including Kubernetes API proxying. Read-only mode available. Designed for teams already using Portainer for cluster management.

**SUSE Rancher Prime** (announced KubeCon EU 2026) — **Built-in MCP server** in the Rancher management platform. "Liz" AI assistant expanded into multi-agent "Crew" architecture with specialized agents (Security, Observability, Platform, Linux, App Collection). External MCP server integration available via Global Settings. Partners (Fsas Technologies, n8n, Revenium, Stacklock, AWS) can invoke SUSE's embedded MCP server. **First enterprise Kubernetes management platform with native MCP** — a significant shift from standalone MCP servers to platform-embedded AI interfaces.

**mrostamii/rancher-mcp-server** — Community MCP server for the Rancher ecosystem covering multi-cluster Kubernetes via Steve API and Norman management API, **Fleet GitOps** (GitRepo, Bundle, cluster list, drift detection), and **Harvester HCI** (VMs, storage, networks). Fills the fleet management gap identified in the original review.

**jmrplens/portainer-mcp-enhanced** — Enhanced fork of portainer-mcp with **98 tools** covering the full Portainer API surface, including K8s proxy. Significant upgrade over the original portainer-mcp (40+ tools).

**AWS EKS/ECS MCP** (still in preview) — Fully managed cloud-hosted MCP servers from AWS. IAM integration, CloudTrail audit logging. Not open-source. No GA announcement as of May 2026. AWS predicts 2026 as "the year of agentic workloads in production on EKS."

## Developer Tools MCP Comparison

| Aspect | GitHub | GitLab | Bitbucket | Docker | Kubernetes | CI/CD | IDE/Editor | Testing/QA | Monitoring | Security | IaC | Packages | Code Gen | API Dev | Logging | DB Migration | Doc Tooling | Debugging | Profiling | Code Review |
|--------|--------|--------|-----------|--------|------------|-------|------------|------------|------------|---------- | ------- |----------|----------|---------|---------------------- | --------------|-----------|-----------|-------------|
| **Official MCP server** | Yes (28.2k stars, 21 toolsets) | Yes (built-in, 15 tools, Premium+) | No (Jira/Confluence only) | [Hub MCP (132 stars, 12+ tools)](/reviews/docker-mcp-servers/) | No (Red Hat leads, 1.5k stars) | [Yes (Jenkins, CircleCI, Buildkite)](/reviews/ci-cd-mcp-servers/) | Yes (JetBrains built-in, 24 tools) | [Yes (MS Playwright, 9.8k stars, 24 tools)](/reviews/testing-qa-mcp-servers/) | [Yes (Grafana 2.5k, Datadog, Sentry, Dynatrace, New Relic, Instana)](/reviews/monitoring-observability-mcp-servers/) | [Yes (Semgrep, SonarQube, Snyk, Trivy, GitGuardian, Cycode, Contrast)](/reviews/security-scanning-mcp-servers/) | Yes (Terraform 1.3k, Pulumi remote, AWS IaC, OpenTofu 84) | Yes (NuGet built-in VS 2026, Homebrew built-in) | Partial (Vercel next-devtools 694, E2B 384, JetBrains built-in server) | Yes (Postman 192, Apollo GraphQL 275, Kong deprecated, Apigee, MuleSoft) | Yes (Splunk 13 tools GA, Grafana Tempo built-in, Grafana Loki 103 stars) | Partial (Liquibase private preview 19 tools, Prisma built-in CLI v6.6.0+) | Yes (Microsoft Learn 1.5k, Mintlify auto, ReadMe per-project, Stainless, OpenAI Docs) | Yes (Chrome DevTools 31k, Microsoft DebugMCP 263, MCP Inspector 9.2k official) | Partial (CodSpeed MCP, Polar Signals remote, Grafana Pyroscope via mcp-grafana) | Yes (SonarQube 442 stars, Codacy 56 stars, Graphite GT built-in) |
| **Remote hosting** | Yes (`api.githubcopilot.com/mcp/`) | No | No | No | AWS EKS MCP (preview) | [Yes (Buildkite remote MCP)](/reviews/ci-cd-mcp-servers/) | No (requires running IDE) | [No (local browser required)](/reviews/testing-qa-mcp-servers/) | [Yes (Datadog, Sentry — OAuth)](/reviews/monitoring-observability-mcp-servers/) | [No (all local/CLI-based)](/reviews/security-scanning-mcp-servers/) | [Yes (Pulumi remote MCP)](/reviews/infrastructure-as-code-mcp-servers/) | N/A | N/A | N/A | N/A | — | N/A | No (local debuggers) | No (local profiling agents) | N/A |
| **Top community server** | GitMCP (7.8k stars) | zereight/gitlab-mcp (1.2k stars) | aashari (132 stars) | [ckreiling (691 stars, 25 tools)](/reviews/docker-mcp-servers/) | Flux159 (1.4k stars, 20+ tools) | [Argo CD (356 stars, 12 tools)](/reviews/ci-cd-mcp-servers/) | vscode-mcp-server (342 stars, 15 tools) | [executeautomation (5.3k stars)](/reviews/testing-qa-mcp-servers/) | [pab1it0/prometheus (340 stars)](/reviews/monitoring-observability-mcp-servers/) | [CodeQL community (143 stars)](/reviews/security-scanning-mcp-servers/) | Ansible (25 stars, 40+ tools) | mcp-package-version (122 stars, 9 registries) | Context7 (50.3k stars), magic-mcp (4.5k stars) | openapi-mcp-generator (495 stars), mcp-graphql (374 stars) | cr7258/elasticsearch (259 stars), Traceloop OTel (178 stars) | mpreziuso/mcp-atlas (Atlas), defrex/drizzle-mcp (Drizzle) | GitMCP (7.8k stars), Grounded Docs (1.2k stars), Docs MCP (87 stars) | claude-debugs-for-you (496 stars), x64DbgMCPServer (398 stars), devtools-debugger (341 stars) | theSharque/mcp-jperf (Java JFR), PageSpeed Insights MCP servers | kopfrechner/gitlab-mr-mcp (86 stars), crazyrabbitLTC (32 stars) |
| **Community tool count** | 28+ (local Git) | 100+ | 25+ | 25 (container mgmt) | 20+ (core) to 253+ (claimed) | [9-21 per server](/reviews/ci-cd-mcp-servers/) | 13-19 per server | [24 (official) + API testing](/reviews/testing-qa-mcp-servers/) | [16+ (Datadog) to 100+ (Instana)](/reviews/monitoring-observability-mcp-servers/) | [7 (Semgrep) to full platform (Snyk)](/reviews/security-scanning-mcp-servers/) | [20+ (Terraform), full platform (Pulumi)](/reviews/infrastructure-as-code-mcp-servers/) | N/A | N/A | Spec-to-server conversion + API interaction | N/A | — | N/A | N/A | N/A | N/A |
| **Server/DC support** | N/A (cloud-only) | Community servers | garc33 (57 stars, 21 tools) | All local | All local + cloud managed | [Jenkins plugin (on-prem)](/reviews/ci-cd-mcp-servers/) | N/A | N/A | [Grafana, Prometheus (self-hosted)](/reviews/monitoring-observability-mcp-servers/) | [Yes (all local/CLI-based)](/reviews/security-scanning-mcp-servers/) | [Yes (all local/CLI-based)](/reviews/infrastructure-as-code-mcp-servers/) | N/A | N/A | 4+ (Postman, Apollo, Kong, Google/Apigee, MuleSoft) | N/A | — | N/A | N/A | N/A | N/A |
| **Helm/package mgmt** | N/A | N/A | N/A | [Compose support](/reviews/docker-mcp-servers/) | Native in top 2 servers | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | Bidirectional (spec-to-tools, API execution) | N/A | — | N/A | N/A | N/A | N/A |
| **Read-only mode** | N/A | N/A | Safety-first (no DELETE) | N/A | Yes (both leaders) | [Limited](/reviews/ci-cd-mcp-servers/) | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | — | N/A | N/A | N/A | N/A |
| **Authentication** | PAT / GitHub App | OAuth 2.0 / PAT | App Password / OAuth | Docker Desktop credentials | kubeconfig / OAuth / OIDC | [API tokens per platform](/reviews/ci-cd-mcp-servers/) | Local connection (port/stdio) | [None (local browsers)](/reviews/testing-qa-mcp-servers/) | [API tokens / OAuth (remote)](/reviews/monitoring-observability-mcp-servers/) | [API tokens / CLI auth](/reviews/security-scanning-mcp-servers/) | API tokens / OAuth / CLI auth | None (public registries) | API keys (Context7, magic-mcp, E2B) | API keys / Bearer / OAuth / 1Password | API tokens / OAuth / RBAC (Splunk) | Database credentials / CLI auth | None (GitMCP, MS Learn) / API keys (platform MCP) | None (local debuggers) / Chrome DevTools auto-connect | API keys (CodSpeed, Polar Signals) / Grafana auth / Google API key (PageSpeed) | API tokens (SonarQube, Codacy) / GitHub PAT / GitLab PAT |
| **AAIF membership** | No (but Microsoft is Platinum) | No | No | [Gold](/reviews/docker-mcp-servers/) | No (but Google/AWS/MS are Platinum) | [No](/reviews/ci-cd-mcp-servers/) | No (but Microsoft is Platinum) | [No (but Microsoft is Platinum)](/reviews/testing-qa-mcp-servers/) | [No](/reviews/monitoring-observability-mcp-servers/) | [No](/reviews/security-scanning-mcp-servers/) | No | No (but Microsoft is Platinum) | No | No | No | No | No (but Microsoft is Platinum) | No (but Google/Microsoft are Platinum) | No | No |
| **Platform users** | 180M+ developers | 30M+ users | ~41k companies | 20M+ users | 5.6M developers | [Jenkins: 11.3M devs](/reviews/ci-cd-mcp-servers/) | VS Code: 75.9% market share | [Playwright: 45.1% QA adoption](/reviews/testing-qa-mcp-servers/) | [Datadog: 32.7k customers](/reviews/monitoring-observability-mcp-servers/) | [SonarQube: 17.7% SAST mindshare](/reviews/security-scanning-mcp-servers/) | Terraform: millions of users, 45% IaC adoption | npm: 5B+ weekly downloads, PyPI: 421.6B yearly | Copilot: 20M+ users, Cursor: 1M+ DAU | Postman: 30M+ users, REST: ~83% of web APIs | Splunk: 15k+ customers, ELK: most-deployed log stack | Prisma: 43k stars, Flyway: 10.7k stars, Atlas: 6.3k stars | Mintlify: 28k+ stars, Docusaurus: 60k+ stars, ReadMe: powering major API docs | Chrome: 65%+ browser share, VS Code: 75.9% IDE share, x64dbg: 45k+ stars | APM market: $7-10B, Pyroscope: 11k+ stars, async-profiler: 9k+ stars | SonarQube: 7.4M+ users, CodeRabbit: top AI reviewer, Qodo/PR-Agent: 10.5k stars |
| **Our rating** | [4.5/5](/reviews/github-mcp-server/) | [3.5/5](/reviews/gitlab-mcp-server/) | [2.5/5](/reviews/bitbucket-mcp-server/) | [4/5](/reviews/docker-mcp-servers/) | 4/5 | [3/5](/reviews/ci-cd-mcp-servers/) | [3.5/5](/reviews/ide-code-editor-mcp-servers/) | [3.5/5](/reviews/testing-qa-mcp-servers/) | [4/5](/reviews/monitoring-observability-mcp-servers/) | [3.5/5](/reviews/security-scanning-mcp-servers/) | [4/5](/reviews/infrastructure-as-code-mcp-servers/) | [3/5](/reviews/package-management-mcp-servers/) | [3.5/5](/reviews/code-generation-mcp-servers/) | [3.5/5](/reviews/api-development-mcp-servers/) | [3.5/5](/reviews/logging-tracing-mcp-servers/) | [2.5/5](/reviews/database-migration-mcp-servers/) | [3.5/5](/reviews/documentation-tooling-mcp-servers/) | [4.5/5](/reviews/debugging-mcp-servers/) | [3/5](/reviews/profiling-performance-mcp-servers/) | [3.5/5](/reviews/code-review-pull-request-mcp-servers/) |

## Known Issues

1. **No official CNCF/Kubernetes MCP server** — Unlike GitHub (official server with 28.2k stars) or Docker (MCP Gateway, MCP Catalog), there is no CNCF-maintained MCP server. Red Hat's server under the `containers` org is the closest, but it's a vendor project with OpenShift-specific toolsets. CNCF published Cloud Native Agentic Standards (March 2026) referencing MCP, but MCP is governed by AAIF, not CNCF. The community has filled the gap well, but official backing would consolidate the ecosystem.

2. **CVE history in Flux159 raises security concerns** — Flux159/mcp-server-kubernetes has **5 security advisories**, including CVE-2026-39884 (High, argument injection in port_forward) and CVE-2025-53355 (High, command injection). The pattern of command/argument injection vulnerabilities — where user input is concatenated into shell commands — suggests architectural risk in the kubectl-wrapping approach. Red Hat's native Go implementation has zero CVEs. Organizations should prefer array-based command construction and audit MCP server security advisories.

3. **Security risk with cluster-admin access** — Kubernetes MCP servers that use kubeconfig inherit whatever permissions are configured. An AI agent with cluster-admin access could delete namespaces, evict pods, or modify RBAC rules. Both leading servers offer read-only modes, but this is opt-in — the default is full access. CNCF's new Cloud Native Agentic Standards recommend "narrowly scoped MCP server tooling access." Red Hat's new **confirmation rules system** (v0.0.60) adds interactive confirmation before destructive operations — a meaningful safety improvement.

4. **Pre-1.0 versioning across the board** — The top servers are all pre-1.0: Flux159 at v3.5.0 (npm-style versioning), Red Hat at v0.0.61 (with a breaking change in v0.0.60), strowk at v0.6.1 (dormant). Red Hat's breaking change in v0.0.60 (user-scoped targets) confirms API instability. Tool names, parameters, and behavior may change between releases.

5. **Tool count inflation** — rohitg00/kubectl-mcp-server claims 253+ tools, but with only 133 commits this is difficult to verify. Some "tools" may be thin wrappers that construct kubectl commands. Users should test actual capabilities rather than relying on tool count claims.

6. **Helm integration varies widely** — Some servers include Helm natively (Flux159, Red Hat, silenceper), some wrap the Helm CLI (alexei-led), and dedicated servers exist (zekker6/mcp-helm). The fragmentation means different capability levels: native servers can install/upgrade/uninstall releases, while the Helm-specific server focuses on chart inspection. Red Hat's v0.0.60 added chart reference validation and registry configuration, improving Helm coverage.

7. **Multi-cluster management gap narrowing** — All top servers support multiple clusters via kubeconfig contexts, but standalone MCP servers still provide one-context-at-a-time access. **NEW: SUSE Rancher Prime's built-in MCP server** and **mrostamii/rancher-mcp-server** with Fleet GitOps now provide fleet-level visibility — partially closing the gap identified in the original review. For organizations running 6+ production clusters, Rancher-based solutions are now the first viable fleet management MCP option.

8. **Secret exposure risk despite masking** — Both leading servers implement secret redaction, but this is pattern-based (tokens, keys, passwords). Custom secrets with non-standard naming, ConfigMap data that contains credentials, or environment variables with sensitive values may not be caught. Red Hat's server is more aggressive with redaction patterns than Flux159's. Red Hat's new read-only root filesystem and configurable ServiceAccount token auto-mounting (v0.0.61) add defense-in-depth.

9. **Cloud provider authentication improving** — Most servers rely on kubeconfig, which works for local development but creates friction for managed K8s services. **Red Hat's v0.0.61 adds Microsoft Entra ID support** with On-Behalf-Of token exchange — the first K8s MCP server with Azure AD integration. alexei-led's server supports AWS/GKE/AKS credentials natively. AWS EKS MCP remains in preview (no GA as of May 2026). The authentication gap is narrowing but not closed.

10. **No cost visibility** — Kubernetes cost management is a major concern (Kubecost, OpenCost), but the main MCP servers don't include cost data. A community Kubecost MCP server exists, and OpenCost has built-in MCP support, but these are separate tools that don't integrate with cluster management workflows.

11. **Container image size and startup** — Docker-based deployments (alexei-led, Red Hat) bundle Kubernetes CLIs and dependencies into container images that can be several hundred MB. Red Hat now supports **multi-architecture images (s390x, ppc64le)** alongside standard AMD64/ARM64, expanding enterprise platform support but increasing image management complexity.

## Bottom Line

**Rating: 4 out of 5** (holds from March 2026)

Kubernetes has a **strong and maturing MCP ecosystem** despite the absence of an official CNCF server. Red Hat's containers/kubernetes-mcp-server **surged to 1,500 stars (+15%)** with 105 new commits, adding Tekton integration, Microsoft Entra ID auth, confirmation rules, and enterprise hardening (TLS enforcement, read-only root filesystem, multi-arch images). Flux159/mcp-server-kubernetes holds at ~1,400 stars but patched **CVE-2026-39884 (High)** — an argument injection vulnerability exploitable via prompt injection. **SUSE Rancher Prime now ships a built-in MCP server** with multi-agent architecture — the first enterprise K8s management platform with native MCP. Fleet management gap partially closed by Rancher MCP and mrostamii/rancher-mcp-server with Fleet GitOps support.

The **4/5 rating holds** — Red Hat's surge (+15% stars, Tekton, Entra ID, enterprise hardening) and SUSE Rancher's built-in MCP are strong positives, but offset by Flux159's CVE history (5 advisories), strowk's dormancy (6+ months), and continued absence of an official CNCF server. The ecosystem is improving on security (confirmation rules, TLS enforcement, read-only root) and authentication (Entra ID) but still pre-1.0 across the board.

**Who benefits from Kubernetes MCP servers today:**

- **Platform engineers** — Red Hat's server provides native Go performance with OpenShift, Tekton, and KubeVirt support, plus Microsoft Entra ID for Azure-based clusters
- **Development teams** — Flux159's kubectl-style interface with Helm support covers the daily workflow of deploying and debugging applications (ensure v3.5.0+ for security patches)
- **Multi-cloud teams** — alexei-led's server with native EKS/GKE/AKS authentication, plus Red Hat's new Entra ID support, reduce setup friction for managed Kubernetes services
- **Enterprise fleet operators** — **NEW: SUSE Rancher Prime's built-in MCP** and mrostamii/rancher-mcp-server with Fleet GitOps now provide fleet-level visibility across multiple clusters
- **Security-conscious organizations** — Red Hat's confirmation rules, read-only root filesystem, TLS enforcement, and configurable token auto-mounting provide defense-in-depth

**Who should be cautious:**

- **Flux159 users on older versions** — CVE-2026-39884 (argument injection) and CVE-2025-53355 (command injection) are both High severity. Upgrade to v3.5.0 immediately. The exec_in_pod residual risk is still open
- **Production environments without RBAC scoping** — Default kubeconfig access gives AI agents whatever permissions you have. Create dedicated service accounts with minimal RBAC. CNCF's Cloud Native Agentic Standards now recommend "narrowly scoped MCP server tooling access"
- **Teams expecting stability** — All servers are pre-1.0. Red Hat's v0.0.60 introduced a breaking change (user-scoped targets). Pin versions in production configurations
- **Cost-sensitive organizations** — Kubernetes cost data is not integrated into the main MCP servers. You'll need separate Kubecost/OpenCost MCP integrations

---

*This review was researched and written by an AI agent. We do not have hands-on access to these tools — our analysis is based on documentation, GitHub repositories, community reports, and official announcements. Information is current as of May 2026. See our [About page](/about/) for details on our review process.*

