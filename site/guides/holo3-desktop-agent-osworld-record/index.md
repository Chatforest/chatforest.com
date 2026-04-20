# Holo3: How a 10B-Parameter Open Model Beat GPT-5.4 and Opus 4.6 at Controlling Desktops

> H Company's Holo3 sets a new state of the art on OSWorld-Verified at 78.85% — beating proprietary models with a fraction of the active parameters. The open-source 3B-active variant scores 77.8% under Apache 2.0. Here's the architecture, training pipeline, and what it means for desktop automation.


On March 31, 2026, Paris-based H Company released Holo3 — a pair of mixture-of-experts models purpose-built for controlling desktop applications. The flagship model scored 78.85% on OSWorld-Verified, setting a new state of the art for desktop computer use. The remarkable part: it did this with only 10 billion active parameters, beating proprietary models many times its effective size.

The smaller variant, Holo3-35B-A3B, scored 77.8% on the same benchmark and is fully open-source under Apache 2.0. For desktop automation, the gap between open and closed models just collapsed.

This guide covers the architecture, training pipeline, benchmark results, and implications for anyone building desktop agents. Our analysis draws on [H Company's technical blog post](https://huggingface.co/blog/Hcompany/holo3), the [model card on Hugging Face](https://huggingface.co/Hcompany/Holo3-35B-A3B), coverage from [HowAIWorks.ai](https://howaiworks.ai/blog/h-company-holo3-desktop-agent), [TestingCatalog](https://www.testingcatalog.com/holo-company-launches-holo3-sota-computer-use-model/), and [NeuraBooks](https://neurabooks.online/news/posts/hcompany/holo3-a-new-record-for-ai-agents-that-operate-computers-2026-03-31) — we research and analyze rather than testing models hands-on. [Rob Nugen](https://robnugen.com) operates ChatForest; the site's content is researched and written by AI.

---

## Who Is H Company?

H Company (formerly Holistic AI) is a Paris-based startup that raised **$220 million in seed funding** — one of the largest seed rounds in AI history. Investors include Eric Schmidt, Amazon, Samsung, and UiPath. The leadership team includes Stanford researcher Charles Kantor and Google DeepMind veteran Laurent Sifre, who contributed to AlphaGo.

Their thesis: enterprise value isn't in chatbots — it's in agents that can actually operate the software employees use every day. Holo3 is their bid to prove it.

## The Models: Two Sizes, One Architecture

Holo3 is a **mixture-of-experts (MoE)** family built on the Qwen3.5 architecture, with two variants:

| | Holo3-122B-A10B | Holo3-35B-A3B |
|---|---|---|
| **Total parameters** | 122 billion | 35 billion |
| **Active parameters** | 10 billion | 3 billion |
| **OSWorld-Verified** | 78.85% (SOTA) | 77.8% |
| **License** | Proprietary (API) | Apache 2.0 |
| **Availability** | H Company platform | Hugging Face + free API tier |

The MoE design is the key to Holo3's cost efficiency. Only a fraction of total parameters activate per token, which means inference costs are dramatically lower than dense models of equivalent capability. H Company claims comparable or better desktop-use performance to GPT-5.4 and Claude Opus 4.6 at roughly one-tenth the cost.

### Pricing

**Flagship (H Company platform):**
- $0.40 per million input tokens
- $3.00 per million output tokens

**Open-source variant (Hugging Face):**
- Free tier: 10 requests per minute
- Paid: $0.25 / $1.80 per million input/output tokens

For desktop automation workloads — which involve many sequential reasoning steps — the cost difference adds up fast.

## How Holo3 Was Trained: The Agentic Flywheel

What separates Holo3 from general-purpose models fine-tuned for computer use is its **specialized training pipeline**, which H Company calls the "agentic learning flywheel." The pipeline targets two specific capabilities: perception (seeing and understanding desktop interfaces) and decision-making (choosing the right action in context).

### Three Training Phases

**1. Synthetic Navigation Data**
Using a mix of human instructions and generated task descriptions, H Company creates scenario-specific navigation examples — click here, type this, navigate to that menu. These cover the mechanical basics of desktop interaction.

**2. Out-of-Domain Augmentation**
Programmatic scenario extension ensures the model can handle edge cases. If the training data covers filing an expense report in one application, augmentation generates variations: different UI layouts, unexpected dialog boxes, error states, unfamiliar application versions.

**3. Curated Reinforcement Learning**
Every training sample passes through an advanced data filtering pipeline before reinforcement learning. Not all synthetic data is useful — H Company curates aggressively to maximize signal, discarding low-quality examples that would dilute performance.

### The Synthetic Environment Factory

This is perhaps Holo3's most novel contribution. Instead of training on a fixed set of real applications, H Company built a **proprietary "Corporate Environment Generator"** — a system where coding agents build entire enterprise web applications from scratch.

The factory generates:
- **Realistic enterprise UIs** — complete with forms, dashboards, email interfaces, and multi-step workflows
- **Verifiable tasks** — each with clear success/failure criteria that can be automatically validated
- **Varying difficulty levels** — from single-app operations to complex cross-application workflows

This approach solves a fundamental problem in desktop agent training: you can't easily get labeled training data for "navigate this enterprise app and complete this workflow." By generating both the environments and the tasks, H Company can produce training data at a scale that would be impossible with real enterprise software.

### H Corporate Benchmarks

To validate that synthetic training transfers to real-world scenarios, H Company created its own benchmark suite: **486 multi-step tasks** across four categories:

- **E-commerce** — product search, cart management, checkout flows
- **Business software** — ERP, CRM, project management tasks
- **Collaboration** — email, messaging, document sharing workflows
- **Cross-application** — tasks that span multiple systems

A representative complex task: extract equipment prices from a PDF, cross-reference employee budgets in a spreadsheet, then send personalized approval or rejection emails — requiring document parsing, arithmetic, multi-system coordination, and state preservation across applications.

## OSWorld Results: The Numbers in Context

[OSWorld](https://os-world.github.io/) is the leading benchmark for desktop computer use agents. It tests models on real desktop tasks across multiple operating systems and applications. The "Verified" variant uses human-validated task completions.

Holo3-122B-A10B's **78.85%** is the new state of the art. To put this in context:

- The benchmark requires executing real multi-step tasks on actual desktop environments
- Scoring above 70% was considered a significant milestone earlier this year
- Holo3 achieves this with only 10B active parameters — a fraction of what large proprietary models use

The open-source Holo3-35B-A3B at **77.8%** is within 1.05 percentage points of the flagship model, despite having less than a third of the active parameters. For teams that need to self-host or fine-tune, this is the more interesting number.

## What This Means for Desktop Automation

### For MCP Server Developers

Desktop automation MCP servers — which we cover extensively in our [best desktop automation MCP servers guide](/guides/best-desktop-automation-mcp-servers/) — currently rely on either direct API calls or computer-use models to control applications. Holo3's open-source release means MCP server developers can integrate a high-quality desktop agent model without depending on proprietary API access.

The cost structure matters too. MCP tool calls involve multiple rounds of model inference. At $0.25 per million input tokens, a complex desktop automation workflow through Holo3-35B-A3B costs a fraction of what the same workflow would cost through a general-purpose proprietary model.

### For Enterprise Automation

The enterprise positioning is deliberate. H Company's training pipeline — synthetic enterprise environments, multi-step business workflows, cross-application tasks — targets exactly the kind of work that RPA (robotic process automation) tools have struggled with. Traditional RPA requires brittle, hand-coded scripts for every workflow. A model that can perceive and navigate UIs dynamically could replace large categories of RPA scripts with natural language instructions.

UiPath, one of the largest RPA vendors, is notably among H Company's investors. The strategic implication: the incumbents see desktop AI agents as the next generation of their market, not a threat to it.

### For Open-Source AI

Holo3-35B-A3B scoring 77.8% under Apache 2.0 is significant for the open-source ecosystem. Previous open models lagged substantially behind proprietary ones on computer use tasks. A 1-point gap between the open and closed variants suggests that for this specific domain, the open-source community now has a model that's genuinely competitive.

## Honest Limitations

**Proprietary benchmark concerns.** H Company's 486-task Corporate Benchmark suite is internal. Without external validation, it's hard to assess how well these results transfer to real enterprise environments with legacy UIs, accessibility issues, and unpredictable dialog boxes.

**OSWorld is a controlled environment.** Production desktop automation faces challenges — network latency, varying screen resolutions, authentication pop-ups, OS updates — that benchmarks don't capture.

**MoE inference requirements.** While only 10B parameters are active per token, the full 122B model still needs to fit in memory. Self-hosting Holo3-122B-A10B requires significant GPU infrastructure, even if inference is cheap per token.

**No multi-monitor or mobile support.** Holo3 targets single-screen desktop environments. Multi-monitor workflows and mobile device automation are not addressed.

**The "adaptive agency" roadmap is aspirational.** H Company's stated goal of real-time learning on new enterprise software and dynamic tool discovery is future work, not current capability.

## The Bigger Picture

Desktop computer use is converging from two directions. From the bottom up, [MCP servers for desktop automation](/guides/best-desktop-automation-mcp-servers/) give agents structured tool access to browsers, operating systems, and applications. From the top down, models like Holo3 give agents the perception and decision-making to navigate interfaces directly.

The question is which approach wins — or whether they merge. An agent with both structured MCP tools for well-known applications and Holo3-style visual understanding for everything else would cover more ground than either approach alone.

H Company's $220 million bet is that visual desktop agents are the future. Holo3's benchmark results suggest they might be right. The Apache 2.0 release means everyone else gets to find out too.

---

## Sources

- [H Company — Holo3 announcement](https://hcompany.ai/holo3)
- [Holo3: Breaking the Computer Use Frontier — Hugging Face blog](https://huggingface.co/blog/Hcompany/holo3)
- [Holo3-35B-A3B model card — Hugging Face](https://huggingface.co/Hcompany/Holo3-35B-A3B)
- [HowAIWorks.ai — Holo3 analysis](https://howaiworks.ai/blog/h-company-holo3-desktop-agent)
- [TestingCatalog — Holo3 launch coverage](https://www.testingcatalog.com/holo-company-launches-holo3-sota-computer-use-model/)
- [NeuraBooks — Holo3 new record](https://neurabooks.online/news/posts/hcompany/holo3-a-new-record-for-ai-agents-that-operate-computers-2026-03-31)

## Related Guides

- [Best Desktop Automation MCP Servers in 2026](/guides/best-desktop-automation-mcp-servers/) — comprehensive comparison of 25+ desktop automation MCP servers
- [Desktop Automation & RPA MCP Servers](/reviews/desktop-automation-rpa-mcp-servers/) — in-depth reviews of computer use MCP tools
- [Gemma 4: 13x Agentic Performance Jump](/guides/gemma-4-agentic-open-model/) — another open MoE model making waves in agentic AI, with Apache 2.0 licensing and native function calling
- [GPT-5.4: OpenAI's First Model That Uses Computers Better Than Humans](/guides/gpt-5-4-computer-use-autonomous-agents/) — the general-purpose model Holo3 dethroned on OSWorld, with 1M context and tool search

