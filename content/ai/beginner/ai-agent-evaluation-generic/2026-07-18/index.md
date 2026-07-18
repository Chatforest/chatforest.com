---
title: "AI Agent Evaluation and Testing — Best Practices (as of 18 Jul 2026)"
date: 2026-07-18
snapshot_date: 2026-07-18
topic: ai-agent-evaluation-generic
track: beginner
audience: "people new to AI"
description: "Plain-language guide to evaluating and testing AI agents: golden datasets, LLM-as-judge, regression CI, unit mocking, red-teaming, evaluation metrics, and trajectory evaluation."
content_type: "Best Practice"
categories: ["AI Agents", "Evaluation", "Testing"]
tags: ["evaluation", "testing", "llm-as-judge", "regression-testing", "red-teaming", "golden-dataset", "benchmarking", "agent-evals"]
last_refreshed: 2026-07-18
graded_by: "RingS panel (Skeptic/Beginner/Timekeeper) + sensei, 2026-07-18"
grading_result: "0 fabrications; beginner re-level by rings-beginner-author, 2026-07-18"
---

<!-- This file lands at content/ai/beginner/ai-agent-evaluation-generic/2026-07-18/index.md
     and is an IMMUTABLE dated snapshot. Once published it is never edited.
     Re-leveled from the 2026-07-18 technical entry; facts unchanged. -->

# AI Agent Evaluation and Testing — Plain-Language Guide (as of 18 Jul 2026)

> **What this is.** A dated snapshot — accurate as of **18 Jul 2026**, frozen here as a permanent
> archive entry. This is the beginner-track version: same facts as the technical entry, written for
> someone who has used ChatGPT but has never built an AI application.

## What is an "AI agent"?

An AI agent is a program that uses a language model (like GPT-4 or Claude) to make decisions and
take actions — it might search the web, call an API, write and run code, or fill out a form.
Because agents do things in the real world, testing them matters: a broken agent can send wrong
emails, delete data, or give dangerous advice.

## How to read the labels

- ✅ **independently-corroborated** — 2 or more independent publishers confirmed this
- 📄 **vendor-documented** — official docs only (authoritative, single source)
- ⚠️ **WARNING** — a default that can cost money, break the machine, or remove a safety net
- 🕒 **verify live** — this changes fast (versions, prices, quotas); check the current value before acting

---

## Practice 1: Build and maintain a "golden dataset" from real failures

**Do:** Collect a set of real examples — actual inputs your agent received, paired with the correct
output you wanted. Do not invent test cases from imagination. Start with 50–100 examples (roughly
40–60 core cases plus 15–25 edge cases), grow to 150–300 as your product matures. Store them in
**JSONL format** ("one JSON object per line" — a plain text file where each line is one test case,
easy to compare changes in version control) inside a version control system like Git, alongside
your prompts. Every time your agent fails in production, add that failure as a new test case.

**Why it matters:** Real users find problems you would never think to test. A dataset built from
actual failures catches the problems that hurt real people. Made-up tests miss the unusual but
real situations that break things.

**What goes wrong without this:** Your agent passes all your hand-crafted tests but fails the
moment a real user asks something slightly different. You have no record of what broke and when.

**Caveat / contested:** How many examples you need is debated. One practitioner guide says 50–100
is enough for early work. An academic guide recommends about 246 samples per scenario at 95%
confidence with a 5% margin of error. The right number depends on how varied your task is. Keep
your few-shot prompt examples (examples you show the model to teach it) strictly separate from
your evaluation cases — if they overlap, your scores look better than they are (this is called
"data leakage"). ⚠️ **WARNING:** Do not put real user information (names, emails, addresses — any
PII, or Personally Identifiable Information) into your golden dataset without removing it first.

**Sources:** [qaskills.sh — golden-dataset-llm-evaluation-guide](https://qaskills.sh/blog/golden-dataset-llm-evaluation-guide) (2026-07-18) · [getmaxim.ai — building-a-golden-dataset](https://www.getmaxim.ai/articles/building-a-golden-dataset-for-ai-evaluation-a-step-by-step-guide/) (2026-07-18) · [digitalapplied.com — ai-agent-evaluation-pipeline-2026](https://www.digitalapplied.com/blog/ai-agent-evaluation-pipeline-2026-testing-methodology) (2026-07-18)
**Confidence:** ✅ independently-corroborated (qaskills.sh, getmaxim.ai, digitalapplied.com)

---

## Practice 2: Use LLM-as-judge carefully — calibrate against humans before trusting it

**What is LLM-as-judge?** Instead of a human scoring every output, you send the output to a second
AI model and ask it to rate the quality. This is fast and can handle many outputs at once, but it
has real costs and real biases.

**Do:** When you need to evaluate open-ended outputs (answers that cannot simply be marked
right/wrong), use a second LLM as a judge. Write a clear rubric (a scoring guide) for the judge.
Ask it to explain its reasoning before giving a score. Use simple scales — pass/fail, or 1–3 —
rather than 1–10 or 1–100. Set the judge model's temperature (a setting that controls how random
the output is) to 0.1–0.2 for consistent results.

Before you use any LLM judge to automatically block a release or fail a build, first score at
least 30–50 examples by hand and compare your scores to the judge's scores. Aim for more than 85%
agreement. Track **Cohen's kappa** — a number from −1 to 1 measuring how much two raters agree
beyond pure chance; 0 means they agree no more than chance would predict; 0.6 means moderate,
useful agreement; 1.0 means perfect agreement. Aim for a kappa of at least 0.6.

⚠️ **WARNING (cost):** Each judge call costs real money. Running a 500-case golden dataset through
a judge model on every automated check adds up fast. At standard frontier model pricing, 500 cases
times about 2,000 tokens each equals about 1 million tokens per run — check what that costs before
you start. Use a cheaper model as the judge where quality allows, and consider running full judge
sweeps only when merging finished work rather than on every small change.

**Why it matters:** LLM judges are fast but carry predictable biases: they tend to prefer longer
answers (verbosity bias), prefer the first option when comparing two outputs (position bias), and
may favor outputs from models in the same family as themselves (self-preference bias). Without
calibrating against humans, you are trusting a biased, unchecked scorer.

**What goes wrong without this:** An uncalibrated LLM judge can silently pass bad outputs or block
good ones. You might ship a regression you never caught, or spend days debugging a CI failure that
was never actually a real problem.

**Caveat / contested:** Research on "Panels of LLM Evaluators" (PoLL) suggests that using several
smaller, diverse models as a committee works better than one large model — but also costs more.
Having a model judge its own outputs (self-evaluation) is especially unreliable and should be
avoided. ⚠️ **WARNING:** An uncalibrated LLM judge that gates builds can silently pass regressions
or block good changes — treat it as infrastructure that needs ongoing monitoring.

**Sources:** [mer.vin — llm-as-a-judge-best-practices](https://mer.vin/2025/11/llm-as-a-judge-best-practices-for-consistent-evaluation/) (2026-07-18) · [digitalapplied.com — ai-agent-evaluation-pipeline-2026](https://www.digitalapplied.com/blog/ai-agent-evaluation-pipeline-2026-testing-methodology) (2026-07-18) · [cameronrwolfe.substack.com — agent-evals](https://cameronrwolfe.substack.com/p/agent-evals) (2026-07-18)
**Confidence:** ✅ independently-corroborated (mer.vin, digitalapplied.com, cameronrwolfe.substack.com)

---

## Practice 3: Treat prompts like code — run automated checks before merging changes

**What is a CI pipeline?** CI stands for Continuous Integration. It is an automated process that
checks your code (and your prompts) every time you make a change — usually before that change is
merged into the shared project. A **pull request** is a proposal to merge your change; CI runs
automatically when you open one.

**Do:** Add an automated evaluation step to your CI pipeline. Each time you open a pull request,
run a fast smoke-test of 20–50 prompts. When you merge to the main branch, run a full set of
200–500 prompts. Fail the build automatically if the pass-rate drops below a threshold — 95% is a
common choice. Store your prompts as plain text or YAML files in version control, not buried inside
application code.

**Recommended tool:** Promptfoo is an open-source tool (acquired by OpenAI in March 2026 but
remains MIT-licensed and works with multiple AI providers, with about 23,400 GitHub stars as of
2026-07-14). It uses YAML configuration files, supports multiple assertion types, and integrates
with GitHub Actions (GitHub Actions requires a GitHub account). You define your test cases in a
file, and Promptfoo runs them and reports results.

🕒 **verify live:** Promptfoo version 0.121.19 (released 2026-07-14) — confirm the current stable
release before using. The March 2026 OpenAI acquisition did not change the license or provider
support, but verify at [promptfoo.dev/blog/promptfoo-joining-openai](https://www.promptfoo.dev/blog/promptfoo-joining-openai/) for any updates.

**Why it matters:** Prompts are instructions to your agent. Changing one word can flip how the
agent responds in ways that are not obvious. Without an automated check, a well-intentioned prompt
edit can silently make things worse for real users before anyone notices.

**What goes wrong without this:** You change a prompt to fix one problem and unknowingly break
three others. You find out when users complain.

**Caveat / contested:** Model-graded checks are not perfectly repeatable — the same prompt can
score differently on two consecutive runs. Use a pass-rate threshold (for example, 95% pass over N
runs) rather than requiring every single test to pass every single time. Tune the threshold to your
own system's noise level.

**Sources:** medium.com/@alexrodriguesj — "Testing LLM prompts like code: regression evals in CI/CD with promptfoo" (2026-07-18; confirmed live via WebFetch, unlinked — Medium returns 403 to bots) · [scrolltest.com — llm-regression-testing-promptfoo](https://scrolltest.com/llm-regression-testing-promptfoo/) (2026-07-18) · [traceloop.com — automated-prompt-regression-testing](https://www.traceloop.com/blog/automated-prompt-regression-testing-with-llm-as-a-judge-and-ci-cd) (2026-07-18)
**Confidence:** ✅ independently-corroborated (Medium/alexrodriguesj — confirmed live, unlinked; scrolltest.com; traceloop.com)

---

## Practice 4: Unit-test your agent's logic by faking the AI — test your code, not the model

**What does "mocking" mean?** A mock is a fake replacement for something your code depends on. In
this case, instead of sending a real request to an AI API (which costs money, takes seconds, and
gives slightly different results every time), you replace it with a fake that returns a fixed,
predictable response. This lets you test whether your code handles the response correctly, without
actually calling the AI.

**Do:** Replace real LLM API calls with fake (mock) objects in your unit tests. `unittest.mock` and
`pytest` are general-purpose Python testing tools — not AI-specific — that can do this. Assert on
what your code does with the LLM's response: did it pick the right tool? Did it retry when the
output was malformed? Did it parse the JSON correctly? Keep a small library of 5–10 saved fake
responses covering: normal responses, tool-call responses, refusals, malformed outputs, and empty
responses. Place the mock at the boundary between your code and the AI client, not deep inside
your agent's logic.

**Why it matters:** Real LLM calls are slow (seconds per call), cost money on every request, hit
rate limits, and produce slightly different outputs each run even at the lowest randomness setting.
Mocking removes those dependencies so you can test fast and for free.

**What goes wrong without this:** Your tests take minutes instead of seconds, cost money every
time you run them, and sometimes fail randomly because the model gave a slightly different answer.
You avoid running tests because they're slow, so bugs pile up.

**Caveat / contested:** Mocked tests do not catch problems caused by model behavior changes or
prompt sensitivity. Those require tests that call the real model. Aim for a combination: mocked
unit tests for your business logic, plus a smaller set of integration tests that call the real
model. ⚠️ **WARNING:** If you mock at the wrong level (for example, replacing your agent's internal
reasoning function rather than the AI API client), your tests give false confidence — they pass
even when the real integration is broken.

**Sources:** [callsphere.ai — unit-testing-ai-agents-mocking-llm-calls](https://callsphere.ai/blog/unit-testing-ai-agents-mocking-llm-calls-deterministic-tests) (2026-07-18) · [langwatch.ai — scenario-testing-guides-mocks](https://langwatch.ai/scenario/testing-guides/mocks/) (2026-07-18) · [arxiv.org/html/2601.18827v1](https://arxiv.org/html/2601.18827v1) — automated structural testing via OTel traces + mocking (2026-07-18) (arXiv is a free, open-access repository where researchers share papers before or alongside formal publication)
**Confidence:** ✅ independently-corroborated (callsphere.ai, langwatch.ai, arXiv paper)

---

## Practice 5: Measure speed and cost — not just accuracy

**Do:** For every evaluation run, record: time-to-first-token (TTFT — how long until the agent
starts responding) at the typical case (p50) and the slow tail (p95 — the slowest 5% of
responses), total response time at p50 and p95, input and output token counts, and estimated API
cost per successful task. Set latency budgets based on what your users experience: for interactive
chat, target p95 TTFT under 2 seconds; for real-time voice, under 1 second. Include these metrics
in your CI as secondary gates — warn or fail when p95 latency spikes or cost per task exceeds your
threshold.

🕒 **verify live:** Specific latency numbers depend on the model and provider, and change as
providers update their infrastructure. The figures here are from mid-2026 testing — recheck before
setting your own targets.

**Why it matters:** A model that gives perfect answers in 30 seconds is unusable in a chat product.
Cost per task tells you whether your agent is economically viable at real traffic volumes. P95
matters more than the average because the slowest 5% of responses define the worst experience real
users encounter. One 2026 benchmark suite found P95 can be about 2.1 times slower than P50 on
average, and can reach 3.2 times in production; reasoning-mode models (where the model thinks
longer before answering) can make TTFT 5–30 times higher.

**What goes wrong without this:** Teams ship agents that work perfectly in testing but are too slow
or too expensive for real traffic. They discover this after launch.

**Caveat / contested:** The 2.1× P95/P50 ratio is from one benchmark suite (digitalapplied.com,
mid-2026) and may not reflect your stack. Token cost figures change when providers update pricing.
⚠️ **WARNING:** Evaluating only accuracy and ignoring latency/cost has led teams to ship agents
that are prohibitively slow or expensive for real traffic volumes.

**Sources:** [aviso.com — how-to-evaluate-ai-agents-latency-cost](https://www.aviso.com/blog/how-to-evaluate-ai-agents-latency-cost-safety-roi) (2026-07-18) · [digitalapplied.com — ai-model-latency-benchmarks-2026](https://www.digitalapplied.com/blog/ai-model-latency-benchmarks-2026-ttft-throughput) (2026-07-18)
**Confidence:** ✅ independently-corroborated (aviso.com and digitalapplied.com are different publishers)

---

## Practice 6: Use human review for the cases automated tools miss

**Do:** Do not rely on automated scorers or LLM judges alone. Set up a human review queue — a list
of agent outputs waiting for a human to label — where a sample of real outputs, especially
failures, user complaints, and low-confidence automated scores, go to domain experts for review.
Use structured rubrics with multiple dimensions (accuracy, tone, completeness, safety) rather than
a single overall rating. Track how consistently different reviewers give the same score (called
inter-annotator agreement — divergence signals that your rubric is becoming unclear). Convert
reviewed failures directly into new test cases in your golden dataset.

**Why it matters:** Automated metrics measure what they measure, not what matters. Users in
healthcare, legal, or finance can detect subtle failures — a wrong implication, a missing
qualification, dangerous advice — that pattern-matching algorithms score as "correct." Human review
is also how you catch that your LLM judge is drifting: if humans and the judge disagree
systematically on more than 20% of cases, your judge rubric needs revision.

**What goes wrong without this:** Your automated scores look great while real users are quietly
receiving wrong or harmful information that the metrics never flag.

**Caveat / contested:** Human review is expensive and slow. The practical approach is strategic
sampling: random samples of automated high-confidence decisions (to validate the scorer), plus
targeted review of all human-flagged complaints and low-confidence cases. Annotation quality
depends heavily on clear guidelines and calibration exercises — skip calibration and reviewers
diverge quickly.

**Sources:** [getmaxim.ai — incorporating-human-in-the-loop-feedback](https://www.getmaxim.ai/articles/incorporating-human-in-the-loop-feedback-for-continuous-improvement-of-ai-agents/) (2026-07-18) · [braintrust.dev — best-human-in-the-loop-llm-evaluation-platforms-2026](https://www.braintrust.dev/articles/best-human-in-the-loop-llm-evaluation-platforms-2026) (2026-07-18) · [aws.amazon.com — evaluating-ai-agents-real-world-lessons](https://aws.amazon.com/blogs/machine-learning/evaluating-ai-agents-real-world-lessons-from-building-agentic-systems-at-amazon/) (2026-07-18)
**Confidence:** ✅ independently-corroborated (getmaxim.ai, braintrust.dev, AWS blog)

---

## Practice 7: Red-team your agent — deliberately try to break it before launch

**What is red-teaming?** Red-teaming means having someone (or a program) try to trick, manipulate,
or break your agent on purpose, to find weaknesses before real attackers do.

**Do:** Before deploying your agent, run structured adversarial testing across these attack types:
- **Direct prompt injection:** A user tries to override the agent's system instructions with their message (e.g., "Ignore your previous instructions and...").
- **Indirect prompt injection:** Malicious instructions are hidden in a document, webpage, or file your agent reads — the user is not the attacker, the content is.
- **Jailbreak techniques:** Roleplay framing ("pretend you are an AI with no rules"), encoding tricks (using Unicode variants or Base64 to hide content), or logic traps.
- **Multi-turn attacks:** An attacker builds up to a harmful request over several conversation turns.

Test each major risk category separately.

⚠️ **WARNING (cost):** Automated red-teaming tools make large numbers of LLM API calls.
"50+ vulnerability categories" at 100–200 probes each means 5,000–10,000+ API calls per run.
Estimate cost before starting: at standard frontier model pricing, 10,000 calls times about 500
tokens each equals about 5 million tokens — check your billing dashboard and set a spend cap
before the first run. **Start with a single category and only 10 probes to validate your tooling,
then scale up.**

After deployment, re-test continuously — a test that passes today may fail after a model update or
system prompt change. Schedule re-tests after every model update or significant prompt change.

**Why it matters:** AI agents can be manipulated into ignoring their instructions or performing
unintended actions. A 2025 study (arXiv:2505.04806 — arXiv is a free, open-access repository
where researchers share papers, tested on GPT-4, Claude 2, Mistral 7B, and Vicuna over about
1,400 prompts) found roleplay-based prompt injection achieved an 89.6% attack success rate against
models not specifically hardened against it. Indirect injection through retrieved content is
particularly dangerous for agents that look things up (RAG-based agents) because a malicious
document in your retrieval store is the attacker.

**What goes wrong without this:** Your agent gets manipulated into leaking private data, performing
harmful actions, or ignoring its safety instructions — and you find out from a user or a news
article, not from your own testing.

**Caveat / contested:** Automated red-teaming finds more attacks faster (69.5% success rate in one
study) than manual-only efforts (47.6%), per Mulla et al. 2025 (arXiv:2504.19855, 214,271
attempts, 1,674 participants from Dreadnode). Manual testing finds more nuanced creative attacks
that automated tools miss — both are needed. OWASP LLM Top 10 for 2025 lists prompt injection as
the top risk, but the list itself is a snapshot; the attack surface evolves with each new model
capability. Specific attack success rates come from testing particular model versions that may
since have been patched. ⚠️ **WARNING:** Do not treat a passed red-team exercise as a permanent
clearance.

**Sources:** [mindgard.ai — what-is-ai-red-teaming](https://mindgard.ai/blog/what-is-ai-red-teaming) (2026-07-18) · [confident-ai.com — best-ai-red-teaming-tools-2026](https://www.confident-ai.com/knowledge-base/compare/best-ai-red-teaming-tools-2026) (2026-07-18) · [arxiv.org/abs/2505.04806](https://arxiv.org/abs/2505.04806) — "Red Teaming the Mind of the Machine" (2025, roleplay ASR 89.6%) · [arxiv.org/abs/2504.19855](https://arxiv.org/abs/2504.19855) — Mulla et al. "The Automation Advantage in AI Red Teaming" (2025, automated 69.5% vs manual 47.6%)
**Confidence:** ✅ independently-corroborated (mindgard.ai, confident-ai.com, two arXiv papers — note: whiteknightlabs.com removed as a source for the statistics; it was cited in the draft but the cited page does not contain the 89.6% or 69.5%/47.6% figures)

---

## Practice 8: Understand evaluation metrics — match the metric to your task

Automated metrics give you a number to compare outputs. Each metric has a different definition of
"good." Here are the main ones, in plain language:

- **BLEU** (Bilingual Evaluation Understudy) — counts how many short word sequences (n-grams) your
  output shares with a reference answer. Originally designed for translation where exact wording
  matters. Limitation: gives a score of 0 for any paraphrase that uses different words, even if the
  meaning is identical.
- **ROUGE-1, ROUGE-2, ROUGE-L** (Recall-Oriented Understudy for Gisting Evaluation) — measures
  how much of the reference answer appears in your output. Favored for summarization where coverage
  matters. Limitation: rewards copying source words, which can inflate scores for repetitive,
  low-quality summaries.
- **chrF** (character-level F-score) — compares outputs character-by-character rather than
  word-by-word. Handles languages with complex word structures better than BLEU. Commonly reported
  alongside BLEU in translation benchmarks.
- **BERTScore** — uses a neural language model to compare the meaning of your output against the
  reference, rather than just counting matching words. More sensitive to paraphrase than BLEU.
  Limitation: depends on which underlying model is used (different model choices give substantially
  different rankings), still requires reference texts, and is slower to compute than BLEU or ROUGE.

**For agentic tasks specifically:** Task-completion rate (did the agent actually achieve the goal?)
and tool-call accuracy (did it call the right tools with the right inputs?) are usually more
informative than any of the metrics above. When BLEU and BERTScore disagree on a sample, that
disagreement is a signal worth investigating — review those cases manually.

**Do:** Choose your metric based on what your task actually requires. Do not default to BLEU
because it is familiar.

**Why it matters:** BLEU gives 0 on short outputs and any paraphrase. ROUGE rewards copying source
words. Neither "understands" what the text means. Beginners often pick BLEU, then wonder why a
clearly better response scores lower than a worse one.

**What goes wrong without this:** You optimize your agent toward a metric that does not match what
you actually care about, and users get worse answers while your scores go up.

**Caveat / contested:** BERTScore is not a magic solution — it depends on which model you use
internally (BERT-base vs. RoBERTa-large give substantially different rankings), still requires
reference texts, and runs slower than BLEU/ROUGE. For most agentic tasks, none of these metrics
are the primary signal — use task-completion rate and human evaluation. Note: widely cited WMT
2025 correlation figures comparing BLEU and BERTScore at system level were not confirmed from the
sources fetched this run and are omitted; consult WMT 2025 proceedings directly for current
benchmark comparisons.

**Sources:** [metricgate.com — bertscore-vs-bleu-vs-rouge](https://metricgate.com/blogs/bertscore-vs-bleu-vs-rouge/) (2026-07-18)
**Confidence:** thin (only one directly fetched source; galileo.ai timed out; oreateai.com sourced via search snippet only — labeled thin to reflect single confirmed source)

---

## Practice 9: Use structured rubrics (the G-Eval pattern) for model-graded scoring

**What is the G-Eval pattern?** It is a way of getting more consistent scores from an LLM judge
by giving it a structured scoring guide (rubric) and asking it to reason step by step before
scoring. "G-Eval" is the name of the research pattern behind this approach.

**Do:** When an LLM judge must score subjective quality (not just pass/fail), define 3–5
independent, non-overlapping criteria — for example: accuracy, completeness, tone, and safety.
For each criterion, write explicit anchors describing what a "1", "3", and "5" look like in
practice. Ask the judge to reason through each criterion before assigning a final score.

The G-Eval pattern uses **probability-weighted scoring**: instead of having the model output a
single integer, you look at the model's internal confidence across possible score tokens — for
example, 60% confident in "4" and 40% confident in "5" gives a weighted score of 4.4 — which is
more stable than rounding to a single integer. Important: accessing these token-level output
probabilities requires your AI provider to expose that data. Not all APIs do. Check your
provider's documentation before relying on this approach.

Validate your rubric by scoring 30–50 examples by hand and comparing to the judge.

**Why it matters:** Asking an LLM to "rate this response 1–10" produces inconsistent and
uninterpretable scores. Rubrics force the judge to reason explicitly, which both improves
consistency and gives you a diagnostic trail when you disagree with a score.

**What goes wrong without this:** You get numbers that feel meaningful but are actually noise —
the same output scores 3 one day and 7 the next.

**Caveat / contested:** The judge model should be at least as capable as the model being evaluated
— using a weaker model as judge is unreliable. Prometheus is an open-source evaluator model (a
13-billion parameter model fine-tuned specifically for rubric scoring, presented at ICLR 2024) that
can approach GPT-4-level agreement on rubric evaluation tasks; the Prometheus GitHub repo is at
[github.com/prometheus-eval/prometheus](https://github.com/prometheus-eval/prometheus) — not
directly fetched this run but referenced in multiple practitioner guides. Rubric quality is the
hard part — vague anchors produce inconsistent scores regardless of the framework used.

**Sources:** [qaskills.sh — rubric-based-llm-evaluation-guide-2026](https://qaskills.sh/blog/rubric-based-llm-evaluation-guide-2026) (2026-07-18) · [cameronrwolfe.substack.com — agent-evals](https://cameronrwolfe.substack.com/p/agent-evals) (2026-07-18)
**Confidence:** thin (qaskills.sh and cameronrwolfe.substack.com are two different publishers and were directly fetched; Prometheus primary sources — ICLR PDF and GitHub — not directly fetched this run)

---

## Practice 10: For multi-step agents, evaluate the journey — not just the final answer

**What is a "trajectory"?** When an agent works through a task, it takes multiple steps: it picks
a tool, calls it, reads the result, picks another tool, and so on. This sequence of steps is called
a trajectory.

**Two key metrics — defined before you encounter the notation:**

- **pass@k** ("pass at k") — the agent succeeds on at least 1 out of k independent attempts at
  the same task. Example: a 70% per-attempt agent achieves 97% pass@3. This is a forgiving metric —
  it only needs one success out of several tries.
- **pass^k** ("pass hat k") — the agent succeeds on ALL k of k independent attempts. Example: a
  70% per-attempt agent achieves only 34% pass^3. This is the harsher and more realistic metric for
  tasks where there is no retry — the agent must succeed every time.

The metric you choose dramatically changes what "good enough" looks like: 97% vs. 34% for the
same 70% agent.

**Do:** Evaluate the full trajectory, not only the final answer. Three dimensions to check:
1. **Task-completion rate** — verify by checking whether the actual environment changed (for
   example, did the database actually update?), not just by trusting what the agent says it did.
2. **Tool-call correctness** — did the agent call the right tools with valid arguments in a
   sensible order?
3. **Trajectory quality** — was the path to the answer coherent and goal-directed, with no
   infinite loops or redundant calls?

**Why it matters:** An agent can produce a plausible-sounding final answer while having taken
completely wrong intermediate steps. If you only check the final answer, you miss "correct by
accident" cases and cannot diagnose why the agent fails in edge cases.

**What goes wrong without this:** Your agent looks like it works in testing, but in production it
occasionally takes destructive side paths — deleting data, sending duplicate requests, or getting
stuck in a loop — and the final answer looks fine while the damage is already done.

**Caveat / contested:** Trajectory evaluation is significantly harder to automate than
final-output evaluation. Checking "did the agent call the right tools in the right order"
requires either hard-coded expected sequences (brittle) or an LLM judge evaluating the trajectory
(expensive). The Amazon blog notes that for multi-agent systems, human-in-the-loop evaluation
became critical precisely because automated metrics missed inter-agent communication failures and
emergent behaviors. Industry predictions about agentic AI project cancellation rates should be
treated as opinion, not verified measurements.

**Sources:** [braintrust.dev — ai-agent-evaluation-framework](https://www.braintrust.dev/articles/ai-agent-evaluation-framework) (2026-07-18) · [digitalapplied.com — ai-agent-evaluation-pipeline-2026](https://www.digitalapplied.com/blog/ai-agent-evaluation-pipeline-2026-testing-methodology) (2026-07-18) · [cameronrwolfe.substack.com — agent-evals](https://cameronrwolfe.substack.com/p/agent-evals) (2026-07-18) · [aws.amazon.com — evaluating-ai-agents-real-world-lessons](https://aws.amazon.com/blogs/machine-learning/evaluating-ai-agents-real-world-lessons-from-building-agentic-systems-at-amazon/) (2026-07-18)
**Confidence:** ✅ independently-corroborated (braintrust.dev, digitalapplied.com, cameronrwolfe.substack.com, AWS blog)

---

## Practice 11: Be skeptical of public benchmark scores — contamination inflates results

**What is benchmark contamination?** AI models are trained on huge amounts of text from the
internet. If the answers to a benchmark's test questions appeared in that training text, the model
may have memorized the answers — not learned to reason. This makes its scores look better than its
real-world ability.

**Common benchmarks, briefly defined:**
- **MMLU** (Massive Multitask Language Understanding) — tests general knowledge across 57 academic
  subjects, from history to biology to law.
- **GSM8K** (Grade School Math 8K) — tests grade-school math word problems.
- **HumanEval** — tests Python programming tasks (writing and completing code).

**Do:** When comparing models using public benchmarks, treat published leaderboard scores with
caution. Ask whether the benchmark data could have appeared in the model's pretraining text. For
your own evaluation, use private test sets that were never published online, or use benchmarks
sourced from content created after the model's training cutoff. When evaluating a vendor's model
for your use case, run your own task-specific evaluation on your own data rather than relying
solely on published benchmark scores.

**Why it matters:** Multiple studies have found that widely used benchmarks are heavily
contaminated — MMLU shows about 29.1% contamination signals, and some multilingual benchmarks
reach 91.8%. One study found a model's score dropped 13 percentage points when retested on a
clean alternative set. If you select a model based on inflated benchmark numbers, you may deploy a
model that performs worse on your actual task.

**What goes wrong without this:** You pick a model because it tops a leaderboard, then discover it
performs far worse on your real users' questions.

**Caveat / contested:** Contamination is hard to measure definitively — exact-match
decontamination methods miss paraphrased or translated versions of contaminated items. Some
researchers argue that memorizing benchmark answers still requires some generalization ability, so
contamination may not fully explain performance gaps. Dynamic benchmarking approaches (LiveBench,
LatestEval, LiveCodeBench) mitigate contamination by continuously refreshing test content from
post-cutoff sources, but these are not yet universal. The contamination rates cited above come
from specific audit studies and may not apply to all models equally.

**Sources:** [arxiv.org/html/2605.19999v1](https://arxiv.org/html/2605.19999v1) — "LLM Benchmark Datasets Should Be Contamination-Resistant" (2026-07-18) · [blog.pebblous.ai — llm-benchmark-contamination](https://blog.pebblous.ai/blog/llm-benchmark-contamination/en/) (2026-07-18)
**Confidence:** ✅ independently-corroborated (arXiv paper and pebblous.ai blog; contamination figures corroborated across both)

---

## Practice 12: Close the loop — use eval results to drive prompt changes systematically

**Do:** Treat prompt improvement as an empirical loop — a repeating cycle driven by data — not
intuition-based editing. The four-phase cycle:

1. **Define** — write down what "good" means for your task as testable criteria before you start.
2. **Test** — run your current prompt against your golden dataset and record scores.
3. **Diagnose** — categorize failures to find systematic patterns: wrong tool choice, hallucinated
   facts, wrong format, and so on.
4. **Fix** — make targeted changes based on the root cause, then re-run against the same dataset
   to measure improvement and check for regressions.

Never deploy a prompt change without running your evaluation set first.

**Why it matters:** Prompt changes that seem obviously better can cause regressions on tasks you
were not thinking about. A 2026 study ("When 'Better' Prompts Hurt: Evaluation-Driven Iteration
for LLM Applications," Daniel Commey, arXiv:2601.22025v2, June 9, 2026) found that adding generic
improvement rules to user prompts caused Qwen 2.5 to drop from 26/30 to 9/30 on a RAG citation
task — a 65% regression — even while the same changes improved other task types. Without an eval
loop, you would not catch this until it reached users.

**What goes wrong without this:** You "improve" a prompt, break something else, and find out when
users start complaining about a problem that your intuition said you had fixed.

**Caveat / contested:** The four-phase loop requires upfront investment in a good golden dataset
and clear success criteria before it pays off. The CHI 2026 "Data-Prompt Co-Evolution" research
suggests building the test set and the prompt iteratively together — letting each revealed failure
shape both the dataset and the prompt — rather than front-loading all test case creation before any
prompt work begins.

**Sources:** [arxiv.org/html/2601.22025v2](https://arxiv.org/html/2601.22025v2) — Daniel Commey, "When 'Better' Prompts Hurt: Evaluation-Driven Iteration for LLM Applications" (2026-07-18) · [braintrust.dev — prompt-optimization-loop](https://www.braintrust.dev/articles/prompt-optimization-loop) (2026-07-18)
**Confidence:** ✅ independently-corroborated (arXiv paper and braintrust.dev)

---

## Held pending fixes

- G-Eval probability-weighted scoring requires access to output token probabilities; not all providers expose this. Verify against your specific provider's API before implementing. ⚠ PENDING
- Prometheus (ICLR 2024) performance figures were not directly re-fetched from the ICLR proceedings PDF this run. Claims about Prometheus-vs-GPT-4 agreement rest on practitioner secondary sources.

---

## CHANGELOG

### Re-leveled from the 2026-07-18 technical entry; facts unchanged.

The following changes were made relative to the technical (best-practices track) entry. No new
facts, statistics, or URLs were introduced.

**KILL fixes (required by beginner grading panel):**
1. **[BEGINNER KILL — Practice 7]** Added prominent cost WARNING before running automated
   red-teaming at scale, including the worked token-cost estimate already present in the technical
   entry. Moved the WARNING earlier in the practice and added explicit instruction to start with a
   single category and 10 probes.
2. **[BEGINNER KILL — Practice 2]** Replaced any implication that LLM-as-judge is simply "fast and
   scalable" with explicit framing that each judge call costs real money. Retained the full cost
   WARNING and token-cost example from the technical entry.

**FIX corrections (required by beginner grading panel):**
3. **[BEGINNER FIX — Practice 2]** Added plain-English definition of Cohen's kappa (a number from
   −1 to 1; 0.6 = moderate agreement) at first use, expanding the definition already present in
   the technical entry's Do section.
4. **[BEGINNER FIX — Practice 3]** Added one-sentence definition of "CI pipeline" and "pull
   request" before the Do section. Added note that GitHub Actions requires a GitHub account.
5. **[BEGINNER FIX — Practice 8]** Added plain-English one-sentence definitions for BLEU, ROUGE,
   chrF, and BERTScore at first use in the Do section. Avoided unexplained references to "RoBERTa-
   large" and "transformer encoder" — retained them only in the Caveat where they are now
   explicitly contextualised.
6. **[BEGINNER FIX — Practice 9]** Explained probability-weighted scoring in plain terms (weighted
   average over confidence scores, not a raw integer). Added note that not all APIs expose output
   token probabilities. Simplified the Prometheus description from "13B fine-tuned" to "13-billion
   parameter model fine-tuned specifically for rubric scoring."
7. **[BEGINNER FIX — Practice 10]** Moved pass^k and pass@k definitions to the opening of the
   practice, before the notation is first used, with plain-English explanations.
8. **[BEGINNER FIX — Practice 1]** Added parenthetical definition of JSONL ("one JSON object per
   line") and "diffable" at first use.
9. **[BEGINNER FIX — Practice 11]** Added one-sentence plain-English definitions of MMLU, GSM8K,
   and HumanEval at first use.

**FLAG improvements (applied for clarity):**
10. **[FLAG — Practice 6]** Changed "annotation queue" to "a list of outputs waiting for a human to
    label" and "inter-annotator agreement" to "how consistently different reviewers give the same
    score" at first use.
11. **[FLAG — Practice 4]** Added note that `unittest.mock` and `pytest` are general-purpose Python
    testing tools, not AI-specific.
12. **[FLAG — Practices 7, 4]** Added brief parenthetical explanation of arXiv ("a free,
    open-access repository where researchers share papers") at first use.

**Structure changes (beginner re-leveling):**
13. Added "What is an AI agent?" introductory section.
14. Added "What does X mean?" context boxes before technical terms in each practice.
15. Added "What goes wrong without this:" to every practice (drawn from existing text in the
    technical entry — no new facts added).
16. Changed front matter `track` from `best-practices` to `beginner` and `audience` to
    `"people new to AI"`.
17. Numbered all practices for easier reference.
