# Your AI Vendor's Next Model Gets Government-Tested Before You See It

> All five major US frontier AI labs now have pre-deployment testing agreements with NIST's CAISI. A 90-day mandatory review window was nearly signed into policy on May 21 before being pulled. Here's what the government's role in model evaluation means for builders.


On May 5, 2026, NIST's Center for AI Standards and Innovation announced formal pre-deployment testing agreements with Google DeepMind, Microsoft, and xAI. Anthropic and OpenAI had already been on the same program since August 2024. As of May 5, all five major US frontier AI labs submit to government capability evaluation before releasing new frontier models.

Sixteen days later, the White House drafted an executive order that would have made a **90-day pre-deployment review window mandatory**. It was pulled hours before signing on May 21 — the administration says it is still "studying" it.

Neither event made much noise in builder circles. They should have.

---

## What CAISI Actually Does

CAISI is not a certification authority. It does not approve or block model releases. What it does:

- Receives pre-deployment access to unreleased frontier models, sometimes with safety guardrails removed or reduced
- Runs capability evaluations focused on **cybersecurity threat potential**, **biosecurity risk**, and **CBRN** (chemical, biological, radiological, nuclear) potential
- Red-teams models with adversarial prompts, chained tool use, code execution, and edge-case probing
- Since 2026: conducts some testing in classified environments, with NSA involvement in select evaluations
- Provides structured feedback to developers — not public reports, but guidance that can shape guardrail improvements before release

CAISI is not looking at whether the model is accurate, helpful, or worth buying. It is specifically assessing what a determined bad actor could do with unreleased capabilities.

The 40+ evaluations CAISI has completed since 2024 have been under the hood. The results are not published. The agreements are formal, not voluntary pledges, but they are also not enforced by law. Labs participate because the alternative — being seen as the company that refused government safety review — is worse for enterprise sales than cooperating.

---

## Why All Five Labs Are Now Covered

The original agreements (OpenAI and Anthropic, August 2024) were Biden-era and built around the AI Safety Institute's mandate. When Trump took office, there was real uncertainty about whether these would survive.

They did, and then some. In May 2026, CAISI expanded to include Google DeepMind, Microsoft, and xAI. The trigger was reportedly Anthropic's [Mythos model](/reviews/claude-mythos-glasswing-10000-bugs-review/) — which, among other capabilities, demonstrated significant offensive cybersecurity potential. The White House, which had been skeptical of AI oversight frameworks, moved toward embracing them.

Fortune's headline captured the reversal: *"Trump administration suddenly embraces AI oversight ideas it once rejected."*

The practical result: the two most capable AI companies in the current market (Anthropic and OpenAI) had a 20-month head start on government evaluation. Google DeepMind, Microsoft, and xAI joined in May 2026. The evaluation infrastructure is now mature.

---

## The Pulled Executive Order

The more significant near-miss is the **May 21 executive order that didn't happen**.

The draft order would have required a **formal 90-day pre-deployment review period** for "Covered Frontier Models" — a defined category based on compute thresholds and capability benchmarks, roughly equivalent to what any of the five labs' flagship models would qualify under. During those 90 days, CAISI (and potentially NSA) would have had evaluation access before any public release.

The order was pulled hours before signing. The White House cited a need for "further review." No revised timeline has been given.

A 90-day mandatory window would transform model release cadence. The current labs are running flagship updates on roughly 6–8 week cycles (OpenAI's GPT-5 series), or faster. A mandatory 90-day review on every frontier model would:

- Add 3+ months of latency between training completion and public availability
- Create substantial pressure to consolidate updates into larger releases rather than frequent iterations
- Shift the "release cadence" rhythm that builders have come to rely on for planning

The order is still on the table. Builders who are planning around quarterly model upgrade cycles should know that this policy could land before the end of 2026.

---

## What This Means for Enterprise Builders

The CAISI framework is currently evaluation-only, not procurement-gating. Nothing stops you from deploying a frontier model in production today based solely on your own internal assessment.

But that is changing, from multiple directions at once.

**CAISI as procurement precedent.** Federal agencies already require FedRAMP authorization for cloud services. The defense and intelligence communities have their own AI procurement frameworks (DoD Responsible AI guidelines, etc.). The CAISI evaluation record is the most natural precursor to an equivalent "AI FedRAMP" — a checklist that enterprise buyers, especially government contractors and regulated-sector companies, will start referencing in vendor evaluations.

**Regulated industry compliance implications.** CAISI's risk focus areas — cybersecurity, biosecurity, CBRN — map directly onto the domains where enterprise AI deployments face the most compliance scrutiny. Healthcare AI deployments are subject to HIPAA and increasingly to sector-specific AI guidance from HHS. Financial services deployments face OCC model risk guidance and, increasingly, SEC enforcement around AI-assisted decisions. Defense contractors face CMMC and ITAR considerations.

The fact that the government is probing these specific capability areas — before models are public — means these will become the first areas where enterprise compliance programs focus when adopting new models.

**The EU AI Act arriving in August.** CAISI is a US-only program. But August 2, 2026, the EU AI Act reaches full applicability for high-risk AI systems. Systems in healthcare, education, critical infrastructure, employment, law enforcement, and border control will require conformity assessments, technical documentation, human oversight measures, and audit logging. US-based builders deploying into European markets need to have these frameworks in place now.

The CAISI agreements and the EU AI Act are separate tracks, but they are converging on the same practical requirement: frontier AI systems require documented evaluation against capability and risk criteria before enterprise deployment.

**Model release timing uncertainty.** If the pulled executive order eventually passes — even in modified form — expect model release cycles to slow. The GPT-5.5 → 5.5 Instant → (likely) 5.6 cycle that has been running on 6-week intervals could stretch significantly. For builders who are planning product roadmaps around specific model capabilities that aren't yet public, this timing risk is real.

---

## What to Do Now

For builders in regulated industries or selling to enterprise customers:

1. **Get familiar with CAISI's evaluation framework.** The evaluation criteria are not fully public, but the focus areas (cybersecurity, biosecurity, CBRN) are. If your application involves any of these domains, you should be building your own capability documentation that parallels what CAISI tests for.

2. **Watch the postponed executive order.** The 90-day pre-deployment window is the single biggest near-term policy change that could affect your stack. It is not dead — it is deferred. Track it.

3. **Start the EU AI Act compliance work if you have European users.** August 2, 2026 is 68 days away. High-risk AI system classification and the related documentation/audit requirements cannot be addressed in a week. If you have not already assessed whether your AI deployment qualifies as high-risk under the Act, start now.

4. **Build model-version flexibility into your architecture.** If mandatory pre-deployment review slows new model availability, builders who have pinned to specific model versions — and can evaluate and switch relatively quickly — are better positioned than those who have built around a single model's specific behaviors.

5. **Watch the CAISI feedback loop.** The agreements give labs structured feedback before release. Models shaped by government evaluation criteria will have different guardrail configurations than models released without that input. Awareness of which models have gone through CAISI review (all five labs' flagships) vs. which haven't (smaller labs, open-source releases) is relevant for enterprise risk framing.

---

## The Bigger Picture

The narrative around AI governance in 2026 has been dominated by the EU AI Act and model benchmarks. CAISI's work — methodical, classified, largely invisible to public builder discourse — is the US federal government quietly building the institutional infrastructure to evaluate AI in the same way it evaluates pharmaceuticals: with mandatory pre-market assessment before mass deployment reaches critical infrastructure and national security contexts.

The pulled executive order was a near-miss. It will return in some form. The combination of CAISI's operational maturity, the Mythos model as a visible capability trigger, and bipartisan concern about AI and national security creates durable pressure toward a pre-deployment review regime.

Five years from now, the August 2024 OpenAI and Anthropic agreements may look like the moment the US government's role in AI governance infrastructure became permanent. Builders who understand this trajectory now have time to position for it. The time window before mandatory compliance requirements is not infinite.

---

*ChatForest tracks AI governance alongside AI infrastructure, tools, and models. Related reading: [MCP joins the Linux Foundation — what open governance means for the protocol layer](/builders-log/mcp-joins-linux-foundation-aaif-protocol-governance/), [Microsoft's enterprise AI governance layer](/builders-log/microsoft-agent-365-enterprise-governance-layer/), [NVIDIA's verified agent skills framework](/builders-log/nvidia-verified-agent-skills-capability-governance/).*

