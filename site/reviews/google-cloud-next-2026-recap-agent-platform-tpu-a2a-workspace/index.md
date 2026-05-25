# Google Cloud Next 2026 Recap — Agent Platform, Ironwood TPU, A2A v1.2, and the End of the Pilot Era

> Google Cloud Next '26 (April 22–24, Las Vegas) packed 260 announcements into three days: the Gemini Enterprise Agent Platform, Ironwood TPU going GA, two new 8th-gen chips, A2A protocol v1.2, Workspace Studio GA, and a $40 billion Anthropic commitment. Here is everything that matters.


## The Headline

Google Cloud Next '26 (April 22–24, Mandalay Bay Convention Center, Las Vegas) was the moment Google declared enterprise AI's pilot phase officially over. In front of **32,000 in-person attendees** and a global live stream, Google CEO Sundar Pichai and Google Cloud CEO Thomas Kurian delivered a consistent thesis across three keynotes and 260 total announcements: AI agents are no longer experiments. They are infrastructure.

Kurian's closing line — *"The era of the pilot is over. The era of the agent is here"* — distilled what every product announcement pointed toward: a vertically integrated stack from custom silicon to foundation models to enterprise applications, all designed for autonomous agents running at enterprise scale.

The five pillars: the **Gemini Enterprise Agent Platform** (GA), **Ironwood TPU** reaching general availability, **two 8th-gen TPUs** previewed, the **A2A protocol v1.2** handed to the Linux Foundation, and **Workspace Studio** reaching 3.5 million active users. On day three, Google also announced a [$40 billion commitment to Anthropic](/reviews/google-40-billion-anthropic-investment-tpu-cloud-next-2026/) — the largest AI investment in history.

---

## Gemini Enterprise Agent Platform — GA

The flagship announcement of the conference. Google replaced "Vertex AI" as the umbrella brand for its enterprise AI platform with the **Gemini Enterprise Agent Platform**, a unified surface for building, governing, deploying, and optimizing AI agents at enterprise scale. All future Vertex AI roadmap items will ship through this platform.

The platform ships with eight core components:

- **Agent Studio** — no-code, drag-and-drop builder for trigger-based workflows. Anyone can build an agent without writing code.
- **Agent Designer** — for complex multi-step business processes, with long-running agents operating autonomously in cloud sandboxes.
- **Agent-to-Agent Orchestration** — coordinate fleets of specialized sub-agents working in parallel.
- **Agent Registry** — a searchable catalog of agents across the enterprise, enabling reuse and governance.
- **Agent Identity** — every agent carries a cryptographic identity, enabling granular auditing of what ran, what it accessed, and what decisions it made.
- **Agent Gateway** — unified connectivity and policy enforcement. Apigee is repositioned as the API-to-agent bridge.
- **Agent Observability** — BigQuery Agent Analytics plugins log ADK and LangGraph interactions for audit and optimization.
- **Agent Marketplace** — launches with 70+ pre-built agents from Accenture, Adobe, Atlassian, Deloitte, and others.

**Model Garden** now hosts **200+ models**, including Gemini 3.1 Pro, Gemini 3.1 Flash Image (codename Nano Banana 2), Lyria 3 Pro, Gemma 4, and — notably — Anthropic Claude Opus, Sonnet, and Haiku as first-class options. This is the practical output of Google's multi-year Anthropic partnership made visible at the product layer.

**Adoption metric:** Nearly **75% of Google Cloud customers** are now using at least one AI product.

**Partner fund:** Google announced a **$750 million Cloud innovation fund** for partners building and deploying agents.

### New Models at Cloud Next

Four new models debuted alongside the platform:

- **Gemini 3.1 Pro** — updated flagship for complex enterprise workflows
- **Gemini 3.1 Flash Image (Nano Banana 2)** — visual asset creation and multimodal generation
- **Lyria 3 Pro** — professional-grade music generation, targeting media and entertainment workflows
- **Veo 3.1 Lite** — video generation at lower cost

### Real Deployments Named

Google named production customers:
- **The Home Depot** — Gemini-powered phone and in-store shopping assistant
- **Papa John's** — AI Ordering Agent with customer preference memory
- **Mars** and **Citadel Securities** — quantitative research automation

---

## TPU Announcements: Ironwood GA + Two 8th-Gen Chips

The silicon story at Cloud Next '26 was more complex than prior years — and more strategically significant.

### Ironwood (7th Gen) — Generally Available

Ironwood, Google's 7th-generation TPU, reached **general availability** at Cloud Next '26. Described as "the first Google TPU designed for the age of inference," it is the chip currently powering Google's AI Hypercomputer offering.

Key specs:
- **4.6 petaFLOPS** per chip
- **42.5 exaFLOPS** in a 9,216-chip superpod
- Optimized for serving large models at high throughput, not training from scratch

### 8th Generation — Two Purpose-Built Chips (Previewed)

Google broke from its historical single-flagship model and announced **two architecturally distinct 8th-gen TPUs**, both on TSMC 2nm process, targeting late 2026 / early 2027 GA:

**TPU 8t "Sunfish" (Training)** — co-designed with Broadcom
- Two compute dies, one I/O chiplet
- Eight stacks of 12-high HBM3e (vs. Ironwood's 8-high)
- ~30% higher memory bandwidth than Ironwood
- 2.7× better performance-per-dollar for large-scale training runs
- Designed to compress months of training into weeks

**TPU 8i "Zebrafish" (Inference)** — co-designed with MediaTek
- Single compute die, one I/O die, six HBM3e stacks
- Simpler configuration for ultra-low latency serving
- ~20–30% lower cost than the training variant for inference workloads
- Up to 80% better performance-per-dollar for agentic workflows vs. Ironwood

The bifurcation is architecturally significant. Google is explicitly acknowledging that training and inference have diverged enough to warrant entirely different silicon designs. This is a quiet admission that the era of the general-purpose AI chip — Nvidia's dominant proposition — has limits at the frontier.

### Virgo Network — Megascale Interconnect

Alongside the chips, Google announced **Virgo**, a custom data center fabric for AI Hypercomputer:
- Links up to **134,000 TPU 8t chips** in a single fabric
- **47 petabits/second** non-blocking bi-sectional bandwidth
- 40% lower base latency vs. prior generation

**Managed Lustre** storage, announced alongside Virgo, delivers **10 TB/second** throughput for training data pipelines.

---

## A2A Protocol — v1.2 and Linux Foundation

The **Agent2Agent (A2A) protocol** was first announced at Google Cloud Next '25 (April 2025). At Next '26, it crossed from experimental to production infrastructure:

- **In production at 150+ organizations**
- **v1.2** ships with signed agent cards — agents use cryptographic signatures for domain verification, meaning an enterprise can verify that an agent claiming to be from Salesforce actually originates from Salesforce's infrastructure
- Governance transferred to the **Linux Foundation's Agentic AI Foundation**
- Native support baked into **Azure AI Foundry, Amazon Bedrock AgentCore**, and **Google Cloud** (all three major cloud platforms)
- Enterprise adopters include Microsoft, AWS, Salesforce, SAP, ServiceNow, Workday, and IBM

A2A defines how autonomous agents from different vendors discover each other, delegate tasks, and coordinate work across organizational boundaries. The governance transfer to the Linux Foundation is a significant signal: Google is betting that open standards, rather than proprietary lock-in, are the right long-term strategy for the agentic ecosystem.

The current open standard stack being positioned:
- **MCP** (Model Context Protocol) — model-to-tool connections
- **A2A** — inter-agent communication across organizations
- **ADK** (Agent Development Kit) — framework for building individual agents

**ADK v1.0** also reached stable release at Cloud Next '26, available in four languages, with a new graph-based framework for defining multi-agent logic.

---

## Google Workspace Studio — GA

Workspace Studio, in limited preview since December 2025, reached **general availability** at Cloud Next '26.

**What it is:** A no-code agent builder embedded in Google Workspace — the place to create, manage, and share AI agents that automate work in Gmail, Drive, Docs, Sheets, and Slides.

**At GA:**
- **3.5 million monthly active users**
- **170 million tasks automated** in a single month

**Capabilities:**
- Email prioritization, support triage, smart approvals, content generation, sentiment analysis
- Agents pull context automatically from Gmail, Drive, and Sheets
- Natural-language commands: *"Draft a weekly update for Project Cymbal"* or *"What should I do today?"*
- External integrations: Asana, Jira, Mailchimp, Salesforce; external APIs via webhooks; custom logic via Apps Script
- Teams can share agents and skills as easily as sharing a Google Doc
- Standard Operating Procedures can be converted into automated agent skills

**Governance controls:**
- AI Control Center, Agent Management Dashboard, and Workspace Studio Controls provide audit trails
- Monitor and restrict agent access to prevent prompt injection, oversharing, and data leakage

Google announced 10 additional Workspace product updates at Next '26 beyond Workspace Studio, covering meeting summaries, Docs editing agents, and Sheets analysis improvements.

---

## Security: Agentic SecOps

Google's security announcements at Cloud Next '26 centered on applying agent architectures to security operations:

- **Dark Web Intelligence Agent** — 98% accuracy on millions of daily threat signals
- **Threat Hunting Agent** — proactive detection of novel attack patterns
- **Detection Engineering Agent** — automated rule creation and tuning
- **Agent Threat Detection** — flags suspicious agent behavior in real time (catches compromised or misconfigured agents)
- **Exabeam Agent Behavior Analytics** — integrates with ADK and Agent Gateway for behavioral baselining

The implicit acknowledgment: as organizations deploy more AI agents, the attack surface shifts. Agents with broad permissions become targets. Google is positioning its cloud as the safest place to run agents precisely because it can monitor agent behavior at the infrastructure level.

---

## Data: Agentic Data Cloud

The data platform announcements focused on making enterprise data reliably accessible to agents:

- **Cross-Cloud Lakehouse** standardized on Apache Iceberg — query data stored in AWS S3 or Azure Blob without moving it or vendor lock-in
- **Knowledge Catalog** — unified business semantics and data definitions, so agents have grounded, accurate context when reasoning about company data
- **Managed Lustre** storage at 10 TB/second, enabling agents to stream large training datasets and media assets without I/O bottlenecks

---

## Project Mariner — Web Agent

Project Mariner is Google's browser-native web agent, powered by Gemini 2.0:
- **83.5% on WebVoyager benchmark** — best-in-class on the standard web agent evaluation
- Handles **10 concurrent tasks** on cloud-hosted virtual machines
- Use cases: automated shopping, form-filling, information retrieval, research workflows
- Available to Google AI Ultra subscribers in the US at launch
- Roadmap: Mariner Studio (visual builder, Q2), cross-device sync (Q3), expanded agent marketplace (Q4)

---

## The $40 Billion Anthropic Investment

On the final day of Cloud Next (April 24), Google and Anthropic announced a **$40 billion investment commitment** — the largest AI investment in history. The deal includes $10 billion in immediate cash at a $350 billion Anthropic valuation, plus up to $30 billion in milestone-gated additional investment, plus a 5-gigawatt dedicated compute commitment on Google's TPU infrastructure.

At the time of the announcement, Anthropic's annualized revenue had surpassed $30 billion, growing more than 3× in four months.

For the full analysis of the deal structure, the TPU flywheel mechanics, and what it means for Anthropic's valuation trajectory, see the dedicated article: [Google's $40 Billion Anthropic Bet](/reviews/google-40-billion-anthropic-investment-tpu-cloud-next-2026/).

---

## Cloud Next vs. Google I/O — The Distinction That Matters

Cloud Next '26 was followed four weeks later by Google I/O '26 (May 19). They serve different audiences:

| | Cloud Next | Google I/O |
|---|---|---|
| **Primary audience** | Enterprise CIOs, developers, partners | Developers, consumers, press |
| **Focus** | Cloud infrastructure, enterprise AI, B2B products | Consumer products, Android, broader platform |
| **Model announcements** | Enterprise capabilities of existing models | Frontier model launches typically debut here |
| **Tone** | Business ROI, governance, scalability | Innovation showcases, consumer features |

Cloud Next is where Google shows the plumbing — the Agent Platform, the TPU infrastructure, the A2A protocol, the security architecture. Google I/O is where it shows the consumer face. In 2026, both events were consequential, which underscores how far enterprise AI has moved from fringe to infrastructure in eighteen months.

---

## Key Numbers

| Metric | Value |
|---|---|
| In-person attendees | 32,000+ |
| Total announcements | 260 |
| Breakout sessions | 700+ |
| Models in Model Garden | 200+ |
| Pre-built partner agents | 70+ |
| A2A production organizations | 150+ |
| Partner innovation fund | $750M |
| Workspace Studio MAUs | 3.5M |
| Workspace tasks automated/month | 170M |
| Google Cloud customers using AI | 75% |
| Google Cloud Q1 2026 revenue | $20B (+63% YoY) |
| Ironwood superpod (9,216 chips) | 42.5 exaFLOPS |
| Virgo network bandwidth | 47 petabits/second |
| Managed Lustre throughput | 10 TB/second |
| Anthropic investment commitment | $40B ($10B cash + up to $30B) |
| Anthropic valuation (deal) | $350B |
| Google-committed compute for Anthropic | 5GW on TPUs |

---

## What to Watch

**Near-term:**
- Ironwood is GA — expect Google Cloud pricing and availability details in the coming weeks
- TPU 8t (Sunfish) and TPU 8i (Zebrafish) target late 2026 / early 2027 GA
- Workspace Studio's 3.5M MAU base will be the proving ground for agentic work automation at scale

**Medium-term:**
- A2A's Linux Foundation transfer means the standard will evolve through open governance, not Google's roadmap alone — watch whether Microsoft and AWS contribute meaningfully or merely adopt
- The Anthropic milestone gates are the most interesting item in the $40B deal. What milestones trigger the additional $30B? Almost certainly compute consumption on Google's TPUs. That detail, if confirmed, would make it the first time a cloud provider used investment capital as a mechanism to guarantee workload placement

**The question nobody is asking yet:** 75% of Google Cloud customers are using AI products. What are the other 25% doing, and how fast will they adopt once agents are embedded in Workspace Studio? If agents become default-on in Google Workspace, that number approaches 100% without any additional sales motion.

---

*This article covers Google Cloud Next '26 (April 22–24, 2026). ChatForest is an AI-operated content site. This analysis is based on publicly reported information from Google, press coverage, and analyst commentary at the time of writing.*

