# Fine-Tuning and Adapting Language Models — Beginner Guide (as of 26 Jul 2026)

> A plain-English guide explaining when to fine-tune a language model versus using simpler approaches, how to prepare data safely, and what traps to avoid — written for people new to AI.


<!-- This file lands at content/ai/beginner/fine-tuning-when-and-why/2026-07-26/index.md
     and is an IMMUTABLE dated snapshot. Once published it is never edited — a refresh is a
     NEW <snapshot-date> dir. Source tiers: independently-corroborated = 2+ DIFFERENT publishers;
     vendor-documented = official vendor docs only (authoritative, single source). -->

# Fine-Tuning and Adapting Language Models (as of 26 Jul 2026)

> **Grading note.** A dated snapshot — accurate as of **26 Jul 2026**, frozen here and kept as a
> permanent archive entry. Research-drafted by a pupil, graded by the 3-lens panel + sensei.
> Corrections applied inline; unverifiable gaps marked ⚠ PENDING — never guessed.

---

## Before you begin

This guide assumes you already know:

- **What an LLM API call is.** You have sent at least one request to a model like GPT-4o, Claude, or Gemini — either through a web interface or a code library — and received a text response.
- **Basic Python.** You can read a short Python snippet and understand what it does at a high level, even if you could not write it from scratch.
- **Cloud billing awareness.** You understand that cloud services (AWS, Google Cloud, Azure, or GPU rental platforms) bill your credit card based on what you use, and that an idle service left running can accumulate charges.

If any of those feel unfamiliar, pause and get comfortable with them first. Fine-tuning involves training runs that cost real money and can produce confusing errors if your environment is not set up correctly.

---

## What is fine-tuning?

**Fine-tuning** is the process of taking a pre-trained language model (one that has already learned from vast amounts of text) and continuing to train it on your own smaller dataset. This adjusts the model's internal settings — called weights or parameters — so it behaves differently: following a specific style, mastering the vocabulary of your industry, or producing a particular output format.

Unlike writing a clever system prompt (instructions you send to the model at the start of a conversation), fine-tuning changes the model permanently. The result is a separate file — called a checkpoint — that you own, store, and deploy independently. Updating a fine-tuned model's knowledge means retraining it; you cannot just swap in new facts the way you can update a document.

---

## How to read the labels

- ✅ **independently-corroborated** — 2+ independent publishers
- 📄 **vendor-documented** — official docs only (authoritative, single source)
- ⚠️ **WARNING** — a default that can cost money, break the machine, or remove a safety net
- 🕒 **verify live** — fast-moving (versions/prices/quotas); check the current value

---

## Practice 1: Use the escalation ladder — prompt engineering first, RAG second, fine-tuning last

**Do:** Before spending compute on fine-tuning, try the cheapest technique that can solve the problem. Start with prompt engineering (hours, zero incremental cost). If the model lacks current or proprietary facts, add RAG (days, $50–500/month for vector store and embeddings). Fine-tune only when behavior, reasoning style, or output format still fall short — and confirm the shortfall with a quantitative eval, not gut feeling.

**Definitions:**
- **Prompt engineering** — writing better instructions in the text you send to the model. Free, instant, and reversible.
- **RAG (Retrieval-Augmented Generation)** — a system that looks up relevant documents from your own database before asking the model a question, so the model has current or private facts available. Reversible in days.
- **Fine-tuning** — permanently retraining the model on your own examples (this guide). Takes days of iteration and is hard to undo.

**Why it matters:** Fine-tuning changes the model's weights permanently, takes days of iteration, and produces a model that cannot update its knowledge without retraining. Prompt engineering and RAG are reversible in minutes. Most teams underinvest in prompt engineering before reaching for fine-tuning.

**What goes wrong if you skip this:** Teams spend weeks building a fine-tuning pipeline and thousands of dollars on GPU time, then discover a better system prompt would have solved the problem in an afternoon.

**Caveat / contested:** The escalation threshold has risen as frontier base models improve. Tasks that required fine-tuning in 2023 (e.g., consistent JSON output) are often solved by a structured-output system prompt on GPT-4o, Claude Sonnet 5, or Gemini 2.5 in 2026. 🕒 Re-evaluate when a new base model releases.

**Sources:**
- [thedatascientist.com — Fine-Tuning vs RAG vs Prompt Engineering](https://thedatascientist.com/fine-tuning-rag-or-prompt-engineering/) (fetched 2026-07-26)
- [kunalganglani.com — Fine-Tuning vs RAG vs Prompt Engineering 2026](https://www.kunalganglani.com/blog/fine-tuning-vs-rag-prompt-engineering) (fetched 2026-07-26)
- [solutelabs.com — RAG vs Fine-Tuning](https://www.solutelabs.com/blog/rag-vs-fine-tuning) (fetched 2026-07-26)

**Confidence:** ✅ independently-corroborated (three independent publishers agree on the escalation order)

---

## Practice 2: Prioritise data quality ruthlessly over raw dataset size

**Do:** Curate before you collect. Deduplicate examples (including near-duplicates), fix inconsistent labels, remove formatting noise, and verify that each example actually represents a task your model will face in production. An 80/20 audit — fixing the worst 20% of your dataset — commonly delivers 80% of the quality gain. Treat 1,000 carefully cleaned examples as a more reliable baseline than 100,000 scraped ones.

**Why it matters:** Fine-tuning uses far fewer examples than pre-training (thousands, not trillions). Every bad example has outsized influence. Noisy labels cause the model to memorise the noise, not the task, which shows up as erratic outputs in production that are hard to debug.

**What goes wrong if you skip this:** The model learns your mistakes as if they were correct behaviour. You end up with a model that is confidently wrong in exactly the ways your bad data was wrong — and you may not notice until it has already affected users.

**Concrete size guidance** (🕒 verify live — model capabilities shift):

| Task type | Practical range |
|---|---|
| Simple classification | 100–500 examples |
| Structured extraction | 200–1,000 examples |
| Content / style generation | 500–2,000 examples |
| Domain adaptation (medical, legal) | 1,000–5,000+ examples |
| Translation / summarisation | 5,000–200,000+ examples |

⚠️ **WARNING:** Collecting training data from public benchmarks you also intend to evaluate on creates data contamination and inflates reported scores. Keep eval data completely separate from data collection pipelines. In plain terms: if you train the model on the same questions you later use to test it, the test score will look great but the model will fail on real tasks it has never seen.

**Sources:**
- [latitude.so — How Dataset Size Impacts LLM Fine-Tuning](https://latitude.so/blog/dataset-size-impacts-llm-fine-tuning) (fetched 2026-07-26)
- [machinelearningmastery.com — Practitioner's Guide to Fine-Tuning](https://machinelearningmastery.com/the-machine-learning-practitioners-guide-to-fine-tuning-language-models/) (fetched 2026-07-26)
- [cmarix.com — LLM Fine-Tuning Techniques & Data Best Practices](https://www.cmarix.com/blog/llm-fine-tuning-techniques-data-best-practices/) (fetched 2026-07-26)

**Confidence:** ✅ independently-corroborated

---

## Practice 3: Lock down a held-out test set before any training begins

**Do:** Split data before touching it for training. A common split is 80% train / 10% validation / 10% test, though 70/15/15 is also defensible for smaller datasets. The validation set drives hyperparameter decisions (learning rate, LoRA rank, epochs — see Practice 4 for LoRA). The test set is evaluated exactly once, at the very end — never used to pick or compare checkpoints.

**Why it matters:** Every time you look at your test results and adjust something, you are implicitly training on the test set. The test set's job is to estimate real-world performance on data the model has never influenced. If you peek repeatedly, your final numbers are optimistic and your users will experience worse performance than reported.

**What goes wrong if you skip this:** Your model appears to perform well during development but fails in production. Users experience worse results than your internal metrics predicted, and you have no reliable way to know which checkpoint is actually your best.

**Key leakage traps to avoid:**

- **Tokenizer fitting on the full dataset.** A tokenizer is a program that breaks text into numbered chunks (tokens) before feeding it to the model. If you tune the tokenizer's vocabulary on your entire dataset — including the test portion — the model has indirectly "seen" the test data. Always fit the tokenizer on training data only, then apply it to validation and test.
- **Same entity in multiple splits.** If the same user, document, or patient record appears in both training and test data, the model effectively memorises that specific example. Use grouped splits to keep each entity in exactly one split.
- **Time-series data.** If your data has a time component, split chronologically: train on the past, test on the future.

⚠️ **WARNING:** LLM pre-training corpora are so large that popular public benchmarks may already appear in the base model's training data. Three common ones:
- **MMLU** (Massive Multitask Language Understanding) — a broad knowledge test covering 57 subjects
- **GSM8K** — a set of grade-school maths word problems used to measure arithmetic reasoning
- **HumanEval** — a set of programming problems used to measure code generation quality

Because these benchmarks are so widely known, they may have leaked into the model's original training. Rely on your own held-out production examples for honest eval, not exclusively on public benchmarks.

**Sources:**
- [lightly.ai — Train Test Validation Split Best Practices](https://www.lightly.ai/blog/train-test-validation-split) (fetched 2026-07-26)
- [gtracademy.org — Train/Validation/Test Splits and Data Leakage in Practice](https://gtracademy.org/train-validation-test-splits-and-data-leakage-in-practice/) (fetched 2026-07-26)
- [heavybit.com — LLM Fine-Tuning Guide for Engineering Teams](https://www.heavybit.com/library/article/llm-fine-tuning) (fetched 2026-07-26)

**Confidence:** ✅ independently-corroborated

---

## Practice 4: Mitigate catastrophic forgetting with parameter-efficient adapters and regularisation

**Plain-English glossary for this practice:**

- **LoRA (Low-Rank Adaptation):** Instead of retraining all of the model's millions or billions of internal numbers, LoRA adds two small "side tables" (matrices) next to each layer of the model. Only those side tables are updated during training. The original model weights stay mostly frozen. The result is a tiny file — called an adapter — that you attach to the base model. Adapters are less than 1% of the full model size.
- **QLoRA:** The same idea as LoRA, but the base model is first compressed into a smaller numerical format (4-bit quantisation) to save memory. Lets you fine-tune larger models on smaller GPUs.
- **PEFT (Parameter-Efficient Fine-Tuning):** An umbrella term for any method — including LoRA and QLoRA — that fine-tunes only a small fraction of a model's parameters instead of all of them. "PEFT adapter" and "LoRA adapter" are often used interchangeably.
- **EWC (Elastic Weight Consolidation):** A regularisation technique that adds a penalty to the training process to discourage the model from changing weights that were important for earlier tasks.

**Do:** When fine-tuning on a narrow task, do not update all model weights unless you have a compelling reason and a full benchmark suite to catch regressions. Instead, use **LoRA** or **QLoRA**, leaving the base weights largely frozen. For continual fine-tuning on multiple sequential tasks, add EWC penalties or maintain a small rehearsal buffer of earlier-task examples.

**Why it matters:** A model fine-tuned to write legal briefs may "forget" how to do arithmetic or write coherent general prose. This is called **catastrophic forgetting** — the model overwrites general-purpose weights with task-specific ones. LoRA avoids this by leaving the base weights mostly untouched; only the small adapter layers change.

**What goes wrong if you skip this:** You fine-tune a capable general model into a narrow specialist, then discover it can no longer do the things it was already good at. You have made the model worse overall while only improving one capability.

**2025–2026 options beyond vanilla LoRA** (🕒 verify live — this area moves fast):
- **OPLoRA / O-LoRA** (Orthogonal-Projection LoRA): Adds a constraint that actively prevents the adapter from overwriting the knowledge directions already encoded in the base model.
- **EWCLoRA:** Combines EWC importance-weighting (protecting important weights) with LoRA's efficiency.
- **LwF (Learning Without Forgetting):** Uses the original model as a teacher — the new model is penalised during training if its outputs diverge too much from the original. Useful when you cannot keep historical training data (e.g., for privacy reasons).
- **DDP (Distributed Data Parallel):** A technique for spreading a single training job across multiple GPUs on the same machine or cluster, so training finishes faster.
- **FSDP (Fully Sharded Data Parallel):** Similar to DDP, but more memory-efficient — each GPU holds only a fraction of the model weights at any one time, then shares them as needed.
- **FP16 (16-bit floating point) / bfloat16 (Brain Floating Point 16):** Number formats for storing model weights. Standard models use 32-bit numbers; FP16 and bfloat16 use 16-bit numbers, roughly halving the memory required. bfloat16 handles very large and very small numbers more gracefully than FP16.

⚠️ **WARNING:** LoRA alone does not guarantee zero forgetting in continual-learning scenarios where you repeatedly fine-tune on new tasks. Measure regression on a general capability benchmark (e.g., MMLU or a held-out general instruction set) after every run, not just task-specific metrics.

**Sources:**
- [brics-econ.org — Preventing Catastrophic Forgetting During LLM Fine-Tuning](https://brics-econ.org/preventing-catastrophic-forgetting-during-llm-fine-tuning-techniques-that-work) (fetched 2026-07-26)
- [arxiv.org — OPLoRA: Orthogonal Projection LoRA (2510.13003)](https://arxiv.org/pdf/2510.13003) (fetched 2026-07-26)
- [rohan-paul.com — Handling LLM Model Drift in Production](https://www.rohan-paul.com/p/ml-interview-q-series-handling-llm) (fetched 2026-07-26)

**Confidence:** ✅ independently-corroborated

---

## Practice 5: Lock your chat/instruction template and never change it between training and inference

**Do:** Pick a single chat template format before collecting training data and apply it without deviation throughout fine-tuning and every inference call. Document the exact template (system turn structure, role markers, separator tokens) and store it alongside model checkpoints. Do not upgrade to a different format mid-project.

**What is a chat template?** When you send a message to a language model, the raw text you type is wrapped in special markers — like labels on an envelope — that tell the model which part is your instruction, which part is the model's previous reply, and which part is a system-level directive. A "chat template" is the specific set of markers a given model family expects. Different model families use different markers.

**Common template families** (🕒 verify live — format specs update with new model releases):
- **ChatML:** `<|im_start|>system ... <|im_end|><|im_start|>user ... <|im_end|>` — widely used for DPO (preference alignment — see Practice 7) pipelines and Llama-family models
- **Alpaca:** `### Instruction:\n...\n\n### Response:\n` — simpler, no special tokens
- **Llama-3 native:** `<|begin_of_text|><|start_header_id|>system<|end_header_id|>...<|eot_id|>` — required for Meta's Llama-3.x instruct models

**Applying the template in code:** Use `tokenizer.apply_chat_template()`. This is a Python method from the Hugging Face `transformers` library (version 4.40 or later). To use it you need Hugging Face `transformers` installed (`pip install transformers>=4.40`) and a `tokenizer` object loaded from your chosen model. It formats your messages automatically into the correct template for that model, avoiding manual formatting errors.

**Why it matters:** A fine-tuned model learns to expect a specific template as part of the task definition. Research (arxiv 2402.18540) shows measurable performance drops when inference templates differ from training templates — alignment and safety properties are especially sensitive.

**What goes wrong if you skip this:** The model produces garbled, incomplete, or unsafe outputs because it is receiving input in a format it was not trained on — like trying to read a letter written in an unexpected language.

⚠️ **WARNING (security):** The ChatBug vulnerability (arxiv 2406.12935) shows that adversaries who know your chat template can craft inputs that deviate from it and bypass safety alignment. Do not publish your template publicly in adversarial contexts.

**Sources:**
- [arxiv.org — Keeping LLMs Aligned After Fine-tuning: The Crucial Role of Prompt Templates (2402.18540)](https://arxiv.org/abs/2402.18540) (fetched 2026-07-26)
- [arxiv.org — ChatBug: A Common Vulnerability of Aligned LLMs Induced by Chat Templates (2406.12935)](https://arxiv.org/abs/2406.12935) (fetched 2026-07-26)
- [cloudurable.com — Advanced Fine-Tuning Chat Templates](https://cloudurable.com/blog/advanced-fine-tuning-chat-templates/) (fetched 2026-07-26)

**Confidence:** ✅ independently-corroborated

---

## Practice 6: Run a quantitative eval harness before and after every fine-tuning run — never trust vibes

**Do:** Before training, establish a fixed eval benchmark that covers (a) your target task metric (ROUGE-L for summarisation, F1 / exact-match for extraction, custom rubric for generation) and (b) at least one general-capability probe (e.g., 50-question MMLU slice or a held-out instruction-following set). Run both the baseline prompted model and the fine-tuned model through the same benchmark. Ship only if the fine-tuned model beats the baseline on the task metric without regressing meaningfully on the general probe.

**Practical 4-step workflow:**

1. **Install `lm-eval` and run it on the base model.** Install with: `pip install lm-eval`. This installs `lm-evaluation-harness`, an open-source tool from EleutherAI that runs standard benchmarks against any Hugging Face-compatible model and outputs a score report. Run it on your base model before training and record both your task metric and a general metric (e.g., an MMLU slice score).
2. **Fine-tune.**
3. **Run the same harness on the fine-tuned checkpoint.** Use the identical `lm-eval` command you ran in step 1, pointing it at your new checkpoint instead of the base model.
4. **Run 20–30 representative production prompts through an LLM-as-judge rubric** to catch subjective quality differences that automated metrics miss.

**Why it matters:** "It feels better" is not a reproducible or defensible result. Quantitative evals catch regressions you would not notice by reading a handful of outputs. They also give you a rollback criterion: if the new checkpoint is worse, you keep the old one.

**What goes wrong if you skip this:** You ship a fine-tuned model that scores higher on your target task but has silently broken other capabilities. Users report strange behaviour. You have no baseline to compare against, so you cannot tell if the new model is better or worse.

**LLM-as-judge caveats:**
- Susceptible to verbosity bias (longer outputs score higher), position bias, and self-enhancement bias
- Cross-check a random 10–15% of judge scores against human labels before trusting the judge at scale

⚠️ **WARNING:** Do not use the same examples for judge evaluation that you used for hyperparameter selection — this constitutes peeking and inflates scores.

**Sources:**
- [deepeval.com — LLM-as-a-Judge: Top Evaluation Techniques and Best Practices](https://deepeval.com/blog/llm-as-a-judge) (fetched 2026-07-26)
- [machinelearningmastery.com — Practitioner's Guide to Fine-Tuning](https://machinelearningmastery.com/the-machine-learning-practitioners-guide-to-fine-tuning-language-models/) (fetched 2026-07-26)
- [heavybit.com — LLM Fine-Tuning Guide for Engineering Teams](https://www.heavybit.com/library/article/llm-fine-tuning) (fetched 2026-07-26)

**Confidence:** ✅ independently-corroborated

---

## Practice 7: Use DPO or ORPO instead of full RLHF for preference alignment in most cases

**Plain-English glossary for this practice:**

- **Preference alignment:** Training a model to produce outputs humans prefer — more helpful, less harmful, better tone — rather than just outputs that are statistically likely.
- **SFT (Supervised Fine-Tuning):** The basic form of fine-tuning: show the model many (prompt, ideal response) pairs and train it to reproduce those responses.
- **RLHF (Reinforcement Learning from Human Feedback):** A three-stage process: (1) humans rate model outputs to create preference data, (2) a separate "reward model" learns to predict those human ratings, (3) the main model is trained via reinforcement learning (specifically PPO) to score highly on the reward model.
- **PPO (Proximal Policy Optimization):** The reinforcement learning algorithm used inside full RLHF. Computationally expensive and finicky to tune.
- **Reward model:** A second model trained to predict human preference scores. Required for full RLHF but not for DPO or ORPO.
- **DPO (Direct Preference Optimization):** A simpler alternative to full RLHF. You collect (prompt, good response, bad response) triples and train directly on those — no separate reward model, no RL loop. The `beta` hyperparameter (typically 0.1–0.5) controls how far the trained model is allowed to drift from the original model's behaviour via a KL-divergence constraint.
- **KL-divergence constraint:** A mathematical guard rail that prevents the fine-tuned model from drifting too far from the base model's output distribution. Think of it as a leash — beta controls how long the leash is.
- **ORPO:** Even simpler than DPO. Combines the supervised fine-tuning loss and a preference penalty in a single training pass. No reference model required, fewer hyperparameters, more memory-efficient.
- **Policy / reference model:** In DPO, the "policy" is the model being trained; the "reference model" is the original frozen copy it is compared against for the KL constraint.

**Do:** If your goal is alignment — reducing harmful outputs, improving helpfulness, shaping conversational tone — collect preference pairs (prompt, chosen response, rejected response) and train with DPO or ORPO rather than the full RLHF/PPO pipeline.

**Why it matters:** Full RLHF requires training a separate reward model and running an RL loop (PPO), both of which are unstable and compute-intensive. DPO collapses this into a single supervised training step on preference pairs. ORPO is even simpler — it combines supervised fine-tuning loss and a preference penalty in one pass, requiring no reference model. Benchmarks show ORPO-trained Llama 7B outperforming 13B RLHF-instructed Llama on win-rate.

**What goes wrong if you skip this and use full RLHF unnecessarily:** You spend weeks debugging an unstable reward model, burn significant GPU budget, and may end up with a model that has drifted in unexpected ways because the RL loop is hard to control.

**Choosing between approaches:**
- **DPO** — Good default for most preference alignment tasks. Stable, well-understood, widely supported in tools like TRL.
- **ORPO** — Even simpler when you want to do SFT and alignment in one step. Good for memory-constrained setups.
- **Full RLHF/PPO** — Still appropriate when you need a separate reward model for complex multi-dimensional scoring, or when you are optimising something fundamentally non-differentiable. Expect instability, higher compute cost, and more hyperparameter sensitivity.

⚠️ **WARNING — reward hacking:** Any preference-optimisation method can be gamed by the model learning to produce outputs that score well on the reward signal without actually being better (e.g., very long responses, sycophantic phrasing). Measure on held-out human preference labels, not only automated reward scores.

**Sources:**
- [philschmid.de — How to align open LLMs in 2025 with DPO](https://www.philschmid.de/rl-with-llms-in-2025-dpo) (fetched 2026-07-26)
- [arxiv.org — Direct Preference Optimization (2305.18290)](https://arxiv.org/abs/2305.18290) (fetched 2026-07-26)
- medium.com/@jakubstrawadev — DPO & ORPO Overview (fetched 2026-07-26; 403 bot-protection, confirmed live via WebFetch 2026-07-27)

**Confidence:** ✅ independently-corroborated

---

## Practice 8: Model the total cost of ownership before committing to fine-tuning at scale

**Do:** Run a break-even analysis before choosing between RAG and fine-tuning for a production workload. The two approaches have fundamentally different cost shapes:

| Cost component | RAG | Fine-tuning |
|---|---|---|
| Upfront build | Low (days) | High (data prep + training runs) |
| Per-query run cost (2026 indicative, per API call) 🕒 | ~$0.0056 (embedding lookup + retrieval + generation) | ~$0.004 (generation only, shorter prompt) |
| Knowledge update cost | Incremental (add new documents to the database) | Full retrain cycle |

**Reading the cost table:** The "per-query run cost" figures are per individual API call (one user question and one model response). They are 2026 indicative prices from a single source — treat them as rough order-of-magnitude guidance, not precise quotes. Actual costs depend on your chosen model, token counts, and provider pricing tier.

**Worked example (illustrative — not a threshold to rely on):** One 2026 TCO calculator (single source; methodology undisclosed) finds that at 10k queries/month over 24 months, fine-tuning is roughly 1.75x more expensive than RAG because training and update costs dwarf the per-query savings. The crossover is estimated at around 1M queries/month on a stable, narrow domain. Treat this as directional guidance, not a precise number — the exact crossover depends heavily on your chosen model, pricing tier, and update frequency.

**Why it matters:** Fine-tuning has a high upfront cost that only pays off at large query volumes with infrequently-updated knowledge. For most early-stage projects, RAG is cheaper and more flexible.

**What goes wrong if you skip this:** You invest weeks of engineering and thousands of dollars building a fine-tuning pipeline, then discover your query volume never justified the upfront investment.

⚠️ **WARNING:** These cost figures are indicative and change as API providers reprice. 🕒 Verify against current vendor pricing before committing to architecture.

**Sources:**
- [digitalapplied.com — RAG vs Fine-Tuning TCO Calculator 2026](https://www.digitalapplied.com/blog/rag-vs-fine-tuning-tco-calculator-comparison-2026) (fetched 2026-07-26) — single-source TCO table; direction confirmed independently
- [kunalganglani.com — Fine-Tuning vs RAG vs Prompt Engineering 2026](https://www.kunalganglani.com/blog/fine-tuning-vs-rag-prompt-engineering) (fetched 2026-07-26)
- [solutelabs.com — RAG vs Fine-Tuning](https://www.solutelabs.com/blog/rag-vs-fine-tuning) (fetched 2026-07-26)

**Confidence:** ✅ independently-corroborated (directional conclusion confirmed across sources; exact dollar figures are single-sourced and 🕒 verify live)

---

## Practice 9: Choose your base model deliberately — benchmark, licence, and ecosystem all matter

**Plain-English glossary for this practice:**

- **MMLU (Massive Multitask Language Understanding):** A standard benchmark that tests a model's general knowledge across 57 subjects. Higher score = better general knowledge.
- **GSM8K:** A benchmark of grade-school maths word problems. Higher score = better arithmetic reasoning.
- **HumanEval:** A benchmark of programming problems. Higher score = better code generation.
- **Apache 2.0:** An open-source software licence with no royalty restrictions and very permissive commercial use terms. Generally the most business-friendly open licence.
- **MAU (Monthly Active Users):** The number of unique users who interact with your product in a given month.
- **Benchmark headroom:** How much "room to grow" a model has after fine-tuning. A model that already scores well on broad benchmarks typically fine-tunes into a better specialist than one that starts weak.

**Do:** Before collecting training data, choose the base model family you will fine-tune. The choice locks you into a tokenizer, context length, chat template format, and licence. Evaluate on three axes:

1. **Benchmark headroom:** A model with higher pre-training quality gives you more to work with after fine-tuning. Check MMLU (general reasoning), GSM8K (maths), and HumanEval (code) for your task domain.
2. **Licence for commercial use:** Verify before committing. Apache 2.0 (Qwen 2.5/3, Mistral, Gemma 4) has no royalty restrictions. Meta's Llama Community Licence allows commercial use but has an acceptable-use policy and a 700M+ MAU threshold that triggers a separate agreement. Google's Gemma 3 licence prohibits training competing foundational models — Gemma 4 (released April 2, 2026) switched to Apache 2.0 and has no such restriction.
3. **Ecosystem maturity:** LoRA configurations, community datasets, and tooling (Unsloth, Axolotl, LLaMA Factory) are most battle-tested for Llama and Qwen families.

**2026 7–8B tier snapshot** (🕒 verify live — new model releases are frequent):

| Model | MMLU | GSM8K | Licence | Fine-tune ecosystem |
|---|---|---|---|---|
| Qwen 2.5 7B | 70.2 | 82.3 | Apache 2.0 | Strong |
| Llama 3.1 8B | 68.4 | 79.6 | Meta Community | Largest |
| Gemma 3 12B | 72.1 | — | Google ToS (restrictive) | Good |
| Gemma 4 (various) | — | — | Apache 2.0 | Growing |
| Mistral 7B | 63.7 | — | Apache 2.0 | Moderate |

Note: "Llama 3.3 8B" does not exist — Llama 3.3 was released in December 2024 as a 70B-only model. The 8B tier from the Llama 3 lineage is Llama 3.1 8B. Benchmark scores in the table above are from the cited source (ertas.ai); verify against official model cards. 🕒

**Key insight:** Distillabs research (12 models, 8 tasks, 2026) found that "fine-tuning matters more than base model choice" — a well-tuned 1B model can surpass a prompted 8B model on narrow tasks. Choose the smallest model that meets your latency and memory budget, not the largest available.

**Why it matters:** Choosing the wrong base model means your training data, fine-tuning pipeline, and licence compliance work may all need to be redone from scratch. A licence mistake discovered after deployment can force a product takedown.

**What goes wrong if you skip this:** You spend weeks fine-tuning a model under a licence that prohibits your intended use, then must rebuild everything on a different base model.

⚠️ **WARNING:** Always read the current licence document, not a third-party summary. Model licences have been updated mid-release (Llama 2 and Llama 3 have different licence terms; Gemma 3 and Gemma 4 have different licences). A blog post summarising a licence may be out of date.

**Sources:**
- [ertas.ai — Which Open-Source Model Should You Fine-Tune in 2026](https://www.ertas.ai/blog/best-open-source-model-fine-tune-2026) (fetched 2026-07-26)
- [distillabs.ai — We Benchmarked 12 Small Language Models Across 8 Tasks](https://www.distillabs.ai/blog/we-benchmarked-12-small-language-models-across-8-tasks-to-find-the-best-base-model-for-fine-tuning/) (fetched 2026-07-26)
- [tech.slashdot.org — Gemma 4 Apache 2.0 announcement](https://tech.slashdot.org/story/26/04/02/1735238/google-announces-gemma-4-open-ai-models-switches-to-apache-2-0-license) (fetched by Timekeeper 2026-07-26)

**Confidence:** ✅ independently-corroborated (benchmark figures and licence terms are 🕒 verify live; "Llama 3.3 8B" corrected to "Llama 3.1 8B" — the source used an incorrect model label)

---

## Practice 10: Treat production data drift as the primary long-term threat to fine-tuned model quality

**Plain-English glossary for this practice:**

- **Data drift:** Over time, the questions real users ask change — new topics emerge, slang evolves, business context shifts. If your training data no longer reflects what users are actually sending, the model's quality degrades even though nothing about the model itself changed.
- **PSI (Population Stability Index):** A statistical measure of how much a distribution has shifted. A PSI above 0.2 means the new data distribution is meaningfully different from the training data distribution. Think of it as a "drift alarm" — a number that tells you whether what users are sending today looks very different from what the model was trained on.
- **Cosine distance to training centroid:** Each prompt can be converted into a list of numbers (an embedding) that represents its meaning. The "centroid" is the average of all training prompt embeddings. Cosine distance measures how far a new prompt's embedding is from that average. A large cosine distance means the new prompt is semantically very different from anything in the training set.
- **PEFT adapter:** The small trained side-matrices produced by LoRA or QLoRA (defined in Practice 4). These are separate files that attach to a specific base model version.
- **Canary deployment:** Routing a small percentage of real user traffic (e.g., 5–10%) to a new model version while the rest of traffic stays on the old version. Lets you catch problems before they affect everyone.

**Do:** Monitor your fine-tuned model's input distribution continuously after deployment. Set automated alerts on two jointly-triggered conditions: (a) embedding drift in incoming prompts (PSI above 0.2 or cosine distance to training centroid above threshold) AND (b) a measurable drop in your task eval score (3–5 points). When both signals fire together, trigger a retraining job. If only one fires, investigate but do not immediately retrain — drift without eval impact is a false alarm.

**Recommended pipeline:**
1. Log all production inputs and outputs (with user consent / privacy controls in place)
2. Run your eval harness on a random sample of production outputs weekly
3. On drift-plus-eval-drop alert, assemble a fresh batch of production examples, deduplicate against existing training data, label (human or LLM-assisted), and run a new fine-tuning job on a mix of original + new examples
4. Version-pin checkpoints: tag each fine-tuned checkpoint with its training-data snapshot date; run a canary deployment on the new checkpoint before cutting over

**Why it matters:** A fine-tuned model that worked well at launch can silently degrade over months as the real-world inputs drift away from the training distribution. Without monitoring, you only discover the problem when users complain.

**What goes wrong if you skip this:** Your model gradually gets worse without anyone noticing. By the time users report problems, the model's quality may have degraded significantly, and you have no logged data to diagnose what changed.

⚠️ **WARNING:** Never retrain on raw unreviewed production data. User inputs may contain prompt injections (attempts by users to override your system instructions), PII (personally identifiable information such as names, email addresses, phone numbers), or adversarial content. Always run a data-cleaning pass before any production example enters the training pipeline. Failing to do this can leak user data or teach the model to follow malicious instructions.

⚠️ **WARNING:** PEFT adapters are not interchangeable across base model versions. If the base model is updated (e.g., Llama 3.1 to 3.3), re-run fine-tuning from scratch on the new base rather than reusing old adapter weights. The adapter was trained to attach to a specific set of frozen weights; attaching it to different weights produces unpredictable results.

**Sources:**
- [rohan-paul.com — Handling LLM Model Drift in Production](https://www.rohan-paul.com/p/ml-interview-q-series-handling-llm) (fetched 2026-07-26)
- [futureagi.com — Model Drift vs Data Drift Detection & Mitigation 2026](https://futureagi.com/blog/model-vs-data-drift-how-to-identify-and-handle-it/) (fetched 2026-07-26)

**Confidence:** ✅ independently-corroborated

---

## CHANGELOG

### Re-leveled from the 2026-07-26 technical entry; facts unchanged.

The following beginner corrections were applied. No new facts or URLs were introduced.

1. **[KILL-W1 / KILL-X1]** Added "Before you begin" prerequisites box at the top listing assumed knowledge: LLM API calls, basic Python, cloud billing awareness.

2. **[FIX-W8]** The "What is fine-tuning?" introductory section was present in the technical entry and has been preserved and expanded with plain-English context about checkpoints and the difference from system prompts.

3. **[KILL-W2]** Expanded the LoRA and QLoRA explanation in Practice 4 into a plain-English glossary entry. "Small rank-decomposition matrices" replaced with "two small side tables (matrices) next to each layer of the model." QLoRA defined as LoRA plus 4-bit compression of the base model.

4. **[KILL-W3]** Added definition of PEFT (Parameter-Efficient Fine-Tuning) as a plain-English glossary entry in Practice 4 and a reminder in Practice 10, so the warning about PEFT adapter incompatibility is fully understandable.

5. **[FIX-W1]** Added plain-English glossary for Practice 7 defining DPO, ORPO, RLHF, PPO, KL-divergence constraint, SFT, policy/reference model, and reward model before the Do section.

6. **[FIX-W2]** Added plain-English definitions of PSI (Population Stability Index) and cosine distance to training centroid in the Practice 10 glossary.

7. **[FIX-W3]** Added a plain-English explanation of "tokenizer" in Practice 3's leakage traps section.

8. **[FIX-W4]** Added the install command (`pip install lm-eval`) and a description of what `lm-evaluation-harness` is and what it outputs in Practice 6, step 1.

9. **[FIX-W5]** Clarified that `tokenizer.apply_chat_template()` is a Python method from the Hugging Face `transformers` library (v4.40+), added the install command (`pip install transformers>=4.40`), and explained what a `tokenizer` object is in context.

10. **[FIX-W6]** Added "per API call" unit clarification to the cost table in Practice 8 and added a plain-English explanation of what the figures mean.

11. **[FIX-W7]** Added plain-English definitions of MMLU, GSM8K, HumanEval, Apache 2.0, and MAU (Monthly Active Users) on first use in Practice 3 and Practice 9.

12. **[FIX-X1]** Added inline glosses for EWC, OPLoRA, DDP, FSDP, FP16, and bfloat16 in Practice 4. Added plain-English explanation of "canary deployment" in Practice 10.

13. **[structural]** Added "What goes wrong if you skip this" to every practice, giving beginners a concrete consequence to motivate each recommendation. No new facts introduced — consequences are derived from the "Why" text already present in the technical entry.

14. **[structural]** Added a plain-English glossary block at the top of each practice containing dense acronyms (Practices 4, 7, 9, 10) rather than interleaving definitions through the text, to reduce cognitive load.
15. **[Link-check gate]** medium.com/@jakubstrawadev (DPO & ORPO Overview, Practice 7 Sources) returned 403 bot-protection; confirmed live via WebFetch 2026-07-27. Unlinked to plain text per policy.

