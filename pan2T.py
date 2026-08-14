import pandas as pd
import numpy as np

# Create a Pandas Series with names (mixed cases + missing values)
names = pd.Series(["Alice", "BOB", None, "ChArLiE", np.nan, "Diana"])

print("Original Series:\n", names)

# Detect missing values
print("\nMissing values:\n", names.isna())

# Fill missing values (replace with "Unknown")
names_filled = names.fillna("Unknown")

print("\nAfter filling missing values:\n", names_filled)

# Convert all names to lowercase using .str.lower()
names_lower = names_filled.str.lower()
print("\nNames in lowercase:\n", names_lower)

# Filter names containing the letter 'a'
filtered_names = names_lower[names_lower.str.contains("a")]
print("\nNames containing 'a':\n", filtered_names)
