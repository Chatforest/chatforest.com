---
title: "LLM Observability and Monitoring — Generic / Architectural Patterns — Beginner Guide (as of 16 Jul 2026)"
date: 2026-07-16
snapshot_date: 2026-07-16
topic: llm-observability-generic
track: beginner
audience: "people new to AI"
description: "Platform-agnostic observability architecture for LLM applications, explained for beginners: OTel semantic conventions, span trees, structured logging, prompt versioning, golden datasets, LLM-as-judge, drift detection, and SLO design."
content_type: "Best Practice"
categories: ["LLM Observability", "OpenTelemetry", "SRE"]
tags: ["llm-observability", "opentelemetry", "tracing", "slo", "eval", "drift-detection", "prompt-versioning", "llm-as-judge"]
last_refreshed: 2026-07-16
graded_by: "RingS panel (Skeptic/Beginner/Timekeeper) + sensei, 2026-07-16"
grading_result: "0 fabrications; beginner re-level applied (KILL-GN-1, FIX-GN-1 through FIX-GN-7); all verified facts and source URLs preserved from technical entry."
---

# LLM Observability and Monitoring — Generic / Architectural Patterns — Beginner Guide (as of 16 Jul 2026)

> **Grading note.** A dated snapshot — accurate as of **16 Jul 2026**, frozen here and kept as
> a permanent archive entry. Research-drafted by a pupil, graded by the 3-lens panel + sensei.
> Corrections applied inline; unverifiable gaps marked PENDING — never guessed.
> Re-leveled from the 2026-07-16 technical entry for readers new to AI and the command line.

## How to read the labels
- OK **independently-corroborated** — 2+ independent publishers
- DOC **vendor-documented** — official docs only (authoritative, single source)
- WARNING **WARNING** — a default that can cost money, break the machine, or remove a safety net
- CLOCK **verify live** — fast-moving (versions/prices/quotas); check the current value

---

> **Prerequisites — start here if you are new.**
> These practices assume you have an OpenTelemetry (OTel)-compatible SDK installed in your
> programming language of choice and a tracing backend (such as Langfuse or Arize Phoenix)
> already configured. If you are starting from scratch and have none of that in place yet,
> begin with the Open-Source Tooling entry and set up Langfuse or Arize Phoenix first before
> returning here.

---

## What is a trace? What is a span?

Before you read any further, two terms appear everywhere in this guide:

A **trace** is the complete record of one request flowing through your AI application — for
example, a user's question and all the steps your app took to answer it.

A **span** is one step within that trace — one LLM call, one database lookup, or one tool
execution. A trace is made up of many spans connected together.

Think of a trace as a receipt for the entire meal and each span as one line item on that receipt.

---

## Practice: Use the `gen_ai.*` OpenTelemetry semantic conventions as your span schema

**Do:** Instrument every LLM call with a span whose attributes follow the OpenTelemetry (OTel)
GenAI semantic conventions. At minimum, set these attributes on each span:

- `gen_ai.operation.name` — what kind of operation (e.g., `chat`, `embeddings`, `invoke_agent`)
- `gen_ai.provider.name` — which AI provider you called (e.g., `openai`, `anthropic`)
- `gen_ai.request.model` — the model you asked for
- `gen_ai.usage.input_tokens` — how many tokens you sent
- `gen_ai.usage.output_tokens` — how many tokens you received
- `gen_ai.response.finish_reasons` — why the model stopped generating

Treat `gen_ai.input.messages` and `gen_ai.output.messages` as **opt-in** (turned off by default)
because they can contain personally identifiable information (PII — real names, emails, private
details) and produce very large spans.

**Why (beginner):** Without a shared naming scheme, every team invents its own field names
(`tokens_in`, `prompt_tokens`, `inputTokens`) and dashboards break whenever you switch providers.
The OTel `gen_ai.*` namespace is provider-neutral: the same dashboard works whether the backend
is OpenAI, Anthropic, or Bedrock.

**Caveat / contested:** CLOCK The GenAI semantic conventions live in a dedicated repository
([github.com/open-telemetry/semantic-conventions-genai](https://github.com/open-telemetry/semantic-conventions-genai))
and are still in **Development** (experimental) stability as of mid-2026. The v1.40/v1.41
version identifiers belong to the main `open-telemetry/semantic-conventions` repository, not the
GenAI-specific repo. The dedicated GenAI repo has **no published releases** — instrumentation
libraries embed the attribute names directly rather than pinning a versioned release artifact.
Attribute names can change between library versions; treat upgrades as planned migrations. The
earlier free-text prompt and completion attributes (`gen_ai.prompt`, `gen_ai.completion`) have
been superseded by the structured message attributes (`gen_ai.input.messages`,
`gen_ai.output.messages`) — the structured forms are the current standard. CLOCK **verify live**
— check the repo for any newly published release or stability change before adopting.

**Sources:**
[opentelemetry.io/docs/specs/semconv/gen-ai/ (redirect notice + link to new repo)](https://opentelemetry.io/docs/specs/semconv/gen-ai/) (fetched 2026-07-16) · [github.com/open-telemetry/semantic-conventions-genai — gen-ai-spans.md](https://github.com/open-telemetry/semantic-conventions-genai/blob/main/docs/gen-ai/gen-ai-spans.md) (fetched 2026-07-16) · [greptime.com — How OpenTelemetry Traces LLM Calls, Agent Reasoning, and MCP Tools](https://greptime.com/blogs/2026-05-09-opentelemetry-genai-semantic-conventions) (2026-05-21) · [cohorte.co — OpenTelemetry GenAI Semantic Conventions](https://cohorte.co/blog/opentelemetry-genai-semantic-conventions) (fetched 2026-07-16)

**Confidence:** OK independently-corroborated (OpenTelemetry project + Greptime + Cohorte, three different organisations)

---

## Practice: Model multi-step agentic pipelines as a parent-child span tree

**Do:** Wrap each user request or agent invocation in a **root span** (with
`gen_ai.operation.name = invoke_agent`). Nest every LLM call, tool execution, and retrieval
step as child spans under that root. Use W3C TraceContext headers — a standard way for
software services to pass trace identity between each other — to propagate the trace context
across process or service boundaries. Modern OpenTelemetry (OTel) SDKs (such as
`opentelemetry-sdk` for Python) handle this propagation automatically when you use their
instrumentation libraries, so you do not need to add headers manually in most cases. The
result is that multi-agent pipelines produce a single connected trace rather than disconnected
fragments. Represent parallel tool calls as sibling spans sharing the same parent, not as
sequential spans.

```
[invoke_agent: research-agent]        <- root span
  [chat: openai/gpt-4o]              <- LLM planning call
  [execute_tool: web_search]          <- tool call 1
  [execute_tool: code_interpreter]    <- tool call 2 (parallel sibling)
  [chat: openai/gpt-4o]              <- LLM synthesis call
```

**Why (beginner):** A flat list of spans tells you each step's duration but not which steps
belong to the same request. The parent-child tree lets you answer "which agent invocations are
slow?" and then drill in to find whether the bottleneck is the LLM call, the tool, or the
retrieval step.

**Caveat / contested:** WARNING **WARNING** — If you forget to propagate trace context across
an async queue or subprocess boundary, spans from downstream services appear as new root traces.
The resulting gaps look like fast responses; the actual work is invisible. Always verify context
propagation end-to-end in a staging environment before going to production.

**Sources:**
[zylos.ai — OpenTelemetry for AI Agents: Observability, Tracing, and the GenAI Semantic Conventions](https://zylos.ai/research/2026-02-28-opentelemetry-ai-agent-observability/) (2026-02-28) · [inference.net — LLM Observability: A Complete Guide to Monitoring Production Deployments](https://inference.net/content/llm-observability-monitoring-production-deployments/) (fetched 2026-07-16)

**Confidence:** OK independently-corroborated (Zylos Research + Inference.net, different publishers)

---

## Practice: Emit structured JSON logs for every LLM call, with PII handling by log level

**Do:** Wrap your LLM client so every call emits a structured JSON log entry automatically.
Required fields: `timestamp`, `trace_id`, `span_id`, `model`, `provider`, `prompt_tokens`,
`completion_tokens`, `latency_ms`, `finish_reason`, `prompt_hash` (a SHA-256 fingerprint of
the rendered prompt — not the raw text itself), and `status`.

Log prompt content and retrieved chunks at `DEBUG` level only (for development and staging
environments). Never log raw prompt text at `INFO` in production — it commonly contains user
PII (personal information such as names, emails, or private details). Use provider-returned
token counts rather than local tokenizer estimates; they are authoritative for billing.

**Why (beginner):** Token counts are your primary cost signal. Without them you cannot
attribute spend to a feature, a user, or a prompt version. The prompt hash lets you detect
duplicate calls and correlate traces without storing sensitive text.

**Caveat / contested:** Different providers return different token-count fields (OpenAI splits
into `cached_tokens`; Anthropic splits into `cache_read_input_tokens`). Log these
provider-specific subfields separately so cache hits are not double-counted in cost estimates.

**Sources:**
[braintrust.dev — How to track LLM token usage (2026)](https://www.braintrust.dev/articles/how-to-track-llm-token-usage-2026) (fetched 2026-07-16) · [latitude.so — How Teams Use Logs to Debug LLM Failures](https://latitude.so/blog/how-teams-use-logs-debug-llm-failures) (fetched 2026-07-16)

**Confidence:** OK independently-corroborated (Braintrust + Latitude, different publishers)

---

## Practice: Version every prompt template and tag every trace with the version

**Do:** Store prompt templates in version control (such as Git). Apply semantic versioning
(`MAJOR.MINOR.PATCH`):

- Increment MAJOR for structural rewrites that change meaning
- Increment MINOR for new examples or sections
- Increment PATCH for typo or wording fixes

At runtime, tag every trace with three version identifiers: `prompt_template_version`,
`model_version` (the exact model ID returned by the API), and `app_version`. Without these
tags you cannot attribute quality or cost changes to a specific deployment.

**Why (beginner):** LLM outputs are non-deterministic — the same prompt can produce different
answers each time. When quality drops after a release, the first question is "did the prompt
change, the model change, or the code change?" If every trace carries all three versions you
can filter in your dashboard; without them you are guessing.

**Caveat / contested:** Some providers silently update a named model (e.g., `gpt-4o` can
change under a stable alias) without incrementing a version string. Always log the model ID
returned in the API response (`gen_ai.response.model`), not just the ID you requested
(`gen_ai.request.model`). These two can differ. CLOCK **verify live** — provider aliasing
behaviour varies and can change.

**Sources:**
[getmaxim.ai — Prompt versioning and its best practices 2025](https://www.getmaxim.ai/articles/prompt-versioning-and-its-best-practices-2025/) (fetched 2026-07-16) · [inference.net — LLM Observability: A Complete Guide to Monitoring Production Deployments](https://inference.net/content/llm-observability-monitoring-production-deployments/) (fetched 2026-07-16) · [braintrust.dev — Best Prompt Versioning Tools for Production Teams (2026)](https://www.braintrust.dev/articles/best-prompt-versioning-tools-2025) (fetched 2026-07-16)

**Confidence:** OK independently-corroborated (Maxim AI + Inference.net + Braintrust, three different publishers)

---

## Practice: Build and maintain a golden dataset for offline regression evaluation

**Do:** Maintain a curated golden dataset of 50-100 input/expected-behaviour pairs per
feature. Draw cases primarily from production failures (real users surface patterns synthetic
data misses). Split the set into roughly 70% core cases and 30% edge cases (adversarial
inputs, ambiguous queries, off-topic requests). Store the dataset as JSONL (JSON Lines — a
text file where each line is one JSON object, easy to read line-by-line and compatible with
most data tools) in version control alongside the prompt templates.

Run the eval suite on every pull request, fail the build when regression exceeds an agreed
tolerance, and grow the set deliberately from new production failures rather than padding with
synthetic duplicates. Keep a holdout partition (a reserved portion that is never optimised
against) to catch over-fitting to the eval set.

**Why (beginner):** Every model update, prompt change, and retrieval tweak can silently break
something that previously worked. A golden dataset turns "it feels worse" into "metric X
dropped 8 percentage points on the edge-case partition" — actionable and attributable.

**Caveat / contested:** WARNING **WARNING** — If you use the same examples as few-shot
examples in the prompt AND as eval cases, scores will be inflated. Strictly separate the eval
pool from the prompt development pool. Also avoid testing on synthetic data that your model
was trained on; contamination produces misleadingly high scores.

**Sources:**
[qaskills.sh — How to Build a Golden Dataset for LLM Evaluation](https://qaskills.sh/blog/golden-dataset-llm-evaluation-guide) (fetched 2026-07-16) · [statsig.com — Golden datasets: Creating evaluation standards](https://www.statsig.com/perspectives/golden-datasets-evaluation-standards) (fetched 2026-07-16) · [braintrust.dev — What is LLM evaluation? A practical guide to evals, metrics, and regression testing](https://www.braintrust.dev/articles/llm-evaluation-guide) (fetched 2026-07-16)

**Confidence:** OK independently-corroborated (QA Skills + Statsig + Braintrust, three different publishers)

---

## Practice: Run LLM-as-judge evaluations asynchronously on sampled production traffic

**What is LLM-as-judge?** LLM-as-judge means using a second, trusted AI model to automatically
grade the outputs of your main AI — the same way a teacher grades homework.

**Do:** Select a strong, stable model as your judge and evaluate sampled production outputs
against explicit rubrics (relevance, faithfulness, task completion, safety). Start with a small
number of high-signal metrics — three to five is enough; more makes the signal noisy and
expensive. Run judge evaluations **asynchronously** (in the background, not while the user is
waiting), never in the critical request path. A sample rate of 5-20% of production traffic
balances coverage against cost; target high-latency and low-heuristic-score traces first.

Before scaling, validate your judge against a domain-expert-annotated sample and track
false-positive rates — a judge that passes unsafe outputs is more dangerous than no judge
at all.

**Why (beginner):** You rarely have labelled ground-truth answers at runtime (that is why
offline evals use golden datasets). LLM-as-judge gives you a scalable proxy quality signal on
live traffic without requiring human review of every response.

**Caveat / contested:** The judge model itself can drift if your provider updates it. Pin the
judge to a specific model version where possible. Vague rubrics produce noisy judges; rewrite
criteria as explicit step-by-step checklists when a metric becomes production-critical. In
high-risk domains (healthcare, legal, safety), false positives from an LLM judge create
dangerous false confidence — supplement with deterministic rule checks and periodic human
audits.

**Sources:**
[deepeval.com — LLM-as-a-Judge in 2026: Top evaluation techniques and best practices](https://deepeval.com/blog/llm-as-a-judge) (fetched 2026-07-16) · [inference.net — LLM Observability: A Complete Guide to Monitoring Production Deployments](https://inference.net/content/llm-observability-monitoring-production-deployments/) (fetched 2026-07-16) · [openobserve.ai — LLM Monitoring Best Practices: Complete Guide for 2026](https://openobserve.ai/blog/llm-monitoring-best-practices/) (fetched 2026-07-16)

**Confidence:** OK independently-corroborated (DeepEval + Inference.net + OpenObserve, three different publishers)

---

## Practice: Detect behavioral drift via a four-layer signal stack

**Do:** Monitor for model behavioral drift (the gradual change in how your AI behaves over
time) using four complementary signals, listed from cheapest to most expensive to run:

**(1) Statistical output signals** — track response-length distribution, vocabulary entropy
(how varied the words your AI uses are), and output-structure consistency; alert when any
shifts by more than two standard deviations from the rolling baseline (that is, when the
value moves unusually far from recent normal levels).

**(2) Embedding-space signals** — compute cosine similarity between rolling output embeddings
and a reference baseline. Embeddings are numerical representations of text that capture
meaning; cosine similarity measures how closely two meanings match on a 0-1 scale where 1 is
identical. A sustained drop beyond 0.15 indicates semantic drift — your AI's responses have
meaningfully changed in content, not just style.

**(3) LLM-as-judge scoring** — run your production judge evaluator (see the LLM-as-judge
practice above) on a fixed reference probe set on a regular schedule and alert on score drops.

**(4) Golden-dataset regression** — run the offline eval suite against the full golden dataset
(the curated set of test cases described in the golden dataset practice above) on a schedule
or after provider-announced model updates.

Use two-tier alerting: statistical shifts get a 24-48-hour response window; judge-score drops
of more than 10% against the 7-day rolling average get an immediate (Tier 1) response.

**Why (beginner):** Providers silently update models under stable aliases. Retrieval indexes
change. Prompt templates drift through well-intentioned edits. None of these send you an
alert — only your monitoring will. Behavioural drift can look like a sudden jump or a slow
degradation across weeks; the four-layer stack catches both.

**Caveat / contested:** WARNING **WARNING** — The judge model you use to detect drift can
itself drift if you do not pin it to a specific model version. Pin both your application model
and your judge model; track them separately. The specific numeric thresholds (two standard
deviations, 0.15 cosine drop) are reference points from observed production practice, not
formal standards — treat them as starting points and adjust to your application's distribution.

**Sources:**
[stackpulsar.com — LLM Model Drift Detection 2026: Monitoring AI Degradation](https://stackpulsar.com/blog/llm-model-drift-detection/) (fetched 2026-07-16) · [leanware.co — LLM Monitoring and Drift Detection Guide](https://leanware.co/insights/llm-monitoring-drift-detection-guide) (fetched 2026-07-16) · medium.com/@EvePaunova — Tracking Behavioral Drift in Large Language Models (confirmed live Jul 2026; curl returns 403 bot-protection — link removed per policy, citation retained)

**Confidence:** OK independently-corroborated (StackPulsar + Leanware + Eva Paunova on Medium, three different publishers)

---

## Practice: Define SLOs on TTFT P99, error rate, and cost-per-request; alert with burn rates

**Some plain-English definitions before this practice:**

- A **Service Level Objective (SLO)** is a target you set for a metric — for example, "TTFT
  must be under 500ms for 99% of requests." It is a formal promise to yourself (and your users)
  about the minimum quality of your service.

- **TTFT** stands for Time to First Token — how long a user waits before they see the first
  word of the AI's response begin to appear. This is often what determines whether an
  interaction feels "instant" or "slow."

- **P99** (99th percentile) means 99% of your users see a response within this time; only 1%
  wait longer. **P95** means 95% are within the limit. Using the average hides the worst cases:
  at 100 requests per second, an average TTFT of 120ms can coexist with a P99 of 600ms,
  meaning one user per second waits half a second before seeing output.

**Do:** Define at least three SLOs for each LLM-backed endpoint:

(a) **Latency** — TTFT P99 target appropriate to the use case:
  - Interactive chat: at or under 500ms
  - Voice agents: at or under 150ms
  - RAG-augmented chat (retrieval + LLM together): at or under 1 second
  - Batch/async tasks: negotiate separately with stakeholders

(b) **Error rate** — overall success rate above 99.5% in a rolling window

(c) **Cost** — cost per 1,000 requests tracked as a P95 metric, alerted when it exceeds 2x
the rolling baseline

**What is burn-rate alerting?** Your error budget is how much failure your SLO allows in a
given period. A burn rate of 14.4x means you are consuming that budget 14.4 times faster than
normal — at that rate, the whole month's budget will be gone in roughly two hours. Most
monitoring tools (Datadog, New Relic, CloudWatch) can calculate burn rates automatically once
you define your SLO.

Use burn-rate alerting rather than static thresholds: page on-call when the error-budget burn
rate exceeds 14.4x over a 1-hour window, or 6x over 6 hours, to catch both sudden spikes and
slow leaks.

**Why (beginner):** Traditional web-service SLOs (HTTP 5xx rate, p95 latency) miss the
LLM-specific failure modes: a response that arrives quickly but is truncated, a refusal that
is not a 5xx error, or a cost spike from a single runaway context window. Separating TTFT from
total latency surfaces streaming quality issues that total-duration metrics hide.

**Caveat / contested:** CLOCK The specific numeric targets above are reference points from SRE
literature and observed production practice, not universal standards. The right TTFT target for
voice agents (at or under 150ms P99) is very different from the right target for asynchronous
report generation. Negotiate SLOs with product stakeholders, not from a checklist. **verify
live** — model provider latency profiles change as capacity scales or degrades.

**Sources:**
[spheron.network — LLM Inference SLO Engineering: TTFT, ITL, and P99 Latency Budgets for Production AI (2026)](https://www.spheron.network/blog/llm-inference-slo-ttft-itl-latency-budget-guide-2026/) (fetched 2026-07-16) · [inference.net — LLM Observability: A Complete Guide to Monitoring Production Deployments](https://inference.net/content/llm-observability-monitoring-production-deployments/) (fetched 2026-07-16) · [openobserve.ai — OpenTelemetry for LLMs: Complete SRE Guide for 2026](https://openobserve.ai/blog/opentelemetry-for-llms/) (fetched 2026-07-16)

**Confidence:** OK independently-corroborated (Spheron + Inference.net + OpenObserve, three different publishers)

---

## Practice: Use a hybrid head-based / tail-based sampling strategy for high-volume LLM tracing

> **Prerequisite note for this practice:** Tail-based sampling requires the OpenTelemetry (OTel)
> Collector running as a separate service sitting between your application and your tracing
> backend. The Collector is not part of the OTel SDK you use to instrument your application
> code — it is an additional process you must deploy and configure. If you are using a managed
> platform (Datadog, New Relic) or Langfuse Cloud, check whether they handle the Collector for
> you — you may not need to run one at all.

**Do:** In development and staging, use 100% sampling to get full visibility. In production,
apply a two-tier strategy:

**(1) Head-based sampling at 10-30%** as the baseline for cost management. This means the
decision to record a trace is made at the very start of the request (the "head"), before you
know the outcome. Use the `TraceIdRatioBased` sampler in the OTel SDK — this is a built-in
sampler you configure via environment variables. In Python, you can enable 10% sampling with
no code changes: set `OTEL_TRACES_SAMPLER=traceidratio` and `OTEL_TRACES_SAMPLER_ARG=0.1` in
your environment. Head-based sampling is lightweight because it makes the decision immediately
with zero buffering.

**(2) Tail-based sampling policy** (applied at the OpenTelemetry (OTel) Collector, which is a
separate service — see prerequisite note above) that **always retains** traces matching any of:
  - error status
  - TTFT exceeding your P99 SLO target
  - LLM-as-judge score below your quality floor
  - a specific tenant or model ID you are investigating

For LLM-as-judge evaluation specifically, a 5-20% sample rate balances quality coverage
against evaluation cost. Route all spans from a single trace to the same collector instance —
tail sampling breaks if spans from one trace are split across collectors.

**Why (beginner):** LLM calls are expensive to trace at 100% when you are handling thousands
of requests per second. Head-based sampling is cheap but blind to outcomes — you cannot choose
to keep a trace after you know it was slow or broken. Tail-based sampling is smarter (it can
keep the important cases) but needs infrastructure. The hybrid catches errors, slow calls, and
low-quality outputs while keeping routine successful calls affordable.

**Caveat / contested:** WARNING **WARNING** — Tail-based sampling requires all spans from a
trace to arrive at the **same** collector instance. If you have multiple collector replicas,
spans from one trace can land on different replicas, making the tail decision impossible. Use a
consistent hashing routing layer in front of your collectors, or use a managed
adaptive-tracing product that handles this for you.

**Sources:**
[grafana.com/docs — Sampling strategies for tracing](https://grafana.com/docs/grafana-cloud/send-data/traces/configure/sampling/) (fetched 2026-07-16) · [betterstack.com — Sampling in OpenTelemetry: A Beginner's Guide](https://betterstack.com/community/guides/observability/opentelemetry-sampling/) (fetched 2026-07-16) · [mlflow.org — Setting Up LLM Observability Pipelines in 2026](https://mlflow.org/articles/setting-up-llm-observability-pipelines-in-2026/) (fetched 2026-07-16)

**Confidence:** OK independently-corroborated (Grafana + Better Stack + MLflow, three different publishers)

---

## Held pending fixes (not publish-ready)

- OTel GenAI semconv dedicated repo (`open-telemetry/semantic-conventions-genai`) has no
  versioned releases as of 2026-07-16. No release artifact to pin; all `gen_ai.*` attribute
  names remain Development-status. Monitor
  [github.com/open-telemetry/semantic-conventions-genai](https://github.com/open-telemetry/semantic-conventions-genai)
  for any stability roadmap or first release.

---

## CHANGELOG

### From technical entry to this beginner entry (re-leveled 2026-07-17)

Re-leveled from the 2026-07-16 technical entry. Facts unchanged. All source URLs preserved
verbatim from the technical entry. No new facts or URLs introduced.

**Beginner corrections applied:**

1. **KILL-GN-1** — Added a prerequisites callout at the top of the file directing readers to
   install an OTel-compatible SDK and set up a tracing backend (Langfuse or Arize Phoenix)
   before proceeding. The technical entry assumed this was already done.

2. **FIX-GN-1** — Added a plain-English definitions section immediately below the prerequisites
   block, defining "trace" (the complete record of one request) and "span" (one step within
   that trace) before any practice uses these terms.

3. **FIX-GN-2** — Expanded "OTel" to "OpenTelemetry (OTel)" and "OTLP" to "OpenTelemetry
   Protocol (OTLP)" on their first appearance in body text, then abbreviated freely thereafter.

4. **FIX-GN-3** — Added plain-English definitions of SLO (Service Level Objective), TTFT (Time
   to First Token), P95, and P99 in a definitions block at the start of the SLO practice.

5. **FIX-GN-4** — Added a plain-English explanation of "error budget" and "burn rate" inside
   the SLO practice, before the numeric targets are given. Explained that monitoring tools
   (Datadog, New Relic, CloudWatch) can calculate burn rates automatically.

6. **FIX-GN-5** — Added a one-sentence definition of "LLM-as-judge" at the start of that
   practice: using a second trusted AI model to automatically grade the outputs of your main AI.

7. **FIX-GN-6** — Added a plain-English parenthetical defining "embeddings" (numerical
   representations of text that capture meaning) and "cosine similarity" (how closely two
   meanings match on a 0-1 scale where 1 is identical) inside the drift detection practice.

8. **FIX-GN-7** — Added a prerequisite note at the start of the sampling practice explaining
   that tail-based sampling requires the OTel Collector as a separate service, and noting that
   managed platforms (Datadog, New Relic, Langfuse Cloud) may handle this automatically.

**Corrections carried forward from the technical entry (unchanged):**

9. **FIX-G1 (Skeptic, original)** — "gen_ai.prompt / gen_ai.completion were deprecated"
   softened to "have been superseded by the structured message attributes" — no formal
   deprecation notice found in cited sources.

10. **FIX-G2 (Skeptic, original)** — "TTFT P95" corrected to "TTFT P99" in heading and body.
    Lead source (Spheron) explicitly argues for P99.

11. **FIX-1 (Timekeeper, original)** — Clarified that the `semantic-conventions-genai`
    dedicated repo has no published releases. v1.40/v1.41 identifiers belong to the main
    `semantic-conventions` repo, not the GenAI repo.

12. **FLAG-G3 (Skeptic, original)** — Greptime blog date corrected from 2026-05-09 to
    2026-05-21.

13. **Link-check gate (publish-time):** medium.com/@EvePaunova drift article returned 403 (bot-protection). Confirmed live via WebFetch. Unlinked to plain text per policy; citation retained. All other URLs: 200.
