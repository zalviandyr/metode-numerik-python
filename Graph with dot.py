import matplotlib.pyplot as plt
import numpy as np

x = [-5,2,10,15]
y = [-10,8,30,5]

paksiX1 = [-8.163, 0.0792, 15.475]
paksiY1 = [0,0,0]

paksiY2 = [-0.304]
paksiX2 = [0]

b0 = -10
b1 = 2.571
b2 = 0.011904762
b3 = -0.03040293

x1 = np.linspace(-10,20)
y1 = b0 + b1*(x1+5) + b2*(x1+5)*(x1-2) + b3*(x1+5)*(x1-2)*(x1-10)

plt.plot(x1,y1)
plt.plot(x, y, 'o', color="red", markersize = 10)
plt.plot(paksiX1, paksiY1, 'x', color="blue", markersize = 10)
plt.plot(paksiX2, paksiY2, 'x', color="red", markersize = 10)
plt.grid();
plt.show();