import  numpy as np


def f(x): #SOAL NO 1
	return np.e**(-x) - x

def fax(x):
	return -np.e**(-x) - 1

def rumus(x0):
	temp = f(x0) / fax(x0)
	x1 = x0 - temp
	
	return x1
	
x0 = int(input("Masukkan angka x0 : "))
iterasi = int(input("Berapa iterasi : "))

for i in range(iterasi):
	if(i == 0):
		x1 = rumus(x0)
	else:
		x1 = rumus(x1)
	print(i," = ",x1)

	'''
hasil0 = rumus(0)
hasil1 = rumus(hasil0)
hasil2 = rumus(hasil1)
hasil3 = rumus(hasil2)
hasil4 = rumus(hasil3)
hasil5 = rumus(hasil4)
hasil6 = rumus(hasil5)
hasil7 = rumus(hasil6)
hasil8 = rumus(hasil7)
hasil9 = rumus(hasil8)
hasil10 = rumus(hasil9)

print("0 ",hasil0)
print("1 ",hasil1)
print("2 ",hasil2)
print("3 ",hasil3)
print("4 ",hasil4)
print("5 ",hasil5)
print("6 ",hasil6)
print("7 ",hasil7)
print("8 ",hasil8)
print("9 ",hasil9)
print("10 ",hasil10)
'''