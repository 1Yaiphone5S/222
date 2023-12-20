import numpy as np
import itertools

# Создаем матрицу 8-го порядка (здесь представлена просто в виде списка списков, но обычно вы бы считали ее из ваших данных)
matrix_data = [
    [1, 2, 3, 4, 5, 6, 7, 8],
    [9, 10, 11, 12, 13, 14, 15, 16],
    [17, 18, 19, 20, 21, 22, 23, 24],
    [25, 26, 27, 28, 29, 30, 31, 32],
    [33, 34, 35, 36, 37, 38, 39, 40],
    [41, 42, 43, 44, 45, 46, 47, 48],
    [49, 50, 51, 52, 53, 54, 55, 56],
    [57, 58, 59, 60, 61, 62, 63, 64]
]

matrix = np.array(matrix_data)

# Вычисляем определитель
determinant = np.linalg.det(matrix)

# Проверяем каждое слагаемое в разложении на наличие нужного произведения и считаем их количество
count = 0
for permutation in itertools.permutations(range(8)):
    product = 1
    sign = (-1) ** sum(1 for i, j in itertools.combinations(permutation, 2) if i > j)
    for i, j in enumerate(permutation):
        product *= matrix[i][j]
    if product == matrix[1][4] * matrix[5][2] * matrix[4][1] * matrix[5][4]:
        count += 1

print("Определитель:", determinant)
print("Количество слагаемых с произведением a14 * a52 * a41 * a54:", count)