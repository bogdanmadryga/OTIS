import math
def skr(x):
    h = 7 * math.log(x, math.e) + math.log(x, 7) + math.log10(x)
    return(h)
def skr1(x):
    h = math.sin(x) - math.cos(x + 2 + (math.pi/2))
    return h
def skr2(x):
    h = (2.24 * (math.e ** (0.5 * x + 0.1))) * 2 ** 0.3 * x
    return h
x = float(input("x="))
if x>=1:
    print(skr(x))
elif -10.3<x<1:
    print(skr1(x))
elif x <= -10.3:
    print(skr2(x))
else:
    print("Entered 'x' not valid")