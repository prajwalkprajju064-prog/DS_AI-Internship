import pandas as pd
import numpy as np
# x=[1, 2, 3, 4, 5]
# y=pd.Series(x)
# print(y)

#series from numpy array
x=np.array([1, 2, 3, 4, 5])
y=pd.Series(x)
print(y.to_string())