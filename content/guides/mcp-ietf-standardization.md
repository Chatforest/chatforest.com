---
title: "MCP Reaches the IETF: 15+ Internet-Drafts and What They Mean for the Protocol's Future"
date: 2026-04-05T18:00:00+09:00
description: "MCP has moved beyond Anthropic's GitHub repo into formal internet standards. We analyze 15+ IETF Internet-Drafts covering mcp:// URI schemes, cryptographic security layers, QUIC transport, and network management — and what this means for MCP's maturation."
content_type: "Guide"
card_description: "15+ IETF Internet-Drafts now reference MCP. From the mcp:// URI scheme to cryptographic agent passports to QUIC transport, the protocol is being pulled into the formal standards track. Here's what's happening and why it matters."
last_refreshed: 2026-04-05
---

Something significant is happening in the IETF datatracker. As of April 2026, over 15 active Internet-Drafts directly reference or extend the Model Context Protocol. They cover server discovery, cryptographic security, high-performance transport, and network management — submitted by authors at Cisco, Google, Huawei, Deutsche Telekom, Orange, Telefonica, and independent researchers.

None of these drafts have been adopted by an IETF working group yet. No MCP working group exists. But the volume and breadth of submissions signals something important: MCP is being pulled into the formal internet standards process from the bottom up, by engineers who see it as infrastructure rather than a product feature.

This article maps the landscape of MCP-related IETF activity, explains what each major draft proposes, and assesses what this means for the protocol's future. Our analysis draws on published IETF Internet-Drafts, the MCP specification, Linux Foundation governance documents, and community discussions — we research and analyze rather than testing implementations ourselves. [Rob Nugen](https://robnugen.com) operates ChatForest; the site's content is researched and written by AI.

## Why IETF Involvement Matters

The IETF (Internet Engineering Task Force) is where internet protocols get standardized. HTTP, TLS, DNS, WebSocket, QUIC — all went through the IETF process. Getting a protocol into the IETF doesn't just add a stamp of approval; it provides:

- **Formal URI scheme registration** through IANA (Internet Assigned Numbers Authority)
- **Interoperability guarantees** through rigorous review and test vectors
- **Long-term stability** — IETF RFCs don't disappear when a company pivots
- **Cross-industry legitimacy** — telecom operators, network vendors, and enterprise IT trust IETF standards

MCP was contributed to the Linux Foundation in December 2025 as part of the Agentic AI Foundation (AAIF). Its internal governance uses Specification Enhancement Proposals (SEPs) for protocol changes. But SEPs are project-internal — the IETF drafts represent external engineers saying "this protocol needs to work at internet scale, and we need formal standards to make that happen."

The current stage is early. All existing drafts are individual submissions — they represent their authors' views, not IETF consensus. This is comparable to where WebRTC and QUIC were before formal working groups formed. The key question is whether the volume of submissions triggers working group formation in 2026-2027.

## The Discovery Problem: mcp:// URI Scheme

**Draft:** `draft-serra-mcp-discovery-uri-04` (Marco Serra, Mumble Group, Milan)
**Last updated:** March 26, 2026 | **Status:** Individual submission, Informational

The most ambitious IETF MCP draft tackles a fundamental problem: how do you find and identify MCP servers on the internet?

Today, connecting to an MCP server requires knowing its exact endpoint URL and transport type. There's no standardized way to discover what MCP servers a domain offers, what capabilities they have, or what authentication they require — before connecting. Serra's draft proposes four things to fix this:

### 1. The `mcp://` URI Scheme

A new URI scheme for machine-to-machine identification of MCP servers:

```
mcp://example.com
mcp://api.example.com:8080/v2
```

This is syntactically identical to HTTPS URIs but signals "this is an MCP endpoint" rather than a web page. The draft requests formal IANA registration of the scheme.

### 2. Dual-Mode Discovery

Two discovery mechanisms, designed to work together:

**Base Mode** — An HTTP GET request to `https://{host}/.well-known/mcp-server` returns a JSON manifest describing the server's identity, transport, capabilities, and authentication requirements. This works on any web host, including shared hosting.

**Fast Mode** — A DNS TXT query to `_mcp.{host}` returns a compact record:

```
v=mcp1; src=https://example.com/.well-known/mcp-server; auth=oauth2
```

This provides sub-10ms confirmation that an MCP server exists at a domain, without TLS handshake overhead. The full manifest is then fetched via Base Mode. If both modes are present, the `.well-known` manifest takes precedence.

If neither mode returns results, a fallback direct MCP handshake at `https://{host}/mcp` is attempted.

### 3. Security Capability Negotiation

The manifest includes trust classification before any connection is made:

- **`public`** — Open access, no authentication
- **`sandbox`** — Temporary/evaluation, requires expiration date
- **`enterprise`** — Requires authentication
- **`regulated`** — Requires authentication, compliance certification, and audit logging

Authentication methods are advertised upfront: `none`, `bearer`, `mtls`, `apikey`, `oauth2`, plus extension methods prefixed with `x-`.

### 4. Pre-Connection Capability Previews

Optional `tools_preview`, `resources_preview`, and `prompts_preview` arrays let clients see what a server offers before connecting. This enables registry indexing, search engines, and agent planning without establishing MCP sessions.

The draft also supports payment advertisement — a `payment_required` flag with supported methods including `x402` (the newly standardized payment protocol), `mpp-tempo`, `stripe`, and API keys.

### Relationship to SEP-2127 (Server Cards)

MCP's own maintainers have a parallel proposal: SEP-2127, "MCP Server Cards," proposed by lead maintainer David Soria Parra. Server Cards use `/.well-known/mcp-server-card/{server-name}` for pre-connection identity and transport discovery.

The two proposals are **complementary rather than competing.** Serra's draft (revision 04) explicitly includes a `server_card` field that can point to a SEP-2127 Server Card URL. The key differences:

| | SEP-2127 (Server Cards) | draft-serra (IETF Discovery) |
|---|---|---|
| **Governed by** | MCP project (LF Projects) | IETF individual submission |
| **Scope** | Identity, transport, capability discovery | URI scheme + DNS + security + payments |
| **Primitive previews** | Excluded (servers are dynamic) | Included (optional) |
| **DNS discovery** | Not included | TXT records at `_mcp.{host}` |
| **IANA registration** | Not applicable | URI scheme + well-known suffix |

In practice, SEP-2127 could become the canonical internal discovery mechanism while the IETF draft handles internet-scale concerns like URI registration and DNS integration.

A reference implementation exists at [mcpstandard.dev](https://mcpstandard.dev) with a Python client library and CMS plugins for WordPress and Django.

## Cryptographic Security: Agent Passports and Signed Messages

**Draft:** `draft-sharif-mcps-secure-mcp-00` (Raza Sharif, CyberSecAI Ltd)
**Published:** March 14, 2026 | **Status:** Individual submission

With [36 CVEs filed against MCP servers](/guides/mcp-security-landscape-2026/) and 84.2% of tool poisoning attacks succeeding against auto-approve configurations, the security gap in MCP is well-documented. Sharif's MCPS (secure MCP) draft proposes a cryptographic layer that addresses four specific threats:

### Agent Passports

A JSON credential binding an ECDSA P-256 public key to an agent identity and origin URI. Think of it as a TLS certificate for AI agents — it proves who the agent is and where it comes from.

Passports have five trust levels:

- **L0 (None):** Self-signed, no verification
- **L1 (Signed):** Issued by any Trust Authority
- **L2 (Verified):** Issued by a recognized Trust Authority
- **L3 (Strict):** L2 plus tool signatures and verified origin ownership
- **L4 (Full):** L3 plus mutual authentication and real-time revocation checking

Trust Authorities are fully self-hostable and distribute public keys via HTTPS JWK endpoints. They support X.509-style issuer chains (max depth 5) with revocation via CRL-style lists or OCSP-style per-passport checks.

### Per-Message Signing

Every JSON-RPC message gets a signed envelope containing the message hash, a cryptographic nonce, a timestamp, and the passport ID. This ensures message integrity and non-repudiation — you can prove exactly which agent sent which request.

The cryptographic specifics: ECDSA P-256 per FIPS 186-5, deterministic signatures per RFC 6979, and RFC 8785 JSON Canonicalization Scheme (JCS) for canonical serialization.

### Tool Definition Integrity

Tool definitions — name, description, input schema, author origin — can be cryptographically signed. Clients maintain "pin stores" mapping server origins and tool names to expected hashes. This directly addresses tool poisoning: if a malicious server modifies a tool description, the signature check fails.

### Replay Protection

16-byte cryptographic nonces with configurable timestamp windows (30-3600 seconds, default 300). Nonce stores key on the nonce string value to prevent ECDSA signature malleability attacks.

### Backward Compatibility

MCPS adds an `mcps` field at the top level of JSON-RPC messages. Non-MCPS implementations simply ignore it. Capability negotiation happens during the standard MCP `initialize` handshake, with transcript binding after init to detect downgrade attacks.

The draft defines 15 dedicated error codes (-33001 through -33015) covering passport, signature, replay, trust level, and chain violations.

### Assessment

This is arguably the most important IETF MCP draft from a practical standpoint. The MCP specification currently has no built-in message-level security — it relies on transport security (TLS) and application-level authentication. MCPS would add defense-in-depth against the [supply chain attacks](/guides/mcp-attack-vectors-defense/) and tool poisoning that have plagued the ecosystem.

The challenge is adoption. Adding cryptographic signing to every message introduces latency and complexity. Whether the ecosystem accepts that tradeoff depends on how severe production security incidents become in 2026.

## High-Performance Transport: MCP over QUIC

**Draft:** `draft-jennings-ai-mcp-over-moq-00` (Cullen Jennings/Cisco, Ian Swett/Google, Jonathan Rosenberg/Five9, Suhas Nandakumar/Cisco)
**Published:** March 2, 2026 | **Status:** Individual submission

The biggest names on any MCP-related IETF draft are on this one. Cullen Jennings (Cisco Fellow, former IETF Area Director) and Ian Swett (Google, QUIC working group contributor) propose transporting MCP over MOQT — Media over QUIC Transport.

### Why QUIC for MCP?

Current MCP transports (stdio, SSE, Streamable HTTP) work well for single-server, single-client scenarios. But they struggle with:

- **Multi-agent fan-out** — An orchestrator sending requests to dozens of MCP servers simultaneously
- **Head-of-line blocking** — A slow tool response blocks other messages on the same HTTP/2 connection
- **Relay and caching** — No built-in support for intermediary nodes that aggregate, cache, or route MCP traffic

MOQT, built on QUIC, provides multiplexed streams without head-of-line blocking, built-in relay support, subscription-based message routing, and priority management.

### How It Works

The draft maps MCP primitives to dedicated MOQT tracks — seven track types covering tool calls, resource subscriptions, prompt requests, notifications, and control messages. Each track operates independently, so a slow tool execution doesn't block notifications or other tool calls.

Relay nodes can aggregate subscriptions and cache responses, enabling architectures where hundreds of agents share tool results without each making independent requests.

### Assessment

This draft is forward-looking. Current MCP deployments don't typically need QUIC-level performance. But as multi-agent architectures scale — think [Pinterest's 66K monthly invocations](/guides/mcp-in-production/) multiplied across enterprise deployments — transport efficiency becomes a real bottleneck. The author pedigree suggests this reflects genuine engineering needs at Cisco and Google.

## Network Management: Huawei's MCP Push

The largest cluster of IETF MCP drafts — at least six — comes from Huawei, with co-authors at Deutsche Telekom, Telefonica, and Orange Research. This represents the telecom industry's attempt to bring MCP into network operations.

### The Core Proposal

**Draft:** `draft-yang-nmrg-mcp-nm-02` (Yuanyuan Yang and Qin Wu/Huawei, Diego Lopez/Telefonica, Nathalie Romo Moreno/Deutsche Telekom, Lionel Tailhardat/Orange)
**Last updated:** February 24, 2026

The flagship draft defines four deployment patterns for MCP in network management:

1. **Element-to-element** — Network devices expose MCP servers directly
2. **Controller-to-external** — Network controllers (SDN, orchestrators) provide MCP interfaces to AI agents
3. **Standalone server** — Dedicated MCP servers wrapping network management APIs
4. **Gateway-to-device** — MCP gateways translating between AI agents and NETCONF/RESTCONF/YANG-managed devices

Crucially, MCP works **alongside** existing network management protocols, not as a replacement. NETCONF and RESTCONF handle device configuration; MCP provides the AI-friendly interface layer for intent translation and closed-loop automation.

### Supporting Drafts

The Huawei team has submitted specialized drafts for:

- **Troubleshooting** (`draft-zm-rtgwg-mcp-troubleshooting-01`) — Intent-based, natural-language-driven network troubleshooting
- **Network measurement** (`draft-zm-rtgwg-mcp-network-measurement-01`) — Devices as MCP servers exposing measurement tools
- **Equipment management** (`draft-zw-opsawg-mcp-network-mgmt-00`) — Capability tokens, tools, resources, and error codes for network devices
- **MCP + A2A for network management** (`draft-zeng-opsawg-applicability-mcp-a2a-00`) — Argues MCP and Google's A2A protocol complement NETCONF for cross-domain multi-agent workflows

These drafts are being discussed within the NMRG (Network Management Research Group), which is a research group rather than a standards-track working group. They've been presented at IETF 123, 124, and 125.

### Why This Matters

The telecom industry has historically been slow to adopt new protocols but immovable once committed. Four major European telecom operators co-authoring MCP drafts signals that network equipment vendors will need MCP support. If Huawei ships MCP in its routers and switches, every network operator evaluating that equipment gets MCP exposure.

## Other Notable Drafts

### SIP Extension for MCP

**Draft:** `draft-howe-sipcore-mcp-extension-00` (Thomas McCarthy-Howe)

Proposes embedding MCP payloads in SIP (Session Initiation Protocol) session setup, using a new `application/mcp+json` media type. This would enable MCP capability negotiation during VoIP call setup — imagine an AI agent joining a conference call and discovering available tools through the SIP handshake. The draft expired in March 2026 but represents an interesting intersection of telecom and AI protocols.

### Multi-Agent Collaboration via Agent Gateways

**Draft:** `draft-li-dmsc-mcps-agw-00` (Xueting Li), now replaced by `draft-li-dmsc-macp`

Proposes Agent Gateways as control-plane entities handling agent registration, authentication, capability management, and semantic routing. This overlaps with the [MCP gateway pattern](/guides/mcp-gateway-proxy-patterns/) discussion but frames it as formal internet infrastructure rather than application architecture.

## The Big Picture: Where Is MCP Heading?

The IETF activity reveals four trends about MCP's trajectory:

### 1. MCP Is Being Treated as Internet Infrastructure

The discovery draft seeks IANA registration. The security draft defines formal error codes and trust hierarchies. The transport draft maps to QUIC. These aren't application-level concerns — they're the kind of plumbing that internet protocols need. The authors are treating MCP as something that will be as fundamental to AI agent communication as HTTP is to web communication.

### 2. Security Is the Biggest Gap

MCPS (the cryptographic security draft) exists because MCP's current security model — rely on transport TLS and hope for the best — is inadequate for production. Agent Passports, message signing, and tool integrity checking address real, documented attack vectors. Whether through this specific draft or another mechanism, MCP needs message-level security before enterprise adoption can scale.

### 3. Telecom Wants In

Six drafts from Huawei with European telecom co-authors, presented at three consecutive IETF meetings. This isn't casual interest — it's a coordinated push to make MCP relevant to network management. Telecom adoption would dramatically expand MCP's footprint beyond the AI/ML developer community.

### 4. No Working Group Yet — But Momentum Is Building

All current drafts are individual submissions. No IETF working group has been chartered for MCP. But 15+ drafts from authors at Cisco, Google, Huawei, Deutsche Telekom, Telefonica, Orange, and Five9 — with presentations at multiple IETF meetings — creates pressure for formalization. The formation of an MCP-related IETF working group in late 2026 or 2027 would be a major milestone.

## What This Means for MCP Users Today

If you're building with MCP today, the IETF drafts don't change anything immediately. They're proposals, not standards. But they signal where the protocol is heading:

- **Discovery will get standardized.** Whether through the IETF draft, SEP-2127 Server Cards, or both, the days of manually configuring MCP server endpoints are numbered. Plan for dynamic discovery in your architectures.

- **Cryptographic security is coming.** MCPS or something like it will likely become expected for production deployments. Start thinking about agent identity and message integrity now.

- **Transport options will expand.** QUIC/MOQT transport would change the performance characteristics of multi-agent systems. If you're building agent orchestration, watch this space.

- **Enterprise/telecom adoption is accelerating.** The network management drafts mean MCP is being evaluated for environments with very different requirements than AI coding assistants. This will drive protocol maturity.

For a broader view of MCP's direction, see our [MCP 2026 Roadmap guide](/guides/mcp-2026-roadmap-whats-coming/) and [MCP Ecosystem State of the Standard](/guides/mcp-ecosystem-2026-state-of-the-standard/).

## Sources

- [IETF Datatracker: draft-serra-mcp-discovery-uri-04](https://datatracker.ietf.org/doc/draft-serra-mcp-discovery-uri/)
- [IETF Datatracker: draft-sharif-mcps-secure-mcp-00](https://datatracker.ietf.org/doc/draft-sharif-mcps-secure-mcp/)
- [IETF Datatracker: draft-jennings-ai-mcp-over-moq-00](https://datatracker.ietf.org/doc/draft-jennings-ai-mcp-over-moq/)
- [IETF Datatracker: draft-yang-nmrg-mcp-nm-02](https://datatracker.ietf.org/doc/draft-yang-nmrg-mcp-nm/)
- [MCP SEP-2127: Server Cards](https://github.com/modelcontextprotocol/specification/discussions/2127)
- [MCP Governance — Linux Foundation](https://github.com/modelcontextprotocol/organization)
- [MCP 2026 Roadmap — Official Blog](https://blog.modelcontextprotocol.io/posts/2026-mcp-roadmap/)
