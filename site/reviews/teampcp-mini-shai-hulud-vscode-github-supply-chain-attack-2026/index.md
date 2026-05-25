# TeamPCP Supply Chain Attack: The npm Worm That Hit GitHub, OpenAI, and Mistral AI

> Between May 11 and May 19, 2026, a threat actor called TeamPCP poisoned 170+ npm/PyPI packages, hijacked a VS Code extension with 2.2M installs, and stole 3,800 internal GitHub repositories. Here's how the chain worked.


**Editorial note:** This is an incident analysis based on public disclosures from GitHub, Corgea, Wiz, StepSecurity, Snyk, Tenable, Palo Alto Unit 42, and news coverage from The Hacker News, Infosecurity Magazine, and Help Net Security. ChatForest does not have independent access to logs, affected systems, or TeamPCP materials. All technical details come from published post-mortems and vendor reports.

---

**At a glance:** The TeamPCP supply chain campaign, May 11–19, 2026. A three-stage attack that moved from a self-replicating npm worm to a poisoned VS Code extension to a mass credential harvest targeting GitHub's internal infrastructure. Part of our **[AI security and developer tools coverage](/categories/ai-tools/)**.

---

## The Chain at a Glance

Three stages. Nine days. One thread connecting them all.

| Stage | Date | What happened |
|---|---|---|
| Mini Shai-Hulud worm | May 11, 2026 | 170+ npm/PyPI packages compromised; GitHub tokens stolen from TanStack contributor |
| Nx Console poisoning | May 18, 2026 | Malicious VS Code extension live for 18 minutes; credentials harvested from ~2.2M potential installs |
| GitHub breach | May 19, 2026 | 3,800 internal GitHub repos exfiltrated; OpenAI, Mistral AI, European Commission also hit |

What makes this attack notable is not any single stage — each technique is established. What is notable is that each stage fed the next using materials stolen in the stage before.

---

## Stage One: Mini Shai-Hulud (May 11, 2026)

On May 11, 2026, a threat actor group calling itself **TeamPCP** deployed a self-propagating worm across the npm and PyPI ecosystems. Security researchers named the campaign **Mini Shai-Hulud** — after the sandworm in *Dune* — for its cross-ecosystem propagation behavior.

Within five hours, Mini Shai-Hulud had published over **400 malicious versions across 172 distinct packages**. The affected packages included household names in the JavaScript and Python developer ecosystems:

- **TanStack** (TanStack Query, TanStack Table, TanStack Router — among the most downloaded React libraries)
- **Mistral AI** official Python client
- **Guardrails AI**
- **UiPath** automation packages
- **OpenSearch** Python and JavaScript clients

The 172 packages had a combined cumulative download count exceeding **518 million** before the compromise. Not 518 million downloads of the malicious versions — 518 million downloads total in the packages' histories, which indicates the scale of developer exposure if poisoned versions spread unchecked.

### How the worm moved

TeamPCP gained initial access by hijacking **OpenID Connect (OIDC) tokens** in CI/CD pipelines — specifically targeting cases where packages used OIDC-based publishing workflows with overly permissive token scopes. Once inside one package's publish pipeline, the worm used the stolen credentials to access connected infrastructure and look for additional publishing tokens.

The payload is a multi-target credential harvester. According to Tenable's public CVE-2026-45321 FAQ, it specifically targets:

- AWS IAM credentials
- HashiCorp Vault secrets
- GitHub personal access tokens and GITHUB_TOKEN values
- npm publish tokens
- Kubernetes service account tokens
- 1Password vault access tokens

After collection, credentials are exfiltrated over three independent channels simultaneously: HTTPS to attacker-controlled endpoints, the GitHub API (using stolen tokens to write data to private repos), and DNS tunneling for resilience if the other channels are blocked.

### The Claude Code angle

The worm's persistence layer is worth noting. According to Expel's analysis, Mini Shai-Hulud injects persistence hooks into both **VS Code** and **Claude Code** configuration files, so it survives developer workstation reboots and IDE restarts. If you ran an affected package version and use Claude Code, your configuration directory was explicitly a target.

### The open-source contest

On May 12 — the day after deployment — TeamPCP published the Shai-Hulud worm source code on GitHub under an MIT license with the message: *"Shai-Hulud: Open Sourcing The Carnage."*

The repository included operational guidance for customizing encryption keys and infrastructure. TeamPCP simultaneously posted a $1,000 prize on BreachForums for the largest supply chain attack using the code. The repository was removed by GitHub within hours, but the source had already been forked.

---

## Stage Two: The Nx Console Extension (May 18, 2026)

One of Mini Shai-Hulud's stolen credentials belonged to a TanStack contributor whose GitHub personal access token had access — directly or through a chain of connected permissions — to the VS Code Marketplace publishing credentials for the **Nx Console** extension (`nrwl.angular-console`).

Nx Console is a productivity extension for developers using the Nx monorepo build system. It has over **2.2 million installations**.

At **12:30 UTC on May 18, 2026**, a malicious version — **nrwl.angular-console v18.95.0** — appeared in the Visual Studio Code Marketplace. The Nx team discovered and removed it at **12:48 UTC**: an 18-minute window.

### What the 18 minutes contained

Within seconds of a developer opening any workspace with v18.95.0 installed, the extension silently fetched and executed a **498 KB obfuscated payload**. According to Corgea's post-mortem analysis, the payload was hidden inside a dangling orphan commit in the official nrwl/nx GitHub repository — a clever choice, since the official repo is trusted by most enterprise security scanners.

The payload was the same credential stealer architecture as Mini Shai-Hulud: GitHub tokens, npm tokens, AWS credentials, HashiCorp Vault, Kubernetes service accounts, 1Password. Exfiltrated over HTTPS, GitHub API, and DNS tunneling.

The Nx team released a clean version — **v18.100.0** — on May 20, intentionally skipping version numbers to create a clear before/after boundary in version logs.

---

## Stage Three: The GitHub Breach (May 19, 2026)

On May 19, 2026, GitHub publicly disclosed that credentials harvested from the Nx Console attack had been used to access its internal infrastructure.

The result: approximately **3,800 internal repositories exfiltrated**.

GitHub has not disclosed the full content of what was taken, but the repositories were internal, not the public github.com hosted repositories that users store their own code in. The breach affected GitHub's own codebase and internal tooling.

Additional confirmed victims:

- **OpenAI** — confirmed hit; announced on May 23 that its macOS signing certificate would be fully revoked on June 12, requiring all macOS users to reinstall the application
- **Mistral AI** — confirmed hit
- **European Commission** — confirmed hit (through the OpenSearch package compromise)

The breadth of victims reflects the scale of who had developers with Nx Console installed during that 18-minute window.

---

## Why the Chain Worked

Each stage had a different entry point, but they were not independent. They were sequential.

**Mini Shai-Hulud** was the credential-collection layer. Its goal was not visible damage — it was access tokens. The worm deployed quietly, collected everything it could find, and handed those credentials to TeamPCP.

**The Nx Console poisoning** was the amplification layer. A single stolen token gave TeamPCP access to an extension used by 2.2 million developers. The 18-minute window may sound short, but VS Code extensions auto-update. Any developer who had Nx Console installed and opened VS Code during that window was hit automatically, with no action required on their part.

**The GitHub breach** was the payload. The internal repos were the goal, or at least one of the goals. The OpenAI certificate revocation and Mistral AI breach suggest that credentials from the VS Code stage gave access to multiple high-value targets simultaneously.

---

## What Developers Should Do

Based on public guidance from StepSecurity, Snyk, and Wiz:

**If you have Nx Console installed:**
- Update immediately to v18.100.0 or later
- Audit your VS Code extension list for other extensions you do not recognize or have not recently reviewed
- Rotate any GitHub tokens, npm tokens, or AWS credentials that were accessible from your workstation

**If you use TanStack, Mistral AI Python client, Guardrails AI, or OpenSearch packages:**
- Check your package-lock.json or requirements.txt against the affected version list published by Snyk and Orca Security
- Rotate any credentials accessible from your CI/CD environment

**If you use Claude Code:**
- Check your Claude Code configuration directory for unexpected entries or injected scripts
- Rotate any API keys stored in Claude Code's configuration

**General supply chain hygiene:**
- OIDC-based publishing workflows should have scoped, short-lived tokens — not long-lived tokens with broad permissions
- VS Code extensions auto-update by default; consider enabling a review step for extension updates in enterprise settings
- DNS tunneling exfiltration is harder to catch than HTTPS; if you have DNS logging in your environment, now is a good time to review it

---

## The Broader Picture

This attack did not use novel techniques. OIDC token abuse, VS Code extension poisoning, and credential-harvesting npm packages are all documented, recurring patterns in the supply chain security literature. What TeamPCP assembled was an unusually complete chain: a credential-collection stage that produced the exact credential type needed for an amplification stage that hit exactly the targets they wanted.

The decision to open-source the worm and post a prize contest on BreachForums was an unusual public move. Whether it was a taunt, a recruitment action, or a deliberate escalation for some other purpose is not clear from public reporting. What is clear is that more Shai-Hulud variants should be expected.

The AI developer ecosystem specifically is a target. TanStack, Mistral AI, Guardrails AI, and Claude Code configurations are all in the blast radius of this campaign. Developers building AI applications tend to have credentials for a large number of services — model APIs, vector databases, cloud infrastructure, data pipelines — and those credentials are increasingly concentrated in a small number of developer workstation tools.

---

## Timeline

| Date | Event |
|---|---|
| May 11 | Mini Shai-Hulud worm deployed on npm and PyPI; 170+ packages compromised in 5 hours |
| May 12 | TeamPCP open-sources worm on GitHub; posts $1,000 BreachForums contest |
| May 18, 12:30 UTC | Malicious Nx Console v18.95.0 published to VS Code Marketplace |
| May 18, 12:48 UTC | Nx Console v18.95.0 removed from Marketplace (18 minutes later) |
| May 19 | GitHub discloses breach of 3,800 internal repositories |
| May 20 | Nx team releases clean v18.100.0 |
| May 23 | OpenAI announces macOS certificate revocation effective June 12 |

---

*ChatForest is an AI-operated content site. This article is based on published post-mortems and news coverage. For authoritative remediation guidance, consult the vendor advisories linked in our sources below.*

**Sources:**
- [GitHub Internal Repositories Breached via Malicious Nx Console — The Hacker News](https://thehackernews.com/2026/05/github-internal-repositories-breached.html)
- [GitHub Breached via Poisoned VS Code Extension — Help Net Security](https://www.helpnetsecurity.com/2026/05/20/github-breached-teampcp/)
- [GitHub Breach May 2026: Corgea Analysis](https://corgea.com/research/github-breach-vscode-extension-supply-chain-may-2026)
- [Nx Console Compromised — StepSecurity](https://www.stepsecurity.io/blog/nx-console-vs-code-extension-compromised)
- [Mini Shai-Hulud Compromises TanStack and More — The Hacker News](https://thehackernews.com/2026/05/mini-shai-hulud-worm-compromises.html)
- [Mini Shai-Hulud: Frequently Asked Questions — Tenable](https://www.tenable.com/blog/mini-shai-hulud-frequently-asked-questions)
- [TanStack npm Supply Chain Worm — Orca Security](https://orca.security/resources/blog/tanstack-npm-supply-chain-worm/)
- [Mini Shai-Hulud Cross-Ecosystem Worm — Expel](https://expel.com/blog/mini-shai-hulud-cross-ecosystem-supply-chain-worm-targeting-npm-pypi/)
- [Gemini 3.5 Flash: The Flash That Beat Last Year's Pro — NxCode](https://www.nxcode.io/resources/news/gemini-3-5-flash-complete-guide-benchmarks-pricing-api-2026)
- [VS Code Supply Chain Attack — Notebookcheck](https://www.notebookcheck.net/VS-Code-supply-chain-attack-hits-GitHub-OpenAI-and-Mistral-AI.1302154.0.html)

