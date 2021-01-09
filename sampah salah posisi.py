import numpy as np


def f(x):
    b0 = -10
    b1 = 2.571428571
    b2 = -0.229761905
    b3 = 0.017930403

    f = b0 + b1 * (x + 5) + b2 * (x + 5) * (x - 2) + b3 * (x + 5) * (x - 2) * (x - 10)
    return f

def xr(xu, xl):
    fxu = f(xu)
    fxl = f(xl)
    temp = fxu * (xl - xu) / (fxl - fxu)
    xr = xu - temp
    return xr


def hitung(xu, xl, iterasi):
    for i in range(iterasi):
        xRoot = xr(xu, xl)
        if (f(xl) * f(xRoot) < 0):
            xu = xRoot
        else:
            xl = xRoot
        print("Iterasi Ke-", i, " = ", xRoot, sep="")


try:  # menangkap error jika user menginputkan bukan angka
    xLower = int(input("X Lower : "))
    xUpper = int(input("X Upper : "))
    iterasi = int(input("Berapa iterasi : "))

    hitung(xLower, xUpper, iterasi)
except ValueError:
    print("input salah")
