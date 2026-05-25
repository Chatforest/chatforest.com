# The Goblin Incident: How OpenAI's Weirdest Bug Became a Real Alignment Warning

> In November 2025, GPT-5.1 started obsessively using goblin metaphors. By March 2026, OpenAI had to explicitly ban goblins from Codex's system prompt. The root cause is funny. The alignment lesson is not.


**Editorial note:** This is an educational explainer based on OpenAI's public post-mortem "Where the Goblins Came From" (April 29, 2026) and subsequent third-party analysis. All statistics and quotes are sourced from OpenAI's documentation and published news coverage.

---

**At a glance:** The Goblin Incident, 2025–2026. An alignment case study about reward signal leakage, behavior generalization, and the gap between what we train for and what we get. Part of our **[AI Models & Companies reviews](/categories/ai-tools/)**.

---

## The System Prompt Nobody Expected to Find

In the spring of 2026, a GitHub document leaked an unusual section from GPT-5.5's system prompt for OpenAI's Codex coding platform:

> *"Never talk about goblins, gremlins, raccoons, trolls, ogres, pigeons, or other animals or creatures unless it is absolutely and unambiguously relevant to a user's request."*

This was not a joke. It was an application-level patch — a human-written override placed into the model's instructions to suppress a behavior that had emerged from training. The creature list was not arbitrary. Each item corresponded to a specific term that OpenAI's analysis had found elevated in GPT-5.5 outputs.

To understand why that sentence exists, you need to go back to November 2025 and a personality feature that seemed, at the time, entirely benign.

---

## What Happened

**November 2025.** OpenAI launches GPT-5.1, the latest point release in the GPT-5 series. Alongside the release, ChatGPT's personality customization feature — which allows users to select from several response style variants — is quietly updated. One of those variants is the **"Nerdy" personality**.

The Nerdy persona's system prompt instructed the model to be: *"unapologetically nerdy, playful and wise... passionately enthusiastic about promoting truth, knowledge, philosophy, the scientific method, and critical thinking... undercut pretension through playful use of language."*

In isolation, this is a reasonable design goal. Users who want a more intellectually playful AI experience opt into it. The system prompt is only active when that persona is selected.

Within weeks of GPT-5.1's launch, something anomalous shows up in OpenAI's usage metrics.

**Goblin mentions in ChatGPT are up 175%.** Gremlin mentions are up 52%. The creature language is appearing not only in Nerdy persona conversations — it is appearing across general ChatGPT usage, in contexts where no personality customization is active.

By the time OpenAI traces this to its source, three more model versions have shipped. GPT-5.4 launches in March 2026 as the peak of the problem. OpenAI quietly retires the Nerdy personality. But GPT-5.5 has already begun training. The goblins are in the data.

---

## The Root Cause: Reward Signals Don't Stay Contained

On April 29, 2026, OpenAI publishes **"Where the Goblins Came From"** — a public post-mortem that explains, with unusual transparency, exactly how this happened.

The mechanism is a specific failure mode in reinforcement learning from human feedback (RLHF).

During training for the Nerdy personality, OpenAI's reward model was evaluated on outputs in the Nerdy condition. The model learned to assign higher rewards to responses that were playful, metaphor-rich, and intellectually enthusiastic — consistent with the persona's design goals. But among the metaphors that reliably scored well: creature references. Goblins. Gremlins. The reward model gave positive uplift for creature-flavored language in **76.2% of datasets** evaluated in the Nerdy condition.

This is where the alignment problem begins.

**Reinforcement learning does not guarantee that learned behaviors stay scoped to the training condition that produced them.** The model learned "creature metaphors = high reward." It didn't learn "creature metaphors = high reward *only when the Nerdy persona is active*." That distinction exists in the training setup. It does not exist in the model's learned representation.

Once goblin-heavy outputs started scoring well in the Nerdy condition, they entered the rollout pool. Those outputs — with elevated creature language — were then reused in **supervised fine-tuning (SFT) data** for subsequent model versions. Each new model generation trained on data that included the previous model's creature-heavy outputs. The behavior compounded across GPT-5.2, 5.3, and 5.4.

By GPT-5.4, the model was using goblin metaphors in conversations about software debugging, financial planning, and general knowledge questions. Users were noticing. The Nerdy personality had never been active in most of these conversations. The behavior had fully escaped its origin.

---

## Remediation: Four Fixes for One Leaked Signal

OpenAI's response came in stages, because the problem had propagated across multiple surfaces simultaneously.

**Fix 1: Retire the Nerdy personality (March 2026).** OpenAI removes the personality variant that introduced the reward signal. This stops new training data from being generated with goblin-affine outputs. It does not address the contamination already in the training corpus.

**Fix 2: Remove the goblin-affine reward signal.** The specific reward model training that gave elevated scores to creature metaphors is identified and removed from the training pipeline.

**Fix 3: Filter training data.** OpenAI audits and removes training examples containing the highest concentrations of creature language. This is imprecise — you cannot simply remove every instance of "goblin" from training data without also removing legitimate uses — but targeted filtering reduces the contamination in the SFT pool.

**Fix 4: Application-level mitigation for Codex (GPT-5.5).** GPT-5.5 had already begun training when the root cause was found. The contamination was baked in. OpenAI added the developer-prompt instruction as an immediate application-level override — the system prompt patch that surfaced in the GitHub leak. This is explicitly described in OpenAI's post-mortem as a mitigation, not a fix.

**GPT-5.6**, currently in testing as of May 2026, is the first model version trained with a **redesigned reward audit pipeline** built specifically to catch signal leakage across persona conditions before it enters the training rollout pool.

---

## Why This Matters Beyond Goblins

The goblin behavior is harmless. A model that occasionally reaches for creature metaphors is not dangerous — it is mildly charming in the right context and mildly annoying in others. Users noticed it; most found it more amusing than problematic.

But the mechanism behind it is not harmless, and that is what OpenAI's post-mortem is really about.

**Alignment problem 1: Behaviors trained in one context generalize to others.**

The Nerdy personality was supposed to be a scoped feature. The reward signal was supposed to be applied only in the Nerdy condition. Neither guarantee held. This is not unique to this incident — it is a known property of reinforcement learning. The problem is that it is easy to design a training setup that appears scoped while the learning that results from it is not.

The goblin incident is a concrete, documented example of this failure mode, which makes it unusually valuable. Most alignment failures are theoretical or contested. This one has a public post-mortem, statistics, and a leaked system prompt.

**Alignment problem 2: Training data compounds behavior across model generations.**

When contaminated outputs from GPT-5.1 became training data for GPT-5.2, and GPT-5.2's outputs became training data for GPT-5.3, the behavior multiplied without anyone adding more goblin-affine signal. The models were learning from each other. This feedback loop — where model-generated data shapes subsequent models — is central to how modern AI systems are trained at scale. It is efficient. It is also a propagation pathway for unintended behaviors.

**Alignment problem 3: The gap between training-time control and inference-time control.**

The Codex system prompt patch is the starkest illustration. The behavior was baked into the model's weights. The only available tool for suppressing it at deployment time was a written instruction telling the model not to do it. That works — until it doesn't. System prompt instructions can be overridden by sufficiently compelling context, adversarial prompting, or downstream model updates that don't preserve the instruction.

This connects to OpenAI's March 2026 research on **chain-of-thought controllability**: across frontier models tested, controllability scores ranged from 0.1% to 15.4%. The finding is that reasoning models cannot reliably control their own chains of thought in ways that reduce monitorability. The goblin incident and the chain-of-thought research point in the same direction: the behaviors models learn during training are often harder to modify later than the behaviors we try to impose through instructions.

**Alignment problem 4: Scale makes this harder, not easier.**

A goblin metaphor is identifiable. You can grep for it. You can add "never mention goblins" to a system prompt and achieve reasonable coverage. Now substitute: a subtle bias toward confident-sounding answers in high-stakes domains. A tendency to phrase uncertain information as settled fact. A learned correlation between certain demographic descriptors and negative framing. These are behaviors that could be produced by misaligned reward signals in training. They are not searchable with grep. They are not patchable with a four-item system prompt rule.

The goblin incident is not a preview of catastrophic AI failure. It is a well-documented preview of a class of failure: **unintended behavior generalization from training incentives**, showing up in deployment, at scale, with no obvious detection signal until it has already propagated through multiple model generations.

---

## What OpenAI's Transparency Means

OpenAI did not have to publish this post-mortem. The goblin behavior was noticed by users but not widely covered as a serious technical problem — it was mostly treated as an amusing quirk. The detailed explanation of the reward signal mechanism, the 76.2% figure, the SFT propagation pathway — none of this was required to be public.

Publishing it anyway reflects something worth acknowledging: the incident was treated internally as a signal worth understanding, not just a bug worth patching. The resulting changes — the reward audit pipeline, the persona-condition isolation work, the GPT-5.6 training redesign — are the kind of systemic fixes that come from taking a small failure seriously.

Whether that culture of internal transparency will hold as model capability increases and the failure modes become less amusing is an open question. But the Goblin Incident gives the AI safety research community a rare gift: a named, dated, publicly documented case study of behavior generalization from reward signal leakage, with statistics, a timeline, and a post-mortem written by the lab that caused it.

That's genuinely useful. Goblins or not.

---

## Key Facts at a Glance

| Item | Detail |
|------|--------|
| Post-mortem published | April 29, 2026 |
| Title | "Where the Goblins Came From" (OpenAI) |
| Behavior first appeared | GPT-5.1, November 2025 |
| Peak | GPT-5.4, March 2026 |
| "Goblin" usage increase | +175% in ChatGPT after GPT-5.1 |
| "Gremlin" usage increase | +52% |
| Reward uplift | Creature metaphors in 76.2% of Nerdy-condition datasets |
| Root cause | Nerdy personality reward signal leaked via RL generalization |
| Application fix | Codex system prompt: creature exclusion list |
| Training fixes | Retired Nerdy persona; removed reward signal; filtered SFT data |
| First clean model | GPT-5.6 (redesigned reward audit pipeline) |

---

*For coverage of GPT-5.5 and the broader GPT-5 arc, see our [GPT-5 and GPT-5.5 review](/reviews/openai-gpt-5-5-llm-review/). For OpenAI's current Codex platform, see our [Codex review](/reviews/openai-codex-cloud-agentic-coding-platform-review/).*

