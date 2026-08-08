# Anthropic Is in Talks With Samsung to Build Its First Custom AI Chip

> Anthropic is in early-stage discussions with Samsung to manufacture a custom 2nm AI accelerator — and hired the second engineer ever to join OpenAI's Jalapeño chip team to lead it. What the talks reveal about AI infrastructure strategy heading into Anthropic's IPO.


**At a glance:** Anthropic is in early-stage talks with Samsung Electronics to manufacture a custom AI chip, targeting Samsung's 2nm process — first reported by [The Information on July 2, 2026](https://finance.yahoo.com/technology/ai/articles/anthropic-explores-samsung-2nm-chip-144844786.html) and covered the same day by [TechCrunch](https://techcrunch.com/2026/07/02/anthropic-is-discussing-a-new-custom-chip-with-samsung/) and [Bloomberg](https://www.bloomberg.com/news/articles/2026-07-02/anthropic-in-talks-with-samsung-for-custom-ai-chip-information-mr3l34t4), both of which credit The Information rather than reporting independently. No design, target workload, or specifications have been finalized. Anthropic has [hired Clive Chan](https://finance.yahoo.com/technology/ai/articles/anthropic-explores-samsung-2nm-chip-144844786.html), the second engineer ever to join OpenAI's custom chip team.

---

For three years, Anthropic has run Claude on other companies' chips — Google TPUs, Amazon Trainium, Nvidia GPUs through CoreWeave and direct contracts. That posture is beginning to shift.

[The Information reported July 2](https://finance.yahoo.com/technology/ai/articles/anthropic-explores-samsung-2nm-chip-144844786.html) that Anthropic is in early discussions with Samsung Electronics about manufacturing a custom AI accelerator, aiming at Samsung's 2-nanometer process node. [TechCrunch](https://techcrunch.com/2026/07/02/anthropic-is-discussing-a-new-custom-chip-with-samsung/) and [Bloomberg](https://www.bloomberg.com/news/articles/2026-07-02/anthropic-in-talks-with-samsung-for-custom-ai-chip-information-mr3l34t4) both picked up the story the same day — both explicitly credit The Information as the source rather than reporting it independently, so this remains, at its core, a single-sourced report. What moves it past pure rumor is that Anthropic itself did not deny it: the company [gave The Information an on-record statement](https://finance.yahoo.com/technology/ai/articles/anthropic-explores-samsung-2nm-chip-144844786.html) about the talks (quoted below). Early-stage means exactly that: no chip design has been started, no target workload has been selected, and no performance specifications exist. Anthropic may not proceed. But the combination of an active hire and a manufacturing partner conversation signals a direction the company is taking seriously.

## The Clive Chan Hire

The clearest evidence that Anthropic's chip ambitions are more than exploratory is the Clive Chan hire. [TechTimes reported](https://www.techtimes.com/articles/319574/20260702/anthropic-talks-samsung-build-custom-ai-chip-aiming-2nm-process.htm), and [The Information's reporting](https://finance.yahoo.com/technology/ai/articles/anthropic-explores-samsung-2nm-chip-144844786.html) separately confirms, that Chan was the second engineer ever to join OpenAI's dedicated custom chip team — the group that spent two and a half years building "Jalapeño," the Broadcom-designed inference accelerator [OpenAI and Broadcom unveiled on June 24, 2026](https://techcrunch.com/2026/06/24/openai-unveils-its-first-custom-chip-built-by-broadcom/).

Chan's background is specifically in inference chip design for large language models — exactly the workload Anthropic needs to optimize. Inference (running model queries against live user traffic) is where most of Anthropic's compute cost lives. Training uses compute for weeks or months at a time during development; inference runs continuously at scale as long as users and API customers are active. A chip purpose-built for Claude inference would have a fundamentally different design target than a general-purpose GPU.

## What Samsung Brings

Samsung's 2-nanometer process node is the technology Samsung is using to challenge TSMC's dominance in leading-edge chip fabrication. For reference:

- TSMC's [3nm process (N3E) powers Apple's M4 chips](https://www.techinsights.com/blog/introducing-tsmc-n3e-seen-apple-m4-soc); Nvidia's Blackwell GPUs use a related but distinct [TSMC 4nm-class node (4NP)](https://en.wikipedia.org/wiki/Blackwell_(microarchitecture)), not 3nm
- Samsung's 2nm process began mass production for mobile applications in 2025; its AI/HPC-targeted variant (SF2X) is [slated for 2026, with an automotive variant (SF2A) targeted for 2027](https://www.sammobile.com/news/samsung-2nm-mobile-chips-process-node-ready-2025-1-4nm-2027/)
- Samsung has advanced packaging capabilities — it [ships commercial HBM4 memory with 12-layer stacking and "extensive in-house expertise in advanced packaging"](https://semiconductor.samsung.com/news-events/news/samsung-ships-industry-first-commercial-hbm4-with-ultimate-performance-for-ai-computing/) — and [SamMobile separately reports Samsung is in talks to make 2nm AI chips for both Anthropic and Meta](https://www.sammobile.com/2026/07/04/samsung-talks-make-2nm-ai-chips-anthropic-meta/)

Critically, Samsung already has a financial relationship with Anthropic. Samsung participated in [Anthropic's $65 billion fundraising round in May 2026](https://mlq.ai/news/anthropic-in-early-talks-with-samsung-to-manufacture-custom-ai-chip-on-2nm-process/), alongside SK Hynix and Micron, at a valuation of [$965 billion](https://www.forbes.com/sites/gabrielalinzainescu/2026/05/29/anthropic-just-raised-65-billion-the-investors-who-matter-most-make-memory-chips/). [The Korea Herald reported](https://www.koreaherald.com/article/10797311) that Samsung's chip and memory divisions see Anthropic as a strategic customer worth deepening ties with beyond just investment.

## The OpenAI Jalapeño Context

OpenAI's Jalapeño chip — designed with Broadcom, [unveiled June 24, 2026](https://techcrunch.com/2026/06/24/openai-unveils-its-first-custom-chip-built-by-broadcom/) — is the immediate reference point for what a custom LLM inference chip looks like from a US frontier lab. Jalapeño is optimized specifically for running large language models more efficiently than commodity GPUs; [OpenAI says early testing shows significantly higher inference performance per watt than current state-of-the-art hardware](https://techcrunch.com/2026/06/24/openai-unveils-its-first-custom-chip-built-by-broadcom/), though it has not published a specific multiplier.

The competitive logic for Anthropic is straightforward: if OpenAI is reducing per-token inference cost through a custom chip while Anthropic continues buying Nvidia GPU time at market rates, Anthropic's margin disadvantage compounds over time. A custom chip isn't a shortcut — the development timeline is typically two to three years from design to volume production — but it is a structural cost lever that compounds in the opposite direction once deployed.

The competitive landscape among frontier labs on custom silicon:

| Lab | Chip program | Status |
|-----|-------------|--------|
| Google | TPU (v1–v7) | [Publicly unveiled 2016](https://thechipletter.substack.com/p/googles-first-tensor-processing-unit), production ongoing |
| Amazon | Trainium (training), Inferentia (inference) | [Production, AWS-only](https://www.anthropic.com/news/anthropic-amazon-compute) |
| Microsoft | Maia 200 | [Launched January 2026](https://news.microsoft.com/source/emea/2026/01/microsoft-introduces-maia-200-new-inference-accelerator-enhances-ai-performance-in-azure/) |
| OpenAI | Jalapeño (Broadcom-designed) | [Unveiled June 24, 2026](https://techcrunch.com/2026/06/24/openai-unveils-its-first-custom-chip-built-by-broadcom/) |
| Anthropic | Unnamed (Samsung talks) | Early-stage, unconfirmed |

Anthropic is the last major US AI frontier lab without its own silicon program in place.

## What Anthropic Said

Anthropic confirmed the Samsung discussions without additional detail and [gave The Information a statement](https://finance.yahoo.com/technology/ai/articles/anthropic-explores-samsung-2nm-chip-144844786.html) reiterating that "Amazon Web Services's Trainium chip, Google tensor processing units and Nvidia graphic processors will remain central to how the company scales its compute strategy." The custom chip, if it proceeds, would be additive — a new option for specific inference workloads rather than a replacement for existing infrastructure commitments.

This is consistent with how every major AI lab has approached custom silicon: not as a full infrastructure replacement, but as a cost-optimization layer for high-volume, well-characterized workloads where model architecture and hardware can be co-designed together.

Anthropic's existing compute commitments are already extensive:

- **Google Cloud:** [reportedly $200 billion committed over five years](https://winbuzzer.com/2026/05/06/anthropic-reportedly-agrees-to-pay-google-200-bill-xcxwbn/) (The Information, May 2026 — neither Google nor Anthropic has confirmed the dollar figure); separately, [Anthropic's confirmed Google/Broadcom TPU expansion](https://www.anthropic.com/news/google-broadcom-partnership-compute) brings multiple gigawatts of next-generation TPU capacity online starting 2027
- **Amazon Web Services:** [More than $100 billion committed over ten years](https://www.anthropic.com/news/anthropic-amazon-compute), securing up to 5 GW of capacity, including nearly 1 GW of Trainium2/Trainium3 capacity by year-end 2026
- **CoreWeave:** [Multi-year deal reported at $6.8 billion](https://www.financialcontent.com/article/marketminute-2026-4-10-the-great-gpu-landgrab-coreweave-secures-68-billion-agreement-with-anthropic-as-the-ai-infrastructure-arms-race-hits-fever-pitch); [CoreWeave's own announcement](https://www.coreweave.com/news/coreweave-announces-multi-year-agreement-with-anthropic) does not disclose a dedicated capacity figure for the Anthropic deal specifically
- **Microsoft:** [$30 billion Azure commitment](https://www.anthropic.com/news/microsoft-nvidia-anthropic-announce-strategic-partnerships); [early-stage Maia 200 talks](https://chatforest.com/reviews/anthropic-microsoft-maia-200-azure-claude-inference-chip-talks-2026/)

A Samsung-manufactured custom chip would sit on top of this stack — potentially used for the highest-volume, most-optimized inference workloads where Anthropic knows exactly what Claude is doing and can co-design hardware for it.

## The IPO Timing

Anthropic [reportedly filed a confidential S-1](https://futurumgroup.com/insights/anthropic-files-for-ipo-looking-to-beat-openai-to-the-punch/) with the SEC and is said to be targeting a public listing as early as October 2026. A custom chip program — even at the discussion stage — strengthens the infrastructure independence narrative that investors evaluating a company at near-trillion-dollar valuation want to see. Dependence on a small number of chip suppliers is a supply chain risk; diversification, including toward proprietary silicon, reduces it.

Whether the Samsung talks are primarily driven by operational need, IPO narrative-building, or both is hard to judge from outside. But the timing — immediately following the Samsung investment in May and ahead of a potential S-1 filing — is notable.

## Bottom Line

Anthropic's custom chip talks are nascent and may not result in a chip. But the Clive Chan hire signals real intent: you don't recruit the second-ever engineer from OpenAI's chip team to explore a hypothetical. Samsung is a credible 2nm manufacturing partner with an existing financial stake in Anthropic's success. OpenAI's Jalapeño has demonstrated that inference-specific silicon can deliver meaningful cost advantages for frontier labs.

The relevant question isn't whether Anthropic will eventually build its own chip — it almost certainly will — but whether it can execute before its per-token cost disadvantage compounds further relative to OpenAI.

---

## Sources
- [The Information (via Yahoo Finance): Anthropic explores Samsung 2nm chip partnership — original scoop, Clive Chan detail, Anthropic's on-record statement (July 2, 2026)](https://finance.yahoo.com/technology/ai/articles/anthropic-explores-samsung-2nm-chip-144844786.html)
- [TechCrunch: Anthropic in talks with Samsung for custom chip, citing The Information (July 2, 2026)](https://techcrunch.com/2026/07/02/anthropic-is-discussing-a-new-custom-chip-with-samsung/)
- [Bloomberg: Anthropic in talks with Samsung for custom AI chip, citing The Information (July 2, 2026)](https://www.bloomberg.com/news/articles/2026-07-02/anthropic-in-talks-with-samsung-for-custom-ai-chip-information-mr3l34t4)
- [TechTimes: Clive Chan hire and 2nm process details](https://www.techtimes.com/articles/319574/20260702/anthropic-talks-samsung-build-custom-ai-chip-aiming-2nm-process.htm)
- [TechCrunch: OpenAI unveils Jalapeño, its first custom chip built with Broadcom (June 24, 2026)](https://techcrunch.com/2026/06/24/openai-unveils-its-first-custom-chip-built-by-broadcom/)
- [MLQ.ai: Samsung in Anthropic's $65B May 2026 fundraise](https://mlq.ai/news/anthropic-in-early-talks-with-samsung-to-manufacture-custom-ai-chip-on-2nm-process/)
- [Forbes: Anthropic's $65B round and $965B valuation, with Samsung/SK Hynix/Micron as investors (May 29, 2026)](https://www.forbes.com/sites/gabrielalinzainescu/2026/05/29/anthropic-just-raised-65-billion-the-investors-who-matter-most-make-memory-chips/)
- [Korea Herald: Samsung chip division strategic view](https://www.koreaherald.com/article/10797311)
- [SamMobile: Samsung's SF2/SF2X/SF2A 2nm process roadmap (mobile 2025, AI/HPC 2026, automotive 2027)](https://www.sammobile.com/news/samsung-2nm-mobile-chips-process-node-ready-2025-1-4nm-2027/)
- [SamMobile: Samsung in talks to make 2nm AI chips for Anthropic and Meta](https://www.sammobile.com/2026/07/04/samsung-talks-make-2nm-ai-chips-anthropic-meta/)
- [Samsung Semiconductor: commercial HBM4 shipment and advanced packaging capabilities](https://semiconductor.samsung.com/news-events/news/samsung-ships-industry-first-commercial-hbm4-with-ultimate-performance-for-ai-computing/)
- [Anthropic: Amazon compute expansion, >$100B/10yr, up to 5GW](https://www.anthropic.com/news/anthropic-amazon-compute)
- [Anthropic: Google/Broadcom TPU capacity expansion starting 2027](https://www.anthropic.com/news/google-broadcom-partnership-compute)
- [Anthropic: Microsoft/Nvidia strategic partnership, $30B Azure commitment](https://www.anthropic.com/news/microsoft-nvidia-anthropic-announce-strategic-partnerships)
- [Winbuzzer: Anthropic's reported (unconfirmed) $200B/5yr Google Cloud commitment, per The Information](https://winbuzzer.com/2026/05/06/anthropic-reportedly-agrees-to-pay-google-200-bill-xcxwbn/)
- [FinancialContent: CoreWeave's $6.8B multi-year Anthropic deal](https://www.financialcontent.com/article/marketminute-2026-4-10-the-great-gpu-landgrab-coreweave-secures-68-billion-agreement-with-anthropic-as-the-ai-infrastructure-arms-race-hits-fever-pitch)
- [CoreWeave: official announcement of the Anthropic agreement](https://www.coreweave.com/news/coreweave-announces-multi-year-agreement-with-anthropic)
- [Microsoft: Maia 200 launch announcement (January 26, 2026)](https://news.microsoft.com/source/emea/2026/01/microsoft-introduces-maia-200-new-inference-accelerator-enhances-ai-performance-in-azure/)
- [The Chip Letter: Google's first Tensor Processing Unit, publicly unveiled at Google I/O 2016](https://thechipletter.substack.com/p/googles-first-tensor-processing-unit)
- [TechInsights: TSMC N3E (3nm) process in Apple's M4](https://www.techinsights.com/blog/introducing-tsmc-n3e-seen-apple-m4-soc)
- [Wikipedia: Nvidia Blackwell architecture, fabricated on TSMC's 4NP (4nm-class) node](https://en.wikipedia.org/wiki/Blackwell_(microarchitecture))
- [Futurum Group: Anthropic's confidential S-1 filing and October 2026 IPO target](https://futurumgroup.com/insights/anthropic-files-for-ipo-looking-to-beat-openai-to-the-punch/)

