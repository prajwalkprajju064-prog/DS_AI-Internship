#adding matrix in numpy
import numpy as np
x=np.array([[2,3,4],
            [4,6,8],
            [5,8,6]])
y=np.array([2,1,1])
result=x+y.reshape(-1,1)
print(result)
