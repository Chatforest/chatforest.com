# Amazon Nova LLM Review — AWS-Native AI with Best-in-Class Pricing and Deep Bedrock Integration

> Amazon Nova (launched December 2024, Nova Premier April 2025) is AWS's in-house LLM family: four text and multimodal models from $0.035/M tokens (Micro) to $2.50/M (Premier). Deep Bedrock integration, native video understanding, and model distillation pipelines. Intelligence scores below median for price tier. Rating: 3.5/5.


Amazon's AI strategy has long looked like a distribution play more than a research bet. AWS hosts Claude via Anthropic's partnership, GPT-4o through Azure's equivalent arrangement, and Llama 4 through Meta's open-weight releases. For years, the implicit message was that AWS customers could access any frontier model — as long as they stayed in the cloud. Amazon was the platform, not the lab.

That posture shifted at [AWS re:Invent 2024](https://aws.amazon.com/blogs/aws/top-announcements-of-aws-reinvent-2024/), when Amazon launched **Amazon Nova**: four in-house language models trained on infrastructure that powers Alexa, Amazon.com search, Amazon Ads, and AWS Marketplace catalog systems. Nova was not a research announcement. It was [a product launch](https://techcrunch.com/2024/12/03/amazon-announces-nova-a-new-family-of-multimodal-ai-models/) backed by years of internal deployment and accompanied by [pricing that undercut every comparable model at the time](https://aws.amazon.com/blogs/aws/introducing-amazon-nova-frontier-intelligence-and-industry-leading-price-performance/).

The question Nova raises is not whether Amazon can build competitive models. The question is whether Nova's integration depth with AWS compensates for intelligence benchmarks that trail the frontier. This review examines both sides.

**Update (2026-08-22):** Since this review was first published, Amazon's own Bedrock documentation has moved **Nova Premier to Legacy status** (as of March 13, 2026) with an **end-of-life date of September 14, 2026** — about three weeks from this update. New customers can no longer start using Premier, and existing customers should migrate before EOL. Reuters-syndicated reporting (via Business Insider, July 28, 2026) says Amazon is winding down most of its flagship first-party Nova models — including Premier, the Omni model, Nova Reel, and Nova Canvas — to concentrate engineering and compute on a single new frontier model from its internal Frontier Model Research group (led by Pieter Abbeel), expected to debut at AWS re:Invent 2026; an AWS spokesperson told Business Insider the company will keep supporting models customers rely on and provide migration guidance as the lineup evolves. Nova Micro, Nova Lite, and Nova Pro remain Active. Nova 2 Lite reached general availability December 2, 2025; Nova 2 Pro remains preview-only as of this update. Details and sources are noted inline below. Sources: [AWS Bedrock model lifecycle](https://docs.aws.amazon.com/bedrock/latest/userguide/model-lifecycle.html), [Nova Premier model card](https://docs.aws.amazon.com/bedrock/latest/userguide/model-card-amazon-nova-premier.html), [Business Insider report via Yahoo Finance](https://finance.yahoo.com/technology/ai/articles/amazon-winds-down-most-flagship-103406019.html).

---

## What Amazon Nova Is

Amazon Nova is a family of foundation models available through **Amazon Bedrock**, AWS's managed AI service. The "understanding" models — the text-in, text-out LLMs — are the focus of this review. (Nova Canvas and Nova Reel, the image and video generation models respectively, are covered separately.)

All Nova understanding models share a few baseline properties:
- Available exclusively through Amazon Bedrock (no open weights, no self-hosting)
- Support the Bedrock Converse API and InvokeModel API
- Natively support tool use, streaming, and batch inference
- Integrate with Bedrock Knowledge Bases (RAG), Bedrock Agents (multi-agent orchestration), Bedrock Guardrails, and Bedrock Prompt Flows
- Support 200+ languages with 15 optimized (English, Spanish, French, German, Japanese, Korean, Mandarin Chinese, Arabic, Italian, Portuguese, Hindi, Dutch, Turkish, Polish, Swedish)
- Accept documents in PDF, CSV, DOC, DOCX, XLS, XLSX, HTML, TXT, and MD formats (except Micro, which is text-only)

The models were built by Amazon's internal AI teams, not Anthropic or any acquired lab. AWS states that the models were trained and validated on Amazon's own production workloads before external release — an unusual form of internal stress testing that most AI labs cannot replicate.

---

## The Model Lineup

### Nova v1 Understanding Models (December 2024 – Present)

**Amazon Nova Micro** is the text-only entry point. 128K context window. No image, video, or document input. At $0.035 per million input tokens and $0.14 per million output tokens, it was the cheapest model from any major provider at launch. Compared to Gemini 1.5 Flash-8B ($0.0375 input) or Claude Haiku ($0.25 input), Nova Micro's pricing is aggressive. Speed: approximately 313 tokens per second by third-party measurement at original publication; [Artificial Analysis measured ~280 tok/s as of this update](https://artificialanalysis.ai/models/nova-micro) — the "top five fastest globally" ranking could not be re-verified and has been removed.

**Amazon Nova Lite** adds multimodal input: text, images, and up to 30 minutes of video per call. 300K context window. At $0.06 per million input tokens and $0.24 output, it was cheaper than Gemini 1.5 Flash at launch. Video understanding was a genuine differentiator at the time — OpenAI and Anthropic models on Bedrock did not natively accept video input.

**Amazon Nova Pro** is the full-featured mid-range model. 300K context. Text, image, and video input. $0.80 per million input tokens and $3.20 output. Supports supervised fine-tuning and can serve as a student in model distillation pipelines (see below). Speed is adequate for production workloads.

**Amazon Nova Premier** is the flagship, [released for general availability on April 30, 2025](https://aws.amazon.com/blogs/aws/amazon-nova-premier-our-most-capable-model-for-complex-tasks-and-teacher-for-model-distillation/) — five months after the initial Nova launch. 1M context window. Text, image, and video input. $2.50 per million input tokens and $12.50 output (list pricing; see update below). The pricing places it in the Claude 3.7 Sonnet / GPT-4o tier. Unlike the other v1 models, Premier does **not** support fine-tuning or provisioned throughput — it is the teacher model for distillation, not the student. Available in US East (N. Virginia) in-region, with Geo cross-region inference to US East (Ohio) and US West (Oregon).

**Update (2026-08-22):** Nova Premier's [AWS Bedrock model card](https://docs.aws.amazon.com/bedrock/latest/userguide/model-card-amazon-nova-premier.html) now lists **Model lifecycle: Legacy** (transitioned March 13, 2026) with **Model EOL date: September 14, 2026**, confirmed by [AWS's model lifecycle page](https://docs.aws.amazon.com/bedrock/latest/userguide/model-lifecycle.html). New customers cannot start using a Legacy model, and AWS's lifecycle policy states pricing "should be expected" to rise during the public extended access portion of the Legacy period — check current pricing on the [Bedrock pricing page](https://aws.amazon.com/bedrock/pricing/) before deploying against Premier. The max output token limit is also higher than at launch: AWS's model card now lists **25K max output tokens** for Premier (see the correction on the v1 output cap below).

| Model | Context | Modalities In | Input Price | Output Price | Speed | Lifecycle (2026-08-22) |
|-------|---------|--------------|-------------|--------------|-------|-------------------------|
| Nova Micro | 128K | Text | $0.035/M | $0.14/M | ~313 tok/s at launch, ~280 tok/s now | Active |
| Nova Lite | 300K | Text, Image, Video | $0.06/M | $0.24/M | ~170 tok/s | Active |
| Nova Pro | 300K | Text, Image, Video | $0.80/M | $3.20/M | N/A | Active |
| Nova Premier | 1M | Text, Image, Video | $2.50/M | $12.50/M | ~30 tok/s at launch, ~34 tok/s now | **Legacy — EOL Sept 14, 2026** |

Prices shown are list prices at original publication; confirm current pricing (Premier's may rise during its Legacy public-extended-access period) on the [Bedrock pricing page](https://aws.amazon.com/bedrock/pricing/). Lifecycle status per [AWS's model lifecycle page](https://docs.aws.amazon.com/bedrock/latest/userguide/model-lifecycle.html).

**Correction (2026-08-22):** the v1 models did not share a uniform 10,000-token output cap. AWS's current [Bedrock model cards](https://docs.aws.amazon.com/bedrock/latest/userguide/model-card-amazon-nova-pro.html) list **5K max output tokens** for Nova Micro, Nova Lite, and Nova Pro, and **25K max output tokens** for Nova Premier (see [Micro](https://docs.aws.amazon.com/bedrock/latest/userguide/model-card-amazon-nova-micro.html) and [Lite](https://docs.aws.amazon.com/bedrock/latest/userguide/model-card-amazon-nova-lite.html) model cards). Prompt caching reduces input costs by 75%.

### Nova v2 (2025 – Present)

Amazon has extended the Nova family with several new models in 2025 that address gaps in the v1 lineup:

**Nova 2 Lite** adds extended thinking (chain-of-thought reasoning with three intensity levels), built-in web grounding (real-time web access without RAG setup), a built-in code interpreter (Python execution), remote MCP tool support, and reinforcement fine-tuning in addition to standard supervised fine-tuning. Context extended to 1M tokens. Output extended to 65,536 tokens (v1 Micro/Lite/Pro cap is 5K, per the correction above — Nova 2 Lite's cap is a larger jump than originally stated). This is a substantial capability upgrade over Nova Lite v1. **Update (2026-08-22):** Nova 2 Lite [reached general availability December 2, 2025](https://aws.amazon.com/about-aws/whats-new/2025/12/nova-2-foundation-models-amazon-bedrock/), with global cross-region inference. Current list pricing is **$0.30 per million input tokens and $2.50 per million output tokens** ([OpenRouter](https://openrouter.ai/amazon/nova-2-lite-v1); confirm against the [Bedrock pricing page](https://aws.amazon.com/bedrock/pricing/) before deploying) — notably higher than Nova Lite v1's $0.06/$0.24.

**Nova 2 Sonic** is a speech-to-speech model, [generally available since December 2, 2025](https://docs.aws.amazon.com/nova/latest/nova2-userguide/release-notes.html), supporting bidirectional streaming for low-latency voice applications. The 7-language figure checks out: AWS's [launch announcement](https://aws.amazon.com/blogs/aws/introducing-amazon-nova-2-sonic-next-generation-speech-to-speech-model-for-conversational-ai/) confirms English, Spanish, German, French, Italian, Portuguese, and Hindi. AWS shipped quality refreshes in [March 2026](https://docs.aws.amazon.com/nova/latest/nova2-userguide/release-notes.html) (Polly-compatible voices, latency cuts) and [May 2026](https://docs.aws.amazon.com/nova/latest/nova2-userguide/release-notes.html) (an 88% reduction in speech-generation hallucinations on AWS's internal test set), deployed as in-place updates with no API changes required.

**Nova 2 Pro** is positioned as the most capable Nova model with extended thinking. **Update (2026-08-22):** as of this update it remains in **preview only**, with early access limited to Amazon Nova Forge customers — [AWS's own December 2025 GA announcement](https://aws.amazon.com/about-aws/whats-new/2025/12/nova-2-foundation-models-amazon-bedrock/) confirms this, and no subsequent AWS announcement of general availability was found. List pricing (per third-party trackers, unverified against AWS's own pricing page) is roughly **$1.25 per million input tokens and $10.00 per million output tokens**.

**Nova Forge** is a service allowing customers to train fully custom frontier models using Amazon's own training infrastructure, not just fine-tuning. Annual subscription pricing. Represents Amazon's highest-tier AI offering for enterprises wanting proprietary model differentiation.

---

## The AWS-Native Advantage

Nova's primary value proposition is not raw benchmark performance — it is integration depth with the AWS ecosystem. For organizations already running workloads on AWS, Nova offers capabilities that third-party models on Bedrock do not:

### Model Distillation Pipelines

Nova's distillation hierarchy is a genuine differentiator. Nova Premier can act as a teacher model: AWS generates synthetic training data using Premier's outputs, which is then used to fine-tune Pro, Lite, or Micro with the customer's use case. The result is a smaller, cheaper, faster custom model that preserves much of Premier's task-specific quality.

This is not standard fine-tuning — it is knowledge distillation, using the large model's distribution to improve a smaller model. AWS has built this into the Bedrock console with a managed workflow. For high-volume production tasks where Premier's quality matters but Premier's latency or cost is prohibitive, distillation creates a viable path.

**Update (2026-08-22):** this pitch is time-limited. Nova Premier — the only teacher model in the hierarchy — is now [Legacy on Bedrock with an EOL of September 14, 2026](https://docs.aws.amazon.com/bedrock/latest/userguide/model-card-amazon-nova-premier.html), and new customers can no longer start using it at all. Teams planning a new distillation pipeline around Premier as the teacher should confirm current access before building on it; existing Provisioned Throughput and on-demand deployments created before the Legacy transition continue to work, but new ones cannot be created.

### Cross-Region Inference

Nova Pro, Lite, and Micro support automatic traffic routing across additional AWS regions via cross-region inference. If a region experiences capacity constraints, Bedrock routes requests to an available region transparently, without application changes. For latency-sensitive or availability-critical applications, this removes a significant operational concern. **Correction (2026-08-22):** the claim that Nova Premier lacks cross-region inference is outdated (and contradicted the model-lineup table above even at original publication). AWS's [Nova Premier model card](https://docs.aws.amazon.com/bedrock/latest/userguide/model-card-amazon-nova-premier.html) confirms Premier supports Geo cross-region inference from US East (N. Virginia), US East (Ohio), and US West (Oregon) to each other — it is not restricted to in-region-only access.

### Deep Bedrock Service Integration

All four models integrate with the full Bedrock surface area:
- **Bedrock Knowledge Bases**: Managed RAG with Amazon OpenSearch, Aurora, Pinecone, MongoDB Atlas, and other vector stores — no custom retrieval code needed
- **Bedrock Agents**: Multi-agent orchestration, with Nova models as orchestrators or sub-agents — native tool use, memory management, and session state
- **Bedrock Guardrails**: Content filtering, topic blocking, PII redaction, grounding checks — applied at the inference layer without custom middleware
- **Bedrock Prompt Flows**: Visual pipeline builder for chaining models, RAG lookups, Lambda functions, and conditional logic
- **Bedrock Studio**: Development environment for building and testing agent applications

Third-party models on Bedrock (Claude, Llama, Mistral) have access to some of these features, but Nova's integration is deepest — AWS tests and certifies Nova against these services continuously. Feature compatibility gaps that occasionally affect third-party models on Bedrock do not apply.

### Internal Battle-Testing

AWS's claim that Nova was "developed for Amazon's internal applications" before external release is meaningful. Amazon Ads processes billions of impressions daily and requires low-latency, high-accuracy text understanding. Amazon catalog systems need to extract structured data from unstructured product descriptions at massive scale. Alexa requires robust instruction following across diverse query types. These are harder production requirements than most AI startup benchmarks test.

The degree to which internal usage translates to external quality is impossible to verify precisely, but it likely explains Nova's speed profile. Nova Micro's output speed — [~280 tokens/second as of this update, per Artificial Analysis](https://artificialanalysis.ai/models/nova-micro) (down from the ~313 tok/s measured at original publication) — remains among the faster hosted models, an outcome consistent with systems engineering optimization for high-throughput internal workloads.

---

## Benchmarks and the Intelligence Gap

The honest picture of Nova's intelligence benchmarks is less flattering than AWS's marketing.

Amazon's official documentation claims "state-of-the-art performance on key benchmarks including TextVQA (visual question answering) and VATEX (video understanding)" for Nova Pro. Specific numbers for MMLU, MATH, HumanEval, GPQA Diamond, and similar standard benchmarks are not published in AWS's externally accessible documentation.

Third-party evaluation data from [Artificial Analysis](https://artificialanalysis.ai/models) placed Nova v1 models at original publication as shown in the "At original publication" column below. Artificial Analysis re-scores models continuously and its comparison pool has grown substantially since; **current figures (2026-08-22)**, pulled directly from each model's Artificial Analysis page, are shown alongside:

| Model | At original publication | Current (2026-08-22) | Current source |
|-------|-------------------------|-----------------------|-----------------|
| Nova Micro | 10, #68/130, median 11 | **4**, #20/32, median 6 — below average | [artificialanalysis.ai/models/nova-micro](https://artificialanalysis.ai/models/nova-micro) |
| Nova Lite | 13, #44/130, above average | **7**, #14/32, median 6 — above average | [artificialanalysis.ai/models/nova-lite](https://artificialanalysis.ai/models/nova-lite) |
| Nova Pro | 13, #56/71 non-reasoning, median 24 | **7**, #53/63, median 23 — well below median | [artificialanalysis.ai/models/nova-pro](https://artificialanalysis.ai/models/nova-pro) |
| Nova Premier | 19, #41/71 non-reasoning, below average | **13**, #43/63, median 23 — below average | [artificialanalysis.ai/models/nova-premier](https://artificialanalysis.ai/models/nova-premier) |

The raw scores dropped across the board — this reflects Artificial Analysis's evolving index and a much larger, more competitive comparison pool (32-63 models in each price class now vs. 71-130 previously), not necessarily the Nova models getting worse in absolute terms. The relative story is unchanged and, if anything, more pronounced: Nova Lite is still the standout, scoring above its price-tier median; Nova Pro is now well below median (7 vs. a median of 23, a wider gap than at original publication); Nova Premier remains below its tier median. At Nova Premier's $2.50/$12.50 pricing, Claude 3.7 Sonnet and GPT-4o scored higher in the same price bracket at original publication — Premier's imminent EOL (see update above) makes this comparison moot for new deployments regardless.

Speed compounds the Premier concern. [Artificial Analysis measures Nova Premier's output speed at ~33.7 tokens/second](https://artificialanalysis.ai/models/nova-premier) as of this update (up slightly from ~30 tok/s at original publication), against a price-tier median of ~66.6 tok/s — still "notably slow" by comparison. Slow speed plus below-median intelligence plus premium pricing plus Legacy/EOL status is a difficult combination.

The pattern suggests Nova's models were optimized primarily for AWS's internal use cases and for cost efficiency at the low end — not for maximizing performance on general-purpose reasoning tasks that standard benchmarks measure. This is not surprising: Amazon Ads and catalog systems care about structured extraction, classification, and instruction following more than open-ended reasoning. The models reflect those priorities.

---

## Nova 2: Course Correction

The Nova 2 series reads as AWS's response to the intelligence gap criticism. Nova 2 Lite's addition of extended thinking (chain-of-thought reasoning) directly addresses the primary weakness of the v1 models on reasoning tasks. Built-in web grounding removes the need for RAG setup for simple retrieval tasks. The extension of output tokens to 65,536 (from the v1 Micro/Lite/Pro cap of 5K — see correction above) addresses a real limitation of v1. Nova 2 Lite reached general availability December 2, 2025, with pricing ($0.30/$2.50 per million tokens) noticeably higher than Nova Lite v1's.

Nova 2 Pro's preview availability is harder to evaluate. AWS's positioning as "the most intelligent Nova model" with extended thinking suggests it is designed to close the gap with Claude 3.7 Sonnet and GPT-4o on reasoning benchmarks. But preview-only access through Nova Forge means independent benchmarking is limited. **Update (2026-08-22):** it is now independently benchmarked despite preview status — [Artificial Analysis scores Nova 2 Pro at 14 on its Intelligence Index (#42 of 63 models), below its price tier's median of 23](https://artificialanalysis.ai/models/nova-2-0-pro) — a modest improvement over Nova Pro v1's score of 7, but still below median for its ~$1.25/$10.00 price tier. It has not reached general availability as of this update, roughly nine months after entering preview (November 27, 2025).

Nova 2 Pro's trajectory is now overshadowed by a larger strategic shift. Reporting from Business Insider (July 28, 2026, [republished via Yahoo Finance](https://finance.yahoo.com/technology/ai/articles/amazon-winds-down-most-flagship-103406019.html)) says Amazon is winding down most of its flagship first-party Nova models — Premier, Omni, Reel, and Canvas — putting them in "keep the lights on" mode while it concentrates engineering and compute on a single new frontier model from its Frontier Model Research group, expected to debut at AWS re:Invent 2026 (autumn 2026), possibly still under the Nova name. This is corroborated independently by AWS's own Bedrock documentation, which shows Nova Premier, Nova Sonic (v1), Nova Canvas, and Nova Reel all transitioned to Legacy status in March 2026. Whether Nova 2 Pro itself reaches general availability, gets folded into the new frontier effort, or is superseded by it is unconfirmed as of this update.

---

## Architecture

Amazon has disclosed almost nothing about Nova's internal architecture. Parameter counts are not published. Transformer architecture details (attention variant, MoE vs. dense, positional encoding method) are not documented externally. Training data composition and dataset sizes are not disclosed. The company has not submitted a technical paper for Nova to arXiv or any comparable venue.

This contrasts sharply with DeepSeek (full technical papers for V3 and R1), Meta (Llama 4 technical report), Mistral (partial technical details), and Google (Gemini technical reports). Amazon's opacity is more comparable to OpenAI's closed-weight approach, but OpenAI at least publishes system cards and evaluation reports. AWS has published neither.

For organizations operating in regulated industries — finance, healthcare, defense — architectural opacity can create compliance barriers. Model cards, training data provenance, and bias evaluation results are increasingly required documentation in regulated AI deployments. Amazon's current documentation does not address these requirements at the level of detail some industries need.

---

## Practical Use Cases

**Where Nova excels:**

- **AWS-native pipelines requiring cost optimization**: Nova Micro at $0.035/M is appropriate for high-throughput classification, routing, summarization, and extraction tasks where cost-per-query matters more than state-of-the-art accuracy.

- **Video understanding workflows**: Nova Lite and Pro's ability to accept video input natively — up to 30 minutes — is a genuine differentiator for media analysis, video moderation, and multimodal RAG applications that need to reason across video content.

- **Enterprise Bedrock deployments**: Organizations already using Bedrock Agents, Knowledge Bases, and Guardrails benefit from Nova's deep integration and AWS-tested compatibility. Avoiding the operational overhead of coordinating multiple model providers has real value at scale.

- **Custom model distillation**: Production teams with stable, well-defined tasks can use Nova Premier as a teacher model to build cheaper, faster custom variants of Pro, Lite, or Micro. The managed distillation workflow lowers the engineering barrier for this approach. **Update (2026-08-22):** Premier is now Legacy with an EOL of September 14, 2026 — confirm current access before planning new work around it as teacher model (see update above).

- **Cross-region high-availability requirements**: Applications requiring 99.99%+ availability without custom routing infrastructure benefit from Nova's cross-region inference for Micro, Lite, and Pro.

**Where Nova falls short:**

- **Open-ended reasoning and analysis tasks**: If the task requires Claude 3.7 or GPT-4o class reasoning, Nova Premier v1 is not a substitute at equivalent price — and as of 2026-08-22 it is Legacy with a September 14, 2026 EOL, so it is not a sound foundation for new work regardless. Use Claude or GPT-4o through Bedrock for these workloads; Nova 2 Pro remains preview-only (see update above).

- **Long-form content generation**: The 5,000-token output cap on Nova Micro/Lite/Pro (v1) is restrictive for report generation, code generation, and document drafting; Nova Premier's cap is 25K. Nova 2 Lite's 65,536-token output addresses this for the entry tier.

- **Latency-sensitive premier workloads**: Nova Premier at ~34 tokens/second is too slow for real-time applications. Nova Micro at ~280 tokens/second makes it suitable for real-time; Premier is not — and is being retired regardless (EOL September 14, 2026).

- **Self-hosted or open-weight requirements**: Nova models are Bedrock-only. Organizations with on-premises requirements, air-gapped environments, or weight-portability requirements should use Llama 4 Scout, Qwen 3, or other open-weight models.

---

## Competitive Positioning

Amazon's entry into in-house LLMs changes its relationship with Anthropic and OpenAI. AWS remains the distribution platform for Claude and GPT-4 class models — and generates significant revenue from that distribution. But Nova creates a competing incentive: AWS profits more when customers use Nova directly than when they use Claude through Bedrock (where Anthropic captures a royalty).

At the low end, Nova Micro and Nova Lite are direct competitors to Claude Haiku and Gemini Flash for budget workloads. AWS has structural pricing advantages here: it controls the infrastructure, and can price Nova models below margin-neutral cost if customer retention on AWS justifies it.

At the high end, the competition is harder. Nova Premier v1 trails Claude 3.7 Sonnet and GPT-4o on intelligence benchmarks, and AWS customers in Bedrock can access both alternatives natively. Until Nova 2 Pro reaches general availability with verified benchmark improvements, Premier is not the recommended choice for reasoning-heavy workloads.

**Update (2026-08-22):** Amazon appears to have reached the same conclusion. Business Insider reporting (July 28, 2026, [via Yahoo Finance](https://finance.yahoo.com/technology/ai/articles/amazon-winds-down-most-flagship-103406019.html)) says Amazon is winding down Nova Premier, Omni, Reel, and Canvas — its highest-tier, most benchmark-exposed models — to concentrate on a single new frontier model from a dedicated Frontier Model Research group led by Pieter Abbeel (who joined via Amazon's Covariant acquisition), targeting a re:Invent 2026 debut; an AWS spokesperson confirmed existing models will keep getting support and migration guidance. AWS's own [Bedrock model lifecycle documentation](https://docs.aws.amazon.com/bedrock/latest/userguide/model-lifecycle.html) independently corroborates the Premier and Sonic (v1) Legacy transitions (March 13, 2026) and Canvas/Reel Legacy transitions (March 30, 2026). Read together, Amazon's high end of Nova was not just underperforming on benchmarks — the company has decided not to keep iterating on it as a first-party flagship, at least until whatever ships at re:Invent 2026.

The strategic bet at the low end is on integration lock-in: if an organization's AI pipelines are deeply embedded in Bedrock Knowledge Bases, Bedrock Agents, and Bedrock Guardrails, switching the underlying model to a non-Nova option introduces compatibility risk. The deeper the Bedrock integration, the stronger Nova's retention advantage — regardless of raw benchmark performance. That bet still stands for Micro, Lite, and (for now) Nova 2 Lite; it does not for Premier.

---

## Limitations Summary

1. **Intelligence below median for price tier** (v1 Pro and Premier, and Nova 2 Pro preview): Third-party benchmarks (Artificial Analysis, current as of 2026-08-22) show Nova Pro at 7 vs. a price-tier median of 23, Nova Premier at 13 vs. median 23, and Nova 2 Pro preview at 14 vs. median 23 — all below median. Nova 2 Lite is the exception, scoring at/above its (lower) price tier's median.

2. **Output token caps**: Nova Micro, Lite, and Pro (v1) cap at 5,000 output tokens; Nova Premier caps at 25,000. Both are restrictive for long-form generation, multi-step reasoning, and complex code generation compared to Nova 2 Lite's 65,536-token cap.

3. **Nova Premier is now Legacy, EOL September 14, 2026**: [Confirmed on AWS's Bedrock model lifecycle page](https://docs.aws.amazon.com/bedrock/latest/userguide/model-lifecycle.html) as of 2026-08-22 — new customers cannot start using it, and existing users must migrate before EOL. No fine-tuning, no new Provisioned Throughput. Available in US East (N. Virginia) in-region with Geo cross-region to US East (Ohio) and US West (Oregon).

4. **Nova Premier is slow**: ~34 tokens/second against a ~66.6 tok/s price-tier median (Artificial Analysis, 2026-08-22). Not suitable for real-time applications — and moot for new deployments given its EOL date.

5. **Architecture opacity**: No parameter counts, training data details, or technical papers published. Limits suitability for regulated industry deployments that require model documentation.

6. **Bedrock-only**: No open weights, no self-hosting. AWS vendor dependency is absolute. If Bedrock pricing changes or service disrupts, there is no migration path that preserves the model.

7. **No native image/audio generation from understanding models**: Nova understanding models output text only. Multimodal output requires separate Nova Canvas (images) or Nova Reel (video) model calls — both of which are also now Legacy, with an EOL of September 30, 2026, per the same [AWS lifecycle page](https://docs.aws.amazon.com/bedrock/latest/userguide/model-lifecycle.html).

8. **Amazon is de-prioritizing the high end of first-party Nova**: Reporting from Business Insider (July 28, 2026, [via Yahoo Finance](https://finance.yahoo.com/technology/ai/articles/amazon-winds-down-most-flagship-103406019.html)), corroborated by the Legacy transitions above, indicates Amazon is winding down Premier, Omni, Reel, and Canvas to focus engineering and compute on a new frontier model expected at re:Invent 2026. Organizations building on Premier-tier Nova today should plan for migration regardless of benchmark performance.

---

## The Amazon Nova Assessment

Amazon Nova is a well-integrated, aggressively priced, and honestly differentiated set of models — as long as you understand what you are buying.

Nova Micro and Nova Lite are genuinely excellent for high-throughput budget workloads. At $0.035/M and $0.06/M respectively, they undercut every major competitor at their tier, run fast, and integrate natively with Bedrock's full service surface. For AWS organizations doing classification, extraction, routing, and lightweight generation at scale, these two models represent the best price-performance ratio in the Bedrock catalog.

Nova Pro is harder to recommend on general-purpose grounds — its intelligence score sits well below the median for its price tier, and the alternatives (Claude 3.7 Sonnet, GPT-4o) are available through the same Bedrock console. **Nova Premier is no longer a forward-looking recommendation at all**: as of 2026-08-22 it is Legacy on Bedrock with a September 14, 2026 EOL, and reporting indicates Amazon is deliberately winding it down rather than continuing to invest in it (see updates above). Any organization currently relying on Premier — including for the distillation-teacher use case this review originally highlighted — should be actively planning migration, not building new dependencies on it.

Nova 2 Lite's capability jump — extended thinking, web grounding, code interpreter, 65K output, 1M context — suggests Amazon knows what needs fixing at the mid tier, and it reached general availability December 2, 2025. Nova 2 Pro remains preview-only nine months after its November 2025 debut, scores below its price tier's median on current third-party benchmarks, and its future is now entangled with Amazon's broader pivot toward a single new frontier model expected at re:Invent 2026. Whether that model ships as "Nova" or something else is unconfirmed.

The honest answer, updated: Amazon Nova is still the right choice for an AWS-native organization running at scale that wants budget inference (Micro, Lite, or the pricier-but-more-capable Nova 2 Lite) and deep Bedrock integration. It is **not** the right choice for anyone evaluating Nova Premier for new work, or for an organization optimizing purely for reasoning quality at the premier tier — Claude and GPT-4o remain better tools available in the same service, and Amazon's own roadmap decisions now agree.

**Rating: 3.5/5** — Best-in-class pricing and AWS integration depth at the low end (Micro, Lite) remains true and is this review's most durable finding. The high end has changed materially since original publication: Nova Premier is now Legacy with a September 14, 2026 EOL, and Amazon is reportedly winding down its first-party flagship models in favor of a still-unreleased frontier model. Readers evaluating Nova today should treat everything above Nova Pro as a moving target.

