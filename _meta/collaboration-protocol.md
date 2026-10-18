---
id: META-PROC-001
title: "Human + Claude collaboration protocol"
genre: PROC
page_status: candidate
page_version: 0.2.0
recorded: 2026-10-17
supersedes: T1_collaboration-protocol_v0.1.md (on ruling)
---

# Human + Claude collaboration protocol v0.2

PURPOSE — Keep every change to the vault, the wiki and the prompt stacks traceable, reversible and owned by exactly one party.

## 0. Git in 60 seconds

- Git only watches the folder it was started in. Today that is exactly one folder: `/Users/CommerceMindCloud/PPC`.
- Every git command must run **inside** that folder. Outside it, git answers `fatal: not a git repository`.
- A **commit** is a saved snapshot you can return to. Nothing is protected until it is committed.
- Both of us commit under your name. The message prefix says who made the change: `Alex:` or `Claude:`.

**Open Terminal in the right place (do this first, every time):**
```
cd /Users/CommerceMindCloud/PPC
```

## 1. Who edits what

| Wiki layer | Owner | You edit by hand? | Claude edits? |
|---|---|---|---|
| raw (your notes, sources, exports) | You | Yes, freely | Only by explicit ruling |
| wiki (pages Claude compiles) | Claude | No. Use rule 7 | Yes |
| schema (CLAUDE.md, subject pack, glossary) | Shared | Through a ruling in chat | Proposes; you promote |
| prompt stacks (live runtime files) | Shared | Only between runs, with a version bump | Proposes the diff |

## 2. Rules with your actions

### Rule 1 — Start a session

Paste this as your first message:
```
Session open. Read claude/wiki-ledger.md and restate: scope, artifact versions, open rulings, next step.
```

### Rule 2 — Commit your own changes before you give Claude a write task

1. Run:
   ```
   cd /Users/CommerceMindCloud/PPC
   git status
   ```
2. If it says `nothing to commit, working tree clean` → stop. Nothing to do.
3. If it lists files → run:
   ```
   git add -A
   git commit -m "Alex: <what you changed, 3-6 words>"
   ```

### Rule 3 — Commit Claude's changes after Claude writes

1. Read the last line of Claude's reply: `PPC touched: yes — commit message: "Claude: …"` or `PPC touched: no`.
2. If `no` → do nothing.
3. If `yes` → run:
   ```
   cd /Users/CommerceMindCloud/PPC
   git add -A
   git commit -m "Claude: <message Claude gave you>"
   ```

### Rule 4 — Look at what changed before you commit

```
git diff --stat
```
Shows which files changed and how many lines.
```
git diff
```
Shows the exact lines: red = removed, green = added. Press `q` to exit.

### Rule 5 — Check Claude's claims against evidence

| Claim Claude makes | Your check |
|---|---|
| "I committed / you committed X" | `git log --oneline -5` → the message must be in the list |
| "I changed files A, B" | `git show --stat HEAD` → lists files in the last commit |
| "Folder is clean" | `git status` → `nothing to commit, working tree clean` |
| "I wrote file F" (outside PPC) | Open F in Obsidian. Files outside PPC are not in git |

### Rule 6 — Hand files over through `_exchange`

- **You → Claude:** put the file in `Wiki/Build/_exchange/to-claude/`. Tell Claude the filename.
- **Claude → you:** Claude puts drafts in `Wiki/Build/_exchange/to-alex/`.
- Do not paste long content into chat.

### Rule 7 — Correct a wiki page

1. Open the wiki page itself in Obsidian.
2. Add a line directly under the wrong statement:
   ```
   > ALEX: <what is wrong and what it should say>
   ```
3. Tell Claude: `Resolve ALEX notes in <page name>.`
4. For corrections that span many pages: create one note in `_exchange/to-claude/` listing them.

### Rule 8 — Edit frontmatter safely

1. Edit it only in source mode (Cmd+E toggles) or in the Properties panel.
2. Never move or delete the two `---` lines.
3. Never add `#` comments inside frontmatter.

### Rule 9 — Prompt-stack files

1. Never edit a prompt-stack file while a run is in progress.
2. Every change gets a new version number and one changelog line, written by Claude.

### Rule 10 — Correct Claude once, explicitly

Say: `Correction: <what was wrong> → <what is right>.` A correction seen twice becomes a proposed schema rule.

### Rule 11 — Decisions live in chat

Answer Claude's open items in chat. Claude writes them to the ledger as WR- rows. Do not record decisions inside notes.

### Rule 12 — Close a session

Paste:
```
Session close. Update claude/wiki-ledger.md and give the continuation seed.
```
Then run Rule 2 once more if you edited anything in PPC.

## 3. Undo (emergency)

| Situation | Command (inside PPC) |
|---|---|
| Throw away uncommitted changes to one file | `git restore "<path/to/file.md>"` |
| Throw away ALL uncommitted changes | `git restore .` |
| Undo the last commit, keep a record of the undo | `git revert HEAD` |
| See an old version of a file | `git log --oneline -- "<path/to/file.md>"` then `git show <commit-id>:"<path/to/file.md>"` |

When unsure: do nothing, paste the Terminal output into `_exchange/to-claude/`, and ask.

## 4. Gate (checkable)

- `git status` is clean at session start and at session end.
- Every commit message starts with `Alex:` or `Claude:`.
- Every ruling made this session has a WR- row in the ledger.

## 5. Provenance

| Claim | Tag | Basis |
|---|---|---|
| Layer ownership | [D] | Karpathy blueprint (WR-013) |
| Human write gate; git as audit | [U] | KB: Schema & Lifecycle critique; Cortex gist |
| Repeated correction → rule | [D] | Harness improvement loop (WR-012) |
| Git command behaviour | [V] | Verified on this repo: commits e8b0398, 37b1ae6, 791991b |
