---
title: "Fine-Tuning and Adapting Language Models: Managed Cloud Services — Best Practices (as of 26 Jul 2026)"
date: 2026-07-26
snapshot_date: 2026-07-26
topic: fine-tuning-cloud-apis
track: best-practices
audience: "technically comfortable readers"
description: "Practical best practices for cloud-managed fine-tuning APIs — Together.ai, Vertex AI, AWS Bedrock, and OpenPipe — covering data format, job creation, cost estimation, limitations, and evaluation. OpenAI's fine-tuning platform is winding down; readers should be aware before investing."
content_type: "Best Practice"
categories: ["Fine-Tuning", "Cloud APIs", "LLM Customization"]
tags: ["fine-tuning", "openai", "together-ai", "vertex-ai", "aws-bedrock", "openpipe", "jsonl", "lora", "model-customization", "cloud-apis"]
last_refreshed: 2026-07-26
graded_by: "RingS panel (Skeptic/Beginner/Timekeeper) + sensei, 2026-07-26"
grading_result: "0 fabrications; 9 corrections applied; 0 unresolved gaps"
---

<!-- This file lands at content/ai/best-practices/fine-tuning-cloud-apis/2026-07-26/index.md and is an IMMUTABLE
     dated snapshot. Once published it is never edited — a refresh is a NEW <snapshot-date> dir.
     "Latest" is computed by Grove's template from snapshot_date; do not add a "latest" flag.
     Source tiers: independently-corroborated = 2+ DIFFERENT publishers; vendor-documented =
     official vendor docs only (authoritative, single source). -->

# Fine-Tuning and Adapting Language Models: Managed Cloud Services (as of 26 Jul 2026)

> **Grading note.** A dated snapshot — accurate as of **26 Jul 2026**, frozen here and kept as
> a permanent archive entry. Research-drafted by a pupil, graded by the 3-lens panel + sensei.
> Corrections applied inline; unverifiable gaps marked ⚠ PENDING — never guessed.

## What is managed cloud fine-tuning?

Managed cloud fine-tuning lets you upload a training dataset, configure a fine-tuning job via API or dashboard, and receive a customised model without managing any GPU infrastructure. You pay per token trained rather than reserving GPU hours. The basic flow: prepare data → upload → submit job → wait for training → test the resulting model → serve it.

**JSONL format** (used by all providers): a text file where each line is a self-contained JSON object — no wrapping array, no commas between lines, newline-delimited. One JSON object = one training example.

## How to read the labels
- ✅ **independently-corroborated** — 2+ independent publishers
- 📄 **vendor-documented** — official docs only (authoritative, single source)
- ⚠️ **WARNING** — a default that can cost money, break the machine, or remove a safety net
- 🕒 **verify live** — fast-moving (versions/prices/quotas); check the current value

---

## Practice 1: OpenAI supervised fine-tuning — data format and job creation

⚠️ **WARNING — PLATFORM WIND-DOWN (read before investing time in data preparation):**
OpenAI is winding down its fine-tuning platform in three phases with specific dates:
- **2026-05-07:** Organizations that had never run a fine-tuning job lost access immediately.
- **2026-07-02 (already passed):** Organizations with no fine-tuned-model inference activity in the prior 60 days lost the ability to create new fine-tuning jobs.
- **2027-01-06:** All remaining active users lose the ability to create new fine-tuning jobs.

As of this snapshot (2026-07-26), the July 2 phase has already passed — a significant fraction of former users have already lost access. Before investing in data preparation, confirm your organization still has access by attempting to list fine-tuning jobs via the API.

---

**Do:** Format every training example as a single JSON object on its own line (JSONL), with a `messages` array following the chat completions structure. Upload the file with `purpose="fine-tune"`, then create a job by POST-ing to `/v1/fine_tuning/jobs`.

```jsonl
{"messages": [{"role": "user", "content": "Classify: 'The battery died'"},
              {"role": "assistant", "content": "hardware"}]}
```

```bash
curl https://api.openai.com/v1/fine_tuning/jobs \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"training_file": "file-YOUR_FILE_ID_HERE",
       "model": "gpt-4.1-nano-2025-04-14"}'
```

`$OPENAI_API_KEY` is an environment variable holding your secret API key — never hardcode it in source files. The `training_file` ID comes from the file upload API response.

**Why:** Each line is one complete training example. The `messages` structure tells OpenAI exactly what a correct conversation looks like. Currently fine-tunable models: `gpt-4.1-2025-04-14`, `gpt-4.1-mini-2025-04-14`, `gpt-4.1-nano-2025-04-14`. The minimum is 10 examples; OpenAI recommends starting with 50 well-crafted examples.

**Caveat / contested:** Tool-calling training (`tools` field) and vision fine-tuning use slightly different JSONL schemas; mixing schemas in one file causes silent validation failures that abort the job after upload fees are charged. 🕒 Model list and platform status — verify live before submitting any job.

**Sources:** [developers.openai.com/api/docs/guides/supervised-fine-tuning](https://developers.openai.com/api/docs/guides/supervised-fine-tuning) (fetched 2026-07-26) · [community.openai.com — wind-down phase dates](https://community.openai.com/t/openai-is-winding-down-the-fine-tuning-api-and-platform-discussion-thread/1380522) (fetched by Timekeeper 2026-07-26)

**Confidence:** 📄 vendor-documented (both sources are OpenAI). 🕒 verify live — platform status and supported model list.

---

## Practice 2: Together.ai fine-tuning — open-weight model customization

**Do:** Upload your JSONL training file using `client.files.upload(file="train.jsonl", purpose="fine-tune")`, then launch a LoRA or full fine-tuning job via the Together.ai API or SDK. The platform provides a pre-launch cost estimate via CLI, web UI, or the estimate-price API endpoint. After training, you can **download the weights** as HuggingFace or GGUF format — you are not locked into Together's inference pricing.

**Why:** Unlike OpenAI's winding-down platform, Together.ai currently accepts new users and supports fine-tuning a wide range of open-weight model families including Llama 3/3.1/3.2/3.3/4, Qwen 2.5/3/3.5, Mistral, Gemma 3/4, and DeepSeek variants. 🕒 **verify live — model catalog:** Llama 4 support was announced as "coming in the weeks ahead" as of February 2026; Gemma 4 and Qwen 3.5 fine-tuning availability should be confirmed from the current supported-models page before training.

**Pricing (🕒 verify live):** Standard LoRA SFT rates: up to 16B params = $0.48/1M tokens, 17B–69B = $1.50/1M tokens, 70B–100B = $2.90/1M tokens. Specialized architectures carry separately-negotiated rates. Minimum charge: $4.00 per job. Failed jobs are fully refunded; cancelled jobs pay only for completed steps.

⚠️ **WARNING:** The default dedicated-endpoint hosting is billed per-minute and runs continuously even when idle. Download the weights and self-host if you only need occasional inference, or delete the endpoint between runs.

**Sources:** [docs.together.ai/docs/fine-tuning](https://docs.together.ai/docs/fine-tuning) (fetched 2026-07-26) · [together.ai/pricing — Fine-tuning](https://www.together.ai/pricing#fine-tuning) (fetched 2026-07-26) · [docs.together.ai/docs/fine-tuning/supported-models](https://docs.together.ai/docs/fine-tuning/supported-models) (fetched 2026-07-26) · [docs.together.ai/docs/fine-tuning/data-preparation](https://docs.together.ai/docs/fine-tuning/data-preparation) (fetched 2026-07-26)

**Confidence:** 📄 vendor-documented (all sources are Together.ai's own documentation). 🕒 verify live — pricing and model catalog.

---

## Practice 3: Vertex AI supervised tuning for Gemini 2.5

**Do:** Store your training data as a JSONL file in Google Cloud Storage, then create a supervised tuning job via the Google Cloud console, the Vertex AI SDK for Python, or the Gen AI SDK. You need a GCP account with billing enabled and a GCS bucket in the same region as your Vertex AI project. Key tunable hyperparameters include epoch count, learning rate, and adapter size.

**Why:** Vertex AI handles all GPU scheduling, checkpoint storage, and monitoring dashboards. The training cost is billed per **character** (not token — note the unit), so short fine-tuning runs on small datasets stay affordable.

**Caveat / contested:** As of this snapshot (2026-07-26), the current fine-tunable Gemini family on Vertex AI is **Gemini 2.5** (Flash, Flash Lite, and Pro). **Gemini 2.0 Flash and Gemini 2.0 Flash Lite were shut down on June 1, 2026 and can no longer be used for fine-tuning or inference.** Gemini 3.x fine-tuning is in restricted preview for enterprise customers only. 🕒 **verify live — model availability and pricing:** Vertex AI pricing is billed per training character; verify current rates at the Vertex AI pricing page before submitting a job. The Python SDK's `aiplatform.from_pretrained()` + `.tune_model()` pattern referenced in older guides may have been superseded by the Gen AI SDK.

⚠️ **WARNING:** Fine-tuned models on Vertex AI are served from the same region where the job ran. Accidentally leaving a high-throughput endpoint provisioned accrues inference charges 24/7.

⚠️ **WARNING:** Gemini 2.5 Pro fine-tuned endpoints are scheduled to shut down on 2027-10-17 — plan migrations if you use Gemini 2.5 Pro fine-tuning in production.

**Sources:** [cloud.google.com/vertex-ai/generative-ai/pricing](https://cloud.google.com/vertex-ai/generative-ai/pricing) (fetched 2026-07-26) · [docs.cloud.google.com/vertex-ai/generative-ai/docs/models/gemini-supervised-tuning](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/models/gemini-supervised-tuning) (fetched 2026-07-26) · aiweekly.co — Gemini 2.0 Flash shutdown confirmed by Timekeeper (fetched 2026-07-26)

**Confidence:** 📄 vendor-documented (Google Cloud documentation). 🕒 verify live — pricing, model availability, and shutdown schedule.

---

## Practice 4: AWS Bedrock model customization — fine-tuning via CreateModelCustomizationJob

**Do:** Put your training data as a JSONL file in an S3 bucket (create the bucket in the same AWS region as your Bedrock job — us-east-1 or us-west-2 depending on your target model). Grant Bedrock an IAM service role with S3 read permissions on your training bucket and S3 write permissions on your output bucket — see the [Bedrock IAM setup guide](https://docs.aws.amazon.com/bedrock/latest/userguide/model-customization-iam-role.html). Call `CreateModelCustomizationJob` with `baseModelIdentifier`, `customModelName`, `jobName`, `trainingDataConfig` (S3 URI), `outputDataConfig` (required), and `hyperParameters`.

**Why:** Bedrock handles GPU allocation and stores the resulting custom model. You pay per token trained rather than reserving a GPU for a fixed time window.

**Supported fine-tunable models as of this snapshot** (🕒 verify live):
- **Amazon Nova:** Nova Micro, Nova Lite, Nova Pro (us-east-1); Nova 2 Lite supports both supervised fine-tuning AND reinforcement fine-tuning (us-east-1)
- **Titan Image Generator G1 v2**
- **Anthropic Claude 3 Haiku** (us-west-2) — newer Claude models (Sonnet, Opus, Haiku 4.x) do not support fine-tuning on Bedrock
- **Meta Llama 3.1 8B/70B, 3.2 1B/3B/11B/90B, 3.3 70B** (us-west-2); **Llama 4** fine-tuning is also supported per 2026 AWS documentation (🕒 verify live)

⚠️ **WARNING — Provisioned Throughput required:** After training completes, you must purchase Provisioned Throughput to use a custom model — there is no on-demand API for fine-tuned Bedrock models. Provisioned Throughput is billed **hourly** whether or not you send requests, and billing continues until you explicitly delete it. Buying and forgetting an unused provisioned endpoint is a common and expensive mistake. Delete provisioned throughput when not in active use; you can repurchase it later. 🕒 Check current hourly rates on the Bedrock pricing page before purchasing.

⚠️ **WARNING — IAM misconfiguration:** The IAM service role must have S3 read permissions on your training bucket and S3 write permissions on your output bucket. Misconfiguring this role is the most common reason jobs fail at submission. Use the Bedrock IAM setup guide linked above; do not attempt to configure these permissions by hand without following the guide.

⚠️ **WARNING:** Set `outputDataConfig` to a valid S3 path. If you omit it, you will have no loss curves to inspect and will be running blind.

**Sources:** [docs.aws.amazon.com/bedrock/latest/userguide/custom-model-fine-tuning.html](https://docs.aws.amazon.com/bedrock/latest/userguide/custom-model-fine-tuning.html) (fetched 2026-07-26) · [docs.aws.amazon.com/bedrock/latest/userguide/model-customization-prepare.html](https://docs.aws.amazon.com/bedrock/latest/userguide/model-customization-prepare.html) (fetched 2026-07-26) · [docs.aws.amazon.com/bedrock/latest/userguide/prov-throughput.html](https://docs.aws.amazon.com/bedrock/latest/userguide/prov-throughput.html) (fetched 2026-07-26) · [docs.aws.amazon.com/bedrock/latest/userguide/nova-2-sft-data-prep.html](https://docs.aws.amazon.com/bedrock/latest/userguide/nova-2-sft-data-prep.html) (fetched by Timekeeper 2026-07-26)

**Confidence:** 📄 vendor-documented (all AWS official documentation). 🕒 verify live — supported models and provisioned throughput pricing.

---

## Practice 5: OpenPipe — capture production traffic as fine-tuning data

⚠️ **WARNING — PII / secrets risk:** Logging raw production traffic can capture PII, API keys in user prompts, and confidential business data. Implement request-level filtering (e.g., skip logging requests that match a PII pattern) **before** enabling blanket capture. Your production data will be transmitted to OpenPipe's infrastructure — review their data-handling terms before enabling.

---

**Do:** Install the OpenPipe SDK as a drop-in replacement for the OpenAI Python SDK (`pip install openpipe`). Change your import and add your OpenPipe API key; the SDK logs every request asynchronously (adding zero latency). Tag requests with metadata like `prompt_id` to distinguish data from different prompts.

```python
# Swap the import — everything else stays the same
from openpipe import OpenAI  # instead of: from openai import OpenAI
client = OpenAI(openpipe={"api_key": "your-openpipe-key"})
# All existing chat.completions.create() calls are now logged
```

For non-Python stacks, use the proxy endpoint and include `"store": true` in the request body.

**Why:** Instead of hand-crafting training examples, you capture what your application is already sending to an LLM. The resulting fine-tuned model learns the exact behavior your users experience in production, and you can replace expensive frontier model calls with a smaller, cheaper fine-tuned model doing the same job.

**Caveat / contested:** Training pricing is billed per token: $0.48/1M tokens (8B models) to $2.90/1M tokens (70B+) 🕒 verify live. The "100,000 free log slots per project" claim could not be verified from any fetched page; one 2026 review describes OpenPipe as having "no permanent free tier, just a trial" 🕒 verify live before assuming free quota exists.

**Sources:** [docs.openpipe.ai/features/request-logs](https://docs.openpipe.ai/features/request-logs) (fetched 2026-07-26) · [docs.openpipe.ai/features/fine-tuning](https://docs.openpipe.ai/features/fine-tuning) (fetched 2026-07-26) · [docs.openpipe.ai/pricing/pricing](https://docs.openpipe.ai/pricing/pricing) (fetched 2026-07-26)

**Confidence:** 📄 vendor-documented (all sources are OpenPipe's own documentation). 🕒 verify live — pricing and log quota.

---

## Practice 6: Validate training data before submitting a fine-tuning job

**Do:** Before uploading a JSONL file to any provider, run a local validation pass that checks: (1) every line parses as valid JSON, (2) required schema fields exist, (3) no individual example exceeds the provider's token limit, (4) no duplicates, and (5) PII has been scrubbed. Use `tiktoken` to count tokens per example and estimate total training cost before submitting.

```python
import tiktoken, json

# Use cl100k_base for OpenAI models ONLY.
# For Llama/Qwen/Mistral/Gemma models, use the model's own tokenizer
# (e.g., AutoTokenizer.from_pretrained("meta-llama/Llama-3.1-8B"))
enc = tiktoken.get_encoding("cl100k_base")

def token_count(messages):
    return sum(len(enc.encode(m["content"])) for m in messages)

total_tokens = 0
with open("train.jsonl") as f:
    for i, line in enumerate(f):
        ex = json.loads(line)
        n = token_count(ex["messages"])
        total_tokens += n
        if n > 16_000:
            print(f"Line {i}: {n} tokens — exceeds limit")

n_epochs = 3
estimated_cost = (total_tokens * n_epochs / 1_000_000) * 0.48  # Together 16B rate
print(f"Estimated training cost: ${estimated_cost:.2f}")
```

**Why:** Cloud fine-tuning providers reject malformed files after billing the upload, or silently skip bad lines. A 5-minute local check can prevent a multi-dollar wasted training run.

**Caveat / contested:** Provider-specific token limits vary: Bedrock's Llama 3.1 allows 16,000 tokens per example; Together.ai uses a packing approach with variable `max_seq_length`. Automated PII detection (spaCy NER, Microsoft Presidio) misses domain-specific identifiers — a human spot-check of 50–100 samples is still recommended.

**Sources:** [docs.together.ai/docs/fine-tuning/data-preparation](https://docs.together.ai/docs/fine-tuning/data-preparation) (fetched 2026-07-26) · [docs.aws.amazon.com/bedrock/latest/userguide/model-customization-prepare.html](https://docs.aws.amazon.com/bedrock/latest/userguide/model-customization-prepare.html) (fetched 2026-07-26) · datacamp.com/tutorial/tiktoken-library-python (fetched 2026-07-26; 403 bot-protection, confirmed live via WebFetch 2026-07-27)

**Confidence:** ✅ independently-corroborated (Together.ai vendor docs + AWS vendor docs + independent DataCamp tutorial — two distinct publishers confirming the core workflow)

---

## Practice 7: Monitor training vs. validation loss to detect overfitting

**Do:** Every major fine-tuning platform writes per-epoch training loss and validation loss to a dashboard or output files. After each epoch, check whether training loss and validation loss are moving together downward (healthy) or diverging — training loss falling while validation loss flattens or rises (overfitting). Where to find the curves: Together.ai provides a training dashboard; Bedrock writes loss metrics to the S3 path in `outputDataConfig`; Vertex AI provides a monitoring dashboard in the Google Cloud console.

**Why:** A model that overfits has memorized your training examples rather than learning the underlying pattern. The validation curve is the only signal that tells you when to stop.

**Caveat / contested:** You must supply a separate validation file or rely on the provider's automatic split. Without a validation dataset, training loss will always improve — making overfitting invisible. The optimal stopping epoch depends on dataset size; smaller datasets converge in fewer epochs. There is no universal safe default.

⚠️ **WARNING:** AWS Bedrock outputs training and validation loss metrics to the S3 path you specify in `outputDataConfig`. If you forget to set this field, you have no loss curves to inspect and are running blind.

**Sources:** [docs.aws.amazon.com/bedrock/latest/userguide/custom-models-hp.html](https://docs.aws.amazon.com/bedrock/latest/userguide/custom-models-hp.html) (fetched 2026-07-26) · databricks.com/blog/llm-fine-tuning (fetched 2026-07-26; 403 bot-protection, confirmed live via WebFetch 2026-07-27)

**Confidence:** ✅ independently-corroborated (AWS Bedrock vendor docs confirm hyperparameters including early-stopping; Databricks blog from a different publisher confirms the principle)

---

## Practice 8: Estimate and compare costs before choosing cloud fine-tuning vs. self-hosted

**Do:** Before starting a fine-tuning project, calculate the full cost: `n_examples × avg_tokens_per_example × n_epochs × price_per_million_tokens`. Compare the managed API cost against the cost of renting a GPU for the same job.

**Worked example** (🕒 verify live — all prices approximate as of 2026-07-26):

| Scenario | Together.ai LoRA (16B) | Together.ai LoRA (70B) | Self-hosted H100 PCIe (cloud rental) |
|---|---|---|---|
| 50K examples × 1K avg tokens × 2 epochs = 100M tokens | ~$48 | ~$290 | ~$20 (10 hrs × $2/hr) |

H100 PCIe is a high-end NVIDIA data-centre GPU available for rent on platforms like Lambda Labs, Vast.ai, or RunPod. Cloud GPU rental is cheaper at raw compute cost for large runs, but managed APIs win on simplicity for one-off or early-stage experiments — they include infrastructure, monitoring, and checkpoints.

⚠️ **WARNING:** Long-term inference cost dwarfs training cost at production query volumes. A fine-tuned model deployed on Together.ai's dedicated endpoint is billed per minute whether or not it is serving requests. If inference volume is low or bursty, serverless (per-token) inference is cheaper than a dedicated endpoint.

**Sources:** [www.together.ai/pricing](https://www.together.ai/pricing#fine-tuning) (fetched 2026-07-26) · [spheron.network/blog/llm-fine-tuning-cost-2026-api-vs-renting-gpus/](https://www.spheron.network/blog/llm-fine-tuning-cost-2026-api-vs-renting-gpus/) (fetched 2026-07-26)

**Confidence:** ✅ independently-corroborated (Together.ai pricing page + independent Spheron cost-comparison article — different publishers). 🕒 verify live — all dollar figures.

---

## Practice 9: Lock the prompt template at inference to match your fine-tuning format

**Do:** Whatever system prompt and message format you used during training, use the **exact same** structure at inference time. Version-pin the system prompt alongside your fine-tuned model ID in your application configuration. When you create a new fine-tuned model version, test all prompt variants against the new checkpoint before switching production traffic.

**Why:** Fine-tuning bakes a specific input format into the model's weights. A fine-tuned model trained on examples starting with "You are a customer support agent. User: ..." will produce worse outputs if the production system prompt is different — even if those prompts seem semantically similar. The model has learned to associate your exact format with correct behavior.

**Caveat / contested:** Research (NeurIPS 2024, arxiv 2402.18540) found a counterintuitive exception specifically for **safety prompts**: fine-tuning models *without* a safety prompt while adding one at inference time ("Pure Tuning, Safe Testing") better preserves alignment than using the same safety prompt in both phases. This applies specifically to safety instructions, not to task-formatting templates — for task-specific format templates, keeping training and inference templates identical remains the standard recommendation.

⚠️ **WARNING:** When a provider updates the underlying base model, your fine-tuned adapter may be silently serving on the new base while your system prompt was tuned for the old base. Plan quarterly revalidation when providers update underlying model versions.

**Sources:** [arxiv.org/html/2402.18540v2](https://arxiv.org/html/2402.18540v2) (NeurIPS 2024 paper, fetched 2026-07-26) · [getmaxim.ai/articles/prompt-versioning-best-practices-for-ai-engineering-teams/](https://www.getmaxim.ai/articles/prompt-versioning-best-practices-for-ai-engineering-teams/) (fetched 2026-07-26)

**Confidence:** ✅ independently-corroborated (peer-reviewed paper + independent engineering guide from different publisher)

---

## Practice 10: Iterate on fine-tuning using checkpoints, evals, and versioning

**Do:** Treat each fine-tuned model as a versioned artifact. Before shipping, run it through an eval harness covering (1) your task-specific holdout set, (2) general-capability benchmarks to check for regression, and (3) a paired arena comparison (200–500 examples, judge model from a different family, position-randomized). Only promote to production when the candidate model clears your pre-registered quality thresholds. Implement a canary deployment (5–10% of traffic; monitor key metrics, roll back automatically if they drop by a threshold).

**Why:** It is easy to improve the specific task you trained on while accidentally degrading the model's ability to follow instructions or handle edge cases. The eval harness catches these regressions before your users do. Versioning every fine-tune (with the model ID, training data hash, and system prompt version) lets you roll back in minutes.

**Caveat / contested:** LLM-as-judge evaluation is fast but introduces biases — position bias (model favors whichever answer appeared first), verbosity bias (longer answers rated higher), and self-preference (judge prefers outputs from its own model family). Mitigation: randomize answer positions per pair, use a judge from a different model family, and supplement with human spot-checks on 5–10% of samples.

⚠️ **WARNING:** Together.ai's checkpoint export URL was returning 404 at pupil fetch time — the feature may have moved. Verify current export instructions in their docs before depending on checkpoint downloads.

**Sources:** [futureagi.com/blog/evaluating-fine-tuned-llms-2026/](https://futureagi.com/blog/evaluating-fine-tuned-llms-2026/) (fetched 2026-07-26) · databricks.com/blog/llm-fine-tuning (fetched 2026-07-26; 403 bot-protection, confirmed live via WebFetch 2026-07-27)

**Confidence:** ✅ independently-corroborated (FutureAGI blog + Databricks blog — different publishers; two FutureAGI articles are counted as one publisher)

---

## CHANGELOG (grading → this entry)

1. **[KILL — Timekeeper/P3]** Practice 3 rewritten. Gemini 2.0 Flash and Gemini 2.0 Flash Lite were shut down June 1, 2026. References to those dead endpoints removed; content updated to Gemini 2.5 (Flash, Flash Lite, Pro) as the current fine-tunable family. Billing unit corrected to characters (not tokens). Gemini 3.x restricted-preview status noted. Gemini 2.5 Pro endpoint shutdown (Oct 17, 2027) added as WARNING.
2. **[KILL — Timekeeper/P1]** OpenAI wind-down description replaced with three specific phase dates (May 7, July 2, January 6, 2027). July 2 phase already passed as of snapshot date. Elevated from buried caveat to prominent WARNING box at top of practice.
3. **[FIX — Beginner/P1]** Wind-down WARNING moved to top of practice, above the code examples. Added explanation of `$OPENAI_API_KEY` as an environment variable. Replaced hardcoded file ID with placeholder.
4. **[FIX — Timekeeper/P4]** Corrected "Nova 2 Lite/Lite/Micro/Pro" typo → "Nova Micro, Nova Lite, Nova Pro, Nova 2 Lite." Added Llama 4 fine-tuning support (confirmed by AWS 2026 docs via Timekeeper). Added Nova 2 Lite reinforcement fine-tuning support. Added link to Bedrock IAM setup guide. Added S3 bucket region guidance. Added `outputDataConfig` WARNING.
5. **[FIX — Timekeeper/P2]** Added verify-live note specifically for Llama 4 and Gemma 4 fine-tuning (Llama 4 was announced "coming" Feb 2026; not all catalog entries confirmed available).
6. **[FIX — Timekeeper/P5]** Moved PII WARNING before code snippet. Marked "100,000 free log slots" as unverified inline with 🕒 note (one 2026 review says "no permanent free tier").
7. **[FIX — Skeptic/P7]** Removed un-citable "search results" source line from P7. AWS and Databricks sources are sufficient.
8. **[FIX — Skeptic/P10]** Corrected independence label reasoning: two FutureAGI articles = one publisher. Corroboration comes from Databricks, giving two real publishers. Confidence label unchanged (still independently-corroborated); reasoning note fixed.
9. **[FIX — Beginner/P6]** Added note that `cl100k_base` is for OpenAI models only; non-OpenAI models (Llama/Qwen/Mistral) require their own tokenizer. Added `pip install` command for tiktoken.
10. **[Link-check gate]** databricks.com/blog/llm-fine-tuning (2 occurrences: P7 Sources, P10 Sources) returned 403 bot-protection; confirmed live via WebFetch 2026-07-27. Unlinked to plain text per policy.
11. **[Link-check gate]** datacamp.com/tutorial/tiktoken-library-python (P6 Sources) returned 403 bot-protection; confirmed live via WebFetch 2026-07-27. Unlinked to plain text per policy.
