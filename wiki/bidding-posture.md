---
id: PPC-REF-002
title: "Bidding posture"
aliases: [PPC-REF-002]
genre: REF
entity_types: [Framework, CampaignSetting]
domain: PPC
page_status: seed
prov_tag: U
evidence_scope: global
sources: [SRC-0006]
recorded: 2026-10-18
producer: llm
page_version: 0.2.0
schema_version: 0.2.2
---

# Bidding posture

## Definition
Bidding posture is the account's overall risk stance across campaign settings, bids and budgets. `prov: U | scope: global | src: SRC-0006`

## Claims

| Element          | Aggressive                                    | Balanced                                   | Conservative                                     | claim                                       |
| ---------------- | --------------------------------------------- | ------------------------------------------ | ------------------------------------------------ | ------------------------------------------- |
| Objective        | Max impressions, top-of-search share          | Stable impression share, TACoS in corridor | Minimize waste, protect contribution margin      | `prov: U \| scope: global \| src: SRC-0006` |
| Bidding strategy | Dynamic up & down / manual high               | Rule-engine or target-ROAS caps            | Dynamic down only / fixed low                    | `prov: U \| scope: global \| src: SRC-0006` |
| TOS modifier     | High (+100% to +300%)                         | Modest, proven placements only             | Minimal or 0%                                    | `prov: U \| scope: global \| src: SRC-0006` |
| Match types      | Broad / phrase / auto                         | Mixed, harvest + test                      | Exact dominant, strict negatives                 | `prov: U \| scope: global \| src: SRC-0006` |
| Bid targets      | Low ROAS threshold / high ACoS ceiling        | Corridor                                   | High ROAS / low ACoS                             | `prov: U \| scope: global \| src: SRC-0006` |
| Budget           | Uncapped or aggressive reallocation           | —                                          | not stated in source                             | `prov: U \| scope: global \| src: SRC-0006` |
| Use case         | Launch, Prime Day, brand defense, rank pushes | Steady state                               | Stock risk, mature SKUs, low margin, budget cuts | `prov: U \| scope: global \| src: SRC-0006` |

## Rationale
Generic explanatory text; producer unknown, treated as LLM-derived. No account evidence.

## See also
- [[account-structure-philosophies|PPC-REF-001]]

## Open questions
- SRC-0006: the source table has Aggressive and Conservative columns only; Balanced cells come from the body text.
- SRC-0006: Budget row — the Conservative cell is empty in the source and the body states no Balanced budget rule.
