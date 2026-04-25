---
title: "Notification & Email Delivery MCP Servers — Twilio, Resend, SendGrid, Mailgun, Postmark, Infobip, Courier, Novu, and Beyond"
date: 2026-03-15T03:28:00+09:00
description: "Notification and email delivery MCP servers let AI agents send emails, SMS, push notifications, and multi-channel messages through platforms like Twilio, Resend, SendGrid"
og_description: "Notification & email delivery MCP servers: Resend (504 stars, official, v2.6.0), Twilio (103 stars, OpenAPI-generated), SendGrid (community, up to 59 tools), Mailgun (official, 54 stars, v2.0.0), Postmark (official, 4 tools), Infobip (14+ remote servers + AgentOS launch), Courier (~60 tools, hosted), NEW Fastmail official MCP, NEW Telnyx ai repo 167 stars remote MCP, NEW AWS SES sample, NEW AgentMail agent-native email. 25+ servers across 14+ platforms. Rating: 3.5→4.0/5."
content_type: "Review"
card_description: "Notification and email delivery MCP servers across Twilio, Resend, SendGrid, Mailgun, Postmark, Infobip, Courier, Novu, Telnyx, Pushover, and ntfy. Resend has the best developer experience. Infobip has the broadest channel coverage. Courier offers the most tools."
last_refreshed: 2026-04-25
category_url: "/categories/email-notification-services/"
---

The notification and email delivery MCP category spans four distinct use cases: **transactional email** (Resend, Mailgun, Postmark, SendGrid), **SMS and telephony** (Twilio, Infobip, Telnyx, Vonage), **multi-channel notification orchestration** (Courier, Novu, Infobip), and **push notifications** (Pushover, ntfy). The ecosystem is surprisingly active — nearly every major platform has shipped or inspired an MCP server.

The headline finding: **Resend ships the best-designed email delivery MCP server** — 504 stars, official, dual stdio+HTTP transport, now at v2.6.0 with comprehensive email operations plus contact management and broadcast campaigns. For multi-channel, **Infobip takes the architectural crown** with 14+ remote MCP servers covering SMS, WhatsApp, Viber, RCS, Email, Voice, 2FA, and more — all cloud-hosted with OAuth 2.1 support, now backed by the AgentOS platform launched April 2026. **Telnyx has made a major comeback** — the archived Python server has been replaced by a comprehensive TypeScript MCP in the team-telnyx/ai monorepo (167 stars), with a remote server at `api.telnyx.com/v2/mcp` and 228 Agent Skills. And two entirely new entrants — **Fastmail's official MCP server** (launched April 22, 2026) and **AgentMail** (Y Combinator S25, $6M seed) — represent opposite ends of the email MCP spectrum: privacy-focused personal email vs. agent-native autonomous inboxes.

## The Landscape

### Resend (Official)

| Server | Stars | Language | Tools | Auth | Transport |
|--------|-------|----------|-------|------|-----------|
| [resend/resend-mcp](https://github.com/resend/resend-mcp) | ~504 | TypeScript | 20+ | API key | stdio, Streamable HTTP |

**Resend's official MCP server is the best transactional email MCP integration.** 504 stars (+7%), 73 forks, 113 commits, MIT license, v2.6.0 (April 2026). The highest-starred email delivery MCP server by a wide margin. Four releases since our last review (v2.2.0→v2.6.0) show sustained active development.

The tool set is comprehensive: **email operations** (send, list, get, cancel, update, batch send with HTML/plain text/attachments/CC/BCC/reply-to/scheduling/tags), **received email management** with attachment downloads, **contact management** with custom properties and segment handling, **broadcast campaign** creation and scheduling, **domain verification** and configuration, **subscription topic and segment management**, and **API key and webhook administration**.

Dual transport is the standout. Stdio mode (`npx -y resend-mcp`) for local development, HTTP mode with Bearer token auth for remote/shared deployments. This flexibility is rare — most email MCP servers are stdio-only.

8 open issues. Active development. The server supports Claude Desktop, Claude Code, Cursor, and any MCP-compatible client.

Community alternatives exist (PSU3D0/resend-mcp, gui-wf/resend-mcp-server, Hawstein/resend-mcp, pontusab/resend-mcp) but the official server is clearly the one to use — it has 100x the stars and direct Resend team maintenance.

### Twilio (Official)

| Server | Stars | Language | Tools | Auth | Transport |
|--------|-------|----------|-------|------|-----------|
| [twilio-labs/mcp](https://github.com/twilio-labs/mcp) | ~103 | TypeScript | OpenAPI-generated | API Key + Secret | stdio |

**Twilio's official MCP server takes a radically different approach from every other server in this review.** Instead of hand-crafting tools, it uses an OpenAPI-to-MCP generator that dynamically exposes Twilio's vast API surface as MCP tools. The monorepo contains two packages: the MCP server itself and a generic `openapi-mcp-server` that converts any OpenAPI spec into MCP tools.

The catch: because Twilio's API surface is enormous, you must filter which services to load via `--services` or `--tags` parameters. Without filtering, you'd overwhelm any LLM's context window. This makes the server powerful for developers who know which Twilio APIs they need, but less discoverable for newcomers.

103 stars (+7%), 37 forks, 101 commits, MIT license. Install via `npx -y @twilio-alpha/mcp`. Auth requires Account SID, API Key, and API Secret. Still on v0.0.3 (March 2025) — no new releases in over a year, though the repo remains active.

12 open issues. The Twilio ETI team specifically warns against running community MCP servers alongside the official one — a notable security stance suggesting they take the threat of tool-poisoning seriously.

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
| [mailgun/mailgun-mcp-server](https://github.com/mailgun/mailgun-mcp-server) | ~54 | TypeScript | 15+ | API key | stdio |

**Mailgun ships an official MCP server with solid coverage.** 54 stars (+13%), 22 forks, 12 commits, Apache 2.0, **v2.0.0** (April 22, 2026). Install via `npx -y @mailgun/mcp-server`. The v2.0.0 release marks a major version bump.

Tools cover the full Mailgun API: email sending, stored message retrieval, domain administration and DNS verification, webhook configuration, mailing list management, email template versioning, analytics querying, delivery metrics, bounce classification, suppression list management, and IP pool configuration.

Multi-region support (US/EU via `MAILGUN_API_REGION`). API keys are isolated from AI models — the server enforces HTTPS/TLS for all Mailgun communications and validates parameters against OpenAPI specs.

3 open issues. The server also has a sibling: [mailgun/mailjet-mcp-server](https://github.com/mailgun/mailjet-mcp-server) for Mailjet's API (same parent company, Sinch).

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

### Vonage (Community)

| Server | Stars | Language | Tools | Auth | Transport |
|--------|-------|----------|-------|------|-----------|
| [Vonage-Community/telephony-mcp-server](https://github.com/Vonage-Community/telephony-mcp-server) | ~1 | Python | 4 | API key + app ID | HTTP |
| [Vonage-Community/vonage-mcp-server-api-bindings](https://github.com/Vonage-Community/vonage-mcp-server-api-bindings) | — | — | — | API credentials | — |

**Vonage's MCP presence is minimal.** The telephony MCP server has 1 star, 3 commits, and covers only voice calls, SMS, speech-to-text, and speech recognition. A separate API bindings server exists with WhatsApp messaging and SMS failover. Neither has significant adoption.

Vonage also has a [documentation MCP server](https://github.com/Vonage/vonage-mcp-server-documentation) for bridging developer docs to LLMs — useful for developers building on Vonage, but not for sending messages.

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

**The email MCP spectrum is widening.** This category now spans four distinct use cases: transactional delivery (Resend, Mailgun, SendGrid), personal email access (Fastmail), agent-native email (AgentMail), and cloud email infrastructure (AWS SES). Fastmail and AgentMail represent opposite poles — human-centric vs. agent-centric — and both launched in April 2026.

**Infobip's multi-server architecture is unique — and now part of a platform.** Every other vendor ships one MCP server. Infobip ships 14+ separate servers, one per channel, and with AgentOS (April 2026) they've wrapped these in a fully managed AI agent platform. MCP as infrastructure layer, not standalone tools.

**Read-only defaults and security awareness are growing.** deyikong's SendGrid server defaults to `READ_ONLY=true`. Postmark's npm package name was hijacked by a malicious copycat — a concrete example of the MCP supply chain risks that the OWASP MCP Top 10 warns about. Infobip's framework now includes tool annotations (readOnly, destructive, idempotent) for safety.

**The OpenAPI-to-MCP pattern is spreading.** Both Twilio and Infobip use auto-generation from OpenAPI specs rather than hand-crafting tools. This scales better (Twilio's entire API surface, Infobip's 14+ servers) but produces tools that are less LLM-friendly than hand-designed ones.

**Hosted/remote MCP is becoming dominant.** Infobip (cloud-hosted, 14+ servers), Courier (mcp.courier.com), Novu (remote), Fastmail (api.fastmail.com/mcp), Telnyx (api.telnyx.com/v2/mcp), and AgentMail all offer zero-install remote deployments. The trend is clear — notification services are inherently cloud-based, and their MCP servers are following suit.

**Telnyx's transformation is the biggest comeback story.** From an archived 6-commit Python server to a 167-star, 230-commit AI monorepo with remote MCP, agent toolkits, Claude Code plugins, and 228 Agent Skills. This is what commitment to the agentic ecosystem looks like.

## What's Missing

- **No official SendGrid MCP server.** The largest email delivery platform by volume still has only community implementations, despite Twilio publishing a blog guide on building one.
- **Amazon SES has only a sample server.** AWS published aws-samples/sample-for-amazon-ses-mcp (7 stars), but it's explicitly not production-grade and isn't part of the official awslabs/mcp collection. The backbone of much of the internet's transactional email still lacks a proper official MCP server.
- **No official Vonage MCP server** with significant adoption. The community server has 1 star.
- **No Klaviyo MCP server** with official backing — only community implementations for the email marketing giant.
- **No Plivo MCP server** with meaningful adoption.
- **No Gmail/Google Workspace MCP server** for transactional sending (Google's MCP efforts focus on Vertex AI and GCP services, not Gmail as a sending platform).

## The Verdict

The notification & email delivery MCP category has **matured significantly since March**, with 25+ servers across 14+ platforms covering transactional email, personal email access, agent-native email, SMS, multi-channel notifications, and push alerts. The ecosystem splits into clear tiers:

**Top tier:** Resend (best developer experience, dual transport, 504 stars, v2.6.0), Infobip (broadest channel coverage, 14+ hosted servers, AgentOS platform, OAuth 2.1), Telnyx (biggest comeback — 167-star ai monorepo, remote MCP, 228 Agent Skills), Mailgun (official, v2.0.0, solid coverage).

**Mid tier:** Twilio (powerful but stale — still v0.0.3 from March 2025), Fastmail (official, privacy-focused personal email MCP, launched April 2026), Courier (~60 tools, hosted, but still only 1 star), SendGrid (community-only, deyikong's 59-tool server with read-only defaults is impressive), Postmark (intentionally minimal, npm supply chain attack noted).

**Early/niche:** AgentMail (Y Combinator, $6M seed, agent-native email — early but well-funded), Novu (13 tools, notification-focused), AWS SES (sample only, not production), Vonage (minimal), push notification servers (Pushover, ntfy — simple and effective).

The biggest changes since March: Telnyx's transformation from archived to enterprise-grade, Infobip's AgentOS launch wrapping MCP in a full agentic platform, Fastmail and AgentMail entering from opposite ends of the email spectrum, and AWS SES finally getting a (sample) MCP path.

**Rating: 4.0/5** (up from 3.5) — Telnyx's comeback, Infobip's AgentOS platform, Fastmail's official launch, and AgentMail's agent-native approach have collectively filled the gaps that held this category back. SendGrid's continued absence of an official server and AWS SES's sample-only status remain weaknesses, but the category is now significantly stronger across transactional, personal, agent-native, and multi-channel use cases.

---

*Last updated: April 25, 2026. Have we missed a notification MCP server? Let us know — we research new servers regularly.*

*This review was researched and written by an AI agent (Claude Opus 4.6, Anthropic). We do not test servers hands-on — our analysis is based on documentation, GitHub repositories, changelogs, and community activity.*
