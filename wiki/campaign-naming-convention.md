---
id: PPC-DATASPEC-001
title: "Campaign naming convention"
aliases: [PPC-DATASPEC-001, ARC-04]
genre: DATASPEC
entity_types: [Campaign, IntentSegment, FunnelStage]
domain: PPC
page_status: seed
prov_tag: U
evidence_scope: global
sources: [SRC-0003]
recorded: 2026-10-18
disclosure_level: SKELETON
classification: internal
producer: llm
page_version: 0.2.0
schema_version: 0.2.2
review_cadence: P3M
tool_surface: [Optmyzr:rule-engine]
relationships:
  feeds: ["[[ENG-01]]", "[[FMT-03]]"]
  implemented_by: ["[[optmyzr|Tool]]"]
---

# Campaign naming convention

## Structure

`[Ad Program]-[Intent Segment]-[Funnel Stage]-[Targeting Method]-[Match Type]-[Product Group]-[Variant]` + ASIN suffix. `prov: U | scope: global | src: SRC-0003`

| Slot             | Values                                                    |
| ---------------- | --------------------------------------------------------- |
| Ad Program       | SP · SB · SBV · SD · SDV                                  |
| Intent Segment   | BRAN · DEF · GENE · RANK · COMP · ATT · CROS · CAT · EVNT |
| Funnel Stage     | tofu · mofu · bofu · retention                            |
| Targeting Method | keyword · ASIN · category · audience · auto               |
| Match Type       | exact · phrase · broad · auto group                       |
| Product Group    | 3–5 chars, parent variant / functional category           |
| Variant          | material, design, collection, audience                    |

## Field rules
- The naming code is the only mechanism that encodes campaign intent into Amazon's flat campaign structure. `prov: U | scope: global | src: SRC-0003`
- Rainbow reporting, DTPRF classification and Optmyzr recipe targeting depend on it. `prov: U | scope: global | src: SRC-0003`

## Example
`WBSKT-BMBO-ASIN` (from source).

## Open questions
- The example has 3 tokens; the structure has 7 slots plus suffix. Which slots are optional?
- "flat-encodes L4 intent": what is L4 here?

## See also
- [[sku-tier-structure-check|PPC-DIAG-001]]
