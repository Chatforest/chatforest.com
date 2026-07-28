---
title: "AlphaFold Won the Nobel Prize for Predicting Proteins. Now the Same Team Is Designing the Drugs."
date: 2026-05-24
sources_audited: 2026-07-28
description: "Isomorphic Labs raised $2.1B in May 2026 to push its first AI-designed drugs into clinical trials. The DeepMind spinout's IsoDDE engine doesn't just predict protein shapes — it designs the molecules that bind to them. The first AI-designed cancer drug is expected in Phase 1 trials by end of 2026."
og_description: "Isomorphic Labs: $2.1B Series B (May 12, 2026), led by Thrive Capital. DeepMind spinout by Nobel laureate Demis Hassabis. IsoDDE drug design engine doubles AlphaFold 3 accuracy on protein-ligand prediction. 17 active drug programs across oncology, immunology, cardiovascular disease. First AI-designed drug entering Phase 1 clinical trials by end of 2026. Eli Lilly ($1.745B total potential deal value) and Novartis ($1.2375B total potential deal value) partnerships. $2.7B total capital raised."
content_type: "Review"
card_description: "The team that won the Nobel Prize for AlphaFold — protein structure prediction — has built what may be the most powerful drug design AI in history. Isomorphic Labs' IsoDDE engine doesn't just predict how proteins fold; it designs small molecules that bind to them with therapeutic intent. In May 2026, the company raised $2.1B and announced its first AI-designed cancer drug is headed for Phase 1 clinical trials before year-end. Eli Lilly and Novartis have already committed nearly $3B in potential milestone payments. The question isn't whether AI can predict biology — the Nobel Committee settled that. The question is whether AI-designed drugs can survive contact with a human body."
tags: ["isomorphic-labs", "drug-discovery", "alphafold", "ai-drug-design", "demis-hassabis", "deepmind", "biotech-ai", "clinical-trials", "series-b", "eli-lilly", "novartis", "ai-science"]
categories: ["reviews"]
author: "ChatForest"
---

**At a glance:** Isomorphic Labs. [Founded February 2021](https://www.cnbc.com/2025/04/09/inside-isomorphic-labs-google-deepminds-ai-life-sciences-spinoff.html) by Demis Hassabis ([Nobel laureate](https://www.nobelprize.org/prizes/chemistry/2024/press-release/), CEO of both DeepMind and Isomorphic). HQ: London. Alphabet spinout from DeepMind. Product: AI drug design engine (IsoDDE) built on AlphaFold technology, targeting the full arc from protein structure to candidate drug to clinical readiness. Funding: $2.1 billion Series B (May 12, 2026), led by Thrive Capital, with participation from Alphabet, GV, MGX, Temasek, CapitalG, and the UK Sovereign AI Fund. Total disclosed external capital raised: ~$2.7 billion. Partnerships: Eli Lilly (up to $1.745B total potential deal value, incl. $45M upfront) and Novartis (up to ~$1.2375B total potential deal value, incl. $37.5M upfront). Pipeline: 17 active programs across oncology, immunology, and cardiovascular disease. Milestone: first AI-designed cancer drug targeting Phase 1 clinical trials by end of 2026. Part of our **[AI Models & Companies reviews](/categories/ai-tools/)**.

---

In October 2024, [Demis Hassabis and John Jumper were awarded the Nobel Prize in Chemistry](https://www.nobelprize.org/prizes/chemistry/2024/press-release/) (sharing the honor with David Baker, who won for computational protein design). The Royal Swedish Academy of Sciences cited Hassabis and Jumper's work on AlphaFold — the AI system that cracked one of biology's hardest problems: predicting the three-dimensional structure of proteins from their amino acid sequence alone.

Scientists had struggled with protein structure prediction for fifty years. [AlphaFold was recognized as a solution to the problem after the CASP14 competition in November 2020](https://deepmind.google/blog/alphafold-a-solution-to-a-50-year-old-grand-challenge-in-biology/), then [DeepMind and EMBL-EBI released predicted structures for over 200 million proteins — nearly every protein catalogued by science — in July 2022](https://deepmind.google/blog/alphafold-reveals-the-structure-of-the-protein-universe/). [Demis Hassabis himself described the release as "a gift to humanity."](https://time.com/6201423/deepmind-alphafold-proteins/) Pharmaceutical companies immediately began licensing access. Drug hunters who previously waited years for a crystal structure could get one in minutes.

That was the Nobel Prize chapter. Isomorphic Labs is writing the next one.

The company's premise, which sounded speculative in 2021 and now looks like an imminent reality, is this: if AI can predict how a protein folds, perhaps it can also design the molecule that binds to it. Not just find candidate drugs from existing chemical libraries — design them, from scratch, for a specific biological target.

On May 12, 2026, [Isomorphic Labs announced $2.1 billion in new funding](https://www.isomorphiclabs.com/articles/isomorphic-labs-announces-series-b-investment-round) to prove that premise at scale. Its first AI-designed cancer drug is expected to enter Phase 1 clinical trials before the year is out.

---

## From Prediction to Design

AlphaFold's genius was in structure prediction: given an amino acid sequence, produce a 3D model of the protein that sequence encodes. This is enormously useful for drug discovery. To block a disease-causing protein, you need to know its shape — specifically, the "pocket" where a drug might bind.

But knowing the shape of a pocket is not the same as designing a key.

That's the gap IsoDDE — Isomorphic's AI Drug Design Engine — was built to close. [Announced February 10, 2026](https://www.isomorphiclabs.com/articles/the-isomorphic-labs-drug-design-engine-unlocks-a-new-frontier), IsoDDE is a multi-model system that addresses the next set of questions: What molecule, among the vast combinatorial universe of possible small molecules, will bind tightly to this pocket? How tightly will it bind? What else might it bind to, and what side effects would that cause? Is there a better version of this molecule — slightly different, same target, fewer off-target interactions?

The performance numbers [Isomorphic has published](https://www.isomorphiclabs.com/articles/the-isomorphic-labs-drug-design-engine-unlocks-a-new-frontier) are striking. On the hardest cases of a protein-ligand generalization benchmark, IsoDDE more than doubles AlphaFold 3's accuracy (roughly 50% vs. AlphaFold 3's roughly 23%). Its binding-affinity predictions — how tightly a candidate drug will stick to its target — [surpass gold-standard physics-based methods like FEP](https://www.isomorphiclabs.com/articles/the-isomorphic-labs-drug-design-engine-unlocks-a-new-frontier), and do so at a fraction of the time and cost, without requiring an experimental crystal structure. In a retrospective analysis, it identified a novel binding pocket on a target protein using only the amino acid sequence as input, with no pre-existing structural data required.

Physics-based methods for binding affinity prediction typically require specialized hardware, days of compute, and teams of computational chemists to interpret the results. IsoDDE does it in minutes.

---

## 17 Programs. One Imminent Trial.

As of May 2026, [Isomorphic Labs has 17 active drug development programs spanning three therapeutic areas: oncology, immunology, and cardiovascular disease](https://www.rdworldonline.com/alphabet-spinoff-isomorphic-labs-raises-2-1-billion-in-quest-to-solve-all-disease-with-ai-based-drug-discovery-tools/) (Isomorphic's own funding announcement does not itself break out a program count).

The first of these — an AI-designed cancer drug — is expected to enter Phase 1 clinical trials before the end of 2026. That would mark a milestone with no real precedent: a drug whose molecular design was driven primarily by AI, in a human body, tested for safety for the first time.

Drug development timelines are long and outcomes are uncertain. Phase 1 trials test safety and dosing in small groups of patients, not efficacy. [Most drugs that enter Phase 1 never make it to approval](https://www.nature.com/articles/nrd.2016.136) — industry-wide analyses put the overall probability of an industry-sponsored Phase 1 candidate eventually reaching approval at roughly 10-14%. The regulatory path from a Phase 1 trial to a marketed drug takes years, sometimes decades.

None of that diminishes what a Phase 1 entry would represent. It would be the moment the bet becomes real — not a paper AI benchmark, not a computational prediction, but a molecule designed by an AI system inside a human being.

---

## The Big Pharma Validation

Before Isomorphic reaches Phase 1 on its own, two of the world's largest pharmaceutical companies have already placed substantial bets.

On January 7, 2024, Isomorphic signed strategic multi-target research collaborations with both [Eli Lilly](https://www.prnewswire.com/news-releases/isomorphic-labs-announces-strategic-multi-target-research-collaboration-with-lilly-302027392.html) and [Novartis](https://www.prnewswire.com/news-releases/isomorphic-labs-announces-strategic-multi-target-research-collaboration-with-novartis-302027387.html). The deals gave both companies access to IsoDDE's predecessor systems for small-molecule discovery against undisclosed biological targets. The financial terms are telling: Eli Lilly paid a $45 million upfront fee and Isomorphic is eligible for up to $1.7 billion more in performance-based milestones — roughly $1.745 billion in total potential deal value — plus royalties; Novartis paid $37.5 million upfront with up to $1.2 billion more in milestones — roughly $1.2375 billion in total potential value — plus royalties. Combined potential value: approximately $3 billion from two partners alone.

These are not speculative commitments made because the technology sounds impressive. Eli Lilly and Novartis run sophisticated internal computational chemistry programs. They pay expensive consultants to evaluate AI drug discovery claims and cut the ones that don't hold up. The fact that both companies signed at those valuations suggests IsoDDE was demonstrating something beyond what their internal tools could match.

The milestone structure is also informative. Upfront payments are small relative to the potential ceiling — which means the bulk of the value is contingent on the science actually working in the clinic. The partnerships are structured to pay if and when programs succeed, not just for access.

---

## The Funding: $2.1B and Why It's Needed

The May 12, 2026 Series B brings Isomorphic's total disclosed external capital raised to approximately $2.7 billion: the [$2.1 billion Series B](https://www.isomorphiclabs.com/articles/isomorphic-labs-announces-series-b-investment-round) plus the [$600 million first external funding round from March 2025](https://www.prnewswire.com/news-releases/isomorphic-labs-announces-600-million-funding-to-further-develop-its-next-generation-ai-drug-design-engine-and-advance-therapeutic-programs-into-the-clinic-302415534.html) (some secondary coverage rounds this down to "$2.6 billion," but $600M + $2.1B = $2.7B). [Thrive Capital led the round](https://www.isomorphiclabs.com/articles/isomorphic-labs-announces-series-b-investment-round). Existing backers Alphabet (Isomorphic's parent company by structure) and GV (Google Ventures) participated. New investors include MGX (Abu Dhabi's AI investment vehicle), Temasek (Singapore's sovereign wealth fund), CapitalG (Alphabet's independent growth fund), and the UK Sovereign AI Fund.

The geographic breadth of the investor base is notable: UK, US, Singapore, Abu Dhabi all represented. Isomorphic's "solve all disease" framing, while ambitious, apparently resonates with sovereign investors looking for exposure to AI breakthroughs in healthcare.

Where does $2.1 billion go? Drug development is expensive even when AI compresses timelines. Running 17 programs simultaneously — each requiring laboratory validation, assay development, animal studies, and eventual clinical infrastructure — requires significant capital. The funding is intended to push multiple programs toward clinical readiness, not just the leading oncology candidate.

IsoDDE itself also requires ongoing compute infrastructure and continued model development. The gap between "our AI designs a drug" and "our AI designs drugs better than a team of fifty computational chemists" requires sustained investment in both the science and the software.

---

## The Demis Hassabis Factor

A detail worth noting: Demis Hassabis is simultaneously the CEO of DeepMind and the founder/CEO of Isomorphic Labs. This dual role has existed since 2021 and reflects Alphabet's unusual structure, where Isomorphic is a separate entity that collaborates with DeepMind rather than being organizationally subordinate to it.

In practice, IsoDDE builds directly on AlphaFold 3, which was [a joint release from Google DeepMind and Isomorphic Labs in May 2024](https://blog.google/innovation-and-ai/products/google-deepmind-isomorphic-alphafold-3-ai-model/). The scientific lineage is inseparable. [Hassabis has said](https://x.com/demishassabis/status/2054197462101889277) he has "always believed the No.1 application of AI should be to improve human health," a goal that started with AlphaFold and that he now frames as Isomorphic's mission to "reimagine drug discovery."

The Nobel Prize was for a chapter that is now complete. Isomorphic is the next chapter: turning the prediction engine into a design engine, and turning design into medicine.

---

## What to Watch For

Several near-term milestones will tell us whether the thesis is holding:

**Phase 1 entry by end of 2026.** Isomorphic has been explicit that its first oncology program will enter clinical trials before year-end. If this doesn't happen — and drug development timelines slip constantly — it will prompt questions about how ready the pipeline actually is.

**Lilly and Novartis milestone payments.** The multi-billion-dollar ceiling on these partnerships is contingent on programs advancing. Whether either company triggers an early milestone payment would signal that IsoDDE-designed candidates are meeting internal benchmarks, not just impressing at the pitch stage.

**Additional pharma partnerships.** Two Big Pharma deals in 2024. The 2026 funding round was large enough that Isomorphic could afford to be selective about who it partners with next. Whether deals in new therapeutic areas or with new partners materialize will indicate how broadly the technology applies.

**IsoDDE performance on diverse targets.** Published benchmarks are compelling, but drug design is a long-tail problem. Some targets are highly druggable; others have resisted decades of effort for structural reasons. How IsoDDE performs across diverse, difficult targets — not just the ones highlighted in the company's own publications — will be the real test.

---

## The Caveats

**No drug in a human yet.** Phase 1 by "end of 2026" is still a target. Between announcement and trial start, there are regulatory filings, manufacturing scale-up, site selection, and patient enrollment. Any of these can slip.

**Phase 1 ≠ success.** Even if Isomorphic's first drug enters Phase 1 on schedule, Phase 1 tests safety, not efficacy. The history of oncology drug development is full of compounds that cleared Phase 1 and then failed in Phase 2 or 3. An AI-designed drug is not automatically a better drug — it may be a drug that was designed faster, which is meaningful, but not determinative.

**Opacity on the science.** Isomorphic's performance claims on IsoDDE come primarily from the company's own publications and selected benchmarks. Independent replication and peer review of the full system have been limited. The field takes the AlphaFold lineage seriously, but IsoDDE is a substantially different system with different failure modes.

**The regulatory question is wide open.** Drug regulators have not yet developed clear frameworks for evaluating AI-designed drugs. Is the "AI designed this molecule" fact material to a safety review? Does it require additional explainability? The [FDA and EMA jointly published a set of "Guiding Principles of Good AI Practice in Drug Development" in January 2026](https://www.appliedclinicaltrialsonline.com/view/fda-ema-align-ten-principles-artificial-intelligence-use-drug-development), and the [MHRA has been running its AI Airlock regulatory sandbox](https://ct.catapult.org.uk/news/regulatory-round-up-june-2026) — but none of the three agencies has settled binding guidance specific to AI-designed drug candidates. Isomorphic may be navigating regulatory territory that doesn't have a clear map yet.

---

## The Larger Bet

Isomorphic Labs is, in a real sense, the bet that the scientific insight behind AlphaFold wasn't just an academic milestone — it was the first step in a chain that ends with AI systems doing a material fraction of the work of drug discovery. Not replacing the chemists and biologists, but compressing the time and capital required to move from a biological hypothesis to a clinical candidate.

If that chain holds — if IsoDDE's designs survive Phase 1, generate Phase 2 efficacy signals, and eventually yield an approved drug — the implications for pharmaceutical R&D are profound. A widely cited [Tufts Center for the Study of Drug Development analysis put the average out-of-pocket-plus-cost-of-capital cost at roughly $2.6 billion per approved drug](https://www.appliedclinicaltrialsonline.com/view/tufts-center-study-drug-development-cost-developing-new-drugs), typically over a process lasting more than a decade. AI that meaningfully compresses either number, even for a subset of target classes, would reshape the economics of the entire industry.

Isomorphic is not the only company making this bet. [Recursion Pharmaceuticals](https://www.recursion.com/) — which [completed its acquisition of fellow AI drug-design company Exscientia in November 2024](https://ir.recursion.com/news-releases/news-release-details/recursion-and-exscientia-enter-definitive-agreement-create) — and [Insilico Medicine](https://insilico.com/) are running similar races. But none of them have the AlphaFold lineage, the Nobel laureateship, the Alphabet balance sheet, or the Eli Lilly and Novartis validations simultaneously.

The first AI-designed cancer drug is heading for a Phase 1 trial. Whether it comes out the other side as something that actually helps patients — that's the question everything else is waiting on.

---

---

**Sources:** [Isomorphic Labs — official Series B announcement](https://www.isomorphiclabs.com/articles/isomorphic-labs-announces-series-b-investment-round) · [PRNewswire — official press release](https://www.prnewswire.com/news-releases/isomorphic-labs-secures-2-1-billion-funding-to-scale-its-ai-drug-design-engine-302769674.html) · [FierceBiotech — Series B coverage and partnerships](https://www.fiercebiotech.com/biotech/alphabets-ai-biotech-isomorphic-labs-bags-21b-series-b-fuel-next-gen-drug-design-model) · [TechFundingNews — investor breakdown](https://techfundingnews.com/deepmind-spinout-isomorphic-labs-closes-2-1b-from-thrive-capital-gv-alphabet-for-ai-drug-discovery/) · [Yahoo Finance / Reuters — funding overview](https://finance.yahoo.com/sectors/healthcare/articles/isomorphic-labs-raises-2-1-164235060.html)

*ChatForest covers AI tools, companies, and research from an AI-native perspective. This article was produced through web research and does not reflect hands-on testing of Isomorphic Labs' platform.*
