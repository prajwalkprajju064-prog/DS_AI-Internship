# ==========================================================
# EXPLORATORY DATA ANALYSIS (EDA)
# Employee Salary Dataset
# ==========================================================

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Improve plot appearance
sns.set(style="whitegrid")

# ==========================================================
# 1. LOAD DATASET
# ==========================================================

df = pd.read_csv("Day9/salary_emp.csv")

print("Dataset loaded successfully!")


# ==========================================================
# 2. BASIC DATA INSPECTION
# ==========================================================

# First 5 rows
print("\n===== FIRST 5 ROWS =====")
print(df.head())

# Last 5 rows
print("\n===== LAST 5 ROWS =====")
print(df.tail())

# Dataset shape
print("\n===== DATASET SHAPE =====")
print("Rows and Columns:", df.shape)

# Column names
print("\n===== COLUMN NAMES =====")
print(df.columns.tolist())

# Dataset information
print("\n===== DATASET INFO =====")
df.info()


# ==========================================================
# 3. MISSING VALUES
# ==========================================================

print("\n===== MISSING VALUES =====")
print(df.isnull().sum())

# Total missing values
print("\nTotal missing values:", df.isnull().sum().sum())


# ==========================================================
# 4. DUPLICATE ROWS
# ==========================================================

print("\n===== DUPLICATE ROWS =====")
print("Number of duplicate rows:", df.duplicated().sum())


# ==========================================================
# 5. UNIQUE VALUES
# ==========================================================

print("\n===== UNIQUE VALUES =====")
print(df.nunique())


# ==========================================================
# 6. SUMMARY STATISTICS
# ==========================================================

print("\n===== SUMMARY STATISTICS =====")
print(df.describe())


# ==========================================================
# 7. DATA TYPES
# ==========================================================

print("\n===== DATA TYPES =====")
print(df.dtypes)


# ==========================================================
# 8. HISTOGRAM - AGE DISTRIBUTION
# ==========================================================

plt.figure(figsize=(8, 5))

sns.histplot(
    df["Age"],
    kde=True
)

plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()


# ==========================================================
# 9. HISTOGRAM - SALARY DISTRIBUTION
# ==========================================================

plt.figure(figsize=(8, 5))

sns.histplot(
    df["Salary"],
    kde=True
)

plt.title("Salary Distribution")
plt.xlabel("Salary")
plt.ylabel("Frequency")
plt.show()


# ==========================================================
# 10. BOXPLOT - SALARY OUTLIERS
# ==========================================================

plt.figure(figsize=(8, 4))

sns.boxplot(
    x=df["Salary"]
)

plt.title("Salary Boxplot")
plt.xlabel("Salary")
plt.show()


# ==========================================================
# 11. DEPARTMENT FREQUENCY
# ==========================================================

print("\n===== DEPARTMENT COUNTS =====")
print(df["Department"].value_counts())


# ==========================================================
# 12. GENDER FREQUENCY
# ==========================================================

print("\n===== GENDER COUNTS =====")
print(df["Gender"].value_counts())


# ==========================================================
# 13. COUNT PLOT - DEPARTMENT
# ==========================================================

plt.figure(figsize=(8, 5))

sns.countplot(
    x="Department",
    data=df
)

plt.title("Department Distribution")
plt.xlabel("Department")
plt.ylabel("Number of Employees")
plt.xticks(rotation=45)
plt.show()


# ==========================================================
# 14. COUNT PLOT - GENDER
# ==========================================================

plt.figure(figsize=(6, 5))

sns.countplot(
    x="Gender",
    data=df
)

plt.title("Gender Distribution")
plt.xlabel("Gender")
plt.ylabel("Number of Employees")
plt.show()


# ==========================================================
# 15. SCATTER PLOT - AGE VS SALARY
# ==========================================================

plt.figure(figsize=(8, 5))

sns.scatterplot(
    x="Age",
    y="Salary",
    data=df
)

plt.title("Age vs Salary")
plt.xlabel("Age")
plt.ylabel("Salary")
plt.show()


# ==========================================================
# 16. SCATTER PLOT - EXPERIENCE VS SALARY
# ==========================================================

plt.figure(figsize=(8, 5))

sns.scatterplot(
    x="Experience",
    y="Salary",
    data=df
)

plt.title("Experience vs Salary")
plt.xlabel("Experience")
plt.ylabel("Salary")
plt.show()


# ==========================================================
# 17. BOXPLOT - SALARY BY GENDER
# ==========================================================

plt.figure(figsize=(7, 5))

sns.boxplot(
    x="Gender",
    y="Salary",
    data=df
)

plt.title("Salary by Gender")
plt.xlabel("Gender")
plt.ylabel("Salary")
plt.show()


# ==========================================================
# 18. BOXPLOT - SALARY BY DEPARTMENT
# ==========================================================

plt.figure(figsize=(10, 5))

sns.boxplot(
    x="Department",
    y="Salary",
    data=df
)

plt.title("Salary by Department")
plt.xlabel("Department")
plt.ylabel("Salary")
plt.xticks(rotation=45)
plt.show()


# ==========================================================
# 19. CORRELATION ANALYSIS
# ==========================================================

# Correlation matrix for numerical columns
corr_matrix = df.corr(numeric_only=True)

print("\n===== CORRELATION MATRIX =====")
print(corr_matrix)


# ==========================================================
# 20. CORRELATION HEATMAP
# ==========================================================

plt.figure(figsize=(8, 6))

sns.heatmap(
    corr_matrix,
    annot=True,
    cmap="coolwarm",
    fmt=".2f"
)

plt.title("Correlation Heatmap")
plt.show()


# ==========================================================
# 21. BOXPLOT - AGE OUTLIERS
# ==========================================================

plt.figure(figsize=(8, 4))

sns.boxplot(
    x=df["Age"]
)

plt.title("Age Outliers")
plt.xlabel("Age")
plt.show()


# ==========================================================
# 22. BOXPLOT - EXPERIENCE OUTLIERS
# ==========================================================

plt.figure(figsize=(8, 4))

sns.boxplot(
    x=df["Experience"]
)

plt.title("Experience Outliers")
plt.xlabel("Experience")
plt.show()


# ==========================================================
# 23. OUTLIER DETECTION USING IQR
# ==========================================================

def detect_outliers(column):

    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)

    IQR = Q3 - Q1

    lower_limit = Q1 - 1.5 * IQR
    upper_limit = Q3 + 1.5 * IQR

    outliers = df[
        (df[column] < lower_limit) |
        (df[column] > upper_limit)
    ]

    print(f"\n===== OUTLIERS IN {column} =====")
    print("Q1:", Q1)
    print("Q3:", Q3)
    print("IQR:", IQR)
    print("Lower Limit:", lower_limit)
    print("Upper Limit:", upper_limit)
    print("Number of Outliers:", len(outliers))

    if len(outliers) > 0:
        print(outliers[[column]])


detect_outliers("Age")
detect_outliers("Experience")
detect_outliers("Salary")


# ==========================================================
# 24. AVERAGE SALARY BY DEPARTMENT
# ==========================================================

print("\n===== AVERAGE SALARY BY DEPARTMENT =====")

department_salary = df.groupby(
    "Department"
)["Salary"].mean().sort_values(ascending=False)

print(department_salary)


# ==========================================================
# 25. AVERAGE SALARY BY GENDER
# ==========================================================

print("\n===== AVERAGE SALARY BY GENDER =====")

gender_salary = df.groupby(
    "Gender"
)["Salary"].mean().sort_values(ascending=False)

print(gender_salary)


# ==========================================================
# 26. AVERAGE SALARY BY EXPERIENCE
# ==========================================================

print("\n===== AVERAGE SALARY BY EXPERIENCE =====")

experience_salary = df.groupby(
    "Experience"
)["Salary"].mean()

print(experience_salary)


# ==========================================================
# 27. HIGHEST PAID EMPLOYEE
# ==========================================================

print("\n===== HIGHEST PAID EMPLOYEE =====")

highest_salary = df.loc[
    df["Salary"].idxmax()
]

print(highest_salary)


# ==========================================================
# 28. LOWEST PAID EMPLOYEE
# ==========================================================

print("\n===== LOWEST PAID EMPLOYEE =====")

lowest_salary = df.loc[
    df["Salary"].idxmin()
]

print(lowest_salary)


# ==========================================================
# 29. FINAL EDA INSIGHTS
# ==========================================================

print("\n")
print("=" * 60)
print("              FINAL EDA INSIGHTS")
print("=" * 60)

print("\n1. Dataset contains", df.shape[0], "rows and", df.shape[1], "columns.")

print(
    "\n2. Total missing values:",
    df.isnull().sum().sum()
)

print(
    "3. Total duplicate rows:",
    df.duplicated().sum()
)

print(
    "\n4. Average Age:",
    round(df["Age"].mean(), 2)
)

print(
    "5. Average Experience:",
    round(df["Experience"].mean(), 2)
)

print(
    "6. Average Salary:",
    round(df["Salary"].mean(), 2)
)

print(
    "\n7. Highest Salary:",
    df["Salary"].max()
)

print(
    "8. Lowest Salary:",
    df["Salary"].min()
)

print(
    "\n9. Department with highest average salary:",
    department_salary.index[0]
)

print(
    "10. Gender with highest average salary:",
    gender_salary.index[0]
)

print(
    "\n11. Correlation between Experience and Salary:",
    round(df["Experience"].corr(df["Salary"]), 2)
)

print(
    "12. Correlation between Age and Salary:",
    round(df["Age"].corr(df["Salary"]), 2)
)

print("\n===== EDA COMPLETED SUCCESSFULLY =====")