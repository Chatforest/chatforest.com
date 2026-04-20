# The AI Scientist-v2 Just Passed Peer Review — And 21% of the Reviews Were Written by AI Too

> Sakana AI's AI Scientist-v2 produced the first fully AI-generated paper to pass peer review at an ICLR workshop — an end-to-end system that generates hypotheses, runs experiments, and writes papers for $20-25 each. Published in Nature. But the celebration landed in an awkward context: analysis revealed 21% of ICLR 2026 peer reviews were fully AI-generated, with over half showing some AI involvement. AI is now writing the science and reviewing it. This is the story of automated research crossing a threshold — and the integrity crisis that arrived at the same time.


A paper written entirely by AI just [passed peer review](https://sakana.ai/ai-scientist-first-publication/) at a major machine learning conference. No human wrote any of it — not the hypothesis, not the experiments, not the analysis, not the manuscript. The system that produced it costs about [$20 per paper](https://github.com/SakanaAI/AI-Scientist-v2).

[Sakana AI](https://sakana.ai/)'s AI Scientist-v2 is an [end-to-end agentic system](https://arxiv.org/abs/2504.08066) that autonomously generates research ideas, searches literature, designs and runs experiments, analyzes results, and writes complete scientific papers. One of its papers was [accepted at an ICLR 2025 workshop](https://sakana.ai/ai-scientist-first-publication/), and the broader work has been [published in Nature](https://sakana.ai/ai-scientist-nature/).

But the milestone landed in a complicated context. Weeks later, [analysis of ICLR 2026](https://www.pangram.com/blog/pangram-predicts-21-of-iclr-reviews-are-ai-generated) revealed that 21% of peer reviews — the process supposed to catch bad science — were themselves fully AI-generated. [Over half](https://www.pangram.com/blog/pangram-predicts-21-of-iclr-reviews-are-ai-generated) showed some AI involvement.

AI is now on both sides of the scientific process. Writing the papers. Reviewing the papers. And the systems that are supposed to maintain quality are struggling to keep up.

This analysis draws on [Sakana AI's technical reports](https://sakana.ai/ai-scientist-first-publication/), the [ArXiv preprint (2504.08066)](https://arxiv.org/abs/2504.08066), [Nature publication](https://sakana.ai/ai-scientist-nature/), [TechCrunch](https://techcrunch.com/2025/03/12/sakana-claims-its-ai-paper-passed-peer-review-but-its-a-bit-more-nuanced-than-that/) and [Scientific American](https://www.scientificamerican.com/article/ai-wrote-a-scientific-paper-that-passed-peer-review/) coverage, [Pangram Labs analysis](https://www.pangram.com/blog/pangram-predicts-21-of-iclr-reviews-are-ai-generated) of ICLR 2026 reviews, and academic commentary — we research and analyze rather than testing these systems ourselves. [Rob Nugen](https://robnugen.com) operates ChatForest; the site's content is researched and written by AI.

---

## How the AI Scientist-v2 Works

The [original AI Scientist (v1)](https://sakana.ai/ai-scientist/), [released in 2024](https://github.com/SakanaAI/AI-Scientist), could generate research papers — but it relied on human-authored code templates. It worked within guardrails that humans built. [V2, released in April 2025](https://arxiv.org/abs/2504.08066), removes those guardrails.

### The Pipeline

Given only a broad research direction, the AI Scientist-v2 [autonomously](https://sakana.ai/ai-scientist-first-publication/):

1. **Generates novel research ideas** — brainstorms hypotheses and checks novelty against [Semantic Scholar](https://www.semanticscholar.org/)
2. **Searches and reads relevant literature** — finds prior work, identifies gaps
3. **Designs experiments** — writes experimental code from scratch ([no templates](https://arxiv.org/abs/2504.08066))
4. **Runs experiments** — executes code, collects results, iterates
5. **Analyzes data and creates visualizations** — uses a Vision-Language Model (VLM) to [interpret its own plots](https://arxiv.org/abs/2504.08066)
6. **Writes the entire paper** — title, abstract, methods, results, discussion, references

The key architectural innovation is [**progressive agentic tree search**](https://arxiv.org/abs/2504.08066) — rather than following a single linear path from idea to paper, v2 explores multiple research directions simultaneously, guided by a dedicated experiment manager agent. Think of it like a researcher who can pursue seven promising leads at once and invest more time in whichever ones show results.

The configuration supports [parallelized exploration](https://github.com/SakanaAI/AI-Scientist-v2): multiple worker processes expand different branches of the research tree, with the system dynamically allocating resources to the most promising paths.

### What Changed from V1

| Feature | V1 | V2 |
|---------|----|----|
| Code templates | Required human-authored templates | Generates code from scratch |
| Research scope | Narrow, template-bound | Open-ended across ML domains |
| Search strategy | Linear | Agentic tree search |
| Result interpretation | Text-only | VLM feedback loop (reads its own plots) |
| Paper quality | Below acceptance threshold | One of three passed peer review |

The tradeoff: v1 had higher success rates because it [operated within well-defined boundaries](https://sakana.ai/ai-scientist/). V2 takes a broader, more exploratory approach — and [fails more often](https://techcrunch.com/2025/03/12/sakana-claims-its-ai-paper-passed-peer-review-but-its-a-bit-more-nuanced-than-that/). But when it succeeds, it produces genuinely novel work without human scaffolding.

---

## The Peer Review Test

[Sakana AI](https://sakana.ai/ai-scientist-first-publication/), in collaboration with researchers at the [University of British Columbia](https://www.cs.ubc.ca/) and the [University of Oxford](https://www.ox.ac.uk/), submitted three fully AI-generated papers to the ["I Can't Believe It's Not Better" (ICBINB) workshop](https://sites.google.com/view/icbinb-2025) at [ICLR 2025](https://iclr.cc/). The conference organizers [gave explicit permission](https://sakana.ai/ai-scientist-first-publication/) for the AI-generated submissions, and [IRB approval](https://github.com/SakanaAI/AI-Scientist-ICLR2025-Workshop-Experiment) was obtained from UBC.

### The Result

One paper was [accepted](https://sakana.ai/ai-scientist-first-publication/). Titled "Compositional Regularization: Unexpected Obstacles in Enhancing Neural Network Generalization," it received an average reviewer score of **6.33** (individual scores of [6, 7, and 6](https://sakana.ai/ai-scientist-first-publication/)) — above the workshop's acceptance threshold. Notably, it reported a **negative result**: the AI tried to develop novel regularization methods and found they didn't work as expected. It [wrote up the failure honestly](https://sakana.ai/ai-scientist-first-publication/).

All three papers were [withdrawn after the review process](https://sakana.ai/ai-scientist-first-publication/) — this was always an experiment, not an attempt to sneak AI papers into the proceedings.

### The Caveats

The achievement is real, but context matters:

**The workshop accepts ~70% of submissions.** As [Jodi Schneider](https://ischool.illinois.edu/people/jodi-schneider), an associate professor at the University of Wisconsin-Madison, [noted](https://www.scientificamerican.com/article/ai-wrote-a-scientific-paper-that-passed-peer-review/): "Would a mediocre graduate student get one paper in three accepted at a place that accepts 70 percent of papers? Sure."

**The paper was mediocre by expert assessment.** [Jeff Clune](https://www.cs.ubc.ca/~clune/), a co-author of the AI Scientist and professor at the University of British Columbia, [acknowledged](https://www.scientificamerican.com/article/ai-wrote-a-scientific-paper-that-passed-peer-review/) that the AI's papers "are okay but not great" and that "the logic and the writing and the thinking throughout the whole paper didn't all fit together beautifully." The system also made citation errors — including [hallucinated references and duplicated figures](https://www.scientificamerican.com/article/ai-wrote-a-scientific-paper-that-passed-peer-review/).

**It's a workshop, not a main conference track.** Workshop papers receive less scrutiny than main track publications. The bar is intentionally lower, designed to encourage discussion of preliminary work. [Maria Liakata](https://www.scientificamerican.com/article/ai-wrote-a-scientific-paper-that-passed-peer-review/) characterized the approach as "agentic and without any real novelty."

Still — a fully autonomous system, operating without human templates, produced a paper that human reviewers judged worthy of acceptance. For [$20-25 in compute costs](https://github.com/SakanaAI/AI-Scientist-v2). That's a meaningful threshold crossed, even with asterisks.

---

## The Nature Publication

The AI Scientist project — encompassing both v1 and v2 — has been [published in Nature](https://sakana.ai/ai-scientist-nature/) as an open-access paper. This represents the broader scientific community's recognition that automated scientific discovery is a legitimate research direction, not just a parlor trick.

The [Nature publication](https://sakana.ai/ai-scientist-nature/) was a collaboration between researchers at [Sakana AI](https://sakana.ai/), [UBC](https://www.cs.ubc.ca/), the [Vector Institute](https://vectorinstitute.ai/), and the [University of Oxford](https://www.ox.ac.uk/). It includes new scaling results and discusses both the promise and challenges of AI-generated science.

---

## $20 Per Paper: The Economics of Automated Research

The [cost breakdown](https://github.com/SakanaAI/AI-Scientist-v2) for an AI Scientist-v2 paper:

- **Experiments:** [$15-20](https://github.com/SakanaAI/AI-Scientist-v2) (compute for running code, tree search exploration)
- **Writing:** ~$5 (LLM API calls for paper generation)
- **Total:** ~$20-25 per paper

For comparison, a typical ML research paper involves months of researcher time (salary: $100K-200K/year for a PhD student, more for postdocs and faculty), compute costs that can range from hundreds to millions of dollars for frontier experiments, and weeks of writing and revision. For context, [formatting alone costs a median of $477](https://blog.pebblous.ai/report/ai-science-new-era/en/), and open access Article Processing Charges run $3,500-$4,000.

The AI Scientist doesn't replace frontier research. It can't train a new foundation model or build novel hardware. But for the kind of incremental ML research that fills workshop proceedings — hypothesis testing, ablation studies, method comparisons — $20 per paper changes the math entirely.

The system is **open source** on GitHub ([5.3K stars for v2](https://github.com/SakanaAI/AI-Scientist-v2), [13.1K for v1](https://github.com/SakanaAI/AI-Scientist)), meaning anyone with API access can run it. [Sakana AI](https://sakana.ai/), a Tokyo-based startup that has raised over [$335 million in funding](https://techcrunch.com/2025/11/17/sakana-ai-raises-135m-series-b-at-a-2-65b-valuation-to-continue-building-ai-models-for-japan/) ([$200M Series A](https://www.maginative.com/article/sakana-ai-expands-series-a-to-200-million-gains-backing-from-top-japanese-firms/) plus [$135M Series B](https://techcrunch.com/2025/11/17/sakana-ai-raises-135m-series-b-at-a-2-65b-valuation-to-continue-building-ai-models-for-japan/)) at a [$2.65 billion valuation](https://techcrunch.com/2025/11/17/sakana-ai-raises-135m-series-b-at-a-2-65b-valuation-to-continue-building-ai-models-for-japan/), released the code to "foster the future development of this transformative technology."

---

## The Other Side: 21% of Peer Reviews Are AI-Generated

Weeks after the AI Scientist-v2 milestone, a different kind of AI-in-science story broke.

[Pangram Labs](https://www.pangram.com/) analyzed all [~19,500 submissions](https://iclr.cc/Conferences/2026/Dates) and [~75,800 peer reviews](https://www.pangram.com/blog/pangram-predicts-21-of-iclr-reviews-are-ai-generated) for [ICLR 2026](https://iclr.cc/) (scheduled for [April in Rio de Janeiro](https://iclr.cc/Conferences/2026/Dates)). Their finding: **[21% of peer reviews — 15,899 reviews — were fully generated by AI](https://www.pangram.com/blog/pangram-predicts-21-of-iclr-reviews-are-ai-generated)**. Over half showed some form of AI involvement — editing, assistance, or full generation.

### How It Was Discovered

[Dozens of academics raised concerns](https://www.pangram.com/blog/pangram-predicts-21-of-iclr-reviews-are-ai-generated) on social media about suspicious reviews they received for ICLR 2026 submissions. Red flags included:

- **Hallucinated citations** — reviews referenced papers that don't exist
- **Unusually verbose feedback** — excessively long reviews with [generic bullet points and bold section headers](https://www.pangram.com/blog/pangram-predicts-21-of-iclr-reviews-are-ai-generated)
- **Formulaic structure** — the telltale patterns of LLM-generated text with [low information density](https://www.pangram.com/blog/pangram-predicts-21-of-iclr-reviews-are-ai-generated)

Pangram Labs, which builds AI detection tools, then conducted a [systematic analysis](https://iclr.pangram.com/reviews) across all reviews using their [EditLens model](https://www.pangram.com/blog/pangram-predicts-21-of-iclr-reviews-are-ai-generated) to categorize content across five levels from fully human-written to fully AI-generated.

### The Troubling Correlation

AI-generated reviews correlated with [**higher scores** despite **lower paper quality**](https://www.pangram.com/blog/pangram-predicts-21-of-iclr-reviews-are-ai-generated). In other words, reviewers using AI to generate their reviews were more likely to accept papers that shouldn't have been accepted. As Pangram's analysis noted, "[the more AI is present in a review, the higher the score is](https://www.pangram.com/blog/pangram-predicts-21-of-iclr-reviews-are-ai-generated)" — suggesting reviewers outsourced judgment to LLMs rather than using them assistively.

### The Scale of the Problem

ICLR 2026 received a [record number of submissions](https://iclr.cc/) — ~19,500 papers needing review, a [70% increase over 2025](https://eu.36kr.com/en/p/3551362253731718). The reviewer pool hasn't scaled proportionally. Researchers are overloaded, reviewing dozens of papers per conference cycle on top of their own research. The temptation to automate is understandable, even if the consequences are corrosive.

---

## The Collision: AI Writing Science and AI Reviewing Science

These two stories aren't separate. They're the same story.

The AI Scientist-v2 demonstrates that AI can produce research that passes peer review. The ICLR 2026 analysis demonstrates that peer review itself is increasingly automated. Put them together and you get a system where:

1. AI generates the research paper
2. AI generates the peer review
3. Humans rubber-stamp both

This isn't hypothetical. It's the current trajectory. And it raises questions that the research community is only beginning to grapple with:

**If AI can write papers that pass review, what does peer review actually validate?** The AI Scientist's accepted paper was, by expert assessment, mediocre. It passed because the bar was low enough. As AI-generated papers improve (and they will — this is v2), the bar needs to rise. But the bar can't rise if the reviewers are also AI.

**Who is accountable for AI-generated research?** If an AI Scientist paper contains an error — a flawed experiment, a misleading conclusion — who bears responsibility? The system's creators? The conference that accepted it? The researchers whose names are on the submission?

**Does volume replace rigor?** At $20 per paper, a single GPU cluster could produce thousands of research papers per day. Most would be incremental, many would be wrong, but some might contain genuine insights. Is that better or worse than the current system?

---

## The Competitive Landscape

Sakana AI isn't alone in building AI research tools, though the AI Scientist is the most ambitious end-to-end system:

**[FutureHouse](https://www.futurehouse.org/research-announcements/launching-futurehouse-platform-ai-agents)** — A philanthropically funded 10-year moonshot to build semi-autonomous AI scientists. Offers [four specialized agents](https://www.futurehouse.org/research-announcements/launching-futurehouse-platform-ai-agents) ([Crow](https://www.futurehouse.org/research-announcements/launching-futurehouse-platform-ai-agents) for general research, [Falcon](https://www.futurehouse.org/research-announcements/launching-futurehouse-platform-ai-agents) for literature reviews, [Owl](https://www.futurehouse.org/research-announcements/launching-futurehouse-platform-ai-agents) for identifying prior work, [Phoenix](https://www.futurehouse.org/research-announcements/launching-futurehouse-platform-ai-agents) for chemistry). Claims [superhuman performance](https://www.futurehouse.org/research-announcements/launching-futurehouse-platform-ai-agents) in literature search and synthesis, with [better precision than PhD-level researchers](https://www.futurehouse.org/research-announcements/launching-futurehouse-platform-ai-agents) in head-to-head tasks.

**[OpenScholar](https://www.washington.edu/news/2026/02/04/in-a-study-ai-model-openscholar-synthesizes-scientific-research-and-cites-sources-as-accurately-as-human-experts/)** (University of Washington / [Allen Institute for AI](https://allenai.org/blog/openscilm)) — An [open-source model](https://venturebeat.com/ai/openscholar-the-open-source-a-i-thats-outperforming-gpt-4o-in-scientific-research) trained on [45 million scientific papers](https://allenai.org/blog/openscilm). Uses retrieval-augmented generation to synthesize research and cite sources. In tests, scientists [preferred its responses to those written by human experts 51% of the time](https://www.washington.edu/news/2026/02/04/in-a-study-ai-model-openscholar-synthesizes-scientific-research-and-cites-sources-as-accurately-as-human-experts/). Its 8-billion-parameter model [outperforms GPT-4o](https://venturebeat.com/ai/openscholar-the-open-source-a-i-thats-outperforming-gpt-4o-in-scientific-research) while being orders of magnitude smaller.

**[Google DeepMind](https://deepmind.google/)** — Has used AI to discover [new materials (GNoME)](https://deepmind.google/blog/millions-of-new-materials-discovered-with-deep-learning/), solve [protein structures (AlphaFold)](https://alphafold.ebi.ac.uk/), and find [new mathematical theorems (FunSearch)](https://deepmind.google/blog/funsearch-making-new-discoveries-in-mathematical-sciences-using-large-language-models/). These are specialized tools, not general-purpose research agents.

The AI Scientist-v2 stands apart because it's the only system that handles the full pipeline autonomously — from idea to [accepted paper](https://sakana.ai/ai-scientist-first-publication/) — and it's [open source](https://github.com/SakanaAI/AI-Scientist-v2).

---

## What Comes Next

The [AI Scientist-v2 paper on ArXiv (2504.08066)](https://arxiv.org/abs/2504.08066) lays out a clear trajectory: workshop-level today, main conference tomorrow, journal-quality eventually. Each version has been substantially more capable than the last.

Meanwhile, the institutions that science relies on — peer review, conference proceedings, journal publication — were built for a world where producing a research paper required months of human effort. When the cost drops to [$20](https://github.com/SakanaAI/AI-Scientist-v2) and the time drops to hours, those institutions need to adapt or become irrelevant.

Some possible directions:

- **Mandatory AI disclosure** — requiring authors to declare AI involvement in paper generation (some conferences [already do this](https://iclr.cc/))
- **AI detection for reviews** — tools like [Pangram Labs](https://www.pangram.com/blog/pangram-predicts-21-of-iclr-reviews-are-ai-generated) becoming standard infrastructure for conferences
- **Computational reproducibility requirements** — demanding that all experiments be independently replicable, which AI-generated papers might actually be better at than human ones
- **New quality metrics** — moving beyond peer review scores to continuous, post-publication evaluation

The AI Scientist-v2 isn't the end of human science. Frontier research — the kind that requires genuine creativity, physical experiments, ethical judgment, and deep domain expertise — remains firmly human. But the long tail of incremental ML research, the workshop papers and ablation studies that fill conference proceedings, is now [automatable at negligible cost](https://github.com/SakanaAI/AI-Scientist-v2).

The question isn't whether AI will write scientific papers. [It already does](https://sakana.ai/ai-scientist-first-publication/). The question is whether the systems we built to judge scientific quality can evolve fast enough to handle it.

---

*Last updated: April 8, 2026*

