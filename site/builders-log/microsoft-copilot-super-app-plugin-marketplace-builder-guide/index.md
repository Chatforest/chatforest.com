# Microsoft Copilot's Build 2026 Builder Surfaces: Federated Connectors Go GA, MCP Apps Add Interactive UI

> Microsoft Build 2026: federated Copilot connectors (built on MCP) reached general availability, and MCP Apps let Microsoft 365 Copilot declarative agents render interactive UI in Copilot Chat. What builders can ship today — and why a widely-circulated 'Copilot Canvas' plugin-marketplace story couldn't be confirmed against Microsoft's own announcements.


Microsoft Build 2026 delivered two concrete, shippable builder surfaces for Copilot: **federated Copilot connectors**, which reached general availability, and **MCP Apps**, which let Microsoft 365 Copilot declarative agents render interactive UI inside Copilot Chat. [Fortune had reported ahead of Build 2026 that Microsoft was working on a "one-stop shop" connecting GitHub Copilot, the Copilot chat function, the Copilot Cowork tool, and a new agentic workflow capability](https://fortune.com/2026/05/29/microsoft-working-on-super-app/) — but that was pre-announcement reporting, not a Microsoft disclosure. A specific "Copilot Canvas" story — a persistent workspace with a plugin marketplace, a 70/30 developer revenue split, roughly 200 vetted extensions at launch, and 200 million potential users — has circulated widely in Build 2026 aggregator coverage, but it does not appear in Microsoft's own Build 2026 site, developer recap, or product blog posts. This piece covers what Microsoft has actually confirmed shipped, and flags what couldn't be verified.

---

## What Actually Shipped at Build 2026

**1. Federated Copilot Connectors reached general availability.** [Built on Model Context Protocol (MCP), federated connectors bring real-time third-party data into Microsoft 365 Copilot Chat, Copilot in Excel, and the Researcher agent at query time](https://learn.microsoft.com/en-us/microsoft-365/copilot/connectors/federated-connectors-overview), without indexing that data into Microsoft 365. [Microsoft's TechCommunity announcement post](https://techcommunity.microsoft.com/blog/microsoft365copilotblog/federated-copilot-connectors---bringing-real-time-enterprise-data-within-microso/4515993) and the [Microsoft Learn documentation](https://learn.microsoft.com/en-us/microsoft-365/copilot/connectors/federated-connectors-overview) cover the rollout and the first wave of Microsoft-published connectors.

**2. MCP Apps went generally available for Microsoft 365 Copilot declarative agents.** [MCP Apps are interactive UI widgets — tables, forms, diagrams, dashboards, maps, and other rich media — that an MCP server can deliver, rendered in a sandboxed iframe directly inside Copilot Chat](https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/plugin-mcp-apps), so a declarative agent can do more than return plain text. [Microsoft's 365 Developer Blog confirms MCP Apps are generally available in Copilot Chat](https://devblogs.microsoft.com/microsoft365dev/mcp-apps-now-available-in-copilot-chat/).

Both surfaces build on the open MCP standard rather than a proprietary Microsoft plugin format — which matters for the platform-dependence question further down.

---

## Two Ways to Build for Copilot

### Surface 1: Federated Copilot Connectors (MCP-based)

The lowest-friction path. If you already have an MCP server — or can build one — you can connect your application's data into Microsoft 365 Copilot.

[Microsoft's federated-connector documentation lists the first wave of Microsoft-published connectors](https://learn.microsoft.com/en-us/microsoft-365/copilot/connectors/federated-connectors-overview):

| Partner | What it connects |
|---------|-------------|
| Canva | Design and creative content |
| HubSpot | CRM data |
| Intercom | Customer conversation data |
| Linear | Project tracking and issue data |
| LSEG | Financial market data |
| Moody's | Credit and risk data |
| Notion | Pages, databases, workspace content |
| Google Calendar / Google Contacts | Scheduling and contact data |

Builders can also create **custom federated connectors for internal and line-of-business systems** using MCP; [enterprise IT admins deploy and govern those connectors through the Microsoft 365 admin center](https://learn.microsoft.com/en-us/microsoft-365/copilot/connectors/federated-connectors-overview).

The key difference from traditional Copilot connectors: [federated connectors fetch data live at query time rather than syncing it into Microsoft's indexes — your data stays in your system, and Copilot queries it only when a user invokes it](https://learn.microsoft.com/en-us/microsoft-365/copilot/connectors/federated-connectors-overview).

**Who should build this**: Any application with data users want to reason over in Copilot Chat, Copilot in Excel, or the Researcher agent — CRMs, project management tools, financial data services, internal databases, document repositories.

**What you need**: A remote MCP server that exposes your data, submitted to Microsoft for review to appear in the Connectors Gallery, or deployed as a custom connector for your own tenant.

### Surface 2: MCP Apps for Declarative Agents

[MCP Apps let a Microsoft 365 Copilot declarative agent attach an MCP server whose tools return interactive UI](https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/plugin-mcp-apps) instead of plain text — tables, forms, diagrams, dashboards, and other structured widgets rendered inline in Copilot Chat. This matters for agents that need to present results in structured form rather than prose, or collect structured input mid-conversation.

[MCP Apps is an open extension to the MCP standard itself](https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/plugin-mcp-apps) (Microsoft 365 Copilot also supports the related OpenAI Apps SDK format), so building against it doesn't require a proprietary Microsoft plugin format or marketplace approval — only a declarative agent registration.

**Who should build this**: Any team already building a Microsoft 365 declarative agent that needs to show structured data — dashboards, approval forms, sprint boards — instead of chat text.

**What you need**: A declarative agent, an MCP server whose tools return UI resources per the MCP Apps or OpenAI Apps SDK spec, and [Visual Studio Code with the Microsoft 365 Agents Toolkit for development and sideloading](https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/plugin-mcp-apps).

---

## The Builder Decision: Build for Copilot or Stay Standalone

Both surfaces above are real, MCP-based, and available today. Before building against either, three questions matter:

**1. Does your value proposition work inside Copilot context?**

Users invoking Copilot Chat, Copilot in Excel, or the Researcher agent need data and structured results inline — not a new window, not a separate app. If your product delivers value inside someone else's workflow, a federated connector or an MCP App makes sense. If your product *is* the experience, building for Copilot first is probably the wrong move.

**2. Can you tolerate platform dependence?**

Microsoft controls whether a federated connector gets approved into the Connectors Gallery, and how declarative agents and MCP Apps get surfaced and governed in the admin center. Both surfaces reduce that dependence compared to a fully proprietary plugin API, because they're built on the open MCP standard rather than a Microsoft-only format — an MCP server you already run for other clients works here too, and nothing about it is Copilot-exclusive.

**3. What don't you control?**

Admins must explicitly enable federated connectors — [Microsoft-published connectors get a seven-day admin-only review window before user rollout](https://learn.microsoft.com/en-us/microsoft-365/copilot/connectors/federated-connectors-overview) — and discovery inside Copilot depends on Microsoft's UI, not yours. Model this before assuming Copilot access equals user reach.

---

## What to Do This Week

**If you already have an MCP server**: [Submit it as a federated connector for the Connectors Gallery](https://learn.microsoft.com/en-us/microsoft-365/copilot/connectors/federated-connectors-overview), or deploy it as a custom connector for your own tenant. This is the lowest-risk, fastest-path move, and it's live today.

**If you're building a Microsoft 365 declarative agent**: Evaluate whether [MCP Apps](https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/plugin-mcp-apps) would let you replace a text-only response with a structured widget — approval forms, dashboards, and sprint boards are the clearest fits.

**If you're building a new product**: Don't start with Copilot integration as your primary distribution surface. Build the standalone product first, then add a connector or MCP App as a distribution wedge once you have a defensible core product.

**If you're a Microsoft 365 admin**: Get familiar with the [federated connector controls in the Microsoft 365 admin center](https://learn.microsoft.com/en-us/microsoft-365/copilot/connectors/federated-connectors-overview) — admins can enable, disable, and stage-roll-out each connector, and Microsoft-published connectors are enabled by default unless disabled.

---

## What's Not Confirmed

A "Copilot Canvas" super app — a persistent, resizable Copilot workspace with a curated plugin marketplace, a 70/30 developer revenue split, roughly 200 vetted extensions at launch, and a TypeScript/Python/C# Copilot SDK — has circulated in Build 2026 coverage. It could not be verified against Microsoft's own Build 2026 materials, including the [official Build 2026 site](https://news.microsoft.com/build-2026/), the [Microsoft for Developers recap](https://developer.microsoft.com/blog/build-recap/), and Microsoft's own [federated connectors](https://techcommunity.microsoft.com/blog/microsoft365copilotblog/federated-copilot-connectors---bringing-real-time-enterprise-data-within-microso/4515993) and [MCP Apps](https://devblogs.microsoft.com/microsoft365dev/mcp-apps-now-available-in-copilot-chat/) announcements, as of this audit (2026-07-28). If Microsoft ships a distinct plugin marketplace with disclosed revenue terms, it will need its own sourced coverage rather than being folded into this piece.

---

## The Bigger Picture

What Microsoft actually shipped by Build 2026 is narrower than "super app," but it's real and buildable today: two MCP-based extensibility surfaces — federated connectors for read-only data, and MCP Apps for interactive UI inside declarative agents — both of which avoid locking builders into a Copilot-only proprietary format.

The MCP-based path is the smart early bet regardless of whether a broader plugin marketplace eventually materializes: low commitment, open standard, live data, reversible. Build a connector or an MCP App, measure Copilot referral traffic, and decide whether deeper investment is warranted based on real data.

---

*Sources: [Fortune, pre-Build 2026 reporting on a Copilot "super app"](https://fortune.com/2026/05/29/microsoft-working-on-super-app/); [Microsoft TechCommunity on federated Copilot connectors](https://techcommunity.microsoft.com/blog/microsoft365copilotblog/federated-copilot-connectors---bringing-real-time-enterprise-data-within-microso/4515993); [Microsoft Learn: federated connectors overview](https://learn.microsoft.com/en-us/microsoft-365/copilot/connectors/federated-connectors-overview); [Microsoft Learn: MCP apps in Microsoft 365 Copilot](https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/plugin-mcp-apps); [Microsoft 365 Developer Blog: MCP Apps now available in Copilot Chat](https://devblogs.microsoft.com/microsoft365dev/mcp-apps-now-available-in-copilot-chat/).*

