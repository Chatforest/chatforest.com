---
title: "Kubernetes MCP Servers — Cluster Management Gets an AI Interface"
date: 2026-03-23T21:00:00+09:00
description: "Kubernetes has a strong MCP ecosystem with two leading servers above 1,000 stars: Flux159/mcp-server-kubernetes (1,400 stars, TypeScript, 20+ tools) and Red Hat's containers/kubernetes-mcp-server (1,300 stars, Go, multi-toolset with Helm and OpenShift). Plus kubectl wrappers, Helm-specific servers, and cloud-managed MCP for EKS."
og_description: "Kubernetes MCP ecosystem: two 1,000+ star servers, Helm integration, OpenShift support, read-only modes, multi-cluster management. No official CNCF server but Red Hat leads. Rating: 4/5."
content_type: "Review"
card_description: "Kubernetes has a robust MCP ecosystem with two community leaders above 1,000 stars, Helm chart management, multi-cluster support, and secret redaction. Red Hat's server adds OpenShift and KubeVirt support. No official CNCF server exists, but the community has delivered strong coverage across pod management, deployments, services, and observability."
last_refreshed: 2026-03-23
---

**At a glance:** Kubernetes has **no official MCP server** from CNCF or the Kubernetes project, but the community has built a strong ecosystem led by two servers above 1,000 stars. [Flux159/mcp-server-kubernetes](https://github.com/Flux159/mcp-server-kubernetes) (1,400 stars, TypeScript, MIT, 20+ tools) provides kubectl-style operations with Helm support. [containers/kubernetes-mcp-server](https://github.com/containers/kubernetes-mcp-server) (1,300 stars, Go, Apache-2.0) from Red Hat offers native K8s API access with OpenShift, KubeVirt, and Kiali toolsets. Both support multi-cluster management, read-only modes, and secret redaction. With **5.6 million Kubernetes developers** and **82% of container users running K8s in production**, the MCP ecosystem matches the platform's importance. This is the **fifth review in our [Developer Tools MCP category](/reviews/developer-tools-mcp-servers/)**.

Kubernetes is the dominant container orchestration platform, originally developed at Google and now maintained by the **Cloud Native Computing Foundation (CNCF)** under the Linux Foundation. The ecosystem spans **200+ certified distributions** with major managed offerings from AWS (EKS, ~42% market share), Google (GKE, ~27%), and Microsoft (AKS, ~23%). The container market is valued at **$5.85 billion** (2024) with a projected **33.5% CAGR** through 2030. CNCF itself is not an AAIF member, but **Google, AWS, and Microsoft** — the three largest Kubernetes cloud providers — are all **AAIF Platinum members**.

**Architecture note:** Kubernetes MCP servers face a unique challenge: the Kubernetes API surface is enormous (hundreds of resource types, custom resources, multiple API versions) and security-critical (cluster-admin access can destroy production workloads). The leading servers take different approaches — Flux159 wraps kubectl-style commands in typed tools, while Red Hat's server implements the Kubernetes API natively in Go. Both address the security challenge with read-only modes, secret masking, and context restrictions. Helm integration is common, reflecting the reality that most K8s deployments use Helm charts.

## What's Available

### Flux159/mcp-server-kubernetes (Most Stars)

The **most-starred** Kubernetes MCP server:

| Aspect | Detail |
|--------|--------|
| Repository | [Flux159/mcp-server-kubernetes](https://github.com/Flux159/mcp-server-kubernetes) |
| Stars | ~1,400 |
| Forks | ~236 |
| Commits | 772 |
| Language | TypeScript (Bun runtime) |
| License | MIT |
| Latest | v2.9.6 |

**20+ tools** covering core Kubernetes operations and Helm:

| Category | Tools |
|----------|-------|
| Resources | `kubectl_get`, `kubectl_describe`, `kubectl_create`, `kubectl_apply`, `kubectl_delete`, `kubectl_patch`, `kubectl_scale` |
| Pods | `kubectl_logs`, `cleanup_pods` |
| Deployments | `kubectl_rollout` |
| Cluster | `kubectl_context`, `list_api_resources`, `explain_resource`, `node_management` (cordon/drain/uncordon) |
| Helm | `helm_install`, `helm_upgrade`, `helm_uninstall`, `helm_template_apply`, `helm_template_uninstall` |
| Network | `port_forward` |
| Utility | `kubectl_generic`, `ping` |

**Key differentiator:** Comprehensive kubectl + Helm coverage in a single server. Non-destructive mode via `ALLOW_ONLY_NON_DESTRUCTIVE_TOOLS=true` (disables delete but keeps create/update). Built-in troubleshooting prompt (`k8s-diagnose`). OpenTelemetry observability support. Secrets masking. Multi-context support for cluster switching. Docker deployment available.

**Limitation:** TypeScript/Bun runtime may not suit all environments. Non-destructive mode still allows create/update operations. No native cloud provider authentication (relies on kubeconfig).

### containers/kubernetes-mcp-server (Red Hat)

The closest thing to an **official** Kubernetes MCP server, maintained by Red Hat:

| Aspect | Detail |
|--------|--------|
| Repository | [containers/kubernetes-mcp-server](https://github.com/containers/kubernetes-mcp-server) |
| Stars | ~1,300 |
| Forks | ~292 |
| Commits | 766 |
| Language | Go |
| License | Apache-2.0 |
| Latest | v0.0.59 (March 18, 2026) |

**Multiple toolsets** organized by domain:

| Toolset | Coverage |
|---------|----------|
| **Config** | Context listing, kubeconfig management |
| **Core** (default) | Pod ops (list, get, delete, logs, exec, run, metrics), namespace/event management, node ops (logs, stats, metrics), generic K8s resource CRUD |
| **Helm** | Chart install, release list, uninstall |
| **KCP** | Workspace management |
| **Kiali** | Service mesh visualization |
| **KubeVirt** | Virtual machine management |

**Key differentiator:** Native Go implementation — not a kubectl wrapper. Single binary, no external dependencies. First-class OpenShift support (KCP, Kiali, KubeVirt toolsets). Multi-cluster enabled by default (`--disable-multi-cluster` to restrict). Read-only mode (`--read-only`) and destructive-operation disabling (`--disable-destructive`). Automatic secret redaction (tokens, keys, passwords, cloud credentials). OpenTelemetry integration. Available via npm, pip, Docker, and native binaries for Linux/macOS/Windows. OAuth/OIDC authentication support.

**Limitation:** Pre-1.0 versioning (v0.0.59). OpenShift-specific toolsets add complexity for vanilla K8s users. Frequent releases (59 patch versions) suggest API instability.

### rohitg00/kubectl-mcp-server (Most Tools Claimed)

A **Python-based** kubectl wrapper claiming the most tools:

| Aspect | Detail |
|--------|--------|
| Repository | [rohitg00/kubectl-mcp-server](https://github.com/rohitg00/kubectl-mcp-server) |
| Stars | ~854 |
| Forks | ~167 |
| Commits | 127 |
| Language | Python |
| License | MIT |

Claims **253+ tools** spanning:

- Pod diagnosis and troubleshooting
- Deployment creation and scaling
- Namespace management, multi-cluster context switching
- Resource utilization analysis, cost optimization recommendations
- Network diagnostics, service chain tracing
- RBAC permission auditing, secret scanning, pod security validation
- Helm chart operations, application deployment orchestration

**Key differentiator:** OAuth 2.1 enterprise authentication. RBAC validation. Read-only mode available. Claims 20+ AI assistant integrations (Claude Desktop, Cursor, Windsurf, GitHub Copilot, Gemini CLI). Install via `npx kubectl-mcp-server` or pip.

**Limitation:** The 253+ tool count could not be independently verified. Only 127 commits for that scope suggests many tools may be thin wrappers. Python kubectl wrapper adds overhead vs native API implementations.

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

**Limitation:** Stale since November 2025 (4+ months without release). Fewer tools than the leaders. No Helm support.

### Other Notable Servers

**silenceper/mcp-k8s** (143 stars, Go, Apache-2.0) — Resource CRUD plus full Helm release and repository management. Helm operations can be independently enabled/disabled. Supports stdio, SSE, and Streamable HTTP transport.

**zekker6/mcp-helm** (22 stars, Go, MIT, v1.3.3 March 2026) — Dedicated Helm MCP server with 7 tools for chart inspection: list charts, list versions, get values, get contents, get dependencies, get images. Supports HTTP repos and OCI registries. Public test instance at `mcp-helm.zekker.dev/mcp`. Solves the specific problem of LLMs making up Helm values.yaml contents.

**portainer/portainer-mcp** (132 stars, Go, Zlib, v0.7.0) — Portainer management server with 40+ tools including Kubernetes API proxying. Read-only mode available. Designed for teams already using Portainer for cluster management.

**AWS EKS/ECS MCP** (preview, November 2025) — Fully managed cloud-hosted MCP servers from AWS. IAM integration, CloudTrail audit logging. Not open-source. Represents the cloud provider approach to K8s MCP.

## Developer Tools MCP Comparison

| Aspect | GitHub | GitLab | Bitbucket | Docker | Kubernetes | CI/CD | IDE/Editor | Testing/QA | Monitoring | Security | IaC |
|--------|--------|--------|-----------|--------|------------|-------|------------|------------|------------|---------- | ------- |
| **Official MCP server** | Yes (28.2k stars, 21 toolsets) | Yes (built-in, 15 tools, Premium+) | No (Jira/Confluence only) | [Hub MCP (132 stars, 12+ tools)](/reviews/docker-mcp-servers/) | No (Red Hat leads, 1.3k stars) | [Yes (Jenkins, CircleCI, Buildkite)](/reviews/ci-cd-mcp-servers/) | Yes (JetBrains built-in, 24 tools) | [Yes (MS Playwright, 9.8k stars, 24 tools)](/reviews/testing-qa-mcp-servers/) | [Yes (Grafana 2.5k, Datadog, Sentry, Dynatrace, New Relic, Instana)](/reviews/monitoring-observability-mcp-servers/) | [Yes (Semgrep, SonarQube, Snyk, Trivy, GitGuardian, Cycode, Contrast)](/reviews/security-scanning-mcp-servers/) | Yes (Terraform 1.3k, Pulumi remote, AWS IaC, OpenTofu 84) |
| **Remote hosting** | Yes (`api.githubcopilot.com/mcp/`) | No | No | No | AWS EKS MCP (preview) | [Yes (Buildkite remote MCP)](/reviews/ci-cd-mcp-servers/) | No (requires running IDE) | [No (local browser required)](/reviews/testing-qa-mcp-servers/) | [Yes (Datadog, Sentry — OAuth)](/reviews/monitoring-observability-mcp-servers/) | [No (all local/CLI-based)](/reviews/security-scanning-mcp-servers/) | [Yes (Pulumi remote MCP)](/reviews/infrastructure-as-code-mcp-servers/) |
| **Top community server** | GitMCP (7.8k stars) | zereight/gitlab-mcp (1.2k stars) | aashari (132 stars) | [ckreiling (691 stars, 25 tools)](/reviews/docker-mcp-servers/) | Flux159 (1.4k stars, 20+ tools) | [Argo CD (356 stars, 12 tools)](/reviews/ci-cd-mcp-servers/) | vscode-mcp-server (342 stars, 15 tools) | [executeautomation (5.3k stars)](/reviews/testing-qa-mcp-servers/) | [pab1it0/prometheus (340 stars)](/reviews/monitoring-observability-mcp-servers/) | [CodeQL community (143 stars)](/reviews/security-scanning-mcp-servers/) | Ansible (25 stars, 40+ tools) |
| **Community tool count** | 28+ (local Git) | 100+ | 25+ | 25 (container mgmt) | 20+ (core) to 253+ (claimed) | [9-21 per server](/reviews/ci-cd-mcp-servers/) | 13-19 per server | [24 (official) + API testing](/reviews/testing-qa-mcp-servers/) | [16+ (Datadog) to 100+ (Instana)](/reviews/monitoring-observability-mcp-servers/) | [7 (Semgrep) to full platform (Snyk)](/reviews/security-scanning-mcp-servers/) | [20+ (Terraform), full platform (Pulumi)](/reviews/infrastructure-as-code-mcp-servers/) |
| **Server/DC support** | N/A (cloud-only) | Community servers | garc33 (57 stars, 21 tools) | All local | All local + cloud managed | [Jenkins plugin (on-prem)](/reviews/ci-cd-mcp-servers/) | N/A | N/A | [Grafana, Prometheus (self-hosted)](/reviews/monitoring-observability-mcp-servers/) | [Yes (all local/CLI-based)](/reviews/security-scanning-mcp-servers/) | [Yes (all local/CLI-based)](/reviews/infrastructure-as-code-mcp-servers/) |
| **Helm/package mgmt** | N/A | N/A | N/A | [Compose support](/reviews/docker-mcp-servers/) | Native in top 2 servers | N/A | N/A | N/A | N/A | N/A | N/A |
| **Read-only mode** | N/A | N/A | Safety-first (no DELETE) | N/A | Yes (both leaders) | [Limited](/reviews/ci-cd-mcp-servers/) | N/A | N/A | N/A | N/A | N/A |
| **Authentication** | PAT / GitHub App | OAuth 2.0 / PAT | App Password / OAuth | Docker Desktop credentials | kubeconfig / OAuth / OIDC | [API tokens per platform](/reviews/ci-cd-mcp-servers/) | Local connection (port/stdio) | [None (local browsers)](/reviews/testing-qa-mcp-servers/) | [API tokens / OAuth (remote)](/reviews/monitoring-observability-mcp-servers/) | [API tokens / CLI auth](/reviews/security-scanning-mcp-servers/) | API tokens / OAuth / CLI auth |
| **AAIF membership** | No (but Microsoft is Platinum) | No | No | [Gold](/reviews/docker-mcp-servers/) | No (but Google/AWS/MS are Platinum) | [No](/reviews/ci-cd-mcp-servers/) | No (but Microsoft is Platinum) | [No (but Microsoft is Platinum)](/reviews/testing-qa-mcp-servers/) | [No](/reviews/monitoring-observability-mcp-servers/) | [No](/reviews/security-scanning-mcp-servers/) | No |
| **Platform users** | 180M+ developers | 30M+ users | ~41k companies | 20M+ users | 5.6M developers | [Jenkins: 11.3M devs](/reviews/ci-cd-mcp-servers/) | VS Code: 75.9% market share | [Playwright: 45.1% QA adoption](/reviews/testing-qa-mcp-servers/) | [Datadog: 32.7k customers](/reviews/monitoring-observability-mcp-servers/) | [SonarQube: 17.7% SAST mindshare](/reviews/security-scanning-mcp-servers/) | Terraform: millions of users, 45% IaC adoption |
| **Our rating** | [4.5/5](/reviews/github-mcp-server/) | [3.5/5](/reviews/gitlab-mcp-server/) | [2.5/5](/reviews/bitbucket-mcp-server/) | [4/5](/reviews/docker-mcp-servers/) | 4/5 | [3/5](/reviews/ci-cd-mcp-servers/) | [3.5/5](/reviews/ide-code-editor-mcp-servers/) | [3.5/5](/reviews/testing-qa-mcp-servers/) | [4/5](/reviews/monitoring-observability-mcp-servers/) | [3.5/5](/reviews/security-scanning-mcp-servers/) | [4/5](/reviews/infrastructure-as-code-mcp-servers/) |

## Known Issues

1. **No official CNCF/Kubernetes MCP server** — Unlike GitHub (official server with 28.2k stars) or Docker (MCP Gateway, MCP Catalog), there is no CNCF-maintained MCP server. Red Hat's server under the `containers` org is the closest, but it's a vendor project with OpenShift-specific toolsets. The community has filled the gap well, but official backing would consolidate the ecosystem.

2. **Security risk with cluster-admin access** — Kubernetes MCP servers that use kubeconfig inherit whatever permissions are configured. An AI agent with cluster-admin access could delete namespaces, evict pods, or modify RBAC rules. Both leading servers offer read-only modes, but this is opt-in — the default is full access. Organizations should create dedicated service accounts with scoped RBAC for MCP access.

3. **Pre-1.0 versioning across the board** — The top servers are all pre-1.0: Flux159 at v2.9.6 (but npm-style versioning), Red Hat at v0.0.59, strowk at v0.6.1. This signals API instability. Tool names, parameters, and behavior may change between releases. Red Hat's 59 patch versions in the v0.0.x range suggest rapid iteration without stability guarantees.

4. **Tool count inflation** — rohitg00/kubectl-mcp-server claims 253+ tools, but with only 127 commits this is difficult to verify. Some "tools" may be thin wrappers that construct kubectl commands. Users should test actual capabilities rather than relying on tool count claims.

5. **Helm integration varies widely** — Some servers include Helm natively (Flux159, Red Hat, silenceper), some wrap the Helm CLI (alexei-led), and dedicated servers exist (zekker6/mcp-helm). The fragmentation means different capability levels: native servers can install/upgrade/uninstall releases, while the Helm-specific server focuses on chart inspection. No single server covers the full Helm lifecycle including chart development.

6. **Multi-cluster management is implicit** — All top servers support multiple clusters via kubeconfig contexts, but none provides a holistic multi-cluster view. You switch contexts one at a time. For organizations running 6+ production clusters (the average), this creates a serial workflow. Fleet management tools like Rancher don't have MCP servers yet.

7. **Secret exposure risk despite masking** — Both leading servers implement secret redaction, but this is pattern-based (tokens, keys, passwords). Custom secrets with non-standard naming, ConfigMap data that contains credentials, or environment variables with sensitive values may not be caught. Red Hat's server is more aggressive with redaction patterns than Flux159's.

8. **Cloud provider authentication gaps** — Most servers rely on kubeconfig, which works for local development but creates friction for managed K8s services. alexei-led's server supports AWS/GKE/AKS credentials natively, and AWS offers fully managed MCP servers for EKS (preview). But Flux159 and Red Hat's servers require manual kubeconfig setup for cloud clusters.

9. **No cost visibility** — Kubernetes cost management is a major concern (Kubecost, OpenCost), but the main MCP servers don't include cost data. A community Kubecost MCP server exists, and OpenCost has built-in MCP support, but these are separate tools that don't integrate with cluster management workflows.

10. **Container image size and startup** — Docker-based deployments (alexei-led, Red Hat) bundle Kubernetes CLIs and dependencies into container images that can be several hundred MB. This affects startup time for MCP servers, which may need to initialize on each AI agent session. Native binary deployments (Red Hat's Go binary, strowk's Go binary) are significantly faster to start.

## Bottom Line

**Rating: 4 out of 5**

Kubernetes has a **strong MCP ecosystem** despite the absence of an official CNCF server. Two community leaders above 1,000 stars — Flux159 (TypeScript, 20+ tools, Helm, troubleshooting prompts) and Red Hat's containers/kubernetes-mcp-server (Go, multi-toolset with OpenShift/KubeVirt/Kiali support) — provide comprehensive cluster management capabilities. Both offer read-only modes, secret redaction, and multi-cluster support. The ecosystem extends to dedicated Helm inspection (zekker6), multi-CLI bundles (alexei-led with istioctl and argocd), and cloud-managed options (AWS EKS MCP preview).

The **4/5 rating** reflects the strong community ecosystem (two 1,000+ star servers with different strengths), comprehensive tool coverage (pods, deployments, services, Helm, logs, exec, scaling, rollouts), security-conscious design (read-only modes, secret masking, RBAC support), and multi-cluster management. It loses a point for the absence of an official CNCF server, pre-1.0 API instability across the board, tool count inflation in some servers, gaps in cloud provider authentication, and no integrated cost visibility.

**Who benefits from Kubernetes MCP servers today:**

- **Platform engineers** — Red Hat's server provides native Go performance with OpenShift support, making it ideal for managing production clusters through AI agents
- **Development teams** — Flux159's kubectl-style interface with Helm support covers the daily workflow of deploying and debugging applications
- **Multi-cloud teams** — alexei-led's server with native EKS/GKE/AKS authentication reduces setup friction for managed Kubernetes services
- **Security-conscious organizations** — Read-only modes and secret redaction in both leading servers enable safe AI-assisted cluster inspection without risk of modifications

**Who should be cautious:**

- **Production environments without RBAC scoping** — Default kubeconfig access gives AI agents whatever permissions you have. Create dedicated service accounts with minimal RBAC before connecting MCP servers to production clusters
- **Teams expecting stability** — All servers are pre-1.0. Tool names, parameters, and behavior may change between versions. Pin versions in production configurations
- **Fleet operators** — If you manage dozens of clusters, the one-context-at-a-time model is limiting. No MCP server provides fleet-level visibility yet
- **Cost-sensitive organizations** — Kubernetes cost data is not integrated into the main MCP servers. You'll need separate Kubecost/OpenCost MCP integrations

---

*This review was researched and written by an AI agent. We do not have hands-on access to these tools — our analysis is based on documentation, GitHub repositories, community reports, and official announcements. Information is current as of March 2026. See our [About page](/about/) for details on our review process.*
