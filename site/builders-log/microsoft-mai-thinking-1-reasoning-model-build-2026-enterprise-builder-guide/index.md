# MAI-Thinking-1: Microsoft's First Reasoning Model Is Not a Distillation

> Microsoft announced MAI-Thinking-1 at Build 2026 — a reasoning model trained from scratch, not distilled from GPT-4 or any other frontier model. It launched in private preview on Microsoft Foundry. Here's what builders need to know.


**At a glance:** [MAI-Thinking-1](https://microsoft.ai/news/introducing-mai-thinking-1/), announced June 2, 2026 at Microsoft Build. Microsoft's first dedicated reasoning model. Microsoft says it was not trained via distillation from existing frontier models. Launched in [private preview on Microsoft Foundry](https://microsoft.ai/models/mai-thinking-1/), with public preview on the MAI Playground to follow; per-token pricing not yet published. Part of our **[Builder's Log](/builders-log/)**.

---

[Mustafa Suleyman](https://fortune.com/article/why-microsoft-ai-chief-mustafa-suleyman-predicts-ai-automation-18-months/), CEO of Microsoft AI, took the stage at Build 2026 on June 2, 2026 and [announced](https://microsoft.ai/news/introducing-mai-thinking-1/) something that hasn't existed before in the MAI family: a reasoning model. Not a coding model. Not an image generator. A model built specifically to think slowly through complex problems — and, Microsoft says, built without copying the reasoning traces of any other frontier system.

That last part matters more than it might seem.

---

## What MAI-Thinking-1 Is

The reasoning model category — models that spend extra compute on intermediate reasoning steps before returning a final answer — has been dominated for the past year by OpenAI's o-series, Google's Gemini thinking variants, and Anthropic's [Claude extended thinking mode](https://www.anthropic.com/news/claude-3-7-sonnet). [DeepSeek R1](https://github.com/deepseek-ai/DeepSeek-R1), the open-weight entrant, shook the category in early 2025 but came with a significant provenance question: OpenAI has publicly [accused DeepSeek](https://restofworld.org/2026/openai-deepseek-distillation-dispute-us-china/) of "inappropriately" distilling its models, and in a [February 2026 memo to the U.S. House Select Committee on China](https://finance.yahoo.com/news/openai-accuses-deepseek-distilling-us-221629899.html), OpenAI said it had observed "accounts associated with DeepSeek employees developing methods to circumvent OpenAI's access restrictions" to obtain outputs for distillation. DeepSeek has not confirmed the allegation, and OpenAI has not published direct evidence for it.

MAI-Thinking-1 is Microsoft's entry into this category, and Microsoft's explicit claim, made in its [own announcement](https://microsoft.ai/news/introducing-mai-thinking-1/), is that it was trained from scratch: "We don't distill from other labs and we don't rely on opaque data." No distillation from GPT-4. No teacher-model outputs. No reasoning traces borrowed from o3 or any other frontier system, per Microsoft's account.

Microsoft has not published the specific training methodology — whether it used reinforcement learning from verifiable rewards (the technique behind OpenAI o1), process reward modeling, or a different approach. What [Microsoft has confirmed](https://microsoft.ai/news/introducing-mai-thinking-1/) is the negative: the model's training data did not include outputs from any other trained AI system.

---

## Why the "Not Distilled" Claim Is Strategic

Distillation is fast and effective, but it creates a legal and regulatory exposure for enterprise customers. If a model was trained on outputs from OpenAI's systems, a regulated enterprise deploying that model may have indirect exposure to OpenAI's training data, licensing terms, and any IP claims downstream.

This is not theoretical. OpenAI's distillation accusation against DeepSeek, described above, is exactly this question surfacing for enterprises evaluating R1: a model with a disputed training lineage carries downstream legal uncertainty that a model with a documented lineage does not.

MAI-Thinking-1 addresses that exposure directly. Microsoft's claim of independent training is the product's differentiator for the enterprise buyer segment that needs a clean IP lineage — not just a capable model.

For builders at startups or working in unregulated contexts, this distinction may feel abstract. For builders deploying AI into healthcare, finance, defense, or any context subject to procurement or data governance requirements, it is likely to show up as a procurement checkbox.

---

## Access: Private Preview on Microsoft Foundry

As of the Build 2026 announcement, [MAI-Thinking-1 is in private preview on Microsoft Foundry](https://microsoft.ai/models/mai-thinking-1/), with a public preview on the MAI Playground "coming" and Chat Completions API compatibility. Microsoft's own model page and announcement post do not state general availability on Azure AI Foundry, a GitHub Models listing, GitHub Copilot Enterprise bundling, or a confidential-computing enclave variant for this model — none of that has been confirmed by Microsoft for MAI-Thinking-1, so treat any such claim as unverified until Microsoft documents it. (GitHub Copilot's newly announced in-house model at Build 2026 is a separate model, [MAI-Code-1-Flash](https://microsoft.ai/news/building-a-hillclimbing-machine-launching-seven-new-mai-models/), not MAI-Thinking-1.)

Per-token pricing for MAI-Thinking-1 has not been published. For comparison context: [OpenAI's o3](https://developers.openai.com/api/docs/pricing) is currently priced at $2/1M input tokens and $8/1M output tokens (cut 80% from its original $10/$40 launch pricing in [June 2025](https://venturebeat.com/ai/openai-announces-80-price-drop-for-o3-its-most-powerful-reasoning-model)); [Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/pricing) is $1.25/$10 per 1M tokens for prompts up to 200K tokens (thinking tokens are billed as output tokens, not a separate "thinking budget"). Where MAI-Thinking-1 lands in that range will determine whether it competes on value or positions as a premium enterprise product.

---

## Positioning Against the Reasoning Model Field

MAI-Thinking-1 enters a field with four established players:

| Model | Training lineage | Access | Notes |
|---|---|---|---|
| OpenAI o3 | OpenAI proprietary | API + ChatGPT | Strong benchmarks, [$2/$8 per 1M tokens](https://developers.openai.com/api/docs/pricing) |
| Gemini 2.5 Pro Thinking | Google DeepMind proprietary | Vertex AI + AI Studio | [1M-token context window](https://blog.google/innovation-and-ai/models-and-research/google-deepmind/gemini-model-thinking-updates-march-2025/) |
| Claude 3.7 Sonnet (extended thinking) | Anthropic proprietary | Anthropic API + AWS Bedrock | [Streaming thinking tokens, 200K context](https://www.anthropic.com/news/claude-3-7-sonnet) |
| DeepSeek R1 | [OpenAI alleges partial distillation (unconfirmed)](https://restofworld.org/2026/openai-deepseek-distillation-dispute-us-china/) | Self-hosted + several APIs | Open-weight, disputed IP provenance |
| MAI-Thinking-1 | Microsoft proprietary, not distilled (Microsoft's claim) | Private preview, Microsoft Foundry | [97.0% AIME 2025, 94.5% AIME 2026, matches Claude Opus 4.6 on SWE-Bench Pro](https://microsoft.ai/news/introducing-mai-thinking-1/) |

Microsoft [published benchmark numbers for MAI-Thinking-1](https://microsoft.ai/news/introducing-mai-thinking-1/) at the Build 2026 keynote itself — 97.0% on AIME 2025, 94.5% on AIME 2026, and SWE-Bench Pro results Microsoft says match Claude Opus 4.6 — rather than holding them back for a later release. The "not distilled" claim, those benchmark numbers, and enterprise positioning are the lead differentiators at launch. Independent third-party evaluations, which have not yet emerged, will be the real test of the self-reported numbers.

---

## What's Still Missing

The [announcement](https://microsoft.ai/news/introducing-mai-thinking-1/) confirmed the model exists, disclosed its architecture (35B active / ~1T total parameters, sparse MoE, [256K-token context window](https://microsoft.ai/models/mai-thinking-1/)), and published AIME/SWE-Bench Pro benchmark numbers. The following details are still missing:

- **MMLU, MATH, and GPQA benchmark numbers** — not published (only AIME 2025/2026 and SWE-Bench Pro results were shared at launch)
- **Per-token pricing** — not published
- **Max output tokens** — not disclosed
- **API schema** — no parameter names published (thinking budget, effort level, etc.)
- **General availability timeline** — currently private preview on Microsoft Foundry only; no date given for public preview or GA

This is a day-one announcement. Expect the Microsoft Foundry documentation to fill in these gaps over the coming days as Microsoft publishes post-Build technical details. The [What's New in Microsoft Foundry blog](https://devblogs.microsoft.com/foundry/) is the canonical tracking source.

---

## Builder Checklist

**Now (day one):**
- [ ] Request [private preview access on Microsoft Foundry](https://microsoft.ai/models/mai-thinking-1/) if you want hands-on evaluation before general availability
- [ ] Bookmark the [Azure AI Foundry model catalog](https://ai.azure.com/explore/models) — MAI-Thinking-1 should appear there with pricing when it moves past private preview
- [ ] Watch the [Microsoft Foundry blog](https://devblogs.microsoft.com/foundry/) for the public-preview and GA announcements

**When pricing drops:**
- [ ] Compare reasoning token cost against o3, Gemini 2.5 Pro, and Claude 3.7 Sonnet for your specific use case (long-context analysis vs. short reasoning bursts)
- [ ] If your deployment has IP provenance requirements, document that MAI-Thinking-1 was not distilled (per Microsoft's own claim) — this will be relevant for procurement review

---

## The Bigger Picture at Build 2026

MAI-Thinking-1 is one piece of a larger announcement pattern at Build 2026. Alongside it, Microsoft [unveiled seven in-house MAI models](https://microsoft.ai/news/building-a-hillclimbing-machine-launching-seven-new-mai-models/) in total:

- **[MAI-Code-1-Flash](https://microsoft.ai/news/building-a-hillclimbing-machine-launching-seven-new-mai-models/)** — Microsoft's first in-house coding model, a 5B-parameter model trained on GitHub Copilot's production harnesses and rolling out across Copilot plans
- **[MAI-Image-2.5, MAI-Voice-2, MAI-Transcribe-1.5](https://microsoft.ai/news/building-a-hillclimbing-machine-launching-seven-new-mai-models/)** — Next-gen multimodal suite announced at Build; pricing TBD, in preview on Foundry
- **[MCP in M365 declarative agents](https://devblogs.microsoft.com/microsoft365dev/build-declarative-agents-for-microsoft-365-copilot-with-mcp/)** — Reached GA in December 2025, enabling cross-vendor agent interoperability

*Editor's note (2026-07-28): an earlier version of this article referenced "Project Polaris" and "Azure Agent Mesh" as Build 2026 announcements. A citation audit found neither name appears in any Microsoft primary source (official blogs, devblogs, techcommunity, github.blog, microsoft.ai, or the Build 2026 live blog/keynote/Book of News) — both references traced back to aggregator content, not Microsoft. They have been removed as unconfirmed.*

The through-line: Microsoft is investing in a proprietary, in-house model stack — spanning reasoning, code, image, voice, and transcription — that it can price, fine-tune, and control the training provenance of, rather than relying solely on OpenAI's models. MAI-Thinking-1 is the reasoning layer of that stack.

---

*MAI-Thinking-1 was announced June 2, 2026 at Microsoft Build. Technical specifications, benchmarks, and pricing will be updated as Microsoft publishes documentation. For related coverage, see our [MAI multimodal family review](/reviews/microsoft-mai-transcribe-voice-image-multimodal-family-review/).*

