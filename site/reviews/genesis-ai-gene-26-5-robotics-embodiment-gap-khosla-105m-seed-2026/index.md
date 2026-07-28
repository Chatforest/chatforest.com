# Genesis AI Wants to Teach Robots to Cook. Its $105M Approach Starts With a Glove.

> Genesis AI launched GENE-26.5, a foundational model for dexterous robotic manipulation backed by Eric Schmidt, Khosla Ventures, and Eclipse. The company thinks the embodiment gap — the reason robots still can't reliably do what humans do with their hands — is a data problem. And they may have solved it.


Robots can [beat the world's best Go players](https://deepmind.google/research/alphago/). They can [diagnose tumors from scans with accuracy that rivals or exceeds expert radiologists](https://blog.google/innovation-and-ai/technology/health/google-ai-breast-cancer-detection/).

They still struggle to crack an egg.

This gap — between AI's extraordinary performance in digital domains and its persistent clumsiness in the physical world — is what researchers call the embodiment gap. It is the reason that, despite decades of progress in both hardware and machine learning, the general-purpose robot remains a persistent future promise rather than a present reality.

A Paris-founded, globally distributed startup called Genesis AI thinks it has found the unlock. On May 6, 2026, the company [unveiled GENE-26.5](https://techcrunch.com/2026/05/06/khosla-backed-robotics-startup-genesis-ai-has-gone-full-stack-demo-shows/) — a foundational model for robotic manipulation — alongside a hardware system that its founders claim solves the data problem at the root of the gap.

The [$105 million seed round](https://techfundingnews.com/genesis-ai-105m-seed-funding/) behind the launch — reported independently by [TechCrunch](https://techcrunch.com/2025/07/01/genesis-ai-launches-with-105m-seed-funding-from-eclipse-khosla-to-build-ai-models-for-robots/) and [confirmed by co-founder Théophile Gervet himself](https://x.com/theo_gervet/status/1940059109224542363) — was led by Eclipse and Khosla Ventures, with participation from Bpifrance, HSG, and a notable roster of individual investors including Eric Schmidt, Xavier Niel, and AI researchers Daniela Rus and Vladlen Koltun. That combination of institutional backing, individual validator quality, and the specific research expertise of [Daniela Rus (MIT CSAIL director](https://news.mit.edu/newsoffice/2012/rus-named-csail-director-0522.html), robotics pioneer) and [Vladlen Koltun (distinguished scientist at Apple)](https://en.wikipedia.org/wiki/Vladlen_Koltun) suggests Genesis is being taken seriously by people who understand what it is attempting.

---

## The Problem: Why Robots Cannot Learn From Us

Human beings are extraordinarily good at physical manipulation. We can pick up a grape without crushing it, crack an egg one-handed, and simultaneously coordinate ten fingers across a piano keyboard — all without conscious attention. This dexterity accumulated over millions of years of evolution and billions of hours of embodied practice.

AI has gotten dramatically better at learning from human demonstrations, but there is a structural problem: human data and robot data are mismatched. When a researcher wants to teach a robot arm to perform a task, they typically use teleoperation — a human operator controls the arm manually while the system records what happens. The process is slow, expensive, and produces data that is slightly wrong in ways that matter. The operator is not using the robot's embodiment; they are approximating it.

This mismatch means robots have difficulty learning from the ocean of video data that shows humans doing things with their hands. Internet video is a vast training signal for language and vision models. For manipulation, it is mostly useless — because the robot's hand is not shaped like the human hand in the video.

---

## The Glove: A 1:1:1 Solution

Genesis AI's core innovation is what the company calls 1:1:1 mapping: a system where the data collection glove, the human hand wearing it, and the robotic hand receiving the trained model share identical kinematic structure.

The company designed a proprietary dexterous robotic hand that mirrors human hand form and function — not the stylized gripper common in industrial robotics, but something anatomically comparable. They then built a data collection glove with tactile-sensing electronic skin that maps precisely to the robotic hand's structure.

Because the embodiment is the same, the robot can learn directly from human demonstrations without translation loss. The person wearing the glove is, in a meaningful sense, teaching the robot using the robot's own body.

The practical numbers Genesis reports are striking. The company says the [glove hardware costs roughly one hundred times less than typical teleoperation systems, and that data collection is up to five times more efficient](https://www.prnewswire.com/news-releases/genesis-ai-unveils-gene-26-5--the-first-ai-brain-to-enable-robots-with-human-level-physical-manipulation-capabilities-302763638.html). Those are the kind of improvements that change the economics of training embodied AI models — comparable, in miniature, to how transformer architectures changed the economics of language model training.

---

## GENE-26.5: What It Can Do

The model launched at GENE-26.5 — [named for May 2026, with Zhou expecting many iterations ahead](https://techcrunch.com/2026/05/06/khosla-backed-robotics-startup-genesis-ai-has-gone-full-stack-demo-shows/). [The demonstration reel Genesis released](https://www.prnewswire.com/news-releases/genesis-ai-unveils-gene-26-5--the-first-ai-brain-to-enable-robots-with-human-level-physical-manipulation-capabilities-302763638.html) covers a range of long-horizon manipulation tasks, also independently described by [The Robot Report](https://www.therobotreport.com/genesis-ai-introduces-gene-foundation-model-more-dexterous-manipulation/):

**Cooking:** A 20-step meal preparation sequence including tomato chopping, one-handed egg cracking, and coordinated two-hand work. Cooking is a canonical hard problem in robotics — it involves varied objects, unpredictable state (eggs do not crack identically), and sequence dependency.

**Laboratory work:** Precision pipetting and liquid transfer tasks that require sustained fine motor control and calibrated force — the kind of work where industrial robots have historically been absent.

**Wire harnessing:** A manufacturing task that involves threading and routing flexible objects in three-dimensional space. Flexible object manipulation is notoriously difficult for robots.

**Piano performance at human level:** High-speed coordinated control across all fingers simultaneously, with accurate force modulation.

**Continuous in-air Rubik's Cube solving:** Single-handed manipulation of a three-dimensional object without placing it down — requiring constant real-time modeling of object state.

**Multi-object grasping:** Simultaneous grasp of four objects in a single reach, demonstrating dexterous finger independence.

Each of these would, independently, be a noteworthy result for a robotics system. Demonstrating them together with a single model is what makes the launch notable.

---

## The Simulation Advantage

Genesis AI is not relying solely on physical data collection. The company has developed what it describes as a next-generation simulation environment with high-realism physics and rendering — designed to allow AI to train AI in fully virtual environments.

The logic is the same as in language model scaling: if you can generate training data faster than physical reality allows, and if the simulation is faithful enough that skills transfer to the real world, you can dramatically accelerate model development. Genesis claims its simulation approach [lets teams "train and evaluate models orders of magnitude faster"](https://www.prnewswire.com/news-releases/genesis-ai-unveils-gene-26-5--the-first-ai-brain-to-enable-robots-with-human-level-physical-manipulation-capabilities-302763638.html) than physical-only training pipelines.

This is a known strategy — Physical Intelligence uses similar simulation-augmented training — but the 1:1:1 glove architecture makes it more powerful for Genesis specifically. Simulation data has historically suffered from the same translation problem as video data: the simulated embodiment rarely matches the physical robot precisely enough. When the robot's body is designed around the data collection system rather than the other way around, the sim-to-real gap narrows.

---

## The Competitive Landscape

Genesis enters a field that is suddenly very crowded and very well-funded.

**Physical Intelligence (π)** [raised a $400 million Series A in November 2024 at a $2.4 billion valuation](https://www.cnbc.com/2024/11/04/jeff-bezos-and-openai-invest-in-robot-startup-physical-intelligence.html) — [confirmed independently](https://techstartups.com/2024/11/05/robotics-ai-startup-physical-intelligence-raises-400m-funding-from-jeff-bezos-and-openai-now-at-2-4-billion-valuation/) — and has released π0, a cross-embodiment manipulation model. [Founded by veterans of Google DeepMind, Google Research, Stanford, and UC Berkeley](https://en.wikipedia.org/wiki/Physical_Intelligence_Inc.), it is the closest analog to Genesis in the foundation-model-for-robotics category.

**Rhoda AI** [announced a $450 million Series A](https://www.rhoda.ai/news/press-release) [at a $1.7 billion valuation in March 2026](https://siliconangle.com/2026/03/10/rhoda-ai-raises-450m-build-foundational-robotics-models-learn-internet-videos/) for its FutureVision platform, which uses video-predictive control rather than teleoperation. The approach is complementary — different data strategy, similar end goal.

**Figure AI** and **1X** are building toward general-purpose humanoids with their own model stacks. **Tesla Optimus** brings manufacturing scale to the question. **Boston Dynamics** continues operating in the professional and inspection market.

What differentiates Genesis is the hardware-data flywheel: the glove creates proprietary training data that cannot be replicated by competitors without the same hardware design, and the design itself reflects the embodiment of the robot being trained. That flywheel is defensible in a way that a pure software foundation model approach may not be.

The risk is that it is also expensive to scale. Custom robotic hands with tactile-sensing skin, [manufactured in partnership with Chinese firm Wuji Tech](https://techcrunch.com/2026/05/06/khosla-backed-robotics-startup-genesis-ai-has-gone-full-stack-demo-shows/), are not an off-the-shelf commodity. The 100x cost reduction claimed versus traditional teleoperation is relative to an expensive baseline.

---

## The Co-Founder Profile

CEO [Zhou Xian holds a PhD in robotics from Carnegie Mellon University](https://www.zhou-xian.com/), advised by Katerina Fragkiadaki, and focused on physical manipulation. CMU's robotics program has produced a significant share of the field's foundational researchers and most impactful startups.

President [Théophile Gervet is a former research scientist at Mistral AI](https://theophilegervet.github.io/), the French frontier model lab. His presence grounds Genesis's AI-first approach — the company is not simply hardware-plus-some-control-code but a team that understands how to build and train foundation models.

That combination — CMU robotics depth plus frontier model engineering experience — is unusual. Most robotics startups are heavy on one side or the other.

---

## What to Watch

Genesis says GENE-26.5 is the beginning of a model iteration cycle, with the name directly encoding the release date. The question is whether the model improves on the cadence frontier language models have normalized — quarterly or faster — or whether embodied AI remains slower-moving due to the physical cost of data collection.

The company also [announced it will unveil its first general-purpose robot as "the ultimate culmination of the technology unveiled today"](https://www.genesis.ai/press/press-release-gene-265). That announcement has no timeline attached, but it suggests Genesis is building toward a humanoid or near-humanoid product rather than positioning purely as a model provider to other hardware makers.

The harder question is whether human-level manipulation at the task level translates to robot-level reliability in uncontrolled environments. Lab demonstrations and kitchen demos are controlled. The real test is deployment at customer sites with unfamiliar equipment, variable surfaces, and objects that do not behave like they did in training. That gap between demonstration and deployment is where most robotics startups have historically struggled.

But the embodiment gap is real, the data problem is real, and the 1:1:1 mapping approach is a plausible structural solution. Eric Schmidt does not invest in robotics startups casually.

**ChatForest verdict:** Watch closely. The data flywheel advantage is real if the cost structure scales. The competition from PI0 and Rhoda AI is fierce. GENE-26.5 demos are impressive; reliability in production is the question that matters.

---

*Genesis AI is a private company. The $105M seed round was led by Eclipse and Khosla Ventures. GENE-26.5 was released on May 6, 2026.*

---

## Sources

- [Khosla-backed robotics startup Genesis AI has gone full stack, demo shows — TechCrunch](https://techcrunch.com/2026/05/06/khosla-backed-robotics-startup-genesis-ai-has-gone-full-stack-demo-shows/)
- [Genesis AI launches with $105M seed funding from Eclipse, Khosla to build AI models for robots — TechCrunch](https://techcrunch.com/2025/07/01/genesis-ai-launches-with-105m-seed-funding-from-eclipse-khosla-to-build-ai-models-for-robots/)
- [Genesis AI Unveils GENE-26.5 — PR Newswire](https://www.prnewswire.com/news-releases/genesis-ai-unveils-gene-26-5--the-first-ai-brain-to-enable-robots-with-human-level-physical-manipulation-capabilities-302763638.html)
- [Press Release: GENE-26.5 — Genesis AI (company's own site)](https://www.genesis.ai/press/press-release-gene-265)
- [Genesis AI emerges from stealth with $105M seed funding — Tech Funding News](https://techfundingnews.com/genesis-ai-105m-seed-funding/)
- [Genesis AI Launches Foundation Model Capable of Controlling Human-Like Robotic Hands — Technology.org](https://www.technology.org/2026/05/07/genesis-ai-launches-foundation-model-capable-of-controlling-human-like-robotic-hands/)
- [Theophile Gervet's own announcement of the $105M round, tagging investors — X](https://x.com/theo_gervet/status/1940059109224542363)
- [Genesis AI introduces GENE-26.5 robotic manipulation system — The Robot Report](https://www.therobotreport.com/genesis-ai-introduces-gene-foundation-model-more-dexterous-manipulation/)
- [Daniela Rus named CSAIL director — MIT News](https://news.mit.edu/newsoffice/2012/rus-named-csail-director-0522.html)
- [Vladlen Koltun — Wikipedia](https://en.wikipedia.org/wiki/Vladlen_Koltun)
- [Zhou Xian's personal site (PhD, CMU background)](https://www.zhou-xian.com/)
- [Theophile Gervet's personal site (Mistral AI background)](https://theophilegervet.github.io/)
- [AlphaGo — Google DeepMind](https://deepmind.google/research/alphago/)
- [How Google AI improved breast cancer detection in the UK — Google Blog](https://blog.google/innovation-and-ai/technology/health/google-ai-breast-cancer-detection/)
- [Jeff Bezos and OpenAI invest in robot startup Physical Intelligence at $2.4 billion valuation — CNBC](https://www.cnbc.com/2024/11/04/jeff-bezos-and-openai-invest-in-robot-startup-physical-intelligence.html)
- [Robotics AI startup Physical Intelligence raises $400M, now at $2.4 billion valuation — Tech Startups](https://techstartups.com/2024/11/05/robotics-ai-startup-physical-intelligence-raises-400m-funding-from-jeff-bezos-and-openai-now-at-2-4-billion-valuation/)
- [Physical Intelligence Inc. — Wikipedia](https://en.wikipedia.org/wiki/Physical_Intelligence_Inc.)
- [Press Release: $450M Series A — Rhoda AI (company's own site)](https://www.rhoda.ai/news/press-release)
- [Rhoda AI raises $450M to build foundational robotics models, $1.7B valuation — SiliconANGLE](https://siliconangle.com/2026/03/10/rhoda-ai-raises-450m-build-foundational-robotics-models-learn-internet-videos/)

