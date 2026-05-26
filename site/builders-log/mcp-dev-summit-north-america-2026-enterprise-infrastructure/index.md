# MCP Dev Summit NYC: When a Protocol Becomes Infrastructure

> 1,200 builders showed up in New York to talk about MCP — and barely anyone was asking 'what is it?' anymore. Uber, Nordstrom, Bloomberg, and PwC were talking scale, security, and the organizational overhead of running it. That's what a protocol looks like when it stops being a bet and starts being load-bearing.


Conferences tell you where the center of gravity is. Not because the talks are always technically deep — because the *attendees* are.

At the MCP Dev Summit North America 2026, held April 2-3 at the New York Marriott Marquis, roughly 1,200 people showed up. That's double the attendance from the previous summit. The Agentic AI Foundation, which organized it through the Linux Foundation, now has 170 member organizations — a growth rate that outpaces CNCF at the same stage of its life.

More telling than the headcount: the people at the podium. Uber. Nordstrom. Bloomberg. Duolingo. PwC.

These are not companies experimenting with AI tools. These are companies running MCP in production and explaining what broke and how they fixed it. That is a different conversation than "here's what MCP is." That is a conversation about infrastructure.

## The Question Nobody Was Asking

Eighteen months ago, most MCP discussions started with definition. What is the Model Context Protocol? Why does it exist? Why should you care?

In New York, nobody wasted time on that. The questions were operational:

- How do you run MCP at 10,000-service scale?
- What's your strategy for supply chain attacks against MCP servers?
- How do you do access control when agents are composing tools dynamically?
- What does observability look like when the call graph is generated at runtime?

That shift in question type is the real news from the summit. The protocol graduated. Now the work is making it production-grade.

## What the Technical Sessions Actually Covered

### The Dispatcher Pattern

The architectural headline from the summit was a dispatcher pattern that finally decouples MCP semantics from wire format and transport. Previously, the tight coupling between protocol logic and transport meant that changing one meant touching the other. The new dispatcher model puts a clean separation between:

1. MCP protocol semantics (tools, resources, prompts, sampling)
2. Wire format (how messages are serialized)
3. Transport (how messages move between processes)

This makes pluggable transports practical for the first time. You can now slot in gRPC, WebSockets, or a custom serverless adapter without reimplementing the protocol layer. For the enterprise teams in the room running internal MCP infrastructure, this matters a lot — they have existing transport infrastructure they need MCP to fit into, not the other way around.

### MCP Gateways as First-Class Architecture

A recurring pattern across enterprise case studies was the **MCP gateway** — a reverse proxy layer that sits between agents and the tool ecosystem. The gateway handles:

- Authentication and authorization (who can call what)
- Rate limiting and quota enforcement
- Logging and observability
- Routing between internal and external MCP servers
- Policy enforcement (data classification, PII handling)

Uber's deployment, for instance, doesn't let agents call MCP servers directly. Everything flows through a gateway layer that enforces their access model. Nordstrom described a similar pattern where the gateway is also the boundary between production MCP servers and staging environments.

This is familiar infrastructure to anyone who has worked with API management. The insight from the summit is that MCP is now complex enough — and high-stakes enough — that the same patterns apply.

### Observability at Runtime-Generated Call Depth

Traditional observability assumes relatively static call graphs. An agent composing tools dynamically generates call graphs at runtime, which breaks most existing tracing setups. The summit included sessions on what useful MCP observability actually looks like:

- Tracing that captures the full tool composition chain, not just individual tool calls
- Metrics that distinguish "agent chose the wrong tool" from "tool responded incorrectly"
- Alerting on behavioral drift — when an agent's tool usage patterns change unexpectedly

This is still early. Most of the case studies were honest about the fact that teams are building custom observability tooling. But the problem space is now well-defined enough that solutions are starting to look similar across organizations.

## The Security Roadmap: Concrete Milestones

The 2026 roadmap announced at the summit addressed the security and scale gaps most frequently cited by enterprise critics. Key milestones from the roadmap:

**OAuth 2.0 GA — September 2026**: The current OAuth implementation in MCP is in preview. The September target gives teams a stable auth foundation to build on. This matters for any deployment where MCP servers need to act on behalf of authenticated users.

**RBAC and Audit Logging — Q4 2026 preview**: Role-based access control and audit logging are the baseline requirements for any enterprise security team signing off on production AI infrastructure. These coming to preview in Q4 means there's a path to GA in early 2027.

**Cross-App Access (XAA) — June 2026 spec**: XAA addresses the multi-agent scenario where one agent needs to call an MCP server that belongs to a different application or tenant. This is the enterprise auth challenge that gets complicated fast: how do you manage identity and trust when the call chain spans organizational boundaries?

**Stateless Transport by Default**: Already covered in the June spec RC (see our [earlier analysis](/builders-log/mcp-stateless-rc-2026-07-28-spec-revision/)), but the summit confirmed the enterprise motivation clearly — stateless transport is what makes MCP deployable on serverless runtimes like AWS Lambda and Cloudflare Workers without session affinity hacks.

## AAIF: The Governance Signal

The Agentic AI Foundation announced at the summit that its Technical Steering Committee approved a formal project lifecycle policy. This is the move that opens the foundation to external projects — a project can now apply to join AAIF without having been a founding contribution.

For context: CNCF's project lifecycle model (sandbox → incubating → graduated) became one of the most influential pieces of cloud infrastructure governance ever created. Projects that passed through CNCF's process got a credibility signal that procurement teams recognized. AAIF is explicitly building toward that model.

The three-stage lifecycle (Growth, Impact, Emeritus) gives the ecosystem a neutral home for MCP-adjacent tooling — gateways, observability tools, security scanners — to seek a stability signal that isn't vendor-branded.

## What This Means for Builders

If you're building on MCP today, the summit signals are mostly good:

**The protocol is stabilizing.** Two major foundational changes — stateless transport and the dispatcher pattern — are being shipped in a coordinated way under AAIF governance. After those land, the core will be stable enough to build on without worrying about foundational churn.

**Enterprise patterns are converging.** The gateway-centric architecture that Uber, Nordstrom, and Bloomberg described independently is now a documented pattern. You don't need to reinvent it. If you're building MCP infrastructure for an enterprise customer, start with the gateway.

**Auth is the unsolved problem for 2026.** OAuth 2.0 GA in September, XAA in the June spec, RBAC in Q4 preview — these are the things that are holding enterprise deployments back. If your product helps with MCP auth, you're working on the right problem.

**The ecosystem is consolidating around neutral infrastructure.** AAIF growing faster than CNCF at the same stage means the tooling will converge on foundation-hosted projects over time. If you're building MCP tooling, tracking what's in the foundation's pipeline is now worth your time.

The question of whether MCP would become real enterprise infrastructure got answered at a hotel in New York in early April. 1,200 people flew in from Uber and Nordstrom and PwC to talk about what they'd built and what they needed next.

That's your answer.

---

*MCP Dev Summit North America 2026 was held April 2-3 at the New York Marriott Marquis, organized by the Agentic AI Foundation under the Linux Foundation. Sources: [AAIF recap](https://aaif.io/blog/mcp-is-now-enterprise-infrastructure-everything-that-happened-at-mcp-dev-summit-north-america-2026/), [InfoQ technical coverage](https://www.infoq.com/news/2026/04/aaif-mcp-summit/), [The New Stack enterprise roadmap](https://thenewstack.io/mcp-maintainers-enterprise-roadmap/), [Futurum Group analysis](https://futurumgroup.com/insights/mcp-dev-summit-2026-aaif-sets-a-clear-direction-with-disciplined-guardrails/).*

