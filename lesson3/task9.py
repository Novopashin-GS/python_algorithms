# 9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.
import random
matrix = [[random.randint(1, 100) for n in range(4)] for m in range(4)]
print('\n'.join(['\t'.join(map(str, element)) for element in matrix]))
max_value = 0
for i in range(4):
    min_element_in_column = matrix[0][i]
    for element in matrix:
        if element[i] < min_element_in_column:
            min_element_in_column = element[i]
    print(f'в столбце {i+1} минимальный элемент равен {min_element_in_column}')
    if min_element_in_column > max_value:
        max_value = min_element_in_column
print(f'максимальное значение среди минимальных - {max_value}')
