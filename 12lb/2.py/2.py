# Функция для создания матрицы
def create_matrix(rows, cols):
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            element = int(input(f'Введите элемент матрицы [{i}][{j}]: '))
            row.append(element)
        matrix.append(row)
    return matrix
def sum_of_rows(matrix):
    sums = []
    for row in matrix:
        row_sum = sum(row)
        sums.append(row_sum)
    return sums
rows = int(input('Введите количество строк: '))
cols = int(input('Введите количество столбцов: '))
matrix = create_matrix(rows, cols)
print('Исходная матрица:')
for row in matrix:
    print(row)
sums = sum_of_rows(matrix)
print('Сумма элементов каждой строки матрицы:', sums)