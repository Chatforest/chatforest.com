# Grok 4.3 on Amazon Bedrock: What Changes for Builders on AWS

> xAI's Grok 4.3 is now available on Amazon Bedrock via the Mantle inference engine. Model ID: xai.grok-4.3. Pricing: $1.25/$2.50/M. Configurable reasoning, 1M context, OpenAI-compatible API. Here's what changes if you're building on AWS.


**At a glance:** Grok 4.3 [became available on Amazon Bedrock on June 15, 2026](https://aws.amazon.com/about-aws/whats-new/2026/06/grok-amazon-bedrock/). Model ID: [`xai.grok-4.3`](https://docs.aws.amazon.com/bedrock/latest/userguide/model-card-xai-grok-4-3.html). Runs on [Mantle, a new inference engine in Amazon Bedrock](https://aws.amazon.com/blogs/machine-learning/introducing-grok-on-amazon-bedrock/) designed for price-performance. OpenAI-compatible API. 1M token context, [131,072 max output tokens by default](https://docs.aws.amazon.com/bedrock/latest/userguide/model-card-xai-grok-4-3.html). Configurable reasoning (none/low/medium/high). [Pricing: $1.25/M input, $2.50/M output, $0.20/M cached](https://aws.amazon.com/bedrock/pricing/). [xAI's first model on Bedrock](https://aws.amazon.com/about-aws/whats-new/2026/06/grok-amazon-bedrock/). For the model itself, see the **[Grok 4.3 review](/reviews/xai-grok-4-3-native-video-agentic-llm-review/)**.

---

On [June 15, 2026, AWS announced that xAI's Grok 4.3 is now available on Amazon Bedrock](https://aws.amazon.com/about-aws/whats-new/2026/06/grok-amazon-bedrock/). This is xAI's first Bedrock integration — the announcement notes ["xAI joins Amazon Bedrock as a model provider"](https://aws.amazon.com/about-aws/whats-new/2026/06/grok-amazon-bedrock/) for the first time; previously, Grok was accessible only through xAI's own API. Bedrock availability changes the calculus for builders already running workloads on AWS: IAM-based access, Bedrock's audit trails, and a familiar SDK surface, with no new vendor relationship to manage.

This article focuses on what that integration means practically: how you access the model, what the new Mantle engine is, and where Grok 4.3 on Bedrock fits versus other options.

---

## What Is Mantle

Grok 4.3 on Bedrock runs on [Mantle, a new inference engine in Amazon Bedrock designed for price performance](https://aws.amazon.com/blogs/machine-learning/introducing-grok-on-amazon-bedrock/). Mantle is not a rebranded version of an existing Bedrock path — [AWS documents it as a distinct endpoint (`bedrock-mantle`) from the standard Bedrock Runtime API](https://docs.aws.amazon.com/bedrock/latest/userguide/model-card-xai-grok-4-3.html), sitting alongside the existing foundation model inference stack as a separate runtime.

Mantle [supports](https://aws.amazon.com/about-aws/whats-new/2026/06/grok-amazon-bedrock/):
- Tool calling (function calling in OpenAI parlance)
- Structured output (JSON mode)
- Response streaming

The endpoint for Mantle-based access is [`https://bedrock-mantle.us-west-2.api.aws/openai/v1`](https://docs.aws.amazon.com/bedrock/latest/userguide/model-card-xai-grok-4-3.html), with the Responses API specifically served on the `openai/v1/responses` path. This is an OpenAI-compatible endpoint, which means existing code that calls OpenAI's responses API can switch to Grok 4.3 on Bedrock by changing the base URL and model ID — no SDK swap required.

AWS positions Mantle as the Bedrock path for builders who care more about cost per token at volume than about millisecond latency optimization. The "price performance" framing is consistent with the type of workloads Grok 4.3 is being pitched for: [customer support, web development, case law research, and financial document Q&A](https://aws.amazon.com/about-aws/whats-new/2026/06/grok-amazon-bedrock/) — high-volume tasks where throughput and cost matter more than time-to-first-token.

---

## Access and Model ID

To call Grok 4.3 through Bedrock:

**Model ID:** [`xai.grok-4.3`](https://docs.aws.amazon.com/bedrock/latest/userguide/model-card-xai-grok-4-3.html)

**Endpoint (OpenAI-compatible):**
```
https://bedrock-mantle.us-west-2.api.aws/openai/v1
```
Per [AWS's programmatic access documentation](https://docs.aws.amazon.com/bedrock/latest/userguide/model-card-xai-grok-4-3.html), swap `us-west-2` for another supported region as needed; in-Region inference is currently available in us-west-2, us-east-1, and us-east-2.

Authentication uses your standard AWS credentials — IAM roles, access keys, or instance profiles, depending on your environment. If you're already on Bedrock for other models, the access pattern is familiar. If you're new to Bedrock, AWS has standard documentation for setting up Bedrock access with your account.

The OpenAI-compatible surface means you can use the `openai` Python SDK by setting `base_url` to the Mantle endpoint and passing `model="xai.grok-4.3"`, per [AWS's sample code](https://docs.aws.amazon.com/bedrock/latest/userguide/model-card-xai-grok-4-3.html). AWS credential signing is handled automatically when you're within an AWS environment.

---

## Configurable Reasoning Effort

Grok 4.3's most builder-relevant architectural feature carries through to the Bedrock integration: [reasoning effort is configurable at request time via the `reasoning` parameter](https://docs.aws.amazon.com/bedrock/latest/userguide/model-card-xai-grok-4-3.html).

| Setting | Behavior |
|---|---|
| `none` | No chain-of-thought; fastest response, lowest token cost |
| `low` | Minimal reasoning pass (Bedrock default); useful for classification, simple extraction |
| `medium` | Balanced; suitable for most agentic steps |
| `high` | Full reasoning; use for complex multi-step problems |

Grok 4.3 is architecturally a reasoning-first model — [AWS's model card describes it as offering "always-on and configurable reasoning effort," noting the model "behaves more consistently across multi-step agent loops than models that can skip thinking"](https://docs.aws.amazon.com/bedrock/latest/userguide/model-card-xai-grok-4-3.html). On Bedrock via Mantle, that reasoning can nonetheless be turned off entirely by setting `effort` to `none`, which matters for cost-sensitive workloads: a high-volume extraction task at `none` costs significantly less than the same task with `high` reasoning enabled.

The practical implication: you can build a single pipeline that calls `xai.grok-4.3` with different reasoning levels depending on task complexity, rather than maintaining two different model endpoints.

---

## Pricing

| Token type | Price |
|---|---|
| Input | [$1.25 per million tokens](https://aws.amazon.com/bedrock/pricing/) |
| Output | [$2.50 per million tokens](https://aws.amazon.com/bedrock/pricing/) |
| Cached input | [$0.20 per million tokens](https://aws.amazon.com/bedrock/pricing/) |

These [match the standard-tier prices on xAI's direct API](https://docs.x.ai/developers/models/grok-4.3) (for prompts under 200K tokens — xAI's direct API doubles the rate above that threshold), which makes sense — Bedrock's margin comes from the managed infrastructure, not from a markup on the model. The cached input rate ($0.20/M) is significant: at 1M context, caching a large document or codebase and making multiple queries against it brings the effective input cost down substantially.

For comparison: [Claude Sonnet 4.6 on Bedrock is $3.00/$15.00/M](https://aws.amazon.com/bedrock/pricing/) (standard on-demand) — higher input, significantly higher output. [GPT-5.4 is $2.50/$15.00/M](https://developers.openai.com/api/docs/models/gpt-5.4) for standard access — same input rate as Grok 4.3, but double the output rate. Grok 4.3's $2.50/M output is competitive for frontier-class reasoning models.

---

## What Grok 4.3 on Bedrock Is Good At

[AWS's launch announcement names four use cases](https://aws.amazon.com/about-aws/whats-new/2026/06/grok-amazon-bedrock/) — "customer support, web development, case law research, and financial document Q&A":

**Customer support:** xAI's own claim, [reported in AWS's Bedrock blog post, is that "Grok 4.3 ranked #1 on the Artificial Analysis Omniscience benchmark with the lowest hallucination rate among the frontier models it compared"](https://aws.amazon.com/blogs/machine-learning/introducing-grok-on-amazon-bedrock/). That framing matters more in customer-facing contexts than in internal tools — a model that consistently retrieves accurately is more valuable in a support context than one that scores higher on reasoning benchmarks but hallucinates policy details. Worth noting: our own [Grok 4.3 review](/reviews/xai-grok-4-3-native-video-agentic-llm-review/) found Grok 4.3 actually regressed on Artificial Analysis's Omniscience score relative to its predecessor, Grok 4.20 — so treat the "#1 among frontier models" framing as xAI/AWS's own comparison set, not an unqualified record.

**Case law and financial document Q&A:** [AWS's model card lists case law research, credit agreement analysis, and financial document Q&A as target enterprise workloads](https://docs.aws.amazon.com/bedrock/latest/userguide/model-card-xai-grok-4-3.html), and the 1M token context handles large document sets without chunking strategies. Legal briefs, financial filings, and policy documents can often be passed in full — reducing the complexity of retrieval pipelines.

**Web development:** AWS's announcement names web development as a target workload, alongside customer support and document Q&A. The structured output support on Mantle makes it easier to extract machine-readable outputs from generated code, though neither AWS nor xAI has published a specific front-end coding benchmark for the Bedrock integration.

**High-volume enterprise batch work:** Mantle's price-performance positioning is the thread connecting all of these. If you are running thousands of document extractions per day, the cost profile matters more than which frontier benchmark a model tops.

---

## What Is Not Covered by the Bedrock Integration

The Bedrock integration does not include:

- **Native video input** — [AWS's model card lists Video as unsupported for both input and output modalities on the `xai.grok-4.3` Bedrock listing](https://docs.aws.amazon.com/bedrock/latest/userguide/model-card-xai-grok-4-3.html). Video input requires xAI's direct API.
- **Custom Voices API** — Grok's [Custom Voices voice-cloning feature](https://docs.x.ai/developers/model-capabilities/audio/custom-voices) is served from `api.x.ai`, xAI's direct API; the Bedrock model card lists Speech/Audio as unsupported on both input and output, so it is not reachable through Mantle.
- **Real-time search / X data** — [xAI's X Search and Web Search tools](https://docs.x.ai/developers/tools/x-search) are documented as features of the xAI API surface; they are not listed among the capabilities (tool calling, structured output, streaming) that AWS documents for the `bedrock-mantle` endpoint.

If your use case depends on video input, voice cloning, or real-time X data, the xAI direct API is the path. The Bedrock integration targets document, text, and structured data workloads where those modalities are not needed.

---

## How This Fits the xAI Distribution Picture

The Bedrock launch is the clearest signal yet that xAI is pursuing enterprise distribution seriously. The direct API targets developers. Grok on X and SuperGrok targets consumers. Bedrock targets enterprises already committed to AWS who want a managed, IAM-integrated model option without a separate vendor relationship.

This is the same distribution strategy [Anthropic has used with Bedrock for Claude](https://aws.amazon.com/bedrock/anthropic/), and that [Google has pursued for Gemini via Vertex AI](https://cloud.google.com/blog/products/ai-machine-learning/gemini-support-on-vertex-ai). The winner in enterprise AI distribution is increasingly not the model that wins the benchmark table but the one that is easiest to procure, audit, and integrate within existing cloud contracts.

For builders on AWS: Grok 4.3 on Bedrock is now a real option. The OpenAI-compatible API, configurable reasoning, and Bedrock-standard IAM access lower the switching cost enough to be worth evaluating on your specific workload — particularly if output volume and token cost are constraints.

---

*Grok 4.3 is xAI's current production model ([API release: April 30, 2026](https://artificialanalysis.ai/articles/xai-launches-grok-4-3-with-improved-agentic-performance-and-lower-pricing)). For the full model review, see **[Grok 4.3: Native Video, Always-On Reasoning, 40% Price Cut](/reviews/xai-grok-4-3-native-video-agentic-llm-review/)**. For xAI's API access path, see **[xAI Grok API review](/reviews/xai-grok-api-llm-inference/)**.*

