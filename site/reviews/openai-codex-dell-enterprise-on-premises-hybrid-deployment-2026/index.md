# OpenAI and Dell Bring Codex On-Premises — What It Means for the Enterprises Still Sitting Out

> OpenAI and Dell Technologies announced a partnership on May 18, 2026, to bring Codex into hybrid and on-premises enterprise environments via the Dell AI Data Platform and Dell AI Factory. Here's what the deal covers, what it doesn't, and why it matters for regulated industries.


**At a glance:** OpenAI and Dell Technologies announced on May 18, 2026 that they are partnering to bring Codex into hybrid and on-premises enterprise environments. Codex connects to the Dell AI Data Platform for governed on-prem data access, with deeper Dell AI Factory integration under exploration. The announcement is a framework — enterprise pricing is custom, and the AI Factory piece is not yet production-ready. Part of our **[OpenAI coverage](/tags/openai/)**.

---

Codex now reaches 4 million weekly active developers. That is a large number, but it is also a ceiling: a significant segment of enterprise engineering has been watching from the sidelines, unwilling to route internal code, business data, or regulated customer records through OpenAI's cloud. The OpenAI-Dell partnership, announced May 18, 2026, is the most direct answer to that holdout so far.

---

## What the Partnership Actually Covers

The deal has two layers, at different levels of readiness.

**Layer 1: Dell AI Data Platform integration (announced, in progress)**

The Dell AI Data Platform is how large organizations manage structured and unstructured enterprise data on-premises — code repositories, documentation, operational knowledge bases, system records. Under this partnership, Codex can connect to data stored on the Dell AI Data Platform without that data leaving the enterprise perimeter.

The practical implication: a team running Codex can give it access to internal codebases, runbooks, architecture documents, and business context that they would never put through a public API. Codex then uses that context to complete tasks — writing tests against real internal APIs, generating documentation that reflects actual system behavior, reasoning across a codebase that lives entirely on-prem.

OpenAI says the Dell AI Data Platform integration is in progress for Q2 2026 deployment.

**Layer 2: Dell AI Factory integration (under exploration)**

The Dell AI Factory is the compute side — the infrastructure businesses use to run AI workloads on-premises or in colocation environments. OpenAI and Dell said they will "explore" how Codex, ChatGPT Enterprise, and other API-based products can interface with AI Factory infrastructure: data preparation, system-of-record management, test execution, and deployment of AI applications inside enterprise environments.

"Under exploration" means it is not production-ready yet. This part of the partnership is a commitment to a direction, not a shipping feature.

---

## Why This Matters

Three categories of enterprise have been structurally locked out of agentic coding tools until now.

**Regulated industries.** Healthcare organizations under HIPAA, financial institutions under FINRA and SOX, government contractors under FedRAMP restrictions — none of them can route production data to cloud inference APIs without extensive compliance review, and often not at all. On-premises deployment with a vendor-supported path (not a self-hosted experiment) changes that calculus.

**IP-sensitive organizations.** Companies building proprietary algorithms or operating in markets where code is a core competitive asset have legitimate reasons to avoid training signals leaking to cloud providers. Even when OpenAI provides contractual assurances against training on Enterprise data, the risk perception remains high. Running Codex against a Dell-hosted environment addresses the perception as much as the technical reality.

**Cost-sensitive scale deployments.** Agentic workflows compound token consumption in ways that single-user AI tools do not. A Codex agent running Goal Mode for six hours generates far more API calls than a developer using Copilot for autocomplete. Dell's framing for this partnership explicitly includes economics: running inference close to data reduces latency, avoids unnecessary round-trips to cloud APIs, and makes the cost structure more predictable for large-scale deployments.

---

## What Has Changed Around Codex

The Dell announcement arrives during a period of rapid Codex expansion. Several developments in May 2026 are relevant context:

**4 million weekly developers.** As of the Dell announcement, Codex has 4 million weekly active users — up from 3 million cited in OpenAI's Q1 enterprise update. The growth is primarily in the developer segment, but OpenAI is actively pushing Codex into broader knowledge work.

**Codex beyond coding.** OpenAI's framing for the Dell partnership consistently described Codex expanding beyond software development. Teams are using Codex-powered agents to gather context across tools, prepare reports, route product feedback, qualify sales leads, write follow-ups, and coordinate workflows across business systems. This broader positioning is important: the Dell integration is not just for engineering teams. It is aimed at any knowledge worker whose workflows touch internal governed data.

**Goal Mode stability.** The [Codex Cloud platform](/reviews/openai-codex-cloud-agentic-coding-platform-review/) reached stable Goal Mode on May 22 — multi-hour, multi-day autonomous task execution across session breaks. An on-premises data connection makes Goal Mode meaningfully more useful for enterprise tasks, because the agent has access to the full internal context it needs without requiring manual uploads or sanitized excerpts.

---

## What It Does Not Cover

The announcement leaves several enterprise questions unanswered.

**Pricing.** Enterprise Codex pricing is listed as "custom" — no published rate card exists for the Dell-integrated tier. Organizations interested in the on-premises path need to engage Dell and OpenAI sales directly.

**The AI Factory integration.** The more powerful half of the partnership — running Codex compute on Dell AI Factory infrastructure — is not yet available. The language ("explore how") is accurate but worth noting: the timeline for that capability is unannounced.

**Model updates and on-prem lag.** One perpetual tension with on-premises AI deployments is version currency. When OpenAI releases codex-2 or a new GPT-5.x variant with improved coding performance, will on-premises Dell deployments receive that update on the same timeline as cloud users? The partnership announcement does not address this.

**Competitive context.** Microsoft has been deploying Copilot on-premises through GitHub Copilot for Business with on-premises network routing options since late 2025. Anthropic offers Claude Code with enterprise self-hosting for qualified customers. The Dell partnership gives OpenAI a comparable story, but it is not arriving to an empty market.

---

## The Bottom Line

For the 4 million developers already using Codex Cloud, this announcement changes nothing. The on-premises path is for a different customer entirely: enterprises with strict data governance requirements, regulated industries that could not consider Codex before, and large organizations weighing on-premises inference economics as they scale agentic workflows.

The Dell AI Data Platform integration is the piece that will actually ship near-term. The AI Factory integration is real but longer-dated. If your organization has been waiting for Codex to have an on-premises story before engaging, the story now exists — though the details of pricing and compute-side deployment will require a direct conversation with Dell and OpenAI enterprise sales.

---

*OpenAI/Dell partnership announced May 18, 2026. Codex Cloud review updated May 24, 2026 — see our [full Codex Cloud platform review](/reviews/openai-codex-cloud-agentic-coding-platform-review/) for the product-level breakdown.*

