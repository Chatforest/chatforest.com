---
title: "Perplexity Computer Enterprise — A Multi-Model Agent That Runs Inside Your Slack, Snowflake, and Salesforce"
date: 2026-05-24
sources_audited: 2026-07-28
description: "Perplexity launched Computer for Enterprise at Ask 2026 in March 2026, turning its search engine roots into a multi-model orchestration platform with 400+ app connectors and a Model Council that routes subtasks to Claude, Gemini, GPT-5, and others automatically. Here's what it actually does, what it costs, and what the serious caveats are."
tags: ["perplexity", "agents", "enterprise", "agentic", "multi-model", "snowflake", "salesforce", "hubspot", "mcp", "computer-use"]
rating: 4
author: "ChatForest"
---

**At a glance:** Perplexity launched Computer for Enterprise on March 11, 2026, at its inaugural Ask 2026 developer conference. The product extends Computer — its autonomous multi-step AI agent — from individual Max subscribers to enterprise teams, with Slack integration, 400+ app connectors (Snowflake, Salesforce, HubSpot, Datadog, GitHub, SharePoint, Microsoft Teams, and more), a 1Password credential-security partnership, and SOC 2 Type II compliance. It runs on a "Model Council" architecture that automatically routes subtasks to Claude, Gemini, GPT-5, Grok, and others. Enterprise pricing is $325/seat/month. Part of our **[agentic AI coverage](/tags/agentic/)**.

---

Perplexity started as an AI-powered search engine. That still describes the product most people use. But since February 2026, the company has been building something with considerably larger ambitions: a general-purpose autonomous agent that can operate across a business's entire application stack, run background tasks while users are away, and — according to Perplexity's own internal testing — compress years of human work into weeks.

The enterprise version of that product, [announced at Ask 2026](https://venturebeat.com/ai/perplexity-takes-its-computer-ai-agent-into-the-enterprise-taking-aim-at) in San Francisco on March 11, 2026, is now available for teams willing to pay $325 per seat per month and trust an AI agent with access to their CRM, data warehouse, code repositories, and messaging channels simultaneously.

Whether that's a reasonable trade depends heavily on your risk tolerance and how closely you read the fine print.

---

## What Perplexity Computer Actually Is

Computer is an autonomous AI agent, not a chatbot. The distinction matters architecturally.

A chatbot responds to queries. Computer accepts a high-level goal — "prepare a competitive analysis for Q3 using our Snowflake data and the latest industry reports," or "draft a follow-up sequence for the 47 leads that went cold in HubSpot last month" — and then plans, executes, and delivers finished work without step-by-step human supervision.

It does this through three mechanisms:

**Browser automation.** Computer can read screens, click, type, and navigate multi-step web workflows — including forms with no APIs, legacy internal dashboards, and other tools that have never been designed for machine interaction. This is roughly equivalent to what Anthropic calls Computer Use, but accessed via Perplexity's cloud infrastructure rather than a self-hosted API.

**Enterprise connectors.** Rather than relying solely on browser automation, Computer connects directly to enterprise systems via native integrations. Named connectors include Snowflake, Salesforce, HubSpot, Datadog, SharePoint, Microsoft Teams, Slack, MySQL, GitHub, Gmail, Notion, and Google Calendar. Perplexity [says Computer connects to "Salesforce, Microsoft Teams, HubSpot, MySQL, GitHub, and over 400 other tools"](https://www.perplexity.ai/help-center/en/articles/13901210-computer-for-enterprise). MCP (Model Context Protocol) support lets teams build custom connectors for internal systems not on that list.

**Persistent background operation.** Tasks continue running while the user is away. The agent maintains context across sessions, so it doesn't need to be re-briefed each time. In an enterprise context, this means a task kicked off Monday morning can be waiting with a completed deliverable by Monday afternoon with no further user interaction.

---

## The Model Council Architecture

The most architecturally distinct thing about Computer is that it is not a single-model product.

Perplexity calls its orchestration layer the "Model Council." When Computer receives a goal, it decomposes the task into subtasks and routes each subtask to the model best suited for it. In practice, this means Claude Opus 4.6 runs as the core reasoning/orchestration engine, Gemini handles deep research queries, GPT-5.2 handles long-context retrieval, and Grok handles speed-sensitive lightweight tasks, with video generation routed to Veo 3.1 — a breakdown [confirmed by Perplexity's own launch coverage](https://venturebeat.com/ai/perplexity-takes-its-computer-ai-agent-into-the-enterprise-taking-aim-at) and [corroborated in independent reporting on the product](https://www.sentisight.ai/how-much-perplexity-computer-cost/).

[Perplexity says](https://www.perplexity.ai/help-center/en/articles/13901210-computer-for-enterprise) Computer "routes work across 20 models, using the right model for each task"; the exact roster has shifted since launch, so the published count varies slightly by source.

The practical claim is that multi-model routing produces better outcomes than locking into a single provider — a claim that is plausible but difficult to verify independently. Perplexity's retrieval infrastructure, built from its search engine origins, is the piece competitors have to bolt on; for Perplexity, web-grounded data retrieval is native.

---

## The "3.25 Years of Work in 4 Weeks" Number

This figure has circulated widely and deserves a careful reading before you cite it in a board presentation.

Perplexity [says it ran more than 16,000 queries](https://www.perplexity.ai/hub/blog/computer-for-enterprise) through Computer in internal testing, measuring performance against institutional knowledge benchmarks it says are used by McKinsey, Harvard, MIT, and Boston Consulting Group. Based on those measurements, the company estimates the system completed what would have required approximately 3.25 years of equivalent human work in four weeks, [saving roughly $1.6 million in labor costs](https://www.pymnts.com/news/artificial-intelligence/2026/perplexity-computer-enterprise-completed-3-years-work-4-weeks/).

This is Perplexity's own internal measurement, constructed using their own query set against third-party benchmark frameworks. It has not been independently verified or replicated by a third party. It is reasonable to treat it as a plausible directional signal about task throughput — and unreasonable to treat it as a precise operational forecast for your organization. Your actual results will depend heavily on what tasks you're running, what your current workflows look like, and how much time your teams spend on the specific categories of work Computer automates well.

That said, the claim is not invented from nothing. Comparable agentic systems have shown meaningful throughput advantages in structured, repetitive, or research-heavy work. The honest position is: the number is compelling, but get your own numbers from a pilot.

---

## Ask 2026: What Perplexity Announced

The March 11 developer conference [packaged several announcements](https://www.perplexity.ai/hub/blog/everything-is-computer) around the Computer for Enterprise launch:

- **Computer for Enterprise** — the main event, with Slack integration, enterprise connectors, SOC 2 Type II, SAML SSO, SCIM provisioning, configurable data retention, expanded file storage, and audit logs
- **Personal Computer for Mac** — a persistent local client running on a Mac mini, giving the cloud agent persistent local file and application access
- **New APIs** — Search, Agent, Embeddings, and (announced as forthcoming) Sandbox endpoints for developers building on the platform
- **Finance data expansion** — [40+ live financial tools](https://www.perplexity.ai/hub/blog/everything-is-computer) pulling from SEC filings, FactSet, Coinbase, Quartr, and other sources, accessible to Computer

We could not independently confirm a Microsoft Teams @-mention feature analogous to the Slack integration; Perplexity's own launch materials describe the chat-based invocation as Slack-specific, with Microsoft Teams appearing instead as one of the 400+ app connectors.

---

## Pricing

- **Max (Personal)**: $200/month. Includes 10,000 monthly Computer credits (plus a one-time 20,000-credit bonus), unlimited Pro searches, access to frontier models, Sora 2 Pro video generation, the Comet browser, and unlimited Labs usage. Computer requires Max — it is not available on Perplexity's $20/month Pro tier or the free plan.
- **Enterprise Max**: [$325/seat/month or $3,250/year](https://www.perplexity.ai/help-center/en/articles/12310544-what-is-enterprise-max). Adds org-level security controls, audit logs, SCIM provisioning, configurable data retention, expanded file storage, and SSO. Enterprise support included.

The pricing sits at the premium end of the AI subscription market, comparable to OpenAI's ChatGPT Pro ($200/month) and roughly in the range of established enterprise software seats. The enterprise tier's $325/seat figure positions it as a productivity tool rather than a commodity subscription — the implied bet is that the ROI from task automation justifies the seat cost.

---

## The Credential Problem and the 1Password Solution

One of the structural problems with enterprise AI agents is credentials: to act on behalf of a user in Salesforce, Slack, or GitHub, the agent needs access to credentials. Putting credentials into a model or agent context creates obvious security and audit risks.

[Perplexity's partnership with 1Password](https://1password.com/blog/1password-and-perplexity-expand-partnership) addresses this directly. In the integrated setup, credentials are "never exposed to models or prompts" — 1Password's Unified Access layer grants the agent access dynamically as workflows execute, so Computer can act on a user's behalf in authorized systems without the credentials themselves touching the agent or the model. Every action remains authorized, governed, and auditable. For enterprise security teams, this is a material difference — a CISO can now see a full audit trail of what the agent did without needing to trust that credentials were handled correctly at every step.

---

## How It Compares to Competitors

The competitive field in enterprise AI agents has several serious players:

**OpenAI ChatGPT Agent** (Plus, Pro, Team, and Enterprise plans; standalone "Operator" was [folded into ChatGPT Agent and shut down on August 31, 2025](https://en.wikipedia.org/wiki/OpenAI_Operator)): Browser-based agent built on OpenAI's GPT-5-series reasoning models. Architecturally simpler — single model family rather than a model council. Strong integration with the broader OpenAI ecosystem. Less native search retrieval than Perplexity's search-engine-derived infrastructure.

**Anthropic Computer Use**: [A developer API rather than a packaged enterprise product](https://www.anthropic.com/news/3-5-models-and-computer-use) — you enable the beta tool and run Claude inside your own VM or container. Maximum flexibility, but requires significant engineering to deploy. Requires the deploying organization to handle its own security, audit logging, and connector infrastructure. No out-of-box enterprise connectors.

**Google Project Mariner**: [Google reported an 83.5% success rate on the WebVoyager benchmark](https://x.com/GoogleDeepMind/status/1866911079194038368) for browser task completion in its own testing. Currently runs as a Chrome extension requiring an active browser session — not suited for background operation or enterprise-scale deployment without significant infrastructure investment.

The honest comparison table: Computer is the most packaged enterprise-ready option of the four, with the broadest connector library and the strongest out-of-box compliance posture. That packaging comes with a higher price and a deeper dependency on Perplexity's trust posture — which, based on recent events, deserves scrutiny.

---

## Serious Caveats

**Privacy lawsuit.** A [class-action suit filed March 31, 2026](https://www.privado.ai/post/perplexity-ai-faces-cipa-class-action-lawsuit) alleged Perplexity embedded tracking software (Meta Pixel, Google Ads, and Google DoubleClick) that shared full conversation transcripts with Meta and Google, allegedly operating even when users activated "Incognito" mode. The suit was [voluntarily dismissed without prejudice on May 1, 2026](https://ppc.land/perplexity-data-lawsuit-dropped-but-the-privacy-questions-remain/), but a dismissal without prejudice is a procedural exit, not a resolution on the merits — no answer was filed and no hearing took place. Separately, in an April 2025 podcast appearance, [Perplexity CEO Aravind Srinivas said](https://techcrunch.com/2025/04/24/perplexity-ceo-says-its-browser-will-track-everything-users-do-online-to-sell-hyper-personalized-ads/) of the then-upcoming Comet browser: "we want to get data even outside the app to better understand you" — a statement, predating the enterprise launch by roughly a year, that enterprise security and legal teams should read carefully before expanding data access.

**Security researcher findings.** A 2025 mobile-security audit by [Appknox](https://winbuzzer.com/2025/04/21/security-audit-says-perplexitys-android-app-is-unsafe-cites-critical-flaws-xcxwbn/) — [also reported by Forbes](https://www.forbes.com/sites/rashishrivastava/2025/04/18/perplexitys-android-app-is-infested-with-security-flaws-report-finds/) — found hardcoded secrets, including API keys, embedded directly in Perplexity's Android app code. Separately, the Comet browser has repeatedly been flagged as vulnerable to prompt injection attacks: researchers at Trail of Bits and Guardio, and later Zenity Labs, [demonstrated multiple working exploits](https://thehackernews.com/2026/03/researchers-trick-perplexitys-comet-ai.html) that could hijack the browser's AI assistant to exfiltrate private data — a structural concern for any agent that reads arbitrary web content as part of task execution.

**The trust gap.** [According to analysis at TechHQ](https://techhq.com/news/perplexity-enterprise-ai-computer-trust-ciso/), trust — not capability — is the harder sell for enterprise AI agents with broad system access; the technology is credible, but CISOs remain wary of routing sensitive data through a young startup. An agent that can read your Snowflake data, write to your Salesforce CRM, and send messages in your Slack channels requires a significant extension of organizational trust. Perplexity's SOC 2 Type II certification and 1Password integration address parts of this, but the platform is less than six months old in its current form.

**Mac-only local client.** The Personal Computer for Mac client requires a Mac mini for persistent local agent operation. Windows support has not been announced.

**Internal benchmark.** As noted above, the productivity claims are internal measurements. Treat them as indicative, not definitive.

---

## Company Context

Perplexity [raised $200 million at a $20 billion valuation, reported September 10, 2025](https://www.pymnts.com/news/artificial-intelligence/2025/perplexity-valuation-hits-20-billion-following-new-funding-round/). By March 2026, the company [says its annual recurring revenue surpassed $450 million, up about 50% in a single month](https://techstartups.com/2026/04/08/perplexity-revenue-surges-50-as-ai-startup-shifts-from-search-to-autonomous-ai-agents/) from roughly $300 million in February 2026. The ARR spike is attributed to Computer's launch and a shift to usage-based pricing.

The company [reports more than 100 million monthly active users](https://techstartups.com/2026/04/08/perplexity-revenue-surges-50-as-ai-startup-shifts-from-search-to-autonomous-ai-agents/) and [signed a $750 million, three-year Azure cloud deal with Microsoft, announced January 29, 2026](https://winbuzzer.com/2026/02/01/perplexity-750m-microsoft-azure-deal-aws-lawsuit-xcxwbn/) — while keeping AWS as its primary cloud provider. [More than 100 enterprise organizations reportedly requested Computer access in a single weekend](https://enterprisedna.co/resources/news/perplexity-computer-enterprise-ai-agent-microsoft-salesforce-2026/) after the consumer launch.

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

---

**Sources:** [Perplexity — Computer for Enterprise launch post](https://www.perplexity.ai/hub/blog/computer-for-enterprise) · [Perplexity — March 2026 product changelog](https://www.perplexity.ai/changelog/what-we-shipped---march-13-2026) · [VentureBeat — Perplexity Computer for Enterprise launch](https://venturebeat.com/ai/perplexity-takes-its-computer-ai-agent-into-the-enterprise-taking-aim-at) · [TechCrunch — Perplexity Computer background](https://techcrunch.com/2026/02/27/perplexitys-new-computer-is-another-bet-that-users-need-many-ai-models/) · [PYMNTS — "3.25 years of work in 4 weeks" claim](https://www.pymnts.com/news/artificial-intelligence/2026/perplexity-computer-enterprise-completed-3-years-work-4-weeks/) · [1Password — Perplexity partnership](https://1password.com/blog/1password-and-perplexity-expand-partnership) · [TechHQ — trust vs. capability analysis](https://techhq.com/news/perplexity-enterprise-ai-computer-trust-ciso/) · [Privado.ai — CIPA class action background](https://www.privado.ai/post/perplexity-ai-faces-cipa-class-action-lawsuit) · [PPC.land — lawsuit voluntarily dismissed May 1, 2026](https://ppc.land/perplexity-data-lawsuit-dropped-but-the-privacy-questions-remain/) · [Techstartups — $450M ARR](https://techstartups.com/2026/04/08/perplexity-revenue-surges-50-as-ai-startup-shifts-from-search-to-autonomous-ai-agents/) · [WinBuzzer — $750M Microsoft Azure deal](https://winbuzzer.com/2026/02/01/perplexity-750m-microsoft-azure-deal-aws-lawsuit-xcxwbn/)
