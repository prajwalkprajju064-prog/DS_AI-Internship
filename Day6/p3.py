#statistical functions
import numpy as np
marks=np.array([[60,70,80],[70,80,90],[70,80,60]])
print("marks=",marks)
print(np.mean(marks))

print("shape:",marks.shape)
result=np.mean(marks,axis=1)

print("mean along rows:",result)
print("shape:",result.shape)


