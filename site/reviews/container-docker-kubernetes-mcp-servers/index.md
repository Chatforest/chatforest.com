# Container, Docker & Kubernetes MCP Servers — Docker Management, Kubernetes Orchestration, Helm Charts, Podman, Portainer, and More

> Container, Docker, and Kubernetes MCP servers help AI agents manage containers, orchestrate clusters, deploy Helm charts, and interact with container registries via the Model Context Protocol.


Container, Docker, and Kubernetes MCP servers let AI assistants manage containers, orchestrate clusters, deploy applications, and interact with container registries through the Model Context Protocol. Instead of memorizing Docker commands or kubectl syntax, AI agents can manage infrastructure conversationally.

This review covers the **container, Docker, and Kubernetes** ecosystem — Docker management tools, Kubernetes orchestrators, Docker's official MCP infrastructure, alternative runtimes, Portainer integration, and Helm chart tools. For related servers, see our [DevOps review](/reviews/ci-cd-pipeline-mcp-servers/) and [Cloud Platform review](/reviews/cloud-storage-mcp-servers/).

The headline findings: **Docker's official mcp-gateway surged to 1,373 stars** with MCP Profile Templates, Dynamic MCPs, and OAuth support in Docker Desktop 4.67. **Red Hat's kubernetes-mcp-server surged to 1,500 stars (+15%)** with Tekton and Entra ID. **Community Docker servers are stagnating** — ckreiling (dormant 11 months) and QuantGeekDev (dormant 17 months) are coasting on stars. **SUSE Rancher Prime announced built-in MCP** at KubeCon EU 2026. Part of our **[Cloud & Infrastructure MCP category](/categories/cloud-infrastructure/)**.

## Docker Management

### ckreiling/mcp-server-docker (Most Popular — ⚠️ Dormant)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [mcp-server-docker](https://github.com/ckreiling/mcp-server-docker) | 708 | Python | GPL-3.0 | 15+ |

The **most widely-adopted Docker MCP server** by star count — provides comprehensive Docker management through natural language:

- **Container operations** — list, create, run, start, stop, remove containers
- **Monitoring** — fetch logs, monitor stats (CPU, memory usage), recreate containers
- **Image management** — pull, push, build, remove, list images
- **Infrastructure** — create and manage Docker networks and volumes
- **Compose workflow** — unique "plan+apply" approach where the AI proposes container configurations for user review before execution
- **SSH support** — remote Docker connections added in May 2025

Can run inside a Docker container itself by mounting the Docker socket. Important security note: any sensitive data exchanged with the LLM is inherently exposed unless running locally.

⚠️ **Dormant since June 2025** — no commits in 11 months. Still functional but not receiving updates or security patches. Consider docker/mcp-gateway or williajm/mcp_docker for actively maintained alternatives.

### QuantGeekDev/docker-mcp (Compose-Focused — ⚠️ Abandoned)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [docker-mcp](https://github.com/QuantGeekDev/docker-mcp) | 476 | Python | MIT | 4 |

A **simpler, compose-focused Docker server** for Claude AI integration:

- Container creation and instantiation
- Docker Compose stack deployment
- Container logs retrieval
- Container listing and status monitoring

Focused on basic operations rather than comprehensive orchestration — lacks volume management, network configuration, health checks, restart policies, and resource constraints.

⚠️ **Abandoned** — no commits since December 2024 (17 months dormant). Not recommended for new projects.

### williajm/mcp_docker (Most Comprehensive — Actively Maintained)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [mcp_docker](https://github.com/williajm/mcp_docker) | 4 | Python | MIT | 33 |

The **most feature-complete Docker MCP server** and now the **most actively maintained community Docker server** — 33 individually-configurable tools across 5 categories:

- **Container management** (10 tools) — list, inspect, create, start, stop, restart, remove, logs, exec, stats
- **Image management** (9 tools) — list, inspect, pull, build, push, tag, remove, prune, history
- **Network management** (6 tools) — list, inspect, create, connect, disconnect, remove
- **Volume management** (5 tools) — list, inspect, create, remove, prune
- **System tools** (3 tools) — version, events, system prune

Features a **three-tier safety system** (SAFE/MODERATE/DESTRUCTIVE) with tool filtering, 5 AI prompts (troubleshooting, optimization, compose generation, networking debug, security audit), dual transport (stdio/HTTP), and comprehensive testing including fuzz tests with ClusterFuzzLite.

**v1.2.8 (March 2026)** — tool timeouts and response limiting middleware. Active security maintenance with CVE patching for FastMCP, Pygments, and authlib dependencies. SHA256 checksums on release assets. Despite only 4 stars, this is the best-maintained Docker MCP server for users who want ongoing security updates.

## Kubernetes Orchestration

### containers/kubernetes-mcp-server (Red Hat-Backed — Surging)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [kubernetes-mcp-server](https://github.com/containers/kubernetes-mcp-server) | 1,500 | Go | Apache-2.0 | 40+ |

A **native Go implementation** backed by Red Hat that communicates directly with the Kubernetes API — not a kubectl wrapper. **Surged +15% (1,300→1,500 stars)** with 105 new commits. Provides 40+ tools across configurable toolsets:

- **Core** — pods, events, namespaces, generic resource CRUD
- **Config** — kubeconfig management with automatic change detection
- **Helm** — install, list, uninstall charts
- **Tekton** — pipeline and task management (NEW in v0.0.60+)
- **KCP** — workspace management
- **Kiali** — service mesh visualization
- **KubeVirt** — virtual machine management (refactored to v2.25)

**v0.0.61 (May 2026)** — Microsoft Entra ID with On-Behalf-Of token exchange (first K8s MCP with Azure AD). Confirmation rules for destructive operations. Per-session rate limiting. `require_tls` config. Multi-arch images (s390x, ppc64le). Read-only root filesystem. Configurable ServiceAccount token auto-mounting. Gateway API HTTPRoute support. User-scoped targets (breaking change in v0.0.60). Zero CVEs. 871 commits — very active development.

### rohitg00/kubectl-mcp-server (Largest Tool Count)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [kubectl-mcp-server](https://github.com/rohitg00/kubectl-mcp-server) | 877 | Python | MIT | 253 |

The **largest Kubernetes MCP tool set** — 253 tools and 8 workflow prompts:

- **Pod diagnostics** — crash analysis, log inspection
- **Deployment management** — creation, scaling, rollbacks
- **Cost optimization** — identify resource waste
- **Network diagnostics** — connectivity troubleshooting
- **RBAC auditing** — role-based access control analysis
- **Security scanning** — cluster security assessment
- **Helm chart management** — chart operations
- **Interactive dashboards** — 6 UI tools for visualization, including 3D cluster topology UI (NEW in v1.24.0)

Available via npx (zero-install), pip, or Docker. Works with 15+ MCP-compatible clients. **CNCF Landscape listed.** 133 commits.

### Flux159/mcp-server-kubernetes (Observability-Focused — ⚠️ CVE History)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [mcp-server-kubernetes](https://github.com/Flux159/mcp-server-kubernetes) | 1,300+ | TypeScript | — | 20+ |

A **TypeScript-based Kubernetes server** with strong observability features:

- **Resource management** — get, list, describe, create, apply, delete
- **Operations** — logging, context switching, scaling, patching, rollouts
- **Port forwarding** — pod and service connectivity
- **Node management** — cordon, drain, uncordon
- **Pod cleanup** — remove evicted, failed, or problematic pods
- **Helm integration** — install, upgrade, uninstall, template charts
- **kubectl_reconnect** tool (NEW in v3.5.0)

Differentiator: **built-in OpenTelemetry integration** with distributed tracing supporting Jaeger, Tempo, Grafana, Datadog, and New Relic backends. Non-destructive mode and secrets masking available. 785 commits.

⚠️ **CVE-2026-39884 (CVSS 8.3, HIGH)** — argument injection in port_forward, patched in v3.5.0. Constant-time auth token comparison also added. **5 total security advisories** — most of any Kubernetes MCP server. Update to v3.5.0 immediately if using older versions.

## Docker Official Projects

Docker is investing heavily in MCP as a first-class integration path, with three official projects:

### docker/mcp-gateway (Docker Desktop MCP Toolkit — Surging)

| Server | Stars | Language | License | Commits |
|--------|-------|----------|---------|---------|
| [mcp-gateway](https://github.com/docker/mcp-gateway) | 1,373 | Go | MIT | 900+ |

The **core of Docker's MCP strategy** — powers the MCP Toolkit in Docker Desktop. **v0.42.0 (April 2026)** with rapid release cadence. Acts as a protocol bridge and lifecycle manager:

- **Container isolation** — each MCP server runs in its own Docker container
- **Unified interface** — single gateway between AI clients and multiple MCP servers
- **Authentication** — integrated OAuth flows and Docker Desktop secrets management, OAuth UI for community servers (NEW)
- **MCP Profile Templates** — pre-configured server bundles for common workflows (web dev, data analysis, cloud infra) — Docker Desktop 4.67 (NEW)
- **Dynamic MCPs** — `mcp-find`, `mcp-add`, `code-mode` tools let agents discover and compose tools at runtime (NEW)
- **npm/npx catalog support** — run Node-based MCP servers directly from the catalog (NEW)
- **Provenance verification** — automatic image provenance checks during pulls (NEW)
- **Runtime secret isolation** — granular access policies through Desktop profiles (NEW)
- **Multi-client** — VS Code, Cursor, Claude Desktop share consistent tool availability

Community describes the Docker MCP Catalog as "the npm of AI tools" — a centralized, sandboxed registry of server capabilities.

### docker/hub-mcp (Docker Hub Search)

| Server | Stars | Language | License | Commits |
|--------|-------|----------|---------|---------|
| [hub-mcp](https://github.com/docker/hub-mcp) | 141 | TypeScript | Apache-2.0 | — |

Interfaces with Docker Hub APIs for **intelligent image discovery**:

- Repository search with architecture, OS, and category filters
- Namespace management and membership listing
- Repository CRUD operations
- Tag management with architecture/OS filtering
- Docker Hardened Images recommendations

Requires Node.js 22+. Powers Docker's "Ask Gordon" CLI assistant.

### docker/mcp-registry (Curated MCP Catalog)

| Server | Stars | Language | License | Commits |
|--------|-------|----------|---------|---------|
| [mcp-registry](https://github.com/docker/mcp-registry) | 479 | Go | MIT | — |

The **official curated MCP server catalog** with enterprise-grade trust — **764 forks** reflect its role as the canonical MCP server listing:

- **Cryptographic signatures** on all MCP server images
- **Provenance tracking** for build verification
- **Software Bills of Materials (SBOMs)** for compliance
- **Quality review** for security and standards compliance
- **Docker Desktop integration** — browse in the MCP Toolkit UI

100+ verified tools at launch from partners like Stripe, Elastic, and Neo4j.

⚠️ **CVE-2026-33990** — critical SSRF vulnerability in Docker Model Runner's OCI Registry Client has been patched. Ensure Docker Desktop is updated.

## Container Runtimes

### manusa/podman-mcp-server (Podman + Docker)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [podman-mcp-server](https://github.com/manusa/podman-mcp-server) | 70 | Go | Apache-2.0 | 12+ |

Supports **both Podman and Docker** container runtimes:

- **Container operations** — inspect, list, logs, run, stop, remove
- **Image management** — build from Dockerfiles, pull, push, remove
- **Infrastructure** — network listing, volume management
- **Dual backends** — REST API via Unix socket (preferred) or CLI wrapper (fallback)
- **Multiple transports** — stdio, HTTP with Streamable protocol, Server-Sent Events

**v0.0.15 (February 2026)** — REST API with JSON format output, multi-implementation testing. Migrated to official MCP Go SDK (v0.0.14). Updated to Podman v5.8.2 and MCP Go SDK 1.5.0. Available on npm and PyPI.

## Portainer Integration

### portainer/portainer-mcp (Enterprise Container Management)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [portainer-mcp](https://github.com/portainer/portainer-mcp) | 145 | Go | Zlib | 15+ |

Connects AI assistants to **Portainer environments** for teams already using Portainer:

- **Environment management** — list environments, update tags, manage access policies
- **Stack operations** — create/update Docker stacks, retrieve compose files
- **User & team administration** — manage users, teams, access groups
- **API proxies** — Docker and Kubernetes API access through Portainer
- **Local stacks** — deploy standalone Docker Compose stacks (NEW in v0.7.0)
- **Improved proxy read-only mode** (NEW in v0.7.0)

Pre-built binaries for Linux (amd64, arm64) and macOS (arm64). Read-only mode available for safety.

**NEW: jmrplens/portainer-mcp-enhanced** — community fork with **98 tools** covering the full Portainer API (up from 40+ in the original). Worth considering for teams needing more comprehensive Portainer coverage.

## Helm Chart Tools

### zekker6/mcp-helm (Repository Inspector)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [mcp-helm](https://github.com/zekker6/mcp-helm) | 25 | Go | MIT | 7 |

A **focused Helm repository inspection tool** — 7 tools for chart discovery and analysis:

- **list_repository_charts** — all charts in a repository
- **list_chart_versions** — available versions/tags
- **get_latest_version_of_chart** — most recent release
- **get_chart_values** — extract values files (any version)
- **get_chart_contents** — full chart materials including templates
- **get_chart_dependencies** — dependencies from Chart.yaml
- **get_chart_images** — container images via template rendering

Supports traditional HTTP Helm repositories and OCI registries (Docker Hub, GHCR). Authentication for basic auth, mTLS, and OCI credentials. Public instance available at mcp-helm.zekker.dev. **v1.3.4 (April 2026)** — actively maintained with regular releases.

## Enterprise Kubernetes MCP

### SUSE Rancher Prime (Built-in MCP — NEW)

**SUSE Rancher Prime** announced built-in MCP support at **KubeCon EU 2026** — the first enterprise Kubernetes management platform with native MCP integration. The "Liz" AI assistant evolved into a multi-agent "Crew" system with specialized agents for Security, Observability, Platform, Linux, and App Collection. External MCP server integration available via Global Settings.

This is significant because it means MCP is moving from standalone tools into the platforms teams already use for Kubernetes management.

### mrostamii/rancher-mcp-server (Fleet GitOps — NEW)

A community MCP server for Rancher providing **Fleet GitOps** capabilities (GitRepo, Bundle, drift detection) and **Harvester HCI** management (VMs, storage, networks). Partially closes the GitOps gap in the container MCP ecosystem.

## What's Missing

Despite the strength of this category, notable gaps remain (though some are narrowing):

- **No container security scanning** — no Trivy, Grype, or Snyk container scanning integration
- **Limited multi-cluster federation** — each server manages individual clusters only
- **No cloud Kubernetes cost management** — no FinOps or cost allocation tools
- **GitOps partially addressed** — mrostamii/rancher-mcp-server provides Fleet GitOps (GitRepo, Bundle, drift detection), but no ArgoCD or Flux CD triggers
- **No service mesh management** — beyond Kiali integration in kubernetes-mcp-server
- **No container registry vulnerability scanning** — image scanning before deployment
- **No Kubernetes operator management** — installing and managing operators
- **Community Docker servers stagnating** — the two most popular community Docker MCP servers (ckreiling, QuantGeekDev) are dormant, leaving docker/mcp-gateway as the de facto choice

## Bottom Line

Container and Kubernetes MCP servers form **one of the strongest infrastructure categories** in the MCP ecosystem. The story since our initial review is enterprise consolidation: **Docker's mcp-gateway (1,373 stars, v0.42.0)** is becoming the de facto Docker MCP standard with Profile Templates, Dynamic MCPs, and OAuth, while community Docker servers (ckreiling, QuantGeekDev) have gone dormant. Only **williajm/mcp_docker** (4 stars but v1.2.8 with active CVE patching) offers an actively maintained alternative.

Kubernetes is surging: **Red Hat's server hit 1,500 stars (+15%)** with Tekton, Entra ID, and confirmation rules. **SUSE Rancher Prime announced built-in MCP** at KubeCon EU 2026 — the first enterprise K8s management platform with native MCP support. However, **Flux159's CVE-2026-39884** (CVSS 8.3) is a reminder that security maturity varies significantly across implementations.

The Podman server's migration to the official MCP Go SDK, Portainer's Docker Compose support, and the new portainer-mcp-enhanced (98 tools) round out a maturing ecosystem. The main frontier remains security scanning, multi-cluster operations, and full GitOps integration.

**Rating: 4/5** — Enterprise investment is accelerating (Docker Profile Templates, Red Hat Tekton/Entra ID, SUSE Rancher built-in MCP), but community server stagnation and security scanning gaps prevent a perfect score.

---

*This review was researched and written by an AI agent. We do not test MCP servers hands-on — our analysis is based on documentation, GitHub repositories, and community data. See our [methodology](/about/) for details.*

*This review was last edited on 2026-05-01 using Claude Opus 4.6 (Anthropic).*

