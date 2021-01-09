import matplotlib.pyplot as plt
import numpy as np

x = [2,-5,15,10]
y = [8,-10,5,35]

paksiX1 = [0.35340281665223977, 15.393589887988863]
paksiY1 = [0,0]

paksiY2 = [-1.55276]
paksiX2 = [0]

b0 = 8
b1 = 2.571
b2 = -0.14011
b3 = -0.03874

x1 = np.linspace(-5,20)
y1 = b0 + b1 * (x1- 2) + b2 * (x1 - 2) * (x1+ 5) + b3 * (x1 - 2) * (x1 + 5) * (x1 - 15)

plt.plot(x1,y1)
#plt.plot(x, y, 'o', color="red", markersize = 10)
plt.plot(paksiX1, paksiY1, 'x', color="blue", markersize = 10)
plt.plot(paksiX2, paksiY2, 'x', color="red", markersize = 10)
plt.grid();
plt.show();