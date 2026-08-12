import numpy as np
#import transpose as tr
x=np.array([[2,1,1],
           [2,1,3]])
flattened=x.flatten()
print("flatten=",flattened)

#reshape
x=np.array([[2,1,1],
           [2,1,3]])
reshaped=x.reshape(3,2)
print("reshape=",reshaped)

#tarnspose of a matrix

transposed=x.transpose()
print("transpose=",transposed)

#cocatitane means adding the given value
y=np.array([[2,3,4]])
concantenate=np.concatenate((x,y), axis=0)
print("concatenate=",concantenate)

#vstack
result = np.vstack((x, y))
print("vstack =", result)