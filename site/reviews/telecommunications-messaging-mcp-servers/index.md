# Telecommunications & Messaging MCP Servers — SMS, Voice, WhatsApp, Telegram, CPaaS, and Unified Communications

> Telecommunications and messaging MCP servers remain the strongest vertical category, with 60+ servers across 8 subcategories. Telegram ecosystem EXPLODED — chigwell/telegram-mcp reached 1,000 stars with 80+ tools v3.0.1.


Telecommunications and messaging MCP servers let AI assistants send SMS, make voice calls, manage WhatsApp conversations, interact with Telegram, and orchestrate multi-channel communications. Instead of integrating with each provider's API separately, these servers expose telephony and messaging capabilities through the Model Context Protocol.

This review covers the **telecommunications and messaging** vertical — CPaaS providers, voice telephony, messaging platforms, unified communications, and telecom standards. For team communication tools like Slack, see our [Collaboration MCP review](/guides/mcp-real-time-collaboration/). For email specifically, see our [Email MCP review](/reviews/gmail-mcp-servers/).

The headline findings: **Eight major CPaaS providers have official MCP servers** — an unprecedented level of vendor adoption. **Twilio exposes all 1,400+ API endpoints** through MCP (103 stars). **WhatsApp MCP has 5,600 stars** — the most popular messaging integration. **Telegram's chigwell/telegram-mcp reached 1,000 stars** with 80+ tools — the biggest growth in this refresh. **Voice AI broke through in 2026** — Vapi (47 stars), Ring-a-Ding, and Vonage telephony bridges are production-ready. **Infobip went enterprise-grade** with 15+ remote MCP servers, OAuth 2.1, and Streamable HTTP. **Traditional telecom infrastructure (PBX, BSS/OSS) is still missing** but CAMARA integration signals change. Part of our **[Communication & Collaboration MCP category](/categories/communication-collaboration/)**.

## SMS & CPaaS Providers

### twilio-labs/mcp (Official)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [twilio-labs/mcp](https://github.com/twilio-labs/mcp) | 103 | TypeScript | MIT | 1,400+ endpoints |

The **official Twilio MCP monorepo** — the most comprehensive CPaaS MCP integration available:

- **All 1,400+ Twilio API endpoints** exposed as MCP tools
- **OpenAPI-to-MCP generator** — automatically converts any Twilio API surface to MCP tools
- **Full platform coverage** — SMS, voice, video, conversations, verify, taskrouter, and more
- Published on npm as `@twilio-alpha/mcp`
- **MCP Dev Summit 2026 participation** — sessions on SSO consolidation and cross-app access for MCP

This isn't a wrapper around a few messaging endpoints — it's the entire Twilio platform made accessible through MCP. The OpenAPI-to-MCP generator is architecturally significant: as Twilio adds new APIs, the MCP surface grows automatically. Grew from ~77 to 103 stars (+34%) since our initial review.

### team-telnyx/telnyx-mcp-server (Official)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [telnyx-mcp-server](https://github.com/team-telnyx/telnyx-mcp-server) | 24 | Python | — | 36 |

The **official Telnyx MCP server** with expanded telephony and cloud services:

- **Call control** (7 tools) — make, transfer, hang up, play audio, text-to-speech
- **Messaging** (3 tools) — send SMS and MMS
- **Phone number management** (4 tools) — search, buy, and configure numbers
- **AI assistant management** (6 tools) — manage Telnyx AI assistants
- **Connection management** (3 tools) — configure SIP connections
- **Cloud storage** (7 tools) — file and object management
- **Embeddings** (3 tools) — vector search and storage
- **Secrets manager** (3 tools) — secure credential management
- **Webhook receiver** — ngrok-based webhook handling for inbound events

Expanded from basic telephony to 36 tools across 8 categories. Telnyx AI Agents now natively integrate with MCP servers for direct API connectivity. Note: the Python version is deprecated — TypeScript migration underway.

### Bandwidth/mcp-server (Official)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [Bandwidth/mcp-server](https://github.com/Bandwidth/mcp-server) | — | Python | — | 40+ |

The **official Bandwidth MCP server** (v0.2.0) for enterprise-grade communications with 40+ tools:

- **Voice** — enterprise voice capabilities, call events, call records
- **Messaging** — SMS/MMS, multi-channel messaging
- **911 access** — emergency services integration
- **Verification** — multi-factor authentication via SMS and voice
- **Phone number lookup** — carrier and number intelligence
- **Media management** — file upload and retrieval
- **Address validation** — postal address verification
- **Document uploads** — compliance document management
- **Analytics** — report generation and retrieval
- **Configurable tool selection** — enable/disable tools via environment variables

Bandwidth powers communications for many enterprise and government customers. Expanded from basic voice/messaging to 40+ tools across communications, verification, analytics, and compliance. The 911 access integration remains unique among CPaaS MCP servers.

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
| [sinch-mcp-server](https://github.com/sinch/sinch-mcp-server) | 1 | TypeScript | — | 25 |

The **official Sinch MCP server** with expanded multi-channel messaging and voice (v0.0.1-alpha.4):

- **Omni-channel messaging** (8 tools) — SMS, WhatsApp, RCS, Messenger via Conversation API
- **WhatsApp-specific** — dedicated WhatsApp send tool (split from omni-channel)
- **Email delivery** (5 tools) — via Mailgun integration
- **Voice calls** (4 tools) — initiate calls, TTS, conference management (mute/unmute/hold/resume)
- **Phone number management** (4 tools) — verification, lookup, multi-region support
- **Verification** (3 tools) — phone number verification flows
- **Streamable HTTP transport** — modern MCP transport support
- **Interactive messaging** — buttons, quick replies, template localization

Sinch was named a **Leader in the IDC MarketScape 2026 Communications Engagement Platforms** assessment. Expanded from basic messaging to 25 distinct tools with RCS support. Also see [messagemedia/sinch-engage-mcp-server](https://github.com/messagemedia/sinch-engage-mcp-server) for Sinch Engage (EU) and MessageMedia (AU) with contact management and reporting.

### infobip/mcp (Official)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [infobip/mcp](https://github.com/infobip/mcp) | 29 | Java | MIT | 15+ servers |

**Official Infobip remote MCP servers** — the most comprehensive enterprise messaging MCP platform:

- **SMS** — send, preview, schedule, bulk send
- **WhatsApp** — WhatsApp Business messaging
- **WhatsApp Flow** — interactive WhatsApp workflows
- **Viber** — Viber Business Messages
- **RCS** — Rich Communication Services
- **Email** — transactional and marketing email
- **Voice** — voice calling capabilities
- **Mobile App Messaging** — push notifications
- **2FA** — multi-factor authentication flows
- **CAMARA** — network API integration (SIM Swap, Number Verification)
- **People management** — customer data and profiles
- **Account management** — Infobip account administration
- **CPaaSX** — multi-tenant workflow orchestration
- **Documentation search** — developer resource access
- **Deep research** — API reference exploration
- **OAuth 2.1** with scope discovery, plus API key auth
- **Streamable HTTP** and SSE transport support

Infobip has gone from a multi-channel messaging provider to the most enterprise-grade MCP platform in the CPaaS space. The **15+ remote MCP server endpoints** cover everything from messaging to 2FA to CAMARA network APIs. Joined the **Agentic AI Foundation as Gold Member**. The [infobip/infobip-openapi-mcp](https://github.com/infobip/infobip-openapi-mcp) framework (28 stars, Java/Spring AI, v0.1.13) auto-generates MCP servers from any OpenAPI specification — and powers Infobip's own production servers. This framework is architecturally significant: any organization with OpenAPI-documented APIs can use it to create MCP servers instantly.

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

**Vonage takes a three-server approach**, now with Postman integration (February 2026):

- **Documentation server** — AI access to Vonage API docs, code snippets, tutorials, troubleshooting. Context-aware answers and code integrated directly into developer tools
- **Tooling server** — **real actions**: send SMS, manage numbers, check balances, voice calls, WhatsApp operations. This goes beyond documentation to actual platform control
- **Telephony server** — voice calls, SMS, speech-to-text, speech recognition via Vonage API
- **API bindings server** — direct Vonage API interaction tools

**February 2026**: Both Documentation and Tooling MCP Servers launched on the **Postman MCP Server verified list**, making them accessible through Postman's developer ecosystem. The Tooling Server is significant — it enables AI agents to perform real actions (send messages, manage numbers) rather than just retrieving information. Works with Claude, Cursor, VS Code Copilot, and OpenAI Agents.

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

2026 has been called the **"Year of the Voice Agent"** — sub-100ms latency, native audio reasoning, and seamless workflow integration have arrived. Voice AI MCP servers went from experimental to production-ready.

### VapiAI/mcp-server (Official)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [VapiAI/mcp-server](https://github.com/VapiAI/mcp-server) | 47 | TypeScript | MIT | 15+ |

**NEW** — The **official Vapi MCP server** for building AI voice assistants and phone agents:

- **Assistants** (5 tools) — list, create, update, retrieve AI voice assistants
- **Calls** (3 tools) — list, create, retrieve, schedule outbound calls
- **Phone numbers** (5 tools) — list, retrieve, manage phone numbers
- **Tools/function calling** (5 tools) — manage tools available to voice agents
- **OAuth + API key auth** — browser-based authentication on first use

Vapi is one of the leading voice AI platforms. Their MCP server means you can build, configure, and trigger voice AI agents directly from Claude or any MCP client. Teams are already using it for workflows like having Claude request a Vapi assistant call a patient to confirm an appointment. Install with: `claude mcp add vapi -- npx -y @vapi-ai/mcp-server`

### Ring-a-Ding/OpenClaw Voice Telephony

**NEW** — **Ring-a-Ding** launched in April 2026 as an OpenClaw skill for AI agent telephony:

- **Outbound phone calls** — AI agents can make real phone calls for tasks like requesting quotes, booking appointments, checking availability
- **Managed US phone number pool** — bring-your-own-key model ($19/month)
- **Real-time voice bridging** — connects AI voice to actual phone calls
- **Transcripts and summaries** — automatic call documentation
- **MCP server compatible** — works with any MCP-compatible agent
- **Dynamic call context** — AI generates purpose and context for each call at call time

This represents the next evolution: AI agents that don't just send messages but actually pick up the phone and have conversations on your behalf.

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
| [whatsapp-mcp](https://github.com/lharries/whatsapp-mcp) | 5,600 | Python + Go | MIT | Multiple |

The **most popular messaging MCP server** by far (5,600 stars, 1K forks):

- **Search messages** — full-text search across WhatsApp conversations
- **Read messages** — retrieve message history from any chat
- **Send messages** — send text messages to contacts
- **Manage contacts** — contact list access
- Uses WhatsApp Web protocol via Go bridge (whatsmeow library)

The star count reflects real demand — people want AI assistants that can interact with their WhatsApp conversations. Uses the WhatsApp Web protocol (not the official API), which means it works with personal accounts but may be fragile if WhatsApp changes their web client.

**Maintenance note (April 2026):** The original repo has been largely unmaintained since April 2025 (last release v0.0.1). Users report "Client outdated (405)" errors due to stale whatsmeow dependency. A maintained fork at [verygoodplugins/whatsapp-mcp](https://github.com/verygoodplugins/whatsapp-mcp) (28 stars) provides ongoing bug fixes, webhook integration, call history capture, and active development.

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

The Telegram MCP ecosystem **exploded** since our initial review — multiple servers crossed significant star milestones, and the full-access server chigwell/telegram-mcp reached 1,000 stars with 80+ tools.

#### chigwell/telegram-mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [telegram-mcp](https://github.com/chigwell/telegram-mcp) | 1,000 | Python | — | 80+ |

**The most popular Telegram MCP server** — surged from uncounted to **1,000 stars** (262 forks, v3.0.1, April 28, 2026):

- **Accounts tools** — current user info, session management
- **Chats tools** — dialog listing, unread filtering, chat search
- **Messages tools** — send, edit, delete, search, retrieve by link
- **Contacts tools** — contact management and lookup
- **Media tools** — download, upload, media handling
- **Profile/privacy tools** — profile settings, privacy configuration
- **Folders/drafts tools** — folder management, draft read/write

Full read/write Telegram access via Telethon with 80+ MCP tools across 7 functional categories. This is the most comprehensive messaging-platform MCP server outside of the CPaaS providers. The jump to 1,000 stars signals massive demand for AI-Telegram integration.

#### sparfenyuk/mcp-telegram

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [mcp-telegram](https://github.com/sparfenyuk/mcp-telegram) | 175 | Python | MIT | Read-only |

**Read-only Telegram MCP** using MTProto protocol (not Bot API):

- List dialogs and chat history
- Get messages with filtering
- Download media files
- Access contacts
- Draft message management
- **Read-only** — designed for safe AI access without accidental sends

Using MTProto instead of the Bot API means this works with personal Telegram accounts, not just bots. The read-only design is a deliberate safety choice — ideal for AI agents that should observe but not act.

#### chaindead/telegram-mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [chaindead/telegram-mcp](https://github.com/chaindead/telegram-mcp) | 321 | — | — | 5 |

**Fast-growing Telegram MCP** (321 stars, 42 forks, v0.2.0, February 2026):

- `tg_me` — get current account information
- `tg_dialogs` — list dialogs with unread filter
- `tg_read` — mark dialog as read
- `tg_dialog` — retrieve messages from specific dialog
- `tg_send` — send draft messages to any dialog

Clean, focused design with 5 well-defined tools and 24 releases. The 321-star count suggests strong community preference for a simpler, more constrained Telegram MCP.

#### dryeab/mcp-telegram

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [dryeab/mcp-telegram](https://github.com/dryeab/mcp-telegram) | 244 | Python | MIT | 8 |

**Mid-range Telegram MCP** (244 stars, 37 forks, 80 commits) via Telethon:

- 4 messaging tools — send, edit, delete, get messages
- 2 search/navigation tools — search dialogs, message from link
- 2 draft management tools — get and set drafts
- Media download capability

A solid middle ground between sparfenyuk's read-only safety and chigwell's full 80+ tools.

#### Other Telegram Servers

- **[IQAIcom/mcp-telegram](https://github.com/IQAIcom/mcp-telegram)** — Telegraf-based, for bots and channels
- **[qpd-v/mcp-communicator-telegram](https://github.com/qpd-v/mcp-communicator-telegram)** — human-in-the-loop via Telegram bot
- **[fast-mcp-telegram](https://pypi.org/project/fast-mcp-telegram/)** — NEW (April 2026), production-ready Telegram integration via PyPI
- **[tensakulabs/telegram-mcp](https://github.com/tensakulabs/telegram-mcp)** — MTProto user client for bot interaction

### Matrix Protocol

#### mjknowles/matrix-mcp-server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [matrix-mcp-server](https://github.com/mjknowles/matrix-mcp-server) | 40 | TypeScript | MIT | 15 |

The **primary federated messaging protocol MCP** (40 stars, 15 forks, 37 commits):

- **OAuth 2.0 authentication** — proper auth flow with token exchange
- **15 tools across tiers** — Tier 0 (read-only: room info, messages, profiles, search, notifications) and Tier 1 (actions: message sending, room lifecycle, administration)
- **Multi-homeserver support** — connect to any Matrix homeserver
- Room creation, joining, messaging, member management
- Production-ready with comprehensive error handling

Matrix is the open standard for decentralized communication (used by Element, French government, German military). Grew from 30 to 40 stars (+33%). Also see NEW [ricelines/matrix-mcp](https://github.com/ricelines/matrix-mcp) — Matrix chat MCP powered by Mautrix, providing an alternative implementation.

### WeChat

#### BiboyQG/WeChat-MCP

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [WeChat-MCP](https://github.com/BiboyQG/WeChat-MCP) | 167 | Python | MIT | 5 sub-agents |

**WeChat automation** on macOS (167 stars, 54 forks) via Accessibility API and screen capture:

- `fetch_messages_by_chat` — get recent messages from a chat
- `reply_to_messages_by_chat` — send replies to chats
- `add_contact_by_wechat_id` — add contacts and send friend requests
- `publish_moment_without_media` — post text-only Moments with optional draft mode
- **5 intelligent sub-agents** for Claude Code: chat-summarizer, auto-replier, message-searcher, multi-chat-checker, chat-insights

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
| [courier-mcp](https://github.com/trycourier/courier-mcp) | 1 | — | — | 60 |

The **official Courier MCP server** (v1.3.0, 180 commits) for unified multi-channel messaging with **60 tools**:

- **Send messages** — inline content, templates, list sends
- **Delivery tracking** — status, rendered content, event history
- **User management** — create, merge, update user profiles
- **Audience targeting** — define and manage recipient audiences
- **Automation triggers** — invoke automation templates
- **Preference controls** — manage notification preferences per user
- **Email** — transactional and marketing
- **SMS** — via integrated providers
- **Push notifications** — mobile push
- **In-app messaging** — embedded notifications
- **Slack, Teams, WhatsApp, Discord** — team and consumer channels
- **Webhooks** — custom integrations
- Hosted at `https://mcp.courier.com` with local development option

Expanded from basic multi-channel to 60 comprehensive tools. For applications that need to reach users across channels, Courier provides the deepest MCP integration for notification orchestration. Currently in beta.

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

The telecom industry's MCP adoption accelerated significantly since our initial review:

- **CAMARA / Open Gateway** — Infobip now has a CAMARA MCP server endpoint in production, providing SIM Swap and Number Verification capabilities through MCP. This is the first production CAMARA-MCP integration
- **Agentic AI Foundation** — Infobip joined as Gold Member, directly shaping the infrastructure standards for AI agent communication
- **IDC MarketScape 2026** — Sinch named a Leader in Communications Engagement Platforms, with MCP as a core enablement technology
- **MCP Dev Summit 2026** — Twilio participated in sessions on SSO consolidation and cross-app access, signaling enterprise-grade MCP standardization
- **Voice AI consensus** — Industry declaring 2026 as "Year of the Voice Agent" with sub-100ms latency, native audio reasoning, and MCP-native telephony
- **Cordial** — launched MCP interface with RCS as a supported channel, with early studies showing 3-7x higher click-through rates than SMS
- **Streamable HTTP adoption** — Sinch and Infobip both adopted Streamable HTTP transport, aligning with the broader MCP ecosystem's move away from SSE

The direction is clear: CPaaS providers are moving from "we have an MCP server" to "MCP is our primary AI agent integration layer."

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

**Rating: 4.5/5** — Telecommunications and messaging remains the strongest vertical category we've reviewed, and it's getting stronger. The **eight major CPaaS providers with official MCP servers** (Twilio, Telnyx, Vonage, Bandwidth, Plivo, Sinch, Infobip, ClickSend) continue to expand — Telnyx now has 36 tools, Bandwidth 40+, Sinch 25 with RCS, Infobip expanded to 15+ remote server endpoints with OAuth 2.1 and CAMARA integration.

The biggest story this refresh is the **Telegram ecosystem explosion** — chigwell/telegram-mcp reached 1,000 stars with 80+ tools, chaindead/telegram-mcp surged to 321 stars, and dryeab/mcp-telegram hit 244 stars. Telegram MCP went from a fragmented subcategory to one of the most active in any vertical.

**Voice AI broke through** — Vapi (47 stars, MIT) provides production-ready voice agent management, Ring-a-Ding launched AI-initiated outbound phone calls, and the industry consensus is that 2026 is the "Year of the Voice Agent." This fills what was previously the weakest subcategory.

Twilio's approach of exposing all 1,400+ endpoints via an OpenAPI-to-MCP generator remains architecturally the most ambitious. Infobip's evolution to 15+ remote servers with CAMARA integration makes them the most enterprise-ready. Courier's expansion to 60 tools makes it the deepest multi-channel integration.

The gap to 5/5 is narrowing. Traditional telecom infrastructure (PBX, BSS/OSS) is still absent, but Infobip's CAMARA integration means network APIs (SIM Swap, Number Verification) are now accessible through MCP. Voice AI is no longer "emerging" — it's here. The CPaaS layer is brilliantly covered, voice AI is production-ready, and CAMARA is bridging toward network infrastructure.

For developers building AI-powered communication features, this is the most production-ready MCP category available. Pick your CPaaS provider, install their official server, and you have enterprise-grade messaging and voice accessible to AI agents immediately.

*This review was refreshed on 2026-04-29 using Claude Opus 4.6 (Anthropic). Initial review: 2026-03-16.*

