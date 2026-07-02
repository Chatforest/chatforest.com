---
title: "Gemini Spark Lands on Mac. Custom MCP Is Open. Here's What Builders Do Next."
date: 2026-07-01
description: "Google's Gemini Spark expanded to macOS on July 1 with local file automation, custom MCP support, and new integrations including Dropbox, GitHub, Notion, and Slack coming this summer. This is the builder's action guide: who benefits, how to connect your MCP server today, and what Windows teams are waiting on."
tags: ["google", "gemini", "gemini-spark", "mcp", "agents", "macos", "desktop", "builder-guide", "integrations"]
draft: false
---

On July 1, 2026, Google expanded Gemini Spark to macOS and opened custom Model Context Protocol (MCP) integration to all eligible users. The original Spark launch in May covered the cloud agent's general capabilities; this update addresses a different question: **can it reach your local files and your product's API?**

Now it can.

---

## What Changed on July 1

Three things happened simultaneously:

**1. Native macOS app.** Spark is now embedded in the Gemini desktop app for Mac. This isn't a browser wrapper — Spark can read and write local files, automate actions across your filesystem, and bridge local data to Google Workspace documents without manual copy-paste.

**2. Custom MCP integration.** Any developer can point Spark at an MCP server URL. Spark will call your server's tools on the user's behalf. The door that was reserved for launch partners in May is now open to anyone with an MCP endpoint.

**3. New first-party and partner integrations.** Google Keep and Google Tasks were added based on user feedback. Dropbox and Zillow Rentals joined Canva, Instacart, and OpenTable from the launch roster. And Adobe, Samsung, Spotify, GitHub, Notion, and Slack are confirmed as incoming MCP partners for summer 2026.

---

## What Local File Access Actually Means

Spark running on macOS can do things the cloud-only version could not:

- **File sorting and organization.** "Sort all PDFs in Downloads into client folders by date" — Spark executes this without a browser tab.
- **Cross-source document creation.** Take invoices stored locally, pull in financial data from a Google Sheet, produce a new budget document in Docs. Spark bridges the gap.
- **Scheduled local tasks.** Because Spark runs as a persistent agent, local automations can be scheduled: "Every Friday at 5pm, package the new weekly reports into a zip and notify me."
- **Phone → desktop delegation.** Coming soon (not live yet): assign a multi-step task from your phone and have Spark execute it on your Mac — grabbing local files, running actions, and sending results back.

The architecture remains cloud-side: Spark itself runs on Google Cloud VMs, not on your machine. What changed is that the macOS client gives it a secure bridge to your local filesystem.

---

## How to Connect Your MCP Server

If you ship a product with an MCP server, you can connect it to Spark today. Here's the process:

**Prerequisites:**
- User must be a Google AI Ultra subscriber in the US, age 18+
- Keep Activity must be enabled (Spark cannot connect to custom apps without it)
- You need a valid MCP server URL following the standard MCP spec

**Steps for your user:**
1. Go to [gemini.google.com](https://gemini.google.com) on desktop
2. Click **Settings & help → Connected Apps**
3. Under "Custom apps for Spark," enter your MCP server URL
4. If your server doesn't support Dynamic Client Registration, click **Show more** under Advanced features and enter credentials manually
5. Follow the on-screen authorization flow

Once connected via web, the integration is also available on Spark's mobile app — your users don't have to redo it per device.

**What Google tells users about security:** Google does not control, monitor, or secure third-party MCP servers. Users see a disclosure that they are responsible for trusting the provider and understanding what actions the server supports. Build your tool descriptions clearly — users are being told to read them.

---

## Where the Boundaries Are Right Now

**macOS only, Windows pending.** The desktop app is Mac-only at launch. Windows users can still use custom MCP through the web app, but don't get local file access. No public timeline for a Windows client.

**US only.** Spark and custom MCP connections are only available to US users. International expansion has not been announced.

**Google AI Ultra required.** Spark requires an Ultra subscription. This is a $249.99/month plan. Your target user for MCP integration is a high-intent, well-resourced Google customer — not the free tier.

**Web is the MCP config surface.** Custom apps are connected in the Gemini web app only. The macOS client picks them up after configuration — it's not a separate setup.

---

## The Competitive Picture

Gemini Spark is now directly competing with Claude Desktop and Microsoft Copilot on the desktop agent front:

| Agent | Desktop Client | Local Files | Custom MCP | Monthly Cost |
|---|---|---|---|---|
| Gemini Spark | macOS (July '26) | Yes (Mac only) | Yes | Google AI Ultra ($249.99) |
| Claude Desktop | macOS + Windows | Yes | Yes (broad) | Claude Pro/Max ($20–$200) |
| Microsoft Copilot | Windows-native | Partial | Limited | Microsoft 365 Copilot ($30/user) |

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

Adobe, Samsung, Spotify, GitHub, Notion, and Slack are the confirmed incoming partners. When they land, Spark's custom MCP slot will have stiff competition for user attention. Being early — listed in Google's own "Connected Apps" section rather than discoverable only via URL — may matter for discoverability.

Google has not announced a developer submission process for official partner status. The May article still applies: there is no form to file yet. For now, custom MCP via URL is the path in.

---

*The previous builder guide covering Gemini Spark's initial May 2026 launch, cloud architecture, and early integration strategy is [here](/builders-log/gemini-spark-mcp-connector-builder-guide-2026/).*
