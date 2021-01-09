import numpy as np

"""
    Contoh soal
    Maksimumkan : Z = 3x1 + 5x2
    Batasan (constrain)
    1) 2x1 <= 8
    2) 3x2 <= 15
    3) 6x1 + 5x2 <= 30

    z - 3x1 + 5x2 = 0
    2x1 + x3 = 8
    3x2 + x4 = 15
    6x1 + 5x2 + x5 = 30


"""

def indexKey(z): #mencari kolom yang mengandung nilai min paling minimum
    minimumValue = min(z)
    if minimumValue is 0:
        return 0
    else:
        return z.index(minimumValue)

def getColumnKey(z, x3, x4, x5):
    key = indexKey(z)
    newRow = [z[key], x3[key], x4[key], x5[key]]
    return newRow

def getValueIndex(z, x3, x4, x5):
    key = indexKey(z)
    try:
        valueIndexZ = z[key] / z[-1]
    except:
        print("Error pembagian nol")

#    z  x1  x2 x3 x4 x5 NK
z = [1, -3, -5, 0, 0, 0, 0]
x3 = [0, 2, 0, 1, 0, 0, 8]
x4 = [0, 0, 3, 0, 1, 0, 15]
x5 = [0, 6, 5, 0, 0, 1, 30]
getValueIndex(z, x3, x4, x5)


