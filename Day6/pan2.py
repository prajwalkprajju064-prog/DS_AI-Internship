import pandas as pd
import numpy as np
x={"math":80,"science":90,"english":70}
y=pd.Series(x)

print(y.to_string())
print(y[y>80])


# marks=[76,76,98]
# z=pd.Series(marks,index=["math","science","english"])
# print(z.to_string())
# print(z.to_list())

