---
title: "Telecommunications & Messaging MCP Servers — SMS, Voice, WhatsApp, Telegram, CPaaS, and Unified Communications"
date: 2026-03-16T00:15:00+09:00
description: "Telecommunications and messaging MCP servers are the strongest vertical category we've reviewed, with 50+ servers across 7 subcategories. SMS/CPaaS: twilio-labs/mcp (official, TypeScript, MIT — 1,400+ API endpoints as MCP tools, OpenAPI-to-MCP generator), team-telnyx/telnyx-mcp-server (official, 22 stars, Python — call control, SMS/MMS, phone number management, AI assistants, webhook receiver), Bandwidth/mcp-server (official, Python — enterprise voice/messaging/911), plivo/mcp (official — send_sms, make_call), sinch/sinch-mcp-server (official, TypeScript — text/media/template messages, voice calls, conference management), infobip/mcp (official, MIT — SMS/WhatsApp/Viber/RCS, bulk send, delivery reports), ClickSend/clicksend-mcp-server (official — SMS/MMS). Vonage: Vonage/vonage-mcp-server-documentation (official — API docs/code snippets), Vonage-Community/telephony-mcp-server (official community — voice/SMS/speech), vonage-mcp-server-api-bindings (API bindings). Voice: voice-call-mcp-server (Twilio + OpenAI GPT-4o Realtime), callcenter.js-mcp (VoIP/SIP + OpenAI). WhatsApp: lharries/whatsapp-mcp (5,300 stars, MIT, Python/Go — search/read/send via WhatsApp Web), FelixIsaac/whatsapp-mcp-extended (41 tools — reactions, groups, polls, newsletters), jlucaso1/whatsapp-mcp-ts (TypeScript/Baileys). Telegram: sparfenyuk/mcp-telegram (172 stars, MIT, Python — MTProto, read-only), chigwell/telegram-mcp (Telethon, full access). Matrix: mjknowles/matrix-mcp-server (30 stars, MIT, TypeScript — OAuth 2.0, 15 tools). iMessage: carterlasalle/mac_messages_mcp (contacts, groups, attachments). Multi-channel: trycourier/courier-mcp (official — email/SMS/push/WhatsApp/Slack/Teams/Discord). 3GPP: edhijlu/3gpp-mcp-server (12 stars, BSD-3, 535M word dataset). Gaps: no Asterisk/FreeSWITCH PBX, no SIP server management, no telecom billing (BSS), no network provisioning (OSS), no spectrum management, no number portability. Rating: 4.5/5."
og_description: "Telecommunications & Messaging MCP servers: Twilio (official, 1,400+ endpoints), Telnyx (official, call control + SMS), WhatsApp MCP (5,300 stars), Bandwidth, Plivo, Sinch, Infobip, Vonage — all official. 50+ servers reviewed. Rating: 4.5/5."
content_type: "Review"
card_description: "Telecommunications and messaging MCP servers for AI-powered SMS, voice calls, WhatsApp, Telegram, and unified communications. This is the strongest vertical category we've reviewed — dominated by official servers from major CPaaS providers. **Twilio launches the most comprehensive CPaaS MCP** — twilio-labs/mcp (TypeScript, MIT) is an official monorepo exposing all 1,400+ Twilio API endpoints as MCP tools. Includes an OpenAPI-to-MCP tool generator, meaning any Twilio API surface automatically becomes available to AI agents. Published on npm as @twilio-alpha/mcp. This isn't a wrapper around a few endpoints — it's the entire Twilio platform made accessible through MCP. **Telnyx delivers full telephony control** — team-telnyx/telnyx-mcp-server (22 stars, Python) is the official Telnyx MCP server with call control (make, transfer, hang up, play audio, text-to-speech), messaging (SMS/MMS), phone number management (search, buy, configure), AI assistant management, and webhook receiver via ngrok. A complete CPaaS-to-AI bridge. **Seven more CPaaS providers go official** — Bandwidth (enterprise voice/messaging/911 access), Plivo (send_sms + make_call), Sinch (text/media/template messages, voice calls, conference management with mute/unmute/hold), Infobip (MIT, SMS/WhatsApp/Viber/RCS, bulk send, scheduling, delivery reports, URL tracking), ClickSend (SMS/MMS), and Vonage (three servers: documentation access, telephony tools, and API bindings). Having 8+ major CPaaS providers with official MCP servers is unprecedented among vertical categories. **WhatsApp MCP is the most popular messaging server** — lharries/whatsapp-mcp (5,300 stars, MIT, Python + Go bridge) provides search, read, and send capabilities via WhatsApp Web protocol. FelixIsaac/whatsapp-mcp-extended adds 41 tools including reactions, group management, polls, presence tracking, and newsletters. Multiple TypeScript alternatives exist. **Telegram gets MTProto-level access** — sparfenyuk/mcp-telegram (172 stars, MIT) provides read-only Telegram access via MTProto protocol (not Bot API), while chigwell/telegram-mcp via Telethon provides full read/write including group management, media, contacts, and settings. **Voice AI agents emerge** — voice-call-mcp-server combines Twilio with OpenAI's GPT-4o Realtime model for AI-initiated voice calls. callcenter.js-mcp connects VoIP/SIP directly to OpenAI's Realtime API with o3-mini for instruction generation. These are early but signal a clear direction. **Matrix gets proper MCP integration** — mjknowles/matrix-mcp-server (30 stars, MIT, TypeScript) provides OAuth 2.0 authentication, 15 tools across tiers, and multi-homeserver support. The only federated/self-hosted messaging protocol with MCP integration. **Multi-channel via Courier** — trycourier/courier-mcp (official) unifies email, SMS, push notifications, in-app messaging, Slack, Teams, WhatsApp, Discord, and webhooks through a single MCP interface. For applications that need to reach users across channels, this eliminates managing separate integrations. **3GPP specifications become queryable** — edhijlu/3gpp-mcp-server (12 stars, BSD-3-Clause) provides sub-500ms search across 535 million words of 3GPP specifications. For telecom engineers working with 5G/LTE standards, this turns dense specification documents into a conversational resource. **SMS-specific community servers fill gaps** — deshartman/twilio-messaging-mcp-server (SMS with status callbacks), YiyangLi/sms-mcp-server (SMS/MMS via Twilio), griffinwork40/twilio-mcp (conversation management), mustafa-boorenie/twilio_sms_mcp (web-hosted, dual REST/MCP), twilio-agent-payments-mcp-server (PCI-compliant payments), and rchanllc/joltsms-mcp-server (real-SIM phone numbers for AI agent verification). **WeChat and iMessage get coverage** — BiboyQG/WeChat-MCP automates WeChat on macOS with 5 sub-agents, while multiple iMessage MCP servers provide read/send capabilities via macOS integration. **Traditional telecom infrastructure is absent** — no Asterisk, FreeSWITCH, or PBX management. No SIP server configuration. No telecom BSS (billing/rating) or OSS (network provisioning) systems. No spectrum management, number portability, or carrier interconnect tools. No MVNO management platforms. The CPaaS layer is excellently covered, but the traditional telco infrastructure layer has zero MCP representation. The category earns 4.5/5 — the highest rating for any vertical-specific category. Eight major CPaaS providers have official MCP servers. WhatsApp and Telegram have mature community implementations. Voice AI is emerging. The only thing keeping this from 5/5 is the complete absence of traditional telecom infrastructure — PBX systems, BSS/OSS, and carrier-grade tools that telcos actually run on."
last_refreshed: 2026-03-16
---

Telecommunications and messaging MCP servers let AI assistants send SMS, make voice calls, manage WhatsApp conversations, interact with Telegram, and orchestrate multi-channel communications. Instead of integrating with each provider's API separately, these servers expose telephony and messaging capabilities through the Model Context Protocol.

This review covers the **telecommunications and messaging** vertical — CPaaS providers, voice telephony, messaging platforms, unified communications, and telecom standards. For team communication tools like Slack, see our [Collaboration MCP review](/guides/collaboration-mcp-servers/). For email specifically, see our [Email MCP review](/reviews/email-mcp-servers/).

The headline findings: **Eight major CPaaS providers have official MCP servers** — an unprecedented level of vendor adoption. **Twilio exposes all 1,400+ API endpoints** through MCP. **WhatsApp MCP has 5,300 stars** — the most popular messaging integration. **Voice AI agents are emerging** with Twilio + OpenAI Realtime combinations. **Traditional telecom infrastructure (PBX, BSS/OSS) is completely missing.** Part of our **[Communication & Collaboration MCP category](/categories/communication-collaboration/)**.

## SMS & CPaaS Providers

### twilio-labs/mcp (Official)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [twilio-labs/mcp](https://github.com/twilio-labs/mcp) | ~77 | TypeScript | MIT | 1,400+ endpoints |

The **official Twilio MCP monorepo** — the most comprehensive CPaaS MCP integration available:

- **All 1,400+ Twilio API endpoints** exposed as MCP tools
- **OpenAPI-to-MCP generator** — automatically converts any Twilio API surface to MCP tools
- **Full platform coverage** — SMS, voice, video, conversations, verify, taskrouter, and more
- Published on npm as `@twilio-alpha/mcp`

This isn't a wrapper around a few messaging endpoints — it's the entire Twilio platform made accessible through MCP. The OpenAPI-to-MCP generator is architecturally significant: as Twilio adds new APIs, the MCP surface grows automatically.

### team-telnyx/telnyx-mcp-server (Official)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [telnyx-mcp-server](https://github.com/team-telnyx/telnyx-mcp-server) | ~22 | Python | — | Multiple |

The **official Telnyx MCP server** with complete telephony control:

- **Call control** — make, transfer, hang up, play audio, text-to-speech
- **Messaging** — send SMS and MMS
- **Phone number management** — search, buy, and configure numbers
- **AI assistant management** — manage Telnyx AI assistants
- **Webhook receiver** — ngrok-based webhook handling for inbound events

A complete CPaaS-to-AI bridge. Telnyx is known for competitive pricing and developer-friendly APIs — their MCP server makes all of that accessible to AI agents.

### Bandwidth/mcp-server (Official)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [Bandwidth/mcp-server](https://github.com/Bandwidth/mcp-server) | — | Python | — | Configurable |

The **official Bandwidth MCP server** for enterprise-grade communications:

- **Voice** — enterprise voice capabilities
- **Messaging** — SMS/MMS
- **911 access** — emergency services integration
- **Configurable tool selection** — enable/disable tools via environment variables

Bandwidth powers communications for many enterprise and government customers. The 911 access integration is unique among CPaaS MCP servers — critical for applications in emergency services or compliance-sensitive environments.

### plivo/mcp (Official)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [plivo/mcp](https://github.com/plivo/mcp) | — | — | — | 2+ |

The **official Plivo MCP server** with core telephony tools:

- `plivo/send_sms` — send SMS messages
- `plivo/make_call` — initiate voice calls
- Supports both API-based and MCP integrations

Plivo is known for cost-effective global messaging and voice. Their MCP integration is straightforward — fewer tools than Twilio but covers the essential use cases.

### sinch/sinch-mcp-server (Official)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [sinch-mcp-server](https://github.com/sinch/sinch-mcp-server) | — | TypeScript | — | Multiple |

The **official Sinch MCP server** covering messaging and voice:

- **Plain text messages** — send text via SMS or messaging channels
- **Media messages** — image, video, and document delivery
- **Template messages** — pre-approved message templates (required for WhatsApp Business)
- **Voice calls** — initiate calls
- **Conference calls** — manage conferences with mute, unmute, hold, and resume
- **End conferences** — clean conference teardown

Sinch acquired MessageMedia and provides global CPaaS. The conference call management (mute/unmute/hold/resume) is a standout feature not seen in other CPaaS MCP servers. Also see [messagemedia/sinch-engage-mcp-server](https://github.com/messagemedia/sinch-engage-mcp-server) for Sinch Engage (EU) and MessageMedia (AU) with contact management and reporting.

### infobip/mcp (Official)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [infobip/mcp](https://github.com/infobip/mcp) | — | — | MIT | Multiple |

**Official Infobip MCP servers** supporting multiple messaging channels:

- **SMS** — send, preview, schedule, bulk send
- **WhatsApp** — WhatsApp Business messaging
- **Viber** — Viber Business Messages
- **RCS** — Rich Communication Services
- **Delivery reports** — message delivery tracking
- **Message logs** — historical message data
- **URL tracking** — link click analytics
- **Multilingual support**

Infobip's multi-channel approach is notable — one MCP server covers SMS, WhatsApp, Viber, and RCS. For businesses that need to reach users across messaging platforms, this is the most comprehensive single-provider MCP integration. The MIT license is a plus. Also see [infobip/infobip-openapi-mcp](https://github.com/infobip/infobip-openapi-mcp) — a Spring AI framework for exposing any OpenAPI spec as MCP servers.

### ClickSend/clicksend-mcp-server (Official)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [clicksend-mcp-server](https://github.com/ClickSend/clicksend-mcp-server) | — | — | — | SMS/MMS |

The **official ClickSend MCP server** for SMS and MMS. ClickSend also covers voice, fax, email, and postal mail — though the MCP server currently focuses on messaging. Community alternative [J-Gal02/clicksend-mcp](https://github.com/J-Gal02/clicksend-mcp) adds text-to-speech call capabilities.

### Vonage (Official — 3 servers)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [vonage-mcp-server-documentation](https://github.com/Vonage/vonage-mcp-server-documentation) | — | — | — | Docs/code |
| [telephony-mcp-server](https://github.com/Vonage-Community/telephony-mcp-server) | — | — | — | Voice/SMS/STT |
| [vonage-mcp-server-api-bindings](https://github.com/Vonage-Community/vonage-mcp-server-api-bindings) | — | — | — | API tools |

**Vonage takes a three-server approach:**

- **Documentation server** — AI access to Vonage API docs, code snippets, tutorials, troubleshooting
- **Telephony server** — voice calls, SMS, speech-to-text, speech recognition
- **API bindings server** — direct Vonage API interaction tools

The documentation server is architecturally interesting — rather than just wrapping API calls, it gives AI agents the knowledge to understand Vonage's platform. This is particularly useful for AI coding assistants helping developers build Vonage integrations.

### Community SMS Servers

Several community-built servers extend the CPaaS MCP ecosystem:

- **[deshartman/twilio-messaging-mcp-server](https://github.com/deshartman/twilio-messaging-mcp-server)** — SMS with status callbacks, npm package
- **[YiyangLi/sms-mcp-server](https://github.com/YiyangLi/sms-mcp-server)** (~8 stars) — SMS/MMS via Twilio
- **[griffinwork40/twilio-mcp](https://github.com/griffinwork40/twilio-mcp)** — SMS with intelligent conversation management
- **[mustafa-boorenie/twilio_sms_mcp](https://github.com/mustafa-boorenie/twilio_sms_mcp)** — web-hosted, works as both MCP server and standalone REST API
- **[deshartman/twilio-agent-payments-mcp-server](https://github.com/deshartman/twilio-agent-payments-mcp-server)** — PCI-compliant agent-assisted payments via Twilio
- **[rchanllc/joltsms-mcp-server](https://github.com/rchanllc/joltsms-mcp-server)** — provisions real-SIM US phone numbers for AI agent phone verification, OTP extraction
- **[twilio-labs/function-templates/mcp-server](https://github.com/twilio-labs/function-templates/tree/main/mcp-server)** — run MCP servers on Twilio Functions infrastructure

## Voice & Telephony

### popcornspace/voice-call-mcp-server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [voice-call-mcp-server](https://github.com/popcornspace/voice-call-mcp-server) | — | — | MIT | Voice calls |

An MCP server combining **Twilio with OpenAI's GPT-4o Realtime model** for AI-initiated voice calls. This represents the emerging pattern of AI agents that can actually make phone calls and converse in real-time — not just send messages.

### gerkensm/callcenter.js-mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [callcenter.js-mcp](https://github.com/gerkensm/callcenter.js-mcp) | — | JavaScript | — | `simple_call`, `advanced_call` |

An **AI Voice Agent VoIP Connector** that makes phone calls using VoIP/SIP and OpenAI's Realtime API:

- Direct VoIP/SIP call initiation
- OpenAI Realtime API for conversation
- Uses o3-mini for instruction generation
- Two tools: `simple_call` and `advanced_call`

Lower-level than the Twilio-based approach — connects directly to SIP rather than through a CPaaS provider. More flexible but requires more infrastructure setup.

### LiveKit Agents (Official MCP Support)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [livekit/agents](https://github.com/livekit/agents) | — | — | — | Native MCP |

**LiveKit's agents framework** has native MCP support, working with LiveKit's telephony stack for phone calls. LiveKit provides real-time audio/video infrastructure — their MCP integration means AI agents can participate in voice and video calls through LiveKit's platform. See [livekit-examples/basic-mcp](https://github.com/livekit-examples/basic-mcp) for examples.

## Messaging Platforms

### WhatsApp

#### lharries/whatsapp-mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [whatsapp-mcp](https://github.com/lharries/whatsapp-mcp) | ~5,300 | Python + Go | MIT | Multiple |

The **most popular messaging MCP server** by far (5,300 stars):

- **Search messages** — full-text search across WhatsApp conversations
- **Read messages** — retrieve message history from any chat
- **Send messages** — send text messages to contacts
- **Manage contacts** — contact list access
- Uses WhatsApp Web protocol via Go bridge

The star count reflects real demand — people want AI assistants that can interact with their WhatsApp conversations. Uses the WhatsApp Web protocol (not the official API), which means it works with personal accounts but may be fragile if WhatsApp changes their web client.

#### FelixIsaac/whatsapp-mcp-extended

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [whatsapp-mcp-extended](https://github.com/FelixIsaac/whatsapp-mcp-extended) | — | — | — | 41 |

An **extended WhatsApp MCP** with 41 tools going well beyond basic messaging:

- Reactions, read receipts, message editing
- Group management (create, modify, admin controls)
- Polls and voting
- Presence/online status tracking
- Newsletter management
- Contact and profile management

If the base WhatsApp MCP is read/send, this is full WhatsApp automation.

#### Other WhatsApp Servers

- **[jlucaso1/whatsapp-mcp-ts](https://github.com/jlucaso1/whatsapp-mcp-ts)** — TypeScript alternative using Baileys library
- **[msaelices/whatsapp-mcp-server](https://github.com/msaelices/whatsapp-mcp-server)** — Python, uses GreenAPI + FastMCP
- **[mario-andreschak/mcp-whatsapp-web](https://github.com/mario-andreschak/mcp-whatsapp-web)** — TypeScript, WhatsApp Web
- **[pnizer/wweb-mcp](https://github.com/pnizer/wweb-mcp)** — WhatsApp Web MCP

### Telegram

#### sparfenyuk/mcp-telegram

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [mcp-telegram](https://github.com/sparfenyuk/mcp-telegram) | ~172 | Python | MIT | Read-only |

The **most popular Telegram MCP server** using MTProto protocol (not Bot API):

- List dialogs and chat history
- Get messages with filtering
- Download media files
- Access contacts
- Draft message management
- **Read-only** — designed for safe AI access without accidental sends

Using MTProto instead of the Bot API means this works with personal Telegram accounts, not just bots. The read-only design is a deliberate safety choice.

#### chigwell/telegram-mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [telegram-mcp](https://github.com/chigwell/telegram-mcp) | — | — | — | Full access |

**Full read/write Telegram access** via Telethon:

- Read chats and message history
- Send, modify, and delete messages
- Group management
- Media handling
- Contact management
- Settings modification

For users who need write access alongside read — but be cautious with AI agents that can modify your Telegram account.

#### Other Telegram Servers

- **[chaindead/telegram-mcp](https://github.com/chaindead/telegram-mcp)** — dialogs, messages, drafts, read statuses
- **[IQAIcom/mcp-telegram](https://github.com/IQAIcom/mcp-telegram)** — Telegraf-based, for bots and channels
- **[dryeab/mcp-telegram](https://github.com/dryeab/mcp-telegram)** — Telethon, send/edit/delete/search/download
- **[qpd-v/mcp-communicator-telegram](https://github.com/qpd-v/mcp-communicator-telegram)** — human-in-the-loop via Telegram bot

### Matrix Protocol

#### mjknowles/matrix-mcp-server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [matrix-mcp-server](https://github.com/mjknowles/matrix-mcp-server) | ~30 | TypeScript | MIT | 15 |

The **only federated messaging protocol with MCP integration**:

- **OAuth 2.0 authentication** — proper auth flow
- **15 tools across tiers** — room management, messaging, user profiles
- **Multi-homeserver support** — connect to any Matrix homeserver
- Room creation, joining, messaging, member management

Matrix is the open standard for decentralized communication (used by Element, French government, German military). This MCP server means AI agents can participate in federated, end-to-end encrypted conversations.

### WeChat

#### BiboyQG/WeChat-MCP

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [WeChat-MCP](https://github.com/BiboyQG/WeChat-MCP) | — | Python | MIT | 5 sub-agents |

**WeChat automation** on macOS via Accessibility API and screen capture:

- Summarize conversations
- Auto-reply to messages
- Search chat history
- Monitor conversations
- Analyze chat patterns

Uses macOS-specific automation rather than an API — necessarily fragile but there's no official WeChat API for personal accounts. Also see [loonghao/wecom-bot-mcp-server](https://github.com/loonghao/wecom-bot-mcp-server) for WeCom (WeChat Work) enterprise messaging.

### iMessage

Several MCP servers provide iMessage access on macOS:

- **[carterlasalle/mac_messages_mcp](https://github.com/carterlasalle/mac_messages_mcp)** — phone validation, attachments, contacts, group chats, send/receive
- **[hannesrudolph/imessage-query-fastmcp-mcp-server](https://github.com/hannesrudolph/imessage-query-fastmcp-mcp-server)** — FastMCP + imessagedb library
- **[wyattjoh/imessage-mcp](https://github.com/wyattjoh/imessage-mcp)** — read iMessage data
- **[marissamarym/imessage-mcp-server](https://github.com/marissamarym/imessage-mcp-server)** — AppleScript-based send/contacts

All macOS-only, leveraging the local Messages database or AppleScript. No cross-platform iMessage access exists (by Apple's design).

## Multi-Channel & Unified Communications

### trycourier/courier-mcp (Official)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [courier-mcp](https://github.com/trycourier/courier-mcp) | — | — | — | Multi-channel |

The **official Courier MCP server** for unified multi-channel messaging:

- **Email** — transactional and marketing
- **SMS** — via integrated providers
- **Push notifications** — mobile push
- **In-app messaging** — embedded notifications
- **Slack, Teams, WhatsApp, Discord** — team and consumer channels
- **Webhooks** — custom integrations

For applications that need to reach users across channels without managing separate provider integrations, Courier provides a single MCP interface that routes to the right channel.

### Other Multi-Channel Servers

- **[Helms-AI/openclaw-mcp-server](https://github.com/Helms-AI/openclaw-mcp-server)** — send messages via Telegram, WhatsApp, Discord, Slack, Signal, iMessage, Google Chat
- **[ComposioHQ/secure-openclaw](https://github.com/ComposioHQ/secure-openclaw)** — personal AI assistant across WhatsApp, Telegram, Signal, iMessage with 500+ app integrations
- **[nirholas/mcp-notify](https://github.com/nirholas/mcp-notify)** — notifications via Discord, Slack, Email, Telegram, Teams, webhooks, RSS

## Telecom Standards & Infrastructure

### edhijlu/3gpp-mcp-server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [3gpp-mcp-server](https://github.com/edhijlu/3gpp-mcp-server) | ~12 | TypeScript | BSD-3-Clause | Spec search |

A **3GPP specification search MCP** providing sub-500ms access to 535 million words of telecom standards:

- Specification search across the 3GPP corpus
- Multi-spec comparison
- Implementation requirements extraction
- Lightweight API bridge to TSpec-LLM dataset

For telecom engineers working with 5G, LTE, and NR standards, this turns impenetrable specification documents into a conversational resource. Also see [Lee-SiHyeon/mcp-server-3gpp](https://github.com/Lee-SiHyeon/mcp-server-3gpp) (MIT, TypeScript) with full-text search covering 17 specs (NAS, RRC, protocol conformance) via pre-built 107MB data via Git LFS.

### Industry Direction

The telecom industry is actively exploring MCP:

- **CAMARA / Open Gateway** (Linux Foundation) has published a position on exposing CAMARA network APIs (SIM Swap, Number Verification, Device Location) through MCP — no public server yet but announced as strategic direction
- **Telefonica Open Gateway** has published on MCP as the evolution of API consumption for telcos
- **SignalWire** acknowledges MCP compatibility but uses their own SWAIG protocol in production

These signals suggest more telecom infrastructure MCP servers are coming, but nothing production-ready today.

## What's Missing

The telecommunications MCP ecosystem has clear gaps on the infrastructure side:

- **PBX systems** — no Asterisk, FreeSWITCH, or 3CX MCP management
- **SIP server management** — no SIP proxy/registrar configuration
- **Telecom BSS** — no billing, rating, or revenue management systems
- **Telecom OSS** — no network provisioning, fault management, or performance monitoring
- **Spectrum management** — no frequency allocation or interference management
- **Number portability** — no LNP/MNP management
- **Carrier interconnect** — no SS7/SIGTRAN/Diameter management
- **MVNO management** — no virtual operator platforms
- **Contact center** — no Genesys, Five9, or NICE inContact MCP servers (despite being CPaaS-adjacent)
- **UCaaS platforms** — no Zoom Phone, Microsoft Teams Calling, or RingCentral MCP servers for unified communications management
- **Signal** — no MCP server for Signal Private Messenger despite its popularity

## The Bottom Line

**Rating: 4.5/5** — Telecommunications and messaging is the strongest vertical category we've reviewed. The unprecedented presence of **eight major CPaaS providers with official MCP servers** (Twilio, Telnyx, Vonage, Bandwidth, Plivo, Sinch, Infobip, ClickSend) sets this category apart. Add WhatsApp MCP at 5,300 stars, mature Telegram integrations, Matrix support, multi-channel via Courier, and emerging voice AI capabilities — this is a category where MCP adoption is already mainstream.

Twilio's approach of exposing all 1,400+ endpoints via an OpenAPI-to-MCP generator is architecturally the most ambitious. Telnyx provides the most complete telephony control. Infobip covers the most messaging channels (SMS/WhatsApp/Viber/RCS) under one MIT-licensed server. WhatsApp MCP's star count proves the consumer demand.

The only thing keeping this from 5/5 is the complete absence of traditional telecom infrastructure. PBX systems, BSS/OSS platforms, carrier interconnect, and contact center systems — the operational backbone of telecommunications — have zero MCP representation. The CPaaS layer is brilliantly covered; the telco infrastructure layer is untouched.

For developers building AI-powered communication features, this is the most production-ready MCP category available. Pick your CPaaS provider, install their official server, and you have enterprise-grade messaging and voice accessible to AI agents immediately.

*This review was last edited on 2026-03-16 using Claude Opus 4.6 (Anthropic).*
