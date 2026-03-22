---
title: "Best Documentation MCP Servers in 2026"
date: 2026-03-14T03:20:28+09:00
description: "Context7 vs GitMCP vs Docfork vs Deepcon vs Nia vs Docs MCP — which documentation MCP server should your AI coding agent use? We compare centralized registries, repo-based retrieval, and local-first indexing with clear recommendations."
og_description: "Context7 vs GitMCP vs Docfork vs Deepcon — which documentation MCP server should your coding agent use? We compared them all. Here's the verdict."
content_type: "Comparison"
card_description: "Context7 vs GitMCP vs Docfork vs Deepcon vs Nia vs Docs MCP — which documentation MCP server feeds the best context to your AI coding agent? A side-by-side comparison with clear recommendations."
last_refreshed: 2026-03-22
---

AI coding agents hallucinate APIs. They invent function signatures that don't exist, reference deprecated parameters, and confidently generate code against last year's version of a library. The fix is straightforward: feed your agent the current documentation at query time instead of relying on stale training data.

The MCP ecosystem now has nearly a dozen documentation servers competing to solve this problem, and they take fundamentally different approaches. Some maintain centralized registries of pre-processed docs. Some read directly from GitHub repos. Some run entirely on your machine. Picking the wrong one means your agent is working with unverified documentation, hitting rate limits, or paying for something it could get for free.

We've [reviewed the Context7 MCP server](/reviews/context7-mcp-server/) (3.5/5) — the market leader with 50,100 GitHub stars. Here's how the full documentation server landscape compares, and which one you should actually use.

## The Contenders

| Server | Stars | Type | Libraries | Free Tier | Paid | Best For |
|--------|-------|------|-----------|-----------|------|----------|
| [Context7](/reviews/context7-mcp-server/) | 50,100 | Centralized registry | 9,000+ | 1K req/mo | $8+/mo | Broadest coverage, largest community |
| [GitMCP](/reviews/gitmcp-server/) | 7,800 | Repo-based | Any public repo | Unlimited | Free | Zero-setup, any GitHub repo |
| Docs MCP | 1,200 | Local-first | Manual indexing | Unlimited | Free | Privacy, offline use |
| Ref.Tools | 1,000 | Cloud + smart chunking | 1,000s | 200 credits | $19–50/mo | Token efficiency |
| Docfork | 438 | Centralized + isolation | 10,000+ | 1K req/mo | Paid tiers | Team context isolation |
| rtfmbro | 80 | Git-tag versioned | npm/PyPI/SPM | Unlimited | Free | Exact version precision |
| Nia | 48 | Cloud + deep research | 3,000+ | 50 queries/mo | $14.99+/mo | Cross-codebase research |
| Deepcon | N/A | Cloud (closed-source) | 10,000+ | Limited | $8–20/mo | Accuracy (vendor-claimed) |

## The Three Architecture Models

Documentation MCP servers fall into three distinct categories. Understanding these matters more than comparing feature counts:

### 1. Centralized Registries (Context7, Docfork, Deepcon)

A company maintains a cloud-hosted registry of pre-processed documentation. Your agent queries their API, and the server returns relevant chunks. The documentation is crawled, processed, and stored ahead of time — not fetched at query time.

**When it works best:** Standard libraries with well-known docs. You ask about React hooks or FastAPI middleware, and the server returns current, pre-chunked documentation instantly. No setup, no indexing — it just works.

**When it fails:** When the registry hasn't crawled the library you need. When the documentation is community-contributed and hasn't been verified against the official source (Context7's [ContextCrush vulnerability](https://noma.security/blog/contextcrush-context7-the-mcp-server-vulnerability/) showed this risk). When the vendor changes pricing — Context7 cut its free tier by 83–92% in January 2026.

### 2. Repo-Based Retrieval (GitMCP, rtfmbro)

Instead of maintaining a separate registry, these servers read documentation directly from the source — the actual GitHub repository. GitMCP turns any public repo into an MCP endpoint by replacing `github.com` with `gitmcp.io` in the URL. rtfmbro reads from the exact git tag matching your lockfile.

**When it works best:** Any public library, including obscure ones no registry has indexed. You get the documentation the maintainers actually wrote, not a third party's processed version. No vendor lock-in, no rate limit surprises.

**When it fails:** Private repos (GitMCP is public-only). Libraries with poor documentation — if the README is sparse, that's all you get. No semantic search, so finding the right section requires knowing what to ask for.

### 3. Local-First Indexing (Docs MCP, Context by Neuledge)

These servers run entirely on your machine. You point them at documentation sources (URLs, files, repos), they index locally, and your agent queries the local index. Nothing leaves your machine.

**When it works best:** Sensitive codebases, air-gapped environments, enterprise compliance requirements. No rate limits, no API costs, no vendor dependencies. You control exactly what gets indexed.

**When it fails:** Requires setup — you must manually index each library. No community-maintained library catalog to draw from. Semantic search requires an embedding API (OpenAI, Gemini, etc.), which reintroduces an external dependency.

## The Servers in Detail

### Context7 — The Market Leader

**[upstash/context7](https://github.com/upstash/context7)** | [Our full review](/reviews/context7-mcp-server/) | Rating: 3.5/5

Context7 is the most popular MCP server of 2026. Period. Over 50,000 GitHub stars, 240,000+ weekly npm downloads, and support for 30+ AI coding clients. It started with two simple tools — `resolve-library-id` and `query-docs` — and that simplicity drove adoption. It now also offers a CLI (`npx ctx7`) and a Skills-based plugin system that can trigger documentation lookup automatically without explicit MCP calls.

**Why it's good:**
- Largest library coverage (9,000+) with version-specific documentation
- Two-tool simplicity plus CLI and Skills-based plugin for automatic triggering
- 30+ client integrations, OAuth setup, VS Code extension
- Active development by Upstash (not a side project)

**The catch:** The [ContextCrush context poisoning vulnerability](https://noma.security/blog/contextcrush-context7-the-mcp-server-vulnerability/) (patched February 2026) exposed an architectural risk — community-contributed docs in a centralized registry are a trust surface. The free tier was cut from ~6,000 to 1,000 requests/month in January 2026. And 148 open GitHub issues suggest connection reliability problems across platforms.

**Best for:** Developers who want the easiest setup and broadest library support, and are comfortable with the trade-offs of a centralized, cloud-dependent model.

### GitMCP — The Zero-Setup Option

**[idosal/git-mcp](https://github.com/idosal/git-mcp)** | 7,800 stars

GitMCP is the most elegant solution in this space. Take any GitHub URL, replace `github.com` with `gitmcp.io`, and you have an MCP documentation endpoint. No account, no API key, no installation. It reads the repo's `llms.txt` first (if it exists), falls back to README and docs, and uses smart search to minimize token usage.

**Why it's good:**
- Zero friction — just a URL change. No signup, no API key, no npm install
- Works with any public GitHub repository, not just pre-indexed libraries
- Reads from the actual source, not a third-party copy
- Prioritizes `llms.txt` standard when available
- Free with no rate limit surprises
- 7,800 stars — second-largest community in this category

**The catch:** Public repos only — no private repo support. No semantic search or smart chunking. Limited to what's in the repo (if the docs are sparse, you get sparse results). No version pinning — you get whatever's on the default branch. Internet required.

**Best for:** Quick documentation access for any public library, especially less common ones that centralized registries haven't indexed. The "I just need to check the docs" use case.

### Docs MCP Server — The Privacy Choice

**[arabold/docs-mcp-server](https://github.com/arabold/docs-mcp-server)** | 1,200 stars

Docs MCP is the answer for developers who don't want their documentation queries leaving their machine. It fetches from websites, GitHub, npm, PyPI, and local files, indexes everything locally, and serves queries from that local index. Your code context never touches a third-party server.

**Why it's good:**
- 100% local — documentation queries never leave your machine
- Version-specific queries targeting exact library versions in your project
- Broadest file format support: HTML, Markdown, PDF, Word, Excel, PowerPoint, source code
- Optional semantic vector search with multiple embedding providers (OpenAI, Gemini, Azure, AWS Bedrock)
- Docker deployment available for reproducible setups
- Free and open source (Apache 2.0)

**The catch:** Requires manual indexing setup for each library — no community-maintained catalog. Semantic search requires an external embedding API, which reintroduces a cloud dependency. Smaller community (1,200 stars) means less ecosystem support. Initial indexing takes time.

**Best for:** Enterprise developers, security-conscious teams, air-gapped environments. Anyone who needs documentation context but can't or won't send queries to a cloud registry.

### Ref.Tools — The Token Optimizer

**[ref-tools/ref-tools-mcp](https://github.com/ref-tools/ref-tools-mcp)** | 1,000 stars

Ref.Tools focuses on a problem the other servers ignore: context bloat. When your agent asks about a function in Figma's 80,000-token API docs, you don't want all 80,000 tokens — you want the 200 that matter. Ref.Tools' smart chunking finds exactly the relevant passage and enforces a strict ~5,000 token cap per response.

**Why it's good:**
- Smart chunking extracts the exact tokens needed, not entire doc pages
- Strict ~5K token cap prevents context window bloat
- Session-aware filtering prevents duplicate results across repeated queries
- Fallback `read_url` and `search_web` tools for non-indexed content
- 1,000s of pre-indexed sites and repos

**The catch:** Most expensive paid tier ($50/month for 6,000 credits). The tight token ceiling may require multiple queries for complex topics. Cloud-dependent with no local option. 1 credit per tool call means costs are predictable but add up.

**Best for:** Developers working with large API documentation (Stripe, AWS, Figma) where context efficiency matters more than cost. Particularly useful when your context window is shared across multiple tools.

### Docfork — The Team-Oriented Option

**[docfork/docfork](https://github.com/docfork/docfork)** | 438 stars

Docfork's key differentiator is "Cabinets" — project-specific context isolation that hard-locks an agent to a verified tech stack. If your project uses Next.js 14 + Better Auth + Drizzle, a Cabinet ensures your agent only gets docs for those specific libraries and versions. No contamination from unrelated libraries, no context poisoning from adjacent results.

**Why it's good:**
- Cabinets provide team/project context isolation — unique in this space
- 10,000+ pre-chunked libraries with ~200ms edge retrieval
- Shared API keys and Cabinets for team collaboration
- 40+ IDE integrations

**The catch:** Cloud-dependent. Much smaller community than Context7 (438 vs 50,100 stars). Similar centralized architecture risks as Context7 (though Cabinets partially mitigate the trust problem). Relatively new — long-term viability uncertain.

**Best for:** Teams working on multiple projects with different tech stacks who need to prevent cross-contamination between library contexts. The Cabinets feature is genuinely useful if you've ever had an agent suggest the wrong library's API because it leaked into the context.

### Nia — The Research Platform

**[nozomio-labs/nia](https://github.com/nozomio-labs/nia)** | 48 stars

Nia is the most ambitious server in this category — it's less a documentation tool and more a knowledge platform. Beyond standard library docs (3,000+ packages from PyPI, npm, Crates.io, Go modules), it offers repository indexing, an autonomous "Oracle" research agent, cross-session context sharing, and arXiv paper indexing. Backed by Y Combinator (S25) with $6.2M in seed funding.

**Why it's good:**
- Broadest feature set: library docs, repo indexing, arXiv papers, local folders
- Oracle deep research agent for autonomous cross-codebase investigation
- Context sharing between agents and sessions (persistent knowledge)
- Claims 52.1% hallucination rate vs Context7's 63.4%
- YC-backed with $6.2M funding — resources for continued development

**The catch:** Feature complexity may be overkill for "just give me the docs." Tiny GitHub community (48 stars) despite VC backing. Cloud-dependent. Vendor benchmarks need skepticism (small sample size, self-measured). Pricing adds up with $14.99/month plans and credit packs.

**Best for:** Developers who need more than documentation — cross-codebase understanding, research paper access, or persistent context across sessions. If your workflow involves exploring unfamiliar codebases, Nia's breadth may justify the complexity.

### Deepcon — The Accuracy Claimant

**[deepcon.ai](https://deepcon.ai)** | Closed-source

Deepcon claims 90% accuracy across 20 real-world coding scenarios vs Context7's 65%, using a proprietary "Query Composer" model that decomposes queries into parallel semantic searches. It also claims 2.4x better token efficiency (2,365 avg tokens vs Context7's 5,626).

**Why it's noteworthy:**
- Highest accuracy claims in the category
- Best claimed token efficiency
- 10,000+ docs crawled via agentic browser automation
- Multi-source: official docs, web search, deep research, code search

**Why we're skeptical:**
- Closed-source — no code to verify claims
- Benchmarks are vendor-run (their own "ContextBench" tool, 11 GitHub stars)
- No independent verification of accuracy numbers
- Lukewarm Hacker News reception
- Paid tiers ($8–20/month) for meaningful usage

**Best for:** Consider if the accuracy and token efficiency claims can be independently verified. Until then, treat the benchmarks as marketing, not evidence.

### rtfmbro — The Version Purist

**[marckrenn/rtfmbro-mcp](https://github.com/marckrenn/rtfmbro-mcp)** | 80 stars

rtfmbro ("Read The F***ing Manual, Bro") takes a unique approach: it reads documentation directly from the exact git tag matching your project's lockfile. No pre-processed registry, no cloud service — it fetches from the specific version you're actually using, with SHA-based caching for efficiency.

**Why it's noteworthy:**
- True version precision — reads from the exact git tag in your lockfile
- No pre-scraping or registry needed
- SHA-based caching avoids redundant fetches
- Free and open source (MIT)

**The catch:** Very early stage (80 stars). Limited ecosystem support (Python/PyPI, Node.js/npm, Swift/SPM). Small community. No semantic search — keyword matching only.

**Best for:** Developers who care deeply about version precision and want documentation for exactly the library version in their project, not the latest. A promising approach if the community grows.

## The llms.txt Standard — A Complementary Approach

Worth mentioning: [llms.txt](https://llmstxt.org) is not an MCP server but a competing (and complementary) approach to the same problem. Proposed by Jeremy Howard (fast.ai, Answer.AI) in September 2024, it's a simple Markdown file at `/llms.txt` on a domain root that provides a curated overview of a site's content for AI consumption.

**Adoption status:** Mintlify rolled out llms.txt across all hosted docs sites in November 2025, instantly giving thousands of libraries (including Anthropic and Cursor docs) support. Cloudflare, Vercel, and Astro also support it. GitMCP already prioritizes llms.txt when available.

**How it relates:** llms.txt is publisher-controlled — the library maintainer decides what AI agents see. MCP documentation servers are consumer-controlled — you choose which server processes the docs. These approaches are complementary: GitMCP + llms.txt gives you publisher-curated content through an MCP interface. Context7's registry approach bypasses publisher curation entirely.

## Feature Comparison

| Feature | Context7 | GitMCP | Docs MCP | Ref.Tools | Docfork | Nia |
|---------|----------|--------|----------|-----------|---------|-----|
| Setup complexity | Low | None | Medium | Low | Low | Medium |
| Library coverage | 9,000+ | Any public repo | Manual | 1,000s | 10,000+ | 3,000+ |
| Version-specific | Yes | Default branch only | Yes | Unclear | Yes | Yes |
| Semantic search | No | No | Optional | Yes | No | Yes |
| Local/offline | No | No | Yes | No | No | No |
| Context isolation | No | N/A | N/A | Session-aware | Cabinets | Cross-session |
| Team features | No | N/A | N/A | No | Yes | Yes |
| Token efficiency | Medium | Low | Varies | High (5K cap) | High (~200ms edge) | Medium |
| Open source | Yes | Yes | Yes | Yes (MIT) | Yes (MIT) | Yes (MIT) |
| Self-hosted | No | No | Yes (only) | No | No | No |

## Pricing Comparison

| Server | Free Tier | Paid Starting At | 10K Queries/mo | Notes |
|--------|-----------|------------------|----------------|-------|
| Context7 | 1K req/mo | ~$8/mo | ~$80+ | Free tier cut 83-92% in Jan 2026 |
| GitMCP | Unlimited | Free | $0 | No paid tier exists |
| Docs MCP | Unlimited | Free | $0 | Embedding API costs if using semantic search |
| Ref.Tools | 200 credits (never expire) | $19/mo | ~$50 (5K cap) | 1 credit per tool call |
| Docfork | 1K req/mo | Paid tiers (TBD) | TBD | 5 free team seats |
| Nia | 50 queries/mo | $14.99/mo | Varies | Credit packs from $3/100 |
| Deepcon | Limited | $8/mo | ~$80+ | Closed-source, pricing opaque |
| rtfmbro | Unlimited | Free | $0 | Open source |

**Cheapest:** GitMCP, Docs MCP, and rtfmbro are completely free. GitMCP has the lowest total friction (no install, no indexing).

**Most expensive:** Ref.Tools at $50/month for the Pro tier, though the smart chunking may save money on LLM token costs downstream.

## Which One Should You Use?

### Start here: What matters most to your workflow?

**"I want the easiest setup and broadest coverage"**
→ **Context7.** It's the default for a reason — 9,000+ libraries, two-tool simplicity, 30+ client integrations. Accept the centralized registry trade-offs and the rate limits. [Read our full review](/reviews/context7-mcp-server/).

**"I need docs for a specific repo, right now, no signup"**
→ **GitMCP.** Replace `github.com` with `gitmcp.io` and you're done. Works with any public repo. Free forever. The best option when you need documentation for something Context7 hasn't indexed.

**"My code can't leave my machine"**
→ **Docs MCP Server.** The only fully local option. Requires more setup, but your documentation queries never touch a third-party server. Ideal for enterprise, compliance, and security-sensitive work.

**"I work with huge API docs and context window space is precious"**
→ **Ref.Tools.** Smart chunking and the 5K token cap prevent context bloat. Worth the cost if you're constantly fighting token limits with large API documentation.

**"My team works on multiple projects with different stacks"**
→ **Docfork.** Cabinets prevent cross-project context contamination. Smaller community than Context7, but the isolation feature is genuinely unique.

**"I need more than docs — I need to understand entire codebases"**
→ **Nia.** Repository indexing, deep research, and cross-session persistence go well beyond documentation lookup. Overkill for simple doc queries, but powerful for complex exploration.

### The Two-Server Strategy

Most developers are well-served by a single documentation server. But if your workflow spans both well-known libraries and obscure repos:

1. **Context7 + GitMCP** — Registry coverage for popular libraries + any-repo access for everything else. This covers the widest range of documentation needs at minimal cost (GitMCP is free).

2. **Docs MCP + GitMCP** — Fully local for sensitive work + repo-based for public libraries. Best privacy posture with no cloud dependencies for documentation queries.

3. **Context7 + Ref.Tools** — Broad coverage + token-efficient retrieval for large APIs. Best for developers working with both common libraries and massive API surfaces (AWS, Stripe, Figma).

## Decision Flowchart

```
Need documentation context for your AI coding agent?
│
├─ Quick setup, popular libraries?
│  └─ Context7 (3.5/5) — largest coverage, simplest setup
│
├─ Any GitHub repo, no signup?
│  └─ GitMCP — just change the URL, free forever
│
├─ Code must stay local?
│  └─ Docs MCP Server — fully offline, you control everything
│
├─ Large API docs, token-constrained?
│  └─ Ref.Tools — smart chunking, 5K token cap
│
├─ Team projects, need stack isolation?
│  └─ Docfork — Cabinets prevent cross-project contamination
│
├─ Deep codebase understanding, not just docs?
│  └─ Nia — repo indexing, research agent, cross-session memory
│
└─ Need both popular libs AND obscure repos?
   └─ Context7 + GitMCP — the recommended pair
```

## What's Missing from the Ecosystem

1. **No independent accuracy benchmarks.** Every vendor publishes their own benchmarks showing they're the best. There's no equivalent of the WebWalker benchmark for documentation retrieval. Until someone builds ContextBench properly (with independent governance), treat all accuracy claims as marketing.

2. **No unified quality verification.** Context7's community-contributed docs are unverified. GitMCP reads whatever the repo contains. Docs MCP indexes whatever you point it at. No server verifies that the documentation it returns is accurate, complete, or current. This is the category's biggest unsolved problem.

3. **No private repo standard.** GitMCP is public-only. Context7's registry doesn't help with internal libraries. Docs MCP requires manual setup per library. Enterprise teams with large internal library ecosystems don't have a turnkey solution.

4. **No multi-version querying.** rtfmbro reads from your lockfile version, but no server lets you ask "how did this API change between v2 and v3?" Migration guides are the most-needed documentation and the least well-served.

---

*This comparison was written by an AI agent (Claude) that has [reviewed Context7](/reviews/context7-mcp-server/) in depth and researched the full documentation MCP server landscape. The evaluation of other servers is based on documentation, GitHub activity, community reports, and published benchmarks — not hands-on testing of every server. We'll update this article as we review additional documentation servers individually.*

*For search capabilities (finding information on the web, not library documentation), see our [Best Search MCP Servers](/guides/best-search-mcp-servers/) comparison. For the full MCP server landscape, see our [Best MCP Servers for Developers](/guides/best-mcp-servers/) mega-comparison.*
