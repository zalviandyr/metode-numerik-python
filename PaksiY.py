b0 = -10
b1 = 2.571
b2 = 0.011904762
b3 = -0.03040293

x = 0
y = b0 + b1*(x+5) + b2*(x+5)*(x-2) + b3*(x+5)*(x-2)*(x-10)
print(y)