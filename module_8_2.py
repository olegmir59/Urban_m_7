#  Домашнее задание по теме "Сложные моменты и исключения в стеке вызовов функции".
# Цель: понять как работают исключения внутри функций и как обрабатываются эти исключения на практике при помощи try-except.
# Задача "План перехват":

def personal_sum(numbers):
    result = 0
    incorrect_data = 0
    number_inp = 0

    for num_ in numbers:
        try:
            number_inp = num_
            result += num_
        except TypeError as err:
            print(f"В numbers записан некорректный тип данных - {number_inp}")
            incorrect_data +=1
    return (result, incorrect_data)

def calculate_average(numbers):
    result = 0
    if type(numbers) is list  or type(numbers)is tuple or type(numbers) is str:
        #isinstance(numbers, (list, tuple))
        len_numbers = len(numbers)
    else:
        numbers = []
        len_numbers = 0

    try:
        numbers_sum, err_count = personal_sum(numbers)
        if float(numbers_sum) == 0. and err_count >0:
            return 0.
        result =numbers_sum / (len_numbers - err_count)
    except ZeroDivisionError as err2:
        print(f"Коллекция numbers оказалась пустой - {err2}")
        result = None
    finally:
        return result

print(f'Результат 1: {calculate_average("1, 2, 3")}') # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}') # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}') # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}') # Всё должно работать