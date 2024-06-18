import math
a=2.8
b=-0.3
c=4

x=float(input("Введите число x: "))

if x< 1.2:
    input (a*x**2+b*x+c)
elif x==1.2:
    input (a/x+ math.sqrt(x**2+1))
    
elif x>1.2:
    input ((a+b*x)/ math.sqrt(x**2 + 1))

