---
title: "Cohere Review: The Enterprise AI Company That Wrote the Transformer Paper and Chose Not to Race OpenAI"
date: 2026-05-09
description: "Aidan Gomez co-authored 'Attention Is All You Need' at 20, then built Cohere around a different bet: enterprises need private, sovereign AI deployments, not the most powerful model. Seven years later, Cohere has $240M ARR growing at 287%, a $20B valuation, a pending merger with Germany's Aleph Alpha, and a copyright lawsuit from 14 media companies. Here is the full picture."
tags: ["enterprise-ai", "llm", "rag", "retrieval", "sovereign-ai", "multilingual", "canada", "review"]
categories: ["reviews"]
rating: 4
author: "ChatForest"
---

In 2017, a 20-year-old undergraduate named Aidan Gomez was interning at Google Brain in Toronto. He worked on a team that was rethinking the foundational architecture for sequence modeling — the class of problem that included machine translation, question answering, and document summarization. The dominant approaches used recurrent neural networks, which processed sequences token by token and struggled to maintain context over long distances. The Google Brain team had a different idea.

The resulting paper, "Attention Is All You Need," introduced the transformer architecture. It was published in June 2017. The eight co-authors included Noam Shazeer, Ashish Vaswani, and six others — one of whom was Gomez, listed as a summer intern. The paper described a model that processed sequences in parallel, using attention mechanisms to directly relate every position to every other position in the input. The architecture turned out to be the foundational structure for GPT, BERT, LLaMA, Claude, Gemini, and essentially every major language model built since.

Gomez had contributed to the most influential architecture paper in modern AI history before completing his undergraduate degree.

Two years later, he co-founded Cohere.

The company he built is not trying to be the most powerful AI lab. It does not compete with OpenAI on frontier benchmark scores. It does not publish papers about superintelligence timelines. What it does instead is offer enterprises something that OpenAI, Anthropic, and Google structurally cannot: AI models that run entirely inside your own infrastructure, on your hardware, under your data governance rules, without your sensitive data leaving your network.

That positioning, combined with a purpose-built retrieval stack, is what Cohere has staked its business on. As of May 2026, the bet looks increasingly correct: $240 million in annual recurring revenue growing at 287% year-over-year, a pending merger that would make Cohere the largest sovereign AI vendor outside Silicon Valley, and a realistic IPO path at a $20 billion valuation.

---

## The Founding Team

**Aidan Gomez** (CEO) is British-Canadian, raised in both the UK and Canada. He completed his BSc in computer science and mathematics at the University of Toronto, where he worked closely with several faculty members in machine learning research. After his Google Brain summer, he began a PhD at the University of Oxford under researcher Phil Blunsom. He paused the doctorate to found Cohere in 2019, and Oxford awarded him the degree in 2024 — based on his published research record rather than a traditional thesis, the kind of recognition typically reserved for researchers whose published work speaks for itself.

The "Attention Is All You Need" co-authorship is not decorative. It is legitimately load-bearing credibility in the AI research community. Few enterprise AI company founders can say they helped build the architecture that every major model runs on. Gomez can.

**Nick Frosst** (co-founder) was also a researcher at Google Brain, also connected to the "Attention Is All You Need" lineage, and had done earlier work with Geoffrey Hinton at the University of Toronto. Frosst co-founded the company but has a lower public profile than Gomez; he leads research operations.

**Ivan Zhang** (co-founder, CTO) had previously worked with Gomez in the research group FOR.ai, which brought together early-career researchers to collaborate on papers and demos before they founded companies.

The Toronto origin matters. Canada's AI ecosystem — anchored by the University of Toronto, the Vector Institute, and decades of Hinton-era research — produced a cluster of technically serious founders who grew up in academic environments rather than startup culture. Cohere's engineering culture reflects this: methodical, research-grounded, and somewhat less interested in consumer splashiness than San Francisco counterparts.

---

## The Core Bet: Sovereignty Over Scale

To understand Cohere, you need to understand what enterprise procurement actually looks like for AI.

When a large bank, a government ministry, or a healthcare system wants to deploy a language model, they do not simply sign up for an API and start shipping. They face a cascade of requirements: data must not leave the jurisdiction, vendor access to sensitive data must be audited and controlled, the model must be certifiable for compliance frameworks like GDPR or SOC-2, and any failure has legal and reputational consequences. Many of these organizations have dedicated information security teams whose job it is to say no.

OpenAI's API sends data through Azure infrastructure. Anthropic's Claude API is primarily SaaS. Google's Vertex AI keeps data inside Google's cloud, but that cloud is still owned by Google. For regulated enterprises, the question is not "which model performs best on MMLU" but "where does my data go and who has theoretical access to it."

Cohere's answer is: the model lives on your machines, in your VPC, or in an air-gapped deployment. You run the inference. No data leaves. The API calls never hit Cohere's servers in production.

This is not technically extraordinary — it requires good containerization, solid MLOps documentation, and models optimized for real-world hardware constraints — but it is extremely difficult to do reliably at enterprise scale, and it is structurally difficult for hyperscalers to match. AWS cannot offer a product that competes with itself. Google Cloud cannot offer enterprise clients a model that bypasses Google Cloud. Cohere can offer models that run on the customer's own Oracle hardware, Azure VPC, or bare-metal servers in a classified facility.

The company calls this framing "sovereign AI." It is an increasingly resonant term: governments that want AI capability without ceding data to Silicon Valley companies, enterprises in industries where data residency is legally required, and defense organizations that simply cannot use public APIs.

---

## Funding History

Cohere has raised approximately $1.5 billion before the current transaction cycle:

- **Series A (September 2021):** $40 million, led by Index Ventures. Notable early investors included Geoffrey Hinton and Fei-Fei Li — two of the most credentialed AI researchers alive. Radical Ventures, Pieter Abbeel, and Raquel Urtasun also participated. The academic backing established research legitimacy from the start.
- **Series B (February 2022):** $125 million, led by Tiger Global Management.
- **Series C (June 2023):** $270 million at a $2.2 billion valuation. Inovia Capital led; Oracle, Salesforce Ventures, Nvidia, Mirae Asset, and Schroders joined. The participation of Oracle at this stage was strategic: it signaled enterprise channel distribution, not just financial backing.
- **Series D (June 2024):** $500 million. Led by Cisco and AMD, with Fujitsu, PSP Investments (Canadian pension fund), and Export Development Canada (a federal Crown corporation). The Canadian government capital is intentional positioning — Canada backing one of its AI champions.
- **Series D Extension — First Close (August 2025):** $500 million at a $6.8 billion valuation. Radical Ventures and Inovia Capital led. AMD, Nvidia, Salesforce Ventures, and PSP Investments all returned.
- **Series D Extension — Second Close (September 2025):** $100 million, bringing the valuation to $7 billion. The Business Development Bank of Canada participated, alongside Nexxus Capital Management.

Then, in April 2026, everything accelerated.

---

## The Aleph Alpha Deal

On April 24, 2026, Cohere announced a definitive agreement to acquire and merge with Aleph Alpha, Germany's leading sovereign AI company. The combined entity — retaining the Cohere name, with Gomez as CEO — is valued at approximately $20 billion.

The financing that accompanies the deal is the Series E: approximately $600 million (structured as roughly €500 million), led by Schwarz Group's digital subsidiary Schwarz Digits. Schwarz Group is the parent of Lidl and Kaufland, two of the largest supermarket chains in Europe. It is also one of the largest private companies in the world by revenue. Schwarz Digits operates STACKIT, a European sovereign cloud platform. Cohere becomes STACKIT's anchor AI tenant.

Cohere will hold approximately 90% of the combined entity. Aleph Alpha's shareholders — including SAP, the Schwarz Group, and German public-sector investors — receive consideration that has not been fully disclosed.

Why Aleph Alpha? The company had positioned itself as Europe's answer to OpenAI: German-founded, government-backed, designed for EU data sovereignty requirements. Its customers include the Baden-Württemberg regional government, federal German ministries, and other regulated European institutions that required domestic AI. The problem was that Aleph Alpha had struggled to scale revenue against much better-capitalized US competitors.

For Cohere, the deal provides immediate access to European government customers and regulatory relationships that would have taken years to build organically. For Aleph Alpha's customers, the deal provides continuity of their sovereign deployment model backed by a company with deeper capital and a stronger technical roadmap. For Schwarz Group, it provides an anchor relationship with the dominant transatlantic sovereign AI vendor.

The deal is subject to Aleph Alpha shareholder approval and regulatory clearance from the German government. Both are expected, though the German government has a stated interest in the outcome — Aleph Alpha is in part a national AI strategy asset, and its transfer to a Canadian company will be reviewed carefully. The EU regulatory dimension (potential review under EU foreign investment screening) adds procedural complexity.

If it closes as structured, Cohere becomes the largest sovereign AI vendor outside Silicon Valley by revenue, valuation, and customer footprint.

---

## Revenue Growth

Cohere's growth trajectory is the most striking number in its story.

In late 2023, the company's annualized recurring revenue was approximately $13 million. By year-end 2024, ARR had grown to around $62 million. By year-end 2025, per an investor memo reviewed by CNBC, ARR had reached $240 million — surpassing an internal target of $200 million.

That is roughly 287% year-over-year growth from 2024 to 2025. Gross margins are approximately 70%, expanding over the prior year. The company has not disclosed net income or EBITDA; it is not publicly confirmed as profitable at the operating level.

The growth rate warrants context. From a $13 million baseline in late 2023 to $240 million by late 2025 is extraordinary for an enterprise AI company selling to regulated industries with long sales cycles. It also came after a meaningful miss: The Information reported that Cohere's 2023 revenue came in approximately $350 million short of what the company had projected to investors during its 2023 funding round. That miss created credibility concerns and contributed to a difficult period in 2024.

The recovery suggests the core enterprise AI market took longer to materialize than Cohere projected — then materialized faster than expected. This is consistent with patterns seen across enterprise software: the hockey-stick inflection often arrives 12-18 months later than the original forecast.

Co-founder Nick Frosst was notably candid in 2025 about "AI proof-of-concept fatigue" — the phenomenon where enterprises run dozens of pilots but struggle to move them into production. The implication was that Cohere had experienced this directly, and the 2025 acceleration reflected those POCs finally converting to production deployments.

---

## The Product Stack

Cohere's products form an integrated retrieval stack rather than a general-purpose model API. Understanding the architecture helps explain why enterprise buyers choose it.

### Command Family (Generation)

**Command R** (35B parameters, 128K context window): The workhorse model, optimized for RAG pipelines. Command R's defining characteristic is that it was trained specifically to work well with retrieved documents — to synthesize multiple sources, attribute statements to specific passages, and avoid hallucinating when grounded context is provided.

**Command R+** (128K context window): A larger, more capable version of Command R, designed for complex multi-step tasks and agentic workflows. Cohere's flagship model from mid-2024 through early 2025.

**Command A** (launched March 2025): Cohere's current flagship. 111 billion parameters. 256K token context window — double Command R+. Maximum output of 8,000 tokens. The specification that most interests enterprise infrastructure teams: Command A can be served from **two A100 or H100 GPUs**. At 111B parameters, that is exceptional compute efficiency.

The GPU economics matter enormously for on-premise deployments. A customer running models in their own data center pays for hardware acquisition, electricity, and operations. A model that requires four GPUs costs roughly twice as much to run as one that requires two, at a given scale. Command A's efficiency advantage translates directly to operational cost for the customer.

Command A benchmarks at 86.6% on MMLU. Cohere positions it as on par with GPT-4o and DeepSeek-V3 on enterprise agentic tasks. The model has a reasoning variant — Command A Reasoning — for complex multi-step workflows. It supports 23 languages with full agent capability.

Command A is also available as open weights on HuggingFace (`c4ai-command-a-03-2025`), which is unusual for a commercial frontier-tier model. The open-weights release serves developer ecosystem and research credibility purposes without significantly cannibalizing enterprise revenue, since enterprise customers pay for support, deployment tooling, and SLA guarantees rather than just the model weights.

### Embed (Retrieval)

**Embed v3** and **Embed v4**: Text and multimodal embedding models used to convert enterprise documents into vector representations for semantic search. Embed v4 (2025) supports interleaved text and image inputs — you can embed a PDF page that contains both text and diagrams, and the embedding captures the visual content alongside the text.

Configuration options include output dimensions from 256 to 1536 and multiple quantization formats (float, int8, binary), which allows enterprises to tune the size/accuracy tradeoff for their vector databases. Embed handles 100+ languages. It is available on AWS SageMaker, Azure AI Foundry, and Google Cloud Vertex AI, in addition to Cohere's own API.

### Rerank (Post-Retrieval Refinement)

**Rerank 3** and **Rerank 4** (December 2025): The reranker is the middle layer in Cohere's RAG architecture. After Embed retrieves candidate documents from a vector database, Rerank scores them for relevance before they are passed to Command for generation. This two-stage retrieval — broad semantic search followed by precise relevance scoring — produces significantly better results than embedding search alone.

Rerank 4 (December 2025) is multilingual across 100+ languages and is Cohere's first reranking model with a self-learning capability. It comes in two variants: Rerank 4 Pro (maximum accuracy) and Rerank 4 Fast (lower latency). The model auto-chunks documents longer than 510 tokens, removing a preprocessing burden from developers.

### Aya (Open-Weights Multilingual Research)

**Aya** is Cohere's open-weights multilingual model line, developed and published by Cohere Labs (the company's non-profit research arm). The Aya initiative covers 101 languages, including dozens that were not served by any major language model before the project began.

**Aya Expanse** is the current instruction-tuned multilingual model, covering 101 languages with cross-lingual transfer techniques that improve low-resource language performance by learning patterns from higher-resource languages.

**Aya Vision** (December 2025) is Cohere's first open-weight multimodal model — it processes both text and images, across 23 languages. This matters for enterprises and governments working with documents that mix text and visual content in non-English languages: legal documents with tables and diagrams, government forms, technical manuals.

**Tiny Aya** (February 2026) is a 3.35B parameter model family designed to run on consumer laptops without internet connectivity. Available in four regional variants:
- **TinyAya-Global**: Broad language coverage
- **TinyAya-Earth**: African languages
- **TinyAya-Fire**: South Asian languages
- **TinyAya-Water**: Asia-Pacific and European languages

The laptop-deployable model opens use cases where even a private cloud deployment is too complex or too connected — field workers without reliable internet, development contexts in bandwidth-constrained regions, or privacy requirements so strict that even a private API cannot satisfy them.

### North (Enterprise Agent Platform)

**North** launched into general availability in August 2025. It is Cohere's enterprise product layer: a low-code/no-code platform for building and deploying AI agents within enterprise environments.

North brings together Command, Embed, and Rerank with a visual interface for building agent workflows, tool integrations, access controls, and deployment management. It supports on-premise, private VPC, hybrid cloud, and air-gapped deployments — the same deployment flexibility as the underlying models.

Security features include granular access controls, agent autonomy policies (limiting what actions an agent can take without human approval), continuous red-teaming built into the platform, and third-party security audits. Certifications include GDPR, SOC-2, and ISO 27001.

North Agent Studio allows custom tool integration, including MCP server connections for interoperability with other agent systems. Cohere maintains a Python SDK specifically for MCP-compatible tools within North (`cohere-ai/north-mcp-python-sdk`). Rather than releasing a standalone MCP server, Cohere has built MCP connectivity into North itself, positioning the platform as an enterprise agent orchestrator.

North has vertical-specific offerings co-developed with anchor customers:
- **North for Banking**: Built with RBC (Royal Bank of Canada). Cohere's flagship financial services deployment.
- **North for Telecom**: Built with STC (Saudi Telecom). Agentic operations for telecommunications workflows.

Other early North customers include Dell, LG CNS (South Korean IT services arm of LG), Ensemble Health Partners (healthcare revenue cycle management), and Bell (BCE, the Canadian telecom).

---

## The RAG Stack as a Philosophy

It is worth pausing on what Cohere has actually built, because the product architecture reflects a deliberate strategic view about where enterprise AI value lives.

The canonical critique of early enterprise AI deployments was hallucination: language models confidently stated false things, undermining trust. The canonical solution was retrieval-augmented generation — retrieve relevant documents from the company's own knowledge base, then generate answers grounded in those documents, with citations. RAG became the default pattern for enterprise AI applications.

Most API providers treated RAG as a pattern for customers to implement themselves: you build the embedding pipeline, you choose a vector database, you wire it to the generation endpoint. The components often came from different vendors, using different APIs, with different performance characteristics.

Cohere built Embed, Rerank, and Command as a unified stack designed to work together. The three components were trained with knowledge of each other's outputs. Rerank 4 was evaluated specifically against the kinds of queries Command A would receive after Embed retrieved candidates. The integration is not just documented compatibility — it is architectural co-design.

This is a legitimate moat. It does not mean competitors cannot build better individual components. It does mean that the experience of deploying Cohere's full stack is more coherent than assembling equivalent capabilities from multiple vendors.

---

## Enterprise Customer Base

Cohere's customer list reflects the vertical focus on regulated industries:

**Financial services**: Royal Bank of Canada (co-developed North for Banking), McKinsey (internal knowledge retrieval and consulting workflow automation). The financial services vertical is Cohere's strongest in terms of public referenceable customers.

**Telecommunications**: STC (Saudi Telecom, co-developed North for Telecom), Bell (BCE, Canadian telecom). Telecom companies have large internal knowledge bases, complex customer-facing workflows, and multilingual requirements that align with Cohere's stack.

**Healthcare**: Ensemble Health Partners, which uses North for agentic revenue cycle management — the complex administrative workflow of billing, claims, and reimbursement that costs healthcare systems billions annually.

**Defense**: Saab has signed an MOU for AI technologies in the GlobalEye airborne surveillance program. This is smaller in scale than Scale AI's DoD relationships, but signals that Cohere's sovereign deployment capability extends to defense contractors with classified data requirements.

**Technology and enterprise**: Dell, LG CNS, Oracle (strategic investor and OCI integration partner). Oracle's investment and partnership provides Cohere access to Oracle's enterprise customer base through OCI Generative AI.

**European government** (via Aleph Alpha, pending): Baden-Württemberg regional government, German federal ministries, and other EU public sector organizations. These become Cohere customers upon deal close.

The multi-cloud availability — Cohere models accessible on AWS Bedrock, Azure AI Foundry, Google Cloud Vertex AI, and Oracle OCI — is a sales enabler. Enterprise buyers who have already committed to a hyperscaler can add Cohere models without switching infrastructure.

---

## Competition

Cohere occupies a specific niche in an increasingly crowded market.

At the frontier capability tier — the race for the largest, most capable models — Cohere has explicitly opted out. Gomez said publicly in 2025 that spending incremental $10 billion per year on scaling no longer delivers sufficient ROI. This is partly genuine conviction (Cohere's researchers have published on the limits of scaling), partly commercial necessity (Cohere cannot match hyperscaler compute budgets), and partly a positioning choice (being the company that competes on deployment rather than benchmarks).

The direct competitive landscape:

**Anthropic** is the closest overlap in the enterprise API space. Both companies target regulated enterprise deployments, both have strong safety and reliability narratives, and both are serious technical organizations. Anthropic has the brand recognition of Claude and the Amazon investment. Cohere has stronger private deployment flexibility and multilingual. As enterprise AI procurement matures, these two companies are increasingly direct competitors.

**OpenAI** dominates general-purpose LLM adoption and developer mindshare. OpenAI is not primarily a sovereign deployment vendor; its enterprise product routes through Microsoft Azure. In regulated industries where data residency is a hard requirement, OpenAI is often disqualified before the evaluation begins. This is the market segment Cohere is hunting.

**Mistral** (French) is the European open-weights competitor. Mistral has built significant credibility with the open-source developer community and has its own European regulatory positioning. The Aleph Alpha deal directly challenges Mistral's European enterprise relevance — Cohere now has deeper government relationships and capital backing on the continent.

**AI21 Labs** (Israeli) competes in enterprise NLP with the Jamba model family. AI21 is better capitalized than some competitors but less visible than Cohere; both are mid-tier enterprise API players.

**Aleph Alpha** (now being acquired): No longer a competitor by definition.

The structural advantage Cohere has pursued — deployment flexibility that hyperscalers cannot match — is real and durable. The question is whether the sovereign AI market is large enough, fast enough, to support a $20 billion valuation.

---

## MCP and the Agent Ecosystem

Cohere does not publish a standalone first-party MCP server in the standard model of many AI tool vendors. Instead, North Agent Studio supports MCP server integration as a connection mechanism within the platform. The `cohere-ai/north-mcp-python-sdk` GitHub repository provides the tooling for building MCP-compatible tool integrations that work with North.

The strategic logic: Cohere wants to be the agent orchestrator inside enterprise environments, not a tool that another orchestrator calls. MCP connectivity flows inward (into North) rather than outward (exposing Cohere's API to external MCP clients). Third-party integrations via Unified.to and Zapier exist for customers who need to connect Cohere's API to external agent frameworks.

Command A's tool use capability is meaningfully stronger than prior Command models. The model can autonomously chain tool calls across complex multi-step tasks, generate citations grounded in retrieved documents, and operate in agentic workflows without continuous human oversight. This is the capability North is built on top of.

---

## Controversies

No company with Cohere's profile moves through 2025 and 2026 without accumulating some problems. Two are worth examining directly.

**Copyright litigation (February 2025):** Fourteen major media publishers — including Condé Nast, The Atlantic, Forbes, The Guardian, Business Insider, the Los Angeles Times, Vox Media, the Toronto Star, and Politico — filed suit against Cohere in the Southern District of New York. The lawsuit alleges that Cohere trained its models on copyrighted works scraped without authorization, including material behind paywalls and pages explicitly blocked by robots.txt. It also alleges that Cohere's RAG feature reproduced substantial verbatim excerpts of publisher articles in responses to user queries.

This is not a frivolous case. Judge Colleen McMahon rejected Cohere's motion to dismiss in full, holding that "substitutive summaries" — responses that reproduce enough of a work to reduce the incentive to read the original — may plausibly constitute copyright infringement. Statutory damages if Cohere loses on all 4,000+ alleged works: potentially hundreds of millions of dollars.

The litigation is precedent-setting for the entire RAG-based AI industry. If verbatim retrieval and reproduction constitutes infringement even when the generation is ostensibly answering a question, the legal framework around enterprise RAG deployments becomes significantly more complicated. Cohere called the suit "misguided and frivolous." The court disagreed with that characterization at the motion-to-dismiss stage.

**Revenue miss vs. 2023 projections:** The Information reported that Cohere's 2023 revenue fell approximately $350 million below what the company had projected to investors during its Series C fundraising round. This was not publicly confirmed by Cohere. The miss damaged investor credibility, contributed to a period of elevated churn concern, and raised questions about whether the enterprise AI market was developing as fast as the fundraising narrative suggested.

The 2025 recovery — from ~$62 million ARR to $240 million — substantially rehabilitates that narrative. But the miss is part of the honest history: Cohere projected faster enterprise AI adoption than materialized, then had to outgrow the credibility gap.

---

## The Aidan Gomez Factor

Founders matter in enterprise AI in a specific way: technical credibility shortcuts sales cycles. When a CISO or CTO is evaluating two AI vendors, knowing that one was co-founded by a named author on "Attention Is All You Need" is not irrelevant. It signals that the company has deep understanding of what it is building, not just commercial packaging on top of licensed technology.

Gomez is an unusually effective public communicator for a technically credentialed founder. He appears at Davos, NeurIPS, and Web Summit. His CNBC interviews are measured and specific. His public position on the AI landscape — that the scaling race is yielding diminishing returns for enterprise applications, that sovereign deployment will matter more than benchmark superiority, that multilingual AI is dramatically underserved — is coherent and defensible regardless of self-interest.

The PhD story is a small thing, but it is symbolically meaningful: Gomez paused an Oxford doctorate to build a company, published enough research to earn the degree in 2024 based on accumulated work, and received it. He did not abandon academic credibility to become a startup CEO. He carried both.

---

## IPO Outlook

Gomez said in late 2025 that a public market debut was coming "soon." The CNBC report from February 2026 on the $240 million ARR milestone was framed explicitly in IPO terms. No S-1 has been filed as of May 2026.

The Aleph Alpha acquisition is the near-term complexity: integrating a German AI company, closing the Schwarz Group financing, and navigating regulatory review takes 6-12 months. The combined entity at $20 billion valuation and an expanded ARR base is a more compelling IPO asset than Cohere standalone at $7 billion.

The realistic window is likely 2027, pending deal close and integration. At $240 million ARR growing at 287% annually, Cohere's trajectory would put it at $700 million to $1 billion ARR by mid-2027 under optimistic assumptions — a size range where IPO comps become favorable.

Canadian government backing adds a sovereignty dimension to exit scenarios: any acquisition would face Investment Canada Act review, and the political optics of selling a Canadian AI champion to a US or Chinese buyer would be fraught. An IPO is a cleaner outcome for all parties.

---

## Assessment

Cohere has built a genuinely differentiated enterprise AI company. The sovereign deployment positioning is real, defensible, and increasingly in demand as enterprises and governments grapple with AI governance. The retrieval stack — Embed, Rerank, Command as an integrated system — is more coherent than assembling equivalent capabilities from separate vendors. The Aleph Alpha deal, if it closes as structured, creates a transatlantic sovereign AI vendor with no direct equivalent.

The challenges are real too. The copyright litigation from 14 publishers is not a nuisance case; the motion-to-dismiss ruling went against Cohere, and the statutory damage exposure is material. Revenue is growing fast but from a smaller base than competitors; at $240 million ARR, Cohere is substantially behind Anthropic (estimated $3-4 billion ARR in 2025) and a long way behind OpenAI. The Aleph Alpha integration is complex and introduces German regulatory and political sensitivities.

The bet Cohere made in 2019 — that enterprises need sovereign AI more than frontier benchmark superiority — is playing out as correct. The question is whether the company can build the customer base, revenue scale, and technical roadmap to become the default choice for that market before better-capitalized competitors develop comparable deployment flexibility.

As of May 2026, the trajectory says yes. The execution has been uneven, but the direction is right.

**Rating: 4/5.** Strongest enterprise RAG stack in the market, unique sovereign deployment capability that hyperscalers cannot replicate, exceptional revenue growth trajectory. Deductions for ongoing copyright litigation with material exposure, revenue base still modest relative to market valuation, Aleph Alpha integration risk, and a model capability tier that deliberately sits below frontier labs — which limits appeal for use cases where raw capability matters most.

---

*ChatForest reviews AI tools and infrastructure for builders. We research based on public information; we do not test products hands-on. This review reflects information available as of May 2026.*
