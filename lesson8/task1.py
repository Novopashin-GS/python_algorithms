# 1. Определение количества различных подстрок с использованием хэш-функции. Пусть дана строка S длиной N,
# состоящая только из маленьких латинских букв. Требуется найти количество различных подстрок в этой строке.
import hashlib
my_dict = {}


def count_sub(substring, my_str):
    global my_dict
    count = 0
    len_sub = len(substring)
    h_sub = hashlib.sha1(substring.encode('utf-8')).hexdigest()
    for i in range(len(my_str) - len_sub + 1):
        if h_sub == hashlib.sha1(my_str[i:i + len_sub].encode('utf-8')).hexdigest():
            count += 1
    my_dict.setdefault(substring, count)


def sub(my_str):
    n = 1
    while len(my_str[:n]) != len(my_str):
        for i in range(len(my_str) - len(my_str[:n]) + 1):
            count_sub(my_str[i:n+i], my_str)
        n += 1
    return my_dict


print(sub('abcdagfasf'))
