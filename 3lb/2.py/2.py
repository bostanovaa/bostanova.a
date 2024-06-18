a = float(input("Введите число a: "))
b = float(input("Введите число b: "))


if abs(a) > abs(b):
    a /= 5

print("a after processing:", a)
print("b after processing:", b)