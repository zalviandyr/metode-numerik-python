import matplotlib.pyplot as plt
import numpy as np

def cetak(x,y,subplot,judul):
	plt.subplot(2,3,subplot)
	plt.plot(x,y)
	plt.title(judul)
	plt.grid()
	
x = np.linspace(-2,2)

#soal 1
y= x + np.exp(x)
cetak(x,y,1,"Soal 1")

#soal 2
y = 0.5*x**2 + 2.5*x + 4.5
cetak(x,y,2,"Soal 2")

#soal 3
y = 5*x**3 - 5*x**2 + 6*x - 2
cetak(x,y,3,"Soal 3")

#soal 4
y = -25 + 82*x - 90*x**2 + 44*x**3 - 8*x**4 + 0.7*x**5
cetak(x,y,4,"Soal 4")

#soal 5
y = np.sin(10*x) + np.cos(3*x)
cetak(x,y,5,"Soal 5")

plt.show()