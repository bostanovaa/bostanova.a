n = int(input("Введите количество записей в словаре: ")) 
dictionary = {}
for _ in range(n):
    word, description = input("Введите слово и его значение через тире: ").split("-")
    dictionary[word.strip()] = description.strip()
search_word = input("Введите слово, значение которого нужно найти: ") 
if search_word in dictionary:
    print("Значение слова", search_word + ":", dictionary[search_word])
else:
    print("Нет в словаре")