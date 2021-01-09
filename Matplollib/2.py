import matplotlib.pyplot as plt
import numpy as np

t = np.linspace(0, 2*np.pi)
x = 30*np.cos(t)
y = 15*np.sin(t)

plt.plot(x, y)
plt.gca().set_aspect('equal')
plt.show()
