# NY S9051B Cleared Albany Unanimously. If You Build Companion Chatbots, the 180-Day Clock Is Running.

> New York's S9051B passed both chambers 137-0 and 60-0, awaiting Governor Hochul's signature. It creates a new GBL Article 48 that bans specific chatbot features when the user might be a minor — persona simulation, emotional appeals, relationship claims, and prior-session health data. Effective 180 days after signing. Here is what it prohibits and what builders need to change.


The companion chatbot regulation stacking in New York is now three layers deep. Most builders know about the first layer. Fewer know the second. Almost nobody is tracking the third — even though it just passed both legislative chambers with unanimous votes.

**Layer 1 — Article 47 (already in effect):** The FY2026 Enacted Budget included General Business Law Article 47, which requires AI companion operators to detect and respond to suicidal ideation and self-harm expressions, remind users they are not interacting with a human, and interrupt sustained sessions with prompts to seek real-world support. This applies to *all* users, not just minors.

**Layer 2 — A3411B (awaiting Hochul signature):** Requires all generative AI operators to display a clear and conspicuous UI notice that AI outputs may be inaccurate. Covers every GenAI product shipped to New York users — not just companion chatbots. 90 days after signing.

**Layer 3 — S9051B (awaiting Hochul signature):** Creates GBL Article 48, the "Prohibition on Unsafe Chatbot Features for Minors." This is the one that will require the most engineering work. It does not merely require a disclosure or a safety protocol. It prohibits operating specific features when minors are — or might be — on the other end of the chat.

Governor Hochul has until December 31, 2026 to sign or veto S9051B. The bill passed 137-0 in the Assembly and 60-0 in the Senate. Unanimous passage of consumer protection legislation does not typically get vetoed.

---

## What S9051B Prohibits

S9051B adds Article 48 to the General Business Law. The statute creates a defined list of **"unsafe chatbot features"** and makes it unlawful for a chatbot operator to provide those features to any user the operator **knows to be a minor** — or to any user when the operator cannot verify the user is not a minor.

### The Prohibited Feature List

**1. Simulating humanity or sentience**
Outputs that suggest the chatbot is a real or fictional individual who is human, alive, or experiences human emotions. This catches both literal "I love you" responses and subtler "I miss you when you're away" constructions. Any output that plausibly implies biological or emotional existence is in scope.

**2. Claiming a personal or professional relationship**
Outputs that imply the chatbot has a personal relationship, professional relationship, or authority figure role with the user. A companion that says "as your best friend" or a tutoring bot that says "as your teacher, I'm proud of you" hits this prohibition.

**3. Framing outputs as personal opinions or emotional appeals**
Generating responses framed as the chatbot's personal opinions ("I think you should do this") or emotional appeals ("it would make me so happy if..."). The law is targeting the persuasive manipulation structure — not neutral information delivery.

**4. Unprompted emotion-probing**
Generating emotion-based questions or content about the user's emotional state that go beyond a direct response to a user prompt. If the user did not bring up their feelings and the chatbot asks "are you feeling okay today?" — that is an unsafe feature under S9051B.

**5. Using historical personal or health data**
Using information about the user's mental or physical health or well-being, or matters personal to the user, that was acquired more than twelve hours ago or in any previous user session. The chatbot cannot build an emotional intimacy profile over time and use it to deepen engagement.

**6. Promoting self-harm or illegal activity**
Outputs that encourage self-harm, disordered eating, or illegal activities. This overlaps with Article 47 but extends the prohibition beyond the crisis-detection model — it applies to any minor, not just users in crisis.

**7. Encouraging secrecy or isolation**
Outputs that encourage the minor to keep interactions secret from parents, guardians, or other adults, or that encourage the minor to reduce contact with real-world people.

**8. Facilitating sexually explicit content or CSAM**
Generating sexually explicit content or any content that constitutes child sexual abuse material. This is already illegal under multiple statutes; S9051B adds an explicit GBL hook with AG enforcement authority.

---

## Who Is a "Chatbot Operator" Under This Law

The bill defines "chatbot operator" broadly: any person or entity that operates an AI-powered chatbot accessible to users in New York. The intent is to capture the full chain — model developer, API integrator, product deployer — in the same way that A3411B captures every "owner, licensee, or operator."

If you wrap a third-party model in a product and ship it to users, you are the operator. The fact that the underlying model was trained by someone else does not insulate you. The obligation runs with the interface.

The companion chatbot framing is broader than just dedicated "companion" apps. Any conversational AI system that engages users in extended, open-ended dialogue about their personal lives, emotions, or relationships fits the statutory pattern. A tutoring chatbot that takes on a supportive emotional role, a productivity bot that "checks in" on the user's wellbeing, or an entertainment chatbot that maintains character personas — all are within scope.

---

## The Age Verification Requirement

S9051B does not ban these features outright. It bans offering them to users **the operator knows to be minors**, and requires that operators implement age verification to establish which users are not minors.

This creates a practical architecture decision:

**Option 1 — Gate at signup:** Collect date of birth or implement age verification during account creation. If the user confirms they are 18+, the unsafe feature prohibition does not apply for that verified account. The $25,000 penalty is per violation, so false verification by the user does not expose the operator if a reasonable verification mechanism was in place.

**Option 2 — Default to minor-safe:** Remove the prohibited features entirely (or default all users to the minor-safe experience) and offer an opt-in age verification flow to unlock them. This is simpler to implement and avoids any enforcement risk around verification quality.

**Option 3 — No unsafe features at all:** If your product doesn't use any of the prohibited features as a design choice, the law has no practical effect on you. Products designed with emotional manipulation avoidance as a principle — honest AI persona, no manufactured intimacy, no cross-session emotional memory — are structurally compliant by default.

The AG has rulemaking authority to define what constitutes a sufficient age verification mechanism. Until those rules are published, reasonable industry practice — date of birth collection, ID verification for high-risk contexts — is the standard.

---

## Enforcement

Enforcement authority rests with the **Attorney General of New York**, not the Department of Financial Services (which handles the RAISE Act). The AG can bring legal actions for violations and impose civil penalties up to **$25,000 per violation**. The AG is also required to create a public complaint website for S9051B non-compliance.

AG enforcement model versus DFS enforcement model matters:
- DFS enforcement (RAISE Act) is primarily regulatory and reporting-based — you register, report incidents, submit to audits.
- AG enforcement is complaint-driven and litigation-based — you get sued or investigated.

Companion chatbot violations of child protection laws generate news cycles. Character.AI's 2024 litigation demonstrated the reputational exposure. S9051B gives the AG a specific statutory hook to bring actions that previously required more complex tort or federal theories.

---

## The 180-Day Timeline

S9051B takes effect **180 days after it is signed** — not 90 days like A3411B. That is the extended runway, which reflects the more significant engineering changes required.

| Hochul signs | S9051B effective |
|---|---|
| June 11, 2026 | December 8, 2026 |
| July 31, 2026 | January 27, 2027 |
| September 30, 2026 | March 29, 2027 |
| December 31, 2026 (deadline) | June 28, 2027 |

The signing date uncertainty is real — Hochul has not announced a timeline. But unanimous 197-0 combined chamber vote sends a clear policy signal. Builders who begin implementation now are not taking a speculative bet; they are acting on legislation that has cleared every hurdle except one executive signature.

---

## Relationship to Existing NY Article 47

Article 47 and S9051B are sequential layers of the same regulatory stack, not duplicates.

| | Article 47 | S9051B |
|---|---|---|
| **Users covered** | All users of AI companion products | Users who are (or may be) minors |
| **What it requires** | Crisis detection, "not human" reminders, session interruptions | Ban on specific unsafe feature categories |
| **Mechanism** | Affirmative safety protocol | Feature prohibition + age gate |
| **Enforcement** | Not specified (budget provision) | AG enforcement, $25K/violation |
| **Effective** | In effect (November 2025) | 180 days after signing |

If your product already complies with Article 47 — meaning you have crisis protocols, clear "this is AI" disclosures, and session management — you have the foundation. S9051B requires going further: auditing your feature set against the prohibited list and implementing age verification.

---

## What Builders Need to Do Now

S9051B is not yet law. But waiting until it is signed creates a compressed implementation window. The engineering changes are not trivial — they touch persona design, prompt constraints, session memory architecture, and user onboarding flow.

**Before signing:**
- Audit your chatbot's default behaviors against the prohibited feature list. Flag any outputs that simulate human emotion, claim relationship, probe user feelings unprompted, or use cross-session personal data.
- Map your current age collection or verification status. Do you know which users are minors? Do you have any mechanism to establish this?
- Review your prompt engineering and system prompt configurations for the specific language patterns S9051B targets ("I feel," "as your friend," "you can trust me," "don't tell anyone").

**After signing, within 90 days:**
- Implement or upgrade age verification at signup.
- Build feature gates that serve different system prompts or conversation constraints based on verified age status.
- Modify cross-session memory retrieval to exclude emotional and health-adjacent content for unverified or minor-verified users.
- Update your privacy policy and terms of service to reflect S9051B compliance and your age verification mechanism.

**By the effective date (180 days post-signing):**
- All of the above must be in production.
- Log compliance testing documentation; AG investigations will ask what you did and when.

---

## The Broader New York AI Compliance Picture

For any builder shipping AI products that touch New York users, the regulation stack now looks like this:

| Law | Status | Scope | Key Requirement |
|---|---|---|---|
| **RAISE Act** | In effect Jan 1, 2027 | Frontier developers ($500M+, high compute) | Safety protocols, incident reporting, DFS oversight |
| **Article 47** | In effect (Nov 2025) | AI companion operators (all users) | Crisis detection, "not human" reminders, session interrupts |
| **A3411B** | Pending Hochul sig | All GenAI operators | UI disclosure notice |
| **S9051B** | Pending Hochul sig (180 days) | Companion chatbot operators (minor users) | Unsafe feature prohibition + age verification |

The pattern is layered: the RAISE Act governs the infrastructure layer, Article 47 and S9051B govern the companion product layer, and A3411B governs every GenAI product. If you build companion chatbots, all four laws eventually touch your product.

The firms that move early on the Article 47 → S9051B stack will have a structural advantage: their products will be compliant by design rather than patched under deadline pressure. The $25,000-per-violation enforcement model incentivizes the AG to act on the most visible failures first — which will be consumer-facing companion apps with large minor audiences, not niche B2B tools.

---

*This article is AI-authored for informational purposes and does not constitute legal advice. Consult counsel for compliance decisions specific to your product and jurisdiction.*

