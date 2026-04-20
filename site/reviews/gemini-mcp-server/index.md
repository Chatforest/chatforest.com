# Google Gemini MCP Servers — The Largest Official MCP Server Ecosystem

> Google offers the most extensive official MCP server catalog: 12 managed remote servers for Cloud services, 12 open-source servers for Workspace and developer tools, plus Gemini


**At a glance:** [google/mcp](https://github.com/google/mcp) (3.4k stars, 364 forks, 24+ official servers) + [Gemini CLI](https://github.com/google-gemini/gemini-cli) (98.7k stars, 12.5k forks, native MCP client). Google provides the **largest official MCP server catalog** of any company — 12 fully-managed remote servers for Google Cloud databases and infrastructure, 12 open-source servers for Workspace and developer tools, and built-in MCP support in Gemini CLI and the Gemini API SDKs. Part of our **[AI Providers MCP category](/categories/ai-providers/)**.

Google's MCP approach is distinct from Anthropic's (protocol creator + reference servers) and OpenAI's (client-only, no official servers). Google went wide with **production-grade managed servers** across their entire Cloud and Workspace portfolio, making it possible for AI agents to query BigQuery, navigate Google Maps, manage Kubernetes clusters, access Firestore, and work with Docs/Sheets/Gmail — all through standard MCP.

[Alphabet/Google](https://about.google/) was founded in 1998 by **Larry Page** and **Sergey Brin**. As of early 2026: **$402.8 billion annual revenue** (FY 2025), approximately **$2 trillion market capitalization**, **190,820 employees**, 900 million+ Google Workspace users, and the Gemini model family powering AI across Search, Cloud, and developer tools. Key AI products include Gemini (3.1 Pro, 3 Flash, 2.5 series), Gemini CLI, Google AI Studio, and Vertex AI.

**Architecture note:** Google's MCP strategy covers three layers: (1) **managed remote servers** — fully hosted by Google Cloud, requiring only authentication and a service endpoint; (2) **open-source servers** — self-hosted, covering Workspace apps and developer tools; (3) **MCP client support** — Gemini CLI and Gemini API SDKs (Python/JavaScript) can consume any MCP server. Google is also a **platinum member** of the Agentic AI Foundation (AAIF) alongside AWS, Microsoft, Anthropic, and OpenAI.

## What It Does

### Managed Remote Servers (12)

Fully hosted by Google Cloud — no infrastructure to manage. These connect AI agents directly to Google's enterprise services:

#### Databases & Analytics

| Server | What It Does |
|--------|-------------|
| BigQuery | Query enterprise data warehouses, interpret schemas, execute SQL — data stays in place and governed |
| AlloyDB for PostgreSQL | PostgreSQL-compatible database with AI-optimized queries |
| Cloud SQL | Natural language interaction with MySQL, PostgreSQL, and SQL Server fleets |
| Spanner | Globally-distributed database with graph, relational, and semantic queries via SQL and GQL |
| Firestore | Document database operations for serverless applications |
| Bigtable | High-performance NoSQL for analytics and time-series workloads |

#### Infrastructure & Services

| Server | What It Does |
|--------|-------------|
| Compute Engine (GCE) | Manage virtual machines and compute infrastructure |
| Kubernetes Engine (GKE) | Container orchestration, cluster management, and deployment |
| Cloud Resource Manager | Project and resource organization across Google Cloud |
| Google Maps (Grounding Lite) | Geocoding, directions, place search, and route validation |
| Google Security Operations (Chronicle) | Security event analysis and threat investigation |
| Developer Knowledge API | Connect IDEs and agents to Google's documentation |

### Open-Source Servers (12)

Self-hosted servers covering Workspace productivity and developer tooling:

#### Workspace & Productivity

| Server | What It Does |
|--------|-------------|
| Google Workspace | Docs, Sheets, Slides, Calendar, Gmail integration |
| Google Analytics | Website and app analytics data access |

#### Developer & Infrastructure

| Server | What It Does |
|--------|-------------|
| Firebase | App platform — database, auth, hosting, cloud functions |
| Cloud Run | Serverless container deployment and management |
| Cloud Storage | Object storage operations (buckets, files, access control) |
| gcloud CLI | Bridge to the full Google Cloud CLI for any gcloud command |
| Google Cloud Observability | Monitoring, logging, and tracing across Cloud services |

#### AI & Creative

| Server | What It Does |
|--------|-------------|
| Genmedia | Image generation (Imagen) and video generation (Veo) |
| Flutter/Dart | Mobile and cross-platform app development tools |
| Chrome DevTools | Browser debugging and performance analysis |
| Go | Go language development tools |
| MCP Toolbox for Databases | Unified database access layer for building database MCP servers |

### Planned Servers (Coming Soon)

Google has announced upcoming MCP support for: **Looker**, **Database Migration Service**, **BigQuery Migration Service**, **Memorystore**, **Database Center**, **Pub/Sub**, and **Kafka**.

## Google as MCP Client

Google provides MCP client support across multiple products:

### Gemini CLI

- [google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli) — **98.7k stars**, 12.5k forks, 5,428 commits, Apache 2.0
- Open-source terminal AI agent with native MCP server support
- Configure MCP servers in `~/.gemini/settings.json`
- Supports stdio and SSE transports
- Built-in tools: file operations, shell commands, web fetch, Google Search grounding
- Three release tracks: Nightly (daily), Preview (weekly), Stable (weekly)
- Install via npm, Homebrew, MacPorts, Anaconda, or Docker

### Gemini API SDKs

- **Python SDK** (`google-genai`) and **JavaScript SDK** (`@google/genai`) include built-in MCP support
- Experimental — connect directly to MCP servers and use their tools with Gemini models
- API automatically calls MCP tools when needed
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

### Free Tier (Rate-Limited)

| Model | Input | Output | Notes |
|-------|-------|--------|-------|
| Gemini 3 Flash Preview | Free | Free | Most intelligent model built for speed |
| Gemini 3.1 Flash-Lite Preview | Free | Free | Most cost-efficient, optimized for agentic tasks |
| Gemini 2.5 Flash | Free | Free | 1M token context window |
| Gemini 2.5 Flash-Lite | Free | Free | Lightweight tasks |

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
| Official MCP servers | **24+** (12 managed + 12 open-source) | 7 reference servers | None |
| Managed remote servers | **12** (BigQuery, Maps, GKE, etc.) | None | None |
| MCP client support | Gemini CLI, API SDKs | Claude.ai, Desktop, Code, API | ChatGPT Desktop, Agents SDK, Codex CLI |
| Protocol role | Platinum AAIF member, major adopter | Protocol **creator**, AAIF co-founder | AAIF co-founder, steering committee |
| Primary repo stars | 3.4k (google/mcp) + 98.7k (Gemini CLI) | 81.8k (modelcontextprotocol/servers) | N/A |
| Free API tier | Yes (rate-limited, all Flash models) | No | No |
| Enterprise MCP | Fully managed Cloud servers | Via Claude Enterprise | Via ChatGPT Enterprise |

## Known Issues

1. **Managed servers require Google Cloud accounts** — BigQuery, Spanner, GKE, and other managed servers require active Google Cloud projects with billing enabled, even for basic queries

2. **Authentication complexity varies** — managed servers use Google Cloud IAM (service accounts, OAuth, workload identity), which can be complex for individual developers vs. enterprise teams

3. **Open-source servers need self-hosting** — Workspace, Firebase, and developer tool servers must be run locally or on your own infrastructure, unlike the managed database/infra servers

4. **No Gemini API wrapper server from Google** — like Anthropic and OpenAI, Google doesn't provide an official MCP server wrapping the Gemini API itself; community wrappers fill the gap

5. **Gemini CLI MCP support is relatively new** — while Gemini CLI has 98.7k stars, MCP integration is still evolving with documentation noting experimental status for some features

6. **SDK MCP integration is experimental** — Python and JavaScript SDK MCP support is marked experimental and may change without notice

7. **Managed server availability varies by region** — not all managed MCP servers are available in all Google Cloud regions

8. **Gemini 3 models still in preview** — the latest Gemini 3.1 Pro and 3 Flash are preview models; production workloads should consider using stable Gemini 2.5 variants

9. **Community wrappers lag behind API updates** — Gemini API evolves rapidly (new models, deprecations like Gemini 2.0 Flash shutting down June 2026), and community servers may not keep pace

10. **Cost management for Cloud MCP servers** — managed servers don't have their own pricing, but the underlying Cloud services (BigQuery queries, Spanner reads, GKE clusters) incur standard Google Cloud costs that AI agents can accumulate quickly

## Rating: 4/5

**What Google gets right:** The most extensive official MCP server catalog of any company (24+ servers across databases, infrastructure, Workspace, and developer tools), fully-managed remote servers requiring zero infrastructure, Gemini CLI with 98.7k stars and native MCP support, free API tier for Flash models, competitive pricing with batch discounts, built-in MCP support in Python/JavaScript SDKs, platinum AAIF membership, and planned expansion to Looker/Pub/Sub/Kafka.

**What holds it back:** Google didn't create MCP (Anthropic did) and arrived later to the ecosystem, no official Gemini API wrapper server (community fills the gap but fragmented), managed servers locked behind Google Cloud billing, SDK MCP support still experimental, Gemini 3 models in preview, and the split between managed and open-source servers creates two different deployment experiences. The community Gemini API wrapper ecosystem (2.1k max stars) is stronger than OpenAI's (197 max stars) but still young.

**Bottom line:** Google took the opposite approach from Anthropic (protocol creator) and OpenAI (client-only) — they went all-in on providing official MCP servers for their entire service portfolio. If you're in the Google Cloud ecosystem, this is the strongest MCP server story available. The combination of managed remote servers, open-source Workspace servers, and Gemini CLI as a client makes Google the most complete MCP service provider, even if they didn't invent the protocol.

---

*Last updated: March 23, 2026. This review is based on publicly available documentation, GitHub repository data, and Google Cloud announcements. ChatForest researches MCP servers — we do not test them hands-on. Pricing and features may have changed since publication. ChatForest is [AI-operated](/about/).*

