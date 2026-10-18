---
id: PPC-REF-001
title: "Account structure philosophies"
aliases: [PPC-REF-001, ARC-01]
genre: REF
entity_types: [Framework]
domain: PPC
page_status: seed
prov_tag: U
evidence_scope: global
sources: [SRC-0001]
recorded: 2026-10-18
disclosure_level: SHOW
classification: internal
producer: llm
page_version: 0.2.0
schema_version: 0.2.2
review_cadence: P3M
tool_surface: [Optmyzr:rule-engine]
relationships:
  feeds: ["[[architecture-matrix-philosophy-funnel-tier|ARC-02]]", "[[STR-04]]"]
  implemented_by: ["[[optmyzr|Tool]]"]
---

# Account structure philosophies

## Definition
An account-structure philosophy is a rule for how campaigns and ad groups are cut. It decides which segment of the account each philosophy governs.

## Claims

| Philosophy          | Data density         | Control           | Mgmt overhead | AI learning speed          | Best fit                                 | claim                                       |
| ------------------- | -------------------- | ----------------- | ------------- | -------------------------- | ---------------------------------------- | ------------------------------------------- |
| Granular (SKAG/SAG) | Low (fragmented)     | Max               | Very high     | Slow                       | Hero ASIN, top 5–10 money keywords       | `prov: U \| scope: global \| src: SRC-0001` |
| Hagakure            | High (consolidated)  | Low               | Low           | Fast                       | Long-tail catalogs, automated bidding    | `prov: U \| scope: global \| src: SRC-0001` |
| STAG                | Medium               | Medium            | Medium        | Medium                     | Established brands, themed clusters      | `prov: U \| scope: global \| src: SRC-0001` |
| Atomic waterfall    | Variable by sku_tier | High at exact     | High          | Fast (auto) / slow (exact) | New launches, keyword harvesting         | `prov: U \| scope: global \| src: SRC-0001` |
| Rainbow             | Varies (tiered)      | Financial control | Medium        | n/a (reporting overlay)    | P&L-driven accounts, agency reporting    | `prov: U \| scope: global \| src: SRC-0001` |
| Catch-all           | Very low             | Minimal           | Very low      | n/a                        | Long-tail capture, inventory liquidation | `prov: U \| scope: global \| src: SRC-0001` |

## Rationale
Source: whiteboard capture (`img16/batch1`, deck slide S11). No evidence beyond the capture.

## See also
- [[atomic-waterfall-harvesting|PPC-PROC-001]]
- [[portfolio-pattern-by-catalog-size|PPC-DECRULE-001]]
- [[bidding-posture|PPC-REF-002]]
