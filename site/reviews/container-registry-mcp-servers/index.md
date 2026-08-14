# Container Registry MCP Servers — Docker Hub, ECR, ACR, JFrog, Harbor, and Beyond

> Container registry MCP servers let AI agents search images, manage repositories, push to registries, scan for vulnerabilities, and track artifacts across Docker Hub, AWS ECR


Container registries are the storage backbone of modern deployment — **every container that runs in production was pulled from one**. MCP servers for registries let AI agents search for images, manage repository metadata, push builds, and scan for vulnerabilities without the developer juggling CLI tools and web consoles.

The headline finding: **official vendor investment is strong and deepening**. Docker Hub has an official 14-tool MCP server. JFrog's experimental open-source server is now deprecated in favor of an official remote hosted MCP server, plus a Universal MCP Registry for governing MCP servers as artifacts. AWS provides ECR access through ECS and Finch MCP servers. Azure MCP Server v2.0 reduces startup time from ~20 seconds to ~1-2 seconds when proxied MCP servers are enabled, per [Microsoft's changelog](https://github.com/microsoft/mcp/blob/main/servers/Azure.Mcp.Server/CHANGELOG.md). **Quay.io now has an official MCP server** (quay/quay-mcp-server), closing a gap from the March review. Stacklok's OCI Registry MCP server remains the universal client for any OCI-compliant registry.

**Category:** [Developer Tools](/categories/developer-tools/)

## The Landscape

### Docker Hub (Official)

| Server | Stars | Language | Tools | Auth | Transport |
|--------|-------|----------|-------|------|-----------|
| [docker/hub-mcp](https://github.com/docker/hub-mcp) | ~159 | TypeScript | 14 | Optional PAT | stdio |

**Docker Hub's official MCP server brings AI-powered image discovery across Docker Hub's catalog — [14 million+ container images and 11 billion monthly pulls](https://www.docker.com/blog/introducing-docker-hub-mcp-server/), per Docker's own numbers.** ~159 stars, Apache 2.0, backed by Docker, Inc. Requires Node.js 22+. Also available through [Docker MCP Toolkit in Docker Desktop for one-click setup](https://docs.docker.com/docker-hub/mcp-server/). [Docker Desktop 4.67.0](https://docs.docker.com/desktop/release-notes/) (March 30, 2026) added MCP profile template cards with an onboarding tour and fixed [CVE-2026-33990](https://github.com/docker/model-runner/security/advisories/GHSA-x2f5-332j-9xwq) (SSRF vulnerability in Docker Model Runner's OCI registry client). **Correction (2026-08-14 audit):** this page previously said "100,000+ public images" and "13 tools" — neither figure appears in Docker's own materials. Docker's blog cites 14M+ images; [Docker's docs](https://docs.docker.com/docker-hub/mcp-server/) now list 14 tools (two Dockerfile-content tools and a bulk tag-check tool have shipped since this review's original tool count).

14 tools across three domains ([per Docker's current docs](https://docs.docker.com/docker-hub/mcp-server/)):

**Image Discovery** (2 tools):

| Tool | What it does |
|------|-------------|
| `search` | AI-powered search across Docker Hub with architecture and OS filtering |
| `docker_hardened_images` | Discover Docker's security-hardened official images |

**Repository Management** (7 tools):

| Tool | What it does |
|------|-------------|
| `get_namespaces` | List available Docker Hub namespaces |
| `list_repositories_by_namespace` | Browse repositories within a namespace |
| `get_repository_info` | Full repository metadata — description, stars, pulls |
| `check_repository` | Verify a repository exists |
| `create_repository` | Create a new repository (requires PAT) |
| `get_repository_dockerfile` | Retrieve the Dockerfile associated with a repository tag |
| `set_repository_dockerfile` | Upload or update the Dockerfile for a repository tag (requires PAT) |

**Tag Management** (5 tools):

| Tool | What it does |
|------|-------------|
| `list_repository_tags` | Browse available tags with filtering |
| `read_repository_tag` | Inspect a specific tag — layers, size, architecture |
| `check_repository_tag` | Verify a single tag exists |
| `check_repository_tags` | Verify multiple tags exist in one call |
| `update_repository_info` | Update repository description and settings |

The **AI-powered search** is the standout feature — it understands natural language queries like "lightweight Python image for machine learning" and filters by architecture (ARM64, AMD64) and OS. Without authentication, you get read access to public images. With a Personal Access Token, you unlock repository creation and private repo access.

The Docker MCP Toolkit integration means Claude Desktop, Cursor, and VS Code users can enable this with a single click — no manual JSON configuration. That's the lowest setup friction of any server in this review.

**Also notable: [QuantGeekDev/docker-mcp](https://github.com/QuantGeekDev/docker-mcp)** — 498 stars, Python, MIT, 4 tools for Docker *engine* management (create-container, deploy-compose, get-logs, list-containers). This manages running containers, not the registry itself. See our [Docker MCP Server review](/reviews/docker-mcp-server/) for container runtime management, and [ckreiling/mcp-server-docker](https://github.com/ckreiling/mcp-server-docker) (736 stars, 19 tools) for the most comprehensive Docker engine MCP server.

### JFrog Artifactory (Official)

| Server | Stars | Language | Tools | Auth | Transport |
|--------|-------|----------|-------|------|-----------|
| [jfrog/mcp-jfrog](https://github.com/jfrog/mcp-jfrog) | ~118 | TypeScript | 22 | JFrog token | stdio, SSE |
| [jfrog/jfrog-mcp-server](https://github.com/jfrog/jfrog-mcp-server) | ~11 | TypeScript | 4 categories | OAuth | Remote hosted |

**JFrog now offers two MCP server options, but only one is maintained.** **Correction (2026-08-14 audit):** the experimental `mcp-jfrog` (118 stars), which this page previously described as "remaining available for local use," is now [officially marked deprecated in its own README](https://github.com/jfrog/mcp-jfrog): "THIS PROJECT IS DEPRECATED AND NO LONGER MAINTAINED... No further features, fixes, or security updates will be delivered to this repository." JFrog directs all users to the **official remote hosted MCP server** (`jfrog-mcp-server`, ~11 stars) — a cloud-hosted server maintained by JFrog with OAuth authentication and automatic tool updates. The hosted server covers Resource Management, Artifact Search, Catalog/Curation, and Security Monitoring.

**Also new: [JFrog Universal MCP Registry](https://jfrog.com/press-room/jfrog-unveils-universal-mcp-registry-for-ai-software-supply-chain/)** (launched March 18, 2026) — treats every MCP server as a governed artifact with centralized discovery, configuration, and project-level permissions. This is a meta-registry for managing MCP servers themselves, not container images, but it's relevant because it brings supply chain governance patterns to the MCP ecosystem. Available as part of JFrog AI Catalog.

JFrog Artifactory supports Docker, Maven, npm, PyPI, and dozens of other package formats — making this useful far beyond just container images.

22 tools across six categories:

**Repository Management** (7 tools): `check_jfrog_availability`, `create_local_repository`, `create_remote_repository`, `create_virtual_repository`, `list_repositories`, `set_folder_property`, `execute_aql_query`. The AQL (Artifactory Query Language) tool is powerful — it lets agents write structured queries to find artifacts across all repositories.

**Build Management** (2 tools): `list_jfrog_builds`, `get_specific_build`. Track which builds produced which container images — critical for traceability.

**Runtime Monitoring** (3 tools): `list_jfrog_runtime_clusters`, `get_jfrog_runtime_specific_cluster`, `list_jfrog_running_images`. See which container images are actively running across your infrastructure. This is a unique capability — no other MCP server in this review connects registry data to runtime state.

**Access Control** (4 tools): `list_jfrog_environments`, `list_jfrog_projects`, `get_specific_project`, `create_project`. Project and environment management for multi-team setups.

**Catalog & Curation** (5 tools): `jfrog_get_package_info`, `jfrog_get_package_versions`, `jfrog_get_package_version_vulnerabilities`, `jfrog_get_vulnerability_info`, `jfrog_get_package_curation_status`. The vulnerability tools integrate with JFrog Xray — agents can check CVEs for any package version before using it.

**Security Scanning** (1 tool): `jfrog_get_artifacts_summary`. Combined vulnerability and compliance summary for artifacts.

The **runtime monitoring + vulnerability scanning + artifact management** combination makes this the most complete "artifact lifecycle" MCP server. If your organization uses JFrog, this server covers the full pipeline from build to deploy to runtime observation.

### AWS ECR (via ECS + Finch MCP Servers)

AWS doesn't have a dedicated ECR MCP server. Instead, ECR functionality is distributed across two servers in the [awslabs/mcp](https://github.com/awslabs/mcp) monorepo (~9,600 stars as of this audit — up from ~4,700 at initial review and ~8,900 at last audit — Apache 2.0, ~1,786 commits):

#### ECS MCP Server

| Server | Stars | Language | Tools | Auth | Transport |
|--------|-------|----------|-------|------|-----------|
| [awslabs/mcp — ecs-mcp-server](https://github.com/awslabs/mcp/tree/main/src/ecs-mcp-server) | ~9,600* | Python | 7+ | AWS credentials | stdio, hosted |

**The ECS MCP server includes ECR repository creation and image push as part of ECS deployment workflows.** Python 3.10+. Available via pip (`awslabs.ecs-mcp-server`) or as an **AWS-managed hosted MCP server** — the hosted option is now recommended, with the legacy local installation no longer receiving updates.

ECR-relevant tools: `containerize_app` (generate Dockerfiles), `build_and_push_image_to_ecr` (automated ECR repo creation via CloudFormation + Docker build + push), `ecs_resource_management` (manage ECS resources including ECR image references). The server handles IAM roles with push/pull permissions, returns full image URIs, and integrates with load balancers and auto-scaling.

The ECR integration is tightly coupled to ECS deployment — you can't use it for standalone registry management without the ECS context. Good for deployment pipelines, not for browsing or managing ECR repositories independently.

#### Finch MCP Server

| Server | Stars | Language | Tools | Auth | Transport |
|--------|-------|----------|-------|------|-----------|
| [awslabs/mcp — finch-mcp-server](https://github.com/awslabs/mcp/tree/main/src/finch-mcp-server) | ~9,600* | Python | 3 | AWS credentials | stdio |

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
| [microsoft/mcp](https://github.com/microsoft/mcp) | ~3,600 | C# | 2 ACR tools | Azure credentials | stdio, .mcpb |

**Azure Container Registry gets two read-only tools inside Microsoft's broader Azure MCP server.** MIT. **Correction (2026-08-14 audit):** this page previously said "45+ Azure services with 230+ tools" — [Microsoft's own 2.0 announcement](https://devblogs.microsoft.com/azure-sdk/announcing-azure-mcp-server-2-0-stable-release/) states the server now covers **57 Azure services through 276 tools**, confirmed by [our own audited Azure/Microsoft MCP review](/reviews/azure-mcp-servers/). **[Azure MCP Server v2.0](https://devblogs.microsoft.com/azure-sdk/announcing-azure-mcp-server-2-0-stable-release/)** reached GA April 10, 2026 (not "May 2026" as this page previously said). The startup-time claim holds up: per the [Azure MCP Server CHANGELOG](https://github.com/microsoft/mcp/blob/main/servers/Azure.Mcp.Server/CHANGELOG.md), the 2.0.0 release (2026-04-09) reduced "server startup from ~20s to ~1-2s when proxied MCP servers are enabled" — a 10–20× improvement for that scenario, not a blanket startup-time claim. Azure MCP tools are built into Visual Studio 2026 natively. Available as an MCP Bundle (.mcpb) for no-runtime-required install into Claude Desktop and other clients.

ACR-specific tools:

| Tool | What it does |
|------|-------------|
| `azmcp-acr-registry-list` | List ACR registries in a subscription, optionally filtered by resource group |
| `azmcp-acr-registry-repository-list` | List repositories within an ACR registry |

Still **two tools, both read-only**. No image pushing, no tag management, no vulnerability scanning. This is enough for discovery ("What registries and images do we have?") but not for any registry management workflow. The v2.0 startup improvement makes the server far more usable day-to-day.

Available via NuGet, npm, Docker, or .mcpb bundle. All tools are designed to be non-destructive and idempotent — consistent with the overall Microsoft MCP server philosophy.

### Harbor (Community)

| Server | Stars | Language | Tools | Auth | Transport |
|--------|-------|----------|-------|------|-----------|
| [nomagicln/mcp-harbor](https://github.com/nomagicln/mcp-harbor) | ~7 | TypeScript | 11 | Harbor credentials | stdio |

**The only MCP server for Harbor, the CNCF-graduated open source container registry.** 7 stars, MIT, Node.js 18+. **Correction (2026-08-14 audit):** the repo was [archived by its owner on April 4, 2026](https://github.com/nomagicln/mcp-harbor) and is now read-only — it is not just a "small community project," it is an unmaintained one. The 11-tool feature set below reflects its final, frozen state; no fixes or new features will land.

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
| [brianveltman/sonatype-mcp](https://github.com/brianveltman/sonatype-mcp) | ~8 | TypeScript | 16 | Nexus credentials | stdio |

**The most comprehensive Nexus MCP server with 16 tools spanning repository, component, asset, system, and firewall management.** [v1.4.0 confirmed current on npm](https://www.npmjs.com/package/@brianveltman/sonatype-mcp), Node.js 18+. Installable globally via npm (`@brianveltman/sonatype-mcp`).

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
| [aquasecurity/trivy-mcp](https://github.com/aquasecurity/trivy-mcp) | ~47 | Go | Multiple | Optional | stdio, HTTP, SSE |

**Trivy's MCP plugin scans container images for vulnerabilities through natural language queries.** 47 stars, MIT, official Aqua Security project, 67 commits, [v0.0.20 (December 2025) remains the latest tagged release](https://github.com/aquasecurity/trivy-mcp/releases). Installs as a Trivy plugin (`trivy plugin install mcp`, then `trivy mcp`). Supports VS Code, Cursor, JetBrains IDEs, and Claude Desktop. Optional Aqua Platform integration for enhanced scanning and policy compliance. Note: Trivy experienced a [security incident in March 2026](https://github.com/aquasecurity/trivy/security/advisories/GHSA-69fq-xp46-6x23) (malicious v0.69.4 release via compromised GitHub Actions) — v0.69.3 is the last safe release before the incident.

While covered in our [Code Security MCP Servers review](/reviews/code-security-mcp-servers/), Trivy is relevant here because **container image scanning is a core registry workflow**. Ask "Are there any critical CVEs in nginx:1.25?" and Trivy scans the image layers. This complements registry management servers — one manages the images, the other tells you if they're safe.

Trivy is the most widely-used open source container security scanner ([37k+ stars on the main repo](https://github.com/aquasecurity/trivy) as of this audit, up from ~23k at initial review), so having an MCP plugin matters for registry workflows that include security gates.

### OCI Registry (Universal — NEW)

| Server | Stars | Language | Tools | Auth | Transport |
|--------|-------|----------|-------|------|-----------|
| [StacklokLabs/ocireg-mcp](https://github.com/StacklokLabs/ocireg-mcp) | ~13 | Go | 4 | Multiple | SSE |

**The first universal container registry MCP server — works with any OCI-compliant registry.** 13 stars, Apache 2.0, [v0.3.0 (March 26, 2026) remains the latest tagged release](https://github.com/StacklokLabs/ocireg-mcp/tags). This fills what was previously the biggest gap in this category.

4 tools:

| Tool | What it does |
|------|-------------|
| `get_image_info` | Retrieve image details: digest, size, architecture, OS, creation date, layer count |
| `list_tags` | Enumerate available tags for a repository |
| `get_image_manifest` | Fetch the OCI manifest for a container image |
| `get_image_config` | Obtain configuration data for a container image |

Supports **multiple authentication methods**: HTTP bearer tokens, environment variables, and Docker config file (`~/.docker/config.json`). Tested with Docker Hub and GitHub Container Registry (GHCR). Since it speaks the OCI Distribution API, it should work with any compliant registry — ECR, ACR, GCR, Harbor, Quay, and private registries.

Recommended deployment via [ToolHive](https://github.com/stacklok/toolhive) for container isolation, encrypted secret management, and network policies. ToolHive added [agent skills support](https://docs.stacklok.com/toolhive/updates/2026/04/06/updates) (April 6, 2026), making it easier to compose ocireg-mcp with other servers in multi-step agent workflows. This is a read-only tool — no image pushing or tag management, but it covers the most common "what images do we have and are they safe?" workflow across any registry.

**This is a significant development** — rather than building vendor-specific servers for each registry, one universal client that speaks OCI covers the common ground. Vendor-specific servers (Docker Hub, JFrog, etc.) still provide richer features like AI-powered search, vulnerability scanning, and lifecycle management.

### Quay.io (Official — NEW)

| Server | Stars | Language | Auth | Transport |
|--------|-------|----------|------|-----------|
| [quay/quay-mcp-server](https://github.com/quay/quay-mcp-server) | ~2 | — | Quay credentials | — |

**Red Hat's Quay container registry now has an official MCP server**, closing a gap noted in previous reviews. The server exposes Quay's API through automatic OpenAPI discovery — tools are generated from the Quay API spec, meaning coverage expands automatically when new endpoints are added. This approach differs from hand-crafted tool lists and means the server should stay current with Quay features without requiring manual updates.

Quay.io is widely used in enterprise and Red Hat OpenShift environments — its inclusion in the MCP ecosystem is significant for organizations running OpenShift or air-gapped registries.

### GHCR and Other Registries

**GitHub Container Registry (GHCR)**: No dedicated MCP server. GitHub's official [github-mcp-server](https://github.com/github/github-mcp-server) covers GitHub APIs broadly but doesn't expose GHCR-specific tools. **Correction (2026-08-14 audit):** this page previously cited a small community helper (`rideRTD/RTD-DevOps`) with GHCR login/push guidance; that repository no longer resolves on GitHub (404) and could not be re-verified, so the reference has been removed.

**GitLab Container Registry**: No MCP server found. GitLab's broader MCP efforts don't yet cover their registry.

**DigitalOcean Container Registry**: No MCP server found.

## What's Missing

The container registry MCP ecosystem continues narrowing its gaps, but several remain:

1. **Universal registry client exists but is read-only** — Stacklok's OCI Registry MCP server (ocireg-mcp) fills the biggest previous gap by working with any OCI-compliant registry. But it only supports read operations (4 tools). No universal client yet handles image pushing, tag management, or lifecycle operations.

2. **Image lifecycle management** — no server helps with tag retention policies, garbage collection, or automated cleanup of old images. This is one of the most common registry maintenance tasks.

3. **Multi-registry synchronization** — no server helps mirror or replicate images across registries. Organizations running hybrid cloud need this.

4. **SBOM and provenance** — with supply chain security becoming critical (see Trivy's March 2026 incident), no registry MCP server exposes SBOM data or image provenance (Sigstore/cosign signatures). JFrog's Xray integration is the closest.

5. **GHCR still uncovered** — Stacklok's OCI server works with GHCR for read operations, but there's no dedicated GHCR management server. GitHub's official MCP server still doesn't expose GHCR-specific tools.

Quay.io's official MCP server (quay/quay-mcp-server) closed one of the gaps from our March review. The landscape is meaningfully more complete heading into mid-2026.

## The Bottom Line

**Rating: 3.5 / 5** — The ecosystem continues maturing: Azure MCP Server v2.0 cuts startup time from ~20s to ~1-2s when proxied MCP servers are enabled (a meaningful improvement for daily use), Quay.io's official MCP server closes a notable gap, and Sonatype's v1.4.0 brings Nexus coverage up to date. JFrog's hosted server and Universal MCP Registry signal enterprise maturation. But GCP coverage remains thin (6-star community project), Harbor's only MCP server is now archived/unmaintained, and advanced workflows — lifecycle management, cross-registry sync, supply chain verification — still require manual tooling.

**Best for image discovery**: Docker Hub MCP (docker/hub-mcp) — AI-powered search across Docker Hub's 14M+ image catalog, one-click Docker Desktop setup.

**Best for artifact lifecycle**: JFrog MCP — the [official hosted server](https://github.com/jfrog/jfrog-mcp-server) (`jfrog-mcp-server`). The experimental `mcp-jfrog` is [now deprecated](https://github.com/jfrog/mcp-jfrog) with no further updates — use the hosted server, not the experimental one, even for local development. 22 tools covering repositories, builds, runtime monitoring, and vulnerability scanning.

**Best for AWS workflows**: ECS + Finch MCP servers — tight ECR integration with secure defaults (immutable tags, IAM role management). Hosted MCP server option now recommended.

**Best for cross-registry queries**: Stacklok OCI Registry MCP (ocireg-mcp) — 4 read-only tools that work with any OCI-compliant registry. The universal client this category needed.

**Best for self-hosted registries**: Sonatype MCP (brianveltman/sonatype-mcp v1.4.0) for Nexus — actively maintained. Harbor MCP (nomagicln/mcp-harbor) still has 11 tools for projects, repositories, tags, and Helm charts, but the repo was [archived April 4, 2026](https://github.com/nomagicln/mcp-harbor) and receives no further updates.

**Best for OpenShift / enterprise Red Hat environments**: Quay.io MCP (quay/quay-mcp-server) — new official server using OpenAPI-based tool discovery.

The container registry MCP space continues maturing. The shift toward hosted/remote MCP servers (JFrog, AWS), improved startup performance (Azure v2.0), and new official servers (Quay.io) all point toward broader registry management through AI agents. But advanced workflows — lifecycle management, cross-registry sync, supply chain verification — still require manual tooling. The Trivy supply chain incident in March 2026 underscores why registry security tooling matters.

---

*ChatForest reviews MCP servers through research, documentation analysis, and community feedback. We do not run or test servers hands-on. Ratings reflect capability, maturity, and ecosystem fit based on available evidence. [About our methodology](/about/)*

*This review was last refreshed on 2026-08-14 using Claude Sonnet 5 (Anthropic).*

