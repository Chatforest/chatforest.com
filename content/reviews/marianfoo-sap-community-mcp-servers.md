---
title: "Marian Zeis's SAP Community MCP Servers — ABAP Documentation, ADT Integration, and SAP Notes"
date: 2026-05-05T21:00:00+09:00
description: "Four community-built SAP MCP servers by independent consultant Marian Zeis (marianfoo): mcp-sap-docs (216 stars, hybrid BM25+semantic search, v0.3.53), abap-mcp-server (86 stars, unified ABAP/RAP search), arc-1 (167 stars, now under org arc-mcp, MIT-licensed, v1.1.0), mcp-sap-notes (56 stars, Playwright-based, being archived in favor of a monorepo). Rating: 4.0/5."
og_description: "Community SAP MCP servers by Marian Zeis: mcp-sap-docs (216 stars, offline-capable BM25+semantic SAP docs search, v0.3.53), abap-mcp-server (86 stars, ABAP/RAP + community search, hosted endpoint), arc-1 (167 stars, enterprise ADT, 3,474+ unit tests, v1.1.0, MIT), mcp-sap-notes (56 stars, Playwright-based SAP Notes search, archiving to a monorepo). Rating: 4.0/5."
content_type: "Review"
card_description: "Where SAP's official MCP servers cover developer tooling (UI5, CAP, Fiori, MDK), independent consultant Marian Zeis has built four community servers that fill the gaps SAP left open — ABAP documentation search, enterprise ADT integration, and SAP Notes retrieval. The standout is mcp-sap-docs (216 stars, v0.3.53): a hybrid BM25 + semantic search engine covering UI5, CAP, ABAP, and Cloud SDK docs, installable in one npx command with offline capability. arc-1 (v1.1.0, Aug 2026, now maintained under the arc-mcp org and MIT-licensed) is the most technically mature: enterprise ABAP ADT integration with 3,474+ unit tests, OAuth 2.0/XSUAA auth, and SAP BTP support, past its v1.0 milestone. abap-mcp-server provides unified ABAP keyword and RAP search plus a public hosted MCP endpoint. mcp-sap-notes accesses SAP's private Notes/KBA API via Playwright — powerful but fragile, and its standalone repo is being archived in favor of a monorepo. Zeis also curates sap-ai-mcp-servers, a community list now tracking 100+ SAP MCP servers, AI skills, and Claude plugins ecosystem-wide. Rating: 4.0/5 — serious technical depth from a credible community maintainer; deducted for uneven release maturity and Playwright fragility."
last_refreshed: 2026-08-22
sources_audited: 2026-08-22
---

SAP development has always had a documentation problem. ABAP has decades of keyword documentation scattered across SAP Help Portal, SAP Community, and proprietary Notes databases. SAPUI5 has thousands of components LLMs routinely hallucinate. The Cloud Application Programming Model has its own docs, CAP CDS has its own, and every SAP product has a separate knowledge base. SAP's **[official MCP servers](/reviews/sap-developer-tools-mcp-servers/)** address some of this — UI5, CAP, Fiori, and MDK — but they focus on toolchains, not on making SAP's documentation searchable to AI agents.

Marian Zeis, a self-employed SAP/UI5/ABAP consultant based in Bavaria, Germany, built the servers SAP's official team didn't. His four community-maintained MCP servers — mcp-sap-docs, abap-mcp-server, arc-1, and mcp-sap-notes — cover documentation aggregation, ABAP language reference, enterprise ABAP ADT integration, and SAP Notes retrieval. He also curates **[sap-ai-mcp-servers](https://github.com/marianfoo/sap-ai-mcp-servers)**, a community list that as of August 2026 tracks **100+ entries** — SAP MCP servers plus adjacent AI skills, Claude plugins, and SDKs — up from roughly 20 when this review was first published in May 2026. Part of our **[Developer Tools MCP category](/categories/developer-tools/)**.

The headline finding: **Zeis's collection is the most complete community response to SAP's MCP gap**, and mcp-sap-docs is the single best SAP documentation MCP server in existence. arc-1 is enterprise-grade. The weaker entries (abap-mcp-server without formal releases, mcp-sap-notes using Playwright) round out a collection where the top two servers are production-ready and the bottom two are valuable-but-rough.

---

## Overview

*Table updated 2026-08-22 with live GitHub data; see [update notes](#update-notes-2026-08-22) below for what changed since the original May 2026 review.*

| Server | Stars | Version | Status | License |
|--------|-------|---------|--------|---------|
| [mcp-sap-docs](https://github.com/marianfoo/mcp-sap-docs) | 216 | v0.3.53 | Stable | Apache-2.0 |
| [abap-mcp-server](https://github.com/marianfoo/abap-mcp-server) | 86 | No releases (177 commits) | Active dev | Apache-2.0 |
| [arc-1](https://github.com/arc-mcp/arc-1) | 167 | v1.1.0 (Aug 18, 2026) | Production-ready (past v1.0) | MIT |
| [mcp-sap-notes](https://github.com/marianfoo/mcp-sap-notes) | 56 | v0.3.1 | Archiving — see below | Apache-2.0 |

mcp-sap-docs, abap-mcp-server, and mcp-sap-notes are TypeScript, installable via npm or Docker, and compatible with Claude Desktop, Claude Code, and Cursor. arc-1 has since moved to a dedicated GitHub org, [arc-mcp](https://github.com/arc-mcp), and its license changed from Apache-2.0 to MIT along with the move — [confirmed in its current LICENSE file](https://github.com/arc-mcp/arc-1/blob/main/LICENSE). Zeis (GitHub handle `marianfoo`) remains by far the dominant contributor to arc-1 under the new org — [430 of the repo's commits are his](https://github.com/arc-mcp/arc-1/graphs/contributors), versus single digits for anyone else.

### Update notes (2026-08-22)

This review was originally published May 2026 and audited claim-by-claim again on 2026-08-22. Since original publication:

- **arc-1 moved to the `arc-mcp` GitHub organization** and relicensed from Apache-2.0 to MIT. It also crossed its [v1.0.0 milestone on July 31, 2026](https://github.com/arc-mcp/arc-1/releases/tag/v1.0.0) and reached [v1.1.0 on August 18, 2026](https://github.com/arc-mcp/arc-1/releases/tag/v1.1.0) — the "toward v1.0" framing in the original review is now out of date; it is a stable, versioned 1.x release.
- **mcp-sap-notes is being archived.** [Its README now states](https://github.com/marianfoo/mcp-sap-notes) active development has moved to `marianfoo/sap-mcp-servers`, a monorepo, where the notes server lives at `packages/notes`. The standalone repo hasn't been pushed to since June 2, 2026.
- **sap-ai-mcp-servers has grown roughly 5x**, from ~20 tracked entries to [100+ as of its August 22, 2026 "last generated" date](https://github.com/marianfoo/sap-ai-mcp-servers), and its scope now explicitly includes AI skills and Claude plugins, not just MCP servers.
- Star counts and mcp-sap-docs's version number are updated throughout this page to reflect live GitHub data as of 2026-08-22.

**Who is Marian Zeis?** He is not a SAP employee — he runs [IT Consulting Marian Zeis](https://github.com/marianfoo) independently in Bavaria and has deep roots in the SAP developer community. He is an active SAP Community contributor and maintains a technical blog at [blog.zeis.de](https://blog.zeis.de) covering ABAP code generation benchmarks, MCP implementation patterns, and the evolving SAP + AI integration ecosystem. His sap-ai-mcp-servers curated list is referenced in SAP Community posts and external MCP directories as a primary discovery resource.

---

## mcp-sap-docs — The Standout (216 Stars, v0.3.53)

| | |
|---|---|
| **Repo** | [marianfoo/mcp-sap-docs](https://github.com/marianfoo/mcp-sap-docs) |
| **Stars** | 216 |
| **Latest version** | v0.3.53 |
| **Install** | `npx -y mcp-sap-docs` |
| **License** | Apache-2.0 |
| **Language** | TypeScript |

mcp-sap-docs is the most starred of Zeis's servers and the most immediately useful for any SAP developer working with AI coding assistants. It aggregates documentation from multiple SAP sources — SAP Help Portal (UI5, CAP, ABAP, Cloud SDK), SAP Community content, and more — into a single searchable MCP tool interface.

### What It Does

The server provides a **hybrid BM25 + semantic search** engine over SAP documentation. BM25 gives precise keyword matching (critical when you need exact API names, CDS annotations, or ABAP keywords); semantic search finds conceptually related content when the exact term is unknown. The combination addresses the core failure mode of SAP documentation queries: AI agents either over-match on exact keywords or drift semantically into wrong APIs.

**Two variants are available:**
- **Full scope** — searches across UI5, CAP, ABAP, Cloud SDK, and SAP Help Portal content
- **ABAP-focused** — a leaner variant scoped to ABAP keyword documentation and the ABAP feature matrix

Both variants support **offline operation** — the documentation index is bundled with the package, so queries don't require network access to SAP's servers at query time. This is a significant operational advantage for air-gapped environments, restricted networks, or simply for query latency.

### Why 216 Stars

The gap mcp-sap-docs fills is real: SAP's own UI5 MCP server gives agents live access to UI5 APIs, but it covers UI5 only. CAP developers, ABAP developers, and Cloud SDK users have no equivalent official server. mcp-sap-docs fills all three with one install command. The `npx -y mcp-sap-docs` zero-configuration install — no server setup, no API keys, no Docker — makes it the lowest-friction SAP MCP server in the ecosystem. The [current README](https://github.com/marianfoo/mcp-sap-docs) confirms the hybrid **BM25 + semantic search** (fused via Reciprocal Rank Fusion) and offline-capable local index are still the core architecture as of this audit.

### Limitations

The bundled index creates a trade-off: offline capability comes at the cost of freshness. SAP documentation updates between releases of the package won't be reflected until Zeis publishes a new version. For rapidly evolving areas like CAP annotations or new UI5 components, users may need to check when the index was last updated.

---

## arc-1 — Enterprise ABAP ADT Integration (v1.1.0)

| | |
|---|---|
| **Repo** | [arc-mcp/arc-1](https://github.com/arc-mcp/arc-1) (moved from `marianfoo/arc-1` to the new `arc-mcp` org in June 2026) |
| **Stars** | 167 |
| **Latest version** | v1.1.0 (Aug 18, 2026) |
| **License** | MIT (changed from Apache-2.0 after the org move) |
| **Language** | TypeScript |

arc-1 is Zeis's most technically ambitious project: a production-grade MCP server for ABAP Development Tools (ADT) integration. ABAP ADT is the Eclipse-based and VS Code framework through which developers interact with on-premise SAP systems and SAP BTP ABAP environments — running programs, managing transports, browsing the ABAP repository, editing code. arc-1 exposes this capability to AI agents via MCP.

### What It Does

arc-1 connects to SAP ABAP systems via the ADT REST API and exposes operations for:
- **Repository browsing** — navigate the ABAP repository structure, list packages, classes, and programs
- **Object management** — read and write ABAP source code objects
- **Transport management** — create and manage CTS (Change and Transport System) requests
- **Feature detection** — probe which ADT features the connected SAP system supports, adapting to different SAP versions and releases

### Authentication

arc-1 supports four authentication modes:
- **API key** — simple token-based for service accounts
- **OIDC** — OpenID Connect for modern identity provider integration
- **OAuth 2.0** — standard OAuth flows
- **XSUAA** — SAP's extended services for User Account and Authentication on BTP

Multi-auth support is unusual for a community MCP server; most community tools support one or two methods. XSUAA support in particular requires understanding SAP BTP's specific OAuth implementation, which is non-trivial to implement correctly. The presence of proper XSUAA support signals Zeis has implemented this against real BTP environments.

### Test Coverage

arc-1 carries [the most rigorous test suite](https://github.com/arc-mcp/arc-1#testing) of any server in this collection, and the current README still reports the same figures verified for this audit:
- **3,474 unit tests** across 104 unit test files (mocked HTTP)
- **262 integration tests** (default integration profile against live SAP systems)
- **141 end-to-end tests** (default E2E profile executing real MCP tool calls against a running arc-1 server and live SAP system)

For a community-maintained MCP server, this level of test infrastructure is exceptional. The integration and E2E test counts in particular suggest the server has been validated against actual SAP systems, not just mocked. The project has since passed the v1.0 milestone the original review anticipated: [v1.0.0 shipped July 31, 2026](https://github.com/arc-mcp/arc-1/releases/tag/v1.0.0), and the latest release, [v1.1.0, shipped August 18, 2026](https://github.com/arc-mcp/arc-1/releases/tag/v1.1.0).

### Limitations

arc-1 requires an ABAP ADT-enabled SAP system — either an on-premise system with ADT configured, or an SAP BTP ABAP Environment. This is not a public API; users need a licensed SAP system. The setup complexity is inherently higher than a documentation server.

---

## abap-mcp-server — Unified ABAP/RAP Search (86 Stars)

| | |
|---|---|
| **Repo** | [marianfoo/abap-mcp-server](https://github.com/marianfoo/abap-mcp-server) |
| **Stars** | 86 |
| **Hosted endpoint** | `mcp-abap.marianzeis.de/mcp` |
| **License** | Apache-2.0 |
| **Language** | TypeScript |
| **Releases** | None (177 commits as of this audit) |

abap-mcp-server is Zeis's ABAP-specific search and assistance server. Where mcp-sap-docs aggregates docs broadly, abap-mcp-server focuses specifically on the ABAP language: keyword documentation, the ABAP RESTful Application Programming (RAP) model, SAP Help Portal content, and SAP Community search. [The current README](https://github.com/marianfoo/abap-mcp-server) describes it explicitly as "the ABAP-focused downstream variant generated from upstream `mcp-sap-docs`" and states the repo is synchronized from that upstream project — it is a generated, ABAP-scoped build of mcp-sap-docs rather than an independently written codebase, which the original review did not make clear.

### What It Does

The server provides unified search across:
- **ABAP keyword documentation** — precise language reference for ABAP statements, built-in functions, and standard library classes
- **ABAP RAP model** — documentation for the RESTful Application Programming model used in modern ABAP development on BTP
- **SAP Help Portal** — SAP's official documentation portal, cross-searched with keyword content
- **SAP Community** — relevant community posts and discussions alongside official docs

It also includes an **ABAP feature matrix** — a structured reference to which ABAP language features are available on which SAP system versions. This matters because ABAP evolves differently between on-premise S/4HANA, SAP BTP ABAP Environment, and legacy ERP systems. Feature matrix access prevents agents from suggesting syntax that's valid on BTP but not on an older on-premise release.

**Local linting integration** — the server can invoke ABAP linting tools locally, allowing agents to validate ABAP code quality within an MCP tool call.

### Public Hosted Endpoint

Zeis offers a public hosted endpoint at `mcp-abap.marianzeis.de/mcp` — usable without any local setup. This zero-friction path is unusual; most community MCP servers require local installation. The hosted endpoint allows SAP developers to trial the server immediately in Claude Desktop or any MCP client that supports HTTP MCP endpoints.

### Limitations

162+ commits but no formal releases is a double-edged situation: active development, but no semantic versioning guarantees. Users consuming the hosted endpoint or installing from npm will get whatever the current main branch state is. For production agentic workflows where stability matters, this is a risk.

---

## mcp-sap-notes — SAP Notes Search via Browser Automation (56 Stars, Archiving)

| | |
|---|---|
| **Repo** | [marianfoo/mcp-sap-notes](https://github.com/marianfoo/mcp-sap-notes) |
| **Stars** | 56 |
| **License** | Apache-2.0 |
| **Language** | TypeScript |
| **Releases** | v0.3.1 (May 28, 2026) |
| **Mechanism** | Playwright browser automation |
| **Status (Aug 2026)** | Being archived — development moved to [marianfoo/sap-mcp-servers](https://github.com/marianfoo/sap-mcp-servers) (`packages/notes`) |

SAP Notes are SAP's proprietary knowledge base — correction instructions, workarounds, security patches, and support documentation, accessible to licensed SAP customers via the SAP Support Portal. They are not available via public API. mcp-sap-notes accesses them via browser automation using Playwright.

> **Update (2026-08-22):** [The repo's README now carries an archival notice](https://github.com/marianfoo/mcp-sap-notes): "This repository is being archived. Active development has moved to `marianfoo/sap-mcp-servers`, where this server now lives in `packages/notes`." The standalone repo hasn't been pushed to since June 2, 2026, while the [monorepo](https://github.com/marianfoo/sap-mcp-servers) (created May 29, 2026) is where new issues and pull requests should go. New installs should target the monorepo path, not this standalone repo.

### What It Does

The server launches a headless browser, authenticates with the user's SAP Support Portal credentials via username/password or SAP Passport certificate (with manual MFA/2FA code entry in headful mode), and scrapes Notes and KBA (Knowledge Base Articles) content on demand. Session cookies are cached locally to avoid repeated authentications. Docker deployment is supported, which helps contain the Playwright browser dependency.

This approach unlocks content that is otherwise invisible to AI agents: SAP Notes are behind the SAP support login, unavailable to any official API. For SAP consultants whose daily workflow includes searching Notes for known issues and patches, this is a genuine capability gap that mcp-sap-notes fills.

### Limitations

Browser automation against private APIs is inherently fragile:
- SAP Support Portal UI changes break the scraper
- Session timeouts require re-authentication
- Playwright adds significant resource overhead compared to API-based servers

The repository includes a compliance note: users are responsible for ensuring their use of the SAP Notes content complies with their SAP license agreement. SAP's terms around automated access to the Support Portal vary by contract — organizations in regulated environments should review this before deploying.

The combination of thin release history (one tag, v0.3.1), Playwright dependency, compliance ambiguity, and the repo's own August 2026 archival notice makes mcp-sap-notes the roughest of the four servers — and the one in the most flux. It is, however, solving a problem that no official API can solve — the content genuinely exists nowhere else as an accessible MCP resource, and that capability is expected to continue under the `marianfoo/sap-mcp-servers` monorepo.

---

## sap-ai-mcp-servers — The Curated Ecosystem List

Beyond his four servers, Zeis maintains **[marianfoo/sap-ai-mcp-servers](https://github.com/marianfoo/sap-ai-mcp-servers)** — a community list that as of its August 22, 2026 "last generated" timestamp tracks **100+ entries**: SAP MCP servers across official SAP orgs and community maintainers, plus adjacent AI skills, Claude plugins, and SDKs (grown roughly 5x from ~20 entries at this review's original May 2026 publication). This serves as the primary discovery resource for the SAP MCP ecosystem, referenced in SAP Community posts and several external MCP directories, and is also browsable via an [interactive catalog](https://sap-ai-tools.marianzeis.de/).

The list includes SAP's official servers (UI5, CAP, Fiori, MDK), community servers like his own, and enterprise tools from vendors building MCP connectivity into SAP systems. For anyone evaluating the SAP MCP landscape, it is the most complete single-source inventory available.

---

## What Works Well

**mcp-sap-docs fills a real gap.** SAP's official servers don't aggregate cross-product documentation. mcp-sap-docs does, with a zero-install npx command and offline-capable search. The 216-star count (as of this audit) reflects genuine adoption by a developer community that needed this.

**arc-1's test infrastructure is exceptional.** [3,474 unit tests plus 262 integration and 141 E2E tests](https://github.com/arc-mcp/arc-1#testing) for a community-maintained MCP server is rare. It signals Zeis has validated arc-1 against real SAP systems and has since delivered on that trajectory — the project [passed v1.0.0 on July 31, 2026](https://github.com/arc-mcp/arc-1/releases/tag/v1.0.0).

**Ecosystem curation.** sap-ai-mcp-servers positions Zeis as a knowledge hub for the entire SAP MCP community, not just his own servers — a role that has grown, not shrunk, since this review's original publication (the list is now 5x its original size). This community role gives his work broader visibility and credibility.

**Mostly permissive open-source licensing.** mcp-sap-docs, abap-mcp-server, and mcp-sap-notes remain Apache-2.0; arc-1 is now MIT after its June 2026 move to the `arc-mcp` org. Both are enterprise-friendly.

---

## Limitations

**Uneven release maturity.** mcp-sap-docs (v0.3.53) and arc-1 (v1.1.0, now past its v1.0 milestone) have active, formal release cadences; mcp-sap-notes has shipped only one tag (v0.3.1) and is being folded into a monorepo; abap-mcp-server has no versioning at all — users get whatever is on the main branch, with no stability guarantees.

**mcp-sap-notes fragility, and now churn.** Playwright-based scraping of a private API portal is inherently maintenance-intensive. A single SAP Support Portal redesign can break the integration, and as of August 2026 the repository itself is mid-migration to a new monorepo, adding near-term instability on top of the scraping fragility.

**Single maintainer (largely still true, with one caveat).** mcp-sap-docs, abap-mcp-server, and mcp-sap-notes remain effectively one-person projects. arc-1's [current LICENSE file lists a second copyright holder](https://github.com/arc-mcp/arc-1/blob/main/LICENSE) alongside Zeis, but Zeis is still overwhelmingly the dominant contributor by commit count. For enterprise deployments, maintainer bus risk remains real across the collection.

**abap-mcp-server vs. mcp-sap-docs overlap.** Both servers cover ABAP documentation. The distinction is meaningful — abap-mcp-server goes deeper on RAP and community content while mcp-sap-docs covers breadth — but users may find it unclear which to reach for.

---

## Who Should Use These

**mcp-sap-docs** — any SAP developer working with Claude, Cursor, or another AI coding assistant who uses CAP, UI5, ABAP, or Cloud SDK. Install it with a single npx command; it immediately reduces hallucination on SAP APIs.

**arc-1** — ABAP developers who need agents to interact with actual SAP systems (on-premise or BTP). Requires ADT-enabled system access; not a documentation tool.

**abap-mcp-server** — ABAP/RAP developers who want deeper language reference and community content search, especially if they prefer the hosted public endpoint to a local installation.

**mcp-sap-notes** — SAP consultants who regularly search Notes for known issues and patches, comfortable with the Playwright dependency and who have reviewed their license agreement. Not for casual use.

---

## Compared to SAP's Official Servers

SAP's **[official MCP servers](/reviews/sap-developer-tools-mcp-servers/)** (UI5, CAP, Fiori, MDK) focus on toolchain integration — they help agents build UI5 apps, scaffold CAP projects, generate Fiori elements, and create MDK mobile apps. They come from SAP engineering teams with organizational backing.

Zeis's servers focus on what SAP's official team left out: **making SAP's documentation machine-readable** (mcp-sap-docs, abap-mcp-server), **connecting to on-premise ABAP systems** (arc-1), and **unlocking proprietary knowledge bases** (mcp-sap-notes). The two collections are complementary, not competing. An SAP developer working with AI agents benefits from deploying both the official servers and mcp-sap-docs as a baseline, with arc-1 added if they work with on-premise or BTP ABAP.

---

## Rating: 4.0 / 5

mcp-sap-docs alone would rate 4.5/5 — it is production-ready, fills a genuine gap, and has real adoption. arc-1 is technically impressive with enterprise-grade test coverage. The collection as a whole earns 4.0/5: the top two servers are strong enough to recommend without reservation, and the bottom two (abap-mcp-server, mcp-sap-notes) add meaningful capability despite their rough edges. The single-maintainer risk and missing releases on two of four servers prevent a higher rating.

For SAP developers building agentic workflows in 2026, Marian Zeis's collection is the essential community complement to SAP's official MCP offering. Start with mcp-sap-docs. Add arc-1 if you work with ABAP systems directly.

---

*This review was originally published in May 2026 and re-audited claim-by-claim against live sources on 2026-08-22 (see [update notes](#update-notes-2026-08-22)). No hands-on testing was performed; findings are based on repository inspection, documentation review, and published technical sources. Marian Zeis is not affiliated with SAP SE. See our **[SAP Developer Tools review](/reviews/sap-developer-tools-mcp-servers/)** for SAP's official MCP servers.*
