#step-1  import pandas  
import pandas as pd

#step 2 create messy dataset
data = {
    "customer_id": [101, 102, 103, 104, 105, 106, 107, 108, 109],
    "name": ["Alice", "Bob", "Charlie", "David", "Eva", "Frank", "Grace", "Hannah", "Ian"],
    "age": [25, 30, 35, 40, 28, 32, 29, 31, 27],
    "city": ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix", "Philadelphia", "San Antonio", "San Diego", "Dallas"],
    "order_amount": [250.75, 180.50, 320.00, 150.25, 275.00, 400.00, 220.50, 310.75, 190.00],
    "payment_method": ["Credit Card", "PayPal", "Credit Card", "Debit Card", "PayPal", "Credit Card", "Debit Card", "PayPal", "Credit Card"],
    "order_date": ["2023-01-15", "2023-02-20", "2023-03-10", "2023-04-05", "2023-05-12", "2023-06-18", "2023-07-22", "2023-08-30", "2023-09-14"]}
df = pd.DataFrame(data)

#step 3 inspect the dataset
print("first row:\n", df.head())
print("\nDataset info:")
print(df.info())

#step 4 check for missing values
print("\nMissing values per column:")
print(df.isna().sum())

#step 5 filling missing values(statistical imputation)
df["age"] = df["age"].fillna(df["age"].mean())
df["order_amount"] = df["order_amount"].fillna(df["order_amount"].mean())
df["city"]=df["city"].fillna(df["city"].mode()[0])
df["payment_method"]=df["payment_method"].fillna(df["payment_method"].mode()[0])
df["name"]=df["name"].fillna("Unknown")


#step 6- check data types and convert if necessary
print("\nData types BEFORE conversion:")
print(df.dtypes)

#STEP 7- convert data types
df["age"] = df["age"].astype(int)
df["order_date"] = pd.to_datetime(df["order_date"])

print("\nData types AFTER conversion:")
print(df.dtypes)

#NEW PART STRING CLEANING
df["City"]=df["city"].str.strip()
df["City"]=df["city"].str.lower()
print("\nCleaned City column:\n", df["City"])

#NEW PART-DUPLICATE HANDLING
# Check for duplicates
print("\n number of duplicate rows:", df.duplicated().sum())

print(df.describe())