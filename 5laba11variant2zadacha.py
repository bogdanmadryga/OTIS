import math
def skr(x1, y1, x2, y2):
    riz =  math.sqrt(((x2 - x1)**2) + ((y2-y1)**2))
    return riz
a = float(input("x A="))
a1 = float(input("y A="))
b =float(input("x B="))
b1= float(input("y B="))
c = float(input("x C="))
c1=float(input("y C="))
z = 0
a0 = skr(a, z, a1, z)
b0 = skr(b, z, b1, z)
c0 = skr(c, z, c1, z)
if a0<b0 and a0<c0:
    print("Найближча точка до центру: A", a0)
elif b0<a0 and b0<c0:
    print("Найближча точка до центру: B", b0)
elif c0<a0 and c0<b0:
    print("Найближча точка до центру: C", c0)
else:
    print("Error")

