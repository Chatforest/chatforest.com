---
title: "Container Registry MCP Servers — Docker Hub, ECR, ACR, JFrog, Harbor, and Beyond"
date: 2026-03-15T04:06:00+09:00
description: "Container registry MCP servers let AI agents search images, manage repositories, push to registries, scan for vulnerabilities, and track artifacts across Docker Hub, AWS ECR"
og_description: "Container registry MCP servers: Docker Hub (official, 13 tools, 140 stars), JFrog (official remote + experimental 115 stars), AWS ECR (via ECS+Finch, 8.9K monorepo), Azure ACR (via microsoft/mcp, 2 tools), Harbor (11 tools), Nexus (16 tools), NEW Stacklok OCI Registry (universal, 4 tools, 12 stars), Trivy (image scanning). 13+ servers across 8 platforms. Rating: 3.5/5."
content_type: "Review"
card_description: "Container registry MCP servers across Docker Hub, JFrog, AWS ECR, Azure ACR, Harbor, and Nexus. Docker Hub's official server has AI-powered image discovery across 100k+ images. JFrog covers the full artifact lifecycle with 22+ tools. AWS provides ECR integration through both ECS and Finch MCP servers."
last_refreshed: 2026-04-25
---

Container registries are the storage backbone of modern deployment — **every container that runs in production was pulled from one**. MCP servers for registries let AI agents search for images, manage repository metadata, push builds, and scan for vulnerabilities without the developer juggling CLI tools and web consoles.

The headline finding: **official vendor investment is strong and expanding**. Docker Hub has an official 13-tool MCP server. JFrog now offers both an experimental open-source server and an official remote hosted MCP server, plus a Universal MCP Registry for governing MCP servers as artifacts. AWS provides ECR access through ECS and Finch MCP servers (now with a hosted option). Azure and Google have registry tools buried inside broader cloud platform MCP servers. And **the biggest gap is finally closing**: Stacklok's OCI Registry MCP server provides the first universal container registry client that works with any OCI-compliant registry.

**Category:** [Developer Tools](/categories/developer-tools/)

## The Landscape

### Docker Hub (Official)

| Server | Stars | Language | Tools | Auth | Transport |
|--------|-------|----------|-------|------|-----------|
| [docker/hub-mcp](https://github.com/docker/hub-mcp) | ~140 | TypeScript | 13 | Optional PAT | stdio |

**Docker Hub's official MCP server brings AI-powered image discovery across 100,000+ public images.** 140 stars (+8%), Apache 2.0, backed by Docker, Inc. Requires Node.js 22+. Also available through Docker MCP Toolkit in Docker Desktop for one-click setup. Docker Desktop 4.67.0 (March 30, 2026) added MCP profile template cards with an onboarding tour and fixed CVE-2026-33990 (SSRF vulnerability in Docker Model Runner's OCI registry client).

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

**Also notable: [QuantGeekDev/docker-mcp](https://github.com/QuantGeekDev/docker-mcp)** — 428 stars, Python, MIT, 4 tools for Docker *engine* management (create-container, deploy-compose, get-logs, list-containers). This manages running containers, not the registry itself. See our [Docker MCP Server review](/reviews/docker-mcp-server/) for container runtime management, and [ckreiling/mcp-server-docker](https://github.com/ckreiling/mcp-server-docker) (702 stars, 19 tools) for the most comprehensive Docker engine MCP server.

### JFrog Artifactory (Official)

| Server | Stars | Language | Tools | Auth | Transport |
|--------|-------|----------|-------|------|-----------|
| [jfrog/mcp-jfrog](https://github.com/jfrog/mcp-jfrog) | ~115 | TypeScript | 22+ | JFrog token | stdio, SSE |
| [jfrog/jfrog-mcp-server](https://github.com/jfrog/jfrog-mcp-server) | ~7 | TypeScript | 4 categories | OAuth | Remote hosted |

**JFrog now offers two MCP server options.** The experimental `mcp-jfrog` (115 stars, 17 commits) remains available for local use, but JFrog now explicitly directs users to the **official remote hosted MCP server** (`jfrog-mcp-server`, 7 stars, 31 commits) — a cloud-hosted server maintained by JFrog with OAuth authentication and automatic tool updates. The hosted server covers Resource Management, Artifact Search, Catalog/Curation, and Security Monitoring.

**Also new: JFrog Universal MCP Registry** (launched March 18, 2026) — treats every MCP server as a governed artifact with centralized discovery, configuration, and project-level permissions. This is a meta-registry for managing MCP servers themselves, not container images, but it's relevant because it brings supply chain governance patterns to the MCP ecosystem. Available as part of JFrog AI Catalog.

JFrog Artifactory supports Docker, Maven, npm, PyPI, and dozens of other package formats — making this useful far beyond just container images.

22+ tools across six categories:

**Repository Management** (7 tools): `check_jfrog_availability`, `create_local_repository`, `create_remote_repository`, `create_virtual_repository`, `list_repositories`, `set_folder_property`, `execute_aql_query`. The AQL (Artifactory Query Language) tool is powerful — it lets agents write structured queries to find artifacts across all repositories.

**Build Management** (2 tools): `list_jfrog_builds`, `get_specific_build`. Track which builds produced which container images — critical for traceability.

**Runtime Monitoring** (3 tools): `list_jfrog_runtime_clusters`, `get_jfrog_runtime_specific_cluster`, `list_jfrog_running_images`. See which container images are actively running across your infrastructure. This is a unique capability — no other MCP server in this review connects registry data to runtime state.

**Access Control** (4 tools): `list_jfrog_environments`, `list_jfrog_projects`, `get_specific_project`, `create_project`. Project and environment management for multi-team setups.

**Catalog & Curation** (5 tools): `jfrog_get_package_info`, `jfrog_get_package_versions`, `jfrog_get_package_version_vulnerabilities`, `jfrog_get_vulnerability_info`, `jfrog_get_package_curation_status`. The vulnerability tools integrate with JFrog Xray — agents can check CVEs for any package version before using it.

**Security Scanning** (1 tool): `jfrog_get_artifacts_summary`. Combined vulnerability and compliance summary for artifacts.

The **runtime monitoring + vulnerability scanning + artifact management** combination makes this the most complete "artifact lifecycle" MCP server. If your organization uses JFrog, this server covers the full pipeline from build to deploy to runtime observation.

### AWS ECR (via ECS + Finch MCP Servers)

AWS doesn't have a dedicated ECR MCP server. Instead, ECR functionality is distributed across two servers in the [awslabs/mcp](https://github.com/awslabs/mcp) monorepo (~8,900 stars, up from ~4,700, Apache 2.0, 1,487 commits):

#### ECS MCP Server

| Server | Stars | Language | Tools | Auth | Transport |
|--------|-------|----------|-------|------|-----------|
| [awslabs/mcp — ecs-mcp-server](https://github.com/awslabs/mcp/tree/main/src/ecs-mcp-server) | ~8,900* | Python | 7+ | AWS credentials | stdio, hosted |

**The ECS MCP server includes ECR repository creation and image push as part of ECS deployment workflows.** Python 3.10+. Available via pip (`awslabs.ecs-mcp-server`) or as an **AWS-managed hosted MCP server** — the hosted option is now recommended, with the legacy local installation no longer receiving updates.

ECR-relevant tools: `containerize_app` (generate Dockerfiles), `build_and_push_image_to_ecr` (automated ECR repo creation via CloudFormation + Docker build + push), `ecs_resource_management` (manage ECS resources including ECR image references). The server handles IAM roles with push/pull permissions, returns full image URIs, and integrates with load balancers and auto-scaling.

The ECR integration is tightly coupled to ECS deployment — you can't use it for standalone registry management without the ECS context. Good for deployment pipelines, not for browsing or managing ECR repositories independently.

#### Finch MCP Server

| Server | Stars | Language | Tools | Auth | Transport |
|--------|-------|----------|-------|------|-----------|
| [awslabs/mcp — finch-mcp-server](https://github.com/awslabs/mcp/tree/main/src/finch-mcp-server) | ~8,900* | Python | 3 | AWS credentials | stdio |

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
| [microsoft/mcp](https://github.com/microsoft/mcp) | ~3,000 | C# | 2 ACR tools | Azure credentials | stdio, .mcpb |

**Azure Container Registry gets two read-only tools inside Microsoft's broader Azure MCP server.** 3,000 stars (up from 2,800), MIT, now covers 45+ Azure services with 230+ tools total. The Azure MCP Server is now also available as an **MCP Bundle (.mcpb)** (April 22, 2026) — install into Claude Desktop and other MCP-compatible clients with no runtime required. Azure MCP tools are also built into Visual Studio 2022 and 2026 natively.

ACR-specific tools:

| Tool | What it does |
|------|-------------|
| `azmcp-acr-registry-list` | List ACR registries in a subscription, optionally filtered by resource group |
| `azmcp-acr-registry-repository-list` | List repositories within an ACR registry |

Still **two tools, both read-only**. No image pushing, no tag management, no vulnerability scanning. This is enough for discovery ("What registries and images do we have?") but not for any registry management workflow. The .mcpb bundle format does lower setup friction significantly.

Available via NuGet, npm, Docker, or .mcpb bundle. All tools are designed to be non-destructive and idempotent — consistent with the overall Microsoft MCP server philosophy.

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

**Trivy's MCP plugin scans container images for vulnerabilities through natural language queries.** 37 stars, MIT, official Aqua Security project, 67 commits, v0.0.20 (December 2025). Installs as a Trivy plugin (`trivy plugin install mcp`, then `trivy mcp`). Supports VS Code, Cursor, JetBrains IDEs, and Claude Desktop. Optional Aqua Platform integration for enhanced scanning and policy compliance. Note: Trivy experienced a security incident in March 2026 (malicious v0.69.4 release, compromised GitHub Actions) — the main Trivy project is now at v0.70.0 with incident resolved.

While covered in our [Code Security MCP Servers review](/reviews/code-security-mcp-servers/), Trivy is relevant here because **container image scanning is a core registry workflow**. Ask "Are there any critical CVEs in nginx:1.25?" and Trivy scans the image layers. This complements registry management servers — one manages the images, the other tells you if they're safe.

Trivy is the most widely-used open source container security scanner (23k+ stars on the main repo), so having an MCP plugin matters for registry workflows that include security gates.

### OCI Registry (Universal — NEW)

| Server | Stars | Language | Tools | Auth | Transport |
|--------|-------|----------|-------|------|-----------|
| [StacklokLabs/ocireg-mcp](https://github.com/StacklokLabs/ocireg-mcp) | ~12 | Go | 4 | Multiple | SSE |

**The first universal container registry MCP server — works with any OCI-compliant registry.** 12 stars, Apache 2.0, 126 commits, v0.3.0 (March 26, 2026). This fills what was previously the biggest gap in this category.

4 tools:

| Tool | What it does |
|------|-------------|
| `get_image_info` | Retrieve image details: digest, size, architecture, OS, creation date, layer count |
| `list_tags` | Enumerate available tags for a repository |
| `get_image_manifest` | Fetch the OCI manifest for a container image |
| `get_image_config` | Obtain configuration data for a container image |

Supports **multiple authentication methods**: HTTP bearer tokens, environment variables, and Docker config file (`~/.docker/config.json`). Tested with Docker Hub and GitHub Container Registry (GHCR). Since it speaks the OCI Distribution API, it should work with any compliant registry — ECR, ACR, GCR, Harbor, Quay, and private registries.

Recommended deployment via [ToolHive](https://github.com/stacklok/toolhive) for container isolation, encrypted secret management, and network policies. This is a read-only tool — no image pushing or tag management, but it covers the most common "what images do we have and are they safe?" workflow across any registry.

**This is a significant development** — rather than building vendor-specific servers for each registry, one universal client that speaks OCI covers the common ground. Vendor-specific servers (Docker Hub, JFrog, etc.) still provide richer features like AI-powered search, vulnerability scanning, and lifecycle management.

### GHCR and Other Registries

**GitHub Container Registry (GHCR)**: No dedicated MCP server. GitHub's official [github-mcp-server](https://github.com/github/github-mcp-server) covers GitHub APIs broadly but doesn't expose GHCR-specific tools. The community [rideRTD/RTD-DevOps](https://github.com/rideRTD/RTD-DevOps) helper includes `ghcr_login_guide` and `ghcr_push` tools, but it's a small DevOps utility, not a GHCR management server.

**Quay.io**: No MCP server found. Red Hat's container registry lacks MCP integration.

**GitLab Container Registry**: No MCP server found. GitLab's broader MCP efforts don't yet cover their registry.

**DigitalOcean Container Registry**: No MCP server found.

## What's Missing

The container registry MCP ecosystem has narrowed its gaps since March, but several remain:

1. **Universal registry client exists but is read-only** — Stacklok's OCI Registry MCP server (ocireg-mcp) fills the biggest previous gap by working with any OCI-compliant registry. But it only supports read operations (4 tools). No universal client yet handles image pushing, tag management, or lifecycle operations.

2. **Image lifecycle management** — no server helps with tag retention policies, garbage collection, or automated cleanup of old images. This is one of the most common registry maintenance tasks.

3. **Multi-registry synchronization** — no server helps mirror or replicate images across registries. Organizations running hybrid cloud need this.

4. **SBOM and provenance** — with supply chain security becoming critical (see Trivy's March 2026 incident), no registry MCP server exposes SBOM data or image provenance (Sigstore/cosign signatures). JFrog's Xray integration is the closest.

5. **GHCR still uncovered** — Stacklok's OCI server works with GHCR for read operations, but there's no dedicated GHCR management server. GitHub's official MCP server still doesn't expose GHCR-specific tools.

## The Bottom Line

**Rating: 3.5 / 5** — The arrival of Stacklok's universal OCI registry server closes the biggest previous gap, and JFrog's shift to a hosted MCP server plus Universal MCP Registry signals enterprise maturation. AWS's monorepo nearly doubled in stars (4,700→8,900) and now offers hosted MCP server options. But Azure and GCP coverage remains minimal (2 read-only ACR tools, 6-star community GCP project), Harbor and Nexus community servers are dormant, and advanced workflows — lifecycle management, cross-registry sync, supply chain verification — still require manual tooling.

**Best for image discovery**: Docker Hub MCP (docker/hub-mcp) — AI-powered search across 100k+ images, one-click Docker Desktop setup.

**Best for artifact lifecycle**: JFrog MCP — the official hosted server (`jfrog-mcp-server`) for production, or the experimental `mcp-jfrog` (115 stars) for local development. 22+ tools covering repositories, builds, runtime monitoring, and vulnerability scanning.

**Best for AWS workflows**: ECS + Finch MCP servers — tight ECR integration with secure defaults (immutable tags, IAM role management). Hosted MCP server option now recommended.

**Best for cross-registry queries**: Stacklok OCI Registry MCP (ocireg-mcp) — 4 read-only tools that work with any OCI-compliant registry. The universal client this category needed.

**Best for self-hosted registries**: Harbor MCP (nomagicln/mcp-harbor) — 11 tools for projects, repositories, tags, and Helm charts. Or Sonatype MCP (brianveltman/sonatype-mcp) for Nexus.

The container registry MCP space continues maturing. The shift toward hosted/remote MCP servers (JFrog, AWS) and universal protocols (Stacklok's OCI client) points toward a more connected future, but advanced registry workflows still require manual tooling. The Trivy supply chain incident in March 2026 underscores why registry security tooling matters.

---

*ChatForest reviews MCP servers through research, documentation analysis, and community feedback. We do not run or test servers hands-on. Ratings reflect capability, maturity, and ecosystem fit based on available evidence. [About our methodology](/about/)*

*This review was last refreshed on 2026-04-25 using Claude Opus 4.6 (Anthropic).*
