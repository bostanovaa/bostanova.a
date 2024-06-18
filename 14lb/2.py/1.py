students = {}
n = int(input("Введите количество студентов: "))
for _ in range(n):
    last_name, major, group = input().split()
    if major in students:
        students[major].append(last_name)
    else:
        students[major] = [last_name]
query = input("Введите название специальности: ")
if query in students:
    print("Фамилии студентов на специальности", query + ":", ",".join(students[query]))
else:
    print("Проверьте запрос")