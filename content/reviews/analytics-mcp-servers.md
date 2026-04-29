---
title: "Analytics MCP Servers — Google Analytics, Mixpanel, PostHog, Amplitude, Microsoft Clarity, and Beyond"
date: 2026-03-15T02:30:00+09:00
lastmod: 2026-04-29
description: "Analytics MCP servers let AI agents query traffic data, analyze user behavior, run retention reports, and manage experiments across Google Analytics, Mixpanel, PostHog, Amplitude, Pendo, Microsoft Clarity"
og_description: "Analytics MCP servers: Google Analytics (2K stars, official), PostHog (27+ tools, 34.2K mono), Amplitude (24+ tools, Session Replays, MCP App, 27 skills), Pendo (NEW official, Claude Connectors), Microsoft Clarity (81 stars), Mixpanel (beta + ChatGPT/Gemini), Sentry's Plausible MCP hosted. 25+ servers reviewed. Rating: 4/5."
content_type: "Review"
card_description: "Analytics MCP servers across Google Analytics, PostHog, Amplitude, Pendo, Mixpanel, Microsoft Clarity, Plausible, and Matomo. Six platforms now have official MCP servers. Amplitude expanded massively into Session Replays, Agent Skills, and in-client chart rendering. Sentry built a hosted Plausible MCP."
last_refreshed: 2026-04-29
---

Analytics is the MCP category where vendor adoption is strongest — and it keeps accelerating. Google, PostHog, Amplitude, Mixpanel, Microsoft Clarity, and now Pendo all ship official MCP servers — six platforms covered. Amplitude expanded massively beyond analytics into Session Replays, Agent Skills, and in-client chart rendering. Sentry built and hosts a Plausible MCP server, partially closing the privacy-first gap. Microsoft added a second official analytics MCP server for Fabric Real-Time Intelligence.

Giving an AI agent access to your analytics data is high-value. Instead of building dashboards or writing SQL, you can ask "what caused the sign-up drop last week?" and get an answer grounded in real data. The question is which platforms have MCP servers mature enough to deliver on that promise. Part of our **[Data & Analytics](/categories/data-analytics/)** category.

## The Landscape

### Google Analytics

| Server | Stars | Language | Tools | Auth | License |
|--------|-------|----------|-------|------|---------|
| [googleanalytics/google-analytics-mcp](https://github.com/googleanalytics/google-analytics-mcp) | 2,000 | Python | 7 | ADC (Google Cloud) | Apache 2.0 |
| [surendranb/google-analytics-mcp](https://github.com/surendranb/google-analytics-mcp) | 205 | Python | 7 | Service account | Apache 2.0 |
| [gomarble-ai/google-analytics-mcp-server](https://github.com/gomarble-ai/google-analytics-mcp-server) | 14 | Python | 7 | OAuth 2.0 | MIT |
| [ruchernchong/mcp-server-google-analytics](https://github.com/ruchernchong/mcp-server-google-analytics) | 70 | JavaScript | — | Service account | MIT (archived) |

### PostHog

| Server | Stars | Language | Tools | Auth | License |
|--------|-------|----------|-------|------|---------|
| [PostHog/posthog/services/mcp](https://github.com/PostHog/posthog/tree/master/services/mcp) (monorepo) | 34,200 | TypeScript | 27+ | API key / OAuth | MIT |

### Amplitude

| Server | Stars | Language | Tools | Auth | License |
|--------|-------|----------|-------|------|---------|
| [Amplitude MCP](https://amplitude.com/mcp-server) (official hosted) | — | — | 24+ | OAuth 2.0 | — |
| [silviorodrigues/amplitude-mcp](https://github.com/silviorodrigues/amplitude-mcp) | 9 | TypeScript | 2 | API key + secret | MIT (archived) |

### Mixpanel

| Server | Stars | Language | Tools | Auth | License |
|--------|-------|----------|-------|------|---------|
| [Mixpanel MCP](https://docs.mixpanel.com/docs/features/mcp) (official) | — | — | — | OAuth | — |
| [dragonkhoi/mixpanel-mcp](https://github.com/dragonkhoi/mixpanel-mcp) | 19 | TypeScript | — | Service account | MIT |
| [moonbirdai/mixpanel-mcp-server](https://github.com/moonbirdai/mixpanel-mcp-server) | — | — | — | API token | — |

### Pendo (New)

| Server | Stars | Language | Tools | Auth | License |
|--------|-------|----------|-------|------|---------|
| [Pendo MCP](https://www.pendo.io/product/mcp/) (official hosted) | — | — | — | OAuth 2.0 | — |

### Plausible

| Server | Stars | Language | Tools | Auth | License |
|--------|-------|----------|-------|------|---------|
| [getsentry/plausible-mcp](https://github.com/getsentry/plausible-mcp) | — | TypeScript | 4 | API key | MIT |
| [AVIMBU/plausible-mcp-server](https://github.com/AVIMBU/plausible-mcp-server) | 7 | TypeScript | — | API key | — |
| [alexanderop/plausible-mcp](https://github.com/alexanderop/plausible-mcp) | 6 | TypeScript | 4 | API key | — |
| [The-Focus-AI/plausible-mcp](https://github.com/The-Focus-AI/plausible-mcp) | 1 | TypeScript | 2 | API key | MIT |

### Matomo

| Server | Stars | Language | Tools | Auth | License |
|--------|-------|----------|-------|------|---------|
| [FGRibreau/mcp-matomo](https://github.com/FGRibreau/mcp-matomo) | 10 | Rust | Dynamic | API token | MIT |
| [kitconcept/matomo-mcp](https://github.com/kitconcept/matomo-mcp) | 1 | Python | 6 | API token | MIT |
| [Jaimeapo/matomo-mcp](https://github.com/Jaimeapo/matomo-mcp) | — | TypeScript | — | API token | — |

### Hotjar (New)

| Server | Stars | Language | Tools | Auth | License |
|--------|-------|----------|-------|------|---------|
| [yasin749/hotjar-mcp-server](https://github.com/yasin749/hotjar-mcp-server) | 2 | TypeScript | — | OAuth | MIT |

### Microsoft Clarity

| Server | Stars | Language | Tools | Auth | License |
|--------|-------|----------|-------|------|---------|
| [microsoft/clarity-mcp-server](https://github.com/microsoft/clarity-mcp-server) | 81 | TypeScript | 3 | API token | MIT |

### Microsoft Fabric (BI/Analytics)

| Server | Stars | Language | Tools | Auth | License |
|--------|-------|----------|-------|------|---------|
| [santhoshravindran7/Fabric-Analytics-MCP](https://github.com/santhoshravindran7/Fabric-Analytics-MCP) | 110 | TypeScript | 52 | Bearer / Service Principal / Azure CLI | MIT |

### Microsoft Fabric Real-Time Intelligence (New)

| Server | Stars | Language | Tools | Auth | License |
|--------|-------|----------|-------|------|---------|
| [microsoft/fabric-rti-mcp](https://github.com/microsoft/fabric-rti-mcp) | 113 | Python | 30+ | Azure Identity | — |

The landscape splits into three tiers: enterprise platforms (Google Analytics, PostHog, Amplitude, Pendo, Mixpanel, Microsoft Clarity) with official servers, BI/data platforms (Microsoft Fabric community + official RTI) with growing coverage, and privacy-first alternatives (Plausible, Matomo) where Sentry's hosted Plausible MCP is starting to close the gap. Hotjar gets its first community server, though it's surveys-only.

---

## googleanalytics/google-analytics-mcp — The Official GA4 Server

[googleanalytics/google-analytics-mcp](https://github.com/googleanalytics/google-analytics-mcp) (2,000 stars, Apache 2.0) is Google's official MCP server for Google Analytics 4. Released in early 2026, it uses the GA4 Admin API and Data API. Stars crossed the 2K milestone — steady continued adoption.

**7 tools across three categories:**

- **Account/property retrieval** — get_account_summaries, get_property_details, get_custom_dimensions_and_metrics
- **Core reporting** — run_report (standard reports with dimensions, metrics, date ranges)
- **Real-time reporting** — run_realtime_report (live data)
- **Metadata** — list_google_ads_links (cross-platform advertising data)

**Read-only by design.** The server cannot edit your Google Analytics configuration or settings. This is a deliberate safety choice — analytics data is read-only, so the MCP server is read-only.

### What works well

**Official and active.** 2,000 stars, v0.2.0, 48 commits, active development. Google is promoting this alongside Gemini Code Assist and Gemini CLI integration. When Google invests in an MCP server, it gets maintained.

**Application Default Credentials.** Uses Google Cloud's ADC with the `analytics.readonly` scope. If you're already authenticated with `gcloud`, the server works immediately — no separate API key management. This is the cleanest auth model in the analytics MCP category.

**Natural language reporting.** The `run_report` tool accepts GA4 dimensions and metrics. An agent can translate "show me top landing pages by bounce rate for the last 30 days" into the correct API call. The `get_custom_dimensions_and_metrics` tool lets the agent discover what metrics are available for your property.

### What doesn't

**GA4-only.** Universal Analytics is dead, so this is less of a limitation than it sounds. But if you have legacy reporting needs, they're not supported.

**7 tools is thin.** Compare this to PostHog's 27+ tools or Amplitude's 24+. There's no funnel analysis, no cohort creation, no A/B test management, no audience building. It's a reporting server, not a full analytics platform interface.

**Google Cloud dependency.** You need a Google Cloud project and ADC credentials. For marketing teams who just want to query GA4 data, this setup is a barrier. The community server gomarble-ai uses OAuth with browser-based auth, which is friendlier for non-developers.

### Community alternatives

**surendranb/google-analytics-mcp** (205 stars) — 200+ GA4 dimensions and metrics with smart data volume management and context window protection. Designed for AI agent workflows with built-in row estimation to prevent query overflows. More thoughtful about LLM integration than the official server.

**gomarble-ai/google-analytics-mcp-server** (14 stars) — OAuth 2.0 with automatic token refresh. One-time browser authentication, then the server handles token lifecycle. Lower friction than ADC for non-technical users.

**ruchernchong/mcp-server-google-analytics** (70 stars) — archived October 2025. Was an early GA4 MCP server in JavaScript. No longer maintained.

---

## PostHog MCP — The All-in-One Product Analytics Server

[PostHog/posthog/services/mcp](https://github.com/PostHog/posthog/tree/master/services/mcp) (PostHog monorepo: 34,200 stars, MIT) is PostHog's official MCP server, hosted at `mcp.posthog.com/mcp`. Originally a standalone repo (archived January 2026), it lives in PostHog's monorepo at `services/mcp` and sees very active development. Monorepo stars grew from 32,700 to 34,200 (+5%).

**27+ tools spanning PostHog's full product suite:**

- **Analytics** — query insights, trends, funnels, retention
- **Feature flags** — create, retrieve, update flags (basic and multivariate)
- **Experiments** — manage A/B tests and feature experiments
- **Error tracking** — monitor errors, suppression rules, grouping rules
- **Prompts** — create, retrieve, update LLM prompt templates
- **Subscriptions** — test delivery, access delivery history (new April 2026)
- **CDP & workflows** — logging and metrics tools for monitoring (new April 2026)

**April 2026 developments:** PostHog migrated MCP tool definitions from hand-coded to a codegen pipeline — meaning new PostHog features can automatically become MCP tools. Added OAuth scope error surfacing, feature flag support for tool definitions, and enhanced "view in PostHog" links.

**Read-only mode available.** Restricts the server to query-only tools — no creating, updating, or deleting resources. Feature filtering via query parameters (e.g., `?features=flags,workspace`) lets you expose only the tool categories you need.

### What works well

**Broadest tool set.** 27+ tools covering analytics, feature flags, experiments, error tracking, and prompt management. No other analytics MCP server covers this breadth. PostHog is a platform, and the MCP server exposes the full platform.

**Multi-IDE installation.** `npx @posthog/wizard@latest mcp add` installs into Cursor, Claude Code, Claude Desktop, Codex, VS Code, and Zed with one command. This is the lowest-friction setup of any analytics MCP server.

**Open source and self-hostable.** PostHog itself is open source (MIT). The MCP server works with both PostHog Cloud and self-hosted instances. No vendor lock-in.

### What doesn't

**Monorepo move complicates contributions.** The standalone repo is archived. Contributing now means navigating PostHog's full monorepo (40,000+ commits). For a small bug fix or feature request, this raises the barrier.

**PostHog pricing structure.** PostHog Cloud has a generous free tier (1M events/month), but costs scale with usage. The MCP server makes it easier to query data, but PostHog's usage-based pricing means heavy agent usage of analytics queries could increase costs.

---

## Amplitude MCP — Enterprise-Grade Hosted Analytics (Major Expansion)

[Amplitude MCP](https://amplitude.com/mcp-server) is Amplitude's official hosted MCP server — a cloud endpoint, not a GitHub repo you self-host. Since our last review, Amplitude expanded massively beyond core analytics.

**24+ tools covering:**

- **Search & retrieval** — search content, retrieve objects from URLs, get charts/dashboards/cohorts/experiments
- **Analysis** — query charts, datasets, experiments, user data
- **Creation** — build charts, dashboards, notebooks, experiments, cohorts
- **Feedback** — access customer insights, comments, mentions
- **Session Replays** (new) — end-to-end qualitative analysis, replay debugging, friction indicators (rage clicks, dead clicks, user errors)
- **Agent Analytics** (new) — AI agent topic analysis, session investigation, quality monitoring
- **Feature Flags** (new) — flag management and monitoring
- **Web Vitals** (new) — reliability monitoring, error debugging via autocapture data

**MCP App** (new) — renders Amplitude charts directly inside AI clients like Claude and Cursor. Replaces raw query results with actual visualizations. This is unique — no other analytics MCP server renders charts in-client.

**Open-source skills repository** — [amplitude/mcp-marketplace](https://github.com/amplitude/mcp-marketplace) (22 stars, MIT, 48 commits) provides 27 pre-built agent skills organized into seven areas: core analytics, product insights, session replay/debugging, AI agent analytics, instrumentation, briefings, and bonus skills. Skills include `daily-brief`, `debug-replay`, `analyze-experiment`, `monitor-reliability`, and `what-would-lenny-do`. Works with Claude Code, Cursor, Codex, and Gemini CLI.

**Cloud-hosted with OAuth 2.0.** Available at `https://mcp.amplitude.com/mcp` (US) and a separate EU endpoint. Streaming HTTP transport. Quick-install support for Cursor, Claude, ChatGPT, Gemini CLI, Replit, Lovable, Figma Make, AWS Kiro, and more.

### What works well

**Broadest expansion of any analytics MCP.** Coverage went from analytics-only to Session Replays, Agent Analytics, Feature Flags, and Web Vitals. The Session Replay Agent automatically analyzes replays across funnels at scale, surfaces behavioral patterns and drop-offs, and backs each insight with curated replay playlists.

**Broadest client support.** Quick-install for 10+ AI clients. No other analytics MCP server supports this many integrations out of the box.

**Permission inheritance.** The MCP server uses your existing Amplitude user permissions. You only see projects and data you already have access to. No need to create separate API credentials or manage MCP-specific access control.

**Read and write.** Unlike Google Analytics MCP (read-only), Amplitude lets agents create charts, dashboards, cohorts, and experiments. An agent can go from "show me retention by country" to "create a dashboard with these metrics" in one conversation.

### What doesn't

**Closed source.** No GitHub repo for the server itself. You can't self-host, audit the code, or contribute. The mcp-marketplace skills repo is open source (MIT), but the server remains proprietary.

**Requires Amplitude subscription.** Available to "any existing Amplitude customer," but Amplitude's pricing starts at enterprise levels. There's a free Starter plan, but the MCP server's value increases with paid features (experiments, predictions, behavioral cohorts).

**No community fallback.** silviorodrigues/amplitude-mcp (9 stars, 2 tools) was **archived March 27, 2026** — the only community alternative is now read-only and unmaintained. If Amplitude's official hosted server doesn't meet your needs, there's no alternative.

---

## Mixpanel MCP — Beta Expanding to ChatGPT and Gemini

[Mixpanel MCP](https://docs.mixpanel.com/docs/features/mcp) is Mixpanel's official MCP server, announced August 2025 as a beta — now expanded to support ChatGPT and Gemini alongside Claude, Cursor, and Notion.

**Key capabilities:**

- Natural language queries to analytics data — events, funnels, flows, retention
- Session replays (new) — combine behavioral data with qualitative context
- Report generation
- Event and property definition access
- Cross-source data correlation
- Funnel and adoption metric exploration

**Target users:** Data analysts (reduce repetitive queries), product managers (explore funnels), non-technical teams (natural language access to insights).

### What works well

**Natural language focus.** Mixpanel emphasizes the "talk to your data" use case more than any other analytics MCP server. The goal is to let anyone — technical or not — ask questions like "what's the conversion rate for users who saw the onboarding flow?" and get answers without writing queries.

**Session replays added.** Teams can now analyze a specific user's replays in combination with event data, allowing AI interfaces to reason about what users did and how they experienced the product — combining behavioral data with qualitative context in a single workflow.

**Cross-source correlation.** The MCP server can combine Mixpanel data with external sources. Mixpanel highlights pulling order events from Mixpanel and merging with external purchase data to analyze revenue — something that normally requires a data warehouse and SQL.

**Multi-client support expanded.** Now works with Claude, ChatGPT, Gemini, Cursor, and Notion — significantly broader than the initial Claude-only beta.

### What doesn't

**Beta status.** Launched August 2025, still in beta. US data center only — EU and IN expansion planned but not yet available. Feature set may change.

**Community alternatives are small.** dragonkhoi/mixpanel-mcp (19 stars) covers event queries, retention, and funnels with Mixpanel Service Account auth. moonbirdai/mixpanel-mcp-server offers tracking events and user profiles. Neither has significant adoption.

---

## Pendo MCP — Product Analytics in Claude's Connectors Directory (New)

[Pendo MCP](https://www.pendo.io/product/mcp/) is Pendo's official hosted MCP server — the sixth analytics platform to ship an official MCP integration.

**Capabilities:**

- Visitor and account metadata queries
- Application analytics and user behavior analysis
- Page, feature, and track event data
- Event-level aggregation queries
- Visitor activity and engagement patterns

**Cloud-hosted with OAuth.** Available through Claude's official Connectors Directory, plus ChatGPT (developer mode), Cursor, VS Code with GitHub Copilot, and Claude Code. Any paid Pendo customer can access the MCP server — admin enablement required.

### Why it matters

Pendo brings product analytics to the MCP ecosystem from a platform focused on product-led growth. Where Google Analytics is web traffic and PostHog is engineering-centric, Pendo's strength is product management — feature adoption, user guides, NPS, and in-app messaging. The MCP server lets agents query this data via natural language without building reports.

### Limitations

**Paid customers only.** No free tier. Pendo's pricing is enterprise-oriented, so this MCP server has the highest barrier to entry in the category.

**Closed source.** Like Amplitude, no GitHub repo — you can't self-host or audit the code.

---

## The Privacy-First Gap: Plausible and Matomo (Partially Closing)

If you use privacy-first analytics, your MCP options have improved — Sentry built a Plausible MCP server with a hosted instance.

**Plausible:** The biggest change is **getsentry/plausible-mcp** (TypeScript, MIT, 23 commits, April 2026) — built by Sentry with a **hosted instance at `plausible-mcp.sentry.dev`**. Four tools: `get_timeseries` (traffic metrics over time), `get_breakdown` (segmentation by pages/sources/countries/devices), `get_conversions` (goal conversion rates), and `compare_periods` (side-by-side date range analysis). All read-only. Includes 53 tests and LLM evaluation. Also deployable to Cloudflare Workers for self-hosting. Having a company like Sentry build and host this is a significant credibility boost for the Plausible MCP ecosystem.

The-Focus-AI/plausible-mcp (1 star, MIT, 2 tools) adds 1Password integration for API key management. AVIMBU/plausible-mcp-server (7 stars) and alexanderop/plausible-mcp (6 stars, 4 tools) remain the original community options.

**Matomo:** FGRibreau/mcp-matomo (10 stars, Rust, MIT, 24 commits) remains the most interesting implementation with dynamic API introspection. kitconcept/matomo-mcp (1 star, Python, MIT, 6 tools) is a new addition covering site info, visit summaries, page URLs, geographic data, browser/device info, and custom API queries.

The gap is closing: Sentry's hosted Plausible server means privacy-first teams now have a production-quality option without building their own. Matomo gets a third implementation. Still no official servers from either platform, but the community is rallying.

---

## Microsoft Clarity MCP — Free Heatmaps and Session Recordings (New)

[microsoft/clarity-mcp-server](https://github.com/microsoft/clarity-mcp-server) (78 stars, MIT) is Microsoft's official MCP server for Clarity, their free web analytics tool focused on heatmaps and session recordings.

**3 tools:**

- **query-analytics-dashboard** — retrieve analytics metrics and traffic data
- **list-session-recordings** — access session recordings with filtering
- **query-documentation-resources** — search Clarity documentation

### Why it matters

**Free and official.** Clarity is a completely free analytics tool (no usage caps). Combined with an official MCP server from the `microsoft/` GitHub organization, this is the lowest-cost entry point for analytics MCP integration. 81 stars and 52 commits show active development.

**Session recordings are unique.** No other analytics MCP server exposes session recording data. An AI agent can search for specific user sessions — useful for debugging UX issues or understanding user behavior patterns that aggregate metrics miss.

### Limitations

**Narrow scope.** 3 tools compared to PostHog's 27+ or Amplitude's 24+. Clarity is intentionally focused on behavioral analytics (heatmaps, recordings, rage clicks), not product analytics (funnels, cohorts, A/B tests). The MCP server reflects this narrow scope.

**No self-hosting.** Clarity is a cloud-only service. Unlike PostHog or Matomo, you can't run it on your own infrastructure.

---

## Microsoft Fabric Analytics MCP — BI Platform Access (Now Two Servers)

[santhoshravindran7/Fabric-Analytics-MCP](https://github.com/santhoshravindran7/Fabric-Analytics-MCP) (110 stars, MIT) is a community server connecting AI agents to Microsoft Fabric, Microsoft's unified analytics and BI platform.

**52 tools** covering workspace management, notebook execution, Spark sessions via Livy API, and Synapse-to-Fabric migration. This is more of a BI/data platform server than a traditional web analytics server, but it fills a gap for teams using Microsoft's analytics stack. Multiple auth methods (Bearer token, Service Principal, Device Code, Azure CLI) make it enterprise-ready.

**New: microsoft/fabric-rti-mcp** (113 stars, Python, public preview) is Microsoft's official MCP server for Fabric Real-Time Intelligence. 30+ tools: 13 for Eventhouse/Kusto KQL queries, 17 for Eventstream management, plus Activator alerts and Map visualization. Uses Azure Identity authentication. This is the second MCP server from the `microsoft/` GitHub organization in the analytics space (alongside Clarity), and brings real-time data streaming and KQL query capabilities to AI agents.

---

## Hotjar MCP — Surveys Only (New)

[yasin749/hotjar-mcp-server](https://github.com/yasin749/hotjar-mcp-server) (2 stars, TypeScript, MIT, 3 commits) is the first community MCP server for Hotjar. Currently surveys-only — it can retrieve and manage Hotjar survey data via OAuth client credentials. No heatmap or session recording access yet. Very early stage, but it establishes that the Hotjar MCP gap is starting to be addressed.

---

## The cross-platform comparison

| Feature | Google Analytics | PostHog | Amplitude | Pendo | Mixpanel | MS Clarity | Plausible | Matomo |
|---------|-----------------|---------|-----------|-------|----------|------------|-----------|--------|
| Official server | **Yes** | **Yes** | **Yes** | **Yes** | **Yes** (beta) | **Yes** | No (Sentry-built) | No |
| Stars (GitHub) | 2,000 | 34,200 (mono) | — (hosted) | — (hosted) | — (hosted) | 81 | — (hosted) | 10 |
| Tools | 7 | 27+ | 24+ | — | — | 3 | 4 | Dynamic |
| Read/write | Read-only | **Read + write** | **Read + write** | Read-only | Read + write | Read-only | Read-only | Read-only |
| Self-hostable | **Yes** | **Yes** | No | No | No | No | **Yes** (Sentry) | **Yes** |
| Auth model | ADC / Service account | API key / OAuth | OAuth 2.0 | OAuth 2.0 | OAuth | API token | API key | API token |
| Hosted endpoint | No | **Yes** | **Yes** | **Yes** | **Yes** | No | **Yes** (Sentry) | No |
| Feature flags | No | **Yes** | **Yes** (new) | No | No | No | No | No |
| A/B testing | No | **Yes** | **Yes** | No | No | No | No | No |
| Session recordings | No | **Yes** | **Yes** (new) | No | **Yes** (new) | **Yes** | No | No |
| In-client charts | No | No | **Yes** (new) | No | No | No | No | No |
| Free tier | **Yes** (GA4 free) | **Yes** (1M events) | Limited | No | Limited | **Yes** (free) | No (paid) | **Yes** (self-hosted) |

## Which one should you use?

**Using Google Analytics?** Start with the [official google-analytics-mcp](https://github.com/googleanalytics/google-analytics-mcp). 2,000 stars, active development, read-only safety. If you want friendlier auth, try gomarble-ai's OAuth-based server. If you need smarter LLM integration, surendranb's server has better context management.

**Using PostHog?** The official MCP server is the clear choice. 27+ tools covering the full platform, read-only mode for safety, one-command installation. The broadest analytics MCP integration available.

**On Amplitude?** Use the [hosted MCP endpoint](https://amplitude.com/mcp-server). The biggest expansion in the category — now covers Session Replays, Agent Analytics, Feature Flags, Web Vitals, plus in-client chart rendering and 27 open-source agent skills. No self-hosting option, but the most feature-rich analytics MCP experience.

**On Pendo?** Use the [official Pendo MCP](https://www.pendo.io/product/mcp/) — available in Claude's Connectors Directory. OAuth 2.0, natural language queries to product analytics. Paid customers only.

**On Mixpanel?** Try the [official beta MCP server](https://docs.mixpanel.com/docs/features/mcp). Now supports ChatGPT, Gemini, Cursor, and Notion alongside Claude. Session replays added. US data center only for now.

**Want free behavioral analytics?** Microsoft's [clarity-mcp-server](https://github.com/microsoft/clarity-mcp-server) is official, free (no usage caps), and gives agents access to heatmaps and session recordings. Narrow scope (3 tools), but zero cost.

**Using Plausible?** The landscape improved significantly. Sentry built and hosts [getsentry/plausible-mcp](https://github.com/getsentry/plausible-mcp) with a production instance at `plausible-mcp.sentry.dev` — 4 tools for time series, breakdowns, conversions, and period comparison. Also self-deployable to Cloudflare Workers.

**Using Matomo?** FGRibreau/mcp-matomo's dynamic API introspection covers the full Matomo API. kitconcept/matomo-mcp adds a Python alternative with 6 explicit tools.

## Security considerations

Analytics MCP servers are lower-risk than most categories — analytics data is typically read-only and non-destructive. But there are still concerns:

- **Data exposure.** Analytics data can reveal business metrics, user behavior patterns, and revenue figures. Scope access to the properties and projects that agents actually need.
- **Write operations.** PostHog and Amplitude MCP servers can create experiments, modify feature flags, and build dashboards. Use read-only modes where available, especially for monitoring agents.
- **API costs.** Heavy querying through MCP can increase API usage. Amplitude and Mixpanel have usage-based pricing; automated agent queries can add up.
- **PII concerns.** Some analytics platforms store user-level data. Ensure your analytics configuration doesn't expose personally identifiable information through MCP queries.

## The verdict

**Rating: 4/5** (up from 3.5) — The analytics MCP ecosystem has the strongest vendor adoption of any MCP category and it widened its lead — six platforms now have official servers (Google Analytics, PostHog, Amplitude, Pendo, Mixpanel, Microsoft Clarity), plus two official Microsoft servers for Fabric (Clarity + RTI). Amplitude's expansion from analytics-only to Session Replays, Agent Skills, Feature Flags, Web Vitals, and in-client chart rendering sets a new bar for what an analytics MCP integration can be.

What works: Google Analytics crossed 2,000 stars. PostHog offers the broadest tool set (27+ tools, 34.2K monorepo stars) with an automated codegen pipeline. Amplitude is now the most feature-rich — 24+ tools plus Session Replay Agent, 27 open-source skills, and MCP App for in-client visualizations. Pendo enters as the sixth official vendor, available in Claude's Connectors Directory. Mixpanel expanded its beta to ChatGPT and Gemini with session replay support. Microsoft ships two official servers (Clarity free, Fabric RTI with 30+ tools). Sentry built and hosts a Plausible MCP server, partially closing the privacy-first gap.

What holds it back: the privacy-first alternatives still lack official support (Sentry's Plausible server is community-built, not Plausible official). Hotjar gets its first server but it's surveys-only (2 stars, 3 commits). The hosted servers (Amplitude, Pendo, Mixpanel) remain closed-source. Google Analytics' 7 read-only tools look increasingly thin compared to Amplitude's expanding feature set.

The strongest individual server is Amplitude's — broadest feature set with Session Replays, Agent Skills, in-client charts, and the most AI client integrations. PostHog remains the best open-source option — broadest tool set, self-hostable, codegen-powered expansion. The most accessible is Google Analytics (free GA4, 2,000 stars, read-only safety). The lowest-cost entry point is Microsoft Clarity (completely free, official). The biggest newcomer is Pendo (official, Claude Connectors). The most improved privacy-first option is Sentry's hosted Plausible MCP.

*Reviewed by [ChatForest](https://chatforest.com). We research MCP servers by reading source code, documentation, GitHub issues, and community discussions. For our methodology, see [How We Review](/about/).*

*This review was last updated on 2026-04-29 using Claude Opus 4.6 (Anthropic).*
