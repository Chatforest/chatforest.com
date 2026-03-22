---
title: "Best Email & Notifications MCP Servers in 2026"
date: 2026-03-22T15:00:00+09:00
description: "Personal email, enterprise email, transactional delivery, SMS, and push notifications — we've reviewed 50+ email and notification MCP servers across 5 categories. Here's what works, what's risky, and what to avoid."
og_description: "50+ email and notification MCP servers reviewed across Gmail, Outlook, transactional delivery, SMS/multi-channel, and push notifications. taylorwilsdon, Resend, Infobip, and more — with honest ratings."
content_type: "Comparison"
card_description: "The definitive guide to email and notification MCP servers in 2026. We've reviewed 50+ servers across personal email, enterprise email, transactional delivery, SMS/multi-channel, and push notifications. Every recommendation links to a full review."
last_refreshed: 2026-03-22
---

Email is the most sensitive data most people have. Bank confirmations, medical records, password resets, private conversations — it's all in your inbox. Notifications are the outbound side: transactional emails, SMS alerts, push notifications, WhatsApp messages. Giving an AI agent access to either side deserves serious thought.

We've published [3 in-depth reviews](/reviews/) covering 50+ email and notification MCP servers across the entire communication stack. This guide synthesizes all of that into one page: what's worth using, what's not, and where the gaps are.

## The short version

| Category | Our pick | Rating | Runner-up |
|----------|----------|--------|-----------|
| Personal email (Gmail) | [taylorwilsdon/google_workspace_mcp](/reviews/gmail-mcp-servers/) | 3.5/5 | [Google Workspace MCP](/reviews/gmail-mcp-servers/) (official, hosted) |
| Enterprise email (Outlook) | [Softeria/ms-365-mcp-server](/reviews/outlook-mcp-servers/) | 3.5/5 | [Microsoft Work IQ Mail](/reviews/outlook-mcp-servers/) (official, Copilot license required) |
| Transactional email delivery | [Resend MCP](/reviews/notification-services-mcp-servers/) | 3.5/5 | [Mailgun MCP](/reviews/notification-services-mcp-servers/) (official, Apache 2.0) |
| SMS & multi-channel | [Infobip MCP](/reviews/notification-services-mcp-servers/) | 3.5/5 | [Twilio MCP](/reviews/notification-services-mcp-servers/) (official, OpenAPI-generated) |
| Push notifications | [ntfy MCP](/reviews/notification-services-mcp-servers/) | 3.5/5 | [Pushover MCP](/reviews/notification-services-mcp-servers/) (30 stars, one-time $5) |
| Multi-provider email | [codefuturist/email-mcp](https://github.com/codefuturist/email-mcp) | — | [marlinjai/email-mcp](https://github.com/marlinjai/email-mcp) (24 tools, unified) |

## Why email MCP servers are different

Most MCP categories are about productivity — do things faster. Email MCP servers are about access to your most sensitive data, and that access cuts both ways:

1. **The stakes are higher.** Your email is the skeleton key to your digital life. Password resets, 2FA codes, financial confirmations, medical records — an agent with email access can reach all of it. A compromised email MCP server is worse than a compromised filesystem server.
2. **Send is irreversible.** An AI agent that sends a hallucinated email to the wrong person can cause real damage. There's no "undo send" via the API. Most MCP categories let you experiment safely; email doesn't.
3. **OAuth scope creep is real.** Most Gmail servers request `gmail.modify` or the full `mail.google.com` scope. Most Outlook servers request broad Graph API permissions. You're often granting access to far more than email.
4. **No official reference server exists.** The MCP project (modelcontextprotocol/servers) has reference servers for filesystem, fetch, GitHub — but not email. Every option is vendor-built or community-built.

Our recommendation across all categories: **start read-only**, enable send/compose only after you trust the agent's behavior, and prefer official servers where available.

## Personal Email — Gmail

**[Full review: Gmail MCP Servers →](/reviews/gmail-mcp-servers/)** | Rating: 3.5/5

Gmail has the most mature MCP ecosystem of any email provider. Multiple solid options, an official Google endpoint, and a dominant community server with 1,700+ stars.

### The winner: taylorwilsdon/google_workspace_mcp

[google_workspace_mcp](https://github.com/taylorwilsdon/google_workspace_mcp) — 1,700+ stars, Python, MIT. Covers 12 Google services including Gmail with 10+ email tools: search, read, send, reply, draft, label management. Three-tier permission system (Core/Extended/Full) lets you start read-only and expand.

**Why it wins:** Largest community, most active development, tiered permissions are a real security advantage. If you're already using Google Workspace, this is the default.

**The catch:** Installing this server grants OAuth access to 12 Google services. If you only need Gmail, you're over-permissioning. The `gmail.modify` scope can delete emails, not just read them.

### Strong alternatives

**Google's official Workspace MCP** — Hosted at `workspace-developer.goog/mcp`. First-party code, Google's security model, no third-party token handling. Documentation is sparser than community options. Choose this if you want maximum trust and don't need to inspect the server code.

**[MarkusPfundstein/mcp-gsuite](https://github.com/MarkusPfundstein/mcp-gsuite)** — 477 stars, Gmail + Calendar only. Narrower OAuth scope is a genuine security advantage. Python 3.13+ requirement is strict.

**[baryhuang/mcp-headless-gmail](https://github.com/baryhuang/mcp-headless-gmail)** — 53 stars. Purpose-built for server/container deployments without a browser. Decoupled OAuth credential model is clever for headless environments.

### Avoid

**GongRzhe/Gmail-MCP-Server** — Abandoned since August 2025, 72+ unmerged PRs. Use the [ArtyMcLabin fork](https://github.com/ArtyMcLabin/Gmail-MCP-Server) if you want that codebase.

## Enterprise Email — Outlook

**[Full review: Outlook MCP Servers →](/reviews/outlook-mcp-servers/)** | Rating: 3.5/5

Outlook MCP servers deal with corporate inboxes behind Entra ID, compliance policies, and DLP rules. Microsoft shipped official servers but locked them behind a Copilot license. Community servers fill the gap.

### The winner: Softeria/ms-365-mcp-server

[ms-365-mcp-server](https://github.com/Softeria/ms-365-mcp-server) — 530 stars, TypeScript, MIT, 243 commits. Covers 8+ Microsoft 365 services from a single install: email, calendar, OneDrive, Excel, OneNote, tasks, contacts, user profile. With `--org-mode`: Teams, SharePoint, online meetings, shared mailboxes.

**Why it wins:** No Copilot license required. Broadest M365 coverage from a single server. Three auth modes (Device Code, OAuth, Bring Your Own Token). TOON output format saves 30-60% on tokens. Read-only mode and tool filtering for safety.

**The catch:** Loading 8+ services means tool sprawl if you only need email. The `--tools` flag mitigates this, but the default is everything. 13 open issues suggest active but imperfect development.

### Strong alternatives

**Microsoft Work IQ Mail** — Official, hosted, 10 tools with KQL search. Microsoft runs it — no local install, no third-party code. ETag concurrency control for enterprise-grade safety. **But:** requires a Microsoft 365 Copilot license (~$30/user/month) and is still in preview. No folder management, no attachment handling.

**[ryaker/outlook-mcp](https://github.com/ryaker/outlook-mcp)** — 278 stars. Unique Power Automate integration alongside email and calendar. An agent that reads emails and triggers automation flows opens workflow possibilities no other server matches. Complex setup (5 steps) and no license specified.

**[merill/lokka](https://github.com/merill/lokka)** — 228 stars, MIT. Exposes the raw Microsoft Graph API as MCP tools. Maximum flexibility — any Graph endpoint, including ones purpose-built servers haven't implemented. Best for developers who already know Graph API. Not for beginners.

### Gmail vs. Outlook — which ecosystem is stronger?

| Feature | Gmail | Outlook (Official) | Outlook (Softeria) |
|---------|-------|-------|-------|
| Official server | Google Workspace MCP | Work IQ Mail | N/A |
| Hosted | Yes | Yes | No (local) |
| License cost | Free | Copilot ~$30/mo | Free (M365 account) |
| Community standard | 1,700+ stars | N/A | 530 stars |
| Services covered | 12 Google services | Mail only | 8+ M365 services |
| Folder management | Labels | No | Yes |
| Attachment handling | Limited | No | Via OneDrive |

**Gmail is more accessible** — no paid license, stronger community, free official endpoint. **Outlook has deeper enterprise integration** — Entra ID, compliance policies, DLP rules. Both share the same fundamental risk: email is sensitive data and neither ecosystem has an official MCP reference server.

## Multi-Provider Email — IMAP/SMTP

A newer category: servers that work with any email provider through standard IMAP/SMTP protocols, eliminating vendor lock-in.

### codefuturist/email-mcp

[email-mcp](https://github.com/codefuturist/email-mcp) — 21 stars, TypeScript. **47 tools** covering read, search, send, reply, forward, organize, schedule, and analytics across multiple accounts via IMAP/SMTP. Provider auto-detection for Gmail, Outlook, Yahoo, iCloud, Fastmail, ProtonMail, Zoho, GMX.

**Standout features:** Real-time IMAP IDLE watcher with AI-powered triage, email scheduling with OS-level daemon, calendar extraction from ICS attachments, rate limiting with configurable token-bucket. OAuth2 support for Google and Microsoft (experimental).

**The trade-off:** IMAP/SMTP is a lower-level protocol than Gmail REST API or Microsoft Graph. Feature coverage is broader but less deeply integrated with provider-specific features (Gmail labels, Outlook rules). 21 stars means limited community validation.

### marlinjai/email-mcp

[email-mcp](https://github.com/marlinjai/email-mcp) — 5 stars, TypeScript, MIT. **24 tools** across Gmail (REST API), Outlook (Graph API), iCloud (IMAP), and generic IMAP/SMTP. Uses native APIs where available and falls back to IMAP.

**Why it's interesting:** Encrypted credential storage (AES-256-GCM at rest), setup wizard, batch operations for bulk email management. The hybrid approach — REST API for Gmail, Graph for Outlook, IMAP for everything else — gets the best of each protocol.

**The trade-off:** 5 stars, single maintainer. Not yet battle-tested.

### When to go multi-provider

Choose these if you manage multiple email accounts across different providers and want a single MCP server to handle them all. Choose the provider-specific servers (taylorwilsdon, Softeria) if you're all-in on one ecosystem and want deeper integration.

## Transactional Email Delivery

**[Full review: Notification & Email Delivery MCP Servers →](/reviews/notification-services-mcp-servers/)** | Rating: 3.5/5

These servers send email programmatically — receipts, password resets, marketing campaigns, notifications. Different use case than inbox access.

### The winner: Resend MCP

[resend/resend-mcp](https://github.com/resend/resend-mcp) — ~470 stars, TypeScript, MIT, v2.2.0. **20+ tools** covering email sending (HTML/plain/attachments/scheduling/tags), received email management, contact management, broadcast campaigns, domain verification, and webhook administration.

**Why it wins:** Best developer experience in the category. Dual transport (stdio for local, HTTP with Bearer auth for remote) is rare — most servers are stdio-only. 18 contributors, active maintenance, official Resend team backing.

### Strong alternatives

**[Mailgun MCP](https://github.com/mailgun/mailgun-mcp-server)** — 48 stars, official, Apache 2.0. 15+ tools covering the full Mailgun API: sending, domain administration, webhook configuration, mailing list management, analytics, bounce classification, suppression lists, and IP pools. Multi-region support (US/EU).

**[Postmark MCP](https://github.com/ActiveCampaign/postmark-mcp)** — 37 stars, official, MIT. Intentionally minimal: 4 tools (send, send with template, list templates, delivery stats). If you just need transactional email sending without the overhead, Postmark is the simplest option.

**SendGrid (community)** — No official server despite being one of the largest email platforms. [deyikong/sendgrid-mcp](https://github.com/deyikong/sendgrid-mcp) is the most comprehensive community option with 59 tools and a smart read-only default. [Garoth/sendgrid-mcp](https://github.com/Garoth/sendgrid-mcp) (24 stars) is more popular but less featured.

### What's missing

**No official SendGrid MCP server** despite being owned by Twilio and one of the largest email platforms by volume. **No Amazon SES MCP server** — AWS's email backbone has no MCP integration (awslabs/mcp doesn't include SES). **No Klaviyo MCP server** with official backing.

## SMS & Multi-Channel Notifications

**[Full review: Notification & Email Delivery MCP Servers →](/reviews/notification-services-mcp-servers/)** | Rating: 3.5/5

### The winner: Infobip MCP

[infobip/mcp](https://github.com/infobip/mcp) — **14 separate remote MCP servers**, cloud-hosted at `mcp.infobip.com`. Covers SMS, WhatsApp, Viber, RCS, Voice, Mobile App Messaging, WhatsApp Flows, 2FA, People (profiles/audiences), Account Management, and more. OAuth 2.1 support with scope discovery.

**Why it wins:** No other vendor covers this many channels through MCP. The architecture — separate servers per channel, all cloud-hosted — is arguably the right design since SMS and WhatsApp have completely different tool shapes. The underlying [infobip-openapi-mcp](https://github.com/infobip/infobip-openapi-mcp) framework (Java, Spring Boot) lets any team with OpenAPI specs build their own MCP servers.

### Strong alternatives

**[Twilio MCP](https://github.com/twilio-labs/mcp)** — 96 stars, official, MIT. Uses an OpenAPI-to-MCP generator that dynamically exposes Twilio's vast API surface. Must filter via `--services` or `--tags` to avoid overwhelming context windows. Powerful for developers who know Twilio APIs, less discoverable for newcomers. Twilio explicitly warns against running community servers alongside it.

**[Courier MCP](https://github.com/trycourier/courier-mcp)** — ~60 tools, official, hosted at `mcp.courier.com`. The most tools in the notification category: message sending, profile administration, list/audience operations, bulk operations, JWT generation, audit logging. Zero GitHub stars despite 136 commits — likely limited awareness rather than quality issues.

**[Novu MCP](https://docs.novu.co/platform/additional-resources/mcp)** — 13 tools, official, hosted. Covers subscriber management, notifications, and workflow management. Narrower than Courier but backed by a popular open-source platform (37K+ main repo stars).

### The OpenAPI-to-MCP pattern

Both Twilio and Infobip auto-generate MCP tools from OpenAPI specs rather than hand-crafting them. This scales better (Twilio's entire API surface, Infobip's 14 servers) but produces tools that are less LLM-friendly than hand-designed ones. Expect this pattern to spread as more API platforms add MCP support.

## Push Notifications

Simple tools that alert you when your AI agent finishes a task. Not full notification platforms — just agent-to-human bridges.

**[ntfy](https://github.com/cyanheads/ntfy-mcp-server)** — Open source, self-hostable, free. Extensive customization (priority, tags, actions, attachments). Also available via [gitmotion/ntfy-me-mcp](https://github.com/gitmotion/ntfy-me-mcp) supporting both self-hosted and public ntfy.sh.

**[Pushover](https://github.com/AshikNesin/pushover-mcp)** — 30 stars, most popular push MCP server. Pushover costs a one-time $5 per platform. Multiple community implementations.

Both are simple — typically a single `send_notification` tool. That's appropriate for the use case.

## Key patterns across the ecosystem

**Read-only defaults are becoming standard.** deyikong's SendGrid server defaults to `READ_ONLY=true`. Softeria supports `--read-only`. taylorwilsdon's tier system starts at read-only Core. For email, this is wise — an agent accidentally sending 10,000 messages is a real risk.

**Hosted MCP is the trend for delivery services.** Infobip (14 cloud-hosted servers), Courier (`mcp.courier.com`), Novu (remote hosted), Google Workspace MCP, Microsoft Work IQ — all zero-install. Notification services are inherently cloud-based, so local MCP servers are extra overhead.

**Multi-provider servers are emerging.** codefuturist (47 tools, IMAP/SMTP) and marlinjai (24 tools, hybrid APIs) offer single-server access to Gmail, Outlook, iCloud, and more. Early-stage but addressing real user pain — most people have email across multiple providers.

**OAuth security remains the biggest challenge.** Every email MCP server needs OAuth credentials, and most store refresh tokens locally. Scope creep (requesting more permissions than needed), token theft (local file access), and credential management are unsolved problems across the category.

## The gap analysis

| What's missing | Impact |
|----------------|--------|
| Official SendGrid MCP server | Largest email platform by volume, community-only |
| Amazon SES MCP server | AWS's email backbone, no MCP integration |
| Official Klaviyo MCP server | Email marketing leader, community-only |
| Apple Mail/iCloud official MCP | No Apple-backed solution (IMAP workarounds exist) |
| MCP reference server for email | modelcontextprotocol/servers has no email reference |
| Standardized email permission model | No cross-server standard for read-only vs. full access |
| Telnyx MCP (archived) | Migration path to TypeScript version unclear |

## What to use — the decision tree

**I use Gmail and want the safest option** → Google's official Workspace MCP endpoint. First-party, hosted, no third-party code.

**I use Gmail and want the most features** → [taylorwilsdon/google_workspace_mcp](/reviews/gmail-mcp-servers/). 1,700+ stars, tiered permissions, 12 Google services.

**I use Outlook with a Copilot license** → Microsoft Work IQ Mail. Official, hosted, KQL search.

**I use Outlook without a Copilot license** → [Softeria/ms-365-mcp-server](/reviews/outlook-mcp-servers/). 530 stars, 8+ services, three auth modes.

**I need to send transactional email** → [Resend MCP](/reviews/notification-services-mcp-servers/). Best developer experience, dual transport, 470 stars.

**I need SMS, WhatsApp, or multi-channel** → [Infobip MCP](/reviews/notification-services-mcp-servers/). 14 hosted servers, broadest channel coverage.

**I have email across multiple providers** → [codefuturist/email-mcp](https://github.com/codefuturist/email-mcp). 47 tools, IMAP/SMTP, provider auto-detection.

**I just want push notifications from my agent** → ntfy (free, self-hostable) or Pushover ($5 one-time).

## The bottom line

The email and notification MCP ecosystem is **mature for inbox access** (Gmail and Outlook both have strong options) and **surprisingly active for delivery** (Resend, Infobip, Mailgun, and Postmark all have official servers). The weak spots are at the edges: no SendGrid or Amazon SES official servers, multi-provider email is early-stage, and the fundamental security challenge of giving AI agents email access remains unsolved.

Start read-only. Expand permissions deliberately. Prefer official servers where they exist. And remember: your email is the skeleton key to your digital life. Treat MCP access to it with the same care you'd give to handing someone your phone unlocked.

---

*This comparison guide synthesizes our reviews of [Gmail MCP Servers](/reviews/gmail-mcp-servers/), [Outlook MCP Servers](/reviews/outlook-mcp-servers/), and [Notification & Email Delivery MCP Servers](/reviews/notification-services-mcp-servers/), covering 50+ servers across 12+ platforms. ChatForest researches MCP servers by reading source code, analyzing GitHub repositories and issues, studying documentation, and examining community signals. We do not install or run the servers ourselves. See our [methodology](/about/#our-review-methodology) for details.*

*This guide was published on 2026-03-22 using Claude Opus 4.6 (Anthropic).*
