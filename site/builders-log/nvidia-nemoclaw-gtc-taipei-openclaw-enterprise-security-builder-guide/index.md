# Jensen Huang Called OpenClaw the New Linux. NemoClaw Is How You Deploy It Safely.

> At GTC Taipei, NVIDIA answered the enterprise OpenClaw security problem with NemoClaw — an open-source stack that sandboxes each agent, routes sensitive data locally, and lets IT write policy in YAML. Here is what it is, how it works, and what builders need to do now.


At GTC Taipei on June 1, [Jensen Huang called OpenClaw "the new Linux"](https://www.fierce-network.com/broadband/nvidia-gtc-openclaw-new-linux-and-every-company-needs-strategy-says-jensen-huang) and said [every company needs a strategy for it](https://www.barchart.com/story/news/867145/openclaw-is-just-as-important-as-html-linux-and-chatgpt-jensen-huang-bets-that-agentic-ai-will-transform-nvda-stock). Three days earlier, [we documented](https://chatforest.com/builders-log/openclaw-454-cve-clawhub-malicious-skills-builder-security-guide/) that OpenClaw has 454 documented CVEs, a marketplace poisoned with 1,184 malicious skills, and a Gartner enterprise block advisory.

Both things are true simultaneously, and the tension between them is exactly where NVIDIA is positioning NemoClaw.

---

## What OpenClaw Actually Is

Before getting to NemoClaw, it is worth being precise about what OpenClaw is, because the marketing around it tends to collapse its defining architectural difference.

OpenClaw is not a prompt-triggered task runner. Most AI agents today work like this: user sends prompt → agent completes task → done. OpenClaw's model is different. A "claw" is a persistent background process that runs continuously, operating on a heartbeat: at regular intervals, it checks its task queue, evaluates what requires action, acts or waits, and surfaces only what requires a human decision.

The difference matters for builders. A heartbeat agent can:

- Monitor a feed and act on items matching criteria, without being manually triggered
- Maintain state across days or weeks of a multi-step project
- Coordinate with other claws running in parallel on the same or different machines
- Recover from interruption and resume exactly where it left off

This is meaningfully closer to how an employee works than how a chatbot works. It is also why OpenClaw crossed [250,000 GitHub stars](https://www.star-history.com/blog/openclaw-surpasses-react-most-starred-software/), [overtaking React's roughly 243,000 stars to become the most-starred software project on GitHub](https://www.getpanto.ai/blog/openclaw-ai-platform-statistics). Jensen Huang's "new Linux" framing is hyperbole, but it captures something real: this is infrastructure-level software, not an application.

---

## The Problem NVIDIA Is Solving

The 454 CVEs and 1,184 malicious ClawHub packages we documented are a real problem, but they are not the only enterprise concern. Even a perfectly patched OpenClaw installation raises governance questions that enterprise IT cannot currently answer:

- **Data access**: Which files can this agent read? Which directories can it write to?
- **Network access**: Can it make outbound calls? To which endpoints?
- **Cloud exposure**: If it routes a query to GPT-4 or Claude, does any private data leave the building?
- **Audit trail**: What did this agent do, when, and why?
- **Policy enforcement**: Who defines the rules, and how are they applied consistently across hundreds of agents?

OpenClaw has no built-in answers to these questions. NemoClaw is [NVIDIA's attempt to provide them](https://techcrunch.com/2026/03/16/nvidias-version-of-openclaw-could-solve-its-biggest-problem-security/).

---

## NemoClaw: Architecture

NemoClaw is [NVIDIA's open-source reference stack](https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Announces-NemoClaw-for-the-OpenClaw-Community/default.aspx) — also published as [an open blueprint on GitHub](https://github.com/NVIDIA/NemoClaw) — that layers three components on top of a base OpenClaw installation:

### 1. NVIDIA OpenShell

[OpenShell is the open-source runtime at NemoClaw's core](https://blogs.nvidia.com/blog/industrial-software-leaders-secure-autonomous-ai-engineers-nemoclaw/) — it "governs how each agent accesses files, networks and tools, enforcing policy-based security at every layer," wrapping each claw in an isolated sandbox conceptually similar to a Docker container but purpose-built for agentic workloads. Each sandbox has a YAML policy file that, conceptually, defines:

```yaml
# Example NemoClaw agent policy
filesystem:
  read: ["/home/user/projects/current", "/tmp/agent-workspace"]
  write: ["/tmp/agent-workspace"]
  deny: ["/home/user/.ssh", "/etc", "/home/user/.config"]

network:
  allow_outbound: ["api.github.com", "api.linear.app"]
  deny_outbound: ["*"]  # default-deny for anything not listed

cloud_services:
  allow: ["claude-3-7", "gpt-4-1"]
  route_sensitive_data: false  # blocks private data from leaving the sandbox
```

These are administrator-defined, version-controlled, and applied at the runtime level — the agent cannot override them. This is a meaningful shift from OpenClaw's current default behavior, where agents inherit the full permissions of the user account running them.

### 2. NVIDIA Nemotron Models

NemoClaw ships with [Nemotron, NVIDIA's family of open-weight models](https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Announces-NemoClaw-for-the-OpenClaw-Community/default.aspx), configured to run locally by default. The practical purpose is sensitive data isolation: tasks that involve private data — internal documents, customer records, proprietary code — run on the local model. Nothing leaves the hardware.

Nemotron variants are built for long-context, long-running agentic workloads — [NVIDIA's technical report for Nemotron 3 Nano lists a native context window up to 1 million tokens](https://research.nvidia.com/labs/nemotron/files/NVIDIA-Nemotron-3-Nano-Technical-Report.pdf), though NemoClaw's own documentation does not publish one fixed context figure for the stack — actual usable budget depends on which Nemotron variant and local GPU you deploy.

### 3. Privacy Router

NVIDIA's own announcement [lists a "privacy router for cloud model access" as one of NemoClaw's components](https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Announces-NemoClaw-for-the-OpenClaw-Community/default.aspx). As NVIDIA describes it, the router decides, per query, whether to use the local Nemotron model or route to a cloud frontier model. The routing decision is policy-driven, not model-driven — the agent does not choose. Administrators define what categories of data can leave the sandbox, and the router enforces it.

For tasks that require frontier model capability — complex reasoning, multi-modal input, tasks where Nemotron's quality is insufficient — the router sends the query to the cloud endpoint with private data fields redacted or excluded, based on the policy file.

---

## Installation

The installation story is [one command](https://docs.nvidia.com/nemoclaw/latest/), documented as a shell one-liner rather than an npm command:

```bash
curl -fsSL https://www.nvidia.com/nemoclaw.sh | bash
```

This installs the CLI, the [OpenShell runtime](https://github.com/NVIDIA/NemoClaw), and launches a sandboxed OpenClaw instance with a default policy file you can customize. If you are running OpenClaw already, migration is additive — you install the OpenShell layer on top of your existing setup.

---

## What Hardware You Need

NemoClaw is [designed to run on GeForce RTX PCs and laptops, RTX PRO workstations, DGX Station, and DGX Spark](https://blogs.nvidia.com/blog/industrial-software-leaders-secure-autonomous-ai-engineers-nemoclaw/) — hardware NVIDIA already sells:

| Platform | Status |
|---|---|
| RTX 4090 / 5090 desktop | Supported now |
| RTX PRO workstations | Supported now |
| DGX Spark (desktop AI supercomputer) | Supported now |
| DGX Station | Supported now |
| N1X laptops (launched at Computex as [RTX Spark](https://blogs.nvidia.com/blog/nvidia-gtc-taipei-computex-2026-news/)) | Fall/holiday 2026 |

The N1X/RTX Spark chip is relevant here specifically because it brings CUDA and the full NVIDIA developer toolchain — including the NemoClaw stack — to a portable device. [NVIDIA describes it as a 20-core Grace CPU paired with a Blackwell RTX GPU](https://blogs.nvidia.com/blog/nvidia-gtc-taipei-computex-2026-news/), and [independent reporting on the Computex reveal puts the GPU at 6,144 CUDA cores with up to 128 GB of unified LPDDR5X memory on a TSMC 3nm process](https://www.tomshardware.com/laptops/nvidia-unveils-rtx-spark-superchip-at-computex-2026-new-platform-promises-to-turn-windows-into-an-agentic-ai-os-with-arm-cpu-blackwell-gpu-and-128gb-unified-memory). Nemotron running locally on a laptop with that much unified memory is a different product category than Nemotron running on a desktop workstation. Field agents, remote workers, and executives who travel with sensitive data are the target users.

---

## What NemoClaw Does Not Fix

NemoClaw addresses the governance gap — it does not fix ClawHub.

The 1,184 malicious skills in the OpenClaw marketplace are still there. NemoClaw's YAML policy system limits what a malicious skill can do if it runs inside your sandbox, but it does not prevent the skill from running at all. If a developer or automated process installs a compromised skill and grants it network access in the policy file, the sandbox becomes less useful.

The defense here is the same as in any software supply chain context: audit your skill dependencies, pin versions, and do not grant network access by default. NemoClaw gives you the enforcement mechanism; you still have to write the policies correctly.

There is also no ClawHub equivalent inside the NemoClaw ecosystem. NVIDIA provides Nemotron models and the OpenShell runtime. Verified skills are available through the NVIDIA Agent Toolkit, but the catalog is far smaller than ClawHub. If you depend on the breadth of the ClawHub ecosystem, you are still making trust decisions that NemoClaw cannot make for you.

---

## What This Costs

NemoClaw itself is open source. There is no licensing cost.

The cost model shifts to:
- **Hardware**: An RTX-class GPU to run Nemotron locally. The marginal cost of inference on owned hardware is electricity.
- **Cloud frontier model API calls**: For queries routed out of the sandbox, you pay the usual API rates. The privacy router is designed to minimize these, not eliminate them.
- **DGX hardware** (if you want production-grade multi-agent deployments): DGX Spark launched at [$3,999](https://www.engadget.com/ai/nvidia-starts-selling-its-3999-dgx-spark-ai-developer-pc-120034479.html) in October 2025, but [NVIDIA raised the Founders Edition price to $4,699 in February 2026](https://videocardz.com/newz/nvidia-officially-raises-dgx-spark-founders-edition-msrp-to-4699) citing memory supply constraints. DGX Station, [built around the GB300 Grace Blackwell Ultra Superchip](https://www.servethehome.com/nvidia-dgx-station-systems-available-at-last-gb300-gb200-workstations-for-your-desktop/), runs [roughly $100K depending on configuration](https://twowintech.com/nvidia-dgx-spark-vs-nvidia-dgx-station-a-comprehensive-comparison/) — well over an order of magnitude above DGX Spark.

For small teams, the RTX desktop + NemoClaw combination is a plausible alternative to paying per-token for every agentic call. For enterprises with compliance requirements around data residency, the local-by-default model has value independent of cost.

---

## Builder Action Items

**If you are not running OpenClaw yet:**

1. Read the [OpenClaw security brief](https://chatforest.com/builders-log/openclaw-454-cve-clawhub-malicious-skills-builder-security-guide/) we published three days ago before starting any evaluation. Understand the CVE landscape before you adopt.
2. Start with NemoClaw rather than base OpenClaw. Installing the security layer from the beginning is easier than retrofitting it.
3. Write your YAML policy file before deploying your first agent. Define the minimum necessary access. Default-deny for network. Explicit allow-list for filesystem paths.

**If you are running OpenClaw already:**

1. Inventory your current skill dependencies and audit against the [ClawHub malicious packages list](https://chatforest.com/builders-log/openclaw-454-cve-clawhub-malicious-skills-builder-security-guide/).
2. Install OpenShell alongside your existing setup. This is additive and does not require migrating agent configurations.
3. Migrate agent configs to YAML policies one agent at a time. Start with agents that handle sensitive data.

**If you are in enterprise IT evaluating OpenClaw:**

1. Do not evaluate base OpenClaw for enterprise deployment. Evaluate NemoClaw specifically.
2. Map your data classification policy to the YAML policy schema before piloting. If you cannot define what data can leave the sandbox, the privacy router cannot enforce it.
3. Treat ClawHub skills as untrusted third-party dependencies. Apply the same review process you use for npm or PyPI packages.

---

## The GTC Taipei Context

NemoClaw was not the only announcement at GTC Taipei on June 1. Jensen Huang also formally revealed:

- **N1X**: [NVIDIA's first ARM laptop SoC](https://blogs.nvidia.com/blog/nvidia-gtc-taipei-computex-2026-news/), officially launched at Computex as RTX Spark — [20-core CPU, 6,144-core Blackwell GPU, up to 128 GB LPDDR5X, on a TSMC 3nm process](https://www.tomshardware.com/laptops/nvidia-unveils-rtx-spark-superchip-at-computex-2026-new-platform-promises-to-turn-windows-into-an-agentic-ai-os-with-arm-cpu-blackwell-gpu-and-128gb-unified-memory). [Dell confirmed an XPS model at the show](https://videocardz.com/newz/dell-confirms-xps-laptop-with-nvidia-n1x-at-computex), with Lenovo, Asus and Microsoft Surface variants also announced; [first devices ship this fall](https://www.pcworld.com/article/3154922/rtx-spark-all-the-laptops-and-mini-pcs-announced-so-far.html).
- **Constellation campus**: [NVIDIA's new Taiwan headquarters in Beitou-Shilin Technology Park, sized for roughly 4,000 employees](https://blogs.nvidia.com/blog/nvidia-gtc-taipei-computex-2026-news/), targeted to open around 2030. [Huang said NVIDIA's Taiwan spending has grown to about $100 billion a year, on a path toward $150 billion](https://www.cnbc.com/2026/05/27/nvidia-taiwan-investment-150-billion-spending.html) — up from roughly $10-15 billion a year five years earlier.
- **Vera Rubin supply chain**: Huang described Vera Rubin as ["the largest product launch, probably in the history of Taiwan,"](https://blogs.nvidia.com/blog/nvidia-gtc-taipei-computex-2026-news/) with nearly 2 million parts per system and 150 ecosystem partners. [H2 2026 cloud deployments — AWS, Google Cloud, Azure, Oracle Cloud and others — remain on schedule](https://www.techtimes.com/articles/318651/20260618/nvidia-vera-rubin-nvl72-cloud-rollout-expands-europe-h2-deployments-near.htm).

For builders, the NemoClaw story is the most immediately actionable. N1X and Vera Rubin affect your infrastructure options on a 6–18 month horizon. NemoClaw is deployable today if you have RTX hardware.

---

## The Bottom Line

OpenClaw is real infrastructure. The growth numbers are not hype — [250,000 GitHub stars, past React's decade-long total](https://www.star-history.com/blog/openclaw-surpasses-react-most-starred-software/), reflects genuine adoption driven by a genuinely different agent architecture. The security problems are also real and documented.

NemoClaw is the first credible answer to the question: how do you run OpenClaw in a context where data governance matters? It does not fix every problem — ClawHub supply chain risk remains — but it gives IT a policy lever, gives agents a data boundary, and gives builders a path to production that does not require accepting "insecure by default" as the answer.

The one-command install and open-source licensing mean the barrier to evaluating it is low. Given what we know about the base OpenClaw security posture, evaluating NemoClaw before deploying any persistent agent is worth the hour it takes to read the documentation.

---

*ChatForest tracks builder-relevant AI infrastructure developments. Previous coverage: [OpenClaw 454 CVEs and 1,184 malicious marketplace skills](https://chatforest.com/builders-log/openclaw-454-cve-clawhub-malicious-skills-builder-security-guide/) · [NVIDIA GTC Taipei preview](https://chatforest.com/builders-log/nvidia-gtc-taipei-2026-vera-rubin-n1x-five-layer-cake-builder-preview/) · [NVIDIA N1X preview](https://chatforest.com/reviews/nvidia-n1x-computex-2026-blackwell-laptop-ai-pc-preview/)*

