# The AI Law Patchwork: 1,561 Bills Across 45 States, a Federal Preemption Fight, and What It Means for Anyone Building with AI

> By March 2026, state lawmakers across 45 US states had introduced 1,561 AI-related bills — already surpassing the total for all of 2024. California's AI Transparency Act (AB 853) and Frontier AI safety law (SB 53) took effect January 1. Texas enacted TRAIGA with NIST-aligned risk management requirements. Colorado's Algorithmic Discrimination Act (SB 205) kicks in June 30. Illinois banned discriminatory AI in hiring decisions. New York City requires annual bias audits for automated employment tools. Meanwhile, the Trump administration is fighting back: a December 2025 executive order created a DOJ AI Litigation Task Force to challenge state AI laws in federal court, conditioned $42 billion in broadband funding on states repealing 'onerous' AI regulations, and in March 2026 released a National Policy Framework asking Congress to preempt state laws entirely. The result is a regulatory collision course — states racing to protect consumers, the federal government racing to clear the field for industry, and AI developers caught in the middle trying to build products that comply with a patchwork of contradictory requirements. This analysis tracks the major laws, the key themes (hiring discrimination, deepfakes, provenance metadata, healthcare AI, surveillance pricing), and the federal-state showdown that will define AI regulation for years to come.


By March 2026, state lawmakers in [45 states had introduced 1,561 AI-related bills](https://www.multistate.ai/artificial-intelligence-ai-legislation). That already exceeds the [total number of AI bills introduced across all of 2024](https://www.ncsl.org/financial-services/artificial-intelligence-legislation-database).

At the same time, the Trump administration is actively trying to stop states from regulating AI at all — using [executive orders](https://www.whitehouse.gov/presidential-actions/2025/12/eliminating-state-law-obstruction-of-national-artificial-intelligence-policy/), [federal litigation](https://www.cbsnews.com/news/doj-creates-task-force-to-challenge-state-ai-regulations/), and [billions of dollars in funding leverage](https://www.lawfaremedia.org/article/the-ai-preemption-executive-order-s-bead-strategy-faces-steep-legal-hurdles) to preempt state laws.

The result is a regulatory collision that anyone building, deploying, or using AI systems needs to understand.

This analysis draws on tracking from [MultiState](https://www.multistate.ai/artificial-intelligence-ai-legislation), the [IAPP US State AI Governance Tracker](https://iapp.org/resources/article/us-state-ai-governance-legislation-tracker), [Kiteworks](https://www.kiteworks.com/regulatory-compliance/state-ai-legislation-2026-compliance-data-governance/), legal analysis from [Ropes & Gray](https://www.ropesgray.com/en/insights/alerts/2026/03/examining-the-landscape-and-limitations-of-the-federal-push-to-override-state-ai-regulation), [Latham & Watkins](https://www.lw.com/en/insights/california-assumes-role-as-lead-us-regulator-of-ai), [Norton Rose Fulbright](https://www.nortonrosefulbright.com/en/knowledge/publications/c6c60e0c/the-texas-responsible-ai-governance-act), [Wiley](https://www.wiley.law/article-2026-State-AI-Bills-That-Could-Expand-Liability-Insurance-Risk), and state legislative texts — we research and analyze rather than testing products hands-on. [Rob Nugen](https://robnugen.com) operates ChatForest; the site's content is researched and written by AI.

---

## The Four Laws That Matter Most Right Now

Most of the 1,561 bills will die in committee. But four state laws are already in effect or taking effect soon, and they represent the major regulatory categories that every AI developer and deployer should understand.

### California — Frontier AI Safety and Transparency

California has positioned itself as the de facto US AI regulator through two landmark laws.

**[SB 53 — Transparency in Frontier Artificial Intelligence Act](https://leginfo.legislature.ca.gov/faces/billNavClient.xhtml?bill_id=202520260SB53)** (effective January 1, 2026) applies to frontier AI developers with [annual revenue exceeding $500 million](https://fpf.org/blog/californias-sb-53-the-first-frontier-ai-law-explained/). It requires companies to publish and maintain a ["frontier AI framework"](https://carnegieendowment.org/emissary/2025/10/california-sb-53-frontier-ai-law-what-it-does) explaining how they identify, assess, and mitigate catastrophic risks. They must release [detailed public transparency reports](https://ai-analytics.wharton.upenn.edu/wharton-accountable-ai-lab/sb-53-what-californias-new-ai-safety-law-means-for-developers/) covering model capabilities, risk assessments, third-party evaluations, and mitigation measures. They must report any ["critical safety incidents" to the California Office of Emergency Services](https://www.nelsonmullins.com/insights/blogs/ai-task-force/ai/california-sb-53-expanded-compliance-guide-for-frontier-ai-developers) within 15 days, or 24 hours if there is imminent danger.

**[AB 853 — California AI Transparency Act](https://leginfo.legislature.ca.gov/faces/billTextClient.xhtml?bill_id=202520260AB853)** ([full requirements phased](https://www.troutmanprivacy.com/2025/10/california-ai-transparency-act-amendments-signed-into-law/) through August 2026 and January 2027) targets generative AI systems with [over one million monthly users](https://www.mayerbrown.com/en/insights/publications/2025/10/new-obligations-under-the-california-ai-transparency-act-and-companion-chatbot-law-add-to-the-compliance-list) in California. Developers must provide [free AI detection tools](https://steg.ai/news/ai-transparency-act-ab-853/) that assess whether image, video, or audio content was created or altered by their system, and output any system provenance data. By January 2027, platforms hosting generative AI models (including those distributing model weights or source code) must include [manifest disclosures and latent disclosures](https://www.mayerbrown.com/en/insights/publications/2025/10/new-obligations-under-the-california-ai-transparency-act-and-companion-chatbot-law-add-to-the-compliance-list) in AI-generated content — essentially requiring watermarking and provenance metadata consistent with [widely accepted industry standards](https://steg.ai/news/ai-transparency-act-ab-853/). Violations carry civil penalties of [$5,000 per violation per day, plus attorney's fees](https://leginfo.legislature.ca.gov/faces/billTextClient.xhtml?bill_id=202520260AB853).

Together, these laws mean that any large AI developer operating in California — which includes virtually every major AI company — must publish safety frameworks, offer detection tools, and embed provenance data in their outputs.

### Texas — Risk Management and Anti-Manipulation

The **[Texas Responsible Artificial Intelligence Governance Act (TRAIGA)](https://www.nortonrosefulbright.com/en/knowledge/publications/c6c60e0c/the-texas-responsible-ai-governance-act)** took effect [January 1, 2026](https://www.bakerbotts.com/thought-leadership/publications/2025/july/texas-enacts-responsible-ai-governance-act-what-companies-need-to-know). It applies to anyone who develops, deploys, or promotes AI systems used by Texas residents.

Key requirements include [referencing NIST's AI Risk Management Framework](https://www.bakerbotts.com/thought-leadership/publications/2025/july/texas-enacts-responsible-ai-governance-act-what-companies-need-to-know) as a recognized safe harbor for compliance, [disclosing to consumers when they are interacting with an AI system](https://www.nortonrosefulbright.com/en/knowledge/publications/c6c60e0c/the-texas-responsible-ai-governance-act) (applies to government agencies and healthcare providers), and [prohibiting AI systems that intentionally incite self-harm, harm to others, or criminal activity](https://www.littler.com/news-analysis/asap/texas-joins-fray-and-enacts-ai-legislation). Government entities are specifically banned from using AI for [social scoring](https://www.jw.com/news/insights-texas-89th-legislature-ai/) or [biometric identification without consent](https://www.securityindustry.org/2025/06/24/groundbreaking-texas-ai-law-also-brings-needed-clarity-on-use-of-biometric-technologies-for-security/). Texas also [established an AI Advisory Council](https://www.littler.com/news-analysis/asap/texas-joins-fray-and-enacts-ai-legislation) to guide state agencies.

TRAIGA is notable for its breadth — the definition of "artificial intelligence system" is expansive enough to cover nearly any machine learning system that generates outputs influencing decisions.

### Colorado — Algorithmic Discrimination

Colorado's **[SB 24-205](https://www.coloradosb205.com/)** ([enforcement begins June 30, 2026](https://www.akingump.com/en/insights/ai-law-and-regulation-tracker/colorado-postpones-implementation-of-colorado-ai-act-sb-24-205), after a [delay from the original February 1 date](https://www.bakerbotts.com/thought-leadership/publications/2025/september/colorado-ai-act-implementation-delayed)) focuses specifically on "high-risk" AI systems — those used in consequential decisions about education, employment, financial services, government services, healthcare, housing, insurance, or legal services.

Developers must use [reasonable care to protect consumers from algorithmic discrimination](https://co-aims.com/blog/colorado-ai-act-sb-24-205-complete-compliance-guide). Deployers must conduct [annual reviews](https://co-aims.com/blog/colorado-ai-act-sb-24-205-complete-compliance-guide) of each high-risk system. Discovery of algorithmic discrimination must be [disclosed to the state attorney general within 90 days](https://www.coloradosb205.com/). The attorney general has [exclusive enforcement authority — no private right of action](https://co-aims.com/blog/colorado-ai-act-sb-24-205-complete-compliance-guide) — with penalties up to [$20,000 per violation](https://co-aims.com/blog/colorado-ai-act-sb-24-205-complete-compliance-guide) and a [60-day cure period](https://www.glacis.io/guide-colorado-ai-act).

Colorado's law is the first to create an affirmative obligation on AI developers to prevent discriminatory outcomes in high-stakes decisions, going beyond disclosure requirements into substantive performance standards.

### Illinois — AI in Hiring

Illinois's [amendments to the **Human Rights Act**](https://www.jonesday.com/en/insights/2024/10/illinois-becomes-second-state-to-pass-broad-legislation-on-the-use-of-ai-in-employment-decisions) (effective January 1, 2026) make it illegal to use AI in recruitment, hiring, promotion, discharge, or other employment decisions in ways that result in discrimination against protected classes — whether intentional or not.

Employers must [notify employees and candidates](https://www.morganlewis.com/pubs/2024/09/illinois-passes-new-law-to-address-ai-in-the-workplace) when AI is used in employment decisions. Using [ZIP codes as a proxy for protected characteristics is explicitly banned](https://www.grsm.com/insight/amendments-to-illinois-human-rights-act-to-regulate-use-of-ai-in-employment-decisions/). Complaints go to the Illinois Department of Human Rights; there is no private right of action.

Illinois joins New York City, which [requires annual independent bias audits](https://www.dciconsult.com/nyc-automated-employment-decision-tools-bill) for any automated employment decision tools, [public posting of audit summaries](https://www.deloitte.com/us/en/services/audit-assurance/articles/nyc-local-law-144-algorithmic-bias.html), ten business days' notice to candidates before using such tools, and offering an alternative selection process on request. Under [Local Law 144](https://www.osc.ny.gov/state-agencies/audits/2025/12/02/enforcement-local-law-144-automated-employment-decision-tools), penalties are up to $500 for a first violation and $500–$1,500 for each subsequent violation, with each day of non-compliance constituting a separate violation.

---

## The Five Major Themes Across All 1,561 Bills

While the laws above are the headline acts, the full legislative landscape reveals five consistent themes.

### 1. Hiring and Employment Discrimination

The most common target across states. The core concern: AI screening tools that filter job applicants based on patterns correlated with race, gender, age, or disability — often without the employer understanding how or why. Illinois and New York City are the models; bills with similar requirements are active in California, New Jersey, Maryland, and at least a dozen other states.

### 2. Deepfakes and Nonconsensual Content

States are expanding liability beyond the people who create deepfakes to the platforms and AI tools that enable them. [Payment processors, hosting platforms, and cloud providers](https://www.naag.org/press-releases/state-and-territory-attorneys-general-urge-tech-and-payment-platforms-to-address-deepfake-exploitation/) are [increasingly named in proposed legislation](https://www.wiley.law/article-2026-State-AI-Bills-That-Could-Expand-Liability-Insurance-Risk). The federal [DEFIANCE Act passed the US Senate unanimously](https://www.judiciary.senate.gov/press/dem/releases/durbin-successfully-passes-bill-to-combat-nonconsensual-sexually-explicit-deepfake-images) in [January 2026](https://rollcall.com/2026/01/13/senate-passes-bill-targeting-nonconsensual-deepfake-images/), establishing a federal right of action (with [minimum $150,000 damages](https://www.judiciary.senate.gov/press/dem/releases/durbin-successfully-passes-bill-to-combat-nonconsensual-sexually-explicit-deepfake-images)) for victims of nonconsensual, sexually explicit deepfakes. At the state level, California's AI Transparency Act requires provenance disclosures consistent with [widely accepted industry standards](https://steg.ai/news/ai-transparency-act-ab-853/) such as C2PA (Coalition for Content Provenance and Authenticity) watermarking.

### 3. Provenance Metadata and Content Labeling

[Washington, Arizona, California, Illinois, and New York](https://www.transparencycoalition.ai/news/ai-legislative-update-march20-2026) have all introduced bills requiring provenance metadata to be attached to AI-generated or AI-modified content. This is the technical infrastructure layer underneath the deepfake and transparency laws — the idea that AI-generated content should carry a machine-readable chain of custody. California's AB 853 is the furthest along, requiring detection tools and latent disclosures in AI outputs. Specific bills include [Washington HB 1170](https://www.transparencycoalition.ai/news/ai-legislative-update-march20-2026) (signed by the governor), Illinois HB 4711, New York S 6954/A 6540, and Arizona HB 2311.

### 4. Healthcare AI

Utah made headlines by becoming the [first state to allow AI to autonomously renew drug prescriptions](https://commerce.utah.gov/2026/01/06/news-release-utah-and-doctronic-announce-groundbreaking-partnership-for-ai-prescription-medication-renewals/), through a pilot program with [Doctronic launched January 6, 2026](https://www.deseret.com/business/2026/01/06/utah-artificial-intelligence-prescription-renewal-regulatory-sandbox-innovation-patient-safety/). The 12-month pilot covers [190 commonly prescribed drugs](https://www.medicaleconomics.com/view/utah-lets-ai-refill-chronic-prescriptions-in-state-backed-pilot-program) (excluding controlled substances and injectables), with physicians required to [review the first 250 prescriptions per drug class](https://www.mobihealthnews.com/news/utah-allows-ai-renew-prescription-drugs-autonomously) before full automation. Across nearly every state, bills regulating AI in healthcare insurance require qualified human professionals to make or approve coverage determinations. The tension is clear: AI is entering clinical workflows while legislators are still debating whether it should be allowed near insurance claims.

### 5. Surveillance Pricing

An emerging category with bipartisan appeal. Colorado's [HB 1210](https://leg.colorado.gov/bills/HB26-1210) passed the House [39–24](https://www.thecentersquare.com/colorado/article_1895034a-d66b-4131-a6c7-3bab8d4b600f.html) banning certain forms of "surveillance pricing" — the practice of using AI to set individualized prices based on personal data like browsing history, purchase patterns, or demographic inferences. [Consumer Reports supports the bill](https://advocacy.consumerreports.org/research/consumer-reports-supports-colorado-bill-to-prohibit-surveillance-pricing-hb26-1210/). California has [similar legislation pending](https://connectontech.bakermckenzie.com/golden-state-update-california-targets-surveillance-pricing/) (AB 2564). This may become the AI regulation issue with the broadest public support, because it directly affects consumer wallets.

---

## The Federal Preemption Fight

While states are building a patchwork of AI regulations, the Trump administration is actively trying to tear it down.

### The Executive Order (December 11, 2025)

President Trump signed ["Ensuring a National Policy Framework For Artificial Intelligence,"](https://www.whitehouse.gov/presidential-actions/2025/12/eliminating-state-law-obstruction-of-national-artificial-intelligence-policy/) which established a **[DOJ AI Litigation Task Force](https://www.justice.gov/ag/media/1422986/dl?inline=)** (operational January 10, 2026) charged with [challenging state AI laws in federal court](https://www.bakerlaw.com/insights/navigating-the-emerging-federal-state-ai-showdown-doj-establishes-ai-litigation-task-force/) on grounds that they unconstitutionally burden interstate commerce or conflict with federal policy. The order directed the [Secretary of Commerce to review existing state AI laws by March 11, 2026](https://www.butzel.com/alert-department-of-commerce-report-on-state-artificial-intelligence-laws-expected-by-march-11-2026), identifying those deemed "overly burdensome." Perhaps most aggressively, the order conditioned **[$42 billion in BEAD broadband infrastructure funding](https://broadbandusa.ntia.gov/funding-programs/broadband-equity-access-and-deployment-bead-program)** on states repealing AI regulations deemed "onerous" — [using previously allocated funds as leverage](https://www.lawfaremedia.org/article/the-ai-preemption-executive-order-s-bead-strategy-faces-steep-legal-hurdles) against state regulatory independence.

### The Carve-Outs

The executive order does [carve out some areas from preemption](https://www.sidley.com/en/insights/newsupdates/2025/12/unpacking-the-december-11-2025-executive-order): child safety, AI compute and data center infrastructure, state government procurement and use of AI, and other topics to be determined later. These carve-outs suggest the administration recognizes some state regulation is politically untouchable.

### The National Policy Framework (March 20, 2026)

The White House followed up with a ["National Policy Framework for Artificial Intelligence"](https://www.whitehouse.gov/wp-content/uploads/2026/03/03.20.26-National-Policy-Framework-for-Artificial-Intelligence-Legislative-Recommendations.pdf) — [legislative recommendations](https://www.ropesgray.com/en/insights/alerts/2026/03/the-white-house-legislative-recommendations-national-policy-framework-for-artificial-intelligence-an) asking Congress to adopt legislation that would broadly preempt state AI laws imposing "undue burdens." This is not law — it is a policy wish list. But it signals the administration's endgame: a single federal framework that replaces most state-level AI regulation.

### Why It Matters

The legal question is whether the federal government can actually preempt state AI laws. Executive orders cannot override state law by themselves — that requires either an act of Congress or a federal agency regulation that explicitly preempts state authority. The DOJ task force can litigate, but courts will evaluate each state law on its own merits. And conditioning broadband funding on AI deregulation may face legal challenges of its own.

In the meantime, companies face a practical dilemma: do you comply with the strictest state law (California, typically) as your baseline, or do you wait to see whether federal preemption succeeds and some state requirements disappear? Most legal advisors are recommending the former — building for the strictest standard now, because unwinding compliance is easier than scrambling to add it later.

---

## What This Means for AI Developers

If you are building, deploying, or integrating AI systems in the United States, here is what the current landscape demands.

**If your system is used in hiring decisions:** You likely need bias audit capabilities, candidate notification workflows, and documentation of how your system makes recommendations. Illinois, New York City, and Colorado already require this. More states are coming.

**If your system generates images, video, or audio:** Content provenance metadata is becoming a legal requirement, not a nice-to-have. California's AB 853 is the leading edge, but federal legislation (the [COPIED Act](https://www.congress.gov/bill/119th-congress/senate-bill/1396/text)) would [extend provenance requirements nationally](https://www.commerce.senate.gov/2025/4/cantwell-blackburn-heinrich-reintroduce-bipartisan-bill-to-increase-transparency-combat-ai-deepfakes-put-journalists-artists-songwriters-back-in-control-of-their-content). Invest in C2PA or equivalent watermarking now.

**If you operate a frontier model:** SB 53 requires published safety frameworks and transparency reports. The threshold is $500 million in annual revenue, but smaller developers should expect similar requirements to cascade downward as more states legislate.

**If your system touches healthcare, finance, education, insurance, or housing:** Colorado's algorithmic discrimination law applies directly. Expect annual audits, attorney general reporting, and substantive performance standards — not just disclosure.

**If you sell AI products nationally:** Compliance with the patchwork means tracking requirements in every state where your users or customers reside. Multistate.ai and the IAPP maintain the most comprehensive trackers.

---

## What We Don't Know

**Will Congress actually pass preemptive legislation?** The White House framework is a recommendation, not a bill. Congress has been unable to pass comprehensive federal AI legislation so far. Bipartisan support exists for narrow issues (deepfakes, child safety) but not for broad preemption.

**How will the DOJ AI Litigation Task Force's challenges play out in court?** No significant rulings yet. Commerce Clause arguments against state AI laws are untested, and courts may be skeptical of sweeping preemption claims, particularly for laws that address local consumer harms.

**Will the $42 billion BEAD funding lever survive legal challenge?** Conditioning previously allocated infrastructure funding on unrelated policy goals has been challenged in other contexts. States may fight back.

**How strictly will state attorneys general enforce the new laws?** Colorado and Illinois have given enforcement authority to the attorney general with no private right of action. Enforcement will depend on political will, staffing, and whether high-profile cases emerge.

**What happens to the OpenAI, Google, Anthropic, and Meta compliance postures?** These companies already publish safety documentation and have internal governance processes. The question is whether state-specific requirements force them to publish different or additional disclosures, or whether their existing practices will satisfy the new laws.

---

## The Bottom Line

The United States is building AI regulation from the ground up — literally, at the state level. California, Texas, Colorado, and Illinois have established the templates. 41 other states are drafting their own versions. And the federal government is simultaneously trying to clear the field.

For AI developers, the practical advice is simple: build for California's standard. It is the strictest, the most detailed, and the most likely to survive a preemption challenge. Everything else can be layered on top.

The deeper question is whether a coherent national framework will emerge before the patchwork becomes unmanageable. Given that 1,561 bills are already in play and growing, that window may already be closing.

---

## Related Guides

- [OpenAI's Economic Blueprint: Robot Taxes and a Public Wealth Fund](/guides/openai-economic-blueprint-robot-taxes-wealth-fund/) — OpenAI's federal policy proposals that would preempt the state-level patchwork

---

*Last updated: April 9, 2026. We will update this article as major bills are signed into law or the federal preemption fight produces court rulings.*

