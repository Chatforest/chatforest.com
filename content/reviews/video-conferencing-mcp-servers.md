---
title: "Video Conferencing & Meeting Intelligence MCP Servers — Joinly, Vexa, tl;dv, Meeting BaaS, and More"
date: 2026-03-19T18:30:00+09:00
description: "Video conferencing MCP servers let AI agents join meetings, access transcripts, manage recordings, and even speak in calls. We reviewed 14+ servers across three approaches: meeting intelligence platforms, platform-specific integrations, and real-time participation. Joinly (413 stars) leads as the most adopted meeting-to-agent bridge with real-time participation. Vexa (1,800 stars) is the strongest open-source transcription API with built-in MCP. InditexTech's Teams MCP (353 stars) is the top single-platform integration."
og_description: "Video conferencing MCP servers: Joinly (413 stars, real-time meeting participation), Vexa (1,800 stars, open-source transcription API), tl;dv (official, multi-platform intelligence), InditexTech Teams MCP (353 stars, messaging), Meeting BaaS (speaking bots), Zoom MCP servers, Webex MCP (52 tools). 14+ servers across 3 approaches. Rating: 3.5/5."
content_type: "Review"
card_description: "Video conferencing and meeting intelligence MCP servers across Joinly, Vexa, tl;dv, Meeting BaaS, Zoom, Teams, and Webex. The ecosystem splits between meeting intelligence platforms (transcript access), platform-specific integrations (API wrappers), and real-time participation (bots that join and speak in calls)."
---

Meetings are where decisions happen, context lives, and information gets trapped. Every organization runs on video calls — Zoom, Google Meet, Microsoft Teams — but the content of those calls has been locked away from AI agents. MCP servers are starting to change that.

This review covers MCP servers for **video conferencing and meeting intelligence** — servers that let AI agents interact with meetings in some way, whether that's accessing transcripts, managing recordings, scheduling calls, or actively participating in real-time. For broader communication platform integrations (Slack, Discord, email), see our [Communication MCP Servers comparison](/guides/best-communication-mcp-servers/).

The headline: **the meeting MCP ecosystem splits into three distinct tiers.** At the top, multi-platform intelligence services like tl;dv and Vexa provide rich transcript and recording access across Zoom, Meet, and Teams. In the middle, platform-specific servers wrap individual APIs (Zoom, Teams, Webex). At the frontier, projects like Joinly and Meeting BaaS are building something more ambitious: AI agents that actually join and participate in video calls.

## Multi-Platform Meeting Intelligence

These servers bridge multiple video conferencing platforms, providing unified access to meeting transcripts, recordings, and metadata.

### Vexa

| Detail | Info |
|--------|------|
| [Vexa-ai/vexa](https://github.com/Vexa-ai/vexa) | ~1,800 stars |
| License | Open source (self-hostable) |
| Language | Python |
| Platforms | Google Meet, Microsoft Teams, Zoom |
| Install | `make all` (self-hosted) or hosted SaaS |

The strongest open-source option for meeting transcription with MCP support. Vexa is a full meeting transcription API — auto-join bots, real-time WebSocket transcripts, and an MCP server microservice that exposes the entire API to any MCP-capable agent.

### What Works Well

**Real-time multilingual transcription.** 100 languages via Whisper, plus real-time translation across all of them. This is production-grade transcription infrastructure, not a weekend project.

**Self-hostable.** Runs locally with a single `make all` on CPU or GPU. Critical for regulated industries and privacy-sensitive teams who can't send meeting audio to third-party services.

**MCP server as a first-class component.** The MCP integration is a dedicated microservice within the Vexa architecture — agents can start/stop meeting bots and fetch or stream transcripts on demand.

**Strong adoption.** 1,800+ stars and actively maintained. The project is aiming for 2,000 stars and publishes regular releases.

### What Doesn't Work Well

**Infrastructure complexity.** Self-hosting requires multiple services running together. This isn't a simple MCP server you pip install — it's a full platform with bots, transcription workers, and APIs.

**Bot-based approach.** Like all services that "join" meetings, Vexa sends a bot that appears as a participant. Some organizations block unknown participants or require manual admission.

### tl;dv MCP Server

| Detail | Info |
|--------|------|
| [tldv-public/tldv-mcp-server](https://github.com/tldv-public/tldv-mcp-server) | ~7 stars |
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

**Very low GitHub adoption.** ~7 stars despite tl;dv's substantial user base suggests the MCP integration is new or not widely promoted.

**Requires tl;dv account.** This is a wrapper around a commercial SaaS. You need a tl;dv account (free tier available, premium for full features), and meeting data lives on their servers.

**No license specified.** The GitHub repository doesn't include a license — technically "all rights reserved" by default.

### Meeting BaaS

| Detail | Info |
|--------|------|
| [Meeting-BaaS/meeting-mcp](https://github.com/Meeting-BaaS/meeting-mcp) | ~25 stars |
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

**Low adoption.** ~25 stars. The speaking bots capability is impressive but apparently not yet widely adopted.

**Requires Meeting BaaS infrastructure.** Like Vexa, this is a platform — not a standalone MCP server you point at your existing Zoom account.

## Real-Time Meeting Participation

### Joinly

| Detail | Info |
|--------|------|
| [joinly-ai/joinly](https://github.com/joinly-ai/joinly) | ~413 stars |
| License | Not specified |
| Language | Not specified |
| Platforms | Zoom, Microsoft Teams, Google Meet |

Joinly is connector middleware that enables AI agents to join and actively participate in video calls. The MCP server provides meeting tools and resources so that any MCP-capable agent can attend meetings, access real-time transcripts, speak, and send chat messages.

### What Works Well

**Highest adoption for real-time participation.** 413 stars makes this the most popular MCP server specifically designed for agents to participate in meetings (vs. just accessing transcripts after the fact).

**Composable architecture.** A joinly agent can connect to other MCP servers (GitHub, Tavily, Notion) alongside the meeting tools — so your meeting bot can pull up code, search the web, or check docs during a call.

**Real-time transcript as a resource.** The MCP server exposes the live meeting transcript as a resource, enabling agents to follow along and respond contextually.

**Active community.** Featured on Hacker News (Show HN), suggesting genuine developer interest in the concept.

### What Doesn't Work Well

**No license specified.** Like tl;dv, the repository lacks a license file.

**Nascent technology.** AI agents actively participating in meetings is ambitious — real-world reliability in production meetings is unproven at scale.

**Browser-based approach.** Joinly works with browser-based meeting platforms, which means it depends on browser automation under the hood. This can be fragile as platforms update their UIs.

## Platform-Specific Servers

### Microsoft Teams MCP (InditexTech)

| Detail | Info |
|--------|------|
| [InditexTech/mcp-teams-server](https://github.com/InditexTech/mcp-teams-server) | ~353 stars |
| License | Not specified |
| Language | Python |
| Tools | 5+ (messaging focused) |
| Install | Docker or Python + uv |

The most popular Teams-specific MCP server, built by Inditex (the parent company of Zara). Focuses on **messaging** — read messages, create messages, reply to threads, mention members.

### What Works Well

**Strong adoption for enterprise.** 353 stars — the highest of any platform-specific meeting/communication MCP server in this review. Being built by a Fortune 500 company (Inditex) adds credibility.

**Docker-first deployment.** Pre-built Docker image on GHCR for easy enterprise deployment.

**Thread management.** Start threads with titles, reply with mentions, read channel messages — covers the core Teams messaging workflow.

### What Doesn't Work Well

**Messaging only, not video.** This is a Teams messaging server, not a video conferencing server. No meeting scheduling, recording access, or transcription features.

**Scoped to one team.** Configured via TEAM_ID and TEAMS_CHANNEL_ID — designed for a specific team's channels, not broad organizational access.

### Microsoft Teams MCP (floriscornel)

| Detail | Info |
|--------|------|
| [floriscornel/teams-mcp](https://github.com/floriscornel/teams-mcp) | ~67 stars |
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

**Lower adoption than InditexTech.** ~67 stars vs. 353 for the simpler alternative. The broader tool coverage hasn't translated to higher adoption.

**No meeting-specific features.** Like InditexTech's server, this is fundamentally a messaging and collaboration server — no video/audio/transcription capabilities.

### Zoom MCP Servers

Multiple Zoom MCP servers exist with varying quality:

| Server | Stars | Language | Focus |
|--------|-------|----------|-------|
| [echelon-ai-labs/zoom-mcp](https://github.com/echelon-ai-labs/zoom-mcp) | ~18 | Python | Full Zoom API (users, meetings, recordings) |
| [Prathamesh0901/zoom-mcp-server](https://github.com/Prathamesh0901/zoom-mcp-server) | ~7 | Not specified | CRUD meetings via Claude/Cursor |
| [forayconsulting/zoom_transcript_mcp](https://github.com/forayconsulting/zoom_transcript_mcp) | Low | Not specified | Zoom Cloud Recording transcripts |
| [peakmojo/mcp-server-zoom-noauth](https://github.com/peakmojo/mcp-server-zoom-noauth) | Low | Not specified | Recordings/transcripts without user auth |
| [JavaProgrammerLB/zoom-mcp-server](https://github.com/JavaProgrammerLB/zoom-mcp-server) | Low | Not specified | Meeting scheduling |

The best of the bunch is **echelon-ai-labs/zoom-mcp** at 18 stars — it supports Server-to-Server OAuth 2.0, retrieves user profiles, meeting details, recordings, and account settings. It requires Python 3.11+ and Zoom admin privileges.

**The notable absence: Zoom itself hasn't shipped an official MCP server.** Zoom does allow admins to build custom agents using MCP, but hasn't released a first-party server. Given Zoom's scale, this is the biggest gap in the category.

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
| [webex/webex-messaging-mcp-server](https://github.com/webex/webex-messaging-mcp-server) | ~6 stars |
| License | Not specified |
| Language | TypeScript/JavaScript |
| Tools | 52 |
| Transport | STDIO and HTTP |

The most feature-complete server in this review by raw tool count. 52 tools covering messages, rooms, teams, people, webhooks, and enterprise features (ECM folders, room tabs, attachments). Hosted under the `webex` GitHub org, suggesting official or semi-official status.

### What Works Well

**Comprehensive API coverage.** 52 tools covering essentially the entire Webex Messaging API. This is the most complete single-platform MCP integration for any video conferencing vendor.

**Dual transport.** STDIO for local use, HTTP for remote deployment. Docker support for production.

**Enterprise features.** ECM folder management, room tabs, attachment actions — features that matter for enterprise Webex deployments.

### What Doesn't Work Well

**Near-zero adoption.** ~6 stars despite being hosted under the official Webex GitHub org. Either very new or very poorly promoted.

**Messaging focus.** Despite Webex being a full video conferencing platform, this MCP server covers messaging only — no meeting scheduling, video, or transcription.

## Adjacent: Meeting Assistants with MCP Potential

### Meetily

| Detail | Info |
|--------|------|
| [Zackriya-Solutions/meeting-minutes](https://github.com/Zackriya-Solutions/meeting-minutes) | ~7,000 stars |
| License | Open source |
| Language | Rust + Python |
| Platforms | All (captures system audio) |

Not an MCP server, but worth noting as the most popular open-source meeting assistant. 7,000+ stars, privacy-first (100% local processing), 4x faster Parakeet/Whisper transcription, speaker diarization, and multiple AI provider support (Ollama, Claude, Groq). Works with every meeting platform by capturing device audio directly.

**Why it matters for MCP:** Meetily's architecture (local transcription + flexible AI backends) would be an excellent foundation for a meeting MCP server. If someone wraps Meetily's output in MCP tools, you'd have a privacy-first, platform-agnostic meeting intelligence server with 7,000 stars of community momentum behind it.

## What's Missing

**No official Zoom MCP server.** The most widely used video conferencing platform has no first-party MCP integration. Zoom's AI Companion and custom agent support exist, but there's no `zoom/zoom-mcp-server` on GitHub.

**No official Google Meet MCP server.** Despite Google launching managed MCP servers for many services in late 2025, Google Meet wasn't included. The community server (23 tools) fills the gap partially.

**No official Microsoft Teams meeting MCP server.** The InditexTech and floriscornel servers cover Teams messaging, but neither Microsoft nor any community server provides meeting scheduling, recording access, or transcription for Teams via MCP.

**No meeting summarization server.** Transcription is covered (Vexa, tl;dv), but no MCP server specializes in generating structured meeting summaries, action items, or decision logs from transcripts.

**No calendar-to-meeting bridge.** Connecting a calendar MCP server to a meeting MCP server (auto-join upcoming meetings, transcribe, and update your notes) requires manual orchestration. A unified "meeting workflow" server could fill this gap.

## How to Choose

**"I want AI agents to participate in my meetings"** → [Joinly](https://github.com/joinly-ai/joinly). Most adopted real-time participation framework (413 stars). Composable with other MCP servers.

**"I need meeting transcripts accessible to AI agents"** → [Vexa](https://github.com/Vexa-ai/vexa) (open source, self-hostable, 1,800 stars) or [tl;dv MCP](https://github.com/tldv-public/tldv-mcp-server) (commercial SaaS, multi-platform).

**"I want speaking bots in meetings"** → [Meeting BaaS](https://github.com/Meeting-BaaS/meeting-mcp) + [speaking-bots-mcp](https://github.com/Meeting-Baas/speaking-bots-mcp). Only option for AI bots that talk in calls.

**"I need a Zoom integration"** → [echelon-ai-labs/zoom-mcp](https://github.com/echelon-ai-labs/zoom-mcp). Best community option (18 stars). Wait for an official Zoom server if you need production reliability.

**"I need a Teams integration"** → [InditexTech/mcp-teams-server](https://github.com/InditexTech/mcp-teams-server) (353 stars, Docker-ready, messaging) or [floriscornel/teams-mcp](https://github.com/floriscornel/teams-mcp) (67 stars, 25+ tools, broader coverage).

**"I need a Webex integration"** → [webex/webex-messaging-mcp-server](https://github.com/webex/webex-messaging-mcp-server). 52 tools, messaging only.

**"I want private, local meeting transcription"** → Watch [Meetily](https://github.com/Zackriya-Solutions/meeting-minutes) (7,000 stars) for MCP integration, or self-host [Vexa](https://github.com/Vexa-ai/vexa).

## Rating: 3.5 / 5

The video conferencing MCP ecosystem is more interesting than its star counts suggest. The three-tier structure — intelligence platforms (Vexa, tl;dv), platform wrappers (Zoom, Teams, Webex), and real-time participation (Joinly, Meeting BaaS) — shows a maturing market finding different approaches to the same problem: making meetings accessible to AI.

Vexa stands out as genuinely production-grade open-source infrastructure (1,800 stars, self-hostable, 100 languages). Joinly's real-time participation concept is the most ambitious and forward-looking. InditexTech's Teams server proves that enterprise adoption is real (353 stars from a Fortune 500 company).

But the category has a glaring gap at the top: **none of the three major platforms — Zoom, Google Meet, or Microsoft Teams — ship an official meeting-focused MCP server.** The community has filled in around the edges, but platform-specific servers are fragmented, low-adoption, and focused on messaging rather than the core video conferencing experience (scheduling, recording, transcription). Until Zoom and Google ship official MCP servers — or Vexa/Joinly reach critical mass — most developers will find themselves stitching together multiple partial solutions.

---

*This review reflects research conducted in March 2026. Star counts, version numbers, and feature availability may have changed since publication. We research MCP servers thoroughly through documentation, GitHub repositories, community discussions, and published benchmarks — we do not test servers hands-on.*

*This review was written on 2026-03-19 using Claude Opus 4.6 (Anthropic).*
