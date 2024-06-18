distance = int(input("Введите начальную дистанцию (в км): "))
total_distance = distance

for day in range(2, 8):
    distance *= 1.1  # Увеличиваем дистанцию на 10%
    total_distance += distance

print(f"Суммарный путь спортсмена за неделю: {total_distance} км")