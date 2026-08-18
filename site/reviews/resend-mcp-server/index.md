# Resend MCP Server — The Developer-First Email API With Full AI Agent Access

> Resend's official MCP server gives AI agents full email platform control — send, receive, manage contacts, run broadcast campaigns, and configure domains.


**At a glance:** [562+ stars](https://github.com/resend/resend-mcp), MIT license, TypeScript, 30+ MCP tools across [16 tool categories as of August 2026](https://github.com/resend/resend-mcp) (up from 10 at this review's original writing — the server has grown to add Templates, Automations, Events, Suppressions, Logs, and Editor tools), stdio + Streamable HTTP transport, free tier (3,000 emails/month). Actively developed — [npm v2.13.0](https://www.npmjs.com/package/resend-mcp), commits ongoing as of August 2026.

[Resend](https://github.com/resend/resend-mcp) is the email API built for developers — clean REST endpoints, React Email integration for writing templates as components, and strong deliverability out of the box. Their official MCP server turns the entire Resend platform into tools that AI agents can use directly: send emails with attachments, manage contact lists, run broadcast campaigns, configure domains, and set up webhooks — all through natural language.

Unlike most email MCP servers that only handle sending, Resend's MCP server exposes the full platform. This isn't just "let the AI send an email" — it's "let the AI manage your entire email infrastructure."

The key question: does an AI agent actually need this much email control, and is it safe to give it?

## Updates Since Original Review (March → May 2026)

Resend had one of the most active 42-day periods in the MCP ecosystem. Here's what changed:

**Launch Week 6 (April 2026)** — Resend shipped five major features:
- [**Automations**](https://resend.com/blog/introducing-automations) — lifecycle email sequences triggered by app events, accessible via the API, Dashboard, SDKs, the MCP Server, or the CLI. Create automations, define events, and inspect runs directly from an MCP client. The [Free plan includes 10,000 automation runs per month](https://resend.com/pricing).
- [**AI Email Editor**](https://resend.com/blog/ai-email-editor) — AI built directly into the email editor for composing, editing, and reviewing emails faster.
- [**Resend CLI 2.0**](https://resend.com/blog/resend-cli-2) — 50+ commands covering the full Resend API from the terminal.
- [**Custom Tracking Domains**](https://resend.com/blog/introducing-custom-tracking-domain) — free for all users, improving deliverability and brand consistency.
- [**React Email 6.0**](https://resend.com/blog/react-email-6) — new open-source visual editor as a standalone package.

[**Official MCP page launched**](https://resend.com/changelog/mcp) (April 7, 2026) — Resend now has a dedicated [`resend.com/mcp`](https://resend.com/mcp) page and [`resend.com/agents`](https://resend.com/agents) landing page, signaling first-class commitment to AI agent integration. The MCP server went from a side project to a named product.

[**Embedded Charts**](https://resend.com/changelog/chart-component) (April 30, 2026) — bar, line, and area charts now embeddable in emails, configurable through the editor's inspector sidebar.

[**New Email Editor**](https://resend.com/changelog/introducing-the-new-email-editor) (March 12, 2026) — completely rebuilt no-code editor for broadcasts, templates, and unsubscribe pages.

**Active development:** [npm package at v2.13.0](https://www.npmjs.com/package/resend-mcp), [commits continuing through August 2026](https://github.com/resend/resend-mcp/commits/main) — the server is under continuous development.

---

## What It Does

Resend's MCP server exposes 30+ tools. This review's original tables (below) cover the 10 categories documented as of the May 2026 refresh; [per the current README](https://github.com/resend/resend-mcp), the server has since grown to 16 categories, adding **Templates** (create, list, get, update, publish, duplicate, remove), **Automations**, **Events** (trigger automations), **Suppressions**, **Logs** (API request inspection), and an **Editor** integration:

### Emails

| Tool | Purpose |
|------|---------|
| **send_email** | Send an email with HTML, plain text, attachments (file, URL, base64), CC/BCC, reply-to, scheduling, and tags |
| **batch_send_emails** | Send multiple emails in a single request |
| **list_emails** | List sent emails with filtering |
| **get_email** | Get details and delivery status of a specific email |
| **update_email** | Update a scheduled email before it's sent |
| **cancel_email** | Cancel a scheduled email |

### Received Emails

| Tool | Purpose |
|------|---------|
| **list_received_emails** | List inbound emails received through Resend |
| **get_received_email** | Read a specific received email |
| **list_received_email_attachments** | List attachments on a received email |
| **download_received_email_attachment** | Download an attachment from a received email |

### Contacts

| Tool | Purpose |
|------|---------|
| **create_contact** | Add a contact to an audience with custom properties |
| **list_contacts** | List contacts in an audience |
| **get_contact** | Get contact details |
| **update_contact** | Update contact properties, segments, and topic subscriptions |
| **remove_contact** | Remove a contact from an audience |

### Broadcasts

| Tool | Purpose |
|------|---------|
| **create_broadcast** | Create a broadcast campaign with scheduling and personalization |
| **send_broadcast** | Send a created broadcast to its audience |
| **list_broadcasts** | List all broadcast campaigns |
| **get_broadcast** | Get broadcast details and stats |
| **update_broadcast** | Update a broadcast before sending |
| **remove_broadcast** | Delete a broadcast campaign |

### Domains

| Tool | Purpose |
|------|---------|
| **create_domain** | Add and configure a sender domain |
| **list_domains** | List all verified and pending domains |
| **get_domain** | Get domain configuration details |
| **update_domain** | Update tracking, TLS, and capability settings |
| **remove_domain** | Remove a sender domain |
| **verify_domain** | Trigger domain DNS verification |

### Segments, Topics, Contact Properties, API Keys, Webhooks

Additional tool groups for managing audience segments, subscription topics, custom contact attributes, API key lifecycle, and webhook event subscriptions — each with standard CRUD operations.

## Setup

### Via npx (Recommended)

No installation needed — run directly:

```json
{
  "mcpServers": {
    "resend": {
      "command": "npx",
      "args": ["-y", "resend-mcp"],
      "env": {
        "RESEND_API_KEY": "re_your_api_key_here"
      }
    }
  }
}
```

### Claude Code

```bash
claude mcp add resend -- npx -y resend-mcp
```

Then set your `RESEND_API_KEY` environment variable.

### Cursor

Add the same npx configuration to your Cursor MCP settings file.

### HTTP Transport

For remote or multi-agent setups, the server also supports HTTP transport mode — useful for shared infrastructure or when multiple agents need email access simultaneously.

### Prerequisites

1. Create a free [Resend account](https://resend.com)
2. Generate an API key from the Resend dashboard
3. To send to addresses outside your own, verify your domain (SPF/DKIM/DMARC)

**Setup difficulty: Low.** One npx command, one API key. Domain verification is optional for testing but required for production sending. No Docker, no build steps.

## Key Capabilities

### Full Email Lifecycle

Most email MCP servers only send emails. Resend's covers the full lifecycle: compose and send (with HTML, attachments, scheduling), track delivery status, cancel scheduled sends, read inbound emails, and download attachments. An AI agent can both send and receive — enabling autonomous email workflows like "check for replies and respond."

### Broadcast Campaigns

The broadcast tools turn the MCP server into a lightweight email marketing platform. An agent can create a campaign, set personalization variables, schedule it, and send it to an audience segment — all without touching a dashboard. This is unusual for an MCP server; most email integrations stop at transactional sending.

### Contact Management

Full CRM-lite functionality: create contacts with custom properties, organize them into segments, manage topic subscriptions. An agent could maintain a mailing list, segment subscribers by behavior, and clean up bounced contacts — tasks that typically require a marketing automation platform.

### React Email Integration

Resend's signature feature is [React Email](https://react.email/) — writing email templates as React components. While the MCP server doesn't compile React templates directly, it sends HTML that React Email generates, keeping the developer-to-agent workflow clean: developers design templates in React, agents send them through MCP.

### Domain and Deliverability Management

Agents can add domains, check verification status, configure open/click tracking, and manage TLS settings. This is the infrastructure layer — useful for DevOps-style automation where an agent sets up email sending for a new project or troubleshoots deliverability issues.

## Pricing

[Resend's pricing](https://resend.com/pricing) applies to the underlying API (the MCP server itself is free and open source):

| Plan | Price | Emails/Month | Domains | Support |
|------|-------|-------------|---------|---------|
| **Free** | $0 | 3,000 | 1 | Ticket support |
| **Pro** | $20/mo (or $35/mo for 100,000) | 50,000 | 10 | Ticket support |
| **Scale** | $90–$1,150/mo (scales to 2,500,000 emails) | 100,000+ | 1,000 | Slack & ticket support |
| **Enterprise** | Custom | Custom | Custom | Dedicated |

The free tier covers 3,000 emails per month with no credit card required — enough for development, testing, and low-volume transactional email. Pro at $20/month for 50K emails is competitive with SendGrid and Postmark at the same price point. (Pricing verified against [resend.com/pricing](https://resend.com/pricing) as of August 2026; plans and tiers change over time.)

## Compared to Other Email MCP Servers

| Feature | Resend | Mailgun | Postmark | SendGrid |
|---------|--------|---------|----------|----------|
| **GitHub stars** | [562](https://github.com/resend/resend-mcp) | [58](https://github.com/mailgun/mailgun-mcp-server) | [54](https://github.com/ActiveCampaign/postmark-mcp) | [29](https://github.com/Garoth/sendgrid-mcp) (community) |
| **Official** | Yes (Resend) | Yes (Mailgun) | Yes (ActiveCampaign) | Community |
| **MCP tools** | 30+ | 15+ | [24](https://github.com/ActiveCampaign/postmark-mcp) | ~8 |
| **Send email** | Yes | Yes | Yes | Yes |
| **Receive email** | Yes | Yes | No | No |
| **Contacts/lists** | Yes | Yes (mailing lists) | No | Yes |
| **Broadcasts** | Yes | No | No | Yes (single sends) |
| **Domain management** | Yes | Yes | No | No |
| **Webhooks** | Yes | Yes | No | No |
| **API key management** | Yes | No | No | No |
| **Transport** | stdio + HTTP | stdio | stdio | stdio |
| **License** | MIT | Apache 2.0 | MIT | MIT |
| **Free tier** | 3,000 emails/mo | 1,000 emails/mo (trial) | 100 emails/mo | 100 emails/day |

### vs. Mailgun

[Mailgun's MCP server](https://github.com/mailgun/mailgun-mcp-server) is the closest competitor in scope — it covers messaging, domains, routes, mailing lists, templates, analytics, and suppressions. Mailgun has deeper analytics (sending metrics, usage metrics, provider/device/country breakdowns) and inbound routing rules. Resend wins on breadth (broadcasts, segments, topics, contact properties, API keys) and developer experience. Choose Mailgun for analytics-heavy email ops; choose Resend for the full marketing + transactional stack.

### vs. Postmark

[Postmark's official MCP server](https://github.com/ActiveCampaign/postmark-mcp) has grown since our original review — it now exposes 24 tools across email sending (single + batch), templates, message search, delivery diagnostics, bounces, suppressions, stats, and webhooks, and its README no longer describes it as experimental. It's still narrower than Resend's 30+ tools (no broadcasts, no contact/segment management), but the gap has closed considerably. Postmark's traditional strength remains deliverability (consistently fast inbox placement). If you need transactional sending plus solid diagnostics, Postmark's MCP server now covers meaningfully more than a bare-bones send tool.

### vs. SendGrid

SendGrid doesn't have an official MCP server — [community implementations](https://github.com/Garoth/sendgrid-mcp) cover contacts, lists, templates, single sends, and stats. SendGrid handles the highest volumes at the lowest per-email cost and has the most mature marketing automation platform. But without official MCP support, you're relying on community maintenance. Resend's official server is actively maintained by the company itself.

## Limitations

- **API key scope is all-or-nothing.** The MCP server uses a single Resend API key. There's no way to restrict which tools an agent can access — if it can send emails, it can also delete domains. For production use, you'd want scoped permissions (e.g., "can send but can't manage domains"). Resend API keys do support granular permissions, but the MCP server doesn't expose per-tool restrictions.
- **Template management has since been added (correction).** This review previously stated the MCP server had no template tools. That's no longer accurate: [the current README](https://github.com/resend/resend-mcp) lists a Templates category (create, list, get, update, publish, duplicate, remove) with `{{{VARIABLE}}}` placeholder support. This was a real gap at the review's original writing but has been closed.
- **Volume limits on free tier.** 3,000 emails/month is fine for testing but tight for any real transactional email workload. A newsletter with 1,000 subscribers uses a third of the monthly quota in one send. The jump to $20/month for 50K emails is reasonable, but it means the MCP server will cost money to use meaningfully.
- **No delivery analytics through MCP.** You can check individual email status, but there are no aggregate analytics tools — no open rates, click rates, bounce rates, or delivery dashboards. Mailgun's MCP server has comprehensive analytics; Resend's doesn't expose this data. You'd need to use webhooks and build your own tracking.
- **Agent safety concerns.** An AI agent with full email access can send emails on your behalf, modify your contact lists, and delete domains. There's no confirmation step, rate limiting, or approval workflow built into the MCP server. A careless prompt could trigger a mass email send or contact deletion. This isn't unique to Resend — it's a systemic issue with email MCP servers — but the broad tool surface makes it more acute.
- **562 stars is still modest relative to the top tier.** Compared to the top-tier MCP servers ([GitHub's official server](https://github.com/github/github-mcp-server) at 32K+, [Playwright MCP](https://github.com/microsoft/playwright-mcp) at 36K+), Resend's MCP adoption is still early. That said, the star count is growing and [active development](https://github.com/resend/resend-mcp/commits/main) (v2.13.0 and counting) shows real momentum.

## Who Should Use This

**Good fit:**
- Developers building AI-assisted workflows that involve email (onboarding sequences, notification systems, support responses)
- Teams that want an agent to manage their email infrastructure — domains, contacts, broadcasts — without touching a dashboard
- Projects already using Resend that want to extend their email automation to AI agents
- Startups where one agent handles email marketing + transactional email through a single integration
- DevOps teams that need agents to set up and verify email domains for new projects

**Not the right fit:**
- High-volume senders who need enterprise-grade analytics (Mailgun has better MCP analytics)
- Teams that need strict per-tool permission controls for agent email access
- Projects that primarily need email template design and management (React Email is separate from the MCP server)
- Organizations that require on-premise email infrastructure (Resend is cloud-only)

## The Bottom Line

Resend's MCP server is the most complete email MCP integration available — and as of May 2026, it's also one of the most actively developed. With 30+ tools spanning email sending/receiving, contacts, broadcasts, domains, segments, webhooks, API key management, and now Automations, it turns a simple email API into a full email operations platform accessible to AI agents. The setup is clean (one npx command, one API key), the free tier covers development and testing, and the official backing means it's maintained by the team that builds the underlying API.

Launch Week 6 (April 2026) made the MCP strategy unambiguous: Resend built a dedicated `/mcp` page and added Automations via MCP, and the npm package has continued shipping new versions since. This isn't a side project — it's a named product.

The breadth is still both its strength and its risk. An agent with access to this server can do everything from sending a single email to mass-deleting contacts and removing verified domains. The lack of per-tool permissions or built-in safety rails means you need to trust your agent's judgment — or carefully scope the prompts that trigger email operations.

For developers already using Resend or evaluating email APIs for AI-assisted workflows, this is the MCP server to start with. It covers more surface area than Mailgun, Postmark, and community SendGrid implementations combined. The developer experience matches Resend's brand: clean, modern, and opinionated toward simplicity.

**Rating: 4 out of 5** — The most comprehensive email MCP server available, backed by a well-regarded developer email API. Covers the full email operations stack (send, receive, contacts, broadcasts, domains, webhooks, automations, and — as of an update since this review's original writing — templates) with a clean setup. Loses a point for the lack of per-tool permissions, absent aggregate delivery analytics, and the inherent safety risks of giving an AI agent broad email platform control.

*Originally reviewed March 2026. Refreshed May 2026. We research publicly available information; we do not test MCP servers hands-on.*

