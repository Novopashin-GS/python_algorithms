# 1. Проанализировать скорость и сложность одного любого алгоритма, разработанных в рамках домашнего задания первых
# трех уроков.
# Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.
# 5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
import time
import cProfile
import random


def min_max_new(n):
    start = time.time()
    random_list = [random.randint(-100, 100) for _ in range(n)]
    min_max_value = max(list(filter(lambda x: x < 0, random_list)))
    print(f'число {min_max_value} на позиции {random_list.index(min_max_value)}')
    end = time.time()
    print(f'{end-start:4f}')


def min_max_second(n):
    start = time.time()
    random_list = [random.randint(-100, 100) for _ in range(n)]
    minus_list = []
    for i in random_list:
        if i < 0:
            minus_list.append(i)
    min_max_value = max(minus_list)
    min_max_value_idx = random_list.index(min_max_value)
    print(f'число {min_max_value} на позиции {min_max_value_idx}')
    end = time.time()
    print(f'{end-start:4f}')


# def main():
    # min_max_second(10000)
    # min_max_new(10000)


# cProfile.run('main()')
# как ни странно min_max_second выполняется быстрее, наверное, filter медленный


def min_max_new2(n):
    start = time.time()
    random_list = [random.randint(-100, 100) for _ in range(n)]
    min_max_value = max([i for i in random_list if i < 0])
    print(f'число {min_max_value} на позиции {random_list.index(min_max_value)}')
    end = time.time()
    print(f'{end-start:4f}')


def main():
    min_max_second(100_000)
    min_max_new(100_000)
    min_max_new2(100_000)


# cProfile.run('main()')
# в этот момент подключил библиотеку time
main()
# наверное, в выбранном мной задании результат зависит от расположения этого максимального среди минимальных значений,
# но в большинстве опытов min_max_new2 показывает лучшие результаты
