Wiki/
  LLM-Wiki/            ← its own git repo; only Claude writes here
    CLAUDE.md          ← the schema's entry point
    index.md · log.md
    schema/            ← subject pack, glossary, abbreviations, frontmatter spec
    wiki/              ← compiled pages, by domain
    _meta/design/      ← Core, KB, Inputs (moved from Build)
  Build/_exchange/     ← temporary hand-off folder

### Separating the LLM wiki from your own notes

**Folder:** everything I write goes in `Wiki/LLM-Wiki/`. Everything else in the vault is yours, the raw sources.

The boundary is enforced in four ways:

1. **Git boundary:** `LLM-Wiki` is its own repo, separate from your notes.
2. **Write scope:** I write only to `LLM-Wiki/` and `_exchange/`, plus the raw edits you approve by ruling.
3. **Frontmatter:** every wiki page carries `producer: llm`.
4. **Visual:** in Obsidian, open the Graph view settings, add a Group for `path:Wiki/LLM-Wiki`, and give it its own color. My pages then stand apart at a glance.

### Vaults Separation
| Factor                                     | One vault, two parts                     | Two vaults                                                  |
| ------------------------------------------ | ---------------------------------------- | ----------------------------------------------------------- |
| Wiki pages link to your notes with `[[…]]` | Yes                                      | **No.** Obsidian links don’t work across vaults.            |
| One graph and one search                   | Yes                                      | No                                                          |
| Obsidian Sync cost                         | 1 vault                                  | 2 vaults. Plan limits vary, and I haven’t checked them [U]. |
| Separation strength                        | Folder + git + write scope + frontmatter | Physical                                                    |

### Fontmatter management
**Your question surfaced a better P4 (W-ISS-19).** As planned, P4 writes frontmatter into about 156 of **your** notes. A cleaner option:

- **What changes:** leave your notes untouched and record their metadata in a registry inside the wiki (`_meta/source-registry.csv`).
- **Why it’s better:** it follows “raw stays untouched”, it removes the frontmatter-damage risk from W-ISS-15 entirely, and it keeps the boundary between your notes and mine clean.
- **What it costs:** Dataview and Bases can’t filter your own notes by those fields.

**Decision: use the registry. Don’t backfill your notes.**

- **Evidence:** [D], from the Karpathy blueprint plus W-ISS-15.
- **Confidence:** medium. The uncertainty is whether you actually filter your own notes with Dataview.
- **What would overturn it:** you need Dataview or Bases queries over your own notes by type or domain at least weekly. Then backfill instead.