import tracemalloc
from memory_profiler import profile


def test_1():
    number_list = [i for i in range(2, 100)]
    for number in range(2, 10):
        print(f'числу {number} кратны {len(list(filter(lambda x: x % number == 0, number_list)))} чисел ')
    print(tracemalloc.get_traced_memory())


def test_2():
    number_list = [i for i in range(2, 100)]
    for number in range(2, 10):
        print(f'числу {number} кратны {len([i for i in number_list if i % number == 0])} чисел ')
    print(tracemalloc.get_traced_memory())


# @profile
# def main():
#  test_1()
#  test_2()

tracemalloc.start()
test_1()
tracemalloc.stop()
tracemalloc.start()
test_2()
tracemalloc.stop()
# Если запустить таким образом, то получается один результат, если по отдельности, то другой. Я не знаю почему,
# не работал с tracemalloc, буду рад, если расскажите, но в любом случае, вариант с генератором потребляет меньше
# памяти
# Line #    Mem usage    Increment  Occurences   Line Contents
# ============================================================
#     23     19.6 MiB     19.6 MiB           1   @profile
#     24                                         def main():
#     25     19.6 MiB      0.0 MiB           1       test_2()
#     26     19.6 MiB      0.0 MiB           1       test_1()
