import numpy as np
a = np.array([[1,0,0],[1,1,0],[1,3,6]])
b = np.array([1,3,1])

x = np.linalg.solve(a,b)
print(x)