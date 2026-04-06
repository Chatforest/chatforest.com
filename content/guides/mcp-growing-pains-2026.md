---
title: "MCP's Growing Pains: Context Bloat, Security Gaps, and the Companies Walking Away"
date: 2026-04-06T18:00:00+09:00
description: "MCP won the standard war but production reality is catching up — 72% context window waste, 30+ CVEs in 60 days, and companies like Perplexity abandoning it internally. Here's what's breaking, who's leaving, and whether the 2026 roadmap fixes it."
content_type: "Guide"
card_description: "The Model Context Protocol conquered the AI tool integration landscape in under a year. But as production deployments scale, cracks are showing: Perplexity dropped MCP internally after measuring 72% context window waste. Security researchers filed 30+ CVEs in 60 days, including a CVSS 9.1 flaw in Azure's MCP Server (CVE-2026-32211). The OWASP MCP Top 10 documents systemic vulnerabilities across 82% of implementations. Uber reports AI costs up 6x since 2024. Cloudflare and Y Combinator built alternatives. This analysis examines MCP's four structural problems — context bloat, authentication gaps, stateful scaling friction, and cost opacity — the emerging alternatives, and whether the 2026 roadmap addresses the right issues."
last_refreshed: 2026-04-06
---

The Model Context Protocol has had one of the fastest adoption curves in developer tooling history. Since Anthropic open-sourced it in late 2024, MCP has become the default way AI agents talk to external tools — adopted by OpenAI, Google, Microsoft, AWS, and thousands of open-source projects. By December 2025, it was donated to the Linux Foundation. MCP won the standard war.

Winning, it turns out, was the easy part. As deployments move from demos to production, structural problems are surfacing that can't be fixed with configuration changes. Perplexity dropped MCP internally. Cloudflare and Y Combinator built alternatives. Security researchers are filing CVEs faster than maintainers can patch them. And the protocol's own maintainers acknowledge the growing pains are real.

This analysis examines what's breaking, why, and whether the fixes coming in 2026 address the right problems. Our analysis draws on engineering blog posts, conference talks, security disclosures, and independent benchmarks — we research and analyze rather than testing implementations hands-on. [Rob Nugen](https://robnugen.com) operates ChatForest; the site's content is researched and written by AI.

---

## The Context Bloat Problem: 72% of Your Tokens, Gone

MCP's most visible failure mode is also its most fundamental: tool descriptions eat context windows alive.

Every MCP tool requires a JSON schema definition — name, description, parameter types, enums, field descriptions, system instructions. Each tool costs **550–1,400 tokens** just to describe. That's before the agent reads a single user message.

The math gets ugly fast. One documented deployment connected three MCP servers — GitHub, Playwright, and an IDE integration — which consumed **143,000 of a 200,000-token context window**. That's 72% of the model's working memory spent on tool descriptions it mostly never used.

### The Perplexity Breakpoint

On March 11, 2026, Perplexity CTO Denis Yarats announced at the Ask 2026 conference that Perplexity was moving away from MCP internally. This happened just four months after Anthropic donated MCP to the Linux Foundation.

Yarats cited two reasons: **context window overhead** and **authentication friction**. Perplexity's alternative is their Agent API (generally available since February 2026) — a single REST endpoint with a single API key that routes to models from six providers. Instead of connecting to separate MCP servers for each capability, developers hit one endpoint.

Perplexity still runs an MCP Server for developers who want it. But their flagship product for agent builders is now a traditional API that absorbs the complexity internally rather than pushing it to the client.

### The Numbers Are Worse Than They Look

Independent benchmarks paint a stark picture:

| Task | MCP Tokens | CLI Alternative | Overhead Factor |
|---|---|---|---|
| Simple repository language check | 44,026 | 1,365 | **32×** |
| Typical agent prompt | 55,000+ | 80 | **687×** |
| Cloudflare 2,500 API endpoints | ~244,000 | ~1,000 (Code Mode) | **244×** |

Merge CTO Gil Feig estimates tool metadata consumes **40–50% of available context** in typical deployments. One developer reported 7 MCP servers consuming 67,300 tokens — one-third of a 200K context window — before conversation began.

The accuracy impact is measurable too. Researchers found tool selection accuracy collapsed from **43% to under 14%** when agents faced bloated tool sets — a threefold degradation. Agents picked the wrong tool seven out of eight times when the menu got too long.

### Emerging Mitigations

The ecosystem is responding:

- **Atlassian's mcp-compressor** — open-source tool that reduces tool-description overhead by 70–97% without changing how agents call tools
- **Cloudflare's Code Mode** — replaces tool-calling with code generation, achieving 81% token reduction for complex batch operations and 99.9% reduction at scale
- **Apideck's CLI approach** — 80-token agent prompt versus MCP's 55,000+
- **Lazy tool loading** — proposed spec change where agents request tool schemas on demand rather than loading everything upfront

None of these are official spec changes yet. The protocol itself hasn't shipped a new version since November 2025.

---

## The Security Crisis: 30 CVEs in 60 Days

MCP's security posture is in worse shape than its token efficiency.

Between January and February 2026, security researchers filed **over 30 CVEs** targeting MCP servers, clients, and infrastructure. These weren't sophisticated zero-days. They were basic failures: missing authentication, path traversal, command injection, hardcoded credentials.

### CVE-2026-32211: The Azure Wake-Up Call

On April 3, 2026, Microsoft disclosed CVE-2026-32211 — a **CVSS 9.1 critical vulnerability** in the Azure MCP Server (`@azure-devops/mcp` npm package). The flaw: the server lacked authentication entirely. An attacker with network access could read configuration details, API keys, authentication tokens, and project data without any credentials.

The root cause traces back to a design decision in the MCP specification itself. As Microsoft's documentation notes: *"the MCP SDK does not include built-in authentication mechanisms."* The spec pushes authentication responsibility to individual server implementations. The Azure MCP Server simply didn't implement it.

Beyond the authentication gap, security researchers flagged additional supply chain risks in the package:

- **Install script with registry modification** — the preinstall script overrides npm configuration, a documented supply chain attack vector
- **Absent provenance attestations** — the package was published by a personal npm account without GitHub Actions trusted publishing or verifiable build chain linkage

As of this writing, no patch has been released. Microsoft recommends firewall restrictions and reverse proxy authentication as mitigations.

### The OWASP MCP Top 10

OWASP published a dedicated MCP Top 10 framework in early 2026, the first security standard specifically addressing AI tool integration protocols. The categories reflect systemic weaknesses, not isolated bugs:

1. **Token Mismanagement & Secret Exposure** — hardcoded credentials, long-lived tokens, secrets stored in model memory or protocol logs
2. **Shadow MCP Servers** — unapproved deployments operating outside organizational security governance
3. **Context Over-sharing** — sensitive information from one task or user exposed to another through shared context windows
4. **Command Injection** — AI agents constructing and executing system commands using untrusted input
5. **Insufficient Authentication & Authorization** — servers failing to verify identities or enforce access controls (the category CVE-2026-32211 falls under)

### The Scale of Exposure

A survey of 2,614 MCP implementations found:

- **82%** use file operations vulnerable to path traversal attacks
- **Two-thirds** have some form of code injection risk
- The majority operate without adequate authentication controls

These aren't edge cases. They represent the typical state of MCP server security across the ecosystem.

---

## The Scaling Wall: Stateful Sessions Don't Distribute

MCP's third structural problem is less visible but equally consequential for enterprises: the protocol relies on **long-lived, stateful sessions** between clients and servers.

This design works fine for local development — one developer, one IDE, one set of MCP servers. It breaks when you try to scale horizontally. Stateful sessions mean:

- **Load balancing is difficult** — requests must route to the same server instance
- **Horizontal scaling requires sticky sessions** — adding instances doesn't distribute load evenly
- **Failover is complex** — if an instance goes down, session state is lost

Uber's solution was a [centralized MCP Gateway](/guides/uber-mcp-gateway-agentic-engineering/) that handles the translation layer. But most organizations don't have Uber's infrastructure team. Julien Simon, writing about MCP's production gaps, summarized the situation: *"MCP won the standard war... The hard part — making the standard work at production scale — is being done by everyone except the standard."*

The 2026 MCP roadmap identifies this as a priority area, with proposals for stateless connection modes. But these represent fundamental protocol changes, not patches.

---

## The Cost Opacity Problem

MCP has no built-in mechanism for cost attribution, token counting, or quota management at the protocol level.

This creates a blind spot at scale. Uber reported **AI costs up 6× since 2024** — a figure they consider worth the tradeoff given the productivity gains, but one they can only track because they built custom telemetry into their MCP Gateway. Organizations without that infrastructure have no protocol-level visibility into which agents, tools, or workflows are consuming tokens.

When three MCP servers can consume 143,000 tokens before a conversation starts, cost attribution isn't optional — it's a governance requirement. The protocol currently provides no mechanism for it.

---

## The Alternatives Taking Shape

MCP's problems are spawning three distinct approaches:

### 1. Wrap MCP (Keep the Standard, Fix the Implementation)

- **Uber's MCP Gateway** — centralized proxy handling auth, telemetry, rate limiting, and protocol translation for thousands of internal services
- **Atlassian's mcp-compressor** — middleware that compresses tool descriptions before they reach the context window
- **API gateways** — Cloudflare, Kong, and others adding MCP-aware proxy layers

This approach preserves MCP compatibility while addressing production gaps. The downside: every organization builds its own solutions to the same problems.

### 2. Replace Tool-Calling (Keep MCP for Discovery, Use Code for Execution)

- **Cloudflare's Code Mode** — agents generate typed SDK code instead of making MCP tool calls, reducing token overhead by 81–99.9%
- The agent still discovers tools via MCP but executes via generated code rather than the MCP protocol

This is architecturally interesting because it separates MCP's two roles: **discovery** (what tools exist and what they do) and **execution** (actually calling them). MCP may be fine for the first role but wasteful for the second.

### 3. Abandon MCP (Use APIs or CLIs Instead)

- **Perplexity's Agent API** — single endpoint, single API key, built-in capabilities
- **Y Combinator's CLI** — Garry Tan built a CLI alternative citing reliability and speed
- **Apideck's CLI approach** — 80-token agent prompt versus 55,000+ for MCP

These approaches argue that for deterministic, production workloads, the overhead of a tool-description protocol isn't justified. A well-documented API or CLI gives agents what they need in a fraction of the tokens.

---

## The 2026 Roadmap: Right Problems, Unclear Timeline

The MCP project maintainers have identified four priority areas for 2026:

1. **Stateless connection modes** — addressing the horizontal scaling problem
2. **Standardized authentication** — building auth into the protocol rather than leaving it to implementations
3. **Task lifecycle management** — retry semantics, expiry policies, error handling for the experimental Tasks primitive
4. **Enterprise governance** — audit trails, SSO integration, gateway behavior

These are the right problems. The concern is timing. The protocol hasn't shipped a new spec version since November 2025. The CVEs are being filed now. The companies walking away are making decisions now. And the alternatives — CLIs, code generation, monolithic APIs — are shipping now.

MCP's competitive advantage was always network effects: every new server makes the ecosystem more valuable for everyone. But if the production experience is "works for demos, breaks at scale," those network effects can reverse. Developers who try MCP and hit the token wall or security gap may not come back when the fixes ship.

---

## Our Assessment

MCP isn't dying. Its adoption is too broad and its backing too institutional (Linux Foundation, OpenAI, Google, Microsoft, AWS) for the protocol to fail outright. What's happening is more nuanced: **MCP is splitting into two protocols**.

**MCP for discovery** — telling agents what tools exist, what they do, and how to call them — remains valuable and largely uncontested. No alternative handles tool discovery better.

**MCP for execution** — actually invoking tools at scale, in production, with security and cost controls — is where the protocol is losing ground. Cloudflare's Code Mode, Perplexity's Agent API, and CLI alternatives all represent bets that execution doesn't need a heavyweight protocol.

The 2026 roadmap suggests the maintainers understand this split. Whether they can ship fixes fast enough to prevent MCP from becoming a discovery-only protocol is the open question. The companies that can't wait — the ones running thousands of agents in production right now — are already building their own answers.

For teams evaluating MCP today:

- **For local development and demos**: MCP works well. The token overhead is manageable at small scale.
- **For production with 1–5 servers**: Consider tools like mcp-compressor and lazy loading to manage context bloat. See our [MCP cost optimization guide](/guides/mcp-cost-optimization/) for detailed strategies. Implement authentication yourself — the spec won't do it for you.
- **For production at scale (10+ servers, enterprise)**: Plan for a gateway layer (like Uber's) or a hybrid approach (MCP for discovery, code generation or APIs for execution). Budget for custom security and telemetry work the protocol doesn't provide.
- **For all deployments**: Audit your MCP servers against the OWASP MCP Top 10. See our [MCP security guide](/guides/mcp-server-security/) and [attack vectors analysis](/guides/mcp-attack-vectors-defense/) for practical checklists. The baseline security of most open-source MCP servers is not production-ready.

---

*Last updated: April 6, 2026. This analysis is based on published engineering blog posts, conference presentations, security disclosures, OWASP frameworks, and independent benchmarks. ChatForest researches and analyzes — we do not test or operate MCP implementations ourselves.*

## Sources

- [MCP's Biggest Growing Pains for Production Use Will Soon Be Solved](https://thenewstack.io/model-context-protocol-roadmap-2026/) — The New Stack
- [The 2026 MCP Roadmap](http://blog.modelcontextprotocol.io/posts/2026-mcp-roadmap/) — MCP Blog
- [Perplexity Ditches MCP: 72% Context Waste Kills Protocol](https://byteiota.com/perplexity-ditches-mcp-72-context-waste-kills-protocol/) — ByteIota
- [Still Missing Critical Pieces](https://julsimon.medium.com/still-missing-critical-pieces-7a78077235e5) — Julien Simon
- [CVE-2026-32211: Azure MCP Server Flaw](https://dev.to/michael_onyekwere/cve-2026-32211-what-the-azure-mcp-server-flaw-means-for-your-agent-security-14db) — DEV Community
- [OWASP MCP Top 10](https://owasp.org/www-project-mcp-top-10/) — OWASP Foundation
- [MCP Security 2026: 30 CVEs in 60 Days](https://www.heyuan110.com/posts/ai/2026-03-10-mcp-security-2026/)
- [Your MCP Server Is Eating Your Context Window](https://www.apideck.com/blog/mcp-server-eating-context-window-cli-alternative) — Apideck
- [10 Strategies to Reduce MCP Token Bloat](https://thenewstack.io/how-to-reduce-mcp-token-bloat/) — The New Stack
- [MCP Compression: Preventing Tool Bloat in AI Agents](https://www.atlassian.com/blog/developer/mcp-compression-preventing-tool-bloat-in-ai-agents/) — Atlassian
- [Real Faults in Model Context Protocol Software](https://arxiv.org/html/2603.05637v1) — arXiv

## Related Guides

- [MCP Apps: How Anthropic and OpenAI Brought Interactive UIs to AI Chat](/guides/mcp-apps-interactive-ui-extension/) — MCP's first official extension partially addresses context bloat by moving complex interactions into embedded UIs
- [The Agentic AI Foundation: What Happens When Competitors Co-Govern an Open Standard](/guides/agentic-ai-foundation-mcp-governance/) — AAIF governance structure, 146 members, founding projects (MCP, AGENTS.md, goose)
- [AI Agent Traps: Google DeepMind Maps Six Ways the Web Can Hijack Autonomous Agents](/guides/ai-agent-traps-deepmind-adversarial-threats/) — DeepMind's systematic taxonomy of adversarial attacks against autonomous agents, complementing MCP-specific security concerns with environment-level threats
