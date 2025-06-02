# Data Analyst Internship - Task 1: Data Cleaning and Preprocessing
## Dataset
**Mall Customer Segmentation Data**  
Source: Kaggle
## Tools Used
- Python
- Pandas
## Cleaning Steps
1. **Loaded dataset** using `pandas.read_csv`.
2. **Renamed columns** to lowercase and underscores for consistency.
3. **Handled missing values** (none found).
4. **Removed duplicates** using `.drop_duplicates()`.
5. **Standardized 'Gender' column** by formatting case and spacing.
6. **Corrected data types**:
   - Age, Income, and Spending Score → `int`
7. **Saved final cleaned dataset** as `cleaned_mall_customers.csv`.
## Files in This Repository
- `mall_customer_cleaning.py` – Data cleaning script
- `cleaned_mall_customers.csv` – Final cleaned dataset
- `README.md` – Task summary
## Outcome
The dataset is now clean, structured, and ready for analysis or machine learning tasks.
