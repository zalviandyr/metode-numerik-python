import numpy as np

def f(x):
	return np.log10(x)
	
def rumus(x, x0, x1):
	b0 = f(x0)
	b1 = (f(x1) - f(x0)) / (x1 - x0)
	
	y = b0 + b1*(x-x0)
	return y

def galat(x, fx):
	hitungGalat = ((f(x) - fx) / f(x)) * 100
	return ("%.4f %%"%hitungGalat)
	#Kembalikan 4 angka dibelakang koma dan persen 2 kali untuk membuat persen
# A
fx1 = rumus(5, 4, 6)
galat1 = galat(5, fx1)
print("1. f(5) = ", fx1," Galat = ", galat1)

# B
fx2 = rumus(5, 4.5, 5.5)
galat2 = galat(5, fx2)
print("2. f(5) = ", fx2," Galat = ", galat2)
