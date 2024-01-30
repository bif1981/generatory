# Домашнее задание по теме "Генераторы"

# Цель работы
# Более глубоко понять особенности работы с функциями генераторами и оператором yield в Python.

# Задание
# Напишите функцию-генератор all_variants, которая будет возвращать все подпоследовательности переданной строки. В
# функцию передаётся только сама строка.

# Примечание
# Используйте оператор yield

# Входные данные
# a = all_variants("abc")
# for i in a:
# print(i)

# Выходные данные
# a
# b
# c
# ab
# bc
# abc

from more_itertools import substrings

print('--------------------------------------------------')
print('Решение способом 1:')
def all_variants(string):
    for element in substrings(string):
        yield element


a = all_variants("abc")
for i in a:
    print(i)

print('--------------------------------------------------')


print('Решение способом 2:')
def all_variants(string):
    for i in range(len(string)):
        for j in range(i + 1, len(string) + 1):
            yield string[i:j]


a = all_variants("abc")
for i in a:
    print(i)
print('--------------------------------------------------')


import itertools
print('Решение способом 3:')
def all_variants(string):
    n = len(string)
    for i in range(1, n+1):
        for combination in itertools.combinations(string, i):
            yield ''.join(combination)


for i in all_variants('abc'):
    print(i)
print('--------------------------------------------------')