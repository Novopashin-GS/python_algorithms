# 4. Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ..Количество элементов (n) вводится с клавиатуры.
n = int(input('Введите количество элементов '))
my_list = [0] * n
my_list[0] = 1
for element in range(1, n):
    my_list[element] = my_list[element - 1] * -0.5
print(sum(my_list))
