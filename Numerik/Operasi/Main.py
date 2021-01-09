# Using sep and end
print("Programming","Uwaw",sep="_",end="...")
print("SRARR")

print("\n")
# Using input()
print("Using python input()")
name = input("Siapa ? ")
print("Oh Hai ",name)

print("\n")
# input two number for math operation
a = float(input("angka1 = "))
b = float(input("angka2 = "))
print("Tambah ",(a+b))
print("Kurang ",(a-b))
print("Kali ",(a*b))
print("Bagi ",(a/b))
print("Mod ",(a%b))

print("\n")
# next 
x = float(input("Nilai x = "))
y = 1/(x+1/(x+1/(x+1/x)))
print("y = ",y)

print("\n")
# task
jam = int(input("Mulai jam : "))
men = int(input("Mulai menit : "))
dura = int(input("Durasi : "))

jamToMin = jam*60
convertToMin = jamToMin + men
final = convertToMin + dura

finalJam = (final//60)%24
finalMen = final%60
print(finalJam,":",finalMen,sep="")

print("\n")
# comparasi
x = int(input("Input Nilai = "))
hasil = (x >= 100)
print(hasil)

print("\n")
# conditional if
x = input("Makanan : ")
if(x.lower() == "lotek"):
	print("Lotek goooooooooood")
else:
	print("Apa itu",x,"? ")