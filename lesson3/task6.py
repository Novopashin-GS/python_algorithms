# 6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.
import random
random_list = [random.randint(0, 100) for i in range(10)]
print(random_list)
max_value_index = random_list.index(max(random_list))
min_value_index = random_list.index(min(random_list))
if max_value_index > min_value_index:
    print(sum(random_list[min_value_index + 1:max_value_index]))
else:
    print(sum(random_list[min_value_index - 1:max_value_index:-1]))

