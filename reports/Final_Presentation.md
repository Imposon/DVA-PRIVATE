# Final Presentation

## Slide 1 - Title
- **Project Title:** Retail Store Sales Analytics: Driving Revenue Through Data
- **Sector:** Retail / E-Commerce
- **Team Name:** CS:GO
- **Team Members:** Aditya Sinha, Ansh Kumar, Ayush Kumar, Vedansha Srivastava, Shekhar Narayan Mishra
- **Institute:** Newton School of Technology
- **Faculty Mentor:** Vrushali Masane
- **Submission Date:** 28 April 2026

## Slide 2 - Context and Problem Statement
- **Sector Context:** Retail margins are increasingly thin; a data-driven understanding of discounting and channel investments is essential for survival.
- **Problem Statement:** Determine precisely how ongoing discounting strategies and omnichannel investments (Online vs. In-Store) impact total revenue and Average Order Value (AOV).
- **Core Objective:** Provide statistically validated, highly actionable recommendations to optimize marketing spend, refine promotional thresholds, and harmonize channel strategies.

## Slide 3 - Data Engineering
- **Source:** Kaggle Retail Store Sales Dataset
- **Structure & Size:** ~12,500 raw transactions spanning 2022–2025; 11 original columns.
- **ETL Methodology:** 
  - Standardized categorical text to `snake_case`.
  - Imputed missing pricing via category medians to prevent outlier skew.
  - Recalculated missing total spend using `price * quantity`.
- **Final Output:** 11,971 pristine rows with 19 analysis-ready engineered columns (e.g., `revenue_bucket`, `is_weekend`).

## Slide 4 - KPI Framework
- **Total Revenue:** Sum of all cart values; tracks top-line scale.
- **Average Order Value (AOV):** Revenue per cart; measures customer value.
- **Discount Rate:** Percentage of transactions discounted; tracks reliance on promotions.
- **Channel Revenue Share:** Online vs. In-Store revenue distribution; measures omnichannel health.

## Slide 5 - Key EDA Insights
- **Promotional Reliance:** 33% of all global transactions utilize a discount.
- **Spend Distribution:** `total_spent` is heavily right-skewed; revenue depends on rare, high-value bulk purchases.
- **Category Pareto:** Revenue is heavily concentrated; top categories dominate, while the bottom 20% act as inventory dead-weight.
- **Omnichannel Balance:** Online and In-Store revenues are nearly equal, indicating a robust, diversified sales structure.

## Slide 6 - Advanced Analysis
- **Mann-Whitney U Test:** Discounted orders show a statistically significant AOV lift, but the actual monetary increase is <$2 (negligible).
- **One-Way ANOVA:** Product category significantly drives transaction value (p < 0.05).
- **Chi-Squared Test:** Discounts are applied unevenly across Online and In-Store channels (p < 0.05).
- **OLS Linear Regression:** Transaction quantity is the overwhelming predictor of `total_spent`; the discount coefficient is minimal.

## Slide 7 - Dashboard Overview
- **Executive View:** High-level KPI scorecards (Total Revenue, AOV, Discount Rate) and longitudinal time-series forecasting.
- **Operational View:** Dual-axis charts comparing channel performance and category matrices for rapid localized decisions.
- **Interactivity:** Global filters for Category, Channel, Time Period, and Discount Flag.
- *(Insert Dashboard Screenshots Here)*

## Slide 8 - Top Insights
- The business gives away margin on 33% of transactions for a negligible AOV lift (<$2).
- Category mix structurally dictates high-value transactions, not just promotional deals.
- Despite equal channel revenue, promotional strategies are dangerously siloed.
- Transaction `quantity` is the ultimate lever for maximizing top-line revenue.
- Reliable cyclical purchasing peaks align perfectly with major retail holidays.

## Slide 9 - Recommendations
1. **Optimize Discount Thresholds:** Cease flat discounts; implement threshold triggers (e.g., "Spend $150 to unlock 10%") to force an increase in quantity.
2. **Reallocate Marketing Budget:** Shift ad spend heavily to top-performing categories and liquidate bottom-tier inventory.
3. **Unify Omnichannel Promotions:** Deploy a centralized loyalty program so Online and In-Store promotions are perfectly synchronized.

## Slide 10 - Impact
- **Expected Outcome:** Higher global AOV, protected baseline profit margins, and optimized ROAS on marketing spend.
- **Priority & Feasibility:** Modifying digital discount thresholds is a high-priority, highly feasible initiative requiring minimal immediate capital expenditure.

## Slide 11 - Limitations
- **Data Constraints:** Complete absence of direct Cost of Goods Sold (COGS) data prevents exact net profit margin modeling.
- **Modeling Constraints:** Simple forecasting algorithms do not fully account for sudden macroeconomic inflationary shifts.

## Slide 12 - Next Steps
- **Future Data Ingestion:** Acquire granular inventory costs to calculate Net Profitability.
- **Advanced Modeling:** Transition to robust, season-aware time-series algorithms (Prophet/ARIMA).
- **Market Basket Analysis:** Deploy Apriori to automate high-margin cross-selling on the checkout page.

## Slide 13 - Contribution Matrix
| Team Member | Dataset & Sourcing | ETL & Cleaning | EDA & Analysis | Statistical Analysis | Tableau Dashboard | Report Writing | PPT & Viva |
|---|---|---|---|---|---|---|---|
| Ansh Kumar | | Worked on | Assisted | Worked on | Assisted | Worked on | |
| Aditya Sinha | Worked on | Assisted | Worked on | Worked on | Worked on | Assisted | |
| Ayush Kumar | Worked on | Worked on | Worked on | | | | Assisted |
| Shekhar Narayan Mishra | | Worked on | Worked on | | | | Worked on |
| Vedansha Srivastava | | | Worked on | | | | Worked on |
