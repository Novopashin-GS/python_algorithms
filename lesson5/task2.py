# Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число представляется как
# коллекция, элементы которой это цифры числа. Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’]
# и [‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
import collections
# Создадим два словаря, один содержит соответствие 16-тиричных чисел с 10-тиричными, второй наоборот
k = ord('A')
dict_16_to_10 = {}
for i in range(10):
    dict_16_to_10[str(i)] = i
for i in range(10, 16):
    dict_16_to_10[str(chr(k))] = i
    k += 1
k = ord('A')
dict_10_to_16 = {}
for i in range(10):
    dict_10_to_16[i] = str(i)
for i in range(10, 16):
    dict_10_to_16[i] = str(chr(k))
    k += 1
# В соответствии с заданием сохраняем введенные числа в списке
a = input('Введите первое шестнадцатиричное число ')
b = input('Введите второе шестнадцатиричное число ')
my_dict = collections.defaultdict(list)
for i in a:
    my_dict['a'].append(i)
for i in b:
    my_dict['b'].append(i)
# Переведем числа в 10-ричную систему
sum_number_one = 0
sum_number_second = 0
n = 0
for number in my_dict['a'][::-1]:
    sum_number_one += dict_16_to_10[number] * 16 ** n
    n += 1
n = 0
for number in my_dict['b'][::-1]:
    sum_number_second += dict_16_to_10[number] * 16 ** n
    n += 1

# Находим сумму чисел и переводим ее в 16-ти ричную систему
def sum_numbers():
    sum_all = sum_number_one + sum_number_second
    while sum_all != 0:
        my_dict['sum'].append(dict_10_to_16[sum_all % 16])
        sum_all //= 16
    my_dict['sum'].reverse()

# Находим произведение чисел и переводим это в 16-ти ричную систему
def mul_numbers():
    mul_all = sum_number_one * sum_number_second
    while mul_all != 0:
        my_dict['mul'].append(dict_10_to_16[mul_all % 16])
        mul_all //= 16
    my_dict['mul'].reverse()


sum_numbers()
mul_numbers()
print(my_dict)
