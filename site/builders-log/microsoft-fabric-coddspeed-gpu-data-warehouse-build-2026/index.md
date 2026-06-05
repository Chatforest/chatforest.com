# CoddSpeed: Microsoft Fabric's GPU-Accelerated Warehouse Is a 7x Benchmark Claim With a Research Paper to Back It Up

> Microsoft announced CoddSpeed at Build 2026 — GPU-accelerated query processing in Fabric Data Warehouse, no query rewrites required. The system won SIGMOD 2026 Best Paper and shows up to 7x performance against three comparable cloud warehouses at 64-user concurrency. Early access opens July 2026.


**At a glance:** CoddSpeed, announced June 2, 2026 at Microsoft Build. GPU-accelerated query processing in Fabric Data Warehouse — no query rewrites required. SIGMOD 2026 Industry Track Best Paper. Benchmark: up to 7x faster than three comparable cloud warehouses at 64-user concurrency. UNC Health (healthcare) reports 5x production improvement on existing workloads. Architecture supports GPUs, FPGAs, ASICs, NVLink, InfiniBand. Early access preview: July 2026. Part of our **[Builder's Log](/builders-log/)**.

---

The name is deliberate. Edgar F. Codd invented the relational model in 1970. Microsoft's new GPU-accelerated query engine for Fabric Data Warehouse is called CoddSpeed — part tribute, part positioning. The relational model ran on CPUs for 55 years. Microsoft is making a case that the next phase runs on something else.

Whether that case holds over time is an open question. But the research is real, the benchmarks are specific, and the timeline is July 2026. That's worth understanding before the early access queue opens.

---

## What CoddSpeed Actually Is

CoddSpeed is a query execution substrate inside Microsoft Fabric Data Warehouse that offloads analytical query processing from CPUs to hardware accelerators. In the July 2026 early access, that means NVIDIA GPUs. The underlying architecture is designed to host multiple accelerator types over time: FPGAs, ASICs, and custom silicon are explicitly listed as future targets. NVLink and InfiniBand are supported for data movement between components.

The GPU execution engine is derived from Microsoft Research's **Tensor Query Processor (TQP)** — a research project that has been developing GPU-native relational query processing for several years. CoddSpeed takes that research and puts it into Fabric's production warehouse layer.

The claim that matters most to builders: **no query rewrites required.** You do not need to modify your SQL, restructure your data model, or change your ingestion pipeline. GPU acceleration is transparent to existing workloads.

---

## The Benchmark Numbers

Microsoft published two sets of performance numbers:

**Against the CPU baseline (TPC-H 1TB benchmark):**
- Up to **30x faster** than Fabric's own CPU-based execution on TPC-H 1TB queries

**Against comparable cloud warehouses (internal testing, May 2026):**
| Concurrency | GPU-Fabric vs. Three Cloud DW Providers |
|---|---|
| Single user (1 concurrent) | ~3x faster |
| 16 concurrent users | ~6x faster |
| 64 concurrent users | ~7x faster |

The three providers are not named. The test covered "common reporting, application and AI-driven analytics scenarios" — not a disclosed subset of TPC-H or a named public benchmark.

**Customer evidence:**
- UNC Health (healthcare): up to **5x faster query speeds on existing workloads** in production

The concurrency scaling pattern is the interesting signal. The gap between GPU-accelerated Fabric and the unnamed comparators grows as user count increases. At single-user, 3x might reflect raw throughput advantage. At 64-user, 7x suggests the GPU architecture handles concurrency more efficiently — likely because GPU parallelism scales differently than CPU thread pools under mixed workload pressure.

For teams running heavy multi-user analytics — dashboards serving dozens of simultaneous viewers, scheduled reports plus interactive queries, agentic workflows querying the warehouse in parallel — the concurrency multiplier matters more than the single-user number.

---

## Research Credibility: The SIGMOD Paper

CoddSpeed was the **ACM SIGMOD 2026 Industry Track Best Paper.** SIGMOD is the premier database research conference. The Industry Track Best Paper specifically recognizes production systems that advance the field — not just internal engineering, and not just academic proposals. This is one of the highest forms of peer recognition in database research.

The paper describes CoddSpeed as "one of the first systems in the era of accelerated analytics" and documents lessons from production deployment. The architecture section covers:

- A novel data movement system using NVLink and InfiniBand
- Hardware-independence as a design principle: the system is built to run on a variety of compute and network accelerators, not just current-generation NVIDIA GPUs
- Validation across both TPC-H benchmarks and production workloads

The academic recognition matters to builders for one reason: **this is not a marketing demo.** GPU-accelerated analytics has been promised by multiple vendors for years. The SIGMOD Best Paper designation means Microsoft's implementation is being judged against the state of the art in database research, not just against its own press release.

---

## Architecture: What's Different About GPU Query Processing

Traditional data warehouses process analytical queries by breaking them into CPU-parallel operations: scan columns, filter predicates, aggregate results, join tables. Modern CPUs are fast but designed for sequential workloads with complex branch prediction.

GPUs are designed for massive parallelism across simple operations — exactly the kind of work that shows up in analytical query plans. Scanning a billion rows for values within a range, computing SUM or COUNT across columns, hashing join keys: these operations map naturally to GPU thread models.

The challenge has always been data movement. GPU memory is fast but not large enough for typical data warehouse datasets. CoddSpeed's NVLink and InfiniBand integration addresses this specifically — data moves to the GPU on demand through high-bandwidth interconnects rather than being resident in GPU memory at all times.

The result: the query planner can send operations to GPU execution dynamically without requiring the dataset to fit in VRAM. This is what makes transparent acceleration possible on production workloads that weren't designed for GPU execution.

---

## What This Means for Builders

**If you are already on Fabric Data Warehouse:**
GPU acceleration will arrive as an opt-in early access preview in July 2026. No migration. No schema changes. No SQL rewrites. The UNC Health result — 5x on existing workloads — is the most relevant number here: it came from a production customer running their existing queries on their existing data.

**If you are evaluating Fabric against Snowflake, Databricks, or BigQuery:**
The May 2026 benchmarks are not independently reproduced, and the three comparison providers are not identified. Treat the 3-7x range as a directional claim, not an audited result. The TPC-H 30x number against Fabric's own CPU baseline is more reliable (same system, controlled comparison), and still substantial.

**If you are running multi-user analytics workloads:**
The concurrency scaling pattern (3x → 7x as user count grows from 1 to 64) suggests this is most impactful for teams running high-concurrency reporting. A small team doing occasional ad-hoc queries gets 3x. A large organization running simultaneous dashboards plus automated agent queries gets 7x. Prioritize accordingly.

**If you are in healthcare, finance, or other high-query-volume regulated industries:**
The UNC Health case is notable not just for the 5x number but for the context: healthcare data workloads tend to be complex joins across large patient datasets. The 5x on production data, not a contrived benchmark, is a meaningful signal for adjacent industries.

**What Microsoft has not disclosed:**
- Pricing for GPU-accelerated execution (whether it's included in Fabric DW SKUs, usage-based, or a separate add-on)
- Which Fabric DW tiers will have access in July
- Multi-region availability at launch
- Query types or workload patterns that do *not* benefit from GPU acceleration

These gaps will matter for cost modeling and capacity planning. Check the July early access documentation before committing to architecture decisions based on the current benchmarks.

---

## The Architecture Roadmap Signal

Microsoft explicitly designed CoddSpeed to be hardware-independent. The paper lists GPUs as the current instantiation but frames the system as a "general substrate for hardware-accelerated query execution that can host different coprocessors over time."

FPGAs, ASICs, NVLink, and InfiniBand are all mentioned in the architecture scope. Microsoft has [its own custom silicon program](/builders-log/anthropic-microsoft-maia-200-custom-silicon-claude-inference-cost/) — MAIA — currently used for inference. Whether custom data warehouse silicon follows the same path is speculative, but the architectural decision to build CoddSpeed as a coprocessor-agnostic substrate is not accidental.

For builders, this is a long-term signal: Fabric DW acceleration is not a one-time GPU integration. It's a layer designed to absorb whatever the next generation of compute hardware looks like. That's a different kind of infrastructure bet than a GPU-specific optimization.

---

## What to Watch

- **July 2026:** Early access preview opens — sign up when the documentation appears on learn.microsoft.com
- **Pricing disclosure:** Watch for Fabric DW billing documentation to include GPU execution details
- **Independent benchmarks:** Third-party TPC-DS and TPC-H runs from the community will be more useful than Microsoft's internal numbers for comparison purposes
- **Snowflake/Databricks response:** Both have GPU acceleration roadmap items; CoddSpeed accelerates the competitive timeline

---

*CoddSpeed was announced at Microsoft Build 2026 and published as a Best Paper at ACM SIGMOD 2026. Source: [Microsoft Research publication](https://www.microsoft.com/en-us/research/publication/coddspeed-hardware-accelerated-query-processing-in-microsoft-fabric/), [Azure Blog — Build 2026 Fabric and Databases](https://azure.microsoft.com/en-us/blog/microsoft-build-2026-building-agentic-apps-with-microsoft-fabric-and-microsoft-databases/), [ACM Digital Library](https://dl.acm.org/doi/abs/10.1145/3788853.3803077).*

