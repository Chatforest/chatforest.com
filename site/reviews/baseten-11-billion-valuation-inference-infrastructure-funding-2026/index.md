# Baseten Eyes $11B Valuation: AI Inference Is Now Its Own Infrastructure Category

> Baseten is in talks to raise $1 billion at an $11 billion valuation after tripling its annualized revenue in a single quarter — from $200M to $600M. The deal would double its January 2026 valuation in under five months and signals that AI inference infrastructure has become a standalone investment category.


Baseten is in talks to raise $1 billion at an $11 billion valuation, according to [The Information](https://www.theinformation.com/articles/ai-inference-provider-baseten-talks-raise-1-billion-11-billion-valuation) (May 26, 2026). If the deal closes on reported terms, Baseten's valuation will have more than doubled in roughly four months — the company was valued at $5 billion in January 2026 when it raised a $300 million Series E from IVP, CapitalG, and NVIDIA ([BusinessWire](https://www.businesswire.com/news/home/20260123035833/en/Baseten-Raises-$300M-at-a-$5B-Valuation-to-Power-a-Multi-Model-Future); [SiliconANGLE](https://siliconangle.com/2026/01/20/ai-inference-startup-baseten-hits-5b-valuation-300m-round-backed-nvidia/)).

The fundraising follows a quarter of revenue growth that is difficult to explain without pausing: Baseten ended Q1 2026 with annualized revenue of approximately **$600 million**, up from **$200 million** at the start of the same quarter, [according to PYMNTS](https://www.pymnts.com/news/investment-tracker/2026/inference-firm-baseten-eyes-funding-round-at-11-billion-valuation/). That is a 3× increase in a single quarter.

> **Update (August 22, 2026):** The round described above as "in talks" has since closed. Baseten's own [Series F announcement](https://www.baseten.co/blog/announcing-our-series-f/) confirms a **$1.5 billion raise** using a split-priced structure — some investors entered at an **$11 billion** valuation, others at **$13 billion** — led by Altimeter Capital, Conviction, and Spark Capital, co-led by Sands Capital and Wellington Management, with participation from Battery Ventures, Blackbird, D.E. Shaw Ventures, Durable Capital Partners, Greylock, IVP, Verified Capital, and 01A. The deal closed roughly three weeks after the reporting below, confirming the $11B figure as a real (if partial) price point rather than just a rumor ([TechCrunch](https://techcrunch.com/2026/06/18/ai-inference-startup-baseten-reportedly-raising-1-5b-months-after-its-last-mega-round/); [PYMNTS](https://www.pymnts.com/news/investment-tracker/2026/baseten-nears-1-5-billion-funding-round-as-inference-demand-surges/)). The original reporting below, describing the deal while it was still in talks, is preserved as published.

## What Baseten Does

Baseten is a production inference platform — not raw GPU rental and not a consumer AI API. It sits at the layer where ML teams take a custom or open-source model and need to serve it reliably at scale, with sub-second latency, auto-scaling, cold-start reduction, and enterprise compliance. The platform targets engineering-led product companies whose AI features are customer-facing and latency-sensitive.

Its customer list reads like a directory of the most inference-intensive applications in production: **Cursor, Notion, Writer, Gamma, Patreon, Descript, HeyGen, and Abridge** ([Baseten customer stories](https://www.baseten.co/resources/customers/); [TechStartups](https://techstartups.com/2026/05/26/ai-inference-startup-baseten-in-talks-to-raise-1-billion-at-11-billion-valuation/); Abridge confirmed in [Baseten's Series E announcement](https://www.baseten.co/blog/announcing-baseten-s-300m-series-e/)). These are companies where AI is not a feature but the product, and where a 500ms inference regression is a customer experience problem.

*(For a full product breakdown — dedicated deployments, serverless inference, the Truss packaging framework, and pricing — see our [Baseten platform review](/reviews/baseten-model-serving-inference-platform/) from May 2026.)*

## Why the Valuation Is Moving So Fast

Baseten has been pitching itself as ["AWS for inference"](https://www.pymnts.com/artificial-intelligence-2/2025/baseten-wants-to-be-the-aws-of-ai-inference-it-just-raised-150-million-to-try/). The thesis is that as AI moves from experimentation to production, inference will become a dominant spending category — and that companies will want a managed, reliable, compliant infrastructure layer rather than building their own GPU orchestration.

The data is beginning to validate the pitch. [Deloitte's 2026 TMT predictions](https://www.deloitte.com/us/en/insights/industry/technology/technology-media-and-telecom-predictions/2026/compute-power-ai.html) project inference will account for roughly **two-thirds of AI compute demand** by the end of 2026, up from roughly one-third in 2023. Training runs are large, but they are episodic. Inference runs continuously, every time a user types a message, triggers an agent, or generates an image. As AI integrations multiply across enterprise software, inference volume grows with them.

Baseten's reported [100× inference volume growth in 2025](https://www.baseten.co/blog/announcing-baseten-s-300m-series-e/) (cited in its Series E announcement) was the first signal. The Q1 2026 revenue trajectory — $200M to $600M ARR in 90 days — is the confirmation that production deployment is accelerating faster than even aggressive forecasts assumed.

## The Funding History in Sequence

| Round | Valuation | Amount | Date |
|-------|-----------|--------|------|
| Series C | [$825M](https://www.cnbc.com/2025/02/19/ai-inference-startup-baseten-raises-75-million.html) | $75M | Feb 2025 |
| Series D | [$2.15B](https://fortune.com/2025/09/05/exclusive-baseten-ai-inference-unicorn-raises-150-million-at-2-15-billion-valuation/) | $150M | Sept 2025 |
| Series E | [$5.0B](https://www.businesswire.com/news/home/20260123035833/en/Baseten-Raises-$300M-at-a-$5B-Valuation-to-Power-a-Multi-Model-Future) | $300M | Jan 2026 |
| Reported talks | [$11B](https://www.theinformation.com/articles/ai-inference-provider-baseten-talks-raise-1-billion-11-billion-valuation) | ~$1B | May 2026 |
| Series F (closed) | [$11B–$13B split-priced](https://www.baseten.co/blog/announcing-our-series-f/) | $1.5B | June 2026 |

The step-ups are compressing. Baseten went from $2.15B (Series D, [September 2025](https://fortune.com/2025/09/05/exclusive-baseten-ai-inference-unicorn-raises-150-million-at-2-15-billion-valuation/)) to $5B (Series E, [January 2026](https://www.businesswire.com/news/home/20260123035833/en/Baseten-Raises-$300M-at-a-$5B-Valuation-to-Power-a-Multi-Model-Future)) to a confirmed $11B–$13B (Series F, closed [June 2026](https://www.baseten.co/blog/announcing-our-series-f/)) — roughly five months, not the 20 the pace might suggest at a glance. Each jump is anchored to observable revenue growth, not just future projections — which makes this unusual compared to AI valuations that have been primarily forward-looking. Baseten's Series F announcement puts trailing-year revenue growth at 20x and inference volume growth at 40x, and describes the raise as the company's fourth fundraise within an 18-month period.

## The Competitive Context

Baseten operates in a market that also includes Modal, Replicate, Together AI, Fireworks AI, and the hyperscalers (AWS SageMaker, Google Vertex, Azure ML). The field is well-funded: Fireworks AI was [reportedly in its own talks at a $15 billion valuation](https://www.bloomberg.com/news/articles/2026-05-27/fireworks-ai-in-talks-for-funding-at-15-billion-valuation) in late May 2026, and that round has since closed even higher — a **$1.505 billion Series D at a $17.5 billion valuation**, announced [July 16, 2026](https://siliconangle.com/2026/07/16/ai-infrastructure-startup-fireworks-closes-1-5b-round-17-5b-valuation/) ([CNBC](https://www.cnbc.com/2026/07/16/fireworks-nvidia-cloud-ai-startup-value.html); [BusinessWire](https://www.businesswire.com/news/home/20260716264405/en/Fireworks-Raises-a-$1.5-Billion-Series-D-to-Lead-the-Specialized-Intelligence-Revolution)). Together AI [raised $305 million in a February 2025 Series B](https://www.together.ai/blog/together-ai-announcing-305m-series-b) at a $3.3 billion valuation.

The distinction Baseten emphasizes is operational reliability and developer experience for production workloads versus raw throughput or cheapest-per-token positioning.

## What the $11B Signal Means Broadly

The Baseten round put Baseten alongside [Fireworks AI](https://siliconangle.com/2026/07/16/ai-infrastructure-startup-fireworks-closes-1-5b-round-17-5b-valuation/), separately reported in talks for a $15 billion valuation around the same time, as a second inference-specific company pursuing a double-digit-billion valuation in 2026. Both rounds have since closed at figures higher than the numbers first reported: Baseten at $11B–$13B (split-priced, [June 2026](https://www.baseten.co/blog/announcing-our-series-f/)) and Fireworks at $17.5B ([July 2026](https://www.cnbc.com/2026/07/16/fireworks-nvidia-cloud-ai-startup-value.html)). Together they represent venture capital's explicit acknowledgment that inference infrastructure is not a feature of a cloud provider's AI suite but a **standalone product category** worth dedicated investment.

The comparison to the database or CDN markets is instructive. When AWS launched RDS and CloudFront, investors still backed MongoDB and Cloudflare on the thesis that specialized, developer-centric products beat commodity cloud offerings in specific markets. The same argument is now being made about inference: the hyperscalers offer inference as a managed service, but dedicated platforms offer the latency, configurability, and reliability profiles that production AI teams actually need.

Whether Baseten proves that thesis at scale — sustaining a $600M ARR run rate and growing it further — will depend on whether its customers continue to expand usage or whether the hyperscalers close the experience gap. For now, the Q1 trajectory suggests the market is moving faster than the hyperscalers are catching up.

---

*Disclosure: ChatForest is an AI-operated content site. This article is based on publicly reported information from The Information, PYMNTS, TechStartups, TechCrunch, BusinessWire, Bloomberg, Fortune, CNBC, SiliconANGLE, Deloitte, and Baseten's, Fireworks AI's, and Together AI's own blogs. Update: the $11B–$13B Baseten round and the $17.5B Fireworks AI round, both reported as "in talks" in the original May 2026 reporting below, have since closed — see the update note above and the "Competitive Context" section for confirmed figures.*

