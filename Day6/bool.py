import pandas as pd

# scores =pd.Series([76, 76, 98,76,65])
# passed=scores[scores>75]
# print("these students are passed",passed)

#handling missing data in series
# data=pd.Series([10,None,20,None,30])
# print(data.isnull())
# print(data.fillna(0))




#vectorized String operations
names=pd.Series(["Alice","Bob","Charlie"])
print(names.str.lower())
print(names.str.contains("a"))