# 2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами на
# промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.

# как я понял, нужно исходный массив разбивать на подмассивы до тех пор, пока не размер подмассивов не окажется равным
# 1. Для этого используем рекурсию, а затем начнем сортировать подмассивы
import operator
import random


def merge_sort(L, compare=operator.lt):

    def merge(left, right, compare): # сортировка
        result = []
        i, j = 0, 0
        while i < len(left) and j < len(right):
            if compare(left[i], right[j]):
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        while i < len(left):
            result.append(left[i])
            i += 1
        while j < len(right):
            result.append(right[j])
            j += 1
        return result

    if len(L) < 2: # разбиение
        return L[:]
    else:
        middle = int(len(L) / 2)
        left = merge_sort(L[:middle], compare)
        right = merge_sort(L[middle:], compare)
        return merge(left, right, compare)


array = [random.randrange(0, 50) for _ in range(20)]
print(array)
print(merge_sort(array))
