# Feature Flags & Experimentation MCP Servers — LaunchDarkly, GrowthBook, Unleash, Flagsmith, and More

> Feature flag and experimentation MCP servers reviewed: LaunchDarkly (13 stars, hosted, 3 MCP endpoints), GrowthBook (21 stars, 14 tools, open-source), Unleash (6 stars, best-practice workflows), Flagsmith (role-based tooling, Gemini/Codex CLI support), DevCycle (35+ tools, OAuth-backed, hosted remote), Statsig (27 Console API tools, metrics), ConfigCat (full management API), Flipt (git-native), VWO FME (3 stars, new entry), Optimizely (closed beta, Gartner Leader 2026), PostHog (141 stars, 27 tools, archived to monorepo), Harness FME (10 tools, 139 resource types, incl. Split.io), Amplitude (experimentation agent). Rating: 4.0/5.


Feature flag and experimentation MCP servers are giving AI coding assistants direct access to flag management, A/B testing, and progressive rollouts. Instead of switching between your IDE and a feature flag dashboard, these servers let AI agents create flags, set up targeting rules, run experiments, and clean up stale flags — all through the Model Context Protocol.

The landscape spans three areas: **official platform servers** (every major vendor has one), **community implementations** (filling gaps or offering alternative approaches), and **analytics platforms with flag support** (where experimentation meets product analytics).

The headline findings: **Vendor coverage is remarkably complete** — LaunchDarkly, GrowthBook, Unleash, Flagsmith, DevCycle, Statsig, ConfigCat, Flipt, Optimizely, PostHog, Harness (with Split.io), and Amplitude all have official MCP servers. **GrowthBook pioneered the category**, branding itself "the first MCP server for experimentation." **Flagsmith takes the smartest approach to tool exposure**, surfacing role-specific subsets rather than dumping 500+ API endpoints on an agent. **PostHog offers the broadest scope** with 27 tools spanning flags, experiments, analytics, error tracking, and session replay. **DevCycle has the strongest security model** with OAuth-backed authentication. **Most servers focus on CRUD** — create, read, update, delete — rather than helping agents make intelligent decisions about rollout strategy based on experiment data.

**Category:** [Developer Tools](/categories/developer-tools/)

## Official Platform Servers

### LaunchDarkly MCP Server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [launchdarkly/mcp-server](https://github.com/launchdarkly/mcp-server) | 13 | TypeScript | MIT | 10+ |

Official MCP server from LaunchDarkly, the category leader in feature management. Provides three hosted MCP servers, each focused on a different product area: **feature management** (create, get, list, toggle, and update flags, targeting rules, rollouts, individual targets), **AI Configs** (manage AI configurations and variations), and **observability** (query logs, traces, errors, and dashboards). The hosted endpoint architecture means zero local installation — just point your MCP client and authenticate.

Key tools include `create-flag` (defaults to boolean temporary flag, OFF in all environments), `get-flag` (detailed configuration scoped to a specific environment), `list-flags` (search and browse), `toggle-flag` (targeting on/off per environment), `update-flag-settings` (name, description, tags, temporary/permanent status, maintainer), `update-targeting-rules`, `update-rollout`, `update-individual-targets`, `query-flag-evaluations` (query evaluations for a session), and `query-timeline-events` (query timeline indicator events). The separation into product-specific servers is a thoughtful design — agents get only the tools relevant to their task rather than a monolithic tool list.

LaunchDarkly is the market leader in enterprise feature management, and their MCP server reflects that maturity with hosted infrastructure and structured tool organization. Works with any MCP-compatible AI client including Cursor, Claude, Windsurf, and Raycast.

### GrowthBook MCP Server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [growthbook/growthbook-mcp](https://github.com/growthbook/growthbook-mcp) | 21 | TypeScript | — | 14 |

Official MCP server from GrowthBook, the leading open-source feature flagging and experimentation platform (7,000+ GitHub stars on the main repo). GrowthBook positioned this as "the first MCP server for experimentation and feature management" — and the 14-tool set backs up that claim.

Tools cover the full experimentation lifecycle: create feature flags, set up safe rollouts, configure A/B tests, manage environments, list projects, get SDK connections, create new SDK connections, list metrics, and search GrowthBook documentation. The documentation search tool is a nice touch — agents can look up implementation details without leaving the workflow.

The server works with Cursor, Claude, VS Code, and Windsurf. Configuration is straightforward: `npx` with `GB_API_KEY` and `GB_USER` environment variables. GrowthBook's open-source nature (the platform itself is free to self-host) makes this a strong choice for teams that want full control over both their experimentation platform and their MCP integration.

### Unleash MCP Server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [Unleash/unleash-mcp](https://github.com/Unleash/unleash-mcp) | 6 | TypeScript | — | 4+ |

Official MCP server from Unleash, the open-source feature management platform (10,000+ stars, 20M+ downloads). This is a **purpose-driven** server — rather than exposing the full Admin API, it implements an opinionated workflow for AI-assisted flag creation.

The workflow follows four steps: detect existing flags (prevent duplicates or encourage reuse), evaluate whether changes need a flag, `create_flag` (with proper validation and typing), and `wrap_change` (generate language-specific implementation code). This is notably different from servers that just expose CRUD operations — Unleash's MCP server guides agents through best practices rather than giving them raw API access.

Currently marked as **experimental** — functionality may change and is not yet recommended for production use. Available via npx without cloning the repo. Community alternatives exist from cuongtl1992 and ylin6 for teams that want broader API access.

### Flagsmith MCP Server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| Flagsmith MCP | — | — | — | — |

Official MCP server from Flagsmith, the open-source feature flag and remote configuration service. What sets Flagsmith apart is their **role-based tool exposure** approach — rather than dumping all 500+ API endpoints on an AI agent, they surface only the tools relevant to a given role.

For **developers**: create and configure flags directly from the IDE, with AI updating code automatically. For **release managers**: run canary releases, schedule staged deployments, manage change requests. For **flag hygiene**: identify stale flags, compare flag status across environments, create multi-flag change requests from the CLI.

Core capabilities cover Organizations & Projects (list and navigate workspaces), Feature Flags (create, update, manage across environments), and Segments (build and modify user segments for targeting). The server also supports organizational conventions — naming standards and best practices enforced at the org level, reducing cognitive burden on developers.

Compatible with Cursor, Claude Code, Claude Desktop, Windsurf, Gemini CLI, Codex CLI, and any other MCP-compatible client. This is one of the broadest client compatibility lists in the feature flag MCP space.

### VWO FME MCP Server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [wingify/vwo-fme-mcp](https://github.com/wingify/vwo-fme-mcp) | 3 | TypeScript | — | 5+ |

Official MCP server from VWO (Visual Website Optimizer) for Feature Management & Experimentation. Provides comprehensive feature flag management within AI coding environments — create, view, list, update, and delete feature flags with environment-specific controls.

Distinctive features include **Cursor Rule Setup** bootstrapping that simplifies configuration of Cursor rules for contextual results and SDK integration, and the ability to create flags with full defaults (variables, variations, associated metrics, rules, and automatic enablement). The server handles the complete flag lifecycle from creation with mandatory requirements through safe removal.

Compatible with Cursor, VS Code, and Claude. VWO is an established A/B testing and experimentation platform, and their MCP server brings their feature management capabilities directly into AI-assisted development workflows.

### DevCycle MCP Server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [DevCycleHQ/cli](https://github.com/DevCycleHQ/cli) | — | TypeScript | — | 35+ |

Official MCP server from DevCycle, built into their CLI and now available as a **hosted remote MCP** — no local server setup needed. One of the few feature flag MCP servers with proper **OAuth-backed authentication**, negotiating Streamable HTTP or SSE transport and respecting the authenticated user's permission level.

The 35+ tools cover the full DevCycle surface: feature and variation CRUD, targeting rules, variables, environments, SDK keys, project introspection, self-targeting overrides, usage/evaluation analytics, and audit history. The evaluation analytics capability is notable — agents can query how flags are actually being evaluated in production, not just how they're configured.

Safety features are well-thought-out: tools that can change production are clearly marked, and destructive actions require explicit confirmation. The OAuth model means the MCP server inherits the same access controls as the DevCycle dashboard — no separate API key management.

Born from a hackathon and shipped to production — DevCycle has written about the journey from prototype to production-ready MCP server. Compatible with Claude Desktop, Cursor, VS Code, Windsurf, and other MCP clients.

### Statsig MCP Server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [GeLi2001/statsig-mcp](https://github.com/GeLi2001/statsig-mcp) | — | TypeScript | — | 27 |

MCP server for Statsig, the enterprise-grade experimentation platform built by engineers from Facebook's experimentation team (handles 1 trillion+ events daily). Provides **27 Console API tools** organized by resource type, using a **hybrid three-API architecture**: Console API for project management (team users, event types), HTTP API for real-time feature checks (gates, configs, experiments, layers), and Events API for direct event logging.

Tools cover feature gate management (CRUD), dynamic configuration management (full CRUD), experiment management, user segment creation and management, metrics access and analysis, and audit logs. The real-time feature check capability via the HTTP API is distinctive — most flag MCP servers only support management operations, but Statsig's can actually evaluate flags in real-time. The recently added metrics and metric source tools let agents read and analyze Statsig metrics metadata from within their workflows.

Statsig's Knowledge Graph (2026) connects codebase, feature gates, experiments, users, and metrics for richer context. Use cases include putting features behind gates, instrumenting apps to log user interaction events, and removing unused gates from codebases. Statsig offers unlimited free feature flags at any scale, making the barrier to entry low.

### ConfigCat MCP Server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [configcat/mcp-server](https://github.com/configcat/mcp-server) | — | TypeScript | — | — |

Official MCP server from ConfigCat providing access to their public management API for feature flag and configuration management. Full CRUD operations on Feature Flags, Configs, Environments, and Products. The server helps integrate ConfigCat SDK, implement feature flags, and remove zombie (stale) flags from codebases.

**Important limitation**: designed for management operations only — do not use it for evaluating feature flag values in production applications. Use ConfigCat SDKs or ConfigCat Proxy for runtime evaluation. This is a clear and honest boundary that other servers should emulate.

ConfigCat also publishes a migration guide showing how to use their MCP server to migrate flags from Statsig — a practical demonstration of MCP servers automating platform migrations.

### Flipt MCP Server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [flipt-io/mcp-server-flipt](https://github.com/flipt-io/mcp-server-flipt) | — | TypeScript | — | — |

Official MCP server for Flipt, the git-native, self-hosted feature management platform. Supports listing, creating, updating, and deleting namespaces, flags, segments, rules, and more. Flipt's git-native approach means flag configurations are stored in version control — making the MCP server a natural fit for developer workflows where everything lives in git.

Installable via Smithery (`npx -y @smithery/cli install @flipt-io/mcp-server-flipt --client claude`) and configurable through `FLIPT_API_URL` environment variable. Supports both OpenFeature integration and direct API access.

### Optimizely Experimentation MCP Server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| Optimizely MCP | — | — | — | — |

Official MCP server from Optimizely for managing the feature flag and experiment lifecycle from within IDEs. Currently in **closed beta** — not publicly available. Runs locally for instant performance, offers comprehensive tool coverage, intelligently abstracts complex operations, and emphasizes security.

Optimizely is one of the oldest and largest experimentation platforms — named a **Leader in the 2026 Gartner Magic Quadrant for Personalization Engines** (2nd year running). Their entry into MCP — even in beta — signals that feature flag MCP servers are becoming table stakes for the category. An npm package (@simonecoelhosfo/optimizely-mcp-server) is available for developers who want to experiment before the official release.

### Harness FME MCP Server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [harness/mcp-server](https://github.com/harness/mcp-server) | — | TypeScript | — | — |

Official MCP server from Harness covering their Feature Management & Experimentation (FME) platform, which includes **Split.io** resources after Harness acquired Split in 2024. The server exposes structured, secure tool sets across pipelines, repositories, logs, and artifact registries.

The server provides **10 consolidated tools and 139 resource types**. FME-specific tools use both the Split.io internal API (scoped by workspace ID for `fme_workspace`, `fme_environment`, `fme_feature_flag`) and the Harness CF admin API (environment-specific definitions with create, delete, and toggle support). The `fme_feature_flag` resource supports full lifecycle management: create (requires traffic_type_id), list, get, update metadata, delete, and kill/restore/archive/unarchive execute actions. The dual-API approach reflects the ongoing integration of Split.io into the Harness platform.

Compatible with Claude Code, Windsurf, Cursor, and VS Code. The server goes beyond just feature flags — it's part of Harness's broader platform that covers the full software delivery lifecycle.

## Analytics Platforms with Experimentation

### PostHog MCP Server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [PostHog/mcp](https://github.com/PostHog/mcp) | 141 | Python | — | 27 |

Official MCP server from PostHog, the open-source product analytics platform. With **27 tools across 7 categories** — workspace management, error tracking, dashboards, insights, experiments, flags, and LLM analytics — this is the broadest feature flag MCP server by scope and the most-starred dedicated feature flag MCP server at 141 stars.

Flag-specific capabilities include creating feature flags (e.g., "create a flag called 'new-checkout-flow' enabled for 20% of users"), querying flags (find all flags rolled out to less than 50% of users), creating multivariate flags, and scheduling future flag changes. But the real power is the analytics context — agents can check experiment results, track errors, view dashboards, and manage flags all in one server.

**Note:** The standalone PostHog/mcp repository was **archived in January 2026** and moved into the PostHog monorepo. PostHog also offers an [ai-plugin](https://github.com/PostHog/ai-plugin) for Claude Code, Cursor, Gemini, Codex, and other AI coding tools. The recommended installation path is now via PostHog's AI wizard at mcp.posthog.com. A European fork (cduguet/posthog-eu-mcp) is available for EU data residency requirements.

### Amplitude MCP Server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [amplitude/mcp-server-guide](https://github.com/amplitude/mcp-server-guide) | — | — | — | — |

Official MCP server from Amplitude (currently in **beta**) enabling teams to analyze product data, experiments, and user behavior through natural language. Tools include Analytics Queries (user behavior and product metrics), Experiment Analysis (A/B test results and feature flag performance), Dashboard Access (retrieve chart and dashboard data), and Session Replay Search.

The standout feature is the **Feature Experimentation Custom Agent** — a specialized GitHub Copilot Coding Agent with Amplitude-specific prompts and MCP tools. This agent can query product insights, add instrumentation, manage feature flags, and automatically run experiments on new features. It's the most advanced agent-to-agent integration in the feature flag space.

Amplitude's MCP server is powered by MCP integration with GitHub Copilot workflows, allowing AI agents to collaborate and make data-driven decisions without manual handoffs.

## Community Implementations

### cuongtl1992/unleash-mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [cuongtl1992/unleash-mcp](https://github.com/cuongtl1992/unleash-mcp) | — | TypeScript | — | — |

Community-maintained MCP server for Unleash that provides broader API access than the official server. While the official Unleash MCP server follows an opinionated workflow (detect → evaluate → create → wrap), this community alternative exposes more of the Unleash Admin API directly. Useful for teams that want full programmatic control rather than guided workflows.

### ylin6/unleash-ff-mcp-server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [ylin6/unleash-ff-mcp-server](https://github.com/ylin6/unleash-ff-mcp-server) | — | TypeScript | — | — |

Another community Unleash MCP server implementation. The existence of multiple community servers alongside the official one reflects Unleash's strong open-source ecosystem (10,000+ stars on the main repo).

## What's missing

The category has remarkably complete vendor coverage, but some gaps remain:

- **No Eppo MCP server** — Eppo is a rising experimentation platform focused on composable, next-gen feature flagging, but has no MCP integration yet
- **Intelligent rollout decisions** — most servers handle flag CRUD but don't help agents decide *when* to roll out based on experiment metrics
- **Cross-platform flag migration** — ConfigCat's Statsig migration guide is the only example; no general-purpose flag migration tools exist
- **OpenFeature MCP integration** — OpenFeature provides a vendor-agnostic API standard, but there's no MCP server that leverages it for cross-platform flag evaluation
- **Experimentation analysis** — only PostHog and Amplitude combine flag management with statistical analysis of experiment results; most servers treat flags as configuration, not experiments

## The bottom line

Feature Flags & Experimentation MCP servers earn **4.0 out of 5**. The vendor coverage is exceptional — nearly every major platform has an official server, which is rare in the MCP ecosystem. The integration patterns are more sophisticated than most categories: OAuth authentication (DevCycle), hosted endpoints (LaunchDarkly), role-based tool exposure (Flagsmith), and purpose-driven workflows (Unleash). The main limitation is that most servers treat feature flags as simple CRUD resources rather than the experimentation instruments they are. The platforms that combine flag management with analytics (PostHog, Amplitude) point toward where this category should evolve — agents that don't just create flags, but understand when to roll them out based on data.

**Best for enterprise teams**: LaunchDarkly MCP — hosted endpoint, structured tool organization, market-leading platform.

**Best for open-source teams**: GrowthBook MCP — 14 tools, free to self-host, documentation search built in.

**Best for developer experience**: Flagsmith MCP — role-based tool exposure prevents tool overload.

**Best for full-stack product teams**: PostHog MCP — 27 tools spanning flags, experiments, analytics, errors, and session replay.

**Best for security-conscious teams**: DevCycle MCP — OAuth authentication with permission-level enforcement.

*This review was refreshed on 2026-04-25 using Claude Opus 4.6 (Anthropic). Star counts, tool counts, and platform details verified via web research. VWO FME added as new entry.*

