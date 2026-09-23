# Digital Europe — Economic Development and Technology Adoption

## Project 01 | Data Analytics Portfolio

**Author:** Sinothile Mpofu  
**Analysis period:** 2023–2025  
**Geographic scope:** European Union (27 countries)  
**Primary data source:** Eurostat / European Commission

---

## 1. Project Overview

Digital transformation is developing at different rates across European countries.

This project investigates the relationship between economic development and selected indicators of digitalisation across the 27 European Union member states.

The analysis combines economic, business, workforce and individual-level digital indicators to examine how technology adoption and digital capability vary between countries.

The project uses official Eurostat datasets and applies data preparation, validation, SQL analysis, statistical correlation and data visualisation techniques.

---

# 2. Business Question

> How does technology adoption vary across European countries, and what relationships can be observed between digitalisation and economic development?

The project investigates whether countries with higher levels of economic development also tend to report higher levels of selected digitalisation indicators.

The analysis focuses on **association rather than causation**.

---

# 3. Analytical Questions

The project addresses the following questions:

1. How does GDP per capita vary across EU countries?

2. How does enterprise AI adoption vary between countries?

3. How widely are enterprises using cloud computing services?

4. How does digital-skills prevalence vary between countries?

5. How does the share of ICT specialists differ across countries?

6. How did the selected indicators change between 2023 and 2025?

7. What statistical relationships can be observed between GDP per capita and the selected digitalisation indicators?

---

# 4. Dataset

Five Eurostat datasets were combined for the analysis.

| Indicator | Eurostat dataset | Purpose |
|---|---|---|
| GDP per capita | `nama_10_pc` | Economic development |
| AI adoption | `isoc_eb_ai` | Enterprise AI adoption |
| Cloud adoption | `isoc_cicce_use` | Enterprise cloud adoption |
| Digital skills | `isoc_sk_dskl` | Individual digital capability |
| ICT specialists | `isoc_sks_itsp` | Digital workforce |

The final analytical dataset contains observations for:

**27 EU countries**

---

# 5. Data Pipeline

The project follows a reproducible data workflow:

```text
Official Eurostat datasets
          ↓
Raw TSV files
          ↓
Data validation
          ↓
Data cleaning and transformation
          ↓
Processed CSV datasets
          ↓
Master analytical dataset
          ↓
SQL analysis
          ↓
Statistical analysis
          ↓
Visualisations
          ↓
Business interpretation
