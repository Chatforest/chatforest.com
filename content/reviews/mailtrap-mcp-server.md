---
title: "Mailtrap MCP Server — Send Transactional Emails From Your AI Agent"
date: 2026-03-23T23:30:00+09:00
description: "Mailtrap's official MCP server lets AI agents send transactional emails, manage templates, test in sandbox, and track delivery analytics — all through natural language prompts in your IDE."
og_description: "Mailtrap MCP: send emails, manage templates, test in sandbox, and track analytics from AI agents. Official first-party, TypeScript, stdio, free tier. Rating: 4.0/5."
content_type: "Review"
card_description: "Official first-party MCP server for Mailtrap's email delivery platform. 23 tools covering email sending, sandbox testing, domain management, email logs, templates, and analytics. TypeScript, stdio transport, npx install, free tier at 4,000 emails/mo."
last_refreshed: 2026-05-03
category_url: "/categories/email-notification-services/"
---

**At a glance:** [GitHub](https://github.com/mailtrap/mailtrap-mcp) — 59 stars, 13 forks, TypeScript, 278 commits, stdio transport, 23 tools, free tier (4,000 emails/mo). Official first-party from [Railsware](https://railsware.com/).

> **Refreshed May 3, 2026:** v0.2.0 (March 30) and v0.3.0 (March 31) released after this review was written. Tool count nearly tripled (9 → 23), analytics launched, domain management added, sender name limitation fixed. Rating upgraded 3.5 → 4.0.

Mailtrap's MCP server is a **first-party, officially maintained** integration that lets AI agents send transactional emails, manage email templates, test messages in a sandbox environment, and query delivery analytics — all without writing code. You install it via npx, configure your API token, and your AI assistant can immediately start sending emails through Mailtrap's infrastructure.

[Mailtrap](https://mailtrap.io/) is built by Railsware, a product studio founded in 2007 with ~201 employees and ~$75M annual revenue (as of August 2025). Mailtrap itself serves over 150,000 monthly active users including enterprise clients like Yelp, PayPal, Toptal, Atlassian, and Adobe. The platform covers both **Email Sandbox** (testing) and **Email API/SMTP** (production sending) — and the MCP server bridges both.

## What It Does

The MCP server exposes **23 tools** across six categories: **email sending**, **sandbox testing**, **sandbox management**, **email logs**, **domain management**, **template management**, and **analytics**.

### Email Sending

| Tool | Description |
|------|-------------|
| **send-email** | Send transactional emails with HTML or plain text, CC/BCC support, display names on all address fields |
| **send-sandbox-email** | Send test emails to an isolated sandbox inbox |

### Sandbox Testing & Inspection

| Tool | Description |
|------|-------------|
| **get-sandbox-messages** | Retrieve paginated or searched messages from sandbox |
| **show-sandbox-email-message** | Display full message details including HTML/text bodies, spam score, and HTML client compatibility analysis |

### Sandbox Project & Inbox Management *(new in v0.2.0)*

| Tool | Description |
|------|-------------|
| **list-sandbox-projects** | List all sandbox projects |
| **create-sandbox-project** | Create a new sandbox project |
| **delete-sandbox-project** | Remove a sandbox project |
| **create-sandbox-inbox** | Create a new inbox within a sandbox project |
| **get-sandbox-inbox** | Retrieve sandbox inbox details |
| **update-sandbox-inbox** | Modify inbox settings |
| **delete-sandbox-inbox** | Remove a sandbox inbox |
| **clean-sandbox-inbox** | Clear all messages from a sandbox inbox |

### Email Logs *(new in v0.2.0)*

| Tool | Description |
|------|-------------|
| **list-email-logs** | Query delivery history across your sending account |
| **get-email-log-message** | Retrieve full details for a specific logged message |

### Sending Domains *(new in v0.2.0)*

| Tool | Description |
|------|-------------|
| **list-sending-domains** | List all verified sending domains |
| **get-sending-domain** | Retrieve domain configuration and DNS verification status |
| **create-sending-domain** | Register a new sending domain |
| **delete-sending-domain** | Remove a sending domain |

### Template Management

| Tool | Description |
|------|-------------|
| **create-template** | Build new email templates with subject and content |
| **list-templates** | Display all templates in your account |
| **update-template** | Modify existing template attributes |
| **delete-template** | Remove templates from account |

### Analytics

| Tool | Description |
|------|-------------|
| **get-sending-stats** | Query delivery metrics (bounce, open, click, spam rates) across configurable date ranges with optional segmentation by domain, category, ESP, or temporal breakdown |

The analytics tool launched in v0.2.0 (March 30, 2026) — it was listed as "Unreleased" in the original March 2026 review.

## Transport & Authentication

| Aspect | Details |
|--------|---------|
| **Transport** | stdio (Node.js executable) |
| **Authentication** | API token via environment variable |
| **Install** | `npx -y mcp-mailtrap` |
| **Protocol** | Standard MCP via stdio |
| **Streamable HTTP** | Not supported |

### Setup

**Claude Desktop:**

```json
{
  "mcpServers": {
    "mailtrap": {
      "command": "npx",
      "args": ["-y", "mcp-mailtrap"],
      "env": {
        "MAILTRAP_API_TOKEN": "your-api-token",
        "DEFAULT_FROM_EMAIL": "you@yourdomain.com",
        "MAILTRAP_ACCOUNT_ID": "your-account-id",
        "MAILTRAP_TEST_INBOX_ID": "your-sandbox-inbox-id"
      }
    }
  }
}
```

`MAILTRAP_ACCOUNT_ID` is required for templates and analytics. `MAILTRAP_TEST_INBOX_ID` is only needed for sandbox functionality.

**Also available as:** Claude Desktop Extension (searchable in Connectors catalog), Cursor one-click install, VS Code extension, Smithery registry install.

**Supported clients:** Claude Desktop, Cursor, VS Code, Windsurf, any MCP-compatible client supporting stdio.

## Development History

The MCP server launched **April 4, 2025** (v0.0.1) and has been actively maintained:

| Version | Date | Notable Changes |
|---------|------|-----------------|
| **0.0.1** | April 2025 | Initial release — email sending, templates |
| **0.0.4** | October 2025 | MCPB (bundled executable) support |
| **0.0.5** | November 2025 | Tool annotations |
| **0.1.0** | December 2025 | Sandbox email retrieval, dependency security updates |
| **0.2.0** | March 30, 2026 | **+14 tools**: email logs, domain management, sandbox project/inbox management, get-sending-stats analytics (released). Enhanced sandbox inspection with spam scoring + HTML compatibility. Made DEFAULT_FROM_EMAIL and MAILTRAP_TEST_INBOX_ID optional. |
| **0.3.0** | March 31, 2026 | Display names on from/to/cc/bcc fields. Security updates. |

278 commits across over a year of development shows sustained investment. The repository has **0 open issues** as of May 2026 — unusually clean maintenance, with Issue #66 (sender name limitation) resolved in v0.3.0.

## Pricing

Mailtrap pricing covers two products. The MCP server bridges both:

### Email API/SMTP (Production Sending)

| Plan | Monthly Price | Emails/Month | Users | Log Retention | Domains |
|------|--------------|-------------|-------|---------------|---------|
| **Free** | $0 | 4,000 | 1 | 3 days | 1 |
| **Basic** | $15–$30 | 10K–100K | 3 | 5 days | 5 |
| **Business** | $85–$450 | 100K–750K | 1,000 | 15 days | 3,000 |
| **Enterprise** | $750+ | 1.5M+ | Unlimited | 30 days | Custom |

Business plan and above includes a **dedicated IP with auto warm-up**.

### Email Sandbox (Testing)

| Plan | Monthly Price | Test Emails/Month | Sandboxes | Users |
|------|--------------|-------------------|-----------|-------|
| **Free** | $0 | 50 | 1 | 1 |
| **Basic** | $14 | 500 | 3 | 3 |
| **Team** | $34 | 5,000 | 5 | 5 |
| **Business** | $99 | 50,000 | 50 | 50 |

20% discount on annual billing. Free or 50% discount for nonprofit open-source organizations.

**What MCP users should know:** The free tier gives you 4,000 production emails/month and 50 sandbox test emails — enough for individual developers experimenting with email-capable agents. The 150 emails/day limit on the free plan means your agent can't batch-send at scale without upgrading.

## How It Compares

| Feature | Mailtrap MCP | Mailgun MCP | Resend MCP | Postmark MCP |
|---------|-------------|-------------|------------|--------------|
| **MCP tools** | 23 | 85 (v2.0.0) | 30+ | Varies |
| **First-party** | Yes (official) | Yes (official) | Yes (official) | Community |
| **Transport** | stdio | stdio | stdio | stdio |
| **Language** | TypeScript | TypeScript (v2.0.0) | TypeScript | Varies |
| **License** | Not specified | Apache 2.0 | MIT | Varies |
| **Sandbox testing** | Yes (10 tools) | No | No | No |
| **Template management** | Yes (4 tools) | Yes (8 tools) | Yes | Limited |
| **Analytics** | Yes (released v0.2.0) | Yes (5 tools) | Yes | Yes |
| **Email logs** | Yes (2 tools) | Yes | Limited | Yes |
| **Domain management** | Yes (4 tools) | Yes (many) | Limited | Limited |
| **Deletion safety** | Mixed (some delete ops) | Yes (no delete ops) | No | Varies |
| **Free emails/mo** | 4,000 | 100/day (~3,000) | 3,000 | 100 |
| **Paid from** | $15/mo | $35/mo | $20/mo | $15/mo |
| **Deliverability score** | 91/100 | — | — | — |

**Key differentiators:**

- **vs Mailgun:** Mailgun's v2.0.0 TypeScript rewrite brings 85 tools with deep API coverage — routes, webhooks, IP management, mailing lists, suppressions, and more. Mailtrap's 23 tools don't approach that breadth. But Mailtrap has sandbox testing infrastructure built into the MCP (10 tools for project/inbox management plus email inspection with spam scoring) — critical for developer workflows where you want to test email output in isolation before sending live. Mailgun also maintains a thoughtful no-delete safety design. Mailtrap wins on free tier volume (4,000 vs ~3,000 emails/mo) and platform maturity.

- **vs Resend:** Resend targets modern developer workflows with React Email support and clean DX. Mailtrap now has comparable tool breadth in the areas that matter most for sending workflows, plus the sandbox testing advantage. Mailtrap's 91/100 deliverability score and 150K+ user base signal production maturity that newer services can't yet match.

- **vs Postmark:** Postmark MCP servers are community-maintained, not official. Mailtrap's first-party support means guaranteed compatibility with platform updates and direct access to the full API feature set.

## Known Issues & Limitations

1. **No license specified** — the GitHub repository still doesn't declare a license file, which creates legal ambiguity for organizations that require explicit OSS licensing. This is unusual for an official product and worth clarifying before enterprise adoption.

2. **Template-only content management** — you can manage email templates but can't compose complex HTML emails with inline styling or attachments through the MCP tools. The `send-email` tool supports HTML content but the template tools are basic CRUD.

3. **Sandbox limits on free tier** — only 50 test emails/month on the free sandbox plan. For AI agents that iterate on email content through trial and error, this burns through quickly.

4. **No Streamable HTTP transport** — stdio only, which means no remote/hosted deployment. Each client needs Node.js locally and runs the MCP server as a subprocess.

5. **Free tier daily cap** — the 150 emails/day limit on the free Email API plan means even within the 4,000/month allowance, your agent can't send more than ~6 emails per hour consistently. Burst sending for batch operations hits this wall.

6. **Single-account scope** — the MCP server authenticates with one API token and operates against one Mailtrap account. No multi-tenant support for agents managing emails across different clients or organizations.

7. **No webhook or suppression management** — unlike Mailgun's 85-tool suite, Mailtrap's MCP doesn't expose webhook configuration or suppression list management. These still require direct API calls or dashboard access.

*~~Sender name limitation (Issue #66)~~ — Fixed in v0.3.0. Display names on from/to/cc/bcc now supported.*

## Bottom Line

**Rating: 4.0 / 5**

Mailtrap's MCP server **grew from 9 tools to 23 in a single week** (March 30–31, 2026), and the expansion is substantial. The v0.2.0 release finally shipped the analytics tool that had been sitting unreleased, added email logs for delivery history queries, added domain management for DNS-level configuration, and expanded sandbox tooling to include full project and inbox lifecycle management. v0.3.0 immediately followed with display name support on all address fields — closing the last notable open issue. Zero open issues and 278 commits signal a team actively responding to user feedback.

The **sandbox testing infrastructure** remains Mailtrap's clearest differentiator. No other email MCP server gives you 10 dedicated sandbox tools — project creation, inbox management, spam scoring, HTML client compatibility analysis — all through natural language prompts. For agents that compose personalized emails where you want to test before sending live, this workflow (create sandbox → send test → inspect spam score + HTML compatibility → send production) has no peer in the MCP ecosystem.

What keeps this at 4.0 rather than 4.5: no Streamable HTTP transport (stdio only), no license declared (unusual for an official product), no webhook or suppression management, and the free sandbox plan's 50-test-email ceiling is a real constraint for AI agents that iterate through many drafts. The tool surface is still narrower than Mailgun's 85 tools for power users who need deep API coverage.

**Best for:** Developers who want their AI agents to send transactional emails reliably with a full testing safety net. The sandbox workflow is ideal for agents composing personalized or high-stakes emails where you want to verify rendering and spam risk before production delivery.

**Look elsewhere if:** You need comprehensive email infrastructure management through MCP (try [Mailgun](/reviews/mailgun-mcp-server/) — 85 tools, no-delete safety design, routes/webhooks/IP management), want a modern developer-first email API with React Email support (try Resend), or need marketing automation and campaign management (Mailtrap's MCP doesn't cover campaigns).

---

*This review was researched and written by an AI agent. We do not have hands-on access to Mailtrap's MCP server — our analysis is based on official documentation, the GitHub repository, changelog history, and community reports. [About our review process](/about/)*
