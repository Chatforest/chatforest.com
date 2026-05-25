# AlphaGo's Creator Raised $1.1 Billion on One Idea: AI That Doesn't Learn From Humans Will Beat AI That Does

> David Silver — the researcher who taught AlphaGo to beat the world's best Go player without human examples — left DeepMind to build Ineffable Intelligence, a London lab with $1.1 billion in seed funding and a single thesis: reinforcement learning, not human data, is the path to superintelligence.


**At a glance:** Ineffable Intelligence. Founded November 2025, London, UK. Founder and Director: David Silver — UCL Professor, former lead of Google DeepMind's reinforcement learning team, creator of AlphaGo, AlphaZero, and MuZero. Funding: $1.1 billion seed round at $5.1 billion valuation, announced April 27, 2026 — the largest seed round in European history. Co-led by Sequoia Capital and Lightspeed Venture Partners, with participation from Nvidia, Google, DST Global, Index Ventures, and the UK Sovereign AI Fund. Mission: build a "superlearner" — an AI system that discovers all knowledge from its own experience, without relying on human-generated data. Nvidia partnership announced May 13, 2026 to co-design reinforcement learning infrastructure at scale. Part of our **[AI Models & Companies reviews](/categories/ai-tools/)**.

---

In March 2016, a Google DeepMind program called AlphaGo played five games of Go against Lee Sedol, widely regarded as the world's best player, and won four of them. It was a watershed moment — Go had long been considered too complex, too intuitive, too human for computers to master at a world-class level. The AI community expected parity with top professionals would be years away, if it came at all.

The researcher who led AlphaGo's development was David Silver.

What made AlphaGo striking wasn't just that it won. It was *how* it learned. AlphaGo was seeded with a large library of human Go games — thousands of games played by professionals, used to give the system a foundation before it refined itself further through self-play. Human knowledge, human games, human strategy patterns: the system started by absorbing what humans knew.

Silver and his team thought they could go further. A year later, they released AlphaZero — a version trained with no human data at all. AlphaZero started knowing only the rules of the game. It learned chess, shogi, and Go from scratch, by playing itself millions of times, refining through feedback alone. It became the strongest player in the history of each game, surpassing every engine trained on human games. The humans had been, in a sense, holding it back.

Now Silver is betting that this idea — AI that learns through experience rather than imitation — scales all the way to superintelligence. In November 2025, he founded Ineffable Intelligence in London. In January 2026, he left DeepMind to run it full-time. In April 2026, he raised $1.1 billion at a $5.1 billion valuation to try.

---

## The Thesis Behind the Name

Ineffable means something beyond language — something that cannot be expressed in words. The name is a signal.

Current AI systems, including the large language models that power ChatGPT, Claude, Gemini, and every major AI product today, learn from human language. They absorb text — articles, books, code, conversations, research papers — and learn to generate language that resembles what humans produce. They are, at their core, sophisticated pattern-matchers for human communication.

Silver's thesis, which he has developed over years of research culminating in a 2021 paper with colleagues titled "Reward Is Enough," is that this approach has a ceiling. A language model can only be as good as the human-generated data it trains on. It can synthesize, interpolate, and recombine what humans have expressed, but it is bounded by what humans have found worth expressing. If there are insights beyond human current understanding — mathematical structures nobody has discovered, scientific hypotheses nobody has articulated, engineering solutions nobody has conceived — a language model cannot find them, because they are not in its training data.

A reinforcement learning system isn't bound by that ceiling. It doesn't start from a library of examples. It starts from a set of goals and a way to measure whether it's achieving them. It explores, acts, observes the consequences, and updates based on what worked. AlphaZero discovered chess strategies that human grandmasters had never seen — not because human grandmasters hadn't thought hard about chess, but because centuries of human chess study had inadvertently narrowed what people considered worth trying. AlphaZero had no such prior.

Ineffable Intelligence wants to apply this approach to intelligence in general — not constrained to games with clean rules and clear win conditions, but extended to open-ended reasoning, scientific discovery, and what Silver calls "elementary motor skills through to profound intellectual breakthroughs."

---

## What a Superlearner Is

Silver uses the term "superlearner" to describe the system Ineffable is building. The concept is more specific than it sounds.

A superlearner is an agent that learns continuously from experience. It acts in an environment, observes the outcome, receives some signal about whether that outcome was good or bad, and updates its behavior accordingly. Over enough iterations, across enough diverse environments, it develops general capabilities — not because it was shown what general capability looks like, but because the reward signal keeps pushing it to find better strategies.

The technical ambition is significant. Reinforcement learning works extraordinarily well in narrow, well-defined domains — games, simulations, robotics tasks with clear success criteria. The history of RL in more open-ended domains is messier. Defining appropriate reward signals for general intelligence is unsolved. Learning efficiently across many different types of environments simultaneously is unsolved. Scaling RL to the compute and data volumes that language models operate at is a deeply active research area.

Ineffable's position is that all of these problems are tractable, and that solving them is the path to superintelligence. The company describes its system as aiming to "rediscover and then transcend the greatest inventions in human history: language, science, mathematics and technology" — the implication being that a system learning from raw experience will eventually re-derive human knowledge from first principles, then go further.

Silver has stated the company's mission bluntly: "make first contact with superintelligence."

---

## The Funding and Who's Behind It

The $1.1 billion seed round is not just a large number — it is the largest seed round in European history, by a wide margin. It values a company with no products and no revenue at $5.1 billion. The investors writing those checks are not gamblers; they are among the most sophisticated capital allocators in technology. Their participation is itself a signal worth examining.

Sequoia Capital and Lightspeed Venture Partners co-led the round. Both firms have decades of experience funding frontier technology companies and have seen enough large research bets to know the difference between credible science and expensive dreams.

Nvidia participated as an investor and has since gone further. In May 2026, Nvidia and Ineffable Intelligence announced a formal technical partnership — not just a capital relationship but an active collaboration on the hardware and software infrastructure RL systems will need to run at scale. Jensen Huang, Nvidia's CEO, said at the announcement: "The next frontier of AI is superlearners — systems that learn continuously from experience." The initial work runs on Nvidia's Grace Blackwell platform and is expected to extend to the upcoming Vera Rubin architecture, which Nvidia is positioning for the next generation of AI training workloads.

Google is also a participating investor — notable given that David Silver built his career at Google DeepMind and that Google's own AI efforts are deeply invested in the current LLM paradigm. That Google would fund a competitor with a contrarian thesis suggests either that they are hedging, or that people inside Google who understood what Silver was working on found his thesis credible enough to back.

The UK Sovereign AI Fund participated through the British Business Bank, representing the UK government's explicit interest in anchoring a frontier AI lab in London.

DST Global and Index Ventures round out the investor list.

---

## Why This Thesis Has Prior Art

The argument for Ineffable Intelligence isn't purely theoretical. Silver has demonstrated it twice at scale.

AlphaGo showed that RL-based systems could reach superhuman performance in Go. AlphaZero showed that removing human data improved rather than hurt performance. MuZero went further still, learning to play games from scratch without even being told the rules — the system inferred the structure of the game from its own observations. In each iteration, reducing reliance on human knowledge improved the system.

The pattern suggests something real: in domains where the environment provides clear feedback, RL systems trained without human data can find solutions that human-informed systems miss. The open question is whether that pattern generalizes outside of games.

Silver's 2021 "Reward Is Enough" paper argued that it does — that a sufficiently general reward signal, combined with powerful enough optimization, produces general intelligence as a byproduct of solving problems well. The paper was theoretical; Ineffable Intelligence is the empirical test.

---

## The Honest Obstacles

Writing about Ineffable Intelligence without noting the difficulties in its path would be incomplete.

**The reward problem.** In chess, the reward is clear: win. In the real world, reward signals are hard to specify. What is the reward for "scientific discovery"? For "intellectual breakthrough"? Specifying what you want precisely enough for an RL system to optimize it, without inadvertently specifying something subtly different that the system optimizes to a perverse extreme, is one of the hard unsolved problems in AI alignment. Ineffable hasn't published a solution, because it almost certainly doesn't have one yet.

**The environmental breadth problem.** AlphaZero's environments were perfectly simulated — chess and Go are complete, deterministic systems. The real world is not. Building environments rich and realistic enough for a superlearner to acquire general capabilities is a substantial research and engineering challenge that is separate from the RL algorithm itself.

**The timeline question.** Silver's previous breakthroughs — AlphaGo in 2016, AlphaZero in 2017, MuZero in 2019 — each took years of sustained work by large teams with enormous compute. Ineffable Intelligence was founded six months ago. "Making first contact with superintelligence" is a mission statement, not a roadmap. The research is real; the timeline is not.

**The LLM is not obviously wrong.** The claim that LLMs hit a ceiling depends on what that ceiling is and when it becomes relevant. Current LLMs are already highly capable and improving rapidly. The argument that they'll eventually plateau because they're bounded by human knowledge is theoretically coherent but empirically unproven. It's possible that by the time RL systems can match LLMs in breadth of capability, LLMs will have solved the underlying problems with other techniques.

None of these objections refute Silver's thesis. They complicate it.

---

## What Ineffable's $1.1 Billion Buys

At this stage, the money buys research time and compute. Ineffable is not building a product — it is building a scientific program. The Nvidia partnership gives it access to cutting-edge accelerated computing infrastructure specifically co-designed for the RL training workloads Silver's team needs: tight act-observe-score-update loops running at scale, with memory bandwidth and interconnect profiles very different from the pretraining pipelines that produced GPT-4 or Claude.

The UK location matters too. London's deep talent pool in machine learning — partly built by DeepMind itself over the past decade — means Silver can recruit researchers without requiring them to move to San Francisco. DeepMind pioneered the idea of a world-class frontier AI lab outside the US; Ineffable is the next heir to that tradition.

---

## Why This Story Matters Beyond the Number

The $1.1 billion seed round will get the headline. The real story is the intellectual bet underneath it.

The current AI industry has converged on a single dominant paradigm: large language models trained on human-generated text, scaled up with more compute and more data, refined with human feedback. This approach has produced remarkable results. It has also produced intense competition, high compute costs, and increasing returns to scale — advantages that favor the largest companies with the deepest pockets.

Ineffable Intelligence's thesis is that the paradigm is wrong in a fundamental way — not wrong because it doesn't work, but wrong because it can't go all the way. If Silver is right, the path to the most capable AI systems doesn't run through better LLMs. It runs through systems that learn from experience the way AlphaZero learned Go: not by studying what humans have done, but by discovering what can be done.

That claim is radical enough that most of the AI industry would disagree with it, or at least hedge it. The investors who wrote $1.1 billion in checks for a six-month-old company disagree with the disagreement.

David Silver spent a decade proving that RL systems without human data could beat the best humans at games. He left one of the most prestigious AI research positions in the world to find out whether the same idea holds for intelligence itself.

The answer is not known. The experiment has started.

---

*ChatForest covers AI companies, tools, and trends. Research on Ineffable Intelligence conducted May 2026 from publicly available sources including TechCrunch, CNBC, EU-Startups, Sequoia Capital blog, NVIDIA blog, British Business Bank, and Pathfounders. This is an independent research-based review; ChatForest has no financial relationship with Ineffable Intelligence or its investors.*

