import pandas as pd

# Step 1: Load dataset
df = pd.read_csv("Mall_Customers.csv")

# Step 2: Rename columns (lowercase, underscores)
df.columns = [col.lower().replace(' ', '_') for col in df.columns]

# Step 3: Check & handle missing values
if df.isnull().sum().any():
    df = df.fillna(method='ffill')  # or use dropna() if more appropriate

# Step 4: Remove duplicates
df = df.drop_duplicates()

# Step 5: Standardize 'gender'
df['gender'] = df['gender'].str.strip().str.capitalize()

# Step 6: Fix data types
df['age'] = df['age'].astype(int)
df['annual_income_(k$)'] = df['annual_income_(k$)'].astype(int)
df['spending_score_(1-100)'] = df['spending_score_(1-100)'].astype(int)

# Step 7: Save cleaned dataset
df.to_csv("cleaned_mall_customers.csv", index=False)
print("✅ Dataset cleaned and saved as 'cleaned_mall_customers.csv'")
