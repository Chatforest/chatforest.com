---
title: "Perplexity Computer Enterprise — A Multi-Model Agent That Runs Inside Your Slack, Snowflake, and Salesforce"
date: 2026-05-24
description: "Perplexity launched Computer for Enterprise at Ask 2026 in March 2026, turning its search engine roots into a multi-model orchestration platform with 400+ app connectors and a Model Council that routes subtasks to Claude, Gemini, GPT-5, and others automatically. Here's what it actually does, what it costs, and what the serious caveats are."
tags: ["perplexity", "agents", "enterprise", "agentic", "multi-model", "snowflake", "salesforce", "hubspot", "mcp", "computer-use"]
rating: 4
author: "ChatForest"
---

**At a glance:** Perplexity launched Computer for Enterprise on March 11, 2026, at its inaugural Ask 2026 developer conference. The product extends Computer — its autonomous multi-step AI agent — from individual Max subscribers to enterprise teams, with Slack and Teams integration, 400+ app connectors (Snowflake, Salesforce, HubSpot, Datadog, GitHub, SharePoint, and more), a 1Password credential-security partnership, and SOC 2 Type II compliance. It runs on a "Model Council" architecture that automatically routes subtasks to Claude, Gemini, GPT-5, Grok, and others. Enterprise pricing is $325/seat/month. Part of our **[agentic AI coverage](/tags/agentic/)**.

---

Perplexity started as an AI-powered search engine. That still describes the product most people use. But since February 2026, the company has been building something with considerably larger ambitions: a general-purpose autonomous agent that can operate across a business's entire application stack, run background tasks while users are away, and — according to Perplexity's own internal testing — compress years of human work into weeks.

The enterprise version of that product, announced at Ask 2026 in San Francisco on March 11, 2026, is now available for teams willing to pay $325 per seat per month and trust an AI agent with access to their CRM, data warehouse, code repositories, and messaging channels simultaneously.

Whether that's a reasonable trade depends heavily on your risk tolerance and how closely you read the fine print.

---

## What Perplexity Computer Actually Is

Computer is an autonomous AI agent, not a chatbot. The distinction matters architecturally.

A chatbot responds to queries. Computer accepts a high-level goal — "prepare a competitive analysis for Q3 using our Snowflake data and the latest industry reports," or "draft a follow-up sequence for the 47 leads that went cold in HubSpot last month" — and then plans, executes, and delivers finished work without step-by-step human supervision.

It does this through three mechanisms:

**Browser automation.** Computer can read screens, click, type, and navigate multi-step web workflows — including forms with no APIs, legacy internal dashboards, and other tools that have never been designed for machine interaction. This is roughly equivalent to what Anthropic calls Computer Use, but accessed via Perplexity's cloud infrastructure rather than a self-hosted API.

**Enterprise connectors.** Rather than relying solely on browser automation, Computer connects directly to enterprise systems via native integrations. Named connectors include Snowflake, Salesforce, HubSpot, Datadog, SharePoint, Microsoft Teams, Slack, MySQL, GitHub, Gmail, Notion, and Google Calendar. Perplexity claims 400+ total application integrations. MCP (Model Context Protocol) support lets teams build custom connectors for internal systems not on that list.

**Persistent background operation.** Tasks continue running while the user is away. The agent maintains context across sessions, so it doesn't need to be re-briefed each time. In an enterprise context, this means a task kicked off Monday morning can be waiting with a completed deliverable by Monday afternoon with no further user interaction.

---

## The Model Council Architecture

The most architecturally distinct thing about Computer is that it is not a single-model product.

Perplexity calls its orchestration layer the "Model Council." When Computer receives a goal, it decomposes the task into subtasks and routes each subtask to the model best suited for it. In practice, this means Claude Opus 4.6 handles complex reasoning and orchestration, Gemini handles deep research queries, GPT-5 handles long-context retrieval, and Grok handles speed-sensitive lightweight tasks. Video generation routes to Sora 2 Pro or Veo 3.1 depending on the task requirements.

The current model catalog sits at approximately 19–20 models depending on when you check; Perplexity has been updating the lineup since launch and the published count varies slightly by source.

The practical claim is that multi-model routing produces better outcomes than locking into a single provider — a claim that is plausible but difficult to verify independently. Perplexity's retrieval infrastructure, built from its search engine origins, is the piece competitors have to bolt on; for Perplexity, web-grounded data retrieval is native.

---

## The "3.25 Years of Work in 4 Weeks" Number

This figure has circulated widely and deserves a careful reading before you cite it in a board presentation.

Perplexity ran more than 16,000 queries through Computer in internal testing, measuring performance against institutional knowledge benchmarks used by McKinsey, Harvard, MIT, and Boston Consulting Group. Based on those measurements, the company estimates the system completed what would have required approximately 3.25 years of equivalent human work in four weeks, at an estimated labor cost savings of $1.6 million.

This is Perplexity's own internal measurement, constructed using their own query set against third-party benchmark frameworks. It has not been independently verified or replicated by a third party. It is reasonable to treat it as a plausible directional signal about task throughput — and unreasonable to treat it as a precise operational forecast for your organization. Your actual results will depend heavily on what tasks you're running, what your current workflows look like, and how much time your teams spend on the specific categories of work Computer automates well.

That said, the claim is not invented from nothing. Comparable agentic systems have shown meaningful throughput advantages in structured, repetitive, or research-heavy work. The honest position is: the number is compelling, but get your own numbers from a pilot.

---

## Ask 2026: What Perplexity Announced

The March 11 developer conference packaged several announcements around the Computer for Enterprise launch:

- **Computer for Enterprise** — the main event, with Slack/Teams integration, enterprise connectors, SOC 2 Type II, SAML SSO, SCIM provisioning, configurable data retention, expanded file storage, and audit logs
- **Personal Computer for Mac** — a persistent local client running on a Mac mini, giving the cloud agent persistent local file and application access
- **New APIs** — search, agent, and analytics endpoints for developers building on the platform
- **Finance data expansion** — 40+ live financial data sources accessible to Computer
- **Microsoft Teams integration** — @computer mention support directly in channels

---

## Pricing

- **Max (Personal)**: $200/month or $2,000/year. Includes 10,000 monthly credits, unlimited Pro searches, access to frontier models, Sora 2 Pro, Comet browser, and unlimited Labs usage. Computer requires Max — it is not available on Perplexity's $20/month Pro tier or the free plan.
- **Enterprise Max**: $325/seat/month or $3,250/year. Adds org-level security controls, audit logs, SCIM provisioning, configurable data retention, expanded file storage, and SSO. Enterprise support included.

The pricing sits at the premium end of the AI subscription market, comparable to OpenAI's ChatGPT Pro ($200/month) and roughly in the range of established enterprise software seats. The enterprise tier's $325/seat figure positions it as a productivity tool rather than a commodity subscription — the implied bet is that the ROI from task automation justifies the seat cost.

---

## The Credential Problem and the 1Password Solution

One of the structural problems with enterprise AI agents is credentials: to act on behalf of a user in Salesforce, Slack, or GitHub, the agent needs access to credentials. Putting credentials into a model or agent context creates obvious security and audit risks.

Perplexity's partnership with 1Password addresses this directly. In the integrated setup, Computer can act on a user's behalf in authorized systems without credentials ever touching the agent or the model. Actions remain authorized, governed, and auditable. For enterprise security teams, this is a material difference — a CISO can now see a full audit trail of what the agent did without needing to trust that credentials were handled correctly at every step.

---

## How It Compares to Competitors

The competitive field in enterprise AI agents has several serious players:

**OpenAI Operator** (via ChatGPT Pro, $200/month): Browser-based agent built around GPT-4o. Architecturally simpler — single model rather than a model council. Strong integration with the broader OpenAI ecosystem. Currently US-only for enterprise. Less native search retrieval.

**Anthropic Computer Use**: A developer API rather than a packaged enterprise product. Maximum flexibility, but requires significant engineering to deploy. Requires the deploying organization to handle its own security, audit logging, and connector infrastructure. No out-of-box enterprise connectors.

**Google Project Mariner**: Strong browser task benchmarks (WebVoyager: 83.5% success rate). Currently runs as a Chrome extension requiring an active browser session — not suited for background operation or enterprise-scale deployment without significant infrastructure investment.

The honest comparison table: Computer is the most packaged enterprise-ready option of the four, with the broadest connector library and the strongest out-of-box compliance posture. That packaging comes with a higher price and a deeper dependency on Perplexity's trust posture — which, based on recent events, deserves scrutiny.

---

## Serious Caveats

**Privacy lawsuit.** A class-action suit filed in April 2026 alleged Perplexity embedded tracking software that shared conversations with Meta and Google, operating even in incognito mode. The suit was voluntarily dismissed on May 1, 2026, but the core claims were not resolved on the merits. Separately, Perplexity's CEO has publicly stated the company's Comet browser is designed to collect user data "even outside the app" — a statement that enterprise security and legal teams should read carefully before expanding data access.

**Security researcher findings.** Researchers found hardcoded secrets in Perplexity's Android app. The Comet browser has been flagged as vulnerable to prompt injection attacks — a structural concern for any agent that reads arbitrary web content as part of task execution.

**The trust gap.** According to analysis at TechHQ, CISOs report that trust, not capability, is the harder sell for enterprise AI agents with broad system access. An agent that can read your Snowflake data, write to your Salesforce CRM, and send messages in your Slack channels requires a significant extension of organizational trust. Perplexity's SOC 2 Type II certification and 1Password integration address parts of this, but the platform is less than six months old in its current form.

**Mac-only local client.** The Personal Computer for Mac client requires a Mac mini for persistent local agent operation. Windows support has not been announced.

**Internal benchmark.** As noted above, the productivity claims are internal measurements. Treat them as indicative, not definitive.

---

## Company Context

Perplexity raised $200 million at a $20–21 billion valuation in September 2025. As of approximately March 2026, the company has surpassed $450 million in annual recurring revenue — up more than 50% from roughly $300 million in late 2025. The ARR spike is directly attributed to Computer's launch and a shift to usage-based pricing.

The company has more than 100 million users and signed a $750 million, three-year Azure cloud deal with Microsoft in approximately February 2026. Over 100 enterprise organizations requested Computer access in a single weekend after the consumer launch.

This is a company that is growing fast, is well-funded, and is making credible product progress. It is also a company whose privacy practices have drawn serious attention at a moment when it is asking enterprise customers to give its agents access to sensitive business systems. Those two facts sit together in real tension.

---

## Bottom Line

Perplexity Computer Enterprise is a genuinely capable autonomous agent platform with an architectural approach — multi-model orchestration with native search retrieval and a broad connector library — that is differentiated from the alternatives. For organizations that run significant volumes of structured research, data retrieval, or cross-system workflow tasks, the productivity case is real.

The cautions are also real: the platform is young, the productivity claims are self-reported, and the company's privacy posture has attracted scrutiny that matters when you are deciding who gets access to your CRM and data warehouse. Enterprise procurement should read the privacy disclosures carefully and treat a structured pilot as mandatory before broad deployment.

**Pricing**: Max $200/month; Enterprise Max $325/seat/month  
**Announced**: March 11, 2026 (Ask 2026 developer conference)  
**Status**: Available; enterprise pricing requires direct contact with Perplexity sales  
**Best suited for**: Knowledge-intensive teams running repetitive research, data retrieval, or cross-system workflows  
**Not suited for**: Organizations with unresolved data sensitivity or privacy governance requirements, or those requiring Windows local client support
