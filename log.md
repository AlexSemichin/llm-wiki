# Log — Amazon LLM Wiki

Append-only. Header: `## [YYYY-MM-DD] op | title`. Ops: ingest · query · lint · schema · rename · supersede.

## [2026-10-18] schema | Promote subject pack v0.2.2, CLAUDE.md v0.2, glossary v0.2, frontmatter spec v0.2
- Ruling: WR-055. Superseded v0.1 files moved to `_archive/` (T-1).
- Changes since v0.1: F1–F14 (WR-045), WR-050 padded tables, WR-051 YOUR ACTIONS, R1–R9, W-ISS-37.

## [2026-10-18] ingest | P2 exemplar pages (10) from SRC-0001..0008
- Built in P2.2, re-rendered against pack v0.2.1 in P2.3 (WR-053), restamped schema_version 0.2.2.
- Registry: 17 rows; SRC-0009..0017 state registered (link targets, not ingested).

## [2026-10-18] lint | full lint, lint.py v0.2
- 0 BLOCK · 5 WARN (L-04b `[[optmyzr]]` ×3, L-11 `AI`, L-11 `myDemand`) · 9 INFO (L-04a pending).

## [2026-10-18] rename | T-1 + T-2 executed on the Mac (WR-060)
- Wiki tree moved from Build/_exchange to Wiki/LLM-Wiki; Build/T1, Architecture, Inputs & Delivery Strategy moved into schema/, _meta/, _archive/; Wiki/KB → _meta/design/wiki-notes (W-ISS-38).
- Commits 1a62e68 (Claude) and 9420812 (Alex). Excluded from Obsidian Sync.

## [2026-10-18] lint | full lint in place, lint.py v0.2
- 0 BLOCK · 5 WARN · 9 INFO — unchanged from the pre-move run.

## [2026-10-18] schema | CLAUDE.md v0.2.1, glossary v0.2.1
- WR-061: paste-safe YOUR ACTIONS block shape (CLAUDE.md §2.1). WR-062: `category_benchmark_rate` locked; PPC-PROC-001 → page_version 0.2.1.

## [2026-10-18] ingest | P3 census — vault registered, no pages built
- Registry 17 → 1166 rows; SRC-0018..1166 `state: registered`. Order: PPC/KB, PPC, then vault A–Z. 0 sha drift on SRC-0001..0017.
- 110 rows have blank `sha256_16` (path > 7 folders deep; staging limit). 33 personal-admin files held out of the registry pending a ruling.
- Hints are path-derived: domain_hint on 1015/1149, genre_hint on 20, producer `unknown` on all 1149.

## [2026-10-18] lint | full lint after census, lint.py v0.2
- 0 BLOCK · 5 WARN · 9 INFO — identical to the pre-census run.

## [2026-11-01] ingest | P3 re-census from the canonical Windows vault (R-P3-4, WR-070)
- Registry 1166 → 1489 rows. Kept IDs: 943 same, 101 moved (path updated by hash match; incl. SRC-0001..0005 → PPC/Core/02_account-architecture/), 3 sha drift (SRC-0447, 0448, 0733). 109 blank `sha256_16` filled. 10 rows `state: missing`.
- 323 new rows SRC-1167..1489 `state: registered`, hints by the census §2 rules. 34 held out (33 personal-admin + 1 credential file); 3 OS/git dotfiles excluded.
- Hashes from sha256sum over the Windows vault (Linux VM mount).

## [2026-11-01] lint | full lint after re-census, lint.py v0.2
- 0 BLOCK · 5 WARN · 9 INFO — identical to the pre-re-census run.

## [2026-11-01] schema | subject pack v0.2.2 → v0.2.3 (W-ISS-61, WR-071)
- Registry `state` enum adds `missing` + definition rule (§7); change map row (§11). L-16 PASS; lint 0 BLOCK.

## [2026-11-01] ingest | domain scope applied to 190 blank-domain rows (W-ISS-49, WR-072)
- domain_hint set on 69: CTLG 50, PPC 8, INTEL 4, LST 2, MEAS 2, AGCY 2 (contains_client_data true, client unknown), ECON 1.
- 121 rows `state: excluded`: Information Retrieval, Agent Architecture & OS Engineering, Command Center, Vault/*, Agency_CommerceMind, Reasoning, KA, Onboarding. States: 1350 registered, 121 excluded, 10 missing, 8 ingested.
- lint 0 BLOCK, 5 WARN, 9 INFO (unchanged).

## [2026-11-01] schema | pack v0.2.3 → v0.2.4, glossary v0.2.1 → v0.2.2 (W-ISS-48, 50, 51; WR-073)
- `source_type` += code; `client_code` += FUWO (FOWU = typo alias); snapshot + 0-byte rows excluded; P4 newest-captured-per-hash rule.

## [2026-11-01] ingest | registry rules applied (WR-073)
- excluded: 39 `_pre-git snapshot` rows + 5 empty files; client_code FUWO on 74 rows; source_type code on 15. States: 1306 registered, 165 excluded, 10 missing, 8 ingested. lint 0 BLOCK, 5 WARN, 9 INFO.

## [2026-11-01] schema | pack v0.2.4 → v0.2.5 (W-ISS-63, WR-074)
- Extension → source_type map completed; .lnk/.zip/.pyc excluded.

## [2026-11-01] ingest | source_type backfill (WR-074)
- export 24, note 22, code 14; 5 rows excluded (registered → excluded). States: 1301 registered, 170 excluded, 10 missing, 8 ingested. No registered row has blank source_type. lint 0 BLOCK, 5 WARN, 9 INFO.
