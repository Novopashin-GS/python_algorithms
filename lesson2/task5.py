# 5. Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером 32 и заканчивая 127-м включительно.
# Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке.
k = 0
for i in range(32, 128):
    k += 1
    print(i, chr(i), end=' ')
    if k % 10 == 0:
        print()
