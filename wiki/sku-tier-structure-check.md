---
id: PPC-DIAG-001
title: "SKU tier vs campaign structure check"
aliases: [PPC-DIAG-001, ARC-08]
genre: DIAG
entity_types: [SKU, Campaign]
domain: PPC
page_status: seed
prov_tag: U
evidence_scope: global
sources: [SRC-0005]
recorded: 2026-10-18
disclosure_level: SHOW
classification: internal
producer: llm
page_version: 0.2.0
schema_version: 0.2.2
review_cadence: P3M
tool_surface: [Optmyzr:rule-engine]
relationships:
  depends_on: ["[[TIER-01]]"]
  feeds: ["[[recipe-vs-campaign-fork|ARC-07]]"]
---

# SKU tier vs campaign structure check

## Input state
A recommended campaign structure and the SKU's sku_tier.

## Checks

| Check                      | Severity | Rule                                                                               | claim                                       |
| -------------------------- | -------- | ---------------------------------------------------------------------------------- | ------------------------------------------- |
| Structure matches sku_tier | WARN     | A = granular per-SKU / per-match-type · B = consolidated ad groups · C = catch-all | `prov: U \| scope: global \| src: SRC-0005` |

## Verdict rules
- WARN, not BLOCK: the structure still runs; it wastes overhead or starves a hero SKU. `prov: U | scope: global | src: SRC-0005`
- The check proposes the sku_tier-correct structure inline and does not rewrite. `prov: U | scope: global | src: SRC-0005 | autonomy: recommend`

## Open questions
- Source calls this "gate check #6" and cites "§5.3": the parent check list and document are not in the vault scan.

## See also
- [[campaign-naming-convention|PPC-DATASPEC-001]]
