#  Домашнее задание по теме "Очереди для обмена данными между потоками."
#  Цель: Применить очереди в работе с потоками, используя класс Queue.
#
# Задача "Потоки гостей в кафе":

import time
from collections import defaultdict

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
        while not self.cafe_queue.empty() and self.find_free_tables(False) is not []:
            pass
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
#cafe.discuss_guests()