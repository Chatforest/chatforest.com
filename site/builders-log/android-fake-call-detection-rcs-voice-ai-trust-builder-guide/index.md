# Google's Android Fake Call Detection and the Emerging Trust Layer for Voice AI

> Google's June 2026 fake call detection feature uses RCS to verify callers at the device level. For builders shipping voice AI, customer service agents, or any phone-based product, it signals where the next trust problem is coming from.


**At a glance:** Google launched fake call detection in Android's June 2026 feature drop (June 2, 2026). The system uses end-to-end encrypted RCS to send a device-level verification signal when a contact calls you. If the signal is absent — as it would be with a cloned or spoofed call — Android warns the recipient to hang up. Google built this on the open RCS standard so other developers can implement the same verification pattern. For builders, the implications extend well beyond phone scam prevention: voice alone is no longer a trusted identity channel, and AI voice cloning is now the attack that's breaking that assumption at scale. Part of our **[Builder's Log](/builders-log/)**.

---

AI voice cloning is good enough to fool people. Not occasionally, in a lab, on a carefully prepared test — but at scale, in real-time, over a standard phone call. Google's new Android feature is a direct response to that fact, and it tells builders something important about where the trust layer for voice is heading.

## What Google Shipped

Google announced fake call detection on June 2, 2026, rolling it out globally through the Phone by Google app to Android 12 and later devices.

The mechanism is straightforward: when a contact calls you, their device sends an encrypted confirmation signal over RCS (Rich Communication Services). Your phone checks for that signal. If it's present and valid, the call appears normally. If it's absent — which it would be if a scammer is spoofing your contact's number and cloning their voice — Android displays a warning and recommends you hang up.

Three things matter technically:

**No audio leaves your device to Google's servers.** The verification runs entirely over encrypted RCS. Google sees that a signal was exchanged, not the content of your call.

**It's device-level attestation, not number-level.** The system isn't checking whether the number is legitimate — it's checking whether the call is originating from the registered hardware of the person who owns that number. Number spoofing becomes irrelevant if the hardware handshake doesn't match.

**It only works when both parties use Phone by Google.** Google Messages and Google Contacts must also be installed. This limits immediate coverage but sets the adoption trajectory.

## Why Google Built This Now

Voice cloning is the capability that made this necessary. A voice can be cloned from as little as three seconds of publicly available audio. Executives' earnings calls, conference keynotes, and podcast appearances give attackers all the training data they need. The FBI has classified deepfake audio and video as one of the fastest-growing fraud categories targeting U.S. enterprises in 2026.

The most documented case: a finance employee at a multinational transferred $25.6 million across fifteen transactions after a video conference in which every participant — including the apparent CFO — was an AI-generated deepfake. That case involved video; voice-only attacks require less infrastructure and have a lower barrier to entry.

The threat Google is responding to isn't theoretical. It's already in production against real users.

## What This Means for Builders

### If You Build Voice AI Agents or IVR Systems

Your automated voice calls now land in a world where users are being trained to distrust audio they can't verify. If your voice agent calls a customer on behalf of a business, and Android cannot verify the call's device origin, it may display a warning — or users may simply hang up based on general deepfake awareness.

The practical implication: pair voice contact with a simultaneous visual channel. Send an email or SMS at the moment of the voice call that confirms the agent is calling and what it's calling about. This creates a corroborating trust signal that doesn't depend on RCS attestation. For high-stakes calls (appointment reminders, payment confirmations, security alerts), this corroboration isn't optional anymore.

### If You Build Identity or Voice Biometric Systems

Voice alone has never been sufficient for high-assurance identity. This event makes that official at the consumer level. If your authentication flow relies on voice recognition or voice-print matching, add a fallback that doesn't depend on the audio channel — OTP, push notification, hardware key. The attack surface voice biometrics faces in 2026 is fundamentally different from what it faced in 2022.

### If You Build Communication or Comms-Adjacent Products

Google explicitly built fake call detection on the open RCS standard so other developers and device manufacturers can adopt the same protection. That's an invitation.

If you run a communication platform — even one not primarily phone-call-focused — the underlying pattern (device-level attestation over an encrypted side channel) is available to you. The architecture is: caller device signs a payload at the moment of call initiation, that payload is delivered over an encrypted channel independent of the call itself, and receiver device checks the signature before displaying the call. You can implement analogous trust signals for in-app voice, video, or messaging.

### If You Build Enterprise Security Tools

The same AI voice infrastructure that enables your customer service agent enables executive impersonation. AI-generated deepfake attacks have evolved from poorly crafted email fraud into real-time voice calls from the apparent CFO. The enterprise builders most exposed are the ones whose workflows have phone calls as a trusted channel for fund transfers, system access changes, or credential resets.

Audit whether any of your internal processes treat a voice call as sufficient authorization for a high-value action. If they do, layer in out-of-band confirmation — push notification to a registered device, cryptographic approval, a secondary human review — that doesn't depend on the audio being authentic.

## The Bigger Picture: A Trust Layer Is Being Built

HTTPS didn't eliminate web fraud, but it created the conditions for trust signals that users could act on. The padlock became a baseline expectation.

Google's fake call detection is a first step toward something similar for voice: device attestation as a baseline trust signal that users can learn to look for, built on an open standard that other developers can implement.

The capability layer for voice AI is moving fast — real-time cloning, sub-second generation, convincing prosody. The trust layer is catching up, but it's lagging. The window between a capability that can be weaponized and the infrastructure to detect that weaponization is where your users are living right now.

Build accordingly.

---

**Sources:**
- [How Android helps keep you safe from impersonation scams with fake call detection](https://blog.google/security/android-fake-call-detection/) — Google Security Blog, June 2, 2026
- [Google Phone app rolling out Android fake call detection that uses RCS](https://9to5google.com/2026/06/02/google-phone-fake-call-detection/) — 9to5Google, June 2, 2026
- [Android fake call detection: Google uses RCS to stop AI scams](https://www.notebookcheck.net/Android-fake-call-detection-Google-uses-RCS-to-stop-AI-scams.1314360.0.html) — Notebookcheck, June 2026
- [New Android feature promises to spot deepfake scam calls](https://www.helpnetsecurity.com/2026/06/03/android-fake-call-detection-feature/) — Help Net Security, June 3, 2026
- [Deepfake Dialers: How AI Voice Cloning Is Breaking Caller Trust in 2026](https://www.1routegroup.com/deepfake-dialers-ai-voice-phishing-2026/) — 1Route Group, 2026

