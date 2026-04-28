"""
etl_pipeline.py
ETL helper functions for the Retail Store Sales dataset.
Called by notebooks/02_cleaning.ipynb via: from scripts.etl_pipeline import basic_clean
"""

import pandas as pd
import numpy as np


# ---------------------------------------------------------------------------
# 1. Basic cleaning (required by notebook 02 template)
# ---------------------------------------------------------------------------

def basic_clean(df: pd.DataFrame) -> pd.DataFrame:
    """
    Apply standard cleaning steps to the raw Retail Store Sales dataset.
    Returns a clean copy of the DataFrame.

    Steps
    -----
    1.  Drop exact duplicate rows.
    2.  Strip leading/trailing whitespace from all string columns.
    3.  Rename columns to snake_case.
    4.  Parse transaction_date → datetime.
    5.  Map discount_applied (True/False/blank) → 1/0/NaN → fillna(0) as int.
    6.  Impute total_spent from price_per_unit * quantity where possible.
    7.  Drop rows where total_spent is still null after imputation.
    8.  Drop rows where total_spent <= 0.
    9.  Fill remaining numeric nulls with column median.
    10. Standardise categorical label casing (Title Case).
    """

    df = df.copy()

    # --- 1. Drop duplicates --------------------------------------------------
    before = len(df)
    df.drop_duplicates(inplace=True)
    dropped = before - len(df)
    if dropped:
        print(f"[basic_clean] Dropped {dropped} duplicate rows.")

    # --- 2. Strip whitespace from object columns ----------------------------
    str_cols = df.select_dtypes(include=["object", "string"]).columns
    for col in str_cols:
        df[col] = df[col].apply(lambda x: x.strip() if isinstance(x, str) else x)

    # --- 3. Rename columns to snake_case ------------------------------------
    rename_map = {
        "Transaction ID":   "transaction_id",
        "Customer ID":      "customer_id",
        "Category":         "category",
        "Item":             "item",
        "Price Per Unit":   "price_per_unit",
        "Quantity":         "quantity",
        "Total Spent":      "total_spent",
        "Payment Method":   "payment_method",
        "Location":         "location",
        "Transaction Date": "transaction_date",
        "Discount Applied": "discount_applied",
    }
    df.rename(columns=rename_map, inplace=True)

    # --- 4. Parse transaction_date ------------------------------------------
    df["transaction_date"] = pd.to_datetime(
        df["transaction_date"], dayfirst=False, errors="coerce"
    )

    # --- 5. Map discount_applied → 0/1 -------------------------------------
    discount_map = {"True": 1, "False": 0, "true": 1, "false": 0,
                    True: 1, False: 0}
    df["discount_applied"] = (
        df["discount_applied"]
        .map(discount_map)
        .fillna(0)
        .astype(int)
    )

    # --- 6. Impute total_spent from price_per_unit * quantity ---------------
    missing_total = df["total_spent"].isnull()
    can_impute = missing_total & df["price_per_unit"].notnull() & df["quantity"].notnull()
    df.loc[can_impute, "total_spent"] = (
        df.loc[can_impute, "price_per_unit"] * df.loc[can_impute, "quantity"]
    )
    imputed = can_impute.sum()
    if imputed:
        print(f"[basic_clean] Imputed {imputed} total_spent values from price_per_unit × quantity.")

    # --- 7. Drop rows where total_spent is still null -----------------------
    still_null = df["total_spent"].isnull().sum()
    if still_null:
        df.dropna(subset=["total_spent"], inplace=True)
        print(f"[basic_clean] Dropped {still_null} rows where total_spent could not be recovered.")

    # --- 8. Drop non-positive total_spent -----------------------------------
    invalid = df["total_spent"] <= 0
    if invalid.any():
        print(f"[basic_clean] Removed {invalid.sum()} rows with total_spent ≤ 0.")
        df = df[~invalid]

    # --- 9. Fill remaining numeric nulls with median ------------------------
    num_cols = df.select_dtypes(include=[np.number]).columns
    for col in num_cols:
        null_count = df[col].isnull().sum()
        if null_count > 0:
            median_val = df[col].median()
            df[col] = df[col].fillna(median_val)
            print(f"[basic_clean] Filled {null_count} nulls in '{col}' with median={median_val:.2f}")

    # --- 10. Standardise categorical casing (Title Case) --------------------
    cat_cols = ["category", "item", "payment_method", "location"]
    for col in cat_cols:
        if col in df.columns:
            df[col] = df[col].str.title()

    # --- 11. Sort the data --------------------------------------------------
    sort_cols = [c for c in ["customer_id", "transaction_date", "transaction_id"] if c in df.columns]
    if sort_cols:
        df.sort_values(by=sort_cols, inplace=True)

    print(f"[basic_clean] Clean dataset shape: {df.shape}")
    return df.reset_index(drop=True)


# ---------------------------------------------------------------------------
# 2. Feature engineering helpers (used in notebook 05)
# ---------------------------------------------------------------------------

def add_derived_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Add business-relevant derived columns for the retail dataset.

    New columns
    -----------
    transaction_year        : Year of transaction
    transaction_month       : Month (1-12)
    transaction_quarter     : Quarter (1-4)
    transaction_day_of_week : Day-of-week name
    is_weekend              : 1 if Sat/Sun else 0
    revenue_bucket          : 'Low' / 'Medium' / 'High' by total_spent tertile
    is_high_value           : 1 if total_spent > 95th percentile else 0
    avg_unit_price          : total_spent / quantity (NaN-safe)
    """

    df = df.copy()

    # Time-based features
    if "transaction_date" in df.columns:
        dt = pd.to_datetime(df["transaction_date"], errors="coerce")
        df["transaction_year"]        = dt.dt.year
        df["transaction_month"]       = dt.dt.month
        df["transaction_quarter"]     = dt.dt.quarter
        df["transaction_day_of_week"] = dt.dt.day_name()
        df["is_weekend"]              = dt.dt.dayofweek.isin([5, 6]).astype(int)

    # Revenue bucket (tertile split)
    if "total_spent" in df.columns:
        low_thr  = df["total_spent"].quantile(0.333)
        high_thr = df["total_spent"].quantile(0.667)
        df["revenue_bucket"] = pd.cut(
            df["total_spent"],
            bins=[-np.inf, low_thr, high_thr, np.inf],
            labels=["Low", "Medium", "High"]
        ).astype(str)

        # High-value transaction flag
        threshold = df["total_spent"].quantile(0.95)
        df["is_high_value"] = (df["total_spent"] > threshold).astype(int)

    # Average unit price (recalculated for consistency)
    if "total_spent" in df.columns and "quantity" in df.columns:
        safe_qty = df["quantity"].replace(0, np.nan)
        df["avg_unit_price"] = (df["total_spent"] / safe_qty).round(2)

    return df


# ---------------------------------------------------------------------------
# 3. KPI computation helper (used in notebook 05)
# ---------------------------------------------------------------------------

def compute_kpis(df: pd.DataFrame) -> dict:
    """
    Compute core business KPIs for the retail dataset and return as a dict.

    KPIs
    ----
    total_transactions      : Total number of transactions
    total_revenue           : Sum of total_spent
    avg_order_value         : Mean total_spent per transaction
    median_order_value      : Median total_spent
    discount_rate_pct       : % of transactions where discount was applied
    discounted_avg_revenue  : Avg total_spent when discount applied
    non_discounted_avg_rev  : Avg total_spent when no discount
    top_category            : Category with highest total revenue
    top_payment_method      : Most used payment method (by transaction count)
    top_location            : Location with highest revenue
    online_pct              : % of transactions that are Online
    instore_pct             : % of transactions that are In-store
    """

    kpis = {}

    kpis["total_transactions"]   = len(df)
    kpis["total_revenue"]        = round(df["total_spent"].sum(), 2)
    kpis["avg_order_value"]      = round(df["total_spent"].mean(), 2)
    kpis["median_order_value"]   = round(df["total_spent"].median(), 2)

    # Discount impact
    disc_df    = df[df["discount_applied"] == 1]
    no_disc_df = df[df["discount_applied"] == 0]
    kpis["discount_rate_pct"]        = round(df["discount_applied"].mean() * 100, 2)
    kpis["discounted_avg_revenue"]   = round(disc_df["total_spent"].mean(), 2) if len(disc_df) else 0.0
    kpis["non_discounted_avg_rev"]   = round(no_disc_df["total_spent"].mean(), 2) if len(no_disc_df) else 0.0

    # Top performers
    if "category" in df.columns:
        kpis["top_category"] = df.groupby("category")["total_spent"].sum().idxmax()

    if "payment_method" in df.columns:
        kpis["top_payment_method"] = df["payment_method"].value_counts().idxmax()

    if "location" in df.columns:
        loc_rev = df.groupby("location")["total_spent"].sum()
        kpis["top_location"] = loc_rev.idxmax()
        total = loc_rev.sum()
        kpis["online_pct"]  = round(loc_rev.get("Online", 0) / total * 100, 2)
        kpis["instore_pct"] = round(loc_rev.get("In-Store", loc_rev.get("In-store", 0)) / total * 100, 2)

    return kpis
