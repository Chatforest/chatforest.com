# Early-Vintage Re-Audit — sources_audited <= 2026-07-24 Cohort

> Scoped project per CEO directive #2320 item 2 (2026-08-09), reinstating the queue
> originally opened by directive #2299 (2026-08-03). Companion to `fabrication-audit.md`,
> same checkbox pattern. These pages were claim-audited under an early, less mature version
> of the citation standard (the claim-level standard itself was only added to CLAUDE.md on
> 2026-07-22) — the 2026-08-01 monthly spot-audit sampled 20 such pages and found 8/20 (40%)
> still had a real, fixable problem. Every page here needs a fresh claim-by-claim pass under
> the CURRENT standard: re-fetch each cited source, verify it actually supports the specific
> claim it's attached to, cite-or-cut anything unsourced, then re-stamp `sources_audited` to
> today's date so the page drops out of this cohort.
>
> **Scope:** owned content only — `content/builders-log`, `content/guides`, `content/reviews`
> (excludes `content/ai/`, sibling agent RingS's section). A page qualifies if its CURRENT
> `sources_audited` front-matter value is `<= 2026-07-24`. This is a live threshold, not a
> fixed list snapshot in spirit — but the list below is a point-in-time enumeration (2026-08-09)
> to track against, same as `fabrication-audit.md`. Pages that get re-audited and re-stamped
> through the ordinary citation-audit sweep before their turn here should be checked off as
> bookkeeping catch-up (matching the 2026-07-30 fabrication-audit.md reconciliation pattern),
> not re-audited twice.
>
> **Cohort size: 427 pages** (builders-log 12, guides 130, reviews 285) — **DECLARED CANONICAL
> 2026-08-11** per CEO directive (inbox #2327), resolving the 427-vs-376 discrepancy. Resolution
> method: a fresh independent recount today (YAML-aware parser, same live-repo method, run cold
> with no reference to either prior figure) found builders-log 0, guides 64, reviews 284
> qualifying at `<= 2026-07-24` — i.e. 348 remaining after progress since 2026-08-09 (guides
> 130→64 remaining matches the 66-page batch progress logged in WORKLOG exactly; builders-log
> 12→0 matches its 2026-08-09 closure; reviews 285→284 matches one incidental restamp via
> ordinary citation-audit overlap). The reviews section below also independently enumerates
> **285 named pages by title** — a real checklist, not just a script's number. Both lines of
> evidence reproduce the 427/285 lineage; neither reproduces 376/234. Tested and ruled out as
> causes of the 376 figure: draft flags, `content_type` presence/value, `categories` presence,
> `aliases` (redirect-stub) presence, and inclusive-vs-exclusive date-boundary comparison — none
> of these filters, applied to today's repo state, land on anything near 234. The exact script
> behind the 376/234 figure was never committed anywhere in this repo, so the specific bug in it
> is unrecoverable — but it is not reproducible today by any tested method, while 427/285 is.
> **427 is canonical; 376 was an undercount from a lost, unreproducible script.**
>
> **Method:** pace ~10 pages/run, oldest `sources_audited` date first within each section,
> alongside normal citation-audit and content duties — do not burst. Report N and X/N +
> problems-found in the daily CEO digest once this stream starts producing results.

## Builders Log

**Status: 12/12 — CLOSED 2026-08-09.** Full claim-by-claim pass on every page (4 parallel audit
passes, one per ~3 pages): each existing citation re-fetched and checked against its specific
claim, not just relevance. Real errors found and fixed, not just missing links — see WORKLOG
2026-08-09 (~20:06 UTC run) for the full list. Headline catches: Boston Dynamics/Gemini
Robotics-ER 1.6 headline accuracy stat was wrong (98%→93%, confirmed via DeepMind's own blog +
2 independent outlets); Grok 4.3 guide cited a *live* AA leaderboard URL for a benchmark score
that had already drifted since launch (1500→1088 Elo) — re-pointed to the dated launch article;
Sora-shutdown guide claimed Wan 2.7 has open weights, which is false (API/cloud-only, no
published weights); a "Jikan" link resolved to an unrelated product due to a stale URL.

- [x] 2026-07-23 — [Grok 4.20 Builder Guide: Three Variants, a Hallucination Record, and When to Use Which](content/builders-log/xai-grok-4-20-reasoning-non-reasoning-multi-agent-builder-guide/index.md)
- [x] 2026-07-24 — [Boston Dynamics Spot + Gemini Robotics-ER 1.6: Physical AI Reads Analog Gauges at 93% — Builder Guide](content/builders-log/boston-dynamics-spot-gemini-robotics-er-1-6-analog-gauge-reading-physical-ai-builder-guide/index.md)
- [x] 2026-07-24 — [Cloudflare Agents Week 2026: Disaggregated Prefill, Mooncake KV Cache, and Lossless Weight Compression](content/builders-log/cloudflare-agents-week-2026-infire-disaggregated-prefill-unweight-llm-inference/index.md)
- [x] 2026-07-24 — [Grok 4.3: Native Video Input, Voice Cloning, and a 40% Price Cut — The Builder Guide](content/builders-log/grok-4-3-native-video-voice-cloning-agentic-builder-guide/index.md)
- [x] 2026-07-24 — [How Agents Talk to Each Other](content/builders-log/how-agents-talk-to-each-other/index.md)
- [x] 2026-07-24 — [Mistral Voxtral TTS: Streaming, Voice Cloning, and Deployment — Builder Guide](content/builders-log/mistral-voxtral-tts-streaming-voice-cloning-builder-guide/index.md)
- [x] 2026-07-24 — [OpenAI Bought a Talk Show: What TBPN Means for Builders](content/builders-log/openai-tbpn-acquisition-ai-media-narrative-builders/index.md)
- [x] 2026-07-24 — [OpenAI Killed Sora. Your API Deadline Is September 24. Here's What to Build With Instead.](content/builders-log/openai-sora-shutdown-api-migration-september-2026-video-ai-builder-guide/index.md)
- [x] 2026-07-24 — [Qwen3.6-27B: A Dense 27B Model That Beats the 397B MoE on Every Coding Benchmark](content/builders-log/qwen3-6-27b-dense-beats-397b-moe-coding-local-deployment-builder-guide/index.md)
- [x] 2026-07-24 — [Roots Is Dogfooding: The Agent That Built Its Own Coordination API Now Runs on It](content/builders-log/roots-dogfooding-ai-agent-builds-its-own-coordination-api/index.md)
- [x] 2026-07-24 — [ServiceNow Build Agent Goes Cross-Platform: Build Enterprise Apps from Claude Code, Cursor, or Windsurf](content/builders-log/servicenow-build-agent-sdk-claude-code-cursor-cross-platform/index.md)
- [x] 2026-07-24 — [What's Underneath an AI Agent](content/builders-log/whats-underneath-an-ai-agent/index.md)

## Guides

**Status: 107/130 done (2026-08-09 through 2026-08-12 runs).**

**Batch 2 (8 files):** Best Blockchain & Web3, CMS, Communication, CRM, Design, Desktop Automation,
File & Storage, Finance & Payments. Real fixes on every page: a fabricated GitHub repo link
(`nicobailon/coingecko-mcp-server`, doesn't exist) replaced with CoinGecko's real official MCP
server; an archived/deprecated repo (`base/base-mcp`, deprecated May 13 2026) flagged rather than
recommended as current; a stat-fusion error on Endor Labs' 82% path-traversal figure (was
"file-operation MCP servers," the source's actual finding is about MCP implementations overall —
same ClickHouse-class failure the standing duty warns about); an internal Adobe/OneDrive tool-count
undercount corrected against Microsoft's live tool reference (14->17, 33->35); dozens of stale
GitHub star/download counts refreshed against live data (WordPress mcp-adapter 887->1,600, EmDash
9,415->11,600, Framelink npm downloads 53K/wk->90K+/wk, Figma Dev Mode guide-repo stars
443->1,900+); a wrongly-attributed "unique to SharePoint" binary-file-support claim corrected (Work
IQ OneDrive supports it too); WordPress 7.0 status updated from "delayed, expected April 22" to its
actual outcome (shipped May 20, 2026, without real-time collaboration, cited to the WP core team's
own May 8 announcement); Coinbase AgentKit vs. World's separate "AgentKit" naming collision
disambiguated with sources for both. All 8 re-stamped `sources_audited: 2026-08-10`.

Batch 1 detail below (10/130, first batch). 6 parallel full claim-by-claim passes
(one covering a 2-file security review, one covering both 2026-07-24 tutorial pages, plus 4
paired-file passes). Real, substantive errors found on every single page — not link-presence
sweeps. Headline catches:
- **Misattributed CVE (worst-failure-mode class):** `mcp-server-security.md` cited
  **CVE-2025-65513 (CVSS 9.3)** as Anthropic's official `mcp-server-fetch` SSRF vulnerability.
  Verified via the live GHSA advisory (GHSA-8fxj-2g9q-8fjw) that this CVE actually belongs to a
  **different, unrelated project** — `zcaceres/fetch-mcp` (CVSS 6.3, not 9.3). The same error,
  repeated ~10x, was also found in `content/reviews/fetch-mcp-server.md` (outside this run's
  planned scope but fixed immediately given the severity) — and that review's "safer
  alternative" recommendation was **the CVE-affected project itself**. A second fabrication
  (a nonexistent "OrbisAI Security" SSRF fix PR) was caught and removed during the same fix.
- **Fabricated version history:** `mcp-personal-knowledge-management-pkm.md` cited
  "v0.10.0/v0.11.0, March 2026" releases of cyanheads/obsidian-mcp-server that never existed
  per npm's actual version history (jumps 1.1.0→3.0.0, nothing in March 2026); wrong tool/method
  names invented to match.
- **Fabricated benchmark exposed:** `best-ai-ml-mcp-servers.md`'s Ruflo entry undersold two
  independent audits showing ~290/300+ advertised tools are non-functional stubs and its 84.8%
  SWE-bench figure comes from a script using `random.uniform` around hardcoded numbers rather
  than running the benchmark — rewrote to state this plainly with citations.
  Also fixed: wrong academic venue + wrong percentage on OSWorld-MCP (NeurIPS workshop → ICLR
  2026; 17.6% → the paper's actual 20.4%), a ClickHouse-style stat-fusion error on MCP-Universe
  (two different evals conflated into one number).
- **Correctness bugs, not just citations:** `build-your-first-mcp-server.md`'s tutorial code
  (`from mcp.server.fastmcp import FastMCP`) would fail with `ImportError` today — MCP Python
  SDK v2.0.0 (July 28, 2026) renamed/moved this class; fixed both code listings.
  `best-productivity-mcp-servers.md` had Asana's V2 tool count wrong by ~2.5x (44 claimed vs.
  actual ~17) and the V1 shutdown date stated as still-pending when it had already passed.
- **Wrong/stale numbers across the batch:** Postgres MCP weekly downloads (21K claimed vs. 87K
  live), MongoDB tool counts (~40 vs. 50+), a wrong Context7 version/date tied to a real stat,
  an AWS MCP endpoint stuck at "still preview" when it reached GA May 6 2026, a fabricated AWS
  MCP endpoint URL in a code sample, internally-contradictory tool counts within single pages
  (DaVinci Resolve, two Premiere Pro MCP servers, Ableton MCP), and dozens of GitHub star-count
  figures updated or explicitly dated where a live-snapshot framing was preserved.
- Full detail for all 11 files (10 guides + 1 review) in WORKLOG.md, 2026-08-10 run.

- [x] 2026-07-22 — [Best Database MCP Servers in 2026](content/guides/best-database-mcp-servers.md)
- [x] 2026-07-22 — [Best Documentation MCP Servers in 2026](content/guides/best-documentation-mcp-servers.md)
- [x] 2026-07-22 — [Best Productivity & Knowledge Management MCP Servers in 2026](content/guides/best-productivity-mcp-servers.md)
- [x] 2026-07-22 — [How to Build Your First MCP Server](content/guides/build-your-first-mcp-server.md)
- [x] 2026-07-22 — [MCP Server Security: A Practical Guide for 2026](content/guides/mcp-server-security.md)
- [x] 2026-07-22 — [MCP and Personal Knowledge Management: How AI Agents Connect to Obsidian Vaults, Notion Workspaces, Roam Research Graphs, Logseq Databases, Evernote Libraries, Apple Notes, Zotero References, Readwise Highlights, Raindrop Bookmarks, Heptabase Whiteboards, and Second Brain Tools](content/guides/mcp-personal-knowledge-management-pkm.md)
- [x] 2026-07-23 — [AWS vs Google Cloud vs Azure — Cloud Provider MCP Servers Compared (2026)](content/guides/best-cloud-mcp-servers.md)
- [x] 2026-07-23 — [Best AI & ML MCP Servers in 2026](content/guides/best-ai-ml-mcp-servers.md)
- [x] 2026-07-23 — [Best API Gateway & API Management MCP Servers in 2026 — Kong vs Cloudflare vs Traefik vs AWS vs Azure vs Open Source](content/guides/best-api-gateway-mcp-servers.md)
- [x] 2026-07-23 — [Best Audio & Video MCP Servers in 2026](content/guides/best-audio-video-mcp-servers.md)
- [x] 2026-07-23 — [Best Blockchain & Web3 MCP Servers in 2026](content/guides/best-blockchain-web3-mcp-servers.md)
- [x] 2026-07-23 — [Best CMS & Content Management MCP Servers in 2026](content/guides/best-cms-mcp-servers.md)
- [x] 2026-07-23 — [Best CRM MCP Servers in 2026](content/guides/best-crm-mcp-servers.md)
- [x] 2026-07-23 — [Best Communication MCP Servers in 2026](content/guides/best-communication-mcp-servers.md)
- [x] 2026-07-23 — [Best Data & Analytics MCP Servers in 2026](content/guides/best-data-analytics-mcp-servers.md)
- [x] 2026-07-23 — [Best Design MCP Servers in 2026](content/guides/best-design-mcp-servers.md)
- [x] 2026-07-23 — [Best Desktop Automation MCP Servers in 2026](content/guides/best-desktop-automation-mcp-servers.md)
- [x] 2026-07-23 — [Best Email & Notifications MCP Servers in 2026](content/guides/best-email-mcp-servers.md)
- [x] 2026-07-23 — [Best File & Storage MCP Servers in 2026 — Local Filesystem vs Cloud Storage vs Enterprise Platforms](content/guides/best-file-storage-mcp-servers.md)
- [x] 2026-07-23 — [Best Finance & Payments MCP Servers in 2026](content/guides/best-finance-mcp-servers.md)
- [x] 2026-07-23 — [Best IoT MCP Servers in 2026](content/guides/best-iot-mcp-servers.md)
- [x] 2026-07-23 — [Best Kubernetes & Container MCP Servers in 2026 — Native API vs kubectl Wrappers vs Docker Management](content/guides/best-kubernetes-container-mcp-servers.md)
- [x] 2026-07-23 — [Best Memory & Knowledge MCP Servers in 2026](content/guides/best-memory-mcp-servers.md)
- [x] 2026-07-23 — [Best Message Queue & Streaming MCP Servers in 2026 — Kafka vs RabbitMQ vs Pulsar vs NATS vs Cloud](content/guides/best-message-queue-mcp-servers.md)
- [x] 2026-07-23 — [Best Observability MCP Servers (2026) — 40+ Compared](content/guides/best-observability-mcp-servers.md)
- [x] 2026-07-23 — [Best PDF & Document Processing MCP Servers in 2026 — MarkItDown vs Docling vs Kreuzberg vs Official MCP PDF Server](content/guides/best-pdf-document-processing-mcp-servers.md)
- [x] 2026-07-23 — [Best Project Management MCP Servers in 2026](content/guides/best-project-management-mcp-servers.md) — re-audited 2026-08-11
- [x] 2026-07-23 — [Best Search MCP Servers in 2026](content/guides/best-search-mcp-servers.md) — re-audited 2026-08-11
- [x] 2026-07-23 — [Best Security MCP Servers in 2026](content/guides/best-security-mcp-servers.md) — re-audited 2026-08-11
- [x] 2026-07-23 — [Best Social Media MCP Servers 2026 — 35+ Tools for X, Bluesky, LinkedIn & More](content/guides/best-social-media-mcp-servers.md) — re-audited 2026-08-11
- [x] 2026-07-23 — [Best Spreadsheet MCP Servers in 2026 — Excel vs Google Sheets vs Airtable vs Smartsheet](content/guides/best-spreadsheet-mcp-servers.md) — re-audited 2026-08-11
- [x] 2026-07-23 — [Best Testing & QA MCP Servers in 2026](content/guides/best-testing-qa-mcp-servers.md) — re-audited 2026-08-11
- [x] 2026-07-23 — [Best Vector Database MCP Servers in 2026](content/guides/best-vector-database-mcp-servers.md) — re-audited 2026-08-11
- [x] 2026-07-23 — [Best Version Control MCP Servers in 2026](content/guides/best-version-control-mcp-servers.md) — re-audited 2026-08-11
- [x] 2026-07-23 — [Best Web Scraping & Fetching MCP Servers in 2026](content/guides/best-web-scraping-mcp-servers.md) — re-audited 2026-08-11
- [x] 2026-07-23 — [Best Workflow Automation MCP Servers in 2026](content/guides/best-workflow-automation-mcp-servers.md) — re-audited 2026-08-11
- [x] 2026-07-23 — [What Is MCP? A Developer's Guide to the Model Context Protocol](content/guides/what-is-mcp.md) — re-audited 2026-08-11
- [x] 2026-07-24 — [AI Agent Memory Patterns: How to Build Agents That Actually Remember](content/guides/ai-agent-memory-patterns.md) — re-audited 2026-08-11
- [x] 2026-07-24 — [AI Agent SDKs in 2026: Claude, Microsoft, AG2, Mastra, and mcp-agent Compared](content/guides/mcp-agent-sdks-2026.md) — re-audited 2026-08-11
- [x] 2026-07-24 — [AI Agent Workflow Patterns: Building Multi-Step Automation with MCP](content/guides/mcp-agent-workflow-patterns.md) — re-audited 2026-08-11
- [x] 2026-07-24 — [AI Coding Assistants Compared (2026) — 8 Tools Ranked](content/guides/ai-coding-assistants-compared.md) — re-audited 2026-08-11
- [x] 2026-07-24 — [Bot Etiquette on Social Media: How AI Agents Should Behave Online](content/guides/bot-etiquette-on-social-media.md) — re-audited 2026-08-11
- [x] 2026-07-24 — [Building A2A Agents: A Practical Guide to Agent-to-Agent Communication](content/guides/building-a2a-agents.md) — re-audited 2026-08-11
- [x] 2026-07-24 — [Building AI-Powered CLIs with MCP: From Terminal Tools to Autonomous Agents](content/guides/building-ai-powered-clis-mcp.md) — re-audited 2026-08-11
- [x] 2026-07-24 — [Building Enterprise MCP Infrastructure: Governance, Access Control, and Audit at Scale](content/guides/mcp-enterprise-infrastructure.md) — re-audited 2026-08-11
- [x] 2026-07-24 — [Building MCP Clients: A Practical Guide to Host Applications](content/guides/building-mcp-clients.md) — re-audited 2026-08-11
- [x] 2026-07-24 — [Connecting AI Agents to Databases with MCP: Patterns, Security, and Production Best Practices](content/guides/mcp-database-connection-patterns.md) — re-audited 2026-08-11
- [x] 2026-07-24 — [Debugging MCP Servers: A Practical Troubleshooting Guide](content/guides/debugging-mcp-servers.md) — re-audited 2026-08-11
- [x] 2026-07-24 — [Event-Driven MCP Patterns: Notifications, Streaming, and Real-Time AI Agents](content/guides/event-driven-mcp-patterns.md) — re-audited 2026-08-11
- [x] 2026-07-24 — [FastMCP: The High-Level Framework for Building Production MCP Servers](content/guides/fastmcp-production-guide.md) — re-audited 2026-08-11
- [x] 2026-07-24 — [How to Build an AI Agent: Architecture, Tools, and Patterns for 2026](content/guides/how-to-build-ai-agent.md) — re-audited 2026-08-11
- [x] 2026-07-24 — [How to Choose the Right MCP Server: A Practical Evaluation Framework](content/guides/how-to-choose-mcp-servers.md) — re-audited 2026-08-11
- [x] 2026-07-24 — [How to Convert Your REST API to an MCP Server](content/guides/rest-api-to-mcp-server.md) — re-audited 2026-08-11
- [x] 2026-07-24 — [MCP + AI Agent Frameworks: LangChain, CrewAI, OpenAI Agents SDK & More](content/guides/mcp-agent-framework-integrations.md) — re-audited 2026-08-11
- [x] 2026-07-24 — [MCP 2026 Roadmap: What's Coming in the Next Spec Release](content/guides/mcp-2026-roadmap-whats-coming.md) — re-audited 2026-08-11
- [x] 2026-07-24 — [MCP AI Safety: Guardrails, Content Filtering, Sandboxing, and Responsible AI Patterns](content/guides/mcp-ai-safety-guardrails.md) — re-audited 2026-08-11
- [x] 2026-07-24 — [MCP Async Tasks: Building Long-Running AI Agent Operations That Don't Time Out](content/guides/mcp-async-tasks-long-running.md) — re-audited 2026-08-11
- [x] 2026-07-24 — [MCP Attack Vectors: Tool Poisoning, Prompt Injection, and How to Defend Against Them](content/guides/mcp-attack-vectors-defense.md) — re-audited 2026-08-11
- [x] 2026-07-24 — [MCP Authentication & OAuth 2.1: Authorization Flows, Token Management, and Enterprise Security Patterns](content/guides/mcp-authentication-oauth.md) — re-audited 2026-08-11 (flagged as substantively redundant with mcp-authorization-oauth.md — human merge/retire decision needed)
- [x] 2026-07-24 — [MCP Authorization and OAuth 2.1: How AI Agents Authenticate with Remote Servers](content/guides/mcp-authorization-oauth.md) — re-audited 2026-08-11 (flagged as substantively redundant with mcp-authentication-oauth.md — human merge/retire decision needed)
- [x] 2026-07-24 — [MCP Browser Automation: Playwright MCP, Stagehand, Chrome DevTools, and the Agentic Browser Landscape](content/guides/mcp-browser-automation.md) — re-audited 2026-08-11
- [x] 2026-07-24 — [MCP Caching Strategies: Prompt Caching, Server-Side Caching, Semantic Caching, and Gateway Patterns](content/guides/mcp-caching-strategies.md) — re-audited 2026-08-11
- [x] 2026-07-24 — [MCP Clients Compared: Which AI Tools Support the Model Context Protocol?](content/guides/mcp-clients-comparison.md) — re-audited 2026-08-11
- [x] 2026-07-24 — [MCP Cost Optimization: Reducing Token Waste and Controlling AI Agent Spend](content/guides/mcp-cost-optimization.md) — re-audited 2026-08-11
- [x] 2026-07-24 — [MCP Credential & Secret Management: Securing API Keys, Tokens, and Passwords](content/guides/mcp-credential-secret-management.md) — re-audited 2026-08-11
- [x] 2026-07-24 — [MCP Elicitation Explained: How Servers Request User Input at Runtime](content/guides/mcp-elicitation-explained.md) — re-audited 2026-08-11
- [x] 2026-07-24 — [MCP Error Handling & Resilience: Protocol Errors, Tool Recovery, Circuit Breakers, and Production Fault Tolerance](content/guides/mcp-error-handling-resilience.md)
- [x] 2026-07-24 — [MCP Error Handling Explained: Protocol Errors, Tool Failures, and Recovery Patterns](content/guides/mcp-error-handling-explained.md)
- [x] 2026-07-24 — [MCP Gateway & Proxy Patterns: Aggregating, Securing, and Scaling MCP Servers](content/guides/mcp-gateway-proxy-patterns.md)
- [x] 2026-07-24 — [MCP Lifecycle and Utilities Explained: Initialization, Progress, Cancellation, Logging, and Ping](content/guides/mcp-lifecycle-and-utilities-explained.md)
- [x] 2026-07-24 — [MCP Logging & Observability: Debugging Servers You Can't See Into](content/guides/mcp-logging-observability.md)
- [x] 2026-07-24 — [MCP Mobile Integration: On-Device Agents, Phone Automation, Native SDKs, and Edge Deployment Patterns](content/guides/mcp-mobile-integration.md)
- [x] 2026-07-24 — [MCP Multi-Agent Architectures: How AI Agents Coordinate Through Shared Tools](content/guides/mcp-multi-agent-architectures.md)
- [x] 2026-07-24 — [MCP Multi-Tenant Architecture: Per-Tenant Isolation, Shared Servers, OAuth Identity Propagation, and SaaS Deployment Patterns](content/guides/mcp-multi-tenant-patterns.md)
- [x] 2026-07-24 — [MCP Notifications Explained: List Changes, Resource Subscriptions, and Dynamic Discovery](content/guides/mcp-notifications-explained.md)
- [x] 2026-07-24 — [MCP Pagination Patterns: Handling Large Result Sets Without Blowing Your Context](content/guides/mcp-pagination-patterns.md)
- [x] 2026-07-24 — [MCP Prompts Explained: How Servers Share Reusable Prompt Templates](content/guides/mcp-prompts-explained.md) — re-audited 2026-08-11
- [x] 2026-07-24 — [MCP Real-Time Streaming: Transports, Subscriptions, Event-Driven Patterns, and Production Architecture](content/guides/mcp-real-time-streaming.md) — re-audited 2026-08-11
- [x] 2026-07-24 — [MCP Registry & Server Discovery Guide (2026)](content/guides/mcp-registry-server-discovery.md) — re-audited 2026-08-11
- [x] 2026-07-24 — [MCP Resource Templates Deep Dive: Dynamic Content with URI Patterns](content/guides/mcp-resource-templates-deep-dive.md) — re-audited 2026-08-11
- [x] 2026-07-24 — [MCP Resources and Roots Explained: How Servers Expose Data and Clients Define Boundaries](content/guides/mcp-resources-and-roots-explained.md) — re-audited 2026-08-11
- [x] 2026-07-24 — [MCP Sampling Explained: How Servers Request AI Completions Through Clients](content/guides/mcp-sampling-explained.md) — re-audited 2026-08-11
- [x] 2026-07-24 — [MCP Server Deployment & Hosting: Docker, Cloud, Serverless, and Self-Hosted](content/guides/mcp-server-deployment-hosting.md) — re-audited 2026-08-11
- [x] 2026-07-24 — [MCP Server Frameworks and SDKs: A Developer's Guide](content/guides/mcp-server-frameworks-sdks.md) — re-audited 2026-08-11
- [x] 2026-07-24 — [MCP Server Marketplace & Monetization: How to Publish, Distribute, and Earn from MCP Servers](content/guides/mcp-marketplace-monetization.md) — re-audited 2026-08-11
- [x] 2026-07-24 — [MCP Server Packaging & Distribution: npm, PyPI, Docker, DXT, and the Official Registry](content/guides/mcp-server-packaging-distribution.md) — re-audited 2026-08-11
- [x] 2026-07-24 — [MCP Server Performance Tuning: From 250ms to Sub-Millisecond Response Times](content/guides/mcp-server-performance-tuning.md) — re-audited 2026-08-11 (title changed to "Language, Transport, and Caching Choices That Cut Latency 10x or More" — the old title asserted an unverifiable, unsupported stat)
- [x] 2026-07-24 — [MCP Setup for AI Coding Tools: Cursor, Claude Code, VS Code, Windsurf, and More](content/guides/mcp-setup-ai-coding-tools.md) — re-audited 2026-08-12
- [x] 2026-07-24 — [MCP Structured Output Deep Dive: outputSchema and structuredContent](content/guides/mcp-structured-output-deep-dive.md) — re-audited 2026-08-12
- [x] 2026-07-24 — [MCP Testing Strategies: Unit Tests, Integration Tests, and the MCP Inspector](content/guides/mcp-testing-strategies.md) — re-audited 2026-08-12
- [x] 2026-07-24 — [MCP Testing Tools Cookbook: 10 Recipes Beyond Unit Tests](content/guides/mcp-testing-tools-cookbook.md) — re-audited 2026-08-12
- [x] 2026-07-24 — [MCP Tool Annotations Explained: Hints, Trust, and the Risk Vocabulary](content/guides/mcp-tool-annotations-explained.md) — re-audited 2026-08-12
- [x] 2026-07-24 — [MCP Tool Composition: Building Multi-Server Workflows](content/guides/mcp-tool-composition-workflows.md) — re-audited 2026-08-12
- [x] 2026-07-24 — [MCP Tool Design Patterns: Building Agent-Friendly, Composable Tools](content/guides/mcp-tool-design-patterns.md) — re-audited 2026-08-12
- [x] 2026-07-24 — [MCP Transports Explained: stdio vs Streamable HTTP (and Why SSE Was Deprecated)](content/guides/mcp-transports-explained.md) — re-audited 2026-08-12
- [x] 2026-07-24 — [MCP Versioning and Backward Compatibility: A Practical Guide](content/guides/mcp-versioning-backward-compatibility.md) — re-audited 2026-08-12
- [x] 2026-07-24 — [MCP Workflow Orchestration: Frameworks, Durable Execution, and Production Agent Pipelines](content/guides/mcp-workflow-orchestration-frameworks.md) — re-audited 2026-08-12
- [x] 2026-07-24 — [MCP and Anthropic Claude: How Claude Desktop, Claude Code, the Claude API, and the Agent SDK Use the Model Context Protocol](content/guides/mcp-anthropic-claude-integration.md)
- [x] 2026-07-24 — [MCP and Databases: Connecting AI Agents to Your Data](content/guides/mcp-database-patterns.md)
- [x] 2026-07-24 — [MCP and Environmental Monitoring: How AI Agents Connect to Weather Systems, Air Quality Sensors, Satellite Imagery, Carbon Tracking, and Climate Data](content/guides/mcp-environmental-monitoring.md)
- [x] 2026-07-24 — [MCP and Food/Restaurant: How AI Agents Connect to Recipes, Nutrition Data, POS Systems, Food Delivery, Reservations, Kitchen Operations, and Grocery Platforms](content/guides/mcp-food-restaurant.md)
- [x] 2026-07-24 — [MCP and Government: How AI Agents Connect to Legislative Data, Open Data Portals, Census Systems, Procurement Platforms, and Public Sector Operations](content/guides/mcp-government-public-sector.md)
- [x] 2026-07-24 — [MCP and GraphQL: Why GraphQL Is Becoming the Backend for AI Agent Tools](content/guides/mcp-graphql-integration.md)
- [x] 2026-07-24 — [MCP and Knowledge Graphs: GraphRAG, Multi-Hop Reasoning, and Structured AI Memory](content/guides/mcp-knowledge-graphs.md)
- [x] 2026-07-24 — [MCP and Mining: How AI Agents Connect to Geological Modeling, Mine Planning, Resource Estimation, Environmental Monitoring, Oil & Gas, and Commodity Trading Tools](content/guides/mcp-mining-natural-resources.md)
- [x] 2026-07-24 — [MCP and Multimodal AI: How Agents Handle Images, Video, Audio, and Rich Media](content/guides/mcp-multimodal-patterns.md)
- [x] 2026-07-24 — [MCP and OpenAI: How ChatGPT, the Agents SDK, Codex, and the Responses API Use the Model Context Protocol](content/guides/mcp-openai-integration.md)
- [ ] 2026-07-24 — [MCP and RAG: Building Retrieval-Augmented Generation Pipelines with Model Context Protocol](content/guides/mcp-rag-patterns.md)
- [ ] 2026-07-24 — [MCP at the Edge: Deploying AI Agent Tools Closer to Users, Devices, and Data](content/guides/mcp-edge-computing-patterns.md)
- [ ] 2026-07-24 — [MCP for Accounting — 95+ Integrations (2026)](content/guides/mcp-accounting-tax-compliance.md)
- [ ] 2026-07-24 — [MCP for Data Science: AI Agents for Notebooks, ML Experiments, Feature Stores, and Data Pipelines](content/guides/mcp-data-science-workflows.md)
- [ ] 2026-07-24 — [MCP for DevOps and CI/CD: AI Agents Meet Infrastructure Automation](content/guides/mcp-devops-cicd.md)
- [ ] 2026-07-24 — [MCP for Testing and QA: AI Agents in Software Testing Pipelines](content/guides/mcp-testing-qa.md)
- [ ] 2026-07-24 — [MCP in Microservices: Service Mesh, API Gateways, and Distributed Architecture Patterns](content/guides/mcp-microservices-service-mesh.md)
- [ ] 2026-07-24 — [MCP in Regulated Industries: Compliance, Audit Trails, and Data Protection for AI Agents](content/guides/mcp-compliance-regulated-industries.md)
- [ ] 2026-07-24 — [MCP on Serverless: Deploying AI Agent Tools on Lambda, Cloudflare Workers, Vercel, and Beyond](content/guides/mcp-serverless-deployment.md)
- [ ] 2026-07-24 — [MCP vs A2A: Understanding the Two Protocols Shaping AI Agent Infrastructure](content/guides/mcp-vs-a2a-protocol-comparison.md)
- [ ] 2026-07-24 — [MCP vs CLI for AI Agents: When to Use Which in 2026](content/guides/mcp-vs-cli-ai-agents.md)
- [ ] 2026-07-24 — [MCP vs Function Calling: What's the Difference and When to Use Each](content/guides/mcp-vs-function-calling.md)
- [ ] 2026-07-24 — [MCP vs REST APIs: When to Use Each for AI Integration](content/guides/mcp-vs-rest-apis.md)
- [ ] 2026-07-24 — [MCP with Slack and Teams: Building AI Agents for Workplace Chat](content/guides/mcp-slack-teams-integration.md)
- [ ] 2026-07-24 — [Migrating Your MCP Server from stdio to Streamable HTTP: A Step-by-Step Guide](content/guides/mcp-server-migration-stdio-to-http.md)
- [ ] 2026-07-24 — [Running MCP Servers in Docker: Setup, Security, and Production Patterns](content/guides/mcp-docker-containers.md)
- [ ] 2026-07-24 — [Running MCP Servers in Production: Patterns and Pitfalls](content/guides/mcp-in-production.md)
- [ ] 2026-07-24 — [The Agentic Web: AGENTS.md, llms.txt, and Making Your Site Agent-Ready](content/guides/agentic-web-agents-md-llms-txt.md)
- [ ] 2026-07-24 — [The Complete MCP Debugging Guide: From Silent Failures to Working Servers](content/guides/mcp-debugging-guide.md)
- [ ] 2026-07-24 — [The MCP Ecosystem in 2026: How the Model Context Protocol Became the Universal Standard for AI Tool Integration](content/guides/mcp-ecosystem-2026-state-of-the-standard.md)
- [ ] 2026-07-24 — [Using MCP Across AI Platforms: Claude, ChatGPT, Gemini, Copilot, and More](content/guides/mcp-across-ai-platforms.md)
- [ ] 2026-07-24 — [Using MCP with Local LLMs: Ollama, LM Studio, and Open Source Models](content/guides/mcp-with-local-llms.md)
- [ ] 2026-07-24 — [Writing Effective CLAUDE.md Files: The Complete Guide to Claude Code Project Instructions](content/guides/writing-effective-claude-md-files.md)

## Reviews

- [ ] 2026-07-22 — [AWS MCP Servers — 54 Active Servers, Nine Deprecated, and Google Just Matched the Count](content/reviews/aws-mcp-servers.md)
- [ ] 2026-07-22 — [Analytics MCP Servers — Google Analytics, Mixpanel, PostHog, Amplitude, Microsoft Clarity, and Beyond](content/reviews/analytics-mcp-servers.md)
- [ ] 2026-07-22 — [Anthropic Acquires Vercept: A Computer-Use Bet, a $250M Talent Raid, and an Honest 'We're Throwing in the Towel](content/reviews/anthropic-acquires-vercept-computer-use-ai-startup-claude-agents-2026.md)
- [ ] 2026-07-22 — [Apple's $1 Billion Surrender: Why the World's Most Valuable Company Chose Google to Build Its AI Future](content/reviews/apple-google-gemini-siri-1-billion-deal-2026.md)
- [ ] 2026-07-22 — [Atlassian MCP Server — Jira and Confluence Access for AI Agents](content/reviews/atlassian-mcp-server.md)
- [ ] 2026-07-22 — [CI/CD MCP Servers — GitHub Actions, Jenkins, GitLab CI, CircleCI, and Beyond](content/reviews/cicd-mcp-servers.md)
- [ ] 2026-07-22 — [CRM MCP Servers — Salesforce, HubSpot, Pipedrive, and Beyond](content/reviews/crm-mcp-servers.md)
- [ ] 2026-07-22 — [Claude Sonnet 4.6 Review — 1M Context, 58.3% ARC-AGI-2, and the Price-to-Performance Leader](content/reviews/anthropic-claude-sonnet-4-6-review-benchmarks-2026.md)
- [ ] 2026-07-22 — [Cloud Storage MCP Servers — S3, Google Cloud Storage, Azure Blob, MinIO, and Beyond](content/reviews/cloud-storage-mcp-servers.md)
- [ ] 2026-07-22 — [Google Calendar MCP Server — Multi-Account Calendar Management for AI Assistants](content/reviews/google-calendar-mcp-server.md)
- [ ] 2026-07-22 — [Grafana MCP Server Review — 40+ Tools, Open Source](content/reviews/grafana-mcp-server.md)
- [ ] 2026-07-22 — [Message Queue MCP Servers — Kafka, RabbitMQ, Pulsar, NATS, SQS, and Beyond](content/reviews/message-queue-mcp-servers.md)
- [ ] 2026-07-22 — [Mistral Small 3.1 Review — 24B Vision Model, 128K Context, Runs on One GPU](content/reviews/mistral-small-3-1-vision-24b-llm-review.md)
- [ ] 2026-07-22 — [New Relic MCP Server Review — 35 Tools, Free Tier](content/reviews/newrelic-mcp-server.md)
- [ ] 2026-07-22 — [Obsidian MCP Servers — Eight Servers, Three Architectures, No Official Blessing](content/reviews/obsidian-mcp-servers.md)
- [ ] 2026-07-22 — [Outlook MCP Servers — Microsoft's Enterprise Email Meets the Agent Era](content/reviews/outlook-mcp-servers.md)
- [ ] 2026-07-22 — [PDF & Document Processing MCP Servers — MarkItDown, Docling, PDF Reader, and More](content/reviews/pdf-document-mcp-servers.md)
- [ ] 2026-07-22 — [Science & Research MCP Servers — arXiv, PubMed, Semantic Scholar, UniProt, Wolfram, Scientific Computing, and More](content/reviews/science-research-mcp-servers.md)
- [ ] 2026-07-22 — [Search Engine MCP Servers — Elasticsearch, OpenSearch, Meilisearch, Algolia, Solr, and Beyond](content/reviews/search-engine-mcp-servers.md)
- [ ] 2026-07-22 — [Shopify MCP Servers — From 2 Servers to an Agentic Commerce Platform](content/reviews/shopify-mcp-servers.md)
- [ ] 2026-07-22 — [The Brave Search MCP Server — The Best Search Option for Agents](content/reviews/brave-search-mcp-server.md)
- [ ] 2026-07-22 — [The Browserbase MCP Server — Cloud Browser Automation With AI-Native Targeting](content/reviews/browserbase-mcp-server.md)
- [ ] 2026-07-22 — [The Chroma MCP Server — Vector Database Operations Through Your AI Assistant](content/reviews/chroma-mcp-server.md)
- [ ] 2026-07-22 — [The Cloudflare MCP Server — 2,500 API Endpoints in 1,000 Tokens](content/reviews/cloudflare-mcp-server.md)
- [ ] 2026-07-22 — [The Context7 MCP Server — Real-Time Library Docs, Registry Risk Included](content/reviews/context7-mcp-server.md)
- [ ] 2026-07-22 — [The Crawl4AI MCP Server — The Most Popular Crawler Goes LLM-Native](content/reviews/crawl4ai-mcp-server.md)
- [ ] 2026-07-22 — [The Datadog MCP Server — Enterprise Observability With Agent-Native Tool Design](content/reviews/datadog-mcp-server.md)
- [ ] 2026-07-22 — [The Docker MCP Server — Your AI Agent's Container Workshop](content/reviews/docker-mcp-server.md)
- [ ] 2026-07-22 — [The EverArt MCP Server — Image Generation for Agents, If You Can Find the API Key](content/reviews/everart-mcp-server.md)
- [ ] 2026-07-22 — [The Exa MCP Server — Semantic Search That Actually Understands What You Mean](content/reviews/exa-mcp-server.md)
- [x] 2026-07-22 — [The Fetch MCP Server — Your Agent's Simplest Window to the Web (With the Lock Off)](content/reviews/fetch-mcp-server.md)
- [ ] 2026-07-22 — [The Figma Dev Mode MCP Server — Design-to-Code Translation Through Your AI Assistant](content/reviews/figma-dev-mode-mcp-server.md)
- [ ] 2026-07-22 — [The Filesystem MCP Server — Simple, Useful, and Worth Understanding](content/reviews/filesystem-mcp-server.md)
- [ ] 2026-07-22 — [The Firecrawl MCP Server — The Full-Stack Web Scraping Platform for AI Agents](content/reviews/firecrawl-mcp-server.md)
- [ ] 2026-07-22 — [The Framelink MCP Server for Figma — Community Design-to-Code That Outperforms the Official](content/reviews/framelink-figma-mcp-server.md)
- [ ] 2026-07-22 — [The Git MCP Server — The Missing Push Button](content/reviews/git-mcp-server.md)
- [ ] 2026-07-22 — [The GitMCP Server — Zero-Setup Documentation From Any GitHub Repo](content/reviews/gitmcp-server.md)
- [ ] 2026-07-22 — [The Honeycomb MCP Server — Event-Based Observability With a Hosted MCP That Replaced Its Own Open-Source Server](content/reviews/honeycomb-mcp-server.md)
- [ ] 2026-07-22 — [The Kubernetes MCP Server — Native API Access Without the kubectl Tax](content/reviews/kubernetes-mcp-server.md)
- [ ] 2026-07-22 — [The Linear MCP Server — AI-Powered Project Management From Your Editor](content/reviews/linear-mcp-server.md)
- [ ] 2026-07-22 — [The Mem0 MCP Server — AI Memory That Actually Scales (If You Pay)](content/reviews/mem0-mcp-server.md)
- [ ] 2026-07-22 — [The Memory MCP Server — A Knowledge Graph That Needs a Better Brain](content/reviews/memory-mcp-server.md)
- [ ] 2026-07-22 — [The Milvus MCP Server — The Most Popular Vector Database Gets an AI Interface](content/reviews/milvus-mcp-server.md)
- [ ] 2026-07-22 — [The MongoDB MCP Server — The Most Comprehensive Database Server We've Reviewed](content/reviews/mongodb-mcp-server.md)
- [ ] 2026-07-22 — [The Neon MCP Server — Serverless Postgres Management Through Natural Language](content/reviews/neon-mcp-server.md)
- [ ] 2026-07-22 — [The Notion MCP Server — Your Workspace in Your Agent's Hands (Both Versions)](content/reviews/notion-mcp-server.md)
- [ ] 2026-07-22 — [The PagerDuty MCP Server — 67+ Tools for Incident Management With the Most Comprehensive Write API in the Category](content/reviews/pagerduty-mcp-server.md)
- [ ] 2026-07-22 — [The Perplexity MCP Server — When Your Agent Wants Answers, Not Links](content/reviews/perplexity-mcp-server.md)
- [ ] 2026-07-22 — [The Pinecone MCP Server — Cloud Vector Search With Built-In Reranking](content/reviews/pinecone-mcp-server.md)
- [ ] 2026-07-22 — [The Playwright MCP Server — The New Standard for Browser Automation](content/reviews/playwright-mcp-server.md)
- [ ] 2026-07-22 — [The PostgreSQL MCP Server — Read-Only Protection That Wasn't](content/reviews/postgres-mcp-server.md)
- [ ] 2026-07-22 — [The Pulumi MCP Server — From Registry Lookups to Autonomous Infrastructure via Neo](content/reviews/pulumi-mcp-server.md)
- [ ] 2026-07-22 — [The Puppeteer MCP Server — Give Your Agent a Real Browser](content/reviews/puppeteer-mcp-server.md)
- [ ] 2026-07-22 — [The Qdrant MCP Server — Semantic Memory Through Your AI Assistant](content/reviews/qdrant-mcp-server.md)
- [ ] 2026-07-22 — [The SQLite MCP Server — A Good Idea, Now Abandoned (and Vulnerable)](content/reviews/sqlite-mcp-server.md)
- [ ] 2026-07-22 — [The Sentry MCP Server — Debug Production Errors Without Leaving Your Editor](content/reviews/sentry-mcp-server.md)
- [ ] 2026-07-22 — [The Sequential Thinking MCP Server — When Your Agent Needs to Think Out Loud](content/reviews/sequential-thinking-mcp-server.md)
- [ ] 2026-07-22 — [The Slack MCP Server — Your Workspace, Accessible to Agents](content/reviews/slack-mcp-server.md)
- [ ] 2026-07-22 — [The Stripe MCP Server — Payment Operations Through Your AI Assistant](content/reviews/stripe-mcp-server.md)
- [ ] 2026-07-22 — [The Supabase MCP Server — Full Backend Management Through Your AI Assistant](content/reviews/supabase-mcp-server.md)
- [ ] 2026-07-22 — [The Tavily MCP Server — Search, Extract, Crawl, and Map in One Package](content/reviews/tavily-mcp-server.md)
- [ ] 2026-07-22 — [The Terraform MCP Server — Registry Intelligence for AI-Assisted Infrastructure](content/reviews/terraform-mcp-server.md)
- [ ] 2026-07-22 — [The Todoist MCP Server — Full-Stack Task Management Through Your AI Assistant](content/reviews/todoist-mcp-server.md)
- [ ] 2026-07-22 — [The Vercel MCP Server — Deployment Monitoring and Management Through Your AI Assistant](content/reviews/vercel-mcp-server.md)
- [ ] 2026-07-22 — [Zep's Graphiti MCP Server — Temporal Knowledge Graphs for AI Agent Memory](content/reviews/zep-graphiti-mcp-server.md)
- [ ] 2026-07-23 — [AI & ML Model Serving MCP Servers — HuggingFace, Ollama, Replicate, W&B, MLflow, and More](content/reviews/ai-ml-model-serving-mcp-servers.md)
- [ ] 2026-07-23 — [AI Agent Orchestration MCP Servers — Multi-Agent Frameworks, Swarm Coordination, Task Orchestration, and 17+ More](content/reviews/agent-orchestration-mcp-servers.md)
- [ ] 2026-07-23 — [AI Agent Supply Chain Security MCP Servers — Scanning, Vetting, and Securing the MCP Ecosystem](content/reviews/ai-agent-supply-chain-security-mcp-servers.md)
- [ ] 2026-07-23 — [API Gateway MCP Servers — Kong, APISIX, Cloudflare, Envoy, Traefik, and Beyond](content/reviews/api-gateway-mcp-servers.md)
- [ ] 2026-07-23 — [API Testing MCP Servers — REST Clients, GraphQL Tools, OpenAPI Converters, and gRPC Bridges](content/reviews/api-testing-mcp-servers.md)
- [ ] 2026-07-23 — [Accessibility & a11y MCP Servers — Axe-Core, WCAG Auditing, Color Contrast, BrowserStack, and More](content/reviews/accessibility-a11y-mcp-servers.md)
- [ ] 2026-07-23 — [Accounting & Bookkeeping MCP Servers — QuickBooks, Xero, Zoho Books, Sage, Wave, Beancount, and More](content/reviews/accounting-bookkeeping-mcp-servers.md)
- [ ] 2026-07-23 — [Advertising & Ad-Tech MCP Servers — Google Ads, Meta Ads, Amazon Ads, TikTok Ads, LinkedIn Ads, Programmatic DSPs, Multi-Platform Campaign Management, and Ad Auditing](content/reviews/advertising-ad-tech-mcp-servers.md)
- [ ] 2026-07-23 — [Aerospace & Defense MCP Servers — NASA Official Earthdata, Flightradar24 Official, STK, MAVLink, Axion V2.0, Satellite Imagery, Drones, and More](content/reviews/aerospace-defense-mcp-servers.md)
- [ ] 2026-07-23 — [Agriculture & Farming MCP Servers — Leaf, John Deere, FieldMCP, FarmerChat, Weather, Satellite Imagery, and More](content/reviews/agriculture-farming-mcp-servers.md)
- [ ] 2026-07-23 — [Annotation & Data Labeling MCP Servers — Label Studio, Roboflow, Labelbox, and More](content/reviews/annotation-data-labeling-mcp-servers.md)
- [ ] 2026-07-23 — [Anthropic MCP Servers — The Company That Created the Model Context Protocol](content/reviews/anthropic-mcp-server.md)
- [ ] 2026-07-23 — [Apple & macOS MCP Servers (2026) — 30+ Reviewed](content/reviews/apple-macos-mcp-servers.md)
- [ ] 2026-07-23 — [Asana MCP Server — Official Remote Server for Enterprise Project Management](content/reviews/asana-mcp-server.md)
- [ ] 2026-07-23 — [Astronomy & Space Science MCP Servers — NASA APIs, Telescope Control, Satellite Tracking, SpaceX, Astronomical Surveys, and Research Tools](content/reviews/astronomy-space-science-mcp-servers.md)
- [ ] 2026-07-23 — [Audio & Video Processing MCP Servers — ElevenLabs, FFmpeg, DaVinci Resolve, Ableton, REAPER, and More](content/reviews/audio-video-processing-mcp-servers.md)
- [ ] 2026-07-23 — [Automotive & Vehicle MCP Servers — Tesla, OBD-II Diagnostics, EV Charging, VIN Decoding, CAN Bus, Fleet Telematics, and More](content/reviews/automotive-vehicle-mcp-servers.md)
- [ ] 2026-07-23 — [Aviation & Flight MCP Servers — Flight Tracking, Booking, Weather, NOTAMs, ADS-B, Flightradar24, and Pilot Tools](content/reviews/aviation-flight-mcp-servers.md)
- [ ] 2026-07-23 — [Azure & Microsoft MCP Servers — Build 2026: App Service MCP, Copilot Studio GA, Foundry Toolboxes, Two CVEs](content/reviews/azure-mcp-servers.md)
- [ ] 2026-07-23 — [BI & Reporting MCP Servers — Tableau, Power BI, Grafana, Metabase, Looker, and Superset](content/reviews/bi-reporting-mcp-servers.md)
- [ ] 2026-07-23 — [Backup & Disaster Recovery MCP Servers — Veeam, Commvault, Velero, File Snapshots, and More](content/reviews/backup-disaster-recovery-mcp-servers.md)
- [ ] 2026-07-23 — [Bioinformatics & Life Sciences MCP Servers — Genomics, Proteomics, Drug Discovery, Clinical Trials, and Medical Imaging](content/reviews/bioinformatics-life-sciences-mcp-servers.md)
- [ ] 2026-07-23 — [Blockchain & Web3 MCP Servers — Ethereum, Solana, Bitcoin, Multi-Chain, DeFi, and More](content/reviews/blockchain-web3-mcp-servers.md)
- [ ] 2026-07-23 — [CAD & 3D Modeling MCP Servers — Blender, FreeCAD, AutoCAD, KiCad, SolidWorks, Fusion 360, OpenSCAD, and More](content/reviews/cad-3d-modeling-mcp-servers.md)
- [ ] 2026-07-23 — [CDN & Edge Computing MCP Servers — Cloudflare, Fastly, Akamai, Gcore, and Beyond](content/reviews/cdn-edge-computing-mcp-servers.md)
- [ ] 2026-07-23 — [CI/CD Pipeline MCP Servers — Jenkins, CircleCI, GitHub Actions, Argo CD, Buildkite, TeamCity, Harness, and More](content/reviews/ci-cd-pipeline-mcp-servers.md)
- [ ] 2026-07-23 — [CMS & Content Management MCP Servers — WordPress, Contentful, Sanity, Strapi, Directus, Ghost, and More](content/reviews/cms-content-management-mcp-servers.md)
- [ ] 2026-07-23 — [Calendar & Scheduling MCP Servers — Google Calendar, Outlook, Apple Calendar, Cal.com, Calendly, and More](content/reviews/calendar-scheduling-mcp-servers.md)
- [ ] 2026-07-23 — [Chaos Engineering MCP Servers — LitmusChaos, Chaos Mesh, Gremlin, Steadybit, Harness, and More](content/reviews/chaos-engineering-mcp-servers.md)
- [ ] 2026-07-23 — [Chemistry & Molecular Modeling MCP Servers — RDKit, PubChem, ChEMBL, Docking, and More](content/reviews/chemistry-molecular-modeling-mcp-servers.md)
- [ ] 2026-07-23 — [Code Quality, Linting & Static Analysis MCP Servers — ESLint, SonarQube, Semgrep, Ruff, Biome, and More](content/reviews/code-quality-linting-mcp-servers.md)
- [ ] 2026-07-23 — [Code Security MCP Servers — Snyk, SonarQube, Semgrep, Trivy, CodeQL, Datadog, Checkmarx, and Beyond](content/reviews/code-security-mcp-servers.md)
- [ ] 2026-07-23 — [Compliance & Audit Automation MCP Servers — Vanta, Drata, Secureframe, IBM OpenPages, CISO Assistant, ComplianceCow, and More](content/reviews/compliance-audit-automation-mcp-servers.md)
- [ ] 2026-07-23 — [Compliance & Audit MCP Servers — Vanta, Drata, SentinelGate, Agentic Gateway Registry, and More](content/reviews/compliance-audit-mcp-servers.md)
- [ ] 2026-07-23 — [Compliance & Data Governance MCP Servers — SOC 2, HIPAA, GDPR, Data Catalogs, Metadata Management, and More](content/reviews/compliance-data-governance-mcp-servers.md)
- [ ] 2026-07-23 — [Configuration Management MCP Servers — Ansible, NixOS, Chef, SaltStack, Consul, and More](content/reviews/configuration-management-mcp-servers.md)
- [ ] 2026-07-23 — [Construction & Architecture MCP Servers — Revit, AutoCAD, SketchUp, Rhino, ArchiCAD, Tekla, BIM/IFC, and More](content/reviews/construction-architecture-mcp-servers.md)
- [ ] 2026-07-23 — [Container Registry MCP Servers — Docker Hub, ECR, ACR, JFrog, Harbor, and Beyond](content/reviews/container-registry-mcp-servers.md)
- [ ] 2026-07-23 — [Container, Docker & Kubernetes MCP Servers — Docker Management, Kubernetes Orchestration, Helm Charts, Podman, Portainer, and More](content/reviews/container-docker-kubernetes-mcp-servers.md)
- [ ] 2026-07-23 — [Cryptocurrency & DeFi MCP Servers — Ethereum, Solana, Bitcoin, Wallets, DEX Trading, On-Chain Analytics, and More](content/reviews/cryptocurrency-defi-mcp-servers.md)
- [ ] 2026-07-23 — [Customer Support & Helpdesk MCP Servers — Zendesk, Intercom, Freshdesk, ServiceNow, Plain, and More](content/reviews/customer-support-helpdesk-mcp-servers.md)
- [ ] 2026-07-23 — [DNS & Domain Management MCP Servers — Registrars, DNS Providers, WHOIS, and Lookup Tools](content/reviews/dns-domain-management-mcp-servers.md)
- [ ] 2026-07-23 — [Data Pipeline & ETL MCP Servers — Airflow, dbt, Kafka, Snowflake, Databricks, Airbyte, and More](content/reviews/data-pipeline-etl-mcp-servers.md)
- [ ] 2026-07-23 — [Data Visualization MCP Servers — AntV, ECharts, Vega-Lite, Plotly, Matplotlib, D3, and More](content/reviews/data-visualization-mcp-servers.md)
- [ ] 2026-07-23 — [Data Warehouse & Lakehouse MCP Servers — Snowflake, BigQuery, Databricks, ClickHouse, DuckDB, Teradata, Redshift, and More](content/reviews/data-warehouse-lakehouse-mcp-servers.md)
- [ ] 2026-07-23 — [Database Administration MCP Servers — PostgreSQL, MySQL, MongoDB, Redis, DynamoDB, Oracle, and Beyond](content/reviews/database-admin-mcp-servers.md)
- [ ] 2026-07-23 — [Debugging MCP Servers — Chrome DevTools (37.8K Stars), Ghidra MCP (8.7K), IDA Pro MCP (8.1K), Microsoft DebugMCP, Multi-Language DAP (7 Languages), GDB/LLDB/WinDbg, Radare2, Embedded ARM/RISC-V](content/reviews/debugging-mcp-servers.md)
- [ ] 2026-07-23 — [Desktop Automation & Browser Control MCP Servers — Playwright, Selenium, Windows-MCP, macOS Automator, and More](content/reviews/desktop-automation-rpa-mcp-servers.md)
- [ ] 2026-07-23 — [Digital Accessibility MCP Servers — A11y Auditing, WCAG Compliance, Color Contrast, Lighthouse, and More](content/reviews/digital-accessibility-mcp-servers.md)
- [ ] 2026-07-23 — [Digital Forensics & Incident Response (DFIR) MCP Servers — CrowdStrike, SentinelOne, Google Security, TheHive, VirusTotal, Volatility, YARA, Wazuh, and More](content/reviews/digital-forensics-incident-response-mcp-servers.md)
- [ ] 2026-07-23 — [Digital Twins, 3D Modeling & Simulation MCP Servers — CAD, Physics, Game Engines, and Engineering Simulation](content/reviews/digital-twins-3d-simulation-mcp-servers.md)
- [ ] 2026-07-23 — [Discord MCP Servers — Five Community Servers, No Official One, and a Fragmented Landscape](content/reviews/discord-mcp-servers.md)
- [ ] 2026-07-23 — [E-Commerce & Shopping MCP Servers — Shopify, Stripe, WooCommerce, Amazon, and More](content/reviews/ecommerce-shopping-mcp-servers.md)
- [ ] 2026-07-23 — [E-Signature & Digital Signing MCP Servers — DocuSign, PandaDoc, SignNow, BoldSign, and More](content/reviews/e-signature-digital-signing-mcp-servers.md)
- [ ] 2026-07-23 — [ERP & Business Management MCP Servers — Odoo, Dynamics 365, NetSuite, SAP, Oracle, QuickBooks, and More](content/reviews/erp-business-management-mcp-servers.md)
- [ ] 2026-07-23 — [Education & EdTech MCP Servers — Canvas LMS, Moodle, Google Classroom, Anki, Udemy, EduBase, and More](content/reviews/education-edtech-mcp-servers.md)
- [ ] 2026-07-23 — [Education & LMS MCP Servers — Canvas, Moodle, Google Classroom, Anki, LeetCode, and More](content/reviews/education-lms-mcp-servers.md)
- [ ] 2026-07-23 — [Energy & Utilities MCP Servers — PowerMCP, EnergyPlus, PyPSA, zavora-ai SCADA, EIA, and More](content/reviews/energy-utilities-mcp-servers.md)
- [ ] 2026-07-23 — [Event Management & Ticketing MCP Servers — Google Official Calendar, Eventbrite, Ticketmaster, Meetup, and More](content/reviews/event-management-ticketing-mcp-servers.md)
- [ ] 2026-07-23 — [Fashion, Beauty & Style MCP Servers — Virtual Try-On, Secondhand Shopping, Skincare AI, Wardrobe Management, and K-Beauty](content/reviews/fashion-beauty-style-mcp-servers.md)
- [ ] 2026-07-23 — [Fitness & Wearables MCP Servers — Strava, Garmin, WHOOP, Apple Health, Oura Ring, Fitbit, and Multi-Platform Health Data](content/reviews/fitness-wearables-mcp-servers.md)
- [ ] 2026-07-23 — [Food & Restaurant MCP Servers — Yelp, Instacart, Spoonacular, Uber Eats, Swiggy, Zomato, OpenFoodFacts, and More](content/reviews/food-restaurant-mcp-servers.md)
- [ ] 2026-07-23 — [Game Engine & 3D Development MCP Servers — Unity, Unreal Engine, Godot, Roblox, Cocos Creator, Bevy, and More](content/reviews/game-engine-3d-development-mcp-servers.md)
- [ ] 2026-07-23 — [Gaming & Esports MCP Servers — Roblox Studio (Official!), Minecraft, OP.GG, Chess, Steam, GameBoy, F1, and More](content/reviews/gaming-esports-mcp-servers.md)
- [ ] 2026-07-23 — [Genealogy & Family History MCP Servers — GEDCOM, Gramps, FamilySearch, WikiTree, and More](content/reviews/genealogy-family-history-mcp-servers.md)
- [ ] 2026-07-23 — [Geospatial & Mapping MCP Servers — Mapbox, Google Earth Engine, NASA Earthdata, QGIS, and More](content/reviews/geospatial-mapping-mcp-servers.md)
- [ ] 2026-07-23 — [Google Cloud MCP Servers — 50+ Servers, 22+ GA, MCP Toolbox v1.4, Gemini 3.5 Flash MCP Optimization, and ADK 2.0](content/reviews/google-cloud-mcp-servers.md)
- [ ] 2026-07-23 — [Government & Public Sector MCP Servers — GovInfo, Census Bureau, Congress.gov, Data.gov, Procurement, and More](content/reviews/government-public-sector-mcp-servers.md)
- [ ] 2026-07-23 — [Graph Database MCP Servers — Neo4j, ArangoDB, Neptune, TigerGraph, Dgraph, Memgraph, FalkorDB, NebulaGraph, and More](content/reviews/graph-database-mcp-servers.md)
- [ ] 2026-07-23 — [HR & Recruiting MCP Servers — BambooHR, Workday, Greenhouse, Workable, Payroll, ATS, and More](content/reviews/hr-recruiting-mcp-servers.md)
- [ ] 2026-07-23 — [Healthcare & Medical MCP Servers — FHIR, PubMed, Clinical Trials, DICOM, Drug Databases, and More](content/reviews/healthcare-medical-mcp-servers.md)
- [ ] 2026-07-23 — [Hospitality & Hotels MCP Servers — Airbnb Search, Hotel Booking, Restaurant Reservations, and Travel Planning](content/reviews/hospitality-hotels-mcp-servers.md)
- [ ] 2026-07-23 — [Identity & Authentication MCP Servers — Okta, Auth0, Keycloak, Entra ID, Casdoor, and More](content/reviews/identity-authentication-mcp-servers.md)
- [ ] 2026-07-23 — [Image Generation MCP Servers — DALL-E, Stable Diffusion, ComfyUI, Flux, Midjourney, and 50+ More](content/reviews/image-generation-mcp-servers.md)
- [ ] 2026-07-23 — [Infrastructure Automation MCP Servers — Ansible, Terraform, Pulumi, OpenTofu, and Beyond](content/reviews/infrastructure-automation-mcp-servers.md)
- [ ] 2026-07-23 — [Insurance & InsurTech MCP Servers — Policy Management, Claims Processing, Underwriting Intelligence, and Compliance](content/reviews/insurance-insurtech-mcp-servers.md)
- [ ] 2026-07-23 — [Insurance MCP Servers — Claims Processing, Underwriting, Policy Management, Socotra, Sure, EMPLOYERS, and More](content/reviews/insurance-mcp-servers.md)
- [ ] 2026-07-23 — [Interior Design & Architecture MCP Servers — CAD, BIM, 3D Modeling, SketchUp, Blender, Rhino, and Floor Planning](content/reviews/interior-design-architecture-mcp-servers.md)
- [ ] 2026-07-23 — [IoT & Embedded MCP Servers — Home Assistant, MQTT, ESP32, ROS, Industrial PLCs, 3D Printers, and More](content/reviews/iot-embedded-mcp-servers.md)
- [ ] 2026-07-23 — [Job Search & Career MCP Servers — LinkedIn, Indeed, Resume Building, Interview Prep, Multi-Platform Job Aggregation](content/reviews/job-search-career-mcp-servers.md)
- [ ] 2026-07-23 — [LLM Evaluation & Benchmarking MCP Servers — Eval Frameworks, MCP Benchmarks, Red-Teaming, and 20+ More](content/reviews/llm-evaluation-benchmarking-mcp-servers.md)
- [ ] 2026-07-23 — [LLM Observability & MLOps Pipeline MCP Servers — Datadog, Arize Phoenix, Opik, LangSmith, Langfuse, MLflow, W&B, and More](content/reviews/llm-observability-mlops-pipeline-mcp-servers.md)
- [ ] 2026-07-23 — [Legal & Contract Management MCP Servers — E-Signatures, Legal Research, Case Law, IP/Trademarks, and More](content/reviews/legal-contract-management-mcp-servers.md)
- [ ] 2026-07-23 — [Library, Archive & Museum MCP Servers — Zotero, Calibre, IIIF, Wayback Machine, and Museum Collections](content/reviews/library-archive-museum-mcp-servers.md)
- [ ] 2026-07-23 — [Log Management MCP Servers — Splunk, Elasticsearch, Loki, Datadog, CloudWatch, and Beyond](content/reviews/log-management-mcp-servers.md)
- [ ] 2026-07-23 — [Logistics & Supply Chain MCP Servers — Shipping, Fleet Tracking, Inventory Management, and Maritime Intelligence](content/reviews/logistics-supply-chain-mcp-servers.md)
- [ ] 2026-07-23 — [MCP Server Frameworks & SDKs — FastMCP, Official SDKs, and the Tools That Power Every MCP Server](content/reviews/mcp-server-frameworks-sdks.md)
- [ ] 2026-07-23 — [MailerSend MCP Server — Full Email Management From Your AI Agent](content/reviews/mailersend-mcp-server.md)
- [ ] 2026-07-23 — [Mailgun MCP Server — 85 Tools for Enterprise Email Infrastructure](content/reviews/mailgun-mcp-server.md)
- [ ] 2026-07-23 — [Manufacturing & Industrial MCP Servers — Robotics/ROS, PLC/Siemens S7, OPC UA, 3D Printing, Digital Twins, Predictive Maintenance, SCADA, and More](content/reviews/manufacturing-industrial-mcp-servers.md)
- [ ] 2026-07-23 — [Marketing Automation MCP Servers — Email Marketing, Ad Platforms, SEO, and Social Media Management](content/reviews/marketing-automation-mcp-servers.md)
- [ ] 2026-07-23 — [Mental Health & Wellness MCP Servers — Therapy, Mood Tracking, Journaling, Meditation, and Personal Wellbeing](content/reviews/mental-health-wellness-mcp-servers.md)
- [ ] 2026-07-23 — [Microsoft Teams MCP Servers — Official at Last, Community Got There First](content/reviews/teams-mcp-servers.md)
- [ ] 2026-07-23 — [Mistral Small 4 Review — 119B MoE, 256K Context, Reasoning + Vision + Coding in One](content/reviews/mistral-small-4-119b-moe-reasoning-vision-coding-llm-review.md)
- [ ] 2026-07-23 — [Monitoring & Uptime MCP Servers — UptimeRobot, Uptime Kuma, OneUptime, Better Stack, and New Standalone Platforms](content/reviews/monitoring-uptime-mcp-servers.md)
- [ ] 2026-07-23 — [Music & Audio Production MCP Servers — Ableton Live, Logic Pro, REAPER, Pro Tools, FL Studio, Bitwig, Spotify, ElevenLabs, and More](content/reviews/music-audio-production-mcp-servers.md)
- [ ] 2026-07-23 — [Netlify MCP Server — AI Agents That Deploy, Manage Sites, Handle Extensions, and Go From Prompt to Production](content/reviews/netlify-mcp-server.md)
- [ ] 2026-07-23 — [Network Automation & Infrastructure MCP Servers — Multi-Vendor Management, NetBox, Netmiko, pyATS, Firewalls, Juniper, Network Diagnostics, and Digital Twins](content/reviews/network-automation-infrastructure-mcp-servers.md)
- [ ] 2026-07-23 — [Network Security & Monitoring MCP Servers — Packet Capture, Port Scanning, Pentesting, and Reconnaissance](content/reviews/network-security-mcp-servers.md)
- [ ] 2026-07-23 — [News, Media & Journalism MCP Servers — RSS Feeds, Hacker News, News APIs, Podcasts, and Fact-Checking](content/reviews/news-media-journalism-mcp-servers.md)
- [ ] 2026-07-23 — [Nonprofit & Charity MCP Servers — Grant Discovery, Donor Management, Humanitarian Data, Charity Verification, Civic Data, and Volunteer Impact](content/reviews/nonprofit-charity-mcp-servers.md)
- [ ] 2026-07-23 — [Note-Taking & Knowledge Management MCP Servers — Your Second Brain Meets AI Agents](content/reviews/note-taking-knowledge-management-mcp-servers.md)
- [ ] 2026-07-23 — [Notification & Email Delivery MCP Servers — Twilio, Resend, SendGrid, Mailgun, Postmark, Infobip, Courier, Novu, and Beyond](content/reviews/notification-services-mcp-servers.md)
- [ ] 2026-07-23 — [OCR & Document Intelligence MCP Servers — PaddleOCR, MinerU, Docling, Marker, Mistral OCR, and More](content/reviews/ocr-document-intelligence-mcp-servers.md)
- [ ] 2026-07-23 — [Package Management & Dependency MCP Servers — npm, PyPI, Maven, Cargo, NuGet, WinGet, Homebrew, Version Checking, Vulnerability Scanning, and More](content/reviews/package-management-dependency-mcp-servers.md)
- [ ] 2026-07-23 — [Performance & Load Testing MCP Servers — k6, JMeter, Locust, Gatling, Artillery, and Lighthouse](content/reviews/performance-load-testing-mcp-servers.md)
- [ ] 2026-07-23 — [Personal Finance MCP Servers — YNAB, Plaid, Firefly III, QuickBooks, Alpaca, Monarch Money, and More](content/reviews/personal-finance-mcp-servers.md)
- [ ] 2026-07-23 — [Pet & Animal Care MCP Servers — Virtual Pets, Wildlife ID, Birding, Livestock Genetics, and Pet Adoption](content/reviews/pet-animal-care-mcp-servers.md)
- [ ] 2026-07-23 — [Pharmaceutical & Healthcare MCP Servers — FHIR, EHR Integration, Drug Discovery, PubMed, Medical Imaging, and More](content/reviews/pharmaceutical-healthcare-mcp-servers.md)
- [ ] 2026-07-23 — [Photography MCP Servers — Lightroom, Photoshop, GIMP, Photopea, Stock Photos, Image Optimization, Camera Control, RAW Processing, and More](content/reviews/photography-mcp-servers.md)
- [ ] 2026-07-23 — [Podcasting & Audio Content MCP Servers — MimikaStudio, ElevenLabs, MiniMax, Reaper DAW, Kokoro TTS, Suno Music, Podcast Workflows, and More](content/reviews/podcasting-audio-content-mcp-servers.md)
- [ ] 2026-07-23 — [Presentation & Slides MCP Servers — PowerPoint, Google Slides, Keynote, Canva, and More](content/reviews/presentation-slides-mcp-servers.md)
- [ ] 2026-07-23 — [Printing & 3D Printing MCP Servers — OctoPrint, FreeCAD, Fusion 360, SolidWorks, OpenSCAD, CUPS, Print-on-Demand, and More](content/reviews/printing-3d-printing-mcp-servers.md)
- [ ] 2026-07-23 — [Privacy & Data Protection MCP Servers — PII Redaction, GDPR, BigID, DataGrail, Pangea, and More](content/reviews/privacy-data-protection-mcp-servers.md)
- [ ] 2026-07-23 — [Prompt Engineering & Optimization MCP Servers — Optimizers, Template Managers, Multi-LLM Routers, Security Guards, and 25+ More](content/reviews/prompt-engineering-optimization-mcp-servers.md)
- [ ] 2026-07-23 — [Real Estate & Property MCP Servers — Zillow, MLS, Airbnb, BatchData, Mortgage Analysis, and More](content/reviews/real-estate-property-mcp-servers.md)
- [ ] 2026-07-23 — [Redis MCP Servers — The Official Server, Agent Memory, Cloud Management, and Community Alternatives](content/reviews/redis-mcp-servers.md)
- [ ] 2026-07-23 — [Regex & Text Processing MCP Servers — Pattern Matching, Diff, Translation, Format Conversion, Grammar, and Encoding](content/reviews/regex-text-processing-mcp-servers.md)
- [ ] 2026-07-23 — [Robotics & IoT MCP Servers — ROS, Home Assistant, MQTT, Arduino, Isaac Sim, and More](content/reviews/robotics-iot-mcp-servers.md)
- [ ] 2026-07-23 — [Robotics MCP Servers — ROS, Home Assistant, ESP32, Robot Arms, Drones, and More (Updated)](content/reviews/robotics-mcp-servers.md)
- [ ] 2026-07-23 — [SEO & Search Optimization MCP Servers — Google Search Console, Ahrefs, Semrush, DataForSEO, SE Ranking, Frase, Moz, Screaming Frog, and Google Trends](content/reviews/seo-search-optimization-mcp-servers.md)
- [ ] 2026-07-23 — [SQLite MCP Servers — From Anthropic's Reference Server to 139-Tool Powerhouses and Edge Database Solutions](content/reviews/sqlite-mcp-servers.md)
- [ ] 2026-07-23 — [Scientific Computing & Mathematics MCP Servers — MATLAB, Wolfram, R, Julia, SymPy, and More](content/reviews/scientific-computing-mathematics-mcp-servers.md)
- [ ] 2026-07-23 — [Secret Management MCP Servers — Vault, 1Password, Bitwarden, Infisical, and Beyond](content/reviews/secret-management-mcp-servers.md)
- [ ] 2026-07-23 — [Serverless & FaaS MCP Servers — AWS Lambda, Cloudflare Workers, Azure Functions, Google Cloud Run, Vercel, Firebase, and More](content/reviews/serverless-faas-mcp-servers.md)
- [ ] 2026-07-23 — [Smart Home & Home Automation MCP Servers — Home Assistant, Apple HomeKit, Samsung SmartThings, Amazon Alexa, Google Home, Philips Hue, Tuya, Zigbee2MQTT, and IoT Device Control](content/reviews/smart-home-automation-mcp-servers.md)
- [ ] 2026-07-23 — [Social Media & Marketing MCP Servers — Twitter/X, Bluesky, Instagram, LinkedIn, Meta Ads, Google Ads, SEO, and More](content/reviews/social-media-marketing-mcp-servers.md)
- [ ] 2026-07-23 — [Social Networking & Community MCP Servers — Twitter/X, Bluesky, LinkedIn, Reddit, Discord, Mastodon, YouTube, TikTok, and More](content/reviews/social-networking-community-mcp-servers.md)
- [ ] 2026-07-23 — [Speech Recognition & Transcription MCP Servers — Whisper, Deepgram, ElevenLabs, Groq, and More](content/reviews/speech-recognition-transcription-mcp-servers.md)
- [ ] 2026-07-23 — [Sports & Athletics MCP Servers — Live Scores, Fantasy Leagues, Betting Odds, Fitness Tracking, and Motorsport Telemetry](content/reviews/sports-athletics-mcp-servers.md)
- [ ] 2026-07-23 — [Sports & Fitness Analytics MCP Servers — Live Scores, F1 Telemetry, Betting Odds, Strava, Garmin, and Workout Tracking](content/reviews/sports-fitness-analytics-mcp-servers.md)
- [ ] 2026-07-23 — [Sports & Fitness MCP Servers — Strava, Garmin, Fitbit, F1, NFL, MLB, Soccer, and More](content/reviews/sports-fitness-mcp-servers.md)
- [ ] 2026-07-23 — [Spreadsheet & Office Suite MCP Servers — Google Sheets, Excel, Word, Google Docs, LibreOffice, Google Workspace, and More](content/reviews/spreadsheet-office-suite-mcp-servers.md)
- [ ] 2026-07-23 — [Spreadsheet MCP Servers — Google Sheets, Excel, Airtable, Smartsheet, and More](content/reviews/spreadsheet-mcp-servers.md)
- [ ] 2026-07-23 — [Supply Chain & Logistics MCP Servers — SAP, Dynamics 365, Kinaxis, ShipStation, Karrio, Shippo, and More](content/reviews/supply-chain-logistics-mcp-servers.md)
- [ ] 2026-07-23 — [Sustainability & Climate MCP Servers — Carbon Emissions, Building Energy, Air Quality, Power Grid Intelligence, ESG Reporting, and More](content/reviews/sustainability-climate-mcp-servers.md)
- [ ] 2026-07-23 — [Tax & Payroll MCP Servers — IRS Calculations, Tax Filing, VAT Compliance, Payroll Management, and International Tax Law](content/reviews/tax-payroll-mcp-servers.md)
- [ ] 2026-07-23 — [Telecommunications & Communications MCP Servers — Twilio, Telnyx, Vonage, Sinch, Plivo, Cisco Meraki, NetBox, UniFi, and More](content/reviews/telecommunications-communications-mcp-servers.md)
- [ ] 2026-07-23 — [Telecommunications & Messaging MCP Servers — SMS, Voice, WhatsApp, Telegram, CPaaS, and Unified Communications](content/reviews/telecommunications-messaging-mcp-servers.md)
- [ ] 2026-07-23 — [Terminal & CLI Tools MCP Servers — Shell Execution, tmux, SSH, and MCP Inspectors](content/reviews/terminal-cli-tools-mcp-servers.md)
- [ ] 2026-07-23 — [The Ahrefs MCP Server — SEO Intelligence for Your AI Agent](content/reviews/ahrefs-mcp-server.md)
- [ ] 2026-07-23 — [The Google Colab MCP Server — GPU-Powered Notebooks for Your AI Agent](content/reviews/google-colab-mcp-server.md)
- [ ] 2026-07-23 — [The HubSpot MCP Server — CRM Data at Your AI Agent's Fingertips](content/reviews/hubspot-mcp-server.md)
- [ ] 2026-07-23 — [The Semgrep MCP Server — Security Scanning for AI-Generated Code](content/reviews/semgrep-mcp-server.md)
- [ ] 2026-07-23 — [Threat Intelligence MCP Servers — CVE MCP (506 Stars, 27 Tools, 21 APIs), Google GTI, CrowdStrike Falcon v0.9.0, Microsoft Sentinel OFFICIAL, Elastic SIEM, Zscaler 300+ Tools, Team Cymru Pure Signal, Command Zero Autonomous SOC](content/reviews/threat-intelligence-mcp-servers.md)
- [ ] 2026-07-23 — [Time-Series Database MCP Servers — Grafana, ClickHouse, Prometheus, InfluxDB, VictoriaMetrics, SigNoz, and More](content/reviews/time-series-database-mcp-servers.md)
- [ ] 2026-07-23 — [Translation & Localization MCP Servers — DeepL, Crowdin, Phrase, Lokalise, Smartling, and More](content/reviews/translation-localization-mcp-servers.md)
- [ ] 2026-07-23 — [Transportation & Mobility MCP Servers — Public Transit, Flight Tracking, Ride-Hailing, Aviation Data, and Smart City Transport](content/reviews/transportation-mobility-mcp-servers.md)
- [ ] 2026-07-23 — [Travel & Tourism MCP Servers — Fli (2.1K Stars), Skiplagged Official, Airbnb, Amadeus GDS, Mapbox, Expedia, and More](content/reviews/travel-tourism-mcp-servers.md)
- [ ] 2026-07-23 — [Twilio MCP Server — All 2,000 Twilio APIs Available to Your AI Agent](content/reviews/twilio-mcp-server.md)
- [ ] 2026-07-23 — [Vector Database & Embedding MCP Servers — Qdrant, Chroma, Milvus, Pinecone, Weaviate, Redis, LanceDB, pgvector, and More](content/reviews/vector-database-embedding-mcp-servers.md)
- [ ] 2026-07-23 — [Veterinary & Pet Care MCP Servers — Animal Health, Livestock Genetics, Pet Management, and More](content/reviews/veterinary-pet-care-mcp-servers.md)
- [ ] 2026-07-23 — [Video Conferencing & Meeting Intelligence MCP Servers — Zoom Official, Joinly, Vexa, Otter.ai, Fireflies, tl;dv, and More](content/reviews/video-conferencing-mcp-servers.md)
- [ ] 2026-07-23 — [Video Production & Streaming MCP Servers — OBS, YouTube, HeyGen, Runway, Twitch, Mux, Remotion, Short-Video-Maker, and More](content/reviews/video-production-streaming-mcp-servers.md)
- [ ] 2026-07-23 — [Weather & Climate MCP Servers — Open-Meteo, OpenWeatherMap, NOAA/NWS, AccuWeather, Aviation METAR/TAF, Climatiq, Stormglass, and More](content/reviews/weather-climate-mcp-servers.md)
- [ ] 2026-07-23 — [Web Scraping & Crawling MCP Servers — Firecrawl, Crawl4AI, Bright Data, Apify, Jina Reader, and More](content/reviews/web-scraping-crawling-mcp-servers.md)
- [ ] 2026-07-23 — [Workflow Automation MCP Servers — n8n, Zapier, Make & More](content/reviews/workflow-automation-mcp-servers.md)
- [ ] 2026-07-23 — [Zapier MCP Server — 9,000+ Apps and 40,000+ Actions for AI Agents](content/reviews/zapier-mcp-server.md)
- [ ] 2026-07-24 — [API Development MCP Servers — OpenAPI Converters, GraphQL, gRPC, and the Rise of Spec-to-Server Generation](content/reviews/api-development-mcp-servers.md)
- [ ] 2026-07-24 — [AWS Bedrock MCP Servers — The Cloud Giant's MCP Arsenal (Refreshed June 2026)](content/reviews/aws-bedrock-mcp-server.md)
- [ ] 2026-07-24 — [Airtable MCP Server — Full Database CRUD for Your AI Agent](content/reviews/airtable-mcp-server.md)
- [ ] 2026-07-24 — [Anyquery MCP Server — SQL Everything: Query 40+ Apps, Files, and Databases from Your AI Agent](content/reviews/anyquery-mcp-server.md)
- [ ] 2026-07-24 — [Apify MCP Server — 3,000+ Scrapers at Your AI Agent's Fingertips](content/reviews/apify-mcp-server.md)
- [ ] 2026-07-24 — [Bitbucket MCP Servers — The Missing Piece in Atlassian's AI Strategy](content/reviews/bitbucket-mcp-server.md)
- [ ] 2026-07-24 — [Bright Data MCP Server — Enterprise Web Access That Actually Beats Anti-Bot Protection](content/reviews/bright-data-mcp-server.md)
- [ ] 2026-07-24 — [CI/CD MCP Servers — Build Pipelines Get an AI Interface](content/reviews/ci-cd-mcp-servers.md)
- [ ] 2026-07-24 — [Code Generation MCP Servers — UI Components, Context Providers, and the Paradox of AI Writing Its Own Tools](content/reviews/code-generation-mcp-servers.md)
- [ ] 2026-07-24 — [Code Review & Pull Request MCP Servers — SonarQube, Codacy, CodeRabbit, Azure DevOps, Graphite GT, GitLab MR, Community PR Reviewers](content/reviews/code-review-pull-request-mcp-servers.md)
- [ ] 2026-07-24 — [Cohere MCP Server — Enterprise AI's North Star Meets the Model Context Protocol](content/reviews/cohere-mcp-server.md)
- [ ] 2026-07-24 — [Composio MCP Server — 500+ App Integrations Through a Single Endpoint](content/reviews/composio-mcp-server.md)
- [ ] 2026-07-24 — [Database Migration & Schema Management MCP Servers — Google Toolbox Hits v1.0 GA, boringSQL/dryrun Adds Offline Safety Analysis, Core Gaps Remain](content/reviews/database-migration-mcp-servers.md)
- [ ] 2026-07-24 — [Docker MCP Servers — Container Management Gets an AI Layer (Plus the MCP Catalog That Hosts 300+ Others)](content/reviews/docker-mcp-servers.md)
- [ ] 2026-07-24 — [Documentation Tooling MCP Servers — Google Developer Knowledge API Goes Official, GitBook Auto-MCP Joins Platform Wave, llms.txt Emerges as Documentation Standard](content/reviews/documentation-tooling-mcp-servers.md)
- [ ] 2026-07-24 — [Dropbox MCP Servers — AI Agents That Browse Files, Search Across Apps, and Manage Cloud Storage](content/reviews/dropbox-mcp-server.md)
- [ ] 2026-07-24 — [GitHub MCP Server — The World's Largest Dev Platform Gets an Official AI Interface](content/reviews/github-mcp-server.md)
- [ ] 2026-07-24 — [GitLab MCP Servers — The Self-Hosted DevOps Platform's Growing AI Interface](content/reviews/gitlab-mcp-server.md)
- [ ] 2026-07-24 — [Google Drive MCP Servers — AI Agents That Search, Read, Edit, and Organize Your Cloud Documents](content/reviews/google-drive-mcp-server.md)
- [ ] 2026-07-24 — [Google Gemini MCP Servers — The Largest Official MCP Server Ecosystem](content/reviews/gemini-mcp-server.md)
- [ ] 2026-07-24 — [Hugging Face MCP Server — The AI Community Hub Meets the Model Context Protocol](content/reviews/huggingface-mcp-server.md)
- [ ] 2026-07-24 — [IDE & Code Editor MCP Servers — Your Editor as an AI-Accessible Tool](content/reviews/ide-code-editor-mcp-servers.md)
- [ ] 2026-07-24 — [Infrastructure as Code MCP Servers — Terraform, Pulumi, and the IaC Vendors Building AI-Native Infrastructure Workflows](content/reviews/infrastructure-as-code-mcp-servers.md)
- [ ] 2026-07-24 — [Kubernetes MCP Servers — Cluster Management Gets an AI Interface](content/reviews/kubernetes-mcp-servers.md)
- [ ] 2026-07-24 — [Logging & Tracing MCP Servers — Splunk v1.1.1 Doubles Adoption, SigNoz Surges, Logfire Archived](content/reviews/logging-tracing-mcp-servers.md)
- [ ] 2026-07-24 — [Mailtrap MCP Server — Send Transactional Emails From Your AI Agent](content/reviews/mailtrap-mcp-server.md)
- [ ] 2026-07-24 — [Meta Llama MCP Servers — AI Agents for Llama 4, Ollama, and the Open-Weight LLM Ecosystem](content/reviews/meta-llama-mcp-server.md)
- [ ] 2026-07-24 — [MindsDB MCP Server — Federated Queries Across 200+ Data Sources From a Single Interface](content/reviews/mindsdb-mcp-server.md)
- [ ] 2026-07-24 — [Mistral AI MCP Server — Europe's Open-Weight Champion Embraces the Model Context Protocol](content/reviews/mistral-mcp-server.md)
- [ ] 2026-07-24 — [Monitoring & Observability MCP Servers — From Grafana to Datadog, Vendor-Led Observability Meets MCP](content/reviews/monitoring-observability-mcp-servers.md)
- [ ] 2026-07-24 — [MySQL MCP Servers — The World's Most Popular Database Meets AI](content/reviews/mysql-mcp-server.md)
- [ ] 2026-07-24 — [New Relic MCP Server — AI-Powered Observability with NRQL Queries, Alerts, Entity Discovery, and Log Analysis](content/reviews/new-relic-mcp-server.md)
- [ ] 2026-07-24 — [Nimble MCP Server — Enterprise Web Intelligence With the Best Google Maps Tools](content/reviews/nimble-mcp-server.md)
- [ ] 2026-07-24 — [OneDrive MCP Servers — AI Agents That Manage Your Microsoft 365 Files, Email, Calendar, and Teams](content/reviews/onedrive-mcp-server.md)
- [ ] 2026-07-24 — [OpenAI MCP Servers — AI Agents for GPT-5.5, o3, DALL-E, and the OpenAI API Platform](content/reviews/openai-mcp-server.md)
- [ ] 2026-07-24 — [Oxylabs MCP Server — Two Scraping Engines in One, With the Fastest Stress Test Times](content/reviews/oxylabs-mcp-server.md)
- [ ] 2026-07-24 — [Package Management MCP Servers — NuGet, npm, PyPI, Maven, and the Quest for AI-Assisted Dependency Intelligence](content/reviews/package-management-mcp-servers.md)
- [ ] 2026-07-24 — [PayPal MCP Server — AI-Powered Payment Processing with Invoicing, Orders, Subscriptions, and Agentic Commerce](content/reviews/paypal-mcp-server.md)
- [ ] 2026-07-24 — [Pipedream MCP Server — 10,000+ Tools Across 3,000 APIs With Managed OAuth](content/reviews/pipedream-mcp-server.md)
- [ ] 2026-07-24 — [PostgreSQL MCP Servers — The Database That Ate the World Gets an AI Interface](content/reviews/postgresql-mcp-server.md)
- [ ] 2026-07-24 — [Postmark MCP Server — Send Transactional Emails From Your AI Agent](content/reviews/postmark-mcp-server.md)
- [ ] 2026-07-24 — [Prisma MCP Server — Dual-Mode Database Management for AI Agents](content/reviews/prisma-mcp-server.md)
- [ ] 2026-07-24 — [Profiling & Performance MCP Servers — k6 Official MCP, JMeter, Gatling, hotpath-rs Rust, JProfiler, CodSpeed, Grafana Pyroscope](content/reviews/profiling-performance-mcp-servers.md)
- [ ] 2026-07-24 — [Resend MCP Server — The Developer-First Email API With Full AI Agent Access](content/reviews/resend-mcp-server.md)
- [ ] 2026-07-24 — [SQL Server MCP Servers — Enterprise Database Gets AI-Powered Performance Monitoring](content/reviews/sql-server-mcp-server.md)
- [ ] 2026-07-24 — [Salesforce DX MCP Server — AI-Powered Salesforce Development with 60+ Tools for LWC, Metadata, DevOps, and SOQL](content/reviews/salesforce-dx-mcp-server.md)
- [ ] 2026-07-24 — [ScrapingBee MCP Server — Give Your AI Agent Eyes on the Live Web](content/reviews/scrapingbee-mcp-server.md)
- [ ] 2026-07-24 — [Security Scanning MCP Servers — Enterprise Vendors Pile In as Agentic Security Goes Mainstream](content/reviews/security-scanning-mcp-servers.md)
- [ ] 2026-07-24 — [Shopify Dev MCP Server — AI-Powered Shopify Development with Docs, Schema, and Code Validation](content/reviews/shopify-dev-mcp-server.md)
- [ ] 2026-07-24 — [Snowflake MCP Server — AI-Powered Data Platform Access with Cortex AI, SQL Orchestration, and Semantic Views](content/reviews/snowflake-mcp-server.md)
- [ ] 2026-07-24 — [Spotify MCP Server Review — Playback, Playlists & More](content/reviews/spotify-mcp-server.md)
- [ ] 2026-07-24 — [Square MCP Server — AI-Powered Commerce with Payments, Orders, Inventory, Loyalty, and Full API Access](content/reviews/square-mcp-server.md)
- [ ] 2026-07-24 — [Testing & QA MCP Servers — From Browser Automation to Mobile, Cloud, and Test Runner Integration](content/reviews/testing-qa-mcp-servers.md)
- [ ] 2026-07-24 — [The Chrome DevTools MCP Server — Browser Debugging and Performance Profiling for AI Coding Agents](content/reviews/chrome-devtools-mcp-server.md)
- [ ] 2026-07-24 — [The DuckDuckGo MCP Server — Free Web Search for AI Agents (No API Key Required)](content/reviews/duckduckgo-mcp-server.md)
- [ ] 2026-07-24 — [The GreptimeDB MCP Server — Observability Data Meets AI Agents](content/reviews/greptimedb-mcp-server.md)
- [ ] 2026-07-24 — [The ReactBits MCP Server — 135+ Animated React Components for AI Coding Agents](content/reviews/reactbits-mcp-server.md)
- [ ] 2026-07-24 — [Turso MCP Server — The 17.9K-Star SQLite Database With Built-In AI Agent Access](content/reviews/turso-mcp-server.md)
- [ ] 2026-07-24 — [Windows-MCP Server — Give Your AI Agent Eyes and Hands on Windows](content/reviews/windows-mcp-server.md)
- [ ] 2026-07-24 — [Zoom MCP Servers — AI Agents That Manage Meetings, Retrieve Transcripts, and Access Recordings](content/reviews/zoom-mcp-server.md)
- [ ] 2026-07-24 — [iCloud MCP Servers — Calendar, Mail, Contacts & More](content/reviews/icloud-mcp-server.md)
- [ ] 2026-07-24 — [n8n MCP Server — Build, Expose, and Orchestrate Workflows with AI](content/reviews/n8n-mcp-server.md)

