import math
def skr(x):
    h = math.tan(2 * x) + math.cos(4 * x - math.sqrt(x) - 2 / math.fabs(x + 1) + 0.1 ** (1. / 3.))
    return h
x1 = float(input("x ="))
print(skr(x1))

