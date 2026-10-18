---
id: PPC-DEC-002
title: "Decision: Fix value formula per subclass"
aliases: [PPC-DEC-002]
genre: DEC
entity_types: [SearchTerm, Metric]
domain: PPC
page_status: seed
prov_tag: U
evidence_scope: entity_only
sources: [SRC-0008]
recorded: 2026-10-18
producer: llm
page_version: 0.2.0
schema_version: 0.2.2
decision_date: 2026-09-30
date_source: file_mtime
relationships:
  uses_technique: ["[[click-vs-cart-gap-diagnosis|LST-TECH-001]]"]
---

# Decision: Fix value formula per subclass

## Date
On or before 2026-09-30 (file date; engine v1.2 amendment).

## Decision
- `FIX/CARTSIDE` keeps `min(myDemand × (1/cartIndex − 1), 1.5 × myDemand)`. `prov: U | scope: global | src: SRC-0008`
- `FIX/CLICKSIDE` uses `min(myDemand × (1/clickIndex − 1), 1.5 × myDemand)`; clickside means clickIndex < 0.60, so the value is ≥ +0.67 × myDemand. `prov: U | scope: global | src: SRC-0008`

## Alternatives rejected
- A $0 floor — would value a listing losing 40–90% of expected clicks at zero. `prov: U | scope: global | src: SRC-0008`

## Rationale
- Root cause: the Fix formula measured the cart-side gap on click-side rows. `prov: U | scope: global | src: SRC-0008`

## Outcome
- 14 click-side rows: $1,140 → $2,315; 2 negative rows → +$91 and +$40; 'sand tray therapy kit' $25 → $252 (cartIndex 0.93, clickIndex 0.59). `prov: U | scope: entity_only | src: SRC-0008 | flag: client_unknown`

## Open questions
- Client account not named in source.
- `myDemand` is not defined in SRC-0008.
