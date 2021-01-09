def b0(x0,y0):
	return y0

def b1(x0,y0,x1,y1):
	return (y1-y0) / (x1 - x0)

def b2(x0,y0,x1,y1,x2,y2):
	return (b1(x2,y2,x1,y1) - b1(x1,y1,x0,y0)) / (x2 - x0)

def b3(x0,y0,x1,y1,x2,y2,x3,y3):
	return (b2(x3,y3,x2,y2,x1,y1) - b2(x2,y2,x1,y1,x0,y0)) / (x3-x0)

def rumus(x,x3,x2,x1,x0):
	B0 = b0(x0)
	B1 = b1(x1,x0)
	B2 = b2(x2,x1,x0)
	B3 = b3(x3,x2,x1,x0)

	y = B0 + B1*(x-x0) + B2*(x-x0)*(x-x1) + B3*(x-x0)*(x-x1)*(x-x2)
	return y

def galat(x, fx):
	hitungGalat = (f(x) - fx) / f(x) * 100
	return ("%.4f"%hitungGalat) #Kembalikan 4 angka dibelakang koma

# D
# fx = rumus(5, 4.0, 4.5, 5.5, 6)
# hitungGalat = galat(5, fx)
#
# print("3. f(5) = ", fx, " Galat = ",hitungGalat)
print(b0(2,8))
print(b1(2,8,-5,-10))
print(b2(2,8,-5,-10,15,5))
print(b3(2,8,-5,-10,15,5,10,30))