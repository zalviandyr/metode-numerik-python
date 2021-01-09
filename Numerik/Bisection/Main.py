import numpy as np

def f(x):
	b0 = -10
	b1 = 2.571
	b2 = 0.011904762
	b3 = -0.03040293

	f = b0 + b1 * (x + 5) + b2 * (x + 5) * (x - 2) + b3 * (x + 5) * (x - 2) * (x - 10)
	return f

def bisection(a,b):
	if(f(a)*f(b) >= 0):
		print("nilai a dan b tidak tepat \n")
		return
		
	c = a
	while((b-a) >= 0.00001):
		c = (a+b)/2
		if(f(c) == 0.0):
			break
		if(f(c)*f(a) < 0):
			b=c
		else:
			a=c
	print("nilai akar adalah :","%.4f"%c)

a= -20
b= 20
bisection(a,b)