# Google Marketing Live 2026 Review — Gemini Now Runs Every Layer of the Ad Stack

> Google Marketing Live 2026 introduced four new Gemini-powered ad formats for AI Mode and Search, a unified cross-platform agent called Ask Advisor, and agentic commerce protocols — here is what changed and what it means for advertisers.


Google Marketing Live 2026 happened on May 20, one day after Google I/O. If I/O was about what Gemini can do, GML 2026 was about how Google plans to make money from it.

The answer: rebuild every layer of the advertising stack around AI.

Four new ad formats that embed Gemini directly into the ad unit. A unified cross-platform agent that replaces separate advisory tools across Google Ads, Analytics, Merchant Center, and Google Marketing Platform. New commerce protocols designed to let AI agents complete purchases on users' behalf. And a revenue base already growing fast: ads now appear in 25.5% of AI Overview search results pages — up from roughly 3% in January 2025.

This is a review of what changed at GML 2026 and what it means for advertisers who depend on Google Search.

---

## What Google Marketing Live Is

Google Marketing Live is Google's annual advertising keynote — the event where new campaign types are introduced, major platform changes are announced, and the strategic direction of Google Ads is made explicit for agencies and advertisers. It is the ad-industry equivalent of I/O.

The 2026 event ran virtually on May 20, with an EMEA follow-up on May 21. The framing was explicit: Gemini is now the core infrastructure of Google's advertising products, not a feature layer on top of them.

---

## Four New Ad Formats

### 1. Conversational Discovery Ads

Conversational Discovery Ads appear inside AI Mode, Google's Gemini-powered conversational search interface. When a user asks a question — say, "what is the best way to make my bathroom smell like a spa" — the AI generates a response. The Conversational Discovery Ad answers that same question from an advertiser's perspective, with Gemini generating bespoke ad copy that highlights relevant product features for the specific query.

The match is bidirectional: Gemini maps the ad to both the query and the AI-generated response surrounding it. The goal is that the ad reads as relevant to the conversation, not as an interruption from outside it.

This is a meaningfully different format from traditional keyword-matched display or search ads. The ad copy is generated at auction time, not written in advance by the advertiser. Google is using advertiser-provided product information and Gemini to produce ad creative on the fly.

### 2. Highlighted Answers

When AI Mode generates a list — the top five language apps for an upcoming trip, the best espresso machines under $500, recommended plumbers in Denver — ads are eligible to appear inside that list as **Highlighted Answers**. A sponsored placement appears alongside the AI's organic recommendations, clearly labeled.

The placement only fires when Google's systems determine the advertiser's offering is highly relevant to the user's specific request. Relevance is determined algorithmically, not through manual bid adjustments.

For advertisers, this is closer to being included in an AI recommendation than buying a position on a keyword. The traffic intent at this placement is high — users are asking for a recommendation — but the advertiser has limited control over which queries trigger the placement.

### 3. AI-Powered Shopping Ads

For e-commerce advertisers, AI-powered Shopping Ads use Gemini to generate custom product explainers for each individual product surfaced. If a user searches for "espresso machines," Gemini writes a short explanation of why each surfaced machine may fit the shopper's needs — drawing on product specifications, reviews, and the user's query context.

Each ad also includes an independent AI explainer written from product data, separate from the advertiser's own creative, as a transparency measure. Google describes this as making the synthesized context visible to the user.

This format builds on the existing Shopping Ads infrastructure. Advertisers using Performance Max campaigns may already be eligible for placement in this format — which Google noted means some advertisers may be appearing in AI Mode shopping placements without being aware of it.

### 4. Business Agent for Leads

Business Agent for Leads is the most conceptually novel format. It puts a Gemini-powered brand chatbot directly inside the ad unit. Instead of clicking through to a landing page or filling out a static contact form, users click a "Chat" button inside the ad and are connected to a conversational agent trained on the advertiser's website content.

The use case Google demonstrated at GML was a student researching universities: the student sees a sponsored ad from a university, clicks Chat, and gets instant answers to specific admissions questions from an AI trained on that institution's published information, without leaving the Google interface.

The format sits at the intersection of lead generation and conversational AI. It reduces the click-through step — instead of driving traffic to a landing page and losing the user to a form, the lead conversation happens inside the SERP. The lead data from that conversation is passed to the advertiser.

---

## Ask Advisor: A Unified Cross-Platform Agent

Beyond new ad formats, Google announced **Ask Advisor** — a unified agent built with Gemini that spans Google Ads, Google Analytics, Merchant Center, and Google Marketing Platform simultaneously.

Ask Advisor consolidates separate advisory tools that previously existed in isolation: Smart Campaigns suggestions in Ads, anomaly explanations in Analytics, catalog health alerts in Merchant Center. A user can ask Ask Advisor a single question — "why did my ROAS drop last Thursday?" — and the agent pulls signals across all four platforms to construct an answer, without the user switching between dashboards or rebuilding context.

This is a significant operational shift for agencies and in-house teams managing complex Google stacks. The value is not in any single data point but in the cross-platform synthesis. Ask Advisor is available in beta to Google Ads users.

---

## Agentic Commerce: AP2, UCP, and Universal Cart

Google also announced infrastructure changes for AI-assisted shopping that go beyond traditional ad formats.

**Agent Payments Protocol (AP2)** is a new standard that allows AI agents — including Gemini Spark, Google's 24/7 personal agent — to complete purchases on behalf of users without requiring them to re-enter payment information or navigate to a merchant site. For advertisers, AP2 means a user could see a Business Agent for Leads interaction, decide to buy, and complete the transaction through the agent without leaving the conversational interface.

**Universal Commerce Protocol (UCP)** is a product data standard that allows merchants to share a single structured product feed that works across Gemini in Search, Gemini Spark, Shopping, and third-party AI agents that support the protocol. It replaces the need to maintain separate data feeds for each surface.

**Universal Cart** is a cross-merchant cart that allows users to add products from different retailers into a single cart and check out once. It works across AP2-compatible merchants.

Together, these three infrastructure pieces suggest Google is building toward a future where a user's AI agent — Gemini Spark — can browse, compare, and purchase across multiple merchants in a single conversational session, with the transaction plumbing already in place.

---

## Revenue Context

The scale of Google's AI search advertising is already significant.

Google Search generated $63 billion in Q4 2025 revenue. Ads now appear in approximately 25.5% of AI Overview search result pages — up from roughly 3% in January 2025, a 394% year-over-year increase. Google AI Mode, which runs a full Gemini-powered conversational search experience, had 75 million monthly active users at the time of GML 2026.

The new formats announced at GML are layered on top of that existing revenue base. Conversational Discovery Ads and Highlighted Answers add new inventory inside AI Mode; AI-powered Shopping Ads add Gemini-generated creative to existing Shopping infrastructure; Business Agent for Leads creates a new conversion pathway that did not exist before.

---

## How This Compares to OpenAI's ChatGPT Ads Manager

OpenAI [launched ChatGPT Ads Manager](/reviews/openai-chatgpt-ads-manager-self-serve-advertising-review/) as a self-serve beta on May 5, 2026 — fifteen days before Google Marketing Live.

The two systems are in different weight classes.

ChatGPT Ads Manager has one format (the chat_card, placed below the AI response), CPC bids of $3–$5, CPMs of $25–$60, and no minimum spend. It is a clean, honest early product with limited targeting transparency and no established conversion benchmarks. Its explicit no-influence policy means the ad sits beside the AI response, not inside it.

Google's new formats operate at orders-of-magnitude larger scale (63B/quarter vs OpenAI's $2.5B/year target), use Gemini to generate ad creative on the fly inside the response rather than adjacent to it, and add agentic commerce infrastructure that lets AI agents complete purchases end-to-end. The Business Agent for Leads format goes further than anything ChatGPT Ads Manager offers — it creates a full conversational sales interaction inside the ad unit itself.

The meaningful gap for now is reach: ChatGPT Ads Manager is available to any US advertiser with a credit card. The new Google formats are rolling out in limited beta, with prioritized access going to Performance Max and Smart Campaigns advertisers. Scale of rollout will determine which format shapes the emerging conventions for AI advertising.

---

## What Advertisers Should Do

**If you run Performance Max campaigns**, check whether your ads are already appearing in AI Mode Shopping placements. Google indicated that existing P-Max campaigns may already be triggering new AI-powered Shopping Ads formats without opt-in. Review your placement data now.

**If you run lead generation campaigns**, Business Agent for Leads is worth evaluating for high-consideration products and services where a quick conversational answer removes buying friction. The format should perform well wherever user questions are complex and a good answer converts. University enrollment, financial services, healthcare, B2B software.

**If you use Google Ads, Analytics, Merchant Center, and GMP together**, Ask Advisor beta access is worth applying for. The cross-platform synthesis — one query, four data sources — is a genuine operational gain for teams managing complex accounts.

**On measurement**: none of the new formats have established conversion benchmarks. Anyone who tells you definitively whether Conversational Discovery Ads out-convert standard search ads does not have the data yet. Treat GML 2026 as the starting gun for building that data internally, not as a reason to reallocate budget before results are in.

**On agentic commerce**: AP2 and UCP are infrastructure plays that matter most to e-commerce retailers. If your platform can support structured product feeds, prioritize UCP compatibility — it positions your inventory for discovery by Gemini Spark agents as agentic shopping behavior grows.

---

## Rating: 4 / 5

Google Marketing Live 2026 is the most significant overhaul of the Google Ads platform in a decade. The shift from keyword-matched ads to AI-generated conversational formats is structural, not cosmetic.

The rating is not 5/5 for the same reason the ChatGPT Ads Manager got 3.5/5: new formats without conversion data are still experiments, and advertisers are being asked to invest in infrastructure — new format structures, new feed standards, new agent protocols — whose returns are unproven at scale.

What is not experimental is the trajectory. Ads now appear in a quarter of all AI Overview SERPs, nine months after AI Overviews launched. The pace of monetization is faster than most industry observers predicted. Advertisers who dismiss GML 2026 as a roadmap event and wait for "proven" results risk watching their competitors build first-mover data advantages in formats that are already live.

Google is not asking advertisers whether AI advertising is coming. It is asking them how quickly they want to catch up.

---

*ChatForest covers AI tools for professionals and developers. This review is based on publicly available announcements, Google's own blog posts, trade reporting from Search Engine Land, WordStream, and CMSWire, and Google's published Marketing Live documentation — not direct advertiser access to the new formats.*

