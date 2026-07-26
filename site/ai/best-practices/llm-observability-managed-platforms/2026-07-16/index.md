# LLM Observability and Monitoring — Managed Cloud Platforms — Best Practices (as of 16 Jul 2026)

> How to instrument and monitor LLM workloads on Datadog Agent Observability, New Relic AI Monitoring, AWS Bedrock + CloudWatch, GCP Vertex AI, and Azure AI Foundry — with trade-offs versus open-source alternatives.


# LLM Observability and Monitoring: Managed Cloud Platforms (as of 16 Jul 2026)

> **Grading note.** A dated snapshot — accurate as of **16 Jul 2026**, frozen here and kept as a permanent archive entry. Research-drafted by a pupil, graded by the 3-lens panel + sensei. Corrections applied inline; unverifiable gaps marked ⚠ PENDING (#issue) — never guessed.

## How to read the labels
- ✅ **independently-corroborated** — 2+ independent publishers
- 📄 **vendor-documented** — official docs only (authoritative, single source)
- ⚠️ **WARNING** — a default that can cost money, break the machine, or remove a safety net
- 🕒 **verify live** — fast-moving (versions/prices/quotas); check the current value

---

## Practice 1: Enable Datadog Agent Observability (formerly "LLM Observability") by setting `DD_LLMOBS_ENABLED=1`

**Do:** Install the `ddtrace` package (Python), `dd-trace` (Node.js), or `dd-trace-java` (Java 8+), set the environment variables `DD_LLMOBS_ENABLED=1`, `DD_API_KEY`, and `DD_SITE`, then start your application with the tracer. Datadog will automatically capture LLM spans — including input/output tokens, latency, model ID, and errors — for each call to supported providers (OpenAI, Anthropic, AWS Bedrock, Vertex AI, LangChain, and others).

> **Product name note (2026):** The product is now marketed as **"Agent Observability"** (visible in the Datadog console and product pages). The environment variable `DD_LLMOBS_ENABLED` and the docs URL (`docs.datadoghq.com/llm_observability/`) retain the older `llm_observability` path. Both names refer to the same product; use `DD_LLMOBS_ENABLED=1` to activate it regardless of the displayed name.

**Why (beginner):** Without instrumentation you have no visibility into what prompts your app sends, how long they take, or when they fail. Datadog Agent Observability went GA on 26 June 2024 and groups every step of a multi-model chain into a single trace so you can pinpoint which call caused a slow or broken response.

**Caveat / contested:** Pricing changed effective **May 1, 2026**: free plan includes 40,000 LLM spans/month; Pro plan starts at $160/month for 100,000 spans. 🕒 **verify live** at datadoghq.com/pricing — these tiers are recent and may change. The product requires an existing Datadog APM subscription; it is not supported on Datadog government-region sites.

⚠️ **WARNING (cost):** Per-span billing scales directly with traffic. Set a Datadog budget alert (Plan & Usage → Budget Alerts) before enabling in production so you receive notification before costs exceed your threshold.

**Sources:**
- [docs.datadoghq.com/llm_observability/setup/](https://docs.datadoghq.com/llm_observability/setup/) (Datadog official docs, fetched 2026-07-16)
- [docs.datadoghq.com/llm_observability/](https://docs.datadoghq.com/llm_observability/) (Datadog official docs, product header reads "Agent Observability", fetched 2026-07-16)
- [datadoghq.com/about/latest-news/press-releases/datadog-llm-observability-is-now-generally-available...](https://www.datadoghq.com/about/latest-news/press-releases/datadog-llm-observability-is-now-generally-available-to-help-businesses-monitor-improve-and-secure-generative-ai-applications/) (Datadog press release, 26 Jun 2024, fetched 2026-07-16)

**Confidence:** 📄 vendor-documented (all three pages are Datadog properties)

---

## Practice 2: Use Datadog's built-in evaluators for hallucination, prompt-injection, and PII detection — but know they count as LLM calls and add cost

**Do:** Enable out-of-the-box quality and security evaluators in the Datadog LLM Observability settings. These run automated checks for hallucination detection, prompt-injection threats, sensitive-data exposure (PII, emails, IP addresses), and topic clustering to understand what users ask. You can also add custom LLM-as-a-judge evaluators (GA as of late 2025).

**Why (beginner):** Evaluators catch quality problems and security threats in production traffic that you would never see by reading logs. Prompt-injection detection is especially important: a single malicious user prompt can hijack your LLM's behaviour if not caught.

**Caveat / contested:** Each evaluation that calls an LLM to judge a response is itself an LLM call — it produces extra spans, extra tokens, and extra cost. 🕒 Evaluate whether the safety benefit justifies the per-span billing increase for your workload.

**Sources:**
- [docs.datadoghq.com/llm_observability/evaluations/](https://docs.datadoghq.com/llm_observability/evaluations/) (Datadog evaluators docs, fetched 2026-07-16)
- [docs.datadoghq.com/llm_observability/monitoring/cost/](https://docs.datadoghq.com/llm_observability/monitoring/cost/) (Datadog cost monitoring docs, fetched 2026-07-16)
- [datadoghq.com/about/latest-news/press-releases/datadog-llm-observability-is-now-generally-available...](https://www.datadoghq.com/about/latest-news/press-releases/datadog-llm-observability-is-now-generally-available-to-help-businesses-monitor-improve-and-secure-generative-ai-applications/) (Datadog press release, 26 Jun 2024, fetched 2026-07-16)

**Confidence:** 📄 vendor-documented

---

## Practice 3: Enable Amazon Bedrock Model Invocation Logging explicitly — it is OFF by default

**Do:** In the AWS Bedrock console go to Settings → Model invocation logging and turn it on. Choose whether to send logs to CloudWatch Logs, S3, or both. Apply an S3 bucket policy granting `s3:PutObject` to the `bedrock.amazonaws.com` service principal (scoped to your account and region). For CloudWatch, create a log group and an IAM role that allows `logs:CreateLogStream` and `logs:PutLogEvents`. Logs capture the full request/response body (up to 100 KB inline; larger payloads stored as S3 objects) and all metadata fields including the caller's IAM ARN.

⚠️ **WARNING:** Model Invocation Logging is **disabled by default**. Without enabling it you have zero record of what prompts users sent or what your model returned — critical for audit, compliance, and debugging.

⚠️ **WARNING (IAM):** S3 bucket policy misconfiguration can expose your logging bucket to unintended write access. Use the **AWS Console wizard** for Bedrock logging setup rather than writing policies by hand — it generates the correct account- and region-scoped policy. Do not copy generic S3 write policies from the internet; they may omit the account-scoping condition that prevents other AWS accounts from writing to your bucket.

**Why (beginner):** CloudWatch Logs Insights lets you run queries across invocation records — for example, summing input tokens by IAM principal to find which service or team is consuming the most quota.

**Caveat / contested:** The `bedrock-mantle` endpoint (used by the Responses API) is not captured by invocation logging as of the documentation fetched today — only the `bedrock-runtime` endpoint is covered. If your application uses the Responses API (`responses.create()` / `client.responses`), invocation logging will NOT capture those calls; you need an alternative approach such as CloudWatch custom metrics or an OTel instrumentation layer. 🕒 Verify live whether mantle endpoint coverage has been added.

**Additional context (May 2026):** AWS added request-level usage attribution tags (team, project, environment) to `InvokeModel` and `InvokeModelWithResponseStream` in May 2026, enabling per-call cost attribution in invocation logs without requiring the Converse API. The `bedrock-mantle` gap persists — verify live at the AWS docs link.

**Sources:**
- [docs.aws.amazon.com/bedrock/latest/userguide/model-invocation-logging.html](https://docs.aws.amazon.com/bedrock/latest/userguide/model-invocation-logging.html) (AWS official docs, fetched 2026-07-16)
- [openobserve.ai/blog/monitoring-aws-bedrock/](https://openobserve.ai/blog/monitoring-aws-bedrock/) (OpenObserve, independent publisher, fetched 2026-07-16)

**Confidence:** ✅ independently-corroborated

---

## Practice 4: Monitor Amazon Bedrock with CloudWatch metrics under the `AWS/Bedrock` namespace — and alert on `InvocationThrottles` before users notice failures

**Do:** Amazon Bedrock automatically publishes runtime metrics to CloudWatch under the `AWS/Bedrock` namespace — no configuration required. Key metrics to watch: `Invocations` (successful call count), `InvocationLatency` (milliseconds, time to last token), `TimeToFirstToken` (streaming latency), `InvocationThrottles` (throttled requests — these are NOT counted as `Invocations`), `InvocationClientErrors`, `InvocationServerErrors`, `InputTokenCount`, and `OutputTokenCount`. Dimension by `ModelId` to compare across foundation models.

⚠️ **WARNING:** `InvocationThrottles` are silently excluded from the `Invocations` count. This means: if Bedrock throttles 200 of your requests, your `Invocations` count shows only the 800 successful ones — the 200 failures are invisible unless you watch `InvocationThrottles` separately. Set a dedicated CloudWatch alarm on `InvocationThrottles` with a threshold of > 0 in a 1-minute period so your team knows when you are hitting token-per-minute (TPM) quota limits.

**Why (beginner):** Throttles mean your users received no response. Catching them early lets you request a quota increase or add retry logic before customer impact becomes severe.

**Caveat / contested:** The `EstimatedTPMQuotaUsage` metric is an approximation and does not reflect reservation-based token consumption that actually drives throttling decisions — AWS explicitly warns against using it as the sole indicator for capacity planning. 🕒 Verify the current set of available models and metric names, as new foundation models are added regularly.

**Sources:**
- [docs.aws.amazon.com/bedrock/latest/userguide/monitoring-runtime-metrics.html](https://docs.aws.amazon.com/bedrock/latest/userguide/monitoring-runtime-metrics.html) (AWS official docs, fetched 2026-07-16)
- [aws.amazon.com/blogs/mt/monitoring-generative-ai-applications-using-amazon-bedrock-and-amazon-cloudwatch-integration/](https://aws.amazon.com/blogs/mt/monitoring-generative-ai-applications-using-amazon-bedrock-and-amazon-cloudwatch-integration/) (AWS Cloud Operations Blog, fetched 2026-07-16)

**Confidence:** 📄 vendor-documented (both sources are AWS properties)

---

## Practice 5: Use Vertex AI Model Monitoring v1 (GA) for tabular/embedding drift — but understand it does not cover generative LLM prompt/response quality

**Do:** For teams monitoring a generative LLM chatbot or text-generation application: Vertex AI Model Monitoring v1 does **not** apply to your use case — skip to the Gen AI Evaluation Service instead. Model Monitoring v1 is Generally Available and designed for traditional ML models (tabular, image classification, regression): it supports feature skew detection (production data diverging from training distribution) and prediction drift (feature attributions changing over time) for online prediction endpoints. For GenAI quality evaluation on GCP, use the separate Gen AI Evaluation Service (batch evaluation and rubrics-driven evaluation are available; agent evaluation is in Preview as of 2026). Model Monitoring v2 is in **Pre-GA status** (Google's preview tier — available "as is" with potentially limited support; not recommended for SLA-bound or sensitive-data workloads).

⚠️ **WARNING:** Vertex AI Model Monitoring is built for traditional ML models — it does not monitor the semantic quality of LLM outputs (hallucinations, tone, factuality) out of the box.

**Why (beginner):** Even when wrapping an LLM, your retrieval pipeline may receive inputs that drift away from what the model was tuned on. Monitoring feature distributions at the embedding or structured-input layer can catch data quality problems before they silently degrade responses.

**Caveat / contested:** The GA/Pre-GA distinction between v1 and v2 matters for production use. Do not rely on Pre-GA features for SLA-bound workloads. 🕒 Verify current GA status of v2 and the Gen AI Evaluation Service agent-evaluation feature before building on either.

**Sources:**
- [docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/model-monitoring/overview](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/model-monitoring/overview) (Google Cloud official docs, fetched 2026-07-16) ⚠ PENDING-vertex-v1-ga — page returned navigation structure, not full GA/Pre-GA confirmation; panel notes confirm v1=GA and v2=Pre-GA from search results
- [cloud.google.com/blog/products/ai-machine-learning/how-to-evaluate-your-gen-ai-at-every-stage](https://cloud.google.com/blog/products/ai-machine-learning/how-to-evaluate-your-gen-ai-at-every-stage) (Google Cloud Blog, fetched 2026-07-16)

**Confidence:** 📄 vendor-documented (both sources are Google Cloud properties)

---

## Practice 6: Enable Microsoft Foundry observability tracing and monitoring (GA March 2026) — but disable playground evaluations before you start testing

**Do:** Microsoft Foundry's Evaluation, Monitoring, and Tracing capabilities reached GA on 17 March 2026. Tracing is OpenTelemetry-based and integrates with Azure Monitor Application Insights. Enable it for your Foundry project to get automatic distributed traces across LLM calls, tool invocations, agent decisions, and retrieval steps — no manual logging calls required. Set up Diagnostic Settings on your Azure OpenAI resource to route resource logs and metrics to a Log Analytics workspace, then use KQL (Kusto Query Language, Azure's query language for Log Analytics) to query `AzureDiagnostics` for request/response metadata.

⚠️ **WARNING (cost — read before you start):** Playground evaluations are **enabled by default** for all Foundry projects and are billed on consumption (safety evaluations, risk evaluations). If you run test prompts in the Foundry agents playground without disabling evaluators, charges will accrue immediately. **Disable evaluators first:** open the Foundry agents playground, find the **Metrics** button in the upper-right corner of the playground screen, and deselect all evaluators before running any test prompts.

**Why (beginner):** The monitoring dashboard surfaces real-time token consumption, latency, error rates, and quality scores. Because evaluation results link directly to the underlying trace, you can click from a failing quality score straight to the exact LLM call that produced it — far faster than manually correlating log entries.

**Caveat / contested:** Custom evaluators (LLM-as-a-Judge and code-based) were still in public preview at the March 2026 GA date. Additional monitoring capabilities were announced at Microsoft Build (May 2026); verify the current feature set at [learn.microsoft.com/azure/foundry/concepts/observability](https://learn.microsoft.com/en-us/azure/foundry/concepts/observability) — the March 2026 GA is the baseline, not the current ceiling. 🕒 Verify live whether custom evaluators have reached GA.

**Sources:**
- [learn.microsoft.com/en-us/azure/foundry/concepts/observability](https://learn.microsoft.com/en-us/azure/foundry/concepts/observability) (Microsoft Learn official docs, updated 2026-06-02, fetched 2026-07-16)
- [azurefeeds.com/2026/03/17/generally-available-evaluations-monitoring-and-tracing-in-microsoft-foundry/](https://azurefeeds.com/2026/03/17/generally-available-evaluations-monitoring-and-tracing-in-microsoft-foundry/) (AzureFeeds, independent publisher, fetched 2026-07-16)
- [learn.microsoft.com/en-us/azure/foundry-classic/openai/how-to/monitor-openai](https://learn.microsoft.com/en-us/azure/foundry-classic/openai/how-to/monitor-openai) (Microsoft Learn official docs, fetched 2026-07-16)

**Confidence:** ✅ independently-corroborated (Microsoft official docs + independent AzureFeeds summary of the GA announcement)

---

## Practice 7: Understand New Relic AI Monitoring's ingest-based pricing before adopting it for high-volume LLM workloads

**Do:** New Relic AI Monitoring (GA: **June 18, 2024**) captures LLM prompt/response pairs, token counts (prompt, completion, response), per-model latency, and user feedback signals. It integrates with OpenAI, Amazon Bedrock, and DeepSeek via APM agents with no new instrumentation required if you already run New Relic APM. The platform offers a 100 GB/month free ingest allowance; beyond that, rates vary by tier: approximately $0.30–$0.40/GB (Standard) and $0.50–$0.60/GB (Data Plus) above the free allowance per third-party sources — 🕒 **verify live at newrelic.com/pricing** as these rates are from third-party guides, not New Relic's own published pricing page.

**Note on New Relic product tiers:** The core AI Monitoring product (LLM call tracking, token counts, prompt/response capture) is GA since June 2024. Agentic AI Monitoring features (multi-step agent workflow tracing) were in preview as of Feb 2026 — verify current GA status before depending on agentic-trace features in production.

⚠️ **WARNING (cost):** LLM traces are payload-heavy. Each trace can carry the full prompt and completion text — easily 5–50 KB per call. A team reported in March 2026 that adding New Relic AI Monitoring to a 4 TB/month agent workload pushed their bill from ~$1,400/month to $9,500–$12,000/month. Model token counts in isolation are small, but prompts + context windows + tool-call payloads add up fast under per-GB billing. Set a New Relic ingest alert (Administration → Data Management → Alerts) before enabling AI Monitoring.

**Why (beginner):** New Relic is a natural choice if your organisation already uses it for APM — you get LLM traces in the same dashboards as your existing services without deploying a separate tool. But the cost model is very different from LLM-native tools that bill per request rather than per GB of ingested data.

**Caveat / contested:** Third-party pricing guides report conflicting per-GB rates ($0.30–$0.40/GB Standard, $0.50–$0.60/GB Data Plus); none were confirmed from New Relic's own published pricing page this run. The cost example ($1,400→$9,500–$12,000/month) was reported in March 2026 but cannot be independently sourced. 🕒 Verify live on newrelic.com/pricing before budgeting.

**Sources:**
- [docs.newrelic.com/docs/ai-monitoring/intro-to-ai-monitoring/](https://docs.newrelic.com/docs/ai-monitoring/intro-to-ai-monitoring/) (New Relic official docs, fetched 2026-07-16)
- [newrelic.com/platform/ai-observability](https://newrelic.com/platform/ai-observability) (New Relic official product page, fetched 2026-07-16)
- [last9.io/blog/new-relic-pricing/](https://last9.io/blog/new-relic-pricing/) (Last9, independent publisher, fetched 2026-07-16)

**Confidence:** ✅ independently-corroborated for feature set; pricing rates from third-party sources only — 🕒 verify live on New Relic's own pricing page

---

## Practice 8: When choosing between managed cloud and open-source LLM observability, match the tool's billing model to your trace volume — not just your existing vendor

**Do:** Managed cloud platforms (Datadog, New Relic, AWS CloudWatch) bundle LLM observability with existing APM infrastructure, delivering compliance certifications (SOC 2 Type II, HIPAA, FedRAMP — availability varies by tier and platform 🕒 verify), pre-built dashboards, and low setup friction. Open-source tools (Langfuse, Arize Phoenix, SigNoz) offer self-hosting for data sovereignty, Apache 2.0 or similar licensing with no per-span or per-GB charges, and strong OpenTelemetry compatibility that avoids instrumentation lock-in. The 2026 consensus in the LLM monitoring community is that both categories now support OpenTelemetry GenAI semantic conventions, so switching backends is more feasible than it was in 2024 — but migrating historical trace data and dashboards still carries real cost.

**Why (beginner):** If your organisation already pays for Datadog or New Relic, adding LLM monitoring looks "free" — until token-heavy traces multiply your ingest bill. Conversely, self-hosting Langfuse requires engineering time to run and maintain. The right answer depends on your team's existing tooling, compliance requirements, and expected trace volume.

**Caveat / contested:** Third-party cost comparisons show significant variation depending on assumptions. Managed cloud compliance certifications (SOC 2 Type II is standard for Datadog and New Relic enterprise; HIPAA BAA and FedRAMP availability must be confirmed per-tier) are an important differentiator for regulated workloads. 🕒 Verify compliance certs before committing.

**Sources:**
- [lakefs.io/blog/llm-observability-tools/](https://lakefs.io/blog/llm-observability-tools/) (LakeFS blog, independent publisher, fetched 2026-07-16)
- [confident-ai.com/knowledge-base/compare/best-ai-observability-tools-2026](https://www.confident-ai.com/knowledge-base/compare/best-ai-observability-tools-2026) (Confident AI, independent publisher, fetched 2026-07-16)
- [last9.io/blog/new-relic-pricing/](https://last9.io/blog/new-relic-pricing/) (Last9, independent publisher, fetched 2026-07-16)

**Confidence:** ✅ independently-corroborated

---

## Held pending fixes (not publish-ready)

- Datadog per-span pricing: exact per-span dollar amount not published on Datadog's own docs pages. May 2026 tier structure (40K spans free; Pro $160/month for 100K spans) comes from third-party sources — 🕒 verify live at datadoghq.com/pricing. ⚠ PENDING-datadog-pricing
- New Relic AI Monitoring per-GB pricing: conflicting rates across third-party sources ($0.30–$0.40/GB Standard, $0.50–$0.60/GB Data Plus); not confirmed from first-party docs. ⚠ PENDING-newrelic-pricing
- Vertex AI Model Monitoring v1 GA / v2 Pre-GA confirmation: fetched docs page returned only navigation structure; panel confirmed v1=GA, v2=Pre-GA from search results. ⚠ PENDING-vertex-v1-ga

## CHANGELOG (grading → this entry)

1. **KILL-M1 (Skeptic):** Removed fabricated Langfuse/LangSmith cost comparison ($3,451/$5,170 at 50M spans, 5 users) — not found in any of the three cited sources (lakefs.io, confident-ai.com, last9.io).
2. **KILL-1 (Timekeeper):** Updated Datadog product name — the product is now marketed as "Agent Observability" while the env var (`DD_LLMOBS_ENABLED`) and docs URL (`llm_observability/`) retain the older paths. Added May 2026 per-span pricing tiers (40K spans/month free; Pro from $160/month for 100K spans).
3. **KILL-2 (Timekeeper):** Fixed New Relic GA date — New Relic AI Monitoring went GA June 18, 2024. Removed "GA status is unconfirmed" language. Updated pricing to a range ($0.30–$0.40/GB Standard, $0.50–$0.60/GB Data Plus) to reflect conflicting third-party sources.
4. **FIX-M2 (Skeptic):** Added Datadog evaluators docs page citation (`docs.datadoghq.com/llm_observability/evaluations/`) for the evaluator list — the evaluators are not documented on the cost monitoring page cited in the original draft.
5. **FIX-4 (Timekeeper):** Added note that Build 2026 (May 2026) added capabilities to Azure AI Foundry beyond the March 2026 GA baseline.
6. **FIX-5 (Timekeeper):** Changed "Preview" to "Pre-GA" for Vertex AI Model Monitoring v2, with Google's specific language ("available as is, might have limited support").
7. **FIX-6 (Timekeeper):** Added AWS May 2026 request-level usage attribution expansion for `InvokeModel` and `InvokeModelWithResponseStream`. The `bedrock-mantle` coverage gap persists.
8. **FIX-7 (Timekeeper):** Changed New Relic per-GB rates to a range ($0.30–$0.40/GB Standard, $0.50–$0.60/GB Data Plus) — the draft's $0.40/$0.60 figures came from an outlier source.
9. **KILL-MP-2 (Beginner — applied to technical entry):** Moved Azure Foundry playground evaluations WARNING above the Do section. Added explicit navigation path: Metrics → upper-right corner of playground → deselect all evaluators.
10. **KILL-MP-4 (Beginner — applied to technical entry):** Added AWS Console wizard recommendation for IAM setup and warning against copying generic S3 write policies from the internet.
11. **FLAG-5 (Timekeeper):** Added note distinguishing New Relic AI Monitoring (GA June 2024) from Agentic AI Monitoring (preview Feb 2026).

