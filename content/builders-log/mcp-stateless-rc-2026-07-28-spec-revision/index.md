---
title: "MCP Goes Stateless: The 2026-07-28 Release Candidate Changes How You Deploy"
date: 2026-05-25
description: "The MCP spec release candidate locked May 21 removes protocol-level sessions entirely. A remote MCP server that once required sticky routing and shared session stores can now run behind a plain load balancer. That is not a minor cleanup — it changes the deployment math for every builder running MCP at scale."
content_type: "Builder's Log"
categories: ["MCP", "Agent Infrastructure", "Open Standards", "Industry Analysis"]
tags: ["mcp", "model-context-protocol", "stateless", "spec", "release-candidate", "protocol", "deployment", "oauth", "tasks-extension", "mcp-apps", "aaif", "linux-foundation", "agent-infrastructure"]
---

On May 21, 2026, the Model Context Protocol team locked the release candidate for the next spec version — designated 2026-07-28 for the date it goes final. It is the largest revision to the protocol since MCP launched in November 2024. The headline change is one sentence: MCP is now stateless at the protocol layer.

That sentence has real deployment consequences.

## What "Stateless" Actually Means Here

The previous MCP spec included a session layer. When a client connected to a remote MCP server, the handshake established a session ID (`Mcp-Session-Id`) that subsequent requests referenced. The server maintained session state — context about the connection, tool call history, authorization state — and both parties expected the same server instance to handle the full lifecycle of a session.

This was a headache for anyone running MCP servers on modern infrastructure. Standard cloud deployment — ECS tasks, Cloud Run instances, Kubernetes pods, Lambda functions, any auto-scaled fleet — assumes your compute is fungible. A load balancer routes each request to whatever instance has capacity. Sticky sessions break that assumption: you need session affinity at the routing layer, a shared external store so any instance can reconstruct session state, or both.

The 2026-07-28 RC removes the `Mcp-Session-Id` header entirely. Protocol-level sessions are gone. A remote MCP server is now just a request-response endpoint. You can put it behind a standard round-robin load balancer. You can run it serverless. You can scale horizontally without any special routing configuration. The gateway no longer needs to read protocol-level headers to route correctly.

For builders who have been running MCP servers at any meaningful scale, this is the change they asked for. The sticky session requirement was the first thing that bit anyone who moved a prototype into production.

## The Five Other Changes Worth Knowing

The stateless core is the structural change. The RC also adds five other meaningful pieces:

**Formal Extensions Framework.** The spec now has a defined mechanism for optional capability negotiation. Extensions are declared in the capability exchange during the initialization handshake. A server that supports an extension announces it; a client that needs it can verify it is present before sending extension-specific requests. Builders who have been shipping custom protocol additions in ad hoc ways now have a sanctioned path to make those additions interoperable.

**Tasks Extension.** The first extension under the new framework is a formal `Tasks` primitive. This handles long-running work — operations that take seconds, minutes, or longer, where the client needs to track status, receive progress updates, and handle cancellation. Previously, builders handled this with workarounds: returning a task ID via a regular tool call and then polling with a separate lookup tool. The Tasks extension formalizes that pattern with defined lifecycle states, structured progress events, and built-in cancellation support.

**MCP Apps.** Servers can now deliver server-rendered UI fragments to clients. The `resources` capability was always a way to expose data; MCP Apps extends that to interactive UI surfaces that render inside the MCP client. The immediate use case is configuration panels, dashboard widgets, and form flows that currently require the user to leave their agent environment and open a separate interface. Whether client developers ship support for this quickly will determine how useful it is in practice, but the primitive is in the spec.

**Tool List Caching.** The `tools/list` response now carries two new fields: `ttlMs` (how long the list is valid) and `cacheScope` (whether the cache is per-session or shareable). Clients that call `tools/list` before every request — the safe but expensive default — can now respect server guidance about when the list has gone stale. For high-traffic deployments where tool list fetches add measurable latency or token cost, this matters.

**OAuth/OIDC Alignment.** The authorization model is now formally aligned with RFC 9728 (OAuth Metadata Discovery) and the evolving OAuth for Agents working group drafts. Authorization flows that previously had to be bolted on outside the spec — especially delegated authorization in multi-agent chains — now have a defined path through standard OAuth infrastructure. Builders who have been implementing custom auth layers to handle agent-to-agent trust can migrate to the standardized approach.

## The Governance Connection

The [AAIF announcement last week](/builders-log/mcp-joins-linux-foundation-aaif-protocol-governance/) established the governance structure: neutral Linux Foundation entity, Spec Enhancement Proposals, working groups open to contributors from any organization. The 2026-07-28 RC is the first major spec revision under that structure.

The ten-week RC window — locked May 21, final July 28 — is explicitly designed for SDK maintainers to validate against the new spec before it becomes the reference. That is new behavior. Previous spec updates shipped and then the SDK ecosystem caught up. This version ships the RC to the ecosystem first and sets a ten-week window for breakage to surface.

That is what governance matures look like in practice. The protocol team is not just writing a spec in isolation and declaring it done. They are sequencing the release to give the community time to find the edge cases before the final version lands. The builders who are running production MCP deployments and find that the stateless changes break an assumption in their implementation can file against the RC rather than the final spec.

The SEP process the AAIF established is also where the five extension areas above originated. The Tasks extension, the Extensions framework, the caching primitives — these were not Anthropic's internal roadmap decisions. They came through the working group process with contributors from multiple organizations who each had real deployment needs the old spec did not serve.

## The Platform Race Angle

The [platform race series](/builders-log/) has been tracking how different enterprise players are building on MCP as infrastructure: [Atlassian's Teamwork Graph](/builders-log/atlassian-teamwork-graph-context-layer/) for context, [Microsoft's Agent 365](/builders-log/microsoft-agent-365-enterprise-governance-layer/) for governance, [Notion's developer platform](/builders-log/notion-developer-platform-workspace-hub/) for workspace coordination.

Every one of those integrations lives above the transport layer. The RC changes do not break any of them — but they make the underlying infrastructure significantly easier to run at enterprise scale. An enterprise MCP deployment that was previously constrained by session affinity requirements can now run on standard fleet infrastructure. That lowers the operational cost of the integrations every platform racer is shipping, which accelerates the pace at which enterprises can adopt them.

The stateless change also matters for agent-to-agent workflows, which are the current frontier of the platform race. [Multi-agent architectures](/builders-log/how-agents-talk-to-each-other/) depend on lightweight, fungible connections between agent nodes. A stateful protocol layer adds coordination overhead to every agent hop. A stateless one does not. The RC alignment with OAuth for Agents is specifically aimed at the authorization problem in delegated multi-agent chains — the question of how Agent A proves to Agent B that it is authorized to act on behalf of a user, without requiring a human in the loop on every step.

## What Builders Should Do Between Now and July 28

**If you run remote MCP servers:** The RC is available now. The stateless change is breaking if your server is relying on protocol-level session state rather than application-level session management. Audit your session handling before July 28. If you are storing per-connection state in the server process itself, plan for how that moves to an external store or becomes stateless.

**If you are building MCP clients:** The `tools/list` caching fields will be in client-facing responses from servers that opt into them. Decide now whether you will respect `ttlMs` by default or require an explicit configuration flag. Servers that advertise a 5-minute TTL for a stable tool list are telling you something real; ignoring it means paying fetch costs you do not have to pay.

**If you are implementing auth:** Read the OAuth/OIDC alignment section of the RC carefully. The delegated authorization work for multi-agent chains is the most complex part of the update. If you are building an agent framework that chains calls across multiple MCP servers, the RC is describing the authorization model you should be building toward.

**If you are evaluating MCP adoption:** The RC removes the deployment headache that most commonly caused enterprises to pause. Horizontal scaling without session affinity is a standard infrastructure requirement, not a luxury. Its absence in the old spec was a genuine adoption barrier. The final spec ships July 28. If deployment complexity was your reason for waiting, the RC clears it.

## The Remaining Gaps

The RC does not solve everything.

Server quality remains a distribution problem, not a protocol problem. 10,000 MCP servers are published; the quality range from production-grade to abandoned prototype is wide. Neutral governance of the spec does not mean quality control of the ecosystem.

The Tasks extension and MCP Apps are new primitives. Client support will lag server support, as it always does when the spec adds capability ahead of the ecosystem. The MCP Apps rendering model in particular depends on client developers choosing to implement it. Builders should not ship product decisions against primitives that do not yet have broad client support.

The ten-week RC window is an improvement over shipping and fixing. It is not a guarantee that every edge case surfaces before July 28. If you are running unusual transport configurations or edge cases in the auth flow, test against the RC actively rather than assuming the community will catch your scenario.

## One Line

The 2026-07-28 RC removes the deployment complexity that has been the main friction point for running MCP at scale. The protocol layer is not just settled — it is now simpler. Everything above it is still the race.
