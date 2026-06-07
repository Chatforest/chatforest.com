---
title: "XPeng IRON and BYD Yao-Shun-Yu: China's EV Giants Enter the Humanoid Robot Race"
date: 2026-06-04
description: "XPeng's IRON humanoid robot — 82 DOF, 3,000 TOPS, open SDK — targets mass production by end of 2026. BYD confirmed its Yao-Shun-Yu project with an open platform strategy and 150 prototypes running 24/7. This guide covers what builders need to know about China's EV-to-robot wave."
og_description: "XPeng IRON ships 82 DOF, triple Turing chip brain (3,000 TOPS), and an open SDK. BYD's Yao-Shun-Yu runs 150 prototypes with an open platform strategy. Two of the world's biggest EV makers just entered the humanoid robot market — here's what it means for builders."
content_type: "Builder's Log"
categories: ["Robotics AI", "AI Hardware", "Open Source Models", "Developer Tools"]
tags: ["xpeng", "byd", "humanoid-robots", "iron-robot", "yao-shun-yu", "embodied-ai", "vla", "vlt", "china-ai", "physical-ai", "open-platform", "builders-log"]
draft: false
---

Two of the world's largest electric vehicle manufacturers — XPeng and BYD — confirmed humanoid robot programs within days of each other in early June 2026. Both are building open platforms. Both are leveraging automotive supply chains to cut costs that pure-play robotics startups can't match. And both are targeting the same sequence: factory floors first, then retail showrooms, then homes.

This isn't a side project. XPeng has a full-chain humanoid factory under construction, mass production targeted for end of 2026, and a developer SDK already announced. BYD has 150 prototypes running 24/7 in Shenzhen and Changsha, a dedicated Future Lab, and a recruitment drive across 10 engineering disciplines.

Here's what builders need to understand about both programs.

---

## Why Automakers Keep Winning at Humanoid Robots

The pattern is no longer surprising. Tesla, XPeng, BYD, and Li Auto are all building humanoid robots. The reasons come down to three supply chain advantages that pure robotics startups can't easily replicate:

**Motors and actuators.** BYD manufactures its own motors, batteries, chips, and electronics at scale for EVs. The same components — brushless DC motors, high-density battery cells, custom silicon — are the critical path items in humanoid robots. BYD already has the supplier relationships and manufacturing lines.

**AI and perception.** XPeng's VLA (Vision-Language-Action) model for IRON is a direct adaptation of the company's autonomous driving AI. The core competency — teaching a neural network to interpret visual input and translate it into motor commands — is identical whether the platform has four wheels or two legs.

**Manufacturing scale.** XPeng produces 190,000+ EVs per year. That manufacturing infrastructure — precision assembly, quality control, supply chain logistics — converts directly to robot production. The company is targeting 1 million IRON units by 2030, a number that would be impossible for a startup without this foundation.

BYD EVP Li Ke framed the strategic gap clearly: *"The fundamental challenge in this space is that China's robots lack a brain, while US robots have strong limbs. BYD aims to produce robots that excel in both dimensions."*

---

## XPeng IRON

### Overview

XPeng unveiled the next-generation IRON humanoid at its 2026 Physical AI showcase alongside XPENG VLA 2.0, a new robotaxi platform, and a flying car. IRON is the robot that will reach mass production first.

**Mass production target:** End of 2026  
**Commercial deployment:** Q1 2027  
**Long-term production goal:** 1 million units by 2030  
**Manufacturing:** Full-chain dedicated humanoid factory (groundbreaking announced 2026)

### Hardware Specifications

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

The 22-DOF hands are a notable spec. Most current-generation humanoid robots operate with 6–12 DOF per hand. 22 DOF enables fine manipulation tasks — assembly, object handling, tool use — that are necessary for both factory work and household assistance.

The solid-state battery is significant for home deployment, where charging infrastructure is limited. Solid-state chemistry offers higher energy density per kilogram and eliminates the flammability risks of lithium-ion, which matters when the robot is operating in a domestic environment.

### Brain Architecture: VLT + VLA + VLM

XPeng's "brain" for IRON combines three large-model systems:

**VLM (Vision-Language Model):** The perceptual foundation. Processes visual and language input together, enabling the robot to understand what it sees and what it's being asked to do. Acts as the base capability layer.

**VLA (Vision-Language-Action):** Derived directly from XPeng's autonomous driving AI. Handles complex joint control — translating high-level intent into precise motor commands across 82 degrees of freedom. End-to-end: visual input goes in, joint angles come out, without intermediate language translation.

**VLT (Vision-Language-Task):** The planning and decision-making layer. Given a high-level instruction ("assemble this part" or "bring me water"), VLT decomposes the goal into a sequence of sub-actions, plans execution order, monitors progress, and adapts when the environment doesn't match expectations. This is what allows IRON to operate in unstructured environments where scripted behavior would fail.

XPENG VLA 2.0, unveiled alongside IRON, runs the same end-to-end visual-to-action architecture without language translation as an intermediate step — the same model that handles the company's robotaxi fleet now handles the robot's physical movements.

### Developer Access: IRON SDK

XPeng has announced an open IRON SDK for global developers. This is the primary builder hook:

- Build customized applications on IRON
- Integrate third-party software with IRON's perception and action systems
- Access XPeng's robot ecosystem for commercial deployment

No release date for the SDK has been confirmed. Mass production of IRON hardware begins end of 2026; SDK availability will likely be announced alongside or shortly before commercial deployment in Q1 2027.

---

## BYD Yao-Shun-Yu

### Overview

BYD's humanoid robot program has been running since 2022 under the codename "Yao-Shun-Yu" — named after three legendary Chinese emperors (Yao, Shun, and Yu) associated with wisdom, virtue, and practical achievement. The program operates under BYD's 15th Business Unit (electronic integration and intelligence) through a specialized lab called the **Future Lab**, carved out from BYD's Technology Research Institute specifically for embodied AI.

The confirmation came from BYD EVP Li Ke in early June 2026, marking the company's first public acknowledgment of the program after four years of development.

### Current Development Status

| Metric | Value |
|--------|-------|
| Development start | 2022 |
| Prototypes active | 150 (running 24/7 in Shenzhen and Changsha) |
| Commercial timeline | Not announced |
| Technical specs | Not disclosed |
| Investment target | Not disclosed |

150 prototypes running continuously is a meaningful signal. At that scale, BYD is past early-stage research and into reliability testing and operational data collection — the phase where robots accumulate the real-world interaction data needed to train robust VLA models.

### Hardware Advantages from EV Manufacturing

BYD's manufacturing edge is deeper than XPeng's. BYD is the world's largest EV manufacturer and one of the few companies that builds its own:

- **Motors** — including the proprietary BYD ET-i drive system
- **Battery cells** — Blade Battery (LFP chemistry, ultra-thin form factor)
- **Semiconductors** — BYD Semiconductor produces IGBT, SiC, and custom AI chips
- **Electronics** — full integration from component to system level
- **Precision manufacturing** — automotive-grade assembly at scale

This vertical integration means BYD can control cost and quality on every major hardware subsystem in a humanoid robot without depending on external suppliers. For comparison, most robotics startups depend on Harmonic Drive actuators, third-party battery packs, and off-the-shelf compute — each with supply constraints and margin requirements.

### Open Platform Strategy

BYD is building what Li Ke described as a platform model similar to BYD's broader "technology fish pond" corporate strategy: develop the core platform, then invite partners to build on top of it.

Concretely:
- BYD builds the core robot hardware and base AI systems
- Third-party software developers integrate via platform APIs
- Third-party hardware makers can build components certified for BYD's platform
- BYD cooperates with established robotics firms to accelerate capability development

This is a meaningful structural difference from pure-play robotics companies that try to own the entire stack. If BYD executes, builders will be able to build software for Yao-Shun-Yu robots without manufacturing their own hardware — similar to how app developers write for Android without building phones.

### Deployment Sequence

BYD has been explicit about the three-phase deployment path:

**Phase 1 — Factories:** BYD's own manufacturing facilities, where the company controls the environment and operational requirements. BYD becomes its own largest customer, providing both revenue and operational data.

**Phase 2 — Retail (4S stores):** BYD's overseas dealership network, starting with European 4S stores. Use cases: multilingual customer service, showroom guidance, product demonstrations. 4S stores operate in a semi-controlled environment (indoor, known layout, bounded task set) that's more predictable than general home use.

**Phase 3 — Homes:** Cooking, housework, companionship. Distributed through BYD's existing dealer network, the same channel that sells EVs.

This deployment sequence is operationally conservative and strategically smart. Each phase provides real-world data for the next, and BYD's own facilities and dealerships provide controlled deployment environments with direct feedback loops.

### Hiring Profile

BYD's Future Lab is actively recruiting across 10 engineering disciplines (Shenzhen, Hefei, and Changsha):

- Senior Algorithm Engineers
- Senior Structural Engineers
- Senior Simulation Engineers
- Senior Robotics Engineers
- Senior Perception Algorithm Engineers
- (Plus additional specializations in motor control, battery systems, chip design, and software)

The hiring profile confirms that BYD is building the full stack internally — hardware, simulation, perception, and algorithms — rather than licensing core capabilities from a partner.

---

## The Competitive Landscape

XPeng and BYD enter a market that already has active deployments:

| Company | Robot | Status (June 2026) |
|---------|-------|---------------------|
| Tesla | Optimus Gen-3 | 50 units deployed at Shanghai Gigafactory |
| XPeng | IRON | Mass production Q4 2026, commercial Q1 2027 |
| Figure AI | Figure 02 | 200-hour autonomous run milestone reached |
| Unitree | H1 / G1 | Shipping commercially, ~$16K–$90K range |
| Xiaomi | CyberOne 2 | Internal deployments, no broad commercial availability |
| BYD | Yao-Shun-Yu | 150 prototypes, no commercial timeline |
| Li Auto | Nexus (internal) | Unconfirmed development stage |

The key distinction is between companies that have disclosed hardware specs and deployment timelines (XPeng) and companies still in the development confirmation phase (BYD). Tesla's Shanghai deployment and Figure AI's autonomous run milestone represent the frontier of real-world reliability testing.

---

## The "Brain vs. Limbs" Problem

Li Ke's framing — China's robots lack a brain, US robots have strong limbs — is a rough cut at a real structural gap in the 2026 humanoid market.

**The limbs side:** Chinese EV manufacturers are well-positioned here. High-DOF actuators, solid-state batteries, precision manufacturing, and cost-effective production are all capabilities BYD and XPeng have from automotive. The hardware cost curves for humanoid robots from Chinese EV manufacturers are expected to track EV cost curves — steep declines through manufacturing scale.

**The brain side:** Foundation models for embodied AI are currently dominated by US-based research (NVIDIA GR00T N1.6, Google DeepMind, Figure AI's Helix). XPeng's VLT/VLA/VLM stack is a credible Chinese response — the company has been training large models for autonomous driving for years and the adaptation to robotics is well-funded.

BYD's 2026 VLA development strategy is less visible. The Future Lab's hiring profile shows AI algorithm work happening in-house, but no model architecture or benchmark data has been published. The 150 prototypes running 24/7 are collecting the operational data needed to train a competitive brain — but training timelines depend on data volume, model architecture, and compute investment, none of which BYD has disclosed.

The practical implication for builders: XPeng's IRON SDK gives you a near-term integration target (Q1 2027) with a disclosed, competitive brain architecture. BYD's open platform is strategically significant but has an undefined timeline.

---

## What Builders Should Watch

**1. XPeng IRON SDK release date.** Mass production hardware end of 2026 means SDK documentation and early access programs should appear in H2 2026. Watch XPeng developer portal and GitHub for announcements.

**2. BYD commercial timeline announcement.** The 150-prototype phase typically precedes a commercial announcement by 6–18 months in the EV industry. BYD's pattern (Disruptive Technology Launch Conference) suggests a staged announcement approach.

**3. VLA 2.0 public availability.** XPENG VLA 2.0 underpins IRON's physical AI capability. Whether XPeng open-sources components (as NVIDIA did with GR00T N1.6) will determine whether builders can fine-tune the model for custom applications.

**4. BYD open platform partner announcements.** BYD has explicitly said it will partner with established robotics firms. Who those partners are will define the developer ecosystem around Yao-Shun-Yu.

**5. Cost curves.** BYD's automotive manufacturing infrastructure points toward aggressive price competition. Unitree's H1 is currently ~$90K. XPeng has not disclosed IRON pricing. If BYD brings automotive-scale economics to humanoid production, the cost per unit could fall below $20K within 3–5 years — the level at which commercial deployments outside of large factories become economically viable.

---

## Quick Reference

**XPeng IRON**
- GitHub / SDK: Not yet public (announced as coming)
- XPENG VLA 2.0 technical details: `xpeng.com/news/`
- Mass production: Q4 2026
- Commercial: Q1 2027

**BYD Yao-Shun-Yu**
- Future Lab: Under BYD 15th Business Unit
- Current status: 150 prototypes, active recruitment
- Open platform: Confirmed, timeline TBD
- Commercial: Not yet announced

**Context**
- NVIDIA GR00T N1.6 (potential "brain" supply for Chinese robots): `github.com/NVIDIA/Isaac-GR00T`
- Unitree (current commercial baseline): `unitree.com`
- Figure AI Helix (US competitor): `figure.ai`
