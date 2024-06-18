n = int(input("Введите количество оценок: "))
grades = []
for i in range(n):
    grade = float(input(f"Введите оценку {i+1}: "))
    grades.append(grade)
print("Оценки:")
for grade in grades:
    print(grade)
average_grade = sum(grades) / len(grades)
print(f"Средняя оценка за урок: {average_grade}")