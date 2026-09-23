# Project 01 — Analytical Findings

## Digital Europe — Economic Development and Technology Adoption

**Author:** Sinothile Mpofu

**Analysis period:** 2023–2025

**Geographic scope:** European Union (27 countries)

**Primary data publisher:** Eurostat / European Commission

---

# 1. Executive Summary

This project examines the relationship between economic development and selected indicators of digitalisation across the 27 European Union member states.

The analysis combines five Eurostat datasets covering:

- GDP per capita measured in purchasing power standards (PPS)
- Enterprise artificial intelligence adoption
- Enterprise cloud computing adoption
- Digital skills among individuals
- ICT specialists as a share of total employment

The analysis compares selected indicators between 2023 and 2025 and examines statistical associations between GDP per capita and technology-related indicators.

The results show substantial differences between EU countries in both economic development and technology adoption.

Across the 27-country dataset, the strongest observed statistical association was between GDP per capita and the share of ICT specialists in employment, with a Pearson correlation coefficient of approximately 0.580.

GDP per capita also showed positive associations with digital skills (approximately 0.522), AI adoption (approximately 0.505), and cloud adoption (approximately 0.404).

These results indicate that countries with higher GDP per capita tended, within this dataset, to also report higher levels of several digitalisation indicators.

However, correlation does not establish causation. The analysis therefore does not conclude that higher GDP causes greater technology adoption, or that technology adoption causes higher GDP.

---

# 2. Dataset Scope

The analytical dataset contains:

**27 EU countries**

The project uses five Eurostat indicators.

| Indicator | Dataset code | Analytical purpose |
|---|---|---|
| GDP per capita | `nama_10_pc` | Economic development |
| AI adoption | `isoc_eb_ai` | Enterprise technology adoption |
| Cloud adoption | `isoc_cicce_use` | Enterprise technology adoption |
| Digital skills | `isoc_sk_dskl` | Digital capability among individuals |
| ICT specialists | `isoc_sks_itsp` | Digital workforce capacity |

The analysis uses comparable observations for 2023 and 2025 where available in the prepared analytical dataset.

---

# 3. Data Quality

The prepared analytical dataset contains observations for all 27 EU countries.

The validation process checked the selected analytical fields for missing values.

The final analytical dataset contained:

- 27 countries
- No missing values in the selected analytical fields used for the correlation analysis

The raw Eurostat tabular files were retained separately in the repository so that the transformation from source data to analytical data remains traceable.

---

# 4. Economic Development

GDP per capita was measured using purchasing power standards (PPS).

PPS is used because price-level differences between countries can make direct monetary comparisons misleading.

Within the 2025 dataset:

- Luxembourg recorded the highest observed GDP per capita at approximately **99,621 PPS per inhabitant**.
- Bulgaria recorded the lowest observed GDP per capita at approximately **28,332 PPS per inhabitant**.

The difference illustrates the substantial variation in economic output per inhabitant across EU countries.

GDP per capita is used in this project as an economic-development indicator.

It should not be interpreted as a direct measure of individual household income or personal wealth.

---

# 5. Artificial Intelligence Adoption

Enterprise AI adoption varied substantially across the EU countries in the 2025 dataset.

The highest observed value was:

**Denmark — approximately 42.03%**

The lowest observed value was:

**Romania — approximately 5.21%**

Across the analytical dataset, the average change in AI adoption between 2023 and 2025 was approximately:

**+12.49 percentage points**

This indicates substantial growth in reported enterprise AI adoption over the analysis period.

The result should be interpreted as a change in the reported share of enterprises using AI rather than as evidence that AI adoption caused improvements in economic performance.

---

# 6. Cloud Computing Adoption

Enterprise cloud adoption also varied substantially between countries.

In 2025:

- Finland recorded the highest observed value at approximately **79.21%**.
- Bulgaria recorded the lowest observed value at approximately **17.83%**.

The average change between 2023 and 2025 was approximately:

**+5.72 percentage points**

The data therefore show an overall increase in reported enterprise cloud adoption across the countries included in the analytical dataset.

---

# 7. Digital Skills

Digital skills represent an important people-focused dimension of digitalisation.

The 2025 dataset shows:

- Netherlands — approximately **83.61%**
- Romania — approximately **31.84%**

These values demonstrate substantial cross-country variation in the reported level of digital skills.

The average change between 2023 and 2025 was approximately:

**+3.40 percentage points**

This suggests that digital capability changed during the period, although the size and direction of change differed between countries.

---

# 8. ICT Specialists

ICT specialists represent the workforce dimension of the analysis.

In 2025:

- Sweden recorded the highest observed share at approximately **8.9% of total employment**.
- Greece recorded the lowest observed share at approximately **2.5%**.

The average change between 2023 and 2025 was approximately:

**+0.26 percentage points**

The relatively smaller average change compared with the enterprise technology indicators suggests that workforce composition changes more gradually than some measures of enterprise technology adoption.

This interpretation is descriptive and should not be treated as a causal explanation.

---

# 9. Correlation Analysis

Pearson correlation was used to examine the association between GDP per capita and selected digitalisation indicators.

The results were:

| Relationship | Pearson correlation |
|---|---:|
| GDP per capita ↔ AI adoption | 0.505 |
| GDP per capita ↔ Cloud adoption | 0.404 |
| GDP per capita ↔ Digital skills | 0.522 |
| GDP per capita ↔ ICT specialists | 0.580 |

All four correlations are positive in this dataset.

The strongest observed association was between:

**GDP per capita and ICT specialists — approximately 0.580**

The weakest of the four observed associations was between:

**GDP per capita and cloud adoption — approximately 0.404**

---

# 10. Interpretation of the Correlations

The positive correlations indicate that, within the 27-country 2025 dataset, countries with higher GDP per capita generally tended to report higher values for the selected digitalisation indicators.

For example, the GDP–ICT-specialist correlation of approximately 0.580 indicates a moderate positive linear association in the observed data.

The GDP–digital-skills correlation of approximately 0.522 similarly indicates a positive association.

The GDP–AI correlation of approximately 0.505 indicates a positive association between economic development and reported enterprise AI adoption.

The GDP–cloud correlation of approximately 0.404 is also positive, although weaker than the other three relationships examined.

These coefficients describe the observed cross-sectional relationships.

They do not identify the mechanisms behind those relationships.

---

# 11. What the Analysis Does Not Establish

The analysis does **not** establish that:

- higher GDP causes higher AI adoption;
- higher GDP causes higher cloud adoption;
- higher digital skills cause higher GDP;
- ICT specialists cause higher GDP;
- technology adoption causes economic growth.

Several other factors could influence both economic development and digitalisation.

Potential factors include:

- education systems;
- labour-market structure;
- industry composition;
- business size;
- infrastructure;
- public-sector digitalisation;
- investment;
- research and development;
- national policies;
- demographic structure;
- access to digital technologies.

These variables are outside the scope of the current analysis.

---

# 12. Business Interpretation

From a business analytics perspective, the analysis highlights that digital transformation should not be evaluated using a single indicator.

The project identifies four complementary dimensions:

### Economic environment

GDP per capita provides an economic-development context.

### Enterprise technology adoption

AI and cloud indicators show the extent to which businesses are adopting selected technologies.

### Human digital capability

Digital-skills data provide an indication of the population's ability to use digital technologies.

### Digital workforce

ICT-specialist data provide an indication of the availability of specialised digital talent.

Considering these dimensions together provides a broader view of digitalisation than focusing on a single technology metric.

---

# 13. Key Analytical Findings

### Finding 1 — Digitalisation varies considerably across EU countries

The indicators show substantial differences between countries in economic development, technology adoption, digital skills and ICT employment.

### Finding 2 — Enterprise AI adoption increased

The average change in reported AI adoption between 2023 and 2025 was approximately **+12.49 percentage points**.

### Finding 3 — Cloud adoption also increased

The average change in reported cloud adoption between 2023 and 2025 was approximately **+5.72 percentage points**.

### Finding 4 — Digital skills changed more gradually

The average change in the selected digital-skills indicator was approximately **+3.40 percentage points**.

### Finding 5 — ICT employment changed more gradually

The average change in the ICT-specialist indicator was approximately **+0.26 percentage points**.

### Finding 6 — Economic development is positively associated with the selected digital indicators

GDP per capita showed positive correlations with:

- AI adoption
- cloud adoption
- digital skills
- ICT specialists

The strongest observed association was GDP per capita with ICT specialists.

---

# 14. Limitations

## Cross-sectional correlation

The correlation analysis uses country-level observations and therefore cannot establish causation.

## Country-level aggregation

Country-level data can hide substantial variation between individuals, businesses, regions and industries.

## Indicator definitions

Each Eurostat indicator measures a specific concept and should not be treated as a complete measure of digitalisation.

## Time comparability

Changes between years should be interpreted with awareness of possible methodological changes, revisions and breaks in series within official statistics.

## GDP interpretation

GDP per capita is an economic-output indicator and should not be interpreted as an individual's income or standard of living.

## Technology adoption

AI and cloud adoption measures describe enterprise use of specified technologies. They do not measure the quality, sophistication or business value of those technologies.

## Correlation

Correlation measures statistical association, not causation.

---

# 15. Reproducibility

The project maintains the original source data separately from processed analytical data.

Repository structure:

```text
data/
├── raw/
│   ├── isoc_cicce_use_tabular.tsv
│   ├── isoc_eb_ai_tabular.tsv
│   ├── isoc_sk_dskl_i21_tabular.tsv
│   ├── isoc_sks_itspt_tabular.tsv
│   └── nama_10_pc_tabular.tsv
│
└── processed/
    ├── DATA_DICTIONARY.md
    ├── ai_adoption_2023_2025.csv
    ├── cloud_adoption_2023_2025.csv
    ├── digital_skills_2023_2025.csv
    ├── gdp_pps_2023_2025.csv
    ├── ict_specialists_2023_2025.csv
    ├── project01_master_2023_2025.csv
    └── validation_summary.csv
