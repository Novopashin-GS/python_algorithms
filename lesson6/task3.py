import tracemalloc


def test_1():
    number_list = [i for i in range(2, 100)]
    for number in range(2, 10):
        print(f'числу {number} кратны {len(list(filter(lambda x: x % number == 0, number_list)))} чисел ')
    print(tracemalloc.get_traced_memory())


tracemalloc.start()
test_1()
tracemalloc.stop()
