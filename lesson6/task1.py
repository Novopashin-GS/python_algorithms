# 1. Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех
# уроков. Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
import tracemalloc
from memory_profiler import profile


def test_1():
    tracemalloc.start()
    user_number = '1000000000000000000'
    sum_even = 0
    sum_not_even = 0
    for number in user_number:
        number = int(number)
        if number % 2 == 0:
            sum_even += 1
        else:
            sum_not_even += 1
    print(tracemalloc.get_traced_memory())
    tracemalloc.stop()


def test_2():
    tracemalloc.start()
    user_number = 1000000000000000000
    sum_even = 0
    sum_not_even = 0
    while user_number != 0:
        remainder = user_number % 10
        if remainder % 2 == 0:
            sum_even += 1
        else:
            sum_not_even += 1
        user_number //= 10
    print(tracemalloc.get_traced_memory())
    tracemalloc.stop()


# @profile
def main():
    test_2()
    tracemalloc.clear_traces()
    test_1()


main()
# не особо показательно, поэтому попробуем что-то другое, заодно сравним размеры двух разных программ
# плюс я не особо понимаю, почему в выводе текущего размера блоков памяти он показывает 0, потому что это обычные
# переменные?
# Line #    Mem usage    Increment  Occurences   Line Contents
# ============================================================
#     39     19.7 MiB     19.7 MiB           1   @profile
#     40                                         def main():
#     41     19.7 MiB      0.0 MiB           1       test_2()
#     42     19.7 MiB      0.0 MiB           1       test_1()
