def input_matrix():
    n = int(input("Введите размер квадратной матрицы: "))
    matrix = []
    for i in range(n):
        row = list(map(int, input(f"Введите элементы {i+1}-й строки через пробел: ").split()))
        matrix.append(row)
    return matrix
def sum_positive_elements(matrix):
    n = len(matrix)
    total_sum = 0
    for i in range(n):
        for j in range(n):
            if j <= i and matrix[i][j] > 0:
                total_sum += matrix[i][j]
    return total_sum
print("Введите элементы квадратной матрицы:")
matrix = input_matrix()
print("\nИсходная матрица:")
for row in matrix:
    print(" ".join(str(element) for element in row))
result = sum_positive_elements(matrix)
print(f"\nСумма положительных элементов под главной диагональю и на диагонали: {result}")