# Docker MCP Servers — Container Management Gets an AI Layer (Plus the MCP Catalog That Hosts 300+ Others)

> Docker's MCP ecosystem is unique: the company builds infrastructure for ALL MCP servers (MCP Gateway, MCP Catalog with 300+ verified servers, ToolHive) while also providing Docker Hub MCP access.


**At a glance:** Docker occupies a **unique dual role** in the MCP ecosystem. On one side, it provides **infrastructure for all MCP servers** — the [MCP Gateway](https://github.com/docker/mcp-gateway) (1.4k stars, Go) runs any MCP server in isolated containers with new **Dynamic MCP discovery** (agents find and add servers at runtime via `mcp-find`/`mcp-add`), the [MCP Catalog](https://docs.docker.com/ai/mcp-catalog-and-toolkit/) hosts **300+ verified servers** on Docker Hub (registry now at 3,006 commits), and [ToolHive](https://github.com/stacklok/toolhive) (1.8k stars, Go, v0.26.0) has **surged with 13 releases in two weeks** — adding Agent Skills, MCP Apps, Cedar authorization, CRD graduation to v1beta1, and Kubernetes horizontal scaling. On the other side, there are MCP servers for Docker itself — [ckreiling/mcp-server-docker](https://github.com/ckreiling/mcp-server-docker) (707 stars, 25 tools) enables AI agents to manage containers, images, networks, and volumes, while Docker's own [Hub MCP server](https://github.com/docker/hub-mcp) (141 stars, 12+ tools) provides Docker Hub access.

Docker is the **world's most popular containerization platform** — with **20M+ users**, **1M+ paid subscribers**, and ubiquitous adoption across development and production environments. The privately held company generates an estimated **$210M in annual revenue** with approximately **950 employees**. Docker is a **Gold member** of the [Agentic AI Foundation (AAIF)](https://aaif.io/), the Linux Foundation initiative that now governs the MCP specification. The company's MCP investment is strategic: by becoming the default runtime and distribution layer for MCP servers, Docker positions itself at the center of the agentic AI infrastructure stack.

**Architecture note:** Docker's MCP story has two distinct dimensions: **(1) MCP for Docker** — servers that let AI agents manage containers and images, and **(2) Docker for MCP** — infrastructure that runs, secures, and distributes MCP servers. This is the **fourth review in our Developer Tools MCP category**. Part of our **[Cloud & Infrastructure MCP category](/categories/cloud-infrastructure/)**.

## MCP for Docker — Container Management Servers

### ckreiling/mcp-server-docker (Community Leader)

The **most comprehensive Docker container management server**:

| Aspect | Detail |
|--------|--------|
| GitHub | [ckreiling/mcp-server-docker](https://github.com/ckreiling/mcp-server-docker) — 707 stars, 98 forks, 53 commits |
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

**Key differentiator:** Full lifecycle management of Docker resources through natural language. Deploys via PyPI or as a Docker container (mounting the Docker socket). Covers the operations most developers need daily — creating containers, inspecting logs, managing images, and handling networks/volumes. **Note:** The project has been dormant since early 2026 — still at 53 commits with no published releases, though star growth continues organically.

### Docker Hub MCP Server — docker/hub-mcp (Official)

Docker's **official MCP server for Docker Hub operations**:

| Aspect | Detail |
|--------|--------|
| GitHub | [docker/hub-mcp](https://github.com/docker/hub-mcp) — 141 stars, 95 forks, 11 commits |
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
| GitHub | [QuantGeekDev/docker-mcp](https://github.com/QuantGeekDev/docker-mcp) — 475 stars, 57 forks, 20 commits |
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
| GitHub | [docker/mcp-gateway](https://github.com/docker/mcp-gateway) — 1.4k stars, 241 forks, 917 commits |
| Language | Go |
| License | MIT |
| Requires | Docker Desktop 4.59+ |

**What it does:** Routes AI client requests (Claude Code, Cursor, Zed, VS Code) to MCP servers running in isolated Docker containers. Handles authentication, lifecycle management, credential storage, and tool discovery across multiple servers simultaneously.

**Key features:**
- **Container isolation** — each MCP server runs in its own container with minimal host privileges
- **Profile management** — group servers by project (e.g., "frontend tools" vs "DevOps tools"), with new **MCP Profile Templates** (Docker Desktop 4.67+) that let developers bootstrap profiles from predefined server collections
- **Dynamic MCP discovery** — NEW: `mcp-find`, `mcp-add`, and `mcp-remove` tools let AI agents search the catalog, add servers, and handle authentication at runtime without manual configuration or restarts
- **Secure credentials** — secrets stored via Docker Desktop, never in plaintext config files
- **OAuth flows** — built-in OAuth authentication with dynamic OAuth discovery for community servers (v0.40.1+)
- **OCI-based catalog** — pull verified server images from Docker Hub's MCP namespace

**Why it matters:** Before MCP Gateway, each AI application (Claude, Cursor, etc.) needed its own MCP server configuration — separate installations, manual updates, credential duplication. The Gateway centralizes this into a single management layer. The new Dynamic MCP discovery takes this further — agents can now self-configure by searching and adding MCP servers from the catalog during a conversation.

### Docker MCP Catalog

The **distribution layer for MCP servers**, integrated into Docker Hub:

| Aspect | Detail |
|--------|--------|
| Registry | [docker/mcp-registry](https://github.com/docker/mcp-registry) — 479 stars, 759 forks, 3,006 commits |
| Launched | Beta — May 5, 2025 (announced April 22, 2025) |
| Servers | 300+ verified servers |
| Partners | Stripe, Elastic, Neo4j, Heroku, Pulumi, Grafana Labs, Kong, New Relic, Continue.dev |

**What it does:** Provides a curated, security-reviewed catalog of MCP servers packaged as Docker container images. Each server gets versioning, provenance tracking, signed images, SBOMs (Software Bills of Materials), and automatic security updates.

**Key differentiator:** This is the **npm/PyPI of MCP servers** — a central registry with trust guarantees. The registry has seen **massive contribution activity** — jumping from 2,012 to 3,006 commits (+994) and 678 to 759 forks in 37 days, reflecting rapid community growth. Organizations can also create custom catalogs to curate approved servers for their teams. E2B sandboxes now include direct Docker MCP Catalog access.

### ToolHive — stacklok/toolhive (Enterprise MCP Management)

An **enterprise-grade platform** for running and managing MCP servers:

| Aspect | Detail |
|--------|--------|
| GitHub | [stacklok/toolhive](https://github.com/stacklok/toolhive) — 1.8k stars, 209 forks, 3,495 commits |
| Language | Go |
| License | Apache-2.0 |
| Latest | v0.26.0 (April 29, 2026) — 13 releases in 2 weeks |

**Key capabilities:**
- **One-click deployment** — start any MCP server via Docker or Kubernetes
- **Container isolation** — each server runs with minimal permissions
- **Secure secrets** — no plaintext credential storage
- **Gateway** — centralized security policies, authentication, access control
- **Registry server** — curate trusted MCP servers with **claim-based authorization** (v1.2.0) for granular access control
- **Portal** — desktop and web interfaces with **threaded chat**, **MCP Apps** (interactive HTML views in chat), and **direct skill installation** into Claude Code and Cursor
- **Auto-configuration** — configures Claude Code, Cursor, VS Code, GitHub Copilot automatically
- **Agent Skills** — NEW: reusable instruction bundles that teach AI agents how and when to use tools, publishable to registry and installable across clients
- **Kubernetes-native scaling** — NEW: CRD graduated from v1alpha1 to v1beta1, horizontal scaling with Redis-backed session routing, per-user rate limiting, Cedar role-based authorization
- **vMCP local mode** — NEW: run Virtual MCP Servers locally without Kubernetes
- **Interactive TUI dashboard** — NEW: manage MCP servers from the terminal (v0.26.0)
- **LLM gateway** — NEW: `thv llm` command group with config management and localhost reverse proxy (v0.25.0)

**Key differentiator:** Where Docker MCP Gateway focuses on individual developer workflows, ToolHive targets enterprise teams that need governance, audit trails, and centralized control over which MCP servers their developers can use. The **13 releases in two weeks** (v0.19–v0.26) represent one of the most aggressive feature expansions in the MCP ecosystem — ToolHive is rapidly evolving from a container management tool into a full enterprise MCP platform with authorization, skills, and production-grade Kubernetes support.

## Developer Tools MCP Comparison

| Aspect | GitHub | GitLab | Bitbucket | Docker | Kubernetes | CI/CD | IDE/Editor | Testing/QA | Monitoring | Security | IaC | Packages | Code Gen | API Dev | Logging | DB Migration | Doc Tooling | Debugging | Profiling | Code Review |
|--------|--------|--------|-----------|--------|------------|-------|------------|------------|------------|---------- | ------- |----------|----------|---------|---------------------- | --------------|-----------|-----------|-------------|
| **Official MCP server** | Yes (28.2k stars, 21 toolsets) | Yes (built-in, 15 tools, Premium+) | No (Jira/Confluence only) | Yes (Hub MCP, 141 stars, 12+ tools) | [No (Red Hat leads, 1.3k stars)](/reviews/kubernetes-mcp-servers/) | [Yes (Jenkins, CircleCI, Buildkite)](/reviews/ci-cd-mcp-servers/) | Yes (JetBrains built-in, 24 tools) | [Yes (MS Playwright, 9.8k stars, 24 tools)](/reviews/testing-qa-mcp-servers/) | [Yes (Grafana 2.5k, Datadog, Sentry, Dynatrace, New Relic, Instana)](/reviews/monitoring-observability-mcp-servers/) | [Yes (Semgrep, SonarQube, Snyk, Trivy, GitGuardian, Cycode, Contrast)](/reviews/security-scanning-mcp-servers/) | Yes (Terraform 1.3k, Pulumi remote, AWS IaC, OpenTofu 84) | Yes (NuGet built-in VS 2026, Homebrew built-in) | Partial (Vercel next-devtools 694, E2B 384, JetBrains built-in server) | Yes (Postman 192, Apollo GraphQL 275, Kong deprecated, Apigee, MuleSoft) | Yes (Splunk 13 tools GA, Grafana Tempo built-in, Grafana Loki 103 stars) | Partial (Liquibase private preview 19 tools, Prisma built-in CLI v6.6.0+) | Yes (Microsoft Learn 1.5k, Mintlify auto, ReadMe per-project, Stainless, OpenAI Docs) | Yes (Chrome DevTools 31k, Microsoft DebugMCP 263, MCP Inspector 9.2k official) | Partial (CodSpeed MCP, Polar Signals remote, Grafana Pyroscope via mcp-grafana) | Yes (SonarQube 442 stars, Codacy 56 stars, Graphite GT built-in) |
| **Remote hosting** | Yes (`api.githubcopilot.com/mcp/`) | No | No | No (Gateway is local) | [AWS EKS MCP (preview)](/reviews/kubernetes-mcp-servers/) | [Yes (Buildkite remote MCP)](/reviews/ci-cd-mcp-servers/) | No (requires running IDE) | [No (local browser required)](/reviews/testing-qa-mcp-servers/) | [Yes (Datadog, Sentry — OAuth)](/reviews/monitoring-observability-mcp-servers/) | [No (all local/CLI-based)](/reviews/security-scanning-mcp-servers/) | [Yes (Pulumi remote MCP)](/reviews/infrastructure-as-code-mcp-servers/) | N/A | N/A | N/A | N/A | — | N/A | No (local debuggers) | No (local profiling agents) | N/A |
| **Top community server** | GitMCP (7.8k stars) | zereight/gitlab-mcp (1.2k stars) | aashari (132 stars) | ckreiling (707 stars, 25 tools) | [Flux159 (1.4k stars, 20+ tools)](/reviews/kubernetes-mcp-servers/) | [Argo CD (356 stars, 12 tools)](/reviews/ci-cd-mcp-servers/) | vscode-mcp-server (342 stars, 15 tools) | [executeautomation (5.3k stars)](/reviews/testing-qa-mcp-servers/) | [pab1it0/prometheus (340 stars)](/reviews/monitoring-observability-mcp-servers/) | [CodeQL community (143 stars)](/reviews/security-scanning-mcp-servers/) | Ansible (25 stars, 40+ tools) | mcp-package-version (122 stars, 9 registries) | Context7 (50.3k stars), magic-mcp (4.5k stars) | openapi-mcp-generator (495 stars), mcp-graphql (374 stars) | cr7258/elasticsearch (259 stars), Traceloop OTel (178 stars) | mpreziuso/mcp-atlas (Atlas), defrex/drizzle-mcp (Drizzle) | GitMCP (7.8k stars), Grounded Docs (1.2k stars), Docs MCP (87 stars) | claude-debugs-for-you (496 stars), x64DbgMCPServer (398 stars), devtools-debugger (341 stars) | theSharque/mcp-jperf (Java JFR), PageSpeed Insights MCP servers | kopfrechner/gitlab-mr-mcp (86 stars), crazyrabbitLTC (32 stars) |
| **Infrastructure role** | None | None | None | MCP Gateway + Catalog (300+ servers) | None | [Build orchestration](/reviews/ci-cd-mcp-servers/) | None | None | None | None | None | N/A | N/A | Spec-to-server conversion + API interaction | N/A | — | N/A | N/A | N/A | N/A |
| **Enterprise management** | N/A | N/A | N/A | ToolHive (1.8k stars, v0.26) | [Read-only + secret redaction](/reviews/kubernetes-mcp-servers/) | [Limited safety controls](/reviews/ci-cd-mcp-servers/) | N/A | N/A | [Metrics querying (PromQL, DQL, NRQL)](/reviews/monitoring-observability-mcp-servers/) | [Scan-and-fix capability](/reviews/security-scanning-mcp-servers/) | N/A | N/A | N/A | 4+ (Postman, Apollo, Kong, Google/Apigee, MuleSoft) | N/A | — | N/A | N/A | N/A | N/A |
| **Authentication** | PAT / GitHub App | OAuth 2.0 / PAT | App Password / OAuth | Docker Desktop credentials | [kubeconfig / OAuth / OIDC](/reviews/kubernetes-mcp-servers/) | [API tokens per platform](/reviews/ci-cd-mcp-servers/) | Local connection (port/stdio) | [None (local browsers)](/reviews/testing-qa-mcp-servers/) | [API tokens / OAuth (remote)](/reviews/monitoring-observability-mcp-servers/) | [API tokens / CLI auth](/reviews/security-scanning-mcp-servers/) | API tokens / OAuth / CLI auth | None (public registries) | API keys (Context7, magic-mcp, E2B) | API keys / Bearer / OAuth / 1Password | API tokens / OAuth / RBAC (Splunk) | Database credentials / CLI auth | None (GitMCP, MS Learn) / API keys (platform MCP) | None (local debuggers) / Chrome DevTools auto-connect | API keys (CodSpeed, Polar Signals) / Grafana auth / Google API key (PageSpeed) | API tokens (SonarQube, Codacy) / GitHub PAT / GitLab PAT |
| **AAIF membership** | No (but Microsoft is Platinum) | No | No | Gold member | [No (Google/AWS/MS are Platinum)](/reviews/kubernetes-mcp-servers/) | [No](/reviews/ci-cd-mcp-servers/) | No (but Microsoft is Platinum) | [No (but Microsoft is Platinum)](/reviews/testing-qa-mcp-servers/) | [No](/reviews/monitoring-observability-mcp-servers/) | [No](/reviews/security-scanning-mcp-servers/) | No | No (but Microsoft is Platinum) | No | No | No | No | No (but Microsoft is Platinum) | No (but Google/Microsoft are Platinum) | No | No |
| **Platform users** | 180M+ developers | 30M+ users | ~41k companies | 20M+ users | [5.6M developers](/reviews/kubernetes-mcp-servers/) | [Jenkins: 11.3M devs](/reviews/ci-cd-mcp-servers/) | VS Code: 75.9% market share | [Playwright: 45.1% QA adoption](/reviews/testing-qa-mcp-servers/) | [Datadog: 32.7k customers](/reviews/monitoring-observability-mcp-servers/) | [SonarQube: 17.7% SAST mindshare](/reviews/security-scanning-mcp-servers/) | Terraform: millions of users, 45% IaC adoption | npm: 5B+ weekly downloads, PyPI: 421.6B yearly | Copilot: 20M+ users, Cursor: 1M+ DAU | Postman: 30M+ users, REST: ~83% of web APIs | Splunk: 15k+ customers, ELK: most-deployed log stack | Prisma: 43k stars, Flyway: 10.7k stars, Atlas: 6.3k stars | Mintlify: 28k+ stars, Docusaurus: 60k+ stars, ReadMe: powering major API docs | Chrome: 65%+ browser share, VS Code: 75.9% IDE share, x64dbg: 45k+ stars | APM market: $7-10B, Pyroscope: 11k+ stars, async-profiler: 9k+ stars | SonarQube: 7.4M+ users, CodeRabbit: top AI reviewer, Qodo/PR-Agent: 10.5k stars |
| **Our rating** | [4.5/5](/reviews/github-mcp-server/) | [3.5/5](/reviews/gitlab-mcp-server/) | [2.5/5](/reviews/bitbucket-mcp-server/) | 4/5 | [4/5](/reviews/kubernetes-mcp-servers/) | [3/5](/reviews/ci-cd-mcp-servers/) | [3.5/5](/reviews/ide-code-editor-mcp-servers/) | [3.5/5](/reviews/testing-qa-mcp-servers/) | [4/5](/reviews/monitoring-observability-mcp-servers/) | [3.5/5](/reviews/security-scanning-mcp-servers/) | [4/5](/reviews/infrastructure-as-code-mcp-servers/) | [3/5](/reviews/package-management-mcp-servers/) | [3.5/5](/reviews/code-generation-mcp-servers/) | [3.5/5](/reviews/api-development-mcp-servers/) | [3.5/5](/reviews/logging-tracing-mcp-servers/) | [2.5/5](/reviews/database-migration-mcp-servers/) | [3.5/5](/reviews/documentation-tooling-mcp-servers/) | [4.5/5](/reviews/debugging-mcp-servers/) | [3/5](/reviews/profiling-performance-mcp-servers/) | [3.5/5](/reviews/code-review-pull-request-mcp-servers/) |

## Known Issues

1. **Docker socket access is a security risk** — Container management MCP servers require mounting the Docker socket (`/var/run/docker.sock`), which grants full control over the Docker daemon. An AI agent with Docker socket access can create privileged containers, mount host filesystems, or affect other running containers. This is inherent to Docker's architecture, not specific to MCP.

2. **No official container management server** — Docker's official Hub MCP server only covers Docker Hub operations (search, repositories, tags). For actual container management (create, start, stop, logs), you need community servers like ckreiling/mcp-server-docker. Docker's MCP investment focuses on infrastructure (Gateway, Catalog) rather than a first-party container management tool.

3. **GPL-3.0 license on the leading server** — ckreiling/mcp-server-docker uses GPL-3.0, which may create licensing concerns for enterprises that integrate it into proprietary toolchains. The MIT-licensed QuantGeekDev alternative has only 4 tools vs 25.

4. **MCP Gateway requires Docker Desktop** — The MCP Gateway is a Docker CLI plugin requiring Docker Desktop 4.59+ (now at 4.71.0 as of April 27, 2026). This ties MCP server management to Docker Desktop's subscription model ($11–$24/user/month for professional/business tiers). Teams using Docker Engine without Desktop need alternatives like ToolHive, which now supports local vMCP without Kubernetes.

5. **Catalog is still in Beta** — The Docker MCP Catalog launched in Beta on May 5, 2025. While 300+ servers are verified, the submission and review process is still maturing. Quality varies across the catalog, and the security review standards haven't been publicly audited by independent parties.

6. **Container operations lack safety guardrails** — Unlike MatanYemini's Bitbucket server (which blocks DELETE operations) or cyanheads/git-mcp-server (which has safety features), the Docker community servers don't implement safety boundaries. An AI agent can `remove` containers, images, networks, and volumes without confirmation flows.

7. **No Kubernetes-native MCP** — Docker's MCP ecosystem focuses on Docker containers and Compose. For Kubernetes management, you need separate servers like [containers/kubernetes-mcp-server](https://github.com/containers/kubernetes-mcp-server) or [Flux159/mcp-server-kubernetes](https://github.com/Flux159/mcp-server-kubernetes). The containerized MCP ecosystem and the orchestrated MCP ecosystem don't overlap.

8. **Hub MCP server is minimal** — Docker's official Hub MCP server has only 11 commits and 12+ tools. Compare this to GitHub's official server (774 commits, 21 toolsets) or even the community Docker management servers. Hub MCP feels like a proof-of-concept rather than a production-grade tool.

9. **ToolHive is not Docker-owned** — ToolHive is maintained by Stacklok (now part of the security ecosystem), not Docker. While it complements Docker's MCP Gateway, the two tools have different governance, release cycles, and support models. Enterprise teams may need to evaluate which management layer to standardize on.

10. **Ecosystem fragmentation between management and infrastructure** — Docker's MCP story requires understanding multiple tools: Hub MCP for Docker Hub, ckreiling for containers, MCP Gateway for running servers, MCP Catalog for discovering servers, and potentially ToolHive for enterprise governance. There's no single "Docker MCP server" that does everything.

## Bottom Line

**Rating: 4 out of 5**

Docker's MCP ecosystem is **unlike any other in this category** because Docker plays a dual role: it's both a **platform with MCP servers** (for managing containers and Docker Hub) and the **infrastructure layer that runs everyone else's MCP servers** (via MCP Gateway and the MCP Catalog). This infrastructure role is arguably more important than the Docker-specific tools.

On the **container management side**, [ckreiling/mcp-server-docker](https://github.com/ckreiling/mcp-server-docker) (707 stars, 25 tools) remains the community leader covering containers, images, networks, and volumes, though it's been dormant (53 commits, no releases). [QuantGeekDev/docker-mcp](https://github.com/QuantGeekDev/docker-mcp) (475 stars, 4 tools) offers a simpler alternative with Compose support. Docker's own [Hub MCP server](https://github.com/docker/hub-mcp) (141 stars, 12+ tools) covers Docker Hub operations but remains minimal.

On the **infrastructure side**, the [MCP Gateway](https://github.com/docker/mcp-gateway) (1.4k stars) now features **Dynamic MCP discovery** — agents can search the catalog and add servers at runtime via `mcp-find`/`mcp-add` without manual configuration. The [MCP Catalog](https://docs.docker.com/ai/mcp-catalog-and-toolkit/) (300+ verified servers, registry at 3,006 commits) continues growing as the default distribution channel. And [ToolHive](https://github.com/stacklok/toolhive) (1.8k stars, v0.26.0) has **exploded with 13 releases in two weeks** — adding Agent Skills, MCP Apps, Cedar authorization, CRD graduation, and Kubernetes horizontal scaling, transforming it from a container management tool into a full enterprise MCP platform.

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

*This review was researched and written by an AI agent. We do not have hands-on access to these tools — our analysis is based on documentation, GitHub repositories, community reports, and official announcements. Information is current as of April 2026. See our [About page](/about/) for details on our review process.*

