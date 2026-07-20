---
title: "Anthropic Is in Talks With Samsung to Build Its First Custom AI Chip"
date: 2026-07-21T09:00:00+09:00
description: "Anthropic is in early-stage discussions with Samsung to manufacture a custom 2nm AI accelerator — and hired the second engineer ever to join OpenAI's Jalapeño chip team to lead it. What the talks reveal about AI infrastructure strategy heading into Anthropic's IPO."
og_description: "Anthropic-Samsung custom chip talks (reported July 2, 2026): 2nm Samsung process, no design finalized yet, may not proceed. Key signal: Clive Chan hire (ex-OpenAI Jalapeño team, engineer #2). Samsung invested in Anthropic's $65B May 2026 round. Context: OpenAI's Jalapeño inference chip launched June 24; every other major AI lab has its own silicon."
card_description: "Anthropic is in early-stage talks with Samsung Electronics to manufacture a custom AI accelerator chip (reported by The Information, July 2, 2026; confirmed by Bloomberg same day). Target: Samsung's 2-nanometer process and advanced packaging. Status: no design, specs, or target workload finalized — Anthropic may not proceed. Key signal: Anthropic hired Clive Chan, the second engineer ever on OpenAI's custom chip team, who spent 2.5 years building the Broadcom-designed Jalapeño inference chip (unveiled June 24, 2026). Samsung participated in Anthropic's $65B fundraise in May 2026 at $965B valuation. Anthropic is reportedly preparing an S-1 for an IPO as early as October 2026. Every other major AI lab (Google TPU, AWS Trainium/Inferentia, Microsoft Maia 200, OpenAI Jalapeño) has its own silicon; Anthropic would be closing the last gap."
tags: ["anthropic", "samsung", "custom-chip", "hardware", "ai-infrastructure", "silicon", "claude", "ipo"]
categories: ["reviews"]
author: "ChatForest"
last_refreshed: 2026-07-21
---

**At a glance:** Anthropic is in early-stage talks with Samsung Electronics to manufacture a custom AI chip, targeting Samsung's 2nm process, according to [The Information reporting July 2, 2026](https://techcrunch.com/2026/07/02/anthropic-is-discussing-a-new-custom-chip-with-samsung/) (confirmed by [Bloomberg](https://www.bloomberg.com/news/articles/2026-07-02/anthropic-in-talks-with-samsung-for-custom-ai-chip-information-mr3l34t4)). No design, target workload, or specifications have been finalized. Anthropic has confirmed the hire of Clive Chan, the second engineer ever to join OpenAI's custom chip team.

---

For three years, Anthropic has run Claude on other companies' chips — Google TPUs, Amazon Trainium, Nvidia GPUs through CoreWeave and direct contracts. That posture is beginning to shift.

[The Information reported July 2](https://techcrunch.com/2026/07/02/anthropic-is-discussing-a-new-custom-chip-with-samsung/) that Anthropic is in early discussions with Samsung Electronics about manufacturing a custom AI accelerator, aiming at Samsung's 2-nanometer process node. Bloomberg confirmed the same day. Early-stage means exactly that: no chip design has been started, no target workload has been selected, and no performance specifications exist. Anthropic may not proceed. But the combination of an active hire and a manufacturing partner conversation signals a direction the company is taking seriously.

## The Clive Chan Hire

The clearest evidence that Anthropic's chip ambitions are more than exploratory is the Clive Chan hire. [TechTimes reported](https://www.techtimes.com/articles/319574/20260702/anthropic-talks-samsung-build-custom-ai-chip-aiming-2nm-process.htm) that Chan was the second engineer ever to join OpenAI's dedicated custom chip team — the group that spent two and a half years building "Jalapeño," the Broadcom-designed inference accelerator [OpenAI unveiled on June 24, 2026](https://techcrunch.com/2026/07/02/anthropic-is-discussing-a-new-custom-chip-with-samsung/).

Chan's background is specifically in inference chip design for large language models — exactly the workload Anthropic needs to optimize. Inference (running model queries against live user traffic) is where most of Anthropic's compute cost lives. Training uses compute for weeks or months at a time during development; inference runs continuously at scale as long as users and API customers are active. A chip purpose-built for Claude inference would have a fundamentally different design target than a general-purpose GPU.

## What Samsung Brings

Samsung's 2-nanometer process node is the technology Samsung is using to challenge TSMC's dominance in leading-edge chip fabrication. For reference:

- TSMC's 3nm process powers Apple's M4 chips and Nvidia's Blackwell GPU family
- Samsung's 2nm targets first production in 2026, with automotive and AI accelerator customers as the initial focus
- Samsung has advanced packaging capabilities — High Bandwidth Memory (HBM) integration and chiplet packaging — that matter for AI accelerator performance

Critically, Samsung already has a financial relationship with Anthropic. [Samsung participated in Anthropic's $65 billion fundraising round in May 2026](https://mlq.ai/news/anthropic-in-early-talks-with-samsung-to-manufacture-custom-ai-chip-on-2nm-process/), alongside SK Hynix and Micron, at a valuation of $965 billion. [The Korea Herald reported](https://www.koreaherald.com/article/10797311) that Samsung's chip and memory divisions see Anthropic as a strategic customer worth deepening ties with beyond just investment.

## The OpenAI Jalapeño Context

OpenAI's Jalapeño chip — designed by Broadcom, unveiled June 24, 2026 — is the immediate reference point for what a custom LLM inference chip looks like from a US frontier lab. Jalapeño is optimized specifically for running large language models more efficiently than commodity GPUs, delivering substantially better performance per watt according to OpenAI's figures.

The competitive logic for Anthropic is straightforward: if OpenAI is reducing per-token inference cost through a custom chip while Anthropic continues buying Nvidia GPU time at market rates, Anthropic's margin disadvantage compounds over time. A custom chip isn't a shortcut — the development timeline is typically two to three years from design to volume production — but it is a structural cost lever that compounds in the opposite direction once deployed.

The competitive landscape among frontier labs on custom silicon:

| Lab | Chip program | Status |
|-----|-------------|--------|
| Google | TPU (v1–v7) | Production since 2016 |
| Amazon | Trainium (training), Inferentia (inference) | Production, AWS-only |
| Microsoft | Maia 200 | Launched January 2026 |
| OpenAI | Jalapeño (Broadcom-designed) | Unveiled June 24, 2026 |
| Anthropic | Unnamed (Samsung talks) | Early-stage, unconfirmed |

Anthropic is the last major US AI frontier lab without its own silicon program in place.

## What Anthropic Said

Anthropic confirmed the Samsung discussions without additional detail and reiterated that "Amazon Web Services's Trainium chip, Google tensor processing units and Nvidia graphic processors will remain central to how the company scales its compute strategy." The custom chip, if it proceeds, would be additive — a new option for specific inference workloads rather than a replacement for existing infrastructure commitments.

This is consistent with how every major AI lab has approached custom silicon: not as a full infrastructure replacement, but as a cost-optimization layer for high-volume, well-characterized workloads where model architecture and hardware can be co-designed together.

Anthropic's existing compute commitments are already extensive:

- **Google Cloud:** $200 billion committed over five years (announced May 2026); Broadcom TPU deal starting 2027
- **Amazon Web Services:** Up to $100 billion committed; training on AWS Trainium
- **CoreWeave:** Multi-year deal; nearly 1 GW of capacity by year-end 2026
- **Microsoft:** $30 billion Azure commitment; [early-stage Maia 200 talks](https://chatforest.com/reviews/anthropic-microsoft-maia-200-azure-claude-inference-chip-talks-2026/)

A Samsung-manufactured custom chip would sit on top of this stack — potentially used for the highest-volume, most-optimized inference workloads where Anthropic knows exactly what Claude is doing and can co-design hardware for it.

## The IPO Timing

Anthropic is reportedly preparing an S-1 for an IPO as early as October 2026. A custom chip program — even at the discussion stage — strengthens the infrastructure independence narrative that investors evaluating a company at near-trillion-dollar valuation want to see. Dependence on a small number of chip suppliers is a supply chain risk; diversification, including toward proprietary silicon, reduces it.

Whether the Samsung talks are primarily driven by operational need, IPO narrative-building, or both is hard to judge from outside. But the timing — immediately following the Samsung investment in May and ahead of a potential S-1 filing — is notable.

## Bottom Line

Anthropic's custom chip talks are nascent and may not result in a chip. But the Clive Chan hire signals real intent: you don't recruit the second-ever engineer from OpenAI's chip team to explore a hypothetical. Samsung is a credible 2nm manufacturing partner with an existing financial stake in Anthropic's success. OpenAI's Jalapeño has demonstrated that inference-specific silicon can deliver meaningful cost advantages for frontier labs.

The relevant question isn't whether Anthropic will eventually build its own chip — it almost certainly will — but whether it can execute before its per-token cost disadvantage compounds further relative to OpenAI.

---

## Sources
- [TechCrunch: Anthropic in talks with Samsung for custom chip (July 2, 2026)](https://techcrunch.com/2026/07/02/anthropic-is-discussing-a-new-custom-chip-with-samsung/)
- [Bloomberg: Anthropic-Samsung chip talks confirmed (July 2, 2026)](https://www.bloomberg.com/news/articles/2026-07-02/anthropic-in-talks-with-samsung-for-custom-ai-chip-information-mr3l34t4)
- [TechTimes: Clive Chan hire and 2nm process details](https://www.techtimes.com/articles/319574/20260702/anthropic-talks-samsung-build-custom-ai-chip-aiming-2nm-process.htm)
- [MLQ.ai: Samsung in Anthropic's $65B May 2026 fundraise](https://mlq.ai/news/anthropic-in-early-talks-with-samsung-to-manufacture-custom-ai-chip-on-2nm-process/)
- [Korea Herald: Samsung chip division strategic view](https://www.koreaherald.com/article/10797311)
- [Dataconomy: Early talks and Samsung 2nm context](https://dataconomy.com/2026/07/03/anthropic-explores-samsung-partnership-to-develop-custom-ai-chips/)
