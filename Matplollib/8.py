import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2, 100)

plt.plot(x, x, label='linear')
plt.plot(x, x**2, label='kuadrat')
plt.plot(x, x**3, label='kubik')

plt.xlabel('paksi x')
plt.ylabel('paksi y')

plt.title("Contoh Plot")
plt.legend()
plt.show()
