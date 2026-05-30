---
title: "Snowflake Buys the Enterprise MCP Gateway: What Builders Need to Know Before Summit 26"
date: 2026-05-30
description: "Snowflake acquired Natoma, an enterprise MCP gateway that enforces identity, policy, and audit at the tool-call level. Builders who want enterprise deals will be selling into this governance layer whether they plan to or not."
og_description: "Snowflake just acquired Natoma — the enterprise MCP gateway that sits between AI agents and every tool they touch. Builders who ignore this layer will lose enterprise deals to builders who don't. Here's what the acquisition means for the MCP ecosystem before Summit 26 opens June 1."
content_type: "Builder's Log"
categories: ["AI Industry", "Developer Tools", "Enterprise AI"]
tags: ["snowflake", "natoma", "mcp", "enterprise", "governance", "ai-agents", "mcp-gateway", "security", "product-launch"]
---

On May 27, 2026, Snowflake signed a definitive agreement to acquire Natoma — a company most developers have never heard of, solving a problem every enterprise buyer cares about.

Natoma is an MCP gateway. It sits between your AI agents and every tool they touch, intercepting each tool call to validate identity, enforce policy, and write an audit log before letting the call through. Snowflake is buying the governance layer for agentic AI.

This matters to you even if you have never touched a Snowflake product.

---

## The Problem Natoma Solves

MCP has grown faster than enterprise security teams expected. Every MCP client can now call any MCP server that's been deployed — whether IT knows about it or not. The result: shadow AI tool access, fragmented governance across dozens of point connections, and no centralized record of which agent touched which system on whose behalf.

The classic enterprise worry about AI agents isn't hallucination. It's audit failure. "Our agent exfiltrated customer data through a misconfigured MCP server" is a CISO nightmare, not an engineering problem. Natoma exists to close that gap.

The Natoma gateway intercepts every tool invocation and validates three things before it goes through:

**Identity.** Who is behind this agent call? Natoma maps the AI action to a specific human user — their role, department, and security profile — then applies RBAC or ABAC rules. Agents act with exactly the permissions of the person behind them, not with ambient system access.

**Policy.** Is this action allowed under current policy? Natoma evaluates the tool, the arguments, the requesting identity, and the context against configured governance rules. The call goes through, is modified, or is blocked — with a policy-matched reason attached to the log.

**Audit.** What happened? Every tool call produces a structured log: user identity, AI client, tool name, inputs, outputs, outcome. Logs forward to SIEM platforms (Splunk, Sentinel, CrowdStrike Falcon) through standard export. When a regulator asks "what did your AI agent access last Tuesday," you have an answer.

---

## Why Snowflake Is the Right Buyer

Snowflake's pitch to enterprise has always been: your data lives here, governed, with access controls you already trust. Adding Natoma extends that pitch to MCP.

The architectural logic: Snowflake Intelligence (the user-facing agent layer) and Cortex Code (the builder-facing development layer) both make MCP tool calls to execute work. Natoma ensures that every one of those calls is governed by the same identity and policy framework that Snowflake customers already apply to their data warehouse access.

The result is a single governance plane across data access and agent tool access. That is a real enterprise pitch. Before Natoma, those were two separate systems with two separate audit logs and two separate security reviews. After the acquisition closes, Snowflake can sell "your agents and your data, under one governed roof."

The timing is also deliberate. Snowflake Summit 26 runs June 1–4 in San Francisco — opening tomorrow. Acquiring Natoma a week before the conference signals this isn't a roadmap item. It's a platform bet they're ready to show customers.

---

## What This Means for the MCP Ecosystem

Natoma's product existed before the acquisition as a standalone enterprise offering. It deploys as a gateway layer in front of MCP servers — any MCP servers, not just Snowflake-native ones. That matters for the ecosystem: Snowflake isn't just governing its own tools. It's positioning itself to govern tool access across the enterprise, regardless of which MCP servers are running.

That creates a new kind of certification question. Today, MCP servers need to pass a technical compatibility bar (do they implement the spec correctly?). Tomorrow, enterprise buyers will also ask: does this MCP server work correctly when deployed behind a Natoma/Snowflake gateway? Does it surface the metadata that governance policies need? Does it emit structured responses the audit layer can parse?

Builders who design for this now will have a shorter enterprise sales cycle than builders who design for it after a procurement team asks.

**Three things to check in your MCP server design:**

1. **Tool descriptions are machine-readable.** Natoma's policy engine needs to classify tools to apply the right governance rules. Vague tool descriptions ("does stuff with files") make governance harder and may trigger conservative default-deny policies. Specific, structured descriptions ("reads file at path, returns content as text, no write access") give the gateway what it needs to apply accurate policy.

2. **Outputs are structured.** Audit logs need to record what the tool returned, not just what was called. If your MCP server returns unstructured blobs, the audit entry is incomplete. Return structured JSON with typed fields. Gateway logs become meaningful; compliance teams can actually use them.

3. **Error responses include context.** When a tool call fails, the reason matters for governance. "Connection refused" tells the audit log nothing useful. "Rate limit exceeded: 1,000 calls per minute for this credential" tells the policy engine the agent was behaving normally and hit an external constraint. Error context shapes downstream governance decisions.

---

## The Bigger Pattern: Two Governance Layers

The Natoma acquisition lands one week after the Agent Control Standard (ACS) announcement — runtime governance at the agent decision layer. Now Snowflake is adding governance at the tool-call layer.

These are different controls solving different problems. ACS governs what agents *decide* to do. Natoma governs whether those decisions *execute* successfully against enterprise tools.

Together they sketch a defense-in-depth architecture that enterprise security teams will recognize from other domains:

- Application-layer policy (what can the agent decide to do?)
- Network-layer gateway (what tool calls actually reach production systems?)

Builders who understand both layers can explain them to enterprise buyers in terms those buyers already use. Builders who don't will find themselves repeatedly stopped at procurement.

---

## Timeline

- **May 27, 2026** — Snowflake signs definitive agreement to acquire Natoma. Financial terms undisclosed.
- **June 1–4, 2026** — Snowflake Summit 26, San Francisco. June 1 keynote features Daniela Amodei (Anthropic) and CEO Sridhar Ramaswamy. June 3 Builder Keynote expected to show Natoma integration in depth.
- **Closing date** — Not disclosed. Subject to standard regulatory review.

---

## The One-Sentence Builder Takeaway

Enterprise MCP tool access is becoming a Snowflake procurement category, and the builders whose servers work cleanly inside that governance layer will be the ones who get into enterprise accounts.

Watch the Snowflake Summit 26 Builder Keynote on June 3 for the first technical view of how Natoma integrates with Cortex Agents and Snowflake Intelligence.
