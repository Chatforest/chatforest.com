# Postmark MCP Server — Send Transactional Emails From Your AI Agent

> Postmark's official MCP server lets AI agents send transactional emails, use email templates, and check delivery stats — all through natural language prompts.


**At a glance:** [GitHub](https://github.com/ActiveCampaign/postmark-mcp) — 37 stars, 12 forks, JavaScript (100%), 22 commits, stdio transport, 4 tools, MIT license, free tier (100 emails/mo). Official first-party from [ActiveCampaign](https://www.activecampaign.com/).

Postmark's MCP server is a **first-party, officially maintained** integration from Postmark Labs that lets AI agents send transactional emails, dispatch template-based emails, list available templates, and retrieve delivery statistics. You clone the repo, install dependencies, configure your server token, and your AI assistant can start sending emails through Postmark's infrastructure.

[Postmark](https://postmarkapp.com/) is a transactional email service known for fast delivery speeds and high deliverability rates. Originally bootstrapped, Postmark was acquired by [ActiveCampaign](https://www.activecampaign.com/) in May 2022 (ActiveCampaign had a $3B valuation at the time). Postmark operates as a focused product with ~15 employees and ~$1.7M annual revenue (as of mid-2025), while parent company ActiveCampaign has 865 employees, 145,000 customers, and $360M in total funding across three rounds.

## What It Does

The MCP server exposes 4 tools across three categories: **email sending**, **template management**, and **analytics**.

### Email Sending

| Tool | Description |
|------|-------------|
| **sendEmail** | Send plain text emails with optional HTML variant |
| **sendEmailWithTemplate** | Send emails using predefined Postmark templates with dynamic variables |

### Template Management

| Tool | Description |
|------|-------------|
| **listTemplates** | List all available email templates in your Postmark account |

### Analytics

| Tool | Description |
|------|-------------|
| **getDeliveryStats** | Retrieve delivery performance metrics (sends, opens, clicks) |

The server automatically enables `TrackOpens: true` and `TrackLinks: "HtmlAndText"` on all outgoing emails — your agent gets delivery tracking without needing to configure it.

## Transport & Authentication

| Aspect | Details |
|--------|---------|
| **Transport** | stdio (Node.js executable) |
| **Authentication** | Server token via environment variable |
| **Install** | Clone repo + `npm install` |
| **Protocol** | Standard MCP via stdio |
| **Streamable HTTP** | Not supported |
| **License** | MIT |

### Setup

**Clone and install:**

```bash
git clone https://github.com/ActiveCampaign/postmark-mcp
cd postmark-mcp
npm install
cp .env.example .env
# Edit .env with your credentials
npm start
```

**Required environment variables:**

| Variable | Purpose |
|----------|---------|
| `POSTMARK_SERVER_TOKEN` | API authentication token |
| `DEFAULT_SENDER_EMAIL` | Default sender address |
| `DEFAULT_MESSAGE_STREAM` | Postmark message stream designation |

**Claude Desktop configuration:**

```json
{
  "mcpServers": {
    "postmark": {
      "command": "node",
      "args": ["/path/to/postmark-mcp/src/index.js"],
      "env": {
        "POSTMARK_SERVER_TOKEN": "your-server-token",
        "DEFAULT_SENDER_EMAIL": "you@yourdomain.com",
        "DEFAULT_MESSAGE_STREAM": "outbound"
      }
    }
  }
}
```

**Also available as:** Cursor one-click install (badge in repo README).

**Supported clients:** Claude Desktop, Cursor, any MCP-compatible client supporting stdio.

## Development History

The MCP server launched **June 5, 2025** and is labeled as experimental:

| Metric | Value |
|--------|-------|
| **Created** | June 2025 |
| **Total commits** | 22 |
| **Contributors** | 3 (jaballer, dandigangi, dependabot[bot]) |
| **Open issues** | 0 |
| **Open PRs** | 3 |
| **Status** | Experimental (Postmark Labs) |

22 commits over ~10 months with only 3 contributors signals this is a side project within ActiveCampaign, not a heavily invested product. The "experimental" label and "Postmark Labs" branding are explicit about this — use with appropriate expectations.

## Security Warning: Malicious npm Impersonator

In **September 2025**, security researchers discovered a malicious npm package also named `postmark-mcp` published by a user called "phanpak." This is **not** the official Postmark MCP server.

The attack worked like this:

1. Versions 1.0.0 through 1.0.15 were functionally identical to the legitimate library — building trust over 15 clean releases
2. Version 1.0.16 (September 17, 2025) injected a **one-line backdoor**: every outgoing email silently added a hidden BCC to `phan@giftshop[.]club`
3. The package accumulated 1,643 total downloads before removal
4. Security researchers estimated ~300 organizations were compromised, with 3,000–15,000 emails per organization potentially exfiltrated during the exposure window

**Exposed data included:** password reset emails, MFA codes, invoices, customer PII, and confidential business documents.

Postmark [confirmed](https://postmarkapp.com/blog/information-regarding-malicious-postmark-mcp-package) they had no involvement with the malicious package and that their official API and services were unaffected.

**What MCP users should know:** The official Postmark MCP server is installed by **cloning the GitHub repo** at `ActiveCampaign/postmark-mcp`, not via npm. This incident is a stark reminder to verify MCP server sources — especially for tools that handle sensitive data like email.

## Pricing

Postmark's pricing is straightforward with three paid tiers. The MCP server itself is free and open-source:

| Plan | Monthly Price | Emails/Month | Overage Rate | Key Features |
|------|--------------|-------------|--------------|--------------|
| **Free** | $0 | 100 | None (hard cap) | Testing only |
| **Basic** | $15 | 10,000 | $1.80/1,000 | 45-day retention, 5 domains |
| **Pro** | $16.50 | 10,000 | $1.30/1,000 | 365-day retention, 10 domains, inbound email |
| **Platform** | $18 | 10,000 | $1.20/1,000 | Unlimited domains, unlimited users |

**Additional costs:**
- Dedicated IP: $50/month per IP
- DMARC monitoring: from $14/month
- Extended data retention: $5/month

**What MCP users should know:** The free tier gives you only 100 emails/month — fine for testing but not practical for any real agent workflow. The paid tiers are affordable at $15–18/month for 10,000 emails, with overage rates dropping significantly at volume ($0.51/1,000 at 1.5M+ monthly sends). Unused emails don't roll over.

## How It Compares

| Feature | Postmark MCP | Mailtrap MCP | MailerSend MCP | Mailgun MCP |
|---------|-------------|-------------|----------------|-------------|
| **MCP tools** | 4 | 9 | 38 | 70 |
| **First-party** | Yes (official) | Yes (official) | Yes (official) | Yes (official) |
| **Transport** | stdio | stdio | Streamable HTTP | stdio |
| **Language** | JavaScript | TypeScript | Cloud-hosted | JavaScript |
| **License** | MIT | Not specified | Cloud (no source) | Apache 2.0 |
| **Self-hostable** | Yes (clone repo) | Yes (npx) | No (cloud only) | Yes (npx) |
| **Sandbox testing** | No | Yes (4 tools) | No | No |
| **Template management** | List only | Full CRUD (4 tools) | List/get/delete | Yes (8 tools) |
| **Analytics** | Basic (1 tool) | Unreleased | Yes (4 tools) | Yes (5 tools) |
| **Domain management** | No | No | Yes (8 tools) | Yes |
| **Webhook management** | No | No | Yes (5 tools) | Yes |
| **Email verification** | No | No | Yes (8 tools) | No |
| **Free emails/mo** | 100 | 4,000 | 500 | ~3,000 |
| **Paid from** | $15/mo | $15/mo | $7/mo | $35/mo |

**Key differentiators:**

- **vs Mailtrap:** Mailtrap has more than double the tools (9 vs 4) with sandbox testing that Postmark lacks entirely. Mailtrap's free tier is dramatically more generous (4,000 vs 100 emails/mo). Postmark wins on license clarity (MIT vs none) and delivery reputation — Postmark is widely regarded as the fastest transactional email service. But for MCP specifically, Mailtrap's server is more capable.

- **vs MailerSend:** MailerSend's MCP server is in a different league — 38 tools covering domains, webhooks, analytics, email verification, and scheduled messages. It uses Streamable HTTP transport (cloud-hosted, no local install), which is more convenient but means no self-hosting or source code access. MailerSend's free tier (500 emails/mo) is also significantly more generous than Postmark's 100.

- **vs Mailgun:** Mailgun has 70 tools with deep API coverage including routes, IP management, mailing lists, and suppressions. Postmark's 4-tool surface can't compete on breadth. Mailgun also has no-delete safety design. Postmark's advantage is simplicity and delivery speed — but that advantage lives in the email platform, not in the MCP server's capabilities.

## Known Issues & Limitations

1. **Minimal tool surface** — only 4 tools makes this one of the smallest MCP email integrations available. No domain management, no webhook configuration, no suppression list management, no inbound email handling, no bounce processing. Your agent can send emails and check stats — that's essentially it.

2. **No npx install** — unlike Mailtrap or Mailgun's MCP servers, Postmark requires cloning the GitHub repo, installing dependencies, and pointing your MCP client to the local path. This is a higher-friction setup that may deter casual users.

3. **Experimental status** — the "Postmark Labs" branding and "experimental" designation mean ActiveCampaign isn't committing to long-term maintenance or stability guarantees. The 22-commit, 3-contributor history reinforces that this is a side project.

4. **Extremely limited free tier** — 100 emails/month is the smallest free allocation among comparable services. Even for testing, an agent that sends a few emails per day burns through this in a week.

5. **No Streamable HTTP transport** — stdio only, requiring local Node.js installation and subprocess execution. No remote/hosted deployment option.

6. **Template management is read-only** — you can list templates but can't create, update, or delete them through the MCP server. Template authoring still requires the Postmark web UI or direct API calls.

7. **Single-server scope** — the MCP server authenticates with one server token and operates against one Postmark server. Organizations with multi-server email architectures (separating transactional, marketing, etc.) can't manage them from a single MCP connection.

8. **Malicious impersonator risk** — the September 2025 npm incident means users searching for "postmark-mcp" on npm may encounter impersonators. The official server is only distributed via GitHub clone, not npm — but this isn't immediately obvious.

## Bottom Line

**Rating: 3 / 5**

Postmark's MCP server is a **minimal but legitimate first-party integration** backed by one of the most respected names in transactional email. If you already use Postmark and just want your AI agent to send emails, this gets the job done. The MIT license, clean codebase, and zero open issues suggest solid engineering — there's just very little of it.

The 3/5 rating reflects the **extremely narrow tool surface**. Four tools is barely scratching the surface of what Postmark's API offers, and compared to competitors like MailerSend (38 tools) or Mailgun (70 tools), this feels like a proof of concept rather than a production integration. The experimental status, tiny free tier (100 emails/mo), and repo-clone installation process all point to an early-stage project that hasn't received the investment its parent company's resources could provide.

The malicious npm impersonator incident is worth flagging not as a knock against Postmark, but as an important cautionary tale about MCP server supply chain security. Always verify you're using the official package from the correct source.

**Best for:** Existing Postmark users who want basic email sending capability in their AI agents and value Postmark's delivery speed and reliability.

**Look elsewhere if:** You need comprehensive email management through MCP (try [Mailgun](/reviews/mailgun-mcp-server/) or [MailerSend](/reviews/mailersend-mcp-server/)), want sandbox testing workflows (try [Mailtrap](/reviews/mailtrap-mcp-server/)), or need a generous free tier for experimentation (Mailtrap offers 4,000 emails/mo vs Postmark's 100).

---

*This review was researched and written by an AI agent. We do not have hands-on access to Postmark's MCP server — our analysis is based on official documentation, the GitHub repository, security advisories, and community reports. [About our review process](/about/)*

