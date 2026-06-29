# AReaL-boba-2: Ant Research's Async RL Coding Models Are Leading the Leaderboard (Builder Guide)

> inclusionAI (Ant Research's RL Lab) released AReaL-boba-2, a family of open-weight coding models (8B, 14B, 32B) trained with asynchronous reinforcement learning that achieves 2.77x speedup over standard RL. The 14B hits 69.1 on LiveCodeBench v5. Apache 2.0. Here is what builders need to evaluate and deploy it.


A model called "Boba" is currently sitting at the top of the AI coding arena leaderboard — above Claude Opus 4.6, above GPT-5.5 Pro. The company behind it lists as "stealth." What is actually verifiable: **AReaL-boba-2**, a family of open-weight coding models from **inclusionAI** (Ant Research's reinforcement learning lab), is live on HuggingFace under Apache 2.0, and the engineering behind it is worth understanding.

This guide covers what the models are, how the async RL training system works, benchmark numbers, deployment options, and what builders should actually do with them.

---

## What inclusionAI Is

inclusionAI is the RL research arm of Ant Group, Alibaba's fintech affiliate. They previously released AReaL, an open and reproducible framework for large-scale RL training of LLMs — all code, datasets, and training recipes public. AReaL-boba-2 is their second major model family release from that framework, pivoting from the math-focused boba-1 to coding-first.

The research paper is available at [arXiv:2505.24298](https://arxiv.org/abs/2505.24298).

---

## The Model Family

All AReaL-boba-2 models use **Qwen3** as the base (Alibaba's open-weight frontier series) and apply async RL post-training specialized for coding tasks.

| Model | Params | License | Weights |
|---|---|---|---|
| AReaL-boba-2-8B | 8B | Apache 2.0 | Public (8B-Open) |
| AReaL-boba-2-14B | 14B | Apache 2.0 | Public (14B-Open) |
| AReaL-boba-2-32B | 32B | Apache 2.0 | Public |

The `-Open` suffix variants (8B-Open, 14B-Open) are fully open-weight releases — weights downloadable directly from HuggingFace. The non-Open 8B and 14B may use a small amount of internal training data on top of the released recipe.

HuggingFace collection: `inclusionAI/areal-boba-2-683f0e819ccb7bb2e1b2f2d5`

---

## The Core Technical Story: boba² Async RL

Standard RL training for LLMs uses a synchronous pipeline: generate rollouts, wait, train, wait, repeat. The generation and training steps block each other. At scale across hundreds of GPUs, idle time compounds.

The boba² system (pronounced "double boba") decouples these stages completely:

- **Decoupled generation and training pipeline** — both stages run simultaneously, not sequentially
- **Decoupled PPO loss** — a system-algorithm co-design change that makes asynchronous updates mathematically sound
- **Result: 2.77x throughput improvement** with no benchmark performance drop

The generation backend is SGLang v0.4.0 (upgraded from vLLM 0.6.3), which leverages radix attention to improve throughput when sampling multiple responses from the same prompt — which RL training requires heavily.

For data transfer at scale, the system uses NCCL GPU-Direct RDMA over InfiniBand/RoCE, keeping data movement overhead under 3 seconds even at 1,000 GPUs.

Multi-turn agentic RL training is also present as an experimental feature — the system can train models on multi-step tool-using trajectories, not just single-turn code generation.

---

## Benchmark Performance

### Coding Benchmarks

The 14B model result is the most documented:

| Benchmark | AReaL-boba-2-14B | Notes |
|---|---|---|
| LiveCodeBench v5 (LCB-v5) | **69.1** | SOTA in the 14B weight class at release |
| Codeforces | SOTA in class | Competitive programming problems |
| CodeContests | SOTA in class | DeepMind competition dataset |

For context: the 14B model sits in territory that previously required 32B+ models. The evaluation protocol uses temperature 1.0, 32 samples per problem, max 32,768 generated tokens.

The 32B model's specific LCB-v5 score is not publicly disclosed in the model card — the card describes it as competitive with models like DeepSeek-R1 and OpenAI o3-mini in its weight class.

### The "Boba by stealth" Leaderboard Position

The AI coding arena at llm-stats.com currently shows "Boba by stealth" at an Elo-style score of 1216, ahead of Claude Opus 4.6 (1157) and Claude Sonnet 4.6 (1122), based on 1,600+ blind head-to-head votes. The "stealth" label reflects that inclusionAI does not have a high-profile public brand. Whether the arena entry is specifically the 32B variant or a larger internal model is not publicly confirmed.

What is confirmed: the open-weight variants are legitimate and the benchmark numbers above for 14B are documented.

---

## Deployment

### Hardware Requirements

| Model | FP16 VRAM | Quantized (Q4) |
|---|---|---|
| 8B | ~16 GB | ~6 GB (runs on RTX 3080) |
| 14B | ~28 GB | ~10 GB (runs on RTX 3090) |
| 32B | ~64 GB | ~22 GB (runs on A10G or 2× consumer GPU) |

### vLLM (recommended for API serving)

```bash
pip install vllm
vllm serve "inclusionAI/AReaL-boba-2-14B-Open" --port 8000
```

The server exposes an OpenAI-compatible API at `http://localhost:8000/v1/`.

### SGLang (recommended for high-throughput RL or multi-sample workloads)

```bash
pip install sglang
python3 -m sglang.launch_server \
    --model-path "inclusionAI/AReaL-boba-2-14B-Open" \
    --host 0.0.0.0 \
    --port 30000
```

SGLang's radix attention is particularly effective when you need to sample multiple completions from the same prompt prefix — common in agent loop patterns that retry or score multiple candidate solutions.

### Transformers (quickstart)

```python
from transformers import pipeline

pipe = pipeline(
    "text-generation",
    model="inclusionAI/AReaL-boba-2-8B-Open",
    device_map="auto"
)

result = pipe(
    "Write a Python function that finds all prime numbers up to n using the Sieve of Eratosthenes.",
    max_new_tokens=2048,
    temperature=1.0,
    do_sample=True
)
print(result[0]["generated_text"])
```

### Ollama / llama.cpp

Quantized GGUF versions are available on HuggingFace. Pull via Ollama once a community GGUF is published, or convert weights with `llama.cpp/convert_hf_to_gguf.py`.

```bash
docker model run hf.co/inclusionAI/AReaL-boba-2-32B
```

---

## Evaluation Against Your Own Codebase

The team released the full evaluation suite alongside the model:

```bash
git clone https://github.com/inclusionAI/AReaL
cd AReaL/evaluation

python eval_and_aggregate.py \
  --model_path inclusionAI/AReaL-boba-2-14B-Open \
  --output_path ./results \
  --data_names aime24,aime25,codeforces,lcb_v5 \
  --prompt_type qwen3-think-pure \
  --temperature 1.0 \
  --max_gen_tokens 32768
```

For your own code evaluation tasks, swap `--data_names` for a custom dataset that mirrors your actual production problem distribution.

---

## Builder Patterns

### Pattern 1: Local coding agent on single A10G

The 14B-Open model fits in 28GB FP16 — within reach of a single A10G instance on most cloud providers. Serve via vLLM and route coding tasks from your agent orchestrator to it instead of a frontier API:

```python
import openai

client = openai.OpenAI(
    base_url="http://localhost:8000/v1",
    api_key="not-needed"
)

response = client.chat.completions.create(
    model="inclusionAI/AReaL-boba-2-14B-Open",
    messages=[
        {"role": "user", "content": "Refactor this function to eliminate the O(n²) loop:\n\n" + your_code}
    ],
    max_tokens=4096,
    temperature=0.7
)
```

At an A10G spot price of roughly $0.30-0.50/hour, the effective cost per query is sub-cent for most coding tasks — competitive with Claude Sonnet API pricing for high-volume workloads.

### Pattern 2: Competitive programming / algorithmic challenge agent

AReaL-boba-2 was trained specifically on Codeforces and CodeContests data. If you are building a tool that solves or generates competitive-programming-style algorithmic problems (interview prep tools, code challenge platforms, CS tutoring), this model has domain-specific RL training that frontier general models lack.

```python
SYSTEM = """You are an expert competitive programmer. 
Think step by step. Use <think> tags for your reasoning. 
Output only the final solution in the code block."""

# Sample multiple solutions and pick the one that passes test cases
responses = [
    client.chat.completions.create(
        model="inclusionAI/AReaL-boba-2-14B-Open",
        messages=[{"role": "system", "content": SYSTEM},
                  {"role": "user", "content": problem_statement}],
        temperature=1.0,
        max_tokens=8192
    )
    for _ in range(8)  # sample 8, score against test cases
]
```

This "sample then verify" pattern mirrors exactly how the model was trained — high-temperature sampling followed by outcome-based scoring.

### Pattern 3: Fine-tune on your own code data (Apache 2.0 permits this)

The AReaL training framework is fully open. You can run RL fine-tuning on your own proprietary codebase:

1. Collect your internal code generation tasks (function stubs + expected behavior)
2. Write a reward function that runs your test suite and returns +1 / -1
3. Train with the AReaL framework starting from AReaL-boba-2-8B-Open weights

The released `AReaL-boba-2-RL-Code` dataset (on HuggingFace) shows the expected data format. Apache 2.0 allows derivative model use in closed commercial products.

---

## What This Does Not Cover

- **SWE-bench Verified**: No scores published for AReaL-boba-2. The model excels at algorithmic coding (LCB-v5, Codeforces) but SWE-bench requires repository-level multi-file context, which is a different skill. Evaluate before assuming parity with Claude Opus 4.8's 88.7%.
- **Long-context file tasks**: The context window is 32,768 tokens maximum — fine for most function-level tasks, but not repository-scale analysis. For that, continue using GLM-5.2 or Gemini 3.1 Pro.
- **Multi-turn agentic RL**: The framework supports it experimentally, but the released model weights were not trained with it. This is a future capability, not a current one.

---

## What to Watch

- **32B benchmark disclosure**: Exact LCB-v5 and Codeforces scores for the 32B model not yet published. When released, this will clarify how close the open-weight model is to the "Boba by stealth" leaderboard entry.
- **inclusionAI public positioning**: The team is associated with Ant Research but has not made a branded announcement. A public launch or paper presentation could raise the profile of these models significantly.
- **Multi-turn agentic RL stabilization**: If the experimental multi-turn training matures, AReaL-boba-2 (or a successor) could become a strong base for tool-using coding agents trained on your specific workflow data.

---

## The Bottom Line

AReaL-boba-2 is the most capable open-weight coding model family available as of June 2026 in the sub-32B class. The 14B-Open model achieves 69.1 on LiveCodeBench v5 under Apache 2.0, fits on a single A10G, and can be fine-tuned with the fully open training framework. For builders running high-volume coding tasks or evaluating self-hosted alternatives to frontier APIs, it belongs in your evaluation set.

