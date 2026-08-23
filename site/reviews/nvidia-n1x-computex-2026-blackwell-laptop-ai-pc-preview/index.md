# NVIDIA N1X Preview: The First Blackwell Laptop Chip and What It Means for Local AI

> NVIDIA's N1X SoC — officially launched as RTX Spark at Computex 2026 — combines a 20-core Grace CPU with a Blackwell-class GPU and full CUDA support. What AI developers need to know, including what was confirmed at Jensen Huang's June 1 keynote.


**Update (2026-08-23):** At the June 1, 2026 keynote this article previewed, NVIDIA officially launched the chip as **RTX Spark** — "N1X" was the pre-announcement codename and was never adopted as the commercial name. The confirmed specs matched most of what had leaked: a 20-core Grace CPU paired with a Blackwell GPU carrying 6,144 CUDA cores and up to 128GB of unified memory, "up to 1 petaflop" of FP4 AI compute, and the ability to run 120-billion-parameter models with a 1-million-token context. NVIDIA says RTX Spark laptops and compact desktops ship "this fall" from ASUS, Dell, HP, Lenovo, Microsoft Surface, MSI, Acer, and Gigabyte. [Source: NVIDIA press release](https://nvidianews.nvidia.com/news/nvidia-microsoft-windows-pcs-agents-rtx-spark). The rest of this article is preserved as originally published (pre-keynote) for historical accuracy, with the "N1X" name used throughout as it was written; see the update note above for current naming and status.

Jensen Huang takes the Computex stage on **[June 1, 2026](https://videocardz.com/newz/nvidia-confirms-jensen-huang-gtc-taipei-keynote-on-june-1st-day-before-computex)** at GTC Taipei — and for the first time, an NVIDIA chip is expected to live inside a *laptop* rather than a data center rack. The [N1X is an ARM-based SoC co-developed with MediaTek](https://www.techtimes.com/articles/317428/20260530/nvidia-arm-laptop-chip-n1x-confirmed-computex-cuda-rtx-5070-gpu-onboard.htm), packing a Blackwell-architecture GPU with [6,144 CUDA cores alongside a 20-core ARM CPU](https://nvidianews.nvidia.com/news/nvidia-microsoft-windows-pcs-agents-rtx-spark). This is a preview based on [pre-announcement leaks and confirmed specifications](https://www.tomshardware.com/pc-components/cpus/nvidias-long-awaited-n1-n1x-soc-specs-leak-ahead-of-computex-launch-n1-to-feature-up-to-20-arm-based-cores-standard-n1-equipped-with-12-and-10-core-configs).

## What Is the N1X?

The N1X is NVIDIA's first laptop system-on-chip — a single die combining CPU and GPU on a [3nm process](https://www.trendforce.com/news/2026/06/01/news-nvidia-enters-pc-market-with-rtx-spark-featuring-mediatek-co-designed-n1x-cpu-on-tsmc-3nm/):

- **CPU**: 20 ARM cores in a hybrid configuration — [10 high-performance Cortex-X925 cores paired with 10 efficiency Cortex-A725 cores](https://videocardz.com/newz/nvidia-n1x-n1-laptop-chip-specifications)
- **GPU**: [48 Blackwell streaming multiprocessors, 6,144 CUDA cores](https://videocardz.com/newz/nvidia-n1x-n1-laptop-chip-specifications) — [the same core count as the desktop RTX 5070](https://www.nvidia.com/en-us/geforce/graphics-cards/50-series/rtx-5070-family/)
- **Memory**: [Up to 128 GB LPDDR5X](https://nvidianews.nvidia.com/news/nvidia-microsoft-windows-pcs-agents-rtx-spark) (unified, shared between CPU and GPU)
- **Architecture**: Blackwell — [the same architecture family as NVIDIA's B100/B200/GB200 datacenter GPUs and the GeForce RTX 50-series desktop cards](https://www.nvidia.com/en-us/data-center/technologies/blackwell-architecture/) (not H100/H200, which are the prior Hopper generation)

A sister chip — [the N1 — is expected with a lower core count](https://videocardz.com/newz/nvidia-n1x-n1-laptop-chip-specifications) (an 18-core, 40-SM/5,120-CUDA-core configuration has leaked), targeting thinner/lighter form factors.

[MediaTek contributed the CPU design, with NVIDIA developing the GPU and overall chip architecture](https://nvidianews.nvidia.com/news/nvidia-microsoft-windows-pcs-agents-rtx-spark). The project was [reportedly delayed from an original second-half-2025 target](https://www.trendforce.com/news/2025/07/23/news-nvidia-and-mediatek-reportedly-delay-n1x-processor-launch-from-second-half-of-2025-to-q1-2026/), with contemporaneous reporting at the time citing [Windows-on-ARM software readiness issues and pointing to availability slipping as late as 2027](https://winbuzzer.com/2025/07/24/nvidias-game-changing-arm-chip-for-laptops-delayed-to-2027-amid-microsoft-os-hurdles-xcxwbn/).

## The CUDA Advantage

The most important word in the N1X spec sheet for AI developers is **CUDA**.

[Qualcomm's Snapdragon X Elite has been the only Windows-on-ARM chip from a major vendor](https://www.windowscentral.com/hardware/laptops/nvidia-wants-push-laptops-forward-after-qualcomm-kickstarted-windows-on-arm) and offers respectable NPU performance ([up to 45 TOPS](https://www.qualcomm.com/laptops/products/snapdragon-x-elite)). But it runs on Qualcomm's proprietary AI stack — [ONNX, QNN, and DirectML are the practical options, with no CUDA](https://onnxruntime.ai/docs/genai/howto/build-models-for-snapdragon.html). AMD's Phoenix and Strix APUs support ROCm, but [ROCm's adoption in the AI tooling ecosystem remains far behind CUDA](https://www.neowin.net/news/amd-rocm-open-source-nvidia-cuda-rival-gets-massive-windows--linux-improvements/), including on Windows.

The N1X changes this. A developer who has tuned a llama.cpp build for CUDA, or relies on PyTorch's CUDA backend, or runs Flash Attention — that code runs natively on the N1X without recompilation gymnastics or framework substitution, in a laptop you can carry through an airport.

## Local AI Inference Capabilities

The raw numbers matter for local LLM inference:

- **128 GB unified memory** removes the discrete GPU VRAM bottleneck that has limited local model sizes — [a 70B model at 4-bit (Q4) quantization needs roughly 35-48 GB depending on the quantization method and context length](https://www.sitepoint.com/quantization-explained-consumer-gpu/), comfortably within the N1X's memory budget
- **Shared, coherent CPU/GPU memory** ([connected via NVLink-C2C](https://nvidianews.nvidia.com/news/nvidia-microsoft-windows-pcs-agents-rtx-spark)) avoids the PCIe copy overhead that hurts discrete GPU setups for small-batch inference

For comparison, Apple's M4 Max offers a [similar unified memory capacity ceiling of 128 GB](https://www.apple.com/newsroom/2024/10/apple-introduces-m4-pro-and-m4-max/) — but in a macOS-only ecosystem, and with meaningfully higher memory bandwidth ([up to 546 GB/s](https://www.apple.com/newsroom/2024/10/apple-introduces-m4-pro-and-m4-max/) versus [an estimated 270-300 GB/s for the N1X](https://hothardware.com/news/nvidia-n1-laptop-motherboard-leaks) based on its leaked 16-channel LPDDR5X configuration). The N1X brings comparable memory capacity to Windows, with full CUDA compatibility, though not comparable bandwidth.

Realistic expectations: a leaked engineering-sample benchmark put the N1X's integrated GPU clock at [just 1.05 GHz, versus the discrete RTX 5070's 2.3-2.51 GHz boost clock](https://www.techspot.com/news/108835-nvidia-n1x-ai-pc-chip-leaks-same-number.html) — despite sharing the same 6,144 CUDA core count. That same leak measured an [OpenCL (Geekbench) score of 46,361, which beat every other integrated GPU tested](https://www.techspot.com/news/108835-nvidia-n1x-ai-pc-chip-leaks-same-number.html) but is well short of the RTX 5070's own scores; the outlet cautioned the sample wasn't confirmed to be running at full clocks. Treat any specific "N1X is X% of an RTX 5070" figure as unconfirmed until NVIDIA publishes real benchmarks — what's verified is that it beats other integrated/NPU-based Windows-on-ARM graphics and has the memory capacity to hold 13B-70B models locally.

## Who Makes N1X Laptops?

Dell and Lenovo have both been confirmed through leaks — [an internal Lenovo sign-in (ADFS) portal referenced the N1X twice in late May 2026](https://winbuzzer.com/2026/05/26/lenovo-leak-points-to-nvidia-n1x-gaming-laptop-push-xcxwbn/), with [leaked Lenovo model names including the Legion 7, IdeaPad Slim 5, Yoga Pro 7, and Yoga 9](https://www.windowscentral.com/hardware/lenovo/lenovo-legion-nvidia-n1x-leak), and [Dell's lineup reportedly including XPS and Alienware models](https://www.tomshardware.com/pc-components/cpus/nvidias-n1-n1x-chips-leak-once-again-this-time-tipped-for-release-in-first-half-of-2026-hotly-anticipated-chips-to-reportedly-debut-on-dell-and-lenovo-laptops). Asus is also [reportedly developing N1X designs](https://www.techtimes.com/articles/317428/20260530/nvidia-arm-laptop-chip-n1x-confirmed-computex-cuda-rtx-5070-gpu-onboard.htm).

Positioning will likely be:
- **Thin-and-light creators** who want CUDA for local AI without carrying a gaming GPU
- **AI developers** who want a portable CUDA environment
- **Power users** who want gaming-capable ARM performance

## The Competitive Landscape

| Platform | CPU | GPU | CUDA | Max Unified RAM | Notes |
|---|---|---|---|---|---|
| [NVIDIA N1X](https://videocardz.com/newz/nvidia-n1x-n1-laptop-chip-specifications) | 20-core ARM | 6,144 CUDA (Blackwell) | Yes | 128 GB | Announced June 1 |
| [Apple M4 Max](https://www.apple.com/newsroom/2024/10/apple-introduces-m4-pro-and-m4-max/) | 16-core Apple | 40-core GPU | No (MPS) | 128 GB | macOS only |
| [Qualcomm Snapdragon X Elite](https://www.qualcomm.com/laptops/products/snapdragon-x-elite) | 12-core Oryon | Adreno | No | 64 GB | No CUDA |
| [AMD Strix Halo](https://www.amd.com/en/products/processors/desktops/ryzen/ryzen-ai-halo/ryzen-ai-max-plus-395.html) | 16-core Zen 5 | 40 RDNA 3.5 CUs | No (ROCm) | 128 GB | x86, ROCm limited |

The N1X is the only option combining Windows compatibility, ARM efficiency, high memory capacity, and the CUDA ecosystem. Its weakness remains Windows ARM software compatibility — not all applications and games run natively, and [kernel-level anti-cheat systems (BattlEye, Vanguard) have historically blocked many multiplayer games on ARM](https://www.techradar.com/computing/windows-laptops/epic-delivers-on-promise-to-fix-anti-cheat-games-so-they-work-on-laptops-with-snapdragon-x-cpus-starting-with-fortnite), though Epic's Easy Anti-Cheat has recently been ported to Windows-on-ARM.

## What to Watch at GTC Taipei (June 1)

Jensen Huang's keynote is scheduled for **[11 a.m. Taiwan Time on June 1, 2026](https://videocardz.com/newz/nvidia-confirms-jensen-huang-gtc-taipei-keynote-on-june-1st-day-before-computex)** (8 p.m. PT on May 31). Specific items worth watching:

1. **Official N1X naming** — leaks use "N1" and "N1X"; NVIDIA may introduce a product family name
2. **Performance numbers** — NVIDIA will likely show AI inference benchmarks (tokens/sec, image generation)
3. **OEM lineup** — confirmed Dell/Lenovo models, pricing, availability dates
4. **CUDA compatibility claims** — which frameworks and tools are supported day one vs. roadmap
5. **N1 (base model)** — a lower-power tier targeting ultrabooks

[MediaTek's Computex keynote, originally scheduled for June 3, was cancelled](https://www.computextaipei.com.tw/en/news/31E5016E7906D36C/info.html?lt=data&cr=7), and industry coverage read the timing as [NVIDIA getting the spotlight for its N1 launch](https://wccftech.com/mediatek-abruptly-pulled-from-computex-2026-keynote-slot-handing-nvidia-the-stage/) — a signal the N1X reveal is a centerpiece announcement.

## What This Means for AI Builders

If the N1X delivers on its specs and CUDA compatibility, it reshapes the local AI development workflow:

- **End of the "Mac or CUDA" choice**: developers building CUDA-optimized AI applications have historically needed either a gaming laptop (heavy, hot, short battery) or to work in the cloud. The N1X offers CUDA in a thin-and-light ARM form factor.
- **Local model development without a workstation**: 70B models locally, on battery, without a $4,000 desktop GPU.
- **Edge deployment testing**: AI apps targeting NVIDIA Jetson or datacenter CUDA can be developed and tested on the same architecture without a separate test machine.
- **Windows on ARM maturation**: The N1X gives the Windows ARM ecosystem a reason to solve its remaining compatibility gaps — NVIDIA's developer relations team will be pushing hard on framework support.

At the time of this preview, the risk was timing: the project had [already slipped once, from an original second-half-2025 target](https://www.trendforce.com/news/2025/07/23/news-nvidia-and-mediatek-reportedly-delay-n1x-processor-launch-from-second-half-of-2025-to-q1-2026/), with [contemporaneous reporting warning broad availability could land as late as 2027](https://winbuzzer.com/2025/07/24/nvidias-game-changing-arm-chip-for-laptops-delayed-to-2027-amid-microsoft-os-hurdles-xcxwbn/). That risk did not materialize on the timeline feared: NVIDIA confirmed at the June 1 keynote that RTX Spark laptops and compact desktops would ship "this fall" (2026), not 2027 — see the update note above. What remains to be seen post-launch is the developer tools certification work — PyTorch, llama.cpp, TensorRT-LLM, ComfyUI — and whether framework support is genuinely day-one-ready across the confirmed OEM lineup.

## Bottom Line

The N1X is the most significant PC hardware announcement for local AI development since Apple Silicon — and potentially more important, because it brings the CUDA ecosystem into a mainstream Windows laptop. Whether NVIDIA can execute the software side as cleanly as the hardware side will determine whether this is a watershed moment or a promising but rough first generation.

The June 1 keynote will answer the key questions: real performance numbers, confirmed pricing, and which developer frameworks are ready at launch.

*This was originally published as a pre-announcement preview based on confirmed leaks and pre-release information. It has since been updated (2026-08-23) with a summary of what NVIDIA officially confirmed at the June 1, 2026 GTC Taipei keynote — see the update note near the top of this article. The body text below the update note is preserved as originally written, pre-keynote.*

---

## Sources

- [NVIDIA ARM Laptop Chip N1X Confirmed for Computex: CUDA and RTX 5070 GPU Onboard — TechTimes](https://www.techtimes.com/articles/317428/20260530/nvidia-arm-laptop-chip-n1x-confirmed-computex-cuda-rtx-5070-gpu-onboard.htm)
- [NVIDIA N1/N1X SoC Specs Leak Ahead of Computex — Tom's Hardware](https://www.tomshardware.com/pc-components/cpus/nvidias-long-awaited-n1-n1x-soc-specs-leak-ahead-of-computex-launch-n1-to-feature-up-to-20-arm-based-cores-standard-n1-equipped-with-12-and-10-core-configs)
- [NVIDIA N1 and N1X Laptop Chips Leaked: Computex Announcement Teased — TBreak](https://tbreak.com/nvidia-n1-n1x-laptop-chips-computex/)
- [Nvidia's N1X Specs Leak in Full — XDA Developers](https://www.xda-developers.com/mere-days-before-computex-2026-information-on-the-nvidia-n1-chip-leaked-online/)
- [Nvidia's N1X: The Jolt Windows Laptops Need — PCWorld](https://www.pcworld.com/article/3151058/nvidias-n1x-could-be-the-jolt-windows-laptops-need-with-one-big-catch.html)

---

*ChatForest researches AI tools and infrastructure to help builders make informed decisions. We have not handled N1X hardware — this assessment is based on published specifications and industry reporting.*

