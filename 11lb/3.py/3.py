numbers = []
for i in range(15):
    num = float(input("Введите число: "))
    numbers.append(num)
max_num = max(numbers)
max_index = numbers.index(max_num)
numbers[-1], numbers[max_index] = numbers[max_index], numbers[-1]
print("Список с наибольшим элементом, поменянным с последним:")
print(numbers)