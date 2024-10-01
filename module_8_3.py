#  Домашнее задание по теме "Создание исключений".
#  Цель: освоить навык создания пользовательских исключений и использовать его в решении задачи. Повторить тему ООП и принцип инкапсуляции.
#
# Задача "Некорректность":


#          Так хотелось сделать сначала !!!
#   def __new__(cls,  model, vin, numbers):
#        if cls.__is_valid_vin(vin):
#            if cls.__is_valid_numbers(numbers):
#                pass

class Car:
    def __init__(self, model, vin, numbers):
             self.model = model
             self.__vin = vin
             self.__numbers = numbers
             if self.__is_valid_vin(self.__vin):
                if self.__is_valid_numbers(self.__numbers):
                   pass

    def __is_valid_vin(self,vin_number):
        if not isinstance(vin_number, int):
            raise IncorrectVinNumber('Некорректный тип vin номер')
        else:
            if vin_number not in range(1000000,9999999):
                raise IncorrectVinNumber('Неверный диапазон для vin номера')
            else:
                return True

    def __is_valid_numbers(self,numbers):
        if not isinstance(numbers, str):
            raise IncorrectCarNumbers('Некорректный тип данных для номеров')
        else:
            if len(numbers) != 6:
                raise IncorrectCarNumbers('Неверная длина номера')
            else:
                return True

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