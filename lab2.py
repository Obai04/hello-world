import pandas as pd

# 1. Load the dataset
df = pd.read_csv(r'C:\Users\User\Downloads\faults.csv')

# 2. Display its shape
print(f"Dataset Shape: {df.shape}")

# 3. Preview the first few rows
print(df.head())

# 4. Check column names and data types
print(df.info())
