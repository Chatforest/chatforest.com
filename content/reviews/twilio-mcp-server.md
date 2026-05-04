---
title: "Twilio MCP Server — All 2,000 Twilio APIs Available to Your AI Agent"
date: 2026-03-23T11:00:00+09:00
description: "Twilio's official MCP server exposes nearly 2,000 API endpoints across SMS, voice, video, conversations, and 40+ services to AI agents."
og_description: "Twilio MCP: ~2,000 API endpoints across 40+ services — SMS, voice, video, TaskRouter, and more. Open-source, TypeScript. Rating: 3/5."
content_type: "Review"
card_description: "Official first-party MCP server from Twilio Labs exposing nearly 2,000 API endpoints across 40+ Twilio services including SMS, voice, video, conversations, TaskRouter, Studio, and Serverless. TypeScript monorepo with OpenAPI-to-MCP generator, stdio and Streamable HTTP transport, API key authentication."
last_refreshed: 2026-05-04
category_url: "/categories/email-notification-services/"
---

**At a glance:** [GitHub](https://github.com/twilio-labs/mcp) — 103 stars, TypeScript, ISC license, ~2,000 API endpoints across 40+ services, stdio + Streamable HTTP transport, API key auth. Official first-party from [Twilio Labs](https://github.com/twilio-labs) ([Twilio Inc.](https://www.twilio.com/), NYSE: TWLO).

> **May 4, 2026 refresh** (42 days since original): Stars 96 → 103. Still alpha, npm at v0.7.0. The big change: Twilio's first-mover advantage in CPaaS MCP is gone — Vonage, Sinch, and Bandwidth have all launched official MCP servers since the original review. The comparison table below has been updated to reflect the new competitive landscape. Rating drops 3.5 → 3/5.

Twilio's MCP server is an **open-source, first-party monorepo** that gives AI agents access to nearly all of Twilio's communications APIs — SMS, voice, video, conversations, TaskRouter, Studio, Serverless, and dozens more. Rather than hand-crafting individual MCP tools, the server auto-generates them from Twilio's OpenAPI specifications, exposing ~2,000 endpoints. The tradeoff: you need to filter aggressively with `--services` and `--tags` flags, because no LLM context window can handle all of them at once.

[Twilio](https://www.twilio.com/) is the dominant cloud communications platform, founded in 2008 by Jeff Lawson and Evan Cooke in San Francisco. Publicly traded on NYSE (TWLO) since 2016. As of early 2026: ~5,500 employees, ~$4.9B annual revenue, ~$18.8B market cap. Twilio powers communications for companies like Uber, Airbnb, Netflix, Shopify, and Morgan Stanley. The MCP server was built by Twilio's Emerging Tech and Innovation (ETI) team and published under the `@twilio-alpha` npm scope — the "alpha" label is intentional.

## What It Does

The monorepo contains two packages:

1. **@twilio-alpha/mcp** — MCP server exposing Twilio's public APIs
2. **@twilio-alpha/openapi-mcp-server** — Generic OpenAPI-to-MCP tool generator (reusable for any OpenAPI spec)

The server supports 40+ Twilio services. Here are the major categories:

### Core Communication APIs

| Service | What It Covers |
|---------|---------------|
| **twilio_api_v2010** | SMS/MMS sending, voice calls, phone number management, recordings, conferences, usage records — the core Twilio API |
| **twilio_messaging_v1** | Messaging services, campaigns, phone number management, alpha senders |
| **twilio_voice_v1** | Voice configuration, IP access control, credential lists, connection policies |
| **twilio_video_v1** | Video rooms, compositions, recordings |
| **twilio_conversations_v1** | Omnichannel conversations, participants, messages |

### Workflow & Automation

| Service | What It Covers |
|---------|---------------|
| **twilio_studio_v2** | Visual flow builder — flows, executions, revisions |
| **twilio_taskrouter_v1** | Task routing — workers, tasks, workflows, workspaces, activities, queues |
| **twilio_serverless_v1** | Functions, assets, deployments, environments |
| **twilio_flex_v1** | Flex contact center — channels, interactions, web channels |

### Identity & Security

| Service | What It Covers |
|---------|---------------|
| **twilio_verify_v2** | Phone verification — services, verifications, access tokens |
| **twilio_lookups_v2** | Phone number lookups — carrier, caller name, line type |
| **twilio_proxy_v1** | Phone number masking for privacy |

### Infrastructure

| Service | What It Covers |
|---------|---------------|
| **twilio_trunking_v1** | SIP trunking — trunks, origination/termination URLs |
| **twilio_supersim_v1** | Global IoT SIM management |
| **twilio_wireless_v1** | IoT device connectivity |
| **twilio_sync_v1** | Real-time state synchronization |
| **twilio_notify_v1** | Push notifications, SMS notifications |
| **twilio_accounts_v1** | Account management, auth tokens, AWS integration |

Plus: Assistants, Bulk Exports, Chat (v1-3), Content, Events, Frontline, Insights, Intelligence, IP Messaging, Marketplace, Media, Monitor, Numbers, Pricing, and more.

## Setup & Configuration

### Quick Start (npx)

```json
{
  "mcpServers": {
    "twilio": {
      "command": "npx",
      "args": [
        "-y", "@twilio-alpha/mcp",
        "YOUR_ACCOUNT_SID/YOUR_API_KEY:YOUR_API_SECRET"
      ]
    }
  }
}
```

### Filtered Setup (recommended)

Since ~2,000 endpoints will overwhelm any LLM, filter by service and/or tag:

```json
{
  "mcpServers": {
    "twilio": {
      "command": "npx",
      "args": [
        "-y", "@twilio-alpha/mcp",
        "YOUR_ACCOUNT_SID/YOUR_API_KEY:YOUR_API_SECRET",
        "--services", "twilio_api_v2010",
        "--tags", "Api20100401IncomingPhoneNumber,Api20100401Message"
      ]
    }
  }
}
```

To filter by tags only, pass `--services ''` as empty.

### Serverless Deployment (Streamable HTTP)

Twilio also provides a [Serverless Functions template](https://github.com/twilio-labs/function-templates/tree/main/mcp-server) for remote deployment with Streamable HTTP transport:

```bash
twilio serverless:init mcp-tutorial --template=mcp-server
twilio serverless:deploy --runtime node20
```

This gives you a hosted HTTPS endpoint with Twilio signature authentication — no local process needed.

## Authentication

Credentials are passed as a command-line argument in the format `ACCOUNT_SID/API_KEY:API_SECRET`. You need to create an API key from the Twilio Console (not your auth token directly). The ETI team recommends using restricted API keys with only the permissions your agent needs.

For the serverless deployment, authentication uses Twilio request signatures via HTTP headers.

## Performance Benchmarks

Twilio's ETI team published [real-world benchmarks](https://www.twilio.com/en-us/blog/developers/twilio-alpha-mcp-server-real-world-performance) testing three tasks (phone number purchase, TaskRouter activity creation, TaskRouter queue creation) using Cline with Claude 3.7 Sonnet:

| Metric | With MCP | Without MCP | Change |
|--------|----------|-------------|--------|
| **Task completion** | 100% | ~92.3% | +7.7% |
| **Speed** | — | — | ~20.5% faster |
| **API calls** | — | — | ~19.2% fewer |
| **User interactions** | — | — | ~3.2% fewer |
| **Token usage** | — | — | ~6.3% fewer |
| **Token cost** | — | — | ~27.5% higher |

The paradox: MCP improved reliability and speed but **increased costs ~27.5%** due to cached context overhead. Cache reads rose 28.5% and cache writes rose 53.7%. The team recommends filtering aggressively to expose only needed endpoints.

## Development History

| Date | Event |
|------|-------|
| March 24, 2025 | Repository created on GitHub |
| March 25, 2025 | v0.0.3 published to npm |
| April 1, 2025 | Official launch blog post |
| May 21, 2025 | Serverless deployment tutorial published |
| Mid-2025 | Performance benchmarking study published |
| December 3, 2025 | Vonage launches official MCP tooling server — first major competitor |
| Late 2025 | Sinch launches production-ready MCP server |
| 2025–2026 | Bandwidth launches MCP server with official docs |
| April 12, 2026 | Last commit to twilio-labs/mcp — 103 stars |
| April 2026 | npm v0.7.0 published — still under @twilio-alpha scope |
| May 2026 | Still alpha; no beta/GA announcement |

## Twilio Pricing

Twilio is pay-as-you-go. The MCP server itself is free — you pay for the Twilio API calls your agent makes:

| Service | Cost (US) |
|---------|-----------|
| **SMS send** | $0.0083/message |
| **SMS receive** | $0.0083/message |
| **MMS send** | $0.0220/message |
| **Voice outbound** | $0.014/minute |
| **Voice inbound (local)** | $0.0085/minute |
| **Voice inbound (toll-free)** | $0.022/minute |
| **Phone number (local)** | $1.15/month |
| **Phone number (toll-free)** | $2.15/month |

Twilio offers a free trial with limited credits for new accounts. No free tier for ongoing usage — you pay per API call. See [full pricing](https://www.twilio.com/en-us/pricing).

## How It Compares

| Feature | Twilio MCP | Vonage MCP | Sinch MCP | Bandwidth MCP |
|---------|-----------|-----------|-----------|--------------|
| **MCP server** | Yes, official (alpha) | Yes, official (stable) | Yes, official (production) | Yes, official (production) |
| **Launch date** | March 2025 | December 2025 | Late 2025 | 2025 |
| **API endpoints** | ~2,000 | SMS, voice, WhatsApp, RCS | SMS, WhatsApp, RCS, email, voice | Voice, messaging |
| **SMS pricing (US)** | $0.0083 | $0.0068 | Varies | Varies |
| **Voice pricing (US)** | $0.014/min | $0.0127/min | Varies | Varies |
| **Open source** | Yes (ISC) | Yes | Yes | Yes |
| **Transport** | stdio + Streamable HTTP | MCP-compliant | MCP-compliant | MCP-compliant |
| **Status** | Alpha | Stable | Production-ready | Production-ready |
| **Free tier** | Trial credits only | Trial credits | Trial credits | Trial credits |

**As of May 2026, Twilio's first-mover advantage has been significantly eroded.** Vonage launched an official MCP tooling server in December 2025 — open-source, MCP-compliant, works with Claude/Cursor/VS Code. Sinch followed with a production-ready MCP server covering SMS, WhatsApp, RCS, email, and voice verification. Bandwidth launched its own MCP server with official documentation. Plivo has community implementations. Twilio still leads on raw API breadth (~2,000 endpoints) but is now competing on a level playing field for basic CPaaS agent tasks — while remaining the only one still labeled alpha.

## Known Issues

1. **Context window overflow** — Loading all ~2,000 endpoints will exceed any LLM's tool limit. You must filter with `--services` and `--tags`. Cursor's free plan limits tools to 40, which a single unfiltered Twilio service can exceed.

2. **Alpha status** — Published under `@twilio-alpha` scope. The team explicitly labels this as experimental. API surface and behavior may change without notice.

3. **Cost amplification** — Benchmarks showed 27.5% higher token costs with MCP enabled, due to cached context overhead. For simple tasks, the cost increase may not justify the reliability improvement.

4. **Credential exposure** — API key and secret are passed as command-line arguments, which may be visible in process listings. The serverless deployment avoids this but requires Twilio Functions.

5. **No granular tool selection** — Filtering is by service name and OpenAPI tag, not by individual tool. You can't expose "just sendMessage" — you get all endpoints tagged under that tag group.

6. **10 open issues, 9 open PRs** — Active development but unresolved issues suggest the project is still maturing. Limited contributor base (primarily ETI team).

7. **No built-in rate limiting** — The MCP server doesn't enforce rate limits beyond what Twilio's API applies. An unconstrained agent could rack up significant charges quickly.

8. **10DLC compliance** — SMS to US phone numbers requires 10DLC registration and campaign verification, which the MCP server doesn't handle. Your Twilio account must be configured separately.

## Bottom Line

The Twilio MCP server is the **most ambitious communications MCP integration in terms of raw API breadth** — no other CPaaS provider exposes ~2,000 endpoints via MCP. The OpenAPI-to-MCP generator approach is clever: it scales automatically as Twilio adds APIs, and the generic `openapi-mcp-server` package can be reused for any OpenAPI spec.

The practical challenge is curation. Loading everything at once is counterproductive, so you're essentially building a custom MCP configuration per use case by filtering services and tags. The alpha status and 27.5% cost increase in benchmarks are real concerns, but the 100% success rate (vs 92.3% without MCP) and 20.5% speed improvement are meaningful for production workflows.

**The landscape has shifted.** As of May 2026, if you simply need to send an SMS or make a voice call via an AI agent, Vonage and Sinch offer stable, production-ready MCP alternatives. Bandwidth has official MCP docs. Twilio is still the right choice if you need deep integrations (TaskRouter, Studio, Serverless, Flex, SuperSIM, Verify, Sync), if you're already on Twilio, or if you want the broadest possible API surface. But the "Twilio is the only CPaaS with an MCP server" argument no longer holds.

If you're already on Twilio and want AI agents to manage your communications infrastructure, this remains the clear choice. If you're choosing a CPaaS provider partly based on AI agent support, the competitive field has leveled — evaluate all four (Twilio, Vonage, Sinch, Bandwidth) rather than defaulting to Twilio on MCP grounds alone.

**Rating: 3 / 5** *(updated May 2026, down from 3.5)* — Massive API surface and reusable OpenAPI generator approach remain genuine strengths. Drops half a point because: the first-mover CPaaS MCP advantage is gone (Vonage, Sinch, Bandwidth all launched stable/production-ready servers), Twilio remains in alpha while competitors ship production releases, and the April 12 last commit suggests development has slowed. Core tradeoffs unchanged: context window challenges, 27.5% cost increase in benchmarks, credential exposure in CLI args. If you're already a Twilio customer, use it — but don't choose Twilio over competitors specifically for MCP.
