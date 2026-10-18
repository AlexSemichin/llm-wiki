---
id: LST-TECH-001
title: "Click-side vs cart-side gap diagnosis"
aliases: [LST-TECH-001]
genre: TECH
entity_types: [Metric, ASIN]
domain: LST
page_status: seed
prov_tag: U
evidence_scope: global
sources: [SRC-0008]
recorded: 2026-10-18
producer: llm
page_version: 0.2.1
schema_version: 0.2.2
---

# Click-side vs cart-side gap diagnosis

## Purpose
Locate where a listing loses shoppers on a search query, then route the fix to the right listing elements.

## Formula/Algorithm

| Gap        | Funnel step        | Signal                                                              | Levers                                                                           | claim                                       |
| ---------- | ------------------ | ------------------------------------------------------------------- | -------------------------------------------------------------------------------- | ------------------------------------------- |
| Click-side | impression → click | clickIndex (CTR Index) = ASIN CTR ÷ query_market_rate               | main image, price, title, rating/review count, badges, Prime                     | `prov: U \| scope: global \| src: SRC-0008` |
| Cart-side  | click → cart add   | cartIndex (Cart-Add Index) = ASIN cart-add rate ÷ query_market_rate | secondary images, bullets, A+, coupons, delivery speed, stock, variation clarity | `prov: U \| scope: global \| src: SRC-0008` |

## Parameters
| Parameter            | Value                      |
| -------------------- | -------------------------- |
| click-side threshold | clickIndex < 0.60 (WR-047) |
| cart-side threshold  | cartIndex < 1.0            |

## Claims
- A row is click-side when clickIndex (CTR Index) < 0.60. `prov: U | scope: global | src: SRC-0008 | supersedes: ^c-02` ^c-01
- A row is click-side when CTR Index < 1.0. `prov: U | scope: global | src: SRC-0008 | valid: ..2026-10-18` ^c-02
- A row is cart-side when cartIndex (Cart-Add Index) < 1.0. `prov: U | scope: global | src: SRC-0008`
- Applying a cart-side formula to a click-side row prescribes detail-page fixes that do not address why shoppers don't click. `prov: U | scope: global | src: SRC-0008`

## Used by
- [[fix-value-formula-by-subclass|PPC-DEC-002]]

## Open questions
- SRC-0008 states two click-side thresholds (0.60 and 1.0). Resolved by WR-047 (Alex): 0.60 holds; ^c-02 closed 2026-10-18. Raw source untouched.
