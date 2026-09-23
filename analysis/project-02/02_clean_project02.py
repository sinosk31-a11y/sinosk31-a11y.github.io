import pandas as pd
from pathlib import Path


# ============================================================
# PROJECT 02
# Customer & Operational Analytics
# Data Cleaning Pipeline
# ============================================================

# ------------------------------------------------------------
# 1. PATHS
# ------------------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parents[2]

RAW_FILE = PROJECT_ROOT / "data" / "raw" / "online_retail_II.xlsx"

PROCESSED_DIR = PROJECT_ROOT / "data" / "processed"
ANALYSIS_DIR = PROJECT_ROOT / "analysis" / "project-02"

PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
ANALYSIS_DIR.mkdir(parents=True, exist_ok=True)


# ------------------------------------------------------------
# 2. LOAD SOURCE DATA
# ------------------------------------------------------------

print("Loading source workbook...")

year_1 = pd.read_excel(
    RAW_FILE,
    sheet_name="Year 2009-2010"
)

year_2 = pd.read_excel(
    RAW_FILE,
    sheet_name="Year 2010-2011"
)

print(f"Year 2009-2010: {len(year_1):,} rows")
print(f"Year 2010-2011: {len(year_2):,} rows")


# ------------------------------------------------------------
# 3. ADD SOURCE IDENTIFIER
# ------------------------------------------------------------

year_1["source_sheet"] = "Year 2009-2010"
year_2["source_sheet"] = "Year 2010-2011"


# ------------------------------------------------------------
# 4. COMBINE DATASETS
# ------------------------------------------------------------

df = pd.concat(
    [year_1, year_2],
    ignore_index=True
)

print(f"Combined rows: {len(df):,}")


# ------------------------------------------------------------
# 5. STANDARDIZE COLUMN NAMES
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
# 6. STANDARDIZE TEXT FIELDS
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
# 7. STANDARDIZE NUMERIC FIELDS
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
# 8. STANDARDIZE DATE FIELD
# ------------------------------------------------------------

df["invoice_date"] = pd.to_datetime(
    df["invoice_date"],
    errors="coerce"
)


# ------------------------------------------------------------
# 9. CREATE TRANSACTION FLAGS
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
# 10. CALCULATE LINE REVENUE
# ------------------------------------------------------------

df["revenue"] = (
    df["quantity"] *
    df["unit_price"]
)


# ------------------------------------------------------------
# 11. CLASSIFY TRANSACTIONS
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

    if row["quantity"] > 0 and row["unit_price"] > 0:
        return "SALE"

    return "OTHER"


df["transaction_type"] = df.apply(
    classify_transaction,
    axis=1
)


# ------------------------------------------------------------
# 12. COUNT EXACT DUPLICATES
# ------------------------------------------------------------

duplicate_count = int(
    df.duplicated().sum()
)

print(
    f"Exact duplicate rows identified: "
    f"{duplicate_count:,}"
)


# ------------------------------------------------------------
# 13. REMOVE EXACT DUPLICATES
# ------------------------------------------------------------

df = df.drop_duplicates().copy()

print(
    f"Rows after duplicate removal: "
    f"{len(df):,}"
)


# ------------------------------------------------------------
# 14. CREATE SALES DATASET
# ------------------------------------------------------------

sales = df[
    (df["transaction_type"] == "SALE")
].copy()


# ------------------------------------------------------------
# 15. CREATE CANCELLATION DATASET
# ------------------------------------------------------------

cancellations = df[
    (df["transaction_type"] == "CANCELLATION")
].copy()


# ------------------------------------------------------------
# 16. CREATE CUSTOMER-ANALYTICS DATASET
# ------------------------------------------------------------

customer_transactions = sales[
    sales["customer_id"].notna()
].copy()


# ------------------------------------------------------------
# 17. CREATE MONTH/YEAR FIELDS
# ------------------------------------------------------------

for dataset in [
    df,
    sales,
    cancellations,
    customer_transactions
]:

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
# 18. SAVE PROCESSED DATASETS
# ------------------------------------------------------------

combined_path = (
    PROCESSED_DIR /
    "project02_transactions_cleaned.csv"
)

sales_path = (
    PROCESSED_DIR /
    "project02_sales.csv"
)

cancellation_path = (
    PROCESSED_DIR /
    "project02_cancellations.csv"
)

customer_path = (
    PROCESSED_DIR /
    "project02_customer_transactions.csv"
)


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
# 19. CREATE CLEANING SUMMARY
# ------------------------------------------------------------

summary = pd.DataFrame(
    [
        {
            "metric": "Original rows",
            "value": len(year_1) + len(year_2)
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
            "value": customer_transactions["customer_id"]
            .nunique()
        },
        {
            "metric": "Unique products",
            "value": sales["stock_code"]
            .nunique()
        },
        {
            "metric": "Countries",
            "value": sales["country"]
            .nunique()
        }
    ]
)


summary_path = (
    ANALYSIS_DIR /
    "02_cleaning_summary.csv"
)


summary.to_csv(
    summary_path,
    index=False
)


# ------------------------------------------------------------
# 20. COMPLETION MESSAGE
# ------------------------------------------------------------

print()
print("=" * 60)
print("PROJECT 02 CLEANING COMPLETE")
print("=" * 60)

print(f"Cleaned dataset:")
print(combined_path)

print(f"Sales dataset:")
print(sales_path)

print(f"Cancellation dataset:")
print(cancellation_path)

print(f"Customer transactions:")
print(customer_path)

print(f"Cleaning summary:")
print(summary_path)

print("=" * 60)
