# 2. Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
user_number = input('Введите число ')
sum_even = 0
sum_not_even = 0
try:
    for number in user_number:
        number = int(number)
        if number % 2 == 0:
            sum_even += 1
        else:
            sum_not_even += 1
except ValueError:
    print('Нужно ввести число')
print(f'{sum_even = }, {sum_not_even = }')
