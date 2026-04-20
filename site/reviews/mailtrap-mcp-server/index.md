# Mailtrap MCP Server — Send Transactional Emails From Your AI Agent

> Mailtrap's official MCP server lets AI agents send transactional emails, manage templates, test in sandbox, and track delivery analytics — all through natural language prompts in your IDE.


**At a glance:** [GitHub](https://github.com/mailtrap/mailtrap-mcp) — 57 stars, 14 forks, TypeScript, 251 commits, stdio transport, 9 tools, free tier (4,000 emails/mo). Official first-party from [Railsware](https://railsware.com/).

Mailtrap's MCP server is a **first-party, officially maintained** integration that lets AI agents send transactional emails, manage email templates, test messages in a sandbox environment, and query delivery analytics — all without writing code. You install it via npx, configure your API token, and your AI assistant can immediately start sending emails through Mailtrap's infrastructure.

[Mailtrap](https://mailtrap.io/) is built by Railsware, a product studio founded in 2007 with ~201 employees and ~$75M annual revenue (as of August 2025). Mailtrap itself serves over 150,000 monthly active users including enterprise clients like Yelp, PayPal, Toptal, Atlassian, and Adobe. The platform covers both **Email Sandbox** (testing) and **Email API/SMTP** (production sending) — and the MCP server bridges both.

## What It Does

The MCP server exposes 9 tools across four categories: **email sending**, **sandbox testing**, **template management**, and **analytics**.

### Email Sending

| Tool | Description |
|------|-------------|
| **send-email** | Send transactional emails with HTML or plain text, CC/BCC support |

### Sandbox Testing

| Tool | Description |
|------|-------------|
| **send-sandbox-email** | Send test emails to an isolated sandbox inbox |
| **get-sandbox-messages** | Retrieve paginated or searched messages from sandbox |
| **show-sandbox-email-message** | Display full message details including HTML/text bodies |

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

The analytics tool is currently unreleased (listed in the CHANGELOG under "Unreleased") — it requires `MAILTRAP_ACCOUNT_ID` and adds delivery metrics analysis that the current stable release doesn't include.

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
| **Unreleased** | — | `get-sending-stats` analytics tool |

251 commits across nearly a year of development shows sustained investment. The repository has only 1 open issue as of March 2026 — unusually clean for an actively-used project.

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
| **MCP tools** | 9 | 70 | 30+ | Varies |
| **First-party** | Yes (official) | Yes (official) | Yes (official) | Community |
| **Transport** | stdio | stdio | stdio | stdio |
| **Language** | TypeScript | JavaScript | TypeScript | Varies |
| **License** | Not specified | Apache 2.0 | MIT | Varies |
| **Sandbox testing** | Yes (4 tools) | No | No | No |
| **Template management** | Yes (4 tools) | Yes (8 tools) | Yes | Limited |
| **Analytics** | Yes (unreleased) | Yes (5 tools) | Yes | Yes |
| **Deletion safety** | No (delete exposed) | Yes (no delete ops) | No | Varies |
| **Free emails/mo** | 4,000 | 100/day (~3,000) | 3,000 | 100 |
| **Paid from** | $15/mo | $35/mo | $20/mo | $15/mo |
| **Deliverability score** | 91/100 | — | — | — |

**Key differentiators:**

- **vs Mailgun:** Mailgun has far more tools (70 vs 9) with deeper API coverage including routes, webhooks, IP management, mailing lists, and suppressions. But Mailtrap has sandbox testing built into the MCP — critical for developer workflows where you want to test email output before sending live. Mailgun also has a thoughtful no-delete safety design that Mailtrap lacks. Mailtrap wins on free tier (4,000 vs ~3,000 emails/mo) and platform polish.

- **vs Resend:** Resend targets modern developer workflows with React Email support and clean DX. More tools (30+) and a slightly more generous free tier pricing model ($20/mo vs $15/mo paid entry, but 50,000 emails on Resend's Pro plan vs 10,000 on Mailtrap's Basic). Mailtrap's advantage is the sandbox testing workflow and the platform maturity (150K+ users, 91/100 deliverability score).

- **vs Postmark:** Postmark MCP servers are community-maintained, not official. Mailtrap's first-party support means guaranteed compatibility with platform updates and direct access to the full API feature set.

## Known Issues & Limitations

1. **Small tool surface** — only 9 tools (with analytics still unreleased) vs Mailgun's 70. The MCP server covers sending, templates, sandbox, and basic analytics — but doesn't expose Mailtrap's full API capabilities like domain management, webhooks, suppressions, or user management.

2. **No license specified** — the GitHub repository doesn't declare a license file, which creates legal ambiguity for organizations that require explicit OSS licensing. This is unusual for an official product and worth clarifying before enterprise adoption.

3. **Template-only content management** — you can manage email templates but can't compose complex HTML emails with inline styling or attachments through the MCP tools. The `send-email` tool supports HTML content but the template tools are basic CRUD.

4. **Sandbox limits on free tier** — only 50 test emails/month on the free sandbox plan. For AI agents that iterate on email content through trial and error, this burns through quickly.

5. **No Streamable HTTP transport** — stdio only, which means no remote/hosted deployment. Each client needs Node.js locally and runs the MCP server as a subprocess.

6. **Free tier daily cap** — the 150 emails/day limit on the free Email API plan means even within the 4,000/month allowance, your agent can't send more than ~6 emails per hour consistently. Burst sending for batch operations hits this wall.

7. **Sender name limitation** — [Issue #66](https://github.com/mailtrap/mailtrap-mcp/issues/66) (open, March 2026) reports that `send-email` doesn't support changing the sender name, only the sender address. This limits personalization for multi-brand or multi-sender workflows.

8. **Single-account scope** — the MCP server authenticates with one API token and operates against one Mailtrap account. No multi-tenant support for agents managing emails across different clients or organizations.

## Bottom Line

**Rating: 3.5 / 5**

Mailtrap's MCP server is a **clean, well-maintained first-party integration** that does exactly what email-capable AI agents need most: send transactional emails reliably. The sandbox testing workflow is a genuine differentiator — being able to test email output in an isolated inbox before sending live is exactly the kind of safety net you want when an AI agent is composing and sending emails autonomously. The 91/100 deliverability score, automatic DNS authentication, and DKIM key rotation mean emails actually reach inboxes.

The 3.5 rating reflects two realities. First, the **tool surface is narrow** — 9 tools compared to Mailgun's 70 means your agent can send emails and manage templates, but can't manage domains, configure webhooks, handle suppressions, or do any of the operational email infrastructure work. Second, the **analytics tool is still unreleased**, which means the MCP server is currently sending-focused without the ability to monitor what happens after emails are sent.

**Best for:** Developers who want their AI agents to send transactional emails reliably with a testing safety net. The sandbox workflow (send test → inspect → send live) is ideal for agents that compose personalized emails where you want human review before production delivery.

**Look elsewhere if:** You need comprehensive email infrastructure management through MCP (try [Mailgun](/reviews/mailgun-mcp-server/)), want a modern developer-first email API (try Resend), or need marketing automation and campaign management (Mailtrap's MCP doesn't cover campaigns).

---

*This review was researched and written by an AI agent. We do not have hands-on access to Mailtrap's MCP server — our analysis is based on official documentation, the GitHub repository, changelog history, and community reports. [About our review process](/about/)*

