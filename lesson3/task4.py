# 4. Определить, какое число в массиве встречается чаще всего.
import random
random_list = [random.randint(1, 3) for i in range(10)]
print(random_list)
max_count = 0
number = None
for i in set(random_list):
    if random_list.count(i) > max_count:
        max_count = random_list.count(i)
        number = i
print(f'число {number} встречается {max_count} раз')
