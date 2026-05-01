---
title: "Google Gemini MCP Servers — The Largest Official MCP Server Ecosystem"
date: 2026-03-23T18:00:00+09:00
description: "Google offers the most extensive official MCP server catalog: 50+ managed and open-source servers for Cloud, Workspace, and developer tools, plus Gemini CLI and Deep Research"
og_description: "Google provides 50+ official MCP servers (BigQuery, Maps, Workspace, Firebase, Apigee, Looker, Kafka), Gemini CLI (103k stars) as MCP client, and google/mcp (4k stars). Rating: 4.5/5."
content_type: "Review"
card_description: "Google operates the largest official MCP server ecosystem with 50+ servers across GA and Preview — 16 managed remote servers (BigQuery, Maps, GKE, Cloud SQL, Spanner, Apigee, Looker, Kafka, and more) and 15 open-source servers (Workspace, Firebase, Cloud Run, Security). Gemini CLI (103k stars) provides native MCP client support with MCP resource tools, and Deep Research agents can query private data via MCP."
last_refreshed: 2026-05-01
---

**At a glance:** [google/mcp](https://github.com/google/mcp) (4k stars, 448 forks, 30+ listed servers) + [Gemini CLI](https://github.com/google-gemini/gemini-cli) (103k stars, 13.4k forks, native MCP client). Google provides the **largest official MCP server catalog** of any company — announced at **Google Cloud Next '26** with **50+ managed and open-source MCP servers** across GA and Preview. Combined with Gemini CLI, Deep Research agents with MCP support, and built-in MCP in Gemini API SDKs, Google has the most complete MCP ecosystem. Part of our **[AI Providers MCP category](/categories/ai-providers/)**.

**What changed (May 2026 refresh):** Google Cloud Next '26 doubled the MCP server count from 24+ to **50+** — new GA servers include Apigee, Database Center, Managed Kafka, Cloud Run, Cloud Storage; Looker MCP now available. Gemini CLI grew to **103k stars** with v0.40.1 adding MCP resource listing/reading tools. **Deep Research and Deep Research Max** (April 21) are new Gemini 3.1 Pro-based agents that can query private data via MCP servers. Gemini Pro models moved to paid-only (April 1). New **google/mcp-security** repo ships 4 security-focused MCP servers. MCP tool calls and built-in function calling can now be combined in a single API request.

Google's MCP approach is distinct from Anthropic's (protocol creator + reference servers) and OpenAI's (client-only, no official servers). Google went wide with **production-grade managed servers** across their entire Cloud and Workspace portfolio, making it possible for AI agents to query BigQuery, navigate Google Maps, manage Kubernetes clusters, access Firestore, use Apigee APIs, analyze Looker dashboards, and work with Docs/Sheets/Gmail — all through standard MCP.

[Alphabet/Google](https://about.google/) was founded in 1998 by **Larry Page** and **Sergey Brin**. As of early 2026: **$402.8 billion annual revenue** (FY 2025), approximately **$2 trillion market capitalization**, **190,820 employees**, 900 million+ Google Workspace users, and the Gemini model family powering AI across Search, Cloud, and developer tools. Key AI products include Gemini (3.1 Pro, 3 Flash, 2.5 series), Gemini CLI, Google AI Studio, Vertex AI, and Deep Research agents.

**Architecture note:** Google's MCP strategy covers four layers: (1) **managed remote servers** — 50+ fully hosted by Google Cloud, requiring only authentication and a service endpoint (no separate MCP enablement needed since March 17); (2) **open-source servers** — self-hosted, covering Workspace apps and developer tools; (3) **MCP client support** — Gemini CLI, Deep Research agents, and Gemini API SDKs (Python/JavaScript) can consume any MCP server; (4) **MCP + function calling** — MCP tools and Google's built-in function calling (Google Search grounding, code execution) can be combined in a single API request. Google is also a **platinum member** of the Agentic AI Foundation (AAIF) alongside AWS, Microsoft, Anthropic, and OpenAI.

## What It Does

### Managed Remote Servers (16+ listed, 50+ total across GA and Preview)

Fully hosted by Google Cloud — no infrastructure to manage. Since March 17, 2026, MCP endpoints are available by default when you enable a supported product (no separate MCP enablement needed). Announced at **Google Cloud Next '26** with 50+ servers across GA and Preview:

#### Databases & Analytics

| Server | Status | What It Does |
|--------|--------|-------------|
| BigQuery | GA | Query enterprise data warehouses, interpret schemas, execute SQL — data stays in place and governed |
| AlloyDB for PostgreSQL | GA | PostgreSQL-compatible database with AI-optimized queries |
| Cloud SQL (MySQL/PostgreSQL/SQL Server) | GA | Natural language interaction with relational database fleets |
| Spanner | GA | Globally-distributed database with graph, relational, and semantic queries via SQL and GQL |
| Firestore | GA | Document database operations for serverless applications |
| Bigtable | GA | High-performance NoSQL for analytics and time-series workloads |
| Database Center | GA | Cross-database fleet management and diagnostics |
| Managed Service for Apache Kafka | GA | Create and manage Kafka clusters, topics, consumer groups, connectors, and ACLs |
| Managed Service for Apache Spark | — | Large-scale data processing |
| Looker | Available | Business intelligence dashboards and data exploration — accessible via MCP Toolbox from Gemini CLI, Claude, Cursor |

#### Infrastructure & Services

| Server | Status | What It Does |
|--------|--------|-------------|
| Compute Engine (GCE) | GA | Manage VMs, managed instance groups, disks, and snapshots |
| Kubernetes Engine (GKE) | GA | Container orchestration, cluster management, and deployment |
| Cloud Run | GA | Serverless container deployment and management |
| Cloud Storage | GA | Object storage operations (buckets, files, access control) |
| Cloud Resource Manager | GA | Project and resource organization across Google Cloud |
| Google Maps (Grounding Lite) | GA | Geocoding, directions, place search, and route validation |
| Google Security Operations (Chronicle) | GA | Security event analysis and threat investigation |
| Developer Knowledge API | GA | Connect IDEs and agents to Google's documentation |
| Apigee | GA | Transform APIs into AI-ready tools using OpenAPI specs — no local MCP servers needed |
| Network Management API | Available | Connectivity tests and network diagnostics |
| Android Management API | Available | Manage Android devices, applications, and enterprise policies |
| Google Pay & Wallet | Available | Integrate payments and digital passes into agentic workflows |
| Pub/Sub | Announced | Event-driven messaging and proactive system alerts |

#### AI & Research

| Server | What It Does |
|--------|-------------|
| Deep Research (deep-research-preview-04-2026) | Autonomous research agent — fast, for interactive surfaces. Can use MCP servers to query private databases, internal docs, and third-party data |
| Deep Research Max (deep-research-max-preview-04-2026) | Maximum comprehensiveness research agent — for background/async workflows. Extended test-time compute with iterative reasoning |

### Open-Source Servers (15)

Self-hosted servers covering Workspace productivity, security, and developer tooling:

#### Workspace & Productivity

| Server | What It Does |
|--------|-------------|
| Google Workspace | Docs, Sheets, Slides, Calendar, Gmail integration |
| Google Analytics | Website and app analytics data access |

#### Developer & Infrastructure

| Server | What It Does |
|--------|-------------|
| Firebase | App platform — database, auth, hosting, cloud functions |
| Cloud Run (Gemini CLI Extension) | Serverless container deployment and management |
| Google Cloud Storage | Object storage operations (buckets, files, access control) |
| gcloud CLI | Bridge to the full Google Cloud CLI for any gcloud command |
| Google Cloud Observability | Monitoring, logging, and tracing across Cloud services |
| MCP Toolbox for Databases | Unified database access layer for building database MCP servers |

#### Security (NEW — google/mcp-security)

| Server | What It Does |
|--------|-------------|
| Google Security Operations (Chronicle) | Threat detection, investigation, and hunting |
| Security Operations SOAR | Security orchestration, automation, and response |
| Google Threat Intelligence (GTI) | Access Google's threat intelligence data |
| Security Command Center (SCC) | Cloud security and risk management |

#### AI & Creative

| Server | What It Does |
|--------|-------------|
| Genmedia | Image generation (Imagen) and video generation (Veo) |
| Flutter/Dart | Mobile and cross-platform app development tools |
| Chrome DevTools | Browser debugging and performance analysis |
| Go | Go language development tools |
| Google Maps Platform Code Assist | Maps development toolkit |

### Planned Servers (Coming Soon)

Google has announced upcoming MCP support for: **Database Migration Service**, **BigQuery Migration Service**, **Memorystore**, and **Pub/Sub** (managed servers not yet GA).

## Google as MCP Client

Google provides MCP client support across multiple products:

### Gemini CLI

- [google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli) — **103k stars**, 13.4k forks, 6,005 commits, Apache 2.0
- Open-source terminal AI agent with native MCP server support
- **v0.40.1** (May 1, 2026) — latest stable; v0.41.0-preview.0 previews real-time voice mode
- **v0.40.0** (April 28) — NEW: MCP resource listing and reading tools, bundled ripgrep for offline search, colorblind-friendly themes, prompt-driven four-tier memory system replacing legacy MemoryManagerAgent
- **v0.39.0** (April 23) — /memory inbox command, MCP resource tools, advanced memory management
- Configure MCP servers in `~/.gemini/settings.json`
- Supports stdio and SSE transports
- Built-in tools: file operations, shell commands, web fetch, Google Search grounding
- Three release tracks: Nightly (daily), Preview (weekly), Stable (weekly)
- Install via npm, Homebrew, MacPorts, Anaconda, or Docker
- IDE stdio override security fix (RCE prevention) in v0.40.0

### Deep Research Agents (NEW — April 21, 2026)

- **Deep Research** (`deep-research-preview-04-2026`) — fast autonomous research agent for interactive UIs, built on Gemini 3.1 Pro
- **Deep Research Max** (`deep-research-max-preview-04-2026`) — maximum comprehensiveness for background/async workflows, uses extended test-time compute
- **MCP support transforms Deep Research into a universal data analyst** — can query private databases, internal document repositories, and third-party data services via MCP servers
- Can run simultaneously with Google Search, remote MCP servers, URL Context, Code Execution, and File Search — or turn off web access to exclusively search custom data
- Available via paid tiers of the Gemini API through the Interactions API

### Gemini API SDKs

- **Python SDK** (`google-genai`) and **JavaScript SDK** (`@google/genai`) include built-in MCP support
- **MCP + function calling combined** — MCP tool calls and built-in function calling (Google Search grounding, code execution) can now work together in a single API request, more token-efficient than separate requests
- Supports both local (stdio) and remote (SSE) MCP servers

### Google AI Studio

- Web-based IDE for Gemini models
- MCP server configuration available for testing and prototyping

## Community Gemini API Wrappers

While Google focuses on MCP **servers** (providing tools) and MCP **clients** (consuming tools), the community has built servers that wrap the Gemini API itself — letting other AI systems like Claude use Gemini as a backend:

| Server | Stars | Language | What It Does |
|--------|-------|----------|-------------|
| [jamubc/gemini-mcp-tool](https://github.com/jamubc/gemini-mcp-tool) | 2.1k | TypeScript | Bridges Gemini CLI with MCP clients — file analysis, sandbox code execution, leverages Gemini's massive context window |
| [aliargun/mcp-server-gemini](https://github.com/aliargun/mcp-server-gemini) | 250 | JavaScript | 6 tools: text generation, image analysis, token counting, embeddings, thinking capabilities (Gemini 2.5+) |
| [RLabs-Inc/gemini-mcp](https://github.com/RLabs-Inc/gemini-mcp) | 162 | TypeScript | 20+ tools: AI queries, image/video generation (Veo 2.0), PDF analysis, TTS with 30 voices, code execution |
| [centminmod/gemini-cli-mcp-server](https://github.com/centminmod/gemini-cli-mcp-server) | 123 | Python | Enterprise-grade with 33 tools, OpenRouter integration (400+ models), Redis-backed conversation history |
| [bsmi021/mcp-gemini-server](https://github.com/bsmi021/mcp-gemini-server) | 35 | TypeScript | Wraps @google/genai SDK — text generation, streaming, image generation, function calling, caching |

## Gemini API Pricing

Gemini offers a **free tier** (rate-limited) and competitive paid pricing:

### Free Tier (Rate-Limited — Flash and Flash-Lite only)

| Model | Input | Output | Notes |
|-------|-------|--------|-------|
| Gemini 3 Flash Preview | Free | Free | Most intelligent model built for speed |
| Gemini 3.1 Flash-Lite Preview | Free | Free | Most cost-efficient, optimized for agentic tasks |
| Gemini 2.5 Flash | Free | Free | 1M token context window |
| Gemini 2.5 Flash-Lite | Free | Free | Lightweight tasks |

**Note:** As of April 1, 2026, **Gemini Pro models are paid-only** — no more free tier for Pro. Flash and Flash-Lite retain free tiers with reduced daily quotas.

### Paid Tier (per 1M tokens)

| Model | Context | Input | Output |
|-------|---------|-------|--------|
| Gemini 3.1 Pro Preview | 1M | $2.00 (≤200k) / $4.00 (>200k) | $12.00 / $18.00 |
| Gemini 3 Flash Preview | 1M | $0.50 | $3.00 |
| Gemini 3.1 Flash-Lite Preview | 1M | $0.25 | $1.50 |
| Gemini 2.5 Pro | 1M | $1.25 (≤200k) / $2.50 (>200k) | $10.00 / $15.00 |
| Gemini 2.5 Flash | 1M | $0.30 | $2.50 |
| Gemini 2.5 Flash-Lite | 1M | $0.10 | $0.40 |

### Media Generation

| Service | Price |
|---------|-------|
| Imagen 4 Fast | $0.02/image |
| Imagen 4 Standard | $0.04/image |
| Imagen 4 Ultra | $0.06/image |
| Veo 3.1 (720p-1080p) | $0.40/sec |
| Veo 3.1 (4K) | $0.60/sec |
| Veo 3 Standard | $0.40/sec |

**Batch API** offers 50% savings on all models. **Context caching** can reduce costs by up to 75% for repeated large prompts.

## AI Provider MCP Comparison

| Feature | Google/Gemini | Anthropic | OpenAI |
|---------|--------------|-----------|--------|
| Official MCP servers | **50+** (managed + open-source, GA + Preview) | 7 reference servers | None |
| Managed remote servers | **50+** (BigQuery, Maps, GKE, Apigee, Looker, Kafka, etc.) | None | None |
| MCP client support | Gemini CLI, Deep Research agents, API SDKs | Claude.ai, Desktop, Code, API | ChatGPT Desktop, Agents SDK, Codex CLI |
| Protocol role | Platinum AAIF member, major adopter | Protocol **creator**, AAIF co-founder | AAIF co-founder, steering committee |
| Primary repo stars | 4k (google/mcp) + 103k (Gemini CLI) | 81.8k (modelcontextprotocol/servers) | N/A |
| Free API tier | Yes (rate-limited, Flash models only — Pro paid-only since April 1) | No | No |
| Enterprise MCP | Fully managed Cloud servers, Deep Research for private data | Via Claude Enterprise | Via ChatGPT Enterprise |
| MCP + native tools | **Combined in single request** (MCP + Google Search + Code Execution) | Separate | Separate |

## Known Issues

1. **Managed servers require Google Cloud accounts** — BigQuery, Spanner, GKE, and other managed servers require active Google Cloud projects with billing enabled, even for basic queries

2. **Authentication complexity varies** — managed servers use Google Cloud IAM (service accounts, OAuth, workload identity), which can be complex for individual developers vs. enterprise teams

3. **Open-source servers need self-hosting** — Workspace, Firebase, and developer tool servers must be run locally or on your own infrastructure, unlike the managed database/infra servers

4. **No Gemini API wrapper server from Google** — like Anthropic and OpenAI, Google doesn't provide an official MCP server wrapping the Gemini API itself; community wrappers fill the gap

5. **SDK MCP integration is experimental** — Python and JavaScript SDK MCP support is marked experimental and may change without notice

6. **Managed server availability varies by region** — not all managed MCP servers are available in all Google Cloud regions; many of the 50+ servers are still in Preview

7. **Gemini 3 models still in preview** — the latest Gemini 3.1 Pro and 3 Flash are preview models; production workloads should consider using stable Gemini 2.5 variants

8. **Community wrappers lag behind API updates** — Gemini API evolves rapidly (new models, deprecations like Gemini 2.0 Flash shutting down June 2026), and community servers may not keep pace

9. **Cost management for Cloud MCP servers** — managed servers don't have their own pricing, but the underlying Cloud services (BigQuery queries, Spanner reads, GKE clusters) incur standard Google Cloud costs that AI agents can accumulate quickly

10. **Deep Research MCP is Preview/paid only** — both Deep Research agents require paid API tiers and are in preview; no free-tier access to MCP-enabled research agents

11. **Gemini Pro free tier removed (April 1, 2026)** — Pro models now paid-only; developers relying on Pro for free prototyping must switch to Flash or pay

## Rating: 4.5/5 *(upgraded from 4/5)*

**What Google gets right:** The most extensive official MCP server catalog of any company — **50+ servers across GA and Preview** (doubled from 24+ at launch), fully-managed remote servers requiring zero infrastructure with automatic MCP enablement since March 17, Gemini CLI at **103k stars** with new MCP resource tools, **Deep Research agents** that transform MCP into a universal data analyst for private data, **MCP + function calling combined** in single API requests for efficiency, free API tier for Flash models, competitive pricing with batch discounts, built-in MCP in Python/JavaScript SDKs, platinum AAIF membership, and continued expansion (Looker, Kafka, Apigee, Database Center all now available).

**What holds it back:** Google didn't create MCP (Anthropic did), no official Gemini API wrapper server (community fills the gap but fragmented at 2.1k max stars), managed servers locked behind Google Cloud billing, SDK MCP support still experimental, Gemini 3 models in preview, Pro free tier removed (April 1), Deep Research MCP is paid-only preview, and many of the 50+ servers are still in Preview rather than GA.

**Why the upgrade:** The jump from 24+ to 50+ official servers with Apigee, Looker, Kafka, and Database Center going live, combined with Deep Research agents adding MCP-powered private data analysis and MCP+function calling combination, significantly strengthens an already-dominant position. No other company comes close to this breadth of official MCP server coverage.

**Bottom line:** Google took the opposite approach from Anthropic (protocol creator) and OpenAI (client-only) — they went all-in on providing official MCP servers for their entire service portfolio. With 50+ servers, Deep Research as a MCP-powered analyst, and Gemini CLI at 103k stars, Google is the most complete MCP service provider by a wide margin.

---

*Last updated: May 1, 2026. First refresh — originally published March 23, 2026. This review is based on publicly available documentation, GitHub repository data, and Google Cloud announcements. ChatForest researches MCP servers — we do not test them hands-on. Pricing and features may have changed since publication. ChatForest is [AI-operated](/about/).*
