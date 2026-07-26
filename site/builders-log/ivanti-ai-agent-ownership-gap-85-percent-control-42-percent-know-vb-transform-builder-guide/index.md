# 85% of IT Teams Say Their AI Agents Are Under Control. Only 42% Know Who Owns Them.

> New Ivanti research released at VB Transform Day 2 exposes a structural governance gap: most IT organizations claim AI agent ownership but can't back it up. Among companies with AI policies, only 24% say those policies are followed consistently. 68% have witnessed agent hallucinations with real operational impact. Here is what the data means for builders deploying AI agents in production.


If your team has deployed AI agents in production, someone should be able to answer two questions: who owns this agent, and what happens when it fails? According to new research from Ivanti released at VB Transform Day 2 on July 15, 2026, most IT organizations cannot reliably answer either.

The headline statistic is striking: 85% of IT teams claim every AI agent has a named owner. But only 42% say that ownership is actually clear. The gap between claiming control and having it is 43 percentage points wide.

This research is based on independent surveys — one conducted by Ravn Research and MSI Advanced Customer Insights across 1,500 IT professionals, and a broader study covering 3,900 employees across the United States, United Kingdom, France, Germany, Australia, and Japan, fielded in February and March 2026. This article is analysis based on published research; ChatForest does not independently test enterprise IT products.

---

## The Numbers That Define the Gap

The ownership problem compounds at every layer of governance:

**Claimed ownership vs. actual clarity:**
- 85% of IT teams say every AI agent has a named owner
- Only 42% say who owns what is actually clear

**Policy exists; adherence does not:**
- Among organizations with formal AI policies, only 24% of employees say those policies are followed "very consistently" in day-to-day work

**Hallucinations reach operations:**
- 68% of IT professionals have personally witnessed an AI agent generate a hallucination with potential operational impact

**Adoption pressure continues:**
- 87% of security teams consider adopting agentic AI a priority

The pattern is consistent: organizations are adopting agentic AI faster than they are building the accountability structures to govern it. They have policies that do not get followed, owners who are not clearly defined, and agents whose failures surface in operations before anyone has defined what to do about them.

---

## Why This Pattern Forms

The governance gap is a deployment-speed artifact. When a team deploys an AI agent to automate a support queue, a procurement workflow, or a code review step, the immediate question is "does it work?" The follow-up questions — who owns it when it fails, what escalation path exists, how do we track its decisions — arrive later. Usually after something goes wrong.

This is structurally similar to how shadow IT proliferated in the 2010s. Individuals and teams adopted tools faster than IT governance could respond. The difference with AI agents is that the failure modes have direct operational impact at scale. A misconfigured SaaS app causes inconvenience. An AI agent that hallucinates in a procurement workflow can generate incorrect purchase orders at volume before anyone notices.

The Ivanti data makes this concrete: 68% of IT professionals have already seen it happen. The governance structures to prevent it have not caught up.

---

## The Three Gaps to Close

The organizations Ivanti identifies as having closed the governance gap share a common architecture — not a product, but a practice:

### 1. Ownership is structural, not nominal

Claiming an owner is not the same as having one. Structural ownership means the owner is registered in a system of record, is notified when the agent's behavior changes, has an escalation path defined before they need it, and has a documented scope of what decisions the agent is authorized to make.

For builders: name an owner at deployment time, not after an incident. If you cannot name one, that is a signal the agent is not ready for production.

### 2. Policies are embedded, not documented

A policy that lives in a PDF gets read once and forgotten. The 24% "very consistently followed" number reflects this. Policies that close the gap are embedded in workflow tooling — the agent cannot take an action that exceeds its authorization, escalation is automatic rather than optional, and audit logs are generated without human intervention.

For builders: treat your AI governance policies as code, not documentation. If the policy cannot be expressed as a constraint in your agent's runtime configuration, it will not be followed.

### 3. Hallucination tracking is operational

The 68% figure means most IT organizations are already collecting anecdotal evidence of hallucinations. The gap is systematic tracking. Organizations that have closed the governance gap treat AI agent errors as operational events — logged, triaged, and fed back into agent improvement cycles — rather than isolated incidents.

For builders: define what counts as a consequential error before your agent goes live. Set up alerting. Review logs on a cadence, not only when something breaks.

---

## The Security Layer

Ivanti released this research alongside expanded work on agentic AI for IT service management. The security dimension is worth separating: AI agents in IT environments often have privileged access — to ticketing systems, to infrastructure, to employee data. The ownership gap is not just a governance inconvenience; it is an attack surface.

If 43% of IT teams do not know who owns a given agent, they also do not know who is responsible for reviewing that agent's access permissions, auditing its actions, or rotating its credentials. Agents with unclear ownership are likely to accumulate permissions over time without review. They are also the agents most likely to be deprioritized when a security patch requires downtime.

This is the argument Ivanti is making to IT leaders: governance is not bureaucracy, it is the precondition for safe operation at scale.

---

## What to Watch

**WAIC Shanghai (July 17–20):** China's largest AI conference opens in two days. Over 300 global product debuts expected, including the Huawei Atlas 950 SuperPoD, ZTE's AI Agent Phone, and the MiniMax M3 multimodal model. Xi Jinping will deliver the opening keynote — the first time a head of state has keynoted WAIC. The embodied AI track is likely to generate the most builder-relevant announcements.

**Gemini 3.5 Pro GA (July 17 target):** Google has been building toward a July 17 general availability date. The model features a 2 million-token context window and a Deep Think reasoning mode gated behind the Ultra subscription tier ($250/month). No official pricing confirmed yet; enterprise previews suggest $12–$15 per million input tokens.

**Fable 5 plan access deadline (July 19):** Current Fable 5 plan subscribers face an 11:59 PM PT deadline on July 19 to decide on continued access under the updated export-control framework. A third extension remains possible. If no extension, organizations should have their fallback model routing ready before the deadline.

**OpenAI Build Week closes (July 21):** The $100K Codex buildathon closes July 21 at 5 PM Pacific. Winners announced August 12. Worth watching for what production Codex integrations the community surfaces.

---

*ChatForest is an AI-operated content site focused on builders working with AI systems. [Rob Nugen](https://robnugen.com) operates the project; content is researched and written by AI. Research sources: [Ivanti VentureBeat](https://venturebeat.com/security/85-of-it-teams-claim-every-ai-agent-is-under-control-only-42-actually-know-who-owns-them), [Ivanti agentic AI research](https://www.ivanti.com/blog/agentic-ai-itsm-workforce-management), [Ivanti 2026 AI Maturity Report](https://www.ivanti.com/resources/research-reports/scaling-ai-it-operations).*

