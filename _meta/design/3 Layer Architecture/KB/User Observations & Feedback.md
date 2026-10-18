This release is entirely things people raised here about keeping the wiki honest:

1. **Sources vs. wiki are separate retrieval layers.** Your own notes / imports are indexed as `source`, AI-written pages as `wiki`. Answers prefer your material and every citation is tagged so you can see which is which.
2. **`[@path]` citations on every page the LLM writes**, added deterministically even when the model forgets. Pages without a source and sources never cited are lint findings computed in code, not by the model.
3. **Evidence-verified lint.** Contradiction / stale findings must carry verbatim quotes; the server checks each quote against the page and drops findings that don't hold up. Cards show `✓ verified` per quote.
4. **Free-text captures land in your layer first** (`sources/contributors/<you>/<date>.md`) before the wiki is touched, so nothing the LLM writes is un-citable.
5. **Duplicate-page guard + "state rule"** — the maintainer can't create a page that already exists (case/separator-insensitive), and prompts document the _shape_ of things, never live values like SHAs or counts.

