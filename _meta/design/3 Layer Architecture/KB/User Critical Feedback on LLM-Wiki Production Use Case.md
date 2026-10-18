- "Confidence scoring" is never defined — float? enum? who computes it? how does it update?
- "Auto-crystallize sessions into knowledge" is pure magic — no extraction algorithm, no dedup, no trigger condition
- 582 nodes is tiny — that's not a knowledge graph, that's a Tuesday afternoon
- Hybrid search has no fusion strategy — BM25 + vectors + graph just means three slow things bolted together
- No latency targets — 100ms? 10 seconds? who knows?
- No accuracy metrics — NDCG? MRR? nothing
- "8-10 hours for 3A+3B" is delusional — that's a notebook hack, not production
- "We already have 60%" assumes components compose — they won't; integration is the work
- Contradiction detection on every write is AI-complete — they're not ready for that complexity
- No access control — any agent can write anything
- No versioning — can't roll back a bad crystallization
- No provenance — which agent wrote this fact? from what source?
- No consistency model — ACID? eventual? multi-agent sync needs this
- No backup or recovery strategy — corruption = game over
- No evaluation framework — how do you know if it worked?
- LLMs are treated as reliable — they'll silently corrupt the graph and you'll never know
- No human-in-the-loop for LLM failures
- No fallback when LLM API is down
- No human-readable addresses — can't cite a fact in an email or doc
- No back-links — "what points to this node?" is missing
- No time stamps — can't audit when a fact changed
- No signature or authentication — can't trust who wrote what
- No external document linking (XDoc) — Slack, email, PDFs stay outside
- The timeline assumes no bugs, no testing, no security, no rollback
- It's a product vision dressed as an architecture document


## [securityguy](https://gist.github.com/securityguy)
For what it is worth, in designing a better memory for long-running agents, I've learned a few things, in no particular order:

- Some formatting must be enforced. If you allow the agent to write .md files directly, some models will do as they are told with respect to a date header, etc., others won't. Even if you define a memory type or a status, some will use it correctly, others will ignore it. If you want a few specific fields in a particular format, either add them programmatically (like the current date) or make them required parameters in the tool call.
    
- Markdown files are great, as long as your context engine is designed to eject old/duplicate copies: Model reads file. Changes it. Reads another part. Changes it. Reads it. Appends to it. The context quickly becomes full of multiple versions of the same file.
    
- Some editing tools are byte-oriented, and they are very inefficient for manipulating md files. Some editing tools require an exact match to search/replace text. It seems straightforward, but things like different encodings, line breaks, and multiple versions in the context can be problematic. I've watched a model read the file, get the "find" part wrong, read the file again, try again, and it ends up just thrashing around and chewing through tokens until it (hopefully) hits a limit. Line-number-based tools seem to work best.
    
- Vectors, embeddings, etc. are cool, and there is no doubt in my mind that they are useful for RAG or where the LLM needs to search through new information. However, I've been able to get good results without it by combining:
    

a) Basic keyword search  
b) Instruct the LLM and allow it to set a list of keywords that, when present in a message, result in a RAG-like addition to the context  
c) Instruct the LLM and allow it to set tool names or tool prefixes that result in the same

For example, my agent that handles email triage will tag the data such that when an email MCP tool is used, relevant data is automatically pulled into the context. Another agent tags information on how I want weather presented so that whenever it uses a tool to retrieve the forecast, the instructions are automatically pulled in.

To be clear, I'm not claiming this is better than vectors, but it gets the job done quite well without requiring a vector database, embeddings server, etc.

- Periodic message scans and consolidation: I've found that providing the model with memory tools and instructions on how to use it works reasonably well. But, every so often, a model fails to recognize that it should add something to memory, or ends up with conflicting instructions in memory. My solution has been to temporarily maintain a copy of every message and periodically process them to extract additional information that should be in memory and/or resolve conflicting memory info.

# [XBlueSky](https://gist.github.com/XBlueSky)
I increasingly think the hard part of an LLM wiki is not retrieval — it is making the compiled memory trustworthy.

A few failure modes surprised me:

1. **Capture pipelines should fail open.** A transcript-filter payload drift silently produced unusable records for two weeks before I noticed it. The mistake was architectural: every compression/filtering stage is optional, but one exception could discard the whole session. The recorder now degrades per stage, preserves the raw content on failure, logs redacted diagnostics, and only moves a completed temp file into the vault after rendering succeeds.
    
2. **Provenance and identity are harder than summaries.** SessionEnd can fire repeatedly on a growing transcript, so I reclaim strict-prefix snapshots — but only within the same repo. A real vault exposed a cross-repo prefix pair where deleting the shorter copy would have erased that repo's only record for months. Separately, a whitespace difference around a distillation marker changed source hashes and made already-distilled records look modified. I ended up validating the fix against 1,174 real Raws and their pre-marker git blobs.
    
3. **Ranking, score, and retrieval provenance are different things.** Cortexes uses BM25 + vector search with RRF. Originally a BM25-only hit could rank #1 while exposing `score: 0.0`; the agent interpreted that as low confidence even though the ranking was correct. Fixing the prompt wasn't enough — hybrid-only hits now get their cosine backfilled, and repo/type/category filters are evaluated consistently by vector, BM25, and graph streams.
    

The pattern I keep seeing is that automatic capture is easy. The real system is everything that prevents silent loss, duplicate memory, stale state, misleading confidence, and accidental over-retrieval.