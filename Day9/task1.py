# Import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset (Titanic example)
df = sns.load_dataset("titanic")

# -------------------------------
# 1. Basic Exploration
# -------------------------------
print("Shape:", df.shape)
print("\nData Types:\n", df.dtypes)
print("\nMissing Values:\n", df.isnull().sum())
print("\nSummary Statistics:\n", df.describe(include="all"))

# -------------------------------
# 2. Univariate Analysis
# -------------------------------
# Numerical variable distribution
plt.figure(figsize=(6,4))
sns.histplot(df["age"].dropna(), kde=True, bins=30)
plt.title("Age Distribution")
plt.show()

# Categorical variable distribution
plt.figure(figsize=(6,4))
sns.countplot(x="sex", data=df)
plt.title("Gender Distribution")
plt.show()

# -------------------------------
# 3. Bivariate Analysis
# -------------------------------
plt.figure(figsize=(6,4))
sns.barplot(x="sex", y="survived", data=df)
plt.title("Survival Rate by Gender")
plt.show()

plt.figure(figsize=(6,4))
sns.boxplot(x="class", y="age", data=df)
plt.title("Age Distribution by Class")
plt.show()

# -------------------------------
# 4. Skewness Analysis
# -------------------------------
print("\nSkewness:\n", df.skew(numeric_only=True))

# -------------------------------
# 5. Correlation Analysis
# -------------------------------
plt.figure(figsize=(10,6))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()

# -------------------------------
# 6. Outlier Detection
# -------------------------------
plt.figure(figsize=(6,4))
sns.boxplot(x=df["fare"])
plt.title("Outlier Detection in Fare")
plt.show()

# -------------------------------
# 7. Pattern Identification
# -------------------------------
# Example: Survival by class and gender
plt.figure(figsize=(8,6))
sns.catplot(x="class", hue="sex", col="survived", kind="count", data=df)
plt.suptitle("Survival Patterns by Class & Gender", y=1.05)
plt.show()