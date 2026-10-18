---
id: PPC-PROC-001
title: "Atomic waterfall keyword harvesting"
aliases: [PPC-PROC-001, ARC-03]
genre: PROC
entity_types: [Framework, Campaign, SearchTerm]
domain: PPC
page_status: seed
prov_tag: U
evidence_scope: global
sources: [SRC-0002]
recorded: 2026-10-18
disclosure_level: SKELETON
classification: internal
producer: llm
page_version: 0.2.1
schema_version: 0.2.2
review_cadence: P3M
tool_surface: [Optmyzr:rule-engine]
relationships:
  feeds: ["[[ENG-03]]"]
  related: ["[[RPT-01]]"]
  implemented_by: ["[[optmyzr|Tool]]"]
---

# Atomic waterfall keyword harvesting

## Trigger
A new launch or an account that needs systematic keyword harvesting.

## Inputs
- Search terms from discovery campaigns.
- Target ACoS per ASIN.
- category_benchmark_rate (CVR) for the ASIN's own category.

## Steps
1. Run harvest_stage **discovery**: auto (LOOSE, CLOSE, SUBST, COMP) and broad GENE campaigns.
2. Graduate a term to **validation** after >3 orders or ACoS ≤ target × 1.2, over 14–28 days. `prov: U | scope: global | src: SRC-0002`
3. Run harvest_stage **validation**: manual phrase, mid bid.
4. Graduate a term to **scale** after ≥5 orders and the ASIN's actual CVR > category_benchmark_rate (CVR). `prov: U | scope: global | src: SRC-0002`
5. Run harvest_stage **scale**: manual exact, aggressive bid, RANK / high-volume GENE.
6. At every graduation, add the graduated term as negative exact in the discovery campaigns, for all graduated terms at once. `prov: U | scope: global | src: SRC-0002`

## Outputs
- Exact-match scale campaigns with proven terms.
- Negative-exact lists in discovery campaigns.

## Failure modes
- Cannibalization when step 6 is skipped.

## Open questions
- SRC-0002: the report or tool that supplies category_benchmark_rate is not stated. Meaning resolved by WR-062.

## See also
- [[account-structure-philosophies|PPC-REF-001]]
