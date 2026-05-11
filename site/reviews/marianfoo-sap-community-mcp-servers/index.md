# Marian Zeis's SAP Community MCP Servers — ABAP Documentation, ADT Integration, and SAP Notes

> Four community-built SAP MCP servers by independent consultant Marian Zeis (marianfoo): mcp-sap-docs (169 stars, hybrid BM25+semantic search, v0.3.21), abap-mcp-server (68 stars, unified ABAP/RAP search), arc-1 (48 stars, enterprise ADT v0.7.2), mcp-sap-notes (48 stars, Playwright-based). All Apache-2.0. Rating: 4.0/5.


SAP development has always had a documentation problem. ABAP has decades of keyword documentation scattered across SAP Help Portal, SAP Community, and proprietary Notes databases. SAPUI5 has thousands of components LLMs routinely hallucinate. The Cloud Application Programming Model has its own docs, CAP CDS has its own, and every SAP product has a separate knowledge base. SAP's **[official MCP servers](/reviews/sap-developer-tools-mcp-servers/)** address some of this — UI5, CAP, Fiori, and MDK — but they focus on toolchains, not on making SAP's documentation searchable to AI agents.

Marian Zeis, a self-employed SAP/UI5/ABAP consultant based in Bavaria, Germany, built the servers SAP's official team didn't. His four community-maintained MCP servers — mcp-sap-docs, abap-mcp-server, arc-1, and mcp-sap-notes — cover documentation aggregation, ABAP language reference, enterprise ABAP ADT integration, and SAP Notes retrieval. He also curates **sap-ai-mcp-servers**, a community list tracking 20+ SAP MCP servers across official and community sources. Part of our **[Developer Tools MCP category](/categories/developer-tools/)**.

The headline finding: **Zeis's collection is the most complete community response to SAP's MCP gap**, and mcp-sap-docs is the single best SAP documentation MCP server in existence. arc-1 is enterprise-grade. The weaker entries (abap-mcp-server without formal releases, mcp-sap-notes using Playwright) round out a collection where the top two servers are production-ready and the bottom two are valuable-but-rough.

---

## Overview

| Server | Stars | Version | Status | License |
|--------|-------|---------|--------|---------|
| [mcp-sap-docs](https://github.com/marianfoo/mcp-sap-docs) | 169 | v0.3.21 | Stable | Apache-2.0 |
| [abap-mcp-server](https://github.com/marianfoo/abap-mcp-server) | 68 | No releases | Active dev | Apache-2.0 |
| [arc-1](https://github.com/marianfoo/arc-1) | 48 | v0.7.2 (May 2, 2026) | Production-ready | Apache-2.0 |
| [mcp-sap-notes](https://github.com/marianfoo/mcp-sap-notes) | 48 | No releases | Community/beta | Apache-2.0 |

All four are TypeScript, installable via npm or Docker, and compatible with Claude Desktop, Claude Code, and Cursor. All are Apache-2.0.

**Who is Marian Zeis?** He is not a SAP employee — he runs IT Consulting Marian Zeis independently in Bavaria and has deep roots in the SAP developer community. He is an active SAP Community contributor and maintains a technical blog at blog.zeis.de covering ABAP code generation benchmarks, MCP implementation patterns, and the evolving SAP + AI integration ecosystem. His sap-ai-mcp-servers curated list is referenced in SAP Community posts and external MCP directories as a primary discovery resource.

---

## mcp-sap-docs — The Standout (169 Stars, v0.3.21)

| | |
|---|---|
| **Repo** | [marianfoo/mcp-sap-docs](https://github.com/marianfoo/mcp-sap-docs) |
| **Stars** | 169 |
| **Latest version** | v0.3.21 |
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

### Why 169 Stars

The gap mcp-sap-docs fills is real: SAP's own UI5 MCP server gives agents live access to UI5 APIs, but it covers UI5 only. CAP developers, ABAP developers, and Cloud SDK users have no equivalent official server. mcp-sap-docs fills all three with one install command. The `npx -y mcp-sap-docs` zero-configuration install — no server setup, no API keys, no Docker — makes it the lowest-friction SAP MCP server in the ecosystem.

### Limitations

The bundled index creates a trade-off: offline capability comes at the cost of freshness. SAP documentation updates between releases of the package won't be reflected until Zeis publishes a new version. For rapidly evolving areas like CAP annotations or new UI5 components, users may need to check when the index was last updated.

---

## arc-1 — Enterprise ABAP ADT Integration (v0.7.2)

| | |
|---|---|
| **Repo** | [marianfoo/arc-1](https://github.com/marianfoo/arc-1) |
| **Stars** | 48 |
| **Latest version** | v0.7.2 (May 2, 2026) |
| **License** | Apache-2.0 |
| **Language** | TypeScript (98%) |

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

arc-1 carries the most rigorous test suite of any server in this collection:
- **1,367+ unit tests**
- **~160 integration tests**
- **~70 end-to-end tests**

For a community-maintained MCP server, this level of test infrastructure is exceptional. The integration and E2E test counts in particular suggest the server has been validated against actual SAP systems, not just mocked. v0.7.2 (released May 2, 2026) is the most recent, indicating active iteration toward a v1.0 stable release.

### Limitations

arc-1 requires an ABAP ADT-enabled SAP system — either an on-premise system with ADT configured, or an SAP BTP ABAP Environment. This is not a public API; users need a licensed SAP system. The setup complexity is inherently higher than a documentation server.

---

## abap-mcp-server — Unified ABAP/RAP Search (68 Stars)

| | |
|---|---|
| **Repo** | [marianfoo/abap-mcp-server](https://github.com/marianfoo/abap-mcp-server) |
| **Stars** | 68 |
| **Hosted endpoint** | `mcp-abap.marianzeis.de/mcp` |
| **License** | Apache-2.0 |
| **Language** | TypeScript |
| **Releases** | None (162+ commits) |

abap-mcp-server is Zeis's ABAP-specific search and assistance server. Where mcp-sap-docs aggregates docs broadly, abap-mcp-server focuses specifically on the ABAP language: keyword documentation, the ABAP RESTful Application Programming (RAP) model, SAP Help Portal content, and SAP Community search.

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

## mcp-sap-notes — SAP Notes Search via Browser Automation (48 Stars)

| | |
|---|---|
| **Repo** | [marianfoo/mcp-sap-notes](https://github.com/marianfoo/mcp-sap-notes) |
| **Stars** | 48 |
| **License** | Apache-2.0 |
| **Language** | TypeScript |
| **Releases** | None |
| **Mechanism** | Playwright browser automation |

SAP Notes are SAP's proprietary knowledge base — correction instructions, workarounds, security patches, and support documentation, accessible to licensed SAP customers via the SAP Support Portal. They are not available via public API. mcp-sap-notes accesses them via browser automation using Playwright.

### What It Does

The server launches a headless browser, authenticates with the user's SAP Support Portal credentials (including 2FA support via OTP), and scrapes Notes and KBA (Knowledge Base Articles) content on demand. Results are cached via token caching to avoid repeated authentications. Docker deployment is supported, which helps contain the Playwright browser dependency.

This approach unlocks content that is otherwise invisible to AI agents: SAP Notes are behind the SAP support login, unavailable to any official API. For SAP consultants whose daily workflow includes searching Notes for known issues and patches, this is a genuine capability gap that mcp-sap-notes fills.

### Limitations

Browser automation against private APIs is inherently fragile:
- SAP Support Portal UI changes break the scraper
- Session timeouts require re-authentication
- Playwright adds significant resource overhead compared to API-based servers

The repository includes a compliance note: users are responsible for ensuring their use of the SAP Notes content complies with their SAP license agreement. SAP's terms around automated access to the Support Portal vary by contract — organizations in regulated environments should review this before deploying.

The combination of no formal releases, Playwright dependency, and compliance ambiguity makes mcp-sap-notes the roughest of the four servers. It is, however, solving a problem that no official API can solve — the content genuinely exists nowhere else as an accessible MCP resource.

---

## sap-ai-mcp-servers — The Curated Ecosystem List

Beyond his four servers, Zeis maintains **[marianfoo/sap-ai-mcp-servers](https://github.com/marianfoo/sap-ai-mcp-servers)** — a community list tracking 20+ SAP MCP servers across official SAP orgs and community maintainers. This serves as the primary discovery resource for the SAP MCP ecosystem, referenced in SAP Community posts and several external MCP directories.

The list includes SAP's official servers (UI5, CAP, Fiori, MDK), community servers like his own, and enterprise tools from vendors building MCP connectivity into SAP systems. For anyone evaluating the SAP MCP landscape, it is the most complete single-source inventory available.

---

## What Works Well

**mcp-sap-docs fills a real gap.** SAP's official servers don't aggregate cross-product documentation. mcp-sap-docs does, with a zero-install npx command and offline-capable search. The 169-star count reflects genuine adoption by a developer community that needed this.

**arc-1's test infrastructure is exceptional.** 1,367+ unit tests plus integration and E2E coverage for a community-maintained MCP server is rare. It signals Zeis has validated arc-1 against real SAP systems and intends to maintain API stability as the project evolves toward v1.0.

**Ecosystem curation.** sap-ai-mcp-servers positions Zeis as a knowledge hub for the entire SAP MCP community, not just his own servers. This community role gives his work broader visibility and credibility.

**All Apache-2.0.** Enterprise-friendly licensing across the entire collection.

---

## Limitations

**Uneven release maturity.** Only mcp-sap-docs (v0.3.21) and arc-1 (v0.7.2) have formal releases. abap-mcp-server and mcp-sap-notes have no versioning — users get whatever is on the main branch, with no stability guarantees.

**mcp-sap-notes fragility.** Playwright-based scraping of a private API portal is inherently maintenance-intensive. A single SAP Support Portal redesign can break the integration.

**Single maintainer.** All four servers depend on one person. There are no public contributors of note beyond Zeis. For enterprise deployments, maintainer bus risk is real.

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

*This review covers the state of these projects as of May 2026. No hands-on testing was performed; findings are based on repository inspection, documentation review, and published technical sources. Marian Zeis is not affiliated with SAP SE. See our **[SAP Developer Tools review](/reviews/sap-developer-tools-mcp-servers/)** for SAP's official MCP servers.*

