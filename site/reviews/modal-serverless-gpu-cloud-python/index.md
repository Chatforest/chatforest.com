# Modal — Serverless GPU Cloud for Python (2026 Review)

> Modal reviewed: Python-native serverless GPU cloud with sub-second cold starts, custom Rust container runtime, per-second billing. $50M ARR, $2.5B valuation in progress. Rating: 4/5.


There are two ways to give developers access to GPU compute. The first is to give them a machine: configure SSH, set up Docker, manage dependencies, pay for idle time, and learn to live with the gap between the local laptop and the remote server. The second way is to make the problem disappear.

Modal takes the second approach. It was built around the thesis that the right interface between a Python developer and a GPU cluster is a Python decorator.

That sounds like a simple product decision. It is actually an enormous infrastructure commitment. To make it true — to make a `@modal.function()` decorator work as a seamless bridge between a laptop and a fleet of H100s with sub-second startup — requires custom everything: a container runtime, a filesystem, a scheduler, and an abstraction layer that hides all of it from the user.

Modal built all of that from scratch. This review explains what they built, why it matters, and where the trade-offs land.

Part of our **[Developer Tools category](/categories/developer-tools/)**.

---

## At a Glance

| | |
|---|---|
| **Service** | [Modal](https://modal.com/) |
| **Founded** | 2021, New York, NY |
| **CEO** | Erik Bernhardsson (co-founder; prev. Spotify ML, Better.com CTO) |
| **CTO** | Akshat Bubna (co-founder) |
| **Funding** | $87M Series B (Sept 2025) — $1.1B valuation |
| **New round (talks)** | Targeting ~$2.5B valuation (Feb 2026); General Catalyst expected to lead |
| **Revenue** | ~$50M ARR (reported at time of $2.5B talks) |
| **Investors** | Amplify Partners, Redpoint, Threshold Ventures; General Catalyst (incoming) |
| **GPU catalog** | T4, A10G, A100 (40GB/80GB), H100 (80GB), B200 |
| **Cold start** | Sub-second (most workloads); <3s with CRIU memory snapshots for heavy deps |
| **Billing** | Per-second; zero idle cost |
| **Architecture** | Multi-cloud (AWS, GCP, OCI); custom Rust runtime; custom lazy-loading filesystem |
| **SDK** | Python decorator API (`@modal.function()`, `@modal.cls()`) |
| **Workload types** | Inference, training, batch, scheduled functions, web endpoints, async queues |
| **Free tier** | Starter: $30/month free credits |
| **Team plan** | $250/month (includes $100 credits) |

---

## The Core Idea: Infrastructure as a Decorator

Erik Bernhardsson spent seven years at Spotify building the music recommendation system, then ran the 300-person engineering team at Better.com. In both roles, he watched the same problem repeat: data and ML teams had a hard time getting code from a laptop to a cluster without weeks of DevOps friction.

Modal was started in 2021 to solve that problem at its root. Not by building better Kubernetes tooling. By replacing the abstraction entirely.

The key insight is that a Python function is a better unit of deployment than a container. If you can annotate a function with a GPU type and a set of dependencies, the platform should handle provisioning, billing, networking, and teardown invisibly. The developer writes code; the cloud runs it. Nothing in between.

Here is what that looks like in practice:

```python
import modal

app = modal.App("inference-demo")

@app.function(gpu="H100", image=modal.Image.debian_slim().pip_install("transformers", "torch"))
def run_inference(prompt: str) -> str:
    from transformers import pipeline
    pipe = pipeline("text-generation", model="meta-llama/Llama-3.3-70B-Instruct")
    return pipe(prompt)[0]["generated_text"]
```

That function runs on an H100 in the cloud. Modal provisions the GPU, installs the packages, runs the code, and tears the container down afterward. You pay only for the seconds it runs. You do not write a Dockerfile. You do not configure a Kubernetes pod spec. You do not manage a persistent VM that accrues charges while idle.

The simplicity is real. So are the constraints — which we will get to.

---

## What Modal Actually Built: The Infrastructure Behind the Decorator

The developer experience is the interface. The engineering achievement is what makes that interface fast enough to be useful.

### Custom Container Runtime (Rust)

Modal does not use Docker. It wrote its own container runtime in Rust, specifically optimized for startup performance. Docker's container startup sequence involves image pulls, layer extraction, copy-on-write filesystem setup, and namespacing operations that compound to multi-second cold starts even for small images. Modal's runtime eliminates those layers entirely, reducing container startup to the point where it is no longer the bottleneck in most workloads.

The decision to build from scratch (rather than on top of Kubernetes) was deliberate. Kubernetes and Docker are optimized for long-running services that start infrequently. Modal's workload is the opposite: short-lived functions that need to start in milliseconds, potentially thousands of times per hour.

### Custom Lazy-Loading Filesystem (FUSE in Rust)

The second bottleneck in cold starts is package loading. A PyTorch installation is roughly 2–3 GB. If every cold start had to download and install PyTorch, sub-second performance would be impossible.

Modal built a custom filesystem using FUSE (Filesystem in Userspace), implemented in Rust after a first iteration in Python proved too slow. The filesystem lazy-loads: when a container starts, it does not pull all dependencies upfront. It fetches only what the code path actually accesses, on demand, from a distributed cache. Most workloads only read a fraction of an installed package's files — Modal loads only that fraction.

The result: containers start executing code before their full dependency set is loaded. For most workloads, the actual execution latency (from function call to first line of Python running) is under one second.

### CRIU Memory Snapshots for Heavy Workloads

For workloads where even lazy-loading is insufficient — particularly large model inference with transformer models that require multiple seconds of initialization — Modal supports memory snapshots using CRIU (Checkpoint/Restore in Userspace).

CRIU allows a running Linux container to be snapshotted to disk and restored later, including all in-memory state. Modal uses this to snapshot a container after initialization (model loaded into GPU memory, tokenizer initialized, etc.) and restore it on subsequent invocations. Cold starts with memory snapshots are typically under 3 seconds even for large PyTorch models.

### Multi-Cloud Scheduler (AWS, GCP, OCI)

Modal does not own its own GPU hardware. It operates as a multi-cloud scheduler: it purchases capacity from AWS, Google Cloud, and Oracle Cloud Infrastructure, then dispatches workloads to whichever availability zone has GPUs available at dispatch time. The user does not choose a region; Modal's scheduler routes automatically.

This creates two properties:
1. **Higher availability**: if one cloud has a capacity shortage, the scheduler can route to another.
2. **Preemptibility**: because Modal is purchasing spot/preemptible capacity to keep prices down, every GPU workload can be interrupted and rescheduled. This is an important trade-off (discussed below).

---

## GPU Catalog and Pricing

Modal's published per-second GPU rates:

| GPU | Per Second | Per Hour (approx.) |
|---|---|---|
| NVIDIA T4 | $0.000164/s | $0.59/hr |
| NVIDIA A10G | — | ~$1.10/hr |
| NVIDIA A100 (40GB) | ~$0.00044/s | $1.58/hr |
| NVIDIA A100 (80GB) | — | ~$2.00/hr |
| NVIDIA H100 (80GB) | $0.001097/s | $3.95/hr |
| NVIDIA B200 | — | $6.25/hr |

**Important pricing caveat**: per-second rates are base rates. Modal applies regional and preemption multipliers in production. Published analyses have found real-world costs running approximately 3.75x the advertised base rate in high-demand configurations. This is not hidden — Modal's pricing page documents the multiplier structure — but it means the effective H100 cost in some configurations can approach $14–15/hr, comparable to or higher than on-demand rates from major cloud providers.

The free tier (Starter plan) includes $30/month in credits, which is enough for meaningful experimentation — a few hundred H100 GPU-seconds, or tens of thousands of T4 GPU-seconds. The Team plan ($250/month) includes $100 in credits and raises limits to 1,000 containers and 50 concurrent GPUs.

---

## What You Can Build on Modal

Modal is not limited to inference. The function-based abstraction generalizes to almost any Python workload:

**Inference endpoints**: serve a model as a web endpoint with auto-scaling to zero. Traffic spikes provision more containers; idle periods cost nothing.

**Batch inference**: process a list of inputs in parallel across GPU workers. Each item in the list can be dispatched as a separate function invocation.

**Training jobs**: run single-GPU or multi-GPU training. Modal supports mounting volumes for checkpoints and persistent datasets.

**Scheduled functions**: run a Python function on a cron schedule. Same GPU access, same zero-config experience.

**Async queues**: decouple a producer (HTTP request handler) from a consumer (GPU worker). Modal handles the queue infrastructure.

**Web endpoints**: expose any function as an HTTPS endpoint with a few lines of code. Modal handles SSL, routing, and auto-scaling.

One notable distinction from purely inference-focused platforms: Modal does not provide a curated model catalog. If you want to run Llama 4, you write the code to load Llama 4. This is more powerful (you can run anything) and more demanding (you need to know how to load and serve models). Platforms like Together AI and Groq provide API endpoints for named models; Modal gives you the GPU and a Python runtime.

---

## Developer Experience: What Works

The developer experience is Modal's primary selling point, and it largely delivers.

**Local-to-cloud parity**: functions decorated with `@modal.function()` can be called locally for testing (they execute on a Modal GPU, but you invoke them from your laptop) or deployed as persistent services. The same code runs in both contexts.

**Dependency management**: Modal images are defined as Python objects. You specify pip packages, system packages, and base images using method chains. There is no Dockerfile syntax to learn, though you can also build from an existing Dockerfile if you prefer.

**Secrets**: API keys and credentials are stored as Modal Secrets, injected into function environments at runtime. They are never in code or environment files.

**Volumes**: persistent storage is handled via Modal Volumes, mountable inside functions. Useful for model weights, datasets, and checkpoints that should not be re-downloaded on every invocation.

**Streaming and real-time outputs**: Modal supports generator functions that yield output incrementally — important for LLM token streaming.

**GPU type negotiation**: you can specify a list of GPU types in priority order. If an H100 is unavailable, fall back to A100. The scheduler handles the rest.

---

## Where Modal Has Trade-Offs

### Preemptibility

Every GPU workload on Modal is preemptible — it can be interrupted and rescheduled at any time. For short inference calls, this is rarely a problem: the overhead of a restart is small relative to the job. For long training runs (hours or days), preemption without careful checkpointing design means lost progress.

Modal supports checkpointing via volumes, but you have to implement it. Platforms like Lambda Labs that sell dedicated GPU VMs guarantee that your job will not be evicted mid-run.

### Cost at Scale

The per-second billing and zero-idle model are genuinely valuable at low utilization — maybe up to 40–50% GPU utilization. Above that threshold, the preemption multipliers and management overhead mean Modal can cost more than a reserved or dedicated instance from a cloud provider or GPU-focused host like CoreWeave or Lambda Labs.

Sustained high-throughput production inference — where you expect GPUs to run near-continuously — is typically not Modal's strongest positioning. At that utilization level, the developer-experience premium costs more than it saves.

### No Managed Model Catalog

If you want to call `gpt-4o` or `llama-4-scout` without writing serving code, use OpenAI, Together AI, Fireworks, or Groq. Modal is for teams that want to host their own models, run their own fine-tunes, or build custom inference pipelines. The distinction matters: Modal requires Python ML engineering skills to get value from; it is not a model API.

### Preemptible Execution Documentation

The preemptible-GPU caveat deserves emphasis: Modal's documentation states that non-preemptible execution for GPU functions is not supported. This is a real constraint for latency-sensitive production systems where a GPU job being rescheduled mid-call would produce a visible failure. For such workloads, dedicated GPU hosting is more appropriate.

---

## Business and Funding

Modal was founded in 2021 by Erik Bernhardsson and Akshat Bubna. Bernhardsson built the machine learning infrastructure behind Spotify's Discover Weekly and other personalization features during a seven-year tenure, then ran the 300-person engineering organization at Better.com (the mortgage startup) from 2015 to 2021. He founded Modal after observing firsthand how much engineering effort teams spend on infrastructure rather than models.

**Funding history**:
- Seed rounds supported by Amplify Partners and others (2021–2023)
- **Series B**: $87M (September 2025) at $1.1B valuation

**New round (Feb 2026)**: TechCrunch and other outlets reported that Modal was in early discussions to raise a new round at approximately $2.5B valuation, more than double the September valuation. General Catalyst was reported as the expected lead. Bernhardsson publicly downplayed the reports as premature, while sources confirmed active conversations. If completed, the round would represent a 2.3x step-up in valuation in less than six months.

**Revenue**: approximately $50M ARR, as reported in conjunction with the $2.5B valuation discussions. This implies a revenue multiple of roughly 50x ARR at $2.5B — elevated, but consistent with comparable AI infrastructure companies in current fundraising markets.

Modal is a small company (roughly 58 employees) generating meaningful revenue relative to headcount. It made two notable acquisitions: Twirl (a database tooling company) and Tidbyt (a consumer electronics company making programmable pixel-art displays) — the strategic rationale for Tidbyt is not obvious from public information, but Twirl suggests interest in data infrastructure adjacent to compute.

---

## Competitive Position

**vs. RunPod**: RunPod sells serverless GPU functions (direct Modal competitor) and persistent GPU pods. RunPod is meaningfully cheaper for sustained workloads — A100 at $1.89–2.49/hr vs. Modal's effective rate. RunPod requires more DevOps awareness (you configure containers explicitly). Modal wins on developer experience, cold start consistency, and Python-native workflow. For high-utilization production use, RunPod is typically cheaper.

**vs. Together AI / Fireworks AI / Groq**: These are inference-as-a-service providers. They host the models; you call an API. Modal gives you the GPU and lets you host your own. Complementary rather than directly competitive — many teams use both (Together/Fireworks for off-the-shelf models, Modal for custom fine-tunes or proprietary models).

**vs. Replicate**: Replicate also focuses on ML model deployment, but with a community-first model-sharing approach (via their open-source Cog tooling). Replicate is optimized for deploying and sharing models publicly; Modal is optimized for building private production systems. Replicate has slower cold starts than Modal for equivalent workloads.

**vs. AWS/GCP/Azure**: The major clouds offer GPU VMs and container services, but the developer experience is significantly heavier: Dockerfile management, Kubernetes, IAM policies, and VPC configuration. Modal's value proposition is entirely the reduction of that overhead. For teams with existing cloud infrastructure and DevOps capacity, the cost-benefit calculus may favor the major clouds. For ML-focused teams without dedicated platform engineers, Modal's approach removes weeks of setup.

---

## Limitations

- **Preemptible GPUs only**: all GPU workloads can be interrupted; no non-preemptible option.
- **No model catalog**: you write the serving code; Modal provides the compute.
- **Cost at high utilization**: the per-second + multiplier model becomes expensive above ~40–50% steady-state utilization.
- **No fine-tuning platform**: Modal gives you GPUs to run training scripts, but it does not provide fine-tuning UI, managed datasets, or DPO/SFT workflows the way Fireworks AI does.
- **Smaller team**: ~58 employees means a narrower support footprint than AWS or GCP.
- **No multi-cloud control**: the scheduler picks regions automatically; you cannot pin to a specific cloud or AZ.

---

## Rating: 4/5

Modal is the best answer to a specific question: *how do I run Python ML code on GPUs without managing infrastructure?* For that use case, it is genuinely excellent — the Python decorator SDK, sub-second cold starts, and zero-idle billing are real engineering achievements that save meaningful engineering time.

The platform loses a point because of real constraints: preemptible-only GPU execution (a problem for long training runs and latency-sensitive production systems), pricing multipliers that can surprise teams at scale, and the absence of a managed model catalog (requiring users to implement model serving themselves).

For an ML practitioner or startup team writing custom model code and wanting GPU access without DevOps overhead, Modal is one of the most productive environments available. For teams running sustained high-throughput inference at fixed models with known traffic, a dedicated-instance provider will likely prove cheaper.

| | |
|---|---|
| **Rating** | 4 / 5 |
| **Best for** | ML engineers building custom model pipelines; teams without dedicated DevOps |
| **Not ideal for** | Sustained high-utilization inference; long training runs without checkpointing; teams wanting a managed model API |
| **Pricing model** | Per-second + multipliers; free $30/mo starter credits |
| **Bottom line** | The most developer-friendly GPU cloud available — at a price premium vs. raw-compute alternatives |

---

*This review is based on publicly available documentation, pricing pages, and published technical analysis. ChatForest researches these platforms; we do not have a commercial relationship with Modal.*

