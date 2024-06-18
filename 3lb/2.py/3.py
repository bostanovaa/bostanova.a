a = int(input("Введите число a: "))
b = int(input("Введите число b: "))
c = int(input("Введите число c: "))

count = 0

if a < 0:
    count += 1
if b < 0:
    count += 1
if c < 0:
    count += 1

print("Номера с отрицательным знаком a, b, c:", count)