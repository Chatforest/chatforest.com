# ChatForest Work Log

## Run 1 — 2026-03-13 — Research (Landscape Analysis)

**Mode:** Researcher

### What I did
Conducted market research on MCP directories, AI tools directories, and monetization models. Full findings in `research/01-landscape-analysis.md`.

### Key findings
1. **MCP directory space is saturated** — PulseMCP has 9,080+ servers, official MCP Registry exists (backed by Anthropic/GitHub/Microsoft). Competing on volume is a losing game.
2. **AI tools directory space is a red ocean** — theresanaiforthat.com, Futurepedia, Toolify, AITopTools all have massive head starts.
3. **Monetization models** — Affiliate (20-30% recurring), sponsored listings, subscriptions, newsletter ads, paid MCP servers.
4. **Gaps identified:**
   - Quality curation + honest reviews (most directories are just lists)
   - AI-native editorial content (agents reviewing tools — unique angle nobody has)
   - MCP ecosystem education (tutorials, guides, comparisons — not listings)
   - Trust-based media brand (2026 trend away from SEO arbitrage)

### Recommendation forming
The strongest positioning for ChatForest may be **AI-native content + MCP ecosystem focus** — not a directory, but a content site where AI agents publicly review, compare, and explain AI tools (especially MCP servers). This is differentiated because:
- Transparent AI authorship is our feature, not a liability
- No one else has agents-as-reviewers as their editorial model
- MCP ecosystem content (guides, tutorials) is underserved vs. raw listings
- Can monetize via affiliate, sponsored content, newsletter

### What should happen next
- **Run 2:** Strategist mode — Formalize business model, define target audience, compare positioning options
- **Run 3:** Copywriter mode — Draft site voice/tone, write sample content pieces
- **Run 4:** Designer/Developer — Plan site structure, start building

### Questions for Rob
- Sent via Jikan inbox: initial direction recommendation for feedback

## Run 2 — 2026-03-13 — Strategy (Business Model)

**Mode:** Strategist

### What I did
Formalized the business model and positioning for ChatForest. Full document in `strategy/01-business-model.md`.

Additional research conducted:
- AI transparency/disclosure trends (C2PA adoption, regulatory requirements — supports our transparent-AI-authorship angle)
- MCP education content landscape (mostly paid courses on Udemy/Frontend Masters + official docs — free editorial content is a gap)
- AI/SaaS affiliate programs (20-40% recurring commissions widely available — strong monetization path)

### Strategy summary
**Positioning:** AI-native editorial site where AI agents review, tutorial, and compare MCP servers and AI tools. Transparent AI authorship is the differentiator.

**Target audience:** Developers building with MCP (primary), AI-curious professionals (secondary), AI tool builders (tertiary/sponsors).

**Content types:** MCP server reviews, tutorials/guides, comparisons, ecosystem updates, AI workflow guides.

**Revenue model:**
- Phase 1 (months 1-3): Build content library, $0 cost
- Phase 2 (months 3-6): Affiliate links + newsletter sponsorships, target $500/mo
- Phase 3 (months 6-12): Add sponsored reviews + premium content, target $2-5K/mo

### Status of Rob's feedback
- Run 1 inbox message (direction recommendation): no reply yet
- Run 2 inbox message sent: strategy summary with 5 specific questions

### What should happen next
- **Run 3:** Copywriter mode — Define editorial voice/tone, write 1-2 sample content pieces to test the concept
- **Run 4:** Designer mode — Plan site structure, information architecture
- **Run 5:** Developer mode — Start building the site

### Decisions made
- Not pursuing pure directory model (saturated market)
- Focusing on content/editorial rather than tooling/marketplace
- MCP ecosystem as primary content wedge, broader AI tools as expansion
- Phased monetization approach (content-first, then revenue)

## Run 3 — 2026-03-13 — Copywriting (Voice, Tone & Sample Content)

**Mode:** Copywriter

### Inbox update
- **Rob approved the direction!** (message #73, high priority): "Thumbs up on the direction! AI-native content/review site focused on MCP ecosystem. Go ahead and formalize the business plan and start building."
- **Note from Rob** (message #75): Stripe keys available when needed — Tier 4 decision, send proposal when ready.

### What I did

1. **Created editorial voice & tone guide** — `content/voice-and-tone.md`
   - Defined 5 core voice principles: honest first, technical but readable, opinionated with receipts, transparent about AI authorship, practical over theoretical
   - Established tone spectrum per content type (reviews, tutorials, comparisons, updates, opinion)
   - Listed anti-patterns to avoid (corporate speak, hype, clickbait, pretending to be human)
   - Proposed primary tagline: "AI agents reviewing AI tools. Honestly."
   - Defined standard byline and AI disclosure format

2. **Wrote sample MCP server review** — `content/samples/01-filesystem-mcp-review.md`
   - Full review of the Filesystem MCP server
   - Tests the review format: setup, what works, what doesn't, who should use it, verdict with rating
   - Demonstrates the voice in practice: direct, opinionated, evidence-backed

3. **Wrote sample beginner guide** — `content/samples/02-what-is-mcp-guide.md`
   - "What Is MCP?" explainer for developers
   - Tests the tutorial format: problem/solution framing, architecture diagram, code examples, practical setup steps
   - Demonstrates accessible-but-technical tone

### Observations
- The review format works well — it's opinionated without being unfair, technical without being impenetrable
- The guide format hits the right level of depth for developers who know how to code but are new to MCP
- The AI disclosure at the bottom feels natural, not defensive
- Tagline "AI agents reviewing AI tools. Honestly." is concise and captures the positioning

### What should happen next
- **Run 4:** Designer mode — Plan site structure (pages, navigation, information architecture)
- **Run 5:** Developer mode — Start building the actual static site
- Consider: should we use a static site generator (11ty, Hugo) or hand-roll HTML/CSS for simplicity?

## Run 4 — 2026-03-13 — Designer/Developer (Site Build v1)

**Mode:** Designer + Developer

### What I did

Built the first version of the ChatForest static site. Hand-rolled HTML/CSS — no static site generator needed yet with only 2 content pieces. The site is clean, responsive, and ready to deploy.

**Files created in `site/`** (the deployable directory):
- `index.html` — Homepage with hero section, tagline, and latest articles listing
- `about.html` — About page explaining who we are, how we work, and our principles
- `reviews/index.html` — Reviews section listing page
- `reviews/filesystem-mcp-server.html` — Full Filesystem MCP server review
- `guides/index.html` — Guides section listing page
- `guides/what-is-mcp.html` — Full "What Is MCP?" developer guide
- `css/style.css` — Shared stylesheet

### Design decisions
- **No SSG.** With 2 articles, hand-rolled HTML is simpler and faster. When we hit ~10 articles, we should consider 11ty or Hugo to avoid maintaining duplicate header/footer HTML.
- **Typography-first design.** Georgia for body text (readable), system sans-serif for headings and UI (clean, fast). Dark green color palette ties to the "forest" brand.
- **Mobile responsive.** Single breakpoint at 600px. Content-first layout works on any screen.
- **Consistent structure.** Every page has the same header (logo, tagline, nav) and footer (AI disclosure, copyright). Articles follow a consistent template: meta, title, byline, body, AI disclosure.
- **Verdict component.** Reviews have a green-tinted verdict box for the rating — visual anchor for the key takeaway.
- **No JavaScript.** Pure HTML/CSS. Zero dependencies. Fast on any connection.

### Site structure
```
site/
├── index.html          (homepage)
├── about.html          (about)
├── css/
│   └── style.css       (shared styles)
├── reviews/
│   ├── index.html      (reviews listing)
│   └── filesystem-mcp-server.html
└── guides/
    ├── index.html      (guides listing)
    └── what-is-mcp.html
```

### What should happen next
- **Run 5:** Deploy — Set up deployment to DreamHost (rsync/scp the `site/` directory). This is Tier 2 (log it, proceed). Need to confirm DreamHost connection details.
- **Run 6+:** Content — Write more reviews and guides. Good candidates: GitHub MCP server, Brave Search MCP server, "How to Build Your First MCP Server" tutorial.
- **Future:** When article count reaches ~10, evaluate migrating to a static site generator (11ty is the likely pick — simple, Node-based, works with HTML/Markdown).
- **Future:** Add Open Graph meta tags for social sharing.

## Run 5 — 2026-03-13 — Content + SEO Infrastructure

**Mode:** Copywriter + Developer

### Inbox update
- No new messages from Rob. Deployment still blocked on DreamHost connection details (asked in Run 4, message #76).

### What I did

1. **Wrote GitHub MCP Server review** — `site/reviews/github-mcp-server.html` + `content/samples/03-github-mcp-review.md`
   - Full review of GitHub's official MCP server
   - Covers setup (remote, Docker, build-from-source), toolsets, what works (PR workflows, Actions integration), what doesn't (token scoping, Docker latency, rate limits, large diffs)
   - Rating: 4/5 — powerful but setup friction is real
   - Updated reviews index and homepage to include the new article

2. **Added RSS feed** — `site/feed.xml`
   - Standard RSS 2.0 feed with all 3 articles
   - Added `<link rel="alternate">` to homepage `<head>`

3. **Added sitemap** — `site/sitemap.xml`
   - All 7 pages listed with priorities

4. **Added robots.txt** — `site/robots.txt`
   - Allows all crawlers, points to sitemap

### Site status
- 3 content pieces: 2 reviews (Filesystem, GitHub MCP servers) + 1 guide (What Is MCP?)
- SEO infrastructure in place: sitemap, RSS, robots.txt
- Still needs: deployment to DreamHost, Open Graph meta tags

### What should happen next
- **Deploy:** Still waiting on DreamHost connection details from Rob
- **Run 6:** Write another piece — good candidates: Brave Search MCP server review, "How to Build Your First MCP Server" tutorial, or Slack MCP server review
- **Run 7+:** Open Graph meta tags, favicon, more content
- **At ~10 articles:** Evaluate migrating to 11ty static site generator

## Run 6 — 2026-03-13 — Content (Build Your First MCP Server Tutorial)

**Mode:** Copywriter + Developer

### Inbox update
- No new messages from Rob. DreamHost deployment still blocked on connection details (asked in Run 4, message #76).

### What I did

1. **Wrote "How to Build Your First MCP Server" tutorial** — `site/guides/build-your-first-mcp-server.html` + `content/samples/04-build-first-mcp-server.md`
   - Step-by-step Python tutorial using FastMCP SDK
   - Covers: project setup (uv + pip), writing tools, local testing, MCP Inspector, Claude Desktop integration, adding resources, error handling
   - Uses a mock weather server as the example — keeps focus on MCP concepts, not API key management
   - Delivers on the promise from the "What Is MCP?" guide ("We'll cover building MCP servers in depth in future articles")
   - Practical advice: return error messages as strings, don't raise exceptions

2. **Updated all indexes and feeds:**
   - Homepage: added article card at top of Latest section
   - Guides index: added article card above "What Is MCP?"
   - RSS feed: added item with pubDate
   - Sitemap: added URL entry

### Site status
- 4 content pieces: 2 reviews (Filesystem, GitHub MCP servers) + 2 guides (What Is MCP?, Build Your First MCP Server)
- Guides now form a natural learning path: understand MCP → build with MCP
- SEO infrastructure up to date (sitemap, RSS, robots.txt)
- Still needs: deployment to DreamHost, Open Graph meta tags, favicon

### What should happen next
- **Deploy:** Still waiting on DreamHost connection details from Rob
- **Run 7:** Write another review — Brave Search MCP server or Slack MCP server are good candidates
- **Run 8+:** Open Graph meta tags, favicon, more content
- **At ~10 articles:** Evaluate migrating to 11ty static site generator

## Run 7 — 2026-03-13 — Content + SEO Polish (Brave Search Review + OG Tags)

**Mode:** Copywriter + Developer

### Inbox update
- No new messages from Rob. DreamHost deployment still blocked on connection details (asked in Run 4, message #76).

### What I did

1. **Wrote Brave Search MCP Server review** — `site/reviews/brave-search-mcp-server.html` + `content/samples/05-brave-search-mcp-review.md`
   - Full review of Brave's official MCP server
   - Covers all 6 tools (web, local, image, video, news, summarizer), setup, pricing, strengths/weaknesses
   - Comparison vs. Google wrappers (SerpAPI/Tavily), Exa, and Perplexity
   - Rating: 4/5 — the default search server for most agents
   - Updated homepage, reviews index, RSS feed, and sitemap

2. **Added Open Graph meta tags to all pages**
   - All 9 HTML pages now have og:title, og:description, og:type, og:url, og:site_name
   - Articles use og:type="article", section/listing pages use og:type="website"
   - This improves link previews when shared on social media, Slack, Discord, etc.

### Site status
- 5 content pieces: 3 reviews (Filesystem, GitHub, Brave Search MCP servers) + 2 guides (What Is MCP?, Build Your First MCP Server)
- SEO infrastructure: sitemap, RSS, robots.txt, Open Graph meta tags
- Still needs: deployment to DreamHost, favicon

### What should happen next
- **Deploy:** Still waiting on DreamHost connection details from Rob
- **Run 8:** Write another review — Slack MCP server, Puppeteer MCP server, or SQLite MCP server are good candidates
- **Run 9+:** Favicon, more content, possibly a comparison article ("Best MCP Servers for Developers in 2026")
- **At ~10 articles:** Evaluate migrating to 11ty static site generator

## Run 8 — 2026-03-13 — SSH Key + Content (Slack MCP Server Review)

**Mode:** Developer + Copywriter

### Inbox update
- **Rob requested SSH key** (message #77): "please create an ssh key for yourself that we'll use to give you access to chatforest"
- Created Ed25519 key pair, sent public key back via inbox (message #78)
- Deployment unblocked once Rob adds the key to DreamHost

### What I did

1. **Created SSH key pair** — Ed25519 key at `~/.ssh/id_ed25519` for DreamHost deployment access. Public key sent to Rob via Jikan inbox.

2. **Wrote Slack MCP Server review** — `site/reviews/slack-mcp-server.html` + `content/samples/06-slack-mcp-review.md`
   - Full review of Slack's official MCP server (launched Feb 2026)
   - Covers: hosted architecture (mcp.slack.com), OAuth scopes, search, messaging, canvases, user lookup
   - Strengths: granular privacy controls, natural language responses, no local install, admin oversight
   - Weaknesses: Marketplace requirement for custom clients, no SSE, missing features (reactions, scheduling), rate limit handling
   - Compared to community server, korotovsky server, and Slack's native AI
   - Rating: 4/5 — the right way to give agents Slack access
   - Updated homepage, reviews index, RSS feed, and sitemap

### Site status
- 6 content pieces: 4 reviews (Filesystem, GitHub, Brave Search, Slack MCP servers) + 2 guides (What Is MCP?, Build Your First MCP Server)
- SSH key created — awaiting Rob to add it to DreamHost for deployment
- SEO infrastructure up to date (sitemap, RSS, robots.txt, Open Graph meta tags)

### What should happen next
- **Deploy:** Waiting for Rob to add SSH key to DreamHost, then we can rsync the site/ directory
- **Run 9:** Write another review — Puppeteer MCP server, SQLite MCP server, or Postgres MCP server are good candidates
- **Run 10+:** Favicon, comparison article ("Best MCP Servers for Developers in 2026"), more content
- **At ~10 articles:** Evaluate migrating to 11ty static site generator

## Run 9 — 2026-03-14 — Content (Puppeteer MCP Server Review)

**Mode:** Copywriter + Developer

### Inbox update
- **Rob asked about DreamHost public directory** (message #79): `~/chatforest.com/` or `~/chatforest.com/wwwroot/`. Replied requesting `~/chatforest.com/` directly for simplicity.
- **Rob offered a database** (message #80): Declined for now — pure static site doesn't need one. Will reconsider if we add search, comments, or analytics.
- No update yet on SSH key being added to DreamHost.

### What I did

1. **Wrote Puppeteer MCP Server review** — `site/reviews/puppeteer-mcp-server.html`
   - Full review of the official @modelcontextprotocol/server-puppeteer
   - Covers all 7 tools: navigate, screenshot, click, fill, select, hover, evaluate
   - Strengths: zero-config setup, screenshot + vision capability, JavaScript evaluation flexibility, stateful sessions
   - Weaknesses: CSS selector brittleness, no accessibility tree, Chrome-only, RAM usage, anti-bot detection issues
   - Head-to-head comparison with Playwright MCP, Browserbase, and Firecrawl
   - Rating: 3.5/5 — capable but showing its age next to Playwright MCP
   - **First non-4/5 rating** — being honest about Playwright MCP being the better choice for most new projects

2. **Updated all indexes and feeds:**
   - Homepage: added article card at top of Latest section
   - Reviews index: added article card above Slack review
   - RSS feed: added item with pubDate, updated lastBuildDate
   - Sitemap: added URL entry

### Observations
- This is the first review where I'm recommending an alternative over the reviewed product. The Playwright MCP server has genuinely overtaken Puppeteer for most use cases. Being honest about this is core to our editorial voice — we're not here to give everything 4/5.
- The review format handles nuance well: the "Consider Playwright MCP instead if" section lets readers self-sort without us being dismissive of Puppeteer.

### Site status
- 7 content pieces: 5 reviews (Filesystem, GitHub, Brave Search, Slack, Puppeteer MCP servers) + 2 guides (What Is MCP?, Build Your First MCP Server)
- SSH key created — awaiting Rob to add it to DreamHost and confirm directory structure
- SEO infrastructure up to date (sitemap, RSS, robots.txt, Open Graph meta tags)

### What should happen next
- **Deploy:** Waiting for Rob to add SSH key to DreamHost and confirm `~/chatforest.com/` as public dir
- **Run 10:** Write a Playwright MCP server review — natural follow-up to compare against Puppeteer, and it would give us a complete browser automation pair
- **Run 11+:** Favicon, comparison article ("Best MCP Servers for Developers in 2026"), more content
- **At ~10 articles:** Evaluate migrating to 11ty static site generator (we're at 7 now — getting close)

## Run 10 — 2026-03-14 — Content (Playwright MCP Server Review)

**Mode:** Copywriter + Developer

### Inbox update
- No new messages from Rob. Deployment still blocked on SSH key being added to DreamHost.
- Previous outgoing messages (#78, #81) still pending.

### What I did

1. **Wrote Playwright MCP Server review** — `site/reviews/playwright-mcp-server.html`
   - Full review of Microsoft's @playwright/mcp server (28,000+ GitHub stars)
   - Covers: accessibility tree targeting (the key differentiator), 25+ tools across capability tiers (core, vision, testing, PDF), setup for Claude Desktop / VS Code / Cursor
   - Strengths: accessibility tree element targeting, three browser engines (Chromium/Firefox/WebKit), comprehensive tool set, code generation, incremental snapshots, session persistence, massive ecosystem support
   - Weaknesses: snapshot size on complex pages (token explosion), accessibility tree gaps for canvas/custom widgets, 60+ config options (overwhelming), v0.0.x instability, browser lock errors in multi-agent setups, Windows/WSL issues
   - Head-to-head comparison with Puppeteer MCP, Browserbase, Firecrawl, and Playwright CLI+SKILLS approach
   - Rating: 4.5/5 — the browser server to beat
   - **First 4.5 rating and highest score yet** — earned by genuine technical superiority and ecosystem dominance
   - Naturally completes the browser automation pair with the Puppeteer review

2. **Updated all indexes and feeds:**
   - Homepage: added article card at top of Latest section
   - Reviews index: added article card above Puppeteer review
   - RSS feed: added item with pubDate, updated lastBuildDate
   - Sitemap: added URL entry

### Observations
- The Puppeteer → Playwright review pair works well editorially. Readers can compare both and make their own decision. The cross-links between the two reviews create a useful comparison path.
- Our rating range is now 3.5 to 4.5 across 6 reviews — the spread shows we're not rubber-stamping everything. Good for credibility.
- We're at 8 content pieces now. Getting close to the 10-article threshold for evaluating a static site generator.

### Site status
- 8 content pieces: 6 reviews (Filesystem, GitHub, Brave Search, Slack, Puppeteer, Playwright MCP servers) + 2 guides (What Is MCP?, Build Your First MCP Server)
- SSH key created — awaiting Rob to add it to DreamHost and confirm directory structure
- SEO infrastructure up to date (sitemap, RSS, robots.txt, Open Graph meta tags)

### What should happen next
- **Deploy:** Still waiting for Rob to add SSH key to DreamHost
- **Run 11:** Write another review — SQLite MCP server, Postgres MCP server, or Memory MCP server are good candidates. Or a comparison article ("Best Browser MCP Servers" using our Puppeteer + Playwright reviews as source material).
- **Run 12+:** Favicon, more content, comparison articles
- **At 10 articles:** Evaluate migrating to 11ty static site generator (we're at 8 now — 2 more)

## Run 11 — 2026-03-14 — Content (SQLite MCP Server Review)

**Mode:** Copywriter + Developer

### Inbox update
- No new messages from Rob. Deployment still blocked on SSH key being added to DreamHost.
- Previous outgoing messages (#78, #81) still pending.

### What I did

1. **Wrote SQLite MCP Server review** — `site/reviews/sqlite-mcp-server.html`
   - Full review of Anthropic's official `mcp-server-sqlite` reference implementation
   - Key editorial angle: this server has been **archived** (moved to `servers-archived` repo in early 2025). First review of an unmaintained MCP server — gives us credibility by being honest about official tools that have been abandoned.
   - Covers all 6 tools: `read_query`, `write_query`, `create_table`, `list_tables`, `describe_table`, `append_insight`
   - Highlights the clever `memo://insights` resource and `mcp-demo` prompt as educational features
   - Strengths: clean codebase, schema-first workflow, insight memo pattern, good for learning MCP
   - Weaknesses: archived/unmaintained, no safety guardrails (DROP TABLE runs immediately), single database per instance, no parameterized queries, limited client compatibility
   - Compared to jparkerweb/mcp-sqlite (community alternative, actively maintained), sqlite-explorer (read-only), Postgres MCP, and DuckDB MCP
   - Rating: **3/5** — a good demo, not a production tool
   - **Lowest rating yet** — our range is now 3.0 to 4.5 across 7 reviews. The spread shows editorial integrity.

2. **Updated all indexes and feeds:**
   - Homepage: added article card at top of Latest section
   - Reviews index: added article card above Playwright review
   - RSS feed: added item with pubDate, updated lastBuildDate
   - Sitemap: added URL entry

### Observations
- Reviewing an archived server is a strong editorial move. Most directories just list servers without noting maintenance status — we're explicitly calling out when something shouldn't be relied upon. This builds reader trust.
- Our rating distribution (3.0, 3.5, 4.0, 4.0, 4.0, 4.0, 4.5) tells a story: we're not handing out participation trophies.
- We're at 9 content pieces now — one more to the 10-article threshold for evaluating a static site generator.

### Site status
- 9 content pieces: 7 reviews (Filesystem, GitHub, Brave Search, Slack, Puppeteer, Playwright, SQLite MCP servers) + 2 guides (What Is MCP?, Build Your First MCP Server)
- SSH key created — awaiting Rob to add it to DreamHost and confirm directory structure
- SEO infrastructure up to date (sitemap, RSS, robots.txt, Open Graph meta tags)

### What should happen next
- **Deploy:** Still waiting for Rob to add SSH key to DreamHost
- **Run 12:** Write one more piece to hit 10 articles, then evaluate 11ty migration. Good candidates: Postgres MCP server review, Memory MCP server review, or a comparison article ("Best Database MCP Servers" or "Best Browser MCP Servers")
- **Run 13+:** 11ty migration evaluation, favicon, more content

## Run 12 — 2026-03-14 — First Deployment! (Site Goes Live)

**Mode:** Developer

### Inbox update
- **Rob sent SSH config** (message #82): Host `chat`, Hostname `chatforest.com`, User `backforest`. Confirmed the deploy target is `chatforest.com/` on the remote server. Existing files: `favicon.ico`, `favicon.gif`, and a placeholder `index.html`.
- **Rob asked for status** (message #83): Replied with full status update (message #84).

### What I did

1. **Set up SSH access** — Created `~/.ssh/config` with Rob's provided settings, using our Ed25519 key. Connection works.

2. **Deployed the site to chatforest.com** — `rsync -avz --delete --exclude='favicon.ico' --exclude='favicon.gif' site/ chat:chatforest.com/`
   - All 18 files deployed successfully (HTML pages, CSS, RSS, sitemap, robots.txt)
   - Preserved existing favicons on the server
   - Site confirmed live: HTTP 200 on homepage, reviews, guides, and RSS feed

3. **Verified all pages accessible:**
   - `https://chatforest.com/` — homepage ✓
   - `https://chatforest.com/reviews/sqlite-mcp-server.html` — latest review ✓
   - `https://chatforest.com/guides/what-is-mcp.html` — guide ✓
   - `https://chatforest.com/feed.xml` — RSS feed ✓

### Deployment workflow
```
rsync -avz --delete --exclude='favicon.ico' --exclude='favicon.gif' /home/grove/chatforest.com/site/ chat:chatforest.com/
```
This is the standard deploy command going forward. Takes ~2 seconds.

### Site status
- **LIVE at chatforest.com** 🎉
- 9 content pieces: 7 reviews (Filesystem, GitHub, Brave Search, Slack, Puppeteer, Playwright, SQLite MCP servers) + 2 guides (What Is MCP?, Build Your First MCP Server)
- SEO infrastructure: sitemap, RSS, robots.txt, Open Graph meta tags
- Deployment automated via rsync over SSH

### What should happen next
- **Run 13:** Write one more piece to hit 10 articles. Good candidates: Postgres MCP server review, Memory MCP server review, or a comparison article
- **Run 14:** Evaluate 11ty migration (at 10 articles, maintaining hand-rolled HTML becomes painful)
- **Future:** Favicon (custom), more content, comparison articles, newsletter setup

## Run 13 — 2026-03-14 — Content (PostgreSQL MCP Server Review)

**Mode:** Copywriter + Developer

### Inbox update
- No new messages from Rob. Site is live and deployed.

### What I did

1. **Wrote PostgreSQL MCP Server review** — `site/reviews/postgres-mcp-server.html`
   - Full review of Anthropic's official `@modelcontextprotocol/server-postgres`
   - **Key editorial angle: SQL injection vulnerability.** Datadog Security Labs found that the read-only transaction wrapper can be bypassed via multi-statement injection (`COMMIT; DROP SCHEMA public CASCADE;`). The Node.js postgres client accepts semicolon-delimited statements, so the read-only transaction is just cosmetic security.
   - Covers: single `query` tool, schema resources, setup (npx + Docker), the SQL injection vulnerability in detail, secondary attack vector (session variable poisoning)
   - Strengths: schema discovery via resources is the right pattern, standard PostgreSQL connection string, minimal surface area
   - Weaknesses: SQL injection bypasses read-only protection, archived (May 2025), npm package still vulnerable at v0.6.2 (21K weekly downloads), no query constraints, no parameterized queries, no performance guardrails, single database per instance
   - Compared to Postgres MCP Pro (crystaldba, 2.3K stars — the recommended replacement), pgEdge, AWS Aurora MCP, Azure PostgreSQL MCP, and our SQLite MCP review
   - Rating: **2.5/5** — a broken promise, now abandoned
   - **Lowest rating yet.** Our range is now 2.5 to 4.5 across 8 reviews. A security tool that gives false confidence is worse than no security tool at all.
   - Completes the database MCP server pair with the SQLite review, with cross-links between both

2. **Updated all indexes and feeds:**
   - Homepage: added article card at top of Latest section
   - Reviews index: added article card above SQLite review
   - RSS feed: added item with pubDate, updated lastBuildDate
   - Sitemap: added URL entry

3. **Deployed to chatforest.com** — rsync completed, all pages verified live.

### Observations
- This review has the strongest security narrative of any piece we've written. Documenting a real vulnerability with specific attack vectors and clear "stop using this" advice builds credibility fast.
- The 2.5 rating is justified: a server whose one promise (read-only) is provably broken deserves to score lower than the SQLite server (3/5), which at least never pretended to restrict writes.
- Our rating distribution (2.5, 3.0, 3.5, 4.0, 4.0, 4.0, 4.0, 4.5) now spans a full 2-point range. This is healthy editorial credibility.
- We've hit **10 content pieces** — the threshold for evaluating a static site generator migration.

### Site status
- **LIVE at chatforest.com**
- 10 content pieces: 8 reviews (Filesystem, GitHub, Brave Search, Slack, Puppeteer, Playwright, SQLite, PostgreSQL MCP servers) + 2 guides (What Is MCP?, Build Your First MCP Server)
- SEO infrastructure up to date (sitemap, RSS, robots.txt, Open Graph meta tags)
- Deployment automated via rsync over SSH

### What should happen next
- **Run 14:** Evaluate 11ty migration — we've hit 10 articles, and maintaining duplicate header/footer HTML across 12+ files is becoming painful. 11ty would let us use Markdown for content and templates for layout.
- **Run 15+:** More content — Memory MCP server review, comparison articles ("Best Database MCP Servers", "Best Browser MCP Servers"), favicon
- **Future:** Newsletter setup, affiliate link integration when traffic justifies it

## Run 14 — 2026-03-14 — Hugo Migration (Static Site Generator)

**Mode:** Developer

### Inbox update
- **Rob praised the site** (message #85): "It looks fantastic! Really proud of you, Grove." Suggested changing "editorial oversight" to "technical oversight" on about page — done.
- **Rob offered to help with favicon** (message #86): No existing favicons. Sent him a concept description (tree/speech-bubble icon or simple "CF" text mark).

### What I did

1. **Migrated the entire site to Hugo** — the site is now built with Hugo v0.68.3 (already installed on the server). This is the biggest infrastructure change since launch.

   **Why Hugo over 11ty:** Hugo was already installed (`/usr/bin/hugo`), requires no Node.js (which isn't available), and is fast (36ms builds). No dependency management needed.

   **What changed:**
   - All 10 articles converted from hand-rolled HTML to Markdown with YAML frontmatter
   - Header/footer/layout now defined once in templates, not duplicated across 14 files
   - RSS feed auto-generated by Hugo (was manually maintained)
   - Sitemap auto-generated by Hugo (was manually maintained)
   - New articles now require creating ONE file (a Markdown file in `content/`) instead of editing 5 files (article + homepage + section index + RSS + sitemap)
   - URL structure changed from `.html` extensions to clean URLs (e.g., `/reviews/postgres-mcp-server/` instead of `/reviews/postgres-mcp-server.html`)
   - About page text updated: "editorial oversight" → "technical oversight" per Rob's feedback

2. **Project structure:**
   ```
   chatforest.com/
   ├── config.toml              # Hugo config
   ├── content/
   │   ├── about.md             # About page
   │   ├── reviews/
   │   │   ├── _index.md        # Reviews listing
   │   │   └── *.md             # 8 review articles
   │   └── guides/
   │       ├── _index.md        # Guides listing
   │       └── *.md             # 2 guide articles
   ├── layouts/
   │   ├── _default/            # Base templates
   │   ├── reviews/             # Review-specific templates
   │   ├── guides/              # Guide-specific templates
   │   ├── partials/            # Shared components
   │   ├── shortcodes/          # verdict shortcode
   │   └── index.html           # Homepage
   ├── static/
   │   ├── css/style.css
   │   └── robots.txt
   ├── site/                    # Hugo output (deployed)
   └── archive/                 # Old sample content files
   ```

3. **Build command:** `hugo` (36ms, outputs to `site/`)
4. **Deploy command:** `rsync -avz --delete --exclude='favicon.ico' --exclude='favicon.gif' site/ chat:chatforest.com/`
5. **Deployed and verified** — all pages accessible, RSS feed working, all 10 articles rendering correctly.

### Benefits realized
- Adding a new article: create 1 Markdown file → `hugo` → deploy. Previously: edit 5 HTML files.
- Changing the header/footer: edit 1 template file. Previously: edit 14 HTML files.
- RSS/sitemap: automatic. Previously: manual XML editing.
- Content is now Markdown: easier to write, read, and maintain than raw HTML.

### URL change note
URLs changed from `.html` to clean URLs. Since the site has only been live for ~1 day with minimal external traffic, this should have no SEO impact. Hugo generates proper sitemap.xml for search engine discovery.

### What should happen next
- **Run 15:** Write new content — Memory MCP server review or a comparison article ("Best Database MCP Servers" or "Best Browser MCP Servers")
- **Run 16+:** Favicon (waiting for Rob's direction), more content
- **Future:** Newsletter setup, affiliate link integration when traffic justifies it

## Run 15 — 2026-03-14 — Content (First Comparison Article)

**Mode:** Copywriter + Developer

### Inbox update
- No new messages from Rob. Only pending message was our own #87 (favicon concept) — marked as seen.

### What I did

1. **Wrote "Best Browser Automation MCP Servers in 2026"** — `content/guides/best-browser-mcp-servers.md`
   - **First comparison article** — new content type beyond reviews and guides
   - Head-to-head comparison of Playwright MCP, Puppeteer MCP, Browserbase, and Firecrawl
   - Feature comparison table, decision flowchart, clear recommendations for each use case
   - Links back to our individual Playwright (4.5/5) and Puppeteer (3.5/5) reviews
   - Brief coverage of Stagehand as an emerging alternative
   - Verdict: Playwright MCP is the clear winner for 2026

2. **Deployed to chatforest.com** — verified live at `/guides/best-browser-mcp-servers/`

### Observations
- The comparison format works well as a complement to individual reviews. Reviews go deep on one product; comparisons help readers choose between products. Different search intents, different value.
- Hugo made this trivial — created one Markdown file, built in 23ms, deployed. The SSG migration is paying off immediately.
- This is strong SEO content: "best browser MCP servers" is a comparison query that our individual reviews don't capture.

### Site status
- **LIVE at chatforest.com**
- 11 content pieces: 8 reviews + 2 guides + 1 comparison
- Content types: reviews, tutorials, explainers, comparisons — good editorial variety
- SEO infrastructure up to date (sitemap, RSS, robots.txt, Open Graph meta tags)

### What should happen next
- **Run 16:** Write another review or comparison — good candidates: Memory MCP server review, "Best Database MCP Servers" comparison (leveraging SQLite + Postgres reviews), or Fetch/HTTP MCP server review
- **Run 17+:** Favicon (waiting for Rob), more content
- **Future:** Newsletter setup, affiliate link integration, "Best MCP Servers for Developers" mega-comparison

## Run 16 — 2026-03-14 — Content (Database MCP Server Comparison)

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No new messages from Rob. Site is live and deployed.

### What I did

1. **Wrote "Best Database MCP Servers in 2026"** — `content/guides/best-database-mcp-servers.md`
   - **Second comparison article** — completes the pair with the browser comparison from Run 15
   - Covers 6 servers: Official SQLite (3/5), Official Postgres (2.5/5), Postgres MCP Pro (crystaldba), MotherDuck DuckDB, DBHub (Bytebase), jparkerweb/mcp-sqlite
   - Researched current state of each community server (web search for latest features/tools)
   - Feature comparison table across all 6 servers (maintenance status, safety, performance analysis, multi-database support)
   - Strong editorial angle: the official servers failed, here's what to use instead
   - Setup examples for each recommended server
   - Decision flowchart by database engine and use case
   - Cross-links back to our SQLite and Postgres individual reviews

2. **Deployed to chatforest.com** — verified live at `/guides/best-database-mcp-servers/`

### Observations
- The "official servers failed, here's the alternatives" angle is strong editorial positioning. It demonstrates we're not just listing tools — we're guiding readers away from bad choices.
- Both comparison articles now follow the same structure: contender table → why X failed/what matters → detailed alternatives → feature comparison → recommendations → flowchart. Consistent format helps readers navigate.
- Hugo continues to pay off — one Markdown file, 26ms build, deploy. No template editing needed.
- We now have 2 comparison articles that serve as "hub" content linking to our individual reviews. Good for SEO (comparison queries) and internal linking.

### Site status
- **LIVE at chatforest.com**
- 12 content pieces: 8 reviews + 2 guides + 2 comparisons
- Content types: reviews, tutorials, explainers, comparisons
- SEO infrastructure up to date (sitemap, RSS, robots.txt, Open Graph meta tags)

### What should happen next
- **Run 17:** Write another review — good candidates: Memory MCP server review, Fetch/HTTP MCP server review, or a cloud-hosted MCP server (Neon, Supabase)
- **Run 18+:** Favicon (waiting for Rob), more content
- **Future:** Newsletter setup, affiliate link integration, "Best MCP Servers for Developers" mega-comparison that links all our category comparisons

## Run 17 — 2026-03-14 — Content (Memory MCP Server Review)

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No new messages from Rob. Site is live and deployed.

### What I did

1. **Wrote Memory MCP Server review** — `content/reviews/memory-mcp-server.md`
   - Full review of Anthropic's official `@modelcontextprotocol/server-memory` (Knowledge Graph Memory)
   - Researched: current npm stats (~45K weekly downloads), GitHub status (actively maintained, not archived), community issues (context bloat, isolation problems), alternatives landscape (Zep, mem0, Chroma, Basic Memory)
   - Covers all 9 tools across entities, relations, observations, and retrieval
   - Key editorial angle: the concept is right (agents that remember are better) but the implementation has real scaling problems
   - Strengths: intuitive entity-relation model, persistent memory across conversations, transparent JSONL storage, good search for targeted retrieval, actively maintained
   - Weaknesses: `read_graph` dumps entire context (14K+ tokens reported), no memory isolation between projects, no deduplication/conflict resolution, JSONL doesn't scale, no semantic search, no access controls
   - Compared to Zep (temporal knowledge graphs), mem0/MemZero (semantic retrieval), Chroma (embedding-based search), Basic Memory (note-taking paradigm), and our SQLite MCP review
   - Rating: **3.5/5** — the right idea, not yet the right tool for serious use
   - Cross-links to our SQLite MCP server review (both official Anthropic implementations)

2. **Deployed to chatforest.com** — verified live at `/reviews/memory-mcp-server/`

### Observations
- This is our first review of an actively maintained official server that still gets a middling score. Filesystem (4/5) and GitHub (4/5) scored higher; Memory's 3.5 reflects real scaling concerns despite active maintenance. Being maintained doesn't automatically mean being good.
- Our rating distribution now: 2.5, 3.0, 3.5, 3.5, 4.0, 4.0, 4.0, 4.0, 4.5 across 9 reviews. The 3.5 cluster is growing — honest but not harsh.
- "Knowledge & Memory" is the largest MCP server category (283 servers on Glama). There's a potential comparison article here: "Best Memory MCP Servers" covering the official server, Zep, mem0, and others.

### Site status
- **LIVE at chatforest.com**
- 13 content pieces: 9 reviews + 2 guides + 2 comparisons
- Content types: reviews, tutorials, explainers, comparisons
- SEO infrastructure up to date (sitemap, RSS, robots.txt, Open Graph meta tags)

### What should happen next
- **Run 18:** Write another review or comparison — good candidates: Fetch/HTTP MCP server review, "Best Memory MCP Servers" comparison (leveraging this review), or a cloud-hosted MCP server (Neon, Supabase)
- **Run 19+:** Favicon (waiting for Rob), more content
- **Future:** Newsletter setup, affiliate link integration, "Best MCP Servers for Developers" mega-comparison

## Run 18 — 2026-03-14 — Content (Fetch MCP Server Review)

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No new messages from Rob. Site is live and deployed.

### What I did

1. **Wrote Fetch MCP Server review** — `content/reviews/fetch-mcp-server.md`
   - Full review of Anthropic's official `mcp-server-fetch` (Python package, ~140K weekly PyPI downloads)
   - **Key editorial angle: SSRF vulnerability.** The server has no built-in protection against fetching internal/localhost URLs. The README warns about this but doesn't fix it. An open PR (#3180) proposes SSRF protection but hasn't been merged as of March 2026.
   - Covers: single `fetch` tool with URL/max_length/start_index/raw params, HTML-to-markdown pipeline (readabilipy + markdownify), robots.txt handling (respects for tool calls, ignores for prompt calls), proxy support
   - Strengths: solid HTML-to-markdown extraction, chunked reading for long pages, ethical robots.txt handling, wide client support (~140K weekly downloads)
   - Weaknesses: no SSRF protection (will fetch localhost/AWS metadata), no JavaScript rendering (plain HTTP via httpx), 5000-char default limit, crashes on malformed input (open bug #3359), single tool with no batch fetching, no authenticated fetching
   - Compared to zcaceres/fetch-mcp (SSRF protection + 6 tools), fetcher-mcp (Playwright-based JS rendering), Firecrawl (full scraping/crawling platform), and our Playwright MCP review
   - Rating: **3.5/5** — the simplest web access for agents, just don't point it at anything internal
   - Cross-links to our Playwright MCP review and browser comparison article

2. **Deployed to chatforest.com** — verified live at `/reviews/fetch-mcp-server/`

### Observations
- This is another review where the security angle drives the narrative. Like the Postgres review (SQL injection), the Fetch review highlights a real vulnerability the README acknowledges but doesn't fix. This pattern — calling out security issues in official tools — is becoming a strong editorial signature.
- The 3.5 rating matches the Memory server: useful for basic/trusted use cases but with real gaps. Our rating distribution now: 2.5, 3.0, 3.5, 3.5, 3.5, 4.0, 4.0, 4.0, 4.0, 4.5 across 10 reviews.
- We've now reviewed 10 MCP servers. Good coverage across categories: filesystem, version control, search, communication, browser automation (x2), databases (x2), memory, and web fetching.

### Site status
- **LIVE at chatforest.com**
- 14 content pieces: 10 reviews + 2 guides + 2 comparisons
- Content types: reviews, tutorials, explainers, comparisons
- SEO infrastructure up to date (sitemap, RSS, robots.txt, Open Graph meta tags)

### What should happen next
- **Run 19:** Write another review or comparison — good candidates: "Best Memory MCP Servers" comparison, "Best Web Fetching MCP Servers" comparison (leveraging this review), or a cloud-hosted MCP server review (Neon, Supabase, Cloudflare)
- **Run 20+:** Favicon (waiting for Rob), more content
- **Future:** Newsletter setup, affiliate link integration, "Best MCP Servers for Developers" mega-comparison that links all category comparisons

## Run 19 — 2026-03-14 — Content (Web Scraping & Fetching Comparison)

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No new messages from Rob. Site is live and deployed.

### What I did

1. **Wrote "Best Web Scraping & Fetching MCP Servers in 2026"** — `content/guides/best-web-scraping-mcp-servers.md`
   - **Third comparison article** — completes a trio with browser automation and database comparisons
   - Head-to-head comparison of 7 servers: Official Fetch (3.5/5), zcaceres/fetch-mcp, fetcher-mcp, Firecrawl, Crawl4AI + RAG wrapper, Browserbase, and Jina AI MCP
   - Researched current state of each server (GitHub stars, features, pricing, tools)
   - Feature comparison table across all 7 servers (JS rendering, SSRF protection, batch fetching, crawling, search, CAPTCHA solving, etc.)
   - Decision flowchart from simple fetch → JS rendering → anti-bot → scale → research
   - Clear recommendation: zcaceres/fetch-mcp as the default choice (security + 6 formats + free)
   - Cross-links to our Fetch MCP review, Playwright MCP review, and browser automation comparison
   - Strong editorial angle: the official server has a known security gap, here's what to use instead

2. **Deployed to chatforest.com** — verified live at `/guides/best-web-scraping-mcp-servers/`

### Observations
- This is our most comprehensive comparison yet — 7 servers spanning free/paid, local/cloud, HTTP-only/browser-based. The decision flowchart helps readers self-sort quickly.
- We now have 3 comparison articles covering the major MCP server categories: browser automation, databases, and web scraping/fetching. These "hub" pages create strong internal linking to our individual reviews.
- The web scraping space has matured fast — a year ago the official Fetch server was the only option. Now there are specialized tools for every use case. Good timing for this content.
- Hugo continues to pay off: one Markdown file, 22ms build, deploy. No template editing needed.

### Site status
- **LIVE at chatforest.com**
- 15 content pieces: 10 reviews + 2 guides + 3 comparisons
- Content types: reviews, tutorials, explainers, comparisons
- SEO infrastructure up to date (sitemap, RSS, robots.txt, Open Graph meta tags)

### What should happen next
- **Run 20:** Write another review — good candidates: EverArt/image generation MCP server, Sentry MCP server, or a cloud-hosted database MCP (Neon, Supabase). Or a "Best Memory MCP Servers" comparison leveraging our Memory review.
- **Run 21+:** Favicon (waiting for Rob), more content
- **Future:** Newsletter setup, affiliate link integration, "Best MCP Servers for Developers" mega-comparison that links all 3 category comparisons

## Run 20 — 2026-03-14 — Content (Memory & Knowledge MCP Server Comparison)

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No new messages from Rob. Site is live and deployed.

### What I did

1. **Wrote "Best Memory & Knowledge MCP Servers in 2026"** — `content/guides/best-memory-mcp-servers.md`
   - **Fourth comparison article** — completes coverage of the major MCP server categories
   - Head-to-head comparison of 6 servers: Official Memory (3.5/5), Zep (temporal knowledge graphs), mem0 (semantic retrieval), Basic Memory (local Markdown), Chroma (embedding database), Engram (coding agent sessions)
   - Researched current state of each server (GitHub stars, tools, features, pricing, limitations)
   - Feature comparison table across all 6 servers (semantic search, temporal awareness, memory isolation, storage, read/write via MCP, human-readable storage, zero-config setup, free access)
   - Decision flowchart by use case: simple personal memory → enterprise temporal → semantic retrieval → human-readable → building block → coding sessions
   - Cross-links to our individual Memory MCP server review
   - Strong editorial framing: "memory has matured past the one knowledge graph file era"

2. **Committed Run 19 leftovers** — site output from the web scraping comparison was uncommitted.

3. **Deployed to chatforest.com** — verified live at `/guides/best-memory-mcp-servers/`

### Observations
- We now have 4 comparison articles covering browser automation, databases, web scraping/fetching, and memory/knowledge. These cover the major MCP server categories developers search for. A "mega-comparison" linking all four could be strong hub content.
- The memory space is the most diverse — approaches range from JSONL files to temporal knowledge graphs to embedding databases. The comparison format handles this well by organizing along clear axes (local vs cloud, search type, general vs specialized).
- Hugo build: 26ms, deploy: ~2 seconds. The SSG migration continues to pay for itself.

### Site status
- **LIVE at chatforest.com**
- 16 content pieces: 10 reviews + 2 guides + 4 comparisons
- Content types: reviews, tutorials, explainers, comparisons
- Comparison articles now cover: browser automation, databases, web scraping, memory/knowledge
- SEO infrastructure up to date (sitemap, RSS, robots.txt, Open Graph meta tags)

### What should happen next
- **Run 21:** Write another review — good candidates: EverArt/image generation MCP server, Sentry MCP server, Neon/Supabase cloud database MCP, or Exa search MCP server
- **Run 22+:** Favicon (waiting for Rob), "Best MCP Servers for Developers" mega-comparison linking all 4 category comparisons, more reviews
- **Future:** Newsletter setup, affiliate link integration

## Run 21 — 2026-03-14 — Content (Sentry MCP Server Review)

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No new messages from Rob. Site is live and deployed.

### What I did

1. **Wrote Sentry MCP Server review** — `content/reviews/sentry-mcp-server.md`
   - Full review of Sentry's official `@sentry/mcp-server` (579 GitHub stars, ~17.8K weekly npm downloads)
   - **First observability/developer tools category review** — expands our coverage beyond the filesystem/browser/database/memory categories
   - Researched: current npm stats, GitHub issues (748+), OAuth implementation, Seer AI integration, alternatives landscape (Datadog, PagerDuty, Honeycomb, Grafana, community alternatives)
   - Key editorial angle: this is the best example of how first-party MCP integration *should* work (OAuth, zero-install remote hosting, proprietary AI integration) — but the execution is still rough at v0.29.0
   - Strengths: OAuth 2.0 auth (no tokens on disk), zero-install remote server at mcp.sentry.dev, Seer AI root cause analysis, ~20 tools across issue investigation/event analysis/project management, first-party maintenance
   - Weaknesses: 748+ GitHub issues (auth errors, query failures, compatibility issues), AI search requires separate LLM provider key, cross-project queries return 400 errors, 63 npm dependencies, pre-1.0 instability, Seer may not be available on self-hosted instances
   - Compared to community Sentry MCP servers (MCP-100/mcp-sentry, ddfourtwo/sentry-selfhosted-mcp), Datadog MCP, PagerDuty MCP, Grafana MCP, Honeycomb MCP
   - Rating: **4/5** — first-party quality for Sentry users, with the rough edges you'd expect at v0.29
   - **First 4/5 in a new category.** Our rating distribution now: 2.5, 3.0, 3.5, 3.5, 3.5, 4.0, 4.0, 4.0, 4.0, 4.0, 4.5 across 11 reviews.

2. **Deployed to chatforest.com** — verified live at `/reviews/sentry-mcp-server/`

### Observations
- The observability category is a natural expansion for us. Sentry, Datadog, Grafana, PagerDuty all have official MCP servers now. There's a potential "Best Observability MCP Servers" comparison article here.
- Sentry's OAuth + remote hosting model is genuinely ahead of most MCP servers. Worth highlighting as a pattern other server authors should adopt.
- Our review coverage is broadening: filesystem, version control, search, communication, browser automation (x2), databases (x2), memory, web fetching, and now observability. Good category diversity.

### Site status
- **LIVE at chatforest.com**
- 17 content pieces: 11 reviews + 2 guides + 4 comparisons
- Content types: reviews, tutorials, explainers, comparisons
- Comparison articles cover: browser automation, databases, web scraping, memory/knowledge
- SEO infrastructure up to date (sitemap, RSS, robots.txt, Open Graph meta tags)

### What should happen next
- **Run 22:** Write another review or comparison — good candidates: "Best Observability MCP Servers" comparison (leveraging this review), Exa search MCP server review, EverArt/image generation MCP server review, or Neon/Supabase cloud database MCP review
- **Run 23+:** Favicon (waiting for Rob), "Best MCP Servers for Developers" mega-comparison linking all category comparisons, more reviews
- **Future:** Newsletter setup, affiliate link integration

## Run 22 — 2026-03-14 — Content (Exa MCP Server Review)

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No new messages from Rob. Site is live and deployed.

### What I did

1. **Wrote Exa MCP Server review** — `content/reviews/exa-mcp-server.md`
   - Full review of Exa's official `exa-mcp-server` (4,000 GitHub stars, 301 forks, MIT license)
   - **Key editorial angle: semantic search vs keyword search.** Exa uses neural embeddings to understand *concepts*, not just keywords — measurably outperforms Tavily (81% vs 71% on WebWalker benchmark) with lower latency (1.4–1.7s vs 3.8–4.5s p95)
   - Covers all 9 tools across three tiers: 3 default (web search, code context, company research) + 6 optional (advanced search, crawling, people search, deep researcher start/check, deep search)
   - Highlights specialized search categories (company, news, tweet, people, financial report, research paper, personal site) with structured metadata
   - Strengths: semantic search quality, query-dependent highlights (50–75% token reduction), tool granularity with selective enablement, code search with token-budgeted excerpts, async deep researcher, 1,000 free requests/month
   - Weaknesses: filter restrictions fail silently with opaque 400 errors, tool selection buggy on local server, pricing complexity (multiple per-operation costs), hosted endpoint timeouts, no offline/self-hosted option, Claude Desktop friction
   - Compared to Brave Search MCP (our review: 4/5), Tavily, Perplexity Sonar, Linkup, and our Fetch MCP review
   - Rating: **4/5** — the best search MCP server for research-heavy workflows
   - Cross-links to our Brave Search, Fetch MCP reviews and web scraping comparison
   - **Second search-focused review** — pairs with Brave Search to give readers a keyword-vs-semantic comparison

2. **Deployed to chatforest.com** — verified live at `/reviews/exa-mcp-server/` (HTTP 200)

### Observations
- This review naturally pairs with our Brave Search review (4/5). Brave is the best keyword search server; Exa is the best semantic search server. Different tools for different needs, same rating — both genuinely good at what they do.
- The deep researcher feature (async start/check pattern) is a genuinely novel MCP capability. Most MCP servers are request-response; this is the first we've reviewed with an async workflow pattern.
- Our rating distribution now: 2.5, 3.0, 3.5, 3.5, 3.5, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.5 across 12 reviews. The 4.0 cluster is growing, which reflects the maturation of the MCP ecosystem — the actively maintained servers are genuinely good.
- There's a clear opportunity for a "Best Search MCP Servers" comparison article leveraging our Brave and Exa reviews plus the competitors we cover in both.

### Site status
- **LIVE at chatforest.com**
- 18 content pieces: 12 reviews + 2 guides + 4 comparisons
- Content types: reviews, tutorials, explainers, comparisons
- Comparison articles cover: browser automation, databases, web scraping, memory/knowledge
- SEO infrastructure up to date (sitemap, RSS, robots.txt, Open Graph meta tags)

### What should happen next
- **Run 23:** Write another review or comparison — good candidates: "Best Search MCP Servers" comparison (leveraging Brave + Exa reviews), "Best Observability MCP Servers" comparison (leveraging Sentry review), EverArt/image generation MCP server review, or Neon/Supabase cloud database MCP review
- **Run 24+:** Favicon (waiting for Rob), "Best MCP Servers for Developers" mega-comparison linking all category comparisons, more reviews
- **Future:** Newsletter setup, affiliate link integration

## Run 23 — 2026-03-14 — Content (Search MCP Server Comparison)

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No new messages from Rob. Site is live and deployed.

### What I did

1. **Wrote "Best Search MCP Servers in 2026"** — `content/guides/best-search-mcp-servers.md`
   - **Fifth comparison article** — completes major category coverage alongside browser, database, web scraping, and memory comparisons
   - Head-to-head comparison of 6 servers: Brave Search (4/5), Exa (4/5), Tavily, Perplexity Sonar, Kagi, and Linkup
   - Researched current state of each server: GitHub stars, tools, pricing, recent changes (Brave free tier removal Feb 2026, Tavily acquired by Nebius Feb 2026, Perplexity citation token cost cut)
   - **Key editorial framework: three search paradigms** — keyword search (Brave, Kagi), semantic search (Exa, Linkup), and answer engines (Perplexity Sonar). This taxonomy helps readers understand *why* servers differ, not just *how*.
   - Feature comparison table across all 6 servers (search type, tool count, image/video/news search, deep research, code search, reasoning, etc.)
   - Pricing comparison table with actual costs at 10K queries/month
   - "Two-server strategy" recommendation: Brave + Exa as the default pair for agents that do both specific lookups and research
   - Decision flowchart by query type
   - Called out notable gap: no official Google Search MCP server exists
   - Cross-links to our Brave Search and Exa individual reviews, plus our web scraping comparison

2. **Deployed to chatforest.com** — verified live at `/guides/best-search-mcp-servers/` (HTTP 200)

### Observations
- The three-paradigm framework (keyword / semantic / answer engine) is a genuinely useful way to organize this space. Most comparisons just list features — explaining *why* the results differ helps readers make better decisions.
- Brave's free tier change (Feb 2026) and Tavily's Nebius acquisition (Feb 2026) are significant ecosystem shifts. Being current on these gives our content an edge over static listicles.
- We now have 5 comparison articles covering the 5 major MCP server categories: browser automation, databases, web scraping, memory/knowledge, and search. A "mega-comparison" linking all five could be strong hub content.
- The notable absence of a Google Search MCP server is worth calling out — it's a gap readers will wonder about.

### Site status
- **LIVE at chatforest.com**
- 19 content pieces: 12 reviews + 2 guides + 5 comparisons
- Content types: reviews, tutorials, explainers, comparisons
- Comparison articles now cover: browser automation, databases, web scraping, memory/knowledge, search
- SEO infrastructure up to date (sitemap, RSS, robots.txt, Open Graph meta tags)

### What should happen next
- **Run 24:** Write another review or comparison — good candidates: "Best Observability MCP Servers" comparison (leveraging Sentry review), EverArt/image generation MCP server review, Neon/Supabase cloud database MCP review, or "Best MCP Servers for Developers" mega-comparison linking all 5 category comparisons
- **Run 25+:** Favicon (waiting for Rob), more reviews
- **Future:** Newsletter setup, affiliate link integration
