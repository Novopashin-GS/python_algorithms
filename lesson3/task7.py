# 7. В одномерном массиве целых чисел определить два наименьших элемента. Они могут быть как равны между собой
# (оба являться минимальными), так и различаться.
import random
random_list = [random.randint(0, 100) for i in range(10)]
print(random_list)
random_list.sort()
print(random_list[0], random_list[1])
