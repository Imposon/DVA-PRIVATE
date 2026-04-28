# Final Presentation

## Slide 1 - Title

- **Project title:** Retail Store Sales Analytics: Driving Revenue Through Data
- **Sector:** Retail / E-Commerce
- **Team ID:** TBD
- **Team members:** TBD
- **Faculty mentor:** TBD

## Slide 2 - Context and Problem Statement

- **Sector context:** Retail margins are thin; pricing and channel decisions must be precise.
- **Stakeholder:** Retail leadership for pricing, category, and channel strategy.
- **Core business question:** How do discounts and channel choices (Online vs. In-Store) impact total revenue and Average Order Value (AOV)?
- **Objective:** Deliver data-backed guidance for promotions and channel investment.

## Slide 3 - Data Engineering

- **Source:** Kaggle Retail Store Sales (2022–2025, ~12k rows)
- **Size and coverage:** 11,971 cleaned rows, 19 columns after feature engineering
- **Major cleaning steps:** Standardized labels, imputed pricing, engineered time and revenue features
- **Data dictionary summary:** Key fields include `total_spent`, `quantity`, `category`, `location`, `discount_applied`, `transaction_date`

## Slide 4 - KPI Framework

- **KPI definitions:** Total Revenue, AOV, Discount Rate, Channel Revenue Share
- **Why they matter:** Measure revenue health, promotional dependency, and channel balance

## Slide 5 - Key EDA Insights

- 33% of all transactions involve a discount.
- The distribution of `total_spent` is right-skewed with rare high-value purchases.
- Revenue is highly concentrated in specific core product categories.
- Online and In-Store channels generate roughly equal total revenue.
- Seasonal purchasing behaviors peak around holidays and mid-year sales.

## Slide 6 - Advanced Analysis

- **Statistical method:** Mann-Whitney U, ANOVA, Chi-Squared, OLS regression
- **Findings:** Category and quantity drive revenue; discount effect is minimal; discounting varies by channel

## Slide 7 - Dashboard Overview

- **Executive view:** High-level metrics tracking Total Revenue, AOV, and Discount Rate over time.
- **Operational view:** Deep dives into category revenue splits and channel performance differences.
- **Filters and drilldowns:** Category, channel, period, discount flag

## Slide 8 - Top Insights

- Discounting is common but yields negligible AOV lift.
- Category mix explains most variation in revenue.
- Channel performance is balanced, but promotions are uneven.
- Quantity is the strongest driver of `total_spent`.

## Slide 9 - Recommendations

- **Optimize Discount Thresholds:** Switch to threshold triggers (e.g., "Spend $150 to unlock 10%") to increase quantity and protect margins.
- **Reallocate Marketing Budget:** Shift ad spend heavily toward top-performing categories and liquidate bottom-tier inventory.
- **Unify Omnichannel Promotions:** Deploy a centralized loyalty program to align Online and In-Store promotions.

## Slide 10 - Impact

- **Expected outcome:** Higher basket size, protected margins, and clearer channel ROI.
- **Priority and feasibility:** High priority; feasible with pricing rules and coordinated marketing.

## Slide 11 - Limitations

- **Data or method constraints:** No margin data for profitability impact; public dataset limits customer-level context; simple forecasting omits complex seasonality.

## Slide 12 - Next Steps

- **Future extensions:** Add margin and inventory data, test advanced time-series models, run A/B tests on threshold-based promotions.
- **Closing summary:** Align discounts, category focus, and channel strategy to protect margins and grow revenue.
