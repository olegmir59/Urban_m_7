#  Домашнее задание по теме "Создание исключений".
#  Цель: освоить навык создания пользовательских исключений и использовать его в решении задачи. Повторить тему ООП и принцип инкапсуляции.
#
# Задача "Некорректность":


#          Так хотелось сделать сначала !!!
#   def __new__(cls,  model, vin, numbers):
#        if cls.__is_valid_vin(vin):
#            if cls.__is_valid_numbers(numbers):
#                 return super().__new__(cls)

class Car():
    def __init__(self, *args):
       # print(*args, "__init__(cls, *args)")
        self.model = args[0]
        self.__vin = args[1]
        self.__numbers = args[2]

    def __is_valid_vin(cls, *args):
        #print(*args, '__is_valid_vin(cls, *args)')
        vin = args[0]
        if not isinstance(vin, int):
            raise IncorrectVinNumber('Некорректный тип vin номер')
        else:
            if vin not in range(1000000,9999999):
                raise IncorrectVinNumber('Неверный диапазон для vin номера')
            else:
                return True

    def __is_valid_numbers(cls, *args):
        #print(*args, '__is_valid_numbers(cls, *args)')
        numbers = args[1]
        if not isinstance(numbers, str):
            raise IncorrectCarNumbers('Некорректный тип данных для номеров')
        else:
            if len(numbers) != 6:
                raise IncorrectCarNumbers('Неверная длина номера')
            else:
                return True

    def __new__(cls, *args):
        #print(*args,"__new__(cls, *args)")
        if cls.__is_valid_vin(*args):
            if cls.__is_valid_numbers(*args):
                 return super().__new__(cls)



class IncorrectVinNumber(Exception):
    def __init__(self, message):
        self.message = message


class IncorrectCarNumbers(Exception):
    def __init__(self, message):
        self.message = message


try:
  first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{first.model} успешно создан')

try:
  second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{second.model} успешно создан')

try:
  third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{third.model} успешно создан')