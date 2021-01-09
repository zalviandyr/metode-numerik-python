import matplotlib.pyplot as plt
import numpy as np

a = int(input("a = "))
b = int(input("b = "))

t = np.linspace(0, 8*np.pi, 1000)
x = (a-b)*np.cos(t) + b*np.cos(t*(a/b - 1))
y = (a-b)*np.sin(t) - b*np.sin(t*(a/b - 1))

plt.plot(x,y)
plt.gca().set_aspect('equal')
plt.show()