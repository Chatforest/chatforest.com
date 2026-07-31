---
title: "Gemini Spark Lands on Mac. Custom MCP Is Open. Here's What Builders Do Next."
date: 2026-07-01
description: "Google's Gemini Spark expanded to macOS on July 1 with local file automation, custom MCP support, and new integrations including Dropbox and Zillow Rentals. This is the builder's action guide: who benefits, how to connect your MCP server today, and what Windows teams are waiting on."
tags: ["google", "gemini", "gemini-spark", "mcp", "agents", "macos", "desktop", "builder-guide", "integrations"]
draft: false
sources_audited: 2026-07-31
---

On July 1, 2026, Google [expanded Gemini Spark to macOS and opened custom Model Context Protocol (MCP) integration](https://blog.google/innovation-and-ai/products/gemini-app/gemini-spark-updates-june-2026/) to eligible users, [confirmed the same day by TechCrunch](https://techcrunch.com/2026/07/01/gemini-spark-googles-agentic-assistant-is-now-available-on-mac/). The original Spark launch in May covered the cloud agent's general capabilities; this update addresses a different question: **can it reach your local files and your product's API?**

Now it can.

---

## What Changed on July 1

Three things happened simultaneously:

**1. Native macOS app.** Spark is now embedded in [the Gemini desktop app for Mac](https://blog.google/innovation-and-ai/products/gemini-app/gemini-spark-updates-june-2026/), available via beta to Google AI Ultra subscribers. This isn't a browser wrapper — Spark can read and write local files the user grants it access to, automate actions across the filesystem, and bridge local data to Google Workspace documents without manual copy-paste.

**2. Custom MCP integration.** Any developer can point Spark at an MCP server URL through [Settings & help → Connected Apps in the Gemini web app](https://support.google.com/gemini/answer/17209137?hl=en&co=GENIE.Platform%3DDesktop). Spark will call your server's tools on the user's behalf. The door that was reserved for launch partners in May is now open to anyone with an MCP endpoint.

**3. New first-party and partner integrations.** [Google Keep and Google Tasks were added](https://blog.google/innovation-and-ai/products/gemini-app/gemini-spark-updates-june-2026/) based on user feedback, and Dropbox and Zillow Rentals joined Canva, Instacart, and OpenTable on the connected-apps roster. Google's own announcements say more MCP partners — [over 30, by Google's May estimate](https://blog.google/innovation-and-ai/products/gemini-app/next-evolution-gemini-app/) — are coming "this summer," but as of this writing Google has not named them. Specific candidates circulating in some trade coverage (Adobe, Samsung, Spotify, GitHub, Notion, Slack) trace back to analyst speculation, not a Google confirmation — treat that list as unverified.

---

## What Local File Access Actually Means

Spark running on macOS can do things the cloud-only version could not:

- **File sorting and organization.** Google's own example: ["sort all the PDFs in your Downloads into specific folders"](https://blog.google/innovation-and-ai/products/gemini-app/gemini-spark-updates-june-2026/) — Spark executes this without a browser tab.
- **Cross-source document creation.** Google's example: ["create a budget spreadsheet using the latest invoices saved to your computer"](https://blog.google/innovation-and-ai/products/gemini-app/gemini-spark-updates-june-2026/), pulling in local files rather than manual copy-paste.
- **Scheduled local tasks.** Because Spark runs as a persistent agent rather than a session tied to an open browser tab, local automations can be scheduled — Google frames this as the core difference from a chat-only assistant.
- **Phone → desktop delegation.** [Coming soon, not live yet](https://blog.google/innovation-and-ai/products/gemini-app/gemini-spark-updates-june-2026/): assign a multi-step task from your phone and have Spark execute it on your Mac while you're away.

The architecture remains cloud-side: [Spark itself runs on dedicated Google Cloud virtual machines, not on your machine](https://techcrunch.com/2026/05/19/google-introduces-gemini-spark-a-24-7-agentic-assistant-with-gmail-integration/) — Google says this is so a task keeps running even if you close your laptop. What changed on macOS is that the client gives it a secure, permissioned bridge to your local filesystem, not that the model moved on-device.

---

## How to Connect Your MCP Server

If you ship a product with an MCP server, you can connect it to Spark today. Here's the process:

**Prerequisites** ([per Google's own support documentation](https://support.google.com/gemini/answer/17209137?hl=en&co=GENIE.Platform%3DDesktop)):
- User must be 18+, in the US, and signed in with a personal Google Account (not work/school) — and have Spark access, which requires a Google AI Ultra subscription
- Keep Activity must be enabled (Spark cannot connect to custom apps without it)
- You need a valid MCP server URL following the standard MCP spec

**Steps for your user** ([Google's connect-apps walkthrough](https://support.google.com/gemini/answer/17209137?hl=en&co=GENIE.Platform%3DDesktop)):
1. Go to [gemini.google.com](https://gemini.google.com) on desktop
2. Click **Settings & help → Connected Apps**
3. Under "Custom apps for Spark," enter your MCP server URL
4. If your server doesn't support Dynamic Client Registration, click **Show more** under Advanced features and enter credentials manually
5. Follow the on-screen authorization flow

Once connected via web, [the integration is also available on Spark's mobile app automatically](https://support.google.com/gemini/answer/17209137?hl=en&co=GENIE.Platform%3DDesktop) — your users don't have to redo it per device.

**What Google tells users about security:** Google's own guidance says [third-party MCP servers operate "outside Google's control," and that "it's very important that you know and trust the custom third-party MCP server before connecting"](https://support.google.com/gemini/answer/17209137?hl=en&co=GENIE.Platform%3DDesktop). Users are told they're responsible for reviewing the provider's privacy policy and terms and understanding what actions the server supports. Build your tool descriptions clearly — users are being told to read them.

---

## Where the Boundaries Are Right Now

**macOS only, Windows pending.** [The desktop app is Mac-only at launch](https://blog.google/innovation-and-ai/products/gemini-app/gemini-spark-updates-june-2026/). Windows users can still use custom MCP through the web app, but don't get local file access. No public timeline for a Windows client.

**US only.** [Spark and custom MCP connections are only available to US users 18 and older](https://support.google.com/gemini/answer/17209137?hl=en&co=GENIE.Platform%3DDesktop). International expansion has not been announced.

**Google AI Ultra required.** Spark requires an Ultra subscription. Google [cut Ultra's price at I/O 2026](https://blog.google/products-and-platforms/products/google-one/google-ai-subscriptions/) to two tiers — $99.99/month (5x Pro's usage limits, includes Spark) or $199.99/month (20x limits) — down from the original $249.99/month launched in 2025; [MacRumors confirms the current entry price as $99 per month](https://www.macrumors.com/2026/07/01/google-gemini-spark-comes-to-mac/) for July's macOS rollout. Your target user for MCP integration is a high-intent, well-resourced Google customer — not the free tier.

**Web is the MCP config surface.** Custom apps are connected in the Gemini web app only. The macOS client picks them up after configuration — it's not a separate setup.

---

## The Competitive Picture

Gemini Spark is now directly competing with Claude Desktop and Microsoft Copilot on the desktop agent front:

| Agent | Desktop Client | Local Files | Custom MCP | Monthly Cost |
|---|---|---|---|---|
| Gemini Spark | macOS (July '26) | Yes (Mac only) | Yes | [Google AI Ultra ($99.99–$199.99)](https://blog.google/products-and-platforms/products/google-one/google-ai-subscriptions/) |
| Claude Desktop | [macOS + Windows](https://support.claude.com/en/articles/10949351-getting-started-with-local-mcp-servers-on-claude-desktop) | Yes | Yes (broad) | [Claude Pro/Max ($20–$200)](https://claude.com/pricing) |
| Microsoft Copilot | Windows-native | Partial | Limited | [Microsoft 365 Copilot ($30/user)](https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-licensing) |

Spark's advantage is deep Google Workspace integration and scheduled autonomous cloud execution. Claude Desktop's advantage is broader OS support and a more mature MCP ecosystem. Copilot's advantage is enterprise seat penetration.

The differentiator for your MCP server: Spark users are Google-ecosystem-heavy. If your product connects to Gmail, Drive, Calendar, or Docs, a Spark integration is unusually high-leverage — the user already has all that context open.

---

## Builder Checklist

**If you already have an MCP server:**

- [ ] Test it against the Gemini Spark MCP connection flow — use the web app, enter your URL, watch for auth errors
- [ ] Review your tool descriptions: users see them during authorization and Spark uses them for routing
- [ ] Check for Dynamic Client Registration support — if you don't have it, provide clear credential docs
- [ ] Monitor your server logs for Spark's user-agent identifier to separate Spark traffic from other MCP clients

**If you don't have an MCP server yet:**

- [ ] Assess whether your product's core action (CRUD, query, trigger) is expressible as 3–5 tools
- [ ] Review the official MCP spec and Gemini Spark's custom app documentation before building
- [ ] Build toward supporting Dynamic Client Registration — it removes the manual credential step and lowers abandonment

**If your product is Google Workspace-adjacent:**

- [ ] This is the highest-priority integration opportunity: Spark can chain your data with Drive, Sheets, and Docs natively
- [ ] Consider use cases that cross the local-to-cloud boundary — that's where Spark has no competitor today

---

## What to Watch This Summer

Google has said [more MCP partners are coming this summer](https://blog.google/innovation-and-ai/products/gemini-app/next-evolution-gemini-app/) without naming them specifically. When named partners do land — in whatever form Google ships them — Spark's custom MCP slot will have stiff competition for user attention. Being early, and eventually listed in Google's own "Connected Apps" section rather than discoverable only via URL, may matter for discoverability.

Google has not announced a developer submission process for official partner status. The May article still applies: there is no form to file yet. For now, custom MCP via URL is the path in for any builder.

---

*The previous builder guide covering Gemini Spark's initial May 2026 launch, cloud architecture, and early integration strategy is [here](/builders-log/gemini-spark-mcp-connector-builder-guide-2026/).*
