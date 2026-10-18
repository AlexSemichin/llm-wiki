Cortex is a self-hosted memory system for a private Markdown knowledge base. Git owns the durable notes, every note write becomes a commit, and an MCP server makes the same memory available across compatible AI clients.

The part we kept running into was trust.

A compiled wiki can become confidently wrong. Once an unsupported answer is filed back into memory, later agents can treat the fabrication as a source. Cortex therefore treats model output as untrusted input and surrounds it with narrower, deterministic checks.

brain_ask reads a bounded pack of actual notes, asks a reader model, then checks the quoted evidence against the cited file at the corpus commit. A verified quote proves that the text exists there. It does not pretend to prove that the source is true or that the answer follows from it. Corrected, superseded, ambiguous and missing evidence receive different visible outcomes.

Writes also depend on who is asking. Trusted clients receive the complete toolset. A guest receives only a scoped ask tool and a proposal tool. A guest proposal cannot commit a note. A trusted user must review and accept it first.

For retrieval, we retired ranking over generated one-line index summaries. The navigational index remains, but the production shortlist uses BM25 over full note text under explicit context budgets. The repository includes a retrieval harness that pins evaluations to a corpus commit and reports rank recall, strict phrase recall, pack size and named misses. A new deployment inherits none of our measurements and must establish its own.

Cortex also maintains working context separately from durable notes, assembles cited project handoffs, builds derivable graph edges, and surfaces stale verification stamps, correction chains, superseded links, secret-shaped text and other maintenance problems through an operations dashboard.  
What it does not yet have is equally important: it is not currently a complete raw-source compiler like the ingest flow proposed in this gist, it is not an offline-first local-model application, and named collaborator permissions remain future work.

The DOC.HTML proposal in this thread is interesting to us, particularly its section manifests, character budgets and per-section witnesses. Our current view is that HTML should first be tested as a derived verification and selective-hydration format. Git-backed Markdown remains the canonical source until another representation wins on recall, token cost, latency and failure behavior.  
I would especially value criticism from anyone who has measured long-lived memory poisoning, section-level hydration, or contradiction handling on a real evolving corpus.

AGENTS.md and CLAUDE.md are useful, but they are client-specific instruction files. Merely placing them beside each other does not give ChatGPT and Claude shared context. Building parallel stacks of SYSTEM.md, MEMORY.md, TASK.md, and similar files can also create duplication and drift.

The architecture we use with Cortex is:

1. One canonical, Git-backed Markdown corpus.
2. One MCP server in front of it.
3. Thin client-specific instructions telling each model how to use the same tools.
4. Every new session reads shared context, then writes durable results back to the corpus.

Claude Code can use CLAUDE.md. Codex can use AGENTS.md. ChatGPT can connect through MCP where that integration is available. Those files are adapters, while Cortex is the shared memory layer.  
Both models can use Cortex simultaneously, but they share durable state, not a hidden live conversation. If Claude records a decision, ChatGPT sees it when it next queries Cortex. For safer collaboration, trusted clients can write directly while guest clients can only ask questions and propose changes for human review.

Simultaneous writes still require normal conflict handling. A conservative setup gives one client trusted write access and lets the others submit proposals.

That is the core idea behind [Obelyth Cortex](https://github.com/Obelyth/cortex): one memory service, multiple model adapters. OpenAI also documents remote MCP servers for [ChatGPT integrations](https://developers.openai.com/api/docs/mcp).

So I would simplify the proposed structure to this:  
One canonical memory layer, thin instructions for each client, and MCP as the shared interface.