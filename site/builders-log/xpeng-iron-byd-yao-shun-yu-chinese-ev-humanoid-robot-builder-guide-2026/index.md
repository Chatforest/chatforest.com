# XPeng IRON and BYD Yao-Shun-Yu: China's EV Giants Enter the Humanoid Robot Race

> XPeng's IRON humanoid robot — 82 DOF, 3,000 TOPS, open SDK — targets mass production by end of 2026. BYD confirmed it is developing a humanoid robot with an open-platform strategy, though it has denied the specific prototype figures reported in the Chinese press. This guide covers what builders need to know about China's EV-to-robot wave.


Two of the world's largest electric vehicle manufacturers are pushing into humanoid robots. [XPeng](https://www.xpeng.com/news/019a56f54fe99a2a0a8d8a0282e402b7) detailed its next-gen IRON robot's specs at its [November 5, 2025 AI Day](https://www.xpeng.com/news/019a56f54fe99a2a0a8d8a0282e402b7) and escalated the program on [June 10, 2026, when CEO He Xiaopeng took direct control of the robotics unit](https://chinabizinsider.com/xpengs-he-xiaopeng-takes-robot-ceo-role-targets-iron-mass-production-by-end-2026/). Days earlier, BYD executive vice president Li Ke (Stella Li) [confirmed for the first time that BYD is developing a humanoid robot](https://cnevpost.com/2026/06/03/byd-enters-humanoid-robot-market/), a program reported in the Chinese press under the internal codename "Yao-Shun-Yu." **Note:** on June 6, 2026, [BYD officially denied several of the specific details that had circulated about that program](https://english.news18a.com/news/english_263357.html) — see the BYD section below for what the company has and hasn't confirmed. Both companies are leveraging automotive supply chains to cut costs that pure-play robotics startups can't match, and both are targeting factory floors first, then retail, then homes.

This isn't a side project for either company. XPeng has a [full-chain humanoid factory under construction in Guangzhou](https://autonews.gasgoo.com/articles/news/xpeng-to-build-full-chain-humanoid-robot-mass-production-base-in-guangzhou-2026901200610291712), mass production targeted for end of 2026, and a developer SDK already announced. BYD has confirmed active humanoid robot development and a hiring drive across multiple engineering disciplines, though — as detailed below — several widely reported specifics (a "150 prototypes" figure, testing locations, a seventh-generation prototype) were denied by BYD as inaccurate.

Here's what builders need to understand about both programs.

---

## Why Automakers Keep Winning at Humanoid Robots

The pattern is no longer surprising. Tesla, XPeng, BYD, and Li Auto are all building humanoid robots. The reasons come down to three supply chain advantages that pure robotics startups can't easily replicate:

**Motors and actuators.** BYD manufactures its own motors, batteries, chips, and electronics at scale for EVs. The same components — brushless DC motors, high-density battery cells, custom silicon — are the critical path items in humanoid robots. BYD already has the supplier relationships and manufacturing lines.

**AI and perception.** XPeng's VLA (Vision-Language-Action) model for IRON is a direct adaptation of the company's autonomous driving AI. The core competency — teaching a neural network to interpret visual input and translate it into motor commands — is identical whether the platform has four wheels or two legs.

**Manufacturing scale.** XPeng delivered [190,068 vehicles in full-year 2024](https://www.globenewswire.com/news-release/2025/03/18/3044283/0/en/XPENG-Reports-Fourth-Quarter-and-Fiscal-Year-2024-Unaudited-Financial-Results.html), with 2025 deliveries running well ahead of that pace. That manufacturing infrastructure — precision assembly, quality control, supply chain logistics — converts directly to robot production. CEO He Xiaopeng has said the [company is targeting 1 million IRON units by 2030](https://www.scmp.com/business/china-business/article/3360814/race-against-tesla-china-ev-maker-xpeng-launch-viral-humanoid-globally-2027), a number that would be impossible for a startup without this foundation.

BYD executive vice president Li Ke (Stella Li) framed the strategic gap this way: [*"Chinese robots lack a developed brain, while US robots face the problem of underdeveloped limbs"*](https://cnevpost.com/2026/06/03/byd-enters-humanoid-robot-market/) — BYD, she said, aims to produce robots that are strong in both.

---

## XPeng IRON

### Overview

XPeng unveiled the next-generation IRON humanoid at its [November 5, 2025 AI Day](https://www.xpeng.com/news/019a56f54fe99a2a0a8d8a0282e402b7) — themed "Physical AI: Emergence" — alongside XPENG VLA 2.0, a new robotaxi platform, and a flying car. IRON is the robot that will reach mass production first.

**Mass production target:** [End of 2026](https://www.xpeng.com/news/019a56f54fe99a2a0a8d8a0282e402b7)  
**Commercial deployment:** [Q1 2027, initially as retail sales assistants in Chinese XPeng stores, with overseas markets targeted for Q2 2027](https://pandaily.com/xpeng-iron-humanoid-robot-mass-production-2027)  
**Long-term production goal:** [1 million units by 2030](https://www.scmp.com/business/china-business/article/3360814/race-against-tesla-china-ev-maker-xpeng-launch-viral-humanoid-globally-2027)  
**Manufacturing:** [Full-chain dedicated humanoid factory under construction in Guangzhou's Tianhe District, announced February 2026 (~110,000 sq m)](https://autonews.gasgoo.com/articles/news/xpeng-to-build-full-chain-humanoid-robot-mass-production-base-in-guangzhou-2026901200610291712)

### Hardware Specifications

Specs below are as [announced by XPeng at its 2025 AI Day](https://www.xpeng.com/news/019a56f54fe99a2a0a8d8a0282e402b7):

| Spec | Value |
|------|-------|
| Degrees of Freedom (total) | 82 |
| Hand DOF (per hand) | 22 |
| Compute | 3 proprietary Turing AI chips |
| AI Performance | 3,000 TOPS |
| Battery | Solid-state (ultra-high energy density) |
| Outer material | Fully flexible biomimetic skin |
| Spine | Biomimetic design with muscle-like actuators |
| Head display | 3D curved display integrated into head |
| Shoulders | Agile joints mimicking full human range of motion |

The 22-DOF hands are a notable spec — well above rival designs like [Figure 02's 16-DOF hand](https://www.prnewswire.com/news-releases/figure-unveils-figure-02-its-second-generation-humanoid-setting-new-standards-in-ai-and-robotics-302214889.html). More DOF enables finer manipulation tasks — assembly, object handling, tool use — that matter for both factory work and household assistance.

The solid-state battery is significant for home deployment, where charging infrastructure is limited. Solid-state chemistry offers higher energy density per kilogram and eliminates the flammability risks of lithium-ion, which matters when the robot is operating in a domestic environment.

### Brain Architecture: VLT + VLA + VLM

XPeng describes IRON's "brain" as [combining three large-model systems, VLT + VLA + VLM, for conversation, walking, and interaction](https://www.xpeng.com/news/019a56f54fe99a2a0a8d8a0282e402b7):

**VLM (Vision-Language Model):** Adapted from XPeng's automotive work; processes visual and language input together as a base perceptual layer.

**VLA (Vision-Language-Action):** [Adapted from XPeng's autonomous driving division, this model handles control of the robot's 82 joints](https://www.humanoidsdaily.com/news/xpeng-debuts-most-human-like-iron-robot-details-vlt-brain-and-2026-production-goal) — translating intent into motor commands.

**VLT (Vision-Language-Task):** Described by XPeng as the ["core engine" and decision-making "brain"](https://www.humanoidsdaily.com/news/xpeng-debuts-most-human-like-iron-robot-details-vlt-brain-and-2026-production-goal) for autonomous action in real-world scenarios.

XPENG VLA 2.0 was [unveiled alongside IRON at the same AI Day event](https://www.xpeng.com/news/019a56f54fe99a2a0a8d8a0282e402b7) as the architecture behind the company's new robotaxi platform.

### Developer Access: IRON SDK

XPeng has [announced an open IRON SDK for global developers](https://www.xpeng.com/news/019a56f54fe99a2a0a8d8a0282e402b7). This is the primary builder hook:

- Build customized applications on IRON
- Integrate third-party software with IRON's perception and action systems
- Access XPeng's robot ecosystem for commercial deployment

No release date for the SDK has been confirmed. Mass production of IRON hardware begins end of 2026; SDK availability will likely be announced alongside or shortly before commercial deployment in Q1 2027.

---

## BYD Yao-Shun-Yu

### Overview — what's confirmed vs. denied

This section requires an unusual amount of care. Since [December 2024, CnEVPost](https://cnevpost.com/2024/12/26/byd-sets-up-lab-humanoid-robots-report/), [TechNode](https://technode.com/2024/12/17/byd-announces-recruitment-for-humanoid-robot-research-team/), and other outlets have reported that BYD set up a dedicated **Future Lab** under its **15th Business Unit** (electronic integration and intelligence) in 2022 to work on embodied AI, and that the program carries the internal codename "Yao-Shun-Yu" (尧舜禹), after three legendary Chinese sage-kings.

On June 3, 2026, BYD executive vice president Li Ke (Stella Li) [gave the company's first on-record confirmation that BYD is developing humanoid robots](https://cnevpost.com/2026/06/03/byd-enters-humanoid-robot-market/), citing overlap with BYD's automotive AI, motor control, and battery expertise, and floating an open-platform model with eventual sales through BYD's dealer network.

Then, on **June 6, 2026, BYD issued an official denial** of several more specific claims that had circulated in Chinese media in the prior days — that the robot's codename is "Yao Shun Yu," that a "seventh-generation prototype" was field-testing at Shenzhen and Changsha factories, and that BYD planned to deploy 150 prototypes now with a target of 20,000 in-house units by year end. [BYD's statement characterized all of these specifics as false](https://english.news18a.com/news/english_263357.html), even as Li Ke reiterated that humanoid robot development is real and underway.

Bottom line for builders: treat "BYD is building a humanoid robot" as confirmed, and treat the codename, the specific prototype count, and the Shenzhen/Changsha testing detail as **reported but explicitly disputed by BYD** — not established fact. BYD has said it will [publicly show a physical prototype for the first time at its "Di Space" event in August 2026](https://finance.biggo.com/news/3089d725-5613-4bac-a61c-5f3d39a7097d).

### Current Development Status

| Metric | Value |
|--------|-------|
| Development start | [2022, per Li Ke](https://cnevpost.com/2026/06/03/byd-enters-humanoid-robot-market/) |
| Prototypes active | Not confirmed by BYD — a widely reported "150 prototypes" figure was [officially denied on June 6, 2026](https://tech.yahoo.com/ai/meta-ai/articles/byds-showroom-humanoid-coming-heres-000800356.html) ("It did not deny developing a humanoid. It denied the numbers."), also [reported by News18](https://english.news18a.com/news/english_263357.html) |
| Commercial timeline | Not announced |
| Technical specs | Not disclosed |
| Investment target | Not disclosed |

### Hardware Advantages from EV Manufacturing

BYD's manufacturing edge is deeper than XPeng's. BYD [became the world's largest seller of battery-electric vehicles in 2025](https://carboncredits.com/byd-overtakes-tesla-as-worlds-biggest-ev-seller-in-2025/), overtaking Tesla, and it is one of the few companies that builds its own:

- **Motors and drive systems** — including its [e-Platform 3.0 8-in-1 electric drive system](https://en.byd.com/news/byd-debuts-e-platform-3-0-leading-the-next-generation-of-smart-electric-vehicles/)
- **Battery cells** — [Blade Battery (LFP chemistry, thin form factor)](https://www.byd.com/eu/technology/byd-blade-battery)
- **Semiconductors** — [BYD Semiconductor produces IGBT modules, SiC power devices, and automotive-grade chips](https://www.nomadsemi.com/p/byd-semiconductor-deep-dive)
- **Electronics** — full integration from component to system level
- **Precision manufacturing** — automotive-grade assembly at scale

This vertical integration means BYD can control cost and quality on major hardware subsystems in a humanoid robot without depending on external suppliers, the way most robotics startups depend on third-party actuators, battery packs, and off-the-shelf compute.

### Open Platform Strategy

Reporting on Li Ke's June 2026 comments describes BYD building [what she has called a "technology fish pond" strategy applied to robots](https://eu.36kr.com/en/p/3838956663650948): develop the core platform internally, then invite partners to build on top of it, or partner directly with established robotics firms to speed development. If BYD executes on this, the implication for builders is that they could eventually build software for BYD's robots without manufacturing their own hardware — similar to how app developers write for Android without building phones. As of this writing, BYD hasn't published API docs, a timeline, or named any launch partners.

### Deployment Sequence

Based on Li Ke's public comments, BYD's likely deployment path runs through three phases:

**Phase 1 — Factories:** [BYD's own manufacturing facilities](https://cnevpost.com/2026/06/03/byd-enters-humanoid-robot-market/), where the company controls the environment and could become its own largest customer.

**Phase 2 — Retail:** [Overseas dealership showrooms, starting with Europe](https://eu.36kr.com/en/p/3838956663650948), as shopping guides addressing labor shortages.

**Phase 3 — Homes:** Li Ke has said BYD would eventually [distribute household robots through its existing dealer network](https://cnevpost.com/2026/06/03/byd-enters-humanoid-robot-market/) if the technology and household-use case mature — this phase has no announced timeline.

None of this has been announced by BYD as a formal, numbered roadmap; it is builders' best read of Li Ke's public statements as reported by CnEVPost and 36Kr.

### Hiring Profile

BYD's Future Lab has been [actively recruiting recent master's and PhD graduates across 10 categories of senior engineer](https://www.scmp.com/tech/big-tech/article/3291243/chinas-top-ev-maker-byd-kicks-robotics-recruitment-drive-young-talent) in Shenzhen, Hefei, and Changsha, [independently corroborated by CnEVPost and Motor1](https://cnevpost.com/2024/12/26/byd-sets-up-lab-humanoid-robots-report/):

- Senior Algorithm Engineers
- Senior Structural Engineers
- Senior Simulation Engineers
- Senior Robotics Engineers
- Senior Perception Algorithm Engineers
- (Plus additional specializations in motor control, battery systems, chip design, and software)

The hiring profile confirms that BYD is building the full stack internally — hardware, simulation, perception, and algorithms — rather than licensing core capabilities from a partner. This recruiting activity predates, and is independent of, the specific June 2026 rumors BYD denied.

---

## The Competitive Landscape

XPeng and BYD enter a market that already has active deployments:

| Company | Robot | Status (as of mid-2026) |
|---------|-------|---------------------|
| Tesla | Optimus Gen-3 | [1,000+ units deployed at Fremont and Giga Texas (Jan 2026)](https://optimusk.blog/blog/tesla-optimus-factory-deployment/); Shanghai Gigafactory [named as a future manufacturing hub, not yet producing units](https://mlq.ai/news/tesla-china-president-highlights-shanghai-gigafactory-as-key-for-humanoid-robot-mass-production/) |
| XPeng | IRON | [Mass production end of 2026, commercial Q1 2027](https://pandaily.com/xpeng-iron-humanoid-robot-mass-production-2027) |
| Figure AI | Figure 03 | [200-hour autonomous package-sorting run completed with no hardware failure, May 2026](https://x.com/adcock_brett/status/2057651077928145235) |
| Unitree | H1 / G1 | [Shipping commercially, ~$13.5K (G1) to $90K (H1)](https://shop.unitree.com/collections/humanoid-robot) |
| Xiaomi | CyberOne V2 | [Internal deployments at Xiaomi facilities, no broad commercial availability](https://www.humanoidsdaily.com/news/xiaomi-debuts-cyberone-v2-at-investor-day-moving-beyond-the-factory-floor) |
| BYD | "Yao-Shun-Yu" (reported codename) | [Development confirmed; specific prototype/testing figures denied by BYD](https://tech.yahoo.com/ai/meta-ai/articles/byds-showroom-humanoid-coming-heres-000800356.html), also [reported by News18](https://english.news18a.com/news/english_263357.html) |
| Li Auto | Nexus (internal) | [Codenamed internal project, described as top-secret as of March 2026](https://cnevpost.com/2026/03/06/li-auto-pivots-to-robotics-with-secret-nexus-project/) |

The key distinction is between companies that have disclosed hardware specs and deployment timelines (XPeng, Unitree) and companies still in the development-confirmation phase (BYD, Li Auto). Figure AI's autonomous run milestone represents the current frontier of real-world reliability testing.

---

## The "Brain vs. Limbs" Problem

Li Ke's framing — [China's robots lack a developed brain, while US robots face the problem of underdeveloped limbs](https://cnevpost.com/2026/06/03/byd-enters-humanoid-robot-market/) — is a rough cut at a real structural gap in the 2026 humanoid market.

**The limbs side:** Chinese EV manufacturers are well-positioned here. High-DOF actuators, solid-state batteries, precision manufacturing, and cost-effective production are all capabilities BYD and XPeng have from automotive.

**The brain side:** Foundation models for embodied AI have a strong US research presence — [NVIDIA's Isaac GR00T N1.6](https://research.nvidia.com/labs/gear/gr00t-n1_6/), Google DeepMind's robotics work, and [Figure AI's Helix](https://www.figure.ai/news/helix). XPeng's VLT/VLA/VLM stack is a credible Chinese response — the company has been training large models for autonomous driving for years and the adaptation to robotics is well-funded.

BYD's VLA development strategy is far less visible. The Future Lab's hiring profile shows AI algorithm work happening in-house, but no model architecture or benchmark data has been published, and — as detailed above — BYD has not confirmed the scale of its current prototype testing. Training timelines for a competitive "brain" depend on data volume, model architecture, and compute investment, none of which BYD has disclosed.

The practical implication for builders: XPeng's IRON SDK gives you a near-term integration target (Q1 2027) with a disclosed, competitive brain architecture. BYD's open platform is strategically significant but has an undefined timeline.

---

## What Builders Should Watch

**1. XPeng IRON SDK release date.** Mass production hardware end of 2026 means SDK documentation and early access programs should appear in H2 2026. Watch XPeng developer portal and GitHub for announcements.

**2. BYD's August 2026 "Di Space" event.** [BYD has said it will publicly show a physical prototype there for the first time](https://finance.biggo.com/news/3089d725-5613-4bac-a61c-5f3d39a7097d) — the first real chance to see verified specs rather than disputed rumors.

**3. VLA 2.0 public availability.** XPENG VLA 2.0 underpins the company's Physical AI push. Whether XPeng open-sources components (as [NVIDIA did with GR00T N1.6](https://github.com/NVIDIA/Isaac-GR00T)) will determine whether builders can fine-tune the model for custom applications.

**4. BYD open platform partner announcements.** Li Ke has said BYD may partner with established robotics firms. Who those partners are — and whether an SDK materializes — will define the developer ecosystem around BYD's robot program.

**5. Cost curves.** BYD's automotive manufacturing infrastructure points toward aggressive price competition, though BYD hasn't disclosed robot pricing. [Unitree's H1 currently lists at $90K](https://shop.unitree.com/collections/humanoid-robot); XPeng has not disclosed IRON pricing.

---

## Quick Reference

**XPeng IRON**
- GitHub / SDK: Not yet public (announced as coming)
- XPENG VLA 2.0 technical details: `xpeng.com/news/`
- Mass production: Q4 2026
- Commercial: Q1 2027

**BYD ("Yao-Shun-Yu")**
- Future Lab: Under BYD's 15th Business Unit (reported since Dec 2024, predates June 2026 rumor cycle)
- Current status: Development confirmed by BYD (June 3, 2026); specific prototype/testing figures denied by BYD (June 6, 2026); active recruitment ongoing
- Open platform: Discussed by EVP Li Ke, no timeline or partners confirmed
- Commercial: Not yet announced; first public prototype showing expected at "Di Space," August 2026

**Context**
- NVIDIA GR00T N1.6 (potential "brain" supply for Chinese robots): `github.com/NVIDIA/Isaac-GR00T`
- Unitree (current commercial baseline): `unitree.com`
- Figure AI Helix (US competitor): `figure.ai`

