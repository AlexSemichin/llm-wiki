There are now 12 genres: 
* REF
* PROC
* **TECH**
* DATASPEC- my genre SCHEMA
* MAP
* META
* TEMPL
* DIAG
* CASE
* GLOSS
* DEC - dated decision record
* DECRULE - “Policy” as a codified rule

- **TECH vs PROC:** TECH is one reusable method. PROC is an ordered sequence of ≥2 steps that calls a TECH through `uses_technique`.

|Pick|Genre it tests|Why this one|
|---|---|---|
|ARC-01 philosophies matrix|REF|A comparative matrix with many entities|
|ARC-03 atomic waterfall|PROC|It has numeric thresholds, which tests the scope, date and tag fields|
|ARC-04 naming convention|SCHEMA|Tests where SCHEMA ends and META begins|
|ARC-06 portfolio decision matrix|POLICY|A catalog-size → pattern rule, which tests the decision-policy genre|
|ARC-08 SKU-tier gate|DIAG / hard gate|Has WARN vs BLOCK severity, which tests the autonomy and hard-gate fields|