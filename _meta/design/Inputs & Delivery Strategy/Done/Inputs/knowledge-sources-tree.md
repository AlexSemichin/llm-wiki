
## Tree (parent → child)

```
KNOWLEDGE SOURCES
├── JUDGEMENTAL               
│   ├── SELF
│   │   ├── ROLE     → ROLE PLAYING
│   │   └── NO ROLE  → INTENTIONS
│   └── OTHERS       → EXPERT OPINIONS
└── STATISTICAL                
    ├── UNIVARIATE   → EXTRAPOLATION MODELS
    └── MULTIVARIATE
        ├── THEORY BASED → ECONOMIC MODELS
        └── DATA BASED   → MULTIVARIATE MODELS
```

## Methods (boxed leaf and lower-tier nodes)

| Box                       | Reached from                                                                          |
| ------------------------- | ------------------------------------------------------------------------------------- |
| ROLE PLAYING              | ROLE (under SELF)                                                                     |
| INTENTIONS                | NO ROLE (under SELF)                                                                  |
| EXPERT OPINIONS           | OTHERS                                                                                |
| EXTRAPOLATION MODELS      | UNIVARIATE                                                                            |
| MULTIVARIATE MODELS       | DATA BASED [cropped at right edge]                                                    |
| ECONOMIC MODELS           | THEORY BASED [cropped at right edge]                                                  |
| ANALOGIES                 | EXPERT OPINIONS; EXTRAPOLATION MODELS                                                 |
| CONJOINT ANALYSIS         | INTENTIONS                                                                            |
| JUDGEMENTAL BOOTSTRAPPING | EXPERT OPINIONS                                                                       |
| RULE BASED FORECASTING    | EXPERT OPINIONS; EXTRAPOLATION MODELS                                                 |
| EXPERT SYSTEMS            | EXPERT OPINIONS; CONJOINT ANALYSIS; JUDGEMENTAL BOOTSTRAPPING; RULE BASED FORECASTING |

## Cross-links drawn between method boxes
- INTENTIONS → CONJOINT ANALYSIS
- EXPERT OPINIONS → JUDGEMENTAL BOOTSTRAPPING
- EXPERT OPINIONS → RULE BASED FORECASTING (arrowhead at the box)
- EXPERT OPINIONS → EXPERT SYSTEMS (line runs down the right side of the bootstrapping box)
- EXPERT OPINIONS — ANALOGIES (line, no arrowhead)
- EXTRAPOLATION MODELS — ANALOGIES (line, no arrowhead)
- EXTRAPOLATION MODELS → RULE BASED FORECASTING
- CONJOINT ANALYSIS → EXPERT SYSTEMS
- JUDGEMENTAL BOOTSTRAPPING → EXPERT SYSTEMS
- RULE BASED FORECASTING → EXPERT SYSTEMS

