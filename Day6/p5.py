import numpy as np
marks=np.array([[60,70,80],[70,80,90],[70,80,60]])
print("marks=",marks)
print(np.median(marks))

print("shape:",marks.shape)

result=np.median(marks,axis=1)
print("median along rows:",result)
print("shape:",result.shape)
