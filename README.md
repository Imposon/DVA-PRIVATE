# NST DVA Capstone 2 - Project Repository

> **Newton School of Technology | Data Visualization & Analytics**
> A 2-week industry simulation capstone using Python, GitHub, and Tableau to convert raw data into actionable business intelligence.

---

## Before You Start

1. Rename the repository using the format `SectionName_TeamID_ProjectName`.
2. Fill in the project details and team table below.
3. Add the raw dataset to `data/raw/`.
4. Complete the notebooks in order from `01` to `05`.
5. Publish the final dashboard and add the public link in `tableau/dashboard_links.md`.
6. Export the final report and presentation as PDFs into `reports/`.

### Quick Start

If you are working locally:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
jupyter notebook
```

If you are working in Google Colab:

- Upload or sync the notebooks from `notebooks/`
- Keep the final `.ipynb` files committed to GitHub
- Export any cleaned datasets into `data/processed/`

---

## Project Overview

| Field | Details |
|---|---|
| **Project Title** | Retail Store Sales Analysis |
| **Sector** | Retail / E-commerce |
| **Team ID** | _To be filled by team_ |
| **Section** | _To be filled by team_ |
| **Faculty Mentor** | _To be filled by team_ |
| **Institute** | Newton School of Technology |
| **Submission Date** | _To be filled by team_ |

### Team Members

| Role | Name | GitHub Username |
|---|---|---|
| Project Lead | _Name_ | `github-handle` |
| Data Lead | _Name_ | `github-handle` |
| ETL Lead | _Name_ | `github-handle` |
| Analysis Lead | _Name_ | `github-handle` |
| Visualization Lead | _Name_ | `github-handle` |
| Strategy Lead | _Name_ | `github-handle` |
| PPT and Quality Lead | _Name_ | `github-handle` |

---

## Business Problem

The retail sector faces continuous pressure to optimize product assortment, pricing strategies, and marketing campaigns to maximize revenue. Understanding customer purchasing patterns across different channels (Online vs. In-Store) and payment methods is crucial for targeted promotions. Furthermore, measuring the true impact of discounts on overall revenue and volume helps refine discounting strategies to ensure profitability.

**Core Business Question**

> How can we optimize sales strategies by understanding the impact of discounts, evaluating channel performance (Online vs. In-Store), and identifying top-revenue product categories?

**Decision Supported**

> This analysis enables retail management to optimize discount frequency and depth, allocate marketing budget toward high-performing categories, and tailor the shopping experience based on preferred payment methods and location trends.

---

## Dataset

| Attribute | Details |
|---|---|
| **Source Name** | Kaggle - Retail Store Sales |
| **Row Count** | ~12,500 |
| **Column Count** | 11 original columns |
| **Time Period Covered** | 2022 to 2025 |
| **Format** | CSV |

**Key Columns Used**

| Column Name | Description | Role in Analysis |
|---|---|---|
| `total_spent` | Total transaction amount | Primary measure for revenue and AOV |
| `category` | Product category | Used for segmenting revenue by product type |
| `discount_applied` | Whether a discount was given | Used to analyze the business impact of discounting |
| `location` | Online vs. In-store | Used to analyze channel performance |

For full column definitions, see [`docs/data_dictionary.md`](docs/data_dictionary.md).

---

## KPI Framework

| KPI | Definition | Formula / Computation |
|---|---|---|
| **Total Revenue** | The overall revenue generated from all sales | `sum(total_spent)` |
| **Average Order Value (AOV)** | The average revenue per transaction | `mean(total_spent)` |
| **Discount Rate** | Percentage of transactions that received a discount | `count(discount_applied == 1) / total_transactions` |
| **Online vs. In-store %** | Revenue/transaction share by location channel | `count(location == 'Online') / total_transactions` |

Document KPI logic clearly in `notebooks/04_statistical_analysis.ipynb` and `notebooks/05_final_load_prep.ipynb`.

---

## Tableau Dashboard

| Item | Details |
|---|---|
| **Dashboard URL** | _Paste Tableau Public link here_ |
| **Executive View** | High-level summary of total revenue, AOV, and discount usage |
| **Operational View** | Breakdown of sales by category, payment method, and monthly trends |
| **Main Filters** | Date range, Category, Location, Payment Method |

Store dashboard screenshots in [`tableau/screenshots/`](tableau/screenshots/) and document the public links in [`tableau/dashboard_links.md`](tableau/dashboard_links.md).

---

## Key Insights

_List 8-12 major findings from the analysis, written in decision language. Each insight should tell the reader what to think or act upon, not merely describe a chart._

1. _Insight 1_
2. _Insight 2_
3. _Insight 3_
4. _Insight 4_
5. _Insight 5_
6. _Insight 6_
7. _Insight 7_
8. _Insight 8_

---

## Recommendations

_Provide 3-5 specific, actionable business recommendations, each linked directly to an insight above._

| # | Insight | Recommendation | Expected Impact |
|---|---|---|---|
| 1 | _Which insight does this address?_ | _What should the stakeholder do?_ | _What measurable impact do you expect?_ |
| 2 | _Which insight does this address?_ | _What should the stakeholder do?_ | _What measurable impact do you expect?_ |
| 3 | _Which insight does this address?_ | _What should the stakeholder do?_ | _What measurable impact do you expect?_ |

---

## Repository Structure

```text
SectionName_TeamID_ProjectName/
|
|-- README.md
|
|-- data/
|   |-- raw/                         # Original dataset (never edited)
|   `-- processed/                   # Cleaned output from ETL pipeline
|
|-- notebooks/
|   |-- 01_extraction.ipynb
|   |-- 02_cleaning.ipynb
|   |-- 03_eda.ipynb
|   |-- 04_statistical_analysis.ipynb
|   `-- 05_final_load_prep.ipynb
|
|-- scripts/
|   `-- etl_pipeline.py
|
|-- tableau/
|   |-- screenshots/
|   `-- dashboard_links.md
|
|-- reports/
|   |-- README.md
|   |-- project_report_template.md
|   `-- presentation_outline.md
|
|-- docs/
|   `-- data_dictionary.md
|
|-- DVA-oriented-Resume/
`-- DVA-focused-Portfolio/
```

---

## Analytical Pipeline

The project follows a structured 7-step workflow:

1. **Define** - Sector selected, problem statement scoped, mentor approval obtained.
2. **Extract** - Raw dataset sourced and committed to `data/raw/`; data dictionary drafted.
3. **Clean and Transform** - Cleaning pipeline built in `notebooks/02_cleaning.ipynb` and `scripts/etl_pipeline.py`.
4. **Analyze** - EDA and statistical analysis performed in notebooks `03` and `04`.
5. **Visualize** - Interactive Tableau dashboard built and published on Tableau Public.
6. **Recommend** - 3-5 data-backed business recommendations delivered.
