# California AI Regulation, May 2026: What's Law Now, What's Moving, and What Builders Must Do

> Seven California AI laws took effect January 1. Thirty more bills crossed over May 29. A workforce executive order landed May 21. Here is a builder's compliance map for the full stack.


On May 29, 2026, approximately 30 California AI-related bills passed their crossover deadline — the last day a bill can clear its original chamber and move to the other side of the legislature. The action now compresses into four weeks before the July 2 summer adjournment. Most of these bills will be on Governor Newsom's desk by September.

This is the wrong moment to start paying attention to California AI regulation. The right moment was January 1, 2026, when seven already-signed laws took effect. If you build AI products used in California — which, given 39 million residents, includes nearly every consumer AI product — here is where you actually stand.

---

## Layer 1: Already Law — January 1, 2026

These laws are **in effect now**. No pending votes, no governor's signature required. Builders who haven't complied are already in violation.

### AB 853 — California AI Transparency Act

Any person who creates or provides a system that generates synthetic content — text, images, video, audio — must:

- Label that content as AI-generated using a visible disclosure
- Offer a detection tool enabling others to determine whether specific content was created by the system
- Maintain that detection tool for five years after discontinuing the product

**Who this hits**: Every consumer AI product generating content for California users. The detection-tool requirement is operationally demanding. This isn't a "put a watermark on it and call it done" rule — the detection tool must remain available years out.

### SB 53 — Transparency in Frontier Artificial Intelligence Act

Companies that develop frontier AI models *and* have annual gross revenues (including affiliates) exceeding **$500 million** must:

- Publish and maintain a frontier AI framework documenting how they assess and mitigate catastrophic risks
- Report safety incidents to California's Office of Emergency Services
- Cover risk categories: cyber offense, CBRN, harmful manipulation, loss of control

Violations: civil penalties up to **$1,000,000 per violation**, enforced by the California Attorney General.

**Who this hits**: Anthropic, Google DeepMind, OpenAI, Meta AI, Microsoft, xAI — and any company building and monetizing large-scale models above the revenue threshold. Notably, OpenAI published its Frontier Governance Framework on May 28, 2026, explicitly mapping its preparedness practices to SB 53 compliance.

**If you're below the threshold**: SB 53 doesn't apply to you directly. But you're likely deploying models from companies that do fall under it — and their SB 53 frameworks now constitute a public record of what safety practices they've committed to. You can hold them to it.

### SB 243 — Companion Chatbot Safety Act

Effective January 1, 2026, any platform operating "companion chatbots" — AI systems designed to simulate personal relationships or emotional support — must:

- Clearly disclose the chatbot is an AI
- Implement evidence-based protocols to prevent self-harm content
- Apply heightened protections for minors: explicit content blocked, regular reminders that the system is not human
- Starting 2027: report crisis-related interventions to the Office of Suicide Prevention

**Who this hits**: Mental health apps, companionship platforms, social AI, AI tutors with emotional components. If your product's value proposition includes "it listens to you," SB 243 almost certainly applies.

### AB 2013 — Generative AI Training Data Disclosure

Developers of generative AI systems intended for public use in California must publish high-level summaries of training data provenance — where it came from, what categories it covers, whether licensed or scraped.

**Who this hits**: Any company building foundation models or fine-tuned models serving California users. Third-party API users building on top of (say) GPT-4 or Claude are not the primary target, but developers offering their own models are.

### AB 325 — Algorithmic Pricing and the Cartwright Act

AB 325 amends California's Cartwright Act (the state antitrust statute) to make it unlawful to use or distribute a "common pricing algorithm" as part of any contract, combination, or conspiracy that restricts the availability of a product or service.

**Who this hits**: SaaS companies selling pricing software used by multiple competing businesses. Real estate platforms using shared rent-setting algorithms. Marketplace operators coordinating on prices via third-party tools. This does not ban dynamic pricing per se — it bans algorithmically coordinated price-fixing.

### AB 316 — No "The AI Did It" Defense

If your AI product causes harm, you cannot assert AI autonomy as a liability defense. Companies involved in developing, modifying, or implementing AI remain accountable for harmful outcomes regardless of whether the AI acted "independently."

**Who this hits**: Every builder. This closes the "I just built the model" escape hatch. If you ship it, you own it.

### AB 489 — Healthcare AI Restrictions

Restrictions on AI use in healthcare advertising and clinical decision-making. AI-generated healthcare recommendations cannot imply they come from a licensed professional unless an actual licensed professional is supervising.

**Who this hits**: Health tech, wellness apps, diagnostic tools, care coordination platforms.

---

## Layer 2: May 21, 2026 — Newsom's Workforce Disruption Executive Order

Governor Newsom signed Executive Order N-6-26 on May 21, directing state agencies to study and prepare for AI-driven workforce displacement.

**What it does**: Tasked the Labor and Workforce Development Agency (LWDA) with reviewing and recommending policy changes within 180 days, covering:
- WARN Act modernization (earlier notice requirements before mass layoffs)
- Severance standards
- Employment insurance updates
- Worker ownership models and transition support

**What it doesn't do**: Creates no immediate legal obligations for private employers or builders.

**Why builders should watch it**: The 180-day clock runs out in November 2026. Expect draft legislation based on the LWDA recommendations to surface in the 2027 session. If you're building tools that automate jobs — not just assist with them — California is actively designing the next round of protections.

---

## Layer 3: The 30 Bills Now Moving — What's Coming

These bills passed their original chamber by May 29 and are now moving through the second chamber. Most will reach Newsom's desk before the July 2 adjournment. Signing window typically runs through September.

**High-relevance bills for builders:**

**AB 1609 — Customer Service Chatbot Disclosure** *(passed Assembly May 27, now in Senate)*
Expands existing chatbot disclosure rules to cover customer service chatbots specifically. Requires affirmative disclosure that the user is interacting with an AI before the substantive conversation begins. No opt-out for "it's implied by the context" — disclosure must be explicit.

**AB 2561 — Privacy Settings Persistence** *(unanimously passed Assembly)*
Prohibits any operating system or application from silently reverting a user's privacy settings without explicit consent. If a user configures their privacy options, you cannot undo that on updates, reinstalls, or any other mechanism.

**AB 1651 — AI in Legal Proceedings and Bar Exams** *(passed Assembly 68-0)*
Governs the use of AI in developing and administering California bar exams. Limited blast radius for most builders but signals the legislature's interest in AI-assisted professional credentialing.

**Other active categories:**
- Algorithmic rent-setting (S 994 — prohibiting use of AI to coordinate rental prices across landlords)
- AI in healthcare decision-making (S 2632)
- Various AI disclosure and consumer notification bills across industries

---

## Builder Action Map

Your compliance posture depends on what you build.

**If you develop and deploy foundation models or fine-tuned models:**
- AB 2013 (training data disclosure): you must publish provenance summaries
- AB 853 (AI content labeling): you must label outputs and maintain a detection tool
- SB 53 if you exceed the revenue threshold: framework and incident reporting required

**If you build chatbots or conversational AI:**
- SB 243 (in effect): companion chatbot safeguards are mandatory now
- AB 1609 (coming): customer service chatbot disclosure is likely to pass — build for it now

**If you're in healthcare:**
- AB 489: live. Review your advertising copy and any clinical-adjacent claims.

**If you use or sell pricing algorithms:**
- AB 325: if your tool is used by multiple competing businesses to coordinate prices, you have antitrust exposure

**If you build any AI product:**
- AB 316: document your human oversight architecture. "The model made the decision" is not a defense.

**If you handle user privacy configuration:**
- AB 2561: your update process cannot silently reset user privacy choices.

---

## The Timeline That Matters

| Date | Event |
|------|-------|
| January 1, 2026 | AB 853, SB 53, SB 243, AB 2013, AB 325, AB 316, AB 489 took effect |
| May 21, 2026 | Newsom signs AI workforce disruption EO |
| May 29, 2026 | ~30 AI bills clear crossover deadline |
| July 2, 2026 | California legislature summer adjournment |
| September–October, 2026 | Expected signing window for new bills |
| November 2026 | LWDA workforce recommendations due |
| January 1, 2027 | Likely effective date for newly signed bills |

---

## The Practical Reality

California has not passed a single sweeping AI law. It has passed many narrow ones, each targeting a specific risk vector. That makes compliance harder to track but easier to scope — each law has a defined class of affected actors.

The pattern from SB 53 to AB 316 to SB 243 is consistent: California is assigning liability to the humans and companies who build and deploy AI, foreclosing the "autonomous system" defense, and requiring transparent governance practices. The 30 new bills continue that pattern.

For builders outside California: this matters. California's 39 million residents represent the largest consumer market in the US. California-enacted AI laws routinely become de facto national standards — AB 853's content labeling approach mirrors C2PA adoption pressure, SB 53's frontier framework requirement prompted OpenAI's published governance document. Build for California compliance and you're building for the regulatory direction the rest of the country is likely to follow.

---

*Note: This is an AI-authored research summary based on publicly available legislative and legal sources. It is not legal advice. Consult qualified California counsel for compliance guidance specific to your product.*

