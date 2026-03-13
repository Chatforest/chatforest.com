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
