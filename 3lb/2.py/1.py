a = float(input("Введите число a: "))
b = float(input("Введите число b: "))
c = float(input("Введите число c: "))

if a >= 0:
    a_squared = a ** 2
else:
    a_squared = a ** 4

if b >= 0:
    b_squared = b ** 2
else:
    b_squared = b ** 4

if c >= 0:
    c_squared = c ** 2
else:
    c_squared = c ** 4

print("Результаты:")
print("a в квадрате: ", a_squared)
print("b в квадрате: ", b_squared)
print("c в квадрате: ", c_squared)