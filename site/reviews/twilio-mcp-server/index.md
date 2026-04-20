# Twilio MCP Server — All 2,000 Twilio APIs Available to Your AI Agent

> Twilio's official MCP server exposes nearly 2,000 API endpoints across SMS, voice, video, conversations, and 40+ services to AI agents.


**At a glance:** [GitHub](https://github.com/twilio-labs/mcp) — 96 stars, TypeScript, ISC license, 101 commits, ~2,000 API endpoints across 40+ services, stdio + Streamable HTTP transport, API key auth. Official first-party from [Twilio Labs](https://github.com/twilio-labs) ([Twilio Inc.](https://www.twilio.com/), NYSE: TWLO).

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
| Ongoing | 101 commits, 10 open issues, 9 open PRs |

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

| Feature | Twilio MCP | Vonage API (no MCP) | Plivo (no MCP) | Sinch (no MCP) |
|---------|-----------|-------------------|----------------|----------------|
| **MCP server** | Yes, official | No | No | No |
| **API endpoints** | ~2,000 | ~200+ | ~100+ | ~150+ |
| **SMS pricing (US)** | $0.0083 | $0.0068 | $0.0055 | Varies |
| **Voice pricing (US)** | $0.014/min | $0.0127/min | $0.010/min | Varies |
| **Open source** | Yes (ISC) | N/A | N/A | N/A |
| **Transport** | stdio + Streamable HTTP | N/A | N/A | N/A |
| **Free tier** | Trial credits only | Trial credits | Trial credits | Trial credits |
| **Channels** | SMS, voice, video, email, chat | SMS, voice, video | SMS, voice | SMS, voice, video |

As of this writing, **none of Twilio's major CPaaS competitors offer official MCP servers**. This gives Twilio a significant first-mover advantage in the AI agent ecosystem. Third-party community servers exist for SMS via various providers, but nothing comparable in scope.

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

The Twilio MCP server is the **most ambitious communications MCP integration available** — no other CPaaS provider has anything close to exposing ~2,000 API endpoints via MCP. The OpenAPI-to-MCP generator approach is clever: it scales automatically as Twilio adds APIs, and the generic `openapi-mcp-server` package can be reused for any OpenAPI spec.

The practical challenge is curation. Loading everything at once is counterproductive, so you're essentially building a custom MCP configuration per use case by filtering services and tags. The alpha status and 27.5% cost increase in benchmarks are real concerns, but the 100% success rate (vs 92.3% without MCP) and 20.5% speed improvement are meaningful for production workflows.

If you're already on Twilio and want AI agents to manage your communications infrastructure, this is the clear choice. If you're choosing a CPaaS provider partly based on AI agent support, Twilio's first-mover MCP advantage is worth factoring in.

**Rating: 3.5 / 5** — Massive API surface and genuine first-mover advantage in CPaaS MCP integration. Open-source with a reusable OpenAPI generator. Loses points for alpha status with uncertain roadmap, context window challenges requiring manual filtering, 27.5% cost increase in benchmarks, credential handling concerns, and no competing MCP servers to pressure improvements. The "expose everything via OpenAPI" approach trades depth for breadth — you get coverage of 40+ services but no hand-tuned tool descriptions or agent-friendly abstractions.

