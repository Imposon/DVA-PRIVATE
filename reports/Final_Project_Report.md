# Retail Store Sales Analytics: Final Project Report

## 1. Cover Page
- **Project title:** Retail Store Sales Analytics: Driving Revenue Through Data
- **Sector:** Retail / E-Commerce
- **Team Name:** CS:GO
- **Team Members:** Aditya Sinha, Ansh Kumar, Ayush Kumar, Vedansha Srivastava, Shekhar Narayan Mishra
- **Institute:** Newton School of Technology
- **Faculty mentor:** Vrushali Masane
- **Submission date:** 28 April 2026

---

## 2. Executive Summary
**Problem:** Retail margins are thin, and leadership needs evidence on whether discounting and channel strategy (Online vs. In-Store) meaningfully improve revenue and Average Order Value (AOV).
**Approach:** Built an end-to-end analytics pipeline using Python over a Kaggle Retail Store Sales dataset (2022–2025), including ETL, EDA, KPI design, statistical testing (ANOVA, Chi-Squared, Mann-Whitney U), and OLS regression.
**Key insights:** About 33% of transactions use discounts, but the AOV lift is statistically significant yet practically negligible. Category and transaction quantity are the dominant drivers of revenue. Discounts are applied unevenly across channels.
**Key recommendations:** Move to threshold-based discounts, prioritize top revenue categories, and synchronize promotions across channels.

---

## 3. Sector Context and Problem Statement
**Sector context:** Retail and e-commerce operations rely heavily on optimized pricing, inventory, and channel mix to sustain profitability. With thin margins, discounting and channel investments directly impact top-line revenue, making data-backed decisions essential.
**Problem Statement:** The core objective is to quantify the impact of discounting and channel choice on revenue and AOV, and to identify category-level revenue drivers.
**Scope and Success Criteria:** Analyzing transactions from 2022–2025 across product categories, discount applications, and channels. Success is defined as delivering statistically validated insights, a KPI framework, and actionable recommendations supported by a Tableau dashboard.

---

## 4. Data Description — Source, Structure, Size, and Limitations
- **Source:** Kaggle Retail Store Sales dataset (publicly available).
- **Structure and Size:** ~12,500 raw rows spanning 2022–2025; 11 columns in the raw file including `transaction_id`, `customer_id`, `category`, `total_spent`, `location`, `discount_applied`, and `transaction_date`.
- **Limitations:** 
  - The dataset lacks direct profitability or cost-of-goods-sold (COGS) margin data.
  - Missing pricing data required median imputation, which might smooth out true price volatility.
  - Public dataset format limits deep, customer-level demographic context.

---

## 5. Data Cleaning and ETL Methodology (Python Pipeline)
An automated Python pipeline was developed to clean and transform the raw data into an analysis-ready format.
- **Standardization:** Column names were converted to `snake_case` and category labels were text-normalized.
- **Imputation:** Missing `total_spent` values were calculated using `price_per_unit * quantity`. Missing `price_per_unit` gaps were filled via category medians to safely prevent skew without dropping viable transactions.
- **Type Casting & Feature Engineering:** `transaction_date` was cast to datetime to derive time-based features (year, month, quarter, day_of_week, is_weekend). `discount_applied` was mapped cleanly to binary (0/1). Additional features like `revenue_bucket` and `is_high_value` were generated.
- **Output:** The resulting `cleaned_dataset.csv` contains 11,971 pristine rows and 19 analysis-ready columns.

---

## 6. KPI and Metric Framework
The following metrics were designed to measure revenue health, promotional dependency, and channel mix:
- **Total Revenue:** Sum of `total_spent` across all transactions. Indicates top-line financial health.
- **Average Order Value (AOV):** Calculated as (Sum of `total_spent` / Transaction Count). Measures cart sizes and customer value.
- **Discount Rate:** Calculated as (Discounted Transactions / All Transactions). Tracks reliance on margin-eroding promotions.
- **Channel Revenue Share:** Revenue segmented by `location` (Online vs. In-Store) as a percentage of total revenue. Tracks omnichannel balance.

---

## 7. EDA with Visualisations and Written Insights
- **Major trends:** `total_spent` is right-skewed with a long tail of high-value orders. Monthly revenue displays strong seasonal purchasing peaks aligned with major retail periods (holidays and mid-year sales).
- **Segment-level insights:** Online and In-Store revenues are incredibly balanced. However, category contribution is heavily concentrated in a few top segments.
- **Visual Insights:**
  - *Distribution of Spend:* Histograms show massive concentration in low-to-medium value carts.
  - *Category Performance:* Bar charts highlight that top categories generate exponentially more revenue than the bottom 20%.
  - *Discount Penetration:* Pie charts reveal that 33% of all orders apply a discount.
  - *Discount vs. AOV:* Side-by-side boxplots visually suggest only a marginal AOV increase when discounts are present.

*(Note: Please refer to the presentation and dashboard for exact chart screenshots.)*

---

## 8. Statistical Analysis Results
To validate the visual findings, rigorous statistical testing was conducted using Python (`scipy` and `statsmodels`):
- **Shapiro-Wilk Test:** Confirmed that `total_spent` is not normally distributed, necessitating non-parametric tests.
- **Mann-Whitney U Test:** Compared AOV between discounted and non-discounted orders. Result: Statistically significant difference, but the effect size is practically negligible (under $2 per order).
- **One-Way ANOVA:** Assessed the impact of product category on AOV. Result: Category significantly impacts AOV (p < 0.05), proving product mix is more vital than discounting.
- **Chi-Squared Test:** Evaluated the relationship between sales channel and discount frequency. Result: Discounts are unevenly distributed between Online and In-Store channels (p < 0.05).
- **OLS Linear Regression:** Modeled `total_spent` against quantity and discounts. Result: Quantity is the overwhelming driver of revenue; the discount coefficient is minimal.

---

## 9. Dashboard Design — Screenshots and Explanation
An interactive Tableau dashboard was built directly on top of the aggregated `tableau_ready_dataset.csv`.
- **Executive View:** Features KPI scorecards (Total Revenue, AOV, Discount Rate) and high-level time-series trend lines for leadership.
- **Operational View:** Deep dives into Category splits and Channel performance using dual-axis charts.
- **Interactivity:** Includes global filters for Category, Channel, Time Period, and Discount Flag, allowing users to drill down into specific performance variances.

*(Note: Insert dashboard screenshots here before exporting to PDF.)*

---

## 10. 8–12 Key Insights Written in Decision Language
1. Roughly one-third (33%) of all transactions are discounted, signaling a heavy, systemic reliance on promotions.
2. Discounted orders show a statistically significant but practically negligible AOV lift (less than $2), meaning we are giving away margin for free.
3. Category mix, rather than discounting, is the primary driver of high Average Order Value.
4. A small set of core categories contributes the vast majority of top-line revenue, exposing an asymmetry in product performance.
5. The bottom 20% of categories contribute marginally to revenue and take up unnecessary inventory space.
6. Online and In-Store channels contribute near-equal revenue, indicating a very healthy omnichannel presence.
7. Despite equal channel revenue, discounts are applied unevenly across Online and In-Store, indicating siloed promotional strategies.
8. Transaction quantity is the dominant, proven predictor of `total_spent` in regression modeling.
9. Monthly revenue displays reliable seasonal peaks aligned with major retail periods, allowing for predictable cash flow.
10. Simple forecasting suggests stable, cyclical baseline revenue over the next two quarters.

---

## 11. 3–5 Actionable Business Recommendations
1. **Optimize Discount Thresholds:** Shift from flat percentage discounts to threshold triggers (e.g., "Spend $150 to unlock 10%"). This forces an increase in transaction quantity—the proven driver of revenue—and protects baseline margins.
2. **Reallocate Marketing Budget:** Concentrate advertising spend heavily on the top-performing categories identified in the ANOVA testing. 
3. **Rationalize Inventory:** Audit the bottom 20% of low-performing categories for potential liquidation to free up working capital and warehouse space.
4. **Unify Omnichannel Promotions:** Implement a centralized loyalty program to standardize offers across Online and In-Store. This fixes the channel discrepancy and stabilizes the customer experience.

---

## 12. Impact Estimation, Limitations, and Future Scope
- **Impact Estimation:** Shifting to threshold-based discounts and focusing on top categories is expected to yield higher basket sizes, protected profit margins, and a clearer ROI on marketing spend. Modifying digital discount thresholds is highly feasible in the short term.
- **Limitations:** The absence of direct cost-of-goods-sold (COGS) data prevents exact margin calculations. Additionally, simple linear forecasting models may not capture complex macroeconomic shifts or black-swan events.
- **Future Scope:** Incorporate granular inventory and margin data. Implement advanced predictive time-series models (like Prophet) for robust forecasting, and conduct market basket analysis to drive intelligent cross-selling strategies.

---

## 14. Contribution Matrix

| Team Member | Dataset & Sourcing | ETL & Cleaning | EDA & Analysis | Statistical Analysis | Tableau Dashboard | Report Writing | PPT & Viva |
|---|---|---|---|---|---|---|---|
| Ansh Kumar | | Worked on | Assisted | Worked on | Assisted | Worked on | |
| Aditya Sinha | Worked on | Assisted | Worked on | Worked on | Worked on | | |
| Ayush Kumar | Worked on | Worked on | Worked on | | | |  |
| Shekhar Narayan Mishra | | | | | | Assisted| Worked on |
| Vedansha Srivastava | | | Worked on | | | | Worked on |
