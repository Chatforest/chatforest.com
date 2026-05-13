# Amazon Nova LLM Review — AWS-Native AI with Best-in-Class Pricing and Deep Bedrock Integration

> Amazon Nova (launched December 2024, Nova Premier April 2025) is AWS's in-house LLM family: four text and multimodal models from $0.035/M tokens (Micro) to $2.50/M (Premier). Deep Bedrock integration, native video understanding, and model distillation pipelines. Intelligence scores below median for price tier. Rating: 3.5/5.


Amazon's AI strategy has long looked like a distribution play more than a research bet. AWS hosts Claude via Anthropic's partnership, GPT-4o through Azure's equivalent arrangement, and Llama 4 through Meta's open-weight releases. For years, the implicit message was that AWS customers could access any frontier model — as long as they stayed in the cloud. Amazon was the platform, not the lab.

That posture shifted at AWS re:Invent 2024, when Amazon launched **Amazon Nova**: four in-house language models trained on infrastructure that powers Alexa, Amazon.com search, Amazon Ads, and AWS Marketplace catalog systems. Nova was not a research announcement. It was a product launch backed by years of internal deployment and accompanied by pricing that undercut every comparable model at the time.

The question Nova raises is not whether Amazon can build competitive models. The question is whether Nova's integration depth with AWS compensates for intelligence benchmarks that trail the frontier. This review examines both sides.

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

**Amazon Nova Micro** is the text-only entry point. 128K context window. No image, video, or document input. At $0.035 per million input tokens and $0.14 per million output tokens, it was the cheapest model from any major provider at launch. Compared to Gemini 1.5 Flash-8B ($0.0375 input) or Claude Haiku ($0.25 input), Nova Micro's pricing is aggressive. Speed: approximately 313 tokens per second by third-party measurement, ranking among the top five fastest models globally.

**Amazon Nova Lite** adds multimodal input: text, images, and up to 30 minutes of video per call. 300K context window. At $0.06 per million input tokens and $0.24 output, it was cheaper than Gemini 1.5 Flash at launch. Video understanding was a genuine differentiator at the time — OpenAI and Anthropic models on Bedrock did not natively accept video input.

**Amazon Nova Pro** is the full-featured mid-range model. 300K context. Text, image, and video input. $0.80 per million input tokens and $3.20 output. Supports supervised fine-tuning and can serve as a student in model distillation pipelines (see below). Speed is adequate for production workloads.

**Amazon Nova Premier** is the flagship, released for general availability on April 30, 2025 — five months after the initial Nova launch. 1M context window. Text, image, and video input. $2.50 per million input tokens and $12.50 output. The pricing places it in the Claude 3.7 Sonnet / GPT-4o tier. Unlike the other v1 models, Premier does **not** support fine-tuning or provisioned throughput — it is the teacher model for distillation, not the student. Available only in US East (N. Virginia) without cross-region inference.

| Model | Context | Modalities In | Input Price | Output Price | Speed |
|-------|---------|--------------|-------------|--------------|-------|
| Nova Micro | 128K | Text | $0.035/M | $0.14/M | ~313 tok/s |
| Nova Lite | 300K | Text, Image, Video | $0.06/M | $0.24/M | ~170 tok/s |
| Nova Pro | 300K | Text, Image, Video | $0.80/M | $3.20/M | N/A |
| Nova Premier | 1M | Text, Image, Video | $2.50/M | $12.50/M | ~30 tok/s |

All v1 models have a maximum output of 10,000 tokens per request. Prompt caching reduces input costs by 75%.

### Nova v2 (2025 – Present)

Amazon has extended the Nova family with several new models in 2025 that address gaps in the v1 lineup:

**Nova 2 Lite** adds extended thinking (chain-of-thought reasoning with three intensity levels), built-in web grounding (real-time web access without RAG setup), a built-in code interpreter (Python execution), remote MCP tool support, and reinforcement fine-tuning in addition to standard supervised fine-tuning. Context extended to 1M tokens. Output extended to 65,536 tokens (6.5× the v1 cap). This is a substantial capability upgrade over Nova Lite v1.

**Nova 2 Sonic** is a speech-to-speech model with 7 languages and 1M context, supporting bidirectional streaming for low-latency voice applications.

**Nova 2 Pro** is positioned as the most capable Nova model with extended thinking, but as of May 2025 is only available in preview to Nova Forge subscribers — not generally accessible.

**Nova Forge** is a service allowing customers to train fully custom frontier models using Amazon's own training infrastructure, not just fine-tuning. Annual subscription pricing. Represents Amazon's highest-tier AI offering for enterprises wanting proprietary model differentiation.

---

## The AWS-Native Advantage

Nova's primary value proposition is not raw benchmark performance — it is integration depth with the AWS ecosystem. For organizations already running workloads on AWS, Nova offers capabilities that third-party models on Bedrock do not:

### Model Distillation Pipelines

Nova's distillation hierarchy is a genuine differentiator. Nova Premier can act as a teacher model: AWS generates synthetic training data using Premier's outputs, which is then used to fine-tune Pro, Lite, or Micro with the customer's use case. The result is a smaller, cheaper, faster custom model that preserves much of Premier's task-specific quality.

This is not standard fine-tuning — it is knowledge distillation, using the large model's distribution to improve a smaller model. AWS has built this into the Bedrock console with a managed workflow. For high-volume production tasks where Premier's quality matters but Premier's latency or cost is prohibitive, distillation creates a viable path.

### Cross-Region Inference

Nova Pro, Lite, and Micro support automatic traffic routing across 11 AWS regions. If a region experiences capacity constraints, Bedrock routes requests to an available region transparently, without application changes. For latency-sensitive or availability-critical applications, this removes a significant operational concern. Nova Premier is currently restricted to US East (N. Virginia) only — cross-region is not yet available.

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

The degree to which internal usage translates to external quality is impossible to verify precisely, but it likely explains Nova's speed profile. Nova Micro's 313 tokens/second is among the fastest of any hosted model — an outcome consistent with systems engineering optimization for high-throughput internal workloads.

---

## Benchmarks and the Intelligence Gap

The honest picture of Nova's intelligence benchmarks is less flattering than AWS's marketing.

Amazon's official documentation claims "state-of-the-art performance on key benchmarks including TextVQA (visual question answering) and VATEX (video understanding)" for Nova Pro. Specific numbers for MMLU, MATH, HumanEval, GPQA Diamond, and similar standard benchmarks are not published in AWS's externally accessible documentation.

Third-party evaluation data from Artificial Analysis, which tracks 130+ models across intelligence, speed, and price, places Nova v1 models:

| Model | Intelligence Score (/130 scale) | Rank | vs. Price-Tier Median |
|-------|--------------------------------|------|----------------------|
| Nova Micro | 10 | #68 of 130 | Below median (median: 11) |
| Nova Lite | 13 | #44 of 130 | Above average |
| Nova Pro | 13 | #56 of 71 non-reasoning | Below median (median: 24) |
| Nova Premier | 19 | #41 of 71 non-reasoning | Below average, somewhat expensive |

Nova Lite is the relative standout — for $0.06/M input, a score of 13 represents good value. Nova Pro and Nova Premier are the concern: both score below the median for non-reasoning models in their price tier. At Nova Premier's $2.50/$12.50 pricing, Claude 3.7 Sonnet ($3.00/$15.00) and GPT-4o ($2.50/$10.00) score substantially higher in the same price bracket.

Speed compounds the Premier concern. At approximately 30 tokens per second, Nova Premier is "notably slow" by Artificial Analysis categorization — in the bottom quartile of 71 non-reasoning models. Slow speed plus below-median intelligence plus premium pricing is a difficult combination.

The pattern suggests Nova's models were optimized primarily for AWS's internal use cases and for cost efficiency at the low end — not for maximizing performance on general-purpose reasoning tasks that standard benchmarks measure. This is not surprising: Amazon Ads and catalog systems care about structured extraction, classification, and instruction following more than open-ended reasoning. The models reflect those priorities.

---

## Nova 2: Course Correction

The Nova 2 series reads as AWS's response to the intelligence gap criticism. Nova 2 Lite's addition of extended thinking (chain-of-thought reasoning) directly addresses the primary weakness of the v1 models on reasoning tasks. Built-in web grounding removes the need for RAG setup for simple retrieval tasks. The extension of output tokens to 65,536 (from 10,000) addresses a real limitation of v1.

Nova 2 Pro's preview availability is harder to evaluate. AWS's positioning as "the most intelligent Nova model" with extended thinking suggests it is designed to close the gap with Claude 3.7 Sonnet and GPT-4o on reasoning benchmarks. But preview-only access through Nova Forge means independent benchmarking is limited, and the general availability timeline is not confirmed.

If Nova 2 Pro reaches performance comparable to Claude 3.7 Sonnet or GPT-4.1 at competitive pricing, the calculus for AWS-native organizations changes substantially. Based on Nova 2 Lite's capabilities upgrade, the trajectory is plausible. As of May 2025, it is unverified.

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

- **Custom model distillation**: Production teams with stable, well-defined tasks can use Nova Premier as a teacher model to build cheaper, faster custom variants of Pro, Lite, or Micro. The managed distillation workflow lowers the engineering barrier for this approach.

- **Cross-region high-availability requirements**: Applications requiring 99.99%+ availability without custom routing infrastructure benefit from Nova's cross-region inference for Micro, Lite, and Pro.

**Where Nova falls short:**

- **Open-ended reasoning and analysis tasks**: If the task requires Claude 3.7 or GPT-4o class reasoning, Nova Premier v1 is not a substitute at equivalent price. Use Claude or GPT-4o through Bedrock for these workloads until Nova 2 Pro reaches general availability.

- **Long-form content generation**: The 10,000-token output cap on v1 models is restrictive for report generation, code generation, and document drafting. Nova 2 Lite's 65,536-token output addresses this, but v1 Nova Pro and Premier users hit this ceiling.

- **Latency-sensitive premier workloads**: Nova Premier at 30 tokens/second is too slow for real-time applications. Nova Micro's 313 tokens/second makes it suitable for real-time; Premier is not.

- **Self-hosted or open-weight requirements**: Nova models are Bedrock-only. Organizations with on-premises requirements, air-gapped environments, or weight-portability requirements should use Llama 4 Scout, Qwen 3, or other open-weight models.

---

## Competitive Positioning

Amazon's entry into in-house LLMs changes its relationship with Anthropic and OpenAI. AWS remains the distribution platform for Claude and GPT-4 class models — and generates significant revenue from that distribution. But Nova creates a competing incentive: AWS profits more when customers use Nova directly than when they use Claude through Bedrock (where Anthropic captures a royalty).

At the low end, Nova Micro and Nova Lite are direct competitors to Claude Haiku and Gemini Flash for budget workloads. AWS has structural pricing advantages here: it controls the infrastructure, and can price Nova models below margin-neutral cost if customer retention on AWS justifies it.

At the high end, the competition is harder. Nova Premier v1 trails Claude 3.7 Sonnet and GPT-4o on intelligence benchmarks, and AWS customers in Bedrock can access both alternatives natively. Until Nova 2 Pro reaches general availability with verified benchmark improvements, Premier is not the recommended choice for reasoning-heavy workloads.

The strategic bet is on integration lock-in: if an organization's AI pipelines are deeply embedded in Bedrock Knowledge Bases, Bedrock Agents, and Bedrock Guardrails, switching the underlying model to a non-Nova option introduces compatibility risk. The deeper the Bedrock integration, the stronger Nova's retention advantage — regardless of raw benchmark performance.

---

## Limitations Summary

1. **Intelligence below median for price tier** (v1 Pro and Premier): Third-party benchmarks show both models underperforming vs. alternatives at comparable price points. Nova 2 is the course correction, but Premier-class reasoning from Nova 2 is not yet generally available.

2. **10,000-token output cap (v1)**: Restrictive for long-form generation, multi-step reasoning, and complex code generation. Nova 2 Lite addresses this at 65,536 tokens; v1 Pro and Premier do not.

3. **Nova Premier availability**: US East (N. Virginia) only. No cross-region inference. No fine-tuning. Limited to API access.

4. **Nova Premier is slow**: 30 tokens/second places it in the bottom quartile across 71 non-reasoning models. Not suitable for real-time applications.

5. **Architecture opacity**: No parameter counts, training data details, or technical papers published. Limits suitability for regulated industry deployments that require model documentation.

6. **Bedrock-only**: No open weights, no self-hosting. AWS vendor dependency is absolute. If Bedrock pricing changes or service disrupts, there is no migration path that preserves the model.

7. **No native image/audio generation from understanding models**: Nova understanding models output text only. Multimodal output requires separate Nova Canvas (images) or Nova Reel (video) model calls.

---

## The Amazon Nova Assessment

Amazon Nova is a well-integrated, aggressively priced, and honestly differentiated set of models — as long as you understand what you are buying.

Nova Micro and Nova Lite are genuinely excellent for high-throughput budget workloads. At $0.035/M and $0.06/M respectively, they undercut every major competitor at their tier, run fast, and integrate natively with Bedrock's full service surface. For AWS organizations doing classification, extraction, routing, and lightweight generation at scale, these two models represent the best price-performance ratio in the Bedrock catalog.

Nova Pro and Premier v1 are harder to recommend on general-purpose grounds. The intelligence scores fall below the median for their price tiers, and the alternatives — Claude 3.7 Sonnet, GPT-4o — are available through the same Bedrock console. The case for Pro and Premier is specifically the distillation pipeline, the cross-region availability (Pro), and the integration depth that comes from AWS certification.

Nova 2 Lite's capability jump — extended thinking, web grounding, code interpreter, 65K output, 1M context — suggests Amazon knows what needs fixing and is fixing it. Nova 2 Pro in preview could change the picture at the top end. The trajectory is improving.

The honest answer is that Amazon Nova is the right choice for an AWS-native organization running at scale that wants budget inference (Micro/Lite), deep Bedrock integration, or model distillation pipelines. It is not the right choice for an organization optimizing purely for reasoning quality at the premier tier, where Claude and GPT-4o are better tools available in the same service.

**Rating: 3.5/5** — Best-in-class pricing and AWS integration depth at the low end. Intelligence scores below the frontier at the high end. Nova 2 is improving this, but general availability of the reasoning tier is pending.

