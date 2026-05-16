# Mobbin MCP Server — 621,500 Real App Screens as Design Reference for AI Agents

> Mobbin's official MCP server (launched May 12, 2026) connects AI agents to 621,500+ real app screens and 142,200+ flows via a remote HTTP endpoint. Agents can search UI patterns, retrieve flows, and view actual screen images for grounded design reference. Paid plans required. Beta. Rating: 4/5.


**At a glance:** Official Mobbin MCP server, launched May 12, 2026. Remote HTTP endpoint at `https://api.mobbin.com/mcp`. Browser OAuth authentication. **621,500+ screens**, **142,200+ flows** from shipped apps across fintech, e-commerce, health, productivity, social, and SaaS. Requires a paid Mobbin plan (Pro from €10/month billed yearly). Currently in beta. Part of our **[Design & Creative MCP category](/categories/design-creative/)**.

Mobbin is a design reference library — a curated catalog of real screens from real apps that shipped. Designers use it to answer questions like: how does Duolingo handle streak recovery? What does Robinhood's onboarding look like? How do the best fintech apps structure their paywall? The library has existed as a web product for years. The MCP server, launched May 12, 2026, makes that reference library available to AI agents mid-workflow.

This is architecturally different from design-to-code servers like [Framelink](/reviews/framelink-figma-mcp-server/) or the [Figma Dev Mode MCP Server](/reviews/figma-dev-mode-mcp-server/). Those translate your own designs into code. Mobbin MCP gives your AI agent access to how other teams solved the same design problems — grounded in what actually shipped.

## The Library

621,500 screens is not a small number. The library spans:

- **App categories:** Fintech, e-commerce, health, productivity, social, SaaS, lifestyle
- **Coverage depth:** Includes subscription-only products, region-locked finance apps, and niche vertical apps that are difficult to find through casual research
- **Flows:** 142,200+ documented user flows — not just individual screens but the complete interaction paths (signup → onboarding → paywall → subscription confirmation, etc.)

Mobbin's human curation is the differentiator here. The screens are selected and organized by the Mobbin team, tagged with meaningful metadata, and linked into flows with context about what pattern each screen represents. This is what makes it more useful as AI agent reference material than, say, scraping app store screenshots yourself.

## Architecture

The Mobbin MCP server is a **remote HTTP endpoint** — there is no local server to install or maintain.

```
claude mcp add mobbin --transport http https://api.mobbin.com/mcp
```

After adding the server, authentication happens via a browser OAuth flow: an `Authenticate` option appears in the MCP menu, a browser window opens, and you sign in to your Mobbin account to authorize the connection. Credentials are managed by Mobbin's authentication system — no API keys to generate or rotate manually.

Remote HTTP transport means this server is compatible with Claude.ai browser access as well as Claude Code, Cursor, and other MCP clients that support streamable HTTP.

## Tools

The Mobbin MCP server provides tools for searching and retrieving from the library:

| Tool | What it does |
|------|-------------|
| `search_screens` | Search screens across all apps by pattern, element, or feature type (e.g., "permission prompt," "empty state," "paywall") |
| `search_flows` | Find user flows across apps by flow type (onboarding, checkout, subscription, settings) |
| `search_apps` | Browse the app library with filtering and sorting — by category, platform, or popularity |
| `get_app_screens` | Retrieve all screens from a specific app — useful for deep-diving one product |
| `get_app_flows` | Get all documented flows for a specific app |
| `get_screen_detail` | Fetch a specific screen and return it as base64 image content that the AI model can view and analyze directly |
| `get_filters` | Access available filter values and definitions for building precise search queries |
| `get_collections` | List metadata for saved Mobbin collections |

The standout tool is **`get_screen_detail`**: it returns the actual screen image in base64 format, making it viewable by multimodal models. An AI agent can search for "subscription upgrade prompt," retrieve a set of matching screens, view them directly, and describe specific layout decisions — without the user ever opening a browser.

## Use Cases

**UI development with AI coding agents.** Ask Claude to implement an onboarding flow; it searches Mobbin for real onboarding patterns, views examples from relevant apps, and builds from what shipped — not from hallucinated best practices.

**Competitive research mid-workflow.** Instead of pausing to open Mobbin in a browser tab, an agent can pull relevant screens as part of a design or strategy task.

**Grounding AI output in production patterns.** AI models are prone to generating generic UI that "looks right" but diverges from how the best apps actually work. Mobbin MCP gives the agent factual references to work from.

**Feature-specific research.** "How do top fintech apps handle biometric re-authentication?" pulls real examples immediately, without the user manually searching.

## Pricing and Access

MCP access is included on all paid Mobbin plans. The free plan does not include MCP.

| Plan | Price | MCP Access |
|------|-------|-----------|
| Free | €0 | No — limited to 4 apps, 3 collections |
| Pro | €10/mo (billed yearly) | Yes |
| Team | €12/member/mo (billed yearly) | Yes |
| Enterprise | Custom | Yes |

Students receive 50% off Pro for up to two years. Nonprofits are also eligible for 50% off the Pro plan.

The paywall is real. For individual developers, €10/month is a reasonable tool cost. For teams already using Mobbin for manual design research, MCP access is an incremental benefit — the subscription pays for itself in the base product.

## What's Missing

**Free-tier MCP access.** The free plan's 4-app, 3-collection limit is unusable for serious design research, and it doesn't include MCP at all. There's no "try the MCP server with limited calls" option comparable to how some API-backed MCP servers handle trial access.

**Collection retrieval in beta.** Collection items (not just metadata) are not yet fetchable through the MCP server in the current beta. If you've organized Mobbin into curated collections, the agent can see those collections exist but can't pull their contents. This will presumably ship as the beta matures.

**No community ecosystem.** Unlike the major code/developer MCP servers, there are no GitHub stars to assess, no community forks, no independent testing data. Mobbin MCP is a managed service — you're trusting Mobbin's implementation and availability. The unofficial third-party implementation ([pdcolandrea/mobbin-mcp](https://github.com/pdcolandrea/mobbin-mcp)) predates the official server and uses session cookie scraping rather than OAuth — interesting proof of demand, but not a substitute for the official server's authenticated access.

**Mobile-and-web focus.** The library is strong on mobile and web app UX. It is not a resource for print design, brand identity, illustration style, motion graphics, or physical product design. The MCP server's value is specific to the product design domain.

## Context in the Design MCP Ecosystem

The Figma/Framelink servers (your designs → code) and the Mobbin MCP server (reference library → grounded output) solve different problems. They're complementary:

- **Framelink** or **Figma Dev Mode MCP**: translate your existing Figma files into code
- **Mobbin MCP**: give your AI agent real-world reference material before or during design work

A complete AI-assisted design workflow could plausibly use both: Mobbin for research and pattern reference, Figma/Framelink for implementation. Neither replaces the other.

The [Adobe Creative Cloud Claude Connector](/reviews/adobe-firefly-video/) and the Claude Connectors for [Ableton, SketchUp, and Autodesk Fusion](/guides/claude-connectors-creative-tools/) are tool-execution integrations — they let AI act on creative software. Mobbin MCP is a reference tool — it lets AI see and reference what others built. Different category.

## Verdict

Mobbin MCP is a well-executed, genuinely novel MCP server. The concept — giving AI agents access to a curated library of real production UIs — fills a gap that code-focused design servers can't address. The remote HTTP architecture is clean. The OAuth authentication is properly handled. The `get_screen_detail` tool returning viewable images is a particularly good implementation choice for a multimodal workflow.

The beta limitations (no collection item retrieval) and the paid-only requirement are the main friction points. These will likely improve: collection retrieval is an obvious next feature, and the beta label signals that the team is still iterating. For designers or developers who already pay for Mobbin, the MCP server is an immediate quality-of-life addition at no extra cost.

**Rating: 4/5** — Excellent concept and execution for product design workflows. Solid remote HTTP architecture, multimodal-ready image retrieval, and a genuinely useful library. Held back by beta-phase limitations and the paid-only barrier, but the core tool is strong.

---

*Mobbin MCP is an official product of Mobbin. ChatForest researched this review using the official Mobbin launch announcement, public documentation at docs.mobbin.com, and third-party coverage. We did not test the MCP server directly.*

