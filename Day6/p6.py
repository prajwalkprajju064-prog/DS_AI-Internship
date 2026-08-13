import numpy as np

sales=np.array([[100,200,300],
                [400,500,600]
                [700,800,900]])

print("\n product wise sales: (axis=0) ")
print("mean:",np.mean(sales,axis=0))
print("median:",np.median(sales,axis=0))
print("std:",np.std(sales,axis=0))
print("var:",np.var(sales,axis=0))


print("\n month wise sales: (axis=1) ")
print("mean:",np.mean(sales,axis=1))
print("median:",np.median(sales,axis=1))
print("std:",np.std(sales,axis=1))
print("var:",np.var(sales,axis=1))
