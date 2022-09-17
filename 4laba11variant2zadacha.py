import math
x = float(input("x ="))
y = float(input("y ="))
h = x * math.log10(y) + 1 / x ** 2 + y ** 2 + 0.03 - math.e ** 6 * x - y
print(h)