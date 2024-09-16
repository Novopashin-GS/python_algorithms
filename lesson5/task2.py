# Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число представляется как
# коллекция, элементы которой это цифры числа. Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’]
# и [‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
import collections
k = ord('A')
dict_16_to_10 = {}
for i in range(10):
    dict_16_to_10[str(i)] = i
for i in range(10, 16):
    dict_16_to_10[str(chr(k))] = i
    k += 1
dict_10_to_16 = {}
for k, v in dict_16_to_10.items():
    dict_10_to_16[v] = k
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


def action_numbers(action):
    if action == '+':
        count_all = sum_number_one + sum_number_second
    elif action == '*':
        count_all = sum_number_one * sum_number_second
    while count_all != 0:
        my_dict[action].append(dict_10_to_16[count_all % 16])
        count_all //= 16
    my_dict[action].reverse()


action_numbers('+')
action_numbers('*')
print(my_dict)
