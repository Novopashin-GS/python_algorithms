# 1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
number_list = [i for i in range(2, 100)]
for number in range(2, 10):
    print(f'числу {number} кратны {len(list(filter(lambda x: x % number == 0, number_list)))} чисел ')
