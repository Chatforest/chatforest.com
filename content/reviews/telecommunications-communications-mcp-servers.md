---
title: "Telecommunications & Communications MCP Servers — Twilio, Telnyx, Vonage, Sinch, Plivo, Cisco Meraki, NetBox, and More"
date: 2026-03-15T18:00:00+09:00
description: "Telecommunications and communications MCP servers are giving AI agents the ability to send SMS, make phone calls, manage network infrastructure, and orchestrate multi-channel messaging. We reviewed 40+ servers across 6 subcategories. CPaaS Platforms: twilio-labs/mcp (96 stars, TypeScript, MIT — official, exposes entire Twilio API catalog via OpenAPI-to-MCP generator), Telnyx MCP (24 stars, Python, official — 8 tool categories covering calls/SMS/phone numbers/AI assistants/cloud storage, archived in favor of TypeScript rewrite), sinch/sinch-mcp-server (TypeScript, official — 23 tools across conversation/email/verification/voice/config), plivo/mcp (Python — 6 tools for SMS/calls/applications/endpoints/CDR/MDR). Network Infrastructure: pamosima/network-mcp-docker-suite (25 stars, Python — 10 MCP servers for Cisco Meraki/Catalyst Center/IOS XE/ISE/ThousandEyes/Splunk/NetBox/Prometheus/ClickHouse/GitLab), netboxlabs/netbox-mcp-server (127 stars, Python, Apache-2.0 — 3 tools for DCIM/IPAM read-only access with 90% token reduction via field filtering), CiscoDevNet/meraki-magic-mcp-community (17 stars, Python — dynamic mode with 804 API endpoints or curated 40 endpoints). Community SMS/Voice: YiyangLi/sms-mcp-server (12 stars, JavaScript, MIT — Twilio SMS/MMS), deshartman/twilio-messaging-mcp-server (5 stars — Twilio messaging tools/resources/prompts), deshartman/twilio-agent-payments-mcp-server (PCI-compliant payment capture during voice calls). Messaging Platforms: WhatsApp MCP (394+ stars across implementations), Telegram MCP (multiple implementations via MTProto and Bot API). Network Scanning: 4+ Nmap MCP servers for AI-driven network analysis. Video Conferencing: Zoom MCP, tl;dv MCP (Google Meet/Zoom/Teams meeting intelligence). Rating: 4.0/5."
og_description: "Telecom & communications MCP servers: Twilio official (96 stars, full API), NetBox (127 stars, DCIM/IPAM), Cisco Meraki (17 stars, 804 endpoints), Telnyx (24 stars, 8 categories), Sinch (23 tools), Plivo (6 tools), WhatsApp (394+ stars), network scanning (Nmap). Rating: 4.0/5."
content_type: "Review"
card_description: "Telecommunications and communications MCP servers for CPaaS platforms, network infrastructure management, SMS/voice, messaging, and video conferencing. This category stands out for strong official vendor participation — Twilio, Telnyx, Sinch, Vonage, and Plivo all have official or vendor-community MCP servers, making it one of the best-supported MCP categories by established companies. Twilio's official MCP server (96 stars) is the clear leader — it dynamically exposes Twilio's entire public API catalog through an OpenAPI-to-MCP generator, giving AI agents access to SMS, voice, video, email (SendGrid), and more through configurable service/tag filters. NetBox's MCP server (127 stars) is the most popular network infrastructure MCP server — read-only access to DCIM and IPAM data with field filtering that reduces API response size by up to 90%, making it highly token-efficient. Cisco's Network MCP Docker Suite (25 stars) is architecturally impressive — 10 containerized MCP servers covering Meraki, Catalyst Center, IOS XE, ISE, ThousandEyes, Splunk, NetBox, Prometheus, ClickHouse, and GitLab, providing unified AI-driven network operations. Sinch's official server provides 23 tools across conversation, email, verification, and voice — the most feature-complete multi-channel communications MCP. The CAMARA project (Linux Foundation) is developing MCP bridges for standardized telco APIs — Quality on Demand, Device Location, SIM Swap detection — potentially transforming how AI agents interact with 5G network capabilities. Major gaps: no official RingCentral, Bandwidth, or MessageBird/Bird MCP servers; no Asterisk/FreeSWITCH/SIP PBX integration; no unified communications platforms (8x8, Genesys); limited carrier network APIs (CAMARA is early-stage); no WebRTC-native MCP servers. The category earns 4.0/5 — exceptional official vendor support from major CPaaS providers, strong network infrastructure tooling, and the CAMARA initiative signals a future where AI agents can directly negotiate network quality with carriers."
last_refreshed: 2026-03-15
---

Telecommunications and communications MCP servers are giving AI agents the power to send messages, make phone calls, manage network infrastructure, and orchestrate multi-channel communications — all through natural language. Instead of writing custom integrations for each provider, an AI agent can discover and use Twilio's SMS API, check Cisco Meraki network health, or send a WhatsApp message through a standardized MCP interface.

The landscape spans six areas: **CPaaS platforms** (Twilio, Telnyx, Sinch, Vonage, Plivo — official vendor servers), **network infrastructure** (Cisco Meraki, NetBox, Catalyst Center, UniFi), **community SMS/voice** (focused Twilio wrappers for messaging and payments), **messaging platforms** (WhatsApp, Telegram), **network scanning and security** (Nmap, vulnerability scanning), and **video conferencing** (Zoom, tl;dv meeting intelligence).

The headline findings: **Official vendor participation is exceptional** — Twilio, Telnyx, Sinch, Vonage, and Plivo all have official MCP servers, making telecom one of the best vendor-supported MCP categories. **Twilio's official server is the most comprehensive** — it dynamically generates MCP tools from Twilio's entire OpenAPI spec. **NetBox leads network infrastructure** at 127 stars with token-efficient read-only DCIM/IPAM access. **Cisco's Docker Suite bundles 10 MCP servers** for unified AIOps across Meraki, Catalyst Center, IOS XE, and observability tools. **CAMARA (Linux Foundation) is building MCP bridges to 5G network APIs** — Quality on Demand, Device Location, SIM Swap detection — potentially the most transformative development in this space. Part of our **[Communication & Collaboration MCP category](/categories/communication-collaboration/)**.

## CPaaS Platforms (Official Vendor Servers)

### Twilio MCP (Official)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [twilio-labs/mcp](https://github.com/twilio-labs/mcp) | 96 | TypeScript | MIT | Dynamic (full API) |

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

Supports tool filtering via environment variables and includes a webhook receiver with ngrok tunnel for real-time event handling. **Note:** This Python version was archived September 2025 — Telnyx recommends migrating to a newer TypeScript implementation. Still useful as a reference for the breadth of what a telecom MCP server can expose.

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

### Vonage Telephony MCP (Community-Official)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [Vonage-Community/telephony-mcp-server](https://github.com/Vonage-Community/telephony-mcp-server) | 1 | Python | MIT | 2 |

A deliberately minimal server from Vonage's community organization — **2 tools: voice call and SMS**. Uses Vonage API for calls, SMS, speech-to-text, and speech recognition.

Includes a callback server on port 8080 for receiving Vonage event notifications, Docker Compose deployment, and compatibility with Claude Desktop and GitHub Copilot. The simplicity is the point — this is a starting template for building more complex telephony integrations, not a full-featured production server.

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

### Network MCP Docker Suite (Cisco)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [pamosima/network-mcp-docker-suite](https://github.com/pamosima/network-mcp-docker-suite) | 25 | Python | — | 10 servers |

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
| [netboxlabs/netbox-mcp-server](https://github.com/netboxlabs/netbox-mcp-server) | 127 | Python | Apache-2.0 | 3 |

The **most popular network infrastructure MCP server** by a significant margin. Provides read-only access to NetBox — the leading open-source DCIM/IPAM platform — through 3 focused tools:

- **get_objects** — retrieve devices, IP addresses, interfaces, sites, and other NetBox objects with filtering
- **get_object_by_id** — detailed information for specific objects
- **get_changelogs** — audit trail and change history

The standout feature is **token optimization**: field filtering reduces API response size by up to 90%, with pre-defined "common field patterns" for devices, IPs, interfaces, and sites. This matters because LLM context windows are expensive, and network infrastructure queries can return massive payloads.

Supports stdio and HTTP transports, Docker deployment, and flexible configuration via environment variables, `.env` files, and CLI arguments. Recently hit v1.0.0 with improved project structure.

### Meraki Magic MCP (Cisco DevNet)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [CiscoDevNet/meraki-magic-mcp-community](https://github.com/CiscoDevNet/meraki-magic-mcp-community) | 17 | Python | — | 12-804 |

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

## Messaging Platforms

The consumer messaging MCP space overlaps with our [Communication MCP Servers](/guides/best-communication-mcp-servers/) comparison. Key telecom-relevant entries:

**WhatsApp** — [lharries/whatsapp-mcp](https://github.com/lharries/whatsapp-mcp) (394+ stars) and [FelixIsaac/whatsapp-mcp-extended](https://github.com/FelixIsaac/whatsapp-mcp-extended) (41 tools including reactions, polls, group management, newsletters). These use Baileys/unofficial WhatsApp Web bridges — not the official WhatsApp Business API.

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
| [echelon-ai-labs/zoom-mcp](https://github.com/echelon-ai-labs/zoom-mcp) | — | — | — | — |
| [tldv-public/tldv-mcp-server](https://github.com/tldv-public/tldv-mcp-server) | — | — | — | — |

**Zoom MCP** — connects Claude to Zoom for meeting management, user data, and recording access via the Zoom API.

**tl;dv MCP** — the more interesting implementation, providing meeting intelligence across **Google Meet, Zoom, and Microsoft Teams**. Accesses meeting transcripts, recordings, and insights through a unified interface. Positions itself as "the first and only MCP solution for video conferencing platforms."

## The CAMARA Initiative

The most significant development in telecom MCP isn't a single server — it's the **CAMARA project** under the Linux Foundation. CAMARA standardizes network APIs across mobile carriers (Quality on Demand, Device Location, SIM Swap detection, Number Verification) and is actively developing MCP bridges to expose these APIs as MCP tools.

This means AI applications could eventually:
- **Request better network quality** for video calls dynamically via QoD APIs
- **Detect SIM swap fraud** in real-time during authentication flows
- **Verify device location** for location-sensitive applications
- **Check number verification** without SMS OTP

The January 2026 white paper from the Linux Foundation outlines the architecture: an MCP server acts as a translator, turning CAMARA APIs into MCP tools that AI applications can discover and call. Major carriers (Deutsche Telekom, Telefónica, and others) are participating. This is still early-stage — no public MCP implementations yet — but it represents a potential paradigm shift where AI agents can directly negotiate with carrier networks.

## What's missing

The gaps are notable:

- **No official RingCentral MCP server** — one of the largest UCaaS providers with no MCP presence
- **No Bandwidth MCP server** — despite owning carrier infrastructure, no official MCP integration
- **No MessageBird/Bird MCP server** — major CPaaS player with no MCP implementation
- **No Asterisk/FreeSWITCH/SIP PBX integration** — open-source PBX systems have no MCP servers for configuration or management
- **No unified communications platforms** — 8x8, Genesys, Five9, and other CCaaS/UCaaS providers are absent
- **No WebRTC-native MCP** — despite WebRTC being the foundation of modern real-time communications
- **No carrier network APIs** — CAMARA's MCP bridge is conceptual, not deployed
- **No emergency services/E911** — regulatory complexity likely blocks this
- **No IETF standards integration** — despite an [IETF draft for MCP network management extensions](https://www.ietf.org/archive/id/draft-zw-opsawg-mcp-network-mgmt-00.html), adoption is early

## The bottom line

**Rating: 4.0/5** — Telecommunications is one of the strongest MCP categories for official vendor support. Having Twilio, Telnyx, Sinch, Vonage, and Plivo all providing official servers is remarkable — most categories are lucky to have one or two vendor-backed implementations. Twilio's OpenAPI-to-MCP generator approach is architecturally elegant and could serve as a model for other companies with large API surfaces. Network infrastructure tooling is solid, with NetBox (127 stars) providing token-efficient DCIM/IPAM access and Cisco's Docker Suite enabling unified AIOps across 10 platforms. The CAMARA initiative could be transformative — if AI agents can eventually negotiate network quality with carriers through MCP, it fundamentally changes how applications interact with telecom infrastructure. The category loses a point for gaps in UCaaS (no RingCentral, no 8x8), PBX systems (no Asterisk/FreeSWITCH), and the still-conceptual nature of carrier network API access.

*Reviewed by ChatForest. We research MCP servers by analyzing GitHub repositories, documentation, community discussions, and published benchmarks. We do not claim to have installed or hands-on tested every server listed. See our [methodology](/about/) for details.*

*This review was last edited on 2026-03-16 using Claude Opus 4.6 (Anthropic).*
