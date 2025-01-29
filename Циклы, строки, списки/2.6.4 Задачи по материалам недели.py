n = int(input())

# Создание пустой матрицы размером n x n
matrix  = [[0 for _ in range(n)] for _ in range(n)]

# Переменные
row, col  = 0, 0
direction = 0 # 0: вправо, 1: вниз, 2: влево, 3: вверх
num = 1 # Номер ячейки

# Границы для движения
left, right = 0, n - 1
top, bottom = 0, n - 1

while num <= n * n:
    #Заполнение текущей ячейки
    matrix[row][col] = num
    num += 1

    # Определение следующего направления
    if direction == 0:  # вправо
        col += 1
        if col > right:
            col = right
            row += 1
            direction = 1
            top += 1
    elif direction == 1:  # вниз
        row += 1
        if row > bottom:
            row = bottom
            col -= 1
            direction = 2
            right -= 1
    elif direction == 2:  # влево
        col -= 1
        if col < left:
            col = left
            row -= 1
            direction = 3
            bottom -= 1
    elif direction == 3:  # вверх
        row -= 1
        if row < top:
            row = top
            col += 1
            direction = 0
            left += 1


for row in matrix:
    print(' '.join(map(str, row)))



