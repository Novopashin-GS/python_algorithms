# 2. Написать два алгоритма нахождения i-го по счёту простого числа.
# Без использования «Решета Эратосфена»;
# Используя алгоритм «Решето Эратосфена»
# Примечание ко всему домашнему заданию: Проанализировать скорость и сложность алгоритмов.
# Результаты анализа сохранить в виде комментариев в файле с кодом.
# от 1 до 1000 168 простых чисел
import time
import cProfile


def with_era(n):
    start = time.time()
    my_list = [i for i in range(2, 1001)]
    for number in my_list:
        if number != 0:
            for k in range(number*2, 1001, number):
                my_list[k-2] = 0
    new_my_list = [i for i in my_list if i != 0]
    end = time.time()
    print(f'{end - start:4f}')
    return new_my_list[n-1]


def without_era(n):
    my_list = []
    start = time.time()
    for number in range(2, 1001):
        trigger = 1
        for k in range(2, number):
            if number % k == 0:
                trigger = 0
                break
        if trigger == 1:
            my_list.append(number)
    end = time.time()
    print(f'{end - start:4f}')
    return my_list[n-1]


def main():
    with_era(168)
    without_era(168)


main()
cProfile.run('main()')
# без использования решета код работает дольше, потому что число приходится делить на все предыдущие до него
