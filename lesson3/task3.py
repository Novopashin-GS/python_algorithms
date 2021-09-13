# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
import random
random_list = [random.randint(1, 100) for i in range(10)]
print(random_list)
max_value_index = random_list.index(max(random_list))
min_value_index = random_list.index(min(random_list))
random_list[max_value_index], random_list[min_value_index] = random_list[min_value_index], random_list[max_value_index]
print(random_list)
