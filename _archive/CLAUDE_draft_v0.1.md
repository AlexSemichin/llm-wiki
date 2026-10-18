---
id: WIKI-META-001
title: "CLAUDE.md — wiki maintainer instructions"
genre: META
page_status: candidate
page_version: 0.1.0
schema_version: 0.1.0
recorded: 2026-10-18
producer: llm
---

# CLAUDE.md — Amazon LLM Wiki

You maintain this wiki. Alex owns the sources and the decisions. [A5]

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
- End every turn that touched a git-tracked folder with: `<folder> touched: yes — commit message: "Claude: …"` or `touched: no`.

## 3. INGEST (one source at a time unless Alex says "batch")

1. Find the source's row in `_meta/source-registry.csv`.
2. Add a registry row if none exists.
3. Read the source.
4. List the 3–7 key takeaways to Alex.
5. Wait for Alex to confirm or redirect.
6. Write or update the wiki pages, using exactly one genre template per page.
7. Write every load-bearing statement as a claim line (pack §5).
8. Tag every claim from a source with `producer: llm` or `mixed` as `prov: U`.
9. Tag every client-specific number `scope: entity_only`.
10. Check each new claim against the predicate groups (pack §4).
11. Close any contradicted older claim with `valid_to` and a `supersedes` link.
12. Update `index.md`.
13. Append one `ingest` entry to `log.md`.
14. Set the registry row's `state: ingested` and `wiki_pages`.
15. Run lint on the touched pages.

## 4. QUERY

1. Read `index.md`.
2. Read the pages it points to.
3. Answer with citations as `[[slug|ID]]`.
4. Mark every statement in the answer with the lowest prov of its supporting claims.
5. Report absence of evidence as absence.
6. Offer to file the answer as a page when it is reusable.

## 5. LINT

1. Run every check in pack §9 on the requested pages, or on all pages when Alex says "full lint".
2. Apply only the auto-fixes marked "yes".
3. Report every other finding as an issue row.
4. Append one `lint` entry to `log.md`.

## 6. Provenance [A4]

- A claim reaches `prov: V` only with `verified_by` V1 (deterministic recompute or quote checked against the source file), V2 (checked against a real Amazon export) or V3 (Alex signed off a sample).
- A review by any Claude model is V5 and never upgrades a tag.
- Two sources from the same producer count as one source.

## 7. Client data (WR-027)

- Ingest client data as-is.
- Tag every client-specific claim `scope: entity_only`.
- Never cite an entity_only claim as support for a `scope: global` claim.

## 8. Schema evolution [A3, A8]

- Propose a schema rule when Alex makes the same correction twice.
- Propose deleting a lint rule that fired zero times across 10 sessions.
- Log every schema change as a `schema` entry in `log.md` and a WR- row in the ledger.

## 9. Files

| File | Role |
|---|---|
| `index.md` | Catalog of every page |
| `log.md` | Append-only operations record |
| `schema/T1_subject-pack_amazon.md` | Domains, types, edges, claim syntax, templates, lint |
| `schema/T1_glossary_amazon.md` | Locked terms |
| `schema/T1_abbreviation-definitions.md` | Locked abbreviations |
| `schema/T1_frontmatter-spec.md` | Page frontmatter |
| `_meta/source-registry.csv` | Raw source metadata |
| `_meta/design/` | Wiki design corpus (read-only) |
| `_meta/eval/golden-queries.csv` | Query test set (P5) |
