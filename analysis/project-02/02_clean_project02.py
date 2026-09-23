import pandas as pd
from pathlib import Path


# ============================================================
# PROJECT 02
# CUSTOMER & OPERATIONAL ANALYTICS
# DATA CLEANING PIPELINE
# ============================================================


# ------------------------------------------------------------
# 1. PROJECT PATHS
# ------------------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parents[2]

RAW_FILE = (
    PROJECT_ROOT
    / "data"
    / "raw"
    / "online_retail_II.xlsx"
)

PROCESSED_DIR = (
    PROJECT_ROOT
    / "data"
    / "processed"
)

ANALYSIS_DIR = (
    PROJECT_ROOT
    / "analysis"
    / "project-02"
)

PROCESSED_DIR.mkdir(
    parents=True,
    exist_ok=True
)

ANALYSIS_DIR.mkdir(
    parents=True,
    exist_ok=True
)


# ------------------------------------------------------------
# 2. CHECK SOURCE FILE
# ------------------------------------------------------------

if not RAW_FILE.exists():

    raise FileNotFoundError(
        f"""
Raw dataset not found.

Expected location:
{RAW_FILE}

Download the official UCI Online Retail II dataset and
place online_retail_II.xlsx in data/raw/.
"""
    )


print("=" * 70)
print("PROJECT 02 — CUSTOMER & OPERATIONAL ANALYTICS")
print("DATA CLEANING PIPELINE")
print("=" * 70)

print()
print("Source file:")
print(RAW_FILE)
print()


# ------------------------------------------------------------
# 3. LOAD BOTH WORKSHEETS
# ------------------------------------------------------------

print("Loading Year 2009-2010...")

year_1 = pd.read_excel(
    RAW_FILE,
    sheet_name="Year 2009-2010"
)

print(
    f"Year 2009-2010 loaded: "
    f"{len(year_1):,} rows"
)


print()
print("Loading Year 2010-2011...")

year_2 = pd.read_excel(
    RAW_FILE,
    sheet_name="Year 2010-2011"
)

print(
    f"Year 2010-2011 loaded: "
    f"{len(year_2):,} rows"
)


# ------------------------------------------------------------
# 4. ADD SOURCE SHEET
# ------------------------------------------------------------

year_1["source_sheet"] = (
    "Year 2009-2010"
)

year_2["source_sheet"] = (
    "Year 2010-2011"
)


# ------------------------------------------------------------
# 5. COMBINE DATA
# ------------------------------------------------------------

df = pd.concat(
    [
        year_1,
        year_2
    ],
    ignore_index=True
)

print()
print(
    f"Combined rows: "
    f"{len(df):,}"
)


# ------------------------------------------------------------
# 6. STANDARDIZE COLUMN NAMES
# ------------------------------------------------------------

df = df.rename(
    columns={
        "Invoice": "invoice",
        "StockCode": "stock_code",
        "Description": "description",
        "Quantity": "quantity",
        "InvoiceDate": "invoice_date",
        "Price": "unit_price",
        "Customer ID": "customer_id",
        "Country": "country"
    }
)


# ------------------------------------------------------------
# 7. STANDARDIZE TEXT FIELDS
# ------------------------------------------------------------

text_columns = [
    "invoice",
    "stock_code",
    "description",
    "country",
    "source_sheet"
]

for column in text_columns:

    df[column] = (
        df[column]
        .astype("string")
        .str.strip()
    )


# ------------------------------------------------------------
# 8. STANDARDIZE NUMERIC FIELDS
# ------------------------------------------------------------

df["quantity"] = pd.to_numeric(
    df["quantity"],
    errors="coerce"
)

df["unit_price"] = pd.to_numeric(
    df["unit_price"],
    errors="coerce"
)

df["customer_id"] = pd.to_numeric(
    df["customer_id"],
    errors="coerce"
)


# ------------------------------------------------------------
# 9. STANDARDIZE DATE
# ------------------------------------------------------------

df["invoice_date"] = pd.to_datetime(
    df["invoice_date"],
    errors="coerce"
)


# ------------------------------------------------------------
# 10. DATA-QUALITY FLAGS
# ------------------------------------------------------------

df["is_cancellation"] = (
    df["invoice"]
    .fillna("")
    .str.startswith("C")
)

df["is_negative_quantity"] = (
    df["quantity"] < 0
)

df["is_zero_quantity"] = (
    df["quantity"] == 0
)

df["is_zero_price"] = (
    df["unit_price"] == 0
)

df["is_negative_price"] = (
    df["unit_price"] < 0
)

df["has_customer_id"] = (
    df["customer_id"].notna()
)


# ------------------------------------------------------------
# 11. CALCULATE LINE REVENUE
# ------------------------------------------------------------

df["revenue"] = (
    df["quantity"]
    * df["unit_price"]
)


# ------------------------------------------------------------
# 12. TRANSACTION CLASSIFICATION
# ------------------------------------------------------------

def classify_transaction(row):

    if row["is_cancellation"]:
        return "CANCELLATION"

    if row["is_negative_quantity"]:
        return "RETURN_OR_NEGATIVE_QUANTITY"

    if row["is_negative_price"]:
        return "NEGATIVE_PRICE"

    if row["is_zero_price"]:
        return "ZERO_PRICE"

    if (
        row["quantity"] > 0
        and row["unit_price"] > 0
    ):
        return "SALE"

    return "OTHER"


df["transaction_type"] = (
    df.apply(
        classify_transaction,
        axis=1
    )
)


# ------------------------------------------------------------
# 13. DUPLICATE ANALYSIS
# ------------------------------------------------------------

duplicate_count = int(
    df.duplicated().sum()
)

print()
print(
    f"Exact duplicate rows identified: "
    f"{duplicate_count:,}"
)


# ------------------------------------------------------------
# 14. REMOVE EXACT DUPLICATES
# ------------------------------------------------------------

df = (
    df
    .drop_duplicates()
    .copy()
)

print(
    f"Rows after duplicate removal: "
    f"{len(df):,}"
)


# ------------------------------------------------------------
# 15. CREATE SALES DATASET
# ------------------------------------------------------------

sales = df[
    df["transaction_type"] == "SALE"
].copy()


# ------------------------------------------------------------
# 16. CREATE CANCELLATION DATASET
# ------------------------------------------------------------

cancellations = df[
    df["transaction_type"] == "CANCELLATION"
].copy()


# ------------------------------------------------------------
# 17. CREATE CUSTOMER ANALYTICS DATASET
# ------------------------------------------------------------

customer_transactions = sales[
    sales["customer_id"].notna()
].copy()


# ------------------------------------------------------------
# 18. CREATE TIME DIMENSIONS
# ------------------------------------------------------------

datasets = [
    df,
    sales,
    cancellations,
    customer_transactions
]

for dataset in datasets:

    dataset["year"] = (
        dataset["invoice_date"]
        .dt.year
    )

    dataset["month"] = (
        dataset["invoice_date"]
        .dt.month
    )

    dataset["year_month"] = (
        dataset["invoice_date"]
        .dt.to_period("M")
        .astype(str)
    )


# ------------------------------------------------------------
# 19. SAVE CLEANED TRANSACTION DATA
# ------------------------------------------------------------

combined_path = (
    PROCESSED_DIR
    / "project02_transactions_cleaned.csv"
)

sales_path = (
    PROCESSED_DIR
    / "project02_sales.csv"
)

cancellation_path = (
    PROCESSED_DIR
    / "project02_cancellations.csv"
)

customer_path = (
    PROCESSED_DIR
    / "project02_customer_transactions.csv"
)


print()
print("Saving processed datasets...")


df.to_csv(
    combined_path,
    index=False
)

sales.to_csv(
    sales_path,
    index=False
)

cancellations.to_csv(
    cancellation_path,
    index=False
)

customer_transactions.to_csv(
    customer_path,
    index=False
)


# ------------------------------------------------------------
# 20. CLEANING SUMMARY
# ------------------------------------------------------------

summary = pd.DataFrame(
    [
        {
            "metric": "Original rows",
            "value": (
                len(year_1)
                + len(year_2)
            )
        },
        {
            "metric": "Exact duplicate rows removed",
            "value": duplicate_count
        },
        {
            "metric": "Cleaned transaction rows",
            "value": len(df)
        },
        {
            "metric": "Sales rows",
            "value": len(sales)
        },
        {
            "metric": "Cancellation rows",
            "value": len(cancellations)
        },
        {
            "metric": "Customer-analysis rows",
            "value": len(customer_transactions)
        },
        {
            "metric": "Customers with ID",
            "value": (
                customer_transactions[
                    "customer_id"
                ].nunique()
            )
        },
        {
            "metric": "Unique products",
            "value": (
                sales[
                    "stock_code"
                ].nunique()
            )
        },
        {
            "metric": "Countries",
            "value": (
                sales[
                    "country"
                ].nunique()
            )
        }
    ]
)


summary_path = (
    ANALYSIS_DIR
    / "02_cleaning_summary.csv"
)

summary.to_csv(
    summary_path,
    index=False
)


# ------------------------------------------------------------
# 21. TRANSACTION TYPE SUMMARY
# ------------------------------------------------------------

transaction_summary = (
    df[
        "transaction_type"
    ]
    .value_counts()
    .rename_axis("transaction_type")
    .reset_index(
        name="row_count"
    )
)

transaction_summary["percentage"] = (
    transaction_summary["row_count"]
    / len(df)
    * 100
)


transaction_summary_path = (
    ANALYSIS_DIR
    / "02_transaction_type_summary.csv"
)

transaction_summary.to_csv(
    transaction_summary_path,
    index=False
)


# ------------------------------------------------------------
# 22. DATA QUALITY SUMMARY
# ------------------------------------------------------------

quality_summary = pd.DataFrame(
    [
        {
            "metric": "Missing customer_id",
            "count": int(
                df["customer_id"].isna().sum()
            )
        },
        {
            "metric": "Missing description",
            "count": int(
                df["description"].isna().sum()
            )
        },
        {
            "metric": "Negative quantity",
            "count": int(
                (df["quantity"] < 0).sum()
            )
        },
        {
            "metric": "Zero quantity",
            "count": int(
                (df["quantity"] == 0).sum()
            )
        },
        {
            "metric": "Negative price",
            "count": int(
                (df["unit_price"] < 0).sum()
            )
        },
        {
            "metric": "Zero price",
            "count": int(
                (df["unit_price"] == 0).sum()
            )
        },
        {
            "metric": "Cancellation invoices",
            "count": int(
                df["is_cancellation"].sum()
            )
        }
    ]
)


quality_path = (
    ANALYSIS_DIR
    / "02_cleaned_data_quality.csv"
)

quality_summary.to_csv(
    quality_path,
    index=False
)


# ------------------------------------------------------------
# 23. FINAL OUTPUT
# ------------------------------------------------------------

print()
print("=" * 70)
print("CLEANING COMPLETE")
print("=" * 70)

print()
print("Processed files:")

print(
    f"1. {combined_path}"
)

print(
    f"2. {sales_path}"
)

print(
    f"3. {cancellation_path}"
)

print(
    f"4. {customer_path}"
)

print()
print("Analysis files:")

print(
    f"5. {summary_path}"
)

print(
    f"6. {transaction_summary_path}"
)

print(
    f"7. {quality_path}"
)

print()
print("Project 02 cleaning pipeline completed successfully.")
print("=" * 70)
