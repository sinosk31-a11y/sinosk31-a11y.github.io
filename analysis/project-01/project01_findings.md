# Project 01 — SQL Analysis Results

## Execution note

The SQL analysis was validated against the cleaned 27-country master dataset. The result tables in this directory correspond to the analytical queries in `sql/project01_analysis.sql`.

## Data quality

- Analytical population: **27 EU countries**.
- Missing analytical values for the selected 2023 and 2025 indicators: **0**.

## 2025 country comparisons

| Indicator | Highest country | Value | Lowest country | Value |
|---|---|---:|---|---:|
| GDP per capita (PPS) | Luxembourg | 99621.3 | Bulgaria | 28332.0 |
| AI adoption (%) | Denmark | 42.03 | Romania | 5.21 |
| Cloud adoption (%) | Finland | 79.21 | Bulgaria | 17.83 |
| Digital skills (%) | Netherlands | 83.61 | Romania | 31.84 |
| ICT specialists (%) | Sweden | 8.9 | Greece | 2.5 |

## Average change, 2023–2025

- AI adoption: **12.49 percentage points**
- Cloud adoption: **5.72 percentage points**
- Digital skills: **3.40 percentage points**
- ICT specialists: **0.26 percentage points**

GDP per capita is measured in PPS per inhabitant, so its 2023–2025 difference is expressed in **PPS per inhabitant**, not percentage points.

## Pearson correlations in 2025

| Relationship | Pearson r | N |
|---|---:|---:|
| GDP vs AI adoption | 0.505 | 27 |
| GDP vs cloud adoption | 0.404 | 27 |
| GDP vs digital skills | 0.522 | 27 |
| GDP vs ICT specialists | 0.580 | 27 |

These are cross-sectional Pearson correlations for the 27-country 2025 dataset. They describe statistical association and do not establish causal effects.

## Next analytical stage

The next stage should visualize country-level comparisons, 2023–2025 changes, and GDP-versus-technology scatterplots. Interpretations should distinguish descriptive patterns from causal claims.
