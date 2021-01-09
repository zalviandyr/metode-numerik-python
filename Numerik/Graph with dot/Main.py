import matplotlib.pyplot as plt
import numpy as np

x = [1,2,4,6]
y = [1,3,1,2]

plt.plot(x, y, 'x', color="red", markersize = 15)

x1 = np.linspace(0,7)
y1 = 1+2*(x1-1)-(x1-1)*(x1-2)+(11/40)*(x1-1)*(x1-2)*(x1-4)

plt.plot(x1,y1)

plt.grid();
plt.show();
