str1 = "1 3 4 2" 
str2 = "Зеркало фильмы мне  заменяет" 
words = str2.split() 
indexes = [int(i) - 1 for i in str1.split()]
new_sentence = " ".join([words[i] for i in indexes]) 
new_sentence = new_sentence.capitalize()
print(new_sentence)