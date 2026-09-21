# Project 01 — Data Preparation Notes

## Project
Digital Europe — Exploring the Relationship Between Economic Development and Technology Adoption

## Raw source files
The `data/raw/` folder contains the five original Eurostat TSV downloads. They are preserved without analytical edits.

## Analytical population
EU-27 member states only. Aggregate areas such as EU27_2020, EA, and non-EU countries are excluded from the master analytical dataset.

## Years
2023 and 2025 are used because all five selected indicators have observations for the EU-27 countries for both years in the downloaded source files.

## Selected indicators

| Variable | Eurostat dataset | Selection |
|---|---|---|
| GDP per capita | `nama_10_pc` | `na_item=B1GQ`, `unit=CP_PPS_EU27_2020_HAB` |
| AI adoption | `isoc_eb_ai` | `size_emp=GE10`, `nace_r2=C10-S951_X_K`, `indic_is=E_AI_TANY`, `unit=PC_ENT` |
| Cloud adoption | `isoc_cicce_use` | `size_emp=GE10`, `nace_r2=C10-S951_X_K`, `indic_is=E_CC`, `unit=PC_ENT` |
| Digital skills | `isoc_sk_dskl_i21` | `ind_type=IND_TOTAL`, `indic_is=I_DSK2_BAB`, `unit=PC_IND` |
| ICT specialists | `isoc_sks_itspt` | `unit=PC_EMP` |

## Interpretation

- GDP per capita is measured in purchasing power standard (PPS) per inhabitant using the EU27_2020 reference.
- AI and cloud values are percentages of enterprises within the Eurostat enterprise survey scope.
- Digital skills are the percentage of individuals with at least basic digital skills.
- ICT specialists are measured as a percentage of total employment.
- Change variables are percentage-point changes: 2025 minus 2023.
- A percentage-point change must not be described as percentage growth.

## Status flags

Eurostat observations can include status flags such as `p`, `e`, and `b`. The cleaned files preserve the flag separately rather than silently removing it.

## Missing values

Eurostat's `:` values are converted to blank/NA in the analytical files. No missing values are imputed.

## Methodological limitation

This is observational cross-country data. Relationships or associations identified in the analysis should not be described as causal effects.

## Attribution

Source: Eurostat, European Commission. Dataset definitions, metadata, and source data remain the property of the original publisher. The filtering, cleaning, calculations, visualizations, analysis, and written interpretation in this portfolio are original work by Sinothile Mpofu.
