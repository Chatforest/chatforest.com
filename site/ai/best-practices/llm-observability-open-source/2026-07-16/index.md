# LLM Observability and Monitoring — Open-Source Tooling — Best Practices (as of 16 Jul 2026)

> How to use Langfuse, Arize Phoenix, W&B Weave, OpenLLMetry/Traceloop, and Helicone for LLM tracing, evaluation, and debugging — including acquisition notes and self-hosting trade-offs as of mid-2026.


# LLM Observability and Monitoring — Open-Source Tooling (as of 16 Jul 2026)

> **Grading note.** A dated snapshot — accurate as of **16 Jul 2026**, frozen here and kept as
> a permanent archive entry. Research-drafted by a pupil, graded by the 3-lens panel + sensei.
> Corrections applied inline; unverifiable gaps marked ⚠ PENDING (#issue) — never guessed.

> **Cross-reference.** Cost-tracking practices for Langfuse and W&B Weave (token spend, budget
> alerts, per-user attribution) are covered in the **LLM Cost Management — Open-Source Tooling**
> entry (snapshot: 2026-07-06). This entry focuses on tracing quality, evaluation, and debugging.

> **Acquisition notes — verify live.** Langfuse was acquired by ClickHouse on 16 Jan 2026.
> Licensing and self-hosting remain unchanged per the official announcement, but future roadmap
> decisions rest with ClickHouse. Re-verify at [langfuse.com/blog](https://langfuse.com/blog) for
> any post-acquisition product or licensing announcements (next scheduled re-check: Oct 2026).
> 🕒 Helicone was acquired by Mintlify on 3 Mar 2026 and is now in maintenance mode (security
> patches, bug fixes, and new model support only; no commitment to new feature development). Re-verify
> Helicone's status at next quarterly refresh (next: Oct 2026) — the Mintlify team's stated roadmap
> could change in either direction.

## How to read the labels
- ✅ **independently-corroborated** — 2+ independent publishers
- 📄 **vendor-documented** — official docs only (authoritative, single source)
- ⚠️ **WARNING** — a default that can cost money, break the machine, or remove a safety net
- 🕒 **verify live** — fast-moving (versions/prices/quotas); check the current value

---

## Practice: Use session IDs to group multi-turn conversation traces in Langfuse

**Do:** When building a chatbot or multi-turn agent, pass a consistent `sessionId` to every
Langfuse trace in the same conversation. Use the `propagate_attributes()` helper or set the
`session_id` attribute in every call. View the resulting session replay in the Langfuse UI to
see the complete interaction in one place.

```python
from langfuse import get_client, propagate_attributes

langfuse = get_client()

# At conversation start, generate or receive a session ID
session_id = "user-abc-conv-123"

with langfuse.start_as_current_observation(as_type="span", name="turn-1") as span:
    propagate_attributes({"session_id": session_id})
    # ... your LLM call here
```

**Why (beginner):** Without session grouping, each turn of a conversation appears as an isolated
trace. Debugging a broken conversation means hunting across dozens of unrelated entries. A session
ID stitches all turns together so you can replay the entire conversation, see where quality
degraded, and add annotation scores at the session level.

**Caveat / contested:** Session IDs must be propagated manually through every code path that
creates observations. If a background job or tool call creates a trace without the session ID,
it will appear disconnected from the session in your dashboard. Test session grouping in
development before relying on it for production debugging.

**Sources:**
[langfuse.com/docs/observability/features/sessions](https://langfuse.com/docs/observability/features/sessions) (Langfuse docs, fetched 16 Jul 2026) ·
[langfuse.com/docs/sdk/python/low-level-sdk](https://langfuse.com/docs/sdk/python/low-level-sdk) (Langfuse docs, fetched 16 Jul 2026)

**Confidence:** 📄 vendor-documented — both sources are Langfuse official docs (acquired by
ClickHouse Jan 2026; licensing unchanged per langfuse.com/blog/joining-clickhouse).

🕒 **verify live** — Code examples use the **Langfuse Python SDK v4** (current: v4.14.0, Jul 10, 2026; server: v3.214.0, Jul 15, 2026). The SDK v4 API (`get_client`, `propagate_attributes`) is incompatible with SDK v3. If you installed an older version, upgrade with `pip install --upgrade langfuse` before using these patterns.

---

## Practice: Use the @observe decorator (Langfuse) or @weave.op decorator (W&B Weave) to add tracing without rewriting code

**Do:** Add the decorator above any function — a retrieval step, a prompt-building function, a
tool call — and it becomes a named, timed span in your trace. For Langfuse use `@observe()`;
for W&B Weave use `@weave.op`. Both capture inputs, outputs, and latency automatically.

**Langfuse example (SDK v4):**
```python
from langfuse import observe

@observe()
def retrieve_documents(query: str) -> list[str]:
    # your retrieval logic
    return docs
```

**W&B Weave example:**

⚠️ **WARNING (W&B Weave data egress):** `weave.init()` requires a W&B account and sends every input and output of the decorated function — including any user-submitted text — to Weights & Biases cloud infrastructure. Do not call `weave.init()` in a production service until you have confirmed this meets your data-handling obligations. See Practice 7 for the full data-egress discussion.

```python
import weave
weave.init("my-team/my-project")  # Requires W&B account; sends data to wandb.ai cloud

@weave.op
def call_llm(prompt: str) -> str:
    # your LLM call
    return response
```

**Why (beginner):** You don't need to change your LLM provider's SDK or wrap every call in
verbose boilerplate. One line per function gives you end-to-end visibility: how long each step
took, what went in, and what came out. When something breaks, the trace shows exactly which
function produced the bad output.

**Caveat / contested:** Capturing large inputs and outputs adds overhead. Langfuse lets you
disable capture per-decorator with `capture_input=False` / `capture_output=False`, or globally
via the `LANGFUSE_OBSERVE_DECORATOR_IO_CAPTURE_ENABLED` environment variable (Langfuse SDK v4).
For functions processing large documents, evaluate the latency impact in your test environment
before enabling in production.

**Sources:**
[langfuse.com/docs/sdk/python/decorators](https://langfuse.com/docs/sdk/python/decorators) (Langfuse docs, fetched 16 Jul 2026) ·
[docs.wandb.ai/weave/quickstart](https://docs.wandb.ai/weave/quickstart) (W&B Weave docs, fetched 16 Jul 2026)

**Confidence:** 📄 vendor-documented — both are official vendor docs, from two different vendors
(Langfuse/ClickHouse and Weights & Biases), each describing their own feature.

---

## Practice: Run automated LLM-as-a-judge evaluation on production traces, not just in offline test suites

**Do:** Configure automated scoring on live traces, not only on held-out datasets. In Langfuse,
set up LLM-as-a-Judge in the Evaluation settings to score incoming production traces on
dimensions like helpfulness, groundedness, or toxicity. In W&B Weave, use `weave.Evaluation`
with a scorer class to run the same evaluator against both your test dataset and sampled
production calls. In Arize Phoenix, use server-side evaluations configured through the UI.

**Why (beginner):** Offline evaluation only tests the examples you thought of in advance.
Production traffic contains the full distribution of real user inputs, including edge cases you
never anticipated. Running evaluators on a sample of live traces catches quality regressions
within hours of a prompt change, not weeks later when users complain.

**Caveat / contested:** LLM-as-a-judge evaluations cost tokens and add latency to your
observability pipeline. Sample rather than score every trace in high-volume production systems.
Also, LLM judges can themselves produce wrong verdicts — treat scores as signals to triage
human review, not as ground truth. Arize Phoenix uses function calling for structured scorer
output (which reduces free-text parsing errors), but the underlying model can still hallucinate.

**Sources:**
[langfuse.com/docs/scores/overview](https://langfuse.com/docs/scores/overview) (Langfuse docs, fetched 16 Jul 2026) ·
[wandb.ai/site/evaluations/](https://wandb.ai/site/evaluations/) (W&B Weave product page, fetched 16 Jul 2026) ·
[arize.com/docs/phoenix/evaluation/evals](https://arize.com/docs/phoenix/evaluation/evals) (Phoenix docs, fetched 16 Jul 2026) ·
[langfuse.com/docs/evaluation/overview](https://langfuse.com/docs/evaluation/overview) (Langfuse docs, fetched 16 Jul 2026)

**Confidence:** ✅ independently-corroborated — Langfuse (ClickHouse), W&B Weave (Weights & Biases), and Arize Phoenix (Arize AI) all document this practice independently.

---

## Practice: Use Langfuse prompt management to deploy prompt changes without code redeployment

**Do:** Store prompts in Langfuse rather than hardcoding them. Fetch the current production
version at runtime using the SDK: `langfuse.get_prompt("my-prompt-name")`. When you want to
ship an updated prompt, create a new version in the UI or API, test it in the playground, then
move the "production" label to the new version. Your running application picks it up on the
next fetch — no code change, no redeploy.

**Why (beginner):** Hardcoded prompts mean every prompt tweak requires a code commit, review,
CI pipeline run, and deployment. With Langfuse prompt management, a non-engineer can fix a
broken prompt in minutes. Version history also lets you roll back instantly if a change makes
quality worse.

**Caveat / contested:** The SDK fetches the prompt at call time, adding a small network round
trip. Langfuse SDKs cache fetched prompts locally (with a configurable TTL), so the overhead is
typically negligible, but cache staleness means a rollback may not propagate immediately to all
running instances. For latency-critical paths, verify the caching behaviour of your SDK version.
This feature is vendor-specific to Langfuse; Phoenix and Weave offer a prompt playground but not
the same deploy-by-label model.

**Sources:**
[langfuse.com/docs/prompts/get-started](https://langfuse.com/docs/prompts/get-started) (Langfuse docs, fetched 16 Jul 2026)

**Confidence:** 📄 vendor-documented — single vendor source (Langfuse/ClickHouse).

---

## Practice: Use OpenLLMetry (Traceloop) to instrument once and send traces to any backend

**Do:** Install `opentelemetry-sdk` and `traceloop-sdk` alongside your provider package
(e.g. `openai`). Call `Traceloop.init(app_name="my-app", exporter=OTLPSpanExporter(...))` once
at startup. OpenLLMetry auto-instruments every supported LLM provider and framework call via
OpenTelemetry spans — you point the exporter at whichever backend you use (Langfuse, Arize
Phoenix, Datadog, New Relic, Honeycomb, Grafana, or any OTLP-compatible endpoint).

The framework currently (v0.62.1, released 28 Jun 2026) supports 16+ LLM providers including
OpenAI/Azure, Anthropic, Gemini, Cohere, Mistral, Groq, AWS Bedrock, HuggingFace, IBM Watsonx,
Ollama, Replicate, SageMaker, Together AI, Vertex AI; and frameworks including LangChain,
LlamaIndex, LangGraph, CrewAI, Haystack, Langflow, LiteLLM, OpenAI Agents, AWS Strands, and
Agno.

**Why (beginner):** Without a common instrumentation layer, switching observability backends
means rewriting every trace call. OpenLLMetry is Apache 2.0 licensed and uses the CNCF
OpenTelemetry standard. If you outgrow one backend, you change one exporter line — not your
entire codebase.

⚠️ **WARNING:** OpenLLMetry captures full prompt text and model responses by default, which may
include personally identifiable information (PII). Audit the `suppress_prompts` and
`suppress_responses` options before going to production in any environment where real users
send text — not just regulated industries. Set `suppress_prompts=True` to disable prompt
logging until you have reviewed what data your traces will capture.

**Caveat / contested:** OpenLLMetry covers instrumentation only — it does not provide a UI for
viewing traces, running evaluations, or managing prompts. You still need a backend (Langfuse,
Phoenix, etc.) to visualise and act on the data. Also, the semantic conventions for GenAI
spans (the data schema) are still evolving in the OpenTelemetry project; field names and
attribute keys may change across minor releases.

**Sources:**
[github.com/traceloop/openllmetry](https://github.com/traceloop/openllmetry) (Traceloop GitHub, fetched 16 Jul 2026) ·
[traceloop.com/docs/openllmetry/introduction](https://www.traceloop.com/docs/openllmetry/introduction) (Traceloop docs, fetched 16 Jul 2026) ·
[langfuse.com/guides/cookbook/otel_integration_openllmetry](https://langfuse.com/guides/cookbook/otel_integration_openllmetry) (Langfuse integration guide, fetched 16 Jul 2026) ·
[docs.newrelic.com/docs/opentelemetry/get-started/traceloop-llm-observability/traceloop-llm-observability-intro/](https://docs.newrelic.com/docs/opentelemetry/get-started/traceloop-llm-observability/traceloop-llm-observability-intro/) (New Relic docs, fetched 16 Jul 2026)

**Confidence:** ✅ independently-corroborated — Traceloop's own docs, Langfuse integration guide
(different publisher), and New Relic documentation (third publisher) all describe this
integration pattern independently.

🕒 **verify live** — v0.62.1 as of 28 Jun 2026; the supported-provider and supported-framework lists grow with each release — verify live at [github.com/traceloop/openllmetry](https://github.com/traceloop/openllmetry) before treating the list above as complete.

---

## Practice: Deploy Arize Phoenix locally (Docker) for zero-data-egress debugging

**Do:** Run Phoenix as a local Docker container before committing traces to any cloud backend:

```bash
docker pull arizephoenix/phoenix
docker run -p 6006:6006 -p 4317:4317 -i -t arizephoenix/phoenix:18.0.0
```

Access the UI at `http://localhost:6006`. For production self-hosting, use Docker Compose with
a PostgreSQL backend (requires Postgres ≥ 14) and pin the image version rather than using
`:latest`. Phoenix accepts traces via OTLP (OpenTelemetry Protocol) on port 4317, so any
OTel-instrumented application can send data to it without changing provider libraries.

Phoenix v18.0.0 (released 14 Jul 2026) supports Python 3.10–3.14. It is licensed under
**Elastic License 2.0 (ELv2)** — self-hosting is free and unrestricted for internal use,
but you may not offer Phoenix as a managed service to third parties.

**Why (beginner):** When debugging a sensitive application (medical, legal, financial), you may
not be permitted to send prompt/response text to a third-party cloud. Running Phoenix locally
means traces never leave your machine. The embedding visualisation and span replay features work
identically whether you run Phoenix locally or in a cloud.

⚠️ **WARNING:** Do not use the `:latest` Docker tag in production. Phoenix v18.0.0 introduced
breaking changes (session time-range filter API), and releases are frequent (multiple per day at
times). Always pin a specific version tag (`arizephoenix/phoenix:18.0.0`). Confirm the tag
exists in Docker Hub before pinning — the PyPI version and Docker Hub image tags are separate
registries and may not always align exactly.

**Caveat / contested:** The Elastic License 2.0 is not OSI-approved open source. Teams that need
a fully permissive license (Apache 2.0, MIT) for their observability backend should evaluate
Langfuse (core is MIT) or OpenLLMetry-based pipelines instead. One community guide incorrectly
described Phoenix as Apache 2.0 — the authoritative license is in the GitHub repository
([github.com/Arize-ai/phoenix](https://github.com/Arize-ai/phoenix) LICENSE file) and the
Phoenix self-hosting license page, both of which state ELv2.

**Sources:**
[arize.com/docs/phoenix/deployment/docker](https://arize.com/docs/phoenix/deployment/docker) (Phoenix docs, fetched 16 Jul 2026) ·
[arize.com/docs/phoenix/self-hosting/license](https://arize.com/docs/phoenix/self-hosting/license) (Phoenix license docs, fetched 16 Jul 2026) ·
[pypi.org/project/arize-phoenix/](https://pypi.org/project/arize-phoenix/) (PyPI, fetched 16 Jul 2026) ·
[github.com/Arize-ai/phoenix/releases](https://github.com/Arize-ai/phoenix/releases) (GitHub, fetched 16 Jul 2026)

**Confidence:** 📄 vendor-documented — version and license confirmed across the vendor's docs, GitHub LICENSE file, and PyPI metadata. Three sources, all Arize AI or Arize-published registries.

🕒 **verify live** — Phoenix releases very frequently; confirm the version tag in both PyPI and Docker Hub before pinning.

---

## Practice: Build evaluation datasets from production traces in W&B Weave and version them automatically

**Do:** In W&B Weave, curate a dataset by selecting interesting (good, bad, or edge-case) traces
from the Traces view and using "Add selected rows to a dataset." Publish the dataset with
`weave.publish(dataset)` to create a versioned snapshot. Reference it in evaluations with
`weave.ref("my-dataset").get()`. Create a `weave.Evaluation` object pairing the dataset with
one or more scorers, then run it across different model versions to compare performance.

Use leaderboards (`leaderboard.Leaderboard`) to publish a ranked view of evaluation results
across model variants so the whole team shares the same benchmark.

**Why (beginner):** A dataset built from real production failures is far more useful than a
hand-crafted test set. Automatic versioning means you can always re-run a previous evaluation
on a new model without losing the original test cases. Leaderboards prevent the "which model
did we test that on?" problem — everyone looks at the same ranked comparison table
(private to your team, not a public ranking).

⚠️ **WARNING:** If you call `weave.init()` in a production service without intending to send
production data to W&B cloud, every user's message and every AI response will egress to
wandb.ai. Confirm your data handling obligations before enabling Weave in production. There is
no documented fully self-hostable Weave deployment as of this writing — teams with strict data
residency requirements should use Langfuse or Arize Phoenix instead. W&B does offer private
cloud / on-premises enterprise deployments, but these require a contract; verify current terms
at wandb.ai.

**Sources:**
[docs.wandb.ai/weave/guides/core-types/datasets](https://docs.wandb.ai/weave/guides/core-types/datasets) (W&B Weave docs, fetched 16 Jul 2026) ·
[docs.wandb.ai/weave/guides/core-types/leaderboards](https://docs.wandb.ai/weave/guides/core-types/leaderboards) (W&B Weave docs, fetched 16 Jul 2026) ·
[docs.wandb.ai/weave/guides/evaluation/scorers](https://docs.wandb.ai/weave/guides/evaluation/scorers) (W&B Weave docs, fetched 16 Jul 2026)

**Confidence:** 📄 vendor-documented — all three sources are official W&B documentation (single
publisher). The data-egress WARNING is inferred from the architecture (cloud-first SaaS)
and the docs' requirement for a W&B account.

---

## Practice: Know when to avoid Helicone for new projects — it is now in maintenance mode

**Do:** If you are evaluating proxy-based LLM logging in mid-2026, treat Helicone as a
migration source, not a migration destination. Helicone's proxy model (change one URL, add
one auth header) is genuinely elegant and its Apache 2.0 codebase remains available on GitHub.
However, since Mintlify acquired Helicone on 3 March 2026, active feature development has
stopped. Only security patches, bug fixes, and new model support continue to ship; there is no
commitment to new feature development.

If you are already running Helicone, it continues to work and the Mintlify team has committed
to supporting migrations to alternative platforms. For new projects, consider Langfuse (MIT
core, self-hostable), Arize Phoenix (ELv2, self-hostable), or LiteLLM proxy (Apache 2.0,
self-hostable) instead.

**Why (beginner):** Choosing a tool in maintenance mode creates compounding risk: compatibility
with new LLM providers lags, community support thins out, and security gaps beyond basic patches
may go unaddressed. The proxy-logging pattern Helicone pioneered is valuable — just use an
actively maintained implementation of it.

**Caveat / contested:** "Maintenance mode" does not mean "broken." The proxy still works
for 100+ models, caching and rate limiting still function, and the GitHub repo (Apache 2.0)
still accepts community contributions. Teams self-hosting Helicone on their own infrastructure
and willing to contribute bug fixes can continue using it. The maintenance-mode characterisation
comes from official statements by Helicone and Mintlify themselves (both corroborate: security
patches, bug fixes, and new model support continue; no commitment to new feature development).

**Sources:**
[helicone.ai/blog/joining-mintlify](https://www.helicone.ai/blog/joining-mintlify) (Helicone official announcement, fetched 16 Jul 2026) ·
[mintlify.com/blog/mintlify-acquires-helicone](https://www.mintlify.com/blog/mintlify-acquires-helicone) (Mintlify official announcement, fetched 16 Jul 2026)

**Confidence:** ✅ independently-corroborated — confirmed by the Helicone team's own announcement
AND the acquiring company Mintlify's own announcement (two separate organisations publishing
the same fact).

---

## Practice: Self-host Langfuse when data residency or budget rules out SaaS

**Do:** For teams that cannot send prompt/response text to an external cloud (regulated
industries, sovereign data requirements, tight cost budgets), self-host Langfuse using Docker
Compose for development or Kubernetes (Helm) for production. The core feature set is MIT
licensed with no usage limits. Enterprise-only add-ons (SCIM, audit logs, data retention
policies) require a license key but the core product runs without one.

Architecture requirements for self-hosted production: Postgres (metadata), ClickHouse
(trace data), Redis (queue), and S3-compatible blob storage. Docker Compose covers all four
for small-scale use. The cloud and self-hosted codebases are identical, so you can migrate
between them without data loss.

**Why (beginner):** SaaS LLM observability means every prompt and response leaves your
infrastructure. For a legal research tool, a medical assistant, or any application where users
input sensitive information, this is often a deal-breaker. Self-hosting eliminates the data
egress entirely, and Langfuse's MIT license means there are no per-trace fees.

⚠️ **WARNING:** Self-hosting Langfuse requires operating four infrastructure components
(Postgres, ClickHouse, Redis, S3 — separate databases and services that must each run
continuously). Schema migrations run on startup and can cause brief downtime; long-running
migrations are offloaded to a background job to reduce this. If you do not have experience
managing server software, use Langfuse Cloud instead of self-hosting. Before upgrading a
production self-hosted instance, read the versioning policy and changelog — skipping major
versions may require intermediate upgrade steps.

**Caveat / contested:** ClickHouse acquired Langfuse in January 2026. The official announcement
states no changes to licensing, pricing, or self-hosting support. However, future decisions on
these policies rest with ClickHouse, not the original Langfuse team. Flag this as a dependency
risk in your architecture review. SOC2 Type II, ISO 27001, and HIPAA compliance are available
on Langfuse Cloud (not on self-hosted community edition without enterprise add-ons).

**Sources:**
[langfuse.com/docs/deployment/self-host](https://langfuse.com/docs/deployment/self-host) (Langfuse docs, fetched 16 Jul 2026) ·
[langfuse.com/docs/open-source](https://langfuse.com/docs/open-source) (Langfuse licensing docs, fetched 16 Jul 2026) ·
[langfuse.com/blog/joining-clickhouse](https://langfuse.com/blog/joining-clickhouse) (Langfuse official statement on acquisition, fetched 16 Jul 2026) ·
[langfuse.com/security/data-regions](https://langfuse.com/security/data-regions) (Langfuse security docs, fetched 16 Jul 2026)

**Confidence:** 📄 vendor-documented — all sources are Langfuse/ClickHouse official pages.

🕒 **verify live** — Langfuse server v3.214.0 as of 15 Jul 2026; Python SDK v4.14.0 as of 10 Jul 2026. ClickHouse acquisition Jan 2026: check langfuse.com for any subsequent licensing announcements (next re-check: Oct 2026).

---

## Held pending fixes (not publish-ready)

- W&B Weave self-hostability status — official docs confirm cloud-first architecture but private cloud / on-premises enterprise availability requires verifying current W&B enterprise terms; no public documentation URL confirmed this run ⚠ PENDING

## CHANGELOG (grading → this entry)

1. **KILL-3 (Timekeeper):** Added Langfuse Python SDK v4 disclosure. Code examples in this entry use the v4 SDK API (current: v4.14.0, Jul 10, 2026; server: v3.214.0, Jul 15, 2026). SDK v3 does not have `get_client`, `propagate_attributes`, or `LANGFUSE_OBSERVE_DECORATOR_IO_CAPTURE_ENABLED` — teams on SDK v3 must upgrade before using these patterns. Version disclosure added to Practice 1 and Practice 2.
2. **KILL-OS-1 (Beginner — applied to technical entry):** Added condensed W&B Weave data-egress WARNING adjacent to the first `weave.init()` code block in Practice 2, before the code runs. The full discussion remains in Practice 7.
3. **FLAG-O1 (Skeptic):** Softened "active feature development has stopped / no new features" to "no commitment to new feature development" — the official announcements enumerate continuing work (security patches, bug fixes, new model support) without explicitly declaring "no new features."
4. **FLAG-O3 (Skeptic):** Changed Arize Phoenix ELv2 confidence label from ✅ independently-corroborated to 📄 vendor-documented. The two substantive sources (docs + GitHub) are both Arize AI properties; PyPI is a metadata registry echoing the package's own declared license, not an independent editorial source.
5. **FIX-2 (Timekeeper):** Added Docker Hub verification note for Phoenix image tag — PyPI versions and Docker Hub image tags are separate registries. Updated Docker command to pin version `18.0.0` rather than `:latest`.
6. **FIX-3 (Timekeeper):** Added verify-live label to OpenLLMetry supported-provider and supported-framework list (not just the version number).
7. **FLAG-1 (Timekeeper):** Added Oct 2026 re-check trigger for Langfuse/ClickHouse licensing announcements.
8. **FLAG-2 (Timekeeper):** Added Oct 2026 re-check trigger for Helicone maintenance-mode status.
9. **Link-check gate (publish-time):** chatforest.com/reviews/helicone-llm-observability-gateway/ removed — chatforest.com is our own publication (authored by Grove); cannot cite as an independent source. Helicone + Mintlify announcements independently confirm all cited facts; confidence label stands. All remaining 29 URLs: 200.

