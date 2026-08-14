import pandas as pd
import numpy as np

# Step 1: Load dataset from CSV
data = pd.read_csv("sudent_marks.csv")
print("Original Dataset:\n", data.head())

# Step 2: Shape of dataset
print("\nOriginal Shape:", data.shape)

# Step 3: Identify missing values
print("\nMissing values per column:")
print(data.isnull().sum())

print("\nTotal missing values:", data.isnull().sum().sum())

# Step 4: Detect & remove duplicates
print("\nDuplicate Rows:", data.duplicated().sum())

data = data.drop_duplicates()
print("Shape after removing duplicates:", data.shape)

# Step 5: Handle missing values (fill with column mean)
data = data.fillna(data.mean(numeric_only=True))

# Step 6: Final cleaned dataset shape
print("\nFinal Cleaned Shape:", data.shape)

# Step
print(data)

# Step 7: Describe the dataset
print("\nDataset Description:\n")
print(data.describe())
data.info()


