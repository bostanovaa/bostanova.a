import math
a=-0.5
b=2
t=float(input("Введите число t: "))
e=float(input("Введите число e: "))

if 1 <= t <=2:
    input (a*t**2*math.log10*t)

elif t<1:
    input (1)
    
elif t>2:
    input (e**(a*t)* math.cos(b*t))