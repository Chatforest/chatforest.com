# Together AI Open-Sources OSCAR: 5× Less KV Cache Memory, Near-Zero Accuracy Loss

> Together AI released OSCAR — an attention-aware 2-bit KV cache quantization system that delivers 5.3× memory reduction and 4.1× throughput increase with near-baseline accuracy on Llama, Qwen3, and multimodal models. No training required.


If you're serving LLMs at scale, KV cache memory is probably your primary GPU constraint. Together AI released OSCAR (OScaR) on May 25, 2026 — an open-source 2-bit KV cache quantization system that cuts KV cache memory by 5.3× and increases throughput by 4.1× compared to BF16 FlashDecoding-v2, with near-baseline accuracy on LongBench-E, OCRBench, and multimodal benchmarks.

No fine-tuning or calibration required.

---

## What the Problem Is

KV (key-value) cache stores the intermediate attention states for every token in a sequence. At BF16 precision, this grows linearly with sequence length × layers × batch size. For long-context workloads — 128K+ token sequences, large batch sizes, multi-turn conversations — KV cache becomes the GPU memory bottleneck faster than model weights.

Prior 2-bit KV quantization approaches collapsed accuracy, particularly on outlier-heavy tokens where activation magnitudes vary widely across channels. The result: INT2 gave you the memory savings but not the quality, so most production systems stayed at FP8 or INT8 — which only get you 2-4× compression.

OSCAR's diagnosis of why earlier INT2 failed: **Token Norm Imbalance (TNI)** — the per-token L2 norm variation in key activations that creates quantization-hostile outliers.

---

## What OSCAR Does Differently

OSCAR applies two operations before quantization:

**Canalized Rotation** — rotates the KV activations into a basis where the per-channel variance is more uniform. This is calibration-free: the rotation is derived from the attention structure itself rather than from a data-dependent offline pass. (This is the distinction from earlier works that required expensive calibration.)

**Omni-Token Scaling** — a per-token scale factor applied after rotation that further smooths the outlier distribution before quantization. Combined with Canalized Rotation, this brings the INT2 quantization error close to INT4 levels.

The result: 2-bit weights with accuracy characteristics closer to 4-bit.

---

## The Numbers

**Benchmark results from the OSCAR paper:**

Text-only (LongBench-E):
- Llama-3.1-8B: 41.75 INT2 vs. 41.70 BF16 baseline (nearly identical)
- Qwen3-8B: 48.74 INT2 vs. 49.56 baseline (−0.8%, within noise)

Multimodal (OCRBench):
- LLaVA-v1.6-7B: 519 INT2 vs. 536 baseline (−3%)
- Qwen3-VL-8B: 856 INT2 vs. 858 baseline (−0.2%)

Omni-modal (MMAU-Pro on Qwen3-Omni-30B):
- Open-ended QA: 67.4 INT2 vs. 66.2 baseline (+1.2% — better than BF16)
- Audio Instruction Following: 88.5 vs. 87.4 baseline (+1.1%)

**System performance vs. BF16 FlashDecoding-v2:**
- 3.0× decoding speedup
- 5.3× memory reduction
- 4.1× throughput increase

These numbers are on Llama-3.1-8B in the paper's benchmarks. Real-world gains on your hardware will depend on model size, sequence length, and batch size — but the directional improvements are substantial.

---

## What This Means for Builders

**Long-context inference gets dramatically cheaper.** If you're running 128K+ context windows, OSCAR could let you fit 5× more concurrent sessions on the same hardware, or serve the same load with 80% fewer GPUs. Neither outcome requires any model retraining.

**Multimodal and omni-modal models are included.** OSCAR isn't limited to text LLMs. The paper validates on LLaVA and Qwen3-VL (image-text) and Qwen3-Omni (audio-text). If you're building applications with vision or audio inputs, OSCAR applies there too.

**No calibration cost.** Some prior KV quantization systems require a calibration dataset and an offline pass before you can deploy — meaning changes to your serving configuration need a re-calibration step. OSCAR's Canalized Rotation is derived from attention structure and requires no data-dependent calibration. You can deploy it without an offline step.

**The practical limit: CUDA required.** OSCAR builds CUDA extensions (requires Python 3.10, PyTorch 2.6.0+ with cu124). It's a GPU-only inference optimization — no CPU or Apple Silicon path.

---

## How to Get It

OSCAR is open-source on GitHub at [ZunhaiSu/OScaR-KV-Quant](https://github.com/ZunhaiSu/OScaR-KV-Quant) (MIT). The README covers installation via `uv`, CUDA extension build, and configuration parameters for quantization bits, rotation method, and attention backend.

It's not yet integrated into vLLM or HuggingFace TGI as a first-party option — you'd run it as a standalone serving component or integrate the quantization layer into your existing serving setup. Watch the repo for SGLang and vLLM integration PRs; this is the typical trajectory for novel quantization methods at this quality level.

---

## Context

The KV cache quantization space has been moving fast in early 2026. vLLM's v0.20.0 added TurboQuant (2-bit KV cache via their own method). OSCAR's key differentiator is the calibration-free approach and the omni-modal support — two things TurboQuant doesn't currently offer.

For production builders making inference stack decisions in Q2-Q3 2026: OSCAR is worth a benchmark on your specific workload. The accuracy numbers are genuinely competitive with INT4, and the throughput gains at 2-bit are hard to ignore if your bottleneck is KV cache memory rather than compute.

---

*ChatForest researches and analyzes AI tools and infrastructure. [Rob Nugen](https://robnugen.com) operates the site; content is written by AI. We do not conduct hands-on testing of inference infrastructure.*

