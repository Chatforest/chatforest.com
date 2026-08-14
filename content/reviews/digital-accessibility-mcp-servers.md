---
title: "Digital Accessibility MCP Servers — A11y Auditing, WCAG Compliance, Color Contrast, Lighthouse, and More"
date: 2026-03-16T05:00:00+09:00
description: "Digital accessibility MCP servers let AI agents audit web pages for WCAG compliance, check color contrast ratios, fix accessibility violations, and reference ARIA patterns through"
og_description: "Digital accessibility MCP servers: Deque Official axe MCP (enterprise, paid), BrowserStack MCP (150 stars, WCAG 2.2), a11ymcp (89 stars, 6 tools), mcp-accessibility-scanner (56 stars, 40+ tools), accessibility-agents (390 stars, 79 agents), Lighthouse MCP (67 stars, 13+ tools). 20+ servers reviewed. Rating: 4.5/5."
content_type: "Review"
card_description: "Digital accessibility MCP servers for WCAG compliance auditing, color contrast checking, accessibility remediation, and ARIA pattern reference. **Deque has launched their official axe MCP Server** — the biggest gap from our initial review is now closed, with enterprise-grade accessibility testing and AI-powered remediation available to all Axe DevTools for Web customers (proprietary, paid). **BrowserStack MCP Server enters the space** — 150 stars, 44 tools including accessibility scanning with their Spectra™ rule engine and WCAG 2.2 compliance — the first enterprise platform with dedicated a11y MCP tooling. **accessibility-agents surges to 390 stars** — holding at 79 specialized agents across eight teams and five platforms (Claude Code, GitHub Copilot, Gemini CLI, Codex CLI, MCP Server), now covering education/standards and desktop accessibility. **a11ymcp grows to 89 stars** with 10,000+ downloads. **mcp-accessibility-scanner reaches 56 stars** with 508 commits. **Lighthouse MCP hits 67 stars** with 234 commits. **New community servers** — plexusone/agent-a11y (Go, LLM-as-a-Judge false positive reduction, VPAT reports), yashpreetbathla/mcp-accessibility-bridge (9 stars, Chrome accessibility tree exposure for selector generation), tsmd/wcag-mcp (WCAG documentation reference). **Gaps still open** — Deque gap closed (paid), but the benoberkfell/android-a11y-mcp server we previously flagged as closing the native-mobile gap has been removed from GitHub (404 as of 2026-08-14) and is no longer available, so native mobile accessibility via MCP remains unaddressed. VPAT generation is now available standalone via agent-a11y. Still missing: WAVE/Pa11y MCP, native mobile a11y MCP, iOS VoiceOver, screen reader simulation, cognitive accessibility tools. Rating upgraded 4→4.5/5 — the ecosystem has matured from community-only to community + enterprise, with Deque and BrowserStack validating the category."
last_refreshed: 2026-08-14
sources_audited: 2026-08-14
---

Digital accessibility MCP servers are making inclusive web development more achievable by giving AI agents the ability to audit web pages for WCAG compliance, check color contrast ratios, fix accessibility violations automatically, and reference ARIA patterns — all through the Model Context Protocol. Instead of manually running audit tools, interpreting cryptic violation reports, and searching for remediation guidance, these servers let AI assistants handle accessibility workflows from detection through remediation.

This review covers **digital accessibility MCP servers** — comprehensive audit platforms (axe-core and Playwright-based scanners), color contrast checkers, Lighthouse integration, accessibility agent frameworks, and ARIA/WCAG reference servers. For broader web quality auditing, see our [Web Scraping & Automation review](/reviews/web-scraping-crawling-mcp-servers/). For design system accessibility, see our [UI/UX & Design review](/guides/best-design-mcp-servers/).

The headline findings: **Deque has launched their official axe MCP Server** — enterprise-grade accessibility testing with AI-powered remediation, available to Axe DevTools for Web customers (proprietary, paid). **BrowserStack's MCP Server** (150 stars, 44 tools) includes accessibility scanning with WCAG 2.2 support. **ronantakizawa/a11ymcp leads open-source with 89 stars** and 6 tools covering WCAG 2.0/2.1/2.2. **Community-Access/accessibility-agents surges to 390 stars** with 79 agents across eight teams. The native mobile a11y MCP server we flagged in an earlier revision of this review (benoberkfell/android-a11y-mcp) has since been removed from GitHub — see [What's Missing](#whats-missing).

**Category:** [Developer Tools](/categories/developer-tools/)

---

## Enterprise & Official Platforms

### dequelabs/axe-mcp-server — Deque's Official axe MCP Server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [axe-mcp-server-public](https://github.com/dequelabs/axe-mcp-server-public) | 6 | — | Proprietary | 2 |

**The biggest gap from our initial review is now closed** — Deque, the creators of axe-core, have launched their official MCP server. [First introduced at Axe-con 2025 and now included in the Axe DevTools for Web bundle at no additional cost](https://www.deque.com/blog/axe-devtools-for-web-now-includes-axe-mcp-server-for-earlier-fixes-and-faster-delivery/), with [further technical detail from Deque's engineering team](https://www.deque.com/blog/a-closer-look-at-axe-mcp-server/):

- **analyze** — comprehensive accessibility scans using axe in a real browser environment (via the axe DevTools Browser Extension)
- **remediate** — AI-powered, code-level guidance to fix accessibility issues
- Works with **Claude, GitHub Copilot, Cursor, Windsurf, VS Code**, and any MCP-compatible client
- Requires Docker and a **paid Axe DevTools for Web subscription** (included in bundle at no additional cost)
- **Privacy-focused** — [Deque states it acts only as a data processor, never a controller, so customer data is never used to train models](https://www.deque.com/axe/mcp-server/)
- Scans both local development URLs and remote production URLs

The proprietary/paid nature limits adoption compared to open-source alternatives, but having the axe-core creators' official blessing adds credibility to the entire ecosystem. Enterprise teams with existing Deque subscriptions get this effectively free.

### browserstack/mcp-server — Enterprise Accessibility Testing

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [browserstack/mcp-server](https://github.com/browserstack/mcp-server) | 150 | TypeScript | — | 44 |

**The first enterprise testing platform with dedicated accessibility MCP tooling** — BrowserStack's official MCP server includes, [per its own README](https://github.com/browserstack/mcp-server), a dedicated accessibility toolset powered by [BrowserStack's Spectra™ rule engine](https://www.browserstack.com/accessibility-testing/accessibility-devtools/mcp-server):

- **startAccessibilityScan** — automated WCAG compliance scans using BrowserStack's Spectra™ rule engine
- **accessibilityExpert** — [AI expert guidance](https://www.browserstack.com/docs/browserstack-mcp-server/tools/accessibility) on WCAG 2.0/2.1/2.2 and accessibility best practices
- **AI-generated contextual code fixes** — production-ready remediation suggestions
- Works with **Claude, GitHub Copilot, Cursor** via one-click setup
- Also covers test management, browser automation, and cross-device testing beyond just accessibility
- Requires BrowserStack credentials (paid platform)

The 44 tools span far beyond accessibility (test cases, automated testing, live sessions); only a handful are accessibility-specific. Note: BrowserStack does offer a [PDF accessibility scanner](https://www.browserstack.com/accessibility-testing/pdf-scanner) (WCAG 2.2 / PDF/UA-2), but it is a separate dashboard product — as of this audit it is **not** exposed as an MCP tool in the `browserstack/mcp-server` README, so we've removed the "PDF via MCP" claim from an earlier revision of this review.

---

## Comprehensive Audit Platforms

### ronantakizawa/a11ymcp — The Most Popular Open-Source A11y MCP Server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [a11ymcp](https://github.com/ronantakizawa/a11ymcp) | 89 | JavaScript | MIT | 6 |

**The most downloaded accessibility MCP server** ([10,000+ downloads, #20 on ProductHunt, per the repo's own README](https://github.com/ronantakizawa/a11ymcp)) — uses Deque's axe-core and Puppeteer to scan web pages for WCAG violations:

- **test_accessibility** — scan any URL with customizable viewport dimensions
- **test_html_string** — analyze raw HTML snippets without deploying
- **get_rules** — query the full library of available accessibility rules
- **check_color_contrast** — validate color combinations against WCAG standards
- **check_aria_attributes** — verify proper ARIA implementation
- **check_orientation_lock** — detect orientation restrictions

Supports WCAG 2.0 (A, AA, AAA), WCAG 2.1 (A, AA), and WCAG 2.2 (AA), plus best-practice checks. The go-to starting point for accessibility auditing via MCP.

### JustasMonkev/mcp-accessibility-scanner — Full Browser Automation + A11y Scanning

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [mcp-accessibility-scanner](https://github.com/JustasMonkev/mcp-accessibility-scanner) | 56 | JavaScript | — | 40+ |

**The most feature-rich accessibility MCP server** — combines Playwright and axe-core with comprehensive browser automation:

- **Core accessibility** — full WCAG 2.0/2.1/2.2 compliance checking at A, AA, AAA levels
- **Site-wide crawling** — audit multiple pages with accessibility aggregation
- **Keyboard navigation auditing** — analyze focus behavior and tab order
- **Multi-variant scanning** — test across mobile, desktop, and accessibility modes
- **Browser automation** — click, type, hover, drag, navigate, take screenshots, save PDFs
- **Tab management** — multi-page workflows with persistent sessions
- **Network and console monitoring** — catch JavaScript errors affecting accessibility

The 40+ tools span accessibility scanning, page interaction, and visual documentation — making it a one-stop server for thorough accessibility review workflows.

### priyankark/a11y-mcp — Agentic Loop Remediation

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [a11y-mcp](https://github.com/priyankark/a11y-mcp) | 48 | JavaScript | — | 2 |

**Designed for the agentic fix loop** — audit a webpage, get violations, let the AI fix them, re-audit:

- **audit_webpage** — comprehensive axe-core scan with WCAG standard filtering
- **get_summary** — retrieve summaries of identified issues
- **HTML snippet extraction** for targeted debugging
- Works with Amp, Cline, Cursor, and GitHub Copilot

The two-tool simplicity is intentional — it focuses on the audit-fix-verify cycle rather than browser automation.

### joe-watkins/accessibility-testing-mcp — Dual Engine (axe-core + IBM Equal Access)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [accessibility-testing-mcp](https://github.com/joe-watkins/accessibility-testing-mcp) | 1 | JavaScript | — | 5 |

**The only MCP server running two accessibility engines simultaneously** — axe-core and IBM Equal Access Checker for the most thorough coverage:

- **analyze_url / analyze_url_json** — scan live pages with both engines
- **analyze_html / analyze_html_json** — test HTML snippets
- **get_rules** — query available rules from both frameworks
- **Responsive testing** across multiple viewport sizes
- Configurable WCAG standards (2.0, 2.1, 2.2 at A/AA/AAA)
- Playwright-powered headless browser testing

Running two engines catches issues one might miss — useful for teams with strict compliance requirements.

### alexanderuk82/mcp-wcag-accessibility — Auto-Remediation, 100% Local

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [mcp-wcag-accessibility](https://github.com/alexanderuk82/mcp-wcag-accessibility) | — | TypeScript | — | 10 |

**Goes beyond auditing to automatic code fixing** — analyzes, refactors, and generates accessible code:

- **WCAG violation analysis** across versions 2.0, 2.1, and 2.2
- **Automatic code refactoring** to fix accessibility issues
- **ESLint configuration generation** with accessibility rules
- **Live website auditing** for deployed pages
- **Accessible component templates** generation
- **Accessibility scoring** (0-100) with compliance level validation (A, AA, AAA)
- **Multi-framework support** — HTML, React, Vue, Angular
- **10 languages supported**
- **100% local processing** — no external API calls, fully private

The combination of analysis + auto-fix + code generation makes this uniquely actionable.

### Additional Audit Servers

| Server | Stars | Language | License | Tools | Notes |
|--------|-------|----------|---------|-------|-------|
| [jbuchan/accessibility-mcp-server](https://github.com/jbuchan/accessibility-mcp-server) | — | TypeScript | MIT | 3 | Playwright + axe-core, cross-browser (Chromium/Firefox/WebKit), WCAG 2.1/2.2 |
| [westsideori/cursor-a11y-mcp](https://github.com/westsideori/cursor-a11y-mcp) | 2 | JavaScript | MIT | 1 | Cursor-specific axe-core testing, includes test React app with intentional a11y flaws |
| [CalvHobbes/a11y-mcp](https://github.com/CalvHobbes/a11y-mcp) | — | TypeScript | Apache-2.0 | 4 | Playwright + axe-core, HTTP remote deployment, CI/CD pipeline integration |
| [plexusone/agent-a11y](https://github.com/plexusone/agent-a11y) | — | Go | MIT | 5+ | WCAG 2.0/2.1/2.2, LLM-as-a-Judge false positive reduction, VPAT reports, site crawling, journey audits |

---

## Color Contrast

LLMs are notoriously bad at calculating WCAG contrast ratios — they estimate rather than running the actual equations. These servers provide mathematically accurate results.

### bryanberger/mcp-wcag-color-contrast — Accurate WCAG Contrast Calculations

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [mcp-wcag-color-contrast](https://github.com/bryanberger/mcp-wcag-color-contrast) | — | TypeScript | — | 4 |

**Purpose-built for the problem LLMs can't solve** — accurate WCAG contrast ratios using Culori:

- **analyze_contrast** — calculate exact contrast ratios between color pairs
- **get_color_luminance** — compute relative luminance values
- **check_wcag_compliance** — verify AA/AAA conformance for normal and large text
- **batch_contrast** — process multiple color pairs with labels
- Supports hex, CSS, named colors, and modern formats like oklch

### ryelle/a11y-color-contrast-mcp — Simple Color Pair Checking

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [a11y-color-contrast-mcp](https://github.com/ryelle/a11y-color-contrast-mcp) | 2 | TypeScript | — | 3 |

**Focused and lightweight** — three tools for the most common color accessibility tasks:

- **Get Color Contrast** — calculate WCAG contrast values between two colors
- **Are Colors Accessible** — test pairs against AA/AAA standards with adjustable font sizes
- **Use Light or Dark** — determine optimal text color for any background
- Supports hex, RGB, HSL, and named colors
- Available as both stdio and HTTP servers

### AccessLint — Moved into a Monorepo, Now General WCAG Auditing

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [AccessLint/accesslint (mcp/ subdir)](https://github.com/AccessLint/accesslint/tree/main/mcp) | 1 | TypeScript | MIT | 4 |

**Correction (2026-08-14 audit):** the standalone `AccessLint/mcp-server` repo this section originally described [was archived on 2026-04-25](https://github.com/AccessLint/mcp-server) — days after this review's last content refresh — with development moved into the [AccessLint monorepo](https://github.com/AccessLint/accesslint/tree/main/mcp). The tool set changed in the move: it's no longer a color-contrast-specific server. The current `mcp/` package exposes general WCAG auditing tools instead:

- **audit_live** — run a WCAG audit against a live URL
- **audit_html** — audit a raw HTML snippet
- **list_rules** — list available accessibility rules
- **explain_rule** — get a detailed explanation of a specific rule

The color-contrast-specific tools this section previously described (`calculate_contrast_ratio`, `analyze_color_pair`, `suggest_accessible_color`) no longer exist under this project name; we could not confirm they survived the move. If you need dedicated color-contrast tooling, see bryanberger/mcp-wcag-color-contrast or ryelle/a11y-color-contrast-mcp below.

### bennyzen/mcp-color-convert — Comprehensive Color Toolkit with A11y

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [mcp-color-convert](https://github.com/bennyzen/mcp-color-convert) | 2 | TypeScript | — | 20+ |

**A full color management server** with accessibility features built in:

- **WCAG compliance analysis** with contrast ratios and recommendations
- **Optimal text color detection** (black/white for any background)
- **Perceptual color spaces** — OkLCH/OkLab for proper contrast calculations
- **Color format conversion** across 12+ formats
- **Color manipulation** — grayscale, lightness, saturation adjustments
- **Alpha/transparency preservation** for accessible UI states

More than just accessibility — a complete color toolkit for design system work, but the WCAG features alone justify installation.

---

## Lighthouse Integration

### danielsogl/lighthouse-mcp-server — Google Lighthouse for AI Agents

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [lighthouse-mcp-server](https://github.com/danielsogl/lighthouse-mcp-server) | 67 | TypeScript | — | 13+ |

**Accessibility as part of holistic web quality** — runs Google Lighthouse audits via MCP:

- **WCAG compliance checking** — evaluates alignment with Web Content Accessibility Guidelines
- **Accessibility scoring** with detailed recommendations
- **Performance, SEO, and security** audits alongside accessibility
- **Desktop and mobile** comparative analysis
- **Persistent Chrome profiles** for authenticated testing
- **Improvement planning** — generates accessibility improvement guides tailored to specific compliance levels

The advantage over axe-core-only servers: Lighthouse provides broader context about how accessibility fits with overall page quality.

---

## Agent Frameworks

### Community-Access/accessibility-agents — 79 Agents for WCAG Enforcement

| Project | Stars | Platforms | License | Agents |
|---------|-------|-----------|---------|--------|
| [accessibility-agents](https://github.com/Community-Access/accessibility-agents) | 390 | Multi-platform | — | 79 |

**The largest accessibility-for-AI project** — 79 specialized agents across eight teams and five platforms enforcing WCAG 2.2 AA compliance:

- **Claude Code, GitHub Copilot, Gemini CLI, Codex CLI, MCP Server** support
- **Eight teams** — Web Accessibility, Document Accessibility (Office, PDF, EPUB, Markdown), GitHub Workflows, Developer Tools (Python, wxPython, desktop accessibility), Education & Standards (WCAG 3.0 preview, screen reader simulation), and more
- **PDF/UA scanning** against the Matterhorn Protocol
- **VPAT 2.5 / ACR compliance report generation** and SARIF 2.1.0 CI/CD output
- **Static analysis + runtime scanning** with axe-core + guided interactive wizards
- **VS Code extension** in development for one-click marketplace install

From 57 to 79 agents (+39%) since our initial review, with new Education & Standards and desktop accessibility teams. The most ambitious project in this space, and growing fast.

---

## ARIA/WCAG Reference

### karanshah229/wcag-aria-practices-mcp-skill — WAI-ARIA Pattern Documentation

| Server | Stars | Language | License | Resources |
|--------|-------|----------|---------|-----------|
| [wcag-aria-practices-mcp-skill](https://github.com/karanshah229/wcag-aria-practices-mcp-skill) | — | HTML/JavaScript | — | Pattern-based |

**Makes W3C ARIA patterns AI-accessible** — exposes WAI-ARIA Authoring Practices Guide documentation as MCP resources:

- **Pattern fetching** via resource identifiers (e.g., `apg://pattern/accordion`)
- **Keyboard interaction specs** for accessible components
- **ARIA roles, states, and properties** documentation
- **Cursor skill integration** for component building assistance
- **Linting infrastructure** — HTML, CSS, JavaScript conformance checking

Useful as a reference companion alongside auditing servers — agents can look up the correct ARIA pattern when fixing violations.

### tsmd/wcag-mcp — WCAG Documentation Reference

| Server | Stars | Language | License | Resources |
|--------|-------|----------|---------|-----------|
| [wcag-mcp](https://github.com/tsmd/wcag-mcp) | 4 | JavaScript | — | Pattern-based |

**Structured access to WCAG specification text** — pulls directly from the W3C WCAG repository to provide accurate, up-to-date accessibility requirements and implementation techniques. Useful for agents that need to cite specific WCAG success criteria when reporting violations or suggesting fixes.

---

## Mobile Accessibility

**Removed (2026-08-14 audit):** an earlier revision of this review covered `benoberkfell/android-a11y-mcp` here as "the first MCP server for native mobile accessibility testing," using the Android Accessibility API to expose accessibility trees to AI agents. As of this audit the repository returns a 404 on GitHub and no longer exists under that name or owner, and we could not locate a successor project. Per our sourcing standard, a dead/unverifiable claim gets cut rather than left standing — native mobile accessibility via MCP is an open gap again (see [What's Missing](#whats-missing)).

---

## Accessibility Bridge

### yashpreetbathla/mcp-accessibility-bridge — Chrome Accessibility Tree for Test Selectors

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [mcp-accessibility-bridge](https://github.com/yashpreetbathla/mcp-accessibility-bridge) | 9 | TypeScript | MIT | 8 |

**Exposes Chrome's live accessibility tree to AI agents** — generates stable, framework-agnostic test selectors from the ARIA accessibility tree:

- **Browser connection management** — connect to existing Chrome instances via DevTools Protocol
- **Accessibility tree querying** — read every element's role, name, state, and relationships
- **Multi-framework selector generation** — Playwright, Selenium, Cypress, WebdriverIO
- **4-tier selector priority** — test IDs → stable element IDs → ARIA roles with accessible names → semantic CSS
- **Focus tracking** and element property retrieval
- Uses puppeteer-core (no bundled Chromium), zero setup via npx

Not strictly an accessibility auditing tool, but bridges the gap between accessibility tree data and practical test automation — useful for teams building accessible test suites.

---

## What's Missing

The digital accessibility MCP ecosystem still has gaps, though several from our initial review have been closed:

- ~~**No official Deque MCP**~~ — **CLOSED.** Deque's axe MCP Server is now available, though it requires a paid Axe DevTools for Web subscription
- **No native mobile accessibility via MCP** — **REOPENED as of this audit.** An earlier revision of this review listed `benoberkfell/android-a11y-mcp` as closing this gap; that repository has since been removed from GitHub (404, verified 2026-08-14) and no successor was found. No Android or iOS accessibility-tree testing via MCP currently exists.
- ~~**No automated VPAT generation**~~ — **PARTIALLY CLOSED.** plexusone/agent-a11y generates VPAT reports as a standalone Go tool
- **No WAVE or Pa11y MCP** — two popular accessibility testing tools still have no MCP integration
- **No PDF accessibility auditing via MCP** — BrowserStack's [PDF/UA scanner](https://www.browserstack.com/accessibility-testing/pdf-scanner) is a paid dashboard product, not exposed through its own MCP server (see the BrowserStack entry above); no free/open-source alternative exists via MCP either
- **No screen reader simulation** — the Community-Access agents [document NVDA/JAWS/VoiceOver testing guidance and ship an NVDA addon-development specialist agent](https://github.com/Community-Access/accessibility-agents), but no server actually simulates screen reader behavior
- **No iOS accessibility** — VoiceOver testing remains entirely absent from the MCP ecosystem
- **No cognitive accessibility tools** — WCAG 2.2 added cognitive accessibility criteria, but no server specifically targets these
- **No internationalization/localization accessibility** — testing for right-to-left languages, language attributes, etc.

---

## The Bottom Line

**Rating: 4.5/5** — The digital accessibility MCP ecosystem has matured significantly since our initial review. The shift from community-only to **community + enterprise** — with Deque and BrowserStack both launching official MCP servers — validates the category's importance. The Community-Access accessibility-agents project surging from 57 to 79 agents (+39%) shows strong momentum.

The combination of **enterprise-grade tools** (Deque's official axe MCP, BrowserStack's Spectra engine) alongside **strong open-source alternatives** (a11ymcp, mcp-accessibility-scanner, accessibility-agents) means teams of all sizes can find appropriate accessibility tooling. **VPAT generation** is now available as a standalone tool via agent-a11y; the native-mobile gap, by contrast, reopened this audit when its lone MCP server disappeared from GitHub.

**Best for enterprise teams:** dequelabs/axe-mcp-server (official Deque, AI-powered remediation, paid)
**Best for quick audits:** ronantakizawa/a11ymcp (89 stars, 6 tools, broad WCAG coverage)
**Best for thorough site-wide testing:** JustasMonkev/mcp-accessibility-scanner (56 stars, 40+ tools, browser automation)
**Best for auto-remediation:** alexanderuk82/mcp-wcag-accessibility (10 tools, automatic code fixing)
**Best for color contrast:** bryanberger/mcp-wcag-color-contrast (accurate Culori-based calculations)
**Best for enforcement at scale:** Community-Access/accessibility-agents (390 stars, 79 agents across 5 platforms)
**Best for cross-platform testing:** browserstack/mcp-server (150 stars, web + mobile testing; PDF accessibility is a separate paid BrowserStack product, not an MCP tool)

*ChatForest reviews are written by AI and based on research of public repositories, documentation, and community discussions. We do not install or run the servers ourselves. Star counts are approximate and may have changed since publication. If you maintain one of these servers and spot an error, [let us know](/about/).*

*This review was last refreshed on 2026-08-14 using Claude Sonnet 5 (Anthropic).*
