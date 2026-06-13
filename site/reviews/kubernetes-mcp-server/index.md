# The Kubernetes MCP Server — Native API Access Without the kubectl Tax

> Red Hat's containers/kubernetes-mcp-server gives AI agents direct Kubernetes API access — no kubectl wrapper, no external dependencies.


Most Kubernetes MCP servers shell out to kubectl. This one doesn't.

**At a glance:** 1,600+ GitHub stars, 340 forks, v0.0.62 (May 5, 2026), 62 releases, 15+ tools across 7 modular toolsets, Go, Apache-2.0, ~6,100 weekly npm downloads, PulseMCP ~9,800 weekly visitors. Part of our **[Cloud & Infrastructure MCP category](/categories/cloud-infrastructure/)**.

The [Kubernetes MCP server](https://github.com/containers/kubernetes-mcp-server) from the `containers` organization (backed by Red Hat engineers) is a Go-native implementation that talks directly to the Kubernetes API server. No kubectl binary. No Helm CLI. No external dependencies at all — just a single binary that reads your kubeconfig and gives AI agents real cluster access.

With 1,600+ stars, 340 forks, and 62 releases, it's the most mature of the six-plus Kubernetes MCP implementations floating around GitHub. And it does something most of them don't: it treats safety as a first-class feature, not an afterthought.

## What's New (April–May 2026 Update)

**v0.1.0 milestone is 99% complete.** The project's milestone tracker shows 849 of 853 items closed — the four remaining are a documentation issue, a code evaluation issue, and two open PRs. After 62 releases under v0.0.x, a stable API release appears imminent. This will directly address the longest-standing criticism of the server.

**v0.0.62 shipped (May 5, 2026) — MCP resource capability and startup auth validation.** The server now exposes Kubernetes resources as MCP resources (not just tools), enabling clients that consume the MCP resource protocol. A breaking change: kubeconfig auth mode with `require_oauth` is now rejected at startup rather than caught at runtime — startup validation is strictly safer. Certificate authority propagation to token exchange HTTP clients was fixed. OIDC fallback to `openid-configuration` when well-known endpoint returns empty was added. `modelcontextprotocol/go-sdk` bumped 1.5→1.6, Tekton pipeline 1.11→1.12, `fsnotify` 1.9→1.10.1.

**v0.0.61 shipped (Apr 24, 2026) — Tekton toolset, Microsoft Entra ID auth, rate limiting.** A new seventh toolset — **Tekton** — adds pipeline and task management for CI/CD workflows on Kubernetes. **Microsoft Entra ID On-Behalf-Of (OBO) token exchange** enables enterprise SSO, making the server viable for corporate environments requiring federated identity. Per-session **rate limiting** via MCP middleware is configurable. Multi-arch builds extended to s390x and ppc64le. Gateway API HTTPRoute support added to the Helm chart. The Helm chart's root filesystem is now read-only; ServiceAccount token auto-mount is configurable. Bug fixes: KEP-2227 default container resolution for multi-container pods, SIGHUP config reload, authorization header passthrough, and kubeconfig empty `current-context` handling.

**MCPSafe AIVSS score: 84/100, Grade B (May 12, 2026).** Issue [#1148](https://github.com/containers/kubernetes-mcp-server/issues/1148) reports the server scored 84/100 — 34 medium findings (all around container and Kubernetes resource access scoping), zero critical or high. The project is actively working on formalizing its security posture with a SECURITY.md policy (#1132) and a private disclosure route (#1126).

**npm downloads up 36%.** Weekly npm downloads jumped from ~4,500 to ~6,110 — continued organic growth in the post-Q1 MCP adoption wave.

**Milestone summary for four closed issues:**
- **#1057** (config validation) — closed; fixed in v0.0.62's startup auth validation.
- **#838** (KubeVirt eval failures) — closed April 21, followed by the new QEMU guest agent tool (#811) merged May 14.
- **#370** (Job/CronJob support) — closed as not_planned. Use generic `resources_create_or_update` for Jobs.
- **#269** (Helm values.yaml retrieval) — closed as not_planned.

**v0.0.60 (Apr 1, 2026) — TLS enforcement, Helm chart validation, confirmation rules.** The `require_tls` config option enforces HTTPS connections. Helm chart validation includes allowed registry configuration, preventing agents from installing charts from untrusted sources. A **confirmation rules system** extends elicitation with configurable policies for when human approval is required. Bugs fixed: unbounded memory consumption in Kiali response handling, panic from non-boolean type assertions in tool handlers, concurrent map access issues.

**v0.0.59 (Mar 18, 2026) — elicitation and MCP Registry support.** URL-mode elicitation for human-in-the-loop confirmation before destructive actions. Container images published to ghcr.io for MCP Registry compatibility. Helm toolset removed from defaults.

## What It Does

The server organizes its capabilities into **modular toolsets** that you enable or disable:

**Core** (default enabled):

| Tool | What it does |
|------|-------------|
| `pods_list` | List pods across namespaces with field/label selectors |
| `pods_get` | Get a specific pod by name and namespace |
| `pods_delete` | Delete a pod |
| `pods_log` | Stream pod logs with filtering |
| `pods_exec` | Execute commands inside running containers |
| `pods_run` | Run a container image as a pod |
| `resources_list` | List any Kubernetes resource type |
| `resources_get` | Get any resource by kind/name/namespace |
| `resources_create_or_update` | Create or update any resource via YAML |
| `resources_delete` | Delete any resource |
| `events_list` | List cluster events for troubleshooting |
| `namespaces_list` | List namespaces (and OpenShift projects) |
| `nodes_list` | List nodes with status and capacity |
| `nodes_logs` | Retrieve kubelet logs from nodes |
| `top` | Resource metrics (CPU/memory) via Metrics Server |

**Config** (default enabled):

| Tool | What it does |
|------|-------------|
| `configuration_view` | View current kubeconfig and contexts |
| `configuration_use_context` | Switch between cluster contexts |
| `targets_list` | List available cluster targets |

**Helm:**

| Tool | What it does |
|------|-------------|
| `helm_install` | Install a Helm chart in a namespace |
| `helm_list` | List installed Helm releases |
| `helm_uninstall` | Uninstall a Helm release |

**KubeVirt:**

| Tool | What it does |
|------|-------------|
| VM management tools | Create, list, start, stop virtual machines on Kubernetes |

**Kiali:**

| Tool | What it does |
|------|-------------|
| Service mesh tools | Istio service mesh observability via Kiali |

**KCP:**

| Tool | What it does |
|------|-------------|
| Workspace tools | Multi-tenant workspace management via kcp |

**Tekton** (new in v0.0.61):

| Tool | What it does |
|------|-------------|
| Pipeline tools | Manage Tekton CI/CD pipelines and tasks on Kubernetes |

The toolset architecture is genuinely useful. A developer debugging pods needs `core` and `config`. A platform engineer managing Helm deployments enables `helm`. Nobody needs KubeVirt tools unless they're running virtual machines on Kubernetes. You configure exactly what you need:

```bash
kubernetes-mcp-server --toolsets core,config,helm
```

## Setup

Multiple installation paths, all straightforward:

**npx (simplest):**
```json
{
  "mcpServers": {
    "kubernetes": {
      "command": "npx",
      "args": ["-y", "kubernetes-mcp-server@latest"]
    }
  }
}
```

**Native binary (best performance):**

Download from [GitHub Releases](https://github.com/containers/kubernetes-mcp-server/releases) for Linux, macOS, or Windows. Single binary, no runtime dependencies.

**Docker:**
```json
{
  "mcpServers": {
    "kubernetes": {
      "command": "docker",
      "args": ["run", "-i", "--rm",
               "-v", "${HOME}/.kube:/home/user/.kube:ro",
               "ghcr.io/containers/kubernetes-mcp-server"]
    }
  }
}
```

**Python (uvx/pip):**
```bash
uvx kubernetes-mcp-server
```

For HTTP/SSE mode (team deployments):
```bash
kubernetes-mcp-server --port 8080
```

**Setup difficulty: Easy** — if you already have a kubeconfig. No API keys, no cloud accounts, no registration. The server reads your existing `~/.kube/config` and connects to whatever clusters are configured there. The hardest part is having a Kubernetes cluster to connect to in the first place.

## What Works Well

**Direct API access, not kubectl wrapping.** This is the key differentiator. While Flux159's `mcp-server-kubernetes` shells out to kubectl and rohitg00's `kubectl-mcp-server` does the same, Red Hat's implementation uses Go's `client-go` library to talk directly to the Kubernetes API server. No process spawning per operation. No parsing kubectl text output. No dependency on kubectl being installed. The performance difference is real — direct API calls are faster and more reliable than shelling out.

**Read-only and non-destructive modes.** The `--read-only` flag prevents all write operations. The `--disable-destructive` flag (independent from read-only) blocks deletes and updates while still allowing creates. This is exactly what you need when connecting an AI agent to a production cluster. "Help me debug this pod" should not require giving the agent permission to delete it. No other Kubernetes MCP server offers this level of granular safety control.

**Multi-cluster support.** The server can access multiple clusters simultaneously via your kubeconfig. Tools accept a `context` parameter to specify which cluster to operate on. Platform engineers managing dev, staging, and production clusters can use a single MCP server instance for all of them.

**Generic resource operations.** Instead of having separate tools for each Kubernetes resource type (a Deployments tool, a Services tool, a ConfigMaps tool...), the server uses generic `resources_list`, `resources_get`, `resources_create_or_update`, and `resources_delete` tools that work with any resource kind — including Custom Resource Definitions. This means it works with Istio VirtualServices, ArgoCD Applications, Tekton Pipelines, or any other CRD without needing explicit support.

**Pod exec.** The `pods_exec` tool lets agents run commands inside running containers — critical for debugging. "Show me the nginx config" or "check the connection to the database" becomes possible. This is the capability that Docker MCP server users have been requesting since issue #22.

**Automatic sensitive data redaction.** The server redacts tokens, credentials, and passwords from tool output. When an agent lists Secrets or reads a ServiceAccount token, sensitive values are masked. This is important given that [AWS's EKS MCP server exposes Kubernetes secrets in plain text](https://github.com/awslabs/mcp/issues/2588).

**Comprehensive distribution.** Single binary, npm, pip, Docker image, one-click VS Code and Cursor installation. Whatever your workflow, there's an installation path that fits.

**Elicitation for human oversight.** New in v0.0.59: the server supports MCP's elicitation protocol, which can prompt a human for confirmation before executing destructive operations. Instead of trusting that an AI agent knows what it's doing when it calls `resources_delete`, the server can require explicit human approval. This is the kind of safety mechanism that should be standard — and this is one of the first Kubernetes MCP servers to implement it.

**Pre-execution validation.** New in v0.0.58: tools now validate inputs before sending requests to the Kubernetes API. This catches malformed resource names, invalid namespaces, and other errors early — rather than letting them hit the API server and returning cryptic error messages. Combined with elicitation, this creates a two-layer safety net.

**TOML configuration with drop-in support.** Beyond command-line flags, the server supports TOML config files with a drop-in directory for composable configuration. Dynamic reload via SIGHUP means you can change settings without restarting. This is the kind of operational maturity you expect from Red Hat-backed infrastructure.

**OpenTelemetry integration.** Optional distributed tracing with configurable sampling. When you're running an MCP server as shared infrastructure, observability matters. The `/stats` endpoint and structured logging add to the operational picture.

## What Doesn't Work Well

**MCPSafe AIVSS grade B (84/100).** A May 2026 security scan ([#1148](https://github.com/containers/kubernetes-mcp-server/issues/1148)) found 34 medium-severity findings — all centered on container and Kubernetes resource access scoping and prompt injection risks — with zero critical or high findings. The project's prior community audit (issue #762, March 2026) closed with a risk score of 20/100 (safe). Two separate signal sets, both reassuring for a server managing production clusters. The project is formalizing a SECURITY.md policy (#1132) and a private disclosure route (#1126).

**No Ingress, Service, or networking management tools.** While you can manage Services and Ingresses via the generic `resources_create_or_update` tool, there are no purpose-built networking tools. For a server that has dedicated tools for pods, events, nodes, namespaces, and now Tekton pipelines, the absence of dedicated networking tools remains a gap.

**37 open issues (up from 31).** Issue count increased slightly from the April 17 tally as new feature requests and security policy work came in. Still open: requests for kubeconfig write tools ([#1008](https://github.com/containers/kubernetes-mcp-server/issues/1008)) and a `count` parameter for object retrieval ([#967](https://github.com/containers/kubernetes-mcp-server/issues/967)) to reduce context usage.

**Still v0.0.x — but v0.1.0 is imminent.** The v0.1.0 milestone is 99% complete (849 of 853 items closed). Breaking changes across releases — the v0.0.58 metrics rename (`mcp_` → `k8s_mcp_`), v0.0.60's `GetTargets` signature change, v0.0.62's startup rejection of `require_oauth` — are exactly what v0.0.x versioning warns about. Pin your version carefully until v0.1.0 lands and the API stabilizes.

**No granular read-only permissions.** Issue [#568](https://github.com/containers/kubernetes-mcp-server/issues/568) requests fine-grained read-only controls — for example, read-only for Deployments but read-write for ConfigMaps. Currently it's all-or-nothing. The safety modes are good but blunt.

**Job and CronJob toolset not planned.** Issue [#370](https://github.com/containers/kubernetes-mcp-server/issues/370) was closed as not_planned in March 2026. The generic `resources_create_or_update` tool can manage Jobs and CronJobs, but without purpose-built tools the agent experience is less guided. Same applies to StatefulSets and DaemonSets.

**OpenShift in developer preview.** The OpenShift integration — a key selling point for Red Hat's enterprise customers — is still in "developer preview," meaning it's suitable for testing but not production.

## How It Compares

The Kubernetes MCP server ecosystem is fragmented. At least six implementations exist, each with different trade-offs.

**vs. Flux159/mcp-server-kubernetes (~1,394 stars):** TypeScript, kubectl wrapper. containers/kubernetes-mcp-server has now clearly pulled ahead — 1,596 vs. 1,394 stars. Flux159's wraps kubectl/helm commands and requires them installed. Has a `/k8s-diagnose` prompt for guided troubleshooting. Non-destructive mode available. Recently added OpenTelemetry integration and template-based Helm operations. Choose this if you want a simpler, kubectl-familiar approach and don't mind the process-spawning overhead.

**vs. rohitg00/kubectl-mcp-server (~870 stars):** Python/Node.js, kubectl wrapper. Now listed in the CNCF Landscape. Claims 253 tools across modules including GitOps, certificate management, cost optimization, and security auditing. Integrates with 15+ AI assistants. Choose this if you want an everything-and-the-kitchen-sink DevOps agent, but expect a larger attack surface.

**vs. Google GKE MCP Server:** Fully managed remote MCP endpoint from Google (`container.googleapis.com/mcp`). No self-hosting, no binary to install. Currently read-only — cluster inspection, node pool status, logs, operation monitoring. GKE-specific. Production-available. Highlighted at KubeCon EU 2026 (Google Cloud blog post, May 17, 2026) and being used for multi-agent deployment with ADK and Gemini CLI. Choose this if you're on GKE and want zero-setup read-only cluster access. Not comparable for write operations or multi-cloud.

**vs. AWS EKS MCP Server:** Part of the [AWS MCP suite](/reviews/aws-mcp-servers/) (4/5). EKS-specific — only works with AWS-managed Kubernetes. Still in **preview** (the broader AWS MCP Server for general AWS APIs went GA May 6, 2026, but the EKS-specific server remains preview). Deep AWS integration but [exposes K8s secrets in plain text](https://github.com/awslabs/mcp/issues/2588). Integrates with Kiro CLI, Amazon Q Developer, Cursor, Cline. Choose this if you're all-in on AWS and need EKS-specific features like managed node groups.

**vs. strowk/mcp-k8s-go (~370 stars):** Another Go-native implementation. Focuses on MCP resources (exposing cluster state as MCP resources) rather than MCP tools (commands). More of a read-only cluster browser than a management tool. Different philosophy.

**vs. [Docker MCP server](/reviews/docker-mcp-server/) (3.5/5):** Different layer. Docker manages containers on a single machine; Kubernetes MCP manages orchestrated clusters. If you're at the docker-compose stage, you don't need Kubernetes MCP. If you're running production clusters, Docker MCP isn't enough.

## The Bottom Line

Red Hat's Kubernetes MCP server does four things that matter: it talks directly to the Kubernetes API (no kubectl tax), it offers real safety controls (read-only, non-destructive, elicitation, TLS enforcement, secret redaction), it's modular (enable only the seven toolsets you need), and it supports configurable confirmation rules for destructive actions.

Two strong releases since April — v0.0.61 adding a Tekton toolset and Microsoft Entra ID enterprise auth, v0.0.62 adding MCP resource capability — show a project in solid forward motion. npm downloads are up 36% to 6,100/week, stars climbed from 1,400 to 1,596, and the v0.1.0 milestone is 99% complete. The long-standing "still v0.0.x" criticism may soon be resolved.

The MCPSafe B grade (84/100) reflects the inherent risk of broad cluster access — not active vulnerabilities. No CVEs. The prior community audit closed safe. The project is formalizing a security policy, which is the right response.

The generic resource approach remains both strength and limitation: powerful for any CRD, but agents need Kubernetes literacy to construct correct YAML. No dedicated networking tools, no granular per-resource read-only permissions, OpenShift still in preview.

For the core use case — "agent, help me debug this pod" or "what's happening in my cluster?" — it's the best self-hosted option available. Google's GKE MCP is a credible read-only alternative for GKE users who don't want to self-host, but it can't write. AWS's EKS MCP can write but remains in preview and exposes secrets in plain text. Red Hat's multi-cloud, self-hosted approach remains the most flexible option for production use.

**Rating: 4 out of 5** — the most architecturally sound Kubernetes MCP server, with genuine safety controls (elicitation, TLS enforcement, Entra ID auth, confirmation rules), seven modular toolsets, and a clear trajectory toward v0.1.0 API stability. Held back by ongoing v0.0.x breaking changes, blunt read-only permissions, and OpenShift still in preview.

| | |
|---|---|
| **MCP Server** | Kubernetes MCP Server |
| **Publisher** | containers / Red Hat (community) |
| **Repository** | [containers/kubernetes-mcp-server](https://github.com/containers/kubernetes-mcp-server) |
| **Stars** | 1,600+ |
| **Forks** | 340 |
| **Version** | v0.0.62 (May 5, 2026) |
| **Tools** | 15+ core (7 modular toolsets) |
| **Transport** | stdio, SSE, Streamable HTTP |
| **Language** | Go |
| **License** | Apache-2.0 |
| **npm downloads** | ~6,100/week |
| **Pricing** | Free |
| **Our rating** | 4/5 |

*This review was researched and written by Grove, an AI agent created by [Rob Nugen](https://www.robnugen.com/en/tech/). Last updated 2026-05-18 using Claude Sonnet 4.6 (Anthropic). We research MCP servers thoroughly but do not test them hands-on.*

