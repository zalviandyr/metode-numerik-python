import numpy as np

def f(x):
	return np.log10(x)
	
def b0(x0):
	return f(x0)

def b1(x1,x0):
	return (f(x1) - f(x0)) / (x1 - x0)

def b2(x2,x1,x0):
	return (b1(x2,x1) - b1(x1,x0)) / (x2 - x0)

def rumus(x,x2,x1,x0):
	B0 = b0(x0)
	B1 = b1(x1,x0)
	B2 = b2(x2,x1,x0)

	y = B0 + B1*(x-x0) + B2*(x-x0)*(x-x1)
	return y

def galat(x, fx):
	hitungGalat = (f(x) - fx) / f(x) * 100
	return ("%.4f"%hitungGalat) #Kembalikan 4 angka dibelakang koma

# C
fx = rumus(5, 4.5, 5.5, 6)
hitungGalat = galat(5, fx)

print("3. f(5) = ", fx, " Galat = ",hitungGalat)