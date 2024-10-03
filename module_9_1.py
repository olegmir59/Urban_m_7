#  Домашнее задание по теме "Введение в функциональное программирование"
# Цель: научиться обращаться к функциям, как к объекту и передавать их в другие функции для вызова.
#
# Задача "Вызов разом":

def apply_all_func(int_list, *functions):
    result = {}
    for func_ in functions:
        result[func_.__name__] = func_(int_list)
    return result


print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))