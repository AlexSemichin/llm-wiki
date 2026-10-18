# T1 FRONTMATTER SPEC v0.1 [A1,A4,A8]

status: CANDIDATE | date: 2026-10-15 | terms: claude/T1_glossary_amazon_v0.1.md

## 1. Principles

- Metadata lives in frontmatter only. No footer metadata blocks. (E-D1)
- Store only fields that query or lint reads, or that provenance requires.
- Derived values are computed, never stored: backlinks, folder subtree, index_state, last_indexed. (E-D2, E-D5)
- Target: body ≥ 50% of page bytes.

## 2. Wiki page (wiki_layer wiki — written by Claude)

```yaml
id: PPC-ARC-001            # stable; never reused, never changed
title: "Account Structure Philosophies — Comparative Matrix"
aliases: [PPC-ARC-001, ARC-01]   # every legacy ID kept for search
genre: REF                 # §2 of glossary
entity_types: [AccountStructurePhilosophy]
domain: ppc-sp
page_status: seed          # seed | candidate | promoted | superseded
superseded_by:             # id; required when page_status = superseded
prov_tag: U                # COMPUTED by lint = lowest prov_tag of load-bearing claims
evidence_scope: global     # entity_only | domain | global
sources: [raw/ppc-vault/account-structure-philosophies-matrix.md]
valid_from:                # when the content was true in the world (blank = unknown)
valid_to:
recorded: 2026-10-15       # when the wiki recorded it
verified_by:               # V1 | V2 | V3 — required for prov_tag V
verified_on:
disclosure_level: SHOW
classification: internal   # internal | confidential | external-safe
experimental: false
page_version: 0.1.0
schema_version: 0.1.0
relationships:
  depends_on: []
  feeds: []
  related: []
  uses_technique: []
  implemented_by: []       # Tool entity ids (E-D9)
tags: []
```

Claim-level fields (`causal_level`, `autonomy_level`, `method_class`, per-claim `prov_tag`) sit inline on the claim line. The syntax is decided in the P2 subject pack.

## 3. Raw capture (wiki_layer raw — stamped by you when saving any LLM session output)

```yaml
capture_id: CAP-2026-10-15-01
captured: 2026-10-15
source_type: llm-session   # llm-session | article | export | whiteboard-image | note | transcript
producer: llm              # human | llm | mixed
llm: claude-opus-5-5       # as shown in the app
session_ref: "<chat title or URL>"
project: "<Claude project name>"
domain_hint: ppc-sp
contains_client_data: false
classification: internal
```

Rules:

- Every capture with `producer: llm` or `producer: mixed` enters at prov_tag U.
- A capture with producer llm never counts as the sole evidence for prov_tag V.
- A capture with `contains_client_data: true` stays in T2 until anonymized.
- Minimum you must fill: captured, source_type, producer, session_ref, contains_client_data. Claude fills the rest at ingest.