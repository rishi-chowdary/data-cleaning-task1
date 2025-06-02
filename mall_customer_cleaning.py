import pandas as pd
df = pd.read_csv("Mall_Customers.csv")
df.columns = [col.lower().replace(' ', '_') for col in df.columns]
if df.isnull().sum().any():
    df = df.fillna(method='ffill')
df = df.drop_duplicates()
df['gender'] = df['gender'].str.strip().str.capitalize()
df['age'] = df['age'].astype(int)
df['annual_income_(k$)'] = df['annual_income_(k$)'].astype(int)
df['spending_score_(1-100)'] = df['spending_score_(1-100)'].astype(int)
df.to_csv("cleaned_mall_customers.csv", index=False)
print("✅ Dataset cleaned and saved as 'cleaned_mall_customers.csv'")
