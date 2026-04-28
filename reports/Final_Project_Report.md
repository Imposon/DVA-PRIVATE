# 1. Cover Page

- **Project title:** Retail Store Sales Analytics: Driving Revenue through Data
- **Sector:** Retail / E-Commerce
- **Team ID and team members:** [Team ID], Rahul, Priya, Ankit, Sneha, Arjun
- **Faculty mentor:** [Faculty Mentor Name]
- **Institute:** Newton School of Technology
- **Submission date:** April 2026

## 2. Executive Summary

- **Problem:** Retail margins are thin, and there's a need to understand how discounting strategies and channel distribution impact total revenue and Average Order Value (AOV).
- **Approach:** End-to-end data analytics pipeline using ETL processes, Exploratory Data Analysis (EDA), advanced statistical modeling (ANOVA, Chi-Squared, Mann-Whitney U, and OLS Linear Regression), and Tableau dashboarding.
- **Key insights:** 33% of transactions involve a discount, but the monetary lift on AOV is statistically significant yet practically negligible. Category selection strongly drives transaction size. Discounts are applied unevenly across Online and In-Store channels.
- **Key recommendations:** Optimize discount thresholds, reallocate marketing budgets to top categories, and unify omnichannel promotional strategies.

## 3. Sector and Business Context

- **Sector overview:** The retail and e-commerce sector operates on thin margins, requiring precise promotional and marketing investments.
- **Decision-maker / stakeholder:** Retail Management, Marketing Executives, Strategy Operations.
- **Why this problem matters:** Every discounting and marketing decision is highly consequential. Management needs data-driven strategies to prevent margin erosion from frequent, ineffective discounting and to guide omnichannel investments.

## 4. Problem Statement and Objectives

- **Formal problem definition:** Determine the impact of frequent discounting and specific channel performance on transaction volumes and revenue to optimize profitability.
- **Scope:** Analysis of retail store sales data spanning from 2022 to 2025.
- **Success criteria:** Deliver statistically validated insights and an interactive dashboard that translates raw data into actionable recommendations for marketing and promotional adjustments.

## 5. Data Description

- **Source citation and access link:** Kaggle Retail Store Sales dataset.
- **Dataset size and coverage:** 12,500 rows, covering 2022–2025.
- **Key columns:** `Transaction ID`, `Customer ID`, `Category`, `Total Spent`, `Location`, and `Discount Applied`.
- **Data quality issues:** Inconsistent capitalization, missing pricing data, mixed data types (boolean/string) in discount fields.

## 6. Cleaning and Transformation

- **Major cleaning steps:**
  # Retail Store Sales Analytics: Final Project Report

  ## 1. Cover Page

  - **Project title:** Retail Store Sales Analytics: Driving Revenue Through Data
  - **Sector:** Retail / E-Commerce
  - **Team ID and team members:** TBD
  - **Faculty mentor:** TBD
  - **Institute:** Newton School of Technology | Data Visualization & Analytics
  - **Submission date:** 28 April 2026

  ---

  ## 2. Executive Summary

  - **Problem:** Retail margins are thin, and leadership needs evidence on whether discounting and channel strategy (Online vs. In-Store) meaningfully improve revenue and Average Order Value (AOV).
  - **Approach:** Built an end-to-end analytics pipeline over a Kaggle Retail Store Sales dataset (2022–2025), including ETL, EDA, KPI design, statistical testing (ANOVA, Chi-Squared, Mann-Whitney U), and OLS regression.
  - **Key insights:** About 33% of transactions use discounts, but the AOV lift is statistically significant yet practically negligible. Category and quantity are the dominant drivers of revenue. Discounts are applied unevenly across channels.
  - **Key recommendations:** Move to threshold-based discounts, prioritize top revenue categories, and synchronize promotions across channels.

  ---

  ## 3. Sector and Business Context

  - **Sector overview:** Retail and e-commerce operations rely on optimized pricing, inventory, and channel mix to sustain profitability.
  - **Decision-maker / stakeholder:** Retail leadership overseeing pricing strategy, category management, and omnichannel growth.
  - **Why this problem matters:** Discounting and channel investments directly impact margin and revenue, making data-backed decisions essential.

  ---

  ## 4. Problem Statement and Objectives

  - **Formal problem definition:** Quantify the impact of discounting and channel choice on revenue and AOV, and identify category-level revenue drivers.
  - **Scope:** Transactions from 2022–2025, covering product categories, discount application, channel, and time-based behavior.
  - **Success criteria:** Deliver statistically validated insights, a KPI framework, and actionable recommendations supported by a dashboard.

  ---

  ## 5. Data Description

  - **Source citation and access link:** Kaggle Retail Store Sales dataset (publicly available).
  - **Dataset size and coverage:** ~12,500 raw rows spanning 2022–2025; 11 columns in the raw file.
  - **Key columns:** `transaction_id`, `customer_id`, `category`, `total_spent`, `location`, `discount_applied`, `transaction_date`.
  - **Data quality issues:** Missing `total_spent` and `price_per_unit`, inconsistent category capitalization, mixed types in discount fields.

  ---

  ## 6. Cleaning and Transformation

  - **Major cleaning steps:**
    - Standardized column names to `snake_case` and normalized category labels.
    - Imputed missing `total_spent` using `price_per_unit * quantity` and filled price gaps via median.
    - Cast `transaction_date` to datetime and derived time features.
    - Mapped `discount_applied` to 0/1 and engineered additional features.
  - **Assumptions made:** Median price is a safe fallback for missing unit prices; unrecoverable rows are removed to protect integrity.
  - **Output dataset description:** `cleaned_dataset.csv` with 11,971 rows and 19 analysis-ready columns.

  ---

  ## 7. KPI Framework

  - **KPI definitions:**
    - **Total Revenue:** Sum of `total_spent` across all transactions.
    - **Average Order Value (AOV):** Total revenue divided by number of transactions.
    - **Discount Rate:** Share of transactions with `discount_applied = 1`.
    - **Channel Revenue Share:** Revenue by `location` as a percentage of total.
  - **Formulae:**
    - $\text{AOV} = \frac{\sum \text{total\_spent}}{\text{transaction count}}$
    - $\text{Discount Rate} = \frac{\text{discounted transactions}}{\text{all transactions}}$
  - **Why each KPI matters:** These KPIs measure revenue health, promotional dependency, and the channel mix driving performance.

  ---

  ## 8. Exploratory Analysis

  - **Major trends:** `total_spent` is right-skewed with a long tail of high-value orders; monthly revenue shows seasonal peaks.
  - **Segment-level insights:** Online and In-Store revenues are balanced; category contribution is concentrated in top segments.
  - **Visual summaries:** Category revenue bars, discount penetration pie, AOV comparison by discount, and monthly revenue trend line.

  ---

  ## 9. Statistical Analysis

  - **Method used:** Shapiro-Wilk test for normality, Mann-Whitney U for AOV differences, One-Way ANOVA for category effects, Chi-Squared for channel-discount dependence, and OLS regression for revenue drivers.
  - **Results:**
    - Discounts yield a statistically significant AOV lift, but the effect size is small (under $2 per order).
    - Category significantly impacts AOV (ANOVA p < 0.05).
    - Discounts are unevenly distributed by channel (Chi-Squared p < 0.05).
    - Quantity is the strongest driver of `total_spent` (OLS).
  - **Business interpretation:** Discounting is overused for limited gain; category mix and basket size are the real levers.

  ---

  ## 10. Dashboard Walkthrough

  - **Dashboard objective:** Provide executives and operators with a single view of revenue, discounting, category performance, and channel trends.
  - **Executive view:** Total revenue, AOV, discount rate, and high-level trends.
  - **Operational view:** Category and channel breakdowns with monthly trend lines.
  - **Filters and interactivity:** Category, channel, time period, and discount flag filters for drilldowns.

  ---

  ## 11. Key Insights

  1. Roughly one-third of transactions are discounted, signaling heavy reliance on promotions.
  2. Discounted orders show a statistically significant but practically small AOV lift.
  3. Online and In-Store channels contribute near-equal revenue.
  4. Discounts are applied unevenly across channels, indicating siloed promotions.
  5. Category drives AOV and revenue more than discounting.
  6. A small set of categories contributes the majority of revenue.
  7. Quantity is the dominant predictor of `total_spent` in regression modeling.
  8. Monthly revenue displays seasonal peaks aligned with major retail periods.
  9. Forecasting suggests stable baseline revenue over the next two quarters.
  10. Category and channel filters in Tableau make performance variances visible at a glance.

  ---

  ## 12. Recommendations

  1. **Optimize discount thresholds:** Replace flat discounts with spend thresholds (e.g., 10% off orders over $150) to grow basket size.
  2. **Reallocate marketing budget:** Concentrate spend on top-performing categories and audit low performers for rationalization.
  3. **Unify omnichannel promotions:** Standardize offers across Online and In-Store to stabilize margins and customer experience.

  ---

  ## 13. Limitations and Next Steps

  - **Data limitations:** Public dataset limits customer-level and margin data; no direct profitability measure.
  - **Method limitations:** Simple linear forecasting does not capture complex seasonal patterns.
  - **Suggested future work:** Add margin and inventory data, test advanced time-series models, and run promotion A/B tests.

  ---

  ## 14. Contribution Matrix

  - TBD (populate based on GitHub commits and PR history).
