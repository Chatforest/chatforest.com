# ChatForest Work Log

> Runs 1-28 archived in `WORKLOG-archive-runs-01-28.md`

## Run 50 — 2026-03-14 — Review (Tavily MCP Server)

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No pending messages.

### What I did

1. **Wrote "The Tavily MCP Server — Search, Extract, Crawl, and Map in One Package"** — `content/reviews/tavily-mcp-server.md`
   - **29th review**, tenth review beyond the original server list
   - Rating: **4/5** — best search-to-extract pipeline, held back by keyword-only search quality and credit expiration
   - 4 tools: search (1), extraction (1), crawling (1), site mapping (1)
   - Official server from Tavily (`tavily-ai/tavily-mcp`), 1,400 stars, JavaScript, MIT
   - Hosted remote MCP server at mcp.tavily.com — zero-install setup, just paste a URL
   - Default search API for LangChain, LlamaIndex, CrewAI, Vercel AI SDK
   - Search + extract + crawl + map pipeline in one server — capabilities that normally need 2-3 servers
   - OAuth 2.0 support with automatic client registration
   - Natural language `instructions` parameter for crawl/map tools
   - Honest about issues: keyword search (71% WebWalker vs Exa's 81%), credits don't roll over, cost stacking, HTTP config friction (#125, #121), API key in URL, Nebius acquisition uncertainty
   - Pricing: 1,000 free credits/mo, then $30-500/mo (credits expire monthly)
   - Compared with Brave (more search types), Exa (semantic search), Firecrawl (deeper scraping), Perplexity (answer engine)

2. **Updated mega-comparison** (`content/guides/best-mcp-servers.md`)
   - Added Tavily 4/5 review link to search section runner-up in summary table
   - Added "Search + extraction" sub-section with Tavily review link
   - Added Tavily to "Beyond the original list" section
   - Updated review count to 29, rating distribution (4/5 tier now has 13 servers)

3. **Updated search comparison** (`content/guides/best-search-mcp-servers.md`)
   - Added review rating (4/5) and review link to contenders table
   - Updated Tavily section header with review link and rating
   - Added Tavily review to intro paragraph (now lists all 3 reviewed search servers)
   - Added rating to decision flowchart

4. **Build succeeded** (40ms, 49 pages). **Deploy throttled** — need 60 min since last deploy (~27 min elapsed).

### Site status
- **Committed, deploy pending**
- 43 content pieces: 29 reviews + 4 guides + 11 comparisons
- Tavily is the 13th server rated 4/5 — the most crowded rating tier

### What should happen next
- **Run 51:** Deploy pending content. Could write Milvus, Crawl4AI, or BrowserMCP review.
- **Run 52+:** Execute promotion plan when accounts approved.
- **Future:** Favicon, newsletter setup, affiliate link integration, new review targets

## Run 49 — 2026-03-14 — Review (Browserbase MCP Server)

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No pending messages.

### What I did

1. **Wrote "The Browserbase MCP Server — Cloud Browser Automation With AI-Native Targeting"** — `content/reviews/browserbase-mcp-server.md`
   - **28th review**, ninth review beyond the original server list
   - Rating: **3.5/5** — innovative AI-native targeting via Stagehand, held back by critical bugs and thin tooling
   - 8 tools: navigation & interaction (3), data extraction (2), visual capture (1), session management (2)
   - Official server from Browserbase (`browserbase/mcp-server-browserbase`), 3,200 stars, TypeScript
   - Stagehand v3 natural language element targeting — agents describe actions in plain English instead of CSS selectors or accessibility tree refs
   - Cloud-only with anti-bot stealth mode, proxy support, session recording
   - stdio + Streamable HTTP transports, Docker support
   - Requires 3 API keys (Browserbase API key, project ID, Gemini/model API key)
   - Honest about issues: 20 open GitHub issues including blank screenshots (#125), Stagehand init failures (#56, #41), SHTTP failures (#149), session creation bugs (#121, #118)
   - Pricing: 1 free browser hour, then $20/mo Developer, $99/mo Startup, custom Scale
   - Compared with Playwright (free, 25+ tools, deterministic), Puppeteer (free, CSS selectors), Firecrawl (content extraction), BrowserMCP (existing browser)

2. **Updated mega-comparison** (`content/guides/best-mcp-servers.md`)
   - Added Browserbase 3.5/5 review link to browser automation runner-up in summary table
   - Added Browserbase to browser automation section with review link
   - Added Browserbase to "Beyond the original list" section
   - Updated review count to 28, rating distribution (3.5/5 tier now has 9 servers)

3. **Updated browser comparison** (`content/guides/best-browser-mcp-servers.md`)
   - Added review rating (3.5/5) and review link to contenders table
   - Updated Browserbase description with Stagehand v3, tool count, pricing details
   - Updated tool count from ~10 to 8 in feature comparison
   - Added review link to production workloads recommendation section
   - Added Browserbase review to bottom links

4. **Updated web scraping comparison** (`content/guides/best-web-scraping-mcp-servers.md`)
   - Added review rating (3.5/5) and review link to Browserbase section header
   - Updated description with Stagehand v3 tools and known bugs

5. **Build succeeded** (45ms, 48 pages). **Deployed to chatforest.com** — 48 pages live.

### Site status
- **Committed, deployed this run**
- 42 content pieces: 28 reviews + 4 guides + 11 comparisons
- Browserbase is the 9th server rated 3.5/5 — the second most crowded rating tier

### What should happen next
- **Run 50:** Could write Tavily, Milvus, Crawl4AI, or BrowserMCP review.
- **Run 51+:** Execute promotion plan when accounts approved.
- **Future:** Favicon, newsletter setup, affiliate link integration, new review targets

## Run 48 — 2026-03-14 — Deploy + Review (Firecrawl MCP Server)

**Mode:** Developer + Researcher + Copywriter

### Inbox update
- No pending messages.

### What I did

1. **Deployed all backlogged content** — Runs 44-47 (timestamps, Qdrant review, vector database comparison, Pinecone review, Todoist review) now live on chatforest.com. 47 pages deployed.

2. **Wrote "The Firecrawl MCP Server — The Full-Stack Web Scraping Platform for AI Agents"** — `content/reviews/firecrawl-mcp-server.md`
   - **27th review**, eighth review beyond the original server list
   - Rating: **4/5** — most comprehensive web scraping MCP server with unique autonomous research
   - 12+ tools across 4 categories: core scraping (5), search & extraction (2), research & agents (2), utility (1), plus optional browser automation (4)
   - Official server from Firecrawl/SideGuide Technologies, 5,800 stars, MIT license, TypeScript
   - Unique `firecrawl_agent` for autonomous multi-source research and `firecrawl_extract` for LLM-powered structured data extraction
   - Cloud + self-hosted, stdio + Streamable HTTP transports, hosted URL endpoint
   - Honest about issues: non-renewable 500-credit free tier, credit stacking (1 credit/page → 9 credits with extraction + enhanced), Extract endpoint billed separately, 49 open issues, agent tools in preview
   - Compared with Official Fetch, fetcher-mcp, Browserbase, Jina AI, community alternatives

3. **Updated mega-comparison** (`content/guides/best-mcp-servers.md`)
   - Added Firecrawl 4/5 review link to web scraping section and browser automation section
   - Added Firecrawl to "Beyond the original list" section
   - Updated review count to 27, rating distribution (4/5 cluster now has 12 servers)

4. **Updated web scraping comparison** (`content/guides/best-web-scraping-mcp-servers.md`)
   - Added review rating (4/5) and review link to Firecrawl section
   - Updated tool count from 7 to 12+, updated pricing to current rates ($16-599/mo)
   - Added LLM extraction and autonomous agent rows to feature comparison table
   - Updated recommendations section with review link
   - Added Firecrawl review link to bottom section

5. **Build succeeded** (38ms, 47 pages). **Deploy throttled** — just deployed this run.

### Site status
- **Committed, deployed earlier this run** (deploy throttle now active)
- 41 content pieces: 27 reviews + 4 guides + 11 comparisons
- Firecrawl is the 12th server rated 4/5 — the most crowded rating tier

### What should happen next
- **Run 49:** Could write Browserbase, Tavily, Milvus, or Crawl4AI review.
- **Run 50+:** Execute promotion plan when accounts approved.
- **Future:** Favicon, newsletter setup, affiliate link integration, new review targets

## Run 47 — 2026-03-14 — Review (Todoist MCP Server)

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No pending messages.

### What I did

1. **Wrote "The Todoist MCP Server — Full-Stack Task Management Through Your AI Assistant"** — `content/reviews/todoist-mcp-server.md`
   - **26th review**, seventh review beyond the original server list
   - Rating: **4/5** — most ambitious productivity MCP server with SDK-first architecture
   - 28+ tools across 7 categories: tasks (7), projects (5), sections (3), comments & collaboration (5), labels (2), information & search (4), data operations (3)
   - Official server from Doist (`Doist/todoist-ai`), 382 stars, MIT license, TypeScript
   - SDK-first architecture — tools reusable in Vercel AI SDK, custom pipelines, not just MCP
   - All three transports: Streamable HTTP, SSE, stdio — rare for any MCP server
   - MCP Apps: interactive UI widgets rendered inline in chat interfaces
   - Hosted endpoint at `ai.todoist.net/mcp` with OAuth — plus local stdio via npx
   - `get-overview` tool for dashboard-style snapshots, full CRUD including delete
   - Honest about issues: two p1 bugs (`add-sections` broken, `manage-assignments` silent failure), batch timeouts, incomplete project hierarchy, no reminders/attachments/reordering, self-described "early stages"
   - Compared with Linear (better tool design, more stable), Notion (knowledge + tasks), 6 community Todoist servers

2. **Updated mega-comparison** (`content/guides/best-mcp-servers.md`)
   - Added Todoist 4/5 review link to Productivity (tasks) runner-up in summary table
   - Updated Todoist section with rating, 28+ tools, SDK-first detail, and review link
   - Added Todoist to "Beyond the original list" section
   - Updated review count to 26, rating distribution (4/5 cluster now has 11 servers)

3. **Updated productivity comparison** (`content/guides/best-productivity-mcp-servers.md`)
   - Added Todoist review link to intro and contenders table (updated stars to 382, tools to 28+)
   - Rewrote Todoist detail section with review rating, full tool count, SDK-first architecture, transport flexibility, MCP Apps, known bugs, and review link
   - Updated recommended stack with review link and rating

4. **Build succeeded** (43ms, 46 pages). **Deploy throttled** — 22 minutes remaining per 1-deploy/hour rule.

### Site status
- **Committed, NOT deployed** (deploy throttle)
- 40 content pieces: 26 reviews + 4 guides + 11 comparisons (counting _index.md separately)
- Todoist is the 11th server rated 4/5 — the most crowded rating tier

### What should happen next
- **Run 48:** Deploy (throttle should be clear). Could write Firecrawl, Browserbase, Milvus, or Tavily review.
- **Run 49+:** Execute promotion plan when accounts approved.
- **Future:** Favicon, newsletter setup, affiliate link integration, new review targets

## Run 46 — 2026-03-14 — Review (Pinecone MCP Server)

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No pending messages.

### What I did

1. **Wrote "The Pinecone MCP Server — Cloud Vector Search With Built-In Reranking"** — `content/reviews/pinecone-mcp-server.md`
   - **25th review**, sixth review beyond the original server list
   - Rating: **3/5** — innovative search features held back by cloud-only limitations
   - 9 tools: index management (3), record operations (2), search quality (2), documentation (1), index creation (1)
   - Unique features no other vector DB MCP server has: `cascading-search` (cross-index search with deduplication), `rerank-documents` (built-in reranking models), `search-docs` (documentation search without auth)
   - Integrated embedding means zero embedding config — pass text, Pinecone handles the rest
   - Researched all three Pinecone MCP servers: Developer (this review), Assistant (42 stars, Rust, 1 tool), Claude Code Plugin
   - Honest about tradeoffs: cloud-only (no local mode), integrated embedding indexes only (existing custom-embedding indexes invisible), no delete/update/namespace management, stdio transport for a cloud-only service, lowest adoption among official servers (56 stars)
   - Comparison with community mcp-pinecone by sirmews (~150 stars) which works with any Pinecone index
   - Feature comparison table across 10 dimensions vs Chroma, Qdrant, Milvus

2. **Updated vector database comparison** (`content/guides/best-vector-database-mcp-servers.md`)
   - Moved Pinecone from "Unreviewed Servers" to reviewed section with rating and review link
   - Added review links in contenders table, recommendations, and decision flowchart
   - Updated intro to mention 3 reviewed servers

3. **Updated mega-comparison** (`content/guides/best-mcp-servers.md`)
   - Updated Pinecone entry in vector database section with rating, review link, and feature description
   - Added Pinecone to "Beyond the original list" section
   - Updated review count from 24 to 25
   - Updated rating distribution (3/5 cluster now has 3 servers: SQLite, Qdrant, Pinecone)

4. **Build succeeded** (45 pages). **Deploy throttled** — 30 minutes remaining per 1-deploy/hour rule.

### Site status
- **Committed, NOT deployed** (deploy throttle)
- 40 content pieces: 25 reviews + 4 guides + 11 comparisons
- Vector database category now has 3 reviewed servers: Chroma (3.5/5), Qdrant (3/5), Pinecone (3/5)

### What should happen next
- **Run 47:** Deploy (throttle should be clear). Could write Milvus MCP review, or a workflow guide.
- **Run 48+:** Execute promotion plan when accounts approved.
- **Future:** Favicon, newsletter setup, affiliate link integration, new review targets

## Run 45 — 2026-03-14 — Comparison (Best Vector Database MCP Servers)

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No pending messages.

### What I did

1. **Wrote "Best Vector Database MCP Servers in 2026"** — `content/guides/best-vector-database-mcp-servers.md`
   - **11th comparison article** — first dedicated vector database comparison
   - Head-to-head comparison of 7 servers: Chroma (3.5/5, reviewed), Qdrant (3/5, reviewed), Pinecone, Milvus, Zilliz Cloud, Weaviate, LanceDB
   - Researched all unreviewed servers: GitHub stars, tool counts, transport support, features, limitations
   - Two-philosophy framework: "database management" (Chroma 13 tools, Milvus 12 tools) vs "semantic memory" (Qdrant 2 tools)
   - Pinecone positioned between the two — 9 tools focused on search quality (cascading search, reranking)
   - Identified the pgvector gap — no dedicated pgvector MCP server exists
   - Feature comparison table across 17 dimensions
   - Decision flowchart by use case (memory, RAG, infrastructure management, remote transport, zero infrastructure)
   - Honest about category immaturity: no server has OAuth, none at 1.0, best is only 3.5/5

2. **Updated mega-comparison** (`content/guides/best-mcp-servers.md`)
   - Added "Full comparison" link in vector databases section
   - Updated comparison count from 10 to 11

3. **Updated database comparison** (`content/guides/best-database-mcp-servers.md`)
   - Added cross-link to vector database comparison in the decision flowchart

4. **Build succeeded** (36ms, 44 pages). **Deploy throttled** — 39 minutes remaining per 1-deploy/hour rule.

### Site status
- **Committed, NOT deployed** (deploy throttle)
- 39 content pieces: 24 reviews + 4 guides + 11 comparisons
- All major MCP server categories now have dedicated comparison articles

### What should happen next
- **Run 46:** Deploy (throttle should be clear). Could write Pinecone MCP or Milvus MCP review, or a workflow guide.
- **Run 47+:** Execute promotion plan when accounts approved.
- **Future:** Favicon, newsletter setup, affiliate link integration, new review targets

## Run 44 — 2026-03-14 — Timestamps in Content (Rob's Editorial Request)

**Mode:** Developer

### Inbox update
- **#105 (normal, Rob):** Editorial suggestion — show timestamps down to the second instead of just dates. Since all articles were published on the same day, timestamps highlight autonomous agent production in real-time bursts. Fits transparent AI authorship brand. Implemented.

### What I did

1. **Updated all 38 content files** with precise timestamps from git commit history
   - Front matter `date:` changed from `2026-03-14` to full ISO 8601 with timezone (e.g., `2026-03-14T09:42:34+09:00`)
   - Timestamps reflect when each piece was actually committed — showing the real production timeline

2. **Updated 5 layout templates** to display full timestamps
   - `layouts/reviews/single.html` — review pages now show `2026-03-14 09:42:34` format
   - `layouts/guides/single.html` — guide pages match
   - `layouts/partials/article-card.html` — listing cards show timestamps
   - `layouts/partials/schema-review.html` — Schema.org `datePublished` now ISO 8601 with time+timezone
   - `layouts/partials/schema-article.html` — same for article schema

3. **Build succeeded** (37ms, 43 pages). **Deploy throttled** — only 8 minutes since last deploy, need 51 more minutes per Rob's 1-deploy/hour rule.

### Site status
- **Committed, NOT deployed** (deploy throttle — will deploy next eligible run)
- 38 content pieces: 24 reviews + 4 guides + 10 comparisons
- All pages now show precise timestamps highlighting autonomous agent workflow

### What should happen next
- **Run 45:** Deploy (throttle should be clear). Could write Pinecone MCP, Milvus MCP, or "Best Vector Database MCP Servers in 2026" comparison.
- **Run 46+:** Execute promotion plan when accounts approved.
- **Future:** Favicon, newsletter setup, affiliate link integration, new review targets

## Run 43 — 2026-03-14 — Review (Qdrant MCP Server) + Deploy Throttle

**Mode:** Operations + Researcher + Copywriter + Developer

### Inbox update
- **#104 (high, Rob):** New deploy rule — deploy at most once per hour using `.last_deploy` file. Implemented.
- **#103 (from me):** SSH restored message from Run 42. Marked seen.

### What I did

1. **Implemented deploy throttle** per Rob's message #104
   - Created `.gitignore` with `.last_deploy`, `.grove_lock`, `resources/_gen/`, `site/`
   - Deploy now checks `.last_deploy` age before attempting rsync
   - After successful deploy, touches `.last_deploy`
   - On failure, does NOT touch `.last_deploy` (per Rob's spec)

2. **Wrote "The Qdrant MCP Server — Semantic Memory Through Your AI Assistant"** — `content/reviews/qdrant-mcp-server.md`
   - **24th review**, fifth review beyond the original server list
   - Rating: **3/5** — most adopted vector DB MCP server (1,300 stars), but too minimal
   - Only 2 tools: `qdrant-store` and `qdrant-find` — no delete, no update, no collection management
   - Only vector DB MCP server supporting all three transports: stdio, SSE, Streamable HTTP
   - Extensible `QdrantMCPServer` class architecture (v0.8.0) — a "server as framework" approach
   - Local embedded mode via `QDRANT_LOCAL_PATH` — zero infrastructure semantic memory
   - Customizable tool descriptions via environment variables
   - Honest about tradeoffs: 2 tools vs Chroma's 13, no delete capability (open issues #74/#101), FastEmbed-only default, no OAuth for MCP transport, 22 open issues with basic feature requests
   - Comparison table with Chroma (13 tools), Pinecone (9 tools), Milvus (11 tools), Weaviate (2 tools)

3. **Updated mega-comparison** (`content/guides/best-mcp-servers.md`)
   - Added Qdrant 3/5 link to vector database runner-up in summary table
   - Added review link and detail to vector database section
   - Added Qdrant to "Beyond the original list" section
   - Updated review count to 24, rating distribution (3/5 cluster now has 2 servers: SQLite, Qdrant)

4. **Updated database comparison** (`content/guides/best-database-mcp-servers.md`)
   - Added Qdrant MCP as alternative for vector search / RAG use cases

5. **Build succeeded** (41ms, 43 pages). **Deployed successfully** to chatforest.com.

### Site status
- **Committed AND deployed**
- 38 content pieces: 24 reviews + 4 guides + 10 comparisons
- Deploy throttle now active (max 1 deploy/hour per Rob's directive)

### What should happen next
- **Run 44:** Could write Pinecone MCP, Milvus MCP, or "Best Vector Database MCP Servers in 2026" comparison. Or a workflow guide.
- **Run 45+:** Execute promotion plan when accounts approved.
- **Future:** Favicon, newsletter setup, affiliate link integration, new review targets

## Run 42 — 2026-03-14 — Deploy + Review (Chroma MCP Server)

**Mode:** Operations + Researcher + Copywriter + Developer

### Inbox update
- **#102 (high, Rob):** DreamHost outage may be resolved — asked for ONE SSH test. SSH succeeded! Deployed all backlogged content. Replied as message #103.

### What I did

1. **SSH restored and all content deployed** — 11 runs of backlogged content (runs 31-41) now live on chatforest.com
   - SSH was returning "Too many authentication failures" because I used `grove@chatforest.com` instead of the `chat` alias (which uses user `backforest` with the correct key)
   - 42 pages deployed: 23 reviews + 4 guides + 10 comparisons + about + homepage + listings

2. **Wrote "The Chroma MCP Server — Vector Database Operations Through Your AI Assistant"** — `content/reviews/chroma-mcp-server.md`
   - **23rd review**, fourth review beyond the original server list
   - Rating: **3.5/5** — most comprehensive vector DB MCP server, but stdio-only and stalling development
   - 13 tools: 8 collection management + 5 document operations
   - Four deployment modes: ephemeral (in-memory), persistent (local files), HTTP (self-hosted), Cloud
   - Six embedding providers: Default, Cohere, OpenAI, Jina, VoyageAI, Roboflow
   - Unique feature: `chroma_fork_collection` — duplicate collections for experimentation
   - Search: semantic + full-text + regex through single `query_documents` tool
   - HNSW parameter configuration at collection creation
   - Honest about tradeoffs: stdio-only transport (no remote MCP), Python-only, beta with no releases in 7 months, context-bloating query results, known bugs (non-ASCII corruption, embedding dimension mismatches)
   - Comparison with Qdrant (1,300 stars, 2 tools, better transport), Pinecone (9 tools, cloud-only), Weaviate (2 tools, minimal)

3. **Updated mega-comparison** (`content/guides/best-mcp-servers.md`)
   - Added "Vector database" row with Chroma 3.5/5 as pick, Qdrant as runner-up
   - Added full vector database section between databases and memory
   - Added Chroma to "Beyond the original list" section
   - Updated review count to 23, rating distribution (3.5/5 cluster now has 8 servers)

4. **Updated database comparison** (`content/guides/best-database-mcp-servers.md`)
   - Added Chroma to decision flowchart for vector search / RAG use cases

5. **Build succeeded** (40ms, 42 pages). **Deployed successfully** to chatforest.com.

### Site status
- **Committed AND deployed** — first successful deploy since Run 29
- 37 content pieces: 23 reviews + 4 guides + 10 comparisons
- All backlogged content now live

### What should happen next
- **Run 43:** Could write Pinecone MCP, Qdrant MCP, or a workflow guide ("MCP Servers for CI/CD Pipelines"). Or a new comparison: "Best Vector Database MCP Servers in 2026".
- **Run 44+:** Execute promotion plan when accounts approved.
- **Future:** Favicon, newsletter setup, affiliate link integration, new review targets

## Run 41 — 2026-03-14 — Review (Linear MCP Server)

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No pending messages. No SSH clearance from Rob yet. 11 runs of content waiting to deploy.

### What I did

1. **Wrote "The Linear MCP Server — Issue Tracking and Project Management Through Your AI Assistant"** — `content/reviews/linear-mcp-server.md`
   - **22nd review**, third review beyond the original server list
   - Rating: **4/5** — best-in-class tool design, but high context cost and remote-only deployment
   - 23+ tools across issues, projects, initiatives, milestones, teams, labels, and documentation
   - Hosted remote-first at `mcp.linear.app/mcp` with OAuth 2.1 and Streamable HTTP transport
   - Standout: flat parameter schemas (flattened from GraphQL), embedded enum values, "me" shortcut for assignee — reduces agent errors significantly
   - February 2026 expansion added initiatives, milestones, project updates — moved from engineering tracker to full PM platform
   - Broad client support: Claude, Cursor, VS Code, Windsurf, Zed, Codex, Jules, v0
   - Honest about tradeoffs: 17.3k token context cost, verbose responses with unnecessary fields, no delete/archive, remote-only, requires paid Linear ($8/user/month), connection reliability issues
   - Comparison with Asana, Atlassian/Jira, Todoist — Linear wins on tool design quality

2. **Updated mega-comparison** (`content/guides/best-mcp-servers.md`)
   - Added Linear 4/5 link to Productivity (tasks) row in summary table
   - Updated Linear section with review link and 23+ tool count
   - Added Linear to "Beyond the original list" section
   - Updated review count to 22, rating distribution (4/5 cluster now has 10 servers)

3. **Updated productivity comparison** (`content/guides/best-productivity-mcp-servers.md`)
   - Added Linear review link to intro and contenders table
   - Updated Linear detail section with review rating, tool count, and design highlights

4. **Build succeeded** (38ms, 41 pages). **Deploy blocked** — complying with Rob's directive to stop all SSH attempts.

### Site status
- **Committed, NOT deployed** (per Rob's directive — no SSH until cleared)
- 36 content pieces: 22 reviews + 4 guides + 10 comparisons
- 11 runs of content waiting to deploy

### What should happen next
- **Run 42:** Check inbox for Rob's SSH clearance. Could write Chroma MCP, Pinecone MCP, or a workflow guide ("MCP Servers for CI/CD Pipelines").
- **Run 43+:** Deploy when Rob clears SSH. Execute promotion plan when accounts approved.
- **Future:** Favicon, newsletter setup, affiliate link integration, new review targets

## Run 40 — 2026-03-14 — Review (Stripe MCP Server)

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No pending messages. No SSH clearance from Rob yet. 9 runs of content waiting to deploy.

### What I did

1. **Wrote "The Stripe MCP Server — Payment Operations Through Your AI Assistant"** — `content/reviews/stripe-mcp-server.md`
   - **21st review**, second review beyond the original server list
   - Rating: **4/5** — best-in-class security model, unique documentation search feature
   - 25 tools across 13 resource categories: customers, products, prices, invoices, subscriptions, refunds, payment links, disputes, balance, coupons, search, and documentation
   - Part of broader Stripe Agent Toolkit (1,400 GitHub stars) with framework integrations for OpenAI, LangChain, CrewAI, Vercel AI SDK
   - Three-layer security: OAuth remote server at mcp.stripe.com, restricted API keys with per-resource permissions for local, dashboard session management
   - Killer feature: `search_stripe_documentation` — agent can query Stripe's knowledge base directly
   - Honest about tradeoffs: covers only 10-15% of Stripe's API surface, most resources only support create+list (no updates), no webhooks, no Checkout Sessions, no Connect, protocol version compatibility issue (#290), TypeScript-only local deployment

2. **Updated mega-comparison** (`content/guides/best-mcp-servers.md`)
   - Added "Payments" row with Stripe 4/5 as pick
   - Added full Payments section describing the server and its Agent Toolkit context
   - Updated "Beyond the original list" to mention Stripe alongside Cloudflare
   - Updated review count to 21, rating distribution (4/5 cluster now has 9 servers)

3. **Build succeeded** (37ms, 40 pages). **Deploy blocked** — complying with Rob's directive to stop all SSH attempts.

### Site status
- **Committed, NOT deployed** (per Rob's directive — no SSH until cleared)
- 35 content pieces: 21 reviews + 4 guides + 10 comparisons
- 10 runs of content waiting to deploy

### What should happen next
- **Run 41:** Check inbox for Rob's SSH clearance. Could write Linear MCP, Chroma MCP, or a workflow guide ("MCP Servers for CI/CD Pipelines").
- **Run 42+:** Deploy when Rob clears SSH. Execute promotion plan when accounts approved.
- **Future:** Favicon, newsletter setup, affiliate link integration, new review targets

## Run 39 — 2026-03-14 — Review (Cloudflare MCP Server — First Beyond Original List)

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- Only pending message was my own reply (#101). No new messages from Rob. No SSH clearance yet.
- Marked #101 as seen.

### What I did

1. **Wrote "The Cloudflare MCP Server — 2,500 API Endpoints in 1,000 Tokens"** — `content/reviews/cloudflare-mcp-server.md`
   - **20th review**, first review beyond our original server list
   - Rating: **4.5/5** — ties with Playwright for our highest rating
   - The most innovative MCP architecture we've reviewed: Code Mode collapses 2,500+ API endpoints into just 2 tools (~1,000 tokens vs 1.17 million for traditional approach)
   - `search()` queries a typed OpenAPI spec; `execute()` runs generated JavaScript in a V8 Dynamic Worker sandbox
   - Plus 16 specialized product servers (Workers Builds, Observability, Browser Rendering, DNS Analytics, AI Gateway, etc.)
   - All remote-first with OAuth, Streamable HTTP transport
   - Also a platform for building MCP servers (Workers + mcp-handler + Agents SDK)
   - Honest about tradeoffs: depends on agent JavaScript competency, fragmented repo structure (3 repos), low Code Mode adoption (262 stars), Cloudflare-only lock-in

2. **Updated mega-comparison** (`content/guides/best-mcp-servers.md`)
   - Added "Cloud infrastructure" row with Cloudflare 4.5/5 as pick
   - Added Cloudflare section to DevOps & infrastructure description
   - Updated "All servers reviewed" to "Beyond the original list"
   - Updated review count to 20, rating distribution (4.5/5 cluster now has 2 servers: Playwright, Cloudflare)

3. **Updated DevOps comparison** (`content/guides/best-devops-mcp-servers.md`)
   - Added Cloudflare as first entry in contenders table
   - Updated intro to mention Cloudflare review

4. **Build succeeded** (37ms, 39 pages). **Deploy blocked** — complying with Rob's directive to stop all SSH attempts.

### Site status
- **Committed, NOT deployed** (per Rob's directive — no SSH until cleared)
- 34 content pieces: 20 reviews + 4 guides + 10 comparisons
- Now expanding beyond original server list
- 9 runs of content waiting to deploy

### What should happen next
- **Run 40:** Check inbox for Rob's SSH clearance. Could write Stripe MCP, Chroma MCP, or Linear MCP review — or a workflow guide ("MCP Servers for CI/CD Pipelines").
- **Run 41+:** Deploy when Rob clears SSH. Execute promotion plan when accounts approved.
- **Future:** Favicon, newsletter setup, affiliate link integration, new review targets

## Run 38 — 2026-03-14 — Guide (How to Set Up Your MCP Server Stack)

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- **#100 (high, Rob):** DreamHost SSH is datacenter outage (pdx1/iad1), not throttling. Still DO NOT retry. Three questions answered:
  1. We use SSH key auth (ed25519), not password — should reconnect fine once outage resolves
  2. Reddit account ready (username: ChatForest). Drafted display name and bio for Rob to set up. Posts go through Rob's review.
  3. Agreed duck.com → grove@chatforest.com forwarding makes sense once email is set up
- Replied as message #101. Marked #100 as seen.

### What I did

1. **Wrote "How to Set Up Your MCP Server Stack: A Practical Guide for 2026"** — `content/guides/mcp-server-setup-guide.md`
   - **4th guide** — first user-focused setup/configuration guide (vs. build tutorial or security)
   - Covers all four major MCP clients: Claude Desktop, VS Code (Copilot), Cursor, Claude Code
   - Configuration file locations, JSON examples for local (stdio) and remote (Streamable HTTP) servers
   - Explains transport protocol evolution: stdio vs SSE (deprecated) vs Streamable HTTP
   - Four role-specific starter stacks: web developer, backend/data engineer, technical writer, full-stack team
   - Managing multiple servers: performance, context window pressure, security, updates
   - Troubleshooting section covering common issues (server won't start, OAuth failures, silent tool failures, too many tools)
   - Cross-links to all 19 reviews and other guides

2. **Updated mega-comparison** (`content/guides/best-mcp-servers.md`)
   - Added setup guide reference in the "starter stack" section

3. **Updated build tutorial** (`content/guides/build-your-first-mcp-server.md`)
   - Added cross-link to setup guide at the end

4. **Build succeeded** (36ms, 38 pages). **Deploy blocked** — complying with Rob's directive to stop all SSH attempts.

### Site status
- **Committed, NOT deployed** (per Rob's directive — no SSH until cleared)
- 33 content pieces: 19 reviews + 4 guides + 10 comparisons
- 8 runs of content waiting to deploy
- Guide library now covers: What is MCP → Build a Server → Set Up Your Stack → Security

### What should happen next
- **Run 39:** Check inbox for Rob's SSH clearance. Could write a new server review (Cloudflare Workers MCP, Stripe MCP, or Chroma MCP are good targets) or a workflow guide ("MCP Servers for CI/CD Pipelines").
- **Run 40+:** Deploy when Rob clears SSH. Execute promotion plan when accounts approved. Reddit bio is drafted and ready.
- **Future:** Favicon, newsletter setup, affiliate link integration, new review targets

## Run 37 — 2026-03-14 — Guide (MCP Server Security: A Practical Guide for 2026)

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No pending messages. No SSH clearance from Rob yet. Complying with deploy ban.

### What I did

1. **Wrote "MCP Server Security: A Practical Guide for 2026"** — `content/guides/mcp-server-security.md`
   - **3rd guide** (after "What is MCP" and "Build Your First MCP Server") — first security-focused content
   - Researched OWASP MCP Top 10, OWASP cheatsheets for using/building MCP servers, OAuth 2.1 spec evolution (March → June → November 2025 revisions)
   - Analyzed security posture of all 19 reviewed servers, organized by strength (Strong → Adequate → Weak → Dangerous)
   - Three real vulnerabilities documented with code examples:
     - SQL injection in PostgreSQL MCP (multi-statement bypass of read-only transaction)
     - SSRF in Fetch MCP (unpatched, can reach AWS metadata/localhost)
     - ContextCrush prompt injection in Context7 (patched Feb 2026)
   - Authentication transition section: local API keys → remote OAuth 2.1 Resource Servers
   - Practical security checklist (20 items across 5 categories: auth, data protection, input validation, operational security, supply chain)
   - Best practices section: prefer OAuth, scope down, isolate by context, use read-only modes, audit regularly
   - Cross-links to all 19 reviews and OWASP resources

2. **Updated mega-comparison** (`content/guides/best-mcp-servers.md`)
   - Added security guide reference in the "starter stack" section

3. **Build succeeded** (31ms, 37 pages). **Deploy blocked** — complying with Rob's directive to stop all SSH attempts.

### Site status
- **Committed, NOT deployed** (per Rob's directive — no SSH until cleared)
- 32 content pieces: 19 reviews + 3 guides + 10 comparisons
- 7 runs of content waiting to deploy
- Content now includes security-focused material — high-value for SEO (OWASP references, vulnerability documentation)

### What should happen next
- **Run 38:** Check inbox for Rob's SSH clearance. Could write another new server review (Cloudflare Workers MCP, Stripe MCP, or Chroma MCP are trending) or a workflow guide ("Setting Up Your First MCP Server Stack").
- **Run 39+:** Deploy when Rob clears SSH. Execute promotion plan when accounts approved.
- **Future:** Favicon, newsletter setup, affiliate link integration, new review targets

## Run 36 — 2026-03-14 — Content (Best DevOps & Infrastructure MCP Servers Comparison)

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No pending messages. No SSH clearance from Rob yet. Complying with deploy ban.

### What I did

1. **Wrote "Best DevOps & Infrastructure MCP Servers in 2026"** — `content/guides/best-devops-mcp-servers.md`
   - **10th comparison article** — first new category beyond the original server list
   - Head-to-head comparison of 5 DevOps platforms: Docker MCP (Toolkit + Catalog), Kubernetes MCP (Red Hat/community), Terraform MCP (HashiCorp), AWS MCP (60+ servers), Azure DevOps MCP (Microsoft, GA)
   - Three-layer framework: container/orchestration (Docker, K8s), infrastructure as code (Terraform, AWS), DevOps platform (Azure DevOps, GitHub)
   - Feature comparison table, decision flowchart, recommended two-layer stack
   - Safety section on production infrastructure risks — read-only modes, credential scoping, staging-first approach
   - Cross-links to our GitHub MCP review (4.5/5) for CI/CD
   - Researched current state: Docker's 300+ verified catalog, K8s fragmentation (6+ implementations), Terraform Stacks support, AWS 60+ specialized servers, Azure DevOps GA + VS 2026 integration

2. **Updated mega-comparison** (`content/guides/best-mcp-servers.md`)
   - Added full DevOps & infrastructure category section
   - Added 3 DevOps rows to summary table (IaC, containers, platform)
   - Updated comparison count from 9 to 10
   - Updated descriptions to reflect 10 categories

3. **Updated observability comparison** cross-links to include DevOps category

4. **Build succeeded** (34ms). **Deploy blocked** — complying with Rob's directive to stop all SSH attempts.

### Site status
- **Committed, NOT deployed** (per Rob's directive — no SSH until cleared)
- 31 content pieces: 19 reviews + 2 guides + 10 comparisons
- Now covering categories beyond the original server list
- 6 runs of content waiting to deploy

### What should happen next
- **Run 37:** Check inbox for Rob's SSH clearance. Write more content — could do a deeper tutorial/workflow guide, or review a specific DevOps server (Docker, Terraform, or Kubernetes).
- **Run 38+:** Deploy when Rob clears SSH. Execute promotion plan when accounts approved.
- **Future:** Favicon, newsletter setup, affiliate link integration, new review targets (DevOps servers)

## Run 29 — 2026-03-14 — Traffic & Promotion Strategy + Schema.org SEO

**Mode:** Researcher + Strategist + Developer

### Inbox update
- **High-priority message from Rob + Boss Claude** (message #88): Asked for a traffic/promotion plan — where to post content, social media strategy, open-source Reddit alternatives, what's needed to execute.
- Replied with full plan summary (message #89).

### What I did

1. **Researched traffic/promotion strategies** — web searches on:
   - Developer content promotion tactics for 2026
   - MCP community platforms and developer channels
   - Open-source Reddit alternatives (Lemmy, Kbin, Tildes)
   - SEO timeline expectations for new technical sites
   - Hacker News submission best practices
   - Dev.to/Hashnode cross-posting strategies

2. **Wrote comprehensive traffic & promotion plan** — `strategy/02-traffic-promotion-plan.md`
   - **Three channels:** Community posting (immediate), SEO optimization (medium-term), newsletter (long-term)
   - **Community targets:** Reddit (r/mcp, r/ClaudeAI, r/LocalLLaMA), Hacker News, Dev.to, Hashnode, Lemmy/Fediverse
   - **Posting approach:** Genuine technical contributions, not link-dropping. Lead with insights, link to reviews in context.
   - **SEO needs:** Google Search Console, Schema.org structured data, backlink building
   - **What I need from Rob:** Reddit account (Tier 3), Google Search Console verification, Dev.to account, OK on transparent AI identity
   - **Execution priority table** with 8 ranked actions
   - **Key principle:** Transparent about being AI-operated on all platforms

3. **Added Schema.org structured data to all pages** — developer work, no accounts needed
   - Reviews get `Review` + `SoftwareApplication` schema (helps rich results in search)
   - Guides/comparisons get `Article` schema
   - Homepage gets `WebSite` schema
   - Created reusable Hugo partials: `schema-review.html`, `schema-article.html`
   - Used Hugo's `dict` + `jsonify` + `safeJS` pipeline for clean JSON-LD output
   - All 25 content pages + homepage now have structured data

4. **Deployed to chatforest.com** — all pages updated with Schema.org markup

### What should happen next
- **Run 30:** While waiting for Rob's reply on the promotion plan, write another review or comparison.
- **Run 31+:** Execute promotion plan once Rob approves accounts, update mega-comparison with Notion
- **Future:** Favicon, newsletter setup, affiliate links

## Run 30 — 2026-03-14 — Content (Best Productivity & Knowledge Management MCP Servers Comparison)

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- Pending message #89 (from me, re: traffic/promotion plan) still unanswered. No new messages from Rob.

### What I did

1. **Wrote "Best Productivity & Knowledge Management MCP Servers in 2026"** — `content/guides/best-productivity-mcp-servers.md`
   - **8th comparison article** — completes coverage of all major MCP server categories (browser, database, web scraping, memory, search, documentation, productivity, plus mega-comparison)
   - Head-to-head comparison of 8 servers: Notion (3.5/5), Linear, Todoist, Asana, Google Calendar, Obsidian, Slack (4/5), Google Workspace
   - Researched current state of each: Linear's Feb 2026 PM tools expansion, Todoist's MCP Apps feature, Asana V2 migration, Google Calendar community server, Obsidian's fragmented ecosystem
   - Identified three architectural patterns: first-party hosted (Notion/Linear/Todoist/Asana/Slack), community local (Google Calendar/Google Workspace), local knowledge (Obsidian)
   - Feature comparison table, decision flowchart by use case, recommended stack
   - Key insight: Google has no official MCP server for any product — the biggest gap in the productivity MCP space
   - Cross-links to our Notion and Slack reviews

2. **Updated mega-comparison** (`content/guides/best-mcp-servers.md`)
   - Added "Productivity & knowledge management" section with all server recommendations
   - Added productivity rows to summary table (Notion 3.5/5 for knowledge, Linear for tasks)
   - Updated Notion from "not yet reviewed" to reviewed with full section
   - Removed Notion and Linear from "servers we haven't reviewed" section
   - Updated review count to 15, comparison count to 8
   - Added Notion to rating distribution table (3.5/5 cluster now has 5 servers)

3. **Deploy failed** — SSH to chatforest.com returned "Network is unreachable." Likely a network issue on the build server or DreamHost side. Content is committed and ready to deploy next run.

### Site status
- **Committed, NOT deployed** (network issue)
- 25 content pieces: 15 reviews + 2 guides + 8 comparisons
- Content types: reviews, tutorials, explainers, comparisons, mega-comparison
- Comparison articles now cover ALL major categories: browser automation, databases, web scraping, memory/knowledge, search, documentation, productivity/knowledge management, plus mega-comparison
- SEO infrastructure up to date

### What should happen next
- **Run 31:** Deploy (retry rsync). Handle inbox messages. Write another review.
- **Run 32+:** Favicon (waiting for Rob), execute promotion plan when Rob replies
- **Future:** Newsletter setup, affiliate link integration

## Run 31 — 2026-03-14 — Operations + Content (Observability MCP Servers Comparison)

**Mode:** Operations + Researcher + Copywriter + Developer

### Inbox update
- 6 pending messages processed:
  - **#91 (high, Boss Claude):** Backup files + log rotation question — replied with file sizes and rotation plan
  - **#92 (high, Rob):** Reddit username — superseded by #94
  - **#94 (normal, Rob + Boss Claude):** Reddit username — replied suggesting `chatforest_grove`, confirmed `~/.config/chatforest/` for credentials
  - **#93 (normal, Rob):** Confirmed transparent AI authorship everywhere — acknowledged
  - **#90 (normal, Boss Claude):** Email address — replied suggesting `grove@chatforest.com` + `hello@chatforest.com`
  - **#89 (high, from me):** My own traffic/promotion plan reply — marked seen
- All 6 messages marked as seen, 3 replies sent (#95, #96, #97)

### What I did

1. **Rotated WORKLOG.md** — archived runs 1-28 to `WORKLOG-archive-runs-01-28.md`. Active file went from 88K/1225 lines to ~4K/85 lines. Will rotate again at ~50K.

2. **Wrote "Best Observability MCP Servers in 2026"** — `content/guides/best-observability-mcp-servers.md`
   - **9th comparison article** — completes our category coverage
   - Head-to-head comparison of 6 servers: Sentry (4/5, reviewed), Datadog, Grafana, New Relic, Honeycomb, PagerDuty
   - Three observability layers framework: error tracking (Sentry/Honeycomb), full-stack APM (Datadog/New Relic/Grafana), incident management (PagerDuty)
   - Feature comparison table, decision flowchart, recommended two-server stack
   - Key insight: observability is the most "first-party" MCP category — every major platform has an official server
   - Researched current state of each: Datadog GA with 50+ tools, Grafana 1,200+ stars (most popular), New Relic Public Preview with NRQL translation, Honeycomb March 2026 Agent Skills expansion

3. **Updated mega-comparison** (`content/guides/best-mcp-servers.md`)
   - Expanded observability section from 2 paragraphs to full category with all 6 servers
   - Removed Datadog from "servers we haven't reviewed" section
   - Updated comparison count from 8 to 9

4. **Deploy failed** — SSH to chatforest.com still returns "Network is unreachable." Same issue as Run 30. Content committed, ready to deploy when network recovers.

### Site status
- **Committed, NOT deployed** (network issue — two consecutive runs)
- 26 content pieces: 15 reviews + 2 guides + 9 comparisons
- Comparison articles: browser automation, databases, web scraping, memory/knowledge, search, documentation, productivity, observability, plus mega-comparison
- All major MCP server categories covered

### What should happen next
- **Run 32:** Deploy (retry rsync — network issue has persisted 2 runs). Write another review — Neon MCP server or Figma Dev Mode MCP are good candidates.
- **Run 33+:** Execute promotion plan when Rob replies on accounts, favicon
- **Future:** Newsletter setup, affiliate link integration

## Run 32 — 2026-03-14 — Content (Neon MCP Server Review) + Deploy Diagnosis

**Mode:** Researcher + Copywriter + Developer + Operations

### Inbox update
- 3 pending messages — all from me (replies #95, #96, #97 from Run 31). No new messages from Rob or Boss Claude.
- Sent message #98 (high priority) to Rob: SSH deploy failing for 3 consecutive runs. IPv4 returns "Connection refused" on port 22, IPv6 "Network is unreachable". HTTP and ping work fine. Asked Rob to check DreamHost panel shell access settings.

### What I did

1. **Diagnosed SSH deploy failure** — network is back (HTTP 200, ping works), but SSH port 22 is explicitly refused. This is a DreamHost-side config change, not a network outage. Notified Rob with detailed diagnosis and specific ask (check DreamHost panel → Manage Users → Shell Access).

2. **Wrote "The Neon MCP Server — Serverless Postgres Management Through Natural Language"** — `content/reviews/neon-mcp-server.md`
   - **16th review**, first cloud-native database MCP server
   - Rating: **4/5** — the most capable database MCP server we've reviewed
   - 20 tools covering project management, branch-based migrations, SQL execution, query tuning, auth, and docs
   - Killer feature: branch-based migration workflow using Neon's copy-on-write storage (prepare → verify → merge/discard)
   - OAuth remote server at mcp.neon.tech (npm package deprecated)
   - Honest about tradeoffs: Neon-only lock-in, development-only limitation, OAuth requires browser (no headless support)
   - Neon built formal eval framework and improved tool selection from 60% to 100%
   - Free tier: 100 projects, 100 CU-hrs/mo, 0.5GB storage per branch

3. **Updated mega-comparison** (`content/guides/best-mcp-servers.md`)
   - Added "Database (cloud Postgres)" row with Neon 4/5 as pick
   - Added Neon section to database category description
   - Removed Neon from "servers we haven't reviewed"
   - Updated review count to 16, rating distribution (4/5 cluster now has 7 servers)

4. **Updated database comparison** (`content/guides/best-database-mcp-servers.md`)
   - Added Neon as first entry in contenders table
   - Added full "For Cloud Postgres: Neon MCP" section in replacements
   - Updated decision flowchart with Neon for cloud Postgres
   - Updated bottom line recommendation

5. **Build succeeded** (34ms). **Deploy blocked** — SSH still refused. Content committed, 4 runs of content waiting to deploy.

### Site status
- **Committed, NOT deployed** (SSH issue — 3 consecutive runs)
- 27 content pieces: 16 reviews + 2 guides + 9 comparisons
- Rating range: 2.5–4.5 across 16 reviews (4/5 is most common with 7 servers)

### What should happen next
- **Run 33:** Check inbox for Rob's reply on SSH issue. If SSH fixed, deploy immediately. Write another review (Figma Dev Mode MCP or Supabase).
- **Run 34+:** Execute promotion plan when Rob replies on accounts
- **Future:** Favicon, newsletter setup, affiliate link integration

## Run 33 — 2026-03-14 — Content (Supabase MCP Server Review)

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- **#99 (high, Rob):** URGENT — stop all SSH/rsync deploy attempts. DreamHost likely throttled us. Do NOT deploy until Rob clears it. Acknowledged and complying.
- Messages #95-98 (from me, previous runs) still pending replies. All marked as seen.

### What I did

1. **Wrote "The Supabase MCP Server — Full Backend Management Through Your AI Assistant"** — `content/reviews/supabase-mcp-server.md`
   - **17th review**, first BaaS (Backend-as-a-Service) MCP server
   - Rating: **4/5** — unmatched breadth, covering database, edge functions, storage, debugging, and more
   - 8 tool groups: account, docs, database, debugging, development, functions, storage, branching
   - Key differentiator vs Neon: Supabase goes wide (full backend), Neon goes deep (database)
   - Best security model we've reviewed: real read-only PostgreSQL role, project scoping, feature group filtering
   - OAuth 2.1 authentication at mcp.supabase.com (no PAT needed)
   - 2.5k GitHub stars (most popular database MCP server)
   - Honest about tradeoffs: schema-only branching (no data copy like Neon), paid plan required for branching, pre-1.0 stability, BaaS lock-in deeper than database lock-in

2. **Updated mega-comparison** (`content/guides/best-mcp-servers.md`)
   - Added "Backend-as-a-Service" row with Supabase 4/5
   - Updated Supabase from "not yet reviewed" to reviewed with link
   - Removed Supabase from "servers we haven't reviewed" section
   - Updated review count to 17, rating distribution (4/5 cluster now has 8 servers)
   - Updated database section with Supabase alongside Neon

3. **Updated database comparison** (`content/guides/best-database-mcp-servers.md`)
   - Added Supabase as first entry in contenders table
   - Added full "For Supabase Users: Supabase MCP" section in replacements
   - Updated decision flowchart with Supabase for full backend management
   - Updated bottom line recommendation

4. **Build succeeded.** **Deploy blocked** — complying with Rob's directive to stop all SSH attempts.

### Site status
- **Committed, NOT deployed** (per Rob's directive — no SSH until cleared)
- 28 content pieces: 17 reviews + 2 guides + 9 comparisons
- Rating range: 2.5–4.5 across 17 reviews (4/5 is most common with 8 servers)
- Only 2 servers remain unreviewed: Figma Dev Mode, Vercel MCP

### What should happen next
- **Run 34:** Check inbox for Rob's SSH clearance. Write Figma Dev Mode or Vercel MCP review.
- **Run 35+:** Deploy when Rob clears SSH. Execute promotion plan when accounts approved.
- **Future:** Favicon, newsletter setup, affiliate link integration

## Run 34 — 2026-03-14 — Content (Vercel MCP Server Review)

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No pending messages. No SSH clearance from Rob yet. Complying with deploy ban.

### What I did

1. **Wrote "The Vercel MCP Server — Deployment Monitoring and Management Through Your AI Assistant"** — `content/reviews/vercel-mcp-server.md`
   - **18th review**, first deployment platform MCP server
   - Rating: **3.5/5** — solid remote-first architecture with strong security, but thin tool coverage
   - 13 tools across 5 categories: documentation, project management, deployments, domains, access/CLI
   - Standout feature: runtime log querying with filtering by level, status code, time range, and full-text search
   - Clean remote-first setup at `mcp.vercel.com` — zero install, OAuth auth, project-specific URLs
   - Honest about tradeoffs: only covers ~20% of Vercel's platform features, client allowlist limits adoption, deploy is CLI passthrough, still public beta after 7 months
   - Compared to community alternatives (Quegenx with 30+ tools) — official is safer, community is more capable

2. **Updated mega-comparison** (`content/guides/best-mcp-servers.md`)
   - Added "Deployment" category section with Vercel 3.5/5
   - Added deployment row to summary table
   - Removed Vercel from "servers we haven't reviewed" (only Figma Dev Mode remains)
   - Updated review count to 18, rating distribution (3.5/5 cluster now has 6 servers)

3. **Build succeeded.** **Deploy blocked** — complying with Rob's directive to stop all SSH attempts.

### Site status
- **Committed, NOT deployed** (per Rob's directive — no SSH until cleared)
- 29 content pieces: 18 reviews + 2 guides + 9 comparisons
- Rating range: 2.5–4.5 across 18 reviews
- Only 1 server remains unreviewed: Figma Dev Mode

### What should happen next
- **Run 35:** Check inbox for Rob's SSH clearance. Write Figma Dev Mode MCP review (last unreviewed server).
- **Run 36+:** Deploy when Rob clears SSH. Execute promotion plan when accounts approved.
- **Future:** Favicon, newsletter setup, affiliate link integration

## Run 35 — 2026-03-14 — Content (Figma Dev Mode MCP Server Review — Final Unreviewed Server)

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No pending messages. No SSH clearance from Rob yet. Complying with deploy ban.

### What I did

1. **Wrote "The Figma Dev Mode MCP Server — Design-to-Code Translation Through Your AI Assistant"** — `content/reviews/figma-dev-mode-mcp-server.md`
   - **19th review**, last unreviewed server from our original list
   - Rating: **3.5/5** — unique write capabilities but crippling free tier
   - 12 tools (8 read, 4 write) covering code generation, design tokens, Code Connect, screenshots, FigJam, and code-to-canvas capture
   - Killer feature: `generate_figma_design` — captures live web pages and converts them to editable Figma frames. No community server can do this.
   - Code Connect maps Figma components to codebase components for improving code generation accuracy over time
   - Biggest issue: **6 tool calls/month** on free tier — most aggressive rate limiting of any MCP server we've reviewed. Paid Figma plan (Dev/Full seats) effectively required.
   - Prescriptive React+Tailwind output can conflict with existing codebases; nested components get flattened
   - Detailed comparison with community Framelink server (13,700 stars vs 403 for official): Framelink outputs descriptive JSON, preserves nesting, ~25% smaller payloads, no seat-type rate limits
   - OAuth remote-first architecture at `mcp.figma.com/mcp`

2. **Updated mega-comparison** (`content/guides/best-mcp-servers.md`)
   - Added "Design-to-code" category row with Figma Dev Mode 3.5/5
   - Added full design-to-code section with Framelink comparison
   - Changed "What about servers we haven't reviewed?" to "All servers reviewed" — milestone reached
   - Updated review count to 19, rating distribution (3.5/5 cluster now has 7 servers)

3. **Build succeeded** (38ms). **Deploy blocked** — complying with Rob's directive to stop all SSH attempts.

### Site status
- **Committed, NOT deployed** (per Rob's directive — no SSH until cleared)
- 30 content pieces: 19 reviews + 2 guides + 9 comparisons
- Rating range: 2.5–4.5 across 19 reviews
- **All servers from original list now reviewed** — milestone reached
- 5 runs of content waiting to deploy

### What should happen next
- **Run 36:** Check inbox for Rob's SSH clearance. With all servers reviewed, pivot to new content types: deeper guides, workflow tutorials, or new server categories (AI/ML, cloud infrastructure, DevOps).
- **Run 37+:** Deploy when Rob clears SSH. Execute promotion plan when accounts approved.
- **Future:** Favicon, newsletter setup, affiliate link integration, new review targets
