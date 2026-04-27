---
title: "Telecommunications & Communications MCP Servers — Twilio, Telnyx, Vonage, Sinch, Plivo, Cisco Meraki, NetBox, UniFi, and More"
date: 2026-03-15T18:00:00+09:00
description: "Telecommunications and communications MCP servers are giving AI agents the ability to send SMS, make phone calls, manage network infrastructure, and orchestrate multi-channel messaging."
og_description: "Telecom & communications MCP servers: UniFi Suite (274 stars, 224 tools), NetBox (158 stars, DCIM/IPAM), Twilio official (103 stars, full API), Voice Call MCP (59 stars, AI calls), Cisco Docker Suite (34 stars, 10 servers), Vonage upgraded (14 tools + docs), RingCentral alpha. Rating: 4.0/5."
content_type: "Review"
card_description: "Telecommunications and communications MCP servers for CPaaS platforms, network infrastructure management, SMS/voice, messaging, and video conferencing. This category stands out for strong official vendor participation — Twilio, Telnyx, Sinch, Vonage, and Plivo all have official or vendor-community MCP servers, making it one of the best-supported MCP categories by established companies. The biggest development since our initial review is the UniFi explosion — sirkirby/unifi-mcp (274 stars, 224 tools) now covers Network, Protect, and Access, making it the most popular network infrastructure MCP server by star count, surpassing even NetBox (158 stars). Vonage has upgraded from a minimal 2-tool server to a full 14-tool API binding platform plus a dedicated documentation MCP server. Voice AI is emerging as a new subcategory — popcornspace/voice-call-mcp-server (59 stars) enables real-time AI voice calls via Twilio and GPT-4o Realtime. RingCentral's App Connect MCP (alpha) partially fills the biggest UCaaS gap. Cisco's Network MCP Docker Suite (34 stars, +36%) continues growing with 10 containerized servers for unified AIOps. The CAMARA project expanded to 60 APIs including 10 stable/production-ready, though public MCP implementations remain pending. Gaps narrowing: RingCentral partially addressed, voice AI emerging, European CPaaS represented (sipgate). Still missing: Asterisk/FreeSWITCH/SIP PBX, WebRTC-native, full UCaaS platforms (8x8, Genesys), carrier network APIs. Rating holds at 4.0/5."
last_refreshed: 2026-04-27
---

Telecommunications and communications MCP servers are giving AI agents the power to send messages, make phone calls, manage network infrastructure, and orchestrate multi-channel communications — all through natural language. Instead of writing custom integrations for each provider, an AI agent can discover and use Twilio's SMS API, check Cisco Meraki network health, or send a WhatsApp message through a standardized MCP interface.

The landscape spans seven areas: **CPaaS platforms** (Twilio, Telnyx, Sinch, Vonage, Plivo — official vendor servers), **network infrastructure** (UniFi, NetBox, Cisco Meraki, Catalyst Center), **voice AI** (real-time AI-powered calling), **community SMS/voice** (focused Twilio wrappers for messaging and payments), **messaging platforms** (WhatsApp, Telegram), **network scanning and security** (Nmap, vulnerability scanning), and **video conferencing** (Zoom, tl;dv meeting intelligence).

**What's changed since our March 2026 review:** The biggest story is the **UniFi explosion** — sirkirby/unifi-mcp (274 stars, 224 tools) now covers Network, Protect, and Access, becoming the most popular network infrastructure MCP server by star count, surpassing NetBox. **Vonage upgraded massively** from 2 tools to a full 14-tool API binding platform plus a dedicated documentation server. **Voice AI emerged as a new subcategory** — popcornspace/voice-call-mcp-server (59 stars) enables real-time AI voice calling via Twilio + GPT-4o Realtime. **RingCentral partially filled its gap** with App Connect MCP in alpha. **sipgate adds European CPaaS representation**. WhatsApp MCP exploded from 394 to 5,600 stars.

The headline findings: **Official vendor participation remains exceptional** — Twilio, Telnyx, Sinch, Vonage, and Plivo all have official MCP servers, with Vonage now providing three separate servers. **UniFi leads network infrastructure** at 274 stars with 224 tools across Network, Protect, and Access. **NetBox hit v1.1.0** at 158 stars (+24%) with improved field filtering. **Cisco's Docker Suite grew to 34 stars** (+36%) for unified AIOps. **CAMARA expanded to 60 APIs** including 10 stable/production-ready, though public MCP implementations remain pending. Part of our **[Communication & Collaboration MCP category](/categories/communication-collaboration/)**.

## CPaaS Platforms (Official Vendor Servers)

### Twilio MCP (Official)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [twilio-labs/mcp](https://github.com/twilio-labs/mcp) | 103 | TypeScript | MIT | Dynamic (full API) |

The **most comprehensive communications MCP server**. This official monorepo takes a unique approach: instead of hand-coding individual tools, it includes an OpenAPI-to-MCP generator that dynamically converts Twilio's entire public API catalog into MCP-compatible tools.

Key capabilities:
- **Full API coverage** — SMS, voice, video, conversations, email (SendGrid), verify, and every other Twilio product
- **Configurable filtering** — `--services` and `--tags` flags let you expose only the APIs you need, reducing tool bloat
- **Two components** — the MCP server itself plus the reusable OpenAPI-to-MCP generator (useful for other OpenAPI specs)

This is the right architecture for a company with hundreds of API endpoints. Rather than maintaining a static list of MCP tools, the server auto-generates tools from the same OpenAPI specs that power Twilio's SDKs. The trade-off is that dynamically generated tools may have less polished descriptions than hand-crafted ones.

Deploy via `npx` with your Twilio account SID and auth token. Twilio's blog warns against using community MCP servers alongside the official one due to potential credential conflicts.

### Telnyx MCP (Official, Archived)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [team-telnyx/telnyx-mcp-server](https://github.com/team-telnyx/telnyx-mcp-server) | 24 | Python | — | 8 categories |

An official Telnyx implementation covering **telephony, messaging, AI assistants, cloud storage, and credential management** — the broadest feature set of any telecom MCP server:

- **Call Control** — make calls, transfer, play audio, send DTMF tones
- **Messaging** — send SMS/MMS, access conversation history
- **Phone Numbers** — list, buy, and configure phone numbers
- **AI Assistants** — create and manage Telnyx AI agents with custom configurations
- **Cloud Storage** — bucket management and file operations
- **Embeddings** — website scraping and file embedding for RAG
- **Connections** — manage voice connections
- **Secrets Manager** — manage integration credentials securely

Supports tool filtering via environment variables and includes a webhook receiver with ngrok tunnel for real-time event handling. **Note:** This Python version was archived September 2025. Telnyx has released a new TypeScript MCP server at `@telnyx/mcp-server` (available via npx) that takes a different approach — a "Code Mode" where agents write TypeScript code against the Telnyx SDK, which is then executed in an isolated sandbox. This gives agents access to the full Telnyx API surface without pre-defining individual tools.

### Sinch MCP (Official)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [sinch/sinch-mcp-server](https://github.com/sinch/sinch-mcp-server) | 0 | TypeScript | — | 23 |

The **most feature-complete multi-channel communications MCP** with 23 tools across five categories:

- **Conversation (8 tools)** — text/media/template/interactive/location/choice messages, app and template management
- **Email (5 tools)** — SendGrid-style message sending, template management, delivery status, event tracking, analytics
- **Verification (3 tools)** — phone number lookup, SMS verification, OTP submission
- **Voice (4 tools)** — text-to-speech callouts, conference calling, participant management, conference termination
- **Configuration (1 tool)** — tool availability and status listing

Supports tool filtering by tags and remote deployment via Server-Sent Events (SSE). Despite zero GitHub stars, this is a well-structured official server that covers more communication channels than any single competitor. The conversation tools support WhatsApp, SMS, RCS, and other channels through Sinch's unified API.

### Vonage MCP Platform (Official — Now 3 Servers)

Vonage has significantly expanded its MCP presence since our initial review, going from a single 2-tool server to a full three-server platform:

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [Vonage-Community/vonage-mcp-server-api-bindings](https://github.com/Vonage-Community/vonage-mcp-server-api-bindings) | 3 | JavaScript | Apache-2.0 | 14 |
| [Vonage/vonage-mcp-server-documentation](https://github.com/Vonage/vonage-mcp-server-documentation) | 0 | — | Apache-2.0 | 7 |
| [Vonage-Community/telephony-mcp-server](https://github.com/Vonage-Community/telephony-mcp-server) | 1 | Python | MIT | 2 |

**Vonage MCP Tooling Server** (NEW) — The headline upgrade. 14 tools across 4 categories: account management (balance, applications, API keys, secrets), number management (search, link), reporting (activity records), and messaging/communication (SMS, WhatsApp, RCS with failover, voice messages). Available via npm as `@vonage/vonage-mcp-server-api-bindings` (v1.3.0). Now available on Postman. Open-source and accepting contributions.

**Vonage Documentation MCP Server** (NEW) — 7 tools for AI-assisted development: `vonage_docs_search`, `vonage_code_generator`, `vonage_api_reference`, `vonage_sdk_info`, `vonage_troubleshooter`, `vonage_tutorial_finder`, `vonage_use_case_examples`. Hosted at `documentation-mcp.vonage.dev/mcp`.

**Vonage Telephony MCP** — The original 2-tool server remains available as a simple starting template for voice calls and SMS.

This three-server approach — tooling, documentation, and simple telephony — makes Vonage the CPaaS provider with the most comprehensive MCP strategy, even if Twilio's single server has broader API coverage.

### Plivo MCP

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [plivo/mcp](https://github.com/plivo/mcp) | 0 | Python | — | 6 |

A FastMCP plugin for Plivo's API with 6 tools:

- **Send SMS** — message delivery via Plivo
- **Make calls** — voice calls with customizable answer/hangup/ring event URLs
- **Create applications** — voice application setup for call routing
- **Create endpoints** — SIP endpoint provisioning for VoIP
- **Get CDRs** — call detail record retrieval
- **Get MDRs** — message detail record retrieval

The CDR/MDR retrieval tools are notable — most telecom MCP servers focus on sending messages but don't provide analytics or billing data access. The SIP endpoint provisioning makes this the only CPaaS MCP server with explicit VoIP infrastructure management.

## Network Infrastructure

### UniFi MCP Suite (NEW — Most Popular Network MCP)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [sirkirby/unifi-mcp](https://github.com/sirkirby/unifi-mcp) | 274 | Python | MIT | 224 |

The **most popular network infrastructure MCP server by star count**, surpassing even NetBox. This monorepo provides MCP servers for three UniFi applications:

- **Network (161 tools)** — network diagnostics, firewall policy management with audit scoring, WiFi configuration, VLAN management, client monitoring, DPI analysis, VPN, and full device lifecycle management
- **Protect (34 tools)** — camera event detection, recording access, cross-product timeline correlation with Network events
- **Access (29 tools)** — door management, visitor credentials, access control policies

Key architectural features:
- **Preview-then-confirm workflow** for all configuration changes — the AI agent shows proposed changes before applying them
- **Cloud relay support** via Cloudflare Workers for remote access without VPN
- **Multi-location capability** with annotation-based tool fan-out
- **Shared permission model** ensuring consistent security across all three servers

The rapid growth from zero to 274 stars reflects strong demand from the homelab and small-business networking community. Where NetBox serves enterprise DCIM/IPAM, this serves the hands-on network operator who wants AI-assisted management of their entire UniFi deployment.

**UniFi ecosystem expanded to 6+ implementations** — other notable entries include [DataKnifeAI/unifi-network-mcp](https://github.com/DataKnifeAI/unifi-network-mcp) (27 tools, Go), [enuno/unifi-mcp-server](https://github.com/enuno/unifi-mcp-server), [ry-ops/unifi-mcp-server](https://github.com/ry-ops/unifi-mcp-server) (with A2A support), and [jmagar/unifi-mcp](https://github.com/jmagar/unifi-mcp).

### Network MCP Docker Suite (Cisco)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [pamosima/network-mcp-docker-suite](https://github.com/pamosima/network-mcp-docker-suite) | 34 | Python | — | 10 servers |

The **most architecturally ambitious networking MCP project** — a Docker Compose suite bundling 10 specialized MCP servers for unified AI-driven network operations:

| Port | Server | Purpose |
|------|--------|---------|
| 8000 | Meraki MCP | Cloud network management via Meraki Dashboard API |
| 8001 | NetBox MCP | DCIM/IPAM infrastructure documentation |
| 8002 | Catalyst Center MCP | Enterprise network management and assurance |
| 8003 | IOS XE MCP | Direct SSH-based device management |
| 8004 | ThousandEyes MCP | Network performance monitoring |
| 8005 | ISE MCP | Identity and access control |
| 8006 | Splunk MCP | Log analysis and operational intelligence |
| 8007 | Prometheus MCP | Metrics querying |
| 8008 | ClickHouse MCP | Syslog and log queries |
| 8009 | GitLab MCP | CI/CD pipeline orchestration |

Supports modular deployment profiles — `cisco`, `monitoring`, `security`, `orchestration`, `netops-stack` — so you can deploy only the servers relevant to your infrastructure. Compatible with Cursor IDE, LibreChat, and Claude Desktop.

The cross-platform correlation is where this shines: an AI agent can investigate a network issue by querying Meraki for cloud network status, Catalyst Center for enterprise health, IOS XE for device-level diagnostics, ThousandEyes for external monitoring, and Splunk for log analysis — all in a single conversation.

### NetBox MCP Server (Official)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [netboxlabs/netbox-mcp-server](https://github.com/netboxlabs/netbox-mcp-server) | 158 | Python | Apache-2.0 | 3 |

The **most popular enterprise DCIM/IPAM MCP server** (surpassed in total stars by UniFi Suite, but serving a different audience). Provides read-only access to NetBox — the leading open-source DCIM/IPAM platform — through 3 focused tools:

- **get_objects** — retrieve devices, IP addresses, interfaces, sites, and other NetBox objects with filtering
- **get_object_by_id** — detailed information for specific objects
- **get_changelogs** — audit trail and change history

The standout feature is **token optimization**: field filtering reduces API response size by up to 90%, with pre-defined "common field patterns" for devices, IPs, interfaces, and sites. This matters because LLM context windows are expensive, and network infrastructure queries can return massive payloads.

Supports stdio and HTTP transports, Docker deployment, and flexible configuration via environment variables, `.env` files, and CLI arguments. Now at v1.1.0 (April 2026) with improved project structure — command changed from `uv run server.py` to `uv run netbox-mcp-server`.

### Meraki Magic MCP (Cisco DevNet)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [CiscoDevNet/meraki-magic-mcp-community](https://github.com/CiscoDevNet/meraki-magic-mcp-community) | 25 | Python | — | 12-804 |

Two implementation approaches in one repository:

- **Dynamic MCP** — auto-generates tools from the Meraki SDK, providing ~804 API endpoints with 100% SDK coverage. Updates automatically when Cisco releases new APIs
- **Manual MCP** — 40 curated endpoints with type-safe Pydantic validation. 12 pre-registered tools for the most common operations

The dynamic mode is impressive in scope but may overwhelm AI agents with too many tools. The manual mode provides a curated experience covering organization/network management, device configuration, wireless SSID management, switch ports, VLANs, firewall rules, camera settings, and client policies.

Performance features include response caching (reduces API calls by 50-90%), optional read-only safety mode, automatic retry, and rate limit handling.

### UniFi Network MCP

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [DataKnifeAI/unifi-network-mcp](https://github.com/DataKnifeAI/unifi-network-mcp) | 1 | Go | MIT | 27 |

The only MCP server for **Ubiquiti UniFi** network management — 27 tools covering:

- WiFi network creation, updates, and monitoring
- Firewall zone and ACL rule management
- Traffic control with rate limiting
- Site-to-site VPN tunnel configuration
- Guest WiFi voucher generation
- Deep Packet Inspection (DPI) application analysis
- Device and client monitoring
- WAN configuration and RADIUS profiles

Written in Go with dual transport support (stdio and HTTP). Covers the full lifecycle of consumer/prosumer network management — useful for home lab operators and small businesses running UniFi infrastructure.

## Community SMS/Voice (Twilio Wrappers)

### Twilio SMS/Messaging Servers

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [YiyangLi/sms-mcp-server](https://github.com/YiyangLi/sms-mcp-server) | 12 | JavaScript | MIT | 1 |
| [deshartman/twilio-messaging-mcp-server](https://github.com/deshartman/twilio-messaging-mcp-server) | 5 | — | — | — |
| [griffinwork40/twilio-mcp](https://github.com/griffinwork40/twilio-mcp) | — | — | — | — |
| [mustafa-boorenie/twilio_sms_mcp](https://github.com/mustafa-boorenie/twilio_sms_mcp) | — | — | — | — |
| [0x-Professor/Twilio-mcp-server](https://github.com/0x-Professor/Twilio-mcp-server) | — | — | — | — |

Five community Twilio SMS servers with different approaches:

**YiyangLi/sms-mcp-server** (12 stars) — the most popular community option. Simple SMS/MMS sending with pre-built prompts for common scenarios.

**deshartman/twilio-messaging-mcp-server** (5 stars) — provides tools, resources, and prompts for Twilio Messaging API interaction. Goes beyond simple sending to include message management.

**griffinwork40/twilio-mcp** — intelligent conversation management with SMS. Maintains conversation state across messages.

**0x-Professor/Twilio-mcp-server** — production-grade SMS/MMS with scheduling, conversation threading, and account/phone number management.

For most use cases, the **official twilio-labs/mcp** server supersedes these community implementations. However, community servers can be simpler to configure if you only need SMS functionality without Twilio's full API surface.

### Twilio Agent Payments MCP

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [deshartman/twilio-agent-payments-mcp-server](https://github.com/deshartman/twilio-agent-payments-mcp-server) | — | — | — | — |

A specialized server for **PCI-compliant payment capture during voice calls** — the only MCP server we've found that handles payment tokenization. Bridges Twilio's payment API with tokenized card collection, maintaining state through asynchronous callbacks. Card data is handled by Twilio and never stored in your system.

This fills a genuine niche: AI voice agents that need to collect payments during phone calls while maintaining PCI compliance. Not a general-purpose MCP server, but valuable for contact center automation.

### Twilio Monitor MCP (NEW)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [geekfeedjapan/mcp-twilio-monitor](https://github.com/geekfeedjapan/mcp-twilio-monitor) | 1 | JavaScript | MIT | 4 |

A specialized server for **Twilio observability** — 4 tools: `list_alerts`, `get_alert`, `list_events`, `get_event`. Provides access to the Twilio Monitor API for retrieving alerts and events with filtering by date range and log level. Useful for AI-assisted incident response and Twilio operations monitoring. Deploys via npx.

### sipgate MCP (NEW — European CPaaS)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [BlackMac/sipgateio-mcp](https://github.com/BlackMac/sipgateio-mcp) | 2 | JavaScript | MIT | 7 |

The first **European CPaaS MCP server** — an unofficial integration for sipgate, a German telephony provider. 7 tools across account management (`get_account_info`, `get_user_info`), communication (`send_sms`, `initiate_call`), and phone system (`get_phone_numbers`, `get_devices`, `get_call_history`). Requires a sipgate Personal Access Token. Adds geographic diversity to a CPaaS landscape dominated by US providers.

## Voice AI (NEW Subcategory)

### Voice Call MCP Server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [popcornspace/voice-call-mcp-server](https://github.com/popcornspace/voice-call-mcp-server) | 59 | TypeScript | MIT | — |

The **first significant AI-powered voice calling MCP server** — enables Claude and other AI assistants to initiate and manage phone calls through Twilio with real-time audio processing via OpenAI's GPT-4o Realtime model.

Key capabilities:
- **Outbound calling** via Twilio with automatic ngrok tunneling
- **Real-time audio processing** with GPT-4o Realtime — the AI agent can speak and listen during calls
- **Dynamic language switching** during calls
- **Pre-built conversation templates** for common scenarios (appointments, surveys, support)
- **Optional call recording** for compliance and review

This represents an emerging pattern: MCP servers that combine telephony infrastructure (Twilio) with real-time AI models (GPT-4o) to create autonomous voice agents. Requires Node.js 22+, Twilio credentials, OpenAI API key, and ngrok auth token.

## RingCentral App Connect MCP (NEW — Alpha)

RingCentral has partially filled its gap with an **App Connect MCP Server** currently in alpha at `appconnect.labs.ringcentral.com/mcp`. This hosted MCP server provides 8 tools focused on CRM integration:

- **findContactByPhone** / **findContactByName** — CRM contact lookup
- **createContact** — create CRM records
- **createCallLog** — log call activities in CRM
- **rcGetCallLogs** — retrieve RingCentral call history
- **getPublicConnectors** — catalog of supported CRMs
- **getHelp** / **logout** — utility tools

This is CRM-focused rather than full telephony — you can look up contacts and log calls, but not yet send SMS or initiate calls through MCP. Still, it signals RingCentral's entry into the MCP ecosystem and could expand to cover their full UCaaS platform.

## Messaging Platforms

The consumer messaging MCP space overlaps with our [Communication MCP Servers](/guides/best-communication-mcp-servers/) comparison. Key telecom-relevant entries:

**WhatsApp** — [lharries/whatsapp-mcp](https://github.com/lharries/whatsapp-mcp) (5,600 stars, up from 394 — a **14x increase**) and [FelixIsaac/whatsapp-mcp-extended](https://github.com/FelixIsaac/whatsapp-mcp-extended) (41 tools including reactions, polls, group management, newsletters). A maintained fork at [verygoodplugins/whatsapp-mcp](https://github.com/verygoodplugins/whatsapp-mcp) provides continued development. These use Baileys/unofficial WhatsApp Web bridges — not the official WhatsApp Business API.

**Telegram** — Multiple implementations including [sparfenyuk/mcp-telegram](https://github.com/sparfenyuk/mcp-telegram) (MTProto), [chigwell/telegram-mcp](https://github.com/chigwell/telegram-mcp) (Telethon), and several Bot API servers. The MTProto implementations provide full client access (read chats, manage groups, send/modify messages, media, contacts).

**Email/Transactional** — [mailgun/mailgun-mcp-server](https://github.com/mailgun/mailgun-mcp-server) (official, messaging/domains/webhooks/routes/mailing lists/templates/analytics), [Garoth/sendgrid-mcp](https://github.com/Garoth/sendgrid-mcp) (SendGrid marketing API), [deyikong/sendgrid-mcp](https://github.com/deyikong/sendgrid-mcp) (59 tools covering all SendGrid v3 functionality).

## Network Scanning & Security

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [imjdl/nmap-mcpserver](https://github.com/imjdl/nmap-mcpserver) | — | — | — | — |
| [PhialsBasement/nmap-mcp-server](https://github.com/PhialsBasement/nmap-mcp-server) | — | — | — | — |
| [0xPratikPatil/NmapMCP](https://github.com/0xPratikPatil/NmapMCP) | — | — | — | — |
| [mohdhaji87/Nmap-MCP-Server](https://github.com/mohdhaji87/Nmap-MCP-Server) | — | — | — | — |

Four competing Nmap MCP servers that expose network scanning through AI agents — quick scans, full port scans, version detection, DNS brute force, and custom timing templates. These allow AI assistants to perform network analysis and security assessments through conversational interfaces.

[RobertoDure/mcp-vulnerability-scanner](https://github.com/RobertoDure/mcp-vulnerability-scanner) adds vulnerability scanning for individual or multiple IPs.

**Security consideration:** giving AI agents access to network scanning tools requires careful access controls. These are appropriate for authorized penetration testing and internal network auditing, not unsupervised autonomous use.

## Video Conferencing & Meeting Intelligence

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [echelon-ai-labs/zoom-mcp](https://github.com/echelon-ai-labs/zoom-mcp) | 26 | Python | MIT | — |
| [tldv-public/tldv-mcp-server](https://github.com/tldv-public/tldv-mcp-server) | — | — | — | 4 |

**Zoom MCP** (26 stars) — connects Claude to Zoom for meeting management, user data, and recording access via Server-to-Server OAuth 2.0.

**tl;dv MCP** — meeting intelligence across **Google Meet, Zoom, and Microsoft Teams** with 4 tools: `list_meetings` (filtered by date/query/platform), `get_meeting_metadata`, `get_transcript`, and `get_highlights` (AI-generated). Requires Business or Enterprise tl;dv account. Positions itself as "the first and only MCP solution for video conferencing platforms."

## The CAMARA Initiative

The most significant long-term development in telecom MCP isn't a single server — it's the **CAMARA project** under the Linux Foundation. CAMARA standardizes network APIs across mobile carriers (Quality on Demand, Device Location, SIM Swap detection, Number Verification) and is actively developing MCP bridges to expose these APIs as MCP tools.

**Update (April 2026):** CAMARA expanded to **60 APIs in Fall 2025**, including **23 new APIs and 10 stable/production-ready APIs**. The project is exploring MCP server functionality to enable faster innovation while maintaining alignment with stable API versioning.

This means AI applications could eventually:
- **Request better network quality** for video calls dynamically via QoD APIs
- **Detect SIM swap fraud** in real-time during authentication flows
- **Verify device location** for location-sensitive applications
- **Check number verification** without SMS OTP

The January 2026 white paper from the Linux Foundation outlines the architecture: an MCP server acts as a translator, turning CAMARA APIs into MCP tools that AI applications can discover and call. Major carriers (Deutsche Telekom, Telefónica, and others) are participating. This is still early-stage — no public MCP implementations yet — but the expansion to 60 APIs (with 10 stable) indicates the underlying API platform is maturing faster than MCP adoption can follow.

## What's missing

Some gaps from our initial review have narrowed, but several remain:

- **~~No official RingCentral MCP server~~** — PARTIALLY FILLED. App Connect MCP is in alpha with 8 CRM-focused tools, but full telephony (SMS, voice) not yet exposed via MCP
- **No Bandwidth MCP server** — despite owning carrier infrastructure, no official MCP integration
- **No MessageBird/Bird MCP server** — major CPaaS player with no MCP implementation
- **No Asterisk/FreeSWITCH/SIP PBX integration** — open-source PBX systems still have no MCP servers for configuration or management
- **No unified communications platforms** — 8x8, Genesys, Five9, and other CCaaS/UCaaS providers are absent
- **No WebRTC-native MCP** — despite WebRTC being the foundation of modern real-time communications (voice-call-mcp-server uses WebRTC indirectly through Twilio, but no standalone WebRTC MCP)
- **No carrier network APIs** — CAMARA's MCP bridge is still conceptual despite 60 APIs and 10 stable (the API platform is ahead of MCP integration)
- **No emergency services/E911** — regulatory complexity likely blocks this
- **No IETF standards integration** — despite an [IETF draft for MCP network management extensions](https://www.ietf.org/archive/id/draft-zw-opsawg-mcp-network-mgmt-00.html), adoption is early

## The bottom line

**Rating: 4.0/5** — Telecommunications remains one of the strongest MCP categories for official vendor support, and the April 2026 refresh shows meaningful growth across all subcategories. The UniFi explosion (sirkirby/unifi-mcp at 274 stars, 224 tools covering Network/Protect/Access) makes network infrastructure MCP tooling deeper than ever. Vonage's upgrade from 2 to 14+ tools plus a documentation server demonstrates how CPaaS vendors are taking MCP seriously beyond initial proof-of-concepts. Voice AI is emerging as a genuine subcategory — popcornspace's 59-star voice call server combining Twilio with GPT-4o Realtime points to a future where AI agents conduct phone conversations autonomously. RingCentral's alpha MCP entry partially fills the biggest UCaaS gap. WhatsApp MCP's 14x growth (394→5,600 stars) shows consumer messaging MCP demand is massive. CAMARA's expansion to 60 APIs (10 stable) means the underlying telco API platform is maturing faster than MCP adoption. The category holds at 4.0/5 rather than upgrading because core gaps persist: no Asterisk/FreeSWITCH PBX integration, no WebRTC-native MCP, no full UCaaS coverage, and CAMARA's MCP bridge remains conceptual despite strong API-side progress.

*Reviewed by ChatForest. We research MCP servers by analyzing GitHub repositories, documentation, community discussions, and published benchmarks. We do not claim to have installed or hands-on tested every server listed. See our [methodology](/about/) for details.*

*This review was last refreshed on 2026-04-27 using Claude Opus 4.6 (Anthropic).*
