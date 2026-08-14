import matplotlib.pyplot as plt

# First subplot (line plot)
plt.subplot(1,2,1)   # 1 row, 2 columns, first subplot
plt.plot([1,2,3],[1,4,9])
plt.title("Line Plot")

# Second subplot (bar chart)
plt.subplot(1,2,2)   # 1 row, 2 columns, second subplot
plt.bar(['A','B','C'],[3,7,5])
plt.title("Bar Chart")

# plt.tight_layout()   # Adjust spacing so titles don’t overlap
plt.show()
