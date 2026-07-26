# Google's Search Services History: The Hidden AI Training Opt-In Every Builder Needs to Audit

> Google quietly replaced Web & App Activity with 'Search Services History' in June 2026, adding a nested 'Save Media' toggle that defaults to ON — feeding your team's Google Lens images, voice searches, Search Live recordings, and uploaded files into Google's AI training pipeline for up to four years. Here is what builders and enterprise teams need to know and do.


On June 10, 2026, Google quietly replaced the familiar Web & App Activity control for search data with a new framework called **Search Services History**. On July 12, it began rolling the change out broadly, with a nested **Save Media** toggle that is **on by default**. When Save Media is on, Google retains images, audio, and video from your interactions with Search services and uses them to develop and improve its AI models — including training generative AI — for up to four years.

Most users never saw a notification. The change arrived via a customer email in late June. Most did not read it.

---

This is a research-based guide. Facts are drawn from Google's support documentation, TechCrunch, TechRepublic, Tom's Guide, Euronews, and reporting from multiple outlets. We did not test these settings ourselves.

---

## What Is Being Captured

When Save Media is on and you are signed into a Google account, Google saves:

- **Google Lens** — images submitted for search, including screenshots from Circle to Search
- **Google Search Live** — audio and video recordings from real-time search sessions
- **Voice search** — recordings from spoken queries
- **Google Translate** — spoken phrases entered for speaking-practice sessions
- **Uploaded files** — documents and images you attach or upload during a search interaction

The data is not saved in identifiable form forever. Google says it disconnects saved media from your Google Account before using it for AI training, applies filtering for sensitive content, and retains it for up to four years.

Four years is a long data retention window, and "disconnected from your account" is not the same as deleted.

---

## Why This Matters for Builders

The personal-privacy story is well covered elsewhere. The builder and enterprise story is less so.

### 1. Your users' inputs may be in Google's training queue

If you build a product that uses Google Lens via the API, or that encourages users to run Google searches as part of your workflow — and those users are signed into Google — their submitted images and audio may now feed Google's AI training. That is a data-flow your privacy policy, terms of service, and enterprise agreements may not currently disclose.

This does not apply to server-side API calls. The Google Lens API and Google Cloud Vision API operate under Google Cloud's separate data processing agreements, which have different data retention terms. The risk is specific to **browser-based and mobile interactions where users are signed into a personal Google account**.

### 2. Enterprise teams doing sensitive research face real exposure

Competitive intelligence teams, legal teams, regulatory affairs teams, and client services teams frequently upload screenshots, product images, and documents into Google Lens or Google Search to identify products, extract text, or research suppliers. If those uploads contain:

- Client materials
- Confidential product designs
- Regulatory filings under NDA
- M&A target information

...and the employee is signed into their personal Google account (common on personal laptops or BYOD devices), those materials may now be in a Google AI training corpus for four years.

Enterprise Google Workspace accounts with managed Chrome policies may have different defaults — IT teams should verify whether their domain policies control the Search Services History setting for managed accounts.

### 3. GDPR and CCPA exposure

In July 2026, the European Union opened an investigation into whether Google's terms on content creators for AI are fair. For EU users, Google's claimed lawful basis for using uploaded media in AI training may face challenge — GDPR generally requires explicit consent, not an opt-out buried in nested account settings.

If you operate a product serving EU users that routes any data through Google Search services, this change may affect your GDPR compliance posture. Legal review is warranted before this becomes a regulatory issue.

---

## How to Opt Out

The setting lives at [myactivity.google.com](https://myactivity.google.com). The path:

1. Sign in to your Google account
2. Find **Search Services History** (separate from Web & App Activity)
3. To stop all search history collection: turn off Search Services History entirely
4. To keep personal search history but stop media capture: leave Search Services History on, find the nested **Save Media** sub-toggle, and uncheck it

The two controls are separate. Turning off Web & App Activity (the old control) does not affect Search Services History — this is a new framework.

---

## What Enterprise IT Teams Should Do Now

- **Audit managed account policies**: Check whether Google Workspace admin controls govern Search Services History for managed accounts, or whether personal account settings override
- **Update acceptable-use guidance**: Add explicit guidance that employees should not upload confidential, client, or regulated data into Google Search, Lens, or Search Live using personal Google accounts
- **Review your privacy policy**: If your product routes any user interaction through Google Search services and users are signed in, your data-processing disclosure may need updating
- **Check BYOD exposure**: Personal devices used for work are the highest-risk surface — employees are signed into personal accounts where corporate policy cannot enforce the Save Media toggle

---

## Context: Google's Broader AI Data Strategy

This change is part of a broader pattern. Google is systematically expanding the data surface it can use for AI training:

- June 10: Search Services History framework introduced, replacing Web & App Activity for search data
- July 7: Rolling out broadly, privacy coverage begins
- July 12: Save Media sub-toggle released to users
- July 2026: EU opens investigation into Google's AI training terms for content creators

The pattern is familiar from the AI industry broadly: expand what is collected, default new categories to on, provide opt-out mechanisms that require effort to discover. For enterprise builders, the appropriate response is not to trust that defaults will protect you — audit what your users' data is touching, what those services' terms permit, and whether your own disclosures are accurate.

---

## The Bottom Line

If your team regularly submits images, documents, or audio into Google Search services, and those team members are signed into personal Google accounts, some of that material may now sit in Google's AI training pipeline for up to four years. The fix takes two minutes at myactivity.google.com. The audit of your enterprise exposure takes longer, but it should happen now, before a compliance review surfaces it under worse conditions.

