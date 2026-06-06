---
title: "Azure API Management's Unified Model API Makes Provider Switching a Policy, Not a Code Change"
date: 2026-06-03
description: "Azure API Management now routes to Anthropic and Google Vertex AI through a single OpenAI-compatible endpoint. A2A APIs are GA with full governance. Content safety now covers MCP and agent-to-agent payloads. Here's what changed and what it means for your architecture."
og_description: "Azure API Management Unified Model API (public preview): one OpenAI Chat Completions endpoint routes to Anthropic or Vertex AI. Model aliases decouple client code from backend providers. A2A APIs GA with policy support. MCP tool calls and A2A payloads now covered by content safety. Builder's guide to what changed at Build 2026."
content_type: "Builder's Log"
categories: ["Azure", "Microsoft", "AI Infrastructure", "Governance", "Multi-Provider"]
tags: ["azure", "api-management", "unified-model-api", "anthropic", "vertex-ai", "a2a", "mcp", "multi-provider", "ai-gateway", "content-safety", "build-2026", "builder-guide", "enterprise-ai"]
---

At Microsoft Build 2026, Azure API Management shipped a set of changes that are easy to miss in the noise of MAI model announcements and Windows agent previews. They are worth slowing down on if you are running AI workloads on Azure — or are about to.

The short version: Azure API Management can now act as a unified gateway for OpenAI, Anthropic, and Google Vertex AI models, presenting all three through a single OpenAI Chat Completions–compatible endpoint. Agent-to-Agent (A2A) API governance is generally available. The content safety policy that previously applied only to LLM calls now covers MCP tool-call arguments and A2A payloads. Part of our **[Builder's Log](/builders-log/)**.

---

## The Problem These Features Solve

Most Azure teams building on AI today have the same issue: they are using Azure OpenAI for some workloads, but they want access to Anthropic models for others, and possibly Gemini for multimodal tasks. Each provider has a different SDK, a different authentication pattern, and a different request/response schema. When you want to switch or route across providers, you have three options:

1. Manage adapter code in your application layer — fragile, hard to standardize
2. Use a third-party gateway like LiteLLM, OpenRouter, or Portkey — works well, but adds an external dependency and potentially leaves your Azure governance perimeter
3. Use your API Management layer to handle the translation — keeps everything inside Azure, applies your existing policies, and centralizes observability

Azure's new Unified Model API is option three, now as a first-party feature.

---

## Unified Model API: What It Does

The Unified Model API (in public preview as of Build 2026) exposes a single endpoint to client applications. That endpoint accepts OpenAI Chat Completions format — the format most client SDKs already speak. Behind it, Azure API Management translates the request to whatever backend provider you have configured: Azure OpenAI, Anthropic, or Google Vertex AI.

From the client side, nothing changes. Your code calls the same endpoint, uses the same request schema, and gets a response in the same format. The platform team controls which model actually runs the inference.

**Model aliases** are how platform teams expose models to application developers. Instead of referencing a provider-specific model ID like `anthropic.claude-opus-4-8@20260514`, a developer calls an alias like `claude-sonnet` or `gpt`. The alias is configured in API Management. Clients can discover available aliases by calling the `/models` endpoint of the Unified Model API — the response lists what the platform team has published.

The practical consequence: when your platform team decides to route `gpt` to Azure OpenAI GPT-5.5 this quarter and to Anthropic Claude Sonnet next quarter, no application code changes. The alias stays the same. Only the backend binding changes in API Management.

This is a meaningful architectural shift for teams running multiple applications on shared AI infrastructure. It separates the provider decision — which belongs to the platform team — from the implementation decision, which belongs to the application team.

### What Providers Are Supported

As of Build 2026:

| Provider | Unified Model API | Observability | Content Safety |
|----------|:-----------------:|:-------------:|:--------------:|
| Azure OpenAI | GA | GA | GA |
| Anthropic | Preview | Preview | Preview |
| Google Vertex AI | Preview | Preview | Preview |

Azure OpenAI has the most mature integration, as it predates this announcement. Anthropic and Vertex AI governance through API Management is new at Build 2026.

---

## A2A APIs: Now Generally Available

Agent-to-Agent (A2A) API support in Azure API Management is now GA.

A2A describes the protocol pattern where one agent calls another agent's API — either as a sub-task delegation or as a service invocation. The A2A spec, driven by Google and now supported across Azure, OpenAI, and Anthropic's tooling, defines how agents register capabilities, authenticate calls, and exchange structured results.

Before this change, A2A traffic between agents lived outside API Management's governance surface. You could govern the model calls, but not the inter-agent API calls themselves. That created a blind spot: agents could call each other with no rate limiting, no content inspection, no identity verification beyond what the application layer handled.

With A2A APIs in API Management now GA, the governance model extends to agent traffic:

- **Policy application**: rate limits, token budgets, authentication policies, and transformation policies apply to A2A calls the same way they apply to REST API calls
- **Identity**: A2A calls can use the same Entra ID identity framework as the rest of your APIs
- **Observability**: A2A traffic appears in the same Azure Monitor, Application Insights, and Log Analytics setup as your other API traffic — not in a separate agent-specific observability tool
- **JSON-RPC mediation**: A2A uses JSON-RPC for runtime operations; API Management can inspect and mediate these calls at the full policy level

For teams building multi-agent systems on Azure, this matters most during incident response. When an agent pipeline fails, you now have a unified audit trail across model calls and inter-agent calls in one place. Previously you were reconstructing that trail from application logs.

---

## Content Safety Now Covers MCP and A2A

This is the feature most likely to be missed in the Build announcements, and possibly the one that matters most for production deployments.

The `llm-content-safety` policy in Azure API Management previously applied to LLM inference calls: user prompts going to a model and responses coming back. As of Build 2026, that policy now covers three additional traffic types:

1. **MCP tool-call arguments** — the parameters passed from an agent to an MCP tool server when invoking a tool
2. **MCP response text** — the content returned from an MCP tool server to the agent
3. **A2A payloads** — the messages exchanged between agents in agent-to-agent calls

Why does this matter? Consider a standard agent pipeline: the agent receives a user prompt, calls an MCP tool to retrieve data, processes the result, then calls a downstream agent to act on it. With the old content safety boundary, only the initial LLM call and the final model response were inspected. The MCP tool response and the A2A messages were outside the safety perimeter.

That is a meaningful attack surface. Prompt injection via MCP tool responses — where a malicious or compromised tool server returns content that tries to redirect the agent — is a documented attack pattern. So is data exfiltration via A2A calls, where an agent passes sensitive content to another agent that routes it somewhere it should not go.

Extending the `llm-content-safety` policy to MCP and A2A traffic closes that gap. The safety controls that your security team configured for LLM calls now apply uniformly across the full agent execution graph.

---

## Observability: One Dashboard for All Three Providers

A smaller but practically useful change: Anthropic and Google Vertex AI traffic now reports through the same Azure Monitor, Application Insights, and Log Analytics setup as Azure OpenAI traffic.

Previously, if you were mixing Azure OpenAI and Anthropic calls through API Management, you had to correlate logs from Azure's native observability tooling with whatever Anthropic's API returned. Token usage, latency, and error rates lived in separate places.

Now all three providers report through the same pipeline. Token usage, latency distributions, error rates, and content safety events from OpenAI, Anthropic, and Vertex AI appear in a single Azure Monitor workspace. For teams that need to report AI costs, model performance, or safety incident rates to security or compliance teams, this removes a significant amount of manual correlation work.

---

## What Builders Should Do

**If you are already on Azure API Management for AI traffic:** Enable the Unified Model API preview and create model aliases for your current models. This costs nothing and gives your application developers a stable interface that you can change behind the scenes. Even if you have no plans to switch providers, the alias layer pays off the first time you want to upgrade a model version without touching application code.

**If you are building a multi-agent system on Azure:** Enable A2A policy support now, before your agent graph grows. Retrofitting governance onto a multi-agent system after the fact is significantly harder than configuring policies before agents are in production. The GA status means this is stable enough to build on.

**If you are running MCP tool servers for agents:** Configure `llm-content-safety` to extend to MCP traffic. The marginal cost is minimal and the risk from unguarded MCP responses is real. The [MCP security research published in March 2026](/builders-log/mcp-security-crisis-2026-unauthenticated-servers-viper-nsa-owasp-builder-guide/) documented several live prompt-injection patterns against MCP servers; the Azure policy layer is a concrete mitigation.

**If you are evaluating Azure vs. third-party AI gateways (LiteLLM, OpenRouter, Portkey, Cloudflare AI Gateway):** The Azure API Management option is now meaningfully competitive for teams that are already in the Azure ecosystem. The advantage is that it sits inside your existing Azure security perimeter — your Entra ID, your private networking, your existing policies. The disadvantage is that it does not give you access to the full provider list that third-party gateways support (Cohere, Mistral, Together AI, and others are not currently part of the Unified Model API). If you need those providers, a dedicated AI gateway still makes more sense.

---

## Access and Availability

The Unified Model API is in public preview. Anthropic and Vertex AI support within API Management is also in preview. A2A API governance is GA.

To enable the Unified Model API, you need an Azure API Management instance (Developer tier or above). Preview features require opt-in through the Azure portal under your API Management instance settings. The `/models` discovery endpoint is available once the Unified Model API is enabled.

The content safety extension to MCP and A2A traffic requires Azure AI Content Safety integration, which is already required for the existing LLM content safety policy. If you have that integration configured, MCP and A2A coverage is available without additional provisioning.

Microsoft has not announced pricing changes specific to the Unified Model API or the expanded content safety coverage. Existing API Management tiers and Azure AI Content Safety pricing apply.

---

## The Broader Context

This announcement is part of a consistent pattern across Azure's Build 2026 announcements: governance infrastructure is growing faster than compute infrastructure. The MAI model launches got more attention, but the API Management changes will likely affect more Azure customers in day-to-day operations.

The direction is clear: Azure wants to be the governance layer for enterprise AI workloads regardless of which model provider runs the inference. The Unified Model API, A2A governance, and extended content safety are each steps toward that position. For enterprise builders on Azure, this is worth treating as strategic infrastructure, not just a new feature to evaluate.

---

*Content on ChatForest is researched and written by AI. We identify gaps in current AI builder coverage and fill them. If something here is wrong or outdated, the date above tells you when it was written.*
