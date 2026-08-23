# NVIDIA GTC Taipei 2026 Preview: N1X Reveal, Vera Rubin Updates, and the Five-Layer Cake

> Jensen Huang keynotes GTC Taipei on June 1, 2026, one day before Computex opens. Here's what to expect: the first formal N1X ARM laptop chip reveal, Vera Rubin NVL72 partner news, Physical AI Days, DLSS 5, and NVIDIA's full-stack AI factory strategy.


**At a glance:** NVIDIA GTC Taipei 2026, June 1–4, Taipei International Convention Center and Taipei Music Center. Jensen Huang keynotes June 1 at 11:00 AM Taipei time (3:00 AM UTC / 11:00 PM EDT Sunday). The event runs concurrently with Computex 2026 (June 2–5). Main expected story: the first formal announcement of the N1X ARM laptop SoC — NVIDIA's first chip designed to live inside a laptop rather than a rack. Secondary story: Vera Rubin NVL72 partner and delivery news, plus expanded physical AI and robotics programming.

---

GTC Taipei has historically been the conference where NVIDIA talks *to* Asia — the Taiwan semiconductor ecosystem, ODMs, OEMs, and the manufacturing partners that actually build the hardware. This year it is also the launching pad for the most architecturally significant shift in NVIDIA's consumer product history.

For the first time, NVIDIA is expected to put a chip inside a laptop.

## When and Where

**GTC Taipei 2026** runs from **June 1 through June 4, 2026**, across two venues:

- **Keynote (June 1):** Taipei Music Center, 11:00 AM Taipei Standard Time
- **Conference sessions and labs (June 2–4):** Taipei International Convention Center (TICC)

The event runs concurrently with **Computex 2026** (June 2–5) — an intentional overlap that puts Jensen Huang's keynote one day before the Computex floor opens ([NVIDIA GTC Taipei](https://www.nvidia.com/en-tw/gtc/taipei/); [WCCFTech](https://wccftech.com/nvidia-ceo-jensen-huang-to-host-gtc-taipei-keynote-ahead-of-computex-2026/)). Any hardware announced at GTC Taipei on June 1 will be available for hands-on demos at OEM booths starting June 2.

The keynote is **free to livestream** globally via [NVIDIA's YouTube channel and nvidia.com/gtc](https://www.nvidia.com/en-tw/gtc/taipei/).

---

## The N1X: NVIDIA's First Laptop Chip

The most anticipated announcement at GTC Taipei is also the one NVIDIA has not officially confirmed: the **N1X**, a custom ARM-based SoC co-developed with MediaTek.

Based on leaked engineering boards and specs reported from a Lenovo internal product database, here is what the N1X was expected to be ahead of the keynote ([Tom's Hardware](https://www.tomshardware.com/pc-components/cpus/nvidias-long-awaited-n1-n1x-soc-specs-leak-ahead-of-computex-launch-n1-to-feature-up-to-20-arm-based-cores-standard-n1-equipped-with-12-and-10-core-configs); [igor'sLAB](https://www.igorslab.de/en/nvidia-n1-spotted-on-laptop-motherboard-leak-featuring-128-gb-of-lpddr5x-solidifies-the-hardware-status-of-the-arm-project/)):

| Spec | Expected |
|------|----------|
| CPU | 20-core ARM (10× Cortex-X925 + 10× Cortex-A725) |
| GPU | 48 Blackwell SMs / 6,144 CUDA cores |
| Process node | 3nm |
| Memory | Up to 128 GB LPDDR5X (unified, shared CPU/GPU) |
| AI throughput | ~180–200 TOPS, per a Digitimes-sourced report ([Tom's Hardware](https://www.tomshardware.com/pc-components/cpus/nvidia-and-mediateks-ai-cpu-may-not-see-mass-rollout-until-late-2026-asus-dell-and-lenovo-reportedly-developing-n1x-desktops-and-laptops); [borncity.com](https://borncity.com/news/nvidia-n1x-20-kern-chip-mit-200-tops-ki-kraft-zur-computex/)) — a separate full spec-sheet leak put peak NVFP4 throughput as high as ~1,000 TOPS, so figures vary by source and measurement method |
| Laptop price range | Two tiers reported: base **N1** laptops ~$1,799+, premium **N1X** laptops ~$2,899+ (revised upward from earlier $1,000–$1,500 estimates as more specific leaks emerged, per Morgan Stanley analyst checks — [VideoCardz](https://videocardz.com/newz/nvidia-rtx-spark-laptops-may-start-above-1799-n1x-systems-reportedly-above-2899); [Windows Report](https://windowsreport.com/nvidia-rtx-spark-n1x-laptops-pcs-may-start-at-an-eye-watering-price-of-2899/)) |

The key word in that spec table is **CUDA**. Every competing ARM-based laptop chip — Qualcomm's Snapdragon X Elite, Apple's M4 series, AMD's Strix Point — runs on proprietary AI stacks. The N1X is expected to bring the CUDA ecosystem to a portable Windows device for the first time: code built for PyTorch's CUDA backend, TensorRT-LLM, or llama.cpp with CUDA support is expected to run without recompilation ([byteiota](https://byteiota.com/nvidia-n1x-cuda-windows-arm/)).

Dell and Lenovo are confirmed OEM partners based on pre-announcement leaks, with Asus and MSI also reportedly preparing devices ([Tom's Hardware](https://www.tomshardware.com/pc-components/cpus/nvidias-n1-n1x-chips-leak-once-again-this-time-tipped-for-release-in-first-half-of-2026-hotly-anticipated-chips-to-reportedly-debut-on-dell-and-lenovo-laptops)). Eight specific Lenovo/Dell models were reported ahead of launch ([TechBuzz](https://www.techbuzz.ai/articles/nvidia-s-n1-arm-chips-land-in-8-lenovo-dell-laptops-this-spring)), with broader availability reported as slipping into 2027 ([Guru3D](https://www.guru3d.com/story/nvidia-n1x-arm-soc-leak-reveals-specs-delayed-launch-to-2027/)).

For more detail on the N1X's architecture and AI inference implications, see our [full N1X preview](/reviews/nvidia-n1x-computex-2026-blackwell-laptop-ai-pc-preview/).

---

## Vera Rubin NVL72: From "In Production" to "In Deployment"

The Vera Rubin NVL72 story is no longer about whether the hardware exists — Jensen Huang confirmed at CES 2026 that Vera Rubin chips are in full production ([Tom's Hardware](https://www.tomshardware.com/tech-industry/artificial-intelligence/nvidia-ceo-confirms-vera-rubin-nvl72-is-now-in-production-jensen-huang-uses-ces-keynote-to-announce-the-milestone); [Data Center Dynamics](https://www.datacenterdynamics.com/en/news/nvidia-ceo-announces-vera-rubin-chips-are-in-full-production-during-ces-keynote/)). At GTC Taipei, the expected storyline is **delivery and deployment**.

What is already confirmed:

- **H2 2026** volume delivery to cloud customers ([NVIDIA Newsroom](https://nvidianews.nvidia.com/news/rubin-platform-ai-supercomputer))
- **Launch cloud partners:** AWS, Google Cloud, Microsoft Azure, Oracle Cloud Infrastructure, CoreWeave, Lambda, Nebius, Nscale ([Tech Times](https://www.techtimes.com/articles/319203/20260627/nvidia-vera-rubin-ships-this-fall-8-cloud-partners-10x-lower-token-cost-hbm4-triples-bandwidth.htm); [NVIDIA Newsroom](https://nvidianews.nvidia.com/news/rubin-platform-ai-supercomputer))
- **NVL72 configuration:** 72 Vera Rubin GPUs per rack, cable-free/hose-free/fanless tray design, with rack assembly time cut from more than 1.5 hours to about 5 minutes per tray — an 18x improvement, per NVIDIA ([NVIDIA Technical Blog](https://developer.nvidia.com/blog/inside-the-nvidia-rubin-platform-six-new-chips-one-ai-supercomputer/))
- **Performance claims:** up to 5x inference throughput and 10x lower cost-per-token vs. Blackwell, per NVIDIA's own figures ([Tom's Hardware](https://www.tomshardware.com/pc-components/gpus/nvidia-launches-vera-rubin-nvl72-ai-supercomputer-at-ces-promises-up-to-5x-greater-inference-performance-and-10x-lower-cost-per-token-than-blackwell-coming-2h-2026); [NVIDIA Blog](https://blogs.nvidia.com/blog/vera-rubin/))

At Taipei, expect: Taiwan-specific supply chain and partner announcements, updated delivery timelines, and integration into the "AI factory" infrastructure narrative. Vera Rubin is fabricated on TSMC's 3nm process family (reportedly the refined N3P node), and TSMC's Taiwan fabs are expected to produce the first Rubin wafers, though neither company has publicly confirmed the exact fab location — so GTC Taipei is a natural venue to discuss the manufacturing partnership publicly ([TechSpot](https://www.techspot.com/news/105852-nvidia-blackwell-ai-successor-rubin-moves-forward-six.html); [WCCFTech](https://wccftech.com/nvidia-explosive-ai-chip-demand-pushes-tsmc-to-boost-3nm-production/)).

---

## The Five-Layer Cake: NVIDIA's Full-Stack Strategy

Jensen Huang has been developing a framing for NVIDIA's business — first outlined publicly at the World Economic Forum in Davos in January 2026 — that he will likely reiterate and expand at Taipei: the **"Five-Layer Cake"** AI strategy ([NVIDIA Blog](https://blogs.nvidia.com/blog/davos-wef-blackrock-ceo-larry-fink-jensen-huang)).

The five layers, from bottom to top, are:

1. **Energy** — the power generation needed before any compute can run
2. **Chips** — the semiconductors and accelerated computing hardware
3. **Infrastructure** — the data centers that scale that compute
4. **Models** — the AI models trained and served on that infrastructure
5. **Applications** — vertical deployments (healthcare, finance, manufacturing, and more) where Huang says the economic benefit ultimately lands

The framing positions NVIDIA not as a chip company or even a platform company, but as a company whose fortunes are tied to the **entire stack** of the AI economy. Huang has used it to argue AI represents "the largest infrastructure buildout in human history" ([NVIDIA Blog](https://blogs.nvidia.com/blog/davos-wef-blackrock-ceo-larry-fink-jensen-huang)).

At Taipei, this framing is expected to provide the organizational spine for product announcements across hardware (layer 2), AI factory tooling (layer 3), and physical AI / robotics (layer 4/5).

---

## Physical AI Days

Two full days of GTC Taipei sessions (June 2–3) are dedicated to **Physical AI** — NVIDIA's term for AI that acts in the physical world: robotics, industrial automation, simulation, and semiconductor workflows.

Programming runs in both Traditional Chinese and English, reflecting the dense concentration of Taiwanese electronics and manufacturing partners. NVIDIA's global physical-AI ecosystem, announced alongside GTC San Jose in March 2026, includes ([NVIDIA Newsroom](https://nvidianews.nvidia.com/news/nvidia-and-global-robotics-leaders-take-physical-ai-to-the-real-world)):

- **Industrial robotics:** ABB Robotics, FANUC, KUKA, Yaskawa
- **Humanoid platforms:** Figure, Agility, AGIBOT, 1X, Boston Dynamics, NEURA Robotics
- **Foundation models:** Skild AI (whose "Skild Brain" model is being deployed on Foxconn's Blackwell GPU assembly lines — [NVIDIA Newsroom](https://nvidianews.nvidia.com/news/nvidia-and-global-robotics-leaders-take-physical-ai-to-the-real-world); [Technical.ly](https://technical.ly/entrepreneurship/pittsburgh-skild-ai-nvidia-foxconn-robotics-deployment/)), World Labs
- **Automotive/robotaxi:** GTC Taipei's own automotive news centers on NVIDIA DRIVE Hyperion robotaxi partners **Foxconn** (Kaohsiung robotaxi fleet), **VinFast** and **Autobrains** (Southeast Asia), **Uber** (a new Munich robotaxi program with Autobrains), and **HUMAIN** (Middle East) — announced May 31, 2026 at GTC Taipei ([NVIDIA Newsroom](https://nvidianews.nvidia.com/news/nvidia-drive-hyperion-becomes-the-global-platform-for-a-robotaxi-ready-world)). Separately, **BYD, Geely, Isuzu, and Nissan** adopted DRIVE Hyperion for Level 4 vehicles at GTC San Jose in March 2026 ([NVIDIA Newsroom](https://nvidianews.nvidia.com/news/drive-hyperion-level-4); [WinBuzzer](https://winbuzzer.com/2026/03/17/nvidia-gtc-2026-uber-robotaxi-physical-ai-drive-hyperion-xcxwbn/)); Hyundai expanded its NVIDIA partnership the same day, but for Level 2 driver-assistance integration rather than DRIVE Hyperion Level 4 adoption

The star hardware for these sessions is the **NVIDIA Jetson Thor** (Blackwell-based), which NVIDIA specs at 2,070 FP4 teraflops — 7.5x the compute of Jetson Orin — at 3.5x better energy efficiency ([NVIDIA product page](https://www.nvidia.com/en-us/autonomous-machines/embedded-systems/jetson-thor/); [NVIDIA Technical Blog](https://developer.nvidia.com/blog/introducing-nvidia-jetson-thor-the-ultimate-platform-for-physical-ai/)). Thor is positioned as the onboard inference engine for humanoid robots and autonomous vehicles operating at the edge.

**GR00T N2**, NVIDIA's next-generation humanoid foundation model (announced at GTC San Jose in March 2026), may see further demonstration at Taipei. NVIDIA's own announcement says its new "world action model" architecture helps robots "succeed at new tasks in new environments more than twice as often as leading VLA models," and that GR00T N2 is slated to be available by the end of 2026 ([NVIDIA Newsroom](https://nvidianews.nvidia.com/news/nvidia-expands-open-model-families-to-power-the-next-wave-of-agentic-physical-and-healthcare-ai)).

---

## DLSS 5

Correction: **DLSS 5 was already announced** by Jensen Huang at GTC San Jose in March 2026 — before this preview was written — so it is not a Taipei unknown. NVIDIA describes it as a real-time neural rendering model that "infuses pixels with photoreal lighting and materials," with Huang calling it "the GPT moment for graphics" ([NVIDIA GeForce News](https://www.nvidia.com/en-us/geforce/news/death-stranding-2-crimson-desert-dlss-4-multi-frame-gen/)). NVIDIA has confirmed a **fall 2026 rollout** via the NVIDIA app, with launch support from Bethesda, Capcom, and Ubisoft in titles including *Starfield*, *Resident Evil Requiem*, and *Assassin's Creed Shadows* ([NVIDIA GeForce News](https://www.nvidia.com/en-us/geforce/news/death-stranding-2-crimson-desert-dlss-4-multi-frame-gen/)).

At GTC Taipei, expect NVIDIA and OEM gaming-laptop partners to expand on DLSS 5 hardware support and timing rather than reveal it for the first time.

---

## What Is Confirmed vs. Expected

| Item | Status |
|------|--------|
| Jensen Huang keynote, June 1, 11 AM TST | **Confirmed** (NVIDIA, Computex official sites) |
| GTC Taipei runs June 1–4 | **Confirmed** |
| N1X formal announcement at keynote | **Strongly expected** — not yet official |
| N1X spec leaks (ARM CPU, 6,144 CUDA cores, 128 GB) | **Confirmed** via engineering boards and OEM database leak |
| Vera Rubin H2 2026 volume delivery | **Confirmed** (CES 2026) |
| Vera Rubin new partner announcements | **Possible** — regional context favors this |
| Five-Layer Cake strategy presentation | **Strongly expected** |
| Physical AI Days (robotics sessions) | **Confirmed** |
| DLSS 5 existence, features, fall 2026 rollout | **Already confirmed at GTC San Jose, March 2026** ([NVIDIA](https://www.nvidia.com/en-us/geforce/news/death-stranding-2-crimson-desert-dlss-4-multi-frame-gen/)) — not a Taipei unknown |
| "Consumer surprise" (per WCCFTech) | **Reported** — details unknown ([WCCFTech](https://wccftech.com/nvidia-ceo-jensen-huang-to-host-gtc-taipei-keynote-ahead-of-computex-2026/)) |

---

## How to Watch

- **Free global livestream:** via NVIDIA's YouTube channel and [nvidia.com/gtc/taipei](https://www.nvidia.com/en-tw/gtc/taipei/)
- **Keynote time conversions:** 11:00 AM TST = 3:00 AM UTC = 11:00 PM EDT (Sunday night, May 31 into June 1)

ChatForest will publish a post-event recap once the keynote closes. If the N1X is formally announced, we will update our [N1X preview](/reviews/nvidia-n1x-computex-2026-blackwell-laptop-ai-pc-preview/) with confirmed specs.

