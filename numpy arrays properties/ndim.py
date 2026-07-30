import numpy as np
ndim = np.array([[1,2,3],
                   [4,5,6],
                   [7,8,9],
                   [7,9,2]
                   ])
ndim1 = np.array([1,2,3])
ndim2 = np.array([[[1,2,3]]])
print(ndim.ndim)
print(ndim1.ndim)
print(ndim2.ndim)