---
id: META-GLOSS-001
title: "T1 Abbreviation Definitions — locked"
genre: GLOSS
page_status: candidate
page_version: 0.2.0
schema_version: 0.1.0
recorded: 2026-10-17
derived_from: "T1 Abbreviation Definitions — advised, for amendment.md (user-amended v0.1)"
ruling: WR-032
---

# T1 Abbreviation Definitions v0.2 — locked

Applied: your amendments to v0.1. 7 rows dropped as NOISE, 5 two-sense terms locked to one sense, 2 definitions edited by you, 142 accepted as advised. Result: 149 entries.

Basis: C = from your notes · K = standard meaning · G = my guess, accepted by you · U = your edit, not checked against a primary source.


## 1. Ad metrics & economics

| # | Abbr | Locked definition | Basis |
|---|---|---|---|
| 1 | CTR | Click-through rate = clicks ÷ impressions | K |
| 2 | CPC | Cost per click = spend ÷ clicks | K |
| 3 | ROAS | Return on ad spend = attributed sales ÷ ad spend | K |
| 4 | CPA | Cost per acquisition (per order) = spend ÷ orders | K |
| 5 | AOV | Average order value; in your notes used as list price per SKU in `dim_economics` | C |
| 6 | ASP | Average selling price = revenue ÷ units (realized) | C |
| 7 | CM | Contribution margin = (basis − COGS − FBA fee − referral − storage − returns) ÷ basis; your notes use CM2 for the post-fee level | C |
| 8 | P&L | Profit and loss statement (SKU-level and account-level) | K |
| 9 | ROI | Return on investment | K |
| 10 | KPI | Key performance indicator | K |
| 11 | VCPM | Cost per 1,000 viewable impressions (SD/SB video bidding model) | C |
| 12 | NTB | New-to-brand (customers who have not bought the brand in the prior 12 months) | K |
| 13 | DPV | Detail page views | K |
| 14 | BSR | Best Sellers Rank | K |
| 15 | SKC | Single-keyword campaign; your engine routes high-volume BIDHARD terms to "its own single-keyword exact campaign" when volume ≥ `SKC_VOL_MIN` | C |
| 16 | YTD | Year to date (your windows: `current_ytd`, `prior_plus_current_ytd`) | C |
| 17 | MRR | Monthly recurring revenue (agency metric) | K |
| 18 | NPS | Net Promoter Score (agency client-satisfaction metric) | K |
| 19 | HHI | Herfindahl-Hirschman Index — market-concentration score used for competitive density; your note: HHI < 2,500 = fragmented market | C |
| 21 | Average Cost of Real Sale | Undefined in corpus. Advised: total ad spend ÷ ad-attributed orders net of returns ("true CPA") | G |

## 2. Amazon programs, placements, inventory

| # | Abbr | Locked definition | Basis |
|---|---|---|---|
| 22 | SP | Sponsored Products | K |
| 23 | SP+SB | Sponsored Products and Sponsored Brands combined (search-term scope) | C |
| 24 | SQP | Search Query Performance report (Brand Analytics); your notes: ASIN view capped at 100 rows per ASIN-week | C |
| 25 | DSP | Amazon Demand-Side Platform (programmatic display/video) | K |
| 26 | TOS | Top of search (placement). Your engine also uses "held-TOS" = organic position ≤ `TOS_ORGANIC_MAX` (default 4) | C |
| 27 | PDP | Product detail page (also a placement: "product pages") | C |
| 28 | A+ | A+ Content (enhanced brand content on the detail page) | K |
| 29 | FBA | Fulfillment by Amazon | K |
| 30 | FBM | Fulfilled by Merchant | K |
| 31 | AFN | Amazon Fulfillment Network (FBA inventory on hand) | K |
| 32 | AWD | Amazon Warehousing and Distribution (upstream bulk storage) | K |
| 33 | OOS | Out of stock | C |
| 34 | OE | Opportunity Explorer (Seller Central niche research tool) | C |
| 35 | ISS | Impression share (search-term impression share; "ISS share %") | C |
| 36 | ST | Search term (as in "SP ST impression share") | C |
| 37 | MKT | Marketplace code slot in file and campaign names, e.g. `{CLIENT}_{MKT}_RUN{n}` | C |
| 38 | ACCT | Account-level (file-naming slot alternative to ASIN) | C |
| 39 | LP | Linear programming (optimization, e.g. budget allocation). The landing-page sense is never abbreviated: write "landing page". | C (sense locked by you) |

## 3. Targeting & intent-segment codes (your naming grammar)

| # | Abbr | Locked definition | Basis |
|---|---|---|---|
| 40 | BRAN | Intent segment: branded search terms (own brand) | C |
| 41 | DEF | Intent segment: defensive — protect own brand/ASINs (keyword or own-ASIN targeting) | C |
| 42 | BRAN DEF | Branded-defense campaigns: bidding on own brand terms to block conquesting | C |
| 43 | GENE | Intent segment: generic (non-branded category) terms | C |
| 44 | RANK | Intent segment: ranking campaigns — exact-match pushes to move organic rank | C |
| 45 | COMP | Intent segment: competitor brand terms (keyword conquesting) | C |
| 46 | ATT | Intent segment: attack — ASIN targeting of in-aisle direct competitors ("node == own_node → ATT") | C |
| 47 | CROS | Intent segment: cross-sell — ASIN targeting on complementary (adjacent-node) products | C |
| 48 | CAT | Intent segment: category targeting (CAT, CAT-DEF, CAT-TEST variants) | C |
| 49 | EVNT | Intent segment: event overlay (Prime Day, deals, seasonal spikes) | C |
| 50 | APR | Audience segment code (SD/DSP audiences); expansion not in corpus. Advised: "Audiences – Purchase Remarketing" | G |
| 51 | AVR | Audience segment code; expansion not in corpus. Advised: "Audiences – Views Remarketing" | G |
| 52 | AAA | Audience segment code; expansion not in corpus. Advised: "Amazon Audiences (in-market/lifestyle)" | G |
| 54 | INMA | Audience code: in-market audiences | G |
| 55 | LOOSE | Auto-targeting group: loose match | K |
| 56 | CLOSE | Auto-targeting group: close match | K |
| 57 | SUBST | Auto-targeting group: substitutes | K |
| 58 | KW | Keyword (targeting type: keyword → Exact/Phrase/Broad) | C |
| 59 | DEFEND | Engine action bucket: impression share fell H1→H2 while volume held → defend the term | C |

## 4. Account-structure philosophies

| # | Abbr | Locked definition | Basis |
|---|---|---|---|
| 61 | SKAG | Single-keyword ad group | K |
| 62 | SAG | Single-ASIN ad group | K |
| 63 | STAG | Single-theme ad group (themed keyword clusters) | C |
| 64 | Hagakure | Consolidation philosophy: fewer, broader campaigns/ad groups to maximize data density for Amazon's bidding algorithm | C |
| 65 | Rainbow | Portfolio/reporting overlay: tier portfolios (by SKU tier or margin band) for P&L-driven accounts; v1.4.1 "Rainbow tier" | C |

## 5. Analytics & statistical methods (TECH genre)

| # | Abbr | Locked definition | Basis |
|---|---|---|---|
| 66 | CI | Confidence interval (CI half-width = `CONF_HI_CIHW`). The continuous-integration sense is never abbreviated. | C (sense locked by you) |
| 67 | SE | Standard error of a proportion: √(p(1−p)/n) | C |
| 68 | ATE | Average treatment effect = E[Y∣T=1] − E[Y∣T=0] | C |
| 69 | DAG | Directed acyclic graph (causal graph) | C |
| 70 | TF | Term frequency (as in TF-IDF). Product-family codes are not glossary terms. | C (sense locked by you) |
| 71 | IDF | Inverse document frequency (TF-IDF) | K |
| 72 | PMI | Pointwise mutual information (term co-occurrence) | C |
| 73 | LDA | Latent Dirichlet allocation (topic model) | C |
| 74 | BERT | Transformer language model used for embeddings / intent classification | K |
| 75 | BART | Sequence-to-sequence transformer (question generation) | K |
| 76 | ABSA | Aspect-based sentiment analysis | C |
| 77 | LSTM | Long short-term memory network (sequence prediction) | K |
| 78 | ARIMA | AutoRegressive Integrated Moving Average (time-series forecasting) | C |
| 79 | STL | Seasonal-Trend decomposition using Loess | C |
| 80 | BSTS | Bayesian structural time series (CausalImpact) | C |
| 81 | PPO | Proximal policy optimization (reinforcement learning) | K |
| 82 | HITS | Hyperlink-Induced Topic Search (hub/authority scoring) | K |
| 83 | ML | Machine learning | K |
| 84 | BI | Business intelligence | K |
| 85 | SEM | Search engine marketing (umbrella for paid search incl. Amazon PPC) | K |
| 86 | SEO | Search engine optimization (on Amazon: organic listing/keyword optimization) | K |
| 87 | GEO | Generative engine optimization (visibility in AI shopping/answer engines, e.g. Alexa Shopping) | U (your edit) |

## 6. Clients

| # | Abbr | Locked definition | Basis |
|---|---|---|---|
| 88 | ENSO | Client code (28 files) | C |
| 89 | BERL | Client code (13 files) | C |
| 90 | LUND | Client code ("reused for BERL/LUND/JAYE") | C |
| 91 | JAYE | Client code | C |
| 93 | ABCD | Placeholder client code in templates (`{ABCD}`) — not a real client | C |

## 7. Your governance, versioning & scaffold codes (not Amazon knowledge — META genre)

| # | Abbr | Locked definition | Basis |
|---|---|---|---|
| 94 | AMD | Amendment ID prefix (AMD-1…AMD-5 on the SQ engine) — **not a client** | C |
| 95 | DECL | Declaration ID prefix (operator-confirmed declaration, e.g. DECL-SQP100) | C |
| 96 | CORR | Correction ID prefix (logged correction) | C |
| 97 | GOV | Governance ruling prefix (GOV-GIT-1) | C |
| 98 | NEG | Negative-keyword ruling/diagnostic prefix (NEG-REVIEW, NEG-EVIDENCE) | C |
| 99 | FUT | Future-module item prefix (FUT-PLM = placement-multiplier module) | C |
| 100 | PREV | Previous (`PREV_RUN_ARTIFACT` slot) | C |
| 101 | FA / FB / FM | Failure-mode ID prefixes in kickoff A / kickoff B / meta-generator | C |
| 102 | GB | Gate-blocker ID prefix (GB-01…) and gate B (GB-E) | C |
| 103 | GM | Guard-mode ID in the Meta-Generator (GM-4) | C |
| 104 | RT | Runtime project prefix (RT-ENSO = client runtime project) | C |
| 105 | PREP | Per-ASIN preparation phase (P2 PREP) | C |
| 106 | QA | Quality assurance (PRE-UPLOAD SOURCE QA) | C |
| 107 | MINOR | Semver bump class (MAJOR.MINOR.PATCH) | C |
| 108 | REGEN | Regeneration cascade on a source-of-truth version bump | C |
| 109 | SSOT | Single source of truth | C |
| 110 | SOP | Standard operating procedure | C |
| 111 | SOTA | State of the art | C |
| 112 | ARCH | Architecture blueprint (ARCH-BLUEPRINT) | C |
| 113 | AMZ | Amazon (as in "AMZ Clever") | K |
| 114 | DTPRF | Decision-Theoretic PPC Reporting Framework (RPT-07) | C |
| 115 | PPT | Universal Report **P**PC **P**rompt **T**emplate (v3.x), paired with PIT | G |
| 116 | SHOW / SKELETON / GUARD | Disclosure levels: full · structure only · existence only (now `disclosure_level`) | C |
| 117 | ENG, RPT, ARC, BUD, FMT, GRD, STR, TIER | PPC Artifact Vault ID prefixes: automation engine · reporting · architecture · budget · ad formats · guard layer · strategy · SKU tiering | C |
| 118 | REF, PROC, PROTO, MAP, IDX, VLT, META, CORE | Your namespace/type codes in `CORE.PPC.REF.X.v1` IDs (IDX = index, VLT = vault). Now governed by the glossary genre list | C |
| 119 | KB | Knowledge base (namespace: research/knowledge acquisition) | C |
| 120 | LLM | Large language model | K |
| 121 | MVP | Minimum viable product | K |
| 122 | QBR | Quarterly business review | K |
| 123 | FAQ | Frequently asked questions | K |
| 124 | Q&A | Question and answer | K |
| 125 | PR | Pull request (git). The public-relations sense is never abbreviated. | C (sense locked by you) |
| 126 | OS | Operating system ("Agent-OS") | C |
| 127 | ISO | ISO-8601 dates / ISO weeks | C |
| 128 | SUN / MON / SAT | Weekday bounds in `WEEK_CONVENTION` (SUN-SAT default, US) | C |
| 129 | YYYY | Date-format placeholder | C |

## 8. File, data & tooling terms

| # | Abbr | Locked definition | Basis |
|---|---|---|---|
| 130 | API | Application programming interface | K |
| 131 | CLI | Command-line interface | K |
| 132 | UI | User interface | K |
| 133 | SQL | Structured Query Language | K |
| 134 | PK / FK | Primary key / foreign key | K |
| 135 | ENUM | Enumeration (closed list of allowed values) | K |
| 136 | XLS | Excel workbook | K |
| 137 | XOR | Exclusive or ("custom instructions XOR project file — never both") | C |
| 138 | CRLF | Windows line ending (carriage return + line feed) | C |
| 139 | BOM | Byte-order mark at the start of a CSV header | C |
| 140 | ASCII | 7-bit character set; your generated text is ASCII-only | C |
| 141 | ISBN | International Standard Book Number (routes to product-target sidecar) | C |
| 142 | NA | Not applicable | C |
| 143 | README | Readme file (reference only) | U (your edit) |

## 9. Core Amazon terms

| # | Abbr | Locked definition | Basis |
|---|---|---|---|
| 147 | ASIN | Amazon Standard Identification Number | K |
| 148 | SKU | Stock keeping unit (seller's own ID) | K |
| 149 | SB / SBV | Sponsored Brands / Sponsored Brands Video | K |
| 150 | SD / SDV | Sponsored Display / Sponsored Display Video | K |
| 151 | CVR | Conversion rate = orders ÷ clicks | K |
| 152 | ACoS | Advertising cost of sale = ad spend ÷ ad-attributed sales | K |
| 153 | TACoS | Total ACoS = ad spend ÷ total (ad + organic) sales | K |
| 154 | STR | Search Term Report. Legacy vault IDs such as `STR-02` are opaque aliases, not uses of this abbreviation. | C (sense locked by you) |
| 155 | ROS | Rest of search (placement) | K |
| 156 | ToFu / MoFu / BoFu | Funnel stages = awareness / consideration / conversion (WR-023) | C |
