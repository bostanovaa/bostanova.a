input_string = input("Введите строку с английским текстом: ")
words = input_string.split()
count_b_words = sum(1 for word in words if word.lower().startswith('b'))
print("Количество слов, начинающихся с буквы 'b':", count_b_words)