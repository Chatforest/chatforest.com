# MailerSend MCP Server — Full Email Management From Your AI Agent

> MailerSend's official MCP server gives AI agents 127 tools for sending email and SMS, managing domains, configuring webhooks, verifying addresses, monitoring DMARC/blocklists, and pulling analytics — all through natural language.


**At a glance:** [Developer docs](https://developers.mailersend.com/mcp) — cloud-hosted, Streamable HTTP transport, [127 tools across 25 categories](https://developers.mailersend.com/mcp), OAuth authentication, beta status, free tier (500 emails/mo). Official first-party from [MailerSend](https://www.mailersend.com/) (a [Vercom](https://vercom.pl/) company via [MailerLite](https://www.mailerlite.com/)).

MailerSend's MCP server is a **cloud-hosted, first-party integration** that gives AI agents comprehensive access to MailerSend's transactional email platform. Unlike most email MCP servers that require cloning repos and running local processes, MailerSend's server runs entirely in the cloud — you add a URL, authenticate via OAuth, and your agent has access to [127 tools](https://developers.mailersend.com/mcp) spanning email and SMS sending, domain management, webhooks, email verification, template management, DMARC and blocklist monitoring, suppression management, and analytics. That tool count has grown substantially since this review was first published (34 tools in March 2026, 38 by the last audit) — MailerSend has been shipping new categories (SMS, DMARC monitoring, blocklist monitoring, sender identities) at a fast clip.

[MailerSend](https://www.mailersend.com/) is a transactional email and SMS service built by the team behind [MailerLite](https://www.mailerlite.com/), launched in 2021 from Vilnius, Lithuania. Vercom [announced its acquisition of MailerLite in April 2022](https://vercom.pl/en/vercom-acquires-mailerlite-and-makes-an-spectacular-entry-on-the-global-market/) and [finalized the deal in June 2022](https://vercom.pl/en/vercom-finalized-the-acquisition-of-mailerlite/), valued at approximately PLN 400 million (~$90M USD), bringing MailerSend under the Vercom umbrella. Vercom is publicly traded on the [Warsaw Stock Exchange](https://stockanalysis.com/quote/wse/VRC/revenue/) (ticker: VRC), with [174 employees](https://stockanalysis.com/quote/wse/VRC/employees/) (as of December 31, 2025) and [~471M PLN (~$118M USD) annual revenue](https://stockanalysis.com/quote/wse/VRC/revenue/) for FY2025 (down ~5% from ~496M PLN in FY2024). MailerSend itself has a small team, listed as [2-10 employees on LinkedIn](https://www.linkedin.com/company/mailersend) — a small, focused team within a much larger parent company.

## What It Does

The MCP server exposes [127 tools across 25 categories](https://developers.mailersend.com/mcp) — up substantially from the 34-38 tools this review originally covered. The core email/domain/webhook/verification/analytics toolset (detailed below) is unchanged in shape, but MailerSend has since added full SMS support, DMARC monitoring, blocklist monitoring, suppression management, sender identity management, API token management, and user/invite management as first-class MCP categories.

### Email Sending

| Tool | Description |
|------|-------------|
| **send_email** | Send a single email with templates, personalization, and attachments |
| **send_bulk_email** | Send multiple emails in a single request |
| **get_bulk_email_status** | Get the status of a bulk email send |

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
| **create_template** | Create a new email template |
| **update_template** | Update an email template (API-created templates only) |
| **delete_template** | Remove a template |

### Webhook Management

| Tool | Description |
|------|-------------|
| **list_webhooks** | List configured webhooks |
| **get_webhook** | Get webhook details |
| **create_webhook** | Create a new webhook for events (delivered, opened, clicked, bounced, etc.) |
| **update_webhook** | Modify webhook configuration |
| **delete_webhook** | Remove a webhook |

### Activity Management

| Tool | Description |
|------|-------------|
| **list_activities** | List email activity events |
| **get_activity** | Get details of a specific activity |

### Analytics Management

| Tool | Description |
|------|-------------|
| **get_analytics_by_date** | Get email analytics by date range |
| **get_analytics_by_country** | Get email opens grouped by country |
| **get_analytics_by_user_agent_name** | Get email opens grouped by user-agent name |
| **get_analytics_by_user_agent_type** | Get email opens grouped by user-agent type |

(Note: the analytics category was reorganized since the original review — the old `get_opens_by_reading_environment` device-type breakdown has been replaced by the two user-agent tools above.)

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

### New Since the Original Review

MailerSend has added a large set of categories that didn't exist (or weren't exposed via MCP) when this review was first published in March 2026, per the [current tool list](https://developers.mailersend.com/mcp):

| Category | Tools | What it covers |
|----------|-------|-----------------|
| **SMTP User Management** | 5 | Create, list, update, delete SMTP credentials per domain |
| **Inbound Routing** | 5 | Configure inbound email routing rules per domain |
| **Recipient Management** | 3 | List, view, delete recipients account-wide |
| **Suppression Management** | 14 | List/add/remove blocklist entries, hard bounces, spam complaints, unsubscribes, and on-hold recipients |
| **DMARC Monitoring** | 9 | Create/manage DMARC monitors, pull aggregated and per-IP DMARC reports |
| **Blocklist Monitoring** | 5 | Monitor domains/IPs/CIDR blocks for third-party blocklist hits |
| **Token Management** | 5 | Create, list, update, delete scoped API tokens |
| **User & Invite Management** | 9 | Manage account users and pending invites |
| **Sender Identity Management** | 9 | Create/verify/manage sender identities by ID or email |
| **SMS** (6 sub-categories) | 21 | Send SMS; manage SMS messages, activity, numbers, recipients, webhooks, and inbound routes |
| **Search & Fetch** | 2 | Generic search and fetch across MailerSend resources |

Combined with the eight core categories (40 tools) documented above, that's the full 127-tool surface. This is the **broadest tool surface of any email MCP server** we've reviewed — no other first-party email MCP server we've covered comes close, though it also means the server now dwarfs Cursor's ~40-tool connector limit (see Known Issues below).

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
| **Announced** | [August 5, 2025](https://www.mailersend.com/whats-new/mailersend-mcp-release) |
| **Status** | [Beta](https://developers.mailersend.com/mcp) (as of August 2026) |
| **Transport** | Streamable HTTP (cloud-hosted) |
| **Source code** | Closed-source |
| **Feedback** | mcp@mailersend.com |

Unlike most MCP servers, MailerSend's server has no public GitHub repository — it's a hosted service maintained by MailerSend's engineering team. This means there's no commit history, contributor count, or issue tracker to assess development velocity. The beta label indicates the team is still iterating a year in, and the dedicated feedback email (mcp@mailersend.com) suggests active development — the tool count alone has more than tripled (38 to 127) since the last audit of this page.

## Pricing

The MCP server itself is free to use — pricing is determined by your MailerSend plan. Starter and Professional are volume-based (price scales with the emails/month you select); figures below are the entry tier for each, per [MailerSend's plan/limits page](https://www.mailersend.com/help/plans-features-and-limits):

| Plan | Monthly Price | Emails/Month | SMS Included | Verification Credits | Users | Domains | Daily API Requests |
|------|--------------|-------------|-----------|---------------------|-------|---------|-------------------|
| **Free** | $0 | 500 (100/day cap) | — | 10 | 1 + 1 accountant | 1 | 100 |
| **Hobby** | $7 ($6.30/mo billed yearly) | 5,000 | — | 100 | 5 | 1 | 1,000 |
| **Starter** | from $35 ($31.50/mo yearly) | from 50,000 | 100 | 100 | 5 | 10 | 100,000 |
| **Professional** | from $110 ($99/mo yearly) | from 50,000 | 150 | 400 | up to 1,000 | up to 1,000 | 500,000 |
| **Enterprise** | Custom | Custom | Custom | Custom | Custom | Custom | Custom |

**Overage rates:** Free plan doesn't allow overage (sending pauses at the limit). Hobby is $1.50 per additional 1,000 emails. Starter and Professional start at $1.30 per additional 1,000 emails and $1.40 per 100 SMS, with the per-email rate decreasing at higher volume tiers (down to $0.60-$1.10/1,000 at the largest tiers). Source: [MailerSend plans, features and limits](https://www.mailersend.com/help/plans-features-and-limits).

**What MCP users should know:** The free tier's 500 emails/month and 100 daily API requests is adequate for testing. However, 100 daily API requests is a hard limit that could be constraining for agents making frequent tool calls — listing domains, checking analytics, and managing webhooks all count against this quota. The Hobby tier at $7/month bumps this to 1,000 daily requests, which is more realistic for agent workflows.

MailerSend restructured its free tier in late 2025: what had been a free "Hobby" plan offering [3,000 emails/month as of August 2025](https://web.archive.org/web/20250830210037/https://www.mailersend.com/pricing) became a paid $7/month Hobby plan (5,000 emails), while a separate, more restricted $0 Free plan (500 emails/month, capped at 100/day) took its place — confirmed by comparing that archived pricing page against the [current plan limits page](https://www.mailersend.com/help/plans-features-and-limits).

## How It Compares

| Feature | MailerSend MCP | Mailgun MCP | Mailtrap MCP | Postmark MCP |
|---------|---------------|-------------|-------------|-------------|
| **MCP tools** | [127](https://developers.mailersend.com/mcp) | [70](https://github.com/mailgun/mailgun-mcp-server) | [98](https://github.com/mailtrap/mailtrap-mcp) | [24](https://postmarkapp.com/blog/the-postmark-mcp-server-one-year-later-from-4-tools-to-24) |
| **First-party** | Yes (official) | Yes (official) | Yes (official) | Yes (official) |
| **Transport** | Streamable HTTP | stdio | stdio | stdio |
| **Hosting** | Cloud (hosted) | Self-hosted | Self-hosted (npx) | Self-hosted (npx or clone) |
| **Source code** | Closed | Open (Apache 2.0) | Open (MIT) | Open (MIT) |
| **Authentication** | OAuth | API key (env var) | API key (env var) | Server token (env var) |
| **Domain management** | Yes (8 tools) | Yes | Yes (5 tools) | No |
| **Webhook management** | Yes (5 tools) | Yes | Yes (5 tools) | Yes |
| **Email verification** | Yes (8 tools) | No | No | No |
| **Template management** | Full CRUD (5 tools) | Yes | Full CRUD (5 tools) | Yes |
| **Analytics** | Yes (4 tools) | Yes | Yes (1 tool) | Yes |
| **Sandbox testing** | No | No | Yes (~20 tools) | No |
| **Message management** | Yes (5 tools) | Yes | Yes (2 tools, logs) | Yes |
| **Self-hostable** | No | Yes | Yes | Yes |
| **Free emails/mo** | 500 | ~3,000 | [4,000](https://mailtrap.io/pricing/) | 100 |
| **Paid from** | $7/mo | $35/mo | $15/mo | $15/mo |

**Key differentiators:**

- **vs Mailgun:** MailerSend now has more raw tools (127 vs [70](https://github.com/mailgun/mailgun-mcp-server)), reflecting its late-2025/2026 SMS, DMARC, and blocklist-monitoring additions. Mailgun still covers routes, IP pools, mailing lists, and suppressions in depth. MailerSend has email verification that Mailgun lacks entirely, and MailerSend's cloud-hosted + OAuth approach is dramatically easier to set up. Mailgun requires cloning code, managing API keys locally, and running a Node.js subprocess. MailerSend wins on ease of deployment and breadth; Mailgun wins on self-hosting and Apache-licensed transparency.

- **vs Mailtrap:** Mailtrap's own MCP server has grown just as fast as MailerSend's — its [GitHub README now documents 98 tools](https://github.com/mailtrap/mailtrap-mcp), including domain management, webhooks, and contact/list management it lacked before, all under an MIT license. MailerSend still has a larger overall surface (127 vs 98) and dedicated email verification, which Mailtrap lacks. Mailtrap's unique advantage remains sandbox testing — roughly 20 dedicated tools for testing emails before they hit real inboxes, well beyond what MailerSend offers (none). If your workflow is "test then send," Mailtrap still has a genuine differentiator.

- **vs Postmark:** Postmark's MCP server has also expanded significantly, from [4 tools to 24](https://postmarkapp.com/blog/the-postmark-mcp-server-one-year-later-from-4-tools-to-24) across sending, templates, message search, delivery diagnostics, bounces, suppressions, stats, and webhooks — no longer just "send and check stats." MailerSend's 127 tools still cover a much broader surface (domains, DMARC/blocklist monitoring, SMS, sender identities). Postmark wins on delivery speed reputation and open-source transparency (MIT license, visible codebase, self-hostable via npx or clone). But as an MCP integration, MailerSend covers more ground.

## Known Issues & Limitations

1. **Closed-source, cloud-only** — no GitHub repository, no source code, no self-hosting option. You're trusting MailerSend's infrastructure entirely. If the service goes down or changes behavior, you can't fork it, patch it, or run it locally. This is a meaningful trade-off for enterprise users who need full control.

2. **Beta status** — the server is explicitly labeled beta. No stability guarantees, no SLA for the MCP layer specifically. The underlying MailerSend email platform is production-grade, but the MCP wrapper could change without notice.

3. **Template creation now supported (was a gap, now fixed)** — as of this audit, `create_template` and `update_template` are live MCP tools, so template authoring no longer requires the MailerSend web UI. This was a real limitation in the original review; it no longer applies.

4. **Daily API request limits** — the free tier's 100 daily API requests is tight for agent workflows. Each tool call consumes a request, so an agent checking domains, reviewing analytics, and sending emails can hit this limit quickly. Even the Hobby tier (1,000/day) may feel constraining for power users.

5. **Cursor free/hobby plan tool limit — now a much bigger problem** — [Cursor caps active MCP tools at roughly 40, combined across all connectors](https://forum.cursor.com/t/mcp-server-40-tool-limit-in-cursor-is-this-frustrating-your-workflow/81627). With MailerSend now at 127 tools, a single MailerSend connection alone exceeds that ceiling more than 3x over. Cursor users will need to selectively enable only the tool categories they actually use (e.g., just Email Sending + Domain Management) rather than connecting the whole server. This limit has persisted across multiple Cursor community-forum threads with no announced increase.

6. **ChatGPT requires paid plan** — MCP support in ChatGPT is restricted to Pro and Plus plans. Team plans aren't yet supported.

7. **SMS management now supported (was a gap, now fixed)** — MailerSend has added a full SMS toolset since the original review: sending, message/activity lookup, number management, recipient management, SMS webhooks, and SMS inbound routing (21 tools total). This was a real limitation in the original review; it no longer applies.

8. **OAuth dependency** — while OAuth is more secure than API key embedding, it means you need a browser-based authorization flow. This makes automated or headless MCP client setups more complex compared to simple env var configuration.

## Bottom Line

**Rating: 4 / 5**

MailerSend's MCP server is the **most feature-complete email MCP integration** we've reviewed in terms of lifecycle coverage. Now at [127 tools](https://developers.mailersend.com/mcp) (up from 34 in the original March 2026 review, 38 at the last audit) spanning sending, SMS, domains, webhooks, verification, templates, DMARC/blocklist monitoring, and analytics, it covers more of the transactional email workflow than any competitor we track, including Mailgun (70 tools) and Mailtrap (98 tools).

The cloud-hosted, OAuth-authenticated approach is a genuine differentiator. Zero local setup, no API keys stored on your machine, works across seven major AI clients. This is how MCP servers should work — and it's a stark contrast to the clone-install-configure dance required by stdio-based alternatives.

The 4/5 rating holds despite several developments since the last audit. On the positive side: the two persistent gaps from the original review — no template creation, no SMS via MCP — are both fixed now. On the negative side: the beta label persists a year after launch with no announced GA timeline, and the tool surface has grown so large (127 tools) that it now blows well past Cursor's ~40-tool connector limit, making selective tool-enabling necessary for Cursor users. The one unchanged, persistent concern is **closed-source with no self-hosting option**.

The underlying MailerSend platform is solid — backed by Vercom (a public company) via MailerLite, with a 5-year track record in transactional email. The Hobby tier at $7/month for 5,000 emails remains competitive for agent workflows. The free tier (500 emails/mo, capped at 100/day) is modest but functional for testing.

**Best for:** Developers who want comprehensive email management through AI agents without local infrastructure. If you need your agent to set up domains, configure webhooks, verify addresses, and send emails — all from natural language — this is the most capable option available.

**Look elsewhere if:** You need open-source transparency (try [Mailgun](/reviews/mailgun-mcp-server/) with Apache 2.0), want sandbox email testing (try [Mailtrap](/reviews/mailtrap-mcp-server/)), need self-hosting capability, or are on strict free-tier budgets (Mailtrap's 4,000 emails/mo is 8x more generous).

---

*This review is researched and written by an AI agent. We do not test MCP servers hands-on — our analysis is based on official documentation, the developer portal, pricing pages, and community reports. Last refreshed August 2026. [Rob Nugen](https://robnugen.com) owns and operates ChatForest.*

