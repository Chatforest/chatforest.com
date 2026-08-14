---
title: "Accessibility & a11y MCP Servers — Axe-Core, WCAG Auditing, Color Contrast, BrowserStack, and More"
date: 2026-03-15T12:55:00+09:00
sources_audited: 2026-08-14
description: "Accessibility and a11y MCP servers are enabling AI-powered WCAG compliance testing and remediation. We reviewed 25+ servers across 7 subcategories."
og_description: "Accessibility MCP servers: Deque axe MCP (official, 2 tools, paid), a11ymcp (89 stars, 6 tools, axe-core), mcp-accessibility-scanner (56 stars, 15+ tools, Playwright), BrowserStack MCP (149 stars, 20+ tools), WCAG reference server (20 tools), and Community-Access/accessibility-agents (390 stars). Rating: 3.5/5."
content_type: "Review"
card_description: "Accessibility and a11y MCP servers for WCAG compliance testing, color contrast checking, code remediation, and enterprise accessibility scanning. Community-Access/accessibility-agents (now 390 stars) shipped its v5.x series (v5.0.0-v5.4.0, April-May 2026) with a GitHub Skills-based installation model, expanded document accessibility (Office formats, PDF, EPUB), and deeper VS Code 1.113 integration; it has since shipped v6.0.0 (June 2026) adding a native Codex CLI plugin. The community leader is ronantakizawa/a11ymcp (89 stars, 10,000+ downloads per its own README) with 6 tools covering URL testing, HTML snippet testing, rule exploration, color contrast, ARIA validation, and orientation lock detection. JustasMonkev's mcp-accessibility-scanner (56 stars) provides Playwright-powered multi-page crawling, keyboard navigation testing, and matrix scanning — the most comprehensive free scanner available. Deque's official axe MCP (6 stars, paid) and BrowserStack's MCP (149 stars, paid) represent the enterprise tier. Rating: 3.5/5."
last_refreshed: 2026-08-14
---

Accessibility MCP servers are bringing automated WCAG compliance testing directly into AI coding workflows. Instead of switching to browser DevTools or running manual audits, these servers let AI agents scan pages for violations, check color contrast ratios, validate ARIA attributes, and even refactor code to fix accessibility issues — all through the Model Context Protocol.

The landscape now spans seven areas: **full-page auditing** (axe-core-powered scanners), **WCAG reference & knowledge** (guideline lookup tools), **color contrast checking** (dedicated contrast ratio tools), **WCAG analysis & remediation** (code-level fixing), **enterprise integration** (Deque, BrowserStack), **color blindness simulation** (visual impairment previews), and **dual-engine testing** (multiple accessibility engines).

The headline findings this cycle: **Community-Access/accessibility-agents shipped its v5.x series** — v5.0.0 (April 16, 2026) through v5.4.0 (early May 2026), per the project's own [CHANGELOG](https://github.com/Community-Access/accessibility-agents/blob/main/CHANGELOG.md) — adopting a [GitHub Skills](https://github.com/Community-Access/accessibility-agents) installation model (a bash installer that syncs skill/agent files across platforms — not, as an earlier version of this review incorrectly stated, compiled Go binaries), expanding document accessibility coverage (DOCX, XLSX, PPTX, PDF, EPUB, Markdown), and deepening VS Code 1.113 integration. The project has since shipped [v6.0.0](https://github.com/Community-Access/accessibility-agents/blob/main/CHANGELOG.md) (June 15, 2026), adding a native Codex CLI plugin, and now stands at [390 stars](https://github.com/Community-Access/accessibility-agents). **Three competing free axe-core scanners** still dominate open-source adoption — ronantakizawa/a11ymcp (89 stars, 10,000+ downloads per its own README), JustasMonkev's mcp-accessibility-scanner (56 stars, 15+ tools), and priyankark/a11y-mcp (48 stars). **The most capable free scanner is JustasMonkev's**, with Playwright-based multi-page crawling, keyboard navigation testing, and matrix scanning across viewport variants. Deque's official axe MCP (dequelabs/axe-mcp-server-public, 6 stars) and BrowserStack's MCP (149 stars) remain the paid enterprise tier. **The biggest remaining gaps**: iOS VoiceOver testing, native Android testing (Community-Access's own roadmap [lists mobile native accessibility as planned but not yet built](https://github.com/Community-Access/accessibility-agents/issues/8)), screen reader emulation, and VPAT/ACR generation remain unaddressed.

**Category:** [Developer Tools](/categories/developer-tools/)

---

## Full-Page Auditing

### a11ymcp (ronantakizawa)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [ronantakizawa/a11ymcp](https://github.com/ronantakizawa/a11ymcp) | 89 | JavaScript | MIT | 6 |

The most popular free accessibility MCP server, with **10,000+ downloads** and a [**#20 ranking on ProductHunt**](https://www.producthunt.com/products/web-accessibility-testing-mcp). Uses axe-core and Puppeteer to provide six distinct tools. 87 commits. Verified on MseeP.ai and listed in the Glama.ai MCP registry.

- **test_accessibility** — scan any public URL with customizable viewport dimensions
- **test_html_string** — test raw HTML snippets without deploying
- **get_rules** — explore axe-core's full rule catalog
- **check_color_contrast** — verify foreground/background color pairs against WCAG thresholds
- **check_aria_attributes** — validate ARIA usage in HTML markup
- **check_orientation_lock** — detect orientation restrictions that violate WCAG 1.3.4

Supports WCAG 2.0, 2.1, and 2.2 testing. The HTML string testing is particularly useful for AI coding assistants — test generated markup before it reaches a browser.

### mcp-accessibility-scanner (JustasMonkev)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [JustasMonkev/mcp-accessibility-scanner](https://github.com/JustasMonkev/mcp-accessibility-scanner) | 56 | JavaScript | — | 15+ |

The **most comprehensive free accessibility scanner** in the MCP ecosystem. Built on Playwright (not Puppeteer), which enables richer browser automation and persistent sessions. Now at [505 commits](https://github.com/JustasMonkev/mcp-accessibility-scanner/commits/main/), indicating active, ongoing development.

Core scanning tools:
- **scan_page** — WCAG compliance checks across 2.0/2.1/2.2 at A/AA/AAA levels
- **audit_site** — multi-page crawling with aggregated violation reporting
- **scan_page_matrix** — variant comparison across mobile, desktop, zoom, and reduced-motion configurations
- **audit_keyboard** — real keyboard navigation testing (not just static analysis)

Plus full browser automation: navigate, click, type, hover, drag, select, take screenshots, save PDFs, manage tabs, and resize viewports.

The matrix scanning feature is unique — it tests the same page across multiple viewport/motion configurations in a single call, catching responsive design accessibility regressions.

### a11y-mcp (priyankark)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [priyankark/a11y-mcp](https://github.com/priyankark/a11y-mcp) | 48 | JavaScript | MPL-2.0 | 2 |

A simpler, focused approach with just two tools:

- **audit_webpage** — detailed accessibility audit with optional HTML snippet extraction and WCAG standard filtering
- **get_summary** — summarize accessibility issues on a page

Designed explicitly for **agentic loops** — audit a page, get violations, let the AI fix them, re-audit. Compatible with Amp, Cline, Cursor, and GitHub Copilot. The MPL-2.0 license (rather than MIT) is worth noting for commercial integrations.

### cursor-a11y-mcp (westsideori)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [westsideori/cursor-a11y-mcp](https://github.com/westsideori/cursor-a11y-mcp) | 2 | JavaScript | MIT | 1 |

A single-tool server purpose-built for Cursor IDE integration. Provides comprehensive accessibility testing via axe-core and Puppeteer with detailed violation reports including impact levels, descriptions, help documentation, affected HTML elements, and failure summaries. Straightforward but limited compared to the multi-tool alternatives.

## Color Contrast Checking

Three dedicated servers solve the specific problem that **LLMs cannot accurately calculate WCAG contrast ratios** from training data — they need to run the actual WCAG contrast algorithm.

### a11y-color-contrast-mcp (ryelle)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [ryelle/a11y-color-contrast-mcp](https://github.com/ryelle/a11y-color-contrast-mcp) | 2 | TypeScript | MIT | 3 |

Three focused tools: **get color contrast** (calculate WCAG ratio between two colors), **are colors accessible** (test against WCAG thresholds), and **use light or dark** (determine optimal text color for a given background). Clean, single-purpose design.

### mcp-wcag-color-contrast (bryanberger)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [bryanberger/mcp-wcag-color-contrast](https://github.com/bryanberger/mcp-wcag-color-contrast) | 0 | TypeScript | MIT | 4 |

Built with Bun and the Culori color library. Includes **batch_contrast** for analyzing multiple color pairs simultaneously — useful for design system audits where you need to check an entire palette. Also provides luminance calculation and specific WCAG level compliance checking.

### AccessLint MCP Server (accesslint/mcp)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [AccessLint/accesslint (mcp/)](https://github.com/AccessLint/accesslint/tree/main/mcp) | 6 | TypeScript | MIT | 4 |

**Correction from an earlier version of this review**: this entry previously described `accesslint/mcp-server` as a 3-tool color-contrast utility with a `suggest_accessible_color` tool. That was accurate for the package's [v0.1.0 release](https://unpkg.com/@accesslint/mcp@0.1.0/README.md) (November 2025), but the project pivoted away from color-contrast checking entirely as of [v0.2.0](https://unpkg.com/@accesslint/mcp@0.2.0/README.md) (February 2026) — before this review was first published. The original repo was [archived on April 25, 2026](https://github.com/accesslint/mcp-server), with development continuing in the [AccessLint monorepo](https://github.com/AccessLint/accesslint/tree/main/mcp), published to npm as [`@accesslint/mcp`](https://www.npmjs.com/package/@accesslint/mcp). It is now a general WCAG-violation auditor with four tools — **audit_live** (live-page audits via a companion browser MCP like chrome-devtools-mcp), **audit_html** (HTML-string audits), **list_rules**, and **explain_rule** — and no longer performs color-pair or contrast-ratio checking, so it overlaps with the axe-core scanners in Full-Page Auditing above rather than with the other servers in this section.

## WCAG Analysis & Remediation

### mcp-wcag-accessibility (alexanderuk82)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [alexanderuk82/mcp-wcag-accessibility](https://github.com/alexanderuk82/mcp-wcag-accessibility) | 0 | TypeScript | MIT | 10 |

The most ambitious remediation-focused server with **10 tools** spanning analysis, fixing, and documentation:

- **analyze_accessibility** — comprehensive WCAG audit
- **refactor_for_wcag** — automatic code refactoring to fix violations
- **validate_compliance** — check against specific WCAG levels
- **get_documentation** — retrieve relevant WCAG guidelines
- **annotate_code** — add accessibility annotations
- **accessibility_score** — generate an accessibility score
- **generate_component** — create accessible component templates
- **eslint_config** — generate ESLint configurations for accessibility rules
- **live_url_audit** — audit live URLs
- **wcag_github_sync** — sync with WCAG GitHub repository

Supports **multi-framework analysis** across HTML, React, Vue, and Angular. Available in 10 languages. The ESLint config generation is a practical touch — bake accessibility rules into the project's linting pipeline rather than relying solely on runtime audits. Runs 100% locally with no external API dependencies.

## Enterprise & Vendor Integration

### Deque axe MCP Server (Official)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [dequelabs/axe-mcp-server-public](https://github.com/dequelabs/axe-mcp-server-public) | 6 | — | Proprietary | 2 |

**The most significant addition to the category since our original review.** Deque — the company that builds axe-core, the engine powering nearly every community accessibility MCP server — now has its own official MCP server with two tools:

- **analyze** — scan pages for accessibility violations using the full axe engine
- **remediate** — AI-powered code fixes for detected violations

Integrates with **Claude, GitHub Copilot, Cursor**, and any MCP-compatible AI coding agent. Included in Deque's Axe DevTools for Web bundle at no additional cost for existing customers. Now generally available and [included in Axe DevTools for Web](https://www.deque.com/blog/axe-devtools-for-web-now-includes-axe-mcp-server-for-earlier-fixes-and-faster-delivery/).

**Requires a paid Axe DevTools for Web subscription** and an API key from axe.deque.com. This is the first time the upstream engine provider has entered the MCP space directly — creating an interesting dynamic where the community servers use Deque's open-source axe-core library for free, while Deque's own server adds proprietary remediation intelligence on top. Only [6 stars and 11 commits](https://github.com/dequelabs/axe-mcp-server-public) so far, suggesting early-stage adoption.

### BrowserStack MCP Server (Official)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [browserstack/mcp-server](https://github.com/browserstack/mcp-server) | 149 | TypeScript | AGPL-3.0 | 20+ |

BrowserStack's official MCP server includes accessibility as part of a broader testing suite (Live, App Live, Automate, screenshots). Now at [627 commits](https://github.com/browserstack/mcp-server/commits/main/). The accessibility tools:

- **runAccessibilityScan** — automated WCAG/ADA compliance scanning with support for both public and local URLs (automatic tunnel management for private dev environments)
- **accessibilityExpert** — expert guidance on WCAG guidelines, usability, and accessibility best practices

Powered by [**Spectra™**](https://www.browserstack.com/accessibility-testing/spectra-rule-engine), BrowserStack's proprietary accessibility rule engine. The key differentiator: it analyzes violations in context, aligns fixes with your design system, and suggests **production-ready code** — not just violation reports. AI-generated contextual code fixes directly in the IDE.

**Requires a BrowserStack Accessibility license** — this is not a free tool. [Available on AWS Marketplace](https://aws.amazon.com/marketplace/pp/prodview-hcllard6w7na4). For teams already using BrowserStack, adding accessibility scanning to their AI workflow is straightforward.

## WCAG Reference & Knowledge

### wcag-mcp (joe-watkins)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [joe-watkins/wcag-mcp](https://github.com/joe-watkins/wcag-mcp) | 13 | JavaScript | MIT | 20 |

A **new addition** that fills a different niche: instead of scanning pages for violations, this server gives AI agents comprehensive access to the **WCAG 2.2 specification itself**. 20 tools spanning four categories:

- **Core WCAG tools** (9) — look up success criteria, filter by level/principle, search guidelines
- **Technique resources** (5) — browse 400+ WCAG techniques with applicability details
- **Glossary functions** (3) — access 101 WCAG glossary definitions
- **Enhanced context** (3) — get Understanding documentation for any success criterion

Covers all 87 success criteria across the four WCAG principles (Perceivable, Operable, Understandable, Robust) and 13 guidelines. Works locally via stdio and remotely through Netlify Functions.

This is genuinely useful for AI coding agents: rather than just detecting violations, an agent can look up the relevant WCAG guideline, understand the technique, and make an informed fix — combining well with any of the scanning servers above.

### accessibility-testing-mcp (joe-watkins)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [joe-watkins/accessibility-testing-mcp](https://github.com/joe-watkins/accessibility-testing-mcp) | 1 | JavaScript | MIT | 5 |

A **dual-engine accessibility testing server** that runs both **axe-core and IBM Equal Access**. Five tools:

- **analyze_url / analyze_url_json** — test live URLs with either or both engines
- **analyze_html / analyze_html_json** — test HTML snippets
- **get_rules** — explore available rules

The IBM Equal Access engine catches some issues that axe-core misses (and vice versa), making this useful for teams wanting broader coverage. Multi-viewport testing supported. 21 commits.

## Color Blindness Simulation

### mcp-web-a11y (bilhasry-deriv)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [bilhasry-deriv/mcp-web-a11y](https://github.com/bilhasry-deriv/mcp-web-a11y) | 4 | JavaScript | MIT | 2 |

Combines accessibility auditing with **color blindness simulation** — a unique pairing in the MCP ecosystem. Two tools:

- **check_accessibility** — standard axe-core WCAG scanning
- **simulate_colorblind** — renders pages through color matrices simulating protanopia (red-blind), deuteranopia (green-blind), and tritanopia (blue-blind)

The simulation feature generates screenshots showing how the page appears to users with different types of color vision deficiency. Useful for catching issues that pass automated contrast checks but still create problems for color-blind users — like using color alone to convey meaning (WCAG 1.4.1).

## Related: Accessibility Agents

### Community-Access/accessibility-agents

| Project | Stars | License | Agents |
|---------|-------|---------|--------|
| [Community-Access/accessibility-agents](https://github.com/Community-Access/accessibility-agents) | 390 | MIT | 79 |

Not an MCP server, but the **most ambitious accessibility-AI project** in the ecosystem. Per its own [CHANGELOG](https://github.com/Community-Access/accessibility-agents/blob/main/CHANGELOG.md), it shipped v5.0.0 (April 16, 2026) through v5.4.0 (early May 2026) — its v5.x series represents a significant shift:

- **GitHub Skills installation model** — a bash installer (`install.sh`) syncs skill and agent files across platforms; an earlier version of this review incorrectly described this as "native Go binaries," which the project's install scripts and CHANGELOG do not support
- **Expanded document accessibility** — deeper coverage for DOCX, XLSX, PPTX, PDF, EPUB, and Markdown with dedicated agent teams
- **VS Code 1.113 integration** — "MCP across agent types" bridges accessibility servers into Copilot CLI and Claude agents
- **Eight teams**, five platforms — Web Accessibility, Document Accessibility, GitHub Workflow, Developer Tools, Education & Standards, plus cross-cutting orchestrators, per the project's own [README](https://github.com/Community-Access/accessibility-agents#readme)

Works with Claude Code, GitHub Copilot (VS Code and CLI), Gemini CLI, Claude Desktop, and Codex CLI. The project has since shipped [v6.0.0](https://github.com/Community-Access/accessibility-agents/blob/main/CHANGELOG.md) (June 15, 2026), adding a native Codex CLI plugin. It emphasizes that "AI and automated tools are not perfect... they miss things, make mistakes, and cannot replace testing with real screen readers and assistive technology."

At [390 stars](https://github.com/Community-Access/accessibility-agents), it has significantly more community traction than any individual accessibility MCP server.

## What's Missing

The accessibility MCP ecosystem has notable gaps:

- **Native mobile accessibility** — no dedicated MCP server tests iOS VoiceOver or Android's native Accessibility API. (A prior version of this review cited a "benoberkfell" Android Accessibility MCP Server said to fill part of this gap; we could not locate that project at its stated GitHub location during this audit and have removed the claim. Community-Access's own project [lists mobile native accessibility as planned but not yet built](https://github.com/Community-Access/accessibility-agents/issues/8).)
- **PDF/document accessibility** — Community-Access v5.x expands document agent coverage, but no dedicated MCP server handles PDF remediation or alt-text generation standalone
- **Screen reader emulation** — no server simulates actual screen reader output (NVDA, JAWS, VoiceOver)
- **VPAT/ACR generation** — no automated Voluntary Product Accessibility Template creation
- **Accessibility management platforms** — no integrations with Level Access, eSSENTIAL Accessibility, or UserWay (Deque now has an official MCP server, but it requires a paid subscription)
- **Cognitive accessibility** — no tools for readability analysis, plain language checking, or cognitive load assessment (WCAG 2.1 Level AAA)
- **Automated remediation at scale** — individual page fixes work, but no server handles site-wide remediation campaigns

## The Bottom Line

**Rating: 3.5 / 5** — The accessibility MCP category continues to mature steadily. The headline: [**Community-Access/accessibility-agents**](https://github.com/Community-Access/accessibility-agents) shipped its v5.x series (v5.0.0-v5.4.0, April-May 2026) and has since shipped v6.0.0 (June 2026), now standing at 390 stars — signaling maturation from a research project into a production-grade tool, via a GitHub Skills installation model (a bash installer, not compiled binaries as an earlier version of this review stated). The free community scanners (a11ymcp at 89 stars, mcp-accessibility-scanner at 56 stars, priyankark/a11y-mcp at 48 stars) continue steady growth.

The rating holds at 3.5/5 because the core limitations persist: iOS/VoiceOver and native Android testing remain absent from any dedicated MCP server, screen reader emulation is still missing, VPAT/ACR generation is unaddressed, and the category still suffers from fragmentation among 10+ servers running variations of the same axe-core scan. Mobile accessibility (the dominant platform for assistive technology users) remains a gap the whole category has yet to fill. For web developers wanting AI that catches and fixes WCAG violations during coding, the tooling is genuinely useful and gaining momentum.

*This review was last edited on 2026-08-14 using Claude Sonnet 5 (Anthropic).*
