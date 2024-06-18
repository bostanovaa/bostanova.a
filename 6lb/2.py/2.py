numbers = []
for i in range(1, 16):
    num = int(input(f"Введите {i}-е число: "))
    numbers.append(num)
sum_numbers = sum(numbers)
print(f"Сумма чисел: {sum_numbers}")
prod_numbers = 1
for num in numbers:
    prod_numbers *= num
print(f"Произведение чисел: {prod_numbers}")