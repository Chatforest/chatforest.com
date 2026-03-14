---
title: "Container Registry MCP Servers — Docker Hub, ECR, ACR, JFrog, Harbor, and Beyond"
date: 2026-03-15T04:06:00+09:00
description: "Container registry MCP servers let AI agents search images, manage repositories, push to registries, scan for vulnerabilities, and track artifacts across Docker Hub, AWS ECR, Azure ACR, JFrog Artifactory, Harbor, and Nexus. We reviewed 12+ servers across 8 platforms. Docker Hub's official server leads with 13 tools and AI-powered image discovery across 100k+ public images. JFrog's official server is the most comprehensive at 22+ tools spanning repository management, security scanning, and runtime monitoring."
og_description: "Container registry MCP servers: Docker Hub (official, 13 tools, 130 stars), JFrog (official, 22+ tools, 112 stars), AWS ECR (via ECS+Finch, 10+ tools), Azure ACR (via microsoft/mcp, 2 tools), Harbor (11 tools), Nexus (16 tools), Trivy (image scanning). 12+ servers across 8 platforms. Rating: 3.5/5."
content_type: "Review"
card_description: "Container registry MCP servers across Docker Hub, JFrog, AWS ECR, Azure ACR, Harbor, and Nexus. Docker Hub's official server has AI-powered image discovery across 100k+ images. JFrog covers the full artifact lifecycle with 22+ tools. AWS provides ECR integration through both ECS and Finch MCP servers."
---

Container registries are the storage backbone of modern deployment — **every container that runs in production was pulled from one**. MCP servers for registries let AI agents search for images, manage repository metadata, push builds, and scan for vulnerabilities without the developer juggling CLI tools and web consoles.

The headline finding: **official vendor investment is strong but narrowly scoped**. Docker Hub has an official 13-tool MCP server. JFrog has the most comprehensive offering at 22+ tools. AWS provides ECR access through two dedicated MCP servers (ECS and Finch). Azure and Google have registry tools buried inside broader cloud platform MCP servers. But **no universal container registry MCP server exists** — each vendor covers only their own platform.

## The Landscape

### Docker Hub (Official)

| Server | Stars | Language | Tools | Auth | Transport |
|--------|-------|----------|-------|------|-----------|
| [docker/hub-mcp](https://github.com/docker/hub-mcp) | ~130 | TypeScript | 13 | Optional PAT | stdio |

**Docker Hub's official MCP server brings AI-powered image discovery across 100,000+ public images.** 130 stars, Apache 2.0, backed by Docker, Inc. Requires Node.js 22+. Also available through Docker MCP Toolkit in Docker Desktop for one-click setup.

13 tools across three domains:

**Image Discovery** (2 tools):

| Tool | What it does |
|------|-------------|
| `search` | AI-powered search across Docker Hub with architecture and OS filtering |
| `docker_hardened_images` | Discover Docker's security-hardened official images |

**Repository Management** (5 tools):

| Tool | What it does |
|------|-------------|
| `get_namespaces` | List available Docker Hub namespaces |
| `list_repositories_by_namespace` | Browse repositories within a namespace |
| `get_repository_info` | Full repository metadata — description, stars, pulls |
| `check_repository` | Verify a repository exists |
| `create_repository` | Create a new repository (requires PAT) |

**Tag Management** (4 tools):

| Tool | What it does |
|------|-------------|
| `list_repository_tags` | Browse available tags with filtering |
| `read_repository_tag` | Inspect a specific tag — layers, size, architecture |
| `check_repository_tag` | Verify a tag exists |
| `update_repository_info` | Update repository description and settings |

The **AI-powered search** is the standout feature — it understands natural language queries like "lightweight Python image for machine learning" and filters by architecture (ARM64, AMD64) and OS. Without authentication, you get read access to public images. With a Personal Access Token, you unlock repository creation and private repo access.

The Docker MCP Toolkit integration means Claude Desktop, Cursor, and VS Code users can enable this with a single click — no manual JSON configuration. That's the lowest setup friction of any server in this review.

**Also notable: [QuantGeekDev/docker-mcp](https://github.com/QuantGeekDev/docker-mcp)** — 454 stars, Python, MIT, 4 tools for Docker *engine* management (create-container, deploy-compose, get-logs, list-containers). This manages running containers, not the registry itself. See our [Docker MCP Server review](/reviews/docker-mcp-server/) for container runtime management, and [ckreiling/mcp-server-docker](https://github.com/ckreiling/mcp-server-docker) (687 stars, 19 tools) for the most comprehensive Docker engine MCP server.

### JFrog Artifactory (Official)

| Server | Stars | Language | Tools | Auth | Transport |
|--------|-------|----------|-------|------|-----------|
| [jfrog/mcp-jfrog](https://github.com/jfrog/mcp-jfrog) | ~112 | TypeScript | 22+ | JFrog token | stdio, SSE |

**JFrog's official MCP server is the most comprehensive artifact management integration available.** 112 stars, Node.js 18+. Supports Smithery one-click install, Docker, or npm. JFrog Artifactory supports Docker, Maven, npm, PyPI, and dozens of other package formats — making this useful far beyond just container images.

22+ tools across six categories:

**Repository Management** (7 tools): `check_jfrog_availability`, `create_local_repository`, `create_remote_repository`, `create_virtual_repository`, `list_repositories`, `set_folder_property`, `execute_aql_query`. The AQL (Artifactory Query Language) tool is powerful — it lets agents write structured queries to find artifacts across all repositories.

**Build Management** (2 tools): `list_jfrog_builds`, `get_specific_build`. Track which builds produced which container images — critical for traceability.

**Runtime Monitoring** (3 tools): `list_jfrog_runtime_clusters`, `get_jfrog_runtime_specific_cluster`, `list_jfrog_running_images`. See which container images are actively running across your infrastructure. This is a unique capability — no other MCP server in this review connects registry data to runtime state.

**Access Control** (4 tools): `list_jfrog_environments`, `list_jfrog_projects`, `get_specific_project`, `create_project`. Project and environment management for multi-team setups.

**Catalog & Curation** (5 tools): `jfrog_get_package_info`, `jfrog_get_package_versions`, `jfrog_get_package_version_vulnerabilities`, `jfrog_get_vulnerability_info`, `jfrog_get_package_curation_status`. The vulnerability tools integrate with JFrog Xray — agents can check CVEs for any package version before using it.

**Security Scanning** (1 tool): `jfrog_get_artifacts_summary`. Combined vulnerability and compliance summary for artifacts.

The **runtime monitoring + vulnerability scanning + artifact management** combination makes this the most complete "artifact lifecycle" MCP server. If your organization uses JFrog, this server covers the full pipeline from build to deploy to runtime observation.

### AWS ECR (via ECS + Finch MCP Servers)

AWS doesn't have a dedicated ECR MCP server. Instead, ECR functionality is distributed across two servers in the [awslabs/mcp](https://github.com/awslabs/mcp) monorepo (~4,700 stars, Apache 2.0):

#### ECS MCP Server

| Server | Stars | Language | Tools | Auth | Transport |
|--------|-------|----------|-------|------|-----------|
| [awslabs/mcp — ecs-mcp-server](https://github.com/awslabs/mcp/tree/main/src/ecs-mcp-server) | ~4,700* | Python | 7+ | AWS credentials | stdio |

**The ECS MCP server includes ECR repository creation and image push as part of ECS deployment workflows.** Python 3.10+. Available via pip (`awslabs.ecs-mcp-server`) or as an AWS-managed hosted service.

ECR-relevant tools: `containerize_app` (generate Dockerfiles), `build_and_push_image_to_ecr` (automated ECR repo creation via CloudFormation + Docker build + push), `ecs_resource_management` (manage ECS resources including ECR image references). The server handles IAM roles with push/pull permissions, returns full image URIs, and integrates with load balancers and auto-scaling.

The ECR integration is tightly coupled to ECS deployment — you can't use it for standalone registry management without the ECS context. Good for deployment pipelines, not for browsing or managing ECR repositories independently.

#### Finch MCP Server

| Server | Stars | Language | Tools | Auth | Transport |
|--------|-------|----------|-------|------|-----------|
| [awslabs/mcp — finch-mcp-server](https://github.com/awslabs/mcp/tree/main/src/finch-mcp-server) | ~4,700* | Python | 3 | AWS credentials | stdio |

**Finch (AWS's open-source container tool) gets a dedicated MCP server for building and pushing images.** 3 focused tools:

| Tool | What it does |
|------|-------------|
| `finch_build_container_image` | Build images with multi-platform support |
| `finch_push_image` | Push to ECR with hash-based tagging and credential verification |
| `finch_create_ecr_repo` | Create ECR repositories with immutable tags via boto3 |

The **immutable tags** enforcement is a security best practice — preventing tag overwriting that could introduce supply chain attacks. The `finch_push_image` tool verifies ECR credential helper configuration before attempting pushes, which prevents the common "no basic auth credentials" error.

*Star count shared across all servers in the awslabs/mcp monorepo.*

### Azure ACR (via Microsoft MCP)

| Server | Stars | Language | Tools | Auth | Transport |
|--------|-------|----------|-------|------|-----------|
| [microsoft/mcp](https://github.com/microsoft/mcp) | ~2,800 | C# | 2 ACR tools | Azure credentials | stdio |

**Azure Container Registry gets two read-only tools inside Microsoft's broader Azure MCP server.** 2,800 stars, MIT, covers 40+ Azure services. An earlier [Azure/azure-mcp](https://github.com/Azure/azure-mcp) repository (~1,200 stars) was archived in August 2025 in favor of this one.

ACR-specific tools:

| Tool | What it does |
|------|-------------|
| `azmcp-acr-registry-list` | List ACR registries in a subscription, optionally filtered by resource group |
| `azmcp-acr-registry-repository-list` | List repositories within an ACR registry |

That's it — **two tools, both read-only**. No image pushing, no tag management, no vulnerability scanning. This is enough for discovery ("What registries and images do we have?") but not for any registry management workflow. Given that the broader Azure MCP server covers 40+ services, ACR coverage is minimal compared to other Azure integrations.

Available via NuGet, npm, or Docker. All tools are designed to be non-destructive and idempotent — consistent with the overall Microsoft MCP server philosophy.

### Harbor (Community)

| Server | Stars | Language | Tools | Auth | Transport |
|--------|-------|----------|-------|------|-----------|
| [nomagicln/mcp-harbor](https://github.com/nomagicln/mcp-harbor) | ~6 | TypeScript | 11 | Harbor credentials | stdio |

**The only MCP server for Harbor, the CNCF-graduated open source container registry.** 6 stars, MIT, Node.js 18+. Small community project but functionally complete for basic Harbor management.

11 tools across four domains:

**Project Management**: `list_projects`, `get_project`, `create_project`, `delete_project`

**Repository Management**: `list_repositories`, `delete_repository`

**Tag Management**: `list_tags`, `delete_tag`

**Helm Charts**: `list_charts`, `list_chart_versions`, `delete_chart`

This covers the core Harbor workflow — create projects, manage repositories and tags, handle Helm charts. The **Helm chart management** is a nice addition that reflects Harbor's role as a multi-artifact registry (not just container images). Missing: vulnerability scanning integration (Harbor has built-in Trivy scanning that isn't exposed here), robot account management, replication policies, and garbage collection triggers.

Setup requires manual clone + npm install + build — no one-click install option.

### Sonatype Nexus (Community)

Two community MCP servers cover Nexus Repository Manager:

#### brianveltman/sonatype-mcp

| Server | Stars | Language | Tools | Auth | Transport |
|--------|-------|----------|-------|------|-----------|
| [brianveltman/sonatype-mcp](https://github.com/brianveltman/sonatype-mcp) | ~7 | TypeScript | 16 | Nexus credentials | stdio |

**The most comprehensive Nexus MCP server with 16 tools spanning repository, component, asset, system, and firewall management.** 7 stars, Node.js 18+. Installable globally via npm.

Repository tools (5): list, get, create, update, delete. Component tools (5): search, get, delete, get versions, upload. Plus system tools (status, blob stores, tasks, metrics, support zip) and optional firewall quarantine management. The **firewall tools** for quarantine retrieval and release are useful for organizations using Nexus Firewall to block suspicious components.

Covers Docker-hosted repositories alongside Maven, npm, PyPI, and other formats.

#### addozhang/nexus-mcp-server

| Server | Stars | Language | Tools | Auth | Transport |
|--------|-------|----------|-------|------|-----------|
| [addozhang/nexus-mcp-server](https://github.com/addozhang/nexus-mcp-server) | ~1 | Python | 6 | Header auth | HTTP streaming |

**A lighter alternative focused on read-only queries, with explicit Docker support.** 1 star, MIT, February 2026. 6 tools: `search_maven_artifact`, `get_maven_versions`, `search_python_package`, `get_python_versions`, `list_docker_images`, `get_docker_tags`.

The `list_docker_images` and `get_docker_tags` tools are Docker-specific — browsing container images stored in Nexus Docker repositories. Supports SSE and streamable HTTP transport. Available as a Docker image (`addozhang/nexus-mcp-server`).

### GCP Artifact Registry (Community)

| Server | Stars | Language | Tools | Auth | Transport |
|--------|-------|----------|-------|------|-----------|
| [enesbol/gcp-mcp](https://github.com/enesbol/gcp-mcp) | ~6 | Python | Multiple | GCP credentials | stdio |

**The only MCP server covering Google Cloud Artifact Registry, buried inside a broader GCP services MCP server.** 6 stars, MIT, single-developer project. Covers 8 GCP services: Artifact Registry, BigQuery, Cloud Build, Compute Engine, Cloud Run, Cloud Storage, IAM, and Pub/Sub.

Artifact Registry tools handle container and package management — listing repositories, browsing images, managing versions. But this is a community project with minimal adoption. **Google has no official Artifact Registry MCP server**, which is a notable gap given that GCP is a major cloud platform and Google has been investing heavily in MCP across other products.

Available via pip or Docker. Includes AI-guided configuration helpers.

### Container Image Scanning (via Trivy)

| Server | Stars | Language | Tools | Auth | Transport |
|--------|-------|----------|-------|------|-----------|
| [aquasecurity/trivy-mcp](https://github.com/aquasecurity/trivy-mcp) | ~37 | Go | Multiple | Optional | stdio, HTTP, SSE |

**Trivy's MCP plugin scans container images for vulnerabilities through natural language queries.** 37 stars, MIT, official Aqua Security project. Installs as a Trivy plugin (`trivy plugin install mcp`, then `trivy mcp`).

While covered in our [Code Security MCP Servers review](/reviews/code-security-mcp-servers/), Trivy is relevant here because **container image scanning is a core registry workflow**. Ask "Are there any critical CVEs in nginx:1.25?" and Trivy scans the image layers. This complements registry management servers — one manages the images, the other tells you if they're safe.

Trivy is the most widely-used open source container security scanner (23k+ stars on the main repo), so having an MCP plugin matters for registry workflows that include security gates.

### GHCR and Other Registries

**GitHub Container Registry (GHCR)**: No dedicated MCP server. GitHub's official [github-mcp-server](https://github.com/github/github-mcp-server) covers GitHub APIs broadly but doesn't expose GHCR-specific tools. The community [rideRTD/RTD-DevOps](https://github.com/rideRTD/RTD-DevOps) helper includes `ghcr_login_guide` and `ghcr_push` tools, but it's a small DevOps utility, not a GHCR management server.

**Quay.io**: No MCP server found. Red Hat's container registry lacks MCP integration.

**GitLab Container Registry**: No MCP server found. GitLab's broader MCP efforts don't yet cover their registry.

**DigitalOcean Container Registry**: No MCP server found.

## What's Missing

The container registry MCP ecosystem has clear gaps:

1. **No universal registry client** — every server is vendor-specific. A server that speaks the OCI Distribution API could manage any compliant registry (Docker Hub, GHCR, ACR, ECR, GCR, Harbor, Quay) through one interface.

2. **Image lifecycle management** — no server helps with tag retention policies, garbage collection, or automated cleanup of old images. This is one of the most common registry maintenance tasks.

3. **Multi-registry synchronization** — no server helps mirror or replicate images across registries. Organizations running hybrid cloud need this.

4. **SBOM and provenance** — with supply chain security becoming critical, no registry MCP server exposes SBOM data or image provenance (Sigstore/cosign signatures). JFrog's Xray integration is the closest.

5. **GHCR is completely uncovered** — surprising given GitHub's dominance in the developer ecosystem and GitHub's own investment in MCP.

## The Bottom Line

**Rating: 3.5 / 5** — Solid vendor coverage from Docker Hub and JFrog with comprehensive official servers. AWS provides good ECR integration through ECS and Finch servers. But the ecosystem is fragmented (no cross-registry server), Azure and GCP coverage is minimal, GHCR is uncovered, and community projects for Harbor and Nexus have very low adoption. The lack of a universal OCI registry MCP server is the biggest gap.

**Best for image discovery**: Docker Hub MCP (docker/hub-mcp) — AI-powered search across 100k+ images, one-click Docker Desktop setup.

**Best for artifact lifecycle**: JFrog MCP (jfrog/mcp-jfrog) — 22+ tools covering repositories, builds, runtime monitoring, and vulnerability scanning.

**Best for AWS workflows**: ECS + Finch MCP servers — tight ECR integration with secure defaults (immutable tags, IAM role management).

**Best for self-hosted registries**: Harbor MCP (nomagicln/mcp-harbor) — 11 tools for projects, repositories, tags, and Helm charts. Or Sonatype MCP (brianveltman/sonatype-mcp) for Nexus.

The container registry MCP space is functional but not yet mature. Official vendor servers cover the basics, but advanced registry workflows — lifecycle management, cross-registry sync, supply chain verification — still require manual tooling. As container security and supply chain concerns grow, expect this category to deepen significantly.

---

*ChatForest reviews MCP servers through research, documentation analysis, and community feedback. We do not run or test servers hands-on. Ratings reflect capability, maturity, and ecosystem fit based on available evidence. [About our methodology](/about/)*
