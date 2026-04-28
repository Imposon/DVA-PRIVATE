"""
run_pipeline.py
Executes the full ETL + KPI pipeline for the Retail Store Sales dataset.
Equivalent to running notebooks 01-05 in sequence.
Run from the project root: python3 run_pipeline.py
"""

import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(PROJECT_ROOT))

import pandas as pd
import numpy as np

from scripts.etl_pipeline import add_derived_features, basic_clean, compute_kpis

PROCESSED_DIR = PROJECT_ROOT / "data" / "processed"
PROCESSED_DIR.mkdir(parents=True, exist_ok=True)

RAW_PATH           = PROJECT_ROOT / "data" / "raw" / "retail_store_sales.csv"
CLEANED_PATH       = PROCESSED_DIR / "cleaned_dataset.csv"
TABLEAU_READY_PATH = PROCESSED_DIR / "tableau_ready_dataset.csv"


# ── STEP 1: Load ──────────────────────────────────────────────────────────────
print("\n[1/6] Loading raw dataset ...")
df_raw = pd.read_csv(RAW_PATH)
print(f"      Raw shape: {df_raw.shape}")


# ── STEP 2: Clean ─────────────────────────────────────────────────────────────
print("\n[2/6] Applying basic_clean ...")
df_clean = basic_clean(df_raw)


# ── STEP 3: Derive features ───────────────────────────────────────────────────
print("\n[3/6] Adding derived features ...")
df_clean = add_derived_features(df_clean)

# revenue_bucket may be Categorical; convert to string for CSV compatibility
if "revenue_bucket" in df_clean.columns:
    df_clean["revenue_bucket"] = df_clean["revenue_bucket"].astype(str)

print(f"      Clean shape: {df_clean.shape}")
df_clean.to_csv(CLEANED_PATH, index=False)
print(f"      Saved → {CLEANED_PATH}")


# ── STEP 4: Compute KPIs ──────────────────────────────────────────────────────
print("\n[4/6] Computing KPIs ...")
kpis = compute_kpis(df_clean)
print()
print("  ┌─────────────────────────────────────────────────┐")
print("  │        RETAIL STORE SALES — KPIs                │")
print("  ├─────────────────────────────────────────────────┤")
for k, v in kpis.items():
    label = k.replace("_", " ").title()
    val   = f"{v:,.2f}" if isinstance(v, float) else (f"{v:,}" if isinstance(v, int) else str(v))
    print(f"  │  {label:<33}: {val}")
print("  └─────────────────────────────────────────────────┘")

kpi_df = pd.DataFrame([{"kpi": k, "value": str(v)} for k, v in kpis.items()])
kpi_df.to_csv(PROCESSED_DIR / "kpi_summary.csv", index=False)
print(f"      Saved → kpi_summary.csv")


# ── STEP 5: Build aggregated Tableau export tables ────────────────────────────
print("\n[5/6] Building aggregated export tables ...")


def sales_agg(df, group_col):
    """Aggregate revenue & transaction metrics by a categorical column."""
    agg = (
        df.groupby(group_col, observed=True)
        .agg(
            total_revenue=("total_spent", "sum"),
            total_transactions=("transaction_id", "count"),
            avg_order_value=("total_spent", "mean"),
            discount_transactions=("discount_applied", "sum"),
        )
        .round(2)
        .reset_index()
    )
    agg["discount_rate_pct"] = (
        agg["discount_transactions"] / agg["total_transactions"] * 100
    ).round(2)
    return agg


# Sales by category
sales_by_cat = sales_agg(df_clean, "category")
sales_by_cat.to_csv(PROCESSED_DIR / "sales_by_category.csv", index=False)
print("      Saved → sales_by_category.csv")

# Sales by payment method
sales_by_pay = sales_agg(df_clean, "payment_method")
sales_by_pay.to_csv(PROCESSED_DIR / "sales_by_payment.csv", index=False)
print("      Saved → sales_by_payment.csv")

# Sales by location (Online vs In-store)
sales_by_loc = sales_agg(df_clean, "location")
sales_by_loc.to_csv(PROCESSED_DIR / "sales_by_location.csv", index=False)
print("      Saved → sales_by_location.csv")

# Discount impact: with vs without discount
disc_impact = (
    df_clean.groupby("discount_applied", observed=True)
    .agg(
        total_transactions=("transaction_id", "count"),
        total_revenue=("total_spent", "sum"),
        avg_order_value=("total_spent", "mean"),
    )
    .round(2)
    .reset_index()
)
disc_impact["discount_applied"] = disc_impact["discount_applied"].map({1: "Yes", 0: "No"})
disc_impact.to_csv(PROCESSED_DIR / "discount_impact.csv", index=False)
print("      Saved → discount_impact.csv")

# Monthly trend
if "transaction_year" in df_clean.columns and "transaction_month" in df_clean.columns:
    monthly = (
        df_clean.groupby(["transaction_year", "transaction_month"], observed=True)
        .agg(
            total_transactions=("transaction_id", "count"),
            total_revenue=("total_spent", "sum"),
            avg_order_value=("total_spent", "mean"),
            discount_transactions=("discount_applied", "sum"),
        )
        .round(2)
        .reset_index()
    )
    monthly["period"] = (
        monthly["transaction_year"].astype(str) + "-" +
        monthly["transaction_month"].astype(str).str.zfill(2)
    )
    monthly.to_csv(PROCESSED_DIR / "sales_monthly_trend.csv", index=False)
    print("      Saved → sales_monthly_trend.csv")

# Top items by revenue
if "item" in df_clean.columns:
    top_items = (
        df_clean.groupby("item", observed=True)
        .agg(
            total_revenue=("total_spent", "sum"),
            total_transactions=("transaction_id", "count"),
            avg_order_value=("total_spent", "mean"),
        )
        .round(2)
        .sort_values("total_revenue", ascending=False)
        .reset_index()
    )
    top_items.to_csv(PROCESSED_DIR / "sales_by_item.csv", index=False)
    print("      Saved → sales_by_item.csv")


# ── STEP 6: Export Tableau-Ready dataset ──────────────────────────────────────
print("\n[6/6] Exporting Tableau-ready dataset ...")

tableau_cols = [
    "transaction_id", "customer_id",
    "category", "item",
    "price_per_unit", "quantity", "total_spent",
    "payment_method", "location",
    "transaction_date", "discount_applied",
    "transaction_year", "transaction_month", "transaction_quarter",
    "transaction_day_of_week", "is_weekend",
    "revenue_bucket", "is_high_value", "avg_unit_price",
]
available = [c for c in tableau_cols if c in df_clean.columns]
df_clean[available].to_csv(TABLEAU_READY_PATH, index=False)
print(f"      Saved → {TABLEAU_READY_PATH}")
print(f"      Shape : {df_clean[available].shape}")


# ── Final checklist ───────────────────────────────────────────────────────────
print("\n" + "─" * 60)
print("  PIPELINE COMPLETE — Output Checklist")
print("─" * 60)
all_files = [
    "cleaned_dataset.csv",
    "tableau_ready_dataset.csv",
    "kpi_summary.csv",
    "sales_by_category.csv",
    "sales_by_payment.csv",
    "sales_by_location.csv",
    "discount_impact.csv",
    "sales_monthly_trend.csv",
    "sales_by_item.csv",
]
for fname in all_files:
    p = PROCESSED_DIR / fname
    status = "✅" if p.exists() else "❌"
    size   = f"{p.stat().st_size / 1024:.1f} KB" if p.exists() else "MISSING"
    print(f"  {status}  {fname:<46} {size}")
print()
