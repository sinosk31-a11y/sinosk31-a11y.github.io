-- ============================================================
-- PROJECT 01: DIGITAL EUROPE
-- Economic Development & Technology Adoption
--
-- Dataset:
-- data/processed/project01_master_2023_2025.csv
--
-- SQL Engine:
-- DuckDB
--
-- Author:
-- Sinothile Mpofu
--
-- Purpose:
-- Answer the analytical questions defined for Project 01.
--
-- Important:
-- This analysis describes associations and changes.
-- It does NOT establish causal relationships.
-- ============================================================


-- ============================================================
-- 1. LOAD THE MASTER DATASET
-- ============================================================

CREATE OR REPLACE VIEW project01 AS
SELECT *
FROM read_csv_auto(
    '../data/processed/project01_master_2023_2025.csv',
    header = true
);


-- ============================================================
-- 2. DATA QUALITY CHECK
-- Confirm that the analytical dataset contains 27 EU countries.
-- ============================================================

SELECT
    COUNT(*) AS country_count
FROM project01;


-- ============================================================
-- 3. CHECK FOR MISSING ANALYTICAL VALUES
-- ============================================================

SELECT
    COUNT(*) FILTER (WHERE gdp_pps_2023 IS NULL) AS missing_gdp_2023,
    COUNT(*) FILTER (WHERE gdp_pps_2025 IS NULL) AS missing_gdp_2025,

    COUNT(*) FILTER (WHERE ai_2023 IS NULL) AS missing_ai_2023,
    COUNT(*) FILTER (WHERE ai_2025 IS NULL) AS missing_ai_2025,

    COUNT(*) FILTER (WHERE cloud_2023 IS NULL) AS missing_cloud_2023,
    COUNT(*) FILTER (WHERE cloud_2025 IS NULL) AS missing_cloud_2025,

    COUNT(*) FILTER (WHERE digital_skills_2023 IS NULL)
        AS missing_digital_skills_2023,

    COUNT(*) FILTER (WHERE digital_skills_2025 IS NULL)
        AS missing_digital_skills_2025,

    COUNT(*) FILTER (WHERE ict_specialists_2023 IS NULL)
        AS missing_ict_specialists_2023,

    COUNT(*) FILTER (WHERE ict_specialists_2025 IS NULL)
        AS missing_ict_specialists_2025

FROM project01;


-- ============================================================
-- 4. ECONOMIC LANDSCAPE
-- GDP PER CAPITA IN 2025
--
-- Question:
-- How does GDP per capita vary across EU countries?
-- ============================================================

SELECT
    country,
    gdp_pps_2025
FROM project01
ORDER BY gdp_pps_2025 DESC;


-- ============================================================
-- 5. GDP CHANGE
--
-- Question:
-- How did GDP per capita change between 2023 and 2025?
-- ============================================================

SELECT
    country,
    gdp_pps_2023,
    gdp_pps_2025,
    gdp_pps_change_pp AS gdp_pps_change
FROM project01
ORDER BY gdp_pps_change_pp DESC;


-- ============================================================
-- 6. AI ADOPTION IN 2025
--
-- Question:
-- How widely are enterprises adopting AI?
-- ============================================================

SELECT
    country,
    ai_2025
FROM project01
ORDER BY ai_2025 DESC;


-- ============================================================
-- 7. AI ADOPTION CHANGE
--
-- Question:
-- Which countries experienced the largest percentage-point
-- change in enterprise AI adoption between 2023 and 2025?
-- ============================================================

SELECT
    country,
    ai_2023,
    ai_2025,
    ai_change_pp
FROM project01
ORDER BY ai_change_pp DESC;


-- ============================================================
-- 8. CLOUD ADOPTION IN 2025
--
-- Question:
-- How widely are enterprises using paid cloud services?
-- ============================================================

SELECT
    country,
    cloud_2025
FROM project01
ORDER BY cloud_2025 DESC;


-- ============================================================
-- 9. CLOUD ADOPTION CHANGE
--
-- Question:
-- How did enterprise cloud adoption change between
-- 2023 and 2025?
-- ============================================================

SELECT
    country,
    cloud_2023,
    cloud_2025,
    cloud_change_pp
FROM project01
ORDER BY cloud_change_pp DESC;


-- ============================================================
-- 10. DIGITAL SKILLS IN 2025
--
-- Question:
-- What proportion of individuals had at least basic
-- digital skills?
-- ============================================================

SELECT
    country,
    digital_skills_2025
FROM project01
ORDER BY digital_skills_2025 DESC;


-- ============================================================
-- 11. DIGITAL SKILLS CHANGE
--
-- Question:
-- How did basic digital skills change between 2023 and 2025?
-- ============================================================

SELECT
    country,
    digital_skills_2023,
    digital_skills_2025,
    digital_skills_change_pp
FROM project01
ORDER BY digital_skills_change_pp DESC;


-- ============================================================
-- 12. ICT SPECIALISTS
--
-- Question:
-- How does the share of ICT specialists in employment
-- vary across countries?
-- ============================================================

SELECT
    country,
    ict_specialists_2025
FROM project01
ORDER BY ict_specialists_2025 DESC;


-- ============================================================
-- 13. ICT SPECIALIST CHANGE
--
-- Question:
-- How did the share of ICT specialists change between
-- 2023 and 2025?
-- ============================================================

SELECT
    country,
    ict_specialists_2023,
    ict_specialists_2025,
    ict_specialists_change_pp
FROM project01
ORDER BY ict_specialists_change_pp DESC;


-- ============================================================
-- 14. COMBINED TECHNOLOGY ADOPTION VIEW
--
-- This creates a consolidated view of the three
-- enterprise technology indicators.
-- ============================================================

SELECT
    country,
    ai_2025,
    cloud_2025,
    digital_skills_2025,
    ict_specialists_2025
FROM project01
ORDER BY country;


-- ============================================================
-- 15. GDP AND AI ASSOCIATION
--
-- Question:
-- Is GDP per capita associated with enterprise AI adoption?
--
-- CORR() measures statistical association.
-- It does NOT demonstrate causation.
-- ============================================================

SELECT
    CORR(gdp_pps_2025, ai_2025) AS gdp_ai_correlation
FROM project01;


-- ============================================================
-- 16. GDP AND CLOUD ASSOCIATION
--
-- Question:
-- Is GDP per capita associated with enterprise cloud adoption?
-- ============================================================

SELECT
    CORR(gdp_pps_2025, cloud_2025) AS gdp_cloud_correlation
FROM project01;


-- ============================================================
-- 17. GDP AND DIGITAL SKILLS ASSOCIATION
--
-- Question:
-- Is GDP per capita associated with digital skills?
-- ============================================================

SELECT
    CORR(gdp_pps_2025, digital_skills_2025)
        AS gdp_digital_skills_correlation
FROM project01;


-- ============================================================
-- 18. GDP AND ICT SPECIALISTS ASSOCIATION
--
-- Question:
-- Is GDP per capita associated with the share of ICT
-- specialists in employment?
-- ============================================================

SELECT
    CORR(gdp_pps_2025, ict_specialists_2025)
        AS gdp_ict_specialists_correlation
FROM project01;


-- ============================================================
-- 19. TECHNOLOGY ADOPTION CHANGE SUMMARY
--
-- Compare average percentage-point changes across the
-- technology indicators.
-- ============================================================

SELECT
    ROUND(AVG(ai_change_pp), 2) AS avg_ai_change_pp,
    ROUND(AVG(cloud_change_pp), 2) AS avg_cloud_change_pp,
    ROUND(AVG(digital_skills_change_pp), 2)
        AS avg_digital_skills_change_pp,
    ROUND(AVG(ict_specialists_change_pp), 2)
        AS avg_ict_specialists_change_pp
FROM project01;


-- ============================================================
-- 20. MASTER ANALYTICAL DATASET
--
-- Final query used as the main analytical extract.
-- ============================================================

SELECT
    country_code,
    country,

    gdp_pps_2023,
    gdp_pps_2025,
    gdp_pps_change_pp AS gdp_pps_change,

    ai_2023,
    ai_2025,
    ai_change_pp,

    cloud_2023,
    cloud_2025,
    cloud_change_pp,

    digital_skills_2023,
    digital_skills_2025,
    digital_skills_change_pp,

    ict_specialists_2023,
    ict_specialists_2025,
    ict_specialists_change_pp

FROM project01
ORDER BY country;
