import numpy as np
a=np.array([[1,2,3],
            [4,5,6],
            [7,8,9]])
b=np.array([[7,8,9],
            [10,11,12],
            [13,14,15]])
matmul= np.dot(a,b)   # or a @ b
print("Matrix Multiplication:\n", matmul)