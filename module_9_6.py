#  Домашнее задание по теме "Генераторы"
# Цель: более глубоко понять особенности работы с функциями генераторами и оператором yield в Python.

def all_variants(text):
    for x in range(1,len(text)+1):       # длина подпоследовательности
        for y in range(len(text)-x+1):   # начало подпоследовательности
            yield text[y: y + x]

a = all_variants("012345678")
for i in a:
    print(i)

a = all_variants("abc")
for i in a:
    print(i)