import matplotlib.pyplot as plt
import numpy as np

t = np.linspace(0, 2*np.pi)
x = np.cos(t)
y = np.sin(t)

plt.plot(x, y)
plt.gca().set_aspect('equal')
plt.show()