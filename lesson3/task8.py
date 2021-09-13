# 8. Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк. Программа должна вычислять сумму
# введенных элементов каждой строки и записывать ее в последнюю ячейку строки.
# В конце следует вывести полученную матрицу.

import random
matrix = [[random.randint(1, 100) for n in range(4)] for m in range(4)]
print(matrix)
for i in matrix:
    i.append(sum(i))
print('\n'.join(['\t'.join(map(str, element)) for element in matrix]))
