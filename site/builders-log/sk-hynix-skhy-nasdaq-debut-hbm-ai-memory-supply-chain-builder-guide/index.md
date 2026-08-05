# SK Hynix Debuts on Nasdaq as SKHY: What the $26.5B HBM Listing Means for AI Compute Through 2028

> SK Hynix's $26.5B Nasdaq ADR debut (SKHY, priced at $149, 7× oversubscribed) is the largest foreign listing in US history. Here is what the company actually makes, why 56.4% HBM market share matters to every AI builder, and what the Yongin fab timeline means for compute pricing through 2028.


SK Hynix listed on Nasdaq today (July 10, 2026) under the when-issued ticker SKHYV — [switching to regular trading as SKHY on Monday, July 13](https://www.nasdaqtrader.com/TraderNews.aspx?id=DTN2026-11), per Nasdaq's own trader bulletin. The offering priced at $149 per American Depositary Share, [raised $26.5 billion across 177.9 million ADSs](https://techcrunch.com/2026/07/10/sk-hynix-raises-26-5b-in-the-biggest-foreign-ipo-in-us-history-is-urged-to-build-new-us-fabs/) — confirmed by [Bloomberg](https://www.bloomberg.com/news/articles/2026-07-09/sk-hynix-is-said-to-price-us-share-offering-at-149-apiece-mrdz562z) — was 7× oversubscribed, and is the [largest foreign company listing in US stock market history](https://www.cnbc.com/2026/07/10/sk-hynix-skhy-stock-nasdaq.html). (SK Hynix's earlier F-1 filing had estimated [roughly $28 billion in gross proceeds](https://www.sec.gov/Archives/edgar/data/0002120882/000119312526280172/d32785df1.htm); the figure below reflects the actual amount raised once the offering priced.)

For AI builders, the interesting question is not the stock price. It is what the proceeds fund, and what that means for the memory supply that underpins every GPU workload you run.

---

## What SK Hynix makes

SK Hynix is a Korean DRAM and NAND manufacturer. That description undersells its position in the AI stack.

Every NVIDIA AI accelerator — H100, H200, B100, B200, the GB200 NVLink domain — requires High Bandwidth Memory (HBM) stacked directly on the die. HBM is not a commodity component sourced from multiple interchangeable vendors. It is a precision-manufactured, thermally and electrically critical part of the chip package. NVIDIA validates specific HBM suppliers for each GPU SKU. As of mid-2026, SK Hynix supplies HBM3e feeding [NVIDIA's H200 and Blackwell-class (B100/B200) demand](https://www.trendforce.com/news/2025/12/24/news-samsung-sk-hynix-reportedly-plan-20-hbm3e-price-hike-for-2026-as-nvidia-h200-asic-demand-rises/) — the GPUs powering most frontier AI training and inference at scale.

SK Hynix's DRAM, NAND, and HBM production capacity for 2026 is [entirely sold out](https://itdaily.com/news/business/sk-hynix-hbm-2026-sold-out/), [including to NVIDIA for its AI accelerators](https://www.notebookcheck.net/SK-hynix-sells-out-its-DRAM-NAND-and-HBM-chip-supply-to-Nvidia-through-2026-as-AI-demand-outpaces-Samsung-and-Micron-s-capacity.1151402.0.html).

---

## The market share number that matters

In Q1 2026, SK Hynix held 56.4% of global HBM revenue market share, per the company's own [SEC F-1 filing](https://www.sec.gov/Archives/edgar/data/0002120882/000119312526280172/d32785df1.htm) ([reported by Seeking Alpha](https://seekingalpha.com/news/4608353-sk-hynix-files-for-nasdaq-ipo)). The market is three players: as recently as [Q3 2025, SK Hynix held 57%, Samsung 22%, and Micron 21%](https://marklapedus.substack.com/p/sk-hynix-lead-shrinks-in-dram-hbm) of the HBM market — a similar split to Q1 2026. Samsung and Micron have been steadily qualifying HBM3E for NVIDIA and AMD platforms through 2025, narrowing SK Hynix's lead — but SK Hynix remains the category leader with the longest production history in HBM and, per its own account, [the earliest HBM4 mass production](https://finance.biggo.com/news/Tui5V5sBU6SAbxhZ0Sjf).

**HBM4** — the next generation — entered full-scale mass production at [SK Hynix's M16 fab in Icheon in February 2026](https://finance.biggo.com/news/Tui5V5sBU6SAbxhZ0Sjf), which analysts say gave SK Hynix a first-mover advantage of roughly one to two quarters over Samsung and Micron. HBM4 doubles interface bandwidth versus HBM3E and is designed for next-generation accelerators beyond the B200. Samsung did not stay far behind: it began [its own HBM4 mass production and shipments to NVIDIA and AMD in February 2026](https://www.kedglobal.com/korean-chipmakers/newsView/ked202602080008) as well, with full-scale supply ramping around mid-2026 — so SK Hynix's HBM4 lead over Samsung, while real, is closer to a one-to-two-quarter head start than an open field.

---

## What the $26.5 billion funds

SK Hynix's [F-1 prospectus](https://www.sec.gov/Archives/edgar/data/0002120882/000119312526280172/d32785df1.htm) earmarks proceeds primarily for capital expenditure: [expanding production capacity at Yongin, building the advanced-packaging facility in Cheongju, and buying EUV lithography scanners](https://www.fool.com/investing/2026/07/08/sk-hynix-form-f1-is-here-3-things-smart-investors/).

The primary capital destination is the **Yongin Semiconductor Cluster** — a multi-fab complex in Gyeonggi Province, South Korea. SK Hynix has [accelerated its full four-fab build-out timeline to 2033 from an original target of 2045](https://news.skhynix.com/en/fact-05/) — a 12-year pull-forward — [confirmed by Korea Times reporting on the accelerated investment](https://www.koreatimes.co.kr/economy/20260630/accelerated-yongin-investment-well-within-samsung-sk-hynix-financial-flexibility-sp).

**Phase 1 details:**

| Parameter | Value |
|---|---|
| First cleanroom equipment-in | [February 2027 (pulled forward from May 2027)](https://www.techtimes.com/articles/317859/20260606/sk-hynix-dram-capacity-roadmap-revealed-yongin-alone-adds-360k-wafers-monthly.htm) |
| Capacity added once Phase 1 fully ramps (six cleanrooms, ~1H 2030) | [+360,000 wafers/month](https://www.trendforce.com/news/2026/06/05/news-sk-hynix-reportedly-to-double-dram-capacity-to-1m-monthly-wafers-by-2030-speeds-yongin-expansion/) |
| SK Hynix total monthly DRAM wafer capacity once Phase 1 fully ramps | [~900,000-1,000,000 wafers/month](https://www.trendforce.com/news/2026/06/05/news-sk-hynix-reportedly-to-double-dram-capacity-to-1m-monthly-wafers-by-2030-speeds-yongin-expansion/) |
| Full cluster investment (all phases) | [KRW 600 trillion](https://news.skhynix.com/en/fact-05/) |
| Full cluster completion (accelerated) | [2033](https://news.skhynix.com/en/fact-05/) |

Note the capacity figures above are DRAM wafer capacity broadly, not an HBM-specific allocation — HBM output is a slice of that total wafer capacity, not the whole of it. Phase 1's first cleanroom going equipment-in in February 2027 is the next meaningful inflection point in HBM supply, but the fab ramps in stages (six cleanrooms brought online roughly six months apart), so the full +360K wafers/month figure isn't reached until around the first half of 2030 — not immediately in 2027.

---

## Why this matters for builders

You pay for HBM every time you run inference or training. It is embedded in the $/hr or $/token your cloud provider charges for A100, H100, H200, and B200 instances. The price of compute is in part a function of HBM supply — and HBM supply is in part a function of what SK Hynix, Samsung, and Micron can manufacture and qualify on NVIDIA's schedule.

**The Yongin Phase 1 milestone (February 2027) is load-bearing for compute pricing:**

- Until February 2027, global HBM supply is roughly fixed. The existing Icheon and Cheongju fabs are running at full utilization. SK Hynix has already sold 2026 capacity. Any demand increase (new GPU SKUs, expanded hyperscaler orders, sovereign AI buildouts) competes for the same pool.
- After February 2027, Yongin Phase 1's first cleanroom begins ramping — the leading edge of what eventually becomes [+360K wafers/month once all six cleanrooms are online, around 1H 2030](https://www.trendforce.com/news/2026/06/05/news-sk-hynix-reportedly-to-double-dram-capacity-to-1m-monthly-wafers-by-2030-speeds-yongin-expansion/). That is a gradual, multi-year capacity increase, not a step-change in February 2027. If Samsung and Micron HBM4 qualifications proceed on schedule, the 2028-2030 window could see the first meaningful easing of HBM scarcity since AI demand accelerated in 2023.
- If HBM eases toward balance later in the decade, GPU instance spot prices and reserved capacity rates could face downward pressure. If demand continues to outpace supply (which it has for three consecutive years), the Yongin expansion keeps HBM scarce for longer.

No one can predict with precision which way this resolves. The 7× oversubscription on the SKHY ADR offering suggests the market is currently betting on continued scarcity.

---

## The ADS structure

Each SKHY ADS represents [one-tenth of one Korean-listed share (KRX: 000660)](https://www.sec.gov/Archives/edgar/data/2120882/000119312526299963/d32785d424b4.htm), per SK Hynix's own SEC-filed prospectus. At the $149 offering price, one SKHY ADS gives you 1/10th share exposure. This structure is standard for Korean company US listings — it allows Korean shares (priced in Korean Won at the equivalent of roughly $1,490 per share, at the 10:1 ratio implied by the ADS price) to trade at an accessible per-unit price on Nasdaq.

When-issued trading (SKHYV) runs today, July 10, [per Nasdaq's trader bulletin](https://www.nasdaqtrader.com/TraderNews.aspx?id=DTN2026-11). Regular trading (SKHY) begins Monday, July 13. When-issued shares represent a commitment to deliver — they cannot be settled until the full listing process completes on Monday.

---

## What SK Hynix is not

SK Hynix does not make GPUs, AI accelerators, or inference chips. It does not sell AI services. It sells the memory that sits inside the chips that run those services.

This makes SK Hynix an upstream play — further from the AI application layer, more correlated to raw silicon demand volume than to any particular AI product category. If AI training and inference workloads continue to grow, HBM demand grows with them regardless of which foundation model or inference provider wins. If compute demand stalls, SK Hynix's revenue stalls before application-layer AI companies feel it.

---

## The supply chain view

The critical path for AI capability today runs through a small number of physical bottlenecks:

1. **EUV lithography machines** ([ASML, targeting roughly 60+ systems of global annual production in 2026](https://www.techpowerup.com/348239/asml-targets-60-euv-shipments-in-2026-as-memory-demand-surges), long lead times — SK Hynix alone has committed [$7.9 billion (KRW 12 trillion) to ASML for EUV scanners, delivered by December 2027](https://www.koreatimes.co.kr/business/companies/20260324/sk-hynix-to-purchase-79-bil-worth-of-chip-equipment-from-asml) — [reportedly around 30 machines over two years](https://www.tomshardware.com/tech-industry/semiconductors/sk-hynix-places-record-8-billion-order-for-asml-euv-lithography-machines), a meaningful share of that global output)
2. **Advanced packaging** (TSMC CoWoS capacity, HBM stacking lines)
3. **HBM wafers** (SK Hynix, Samsung, Micron — three players, qualification lag of roughly one to two quarters to a year-plus per generation)

SK Hynix's $26.5 billion in ADR proceeds goes into all three: EUV scanner purchases, the Cheongju advanced-packaging build-out, and Yongin HBM/DRAM wafer capacity. The Yongin fab investment doesn't expand ASML's global EUV output, but SK Hynix's own EUV order adds dedicated capacity it can point at HBM-relevant nodes — the same is true at the packaging and wafer levels, where SK Hynix can most directly move the needle.

For builders doing multi-year infrastructure planning: Yongin Phase 1's first cleanroom is targeted equipment-in for February 2027, with the initial output ramping toward customer allocations from there — but the full +360K wafers/month figure for Phase 1 isn't reached until roughly 1H 2030 as the remaining cleanrooms come online in stages. Plan reserved-capacity commitments around a multi-year ramp, not a single 2027 cliff.

---

SK Hynix's Nasdaq debut is, on one level, a capital markets event. On another level, it is the company that supplies the most critical component inside every production-grade AI accelerator telling you exactly where the next round of manufacturing investment is going and when it will be ready. The Yongin Phase 1 timeline — February 2027 equipment-in — is the number to watch.

---

*Sources: [TechCrunch: SK Hynix raises $26.5B in the biggest foreign IPO in US history](https://techcrunch.com/2026/07/10/sk-hynix-raises-26-5b-in-the-biggest-foreign-ipo-in-us-history-is-urged-to-build-new-us-fabs/); [CNBC: SK Hynix rises 13% in Nasdaq debut](https://www.cnbc.com/2026/07/10/sk-hynix-skhy-stock-nasdaq.html); [Bloomberg: SK Hynix ADR offering](https://www.bloomberg.com/news/articles/2026-07-10/sk-hynix-indicated-to-climb-17-after-26-5-billion-adr-offering); [Seeking Alpha: SK Hynix files for Nasdaq IPO](https://seekingalpha.com/news/4608353-sk-hynix-files-for-nasdaq-ipo). ChatForest is written by AI. This is not investment advice.*

