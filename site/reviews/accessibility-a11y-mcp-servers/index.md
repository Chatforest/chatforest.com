# Accessibility & a11y MCP Servers — Axe-Core, WCAG Auditing, Color Contrast, BrowserStack, and More

> Accessibility and a11y MCP servers are enabling AI-powered WCAG compliance testing and remediation. We reviewed 25+ servers across 7 subcategories.


Accessibility MCP servers are bringing automated WCAG compliance testing directly into AI coding workflows. Instead of switching to browser DevTools or running manual audits, these servers let AI agents scan pages for violations, check color contrast ratios, validate ARIA attributes, and even refactor code to fix accessibility issues — all through the Model Context Protocol.

The landscape now spans seven areas: **full-page auditing** (axe-core-powered scanners), **WCAG reference & knowledge** (guideline lookup tools), **color contrast checking** (dedicated contrast ratio tools), **WCAG analysis & remediation** (code-level fixing), **enterprise integration** (Deque, BrowserStack), **color blindness simulation** (visual impairment previews), and **dual-engine testing** (multiple accessibility engines).

The headline findings this cycle: **Community-Access/accessibility-agents shipped five major releases** (v5.0.0 through v5.4.0) in 30 days, jumping from 236 to **276 stars (+17%)** — the highest velocity of any project in the category. The v5.x series migrated to a GitHub Skills installation model with **native Go binaries**, expanded document accessibility coverage (DOCX, XLSX, PPTX, PDF, EPUB, Markdown), and deepened VS Code 1.113 integration. **Three competing free axe-core scanners** still dominate open-source adoption — ronantakizawa/a11ymcp (86 stars, 6,000+ downloads), JustasMonkev's mcp-accessibility-scanner (49 stars, 15+ tools), and priyankark/a11y-mcp (44 stars). **The most capable free scanner is JustasMonkev's**, with Playwright-based multi-page crawling, keyboard navigation testing, and matrix scanning across viewport variants. Deque's official axe MCP (dequelabs/axe-mcp-server-public, 4 stars) and BrowserStack's MCP (139 stars) remain the paid enterprise tier. **A new Android Accessibility MCP Server** (benoberkfell) now provides AI-driven accessibility testing for Android apps via the Accessibility API — the first server to address the mobile testing gap this review has flagged since launch. **The biggest remaining gaps**: iOS VoiceOver testing, screen reader emulation, and VPAT/ACR generation remain unaddressed.

**Category:** [Developer Tools](/categories/developer-tools/)

---

## Full-Page Auditing

### a11ymcp (ronantakizawa)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [ronantakizawa/a11ymcp](https://github.com/ronantakizawa/a11ymcp) | 86 | JavaScript | MIT | 6 |

The most popular free accessibility MCP server, with **6,000+ downloads** and a **#20 ranking on ProductHunt**. Uses axe-core and Puppeteer to provide six distinct tools. 87 commits. Verified on MseeP.ai and listed in the Glama.ai MCP registry.

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
| [JustasMonkev/mcp-accessibility-scanner](https://github.com/JustasMonkev/mcp-accessibility-scanner) | 49 | JavaScript | — | 15+ |

The **most comprehensive free accessibility scanner** in the MCP ecosystem. Built on Playwright (not Puppeteer), which enables richer browser automation and persistent sessions. Now at 193 commits (+20% since March), indicating active, ongoing development.

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
| [priyankark/a11y-mcp](https://github.com/priyankark/a11y-mcp) | 44 | JavaScript | MPL-2.0 | 2 |

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

### AccessLint MCP Server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [accesslint/mcp-server](https://github.com/accesslint/mcp-server) | 1 | TypeScript | MIT | 3 |

From AccessLint, an established accessibility linting company. Uniquely includes **suggest_accessible_color** — given a color pair that fails WCAG, it proposes alternative colors that would pass. Also provides contrast ratio calculation and detailed color pair analysis for WCAG 2.1. Designed for integration with both Claude Desktop and the AccessLint marketplace plugin.

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
| [dequelabs/axe-mcp-server-public](https://github.com/dequelabs/axe-mcp-server-public) | 4 | — | Proprietary | 2 |

**The most significant addition to the category since our original review.** Deque — the company that builds axe-core, the engine powering nearly every community accessibility MCP server — now has its own official MCP server with two tools:

- **analyze** — scan pages for accessibility violations using the full axe engine
- **remediate** — AI-powered code fixes for detected violations

Integrates with **Claude, GitHub Copilot, Cursor**, and any MCP-compatible AI coding agent. Included in Deque's Axe DevTools for Web bundle at no additional cost for existing customers. First announced at Axe-con 2025, now generally available.

**Requires a paid Axe DevTools for Web subscription** and an API key from axe.deque.com. This is the first time the upstream engine provider has entered the MCP space directly — creating an interesting dynamic where the community servers use Deque's open-source axe-core library for free, while Deque's own server adds proprietary remediation intelligence on top. Only 3 stars and 7 commits so far, suggesting early-stage adoption.

### BrowserStack MCP Server (Official)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [browserstack/mcp-server](https://github.com/browserstack/mcp-server) | 139 | TypeScript | — | 20+ |

BrowserStack's official MCP server includes accessibility as part of a broader testing suite (Live, App Live, Automate, screenshots). Now at 469 commits. The accessibility tools:

- **runAccessibilityScan** — automated WCAG/ADA compliance scanning with support for both public and local URLs (automatic tunnel management for private dev environments)
- **accessibilityExpert** — expert guidance on WCAG guidelines, usability, and accessibility best practices

Powered by **Spectra™**, BrowserStack's accessibility engine. The key differentiator: it analyzes violations in context, aligns fixes with your design system, and suggests **production-ready code** — not just violation reports. AI-generated contextual code fixes directly in the IDE.

**Requires a BrowserStack Accessibility license** — this is not a free tool. Available on AWS Marketplace. For teams already using BrowserStack, adding accessibility scanning to their AI workflow is straightforward.

## WCAG Reference & Knowledge

### wcag-mcp (joe-watkins)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [joe-watkins/wcag-mcp](https://github.com/joe-watkins/wcag-mcp) | 8 | JavaScript | MIT | 20 |

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

A **dual-engine accessibility testing server** that runs both **axe-core and IBM Equal Access** — the first MCP server to offer multiple accessibility testing engines in a single package. Five tools:

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
| [Community-Access/accessibility-agents](https://github.com/Community-Access/accessibility-agents) | 276 | MIT | 79+ |

Not an MCP server, but the **most ambitious accessibility-AI project** in the ecosystem — and it shipped **five major releases in 30 days** (v5.0.0 through v5.4.0), surging from 236 to **276 stars (+17%)** in this cycle alone. The v5.x series represents a significant architectural shift:

- **GitHub Skills installation model** — agents now install via native Go binaries, removing language runtime dependencies
- **Expanded document accessibility** — deeper coverage for DOCX, XLSX, PPTX, PDF, EPUB, and Markdown with dedicated agent teams
- **VS Code 1.113 integration** — "MCP across agent types" bridges accessibility servers into Copilot CLI and Claude agents
- **Eight teams**, five platforms — Web Accessibility, Document Accessibility, GitHub Workflow, Developer Tools, Education & Standards, plus cross-cutting orchestrators

Works with Claude Code, GitHub Copilot (VS Code and CLI), Gemini CLI, Claude Desktop, and Codex CLI. The project emphasizes that "AI and automated tools are not perfect — they cannot replace testing with real screen readers."

At 276 stars, it has significantly more community traction than any individual accessibility MCP server.

## New This Cycle

### Android Accessibility MCP Server (benoberkfell)

A new server using the **Android Accessibility API** to provide AI-driven accessibility testing for Android apps. This is the first MCP server to target native mobile accessibility — partially addressing the mobile gap this review has flagged since launch. Details on star count and toolset are still emerging as the project is newly published.

## What's Missing

The accessibility MCP ecosystem has notable gaps — some narrowing:

- **iOS accessibility** — no VoiceOver or iOS-native testing; Android is now partially covered (see above)
- **PDF/document accessibility** — Community-Access v5.x expands document agent coverage, but no dedicated MCP server handles PDF remediation or alt-text generation standalone
- **Screen reader emulation** — no server simulates actual screen reader output (NVDA, JAWS, VoiceOver)
- **VPAT/ACR generation** — no automated Voluntary Product Accessibility Template creation
- **Accessibility management platforms** — no integrations with Level Access, eSSENTIAL Accessibility, or UserWay (Deque now has an official MCP server, but it requires a paid subscription)
- **Cognitive accessibility** — no tools for readability analysis, plain language checking, or cognitive load assessment (WCAG 2.1 Level AAA)
- **Automated remediation at scale** — individual page fixes work, but no server handles site-wide remediation campaigns

## The Bottom Line

**Rating: 3.5 / 5** — The accessibility MCP category showed its strongest activity cycle yet. The headline: **Community-Access/accessibility-agents shipped v5.0.0 through v5.4.0 in 30 days**, hitting 276 stars (+17%) and adopting native Go binaries — signaling maturation from a research project into a production-grade tool. A new **Android Accessibility MCP Server** (benoberkfell) partially addresses the mobile testing gap that has held this category back. The free community scanners (a11ymcp at 86 stars, mcp-accessibility-scanner at 49 stars) continue steady growth, and priyankark/a11y-mcp gained 4 stars in 30 days.

The rating holds at 3.5/5 because the core limitations persist: iOS/VoiceOver testing remains absent, screen reader emulation is still missing, VPAT/ACR generation is unaddressed, and the category still suffers from fragmentation among 10+ servers running variations of the same axe-core scan. Android coverage is a meaningful step, but enterprise mobile accessibility (iOS is the dominant platform for assistive technology users) remains a gap. For web developers wanting AI that catches and fixes WCAG violations during coding, the tooling is genuinely useful and gaining momentum.

*This review was last edited on 2026-05-20 using Claude Sonnet 4.6 (Anthropic).*

