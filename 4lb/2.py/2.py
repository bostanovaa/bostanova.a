import math
a = 1,5
p = 3.14

x=float(input("Введите число x: "))

if x < 1.3:
    input ( p*x**2 - 7/x**2)

elif x == 1.3:
    input (a*x**3 + 7*math.sqrt(x))
    
elif x>1.3:
    input (math.log10(x+ 7*math.sqrt(x)))