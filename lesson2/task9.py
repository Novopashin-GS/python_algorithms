# Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
# Вывести на экран это число и сумму его цифр.
user_numbers = input("Введите через запятую и пробел числа ")
user_list = list(map(int, user_numbers.split(', ')))
sum_dict = {}
for element in user_list:
    number = element
    sum_element = 0
    while number != 0:
        sum_element += number % 10
        number //= 10
    sum_dict[element] = sum_element
max_value = max(sum_dict.values())
for key, value in sum_dict.items():
    if value == max_value:
        print(f'Число - {key}, сумма его цифр максимальная и равна {value}')
