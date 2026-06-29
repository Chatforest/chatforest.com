# Every Frontier Model Fails Most SRE Incidents: What ITBench-AA Means for Enterprise Agent Builders

> IBM Research and Artificial Analysis launched ITBench-AA, the first benchmark for agentic enterprise IT tasks, starting with Kubernetes SRE incident diagnosis. Every frontier model scores below 50%. Claude Opus 4.7 leads at 47% for $5.38/task; Gemma 4 31B hits 37% for $0.14/task. More investigation turns do not improve accuracy.


IBM Research and Artificial Analysis jointly launched **ITBench-AA**, the first independent benchmark for agentic enterprise IT tasks. The headline result is blunt: every tested frontier model fails the majority of Kubernetes site reliability engineering incidents. No model clears 50%. The benchmark is live, open-source, and expanding to Financial Operations and CISO tasks next.

This is a research-based summary. We have not executed any of the tools or infrastructure described here.

---

## What ITBench-AA measures

Most AI benchmarks test knowledge retrieval or code generation in isolated, well-framed problems. Enterprise IT is not that. A production Kubernetes cluster under incident is a live distributed system with incomplete signals, multiple plausible failure causes, and noise. The engineer's job — or the agent's job — is to process heterogeneous telemetry data and identify the minimum set of root-cause entities with no false positives.

ITBench-AA starts with 59 SRE tasks drawn from that scenario. Each task presents an agent with:

- **Kubernetes alerts and events**
- **Distributed traces and metrics**
- **Application logs**
- **Service topology maps**

The agent has shell access to an offline snapshot of the environment. It can issue commands, read files, and inspect manifests. The task ends when the agent submits a structured JSON response naming the root-cause Kubernetes entities.

**Scoring is strict.** If the agent misses any ground-truth root cause, the score is zero for that task. If it identifies all root causes, the score is precision — true positives over all submitted entities. Partial credit requires completeness first. The headline score is the average across 59 tasks with 3 repeats each.

The task set is split: 40 public tasks are available for inspection on HuggingFace; 19 are held-out for leaderboard evaluation. This prevents prompt engineering against the benchmark itself.

---

## Leaderboard

| Model | Score | Avg Turns | Cost/Task |
|---|---|---|---|
| Claude Opus 4.7 (Adaptive Reasoning, Max Effort) | **47%** | — | $5.38 |
| GPT-5.5 (xhigh) | **46%** | 31 | — |
| Qwen 3.7 Max | **42%** | — | — |
| GLM-5.1 (Reasoning) | 40% | — | $1.23 |
| Gemini 3.5 Flash (high) | 40% | — | $1.70 |
| DeepSeek V4 Pro (Reasoning, Max Effort) | 38% | — | — |
| Gemma 4 31B (Reasoning) | 37% | 58 | $0.14 |
| Gemini 3.1 Pro Preview | 30% | 83 | $2.23 |

Two things stand out immediately. First, the spread between best and worst proprietary models is 17 percentage points, but the best model only reaches 47%. This is not a saturated benchmark where all frontier models score in the high 90s and the difference comes down to rounding. There is genuine variation, and there is genuine room to improve.

Second, Gemma 4 31B scores 37% at $0.14 per task while Claude Opus 4.7 scores 47% at $5.38 per task. That is a 36× cost difference for a 10-point accuracy gap. Whether that trade-off makes sense depends on your deployment context.

---

## The turns finding

Gemini 3.1 Pro Preview averages **83 investigation turns** and scores **30%**. GPT-5.5 averages **31 turns** and scores **46%**.

More turns do not produce better diagnoses. The pattern the benchmark team observed: models that over-investigate surface upstream error signals and co-occurring anomalies, treating correlated events as separate root causes and submitting them as candidates. This inflates false positives and drags precision down. The model that issues 31 focused turns and stops is more accurate than the one that issues 83 exploratory turns and accumulates noise.

This is a significant finding for builders designing agent harnesses. Imposing a turn budget — or training agents to converge and submit rather than continue searching — may improve outcomes more than upgrading the underlying model.

The benchmark caps agents at 100 turns. The models that use that budget fully tend to underperform.

---

## What the results mean for builders deploying SRE agents

**No model is ready to run autonomous SRE.** A 47% task completion rate means the best available model fails more than half of incidents when acting alone. Production SRE requires a human-in-the-loop or a tiered architecture where the agent handles structured triage and a human validates the root-cause claim before action.

**Triage and initial scoping are viable.** The benchmark tasks require full root-cause identification with no false positives. A model can still provide high value by narrowing the search space — surfacing the relevant subsystems, filtering out noise alerts, and presenting a short candidate list for human review — even if it cannot consistently nail the final answer autonomously.

**Turn discipline matters more than model size.** Design your agent harness to converge. Give the agent explicit stopping criteria and penalize or limit continued investigation after a confidence threshold is reached. Based on the benchmark data, a focused shorter-turn agent outperforms a longer-exploring one.

**Cost-performance options exist.** If you are building an internal SRE tool and cost matters, Gemma 4 31B at $0.14/task with 37% accuracy is worth evaluating in your specific incident mix before defaulting to Opus 4.7 at $5.38/task. Run both against your own incident library and measure on the task types you actually face, not the leaderboard average.

**The benchmark is expanding.** Financial Operations and CISO task tracks are next. If your agents touch either of those domains, the methodology is worth understanding now: the same strict scoring (miss any root cause = 0) will apply, and the current results suggest those tracks will also show sub-50% performance across frontier models.

---

## How to access and run the benchmark

- **Live leaderboard**: [artificialanalysis.ai/evaluations/itbench-aa](https://artificialanalysis.ai/evaluations/itbench-aa)
- **HuggingFace dataset (public tasks)**: [huggingface.co/datasets/ArtificialAnalysis/ITBench-AA](https://huggingface.co/datasets/ArtificialAnalysis/ITBench-AA/tree/main/sre)
- **GitHub (open-source harness)**: [github.com/itbench-hub/ITBench](https://github.com/itbench-hub/ITBench)
- **Research paper**: arxiv.org/abs/2502.05352
- **Lightweight version**: [huggingface.co/datasets/ibm-research/ITBench-Lite](https://huggingface.co/datasets/ibm-research/ITBench-Lite)

The Stirrup framework used as the reference harness is open-source. The benchmark is designed for apples-to-apples comparisons: sandboxed environment, 100-turn cap, 3 repeats per task, consistent tooling across models.

---

## The broader context

ITBench-AA fills a gap that has been uncomfortable for enterprise AI teams: there was no credible, independent, third-party evaluation of how AI agents actually perform on the messy, multi-signal diagnostic problems that characterize real IT operations. Synthetic benchmarks and vendor-reported demos do not capture the false-positive problem, the turn-efficiency problem, or the cost-performance trade-offs that matter in practice.

The results are sobering but useful. They set a calibrated baseline. They show that the problem is genuinely hard and that current agents need structural support — human review, turn constraints, escalation paths — to be production-deployable. They also show that open-weight models are competitive enough on cost-performance to warrant serious evaluation alongside proprietary options.

The next question the benchmark will answer: does the same pattern hold for FinOps and CISO tasks, or does model performance vary significantly by IT domain?

