---
title: "AI Agent Evaluation and Testing — Anthropic / Claude Best Practices (as of 18 Jul 2026)"
date: 2026-07-18
snapshot_date: 2026-07-18
topic: ai-agent-evaluation-anthropic
track: best-practices
audience: "technically comfortable readers"
description: "Source-verified best practices for evaluating AI agents built on Anthropic's Claude: Console Evaluation tool, Batches API, cross-family LLM-as-judge, adaptive thinking for evals, tool-use testing, multi-turn evaluation, and safety/refusal testing."
content_type: "Best Practice"
categories: ["Anthropic", "Claude", "AI Evaluation"]
tags: ["claude", "anthropic", "evaluation", "testing", "evals", "llm-as-judge", "batch-api", "extended-thinking", "tool-use", "safety", "multi-turn"]
last_refreshed: 2026-07-18
graded_by: "RingS panel (Skeptic/Beginner/Timekeeper) + sensei, 2026-07-18"
grading_result: "0 fabrications; 13 corrections applied; 0 issues filed"
---

<!-- This file lands at content/ai/best-practices/ai-agent-evaluation-anthropic/2026-07-18/index.md
     and is an IMMUTABLE dated snapshot. Once published it is never edited.
     Source tiers: independently-corroborated = 2+ DIFFERENT publishers;
     vendor-documented = official vendor docs only. -->

# AI Agent Evaluation and Testing — Anthropic / Claude-Specific (as of 18 Jul 2026)

> **Grading note.** A dated snapshot — accurate as of **18 Jul 2026**, frozen here and kept as
> a permanent archive entry. Research-drafted by a pupil, graded by the 3-lens panel + sensei.
> Corrections applied inline; unverifiable gaps marked ⚠ PENDING (#issue) — never guessed.

## How to read the labels
- ✅ **independently-corroborated** — 2+ independent publishers
- 📄 **vendor-documented** — official docs only (authoritative, single source)
- ⚠️ **WARNING** — a default that can cost money, break the machine, or remove a safety net
- 🕒 **verify live** — fast-moving (versions/prices/quotas); check the current value

---

## Practice: Use the Console Evaluation tool to test prompts before shipping

**Do:** Sign up for an Anthropic account at [console.anthropic.com](https://console.anthropic.com). In the Console, open any prompt in the Workbench — the interactive editor for building and testing prompts. Click the **Evaluate** tab. Create test cases manually, by importing a CSV, or by clicking "Generate Test Case" to let Claude auto-generate them. Run all cases at once, view outputs side-by-side, grade quality on a 5-point scale, and create new prompt versions that re-run the full suite.

**Why:** Without a systematic test harness you are guessing. The built-in tool lets you see in one screen how a prompt change affects ten or a hundred inputs at once, so you catch regressions before they reach users.

**Caveat / contested:**
- Your prompt must contain at least one `{{variable}}` placeholder (double-brace syntax) for the Evaluate tab to activate. Prompts with no variables cannot build a test set here.
- The Console's grading is human-applied (you click stars) — it does not run automated scoring. For large suites you will still need programmatic scoring.
- The built-in prompt generator is currently powered by Claude Sonnet 4.5. 🕒 verify live — may change with model releases.

**Sources:** [platform.claude.com/docs/en/docs/test-and-evaluate/eval-tool](https://platform.claude.com/docs/en/docs/test-and-evaluate/eval-tool) (Anthropic, 2026-07-18) · [sdtimes.com/ai/anthropic-adds-prompt-evaluation-feature-to-console](https://sdtimes.com/ai/anthropic-adds-prompt-evaluation-feature-to-console/) (SD Times, 2024-07-10, 2026-07-18) · [claude.com/blog/evaluate-prompts](https://claude.com/blog/evaluate-prompts) (Anthropic blog, 2026-07-18)
**Confidence:** ✅ independently-corroborated (Anthropic docs + independent tech news coverage)

---

## Practice: Use a different model family as judge when running LLM-as-judge evals

**Do:** When you use an LLM to score Claude's outputs (LLM-as-judge), choose a judge from a different model family — for example, GPT-5 or Gemini 2.5 Pro to evaluate Claude outputs, not Claude evaluating Claude. Note: using GPT-5 requires an OpenAI account and API key; using Gemini requires a Google AI Studio account — both are separate from your Anthropic account and billed separately. Anthropic's own evaluation guide says this is "generally best practice." For high-stakes decisions, run a three-judge ensemble across three families and aggregate by majority vote.

**Why:** Research shows LLM judges systematically rate outputs from their own model family 10–25% higher than equivalent outputs from another family — a "self-preference bias" documented in Zheng et al. 2024 (MT-Bench study, arXiv:2306.05685), where GPT-4 favored its own family's outputs ~10% and Claude-v1 ~25%. This bias operates at the embedding level and cannot be fixed just by asking the judge to "be objective." If you use Claude to judge Claude, your scores will look better than reality.

**Caveat / contested:**
- The three-judge ensemble reduces bias by ~30–40% (Label Your Data, 2026) but costs 3–5× more per eval run. Reserve it for launch-gate decisions.
- Anthropic's own code examples in their evaluation docs sometimes show `claude-opus-4-8` evaluating `claude-opus-4-8` (same model). Their text warns against this; treat example code as illustrative, not a recommendation.
- Bias direction can shift across model generations. Always validate your chosen judge on a labeled sample from your own data before relying on it at scale.
- ⚠️ **WARNING:** Ignoring self-preference bias is one of the most common reasons eval scores fail to predict real-world quality. Do not skip cross-family validation.

**Sources:** [platform.claude.com/docs/en/docs/test-and-evaluate/develop-tests](https://platform.claude.com/docs/en/docs/test-and-evaluate/develop-tests) (Anthropic, 2026-07-18) · [arxiv.org/abs/2306.05685](https://arxiv.org/abs/2306.05685) — Zheng et al. 2024, MT-Bench (primary source for 10–25% figure, 2026-07-18) · [futureagi.com/blog/llm-as-a-judge](https://futureagi.com/blog/llm-as-a-judge/) (Future AGI, vendor, 2026-07-18) · [labelyourdata.com/articles/llm-as-a-judge](https://labelyourdata.com/articles/llm-as-a-judge) (Label Your Data, 2026-07-18)
**Confidence:** ✅ independently-corroborated (Anthropic docs + academic paper + independent publisher; three Future AGI posts consolidated to one vendor citation)

---

## Practice: Use the Message Batches API for large eval runs to cut costs by 50%

**Do:** Submit your eval test cases to the [Message Batches API](https://platform.claude.com/docs/en/build-with-claude/batch-processing) instead of the synchronous Messages API. Pack up to **100,000 requests** (or 256 MB) into one batch call; results come back within 1 hour in most cases, hard timeout 24 hours. All active Claude models are supported. In Python: `client.messages.batches.create(requests=[...])`.

⚠️ **WARNING (cost — read before submitting):** Before submitting a batch, estimate the total cost: `requests × average_tokens × price_per_token ÷ 2`. Example: 10,000 requests × 2,000 tokens × (Sonnet 5 introductory input price $0.002/1k) ÷ 2 = roughly **$20**. At standard prices this is still $30. Always know your number before you submit. Set a Workspace spend limit at [console.anthropic.com](https://console.anthropic.com) before running large batches — batches can overshoot the limit slightly because requests are processed concurrently. Beginners: start with a 10-request test batch to validate your code before scaling.

**Why:** Running 1,000 eval cases synchronously costs the same per-token rate and blocks your code while waiting. The Batches API charges exactly 50% of standard token prices and runs everything asynchronously, so you can run 10,000-case eval suites overnight at half the cost.

**Caveat / contested:**
- Results are available for **29 days** after creation, then deleted. Download and store them before the window closes.
- **Unsupported inside batch requests** (attempting these returns a validation error): `stream: true`, Threads (`store` / `previous_thread_event_id`), Fast mode, `max_tokens: 0`, `cache_hint`/`context_hint` routing hints, and `research_preview_2026_02`. 🕒 Check [platform.claude.com/docs/en/build-with-claude/batch-processing](https://platform.claude.com/docs/en/build-with-claude/batch-processing) for the current full list.
- Prompt caching and batch discounts stack: a cached system prompt in a batch can see up to 95% off standard prices. 🕒 Verify current pricing before budgeting — prices change with model releases.
- Rate limits still apply to the number of pending batch requests.

🕒 **Sonnet 5 pricing note:** Claude Sonnet 5 is on introductory pricing ($2/$10 per MTok input/output) through **August 31, 2026**. After that date prices revert to $3/$15 per MTok. If your batch eval budget spans September 2026, account for the ~50% price increase on Sonnet 5.

**Sources:** [platform.claude.com/docs/en/build-with-claude/batch-processing](https://platform.claude.com/docs/en/build-with-claude/batch-processing) (Anthropic, 2026-07-18) · [claude.com/blog/message-batches-api](https://claude.com/blog/message-batches-api) (Anthropic blog, 2026-07-18) · [codewords.ai/blog/anthropic-batch-api](https://www.codewords.ai/blog/anthropic-batch-api) (CodeWords, 2026-07-18)
**Confidence:** 📄 vendor-documented (Anthropic docs are the authoritative source; codewords.ai is a vendor platform, not an independent publisher — label downgraded from draft)

---

## Practice: Pin prompts as versioned templates in the Console for reproducible eval reruns

**Do:** In the Anthropic Console, write prompts using `{{variable}}` placeholders for any dynamic content. Save named versions each time you make a meaningful change. The Console tracks prompt templates separately from variable values, letting you re-run the same eval suite against a new prompt version and compare outputs side-by-side on the same test cases.

**Why:** If you change your prompt and do not track versions, you cannot tell whether a score change came from the prompt change or from something else. Treating prompts like code commits — save a version, run the suite, compare — gives you a paper trail.

**Caveat / contested:**
- The Console's versioning is lightweight — it is not Git. It does not show diffs between versions. For team workflows, many teams export prompt text to Git and use the Console only for running evals.
- The prompt improver tool creates longer, more chain-of-thought-heavy prompts. These are more thorough but slower. Do not apply the improver on latency-sensitive or cost-sensitive paths without re-benchmarking.
- Keep your golden test-case CSVs in source control — the Console prompt library is not a substitute.

**Sources:** [platform.claude.com/docs/en/docs/build-with-claude/prompt-engineering/prompt-generator](https://platform.claude.com/docs/en/docs/build-with-claude/prompt-engineering/prompt-generator) (Anthropic, 2026-07-18) · [platform.claude.com/docs/en/docs/test-and-evaluate/eval-tool](https://platform.claude.com/docs/en/docs/test-and-evaluate/eval-tool) (Anthropic, 2026-07-18) · [sdtimes.com/ai/anthropic-adds-prompt-evaluation-feature-to-console](https://sdtimes.com/ai/anthropic-adds-prompt-evaluation-feature-to-console/) (SD Times, 2026-07-18)
**Confidence:** ✅ independently-corroborated (Anthropic docs + independent tech news)

---

## Practice: Use adaptive thinking (effort parameter) for hard eval tasks; use low effort for cheap screening

**Do:** On Claude Opus 4.8, Fable 5, Sonnet 5, and predecessors back to Opus 4.6, set `output_config={"effort": "max"}` for your hardest eval tasks — complex multi-step reasoning, graduate-level science questions, agentic planning — so the model spends maximum tokens thinking before answering. Use `effort: "low"` or `effort: "medium"` for simple classification or screening tasks where full reasoning is unnecessary. The five levels are: `low`, `medium`, `high` (default), `xhigh`, `max`.

```python
import anthropic
client = anthropic.Anthropic()
response = client.messages.create(
    model="claude-opus-4-8",
    max_tokens=16000,
    output_config={"effort": "max"},
    messages=[{"role": "user", "content": "Your hard eval task here"}]
)
```

⚠️ **WARNING (cost):** Thinking tokens at `max` effort on a frontier model can cost **10× or more** compared to a `low`-effort or non-thinking call on the same model. A single eval case at max effort on Opus 4.8 may cost as much as dozens of standard calls. Test on 5 cases and check your billing dashboard before scaling to hundreds.

**Why:** Harder tasks produce better answers when the model spends more time reasoning. But spending maximum compute on every eval case is expensive and slow. Tiering effort to task difficulty cuts cost while preserving quality where it matters.

**Caveat / contested:**
- `budget_tokens` (older API) is deprecated on Opus 4.6, Sonnet 4.6 and later models. Use the `effort` parameter instead.
- On **Claude Haiku 4.5** (only), the `effort` parameter is not supported; use `thinking: {type: "enabled", budget_tokens: N}` for that model. Opus 4.5 does support the `effort` parameter (Timekeeper correction: the draft incorrectly excluded Opus 4.5).
- `effort` is a behavioral signal, not a hard token cap. At low effort, Claude may still think on genuinely difficult problems, and actual token spend can vary.
- 🕒 Check [platform.claude.com/docs/en/build-with-claude/effort](https://platform.claude.com/docs/en/build-with-claude/effort) for the current supported model list — verify live.

**Sources:** [platform.claude.com/docs/en/build-with-claude/effort](https://platform.claude.com/docs/en/build-with-claude/effort) (Anthropic, 2026-07-18) · [platform.claude.com/docs/en/build-with-claude/extended-thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking) (Anthropic, 2026-07-18)
**Confidence:** 📄 vendor-documented (Anthropic official docs; no independent publisher covered the specifics of the effort parameter in sufficient depth)

---

## Practice: Match model capability to eval task difficulty to control cost

**Do:** Do not run every eval case through your most capable (and most expensive) model. For bulk screening or simple classification cases, use Claude Haiku 4.5 (`claude-haiku-4-5`). For moderate-complexity reasoning, use Claude Sonnet 5 (`claude-sonnet-5`). Reserve Claude Opus 4.8 (`claude-opus-4-8`) or Claude Fable 5 (`claude-fable-5`) for the hardest cases — graduate-level science, long-horizon agentic tasks, complex code generation.

As of 2026-07-18: Haiku 4.5 costs $1/MTok input (MTok = one million tokens; a typical paragraph is ~100–150 tokens) versus $10/MTok for Fable 5 — a 10× difference. Running 10,000 screening cases through Haiku instead of Fable 5 saves $90 per million input tokens. Use your expensive model only where the extra quality shows up in your eval scores.

🕒 **verify live:** Claude Sonnet 5 is on introductory pricing ($2/$10 per MTok) through August 31, 2026 — reverts to $3/$15 after that. Always verify current pricing at [platform.claude.com/docs/en/about-claude/pricing](https://platform.claude.com/docs/en/about-claude/pricing) before budgeting. Prices change with model releases.

**Why:** Using the right model tier for each task type is the single highest-leverage cost lever for large eval suites. "Harder tasks benefit from more capable models" is a general rule — always measure on a random sample first.

**Caveat / contested:**
- For your specific task, always measure: run a random sample through both tiers and compare eval scores before committing. The quality difference may be negligible for your use case.
- Haiku 4.5 has a 200k token context window vs 1M for Opus 4.8. Long-context eval cases (multi-document, long chat histories) require a larger context model.

**Sources:** [platform.claude.com/docs/en/about-claude/models/overview](https://platform.claude.com/docs/en/about-claude/models/overview) (Anthropic, 2026-07-18) · [platform.claude.com/docs/en/about-claude/pricing](https://platform.claude.com/docs/en/about-claude/pricing) (Anthropic, 2026-07-18)
**Confidence:** 📄 vendor-documented (pricing and model specs from Anthropic only)

---

## Practice: Treat Anthropic's published benchmark scores as signals, not guarantees

**Do:** When reading Anthropic's system cards and Transparency Hub, look at the evaluation **methodology** — what benchmark, what settings, what models were tested against — not just the headline number. Cross-reference scores on multiple benchmarks because no single number captures full capability. Build your own held-out test set for your specific use case. Benchmarks referenced in Anthropic system cards:
- **ARC-AGI** — abstract reasoning tasks; 94.00% (ARC-AGI-1) / 69.17% (ARC-AGI-2) were published for Claude Opus 4.6 using 120k thinking tokens at High effort. Newer models (Opus 4.8, Fable 5) have been released with new system cards — 🕒 check [anthropic.com/transparency](https://www.anthropic.com/transparency) for current figures.
- **SWE-bench Verified** — real-world software engineering pull requests from GitHub; measures how often the model correctly fixes a bug.
- **GPQA Diamond** — graduate-level science questions in biology, chemistry, and physics; used to test expert-level reasoning.
- **MMLU** — 57 academic subjects from STEM to law; now saturated above 90% for frontier models and no longer discriminates between top systems.

**Why:** Benchmarks like MMLU are saturated above 90% for frontier models, so they no longer distinguish between the top systems. SWE-bench scores over 49% on isolated code problems may not reflect performance on your actual codebase. A headline benchmark number is one signal, not a buying decision.

**Caveat / contested:**
- Data contamination is a real risk: if benchmark questions appear in training data, scores can be inflated. Anthropic acknowledges this in system cards but cannot fully audit for it.
- Anthropic's own evals use test-time compute (adaptive thinking at high or max effort) for their reported scores. A developer running the same model at `low` effort will see lower scores. Check which effort/thinking settings were used before comparing.

**Sources:** [anthropic.com/transparency](https://www.anthropic.com/transparency) (Anthropic, 2026-07-18) · [stackviv.ai/blog/ai-model-benchmarks-mmlu-humaneval](https://stackviv.ai/blog/ai-model-benchmarks-mmlu-humaneval) (StackViv, 2026-07-18)
**Confidence:** ✅ independently-corroborated (Anthropic system cards + independent benchmark-interpretation article)

---

## Practice: Evaluate tool use by testing tool selection, argument correctness, and schema compliance

**Do:** When testing Claude's function-calling (tool use), run eval cases across three dimensions: (1) **tool selection** — does Claude call the right tool given the request? (2) **argument correctness** — are the extracted arguments semantically correct (e.g., the right units, date format, numeric type), not just syntactically valid JSON? (3) **schema compliance** — does the returned JSON match the defined `input_schema`? Compare actual vs. expected `tool_use` blocks in API responses. Use Anthropic's Claude Cookbook [tool evaluation example](https://platform.claude.com/cookbook/tool-evaluation-tool-evaluation) as a starting framework.

**Why:** Claude's function-calling outputs are structured JSON objects. Unlike free text, these go directly into your application code. A wrong argument (`^` instead of `**` for exponentiation) or a missing required field can silently break downstream systems. Structured eval catches this before it reaches production.

**Caveat / contested:**
- Anthropic's Cookbook example evaluates accuracy as exact-match against expected responses. For many real-world cases, functional equivalence is a better target than exact string match.
- Anthropic's internal data showed accuracy improving from 72% to 90% **on complex parameter handling** when `input_examples` were added to tool definitions (Anthropic Engineering blog, 2026-07-18). Include examples in your tool schema before blaming the model for low scores. Note: this figure is from an Anthropic engineering blog post with no published dataset or methodology — treat as directional, not a reproducible benchmark.
- ⚠️ **WARNING:** Extended thinking with tool use has specific constraints: only `tool_choice: "auto"` or `"none"` is supported; you cannot force specific tools. In multi-turn tool-use evaluations, you must preserve the thinking blocks from prior turns in the message history, or the API will error.
- Tool-use evals can be batched through the Message Batches API (tool use is explicitly listed as batchable).

**Sources:** [platform.claude.com/cookbook/tool-evaluation-tool-evaluation](https://platform.claude.com/cookbook/tool-evaluation-tool-evaluation) (Anthropic, 2026-07-18) · [platform.claude.com/docs/en/build-with-claude/extended-thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking) (Anthropic, 2026-07-18) · [www.anthropic.com/engineering/advanced-tool-use](https://www.anthropic.com/engineering/advanced-tool-use) (Anthropic Engineering, 2026-07-18)
**Confidence:** 📄 vendor-documented (all sources are Anthropic)

---

## Practice: Evaluate multi-turn conversations per-turn, not just on final output

**Do:** For agents that maintain state across turns (customer service, tutors, long-form assistants), evaluate each turn independently as well as the final answer. Check: does the model recall facts stated earlier? Does it contradict itself? Does it stay on the user's goal across topic shifts? Use a per-turn rubric (1–5 scale per turn), then aggregate. For state-dependent evals, extract memory or context blocks directly, not just the assistant's text, to confirm the information was actually stored.

**Why:** A model can give a correct final answer while having contradicted itself three turns earlier. Single-output scoring misses degradation patterns that users experience in real conversations. Checking each turn catches context drift early.

**Caveat / contested:**
- Multi-turn evals are harder to automate because they require simulating a realistic user who adapts to prior turns. Naive fixed-script users miss model failures that only appear when the user responds to model output.
- For long conversations, Claude's context compaction (automatic summarization that activates near the context limit — when the conversation history grows too large to fit in memory) may alter what the model "recalls" from earlier. Test around the compaction boundary if your app uses long sessions.
- Anthropic's safety team uses multi-turn evals internally but the methodology is not publicly documented in detail.

**Sources:** [docs.letta.com/guides/evals/advanced/multi-turn-conversations](https://docs.letta.com/guides/evals/advanced/multi-turn-conversations/) (Letta, 2026-07-18) · [platform.claude.com/docs/en/docs/test-and-evaluate/develop-tests](https://platform.claude.com/docs/en/docs/test-and-evaluate/develop-tests) (Anthropic, 2026-07-18) · [getmaxim.ai/articles/how-to-ensure-consistency-in-multi-turn-ai-conversations](https://www.getmaxim.ai/articles/how-to-ensure-consistency-in-multi-turn-ai-conversations) (Maxim, 2026-07-18)
**Confidence:** ✅ independently-corroborated (Letta docs + Anthropic docs + Maxim article)

---

## Practice: Evaluate both over-refusal and under-refusal; vendor safety testing does not cover your deployment

**Do:** Build two separate safety eval suites: (1) **under-refusal** — prompts that should be refused (harmful, policy-violating); (2) **over-refusal** (false positives) — prompts that look superficially risky but are legitimate (e.g., "how does a lock-picking mechanism work?" from a security researcher). Target a calibration where the refusal rate tracks actual risk, not surface keywords. Run multi-turn escalation sequences — not just single harmful prompts — because Claude's safety training found gradual multi-turn escalation ("Crescendo jailbreaking") more effective at bypassing safety than single-turn attacks.

**Why:** A model that refuses too many benign requests is nearly as harmful to your product as one that fails to refuse harmful ones. High over-refusal frustrates users and causes abandonment. Anthropic's own system cards track over-refusal rates alongside harm rates — you should too.

**Caveat / contested:**
- ⚠️ **WARNING:** Anthropic's safety evaluations are conducted on their infrastructure with their safety guardrails enabled. If you fine-tune, use prompt injection paths, or disable default safety system prompts, you are outside the scope of published safety results and must re-evaluate.
- The joint OpenAI-Anthropic safety evaluation (August 2025) found both companies' models showed "concerning forms of sycophancy" under certain multi-turn scenarios, despite strong single-turn refusals. Your safety evals must include multi-turn social engineering scenarios.
- Constitutional AI (Anthropic's training technique that teaches Claude to reason from a set of ethical principles) makes Claude more consistent on ambiguous inputs than keyword-filter approaches but does not eliminate failures, especially under adversarial multi-turn pressure.

**Sources:** [trydeepteam.com/guides/guide-red-teaming-anthropic](https://www.trydeepteam.com/guides/guide-red-teaming-anthropic) (DeepTeam, 2026-07-18) · [frugaltesting.com/blog/how-claude-is-trained-and-tested-for-safety-at-anthropic](https://www.frugaltesting.com/blog/how-claude-is-trained-and-tested-for-safety-at-anthropic) (Frugal Testing, 2026-07-18) · [edtechinnovationhub.com — openai-and-anthropic-cross-test-ai-models](https://www.edtechinnovationhub.com/news/openai-and-anthropic-cross-test-ai-models-in-rare-joint-safety-evaluation) (EdTech Innovation Hub, 2026-07-18) · [anthropic.com/transparency](https://www.anthropic.com/transparency) (Anthropic, 2026-07-18)
**Confidence:** ✅ independently-corroborated (multiple independent publishers + Anthropic docs)

---

## Held pending fixes

- Claude Opus 4.6 system card PDF (ARC-AGI benchmark figures): PDF exceeds fetch tool size limit. Figures (94.00% ARC-AGI-1, 69.17% ARC-AGI-2 at 120k tokens / High effort) corroborated via system-card search index and ARC Prize Foundation reporting. Recommend a human open the PDF at [anthropic.com/transparency](https://www.anthropic.com/transparency) to fully close the loop. ⚠ PENDING

## CHANGELOG (grading → this entry)
1. **[SKEPTIC FIX]** LLM-as-judge (Practice 2): Replaced three Future AGI posts as the sole source for 10–25% self-preference bias figure. Now cites Zheng et al. 2024 (MT-Bench, arXiv:2306.05685) as the academic primary source; Future AGI consolidated to a single vendor citation. Confidence label updated to reflect this change.
2. **[SKEPTIC FIX]** Tool-use accuracy (Practice 8): Added "on complex parameter handling" scope qualifier to the 72%→90% accuracy improvement figure, matching the Anthropic Engineering blog's exact wording. Added explicit note that this is not a reproducible benchmark.
3. **[BEGINNER KILL]** Batch API (Practice 3): Added prominent worked cost example BEFORE the code block, instructing readers to estimate total cost and set a Workspace spend limit before submitting. Added "start with 10-request test batch" recommendation.
4. **[BEGINNER KILL]** Adaptive thinking (Practice 5): Replaced "substantially more" with a concrete multiplier ("10× or more") and explicit instruction to test on 5 cases and check billing before scaling.
5. **[BEGINNER FIX]** Console Evaluation tool (Practice 1): Added prerequisite: sign up for an Anthropic account at console.anthropic.com; defined what the Workbench is.
6. **[BEGINNER FIX]** LLM-as-judge (Practice 2): Added explicit note that GPT-5/Gemini require separate vendor accounts and billing.
7. **[BEGINNER FIX]** Adaptive thinking (Practice 5): Added full `messages.create()` call context showing the effort parameter in a runnable code snippet.
8. **[BEGINNER FIX]** Model capability tiering (Practice 6): Defined "MTok" with plain-language explanation (1 million tokens; ~100–150 tokens per paragraph).
9. **[BEGINNER FIX]** Benchmark scores (Practice 7): Added one-line definitions for ARC-AGI, SWE-bench Verified, GPQA Diamond, and MMLU.
10. **[TIMEKEEPER KILL]** Adaptive thinking (Practice 5): Fixed caveat — Opus 4.5 incorrectly listed as not supporting the `effort` parameter. Current Anthropic docs explicitly include Opus 4.5. Caveat corrected to apply only to Haiku 4.5.
11. **[TIMEKEEPER FIX]** Adaptive thinking (Practice 5): Updated primary model reference from "Opus 4.6 and later" to "Opus 4.8, Fable 5, Sonnet 5, and predecessors back to Opus 4.6" since Opus 4.6 is now a legacy model.
12. **[TIMEKEEPER FIX]** Batch API (Practice 3): Added two missing unsupported parameters: `cache_hint`/`context_hint` and `research_preview_2026_02`.
13. **[TIMEKEEPER FLAG]** Batch API + Model tiering (Practices 3 and 6): Added explicit Sonnet 5 introductory pricing expiry date (August 31, 2026) with note about $3/$15 post-expiry pricing.
14. **[AUDIENCE FIX]** Front matter: corrected `audience` from "people new to AI" to "technically comfortable readers".
