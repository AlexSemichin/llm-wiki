**Habits this setup needs (2.2):**

1. Each folder has exactly one active repo at a time.
2. Obsidian Sync and git never both move the same folder.
3. Before Windows touches git, set it up for both systems:
    - `core.longpaths=true` (lifts the path limit);
    - `core.filemode=false` (ignores permission differences);
    - a `.gitattributes` file containing `* text=auto eol=lf` (one line-ending style);
    - a `.gitignore` covering `.DS_Store`, `Thumbs.db`, `.obsidian/workspace*` and `.trash/` (keeps system and Obsidian clutter out).
4. For the wiki layer: pull, work, commit, push. Never edit offline on both machines at once.
5. I only write on the machine this session is linked to, and each write session is recorded in log.md.

**One is.** The two copies hold one set of content, but they are two separate copies. With asynchronous sync, there are moments when the Mac has an edit Windows hasn’t received yet. In those moments the copies differ, and if both machines touch the same file, one side has to win. So exactly one machine must be the authority.

**Windows `D:\!ObsidianVault` is canonical (WR-029).** The Mac is a travel copy. It’s authoritative only for edits made on it, until they’ve synced.

**What git changes:** git keeps history, and history doesn’t merge the way files do. Only one machine can own the history at a time.

### 3. What running git on two machines means

**What can go wrong:**

|Hazard|In your setup|Severity|
|---|---|---|
|**Two sync systems moving the same files.** Obsidian Sync carries a git pull from one machine to the other, where it shows up as fresh edits and gets committed a second time, giving duplicate commits and conflicts.|It would happen as soon as both machines have a repo|**High**|
|Obsidian Sync might also sync the hidden `.git` folder. My understanding is that it skips hidden folders, so your history would exist only on the Mac, but I’m not certain. If it does sync `.git`, two machines would write into one history through a laggy sync, which risks corrupting it.|Not verified|**High until checked**|
|Windows has a 260-character path limit|Your longest path would be 252 characters on Windows. 39 files are over 200.|Medium|
|Windows and Mac end lines differently (CRLF vs LF)|Without a rule, every file can show up as entirely changed|Medium|
|File permissions differ between the systems (`filemode=true` on the Mac)|Shows phantom changes|Low|
|`.DS_Store` (a Mac system file) got committed|Noise in history|Low|
|8 file names contain an em dash|Fine on both systems as long as the Mac setting `precomposeunicode=true` stays on (it is on)|Low|

**Decision: split by wiki layer, with exactly one channel per folder.**

|Wiki layer|Moves between machines via|Git’s role|Why|
|---|---|---|---|
|**raw** (your existing vault: PPC and the rest)|Obsidian Sync, as now|A safety-snapshot repo on the machine I’m working on, made only before bulk edits. The Mac repo serves while you travel. On your return, start a fresh baseline on Windows and stop using the Mac repo.|Raw sources are almost never edited after the one-time cleanup in P4, so snapshots are enough.|
|**wiki + schema** (the new wiki, CLAUDE.md, prompt stacks)|**git only**, through a private GitHub repo. Exclude this folder from Obsidian Sync on both machines.|Full history: pull before a session, commit and push after it|This is the part you actually want version-controlled, and keeping Obsidian Sync off it removes the double-sync problem.|