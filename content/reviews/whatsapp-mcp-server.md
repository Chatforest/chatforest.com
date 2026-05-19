---
title: "WhatsApp MCP Server — AI Agents Meet Your Private Messages"
date: 2026-04-20T21:00:00+09:00
description: "WhatsApp MCP server by Luke Harries lets AI agents read, search, and send WhatsApp messages through your personal account. 5,658 GitHub stars, MIT license — the prompt injection poster child, now with a path traversal vulnerability and a broken main branch."
og_description: "WhatsApp MCP: AI agents access your personal WhatsApp. 5.7K stars, MIT, Go+Python, broken main branch, CWE-22 path traversal unpatched. Rating: 2/5."
content_type: "Review"
card_description: "MCP server that connects AI agents to your personal WhatsApp account. A Go bridge handles WhatsApp Web authentication and stores messages in local SQLite; a Python MCP server exposes tools for searching messages, contacts, and sending texts and media. Created by Luke Harries, Head of Growth at ElevenLabs. No new commits since July 2025. The main branch is currently broken for many users due to unmerged whatsmeow API fixes. A path traversal vulnerability (CWE-22) and MCPSafe Grade D scan remain unaddressed."
last_refreshed: 2026-05-19
---

Part of our **[Communication & Collaboration MCP category](/categories/communication-collaboration/)**.

*At a glance: 5,658 GitHub stars, 1,048 forks, MIT license, Go (51.2%) + Python (48.8%), only release v0.0.1 (April 6, 2025). Created by Luke Harries (Head of Growth at ElevenLabs). PulseMCP: ~1.1M all-time visitors, ~20,600 weekly, #56 globally. 78 open issues, 99 open PRs. Last commit: July 13, 2025 (README only). Main branch currently broken for many users.*

WhatsApp MCP bridges AI agents directly to your personal WhatsApp account. You authenticate via QR code (same as WhatsApp Web), and the server gives Claude, Cursor, or other MCP clients the ability to search your messages, read conversations, look up contacts, and send messages — including images, videos, documents, and voice notes.

It works. It's also the single most-cited example of why MCP + private data + agent actions = danger.

## Architecture

The project has two components:

- **Go Bridge** (`whatsapp-bridge/`) — connects to WhatsApp's web multidevice API using the [whatsmeow](https://github.com/tulir/whatsmeow) library. Handles QR code authentication, maintains the WhatsApp connection, and stores all messages locally in SQLite. Runs as a persistent process.

- **Python MCP Server** (`whatsapp-mcp-server/`) — implements the Model Context Protocol, exposing tools that query the local SQLite database and send messages through the Go bridge.

All message data stays local — nothing is sent to external servers beyond WhatsApp itself. Messages only reach your LLM when the agent explicitly calls a tool. This is a meaningful privacy design choice, though it doesn't address the prompt injection risks discussed below.

## What It Does

The MCP server exposes tools for:

- **Searching chats** — find conversations by contact name, group name, or message content
- **Listing messages** — retrieve message history from specific chats with filters
- **Getting message context** — fetch surrounding messages for a specific message
- **Searching contacts** — look up contacts by name or phone number
- **Sending messages** — text messages to individuals or groups
- **Sending media** — images, videos, documents, and audio files
- **Voice messages** — automatic conversion to WhatsApp's .ogg Opus format via FFmpeg

## Who Built It

**Luke Harries** — Head of Growth at ElevenLabs, the AI voice company valued at $6.6B. Previously interim Head of Product at PostHog, before that at Microsoft Research working on reinforcement learning. Cambridge-educated (pre-med). Also co-founded Fella, a men's health startup that pivoted through AI browser automation, COVID testing, digital CBT, and GLP-1 weight loss medication.

WhatsApp MCP appears to be a side project that caught fire — it has 5.7K stars but only 27 commits and a single release (v0.0.1, April 6, 2025). Harries built it, it went viral, and the community has been submitting PRs ever since (99 open PRs vs. 27 commits tells the story). He's been vocal about it on LinkedIn and Twitter, and featured it in a [Lenny's Newsletter piece](https://www.lennysnewsletter.com/p/the-ai-marketing-stack) about ElevenLabs' AI playbook that saved the company $140K. His last commit was a README update on July 13, 2025 — adding the prompt injection warning. He has made no public statements about the project's maintenance status or the growing security backlog.

## Setup

Requires Go and Python 3.6+, plus the UV package manager:

1. Clone the repo and start the Go bridge — scan the QR code with your phone
2. The bridge begins downloading and indexing your WhatsApp message history into SQLite
3. Configure your MCP client to point at the Python server
4. Compatible with Claude Desktop and Cursor

Optional: install FFmpeg for voice message support.

**Windows users:** CGO must be enabled for the SQLite driver (`set CGO_ENABLED=1`).

## What's Good

**It just works for the core use case.** Searching old WhatsApp conversations, finding that link someone sent you three months ago, or quickly sending a message from your desktop without picking up your phone — these are genuinely useful daily tasks. The tool set is simple and focused.

**Local-only data storage.** Messages are stored in a local SQLite database, not shipped to a cloud service. You control the data. Messages only reach the LLM when you (or your agent) invoke a tool.

**Strong adoption signals.** 5.7K stars, 1,048 forks, ~1.1M all-time PulseMCP visitors, and ~20,600 weekly visitors make this one of the most popular MCP servers in any category. #56 globally on PulseMCP.

**MIT license.** Fully open source, no restrictions, no paid tiers.

**Media support is thoughtful.** Sending images, videos, documents, and especially voice messages (with automatic .ogg Opus conversion) shows real attention to how people actually use WhatsApp.

## What's Not

**The "lethal trifecta" poster child.** WhatsApp MCP became the canonical example of MCP prompt injection attacks. Invariant Labs published a [detailed exploit demonstration](https://invariantlabs.ai/blog/whatsapp-mcp-exploited) showing two attack vectors:

1. **Malicious MCP server attack:** If you have WhatsApp MCP installed alongside *any* compromised MCP server, the attacker can use "tool shadowing" to intercept and redirect your WhatsApp messages — reading your conversations and sending messages as you.

2. **Injected message attack:** An attacker sends you a specially crafted WhatsApp message containing hidden prompt injection instructions. When your AI agent processes that chat, the injected text manipulates the agent into exfiltrating your private conversations.

Docker published a follow-up [horror story blog post](https://www.docker.com/blog/mcp-horror-stories-whatsapp-data-exfiltration-issue/) about this exact scenario. The README itself warns: *"the WhatsApp MCP is subject to the lethal trifecta... project injection could lead to private data exfiltration."* Credit to Harries for the transparency, but the vulnerability is structural and unfixed.

**The main branch is currently broken.** WhatsApp changed its protocol; the whatsmeow library that powers this project updated its `context.Context` API accordingly. At least five community PRs (filed May 12–18, 2026) fix the incompatibility. None have been merged. For new users trying to install and run the project, it will fail. The fix exists — it's just sitting in the PR queue.

**Path traversal vulnerability (CWE-22) — unaddressed.** Issue #241 (filed May 10, 2026) documents that the `sendWhatsAppMessage` function passes a `media_path` parameter directly to `os.ReadFile()` with no path sanitization. The proof-of-concept shows that posting `"media_path": "../../../etc/passwd"` reads arbitrary files from the host system. No maintainer response. No fix. No CVE assigned.

**MCPSafe Grade D.** An automated security scan (Issues #246–247, filed May 12, 2026) gave the project an AIVSS score of 67/100 — Grade D — with 13 high-severity and 12 medium-severity findings. The scanner flagged it as having the highest count of high-severity findings across scanned repos. No maintainer response.

**27 commits, v0.0.1 — over a year with no release.** Despite 5.7K stars and massive community interest, the repo has just 27 commits on main and only one release. 99 open PRs (up from 81 in April) suggest substantial community contributions piling up unmerged. 78 open issues remain unaddressed. The project feels more like a viral proof-of-concept that exceeded its maintenance capacity.

**No security policy.** No SECURITY.md, no responsible disclosure process, no CVE tracking. For a tool that accesses your entire private message history and has an open path traversal vulnerability, this is a critical gap.

**WhatsApp ToS gray area.** WhatsApp's Terms of Service prohibit automated or bulk messaging and unofficial API access. The whatsmeow library (which this project uses) reverse-engineers the WhatsApp Web protocol. Meta could ban your account — and there's no recourse if they do.

**No sandboxing or permission model.** Once connected, the AI agent has full read/write access to your entire WhatsApp account. There's no way to restrict which contacts or groups the agent can access, no approval step before sending messages, and no rate limiting.

## Competitors

- **[whatsapp-mcp-extended](https://github.com/FelixIsaac/whatsapp-mcp-extended)** — Fork with 41 tools adding reactions, group management, polls, presence tracking, newsletters, HMAC-SHA256 webhook security, and a web UI. Much more feature-rich; 15 stars and growing (~137 commits, actively maintained since December 2025).

- **[verygoodplugins/whatsapp-mcp](https://github.com/verygoodplugins/whatsapp-mcp)** — Explicitly positioned as the actively maintained alternative since the original "hasn't been updated since April 2025." Adds webhook forwarding, call history, and expanded media support. 56 stars, 37 forks, 108 commits. The most serious fork challenger today.

- **[msaelices/whatsapp-mcp-server](https://github.com/msaelices/whatsapp-mcp-server)** — Python implementation using the WhatsApp Business API via GreenAPI (a commercial service). Officially supported API, but requires a paid GreenAPI subscription and a WhatsApp Business account.

- **[Peach AI WhatsApp](https://trypeach.io/)** — Official MCP server (530 weekly PulseMCP visitors). Commercial offering with presumably more polish, but much smaller adoption.

- **Twilio / Telnyx / CPaaS platforms** — For production messaging with proper API support, compliance, and SLAs. Different category entirely — business infrastructure vs. personal account access.

## The Elephant in the Room

WhatsApp MCP perfectly illustrates the tension at the heart of the MCP ecosystem: the most *useful* MCP servers are often the most *dangerous*. Accessing your personal messages is genuinely valuable. It's also genuinely risky when any MCP server in your stack — or any message in your inbox — can hijack the agent's behavior.

The project's own README warns about this. Invariant Labs used it as their primary case study. Docker wrote a blog post about it. And yet it has 5.7K stars and growing, because the use case is compelling.

If you use this: don't run it alongside untrusted MCP servers, be cautious about processing messages from unknown contacts, and understand that there is no permission boundary between the agent and your entire WhatsApp history.

One policy footnote: in January 2026, Meta banned general-purpose AI chatbots from the WhatsApp Business API, primarily affecting official business integrations. Unofficial API users (including this project, which uses whatsmeow) were already ToS-violating; this change doesn't add new risk for them specifically, but it does further narrow the space of compliant alternatives.

## Rating: 2/5

WhatsApp MCP remains a well-conceived tool for a real use case, and the local-only architecture and media support are still design strengths. But a lot has changed since it first went viral.

The main branch doesn't build for many users right now — a whatsmeow API change broke it, five community PRs fix it, and none have been merged. A path traversal vulnerability (CWE-22) that lets anyone read arbitrary files from your system has been sitting open since May 10 with zero maintainer response. A formal security scan gave the project a Grade D with 13 high-severity findings. Open PRs climbed from 81 to 99. No commits since July 2025. Still on v0.0.1, more than a year after release.

The "lethal trifecta" prompt injection risk that defined this project's reputation hasn't been addressed — it's structural and still live. Now add an active path traversal vulnerability on top.

Luke Harries built something real, and the community clearly wants it to succeed — 99 open PRs from contributors who did the work. But the project is effectively unmaintained at this point. If you need WhatsApp MCP today, consider **verygoodplugins/whatsapp-mcp** (56 stars, actively maintained, compatible with the current whatsmeow API) or **FelixIsaac/whatsapp-mcp-extended** (15 stars, feature-complete, HMAC webhook security).

Two stars: strong original concept, genuine community need, but currently broken to install, has an open path traversal vulnerability, and shows no signs of active maintenance.
