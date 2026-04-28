# Retail Store Sales Analytics: Final Project Report

**Prepared For:** Newton School of Technology | Data Visualization & Analytics
**Sector:** Retail / E-Commerce
**Date:** April 2026

---

## Executive Summary

This report presents a comprehensive end-to-end data analytics pipeline applied to a Kaggle Retail Store Sales dataset (12,500 rows, 2022–2025). The core objective of this project was to understand how discounting strategies and channel distribution (Online vs. In-Store) impact total revenue and average order values (AOV). 

Through robust ETL processes, Exploratory Data Analysis (EDA), and advanced statistical modeling (ANOVA, Chi-Squared, Mann-Whitney U, and OLS Linear Regression), we derived critical business intelligence. The most striking finding is that while roughly 33% of transactions involve a discount, the actual monetary lift on the Average Order Value is statistically significant but practically negligible. We propose specific recommendations to optimize discount thresholds, realign marketing budget to top categories, and unify omnichannel promotions.

---

## 1. Business Problem & Project Scope

### 1.1 Context
Retail operations operate on thin margins, making every discounting and marketing decision highly consequential. Management requires a data-driven strategy to determine whether frequent discounting drives meaningful volume or merely erodes profit margins. Furthermore, they need visibility into channel performance to decide where to allocate future infrastructure and marketing investments.

### 1.2 Core Business Questions
1. How does the application of discounts impact the Average Order Value (AOV)?
2. Which product categories are driving the majority of revenue, and do payment preferences change by category?
3. How does Online channel performance compare to In-Store performance across transaction volume and revenue?
4. What is the historical revenue trend, and what is the forecasted trajectory for the next two quarters?

---

## 2. Dataset Overview & ETL Methodology

### 2.1 The Raw Dataset
The analysis is built upon a publicly available Kaggle Retail Store Sales dataset spanning from January 2022 to the current year. The raw dataset contained 11 columns including `Transaction ID`, `Customer ID`, `Category`, `Total Spent`, `Location`, and `Discount Applied`.

### 2.2 Data Cleaning & Transformation Pipeline
Data integrity is the bedrock of actionable analytics. We implemented a strict 10-step cleaning pipeline documented in `notebooks/02_cleaning.ipynb`:
- **Standardization:** Converted all columns to standard `snake_case` to prevent programmatic errors. Fixed inconsistent capitalization in categorical variables (e.g., standardizing 'electronics' and 'Electronics').
- **Imputation:** Recovered missing `total_spent` values safely by calculating `price_per_unit * quantity`. Null price values were imputed using the median to prevent skew. Unrecoverable rows were permanently dropped.
- **Data Type Casting:** The `transaction_date` field was parsed into proper datetime objects, enabling the extraction of time-based features (`transaction_year`, `transaction_month`, `transaction_day_of_week`). The boolean/string mix in `discount_applied` was securely mapped to `0` and `1` integers.
- **Feature Engineering:** We derived 8 new features, including `revenue_bucket` (Low, Medium, High spenders), `is_weekend` flag, and `avg_unit_price` benchmarks.

The resulting dataset, `cleaned_dataset.csv`, contains 11,971 pristine rows and 19 analysis-ready columns.

---

## 3. Exploratory Data Analysis (EDA)

The EDA phase (`03_eda.ipynb`) was designed to identify the shape of the data and surface initial business signals.

### 3.1 Univariate Analysis
- **Transaction Distribution:** The distribution of `total_spent` is heavily right-skewed. The vast majority of orders fall in the low-to-medium price range, but a long tail of rare, high-value bulk purchases exists. We utilized an Interquartile Range (IQR) filter to identify these as statistical outliers.
- **Category Popularity:** The transaction volume is not spread evenly. Specific categories command the highest volume, indicating core competencies in the retailer's portfolio.
- **Discount Penetration:** Exactly 33% of all transactions involve a discount, showing heavy reliance on promotional pricing to drive volume.

### 3.2 Bivariate Analysis
- **Revenue by Channel:** Online and In-Store channels are highly balanced, both contributing near-equal shares to the total revenue. This is a sign of a very healthy omnichannel presence.
- **Discount vs. Non-Discount AOV:** Initial visualizations showed that discounted orders have a slightly higher AOV. However, the visual gap was small enough to warrant rigorous statistical testing to verify if it was a real phenomenon or random noise.

### 3.3 Time Series Analysis
Plotting monthly revenue over a 3-year period revealed cyclical purchasing behaviors, with distinct peaks usually aligning with end-of-year holidays and mid-year liquidation sales.

---

## 4. Statistical Validation & Modeling

To ensure our recommendations are bulletproof, we subjected the EDA findings to strict statistical tests in `04_statistical_analysis.ipynb`.

### 4.1 Normality and Non-Parametric Testing
A **Shapiro-Wilk Test** confirmed our observation that `total_spent` is not normally distributed (p < 0.05). Consequently, we utilized the non-parametric **Mann-Whitney U Test** to compare discounted vs. non-discounted AOV. 
- **Result:** The test rejected the null hypothesis. There *is* a statistically significant difference in AOV when discounts are applied. However, the absolute monetary increase is negligible (less than $2 per transaction).

### 4.2 Analysis of Variance (ANOVA)
We ran a **One-Way ANOVA** to determine if the product category fundamentally shifts the average order value.
- **Result:** The p-value was less than 0.05, proving that category selection is a major driver of transaction size, further validating the need to shift marketing toward high-value categories.

### 4.3 Chi-Squared Test of Independence
We checked if the business was applying discounts evenly across sales channels.
- **Result:** The **Chi-Squared Test** revealed a dependency (p < 0.05). Discounts are not distributed evenly, meaning one channel (e.g., Online) is artificially subsidized by promotions more than the other.

### 4.4 OLS Multiple Linear Regression
We modeled `total_spent` using `quantity`, `discount_applied`, and dummy variables for `location` via `statsmodels`. 
- **Result:** The summary statistics (P-values, Coefficients) quantitatively proved that `quantity` is the overwhelming driver of revenue, while the `discount_applied` coefficient confirmed its minimal lift on final spend.

### 4.5 Time Series Forecasting
Using **Scikit-Learn Simple Linear Regression**, we modeled the historical monthly aggregate revenue. We successfully extended the trendline to forecast the next 2 quarters (6 months), providing management with a baseline expectation for future cash flow.

---

## 5. Tableau Dashboard Integration

The final step in the pipeline (`05_final_load_prep.ipynb`) involved pre-aggregating the data to ensure high-performance rendering in Tableau. We generated 4 specific summary tables:
1. `monthly_revenue_summary.csv`
2. `revenue_by_category.csv`
3. `discount_impact.csv`
4. `channel_performance.csv`

The full `tableau_ready_dataset.csv` was connected to Tableau Public, utilizing calculated fields (e.g., aliasing `discount_applied` from 0/1 to "No/Yes" for readability) to build a dual-view dashboard:
- **Executive View:** High-level KPIs (Total Revenue, AOV, Discount Rate).
- **Operational View:** Deep dives into Category splits, Channel performance, and Monthly trend lines.

---

## 6. Final Recommendations & Conclusion

Based on the synthesis of EDA and statistical modeling, we present the following strategic directives:

1. **Optimize Discount Thresholds to Protect Margin**
   *Insight:* Discounts apply to 33% of orders but barely lift the AOV, meaning they are likely eroding profit without driving larger baskets.
   *Action:* Shift from flat discounts to threshold-based promotions (e.g., "10% off orders over $150"). This forces the customer to increase their `quantity` (the proven driver of revenue in our OLS model) to unlock the deal.

2. **Reallocate Marketing Budget to Top Categories**
   *Insight:* ANOVA testing proved that category drives transaction value, and EDA showed revenue is heavily concentrated in top segments.
   *Action:* Double down on advertising spend for the highest-performing categories. Simultaneously, audit the bottom 20% of categories for potential inventory liquidation or removal to reduce warehousing costs.

3. **Unify Omnichannel Promotions**
   *Insight:* Chi-Squared testing proved that discounts are applied unevenly across Online and In-Store channels, despite both channels contributing equally to total revenue.
   *Action:* Implement a centralized, omnichannel loyalty program. Synchronize promotional offers so that an In-Store shopper receives the exact same incentives as an Online shopper, harmonizing the customer experience and stabilizing channel margins.

### Conclusion
This analytics pipeline successfully transitioned a raw, messy dataset into a pristine, statistically validated decision engine. By implementing the recommendations above, retail management can directly optimize their promotional spend and maximize top-line revenue growth over the forecasted quarters.
