******# INPUT DELIVERY STRATEGY v0.1 — Amazon LLM Wiki

status: DRAFT (proposed, not promoted) | date: 2026-09-27 | session: 1

## 1. Corpus intake (done in session 1, read in place)

- "3 Layer Architecture": 12 files, 124 KB (~30k tokens). Core = 2, KB = 10.
- Independent producers: about 7, not 12 (correlated-source rule).
- Karpathy gist = [V] only for what the pattern says. All other docs = [U] practitioner/vendor claims.
- KB/MindBase file mixes 2 producers (sidleo comment + frankchu91 README). "User Observations & Feedback" = MindBase release notes (correlated). "Rohit's Gist" reacts to v2 (correlated).
- "Entity conflict resolution" benchmark figures: self-reported by a vendor, not verified → [U].

## 2. Delivery rules

- R1 Deliver by reference (connected folder / connector), never by paste.
- R2 Run a metadata census before reading any content.
- R3 Treat existing LLM-generated vault notes as `legacy-derived` [U]. Never cite them as evidence.
- R4 Handle one silo per session and one sub-domain per ingest batch.
- R5 Use scripts for deterministic ops (frontmatter, IDs, index, log). Use the LLM for judgment ops only.
- R6 Open and close every session with a continuation seed.
- R7 Keep ingest manual until at least 20 clean manual cycles per source type, then automate.

## 3. Phases

|Phase|You deliver|Claude returns|Exit gate|
|---|---|---|---|
|P0 Charter/L0|rulings B-01, A-01, A-02|L0 axioms v0.1 + scope log|L0 signed by human|
|P1 Design Decision Register|nothing new|C1–C8 proposals, feature→tier map|C1–C8 ruled|
|P2 Schema v0.1|existing type-taxonomy doc + 3–5 exemplar notes|CLAUDE.md: types, edges, frontmatter, templates, index/log, tree|3 exemplars re-render with no loss|
|P3 Source census|per-silo access|inventory.csv (path, type, size, mtime, hash, class, domain)|100% of reachable silos enumerated; hash dupes found|
|P4 Vault normalization|vault folder + git init|dry-run diff → scripted frontmatter backfill, legacy tags, orphan/dup report|0 notes missing required fields; originals recoverable|
|P5 Pilot ingest|10–15 raw sources, one sub-domain (SP PPC)|pages, index, log, defect log|defect rate and review verdict logged|
|P6 Scale|batches of ≤10, same type|lint after each batch|lint clean|
|P7 Tooling|triggered|BM25 above 150 pages; MCP when a 2nd client writes|measured miss rate|

## 4. Silo routing

|Silo|Route|Status|
|---|---|---|
|Obsidian vault (PC)|connect folder, work in place|available|
|PC disk|connect specific parent folders|available|
|Google Drive|Drive connector (explicit invoke)|needs invoke|
|Notion|Notion connector (explicit invoke)|needs invoke|
|Mac disk|sync to cloud drive, or a Mac-linked session for census|deferred|
|Apple Notes|bulk export to Markdown into a synced folder|deferred|

## 5. Conflict register (proposals)

- C1 Confidence: use discrete [V]/[D]/[U]/[X] plus a source list. No floats. Compute rank weight from the independent-source count.
- C2 Decay vs supersession: supersede, close, never delete. Carry two time fields: valid_from/valid_to (world) and recorded (belief).
- C3 Hooks vs human gate: keep the human write gate.
- C4 Index vs hybrid search: index.md + grep up to 150 pages, then full-text BM25. Add vectors only after a measured miss rate.
- C5 Contradictions: detect at write time with declared mutually-exclusive predicate groups. Lint finds gaps.
- C6 OKF strict: reject strict OKF (it forbids custom fields). Adopt per-directory AGENTS.md write gates.
- C7 One canonical corpus with thin client adapters. No parallel instruction stacks.
- C8 Evidence scope: every claim carries scope entity_only | local | global.

## 6. Ledger

- B-01 blocker (P0): L0 axiom set is unbound, and the project has 0 docs.
- B-02 blocker (P3, Mac + Apple Notes only): unreachable from this session → deferred.
- A-01 ambiguity (P2): agency-ops in or out of scope.
- A-02 ambiguity (P2): relationship to knowledge-vault taxonomy, PPC Artifact Vault, ICM wiki.
- A-03 ambiguity: design corpus stored as a separate meta layer, not in the Amazon wiki.
- F-01 legacy notes = [U] (resolved by R3).
- F-02 KB corpus is 100% [U].
- F-03 PPC Artifact Vault: partner/IP scoping.
- F-04 MindBase file misattribution.
- F-05 Drive/Notion need explicit invoke.
- AS-01 vault under git before any write.
- AS-02 Claude is the sole writer; other clients read-only.