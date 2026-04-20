# Notification & Email Delivery MCP Servers — Twilio, Resend, SendGrid, Mailgun, Postmark, Infobip, Courier, Novu, and Beyond

> Notification and email delivery MCP servers let AI agents send emails, SMS, push notifications, and multi-channel messages through platforms like Twilio, Resend, SendGrid


The notification and email delivery MCP category spans four distinct use cases: **transactional email** (Resend, Mailgun, Postmark, SendGrid), **SMS and telephony** (Twilio, Infobip, Telnyx, Vonage), **multi-channel notification orchestration** (Courier, Novu, Infobip), and **push notifications** (Pushover, ntfy). The ecosystem is surprisingly active — nearly every major platform has shipped or inspired an MCP server.

The headline finding: **Resend ships the best-designed email delivery MCP server** — 470 stars, official, dual stdio+HTTP transport, comprehensive email operations plus contact management and broadcast campaigns. For multi-channel, **Infobip takes the architectural crown** with 14 remote MCP servers covering SMS, WhatsApp, Viber, RCS, Voice, 2FA, and more — all cloud-hosted with OAuth 2.1 support. And **Twilio's official server** takes a unique OpenAPI-generated approach that exposes the entire Twilio API surface, though with usability trade-offs.

## The Landscape

### Resend (Official)

| Server | Stars | Language | Tools | Auth | Transport |
|--------|-------|----------|-------|------|-----------|
| [resend/resend-mcp](https://github.com/resend/resend-mcp) | ~470 | TypeScript | 20+ | API key | stdio, Streamable HTTP |

**Resend's official MCP server is the best transactional email MCP integration.** 470 stars, 66 forks, 86 commits, 18 contributors, MIT license, v2.2.0 (March 2026). The highest-starred email delivery MCP server by a wide margin.

The tool set is comprehensive: **email operations** (send, list, get, cancel, update, batch send with HTML/plain text/attachments/CC/BCC/reply-to/scheduling/tags), **received email management** with attachment downloads, **contact management** with custom properties and segment handling, **broadcast campaign** creation and scheduling, **domain verification** and configuration, **subscription topic and segment management**, and **API key and webhook administration**.

Dual transport is the standout. Stdio mode (`npx -y resend-mcp`) for local development, HTTP mode with Bearer token auth for remote/shared deployments. This flexibility is rare — most email MCP servers are stdio-only.

6 open issues. Active development with 18 contributors. The server supports Claude Desktop, Claude Code, Cursor, and any MCP-compatible client.

Community alternatives exist (PSU3D0/resend-mcp, gui-wf/resend-mcp-server, Hawstein/resend-mcp, pontusab/resend-mcp) but the official server is clearly the one to use — it has 100x the stars and direct Resend team maintenance.

### Twilio (Official)

| Server | Stars | Language | Tools | Auth | Transport |
|--------|-------|----------|-------|------|-----------|
| [twilio-labs/mcp](https://github.com/twilio-labs/mcp) | ~96 | TypeScript | OpenAPI-generated | API Key + Secret | stdio |

**Twilio's official MCP server takes a radically different approach from every other server in this review.** Instead of hand-crafting tools, it uses an OpenAPI-to-MCP generator that dynamically exposes Twilio's vast API surface as MCP tools. The monorepo contains two packages: the MCP server itself and a generic `openapi-mcp-server` that converts any OpenAPI spec into MCP tools.

The catch: because Twilio's API surface is enormous, you must filter which services to load via `--services` or `--tags` parameters. Without filtering, you'd overwhelm any LLM's context window. This makes the server powerful for developers who know which Twilio APIs they need, but less discoverable for newcomers.

96 stars, 35 forks, 101 commits, 3 contributors, MIT license. Install via `npx -y @twilio-alpha/mcp`. Auth requires Account SID, API Key, and API Secret.

10 open issues. The Twilio ETI team specifically warns against running community MCP servers alongside the official one — a notable security stance suggesting they take the threat of tool-poisoning seriously.

Community SMS-focused alternatives: YiyangLi/sms-mcp-server (simple SMS via Twilio), deshartman/twilio-messaging-mcp-server (messaging-focused), deshartman/twilio-agent-payments-mcp-server (PCI-compliant payment flows — unique in the ecosystem).

### SendGrid (Community)

| Server | Stars | Language | Tools | Auth | Transport |
|--------|-------|----------|-------|------|-----------|
| [Garoth/sendgrid-mcp](https://github.com/Garoth/sendgrid-mcp) | ~24 | TypeScript | 15+ | API key | stdio |
| [deyikong/sendgrid-mcp](https://github.com/deyikong/sendgrid-mcp) | ~3 | TypeScript | 59 | API key | stdio |
| [recepyavuz0/sendgrid-mcp-server](https://github.com/recepyavuz0/sendgrid-mcp-server) | — | — | — | API key | stdio |
| [CDataSoftware/sendgrid-mcp-server-by-cdata](https://github.com/CDataSoftware/sendgrid-mcp-server-by-cdata) | — | — | Read-only | JDBC | stdio |

**SendGrid has no official MCP server** despite being one of the largest email platforms (owned by Twilio). The community has filled the gap, but with fragmentation.

**Garoth/sendgrid-mcp** is the most popular (24 stars, 13 forks, 27 commits, MIT). Covers contacts, lists, templates (Handlebars), single sends, email sending, analytics, and verified senders. Uses the Single Sends API rather than legacy transactional endpoints. 2 open issues.

**deyikong/sendgrid-mcp** is the most comprehensive — 59 tools covering marketing automation, campaigns, contacts, dynamic segments, templates, transactional email, suppressions, and 13-month historical analytics. Crucially, it **defaults to read-only mode** (`READ_ONLY=true`), registering all tools but blocking mutations with error messages. This is a smart safety pattern for email — you really don't want an AI agent accidentally blasting your entire contact list.

Twilio/SendGrid's own blog published a guide on building a SendGrid MCP server, suggesting they see the use case but haven't prioritized an official server.

### Mailgun (Official)

| Server | Stars | Language | Tools | Auth | Transport |
|--------|-------|----------|-------|------|-----------|
| [mailgun/mailgun-mcp-server](https://github.com/mailgun/mailgun-mcp-server) | ~48 | JavaScript | 15+ | API key | stdio |

**Mailgun ships an official MCP server with solid coverage.** 48 stars, 19 forks, 11 commits, Apache 2.0. Install via `npx -y @mailgun/mcp-server`.

Tools cover the full Mailgun API: email sending, stored message retrieval, domain administration and DNS verification, webhook configuration, mailing list management, email template versioning, analytics querying, delivery metrics, bounce classification, suppression list management, and IP pool configuration.

Multi-region support (US/EU via `MAILGUN_API_REGION`). API keys are isolated from AI models — the server enforces HTTPS/TLS for all Mailgun communications and validates parameters against OpenAPI specs.

2 open issues, 3 active PRs. The server also has a sibling: [mailgun/mailjet-mcp-server](https://github.com/mailgun/mailjet-mcp-server) for Mailjet's API (same parent company, Sinch).

### Postmark (Official)

| Server | Stars | Language | Tools | Auth | Transport |
|--------|-------|----------|-------|------|-----------|
| [ActiveCampaign/postmark-mcp](https://github.com/ActiveCampaign/postmark-mcp) | ~37 | JavaScript | 4 | Server token | stdio |

**Postmark's official MCP server is intentionally minimal.** 37 stars, 11 forks, 22 commits, 3 contributors, MIT. Built by Postmark Labs (ActiveCampaign).

Just 4 tools: `sendEmail`, `sendEmailWithTemplate`, `listTemplates`, `getDeliveryStats`. That's it. No contact management, no domain configuration, no webhook setup. The philosophy is clear — Postmark positions itself as the transactional email specialist, and the MCP server reflects that focus.

Automatic open and link tracking. Environment variable configuration (server token, default sender, message stream). 0 open issues, 2 pending PRs. The self-described "experimental" status is honest.

For teams that just need to send transactional emails from an AI agent and check delivery stats, Postmark's server is the simplest option in this review.

### Infobip (Official)

| Server | Stars | Language | Tools | Auth | Transport |
|--------|-------|----------|-------|------|-----------|
| [infobip/mcp](https://github.com/infobip/mcp) | ~25 | Documentation | 14 remote servers | API key, OAuth 2.1 | HTTPS, SSE |

**Infobip takes the most ambitious architectural approach in this category.** Instead of one MCP server, they ship **14 separate remote MCP servers**, each covering a different communication channel or capability:

- **Messaging:** SMS, WhatsApp, Viber, RCS, Voice, Mobile App Messaging
- **Advanced:** WhatsApp Flows, 2FA (SMS/Email/Voice delivery)
- **Customer data:** People (profiles, companies, audiences), Account Management
- **Platform:** CPaaSX Applications/Entities, CAMARA verification
- **Meta:** Documentation Search, Deep Research

All servers are cloud-hosted at `mcp.infobip.com/{service}` — no local installation required. Authentication supports both API key (`App ${INFOBIP_API_KEY}` header) and OAuth 2.1 with scope discovery via `.well-known/oauth-authorization-server`. Transport options include HTTPS (direct), SSE (`/sse` suffix), and stdio bridge via `mcp-remote`.

The open-source framework powering these servers is [infobip/infobip-openapi-mcp](https://github.com/infobip/infobip-openapi-mcp) (24 stars, Java, Spring AI/Spring Boot) — a generic OpenAPI-to-MCP converter with auto schema transformation, mock mode, live reload, OAuth with auto scope discovery, and automatic JSON error correction. Any team with OpenAPI specs can use this to build their own MCP servers.

25 stars on the documentation repo, 52 commits. The breadth is unmatched — no other vendor in this review covers SMS, WhatsApp, Viber, RCS, Voice, and 2FA through MCP.

### Courier (Official)

| Server | Stars | Language | Tools | Auth | Transport |
|--------|-------|----------|-------|------|-----------|
| [trycourier/courier-mcp](https://github.com/trycourier/courier-mcp) | ~0 | TypeScript | ~60 | API key | HTTP |

**Courier's MCP server has the most tools in this review — roughly 60** — but zero GitHub stars despite 136 commits from 2 contributors. This disconnect suggests either very recent release or limited community awareness.

Tools cover: message sending (direct, templated, list-based), message management (list, retrieve, inspect content, history, cancel), profile administration (create, merge, replace, delete, subscription management), list and audience operations, brand configuration, JWT generation, push token management, automation invocation, bulk operations, audit logging, and tenant administration.

Both hosted (`mcp.courier.com` — zero setup) and self-hosted (clone + `dev.sh`). v1.3.0 (March 2026), 0 open issues.

Courier's value proposition is multi-channel orchestration — email, SMS, push, Slack, Teams through a single API. The MCP server inherits this, making it the most channel-flexible option for teams already using Courier.

### Novu (Official)

| Server | Stars | Language | Tools | Auth | Transport |
|--------|-------|----------|-------|------|-----------|
| [Novu MCP](https://docs.novu.co/platform/additional-resources/mcp) | ~2–4 | TypeScript | 13 | API key | HTTP |

**Novu's MCP server covers the notification infrastructure basics.** Novu itself is a popular open-source notification platform (37K+ stars on the main repo). The MCP server provides 13 tools: subscriber management (create, get, update, delete), notification operations (list, stats, cancel), workflow management (list, trigger, create), plus environment listing and API key status checks.

Remote hosted server available. The tool set is narrower than Courier's (~60 tools) but covers the core notification workflow. Low GitHub stars on the MCP server specifically, despite Novu's strong main repo.

### Telnyx (Official — Archived)

| Server | Stars | Language | Tools | Auth | Transport |
|--------|-------|----------|-------|------|-----------|
| [team-telnyx/telnyx-mcp-server](https://github.com/team-telnyx/telnyx-mcp-server) | ~24 | Python | 20+ | API key | stdio |

**Telnyx shipped an official MCP server, then archived it.** 24 stars, 5 forks, 6 commits. The repository was archived September 29, 2025 — read-only, no longer maintained. Users are directed to migrate to an official TypeScript version in the telnyx-node repository.

When active, the server covered: AI assistant management (create, list, update, delete), call control (outbound calls, hangup, transfer, audio playback, DTMF, TTS), SMS/MMS messaging, phone number management (list, purchase, configure), voice connections, cloud storage, and webhook support via ngrok.

The archival is notable — Telnyx invested in MCP, built a working server, then deprecated it. The migration to TypeScript suggests a strategic shift rather than abandonment of MCP.

### Vonage (Community)

| Server | Stars | Language | Tools | Auth | Transport |
|--------|-------|----------|-------|------|-----------|
| [Vonage-Community/telephony-mcp-server](https://github.com/Vonage-Community/telephony-mcp-server) | ~1 | Python | 4 | API key + app ID | HTTP |
| [Vonage-Community/vonage-mcp-server-api-bindings](https://github.com/Vonage-Community/vonage-mcp-server-api-bindings) | — | — | — | API credentials | — |

**Vonage's MCP presence is minimal.** The telephony MCP server has 1 star, 3 commits, and covers only voice calls, SMS, speech-to-text, and speech recognition. A separate API bindings server exists with WhatsApp messaging and SMS failover. Neither has significant adoption.

Vonage also has a [documentation MCP server](https://github.com/Vonage/vonage-mcp-server-documentation) for bridging developer docs to LLMs — useful for developers building on Vonage, but not for sending messages.

### Push Notification Servers

| Server | Stars | Language | Tools | Auth | Transport |
|--------|-------|----------|-------|------|-----------|
| [AshikNesin/pushover-mcp](https://github.com/AshikNesin/pushover-mcp) | ~30 | TypeScript | 1 | API token | stdio |
| [cyanheads/ntfy-mcp-server](https://github.com/cyanheads/ntfy-mcp-server) | — | TypeScript | 1 | Optional token | stdio |
| [gitmotion/ntfy-me-mcp](https://github.com/gitmotion/ntfy-me-mcp) | — | TypeScript | 1+ | Optional token | stdio |

**Push notification MCP servers solve a specific problem: alerting you when your AI agent finishes a task.** These aren't full notification platforms — they're agent-to-human notification bridges.

**Pushover** has the most implementations (5+ community servers). AshikNesin/pushover-mcp (30 stars) is the most popular. Pushover itself costs a one-time $5 per platform.

**ntfy** is the open-source alternative. cyanheads/ntfy-mcp-server offers extensive customization (priority, tags, actions, attachments). gitmotion/ntfy-me-mcp supports both self-hosted and ntfy.sh public instances. ntfy is completely free for self-hosted.

Both Pushover and ntfy servers are simple — typically a single `send_notification` tool. That's appropriate. These aren't email platforms; they're push buttons.

## Key Patterns

**Email delivery is the most mature subcategory.** Resend, Mailgun, and Postmark all have official servers. SendGrid is the notable gap — community-only despite being owned by Twilio. The clear trend: developer-focused email platforms (Resend, Postmark) ship MCP servers faster than enterprise platforms.

**Infobip's multi-server architecture is unique.** Every other vendor in this review ships one MCP server. Infobip ships 14 separate servers, one per channel. This is arguably the right design — SMS and WhatsApp have completely different tool shapes — but it means clients need multiple server configurations.

**Read-only defaults are becoming standard.** deyikong's SendGrid server defaults to `READ_ONLY=true`. Postmark's server is read-focused (4 tools, mostly querying). This is wise for notification services — an AI agent accidentally sending 10,000 emails is a real risk.

**The OpenAPI-to-MCP pattern is spreading.** Both Twilio and Infobip use auto-generation from OpenAPI specs rather than hand-crafting tools. This scales better (Twilio's entire API surface, Infobip's 14 servers) but produces tools that are less LLM-friendly than hand-designed ones.

**Hosted MCP is the future for notification services.** Infobip (cloud-hosted, 14 servers), Courier (hosted at mcp.courier.com), and Novu (remote hosted) all offer zero-install deployments. This makes sense — notification services are inherently cloud-based, so why run a local MCP server?

## What's Missing

- **No official SendGrid MCP server.** The largest email delivery platform by volume has only community implementations.
- **No Amazon SES MCP server.** AWS's email service — the backbone of much of the internet's transactional email — has no MCP integration (awslabs/mcp doesn't include SES).
- **No official Vonage MCP server** with significant adoption. The community server has 1 star.
- **No Klaviyo MCP server** with official backing — only community implementations (mattcoatsworth/Klaviyo-MCP-Server) for the email marketing giant.
- **No Plivo MCP server** with meaningful adoption.
- **Telnyx archived their server** — migration path to TypeScript version unclear.

## The Verdict

The notification & email delivery MCP category is **active and broadening fast**, with 20+ servers across 12 platforms covering email, SMS, multi-channel notifications, and push alerts. The ecosystem splits into clear tiers:

**Top tier:** Resend (best developer experience, dual transport, 470 stars), Infobip (broadest channel coverage, 14 hosted servers, OAuth 2.1), Mailgun (official, solid coverage, Apache 2.0).

**Mid tier:** Twilio (powerful but requires API filtering knowledge), Courier (~60 tools, hosted, but zero community adoption), SendGrid (community-only, deyikong's 59-tool server with read-only defaults is impressive), Postmark (intentionally minimal, good for simple transactional email).

**Early/niche:** Novu (13 tools, notification-focused), Telnyx (archived), Vonage (minimal), push notification servers (Pushover, ntfy — simple and effective for their use case).

The gap compared to more mature MCP categories is the absence of SendGrid and Amazon SES official servers. When those arrive, this category will be significantly stronger.

**Rating: 3.5/5** — Resend's official server is excellent, Infobip's multi-channel hosted architecture is innovative, and Mailgun/Postmark provide solid official options. But the lack of official SendGrid and Amazon SES servers, Telnyx's archival, and Vonage's minimal presence leave notable holes in the landscape.

---

*Last updated: March 15, 2026. Have we missed a notification MCP server? Let us know — we research new servers regularly.*

*This review was last edited on 2026-03-16 using Claude Opus 4.6 (Anthropic).*

