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

The event runs concurrently with **Computex 2026** (June 2–5) — an intentional overlap that puts Jensen Huang's keynote one day before the Computex floor opens. Any hardware announced at GTC Taipei on June 1 will be available for hands-on demos at OEM booths starting June 2.

The keynote is **free to livestream** globally via NVIDIA's YouTube channel and nvidia.com/gtc.

Pre-show: A GTC Live pregame conversation with industry leaders begins at **9:00 AM TST** (two hours before the main keynote).

---

## The N1X: NVIDIA's First Laptop Chip

The most anticipated announcement at GTC Taipei is also the one NVIDIA has not officially confirmed: the **N1X**, a custom ARM-based SoC co-developed with MediaTek.

Based on leaked engineering boards and confirmed details from Lenovo's accidentally-published internal product database, here is what the N1X is expected to be:

| Spec | Expected |
|------|----------|
| CPU | 20-core ARM (10× Cortex-X925 + 10× Cortex-A725) |
| GPU | 48 Blackwell SMs / 6,144 CUDA cores |
| Process node | 3nm |
| Memory | Up to 128 GB LPDDR5X (unified, shared CPU/GPU) |
| AI throughput | ~180–200 TOPS |
| Laptop price range | ~$1,000–$1,500 |

The key word in that spec table is **CUDA**. Every competing ARM-based laptop chip — Qualcomm's Snapdragon X Elite, Apple's M4 series, AMD's Strix Point — runs on proprietary AI stacks. The N1X brings the CUDA ecosystem to a portable Windows device for the first time: llama.cpp, PyTorch CUDA backend, Flash Attention, and the broader NVIDIA developer toolchain all run natively, without recompilation.

Dell and Lenovo are confirmed OEM partners based on pre-announcement leaks; Asus is reportedly in development. Eight specific models are expected at launch, with broader availability arriving in H1 2027.

For more detail on the N1X's architecture and AI inference implications, see our [full N1X preview](/reviews/nvidia-n1x-computex-2026-blackwell-laptop-ai-pc-preview/).

---

## Vera Rubin NVL72: From "In Production" to "In Deployment"

The Vera Rubin NVL72 story is no longer about whether the hardware exists — Jensen Huang confirmed at CES 2026 that Vera Rubin chips are in full production. At GTC Taipei, the expected storyline is **delivery and deployment**.

What is already confirmed:

- **H2 2026** volume delivery to cloud customers
- **Launch cloud partners:** AWS, Google Cloud, Microsoft Azure, Oracle Cloud Infrastructure, CoreWeave, Lambda, Nebius, Nscale
- **NVL72 configuration:** 72 Vera Rubin GPUs per rack, cable-free/hose-free/fanless tray design, assembly time reduced from 2 hours to 5 minutes per tray
- **Performance claims:** up to 5x inference throughput and 10x lower cost-per-token vs. Blackwell H100-class systems

At Taipei, expect: Taiwan-specific supply chain and partner announcements, updated delivery timelines, and integration into the "AI factory" infrastructure narrative. TSMC's fab in Hsinchu produces the Vera Rubin die — GTC Taipei is naturally the right venue to discuss the manufacturing partnership publicly.

---

## The Five-Layer Cake: NVIDIA's Full-Stack Strategy

At GTC San Jose (March 2026), Jensen Huang introduced a framing for NVIDIA's business that he will likely formalize and expand at Taipei: the **"Five-Layer Cake"** AI strategy.

The five layers are:

1. **Energy and infrastructure** — power, cooling, real estate for AI facilities
2. **Accelerated computing** — GPU hardware and networking (InfiniBand, Spectrum-X)
3. **AI factories** — the full stack for training and inference at scale (Vera Rubin, DGX, NIM microservices)
4. **Agentic systems** — multi-agent orchestration, reasoning frameworks, NVIDIA NeMo and Blueprints
5. **Applications** — vertical deployments (healthcare, automotive, manufacturing, retail)

The framing positions NVIDIA not as a chip company or even a platform company, but as a **full-stack infrastructure provider** for the AI economy — analogous to what AWS is to general compute, but specialized for AI. Huang uses this structure to explain why NVIDIA's total addressable market is measured in the trillions.

At Taipei, this framing is expected to provide the organizational spine for product announcements across hardware (layer 2), AI factory tooling (layer 3), and physical AI / robotics (layer 4/5).

---

## Physical AI Days

Two full days of GTC Taipei sessions (June 2–3) are dedicated to **Physical AI** — NVIDIA's term for AI that acts in the physical world: robotics, industrial automation, simulation, and semiconductor workflows.

Programming runs in both Traditional Chinese and English, reflecting the dense concentration of Taiwanese electronics and manufacturing partners. Confirmed ecosystem participants include:

- **Industrial robotics:** ABB, FANUC, KUKA, Yaskawa
- **Humanoid platforms:** Figure, Agility Robotics, AGIBOT
- **Foundation models:** Skild AI (whose models now run on Foxconn's Blackwell production lines), World Labs
- **Automotive:** BYD, Hyundai, Nissan, Geely, Uber (robotaxi deployment)

The star hardware for these sessions is the **NVIDIA Jetson Thor** (Blackwell-based), which delivers 2,070 FP4 teraflops — 7.5x the compute of Jetson Orin — at 3.5x better energy efficiency. Thor is positioned as the onboard inference engine for humanoid robots and autonomous vehicles operating at the edge.

**GR00T N2**, NVIDIA's next-generation humanoid foundation model (previewed at GTC San Jose), may see further demonstration. Early benchmarks showed >2x success rate vs. leading vision-language-action models on novel manipulation tasks.

---

## DLSS 5

A formal rollout of **DLSS 5** is expected at or around GTC Taipei, though NVIDIA has not confirmed a specific announcement date. DLSS 5 was briefly referenced in early 2026 documentation but has not been publicly released. The Taipei timing aligns with Computex, where OEM gaming laptops would be natural launch vehicles for a DLSS software update.

No confirmed feature list for DLSS 5 is publicly available as of this writing.

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
| DLSS 5 rollout | **Expected** — timing unconfirmed |
| "Consumer surprise" (per WCCFTech) | **Reported** — details unknown |

---

## How to Watch

- **Free global livestream:** via NVIDIA's YouTube channel and [nvidia.com/gtc/taipei](https://www.nvidia.com/en-tw/gtc/taipei/)
- **Keynote time conversions:** 11:00 AM TST = 3:00 AM UTC = 11:00 PM EDT (Sunday night June 1)
- **Pre-show:** 9:00 AM TST (1:00 AM UTC / 9:00 PM EDT Saturday) — industry leader roundtable

ChatForest will publish a post-event recap once the keynote closes. If the N1X is formally announced, we will update our [N1X preview](/reviews/nvidia-n1x-computex-2026-blackwell-laptop-ai-pc-preview/) with confirmed specs.

