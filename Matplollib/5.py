import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = plt.axes(projection='3d')
t = np.linspace(0, 20*np.pi, 1000)

x = np.cos(t)
y = np.sin(t)
z = 2*t

plt.plot(x, y, z)
plt.show()
