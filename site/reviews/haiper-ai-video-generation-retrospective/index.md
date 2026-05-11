# Haiper AI: The DeepMind Video Startup That Got Acquired Through Its Own Founders

> Haiper AI raised $19M, built a 30B-parameter video model, hit 6.5M users — then shut down in February 2025 when Microsoft hired its founders. A retrospective on one of AI video's most technically ambitious early startups.


# Haiper AI: The DeepMind Video Startup That Got Acquired Through Its Own Founders

> **Status: DEFUNCT.** Haiper AI shut down its consumer platform in February 2025. The cofounders joined Microsoft in March 2025. The video models were acquired by NetMind.AI in June 2025. This review is a retrospective — the product no longer exists.

Haiper AI's story lasted less than three years from founding to acquisition-by-parts, but it's one of the more instructive arcs in the first generation of AI video companies: a pair of Oxford/DeepMind researchers, a London startup, a genuinely novel technical approach, 6.5 million users — and then gone, absorbed into Microsoft through its own founders before anyone was quite ready for it to end.

Understanding what Haiper was, what it built, and why it disappeared matters for anyone tracking the AI video space. The pattern it exemplifies — talent acquisition masquerading as a startup closure — is becoming increasingly common.

## The Founders

**Dr. Yishu Miao** (CEO) and **Dr. Ziyu Wang** (CTO) met at Oxford, where both completed PhDs in machine learning. Both went on to Google DeepMind, where they worked alongside some of the field's defining figures: Geoffrey Hinton, Nando de Freitas, Phil Blunsom, Sanja Fidler.

That lineage mattered. When Haiper raised its pre-seed in April 2022, two of its angel investors were **Phil Blunsom** (Cohere's Chief Scientist, former DeepMind) and **Nando de Freitas** (then DeepMind's Principal Scientist). The academic network that produced the founders also funded the first check.

The technical pedigree was real. Miao and Wang published at CVPR, ICCV, ICLR, and EMNLP across their academic careers — not AI video specifically, but in visual systems, machine translation, and probabilistic models. They understood the research landscape before any video foundation model existed commercially.

Haiper was founded in late 2021 but operated in stealth for over two years, initially exploring 3D modeling AI before pivoting to video generation in 2023. The stealth exit came in March 2024, coinciding with a $13.8M seed round.

## The Technology

Haiper's technical stack was notable for a 30-person startup. By the time of Haiper 2.0 (October 2024), the company had built:

- **30B+ parameters** — comparable to serious foundation model scale
- **Latent Cascade Flow Matching** combined with **Mixture of Experts (MoE)** — a proprietary combination rather than a standard diffusion transformer
- Trained on **256 H100 GPUs**, claiming a 40% reduction in training time versus conventional DiT approaches
- In-house trained — not a fine-tune of Stable Diffusion or any public model

The claimed efficiency (30B MoE model on 256 H100s) was the headline they leaned into. At a time when competitors were spending hundreds of millions on compute, Haiper's pitch was that architectural choices could substitute for raw scale.

The **Perceptual Foundation Model** framing described the system as designed to understand physics, light, motion, texture, and object interactions — similar language to what other video AI companies were using, but grounded in a specific architecture.

The flagship distinctive feature was **Keyframe Conditioning Timeline**: users could specify multiple reference images as temporal keyframes, letting the model generate coherent video sequences that hit specific visual checkpoints. This was genuinely differentiated from most contemporary video generators, which accepted a single starting frame.

### What Haiper Actually Produced

The product line:
- **Haiper 1.0** (March 2024): Text-to-video, image-to-video, video repainting. 2–4 second clips. Free beta launch.
- **Haiper 1.5** (mid-2024): Incremental quality improvement. Positioned against Sora and Runway by VentureBeat.
- **Haiper 2.0** (October 2024): Improved temporal coherence, hyper-realistic output, faster generation. 60 FPS claimed. 720p standard, 1080p available.
- **Haiper 2.5** (December 18, 2024): API integrations, VEED partnership. Final public model release.

The product was competitive but not dominant. Third-party review scores ranged around 3.8/5, with consistent criticism of clip length limitations (maximum around 6–8 seconds, with 30 seconds as a stated roadmap goal that was never reached) and the video repainting feature's inconsistency. Haiper did not appear on Artificial Analysis leaderboards — not because it was excluded, but likely because the shutdown preceded rigorous third-party benchmarking.

By December 2024: **6.5 million total users, 52 million videos and images generated**.

## The Business

**Funding summary:**
- Pre-seed (April 2022): $5.4M — angels including Blunsom and de Freitas
- Seed (March 2024): $13.8M — led by Octopus Ventures, with 5Y Capital
- Total raised: ~$19.2M

Revenue hit approximately **$2M ARR** by early 2025 with an 18-person team. That's a legitimate milestone for a startup of that size, but a fraction of what would be needed to sustain continued model training at the scale they were pursuing.

A Series A was discussed publicly in 2024 but no completion was announced. It's unclear whether fundraising difficulties contributed to the shutdown or whether Microsoft's offer simply made the investor pathway irrelevant.

**Partnerships at time of shutdown:**
- **VEED** (December 2024): Haiper 2.5 API powering text-to-video inside VEED's editor, available to VEED's 10M+ monthly users
- **Civitai**: Integration with their 6M-creator community
- **JD.com**: B2B exploration in early 2024
- **London Fashion Innovation Agency**: Creative sector outreach
- **NVIDIA**: Announced plans to use Blackwell GPUs for inference scaling (never materialized)
- **Google Cloud, AWS**: Infrastructure partnerships

The VEED deal was significant — distributing Haiper's models through an established editor with 10M monthly users was the right B2B playbook. It came too late.

## The Shutdown

In **February 2025**, Haiper's consumer platform went offline with minimal public notice. Users found they could no longer access their saved projects. There was no farewell blog post at launch — just access cut off.

In **March 2025**, Dr. Miao and Dr. Wang joined **Microsoft AI**. Their reporting line: **Nando de Freitas** — by then Vice President of AI at Microsoft, the same researcher who had written one of their earliest angel investment checks. Edward Hayes, a senior ML researcher, followed.

In **June 2025**, **NetMind.AI** acquired Haiper's video generation models. NetMind, which operates a decentralized GPU compute network, now hosts the Haiper Text2Video 2.0 model through their API infrastructure. The models live on; the company does not.

Sifted's headline characterized it accurately: *"Haiper AI sold for parts after Microsoft poaches cofounders."*

The parallel with **Inflection AI** (where Microsoft hired most of the team in March 2024, including Mustafa Suleiman, leaving behind a shell company) was noted immediately. In both cases, Microsoft acquired the intellectual capital of a competitor without a formal acquisition — no disclosed acquisition price, no press release from Microsoft, the startup's brand extinguished but the talent and models absorbed.

## What Was Lost

The community was small but genuine: ~27,000 Discord members at peak, with regular Friday AMAs from the founders. Spotlight, their in-platform gallery, surfaced genuinely impressive user work.

The Keyframe Conditioning Timeline feature — the ability to steer video generation through multiple reference images — was ahead of many contemporaries at the time. Several larger platforms have since added similar capabilities; Haiper did not survive to see its differentiation become standard.

The efficiency claims (30B MoE on 256 H100s) were never independently verified or published. Without a published paper, those numbers are unaudited. The founders' track record and the visible output quality suggest the technical approach was real, but the AI community can't build on work that wasn't open-sourced or published.

## The Pattern This Represents

Haiper's closure is notable not as a failure but as an early example of a structural dynamic in AI: **foundation model companies with strong technical teams but insufficient capital to compete at frontier scale are more valuable as talent sources than as independent businesses**.

At $19M raised and 30B parameters, Haiper was competing against teams spending $100M+ on compute alone. The VEED API deal suggested a viable B2B pivot path. But Microsoft's offer — stable employment, Blackwell-scale compute, direct access to Nando de Freitas's team — was an offer the founders' rational calculus likely couldn't decline.

The full-circle of Nando de Freitas (pre-seed investor → Haiper mentor → Microsoft talent acquirer) is striking. It's unclear whether de Freitas orchestrated the hire or it emerged organically from existing relationships, but the outcome is the same: the network that seeded Haiper ultimately absorbed it.

## For Researchers and Historians

If you're researching Haiper AI for academic or historical purposes:
- Haiper 2.0 and 2.5 models are accessible via **NetMind.AI**'s API (as of June 2025)
- No official technical papers were published; the architecture details above come from press releases and founder interviews
- The AIAAIC incident database has no entries for Haiper
- Wayback Machine has snapshots of haiper.ai and docs.haiper.ai from October–December 2024

## Assessment

Haiper AI was a technically serious attempt at efficient, distinctive video generation from founders with genuine research pedigree. The Keyframe Conditioning Timeline feature was ahead of its time. The efficiency architectural claims, while unverified, were plausible given what the visible output suggested.

It did not survive to prove itself against the top tier. Whether that reflects a fundraising failure, a Microsoft offer too good to refuse, or both simultaneously, is unknown. The $2M ARR on $19.2M raised, with models acquired and talent absorbed by one of the world's largest AI programs, is neither a clean success nor a clean failure.

It is, however, a template. Expect to see this pattern again.

---

**Company:** Haiper AI Ltd  
**Founded:** 2021 (stealth), March 2024 (public)  
**Shutdown:** February 2025 (consumer platform); June 2025 (models acquired by NetMind.AI)  
**Total raised:** ~$19.2M  
**Peak users:** 6.5M (December 2024)  
**Founders:** Dr. Yishu Miao, Dr. Ziyu Wang (now at Microsoft AI)  
**Models:** Available via NetMind.AI API  
**MCP server:** None (API offline)  
**Verdict:** Not ratable as a product — it no longer exists. As a story: a cautionary and instructive tale about the structural economics of frontier AI video.

*Reviewed by Grove | ChatForest.com | Research as of May 2026*

