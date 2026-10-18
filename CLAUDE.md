---
id: WIKI-META-001
title: "CLAUDE.md — wiki maintainer instructions"
genre: META
page_status: promoted
page_version: 0.2.0
schema_version: 0.2.2
promoted: 2026-10-18 (WR-055)
recorded: 2026-10-18
producer: llm
---

# CLAUDE.md — Amazon LLM Wiki

You maintain this wiki. Alex owns the sources and the decisions. [A5]
v0.2 changes: PG-5-HOLD in INGEST (pack §4), padded tables (WR-050), YOUR ACTIONS block (WR-051), conditional Open questions (pack §6.1).

## 1. Read order (every session)

1. Read this file.
2. Read `index.md`.
3. Read the last 10 entries of `log.md`.
4. Read `schema/T1_subject-pack_amazon.md` only when you ingest, lint or change the schema.
5. Read wiki pages only when the task names them or `index.md` points to them.

## 2. Write scope [A2, A5]

- Write only inside `Wiki/LLM-Wiki/` and `Wiki/Build/_exchange/to-alex/`.
- Never edit a raw source. Exception subclass RAW-RULING — trigger: a WR- ruling names the raw files. Rule: edit only the named files.
- Never edit `schema/` without a WR- ruling.
- Write every markdown table pre-padded per pack §6.2 (WR-050).
- End every turn that touched a git-tracked folder with: `<folder> touched: yes — commit message: "Claude: …"` or `touched: no`.

### 2.1 Exception subclass MAC-FILE-OP (WR-051)

Trigger: a step needs a move, rename or delete on the Mac, and the Mac link has no shell.
Rule:
1. Put a `YOUR ACTIONS` block in the same reply that raises the step.
2. Write each command for macOS Terminal with absolute paths.
3. Use `mv -n` for every move and rename.
4. End the block with exactly one verify step Alex can run.
5. After Alex reports done, list the affected folder yourself.
6. Log the listing result as a WR- row in the ledger.

Block shape:

```
YOUR ACTIONS (Mac Terminal)
1. mv -n "/Users/CommerceMindCloud/<abs source>" "/Users/CommerceMindCloud/<abs target>/"
2. Verify: ls "/Users/CommerceMindCloud/<abs target>/"
```

Known upcoming triggers: T-1 after pack v0.2 promotion, T-2 reorganization, T-3 repo retirement.

## 3. INGEST (one source at a time unless Alex says "batch")

1. Find the source's row in `_meta/source-registry.csv`.
2. Add a registry row if none exists.
3. Read the source.
4. List the 3–7 key takeaways to Alex.
5. Wait for Alex to confirm or redirect.
6. Write or update the wiki pages, using exactly one genre template per page (pack §6).
7. Split a source that spans 2 genres or 2 domains into one page per genre+domain pair (pack §2).
8. Write every load-bearing statement as a claim line or a table claim (pack §5.1).
9. Tag every claim from a source with `producer: llm`, `mixed` or `unknown` as `prov: U`.
10. Tag every client-specific number `scope: entity_only`.
11. Check each new claim against predicate groups PG-1..5 (pack §4).
12. Close any older claim contradicted under PG-1..4 with `valid_to` and a `supersedes` link.
13. Apply PG-5-HOLD to every PG-5 conflict: flag both claims and raise an issue row.
14. Record every unresolved source defect under `Open questions` (pack §6.1).
15. Update `index.md`.
16. Append one `ingest` entry to `log.md`.
17. Set the registry row's `state: ingested` and `wiki_pages`.
18. Run lint on the touched pages.

## 4. QUERY

1. Read `index.md`.
2. Read the pages it points to.
3. Answer with citations as `[[slug|ID]]`.
4. Mark every statement in the answer with the lowest prov of its supporting claims.
5. Report absence of evidence as absence.
6. Offer to file the answer as a page when it is reusable.

## 5. LINT

1. Run `python3 _meta/tools/lint.py .` from the wiki root; it checks every page in `wiki/` against pack §9.
2. Narrow the report to the requested pages unless Alex says "full lint".
3. Apply only the auto-fixes marked "yes".
4. Read every file fully before an auto-fix writes it (W-ISS-36).
5. Report every WARN and BLOCK finding as an issue row.
6. Report INFO counts as one summary line.
7. Append one `lint` entry to `log.md`.

## 6. Provenance [A4]

- A claim reaches `prov: V` only with `verified_by` V1 (deterministic recompute or quote checked against the source file), V2 (checked against a real Amazon export) or V3 (Alex signed off a sample).
- A review by any Claude model is V5 and never upgrades a tag.
- Two sources from the same producer count as one source.

## 7. Client data (WR-027)

- Ingest client data as-is.
- Tag every client-specific claim `scope: entity_only`.
- Set `project_tier: T2` on every page that declares entity type Client.
- Never cite an entity_only claim as support for a `scope: global` claim.

## 8. Schema evolution [A3, A8]

- Propose a schema rule when Alex makes the same correction twice.
- Propose deleting a lint rule that fired zero times across 10 sessions.
- Log every schema change as a `schema` entry in `log.md` and a WR- row in the ledger.

## 9. Files

| File                                    | Role                                                 |
| --------------------------------------- | ---------------------------------------------------- |
| `index.md`                              | Catalog of every page                                |
| `log.md`                                | Append-only operations record                        |
| `schema/T1_subject-pack_amazon.md`      | Domains, types, edges, claim syntax, templates, lint |
| `schema/T1_glossary_amazon.md`          | Locked terms                                         |
| `schema/T1_abbreviation-definitions.md` | Locked abbreviations                                 |
| `schema/T1_frontmatter-spec.md`         | Page frontmatter                                     |
| `_meta/source-registry.csv`             | Raw source metadata                                  |
| `_meta/collaboration-protocol.md`       | Alex + Claude working protocol (WR-048)              |
| `_meta/tools/`                          | lint.py, pad.py, terms.txt (lint allowlist)          |
| `_archive/`                             | Superseded pre-git versions (WR-039)                 |
| `_meta/design/`                         | Wiki design corpus (read-only)                       |
| `_meta/eval/golden-queries.csv`         | Query test set (P5)                                  |
