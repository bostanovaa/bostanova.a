def print_matrix_in_snake_order(matrix):
    for i in range(len(matrix)):
        if i % 2 == 0:
            print(*matrix[i])
        else:
            print(*matrix[i][::-1])
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]
print_matrix_in_snake_order(matrix)