# INPUT DELIVERY STRATEGY v0.2 — Amazon LLM Wiki [A1,A3,A7,A8]

status: CANDIDATE | date: 2026-10-11 | supersedes: claude/input-delivery-strategy-v0.1.md ON RULING (pending, A5) glossary conformance: "layer" is used ONLY in the L0–L4 sense. Karpathy's raw/wiki/schema split is renamed "zone".

## 0. Zones (replaces v0.1 "layers")

|Zone|Holds|Writer|
|---|---|---|
|raw|immutable sources|human|
|wiki|T1 subject pages|Claude (sole writer, AS-02)|
|schema|subject pack + CLAUDE.md + META genre|Claude proposes, human promotes|
|_meta/design|wiki-design corpus (Core, KB, Inputs)|read-only|

## 1. Rulings received in session 2 (provisional IDs — the ledger is absent from the project)

|Prov. ID|Ruling|
|---|---|
|R-024|C1–C8 adopted as proposed. P1 closed.|
|R-025|B-01 resolved: L0 = 00_L0_axioms_v1.0.1.|
|R-026|B-02: Mac + Apple Notes deferred until P5 is complete.|
|R-027|A-01: agency SOPs in scope only where they cover running an Amazon account; BD and sales out.|
|R-028|A-02: this wiki is canonical; the knowledge-vault genre list seeds the schema; the PPC Artifact Vault is link-only.|
|R-029|A-03: design documents live in _meta/design, outside the Amazon wiki.|
|R-030|F-03: artifacts with Frederick as owner are excluded from ingest pending an ownership ruling.|
|R-031|F-05: Drive and Notion invoked per silo at P3.|
|R-032|AS-01: vault under git before any write.|
|R-033|AS-02: Claude is the sole writer; other AI apps read only.|
|R-034|Inputs folder admitted as amplification only, non-canonical.|

## 2. Phase status

|Phase|Status|Remaining input|
|---|---|---|
|P0 Charter/L0|DONE (L0 v1.0.1)|—|
|P1 Design decision register|DONE (R-024)|—|
|P2 Subject pack v0.1 (Amazon)|READY TO DRAFT|3–5 exemplar notes; TECH ruling (I-F02); 03_L3_ledger.md + 04_L4_harness-augmentation_v2.0.0.md for promotion|
|P3 Source census|waiting on P2|per-silo access|
|P4–P7|unchanged from v0.1|—|

## 3. P2 output shape (declared now so the inputs fit)

- Output file: `T1_subject-pack_amazon_v0.1.md` (a subject pack per glossary; harness types stay in 01_L1_types).
- Axis 1 genre: REF, PROC, SCHEMA, MAP, META, TEMPL, DIAG, CASE, GLOSS, LOG, POLICY (+TECH on ruling; PROTO → status `experimental`).
- Axis 2 entity type: Amazon nouns (ASIN, Brand, Campaign, Keyword, Metric, Dimension, Fee, Policy, Competitor, Tool, Client…) with edge set and mutually-exclusive predicate groups (C5).
- Axis 3 domain: union of the 10 underweighted domains + 6 core domains (I-F12).
- Claim attributes: tag, sources[], scope (C8), valid_from/valid_to + recorded (C2), causal_level (AUG-02), analytics_maturity (AUG-07), method_class (AUG-11), autonomy + hard_gates (AUG-05, PROC/POLICY only).

## 4. Open issues


| ID          | Category  | Status                                      | Item                                                                                                                                                                                                                                        | Cheapest fix                                                          |
| ----------- | --------- | ------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------- |
| B-03        | Blocker   | Blocking promotion of P2 (not drafting)     | 03_L3_ledger.md, 04_L4_harness-augmentation_v2.0.0.md, 04_L4_corpus_manifest.md are cited by L0/L1/glossary but absent. Ruling IDs R-024+ are provisional. Issue schema A§6.1, Stage S0–S7 (A§2) and evidence package A§8.2 are unreadable. | Upload the ledger + A§ (2 files). The manifest is optional.           |
| A-04        | Ambiguity | Note                                        | Phase P0–P7 (this plan) vs Stage S0–S7 (A§2): possible duplicate lifecycle.                                                                                                                                                                 | Resolves on B-03; until then "Phase" = wiki build-plan position only. |
| I-F02       | Ambiguity | Blocking genre-axis promotion               | TECH undefined.                                                                                                                                                                                                                             | One line or drop.                                                     |
| I-F06/I-F07 | Flag      | Blocking ingest of reporting framework only | Client data + employer/partner ownership.                                                                                                                                                                                                   | Admit theory structures only; sanitize.                               |
## Inputs Delivery Rules & When To Connect Folders

## When to connect more Obsidian folders

**At P3, the inventory step, once the P2 subject pack v0.1 exists.**

- **Why wait:** the inventory sorts every file by genre, domain and entity type, and the schema defines those categories. Connecting earlier means scanning twice. The abbreviation scan is already done.
- **How:** grant the vault root once, not subfolder by subfolder. One approval, and I sort out-of-scope material during the inventory.
- **Where from:** run P3 from the Windows link if you can. That link gave me a shell on your machine, so the inventory is one script. The Mac link has no shell, so I have to copy files over in batches of 50: 233 files took 5 rounds, and the full vault would take about 8 or more.
- **One exception:** connect a folder earlier if it holds definitions for the 94 undefined abbreviations.

## **Inputs Delivery Rules** 

| #      | Rule                                                                                                                                    | Why                                                                                   |
| ------ | --------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| **R1** | Give me access to a folder or connector instead of pasting content.                                                                     | Pasting costs the tokens twice.                                                       |
| **R2** | List what’s in each source (count, format, size, date, hash) before I read any content.                                                 | It’s cheap, and it finds duplicates and sensitive files early.                        |
| **R3** | **Your existing LLM-written Obsidian notes are not raw sources.** They go in marked as legacy and [U], and are never cited as evidence. | Otherwise earlier AI guesses get treated as facts (“5 degradation modes” #2, Cortex). |
| **R4** | One source location per session, one sub-domain per ingest batch.                                                                       | Keeps each batch coherent and defects easy to trace.                                  |
| **R5** | Frontmatter, IDs, index and log are handled by scripts. The LLM handles only judgment calls.                                            | securityguy and MindBase both found models don’t reliably follow format rules.        |
| **R6** | Every session opens and closes with a continuation seed.                                                                                | Keeps the reasoning traceable between sessions.                                       |
| **R7** | Stay manual until there are ≥20 clean ingests per source type, then automate.                                                           | “Schema & Lifecycle” critique. The threshold of 20 is my proposal.                    |
