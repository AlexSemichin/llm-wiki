---
id: WIKI-META-002
aliases: [WIKI-META-002, WIKI-DATASPEC-001]
title: "T1 Subject Pack — Amazon (schema)"
genre: META
page_status: promoted
page_version: 0.2.2
schema_version: 0.2.2
promoted: 2026-10-18 (WR-055)
recorded: 2026-10-18
producer: llm
depends_on: [T1_glossary_amazon, T1_abbreviation-definitions, T1_frontmatter-spec]
---

# T1 Subject Pack — Amazon v0.2

PURPOSE — Define what can exist in the Amazon LLM wiki (domains, entity types, edges, claims), how pages are identified and shaped, and which deterministic checks every page must pass. [A3, A7]

Terms resolve in `schema/T1_glossary_amazon.md`. Abbreviations resolve in `schema/T1_abbreviation-definitions.md`. Versions live in each file's frontmatter and in git (WR-039).
v0.2 applies P2.2 findings F1–F14 (WR-045) and WR-050. v0.2.1 applies the re-render findings R1–R6. v0.2.2 applies W-ISS-37 (3 widest cells shortened) and R9 (`query_market_rate`). Change map: §11.

---

## 1. Domain axis (14) [A2]

The domain list unites the 10 underweighted domains (Inputs) and the 6 core domains (I-F12). Two merges reduce 16 to 14: "creative listing optimization" merges into LST; "FBA logistics & reimbursements" merges into INV.

| Code  | Domain                      | In scope                                                                         |
| ----- | --------------------------- | -------------------------------------------------------------------------------- |
| PPC   | Amazon advertising          | SP, SB, SBV, SD, SDV, DSP: structure, bidding, targeting, harvesting, automation |
| LST   | Listing & search visibility | Titles, bullets, backend terms, images, A+, keyword research, organic rank       |
| CTLG  | Catalog & brand             | Brand Registry, variations, browse nodes, catalog data                           |
| INV   | Inventory & fulfillment     | Replenishment, lead times, IPI, FBA/FBM/AWD, reimbursements, stranded inventory  |
| VOC   | Reviews & customer voice    | Ratings, reviews, returns reasons, Q&A                                           |
| OFF   | Off-Amazon traffic          | External ads aimed at Amazon growth, attribution, brand referral                 |
| ECON  | Unit economics              | Contribution margin, fees, P&L, break-even ACoS                                  |
| HLTH  | Account health & policy     | Violations, appeals, reinstatement, compliance                                   |
| INTEL | Competitor intelligence     | How intel is gathered, structured, acted on                                      |
| CUST  | Customer lifecycle          | Repeat purchase, cohorts, LTV/CAC, NTB                                           |
| LNCH  | Launch sequencing           | Honeymoon mechanics, velocity ramp, review seeding                               |
| PRCE  | Pricing                     | MAP, repricing triggers, floor and ceiling logic, deals                          |
| AGCY  | Agency account operations   | SOPs for running an Amazon account only (WR-004)                                 |
| MEAS  | Measurement & reporting     | Metric definitions, report specs, dashboards                                     |
| WIKI  | The wiki itself             | Pages about the wiki (genre META and DIAG only)                                  |

Note: WIKI is a housekeeping domain, not a subject domain. Subject domain count = 14. Table row count = 15.

## 2. Page ID scheme [A8] (WR-028)

- Format: `{DOMAIN}-{GENRE}-{NNN}`, e.g. `PPC-REF-001`.
- NNN is a 3-digit counter per DOMAIN+GENRE pair, never reused.
- Filenames are slugs. The `id` and every legacy ID go into `aliases`.
- Links are written `[[slug|ID]]`.
- Legacy IDs (`ARC-01`, `CORE.PPC.REF.X.v1`, `STR-02`) are opaque alias strings. They are outside the term lock.
- Split rule: one source that spans 2 genres or 2 domains yields one page per genre+domain pair. Each page lists the same `src`. (Held 2/2 in P2.2.)

## 3. Entity types (L1) [A3]

Every page declares ≥1 entity type in `entity_types`.

| Group         | Entity type     | Key attributes                                                  |
| ------------- | --------------- | --------------------------------------------------------------- |
| Catalog       | Brand           | name, own (bool)                                                |
| Catalog       | Product         | parent ASIN, variation theme                                    |
| Catalog       | ASIN            | asin, sku_tier                                                  |
| Catalog       | SKU             | sku                                                             |
| Catalog       | Category        | browse node id, path                                            |
| Ads           | AdProgram       | SP · SB · SBV · SD · SDV · DSP                                  |
| Ads           | Campaign        | naming code, state                                              |
| Ads           | AdGroup         | —                                                               |
| Ads           | AdsPortfolio    | budget cap                                                      |
| Ads           | Target          | kind: keyword · asin · category · audience · auto_group         |
| Ads           | SearchTerm      | text                                                            |
| Ads           | Placement       | TOS · ROS · PDP                                                 |
| Ads           | CampaignSetting | name (every CampaignSetting is a lever)                         |
| Ads           | IntentSegment   | code (BRAN, DEF, GENE, RANK, COMP, ATT, CROS, CAT, EVNT)        |
| Ads           | Audience        | code                                                            |
| Ads           | FunnelStage     | tofu · mofu · bofu · retention (WR-023)                         |
| Market        | Competitor      | brand, ASINs                                                    |
| Market        | Marketplace     | code                                                            |
| Economics     | Metric          | formula, metric_class (effectiveness · efficiency · governance) |
| Economics     | Dimension       | values                                                          |
| Economics     | Fee             | type                                                            |
| Economics     | Price           | type                                                            |
| Operations    | InventoryPool   | AFN · AWD · inbound                                             |
| Governance    | AmazonPolicy    | source URL, effective date                                      |
| Governance    | HealthSignal    | metric, threshold                                               |
| Knowledge     | Framework       | named method or philosophy (Hagakure, STAG, Pearl ladder)       |
| Knowledge     | Report          | Amazon report source (SQP, Search Term Report, Business Report) |
| External      | Tool            | vendor (Optmyzr, Helium10…)                                     |
| External      | Channel         | off-Amazon traffic channel                                      |
| Client-scoped | Client          | client code (note below)                                        |

Entity type count = 30.
Client note: every claim about a Client is `entity_only` (WR-027); every page that declares Client carries `project_tier: T2` (§5.2).

## 4. Edge types (L1) [A3]

| Edge           | Domain → Range                                   | Relation class |
| -------------- | ------------------------------------------------ | -------------- |
| has_variation  | Product → ASIN                                   | composition    |
| sold_as        | ASIN → SKU                                       | dependency     |
| belongs_to     | ASIN → Category                                  | inheritance    |
| owned_by       | ASIN → Brand                                     | dependency     |
| advertises     | Campaign → ASIN                                  | dependency     |
| contains       | Campaign → AdGroup; AdGroup → Target             | composition    |
| member_of      | Campaign → AdsPortfolio                          | composition    |
| runs_on        | Campaign → AdProgram                             | dependency     |
| aims_at        | Target → SearchTerm · ASIN · Category · Audience | dependency     |
| serves_stage   | Campaign · IntentSegment → FunnelStage           | dependency     |
| has_setting    | Campaign → CampaignSetting                       | composition    |
| measured_by    | any → Metric                                     | dependency     |
| sliced_by      | Metric → Dimension                               | dependency     |
| computed_from  | Metric → Metric                                  | transformation |
| competes_with  | ASIN → ASIN; Brand → Brand                       | dependency     |
| governed_by    | any → AmazonPolicy                               | dependency     |
| implemented_by | Framework · page → Tool                          | dependency     |
| sourced_from   | Metric · page → Report                           | dependency     |
| uses_technique | PROC page → TECH page                            | dependency     |
| instance_of    | Client-scoped page → Framework                   | inheritance    |
| supersedes     | page → page; claim → claim                       | transformation |

### Mutually exclusive predicate groups (C5) — conflict detected at write time

| Group                 | Predicates (same ordered pair, same valid time)                                        | Example                           |
| --------------------- | -------------------------------------------------------------------------------------- | --------------------------------- |
| PG-1 Eligibility      | eligible_for · restricted_from                                                         | ASIN × AdProgram                  |
| PG-2 Effect direction | increases · decreases                                                                  | CampaignSetting × Metric          |
| PG-3 Ownership        | own_asset · competitor_asset                                                           | ASIN × Brand                      |
| PG-4 Product relation | complements · substitutes                                                              | ASIN × ASIN (CROS vs ATT routing) |
| PG-5 Value            | one parameter (threshold, target, window, coefficient) with 2 different numeric values | SRC-0008 CTR Index 0.60 vs 1.0    |

Rule PG-1..4: a new claim that asserts one predicate where the other already holds closes the older claim (`valid_to` set) and links both by `supersedes`. Nothing is deleted.

Exception subclass PG-5-HOLD — trigger: a PG-5 conflict is detected (across sources or inside one source). Rule:
1. Keep both claims open.
2. Add `flag: value_conflict` to both claim spans.
3. Add one Open questions entry that names both values and their src IDs.
4. Raise one issue row for a WR- ruling.
5. On the ruling, close the losing claim with `valid_to` and link the winner by `supersedes`.

Reason: no recency order exists inside one source, so auto-closing would pick a winner without warrant.

## 5. Claim syntax (L2) [A4]

### 5.1 Claim line

Every load-bearing statement in a wiki page is one bullet ending in one code span:

```
- Graduate a term from discovery to validation after >3 orders or ACoS ≤ target × 1.2 over 14–28 days. `prov: U | scope: global | src: SRC-0002`
```

| Field      | Values                                                                                    | Required                                      |
| ---------- | ----------------------------------------------------------------------------------------- | --------------------------------------------- |
| prov       | V · D · U · X                                                                             | yes                                           |
| scope      | entity_only · domain · global                                                             | yes                                           |
| src        | ≥1 source-registry ID, comma-separated                                                    | yes                                           |
| valid      | `YYYY-MM-DD..YYYY-MM-DD`, open ends allowed                                               | no                                            |
| causal     | association · intervention · counterfactual                                               | only for causal claims                        |
| autonomy   | inform · recommend · execute_report · delegate                                            | only in DECRULE pages                         |
| method     | expert_opinion · extrapolation · econometric · data_multivariate · intentions · role_play | only in TECH/REF forecasting claims           |
| flag       | autonomy_default · client_unknown · value_conflict (comma-separated)                      | only when a subclass below sets it            |
| supersedes | block ID of the closed claim, e.g. `^c-02`                                                | only on the winning claim of a supersede pair |

Exception subclass TABLE-CLAIM (F1) — trigger: a load-bearing statement is a table row. Rule:
1. Add a last column named `claim` to that table.
2. Put the claim code span in that column.
3. Escape every pipe inside the span as `\|`.

| Condition (illustrative) | Action (illustrative) | claim                                       |
| ------------------------ | --------------------- | ------------------------------------------- |
| {condition}              | {action}              | `prov: U \| scope: global \| src: SRC-0002` |

Exception subclass SUPERSEDE-PAIR (R3) — trigger: a claim closes another claim (PG-1..4 rule or PG-5-HOLD step 5). Rule:
1. End both claim lines with an Obsidian block ID `^c-NN`, unique per page.
2. Set `valid: ..YYYY-MM-DD` on the closed claim.
3. Set `supersedes: ^c-NN` on the winning claim, naming the closed claim's block ID.

Exception subclass DERIVED-CLAIM — trigger: Claude derives the claim from ≥2 claims with prov V. Rule: set `prov: D` and list the source claims' src IDs.

Exception subclass AUTONOMY-DEFAULT (F5) — trigger: a DECRULE claim's source states no autonomy. Rule: set `autonomy: recommend` and `flag: autonomy_default`.

Exception subclass CLIENT-UNKNOWN (F7) — trigger: a claim is client-specific and the client cannot be identified. Rule: set `scope: entity_only` and `flag: client_unknown`; leave the registry `client_code` blank.

### 5.2 Frontmatter fields added by this pack

These move into frontmatter spec v0.2 on promotion (§10).

| Field          | Values                                                                     | Required                                                       | Finding |
| -------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------- | ------- |
| review_cadence | ISO 8601 duration (`P7D`, `P1M`) or `on_event`                             | no                                                             | F2      |
| tool_surface   | list of `Tool:surface` strings, e.g. `Optmyzr:rule-engine` (glossary form) | no                                                             | F3      |
| decision_date  | `YYYY-MM-DD`                                                               | yes, genre DEC only                                            | F8      |
| date_source    | stated · file_mtime                                                        | yes, genre DEC only                                            | F8      |
| project_tier   | T1 · T2                                                                    | yes when `entity_types` includes Client (value T2); default T1 | F14     |

## 6. Genre body templates (L2) [A7]

Each page = frontmatter + exactly the sections listed for its genre, in order, then the conditional section `Open questions`.

| Genre    | Body sections                                                                                    |
| -------- | ------------------------------------------------------------------------------------------------ |
| REF      | Definition · Claims · Rationale · See also                                                       |
| PROC     | Trigger · Inputs · Steps (numbered) · Outputs · Failure modes · See also                         |
| TECH     | Purpose · Formula/Algorithm · Parameters · Claims · Used by · See also                           |
| DATASPEC | Structure (table) · Field rules · Example · See also                                             |
| MAP      | Relations (table: from · edge · to) · See also                                                   |
| META     | Rule · Rationale                                                                                 |
| TEMPL    | Use when · Template (fenced block) · Slots                                                       |
| DIAG     | Input state · Checks (table: check · severity WARN/BLOCK · threshold) · Verdict rules · See also |
| CASE     | Client · Window · Situation · Action · Result · Lessons (all claims entity_only)                 |
| GLOSS    | Terms (table: term · definition · src)                                                           |
| DEC      | Date · Decision · Alternatives rejected · Rationale · Outcome                                    |
| DECRULE  | IF (conditions) · THEN (action) · autonomy · hard_constraints · Claims · See also                |

Genre count = 12.

### 6.1 Open questions (F4)

- Append `## Open questions` as the last section when the page has ≥1 unresolved item.
- Omit the section when the page has 0 unresolved items.
- Write each item as one bullet naming the src ID and the defect (gap, contradiction, undefined term, missing citation).

### 6.2 Table format (WR-050)

- Write every markdown table pre-padded in Obsidian's column-aligned format.
- Open each row with `| `, separate cells with ` | `, close each row with ` |`.
- Pad every cell with trailing spaces to the widest cell in its column.
- Fill the delimiter row with dashes to the column width (minimum 3), keeping any alignment colons.
- Count an escaped pipe `\|` as 2 characters.
- Leave tables inside fenced code blocks unpadded.

Goal: opening a page in Obsidian produces an empty `git diff`.

## 7. Source registry (WR-040) [A4, A8]

Raw notes stay untouched. Their metadata lives in `_meta/source-registry.csv`.

| Column               | Meaning                                                                                     |
| -------------------- | ------------------------------------------------------------------------------------------- |
| src_id               | `SRC-0001`… never reused                                                                    |
| path                 | vault-relative path of the raw note or file                                                 |
| silo                 | obsidian · gdrive · notion · mac-disk · apple-notes                                         |
| source_type          | note · llm-session · article · export · whiteboard-image · transcript                       |
| producer             | human · llm · mixed · unknown                                                               |
| captured             | the source's own capture date when its frontmatter states one, else file mtime (local date) |
| sha256_16            | first 16 hex characters of the SHA-256 content hash at registration                         |
| bytes                | size                                                                                        |
| domain_hint          | one domain code                                                                             |
| genre_hint           | one genre code                                                                              |
| contains_client_data | true · false                                                                                |
| client_code          | ENSO · BERL · LUND · JAYE · blank                                                           |
| legacy_ids           | `\|`-separated                                                                              |
| state                | registered · ingested · excluded                                                            |
| wiki_pages           | `\|`-separated page IDs built from it                                                       |

Rule: a source with `producer: llm`, `mixed` or `unknown` never supports `prov: V` on its own.
Rule: `producer: unknown` is treated as `mixed` (F6).
Rule: `client_code` is blank when `contains_client_data: false`, or when the client is unknown (CLIENT-UNKNOWN, §5.1).
Rule: a sha256_16 change marks the source `registered` again (re-ingest due).

## 8. index.md and log.md [A8]

- `index.md`: grouped by domain, then genre. One line per page: `- [[slug|ID]] — one-line summary · prov · page_status`.
- `log.md`: append-only. Entry header: `## [YYYY-MM-DD] op | title`. Ops: ingest · query · lint · schema · rename · supersede.

## 9. Lint rules (deterministic, V1) [A4, A6]

Severity set: BLOCK (write refused) · WARN (reported) · INFO (counted, not reported as a defect).

| ID    | Check                                                                                                                                                                                    | On fail | Auto-fix        |
| ----- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- | --------------- |
| L-01  | Frontmatter fence intact: line 1 = `---`, a closing `---` exists                                                                                                                         | BLOCK   | no              |
| L-02  | Required frontmatter fields present, including genre-specific fields (§5.2)                                                                                                              | BLOCK   | no              |
| L-03  | `id` unique and matches §2 pattern                                                                                                                                                       | BLOCK   | no              |
| L-04a | A `[[link]]` target is absent from the wiki, and the target, its path basename or the link alias is in a registry row (`src_id`, `legacy_ids`, `path`) with `state` ≠ ingested — pending | INFO    | no              |
| L-04b | A `[[link]]` target is absent from both the wiki and the registry — broken                                                                                                               | WARN    | no              |
| L-05  | Duplicate links in the page body (frontmatter excluded)                                                                                                                                  | WARN    | yes, keep first |
| L-06  | `prov: V` only with `verified_by` ∈ {V1, V2, V3}                                                                                                                                         | BLOCK   | no              |
| L-07  | Every claim span carries prov, scope, src                                                                                                                                                | BLOCK   | no              |
| L-08  | Every src ID exists in the registry                                                                                                                                                      | BLOCK   | no              |
| L-09  | Page `prov_tag` = lowest claim prov                                                                                                                                                      | —       | yes (computed)  |
| L-10  | `page_status: superseded` requires `superseded_by`                                                                                                                                       | BLOCK   | no              |
| L-11  | Bare banned words (`layer`, `tier`, `stage`, `level`), abbreviations absent from definitions v0.2, and camelCase identifiers outside code spans absent from the glossary                 | WARN    | no              |
| L-12  | A `scope: global` claim cites no source whose claims are all entity_only                                                                                                                 | WARN    | no              |
| L-13  | DECRULE claims carry `autonomy`                                                                                                                                                          | BLOCK   | no              |
| L-14  | The word "driver" requires `causal` ≥ intervention                                                                                                                                       | WARN    | no              |
| L-15  | Page has ≥1 inbound link (except index targets)                                                                                                                                          | WARN    | no              |
| L-16  | Every table outside fenced code is padded per §6.2                                                                                                                                       | WARN    | yes, re-pad     |

L-11 allowlist (F12): every compound term locked in the glossary (e.g. "Rainbow tier", "SKU tier", "FunnelStage") and every token inside a code span is exempt. A banned word is "bare" only when no allowlisted compound contains it at that position.
L-11 exemptions (R5): the pack-defined keywords `IF`, `THEN`, `WARN`, `BLOCK`, `INFO` are not abbreviations. Write enum values and engine codes (`HIGH`, `FIX/CLICKSIDE`) in code spans.
L-11 camelCase (F10): a token matching `[a-z]+[A-Z][A-Za-z]*` outside code spans is checked against the glossary.
L-04 split (F13): a link to a not-yet-ingested source is work in progress, not a defect.

Every auto-fix is logged in `log.md` as `lint`.

## 10. Changes this pack makes to other artifacts

| Artifact                                        | Change                                                                                                                                                              |
| ----------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| T1_frontmatter-spec v0.1 §3 (raw capture stamp) | Retired by WR-040. Captures get a registry row instead.                                                                                                             |
| T1_frontmatter-spec v0.1 §2                     | Add `producer: llm`. Claim fields move to §5.1. Add the 5 fields in §5.2.                                                                                           |
| T1_glossary_amazon v0.1                         | Add domain codes (§1) and entity types (§3) as locked terms.                                                                                                        |
| T1_glossary_amazon v0.1                         | Add `query_market_rate`, `clickIndex`, `cartIndex` (F10, R9). `myDemand` deferred (W-ISS-34).                                                                       |
| CLAUDE draft v0.1                               | Becomes CLAUDE.md v0.2: PG-5-HOLD in INGEST, padded tables (WR-050), YOUR ACTIONS block (WR-051).                                                                   |
| T1_abbreviation-backlog                         | Add `AI` (used in SRC-0001 "AI learning speed"; absent from definitions v0.2). Add engine codes `FIX`, `CLICKSIDE`, `CARTSIDE` (SRC-0008). Definitions = Alex only. |
| lint.py                                         | Implements L-04a/b, L-05 body scope, L-11 allowlist + abbreviations + camelCase, L-12, L-16 (lint.py v0.2).                                                         |

These land as frontmatter spec v0.2 and glossary v0.2 when this pack is promoted.

## 11. Change map v0.1 → v0.2

| Finding  | Fix                                                                                                            | Section           |
| -------- | -------------------------------------------------------------------------------------------------------------- | ----------------- |
| F1       | TABLE-CLAIM subclass                                                                                           | §5.1              |
| F2       | `review_cadence`                                                                                               | §5.2              |
| F3       | `tool_surface`                                                                                                 | §5.2              |
| F4       | Conditional Open questions section                                                                             | §6.1              |
| F5       | AUTONOMY-DEFAULT subclass + `flag` field                                                                       | §5.1              |
| F6       | `producer: unknown`                                                                                            | §7                |
| F7       | CLIENT-UNKNOWN subclass                                                                                        | §5.1, §7          |
| F8       | `decision_date`, `date_source`                                                                                 | §5.2              |
| F9       | PG-5 + PG-5-HOLD                                                                                               | §4                |
| F10      | L-11 camelCase + glossary entries                                                                              | §9, §10           |
| F11      | L-05 body only                                                                                                 | §9                |
| F12      | L-11 allowlist                                                                                                 | §9                |
| F13      | L-04a/b split + INFO severity                                                                                  | §9                |
| F14      | "Tier 2" → Client-scoped + `project_tier`                                                                      | §3, §5.2          |
| WR-050   | Padded tables + L-16                                                                                           | §6.2, §9          |
| —        | Split rule written down (held in P2.2)                                                                         | §2                |
| —        | WIKI domain admits DIAG (the gate report is a WIKI page)                                                       | §1                |
| R1       | Pack genre DATASPEC → META; id WIKI-DATASPEC-001 → WIKI-META-002 (glossary: DATASPEC is never the wiki itself) | frontmatter, §1   |
| R2       | Example src SRC-0012 → SRC-0002 (SRC-0012 is now a real row, TIER-01; the example text is SRC-0002's rule)     | §5.1              |
| R3       | SUPERSEDE-PAIR subclass + `supersedes` claim field (claims had no anchor)                                      | §5.1              |
| R4       | Registry `sha256_16` and `captured` defined as the registry already stores them                                | §7                |
| R5       | L-04a matches path basename and link alias; L-11 keyword exemptions                                            | §9                |
| R6       | `tool_surface` example uses the glossary form `rule-engine`                                                    | §5.2              |
| W-ISS-37 | 3 widest table cells moved to notes (Client row, §10 glossary row, appendix padding row)                       | §3, §10, appendix |
| R9       | "market CTR" and "category benchmark" (SRC-0008 sense) locked as `query_market_rate` (WR-055)                  | §10               |

---

## Appendix — Provenance

| Claim                                       | Tag | Basis                                                                                        |
| ------------------------------------------- | --- | -------------------------------------------------------------------------------------------- |
| Domain list                                 | [D] | Inputs domain file (10) + I-F12 (6), 2 merges stated in §1                                   |
| Write-time conflict via PG-1..4             | [U] | KB "Entity conflict resolution" (single vendor source) — adopted by WR-001 (C5)              |
| PG-5 and PG-5-HOLD                          | [D] | F9 (SRC-0008 internal contradiction) + WR-047 resolution path                                |
| Registry instead of raw frontmatter         | [D] | Karpathy raw immutability (WR-013) + WR-040                                                  |
| Claim fields                                | [D] | WR-001 (C1, C2, C8), AUG-02, AUG-05, AUG-11, F5, F7                                          |
| Entity types and edges                      | [D] | Exemplars ARC-01..08, FF-1..3, abbreviation definitions v0.2; 8/8 converted in P2.2 (WR-044) |
| §6.2 padding matches Obsidian byte-for-byte | [V] | WR-054 (V1). Emoji and CJK untested                                                          |
| `review_cadence` value format               | [D] | ISO 8601 chosen by Claude; no source states a format                                         |
