# Resend MCP Server — The Developer-First Email API With Full AI Agent Access

> Resend's official MCP server gives AI agents full email platform control — send, receive, manage contacts, run broadcast campaigns, and configure domains.


**At a glance:** 475+ stars, MIT license, TypeScript, 30+ MCP tools across 10 categories, stdio + HTTP transport, free tier (3,000 emails/month).

[Resend](https://github.com/resend/resend-mcp) is the email API built for developers — clean REST endpoints, React Email integration for writing templates as components, and strong deliverability out of the box. Their official MCP server turns the entire Resend platform into tools that AI agents can use directly: send emails with attachments, manage contact lists, run broadcast campaigns, configure domains, and set up webhooks — all through natural language.

Unlike most email MCP servers that only handle sending, Resend's MCP server exposes the full platform. This isn't just "let the AI send an email" — it's "let the AI manage your entire email infrastructure."

The key question: does an AI agent actually need this much email control, and is it safe to give it?

## What It Does

Resend's MCP server exposes 30+ tools organized across 10 categories:

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

Resend's pricing applies to the underlying API (the MCP server itself is free and open source):

| Plan | Price | Emails/Month | Domains | Support |
|------|-------|-------------|---------|---------|
| **Free** | $0 | 3,000 | 1 | Community |
| **Pro** | $20/mo | 50,000 | 10 | Email |
| **Scale** | $90/mo | 100,000 | Unlimited | Priority |
| **Enterprise** | Custom | Custom | Custom | Dedicated |

The free tier covers 3,000 emails per month with no credit card required — enough for development, testing, and low-volume transactional email. Pro at $20/month for 50K emails is competitive with SendGrid and Postmark at the same price point.

## Compared to Other Email MCP Servers

| Feature | Resend | Mailgun | Postmark | SendGrid |
|---------|--------|---------|----------|----------|
| **GitHub stars** | 475 | 43 | ~30 | ~20 (community) |
| **Official** | Yes (Resend) | Yes (Mailgun) | Yes (ActiveCampaign) | Community |
| **MCP tools** | 30+ | 15+ | ~3 | ~8 |
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

[Postmark's MCP server](https://github.com/ActiveCampaign/postmark-mcp) is explicitly experimental and minimal — sending emails, listing templates, and checking delivery stats. Postmark's strength is deliverability (consistently the fastest inbox placement), but their MCP server is a fraction of Resend's surface area. If you just need to send transactional emails and nothing else, Postmark is fine. For anything more, Resend covers far more ground.

### vs. SendGrid

SendGrid doesn't have an official MCP server — the community implementations cover contacts, lists, templates, single sends, and stats. SendGrid handles the highest volumes at the lowest per-email cost and has the most mature marketing automation platform. But without official MCP support, you're relying on community maintenance. Resend's official server is actively maintained by the company itself.

## Limitations

- **API key scope is all-or-nothing.** The MCP server uses a single Resend API key. There's no way to restrict which tools an agent can access — if it can send emails, it can also delete domains. For production use, you'd want scoped permissions (e.g., "can send but can't manage domains"). Resend API keys do support granular permissions, but the MCP server doesn't expose per-tool restrictions.
- **No template management.** Despite Resend's React Email integration, the MCP server doesn't include tools for managing email templates. You can send HTML, but you can't list, create, or preview templates through MCP. This is a gap — an agent that can compose broadcasts but can't manage the templates those broadcasts use.
- **Volume limits on free tier.** 3,000 emails/month is fine for testing but tight for any real transactional email workload. A newsletter with 1,000 subscribers uses a third of the monthly quota in one send. The jump to $20/month for 50K emails is reasonable, but it means the MCP server will cost money to use meaningfully.
- **No delivery analytics through MCP.** You can check individual email status, but there are no aggregate analytics tools — no open rates, click rates, bounce rates, or delivery dashboards. Mailgun's MCP server has comprehensive analytics; Resend's doesn't expose this data. You'd need to use webhooks and build your own tracking.
- **Agent safety concerns.** An AI agent with full email access can send emails on your behalf, modify your contact lists, and delete domains. There's no confirmation step, rate limiting, or approval workflow built into the MCP server. A careless prompt could trigger a mass email send or contact deletion. This isn't unique to Resend — it's a systemic issue with email MCP servers — but the broad tool surface makes it more acute.
- **475 stars is modest.** Compared to the top-tier MCP servers (GitHub at 20K+, Playwright at 8K+), Resend's MCP adoption is early. The server is official and actively maintained, but the community ecosystem (integrations, tutorials, troubleshooting) is thin.

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

Resend's MCP server is the most complete email MCP integration available. With 30+ tools spanning email sending/receiving, contacts, broadcasts, domains, segments, webhooks, and API key management, it turns a simple email API into a full email operations platform accessible to AI agents. The setup is clean (one npx command, one API key), the free tier covers development and testing, and the official backing means it's maintained by the team that builds the underlying API.

The breadth is both its strength and its risk. An agent with access to this server can do everything from sending a single email to mass-deleting contacts and removing verified domains. The lack of per-tool permissions or built-in safety rails means you need to trust your agent's judgment — or carefully scope the prompts that trigger email operations.

For developers already using Resend or evaluating email APIs for AI-assisted workflows, this is the MCP server to start with. It covers more surface area than Mailgun, Postmark, and community SendGrid implementations combined. The developer experience matches Resend's brand: clean, modern, and opinionated toward simplicity.

**Rating: 4 out of 5** — The most comprehensive email MCP server available, backed by a well-regarded developer email API. Covers the full email operations stack (send, receive, contacts, broadcasts, domains, webhooks) with a clean setup. Loses a point for the lack of per-tool permissions, missing template management, absent delivery analytics, and the inherent safety risks of giving an AI agent broad email platform control.

*This review reflects research conducted in March 2026. We research publicly available information; we do not test MCP servers hands-on.*

