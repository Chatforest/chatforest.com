---
title: "OpenAI Codex Expands Beyond Code: Sites, Six Role Plugins, and What It Means for Enterprise AI Builders"
date: 2026-06-04
description: "OpenAI's June 3 'Intelligence at Work' update turns Codex into an enterprise workspace platform with hosted Sites, six role-specific plugins covering data analytics through investment banking, and scoped Annotations editing. If you're building vertical AI for any of those six domains, your competitive landscape just changed."
content_type: "Builder's Log"
categories: ["OpenAI", "Enterprise AI", "Agent Development", "Product Strategy"]
tags: ["openai", "codex", "codex-sites", "role-plugins", "enterprise-ai", "knowledge-workers", "annotations", "agentic-platform", "non-developers", "vertical-ai"]
---

On June 3, 2026, OpenAI held an "Intelligence at Work" event and shipped a Codex update that reframes what the platform is. Codex started as a coding agent for developers. After this update, it is also a configurable enterprise workspace for data analysts, marketers, salespeople, product designers, and investment bankers.

Three things shipped at once: Sites (OpenAI-hosted internal tools), six role-specific plugins, and Annotations (scoped in-place editing). None of them require coding knowledge.

---

## What Shipped

### Sites — OpenAI Hosts Your Internal Tools

Sites lets users build, deploy, and share web apps, dashboards, internal tools, and interactive documents — all hosted by OpenAI. No deployment pipeline, no IT ticket, no infrastructure.

Sites is in preview for ChatGPT Business and Enterprise customers. During preview it is free; pricing has not been announced. Enterprise admins control availability via RBAC in workspace settings.

What you can build: interactive data dashboards, lightweight internal apps, shareable reports, tools-with-instructions for non-technical teammates. The output is a URL that teammates can load directly.

The infrastructure implication is real. OpenAI is now in the business of hosting enterprise software. Your users — the ones who previously asked your SaaS for a dashboard — may start building their own in Codex and hosting it at OpenAI instead.

### Six Role-Specific Plugins

The six plugins are designed for specific jobs rather than specific technologies:

| Plugin | Target User | Sample Integrations |
|---|---|---|
| **Data Analytics** | Analysts, data teams | Snowflake, Databricks Genie, Hex, Tableau |
| **Creative Production** | Marketing, creative teams | Brief-to-asset workflows |
| **Sales** | Account executives, revenue ops | Sales stack tools |
| **Product Design** | Product and design teams | Design and PM tools |
| **Equity Investing** | Public equity analysts | Market data integrations |
| **Investment Banking** | IB analysts and associates | Financial model tools |

Together these six plugins bundle 62 apps and 110 automated skills. Non-developer users — analysts, operators, marketers, researchers — now constitute about 20% of Codex's 5 million weekly active users and are adopting the platform three times faster than engineers.

More plugins are on the roadmap: Corporate Finance, Private Equity Investing, Marketing Strategy, Strategy Consulting, and Legal.

### Annotations — Scoped In-Place Editing

Annotations is the feature that makes this credible for knowledge work. A user highlights a specific cell range in a financial model, prompts Codex to add a chart, and the model executes only within that boundary — leaving the rest of the document untouched.

Before Annotations, LLM editing of complex documents meant whole-document replacement, which breaks carefully structured spreadsheets, slides, and reports. Scoped editing closes the last friction point for document-heavy roles.

---

## What This Means for Builders

### Your Vertical May Now Be a Plugin

If you are building an AI product for data analytics, sales, marketing, product design, or finance, OpenAI just shipped a competing product with 62 prebuilt integrations and a $20/month price floor (Plus tier).

That is not a reason to stop building. But it changes the question from "does an AI product exist?" to "why is your product better than Codex for this specific workflow?"

The honest answer will vary by domain:

- **Depth over breadth**: Codex plugins are built for general workflows. If your product handles one domain at production depth — regulatory reporting for investment banking, or warranty analytics for manufacturing — Codex's generic sales plugin is not a substitute.
- **Data residency and compliance**: OpenAI-hosted Sites runs on OpenAI infrastructure. Enterprise buyers in regulated industries (healthcare, financial services, government) cannot route sensitive data through ChatGPT Business without explicit DPA and security review. On-prem and private cloud deployments remain the default requirement.
- **Integration ownership**: Codex connects to 62 apps via prebuilt connectors. If your workflow requires a proprietary internal system, a legacy API, or a niche vertical SaaS not in that list, you own the integration advantage.
- **Customization**: Role plugins are broad by design. The more domain-specific the workflow — the closer to "this is how this specific company does this thing" — the less a general plugin applies.

### The Sites Hosting Play

Sites positions OpenAI as a lightweight internal tools platform. This is a new competitive surface for companies in the low-code/no-code space and for builders who deliver dashboards and reports as a product.

The risk for builders: if a knowledge worker can describe a dashboard in a Codex prompt and get a hosted URL in minutes, they may not wait for your product's roadmap item. The response is either faster delivery (build that feature before they defect) or deeper lock-in (make sure your data layer is something they cannot replicate in a Codex prompt).

### The Non-Developer Growth Signal

20% of 5 million weekly users and growing 3x faster than the developer segment is a market signal. Knowledge workers who were never going to write code are now using Codex as a work tool. This expands the total addressable market for enterprise AI products while also creating the expectation that AI tools require no technical setup.

If your product requires IT installation, developer integration, or API key management, that expectation mismatch will drive non-developer buyers toward Codex alternatives.

---

## What to Watch

**Sites pricing**: Currently free in preview. When pricing lands, it will determine whether Sites becomes a default enterprise tool or an upsell feature. Free or bundled with existing plans makes this a strong incumbent play.

**Plugin expansion**: Corporate Finance, Private Equity, Marketing Strategy, Strategy Consulting, and Legal are confirmed next. Each launch narrows another vertical that previously had no direct OpenAI competition.

**Annotations stability**: Scoped editing in live documents is technically difficult. If it works reliably in production — particularly for financial models — it removes the last blocker for Codex adoption in document-heavy workflows.

**API access**: It is not yet clear whether Sites and role plugin functionality will be available via API or only through the Codex app. API access would let builders embed this capability; app-only locks users into ChatGPT as the front end.

---

*OpenAI's "Intelligence at Work" announcement was made June 3, 2026. Sites is in preview for Business and Enterprise teams. Role plugin availability follows existing subscription tiers (Plus at $20/month, Pro at $100/month, Business and Enterprise with seat licenses). This article covers the announcement and its strategic implications; ChatForest has not directly tested the features.*
