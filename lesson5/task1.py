# Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала (т.е. 4 отдельных числа)
# для каждого предприятия.. Программа должна определить среднюю прибыль (за год для всех предприятий) и вывести
# наименования предприятий, чья прибыль выше среднего и отдельно вывести наименования предприятий,
# чья прибыль ниже среднего.
count_enterprise = int(input('Введите количество предприятий '))
my_dict = {}
count = 0
for i in range(count_enterprise):
    name = input('Введите название предприятия ')
    proceeds = list(map(int, input('Введите через запятую и пробел выручку за каждый квартал ').split(', ')))
    my_dict.setdefault(name, sum(proceeds))
    count += sum(proceeds)
average_proceeds = count/count_enterprise
name_first = [n for n, v in my_dict.items() if v >= average_proceeds]
name_second = [n for n, v in my_dict.items() if v < average_proceeds]
print(f'Названия предприятий, чья прибыль выше средней: {", ".join(name_first)}')
print(f'Названия предприятий, чья прибыль ниже средней: {", ".join(name_second)}')
