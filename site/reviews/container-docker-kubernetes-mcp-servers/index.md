# Container, Docker & Kubernetes MCP Servers — Docker Management, Kubernetes Orchestration, Helm Charts, Podman, Portainer, and More

> Container, Docker, and Kubernetes MCP servers help AI agents manage containers, orchestrate clusters, deploy Helm charts, and interact with container registries via the Model Context Protocol.


Container, Docker, and Kubernetes MCP servers let AI assistants manage containers, orchestrate clusters, deploy applications, and interact with container registries through the Model Context Protocol. Instead of memorizing Docker commands or kubectl syntax, AI agents can manage infrastructure conversationally.

This review covers the **container, Docker, and Kubernetes** ecosystem — Docker management tools, Kubernetes orchestrators, Docker's official MCP infrastructure, alternative runtimes, Portainer integration, and Helm chart tools. For related servers, see our [DevOps review](/reviews/ci-cd-pipeline-mcp-servers/) and [Cloud Platform review](/reviews/cloud-storage-mcp-servers/).

The headline findings: **Three Kubernetes servers have 1,000+ stars** — containers/kubernetes-mcp-server, Flux159/mcp-server-kubernetes, and docker/mcp-gateway. **Docker is investing heavily in MCP** with three official projects (gateway, hub-mcp, registry). **ckreiling/mcp-server-docker (687 stars) leads Docker management** with a unique plan+apply compose workflow. Part of our **[Cloud & Infrastructure MCP category](/categories/cloud-infrastructure/)**.

## Docker Management

### ckreiling/mcp-server-docker (Most Popular)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [mcp-server-docker](https://github.com/ckreiling/mcp-server-docker) | 687 | Python | GPL-3.0 | 15+ |

The **most widely-adopted Docker MCP server** — provides comprehensive Docker management through natural language:

- **Container operations** — list, create, run, start, stop, remove containers
- **Monitoring** — fetch logs, monitor stats (CPU, memory usage), recreate containers
- **Image management** — pull, push, build, remove, list images
- **Infrastructure** — create and manage Docker networks and volumes
- **Compose workflow** — unique "plan+apply" approach where the AI proposes container configurations for user review before execution

Can run inside a Docker container itself by mounting the Docker socket. Important security note: any sensitive data exchanged with the LLM is inherently exposed unless running locally.

### QuantGeekDev/docker-mcp (Compose-Focused)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [docker-mcp](https://github.com/QuantGeekDev/docker-mcp) | 454 | Python | MIT | 4 |

A **simpler, compose-focused Docker server** for Claude AI integration:

- Container creation and instantiation
- Docker Compose stack deployment
- Container logs retrieval
- Container listing and status monitoring

Focused on basic operations rather than comprehensive orchestration — currently lacks volume management, network configuration, health checks, restart policies, and resource constraints.

### williajm/mcp_docker (Most Comprehensive)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [mcp_docker](https://github.com/williajm/mcp_docker) | 3 | Python | MIT | 33 |

The **most feature-complete Docker MCP server** despite low star count — 33 individually-configurable tools across 5 categories:

- **Container management** (10 tools) — list, inspect, create, start, stop, restart, remove, logs, exec, stats
- **Image management** (9 tools) — list, inspect, pull, build, push, tag, remove, prune, history
- **Network management** (6 tools) — list, inspect, create, connect, disconnect, remove
- **Volume management** (5 tools) — list, inspect, create, remove, prune
- **System tools** (3 tools) — version, events, system prune

Features a **three-tier safety system** (SAFE/MODERATE/DESTRUCTIVE) with tool filtering, 5 AI prompts (troubleshooting, optimization, compose generation, networking debug, security audit), dual transport (stdio/HTTP), and comprehensive testing including fuzz tests with ClusterFuzzLite. 155 commits — most mature codebase in this subcategory.

## Kubernetes Orchestration

### containers/kubernetes-mcp-server (Red Hat-Backed)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [kubernetes-mcp-server](https://github.com/containers/kubernetes-mcp-server) | 1,300 | Go | Apache-2.0 | 40 |

A **native Go implementation** backed by Red Hat that communicates directly with the Kubernetes API — not a kubectl wrapper. Provides 40 tools across configurable toolsets:

- **Core** — pods, events, namespaces, generic resource CRUD
- **Config** — kubeconfig management with automatic change detection
- **Helm** — install, list, uninstall charts
- **KCP** — workspace management
- **Kiali** — service mesh visualization
- **KubeVirt** — virtual machine management

Single native binary with no external dependencies. Multi-cluster support, read-only mode, destructive operation restrictions, OpenTelemetry tracing. Deployable via its own Helm chart. 747 commits, 285 forks — very active development.

### rohitg00/kubectl-mcp-server (Largest Tool Count)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [kubectl-mcp-server](https://github.com/rohitg00/kubectl-mcp-server) | 848 | Python | MIT | 253 |

The **largest Kubernetes MCP tool set** — 253 tools and 8 workflow prompts:

- **Pod diagnostics** — crash analysis, log inspection
- **Deployment management** — creation, scaling, rollbacks
- **Cost optimization** — identify resource waste
- **Network diagnostics** — connectivity troubleshooting
- **RBAC auditing** — role-based access control analysis
- **Security scanning** — cluster security assessment
- **Helm chart management** — chart operations
- **Interactive dashboards** — 6 UI tools for visualization

Available via npx (zero-install), pip, or Docker. Works with 15+ MCP-compatible clients including Claude Desktop, Cursor, Windsurf, GitHub Copilot, and Gemini CLI.

### Flux159/mcp-server-kubernetes (Observability-Focused)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [mcp-server-kubernetes](https://github.com/Flux159/mcp-server-kubernetes) | 1,300 | TypeScript | — | 20+ |

A **TypeScript-based Kubernetes server** with strong observability features:

- **Resource management** — get, list, describe, create, apply, delete
- **Operations** — logging, context switching, scaling, patching, rollouts
- **Port forwarding** — pod and service connectivity
- **Node management** — cordon, drain, uncordon
- **Pod cleanup** — remove evicted, failed, or problematic pods
- **Helm integration** — install, upgrade, uninstall, template charts

Differentiator: **built-in OpenTelemetry integration** with distributed tracing supporting Jaeger, Tempo, Grafana, Datadog, and New Relic backends. Non-destructive mode and secrets masking available. 772 commits — very active.

## Docker Official Projects

Docker is investing heavily in MCP as a first-class integration path, with three official projects:

### docker/mcp-gateway (Docker Desktop MCP Toolkit)

| Server | Stars | Language | License | Commits |
|--------|-------|----------|---------|---------|
| [mcp-gateway](https://github.com/docker/mcp-gateway) | 1,300 | Go | MIT | 865 |

The **core of Docker's MCP strategy** — powers the MCP Toolkit in Docker Desktop. Acts as a protocol bridge and lifecycle manager:

- **Container isolation** — each MCP server runs in its own Docker container
- **Unified interface** — single gateway between AI clients and multiple MCP servers
- **Authentication** — integrated OAuth flows and Docker Desktop secrets management
- **Profiles** — organize servers into logical groupings, shareable via OCI registries
- **Discovery** — dynamic tool/resource discovery across connected servers
- **Multi-client** — VS Code, Cursor, Claude Desktop share consistent tool availability

### docker/hub-mcp (Docker Hub Search)

| Server | Stars | Language | License | Commits |
|--------|-------|----------|---------|---------|
| [hub-mcp](https://github.com/docker/hub-mcp) | 130 | TypeScript | Apache-2.0 | — |

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
| [mcp-registry](https://github.com/docker/mcp-registry) | 453 | Go | MIT | — |

The **official curated MCP server catalog** with enterprise-grade trust:

- **Cryptographic signatures** on all MCP server images
- **Provenance tracking** for build verification
- **Software Bills of Materials (SBOMs)** for compliance
- **Quality review** for security and standards compliance
- **Docker Desktop integration** — browse in the MCP Toolkit UI

100+ verified tools at launch from partners like Stripe, Elastic, and Neo4j.

## Container Runtimes

### manusa/podman-mcp-server (Podman + Docker)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [podman-mcp-server](https://github.com/manusa/podman-mcp-server) | 61 | Go | Apache-2.0 | 12+ |

Supports **both Podman and Docker** container runtimes:

- **Container operations** — inspect, list, logs, run, stop, remove
- **Image management** — build from Dockerfiles, pull, push, remove
- **Infrastructure** — network listing, volume management
- **Dual backends** — REST API via Unix socket (preferred) or CLI wrapper (fallback)
- **Multiple transports** — stdio, HTTP with Streamable protocol, Server-Sent Events

Automatic runtime detection. Available on npm and PyPI for easy installation. 154 commits.

## Portainer Integration

### portainer/portainer-mcp (Enterprise Container Management)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [portainer-mcp](https://github.com/portainer/portainer-mcp) | 127 | Go | Zlib | 15+ |

Connects AI assistants to **Portainer environments** for teams already using Portainer:

- **Environment management** — list environments, update tags, manage access policies
- **Stack operations** — create/update Docker stacks, retrieve compose files
- **User & team administration** — manage users, teams, access groups
- **API proxies** — Docker and Kubernetes API access through Portainer
- **Local stacks** — deploy standalone Docker Compose stacks (v0.7.0+)

Pre-built binaries for Linux (amd64, arm64) and macOS (arm64). Read-only mode available for safety. 112 commits, 5 contributors.

## Helm Chart Tools

### zekker6/mcp-helm (Repository Inspector)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [mcp-helm](https://github.com/zekker6/mcp-helm) | 21 | Go | MIT | 7 |

A **focused Helm repository inspection tool** — 7 tools for chart discovery and analysis:

- **list_repository_charts** — all charts in a repository
- **list_chart_versions** — available versions/tags
- **get_latest_version_of_chart** — most recent release
- **get_chart_values** — extract values files (any version)
- **get_chart_contents** — full chart materials including templates
- **get_chart_dependencies** — dependencies from Chart.yaml
- **get_chart_images** — container images via template rendering

Supports traditional HTTP Helm repositories and OCI registries (Docker Hub, GHCR). Authentication for basic auth, mTLS, and OCI credentials. Public instance available at mcp-helm.zekker.dev. 186 commits.

## What's Missing

Despite the strength of this category, notable gaps remain:

- **No Docker Swarm management** — Swarm is declining but still used in production
- **No container security scanning** — no Trivy, Grype, or Snyk container scanning integration
- **Limited multi-cluster federation** — each server manages individual clusters only
- **No cloud Kubernetes cost management** — no FinOps or cost allocation tools
- **No GitOps integration** — no ArgoCD or Flux CD workflow triggers
- **No service mesh management** — beyond Kiali integration in kubernetes-mcp-server
- **No container registry vulnerability scanning** — image scanning before deployment
- **No Kubernetes operator management** — installing and managing operators
- **No namespace-level resource quota tools** — quota management and enforcement

## Bottom Line

Container and Kubernetes MCP servers form **one of the strongest infrastructure categories** in the MCP ecosystem. Docker management has multiple mature options — ckreiling's server leads on adoption (687 stars) while williajm's leads on features (33 tools with safety tiers). Kubernetes is exceptionally well-served with three implementations over 800 stars, each taking a different approach: native Go API (containers/kubernetes-mcp-server), Python wrapper with 253 tools (kubectl-mcp-server), and TypeScript with OpenTelemetry (Flux159/mcp-server-kubernetes).

Docker's official investment through mcp-gateway, hub-mcp, and mcp-registry signals that the company sees MCP as a first-class integration path — not a community experiment. The Podman and Portainer entries ensure the ecosystem isn't Docker-only. Helm chart inspection rounds things out.

The main frontier is security scanning, GitOps workflows, and multi-cluster operations. When those gaps fill, this will be a 5/5 category.

**Rating: 4/5** — Strong ecosystem with enterprise backing, multiple mature implementations, and clear Docker corporate investment. Gaps in security scanning and GitOps keep it from a perfect score.

---

*This review was researched and written by an AI agent. We do not test MCP servers hands-on — our analysis is based on documentation, GitHub repositories, and community data. See our [methodology](/about/) for details.*

*This review was last edited on 2026-03-16 using Claude Opus 4.6 (Anthropic).*

