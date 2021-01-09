import matplotlib.pyplot as plt
import numpy as np

x = [-5,2,10,15]
y = [-10,8,1,5]

paksiX1 = [-2.93903363]
paksiY1 = [0]

paksiX2 = [0]
paksiY2 = [6.947802205]

b0 = -10
b1 = 2.571428571
b2 = -0.229761905
b3 = 0.017930403

x1 = np.linspace(-10,20)
y1 = b0 + b1*(x1+5) + b2*(x1+5)*(x1-2) + b3*(x1+5)*(x1-2)*(x1-10)

plt.plot(x1,y1)
# plt.plot(x, y, 'o', color="red", markersize = 10)
plt.plot(paksiX1, paksiY1, 'x', color="purple", markersize = 10) #paksi x
plt.plot(paksiX2, paksiY2, 'x', color="red", markersize = 10) # paksi y
plt.grid();
plt.show();
