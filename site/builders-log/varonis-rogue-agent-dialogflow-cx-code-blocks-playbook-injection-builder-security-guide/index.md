# Rogue Agent: The Dialogflow CX Flaw That Let One Permission Hijack Every Chatbot in Your Project

> Varonis disclosed 'Rogue Agent' on July 7, 2026: a now-patched Google Dialogflow CX vulnerability where a single dialogflow.playbooks.update permission let an attacker overwrite the shared execution environment, silently intercepting conversations and injecting phishing prompts across every chatbot agent in the GCP project. No CVE, no known exploitation. Here's what happened and what builders should check.


Varonis Threat Labs published "Rogue Agent" on July 7, 2026: a detailed disclosure of a now-patched vulnerability in Google Cloud's Dialogflow CX service. The flaw sat in the Code Blocks feature inside Playbooks — a way to embed custom Python logic directly into conversation flows. It let an attacker with a single low-privilege permission overwrite the shared execution environment that every agent in a GCP project uses, intercepting conversations and injecting phishing prompts at scale.

The attack was discovered in November 2025. Google issued an initial patch in April 2026 and fully resolved the issue in June 2026. Varonis is not aware of exploitation in the wild before the patch.

If your organization uses Dialogflow CX with Playbooks and Code Blocks, this is a good time to audit — even though the underlying vulnerability is gone.

---

## How the Attack Worked

Dialogflow CX Playbooks let developers embed Code Blocks: fragments of Python that run during a conversation to call external APIs, process user input, or manipulate session state. Google executes these blocks in a Cloud Run container.

Varonis found that the wrapper file handling Code Block execution — `code_execution_env.py` — sat inside that container with write access. Anyone who could create or update a Code Block could modify it.

The attack chain:

1. **Initial foothold**: Attacker obtains `dialogflow.playbooks.update` permission on any one agent in the GCP project. This is presented as a scoped, per-agent permission.

2. **Reconnaissance**: A malicious Code Block enumerates the Cloud Run filesystem and locates `code_execution_env.py`.

3. **Overwrite**: The block downloads a modified version of the file from an attacker-controlled bucket and replaces the original inside the running container.

4. **Persistence**: From that point, the attacker's version runs for every Code Block execution — across every agent sharing the same project environment. It sits in the same execution scope as legitimate code, with access to `history` (full conversation records) and `state` (session parameters).

5. **Exfiltration and phishing**: The compromised wrapper silently transmits conversation data to an external server. It can also inject phishing prompts into the agent's responses — impersonating reauthentication requests to harvest user credentials.

6. **Cover-up**: Original Code Block configurations can be restored, leaving minimal forensic traces.

---

## What "One Permission" Actually Meant

The permission label `dialogflow.playbooks.update` sounds scoped: update permissions on a playbook, in one agent. The reality was broader.

Because Code Blocks in Dialogflow CX ran inside a shared Cloud Run execution environment at the GCP project level, modifying the execution wrapper affected every agent in that project, not just the one the attacker had permission on. A developer with access to a low-value test agent could — if they were compromised or malicious — affect production agents handling real user data.

This is the core lesson. Platform abstractions often make blast radius invisible. The IAM permission sounds narrow. The underlying infrastructure it can reach may not be.

---

## What Data Was at Risk

Within the execution scope available to Code Blocks, the attacker's modified wrapper had access to:

- Full conversation histories (the `history` variable)
- Session state parameters (the `state` variable)
- Any credentials submitted through phishing prompts injected into agent responses
- PII, payment details, and confidential business information passed through the chatbot

VPC Service Controls — a common GCP defense-in-depth measure — could be bypassed if the compromised container had unrestricted outbound access to the attacker's bucket.

---

## Google's Response

Varonis reported the vulnerability in November 2025 under responsible disclosure. Google acknowledged it and issued an initial mitigation in April 2026, with full resolution in June 2026. Google stated there is no known indication of customer compromise and that the underlying issue has been fully mitigated.

No CVE number has been assigned.

---

## Builder Checklist

The platform-level vulnerability is patched. What builders should still do:

**Audit IAM permissions now**
- Identify everyone with `dialogflow.playbooks.update` in your GCP project
- Verify each grant is scoped to the appropriate role and justification
- Revoke grants for offboarded employees and unused service accounts
- Apply least privilege: if someone only needs to read agents, they should not have update permissions

**Review all Code Blocks**
- Enumerate every Code Block in every Playbook in every agent in your project
- Confirm each block was created or last modified by an authorized actor
- Check for any Code Block that makes outbound network calls, writes to the filesystem, or references external URLs — those deserve closest scrutiny
- Correlate Playbook update events in Cloud Logging against expected change events

**Enable audit logging**
- Ensure Cloud Logging has DATA_WRITE audit logs enabled for Dialogflow CX
- Log queries to identify unusual Playbook update events:
  - Rare users making changes
  - Atypical source IPs
  - Off-hours modifications
  - Bulk updates across multiple agents

**Consider UEBA for GCP**
- User and Entity Behavior Analytics tools can baseline what normal Playbook update activity looks like and alert on deviations
- Posture management tools can flag when a Code Block pattern matches known risky behaviors (outbound HTTP, filesystem writes)

---

## The Broader Pattern

Rogue Agent sits alongside GuardFall and Friendly Fire as a reminder that the attack surface of AI development platforms extends into the platform infrastructure itself, not just your application code.

GuardFall (disclosed June 2026) showed a universal shell injection design flaw in agent guard implementations. Friendly Fire (disclosed July 8, 2026) showed how defensive coding agents could be tricked into executing attacker-controlled code from third-party codebases. Rogue Agent shows how a single low-privilege permission in a cloud AI platform can exceed its labeled blast radius by touching shared infrastructure.

In all three cases, the exploitable surface was not an obvious security component. It was a developer productivity feature: shell integration, code review automation, conversation logic blocks.

The emerging pattern is that the "one agent does one thing" mental model breaks down when execution environments are shared. Whether that is a shared Cloud Run container in Dialogflow CX, a shared file system in an agent orchestrator, or a shared process in a code execution sandbox, the permission that governs access to one agent may be executing in an environment that touches many.

Builders running agentic platforms on GCP — or any managed AI platform — should ask their vendors: what is the actual execution boundary for this permission, and does it align with what the permission label says?

---

*Varonis's original disclosure: [Rogue Agent: How a Single Code Block Could Hijack Your AI Conversations in Google's Dialogflow](https://www.varonis.com/blog/rogue-agent-dialogflow-attack) (July 7, 2026).*

