---
title: "LLM Observability and Monitoring — Managed Cloud Platforms — Beginner Guide (as of 16 Jul 2026)"
date: 2026-07-16
snapshot_date: 2026-07-16
topic: llm-observability-managed-platforms
track: beginner
audience: "people new to AI"
description: "How to instrument and monitor LLM workloads on Datadog Agent Observability, New Relic AI Monitoring, AWS Bedrock + CloudWatch, GCP Vertex AI, and Azure AI Foundry — written for people brand new to AI and to the command line."
content_type: "Best Practice"
categories: ["LLM Observability", "Managed Cloud"]
tags: ["datadog", "new-relic", "aws-bedrock", "cloudwatch", "vertex-ai", "azure-ai-foundry", "llm-monitoring", "observability"]
last_refreshed: 2026-07-16
graded_by: "RingS panel (Skeptic/Beginner/Timekeeper) + sensei, 2026-07-16"
grading_result: "0 fabrications; beginner re-level applied (KILL-MP-1 through KILL-MP-4, FIX-MP-1 through FIX-MP-5); all verified facts and source URLs preserved from technical entry."
---

# LLM Observability and Monitoring: Managed Cloud Platforms — Beginner Guide (as of 16 Jul 2026)

> **What this is.** A dated snapshot — accurate as of **16 Jul 2026**, frozen here as a permanent archive entry. Written for someone brand new to AI, Ubuntu, and cloud tools. Every fact here comes from the technical entry graded by the RingS panel on 2026-07-16. No new facts have been added.

## A quick vocabulary note before you start

**Observability** means being able to see what your AI application is actually doing — what prompts it sends, how long it takes to respond, and when it fails.

**A trace** is the complete record of one request flowing through your AI application — for example, a user's question and all the steps your app took to answer it.

**A span** is one step within that trace — one call to an AI model, one tool call, or one step in a chain of actions.

**APM (Application Performance Monitoring)** is a paid Datadog add-on that tracks the performance of software applications. Datadog's LLM monitoring requires an existing APM subscription — it is not available on free plans.

## How to read the labels
- ✅ **independently-corroborated** — 2+ independent publishers confirmed this
- 📄 **vendor-documented** — official docs only (authoritative, single source)
- ⚠️ **WARNING** — a default that can cost money, break the machine, or remove a safety net
- 🕒 **verify live** — fast-moving (versions, prices, quotas); check the current value before acting

---

## Practice 1: Enable Datadog Agent Observability (formerly "LLM Observability") by setting `DD_LLMOBS_ENABLED=1`

**Before you enable anything — read the cost warning below.**

⚠️ **WARNING (cost):** Per-span billing scales directly with your traffic. As a rough example: if your app handles 10,000 LLM calls per day and Datadog creates two spans per call, you have 20,000 spans per day. At any per-span rate, this grows directly with your traffic — and grows again if you enable evaluators (see Practice 2). Set a Datadog budget alert before enabling in production: go to Plan & Usage → Budget Alerts and set a monthly cap. Without this step, you will discover the cost on your next invoice, not before it.

⚠️ **WARNING (plan check):** APM (Application Performance Monitoring) is a paid Datadog add-on. Check your current Datadog plan before enabling LLM Observability — you may need to upgrade. See datadoghq.com/pricing for current plan details.

**Do:** Install the `ddtrace` package (Python), `dd-trace` (Node.js), or `dd-trace-java` (Java 8+). Set three environment variables: `DD_LLMOBS_ENABLED=1`, `DD_API_KEY` (your Datadog API key), and `DD_SITE` (your Datadog region, e.g. `datadoghq.com`). Then start your application with the tracer running. Datadog will automatically capture LLM spans — including input and output tokens, latency, model ID, and errors — for each call to supported providers (OpenAI, Anthropic, AWS Bedrock, Vertex AI, LangChain, and others).

> **Product name note (2026):** The product is now marketed as "Agent Observability" in the Datadog console and product pages. The environment variable `DD_LLMOBS_ENABLED` and the docs URL (`docs.datadoghq.com/llm_observability/`) keep the older `llm_observability` path. Both names refer to the same product; use `DD_LLMOBS_ENABLED=1` to activate it regardless of which name you see.

**Why it matters (and what goes wrong without it):** Without instrumentation you have no visibility into what prompts your app sends, how long they take, or when they fail. If a user complains that your AI gave a wrong answer or timed out, you have no record to investigate. Datadog Agent Observability went Generally Available (GA — meaning it is production-ready and fully supported) on 26 June 2024 and groups every step of a multi-model chain into a single trace so you can pinpoint which call caused a slow or broken response.

**Pricing:** 🕒 As of May 2026, the free plan includes 40,000 LLM spans per month; the Pro plan starts at $160 per month for 100,000 spans. These tiers are recent and may change — verify live at datadoghq.com/pricing. Note: this product is not supported on Datadog government-region sites.

**Sources:**
- [docs.datadoghq.com/llm_observability/setup/](https://docs.datadoghq.com/llm_observability/setup/) (Datadog official docs, fetched 2026-07-16)
- [docs.datadoghq.com/llm_observability/](https://docs.datadoghq.com/llm_observability/) (Datadog official docs, product header reads "Agent Observability", fetched 2026-07-16)
- [datadoghq.com/about/latest-news/press-releases/datadog-llm-observability-is-now-generally-available...](https://www.datadoghq.com/about/latest-news/press-releases/datadog-llm-observability-is-now-generally-available-to-help-businesses-monitor-improve-and-secure-generative-ai-applications/) (Datadog press release, 26 Jun 2024, fetched 2026-07-16)

**Confidence:** 📄 vendor-documented (all three pages are Datadog properties)

---

## Practice 2: Use Datadog's built-in evaluators for hallucination, prompt-injection, and PII detection — but know they count as LLM calls and add cost

**Do:** Enable out-of-the-box quality and security evaluators in the Datadog LLM Observability settings. These run automated checks for hallucination detection, prompt-injection threats, sensitive-data exposure (PII — Personally Identifiable Information — like emails and IP addresses), and topic clustering (a way to understand what categories of questions users are asking). You can also add custom LLM-as-a-judge evaluators (where a second AI model grades your first AI model's answers — GA as of late 2025).

**Why it matters (and what goes wrong without it):** Evaluators catch quality problems and security threats in production traffic that you would never see by reading logs. Prompt-injection detection is especially important: a single malicious user prompt can hijack your AI's behaviour if not caught — for example, a user could write a message that tricks your AI into ignoring its instructions.

**Caveat:** Each evaluation that calls an LLM to judge a response is itself an LLM call — it produces extra spans, extra tokens, and extra cost on top of the spans counted in Practice 1. 🕒 Evaluate whether the safety benefit justifies the per-span billing increase for your workload.

**Sources:**
- [docs.datadoghq.com/llm_observability/evaluations/](https://docs.datadoghq.com/llm_observability/evaluations/) (Datadog evaluators docs, fetched 2026-07-16)
- [docs.datadoghq.com/llm_observability/monitoring/cost/](https://docs.datadoghq.com/llm_observability/monitoring/cost/) (Datadog cost monitoring docs, fetched 2026-07-16)
- [datadoghq.com/about/latest-news/press-releases/datadog-llm-observability-is-now-generally-available...](https://www.datadoghq.com/about/latest-news/press-releases/datadog-llm-observability-is-now-generally-available-to-help-businesses-monitor-improve-and-secure-generative-ai-applications/) (Datadog press release, 26 Jun 2024, fetched 2026-07-16)

**Confidence:** 📄 vendor-documented

---

## Practice 3: Enable Amazon Bedrock Model Invocation Logging explicitly — it is OFF by default

⚠️ **WARNING:** Model Invocation Logging is **disabled by default**. Without enabling it you have zero record of what prompts users sent or what your model returned — critical for auditing, compliance, and debugging.

⚠️ **WARNING (IAM security):** If you are not familiar with AWS IAM policies, use the AWS Console wizard for Bedrock logging setup rather than writing policies by hand — it generates the correct policy for you. Do not copy generic S3 write policies from the internet; they may not include the account-scoping clause that prevents other AWS accounts from writing to your bucket. A misconfigured S3 bucket policy can grant unintended public write access to your logging bucket.

**Do:** In the AWS Bedrock console go to Settings → Model invocation logging and turn it on. Choose whether to send logs to CloudWatch Logs, S3, or both. Apply an S3 bucket policy granting `s3:PutObject` to the `bedrock.amazonaws.com` service principal (scoped to your account and region). For CloudWatch, create a log group and an IAM role that allows `logs:CreateLogStream` and `logs:PutLogEvents`. Logs capture the full request and response body (up to 100 KB inline; larger payloads stored as S3 objects) and all metadata fields including the caller's IAM ARN (the identifier for who made the request).

**Important limitation — which API are you using?** If you are calling Bedrock using the Converse API or InvokeModel API, invocation logging works. If you are using the newer Responses API (check your code for `responses.create()` or `client.responses`), logging will NOT capture those calls — the `bedrock-mantle` endpoint used by the Responses API is not covered by invocation logging. You would need an alternative approach such as CloudWatch custom metrics or an OpenTelemetry instrumentation layer. 🕒 Verify live at the AWS docs link whether this gap has been closed.

**Why it matters (and what goes wrong without it):** CloudWatch Logs Insights lets you run queries across invocation records — for example, summing input tokens by IAM principal to find which service or team is consuming the most quota. Without this logging, a prompt that caused harmful or incorrect output leaves no trace.

**Additional context (May 2026):** AWS added request-level usage attribution tags (team, project, environment) to `InvokeModel` and `InvokeModelWithResponseStream` in May 2026, enabling per-call cost attribution in invocation logs without requiring the Converse API.

**Sources:**
- [docs.aws.amazon.com/bedrock/latest/userguide/model-invocation-logging.html](https://docs.aws.amazon.com/bedrock/latest/userguide/model-invocation-logging.html) (AWS official docs, fetched 2026-07-16)
- [openobserve.ai/blog/monitoring-aws-bedrock/](https://openobserve.ai/blog/monitoring-aws-bedrock/) (OpenObserve, independent publisher, fetched 2026-07-16)

**Confidence:** ✅ independently-corroborated

---

## Practice 4: Monitor Amazon Bedrock with CloudWatch metrics under the `AWS/Bedrock` namespace — and alert on `InvocationThrottles` before users notice failures

**Do:** Amazon Bedrock automatically publishes runtime metrics to CloudWatch under the `AWS/Bedrock` namespace — no configuration required beyond what you set up in Practice 3. Key metrics to watch:

- `Invocations` — number of successful calls
- `InvocationLatency` — time in milliseconds from sending a request to receiving the last token
- `TimeToFirstToken` — how long until the first word of a streaming response arrives
- `InvocationThrottles` — requests that Bedrock rejected because you hit a quota limit (see WARNING below)
- `InvocationClientErrors` — errors caused by your code (bad request format, etc.)
- `InvocationServerErrors` — errors on Bedrock's side
- `InputTokenCount` and `OutputTokenCount` — how many tokens were consumed

Use the `ModelId` dimension to compare these metrics across different foundation models.

⚠️ **WARNING:** `InvocationThrottles` are silently excluded from the `Invocations` count. This means: if Bedrock throttles 200 of your requests, your `Invocations` count shows only the 800 successful ones — the 200 failures are invisible unless you watch `InvocationThrottles` separately. Your dashboard can show 0% errors while users are receiving no responses at all. Set a dedicated CloudWatch alarm on `InvocationThrottles` with a threshold of greater than 0 in a 1-minute period so your team knows when you are hitting token-per-minute (TPM) quota limits.

**Why it matters (and what goes wrong without it):** Throttles mean your users received no response. Catching them early lets you request a quota increase from AWS or add retry logic before customer impact becomes severe.

**Caveat:** The `EstimatedTPMQuotaUsage` metric is an approximation and does not reflect reservation-based token consumption that actually drives throttling decisions — AWS explicitly warns against using it as the sole indicator for capacity planning. 🕒 Verify the current set of available models and metric names, as new foundation models are added regularly.

**Sources:**
- [docs.aws.amazon.com/bedrock/latest/userguide/monitoring-runtime-metrics.html](https://docs.aws.amazon.com/bedrock/latest/userguide/monitoring-runtime-metrics.html) (AWS official docs, fetched 2026-07-16)
- [aws.amazon.com/blogs/mt/monitoring-generative-ai-applications-using-amazon-bedrock-and-amazon-cloudwatch-integration/](https://aws.amazon.com/blogs/mt/monitoring-generative-ai-applications-using-amazon-bedrock-and-amazon-cloudwatch-integration/) (AWS Cloud Operations Blog, fetched 2026-07-16)

**Confidence:** 📄 vendor-documented (both sources are AWS properties)

---

## Practice 5: Vertex AI Model Monitoring — know which tool applies to your use case before you start

**Are you monitoring a chatbot or text-generation application?** If yes, skip Model Monitoring v1 entirely. Go straight to the Gen AI Evaluation Service — Model Monitoring v1 is designed for traditional machine-learning models (image classifiers, tabular data predictors), not for LLM prompt and response quality. The Gen AI Evaluation Service (on GCP) offers batch evaluation and rubrics-driven evaluation and is the right tool for generative AI quality monitoring on Google Cloud.

**Do (only for teams running traditional ML models, not LLMs):** Vertex AI Model Monitoring v1 is Generally Available (GA — production-ready) and is designed for tabular, image classification, and regression models. It supports:

- Feature skew detection: catching cases where the data your model sees in production is drifting away from the data it was trained on
- Prediction drift: detecting when the model's feature attributions (which inputs most affect its outputs) are changing over time

This applies to online prediction endpoints, not to generative AI chat endpoints.

⚠️ **WARNING:** Vertex AI Model Monitoring is built for traditional ML models — it does not monitor the semantic quality of LLM outputs (hallucinations, tone, factuality) out of the box.

⚠️ **WARNING (Pre-GA):** Model Monitoring v2 is in Pre-GA status — Google's preview tier, available "as is" with potentially limited support. Do not rely on Pre-GA features for workloads where downtime or data loss would be costly. 🕒 Verify the current GA status of v2 and the Gen AI Evaluation Service's agent-evaluation feature before building on either.

**Why it matters (and what goes wrong without it):** Even when wrapping an LLM, your retrieval pipeline may receive inputs that drift away from what the model was tuned on. Monitoring feature distributions at the embedding or structured-input layer can catch data quality problems before they silently degrade responses — but only if you are running a traditional ML model alongside your LLM.

**Sources:**
- [docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/model-monitoring/overview](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/model-monitoring/overview) (Google Cloud official docs, fetched 2026-07-16) ⚠ PENDING-vertex-v1-ga — page returned navigation structure, not full GA/Pre-GA confirmation; panel notes confirm v1=GA and v2=Pre-GA from search results
- [cloud.google.com/blog/products/ai-machine-learning/how-to-evaluate-your-gen-ai-at-every-stage](https://cloud.google.com/blog/products/ai-machine-learning/how-to-evaluate-your-gen-ai-at-every-stage) (Google Cloud Blog, fetched 2026-07-16)

**Confidence:** 📄 vendor-documented (both sources are Google Cloud properties)

---

## Practice 6: Enable Microsoft Foundry observability tracing and monitoring (GA March 2026) — but disable playground evaluations before you start testing

⚠️ **WARNING (cost — do this first, before anything else):** Playground evaluations are **turned ON by default** and cost money for every test prompt — safety evaluations and risk evaluations are billed on consumption. **Disable them before you run any test prompts:** open the Foundry agents playground, find the **Metrics** button in the upper-right corner of the playground screen, and deselect all evaluators. If you run test prompts without doing this first, charges will accrue immediately.

**Do:** Microsoft Foundry's Evaluation, Monitoring, and Tracing capabilities reached Generally Available (GA) status on 17 March 2026. Tracing is built on OpenTelemetry (an open standard for collecting telemetry data) and integrates with Azure Monitor Application Insights. Enable it for your Foundry project to get automatic distributed traces across LLM calls, tool invocations, agent decisions, and retrieval steps — no manual logging calls required.

Set up Diagnostic Settings on your Azure OpenAI resource to route resource logs and metrics to a Log Analytics workspace. Then use KQL (Kusto Query Language — Azure's query language for Log Analytics) to query `AzureDiagnostics` for request and response metadata.

**Why it matters (and what goes wrong without it):** The monitoring dashboard surfaces real-time token consumption, latency, error rates, and quality scores. Because evaluation results link directly to the underlying trace, you can click from a failing quality score straight to the exact LLM call that produced it — far faster than manually correlating log entries.

**Caveat:** Custom evaluators (LLM-as-a-Judge and code-based) were still in public preview at the March 2026 GA date. Additional monitoring capabilities were announced at Microsoft Build (May 2026); verify the current feature set at the link below — the March 2026 GA is the baseline, not the current ceiling. 🕒 Verify live whether custom evaluators have reached GA.

**Sources:**
- [learn.microsoft.com/en-us/azure/foundry/concepts/observability](https://learn.microsoft.com/en-us/azure/foundry/concepts/observability) (Microsoft Learn official docs, updated 2026-06-02, fetched 2026-07-16)
- [azurefeeds.com/2026/03/17/generally-available-evaluations-monitoring-and-tracing-in-microsoft-foundry/](https://azurefeeds.com/2026/03/17/generally-available-evaluations-monitoring-and-tracing-in-microsoft-foundry/) (AzureFeeds, independent publisher, fetched 2026-07-16)
- [learn.microsoft.com/en-us/azure/foundry-classic/openai/how-to/monitor-openai](https://learn.microsoft.com/en-us/azure/foundry-classic/openai/how-to/monitor-openai) (Microsoft Learn official docs, fetched 2026-07-16)

**Confidence:** ✅ independently-corroborated (Microsoft official docs + independent AzureFeeds summary of the GA announcement)

---

## Practice 7: Understand New Relic AI Monitoring's ingest-based pricing before enabling it for LLM workloads

⚠️ **WARNING (cost — read before enabling):** LLM traces are payload-heavy. Each trace can carry the full prompt and completion text — easily 5 to 50 KB per call. A team reported in March 2026 that adding New Relic AI Monitoring to a 4 TB/month agent workload pushed their monthly bill from roughly $1,400 to between $9,500 and $12,000. Model token counts in isolation are small, but prompts, context windows, and tool-call payloads add up fast under per-GB billing.

**Set a New Relic ingest alert before you enable AI Monitoring:** go to newrelic.com → Administration → Data Management → Alerts and set a monthly ingest cap. Without this step you will discover the cost on your next invoice.

**Do:** New Relic AI Monitoring went Generally Available on June 18, 2024. It captures LLM prompt and response pairs, token counts (prompt, completion, response), per-model latency, and user feedback signals. It integrates with OpenAI, Amazon Bedrock, and DeepSeek via APM agents — if your organisation already runs New Relic APM, no new instrumentation is required.

The platform offers a 100 GB/month free ingest allowance. Beyond that, rates vary by tier: approximately $0.30–$0.40/GB (Standard) and $0.50–$0.60/GB (Data Plus) above the free allowance, according to third-party sources. 🕒 **Verify live at newrelic.com/pricing** — these rates are from third-party guides, not New Relic's own published pricing page.

**Note on product tiers:** The core AI Monitoring product (LLM call tracking, token counts, prompt and response capture) has been GA since June 2024. Agentic AI Monitoring features (tracing multi-step agent workflows) were in preview as of February 2026. 🕒 Verify the current GA status of agentic-trace features before depending on them in production.

**Why it matters:** New Relic is a natural choice if your organisation already uses it for APM — you get LLM traces in the same dashboards as your existing services without deploying a separate tool. But the cost model is very different from LLM-native tools that bill per request rather than per GB of ingested data.

**Sources:**
- [docs.newrelic.com/docs/ai-monitoring/intro-to-ai-monitoring/](https://docs.newrelic.com/docs/ai-monitoring/intro-to-ai-monitoring/) (New Relic official docs, fetched 2026-07-16)
- [newrelic.com/platform/ai-observability](https://newrelic.com/platform/ai-observability) (New Relic official product page, fetched 2026-07-16)
- [last9.io/blog/new-relic-pricing/](https://last9.io/blog/new-relic-pricing/) (Last9, independent publisher, fetched 2026-07-16)

**Confidence:** ✅ independently-corroborated for feature set; pricing rates from third-party sources only — 🕒 verify live on New Relic's own pricing page

---

## Practice 8: Choosing between managed cloud and open-source LLM observability — match the tool to your situation

> **Before enabling New Relic AI Monitoring**, read the cost warning in Practice 7 and set an ingest alert first.

**A simple rule of thumb:** For a small application (under 1,000 LLM calls per day), open-source self-hosted tools have no per-request cost. For larger volumes, compare managed cloud costs against self-hosting engineering time.

**Do:** Managed cloud platforms (Datadog, New Relic, AWS CloudWatch) bundle LLM observability with existing APM infrastructure, delivering compliance certifications, pre-built dashboards, and low setup friction. Open-source tools (Langfuse, Arize Phoenix, SigNoz) offer self-hosting for data sovereignty, Apache 2.0 or similar licensing with no per-span or per-GB charges, and strong OpenTelemetry compatibility that avoids being locked into one vendor's instrumentation. The 2026 consensus in the LLM monitoring community is that both categories now support OpenTelemetry GenAI semantic conventions, so switching backends is more feasible than it was in 2024 — but migrating historical trace data and dashboards still carries real cost.

**Why it matters (and what goes wrong without thinking this through):** If your organisation already pays for Datadog or New Relic, adding LLM monitoring can look "free" until token-heavy traces multiply your ingest bill. Conversely, self-hosting Langfuse requires engineering time to run and maintain. The right answer depends on your team's existing tooling, compliance requirements, and expected trace volume.

**Compliance note:** Managed cloud compliance certifications — such as SOC 2 Type II (data security auditing standard), HIPAA BAA (required for handling healthcare data in the US), and FedRAMP (required for US government use) — are an important differentiator for regulated workloads. SOC 2 Type II is standard for Datadog and New Relic enterprise tiers; HIPAA BAA and FedRAMP availability must be confirmed per tier and plan. 🕒 Verify compliance certifications before committing if these matter for your use case.

**Sources:**
- [lakefs.io/blog/llm-observability-tools/](https://lakefs.io/blog/llm-observability-tools/) (LakeFS blog, independent publisher, fetched 2026-07-16)
- [confident-ai.com/knowledge-base/compare/best-ai-observability-tools-2026](https://www.confident-ai.com/knowledge-base/compare/best-ai-observability-tools-2026) (Confident AI, independent publisher, fetched 2026-07-16)
- [last9.io/blog/new-relic-pricing/](https://last9.io/blog/new-relic-pricing/) (Last9, independent publisher, fetched 2026-07-16)

**Confidence:** ✅ independently-corroborated

---

## Held pending fixes (not confirmed — check before acting)

- Datadog per-span pricing: the exact per-span dollar amount is not published on Datadog's own docs pages. The May 2026 tier structure (40K spans free; Pro $160/month for 100K spans) comes from third-party sources. 🕒 Verify live at datadoghq.com/pricing. ⚠ PENDING-datadog-pricing
- New Relic AI Monitoring per-GB pricing: conflicting rates across third-party sources ($0.30–$0.40/GB Standard, $0.50–$0.60/GB Data Plus); not confirmed from first-party docs. ⚠ PENDING-newrelic-pricing
- Vertex AI Model Monitoring v1 GA / v2 Pre-GA confirmation: fetched docs page returned only navigation structure; panel confirmed v1=GA, v2=Pre-GA from search results. ⚠ PENDING-vertex-v1-ga

---

## CHANGELOG

### From technical entry (grading corrections already applied before this re-level)

1. **KILL-M1 (Skeptic):** Removed fabricated Langfuse/LangSmith cost comparison ($3,451/$5,170 at 50M spans, 5 users) — not found in any of the three cited sources (lakefs.io, confident-ai.com, last9.io).
2. **KILL-1 (Timekeeper):** Updated Datadog product name — the product is now marketed as "Agent Observability" while the env var (`DD_LLMOBS_ENABLED`) and docs URL (`llm_observability/`) retain the older paths. Added May 2026 per-span pricing tiers (40K spans/month free; Pro from $160/month for 100K spans).
3. **KILL-2 (Timekeeper):** Fixed New Relic GA date — New Relic AI Monitoring went GA June 18, 2024. Removed "GA status is unconfirmed" language. Updated pricing to a range ($0.30–$0.40/GB Standard, $0.50–$0.60/GB Data Plus) to reflect conflicting third-party sources.
4. **FIX-M2 (Skeptic):** Added Datadog evaluators docs page citation for the evaluator list.
5. **FIX-4 (Timekeeper):** Added note that Build 2026 (May 2026) added capabilities to Azure AI Foundry beyond the March 2026 GA baseline.
6. **FIX-5 (Timekeeper):** Changed "Preview" to "Pre-GA" for Vertex AI Model Monitoring v2, with Google's specific language.
7. **FIX-6 (Timekeeper):** Added AWS May 2026 request-level usage attribution expansion for `InvokeModel` and `InvokeModelWithResponseStream`.
8. **FIX-7 (Timekeeper):** Changed New Relic per-GB rates to a range — the draft's $0.40/$0.60 figures came from an outlier source.
9. **KILL-MP-2 (Beginner — applied to technical entry):** Moved Azure Foundry playground evaluations WARNING above the Do section. Added explicit navigation path: Metrics button in upper-right corner of playground → deselect all evaluators.
10. **KILL-MP-4 (Beginner — applied to technical entry):** Added AWS Console wizard recommendation for IAM setup and warning against copying generic S3 write policies from the internet.
11. **FLAG-5 (Timekeeper):** Added note distinguishing New Relic AI Monitoring (GA June 2024) from Agentic AI Monitoring (preview Feb 2026).

### Beginner re-level applied (re-leveled from the 2026-07-16 technical entry; facts unchanged)

12. **KILL-MP-1:** Added concrete budget example for Datadog cost: "if your app handles 10,000 LLM calls per day and Datadog creates two spans per call, you have 20,000 spans/day." Added explicit budget alert instruction (Plan & Usage → Budget Alerts) at the top of Practice 1, before the Do section.
13. **KILL-MP-2:** Moved Azure Foundry playground-evaluations WARNING above the Do section in Practice 6, as the first thing the reader sees. Rewrote to make the disable path unambiguous: Metrics button → upper-right corner of the playground screen → deselect all evaluators.
14. **KILL-MP-3:** Added forward reference at the top of Practice 8 directing readers to Practice 7's cost warning before enabling New Relic AI Monitoring. Added instruction to set a New Relic ingest alert (Administration → Data Management → Alerts) in Practice 7 before enabling AI Monitoring.
15. **KILL-MP-4:** Added guardrail at the top of Practice 3's Do section: use the AWS Console wizard rather than writing IAM policies by hand; do not copy generic S3 write policies from the internet.
16. **FIX-MP-1:** Defined APM on first use: "APM (Application Performance Monitoring) is a paid Datadog add-on. Check your current Datadog plan before enabling LLM Observability — you may need to upgrade."
17. **FIX-MP-2:** Restructured Practice 5 to lead with the redirect: "If you are monitoring a chatbot or other generative AI application, skip to the Gen AI Evaluation Service — Model Monitoring v1 is for traditional machine-learning models, not for LLM prompt/response quality."
18. **FIX-MP-3:** Defined KQL on first use in Practice 6: "KQL (Kusto Query Language — Azure's query language for Log Analytics)."
19. **FIX-MP-4:** Explained the bedrock-mantle endpoint consequence in plain terms in Practice 3: if you use `responses.create()` or `client.responses`, logging will NOT capture those calls.
20. **FIX-MP-5:** Confirmed the $3,451/$5,170 stat (KILL-M1) is not in the technical entry and was not re-introduced. Replaced Practice 8's comparison with the simple rule: "For a small application (under 1,000 LLM calls per day), open-source self-hosted tools have no per-request cost. For larger volumes, compare managed cloud costs against self-hosting engineering time."
21. **Vocabulary section added:** Defined "observability," "trace," "span," and "APM" at the top of the document for readers new to these concepts.
22. **FLAG-MP-1:** Added plain-language parentheticals for SOC 2 Type II, HIPAA BAA, and FedRAMP in Practice 8.
23. **FLAG-MP-2:** Expanded the InvocationThrottles WARNING with the plain consequence: "your `Invocations` count shows only the 800 successful ones — the 200 failures are invisible."
