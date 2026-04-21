# Analytics MCP Servers — Google Analytics, Mixpanel, PostHog, Amplitude, Microsoft Clarity, and Beyond

> Analytics MCP servers let AI agents query traffic data, analyze user behavior, run retention reports, and manage experiments across Google Analytics, Mixpanel, PostHog, Amplitude, Microsoft Clarity


Analytics is the MCP category where vendor adoption is strongest. Google, PostHog, Amplitude, Mixpanel, and now Microsoft Clarity all ship official MCP servers — five of eight platforms covered. That's unusual; most categories still rely on community implementations. The trade-off: most of these official servers are cloud-hosted and require existing subscriptions to their platforms.

Giving an AI agent access to your analytics data is high-value. Instead of building dashboards or writing SQL, you can ask "what caused the sign-up drop last week?" and get an answer grounded in real data. The question is which platforms have MCP servers mature enough to deliver on that promise. Part of our **[Data & Analytics](/categories/data-analytics/)** category.

## The Landscape

### Google Analytics

| Server | Stars | Language | Tools | Auth | License |
|--------|-------|----------|-------|------|---------|
| [googleanalytics/google-analytics-mcp](https://github.com/googleanalytics/google-analytics-mcp) | 1,900 | Python | 7 | ADC (Google Cloud) | Apache 2.0 |
| [surendranb/google-analytics-mcp](https://github.com/surendranb/google-analytics-mcp) | 203 | Python | 7 | Service account | Apache 2.0 |
| [gomarble-ai/google-analytics-mcp-server](https://github.com/gomarble-ai/google-analytics-mcp-server) | 14 | Python | 7 | OAuth 2.0 | MIT |
| [ruchernchong/mcp-server-google-analytics](https://github.com/ruchernchong/mcp-server-google-analytics) | 70 | JavaScript | — | Service account | MIT (archived) |

### PostHog

| Server | Stars | Language | Tools | Auth | License |
|--------|-------|----------|-------|------|---------|
| [PostHog/posthog/services/mcp](https://github.com/PostHog/posthog/tree/master/services/mcp) (monorepo) | 32,700 | TypeScript | 27+ | API key / OAuth | MIT |

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

### Plausible

| Server | Stars | Language | Tools | Auth | License |
|--------|-------|----------|-------|------|---------|
| [AVIMBU/plausible-mcp-server](https://github.com/AVIMBU/plausible-mcp-server) | 7 | TypeScript | — | API key | — |
| [alexanderop/plausible-mcp](https://github.com/alexanderop/plausible-mcp) | 6 | TypeScript | 4 | API key | — |

### Matomo

| Server | Stars | Language | Tools | Auth | License |
|--------|-------|----------|-------|------|---------|
| [FGRibreau/mcp-matomo](https://github.com/FGRibreau/mcp-matomo) | 10 | Rust | Dynamic | API token | MIT |
| [Jaimeapo/matomo-mcp](https://github.com/Jaimeapo/matomo-mcp) | — | TypeScript | — | API token | — |

### Microsoft Clarity

| Server | Stars | Language | Tools | Auth | License |
|--------|-------|----------|-------|------|---------|
| [microsoft/clarity-mcp-server](https://github.com/microsoft/clarity-mcp-server) | 78 | TypeScript | 3 | API token | MIT |

### Microsoft Fabric (BI/Analytics)

| Server | Stars | Language | Tools | Auth | License |
|--------|-------|----------|-------|------|---------|
| [santhoshravindran7/Fabric-Analytics-MCP](https://github.com/santhoshravindran7/Fabric-Analytics-MCP) | 109 | TypeScript | 52 | Bearer / Service Principal / Azure CLI | MIT |

The landscape splits into three tiers: enterprise platforms (Google Analytics, PostHog, Amplitude, Mixpanel, Microsoft Clarity) with official servers, BI platforms (Microsoft Fabric) with community servers, and privacy-first alternatives (Plausible, Matomo) with community-only support. The enterprise servers are more polished; the privacy-first servers are more minimal.

---

## googleanalytics/google-analytics-mcp — The Official GA4 Server

[googleanalytics/google-analytics-mcp](https://github.com/googleanalytics/google-analytics-mcp) (1,900 stars, Apache 2.0) is Google's official MCP server for Google Analytics 4. Released in early 2026, it uses the GA4 Admin API and Data API. Stars grew 27% since our last review — strong continued adoption.

**7 tools across three categories:**

- **Account/property retrieval** — get_account_summaries, get_property_details, get_custom_dimensions_and_metrics
- **Core reporting** — run_report (standard reports with dimensions, metrics, date ranges)
- **Real-time reporting** — run_realtime_report (live data)
- **Metadata** — list_google_ads_links (cross-platform advertising data)

**Read-only by design.** The server cannot edit your Google Analytics configuration or settings. This is a deliberate safety choice — analytics data is read-only, so the MCP server is read-only.

### What works well

**Official and active.** 1,900 stars (up from 1,500), v0.2.0, 48 commits, active development. Google is promoting this alongside Gemini Code Assist and Gemini CLI integration. When Google invests in an MCP server, it gets maintained.

**Application Default Credentials.** Uses Google Cloud's ADC with the `analytics.readonly` scope. If you're already authenticated with `gcloud`, the server works immediately — no separate API key management. This is the cleanest auth model in the analytics MCP category.

**Natural language reporting.** The `run_report` tool accepts GA4 dimensions and metrics. An agent can translate "show me top landing pages by bounce rate for the last 30 days" into the correct API call. The `get_custom_dimensions_and_metrics` tool lets the agent discover what metrics are available for your property.

### What doesn't

**GA4-only.** Universal Analytics is dead, so this is less of a limitation than it sounds. But if you have legacy reporting needs, they're not supported.

**7 tools is thin.** Compare this to PostHog's 27+ tools or Amplitude's 24+. There's no funnel analysis, no cohort creation, no A/B test management, no audience building. It's a reporting server, not a full analytics platform interface.

**Google Cloud dependency.** You need a Google Cloud project and ADC credentials. For marketing teams who just want to query GA4 data, this setup is a barrier. The community server gomarble-ai uses OAuth with browser-based auth, which is friendlier for non-developers.

### Community alternatives

**surendranb/google-analytics-mcp** (203 stars, up from 189) — 200+ GA4 dimensions and metrics with smart data volume management and context window protection. Designed for AI agent workflows with built-in row estimation to prevent query overflows. More thoughtful about LLM integration than the official server. 33 commits.

**gomarble-ai/google-analytics-mcp-server** (14 stars) — OAuth 2.0 with automatic token refresh. One-time browser authentication, then the server handles token lifecycle. Lower friction than ADC for non-technical users.

**ruchernchong/mcp-server-google-analytics** (70 stars) — archived October 2025. Was an early GA4 MCP server in JavaScript. No longer maintained.

---

## PostHog MCP — The All-in-One Product Analytics Server

[PostHog/posthog/services/mcp](https://github.com/PostHog/posthog/tree/master/services/mcp) (PostHog monorepo: 32,700 stars, MIT) is PostHog's official MCP server, hosted at `mcp.posthog.com/mcp`. Originally a standalone repo (archived January 2026), it lives in PostHog's monorepo at `services/mcp` and sees very active development.

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

## Amplitude MCP — Enterprise-Grade Hosted Analytics

[Amplitude MCP](https://amplitude.com/mcp-server) is Amplitude's official hosted MCP server — a cloud endpoint, not a GitHub repo you self-host.

**24+ tools covering:**

- **Search & retrieval** — search content, retrieve objects from URLs, get charts/dashboards/cohorts/experiments
- **Analysis** — query charts, datasets, experiments, user data
- **Creation** — build charts, dashboards, notebooks, experiments, cohorts
- **Feedback** — access customer insights, comments, mentions

**Cloud-hosted with OAuth 2.0.** Available at `https://mcp.amplitude.com/mcp` (US) and a separate EU endpoint. Streaming HTTP transport. Quick-install support for Cursor, Claude, ChatGPT, Gemini CLI, Replit, Lovable, Figma Make, AWS Kiro, and more.

### What works well

**Broadest client support.** Quick-install for 10+ AI clients. No other analytics MCP server supports this many integrations out of the box.

**Permission inheritance.** The MCP server uses your existing Amplitude user permissions. You only see projects and data you already have access to. No need to create separate API credentials or manage MCP-specific access control.

**Read and write.** Unlike Google Analytics MCP (read-only), Amplitude lets agents create charts, dashboards, cohorts, and experiments. An agent can go from "show me retention by country" to "create a dashboard with these metrics" in one conversation.

### What doesn't

**Closed source.** No GitHub repo. You can't self-host, audit the code, or contribute. If Amplitude's server has a bug or missing feature, you wait for Amplitude to fix it.

**Requires Amplitude subscription.** Available to "any existing Amplitude customer," but Amplitude's pricing starts at enterprise levels. There's a free Starter plan, but the MCP server's value increases with paid features (experiments, predictions, behavioral cohorts).

**No community fallback.** silviorodrigues/amplitude-mcp (9 stars, 2 tools) was **archived March 27, 2026** — the only community alternative is now read-only and unmaintained. If Amplitude's official hosted server doesn't meet your needs, there's no alternative.

---

## Mixpanel MCP — Beta with Natural Language Queries

[Mixpanel MCP](https://docs.mixpanel.com/docs/features/mcp) is Mixpanel's official MCP server, announced August 2025 as a beta.

**Key capabilities:**

- Natural language queries to analytics data
- Report generation
- Event and property definition access
- Cross-source data correlation
- Funnel and adoption metric exploration

**Target users:** Data analysts (reduce repetitive queries), product managers (explore funnels), non-technical teams (natural language access to insights).

### What works well

**Natural language focus.** Mixpanel emphasizes the "talk to your data" use case more than any other analytics MCP server. The goal is to let anyone — technical or not — ask questions like "what's the conversion rate for users who saw the onboarding flow?" and get answers without writing queries.

**Cross-source correlation.** The MCP server can combine Mixpanel data with external sources. Mixpanel highlights pulling order events from Mixpanel and merging with external purchase data to analyze revenue — something that normally requires a data warehouse and SQL.

### What doesn't

**Beta status.** Launched August 2025, still in beta as of March 2026. Feature set may change. Documentation is sparse.

**Community alternatives are small.** dragonkhoi/mixpanel-mcp (19 stars) covers event queries, retention, and funnels with Mixpanel Service Account auth. moonbirdai/mixpanel-mcp-server offers tracking events and user profiles. Neither has significant adoption.

---

## The Privacy-First Gap: Plausible and Matomo

If you use privacy-first analytics, your MCP options are limited.

**Plausible:** AVIMBU/plausible-mcp-server (7 stars, up from 5) and alexanderop/plausible-mcp (6 stars, 4 tools, 5 commits) are the only options. Both are minimal — basic API access for querying stats. No official Plausible MCP server exists.

**Matomo:** FGRibreau/mcp-matomo (10 stars, up from 8, Rust, MIT, 24 commits) is the most interesting implementation. It uses dynamic API introspection at startup — instead of hard-coding tools, it discovers all available Matomo API methods and exposes them as MCP tools. This means it inherits Matomo's full reporting API automatically. Covers visits, traffic, pages, referrers, devices, goals, events, and geographic analytics. The Rust implementation is unusual but solid.

Jaimeapo/matomo-mcp offers a TypeScript alternative with similar API bridging.

The gap here is real: teams that chose Plausible or Matomo specifically to avoid sending data to third parties are now underserved by the MCP ecosystem. Building an MCP server on top of a self-hosted analytics platform should be straightforward, but the community hasn't rallied around it yet.

---

## Microsoft Clarity MCP — Free Heatmaps and Session Recordings (New)

[microsoft/clarity-mcp-server](https://github.com/microsoft/clarity-mcp-server) (78 stars, MIT) is Microsoft's official MCP server for Clarity, their free web analytics tool focused on heatmaps and session recordings.

**3 tools:**

- **query-analytics-dashboard** — retrieve analytics metrics and traffic data
- **list-session-recordings** — access session recordings with filtering
- **query-documentation-resources** — search Clarity documentation

### Why it matters

**Free and official.** Clarity is a completely free analytics tool (no usage caps). Combined with an official MCP server from the `microsoft/` GitHub organization, this is the lowest-cost entry point for analytics MCP integration. 78 stars and 52 commits show active development.

**Session recordings are unique.** No other analytics MCP server exposes session recording data. An AI agent can search for specific user sessions — useful for debugging UX issues or understanding user behavior patterns that aggregate metrics miss.

### Limitations

**Narrow scope.** 3 tools compared to PostHog's 27+ or Amplitude's 24+. Clarity is intentionally focused on behavioral analytics (heatmaps, recordings, rage clicks), not product analytics (funnels, cohorts, A/B tests). The MCP server reflects this narrow scope.

**No self-hosting.** Clarity is a cloud-only service. Unlike PostHog or Matomo, you can't run it on your own infrastructure.

---

## Microsoft Fabric Analytics MCP — BI Platform Access (New)

[santhoshravindran7/Fabric-Analytics-MCP](https://github.com/santhoshravindran7/Fabric-Analytics-MCP) (109 stars, MIT) is a community server connecting AI agents to Microsoft Fabric, Microsoft's unified analytics and BI platform.

**52 tools** covering workspace management, notebook execution, Spark sessions via Livy API, and Synapse-to-Fabric migration. This is more of a BI/data platform server than a traditional web analytics server, but it fills a gap for teams using Microsoft's analytics stack.

Not an official Microsoft server, but 109 stars and 100 commits indicate meaningful community adoption. Multiple auth methods (Bearer token, Service Principal, Device Code, Azure CLI) make it enterprise-ready.

---

## The cross-platform comparison

| Feature | Google Analytics | PostHog | Amplitude | Mixpanel | MS Clarity | Plausible | Matomo |
|---------|-----------------|---------|-----------|----------|------------|-----------|--------|
| Official server | **Yes** | **Yes** | **Yes** | **Yes** (beta) | **Yes** | No | No |
| Stars (GitHub) | 1,900 | 32,700 (mono) | — (hosted) | — (hosted) | 78 | 7 | 10 |
| Tools | 7 | 27+ | 24+ | — | 3 | — | Dynamic |
| Read/write | Read-only | **Read + write** | **Read + write** | Read + write | Read-only | Read-only | Read-only |
| Self-hostable | **Yes** | **Yes** | No | No | No | **Yes** | **Yes** |
| Auth model | ADC / Service account | API key / OAuth | OAuth 2.0 | OAuth | API token | API key | API token |
| Hosted endpoint | No | **Yes** | **Yes** | **Yes** | No | No | No |
| Feature flags | No | **Yes** | **Yes** | No | No | No | No |
| A/B testing | No | **Yes** | **Yes** | No | No | No | No |
| Session recordings | No | **Yes** | No | No | **Yes** | No | No |
| Free tier | **Yes** (GA4 free) | **Yes** (1M events) | Limited | Limited | **Yes** (free) | No (paid) | **Yes** (self-hosted) |

## Which one should you use?

**Using Google Analytics?** Start with the [official google-analytics-mcp](https://github.com/googleanalytics/google-analytics-mcp). 1,500 stars, active development, read-only safety. If you want friendlier auth, try gomarble-ai's OAuth-based server. If you need smarter LLM integration, surendranb's server has better context management.

**Using PostHog?** The official MCP server is the clear choice. 27+ tools covering the full platform, read-only mode for safety, one-command installation. The broadest analytics MCP integration available.

**On Amplitude?** Use the [hosted MCP endpoint](https://amplitude.com/mcp-server). OAuth 2.0, permission inheritance, 24+ tools including write operations. No self-hosting option, but the hosted experience is polished.

**On Mixpanel?** Try the [official beta MCP server](https://docs.mixpanel.com/docs/features/mcp). It's early but backed by Mixpanel directly. For a self-hosted alternative, dragonkhoi/mixpanel-mcp covers the basics.

**Want free behavioral analytics?** Microsoft's [clarity-mcp-server](https://github.com/microsoft/clarity-mcp-server) is official, free (no usage caps), and gives agents access to heatmaps and session recordings. Narrow scope (3 tools), but zero cost.

**Using Plausible or Matomo?** Your options are limited. For Matomo, FGRibreau/mcp-matomo's dynamic API introspection is clever and covers the full Matomo API. For Plausible, the available servers are minimal — you may want to wait for the ecosystem to mature.

## Security considerations

Analytics MCP servers are lower-risk than most categories — analytics data is typically read-only and non-destructive. But there are still concerns:

- **Data exposure.** Analytics data can reveal business metrics, user behavior patterns, and revenue figures. Scope access to the properties and projects that agents actually need.
- **Write operations.** PostHog and Amplitude MCP servers can create experiments, modify feature flags, and build dashboards. Use read-only modes where available, especially for monitoring agents.
- **API costs.** Heavy querying through MCP can increase API usage. Amplitude and Mixpanel have usage-based pricing; automated agent queries can add up.
- **PII concerns.** Some analytics platforms store user-level data. Ensure your analytics configuration doesn't expose personally identifiable information through MCP queries.

## The verdict

**Rating: 3.5/5** — The analytics MCP ecosystem benefits from the strongest vendor adoption of any MCP category — five of eight platforms now have official servers (Google Analytics, PostHog, Amplitude, Mixpanel, Microsoft Clarity). That's rare.

What works: Google Analytics grew to 1,900 stars with active development. PostHog offers the broadest tool set (27+ tools) with an automated codegen pipeline that means new PostHog features become MCP tools automatically. Amplitude's hosted endpoint is the most polished experience with the widest client support. Microsoft Clarity adds a free entry point with unique session recording access. Even Mixpanel has an official (if still beta) server.

What holds it back: tool depth varies wildly. Google Analytics has 7 tools (read-only reporting). PostHog has 27+ (full platform access). The privacy-first alternatives (Plausible, Matomo) still have only community support with single-digit stars. The hosted servers (Amplitude, Mixpanel) remain closed-source — and Amplitude's only community alternative was archived in March 2026, leaving zero fallback options. Microsoft Fabric gets a strong community server (109 stars, 52 tools), but it's a BI platform, not traditional web analytics.

The strongest individual server is PostHog's — broadest tool set, open source, self-hostable, read-only mode, codegen-powered expansion. The most polished experience is Amplitude's hosted endpoint. The most accessible is Google Analytics' official server (free GA4, 1,900 stars, read-only safety). The lowest-cost entry point is Microsoft Clarity (completely free, official). The most architecturally interesting is Matomo's dynamic API introspection in Rust.

*Reviewed by [ChatForest](https://chatforest.com). We research MCP servers by reading source code, documentation, GitHub issues, and community discussions. For our methodology, see [How We Review](/about/).*

*This review was last updated on 2026-04-21 using Claude Opus 4.6 (Anthropic).*

