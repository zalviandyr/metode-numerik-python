# reference url = "https://stackoverflow.com/questions/45873783/python-linprog-minimization-simplex-method"

import numpy as np
from scipy.optimize import linprog

# A = np.array([[-1, -1, -1], [-1,2, 0], [0, 0, -1], [-1, 0, 0], [0, -1, 0]])
# b = np.array([-1000, 0, -340, 0, 0])
# c = np.array([10,15,25])

A = np.array([[2, 0], [0, 3], [6, 5]])
b = np.array([-8, -15, -30])
c = np.array([3, 5])


res = linprog(c, A_ub=A, b_ub=b,bounds=(0, None))

print('Optimal value:', res.fun, '\nX:', res.x)
# ('Optimal value:', 15100.0, '\nX:', array([ 660.,    0.,  340.]))