# MAI-Thinking-1: Microsoft's First Reasoning Model Is Not a Distillation

> Microsoft announced MAI-Thinking-1 at Build 2026 — a reasoning model trained from scratch, not distilled from GPT-4 or any other frontier model. It's bundled with GitHub Copilot Enterprise and runs inside Azure Confidential Computing enclaves. Here's what builders need to know.


**At a glance:** MAI-Thinking-1, announced June 2, 2026 at Microsoft Build. Microsoft's first dedicated reasoning model. Not trained via distillation from existing frontier models. Available on Azure AI Foundry and GitHub Models. Pay-as-you-go pricing on reasoning tokens (rates not yet published). Bundled with GitHub Copilot Enterprise. Confidential Computing enclave version planned. Part of our **[Builder's Log](/builders-log/)**.

---

Microsoft AI chief Mustafa Suleiman took the stage at Build 2026 today and announced something that hasn't existed before in the MAI family: a reasoning model. Not a coding model. Not an image generator. A model built specifically to think slowly through complex problems — and built without copying the reasoning traces of any other frontier system.

That last part matters more than it might seem.

---

## What MAI-Thinking-1 Is

The reasoning model category — models that spend extra compute on intermediate reasoning steps before returning a final answer — has been dominated for the past year by OpenAI's o-series, Google's Gemini thinking variants, and Anthropic's Claude extended thinking mode. DeepSeek R1, the open-weight entrant, shook the category in early 2025 but came with a significant provenance question: it was trained in part by distilling reasoning traces from OpenAI's models.

MAI-Thinking-1 is Microsoft's entry into this category, and Microsoft's explicit claim is that it was trained from scratch. No distillation from GPT-4. No teacher-model outputs. No reasoning traces borrowed from o3 or any other frontier system.

Microsoft has not published the specific training methodology — whether it used reinforcement learning from verifiable rewards (the technique behind OpenAI o1), process reward modeling, or a different approach. What they have confirmed is the negative: the model's training data did not include the probability distributions or output sequences of any other trained AI system.

---

## Why the "Not Distilled" Claim Is Strategic

Distillation is fast and effective, but it creates a legal and regulatory exposure for enterprise customers. If a model was trained on outputs from OpenAI's systems, a regulated enterprise deploying that model may have indirect exposure to OpenAI's training data, licensing terms, and any IP claims downstream.

This is not theoretical. The DeepSeek distillation controversy in Q1 2025 surfaced exactly this question for enterprises evaluating R1. Several large financial institutions that had considered R1 as an on-premise reasoning engine paused deployments pending legal review of what "trained on OpenAI outputs" meant for their liability posture.

MAI-Thinking-1 addresses that exposure directly. Microsoft's claim of independent training is the product's differentiator for the enterprise buyer segment that needs a clean IP lineage — not just a capable model.

For builders at startups or working in unregulated contexts, this distinction may feel abstract. For builders deploying AI into healthcare, finance, defense, or any context subject to procurement or data governance requirements, it is likely to show up as a procurement checkbox.

---

## Access: Azure AI Foundry and GitHub Models

MAI-Thinking-1 will be available through two access paths:

**Azure AI Foundry** — the primary enterprise access path. Pay-as-you-go pricing on reasoning tokens consumed. As of the Build 2026 announcement, per-token rates have not been published. The model is expected to appear in the Azure AI Foundry model catalog alongside the rest of the MAI family: MAI-Transcribe-1, MAI-Voice-1, MAI-Image-2, and their Build-era successors.

**GitHub Models** — the developer sandbox path. GitHub Models provides free-tier access to frontier models for prototyping and evaluation. MAI-Thinking-1 being available here is significant: it means developers can test reasoning capabilities without an Azure subscription, using their GitHub credentials.

Watch the Azure AI Foundry pricing page for rate disclosure. For comparison context: OpenAI o3 is currently priced at $10/1M input tokens and $40/1M output tokens; Gemini 2.5 Pro is $1.25/$10 with a 200K-token thinking budget. Where MAI-Thinking-1 lands in that range will determine whether it competes on value or positions as a premium enterprise product.

---

## GitHub Copilot Enterprise Bundling

MAI-Thinking-1 is bundled into GitHub Copilot Enterprise subscriptions. Microsoft's stated use cases for this integration are specific:

- **Architecture reviews** — reasoning over large codebases to assess structure, dependencies, and technical debt
- **Migration planning** — analyzing legacy systems and generating step-by-step migration strategies across frameworks or cloud environments
- **Incident post-mortems** — ingesting logs, trace data, and runbooks to reconstruct failure sequences and recommend remediations

These are all workloads that benefit from extended reasoning time and large context — not the low-latency completions that Copilot's existing code-suggestion flow delivers. The pairing with Project Polaris (which replaces GPT-4 Turbo as the Copilot default in August 2026 for completions) creates a two-tier system inside Copilot Enterprise:

- Polaris for fast, inline code completion and generation
- MAI-Thinking-1 for slow, deliberate architectural analysis

If you are running a Copilot Enterprise subscription, expect MAI-Thinking-1 to surface in Copilot Workspace and possibly in the Copilot Chat for complex queries. Microsoft has not published the exact UI surface and workflow integration yet.

---

## Confidential Computing Enclave Version

A containerized version of MAI-Thinking-1 designed to run inside **Azure Confidential Computing** enclaves was announced alongside the model.

Confidential Computing on Azure uses hardware-based trusted execution environments (TEEs) — specifically AMD SEV-SNP and Intel TDX — to encrypt data in use, not just at rest and in transit. The practical guarantee for the end user: even Microsoft's own infrastructure cannot read the code or data being analyzed inside the enclave.

This matters for specific enterprise segments:

- **Defense contractors** with code that cannot leave controlled environments
- **Financial institutions** with trading logic or proprietary risk models they cannot expose even to cloud providers
- **Healthcare organizations** running PHI through analytical pipelines
- **Any enterprise** subject to data residency requirements that make standard cloud AI problematic

No GA timeline was announced for the confidential enclave version. It was framed as "planned" alongside the standard Foundry deployment. For builders with privacy requirements at the infrastructure level, this is worth tracking — but it is not immediately buildable.

---

## Positioning Against the Reasoning Model Field

MAI-Thinking-1 enters a field with four established players:

| Model | Training lineage | Access | Notes |
|---|---|---|---|
| OpenAI o3 | OpenAI proprietary | API + ChatGPT | Strong benchmarks, high pricing |
| Gemini 2.5 Pro Thinking | Google DeepMind proprietary | Vertex AI + AI Studio | Competitive on cost, 1M context |
| Claude 3.7 Sonnet (extended thinking) | Anthropic proprietary | Anthropic API + AWS Bedrock | Streaming thinking tokens, 200K context |
| DeepSeek R1 | Partly distilled from OpenAI | Self-hosted + several APIs | Open-weight, IP provenance questions |
| MAI-Thinking-1 | Microsoft proprietary, not distilled | Azure AI Foundry + GitHub Models | No benchmarks published yet |

Microsoft has not published benchmark numbers for MAI-Thinking-1 as of the Build 2026 keynote. The "not distilled" claim and enterprise positioning are the lead differentiators at launch. Performance claims will follow as third-party evaluations emerge.

---

## What's Still Missing

The announcement today confirmed the model exists and its high-level positioning. The following details have not been released:

- **Benchmarks** — No MMLU, MATH, AIME, GPQA, or SWE-bench numbers published
- **Per-token pricing** — Only "pay-as-you-go on reasoning tokens" confirmed; no rates
- **Context window and max output** — Not disclosed
- **API schema** — No parameter names published (thinking budget, effort level, etc.)
- **Model ID** — Not yet in the Azure AI Foundry catalog as of June 2
- **Confidential Computing GA timeline** — "Planned" with no date

This is a day-one announcement. Expect the Azure AI Foundry documentation to fill in these gaps over the coming days as Microsoft publishes post-Build technical details. The [What's New in Microsoft Foundry blog](https://devblogs.microsoft.com/foundry/) is the canonical tracking source.

---

## Builder Checklist

**Now (day one):**
- [ ] If you have a GitHub Copilot Enterprise subscription, watch the Copilot Workspace update notes for MAI-Thinking-1 rollout
- [ ] Bookmark the [Azure AI Foundry model catalog](https://ai.azure.com/explore/models) — MAI-Thinking-1 should appear there with pricing when available
- [ ] If you're evaluating GitHub Models for prototyping, check for MAI-Thinking-1 availability in the models list

**When pricing drops:**
- [ ] Compare reasoning token cost against o3, Gemini 2.5 Pro, and Claude 3.7 Sonnet for your specific use case (long-context analysis vs. short reasoning bursts)
- [ ] If your deployment has IP provenance requirements, document that MAI-Thinking-1 was not distilled — this will be relevant for procurement review

**If you have confidential computing requirements:**
- [ ] Track the confidential enclave version timeline via the Azure Confidential Computing blog
- [ ] Evaluate whether hardware-level isolation changes your analysis of cloud AI feasibility for sensitive workloads

---

## The Bigger Picture at Build 2026

MAI-Thinking-1 is one piece of a larger announcement pattern at Build 2026. Alongside it:

- **Project Polaris** — Microsoft's coding model replaces GPT-4 Turbo in GitHub Copilot by August 2026. Not a reasoning model; a fast, code-specialized completion engine with MoE architecture and a Code Content Guarantee (IP indemnification for customers).
- **MAI-Image-2.5, MAI-Voice-2, MAI-Transcribe-1.5** — Next-gen multimodal suite announced at Build; pricing TBD, in preview on Foundry
- **Azure Agent Mesh** — Multi-agent cloud infrastructure announced for Q4 2026 GA
- **MCP in M365 declarative agents** — Now GA, enabling cross-vendor agent interoperability

The through-line: Microsoft is dismantling its OpenAI dependency systematically, replacing it with a proprietary model stack that it can price, fine-tune, and guarantee IP provenance for. MAI-Thinking-1 is the reasoning layer of that stack.

---

*MAI-Thinking-1 was announced June 2, 2026 at Microsoft Build. Technical specifications, benchmarks, and pricing will be updated as Microsoft publishes documentation. For related coverage, see our [Project Polaris builder guide](/builders-log/microsoft-build-2026-project-polaris-copilot-workspace-windows-agent-platform-builder-guide/) and [MAI multimodal family review](/reviews/microsoft-mai-transcribe-voice-image-multimodal-family-review/).*

