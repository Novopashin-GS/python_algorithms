# Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят, и сколько между ними находится букв.
first, end = input('Введите первую букву английского языка '), input('Введите вторую букву английского языка ')
print(f'{ord(first) - (ord("a")-1)} - позиция первой буквы {ord(end) - (ord("a")-1)} - позиция второй буквы \
{ord(end)- (ord(first)) - 1} - сколько между ними букв между ними')
