---
id: PPC-DEC-001
title: "Decision: confidence rule P-12 v2"
aliases: [PPC-DEC-001]
genre: DEC
entity_types: [Metric, SearchTerm]
domain: PPC
page_status: seed
prov_tag: U
evidence_scope: entity_only
sources: [SRC-0007]
recorded: 2026-10-18
producer: llm
page_version: 0.2.0
schema_version: 0.2.2
decision_date: 2026-09-23
date_source: file_mtime
---

# Decision: confidence rule P-12 v2

## Date
On or before 2026-09-23 (file date; source states none).

## Decision
Adopt the hybrid standard-error rule from [[rate-confidence-classing|MEAS-TECH-001]] as P-12 v2 in the search query engine. `prov: U | scope: entity_only | src: SRC-0007 | flag: client_unknown`

## Alternatives rejected
- `MAX`/`MIN`/`AVG` thresholds — outlier-dominated. `prov: U | scope: global | src: SRC-0007`
- Percentile/tertile classes — jumpy at n = 36–63 queries per family; drift run to run. `prov: U | scope: entity_only | src: SRC-0007 | flag: client_unknown`

## Rationale
- Sample: 693 clicks at rank 1, median ~15 clicks per term. `prov: U | scope: entity_only | src: SRC-0007 | flag: client_unknown`

## Outcome
- Backtest reproduced High/Medium/Low on 27 of 29 spot-checked rows; 2 divergences were Low→Medium on ~15-click rows. `prov: U | scope: entity_only | src: SRC-0007 | flag: client_unknown`

## Open questions
- Which client account produced the sample?
