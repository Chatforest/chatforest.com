# Anthropic Stopped Selling APIs. It's Building Software Now.

> In three weeks, Anthropic shipped four vertical product bundles — Creative tools, Legal, Small Business, and Marketing Ops — all wired together via MCP connectors. This is not a model story. It is a platform strategy, and MCP is what makes it scale.


Anthropic's public identity has always been: safety-focused research lab that happens to offer a very good model API. That identity is becoming inaccurate.

In the space of three weeks — April 28 through May 18, 2026 — Anthropic shipped four vertical product bundles, each targeting a specific professional context, each wired into the tools professionals already use, and each built on the same underlying platform: Claude Cowork.

The four launches, in order:

- **April 28**: Creative tools — 9 MCP connectors (Blender, Adobe Creative Cloud, Autodesk Fusion, Ableton, Splice, Affinity by Canva, SketchUp, Resolume ×2)
- **May 12**: Claude for Legal — 20+ MCP connectors + 12 practice-area plugins
- **May 13**: Claude for Small Business — 15 ready-to-run workflows, 15 skills, 10+ connectors
- **May 18**: Claude Cowork for Marketing Ops — 5 deep workflow bundles

This is not API evolution. This is Anthropic entering the vertical software business. MCP is the integration layer that makes it possible — and the strategic choice that will define whether Anthropic wins or loses this bet.

## The Platform Underneath

Claude Cowork launched in January 2026 — relatively quietly, framed as a productivity tool. It can carry out multistep tasks spanning multiple applications and repeat those tasks at user-defined intervals. Users initiate each workflow and sign off before anything is sent, posted, or paid. It is available at no extra cost to Pro, Max, and Teams subscribers.

That January launch was foundation-laying. The vertical bundles started shipping in April.

The analogy that leaked out of Anthropic communications is telling: they are treating Cowork the way Microsoft treats Office — a platform first, then verticals stacked on top. The Creative connector pack was the proof of concept. Legal, Small Business, and Marketing Ops followed within 25 days.

## How the Verticals Differ

The four bundles are not the same product with different labels. Anthropic made deliberate choices about depth vs. breadth in each one.

**Creative tools** is the thinnest — nine connectors that hook Claude into professional software, giving it access to Blender's scene graph, Adobe Creative Cloud's 50+ tools, Autodesk Fusion's geometry API, Ableton's documentation layer. The connectors expose existing APIs; Claude brings reasoning on top. Anthropic also became a Blender Development Fund patron alongside this launch, signaling something beyond a checkbox integration.

**Claude for Legal** is the densest. Twenty-plus MCP connectors touch virtually every segment of the legal technology stack: document management (iManage, NetDocuments), contracts (Ironclad, DocuSign, Definely), e-discovery (Relativity, Everlaw, Consilio), deal infrastructure (Datasite, Box), legal research (Thomson Reuters Westlaw + CoCounsel + Practical Law, Harvey, Midpage, Trellis, Legal Data Hunter). The iManage connector gives Claude access to matter-centric document organization, version history, and workspace navigation. The Relativity connector exposes document review queues, search, and production workflows. These are not shallow read-only integrations.

The 12 practice-area plugins cut across corporate, litigation, privacy, IP, and more — pre-configured context that tells Claude what matters in each domain without requiring a lawyer to prompt-engineer it. Thomson Reuters and Free Law Project both shipped MCP integrations on or around the launch date, suggesting Anthropic coordinated the vendor ecosystem rather than wiring connectors unilaterally.

**Small Business** went wide: 15 workflows across finance, operations, sales, marketing, HR, and customer service, plus 10+ connectors to the tools small businesses already run (QuickBooks, PayPal, HubSpot, Canva, DocuSign, Google Workspace, Microsoft 365). The pitch is horizontal depth for users who handle all business functions themselves rather than specialists in one domain.

**Marketing Ops** went narrow by design: five workflows, not fifteen. Anthropic's stated reason is that marketing ops teams want depth on weekly tasks, not breadth on quarterly ones. This suggests Anthropic is learning from the Small Business launch — more is not always better; the right amount of pre-packaged workflow is what reduces friction for each specific user.

## MCP as Connective Tissue

What makes this strategy coherent is the choice to build on MCP rather than proprietary integration.

Prior to MCP, building AI integrations into professional software required custom API wrappers, separate authentication flows, and bespoke context-passing. Every integration was a one-off engineering project. MCP standardized the protocol: a tool vendor builds one MCP server, and any MCP-compatible client can connect to it.

Anthropic's first-party connectors benefit from this in two directions. Toward tool vendors: Relativity, iManage, and Thomson Reuters can maintain one MCP server that serves multiple AI clients, not just Claude. Toward users: a connector that works in Claude Cowork works (in principle) in any MCP-compatible agent runtime. Anthropic is not trying to lock the ecosystem; they are trying to lead it.

The trade-off is that the same connectors can be wired to competing models. Harvey, which connects to Claude via the Legal bundle, also has its own AI and its own model relationships. The Legal Data Hunter corpus with 31 million documents from 160-plus jurisdictions will not be exclusive to Anthropic. Openness is the bet, not exclusivity.

What Anthropic controls is the quality of the first-party integration, the depth of practice-area plugins, and the platform experience. The iManage connector is not just a read operation — it understands matter structure, version history, and workspace navigation. That kind of depth takes deliberate work with the tool vendor. First-party connectors built through partnership are likely to be more capable than connectors built by scraping public APIs.

## The Competitive Frame

The obvious competitor is Microsoft Copilot, which has been wiring AI into Microsoft 365 and associated enterprise software since 2023. Copilot's advantage is distribution — M365 is already in the enterprise, and Copilot extends it. Copilot's disadvantage is that it is implicitly tied to Microsoft's ecosystem: the connectors tend to start and end with Microsoft products.

Anthropic's connector strategy targets the non-Microsoft tools. Legal work happens in iManage and Relativity, not SharePoint and Teams. Design work happens in Blender and Adobe, not Visio. Marketing Ops runs on HubSpot and Canva, not Microsoft Publisher. This is a flanking move, not a frontal assault.

Google's Workspace AI is the other natural comparator — but Google's AI integrations are primarily within Google's own properties, with third-party connectors lagging. Anthropic's Legal bundle shipped with more third-party depth than any comparable product from Google or Microsoft.

Salesforce's Agentforce is a closer parallel: a workflow platform targeting specific professional use cases (sales, service, commerce) with deep integration into the Salesforce data stack. The difference is that Agentforce is deeply tied to Salesforce data; Anthropic's connectors are protocol-based and theoretically model-agnostic. Agentforce is building a walled garden; Anthropic is building on an open protocol while trying to be the preferred tenant.

## What Is Still Missing

The connector ecosystem is not uniform. Marketing Ops ships without a native Salesforce Sales or HubSpot Sales connector (HubSpot Marketing yes, Sales no). The Creative bundle's Ableton integration is documentation-grounded, not session-aware — Claude can answer questions about Live and Push, but it cannot manipulate a session directly. Some connectors read; fewer write with depth.

The workflow design also assumes that each vertical has homogeneous needs. Large law firms doing M&A due diligence use the same Legal bundle as solo practitioners doing estate planning. In practice, the 12 practice-area plugins partially address this — but the bundles are still broad-strokes, not firm-specific.

Pricing for enterprise-grade use at scale is unclear. Pro/Max/Teams subscribers get the workflows at no extra cost, but volume and compliance requirements for a 500-lawyer firm running Claude inside Relativity at scale will need an Enterprise conversation. Anthropic has not published that pricing.

Financial Services is expected next, based on Anthropic's public commentary about the Anthropic Economic Index. Finance is a harder target: heavier compliance requirements, longer procurement cycles, more entrenched legacy systems. The Legal launch is a useful template — connector depth matters more than breadth, and coordinating with ecosystem vendors before launch (Thomson Reuters, Free Law Project) signals readiness.

## The Builder's Takeaway

If you are building on Claude's API today, this strategy has direct implications.

The verticals Anthropic ships are not all the verticals. Healthcare, financial services, architecture, scientific research, manufacturing, education — none have first-party bundles yet. MCP is the protocol you should be building your tool integration on, because first-party connectors from whoever ships them first will have an advantage in trust, depth, and discoverability from within Claude.

The practice-area plugin model is worth studying. Pre-configured context that orients a general model toward a specific professional domain — without requiring end users to write system prompts — is a meaningful product layer. The same concept applies outside legal: a medical billing plugin that knows CPT codes, payer rules, and documentation requirements is more useful than a generic AI that can be prompted to think about medical billing.

The approval-gate workflow design (user initiates, user signs off before anything is sent, posted, or paid) is becoming a standard trust pattern for agentic products. It threads the needle between "AI does nothing" and "AI does everything without oversight." The specific design — Claude proposes, human approves, then Claude executes — matches the comfort level of most professionals who are not yet ready to give AI autonomous execution authority.

Three weeks. Four verticals. The same platform underneath all of them. Anthropic's API identity is not gone — the API business is funding all of this. But the product identity is shifting, and the direction is clear: Claude is becoming the AI layer inside the software stacks where work actually happens, not the chat interface in front of them.

Financial Services is probably next. Watch which tool vendors ship MCP servers in the weeks before the announcement.

