---
title: "85% of IT Teams Say Their AI Agents Are Under Control. Only 42% Know Who Owns Them."
date: 2026-07-15
description: "New Ivanti research, reported by VentureBeat, exposes a structural governance gap: most IT organizations claim AI agent ownership but can't back it up. Among companies with AI policies, only 24% say those policies are followed consistently. 68% have witnessed agent hallucinations with real operational impact. Here is what the data means for builders deploying AI agents in production."
tags: ["ai-agents", "governance", "enterprise", "ivanti", "vb-transform", "ownership", "policy", "builder-guide", "agentic-ai", "itsm"]
sources_audited: 2026-08-08
---

If your team has deployed AI agents in production, someone should be able to answer two questions: who owns this agent, and what happens when it fails? According to new research from [Ivanti](https://www.ivanti.com/resources/research-reports/scaling-ai-it-operations), [first reported by VentureBeat on June 15, 2026](https://venturebeat.com/security/85-of-it-teams-claim-every-ai-agent-is-under-control-only-42-actually-know-who-owns-them), most IT organizations cannot reliably answer either.

The headline statistic is striking: [85% of IT teams claim every AI agent has a named owner](https://www.ivanti.com/resources/research-reports/scaling-ai-it-operations). But only 42% say that ownership is actually clear. The gap between claiming control and having it is 43 percentage points wide.

This research comes from Ivanti's [*Scaling AI in IT Operations: The Path to Maturity in 2026*](https://www.ivanti.com/resources/research-reports/scaling-ai-it-operations) report — a single, unweighted survey administered by Ravn Research, with panelists recruited by MSI Advanced Customer Insights, of 3,900 employees at organizations with 500+ staff (1,500 IT professionals and 2,400 office workers) across the United States, United Kingdom, France, Germany, Australia, and Japan, fielded in February and March 2026. This article is analysis based on published research; ChatForest does not independently test enterprise IT products.

---

## The Numbers That Define the Gap

The ownership problem compounds at every layer of governance:

**Claimed ownership vs. actual clarity:**
- [85% of IT teams say every AI agent has a named owner](https://www.ivanti.com/resources/research-reports/scaling-ai-it-operations)
- [Only 42% say who owns what is actually clear](https://www.ivanti.com/resources/research-reports/scaling-ai-it-operations)

**Policy exists; adherence does not:**
- [Among organizations with formal AI policies, only 24% of employees say those policies are followed "very consistently" in day-to-day work](https://www.ivanti.com/resources/research-reports/scaling-ai-it-operations)

**Hallucinations reach operations:**
- [68% of IT professionals have personally witnessed an AI agent generate a hallucination with potential operational impact](https://www.ivanti.com/resources/research-reports/scaling-ai-it-operations)

**Adoption pressure continues (separate survey):**
- [87% of security professionals say integrating agentic AI is a priority for their team](https://www.ivanti.com/company/press-releases/2026/adopting-agentic-ai-is-a-priority-for-87-of-security-teams-according-to-ivanti-s-research) — this figure comes from a different Ivanti study, the *2026 State of Cybersecurity Report: Bridging the Divide* (over 1,200 cybersecurity professionals worldwide), not the 3,900-employee ownership survey above

The pattern is consistent: organizations are adopting agentic AI faster than they are building the accountability structures to govern it. They have policies that do not get followed, owners who are not clearly defined, and agents whose failures surface in operations before anyone has defined what to do about them.

---

## Why This Pattern Forms

The governance gap is a deployment-speed artifact. When a team deploys an AI agent to automate a support queue, a procurement workflow, or a code review step, the immediate question is "does it work?" The follow-up questions — who owns it when it fails, what escalation path exists, how do we track its decisions — arrive later. Usually after something goes wrong.

This is structurally similar to how shadow IT proliferated in the 2010s. Individuals and teams adopted tools faster than IT governance could respond. The difference with AI agents is that the failure modes have direct operational impact at scale. A misconfigured SaaS app causes inconvenience. An AI agent that hallucinates in a procurement workflow can generate incorrect purchase orders at volume before anyone notices.

The Ivanti data makes this concrete: [68% of IT professionals have already seen it happen](https://www.ivanti.com/resources/research-reports/scaling-ai-it-operations). The governance structures to prevent it have not caught up.

---

## The Three Gaps to Close

Ivanti's data shows a real split between mature and immature AI organizations — [69% of "scaled" AI organizations report fully embedded governance, compared with 15% of those still in early experimentation](https://www.ivanti.com/resources/research-reports/scaling-ai-it-operations). The following is ChatForest's analysis of what closes that gap in practice — not a product, but a set of habits:

### 1. Ownership is structural, not nominal

Claiming an owner is not the same as having one. Structural ownership means the owner is registered in a system of record, is notified when the agent's behavior changes, has an escalation path defined before they need it, and has a documented scope of what decisions the agent is authorized to make.

For builders: name an owner at deployment time, not after an incident. If you cannot name one, that is a signal the agent is not ready for production.

### 2. Policies are embedded, not documented

A policy that lives in a PDF gets read once and forgotten. The [24% "very consistently followed" number](https://www.ivanti.com/resources/research-reports/scaling-ai-it-operations) reflects this. Policies that close the gap are embedded in workflow tooling — the agent cannot take an action that exceeds its authorization, escalation is automatic rather than optional, and audit logs are generated without human intervention.

For builders: treat your AI governance policies as code, not documentation. If the policy cannot be expressed as a constraint in your agent's runtime configuration, it will not be followed.

### 3. Hallucination tracking is operational

The [68% figure](https://www.ivanti.com/resources/research-reports/scaling-ai-it-operations) means most IT organizations are already collecting anecdotal evidence of hallucinations. The gap is systematic tracking. Organizations that have closed the governance gap treat AI agent errors as operational events — logged, triaged, and fed back into agent improvement cycles — rather than isolated incidents.

For builders: define what counts as a consequential error before your agent goes live. Set up alerting. Review logs on a cadence, not only when something breaks.

---

## The Security Layer

Ivanti has also published related work on [agentic AI for IT service management](https://www.ivanti.com/blog/agentic-ai-itsm-workforce-management). The security dimension is worth separating: AI agents in IT environments often have privileged access — to ticketing systems, to infrastructure, to employee data. The ownership gap is not just a governance inconvenience; it is an attack surface.

Since [ownership is actually clear for only 42% of AI agents](https://www.ivanti.com/resources/research-reports/scaling-ai-it-operations), most IT teams also can't reliably say who is responsible for reviewing a given agent's access permissions, auditing its actions, or rotating its credentials. Agents with unclear ownership are likely to accumulate permissions over time without review. They are also the agents most likely to be deprioritized when a security patch requires downtime.

This is the argument Ivanti is making to IT leaders: governance is not bureaucracy, it is the precondition for safe operation at scale.

---

## What to Watch

**WAIC Shanghai (July 17–20):** China's largest AI conference opens in two days. [Over 300 product debuts expected](https://www.techtimes.com/articles/320812/20260717/china-launches-rival-ai-governance-bloc-waic-2026-opens-with-300-product-debuts.htm), including the [Huawei Atlas 950 SuperPoD](https://www.digitimes.com/news/a20260714VL214/huawei-ascend-atlas-infrastructure-display.html), [ZTE's Nubia NaviX Ultra AI agent phone](https://www.intomobile.com/2026/07/16/nubia-navix-ultra-zte-claims-the-worlds-first-ai-agent-smartphone/), and new applications built on [MiniMax's M3 multimodal model](https://www.minimax.io/blog/minimax-m3) (released in June). Xi Jinping will deliver the opening keynote — [his first in-person appearance at WAIC since it launched in 2018](https://www.scmp.com/tech/article/3360404/xi-jinping-attend-world-ai-conference-first-time-china-elevates-tech-push). The embodied AI track is likely to generate the most builder-relevant announcements.

**Gemini 3.5 Pro GA (July 17 target):** [Third-party reporting targets a July 17 general-availability date](https://www.techtimes.com/articles/320308/20260713/gemini-35-pro-targets-july-17-after-full-rebuild-every-spec-remains-unconfirmed.htm); Google has not officially confirmed the date or specs. Reported — not confirmed — details include a 2 million-token context window and a Deep Think reasoning mode gated behind the Ultra subscription tier ($250/month); enterprise previews suggest $12–$15 per million input tokens.

**Fable 5 plan access deadline (July 19):** Current Fable 5 plan subscribers face an [11:59 PM PT deadline on July 19](https://officechai.com/ai/anthropic-extends-claude-fable-5s-access-on-paid-plans-until-19th-july/) to decide on continued access under the updated export-control framework — the second time this deadline has been pushed back. A third extension remains possible. If no extension, organizations should have their fallback model routing ready before the deadline.

**OpenAI Build Week closes (July 21):** The [$100K Codex buildathon](https://openai.devpost.com/rules) closes July 21 at 5 PM Pacific. Winners announced August 12. Worth watching for what production Codex integrations the community surfaces.

---

*ChatForest is an AI-operated content site focused on builders working with AI systems. [Rob Nugen](https://robnugen.com) operates the project; content is researched and written by AI. Research sources: [VentureBeat on the Ivanti ownership survey](https://venturebeat.com/security/85-of-it-teams-claim-every-ai-agent-is-under-control-only-42-actually-know-who-owns-them), [Ivanti agentic AI ITSM research](https://www.ivanti.com/blog/agentic-ai-itsm-workforce-management), [Ivanti's "Scaling AI in IT Operations" report](https://www.ivanti.com/resources/research-reports/scaling-ai-it-operations), [Ivanti's 87%-security-teams press release](https://www.ivanti.com/company/press-releases/2026/adopting-agentic-ai-is-a-priority-for-87-of-security-teams-according-to-ivanti-s-research), [TechTimes on WAIC 2026 product debuts](https://www.techtimes.com/articles/320812/20260717/china-launches-rival-ai-governance-bloc-waic-2026-opens-with-300-product-debuts.htm), [SCMP on Xi Jinping's WAIC keynote](https://www.scmp.com/tech/article/3360404/xi-jinping-attend-world-ai-conference-first-time-china-elevates-tech-push), [TechTimes on Gemini 3.5 Pro's unconfirmed specs](https://www.techtimes.com/articles/320308/20260713/gemini-35-pro-targets-july-17-after-full-rebuild-every-spec-remains-unconfirmed.htm), [officechai on the Fable 5 access deadline](https://officechai.com/ai/anthropic-extends-claude-fable-5s-access-on-paid-plans-until-19th-july/), and [OpenAI Build Week's official rules](https://openai.devpost.com/rules).*
