sinosk31-a11y.github.io

Data Analytics Portfolio

A professional data analytics portfolio focused on data analysis, SQL, data cleaning, visualization, business intelligence, and evidence-based problem solving.

The projects in this repository demonstrate the complete analytical workflow:

Data → Cleaning → SQL Analysis → Statistical Analysis → Visualization → Findings → Business Interpretation

About This Portfolio

This portfolio demonstrates practical application of data analytics techniques to real-world and publicly available datasets.

The objective is not only to produce charts, but to demonstrate the ability to:

Define analytical and business questions

Identify and evaluate appropriate datasets

Clean and validate data

Work with structured datasets using SQL

Perform exploratory and statistical analysis

Calculate changes and relationships between variables

Create clear data visualizations

Interpret findings responsibly

Document limitations and data-quality considerations

Communicate technical findings to a non-technical audience

Produce reproducible analytical work

Core Skills

Data Analysis

Exploratory Data Analysis (EDA)

Data cleaning and validation

Descriptive statistics

Comparative analysis

Trend and change analysis

Correlation analysis

Data-quality assessment

Customer analytics

Operational analytics

Revenue analysis

SQL

DuckDB

Filtering and aggregation

GROUP BY analysis

CASE expressions

Common table expressions

Joins

Window functions

Statistical calculations

Analytical extracts

Visualization

Comparative charts

Horizontal bar charts

Scatterplots

Trend analysis

Correlation visualizations

Data storytelling

Tools & Technologies

SQL

DuckDB

Python

Pandas

Matplotlib

Git

GitHub

GitHub Pages

HTML

CSS

Project 01 — Digital Europe

Exploring the Relationship Between Economic Development and Technology Adoption

Live case study:
https://sinosk31-a11y.github.io/projects/project-01/

Business Question

How does technology adoption vary across European countries, and what relationships can be observed between digitalization and economic development?

Research Questions

The project investigates:

How does GDP per capita vary across European countries?

How does the prevalence of digital skills differ between countries?

How widely are enterprises adopting artificial intelligence?

How widely are enterprises adopting cloud computing?

How does the share of ICT specialists differ across countries?

What relationships can be observed between GDP per capita and technology-adoption indicators?

How have selected digital indicators changed between comparable years and 2025?

Analytical Workflow

Public Data Sources
        ↓
Data Validation
        ↓
Data Cleaning & Standardization
        ↓
Processed Analytical Dataset
        ↓
SQL Analysis with DuckDB
        ↓
Statistical Analysis
        ↓
Python Visualizations
        ↓
Findings & Interpretation
        ↓
Published Case Study

Key Analytical Areas

Economic development

Digital skills

Artificial intelligence adoption

Cloud computing adoption

ICT specialist employment

Cross-country comparison

Correlation analysis

Change over time

Tools Used

Python

Pandas

DuckDB

SQL

Matplotlib

GitHub

GitHub Pages

Project Outcome

Project 01 demonstrates an end-to-end approach to combining multiple public datasets, standardizing indicators, performing SQL and statistical analysis, creating visualizations, and communicating relationships between economic and digital-development indicators.

View Project 01:
https://sinosk31-a11y.github.io/projects/project-01/

Project 02 — Customer & Operational Analytics

Online Retail Customer, Revenue and Operational Analysis

Live case study:
https://sinosk31-a11y.github.io/projects/project-02/

Business Question

How do customer purchasing behavior, repeat purchasing, geography and cancellations relate to revenue performance in an online retail business?

Analytical Questions

The project investigates:

How does revenue change over time?

What proportion of customers make repeat purchases?

How is revenue distributed between one-time and repeat customers?

How concentrated is revenue among the highest-value customers?

How does revenue vary across countries?

Which products generate the most revenue?

What cancellation patterns can be observed over time?

What operational and customer-level patterns are visible in the transaction data?

Dataset

The project uses the Online Retail II dataset from the UCI Machine Learning Repository.

Official source:
https://archive.ics.uci.edu/dataset/502/online%2Bretail%2Bii

Citation:

Chen, D. (2019). Online Retail II. UCI Machine Learning Repository.

DOI:
https://doi.org/10.24432/C5CG6D

Dataset Description

The dataset contains transaction-level information from a UK-based online retail business.

The source covers:

December 2009 through December 2011

Two original workbook sheets:

Year 2009-2010

Year 2010-2011

Approximately 1.07 million transaction records

Invoice information

Product information

Quantity

Transaction date

Unit price

Customer ID

Country

Invoices beginning with C are identified by the source as cancellations.

Analytical Workflow

UCI Online Retail II Dataset
        ↓
Data Validation
        ↓
Data Cleaning
        ↓
Transaction Classification
        ↓
Revenue & Customer Calculations
        ↓
SQL / Python Analysis
        ↓
Customer & Operational Analysis
        ↓
Visualization
        ↓
Findings & Business Interpretation
        ↓
Published Case Study

Data Preparation

The analysis includes:

Combining the original dataset sheets

Inspecting missing values

Identifying cancellation transactions

Separating sales transactions from cancellations

Calculating transaction revenue

Standardizing dates and fields

Creating customer-level summaries

Creating country-level summaries

Creating product-level summaries

Creating monthly revenue and cancellation summaries

Key Areas of Analysis

Revenue Analysis

The project examines:

Monthly revenue

Monthly transaction volume

Units sold

Average order value

Revenue changes over time

Total sales revenue across the analyzed sales transactions is approximately:

£20.91 million

The highest observed monthly revenue occurred in:

November 2011 — approximately £1.50 million

The lowest observed monthly revenue occurred in:

February 2011 — approximately £522,546

December 2011 is treated cautiously because the source data ends on December 9, 2011, making that month incomplete.

Customer Analysis

The customer analysis examines purchasing frequency and revenue contribution.

The analysis identified approximately:

5,878 customers

1,623 one-time customers

4,255 repeat customers

Repeat customers represented approximately:

72.4% of customers

and generated approximately:

96.8% of analyzed revenue

One-time customers represented approximately:

27.6% of customers

and generated approximately:

3.2% of analyzed revenue

Revenue Concentration

The analysis also examines the distribution of revenue across customers.

Key observations include:

The top 10% of customers generated approximately 64% of revenue.

The top 100 customers generated approximately 37.6% of revenue.

A very small group of customers accounted for a substantial proportion of total revenue.

These results describe revenue concentration in the dataset; they do not establish causal relationships.

Customer Purchasing Behavior

The analysis compares:

Number of invoices

Revenue generated

Purchasing frequency

Customer contribution to total revenue

The relationship between invoice frequency and revenue was examined using correlation analysis.

The results showed:

Pearson correlation: approximately 0.629

Spearman correlation: approximately 0.859

These statistics indicate a positive association between purchasing frequency and revenue contribution in this dataset.

Correlation is descriptive and does not establish causation.

Geographic Analysis

Country-level analysis examines:

Number of customers

Number of transactions

Units sold

Revenue

Average order value

This provides a geographic view of where sales activity and revenue were generated within the dataset.

Product Analysis

Product-level analysis examines:

Product sales volume

Units sold

Revenue

Transaction activity

Product contribution to overall sales

This helps identify products with substantial transaction and revenue activity.

Cancellation Analysis

The project separately analyzes cancellation transactions to examine:

Monthly cancellation activity

Cancelled units

Cancellation revenue impact

Cancellation patterns over time

Operational implications of cancellations

Cancellation records are treated separately from completed sales when calculating sales revenue.

Tools Used

Python

Pandas

SQL

DuckDB

Matplotlib

Git

GitHub

GitHub Pages

Technical Skills Demonstrated

Data ingestion

Data cleaning

Data validation

Data transformation

Exploratory Data Analysis

SQL aggregation

Customer segmentation

Revenue analysis

Correlation analysis

Operational analysis

Data visualization

Business interpretation

Reproducible analytical workflows

Data Limitations

The analysis has several important limitations:

The dataset represents one online retail business.

It is historical data covering 2009–2011.

The final month of the source data is incomplete.

Customer IDs are missing for some transactions.

Transaction-level data does not explain customer motivations.

Correlation analysis does not establish causation.

Revenue concentration should not automatically be interpreted as customer loyalty or future customer value.

These limitations are considered when interpreting the findings.

Reproducibility

The original online_retail_II.xlsx workbook is approximately 43 MB and is not committed to this GitHub repository.

To reproduce the analysis:

Download the dataset from the official UCI Machine Learning Repository.

Place the workbook locally in the project's raw-data directory.

Run the documented data-cleaning and analysis workflow.

Generate the processed analytical datasets.

Recreate the visualizations and findings.

The processed analytical outputs used for the published case study are maintained separately from the original raw workbook.

Project Outcome

Project 02 demonstrates an end-to-end customer and operational analytics workflow using transaction-level retail data.

The project moves from raw transaction records through:

Data Validation → Cleaning → Transformation → Customer Analysis → Revenue Analysis → Operational Analysis → Visualization → Business Interpretation

The case study demonstrates the ability to use analytical methods to investigate customer behavior, revenue concentration, geographic performance, product activity, and cancellation patterns while documenting data limitations and avoiding unsupported causal conclusions.

View Project 02:
https://sinosk31-a11y.github.io/projects/project-02/

Portfolio Project Structure

Project

Focus

Primary Skills

Project 01

Digital Europe

SQL, Python, EDA, statistical analysis, visualization

Project 02

Customer & Operational Analytics

SQL, Python, customer analytics, revenue analysis, operational analysis

Reproducibility & Documentation

Each project is designed to document the analytical process rather than only present final charts.

The portfolio emphasizes:

Source attribution

Data validation

Transparent cleaning decisions

Reproducible calculations

Appropriate statistical interpretation

Documentation of limitations

Clear separation between findings and assumptions

Author

Sinothile Mpofu

Data Analytics Portfolio

GitHub:
https://github.com/sinosk31-a11y

LinkedIn:
https://www.linkedin.com/in/sinothile-mpofu-74a01821

Portfolio:
https://sinosk31-a11y.github.io/

Dataset Attribution

Project 02 uses:

Chen, D. (2019). Online Retail II. UCI Machine Learning Repository.

https://archive.ics.uci.edu/dataset/502/online%2Bretail%2Bii

DOI: https://doi.org/10.24432/C5CG6D
