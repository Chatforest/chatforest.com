# Grok 4.3 on Amazon Bedrock: What Changes for Builders on AWS

> xAI's Grok 4.3 is now available on Amazon Bedrock via the Mantle inference engine. Model ID: xai.grok-4.3. Pricing: $1.25/$2.50/M. Configurable reasoning, 1M context, OpenAI-compatible API. Here's what changes if you're building on AWS.


**At a glance:** Grok 4.3 became available on Amazon Bedrock on June 15, 2026. Model ID: `xai.grok-4.3`. Runs on Mantle, a new AWS inference engine. OpenAI-compatible API. 1M token context, 30K max output. Configurable reasoning (none/low/medium/high). Pricing: $1.25/M input, $2.50/M output, $0.20/M cached. xAI's first model on Bedrock. For the model itself, see the **[Grok 4.3 review](/reviews/xai-grok-4-3-native-video-agentic-llm-review/)**.

---

On June 15, 2026, AWS announced that xAI's Grok 4.3 is now available on Amazon Bedrock. This is xAI's first Bedrock integration — previously, Grok was accessible only through xAI's own API. Bedrock availability changes the calculus for builders already running workloads on AWS: IAM-based access, Bedrock's audit trails, and a familiar SDK surface, with no new vendor relationship to manage.

This article focuses on what that integration means practically: how you access the model, what the new Mantle engine is, and where Grok 4.3 on Bedrock fits versus other options.

---

## What Is Mantle

Grok 4.3 on Bedrock runs on Mantle, a new inference engine that AWS built specifically for price-performance workloads. Mantle is not a rebranded version of an existing Bedrock path — it sits alongside the existing foundation model inference stack as a separate runtime optimized for high-throughput, cost-sensitive inference.

Mantle supports:
- Tool calling (function calling in OpenAI parlance)
- Structured output (JSON mode)
- Response streaming

The endpoint for Mantle-based access is `https://bedrock-mantle.us-west-2.api.aws/openai/v1/responses`. This is an OpenAI-compatible endpoint, which means existing code that calls OpenAI's responses API can switch to Grok 4.3 on Bedrock by changing the base URL and model ID — no SDK swap required.

AWS positions Mantle as the Bedrock path for builders who care more about cost per token at volume than about millisecond latency optimization. The "price performance" framing is consistent with the type of workloads Grok 4.3 is being pitched for: customer support, document processing, and other high-volume batch tasks where throughput and cost matter more than time-to-first-token.

---

## Access and Model ID

To call Grok 4.3 through Bedrock:

**Model ID:** `xai.grok-4.3`

**Endpoint (OpenAI-compatible):**
```
https://bedrock-mantle.us-west-2.api.aws/openai/v1/responses
```

Authentication uses your standard AWS credentials — IAM roles, access keys, or instance profiles, depending on your environment. If you're already on Bedrock for other models, the access pattern is familiar. If you're new to Bedrock, AWS has standard documentation for setting up Bedrock access with your account.

The OpenAI-compatible surface means you can use the `openai` Python SDK by setting `base_url` to the Mantle endpoint and passing `model="xai.grok-4.3"`. AWS credential signing is handled automatically when you're within an AWS environment.

---

## Configurable Reasoning Effort

Grok 4.3's most builder-relevant architectural feature carries through to the Bedrock integration: reasoning effort is configurable at request time.

| Setting | Behavior |
|---|---|
| `none` | No chain-of-thought; fastest response, lowest token cost |
| `low` | Minimal reasoning pass; useful for classification, simple extraction |
| `medium` | Balanced; suitable for most agentic steps |
| `high` | Full reasoning; use for complex multi-step problems |

This is a different model than Grok 4.3's default API behavior, where reasoning is always on. On Bedrock via Mantle, the effort setting is explicitly configurable, which matters for cost-sensitive workloads: a high-volume extraction task at `none` costs significantly less than the same task with `high` reasoning enabled.

The practical implication: you can build a single pipeline that calls `xai.grok-4.3` with different reasoning levels depending on task complexity, rather than maintaining two different model endpoints.

---

## Pricing

| Token type | Price |
|---|---|
| Input | $1.25 per million tokens |
| Output | $2.50 per million tokens |
| Cached input | $0.20 per million tokens |

These match the prices on xAI's direct API, which makes sense — Bedrock's margin comes from the managed infrastructure, not from a markup on the model. The cached input rate ($0.20/M) is significant: at 1M context, caching a large document or codebase and making multiple queries against it brings the effective input cost down substantially.

For comparison: Claude Sonnet 4.6 on Bedrock is $3.00/$15.00/M (standard) — higher input, significantly higher output. GPT-5.4 on Azure/OpenAI runs around $2.50/$10.00/M for standard access (higher output rate). Grok 4.3's $2.50/M output is competitive for frontier-class reasoning models.

---

## What Grok 4.3 on Bedrock Is Good At

AWS's announced use cases align with what the model benchmarks show:

**Customer support:** The lowest hallucination rate claim among frontier models — which AWS highlights in the Mantle announcement — matters more in customer-facing contexts than in internal tools. A model that consistently retrieves accurately is more valuable in a support context than one that scores higher on reasoning benchmarks but hallucinates policy details.

**Case law and financial document Q&A:** The 1M token context handles large document sets without chunking strategies. Legal briefs, financial filings, and policy documents can often be passed in full — reducing the complexity of retrieval pipelines.

**Web development:** xAI has benchmarked Grok 4.3 on front-end tasks (HTML/CSS generation, JavaScript debugging). The structured output support on Mantle makes it easier to extract machine-readable outputs from UI code generation.

**High-volume enterprise batch work:** Mantle's price-performance positioning is the thread connecting all of these. If you are running thousands of document extractions per day, the cost profile matters more than which frontier benchmark a model tops.

---

## What Is Not Covered by the Bedrock Integration

The Bedrock integration does not include:

- **Native video input** — Grok 4.3's video understanding capability (up to 5 minutes, 1080p) is not exposed through the Mantle endpoint. Video input requires xAI's direct API.
- **Custom Voices API** — Grok 4.3's voice cloning feature is xAI-direct only.
- **Real-time search / X data** — Grok's live web and X platform search grounding is not available through Bedrock.

If your use case depends on video input or real-time X data, the xAI direct API is the path. The Bedrock integration targets document, text, and structured data workloads where those modalities are not needed.

---

## How This Fits the xAI Distribution Picture

The Bedrock launch is the clearest signal yet that xAI is pursuing enterprise distribution seriously. The direct API targets developers. Grok on X and SuperGrok targets consumers. Bedrock targets enterprises already committed to AWS who want a managed, IAM-integrated model option without a separate vendor relationship.

This is the same distribution strategy Anthropic has used successfully with Bedrock for Claude, and that Google is pursuing for Gemini via Vertex AI. The winner in enterprise AI distribution is increasingly not the model that wins the benchmark table but the one that is easiest to procure, audit, and integrate within existing cloud contracts.

For builders on AWS: Grok 4.3 on Bedrock is now a real option. The OpenAI-compatible API, configurable reasoning, and Bedrock-standard IAM access lower the switching cost enough to be worth evaluating on your specific workload — particularly if output volume and token cost are constraints.

---

*Grok 4.3 is xAI's current production model (API release: April 30, 2026). For the full model review, see **[Grok 4.3: Native Video, Always-On Reasoning, 40% Price Cut](/reviews/xai-grok-4-3-native-video-agentic-llm-review/)**. For xAI's API access path, see **[xAI Grok API review](/reviews/xai-grok-api-llm-inference/)**.*

