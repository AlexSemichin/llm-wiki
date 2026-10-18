Conflict and entity resolution belongs at write time, and the  
reason is structural rather than stylistic.

A lint pass has to _find_ the contradiction before it can resolve it, and  
finding it is the expensive half: two pages that disagree are discoverable only  
by reading both and noticing. That is quadratic in pages, it runs on every  
sweep, and an LLM adjudicates each comparison. At write time the comparison is  
already local & you hold the arriving assertion and the one it lands on. The  
cost collapses to a lookup.

The price is that you must declare in advance which claims are mutually  
exclusive. We do that with predicate groups: sets of relations that cannot  
simultaneously hold between the same ordered pair. On company filings,  
`{generates_cash_flow, consumes_cash}` and `{grounds, certifies}` are two of  
eight. A later document asserting one against a pair that already holds the  
other closes the earlier edge. No sweep, no adjudication, no second LLM call.

Two design rules make this work on real corpora.

**Order by document, never by extracted dates.** The intuitive design asks the  
model when each fact was true and sorts on that. It does not survive contact  
with source material: models state a period only when the text happens to say  
so, which is rare. Document order is always available - publication order for a  
book series, fiscal year for filings, ingest order for everything else - and it  
is robust to backfilling. Index 2019 filings after 2024 ones and resolution is  
still correct, because the declared order governs, not the write order.  
[@gowtham0992](https://github.com/gowtham0992)'s use of git history to spot stale memories is the same instinct;  
the repository already knows which assertion came later, and that ordering is  
more reliable than anything a model will tell you about when something was  
true.

**Close, never delete.** A superseded edge is marked and timestamped, and stays  
retrievable on request. This is the gist's own "compounding artifact" argument  
taken to its conclusion: a wiki that silently overwrites yesterday's claim is  
worth less than one that can show you the succession.

It fires on ordinary prose, not just structured filings. On the d'Artagnan  
trilogy - three novels, ~645k chars, indexed in publication order - thirteen  
relationships were closed by a later book, including the `ally_of` edge between  
d'Artagnan and Aramis once a later volume recasts them as opponents. The  
extractor supplied no dates for any of those pairs.

**The pattern needs a second clock.** "What is true" and "what did this system  
believe in March" are different questions with different answers, because a  
source published today can restate a figure from 2019. Both need to be  
recoverable, and the second is the one that matters when someone asks why a  
decision was made. Model them as separate axes - valid time for when a fact  
held in the world, belief time for when the system came to hold it - and  
reproducing a past answer is a query parameter rather than an archaeology  
expedition through old snapshots. Markdown makes this genuinely hard; it is the  
strongest argument for structure I know.

---

**What this is worth, on benchmarks built around exactly this problem.**

LongMemEval is long-horizon chat memory, and two of its six categories are the  
gist's problem directly: knowledge-update asks whether a fact can be  
distinguished from the fact that replaced it, and temporal-reasoning asks for  
ordering and intervals. Full benchmark, nothing sampled, against Zep/Graphiti's  
published figures:

||ours (gemini-3.6-flash)|Zep (gpt-4o)|
|---|---|---|
|temporal-reasoning|**96.2%**|62.4%|
|knowledge-update|**94.9%**|83.3%|
|multi-session|**90.2%**|57.9%|
|overall|**94.0%**|71.2%|

A full-context baseline that simply puts the entire history in the prompt  
scores 60.2% - worth keeping in mind whenever someone suggests a long context  
window makes this architecture unnecessary.

Read that as informative about the tier rather than a controlled head-to-head:  
their figures are as published, judged by a single gpt-4o where ours is a  
three-model panel, and two years separate the model generations in a direction  
I cannot sign. One instance of 500 is excluded (a session both extraction  
prompts refused) so the denominator is 499.

The mechanism behind the temporal categories is isolable. Carrying each  
relation's validity period through to synthesis (not merely extracting and  
storing it) is worth **+38.4 points on temporal-reasoning** and **+16.3 on  
knowledge-update**, ablated paired on one fixed graph per instance so that  
re-indexing noise cannot account for it. Storing time is not the hard part.  
Rendering it into the prompt is.

**ECT-QA** is the adversarial version: earnings-call transcripts, six companies,  
sixteen consecutive quarters each, where every metric is restated every quarter  
so only the date distinguishes sixteen competing values. Under that benchmark's  
own element-wise protocol it scores **0.807 Correct** against 0.599 for TG-RAG and  
0.406/0.405 for LightRAG and GraphRAG as published - on their corpus slice with  
a judge we cannot run, so treat a few points of the margin as approximate.

The reason these are worth citing in this thread is not the ranking. It is that  
the two categories which separate systems most are the two that turn on time,  
and the gap between handling temporal evolution and ignoring it is measurable  
at benchmark scale rather than being an architectural preference.

---

**[@ShootJackal](https://github.com/ShootJackal)'s "model output as untrusted input" is the right frame, and it  
has a stricter form on the write path than on the read path.**

Verifying an answer against source files catches what the model said. The  
earlier problem is what the extractor is allowed to put into the store in the  
first place. Every extracted record passes deterministic gates before it can  
become structure, and the gates are stated as rejections rather than repairs: a  
record that cannot be made into a well-formed assertion is dropped, not guessed  
at. No placeholder structure, no vague predicates, no pronominal or conjunctive  
entity names, no bare quantities as entities, and no inverting a predicate to  
express a denial.

The placeholder rule is the one I would argue hardest for. A synthesised  
stand-in written so the pipeline can continue is indistinguishable from genuine  
extracted structure once stored, so a transient provider outage mid-run  
permanently poisons the store; and nothing downstream can tell. Failing the  
chunk loudly is the only option that keeps the artifact trustworthy. A wiki that  
compounds is a wiki whose early errors compound too.

---

**Two operations in the gist get easier once the structure is a graph, and  
both for the same reason: they become computed rather than adjudicated.**

_The index._ [@kriss-b](https://github.com/kriss-b)'s observation that the Statement of Applicability  
naturally becomes the index is, I think, the general case; every wiki grows  
one, and maintaining it by hand is where the maintenance burden the gist warns  
about actually lands. A clustered graph generates it instead. We cluster  
entities into communities, summarise each, and then build a topic tree above  
them by recursive supergraph clustering: one node per cluster, edge weights  
summed across the cut, re-cluster, repeat per level.

The recursion is the part that matters, and it is worth being precise about  
why. A hierarchy built by sweeping a resolution parameter gives you levels but  
guarantees nothing about containment - children can sit outside their parents.  
Any drill-down built on such a tree is lying: you click a topic and get  
material that is not in it, or miss material that is. Recursing over the  
supergraph guarantees nesting by construction, because level _n+1_ is built  
from level _n_'s own nodes. Parent summaries are synthesised from child  
summaries rather than from raw relations, which caps the added LLM cost at  
roughly the cluster count per level rather than re-reading the corpus.

The practical effect is a wiki index at several zoom levels that nobody  
maintains, and that cannot drift from the pages beneath it, because it is  
derived from them.

_Lint's other half._ The gist's lint pass looks for contradictions and gaps.  
Contradictions are handled at write time, above. Gaps are the harder question,  
because a wiki cannot normally tell you what it does not cover - absence has no  
page. Recording which entities and communities each query touched turns that  
into arithmetic: which regions of the corpus have received least retrieval  
attention, and which entities have never been retrieved at all. Not an LLM  
judging completeness, just a count over what was actually read. Storing a hash  
of the query rather than its text keeps the telemetry from becoming a second  
sensitive dataset.

The pattern across all three (conflicts, index, gaps) is the same, and  
[@wy-cats](https://github.com/wy-cats) found the same edge from a different direction in discovering that  
"pending ingest" works better as computed state than as an explicit flag. A  
flag has to be maintained and can be wrong; a computed value cannot drift from  
what it describes. An LLM sweep is the expensive way to rediscover something  
the write path, a clustering, or a counter already knew.

---

One thing worth instrumenting, because it is invisible to every metric this  
architecture naturally produces.

Between the retriever and the model sits an assembler that fits retrieved  
material into a token budget. Any assembler that fills greedily and stops at  
the first oversized passage will silently contribute nothing from that channel  
and a wiki page or a filing section is routinely larger than a per-channel  
budget. The model then answers "no information available" while holding the  
answer, unread, in material that was retrieved successfully.

Retrieval metrics cannot see this. They are computed over what was found, not  
over what survived into the prompt; recall@k reads as perfect throughout. On  
LongMemEval the gap between clipping oversized passages and dropping them is  
eight points of end-to-end accuracy - larger than most differences between  
retrieval strategies, and attributable entirely to the step after retrieval.

Log how many retrieved characters actually reach the model. One number, and it  
makes the whole failure class visible.

---

On markdown versus structure: markdown is readable, diffable and hand-editable,  
and a graph gives all three up. Which side wins depends on whether your wiki is  
read mostly by people or mostly by systems.

Both layers are open source and run entirely on PostgreSQL with pgvector for  
similarity, ordinary tables for the graph, one backup, one transaction spanning  
your graph and your application rows. No additional services.

- `post-graph-rag` => the retrieval layer described here:  
    [https://github.com/crajah/post-graph-rag](https://github.com/crajah/post-graph-rag)
- `post-graph` => the graph substrate alone, no LLM dependency:  
    [https://github.com/crajah/post-graph](https://github.com/crajah/post-graph)
- Evaluation and method: [https://arxiv.org/abs/2608.24921](https://arxiv.org/abs/2608.24921)

Entity resolution across documents and structural negation so "not a  
subsidiary of" is never retrieved as "subsidiary of" are the other two write-  
path problems worth comparing notes on.