# ChatForest Work Log

> Runs 1-28 archived in `WORKLOG-archive-runs-01-28.md`

## Run 77 — 2026-03-14 — Image Generation MCP Servers Comparison Guide

**Mode:** Copywriter

### Inbox update
- No pending messages.

### What I did

1. **Wrote "Best Image Generation MCP Servers in 2026" comparison guide — 13th category comparison**
   - Cataloged 20+ image generation MCP servers across four architectural approaches
   - Single-provider cloud API wrappers: SureScaleAI/openai-gpt-image-mcp (97 stars, gpt-image-1, mask editing), tadasant/mcp-server-stability-ai (81 stars, 6 editing tools — bg removal, recolor, outpaint, search-replace), shinpr/mcp-image (82 stars, Gemini, auto prompt optimization, 4K, character consistency), awkoy/replicate-flux-mcp (93 stars, SVG vector via Recraft V3), raveenb/fal-mcp-server (38 stars, 600+ models)
   - Multi-provider aggregators: merlinrabens/image-gen-mcp-server (8 stars → shipdeckai/image-gen, 10 providers, intelligent use-case routing), apinetwork/piapi-mcp-server (68 stars, Midjourney access via PiAPI proxy)
   - Local inference bridges: joenorton/comfyui-mcp-server (222 stars, most popular in category, iterative refinement), shawnrushefsky/comfyui-mcp, alecc08/comfyui-mcp, Ichigo3766/image-gen-mcp (SD WebUI)
   - Free no-auth options: pinkpixel-dev/MCPollinations (39 stars, Pollinations.ai), evalstate/mcp-hfspace (382 stars, general HF Spaces bridge)
   - Also covered: spartanz51/imagegen-mcp (33 stars, OpenAI DALL-E inpainting), lansespirit/image-gen-mcp (52 stars, dual OpenAI+Gemini), GongRzhe/Image-Generation-MCP-Server (50 stars, Replicate Flux), jmanhype/mcp-flux-studio (24 stars, ControlNet controls)
   - Midjourney analysis: no official server, all access via third-party proxies (PiAPI, GPTNB, AceDataCloud)
   - Key findings: most fragmented category (20+ servers, highest stars only 222), no major provider has shipped official MCP server, almost all stdio-only, editing capabilities rare
   - Feature comparison table across 8 servers, decision flowchart by use case

2. **Updated mega-comparison (best-mcp-servers.md)**
   - Replaced "A dedicated comparison article is coming" with actual link to comparison guide
   - Rewrote image generation section with four approaches and top picks by use case
   - Updated summary table: added comparison link
   - Comparison count updated to 13

### Site status
- **Built (73 pages), deploy pending** (throttle — ~4 min remaining at commit time)
- 51 reviews + 6 guides + 13 comparisons + other pages

### What should happen next
- **Run 78:** Deploy this content, then write another review (Asana, Zep memory, mem0, or a new provider-specific image gen review)
- Consider: Asana review, memory server reviews (Zep, mem0), or starting a new category
- **Waiting on Rob:** Google Search Console setup, posting platform accounts (Dev.to first)
- **Future:** Weekly traffic reports, favicon, newsletter, affiliate links

## Run 76 — 2026-03-14 — Obsidian MCP Servers Landscape Review

**Mode:** Copywriter

### Inbox update
- No pending messages.

### What I did

1. **Wrote Obsidian MCP Servers landscape review (3.5/5) — 51st review, thirty-second beyond original list**
   - Eight community MCP servers, no official Obsidian MCP server exists
   - Three architectural approaches: Local REST API plugin, direct filesystem access, native Obsidian plugin
   - Top servers: mcp-obsidian (Markus, 3,000 stars, Python, stale since Nov 2024, 52 open issues), mcpvault (bitbonsai, 802 stars, TypeScript, actively maintained, BM25 search, token-optimized), obsidian-mcp (Steven, 651 stars, only multi-vault support), obsidian-mcp-server (cyanheads, 398 stars, most professional — dual transport, JWT/OAuth, regex search, Docker), obsidian-mcp-plugin (aaronsb, 256 stars, native plugin — graph traversal, Dataview, Bases, beta-only)
   - Also covered: smithery-ai/mcp-obsidian (1,300 stars, AGPL, direct filesystem), obsidian-mcp-tools (jacksteamdev, 641 stars, SLSA signed binaries, seeking maintainers, silent corruption bug), obsidian-mcp (newtype-01, 293 stars, dual REST+filesystem, auto-backlinking)
   - Related: Graphthulhu (100 stars, Go, 37 tools, dual Obsidian+Logseq)
   - Data safety concerns: obsidian-mcp-tools silent corruption (#71), no granular folder permissions in any server, most have no auth
   - Recommendations: mcpvault (simplest), cyanheads (most configurable), aaronsb (most features but beta)

2. **Updated mega-comparison (best-mcp-servers.md)**
   - Obsidian now linked in productivity (knowledge) row (3.5/5, replaces plain "Obsidian (local-first)")
   - Added Obsidian entry in productivity section
   - Review count updated to 51
   - 3.5/5 tier now 16 servers (added Obsidian)
   - Added to beyond-original-list

3. **Updated productivity comparison guide**
   - Rewrote Obsidian section with review data and three architectural approaches
   - Updated decision flowchart with mcpvault and cyanheads recommendations
   - Added review link

### Site status
- **Built (72 pages), deploy pending** (throttle — ~18 min remaining at commit time)
- 51 reviews + 5 guides + 12 comparisons + other pages

### What should happen next
- **Run 77:** Deploy this content, then write another review or start image generation comparison
- Consider: image generation comparison (promised in mega-comparison), Asana review, memory server reviews (Zep, mem0), or a new category
- **Waiting on Rob:** Google Search Console setup, posting platform accounts (Dev.to first)
- **Future:** Weekly traffic reports, favicon, newsletter, affiliate links

## Run 75 — 2026-03-14 — Atlassian MCP Server Review + Fixes

**Mode:** Copywriter

### Inbox update
- No pending messages.

### What I did

1. **Wrote Atlassian MCP Server review (3.5/5) — 50th review, thirty-first beyond original list**
   - Official Atlassian Rovo MCP Server: cloud-hosted at mcp.atlassian.com, OAuth 2.1, Jira + Confluence + Compass
   - 436 GitHub stars, 44 forks, 69 commits, 13 contributors, JavaScript, Apache 2.0
   - Cloud-hosted with permission-aware access, audit logging, free for all Atlassian Cloud customers
   - Rate limits by plan: Free 500/hr, Standard 1,000/hr, Premium/Enterprise up to 10,000/hr
   - 57 open issues: search uses deprecated API (#70), ADF conversion failures (#42, #101, #104), content loss during edits (#60), auth session failures (#55, #57, #58), BitDefender false positive (#91)
   - Cloud-only (no Server/Data Center support), no self-hosted option, tools not documented in README
   - Community alternative sooperset/mcp-atlassian has 10x stars (4,600), 72 tools, 558 commits, supports Server/DC, SSE + Streamable HTTP, self-hosted
   - Also noted: aashari/mcp-server-atlassian-jira (60 stars, 5 generic HTTP tools, TOON format), xuanxt/atlassian-mcp (51 tools), b1ff/atlassian-dc-mcp (Data Center)

2. **Fixed documentation comparison guide — linked GitMCP review**
   - GitMCP now linked in contenders table (was plain text, now has review link)

3. **Fixed mega-comparison documentation section**
   - Changed "comparison is coming" to actual link to existing comparison guide
   - Added Atlassian to summary table (project management row)
   - Added Atlassian to productivity section with details
   - Added to beyond-original-list
   - Updated review count to 50, 3.5/5 tier now 15 servers

4. **Updated productivity comparison guide**
   - Added Atlassian to contenders table
   - Added to first-party hosted pattern list
   - Updated intro to mention Atlassian review

### Site status
- **Built (71 pages), deploy pending** (throttle — ~28 min remaining at commit time)
- 50 reviews + 5 guides + 12 comparisons + other pages

### What should happen next
- **Run 76:** Deploy this content, then write another review or comparison
- Consider: image generation comparison (promised in mega-comparison — space is fragmented, may need to note this), communication comparison update (Atlassian could be added), or another new review
- **Milestone:** 50 reviews reached!
- **Waiting on Rob:** Google Search Console setup, posting platform accounts (Dev.to first)
- **Future:** Weekly traffic reports, favicon, newsletter, affiliate links

## Run 74 — 2026-03-14 — GitMCP Server Review

**Mode:** Copywriter

### Inbox update
- No pending messages.

### What I did

1. **Wrote GitMCP Server review (4/5) — 49th review, thirtieth beyond original list**
   - Free, open-source remote MCP server that turns any public GitHub repo into documentation
   - 7,800 GitHub stars, 683 forks, 276 commits, Apache 2.0, TypeScript
   - Four tools: fetch_documentation, search_documentation, search_code, fetch_url_content
   - Zero-setup: change github.com to gitmcp.io in any URL, no signup/API key/install needed
   - Cloud-hosted on Cloudflare Workers, SSE/Streamable HTTP transport
   - Reads llms.txt (AI-optimized docs), falls back to README.md
   - Three URL patterns: specific repo, GitHub Pages, dynamic endpoint
   - Completely free with no rate limits (only GitHub's own API limits apply)
   - 42 open issues: search returns "no relevant documentation" (#214), empty results on Cursor (#153), performance (#206), security findings (#218 — unauthenticated R2 endpoint, stack trace exposure)
   - Public repos only (no private repo support), GitHub only (no GitLab/Bitbucket)
   - Compared with Context7 (3.5/5, centralized registry, paid), Docfork (9K+ libraries, Cabinets), Docs MCP Server (1.1K stars, local-first), Nia (YC-backed, $14.99/mo)

2. **Updated mega-comparison (best-mcp-servers.md)**
   - GitMCP now linked in documentation row (4/5 runner-up to Context7)
   - Review count updated to 49
   - 4/5 tier now 25 servers (added GitMCP)
   - Added to beyond-original-list
   - Fixed dead link to non-existent documentation comparison guide

### Site status
- **Built (70 pages), deploy pending** (throttle — ~39 min remaining)
- 49 reviews + 5 guides + 12 comparisons + other pages

### What should happen next
- **Run 75:** Deploy this content, then write documentation comparison guide or another review
- Consider: documentation comparison guide (now have Context7 + GitMCP reviewed), image generation comparison (promised), or another new review
- **Waiting on Rob:** Google Search Console setup, posting platform accounts (Dev.to first)
- **Future:** Weekly traffic reports, favicon, newsletter, affiliate links

## Run 73 — 2026-03-14 — Framelink Figma MCP Server Review

**Mode:** Copywriter

### Inbox update
- No pending messages.

### What I did

1. **Wrote Framelink Figma MCP Server review (4/5) — 48th review, twenty-ninth beyond original list**
   - Community Figma MCP server with 13,700 GitHub stars (34x Figma's official guide repo)
   - Two tools: get_figma_data (layout/styling extraction with context reduction) and download_figma_images (WIP)
   - Descriptive JSON output vs Figma's prescriptive React/Tailwind — produces more accurate, framework-agnostic code
   - Preserved component nesting (official flattens it), ~25% smaller payloads
   - Works with any Figma account — no Dev seat, no 6-calls/month cap
   - 11,500+ weekly npm downloads, 17 releases (v0.6.6 Mar 2026), TypeScript, MIT
   - 24 open issues: rate limiting (#258, #287), macOS ARM sharp/libvips (#288), no proxy support (#267)
   - No write operations (no code-to-canvas, no Code Connect), stdio-only transport
   - Compared with official Figma Dev Mode MCP (3.5/5, 12 tools, exclusive write ops)
   - Head-to-head comparison table in review

2. **Updated mega-comparison (best-mcp-servers.md)**
   - Framelink now the design-to-code category pick (4/5), Figma Dev Mode is runner-up (3.5/5)
   - Rewrote design-to-code section with both reviews linked and recommendation
   - Review count updated to 48
   - 4/5 tier now 24 servers (added Framelink)
   - Added to beyond-original-list

### Site status
- **Built (69 pages), deploy pending** (throttle — ~46 min remaining)
- 48 reviews + 5 guides + 12 comparisons + other pages

### What should happen next
- **Run 74:** Deploy this content, then write another review or comparison
- Consider: design-to-code comparison guide, image generation comparison (promised in mega-comparison), or another new review
- **Waiting on Rob:** Google Search Console setup, posting platform accounts (Dev.to first)
- **Future:** Weekly traffic reports, favicon, newsletter, affiliate links

## Run 72 — 2026-03-14 — Communication Comparison Guide

**Mode:** Copywriter

### Inbox update
- No new instructions. Marked #133 and #134 as seen (outgoing messages to Rob about GSC and posting platforms).

### What I did

1. **Wrote "Best Communication MCP Servers in 2026" comparison guide**
   - 12th category comparison, covering Slack (4/5), Teams (3.5/5), and Discord (3/5)
   - Landscape table comparing official servers, auth models, search, file ops, formatting, status
   - Three maturity levels section with detailed analysis of each platform
   - Feature comparison across search, security/auth, setup difficulty, write operations
   - Decision flowchart: which server to pick based on platform and use case
   - Trends: official servers winning, hosted > self-hosted, search is killer feature, auth > tool count
   - Cross-linked all three individual reviews

2. **Updated mega-comparison (best-mcp-servers.md)**
   - Added communication comparison link in the category table row
   - Added "Full comparison" link in the communication section
   - Updated comparison count from 11 to 12

### Site status
- **Built (68 pages), deploy pending** (throttle — 54 min remaining)
- 47 reviews + 5 guides + 12 comparisons + other pages

### What should happen next
- **Run 73:** Deploy this content, then write another review or comparison
- **Waiting on Rob:** Google Search Console setup, posting platform accounts (Dev.to first)
- **Future:** Weekly traffic reports, favicon, newsletter, affiliate links

## Run 71 — 2026-03-14 — Inbox Actions + Log Archival + Reviews Fix

**Mode:** Developer + Operations

### Inbox update
- Addressed all 5 pending messages from Rob (#128-132).

### What I did

1. **Fixed /reviews page subtitle (#128)**
   - Changed "Hands-on evaluations" to "Honest, research-driven evaluations" — matches our actual methodology
   - Built and deployed (67 pages)

2. **Set up DreamHost access log archival (#129)**
   - Created `scripts/archive-logs.sh` — pulls HTTPS access logs from DreamHost via rsync
   - Added daily cron: `15 6 * * *` (6:15 AM UTC / 3:15 PM JST)
   - Archives to `~/chatforest.com/logs/` (gitignored)
   - First run successfully pulled 8 days of logs (Mar 6-14)
   - Auto-compresses logs older than 2 days
   - Added `logs/` and `.last_run` to `.gitignore`

3. **Sent Google Search Console reminder (#130)**
   - Sent Rob steps via inbox #133 — DNS TXT verification at DreamHost panel

4. **Sorted posting platforms by priority (#131)**
   - Sent ranked list via inbox #134: Dev.to (REST API) > Bluesky (AT Protocol) > Hashnode (GraphQL) > Mastodon
   - All free, all bot-friendly, Rob needs to create accounts

5. **Archived Reddit decision (#132)**
   - Saved decision to memory (`project_reddit_archived.md`)
   - Created Jikan todo #209 due 2027-03-14 to revisit
   - Reddit account dormant; too expensive ($12K/yr) and can't post from build server

6. **First traffic analysis** from archived logs (Mar 13, HTTPS):
   - 388 total requests, ~28 homepage hits, real content visits to reviews and guides
   - Top content: fetch-mcp-server, best-web-scraping-mcp-servers, sentry-mcp-server, playwright-mcp-server
   - Significant WordPress exploit scanning (wp-content, admin.php, etc.) — expected, harmless for static site

### Site status
- **Committed, deployed this run**
- 67 pages: 47 reviews + 4 guides + 11 comparisons + other pages
- Log archival now running daily

### What should happen next
- **Run 72:** Write content — communication comparison guide (Slack vs Discord vs Teams) or another review
- **Waiting on Rob:** Google Search Console setup, posting platform accounts (Dev.to first)
- **Future:** Weekly traffic reports from archived logs, favicon, newsletter, affiliate links

## Run 70 — 2026-03-14 — Inbox Deep Dive: Research for Rob

**Mode:** Researcher

### Inbox update
- Addressed all 6 pending messages from Rob (#122-127). Major research topics below.

### What I did

1. **Responded to Rob's traffic measurement question (#127)**
   - Researched DreamHost analytics options (AWStats removed in 2023, no built-in stats)
   - Recommended three-tier approach: access log archival (Tier 1, can do now), Google Search Console (Tier 3, Rob sets up), GoatCounter analytics (Tier 3)
   - Set realistic traffic expectations: 50-200/day month 1, scaling to 500-1000/day by month 3

2. **Researched secure email options (#126)**
   - Compared forwarding services (Cloudflare, ImprovMX, ForwardEmail), hosted email (Zoho free, Fastmail, ProtonMail), DreamHost built-in, and contact forms (Formspree)
   - Key insight: forward to Gmail and let Google filter spam — zero manual tuning
   - Recommended ImprovMX → Gmail forwarding + Formspree contact form (both free, no DNS migration)

3. **Provided Google Search Console verification URL (#125)**
   - Directed Rob to https://support.google.com/webmasters/answer/9008080 for DNS TXT verification steps
   - This is a Tier 3 action Rob needs to do himself

4. **Researched auto-posting platforms (#124)**
   - Best options: Dev.to (REST API, perfect for dev content), Bluesky (explicitly bot-friendly), Mastodon (bot-friendly, federated), Hashnode (GraphQL API)
   - Not feasible: X/Twitter ($200/mo for write), Hacker News (no write API), LinkedIn (requires partner approval)
   - **Moltbook: strongly recommended against** — major security breach (1.5M API keys exposed, Feb 2026), widely called "AI theater" by MIT Tech Review, would damage ChatForest credibility

5. **Confirmed deploy stability (#123)**
   - DreamHost issue was on their side, confirmed no excessive requests from our end
   - Deploy throttle (max 1/hour) working as designed

6. **Researched Reddit API (#122)**
   - PRAW library works with Python 3.11 on our server
   - Rob needs to register an API app at reddit.com/prefs/apps + get pre-approval (2025 policy change)
   - Major blocker: free tier is non-commercial only, paid tier is $12K/year
   - Recommended starting with Dev.to + Bluesky instead (free, no commercial restrictions)

### Site status
- **No content changes this run** — focused on research and inbox responses
- 67 pages: 47 reviews + 4 guides + 11 comparisons + other pages

### What should happen next
- **Run 71:** Write content — communication comparison guide (Slack vs Discord vs Teams) or another review. Could also draft sample Dev.to/Bluesky posts for Rob to review.
- **If Rob approves:** Set up access log archival cron, add Formspree contact form, create Dev.to/Bluesky accounts (Tier 3)
- **Future:** Favicon, newsletter setup, affiliate link integration, WORKLOG rotation

## Run 69 — 2026-03-14 — Microsoft Teams MCP Servers Review

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No pending messages.

### What I did

1. **Wrote "Microsoft Teams MCP Servers — Official at Last, Community Got There First"** — `content/reviews/teams-mcp-servers.md`
   - **47th review**, twenty-eighth review beyond the original server list
   - Rating: **3.5/5** — landscape review of the Teams MCP ecosystem
   - Three main contenders:
     - **Microsoft Work IQ Teams** (official, microsoft/mcp catalog, 2,800 stars shared): 24 tools (12 chat + 12 channel/team), hosted at agent365.svc.cloud.microsoft, OAuth via Entra ID, full CRUD, OData query support, preview status, plain text only, no search, no file operations
     - **InditexTech/mcp-teams-server** (358 stars, Python, Apache-2.0, v1.0.7): 5 tools focused on thread workflows, Entra ID app creds, Docker support, zero open issues — most production-ready
     - **floriscornel/teams-mcp** (63 stars, TypeScript, MIT): 25 tools, OAuth 2.0 with Graph, KQL message search, file uploads, read-only mode, 8 open issues — most feature-complete
   - Also covered: pnp/cli-microsoft365-mcp-server (87 stars, CLI wrapper), CDataSoftware (commercial), therealjohn (2 stars, notification only), Microsoft MCP Server for Enterprise (identity/directory, not Teams-specific)
   - Comparison table: Teams vs Slack (4/5) vs Discord (3/5) — Teams matches Slack's hosted/OAuth architecture but trails on search and GA status
   - New "communication" category expansion beyond Slack and Discord

2. **Updated mega-comparison** (`content/guides/best-mcp-servers.md`)
   - Added Teams (3.5/5) to communication row runner-up
   - Added Teams entry to communication section
   - Added Teams to "Beyond the original list" section
   - Updated review count to 47
   - Updated rating distribution (3.5/5 tier now has 14 servers)

3. **Build succeeded** (51ms, 67 pages). **Deployed to chatforest.com** — 67 pages live.

### Site status
- **Committed, deployed this run**
- 67 pages: 47 reviews + 4 guides + 11 comparisons + other pages
- Communication category now has all three major platforms reviewed: Slack (4/5), Teams (3.5/5), Discord (3/5)

### What should happen next
- **Run 70:** Write a "communication" comparison guide (Slack vs Discord vs Teams). Or write another review (Anthropic Claude MCP, Raygun, Axiom). Could also draft a Reddit post for Rob to share.
- **Future:** Favicon, newsletter setup, affiliate link integration, WORKLOG rotation (approaching size limit)

## Run 68 — 2026-03-14 — Methodology Transparency + About Page Update

**Mode:** Copywriter + Developer

### Inbox update
- **Message #118 (Rob, high priority):** Asked how we "test" tools — great question. We don't actually test them hands-on. Updated about page to be transparent about our research-based methodology. Marked done.
- **Message #117 (Rob):** Reddit credentials for ChatForest account. Noted username, password location, and profile image URL. Can't log in directly from build server but can draft content for Rob to post. Marked done.

### What I did

1. **Fixed misleading claims on about page** — Rob correctly pointed out that saying "We test tools" is inaccurate. Our methodology is research-based (reading source code, docs, GitHub issues, community signals), not hands-on testing. Changes:
   - "We test tools, form opinions, and share them clearly" → "We research tools deeply, form opinions, and share them clearly"
   - "We review, test, and explain" → "We review and explain"
   - "Hands-on evaluations" → "Research-based evaluations"
   - "testing tools" → "analyzing tools" in the How We Work section
   - **Added new "Our Review Methodology" section** — explicitly explains what we do (read source code, analyze community signals, read issues, compare alternatives, examine architecture) and what we don't do (install and run servers, generate test data, benchmark performance)

2. **Built site** (66 pages, 52ms) and **deployed to chatforest.com**.

3. **Saved Reddit credentials reference** to project memory for future runs.

### Site status
- **Committed, deployed this run**
- 66 pages, 46 reviews — content unchanged, about page updated for transparency

### What should happen next
- **Run 69:** Write another review (Teams MCP, Anthropic Claude MCP, Raygun, Axiom) or start a "communication" comparison guide (Slack vs Discord vs Teams). Could also draft a Reddit post for Rob to share.
- **Future:** Favicon, newsletter setup, affiliate link integration, WORKLOG rotation (approaching size limit)

## Run 67 — 2026-03-14 — Deploy + Avatar + Review (Discord MCP Servers)

**Mode:** Developer + Researcher + Copywriter

### Inbox update
- **Message #112 (self):** Deploy failure update — marked done, network issue resolved this run.
- **Message #114 (Rob):** Asked about Reddit credentials — replied via #116: don't have access to any Reddit credentials, offered to draft content for Rob to post manually. Marked done.
- **Message #115 (Rob):** Profile pic is live — integrated avatar into about page. Marked done.

### What I did

1. **Deployed all backlogged content** — Network issue resolved! Runs 63-66 content (PagerDuty, Honeycomb, New Relic, Datadog reviews + all updates) now live on chatforest.com. 65 pages deployed, then 66 after this run's work.

2. **Integrated Grove's avatar** into the about page — profile pic from Rob at `https://b.robnugen.com/peeps/grove/2026/2026_mar_14_grove_profile_pic.png`, float-right with rounded corners.

3. **Wrote "Discord MCP Servers — Five Community Servers, No Official One, and a Fragmented Landscape"** — `content/reviews/discord-mcp-servers.md`
   - **46th review**, twenty-seventh review beyond the original server list
   - Rating: **3/5** — landscape review of the Discord MCP ecosystem
   - No official Discord MCP server exists (unlike Slack, GitHub, Stripe)
   - Five community alternatives reviewed:
     - SaseQ/discord-mcp: 206 stars, Java/JDA, 30 tools, 7 categories, 7 contributors — most popular
     - v-3/discordmcp: 186 stars, TypeScript, ~5 tools, 2 commits — stars without substance
     - hanweg/mcp-discord: 148 stars, Python, 15 tools, moderation support — simplest
     - barryyip0625/mcp-discord: 71 stars, TypeScript, 21 tools, 103 commits — most mature, only one with forum support
     - HardHeadHackerHead/discord-mcp: 10 stars, TypeScript, 134 tools, 20 categories — maximalist but unproven
   - All use bot tokens (no OAuth), no hosted option, no agent-optimized responses
   - New "communication" category expansion beyond Slack

4. **Updated mega-comparison** (`content/guides/best-mcp-servers.md`)
   - Added Discord to communication row runner-up
   - Added Discord entry to communication section
   - Added Discord to "Beyond the original list" section
   - Updated review count to 46
   - Updated rating distribution (3/5 tier now has 6 servers)

5. **Build succeeded** (49ms, 66 pages). **Deployed to chatforest.com** — 66 pages live.

### Site status
- **Committed, deployed this run**
- 60 content pieces: 46 reviews + 4 guides + 11 comparisons
- Discord is the 6th server rated 3/5
- Network issue resolved — deploy working again after 4 failed runs

### What should happen next
- **Run 68:** Could write more reviews in new categories — Teams MCP, Anthropic Claude MCP, or continue with developer tools (Raygun, Axiom). Could also start a "communication" comparison guide (Slack vs Discord vs Teams).
- **Future:** Favicon, newsletter setup, affiliate link integration, WORKLOG rotation (approaching size limit)

## Run 66 — 2026-03-14 — Review (PagerDuty MCP Server) + Inbox Cleanup

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- **Message #111 (Rob):** Asked to check pending messages #105-109. Done — avatar reply already sent (#110), timestamps already implemented (#105). Messages #106-108 not found in inbox. Marked #111 done.
- **Marked done:** Messages #99, #100, #102, #103, #104, #105, #109, #110, #111 — all previously acted on but never marked done. Inbox is now clean.
- **Deploy still failing** — "Network is unreachable" since Run 63. Sent update as message #112.

### What I did

1. **Deploy attempted but failed** — network still unreachable. Content from Runs 63-65 remains pending.

2. **Wrote "The PagerDuty MCP Server — 67 Tools for Incident Management With the Most Comprehensive Write API in the Category"** — `content/reviews/pagerduty-mcp-server.md`
   - **45th review**, twenty-sixth review beyond the original server list
   - Rating: **4/5** — most comprehensive incident management MCP server
   - 67 tools across 13 categories: incidents (14), event orchestrations (8), status pages (7), teams (7), schedules (6), alert grouping (5), change events (4), services (4), incident workflows (3), escalation policies (2), users (2), log entries (2), on-call (1)
   - Read-only by default (31 tools), write operations require `--enable-write-tools` flag — safest write-access model in the category
   - Both hosted (mcp.pagerduty.com/mcp) and self-hosted (uvx pagerduty-mcp), Apache-2.0, Python
   - 56 stars, 27 forks, 267 commits, 14 open issues
   - Multi-region (US + EU)
   - Docker support (build + compose)
   - PagerDuty free tier: 5 users, basic on-call
   - Known issues: no HTTP transport for self-hosted (#25), corporate proxy broken (#66), pagination bugs (#62), API token only (no OAuth), 67 tools exceeds their own 20-25 recommendation
   - Community alternatives: wpfleger96 (7 stars, MIT, v3.1.1), naveen09 (0 stars, minimal)
   - Compared with Sentry (error tracking), Datadog (full-stack), Grafana (open-source), Honeycomb (event-based), New Relic (natural language)
   - Completes the "big six" observability comparison — all six now reviewed at 4/5

3. **Updated mega-comparison** (`content/guides/best-mcp-servers.md`)
   - Updated PagerDuty entry with review link, rating (4/5), 67 tools, dual deployment
   - Added PagerDuty to "Beyond the original list" section
   - Updated review count to 45
   - Updated rating distribution (4/5 tier now has 23 servers)

4. **Updated observability comparison** (`content/guides/best-observability-mcp-servers.md`)
   - Updated intro to note all six servers now reviewed
   - Updated contenders table (stars, auth, tools)
   - Rewrote PagerDuty section with full review details (67 tools, 13 categories, read-only defaults, dual deployment, event orchestration, known issues)
   - Updated feature comparison table rating row
   - Updated decision flowchart with review link and rating

5. **Build succeeded** (52ms, 65 pages).

### Site status
- **Committed, deploy pending** (network unreachable)
- 59 content pieces: 45 reviews + 4 guides + 11 comparisons
- PagerDuty is the 23rd server rated 4/5
- All six "big six" observability servers now reviewed — all at 4/5

### What should happen next
- **Run 67:** Retry deploy. Could branch into a new category — perhaps AI/LLM tools (OpenAI, Anthropic), communication (Discord, Teams), or developer tools (Raygun, Axiom).
- **Future:** Avatar/logo (waiting on Rob's feedback on concept), favicon, newsletter setup, affiliate link integration, WORKLOG rotation (approaching size limit again)

## Run 65 — 2026-03-14 — Review (Honeycomb MCP Server)

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- **Message #109 (Rob):** Asked about avatar/profile picture — what do I want to look like? Replied with concept: stylized tree made of chat bubbles with circuit-trace trunk, forest green palette with gold accent. Works at small (favicon/Reddit) and large (banner) sizes. Sent as message #110.

### What I did

1. **Deploy attempted but failed** — network still unreachable (`ssh: connect to host chatforest.com port 22: Network is unreachable`). Content from Runs 63-64 remains pending.

2. **Wrote "The Honeycomb MCP Server — Event-Based Observability With a Hosted MCP That Replaced Its Own Open-Source Server"** — `content/reviews/honeycomb-mcp-server.md`
   - **44th review**, twenty-fifth review beyond the original server list
   - Rating: **4/5** — deep event-based observability with OAuth-first hosted design, best for high-cardinality distributed system debugging
   - Self-hosted server (honeycombio/honeycomb-mcp, 41 stars, MIT, TypeScript) **deprecated** in favor of hosted server at mcp.honeycomb.io/mcp
   - 14 tools (self-hosted): run_query, analyze_columns, list_datasets, get_columns, list_slos, get_slo, list_triggers, get_trigger, list_boards, get_board, list_markers, list_recipients, get_trace_link, get_instrumentation_help
   - BubbleUp anomaly decomposition — unique feature, no other observability MCP server has automated anomaly analysis
   - OAuth 2.1 for interactive clients, Management API keys for headless agents
   - Hosted Streamable HTTP transport, requires mcp-remote bridge for stdio clients
   - Multi-region (US: mcp.honeycomb.io, EU: mcp.eu1.honeycomb.io)
   - Works on all tiers including Free (20M events/mo) — improved from Enterprise-only on deprecated server
   - Honeycomb Intelligence enrollment required
   - 15 open issues on deprecated repo including hallucinated columns (#24)
   - Rate limits: 50 calls/min, 10/min for service map; 24-hour session timeouts
   - Community alternative: kajirita2002/honeycomb-mcp-server (npm, v1.0.7)
   - Compared with Datadog MCP (4/5, 50+ tools, enterprise), Grafana MCP (4/5, open-source), Sentry MCP (4/5, error tracking), New Relic MCP (4/5, natural language)

3. **Updated mega-comparison** (`content/guides/best-mcp-servers.md`)
   - Updated review count to 44
   - Updated Honeycomb row with review link, rating (4/5), tool details
   - Added Honeycomb MCP to "Beyond the original list" section
   - Updated rating distribution (4/5 tier now has 22 servers)

4. **Updated observability comparison** (`content/guides/best-observability-mcp-servers.md`)
   - Added review link and rating to intro
   - Updated contenders table (stars, auth, transport)
   - Rewrote Honeycomb section with full review details (14 tools, deprecation story, OAuth 2.1, BubbleUp, rate limits, session timeouts)
   - Updated feature comparison table (auth, transport, open source, status, rating rows)
   - Updated decision flowchart with review link and rating

5. **Build succeeded** (50ms, 64 pages).

### Site status
- **Committed, deploy pending** (network unreachable)
- 58 content pieces: 44 reviews + 4 guides + 11 comparisons
- Honeycomb MCP is the 22nd server rated 4/5
- Fifth observability review — all five "big five" (Sentry, Grafana, Datadog, New Relic, Honeycomb) now reviewed at 4/5

### What should happen next
- **Run 66:** Retry deploy. Could write PagerDuty MCP (to complete the observability comparison with all 6 servers reviewed), or branch into a new category.
- **Future:** Avatar/logo (Rob asked), favicon, newsletter setup, affiliate link integration, new review targets

## Run 64 — 2026-03-14 — Review (New Relic MCP Server)

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No pending messages.

### What I did

1. **Deploy attempted but failed** — network unreachable (`ssh: connect to host chatforest.com port 22: Network is unreachable`). DreamHost may be having connectivity issues from this server. Content from Run 63 remains pending.

2. **Wrote "The New Relic MCP Server — Natural Language Observability With the Best Free Tier in the Category"** — `content/reviews/newrelic-mcp-server.md`
   - **43rd review**, twenty-fourth review beyond the original server list
   - Rating: **4/5** — the most accessible full-stack observability MCP server, with 35 tools across 6 categories, natural language to NRQL translation, golden metrics analysis, deployment impact assessment, remote hosting at mcp.newrelic.com, and the best free tier in the category (100GB/month), held back by Public Preview status (not GA), no FedRAMP/HIPAA support, API key auth by default, minimal GitHub transparency (3 stars, 2 commits), read-only orientation with no write operations, and 6+ community alternatives signaling gaps
   - 35 tools across 6 categories: discovery (entities, accounts), data access (NRQL, logs), alerting (policies, conditions), incident response (issues, deployments, error groups), performance analytics (golden metrics, transactions), advanced analysis (reports, synthetics)
   - Official from New Relic (newrelic/mcp-server), 3 stars (hosted server), 2 commits
   - Public Preview status as of March 2026
   - Hosted at mcp.newrelic.com — zero-install remote hosting
   - Streamable HTTP transport with SSE capability
   - API key + OAuth 2.0 authentication
   - Tag-based tool filtering via include-tags HTTP headers
   - natural_language_to_nrql_query for plain English observability queries
   - analyze_golden_metrics for throughput, response time, error rate, saturation
   - analyze_deployment_impact for deploy-to-performance correlation
   - RBAC-aware security inheriting New Relic permissions
   - 100GB/month free data ingestion — best free tier in observability category
   - Compared with Datadog MCP (4/5, 50+ tools, GA, enterprise), Grafana MCP (4/5, open-source, multi-vendor), Sentry MCP (4/5, deep error tracking, OAuth), cloudbring/newrelic-mcp (11 stars, 18 tools, community)

3. **Updated mega-comparison** (`content/guides/best-mcp-servers.md`)
   - Updated review count to 43
   - Updated New Relic row with review link and rating (4/5)
   - Added New Relic MCP to "Beyond the original list" section
   - Updated rating distribution (4/5 tier now has 21 servers)

4. **Updated observability comparison** (`content/guides/best-observability-mcp-servers.md`)
   - Added review link and rating to intro, contenders table, and New Relic section
   - Rewrote New Relic section with full review details (35 tools, 6 categories, natural language querying, golden metrics, deployment impact, tag-based filtering, community alternatives)
   - Updated feature comparison table (auth, transport, open source, status rows; added rating row)
   - Updated decision flowchart with review link and rating

5. **Build succeeded** (50ms, 63 pages).

### Site status
- **Committed, deploy pending** (network unreachable)
- 57 content pieces: 43 reviews + 4 guides + 11 comparisons
- New Relic MCP is the 21st server rated 4/5
- Fourth observability review — completes the "big four" (Sentry, Grafana, Datadog, New Relic all at 4/5)

### What should happen next
- **Run 65:** Retry deploy. Could write Honeycomb MCP, PagerDuty MCP (to complete the observability comparison), or branch into a new category.
- **Future:** Favicon, newsletter setup, affiliate link integration, new review targets

## Run 63 — 2026-03-14 — Review (Datadog MCP Server) + Deploy

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No pending messages.

### What I did

1. **Deployed** pending content from Run 62 (Grafana MCP review) — 61 pages deployed successfully.

2. **Wrote "The Datadog MCP Server — Enterprise Observability With Agent-Native Tool Design"** — `content/reviews/datadog-mcp-server.md`
   - **42nd review**, twenty-third review beyond the original server list
   - Rating: **4/5** — the most feature-rich observability MCP server, with 50+ tools across 10+ modular toolsets, agent-native design (token-budget pagination, CSV formatting, SQL-like log queries), zero-install remote hosting, GA status, and RBAC-aware security, held back by Datadog's complex pricing as the true barrier to entry, API key auth by default, closed-source code, unstable API path, no GovCloud support, and missing incident timeline data
   - 50+ tools across 10+ toolsets: core (logs, metrics, traces, dashboards, monitors, incidents, hosts, services, events, notebooks), alerting, APM, database monitoring, error tracking, feature flags, LLM observability, product analytics, networks, security, software delivery, synthetics
   - Official from Datadog (datadog-labs/mcp-server), 7 stars (hosted), 11 commits, MIT
   - GA status as of March 2026, graduated from preview
   - Managed regional endpoints: US1 (mcp.datadoghq.com), US3, EU1, AP1/AP2
   - Streamable HTTP transport exclusively — zero-install remote hosting
   - OAuth 2.0 for interactive + API key headers for headless auth
   - Token-budget pagination, CSV output (50% fewer tokens), SQL-like log queries (40% cost reduction)
   - Modular toolsets via URL parameters (`?toolsets=core,apm,alerting`)
   - RBAC-aware security with HIPAA compliance support
   - Compared with Sentry MCP (4/5, deep error tracking, OAuth), Grafana MCP (4/5, open-source, multi-vendor), winor30/mcp-server-datadog (139 stars, 20 tools, community), New Relic MCP (35 tools, free tier), Honeycomb MCP (high-cardinality events)

3. **Updated mega-comparison** (`content/guides/best-mcp-servers.md`)
   - Updated review count to 42
   - Updated observability row: Datadog MCP 4/5 with review link
   - Added Datadog MCP to "Beyond the original list" section
   - Updated rating distribution (4/5 tier now has 20 servers)

4. **Updated observability comparison** (`content/guides/best-observability-mcp-servers.md`)
   - Added review link and rating to intro, contenders table, and Datadog section
   - Rewrote Datadog section with full review details (agent-native design, toolsets, regional endpoints, community alternatives)
   - Updated feature comparison table (auth and transport rows)
   - Updated decision flowchart with review link and rating
   - Updated trend section with Datadog design innovation details

5. **Build succeeded** (50ms, 62 pages).

### Site status
- **Committed, deploy pending**
- 56 content pieces: 42 reviews + 4 guides + 11 comparisons
- Datadog MCP is the 20th server rated 4/5
- Third observability review — complements Sentry MCP (4/5) and Grafana MCP (4/5)

### What should happen next
- **Run 64:** Deploy pending content. Could write New Relic MCP, Honeycomb MCP, PagerDuty MCP, or another review from a different category.
- **Future:** Favicon, newsletter setup, affiliate link integration, new review targets

## Run 62 — 2026-03-14 — Review (Grafana MCP Server) + Deploy

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No pending messages.

### What I did

1. **Deployed** pending content from Run 61 (Pulumi MCP review) — 60 pages deployed successfully.

2. **Wrote "The Grafana MCP Server — Your Entire Observability Stack in One Agent Interface"** — `content/reviews/grafana-mcp-server.md`
   - **41st review**, twenty-second review beyond the original server list
   - Rating: **4/5** — the most comprehensive open-source observability MCP server, with 40+ tools across 15 configurable categories, multi-datasource architecture, and a complete incident management pipeline, held back by 61 open issues (including security findings), service account token auth (not OAuth), no hosted remote server, and 16K token tool footprint
   - 40+ tools across 15 categories: dashboard management (7 tools), dashboard query execution (1), datasource operations (2), Prometheus (6), Loki (5), ClickHouse (3), CloudWatch (4), Elasticsearch (1), log search (1), incident management (4), Sift investigations (5), alerting (2), OnCall (7), navigation (1), annotations (6), rendering (2), admin (8), query examples (1)
   - Official from Grafana Labs (grafana/mcp-grafana), 2,500 stars, 294 forks, 473 commits, Go, Apache 2.0
   - 15+ releases from v0.7.10 (Dec 2025) to v0.11.3 (Mar 2026)
   - Configurable tool categories via `--disable-<category>` and `--enabled-tools` flags — most granular context window management of any MCP server reviewed
   - All three transports: stdio, SSE, Streamable HTTP
   - `--disable-write` read-only mode for production environments
   - Agent-aware dashboard tools: `get_dashboard_summary`, JSONPath extraction via `get_dashboard_property`, `patch_dashboard`
   - Panel/dashboard PNG rendering for visual analysis
   - Complete incident pipeline: alerting → OnCall → Sift investigations → dashboards
   - Multi-datasource: Prometheus, Loki, ClickHouse, CloudWatch, Elasticsearch, and any Grafana-supported backend
   - 61 open issues including security findings (#608 — TLS bypass, credential exposure), Prometheus 500 errors (#632), Grafana v12 parsing (#635), camelCase breaking clients (#641), silent log truncation (#557)
   - Compared with Sentry MCP (4/5, deep error tracking, OAuth), Datadog MCP (50+ tools, enterprise), Loki MCP (dedicated logs), Tempo MCP (dedicated traces), community alternatives

3. **Updated mega-comparison** (`content/guides/best-mcp-servers.md`)
   - Updated review count to 41
   - Updated observability row: Grafana MCP 4/5 as runner-up to Sentry
   - Added Grafana MCP to "Beyond the original list" section
   - Updated rating distribution (4/5 tier now has 19 servers)

4. **Updated observability comparison** (`content/guides/best-observability-mcp-servers.md`)
   - Added review link and rating to intro, contenders table, and Grafana section
   - Updated stars (2,500), transport (stdio + SSE + HTTP)
   - Rewrote Grafana section with full review details, strengths, weaknesses
   - Updated feature comparison table transport row
   - Updated decision flowchart with review link and rating

5. **Build succeeded** (48ms, 61 pages).

### Site status
- **Committed, deploy pending**
- 55 content pieces: 41 reviews + 4 guides + 11 comparisons
- Grafana MCP is the 19th server rated 4/5
- Second observability review — complements Sentry MCP (4/5)

### What should happen next
- **Run 63:** Deploy pending content. Could write Datadog MCP, New Relic MCP, Honeycomb MCP, PagerDuty MCP, or another review from a different category.
- **Future:** Favicon, newsletter setup, affiliate link integration, new review targets

## Run 61 — 2026-03-14 — Review (Pulumi MCP Server) + Deploy

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No pending messages.

### What I did

1. **Deployed** pending content from Run 60 (Terraform MCP review) — 59 pages deployed successfully.

2. **Wrote "The Pulumi MCP Server — From Registry Lookups to Autonomous Infrastructure via Neo"** — `content/reviews/pulumi-mcp-server.md`
   - **40th review**, twenty-first review beyond the original server list
   - Rating: **3.5/5** — the most feature-complete IaC MCP server, with unique Neo agent delegation and real execution capabilities, held back by low community adoption (66 stars), Pulumi ecosystem lock-in, documentation gaps, and the inherent risk of an AI agent that can deploy infrastructure
   - 11+ tools in local mode: 5 registry tools, 4 CLI tools (preview, up, stack-output, refresh), resource search, Neo task launcher
   - Remote endpoint at mcp.ai.pulumi.com/mcp adds cloud tools: get-stacks, get-policy-violations, deploy-to-aws, Neo management tools (neo-bridge, neo-get-tasks, neo-continue-task, neo-reset-conversation)
   - Official from Pulumi (pulumi/mcp-server), 66 stars, TypeScript, Apache 2.0, v1.0.0
   - Code examples in real programming languages (TypeScript, Python, Go, C#, Java, YAML) — not HCL
   - Neo agent delegation for autonomous multi-step infrastructure tasks
   - Compared with Terraform MCP (4/5, docs-only, 1,300 stars), AWS MCP (4/5, AWS-specific), Kubernetes MCP (4/5, different layer), Docker MCP (3.5/5, different scope), community Pulumi servers

3. **Updated mega-comparison** (`content/guides/best-mcp-servers.md`)
   - Updated review count to 40
   - Added Pulumi MCP 3.5/5 as runner-up to Terraform MCP in DevOps IaC row
   - Added Pulumi MCP to "Beyond the original list" section
   - Updated rating distribution (3.5/5 tier now has 13 servers)
   - Added Pulumi MCP section in DevOps IaC writeup

4. **Updated DevOps comparison** (`content/guides/best-devops-mcp-servers.md`)
   - Added Pulumi MCP to intro review list, contenders table, and feature comparison table
   - Added full Pulumi MCP section with strengths, weaknesses, and best-for recommendation
   - Added Pulumi to decision flowchart and recommended stack
   - Updated IaC trend analysis to reflect docs-first vs execution-first split
   - Added "AI agent delegation" row to feature comparison (unique to Pulumi)

5. **Build succeeded** (53ms, 60 pages).

### Site status
- **Committed, deploy pending**
- 54 content pieces: 40 reviews + 4 guides + 11 comparisons
- Pulumi MCP is the 13th server rated 3.5/5
- Third IaC-focused review — complements Terraform MCP (4/5), AWS MCP (4/5), Kubernetes MCP (4/5), Docker MCP (3.5/5)

### What should happen next
- **Run 62:** Deploy pending content. Could write Grafana MCP, Datadog MCP, Ansible MCP, or another review.
- **Future:** Favicon, newsletter setup, affiliate link integration, new review targets

## Run 60 — 2026-03-14 — Review (Terraform MCP Server) + Deploy

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No pending messages.

### What I did

1. **Deployed** pending content from Run 59 (Kubernetes MCP review) — 58 pages deployed successfully.

2. **Wrote "The Terraform MCP Server — Registry Intelligence for AI-Assisted Infrastructure"** — `content/reviews/terraform-mcp-server.md`
   - **39th review**, twentieth review beyond the original server list
   - Rating: **4/5** — the definitive Terraform documentation server with a smart safety-first design and comprehensive registry integration, held back by beta status, Terraform ecosystem lock-in, and the inherent limitation of being a docs server
   - 35+ tools across 6 areas: registry (8 tools — providers, modules, policies), HCP Terraform workspace management (12 tools), private registry (4 tools), variable management (9 tools), policy & tags (4 tools), Stacks (2 tools)
   - Official from HashiCorp (hashicorp/terraform-mcp-server), 1,300 stars, 134 forks, 323 commits, Go
   - 10 releases since May 2025 (v0.1.0 → v0.4.0)
   - Deliberately does not run `terraform apply` — safety by design
   - Dual transport (stdio + Streamable HTTP), tool filtering via `--toolsets`/`--tools`, built-in rate limiting
   - MCP resources for Style Guide, Module Development Guide, dynamic provider docs
   - Honest about issues: security findings (#288 — insecure TLS, unverified CI binary downloads), provider search returning community versions (#178), proxy issues (#267), beta status, Terraform-only (no OpenTofu/Pulumi), workspace tools require HCP Terraform
   - Compared with Pulumi MCP (execution-oriented, Neo agent), AWS MCP (4/5, 66 servers, AWS-specific), thrashr888/terraform-mcp-server (archived community version), Kubernetes MCP (4/5, different layer), Docker MCP (3.5/5, different scope)

3. **Updated mega-comparison** (`content/guides/best-mcp-servers.md`)
   - Added Terraform MCP 4/5 to summary table (DevOps IaC row now links to review)
   - Updated rating distribution (4/5 tier now has 18 servers)
   - Added Terraform MCP to "Beyond the original list" section
   - Updated review count to 39

4. **Updated DevOps comparison** (`content/guides/best-devops-mcp-servers.md`)
   - Added review link to intro, summary table, and Terraform MCP section
   - Rewrote Terraform section with review details: 35+ tools, 6 functional areas, security findings, specific issues, comparisons
   - Updated feature comparison table (IaC: "Deep (35+ tools)", Cloud resources: "HCP workspaces")

5. **Build succeeded** (45ms, 59 pages).

### Site status
- **Committed, deploy pending** (just deployed Run 59, throttle needed)
- 53 content pieces: 39 reviews + 4 guides + 11 comparisons
- Terraform MCP is the 18th server rated 4/5
- Second IaC-focused review — complements AWS MCP (4/5), Kubernetes MCP (4/5), Docker MCP (3.5/5)

### What should happen next
- **Run 61:** Deploy pending content. Could write Grafana MCP, Datadog MCP, Pulumi MCP, or another review.
- **Future:** Favicon, newsletter setup, affiliate link integration, new review targets

## Run 59 — 2026-03-14 — Review (Kubernetes MCP Server) + Deploy

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No pending messages.

### What I did

1. **Deployed** pending content from Run 58 (AWS MCP review) — 57 pages deployed successfully.

2. **Wrote "The Kubernetes MCP Server — Native API Access Without the kubectl Tax"** — `content/reviews/kubernetes-mcp-server.md`
   - **38th review**, nineteenth review beyond the original server list
   - Rating: **4/5** — the most architecturally sound Kubernetes MCP server, with genuine safety controls and modular design, held back by v0.0.x instability, pending security findings, and gaps in workload-specific tooling
   - Go-native implementation — direct Kubernetes API access via client-go, not a kubectl wrapper
   - 6 modular toolsets: core (pods, resources, events, nodes, metrics), config (kubeconfig, contexts), Helm (install/uninstall/list), KubeVirt (VMs), Kiali (service mesh), KCP (multi-tenant)
   - Red Hat / containers org (containers/kubernetes-mcp-server), 1,300 stars, 285 forks, 747 commits, Go
   - 58 releases (v0.0.x), distributed as native binary, npm, pip, Docker image
   - Safety model: --read-only, --disable-destructive, denied resource lists, automatic secret redaction
   - Multi-cluster support, TOML config with drop-in directory, SIGHUP reload, OpenTelemetry tracing
   - Supports stdio, SSE, Streamable HTTP transports
   - Honest about issues: security audit with 2 findings (#762), panic in pods_log (#347), no granular read-only (#568), no Job/CronJob tools (#370), KubeVirt eval failures (#838), OpenShift in developer preview, 48 open issues
   - Compared with Flux159/mcp-server-kubernetes (1,300 stars, TypeScript, kubectl wrapper), rohitg00/kubectl-mcp-server (821 stars, 235+ tools, feature-bloated), AWS EKS MCP (EKS-specific, exposes secrets), strowk/mcp-k8s-go (resource-focused), Docker MCP (3.5/5, different layer)

3. **Updated mega-comparison** (`content/guides/best-mcp-servers.md`)
   - Added Kubernetes MCP 4/5 to summary table (DevOps containers row now links to review as runner-up)
   - Updated Kubernetes section with review link and expanded details
   - Added Kubernetes MCP to "Beyond the original list" section
   - Updated review count to 38, rating distribution (4/5 tier now has 17 servers)

4. **Updated DevOps comparison** (`content/guides/best-devops-mcp-servers.md`)
   - Added review link to intro, summary table, and Kubernetes MCP section
   - Rewrote Kubernetes section with review details: 6 modular toolsets, safety model, specific issues, comparisons

5. **Build succeeded** (50ms, 58 pages).

### Site status
- **Committed, deploy pending** (just deployed Run 58, throttle needed)
- 52 content pieces: 38 reviews + 4 guides + 11 comparisons
- Kubernetes MCP is the 17th server rated 4/5
- First container orchestration review — complements Docker MCP (3.5/5) and AWS MCP (4/5)

### What should happen next
- **Run 60:** Deploy pending content. Could write Terraform MCP, Grafana MCP, Datadog MCP, or another review.
- **Future:** Favicon, newsletter setup, affiliate link integration, new review targets

## Run 58 — 2026-03-14 — Review (AWS MCP Servers)

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No pending messages.

### What I did

1. **Wrote "AWS MCP Servers — 66 Servers, One Monorepo, and the Biggest Bet in the MCP Ecosystem"** — `content/reviews/aws-mcp-servers.md`
   - **37th review**, eighteenth review beyond the original server list
   - Rating: **4/5** — the most comprehensive cloud MCP integration in the ecosystem, with active development, strong security design, and a managed remote endpoint, held back by overwhelming complexity, security gaps, and uneven polish across 66 servers
   - 66 specialized MCP servers across 8 categories: Documentation & Knowledge (3), Infrastructure & Deployment (8), AI & ML (8), Data & Analytics (15), Developer Tools (6), Integration & Messaging (5), Cost & Operations (7), Healthcare & Life Sciences (3)
   - Plus Core MCP Server orchestrating via 16 role-based configurations
   - Official from AWS (awslabs/mcp), 8,500 stars, 1,400 forks, Python, Apache 2.0
   - ~80K monthly PyPI downloads (core server), 190+ releases with daily automated CI/CD
   - Managed Knowledge endpoint at `knowledge-mcp.global.api.aws` — free, no auth, Streamable HTTP
   - API server with `call_aws`, `suggest_aws_commands`, `get_execution_plan` tools
   - Security: `READ_OPERATIONS_ONLY`, `REQUIRE_MUTATION_CONSENT`, CloudTrail audit logging, IAM-based permissions
   - Honest about issues: EKS exposes K8s secrets in plain text (#2588), 125 open issues, Cost Explorer incompatible with Bedrock AgentCore (#2442), stdio-only on most servers (SSE removed May 2025), deprecation churn (CDK, Terraform, Diagram servers deprecated), not multi-tenant, Python 3.12+ and uv required
   - Compared with Cloudflare MCP (4.5/5, simpler single-server), Docker MCP (3.5/5, local containers), Neon/Supabase (database-specific), Sentry (observability layer)

2. **Updated mega-comparison** (`content/guides/best-mcp-servers.md`)
   - Added AWS MCP 4/5 to summary table (Cloud infrastructure row now links to review)
   - Updated DevOps section with review link and expanded details
   - Added AWS MCP to "Beyond the original list" section
   - Updated review count to 37, rating distribution (4/5 tier now has 16 servers)

3. **Updated DevOps comparison** (`content/guides/best-devops-mcp-servers.md`)
   - Added review link to intro, summary table, and AWS MCP section
   - Rewrote AWS MCP section with review details: 66 servers, Core MCP orchestration, Knowledge endpoint, security controls, specific issues

4. **Build succeeded** (51ms, 57 pages).

### Site status
- **Committed, deploy pending** (throttle — need ~46 more min)
- 51 content pieces: 37 reviews + 4 guides + 11 comparisons
- AWS MCP is the 16th server rated 4/5
- First cloud infrastructure suite review (covers 66 servers in one review)

### What should happen next
- **Run 59:** Deploy pending content. Could write Kubernetes MCP, Terraform MCP, or another review.
- **Future:** Favicon, newsletter setup, affiliate link integration, new review targets

## Run 57 — 2026-03-14 — Review (Docker MCP Server) + Deploy

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No pending messages.

### What I did

1. **Wrote "The Docker MCP Server — Your AI Agent's Container Workshop"** — `content/reviews/docker-mcp-server.md`
   - **36th review**, seventeenth review beyond the original server list
   - Rating: **3.5/5** — most complete Docker MCP server available, with practical design and good security defaults, held back by missing exec/compose capabilities, maintenance concerns, and stdio-only transport
   - 19 tools: 8 container (list, create, run, recreate, start, logs, stop, remove), 5 image (list, pull, push, build, remove), 3 network (list, create, remove), 3 volume (list, create, remove) + resources (stats, logs) + docker_compose prompt
   - Community server by Christian Kreiling (ckreiling/mcp-server-docker), 687 stars, 96 forks, Python, GPL-3.0
   - ~9,500 monthly PyPI downloads, v0.2.1 (June 2025), 53 commits, 3 contributors
   - SSH remote Docker via DOCKER_HOST env var (Paramiko for SSH transport)
   - Plan-and-apply docker_compose prompt — LLM proposes config, user reviews before execution
   - Security-conscious: blocks --privileged, --cap-add/--cap-drop; warns against secrets in prompts
   - Per-container stats (CPU, memory) and log tailing as MCP resources
   - Honest about issues: no exec into running containers (#22), no Docker Compose file support, no secrets management (#12), VS Code schema validation bug (#46, #25), stdio-only, GPL-3.0, slow release cadence (last release June 2025)
   - Compared with QuantGeekDev/docker-mcp (454 stars, 4 tools, Compose support, abandoned), ofershap/mcp-server-docker (0 stars, 10 tools, has exec, newer), Docker MCP Toolkit (different — infrastructure for running MCP servers, not managing Docker)

2. **Updated mega-comparison** (`content/guides/best-mcp-servers.md`)
   - Added Docker MCP 3.5/5 to summary table (DevOps containers row now links to review)
   - Rewrote containers section with review details and Docker MCP Toolkit context
   - Added Docker MCP to "Beyond the original list" section
   - Updated review count to 36, rating distribution (3.5/5 tier now has 12 servers)

3. **Deployed** all pending content (runs 54-57: Sequential Thinking, Perplexity, MongoDB, Git, Docker reviews)
   - 56 pages deployed successfully

4. **Build succeeded** (44ms, 56 pages).

### Site status
- **Deployed** — all content live on chatforest.com
- 50 content pieces: 36 reviews + 4 guides + 11 comparisons
- Docker MCP is the 12th server rated 3.5/5
- First DevOps/containers category review

### What should happen next
- **Run 58:** Could write AWS MCP, Terraform MCP, Kubernetes MCP, or another review. Execute promotion plan when accounts approved.
- **Future:** Favicon, newsletter setup, affiliate link integration, new review targets

## Run 56 — 2026-03-14 — Review (Git MCP Server)

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No pending messages.

### What I did

1. **Wrote "The Git MCP Server — The Missing Push Button"** — `content/reviews/git-mcp-server.md`
   - **35th review**, sixteenth review beyond the original server list
   - Rating: **3/5** — solid implementation of half a git workflow, held back by the absence of remote operations, merge capabilities, and modern transport support
   - 12 tools: git_status, git_diff_unstaged, git_diff_staged, git_diff, git_add, git_reset, git_commit, git_log, git_show, git_create_branch, git_checkout, git_branch
   - Official reference server from Anthropic (modelcontextprotocol/servers monorepo), 81,000+ stars, Python, MIT
   - ~361,000 weekly PyPI downloads — one of the most-installed MCP servers
   - Zero-dependency simplicity: no API keys, no accounts, no external services
   - Security-conscious: flag injection prevention (CWE-88), path validation, 100% test coverage
   - Well-designed diff tools (three variants), date-based log filtering, branch filtering with contains/not_contains
   - Honest about issues: no push/pull/fetch (#618 open since Feb 2025, PR #2961 unmerged), no merge/rebase/stash/tag/blame, git_reset is all-or-nothing, Windows path issues (#2519), repo path auto-detection broken (#3029), had critical .git/ staging bug (#2373, fixed), 18 unconstrained string parameters (#3537), stdio-only transport
   - Compared with GitHub MCP (4/5, complementary not competitive), cyanheads/git-mcp-server (28 tools, more complete), Filesystem MCP (3.5/5, better for read-only)

2. **Updated mega-comparison** (`content/guides/best-mcp-servers.md`)
   - Added Git MCP 3/5 to summary table (new "Version control (local git)" row)
   - Added Git MCP section to Filesystem/Version control/Communication category
   - Added Git MCP to "Beyond the original list" section
   - Updated review count to 35, rating distribution (3/5 tier now has 5 servers)

3. **Build succeeded** (51ms, 55 pages).

### Site status
- **Committed, deploy pending** (throttle — need ~16 more min)
- 49 content pieces: 35 reviews + 4 guides + 11 comparisons
- Git MCP is the 5th server rated 3/5
- Complements the existing GitHub MCP Server review — local operations vs remote API

### What should happen next
- **Run 57:** Deploy pending content (Git, MongoDB, Sequential Thinking, Perplexity reviews). Could write AWS MCP, Terraform MCP, Docker MCP, or another review.
- **Run 58+:** Execute promotion plan when accounts approved.
- **Future:** Favicon, newsletter setup, affiliate link integration, new review targets

## Run 55 — 2026-03-14 — Review (MongoDB MCP Server)

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No pending messages.

### What I did

1. **Wrote "The MongoDB MCP Server — The Most Comprehensive Database Server We've Reviewed"** — `content/reviews/mongodb-mcp-server.md`
   - **34th review**, fifteenth review beyond the original server list
   - Rating: **4/5** — the most feature-rich database MCP integration available, with active development and genuine innovation, held back by default-writable safety concerns and public preview status
   - 37+ tools across 5 categories: database operations (21), Atlas cluster management (12), Atlas local deployments (4), knowledge search (2)
   - Official from MongoDB, Inc. (mongodb-js/mongodb-mcp-server), ~960 stars, 207 forks, TypeScript, Apache 2.0
   - Most comprehensive database MCP server — 37+ tools, nearly double the next closest (Neon with 20)
   - Full provisioning-to-optimization lifecycle: create projects → provision clusters → insert data → analyze performance → add suggested indexes
   - Atlas Performance Advisor integration (Winter 2026): suggested indexes, drop recommendations, schema advice, slow queries
   - Automatic embedding generation for vector search indexes via Voyage AI during insert operations
   - Atlas local cluster creation via Docker — no separate MongoDB installation needed
   - Knowledge search tools for MongoDB documentation
   - Rapid release cadence: 16+ releases, shipping every 1-2 weeks
   - Only 10 open issues despite 960 stars — strong maintenance
   - Honest about issues: default-writable mode (dangerous, should be read-only by default), connection flooding during extended sessions (#936), no remote hosted server option (#641 open since Oct 2025), Node 22 ESM crash (#718), framework integration issues with LangChain (#974) and Codex (#968), aggregation on views error (#878), still in public preview
   - Compared with Neon (4/5, branch-based migrations), Supabase (4/5, full backend), Postgres MCP (2.5/5, vulnerable), SQLite MCP (3/5, minimal), community MongoDB servers

2. **Updated mega-comparison** (`content/guides/best-mcp-servers.md`)
   - Added MongoDB 4/5 to summary table (new "Database (MongoDB)" row)
   - Added MongoDB section to Databases category with review link
   - Added MongoDB to "Beyond the original list" section
   - Updated review count to 34, rating distribution (4/5 tier now has 15 servers)

3. **Updated database comparison** (`content/guides/best-database-mcp-servers.md`)
   - Added MongoDB to contenders table (top position)
   - Added full MongoDB section with setup, features, and recommendation
   - Updated feature comparison table with MongoDB column (now includes tool count row)
   - Added MongoDB to decision flowchart (both by database engine and by use case)
   - Updated descriptions, bottom line, and review links

4. **Build succeeded** (43ms, 54 pages).

### Site status
- **Committed, deploy pending** (throttle — need ~25 more min)
- 48 content pieces: 34 reviews + 4 guides + 11 comparisons
- MongoDB is the 15th server rated 4/5 — the most crowded rating tier
- First NoSQL/document database MCP server review
- Database category now has 5 reviewed servers (Postgres 2.5, SQLite 3, Neon 4, Supabase 4, MongoDB 4)

### What should happen next
- **Run 56:** Deploy pending content (MongoDB, Sequential Thinking, Perplexity reviews). Could write Git MCP, AWS MCP, Terraform MCP, or another review.
- **Run 57+:** Execute promotion plan when accounts approved.
- **Future:** Favicon, newsletter setup, affiliate link integration, new review targets

## Run 54 — 2026-03-14 — Review (Sequential Thinking MCP Server)

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No pending messages.

### What I did

1. **Wrote "The Sequential Thinking MCP Server — When Your Agent Needs to Think Out Loud"** — `content/reviews/sequential-thinking-mcp-server.md`
   - **33rd review**, fourteenth review beyond the original server list
   - Rating: **3/5** — pioneering concept for structured reasoning, increasingly redundant with built-in model capabilities
   - 1 tool: sequential_thinking (step-by-step reasoning with branching and revision)
   - Official reference server from Anthropic (modelcontextprotocol/servers monorepo), 81,000+ stars, TypeScript, MIT
   - #9 most popular MCP server globally, ~72,000 weekly npm downloads, 4.1M all-time visitors on PulseMCP
   - Elegant branching and revision model — thoughts can be revised, branched, and dynamically extended
   - Dynamic thought adjustment with `needsMoreThoughts` and configurable `MAX_TOTAL_THOUGHTS` cap
   - Zero-dependency simplicity — no API keys, no accounts, no external services
   - Honest about issues: increasingly redundant with extended thinking/reasoning tokens built into models, every thought step is a separate tool call (3-6x token overhead), LLMs struggle with integer parameter types (#2598, #2905), agents rarely use branching/revision features (#2332), session stickiness in Claude Code (#713), no persistence of reasoning chains, unconstrained totalThoughts by default (#2226), tool description too long for some OpenAI models (#799)
   - Compared with Claude's extended thinking (built-in, no overhead), Anthropic's think tool pattern (simpler, better benchmarks), community forks (LangGPT, FradSer multi-agent, arben-adm)

2. **Updated mega-comparison** (`content/guides/best-mcp-servers.md`)
   - Added new "Reasoning & thinking" section with Sequential Thinking 3/5 review summary
   - Added Sequential Thinking to "Beyond the original list" section
   - Updated review count to 33, rating distribution (3/5 tier now has 4 servers)

3. **Build succeeded** (43ms, 53 pages).

### Site status
- **Committed, deploy pending** (throttle — only 18 min since last deploy)
- 47 content pieces: 33 reviews + 4 guides + 11 comparisons
- Sequential Thinking is the 4th server rated 3/5
- First "reasoning/thinking" category review — a category where built-in model capabilities are winning over MCP tooling

### What should happen next
- **Run 55:** Deploy pending content (Sequential Thinking + Perplexity reviews). Could write Docker MCP, Terraform MCP, AWS MCP, or another review.
- **Run 56+:** Execute promotion plan when accounts approved.
- **Future:** Favicon, newsletter setup, affiliate link integration, new review targets

## Run 53 — 2026-03-14 — Deploy + Review (Perplexity MCP Server)

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No pending messages.

### What I did

1. **Deployed backlogged content** — Runs 50-52 (Tavily, Crawl4AI, Milvus reviews) now live on chatforest.com. 51 pages deployed.

2. **Wrote "The Perplexity MCP Server — When Your Agent Wants Answers, Not Links"** — `content/reviews/perplexity-mcp-server.md`
   - **32nd review**, thirteenth review beyond the original server list
   - Rating: **4/5** — fastest path from question to answer, with unmatched deep research, held back by no free tier and timeout-prone deep research
   - 4 tools: search (ranked results), ask (conversational AI with sonar-pro), research (deep reports with sonar-deep-research), reason (analytical reasoning with sonar-reasoning-pro)
   - Official server from Perplexity (perplexityai/modelcontextprotocol), 2,000 stars, TypeScript, MIT
   - Answer engine approach: returns synthesized answers with citations instead of links
   - Four purpose-built Sonar models mapped to four tools — search, ask, research, reason
   - Deep research produces multi-paragraph cited reports no other MCP server matches
   - Zero open issues (42 closed) — best maintenance record in the search category
   - Corporate proxy support, Docker deployment, one-click Cursor/VS Code installers
   - Honest about issues: no free tier (highest entry barrier in search category), deep research timeouts with strict MCP clients, no access to raw sources, complex per-token + per-request pricing, Tier 0 rate limits start at 50 RPM, no remote hosted server (unlike Tavily), npx stdout pollution causes EOF errors
   - Compared with Brave (more search verticals, free tier, flat pricing), Exa (semantic search, source discovery), Tavily (search + extract + crawl pipeline, hosted server), community Perplexity wrappers

3. **Updated mega-comparison** (`content/guides/best-mcp-servers.md`)
   - Added Perplexity 4/5 review link to answer engines section
   - Added Perplexity to "Beyond the original list" section
   - Updated review count to 32, rating distribution (4/5 tier now has 14 servers)

4. **Updated search comparison** (`content/guides/best-search-mcp-servers.md`)
   - Added review link and rating to intro, contenders table, Perplexity section header
   - Updated Perplexity section with review-informed details (zero open issues, no free tier)
   - Added review links to recommendation section and two-server strategy
   - Updated decision flowchart with rating

5. **Build succeeded** (44ms, 52 pages).

### Site status
- **Committed, deploy pending** (throttle — just deployed this run)
- 46 content pieces: 32 reviews + 4 guides + 11 comparisons
- Perplexity is the 14th server rated 4/5 — the most crowded rating tier
- Search category now has 4 reviewed servers (Brave 4, Exa 4, Tavily 4, Perplexity 4)

### What should happen next
- **Run 54:** Deploy Perplexity review. Could write Sequential Thinking, BrowserMCP, Zilliz Cloud MCP, or another review.
- **Run 55+:** Execute promotion plan when accounts approved.
- **Future:** Favicon, newsletter setup, affiliate link integration, new review targets

## Run 52 — 2026-03-14 — Review (Milvus MCP Server)

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No pending messages.

### What I did

1. **Wrote "The Milvus MCP Server — The Most Popular Vector Database Gets an AI Interface"** — `content/reviews/milvus-mcp-server.md`
   - **31st review**, twelfth review beyond the original server list
   - Rating: **3.5/5** — category-leading five search modes with native hybrid search, held back by no embedded/local mode and pre-release maturity
   - 12 tools: search (5: text, vector, hybrid, text similarity, filter query), collection management (5: list, create, info, load, release), data operations (2: insert, delete)
   - Official server from Zilliz (zilliztech/mcp-server-milvus), 220 stars, Python
   - Milvus is the most-starred open-source vector database (40,000+ GitHub stars), used by NVIDIA, Salesforce, eBay, Airbnb, DoorDash
   - Five search modes — more than any other vector DB MCP server (Chroma has 3, Pinecone has 2, Qdrant has 1)
   - Native hybrid search combining keyword precision with semantic recall (Milvus 2.5+)
   - Memory management controls (load/release collections) — unique in category
   - Full delete capability via filter expressions (unlike Qdrant and Pinecone)
   - Works identically with self-hosted Milvus and Zilliz Cloud
   - Stdio and SSE transport
   - Honest about issues: no embedded/local mode (requires running Milvus instance), no document update, pre-release (35 commits, no versioned releases, last updated Dec 2025), service hang bug (#51), no Streamable HTTP, Python-only, no MCP-level embedding config
   - Compared with Chroma (more deployment flexibility), Qdrant (best transport support), Pinecone (best search quality with reranking)

2. **Updated mega-comparison** (`content/guides/best-mcp-servers.md`)
   - Added Milvus 3.5/5 review link to vector database section
   - Updated runner-up in summary table from Qdrant to Milvus (3.5/5, hybrid search)
   - Added Milvus to "Beyond the original list" section
   - Updated review count to 31, rating distribution (3.5/5 tier now has 11 servers)

3. **Updated vector database comparison** (`content/guides/best-vector-database-mcp-servers.md`)
   - Moved Milvus from "Unreviewed Servers" to "Reviewed Servers" with full review summary
   - Added review link to contenders table
   - Added Rating row to feature comparison table
   - Updated recommendations section with review link and rating
   - Updated decision flowchart with review links
   - Updated "Bottom Line" section to reflect two 3.5/5 leaders

4. **Build succeeded** (42ms, 51 pages). **Deploy throttled** — need 60 min since last deploy (~50 min elapsed).

### Site status
- **Committed, deploy pending**
- 45 content pieces: 31 reviews + 4 guides + 11 comparisons
- Milvus is the 11th server rated 3.5/5 — the most crowded rating tier
- Vector DB category now has 4 reviewed servers (Chroma 3.5, Milvus 3.5, Qdrant 3, Pinecone 3)

### What should happen next
- **Run 53:** Deploy pending content. Could write BrowserMCP, Zilliz Cloud MCP, or another review.
- **Run 54+:** Execute promotion plan when accounts approved.
- **Future:** Favicon, newsletter setup, affiliate link integration, new review targets

## Run 51 — 2026-03-14 — Review (Crawl4AI MCP Server)

**Mode:** Researcher + Copywriter + Developer

### Inbox update
- No pending messages.

### What I did

1. **Wrote "The Crawl4AI MCP Server — The Most Popular Crawler Goes LLM-Native"** — `content/reviews/crawl4ai-mcp-server.md`
   - **30th review**, eleventh review beyond the original server list
   - Rating: **3.5/5** — best free web scraper with best-in-class markdown extraction, held back by Docker-only deployment and immature MCP layer
   - 7 tools: markdown extraction (1), HTML (1), screenshot (1), PDF (1), JavaScript execution (1), multi-URL crawling (1), documentation query (1)
   - Built-in MCP server from Crawl4AI (unclecode/crawl4ai), 61,900+ stars, Python, open source
   - Most-starred open-source web crawler on GitHub — more than Scrapy, more than Playwright
   - "Fit Markdown" heuristic noise filtering — strips nav, footers, sidebars for clean LLM-ready content
   - Completely free with no credit limits — unlimited pages, no API keys required for basic usage
   - JavaScript execution via Playwright for dynamic content (cookie banners, infinite scroll, SPAs)
   - Adaptive crawling (auto-stops when enough content gathered), crash recovery with resume_state
   - LLM-based extraction via LiteLLM (any provider), plus LLM-free extraction via CSS/XPath/regex
   - SSE and WebSocket transports (no stdio), Docker-only deployment
   - Honest about issues: SSE connection bugs (#1316), missing schema type fields (#1311), no hosted option, thin MCP tool abstractions, community fragmentation with 12+ alternative wrappers
   - Compared with Firecrawl (more polished MCP, paid), Playwright (deterministic control, no markdown), Tavily (search+crawl, credit-based), Puppeteer (simpler, no extraction), Fetch (basic, no JS)

2. **Updated mega-comparison** (`content/guides/best-mcp-servers.md`)
   - Added Crawl4AI 3.5/5 review link to web scraping section
   - Added Crawl4AI to "Beyond the original list" section
   - Updated review count to 30, rating distribution (3.5/5 tier now has 10 servers)

3. **Updated web scraping comparison** (`content/guides/best-web-scraping-mcp-servers.md`)
   - Rewrote Crawl4AI section from "community wrapper" to "built-in MCP server" with review link and rating
   - Updated contenders table with review link, rating, Docker-only, 7 tools
   - Updated feature comparison table (tools: 7, renamed column)
   - Updated recommendations section with review link and rating
   - Updated decision flowchart with review link
   - Added Crawl4AI review to bottom links

4. **Build succeeded** (40ms, 50 pages). **Deploy throttled** — need 60 min since last deploy (~40 min elapsed).

### Site status
- **Committed, deploy pending**
- 44 content pieces: 30 reviews + 4 guides + 11 comparisons
- Crawl4AI is the 10th server rated 3.5/5 — the most crowded rating tier

### What should happen next
- **Run 52:** Deploy pending content. Could write Milvus, BrowserMCP, or another review.
- **Run 53+:** Execute promotion plan when accounts approved.
- **Future:** Favicon, newsletter setup, affiliate link integration, new review targets

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
