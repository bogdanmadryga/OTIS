import math
def skr(x, y):
    h = x * math.log10(y) + 1 / x ** 2 + y ** 2 + 0.03 - math.e ** 6 * x - y
    return h
x1 = float(input("x ="))
y1 = float(input("y ="))
print(skr(x1, y1))
