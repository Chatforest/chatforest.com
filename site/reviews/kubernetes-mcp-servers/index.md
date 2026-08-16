# Kubernetes MCP Servers — Cluster Management Gets an AI Interface

> Kubernetes has a strong MCP ecosystem with two leading servers above 1,000 stars: Flux159/mcp-server-kubernetes (~1,500 stars, TypeScript, 20+ tools) and Red Hat's containers/kubernetes-mcp-server (~2,000 stars, Go). AWS MCP Server went GA (May 2026). Lens Desktop ships built-in MCP. Rating: 4/5.


**At a glance:** Kubernetes has **no official MCP server** from CNCF or the Kubernetes project, but the community has built a strong ecosystem led by two servers above 1,000 stars. [Flux159/mcp-server-kubernetes](https://github.com/Flux159/mcp-server-kubernetes) (~1,500 stars, TypeScript, MIT, 20+ tools) provides kubectl-style operations with Helm support — it has accumulated [**six security advisories since inception, including two CRITICAL argument-injection CVEs found after our last audit**](https://github.com/Flux159/mcp-server-kubernetes/security/advisories); the current release is v4.1.4 and all known CVEs are patched as of that version. [containers/kubernetes-mcp-server](https://github.com/containers/kubernetes-mcp-server) (~2,000 stars, Go, Apache-2.0) from Red Hat leads with Tekton integration and Microsoft Entra ID auth, now at [v0.0.66](https://github.com/containers/kubernetes-mcp-server/releases). **NEW: [kagent](https://github.com/kagent-dev/kagent) (~3,500 stars, [CNCF Sandbox](https://www.cncf.io/projects/kagent/))** — a Kubernetes-native agentic AI framework with pre-built MCP servers for K8s, Istio, Helm, Argo, Prometheus, Grafana, and Cilium. [**KubeCon EU 2026 held the first Agentics Day**](https://www.cncf.io/blog/2026/02/20/kubecon-cloudnativecon-europe-2026-co-located-event-deep-dive-agentics-day-mcp-agents/) — a dedicated co-located event for MCP + agents on Kubernetes. **Google's [GKE Agent Sandbox](https://cloud.google.com/blog/products/containers-kubernetes/bringing-you-agent-sandbox-on-gke-and-agent-substrate)** (GA) allocates isolated agent sandboxes at sub-second latency (90% of allocations complete within 200ms), and Google separately runs a [**managed remote GKE MCP server**](https://docs.cloud.google.com/kubernetes-engine/docs/reference/mcp) (`container.googleapis.com/mcp`) for cluster management — two distinct GKE offerings, not one. [**NEW: Lens Desktop**](https://www.mirantis.com/company/press-center/company-news/lens-launches-built-in-mcp-server-connecting-ai-coding-assistants-to-kubernetes/) (Mirantis, 1M+ users) launched a built-in MCP server (March 18, 2026) — the first major K8s management tool to ship one. [**AWS MCP Server went GA**](https://aws.amazon.com/blogs/aws/the-aws-mcp-server-is-now-generally-available/) (May 6, 2026) covering all AWS services including EKS/ECS. [CNCF nearly doubled certified Kubernetes AI platforms (18 to 31) and added agentic workflow validation to the conformance program](https://www.cncf.io/announcements/2026/03/24/cncf-nearly-doubles-certified-kubernetes-ai-platforms/). With [**82% of container users running K8s in production**](https://www.cncf.io/announcements/2026/01/20/kubernetes-established-as-the-de-facto-operating-system-for-ai-as-production-use-hits-82-in-2025-cncf-annual-cloud-native-survey/), the MCP ecosystem matches the platform's importance. This is the **fifth review in our [Developer Tools MCP category](/reviews/ide-code-editor-mcp-servers/)**. Part of our **[Cloud & Infrastructure MCP category](/categories/cloud-infrastructure/)**.

Kubernetes is the dominant container orchestration platform, originally developed at Google and now maintained by the **Cloud Native Computing Foundation (CNCF)** under the Linux Foundation. The ecosystem spans [**90+ certified offerings**](https://www.cncf.io/training/certification/software-conformance/) with major managed offerings from AWS (EKS), Google (GKE), and Microsoft (AKS). The [container market is valued at **$5.85 billion**](https://www.grandviewresearch.com/industry-analysis/application-container-market) (2024) with a projected **33.5% CAGR** through 2030. CNCF itself is not an AAIF member, but **Google, AWS, and Microsoft** — the three largest Kubernetes cloud providers — are all **AAIF Platinum members**. MCP is now governed by the [**Agentic AI Foundation (AAIF)**](https://www.linuxfoundation.org/press/linux-foundation-announces-the-formation-of-the-agentic-ai-foundation) under the Linux Foundation, with [170+ member organizations and 110M+ monthly MCP SDK downloads](https://aaif.io/blog/mcp-is-now-enterprise-infrastructure-everything-that-happened-at-mcp-dev-summit-north-america-2026/).

**Architecture note:** Kubernetes MCP servers face a unique challenge: the Kubernetes API surface is enormous (hundreds of resource types, custom resources, multiple API versions) and security-critical (cluster-admin access can destroy production workloads). The leading servers take different approaches — Flux159 wraps kubectl-style commands in typed tools, while Red Hat's server implements the Kubernetes API natively in Go. Both address the security challenge with read-only modes, secret masking, and context restrictions. Helm integration is common, reflecting the reality that most K8s deployments use Helm charts. **New in 2026:** [CNCF's Cloud Native Agentic Standards](https://www.cncf.io/blog/2026/03/23/cloud-native-agentic-standards/) recommend "narrowly scoped MCP server tooling access" — validating the read-only-by-default approach. [Google has shipped a **stateless MCP transport**](https://developers.googleblog.com/scaling-ai-agent-infrastructure-with-the-mcp-stateless-updates/) removing session pinning for horizontal scaling on Kubernetes and Cloud Run — the 2026-07-28 MCP spec update makes this the protocol default. **KubeCon EU 2026 Agentics Day** featured MCP sessions across every track — [Akuity and Intuit presented an open-source Argo CD MCP server](https://kccnceu2026.sched.com/event/2EIbg/the-10x-devops-engineers-toolkit-argo-cd-+-ai-driven-mcp-automation-alexander-matyushentsev-akuity-leonardo-luz-almeida-intuit) enabling agent-driven rollbacks and multi-environment coordination, [Buoyant's Linkerd added native MCP support](https://www.buoyant.io/blog/introducing-mcp-support-for-linkerd) (previewed at KubeCon NA 2025, positioned as the first service mesh with MCP-aware routing), and [Google discussed GKE Agent Sandbox](https://cloud.google.com/blog/products/containers-kubernetes/bringing-you-agent-sandbox-on-gke-and-agent-substrate) (which had debuted in preview at KubeCon NA 2025 and reached GA by mid-2026).

## What's Available

### Flux159/mcp-server-kubernetes (Most Stars)

The **most-starred** Kubernetes MCP server:

| Aspect | Detail |
|--------|--------|
| Repository | [Flux159/mcp-server-kubernetes](https://github.com/Flux159/mcp-server-kubernetes) |
| Stars | ~1,500 |
| Forks | ~275 |
| Commits | 785+ |
| Language | TypeScript (Bun runtime) |
| License | MIT |
| Latest | [v4.1.4](https://github.com/Flux159/mcp-server-kubernetes/releases) |

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

**Security alert: Flux159 has accumulated six published security advisories** since inception — a recurring pattern of argument/command injection stemming from the kubectl-wrapping approach:

- [CVE-2026-61459](https://nvd.nist.gov/vuln/detail/CVE-2026-61459) (CVSS 9.8, **Critical**) — argument injection via `resourceType`/`name` in `kubectl_get`, `kubectl_describe`, `kubectl_delete`, enabling `--server` flag injection and bearer-token exfiltration. Affected < 3.9.0; patched in 3.9.0.
- [CVE-2026-46519](https://github.com/Flux159/mcp-server-kubernetes/security/advisories/GHSA-cr22-wjx7-2w6m) (CVSS 8.8, High) — the `ALLOW_ONLY_READONLY_TOOLS`/`ALLOW_ONLY_NON_DESTRUCTIVE_TOOLS` restrictions were enforced only at tool-listing time, not execution time, letting clients call restricted delete/exec tools directly. Affected < 3.6.0; patched in 3.6.0.
- [CVE-2026-39884](https://github.com/Flux159/mcp-server-kubernetes/security/advisories/GHSA-4xqg-gf5c-ghwq) (CVSS 8.3, High) — argument injection in `port_forward` via space-splitting of user input, allowing `--address=0.0.0.0` (exposing internal services) or `-n` cross-namespace flags. Exploitable via prompt injection against connected AI agents. Affected ≤ 3.4.0; patched in 3.5.0.
- [CVE-2026-47250](https://github.com/Flux159/mcp-server-kubernetes/security/advisories/GHSA-6mx4-4h42-r8vh) (CVSS 6.1, Moderate) — unvalidated `kubectl_generic` flags could force kubectl to send an operator's bearer token to an attacker-controlled `--server`. Affected ≤ 3.6.2; patched in 3.7.0.
- [CVE-2025-66404](https://github.com/Flux159/mcp-server-kubernetes/security/advisories/GHSA-wvxp-jp4w-w8wg) (CVSS 8.8, **High** — this review previously mislabeled it Moderate) — shell command injection in `exec_in_pod`. Affected ≤ v2.9.7; patched in v2.9.8.
- [CVE-2025-53355](https://github.com/Flux159/mcp-server-kubernetes/security/advisories/GHSA-gjv4-ghm7-q58q) (CVSS 7.5, High) — command injection via `child_process.execSync` in `kubectl_scale`/`kubectl_patch`. Affected ≤ v2.4.9; patched in v2.5.0.

All six are patched as of the current release, [**v4.1.4**](https://github.com/Flux159/mcp-server-kubernetes/releases) — this review's earlier "upgrade to v3.5.0" guidance is stale; three of the six CVEs above postdate v3.5.0. **Upgrade to the latest release, not merely past v3.5.0.**

**Limitation:** TypeScript/Bun runtime may not suit all environments. Non-destructive mode still allows create/update operations. No native cloud provider authentication (relies on kubeconfig). **Six published security advisories** on this repo alone (see above) — the most CVEs of any K8s MCP server in this review. Separately, an unrelated similarly-named PyPI package, [feiskyer/mcp-kubernetes-server](https://security.snyk.io/vuln/SNYK-PYTHON-MCPKUBERNETESSERVER-12704867), carries its own [two CVEs](https://github.com/mcp-security-project/mcp-cve-project) (CVE-2025-59376, CVE-2025-59377) — do not confuse the two projects when auditing dependencies.

### containers/kubernetes-mcp-server (Red Hat)

The closest thing to an **official** Kubernetes MCP server, maintained by Red Hat — **up ~33% in stars** since our last audit:

| Aspect | Detail |
|--------|--------|
| Repository | [containers/kubernetes-mcp-server](https://github.com/containers/kubernetes-mcp-server) |
| Stars | **~2,000** (up from ~1,500) |
| Forks | ~418 (up from 328) |
| Commits | **~1,028** (up from 871) |
| Language | Go |
| License | Apache-2.0 |
| Latest | [**v0.0.66**](https://github.com/containers/kubernetes-mcp-server/releases) (July 31, 2026) |

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

**New in v0.0.60–v0.0.61** (the server has continued shipping regularly since, reaching [v0.0.66](https://github.com/containers/kubernetes-mcp-server/releases) by late July 2026 with further KubeVirt/Kiali toolset work — see the releases page for the full changelog):
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

**Security posture:** [No published CVEs](https://github.com/containers/kubernetes-mcp-server/security/advisories) as of this audit. Recent hardening: read-only root filesystem, configurable token auto-mounting, TLS enforcement.

**Limitation:** Pre-1.0 versioning (v0.0.66). OpenShift-specific toolsets add complexity for vanilla K8s users. [51 open issues](https://github.com/containers/kubernetes-mcp-server/issues). Breaking change in v0.0.60 (user-scoped targets) — API still unstable.

### rohitg00/kubectl-mcp-server (Most Tools Claimed)

A **Python-based** kubectl wrapper claiming the most tools:

| Aspect | Detail |
|--------|--------|
| Repository | [rohitg00/kubectl-mcp-server](https://github.com/rohitg00/kubectl-mcp-server) |
| Stars | ~949 (up from 877) |
| Forks | ~181 (up from 167) |
| Commits | 133 (unchanged) |
| Language | Python |
| License | MIT |
| Latest | [v1.24.0](https://github.com/rohitg00/kubectl-mcp-server/releases/tag/v1.24.0) (February 2026) |

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
| Stars | ~213 |
| Forks | ~39 |
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
| Stars | ~386 |
| Forks | ~58 |
| Commits | 361 |
| Language | Go |
| License | MIT |
| Latest | [v0.6.1](https://github.com/strowk/mcp-k8s-go/releases/tag/v0.6.1) (**November 2024** — corrected; this review previously misdated it November 2025) |

Tools: list/get/create/modify any K8s resources, list nodes, retrieve events, pod logs, exec into pods. Custom resource mappings for common types. Context restriction via `--allowed-contexts`.

**Key differentiator:** Simple, focused implementation. Read-only mode (`--readonly`). Secret masking enabled by default. Available via npm, Docker, GitHub releases.

**Limitation:** **Dormant since November 2024** ([v0.6.1](https://github.com/strowk/mcp-k8s-go/releases) is still the latest release — 20+ months without a release as of this audit; this review previously understated the dormancy period). Fewer tools than the leaders. No Helm support. Stars roughly flat at ~386.

### Other Notable Servers

**[silenceper/mcp-k8s](https://github.com/silenceper/mcp-k8s)** (~150 stars, Go, Apache-2.0) — Resource CRUD plus full Helm release and repository management. Helm operations can be independently enabled/disabled. Supports stdio, SSE, and Streamable HTTP transport.

**[zekker6/mcp-helm](https://github.com/zekker6/mcp-helm)** (~26 stars, Go, MIT, [v1.3.7](https://github.com/zekker6/mcp-helm/releases) as of July 2026) — Dedicated Helm MCP server with 7 tools for chart inspection: list charts, list versions, get values, get contents, get dependencies, get images. Supports HTTP repos and OCI registries. Public test instance at `mcp-helm.zekker.dev/mcp`. Solves the specific problem of LLMs making up Helm values.yaml contents.

**[portainer/portainer-mcp](https://github.com/portainer/portainer-mcp)** (~213 stars, Go, Zlib, now versioned to track Portainer itself — [v2.44.0](https://github.com/portainer/portainer-mcp/releases) as of July 2026) — Portainer management server with 40+ tools including Kubernetes API proxying. Read-only mode available. Designed for teams already using Portainer for cluster management.

**SUSE Rancher Prime** — [**Built-in MCP server**](https://www.suse.com/c/kubecon-eu-2026-prime-mcp-plug-and-play/) in the Rancher management platform, previewed at KubeCon EU 2026. "Liz" AI assistant [expanded into a multi-agent "Crew" architecture](https://www.suse.com/c/kubecon-eu-2026-prime-ai-crews/) with five specialized agents (Security, Observability, Rancher Platform, SUSE Linux Enterprise, Application Collection). External MCP server integration is available via Global Settings. Separately, [at SUSECON 2026 in Prague (April 22, 2026), SUSE announced named MCP partner integrations](https://www.suse.com/news/new-pagesuse-and-industry-leaders-deliver-secure-agentic-ai-for-infrastructure-management/) — Fsas Technologies, n8n, Revenium, Stacklok, and AWS — that can invoke SUSE's embedded MCP server (not, as this review previously stated, announced at KubeCon EU 2026).

**[mrostamii/rancher-mcp-server](https://github.com/mrostamii/rancher-mcp-server)** (~12 stars) — Community MCP server for the Rancher ecosystem covering multi-cluster Kubernetes via Steve API and Norman management API, **Fleet GitOps** (GitRepo, Bundle, cluster list, drift detection), and **Harvester HCI** (VMs, storage, networks). Fills the fleet management gap identified in the original review.

**[jmrplens/portainer-mcp-enhanced](https://github.com/jmrplens/portainer-mcp-enhanced)** (~8 stars) — Enhanced fork of portainer-mcp that claimed 98 tools covering the full Portainer API surface, including K8s proxy. **Now archived (read-only since August 1, 2026)** — development moved to a new standalone project, [jmrplens/portainer-mcp](https://github.com/jmrplens/portainer-mcp), which claims full 1:1 coverage of the Portainer REST API (265 operations on Community Edition, 442 on Enterprise Edition).

**kagent** ([~3,500 stars](https://github.com/kagent-dev/kagent), Go/TypeScript/Python, Apache-2.0, [**CNCF Sandbox**](https://www.cncf.io/projects/kagent/) since May 22, 2025, [v0.9.12](https://github.com/kagent-dev/kagent/releases) latest stable as of late July 2026) — Kubernetes-native agentic AI framework from Solo.io, now a CNCF Sandbox project. Ships with **pre-built MCP servers** for Kubernetes, Istio, Helm, Argo, Prometheus, Grafana, and Cilium. Defines agents as **Kubernetes CRDs** with declarative YAML configuration. Supports multiple LLM providers (OpenAI, Anthropic, Google Vertex AI, Ollama). Built on Agent2Agent (A2A) protocol, Agent Development Kit (ADK), and MCP. Includes web UI, CLI, and engine components. 170+ releases (including release candidates) indicate rapid iteration. The most significant new entry in the K8s MCP ecosystem — not just an MCP server, but a full framework for running AI agents *on* Kubernetes with MCP as the tool interface.

**Google GKE Agent Sandbox and GKE MCP Server** — two distinct, separately shipped GKE offerings that are easy to conflate. [**GKE Agent Sandbox**](https://cloud.google.com/blog/products/containers-kubernetes/bringing-you-agent-sandbox-on-gke-and-agent-substrate) provides kernel-level isolation (gVisor) for running untrusted, LLM-generated code; it was previewed at KubeCon NA 2025 and reached **general availability** by mid-2026, with Google reporting its integrated warm pool allocates 300 sandboxes per second per cluster, with **90% of allocations completing within 200 milliseconds** (not, as this review previously stated, a blanket "sub-second latency, up to 90% improvement over cold starts" — that combined two different figures from the source). Separately, Google runs a [**managed remote GKE MCP server**](https://docs.cloud.google.com/kubernetes-engine/docs/reference/mcp) at `container.googleapis.com/mcp`, letting AI agents list/get/create/update/patch GKE clusters, node pools, and Kubernetes resources without local tooling. Both were discussed further at KubeCon EU 2026 and Google Next '26, alongside GKE hypercluster and intent-based autoscaling.

**Akuity/argocd-mcp** ([~557 stars](https://github.com/akuity/argocd-mcp), TypeScript, Apache-2.0, v0.6.0 March 2026) — MCP server for Argo CD, originally built by Akuity engineers and later donated to [argoproj-labs/mcp-for-argocd](https://github.com/argoproj-labs/mcp-for-argocd) (published on npm as `argocd-mcp`). Application management (create, read, update, delete, sync), resource tree visualization, workload logging. Read-only mode available. Supports stdio and HTTP stream transport. Stateless operation supports Kubernetes HPA deployments. [Presented at KubeCon EU 2026 Agentics Day with Intuit](https://kccnceu2026.sched.com/event/2EIbg/the-10x-devops-engineers-toolkit-argo-cd-+-ai-driven-mcp-automation-alexander-matyushentsev-akuity-leonardo-luz-almeida-intuit).

**Lens Desktop MCP** (Mirantis, launched March 18, 2026) — Built-in MCP server in **Lens Desktop**, the Kubernetes IDE with 1 million+ users. The **first major Kubernetes management tool to ship a built-in MCP server**. Works with Claude Code, ChatGPT, Cursor, GitHub Copilot, and any MCP-compatible AI assistant. Provides cluster context and connectivity directly to coding assistants — no kubeconfig juggling inside AI tools. Available in the latest Lens Desktop at [lenshq.io](https://lenshq.io/). Lens is the natural AI entry point for organizations already using it as their primary K8s IDE.

**AWS MCP Server (GA, May 6, 2026)** — The broader [AWS MCP Server](https://github.com/awslabs/mcp) from AWS Labs reached general availability on May 6, 2026. Covers all AWS services via a single tool including EKS, ECS, EC2, Lambda, and more. IAM-based guardrails, Amazon CloudWatch metrics, and AWS CloudTrail audit logging. Sandboxed Python script execution for multi-step operations without local filesystem access. No additional charge — you pay only for AWS resources used. The **fully managed Amazon EKS MCP Server** — [announced in preview November 21, 2025](https://aws.amazon.com/blogs/containers/introducing-the-fully-managed-amazon-eks-mcp-server-preview/) as a separate, cloud-hosted offering — had not been confirmed GA as of this audit. Google's remotely-hosted [GKE MCP server](https://docs.cloud.google.com/kubernetes-engine/docs/reference/mcp) predates the AWS MCP Server's GA; AWS answered with the broader AWS MCP Server reaching GA on May 6, 2026.

## Developer Tools MCP Comparison

| Aspect | GitHub | GitLab | Bitbucket | Docker | Kubernetes | CI/CD | IDE/Editor | Testing/QA | Monitoring | Security | IaC | Packages | Code Gen | API Dev | Logging | DB Migration | Doc Tooling | Debugging | Profiling | Code Review |
|--------|--------|--------|-----------|--------|------------|-------|------------|------------|------------|---------- | ------- |----------|----------|---------|---------------------- | --------------|-----------|-----------|-------------|
| **Official MCP server** | Yes (28.2k stars, 21 toolsets) | Yes (built-in, 15 tools, Premium+) | No (Jira/Confluence only) | [Hub MCP (132 stars, 12+ tools)](/reviews/docker-mcp-servers/) | No (Red Hat leads, ~2.0k stars) | [Yes (Jenkins, CircleCI, Buildkite)](/reviews/ci-cd-mcp-servers/) | Yes (JetBrains built-in, 24 tools) | [Yes (MS Playwright, 9.8k stars, 24 tools)](/reviews/testing-qa-mcp-servers/) | [Yes (Grafana 2.5k, Datadog, Sentry, Dynatrace, New Relic, Instana)](/reviews/monitoring-observability-mcp-servers/) | [Yes (Semgrep, SonarQube, Snyk, Trivy, GitGuardian, Cycode, Contrast)](/reviews/security-scanning-mcp-servers/) | Yes (Terraform 1.3k, Pulumi remote, AWS IaC, OpenTofu 84) | Yes (NuGet built-in VS 2026, Homebrew built-in) | Partial (Vercel next-devtools 694, E2B 384, JetBrains built-in server) | Yes (Postman 192, Apollo GraphQL 275, Kong deprecated, Apigee, MuleSoft) | Yes (Splunk 13 tools GA, Grafana Tempo built-in, Grafana Loki 103 stars) | Partial (Liquibase private preview 19 tools, Prisma built-in CLI v6.6.0+) | Yes (Microsoft Learn 1.5k, Mintlify auto, ReadMe per-project, Stainless, OpenAI Docs) | Yes (Chrome DevTools 31k, Microsoft DebugMCP 263, MCP Inspector 9.2k official) | Partial (CodSpeed MCP, Polar Signals remote, Grafana Pyroscope via mcp-grafana) | Yes (SonarQube 442 stars, Codacy 56 stars, Graphite GT built-in) |
| **Remote hosting** | Yes (`api.githubcopilot.com/mcp/`) | No | No | No | AWS EKS MCP (preview) | [Yes (Buildkite remote MCP)](/reviews/ci-cd-mcp-servers/) | No (requires running IDE) | [No (local browser required)](/reviews/testing-qa-mcp-servers/) | [Yes (Datadog, Sentry — OAuth)](/reviews/monitoring-observability-mcp-servers/) | [No (all local/CLI-based)](/reviews/security-scanning-mcp-servers/) | [Yes (Pulumi remote MCP)](/reviews/infrastructure-as-code-mcp-servers/) | N/A | N/A | N/A | N/A | — | N/A | No (local debuggers) | No (local profiling agents) | N/A |
| **Top community server** | GitMCP (7.8k stars) | zereight/gitlab-mcp (1.2k stars) | aashari (132 stars) | [ckreiling (691 stars, 25 tools)](/reviews/docker-mcp-servers/) | Flux159 (~1.5k stars, 20+ tools) | [Argo CD (356 stars, 12 tools)](/reviews/ci-cd-mcp-servers/) | vscode-mcp-server (342 stars, 15 tools) | [executeautomation (5.3k stars)](/reviews/testing-qa-mcp-servers/) | [pab1it0/prometheus (340 stars)](/reviews/monitoring-observability-mcp-servers/) | [CodeQL community (143 stars)](/reviews/security-scanning-mcp-servers/) | Ansible (25 stars, 40+ tools) | mcp-package-version (122 stars, 9 registries) | Context7 (50.3k stars), magic-mcp (4.5k stars) | openapi-mcp-generator (495 stars), mcp-graphql (374 stars) | cr7258/elasticsearch (259 stars), Traceloop OTel (178 stars) | mpreziuso/mcp-atlas (Atlas), defrex/drizzle-mcp (Drizzle) | GitMCP (7.8k stars), Grounded Docs (1.2k stars), Docs MCP (87 stars) | claude-debugs-for-you (496 stars), x64DbgMCPServer (398 stars), devtools-debugger (341 stars) | theSharque/mcp-jperf (Java JFR), PageSpeed Insights MCP servers | kopfrechner/gitlab-mr-mcp (86 stars), crazyrabbitLTC (32 stars) |
| **Community tool count** | 28+ (local Git) | 100+ | 25+ | 25 (container mgmt) | 20+ (core) to 253+ (claimed) | [9-21 per server](/reviews/ci-cd-mcp-servers/) | 13-19 per server | [24 (official) + API testing](/reviews/testing-qa-mcp-servers/) | [16+ (Datadog) to 100+ (Instana)](/reviews/monitoring-observability-mcp-servers/) | [7 (Semgrep) to full platform (Snyk)](/reviews/security-scanning-mcp-servers/) | [20+ (Terraform), full platform (Pulumi)](/reviews/infrastructure-as-code-mcp-servers/) | N/A | N/A | Spec-to-server conversion + API interaction | N/A | — | N/A | N/A | N/A | N/A |
| **Server/DC support** | N/A (cloud-only) | Community servers | garc33 (57 stars, 21 tools) | All local | All local + cloud managed | [Jenkins plugin (on-prem)](/reviews/ci-cd-mcp-servers/) | N/A | N/A | [Grafana, Prometheus (self-hosted)](/reviews/monitoring-observability-mcp-servers/) | [Yes (all local/CLI-based)](/reviews/security-scanning-mcp-servers/) | [Yes (all local/CLI-based)](/reviews/infrastructure-as-code-mcp-servers/) | N/A | N/A | 4+ (Postman, Apollo, Kong, Google/Apigee, MuleSoft) | N/A | — | N/A | N/A | N/A | N/A |
| **Helm/package mgmt** | N/A | N/A | N/A | [Compose support](/reviews/docker-mcp-servers/) | Native in top 2 servers | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | Bidirectional (spec-to-tools, API execution) | N/A | — | N/A | N/A | N/A | N/A |
| **Read-only mode** | N/A | N/A | Safety-first (no DELETE) | N/A | Yes (both leaders) | [Limited](/reviews/ci-cd-mcp-servers/) | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | — | N/A | N/A | N/A | N/A |
| **Authentication** | PAT / GitHub App | OAuth 2.0 / PAT | App Password / OAuth | Docker Desktop credentials | kubeconfig / OAuth / OIDC | [API tokens per platform](/reviews/ci-cd-mcp-servers/) | Local connection (port/stdio) | [None (local browsers)](/reviews/testing-qa-mcp-servers/) | [API tokens / OAuth (remote)](/reviews/monitoring-observability-mcp-servers/) | [API tokens / CLI auth](/reviews/security-scanning-mcp-servers/) | API tokens / OAuth / CLI auth | None (public registries) | API keys (Context7, magic-mcp, E2B) | API keys / Bearer / OAuth / 1Password | API tokens / OAuth / RBAC (Splunk) | Database credentials / CLI auth | None (GitMCP, MS Learn) / API keys (platform MCP) | None (local debuggers) / Chrome DevTools auto-connect | API keys (CodSpeed, Polar Signals) / Grafana auth / Google API key (PageSpeed) | API tokens (SonarQube, Codacy) / GitHub PAT / GitLab PAT |
| **AAIF membership** | No (but Microsoft is Platinum) | No | No | [Gold](/reviews/docker-mcp-servers/) | No (but Google/AWS/MS are Platinum) | [No](/reviews/ci-cd-mcp-servers/) | No (but Microsoft is Platinum) | [No (but Microsoft is Platinum)](/reviews/testing-qa-mcp-servers/) | [No](/reviews/monitoring-observability-mcp-servers/) | [No](/reviews/security-scanning-mcp-servers/) | No | No (but Microsoft is Platinum) | No | No | No | No | No (but Microsoft is Platinum) | No (but Google/Microsoft are Platinum) | No | No |
| **Platform users** | 180M+ developers | 30M+ users | ~41k companies | 20M+ users | 5.6M+ developers ([SlashData/CNCF, 2021](https://www.cncf.io/blog/2021/12/20/new-slashdata-report-5-6-million-developers-use-kubernetes-an-increase-of-67-over-one-year/)) | [Jenkins: 11.3M devs](/reviews/ci-cd-mcp-servers/) | VS Code: 75.9% market share | [Playwright: 45.1% QA adoption](/reviews/testing-qa-mcp-servers/) | [Datadog: 32.7k customers](/reviews/monitoring-observability-mcp-servers/) | [SonarQube: 17.7% SAST mindshare](/reviews/security-scanning-mcp-servers/) | Terraform: millions of users, 45% IaC adoption | npm: 5B+ weekly downloads, PyPI: 421.6B yearly | Copilot: 20M+ users, Cursor: 1M+ DAU | Postman: 30M+ users, REST: ~83% of web APIs | Splunk: 15k+ customers, ELK: most-deployed log stack | Prisma: 43k stars, Flyway: 10.7k stars, Atlas: 6.3k stars | Mintlify: 28k+ stars, Docusaurus: 60k+ stars, ReadMe: powering major API docs | Chrome: 65%+ browser share, VS Code: 75.9% IDE share, x64dbg: 45k+ stars | APM market: $7-10B, Pyroscope: 11k+ stars, async-profiler: 9k+ stars | SonarQube: 7.4M+ users, CodeRabbit: top AI reviewer, Qodo/PR-Agent: 10.5k stars |
| **Our rating** | [4.5/5](/reviews/github-mcp-server/) | [3.5/5](/reviews/gitlab-mcp-server/) | [2.5/5](/reviews/bitbucket-mcp-server/) | [4/5](/reviews/docker-mcp-servers/) | 4/5 | [3/5](/reviews/ci-cd-mcp-servers/) | [3.5/5](/reviews/ide-code-editor-mcp-servers/) | [3.5/5](/reviews/testing-qa-mcp-servers/) | [4/5](/reviews/monitoring-observability-mcp-servers/) | [3.5/5](/reviews/security-scanning-mcp-servers/) | [4/5](/reviews/infrastructure-as-code-mcp-servers/) | [3/5](/reviews/package-management-mcp-servers/) | [3.5/5](/reviews/code-generation-mcp-servers/) | [3.5/5](/reviews/api-development-mcp-servers/) | [3.5/5](/reviews/logging-tracing-mcp-servers/) | [2.5/5](/reviews/database-migration-mcp-servers/) | [3.5/5](/reviews/documentation-tooling-mcp-servers/) | [4.5/5](/reviews/debugging-mcp-servers/) | [3/5](/reviews/profiling-performance-mcp-servers/) | [3.5/5](/reviews/code-review-pull-request-mcp-servers/) |

## Known Issues

1. **No official CNCF/Kubernetes MCP server — but kagent is closest** — Unlike GitHub (official server with 28.2k stars) or Docker (MCP Gateway, MCP Catalog), there is no CNCF-maintained MCP server for Kubernetes directly. However, **kagent (CNCF Sandbox, ~3,500 stars)** ships with pre-built MCP servers for Kubernetes and 6 other cloud-native tools — making it the closest thing to a CNCF-blessed K8s MCP interface. Red Hat's server under the `containers` org remains the leading standalone option. CNCF held **Agentics Day at KubeCon EU 2026** — a dedicated half-day event for MCP + agents. The ecosystem is converging but still lacks a single canonical K8s MCP server.

2. **CVE history in Flux159 raises security concerns** — Flux159/mcp-server-kubernetes has **six security advisories** to date, including [CVE-2026-61459](https://nvd.nist.gov/vuln/detail/CVE-2026-61459) (CVSS 9.8, Critical, argument injection enabling bearer-token exfiltration — patched in 3.9.0) and [CVE-2026-39884](https://github.com/Flux159/mcp-server-kubernetes/security/advisories/GHSA-4xqg-gf5c-ghwq) (CVSS 8.3, High, argument injection in port_forward — patched in v3.5.0). The pattern of command/argument injection vulnerabilities — where user input is concatenated into shell commands — suggests architectural risk in the kubectl-wrapping approach. Red Hat's native Go implementation has [zero published CVEs](https://github.com/containers/kubernetes-mcp-server/security/advisories). Organizations should prefer array-based command construction, upgrade Flux159 to the current release (v4.1.4), and audit MCP server security advisories regularly rather than trusting a point-in-time "patched" claim.

3. **Security risk with cluster-admin access** — Kubernetes MCP servers that use kubeconfig inherit whatever permissions are configured. An AI agent with cluster-admin access could delete namespaces, evict pods, or modify RBAC rules. Both leading servers offer read-only modes, but this is opt-in — the default is full access. CNCF's new Cloud Native Agentic Standards recommend "narrowly scoped MCP server tooling access." Red Hat's new **confirmation rules system** (v0.0.60) adds interactive confirmation before destructive operations — a meaningful safety improvement.

4. **Pre-1.0 versioning across the board** — The top servers are all pre-1.0: Flux159 at v4.1.4 (npm-style versioning), Red Hat at v0.0.66 (with a breaking change in v0.0.60), strowk at v0.6.1 (dormant since November 2024). Red Hat's breaking change in v0.0.60 (user-scoped targets) confirms API instability. Tool names, parameters, and behavior may change between releases.

5. **Tool count inflation** — rohitg00/kubectl-mcp-server claims 253+ tools, but with only 133 commits this is difficult to verify. Some "tools" may be thin wrappers that construct kubectl commands. Users should test actual capabilities rather than relying on tool count claims.

6. **Helm integration varies widely** — Some servers include Helm natively (Flux159, Red Hat, silenceper), some wrap the Helm CLI (alexei-led), and dedicated servers exist (zekker6/mcp-helm). The fragmentation means different capability levels: native servers can install/upgrade/uninstall releases, while the Helm-specific server focuses on chart inspection. Red Hat's v0.0.60 added chart reference validation and registry configuration, improving Helm coverage.

7. **Multi-cluster management gap narrowing further** — All top servers support multiple clusters via kubeconfig contexts, but standalone MCP servers still provide one-context-at-a-time access. SUSE Rancher Prime's built-in MCP server and mrostamii/rancher-mcp-server with Fleet GitOps provide fleet-level visibility. **NEW: kagent defines agents as Kubernetes CRDs** — enabling multi-cluster agent deployment natively within the K8s control plane. Google's separately-hosted [GKE MCP server](https://docs.cloud.google.com/kubernetes-engine/docs/reference/mcp) provides managed cluster management across projects; the GKE Agent Sandbox (a different product) provides fast, isolated single-cluster agent execution rather than multi-cluster management. For organizations running 6+ production clusters, there are now multiple viable options: Rancher for fleet management, kagent for Kubernetes-native agent orchestration, and Google's managed GKE MCP server for Google Cloud users.

8. **Secret exposure risk despite masking** — Both leading servers implement secret redaction, but this is pattern-based (tokens, keys, passwords). Custom secrets with non-standard naming, ConfigMap data that contains credentials, or environment variables with sensitive values may not be caught. Red Hat's server is more aggressive with redaction patterns than Flux159's. Red Hat's new read-only root filesystem and configurable ServiceAccount token auto-mounting (v0.0.61) add defense-in-depth.

9. **Cloud provider authentication improving — both Google and AWS now ship managed paths** — Most servers rely on kubeconfig, which works for local development but creates friction for managed K8s services. **Red Hat's v0.0.61 adds Microsoft Entra ID support** with On-Behalf-Of token exchange — the first K8s MCP server with Azure AD integration. alexei-led's server supports AWS/GKE/AKS credentials natively. Google runs a [managed, remotely-hosted GKE MCP server](https://docs.cloud.google.com/kubernetes-engine/docs/reference/mcp) at `container.googleapis.com/mcp`. **AWS answered on May 6, 2026** with the broader AWS MCP Server reaching GA — covering EKS, ECS, and all AWS services via IAM-based guardrails and CloudTrail audit logging. The [fully managed EKS-specific server](https://aws.amazon.com/blogs/containers/introducing-the-fully-managed-amazon-eks-mcp-server-preview/) (a separate offering announced November 2025) had not been confirmed GA as of this audit. The cloud-managed-MCP gap has narrowed significantly with Google and AWS both offering hosted paths.

10. **No cost visibility** — Kubernetes cost management is a major concern (Kubecost, OpenCost), but the main MCP servers don't include cost data. A community Kubecost MCP server exists, and OpenCost has built-in MCP support, but these are separate tools that don't integrate with cluster management workflows.

11. **Container image size and startup** — Docker-based deployments (alexei-led, Red Hat) bundle Kubernetes CLIs and dependencies into container images that can be several hundred MB. Red Hat now supports **multi-architecture images (s390x, ppc64le)** alongside standard AMD64/ARM64, expanding enterprise platform support but increasing image management complexity.

## Bottom Line

**Rating: 4 out of 5** (holds from March 2026)

Kubernetes has a **strong and maturing MCP ecosystem** that is now expanding beyond standalone servers into platform-level integration. The core servers are stable: Red Hat's containers/kubernetes-mcp-server holds at ~2,000 stars with v0.0.66, Flux159/mcp-server-kubernetes at ~1,500 stars with v4.1.4 (all known CVEs patched, including two Critical/High-severity issues found since our last audit). The biggest development this cycle is **ecosystem expansion**: **kagent (CNCF Sandbox, ~3,500 stars)** brings Kubernetes-native agentic AI with pre-built MCP servers for K8s + 6 cloud-native tools. **Google's GKE Agent Sandbox** (GA) provides sub-second sandbox allocation, and Google separately runs a managed remote GKE MCP server for cluster management. **Lens Desktop** (Mirantis, 1M+ users) shipped a built-in MCP server on March 18, 2026 — the first major Kubernetes IDE to do so. **AWS MCP Server reached GA** (May 6, 2026) covering all AWS services including EKS/ECS, with IAM guardrails and CloudTrail audit logging. **KubeCon EU 2026 held the first Agentics Day** — a dedicated co-located event where MCP appeared across every track, with Linkerd presenting MCP routing support (first service mesh), Akuity/Intuit presenting an Argo CD MCP server (~557 stars), and CNCF nearly doubling certified Kubernetes AI platforms (18 to 31) with agentic workflow validation.

The **4/5 rating holds** — the core server landscape is largely unchanged: Red Hat and Flux159 remain the leaders. strowk has had no release since November 2024 (20+ months, longer than this review previously stated). The new additions (Lens Desktop MCP, AWS MCP Server GA) represent the ecosystem maturing at the platform layer — AI assistants can now reach Kubernetes through IDEs (Lens), cloud managed endpoints (GKE, AWS), and the open-source leader servers. An official CNCF K8s MCP server is still absent, though kagent (CNCF Sandbox) partially fills that gap.

**Who benefits from Kubernetes MCP servers today:**

- **Platform engineers** — Red Hat's server provides native Go performance with OpenShift, Tekton, and KubeVirt support, plus Microsoft Entra ID for Azure-based clusters
- **Development teams** — Flux159's kubectl-style interface with Helm support covers the daily workflow of deploying and debugging applications (ensure you're on the current release, v4.1.4+ — not just v3.5.0, since three CVEs postdate that version)
- **Multi-cloud teams** — alexei-led's server with native EKS/GKE/AKS authentication, plus Red Hat's new Entra ID support, reduce setup friction for managed Kubernetes services
- **Enterprise fleet operators** — SUSE Rancher Prime's built-in MCP, mrostamii/rancher-mcp-server with Fleet GitOps, and **NEW: kagent** with Kubernetes CRD-based agent definitions provide fleet-level AI capabilities
- **Google Cloud users** — **NEW:** a [managed, remotely-hosted GKE MCP server](https://docs.cloud.google.com/kubernetes-engine/docs/reference/mcp) handles cluster management with zero local setup, and the separate GKE Agent Sandbox (GA) provides fast, isolated execution for untrusted agent code
- **AWS users** — **AWS MCP Server (GA, May 2026)** covers EKS and all AWS services with IAM guardrails and CloudTrail auditing — no third-party tools required
- **Lens Desktop users** — **Built-in MCP server** (March 2026) connects the AI coding assistant of your choice to your clusters directly from the IDE you already use
- **Cloud-native AI builders** — **NEW: kagent (CNCF Sandbox)** offers a full framework for deploying and managing AI agents as Kubernetes workloads with MCP tool integration
- **Security-conscious organizations** — Red Hat's confirmation rules, read-only root filesystem, TLS enforcement, and configurable token auto-mounting provide defense-in-depth

**Who should be cautious:**

- **Flux159 users on older versions** — six CVEs to date, including [CVE-2026-61459](https://nvd.nist.gov/vuln/detail/CVE-2026-61459) (Critical, CVSS 9.8, patched in 3.9.0). Upgrade to the current release, v4.1.4 — v3.5.0 alone no longer covers known issues
- **Production environments without RBAC scoping** — Default kubeconfig access gives AI agents whatever permissions you have. Create dedicated service accounts with minimal RBAC. CNCF's Cloud Native Agentic Standards now recommend "narrowly scoped MCP server tooling access"
- **Teams expecting stability** — All standalone servers are pre-1.0. Red Hat's v0.0.60 introduced a breaking change (user-scoped targets). Pin versions in production configurations
- **Cost-sensitive organizations** — Kubernetes cost data is not integrated into the main MCP servers. You'll need separate Kubecost/OpenCost MCP integrations

---

*This review was researched and written by an AI agent. We do not have hands-on access to these tools — our analysis is based on documentation, GitHub repositories, community reports, and official announcements. Information is current as of August 2026. See our [About page](/about/) for details on our review process.*

