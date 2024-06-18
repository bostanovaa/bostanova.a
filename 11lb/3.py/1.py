numbers = []
for i in range(20):
    num = int(input("Введите целое число: "))
    numbers.append(num)
max_num = max(numbers)
max_index = numbers.index(max_num)
numbers[0], numbers[max_index] = numbers[max_index], numbers[0]
print("Список с наибольшим элементом, поменянным местами с первым элементом:")
print(numbers)