## PURPOSE

This document maps the epistemological and decision-theoretic foundations of six pioneering traditions to the operational reality of Amazon PPC monthly performance reporting at AMZ Clever. Each reporting module names its theoretical grounding. The goal: make every section of a client report a decision instrument, not a data dump.

---

## FRAMEWORK ARCHITECTURE

The system rests on five foundational pillars, each contributed by a specific intellectual lineage. These pillars are not decorative — they dictate what gets measured, how it gets structured, what gets communicated, and what decisions the report enables.

```
┌─────────────────────────────────────────────────────────────┐
│              DECISION-THEORETIC REPORTING SYSTEM            │
├─────────────┬─────────────┬──────────┬──────────┬───────────┤
│  PROBLEM    │  EVIDENCE   │ CAUSAL   │ DECISION │ ANALYTICS │
│  FRAMING    │  STRUCTURE  │ ENGINE   │ QUALITY  │ MATURITY  │
│             │             │          │          │           │
│  Simon &    │  Inmon &    │  Pearl   │ Howard & │ Davenport │
│  Newell     │  Kimball    │          │ Raiffa   │           │
└─────────────┴─────────────┴──────────┴──────────┴───────────┘
```

---

## PILLAR 1: PROBLEM FRAMING — Simon & Newell

**Theoretical Basis:** Bounded rationality and rational problem solving. Decision-makers operate under cognitive limits — finite attention, incomplete information, satisficing rather than optimizing. Newell & Simon's problem-space hypothesis: every business problem is a search through a space of possible states toward a goal state.

**Reporting Application:**

Every performance report must begin by defining the **problem space** the client is navigating, not by presenting data. Data without a framed problem is noise.

| Concept | Reporting Manifestation |
|---|---|
| Bounded Rationality | Reports are scoped to 3-5 actionable decisions per period — never an exhaustive data catalogue. The operator triages what the client can actually process. |
| Problem Space | Each report opens with a **Situation Frame**: current state → goal state → constraint set. E.g., "BERL is at $34K/mo revenue, targeting $50K, constrained by 25% TACOS ceiling and seasonal inventory risk." |
| Satisficing vs. Optimizing | Recommendations are framed as "sufficient improvement thresholds" not theoretical optima. E.g., "Reducing ACoS from 32% to 27% is the satisficing target; pursuing 20% risks underspending into organic rank loss." |
| Task Decomposition | Complex performance narratives are decomposed into discrete decision blocks (budget allocation, bid strategy, keyword portfolio, creative/listing, inventory). Each block is independently evaluable. |

**Template Integration Point:** This pillar governs the **Executive Summary** and **Situation Frame** sections of the Project Instructions template. The operator's first task is problem framing, not metric extraction.

**Operator Directive:** Before pulling any data, answer: *What is the client's current problem space? What are they trying to decide?*

---

## PILLAR 2: EVIDENCE STRUCTURE — Inmon & Kimball

**Theoretical Basis:** Two competing but complementary data architecture philosophies. Inmon's top-down enterprise data warehouse (EDW) provides a single source of truth via normalized schemas. Kimball's bottom-up dimensional modeling (star schema, fact tables, dimension tables) provides fast, intuitive analytical access via subject-specific data marts.

**Reporting Application:**

The reporting system needs both architectures operating simultaneously:

| Concept | Reporting Manifestation |
|---|---|
| Inmon: Enterprise Data Warehouse (Top-Down) | The **Unified Account Context** document (operational context architecture) serves as the EDW — one canonical truth source per client. All campaign data, brand rules, TACOS thresholds, funnel-stage definitions, and historical baselines live here. No report contradicts this source. |
| Kimball: Star Schema / Data Marts (Bottom-Up) | Each **reporting module** (Budget, Keyword, Campaign Type, Funnel Stage) is a subject-specific data mart. Structured as fact tables (spend, revenue, clicks, impressions) sliced by dimensions (time period, campaign type, match type, funnel stage). |
| Fact Tables | Quantitative actuals: Spend, Revenue, Orders, Clicks, Impressions, ACoS, ROAS, TACOS, CVR, CTR. These are the non-negotiable numeric spine of every report. |
| Dimension Tables | Categorical slicers: Period (WoW, MoM, QoQ), Campaign Type (SP, SB, SD, DSP), Match Type (Exact, Phrase, Broad, Auto), Funnel Stage (Awareness, Consideration, Conversion, Retention), Product/ASIN grouping. |
| Star Schema Discipline | Every metric in the report must be locatable at the intersection of one fact and one or more dimensions. If a number can't be placed in the star, it doesn't belong in the report. |

**Template Integration Point:** This pillar governs the **Operational Context Architecture** and the data extraction phases (PPT/PIT layers) of the four-layer system. The context doc is Inmon; each report section is Kimball.

**Operator Directive:** *Can every number in this report be traced to a fact-dimension intersection in the context doc? If not, the number is orphaned — fix or remove.*

---

## PILLAR 3: CAUSAL ENGINE — Judea Pearl

**Theoretical Basis:** Probabilistic causality and the causal hierarchy (Association → Intervention → Counterfactual). Pearl's framework distinguishes between seeing (correlation), doing (intervention), and imagining (counterfactual). Most reporting systems never get past Level 1 (association). Decision-useful reports require Level 2 (intervention) minimum.

**Reporting Application:**

| Concept | Reporting Manifestation |
|---|---|
| Level 1: Association (Seeing) | Descriptive metrics — "ACoS was 28% this month." This is table stakes. Every report has this. It is insufficient alone. |
| Level 2: Intervention (Doing) | Attribution of outcomes to actions — "We reduced bids on broad match by 15%, which caused spend to decrease $2.1K while revenue held, improving ROAS from 3.8x to 4.5x." The operator must identify the **intervention** and link it to the **effect**. |
| Level 3: Counterfactual (Imagining) | "Had we not paused Campaign X during the stock-out, we would have wasted ~$4.2K at a projected 0.3x ROAS." Counterfactuals justify past decisions and frame future ones. |
| Causal Chain Notation | Every performance narrative must follow the **Cause → Behavior → Effect → Performance** chain from your framework. E.g., Budget cut (cause) → reduced impression share (behavior) → fewer conversions (effect) → ROAS improved but revenue declined (performance). |
| Deterministic Link / Attribution | The root cause analysis chain: **Cause → Impact → Evidence → Attribution %**. E.g., "PPC spend reduction → $34K revenue impact → 25% cut, 4.25x ROAS lost → 35% attribution to the decline." |

**Template Integration Point:** This pillar governs the **Narrative Analysis** sections and the OCT (Operational Context Template) causal framing. Every "what happened" paragraph must include a "because" clause grounded in intervention logic, not correlation.

**Operator Directive:** *For every performance change reported, identify: What intervention caused it? What would have happened without it? State the causal direction explicitly.*

---

## PILLAR 4: DECISION QUALITY — Ronald A. Howard & Howard Raiffa

**Theoretical Basis:** Decision analysis as the application of expected utility theory to real-world problems under uncertainty. Howard formalized the six elements of decision quality. Raiffa formalized rational agency as requiring Beliefs (epistemic state), Preferences (utility functions), Actions (intervention options), and Outcomes (consequence mapping).

**Reporting Application:**

### Howard's Decision Quality Chain (applied to reporting)

| Decision Quality Element | Reporting Manifestation |
|---|---|
| Appropriate Frame | Is the report answering the right question? (Inherited from Pillar 1 — Simon) |
| Creative Alternatives | Does the recommendation section present 2-3 genuine strategic options, not just "keep doing what we're doing"? |
| Meaningful, Reliable Information | Are the metrics current, correctly attributed by funnel stage, and cross-validated? (Inherited from Pillar 2 — Inmon/Kimball) |
| Clear Values and Tradeoffs | Does the report explicitly state the tradeoff the client faces? E.g., "Scaling spend 20% will likely grow revenue 12-15% but compress ROAS from 4.5x to 3.8x. Is that acceptable?" |
| Sound Reasoning | Is the causal logic valid? (Inherited from Pillar 3 — Pearl) |
| Commitment to Action | Does the report end with a concrete decision request, not a vague "let us know your thoughts"? |

### Raiffa's Rational Agency Model (applied to reporting)

| Agency Component | Reporting Manifestation |
|---|---|
| Beliefs (Epistemic State) | What does the client currently believe about their account performance? The report must update these beliefs with evidence. Bayesian updating: prior belief + new data = posterior belief. |
| Preferences (Utility Functions) | What does the client value? Revenue growth vs. profitability vs. market share vs. organic rank defense. This is captured in the Operational Context doc and must be referenced in every recommendation. |
| Actions (Decision Options) | The recommendation section maps available actions: budget reallocation, bid adjustments, keyword portfolio changes, campaign structure modifications. Each action has an expected outcome range. |
| Outcomes (Consequence Mapping) | Every recommended action includes a projected outcome with confidence bounds. E.g., "Increasing exact match bids 10% → projected +8-12% conversion volume, ±3% ACoS impact." |

**Template Integration Point:** This pillar governs the **Recommendations & Next Steps** section and the QUIT (Quality Upgrade & Iteration Template) layer. Every recommendation must pass the Howard decision quality chain. Every recommendation must map to Raiffa's agency model (belief update → preference alignment → action specification → outcome projection).

**Operator Directive:** *Does this report enable the client to make a decision, or does it merely inform them? If the latter, it's incomplete.*

---

## PILLAR 5: ANALYTICS MATURITY — Thomas Davenport

**Theoretical Basis:** Davenport bridges symbolic AI theory to business practice through three mechanisms: (1) a translation layer that operationalizes Newell/Simon's rational problem-solving into business decision frameworks, (2) an analytics evolution narrative (4-stage model) that provides a heuristic for organizational AI adoption maturity, and (3) a decision intelligence synthesis that frames AI/ML capabilities within decision theory and integrates change management from organizational behavior.

**Reporting Application:**

### Davenport's Analytics Maturity Stages (applied to client reporting)

| Stage           | Description        | Reporting Behavior                                                                                                                                                    |
| --------------- | ------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **1. Descriptive**  | What happened?     | Metric tables, period-over-period comparisons. Every report has this. Minimum viable.                                                                                 |
| **2. Diagnostic**   | Why did it happen? | Causal narratives (Pearl's Level 2). Root cause analysis chains. This is where most agency reports fail — they stop at descriptive.                                   |
| **3. Predictive**   | What will happen?  | Trend projections, seasonality modeling, budget pacing forecasts. E.g., "At current spend rate, you'll exhaust budget by Day 22 with projected $X revenue shortfall." |
| **4. Prescriptive** | What should we do? | Decision-ready recommendations with quantified tradeoffs (Howard/Raiffa). This is the target state for AMZ Clever reports.                                            |

### Davenport's Integration Framework (applied to reporting system design)

| Integration Element        | Reporting Manifestation                                                                                                                                                                                                                     |
| -------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Decision Intelligence Loop** | The report itself is a loop: Frame problem → Gather evidence → Analyze causally → Generate options → Recommend → Client decides → Execute → Measure → Re-frame. The monthly report is one full cycle.                                       |
| **Decision Policy Engine**     | Recurring decisions (e.g., "If ACoS > threshold, reduce bids by X%") are codified as policies in the Operational Context doc, not re-derived monthly. The report flags policy triggers, not first-principles analyses of settled questions. |
| **Feedback/Update Mechanism**  | Every report includes a "What we learned this period" section that feeds back into the Operational Context doc. Beliefs update. Policies refine. The system improves.                                                                       |

**Template Integration Point:** This pillar governs the **overall report maturity standard** and the feedback loop between the QUIT layer and the Operational Context Architecture. Every report section must tag its analytics stage (Descriptive / Diagnostic / Prescriptive). The minimum acceptable standard for AMZ Clever is Stage 2 (Diagnostic) for all sections, with Stage 4 (Prescriptive) required for the Recommendations section.

**Operator Directive:** *Tag each paragraph. If you're writing "ACoS was 28%," you're at Stage 1. That sentence must be followed by a Stage 2 sentence ("because we increased broad match spend 18%") and ideally a Stage 3/4 sentence ("projecting this forward, maintaining this mix will push ACoS to ~31% by month-end; recommend rebalancing toward exact match").*

---

## SYNTHESIS: THE REPORTING EXECUTION CHAIN

The five pillars execute in sequence. This is the operational workflow:

```
**STEP 1: FRAME THE PROBLEM (Simon & Newell)**
  └→ Define situation: current state, goal state, constraints
  └→ Decompose into 3-5 decision blocks
  └→ Scope report to bounded rationality — what can client actually act on?

**STEP 2: STRUCTURE THE EVIDENCE (Inmon & Kimball)**
  └→ Pull data from canonical context doc (Inmon EDW)
  └→ Organize into subject-specific modules (Kimball data marts)
  └→ Validate: every number sits at a fact × dimension intersection

**STEP 3: BUILD CAUSAL NARRATIVES (Pearl)**
  └→ For each module, identify interventions and their effects
  └→ Construct Cause → Behavior → Effect → Performance chains
  └→ Include at least one counterfactual per report
  └→ Quantify attribution where possible

**STEP 4: GENERATE DECISION-READY RECOMMENDATIONS (Howard & Raiffa)**
  └→ Present 2-3 genuine alternatives, not a single "recommendation"
  └→ State tradeoffs explicitly (what you gain, what you risk)
  └→ Map to client preferences from context doc
  └→ Project outcomes with confidence bounds
  └→ End with a concrete decision request

**STEP 5: TAG MATURITY & FEED BACK (Davenport)**
  └→ Every section tagged: Descriptive / Diagnostic / Predictive / Prescriptive
  └→ Minimum standard: Diagnostic (Stage 2) everywhere
  └→ Prescriptive (Stage 4) required in Recommendations
  └→ "What we learned" feeds back into Operational Context doc
  └→ Policy triggers documented for next cycle
```

---

## METRIC FRAMEWORK ALIGNMENT

Your card system distinguishes **Effectiveness Metrics** from **Efficiency Metrics**. This maps directly:

### Effectiveness Metrics (Are we doing the right things?)
- Revenue Growth
- New Customers to Small (market expansion)
- Market Share
- Brand Searches (organic brand momentum)
- **Inventory: Stock-Aware Throttle** (don't advertise what you can't sell)

### Efficiency Metrics (Are we doing things right?)
- Average Cost of Real Sale (true CPA)
- Cost per Acquisition
- Budget Utilization
- Return on Investment
- Return on Ad Spend

### Scaling Governance
- **Effectiveness Bound:** TACOS — the ceiling on advertising intensity relative to total revenue. Scaling decisions reference this.
- **Efficiency Bound:** ACoS / ROAS — the floor on per-campaign return. Guard scaling (don't scale what doesn't work).
- **Defense Metric:** Organic Rank Defense — are paid campaigns protecting or building organic position?

### Optmyzr Capabilities Mapping
| Optmyzr Feature | Pillar Served |
|---|---|
| Automated Bid-to-Value, Budget Pacing | Pillar 2 (Evidence Structure) + Pillar 3 (Causal — intervention execution) |
| Budget Deviation Alerts, Campaign Optimization | Pillar 1 (Problem detection within bounded rationality) |
| Weekly/Monthly/Quarterly Performance Reports by Dimension | Pillar 2 (Kimball data marts) + Pillar 5 (Davenport maturity tagging) |
| Cross-Channel Unified/Centralized View | Pillar 2 (Inmon EDW) |
| Funnel-Stage-Specific Analytics Dashboards | Pillar 3 (Pearl — causal attribution by funnel position) |

---

## TERMINOLOGY DISCIPLINE

From your cards — three terms that must be used precisely in reports:

| Term | Definition | Usage |
|---|---|---|
| **Factor** | A variable that contributes to variance in an outcome. | "Budget allocation was a key factor in the revenue decline." (Explains variance) |
| **Driver** | A variable with demonstrated propulsive force on an outcome. | "Exact match spend was the primary driver of conversion growth." (Propulsion — magnitude + direction) |
| **Lever** | A variable the operator can directly control and intervene on. | "Bid adjustments on top-10 ASINs are the available lever for next period." (Agency — controllability + intervention capability) |

**Rule:** Never call something a "driver" unless you've demonstrated its propulsive magnitude. Never call something a "lever" unless the operator has direct control over it. "Factor" is the weakest claim; "lever" is the strongest.

---

## AUTONOMY & GOVERNANCE

From your Newell/Simon + Boole layer:

| Concept | Application |
|---|---|
| Clear Autonomy Boundaries | The operator's scope of independent action is defined in the Project Protocol. Decisions within boundaries execute without client approval. Decisions crossing boundaries require client sign-off. |
| Autonomy Levels | Level 1: Inform (report only). Level 2: Recommend (present options). Level 3: Execute-and-report (act within policy, report after). Level 4: Full delegation (operator decides and acts, client reviews periodically). Each decision block in the report should be tagged with its autonomy level. |
| Hard Gates | Non-negotiable constraints that halt execution. E.g., "Do not exceed $X daily spend," "Do not bid on competitor brand terms," "Maintain minimum 3.0x ROAS on all SP campaigns." These come from the Operational Context doc and are never overridden by the operator without explicit client authorization. |
| Explicit Tool Plans | When recommending an intervention, specify the exact tool and sequence. E.g., "Via Optmyzr: create bid rule reducing broad match bids 12% on ASINs where ACoS > 35% over trailing 14 days." |

---

## REPORT QUALITY SELF-CHECK (Operator Checklist)

Before submitting any report, the operator validates:

- [ ] **Simon Check:** Is the problem framed before data is presented? Are there ≤5 decision blocks?
- [ ] **Inmon Check:** Does every number trace to the canonical context doc?
- [ ] **Kimball Check:** Is every metric at a valid fact × dimension intersection?
- [ ] **Pearl Check:** Does every "what happened" have a "because" clause? Is at least one counterfactual included?
- [ ] **Howard Check:** Does the recommendation section present genuine alternatives with explicit tradeoffs?
- [ ] **Raiffa Check:** Are recommendations aligned to documented client preferences? Are outcomes projected with bounds?
- [ ] **Davenport Check:** Is every section tagged by analytics stage? Is Stage 2 the minimum? Is the Recommendations section at Stage 4?
- [ ] **Terminology Check:** Are Factor/Driver/Lever used correctly per definitions?
- [ ] **Autonomy Check:** Is each decision block tagged with its autonomy level?
- [ ] **Hard Gate Check:** Are all hard gates from the context doc respected?
- [ ] **Feedback Check:** Is there a "What we learned" section that updates the context doc?

---

## VERSION HISTORY

| Version | Date | Changes |
|---|---|---|
| 1.0 | 2026-04-14 | Initial framework mapping. Five pillars established. Execution chain defined. Operator checklist created. |

---

*Framework authored for AMZ Clever. Theoretical grounding: Simon & Newell (bounded rationality), Inmon & Kimball (data architecture), Pearl (probabilistic causality), Howard & Raiffa (decision analysis), Davenport (analytics maturity). All theory operationalized for Amazon PPC performance reporting context.*
