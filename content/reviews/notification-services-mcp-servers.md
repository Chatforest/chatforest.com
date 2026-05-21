---
title: "Notification & Email Delivery MCP Servers — Twilio, Resend, SendGrid, Mailgun, Postmark, Infobip, Courier, Novu, and Beyond"
date: 2026-03-15T03:28:00+09:00
description: "Notification and email delivery MCP servers let AI agents send emails, SMS, push notifications, and multi-channel messages through platforms like Twilio, Resend, SendGrid"
og_description: "Notification & email delivery MCP servers: Resend (512 stars, official, v2.6.0), Twilio (Public Beta May 7 — 1,800+ endpoints, natural language discovery), Mailgun (official, Forwards API May 12), Infobip (14+ remote servers + AgentOS), NEW Klaviyo official MCP (Anthropic partnership, 200K brands), Vonage (2 official servers — Documentation + Tooling), Fastmail, AgentMail, NEW PowerDMARC, NEW Adobe Marketo Engage. 30+ servers across 18+ platforms. Rating: 4.0→4.5/5."
content_type: "Review"
card_description: "Notification and email delivery MCP servers across Twilio, Resend, SendGrid, Mailgun, Postmark, Infobip, Courier, Novu, Telnyx, Pushover, and ntfy. Resend has the best developer experience. Infobip has the broadest channel coverage. Courier offers the most tools."
last_refreshed: 2026-05-21
category_url: "/categories/email-notification-services/"
---

The notification and email delivery MCP category spans four distinct use cases: **transactional email** (Resend, Mailgun, Postmark, SendGrid), **SMS and telephony** (Twilio, Infobip, Telnyx, Vonage), **multi-channel notification orchestration** (Courier, Novu, Infobip, Klaviyo), and **push notifications** (Pushover, ntfy). The ecosystem has continued maturing through May 2026, with several major platform upgrades closing gaps identified in our April review.

The headline finding: **Resend ships the best-designed email delivery MCP server** — 512 stars, official, dual stdio+HTTP transport, v2.6.0 with comprehensive email operations plus contact management and broadcast campaigns. For multi-channel, **Infobip takes the architectural crown** with 14+ remote MCP servers covering SMS, WhatsApp, Viber, RCS, Email, Voice, 2FA, and more — all cloud-hosted with OAuth 2.1 support, backed by the AgentOS platform. **Twilio's MCP has made a dramatic comeback**: after stagnating at v0.0.3 for over a year, Twilio launched a **Public Beta on May 7, 2026** with natural language API discovery across 1,800+ endpoints and 30+ products — now one of the most capable telephony MCPs in existence. And **Klaviyo** closes the biggest gap from our last review: their official MCP server (in partnership with Anthropic) brings email marketing automation to 200,000+ e-commerce brands.

## The Landscape

### Resend (Official)

| Server | Stars | Language | Tools | Auth | Transport |
|--------|-------|----------|-------|------|-----------|
| [resend/resend-mcp](https://github.com/resend/resend-mcp) | ~512 | TypeScript | 20+ | API key | stdio, Streamable HTTP |

**Resend's official MCP server is the best transactional email MCP integration.** 512 stars (+2%), 73 forks, MIT license, v2.6.0 (April 2026). The highest-starred email delivery MCP server by a wide margin. Steady growth reflects a stable, well-maintained server with no major new releases in May — the v2.6.0 feature set (10 tool groups covering the full Resend API) is comprehensive and holding.

The tool set is comprehensive: **email operations** (send, list, get, cancel, update, batch send with HTML/plain text/attachments/CC/BCC/reply-to/scheduling/tags), **received email management** with attachment downloads, **contact management** with custom properties and segment handling, **broadcast campaign** creation and scheduling, **domain verification** and configuration, **subscription topic and segment management**, and **API key and webhook administration**.

Dual transport is the standout. Stdio mode (`npx -y resend-mcp`) for local development, HTTP mode with Bearer token auth for remote/shared deployments. This flexibility is rare — most email MCP servers are stdio-only.

8 open issues. Active development. The server supports Claude Desktop, Claude Code, Cursor, and any MCP-compatible client.

Community alternatives exist (PSU3D0/resend-mcp, gui-wf/resend-mcp-server, Hawstein/resend-mcp, pontusab/resend-mcp) but the official server is clearly the one to use — it has 100x the stars and direct Resend team maintenance.

### Twilio (Official)

| Server | Stars | Language | Tools | Auth | Transport |
|--------|-------|----------|-------|------|-----------|
| [twilio-labs/mcp](https://github.com/twilio-labs/mcp) | ~104 | TypeScript | 1,800+ endpoints | API Key + Secret | stdio |

**Twilio's MCP server went from the most stagnant to one of the most capable in this category.** On **May 7, 2026**, Twilio launched a **Public Beta** that dramatically expands the server's scope: access to **1,800+ endpoints across 30+ Twilio products** — SMS, Voice, Messaging, WhatsApp, Email, Verify, Video, Conversations, Flex, and more — all through a single MCP server.

The key new tools: **`twilio__search`** (natural language API discovery — describe what you want to do and it finds the right Twilio API) and **`twilio__retrieve`** (full operation specifications including schema and examples). This is a major UX improvement over the previous approach of manually specifying `--services` or `--tags` filters. Discoverability was the core weakness of the old server; the search tool addresses it directly.

Available via Claude Code plugin (search "twilio-developer-kit"), `npx -y @twilio-alpha/mcp`, or as a remote server. Auth requires Account SID, API Key, and API Secret. MIT license.

104 stars, 37 forks, MIT license. The Twilio ETI team still warns against running community MCP servers alongside the official one — a security stance against tool-poisoning.

Community SMS-focused alternatives remain: YiyangLi/sms-mcp-server, deshartman/twilio-messaging-mcp-server, deshartman/twilio-agent-payments-mcp-server (PCI-compliant payment flows — unique in the ecosystem).

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
| [mailgun/mailgun-mcp-server](https://github.com/mailgun/mailgun-mcp-server) | ~54 | TypeScript | 15+ | API key | stdio |

**Mailgun ships an official MCP server with solid coverage.** ~54 stars, 22 forks, Apache 2.0, **v2.0.0** (April 22, 2026), updated May 9, 2026. Install via `npx -y @mailgun/mcp-server`.

Tools cover the full Mailgun API: email sending, stored message retrieval, domain administration and DNS verification, webhook configuration, mailing list management, email template versioning, analytics querying, delivery metrics, bounce classification, suppression list management, and IP pool configuration.

**Platform updates in May 2026**: Mailgun added a **Forwards API** (May 12) for inbound email forwarding with wildcard patterns — enabling "forward all mail to `*@yourdomain.com` to a single handler" routing logic. Inbound routes now include **authentication results** in the payload (May 8) — DKIM, SPF, and DMARC pass/fail data arrives with every inbound message. These are infrastructure-level improvements that complement the MCP server's capabilities.

Multi-region support (US/EU via `MAILGUN_API_REGION`). API keys are isolated from AI models — the server enforces HTTPS/TLS for all Mailgun communications and validates parameters against OpenAPI specs. The server also has a sibling: [mailgun/mailjet-mcp-server](https://github.com/mailgun/mailjet-mcp-server) for Mailjet's API (same parent company, Sinch).

### Postmark (Official)

| Server | Stars | Language | Tools | Auth | Transport |
|--------|-------|----------|-------|------|-----------|
| [ActiveCampaign/postmark-mcp](https://github.com/ActiveCampaign/postmark-mcp) | ~41 | JavaScript | 4 | Server token | stdio |

**Postmark's official MCP server is intentionally minimal.** 41 stars (+11%), 13 forks, 22 commits, MIT. Built by Postmark Labs (ActiveCampaign). **Security note:** a malicious copycat was uploaded to npm under the same package name — only use the official version from GitHub, not npm.

Just 4 tools: `sendEmail`, `sendEmailWithTemplate`, `listTemplates`, `getDeliveryStats`. That's it. No contact management, no domain configuration, no webhook setup. The philosophy is clear — Postmark positions itself as the transactional email specialist, and the MCP server reflects that focus.

Automatic open and link tracking. Environment variable configuration (server token, default sender, message stream). 0 open issues, 2 pending PRs. The self-described "experimental" status is honest.

For teams that just need to send transactional emails from an AI agent and check delivery stats, Postmark's server is the simplest option in this review.

### Infobip (Official)

| Server | Stars | Language | Tools | Auth | Transport |
|--------|-------|----------|-------|------|-----------|
| [infobip/mcp](https://github.com/infobip/mcp) | ~29 | Documentation | 14+ remote servers | API key, OAuth 2.1 | HTTPS, SSE |

**Infobip takes the most ambitious architectural approach in this category.** Instead of one MCP server, they ship **14+ separate remote MCP servers**, each covering a different communication channel or capability:

- **Messaging:** SMS, WhatsApp, Viber, RCS, Email, Voice, Mobile App Messaging
- **Advanced:** WhatsApp Flows, 2FA (SMS/Email/Voice delivery)
- **Customer data:** People (profiles, companies, audiences), Account Management
- **Platform:** CPaaSX Applications/Entities, CAMARA verification
- **Meta:** Documentation Search, Deep Research

All servers are cloud-hosted at `mcp.infobip.com/{service}` — no local installation required. Authentication supports both API key (`App ${INFOBIP_API_KEY}` header) and OAuth 2.1 with scope discovery via `.well-known/oauth-authorization-server`. Transport options include HTTPS (direct), SSE (`/sse` suffix), and stdio bridge via `mcp-remote`.

**Major development: Infobip launched AgentOS on April 1, 2026** — a fully managed AI-native platform that orchestrates autonomous, goal-driven customer journeys across 15+ channels. AgentOS integrates MCP servers as the communication layer for AI agents, enabling businesses to move from campaigns and workflows to autonomous interactions. This positions Infobip's MCP servers not just as standalone tools, but as the communication backbone for a complete agentic platform. Human-in-the-loop design ensures AI handles scale while specialists handle complex cases.

The open-source framework powering these servers is [infobip/infobip-openapi-mcp](https://github.com/infobip/infobip-openapi-mcp) (28 stars, Java, Spring AI/Spring Boot 3.5.x, Java 21+, v0.1.13) — a generic OpenAPI-to-MCP converter with auto schema transformation, mock mode, live reload, OAuth with auto scope discovery, automatic JSON error correction, and tool annotations (readOnly, destructive, idempotent). 99 commits. Any team with OpenAPI specs can use this to build their own MCP servers.

29 stars (+16%) on the documentation repo, 73 commits (+40%). The breadth is unmatched — no other vendor in this review covers SMS, WhatsApp, Email, Viber, RCS, Voice, and 2FA through MCP.

### Courier (Official)

| Server | Stars | Language | Tools | Auth | Transport |
|--------|-------|----------|-------|------|-----------|
| [trycourier/courier-mcp](https://github.com/trycourier/courier-mcp) | ~1 | TypeScript | ~60 | API key | HTTP |

**Courier's MCP server has the most tools in this review — roughly 60** — but only 1 GitHub star despite 180 commits. This disconnect suggests limited community awareness despite very active internal development (44 new commits since March).

Tools cover: message sending (direct, templated, list-based), message management (list, retrieve, inspect content, history, cancel), profile administration (create, merge, replace, delete, subscription management), list and audience operations, brand configuration, JWT generation, push token management, automation invocation, bulk operations, audit logging, and tenant administration.

Both hosted (`mcp.courier.com` — zero setup) and self-hosted (clone + `dev.sh`). v1.3.0 (March 2026), 0 open issues.

Courier's value proposition is multi-channel orchestration — email, SMS, push, Slack, Teams through a single API. The MCP server inherits this, making it the most channel-flexible option for teams already using Courier.

### Novu (Official)

| Server | Stars | Language | Tools | Auth | Transport |
|--------|-------|----------|-------|------|-----------|
| [Novu MCP](https://docs.novu.co/platform/additional-resources/mcp) | ~2–4 | TypeScript | 13 | API key | HTTP |

**Novu's MCP server covers the notification infrastructure basics.** Novu itself is a popular open-source notification platform (37K+ stars on the main repo). The MCP server provides 13 tools: subscriber management (create, get, update, delete), notification operations (list, stats, cancel), workflow management (list, trigger, create), plus environment listing and API key status checks.

Remote hosted server available. The tool set is narrower than Courier's (~60 tools) but covers the core notification workflow. Low GitHub stars on the MCP server specifically, despite Novu's strong main repo.

### Telnyx (Official — Major Upgrade)

| Server | Stars | Language | Tools | Auth | Transport |
|--------|-------|----------|-------|------|-----------|
| [team-telnyx/ai](https://github.com/team-telnyx/ai) | ~167 | TypeScript | 228 Agent Skills | API key | stdio, Remote HTTP |
| [team-telnyx/telnyx-mcp-server](https://github.com/team-telnyx/telnyx-mcp-server) | ~24 | Python | 20+ | API key | stdio (archived) |

**Telnyx has made a major comeback.** The archived Python server (24 stars, September 2025) has been fully replaced by the **team-telnyx/ai monorepo** — 167 stars, 230 commits, 7 forks. This is now the "official one-stop shop for AI Agents and developers building with Telnyx."

The new setup includes: a **remote MCP server** at `api.telnyx.com/v2/mcp` (zero local installation), a local `@telnyx/mcp` package via npx, **228 Agent Skills** covering telephony, messaging, AI assistants, and more. The monorepo also ships Python and TypeScript agent toolkits integrating with OpenAI Agent SDK, LangChain, CrewAI, and Vercel AI SDK, plus plugins for Claude Code and Gemini CLI.

This is one of the most comprehensive transformations in the review — from an archived 6-commit Python script to a 230-commit enterprise-grade AI platform with remote MCP, agent toolkits, and deep framework integrations.

### Vonage (Official — Major Upgrade)

| Server | Stars | Language | Tools | Auth | Transport |
|--------|-------|----------|-------|------|-----------|
| Vonage Documentation MCP | — | Hosted | Documentation Q&A | API key | Remote |
| Vonage MCP Tooling Server | — | Hosted | SMS, Voice, WhatsApp, balance | API credentials | Remote |

**Vonage has gone from minimal to enterprise-ready with two official servers in early 2026.** Both are discoverable on the **Postman API Network** (reaching 40M+ Postman users) and integrate with Claude, Cursor, VS Code Copilot, and Antigravity.

**Vonage Documentation MCP Server**: Query Vonage's official API documentation inline — ask about SDK usage, error codes, or integration patterns and get context-aware answers without leaving your AI client. Purpose-built for the 1.8M registered Vonage developers.

**Vonage MCP Tooling Server**: Execute real Vonage actions via MCP — SMS sending, voice calls, WhatsApp messaging, and account balance checks. This server moves Vonage from documentation-only to actionable channel coverage, directly competing with Twilio and Telnyx.

This is a meaningful reversal from our last review, where Vonage's community-only telephony server had 1 star and 3 commits. Vonage now has production-grade official infrastructure for both developer assistance and communication actions.

### Klaviyo (Official — NEW)

| Server | Stars | Language | Tools | Auth | Transport |
|--------|-------|----------|-------|------|-----------|
| [Klaviyo MCP](https://developers.klaviyo.com/en/docs/klaviyo_mcp_server) | — | Hosted | 15+ | OAuth / API key | Remote |

**Klaviyo's official MCP server closes the biggest gap from our April review** — where we flagged the absence of any official Klaviyo integration as a notable weakness. Built in partnership with Anthropic, Klaviyo's MCP brings email marketing automation to **200,000+ e-commerce brands** using the platform.

Tools cover: **campaigns** (create, draft, schedule, deploy), **flows** (automation sequences), **profiles** (subscriber data), **lists and segments**, **events** (track customer actions), **metrics** (performance analytics), **templates** (email designs). Auth via OAuth or private API key.

The practical workflow Klaviyo describes: Plan → Draft (AI writes subject lines and email copy via MCP) → Review (human approval step) → Deploy (AI executes send via MCP). This compresses a typical 1–2 day campaign production cycle to **3–4 hours**. For e-commerce brands running frequent promotions, the throughput gain is significant.

This shifts Klaviyo from "missing" to competitive with Courier and Novu for multi-channel notification orchestration use cases — but with a focused advantage in email marketing specifically.

### Adobe Marketo Engage (Official — NEW)

| Server | Stars | Language | Tools | Auth | Transport |
|--------|-------|----------|-------|------|-----------|
| Adobe Marketo Engage MCP | — | Hosted | 100+ | OAuth | Remote |

**Adobe launched an official Marketo Engage MCP server in April 2026** with 100+ operations covering email programs, lead management, forms, custom objects, and campaign execution. This is the first enterprise marketing automation platform with an official MCP server at scale — Marketo Engage powers some of the world's largest B2B marketing operations.

The tool surface is broad: lead database management, smart list operations, email asset management, program creation and scheduling, form submissions, and activity logging. For B2B marketing teams already on Marketo, the MCP unlocks AI-assisted campaign planning and execution without API scripting.

### Fastmail (Official — NEW)

| Server | Stars | Language | Tools | Auth | Transport |
|--------|-------|----------|-------|------|-----------|
| [Fastmail MCP](https://www.fastmail.com/blog/an-mcp-server-for-fastmail/) | — | Hosted | 6+ | OAuth (3 levels) | Remote HTTP |

**Fastmail launched an official MCP server on April 22, 2026 (National Email Day).** Available at `api.fastmail.com/mcp`, this is the first privacy-focused email provider with an official MCP integration. No local installation needed — any MCP-compatible client (Claude, ChatGPT, Cursor) connects directly.

Tools include: **email operations** (get recent emails, get specific email, send email, search emails), **contacts** (list contacts), and **calendar** (create events with participants, locations, and ISO 8601 times). OAuth consent screen offers three access levels: read-only, write (update emails, save drafts, edit contacts/events), and send (send emails).

This is a fundamentally different use case from Resend or SendGrid — Fastmail's MCP connects agents to a user's personal email, calendar, and contacts rather than providing transactional email delivery infrastructure. Think "email client for AI" rather than "email API for AI."

Community alternatives exist (MadLlama25/fastmail-mcp, gr3enarr0w/fastmail-mcp-server, others) but the official hosted server at api.fastmail.com/mcp is clearly the one to use.

### AgentMail (Official — NEW)

| Server | Stars | Language | Tools | Auth | Transport |
|--------|-------|----------|-------|------|-----------|
| [AgentMail MCP](https://docs.agentmail.to/integrations/mcp) | — | Hosted | Multiple | API key | MCP |

**AgentMail represents a new paradigm: email infrastructure designed for AI agents, not humans.** Y Combinator Summer 2025 batch, $6M seed round (March 2026) led by General Catalyst with investors including Paul Graham, Dharmesh Shah (HubSpot CTO), Paul Copplestone (Supabase CEO), and Karim Atiyeh (Ramp CTO).

Instead of connecting AI agents to existing human email accounts (like Fastmail's MCP or Gmail integrations), AgentMail gives agents their own email inboxes. Agents can create, send, receive, and manage email threads entirely via API. One customer provisions 25,000 inboxes and processes millions of emails through AgentMail.

The MCP server allows MCP-compatible clients to interact with AgentMail's API. Integrations with LangChain, LlamaIndex, CrewAI, LiveKit, and Google ADK. This is the first agent-native email infrastructure with MCP support in this review.

### AWS SES (Sample — NEW)

| Server | Stars | Language | Tools | Auth | Transport |
|--------|-------|----------|-------|------|-----------|
| [aws-samples/sample-for-amazon-ses-mcp](https://github.com/aws-samples/sample-for-amazon-ses-mcp) | ~7 | Java (Smithy) | All SES v2 API | AWS credentials | stdio |

**AWS has published a sample MCP server for Amazon SES**, filling one of the biggest gaps from our March review. 7 stars, 3 forks, 4 commits, MIT-0 license. The server exposes all public SES v2 API actions — email sending (single/batch, template-based), contact list management, suppression lists, dedicated IP pools, deliverability metrics, and verified senders.

**Important caveat:** this is explicitly a sample, not an official production-grade server. The README states it's "not intended to be used in a production environment" and lives under `aws-samples` rather than `awslabs`. Built on the Smithy Java project (still in development). For production SES needs, developers should evaluate this sample as a starting point, not a finished product.

Still, its existence is significant — Amazon SES backs a massive share of the internet's transactional email, and having any MCP path, even a sample, is a step forward.

### PowerDMARC (Official — NEW)

| Server | Stars | Language | Tools | Auth | Transport |
|--------|-------|----------|-------|------|-----------|
| [PowerDMARC MCP](https://powerdmarc.com/) | — | Hosted | 10+ | API key | Remote |

**PowerDMARC launched an official MCP server on May 11, 2026** — the first email authentication and domain security service with MCP support. The server exposes: live domain portfolio audits, email authentication health scores (DMARC/DKIM/SPF), spoofing detection alerts, DNS/WHOIS lookups, and deliverability diagnostics.

This is a niche but important entrant. Email delivery failures due to misconfigured DMARC records are one of the most common causes of transactional email problems. An MCP server that lets AI agents audit and diagnose authentication issues in context — without switching to a separate dashboard — fills a real operational gap for email platform teams. Integrates with Claude, Cursor, and other major AI clients.

### Push Notification Servers

| Server | Stars | Language | Tools | Auth | Transport |
|--------|-------|----------|-------|------|-----------|
| [AshikNesin/pushover-mcp](https://github.com/AshikNesin/pushover-mcp) | ~30 | TypeScript | 1 | API token | stdio |
| [cyanheads/ntfy-mcp-server](https://github.com/cyanheads/ntfy-mcp-server) | — | TypeScript | 1 | Optional token | stdio |
| [gitmotion/ntfy-me-mcp](https://github.com/gitmotion/ntfy-me-mcp) | — | TypeScript | 1+ | Optional token | stdio |

**Push notification MCP servers solve a specific problem: alerting you when your AI agent finishes a task.** These aren't full notification platforms — they're agent-to-human notification bridges.

**Pushover** has the most implementations (5+ community servers). AshikNesin/pushover-mcp (30 stars) is the most popular. Pushover itself costs a one-time $5 per platform.

**ntfy** is the open-source alternative. cyanheads/ntfy-mcp-server (8 stars) offers extensive customization (priority, tags, actions, attachments). gitmotion/ntfy-me-mcp (24 stars) supports both self-hosted and ntfy.sh public instances and is now the most popular ntfy MCP implementation. ntfy is completely free for self-hosted.

Both Pushover and ntfy servers are simple — typically a single `send_notification` tool. That's appropriate. These aren't email platforms; they're push buttons.

## Key Patterns

**Email delivery is the most mature subcategory.** Resend, Mailgun, and Postmark all have official servers. SendGrid remains the notable gap — still community-only despite being owned by Twilio. The clear trend: developer-focused email platforms (Resend, Postmark) ship MCP servers faster than enterprise platforms.

**The email MCP spectrum is widening.** This category now spans five distinct use cases: transactional delivery (Resend, Mailgun, SendGrid), personal email access (Fastmail), agent-native email (AgentMail), email marketing automation (Klaviyo, Marketo Engage), and email security/authentication (PowerDMARC). Each use case has distinct tooling needs, and all five now have MCP coverage.

**Stagnant servers can revive.** Twilio's MCP sat at v0.0.3 for 14 months — the clearest stagnation signal in the category. Its May 7 Public Beta launch with 1,800+ endpoints and natural language discovery rewrites that story entirely. Similarly, Vonage moved from a 1-star community server to two official enterprise-ready servers in early 2026. Don't write off a major platform just because it was slow to ship.

**Infobip's multi-server architecture is unique — and now part of a platform.** Every other vendor ships one MCP server. Infobip ships 14+ separate servers, one per channel, and with AgentOS they've wrapped these in a fully managed AI agent platform. MCP as infrastructure layer, not standalone tools.

**Read-only defaults and security awareness are growing.** deyikong's SendGrid server defaults to `READ_ONLY=true`. Postmark's npm package name was hijacked by a malicious copycat — a concrete example of the MCP supply chain risks that the OWASP MCP Top 10 warns about. Infobip's framework now includes tool annotations (readOnly, destructive, idempotent) for safety.

**The OpenAPI-to-MCP pattern is spreading.** Both Twilio and Infobip use auto-generation from OpenAPI specs rather than hand-crafting tools. This scales better (Twilio's 1,800+ endpoint surface, Infobip's 14+ servers) but produces tools that are less LLM-friendly than hand-designed ones. Twilio's new natural language search tool partially compensates for this.

**Hosted/remote MCP is becoming dominant.** Infobip (cloud-hosted, 14+ servers), Courier (mcp.courier.com), Novu (remote), Fastmail (api.fastmail.com/mcp), Telnyx (api.telnyx.com/v2/mcp), Klaviyo, Marketo Engage, and AgentMail all offer zero-install remote deployments. The trend is clear — notification services are inherently cloud-based, and their MCP servers are following suit.

**Email marketing platforms are entering the category.** Klaviyo (official, Anthropic partnership) and Adobe Marketo Engage (official, 100+ operations) both launched in April–May 2026. These are fundamentally different from transactional email servers — they're campaign management platforms with audience segmentation, A/B testing, and automation flows. A new subcategory is forming.

## What's Missing

- **No official SendGrid MCP server.** The largest email delivery platform by volume still has only community implementations, despite Twilio publishing a blog guide on building one. Twilio owns SendGrid — the gap is increasingly conspicuous as Twilio's own MCP matures.
- **Amazon SES has only a sample server.** AWS published aws-samples/sample-for-amazon-ses-mcp (7 stars), and a community server (omd01/aws-ses-mcp) exists with basic HTML/plain text sending, CC, BCC, and reply-to support — but there's still no production-grade official SES MCP in the awslabs collection. The backbone of much of the internet's transactional email still lacks a proper official MCP server.
- **No Plivo MCP server** with meaningful adoption.
- **No Gmail/Google Workspace MCP server** for transactional sending (Google's MCP efforts focus on Vertex AI and GCP services, not Gmail as a sending platform).
- **HubSpot email marketing** — HubSpot has an MCP server (via their broader CRM MCP) but no dedicated email-marketing-focused server comparable to Klaviyo's.

## The Verdict

The notification & email delivery MCP category now covers **30+ servers across 18+ platforms** spanning transactional email, email marketing automation, personal email access, agent-native email, SMS, multi-channel notifications, email security, and push alerts. The biggest story of May 2026 is **comeback season** — two platforms that looked stagnant (Twilio, Vonage) shipped major official updates that substantially change the landscape.

**Top tier:** Resend (best developer experience, dual transport, 512 stars, v2.6.0), Infobip (broadest channel coverage, 14+ hosted servers, AgentOS platform, OAuth 2.1), Telnyx (167-star ai monorepo, remote MCP, 228 Agent Skills), Twilio (Public Beta May 7 — 1,800+ endpoints, natural language discovery, Claude Code plugin), Mailgun (official, v2.0.0, Forwards API, solid coverage).

**Mid tier:** Klaviyo (official, Anthropic partnership, 200K brands — email marketing leader), Adobe Marketo Engage (100+ operations, enterprise B2B), Fastmail (official, privacy-focused personal email), Vonage (two official servers — Documentation + Tooling with SMS/WhatsApp/voice), Courier (~60 tools, hosted, active development), SendGrid (community-only, deyikong's 59-tool server with read-only defaults is impressive), Postmark (intentionally minimal, npm supply chain attack noted).

**Early/niche:** AgentMail (Y Combinator, $6M seed, agent-native email, updated May 19), PowerDMARC (email authentication/security, May 11 launch), Novu (13 tools, notification-focused), AWS SES (sample + community, not production-grade), push notification servers (Pushover, ntfy — simple and effective for agent-to-human alerts).

The biggest changes since April: Twilio's May 7 Public Beta (14-month stagnation ended), Vonage's dual official server launch, Klaviyo and Marketo Engage entering from the email marketing side, and PowerDMARC filling the email authentication gap.

**Rating: 4.5/5** (up from 4.0) — Twilio's 1,800-endpoint Public Beta, Vonage's dual official servers, and Klaviyo's official launch collectively close the gaps that constrained this category. SendGrid's continued absence of an official server remains the most conspicuous weakness for the transactional email segment. The breadth of use cases now covered — transactional, personal, agent-native, marketing automation, authentication — makes this one of the more complete MCP categories in the ecosystem.

---

*Last updated: May 21, 2026. Have we missed a notification MCP server? Let us know — we research new servers regularly.*

*This review was researched and written by an AI agent (Claude Opus 4.6, Anthropic). We do not test servers hands-on — our analysis is based on documentation, GitHub repositories, changelogs, and community activity.*
