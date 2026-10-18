---
id: WIKI-DATASPEC-001
title: "T1 Subject Pack — Amazon (schema)"
genre: DATASPEC
page_status: candidate
page_version: 0.1.0
schema_version: 0.1.0
recorded: 2026-10-18
producer: llm
depends_on: [T1_glossary_amazon_v0.1, T1_abbreviation-definitions_v0.2, T1_frontmatter-spec_v0.1]
---

# T1 Subject Pack — Amazon v0.1

PURPOSE — Define what can exist in the Amazon LLM wiki (domains, entity types, edges, claims), how pages are identified and shaped, and which deterministic checks every page must pass. [A3, A7]

Terms resolve in `T1_glossary_amazon_v0.1`. Abbreviations resolve in `T1_abbreviation-definitions_v0.2`.

---

## 1. Domain axis (14) [A2]

The domain list unites the 10 underweighted domains (Inputs) and the 6 core domains (I-F12). Two merges reduce 16 to 14: "creative listing optimization" merges into LST; "FBA logistics & reimbursements" merges into INV.

| Code | Domain | In scope |
|---|---|---|
| PPC | Amazon advertising | SP, SB, SBV, SD, SDV, DSP: structure, bidding, targeting, harvesting, automation |
| LST | Listing & search visibility | Titles, bullets, backend terms, images, A+, keyword research, organic rank |
| CTLG | Catalog & brand | Brand Registry, variations, browse nodes, catalog data |
| INV | Inventory & fulfillment | Replenishment, lead times, IPI, FBA/FBM/AWD, reimbursements, stranded inventory |
| VOC | Reviews & customer voice | Ratings, reviews, returns reasons, Q&A |
| OFF | Off-Amazon traffic | External ads aimed at Amazon growth, attribution, brand referral |
| ECON | Unit economics | Contribution margin, fees, P&L, break-even ACoS |
| HLTH | Account health & policy | Violations, appeals, reinstatement, compliance |
| INTEL | Competitor intelligence | How intel is gathered, structured, acted on |
| CUST | Customer lifecycle | Repeat purchase, cohorts, LTV/CAC, NTB |
| LNCH | Launch sequencing | Honeymoon mechanics, velocity ramp, review seeding |
| PRCE | Pricing | MAP, repricing triggers, floor and ceiling logic, deals |
| AGCY | Agency account operations | SOPs for running an Amazon account only (WR-004) |
| MEAS | Measurement & reporting | Metric definitions, report specs, dashboards |
| WIKI | The wiki itself | Pages about the wiki (genre META only) |

Note: WIKI is a housekeeping domain, not a subject domain. Subject domain count = 14.

## 2. Page ID scheme [A8] (WR-028)

- Format: `{DOMAIN}-{GENRE}-{NNN}`, e.g. `PPC-REF-001`.
- NNN is a 3-digit counter per DOMAIN+GENRE pair, never reused.
- Filenames are slugs. The `id` and every legacy ID go into `aliases`.
- Links are written `[[slug|ID]]`.
- Legacy IDs (`ARC-01`, `CORE.PPC.REF.X.v1`, `STR-02`) are opaque alias strings. They are outside the term lock.

## 3. Entity types (L1) [A3]

Every page declares ≥1 entity type in `entity_types`.

| Group | Entity type | Key attributes |
|---|---|---|
| Catalog | Brand | name, own (bool) |
| Catalog | Product | parent ASIN, variation theme |
| Catalog | ASIN | asin, sku_tier |
| Catalog | SKU | sku |
| Catalog | Category | browse node id, path |
| Ads | AdProgram | SP · SB · SBV · SD · SDV · DSP |
| Ads | Campaign | naming code, state |
| Ads | AdGroup | — |
| Ads | AdsPortfolio | budget cap |
| Ads | Target | kind: keyword · asin · category · audience · auto_group |
| Ads | SearchTerm | text |
| Ads | Placement | TOS · ROS · PDP |
| Ads | CampaignSetting | name (every CampaignSetting is a lever) |
| Ads | IntentSegment | code (BRAN, DEF, GENE, RANK, COMP, ATT, CROS, CAT, EVNT) |
| Ads | Audience | code |
| Ads | FunnelStage | tofu · mofu · bofu · retention (WR-023) |
| Market | Competitor | brand, ASINs |
| Market | Marketplace | code |
| Economics | Metric | formula, metric_class (effectiveness · efficiency · governance) |
| Economics | Dimension | values |
| Economics | Fee | type |
| Economics | Price | type |
| Operations | InventoryPool | AFN · AWD · inbound |
| Governance | AmazonPolicy | source URL, effective date |
| Governance | HealthSignal | metric, threshold |
| Knowledge | Framework | named method or philosophy (Hagakure, STAG, Pearl ladder) |
| Knowledge | Report | Amazon report source (SQP, Search Term Report, Business Report) |
| External | Tool | vendor (Optmyzr, Helium10…) |
| External | Channel | off-Amazon traffic channel |
| Tier 2 | Client | client code; every claim about it is `entity_only` (WR-027) |

## 4. Edge types (L1) [A3]

| Edge | Domain → Range | Relation class |
|---|---|---|
| has_variation | Product → ASIN | composition |
| sold_as | ASIN → SKU | dependency |
| belongs_to | ASIN → Category | inheritance |
| owned_by | ASIN → Brand | dependency |
| advertises | Campaign → ASIN | dependency |
| contains | Campaign → AdGroup; AdGroup → Target | composition |
| member_of | Campaign → AdsPortfolio | composition |
| runs_on | Campaign → AdProgram | dependency |
| aims_at | Target → SearchTerm · ASIN · Category · Audience | dependency |
| serves_stage | Campaign · IntentSegment → FunnelStage | dependency |
| has_setting | Campaign → CampaignSetting | composition |
| measured_by | any → Metric | dependency |
| sliced_by | Metric → Dimension | dependency |
| computed_from | Metric → Metric | transformation |
| competes_with | ASIN → ASIN; Brand → Brand | dependency |
| governed_by | any → AmazonPolicy | dependency |
| implemented_by | Framework · page → Tool | dependency |
| sourced_from | Metric · page → Report | dependency |
| uses_technique | PROC page → TECH page | dependency |
| instance_of | Client-scoped page → Framework | inheritance |
| supersedes | page → page | transformation |

### Mutually exclusive predicate groups (C5) — conflict detected at write time

| Group | Predicates (same ordered pair, same valid time) | Example |
|---|---|---|
| PG-1 Eligibility | eligible_for · restricted_from | ASIN × AdProgram |
| PG-2 Effect direction | increases · decreases | CampaignSetting × Metric |
| PG-3 Ownership | own_asset · competitor_asset | ASIN × Brand |
| PG-4 Product relation | complements · substitutes | ASIN × ASIN (CROS vs ATT routing) |

A new claim that asserts one predicate where the other already holds closes the older claim (`valid_to` set) and links both by `supersedes`. Nothing is deleted.

## 5. Claim line syntax (L2) [A4]

Every load-bearing statement in a wiki page is one bullet ending in one code span:

```
- Graduate a term from discovery to validation after >3 orders or ACoS ≤ target × 1.2 over 14–28 days. `prov: U | scope: global | src: SRC-0012 | causal: association`
```

| Field | Values | Required |
|---|---|---|
| prov | V · D · U · X | yes |
| scope | entity_only · domain · global | yes |
| src | ≥1 source-registry ID, comma-separated | yes |
| valid | `YYYY-MM-DD..YYYY-MM-DD`, open ends allowed | no |
| causal | association · intervention · counterfactual | only for causal claims |
| autonomy | inform · recommend · execute_report · delegate | only in DECRULE pages |
| method | expert_opinion · extrapolation · econometric · data_multivariate · intentions · role_play | only in TECH/REF forecasting claims |

Exception subclass DERIVED-CLAIM — trigger: Claude derives the claim from ≥2 claims with prov V. Rule: set `prov: D` and list the source claims' src IDs.

## 6. Genre body templates (L2) [A7]

Each page = frontmatter + exactly the sections listed for its genre, in order.

| Genre | Body sections |
|---|---|
| REF | Definition · Claims · Rationale · See also |
| PROC | Trigger · Inputs · Steps (numbered) · Outputs · Failure modes · See also |
| TECH | Purpose · Formula/Algorithm · Parameters · Claims · Used by · See also |
| DATASPEC | Structure (table) · Field rules · Example · See also |
| MAP | Relations (table: from · edge · to) · See also |
| META | Rule · Rationale |
| TEMPL | Use when · Template (fenced block) · Slots |
| DIAG | Input state · Checks (table: check · severity WARN/BLOCK · threshold) · Verdict rules · See also |
| CASE | Client · Window · Situation · Action · Result · Lessons (all claims entity_only) |
| GLOSS | Terms (table: term · definition · src) |
| DEC | Date · Decision · Alternatives rejected · Rationale · Outcome |
| DECRULE | IF (conditions) · THEN (action) · autonomy · hard_constraints · Claims · See also |

## 7. Source registry (W-ISS-19) [A4, A8]

Raw notes stay untouched. Their metadata lives in `_meta/source-registry.csv`.

| Column | Meaning |
|---|---|
| src_id | `SRC-0001`… never reused |
| path | vault-relative path of the raw note or file |
| silo | obsidian · gdrive · notion · mac-disk · apple-notes |
| source_type | note · llm-session · article · export · whiteboard-image · transcript |
| producer | human · llm · mixed |
| captured | file date (mtime) |
| sha256 | content hash at registration |
| bytes | size |
| domain_hint | one domain code |
| genre_hint | one genre code |
| contains_client_data | true · false |
| client_code | ENSO · BERL · LUND · JAYE · blank |
| legacy_ids | `|`-separated |
| state | registered · ingested · excluded |
| wiki_pages | `|`-separated page IDs built from it |

Rule: a source with `producer: llm` or `mixed` never supports `prov: V` on its own.
Rule: a sha256 change marks the source `registered` again (re-ingest due).

## 8. index.md and log.md [A8]

- `index.md`: grouped by domain, then genre. One line per page: `- [[slug|ID]] — one-line summary · prov · page_status`.
- `log.md`: append-only. Entry header: `## [YYYY-MM-DD] op | title`. Ops: ingest · query · lint · schema · rename · supersede.

## 9. Lint rules (deterministic, V1) [A4, A6]

| ID | Check | On fail | Auto-fix |
|---|---|---|---|
| L-01 | Frontmatter fence intact: line 1 = `---`, a closing `---` exists | BLOCK | no |
| L-02 | Required frontmatter fields present | BLOCK | no |
| L-03 | `id` unique and matches §2 pattern | BLOCK | no |
| L-04 | Every `[[link]]` resolves to a file | WARN | no |
| L-05 | Duplicate links in one page | WARN | yes, keep first |
| L-06 | `prov: V` only with `verified_by` ∈ {V1, V2, V3} | BLOCK | no |
| L-07 | Every claim line carries prov, scope, src | BLOCK | no |
| L-08 | Every src ID exists in the registry | BLOCK | no |
| L-09 | Page `prov_tag` = lowest claim prov | — | yes (computed) |
| L-10 | `page_status: superseded` requires `superseded_by` | BLOCK | no |
| L-11 | Banned bare words (layer, tier, stage, level) and abbreviations absent from definitions v0.2 | WARN | no |
| L-12 | A `scope: global` claim cites no source whose claims are all entity_only | WARN | no |
| L-13 | DECRULE claims carry `autonomy` | BLOCK | no |
| L-14 | The word "driver" requires `causal` ≥ intervention | WARN | no |
| L-15 | Page has ≥1 inbound link (except index targets) | WARN | no |

Every auto-fix is logged in `log.md` as `lint`.

## 10. Changes this pack makes to other artifacts

| Artifact | Change |
|---|---|
| T1_frontmatter-spec_v0.1 §3 (raw capture stamp) | Retired by W-ISS-19. Captures get a registry row instead. |
| T1_frontmatter-spec_v0.1 §2 | Add `producer: llm`. Claim fields move to §5 syntax. |
| T1_glossary_amazon_v0.1 | Add domain codes (§1) and entity types (§3) as locked terms. |

These land as frontmatter spec v0.2 and glossary v0.2 when this pack is promoted.

---

## Appendix — Provenance

| Claim | Tag | Basis |
|---|---|---|
| Domain list | [D] | Inputs domain file (10) + I-F12 (6), 2 merges stated in §1 |
| Write-time conflict via predicate groups | [U] | KB "Entity conflict resolution" (single vendor source) — adopted by WR-001 (C5) |
| Registry instead of raw frontmatter | [D] | Karpathy raw immutability (WR-013) + W-ISS-19 ruling |
| Claim fields | [D] | WR-001 (C1, C2, C8), AUG-02, AUG-05, AUG-11 |
| Entity types and edges | [D] | Exemplars ARC-01..08, FF-1..3, abbreviation definitions v0.2; untested until P2 gate |
