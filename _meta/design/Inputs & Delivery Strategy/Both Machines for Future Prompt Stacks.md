### 2. Both machines, for future prompt stacks

This is the wiki and schema folders, per WR-030.

**One-time setup:**

1. **You:** create a private, empty GitHub repo, for example `amazon-llm-wiki`.
2. **You:** sign in on each machine. Git Credential Manager prompts on the first push on Windows. On the Mac, run `gh auth login` or use GitHub Desktop. I never handle credentials.
3. Exclude `Wiki/LLM-Wiki/` from Obsidian Sync on both devices (Sync settings → excluded folders). That makes git the only thing moving this folder.
4. **Windows:** `git clone <repo URL> "D:\!ObsidianVault\Wiki\LLM-Wiki"`. I add the same two config files. Commit and push.
5. **Mac:** clone the same repo into `/Users/CommerceMindCloud/Wiki/LLM-Wiki`.

**Every session:**

|When|Command|
|---|---|
|Start|`git pull --ff-only`|
|End|`git add -A && git commit -m "<message>" && git push`|
|Rule|Never edit on both machines without a pull in between. One repo per prompt stack, same pattern for each.|