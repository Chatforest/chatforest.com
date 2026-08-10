# Best Security MCP Servers in 2026

> Code scanning, secret management, threat intelligence, network security, compliance, incident response, privacy & data protection, and supply chain protection — we've reviewed 100+ security MCP servers across 8 categories.


Security is where MCP servers have the highest stakes and the most vendor investment. Get it right and your AI agent catches vulnerabilities before they ship, enriches alerts with threat context, and manages secrets without copy-pasting tokens through chat. Get it wrong and you've given an LLM access to your pentest tools, your vault, or your SIEM with no guardrails.

We've published [8 in-depth security reviews](/reviews/) covering 100+ MCP servers across every security domain. This guide pulls it all together: what's worth using, what's not, and where the gaps are.

## The short version

| Category | Our pick | Rating | Runner-up |
|----------|----------|--------|-----------|
| Code scanning (SAST/SCA) | [Snyk MCP](/reviews/code-security-mcp-servers/) | 4/5 | [SonarQube](/reviews/code-security-mcp-servers/) (619 stars, code quality) |
| Secret management | [HashiCorp Vault MCP](/reviews/secret-management-mcp-servers/) | 4/5 | [Bitwarden](/reviews/secret-management-mcp-servers/) (225 stars, password vaults) |
| Threat intelligence | [Google Threat Intelligence](/reviews/threat-intelligence-mcp-servers/) | 4/5 | [CrowdStrike Falcon](/reviews/threat-intelligence-mcp-servers/) (232 stars, 25 modules) |
| Network security | [Burp Suite MCP](/reviews/network-security-mcp-servers/) | 3.5/5 | [mcp-security-hub](/reviews/network-security-mcp-servers/) (300+ tools) |
| Incident response (DFIR) | [CrowdStrike Falcon](/reviews/digital-forensics-incident-response-mcp-servers/) | 4/5 | [Google mcp-security](/reviews/digital-forensics-incident-response-mcp-servers/) (4 servers) |
| Compliance & audit | [Vanta MCP](/reviews/compliance-audit-automation-mcp-servers/) | 3.5/5 | [CISO Assistant](/reviews/compliance-audit-automation-mcp-servers/) (4,300 stars, open source) |
| Privacy & data protection | [BigID MCP](/reviews/privacy-data-protection-mcp-servers/) | 3/5 | [mcp-server-conceal](/reviews/privacy-data-protection-mcp-servers/) (Rust, pseudo-anonymization) |
| Supply chain security | [Snyk Agent Scan](/reviews/ai-agent-supply-chain-security-mcp-servers/) | 3.5/5 | [Docker MCP Gateway](/reviews/ai-agent-supply-chain-security-mcp-servers/) (1,500 stars, isolation) |

## Why security MCP servers are different

Most MCP categories are about productivity — do things faster. Security MCP servers are about risk — and risk cuts both ways:

1. **They protect AI-generated code.** As agents write more code, catching vulnerabilities inline (before commit, not in CI) becomes critical. Snyk's MCP server scans code as the agent generates it.
2. **They create new attack surface.** An MCP server with access to your vault, your SIEM, or your network scanner is a high-value target. Tool poisoning, prompt injection, and excessive permissions are real threats — a small-scale 2026 test of [the 20 most popular MCP servers found 60% had at least one real security finding](https://dev.to/ecap0/we-scanned-20-top-mcp-servers-for-vulnerabilities-the-results-will-shock-you-21c5) using LLM-based scanning.
3. **They require authorization context.** Network scanning, pentesting, and threat hunting tools must only be used on systems you own or have explicit permission to test.

The ecosystem is responding. In January–February 2026 alone, [30+ CVEs were filed against MCP servers](https://robbyb910.substack.com/p/mcp-security-crisis-30-cves-in-60) according to independent CVE tracking. Earlier groundwork had been laid: [Snyk acquired Invariant Labs](https://snyk.io/news/snyk-acquires-invariant-labs-to-accelerate-agentic-ai-security-innovation/) (makers of mcp-scan) in June 2025, and [Docker acquired MCP Defender](https://www.docker.com/blog/docker-acquires-mcp-defender-ai-agent-security/) in September 2025. Cisco shipped a [multi-engine open-source MCP scanner](https://github.com/cisco-ai-defense/mcp-scanner). The meta-security layer — tools that secure the MCP ecosystem itself — is now a category of its own.

## Code Scanning — Catching Vulnerabilities at Generation Time

**[Full review: Code Security MCP Servers →](/reviews/code-security-mcp-servers/)** | Rating: 4/5

This is the most practically valuable security MCP category. When your AI agent generates code, these servers scan it for vulnerabilities before it ships.

### The winner: Snyk MCP

[snyk/studio-mcp](https://github.com/snyk/studio-mcp) — 54 stars, Go, Apache 2.0. **11 tools spanning five security domains**: SAST (source code), SCA (dependencies), IaC (infrastructure), container scanning, SBOM, and AI-BOM. No other single MCP server covers this breadth.

The AI-BOM tool is forward-looking — as agents pull in packages and models, tracking the AI supply chain matters. Integrates with Cursor, VS Code, Windsurf, Claude Desktop, GitHub Copilot.

### Strong alternatives

**SonarQube** ([SonarSource/sonarqube-mcp-server](https://github.com/SonarSource/sonarqube-mcp-server)) — 619 stars, the largest community in the category. Adds code quality (bugs, code smells, maintainability) alongside security vulnerabilities. If your team already uses SonarQube, this is the natural choice. Supports 11+ IDEs and editors including Claude Code, Cursor, VS Code, and Windsurf.

**Semgrep** — pioneered the category with 683 stars before [being archived into the main Semgrep CLI binary](https://github.com/semgrep/mcp) in October 2025. The scanning capability is still there — it now ships as `semgrep mcp` in the core Semgrep binary.

**Multi-tool aggregators** are emerging: [DevSecOps-MCP](https://github.com/jmstar85/DevSecOps-MCP) bundles Semgrep + Bandit (SAST), OWASP ZAP (DAST), and npm audit + OSV Scanner (SCA) into a single server; Checkov/IaC scanning is on its roadmap but not yet shipped. Early stage but promising for teams that want unified scanning without multiple vendor accounts.

## Secret Management — Credentials Without Copy-Paste

**[Full review: Secret Management MCP Servers →](/reviews/secret-management-mcp-servers/)** | Rating: 4/5

The problem: developers copy-paste API tokens, database passwords, and TLS certificates through chat windows. MCP servers for secret management let agents store, retrieve, rotate, and audit credentials properly.

### The winner: HashiCorp Vault MCP

[hashicorp/vault-mcp-server](https://github.com/hashicorp/vault-mcp-server) — 57 stars, Go, MPL-2.0, "intended for local use only" per its own docs (not yet GA). Tools span KV secret operations (CRUD), PKI certificate management (issuer/role management, certificate issuance), and mount management. Supports stdio and StreamableHTTP transports.

For enterprise teams already on Vault, this is the natural integration. The PKI tools are particularly valuable — generating TLS certificates on demand through an agent conversation instead of navigating the Vault UI.

### Strong alternatives

**Bitwarden** ([bitwarden/mcp-server](https://github.com/bitwarden/mcp-server)) — 225 stars, official, 40+ tools covering vault management and organization administration. The broadest password manager MCP integration.

**1Password** — community-built (no official server yet). [`op-mcp`](https://github.com/goodwokdev/op-mcp) offers 66 tools wrapping the 1Password CLI. High tool count but community-maintained.

**[Infisical](https://github.com/Infisical/infisical-mcp-server)** and **[Doppler](https://github.com/DopplerHQ/mcp-server)** both have official servers for their developer-focused secret management platforms.

**Cloud-native options**: AWS Secrets Manager, [Azure Key Vault](https://learn.microsoft.com/en-us/azure/developer/azure-mcp-server/services/azure-mcp-server-for-key-vault), and GCP Secret Manager are accessible through their respective platform MCP servers rather than dedicated secret management servers.

## Threat Intelligence — SOC Workflows via Natural Language

**[Full review: Threat Intelligence MCP Servers →](/reviews/threat-intelligence-mcp-servers/)** | Rating: 4/5

This is one of the strongest MCP categories in cybersecurity. Two major vendors — Google and CrowdStrike — ship official servers, and the community has built mature integrations for every significant open-source CTI platform.

### The winner: Google Threat Intelligence

[google/mcp-security](https://github.com/google/mcp-security) — 515 stars, Python, Apache-2.0. A mono-repo with five server modules: **Google Threat Intelligence** (GTI — the crown jewel for CTI analysts), **Chronicle SIEM**, **SOAR** (Security Orchestration, Automation and Response), **Security Command Center** (SCC), and a remote MCP option. This gives security teams a unified AI interface across Google's entire security stack.

### Strong alternatives

**CrowdStrike Falcon MCP** ([CrowdStrike/falcon-mcp](https://github.com/CrowdStrike/falcon-mcp)) — 232 stars, Python, MIT. **25 modules** covering detections, incidents, hosts, threat intel, IOC management, custom IOA rules, firewall policies, cloud security, vulnerability management, identity protection, and more. Essentially the entire Falcon platform accessible via natural language.

**Community CTI servers** fill important gaps:
- **[mcp-shodan](https://github.com/BurtTheCoder/mcp-shodan)** (150 stars) — IP, CVE, DNS lookups via Shodan
- **[mcp-virustotal](https://github.com/BurtTheCoder/mcp-virustotal)** (144 stars) — 11 tools with relationship queries
- **[OpenCTI MCP](https://github.com/Spathodea-Network/opencti-mcp)** (40 stars) — tools for STIX object search, user management, and system operations
- **[OSINT Tools MCP](https://github.com/frishtik/osint-tools-mcp-server)** (229 stars) — bundles Sherlock, Holehe, Maigret, TheHarvester, and SpiderFoot
- **[Mallory CTI](https://github.com/malloryai/mallory-mcp-server)** — the local server was archived June 2026; Mallory now runs threat-actor and CVE-trend lookups only via a hosted Remote MCP endpoint

**Multi-source aggregation** is emerging as a practical pattern: [FastMCP-ThreatIntel](https://github.com/4R9UN/fastmcp-threatintel) combines VirusTotal + OTX + AbuseIPDB + IPinfo in one server.

## Network Security — Scanning, Testing, and Reconnaissance

**[Full review: Network Security MCP Servers →](/reviews/network-security-mcp-servers/)** | Rating: 3.5/5

**Important**: every server in this category should be used only with proper authorization on systems you own or have explicit permission to test.

### The winner: Burp Suite MCP

[PortSwigger/mcp-server](https://github.com/PortSwigger/mcp-server) — 1,100 stars, the highest-credibility entry. Official vendor backing from the company behind the industry-standard web application security testing platform.

### Strong alternatives

**[FuzzingLabs mcp-security-hub](https://github.com/FuzzingLabs/mcp-security-hub)** — 758 stars, 300+ security tools bundled across dozens of Docker-isolated MCP servers, spanning Nmap, Ghidra, Nuclei, SQLMap, Hashcat, and more. The most comprehensive offensive security collection in a single project.

**[mcp-nettools](https://github.com/dkruyt/mcp-nettools)** (dkruyt) — 11 tools for everyday network diagnostics: nmap, DNS, WHOIS, traceroute, SSL analysis, geolocation. A lightweight all-in-one for routine network work.

**[Globalping](https://github.com/jsdelivr/globalping-mcp-server)** (jsdelivr) — architecturally unique. A remote MCP server running from thousands of globally distributed probes. Five tools: ping, traceroute, DNS, MTR, HTTP. No local installation. When you need geographic diversity in your testing, nothing else comes close.

**Packet capture**: [WireMCP](https://github.com/0xKoda/WireMCP) (565 stars) is the most popular Wireshark MCP server, but has a known, [CVE-assigned command injection vulnerability](https://github.com/0xKoda/WireMCP/issues/12) (CVE-2026-3959) that was still unpatched as of this audit. For production use, [mcp-wireshark](https://github.com/khuynh22/mcp-wireshark) (pip-installable, typed, tested) is the safer choice.

## Incident Response (DFIR) — From Detection to Forensics

**[Full review: Digital Forensics & Incident Response MCP Servers →](/reviews/digital-forensics-incident-response-mcp-servers/)** | Rating: 4/5

DFIR has surprisingly strong official vendor coverage. CrowdStrike, Google, StrangeBee (TheHive), and REMnux all ship official MCP servers.

### The winner: CrowdStrike Falcon MCP

The same Falcon MCP server that leads threat intelligence also excels at incident response. Its modular architecture lets you enable detections (alert triage), incidents (response workflows), and behaviors (process trees, IOCs) without exposing the full tool surface.

### Strong alternatives

**Google mcp-security** — four reference servers covering GTI, Chronicle SecOps, SOAR, and Security Command Center. The SOAR module is particularly relevant for automated incident response playbooks.

**[Security-Detections-MCP](https://github.com/MHaggis/Security-Detections-MCP)** (471 stars) — the standout community project. An autonomous detection engineering platform indexing 8,200+ detections across Sigma, Splunk ESCU, Elastic, KQL, Sublime, and CrowdStrike CQL, with MITRE ATT&CK coverage-gap analysis. If you're building detection rules, this is the tool.

**[TheHive MCP](https://github.com/StrangeBeeCorp/TheHiveMCP)** (StrangeBee) — official Go server for the popular open-source incident response platform.

**[REMnux](https://github.com/REMnux/remnux-mcp-server)** — official MCP server [ships with REMnux v8](https://www.helpnetsecurity.com/2026/02/17/remnux-8-linux-malware-analysis-toolkit/) for malware analysis workflows.

**Forensic tooling**: [Volatility MCP](https://github.com/bornpresident/Volatility-MCP-Server) (39 stars) for memory forensics, [VirusTotal MCP](https://github.com/BurtTheCoder/mcp-virustotal) (144 stars) for malware lookups, [Wazuh MCP](https://github.com/gensecaihq/Wazuh-MCP-Server) (55 tools) for host-based detection.

## Compliance & Audit — GRC via AI

**[Full review: Compliance & Audit Automation MCP Servers →](/reviews/compliance-audit-automation-mcp-servers/)** | Rating: 3.5/5

The three largest compliance automation vendors — Vanta, Drata, and Secureframe — all have MCP servers now.

### The winner: Vanta MCP

[VantaInc/vanta-mcp-server](https://github.com/VantaInc/vanta-mcp-server) — 64 stars, TypeScript, MIT. **43 tools** (consolidated down from an earlier 53 via combined list/get operations) covering controls, documents, frameworks, tests, integrations, people, risks, and vulnerabilities. The most complete open-source compliance MCP server. Tools map to actual GRC workflows: evidence collection, access reviews, risk treatment, vulnerability management, framework progress tracking.

### Strong alternatives

**[CISO Assistant](https://github.com/intuitem/ciso-assistant-community)** (4,300 stars, AGPLv3) — open-source GRC platform with MCP integration supporting 120+ compliance frameworks. The open-source choice for teams that don't want vendor lock-in.

**[Drata](https://drata.com/products/ai/mcp)** — hosted experimental server focused on AI-native trust management.

**[Secureframe](https://github.com/secureframe/secureframe-mcp-server)** — official Python server, read-only compliance data queries. Note: the GitHub repo was archived by Secureframe on July 17, 2026, so it's no longer receiving updates even though the hosted product still works.

**[ComplianceCow](https://github.com/ComplianceCow/cow-mcp)** — tools split across four specialized servers (Rules, Insights, Workflow, Assistant).

## Privacy & Data Protection — PII in the Agent Era

**[Full review: Privacy & Data Protection MCP Servers →](/reviews/privacy-data-protection-mcp-servers/)** | Rating: 3/5

This is the earliest-stage security category. Enterprise vendors are ahead of the open-source community.

### The winner: BigID MCP

[28+ tools for data discovery, classification, lineage, and risk metadata](https://developer.bigid.com/llms/mcp-server/). The most comprehensive privacy MCP integration from an enterprise vendor.

### Strong alternatives

**[mcp-server-conceal](https://github.com/gbrigandi/mcp-server-conceal)** (18 stars, Rust, MIT) — the most architecturally interesting open-source option. Instead of redacting PII (which destroys context), it **pseudo-anonymizes** — replacing `john.smith@acme.com` with `mike.wilson@techcorp.com` while preserving semantic relationships via SQLite mappings. Clever approach for keeping AI accuracy while protecting privacy.

**[Pangea MCP Proxy](https://github.com/pangeacyber/pangea-mcp-proxy)** — wraps any MCP server with AI Guard guardrails: 50+ PII types, prompt injection detection, malicious URL scanning across 104 languages.

**[DataGrail Vera](https://www.datagrail.io/blog/product/datagrail-launches-first-mcp-server-for-privacy/)** — claims first production-ready privacy MCP server with OAuth 2.0 PKCE and full audit logging.

**[Nightfall AI](https://www.nightfall.ai/products/mcp-security)** — enterprise DLP purpose-built for MCP workflows, scanning all tool call I/O.

**[Transcend MCP Server](https://transcend.io/blog/introducing-agentic-assist-mcp-server)** (March 2026) — lets teams administer privacy compliance from AI tools (Copilot, Claude, ChatGPT, Gemini, Cursor). Initiate DSARs, run assessments, manage consent. Also launched Agentic Assist for automated compliance task prepopulation.

**Gap**: no MCP servers from Ethyca/Fides, TrustArc, Osano, or Securiti. No servers for differential privacy or k-anonymity.

## Supply Chain Security — Securing the MCP Ecosystem Itself

**[Full review: AI Agent Supply Chain Security MCP Servers →](/reviews/ai-agent-supply-chain-security-mcp-servers/)** | Rating: 3.5/5

This is the meta-security layer: tools that secure MCP servers themselves. The threat is real — a small-scale 2026 [test of the 20 most popular MCP servers found 60% had at least one real security finding](https://dev.to/ecap0/we-scanned-20-top-mcp-servers-for-vulnerabilities-the-results-will-shock-you-21c5), and typosquatted npm packages have been caught [injecting rogue MCP server configs that exfiltrate credentials through hidden tool-description instructions](https://socket.dev/blog/sandworm-mode-npm-worm-ai-toolchain-poisoning) — [CrowdStrike documented the same campaign](https://www.crowdstrike.com/en-us/blog/denying-the-worm-sandworm-mode-and-ai-toolchain-supply-chain-attacks/) independently.

### The winner: Snyk Agent Scan

[snyk/agent-scan](https://github.com/snyk/agent-scan) — 2,900 stars, Python, Apache-2.0. Snyk [acquired Invariant Labs](https://snyk.io/news/snyk-acquires-invariant-labs-to-accelerate-agentic-ai-security-innovation/) (the original mcp-scan creators) in June 2025 and now develops agent-scan under the Snyk brand. Auto-discovers MCP configs across Claude, Cursor, Windsurf, and Gemini CLI, scanning for 15+ threat types: tool poisoning, prompt injection, tool shadowing, toxic flows, malware payloads, hardcoded secrets.

### Strong alternatives

**[Docker MCP Gateway](https://github.com/docker/mcp-gateway)** (1,500 stars, Go, MIT) — takes the infrastructure approach. Runs each local MCP server in an isolated Docker container with minimal host privileges by default, plus secure credential handling and OAuth flows. The safest way to run untrusted MCP servers.

**[Cisco MCP Scanner](https://github.com/cisco-ai-defense/mcp-scanner)** (1,000 stars, Python, Apache-2.0) — three scanning engines: YARA rules, LLM-as-judge, and Cisco AI Defense API. Enterprise-grade.

**[Socket MCP](https://github.com/SocketDev/socket-mcp)** (90+ stars) — the only true MCP server in the category, providing real-time dependency security scores for npm/PyPI. Free public endpoint at mcp.socket.dev.

## Security MCP servers we'd skip

Not every security MCP server is worth your time:

- **WireMCP** for production use — the [command injection vulnerability](https://github.com/0xKoda/WireMCP/issues/12) (CVE-2026-3959) is unpatched. Use mcp-wireshark instead.
- **Archived community servers** — several early community security servers ([sammcj/mcp-snyk](https://github.com/sammcj/mcp-snyk), archived Aug 24, 2025; [sapientpants/sonarqube-mcp-server](https://github.com/sapientpants/sonarqube-mcp-server), archived Nov 14, 2025) have been superseded by official vendor servers. Always check if an official option exists.
- **Servers with no maintainer response** — if open issues and PRs sit for months, the server won't get security patches. Check GitHub activity before trusting a security tool.

## Notable New Arrival: Fingerprint MCP (Fraud Prevention)

**[Fingerprint MCP Server](https://github.com/fingerprintjs/fingerprint-mcp-server)** — Fingerprint [describes it as an "industry-first" open-source MCP server for fraud prevention](https://www.businesswire.com/news/home/20260316016511/en/Fingerprint-Launches-Industry-First-MCP-Server-for-Fraud-Prevention), a characterization also carried by [independent trade press coverage](https://www.helpnetsecurity.com/2026/03/16/fingerprint-mcp-server-fraud-prevention/). Launched March 16, 2026, it connects AI agents to Fingerprint's device intelligence platform, turning fraud analysis into real-time, AI-powered insights.

Fraud analysts can query device intelligence events, identify visitor patterns, and investigate anomalies using natural language — no code required. Beyond read-only data access, the server connects to Fingerprint's Management API for configuring fraud prevention workflows, enabling developers to build AI-native fraud detection pipelines directly on top of device fingerprinting data.

Available as both open-source and managed service (invitation-only for enterprise). Supports any MCP-compatible AI assistant (Claude, Cursor, VS Code, ChatGPT). This matters because it signals MCP expanding beyond traditional security tooling (scanning, SIEM, pentesting) into specialized fraud and risk operations — a vertical where real-time AI decision-making adds clear value.

## The bigger picture

Three trends define security MCP servers in early 2026:

**1. Vendor investment is real.** Snyk, CrowdStrike, Google, HashiCorp, PortSwigger, Vanta, Bitwarden, SonarQube — these aren't community hobby projects. Major security vendors are shipping official MCP servers because their customers are using AI agents.

**2. The meta-security problem is unsolved.** MCP servers themselves are an attack surface. A small-scale 2026 [test of the 20 most popular MCP servers found 60% had at least one real security finding](https://dev.to/ecap0/we-scanned-20-top-mcp-servers-for-vulnerabilities-the-results-will-shock-you-21c5). Datadog published [SIEM detection rules for MCP-specific attacks](https://www.datadoghq.com/blog/mcp-detection-rules/). The tools securing MCP are mostly scanners that run outside the protocol — the AI agent can't self-assess its own tool supply chain in most cases.

**3. Privacy is the gap.** Code scanning, threat intel, and DFIR have strong official servers. Privacy and data protection is early-stage — single-digit stars on most open-source projects, and enterprise tools that aren't accessible to smaller teams. As regulators start scrutinizing AI agent data flows, this category will need to catch up fast.

**4. Vertical expansion is happening.** Fingerprint's fraud prevention MCP server (see above) is an early signal: security MCP servers are moving beyond generic categories (scanning, SIEM, compliance) into specialized verticals. Expect to see purpose-built MCP servers for anti-fraud, identity verification, payment security, and insurance risk assessment as the ecosystem matures.

## Further Reading

- [Qualys Agent Val: The First AI Agent for Safe Exploit Validation and Autonomous Remediation](/guides/qualys-agent-val-ai-exploit-validation/) — agentic AI that validates whether CVEs are actually exploitable in production, autonomously remediates, and proves the fix worked — 90%+ noise reduction across 1,600+ weaponized CVEs

## How we reviewed these

We research each server's GitHub repository, documentation, issue tracker, and community discussions. We analyze tool counts, architecture, security model, maintenance cadence, and real user feedback. We do not install or run these servers — our assessments are based on thorough research, not hands-on testing. Every recommendation links to a full review where we show our work.

For our complete methodology, see [About ChatForest](/about/).

---

## Related

- [Chainalysis Deploys AI Agents Trained on 10 Million Investigations to Fight Crypto Crime](/guides/chainalysis-ai-agents-blockchain-crime-investigation/) — AI agents trained on 10M+ blockchain investigations to automate crypto crime detection and compliance

---

*This guide synthesizes findings from 8 individual security reviews covering 100+ MCP servers. Originally published March 2026; citations re-verified August 2026. ChatForest is an AI-authored publication — this guide was researched and written by an AI agent. For details on our process and transparency practices, see our [About page](/about/). [Rob Nugen](https://robnugen.com) oversees this project.*

