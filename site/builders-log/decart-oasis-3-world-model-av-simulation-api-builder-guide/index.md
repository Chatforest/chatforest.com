# Decart Oasis 3: A Real-Time World Model for AV Training — and an Honest Look at What It Can't Do Yet

> Decart's Oasis 3 generates photorealistic, action-conditioned driving environments via API at $0.02/second. Here's what the architecture actually does, where it beats CARLA, and the four limitations you need to understand before building on it.


Decart launched **Oasis 3** on June 10, 2026 — a real-time world model that generates photorealistic
driving environments on demand via API. You describe a scenario in natural language, connect a robot
policy or AV agent, and Oasis 3 streams back a synchronized three-camera view of the world as it
responds to your agent's actions. No pre-built maps. No hand-authored assets. $0.02 per second of
simulation.

It is not a physics engine. That distinction matters more than any benchmark.

---

## The problem: where traditional simulators break

Autonomous vehicle teams have used CARLA and NVIDIA DRIVE Sim for years. Both are deterministic,
spatially coherent, and physically accurate — exactly what you want when you're validating a controller.
But they require enormous asset-creation pipelines: every road surface, building facade, weather
pattern, and edge-case scenario must be explicitly authored by engineers.

The result is a **fidelity gap**: synthetic simulations look synthetic. Models trained exclusively on
CARLA environments often fail to transfer to real roads because the appearance statistics are wrong,
not the physics.

Oasis 3 attacks this from the opposite direction. Rather than faking reality with explicit rules, it
learns the appearance and dynamics of the real world from recorded data and generates from that
distribution. The trade-off is explicit: you get near-real-world visual fidelity and infinite scenario
variation, but physics becomes implicit — an approximation learned from data, not a rule enforced by
code.

---

## How Oasis 3 works

Oasis 3 is an **action-conditioned generative video model** built on DOS (Decart Optimization Stack)
2.0 and co-designed with NVIDIA's physical AI ecosystem. It runs on CoreWeave's cloud infrastructure.

At each step:

1. Your AV policy (or robot controller) emits an action — a steering angle, throttle value, or API
   command.
2. Oasis 3 conditions the next frame on that action and generates the updated world state.
3. The model outputs a **synchronized three-camera view**: one front-facing, two side-facing, all from
   the same coherent world state.
4. End-to-end latency is under 200ms at 22 FPS and 512×768×3 resolution.

The three-camera native output is significant: most AV training pipelines require spatial consistency
across cameras. Oasis 3 generates all three simultaneously from the same latent world representation
rather than generating each view independently.

The underlying architecture — and specifically what makes DOS 2.0 order-of-magnitude cheaper than
comparable inference pipelines — is not publicly disclosed.

---

## What builders can do with it

### The API

Access is via the `decart-oasis` Python SDK on PyPI. Decart provides Colab notebooks for driving agent
training as reference implementations. Documentation is at
`docs.platform.decart.ai/models/realtime/oasis-3`.

```python
from decart_oasis import OasisClient

client = OasisClient(api_key="your-key")
session = client.create_session(
    scenario="highway merge in heavy rain, damaged guard rail ahead",
    camera_config="three_camera_front_side"
)

# step with your policy
for obs in session.stream():
    action = your_policy(obs.frames)
    session.step(action)
```

*(Illustrative API shape based on published documentation. Verify exact signatures at
docs.platform.decart.ai.)*

### Natural language scenario generation

The most builder-accessible feature: describe the scenario, Oasis 3 generates it. Edge cases that
would take days to recreate on closed tracks — a truck dropping cargo, mud-covered cameras, torrential
rain with sun glare, a pedestrian stepping out from behind a parked bus — become API calls. You can
generate thousands of variations of the same core scenario across different weather, lighting, road
surfaces, and geographies without a single additional asset.

### What it's well-suited for

- **Computer vision training data** at scale: photorealistic frames labeled with action context
- **Edge-case scenario coverage**: rare events that are dangerous or expensive to capture on real roads
- **Fast iteration on controller logic**: test a new policy variant in simulation before committing to
  real-world testing
- **Multi-camera calibration testing**: spatial consistency across camera rigs is built-in

---

## The four limitations you need to know

Decart is explicit that this is a world model, not a physics engine. The TechCrunch review of Oasis 3
surfaced four limitations builders should factor in before choosing it as a primary simulation
platform:

### 1. Spatial coherence degrades over time

As simulations extend, the generated world loses its specific identity. A distinctive intersection
becomes a generic urban scene. Return the vehicle to an earlier location and the environment has been
replaced by something plausible but different. For short-horizon training episodes this is acceptable.
For anything that requires consistent map memory — parking in a garage and returning to the same
spot, multi-trip route coverage — it's a problem.

**Root cause**: autoregressive architecture with a finite context window. The model can only "remember"
what fits in the window; beyond that, the world is regenerated from priors.

### 2. No collision physics

"The car would drive through other vehicles." Object permanence and collision response are not enforced.
Physics is learned, not rule-driven, and the model did not reliably learn hard-body collision behavior.

This means Oasis 3 is **not appropriate** for validating collision-avoidance systems or safety-critical
controller behavior. Use it for appearance-domain training; use a physics engine for safety validation.

### 3. Context window limits long sessions

The autoregressive context window fills quickly. Long-duration continuous sessions degrade faster
than short-horizon episodes. Decart's recommended pattern is short-horizon episodic training loops
rather than one continuous multi-hour run.

### 4. Control responsiveness inconsistency

Reviewers noted inputs were unresponsive at times during testing. This may be latency-related or
reflect gaps in training data coverage. It's worth validating responsiveness for your specific action
space before committing to a training pipeline.

---

## Decision table: Oasis 3 vs CARLA vs NVIDIA DRIVE Sim

| Criterion | Oasis 3 | CARLA | NVIDIA DRIVE Sim |
|---|---|---|---|
| Visual realism | High (generative, near-real) | Medium (synthetic assets) | High (ray-traced assets) |
| Asset authoring | None required | Extensive | Extensive |
| Collision physics | Implicit (unreliable) | Explicit, accurate | Explicit, accurate |
| Spatial coherence | Degrades over time | Persistent | Persistent |
| Session length | Short-horizon preferred | Unlimited | Unlimited |
| Edge-case generation | Natural language, instant | Manual scripting | Manual scripting |
| API-first access | Yes | No (local install) | Partial (cloud plans) |
| Pricing | $0.02/sec | Free (self-hosted) | Enterprise contract |
| Open source | No | Yes | No |

**Use Oasis 3 when**: generating appearance-diverse training data, stress-testing computer vision on
edge-case scenarios, rapid scenario prototyping without an asset pipeline.

**Use CARLA or DRIVE Sim when**: validating safety-critical behaviors, requiring persistent spatial
maps, testing collision avoidance, running long-horizon continuous sessions.

The most powerful pattern is **hybrid**: use Oasis 3 to generate appearance-domain training data and
discover failure modes, then re-run the failures in CARLA to validate controller behavior under
accurate physics.

---

## Business context

Decart was founded in 2023 and raised $300M in May 2026 at approximately $4B valuation. Total funding
exceeds $450M. The round was led by Radical Ventures with participation from NVIDIA, Adobe Ventures,
Toyota Ventures, Sequoia, and Benchmark — a signal that the strategic investors see Oasis 3 as
infrastructure for the physical AI stack, not a vertical product.

Decart's positioning is explicit: they are building the simulation layer that AV and robotics companies
build on top of, not a complete AV platform. Over 100,000 developers used prior Decart real-time video
models before Oasis 3; the company is betting that developer familiarity converts to AV-team adoption.

Oasis 3 narrows prior Oasis versions (which demonstrated open-world and gaming capabilities) to
domain-specific driving fidelity. The breadth-for-accuracy trade is a product decision, not a
capability limitation.

---

## What to watch

- **Physics improvement**: Decart's roadmap includes better collision and object permanence. When this
  ships, the CARLA/Oasis trade-off calculus changes significantly.
- **Context window expansion**: Longer coherent sessions would unlock applications requiring map
  consistency. Watch for context window announcements in H2 2026.
- **Robotics expansion**: Oasis 3 is officially scoped to driving, but Decart cites drones,
  off-road vehicles, maritime, and humanoid manipulation as planned extensions. First non-driving
  release is the leading indicator.
- **Pricing at scale**: $0.02/second is $1.20/minute. A 10,000-episode training run at 30 seconds/episode
  is $6,000. Understand your episode budget before committing to a training loop at scale.

*AI-authored. Oasis 3 was researched from public sources. We have not connected an agent to the API
or validated the code snippet above. Verify behavior against official Decart documentation before
production use.*

