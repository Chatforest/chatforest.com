# Microsoft Copilot Is Now a Super App: What Builders Need to Know About the Plugin Marketplace

> Microsoft Copilot transformed from sidebar assistant to full-blown super app at Build 2026. Copilot Canvas, a new plugin marketplace with 70/30 revenue split, federated MCP connectors GA, and a TypeScript/Python/C# extension SDK. Here's the builder's guide to the new distribution channel.


Microsoft Build 2026 shipped something most builders are underestimating: a new distribution channel with 200 million potential users and a 70/30 revenue split.

It's called Copilot Canvas. It used to be called the Copilot sidebar.

---

## What Changed at Build 2026

For two years, Microsoft Copilot was a competent-but-limited AI assistant embedded in Windows and Microsoft 365 apps. Useful, but not a platform builders could build businesses on top of.

That changed at Build 2026 with three interconnected announcements:

**1. Copilot Canvas** — Copilot is no longer a sidebar. It's now a persistent workspace that can snap to the side of any screen or float as a resizable window. Inside the Canvas, users can drop files, images, code snippets, and live web widgets. Copilot maintains context across everything — a spreadsheet open in Excel, a codebase in Visual Studio, a design in Canva, a deal in HubSpot — and can operate across those surfaces simultaneously. The Canvas also introduces a universal inbox and a project workspace that persist across sessions.

**2. Plugin Marketplace with Revenue Model** — Microsoft is launching a curated extension marketplace for Copilot, expected to open with around 200 vetted third-party extensions. For the first time, Microsoft has disclosed a developer revenue share: **70% to developers after payment processing fees**. This isn't a beta API program — it's a monetization surface.

**3. Federated Copilot Connectors GA** — Built on Model Context Protocol (MCP), federated connectors bring real-time third-party data into Microsoft 365 Copilot at query time. These reached general availability with a first wave of major partners and are immediately open to custom builders.

---

## Three Ways to Build for Copilot

Microsoft has created three distinct distribution surfaces at Build 2026. They're different in complexity, control, and revenue potential.

### Surface 1: Federated Copilot Connectors (MCP-based)

The lowest-friction path. If you already have an MCP server — or can build one — you can connect your application's data into Microsoft 365 Copilot and GitHub Copilot.

The first wave of launch partners shows the range of data types this works for:

| Partner | Data Surface |
|---------|-------------|
| Canva | Designs, brand templates, creative performance data |
| HubSpot | Deal and contact information |
| Intercom | Customer conversation data |
| Linear | Project tracking and issue data |
| LSEG | Financial market data (also coming to Excel) |
| Moody's | Credit and risk data (also coming to Excel) |
| Notion | Pages, databases, workspace content |
| Google Calendar / Contacts | Scheduling and contact data |

Builders can also create **custom federated connectors for internal and line-of-business systems** using MCP. Enterprise IT admins can then deploy those connectors organization-wide through the Microsoft 365 admin center.

The key difference from traditional Copilot connectors: federated connectors fetch data **live at query time** rather than syncing it to Microsoft's indexes. Your data stays in your system. Microsoft queries it only when a user invokes it from Copilot.

**Who should build this**: Any application with data users want to reason over in Copilot. CRMs, project management tools, financial data services, internal databases, document repositories. If your data is currently siloed away from where people do their AI-assisted work, a federated connector closes that gap.

**What you need**: An MCP server that exposes your data, registered as a federated connector through Azure. Microsoft's Learn documentation has the full connector schema.

### Surface 2: Plugin Marketplace Extensions

The higher-complexity, higher-monetization surface. Plugins are more than data connectors — they're interactive, can take actions, and render UI directly inside Copilot Canvas.

The new **Copilot SDK** supports TypeScript, Python, and C#. A plugin is defined by a metadata file that describes what the skill does (similar to Alexa Skills or ChatGPT plugins), plus the action code itself. Registered skills can surface in:

- The Copilot side panel
- File Explorer
- The Windows taskbar
- The Canvas workspace

Plugins can:
- Tap into Windows AI models for local NPU inference (no API call needed)
- Call any REST API
- Access the local file system, local network services, and hardware sensors (with user permission)

**Revenue model**: 70/30 split in the developer's favor, after payment processing fees. Marketplace opens with ~200 vetted extensions. Microsoft hasn't disclosed whether they plan a curated or open submission model after launch.

**Who should build this**: If you're already serving Windows or Microsoft 365 users, and you have a workflow they currently context-switch out of Copilot to complete, building an extension keeps them in one place. Productivity tools, coding utilities, research services, and data enrichment tools are the most natural fits.

### Surface 3: Declarative Agents with MCP Apps

Between connectors and full plugins sits a third path: MCP Apps for M365 Copilot declarative agents.

MCP Apps let a declarative Copilot agent render interactive UI directly inside Copilot Chat — not just return text, but show cards, buttons, and structured data. This is significant for agents that need to present results in structured form (tables, timelines, dashboards) rather than prose.

This surface is still more limited than full Canvas plugins, but it's also less gatekept — it builds directly on the MCP standard rather than requiring marketplace approval.

---

## The Builder Decision: Copilot Extension vs. Standalone Product

Microsoft's Copilot distribution channel is genuinely large. Windows is installed on over 1.5 billion devices. Microsoft 365 has over 400 million commercial seats. Any plugin in the Copilot marketplace has implicit access to that install base — pending user discovery and installation.

But "large install base" doesn't mean "easy distribution." ChatGPT's plugin store was also large, and most plugins never found meaningful traction. The same dynamics apply here.

Before building for this platform, three questions matter:

**1. Does your value proposition work inside Copilot context?**

Copilot Canvas users are doing AI-assisted work. They need data, actions, and results inline — not a new window, not a separate app. If your product delivers value inside a workflow (not as a standalone experience), a Copilot extension makes sense. If your product *is* the experience — a standalone app with its own UX — an extension is probably the wrong model.

**2. Do your economics work at 70/30?**

70% sounds developer-favorable, but if your product is currently direct-sold or API-billed at higher margins, the marketplace cut plus the reduced pricing pressure (Copilot users expect simple, bundled pricing) may compress your revenue per user. Model this before building.

**3. Can you tolerate platform dependence?**

Microsoft controls the marketplace approval, the discovery algorithm, the billing, and the SDK. They've already pivoted Copilot's underlying architecture multiple times (OpenAI → Polaris, sidebar → Canvas). Building a significant business line on Copilot extensions means accepting that dependency. The federated connector path carries less dependence — it's an MCP server Microsoft queries, not a binary Microsoft distributes.

---

## What to Do This Week

**If you already have an MCP server**: File for federated Copilot connector registration now. The documentation is live, the first-wave partners are already indexed, and early connectors benefit from discovery advantage while the catalog is small. This is the lowest-risk, fastest-path move.

**If you serve Windows or M365 enterprise users**: Evaluate whether one of your workflows qualifies for a Canvas plugin. The 70/30 revenue split is competitive with other platform marketplaces, and the enterprise-quality user segment may accept premium pricing.

**If you're building a new product**: Don't start with a Copilot extension as the primary surface. Build the standalone product first, then add a connector or plugin as a distribution wedge. The Canvas is a good *second* channel, not a primary one.

**If you're a Microsoft 365 admin**: Get familiar with the new Copilot admin center controls for deploying and managing federated connectors. Your organization will have an immediate question when teams discover they can bring HubSpot and Linear data into Copilot: who approves which connectors, and what are the data residency implications?

---

## What's Not Yet Clear

A few things Microsoft hasn't disclosed as of Build 2026 Day 1:

- **Marketplace submission process**: Open or curated after the initial 200? Timeline for developer applications?
- **Revenue payout mechanics**: Stripe? Azure billing integration? Minimum thresholds?
- **Discovery algorithm**: What determines which plugins surface to which users?
- **Copilot Canvas availability date**: Announced at Build 2026, but general availability date not confirmed
- **MAI model access from plugins**: Can plugins invoke MAI-Thinking-1 and MAI-Image-2.5, or only the standard Windows AI models?

Day 2 of Build 2026 runs June 3. Some of these questions may get answers then.

---

## The Bigger Picture

Microsoft is building a platform play here that looks more like WeChat than Windows Store. Copilot Canvas is meant to be the surface where work happens — not an app launcher, but the work environment itself, with plugins bringing the apps inside rather than apps existing outside.

Whether it achieves that depends on developer adoption. Microsoft has made the economics reasonable (70/30, MCP-compatible, multi-language SDK) and the install base is real. But they've also tried similar things before — Office Add-ins, SharePoint extensions, Teams apps — with mixed results.

The MCP connectors path is the smart early bet: low commitment, open standard, live data, reversible. Build a connector, measure Copilot referral traffic, and decide whether the full plugin investment is warranted based on real data.

---

*ChatForest covers AI builder news and tools. Read [Rob Nugen's](https://robnugen.com) posts at [robnugen.com](https://robnugen.com).*

