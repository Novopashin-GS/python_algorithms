# Написать программу, которая генерирует в указанных пользователем границах
# случайное целое число,
# случайное вещественное число,
# случайный символ.
# Для каждого из трех случаев пользователь задает свои границы диапазона.
# Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти символы.
# Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.
import random
low_range_for_int = int(input('Введите нижнию границу диапазона для целого числа '))
upper_range_for_int = int(input('Введите верхнюю границу диапазона для целого числа '))
print(random.randint(low_range_for_int, upper_range_for_int))
low_range_for_float = float(input('Введите нижнию границу диапазона для вещественного числа '))
upper_range_for_float = float(input('Введите верхнюю границу диапазона для вещественного числа '))
print(random.uniform(low_range_for_float, upper_range_for_float))
low_range_for_symbol = input('Введите нижнию границу диапазона для символа ')
upper_range_for_symbol = input('Введите верхнюю границу диапазона для символа ')
print(random.choice([chr(symbol) for symbol in range(ord(low_range_for_symbol), ord(upper_range_for_symbol)+1)]))
