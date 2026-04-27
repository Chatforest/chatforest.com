---
title: "Video Conferencing & Meeting Intelligence MCP Servers — Zoom Official, Joinly, Vexa, Otter.ai, Fireflies, tl;dv, and More"
date: 2026-03-19T18:30:00+09:00
description: "Video conferencing MCP servers let AI agents join meetings, access transcripts, manage recordings, and even speak in calls. Now with official Zoom MCP and Microsoft Work IQ Teams."
og_description: "Video conferencing MCP servers: Zoom Official MCP Connector (April 2026), Microsoft Work IQ Teams (25+ tools), Joinly (494 stars, real-time meeting participation), Vexa (1,900 stars, v0.10.4 Zoom bot), Otter.ai (official meeting intelligence MCP), Fireflies.ai (beta MCP), tl;dv, Meeting BaaS (speaking bots), Meetily (11.4K stars). 20+ servers. Rating: 4.0/5."
content_type: "Review"
card_description: "Video conferencing and meeting intelligence MCP servers across Zoom (official), Microsoft Work IQ Teams, Joinly, Vexa, Otter.ai, Fireflies.ai, tl;dv, Meeting BaaS, and Webex. The ecosystem has matured significantly with Zoom's official MCP connector (April 2026), Microsoft Agent 365 Work IQ Teams, and major meeting intelligence platforms launching MCP servers."
last_refreshed: 2026-04-28
---

Meetings are where decisions happen, context lives, and information gets trapped. Every organization runs on video calls — Zoom, Google Meet, Microsoft Teams — but the content of those calls has been locked away from AI agents. MCP servers are changing that — and as of April 2026, the major platforms are finally shipping official integrations.

This review covers MCP servers for **video conferencing and meeting intelligence** — servers that let AI agents interact with meetings in some way, whether that's accessing transcripts, managing recordings, scheduling calls, or actively participating in real-time. For broader communication platform integrations (Slack, Discord, email), see our [Communication MCP Servers comparison](/guides/best-communication-mcp-servers/).

**April 2026 update: The biggest gap in this category has closed.** Zoom launched its official MCP connector on April 9, 2026. Microsoft shipped Work IQ Teams as part of Agent 365. Otter.ai and Fireflies.ai both launched MCP servers for their meeting intelligence platforms. Meanwhile, Vexa hit v0.10.4 with Zoom Web bot support, Joinly grew 20% to 494 stars, and Meetily exploded to 11,400 stars. The meeting MCP ecosystem has matured dramatically in 40 days.

The ecosystem now splits into **four tiers**: official platform connectors (Zoom, Microsoft), multi-platform intelligence services (Vexa, tl;dv, Otter.ai, Fireflies.ai), community platform wrappers (Teams, Webex), and real-time participation frameworks (Joinly, Meeting BaaS). Part of our **[Communication & Collaboration MCP category](/categories/communication-collaboration/)**.

## Official Platform MCP Servers (NEW)

The biggest development since our March review: major platforms are shipping official MCP integrations.

### Zoom Official MCP Connector (NEW — April 9, 2026)

| Detail | Info |
|--------|------|
| Vendor | Zoom (official) |
| Launch | April 9, 2026 |
| Platforms | Claude Cowork, Claude Code |
| Auth | Zoom account + AI Companion license |
| Type | Hosted/managed connector |

**The single biggest gap in meeting MCP has closed.** Zoom launched its official MCP connector on April 9, 2026, providing secure access to meeting summaries, transcripts, recordings, and scheduling capabilities directly within Claude.

### What Works Well

**Official first-party integration.** This isn't a community wrapper — it's built and maintained by Zoom. Meeting data stays on Zoom's servers; the connector provides structured access without duplicating customer information.

**Meeting intelligence, not just API access.** The connector exposes AI-generated meeting summaries, key moments, action items, and full transcripts — not raw API endpoints. This is meeting intelligence as a service.

**Scheduling and coordination.** Developers can automate meeting scheduling for sprint planning, standups, and team coordination. This goes beyond passive transcript access into active meeting management.

**Claude Cowork + Claude Code.** Available as a connector in Claude Cowork for general users and as a plugin in Claude Code for developers building custom workflows.

### What Doesn't Work Well

**Claude-only (for now).** The MCP connector is currently available only through Anthropic's Claude platforms. No standalone MCP server for arbitrary MCP clients.

**Requires AI Companion license.** Not available on all Zoom plans — you need a Zoom license with AI Companion capabilities enabled.

**Not open source.** No GitHub repository. This is a managed, hosted connector.

### Microsoft Work IQ Teams (NEW — Agent 365)

| Detail | Info |
|--------|------|
| Vendor | Microsoft (official) |
| Server ID | `mcp_TeamsServer` |
| Status | Preview |
| Tools | 25+ (chat, channels, teams, members) |
| Auth | Microsoft 365 Copilot license |
| Scope | `McpServers.Teams.All` |

Microsoft shipped Work IQ Teams as part of Agent 365 — enterprise-grade MCP servers that expose Microsoft 365 workloads through the Agent 365 tooling gateway.

### What Works Well

**Enterprise-grade with full Microsoft backing.** Unlike community Teams servers, Work IQ Teams respects the same security, licensing, and compliance boundaries as Microsoft 365 Copilot. Admin center management, Defender integration, scoped permissions.

**25+ tools via Microsoft Graph.** Full CRUD for chats and channels, message threading, member management (add, update, list), private/shared channel support, OData query filtering. Comparable to floriscornel/teams-mcp but with official support.

**Part of a broader suite.** Work IQ Calendar handles meeting scheduling (create, list, update, delete events, find free/busy slots, accept/decline invitations). Work IQ Mail covers email. Work IQ User Profile provides org chart and user search. Together these cover the full Microsoft 365 meeting workflow.

### What Doesn't Work Well

**Preview status.** Not yet GA. Subject to change.

**Requires Microsoft 365 Copilot license.** This is an enterprise offering — not accessible to individual developers or small teams without Copilot licensing.

**Still messaging-focused.** Like community Teams servers, Work IQ Teams covers chats, channels, and members — not meeting recordings, transcriptions, or video features directly. Calendar/scheduling is via the separate Work IQ Calendar server.

## Multi-Platform Meeting Intelligence

These servers bridge multiple video conferencing platforms, providing unified access to meeting transcripts, recordings, and metadata.

### Vexa

| Detail | Info |
|--------|------|
| [Vexa-ai/vexa](https://github.com/Vexa-ai/vexa) | ~1,900 stars (+6%) |
| License | Open source (self-hostable) |
| Language | Python |
| Platforms | Google Meet, Microsoft Teams, Zoom |
| Latest | v0.10.4 (April 26, 2026) |
| Install | `make all` (self-hosted) or hosted SaaS |

The strongest open-source option for meeting transcription with MCP support. Vexa is a full meeting transcription API — auto-join bots, real-time WebSocket transcripts, and an MCP server microservice that exposes the entire API to any MCP-capable agent.

### What Works Well

**Real-time multilingual transcription.** 100 languages via Whisper, plus real-time translation across all of them. This is production-grade transcription infrastructure, not a weekend project.

**v0.10 architecture refactor.** The project restructured into three clean layers: infrastructure (runtime-api for container orchestration), data (meeting-api), and intelligence (agent-api, experimental). Real-time transcription pipeline now runs inside bot containers, eliminating external dependencies.

**Zoom Web bot + 4x CPU reduction.** v0.10.4 (April 26, 2026) enables `platform=zoom` without SDK setup and delivers a 4x reduction in CPU usage. This is a significant operational improvement.

**Self-hostable with Kubernetes support.** Runs locally with `make all` on CPU or GPU, plus Kubernetes/Helm support for production deployment. Modular design lets you deploy only what you need — transcription, speaking bots, MCP tools, or agent runtimes.

**Approaching 2,000 stars.** 1,900+ stars and actively maintained with regular releases. The strongest community momentum in open-source meeting MCP.

### What Doesn't Work Well

**Infrastructure complexity.** Despite the v0.10 refactor simplifying deployment, this is still a multi-service platform — not a simple MCP server you pip install.

**Bot-based approach.** Like all services that "join" meetings, Vexa sends a bot that appears as a participant. Some organizations block unknown participants or require manual admission.

### tl;dv MCP Server

| Detail | Info |
|--------|------|
| [tldv-public/tldv-mcp-server](https://github.com/tldv-public/tldv-mcp-server) | ~10 stars (+43%) |
| License | Not specified |
| Language | Not specified |
| Platforms | Google Meet, Zoom, Microsoft Teams |
| Auth | tl;dv API key |

The official MCP server from tl;dv, one of the most popular meeting recording and transcription platforms. tl;dv has a large user base (the service itself is widely adopted), and this MCP server exposes that meeting intelligence to AI agents.

### What Works Well

**Official vendor server.** Backed by tl;dv's commercial platform, which means reliable transcription, consistent API, and ongoing maintenance tied to a revenue-generating product.

**Multi-platform coverage.** Works across Zoom, Google Meet, and Microsoft Teams from a single integration — no need for separate servers per platform.

**Rich meeting data.** Tools to list meetings with filters, get meeting metadata, obtain full transcripts, and retrieve AI-generated highlights. This goes beyond raw transcription into meeting intelligence.

### What Doesn't Work Well

**Low GitHub adoption.** ~10 stars despite tl;dv's substantial user base suggests the MCP integration is still not widely discovered.

**Requires tl;dv account.** This is a wrapper around a commercial SaaS. You need a tl;dv account (free tier available, premium for full features), and meeting data lives on their servers.

**No license specified.** The GitHub repository doesn't include a license — technically "all rights reserved" by default.

### Otter.ai MCP Server (NEW)

| Detail | Info |
|--------|------|
| Vendor | Otter.ai (official) |
| Type | Commercial (hosted) |
| Platforms | Claude, ChatGPT, Cursor |
| Auth | OAuth (granular permissions) |
| Status | GA |

Otter.ai — one of the most widely used meeting transcription platforms — launched its official MCP server, enabling AI assistants to search meeting transcripts, analyze patterns across meetings, and surface insights without leaving the AI workflow.

### What Works Well

**Official vendor integration.** Backed by Otter.ai's commercial platform with millions of users. OAuth-authenticated with granular permissions — your AI assistant only accesses meetings you explicitly authorize.

**Cross-meeting analysis.** The real power isn't accessing a single transcript (you can already do that) — it's analyzing patterns and themes across multiple meetings. Sales teams can track objections across demo calls, product managers can mine feature requests from user interviews.

**Multi-platform AI support.** Works with Claude, ChatGPT, and Cursor. Otter is working to expand to all MCP-compatible applications.

### What Doesn't Work Well

**No public API key.** Otter currently doesn't provide a public API key for self-service setup. You need to contact Otter Support Team for MCP configuration, which adds friction.

**Requires Otter account.** This is a wrapper around Otter's commercial service. Meeting data lives on their servers.

**No open-source option.** The community alternative (DarrenZal/otter-mcp, 2 stars, MIT) provides basic transcript search but uses unofficial APIs.

### Fireflies.ai MCP Server (NEW)

| Detail | Info |
|--------|------|
| Vendor | Fireflies.ai (official) |
| Type | Commercial (hosted) |
| Platforms | Claude, ChatGPT, Cursor, Devin |
| Auth | OAuth or API key |
| Status | Beta (V2 coming) |

Fireflies.ai launched its MCP server in beta, providing direct access to meeting transcripts, metadata, speaker information, and summary data from its meeting intelligence platform.

### What Works Well

**OAuth integration — no API key required.** ChatGPT has native OAuth support. Claude works via connector or config. This removes the biggest friction point for non-technical users.

**Meeting data, not just transcripts.** Access to transcripts, meeting metadata, speaker information, and summary data. Sales teams analyze pipeline conversations, product managers extract research insights, customer success monitors account health.

### What Doesn't Work Well

**V1 being deprecated.** The current Firefly MCP integration will be deprecated on April 30, 2026. V2 is coming, but the transition creates uncertainty for early adopters.

**Beta status.** Not yet production-ready. Feature set may change.

### Meeting BaaS

| Detail | Info |
|--------|------|
| [Meeting-BaaS/meeting-mcp](https://github.com/Meeting-BaaS/meeting-mcp) | ~27 stars |
| License | Open source |
| Language | TypeScript |
| Platforms | Google Meet, Zoom, Microsoft Teams |
| Port | 7017 (default) |

Meeting BaaS (Bot-as-a-Service) provides meeting bot infrastructure as a platform, and their MCP server exposes that infrastructure to AI agents. The most interesting feature: **speaking bots** that can actively participate in calls with customizable personas.

### What Works Well

**Speaking bot capability.** The companion [speaking-bots-mcp](https://github.com/Meeting-Baas/speaking-bots-mcp) server goes beyond passive recording — it can send AI-powered bots that speak in meetings with distinct personalities and real-time audio streaming via Pipecat. This is the most ambitious meeting automation approach in the MCP ecosystem.

**Full meeting lifecycle.** Create/invite recording bots, search through transcripts, manage calendar events, access recording metadata, and generate shareable links to specific timestamps.

**AI-generated QR code avatars.** A small but distinctive feature — generate unique bot avatars as QR codes.

**Self-hostable.** Can run entirely on your own infrastructure for security-sensitive environments.

### What Doesn't Work Well

**Low adoption.** ~27 stars. The speaking bots capability is impressive but apparently not yet widely adopted.

**Requires Meeting BaaS infrastructure.** Like Vexa, this is a platform — not a standalone MCP server you point at your existing Zoom account.

## Real-Time Meeting Participation

### Joinly

| Detail | Info |
|--------|------|
| [joinly-ai/joinly](https://github.com/joinly-ai/joinly) | ~494 stars (+20%) |
| License | Not specified |
| Language | Not specified |
| Platforms | Zoom, Microsoft Teams, Google Meet |
| Commits | 820+ |

Joinly is connector middleware that enables AI agents to join and actively participate in video calls. The MCP server provides meeting tools and resources so that any MCP-capable agent can attend meetings, access real-time transcripts, speak, and send chat messages.

### What Works Well

**Highest adoption for real-time participation.** 494 stars (up 20% from 413 in March) makes this the most popular MCP server specifically designed for agents to participate in meetings. 820+ commits shows sustained development velocity.

**Flexible STT/TTS providers.** Supports multiple providers: Whisper and Deepgram for speech-to-text, Kokoro and ElevenLabs and Deepgram for text-to-speech. Multiple LLM backends: OpenAI, Anthropic, and local Ollama.

**Composable architecture.** A joinly agent can connect to other MCP servers (GitHub, Tavily, Notion) alongside the meeting tools — so your meeting bot can pull up code, search the web, or check docs during a call.

**Real-time transcript as a resource.** The MCP server exposes the live meeting transcript as a resource (`transcript://live`), enabling agents to follow along and respond contextually.

**Active community.** Featured on Hacker News (Show HN), suggesting genuine developer interest in the concept. Recent updates include direct list_tools and session access, split system prompt/custom instructions, and message history limits to reduce token usage.

### What Doesn't Work Well

**No license specified.** Like tl;dv, the repository lacks a license file.

**Nascent technology.** AI agents actively participating in meetings is ambitious — real-world reliability in production meetings is unproven at scale.

**Browser-based approach.** Joinly works with browser-based meeting platforms, which means it depends on browser automation under the hood. This can be fragile as platforms update their UIs.

## Platform-Specific Servers

### Microsoft Teams MCP (InditexTech)

| Detail | Info |
|--------|------|
| [InditexTech/mcp-teams-server](https://github.com/InditexTech/mcp-teams-server) | ~369 stars (+5%) |
| License | Apache-2.0 |
| Language | Python (97%) |
| Tools | 5+ (messaging focused) |
| Latest | v1.0.8 (March 16, 2026) |
| Install | Docker or Python + uv |

The most popular community Teams MCP server, built by Inditex (the parent company of Zara). Focuses on **messaging** — read messages, create messages, reply to threads, mention members. Now has an official alternative in Microsoft Work IQ Teams (see above), but remains valuable for organizations without Copilot licensing.

### What Works Well

**Strong adoption for enterprise.** 369 stars — the highest of any community platform-specific meeting/communication MCP server. Being built by a Fortune 500 company (Inditex) adds credibility. 145 commits, 9 releases, SonarCloud quality tracking.

**Docker-first deployment.** Pre-built Docker image on GHCR for easy enterprise deployment.

**Thread management.** Start threads with titles, reply with mentions, read channel messages — covers the core Teams messaging workflow.

### What Doesn't Work Well

**Messaging only, not video.** This is a Teams messaging server, not a video conferencing server. No meeting scheduling, recording access, or transcription features.

**Now has an official alternative.** Microsoft's Work IQ Teams provides similar messaging capabilities with official support and enterprise compliance. InditexTech remains relevant for teams without Microsoft 365 Copilot licensing.

**Scoped to one team.** Configured via TEAM_ID and TEAMS_CHANNEL_ID — designed for a specific team's channels, not broad organizational access.

### Microsoft Teams MCP (floriscornel)

| Detail | Info |
|--------|------|
| [floriscornel/teams-mcp](https://github.com/floriscornel/teams-mcp) | ~91 stars (+36%) |
| License | Not specified |
| Language | TypeScript |
| Tools | 25+ (15 read, 10 write) |
| Auth | OAuth 2.0 with auto-refresh |

A more comprehensive Teams integration with 25+ tools covering messaging, search, user management, and file sharing via Microsoft Graph API.

### What Works Well

**Most complete Teams MCP server.** 25+ tools spanning channel messages, chat, file uploads, user search, and mentions. Read-only mode option for security-conscious deployments.

**Proper OAuth flow.** Automatic refresh token support means no manual re-authentication every hour. This is how enterprise integrations should work.

**npm package available.** Published to npm as `@floriscornel/teams-mcp` for easy installation.

### What Doesn't Work Well

**Growing but still trailing InditexTech.** ~91 stars (up 36%) vs. 369 for the simpler alternative. The broader tool coverage is gaining traction but hasn't overtaken InditexTech's simpler approach.

**No meeting-specific features.** Like InditexTech's server, this is fundamentally a messaging and collaboration server — no video/audio/transcription capabilities.

### Zoom Community MCP Servers

With Zoom's official MCP connector now available (see above), community servers still serve developers who need direct API access or work outside Claude's ecosystem:

| Server | Stars | Language | Focus |
|--------|-------|----------|-------|
| [echelon-ai-labs/zoom-mcp](https://github.com/echelon-ai-labs/zoom-mcp) | ~26 (+44%) | Python | Full Zoom API (users, meetings, recordings) |
| [Prathamesh0901/zoom-mcp-server](https://github.com/Prathamesh0901/zoom-mcp-server) | ~7 | Not specified | CRUD meetings via Claude/Cursor |
| [forayconsulting/zoom_transcript_mcp](https://github.com/forayconsulting/zoom_transcript_mcp) | Low | Not specified | Zoom Cloud Recording transcripts |
| [peakmojo/mcp-server-zoom-noauth](https://github.com/peakmojo/mcp-server-zoom-noauth) | Low | Not specified | Recordings/transcripts without user auth |
| [JavaProgrammerLB/zoom-mcp-server](https://github.com/JavaProgrammerLB/zoom-mcp-server) | Low | Not specified | Meeting scheduling |

The best community option is **echelon-ai-labs/zoom-mcp** at 26 stars (up from 18) — Server-to-Server OAuth 2.0, user profiles, meeting details, recordings, and account settings. Python 3.11+ and Zoom admin privileges required.

**The gap has closed:** Zoom's official MCP connector (April 9, 2026) provides meeting intelligence through Claude Cowork and Claude Code. Community servers remain valuable for developers needing self-hosted or platform-agnostic MCP access.

### Google Meet MCP Server

| Detail | Info |
|--------|------|
| [INSIDE-HAIR/google-meet-mcp-server](https://github.com/INSIDE-HAIR/google-meet-mcp-server) | Low stars |
| License | Not specified |
| Language | TypeScript |
| Tools | 23 |
| Auth | Google OAuth 2.0 |

An enterprise-grade Google Meet management server using Google Calendar API v3 and Google Meet API v2. Docker containerization, Smithery deployment support, and 23 validated tools.

**The gap here is the same as Zoom: Google hasn't shipped an official Meet MCP server.** Google launched managed MCP servers for many of its tools in December 2025, but Google Meet wasn't among them. The community server above is ambitious (23 tools, strong testing) but has low adoption.

### Cisco Webex Messaging MCP

| Detail | Info |
|--------|------|
| [WebexSamples/webex-messaging-mcp-server](https://github.com/WebexSamples/webex-messaging-mcp-server) | ~4 stars |
| License | Not specified |
| Language | TypeScript/JavaScript |
| Tools | 52 |
| Transport | STDIO and HTTP |

The most feature-complete server in this review by raw tool count. 52 tools covering messages, rooms, teams, people, webhooks, and enterprise features (ECM folders, room tabs, attachments). Moved from the `webex` org to `WebexSamples`, suggesting it's positioned as sample code rather than an official product.

**Webex federated agentic platform (NEW).** Webex is building a federated platform where every Webex product can participate independently with shared governance, consistency, and interoperability of deployed MCP servers. MCP Server Developer Onboarding is the first beta feature (March 2026). Webex Contact Center now supports MCP fulfillment actions — autonomous AI agents can connect directly to remote MCP servers.

### What Works Well

**Comprehensive API coverage.** 52 tools covering essentially the entire Webex Messaging API. This is the most complete single-platform MCP integration for any video conferencing vendor. 118 unit tests.

**Dual transport.** STDIO for local use, HTTP for remote deployment. Docker support for production.

**Enterprise features.** ECM folder management, room tabs, attachment actions — features that matter for enterprise Webex deployments.

**Platform direction is promising.** The federated agentic platform vision suggests Webex meeting-specific MCP servers (not just messaging) are coming.

### What Doesn't Work Well

**Minimal adoption.** ~4 stars. The move from `webex` to `WebexSamples` org may reduce perceived official status.

**Messaging focus.** Despite Webex being a full video conferencing platform and building a federated MCP platform, the current MCP server covers messaging only — no meeting scheduling, video, or transcription.

## Adjacent: Meeting Assistants with MCP Potential

### Meetily

| Detail | Info |
|--------|------|
| [Zackriya-Solutions/meetily](https://github.com/Zackriya-Solutions/meetily) | ~11,400 stars (+63%) |
| License | MIT |
| Language | Rust + Next.js |
| Latest | v0.3.0 (March 3, 2026) |
| Platforms | macOS, Windows, Linux |

Not an MCP server, but the most popular open-source meeting assistant by a massive margin. **11,400 stars** (up 63% from 7,000 in March) — privacy-first with 100% local processing, 4x faster Parakeet/Whisper transcription, speaker diarization, and multiple AI provider support (Ollama, Claude, Groq, OpenRouter). Works with every meeting platform by capturing device audio directly. Now also offers a "PRO" version alongside the free community edition.

**Why it matters for MCP:** Meetily's explosive growth (63% in 40 days) and architecture (local transcription + flexible AI backends) make it the most likely candidate for a meeting MCP server integration. With 11,400 stars of community momentum and privacy-first positioning, a Meetily MCP wrapper would instantly become the most popular open-source meeting intelligence MCP server. The project still doesn't have MCP integration — this remains the biggest opportunity in the category.

## What's Missing

**~~No official Zoom MCP server.~~** ✅ **CLOSED (April 9, 2026).** Zoom launched its official MCP connector for Claude Cowork and Claude Code.

**~~No official Microsoft Teams meeting MCP server.~~** ✅ **PARTIALLY CLOSED.** Microsoft Work IQ Teams provides official 25+ tool messaging/channel management. Meeting-specific features (recordings, transcriptions) are still via Work IQ Calendar for scheduling only.

**No official Google Meet MCP server.** Google launched a Workspace MCP Server in preview covering Calendar, Drive, Gmail, and Chat — but **Google Meet was not included**. Despite 110 million+ monthly "Take Notes For Me" users, there's no dedicated Meet MCP server. The community server (23 tools) fills the gap partially. This is now the biggest remaining platform gap.

**No meeting summarization server.** Transcription is covered (Vexa, tl;dv, Otter.ai, Fireflies.ai), and some platforms provide AI-generated summaries, but no standalone MCP server specializes in generating structured meeting summaries, action items, or decision logs from arbitrary transcript input.

**No Meetily MCP wrapper.** The most popular open-source meeting assistant (11,400 stars, 63% growth in 40 days) still doesn't have MCP integration. This is the biggest open-source opportunity in the category.

**No calendar-to-meeting bridge.** Connecting a calendar MCP server to a meeting MCP server (auto-join upcoming meetings, transcribe, and update your notes) requires manual orchestration. Microsoft's Work IQ suite (Calendar + Teams) comes closest but doesn't fully bridge the gap.

## How to Choose

**"I use Zoom and want meeting intelligence in Claude"** → **Zoom Official MCP Connector** (April 2026). First-party, managed, secure. The default choice for Zoom users on Claude.

**"I want AI agents to participate in my meetings"** → [Joinly](https://github.com/joinly-ai/joinly). Most adopted real-time participation framework (494 stars). Composable with other MCP servers. Multiple STT/TTS providers.

**"I need meeting transcripts accessible to AI agents"** → [Vexa](https://github.com/Vexa-ai/vexa) (open source, self-hostable, 1,900 stars, v0.10.4) or [tl;dv MCP](https://github.com/tldv-public/tldv-mcp-server) (commercial SaaS, multi-platform). For cross-meeting analysis: [Otter.ai MCP](https://otter.ai/) or [Fireflies.ai MCP](https://fireflies.ai/) (commercial, hosted).

**"I want speaking bots in meetings"** → [Meeting BaaS](https://github.com/Meeting-BaaS/meeting-mcp) + [speaking-bots-mcp](https://github.com/Meeting-Baas/speaking-bots-mcp). Only option for AI bots that talk in calls.

**"I need a Zoom integration outside Claude"** → [echelon-ai-labs/zoom-mcp](https://github.com/echelon-ai-labs/zoom-mcp). Best community option (26 stars). Use the official Zoom connector if you're on Claude.

**"I need a Teams integration"** → **Microsoft Work IQ Teams** (official, 25+ tools, Copilot license required) or [InditexTech/mcp-teams-server](https://github.com/InditexTech/mcp-teams-server) (369 stars, Docker-ready, no Copilot needed) or [floriscornel/teams-mcp](https://github.com/floriscornel/teams-mcp) (91 stars, 25+ tools, npm package).

**"I need a Webex integration"** → [WebexSamples/webex-messaging-mcp-server](https://github.com/WebexSamples/webex-messaging-mcp-server). 52 tools, messaging only. Watch for Webex's federated agentic platform for meeting-specific MCP.

**"I want private, local meeting transcription"** → Watch [Meetily](https://github.com/Zackriya-Solutions/meetily) (11,400 stars) for MCP integration, or self-host [Vexa](https://github.com/Vexa-ai/vexa).

## Rating: 4.0 / 5 (↑ from 3.5)

The video conferencing MCP ecosystem has matured dramatically in 40 days. The category now spans **four tiers**: official platform connectors (Zoom, Microsoft Work IQ), multi-platform intelligence services (Vexa, tl;dv, Otter.ai, Fireflies.ai), community platform wrappers (Teams, Zoom, Webex), and real-time participation frameworks (Joinly, Meeting BaaS). **20+ servers** across the ecosystem, up from 14+.

**What changed:** Zoom's official MCP connector (April 9, 2026) closed the single biggest gap in the entire category. Microsoft's Agent 365 Work IQ Teams brought official enterprise support. Otter.ai and Fireflies.ai brought two of the most popular meeting intelligence platforms into the MCP ecosystem. Vexa shipped v0.10.4 with Zoom Web bot support and 4x CPU reduction. Joinly grew 20% to 494 stars. Meetily exploded to 11,400 stars (+63%).

**The remaining gap:** Google Meet still has no official MCP server — surprising given 110 million+ monthly "Take Notes For Me" users and Google's Workspace MCP Server preview covering Calendar, Chat, and Drive. Google Meet is now the last major holdout among the top three platforms.

Vexa remains the strongest open-source option (1,900 stars, self-hostable, 100 languages, v0.10 architecture refactor). Joinly's real-time participation concept is the most ambitious. Meetily's 11,400-star community is the biggest untapped MCP opportunity.

The upgrade from 3.5 to 4.0 reflects a fundamental shift: meeting MCP has moved from "community fills the gaps" to "platforms ship official integrations." Two of three major platforms now have first-party MCP support. The developer experience has improved substantially — most use cases can now be solved with official, maintained integrations rather than community workarounds.

---

*This review was originally written on 2026-03-19 and refreshed on 2026-04-28. Star counts, version numbers, and feature availability may have changed since publication. We research MCP servers thoroughly through documentation, GitHub repositories, community discussions, and published benchmarks — we do not test servers hands-on.*

*Refreshed on 2026-04-28 using Claude Opus 4.6 (Anthropic).*
