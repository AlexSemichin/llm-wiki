---
id: MEAS-TECH-001
title: "Rate confidence classing by standard error"
aliases: [MEAS-TECH-001]
genre: TECH
entity_types: [Metric]
domain: MEAS
page_status: seed
prov_tag: U
evidence_scope: global
sources: [SRC-0007]
recorded: 2026-10-18
producer: llm
page_version: 0.2.0
schema_version: 0.2.2
relationships:
  related: ["[[confidence-rule-p12-v2|PPC-DEC-001]]"]
---

# Rate confidence classing by standard error

## Purpose
Classify how much to trust a rate (CVR, CTR, an index) by its sampling error, not by raw click counts.

## Formula/Algorithm
- SE = √(p(1−p)/n), p = observed rate, n = clicks. `prov: D | scope: global | src: SRC-0007`
- CI half-width = z · SE. `prov: D | scope: global | src: SRC-0007`
- `HIGH` if CI half-width ÷ p ≤ 25% and both halves published; `LOW` if > 60% or a half unpublished; else `MEDIUM`. `prov: U | scope: global | src: SRC-0007`

## Parameters
| Parameter        | Value                |
| ---------------- | -------------------- |
| z                | not stated in source |
| `HIGH` threshold | 25%                  |
| `LOW` threshold  | 60%                  |

## Claims
- Min/max are outlier artifacts; the mean is distorted by heavy-tailed click distributions. `prov: U | scope: global | src: SRC-0007`
- Percentile classes drift run to run and break delta comparisons. `prov: U | scope: global | src: SRC-0007`

## Used by
- [[confidence-rule-p12-v2|PPC-DEC-001]]

## Open questions
- SRC-0007: which z (which confidence percentage)?
