# AI Agent Evaluation and Testing — Best Practices (as of 18 Jul 2026)

> Cross-framework best practices for evaluating and testing AI agents: golden datasets, LLM-as-judge calibration, regression CI, unit mocking, red-teaming, evaluation metrics, trajectory evaluation, and the eval-driven iteration loop.


<!-- This file lands at content/ai/best-practices/ai-agent-evaluation-generic/2026-07-18/index.md
     and is an IMMUTABLE dated snapshot. Once published it is never edited.
     Source tiers: independently-corroborated = 2+ DIFFERENT publishers;
     vendor-documented = official vendor docs only. -->

# AI Agent Evaluation and Testing — Generic / Cross-Framework Patterns (as of 18 Jul 2026)

> **Grading note.** A dated snapshot — accurate as of **18 Jul 2026**, frozen here and kept as
> a permanent archive entry. Research-drafted by a pupil, graded by the 3-lens panel + sensei.
> Corrections applied inline; unverifiable gaps marked ⚠ PENDING (#issue) — never guessed.

## How to read the labels
- ✅ **independently-corroborated** — 2+ independent publishers
- 📄 **vendor-documented** — official docs only (authoritative, single source)
- ⚠️ **WARNING** — a default that can cost money, break the machine, or remove a safety net
- 🕒 **verify live** — fast-moving (versions/prices/quotas); check the current value

---

## Practice: Build and maintain a golden dataset drawn from real production failures

**Do:** Assemble a curated set of input/expected-output pairs that represent actual usage of your agent — not invented test cases. Start with 50–100 cases (roughly 40–60 core cases plus 15–25 edge cases), grow to 150–300 as the product matures, and keep the set in a diffable format (JSONL — one JSON object per line — in version control) alongside your prompts. Continuously feed in new production failures as new test cases.

**Why:** Your agent will be tested by real users in ways you did not anticipate. A golden dataset built from actual failures catches the problems that matter most. Datasets invented from imagination tend to miss the tail cases that actually break things in production.

**Caveat / contested:** Sizing recommendations differ across sources. One practitioner guide suggests 50–100 cases are sufficient for early iteration; an academic-style guide recommends ~246 samples per scenario at 95% confidence with 5% margin of error. The right size depends on how much variance your task has and how sensitive you need the regression signal to be. Strictly separate your few-shot prompt examples from your eval cases — overlap inflates scores artificially (data leakage). ⚠️ **WARNING:** Do not include PII from production logs in your golden dataset without scrubbing it first.

**Sources:** [qaskills.sh — golden-dataset-llm-evaluation-guide](https://qaskills.sh/blog/golden-dataset-llm-evaluation-guide) (2026-07-18) · [getmaxim.ai — building-a-golden-dataset](https://www.getmaxim.ai/articles/building-a-golden-dataset-for-ai-evaluation-a-step-by-step-guide/) (2026-07-18) · [digitalapplied.com — ai-agent-evaluation-pipeline-2026](https://www.digitalapplied.com/blog/ai-agent-evaluation-pipeline-2026-testing-methodology) (2026-07-18)
**Confidence:** ✅ independently-corroborated (qaskills.sh, getmaxim.ai, digitalapplied.com)

---

## Practice: Use LLM-as-judge carefully — calibrate against humans before gating on it

**Do:** When you need to evaluate open-ended outputs, use a second LLM as a judge. Design the judge prompt with an explicit rubric, request chain-of-thought reasoning before any score, and use binary (pass/fail) or 3-point scales rather than 10- or 100-point scales. Set the judge's temperature to 0.1–0.2 for consistency. Before using any LLM judge to block a build or gate a release, score at least 30–50 examples manually and compare against the judge's scores — target >85% agreement with human reviewers and track Cohen's kappa (a statistic from −1 to 1 measuring how much two raters agree beyond chance; aim for ≥ 0.6, which indicates moderate agreement).

⚠️ **WARNING:** Each judge call costs real money — running a 500-case golden dataset through a judge model on every CI push adds up quickly. Estimate cost before scaling: at standard frontier model pricing, 500 cases × ~2k tokens each = ~1M tokens per run. Use a cheaper model for the judge where quality allows, and consider running full judge sweeps only on merge rather than on every commit.

**Why:** LLM judges are fast and scalable but carry systematic biases: they prefer longer answers (verbosity bias), prefer earlier responses when comparing two outputs (position bias), and may favor outputs from models in the same family (self-preference bias). Without calibration, you are gating on an unreliable signal.

**Caveat / contested:** The research on Panels of LLM Evaluators (PoLL) suggests using several smaller, diverse models as a committee outperforms a single large model on agreement metrics, but this also costs more. Self-evaluation (having a model judge its own outputs) is especially unreliable and should be avoided. ⚠️ **WARNING:** An uncalibrated LLM judge that gates CI builds can silently pass regressions or block good changes — treat it as infrastructure that needs ongoing monitoring.

**Sources:** [mer.vin — llm-as-a-judge-best-practices](https://mer.vin/2025/11/llm-as-a-judge-best-practices-for-consistent-evaluation/) (2026-07-18) · [digitalapplied.com — ai-agent-evaluation-pipeline-2026](https://www.digitalapplied.com/blog/ai-agent-evaluation-pipeline-2026-testing-methodology) (2026-07-18) · [cameronrwolfe.substack.com — agent-evals](https://cameronrwolfe.substack.com/p/agent-evals) (2026-07-18)
**Confidence:** ✅ independently-corroborated (mer.vin, digitalapplied.com, cameronrwolfe.substack.com)

---

## Practice: Treat prompts like code — run regression evals in CI before merging changes

**Do:** Add an automated eval step to your CI pipeline (CI — Continuous Integration — is an automated process that checks your code every time you make a change, often before it merges). On every pull request, run a fast smoke set of 20–50 prompts. On merge to main, run a full set of 200–500. Fail the build if your pass-rate drops below a threshold (a common choice is 95%). Store prompts in version control as plain text or YAML files, not embedded in application code. Promptfoo (open source, acquired by OpenAI in March 2026 but remains MIT-licensed and multi-provider, ~23,400 GitHub stars as of 2026-07-14) provides YAML-based test definitions, multiple assertion types, and GitHub Actions integration.

🕒 **verify live:** Promptfoo version 0.121.19 (released 2026-07-14) — confirm the current stable release before using. The March 2026 OpenAI acquisition did not change the license or provider support, but verify at [promptfoo.dev/blog/promptfoo-joining-openai](https://www.promptfoo.dev/blog/promptfoo-joining-openai/) for any updates.

**Why:** Prompts are instructions to your agent. Changing a single word can flip responses in ways that are not obvious. Without a CI gate, a well-intentioned prompt edit can silently degrade quality for real users before anyone notices.

**Caveat / contested:** Model-graded assertions are non-deterministic — the same prompt can score differently on two consecutive runs. Use a pass-rate threshold (e.g., 95% pass over N runs) rather than requiring every single test to pass every time. Thresholds should be tuned to your own system's noise floor.

**Sources:** medium.com/@alexrodriguesj — "Testing LLM prompts like code: regression evals in CI/CD with promptfoo" (2026-07-18; confirmed live via WebFetch, unlinked — Medium returns 403 to bots) · [scrolltest.com — llm-regression-testing-promptfoo](https://scrolltest.com/llm-regression-testing-promptfoo/) (2026-07-18) · [traceloop.com — automated-prompt-regression-testing](https://www.traceloop.com/blog/automated-prompt-regression-testing-with-llm-as-a-judge-and-ci-cd) (2026-07-18)
**Confidence:** ✅ independently-corroborated (Medium/alexrodriguesj — confirmed live, unlinked; scrolltest.com; traceloop.com)

---

## Practice: Unit-test agent logic by mocking LLM calls — test your code, not the model

**Do:** Replace real LLM API calls with deterministic mock objects (fake LLM classes, response fixtures, or `unittest.mock` patches) in your unit tests. Assert on what *your code* does with the LLM's response: did it select the right tool? Did it retry on malformed output? Did it parse the JSON correctly? Keep a small fixture library (5–10 files) covering normal responses, tool-call responses, refusals, malformed outputs, and empty responses. Mock at the tool boundary rather than deep inside agent logic, so you still test the real integration code paths.

**Why:** Real LLM calls are slow (seconds per call), cost money, hit rate limits, and are non-deterministic — they produce slightly different outputs each run even at temperature 0. Mocking removes those dependencies while still exercising your routing logic, retry handling, and output parsing.

**Caveat / contested:** Mocked tests do not catch model-specific behavior changes or prompt sensitivity issues — those require eval harnesses with real model calls. Aim for a mix: mocked unit tests for business logic, plus a smaller set of integration tests that call the real model. ⚠️ **WARNING:** If you mock at the wrong level (e.g., patching the agent's internal reasoning function rather than the LLM client), your tests give false confidence.

**Sources:** [callsphere.ai — unit-testing-ai-agents-mocking-llm-calls](https://callsphere.ai/blog/unit-testing-ai-agents-mocking-llm-calls-deterministic-tests) (2026-07-18) · [langwatch.ai — scenario-testing-guides-mocks](https://langwatch.ai/scenario/testing-guides/mocks/) (2026-07-18) · [arxiv.org/html/2601.18827v1](https://arxiv.org/html/2601.18827v1) — automated structural testing via OTel traces + mocking (2026-07-18)
**Confidence:** ✅ independently-corroborated (callsphere.ai, langwatch.ai, arXiv paper)

---

## Practice: Measure p95 latency and cost-per-task — not just accuracy

**Do:** For every eval run, record: time-to-first-token (TTFT) at p50 and p95, total response time at p50 and p95, input/output token counts, and estimated API cost per successful task completion. Set latency budgets by UX class: for interactive chat, target p95 TTFT under 2 seconds; for real-time voice, under 1 second. Include these metrics in CI as supplementary gates — fail or warn when p95 latency spikes or cost per task exceeds threshold.

🕒 **verify live:** Specific latency numbers depend on the model and provider, and change as providers update infrastructure. The figures below are benchmarks from mid-2026 testing — recheck before setting SLOs.

**Why:** A model that gives perfect answers in 30 seconds is unusable in a chat product. Cost per task tells you whether the agent is economically viable at scale. P95 matters more than P50 because the slowest 5% of responses define the worst experience real users encounter. One 2026 benchmark suite found P95/P50 averages around 2.1× and can reach 3.2× in production; reasoning-mode models (extended thinking) can inflate TTFT by 5–30×.

**Caveat / contested:** The 2.1× P95/P50 ratio is from one benchmark suite (digitalapplied.com, mid-2026) and may not reflect your stack. Token cost figures change when providers update pricing. ⚠️ **WARNING:** Evaluating only accuracy and ignoring latency/cost has led teams to ship agents that are prohibitively slow or expensive for real traffic volumes.

**Sources:** [aviso.com — how-to-evaluate-ai-agents-latency-cost](https://www.aviso.com/blog/how-to-evaluate-ai-agents-latency-cost-safety-roi) (2026-07-18) · [digitalapplied.com — ai-model-latency-benchmarks-2026](https://www.digitalapplied.com/blog/ai-model-latency-benchmarks-2026-ttft-throughput) (2026-07-18)
**Confidence:** ✅ independently-corroborated (aviso.com and digitalapplied.com are different publishers)

---

## Practice: Use human review for the cases automated evals miss

**Do:** Do not rely on automated scorers or LLM judges alone. Set up a human review queue where a sample of real agent outputs — especially failures, user complaints, and low-confidence automated scores — go to domain experts for review. Use structured multi-dimensional rubrics (accuracy, tone, completeness, safety) rather than a single overall rating. Track inter-annotator agreement (how consistently different reviewers give the same score — divergence signals rubric drift) and convert reviewed failures directly into permanent test cases in your golden dataset.

**Why:** Automated metrics measure what they measure — not what matters. Users in healthcare, legal, or finance domains can detect subtle failures (wrong implication, missing hedge, dangerous advice) that pattern-matching algorithms will score as "correct." Human review is also how you catch that your LLM judge is drifting — if humans and the judge disagree systematically on 20%+ of cases, your judge rubric needs revision.

**Caveat / contested:** Human review is expensive and slow. The practical approach is strategic sampling: random samples of automated high-confidence decisions (to validate the scorer), plus targeted review of all human-flagged complaints and low-confidence cases. Annotation quality depends heavily on clear guidelines and calibration exercises — skip calibration and annotators diverge quickly.

**Sources:** [getmaxim.ai — incorporating-human-in-the-loop-feedback](https://www.getmaxim.ai/articles/incorporating-human-in-the-loop-feedback-for-continuous-improvement-of-ai-agents/) (2026-07-18) · [braintrust.dev — best-human-in-the-loop-llm-evaluation-platforms-2026](https://www.braintrust.dev/articles/best-human-in-the-loop-llm-evaluation-platforms-2026) (2026-07-18) · [aws.amazon.com — evaluating-ai-agents-real-world-lessons](https://aws.amazon.com/blogs/machine-learning/evaluating-ai-agents-real-world-lessons-from-building-agentic-systems-at-amazon/) (2026-07-18)
**Confidence:** ✅ independently-corroborated (getmaxim.ai, braintrust.dev, AWS blog)

---

## Practice: Red-team your agent deliberately — probe for jailbreaks and prompt injection before launch

**Do:** Before deploying, run structured adversarial testing: direct prompt injection (user tries to override system instructions), indirect prompt injection (malicious instructions in retrieved documents, webpages, or files your agent reads), jailbreak techniques (roleplay framing, encoding tricks such as Unicode variants or Base64, logic traps), and multi-turn attacks that build up over several turns. Test each major risk category separately.

⚠️ **WARNING (cost):** Automated red-teaming tools make large numbers of LLM API calls. "50+ vulnerability categories" at 100–200 probes each means 5,000–10,000+ API calls per run. Estimate cost before starting: at standard frontier model pricing, 10,000 calls × ~500 tokens each = ~5M tokens — check your billing dashboard and set a spend cap before the first run. Start with a single category and 10 probes to validate tooling, then scale.

After deployment, run red-teaming continuously — a test that passes today may fail after a model update or system prompt change. Schedule re-tests after every model update or significant prompt change.

**Why:** AI agents can be manipulated into ignoring their instructions or performing unintended actions. A 2025 study (arXiv:2505.04806, tested on GPT-4, Claude 2, Mistral 7B, and Vicuna over ~1,400 prompts) found roleplay-based prompt injection achieved an 89.6% attack success rate against models not specifically hardened against it. Indirect injection through retrieved content is particularly dangerous for RAG-based agents because the user is not the attacker — a malicious document in your retrieval store is.

**Caveat / contested:** Automated red-teaming reports higher success rates (69.5%) than manual-only efforts (47.6%), per Mulla et al. 2025 (arXiv:2504.19855, 214,271 attempts, 1,674 participants from Dreadnode). Manual testing finds more nuanced creative attacks that automated tools miss — both are needed. OWASP LLM Top 10 for 2025 lists prompt injection as the top risk, but the list itself is a snapshot; the attack surface evolves with each new model capability. Specific attack success rates come from testing particular model versions that may since have been patched. ⚠️ **WARNING:** Do not treat a passed red-team exercise as a permanent clearance.

**Sources:** [mindgard.ai — what-is-ai-red-teaming](https://mindgard.ai/blog/what-is-ai-red-teaming) (2026-07-18) · [confident-ai.com — best-ai-red-teaming-tools-2026](https://www.confident-ai.com/knowledge-base/compare/best-ai-red-teaming-tools-2026) (2026-07-18) · [arxiv.org/abs/2505.04806](https://arxiv.org/abs/2505.04806) — "Red Teaming the Mind of the Machine" (2025, roleplay ASR 89.6%) · [arxiv.org/abs/2504.19855](https://arxiv.org/abs/2504.19855) — Mulla et al. "The Automation Advantage in AI Red Teaming" (2025, automated 69.5% vs manual 47.6%)
**Confidence:** ✅ independently-corroborated (mindgard.ai, confident-ai.com, two arXiv papers — note: whiteknightlabs.com removed as a source for the statistics; it was cited in the draft but the cited page does not contain the 89.6% or 69.5%/47.6% figures)

---

## Practice: Understand evaluation metrics — BLEU/ROUGE have known limits; match metric to task

**Do:** Choose your automated evaluation metric based on what your task actually requires:
- **BLEU** (Bilingual Evaluation Understudy) — measures n-gram precision between your output and a reference; good for translation where exact wording matters; gives a score of 0 on any paraphrase that uses different words.
- **ROUGE** (Recall-Oriented Understudy for Gisting Evaluation) — measures recall of reference n-grams; favored for summarization where coverage matters; rewards copying source words, which can inflate scores for repetitive summaries.
- **chrF** — character-level F-score that handles morphologically rich languages better than word-level BLEU; commonly reported alongside BLEU in translation benchmarks.
- **BERTScore** — uses contextual embeddings from a transformer encoder to compare meaning rather than surface n-grams; more sensitive to paraphrase than BLEU.
- For agentic tasks: **task-completion rate** and **tool-call accuracy** are usually more informative than any of the above. When BLEU and BERTScore disagree on a sample, that disagreement is a signal — review those cases manually.

**Why:** BLEU gives 0 on short outputs and any paraphrase. ROUGE rewards copying source words, inflating scores for low-quality repetitive summaries. Neither metric "understands" what the text means. Beginners often pick BLEU because it is familiar, then wonder why a clearly better response scores lower than a worse one.

**Caveat / contested:** BERTScore is not a magic solution — it depends on which transformer encoder you use (BERT-base vs. RoBERTa-large give substantially different rankings), still requires reference texts, and runs slower than BLEU/ROUGE. For most agentic tasks, none of these metrics are the primary signal — use task-completion rate and human evaluation. Note: widely cited WMT 2025 correlation figures comparing BLEU and BERTScore at system level were not confirmed from the sources fetched this run and are omitted; consult WMT 2025 proceedings directly for current benchmark comparisons.

**Sources:** [metricgate.com — bertscore-vs-bleu-vs-rouge](https://metricgate.com/blogs/bertscore-vs-bleu-vs-rouge/) (2026-07-18)
**Confidence:** thin (only one directly fetched source; galileo.ai timed out; oreateai.com sourced via search snippet only — labeled thin to reflect single confirmed source)

---

## Practice: Use structured rubrics (G-Eval pattern) for model-graded scoring

**Do:** When an LLM judge must score subjective quality (not just pass/fail), use rubric-based evaluation: define 3–5 independent, non-overlapping criteria (e.g., accuracy, completeness, tone, safety), write explicit behavioral anchors for each score level (what a "1", "3", and "5" look like in practice), and ask the judge to reason through each criterion before assigning a final score. This is the G-Eval pattern: chain-of-thought reasoning grounded in explicit criteria, followed by probability-weighted scoring rather than a raw integer. Validate your rubric by scoring 30–50 examples manually and comparing to the judge.

**Why:** Asking an LLM to "rate this response 1–10" produces inconsistent and uninterpretable scores. Rubrics force the judge to reason explicitly, which both improves consistency and gives you a diagnostic trail when you disagree with a score. G-Eval's probability-weighted scoring — where the model emits a probability distribution over score tokens (e.g., 60% confident in "4", 40% in "5" → score 4.4) — is more stable than rounding to a single integer. Note: accessing token-level output probabilities is required for this approach; not all APIs expose this (check your provider's docs).

**Caveat / contested:** The judge model should be at least as capable as the model being evaluated — using a weaker model as judge is unreliable. Prometheus (an open-source 13B evaluator LM fine-tuned for rubric scoring, ICLR 2024) can approach GPT-4-level agreement on rubric evaluation tasks; the Prometheus GitHub repo is at [github.com/prometheus-eval/prometheus](https://github.com/prometheus-eval/prometheus) — not directly fetched this run but referenced in multiple practitioner guides. Rubric quality is the hard part — vague anchors produce inconsistent scores regardless of the framework used.

**Sources:** [qaskills.sh — rubric-based-llm-evaluation-guide-2026](https://qaskills.sh/blog/rubric-based-llm-evaluation-guide-2026) (2026-07-18) · [cameronrwolfe.substack.com — agent-evals](https://cameronrwolfe.substack.com/p/agent-evals) (2026-07-18)
**Confidence:** thin (qaskills.sh and cameronrwolfe.substack.com are two different publishers and were directly fetched; Prometheus primary sources — ICLR PDF and GitHub — not directly fetched this run)

---

## Practice: For agentic tasks, evaluate trajectories — not just final outputs

**Do:** Multi-step agents generate a trajectory: a sequence of tool calls, reasoning steps, and intermediate outputs before producing a final result. Define two metrics clearly before using them:
- **pass@k** — the agent succeeds on at least 1 of k independent runs ("best of k"). A 70% per-trial agent achieves 97% pass@3.
- **pass^k** — the agent succeeds on ALL k of k independent runs ("all of k"). A 70% per-trial agent achieves only 34% pass^3. This is the harsher and more realistic metric for tasks with no retry.

Evaluate the trajectory, not only the final answer. Key dimensions: (1) task-completion rate — verified by checking environmental state (e.g., did the database actually change?), not just the agent's claim; (2) tool-call correctness — did the agent call the right tools with valid arguments in a sensible order; (3) trajectory quality — coherent and goal-directed, with no infinite loops or redundant calls.

**Why:** An agent can produce a plausible-sounding final answer while having taken completely wrong intermediate steps. If you only check the final answer, you miss "correct by accident" cases and cannot diagnose why the agent fails in edge cases. Pass@3 vs. pass^3 is a 97% vs. 34% difference for a 70% agent — the metric you choose dramatically changes what "good enough" looks like.

**Caveat / contested:** Trajectory evaluation is significantly harder to automate than final-output evaluation. Checking "did the agent call the right tools in the right order" requires either hard-coded expected sequences (brittle) or an LLM judge evaluating the trajectory (expensive). The Amazon blog notes that for multi-agent systems, human-in-the-loop evaluation became critical precisely because automated metrics missed inter-agent communication failures and emergent behaviors. Industry predictions about agentic AI project cancellation rates should be treated as opinion, not verified measurements.

**Sources:** [braintrust.dev — ai-agent-evaluation-framework](https://www.braintrust.dev/articles/ai-agent-evaluation-framework) (2026-07-18) · [digitalapplied.com — ai-agent-evaluation-pipeline-2026](https://www.digitalapplied.com/blog/ai-agent-evaluation-pipeline-2026-testing-methodology) (2026-07-18) · [cameronrwolfe.substack.com — agent-evals](https://cameronrwolfe.substack.com/p/agent-evals) (2026-07-18) · [aws.amazon.com — evaluating-ai-agents-real-world-lessons](https://aws.amazon.com/blogs/machine-learning/evaluating-ai-agents-real-world-lessons-from-building-agentic-systems-at-amazon/) (2026-07-18)
**Confidence:** ✅ independently-corroborated (braintrust.dev, digitalapplied.com, cameronrwolfe.substack.com, AWS blog)

---

## Practice: Be skeptical of public benchmark scores — contamination inflates results

**Do:** When comparing models using public benchmarks (MMLU — tests general knowledge across 57 academic subjects; GSM8K — tests grade-school math word problems; HumanEval — tests Python code generation), treat published leaderboard scores with caution. Ask whether the benchmark data could have appeared in the model's pretraining corpus. For your own evaluation, use private hold-out test sets that were never published online, or use benchmarks sourced from content created after the model's training cutoff. When evaluating a vendor's model for your use case, run your own task-specific eval on your own data rather than relying solely on published benchmark scores.

**Why:** Multiple studies have found that widely used benchmarks are heavily contaminated — MMLU shows ~29.1% contamination signals, some multilingual benchmarks reach 91.8%. One study found a model's score dropped 13 percentage points when retested on a clean alternative set. If you select a model based on inflated benchmark numbers, you may deploy a model that performs worse on your actual task.

**Caveat / contested:** Contamination is hard to measure definitively — exact-match decontamination methods miss paraphrased or translated versions of contaminated items. Some researchers argue that memorizing benchmark answers still requires some generalization ability, so contamination may not fully explain performance gaps. Dynamic benchmarking approaches (LiveBench, LatestEval, LiveCodeBench) mitigate contamination by continuously refreshing test content from post-cutoff sources, but these are not yet universal. The contamination rates cited above come from specific audit studies and may not apply to all models equally.

**Sources:** [arxiv.org/html/2605.19999v1](https://arxiv.org/html/2605.19999v1) — "LLM Benchmark Datasets Should Be Contamination-Resistant" (2026-07-18) · [blog.pebblous.ai — llm-benchmark-contamination](https://blog.pebblous.ai/blog/llm-benchmark-contamination/en/) (2026-07-18)
**Confidence:** ✅ independently-corroborated (arXiv paper and pebblous.ai blog; contamination figures corroborated across both)

---

## Practice: Close the loop — use eval results to drive prompt iteration systematically

**Do:** Treat prompt improvement as an empirical loop, not intuition-based editing. The four-phase cycle: (1) **Define** — write down what "good" means for your task as testable criteria; (2) **Test** — run your current prompt against your golden dataset and record scores; (3) **Diagnose** — categorize failures to find systematic patterns (wrong tool choice, hallucinated facts, wrong format, etc.); (4) **Fix** — make targeted changes based on the root cause, then re-run against the same dataset to measure improvement and check for regressions. Never deploy a prompt change without running your eval set first.

**Why:** Prompt changes that seem obviously better can cause regressions on tasks you were not thinking about. A 2026 study ("When 'Better' Prompts Hurt: Evaluation-Driven Iteration for LLM Applications," Daniel Commey, arXiv:2601.22025v2, June 9, 2026) found that adding generic improvement rules to user prompts caused Qwen 2.5 to drop from 26/30 to 9/30 on a RAG citation task — a 65% regression — even while the same changes improved other task types. Without an eval loop, you would not catch this until it reached users.

**Caveat / contested:** The four-phase loop requires upfront investment in a good golden dataset and clear success criteria before it pays off. The CHI 2026 "Data-Prompt Co-Evolution" research suggests building the test set and the prompt iteratively together — letting each revealed failure shape both the dataset and the prompt — rather than front-loading all test case creation before any prompt work begins.

**Sources:** [arxiv.org/html/2601.22025v2](https://arxiv.org/html/2601.22025v2) — Daniel Commey, "When 'Better' Prompts Hurt: Evaluation-Driven Iteration for LLM Applications" (2026-07-18) · [braintrust.dev — prompt-optimization-loop](https://www.braintrust.dev/articles/prompt-optimization-loop) (2026-07-18)
**Confidence:** ✅ independently-corroborated (arXiv paper and braintrust.dev)

---

## Held pending fixes

- G-Eval probability-weighted scoring requires access to output token probabilities; not all providers expose this. Verify against your specific provider's API before implementing. ⚠ PENDING
- Prometheus (ICLR 2024) performance figures were not directly re-fetched from the ICLR proceedings PDF this run. Claims about Prometheus-vs-GPT-4 agreement rest on practitioner secondary sources.

## CHANGELOG (grading → this entry)
1. **[SKEPTIC FIX]** Red-teaming (Practice 7): Replaced whiteknightlabs.com as source for 89.6% ASR — real source is arXiv:2505.04806 ("Red Teaming the Mind of the Machine"). Added as direct citation.
2. **[SKEPTIC FIX]** Red-teaming (Practice 7): Replaced whiteknightlabs.com as source for automated 69.5% vs. manual 47.6% — real source is arXiv:2504.19855 (Mulla et al., Dreadnode). Added as direct citation.
3. **[SKEPTIC FIX]** BLEU/ROUGE (Practice 8): Removed WMT 2025 correlation figures (0.781–0.908 vs. 0.759–0.904) and "5–10× slower" — neither figure was supported by any fetched source (metricgate.com does not contain them). Added note directing readers to WMT 2025 proceedings.
4. **[BEGINNER KILL]** Red-teaming (Practice 7): Added prominent cost WARNING before running automated adversarial testing at scale, including worked token-cost estimate.
5. **[BEGINNER KILL]** LLM-as-judge (Practice 2): Replaced "cheap, fast, and scalable" framing with concrete cost warning and guidance on when to run full judge sweeps.
6. **[BEGINNER FIX]** LLM-as-judge (Practice 2): Added plain-language definition of Cohen's kappa.
7. **[BEGINNER FIX]** Regression CI (Practice 3): Added one-sentence definition of CI/CD and pull request.
8. **[BEGINNER FIX]** BLEU/ROUGE (Practice 8): Added plain-English one-sentence definition for each metric (BLEU, ROUGE, chrF, BERTScore) at first use in Do section.
9. **[BEGINNER FIX]** G-Eval (Practice 9): Added note that probability-weighted scoring requires access to output token probabilities; not available on all providers.
10. **[BEGINNER FIX]** Trajectory evaluation (Practice 10): Moved pass^k and pass@k definitions to the Do section before the notation is used; concrete example retained in Why.
11. **[BEGINNER FIX]** Golden dataset (Practice 1): Added parenthetical definitions for JSONL and "diffable."
12. **[BEGINNER FIX]** Benchmark contamination (Practice 11): Added one-line explanations of MMLU, GSM8K, and HumanEval.
13. **[TIMEKEEPER FIX]** Close the loop (Practice 12): Corrected arXiv 2601.22025 title to "When 'Better' Prompts Hurt: Evaluation-Driven Iteration for LLM Applications" (canonical form from arXiv abstract page).
14. **[TIMEKEEPER FIX]** Regression CI (Practice 3): Updated Promptfoo version to 0.121.19 (released 2026-07-14), star count to ~23,400; added note about March 2026 OpenAI acquisition and continued open-source/multi-provider status.
15. **[AUDIENCE FIX]** Front matter: corrected `audience` from "people new to AI" to "technically comfortable readers" (was a draft error — this is the best-practices track).
16. **[LINK-CHECK]** Regression CI (Practice 3): medium.com/@alexrodriguesj article confirmed live via WebFetch (403 = bot-protection, not dead). Unlinked to plain text per policy; citation retained with title.

