# Google's Search Services History: The Hidden AI Training Opt-In Every Builder Needs to Audit

> Google quietly replaced Web & App Activity with 'Search Services History' in June 2026, adding a nested 'Save Media' toggle that defaults to ON — feeding your team's Google Lens images, voice searches, Search Live recordings, and uploaded files into Google's AI training pipeline for up to four years. Here is what builders and enterprise teams need to know and do.


In late May 2026, Google began rolling out a replacement for the long-standing Web & App Activity control on search-related data: a new framework called **Search Services History**, paired with a separate **Personalized Recommendations** setting ([9to5Google, May 26, 2026](https://9to5google.com/2026/05/26/google-search-services-history-settings/); [Google Search Help: Get started with Search Services History](https://support.google.com/websearch/answer/17025248?hl=en)). By late June, coverage identified a nested **Save Media** sub-toggle inside that framework, and Google's own support documentation confirms it migrates to **on** for any account that previously had Web & App Activity turned on — which is most accounts, since that was itself the historical default ([9to5Google, June 22, 2026](https://9to5google.com/2026/06/22/google-saving-audio-images-used-to-search-how-to-turn-it-off/); [BleepingComputer, June 24, 2026](https://www.bleepingcomputer.com/news/google/google-releases-new-privacy-controls-for-activity-history-personalization/); [TechRepublic](https://www.techrepublic.com/article/news-google-search-uploads-train-ai-opt-out/)). When Save Media is on, Google retains images, audio, and video from your interactions with Search services and uses them to develop and improve its AI models — including the generative AI models behind AI Mode, Lens, Translate, and Search Live — disconnecting the media from your account first and retaining it for up to four years ([Google Search Help: Manage your saved media in Search Services History](https://support.google.com/websearch/answer/17028154?hl=en)).

TechCrunch described the update as "under-the-radar," reporting that Google announced it to users only via a customer email in June rather than a more prominent notice ([TechCrunch, July 6, 2026](https://techcrunch.com/2026/07/06/if-you-use-google-youre-training-its-ai-heres-how-to-opt-out/)).

---

This is a research-based guide. Facts are drawn from Google's own support documentation and reporting from [9to5Google](https://9to5google.com/2026/06/22/google-saving-audio-images-used-to-search-how-to-turn-it-off/), [TechCrunch](https://techcrunch.com/2026/07/06/if-you-use-google-youre-training-its-ai-heres-how-to-opt-out/), [TechRepublic](https://www.techrepublic.com/article/news-google-search-uploads-train-ai-opt-out/), [Tom's Guide](https://www.tomsguide.com/ai/google-just-changed-a-major-privacy-setting-heres-the-switch-i-turned-off-immediately), [BleepingComputer](https://www.bleepingcomputer.com/news/google/google-releases-new-privacy-controls-for-activity-history-personalization/), and [Euronews](https://www.euronews.com/next/2026/07/07/is-google-using-your-searches-to-train-its-ai-heres-how-to-opt-out). We did not test these settings ourselves.

---

## What Is Being Captured

When Save Media is on and you are signed into a Google account, Google's own support documentation and contemporary reporting describe it saving:

- **Google Lens** — images submitted for search, including screenshots from Circle to Search ([BleepingComputer](https://www.bleepingcomputer.com/news/google/google-releases-new-privacy-controls-for-activity-history-personalization/))
- **Google Search Live** — audio and video recordings from real-time search sessions ([Google Search Help](https://support.google.com/websearch/answer/17028154?hl=en))
- **Voice search** — recordings from spoken queries ([Google Search Help](https://support.google.com/websearch/answer/17028154?hl=en))
- **Google Translate** — spoken phrases entered for speaking-practice sessions ([9to5Google](https://9to5google.com/2026/06/22/google-saving-audio-images-used-to-search-how-to-turn-it-off/))
- **Uploaded files** — documents and images attached during AI Mode or Ask Maps search interactions ([Euronews](https://www.euronews.com/next/2026/07/07/is-google-using-your-searches-to-train-its-ai-heres-how-to-opt-out))

The data is not saved in identifiable form forever. Google's support page for the setting states that data is "disconnected from your Google Account before it is used to train our AI models or reviewed by our trained service providers," that Google uses "filters designed to automatically remove a broad range of identifying info or sensitive personal information," and that saved media used for training is retained for up to four years ([Google Search Help: Manage your saved media in Search Services History](https://support.google.com/websearch/answer/17028154?hl=en)). That same page notes disabling Save Media does not delete or disconnect media saved before the toggle was switched off.

Four years is a long data retention window, and "disconnected from your account" is not the same as deleted.

---

## Why This Matters for Builders

The personal-privacy story is well covered elsewhere. The builder and enterprise story is less so.

### 1. Your users' inputs may be in Google's training queue

If you build a product that uses Google Lens via the API, or that encourages users to run Google searches as part of your workflow — and those users are signed into Google — their submitted images and audio may now feed Google's AI training. That is a data-flow your privacy policy, terms of service, and enterprise agreements may not currently disclose.

This does not apply to server-side API calls. Google Cloud's Vision API documentation states Google does not use customer image content "for any purpose except to provide you with the Vision API service," that content isn't used to train or fine-tune models without customer permission, and that the API is covered by the Cloud Data Processing Addendum rather than the consumer Search settings described here ([Google Cloud: Vision API data usage](https://docs.cloud.google.com/vision/docs/data-usage)). The risk described in this piece is specific to **browser-based and mobile interactions where users are signed into a personal Google account**, not to Google Cloud API usage.

### 2. Enterprise teams doing sensitive research face real exposure

Competitive intelligence teams, legal teams, regulatory affairs teams, and client services teams frequently upload screenshots, product images, and documents into Google Lens or Google Search to identify products, extract text, or research suppliers. If those uploads contain:

- Client materials
- Confidential product designs
- Regulatory filings under NDA
- M&A target information

...and the employee is signed into their personal Google account (common on personal laptops or BYOD devices), those materials may now be in a Google AI training corpus for four years.

Enterprise Google Workspace accounts with managed Chrome policies may have different defaults — IT teams should verify whether their domain policies control the Search Services History setting for managed accounts.

### 3. GDPR and CCPA exposure

This is our own analysis, not a reported fact: we found no formal regulatory complaint or investigation specifically targeting the Save Media default as of this writing. Separately, on December 9, 2025, the European Commission opened a formal antitrust investigation into Google's use of web publisher and YouTube content to power AI Overviews and AI Mode — a different issue (competition law, publisher/creator compensation for training content) from the consumer Save Media setting covered here ([European Commission press release IP/25/2964](https://ec.europa.eu/commission/presscorner/detail/en/ip_25_2964); [Computerworld](https://www.computerworld.com/article/4103262/european-commission-investigates-googles-ai-training-processes.html)). We mention it only as evidence that Google's AI-training data sourcing is under active EU scrutiny generally, not as an investigation into this specific setting.

On the merits: where a company relies on consent as its lawful basis under the GDPR, that consent must be freely given, specific, informed, and given through a clear affirmative action — not inferred from a pre-set default a user never actively chose (GDPR [Article 6](https://gdpr-info.eu/art-6-gdpr/) and [Article 7](https://gdpr-info.eu/art-7-gdpr/)). Whether Google is instead relying on a different lawful basis (such as legitimate interest) for Save Media, and whether that basis would hold up, is a genuinely open legal question we are not able to resolve here. If you operate a product serving EU users that routes any data through Google Search services, that open question is a reason for your own legal review, not a settled compliance verdict.

---

## How to Opt Out

The setting lives at [myactivity.google.com](https://myactivity.google.com). The path:

1. Sign in to your Google account
2. Find **Search Services History** (separate from Web & App Activity)
3. To stop all search history collection: turn off Search Services History entirely
4. To keep personal search history but stop media capture: leave Search Services History on, find the nested **Save Media** sub-toggle, and uncheck it

The two controls are separate. Turning off Web & App Activity (the old control) does not affect Search Services History — this is a new framework ([Google Search Help: Manage your saved media in Search Services History](https://support.google.com/websearch/answer/17028154?hl=en); [TechRepublic](https://www.techrepublic.com/article/news-google-search-uploads-train-ai-opt-out/)).

---

## What Enterprise IT Teams Should Do Now

- **Audit managed account policies**: Check whether Google Workspace admin controls govern Search Services History for managed accounts, or whether personal account settings override
- **Update acceptable-use guidance**: Add explicit guidance that employees should not upload confidential, client, or regulated data into Google Search, Lens, or Search Live using personal Google accounts
- **Review your privacy policy**: If your product routes any user interaction through Google Search services and users are signed in, your data-processing disclosure may need updating
- **Check BYOD exposure**: Personal devices used for work are the highest-risk surface — employees are signed into personal accounts where corporate policy cannot enforce the Save Media toggle

---

## Context: Google's Broader AI Data Strategy

This change is part of a broader pattern. Google is systematically expanding the data surface it can use for AI training:

- **December 9, 2025**: European Commission opens a formal antitrust investigation into Google's use of publisher and YouTube content for AI ([European Commission](https://ec.europa.eu/commission/presscorner/detail/en/ip_25_2964)) — a separate matter from Search Services History, included here only as evidence of the broader pattern
- **May 26, 2026**: Search Services History and Personalized Recommendations settings begin rolling out, replacing Web & App Activity for Search services ([9to5Google](https://9to5google.com/2026/05/26/google-search-services-history-settings/))
- **June 22, 2026**: Reporting identifies the Save Media sub-toggle capturing images, audio, and video by default for migrated accounts ([9to5Google](https://9to5google.com/2026/06/22/google-saving-audio-images-used-to-search-how-to-turn-it-off/))
- **July 6–7, 2026**: Broader "how to opt out" press coverage begins ([TechCrunch](https://techcrunch.com/2026/07/06/if-you-use-google-youre-training-its-ai-heres-how-to-opt-out/); [Euronews](https://www.euronews.com/next/2026/07/07/is-google-using-your-searches-to-train-its-ai-heres-how-to-opt-out))

The pattern is familiar from the AI industry broadly: expand what is collected, default new categories to on, provide opt-out mechanisms that require effort to discover. For enterprise builders, the appropriate response is not to trust that defaults will protect you — audit what your users' data is touching, what those services' terms permit, and whether your own disclosures are accurate.

---

## The Bottom Line

If your team regularly submits images, documents, or audio into Google Search services, and those team members are signed into personal Google accounts, some of that material may now sit in Google's AI training pipeline for up to four years. The fix takes two minutes at myactivity.google.com. The audit of your enterprise exposure takes longer, but it should happen now, before a compliance review surfaces it under worse conditions.

