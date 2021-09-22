import tracemalloc


def test_2():
    number_list = [i for i in range(2, 100)]
    for number in range(2, 10):
        print(f'числу {number} кратны {len([i for i in number_list if i % number == 0])} чисел ')
    print(tracemalloc.get_traced_memory())


tracemalloc.start()
test_2()
tracemalloc.stop()
