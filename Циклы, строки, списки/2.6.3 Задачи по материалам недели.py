matrix = []
matrix_result = []
a = ''
stop_flag = False
while not stop_flag:
    a = input()
    if a != 'end':
        matrix.append(list(map(int, a.split())))
    else:
        stop_flag = True

# Создание новой матрицы для результатов
matrix_result = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]

# Проверка и обработка элементов матрицы
for row_index in range(len(matrix)):
    for col_index in range(len(matrix[row_index])):
        if row_index == len(matrix) - 1 and col_index == len(matrix[row_index]) - 1:
            matrix_result[row_index][col_index] = (matrix[row_index - 1][col_index] +
                                            matrix[0][col_index] +
                                            matrix[row_index][col_index - 1] +
                                            matrix[row_index][0])
        elif row_index == len(matrix) - 1:
            matrix_result[row_index][col_index] = (matrix[row_index - 1][col_index] +
                                            matrix[0][col_index] +
                                            matrix[row_index][col_index - 1] +
                                            matrix[row_index][col_index + 1])
        elif col_index == len(matrix[row_index]) - 1:
            matrix_result[row_index][col_index] = (matrix[row_index - 1][col_index] +
                                            matrix[row_index + 1][col_index] +
                                            matrix[row_index][col_index - 1] +
                                            matrix[row_index][0])
        else:
            matrix_result[row_index][col_index] = (matrix[row_index - 1][col_index] +
                                            matrix[row_index + 1][col_index] +
                                            matrix[row_index][col_index - 1] +
                                            matrix[row_index][col_index + 1])

for row in matrix_result:
    for elem in row:
        print(elem, end=' ')
    print()