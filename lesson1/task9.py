# Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).
first_number = int(input("Введите первое число "))
second_number = int(input("Введите второе число "))
last_number = int(input("Введите третье число "))
if first_number <= second_number <= last_number or last_number <= second_number <= first_number:
    print(f'Среднее число - {second_number}')
elif second_number <= first_number <= last_number or last_number <= first_number <= second_number:
    print(f'Среднее число - {first_number}')
else:
    print(f'Среднее число - {last_number}')
