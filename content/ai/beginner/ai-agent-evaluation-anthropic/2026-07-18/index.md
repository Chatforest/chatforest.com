---
title: "AI Agent Evaluation and Testing — Anthropic / Claude Best Practices (as of 18 Jul 2026)"
date: 2026-07-18
snapshot_date: 2026-07-18
topic: ai-agent-evaluation-anthropic
track: beginner
audience: "people new to AI"
description: "Plain-language guide to evaluating AI agents built on Anthropic's Claude: Console Evaluation tool, Batches API, LLM-as-judge, adaptive thinking for evals, tool-use testing, and safety testing."
content_type: "Best Practice"
categories: ["Anthropic", "Claude", "AI Evaluation"]
tags: ["claude", "anthropic", "evaluation", "testing", "evals", "llm-as-judge", "batch-api", "extended-thinking", "tool-use", "safety"]
last_refreshed: 2026-07-18
graded_by: "RingS panel (Skeptic/Beginner/Timekeeper) + sensei, 2026-07-18"
grading_result: "0 fabrications; beginner re-level by rings-beginner-author, 2026-07-18"
---

<!-- This file lands at content/ai/beginner/ai-agent-evaluation-anthropic/2026-07-18/index.md
     and is an IMMUTABLE dated snapshot. Once published it is never edited.
     Source tiers: independently-corroborated = 2+ DIFFERENT publishers;
     vendor-documented = official vendor docs only. -->

# AI Agent Evaluation and Testing — Anthropic / Claude (as of 18 Jul 2026)

> **Grading note.** A dated snapshot — accurate as of **18 Jul 2026**, frozen here and kept as
> a permanent archive entry. Research-drafted by a pupil, graded by the 3-lens panel + sensei.
> Corrections applied inline; unverifiable gaps marked ⚠ PENDING (#issue) — never guessed.

## What this guide is about

When you build an AI application using Claude, you need a way to check whether it is working correctly — not just once, but repeatedly, as you change your prompts or upgrade models. That process is called **evaluation** (or "evals" for short). Think of it as automated testing for AI outputs.

This guide covers ten practices Anthropic recommends for evaluating Claude-based applications. They go roughly from "easiest to start with" to "more involved." You do not need to do all ten at once — pick the ones that match where you are right now.

## How to read the labels

- ✅ **independently-corroborated** — 2+ independent publishers confirmed this
- 📄 **vendor-documented** — official Anthropic docs only (authoritative, single source)
- ⚠️ **WARNING** — a default that can cost money, break the machine, or remove a safety net
- 🕒 **verify live** — fast-moving detail (versions, prices, quotas); check the current value before acting

---

## Practice 1: Use the Console Evaluation tool to test prompts before shipping

**Prerequisite:** You need an Anthropic account. Sign up at [console.anthropic.com](https://console.anthropic.com). Note that API access (needed for building applications) may require a paid plan — check Anthropic's current account tiers when you sign up.

**Do:** Once logged in, open the **Workbench** — Anthropic's interactive, browser-based editor where you write and test prompts. Inside the Workbench, click the **Evaluate** tab. From there you can create test cases manually, import a list of test cases from a CSV file, or click "Generate Test Case" to let Claude suggest test cases for you. Run all your test cases at once, see the outputs side by side, and rate quality on a 1–5 scale. When you change your prompt, re-run the same test cases so you can spot regressions (cases that used to work but now fail).

**Why (beginner):** Without a test harness, you are guessing. You change one word in your prompt and hope nothing breaks. The Console Evaluation tool shows you — on one screen — how a prompt change affects ten or a hundred different inputs at once. You catch problems before your users do.

**Caveat / contested:**
- Your prompt must contain at least one `{{variable}}` placeholder (double curly braces around a word, like `{{customer_question}}`) for the Evaluate tab to turn on. A prompt with no variables cannot build a test set here.
- The Console's grading is human-applied — you click the star rating. There is no automatic scoring. For large test suites (hundreds of cases) you will eventually need programmatic scoring (see the Batches API practice below).
- The built-in prompt generator is currently powered by Claude Sonnet 4.5. 🕒 verify live — this may change with future model releases.

**Sources:** [platform.claude.com/docs/en/docs/test-and-evaluate/eval-tool](https://platform.claude.com/docs/en/docs/test-and-evaluate/eval-tool) (Anthropic, 2026-07-18) · [sdtimes.com/ai/anthropic-adds-prompt-evaluation-feature-to-console](https://sdtimes.com/ai/anthropic-adds-prompt-evaluation-feature-to-console/) (SD Times, 2024-07-10, 2026-07-18) · [claude.com/blog/evaluate-prompts](https://claude.com/blog/evaluate-prompts) (Anthropic blog, 2026-07-18)
**Confidence:** ✅ independently-corroborated (Anthropic docs + independent tech news coverage)

---

## Practice 2: Use a different AI company's model as your judge when scoring Claude's outputs

**What is LLM-as-judge?** Instead of having a human read every output and decide if it is good, you send Claude's answer to a second AI model and ask that model to rate it. This second model is called the "judge."

**Do:** Choose a judge from a *different* model family — for example, use GPT-5 (from OpenAI) or Gemini 2.5 Pro (from Google) to grade Claude's outputs, rather than using Claude to grade Claude. Anthropic's own evaluation guide calls this "generally best practice."

Important practicalities:
- Using **GPT-5** as your judge requires an **OpenAI account**, a separate OpenAI API key, and the OpenAI Python SDK. This is a completely separate sign-up and billing relationship from your Anthropic account.
- Using **Gemini 2.5 Pro** requires a **Google AI Studio account** and a Google API key — again, separate from both Anthropic and OpenAI.

For the highest-stakes decisions (e.g., before launching a product), run a three-judge ensemble: have one judge from each of three different AI families each score the output, then take the majority vote.

Note: Anthropic's own code examples in their evaluation docs sometimes show `claude-opus-4-8` evaluating `claude-opus-4-8` (the same model). Their written guidance warns against this. Treat that example code as illustrative, not as a recommendation.

**Why (beginner):** Research shows that AI models give higher scores to outputs from their own "family" — anywhere from 10% to 25% higher, even when the outputs are equally good. This is called "self-preference bias." If you use Claude to judge Claude, your eval scores will look better than reality, and you will not know your application is failing until users tell you.

⚠️ **WARNING:** Ignoring self-preference bias is one of the most common reasons that good eval scores fail to predict real-world quality. Do not skip cross-family validation.

**Caveat / contested:**
- The three-judge ensemble reduces bias by roughly 30–40% but costs 3–5 times more per eval run. Reserve it for final go/no-go decisions, not routine testing.
- Bias direction can shift across model generations. Always validate your chosen judge model against a set of human-labeled examples from your own data before relying on it at scale.

**Sources:** [platform.claude.com/docs/en/docs/test-and-evaluate/develop-tests](https://platform.claude.com/docs/en/docs/test-and-evaluate/develop-tests) (Anthropic, 2026-07-18) · [arxiv.org/abs/2306.05685](https://arxiv.org/abs/2306.05685) — Zheng et al. 2024, MT-Bench (primary source for 10–25% figure, 2026-07-18) · [futureagi.com/blog/llm-as-a-judge](https://futureagi.com/blog/llm-as-a-judge/) (Future AGI, vendor, 2026-07-18) · [labelyourdata.com/articles/llm-as-a-judge](https://labelyourdata.com/articles/llm-as-a-judge) (Label Your Data, 2026-07-18)
**Confidence:** ✅ independently-corroborated (Anthropic docs + academic paper + independent publisher)

---

## Practice 3: Use the Message Batches API for large eval runs to cut costs by 50%

**What is the Message Batches API?** Normally when you call Claude's API, you send one request and wait for one response before sending the next. The **Message Batches API** lets you package thousands of requests into a single call, submit them all at once, and pick up the results when they are ready — like dropping off a stack of letters instead of waiting at the post office counter for each one.

⚠️ **WARNING (cost — read this before submitting your first batch):**

A batch can get expensive fast. Before you submit, estimate your total cost using this formula:

> **number of requests × average tokens per request × price per token ÷ 2**

Tokens are the units Claude charges for. One token is roughly three-quarters of a word; a typical short paragraph is about 100–150 tokens.

Example: 10,000 requests × 2,000 tokens × (Sonnet 5 introductory input price of $0.002 per 1,000 tokens) ÷ 2 = roughly **$20** at the discounted batch rate. At standard (non-introductory) prices the same batch would cost roughly $30. Always know your number before you submit.

**Before submitting any batch:**
1. Set a Workspace spend limit at [console.anthropic.com](https://console.anthropic.com). Be aware that batches can overshoot the limit slightly because requests are processed at the same time.
2. Start with a **10-request test batch** to confirm your code works before scaling to thousands.

**Do:** Submit your eval test cases to the [Message Batches API](https://platform.claude.com/docs/en/build-with-claude/batch-processing) instead of the standard Messages API. You can pack up to 100,000 requests (or 256 MB, whichever comes first) into one batch call. Results come back within 1 hour in most cases, with a hard timeout of 24 hours. All active Claude models are supported. In Python:

```python
client.messages.batches.create(requests=[...])
```

**Why (beginner):** Running 1,000 eval cases one by one costs the full per-token rate and ties up your code while it waits. The Batches API charges exactly 50% of standard token prices and runs everything in the background. You can kick off a 10,000-case eval run before you go to sleep and have the results in the morning at half the cost.

**Caveat / contested:**
- Results are available for **29 days** after creation, then permanently deleted. Download and save them before the window closes.
- The following features are **not supported inside batch requests** (using them returns a validation error): `stream: true`, Threads (`store` / `previous_thread_event_id`), Fast mode, `max_tokens: 0`, `cache_hint`/`context_hint` routing hints, and `research_preview_2026_02`. 🕒 Check [platform.claude.com/docs/en/build-with-claude/batch-processing](https://platform.claude.com/docs/en/build-with-claude/batch-processing) for the current full list.
- Prompt caching and batch discounts stack: a cached system prompt in a batch can mean up to 95% off standard prices. 🕒 Verify current pricing before budgeting — prices change with model releases.
- Rate limits still apply to the number of pending batch requests.

🕒 **Sonnet 5 pricing note:** Claude Sonnet 5 is on introductory pricing ($2/$10 per MTok input/output — MTok means one million tokens) through **August 31, 2026**. After that date, prices revert to $3/$15 per MTok. If your eval budget spans September 2026, account for the roughly 50% price increase on Sonnet 5.

**Sources:** [platform.claude.com/docs/en/build-with-claude/batch-processing](https://platform.claude.com/docs/en/build-with-claude/batch-processing) (Anthropic, 2026-07-18) · [claude.com/blog/message-batches-api](https://claude.com/blog/message-batches-api) (Anthropic blog, 2026-07-18) · [codewords.ai/blog/anthropic-batch-api](https://www.codewords.ai/blog/anthropic-batch-api) (CodeWords, 2026-07-18)
**Confidence:** 📄 vendor-documented (Anthropic docs are the authoritative source; codewords.ai is a vendor platform, not an independent publisher)

---

## Practice 4: Save versioned prompt templates so you can re-run the same eval suite after changes

**Do:** In the Anthropic Console, write your prompts using `{{variable}}` placeholders for any content that changes between test cases (for example, `{{user_question}}`). Save a named version each time you make a meaningful change to the prompt. The Console tracks these versions separately, letting you re-run the exact same test cases against a new prompt version and compare outputs side by side.

**Why (beginner):** If you tweak your prompt but do not save a version, you cannot tell whether a change in your scores came from the prompt change or from something else. Treating prompts like code — save a version, run the suite, compare — gives you a clear record of what changed when.

**Caveat / contested:**
- The Console's versioning is lightweight and does not show a diff (line-by-line comparison) between versions. For team projects, many teams copy the prompt text into Git and use the Console only for running evals.
- The Console includes a "prompt improver" tool that rewrites your prompt to be more detailed and chain-of-thought-heavy (it instructs Claude to think step by step). These improved prompts are more thorough but slower and cost more tokens. Do not apply the improver on latency-sensitive or budget-sensitive paths without re-measuring.
- Keep your test-case CSV files in source control (Git or similar) — the Console prompt library is not a backup system.

**Sources:** [platform.claude.com/docs/en/docs/build-with-claude/prompt-engineering/prompt-generator](https://platform.claude.com/docs/en/docs/build-with-claude/prompt-engineering/prompt-generator) (Anthropic, 2026-07-18) · [platform.claude.com/docs/en/docs/test-and-evaluate/eval-tool](https://platform.claude.com/docs/en/docs/test-and-evaluate/eval-tool) (Anthropic, 2026-07-18) · [sdtimes.com/ai/anthropic-adds-prompt-evaluation-feature-to-console](https://sdtimes.com/ai/anthropic-adds-prompt-evaluation-feature-to-console/) (SD Times, 2026-07-18)
**Confidence:** ✅ independently-corroborated (Anthropic docs + independent tech news)

---

## Practice 5: Use the "effort" setting to match reasoning depth to task difficulty

**What is adaptive thinking?** Some Claude models can "think out loud" before answering — working through a problem step by step before producing a response. The amount of thinking is controlled by an `effort` parameter. More effort means more thinking, better answers on hard problems, and higher cost.

**Do:** On Claude Opus 4.8, Fable 5, Sonnet 5, and older models back to Opus 4.6, set `output_config={"effort": "max"}` for your hardest eval tasks — complex multi-step reasoning, graduate-level science questions, planning tasks with many steps. Use `effort: "low"` or `effort: "medium"` for simple sorting, classification, or screening tasks where deep reasoning is unnecessary. The five levels are: `low`, `medium`, `high` (the default if you do not specify), `xhigh`, and `max`.

Here is the complete Python code to make a call with max effort:

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

The `import anthropic` line loads the official Anthropic Python SDK. `client.messages.create(...)` is the method that sends your request to the API.

⚠️ **WARNING (cost):** At `max` effort, thinking tokens alone can cost **10 times or more** compared to a `low`-effort call on the same model. A single eval case at max effort on Opus 4.8 may cost as much as dozens of standard calls. Test on **5 cases** and check your billing dashboard before scaling to hundreds.

**Why (beginner):** Harder tasks get better answers when Claude spends more time reasoning. But paying for maximum reasoning on every eval case — including simple ones — wastes money and slows things down. Matching effort to difficulty keeps your costs reasonable while preserving quality where it actually matters.

**Caveat / contested:**
- `budget_tokens` (an older API parameter) is deprecated on Opus 4.6, Sonnet 4.6, and later models. Use the `effort` parameter instead.
- On **Claude Haiku 4.5 only**, the `effort` parameter is not supported. For Haiku 4.5, use `thinking: {type: "enabled", budget_tokens: N}` instead. All other models listed above (including Opus 4.5) do support `effort`.
- `effort` is a behavioral signal, not a hard token cap. Even at `low` effort, Claude may still reason on a genuinely difficult problem. Actual token usage can vary.
- 🕒 Check [platform.claude.com/docs/en/build-with-claude/effort](https://platform.claude.com/docs/en/build-with-claude/effort) for the current supported model list — verify live.

**Sources:** [platform.claude.com/docs/en/build-with-claude/effort](https://platform.claude.com/docs/en/build-with-claude/effort) (Anthropic, 2026-07-18) · [platform.claude.com/docs/en/build-with-claude/extended-thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking) (Anthropic, 2026-07-18)
**Confidence:** 📄 vendor-documented (Anthropic official docs)

---

## Practice 6: Match the model to the difficulty of the eval task to control cost

**Do:** Do not run every eval case through your most powerful (and most expensive) model. Choose the model that is just capable enough for each type of task:

- **Simple sorting or classification** → Claude Haiku 4.5 (`claude-haiku-4-5`): cheapest, fastest
- **Moderate reasoning** → Claude Sonnet 5 (`claude-sonnet-5`): good balance
- **Hard tasks** (graduate-level science, long planning chains, complex code generation) → Claude Opus 4.8 (`claude-opus-4-8`) or Claude Fable 5 (`claude-fable-5`): most capable, most expensive

As of 2026-07-18, Haiku 4.5 costs $1 per MTok input versus $10 per MTok for Fable 5 — a 10-times difference. (MTok = one million tokens. A typical paragraph is roughly 100–150 tokens, so one million tokens is roughly 7,000–10,000 paragraphs.) Running 10,000 screening cases through Haiku instead of Fable 5 saves $90 per million input tokens.

🕒 **verify live:** Claude Sonnet 5 is on introductory pricing ($2/$10 per MTok input/output) through August 31, 2026 — the price reverts to $3/$15 after that. Always verify current pricing at [platform.claude.com/docs/en/about-claude/pricing](https://platform.claude.com/docs/en/about-claude/pricing) before budgeting. Prices change with model releases.

**Why (beginner):** Choosing the right model tier is the single highest-leverage cost lever for large eval suites. "Harder tasks benefit from more capable models" is a general rule — but always measure on a small random sample first, because the quality difference may be negligible for your specific use case.

**Caveat / contested:**
- Always measure first: run a random sample through both tiers and compare your eval scores before committing to the cheaper model at scale.
- Haiku 4.5 has a 200,000-token context window versus 1 million tokens for Opus 4.8. Eval cases that involve long documents or long conversation histories may require the larger context window.

**Sources:** [platform.claude.com/docs/en/about-claude/models/overview](https://platform.claude.com/docs/en/about-claude/models/overview) (Anthropic, 2026-07-18) · [platform.claude.com/docs/en/about-claude/pricing](https://platform.claude.com/docs/en/about-claude/pricing) (Anthropic, 2026-07-18)
**Confidence:** 📄 vendor-documented (pricing and model specs from Anthropic only)

---

## Practice 7: Treat Anthropic's published benchmark scores as signals, not guarantees

**What is a benchmark?** A benchmark is a standardized test — a fixed set of questions or tasks — that researchers use to compare AI models. The scores look precise but come with important caveats.

**Do:** When reading Anthropic's system cards (detailed technical reports about each model) or the Transparency Hub, look at the evaluation *methodology* — which benchmark, which settings, which other models were compared — not just the headline number. Cross-reference scores across multiple benchmarks. Build your own held-out test set for your specific use case.

Benchmarks referenced in Anthropic system cards (one-line definitions):
- **ARC-AGI-2** — a visual and abstract reasoning benchmark; tests whether models can solve novel pattern problems that require general reasoning rather than memorized knowledge.
- **SWE-bench Verified** — a collection of real-world software engineering tasks from GitHub pull requests; measures how often the model correctly fixes a bug in an actual codebase.
- **GPQA Diamond** — graduate-level science questions in biology, chemistry, and physics; used to test expert-level reasoning.
- **MMLU** — 57 academic subjects ranging from STEM to law and history; now above 90% for all frontier models and no longer distinguishes between the top systems.

For reference: Claude Opus 4.6 scored 94.00% (ARC-AGI-1) and 69.17% (ARC-AGI-2) using 120,000 thinking tokens at High effort. Newer models (Opus 4.8, Fable 5) have been released with new system cards. 🕒 Check [anthropic.com/transparency](https://www.anthropic.com/transparency) for current figures.

**Why (beginner):** MMLU is now saturated above 90% for frontier models, so it no longer tells you which model is better. SWE-bench scores over 49% on isolated code problems may not reflect how the model performs on your actual codebase. A headline benchmark number is one signal, not a buying decision.

**Caveat / contested:**
- Data contamination is a real risk: if benchmark questions appear in a model's training data, scores can be inflated. Anthropic acknowledges this in their system cards but cannot fully audit for it.
- Anthropic's own benchmark scores use adaptive thinking at high or max effort. A developer running the same model at `low` effort will see lower scores. Always check which effort settings were used before comparing numbers.

**Sources:** [anthropic.com/transparency](https://www.anthropic.com/transparency) (Anthropic, 2026-07-18) · [stackviv.ai/blog/ai-model-benchmarks-mmlu-humaneval](https://stackviv.ai/blog/ai-model-benchmarks-mmlu-humaneval) (StackViv, 2026-07-18)
**Confidence:** ✅ independently-corroborated (Anthropic system cards + independent benchmark-interpretation article)

---

## Practice 8: When testing tool use, check tool selection, argument values, and schema compliance separately

**What is "tool use" (function calling)?** You can give Claude a set of tools — for example, a function that looks up the weather, or one that queries a database. When Claude decides to use a tool, the API does not return a normal text answer. Instead it returns a structured JSON object (a machine-readable block of data, formatted like `{"tool": "get_weather", "arguments": {"city": "Tokyo"}}`) containing the tool name and the arguments Claude wants to pass. Your code then actually runs the function and feeds the result back to Claude.

**Do:** When testing Claude's function-calling, run eval cases across three separate dimensions:

1. **Tool selection** — did Claude call the right tool for the request, or the wrong one?
2. **Argument correctness** — are the values Claude chose semantically correct? (Right units? Right date format? Right numeric type?)
3. **Schema compliance** — does the JSON Claude returned match the shape your tool definition requires?

Compare the actual `tool_use` block in the API response against what you expected. Anthropic's Claude Cookbook has a [tool evaluation example](https://platform.claude.com/cookbook/tool-evaluation-tool-evaluation) you can use as a starting framework.

**Why (beginner):** When Claude calls a function, the JSON output goes directly into your application code — not to a human reader. A wrong argument (for example, using `^` instead of `**` for exponentiation in a math function) or a missing required field can silently break your application downstream. Structured eval catches this before it reaches production.

**Caveat / contested:**
- Anthropic's Cookbook example evaluates accuracy as an exact-match against expected responses. For many real-world cases, functional equivalence is a better target than exact string match.
- Anthropic's internal data showed accuracy improving from 72% to 90% on complex parameter handling when `input_examples` were added to tool definitions. Include examples in your tool schema before blaming the model for low scores. Note: this figure is from an Anthropic engineering blog post with no published dataset or methodology — treat it as directional, not a reproducible benchmark.
- ⚠️ **WARNING:** Extended thinking (the effort parameter) with tool use has specific constraints: only `tool_choice: "auto"` or `"none"` is supported — you cannot force a specific tool. In multi-turn tool-use evaluations, you must preserve the thinking blocks from prior turns in the message history, or the API will return an error.
- Tool-use eval cases can be submitted through the Message Batches API (tool use is explicitly listed as batchable).

**Sources:** [platform.claude.com/cookbook/tool-evaluation-tool-evaluation](https://platform.claude.com/cookbook/tool-evaluation-tool-evaluation) (Anthropic, 2026-07-18) · [platform.claude.com/docs/en/build-with-claude/extended-thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking) (Anthropic, 2026-07-18) · [www.anthropic.com/engineering/advanced-tool-use](https://www.anthropic.com/engineering/advanced-tool-use) (Anthropic Engineering, 2026-07-18)
**Confidence:** 📄 vendor-documented (all sources are Anthropic)

---

## Practice 9: Evaluate multi-turn conversations turn by turn, not just on the final answer

**What is a multi-turn conversation?** Most AI applications are not single question-answer pairs. A customer service bot, a tutor, or a writing assistant might go back and forth with a user across ten or twenty exchanges. This is called a "multi-turn conversation."

**Do:** For agents that maintain state across turns, evaluate each turn independently as well as scoring the final answer. Check per turn: does the model remember facts the user stated earlier? Does it contradict itself? Does it stay focused on the user's goal across topic shifts? Use a per-turn rubric (1–5 scale per turn), then aggregate across turns. For state-dependent evals, inspect the memory or context blocks directly — not just what the assistant said — to confirm the information was actually stored.

**Why (beginner):** A model can give a correct final answer while having contradicted itself three turns earlier. Scoring only the last message misses the degradation patterns that real users experience. Checking each turn catches context drift before it frustrates users.

**Caveat / contested:**
- Multi-turn evals are harder to automate because they require simulating a realistic user who adapts to what the model said. A naive fixed script (a user that says the same things regardless of the model's response) misses failures that only appear when the user actually reacts.
- For long conversations, Claude uses **context compaction** — automatic summarization that activates when the conversation history grows too large to fit in Claude's memory limit. After compaction, the model works from a summary rather than the full history, which can alter what it "recalls" from earlier turns. Test around the compaction boundary if your application uses long sessions.
- Anthropic's safety team uses multi-turn evals internally, but the methodology is not publicly documented in detail.

**Sources:** [docs.letta.com/guides/evals/advanced/multi-turn-conversations](https://docs.letta.com/guides/evals/advanced/multi-turn-conversations/) (Letta, 2026-07-18) · [platform.claude.com/docs/en/docs/test-and-evaluate/develop-tests](https://platform.claude.com/docs/en/docs/test-and-evaluate/develop-tests) (Anthropic, 2026-07-18) · [getmaxim.ai/articles/how-to-ensure-consistency-in-multi-turn-ai-conversations](https://www.getmaxim.ai/articles/how-to-ensure-consistency-in-multi-turn-ai-conversations) (Maxim, 2026-07-18)
**Confidence:** ✅ independently-corroborated (Letta docs + Anthropic docs + Maxim article)

---

## Practice 10: Test for both over-refusal and under-refusal — vendor safety testing does not cover your deployment

**What is refusal?** Claude is trained to refuse requests that are harmful or violate Anthropic's policies. But sometimes it also refuses requests that are completely legitimate (a false positive), or fails to refuse something it should (a false negative). You need to test both.

**Do:** Build two separate safety eval suites:

1. **Under-refusal suite** — prompts that *should* be refused (harmful, policy-violating). Check that Claude refuses these.
2. **Over-refusal suite** (false positives) — prompts that look superficially risky but are legitimate (for example, "how does a lock-picking mechanism work?" from a security researcher). Check that Claude does *not* refuse these.

Target a calibration where the refusal rate tracks actual risk, not surface keywords. Run multi-turn escalation sequences — not just single harmful prompts — because gradual, step-by-step escalation across turns ("Crescendo jailbreaking") is more effective at bypassing safety than a single blunt attack.

**Why (beginner):** A model that refuses too many legitimate requests damages your product almost as badly as one that fails to refuse harmful ones. High over-refusal frustrates users and causes them to abandon your application. Anthropic's own system cards track over-refusal rates alongside harm rates — your evals should too.

**Caveat / contested:**
- ⚠️ **WARNING:** Anthropic's published safety evaluations are conducted on their own infrastructure with their standard safety guardrails enabled. If you fine-tune the model, use prompt injection paths, or turn off default safety system prompts, you are outside the scope of Anthropic's published safety results and you must run your own safety evaluation.
- A joint OpenAI-Anthropic safety evaluation (August 2025) found both companies' models showed "concerning forms of sycophancy" — a tendency to tell users what they want to hear — under certain multi-turn scenarios, even when single-turn refusals were strong. Your safety evals must include multi-turn social engineering scenarios.
- **Constitutional AI** is Anthropic's training technique that teaches Claude to reason from a set of ethical principles before answering, rather than relying on keyword filters. This makes Claude more consistent on ambiguous inputs, but it does not eliminate failures — especially under adversarial multi-turn pressure.

**Sources:** [trydeepteam.com/guides/guide-red-teaming-anthropic](https://www.trydeepteam.com/guides/guide-red-teaming-anthropic) (DeepTeam, 2026-07-18) · [frugaltesting.com/blog/how-claude-is-trained-and-tested-for-safety-at-anthropic](https://www.frugaltesting.com/blog/how-claude-is-trained-and-tested-for-safety-at-anthropic) (Frugal Testing, 2026-07-18) · [edtechinnovationhub.com — openai-and-anthropic-cross-test-ai-models](https://www.edtechinnovationhub.com/news/openai-and-anthropic-cross-test-ai-models-in-rare-joint-safety-evaluation) (EdTech Innovation Hub, 2026-07-18) · [anthropic.com/transparency](https://www.anthropic.com/transparency) (Anthropic, 2026-07-18)
**Confidence:** ✅ independently-corroborated (multiple independent publishers + Anthropic docs)

---

## Held pending fixes

- Claude Opus 4.6 system card PDF (ARC-AGI benchmark figures): PDF exceeds fetch tool size limit. Figures (94.00% ARC-AGI-1, 69.17% ARC-AGI-2 at 120k tokens / High effort) corroborated via system-card search index and ARC Prize Foundation reporting. Recommend a human open the PDF at [anthropic.com/transparency](https://www.anthropic.com/transparency) to fully close the loop. ⚠ PENDING

---

## CHANGELOG

### Inherited from the 2026-07-18 technical entry (facts unchanged, sources unchanged)
1. **[SKEPTIC FIX]** LLM-as-judge (Practice 2): Replaced three Future AGI posts as the sole source for the 10–25% self-preference bias figure. Now cites Zheng et al. 2024 (MT-Bench, arXiv:2306.05685) as the academic primary source; Future AGI consolidated to a single vendor citation.
2. **[SKEPTIC FIX]** Tool-use accuracy (Practice 8): Added "on complex parameter handling" scope qualifier to the 72% to 90% accuracy improvement figure. Added explicit note that this is not a reproducible benchmark.
3. **[BEGINNER KILL]** Batch API (Practice 3): Added prominent worked cost example before the code block, instructing readers to estimate total cost and set a Workspace spend limit before submitting. Added "start with 10-request test batch" recommendation.
4. **[BEGINNER KILL]** Adaptive thinking (Practice 5): Replaced "substantially more" with a concrete multiplier ("10x or more") and explicit instruction to test on 5 cases and check billing before scaling.
5. **[BEGINNER FIX]** Console Evaluation tool (Practice 1): Added prerequisite — sign up for an Anthropic account at console.anthropic.com; defined what the Workbench is.
6. **[BEGINNER FIX]** LLM-as-judge (Practice 2): Added explicit note that GPT-5 and Gemini require separate vendor accounts, separate API keys, and separate billing.
7. **[BEGINNER FIX]** Adaptive thinking (Practice 5): Added full messages.create() call context showing the effort parameter in a runnable code snippet, including the import statement.
8. **[BEGINNER FIX]** Model capability tiering (Practice 6): Defined "MTok" with plain-language explanation (one million tokens; roughly 100-150 tokens per paragraph).
9. **[BEGINNER FIX]** Benchmark scores (Practice 7): Added one-line definitions for ARC-AGI-2, SWE-bench Verified, GPQA Diamond, and MMLU.
10. **[TIMEKEEPER KILL]** Adaptive thinking (Practice 5): Fixed caveat — Opus 4.5 incorrectly listed as not supporting the effort parameter. Corrected to apply only to Haiku 4.5.
11. **[TIMEKEEPER FIX]** Adaptive thinking (Practice 5): Updated primary model reference from "Opus 4.6 and later" to "Opus 4.8, Fable 5, Sonnet 5, and predecessors back to Opus 4.6."
12. **[TIMEKEEPER FIX]** Batch API (Practice 3): Added two missing unsupported parameters: cache_hint/context_hint and research_preview_2026_02.
13. **[TIMEKEEPER FLAG]** Batch API and Model tiering (Practices 3 and 6): Added explicit Sonnet 5 introductory pricing expiry date (August 31, 2026) with note about post-expiry pricing.
14. **[AUDIENCE FIX]** Front matter: corrected audience from "people new to AI" (original draft error in the technical entry) to "technically comfortable readers" in the technical entry; set back to "people new to AI" for this beginner track.

### Beginner re-level changes (this file only)
- Re-leveled from the 2026-07-18 technical entry; facts unchanged.
- Added "What this guide is about" introduction explaining what evaluation means for a newcomer.
- Added "What is..." plain-language definitions at the top of practices 2 (LLM-as-judge), 3 (Batches API), 5 (adaptive thinking), 7 (benchmark), 8 (tool use / function calling), 9 (multi-turn conversation), and 10 (refusal).
- Numbered the practices 1 through 10 for easier navigation.
- Moved the cost warning in Practice 3 (Batches API) to a prominent position before the API call example, with a worked formula and numbered pre-flight checklist, per KILL item 1.
- Replaced "substantially more" in Practice 5 with "10 times or more" and added the explicit "test on 5 cases" instruction, per KILL item 2.
- Added account and API-key prerequisites for GPT-5 and Gemini in Practice 2, per FIX item 2.
- Added full import + method context for the effort parameter code snippet in Practice 5, per FIX item 3.
- Added ARC-AGI-2 definition in Practice 7 (the technical entry included ARC-AGI-1 and ARC-AGI-2 scores but the beginner lens noted ARC-AGI-2 needed a definition), per FIX item 6.
- Added one-sentence explanation of context compaction in Practice 9, per FLAG item.
- Added one-sentence definition of Constitutional AI in Practice 10, per FLAG item.
- Added note that claude-opus-4-8 in the LLM-as-judge example code is a real model ID, per FLAG item.
- No new facts, statistics, or URLs introduced. All source links preserved verbatim.
