# Project 02 — Customer & Operational Analytics

## Online Retail Customer, Revenue and Operational Analysis

This project is an end-to-end data analytics case study using the **Online Retail II** dataset from the UCI Machine Learning Repository.

The analysis examines customer purchasing behavior, repeat purchasing, revenue concentration, geography, product performance and cancellation patterns in an online retail business.

The objective is to demonstrate a complete analytical workflow:

**Business Question → Data Preparation → Validation → Analysis → Insights → Business Interpretation**

---

## Business Question

**How do customer purchasing behavior, repeat purchasing, geography and cancellations relate to revenue performance in an online retail business?**

---

## Analytical Questions

The project investigates the following questions:

1. How does revenue change over time?
2. How concentrated is revenue among customers?
3. How does repeat purchasing relate to revenue?
4. Which countries contribute the most revenue?
5. Which products generate the most revenue?
6. What patterns exist in cancelled transactions?
7. What operational and customer-level insights can be derived from the transaction data?

---

# Dataset

## Source

The project uses the **Online Retail II** dataset provided by the UCI Machine Learning Repository.

Official dataset:

https://archive.ics.uci.edu/dataset/502/online%2Bretail%2Bii

DOI:

https://doi.org/10.24432/C5CG6D

### Citation

Chen, D. (2019). *Online Retail II*. UCI Machine Learning Repository.

---

## Dataset Description

The Online Retail II dataset contains transaction-level information from a UK-based registered non-store online retailer.

The dataset covers transactions from:

- December 2009
- through December 2011

The original workbook contains two sheets:

- `Year 2009-2010`
- `Year 2010-2011`

Together, the dataset contains approximately **1.07 million transaction records** across 8 fields:

- Invoice
- StockCode
- Description
- Quantity
- InvoiceDate
- Price
- Customer ID
- Country

The UCI documentation identifies invoices beginning with **C** as cancellations.

---

# Data Handling

The original workbook was approximately **43 MB** and is therefore not committed to this GitHub repository.

The raw dataset should be downloaded directly from the official UCI source and placed locally at:

```text
data/raw/online_retail_II.xlsx
