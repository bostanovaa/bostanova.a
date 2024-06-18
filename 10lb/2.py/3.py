sequence = input("Введите последовательность символов: ")
result_set = set()
for char in sequence:
    if char.isdigit() and '5' <= char <= '9':
        result_set.add(char)
    elif char in ['+', '-', '*', '/']:
        result_set.add(char)
print("Множество элементов:")
print(result_set)