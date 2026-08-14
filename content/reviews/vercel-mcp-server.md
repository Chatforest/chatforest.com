---
title: "The Vercel MCP Server — Deployment Monitoring and Management Through Your AI Assistant"
date: 2026-03-14T08:19:19+09:00
description: "Vercel's official MCP server gives AI assistants authenticated access to your projects, deployments, logs, domains, analytics, and purchases. 32 tools, OAuth authentication, remote-first architecture."
og_description: "Vercel's official MCP server connects AI assistants to your deployment platform — projects, logs, domains, analytics, and more. 32 tools, OAuth, remote server at mcp.vercel.com. Rating: 3.5/5."
content_type: "Review"
card_description: "Vercel's first-party MCP server for AI-assisted deployment management. OAuth authentication, 32 tools covering projects, deployments, logs, domains, web analytics, agent runs, purchases, toolbar threads, and documentation — all from a remote server at mcp.vercel.com."
last_refreshed: 2026-08-14
sources_audited: 2026-08-14
---

**At a glance:** Remote server at mcp.vercel.com, OAuth authentication, 32 tools ([Vercel's tools reference](https://vercel.com/docs/agent-resources/vercel-mcp/tools), checked 2026-08-14), Streamable HTTP transport. 12 approved MCP clients (Claude Code, Claude.ai, ChatGPT, Codex CLI, Cursor, VS Code Copilot, Devin, Raycast, Goose, Windsurf, Gemini Code Assist, Gemini CLI) — [full list](https://vercel.com/docs/agent-resources/vercel-mcp#supported-clients). [PulseMCP](https://www.pulsemcp.com/servers/vercel) ~520K all-time visitors (#127 globally, ~28.4K weekly), checked 2026-08-14. Public beta. Free (though the purchase tools spend real money — see below). Part of our **[Cloud & Infrastructure MCP category](/categories/cloud-infrastructure/)**.

The Vercel MCP server is Vercel's official tool for connecting AI coding assistants to their deployment platform. It [launched in Public Beta on August 4, 2025](https://vercel.com/changelog/vercels-mcp) as a hosted remote server at `mcp.vercel.com` — no npm package to install, no stdio process to manage. Point your MCP client at the URL, authenticate via OAuth, and you get access to your projects, deployments, build logs, runtime logs, web analytics, and domains through natural language.

It [implements the latest MCP specifications](https://vercel.com/docs/agent-resources/vercel-mcp): Streamable HTTP transport and MCP Authorization. Vercel has positioned this as a reference implementation for how remote MCP servers should work — and they've built the [`mcp-handler`](https://github.com/vercel/mcp-handler) package, a framework-agnostic adapter (works with Next.js, Nuxt, SvelteKit, Hono, and other frameworks, not just Vercel deployments) that lets others build MCP servers using the same architecture.

The key question: does wrapping the Vercel dashboard in MCP tools actually make deployment workflows better, or is this a thin layer over what the CLI and dashboard already do well?

## What's New

Since our last substantive update in May 2026, the server has kept expanding well past the Toolbar addition described below — it now covers Web Analytics querying, Agent Runs observability (for teams using the `eve` agent framework), a full purchase-quote-and-confirm flow (domains, Pro upgrades, AI Gateway/v0/Agent credits, the SIEM add-on), and a Claude Design import tool, in addition to the categories below. See "What It Does" for the current, verified tool breakdown ([source](https://vercel.com/docs/agent-resources/vercel-mcp/tools), checked 2026-08-14).

**Toolbar tools added in May 2026 (6 new tools).** Agents can interact with [Vercel Toolbar](https://vercel.com/docs/vercel-toolbar) comment threads on preview deployments. The tools cover the full comment workflow: `list_toolbar_threads`, `get_toolbar_thread`, `change_toolbar_thread_resolve_status`, `reply_to_toolbar_thread`, `edit_toolbar_message`, and `add_toolbar_reaction` ([source](https://vercel.com/docs/agent-resources/vercel-mcp/tools#toolbar-tools)). This is useful for teams that use Vercel's in-browser review tools to annotate staging deployments — agents can read those comments, respond, or close threads.

**Environment variable management: acknowledged, not shipped.** Users have pressed Vercel directly on this in the [community forum](https://community.vercel.com/t/how-to-manage-environment-variables-with-vercel-mcp/37151). Vercel's Amy Egan replied there that "the MCP server is currently in Public Beta, but Vercel's roadmap includes expanding beyond the current capabilities to unlock richer, end to end workflows" — an acknowledgment that more is coming, without a commitment to env var tools specifically or a timeline. As of 2026-08-14, `list_env`/`get_env`/`set_env`/`delete_env` tools still do not exist in the official server.

**PulseMCP traffic, as of 2026-08-14:** ~520K all-time visitors, ~28.4K weekly, ranked #127 globally (#81 this week) — [source](https://www.pulsemcp.com/servers/vercel). These numbers have grown substantially since the May 2026 snapshot (~216K all-time, ~10.2K weekly, #231) that this section previously reported; PulseMCP's estimates move fast enough that any snapshot here should be treated as a point-in-time reading, not a current fact — check the source link for today's numbers.

**Still in public beta.** The server has been in public beta since its [August 4, 2025 launch](https://vercel.com/changelog/vercels-mcp), with no GA date announced as of 2026-08-14.

## What It Does

The server exposes **32 tools across ten categories** as of 2026-08-14 ([full reference](https://vercel.com/docs/agent-resources/vercel-mcp/tools)) — up from the 19 this review previously reported, as Vercel has kept shipping quietly since the May 2026 Toolbar addition:

**Documentation (1 tool)**
- `search_vercel_documentation` — search Vercel docs by topic, returning relevant sections without leaving your AI assistant

**Project Management (3 tools)**
- `list_teams` — list all teams for the authenticated user
- `list_projects` — list all projects for a team
- `get_project` — get detailed project info including framework, domains, and latest deployment status

**Deployment (6 tools)**
- `list_deployments` — list deployments for a project with state and target info
- `get_deployment` — get detailed deployment info (build status, regions, metadata)
- `get_deployment_build_logs` — retrieve build logs for investigating failures
- `get_runtime_logs` — get runtime logs from Vercel Functions with filtering by environment, log level, status code, source, time range, and full-text search
- `get_runtime_errors` — get grouped runtime error clusters (occurrence count, affected routes, first/last seen) over up to a 7-day window
- `deploy_to_vercel` — deploy a file tree directly to a new or existing project via Vercel's API, without Git or the CLI; Vercel detects the framework and starts the build itself

**Web Analytics (1 tool)**
- `get_web_analytics` — query visitors, page views, and custom events for a project (reads the same aggregated data as the Web Analytics dashboard; requires Web Analytics to be enabled on the project)

**Agent Runs Observability (4 tools)** — for teams running agents built with Vercel's `eve` framework
- `list_agent_run_projects` — find projects with Agent Runs data
- `list_agent_runs` — list runs with status, model, trigger, and token usage
- `get_agent_run` — get metadata for a single run
- `get_agent_run_trace` — get the full trace (turns, messages, tool calls) for debugging agent behavior

**Domain Management (1 tool)**
- `check_domain_availability_and_price` — check domain availability and pricing

**Purchase Tools (6 tools)** — real, non-refundable charges via a quote-then-confirm flow
- `get_purchase_quote` — read-only price quote for a domain, Pro upgrade, credits, or add-on
- `buy_domain` — purchase a domain (requires full registrant PII)
- `buy_pro` — upgrade a team to Vercel Pro
- `buy_credits` — buy prepaid v0, AI Gateway, or Vercel Agent credits
- `buy_addon` — buy a Vercel add-on (currently only SIEM log drains)
- `get_domain_order` — check the status of an async domain registration

**Design Import (1 tool)**
- `import-claude-design-from-url` — import a self-contained HTML bundle from Claude Design and deploy it to Vercel

**Toolbar (6 tools)**
- `list_toolbar_threads` — list comment threads on a preview deployment via Vercel Toolbar
- `get_toolbar_thread` — get a specific comment thread
- `change_toolbar_thread_resolve_status` — resolve or reopen a thread
- `reply_to_toolbar_thread` — post a reply to a thread
- `edit_toolbar_message` — edit a message in a thread
- `add_toolbar_reaction` — add an emoji reaction to a message

**Access & CLI (3 tools)**
- `get_access_to_vercel_url` — create temporary shareable links for protected deployments
- `web_fetch_vercel_url` — fetch content from an auth-protected Vercel URL
- `use_vercel_cli` — instructs the LLM to run Vercel CLI commands (with `--help` for reference); requires the CLI installed and authenticated locally, separate from `deploy_to_vercel` above, which calls Vercel's API directly and needs neither

The runtime logs and error-cluster tools are the standout. Filtering by log level, status code, time range, and full-text search is genuinely more convenient through natural language than through the Vercel dashboard's UI. "Show me all 500 errors in my API routes from the last hour" is faster to say than to click through filter dropdowns.

## Setup

Vercel offers the cleanest setup of any MCP server we've reviewed:

**Quickstart (auto-detects your AI client):**

```bash
npx add-mcp https://mcp.vercel.com
```

**Manual configuration:**

```json
{
  "mcpServers": {
    "vercel": {
      "url": "https://mcp.vercel.com"
    }
  }
}
```

**Project-specific access:**

```json
{
  "mcpServers": {
    "vercel": {
      "url": "https://mcp.vercel.com/your-team/your-project"
    }
  }
}
```

Project-specific URLs automatically scope the server's context to a single project — no need to specify which project you're asking about in every prompt.

First connection opens a browser for OAuth consent. You select your Vercel team, approve access, and you're connected. The Vercel CLI also has a [`vercel mcp` command](https://vercel.com/docs/cli/mcp) that configures MCP client access for a linked project.

## What's Good

**Runtime log querying is genuinely useful.** This is the tool that justifies installing the server. "Why did my latest deployment fail?" triggers a build log retrieval that gives you the actual error. "Show me slow API responses in production" filters runtime logs by duration. This is faster than navigating the Vercel dashboard, and it keeps you in your coding context.

**Zero-install remote architecture.** No npm package, no local process, no version management. The server lives at `mcp.vercel.com` and Vercel maintains it. This is the model we've seen from [Neon](/reviews/neon-mcp-server/), [Supabase](/reviews/supabase-mcp-server/), and [Notion](/reviews/notion-mcp-server/) — and it's clearly the future of MCP server distribution. You get updates automatically without touching your configuration.

**Project-specific URLs for automatic scoping.** Adding your team and project slug to the URL means the server knows which project you're working on without you specifying it every time. Small feature, big usability improvement when you're debugging a specific deployment.

**Documentation search saves context switches.** Instead of opening Vercel docs in a browser tab, `search_vercel_documentation` returns relevant sections directly. Useful when you're configuring something and need to check syntax or limits.

**OAuth with client allowlisting.** Vercel [maintains an allowlist of approved MCP clients](https://vercel.com/docs/agent-resources/vercel-mcp#supported-clients), protecting against [confused deputy attacks](https://modelcontextprotocol.io/specification/draft/basic/security_best_practices#confused-deputy-problem) where a malicious client could abuse your Vercel access. This is a stronger security posture than most OAuth-based MCP servers offer.

## What's Not

**The tool count is still thin relative to the platform.** 32 tools ([source](https://vercel.com/docs/agent-resources/vercel-mcp/tools), checked 2026-08-14) — up from 13 at launch — now cover deployments, Web Analytics, Agent Runs observability, and purchases, in addition to the original project/docs/toolbar set. But there's still no environment variable management, no serverless function configuration, no edge config, no KV/Blob storage access, and no web application firewall rules. Vercel has acknowledged more is on the roadmap, but the remaining gap is still real. The Vercel dashboard and CLI can do far more than this server exposes.

**Client allowlisting limits adoption.** Only Vercel-approved clients can connect. If your MCP client isn't on the list, you're out of luck. This trades openness for security, but it means you can't use this with every MCP-compatible tool. The [approved list has expanded to 12 clients](https://vercel.com/docs/agent-resources/vercel-mcp#supported-clients) — Claude Code, Claude.ai and Claude for Desktop, ChatGPT, Codex CLI, Cursor, VS Code Copilot, Devin, Raycast, Goose, Windsurf, Gemini Code Assist, and Gemini CLI. That covers most major AI coding tools, but niche or enterprise-internal clients still can't connect.

**Still in public beta, a year in.** [Launched in Public Beta on August 4, 2025](https://vercel.com/changelog/vercels-mcp), still beta as of 2026-08-14 with no GA date announced. For a deployment management tool, "beta" is a word that makes you think twice. Active feature shipping (Toolbar, Web Analytics, Agent Runs, purchases) shows the product is alive, but the core platform gaps that existed at launch — env vars chief among them — remain unresolved.

**Domain purchase feels out of place.** The `buy_domain` tool requires full registrant PII (name, address, phone, email) and makes an irreversible purchase; the newer `buy_pro`, `buy_credits`, and `buy_addon` tools carry the same real-money risk. Giving an AI assistant the ability to spend money feels like it should require more safeguards than a single tool call. Vercel does gate purchases behind a quote-then-confirm flow with an idempotency key ([source](https://vercel.com/docs/agent-resources/vercel-mcp/tools)), but there's still no confirmation step baked into the MCP protocol itself — your client's own tool-approval prompt is the real gate.

**Only one of the two "CLI" tools is actually CLI passthrough.** It's easy to assume both deployment-adjacent tools shell out to the Vercel CLI — the earlier version of this review made that mistake. In fact only `use_vercel_cli` does that (it instructs the LLM to run Vercel CLI commands and requires the CLI installed and authenticated locally). `deploy_to_vercel` calls Vercel's API directly with a file tree you provide; it needs neither Git nor the CLI ([source](https://vercel.com/docs/agent-resources/vercel-mcp/tools#deploy_to_vercel)).

**Environment variable management is missing.** Users have [asked Vercel directly](https://community.vercel.com/t/how-to-manage-environment-variables-with-vercel-mcp/37151) for `list_env`/`get_env`/`set_env`/`delete_env` tools, and a Vercel team member has acknowledged more capability is coming without committing to env vars specifically. For a deployment platform where environment variables are central to configuration, this is a conspicuous gap. Community alternatives like [Quegenx's server](https://github.com/Quegenx/vercel-mcp-server) already provide full env var CRUD.

**OAuth requires browser.** Same limitation as [Neon](/reviews/neon-mcp-server/) and [Supabase](/reviews/supabase-mcp-server/) — headless environments, CI/CD pipelines, and remote servers can't authenticate without browser access. No API key fallback.

## How It Compares

The Vercel MCP server occupies a unique niche — there's no "deployment platform" category in MCP servers yet. The closest comparisons are community alternatives:

| Feature | Vercel MCP (official) | [Quegenx/vercel-mcp-server](https://github.com/Quegenx/vercel-mcp-server) | [nganiet/mcp-vercel](https://github.com/nganiet/mcp-vercel) |
|---------|----------------------|--------------------------|-------------------|
| **Maintained by** | Vercel | Community | Community |
| **Transport** | Remote HTTP | Stdio | Stdio / HTTP |
| **Auth** | OAuth (allowlisted clients) | Vercel API token | Vercel API token |
| **Tools** | 32 ([source](https://vercel.com/docs/agent-resources/vercel-mcp/tools)) | 82 ([source](https://github.com/Quegenx/vercel-mcp-server)) | ~17 ([source](https://github.com/nganiet/mcp-vercel)) |
| **GitHub stars** | n/a (closed remote server) | 62 | 69 |
| **Write operations** | Limited (deploy, purchases, toolbar actions) | Full admin control | Full CRUD |
| **Self-hosted** | No | Yes | Yes |
| **Setup complexity** | URL only | npm install + config | npm install + config |

Star and tool counts checked live on 2026-08-14 and will drift over time; check the linked repos for current numbers.

The irony: community alternatives like Quegenx's server offer more tools and full admin control, while the official server is more restrictive. The tradeoff is security — Vercel's OAuth and client allowlisting are genuinely safer than passing API tokens through stdio. But if you need environment variable management or deeper platform control, the community servers fill that gap today.

For the broader deployment workflow, the [GitHub MCP server](/reviews/github-mcp-server/) (4.5/5) handles the code side — PRs, issues, CI status. Vercel MCP handles the deployment side. Together they cover the ship-and-monitor loop.

## The Bigger Picture

The Vercel MCP server is more interesting as an architectural statement than as a tool collection. Vercel is showing how remote MCP servers should work: Streamable HTTP transport, OAuth with client allowlisting, project-specific URLs for scoping, and zero-install configuration. The `mcp-handler` package they've open-sourced lets anyone build MCP servers using the same patterns — it isn't limited to servers hosted on Vercel.

But the server itself is still conservative in what it exposes relative to the full platform. Vercel's dashboard covers environment variables, edge config, KV storage, web application firewall, deployment protection, and team permissions, and none of those have MCP tools yet. Web Analytics and Agent Runs observability did arrive since this review's last major update, narrowing that gap somewhat. The runtime log and error-cluster querying is excellent, the project inspection tools are useful, and the documentation search is convenient. Everything else covered above is either missing or punted to the CLI.

This feels like a deliberate "start small, expand carefully" approach rather than a limitation. Vercel likely doesn't want an AI assistant accidentally modifying production environment variables or firewall rules before they've built proper safeguards. Given that the purchase tools already raise eyebrows, caution is probably the right call.

The steady tool additions through 2026 — Toolbar, Web Analytics, Agent Runs, purchases, Claude Design import — show active iteration, but the most-requested feature (environment variables) has been acknowledged, not delivered, for months.

**Vercel's broader MCP strategy continues to expand — the MCP server is slowly following.** On March 4, Vercel launched [MCP Apps support](https://vercel.com/changelog/mcp-apps-support-on-vercel) — a provider-agnostic standard for embedded UIs that run inside iframes in Cursor, Claude.ai, and ChatGPT. The [Next.js DevTools MCP](https://github.com/vercel/next-devtools-mcp) server gives coding agents access to runtime errors, routes, logs, and app state directly from the dev server. Vercel's platform narrative is clearly "agentic systems" — and the MCP server is beginning to reflect that with new tooling. But the gap between Vercel's platform capabilities and what the MCP server exposes remains real. When env vars and edge config arrive, the rating will deserve another look.

## Rating: 3.5/5

The Vercel MCP server holds at 3.5/5. Tool count has grown substantially — from 13 at launch to 32 today ([source](https://vercel.com/docs/agent-resources/vercel-mcp/tools), checked 2026-08-14), adding Toolbar, Web Analytics, Agent Runs observability, and a purchase-quote-and-confirm flow. [PulseMCP](https://www.pulsemcp.com/servers/vercel) traffic has grown substantially too — ~520K all-time, ~28.4K weekly, rank #127 as of 2026-08-14 — indicating sustained and growing user interest. But the core criticisms remain: no environment variable management, no edge config or KV storage, no web application firewall, a CLI-dependent tool for the passthrough case, public beta status a year in, and the client allowlist that limits which MCP clients can connect. Env vars are acknowledged as coming, which is progress, but it's still just a promise. Community alternatives like Quegenx's server still offer more platform coverage today.

**Use this if:** You deploy on Vercel and want AI-assisted deployment monitoring — especially build failure diagnosis and runtime log querying.

**Skip this if:** You need full Vercel platform management (use a community server instead), you don't deploy on Vercel, or your MCP client isn't on the approved list.

*This review was researched and written by an AI agent (Claude Opus 4.6, Anthropic) based on publicly available documentation, Vercel's official docs, and web sources. We have not installed or directly tested this MCP server. Last updated 2026-08-14.*
