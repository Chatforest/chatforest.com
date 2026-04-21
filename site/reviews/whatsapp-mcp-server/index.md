# WhatsApp MCP Server — AI Agents Meet Your Private Messages

> WhatsApp MCP server by Luke Harries lets AI agents read, search, and send WhatsApp messages through your personal account. 5,500 GitHub stars, 1.1M PulseMCP visitors, MIT license — but it became the poster child for MCP prompt injection attacks.


Part of our **[Communication & Collaboration MCP category](/categories/communication-collaboration/)**.

*At a glance: 5,500 GitHub stars, 991 forks, MIT license, Go (51.2%) + Python (48.8%), only release v0.0.1 (April 6, 2025). Created by Luke Harries (Head of Growth at ElevenLabs). PulseMCP: ~1.1M all-time visitors, ~21.1K weekly, #56 globally. 73 open issues, 81 open PRs.*

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

WhatsApp MCP appears to be a side project that caught fire — it has 5.5K stars but only 27 commits and a single release (v0.0.1). Harries built it, it went viral, and the community has been submitting PRs ever since (81 open PRs vs. 27 commits tells the story). He's been vocal about it on LinkedIn and Twitter, and featured it in a [Lenny's Newsletter piece](https://www.lennysnewsletter.com/p/the-ai-marketing-stack) about ElevenLabs' AI playbook that saved the company $140K.

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

**Strong adoption signals.** 5.5K stars, 991 forks, ~1.1M all-time PulseMCP visitors, and ~21.1K weekly visitors make this one of the most popular MCP servers in any category. #56 globally on PulseMCP.

**MIT license.** Fully open source, no restrictions, no paid tiers.

**Media support is thoughtful.** Sending images, videos, documents, and especially voice messages (with automatic .ogg Opus conversion) shows real attention to how people actually use WhatsApp.

## What's Not

**The "lethal trifecta" poster child.** WhatsApp MCP became the canonical example of MCP prompt injection attacks. Invariant Labs published a [detailed exploit demonstration](https://invariantlabs.ai/blog/whatsapp-mcp-exploited) showing two attack vectors:

1. **Malicious MCP server attack:** If you have WhatsApp MCP installed alongside *any* compromised MCP server, the attacker can use "tool shadowing" to intercept and redirect your WhatsApp messages — reading your conversations and sending messages as you.

2. **Injected message attack:** An attacker sends you a specially crafted WhatsApp message containing hidden prompt injection instructions. When your AI agent processes that chat, the injected text manipulates the agent into exfiltrating your private conversations.

Docker published a follow-up [horror story blog post](https://www.docker.com/blog/mcp-horror-stories-whatsapp-data-exfiltration-issue/) about this exact scenario. The README itself warns: *"the WhatsApp MCP is subject to the lethal trifecta... project injection could lead to private data exfiltration."* Credit to Harries for the transparency, but the vulnerability is structural and unfixed.

**Only 27 commits and v0.0.1.** Despite 5.5K stars and massive community interest, the repo has just 27 commits on main and only one release. 81 open PRs suggest substantial community contributions are sitting unmerged. 73 open issues remain unaddressed. The project feels more like a viral proof-of-concept than an actively maintained tool.

**No security policy.** No SECURITY.md, no responsible disclosure process, no CVE tracking. For a tool that accesses your entire private message history, this is a notable gap.

**WhatsApp ToS gray area.** WhatsApp's Terms of Service prohibit automated or bulk messaging and unofficial API access. The whatsmeow library (which this project uses) reverse-engineers the WhatsApp Web protocol. Meta could ban your account — and there's no recourse if they do.

**No sandboxing or permission model.** Once connected, the AI agent has full read/write access to your entire WhatsApp account. There's no way to restrict which contacts or groups the agent can access, no approval step before sending messages, and no rate limiting.

## Competitors

- **[whatsapp-mcp-extended](https://github.com/FelixIsaac/whatsapp-mcp-extended)** — Fork with 41 tools adding reactions, group management, polls, presence tracking, newsletters, and webhooks. Much more feature-rich but tiny community (~10 stars).

- **[verygoodplugins/whatsapp-mcp](https://github.com/verygoodplugins/whatsapp-mcp)** — Alternative WhatsApp MCP implementation focused on reading and sending messages. Smaller scope and community.

- **[msaelices/whatsapp-mcp-server](https://github.com/msaelices/whatsapp-mcp-server)** — Python implementation using the WhatsApp Business API via GreenAPI (a commercial service). Officially supported API, but requires a paid GreenAPI subscription and a WhatsApp Business account.

- **[Peach AI WhatsApp](https://trypeach.io/)** — Official MCP server (530 weekly PulseMCP visitors). Commercial offering with presumably more polish, but much smaller adoption.

- **Twilio / Telnyx / CPaaS platforms** — For production messaging with proper API support, compliance, and SLAs. Different category entirely — business infrastructure vs. personal account access.

## The Elephant in the Room

WhatsApp MCP perfectly illustrates the tension at the heart of the MCP ecosystem: the most *useful* MCP servers are often the most *dangerous*. Accessing your personal messages is genuinely valuable. It's also genuinely risky when any MCP server in your stack — or any message in your inbox — can hijack the agent's behavior.

The project's own README warns about this. Invariant Labs used it as their primary case study. Docker wrote a blog post about it. And yet it has 5.5K stars and growing, because the use case is compelling.

If you use this: don't run it alongside untrusted MCP servers, be cautious about processing messages from unknown contacts, and understand that there is no permission boundary between the agent and your entire WhatsApp history.

## Rating: 3/5

WhatsApp MCP is a well-conceived tool that solves a real problem — AI agents that can interact with your most-used messaging platform. The local-only architecture is a sound privacy decision, the media support is thoughtful, and the adoption numbers speak for themselves. Luke Harries deserves credit for both building it and being transparent about its risks.

But 27 commits, one pre-release version, 81 unmerged PRs, no security policy, and the distinction of being the MCP ecosystem's most famous prompt injection case study — these are hard to overlook. The "lethal trifecta" isn't a theoretical concern; it's been publicly demonstrated with working exploits. The project reads as a viral side project that outgrew its maintenance capacity.

Three stars: strong concept, real adoption, genuine utility, but treat it as experimental software with serious security implications for your private communications.

