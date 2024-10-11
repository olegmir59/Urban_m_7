#  Домашнее задание по теме "Очереди для обмена данными между потоками."
#  Цель: Применить очереди в работе с потоками, используя класс Queue.
#
# Задача "Потоки гостей в кафе":

import time
#from collections import defaultdict
import queue
import random
from threading import Thread


#import threading.Thread


class Table:

    def __init__(self,number):
        self.number = number
        self.guest = None


class Guest(Thread):

    def __init__(self,name):
        super().__init__()
        self.name = name

    def run(self):
        guest_move_time = random.randint(3,10)
        time.sleep(guest_move_time)


class Cafe:
    def __init__(self,*tables):
        self.tables = tables
        self.cafe_queue = queue.Queue(maxsize=20)


#   Поиск свободных столиков.
#   Если find_flag = True  возвращает список свободных столиков
#   Если find_flag = False возвращает список занятых столиков
    def find_free_tables(self,find_flag):
        list_free_tables = []
        list_tables_with_guest =[]
        for table in self.tables:
            if table.guest is None:
                list_free_tables.append(table)
            else:
                list_tables_with_guest.append(table)
        if find_flag:
            return list_free_tables
        else:
            return list_tables_with_guest

    def guest_arrival(self, *guests):
        list_guests = list(guests)
        for table in self.find_free_tables(True):
            if len(list_guests) > 0:
                table.guest = list_guests.pop(0)
                print(f"{table.guest.name} сел(-а) за стол номер {table.number}")
                table.guest.start()         # поток гостя запущен
        while len(list_guests) > 0:
                g_ = list_guests.pop(0)
                self.cafe_queue.put(g_)
                print(f"{g_.name} в очереди")

    def discuss_guests(self):
        while len(self.find_free_tables(False)) > 0:
            for table in self.find_free_tables(False):
                if not table.guest.is_alive():
                    print(f"{table.guest.name} покушал(-а) и ушёл(ушла)")
                    print(f"Стол номер {table.number}  свободен")
                    table.guest = None

            if not self.cafe_queue.empty() and len(self.find_free_tables(True)) > 0:
                for table in self.find_free_tables(True):
                    table.guest = self.cafe_queue.get()
                    print(f"{table.guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}")
                    table.guest.start()  # поток гостя запущен

# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()