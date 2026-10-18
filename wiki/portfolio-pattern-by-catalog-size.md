---
id: PPC-DECRULE-001
title: "Portfolio pattern by catalog size"
aliases: [PPC-DECRULE-001, ARC-06]
genre: DECRULE
entity_types: [AdsPortfolio, SKU]
domain: PPC
page_status: seed
prov_tag: U
evidence_scope: global
sources: [SRC-0004]
recorded: 2026-10-18
disclosure_level: SHOW
classification: internal
producer: llm
page_version: 0.2.0
schema_version: 0.2.2
review_cadence: P3M
tool_surface: [Optmyzr:rule-engine]
relationships:
  feeds: ["[[BUD-01]]"]
---

# Portfolio pattern by catalog size

## IF
Catalog size (count of active SKUs) falls in one band below.

## THEN

| Catalog size | Portfolio pattern                                                | Rationale                                                             | claim                                                                                        |
| ------------ | ---------------------------------------------------------------- | --------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| ≤ 20 SKUs    | Hero-SKU portfolios + Rainbow tier for B/C SKUs                  | portfolio visibility in the Amazon Ads UI; portfolio count manageable | `prov: U \| scope: global \| src: SRC-0004 \| autonomy: recommend \| flag: autonomy_default` |
| 20–80 SKUs   | Hero-SKU portfolio for sku_tier A (10–15) + Rainbow tier for B/C | Best of both                                                          | `prov: U \| scope: global \| src: SRC-0004 \| autonomy: recommend \| flag: autonomy_default` |
| 80–200 SKUs  | Rainbow tier only                                                | Hero-SKU multiplication becomes unsustainable                         | `prov: U \| scope: global \| src: SRC-0004 \| autonomy: recommend \| flag: autonomy_default` |
| 200+ SKUs    | Rainbow tier + product-group reporting                           | Portfolio cap (~8) — overhead dominates                               | `prov: U \| scope: global \| src: SRC-0004 \| autonomy: recommend \| flag: autonomy_default` |

## autonomy
recommend — default; the source states none.

## hard_constraints
None stated in source.

## See also
- [[account-structure-philosophies|PPC-REF-001]]
