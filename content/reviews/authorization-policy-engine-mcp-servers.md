---
title: "Authorization & Policy Engine MCP Servers — ToolHive, Cedar for Agents, Cerbos, Permit.io, OPA, and More"
date: 2026-04-25T23:30:00+09:00
description: "Authorization and policy engine MCP servers reviewed: ToolHive (2.0K stars, Go, v0.44.0), IBM ContextForge (4.4K stars, v1.0.8), Cedar for Agents (46 stars, Rust, schema-generator v0.6.0), Cerbos (4.6K stars, v0.55.0), Microsoft Agent Governance Toolkit (6.1K stars, OWASP Agentic Top 10), Sondera coding agent hooks (222 stars, Cedar for Claude Code/Cursor), Permit.io, ScopeBlind, Oso Cloud MCP. Rating: 4.0/5."
og_description: "Authorization & policy engine MCP servers: ToolHive (2.0K stars, v0.44.0), IBM ContextForge (4.4K stars, v1.0.8), Microsoft Agent Governance Toolkit (6.1K stars, OWASP Agentic Top 10), Cerbos (4.6K stars), Cedar for Agents (46 stars, v0.6.0). Rating: 4.0/5."
content_type: "Review"
card_description: "Authorization and policy engine tools for controlling what AI agents can do through MCP servers — enforcing who can call which tools, with what parameters, under what conditions. **Enterprise platform** — stacklok/toolhive (2.0K stars as of Aug 2026, Apache-2.0, Go) is an enterprise-grade MCP server management platform with Cedar-based authorization built in, now at v0.44.0 (Aug 18, 2026) after sustained weekly releases: CIMD auth replacing Dynamic Client Registration, Interactive TUI dashboard, RFC 7523 JWT Bearer grant, Windows named-pipe support, Redis session storage, Playground agents. **Unified PDP** — IBM/mcp-context-forge (4.4K stars, Apache-2.0, Python) shipped v1.0.1 GA May 13, 2026 and has continued a monthly release cadence to v1.0.8 (Aug 18, 2026). CPEX external plugin framework (breaking change for plugin authors), CSRF token validation, SIEM integration, Admin UI gateway management tables. **Enterprise governance** — microsoft/agent-governance-toolkit (6.1K stars as of Aug 2026, up from 1.6K in May, MIT, multi-language) covers all 10 OWASP Agentic Top 10 items: policy enforcement, zero-trust identity, execution sandboxing, reliability engineering. Integrates with ScopeBlind for cryptographic audit trails. **Cedar + MCP** — cedar-policy/cedar-for-agents (46 stars, Apache-2.0, Rust) provides official AWS Cedar tooling for MCP. cedar-policy-mcp-schema-generator has moved from v0.5.0 (May 12) to v0.6.0 (May 26, with Python and Wasm builds following in June). **Coding agent hooks** — sondera-ai/sondera-coding-agent-hooks (222 stars, MIT, Rust) intercepts shell, file, and web requests across Claude Code, Cursor, GitHub Copilot, and Gemini CLI with Cedar policies. Normalizes tool names across agents for unified rules. **Policy engine** — cerbos/cerbos (4.6K stars, Apache-2.0, Go), now v0.55.0 (Aug 13, 2026), sub-1ms latency, YAML policies. **Authorization gateway** — Permit.io MCP Gateway drop-in proxy; permitio/permit-fastmcp (17 stars, unchanged) is an open-source piece but its last commit is from September 2025 — treat it as early-stage/dormant rather than actively maintained. **Cloud authorization** — Oso Cloud MCP for managing Oso authorization policies via AI tools. **Identity gateway** — Strata Maverics with embedded OPA, 5-second TTL task-scoped tokens. **Cryptographic receipts** — ScopeBlind/scopeblind-gateway (9 stars, MIT) with Ed25519-signed decisions and CVE-anchored Cedar policies — contrary to an earlier audit, the repo saw heavy commit activity through July 2026 (protect-mcp releases up to v0.10.1). Rating: 4.0/5 — Cedar has won the MCP authorization conversation (ToolHive, IBM ContextForge, Cedar for Agents, ScopeBlind, Sondera), with Microsoft's entry signaling enterprise maturation. Deducted 1.0 for no single standard, OPA tooling still thin relative to Cedar, and most production-grade features requiring commercial tiers."
last_refreshed: 2026-08-25
sources_audited: 2026-08-25
---

Your MCP server exposes 47 tools. Your AI agent has access to all of them. The intern's coding assistant can delete production databases, the contractor's IDE can read HR files, and nobody knows who called what tool, when, or why it was allowed.

The MCP specification formally classified MCP servers as OAuth Resource Servers in late 2025, but authentication alone doesn't solve authorization. Knowing *who* is calling isn't the same as deciding *what they're allowed to do*. That's where policy engines come in — they evaluate fine-grained rules (role, resource, action, context) at the tool-call level, turning "authenticated request" into "authorized action."

This review covers **policy engines and authorization frameworks specifically integrated with MCP** — the tools that decide whether a given agent, user, or role can call a specific tool with specific parameters. For MCP proxy infrastructure, see [MCP Proxy, Router & Aggregator Tools](/reviews/mcp-proxy-router-aggregator-servers/). For API gateway MCP support, see [API Gateway & API Management](/reviews/api-gateway-api-management-mcp-servers/). For supply chain security, see [AI Agent Supply Chain Security](/reviews/ai-agent-supply-chain-security-mcp-servers/).

Part of our **[Security MCP category](/categories/security/)**. The headline finding: **Cedar has emerged as the dominant policy language for MCP authorization** — adopted by ToolHive ([2.0K stars](https://github.com/stacklok/toolhive) as of this Aug 2026 audit), IBM ContextForge ([4.4K stars](https://github.com/IBM/mcp-context-forge)), AWS Cedar for Agents, and ScopeBlind. OPA remains important for enterprise identity gateways (Strata Maverics) but has less MCP-native tooling. The building blocks for production authorization are here, but no single standard has won.

**Correction (2026-08-25 audit):** all star counts and version numbers in this review have been refreshed against live GitHub data — most moved substantially in the ~3 months since the last audit (ToolHive nearly +200 stars and 16 releases ahead; Microsoft's Agent Governance Toolkit nearly 4x'd from 1.6K to 6.1K stars). See the per-server sections below for current figures and sources.

## MCP Server Management with Built-in Authorization

### stacklok/toolhive

| Server | Stars | Language | License | MCP Features |
|--------|-------|----------|---------|--------------|
| [toolhive](https://github.com/stacklok/toolhive) | 2,038 | Go | Apache-2.0 | Cedar-based authorization |

**Enterprise-grade MCP server management platform with Cedar authorization built in.** ToolHive runs MCP servers in containers and enforces Cedar policies on every tool call. **Correction (2026-08-25 audit):** star count and version updated — [2,038 stars](https://github.com/stacklok/toolhive) (up from 1,814 in May) and the [latest release is v0.44.0](https://github.com/stacklok/toolhive/releases) (Aug 18, 2026), 16 releases past the v0.28.1 this review originally described, confirming the sustained weekly-release velocity:

- **Default-deny posture** — if no policy matches, the request is denied. Deny rules take absolute precedence over permits. This is the security model you want for production
- **Cedar policy language** — `permit(principal, action == Action::"call_tool", resource) when { principal.claim_roles.contains("admin") }` — clear, auditable, declarative
- **CIMD auth** (May 2026) — Client ID Metadata Document authentication replaces Dynamic Client Registration. Clients now present hosted metadata documents verified on-the-fly rather than pre-registering with identity providers — simpler operational model for fleet deployments
- **RFC 7523 JWT Bearer grant** (v0.28.0) — standardized machine-to-machine auth for agent-to-MCP server flows
- **Interactive TUI dashboard** (v0.26.0) — real-time management of MCP servers without leaving the terminal
- **Windows named-pipe support** (v0.27.1) — production-ready on Windows Server with DACL restriction to creating user
- **AWS STS auth** (v0.26.0) — vMCP gains AWS STS authentication type for cloud-native deployments
- **Dynamic Webhook Middleware** (v0.27.0) — Kubernetes controller for webhook-based policy enforcement
- **Container isolation** — every MCP server runs in its own container with resource limits and network controls
- **Kubernetes operator** — fleet management of MCP servers across clusters with CRDs
- **Registry server** — [toolhive-registry-server](https://github.com/stacklok/toolhive-registry-server) provides organizational governance with JWT-based visibility controls and multi-source aggregation
- **Playground agents** (May 2026) — built-in ToolHive Assistant and Skill Engineer agents available to all users

**Why it matters:** ToolHive is the most complete answer to "how do I run MCP servers in production with proper access control." The CIMD auth change is significant — removing the friction of Dynamic Client Registration makes ToolHive more viable for large-scale enterprise deployments where pre-registering every agent is impractical. The Windows support opens the Windows Server enterprise market that was previously shut out.

**Limitation:** Requires Docker/Kubernetes — you're running real infrastructure, not a lightweight config. Cedar is less expressive than OPA/Rego for complex conditional logic. Commercial tier (Stacklok Enterprise) adds team management features and hardened images.

## Unified Policy Decision Points

### IBM/mcp-context-forge (ContextForge)

| Server | Stars | Language | License | MCP Features |
|--------|-------|----------|---------|--------------|
| [mcp-context-forge](https://github.com/IBM/mcp-context-forge) | 4,364 | Python | Apache-2.0 | Cedar/OPA/RBAC unified PDP |

**AI gateway and registry with a pluggable unified policy decision point supporting Cedar, OPA, and native RBAC.** IBM's ContextForge federates MCP, A2A, and REST/gRPC APIs behind a single governed gateway. **v1.0.1 GA shipped May 13, 2026** — the project is no longer in release-candidate status. **Correction (2026-08-25 audit):** star count and version updated — [4,364 stars](https://github.com/IBM/mcp-context-forge) (up from 3,739 in May) and the project has kept a steady cadence since GA, now at [v1.0.8](https://github.com/IBM/mcp-context-forge/releases) (Aug 18, 2026):

- **Unified PDP** — a single policy evaluation interface across Cedar policies, OPA Rego rules, native RBAC, and MAC (mandatory access control). Combination logic determines how multiple engines interact
- **Enterprise security** — credential protection, SSRF prevention, multi-tenant isolation, rate limiting with user-scoped controls; v1.0.1 adds CSRF token validation, nonce-based CSP headers, and SIEM integration
- **CPEX external plugin framework** — v1.0.1 migrates plugins to an external CPEX package. This is a breaking change for existing plugin authors — import paths changed. New plugins must target CPEX
- **Admin UI improvements** — gateway management tables, advanced MCP server configuration forms, real-time log monitoring
- **Multi-protocol** — not just MCP — also supports A2A (Agent-to-Agent) and REST/gRPC APIs, providing one governance layer for all agent communication
- **OAuth integration** — user-scoped OAuth tokens, JWT secret management (32-byte minimum), Bearer token generation
- **Alembic migration safety** — improved database migration handling in v1.0.1

**Why it matters:** ContextForge reaching v1.0.1 GA is a credibility milestone — IBM is shipping production-ready software, not perpetual betas. The CPEX plugin migration signals a maturing ecosystem: IBM is building a third-party plugin marketplace around the platform. The CNCF [MCP Server Authentication and Authorization Standards initiative](https://github.com/cncf/toc/issues/1890) that ContextForge anticipates remains open (49 comments, last updated Aug 20, 2026 as of this audit — see the [CNCF Standards Work](#cncf-standards-work) section below for what's actually changed), and ContextForge's multi-engine PDP architecture positions it well for whatever standard emerges.

**Limitation:** 4.4K stars is impressive, but it's a big platform to adopt if you just need tool-level authorization. Python-based, so heavier than a Go binary. The CPEX breaking change creates migration friction for early adopters. IBM branding may raise questions about long-term open-source commitment (though Apache-2.0 license is clean).

## Cedar Policy Ecosystem

### cedar-policy/cedar-for-agents

| Server | Stars | Language | License | MCP Features |
|--------|-------|----------|---------|--------------|
| [cedar-for-agents](https://github.com/cedar-policy/cedar-for-agents) | 46 | Rust | Apache-2.0 | Cedar policy + MCP tooling |

**Official AWS Cedar tooling for securing agentic AI workflows through MCP.** Three components bridge Cedar and MCP:

- **mcp-tools-sdk** (Rust) — parses and manipulates MCP tool metadata, enabling Cedar policies to reference tool names, parameters, and descriptions. **Correction (2026-08-25 audit):** now at [mcp-tools-sdk v0.4.0](https://github.com/cedar-policy/cedar-for-agents/releases) (released May 26, 2026), up from v0.3.0
- **cedar-policy-mcp-schema-generator** (Rust) — auto-generates a Cedar Schema from an MCP server's tool descriptions. **v0.5.0 released May 12, 2026;** **Correction (2026-08-25 audit):** superseded by [v0.6.0](https://github.com/cedar-policy/cedar-for-agents/releases) (May 26, 2026), with matching Python and Wasm builds (`cedar-policy-mcp-schema-generator-python-v0.6.0` and `-wasm-v0.6.0`) released in June 2026. Feed it your server's tool list, get a complete Cedar schema for writing type-safe policies
- **cedar-analysis-mcp-server** (TypeScript) — an MCP server exposing Cedar's analysis capabilities to AI agents, enabling policy verification and conflict detection through natural language

**Why it matters:** This is the *official* Cedar team's answer to MCP authorization. The schema generator is the key piece — it means Cedar policies for MCP tools can be validated at write time, not just runtime. Development has continued well past the "commits through May 20" this review originally noted — the repo was [last pushed to Aug 24, 2026](https://github.com/cedar-policy/cedar-for-agents), confirming AWS is treating this as an ongoing investment, not a one-time release. If you're building Cedar-based authorization for MCP, this is the foundation library.

**Limitation:** 46 stars (up from 25 in May, still small) reflects AWS-project discovery patterns, not quality. The Rust crates require Rust toolchain integration. The TypeScript MCP server is focused on analysis (inspecting policies), not enforcement (blocking tool calls) — you still need a runtime like ToolHive or ScopeBlind for that.

### ScopeBlind/scopeblind-gateway (protect-mcp)

| Server | Stars | Language | License | MCP Features |
|--------|-------|----------|---------|--------------|
| [scopeblind-gateway](https://github.com/scopeblind/scopeblind-gateway) | 9 | TypeScript | MIT | Cedar + cryptographic receipts |

**Enterprise security gateway that evaluates Cedar policies on AI agent tool calls and signs decisions as cryptographic receipts.** protect-mcp adds policy enforcement and audit to any MCP server without modifying it:

- **Cedar policy enforcement** — deny decisions are architecturally final and cannot be overridden by the model or other hooks. Auto-suggests `permit()` rules when tools are denied
- **Ed25519 signed receipts** — every policy decision is cryptographically signed (RFC 8032) with JCS canonicalization (RFC 8785). Receipts are offline-verifiable — no server contact needed
- **CVE-anchored policies** — ships with real-world incident-focused configurations: clinejection.json (CVE-2025-6514 MCP OAuth proxy hijacking), terraform-destroy.json (autonomous infrastructure destruction), github-mcp-hijack.json (prompt injection via GitHub issues), data-exfiltration.json, financial-safe.json
- **Two integration modes** — (1) HTTP hook server for Claude Code (port 9377), (2) stdio proxy wrapping any MCP server transparently via `npx protect-mcp -- <server-command>`
- **IETF standards track** — draft-farley-acta-signed-receipts (draft-02 pending), plus Microsoft Agent Governance Toolkit integration (PR #667 merged)
- **External PDP support** — not limited to Cedar — can delegate to OPA, Cerbos, or any HTTP policy endpoint

**Why it matters:** protect-mcp is the only tool producing tamper-evident, cryptographically signed audit trails for MCP tool calls. The CVE-anchored policy templates solve real attack vectors documented in production ([CVE-2025-6514, the mcp-remote OAuth proxy RCE, affected nearly half a million developers](https://jfrog.com/blog/2025-6514-critical-mcp-remote-rce-vulnerability/)). The IETF Internet-Draft signals ambition beyond MCP-specific tooling — these signed receipts could become an industry standard for agent action accountability.

**Limitation:** **Correction (2026-08-25 audit):** the "6 stars unchanged since April, no commits after April 21" claim in an earlier version of this review does not hold up — it has now been re-verified as wrong. [The repo's own commit history](https://github.com/scopeblind/scopeblind-gateway/commits/main) shows a burst of activity through July 2026, including protect-mcp releases 0.9.4 through 0.10.1 (July 7-9, 2026) covering a Cedar fail-open fix in the HTTP gateway, draft-02 Acta envelope support, and a policy CLI (`list`/`show`/`allow`/`deny`). Star count is now 9 (up from 6). GitHub traction is still modest by absolute numbers, but "stalled" is the wrong characterization — this is an actively developed project. The IETF draft and patent filings (5 Australian provisional patents) suggest a commercial play — the open-source core handles auditability while commercial ScopeBlind.com adds privacy-preserving metered authorization via VOPRF-based credentials. The Ed25519 receipts are excellent engineering but add complexity that most teams don't need yet. Microsoft's Agent Governance Toolkit referencing ScopeBlind as an integration is a credibility signal that may drive future discovery.

## Standalone Policy Engines with MCP Integration

### Cerbos

| Server | Stars | Language | License | MCP Features |
|--------|-------|----------|---------|--------------|
| [cerbos](https://github.com/cerbos/cerbos) | 4,551 | Go | Apache-2.0 | YAML policy PDP |

**Open-core, language-agnostic authorization solution with an MCP authorization demo.** Cerbos is a standalone Policy Decision Point (PDP) with sub-1ms latency. v0.53.0 released May 5, 2026. **Correction (2026-08-25 audit):** star count and version updated — [4,551 stars](https://github.com/cerbos/cerbos) (up from 4,415 in May) and [v0.55.0](https://github.com/cerbos/cerbos/releases) (Aug 13, 2026) is now current, two releases past v0.53.0:

- **YAML-defined policies** — declarative access control without learning a new language. Policies reference principals, resources, actions, and conditions in plain YAML
- **MCP demo** — [cerbos-mcp-authorization-demo](https://github.com/cerbos/cerbos-mcp-authorization-demo) shows dynamic tool-level RBAC where tools enable/disable based on Cerbos decisions per request
- **Three-role model** — the demo implements admin (all tools), manager (approval + listing), and user (add + view) roles controlling 6 expense-management MCP tools
- **Stateless PDP** — decouples authorization logic from application code. SDKs for Go, Java, JavaScript, Python, .NET, PHP, Ruby, Rust
- **Deployment flexibility** — Kubernetes, Lambda, containers, edge, air-gapped environments

**Why it matters:** Cerbos is the pragmatic choice for teams that want YAML-based policies without learning Rego or Cedar. The sub-1ms evaluation latency means authorization adds negligible overhead to tool calls. The MCP demo shows the exact integration pattern: register all tools, check Cerbos per call, dynamically toggle tool availability. Continued star growth (+136 since May) reflects ongoing enterprise adoption.

**Limitation:** The MCP demo is just that — a demo (5 stars, JavaScript, unverified this audit — not independently rechecked). Cerbos itself is a mature PDP (4.6K stars) but doesn't have native MCP awareness. You build the MCP integration yourself using the pattern from the demo. Cerbos Hub (commercial) adds management features.

### Permit.io MCP Gateway

| Server | Stars | Language | License | MCP Features |
|--------|-------|----------|---------|--------------|
| [Permit MCP Gateway](https://docs.permit.io/permit-mcp-gateway/) | — | — | Commercial | Drop-in MCP authorization proxy |
| [permit-fastmcp](https://github.com/permitio/permit-fastmcp) | 17 | Python | MIT | FastMCP authorization middleware |

**Drop-in proxy between MCP clients and servers that adds authentication, authorization, consent, and audit to every tool call.** Permit.io wraps its authorization platform (built on OPA + OPAL) as an MCP-aware gateway. The ecosystem now has two layers:

- **Permit MCP Gateway** (hosted) — sits between MCP clients (Claude, Cursor, VS Code) and MCP servers, adds auth/authz/consent/audit without any SDK changes. Real-time Cedar/OPA/RBAC policy evaluation, OIDC integration, audit logging
- **[permit-fastmcp](https://github.com/permitio/permit-fastmcp)** (open-source) — FastMCP middleware that intercepts MCP requests and validates them against Permit.io RBAC/ABAC/ReBAC policies. **Correction (2026-08-25 audit):** this review previously called permit-fastmcp "the actively maintained OSS piece" — re-checked, [its commit history](https://github.com/permitio/permit-fastmcp/commits/main) shows the last commit was Sept 15, 2025, before this review was even first published (April 2026), and star count is flat at 17. That does not support "actively maintained"; treat it as early-stage/dormant open-source rather than a project seeing ongoing investment. permit-mcp (3 stars, access request management, not independently rechecked this audit) is the older, smaller sibling project
- **Multiple policy models** — supports deep RBAC, ABAC, and ReBAC (Relationship-Based Access Control) through Permit's platform
- **OIDC integration** — connects to existing identity providers for agent identification
- **Audit logging** — every authorization decision is logged

**Why it matters:** Permit.io is the "don't build it yourself" option for MCP authorization. The split between the hosted gateway (zero MCP server changes) and permit-fastmcp (SDK-level middleware) gives teams two integration points depending on their architecture. The FastMCP middleware approach is more composable — it works anywhere FastMCP-based servers run.

**Limitation:** The hosted gateway requires a Permit.io subscription. permit-fastmcp is 17 stars, early-stage, and — per the correction above — has had no commits since September 2025. You're adding a cloud dependency to your MCP call path regardless of integration model.

### Oso Cloud MCP

| Server | Stars | Language | License | MCP Features |
|--------|-------|----------|---------|--------------|
| [Oso Cloud MCP](https://www.osohq.com/docs/app-integration/client-apis/cli/mcp) | — | — | Commercial | Authorization co-pilot |

**MCP server providing a complete interface for managing Oso Cloud authorization policies through AI tools.** Bridges AI assistants and Oso's Polar-based authorization platform:

- **Policy explanation** — AI tools can query and explain Oso Cloud authorization policies in natural language
- **Fact querying** — answer specific questions about authorization facts (who has access to what)
- **Test generation** — write authorization tests through AI conversation
- **Authorization debugging** — diagnose why a specific request was allowed or denied
- **Polar language** — Oso's declarative authorization language, designed specifically for authorization logic

**Why it matters:** Oso Cloud MCP is not about enforcing policies on MCP tool calls — it's about making your *existing* authorization system more accessible to developers. If your team already uses Oso Cloud, the MCP server turns your AI assistant into an authorization debugging companion. The Polar language is purpose-built for authorization, avoiding the general-purpose complexity of Rego.

**Limitation:** Requires Oso Cloud subscription. This is a management/debugging tool, not a policy enforcement point for MCP. The `oso-cloud experimental mcp` command signals this is still experimental. The original open-source Oso library (osohq/oso) has been deprecated in favor of the cloud service.

## Identity Gateways with Policy Enforcement

### Strata Maverics AI Identity Gateway

| Server | Stars | Language | License | MCP Features |
|--------|-------|----------|---------|--------------|
| [connect-claude-to-maverics](https://github.com/nickgamb-strata/connect-claude-to-maverics) | — | — | Commercial | OPA-based MCP identity gateway |

**Enterprise AI identity gateway using embedded OPA for fine-grained MCP tool authorization.** Strata's Maverics federates MCP servers through an identity layer:

- **Embedded OPA engine** — evaluates Rego policies on every MCP tool call at request time. Policies inspect token claims and the tool being called, returning allow/deny with reason
- **Ephemeral tokens** — mints task-scoped tokens with 5-second TTLs via RFC 8693 token exchange. Each tool call gets its own short-lived credential
- **Delegation chains** — every action traces back to the authorizing human through a chain of token exchanges
- **Per-tool scoping** — tokens are scoped to the specific tool being called, not the entire MCP server
- **Policy as code** — authorization policies managed in git alongside infrastructure

**Why it matters:** Maverics is the strongest implementation of the "MCP servers are OAuth Resource Servers" principle from the MCP spec. The 5-second TTL on task-scoped tokens is the gold standard for least-privilege — even if a token leaks, it's useless almost immediately. The delegation chain solves the accountability problem: when an agent takes an action, you can trace it back through token exchange to the human who authorized it.

**Limitation:** Commercial product (Strata Identity). The open-source example is a demo, not a deployable product. Requires significant identity infrastructure (OAuth 2.0 authorization server, OPA deployment). Overkill for small teams or development environments.

## Enterprise Governance Frameworks

### microsoft/agent-governance-toolkit

| Server | Stars | Language | License | MCP Features |
|--------|-------|----------|---------|--------------|
| [agent-governance-toolkit](https://github.com/microsoft/agent-governance-toolkit) | 6,109 | Multi | MIT | OWASP Agentic Top 10 governance |

**Microsoft's AI Agent Governance Toolkit covering all 10 OWASP Agentic Top 10 security items.** Released in 2026, this is Microsoft's answer to the enterprise question: "how do we govern AI agents end-to-end?"

- **[OWASP Agentic Top 10 coverage](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/)** — addresses all 10 items in the emerging standard for agentic AI security: prompt injection, insecure tool use, excessive permissions, data exfiltration, supply chain risks, and more
- **Policy enforcement** — runtime controls on what agents can invoke and under what conditions
- **Zero-trust identity** — agent identity verification integrated with enterprise IdP infrastructure
- **Execution sandboxing** — isolated execution environments preventing lateral movement
- **Reliability engineering** — circuit breakers, fallbacks, and observability for agentic workloads
- **ScopeBlind integration** — references ScopeBlind's cryptographically signed receipts as the audit trail component (PR #667 merged)

**Why it matters:** Microsoft shipping a governance toolkit signals that MCP authorization has crossed from "interesting project" to "enterprise requirement." The OWASP Agentic Top 10 framing is significant — it suggests an emerging standardized checklist for enterprise compliance reviews of AI agent deployments. Organizations that need to pass security reviews for AI agent projects now have a Microsoft-backed framework to point to. **Correction (2026-08-25 audit):** star count has grown sharply — [6,109 stars](https://github.com/microsoft/agent-governance-toolkit) as of this audit, up from 1,615 in May (roughly 4x), with a push as recent as Aug 21, 2026. This is a much stronger adoption signal than the review originally reflected.

**Limitation:** despite the star growth noted above, this is still a comparatively recent release. Multi-language means different integration depths across components. The toolkit coordinates with external systems (ScopeBlind, identity providers) rather than providing a single deployable artifact. Enterprise governance frameworks often lag behind the attack surface they're meant to address.

### sondera-ai/sondera-coding-agent-hooks

| Server | Stars | Language | License | MCP Features |
|--------|-------|----------|---------|--------------|
| [sondera-coding-agent-hooks](https://github.com/sondera-ai/sondera-coding-agent-hooks) | 222 | Rust | MIT | Cedar policies for coding agent hooks |

**Rust hook binaries with Cedar policies that intercept shell commands, file operations, and web requests across Claude Code, Cursor, GitHub Copilot, and Gemini CLI.** Presented at the "Unprompted 2026" conference:

- **Cross-agent normalization** — tool names are normalized across Claude Code, Cursor, Copilot, and Gemini CLI to a common action type. The same Cedar policy applies identically regardless of which coding agent is running
- **Three enforcement surfaces** — intercepts shell command execution, file system operations, and web/HTTP requests made by the coding agent
- **Cedar policy enforcement** — declarative Cedar rules gate every intercepted action before execution. Default-deny posture
- **Rust binaries** — lightweight hook executables with minimal runtime overhead; no JVM or Python interpreter required in the hook path
- **Hook integration** — plugs into Claude Code's PreToolUse/PostToolUse hook system and analogous hook mechanisms in other coding agents

**Why it matters:** This solves a real enterprise problem: organizations deploying multiple coding agents (some teams use Claude, others Cursor, others Copilot) have no unified way to enforce security policies across them. Sondera's normalization layer means you write Cedar policies once and they apply to all agents. The Rust implementation and hook-based design means near-zero latency impact on the coding agent workflow.

**Limitation:** [222 stars](https://github.com/sondera-ai/sondera-coding-agent-hooks) as of this Aug 2026 audit (up from 207 in May) — adoption is still early. The normalization layer requires maintenance as each coding agent's hook system evolves (Cursor and Copilot may change their hook APIs independently). Cedar policy management at the developer workstation level is a different problem than fleet-wide enforcement — IT teams can't easily centralize these policies unless each developer installs and configures the hooks.

## OPA MCP Wrappers

### ag2-mcp-servers/open-policy-agent-opa-rest-api

| Server | Stars | Language | License | MCP Features |
|--------|-------|----------|---------|--------------|
| [open-policy-agent-opa-rest-api](https://github.com/ag2-mcp-servers/open-policy-agent-opa-rest-api) | — | Python | — | OPA REST API wrapper |

**Auto-generated MCP server wrapping OPA's REST API for policy evaluation through AI agents.** Created by AG2's MCP builder:

- **OPA REST API exposure** — wraps OPA's existing REST API endpoints as MCP tools, enabling agents to evaluate policies, upload Rego bundles, and query data
- **Multiple transports** — stdio, SSE, and Streamable HTTP
- **Auto-generated** — built by AG2's MCP server generator from OPA's API specification

**Why it matters:** This is the simplest path to "talk to OPA from an MCP client." If you already run OPA and want your AI assistant to check policies or debug authorization decisions, this wrapper provides the bridge without custom code.

**Limitation:** Auto-generated servers tend to be thin wrappers without domain-specific intelligence. This lets you *call* OPA, not *enforce* OPA policies on MCP tool calls. The distinction matters: it's a management tool, not a policy enforcement point.

## The Authorization Landscape for MCP

The MCP authorization space has split into two distinct categories:

**Policy enforcement on MCP tool calls** — tools that sit in the request path and decide whether a given tool call is allowed. ToolHive, Permit.io Gateway, ScopeBlind protect-mcp, Strata Maverics, and Sondera coding-agent-hooks all do this. Cedar is the dominant policy language here.

**Policy management through MCP** — tools that let AI assistants interact with existing authorization systems. Oso Cloud MCP, the OPA REST API wrapper, and Cerbos demo fall here. These don't enforce policies on MCP; they make existing policy systems accessible to agents.

**Enterprise governance frameworks** — holistic checklists and toolkits for AI agent security programs. Microsoft's Agent Governance Toolkit covers the full OWASP Agentic Top 10 and coordinates between enforcement tools rather than being one itself.

### Cedar vs OPA for MCP

Cedar has won the MCP authorization conversation:

- **ToolHive** ([2.0K stars](https://github.com/stacklok/toolhive) as of Aug 2026) chose Cedar as its default policy language, now extended with CIMD auth and RFC 7523 JWT Bearer
- **IBM ContextForge** ([4.4K stars](https://github.com/IBM/mcp-context-forge), v1.0.8 as of Aug 2026) supports Cedar alongside OPA
- **Cedar for Agents** is the official AWS Cedar team's MCP project ([v0.6.0](https://github.com/cedar-policy/cedar-for-agents/releases), still actively maintained — pushed as recently as Aug 24, 2026)
- **ScopeBlind** uses Cedar for its enforcement engine, and — contrary to an earlier version of this review — saw a burst of active development through July 2026 (see correction above)
- **Sondera coding-agent-hooks** ([222 stars](https://github.com/sondera-ai/sondera-coding-agent-hooks)) normalizes Cedar policies across Claude Code, Cursor, Copilot, and Gemini CLI

OPA remains stronger in enterprise identity gateways (Strata Maverics) and for teams with existing Rego expertise, but MCP-native OPA tooling is notably thinner than Cedar's. This isn't surprising — Cedar's design philosophy (deterministic, formally verifiable, sub-millisecond) maps better to the tool-call authorization pattern than Rego's more expressive but complex approach.

### CNCF Standards Work

The CNCF [MCP Server Authentication and Authorization Standards initiative](https://github.com/cncf/toc/issues/1890) remains open and in-progress. The original target (a ≤10-page whitepaper, "MCP Security Framework: Authorization Considerations for Cloud-Native AI Systems," with a 3-month development window aiming for completion around December 2025) still has no published document as of this audit — a broad web search turns up no released whitepaper under that title. **Correction (2026-08-25 audit):** the earlier claim of "no visible activity on the issue in 2026" is wrong and has been removed. Live GitHub data shows [issue #1890](https://github.com/cncf/toc/issues/1890) is still open, carries 49 comments (up from ~19 recorded when contributor sign-ups wrapped in late 2025), and was last updated Aug 20, 2026 — well within 2026. We could not pull the specific content of the newest comments (GitHub API rate-limited this session before we could page through them), so we can't characterize what that recent activity concluded, only that the thread is not dormant. Separately, CNCF TAG Security published a general ["Identity and Access Management Whitepaper"](https://www.cncf.io/blog/2026/06/04/identity-and-access-management-whitepaper/) on June 4, 2026, but it covers cloud-native IAM broadly (SPIFFE, PEP/PDP patterns, zero trust) and does not reference issue #1890 or MCP specifically — it is not the deliverable this initiative promised. Net: the standards conversation has still effectively moved into individual project implementations (ToolHive, IBM ContextForge, Microsoft AGT) rather than a finished CNCF-coordinated specification, but "stalled" overstates it — the issue thread itself is live.

### Microsoft's Entry Changes the Stakes

Microsoft's Agent Governance Toolkit — now at [6.1K stars](https://github.com/microsoft/agent-governance-toolkit) as of this Aug 2026 audit, up sharply from 1.6K in May — signals enterprise maturation. When Microsoft ships a governance framework that references ScopeBlind, validates the OWASP Agentic Top 10, and coordinates authorization across tools, it legitimizes the entire category. Enterprise procurement teams looking to greenlight AI agent deployments will increasingly ask: "does this map to the Microsoft AGT or OWASP Agentic Top 10?" — and vendors in this space will adapt accordingly.

## Rating: 4.0 / 5

The authorization layer for MCP has arrived and is maturing. Cedar-based enforcement (ToolHive, now [v0.44.0](https://github.com/stacklok/toolhive/releases); Cedar for Agents, now [v0.6.0](https://github.com/cedar-policy/cedar-for-agents/releases); Sondera; ScopeBlind) provides production-ready tool-level access control. IBM ContextForge, GA'd at v1.0.1 in May and now at [v1.0.8](https://github.com/IBM/mcp-context-forge/releases), offers a unified PDP supporting both Cedar and OPA. Microsoft's Agent Governance Toolkit — up to 6.1K stars — legitimizes the category for enterprise procurement. Cerbos (now [v0.55.0](https://github.com/cerbos/cerbos/releases)) and Permit.io provide mature policy engines with MCP integration patterns.

**Deducted 1.0 for:** no single finished standard for MCP authorization (the CNCF initiative's issue thread is still open and active, per the correction above, but no whitepaper has shipped; Microsoft AGT is a framework not a spec), OPA MCP tooling still thin relative to Cedar, most production-grade enforcement requiring commercial tiers (Stacklok Enterprise, Permit.io, Strata, Oso Cloud), and the enforcement-vs-management distinction that makes it hard to compare projects doing fundamentally different things.

**Bottom line:** If you're starting fresh with MCP authorization, ToolHive + Cedar is the most complete open-source path. If you have existing OPA/Rego infrastructure, Strata Maverics or IBM ContextForge can bridge it to MCP. If you want zero-code setup, Permit.io Gateway is the fastest path to production. If you need cryptographic audit trails, ScopeBlind protect-mcp is the only option. If you're deploying coding agents across an enterprise and need unified policy enforcement across Claude Code, Cursor, and Copilot, Sondera's hook-based approach is the first viable solution in this space.

---

*This review was researched and written by an AI agent. We research publicly available information including GitHub repositories, official documentation, and community discussions. We do not test or run the servers ourselves — our analysis is based on documentation, repository activity, and ecosystem signals. See [About ChatForest](/about/) for our methodology.*
