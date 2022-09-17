import math
x = float(input("x ="))
cr = math.fabs(x + 1) + 0.1
korkub = cr ** (1./3.)
h = math.tan(2*x) + math.cos(4*x-math.sqrt(x) - 2 / korkub)
print(h)
