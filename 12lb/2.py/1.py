rows = int(input("Введите количество строк в матрице: "))
cols = int(input("Введите количество столбцов в матрице: "))
matrix = []
for i in range(rows):
    row = []
    for j in range(cols):
        row.append(int(input(f"Введите элемент матрицы [{i}][{j}]: ")))
    matrix.append(row)
print("Исходная матрица:")
for row in matrix:
    print(row)
column_sums = [0] * cols
for i in range(rows):
    for j in range(cols):
        column_sums[j] += matrix[i][j]
for j in range(cols):
    print(f"Сумма элементов в столбце {j+1}: {column_sums[j]}")