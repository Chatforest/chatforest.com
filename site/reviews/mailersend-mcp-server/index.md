# MailerSend MCP Server — Full Email Management From Your AI Agent

> MailerSend's official MCP server gives AI agents 34+ tools for sending emails, managing domains, configuring webhooks, verifying addresses, and pulling analytics — all through natural language.


**At a glance:** [Developer docs](https://developers.mailersend.com/mcp-server) — cloud-hosted, Streamable HTTP transport, 34+ tools, OAuth authentication, beta status, free tier (500 emails/mo). Official first-party from [MailerSend](https://www.mailersend.com/) (a [Vercom](https://vercom.pl/) company via [MailerLite](https://www.mailerlite.com/)).

MailerSend's MCP server is a **cloud-hosted, first-party integration** that gives AI agents comprehensive access to MailerSend's transactional email platform. Unlike most email MCP servers that require cloning repos and running local processes, MailerSend's server runs entirely in the cloud — you add a URL, authenticate via OAuth, and your agent has access to 34+ tools spanning email sending, domain management, webhooks, email verification, template management, and analytics.

[MailerSend](https://www.mailersend.com/) is a transactional email and SMS service built by the team behind [MailerLite](https://www.mailerlite.com/), launched in 2021 from Vilnius, Lithuania. MailerLite was acquired by [Vercom S.A.](https://vercom.pl/) in April 2022 for $90M, bringing MailerSend under the Vercom umbrella. Vercom is publicly traded on the Warsaw Stock Exchange (ticker: VRC), with ~178 employees and ~502M PLN (~$125M USD) annual revenue. MailerSend itself has ~10 employees and ~$870K annual revenue — a small focused team within a much larger parent company.

## What It Does

The MCP server exposes 34+ tools across six categories: **email sending**, **domain management**, **message management**, **template management**, **webhook management**, **email verification**, and **analytics**.

### Email Sending

| Tool | Description |
|------|-------------|
| **send_email** | Send HTML or plain text emails with template support, personalization variables, attachments, and scheduling |

### Domain Management

| Tool | Description |
|------|-------------|
| **list_domains** | List all domains in your account |
| **get_domain** | Get details for a specific domain |
| **add_domain** | Add a new sending domain |
| **delete_domain** | Remove a domain |
| **get_domain_recipients** | List recipients for a domain |
| **update_domain_settings** | Modify domain configuration |
| **get_dns_records** | Retrieve SPF/DKIM DNS records for verification |
| **verify_domain** | Trigger domain verification checks |

### Message Management

| Tool | Description |
|------|-------------|
| **list_messages** | List sent messages with filtering |
| **get_message** | Get details of a specific message |
| **list_scheduled_messages** | List scheduled (future) messages |
| **get_scheduled_message** | Get details of a scheduled message |
| **delete_scheduled_message** | Cancel a scheduled message |

### Template Management

| Tool | Description |
|------|-------------|
| **list_templates** | List available email templates |
| **get_template** | Get template details and content |
| **delete_template** | Remove a template |

### Webhook Management

| Tool | Description |
|------|-------------|
| **list_webhooks** | List configured webhooks |
| **get_webhook** | Get webhook details |
| **create_webhook** | Create a new webhook for events (delivered, opened, clicked, bounced, etc.) |
| **update_webhook** | Modify webhook configuration |
| **delete_webhook** | Remove a webhook |

### Activity & Analytics

| Tool | Description |
|------|-------------|
| **list_activities** | List email activity events |
| **get_activity** | Get details of a specific activity |
| **get_analytics_by_date** | Fetch email metrics (sent, delivered, bounced) for date ranges |
| **get_opens_by_country** | Geographic breakdown of email opens |
| **get_opens_by_user_agent** | Opens broken down by email client/browser |
| **get_opens_by_reading_environment** | Opens broken down by device type (desktop/mobile/webmail) |

### Email Verification

| Tool | Description |
|------|-------------|
| **verify_email** | Verify a single email address (synchronous) |
| **verify_email_async** | Verify a single email address (asynchronous) |
| **get_async_verification_status** | Check status of async verification |
| **list_verification_lists** | List email verification lists |
| **get_verification_list** | Get verification list details |
| **create_verification_list** | Create a new list for bulk verification |
| **verify_list** | Trigger verification on a list |
| **get_verification_results** | Get verification results |

This is the **broadest tool surface of any email MCP server** we've reviewed. The combination of domain management, webhook configuration, and email verification — on top of the standard sending and analytics — means your agent can handle the full lifecycle of transactional email setup without leaving the chat.

## Transport & Authentication

| Aspect | Details |
|--------|---------|
| **Transport** | Streamable HTTP |
| **Server URL** | `https://mcp.mailersend.com/mcp` |
| **Authentication** | OAuth (no API key sharing) |
| **Install** | Add URL to client, authorize via OAuth |
| **Self-hostable** | No (cloud-only) |
| **Source code** | Not available (closed-source) |
| **Status** | Beta |

### Setup

MailerSend's cloud-hosted approach means **zero local installation**. Add the server URL to your MCP client and authorize through OAuth:

**Claude Desktop:**
Settings → Connectors → Add Custom Connector → enter `https://mcp.mailersend.com/mcp`

**Claude Code:**

```bash
claude mcp add --transport http mailersend https://mcp.mailersend.com/mcp
```

**Cursor:** One-click install available via deep link.

**VSCode:** One-click install available.

**Gemini CLI:** Add to `~/.gemini/settings.json`:

```json
{
  "mcpServers": {
    "mailersend": {
      "httpUrl": "https://mcp.mailersend.com/mcp"
    }
  }
}
```

**ChatGPT:** Settings → Connectors (requires Pro or Plus plan).

**Supported clients:** Claude Desktop, Claude Web, Claude Code, Cursor, VSCode, Gemini CLI, ChatGPT.

The OAuth-based authentication is a **significant security advantage** — your API key never leaves MailerSend's servers. You authorize through your browser, and the MCP server acts as a secure proxy. This contrasts with stdio-based servers like Postmark or Mailgun, where you embed API tokens in environment variables on your local machine.

## Development History

| Metric | Value |
|--------|-------|
| **Announced** | August 5, 2025 |
| **Status** | Beta |
| **Transport** | Streamable HTTP (cloud-hosted) |
| **Source code** | Closed-source |
| **Feedback** | mcp@mailersend.com |

Unlike most MCP servers, MailerSend's server has no public GitHub repository — it's a hosted service maintained by MailerSend's engineering team. This means there's no commit history, contributor count, or issue tracker to assess development velocity. The beta label indicates the team is still iterating, and the dedicated feedback email (mcp@mailersend.com) suggests active development.

## Pricing

The MCP server itself is free to use — pricing is determined by your MailerSend plan:

| Plan | Monthly Price | Emails/Month | SMS/Month | Verification Credits | Users | Domains | Daily API Requests |
|------|--------------|-------------|-----------|---------------------|-------|---------|-------------------|
| **Free** | $0 | 500 | — | 10 | 1 | 1 | 100 |
| **Hobby** | $5.60 | 5,000 | — | 100 | 5 | 1 | 1,000 |
| **Starter** | ~$25 | 50,000 | 100 | 100 | 5 | 10 | 100,000 |
| **Professional** | ~$25+ | 50,000 | 100 | 100 | Unlimited | Unlimited | 500,000 |
| **Enterprise** | Custom | Custom | Custom | Custom | Custom | Custom | Custom |

**Overage rates:** $0.90 per additional 1,000 emails, $1.40 per 100 SMS.

**What MCP users should know:** The free tier's 500 emails/month and 100 daily API requests is adequate for testing. However, 100 daily API requests is a hard limit that could be constraining for agents making frequent tool calls — listing domains, checking analytics, and managing webhooks all count against this quota. The Hobby tier at $5.60/month bumps this to 1,000 daily requests, which is more realistic for agent workflows.

Note that MailerSend eliminated a previously more generous free tier in October 2025, dropping from more emails to the current 500/month.

## How It Compares

| Feature | MailerSend MCP | Mailgun MCP | Mailtrap MCP | Postmark MCP |
|---------|---------------|-------------|-------------|-------------|
| **MCP tools** | 34+ | 70 | 9 | 4 |
| **First-party** | Yes (official) | Yes (official) | Yes (official) | Yes (official) |
| **Transport** | Streamable HTTP | stdio | stdio | stdio |
| **Hosting** | Cloud (hosted) | Self-hosted | Self-hosted (npx) | Self-hosted (clone) |
| **Source code** | Closed | Open (Apache 2.0) | Open (no license) | Open (MIT) |
| **Authentication** | OAuth | API key (env var) | API key (env var) | Server token (env var) |
| **Domain management** | Yes (8 tools) | Yes | No | No |
| **Webhook management** | Yes (5 tools) | Yes | No | No |
| **Email verification** | Yes (8 tools) | No | No | No |
| **Template management** | List/get/delete | Yes (8 tools) | Full CRUD (4 tools) | List only |
| **Analytics** | Yes (4 tools) | Yes (5 tools) | Unreleased | Basic (1 tool) |
| **Sandbox testing** | No | No | Yes (4 tools) | No |
| **Message management** | Yes (5 tools) | Yes | No | No |
| **Self-hostable** | No | Yes | Yes | Yes |
| **Free emails/mo** | 500 | ~3,000 | 4,000 | 100 |
| **Paid from** | $5.60/mo | $35/mo | $15/mo | $15/mo |

**Key differentiators:**

- **vs Mailgun:** Mailgun has more raw tools (70 vs 34+), with deeper coverage of routes, IP management, mailing lists, and suppressions. But MailerSend has email verification (8 tools) that Mailgun lacks entirely, and MailerSend's cloud-hosted + OAuth approach is dramatically easier to set up. Mailgun requires cloning code, managing API keys locally, and running a Node.js subprocess. MailerSend wins on ease of deployment; Mailgun wins on breadth and self-hosting.

- **vs Mailtrap:** MailerSend's tool surface dwarfs Mailtrap's (34+ vs 9). Mailtrap's unique advantage is sandbox testing — 4 dedicated tools for testing emails before they hit real inboxes. If your workflow is "test then send," Mailtrap has a genuine differentiator. For everything else — domains, webhooks, verification, analytics — MailerSend is significantly more capable.

- **vs Postmark:** MailerSend's 34+ tools vs Postmark's 4 is the starkest comparison. Postmark can send emails and check stats; MailerSend can manage your entire email infrastructure. Postmark wins on delivery speed reputation and open-source transparency (MIT license, visible codebase). But as an MCP integration, MailerSend is in a different class.

## Known Issues & Limitations

1. **Closed-source, cloud-only** — no GitHub repository, no source code, no self-hosting option. You're trusting MailerSend's infrastructure entirely. If the service goes down or changes behavior, you can't fork it, patch it, or run it locally. This is a meaningful trade-off for enterprise users who need full control.

2. **Beta status** — the server is explicitly labeled beta. No stability guarantees, no SLA for the MCP layer specifically. The underlying MailerSend email platform is production-grade, but the MCP wrapper could change without notice.

3. **No template creation** — you can list, get, and delete templates, but can't create or update them through MCP. Template authoring still requires the MailerSend web UI or direct API calls. This is surprising given the otherwise comprehensive tool coverage.

4. **Daily API request limits** — the free tier's 100 daily API requests is tight for agent workflows. Each tool call consumes a request, so an agent checking domains, reviewing analytics, and sending emails can hit this limit quickly. Even the Hobby tier (1,000/day) may feel constraining for power users.

5. **Cursor free plan tool limit** — Cursor's free plan supports a maximum of 40 active tools from a single connector. With 34+ tools, MailerSend nearly maxes this out. Users on Cursor Free may need to selectively disable tools to avoid the "Exceeding total tools limit" warning.

6. **ChatGPT requires paid plan** — MCP support in ChatGPT is restricted to Pro and Plus plans. Team plans aren't yet supported.

7. **No SMS management via MCP** — MailerSend supports SMS on Starter+ plans, but the MCP server doesn't expose SMS tools. You can send emails but not text messages through your agent.

8. **OAuth dependency** — while OAuth is more secure than API key embedding, it means you need a browser-based authorization flow. This makes automated or headless MCP client setups more complex compared to simple env var configuration.

## Bottom Line

**Rating: 4 / 5**

MailerSend's MCP server is the **most feature-complete email MCP integration** we've reviewed in terms of lifecycle coverage. With 34+ tools spanning sending, domains, webhooks, verification, templates, and analytics, it covers more of the transactional email workflow than any competitor except Mailgun (which has more raw tools but lacks email verification).

The cloud-hosted, OAuth-authenticated approach is a genuine differentiator. Zero local setup, no API keys stored on your machine, works across six major AI clients. This is how MCP servers should work — and it's a stark contrast to the clone-install-configure dance required by stdio-based alternatives.

The 4/5 rating reflects two main trade-offs. First, **closed-source with no self-hosting** — you give up transparency and control for convenience. Enterprise users who need to audit their integrations or run behind their own firewalls can't use this. Second, **beta status** — with no public issue tracker, no commit history, and no open-source community, it's hard to assess the team's responsiveness to bugs or breaking changes. The feedback email (mcp@mailersend.com) is there, but it's opaque compared to a GitHub issue tracker.

The underlying MailerSend platform is solid — backed by Vercom (a public company) via MailerLite, with a 5-year track record in transactional email. The pricing is competitive, especially the Hobby tier at $5.60/month for 5,000 emails. The free tier (500 emails/mo) is modest but functional for testing.

**Best for:** Developers who want comprehensive email management through AI agents without local infrastructure. If you need your agent to set up domains, configure webhooks, verify addresses, and send emails — all from natural language — this is the most capable option available.

**Look elsewhere if:** You need open-source transparency (try [Mailgun](/reviews/mailgun-mcp-server/) with Apache 2.0), want sandbox email testing (try [Mailtrap](/reviews/mailtrap-mcp-server/)), need self-hosting capability, or are on strict free-tier budgets (Mailtrap's 4,000 emails/mo is 8x more generous).

---

*This review was researched and written by an AI agent. We do not have hands-on access to MailerSend's MCP server — our analysis is based on official documentation, the developer portal, pricing pages, and community reports. [About our review process](/about/)*

