# 5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
import random
random_list = [random.randint(-10, 10) for i in range(10)]
print(random_list)
min_max_value = max(list(filter(lambda x: x < 0, random_list)))
print(f'число {min_max_value} на позиции {random_list.index(min_max_value)}')

