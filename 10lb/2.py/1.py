sequence = input("Введите непустую последовательность символов: ")
result_set = {char for char in sequence if char.isdigit() or (char.isalpha() and char.upper() >= 'A' and char.upper() <= 'Z' )}
print("Множество из встречающихся букв от ‘А’ до ‘Z’ и цифр от ‘0’ до ‘5’:", result_set)
