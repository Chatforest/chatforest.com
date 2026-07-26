---
title: "Cloud Fine-Tuning APIs — Beginner Guide (as of 26 Jul 2026)"
date: 2026-07-26
snapshot_date: 2026-07-26
topic: fine-tuning-cloud-apis
track: beginner
audience: "people new to AI"
description: "A plain-English guide to training a custom AI model using cloud services — no GPU required. Covers OpenAI, Together.ai, Vertex AI, AWS Bedrock, and OpenPipe, with cost warnings and step-by-step data preparation."
content_type: "Best Practice"
categories: ["Fine-Tuning", "Cloud APIs", "Beginners"]
tags: ["fine-tuning", "openai", "together-ai", "vertex-ai", "aws-bedrock", "beginners", "cloud"]
last_refreshed: 2026-07-26
graded_by: "RingS panel (Skeptic/Beginner/Timekeeper) + sensei, 2026-07-26"
grading_result: "14 beginner corrections applied; 0 fabrications"
---

<!-- This file lands at content/ai/beginner/fine-tuning-cloud-apis/2026-07-26/index.md and is an IMMUTABLE
     dated snapshot. Once published it is never edited — a refresh is a NEW <snapshot-date> dir.
     "Latest" is computed by Grove's template from snapshot_date; do not add a "latest" flag.
     Source tiers: independently-corroborated = 2+ DIFFERENT publishers; vendor-documented =
     official vendor docs only (authoritative, single source). -->

# Cloud Fine-Tuning APIs — Beginner Guide (as of 26 Jul 2026)

> **Grading note.** A dated snapshot — accurate as of **26 Jul 2026**, frozen here and kept as
> a permanent archive entry. Re-leveled from the 2026-07-26 technical entry; facts unchanged.
> Corrections applied inline; unverifiable gaps marked ⚠ PENDING — never guessed.

---

## What is cloud fine-tuning? (Start here)

Fine-tuning means taking a pre-trained AI language model and continuing to train it on your own data so that it learns to behave the way you want. Think of it like hiring an employee who already speaks English fluently, then giving them a week of company-specific training.

**Cloud** fine-tuning means a service (OpenAI, Together.ai, Google Vertex AI, or AWS Bedrock) does the heavy computing for you. You upload a file of training examples, click a button (or run a short command), and the service trains the model on their computers. You do not need a GPU of your own.

The basic flow for every cloud provider: prepare your data as a JSONL file → upload it → submit a training job → wait (minutes to hours) → test the resulting model → use it or serve it.

**JSONL** (JSON Lines) is the data format every provider on this page requires. It is a plain text file where **each line is one complete training example written as a JSON object** — no wrapping array, no commas between lines, just one JSON object per line followed by a newline character. The file extension is `.jsonl`.

---

## Before you begin — prerequisites

Before following any practice on this page, make sure you have:

- **Python installed** — any recent version (3.10 or later). Type `python3 --version` in your terminal to check.
- **pip installed** — Python's package installer. Type `pip --version` to check. If you have Python, pip is usually already there.
- **A terminal / command line** — on Mac or Linux, open Terminal. On Windows, use PowerShell or Windows Terminal.
- **An API key for the provider you choose** — an API key (also called a secret key) is a long string of letters and numbers that proves to the cloud service that you are you. Think of it as a password for the service's API (application programming interface — the way programs talk to each other). You get an API key by signing up on the provider's website and going to their API keys or settings page. **Never share your API key or paste it into code that you push to GitHub** — anyone who has your key can bill charges to your account. Store it as an environment variable (see the note under Practice 1).
- **Cloud billing awareness** — every provider on this page charges money for training jobs. The amounts can be small (a few dollars for a test run) or large (hundreds of dollars for big datasets). Check the provider's pricing page before submitting a job, and set a spending alert in your cloud account if the provider offers one.

---

## How to read the labels
- ✅ **independently-corroborated** — 2+ independent publishers
- 📄 **vendor-documented** — official docs only (authoritative, single source)
- ⚠️ **WARNING** — a default that can cost money, break the machine, or remove a safety net
- 🕒 **verify live** — fast-moving (versions/prices/quotas); check the current value

---

## Practice 1: OpenAI supervised fine-tuning — data format and job creation

⚠️ **WARNING — PLATFORM WIND-DOWN (read this before preparing any data):**
OpenAI is shutting down its fine-tuning platform in three stages:
- **2026-05-07:** Organizations that had never run a fine-tuning job lost access immediately.
- **2026-07-02 (already passed as of this snapshot):** Organizations with no fine-tuned-model inference activity in the prior 60 days lost the ability to create new fine-tuning jobs.
- **2027-01-06:** All remaining active users lose the ability to create new fine-tuning jobs.

As of this snapshot (2026-07-26), the July 2 stage has already passed — a large portion of former users have already lost access. **Before spending any time preparing data, confirm your organization still has access** by trying to list fine-tuning jobs via the API. If you get an access error, OpenAI's platform is not available to you — use Together.ai (Practice 2) instead.

---

**Do:** Format every training example as a JSONL file (one JSON object per line). Each object must have a `messages` array that follows the chat format — a list of turns with `role` and `content`. Upload the file with `purpose="fine-tune"`, then submit a training job.

Here is what one training example looks like (this single line is the entire content of one entry in your `.jsonl` file):

```jsonl
{"messages": [{"role": "user", "content": "Classify: 'The battery died'"},
              {"role": "assistant", "content": "hardware"}]}
```

Once you have your JSONL file uploaded and have received a file ID from the upload API, submit a fine-tuning job using this command. Replace `file-YOUR_FILE_ID_HERE` with the actual ID you received from the upload step:

```bash
curl https://api.openai.com/v1/fine_tuning/jobs \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"training_file": "file-YOUR_FILE_ID_HERE",
       "model": "gpt-4.1-nano-2025-04-14"}'
```

**What is `$OPENAI_API_KEY`?** The `$` means this is an environment variable — a secret your terminal passes to the command without you typing it directly into the command (which would expose it in your shell history). To set it, run `export OPENAI_API_KEY="your-actual-key-here"` in your terminal before running the curl command. Do not paste the key into the command itself, and do not commit it to a git repository.

**Why this matters:** Each line is one complete training example. The `messages` structure shows the model exactly what a correct conversation looks like. Currently fine-tunable models: `gpt-4.1-2025-04-14`, `gpt-4.1-mini-2025-04-14`, `gpt-4.1-nano-2025-04-14`. The minimum dataset size is 10 examples; OpenAI recommends starting with 50 well-crafted examples.

**Caveat / contested:** Tool-calling training (using the `tools` field) and vision fine-tuning use slightly different JSONL schemas. Mixing schemas in one file causes silent validation failures that abort the job — and the upload fee may still be charged. 🕒 Model list and platform status — verify live before submitting any job.

**Sources:** [developers.openai.com/api/docs/guides/supervised-fine-tuning](https://developers.openai.com/api/docs/guides/supervised-fine-tuning) (fetched 2026-07-26) · [community.openai.com — wind-down phase dates](https://community.openai.com/t/openai-is-winding-down-the-fine-tuning-api-and-platform-discussion-thread/1380522) (fetched by Timekeeper 2026-07-26)

**Confidence:** 📄 vendor-documented (both sources are OpenAI). 🕒 verify live — platform status and supported model list.

---

## Practice 2: Together.ai fine-tuning — open-weight model customization

Together.ai is currently the recommended starting point for beginners because it accepts new users, supports many popular open-weight models (models whose weights are publicly available), and gives you a pre-launch cost estimate before you spend anything.

**Do:** Upload your JSONL training file using `client.files.upload(file="train.jsonl", purpose="fine-tune")`, then launch a fine-tuning job via the Together.ai API or SDK. The platform gives you a cost estimate before the job starts — use this to avoid surprises. After training, you can **download the weights** in HuggingFace or GGUF format, so you are not locked into Together.ai's inference pricing.

**Why this matters:** Together.ai supports fine-tuning a wide range of open-weight model families including Llama 3/3.1/3.2/3.3/4, Qwen 2.5/3/3.5, Mistral, Gemma 3/4, and DeepSeek variants. 🕒 **verify live — model catalog:** Llama 4 support was announced as "coming in the weeks ahead" as of February 2026; Gemma 4 and Qwen 3.5 fine-tuning availability should be confirmed from the current supported-models page before training.

**Pricing (🕒 verify live):** Standard LoRA (a common fine-tuning method — see note below) rates: up to 16B params = $0.48/1M tokens, 17B–69B = $1.50/1M tokens, 70B–100B = $2.90/1M tokens. Minimum charge: $4.00 per job. Failed jobs are fully refunded; cancelled jobs pay only for completed steps.

**Two inference options explained:**
- A **dedicated endpoint** reserves a GPU exclusively for your fine-tuned model. It is billed per minute and keeps running even when no one is sending requests. If you deploy a dedicated endpoint and then do not use it for several days, you will be billed for all that idle time.
- **Serverless inference** uses a shared pool of GPUs and only charges you when you actually send a request. It is cheaper for occasional use.

⚠️ **WARNING:** The default hosting option on Together.ai is a dedicated endpoint — billed per minute even when idle. If you only need occasional inference, download the weights and self-host, or delete the endpoint between runs. Do not leave a dedicated endpoint running when you are not actively using it.

**Sources:** [docs.together.ai/docs/fine-tuning](https://docs.together.ai/docs/fine-tuning) (fetched 2026-07-26) · [together.ai/pricing — Fine-tuning](https://www.together.ai/pricing#fine-tuning) (fetched 2026-07-26) · [docs.together.ai/docs/fine-tuning/supported-models](https://docs.together.ai/docs/fine-tuning/supported-models) (fetched 2026-07-26) · [docs.together.ai/docs/fine-tuning/data-preparation](https://docs.together.ai/docs/fine-tuning/data-preparation) (fetched 2026-07-26)

**Confidence:** 📄 vendor-documented (all sources are Together.ai's own documentation). 🕒 verify live — pricing and model catalog.

---

## Practice 3: Vertex AI supervised tuning for Gemini 2.5

Vertex AI is Google's cloud AI platform. To use it for fine-tuning you need a Google Cloud Platform (GCP) account with billing enabled and a GCS (Google Cloud Storage) bucket in the same region as your Vertex AI project. GCS is Google's cloud file storage — it is separate from Google Drive and is where you store your training data and output files.

**Do:** Store your training data as a JSONL file in Google Cloud Storage (GCS). Then create a supervised tuning job via the Google Cloud console, the Vertex AI SDK for Python, or the Gen AI SDK. Key settings you can tune: epoch count (how many times the model sees your full dataset), learning rate (how fast it updates), and adapter size.

**Why this matters:** Vertex AI handles all GPU scheduling, checkpoint storage, and monitoring dashboards for you. The training cost is billed per **character** (not per token — note the different unit), so short fine-tuning runs on small datasets can stay affordable.

**Where to see your loss curves:** Vertex AI provides a monitoring dashboard in the Google Cloud console. After submitting a job, open the Vertex AI section of the console and look for your tuning job to see per-epoch training and validation loss.

**Caveat / contested:** As of this snapshot (2026-07-26), the current fine-tunable Gemini family on Vertex AI is **Gemini 2.5** (Flash, Flash Lite, and Pro). **Gemini 2.0 Flash and Gemini 2.0 Flash Lite were shut down on June 1, 2026 and can no longer be used for fine-tuning or inference** — do not attempt to use them. Gemini 3.x fine-tuning is in restricted preview for enterprise customers only. 🕒 **verify live — model availability and pricing:** Verify current rates at the Vertex AI pricing page before submitting a job.

⚠️ **WARNING:** Fine-tuned models on Vertex AI are served from the same region where the job ran. Accidentally leaving a high-throughput endpoint provisioned accrues inference charges 24/7 — even if no one is sending requests.

⚠️ **WARNING:** Gemini 2.5 Pro fine-tuned endpoints are scheduled to shut down on 2027-10-17. If you build a production system on Gemini 2.5 Pro fine-tuning, plan your migration before that date.

**Sources:** [cloud.google.com/vertex-ai/generative-ai/pricing](https://cloud.google.com/vertex-ai/generative-ai/pricing) (fetched 2026-07-26) · [docs.cloud.google.com/vertex-ai/generative-ai/docs/models/gemini-supervised-tuning](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/models/gemini-supervised-tuning) (fetched 2026-07-26) · aiweekly.co — Gemini 2.0 Flash shutdown confirmed by Timekeeper (fetched 2026-07-26)

**Confidence:** 📄 vendor-documented (Google Cloud documentation). 🕒 verify live — pricing, model availability, and shutdown schedule.

---

## Practice 4: AWS Bedrock model customization — fine-tuning via CreateModelCustomizationJob

AWS Bedrock is Amazon's managed AI service. Fine-tuning on Bedrock has more setup steps than the other providers, but once configured it handles all the GPU work for you.

**Before you start — two things you need to set up:**

1. **An S3 bucket** — S3 (Simple Storage Service) is Amazon's cloud file storage. You need to create an S3 bucket (a named container for files) in the same AWS region where you will run your Bedrock job. Supported regions are `us-east-1` or `us-west-2` depending on your target model. S3 bucket names must be globally unique — no two users anywhere in the world can have the same bucket name. You create a bucket in the AWS Console under the S3 service.

2. **An IAM service role** — IAM (Identity and Access Management) is the AWS system that controls what services are allowed to do. Bedrock needs permission to read your training data from S3 and write output back to S3, and you grant this by creating an IAM service role. Follow the [Bedrock IAM setup guide](https://docs.aws.amazon.com/bedrock/latest/userguide/model-customization-iam-role.html) step by step — do not try to configure this by hand, as misconfiguring it is the most common reason Bedrock fine-tuning jobs fail at submission.

**Do:** Put your training data as a JSONL file in your S3 bucket. Call `CreateModelCustomizationJob` with these fields: `baseModelIdentifier` (which model to start from), `customModelName` (a name for your new model), `jobName`, `trainingDataConfig` (the S3 path to your training file), `outputDataConfig` (the S3 path where results will be written — required, see WARNING below), and `hyperParameters`.

**Why this matters:** Bedrock handles GPU allocation and stores the resulting custom model. You pay per token trained rather than reserving a GPU for a fixed time window.

**Supported fine-tunable models as of this snapshot** (🕒 verify live):
- **Amazon Nova:** Nova Micro, Nova Lite, Nova Pro (us-east-1); Nova 2 Lite supports both supervised fine-tuning AND reinforcement fine-tuning (us-east-1)
- **Titan Image Generator G1 v2**
- **Anthropic Claude 3 Haiku** (us-west-2) — newer Claude models (Sonnet, Opus, Haiku 4.x) do not support fine-tuning on Bedrock
- **Meta Llama 3.1 8B/70B, 3.2 1B/3B/11B/90B, 3.3 70B** (us-west-2); **Llama 4** fine-tuning is also supported per 2026 AWS documentation (🕒 verify live)

⚠️ **WARNING — Provisioned Throughput required and billed hourly:** After training completes, you must purchase something called Provisioned Throughput to actually use your custom model. There is no pay-per-request option for fine-tuned Bedrock models. Provisioned Throughput is billed **every hour** whether or not you send any requests to the model. If you purchase Provisioned Throughput to test your model and then forget about it — even just for a week — you will be billed for every hour it was running. 🕒 Check the current hourly rate on the Bedrock pricing page before purchasing. Buying and forgetting an unused provisioned endpoint is a common and expensive mistake. Delete provisioned throughput when not in active use; you can repurchase it later.

⚠️ **WARNING — IAM misconfiguration:** The IAM service role must have S3 read permissions on your training bucket and S3 write permissions on your output bucket. Misconfiguring this role is the most common reason jobs fail at submission. Use the [Bedrock IAM setup guide](https://docs.aws.amazon.com/bedrock/latest/userguide/model-customization-iam-role.html) and do not attempt to configure these permissions by hand without following the guide.

⚠️ **WARNING:** Set `outputDataConfig` to a valid S3 path. If you omit this field, Bedrock has nowhere to write your loss curves (the graphs that show whether training is working). Without them, you are running blind — you will not be able to tell if training went well or badly.

**Where to see your loss curves:** Bedrock writes training and validation loss metrics to the S3 path you specify in `outputDataConfig`. Download or view those files after the job completes to check training progress.

**Sources:** [docs.aws.amazon.com/bedrock/latest/userguide/custom-model-fine-tuning.html](https://docs.aws.amazon.com/bedrock/latest/userguide/custom-model-fine-tuning.html) (fetched 2026-07-26) · [docs.aws.amazon.com/bedrock/latest/userguide/model-customization-prepare.html](https://docs.aws.amazon.com/bedrock/latest/userguide/model-customization-prepare.html) (fetched 2026-07-26) · [docs.aws.amazon.com/bedrock/latest/userguide/prov-throughput.html](https://docs.aws.amazon.com/bedrock/latest/userguide/prov-throughput.html) (fetched 2026-07-26) · [docs.aws.amazon.com/bedrock/latest/userguide/nova-2-sft-data-prep.html](https://docs.aws.amazon.com/bedrock/latest/userguide/nova-2-sft-data-prep.html) (fetched by Timekeeper 2026-07-26)

**Confidence:** 📄 vendor-documented (all AWS official documentation). 🕒 verify live — supported models and provisioned throughput pricing.

---

## Practice 5: OpenPipe — capture production traffic as fine-tuning data

OpenPipe is a service that acts as a drop-in replacement for the OpenAI Python SDK. A **drop-in replacement** means you swap one import line in your code and everything else stays the same — your existing calls to `chat.completions.create()` work without any other changes. OpenPipe silently logs every request your application makes to an LLM, and those logs become your fine-tuning training data.

⚠️ **WARNING — PII and secrets risk (read this BEFORE enabling logging):** Logging raw production traffic can capture Personally Identifiable Information (PII — names, emails, addresses, etc.), API keys embedded in user prompts, and confidential business data. Your production data will be transmitted to OpenPipe's infrastructure. Before enabling blanket capture: (1) review OpenPipe's data-handling terms, (2) implement request-level filtering to skip logging requests that match sensitive patterns, (3) confirm you have the right to log the data you are capturing.

---

**Do:** First install the OpenPipe SDK:

```bash
pip install openpipe
```

Then swap one import line in your existing Python code. Everything else stays the same:

```python
# Swap the import — everything else stays the same
from openpipe import OpenAI  # instead of: from openai import OpenAI
client = OpenAI(openpipe={"api_key": "your-openpipe-key"})
# All existing chat.completions.create() calls are now logged
```

The SDK logs every request asynchronously — it adds no delay to your application. Tag requests with metadata like `prompt_id` to distinguish data from different prompts.

For non-Python stacks, use the proxy endpoint and include `"store": true` in the request body.

**Why this matters:** Instead of hand-crafting training examples, you capture what your application is already sending to an LLM. The resulting fine-tuned model learns the exact behavior your users experience in production, and you can replace expensive large-model calls with a smaller, cheaper fine-tuned model doing the same job.

**Caveat / contested:** Training pricing is billed per token: $0.48/1M tokens (8B models) to $2.90/1M tokens (70B+) 🕒 verify live. The "100,000 free log slots per project" claim could not be verified from any fetched page; one 2026 review describes OpenPipe as having "no permanent free tier, just a trial" 🕒 verify live before assuming free quota exists.

**Sources:** [docs.openpipe.ai/features/request-logs](https://docs.openpipe.ai/features/request-logs) (fetched 2026-07-26) · [docs.openpipe.ai/features/fine-tuning](https://docs.openpipe.ai/features/fine-tuning) (fetched 2026-07-26) · [docs.openpipe.ai/pricing/pricing](https://docs.openpipe.ai/pricing/pricing) (fetched 2026-07-26)

**Confidence:** 📄 vendor-documented (all sources are OpenPipe's own documentation). 🕒 verify live — pricing and log quota.

---

## Practice 6: Validate training data before submitting a fine-tuning job

This is one of the most beginner-friendly practices in this guide — a 5-minute check on your own computer before you upload anything.

**Do:** Before uploading your JSONL file to any provider, run a local validation pass that checks: (1) every line parses as valid JSON, (2) required schema fields exist, (3) no individual example exceeds the provider's token limit, (4) no duplicates, and (5) PII has been scrubbed (removed).

First, install the `tiktoken` library (OpenAI's tokenizer — counts how long text is in tokens):

```bash
pip install tiktoken
```

Then run this script to count tokens and estimate cost:

```python
import tiktoken, json

# IMPORTANT: cl100k_base is for OpenAI models ONLY.
# If you are training a Llama, Qwen, or Mistral model on Together.ai or Bedrock,
# use that model's own tokenizer instead:
#   from transformers import AutoTokenizer
#   enc = AutoTokenizer.from_pretrained("meta-llama/Llama-3.1-8B")
# The cl100k_base tokenizer will give inaccurate counts for non-OpenAI models.
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

**Why this matters:** Cloud fine-tuning providers can reject malformed files after billing the upload fee, or silently skip bad lines. A 5-minute local check can prevent a multi-dollar wasted training run.

**Caveat / contested:** Token limits vary by provider: Bedrock's Llama 3.1 allows 16,000 tokens per example; Together.ai uses a packing approach with variable `max_seq_length`. Automated PII detection tools miss domain-specific identifiers — a human spot-check of 50–100 samples is still recommended.

**Sources:** [docs.together.ai/docs/fine-tuning/data-preparation](https://docs.together.ai/docs/fine-tuning/data-preparation) (fetched 2026-07-26) · [docs.aws.amazon.com/bedrock/latest/userguide/model-customization-prepare.html](https://docs.aws.amazon.com/bedrock/latest/userguide/model-customization-prepare.html) (fetched 2026-07-26) · datacamp.com/tutorial/tiktoken-library-python (fetched 2026-07-26; 403 bot-protection, confirmed live via WebFetch 2026-07-27)

**Confidence:** ✅ independently-corroborated (Together.ai vendor docs + AWS vendor docs + independent DataCamp tutorial — two distinct publishers confirming the core workflow)

---

## Practice 7: Monitor training vs. validation loss to detect overfitting

**Loss** is a number that measures how wrong the model is. During training, you want to see this number fall. **Overfitting** is what happens when the model memorizes your training examples instead of learning the underlying pattern — it scores well on training data but performs poorly on new data.

**Do:** Every major fine-tuning platform writes per-epoch training loss and validation loss to a dashboard or output files. After each epoch (one full pass through your training data), check whether training loss and validation loss are moving together downward (healthy) or diverging — training loss falling while validation loss flattens or rises (overfitting, time to stop).

**Where to see your loss curves on each platform:**
- **Together.ai:** A training dashboard is available in the Together.ai web interface for your job.
- **AWS Bedrock:** Loss metrics are written to the S3 path you set in `outputDataConfig`. Download those files after the job completes.
- **Vertex AI:** A monitoring dashboard is available in the Google Cloud console under your tuning job.

**Why this matters:** The validation curve is the only reliable signal that tells you when training is going wrong. Without it, you could end up with a model that scores perfectly on your training file but fails on real-world inputs.

**Caveat / contested:** You must supply a separate validation file or rely on the provider's automatic split. Without a validation dataset, training loss will always improve — making overfitting completely invisible. The optimal stopping epoch depends on dataset size; smaller datasets converge in fewer epochs. There is no universal safe default.

⚠️ **WARNING:** AWS Bedrock outputs training and validation loss metrics to the S3 path you specify in `outputDataConfig`. If you forget to set this field, you have no loss curves to inspect and are running blind.

**Sources:** [docs.aws.amazon.com/bedrock/latest/userguide/custom-models-hp.html](https://docs.aws.amazon.com/bedrock/latest/userguide/custom-models-hp.html) (fetched 2026-07-26) · databricks.com/blog/llm-fine-tuning (fetched 2026-07-26; 403 bot-protection, confirmed live via WebFetch 2026-07-27)

**Confidence:** ✅ independently-corroborated (AWS Bedrock vendor docs confirm hyperparameters including early-stopping; Databricks blog from a different publisher confirms the principle)

---

## Practice 8: Estimate and compare costs before choosing cloud fine-tuning vs. self-hosted

**Do:** Before starting a fine-tuning project, calculate the full cost using this formula:

```
total cost = (number of examples) × (average tokens per example) × (number of epochs) × (price per million tokens)
```

An **epoch** is one complete pass through your entire training dataset. Running 3 epochs means the model sees each training example 3 times.

**Worked example** (🕒 verify live — all prices approximate as of 2026-07-26):

| Scenario | Together.ai LoRA (16B model) | Together.ai LoRA (70B model) | Self-hosted H100 PCIe (cloud rental) |
|---|---|---|---|
| 50K examples × 1K avg tokens × 2 epochs = 100M tokens | ~$48 | ~$290 | ~$20 (10 hrs × $2/hr) |

**What is an H100 PCIe?** An H100 PCIe is a high-end NVIDIA data-center GPU (the specialized chip that runs AI training) available for rent on platforms like Lambda Labs, Vast.ai, or RunPod. Cloud GPU rental is cheaper at raw compute cost for large runs, but managed APIs win on simplicity for one-off or early-stage experiments — they include infrastructure, monitoring, and checkpoints without any setup.

⚠️ **WARNING:** Long-term inference cost can dwarf training cost at production query volumes. A fine-tuned model deployed on Together.ai's dedicated endpoint is billed per minute whether or not it is serving requests. If your inference volume is low or bursty, serverless (per-token) inference is cheaper than a dedicated endpoint.

**Sources:** [www.together.ai/pricing](https://www.together.ai/pricing#fine-tuning) (fetched 2026-07-26) · [spheron.network/blog/llm-fine-tuning-cost-2026-api-vs-renting-gpus/](https://www.spheron.network/blog/llm-fine-tuning-cost-2026-api-vs-renting-gpus/) (fetched 2026-07-26)

**Confidence:** ✅ independently-corroborated (Together.ai pricing page + independent Spheron cost-comparison article — different publishers). 🕒 verify live — all dollar figures.

---

## Practice 9: Lock the prompt template at inference to match your fine-tuning format

A **prompt template** is the fixed structure you wrap around user input before sending it to the model. For example: "You are a customer support agent. User: [input]. Answer:". During fine-tuning, the model learns to respond to this exact format. If you change it later, the model gets confused.

**Do:** Whatever system prompt and message format you used during training, use the **exact same** structure at inference time (when the model is actually running in production). Version-pin the system prompt alongside your fine-tuned model ID in your application configuration. When you create a new fine-tuned model version, test all prompt variants against the new checkpoint before switching production traffic.

**Why this matters:** Fine-tuning bakes a specific input format into the model's weights. A fine-tuned model trained on examples starting with "You are a customer support agent. User: ..." will produce noticeably worse outputs if the production system prompt is different — even if those prompts seem semantically similar.

**Caveat / contested:** Research (NeurIPS 2024, arxiv 2402.18540) found an exception specifically for **safety prompts**: fine-tuning models without a safety prompt while adding one at inference time better preserves alignment than using the same safety prompt in both phases. This applies specifically to safety instructions, not to task-formatting templates — for task-specific format templates, keeping training and inference templates identical remains the standard recommendation.

⚠️ **WARNING:** When a provider updates the underlying base model, your fine-tuned adapter may be silently serving on the new base while your system prompt was tuned for the old base. Plan quarterly revalidation when providers update underlying model versions.

**Sources:** [arxiv.org/html/2402.18540v2](https://arxiv.org/html/2402.18540v2) (NeurIPS 2024 paper, fetched 2026-07-26) · [getmaxim.ai/articles/prompt-versioning-best-practices-for-ai-engineering-teams/](https://www.getmaxim.ai/articles/prompt-versioning-best-practices-for-ai-engineering-teams/) (fetched 2026-07-26)

**Confidence:** ✅ independently-corroborated (peer-reviewed paper + independent engineering guide from different publisher)

---

## Practice 10: Iterate on fine-tuning using checkpoints, evals, and versioning

**Do:** Treat each fine-tuned model as a versioned artifact — give it a name, record which training data it was built on, and keep the system prompt version it was tuned with. Before shipping to users, test it with:
1. Your task-specific holdout set (examples the model was not trained on)
2. General-capability tests to check for regression (making sure the model did not forget things it could do before)
3. A paired comparison: show the judge model (from a different AI family than the one you are testing) pairs of responses, randomize which appears first, and score them

Only move to production when the candidate model passes your pre-set quality thresholds. Start with a canary deployment — send 5 to 10 percent of live traffic to the new model, monitor the key metrics, and automatically roll back if they drop.

**Why this matters:** It is easy to improve the specific task you trained on while accidentally making the model worse at following instructions or handling edge cases. The eval harness catches these regressions before your users do. Versioning every fine-tune lets you roll back in minutes.

**Caveat / contested:** LLM-as-judge evaluation is fast but introduces biases — position bias (model favors whichever answer appeared first), verbosity bias (longer answers rated higher), and self-preference (judge prefers outputs from its own model family). Mitigation: randomize answer positions per pair, use a judge from a different model family, and supplement with human spot-checks on 5–10% of samples.

⚠️ **WARNING:** Together.ai's checkpoint export URL was returning 404 at the time this entry was researched — the feature may have moved. Verify current export instructions in their docs before depending on checkpoint downloads.

**Sources:** [futureagi.com/blog/evaluating-fine-tuned-llms-2026/](https://futureagi.com/blog/evaluating-fine-tuned-llms-2026/) (fetched 2026-07-26) · databricks.com/blog/llm-fine-tuning (fetched 2026-07-26; 403 bot-protection, confirmed live via WebFetch 2026-07-27)

**Confidence:** ✅ independently-corroborated (FutureAGI blog + Databricks blog — different publishers; two FutureAGI articles are counted as one publisher)

---

## CHANGELOG (re-leveled from the 2026-07-26 technical entry; facts unchanged)

1. **[KILL-C1]** OpenAI platform wind-down elevated to prominently placed WARNING at the very top of Practice 1, above all code and instructions. It now appears before any data preparation steps.
2. **[KILL-C2]** Bedrock Provisioned Throughput WARNING expanded with plain-language explanation of what hourly billing means in practice ("even just for a week — you will be billed for every hour"). Note that a specific dollar figure requires live verification per the technical entry; a 🕒 pointer to the Bedrock pricing page is provided.
3. **[KILL-C3]** JSONL defined on first use in the "What is cloud fine-tuning?" intro section: "a plain text file where each line is one complete training example written as a JSON object — no wrapping array, no commas between lines, just one JSON object per line followed by a newline character."
4. **[KILL-C4]** IAM service role: added pointer to the [Bedrock IAM setup guide](https://docs.aws.amazon.com/bedrock/latest/userguide/model-customization-iam-role.html) (URL already present in technical entry) with explicit instruction to follow that guide step by step, not to attempt manual configuration.
5. **[KILL-C5]** S3 bucket: added explicit instruction to create the bucket in the same AWS region as the Bedrock job (us-east-1 or us-west-2) and noted that bucket names must be globally unique.
6. **[KILL-C6]** OpenPipe PII WARNING moved before the code snippet that enables logging. The WARNING now appears above the `pip install openpipe` and import-swap steps.
7. **[KILL-X1]** "Before you begin" prerequisites section added at the top: Python, pip, terminal, API key definition and safe handling, cloud billing awareness.
8. **[KILL-X2]** API key explained on first use in the prerequisites section and in Practice 1: definition, how to get one, how to set as environment variable (`export OPENAI_API_KEY=...`), and why never to hardcode or commit it.
9. **[FIX-C1]** tiktoken note expanded: cl100k_base is for OpenAI models only; Llama/Qwen/Mistral need the model's own tokenizer. `pip install tiktoken` added before the code snippet.
10. **[FIX-C2]** "Dedicated endpoint" vs "serverless" explained in one sentence each in Practice 2.
11. **[FIX-C3]** Vertex AI prerequisite added: GCP account with billing enabled, GCS bucket in same region. GCS distinguished from Google Drive.
12. **[FIX-C4]** H100 PCIe explained in Practice 8: "a high-end NVIDIA data-center GPU available for rent on platforms like Lambda Labs, Vast.ai, or RunPod."
13. **[FIX-C5]** curl example file ID already replaced with placeholder `file-YOUR_FILE_ID_HERE` in the technical entry (this was applied there); confirmed carried through here with accompanying explanation.
14. **[FIX-C6]** "Drop-in replacement" explained in plain English in Practice 5. `pip install openpipe` added as the first step.
15. **[FIX-C7]** "What is cloud fine-tuning?" intro paragraph added at the top of the document: what it is, how it differs from local training, and the basic flow.
16. **[FIX-C8]** Platform-specific pointers added to Practice 7 showing where to find loss curves: Together.ai dashboard, Bedrock S3 output, Vertex AI console.
17. **[Link-check gate]** databricks.com/blog/llm-fine-tuning (Practice 7 Sources, Practice 10 Sources) returned 403 bot-protection; confirmed live via WebFetch 2026-07-27. Unlinked to plain text per policy (2 occurrences).
18. **[Link-check gate]** datacamp.com/tutorial/tiktoken-library-python (Practice 6 Sources) returned 403 bot-protection; confirmed live via WebFetch 2026-07-27. Unlinked to plain text per policy.
