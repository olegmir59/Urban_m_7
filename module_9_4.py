#  Домашнее задание по теме "Создание функций на лету"
# Цель: освоить на практике замыкание, объекты-функторы и lambda-функции.
#
# Задача "Функциональное разнообразие":
# Lambda-функция:

from random import choice

first  = 'Мама мыла раму'
second = 'Рамена мало было'

lam_ = lambda x, y: x == y
list_ = list(map(lam_, first, second))

def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, mode='w', encoding='utf8') as file:
            if len(data_set) > 0:
                for item in data_set:
                    if isinstance(item, str):
                        file.write(item + "\n")
                    else:
                        # if isinstance(item, (list, tuple, set, dict)):
                        file.write(str(item) + "\n")
    return write_everything


class MysticBall:
    def __init__(self,*words):
        self.words = words

    def __call__(self):
        return choice(self.words)


print(list_)

write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'],(22,222),{22:44})

first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())
print(first_ball())
print(first_ball())
print(first_ball())
