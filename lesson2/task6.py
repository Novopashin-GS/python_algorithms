# 6. В программе генерируется случайное целое число от 0 до 100. Пользователь должен его отгадать не более чем за
# 10 попыток. После каждой неудачной попытки должно сообщаться больше или меньше введенное пользователем число, чем то,
# что загадано. Если за 10 попыток число не отгадано, то вывести загаданное число.
import random
random_number = random.randint(1, 100)
count = 0
while count < 10:
    count += 1
    user_answer = int(input('Отгадайте число от 1 до 100: '))
    if user_answer == random_number:
        print(f'Верно, это {random_number}')
        break
    elif user_answer < random_number:
        print('Нет, загаданное число больше')
    else:
        print('Нет, загаданное число меньше')
else:
    print(f'Вы не угадали, это было {random_number}')
