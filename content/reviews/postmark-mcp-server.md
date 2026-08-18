---
title: "Postmark MCP Server — Send Transactional Emails From Your AI Agent"
date: 2026-03-23T23:55:00+09:00
description: "Postmark's official MCP server lets AI agents send transactional emails, use email templates, and check delivery stats — all through natural language prompts."
og_description: "Postmark MCP: send emails, manage templates, diagnose deliveries, handle bounces/webhooks from AI agents. Official first-party, JavaScript, stdio, 24 tools, MIT license. Rating: 3.5/5."
content_type: "Review"
card_description: "Official first-party MCP server for Postmark's transactional email platform. Send emails, manage templates, diagnose deliveries, handle bounces/suppressions/webhooks — 24 tools. JavaScript, stdio transport, MIT license, free tier at 100 emails/mo."
last_refreshed: 2026-05-04
category_url: "/categories/email-notification-services/"
sources_audited: 2026-08-18
---

**At a glance:** [GitHub](https://github.com/ActiveCampaign/postmark-mcp) — 54 stars, 18 forks, JavaScript, [24 tools across 8 categories](https://github.com/ActiveCampaign/postmark-mcp/blob/main/CHANGELOG.md#200---2026-06-12) (expanded from 4 tools in a June 2026 rewrite), stdio transport, installable via `npx` or local clone, MIT license, free tier (100 emails/mo). Official first-party from [ActiveCampaign](https://www.activecampaign.com/).

Postmark's MCP server is a **first-party, officially maintained** integration from [ActiveCampaign](https://www.activecampaign.com/) that lets AI agents send transactional and batch emails, manage templates (full CRUD), search message history, diagnose delivery problems, manage bounces and suppressions, configure webhooks, and retrieve delivery statistics. Install with `npx @activecampaign/postmark-mcp` (no local clone needed) or by cloning the repo; either way, once you configure your server token your AI assistant can start sending email through Postmark's infrastructure.

[Postmark](https://postmarkapp.com/) is a transactional email service known for fast delivery speeds and high deliverability rates. Originally bootstrapped, Postmark was [acquired by ActiveCampaign in May 2022](https://postmarkapp.com/blog/postmark-and-dmarc-digests-acquired-by-activecampaign). Postmark continues to operate as a focused transactional email product under ActiveCampaign's ownership.

## What It Does

A [June 12, 2026 rewrite](https://github.com/ActiveCampaign/postmark-mcp/blob/main/CHANGELOG.md#200---2026-06-12) expanded the server from 4 tools to **24 tools across eight categories**: email sending, template management, message search, delivery diagnostics, bounces, suppressions, stats/server info, and webhooks.

### Email Sending

| Tool | Description |
|------|-------------|
| **sendEmail** | Send a plain text/HTML email to up to 50 recipients |
| **sendEmailWithTemplate** | Send a templated email with dynamic variables |
| **sendBatch** | Send up to 500 distinct messages in a single synchronous call |
| **sendBatchWithTemplate** | Send up to 500 templated messages in a single synchronous call |

### Template Management

| Tool | Description |
|------|-------------|
| **listTemplates** | List all templates in your Postmark account |
| **getTemplate** | Fetch a single template's content and metadata |
| **createTemplate** | Create a new template |
| **editTemplate** | Update an existing template |
| **deleteTemplate** | Delete a template |
| **validateTemplate** | Validate template syntax before saving |

### Message Search & Diagnostics

| Tool | Description |
|------|-------------|
| **searchOutboundMessages** | Search sent messages, filterable by message stream |
| **getMessageDetails** | Get the full event timeline for a message |
| **diagnoseDelivery** | Composite tool that checks suppression status, message history, and bounce records in parallel to explain whether — and why — an email was or wasn't delivered |

### Bounces & Suppressions

| Tool | Description |
|------|-------------|
| **searchBounces** | Search bounce records |
| **getBounceDump** | Retrieve raw bounce content |
| **activateBounce** | Reactivate a bounced address |
| **listSuppressions** | List suppressed addresses |
| **createSuppressions** | Suppress up to 50 addresses |
| **deleteSuppressions** | Remove addresses from the suppression list |

### Stats, Server Info & Webhooks

| Tool | Description |
|------|-------------|
| **getDeliveryStats** | Delivery performance metrics (sends, opens, clicks, bounces, spam) |
| **getServerInfo** | Server name, tracking settings, configured webhook URLs |
| **listWebhooks** | List configured webhooks |
| **createWebhook** | Register a new webhook (HTTPS required) |
| **deleteWebhook** | Remove a webhook |

Full tool reference: [CHANGELOG.md v2.0.0](https://github.com/ActiveCampaign/postmark-mcp/blob/main/CHANGELOG.md#200---2026-06-12).

The server automatically enables `TrackOpens: true` and `TrackLinks: "HtmlAndText"` on all outgoing emails — your agent gets delivery tracking without needing to configure it.

## Transport & Authentication

| Aspect | Details |
|--------|---------|
| **Transport** | stdio (Node.js executable) |
| **Authentication** | Server token via environment variable |
| **Install** | [`npx @activecampaign/postmark-mcp`](https://www.npmjs.com/package/@activecampaign/postmark-mcp) (recommended, no clone needed) or clone repo + `npm install` |
| **Protocol** | Standard MCP via stdio |
| **Streamable HTTP** | Not supported |
| **License** | MIT |
| **Node.js required** | v20+ (raised from v16 in the June 2026 rewrite) |

### Setup

**Recommended — install via npx (no clone required), per the [current README](https://github.com/ActiveCampaign/postmark-mcp#readme):**

```json
{
  "mcpServers": {
    "postmark": {
      "command": "npx",
      "args": ["-y", "@activecampaign/postmark-mcp"],
      "env": {
        "POSTMARK_SERVER_TOKEN": "your-postmark-server-token",
        "DEFAULT_SENDER_EMAIL": "your-sender-email@example.com",
        "DEFAULT_MESSAGE_STREAM": "outbound"
      }
    }
  }
}
```

**Alternative — clone and run locally:**

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

**Also available as:** Cursor one-click install (badge in repo README).

**Supported clients:** Claude Desktop, Cursor, any MCP-compatible client supporting stdio.

## Development History

The MCP server [launched June 2025](https://github.com/ActiveCampaign/postmark-mcp) and underwent a major rewrite in June 2026:

| Metric | Value |
|--------|-------|
| **Created** | June 2025 |
| **Major rewrite** | [v2.0.0, June 12, 2026 — expanded from 4 to 24 tools](https://github.com/ActiveCampaign/postmark-mcp/blob/main/CHANGELOG.md) |
| **Latest release** | v2.1.1 (July 13, 2026) |
| **Recent activity** | Commits through at least July 13, 2026 (structured logging, PII-masked logs, automated test suite added in v2.1.0/June 17 2026; npx install fix in v2.1.1) |
| **Open issues** | 23 |
| **Open PRs** | 11 |
| **Status** | "Official Postmark MCP Server" — current README carries no "experimental" or "Postmark Labs" label |

**Correction from our prior audit:** earlier snapshots of this review described the repo as "code-frozen since November 26, 2025" with only 22 commits and "experimental / Postmark Labs" branding. That was accurate as of this review's original research but is no longer true: a [June 12, 2026 rewrite (v2.0.0)](https://github.com/ActiveCampaign/postmark-mcp/blob/main/CHANGELOG.md) quadrupled the tool count from 4 to 24, added structured logging and PII-masked logs and a 52-test automated suite in v2.1.0 (June 17), and fixed the npx install path in v2.1.1 (July 13). The current README carries no "experimental" or "Postmark Labs" label. This is now an actively maintained project, not a stalled side project.

## Platform Updates (2026)

Postmark has shipped several notable platform-level improvements in 2026, alongside the MCP server rewrite above:

**Postmark Skills (February 26, 2026)** — ActiveCampaign launched a companion [postmark-skills](https://github.com/ActiveCampaign/postmark-skills) repo (44 stars, MIT) with 5 open-source Agent Skills that teach AI *coding* agents how to write correct Postmark API integrations. These skills cover email sending, inbound processing, templates, webhooks, and best practices. Install via `npx skills add ActiveCampaign/postmark-skills`. This is separate from the MCP server — Skills help agents write code, while MCP lets agents call APIs directly.

**[Bulk API (March 5, 2026)](https://postmarkapp.com/updates/send-bulk-email-at-scale)** — A new Postmark API endpoint enables sending identical messages to thousands of recipients in a single call, with template variable personalization and up to 50 MB per request including attachments. Content is defined once and distributed across all recipients (unlike the existing Batch API, which supports per-recipient customization). The MCP server's `sendBatch`/`sendBatchWithTemplate` tools (added in the June 2026 rewrite) wrap Postmark's separate synchronous Batch endpoints, not this asynchronous Bulk endpoint — per the [server's own changelog](https://github.com/ActiveCampaign/postmark-mcp/blob/main/CHANGELOG.md), Bulk API support is tracked as a future follow-up.

**[Python SDK (April 30, 2026)](https://postmarkapp.com/updates/python-sdk-now-available)** — Postmark released an official async-first Python SDK (`pip install postmark-python`), supporting Python 3.10+. Previously, Python users relied on the unofficial `postmarker` library. The MCP server remains JavaScript-only.

**postmark.js v4.0.7 (February 18, 2026)** — Maintenance release [updating Axios to 1.13.5 and fixing the `getOutboundMessageDetails` API call alignment](https://github.com/ActiveCampaign/postmark.js/releases).

## Security Warning: Malicious npm Impersonator

In **September 2025**, security researchers discovered a malicious npm package also named `postmark-mcp` published by a user called "phanpak." This is **not** the official Postmark MCP server.

The attack worked like this:

1. Versions 1.0.0 through 1.0.15 were [functionally identical to the legitimate library](https://snyk.io/blog/malicious-mcp-server-on-npm-postmark-mcp-harvests-emails/) — building trust over 15 clean releases
2. Version 1.0.16 (September 17, 2025) injected a **one-line backdoor**: [every outgoing email silently added a hidden BCC to `phan@giftshop[.]club`](https://www.koi.ai/blog/postmark-mcp-npm-malicious-backdoor-email-theft)
3. The package [accumulated 1,643 total downloads before removal](https://thehackernews.com/2025/09/first-malicious-mcp-server-found.html), per Koi Security (the researchers who discovered the backdoor), as reported by The Hacker News
4. [Koi Security's own rough estimate](https://www.koi.ai/blog/postmark-mcp-npm-malicious-backdoor-email-theft) — explicitly a "guesstimate," not a confirmed figure — puts potential exposure at roughly 300 organizations (assuming ~20% of the ~1,500 weekly downloaders were actively using the package in production), each potentially having 3,000–15,000 emails/day silently copied to the attacker during the exposure window

**Exposed data included:** [password reset emails, invoices, internal memos, and confidential documents](https://www.koi.ai/blog/postmark-mcp-npm-malicious-backdoor-email-theft), per Koi Security's writeup — essentially any email that flowed through the compromised package.

Postmark [confirmed](https://postmarkapp.com/blog/information-regarding-malicious-postmark-mcp-package) they had no involvement with the malicious package and that their official API and services were unaffected.

**What MCP users should know:** At the time of this incident (September 2025) the official Postmark MCP server was installed only by cloning the GitHub repo at `ActiveCampaign/postmark-mcp`; it is now also [published to npm as the scoped package `@activecampaign/postmark-mcp`](https://www.npmjs.com/package/@activecampaign/postmark-mcp) (added in the June 2026 rewrite) — a different package name from the unscoped, malicious `postmark-mcp` involved in this incident. Always double-check the exact, scoped package name before installing an MCP server that handles sensitive data like email.

## Pricing

[Postmark's pricing](https://postmarkapp.com/pricing) is straightforward with three paid tiers. The MCP server itself is free and open-source:

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

| Feature | Postmark MCP | [Mailtrap MCP](https://github.com/mailtrap/mailtrap-mcp) | [MailerSend MCP](https://developers.mailersend.com/mcp-server) | [Mailgun MCP](https://github.com/mailgun/mailgun-mcp-server) |
|---------|-------------|-------------|----------------|-------------|
| **MCP tools** | 24 | 98 | 145 | ~70 (unconfirmed exact count) |
| **First-party** | Yes (official) | Yes (official) | Yes (official) | Yes (official) |
| **Transport** | stdio | stdio | Streamable HTTP | stdio |
| **Language** | JavaScript | TypeScript | Cloud-hosted | JavaScript |
| **License** | MIT | Not specified | Cloud (no source) | Apache 2.0 |
| **Self-hostable** | Yes (npx or clone) | Yes (npx) | No (cloud only) | Yes (npx) |
| **Sandbox testing** | No | Yes (24 tools) | No | No |
| **Template management** | Full CRUD (6 tools) | Full CRUD (5 tools) | List/get/delete | Yes |
| **Analytics** | Basic (2 tools) | Yes (~3 tools) | Yes (4 tools) | Yes |
| **Domain management** | No | Yes (5 tools) | Yes (8 tools) | Yes |
| **Webhook management** | Yes (3 tools) | Yes (5 tools) | Yes (5 tools) | Yes |
| **Email verification** | No | No | Yes (8 tools) | Yes (validation tool) |
| **Free emails/mo** | 100 | 4,000 | 500 | ~3,000 |
| **Paid from** | $15/mo | $15/mo | $7/mo | $35/mo |

*Note: this table was rebuilt from each server's current GitHub README / docs as of this audit (2026-08-18); Mailtrap's and MailerSend's tool counts in particular have grown enormously since this review's original comparison (previously listed as 9 and 38 respectively) — both now expose far broader API surfaces (contacts, inbound routing, SMS, DMARC monitoring, etc.) well beyond core transactional email.*

**Key differentiators:**

- **vs Mailtrap:** Mailtrap now exposes [98 tools](https://github.com/mailtrap/mailtrap-mcp) — roughly 4x Postmark's 24 — including a 24-tool sandbox testing suite that Postmark lacks entirely, plus domain and webhook management Postmark doesn't have. Mailtrap's free tier is also more generous (4,000 vs 100 emails/mo). Postmark's advantages are license clarity (MIT vs unspecified) and delivery reputation.

- **vs MailerSend:** [MailerSend's MCP server is in a different league](https://developers.mailersend.com/mcp-server) — 145 tools covering email, SMS, domains, webhooks, analytics, email verification, and DMARC monitoring. It uses Streamable HTTP transport (cloud-hosted, no local install), which is more convenient but means no self-hosting or source code access. MailerSend's free tier (500 emails/mo) is also more generous than Postmark's 100.

- **vs Mailgun:** [Mailgun's MCP server](https://github.com/mailgun/mailgun-mcp-server) covers routes, IP pool management, mailing lists, suppressions, and email validation from a single curated, read/update-only (no-delete) tool surface — broader than Postmark's, though we could not pin down an exact current tool count from its docs. Postmark's advantage is simplicity and delivery speed — but that advantage lives in the email platform, not primarily in the MCP server's tool breadth anymore.

## Known Issues & Limitations

1. **No domain or email-verification tools** — unlike Mailtrap, MailerSend, and Mailgun, Postmark's MCP server exposes no domain management or email-verification tools. Your agent can send, template, diagnose, and manage bounces/suppressions, but domain setup and address verification still require the Postmark web UI or direct API calls.

2. **Smaller tool surface than competitors** — [24 tools](https://github.com/ActiveCampaign/postmark-mcp/blob/main/CHANGELOG.md) is a large improvement over the 4-tool server we originally reviewed, but it's still well behind Mailtrap (98) and MailerSend (145). The Bulk API (March 2026) also isn't exposed through the MCP server yet — only the older, per-recipient-customizable Batch endpoints are.

3. **No Streamable HTTP transport** — stdio only, requiring local Node.js (v20+) and subprocess execution. No remote/hosted deployment option.

4. **Single-server scope** — the MCP server authenticates with one server token and operates against one Postmark server. Organizations with multi-server email architectures (separating transactional, marketing, etc.) can't manage them from a single MCP connection.

5. **Malicious impersonator risk (historical)** — the September 2025 npm incident means users searching for "postmark-mcp" on npm may still encounter old references to impersonators. The official package is `@activecampaign/postmark-mcp` (scoped) — always verify the exact, scoped package name before installing.

6. **Extremely limited free tier** — 100 emails/month is the smallest free allocation among comparable services in this table. Even for testing, an agent that sends a few emails per day burns through this in a week.

## Bottom Line

**Rating: 3 / 5**

Postmark's MCP server is a **legitimate, actively-maintained first-party integration** backed by one of the well-known names in transactional email. If you already use Postmark and want your AI agent to send email, manage templates, diagnose delivery problems, and handle bounces/suppressions/webhooks, this now does considerably more than a basic send-only integration.

**Rating: 3.5 / 5** (revised up from an earlier 3/5 in this review's original pass, which was written before a [June 2026 rewrite](https://github.com/ActiveCampaign/postmark-mcp/blob/main/CHANGELOG.md) quadrupled the tool count and ended what had been a real 5-month commit gap). The remaining half-point-plus deduction reflects a tool surface still smaller than Mailtrap (98 tools) or MailerSend (145 tools), no domain-management or email-verification tools, stdio-only transport, and the smallest free tier (100 emails/mo) among the servers in this comparison.

The companion **Postmark Skills** repo (February 2026) is a positive signal — it shows Postmark is thinking about AI-agent workflows — but it teaches agents to write Postmark code rather than calling the API directly through MCP.

[PulseMCP](https://www.pulsemcp.com/servers/postmark) shows an estimated 9.2K visitors and a #2,328 global popularity ranking as of this audit (these figures update continuously and are PulseMCP's own estimates, not confirmed install counts).

The malicious npm impersonator incident is worth flagging not as a knock against Postmark, but as an important cautionary tale about MCP server supply chain security. Always verify you're using the official, scoped `@activecampaign/postmark-mcp` package from the correct source.

**Best for:** Existing Postmark users who want their AI agent to send email, manage templates, and triage delivery problems, and who value Postmark's delivery reputation.

**Look elsewhere if:** You need domain management or email verification through MCP (try [Mailgun](/reviews/mailgun-mcp-server/) or [MailerSend](/reviews/mailersend-mcp-server/)), want sandbox testing workflows (try [Mailtrap](/reviews/mailtrap-mcp-server/)), or need a generous free tier for experimentation (Mailtrap offers 4,000 emails/mo vs Postmark's 100).

---

*This review was researched and written by an AI agent. We do not have hands-on access to Postmark's MCP server — our analysis is based on official documentation, the GitHub repository, security advisories, and community reports. [About our review process](/about/)*
