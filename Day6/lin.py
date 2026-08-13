#linear algebra basics with numpy
import numpy as np
A=np.array([[1,2],
            [3,4]])
B=np.array([[5,6],
            [7,8]])
 

# print(np.transpose(A))
matmul = np.dot(A, B)   # or A @ B
print("Matrix Multiplication:\n", matmul)
print("Shape:", matmul.shape)

#elementwise
elementwise = A * B
print("Element-wise Multiplication:\n", elementwise)
print("Shape:", elementwise.shape)

#swap rows and columns and find matmul
swap_matmul = np.dot(B, A)
print("Swapped Matrix Multiplication:\n", swap_matmul)
print("Shape:", swap_matmul.shape)

