numbers = []
for i in range(10):
    num = int(input("Введите целое число: "))
    numbers.append(num)
min_num = min(numbers)
min_index = numbers.index(min_num)
numbers[min_index], numbers[-1] = numbers[-1], numbers[min_index]
print("Список после замены наименьшего элемента с последним:")
print(numbers)