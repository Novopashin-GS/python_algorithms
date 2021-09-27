# 1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив, заданный случайными числами
# на промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы. Сортировка должна быть реализована
# в виде функции. По возможности доработайте алгоритм (сделайте его умнее).
import random


def my_sort3(my_array):
    a = my_array
    n = 1
    while n < len(a):
        flag_sorted = True
        for i in range(len(a) - n):
            if a[i] < a[i+1]:
                a[i], a[i+1] = a[i+1], a[i]
                flag_sorted = False
        if flag_sorted:
            break
        n += 1
    return a


numbers = [random.randrange(-100, 100) for _ in range(50)]
print(my_sort3(numbers))
