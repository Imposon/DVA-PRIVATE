# Data Dictionary: Retail Store Sales

This data dictionary outlines the 19 columns present in the finalized, Tableau-ready dataset (`data/processed/cleaned_dataset.csv` or `tableau_ready_dataset.csv`).

| Column Name | Data Type | Description | Role in Analysis |
|---|---|---|---|
| `transaction_id` | String | Unique identifier for each transaction | Primary key |
| `customer_id` | String | Unique identifier for the customer | Useful for tracking repeat customers |
| `category` | String | Product category (e.g., Electronics, Clothing) | Primary dimension for segmenting revenue |
| `item` | String | Specific product name/item purchased | Granular product analysis |
| `price_per_unit` | Float | Cost of a single unit of the item | Helps determine average pricing |
| `quantity` | Integer | Number of units purchased in the transaction | Volume driver |
| `total_spent` | Float | Total transaction amount (`price_per_unit` * `quantity`) | Primary measure for revenue and AOV |
| `payment_method` | String | Method used for payment (e.g., Credit Card, Cash) | Dimension for checkout preferences |
| `location` | String | Where the sale occurred (Online vs In-Store) | Channel performance dimension |
| `transaction_date` | Date/Time | The raw date of the transaction | Base for time-series extraction |
| `discount_applied` | Integer | Whether a discount was given (1 = Yes, 0 = No) | Evaluates the business impact of discounting |
| `transaction_year` | Integer | The year extracted from `transaction_date` | High-level temporal dimension |
| `transaction_month` | Integer | The month extracted from `transaction_date` | Seasonal trend dimension |
| `transaction_day_of_week` | String | Day of the week (e.g., Monday, Tuesday) | Operational traffic analysis |
| `transaction_quarter` | Integer | The quarter of the year (1-4) | Quarterly financial reporting |
| `is_weekend` | Integer | Boolean flag indicating if the transaction occurred on a weekend (1 = Yes, 0 = No) | Traffic comparison |
| `revenue_bucket` | String | Categorization of the spend amount (Low, Medium, High) | Customer segmentation |
| `is_high_value` | Integer | Flag indicating if `total_spent` is exceptionally high (1 = Yes, 0 = No) | VIP order identification |
| `avg_unit_price` | Float | Global average price for the given product category | Relative price analysis |
