import pandas as pd

# Create a Pandas Series of student marks with subject names as labels
marks = pd.Series([85, 72, 58, 91, 67], 
                  index=["Math", "Science", "English", "History", "Computer"])

# Access values using positions (use .iloc)
print("By position (0th element):", marks.iloc[0])   # Math → 85
print("By position (2nd element):", marks.iloc[2])   # English → 58

# Access values using labels
print("By label (Science):", marks["Science"])       # 72
print("By label (History):", marks.loc["History"])   # 91

# Print values and index
print("\nValues:", marks.values)   # [85 72 58 91 67]
print("Index:", marks.index)       # Index(['Math','Science','English','History','Computer'])

# Filter students who scored above 60 using boolean masking
print("\nStudents scoring above 60:\n", marks[marks > 60])
