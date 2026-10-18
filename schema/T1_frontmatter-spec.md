---
id: WIKI-META-003
title: "T1 Frontmatter Spec"
genre: META
page_status: promoted
page_version: 0.2.0
schema_version: 0.2.2
recorded: 2026-10-18
promoted: 2026-10-18 (WR-055)
producer: llm
---

# T1 Frontmatter Spec v0.2 [A1, A4, A8]

terms: `schema/T1_glossary_amazon.md` · claim syntax: pack §5.1 · lint: pack §9
v0.2 changes (pack §10): §2 uses pack domain codes and registry IDs; adds `producer` and the 5 pack §5.2 fields; v0.1 §3 (raw capture stamp) retired by WR-040 — raw sources get a row in `_meta/source-registry.csv` instead.

## 1. Principles

- Metadata lives in frontmatter only. No footer metadata blocks. (E-D1)
- Store only fields that query or lint reads, or that provenance requires.
- Derived values are computed, never stored: backlinks, folder subtree, index_state, last_indexed. (E-D2, E-D5)
- Target: body ≥ 50% of page bytes.

## 2. Wiki page (wiki_layer wiki — written by Claude)

```yaml
id: PPC-REF-001            # pack §2: {DOMAIN}-{GENRE}-{NNN}; never reused, never changed
title: "Account structure philosophies"
aliases: [PPC-REF-001, ARC-01]   # every legacy ID kept for search
genre: REF                 # glossary §2
entity_types: [Framework]  # pack §3
domain: PPC                # pack §1 code
page_status: seed          # seed | candidate | promoted | superseded
superseded_by:             # id; required when page_status = superseded
prov_tag: U                # COMPUTED by lint = lowest prov of the page's claims
evidence_scope: global     # entity_only | domain | global
sources: [SRC-0001]        # registry src_id values
valid_from:                # when the content was true in the world (blank = unknown)
valid_to:
recorded: 2026-10-18       # when the wiki recorded it
producer: llm              # human | llm | mixed
verified_by:               # V1 | V2 | V3 — required for prov_tag V
verified_on:
disclosure_level: SHOW
classification: internal   # internal | confidential | external-safe
experimental: false
project_tier: T1           # T1 | T2; T2 required when entity_types includes Client
review_cadence: P3M        # ISO 8601 duration or on_event (optional)
tool_surface: [Optmyzr:rule-engine]   # optional
decision_date:             # YYYY-MM-DD; required for genre DEC
date_source:               # stated | file_mtime; required for genre DEC
page_version: 0.1.0
schema_version: 0.2.2
relationships:
  depends_on: []
  feeds: []
  related: []
  uses_technique: []
  implemented_by: []       # Tool entity ids (E-D9)
tags: []
```

## 3. Required fields (lint L-02)

| Scope                        | Required fields                                                                                                            |
| ---------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| every page                   | id, title, genre, domain, page_status, prov_tag, evidence_scope, sources, recorded, producer, page_version, schema_version |
| genre DEC                    | decision_date, date_source                                                                                                 |
| entity_types includes Client | project_tier                                                                                                               |
| page_status superseded       | superseded_by (lint L-10)                                                                                                  |
| prov_tag V                   | verified_by (lint L-06)                                                                                                    |

Claim-level fields (`prov`, `scope`, `src`, `valid`, `causal`, `autonomy`, `method`, `flag`, `supersedes`) sit inline on the claim line (pack §5.1).
