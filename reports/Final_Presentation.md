# Presentation Outline: Retail Store Sales Analytics

**Slide 1: Title Slide**
- **Title:** Retail Store Sales Analytics: Driving Revenue through Data
- **Subtitle:** Newton School of Technology | Capstone Project 2
- **Team Names:** Rahul, Priya, Ankit, Sneha, Arjun

---

**Slide 2: The Business Problem**
- **Context:** Retail margins are thin; promotional strategies and channel investments must be precise.
- **Core Question:** How do discounts and channel choices (Online vs. In-Store) impact total revenue and Average Order Value (AOV)?
- **Goal:** Provide data-backed recommendations to optimize marketing spend and promotional thresholds.

---

**Slide 3: Data Architecture & ETL**
- **Dataset:** Kaggle Retail Store Sales (2022–2025, ~12,000 rows).
- **The Pipeline:** 10-step automated cleaning process built in Python.
- **Transformations:** 
  - Standardized column names to `snake_case`.
  - Imputed missing pricing data via median mapping.
  - Engineered 8 new features including `revenue_bucket` and time-series variables.
- **Result:** A pristine 19-column dataset ready for Tableau.

---

**Slide 4: Key Insight 1 - The Reality of Discounts**
- **Visual Suggestion:** Show the Pie Chart (33% discount usage) next to the Bar Chart comparing AOV.
- **The Finding:** 1 in 3 transactions uses a discount.
- **The Catch:** Discounted orders only show a negligible increase in Average Order Value.
- **Statistical Proof:** Mann-Whitney U Test confirms the difference is statistically real, but practically insignificant. We are giving away margin for free.

---

**Slide 5: Key Insight 2 - Category Concentration**
- **Visual Suggestion:** Horizontal Bar Chart of Revenue by Category.
- **The Finding:** Revenue is highly concentrated at the top. 
- **Statistical Proof:** One-Way ANOVA testing proves that product category fundamentally drives the transaction value.
- **Takeaway:** Not all products are created equal; marketing spend should reflect this asymmetry.

---

**Slide 6: Key Insight 3 - Omnichannel Discrepancy**
- **Visual Suggestion:** Side-by-side Bar Chart (Online vs In-Store Revenue).
- **The Finding:** Both channels generate roughly equal revenue, indicating a healthy business.
- **The Catch:** Chi-Squared testing reveals discounts are applied unevenly across the two channels.
- **Takeaway:** Promotional strategies are siloed and need synchronization.

---

**Slide 7: Forecasting the Future**
- **Visual Suggestion:** Time-Series Line Chart showing historical peaks and the forecasted trend line.
- **The Methodology:** Scikit-Learn Simple Linear Regression on monthly aggregates.
- **The Forecast:** Projected revenue trajectory for the next 2 quarters (6 months), providing management with baseline cash flow expectations.

---

**Slide 8: Executive Recommendations**
1. **Optimize Discount Thresholds:** Switch from flat discounts to threshold triggers (e.g., "Spend $150 to unlock 10%") to force an increase in cart size and protect margins.
2. **Reallocate Marketing Budget:** Shift ad spend heavily toward the top-performing categories identified in the ANOVA test. Liquidate bottom-tier inventory.
3. **Unify Omnichannel Promotions:** Deploy a centralized loyalty program to ensure Online and In-Store shoppers receive the same promotional experience, fixing the Chi-Squared discrepancy.

---

**Slide 9: Q&A**
- Thank you!
- Open the floor for questions regarding the ETL pipeline, statistical methodologies, or Tableau dashboard architecture.
