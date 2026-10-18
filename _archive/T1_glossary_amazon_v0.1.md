# T1 GLOSSARY — Amazon LLM Wiki v0.1 [A3,A4]

status: CANDIDATE (promotion = human ruling) | date: 2026-10-15 precedence: Karpathy blueprint (WR-013) > this glossary > 01_L1_glossary_v1.0.0 (amplification only) rule: one term, one meaning. A bare polysemous word is banned when a locked compound exists.

## 1. Disambiguated terms (polysemy → locked terms)

|Bare word (banned bare)|Locked term|Meaning|Values / example|
|---|---|---|---|
|layer|`harness_layer`|Project-instruction derivation level|L0–L4|
|layer|`wiki_layer`|Karpathy storage layer|raw · wiki · schema|
|layer (waterfall)|`harvest_stage`|Position of a search term in the keyword harvesting waterfall|discovery · validation · scale|
|layer (optmyzr_layer)|`tool_surface`|Part of a tool where a rule is implemented; paired with `tool`|tool: optmyzr · tool_surface: rule-engine \| recipes|
|tier (disclosure)|`disclosure_level`|How much of a page may be exposed outside the owner|SHOW · SKELETON · GUARD|
|tier (SKU)|`sku_tier`|Revenue-contribution class of a SKU|A · B · C|
|tier (harness T0–T2)|`project_tier`|Which project holds the knowledge|T1 subject (this wiki) · T2 client|
|level (Pearl)|`causal_level`|Strength of a causal claim|association · intervention · counterfactual|
|level (autonomy)|`autonomy_level`|What an agent may do without human sign-off|inform · recommend · execute_report · delegate|
|stage (Davenport)|`analytics_maturity`|Analytical depth of an output|descriptive · diagnostic · predictive · prescriptive|
|stage (funnel)|`funnel_stage`|Buyer-journey position targeted|tofu · mofu · bofu · retention (see §3 A-05)|
|stage (build plan)|`build_phase`|Position in the wiki build plan|P0–P7|
|status|`page_status`|Knowledge lifecycle of a wiki page (stored)|seed · candidate · promoted · superseded|
|status (captured/indexed)|`index_state`|Whether a page is listed in index.md (COMPUTED, never stored)|listed · unlisted|
|status (stub-source-missing)|`completeness`|Coverage of the raw source|full · partial · stub|
|status (guarded)|→ `disclosure_level: GUARD`|—|—|
|tag ([V]/[D]/[U]/[X])|`prov_tag`|Provenance tag of a claim|V · D · U · X|
|tags (Obsidian)|`tags`|Topical keywords for search only; carry no provenance meaning|free list|
|schema (Karpathy)|`wiki_schema`|CLAUDE.md + this subject pack|—|
|schema (genre)|genre `DATASPEC`|Page that specifies a business data structure|fact tables, naming codes, report fields|
|log (Karpathy log.md)|`log.md`|Append-only record of wiki operations|`## [YYYY-MM-DD] op \| title`|
|log (genre)|genre `DEC`|Dated record of one business decision with rationale and outcome|bid change, price move|
|policy (codified rule)|genre `DECRULE`|Standing if-then rule for a recurring decision|"IF catalog >80 SKUs THEN rainbow portfolios"|
|policy (Amazon)|entity `AmazonPolicy`|A rule published by Amazon (TOS, category, ads policy)|—|
|gate (harness)|`gate`|Predicate set a candidate must pass for promotion|—|
|gate (ops check)|`ops_check`|Operational check on a recommendation, with severity|severity: WARN · BLOCK|
|hard gate|`hard_constraint`|Non-negotiable account/client limit an agent must never cross|max daily spend; no competitor brand terms|
|dimension (campaign)|`campaign_setting`|A configurable campaign parameter; every campaign_setting is a lever|budget, bid strategy, TOS modifier|
|dimension (Kimball)|`dimension`|Categorical slicer of a metric|period, ad_type, match_type|
|model (theory)|`model`|Theory-based, subject-generic construct|Pearl ladder|
|model (LLM)|`llm`|Language model that produced or judged text|claude-opus-5-5|
|model (data)|→ genre `DATASPEC`|—|—|
|source (file)|`raw_source`|Immutable file in wiki_layer raw|raw/ppc/img16.png|
|source (format)|`source_type`|Format of a raw_source|llm-session · article · export · whiteboard-image · note · transcript|
|source (knowledge method)|`method_class`|Epistemic method behind a claim|expert_opinion · extrapolation · econometric · data_multivariate · intentions · role_play|
|scope (project)|`project_scope`|H§2 boundary|—|
|scope (claim)|`evidence_scope`|How far a claim may be generalized|entity_only · domain · global|
|type (entity)|`entity_type`|Kind of Amazon thing a page is about|ASIN, Campaign, Keyword, Fee…|
|type / category (page)|`genre`|Function of a page|see §2|
|atomic (fact)|`atomic_fact`|Smallest independently verifiable claim|—|
|atomic (account)|`atomic_waterfall`|Account-structure philosophy|—|
|recipe|`tool_recipe`|Tool-specific automation bundle (Optmyzr recipe)|—|
|portfolio|`ads_portfolio`|Amazon Ads portfolio container|—|
|intent (naming)|`intent_segment`|Naming-code slot for search intent|BRAN, COMP, GENE (definitions pending §4)|
|version|`page_version` / `schema_version`|Page edit version / wiki_schema version|semver|

## 2. Genres (12)

|Genre|Definition|Split rule|
|---|---|---|
|REF|Foundational business logic, definitions, formulas, rationale|Explains why/what; no ordered steps|
|PROC|Ordered sequence of ≥2 steps with a trigger|Says how to execute a process end to end|
|TECH|Specific algorithm or technique used in executing a task or process (user, WR-017)|One reusable method; invoked by ≥1 PROC via `uses_technique`|
|DATASPEC|Specification of a business data structure|Business data, never the wiki itself|
|MAP|Cross-references, dependencies, routing between entities|Relations only, no new claims|
|META|Structure of the wiki itself (naming, directory, index rules)|Lives in wiki_layer schema|
|TEMPL|Output shape to be filled|Has blanks; no execution steps|
|DIAG|Evaluation of a state → scored output|Input state → score/verdict|
|CASE|Anonymized empirical record from a real account|Enters only via the T2→T1 hop; never names the client|
|GLOSS|Term definitions|One term per row|
|DEC|Dated record of one decision|Instance; carries rationale, alternatives, outcome|
|DECRULE|Standing if-then rule for a recurring decision|General; carries autonomy_level + hard_constraints|
|Dropped: PROTO → `page_status: seed` plus `experimental: true` on any genre (I-F03).|||

## 3. Open ambiguities

- A-05: The exemplars use tofu/mofu/bofu; the reporting framework uses awareness/consideration/conversion/retention. Proposed mapping tofu=awareness, mofu=consideration, bofu=conversion, retention=new value. [U] until you confirm.

## 4. Abbreviation backlog (definitions = human only; Claude never invents)

BRAN DEF, GENE, COMP, ATT, RANK, SUBST, CLOSE, AAA+, DTPRF, Rainbow, SKAG, SAG, STAG, Hagakure, TOS modifier, New Customers to Small (?), Average Cost of Real Sale (?) Source for full extraction: read-only scan of the PPC vault (E-D7).