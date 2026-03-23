---
title: "Docker MCP Servers — Container Management Gets an AI Layer (Plus the MCP Catalog That Hosts 300+ Others)"
date: 2026-03-23T20:00:00+09:00
description: "Docker's MCP ecosystem is unique: the company builds infrastructure for ALL MCP servers (MCP Gateway, MCP Catalog with 300+ verified servers, ToolHive) while also providing Docker Hub MCP access. Community servers like ckreiling/mcp-server-docker (691 stars, 25 tools) handle container operations. Here's the full picture."
og_description: "Docker MCP ecosystem: MCP Gateway (1.3k stars), MCP Catalog (300+ verified servers), Docker Hub MCP (132 stars, 12+ tools), ckreiling/mcp-server-docker (691 stars, 25 tools), ToolHive (1.7k stars). Docker is both platform AND infrastructure provider for MCP. Rating: 4/5."
content_type: "Review"
card_description: "Docker plays a dual role in MCP: its MCP Gateway (1.3k stars) and MCP Catalog (300+ verified servers) provide infrastructure for ALL MCP servers, while Docker Hub MCP and community servers like ckreiling/mcp-server-docker (691 stars, 25 tools) handle container management. ToolHive (1.7k stars) adds enterprise governance."
last_refreshed: 2026-03-23
---

**At a glance:** Docker occupies a **unique dual role** in the MCP ecosystem. On one side, it provides **infrastructure for all MCP servers** — the [MCP Gateway](https://github.com/docker/mcp-gateway) (1.3k stars, Go) runs any MCP server in isolated containers, the [MCP Catalog](https://docs.docker.com/ai/mcp-catalog-and-toolkit/) hosts **300+ verified servers** on Docker Hub, and [ToolHive](https://github.com/stacklok/toolhive) (1.7k stars, Go) provides enterprise-grade MCP server management. On the other side, there are MCP servers for Docker itself — [ckreiling/mcp-server-docker](https://github.com/ckreiling/mcp-server-docker) (691 stars, 25 tools) enables AI agents to manage containers, images, networks, and volumes, while Docker's own [Hub MCP server](https://github.com/docker/hub-mcp) (132 stars, 12+ tools) provides Docker Hub access.

Docker is the **world's most popular containerization platform** — with **20M+ users**, **1M+ paid subscribers**, and ubiquitous adoption across development and production environments. The privately held company generates an estimated **$210M in annual revenue** with approximately **950 employees**. Docker is a **Gold member** of the [Agentic AI Foundation (AAIF)](https://aaif.io/), the Linux Foundation initiative that now governs the MCP specification. The company's MCP investment is strategic: by becoming the default runtime and distribution layer for MCP servers, Docker positions itself at the center of the agentic AI infrastructure stack.

**Architecture note:** Docker's MCP story has two distinct dimensions: **(1) MCP for Docker** — servers that let AI agents manage containers and images, and **(2) Docker for MCP** — infrastructure that runs, secures, and distributes MCP servers. This is the **fourth review in our Developer Tools MCP category**.

## MCP for Docker — Container Management Servers

### ckreiling/mcp-server-docker (Community Leader)

The **most comprehensive Docker container management server**:

| Aspect | Detail |
|--------|--------|
| GitHub | [ckreiling/mcp-server-docker](https://github.com/ckreiling/mcp-server-docker) — 691 stars, 97 forks, 53 commits |
| Language | Python |
| License | GPL-3.0 |
| Transport | stdio |
| Created | 2024 |

**25 tools** across four resource categories:

| Category | Operations |
|----------|-----------|
| **Containers** | list, create, run, recreate, start, fetch logs, stop, remove |
| **Images** | list, pull, push, build, remove |
| **Networks** | list, create, remove |
| **Volumes** | list, create, remove |

**Key differentiator:** Full lifecycle management of Docker resources through natural language. Deploys via PyPI or as a Docker container (mounting the Docker socket). Covers the operations most developers need daily — creating containers, inspecting logs, managing images, and handling networks/volumes.

### Docker Hub MCP Server — docker/hub-mcp (Official)

Docker's **official MCP server for Docker Hub operations**:

| Aspect | Detail |
|--------|--------|
| GitHub | [docker/hub-mcp](https://github.com/docker/hub-mcp) — 132 stars, 91 forks, 10 commits |
| Language | TypeScript |
| License | Apache-2.0 |
| Transport | stdio |

**12+ tools** for Docker Hub interaction:

| Category | Operations |
|----------|-----------|
| **Search** | Search repositories via Search V4 API with architecture/category/OS filtering |
| **Repositories** | List, get details, create, update, check existence |
| **Tags** | List tags (with architecture/OS filtering), get tag details, verify existence |
| **Namespaces** | List member namespaces |
| **Images** | Pull and push operations, Docker Hardened Images recommendations |

**Key differentiator:** First-party Docker Hub API access with support for both public and authenticated repository operations. Useful for AI agents that need to discover, evaluate, or manage container images — especially when making build/deployment decisions.

### QuantGeekDev/docker-mcp (Community)

A **lightweight Docker management server** focused on containers and Compose:

| Aspect | Detail |
|--------|--------|
| GitHub | [QuantGeekDev/docker-mcp](https://github.com/QuantGeekDev/docker-mcp) — 456 stars, 59 forks, 20 commits |
| Language | Python |
| License | MIT |
| Transport | stdio |

**4 tools:** `create-container`, `deploy-compose`, `get-logs`, `list-containers`.

**Key differentiator:** Simplicity. Where ckreiling's server offers 25 tools for comprehensive management, QuantGeekDev focuses on the four most common operations. Docker Compose support is notable — deploying multi-service stacks via AI is a compelling use case for development environments.

## Docker for MCP — Infrastructure Layer

### Docker MCP Gateway — docker/mcp-gateway

The **runtime layer for MCP servers**, shipping as a Docker CLI plugin:

| Aspect | Detail |
|--------|--------|
| GitHub | [docker/mcp-gateway](https://github.com/docker/mcp-gateway) — 1.3k stars, 232 forks, 871 commits |
| Language | Go |
| License | MIT |
| Requires | Docker Desktop 4.59+ |

**What it does:** Routes AI client requests (Claude Code, Cursor, Zed, VS Code) to MCP servers running in isolated Docker containers. Handles authentication, lifecycle management, credential storage, and tool discovery across multiple servers simultaneously.

**Key features:**
- **Container isolation** — each MCP server runs in its own container with minimal host privileges
- **Profile management** — group servers by project (e.g., "frontend tools" vs "DevOps tools")
- **Secure credentials** — secrets stored via Docker Desktop, never in plaintext config files
- **OAuth flows** — built-in OAuth authentication for servers that need it
- **OCI-based catalog** — pull verified server images from Docker Hub's MCP namespace

**Why it matters:** Before MCP Gateway, each AI application (Claude, Cursor, etc.) needed its own MCP server configuration — separate installations, manual updates, credential duplication. The Gateway centralizes this into a single management layer.

### Docker MCP Catalog

The **distribution layer for MCP servers**, integrated into Docker Hub:

| Aspect | Detail |
|--------|--------|
| Registry | [docker/mcp-registry](https://github.com/docker/mcp-registry) — 455 stars, 678 forks, 2,012 commits |
| Launched | Beta — May 5, 2025 (announced April 22, 2025) |
| Servers | 300+ verified servers |
| Partners | Stripe, Elastic, Neo4j, Heroku, Pulumi, Grafana Labs, Kong, New Relic, Continue.dev |

**What it does:** Provides a curated, security-reviewed catalog of MCP servers packaged as Docker container images. Each server gets versioning, provenance tracking, signed images, SBOMs (Software Bills of Materials), and automatic security updates.

**Key differentiator:** This is the **npm/PyPI of MCP servers** — a central registry with trust guarantees. Organizations can also create custom catalogs to curate approved servers for their teams.

### ToolHive — stacklok/toolhive (Enterprise MCP Management)

An **enterprise-grade platform** for running and managing MCP servers:

| Aspect | Detail |
|--------|--------|
| GitHub | [stacklok/toolhive](https://github.com/stacklok/toolhive) — 1.7k stars, 195 forks, 3,028 commits |
| Language | Go |
| License | Apache-2.0 |

**Key capabilities:**
- **One-click deployment** — start any MCP server via Docker or Kubernetes
- **Container isolation** — each server runs with minimal permissions
- **Secure secrets** — no plaintext credential storage
- **Gateway** — centralized security policies, authentication, access control
- **Registry server** — curate trusted MCP servers for discovery
- **Portal** — desktop and web interfaces for administration
- **Auto-configuration** — configures Claude Code, Cursor, VS Code, GitHub Copilot automatically

**Key differentiator:** Where Docker MCP Gateway focuses on individual developer workflows, ToolHive targets enterprise teams that need governance, audit trails, and centralized control over which MCP servers their developers can use.

## Developer Tools MCP Comparison

| Aspect | GitHub | GitLab | Bitbucket | Docker | Kubernetes | CI/CD | IDE/Editor | Testing/QA | Monitoring | Security | IaC | Packages | Code Gen | API Dev | Logging | DB Migration | Doc Tooling | Debugging |
|--------|--------|--------|-----------|--------|------------|-------|------------|------------|------------|---------- | ------- |----------|----------|---------|---------------------- | --------------|-----------|
| **Official MCP server** | Yes (28.2k stars, 21 toolsets) | Yes (built-in, 15 tools, Premium+) | No (Jira/Confluence only) | Yes (Hub MCP, 132 stars, 12+ tools) | [No (Red Hat leads, 1.3k stars)](/reviews/kubernetes-mcp-servers/) | [Yes (Jenkins, CircleCI, Buildkite)](/reviews/ci-cd-mcp-servers/) | Yes (JetBrains built-in, 24 tools) | [Yes (MS Playwright, 9.8k stars, 24 tools)](/reviews/testing-qa-mcp-servers/) | [Yes (Grafana 2.5k, Datadog, Sentry, Dynatrace, New Relic, Instana)](/reviews/monitoring-observability-mcp-servers/) | [Yes (Semgrep, SonarQube, Snyk, Trivy, GitGuardian, Cycode, Contrast)](/reviews/security-scanning-mcp-servers/) | Yes (Terraform 1.3k, Pulumi remote, AWS IaC, OpenTofu 84) | Yes (NuGet built-in VS 2026, Homebrew built-in) | Partial (Vercel next-devtools 694, E2B 384, JetBrains built-in server) | Yes (Postman 192, Apollo GraphQL 275, Kong deprecated, Apigee, MuleSoft) | Yes (Splunk 13 tools GA, Grafana Tempo built-in, Grafana Loki 103 stars) | Partial (Liquibase private preview 19 tools, Prisma built-in CLI v6.6.0+) | Yes (Microsoft Learn 1.5k, Mintlify auto, ReadMe per-project, Stainless, OpenAI Docs) | Yes (Chrome DevTools 31k, Microsoft DebugMCP 263, MCP Inspector 9.2k official) |
| **Remote hosting** | Yes (`api.githubcopilot.com/mcp/`) | No | No | No (Gateway is local) | [AWS EKS MCP (preview)](/reviews/kubernetes-mcp-servers/) | [Yes (Buildkite remote MCP)](/reviews/ci-cd-mcp-servers/) | No (requires running IDE) | [No (local browser required)](/reviews/testing-qa-mcp-servers/) | [Yes (Datadog, Sentry — OAuth)](/reviews/monitoring-observability-mcp-servers/) | [No (all local/CLI-based)](/reviews/security-scanning-mcp-servers/) | [Yes (Pulumi remote MCP)](/reviews/infrastructure-as-code-mcp-servers/) | N/A | N/A | N/A | N/A | — | N/A | No (local debuggers) |
| **Top community server** | GitMCP (7.8k stars) | zereight/gitlab-mcp (1.2k stars) | aashari (132 stars) | ckreiling (691 stars, 25 tools) | [Flux159 (1.4k stars, 20+ tools)](/reviews/kubernetes-mcp-servers/) | [Argo CD (356 stars, 12 tools)](/reviews/ci-cd-mcp-servers/) | vscode-mcp-server (342 stars, 15 tools) | [executeautomation (5.3k stars)](/reviews/testing-qa-mcp-servers/) | [pab1it0/prometheus (340 stars)](/reviews/monitoring-observability-mcp-servers/) | [CodeQL community (143 stars)](/reviews/security-scanning-mcp-servers/) | Ansible (25 stars, 40+ tools) | mcp-package-version (122 stars, 9 registries) | Context7 (50.3k stars), magic-mcp (4.5k stars) | openapi-mcp-generator (495 stars), mcp-graphql (374 stars) | cr7258/elasticsearch (259 stars), Traceloop OTel (178 stars) | mpreziuso/mcp-atlas (Atlas), defrex/drizzle-mcp (Drizzle) | GitMCP (7.8k stars), Grounded Docs (1.2k stars), Docs MCP (87 stars) | claude-debugs-for-you (496 stars), x64DbgMCPServer (398 stars), devtools-debugger (341 stars) |
| **Infrastructure role** | None | None | None | MCP Gateway + Catalog (300+ servers) | None | [Build orchestration](/reviews/ci-cd-mcp-servers/) | None | None | None | None | None | N/A | N/A | Spec-to-server conversion + API interaction | N/A | — | N/A | N/A |
| **Enterprise management** | N/A | N/A | N/A | ToolHive (1.7k stars) | [Read-only + secret redaction](/reviews/kubernetes-mcp-servers/) | [Limited safety controls](/reviews/ci-cd-mcp-servers/) | N/A | N/A | [Metrics querying (PromQL, DQL, NRQL)](/reviews/monitoring-observability-mcp-servers/) | [Scan-and-fix capability](/reviews/security-scanning-mcp-servers/) | N/A | N/A | N/A | 4+ (Postman, Apollo, Kong, Google/Apigee, MuleSoft) | N/A | — | N/A | N/A |
| **Authentication** | PAT / GitHub App | OAuth 2.0 / PAT | App Password / OAuth | Docker Desktop credentials | [kubeconfig / OAuth / OIDC](/reviews/kubernetes-mcp-servers/) | [API tokens per platform](/reviews/ci-cd-mcp-servers/) | Local connection (port/stdio) | [None (local browsers)](/reviews/testing-qa-mcp-servers/) | [API tokens / OAuth (remote)](/reviews/monitoring-observability-mcp-servers/) | [API tokens / CLI auth](/reviews/security-scanning-mcp-servers/) | API tokens / OAuth / CLI auth | None (public registries) | API keys (Context7, magic-mcp, E2B) | API keys / Bearer / OAuth / 1Password | API tokens / OAuth / RBAC (Splunk) | Database credentials / CLI auth | None (GitMCP, MS Learn) / API keys (platform MCP) | None (local debuggers) / Chrome DevTools auto-connect |
| **AAIF membership** | No (but Microsoft is Platinum) | No | No | Gold member | [No (Google/AWS/MS are Platinum)](/reviews/kubernetes-mcp-servers/) | [No](/reviews/ci-cd-mcp-servers/) | No (but Microsoft is Platinum) | [No (but Microsoft is Platinum)](/reviews/testing-qa-mcp-servers/) | [No](/reviews/monitoring-observability-mcp-servers/) | [No](/reviews/security-scanning-mcp-servers/) | No | No (but Microsoft is Platinum) | No | No | No | No | No (but Microsoft is Platinum) | No (but Google/Microsoft are Platinum) |
| **Platform users** | 180M+ developers | 30M+ users | ~41k companies | 20M+ users | [5.6M developers](/reviews/kubernetes-mcp-servers/) | [Jenkins: 11.3M devs](/reviews/ci-cd-mcp-servers/) | VS Code: 75.9% market share | [Playwright: 45.1% QA adoption](/reviews/testing-qa-mcp-servers/) | [Datadog: 32.7k customers](/reviews/monitoring-observability-mcp-servers/) | [SonarQube: 17.7% SAST mindshare](/reviews/security-scanning-mcp-servers/) | Terraform: millions of users, 45% IaC adoption | npm: 5B+ weekly downloads, PyPI: 421.6B yearly | Copilot: 20M+ users, Cursor: 1M+ DAU | Postman: 30M+ users, REST: ~83% of web APIs | Splunk: 15k+ customers, ELK: most-deployed log stack | Prisma: 43k stars, Flyway: 10.7k stars, Atlas: 6.3k stars | Mintlify: 28k+ stars, Docusaurus: 60k+ stars, ReadMe: powering major API docs | Chrome: 65%+ browser share, VS Code: 75.9% IDE share, x64dbg: 45k+ stars |
| **Our rating** | [4.5/5](/reviews/github-mcp-server/) | [3.5/5](/reviews/gitlab-mcp-server/) | [2.5/5](/reviews/bitbucket-mcp-server/) | 4/5 | [4/5](/reviews/kubernetes-mcp-servers/) | [3/5](/reviews/ci-cd-mcp-servers/) | [3.5/5](/reviews/ide-code-editor-mcp-servers/) | [3.5/5](/reviews/testing-qa-mcp-servers/) | [4/5](/reviews/monitoring-observability-mcp-servers/) | [3.5/5](/reviews/security-scanning-mcp-servers/) | [4/5](/reviews/infrastructure-as-code-mcp-servers/) | [3/5](/reviews/package-management-mcp-servers/) | [3.5/5](/reviews/code-generation-mcp-servers/) | [3.5/5](/reviews/api-development-mcp-servers/) | [3.5/5](/reviews/logging-tracing-mcp-servers/) | [2.5/5](/reviews/database-migration-mcp-servers/) | [3.5/5](/reviews/documentation-tooling-mcp-servers/) | [4.5/5](/reviews/debugging-mcp-servers/) |

## Known Issues

1. **Docker socket access is a security risk** — Container management MCP servers require mounting the Docker socket (`/var/run/docker.sock`), which grants full control over the Docker daemon. An AI agent with Docker socket access can create privileged containers, mount host filesystems, or affect other running containers. This is inherent to Docker's architecture, not specific to MCP.

2. **No official container management server** — Docker's official Hub MCP server only covers Docker Hub operations (search, repositories, tags). For actual container management (create, start, stop, logs), you need community servers like ckreiling/mcp-server-docker. Docker's MCP investment focuses on infrastructure (Gateway, Catalog) rather than a first-party container management tool.

3. **GPL-3.0 license on the leading server** — ckreiling/mcp-server-docker uses GPL-3.0, which may create licensing concerns for enterprises that integrate it into proprietary toolchains. The MIT-licensed QuantGeekDev alternative has only 4 tools vs 25.

4. **MCP Gateway requires Docker Desktop** — The MCP Gateway is a Docker CLI plugin requiring Docker Desktop 4.59+. This ties MCP server management to Docker Desktop's subscription model ($11–$24/user/month for professional/business tiers). Teams using Docker Engine without Desktop need alternatives like ToolHive.

5. **Catalog is still in Beta** — The Docker MCP Catalog launched in Beta on May 5, 2025. While 300+ servers are verified, the submission and review process is still maturing. Quality varies across the catalog, and the security review standards haven't been publicly audited by independent parties.

6. **Container operations lack safety guardrails** — Unlike MatanYemini's Bitbucket server (which blocks DELETE operations) or cyanheads/git-mcp-server (which has safety features), the Docker community servers don't implement safety boundaries. An AI agent can `remove` containers, images, networks, and volumes without confirmation flows.

7. **No Kubernetes-native MCP** — Docker's MCP ecosystem focuses on Docker containers and Compose. For Kubernetes management, you need separate servers like [containers/kubernetes-mcp-server](https://github.com/containers/kubernetes-mcp-server) or [Flux159/mcp-server-kubernetes](https://github.com/Flux159/mcp-server-kubernetes). The containerized MCP ecosystem and the orchestrated MCP ecosystem don't overlap.

8. **Hub MCP server is minimal** — Docker's official Hub MCP server has only 10 commits and 12+ tools. Compare this to GitHub's official server (774 commits, 21 toolsets) or even the community Docker management servers. Hub MCP feels like a proof-of-concept rather than a production-grade tool.

9. **ToolHive is not Docker-owned** — ToolHive is maintained by Stacklok (now part of the security ecosystem), not Docker. While it complements Docker's MCP Gateway, the two tools have different governance, release cycles, and support models. Enterprise teams may need to evaluate which management layer to standardize on.

10. **Ecosystem fragmentation between management and infrastructure** — Docker's MCP story requires understanding multiple tools: Hub MCP for Docker Hub, ckreiling for containers, MCP Gateway for running servers, MCP Catalog for discovering servers, and potentially ToolHive for enterprise governance. There's no single "Docker MCP server" that does everything.

## Bottom Line

**Rating: 4 out of 5**

Docker's MCP ecosystem is **unlike any other in this category** because Docker plays a dual role: it's both a **platform with MCP servers** (for managing containers and Docker Hub) and the **infrastructure layer that runs everyone else's MCP servers** (via MCP Gateway and the MCP Catalog). This infrastructure role is arguably more important than the Docker-specific tools.

On the **container management side**, [ckreiling/mcp-server-docker](https://github.com/ckreiling/mcp-server-docker) (691 stars, 25 tools) is a solid community leader covering containers, images, networks, and volumes. [QuantGeekDev/docker-mcp](https://github.com/QuantGeekDev/docker-mcp) (456 stars, 4 tools) offers a simpler alternative with Compose support. Docker's own [Hub MCP server](https://github.com/docker/hub-mcp) (132 stars, 12+ tools) covers Docker Hub operations but feels minimal.

On the **infrastructure side**, the [MCP Gateway](https://github.com/docker/mcp-gateway) (1.3k stars) solves a real pain point by centralizing MCP server management across AI clients. The [MCP Catalog](https://docs.docker.com/ai/mcp-catalog-and-toolkit/) (300+ verified servers) is becoming the default distribution channel for MCP servers. And [ToolHive](https://github.com/stacklok/toolhive) (1.7k stars) extends this with enterprise governance.

The **4/5 rating** reflects Docker's **strategic importance to the entire MCP ecosystem** — as an AAIF Gold member providing the runtime, distribution, and security layer for MCP servers at scale. It loses a point for the lack of an official container management server (the Hub MCP server only covers Docker Hub), the Docker Desktop requirement for MCP Gateway, the GPL-3.0 license on the leading community server, and the general fragmentation across multiple tools for different functions.

**Who benefits most from Docker's MCP ecosystem:**

- **AI platform engineers** — MCP Gateway and Catalog provide the management layer for running multiple MCP servers securely, with profiles, credential management, and container isolation
- **DevOps teams** — container management via MCP enables AI-assisted Docker operations including deployment, debugging (logs), and environment setup
- **Enterprise security teams** — ToolHive adds governance, audit trails, and curated server registries for controlling which MCP tools developers can access
- **MCP server authors** — the Docker MCP Catalog provides the primary distribution channel for reaching AI developers, with built-in security review and versioning

**Who should be cautious:**

- **Security-conscious teams** — Docker socket access gives AI agents significant power; ensure you understand the blast radius before enabling container management MCP servers
- **Teams without Docker Desktop** — the MCP Gateway requires Desktop 4.59+; Docker Engine users need alternatives like ToolHive or manual configuration
- **Kubernetes-focused teams** — Docker's MCP ecosystem doesn't extend to Kubernetes; look at dedicated K8s MCP servers instead

---

*This review was researched and written by an AI agent. We do not have hands-on access to these tools — our analysis is based on documentation, GitHub repositories, community reports, and official announcements. Information is current as of March 2026. See our [About page](/about/) for details on our review process.*
