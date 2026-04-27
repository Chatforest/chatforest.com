# Deployment Platform & PaaS MCP Servers — Vercel, Cloudflare, Netlify, Railway, Dokploy, Coolify, ArgoCD, FluxCD, and More

> Deployment platform and PaaS MCP servers reviewed: Vercel (official, OAuth, remote MCP), Cloudflare (official, 2500+ endpoints), Netlify (official, 9 tools), Railway (186 stars, official), Dokploy (26K stars, 508 tools), Coolify (38 tools, self-hosted PaaS), ArgoCD (354 stars, GitOps), FluxCD (Go, GitOps operator), Heroku (official, Salesforce Agentforce), DigitalOcean (official, 9 services), DeployHQ (7 tools), Fly.io (community). 15+ tools reviewed. Rating: 4.0/5.


You just merged a PR. Now you need to deploy it. You open a browser tab, navigate to your hosting dashboard, find the project, click deploy, wait for the build, check logs, maybe update some environment variables first. Three clicks become ten. Ten become twenty when something breaks.

Now imagine telling your AI assistant: "Deploy the latest commit to staging, then show me the build logs." Done. No dashboard. No context-switching. No remembering which tab has which environment.

That's what deployment platform MCP servers enable. They connect AI agents directly to your hosting platform — Vercel, Cloudflare, Netlify, Railway, Heroku, DigitalOcean, Dokploy, Coolify — and to your GitOps tools like ArgoCD and FluxCD. Your AI can deploy code, manage environments, check build status, roll back failures, and configure services, all through natural language from inside your editor.

This review covers **MCP servers for deployment platforms, PaaS providers, and GitOps deployment tools**. For CI/CD pipelines and build automation (GitHub Actions, Jenkins, CircleCI), see [CI/CD MCP Servers](/reviews/ci-cd-mcp-servers/). For container orchestration (Kubernetes management), see [Kubernetes MCP Servers](/reviews/kubernetes-mcp-servers/). For infrastructure provisioning (Terraform, Pulumi, Ansible), see [Infrastructure Automation MCP Servers](/reviews/infrastructure-automation-mcp-servers/).

Part of our **[DevOps MCP category](/categories/devops/)**. The headline finding: **every major deployment platform now has an official MCP server**, from edge platforms (Cloudflare, Vercel) to traditional PaaS (Heroku, Railway) to self-hosted alternatives (Dokploy, Coolify). The self-hosted PaaS space has particularly strong MCP coverage, with Dokploy offering 508 tools — the most tool-rich deployment MCP server we've reviewed.

## Cloud & Edge Platform MCP Servers

### Cloudflare MCP Servers

| Server | Stars | Language | License | MCP Features |
|--------|-------|----------|---------|--------------|
| [cloudflare/mcp](https://github.com/cloudflare/mcp) | — | TypeScript | — | 2500+ endpoints |
| [cloudflare/mcp-server-cloudflare](https://github.com/cloudflare/mcp-server-cloudflare) | — | TypeScript | — | Domain-specific tools |
| [cloudflare/workers-mcp](https://github.com/cloudflare/workers-mcp) | — | TypeScript | — | Worker bridge |

**The broadest deployment platform MCP coverage available.** Cloudflare's unified MCP server at mcp.cloudflare.com covers 2500+ API endpoints in approximately 1K tokens using Code Mode — a remarkably token-efficient approach that compresses the entire Cloudflare API surface.

Coverage spans across: **Workers** (serverless compute), **Pages** (static sites), **KV** (key-value storage), **R2** (object storage), **D1** (SQLite databases), **DNS**, **Firewall**, **Load Balancers**, **Stream** (video), **Images**, **AI Gateway**, **Vectorize** (vector database), **Access** (zero-trust), and more.

Cloudflare also offers domain-specific servers at `*.mcp.cloudflare.com` — curated, typed tools for specific product areas when you need focused coverage rather than the full API surface.

**Why it matters:** Cloudflare's approach of wrapping their entire API surface into a single MCP server with Code Mode is architecturally distinctive. Instead of creating dozens of individual tools, the server provides a code-execution interface that lets the AI construct and execute API calls dynamically. This scales to thousands of endpoints without bloating the tool list. For teams running on Cloudflare's stack, this means one MCP server covers everything from DNS management to Worker deployment to database queries.

**Limitation:** The breadth-over-depth approach means individual operations may require more AI reasoning to construct compared to purpose-built tools. The Code Mode approach requires the AI to understand Cloudflare API semantics rather than just calling named tools.

### Vercel MCP Server

| Server | Stars | Language | License | MCP Features |
|--------|-------|----------|---------|--------------|
| [Vercel MCP](https://vercel.com/docs/mcp) | — | — | — | Remote MCP, OAuth |

**Vercel's official MCP server implements the latest MCP Authorization and Streamable HTTP specifications.** Available as a remote MCP server — no local installation required.

Tools are split between public (no auth needed) and authenticated categories:

- **Teams** — manage Vercel team settings and membership
- **Projects** — create, configure, and manage projects
- **Project Members** — manage project-level access
- **Deployments** — trigger, list, and inspect deployments
- **Deployment Events** — monitor deployment progress and logs
- **Environment Variables** — manage environment configuration across preview, development, and production

**Security model:** OAuth-based authentication with strict client approval — Vercel MCP only supports AI clients that have been reviewed and approved by Vercel. This is an unusually cautious approach compared to most MCP servers, which accept any client with valid credentials.

**Why it matters:** Vercel is the dominant hosting platform for Next.js and modern frontend applications. Their MCP server enables the complete deployment loop from within an AI assistant: create a project, configure environment variables, deploy, and monitor — without touching the Vercel dashboard. The remote MCP approach means zero local setup.

**Additional Vercel MCP tooling:**
- **vercel/mcp-handler** — helps developers build their own MCP servers that run on Vercel, supporting Next.js, Nuxt, Svelte, and more frameworks
- **vercel/next-devtools-mcp** — provides Next.js development tools specifically for coding agents
- **IvanAmador/vercel-ai-docs-mcp** — AI-powered search and querying of Vercel AI SDK documentation

**Limitation:** Beta status on all plans. The approved-clients-only requirement limits ecosystem compatibility. Star counts not publicly available for the official server.

### Netlify MCP Server

| Server | Stars | Language | License | MCP Features |
|--------|-------|----------|---------|--------------|
| [netlify/netlify-mcp](https://github.com/netlify/netlify-mcp) | — | TypeScript | — | 9 tools |

**Netlify's official MCP server enables the "prompt to production" workflow** — create, build, deploy, and manage Netlify sites from within an AI assistant.

The 9 tools cover:

- **Create and deploy sites** — from code to live URL in a single conversation
- **Manage environment variables and secrets** — configure build settings, API keys, environment-specific values
- **Install and uninstall extensions** — manage Netlify integrations programmatically
- **Configure access controls** — manage site-level permissions
- **Fetch user and team information** — check account details and team membership
- **Manage form submissions** — access Netlify Forms data

**Why it matters:** Netlify pioneered the Jamstack deployment model. Their MCP server covers the essentials for the typical static site / serverless function deployment workflow. The focus on 9 well-curated tools (rather than trying to cover every API endpoint) makes for clean AI interactions.

**Community alternative:** DynamicEndpoints/Netlify-MCP-Server offers 43 tools with comprehensive CLI coverage including Blobs, Dev Server, and Recipes — useful when you need deeper Netlify CLI integration than the official 9-tool server provides.

**Limitation:** 9 tools is relatively thin compared to competitors. No deployment rollback capability visible in the tool set. Star count not publicly available.

## Developer PaaS MCP Servers

### Railway MCP Server

| Server | Stars | Language | License | MCP Features |
|--------|-------|----------|---------|--------------|
| [railwayapp/railway-mcp-server](https://github.com/railwayapp/railway-mcp-server) | 186 | TypeScript | — | Project & deploy management |

**Railway's official MCP server connects AI assistants to the full Railway deployment lifecycle.** Railway positions itself as "stateful, serverful, pay-per-use infrastructure" — ideal for backend services, databases, and always-on processes.

Key capabilities:

- **Create projects** and deploy from templates
- **Manage environments** — create, select, and configure staging/production environments
- **Pull environment variables** — access runtime configuration
- **Retrieve build and deployment logs** — essential for AI-assisted debugging of deployed services
- **Manage services** — create, configure, and monitor Railway services

**Why it matters:** Railway's $5/month Hobby plan makes it one of the most accessible PaaS options for individual developers. The MCP server turns Railway into an AI-managed deployment platform — you describe what you want deployed and how, and the AI handles the infrastructure. The deployment log retrieval is particularly valuable: an AI can analyze why a deployment failed without you having to navigate the Railway dashboard.

**Community alternative:** jason-tan-swe/railway-mcp (72 stars) provides additional integration features as an unofficial community implementation.

**Limitation:** 186 stars suggests moderate adoption. The tool set focuses on Railway-specific resources rather than providing generic deployment primitives.

### Heroku MCP Server

| Server | Stars | Language | License | MCP Features |
|--------|-------|----------|---------|--------------|
| [heroku/heroku-mcp-server](https://github.com/heroku/heroku-mcp-server) | — | TypeScript | — | Heroku CLI integration |

**Heroku's official MCP server is the only deployment platform with native Salesforce Agentforce integration.** The server wraps the Heroku CLI, providing platform management through AI assistants.

Heroku provides official MCP server templates in **Python, Node.js, Ruby, and Go**, making it easy to deploy MCP servers on the platform itself. The managed `heroku-inference` add-on handles tool routing, authentication, and scaling for AI agents automatically.

**Why it matters:** Heroku's Salesforce integration is unique in the deployment MCP space. For enterprise teams already in the Salesforce ecosystem, this is the natural deployment MCP choice. Review Apps integration means every PR can spin up a disposable test environment — and with the MCP server, an AI agent can manage the full PR → Review App → Production pipeline.

**Limitation:** Heroku has no free tier for new accounts. The MCP server wraps the CLI rather than the API directly, which may limit some advanced workflows. Star count not publicly available.

### DigitalOcean MCP Server

| Server | Stars | Language | License | MCP Features |
|--------|-------|----------|---------|--------------|
| [digitalocean/digitalocean-mcp](https://github.com/digitalocean/digitalocean-mcp) | — | — | — | 9 services |

**DigitalOcean's official MCP server covers App Platform deployment and broader infrastructure management.** The server exposes 9 service categories (and growing):

- **App Platform** — deploy and manage applications
- **Databases** — managed database provisioning and management
- **DOKS** — DigitalOcean Kubernetes Service
- **Droplets** — virtual machine management
- **Networking** — VPCs, load balancers, firewalls
- **Spaces Storage** — S3-compatible object storage
- **Accounts, Insights, Marketplace** — account and platform tools

DigitalOcean App Platform now natively supports hosting remote MCP servers with HTTP response streaming and subdomain routing — making DigitalOcean both an MCP-managed platform and an MCP server hosting platform.

**Why it matters:** DigitalOcean's blend of simplicity and infrastructure depth makes their MCP server a one-stop shop for teams that run on DO. Unlike pure PaaS servers (Railway, Render), the DigitalOcean MCP covers both app deployment and underlying infrastructure — Droplets, networking, storage, and managed databases.

**Limitation:** The original digitalocean/digitalocean-mcp repository was archived, with the recommendation to use a newer version — suggesting an API transition that may cause confusion. Star count not publicly available.

### DeployHQ MCP Server

| Server | Stars | Language | License | MCP Features |
|--------|-------|----------|---------|--------------|
| [deployhq/deployhq-mcp-server](https://github.com/deployhq/deployhq-mcp-server) | — | TypeScript | — | 7 tools |

**DeployHQ's official MCP server provides focused deployment automation tools.** DeployHQ is a deployment service that deploys code from Git repositories to servers via FTP, SFTP, or SSH.

The 7 tools cover: List Projects, Get Project Details, List Servers, List Deployments, Get Deployment Details, Get Deployment Log, and Create Deployment.

**Why it matters:** DeployHQ fills a niche that cloud PaaS platforms don't — deploying to traditional servers. If you're deploying to shared hosting, VPS, or on-premise servers via FTP/SFTP, DeployHQ's MCP server lets your AI trigger deployments and inspect logs without navigating the deployment dashboard.

**Limitation:** 7 tools is minimal. No rollback, no environment variable management, no build configuration. The server covers the read/deploy cycle but not the full deployment lifecycle.

## Self-Hosted PaaS MCP Servers

### Dokploy MCP Server

| Server | Stars | Language | License | MCP Features |
|--------|-------|----------|---------|--------------|
| [Dokploy/mcp](https://github.com/Dokploy/mcp) | — | TypeScript | — | 508 tools, 49 categories |

**The most tool-rich deployment MCP server we've reviewed — 508 tools across 49 categories.** Dokploy (26K+ stars) is an open-source, self-hostable PaaS alternative to Vercel, Heroku, and Netlify.

The MCP server exposes the full Dokploy API: project and application management, databases, Docker configuration, notifications, SSO, backups, domain management, SSL certificates, environment variables, and more. Modern HTTP mode supports both Streamable HTTP (MCP 2025-03-26 spec) and Legacy SSE (MCP 2024-11-05).

**Why it matters:** 508 tools is exceptional coverage. For teams running Dokploy as their self-hosted deployment platform, this MCP server turns the entire platform into an AI-managed resource. The breadth means an AI agent can handle everything from creating a new project to configuring SSL to managing database backups — the complete operational lifecycle.

**Limitation:** 508 tools is a lot for an AI to navigate efficiently. Tool discovery and selection may degrade with this many options. The server is auto-generated from the API spec, so tool descriptions may not be optimized for AI consumption.

### Coolify MCP Servers

| Server | Stars | Language | License | MCP Features |
|--------|-------|----------|---------|--------------|
| [StuMason/coolify-mcp](https://github.com/StuMason/coolify-mcp) | — | TypeScript | — | 38 tools |
| [dazeb/coolify-mcp-enhanced](https://github.com/dazeb/coolify-mcp-enhanced) | — | TypeScript | — | Enhanced AI features |

**Coolify (35K+ stars) is the most-starred self-hosted PaaS platform, and its MCP ecosystem reflects that popularity.** StuMason/coolify-mcp provides 38 optimized tools covering:

- **Teams and Projects** — organizational management
- **Servers** — manage deployment targets
- **Private Keys** — SSH key management for server access
- **Applications** — deploy, configure, and manage apps
- **Databases** — provision and manage databases
- **Services** — manage background services
- **Environment Variables** — configure runtime settings
- **Deployments** — trigger and monitor deployments

The enhanced version (dazeb/coolify-mcp-enhanced) adds AI-powered natural language infrastructure management, letting you manage your entire Coolify infrastructure through conversational prompts.

**Why it matters:** Coolify's 35K stars make it the most popular self-hosted PaaS, and 38 tools is a sweet spot for AI usability — comprehensive enough for real work, focused enough for efficient tool selection. For teams that want Vercel-like deployment experience on their own hardware, Coolify + its MCP server delivers that with AI assistance.

**Additional implementations:** GoCoder7/coolify-mcp-server provides a focused 4-tool implementation for simpler use cases.

**Limitation:** No official MCP server from the Coolify team — all implementations are community-built. 38 tools covers the core workflow but may miss edge cases of the full Coolify API.

## GitOps Deployment MCP Servers

### ArgoCD MCP Server

| Server | Stars | Language | License | MCP Features |
|--------|-------|----------|---------|--------------|
| [argoproj-labs/mcp-for-argocd](https://github.com/argoproj-labs/mcp-for-argocd) | 354 | Go | — | GitOps tools |

**The most-starred GitOps MCP server, from the ArgoCD Labs organization.** ArgoCD (18K+ stars) is the dominant Kubernetes GitOps tool, and this MCP server enables AI-assisted GitOps workflows.

Core tools:

- **list_clusters** — list all clusters registered with ArgoCD
- **list_applications** — list and filter all applications across clusters
- **get_application** — get detailed information about a specific application, including sync status, health, and deployment history

Supports both **stdio and HTTP stream transport** for flexible integration with different MCP clients.

**Why it matters:** 354 stars is strong community adoption for a GitOps MCP server. ArgoCD manages Kubernetes deployments declaratively through Git — and with this MCP server, an AI agent can answer questions like "which applications are out of sync?" or "what's the health status of our production cluster?" without navigating the ArgoCD UI. For GitOps-driven deployment workflows, this bridges the gap between code changes and deployment visibility.

**Community alternative:** severity1/argocd-mcp provides a community implementation that integrates with the ArgoCD API for natural language management including additional operations beyond the labs version.

**Limitation:** The tool set is currently read-heavy — list and get operations. No sync, rollback, or application creation tools visible. 354 stars is solid but suggests the server is still maturing.

### FluxCD MCP Server

| Server | Stars | Language | License | MCP Features |
|--------|-------|----------|---------|--------------|
| [flux-operator MCP](https://github.com/controlplaneio-fluxcd/flux-operator) | — | Go | — | GitOps tools |

**The Flux Operator MCP Server connects AI assistants directly to Kubernetes clusters running Flux GitOps.** Built as a component of the Flux Operator project by ControlPlane.

The server enables AI assistants to:

- **Analyze cluster state** — trace issues from high-level GitOps resources (ResourceSets, HelmReleases, Kustomizations) all the way down to Kubernetes deployments and pod logs
- **Troubleshoot deployment issues** — correlate events across the GitOps stack
- **Perform operations** — interact with Flux resources through conversational prompts

Distributed as a **single statically-compiled Go binary** with no external dependencies, available for Linux, macOS, and Windows on both AMD64 and ARM64.

**Why it matters:** Flux's MCP server has a unique architectural advantage — it traces the full deployment path from Git source to running pod. When something breaks, the AI doesn't just tell you "the pod is crashing" — it traces back through the HelmRelease, the Kustomization, the GitRepository source, and identifies where in the reconciliation chain the issue occurred. This depth of GitOps observability is uncommon.

**Limitation:** The MCP server is embedded within the Flux Operator rather than being a standalone project, which may make adoption tracking and independent updates more difficult. Star count for the MCP component specifically is not trackable separately.

## Cloud Deployment Assistants

### Fly.io MCP Tools

| Server | Stars | Language | License | MCP Features |
|--------|-------|----------|---------|--------------|
| [brannn/fly-mcp](https://github.com/brannn/fly-mcp) | — | — | — | Infrastructure management |

**Community-built MCP server for managing Fly.io infrastructure.** Provides core tools: `ping`, `fly_list_apps` (list all applications with filtering), `fly_app_info` (detailed application information), `fly_status` (real-time status), and `fly_restart` (restart applications).

Fly.io also offers the **official `fly mcp launch` command** — a first-party CLI integration that deploys any stdio-based MCP server (npx, uv, go run, or Docker image) to a Fly machine and configures MCP client connectivity. This makes Fly.io both an MCP-managed platform and an MCP server hosting platform.

**NakulRajan/mcp-fly-deployer** generates Dockerfiles and fly.toml configurations for deploying MCP servers to Fly.io — useful for teams standardizing MCP server deployment on the platform.

**Limitation:** No official Fly.io MCP server for managing Fly.io itself (the community fly-mcp is the closest). Star counts suggest early adoption.

## The Deployment Platform MCP Landscape

The deployment platform MCP space reveals a clear market structure:

**Tier 1 — Full API coverage:**
- Cloudflare (2500+ endpoints via Code Mode)
- Dokploy (508 tools, auto-generated from OpenAPI)

**Tier 2 — Production-ready official servers:**
- Vercel (remote MCP, OAuth, deployment management)
- Netlify (9 curated tools, prompt to production)
- Railway (186 stars, project/deploy/log management)
- Heroku (CLI integration, Salesforce Agentforce)
- DigitalOcean (9 services, infrastructure + PaaS)
- ArgoCD (354 stars, GitOps visibility)

**Tier 3 — Emerging/community:**
- Coolify (38 tools, community-built, strong self-hosted PaaS)
- FluxCD (Flux Operator component, deep GitOps tracing)
- DeployHQ (7 tools, traditional deployment)
- Fly.io (community + official CLI integration)

### Key Trends

1. **Every major platform has an official server.** Vercel, Netlify, Railway, Heroku, DigitalOcean, Cloudflare, and ArgoCD all ship official MCP servers. This level of first-party support didn't exist 12 months ago.

2. **Self-hosted PaaS has the strongest MCP coverage.** Dokploy (508 tools) and Coolify (38 tools) — the two leading open-source PaaS platforms — have remarkably comprehensive MCP integration. This makes sense: self-hosted PaaS users are exactly the audience likely to adopt AI-assisted infrastructure management.

3. **Remote MCP is the default for cloud platforms.** Vercel, Cloudflare, and DigitalOcean all offer remote MCP servers. No local installation, no API key management complexity, no version synchronization. This matches the broader MCP ecosystem trend toward hosted remote servers.

4. **GitOps MCP is read-heavy.** Both ArgoCD (354 stars) and FluxCD MCP servers focus on listing and inspecting resources rather than modifying them. This is appropriate for GitOps (where changes should go through Git, not direct API calls), but limits what an AI agent can automate.

5. **Write-safety controls are rare.** Unlike PagerDuty's explicit `--enable-write-tools` flag or ArgoCD's read-only approach, most deployment platform MCP servers allow destructive operations (creating deployments, modifying configurations) without guardrails. This is a meaningful gap for production environments.

## Comparison Table

| Platform | Server | Stars | Tools | Official | Transport | Key Strength |
|----------|--------|-------|-------|----------|-----------|-------------|
| Cloudflare | cloudflare/mcp | — | 2500+ endpoints | Yes | Remote | Broadest API coverage |
| Dokploy | Dokploy/mcp | — | 508 | Yes | HTTP/SSE | Most tools, self-hosted |
| Coolify | StuMason/coolify-mcp | — | 38 | Community | stdio | Self-hosted PaaS |
| ArgoCD | argoproj-labs/mcp-for-argocd | 354 | 3+ | Labs | stdio/HTTP | GitOps visibility |
| Railway | railwayapp/railway-mcp-server | 186 | Multiple | Yes | stdio | Deploy + debug logs |
| Vercel | Vercel MCP | — | Multiple | Yes | Remote | Frontend deployment |
| Netlify | netlify/netlify-mcp | — | 9 | Yes | stdio | Prompt to production |
| Heroku | heroku/heroku-mcp-server | — | Multiple | Yes | stdio | Salesforce integration |
| DigitalOcean | digitalocean/digitalocean-mcp | — | 9 services | Yes | stdio | Infrastructure + PaaS |
| DeployHQ | deployhq/deployhq-mcp-server | — | 7 | Yes | stdio | Traditional deployment |
| FluxCD | flux-operator | — | Multiple | Yes | stdio | Deep GitOps tracing |
| Fly.io | brannn/fly-mcp | — | 5 | Community | stdio | Container deployment |

## Rating: 4.0 / 5

**Every major deployment platform now ships an official MCP server.** Cloudflare's 2500+ endpoint coverage and Dokploy's 508-tool breadth demonstrate the upper end of what's possible. ArgoCD's 354 stars shows real community adoption for GitOps workflows. The self-hosted PaaS category (Dokploy, Coolify) has particularly strong AI integration.

**Deducted 1.0 point for:**
- **Missing write-safety controls** — most servers allow destructive deployment operations without guardrails, unlike the safety-conscious defaults in SRE tooling
- **Fragmented quality** — official servers range from comprehensive (Cloudflare) to minimal (DeployHQ's 7 tools), with no consistent baseline
- **GitOps servers are read-only** — ArgoCD and FluxCD MCP servers can inspect but not trigger syncs or rollbacks, limiting automated deployment workflows
- **Star counts are low or unavailable** — many official servers don't have public star counts, making adoption difficult to assess

For teams deploying to a single platform, their platform's official MCP server is the obvious choice. For multi-platform deployment, there's no cross-platform MCP server that abstracts deployment across providers — you'll need to configure multiple platform-specific servers.

---

*This review covers publicly available data as of April 2026. Star counts and feature sets change; check the linked repositories for current information. ChatForest researches MCP servers — we do not test or endorse specific tools. See our [methodology](/about/#methodology) for how we research and rate MCP servers.*

