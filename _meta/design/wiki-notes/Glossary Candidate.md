- **Layer:**
    - `harness_layer` means L0–L4.
    - `wiki_layer` means raw/wiki/schema.
    - The waterfall “layers” become `harvest_stage` (discovery / validation / scale).
    - `optmyzr_layer` becomes `tool_surface` + `tool: optmyzr`. Putting the vendor name in the field name would break your E-D9 ruling (tool-neutral pages).
- **Tier:**
    - `sku_tier` (A/B/C).
    - `disclosure_level` (SHOW / SKELETON / GUARD). “Tier” would collide twice, and these are ordered exposure levels, not stacked layers.
    - `project_tier` (T1/T2).
- **Level and stage:** 
	- `causal_level`
	- `autonomy_level` 
	- `analytics_maturity`
	- `funnel_stage` 
	- `build_phase`.

| Clash                                                | Resolution                                                                                        |
| ---------------------------------------------------- | ------------------------------------------------------------------------------------------------- |
| Your genre SCHEMA vs Karpathy’s schema layer         | The genre becomes **DATASPEC**                                                                    |
| Your genre LOG vs Karpathy’s `log.md`                | The genre becomes **DEC** (a dated decision record). `log.md` stays, since Karpathy is canonical. |
| “Policy” as a codified rule vs Amazon’s policies     | The genre becomes **DECRULE**; Amazon’s rules become the entity `AmazonPolicy`                    |
| ARC-05’s campaign “dimensions” vs Kimball dimensions | `campaign_setting` vs `dimension`                                                                 |
| `atomic_fact` vs `atomic_waterfall`                  | Two separate terms                                                                                |
| `prov_tag` vs Obsidian `tags`                        | Two separate fields                                                                               |
| `evidence_scope` vs `project_scope`                  | Two separate fields                                                                               |
| Exemplar “gate check” vs a hard gate                 | `ops_check` (severity WARN/BLOCK) vs `hard_constraint`                                            |