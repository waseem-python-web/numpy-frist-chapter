# it is used to convert data tupes to data types
import numpy as np
ndim = np.array([[1,2,3],
                   [4,5,6],
                   [7,8,9],
                   [7,9,2]
                   ])
ints = ndim.astype(float)
print(ints.dtype)
print(ints)

ndim1 = np.array([1.2,2.5,3.9])

ints = ndim1.astype(int)
print(ints.dtype)
print(ints)


ndim2 = np.array([[[1,2,3]]])
ints = ndim2.astype(str)

print(ints.dtype)
print(ints)
