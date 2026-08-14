# Container, Docker & Kubernetes MCP Servers — Docker Management, Kubernetes Orchestration, Helm Charts, Podman, Portainer, and More

> Container, Docker, and Kubernetes MCP servers help AI agents manage containers, orchestrate clusters, deploy Helm charts, and interact with container registries via the Model Context Protocol.


Container, Docker, and Kubernetes MCP servers let AI assistants manage containers, orchestrate clusters, deploy applications, and interact with container registries through the Model Context Protocol. Instead of memorizing Docker commands or kubectl syntax, AI agents can manage infrastructure conversationally.

This review covers the **container, Docker, and Kubernetes** ecosystem — Docker management tools, Kubernetes orchestrators, Docker's official MCP infrastructure, alternative runtimes, Portainer integration, and Helm chart tools. For related servers, see our [DevOps review](/reviews/ci-cd-pipeline-mcp-servers/) and [Cloud Platform review](/reviews/cloud-storage-mcp-servers/).

The headline findings: **Docker's official mcp-gateway is at ~1,500 stars** (v0.42.0→v0.43.3) with MCP Profile Templates, Dynamic MCPs, and OAuth support in Docker Desktop 4.67. **Red Hat's kubernetes-mcp-server surged to ~2,000 stars** (from ~1,300 in early 2026) with Tekton and Entra ID. **Community Docker servers are stagnating** — ckreiling (14 months dormant, one automated revival commit in August 2026) and QuantGeekDev (20+ months dormant) are coasting on stars. **SUSE Rancher Prime announced built-in MCP** at KubeCon EU 2026. Part of our **[Cloud & Infrastructure MCP category](/categories/cloud-infrastructure/)**.

## Docker Management

### ckreiling/mcp-server-docker (Most Popular — ⚠️ Long-Dormant, One Recent Commit)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [mcp-server-docker](https://github.com/ckreiling/mcp-server-docker) | 736 | Python | GPL-3.0 | 15+ |

The **most widely-adopted Docker MCP server** by star count — provides comprehensive Docker management through natural language:

- **Container operations** — list, create, run, start, stop, remove containers
- **Monitoring** — fetch logs, monitor stats (CPU, memory usage), recreate containers
- **Image management** — pull, push, build, remove, list images
- **Infrastructure** — create and manage Docker networks and volumes
- **Compose workflow** — unique "plan+apply" approach where the AI proposes container configurations for user review before execution
- **SSH support** — [remote Docker connections added May 11, 2025](https://github.com/ckreiling/mcp-server-docker/pull/24)

Can run inside a Docker container itself by mounting the Docker socket. Important security note: any sensitive data exchanged with the LLM is inherently exposed unless running locally.

*Correction (2026-08-14 audit): an earlier version of this review said the project was "dormant since June 2025 — no commits in 11 months." That was accurate as of our May 2026 refresh but is now stale — [the repo's last commit before this audit was June 5, 2025, until a single automated dependency-migration commit landed on August 7, 2026](https://github.com/ckreiling/mcp-server-docker/commits/main) ("Migrate to MCP Python SDK v2," authored by an automated integration account, not the original maintainer). Treat this as a 14-month-dormant project with one recent revival commit, not as actively maintained — still worth pairing with docker/mcp-gateway for updates and security patches.*

### QuantGeekDev/docker-mcp (Compose-Focused — ⚠️ Abandoned)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [docker-mcp](https://github.com/QuantGeekDev/docker-mcp) | 498 | Python | MIT | 4 |

A **simpler, compose-focused Docker server** for Claude AI integration:

- Container creation and instantiation
- Docker Compose stack deployment
- Container logs retrieval
- Container listing and status monitoring

Focused on basic operations rather than comprehensive orchestration — lacks volume management, network configuration, health checks, restart policies, and resource constraints.

⚠️ **Abandoned** — [no commits since December 14, 2024](https://github.com/QuantGeekDev/docker-mcp/commits/main) (20+ months dormant as of this audit). Not recommended for new projects.

### williajm/mcp_docker — removed, repo no longer exists

*Correction (2026-08-14 audit): a prior version of this section covered williajm/mcp_docker as "the most actively maintained community Docker server," citing v1.2.8, a three-tier safety system, and active CVE patching. As of this audit, `github.com/williajm/mcp_docker` returns a 404, the account's public repository list no longer includes a project by that name, no matching package exists on PyPI, and no Wayback Machine snapshot is available. We cannot verify the repository still exists in any accessible form, so per our sourcing standard we've removed the section rather than repeat unverifiable claims. If it reappears under a new name or owner, we'll restore coverage with fresh citations.*

## Kubernetes Orchestration

### containers/kubernetes-mcp-server (Red Hat-Backed — Surging)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [kubernetes-mcp-server](https://github.com/containers/kubernetes-mcp-server) | ~2,000 | Go | Apache-2.0 | 40+ |

A **native Go implementation** backed by Red Hat that communicates directly with the Kubernetes API — not a kubectl wrapper. Continued its surge past our last refresh: roughly **1,300 stars in early 2026 to ~2,000 as of this audit**. Provides 40+ tools across configurable toolsets:

- **Core** — pods, events, namespaces, generic resource CRUD
- **Config** — kubeconfig management with automatic change detection
- **Helm** — install, list, uninstall charts
- **Tekton** — pipeline and task management (NEW in v0.0.60+)
- **KCP** — workspace management
- **Kiali** — service mesh visualization
- **KubeVirt** — virtual machine management (refactored to v2.25)

**[v0.0.61 (April 24, 2026)](https://github.com/containers/kubernetes-mcp-server/releases/tag/v0.0.61)** — Microsoft Entra ID with On-Behalf-Of token exchange (first K8s MCP with Azure AD). Confirmation rules for destructive operations. Per-session rate limiting. `require_tls` config. Multi-arch images (s390x, ppc64le). Read-only root filesystem. Configurable ServiceAccount token auto-mounting. Gateway API HTTPRoute support. User-scoped targets (breaking change in v0.0.60). Zero CVEs. ~1,030 commits as of this audit (up from 871 in May) — very active development; the project has since shipped through [v0.0.66 (July 31, 2026)](https://github.com/containers/kubernetes-mcp-server/releases/tag/v0.0.66).

### rohitg00/kubectl-mcp-server (Largest Tool Count)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [kubectl-mcp-server](https://github.com/rohitg00/kubectl-mcp-server) | 947 | Python | MIT | 253 |

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
| [mcp-server-kubernetes](https://github.com/Flux159/mcp-server-kubernetes) | 1,500+ | TypeScript | — | 20+ |

A **TypeScript-based Kubernetes server** with strong observability features:

- **Resource management** — get, list, describe, create, apply, delete
- **Operations** — logging, context switching, scaling, patching, rollouts
- **Port forwarding** — pod and service connectivity
- **Node management** — cordon, drain, uncordon
- **Pod cleanup** — remove evicted, failed, or problematic pods
- **Helm integration** — install, upgrade, uninstall, template charts
- **kubectl_reconnect** tool (NEW in v3.5.0)

Differentiator: **built-in OpenTelemetry integration** with distributed tracing supporting Jaeger, Tempo, Grafana, Datadog, and New Relic backends. Non-destructive mode and secrets masking available. ~870 commits as of this audit (up from 785 in May).

⚠️ **[GHSA-4xqg-gf5c-ghwq / CVE-2026-39884](https://github.com/Flux159/mcp-server-kubernetes/security/advisories/GHSA-4xqg-gf5c-ghwq) (CVSS 8.3, HIGH)** — argument injection in port_forward, patched in v3.5.0 ([SentinelOne writeup](https://www.sentinelone.com/vulnerability-database/cve-2026-39884/)). Constant-time auth token comparison also added. **5 total security advisories** — most of any Kubernetes MCP server. The project has continued releasing since; [current latest is v4.1.4 (August 8, 2026)](https://github.com/Flux159/mcp-server-kubernetes/releases), so any version from v3.5.0 onward has the fix — update if you're on v3.4.0 or earlier.

## Docker Official Projects

Docker is investing heavily in MCP as a first-class integration path, with three official projects:

### docker/mcp-gateway (Docker Desktop MCP Toolkit — Surging)

| Server | Stars | Language | License | Commits |
|--------|-------|----------|---------|---------|
| [mcp-gateway](https://github.com/docker/mcp-gateway) | ~1,500 | Go | MIT | 1,000+ |

The **core of Docker's MCP strategy** — powers the MCP Toolkit in Docker Desktop. **[v0.42.0 (April 30, 2026)](https://github.com/docker/mcp-gateway/releases/tag/v0.42.0)** with rapid release cadence — the project has kept shipping since, reaching [v0.43.3 (July 16, 2026)](https://github.com/docker/mcp-gateway/releases/tag/v0.43.3) as of this audit. Acts as a protocol bridge and lifecycle manager:

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
| [hub-mcp](https://github.com/docker/hub-mcp) | 159 | TypeScript | Apache-2.0 | — |

Interfaces with Docker Hub APIs for **intelligent image discovery**:

- Repository search with architecture, OS, and category filters
- Namespace management and membership listing
- Repository CRUD operations
- Tag management with architecture/OS filtering
- Docker Hardened Images recommendations

Requires Node.js 22+. Can be configured as an MCP source for [Docker's "Ask Gordon" assistant](https://docs.docker.com/ai/gordon/) in Docker Desktop and CLI.

### docker/mcp-registry (Curated MCP Catalog)

| Server | Stars | Language | License | Commits |
|--------|-------|----------|---------|---------|
| [mcp-registry](https://github.com/docker/mcp-registry) | 543 | Go | MIT | — |

The **official curated MCP server catalog** with enterprise-grade trust — **1,100+ forks** as of this audit (up from 764 at last refresh) reflect its role as the canonical MCP server listing:

- **Cryptographic signatures** on all MCP server images
- **Provenance tracking** for build verification
- **Software Bills of Materials (SBOMs)** for compliance
- **Quality review** for security and standards compliance
- **Docker Desktop integration** — browse in the MCP Toolkit UI

[100+ verified tools at launch from partners like Stripe, Elastic, and Neo4j](https://www.docker.com/blog/introducing-docker-mcp-catalog-and-toolkit/).

⚠️ *Correction (2026-08-14 audit): this had been labeled a "critical" SSRF vulnerability in the mcp-registry catalog itself. Neither is accurate — [GHSA-x2f5-332j-9xwq / CVE-2026-33990](https://github.com/advisories/GHSA-x2f5-332j-9xwq) is a **moderate-severity** (CVSS v4 6.8) SSRF in **Docker Model Runner's** OCI registry token-exchange flow (a separate Docker Desktop component, not this repo), fixed in Docker Model Runner v1.1.25 / [Docker Desktop 4.67.0](https://www.sentinelone.com/vulnerability-database/cve-2026-33990/). Ensure Docker Desktop is updated to 4.67.0 or later if you use Model Runner.*

## Container Runtimes

### manusa/podman-mcp-server (Podman + Docker)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [podman-mcp-server](https://github.com/manusa/podman-mcp-server) | 81 | Go | Apache-2.0 | 12+ |

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
| [portainer-mcp](https://github.com/portainer/portainer-mcp) | 213 | Python | MIT | 15+ (legacy Go version) |

Connects AI assistants to **Portainer environments** for teams already using Portainer:

- **Environment management** — list environments, update tags, manage access policies
- **Stack operations** — create/update Docker stacks, retrieve compose files
- **User & team administration** — manage users, teams, access groups
- **API proxies** — Docker and Kubernetes API access through Portainer
- **Local stacks** — deploy standalone Docker Compose stacks (added in v0.7.0)
- **Improved proxy read-only mode** (added in v0.7.0)

Pre-built binaries for Linux (amd64, arm64) and macOS (arm64) were available for the Go-based v0.7.0 release described above.

*Correction (2026-08-14 audit): the official [portainer/portainer-mcp](https://github.com/portainer/portainer-mcp) repo has been substantially rewritten since our v0.7.0 (Go, Zlib license) description above. The current codebase is Python, built with FastMCP and [generated from the Portainer OpenAPI spec](https://raw.githubusercontent.com/portainer/portainer-mcp/main/README.md), licensed [MIT](https://raw.githubusercontent.com/portainer/portainer-mcp/main/LICENSE) (not Zlib), and versioned to track Portainer's own release numbers (currently 2.44.x) rather than an independent MCP-server version line. We could not confirm the exact current tool count for the rewritten server from public docs at audit time — treat the v0.7.0 feature list above as historical, and check the live repo before relying on Go-specific details like the pre-built binaries.*

**Update: jmrplens/portainer-mcp-enhanced is archived.** As of August 1, 2026 the [portainer-mcp-enhanced repo is archived](https://github.com/jmrplens/portainer-mcp-enhanced), with development continuing at a new, differently-named repo, [jmrplens/portainer-mcp](https://github.com/jmrplens/portainer-mcp) — a from-scratch rewrite ("began as a fork of the official Portainer MCP server but is no longer one: the server was rewritten from scratch and none of that project's code remains," per its README) that claims full 1:1 coverage of the Portainer REST API: 265 operations on Portainer CE and 442 on EE, exposed as either 98 granular tools or 15 grouped meta-tools. This supersedes the "98 tools" figure previously reported for the enhanced fork.

## Helm Chart Tools

### zekker6/mcp-helm (Repository Inspector)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [mcp-helm](https://github.com/zekker6/mcp-helm) | 26 | Go | MIT | 7 |

A **focused Helm repository inspection tool** — 7 tools for chart discovery and analysis:

- **list_repository_charts** — all charts in a repository
- **list_chart_versions** — available versions/tags
- **get_latest_version_of_chart** — most recent release
- **get_chart_values** — extract values files (any version)
- **get_chart_contents** — full chart materials including templates
- **get_chart_dependencies** — dependencies from Chart.yaml
- **get_chart_images** — container images via template rendering

Supports traditional HTTP Helm repositories and OCI registries (Docker Hub, GHCR). Authentication for basic auth, mTLS, and OCI credentials. Public instance available at mcp-helm.zekker.dev. **[v1.3.4 (April 14, 2026)](https://github.com/zekker6/mcp-helm/releases/tag/v1.3.4)** — actively maintained with regular releases; the project has since shipped through [v1.3.7 (July 29, 2026)](https://github.com/zekker6/mcp-helm/releases/tag/v1.3.7) as of this audit.

## Enterprise Kubernetes MCP

### SUSE Rancher Prime (Built-in MCP — NEW)

**[SUSE Rancher Prime announced built-in MCP support at KubeCon EU 2026](https://www.suse.com/c/kubecon-eu-2026-prime-ai-crews/)** — the first enterprise Kubernetes management platform with native MCP integration. The "Liz" AI assistant evolved into a multi-agent "Crew" system with specialized agents for Security, Observability, Platform, Linux, and App Collection. External MCP server integration available via Global Settings.

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

Container and Kubernetes MCP servers form **one of the strongest infrastructure categories** in the MCP ecosystem. The story since our initial review is enterprise consolidation: **Docker's mcp-gateway (~1,500 stars, v0.42.0→v0.43.3)** is becoming the de facto Docker MCP standard with Profile Templates, Dynamic MCPs, and OAuth, while community Docker servers (ckreiling, QuantGeekDev) have largely gone dormant — ckreiling saw a single revival commit in August 2026 after 14 months quiet, but neither is actively maintained in any meaningful sense. *(Correction, 2026-08-14 audit: williajm/mcp_docker, previously cited here as the one actively-maintained alternative, is no longer accessible on GitHub — see the note above.)*

Kubernetes is surging: **Red Hat's server passed ~2,000 stars** (up from ~1,300 in early 2026) with Tekton, Entra ID, and confirmation rules. **SUSE Rancher Prime announced built-in MCP** at KubeCon EU 2026 — the first enterprise K8s management platform with native MCP support. However, **Flux159's CVE-2026-39884** (CVSS 8.3) is a reminder that security maturity varies significantly across implementations.

The Podman server's migration to the official MCP Go SDK, Portainer's Docker Compose support (in the now-superseded v0.7.0 Go release), and jmrplens's Portainer coverage (now continued at portainer-mcp, not portainer-mcp-enhanced, with 265–442 API operations) round out a maturing ecosystem. The main frontier remains security scanning, multi-cluster operations, and full GitOps integration.

**Rating: 4/5** — Enterprise investment is accelerating (Docker Profile Templates, Red Hat Tekton/Entra ID, SUSE Rancher built-in MCP), but community server stagnation and security scanning gaps prevent a perfect score.

---

*This review was researched and written by an AI agent. We do not test MCP servers hands-on — our analysis is based on documentation, GitHub repositories, and community data. See our [methodology](/about/) for details.*

*This review was originally written 2026-05-01 using Claude Opus 4.6 (Anthropic); last claim-level citation audit and correction pass 2026-08-14 using Claude Sonnet 5 (Anthropic).*

