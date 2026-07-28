# OpenAI and Dell Bring Codex On-Premises — What It Means for the Enterprises Still Sitting Out

> OpenAI and Dell Technologies announced a partnership on May 18, 2026, to bring Codex into hybrid and on-premises enterprise environments via the Dell AI Data Platform and Dell AI Factory. Here's what the deal covers, what it doesn't, and why it matters for regulated industries.


**At a glance:** OpenAI and Dell Technologies announced on May 18, 2026 that they are partnering to bring Codex into hybrid and on-premises enterprise environments. Codex connects to the Dell AI Data Platform for governed on-prem data access, with deeper Dell AI Factory integration under exploration. The announcement is a framework — enterprise pricing is custom, and the AI Factory piece is not yet production-ready. Part of our **[OpenAI coverage](/tags/openai/)**.

---

Codex now reaches [4 million weekly active developers](https://openai.com/index/scaling-codex-to-enterprises-worldwide/). That is a large number, but it is also a ceiling: a significant segment of enterprise engineering has been watching from the sidelines, unwilling to route internal code, business data, or regulated customer records through OpenAI's cloud. The [OpenAI-Dell partnership, announced May 18, 2026](https://openai.com/index/dell-codex-enterprise-partnership/), is the most direct answer to that holdout so far.

---

## What the Partnership Actually Covers

The deal has two layers, at different levels of readiness.

**Layer 1: Dell AI Data Platform integration (announced, in progress)**

The Dell AI Data Platform is how large organizations manage structured and unstructured enterprise data on-premises — code repositories, documentation, operational knowledge bases, system records. Under this partnership, Codex can connect to data stored on the Dell AI Data Platform without that data leaving the enterprise perimeter.

The practical implication: a team running Codex can give it access to internal codebases, runbooks, architecture documents, and business context that they would never put through a public API. Codex then uses that context to complete tasks — writing tests against real internal APIs, generating documentation that reflects actual system behavior, reasoning across a codebase that lives entirely on-prem.

Neither company has published a specific launch date for the Codex–Dell AI Data Platform connection itself. Dell has separately scheduled orchestration and search upgrades to the AI Data Platform product for Q2 2026 ([WinBuzzer](https://winbuzzer.com/2026/05/19/openai-and-dell-bring-codex-closer-to-enterprise-data-xcxwbn/)) — a platform-wide roadmap item, not a Codex-specific commitment.

**Layer 2: Dell AI Factory integration (under exploration)**

The Dell AI Factory is the compute side — the infrastructure businesses use to run AI workloads on-premises or in colocation environments. [OpenAI and Dell said they will "explore" how Codex, ChatGPT Enterprise, and other API-based products can interface with AI Factory infrastructure](https://openai.com/index/dell-codex-enterprise-partnership/): data preparation, system-of-record management, test execution, and deployment of AI applications inside enterprise environments.

"Under exploration" means it is not production-ready yet. This part of the partnership is a commitment to a direction, not a shipping feature.

---

## Why This Matters

Three categories of enterprise have been structurally locked out of agentic coding tools until now.

**Regulated industries.** Healthcare organizations under HIPAA, financial institutions under FINRA and SOX, government contractors under FedRAMP restrictions — none of them can route production data to cloud inference APIs without extensive compliance review, and often not at all. On-premises deployment with a vendor-supported path (not a self-hosted experiment) changes that calculus.

**IP-sensitive organizations.** Companies building proprietary algorithms or operating in markets where code is a core competitive asset have legitimate reasons to avoid training signals leaking to cloud providers. Even when [OpenAI provides contractual assurances against training on Enterprise data](https://openai.com/enterprise-privacy/), the risk perception remains high. Running Codex against a Dell-hosted environment addresses the perception as much as the technical reality.

**Cost-sensitive scale deployments.** Agentic workflows compound token consumption in ways that single-user AI tools do not — [Dell SVP Jon Siegal has pointed to a developer consuming 1 billion tokens in 24 hours generating a $3,400 cloud bill](https://www.forbes.com/sites/janakirammsv/2026/05/18/dell-becomes-openais-on-prem-channel-for-frontier-models/) as the kind of usage pattern public cloud pricing struggles to absorb. [Dell's framing for this partnership explicitly includes economics](https://www.forbes.com/sites/janakirammsv/2026/05/18/dell-becomes-openais-on-prem-channel-for-frontier-models/): running inference close to data reduces latency, avoids unnecessary round-trips to cloud APIs, and makes the cost structure more predictable for large-scale deployments.

---

## What Has Changed Around Codex

The Dell announcement arrives during a period of rapid Codex expansion. Several developments in May 2026 are relevant context:

**4 million weekly developers.** As of the Dell announcement, Codex has 4 million weekly active users. [OpenAI reported the jump from more than 3 million to more than 4 million happened within about two weeks in early-to-mid April 2026](https://openai.com/index/scaling-codex-to-enterprises-worldwide/) — not a quarterly figure, but a rapid short-cycle spike. The growth is primarily in the developer segment, but OpenAI is actively pushing Codex into broader knowledge work.

**Codex beyond coding.** [OpenAI's framing for the Dell partnership consistently described Codex expanding beyond software development](https://openai.com/index/dell-codex-enterprise-partnership/): teams are using Codex-powered agents to gather context across tools, prepare reports, route product feedback, qualify sales leads, write follow-ups, and coordinate workflows across business systems. This broader positioning is important: the Dell integration is not just for engineering teams. It is aimed at any knowledge worker whose workflows touch internal governed data.

**Goal Mode stability.** The [Codex Cloud platform](/reviews/openai-codex-cloud-agentic-coding-platform-review/) reached stable Goal Mode on May 22 — multi-hour, multi-day autonomous task execution across session breaks. An on-premises data connection makes Goal Mode meaningfully more useful for enterprise tasks, because the agent has access to the full internal context it needs without requiring manual uploads or sanitized excerpts.

---

## What It Does Not Cover

The announcement leaves several enterprise questions unanswered.

**Pricing.** Enterprise Codex pricing is listed as "custom" — no published rate card exists for the Dell-integrated tier. Organizations interested in the on-premises path need to engage Dell and OpenAI sales directly.

**The AI Factory integration.** The more powerful half of the partnership — running Codex compute on Dell AI Factory infrastructure — is not yet available. The language ("explore how") is accurate but worth noting: the timeline for that capability is unannounced.

**Model updates and on-prem lag.** One perpetual tension with on-premises AI deployments is version currency. When OpenAI releases codex-2 or a new GPT-5.x variant with improved coding performance, will on-premises Dell deployments receive that update on the same timeline as cloud users? The partnership announcement does not address this.

**Competitive context.** Neither major rival offers a true on-premises equivalent yet. GitHub Copilot requires connectivity to GitHub's cloud for inference; the closest Microsoft has shipped is [self-hosted runner support for Copilot coding agent's development environment, in public preview since October 2025](https://github.blog/changelog/2025-10-28-copilot-coding-agent-now-supports-self-hosted-runners/) — which keeps the execution sandbox on customer infrastructure but not the model itself. Anthropic's Claude Code [deploys through Amazon Bedrock, Google Vertex AI, or Microsoft Azure](https://code.claude.com/docs/en/third-party-integrations) so enterprises can route traffic through their own cloud tenancy, but that is cloud-hosted inference, not on-premises deployment. The Dell partnership gives OpenAI a genuinely different story on this specific axis, though it is not arriving to an empty competitive market overall.

---

## The Bottom Line

For the 4 million developers already using Codex Cloud, this announcement changes nothing. The on-premises path is for a different customer entirely: enterprises with strict data governance requirements, regulated industries that could not consider Codex before, and large organizations weighing on-premises inference economics as they scale agentic workflows.

The Dell AI Data Platform integration is the piece that will actually ship near-term. The AI Factory integration is real but longer-dated. If your organization has been waiting for Codex to have an on-premises story before engaging, the story now exists — though the details of pricing and compute-side deployment will require a direct conversation with Dell and OpenAI enterprise sales.

---

---

**Sources:** [OpenAI — Dell Codex enterprise partnership announcement](https://openai.com/index/dell-codex-enterprise-partnership/) · [OpenAI — Scaling Codex to enterprises worldwide (3M→4M weekly developers, April 2026)](https://openai.com/index/scaling-codex-to-enterprises-worldwide/) · [OpenAI — Enterprise privacy (no training on Enterprise data by default)](https://openai.com/enterprise-privacy/) · [Forbes — Dell becomes OpenAI's on-prem channel for frontier models](https://www.forbes.com/sites/janakirammsv/2026/05/18/dell-becomes-openais-on-prem-channel-for-frontier-models/) · [WinBuzzer — OpenAI and Dell bring Codex to enterprise data](https://winbuzzer.com/2026/05/19/openai-and-dell-bring-codex-closer-to-enterprise-data-xcxwbn/) · [Pulse2 — full partnership announcement coverage](https://pulse2.com/openai-and-dell-technologies-announce-codex-partnership-to-bring-ai-agents-to-hybrid-and-on-premises-enterprise-environments/) · [GitHub Changelog — Copilot coding agent self-hosted runners](https://github.blog/changelog/2025-10-28-copilot-coding-agent-now-supports-self-hosted-runners/) · [Claude Code docs — enterprise deployment overview](https://code.claude.com/docs/en/third-party-integrations)

*OpenAI/Dell partnership announced May 18, 2026. Codex Cloud review updated May 24, 2026 — see our [full Codex Cloud platform review](/reviews/openai-codex-cloud-agentic-coding-platform-review/) for the product-level breakdown.*

