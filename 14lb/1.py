phone_book = {}
n = int(input("Введите количество номеров телефонов: "))
for _ in range(n):
    phone, name = input().split()
    phone_book[name] = phone
query = input("Введите имя, чей телефон нужно найти: ")
if query in phone_book:
    print(f"Номер телефона: {phone_book[query]}")
else:
    print("Нет в телефонной книге")