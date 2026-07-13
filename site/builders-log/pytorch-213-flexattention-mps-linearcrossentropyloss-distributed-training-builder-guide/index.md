# PyTorch 2.13 Ships FlexAttention on Apple Silicon and a 4x Memory Win for LLM Training — What Builders Should Apply First

> PyTorch 2.13 (3,328 commits, 526 contributors) landed July 8 with five features worth your attention: FlexAttention on MPS with 12.3x sparse-attention speedup, a fused LinearCrossEntropyLoss that cuts peak GPU memory 4x for large-vocab training, the CuTeDSL backend as a Triton alternative, FSDP2 communication overlap, and native safetensors loading. Here's what each one means and what to reach for first.


PyTorch 2.13 shipped July 8, 2026, with 3,328 commits from 526 contributors. It is a training-heavy release — the two headlining features (FlexAttention on Apple Silicon and LinearCrossEntropyLoss) are both aimed directly at LLM workloads — but there is also meaningful progress in the distributed training stack, kernel generation, and model loading ergonomics. Below is a technical summary of the five changes most likely to matter to builders working on ML systems today.

---

## FlexAttention Lands on Apple Silicon (MPS)

FlexAttention — PyTorch's API for writing custom attention patterns in Python that compile down to efficient kernels — now runs on Apple Silicon via Metal Performance Shaders. The implementation uses hand-written Metal kernels for both the prefill and decode paths, and supports GQA (Grouped Query Attention) and captured buffers.

The speedup numbers are context-dependent:

| Pattern | Sequence Length | Speedup vs SDPA |
|---|---|---|
| Sliding window (256-element, 0.8% density) | 32,768 | **~12.3x** |
| Sliding window (64-element) | 8,192 | **~4.15x** |
| Dense full attention | any | SDPA still wins |

The key phrase in those numbers is "density." FlexAttention on MPS is fast when the attention mask is sparse — sliding window attention, document masking, ALiBi-style locality patterns. Dense full attention still runs faster through SDPA. If your model uses a custom sparse attention pattern and you're running or prototyping on an M-series Mac, this matters immediately.

The API is straightforward: write a Python function that specifies which attention pairs to compute, pass it to `flex_attention`, and PyTorch compiles the Metal kernel. The interface is marked API Unstable in 2.13, so treat the API surface as subject to change in minor releases.

CUDA users also get a related improvement: a **deterministic backward pass** for FlexAttention. The previous implementation used atomic operations during backpropagation, producing results that could vary run-to-run at high precision. The new path pre-computes write ordering and replaces atomics with a deterministic sequence. The overhead is approximately 0.2% at a 32,768-token sequence length. Enable it with `torch.use_deterministic_algorithms(True)`.

---

## LinearCrossEntropyLoss: 4x Peak Memory Reduction for Large-Vocab Training

This is the most immediately deployable change in 2.13 for anyone training or fine-tuning a language model.

The problem it solves: during training, the standard pattern is to project hidden states through a final linear layer (shape: `[batch × seq_len, hidden_dim]` → `[batch × seq_len, vocab_size]`) and then pass the result to `CrossEntropyLoss`. For a 100,000-token vocabulary, this materializes a logit matrix that can consume tens of gigabytes of GPU memory — before gradients, before activations, before optimizer state. On a single 80GB A100, that logit matrix alone can saturate available memory at moderate batch sizes.

PyTorch 2.13 ships `nn.LinearCrossEntropyLoss`, a fused module that combines the projection and the loss computation. Instead of materializing the full logit matrix, it processes the vocabulary dimension in chunks — computing the loss against each chunk and accumulating the result without ever holding the full matrix in GPU memory simultaneously.

The reported reduction is **up to ~4x peak GPU memory** for models with vocabularies of 100,000 tokens or more. The fused path maintains numerical equivalence with the unfused baseline.

The API is a drop-in replacement:

```python
# Before
linear = nn.Linear(hidden_dim, vocab_size)
loss_fn = nn.CrossEntropyLoss()
loss = loss_fn(linear(x), labels)

# After
loss_fn = nn.LinearCrossEntropyLoss(hidden_dim, vocab_size)
loss = loss_fn(x, labels)
```

Additional features: label smoothing, weight tying (for models that share embedding and output projection weights), z-loss regularization (Mesh TensorFlow-style auxiliary loss for training stability), and integration with `torch.compile` for further kernel fusion.

If you are training a model with a large vocabulary — any multilingual model, code model with a broad token set, or model with a custom tokenizer that reaches into six figures — this is worth switching to before your next training run.

---

## CuTeDSL Backend for Inductor (Alternative to Triton)

PyTorch's compilation stack (Inductor) gets a new kernel generation backend in 2.13: CuTeDSL, a Python-native domain-specific language built on NVIDIA's CuTe (CUDA Templates) library.

For most builders, this is a background improvement. Inductor previously generated CUDA kernels primarily through Triton. Triton produces good kernels for most operations but is a separate compilation system with its own overhead, and the quality of generated matrix multiply code varies. CuTeDSL is an alternative path that generates GEMM and RMSNorm kernels using NVIDIA's own template library — potentially higher-quality matrix multiply code without Triton as an intermediary.

A practical change accompanies the new backend: kernel compilation has been moved to a subprocess pool, which removes a Python GIL bottleneck during compilation. For workloads that trigger many kernel compilations (large models, many distinct shapes), this can reduce cold-start compilation time.

CuTeDSL is available alongside Triton — Inductor selects between them based on operation type. No API changes are required to benefit from it.

---

## FSDP2 Communication Overlap

Fully Sharded Data Parallel (FSDP2) gets a single-line optimization worth enabling: a separate NCCL communicator for reduce-scatter operations.

In the current default configuration, FSDP2 uses one NCCL communicator for both all-gather and reduce-scatter collectives. NCCL serializes operations on a single communicator, which means forward-pass all-gathers and backward-pass reduce-scatters run sequentially rather than overlapping.

The new flag adds a dedicated communicator:

```python
FSDPModule.set_separate_reduce_scatter_group(enable=True)
```

With this enabled, all-gather and reduce-scatter can progress concurrently on separate NCCL streams. The expected result is increased training throughput for distributed workloads — the backward collective can begin while forward collectives are still in flight. No model code changes are required.

If you are running multi-node FSDP2 training, this is worth enabling and measuring against your current baseline.

---

## Native Safetensors Loading

`torch.load()` now natively detects and loads `.safetensors` files without requiring a separate library import:

```python
model_state = torch.load("model.safetensors")
```

Previously, loading a safetensors checkpoint required either the `safetensors` Python package or a manual format conversion. The native support auto-detects the file format and enables memory-mapped loading by default.

The security benefit is meaningful: safetensors format does not execute arbitrary Python code during loading (a known risk of the pickle-based `.pt` format). Memory-mapped loading also reduces peak RAM usage during model loading, which matters when loading large checkpoint files on machines with limited system memory.

For builders distributing model checkpoints or pulling from Hugging Face Hub, you can now standardize on `.safetensors` without an additional dependency in your inference code.

---

## Other Changes Worth Noting

**Python 3.15 support.** Wheels are available for Linux x86_64 and aarch64 with CPU, CUDA 13.0, ROCm 7.2, and XPU backends. Experimental free-threaded (no-GIL) 3.15t builds are also available. Note: `torch.compile` does not yet support Python 3.15 — if you rely on compilation, stay on 3.12 or 3.13 for now.

**Intel GPU telemetry APIs.** New `torch.xpu` device monitoring functions — power draw, temperature, memory utilization, clock rate — for workloads running on Intel GPU hardware.

**torchcomms backend.** A new communications layer alternative to c10d's `ProcessGroup` with improved fault tolerance, partial-group recovery, and structured logging for debugging distributed collective failures.

**Collective API renames.** `all_gather_into_tensor` is now `all_gather_single`; `reduce_scatter_tensor` is now `reduce_scatter_single`. Old names remain as deprecated wrappers.

---

## What to Apply First

The decision depends on your workload:

**If you are training or fine-tuning a language model with a large vocabulary (100K+ tokens):** Switch to `nn.LinearCrossEntropyLoss`. It is a drop-in replacement, maintains numerical equivalence, and the 4x memory reduction is effectively free — you gain either headroom to increase batch size, or the ability to run a configuration that was previously OOM.

**If you are running on Apple Silicon for development or inference:** Enable FlexAttention on MPS for any workload using sparse attention patterns (sliding window, document masking, local attention). The 12x speedup on sparse patterns is substantial. For dense attention, leave SDPA in place.

**If you are running FSDP2 across multiple nodes:** Enable `set_separate_reduce_scatter_group(enable=True)` and benchmark. This is a one-line change with no model code impact and a meaningful expected throughput improvement.

**If you distribute or load model checkpoints:** Adopt `.safetensors` format. The native loading support in 2.13 removes the last friction point.

PyTorch 2.13 is not a release that rewrites how you think about the framework — it is a release that makes specific expensive operations substantially cheaper. The LinearCrossEntropyLoss alone makes this a worthwhile upgrade for anyone in the LLM training space.

The full release blog is at [pytorch.org/blog/pytorch-2-13-release-blog](https://pytorch.org/blog/pytorch-2-13-release-blog/). A live Q&A with contributors is scheduled for July 22, 2026 at 11 a.m. PT.

