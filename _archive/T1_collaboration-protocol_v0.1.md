---
id: META-PROC-001
title: "Human + Claude collaboration protocol"
genre: PROC
page_status: candidate
page_version: 0.1.0
recorded: 2026-10-17
---

# Human + Claude collaboration protocol v0.1

PURPOSE — Keep every change to the vault, the wiki and the prompt stacks traceable, reversible and owned by exactly one party.

## 1. Who edits what (Karpathy wiki layers)

| Wiki layer | Owner | You may edit by hand? | Claude may edit? |
|---|---|---|---|
| raw (your notes, sources, exports) | You | Yes, freely | Only by explicit ruling (e.g. E-D2, P4 normalization) |
| wiki (pages Claude compiles) | Claude | Read only. Correct by telling Claude, or by a comment line `> ALEX: …` that Claude resolves | Yes |
| schema (CLAUDE.md, subject pack, glossary) | Shared | Through a ruling in chat | Proposes; you promote |
| prompt stacks (live runtime files) | Shared | Only between runs, with a version bump | Proposes the diff |

## 2. Rules

1. Exactly one writer per file per turn.
2. Hand files over through `Wiki/Build/_exchange/`, not by pasting large content into chat.
3. Commit before you hand Claude a write task.
4. Commit after Claude writes. Keep your commits separate from Claude's.
5. Review changes with `git diff`, not by re-reading whole files.
6. Make decisions in chat. Claude logs them in the ledger. Do not decide inside notes.
7. Edit frontmatter only in source mode or in the Properties panel.
8. Never move or delete the `---` lines that fence frontmatter.
9. Keep frontmatter free of comments.
10. Never edit a prompt-stack file during a live run.
11. Change a prompt-stack file only with a version bump and a changelog line.
12. Correct a Claude error once, explicitly. A correction seen twice becomes a proposed schema rule.
13. Verify Claude's claims against evidence (git log, file content), not against Claude's statements.
14. Open each session by pointing Claude at `claude/wiki-ledger.md`. Close each session with the continuation seed.

## 3. Gate (checkable)

- `git status` is clean at session start and at session end.
- Every wiki-layer file changed this session has exactly one author in its commit.
- Every ruling made this session has a WR- row in the ledger.

## 4. Provenance

| Claim | Tag | Basis |
|---|---|---|
| Layer ownership | [D] | Karpathy blueprint (WR-013), raw immutable / wiki LLM-owned |
| Human write gate, git as audit | [U] | KB: Schema & Lifecycle critique; Cortex gist |
| Repeated correction → rule | [D] | Harness improvement loop (WR-012 adoption) |
