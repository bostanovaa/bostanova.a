sequence = []
for i in range(1, 17):
    num = int(input(f"Введите {i}-й элемент последовательности: "))
    sequence.append(num)
even_index_values = sequence[1::2]
print("even_index_values:", even_index_values)